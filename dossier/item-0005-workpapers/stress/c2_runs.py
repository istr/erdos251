#!/usr/bin/env python3
# C2 numerics 2: census of 2-power congruent runs in real primes.
# A "depth-d site" = index n with gaps g_{n+1..n+d} all == 0 (mod 2^d)
# (equivalently d+1 consecutive primes all congruent mod 2^d).
# Rationality of S would force b delta_{n+d} == 0 (mod 2^d), hence
# delta_{n+d} >= 2^d / b, at every such site with n >= s.
# Census: max depth d available below X, first site per depth, counts.

import numpy as np

X = 30_000_000
sieve = np.ones(X + 1, dtype=bool)
sieve[:2] = False
for p in range(2, int(X**0.5) + 1):
    if sieve[p]:
        sieve[p*p::p] = False
primes = np.flatnonzero(sieve)
gaps = np.diff(primes)
print("primes below %d: %d" % (X, len(primes)))

# v2(gap)
g = gaps.astype(np.int64)
v2 = np.zeros_like(g)
gg = g.copy()
mask = gg > 0
while True:
    even = (gg % 2 == 0) & (gg > 0)
    if not even.any():
        break
    v2[even] += 1
    gg[even] //= 2

# depth at position i (gap index i = gap between p_i and p_{i+1}, 0-based):
# max d such that v2[i], v2[i+1], ..., v2[i+d-1] >= d for run starting at i.
# compute per-t runs instead (simpler): for t = 1..12, run lengths of
# consecutive gaps with v2 >= t; depth contributed = min(runlen, t).
best_depth = 0
best_info = None
counts = {}
for t in range(1, 13):
    ok = v2 >= t
    # run-length encode
    d = np.diff(np.concatenate(([0], ok.view(np.int8), [0])))
    starts = np.flatnonzero(d == 1)
    ends = np.flatnonzero(d == -1)
    lens = ends - starts
    if len(lens) == 0:
        continue
    for depth in range(1, t + 1):
        c = int((lens >= depth).sum())
        if c > 0:
            counts[(t, depth)] = c
    m = int(lens.max())
    depth_t = min(m, t)
    i = int(starts[int(lens.argmax())])
    if depth_t > best_depth:
        best_depth = depth_t
        best_info = (t, m, i)
    print("t=%2d: runs of gaps ==0 mod 2^%d: count=%7d  maxlen=%2d  "
          "-> effective depth min(len,t)=%d" % (t, t, len(lens), m, depth_t))

t, m, i = best_info
print("\nbest depth below %d: d = %d  (t=%d, runlen=%d)" % (X, best_depth, t, m))
print("site: consecutive primes", primes[i:i + m + 2].tolist())
print("gaps:", gaps[i:i + m + 1].tolist())

# What does the site demand of rationality? b delta_{n+d} >= 2^d, i.e.
# delta at run end >= 2^d/b. Actual delta there (truncated, converges fast):
i_end = i + min(m, t)
dl = float(sum(int(gaps[i_end + j]) * 2.0**-(j + 1) for j in range(60)))
print("actual delta_{n+d} at best site = %.6f  vs forced >= 2^%d/b = %g/b"
      % (dl, best_depth, 2.0**best_depth))
print("=> any rational S with odd b < %g is contradicted by this single site"
      % (2.0**best_depth / dl), "(IF the site index n >= s, which finite data")
print("   cannot certify against the unknown 2-power s -- see analysis file)")
