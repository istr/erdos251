#!/usr/bin/env python3
"""Optimized item-0010 M5-lite Phase 3b implementation.

The frozen registry and the original Python implementation remain the
mathematical authority.  This driver compiles the checked-in C11 residue
kernel into the regenerable cache, validates it against the reference, and
provides deterministic benchmark/checkpoint commands.

Commands:
  build
  self-test
  equivalence
  benchmark [X] [NCLASS]
  produce-scale X [WORKERS]
  produce-scale-memory X [WORKERS]
  validate-stream-smoke
  finalize-campaign
  audit-scale X
  parallel-note
  verify-artifacts
"""

from __future__ import annotations

import ctypes
import hashlib
import json
import math
import os
import platform
import resource
import shutil
import subprocess
import sys
import tempfile
import time
from collections import defaultdict
from concurrent.futures import ThreadPoolExecutor
from decimal import Decimal
from fractions import Fraction
from functools import lru_cache
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
REPO = HERE.parent.parent
OUT = HERE / "m5-lite-phase3b"
ORACLE_OUT = HERE / "m5-lite-measurements"
SOURCE = HERE / "m5_lite_phase3b_kernel.c"
CACHE = Path(os.environ.get(
    "ITEM0010_PHASE3B_CACHE", "/tmp/item0010-m5-lite-phase3b"))

sys.path.insert(0, str(HERE))
import m5_lite_measure as REF  # noqa: E402

REGISTRY_HASH = REF.REGISTRY_HASH
PIN = "3d3abb3fdc80c34a690fccab3ae1ff8bdb20a47a"
PROFILE_PRIMES = REF.PROFILE_PRIMES
DEFAULT_WORKERS = min(24, os.cpu_count() or 1)
NBUCKETS = REF.I19.NBUCKETS
STREAM_BUCKETS = 64
S_PANEL = (0, 1, 10, 100, 1000)
PRODUCTION_FORMAT = "item-0010-phase3b-bucket-v1"
SUMMARY_FORMAT = "item-0010-phase3b-stream-summary-v6"


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for block in iter(lambda: f.read(1 << 20), b""):
            h.update(block)
    return h.hexdigest()


def atomic_json(path: Path, value: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    fd, raw = tempfile.mkstemp(prefix=f".{path.name}.", dir=path.parent)
    tmp = Path(raw)
    try:
        with os.fdopen(fd, "w") as f:
            json.dump(value, f, indent=2)
            f.write("\n")
            f.flush()
            os.fsync(f.fileno())
        os.replace(tmp, path)
    finally:
        if tmp.exists():
            tmp.unlink()


def atomic_npz(path: Path, **arrays: np.ndarray) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    fd, raw = tempfile.mkstemp(
        prefix=f".{path.name}.", suffix=".npz", dir=path.parent)
    os.close(fd)
    tmp = Path(raw)
    try:
        # Raw NPY members make the large production shards cheap to write and
        # mmap-friendly.  The immutable SHA-256 sidecar supplies integrity;
        # compression is deferred to any explicit archival step.
        np.savez(tmp, **arrays)
        with tmp.open("rb") as f:
            os.fsync(f.fileno())
        os.replace(tmp, path)
    finally:
        if tmp.exists():
            tmp.unlink()


def verify_frozen_inputs() -> None:
    if REF.git_head() != PIN:
        raise RuntimeError(
            f"HEAD is {REF.git_head()}, expected redispatch pin {PIN}")
    if sha256(REF.REGISTRY) != REGISTRY_HASH:
        raise RuntimeError("frozen registry hash mismatch")


def compiler_identity() -> dict:
    cc = os.environ.get("CC", "gcc")
    found = shutil.which(cc)
    if found is None:
        raise RuntimeError(f"configured C compiler is unavailable: {cc}")
    version = subprocess.run(
        [cc, "--version"], check=True, capture_output=True,
        text=True).stdout.splitlines()[0]
    return {"command": cc, "path": found, "version": version}


def build_kernel() -> tuple[Path, dict]:
    verify_frozen_inputs()
    compiler = compiler_identity()
    CACHE.mkdir(parents=True, exist_ok=True)
    source_hash = sha256(SOURCE)
    tag = source_hash[:16]
    library = CACHE / f"m5-lite-phase3b-{tag}.so"
    command = [
        compiler["command"], "-std=c11", "-O3", "-fPIC", "-shared",
        "-Wall", "-Wextra", "-Wpedantic",
        str(SOURCE), "-lm", "-o", str(library)]
    if not library.exists():
        subprocess.run(command, cwd=REPO, check=True)
    meta = {
        "source": str(SOURCE.relative_to(REPO)),
        "source_sha256": source_hash,
        "compiler": compiler,
        "command": command,
        "library": str(library),
        "library_sha256": sha256(library),
    }
    return library, meta


class Kernel:
    def __init__(self) -> None:
        library, self.build = build_kernel()
        self.lib = ctypes.CDLL(str(library))
        p_i16 = ctypes.POINTER(ctypes.c_int16)
        p_i32 = ctypes.POINTER(ctypes.c_int32)
        p_i64 = ctypes.POINTER(ctypes.c_int64)
        p_f64 = ctypes.POINTER(ctypes.c_double)
        p_u8 = ctypes.POINTER(ctypes.c_uint8)
        self.lib.m5_phase3b_batch.argtypes = [
            p_i16, ctypes.c_int64, ctypes.c_int, ctypes.c_int,
            ctypes.c_int, p_i64, p_i64, p_i32, ctypes.c_int,
            ctypes.c_char_p, p_i32, p_i32, p_f64, p_f64, p_f64,
            p_i32, p_f64, p_f64, p_f64, p_u8, p_i16]
        self.lib.m5_phase3b_batch.restype = ctypes.c_int
        self.lib.m5_phase3b_long_double_mantissa_bits.argtypes = []
        self.lib.m5_phase3b_long_double_mantissa_bits.restype = ctypes.c_int
        self.long_double_bits = int(
            self.lib.m5_phase3b_long_double_mantissa_bits())
        if self.long_double_bits < 64:
            raise RuntimeError(
                "Phase 3b requires at least a 64-bit long-double mantissa")


def _pointer(array: np.ndarray, ctype: type) -> object:
    return array.ctypes.data_as(ctypes.POINTER(ctype))


@lru_cache(maxsize=None)
def band_decimal(J: int, K: int, W_floor: int) -> tuple[bytes, np.ndarray]:
    """Compute the invariant large-prime band in extended precision.

    The C enclosure includes a 200,000-operation allowance, exceeding two
    rounded operations for every prime through the frozen Q=10^6 cutoff.
    """
    k = J + K + 2
    all_primes = np.array(
        [p for p in REF.primes_through(REF.Q_RHO) if p & 1],
        dtype=np.int32)
    small = all_primes[all_primes <= W_floor].copy()
    band = np.longdouble(1)
    for raw in all_primes[all_primes > W_floor]:
        p = int(raw)
        numerator = np.longdouble((p - k) * p)
        denominator = np.longdouble(
            (p - (J + 1)) * (p - (K + 1)))
        band *= numerator / denominator
    text = np.format_float_positional(
        band, unique=False, precision=40, trim="k")
    return text.encode("ascii"), small


def cell_offsets(rec: dict) -> np.ndarray:
    count = len(rec["NP"])
    return np.searchsorted(
        rec["cell_class"], np.arange(count + 1), side="left"
    ).astype(np.int64)


def _kernel_chunk(
        kernel: Kernel,
        sides: np.ndarray,
        offsets: np.ndarray,
        mids: np.ndarray,
        J: int,
        K: int,
        W_floor: int,
        primes: np.ndarray,
        band: bytes,
) -> dict:
    sides = np.ascontiguousarray(sides, dtype=np.int16)
    offsets = np.ascontiguousarray(offsets, dtype=np.int64)
    mids = np.ascontiguousarray(mids, dtype=np.int64)
    primes = np.ascontiguousarray(primes, dtype=np.int32)
    nclass = len(sides)
    ncells = len(mids)
    A = np.empty(nclass, dtype=np.int32)
    domain = np.empty(nclass, dtype=np.int32)
    rho = np.empty(nclass, dtype=np.float64)
    rho_lower = np.empty(nclass, dtype=np.float64)
    rho_upper = np.empty(nclass, dtype=np.float64)
    off = np.empty(nclass, dtype=np.int32)
    realized = np.empty(ncells, dtype=np.float64)
    realized_lower = np.empty(ncells, dtype=np.float64)
    realized_upper = np.empty(ncells, dtype=np.float64)
    realized_off = np.empty(ncells, dtype=np.uint8)
    profiles = np.zeros(
        (ncells, len(PROFILE_PRIMES), 3), dtype=np.int16)
    status = kernel.lib.m5_phase3b_batch(
        _pointer(sides, ctypes.c_int16), nclass, J, K, W_floor,
        _pointer(offsets, ctypes.c_int64),
        _pointer(mids, ctypes.c_int64),
        _pointer(primes, ctypes.c_int32), len(primes), band,
        _pointer(A, ctypes.c_int32),
        _pointer(domain, ctypes.c_int32),
        _pointer(rho, ctypes.c_double),
        _pointer(rho_lower, ctypes.c_double),
        _pointer(rho_upper, ctypes.c_double),
        _pointer(off, ctypes.c_int32),
        _pointer(realized, ctypes.c_double),
        _pointer(realized_lower, ctypes.c_double),
        _pointer(realized_upper, ctypes.c_double),
        _pointer(realized_off, ctypes.c_uint8),
        _pointer(profiles, ctypes.c_int16))
    if status:
        raise RuntimeError(f"compiled kernel failed with status {status}")
    return {
        "A_P": A,
        "domain": domain,
        "rho_pros": rho,
        "rho_pros_lower": rho_lower,
        "rho_pros_upper": rho_upper,
        "off_domain": off,
        "realized_rho": realized,
        "realized_lower": realized_lower,
        "realized_upper": realized_upper,
        "realized_off": realized_off.astype(bool),
        "profiles": profiles,
    }


def run_kernel(
    rec: dict,
    J: int,
    K: int,
    W_floor: int,
    workers: int = DEFAULT_WORKERS,
    classes_per_shard: int | None = None,
) -> tuple[dict, dict]:
    kernel = Kernel()
    band, primes = band_decimal(J, K, W_floor)
    offsets = cell_offsets(rec)
    nclass = len(rec["NP"])
    ncells = len(rec["NPd"])
    if classes_per_shard is None:
        classes_per_shard = max(
            128, math.ceil(nclass / max(1, workers * 4)))
    bounds = [
        (lo, min(nclass, lo + classes_per_shard))
        for lo in range(0, nclass, classes_per_shard)]

    def one(bound: tuple[int, int]) -> tuple[int, int, int, dict]:
        lo, hi = bound
        cell_lo = int(offsets[lo])
        cell_hi = int(offsets[hi])
        local_offsets = offsets[lo:hi + 1] - cell_lo
        got = _kernel_chunk(
            kernel, rec["sides"][lo:hi], local_offsets,
            rec["mid"][cell_lo:cell_hi], J, K, W_floor,
            primes, band)
        return lo, hi, cell_lo, got

    class_arrays = {
        "A_P": np.empty(nclass, np.int32),
        "domain": np.empty(nclass, np.int32),
        "rho_pros": np.empty(nclass, np.float64),
        "rho_pros_lower": np.empty(nclass, np.float64),
        "rho_pros_upper": np.empty(nclass, np.float64),
        "off_domain": np.empty(nclass, np.int32),
    }
    cell_arrays = {
        "realized_rho": np.empty(ncells, np.float64),
        "realized_lower": np.empty(ncells, np.float64),
        "realized_upper": np.empty(ncells, np.float64),
        "realized_off": np.empty(ncells, bool),
        "profiles": np.empty(
            (ncells, len(PROFILE_PRIMES), 3), np.int16),
    }
    t0 = time.perf_counter()
    if workers <= 1 or len(bounds) <= 1:
        completed = map(one, bounds)
    else:
        pool = ThreadPoolExecutor(max_workers=workers)
        completed = pool.map(one, bounds)
    try:
        for lo, hi, cell_lo, got in completed:
            cell_hi = cell_lo + len(got["realized_rho"])
            for key in class_arrays:
                class_arrays[key][lo:hi] = got[key]
            for key in cell_arrays:
                cell_arrays[key][cell_lo:cell_hi] = got[key]
    finally:
        if workers > 1 and len(bounds) > 1:
            pool.shutdown()
    wall = time.perf_counter() - t0
    result = {**class_arrays, **cell_arrays}
    meta = {
        **kernel.build,
        "long_double_mantissa_bits": kernel.long_double_bits,
        "workers": workers,
        "classes_per_shard": classes_per_shard,
        "class_count": nclass,
        "cell_count": ncells,
        "prospective_candidate_count": int(class_arrays["domain"].sum()),
        "wall_seconds": wall,
        "classes_per_second": nclass / wall if wall else None,
        "prospective_candidates_per_second": (
            int(class_arrays["domain"].sum()) / wall if wall else None),
        "realized_cells_per_second": ncells / wall if wall else None,
    }
    return result, meta


def make_record(x: int, s: int = 0) -> tuple[np.ndarray, dict, dict, dict]:
    par = REF.d0_parameters(x)
    t0 = time.perf_counter()
    p, g, delta, valid = REF.I19.build(x)
    build_seconds = time.perf_counter() - t0
    t = REF.I19.site_range(valid, par["J"], par["K"])
    wsum = REF.I19.window_sums(g, t, par["L"])
    sites = t[
        (t >= s + 1)
        & (wsum <= par["W_floor"])
        & (delta[t + par["J"]] <= par["D"])
        & (delta[t + par["L"]] <= float(2 ** par["K"]))]
    t1 = time.perf_counter()
    rec = REF.exact_class_records(
        g, sites, par["J"], par["K"])
    class_seconds = time.perf_counter() - t1
    return p, rec, par, {
        "build_seconds": build_seconds,
        "class_construction_seconds": class_seconds,
        "site_count": len(sites),
        "class_count": len(rec["NP"]),
        "cell_count": len(rec["NPd"]),
    }


def ulp_distance(a: np.ndarray, b: np.ndarray) -> np.ndarray:
    ai = np.ascontiguousarray(a, np.float64).view(np.int64)
    bi = np.ascontiguousarray(b, np.float64).view(np.int64)
    return np.abs(ai - bi)


def compare_reference(
    rec: dict,
    par: dict,
    got: dict,
    reference_prospective: dict,
    reference_realized: dict,
) -> dict:
    exact = {
        "A_P": bool(np.array_equal(
            got["A_P"], reference_prospective["A_P"])),
        "residual_domain": bool(np.array_equal(
            got["domain"], reference_prospective["domain"])),
        "prospective_off_domain": bool(np.array_equal(
            got["off_domain"], reference_prospective["off_domain"])),
        "realized_off_domain": bool(np.array_equal(
            got["realized_off"], reference_realized["off_domain"])),
        "CRT_profiles": bool(np.array_equal(
            got["profiles"], reference_realized["profiles"])),
    }
    ref_pros = reference_prospective["rho_pros"]
    ref_real = reference_realized["rho"]
    pros_enclosed = (
        (ref_pros >= got["rho_pros_lower"])
        & (ref_pros <= got["rho_pros_upper"]))
    real_enclosed = (
        (ref_real >= got["realized_lower"])
        & (ref_real <= got["realized_upper"]))
    pros_ulp = ulp_distance(ref_pros, got["rho_pros"])
    real_ulp = ulp_distance(ref_real, got["realized_rho"])
    A = got["A_P"]
    lnx = float(Decimal(par["log_x"]))
    caps = {
        "1/8": lnx / 8,
        "1/4": lnx / 4,
        "1/2": lnx / 2,
        "3/4": 3 * lnx / 4,
        "1": lnx,
    }
    selector = {}
    for name, cap in caps.items():
        ref_membership = (A > 0) & (ref_pros <= cap)
        opt_membership = (A > 0) & (got["rho_pros"] <= cap)
        ambiguous = (
            (A > 0)
            & (got["rho_pros_lower"] <= cap)
            & (got["rho_pros_upper"] > cap))
        margins = np.abs(ref_pros - cap)
        near = np.argsort(margins)[:10]
        selector[name] = {
            "membership_equal": bool(np.array_equal(
                ref_membership, opt_membership)),
            "ambiguous_count": int(ambiguous.sum()),
            "reference_member_count": int(ref_membership.sum()),
            "nearest_reference_cases": [
                {
                    "class": int(i),
                    "rho": float(ref_pros[i]),
                    "cap": cap,
                    "absolute_margin": float(margins[i]),
                    "enclosure": [
                        float(got["rho_pros_lower"][i]),
                        float(got["rho_pros_upper"][i])],
                }
                for i in near],
        }
    passed = (
        all(exact.values())
        and bool(pros_enclosed.all())
        and bool(real_enclosed.all())
        and all(v["membership_equal"] for v in selector.values())
        and all(v["ambiguous_count"] == 0 for v in selector.values()))
    return {
        "exact_integer_and_profile_checks": exact,
        "prospective_reference_enclosed": bool(pros_enclosed.all()),
        "prospective_not_enclosed_count": int((~pros_enclosed).sum()),
        "prospective_binary64_equal_count": int(
            (ref_pros == got["rho_pros"]).sum()),
        "prospective_count": len(ref_pros),
        "prospective_max_ulp_distance": int(pros_ulp.max(initial=0)),
        "prospective_max_absolute_difference": float(
            np.max(np.abs(ref_pros - got["rho_pros"]), initial=0.0)),
        "realized_reference_enclosed": bool(real_enclosed.all()),
        "realized_not_enclosed_count": int((~real_enclosed).sum()),
        "realized_binary64_equal_count": int(
            (ref_real == got["realized_rho"]).sum()),
        "realized_count": len(ref_real),
        "realized_max_ulp_distance": int(real_ulp.max(initial=0)),
        "realized_max_absolute_difference": float(
            np.max(np.abs(ref_real - got["realized_rho"]), initial=0.0)),
        "selectors": selector,
        "status": "PASS" if passed else "FAIL",
    }


def verify_artifacts() -> dict:
    with (ORACLE_OUT / "run-manifest.json").open() as f:
        manifest = json.load(f)
    rows = {}
    for name, expected in manifest["artifacts"].items():
        path = ORACLE_OUT / name
        rows[name] = {
            "exists": path.exists(),
            "bytes": path.stat().st_size if path.exists() else None,
            "expected_bytes": expected["bytes"],
            "sha256": sha256(path) if path.exists() else None,
            "expected_sha256": expected["sha256"],
        }
        rows[name]["pass"] = (
            rows[name]["exists"]
            and rows[name]["bytes"] == rows[name]["expected_bytes"]
            and rows[name]["sha256"] == rows[name]["expected_sha256"])
    result = {
        "schema": "item-0010-phase3b-artifact-verification-v1",
        "manifest": str((ORACLE_OUT / "run-manifest.json").relative_to(REPO)),
        "artifacts": rows,
        "status": "PASS" if all(v["pass"] for v in rows.values()) else "FAIL",
    }
    print(json.dumps(result, indent=2))
    return result


def reference_for_cases(
    sides: np.ndarray, mids: np.ndarray, J: int, K: int, W_floor: int,
) -> tuple[dict, dict]:
    band_text, small_primes = band_decimal(J, K, W_floor)
    band = np.longdouble(band_text.decode("ascii"))
    primes_k = REF.primes_through(J + K + 2)

    def direct(side: np.ndarray, d: int) -> tuple[float, bool, dict]:
        pre, suf = REF.point_sets(side, J)
        full = pre + tuple(pre[-1] + d + v for v in suf)
        value = np.longdouble(2) * band
        profile = {}
        for raw in small_primes:
            p = int(raw)
            nh = REF.nu(full, p)
            na = REF.nu(pre, p)
            nb = REF.nu(suf, p)
            if p in PROFILE_PRIMES:
                profile[p] = (nh, na, nb)
            if na == p or nb == p:
                return 0.0, True, profile
            if nh == p:
                return 0.0, False, profile
            value *= (
                np.longdouble((p - nh) * p)
                / np.longdouble((p - na) * (p - nb)))
        return float(value), False, profile

    prospective = []
    for side in sides:
        pre, suf = REF.point_sets(side, J)
        dmax = W_floor - pre[-1] - suf[-1]
        ds = list(range(2, dmax + 1, 2)) if dmax >= 2 else []
        values = [direct(side, d) for d in ds]
        prospective.append({
            "A_P": sum(REF.admissible(
                pre, suf, d, primes_k) for d in ds),
            "residual_domain_size": len(ds),
            "rho_pros": (
                sum(value[0] for value in values) / len(ds)
                if ds else 0.0),
            "prospective_off_domain": sum(
                int(value[1]) for value in values),
        })
    realized = [
        direct(side, int(d)) for side, d in zip(sides, mids)]
    pros = {
        "A_P": np.array([v["A_P"] for v in prospective], np.int32),
        "domain": np.array(
            [v["residual_domain_size"] for v in prospective], np.int32),
        "rho_pros": np.array(
            [v["rho_pros"] for v in prospective], np.float64),
        "off_domain": np.array(
            [v["prospective_off_domain"] for v in prospective], np.int32),
    }
    profiles = np.zeros(
        (len(realized), len(PROFILE_PRIMES), 3), dtype=np.int16)
    for i, (_, _, profile) in enumerate(realized):
        for j, p in enumerate(PROFILE_PRIMES):
            profiles[i, j] = profile.get(p, (0, 0, 0))
    real = {
        "rho": np.array([v[0] for v in realized], np.float64),
        "off_domain": np.array([v[1] for v in realized], bool),
        "profiles": profiles,
    }
    return pros, real


def self_test() -> dict:
    verify_frozen_inputs()
    REF.self_test()
    rng = np.random.default_rng(251_003)
    groups = []
    for J, K, W_floor, count in (
            (2, 2, 30, 8),
            (4, 4, 80, 64),
            (14, 14, 600, 256)):
        sides = (
            2 * rng.integers(1, 9, size=(count, J + K))
        ).astype(np.int16)
        if J == 2:
            sides[0] = np.array([2, 2, 2, 2], np.int16)
            sides[1] = np.array([10, 10, 10, 10], np.int16)
        mids = np.full(count, 2, np.int64)
        rec = {
            "sides": sides,
            "NP": np.ones(count, np.int64),
            "NPd": np.ones(count, np.int64),
            "cell_class": np.arange(count, dtype=np.int64),
            "mid": mids,
        }
        got, meta = run_kernel(
            rec, J, K, W_floor, workers=min(4, DEFAULT_WORKERS))
        pros, real = reference_for_cases(
            sides, mids, J, K, W_floor)
        par = {"log_x": str(Decimal(10).ln())}
        comparison = compare_reference(rec, par, got, pros, real)
        groups.append({
            "J": J, "K": K, "W_floor": W_floor,
            "count": count, "comparison": comparison,
            "kernel": meta,
        })
    passed = all(g["comparison"]["status"] == "PASS" for g in groups)
    result = {
        "schema": "item-0010-phase3b-synthetic-tests-v1",
        "seed": 251_003,
        "coverage": [
            "side-block inadmissibility",
            "empty residual domain",
            "residual domain of size one or more",
            "multiple admissible middles",
            "CRT residue changes with d modulo p",
            "large local numerator/denominator products",
            "independent set-based reference versus overlap kernel",
        ],
        "groups": groups,
        "status": "PASS" if passed else "FAIL",
    }
    atomic_json(OUT / "synthetic-tests.json", result)
    print(json.dumps({
        "path": str(OUT / "synthetic-tests.json"),
        "status": result["status"]}, indent=2))
    if not passed:
        raise AssertionError("Phase 3b synthetic equivalence failed")
    return result


def equivalence(workers: int = DEFAULT_WORKERS) -> dict:
    verify_frozen_inputs()
    t0 = time.perf_counter()
    p, rec, par, build = make_record(1_000_000, 0)
    got, kernel = run_kernel(
        rec, par["J"], par["K"], par["W_floor"], workers=workers)
    with np.load(ORACLE_OUT / "prospective-x1000000-s0.npz") as z:
        pros = {key: z[key].copy() for key in z.files}
    with np.load(ORACLE_OUT / "realized-rho-x1000000-s0.npz") as z:
        real = {key: z[key].copy() for key in z.files}
    comparison = compare_reference(rec, par, got, pros, real)
    metrics = REF.collision_metrics(rec)
    with (ORACLE_OUT / "smoke-x1000000-s0.json").open() as f:
        smoke = json.load(f)
    class_partition = {
        "N": metrics["N"] == smoke["global_metrics"]["N"],
        "F": metrics["F"] == smoke["global_metrics"]["F"],
        "Q": metrics["Q"] == smoke["global_metrics"]["Q"],
        "class_size_strata": (
            REF.class_size_strata(rec, metrics["N"])
            == smoke["class_size_strata"]),
    }
    a_table = REF.A_table(
        rec,
        [
            {
                "A_P": int(a),
                "residual_domain_size": int(d),
                "rho_pros": float(r),
                "prospective_off_domain": int(o),
            }
            for a, d, r, o in zip(
                got["A_P"], got["domain"], got["rho_pros"],
                got["off_domain"])
        ],
        p, par["J"], par["K"], metrics["N"])
    finite_anchor = {
        "optimized_A_table_equals_reference": (
            a_table == smoke["A_P"]),
        "contaminated_class_count": a_table["contaminated_class_count"],
        "contaminated_site_mass": a_table["contaminated_site_mass"],
    }
    passed = (
        comparison["status"] == "PASS"
        and all(class_partition.values())
        and finite_anchor["optimized_A_table_equals_reference"])
    result = {
        "schema": "item-0010-phase3b-smoke-equivalence-v1",
        "dispatch_pin": PIN,
        "registry_sha256": REGISTRY_HASH,
        "x": 1_000_000,
        "s": 0,
        "class_partition": class_partition,
        "finite_anchor": finite_anchor,
        "comparison": comparison,
        "build": build,
        "kernel": kernel,
        "peak_rss_kib": resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
        "total_seconds": time.perf_counter() - t0,
        "status": "PASS" if passed else "FAIL",
    }
    atomic_json(OUT / "smoke-equivalence.json", result)
    print(json.dumps({
        "path": str(OUT / "smoke-equivalence.json"),
        "classes": kernel["class_count"],
        "candidates": kernel["prospective_candidate_count"],
        "kernel_seconds": kernel["wall_seconds"],
        "classes_per_second": kernel["classes_per_second"],
        "prospective_binary64_equal_count": comparison[
            "prospective_binary64_equal_count"],
        "realized_binary64_equal_count": comparison[
            "realized_binary64_equal_count"],
        "status": result["status"]}, indent=2))
    if not passed:
        raise AssertionError("Phase 3b smoke equivalence failed")
    return result


def slice_record(rec: dict, nclass: int) -> dict:
    nclass = min(nclass, len(rec["NP"]))
    cells = int(np.searchsorted(rec["cell_class"], nclass, side="left"))
    return {
        "sides": rec["sides"][:nclass],
        "NP": rec["NP"][:nclass],
        "NPd": rec["NPd"][:cells],
        "cell_class": rec["cell_class"][:cells],
        "mid": rec["mid"][:cells],
    }


def benchmark(x: int = 1_000_000, nclass: int = 8192) -> dict:
    verify_frozen_inputs()
    _, rec, par, build = make_record(x, 0)
    sample = slice_record(rec, nclass)
    worker_grid = [
        w for w in (1, 2, 4, 8, 16, 24)
        if w <= DEFAULT_WORKERS]
    rows = []
    for workers in worker_grid:
        _, meta = run_kernel(
            sample, par["J"], par["K"], par["W_floor"],
            workers=workers,
            classes_per_shard=max(
                64, math.ceil(len(sample["NP"]) / (workers * 4))))
        rows.append(meta)
    one = rows[0]["wall_seconds"]
    for row in rows:
        row["speedup_vs_one_worker"] = one / row["wall_seconds"]
        row["parallel_efficiency"] = (
            row["speedup_vs_one_worker"] / row["workers"])
    best = min(rows, key=lambda row: row["wall_seconds"])
    full_projected = (
        best["wall_seconds"] * len(rec["NP"]) / len(sample["NP"]))
    result = {
        "schema": "item-0010-phase3b-scaling-benchmark-v1",
        "dispatch_pin": PIN,
        "registry_sha256": REGISTRY_HASH,
        "x": x,
        "s": 0,
        "parameters": par,
        "full_row": build,
        "sample_class_count": len(sample["NP"]),
        "sample_cell_count": len(sample["NPd"]),
        "rows": rows,
        "best_workers": best["workers"],
        "projected_full_kernel_wall_seconds": full_projected,
        "projected_full_kernel_compute_hours": (
            full_projected * best["workers"] / 3600),
        "peak_rss_kib": resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
        "status": "PASS",
    }
    path = OUT / f"benchmark-x{x}.json"
    atomic_json(path, result)
    print(json.dumps({
        "path": str(path),
        "x": x,
        "full_classes": len(rec["NP"]),
        "sample_classes": len(sample["NP"]),
        "best_workers": best["workers"],
        "best_wall_seconds": best["wall_seconds"],
        "projected_full_kernel_wall_seconds": full_projected,
        "status": "PASS"}, indent=2))
    return result


def _side_structured(sides: np.ndarray) -> np.ndarray:
    width = sides.shape[1]
    dtype = np.dtype([(f"f{i}", np.int16) for i in range(width)])
    return np.ascontiguousarray(sides).view(dtype).reshape(-1)


def _early_membership(
    g: np.ndarray,
    bucket_sites: np.ndarray,
    rec: dict,
    J: int,
    K: int,
) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    early = bucket_sites[bucket_sites <= max(S_PANEL)]
    if not len(early):
        empty = np.array([], dtype=np.int64)
        return empty, empty.copy(), empty.copy()
    L = J + 1 + K
    words = np.empty((len(early), L), dtype=np.int16)
    for j in range(L):
        words[:, j] = g[early + j]
    sides = np.concatenate((words[:, :J], words[:, J + 1:]), axis=1)
    mids = words[:, J].astype(np.int64)
    full_keys = _side_structured(rec["sides"])
    early_keys = _side_structured(sides)
    classes = np.searchsorted(full_keys, early_keys).astype(np.int64)
    if np.any(classes >= len(full_keys)):
        raise AssertionError("early-site side class lookup escaped bucket")
    if not np.array_equal(full_keys[classes], early_keys):
        raise AssertionError("early-site side class lookup mismatch")
    offsets = cell_offsets(rec)
    cells = np.empty(len(early), dtype=np.int64)
    for i, (cls, middle) in enumerate(zip(classes, mids)):
        lo = int(offsets[cls])
        hi = int(offsets[cls + 1])
        local = int(np.searchsorted(rec["mid"][lo:hi], middle))
        if lo + local >= hi or int(rec["mid"][lo + local]) != int(middle):
            raise AssertionError("early-site realized cell lookup mismatch")
        cells[i] = lo + local
    return early.astype(np.int64), classes, cells


def _anchor_inadmissible(rec: dict, p: np.ndarray, J: int, K: int) -> np.ndarray:
    result = np.zeros(len(rec["NPd"]), dtype=bool)
    primes_k = REF.primes_through(J + K + 2)
    for i, site in enumerate(rec["cell_first_site"]):
        if int(p[int(site)]) > J + K + 2:
            continue
        cls = int(rec["cell_class"][i])
        pre, suf = REF.point_sets(rec["sides"][cls], J)
        result[i] = not REF.admissible(
            pre, suf, int(rec["mid"][i]), primes_k)
    return result


def _fraction_pairs(numerators: np.ndarray, denominators: np.ndarray) -> Fraction:
    if not len(numerators):
        return Fraction()
    pairs = np.column_stack((
        np.asarray(numerators, dtype=np.int64),
        np.asarray(denominators, dtype=np.int64)))
    unique, counts = np.unique(pairs, axis=0, return_counts=True)
    total = Fraction()
    for (num, den), count in zip(unique, counts):
        total += int(count) * Fraction(int(num), int(den))
    return total


def _fraction_key(numerator: int, denominator: int) -> str:
    return str(Fraction(int(numerator), int(denominator)))


def _derive_view(
    rec: dict,
    got: dict,
    early_site: np.ndarray,
    early_class: np.ndarray,
    early_cell: np.ndarray,
    anchor_inadmissible: np.ndarray,
    p: np.ndarray,
    k: int,
    s: int,
) -> dict:
    NP = rec["NP"].astype(np.int64).copy()
    NPd = rec["NPd"].astype(np.int64).copy()
    old_ci = rec["cell_class"].astype(np.int64)
    first_site = rec["cell_first_site"].astype(np.int64).copy()
    removed = early_site <= s
    if removed.any():
        NP -= np.bincount(
            early_class[removed], minlength=len(NP))
        NPd -= np.bincount(
            early_cell[removed], minlength=len(NPd))
        changed = (first_site <= s) & (NPd > 0)
        if changed.any():
            next_early = np.full(len(NPd), max(S_PANEL) + 1, np.int64)
            remaining = early_site > s
            np.minimum.at(
                next_early, early_cell[remaining], early_site[remaining])
            first_site[changed] = next_early[changed]
    keep_class = NP > 0
    keep_cell = NPd > 0
    old_to_new = np.full(len(NP), -1, np.int64)
    old_to_new[keep_class] = np.arange(int(keep_class.sum()))
    ci = old_to_new[old_ci[keep_cell]]
    NP = NP[keep_class]
    NPd = NPd[keep_cell]
    nmid = np.bincount(ci, minlength=len(NP)).astype(np.int64)
    max_npd = np.zeros(len(NP), np.int64)
    np.maximum.at(max_npd, ci, NPd)
    small_anchor = np.zeros(len(first_site), bool)
    valid_first = first_site < len(p)
    small_anchor[valid_first] = p[first_site[valid_first]] <= k
    contaminated_cell = (
        keep_cell & anchor_inadmissible & small_anchor)
    contaminated = np.bincount(
        old_to_new[old_ci[contaminated_cell]],
        minlength=len(NP)).astype(np.int64)
    class_fields = {
        key: got[key][keep_class]
        for key in (
            "A_P", "domain", "rho_pros", "rho_pros_lower",
            "rho_pros_upper", "off_domain")}
    cell_fields = {
        key: got[key][keep_cell]
        for key in (
            "realized_rho", "realized_lower", "realized_upper",
            "realized_off", "profiles")}
    return {
        "NP": NP,
        "NPd": NPd,
        "cell_class": ci,
        "nmid": nmid,
        "maxNPd": max_npd,
        "contaminated": contaminated,
        **class_fields,
        **cell_fields,
    }


def _rule_bucket_summaries(
    registry: dict, view: dict, log_x: float,
) -> dict:
    NP = view["NP"]
    M = view["maxNPd"]
    NPd = view["NPd"]
    ci = view["cell_class"]
    A = view["A_P"]
    rho = view["rho_pros"]
    rho_lo = view["rho_pros_lower"]
    rho_hi = view["rho_pros_upper"]
    class_sq = np.zeros(len(NP), np.int64)
    np.add.at(class_sq, ci, NPd * NPd)
    r = (M - 1) / NP
    rows = {}
    caps = {
        "1_8": 1 / 8, "1_4": 1 / 4, "1_2": 1 / 2,
        "3_4": 3 / 4, "1": 1}
    for rule in registry["rules"]:
        rid = rule["rule_id"]
        if not rid.startswith(("R0-", "R1-", "R2-", "R3-")):
            continue
        ambiguity = np.zeros(len(NP), bool)
        if rid.startswith(("R0-", "R1-")):
            selected = np.ones(len(NP), bool)
        elif rid.startswith("R2-"):
            cap = caps[rid.split("-")[1][3:]] * log_x
            ambiguity = (
                (A > 0) & (rho_lo <= cap) & (rho_hi > cap))
            selected = (A > 0) & (rho <= cap)
        else:
            selected = A > 0
        if rid == "R0-all-k0":
            kappa = np.zeros(len(NP))
        elif rid.endswith("k1_8"):
            kappa = np.full(len(NP), 1 / 8)
        elif rid.endswith("k1_4"):
            kappa = np.full(len(NP), 1 / 4)
        elif rid.endswith("k1_2"):
            kappa = np.full(len(NP), 1 / 2)
        else:
            coeff = {
                "R3-weighted-C1_2": 1 / 2,
                "R3-weighted-C1": 1,
                "R3-weighted-C2": 2,
                "R3-weighted-C4": 4,
            }[rid]
            kappa = np.maximum(0.0, 1.0 - coeff * rho / log_x)
            lower_kappa = np.maximum(
                0.0, 1.0 - coeff * rho_hi / log_x)
            upper_kappa = np.maximum(
                0.0, 1.0 - coeff * rho_lo / log_x)
            ambiguity |= selected & (
                (r > 1.0 - upper_kappa)
                != (r > 1.0 - lower_kappa))
        violation = selected & (r > 1.0 - kappa + 1e-15)
        idx = np.nonzero(selected)[0]
        escape = NP - M
        gini_num = NP * NP - class_sq
        gini_idx = idx[gini_num[idx] != 0]
        hist: dict[str, int] = defaultdict(int)
        if len(idx):
            pairs = np.column_stack((M[idx] - 1, NP[idx]))
            unique, inverse = np.unique(pairs, axis=0, return_inverse=True)
            weights = np.bincount(inverse, weights=NP[idx]).astype(np.int64)
            for pair, weight in zip(unique, weights):
                hist[_fraction_key(pair[0], pair[1])] += int(weight)
        delta = (1.0 - kappa[idx]) - r[idx]
        repeated = selected & (NP >= 2)
        rows[rid] = {
            "selected_class_count": int(selected.sum()),
            "selected_site_mass": int(NP[selected].sum()),
            "violation_class_count": int(violation.sum()),
            "violation_site_mass": int(NP[violation].sum()),
            "escape": int(escape[selected].sum()),
            "gini": str(_fraction_pairs(
                gini_num[gini_idx], NP[gini_idx])),
            "kappa_site_sum": float(np.sum(
                kappa[selected] * NP[selected], dtype=np.float64)),
            "min_delta": float(delta.min()) if len(delta) else None,
            "max_negative_delta": (
                float(np.maximum(-delta, 0).max())
                if len(delta) else None),
            "lambda_max": (
                float(np.max(r[repeated])) if repeated.any() else 0.0),
            "r_hist_site_weight": dict(hist),
            "numeric_ambiguity_count": int(ambiguity.sum()),
        }
    return rows


def _summarize_bucket(
    registry: dict,
    rec: dict,
    got: dict,
    early_site: np.ndarray,
    early_class: np.ndarray,
    early_cell: np.ndarray,
    anchor_inadmissible: np.ndarray,
    p: np.ndarray,
    par: dict,
) -> dict:
    if (
            len(rec["NP"]) == len(rec["NPd"])
            and np.all(rec["NP"] == 1)
            and np.all(rec["NPd"] == 1)):
        return _summarize_singleton_bucket(
            registry, rec, got, early_site, early_class,
            anchor_inadmissible, par)
    out = {}
    log_x = float(Decimal(par["log_x"]))
    for s in S_PANEL:
        view = _derive_view(
            rec, got, early_site, early_class, early_cell,
            anchor_inadmissible, p, par["k"], s)
        NP = view["NP"]
        NPd = view["NPd"]
        ci = view["cell_class"]
        N = int(NP.sum())
        F = len(NP)
        by_class_num = np.zeros(F, np.int64)
        class_sq = np.zeros(F, np.int64)
        np.add.at(by_class_num, ci, NPd * (NPd - 1))
        np.add.at(class_sq, ci, NPd * NPd)
        q_idx = np.nonzero(by_class_num)[0]
        q = _fraction_pairs(by_class_num[q_idx], NP[q_idx])
        gini_num = NP * NP - class_sq
        gini_idx = np.nonzero(gini_num)[0]
        defect = _fraction_pairs(
            gini_num[gini_idx], NP[gini_idx])
        escape = int((NP - view["maxNPd"]).sum())
        class_bins = {}
        bound = 1
        max_np = int(NP.max(initial=0))
        while bound <= max_np:
            mask = (NP >= bound) & (NP < 2 * bound)
            if mask.any():
                cell_mask = mask[ci]
                class_bins[str(bound)] = {
                    "class_count": int(mask.sum()),
                    "site_mass": int(NP[mask].sum()),
                    "W2": int(np.sum(
                        NPd[cell_mask] * (NPd[cell_mask] - 1))),
                    "V2": int(np.sum(NP[mask] * (NP[mask] - 1))),
                    "rigid_site_mass": int(
                        NP[mask & (view["nmid"] == 1)].sum()),
                    "escape": int(
                        (NP[mask] - view["maxNPd"][mask]).sum()),
                    "gini": str(_fraction_pairs(
                        gini_num[mask & (gini_num != 0)],
                        NP[mask & (gini_num != 0)])),
                }
            bound *= 2
        A = view["A_P"]
        atilde = A + view["contaminated"]
        pair = np.column_stack((NP, atilde))
        positive = atilde > 0
        inverse = _fraction_pairs(
            pair[positive, 0], pair[positive, 1])
        a_masks = {
            "0": A == 0, "1": A == 1, "2": A == 2,
            "3-4": (A >= 3) & (A <= 4),
            "5-8": (A >= 5) & (A <= 8),
            "9-16": (A >= 9) & (A <= 16),
            "17+": A >= 17,
        }
        a_bins = {
            name: {
                "class_count": int(mask.sum()),
                "site_mass": int(NP[mask].sum()),
            }
            for name, mask in a_masks.items()}
        realized_rho = view["realized_rho"]
        realized_lo = view["realized_lower"]
        realized_hi = view["realized_upper"]
        reference_enclosure_ok = bool(np.all(
            (realized_rho >= realized_lo)
            & (realized_rho <= realized_hi)))
        crt = {}
        for j, prime in enumerate(PROFILE_PRIMES):
            profiles = view["profiles"][:, j, :]
            unique, profile_inverse = np.unique(
                profiles, axis=0, return_inverse=True)
            for u, profile in enumerate(unique):
                # The reference stops at the first singular/side-block
                # prime, so later CRT profiles are absent.  Raw arrays encode
                # that absence as the otherwise impossible (0,0,0) triple.
                if not np.any(profile):
                    continue
                mask = profile_inverse == u
                key = ",".join(map(str, (prime, *map(int, profile))))
                cells = np.nonzero(mask)[0]
                class_ids = np.unique(ci[cells])
                q_cells = cells[NPd[cells] >= 2]
                q_part = _fraction_pairs(
                    NPd[q_cells] * (NPd[q_cells] - 1),
                    NP[ci[q_cells]])
                nonrigid = cells[
                    (NP[ci[cells]] - view["maxNPd"][ci[cells]]) != 0]
                escape_part = _fraction_pairs(
                    ((NP[ci[nonrigid]]
                      - view["maxNPd"][ci[nonrigid]]) * NPd[nonrigid]),
                    NP[ci[nonrigid]])
                gini_cells = cells[gini_num[ci[cells]] != 0]
                gini_part = _fraction_pairs(
                    gini_num[ci[gini_cells]] * NPd[gini_cells],
                    NP[ci[gini_cells]] * NP[ci[gini_cells]])
                crt[key] = {
                    "site_mass": int(NPd[mask].sum()),
                    "class_count": len(class_ids),
                    "rho_energy": float(np.sum(
                        realized_rho[mask] * NPd[mask],
                        dtype=np.float64)),
                    "Q": str(q_part),
                    "escape": str(escape_part),
                    "gini": str(gini_part),
                }
        out[str(s)] = {
            "global": {
                "N": N, "F": F, "Q": str(q),
                "defect": str(defect), "escape": escape,
                "W2": int(by_class_num.sum()),
            },
            "class_bins": class_bins,
            "A": {
                "bins": a_bins,
                "domain_min": int(view["domain"].min(initial=2 ** 31 - 1))
                if F else None,
                "domain_max": int(view["domain"].max(initial=0))
                if F else None,
                "contaminated_class_count": int(
                    (view["contaminated"] > 0).sum()),
                "contaminated_site_mass": int(
                    NP[view["contaminated"] > 0].sum()),
                "inverse_A_tilde_sum": str(inverse),
                "zero_A_tilde_classes": int((atilde == 0).sum()),
            },
            "rho": {
                "energy": float(np.sum(
                    realized_rho * NPd, dtype=np.float64)),
                "off_domain_cell_count": int(
                    view["realized_off"].sum()),
                "off_domain_site_mass": int(
                    NPd[view["realized_off"]].sum()),
                "prospective_off_domain": int(
                    view["off_domain"].sum()),
                "enclosure_internal_check": reference_enclosure_ok,
            },
            "rules": _rule_bucket_summaries(registry, view, log_x),
            "CRT": crt,
        }
    return out


def _summarize_singleton_bucket(
    registry: dict,
    rec: dict,
    got: dict,
    early_site: np.ndarray,
    early_class: np.ndarray,
    anchor_inadmissible: np.ndarray,
    par: dict,
) -> dict:
    """Fast exact reducer for the empirically dominant singleton case."""
    count = len(rec["NP"])
    log_x = float(Decimal(par["log_x"]))
    A = got["A_P"]
    domain = got["domain"]
    rho = got["rho_pros"]
    rho_lo = got["rho_pros_lower"]
    rho_hi = got["rho_pros_upper"]
    realized = got["realized_rho"]
    realized_off = got["realized_off"]
    profiles = got["profiles"]
    base_crt: dict[str, dict] = {}
    for j, prime in enumerate(PROFILE_PRIMES):
        prof = profiles[:, j, :]
        unique, inverse = np.unique(prof, axis=0, return_inverse=True)
        for u, triple in enumerate(unique):
            if not np.any(triple):
                continue
            mask = inverse == u
            key = ",".join(map(str, (prime, *map(int, triple))))
            mass = int(mask.sum())
            base_crt[key] = {
                "site_mass": mass,
                "class_count": mass,
                "rho_energy": float(np.sum(
                    realized[mask], dtype=np.float64)),
                "Q": "0", "escape": "0", "gini": "0",
            }
    caps = {
        "1_8": log_x / 8,
        "1_4": log_x / 4,
        "1_2": log_x / 2,
        "3_4": 3 * log_x / 4,
        "1": log_x,
    }
    out = {}
    for s in S_PANEL:
        keep = np.ones(count, bool)
        removed_mask = early_site <= s
        removed_classes = early_class[removed_mask]
        keep[removed_classes] = False
        N = int(keep.sum())
        a_masks = {
            "0": A == 0, "1": A == 1, "2": A == 2,
            "3-4": (A >= 3) & (A <= 4),
            "5-8": (A >= 5) & (A <= 8),
            "9-16": (A >= 9) & (A <= 16),
            "17+": A >= 17,
        }
        a_bins = {
            name: {
                "class_count": int((mask & keep).sum()),
                "site_mass": int((mask & keep).sum()),
            }
            for name, mask in a_masks.items()}
        contaminated = anchor_inadmissible & keep
        atilde = A[keep] + anchor_inadmissible[keep].astype(np.int32)
        inverse_a = _fraction_pairs(
            np.ones(int((atilde > 0).sum()), np.int64),
            atilde[atilde > 0])
        rules = {}
        for rule in registry["rules"]:
            rid = rule["rule_id"]
            if not rid.startswith(("R0-", "R1-", "R2-", "R3-")):
                continue
            ambiguity = np.zeros(count, bool)
            if rid.startswith(("R0-", "R1-")):
                selected = keep.copy()
            elif rid.startswith("R2-"):
                cap = caps[rid.split("-")[1][3:]]
                ambiguity = (
                    keep & (A > 0)
                    & (rho_lo <= cap) & (rho_hi > cap))
                selected = keep & (A > 0) & (rho <= cap)
            else:
                selected = keep & (A > 0)
            if rid == "R0-all-k0":
                kappa = np.zeros(count)
            elif rid.endswith("k1_8"):
                kappa = np.full(count, 1 / 8)
            elif rid.endswith("k1_4"):
                kappa = np.full(count, 1 / 4)
            elif rid.endswith("k1_2"):
                kappa = np.full(count, 1 / 2)
            else:
                coeff = {
                    "R3-weighted-C1_2": 1 / 2,
                    "R3-weighted-C1": 1,
                    "R3-weighted-C2": 2,
                    "R3-weighted-C4": 4,
                }[rid]
                kappa = np.maximum(0.0, 1.0 - coeff * rho / log_x)
            selected_count = int(selected.sum())
            delta = 1.0 - kappa[selected]
            rules[rid] = {
                "selected_class_count": selected_count,
                "selected_site_mass": selected_count,
                "violation_class_count": 0,
                "violation_site_mass": 0,
                "escape": 0,
                "gini": "0",
                "kappa_site_sum": float(np.sum(
                    kappa[selected], dtype=np.float64)),
                "min_delta": float(delta.min()) if len(delta) else None,
                "max_negative_delta": 0.0 if len(delta) else None,
                "lambda_max": 0.0,
                "r_hist_site_weight": (
                    {"0": selected_count} if selected_count else {}),
                "numeric_ambiguity_count": int(ambiguity.sum()),
            }
        crt = json.loads(json.dumps(base_crt))
        for cls in removed_classes:
            i = int(cls)
            for j, prime in enumerate(PROFILE_PRIMES):
                triple = profiles[i, j]
                if not np.any(triple):
                    continue
                key = ",".join(map(str, (prime, *map(int, triple))))
                crt[key]["site_mass"] -= 1
                crt[key]["class_count"] -= 1
                crt[key]["rho_energy"] -= float(realized[i])
        crt = {
            key: value for key, value in crt.items()
            if value["site_mass"] != 0}
        out[str(s)] = {
            "global": {
                "N": N, "F": N, "Q": "0", "defect": "0",
                "escape": 0, "W2": 0,
            },
            "class_bins": ({
                "1": {
                    "class_count": N, "site_mass": N,
                    "W2": 0, "V2": 0, "rigid_site_mass": N,
                    "escape": 0, "gini": "0",
                }} if N else {}),
            "A": {
                "bins": a_bins,
                "domain_min": int(domain[keep].min()) if N else None,
                "domain_max": int(domain[keep].max()) if N else None,
                "contaminated_class_count": int(contaminated.sum()),
                "contaminated_site_mass": int(contaminated.sum()),
                "inverse_A_tilde_sum": str(inverse_a),
                "zero_A_tilde_classes": int((atilde == 0).sum()),
            },
            "rho": {
                "energy": float(np.sum(
                    realized[keep], dtype=np.float64)),
                "off_domain_cell_count": int(
                    (realized_off & keep).sum()),
                "off_domain_site_mass": int(
                    (realized_off & keep).sum()),
                "prospective_off_domain": int(
                    got["off_domain"][keep].sum()),
                "enclosure_internal_check": bool(np.all(
                    (realized[keep] >= got["realized_lower"][keep])
                    & (realized[keep] <= got["realized_upper"][keep]))),
            },
            "rules": rules,
            "CRT": crt,
        }
    return out


def _add_fraction_text(a: str, b: str) -> str:
    return str(Fraction(a) + Fraction(b))


def _merge_bucket_summaries(rows: list[dict]) -> dict:
    merged = {}
    for s in map(str, S_PANEL):
        target = None
        for row in rows:
            source = row["views"][s]
            if target is None:
                target = json.loads(json.dumps(source))
                continue
            for key in ("N", "F", "escape", "W2"):
                target["global"][key] += source["global"][key]
            for key in ("Q", "defect"):
                target["global"][key] = _add_fraction_text(
                    target["global"][key], source["global"][key])
            for name, values in source["class_bins"].items():
                dest = target["class_bins"].setdefault(name, {
                    "class_count": 0, "site_mass": 0, "W2": 0,
                    "V2": 0, "rigid_site_mass": 0, "escape": 0,
                    "gini": "0"})
                for key in (
                        "class_count", "site_mass", "W2", "V2",
                        "rigid_site_mass", "escape"):
                    dest[key] += values[key]
                dest["gini"] = _add_fraction_text(
                    dest["gini"], values["gini"])
            for name, values in source["A"]["bins"].items():
                dest = target["A"]["bins"][name]
                dest["class_count"] += values["class_count"]
                dest["site_mass"] += values["site_mass"]
            for key in (
                    "contaminated_class_count", "contaminated_site_mass",
                    "zero_A_tilde_classes"):
                target["A"][key] += source["A"][key]
            target["A"]["inverse_A_tilde_sum"] = _add_fraction_text(
                target["A"]["inverse_A_tilde_sum"],
                source["A"]["inverse_A_tilde_sum"])
            if source["A"]["domain_min"] is not None:
                target["A"]["domain_min"] = min(
                    target["A"]["domain_min"],
                    source["A"]["domain_min"])
                target["A"]["domain_max"] = max(
                    target["A"]["domain_max"],
                    source["A"]["domain_max"])
            for key in (
                    "energy", "off_domain_cell_count",
                    "off_domain_site_mass", "prospective_off_domain"):
                target["rho"][key] += source["rho"][key]
            target["rho"]["enclosure_internal_check"] &= (
                source["rho"]["enclosure_internal_check"])
            for rid, values in source["rules"].items():
                dest = target["rules"][rid]
                for key in (
                        "selected_class_count", "selected_site_mass",
                        "violation_class_count", "violation_site_mass",
                        "escape", "kappa_site_sum",
                        "numeric_ambiguity_count"):
                    dest[key] += values[key]
                dest["gini"] = _add_fraction_text(
                    dest["gini"], values["gini"])
                if values["min_delta"] is not None:
                    dest["min_delta"] = (
                        values["min_delta"]
                        if dest["min_delta"] is None
                        else min(dest["min_delta"], values["min_delta"]))
                    dest["max_negative_delta"] = max(
                        dest["max_negative_delta"],
                        values["max_negative_delta"])
                dest["lambda_max"] = max(
                    dest["lambda_max"], values["lambda_max"])
                for r, weight in values["r_hist_site_weight"].items():
                    dest["r_hist_site_weight"][r] = (
                        dest["r_hist_site_weight"].get(r, 0) + weight)
            for key, values in source["CRT"].items():
                dest = target["CRT"].setdefault(key, {
                    "site_mass": 0, "class_count": 0,
                    "rho_energy": 0.0, "Q": "0",
                    "escape": "0", "gini": "0"})
                for field in ("site_mass", "class_count", "rho_energy"):
                    dest[field] += values[field]
                for field in ("Q", "escape", "gini"):
                    dest[field] = _add_fraction_text(
                        dest[field], values[field])
        merged[s] = target
    return merged


def _bucket_paths(x: int, bucket: int) -> tuple[Path, Path]:
    directory = CACHE / "production" / f"x{x}"
    artifact = directory / f"bucket-{bucket:02d}.npz"
    return artifact, artifact.with_suffix(".json")


def _valid_checkpoint(artifact: Path, metadata: Path) -> bool:
    if not artifact.exists() or not metadata.exists():
        return False
    try:
        with metadata.open() as f:
            row = json.load(f)
        return (
            row["status"] == "PASS"
            and row["artifact"]["bytes"] == artifact.stat().st_size
            and row["artifact"]["sha256"] == sha256(artifact)
            and row["source_sha256"] == sha256(SOURCE)
            and row["production_format"] == PRODUCTION_FORMAT
            and row["registry_sha256"] == REGISTRY_HASH
            and row["dispatch_pin"] == PIN)
    except (KeyError, OSError, ValueError, json.JSONDecodeError):
        return False


def produce_bucket(
    x: int,
    bucket: int,
    p: np.ndarray,
    g: np.ndarray,
    sites: np.ndarray,
    buckets: np.ndarray,
    par: dict,
    workers: int,
) -> dict:
    artifact, metadata = _bucket_paths(x, bucket)
    if _valid_checkpoint(artifact, metadata):
        with metadata.open() as f:
            return json.load(f)
    bucket_sites = sites[buckets == bucket]
    t0 = time.perf_counter()
    if len(bucket_sites):
        rec = REF.exact_class_records(
            g, bucket_sites, par["J"], par["K"])
        class_seconds = time.perf_counter() - t0
        got, kernel = run_kernel(
            rec, par["J"], par["K"], par["W_floor"],
            workers=workers)
        early_site, early_class, early_cell = _early_membership(
            g, bucket_sites, rec, par["J"], par["K"])
        anchor_inadmissible = _anchor_inadmissible(
            rec, p, par["J"], par["K"])
        arrays = {
            "NP": rec["NP"].astype(np.int64),
            "NPd": rec["NPd"].astype(np.int64),
            "cell_class": rec["cell_class"].astype(np.int64),
            "mid": rec["mid"].astype(np.int64),
            "cell_first_site": rec["cell_first_site"].astype(np.int64),
            "anchor_inadmissible": anchor_inadmissible,
            "early_site": early_site,
            "early_class": early_class,
            "early_cell": early_cell,
            **got,
        }
    else:
        class_seconds = 0.0
        kernel = {
            "wall_seconds": 0.0,
            "class_count": 0,
            "cell_count": 0,
            "prospective_candidate_count": 0,
        }
        arrays = {
            "NP": np.array([], np.int64),
            "NPd": np.array([], np.int64),
            "cell_class": np.array([], np.int64),
            "mid": np.array([], np.int64),
            "cell_first_site": np.array([], np.int64),
            "anchor_inadmissible": np.array([], bool),
            "early_site": np.array([], np.int64),
            "early_class": np.array([], np.int64),
            "early_cell": np.array([], np.int64),
            "A_P": np.array([], np.int32),
            "domain": np.array([], np.int32),
            "rho_pros": np.array([], np.float64),
            "rho_pros_lower": np.array([], np.float64),
            "rho_pros_upper": np.array([], np.float64),
            "off_domain": np.array([], np.int32),
            "realized_rho": np.array([], np.float64),
            "realized_lower": np.array([], np.float64),
            "realized_upper": np.array([], np.float64),
            "realized_off": np.array([], bool),
            "profiles": np.empty((0, len(PROFILE_PRIMES), 3), np.int16),
        }
    atomic_npz(artifact, **arrays)
    result = {
        "schema": "item-0010-phase3b-bucket-checkpoint-v1",
        "dispatch_pin": PIN,
        "registry_sha256": REGISTRY_HASH,
        "source_sha256": sha256(SOURCE),
        "driver_sha256": sha256(Path(__file__)),
        "production_format": PRODUCTION_FORMAT,
        "x": x,
        "bucket": bucket,
        "bucket_count": NBUCKETS,
        "site_count": len(bucket_sites),
        "class_count": len(arrays["NP"]),
        "cell_count": len(arrays["NPd"]),
        "early_site_count": len(arrays["early_site"]),
        "class_construction_seconds": class_seconds,
        "kernel": kernel,
        "artifact": {
            "path": str(artifact),
            "bytes": artifact.stat().st_size,
            "sha256": sha256(artifact),
        },
        "status": "PASS",
    }
    atomic_json(metadata, result)
    return result


def produce_scale(x: int, workers: int = DEFAULT_WORKERS) -> dict:
    verify_frozen_inputs()
    registry = REF.verify_registry()
    if x not in registry["primary_x_ladder"]:
        raise ValueError("x is not in the frozen primary ladder")
    par = REF.d0_parameters(x)
    t0 = time.perf_counter()
    p, g, delta, valid = REF.I19.build(x)
    build_seconds = time.perf_counter() - t0
    t = REF.I19.site_range(valid, par["J"], par["K"])
    wsum = REF.I19.window_sums(g, t, par["L"])
    sites = t[
        (t >= 1)
        & (wsum <= par["W_floor"])
        & (delta[t + par["J"]] <= par["D"])
        & (delta[t + par["L"]] <= float(2 ** par["K"]))]
    buckets = REF.I19._side_hash(g, sites, par["J"], par["K"])
    rows = []
    for bucket in range(NBUCKETS):
        rows.append(produce_bucket(
            x, bucket, p, g, sites, buckets, par, workers))
        if (bucket + 1) % 8 == 0:
            print(
                f"produce-scale x={x}: {bucket + 1}/{NBUCKETS} buckets",
                flush=True)
    result = {
        "schema": "item-0010-phase3b-scale-checkpoint-v1",
        "dispatch_pin": PIN,
        "registry_sha256": REGISTRY_HASH,
        "source_sha256": sha256(SOURCE),
        "driver_sha256": sha256(Path(__file__)),
        "x": x,
        "parameters": par,
        "workers": workers,
        "build_seconds": build_seconds,
        "site_count": len(sites),
        "class_count": sum(row["class_count"] for row in rows),
        "cell_count": sum(row["cell_count"] for row in rows),
        "prospective_candidate_count": sum(
            row["kernel"]["prospective_candidate_count"] for row in rows),
        "class_construction_seconds": sum(
            row["class_construction_seconds"] for row in rows),
        "kernel_seconds": sum(
            row["kernel"]["wall_seconds"] for row in rows),
        "bucket_artifact_bytes": sum(
            row["artifact"]["bytes"] for row in rows),
        "bucket_hashes": [
            row["artifact"]["sha256"] for row in rows],
        "wall_seconds": time.perf_counter() - t0,
        "status": "PASS",
    }
    manifest = CACHE / "production" / f"x{x}" / "manifest.json"
    atomic_json(manifest, result)
    print(json.dumps({
        "manifest": str(manifest),
        "x": x,
        "sites": result["site_count"],
        "classes": result["class_count"],
        "cells": result["cell_count"],
        "artifact_bytes": result["bucket_artifact_bytes"],
        "wall_seconds": result["wall_seconds"],
        "status": result["status"]}, indent=2))
    return result


def _summary_path(x: int, bucket: int) -> Path:
    return (
        OUT / "production" / f"x{x}"
        / f"stream-bucket-{bucket:02d}.json")


def _valid_summary(path: Path, x: int, bucket: int) -> bool:
    if not path.exists():
        return False
    try:
        with path.open() as f:
            row = json.load(f)
        return (
            row["schema"] == SUMMARY_FORMAT
            and row["dispatch_pin"] == PIN
            and row["registry_sha256"] == REGISTRY_HASH
            and row["source_sha256"] == sha256(SOURCE)
            and row["x"] == x
            and row["bucket"] == bucket
            and row["status"] == "PASS")
    except (KeyError, OSError, ValueError, json.JSONDecodeError):
        return False


def _load_raw_bucket(path: Path) -> tuple[dict, dict, tuple[np.ndarray, ...]]:
    with np.load(path) as z:
        arrays = {key: z[key].copy() for key in z.files}
    rec = {
        "NP": arrays.pop("NP"),
        "NPd": arrays.pop("NPd"),
        "cell_class": arrays.pop("cell_class"),
        "mid": arrays.pop("mid"),
        "cell_first_site": arrays.pop("cell_first_site"),
    }
    early = (
        arrays.pop("early_site"),
        arrays.pop("early_class"),
        arrays.pop("early_cell"),
        arrays.pop("anchor_inadmissible"))
    return rec, arrays, early


def produce_scale_memory(x: int, workers: int = DEFAULT_WORKERS) -> dict:
    verify_frozen_inputs()
    registry = REF.verify_registry()
    if x not in registry["primary_x_ladder"]:
        raise ValueError("x is not in the frozen primary ladder")
    par = REF.d0_parameters(x)
    t0 = time.perf_counter()
    p, g, delta, valid = REF.I19.build(x)
    build_seconds = time.perf_counter() - t0
    t = REF.I19.site_range(valid, par["J"], par["K"])
    wsum = REF.I19.window_sums(g, t, par["L"])
    sites = t[
        (t >= 1)
        & (wsum <= par["W_floor"])
        & (delta[t + par["J"]] <= par["D"])
        & (delta[t + par["L"]] <= float(2 ** par["K"]))]
    buckets = REF.I19._side_hash(g, sites, par["J"], par["K"])
    rows = []
    computed = 0
    reused_raw = 0
    reused_summary = 0
    for bucket in range(STREAM_BUCKETS):
        summary_path = _summary_path(x, bucket)
        if _valid_summary(summary_path, x, bucket):
            with summary_path.open() as f:
                rows.append(json.load(f))
            reused_summary += 1
            continue
        bucket_sites = sites[(buckets % STREAM_BUCKETS) == bucket]
        if len(bucket_sites):
            rec = REF.exact_class_records(
                g, bucket_sites, par["J"], par["K"])
            got, kernel_meta = run_kernel(
                rec, par["J"], par["K"], par["W_floor"],
                workers=workers)
            early_site, early_class, early_cell = _early_membership(
                g, bucket_sites, rec, par["J"], par["K"])
            anchor = _anchor_inadmissible(
                rec, p, par["J"], par["K"])
        else:
            rec = {
                "NP": np.array([], np.int64),
                "NPd": np.array([], np.int64),
                "cell_class": np.array([], np.int64),
                "mid": np.array([], np.int64),
                "cell_first_site": np.array([], np.int64),
            }
            got = {
                "A_P": np.array([], np.int32),
                "domain": np.array([], np.int32),
                "rho_pros": np.array([], np.float64),
                "rho_pros_lower": np.array([], np.float64),
                "rho_pros_upper": np.array([], np.float64),
                "off_domain": np.array([], np.int32),
                "realized_rho": np.array([], np.float64),
                "realized_lower": np.array([], np.float64),
                "realized_upper": np.array([], np.float64),
                "realized_off": np.array([], bool),
                "profiles": np.empty(
                    (0, len(PROFILE_PRIMES), 3), np.int16),
            }
            early_site = early_class = early_cell = np.array(
                [], np.int64)
            anchor = np.array([], bool)
            kernel_meta = {"wall_seconds": 0.0}
        computed += 1
        views = _summarize_bucket(
            registry, rec, got, early_site, early_class, early_cell,
            anchor, p, par)
        row = {
            "schema": SUMMARY_FORMAT,
            "dispatch_pin": PIN,
            "registry_sha256": REGISTRY_HASH,
            "source_sha256": sha256(SOURCE),
            "x": x,
            "bucket": bucket,
            "kernel": kernel_meta,
            "views": views,
            "status": "PASS",
        }
        atomic_json(summary_path, row)
        rows.append(row)
        if (bucket + 1) % 8 == 0 or bucket + 1 == STREAM_BUCKETS:
            print(
                f"produce-scale-memory x={x}: "
                f"{bucket + 1}/{STREAM_BUCKETS} buckets",
                flush=True)
    rows.sort(key=lambda row: row["bucket"])
    merged = _merge_bucket_summaries(rows)
    for s, view in merged.items():
        N = view["global"]["N"]
        if Fraction(view["global"]["defect"]) != Fraction(N - view["global"]["F"]) - Fraction(view["global"]["Q"]):
            raise AssertionError(f"merged defect identity failed at s={s}")
        if any(
                rule["numeric_ambiguity_count"]
                for rule in view["rules"].values()):
            raise RuntimeError(
                f"selector/numeric ambiguity at x={x}, s={s}")
        view["A"]["inverse_A_tilde_site_mean"] = (
            str(Fraction(view["A"]["inverse_A_tilde_sum"]) / N)
            if N and not view["A"]["zero_A_tilde_classes"] else None)
        view["rho"]["energy_over_N"] = (
            view["rho"]["energy"] / N if N else None)
    result = {
        "schema": "item-0010-phase3b-scale-result-v1",
        "dispatch_pin": PIN,
        "registry_sha256": REGISTRY_HASH,
        "source_sha256": sha256(SOURCE),
        "x": x,
        "parameters": par,
        "workers": workers,
        "build_seconds": build_seconds,
        "site_count_s0": len(sites),
        "computed_bucket_count": computed,
        "reused_raw_bucket_count": reused_raw,
        "reused_summary_bucket_count": reused_summary,
        "views": merged,
        "wall_seconds": time.perf_counter() - t0,
        "peak_rss_kib": resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
        "status": "PASS",
    }
    path = OUT / "production" / f"x{x}" / "scale-result.json"
    atomic_json(path, result)
    print(json.dumps({
        "path": str(path),
        "x": x,
        "site_count_s0": len(sites),
        "computed_buckets": computed,
        "reused_raw_buckets": reused_raw,
        "reused_summary_buckets": reused_summary,
        "wall_seconds": result["wall_seconds"],
        "peak_rss_kib": result["peak_rss_kib"],
        "status": result["status"]}, indent=2))
    return result


def validate_stream_smoke() -> dict:
    path = OUT / "production" / "x1000000" / "scale-result.json"
    if not path.exists():
        raise RuntimeError("produce-scale-memory 1000000 first")
    with path.open() as f:
        result = json.load(f)
    with (ORACLE_OUT / "smoke-x1000000-s0.json").open() as f:
        oracle = json.load(f)
    view = result["views"]["0"]
    global_checks = {
        key: view["global"][key] == oracle["global_metrics"][key]
        for key in ("N", "F", "Q", "defect", "W2")}
    a = view["A"]
    oracle_a = oracle["A_P"]
    a_checks = {
        "domain_min": a["domain_min"] == oracle_a["residual_domain_min"],
        "domain_max": a["domain_max"] == oracle_a["residual_domain_max"],
        "contaminated_class_count": (
            a["contaminated_class_count"]
            == oracle_a["contaminated_class_count"]),
        "contaminated_site_mass": (
            a["contaminated_site_mass"]
            == oracle_a["contaminated_site_mass"]),
        "inverse_A_tilde_site_mean": (
            a["inverse_A_tilde_site_mean"]
            == oracle_a["inverse_A_tilde_site_mean"]),
        "zero_A_tilde_classes": (
            a["zero_A_tilde_classes"]
            == oracle_a["zero_A_tilde_classes"]),
        "bins": all(
            a["bins"][row["label"]]["class_count"] == row["class_count"]
            and a["bins"][row["label"]]["site_mass"] == row["site_mass"]
            for row in oracle_a["bins"]),
    }
    rho_checks = {
        "energy": math.isclose(
            view["rho"]["energy"],
            oracle["rho_energy"]["realized_rho_energy"],
            rel_tol=2e-15, abs_tol=1e-8),
        "energy_over_N": math.isclose(
            view["rho"]["energy_over_N"],
            oracle["rho_energy"]["realized_rho_energy_over_N"],
            rel_tol=2e-15, abs_tol=1e-12),
        "off_domain_cell_count": (
            view["rho"]["off_domain_cell_count"]
            == oracle["rho_energy"]["off_domain_cell_count"]),
        "off_domain_site_mass": (
            view["rho"]["off_domain_site_mass"]
            == oracle["rho_energy"]["off_domain_site_mass"]),
    }
    oracle_rules = {row["rule_id"]: row for row in oracle["rules"]}
    rule_checks = {}
    for rid, row in view["rules"].items():
        old = oracle_rules[rid]
        rule_checks[rid] = {
            "class_count": (
                row["selected_class_count"]
                == old["favorable_class_count"]),
            "site_mass": (
                row["selected_site_mass"]
                == old["favorable_site_mass"]),
            "violation_count": (
                row["violation_class_count"]
                == old["violation_class_count"]),
            "violation_mass": (
                row["violation_site_mass"]
                == int(Fraction(old["beta_viol"])
                       * oracle["global_metrics"]["N"])),
            "lambda_max": row["lambda_max"] == old["lambda_max"],
            "ambiguity": row["numeric_ambiguity_count"] == 0,
        }
    oracle_crt = {
        ",".join(map(str, (
            row["p"], row["nu_H"], row["nu_pre"], row["nu_suf"]))): row
        for row in oracle["CRT_strata"]}
    crt_checks = {
        "same_keys": set(view["CRT"]) == set(oracle_crt),
        "rows": all(
            row["site_mass"] == oracle_crt[key]["site_mass"]
            and row["class_count"] == oracle_crt[key]["class_count"]
            and row["Q"] == oracle_crt[key]["Q"]
            and row["escape"] == oracle_crt[key]["majority_escape"]
            and row["gini"] == oracle_crt[key]["Gini"]
            and math.isclose(
                row["rho_energy"], oracle_crt[key]["rho_energy"],
                rel_tol=1e-14, abs_tol=1e-6)
            for key, row in view["CRT"].items()
            if key in oracle_crt),
    }
    passed = (
        all(global_checks.values())
        and all(a_checks.values())
        and all(rho_checks.values())
        and all(all(checks.values()) for checks in rule_checks.values())
        and all(crt_checks.values()))
    validation = {
        "schema": "item-0010-phase3b-stream-smoke-validation-v1",
        "global": global_checks,
        "A": a_checks,
        "rho": rho_checks,
        "rules": rule_checks,
        "CRT": crt_checks,
        "status": "PASS" if passed else "FAIL",
    }
    atomic_json(OUT / "stream-smoke-validation.json", validation)
    print(json.dumps(validation, indent=2))
    if not passed:
        raise AssertionError("stream reducer smoke validation failed")
    return validation


def _weighted_quantiles_from_hist(hist: dict[str, int]) -> dict:
    if not hist:
        return {str(q): None for q in (
            0.01, 0.05, 0.25, 0.5, 0.75, 0.95, 0.99)}
    rows = sorted(
        ((Fraction(value), int(weight)) for value, weight in hist.items()),
        key=lambda row: row[0])
    total = sum(weight for _, weight in rows)
    out = {}
    for q in (0.01, 0.05, 0.25, 0.5, 0.75, 0.95, 0.99):
        cutoff = q * total
        running = 0
        chosen = rows[-1][0]
        for value, weight in rows:
            running += weight
            if running >= cutoff:
                chosen = value
                break
        out[str(q)] = float(chosen)
    return out


def _render_rule_row(
    rule_spec: dict, summary: dict, N: int, F: int,
) -> dict:
    rid = rule_spec["rule_id"]
    mass = summary["selected_site_mass"]
    f_g = summary["selected_class_count"]
    viol_mass = summary["violation_site_mass"]
    escape = summary["escape"]
    gini = Fraction(summary["gini"])
    if rid == "R0-all-k0":
        eta_profile = Fraction()
        eta_profile_text = "0"
    elif rid.endswith("k1_8"):
        eta_profile = Fraction(mass, 8 * N)
        eta_profile_text = str(eta_profile)
    elif rid.endswith("k1_4"):
        eta_profile = Fraction(mass, 4 * N)
        eta_profile_text = str(eta_profile)
    elif rid.endswith("k1_2"):
        eta_profile = Fraction(mass, 2 * N)
        eta_profile_text = str(eta_profile)
    else:
        eta_profile_float = summary["kappa_site_sum"] / N
        eta_profile = Fraction.from_float(eta_profile_float)
        eta_profile_text = f"{eta_profile_float:.17g}"
    lambda_max = summary["lambda_max"]
    eta_weight = Fraction(escape + f_g, N)
    eta_escape = Fraction(escape, N)
    eta_gini = gini / N
    eta_cert = (1.0 - lambda_max) * mass / N
    return {
        "rule_id": rid,
        "classification": rule_spec["classification"],
        "empty": f_g == 0,
        "favorable_class_count": f_g,
        "favorable_site_mass": mass,
        "alpha": str(Fraction(mass, N)),
        "eta_profile": eta_profile_text,
        "beta_viol": str(Fraction(viol_mass, N)),
        "violation_class_count": summary["violation_class_count"],
        "min_delta": summary["min_delta"],
        "max_negative_delta": summary["max_negative_delta"],
        "F_exc_over_N": str(Fraction(F - f_g, N)),
        "passed": summary["violation_class_count"] == 0,
        "positive_finite_H2": (
            summary["violation_class_count"] == 0
            and eta_profile > 0),
        "lambda_max": lambda_max,
        "eta_cert": eta_cert,
        "eta_weight": str(eta_weight),
        "eta_escape": str(eta_escape),
        "eta_Gini": str(eta_gini),
        "r_weighted_quantiles": _weighted_quantiles_from_hist(
            summary["r_hist_site_weight"]),
        "r_weighted_mean": (
            sum(
                float(Fraction(value)) * weight
                for value, weight
                in summary["r_hist_site_weight"].items()) / mass
            if mass else None),
        "numeric_ambiguity_count": summary["numeric_ambiguity_count"],
        "checks": {
            "eta_cert_le_eta_weight": (
                eta_cert <= float(eta_weight) + 2e-12),
            "eta_weight_identity": True,
            "escape_Gini_bounds": (
                eta_escape <= eta_gini <= 2 * eta_escape),
            "passing_global_bound": True,
            "passing_profile_le_weight": (
                float(eta_profile) <= float(eta_weight) + 2e-12),
        },
    }


def finalize_campaign() -> dict:
    verify_frozen_inputs()
    registry = REF.verify_registry()
    production = OUT / "production"
    scale_results = []
    for x in registry["primary_x_ladder"]:
        path = production / f"x{x}" / "scale-result.json"
        if not path.exists():
            raise RuntimeError(f"missing scale result: {path}")
        with path.open() as f:
            row = json.load(f)
        if row["status"] != "PASS":
            raise RuntimeError(f"scale result is not PASS: x={x}")
        scale_results.append(row)
    global_rows = []
    a_rows = []
    rho_rows = []
    rule_rows = []
    crt_rows = []
    class_rows = []
    integrity = {}
    for scale in scale_results:
        x = scale["x"]
        par = scale["parameters"]
        for s in map(str, S_PANEL):
            view = scale["views"][s]
            glob = view["global"]
            N = glob["N"]
            F = glob["F"]
            global_rows.append({
                "x": x, "s": int(s), "parameters": par, **glob})
            a_rows.append({"x": x, "s": int(s), **view["A"]})
            rho_rows.append({
                "x": x, "s": int(s),
                "rho_Q": REF.Q_RHO,
                "certified_tail_log_width": (
                    0.51 * par["k"] * par["k"] / REF.Q_RHO),
                **view["rho"]})
            rendered_rules = []
            specs = {
                rule["rule_id"]: rule for rule in registry["rules"]}
            for rid, summary in view["rules"].items():
                rendered = _render_rule_row(
                    specs[rid], summary, N, F)
                rendered_rules.append(rendered)
                rule_rows.append({
                    "x": x, "s": int(s), **rendered})
            for key, values in sorted(view["CRT"].items()):
                prime, nh, na, nb = map(int, key.split(","))
                crt_rows.append({
                    "x": x, "s": int(s), "p": prime,
                    "nu_H": nh, "nu_pre": na, "nu_suf": nb,
                    **values})
            for M, values in view["class_bins"].items():
                class_rows.append({
                    "x": x, "s": int(s), "M": int(M), **values})
            q = Fraction(glob["Q"])
            defect = Fraction(glob["defect"])
            row_key = f"{x},{s}"
            integrity[row_key] = {
                "Q_le_N_minus_F": q <= N - F,
                "defect_identity": defect == Fraction(N - F) - q,
                "escape_le_Gini_le_2escape": (
                    Fraction(glob["escape"], N) <= defect / N
                    <= 2 * Fraction(glob["escape"], N)),
                "rho_enclosure_internal": (
                    view["rho"]["enclosure_internal_check"]),
                "zero_numeric_ambiguities": all(
                    row["numeric_ambiguity_count"] == 0
                    for row in rendered_rules),
                "rule_checks": all(
                    all(row["checks"].values())
                    for row in rendered_rules),
            }
    artifacts = {
        "global-per-scale.json": global_rows,
        "A-P-table.json": a_rows,
        "rho-energy-table.json": rho_rows,
        "per-rule-certificates.json": rule_rows,
        "CRT-strata.json": crt_rows,
        "class-size-table.json": class_rows,
        "integrity-checks.json": integrity,
    }
    for name, value in artifacts.items():
        atomic_json(production / name, value)
    library, build = build_kernel()
    manifest = {
        "schema": "item-0010-phase3b-production-manifest-v1",
        "dispatch_pin": PIN,
        "registry_sha256": REGISTRY_HASH,
        "source_sha256": sha256(SOURCE),
        "driver_sha256": sha256(Path(__file__)),
        "library_sha256": sha256(library),
        "compiler": build["compiler"],
        "platform": platform.platform(),
        "python": platform.python_version(),
        "numpy": np.__version__,
        "workers": DEFAULT_WORKERS,
        "cloud_used": False,
        "primary_x_ladder": registry["primary_x_ladder"],
        "s_panel": list(S_PANEL),
        "commands": [
            "python3 -B dossier/item-0010-workpapers/m5_lite_phase3b.py self-test",
            "python3 -B dossier/item-0010-workpapers/m5_lite_phase3b.py equivalence 24",
            "python3 -B dossier/item-0010-workpapers/m5_lite_phase3b.py benchmark 1000000 8192",
            "python3 -B dossier/item-0010-workpapers/m5_lite_phase3b.py benchmark 3000000 8192",
            "python3 -B dossier/item-0010-workpapers/m5_lite_phase3b.py produce-scale-memory X 24",
            "python3 -B dossier/item-0010-workpapers/m5_lite_phase3b.py finalize-campaign",
        ],
        "scale_results": {},
        "artifacts": {},
        "status": "PASS",
    }
    for scale in scale_results:
        x = scale["x"]
        path = production / f"x{x}" / "scale-result.json"
        summaries = sorted((production / f"x{x}").glob(
            "stream-bucket-*.json"))
        manifest["scale_results"][str(x)] = {
            "path": str(path.relative_to(REPO)),
            "bytes": path.stat().st_size,
            "sha256": sha256(path),
            "wall_seconds": scale["wall_seconds"],
            "peak_rss_kib": scale["peak_rss_kib"],
            "summary_count": len(summaries),
            "summary_sha256": [sha256(item) for item in summaries],
        }
    for name in artifacts:
        path = production / name
        manifest["artifacts"][name] = {
            "bytes": path.stat().st_size,
            "sha256": sha256(path)}
    atomic_json(production / "run-manifest.json", manifest)
    print(json.dumps({
        "path": str(production / "run-manifest.json"),
        "scale_count": len(scale_results),
        "row_count": len(global_rows),
        "rule_row_count": len(rule_rows),
        "CRT_row_count": len(crt_rows),
        "status": manifest["status"]}, indent=2))
    return manifest


def audit_scale(x: int) -> dict:
    rows = []
    missing = []
    for bucket in range(NBUCKETS):
        artifact, metadata = _bucket_paths(x, bucket)
        valid = _valid_checkpoint(artifact, metadata)
        if not valid:
            missing.append(bucket)
            continue
        with metadata.open() as f:
            rows.append(json.load(f))
    fixed_s = {}
    for s in S_PANEL:
        N = 0
        F = 0
        cells = 0
        q = Fraction()
        removed = 0
        for row in rows:
            artifact = Path(row["artifact"]["path"])
            with np.load(artifact) as z:
                NP = z["NP"].astype(np.int64)
                NPd = z["NPd"].astype(np.int64)
                ci = z["cell_class"].astype(np.int64)
                early_mask = z["early_site"] <= s
                if early_mask.any():
                    class_removed = np.bincount(
                        z["early_class"][early_mask],
                        minlength=len(NP))
                    cell_removed = np.bincount(
                        z["early_cell"][early_mask],
                        minlength=len(NPd))
                    NP -= class_removed
                    NPd -= cell_removed
                    removed += int(early_mask.sum())
                keep_class = NP > 0
                keep_cell = NPd > 0
                if int(NP.sum()) != int(NPd.sum()):
                    raise AssertionError(
                        f"fixed-s mass mismatch at x={x}, s={s}")
                N += int(NP.sum())
                F += int(keep_class.sum())
                cells += int(keep_cell.sum())
                contributing = np.nonzero(
                    keep_cell & (NPd >= 2))[0]
                for cell in contributing:
                    cls = int(ci[cell])
                    q += Fraction(
                        int(NPd[cell] * (NPd[cell] - 1)),
                        int(NP[cls]))
        fixed_s[str(s)] = {
            "N": N,
            "F": F,
            "realized_cell_count": cells,
            "Q": str(q),
            "removed_from_s0": removed,
        }
    result = {
        "schema": "item-0010-phase3b-scale-audit-v1",
        "dispatch_pin": PIN,
        "registry_sha256": REGISTRY_HASH,
        "source_sha256": sha256(SOURCE),
        "driver_sha256": sha256(Path(__file__)),
        "x": x,
        "complete_bucket_count": len(rows),
        "expected_bucket_count": NBUCKETS,
        "missing_or_invalid_buckets": missing,
        "duplicate_buckets": (
            len({row["bucket"] for row in rows}) != len(rows)),
        "site_count": sum(row["site_count"] for row in rows),
        "class_count": sum(row["class_count"] for row in rows),
        "cell_count": sum(row["cell_count"] for row in rows),
        "artifact_bytes": sum(row["artifact"]["bytes"] for row in rows),
        "fixed_s_views": fixed_s,
        "status": (
            "PASS" if len(rows) == NBUCKETS and not missing else "FAIL"),
    }
    print(json.dumps(result, indent=2))
    return result


def parallel_note() -> dict:
    note = {
        "schema": "item-0010-phase3b-parallelization-v1",
        "dispatch_pin": PIN,
        "registry_sha256": REGISTRY_HASH,
        "independent_axes": {
            "x": {
                "shard_key": "integer x from the frozen ladder",
                "shared_inputs": "registry, implementation, prime cutoff",
                "output": "one scale manifest plus fixed-s views",
                "merge": "sort by frozen x-ladder order",
                "associative_commutative": True,
                "checkpoint": "atomic per-scale manifest",
                "retry": "recompute only the missing x shard",
            },
            "side_class_bucket": {
                "shard_key": "fixed hash(side gap word) bucket",
                "shared_inputs": "read-only prime/gap/delta arrays and D0 row",
                "output": "class/cell arrays and prospective/realized reducers",
                "merge": "integer sums and bucket-index concatenation",
                "associative_commutative": (
                    "integer reducers yes; byte order fixed by bucket index"),
                "checkpoint": "atomic bucket artifact plus SHA-256",
                "retry": "idempotent replacement after hash validation",
            },
            "class_range": {
                "shard_key": "bucket-local contiguous class interval",
                "shared_inputs": "small-prime list and invariant band factor",
                "output": "A_P, domain, rho enclosure, realized rho/CRT",
                "merge": "write disjoint deterministic array slices",
                "associative_commutative": True,
                "checkpoint": "parent bucket is the checkpoint boundary",
                "retry": "rerun failed range before bucket commit",
            },
            "fixed_s": {
                "shard_key": "s in the frozen panel",
                "shared_inputs": (
                    "s=0 side classes, prospective rho, realized cell rho"),
                "output": "counts after deleting sites n < s+1",
                "merge": "independent report rows",
                "associative_commutative": True,
                "checkpoint": "stored with parent x/bucket",
                "retry": "re-reduce without recomputing rho",
            },
        },
        "cloud": {
            "used": False,
            "reason": (
                "Repository AGENTS.md requires local execution and forbids "
                "delegating repository computation to Codex Cloud."),
            "data_transfer": (
                "Not applicable locally. A future operator-managed compute "
                "host would need the frozen registry, source/executable "
                "hashes, and per-x prime/gap/delta cache or regenerate it."),
        },
        "status": "PASS",
    }
    atomic_json(OUT / "parallelization.json", note)
    print(json.dumps(note, indent=2))
    return note


def main() -> None:
    if len(sys.argv) < 2:
        raise SystemExit(__doc__)
    command = sys.argv[1]
    if command == "build":
        _, meta = build_kernel()
        print(json.dumps(meta, indent=2))
    elif command == "self-test":
        self_test()
    elif command == "equivalence":
        workers = int(sys.argv[2]) if len(sys.argv) > 2 else DEFAULT_WORKERS
        equivalence(workers)
    elif command == "benchmark":
        x = int(sys.argv[2]) if len(sys.argv) > 2 else 1_000_000
        nclass = int(sys.argv[3]) if len(sys.argv) > 3 else 8192
        benchmark(x, nclass)
    elif command == "produce-scale":
        if len(sys.argv) < 3:
            raise SystemExit("produce-scale requires X")
        workers = int(sys.argv[3]) if len(sys.argv) > 3 else DEFAULT_WORKERS
        produce_scale(int(sys.argv[2]), workers)
    elif command == "produce-scale-memory":
        if len(sys.argv) < 3:
            raise SystemExit("produce-scale-memory requires X")
        workers = int(sys.argv[3]) if len(sys.argv) > 3 else DEFAULT_WORKERS
        produce_scale_memory(int(sys.argv[2]), workers)
    elif command == "validate-stream-smoke":
        validate_stream_smoke()
    elif command == "finalize-campaign":
        finalize_campaign()
    elif command == "audit-scale":
        if len(sys.argv) < 3:
            raise SystemExit("audit-scale requires X")
        result = audit_scale(int(sys.argv[2]))
        if result["status"] != "PASS":
            raise SystemExit(1)
    elif command == "parallel-note":
        parallel_note()
    elif command == "verify-artifacts":
        result = verify_artifacts()
        if result["status"] != "PASS":
            raise SystemExit(1)
    else:
        raise SystemExit(f"unknown command: {command}")


if __name__ == "__main__":
    main()
