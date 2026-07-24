#!/usr/bin/env python3
"""Exact equality-refinement diagnostics for the frozen D0 site rows.

This reads only the regenerable prime-gap/delta cache used by Phase 3b.
Every site count is checked against the committed production summary before
any collision statistic is emitted.  Equality classes are refined directly
by the next int16 gap value, so no probabilistic hash is used.
"""

from __future__ import annotations

import argparse
import json
import math
import resource
import sys
import time
from collections import Counter
from pathlib import Path

import numpy as np

REPO = Path("../..")
WORK = REPO / "dossier/item-0010-workpapers"
CACHE = Path("/tmp/item0010-m5-lite-cache")
GLOBAL = WORK / "m5-lite-phase3b/production/global-per-scale.json"
sys.path.insert(0, str(WORK))
import m5_lite_measure as REF  # noqa: E402

BASE = np.uint64(32768)


def production_n() -> dict[tuple[int, int], int]:
    rows = json.loads(GLOBAL.read_text())
    return {(int(r["x"]), int(r["s"])): int(r["N"]) for r in rows}


def sites_for(x: int, par: dict) -> tuple[np.memmap, np.memmap, np.ndarray]:
    g = np.load(CACHE / f"g_{x}.npy", mmap_mode="r")
    delta = np.load(CACHE / f"delta_{x}.npy", mmap_mode="r")
    valid = len(g) - 200
    lo = 1
    hi = valid - (par["J"] + par["K"] + 2)
    cs = np.empty(len(g) + 1, dtype=np.int64)
    cs[0] = 0
    np.cumsum(g, dtype=np.int64, out=cs[1:])
    chunks: list[np.ndarray] = []
    step = 4_000_000
    for a in range(lo, hi, step):
        b = min(a + step, hi)
        t = np.arange(a, b, dtype=np.int64)
        keep = (
            (cs[t + par["L"]] - cs[t] <= par["W_floor"])
            & (delta[t + par["J"]] <= par["D"])
            & (delta[t + par["L"]] <= float(2 ** par["K"]))
        )
        chunks.append(t[keep].astype(np.int32))
    del cs
    return g, delta, np.concatenate(chunks)


def refine_curve(
    g: np.ndarray,
    sites: np.ndarray,
    steps: list[tuple[int, ...]],
) -> tuple[list[dict], np.ndarray]:
    active_sites = sites
    active_group = np.zeros(len(sites), dtype=np.uint32)
    singleton_classes = 0
    rows: list[dict] = []
    for depth, offsets in enumerate(steps, 1):
        if not len(active_sites):
            rows.append(
                {
                    "depth": depth,
                    "class_count": len(sites),
                    "pair_collisions": 0,
                    "max_multiplicity": 1 if len(sites) else 0,
                    "repeated_site_mass": 0,
                    "repeated_classes": 0,
                    "S2": float(len(sites)),
                    "H2": math.log(len(sites)) if len(sites) else None,
                }
            )
            continue
        key = active_group.astype(np.uint64)
        for off in offsets:
            key = key * BASE + g[active_sites.astype(np.int64) + off].astype(
                np.uint64
            )
        _, inverse, counts = np.unique(
            key, return_inverse=True, return_counts=True
        )
        repeated_class = counts > 1
        repeated_site = repeated_class[inverse]
        pair_collisions = int(
            np.sum(
                counts.astype(object) * (counts.astype(object) - 1) // 2,
                dtype=object,
            )
        )
        repeated_mass = int(counts[repeated_class].sum())
        nclasses = singleton_classes + len(counts)
        n = len(sites)
        denom = n + 2 * pair_collisions
        s2 = n * n / denom if denom else 0.0
        rows.append(
            {
                "depth": depth,
                "class_count": int(nclasses),
                "pair_collisions": pair_collisions,
                "max_multiplicity": int(counts.max()),
                "repeated_site_mass": repeated_mass,
                "repeated_classes": int(repeated_class.sum()),
                "S2": s2,
                "H2": math.log(s2) if s2 else None,
            }
        )
        singleton_classes += int((counts == 1).sum())
        active_sites = active_sites[repeated_site]
        relabel = np.cumsum(repeated_class, dtype=np.uint32) - 1
        active_group = relabel[inverse[repeated_site]]
    return rows, active_sites


def multiplicity_histogram(
    g: np.ndarray, sites: np.ndarray, steps: list[tuple[int, ...]]
) -> dict[str, int]:
    active_sites = sites
    active_group = np.zeros(len(sites), dtype=np.uint32)
    singleton_count = 0
    counts = np.array([len(sites)], dtype=np.int64)
    for offsets in steps:
        if not len(active_sites):
            break
        key = active_group.astype(np.uint64)
        for off in offsets:
            key = key * BASE + g[active_sites.astype(np.int64) + off].astype(
                np.uint64
            )
        _, inverse, counts = np.unique(
            key, return_inverse=True, return_counts=True
        )
        repeated_class = counts > 1
        singleton_count += int((counts == 1).sum())
        repeated_site = repeated_class[inverse]
        active_sites = active_sites[repeated_site]
        relabel = np.cumsum(repeated_class, dtype=np.uint32) - 1
        active_group = relabel[inverse[repeated_site]]
    hist = Counter(map(int, counts[counts > 1]))
    hist[1] += singleton_count
    return {str(k): int(hist[k]) for k in sorted(hist)}


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("x", type=int)
    ap.add_argument("--s", type=int, default=0)
    ap.add_argument("--output", type=Path)
    args = ap.parse_args()
    started = time.perf_counter()
    par = REF.d0_parameters(args.x)
    g, _delta, sites0 = sites_for(args.x, par)
    expected = production_n()[(args.x, args.s)]
    sites = sites0[sites0 >= args.s + 1]
    if len(sites) != expected:
        raise RuntimeError(
            f"site count {len(sites)} != committed production N {expected}"
        )
    J, K = par["J"], par["K"]
    pre_first = [(j,) for j in range(J)]
    pre_last = [(j,) for j in range(J - 1, -1, -1)]
    suf_first = [(J + 1 + j,) for j in range(K)]
    suf_last = [(J + K - j,) for j in range(K)]
    joint_first = [
        (j, J + 1 + j) for j in range(min(J, K))
    ]
    joint_inner = [
        (J - 1 - j, J + 1 + j) for j in range(min(J, K))
    ]
    joint_outer = [
        (j, J + K - j) for j in range(min(J, K))
    ]
    joint_reverse = [
        (J - 1 - j, J + K - j) for j in range(min(J, K))
    ]
    result: dict[str, object] = {
        "schema": "item-0010-flank-frontier-diagnostic-v1",
        "classification": (
            "MEASURED exact finite reconstruction from regenerable cache; "
            "site count checked against committed Phase-3b production"
        ),
        "x": args.x,
        "s": args.s,
        "parameters": {k: par[k] for k in ("D", "J", "K", "L", "W_floor")},
        "N": len(sites),
        "curves": {},
    }
    active: dict[str, np.ndarray] = {}
    for name, steps in (
        ("pre_first", pre_first),
        ("pre_last", pre_last),
        ("suf_first", suf_first),
        ("suf_last", suf_last),
        ("joint_first", joint_first),
        ("joint_inner", joint_inner),
        ("joint_outer", joint_outer),
        ("joint_reverse", joint_reverse),
    ):
        curve, repeated_sites = refine_curve(g, sites, steps)
        result["curves"][name] = curve
        active[name] = repeated_sites
    pre_repeat = np.sort(active["pre_first"])
    suf_repeat = np.sort(active["suf_first"])
    both = np.intersect1d(pre_repeat, suf_repeat, assume_unique=True)
    result["full_side_summary"] = {
        "C_pre": result["curves"]["pre_first"][-1]["pair_collisions"],
        "C_suf": result["curves"]["suf_first"][-1]["pair_collisions"],
        "max_pre": result["curves"]["pre_first"][-1]["max_multiplicity"],
        "max_suf": result["curves"]["suf_first"][-1]["max_multiplicity"],
        "pre_repeated_site_mass": len(pre_repeat),
        "suf_repeated_site_mass": len(suf_repeat),
        "both_sides_repeated_site_mass": len(both),
        "both_sides_repeat_but_joint_unique": len(both),
        "pre_multiplicity_histogram": multiplicity_histogram(
            g, sites, pre_first
        ),
        "suf_multiplicity_histogram": multiplicity_histogram(
            g, sites, suf_first
        ),
    }
    result["elapsed_seconds"] = time.perf_counter() - started
    result["max_rss_kib"] = resource.getrusage(
        resource.RUSAGE_SELF
    ).ru_maxrss
    text = json.dumps(result, indent=2) + "\n"
    if args.output:
        args.output.write_text(text)
    else:
        print(text, end="")


if __name__ == "__main__":
    main()
