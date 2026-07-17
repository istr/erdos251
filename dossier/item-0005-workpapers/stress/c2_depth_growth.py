#!/usr/bin/env python3
# C2 (mine): does the single-site VALUE-RESIDUE trap grow strong enough to
# prove irrationality, or does it self-defeat / stall at finite exclusions?
#
# A depth-d site: run-end index n_d with g_{n_d-d+1..n_d} all == 0 mod 2^d
# (equivalently d+1 consecutive primes all congruent mod 2^d).
# Rationality S=a/(2^s b), b odd => IF n_d >= s THEN b delta_{n_d} == 0 mod 2^d,
# hence delta_{n_d} >= 2^d / b   (since delta_{n_d} > 0 integer/b).
# A site refutes (s,b) with s <= n_d and b < 2^d / delta_{n_d}.
#
# CRUX: track, across X, (i) max achievable depth d, (ii) the ratio
# R = 2^d / delta_{n_d} (= the largest odd b the site can exclude, +1),
# (iii) whether R grows with X (=> reaches larger b, but still only s<=n_d)
# or stalls. Also expose the SELF-DEFEAT geometry: 2^d vs the run's gaps
# vs the forward-looking delta_{n_d}.

import numpy as np

X = 100_000_000
print("sieving to", X, "...")
sieve = np.ones(X + 1, dtype=bool)
sieve[:2] = False
for p in range(2, int(X**0.5) + 1):
    if sieve[p]:
        sieve[p*p::p] = False
primes = np.flatnonzero(sieve)
gaps = np.diff(primes).astype(np.int64)
Np = len(primes)
print("primes below %d: %d" % (X, Np))

# 2-adic valuation of each gap
g = gaps.copy()
v2 = np.zeros_like(g)
gg = g.copy()
while True:
    even = (gg % 2 == 0) & (gg > 0)
    if not even.any():
        break
    v2[even] += 1
    gg[even] //= 2

# delta at gap-index i (tail starting after prime i+1): sum_{j>=1} g[i+j] 2^-j
# computed with 64 forward gaps (tail beyond is < 2^-64 * maxgap, negligible
# for our ratio purposes; we also form a rigorous UPPER bound separately).
def delta_at(i, terms=64):
    s = 0.0
    for j in range(1, terms + 1):
        if i + j < len(gaps):
            s += float(gaps[i + j]) * 2.0 ** (-j)
    return s

# rigorous-ish upper bound on delta_at(i): known forward gaps for j<=T plus
# a tail bound using the largest gap below X as a crude cap (delta tail
# <= maxgap * 2^-T). This is an honest upper bound within the sieved range.
maxgap = int(gaps.max())
def delta_upper(i, T=40):
    s = 0.0
    for j in range(1, T + 1):
        if i + j < len(gaps):
            s += float(gaps[i + j]) * 2.0 ** (-j)
    s += maxgap * 2.0 ** (-T)   # crude but valid within range
    return s

# For each depth d, find run-END gap-indices with d consecutive gaps having
# v2 >= d. Track the best site (max ratio 2^d/delta) per depth, per cutpoint.
cutpoints = [1_000_000, 3_000_000, 10_000_000, 30_000_000, 100_000_000]
# map prime value cut -> gap index cut
def gapidx_below(xcut):
    return int(np.searchsorted(primes, xcut)) - 2  # last gap fully below xcut

print("\n%-12s %5s %5s %10s %10s %8s  %s" %
      ("X", "maxd", "bestd", "2^d", "delta_end", "ratio", "excludes b< (site geometry)"))
for xcut in cutpoints:
    gi = gapidx_below(xcut)
    best = None  # (ratio, d, run_end_gapidx)
    maxd = 0
    for d in range(1, 12):
        ok = (v2[:gi] >= d)
        if not ok.any():
            continue
        # run-length encode consecutive True
        diff = np.diff(np.concatenate(([0], ok.view(np.int8), [0])))
        starts = np.flatnonzero(diff == 1)
        ends = np.flatnonzero(diff == -1)
        lens = ends - starts
        # a depth-d site needs a run of >= d consecutive v2>=d gaps
        good = lens >= d
        if not good.any():
            continue
        maxd = max(maxd, d)
        # for each qualifying run, the run-END gap index is starts + d - 1
        # (first window of length d); but the strongest is where forward
        # delta is smallest. Evaluate the end-of-first-window for each run.
        for st in starts[good]:
            run_end_gapidx = st + d - 1   # last gap of the length-d window
            de = delta_at(run_end_gapidx)
            if de <= 0:
                continue
            ratio = (2.0 ** d) / de
            if best is None or ratio > best[0]:
                best = (ratio, d, run_end_gapidx, de)
    if best is None:
        print("%-12d %5d  none" % (xcut, maxd))
        continue
    ratio, d, rei, de = best
    # geometry: the d gaps of the run and the forward gap
    run_gaps = gaps[rei - d + 1: rei + 1].tolist()
    fwd = gaps[rei + 1: rei + 6].tolist()
    excl_b = ratio  # largest b (real) with 2^d/b > de
    print("%-12d %5d %5d %10d %10.4f %8.3f  b<%.2f  rungaps=%s fwd=%s" %
          (xcut, maxd, d, 2**d, de, ratio, excl_b, run_gaps, fwd))

print("\nInterpretation:")
print(" - ratio = 2^d/delta_end = largest b the single site can exclude (for s<=n_d).")
print(" - If ratio grows with X, single-site reaches larger b but STILL only s<=n_d.")
print(" - 'rungaps' shows the self-defeat geometry: 2^d is set by the run's")
print("   own gap sizes; delta_end looks FORWARD at generic gaps (~log x).")
