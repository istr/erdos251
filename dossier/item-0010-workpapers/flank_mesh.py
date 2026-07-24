#!/usr/bin/env python3
"""Exact canonical parity mesh for the item-0010 flank audit.

Computes E_J x E_K, where E_r = {1,r} union the positive even depths.
All diagonal cells are supplied separately by flank_panel.py's joint_first
curve.  Positive-s counts use exact deletions from each s=0 class.
"""

from __future__ import annotations

import argparse
import json
import resource
import time
from pathlib import Path

import numpy as np

from flank_panel import (
    BASE,
    S_VALUES,
    deletion_panel,
    production_n,
    sites_for,
)
from flank_panel import REF


def refine_state(
    g: np.ndarray,
    active_sites: np.ndarray,
    active_group: np.ndarray,
    offsets: tuple[int, ...],
) -> tuple[dict, np.ndarray, np.ndarray]:
    if not len(active_sites):
        return (
            {
                "pair_collisions": {str(s): 0 for s in S_VALUES},
                "s0_repeated_classes": 0,
                "s0_repeated_site_mass": 0,
                "s0_max_multiplicity": 1,
            },
            active_sites,
            active_group,
        )
    key = active_group.astype(np.uint64)
    for off in offsets:
        key = key * BASE + g[
            active_sites.astype(np.int64) + off
        ].astype(np.uint64)
    _, inverse, counts = np.unique(
        key, return_inverse=True, return_counts=True
    )
    row = {
        "pair_collisions": deletion_panel(
            counts, inverse, active_sites
        ),
        "s0_repeated_classes": int(np.sum(counts > 1)),
        "s0_repeated_site_mass": int(
            np.sum(counts[counts > 1], dtype=np.int64)
        ),
        "s0_max_multiplicity": int(counts.max()),
    }
    repeated_class = counts > 1
    repeated_site = repeated_class[inverse]
    next_sites = active_sites[repeated_site]
    relabel = np.cumsum(repeated_class, dtype=np.uint32) - 1
    next_group = relabel[inverse[repeated_site]]
    return row, next_sites, next_group


def parity_depths(depth: int) -> list[int]:
    return sorted({1, depth, *range(2, depth + 1, 2)})


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
    ej = parity_depths(J)
    ek = parity_depths(K)
    prefix_sites = sites
    prefix_group = np.zeros(len(sites), dtype=np.uint32)
    previous_j = 0
    cells: dict[str, dict] = {}
    prefix_checks: dict[str, dict] = {}
    for j in ej:
        prefix_offsets = tuple(range(previous_j, j))
        prefix_row, prefix_sites, prefix_group = refine_state(
            g, prefix_sites, prefix_group, prefix_offsets
        )
        prefix_checks[str(j)] = prefix_row
        previous_j = j

        joint_sites = prefix_sites
        joint_group = prefix_group
        previous_k = 0
        for k in ek:
            suffix_offsets = tuple(
                J + 1 + q for q in range(previous_k, k)
            )
            row, joint_sites, joint_group = refine_state(
                g, joint_sites, joint_group, suffix_offsets
            )
            row["j"] = j
            row["k"] = k
            cells[f"{j},{k}"] = row
            previous_k = k
        print(
            f"x={args.x} finished mesh row j={j} in "
            f"{time.perf_counter() - started:.1f}s",
            flush=True,
        )

    result = {
        "schema": "item-0010-flank-frontier-parity-mesh-v1",
        "classification": (
            "MEASURED exact finite reconstruction from regenerable cache; "
            "positive-s counts are exact deletions from s=0 classes"
        ),
        "x": args.x,
        "parameters": {
            k: par[k] for k in ("D", "J", "K", "L", "W_floor")
        },
        "N": populations,
        "E_J": ej,
        "E_K": ek,
        "prefix_checks": prefix_checks,
        "cells": cells,
        "elapsed_seconds": time.perf_counter() - started,
        "max_rss_kib": resource.getrusage(
            resource.RUSAGE_SELF
        ).ru_maxrss,
    }
    output = args.output_dir / f"flank-mesh-{args.x}.json"
    output.write_text(json.dumps(result, indent=2) + "\n")
    print(
        f"x={args.x} wrote {output}; elapsed="
        f"{result['elapsed_seconds']:.3f}s rss={result['max_rss_kib']} KiB",
        flush=True,
    )


if __name__ == "__main__":
    main()
