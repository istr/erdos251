#!/usr/bin/env python3
# C2 (mine): pin down WHY the single-site value-residue trap stalls.
# Hypothesis: unconditional depth (congruent prime strings, Shiu/Maynard16
# Thm 3.3) comes with a GENERIC forward tail delta_end ~ log x, while the
# forced bound is only 2^d ~ (achievable within run). So ratio 2^d/delta_end
# is ~1, and >1 only by coincidence (depth-d run happening to be followed by
# a small-gap tail) -- a joint (congruent-string + small-tail) constellation
# that is Hypothesis-A shaped, not Shiu-supplied.

import numpy as np

X = 100_000_000
sieve = np.ones(X + 1, dtype=bool)
sieve[:2] = False
for p in range(2, int(X**0.5) + 1):
    if sieve[p]:
        sieve[p*p::p] = False
primes = np.flatnonzero(sieve)
gaps = np.diff(primes).astype(np.int64)

g = gaps.copy(); v2 = np.zeros_like(g); gg = g.copy()
while True:
    even = (gg % 2 == 0) & (gg > 0)
    if not even.any(): break
    v2[even] += 1; gg[even] //= 2

def delta_at(i, terms=64):
    s = 0.0
    for j in range(1, terms + 1):
        if i + j < len(gaps):
            s += float(gaps[i + j]) * 2.0 ** (-j)
    return s

# (A) delta_end DISTRIBUTION over all depth-d sites. run-end gap index = st+d-1.
print("(A) forward-tail delta_end distribution at depth-d value-residue sites")
print("    (delta_end small => ratio 2^d/delta_end large => excludes bigger b)")
for d in range(2, 6):
    ok = (v2 >= d)
    if not ok.any():
        print("  d=%d: none" % d); continue
    diff = np.diff(np.concatenate(([0], ok.view(np.int8), [0])))
    starts = np.flatnonzero(diff == 1); ends = np.flatnonzero(diff == -1)
    lens = ends - starts; good = starts[lens >= d]
    if len(good) == 0:
        print("  d=%d: no run of length>=d" % d); continue
    des = np.array([delta_at(st + d - 1) for st in good])
    ratios = (2.0 ** d) / des
    print("  d=%d: %6d sites | delta_end: min=%.2f med=%.2f mean=%.2f max=%.2f"
          " | ratio 2^d/delta: max=%.2f frac(ratio>1)=%.3f frac(>3)=%.4f" %
          (d, len(good), des.min(), np.median(des), des.mean(), des.max(),
           ratios.max(), (ratios > 1).mean(), (ratios > 3).mean()))

# (B) the DEEPEST congruent strings (largest actual 2-adic run) and their
# forward tail -- do 'constructible-deep' sites have small or generic tails?
print("\n(B) deepest congruent strings vs their forward tail")
for d in [4]:
    ok = (v2 >= d)
    diff = np.diff(np.concatenate(([0], ok.view(np.int8), [0])))
    starts = np.flatnonzero(diff == 1); ends = np.flatnonzero(diff == -1)
    lens = ends - starts; good = starts[lens >= d]
    des = np.array([delta_at(st + d - 1) for st in good])
    order = np.argsort(des)  # smallest tail first
    print("  depth-%d sites, smallest-tail 3 and largest-tail 3:" % d)
    for idx in list(order[:3]) + list(order[-3:]):
        st = good[idx]; rei = st + d - 1
        print("    anchor p=%d rungaps=%s fwd=%s delta_end=%.3f ratio=%.3f" %
              (primes[rei - d + 1], gaps[rei-d+1:rei+1].tolist(),
               gaps[rei+1:rei+6].tolist(), des[idx], (2.0**d)/des[idx]))

# (C) confirm delta_n >= 2 (so b delta_n >= 2b >= 2; trap in (0,2) impossible)
mind = min(delta_at(i) for i in range(0, 200000, 7))
print("\n(C) min delta_n over sampled n = %.4f  (>= 2 always => b delta>=2;"
      " 'trap b delta in (0,2)' is impossible a priori)" % mind)

# (D) general-head parity trap vs divisibility: for a FIXED (s,b), the full
# head b*sum g 2^-k mod 2^{d} excludes b whenever the pinned residue r of
# b*delta_N mod 2^{d} has 0 < r and forces b delta_N off the even lattice,
# OR (divisibility) r=0 forces delta>=2^d/b. Show the general trap reaches
# more b per site, but is a per-(s,b) computation. Reproduce reach vs b.
print("\n(D) reach of the single-site parity/lattice trap vs b (per-(s,b),")
print("    NOT b-uniform): largest b excludable by ONE site of depth d")
print("    divisibility: b < 2^d/delta_end ; general head: needs tail bound")
for d in [3, 4]:
    print("    depth d=%d: b-free divisibility excludes odd b in {b: b<%.2f}"
          " -> {%s}" % (d, (2.0**d)/5.0,
          ",".join(str(b) for b in range(1, int(2**d/5.0)+1, 2))))
print("    (8.4 on record reaches b<=99999 by the GENERAL head trap with a")
print("     computed 2000-gap tail bound -- a finite per-(s,b) certificate,")
print("     not a uniform theorem: each larger b needs a deeper computed")
print("     tail (T ~ log2 b) and only settles s <= that site's index.)")
