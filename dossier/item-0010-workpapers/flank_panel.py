#!/usr/bin/env python3
"""Exact eight-path flank panel with deletion-derived positive-s rows.

Repository and cache inputs are read-only.  For each equality refinement,
the s=0 class size m and the number r_s of deleted early sites give the
positive-s collision contribution exactly as choose(m-r_s, 2).
"""

from __future__ import annotations

import argparse
import json
import math
import resource
import sys
import time
from pathlib import Path

import numpy as np

REPO = Path("../..")
WORK = REPO / "dossier/item-0010-workpapers"
CACHE = Path("/tmp/item0010-m5-lite-cache")
GLOBAL = WORK / "m5-lite-phase3b/production/global-per-scale.json"
sys.path.insert(0, str(WORK))
import m5_lite_measure as REF  # noqa: E402

BASE = np.uint64(32768)
S_VALUES = (0, 1, 10, 100, 1000)


def production_n() -> dict[tuple[int, int], int]:
    rows = json.loads(GLOBAL.read_text())
    return {(int(r["x"]), int(r["s"])): int(r["N"]) for r in rows}


def sites_for(x: int, par: dict) -> tuple[np.memmap, np.ndarray]:
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
    return g, np.concatenate(chunks)


def pair_count(counts: np.ndarray) -> int:
    return int(np.sum(counts * (counts - 1) // 2, dtype=np.int64))


def deletion_panel(
    counts: np.ndarray,
    inverse: np.ndarray,
    active_sites: np.ndarray,
) -> dict[str, int]:
    base = pair_count(counts)
    out = {"0": base}
    for s in S_VALUES[1:]:
        removed_inverse = inverse[active_sites < s + 1]
        if not len(removed_inverse):
            out[str(s)] = base
            continue
        touched, removed = np.unique(
            removed_inverse, return_counts=True
        )
        old = counts[touched]
        reduction = np.sum(
            removed * (old - 1) - removed * (removed - 1) // 2,
            dtype=np.int64,
        )
        out[str(s)] = base - int(reduction)
    return out


def refine_curve(
    g: np.ndarray,
    sites: np.ndarray,
    steps: list[tuple[int, ...]],
) -> list[dict]:
    active_sites = sites
    active_group = np.zeros(len(sites), dtype=np.uint32)
    rows: list[dict] = []
    for depth, offsets in enumerate(steps, 1):
        if not len(active_sites):
            rows.append(
                {
                    "depth": depth,
                    "pair_collisions": {
                        str(s): 0 for s in S_VALUES
                    },
                }
            )
            continue
        key = active_group.astype(np.uint64)
        for off in offsets:
            key = key * BASE + g[
                active_sites.astype(np.int64) + off
            ].astype(np.uint64)
        _, inverse, counts = np.unique(
            key, return_inverse=True, return_counts=True
        )
        panel = deletion_panel(counts, inverse, active_sites)
        rows.append(
            {
                "depth": depth,
                "pair_collisions": panel,
                "s0_repeated_classes": int(np.sum(counts > 1)),
                "s0_repeated_site_mass": int(
                    np.sum(counts[counts > 1], dtype=np.int64)
                ),
                "s0_max_multiplicity": int(counts.max()),
            }
        )
        repeated_class = counts > 1
        repeated_site = repeated_class[inverse]
        active_sites = active_sites[repeated_site]
        relabel = np.cumsum(repeated_class, dtype=np.uint32) - 1
        active_group = relabel[inverse[repeated_site]]
    return rows


def enrich_entropy(
    rows: list[dict], populations: dict[str, int]
) -> None:
    for row in rows:
        row["diagnostics"] = {}
        for s_text, collisions in row["pair_collisions"].items():
            n = populations[s_text]
            diagonal_denom = n + 2 * collisions
            plugin_s2 = n * n / diagonal_denom
            if collisions:
                offdiag_s2 = (n * (n - 1) // 2) / collisions
                offdiag_h2 = math.log(offdiag_s2)
            else:
                offdiag_s2 = None
                offdiag_h2 = None
            row["diagnostics"][s_text] = {
                "plugin_S2": plugin_s2,
                "plugin_H2_natural": math.log(plugin_s2),
                "offdiag_S2": offdiag_s2,
                "offdiag_H2_natural": offdiag_h2,
            }


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("x", type=int)
    ap.add_argument("--output-dir", type=Path, default=Path("/tmp"))
    args = ap.parse_args()
    started = time.perf_counter()
    par = REF.d0_parameters(args.x)
    g, sites = sites_for(args.x, par)
    expected = production_n()
    populations: dict[str, int] = {}
    for s in S_VALUES:
        observed = int(np.sum(sites >= s + 1))
        want = expected[(args.x, s)]
        if observed != want:
            raise RuntimeError(
                f"x={args.x} s={s}: site count {observed} != {want}"
            )
        populations[str(s)] = observed
    J, K = par["J"], par["K"]
    paths = (
        ("pre_first", [(j,) for j in range(J)]),
        ("pre_last", [(j,) for j in range(J - 1, -1, -1)]),
        ("suf_first", [(J + 1 + j,) for j in range(K)]),
        ("suf_last", [(J + K - j,) for j in range(K)]),
        (
            "joint_first",
            [(j, J + 1 + j) for j in range(min(J, K))],
        ),
        (
            "joint_inner",
            [
                (J - 1 - j, J + 1 + j)
                for j in range(min(J, K))
            ],
        ),
        (
            "joint_outer",
            [
                (j, J + K - j)
                for j in range(min(J, K))
            ],
        ),
        (
            "joint_reverse",
            [
                (J - 1 - j, J + K - j)
                for j in range(min(J, K))
            ],
        ),
    )
    result: dict[str, object] = {
        "schema": "item-0010-flank-frontier-eight-path-panel-v1",
        "classification": (
            "MEASURED exact finite reconstruction from regenerable cache; "
            "positive-s counts are exact deletions from s=0 classes"
        ),
        "x": args.x,
        "parameters": {
            k: par[k] for k in ("D", "J", "K", "L", "W_floor")
        },
        "N": populations,
        "paths": {},
    }
    for name, steps in paths:
        curve = refine_curve(g, sites, steps)
        enrich_entropy(curve, populations)
        result["paths"][name] = curve
        print(
            f"x={args.x} finished {name} in "
            f"{time.perf_counter() - started:.1f}s",
            flush=True,
        )
    result["elapsed_seconds"] = time.perf_counter() - started
    result["max_rss_kib"] = resource.getrusage(
        resource.RUSAGE_SELF
    ).ru_maxrss
    output = args.output_dir / f"flank-panel-{args.x}.json"
    output.write_text(json.dumps(result, indent=2) + "\n")
    print(
        f"x={args.x} wrote {output}; elapsed="
        f"{result['elapsed_seconds']:.3f}s rss={result['max_rss_kib']} KiB",
        flush=True,
    )


if __name__ == "__main__":
    main()
