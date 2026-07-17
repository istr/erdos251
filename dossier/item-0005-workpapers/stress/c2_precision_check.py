#!/usr/bin/env python3
# Precision-check of the C2 obstruction sentence (verifier pass).
# (1) PARTIAL DEPTH: full 2^d divisibility at run-end needs s <= run-START;
#     s inside the run degrades depth to 2^{run_end - s}. Synthetic rational.
# (2) TRIVIAL-TAIL CERTIFICATE: the per-(s,b) trap works with ONLY the
#     dossier-internal Chebyshev-type bound p_n <= C0 n ln(n+2) =>
#     delta_M <= B_triv(M); the binding demand is the EXACT HEAD of length
#     T ~ log2 b + log2 p_N, not any extra-dossier tail bound.
# (3) SELF-DEFEAT arithmetic for Thm-3.3-constructible sites.
from fractions import Fraction
import math, numpy as np

# ---------- synthetic rational series with planted run (as in c2_synth) ----
# gaps: even, with a planted run of r=3 gaps == 0 mod 2^4 at positions n0+1..n0+r
# choose a periodic even-gap word => S-analog rational.
word = [2, 4, 16, 32, 48, 6, 2, 4]  # planted run 16,32,48 at positions 3,4,5 (1-based in word)
P = len(word)
# delta_n for periodic gaps: delta_n = sum_{j>=1} w[(n+j) mod P] 2^{-j}, exact:
# delta_n = (sum_{j=1}^{P} w[(n+j) mod P] 2^{P-j}) / (2^P - 1)
def delta_periodic(n):
    num = sum(word[(n + j) % P] << (P - j) for j in range(1, P + 1))
    return Fraction(num, (1 << P) - 1)
D = (1 << P) - 1  # 255 odd => b | 255 candidates; actual b = denominator odd part
b = delta_periodic(0).denominator
while b % 2 == 0: b //= 2
# find lcm denominator over one period (all delta_n share denominator dividing 255)
from math import lcm
den = 1
for n in range(P): den = lcm(den, delta_periodic(n).denominator)
bodd = den
while bodd % 2 == 0: bodd //= 2
s2 = 0; d2 = den
while d2 % 2 == 0: d2 //= 2; s2 += 1
print("(1) synthetic: denominator", den, " odd part b =", bodd, " 2-power s =", s2)
# run of gaps ==0 mod 2^4 occupies word positions i=3,4,5 (w[2],w[3],w[4]).
# run-start index N (delta_N multiplies 2^d) vs run-end N+d.
d = 4; r = 3
for start in range(0, P):
    ok = all(word[(start + i) % P] % (1 << d) == 0 for i in range(1, r + 1))
    if ok:
        N = start
        bdN  = bodd * delta_periodic(N)          # integer if s<=N (here s=0 effectively)
        bdNr = bodd * delta_periodic(N + r)
        assert bdN.denominator == 1 and bdNr.denominator == 1
        full = int(bdNr) % (1 << r) == 0  # depth r available with s <= N
        print("    run-start N=%d: b*delta_{N+r}=%d div by 2^r=%d: %s (s<=N case)"
              % (N, int(bdNr), 1 << r, full))
        # now emulate s INSIDE the run: s' = N+1 means we may only use
        # integrality from N+1 on: chain gives b delta_{N+r} == 0 mod 2^{r-1} only.
        # verify the sharper claim: 2^{r-j} | b delta_{N+r} for start N+j:
        for j in range(0, r + 1):
            got = int(bdNr) % (1 << (r - j)) == 0
            print("      if s = N+%d: guaranteed modulus 2^%d ; holds: %s"
                  % (j, r - j, got))
        break

# ---------- (2) certificate with ONLY the trivial tail bound ----------------
X = 30_000_000
sieve = np.ones(X + 1, dtype=bool); sieve[:2] = False
for p in range(2, int(X**0.5) + 1):
    if sieve[p]: sieve[p*p::p] = False
primes = np.flatnonzero(sieve); gaps = np.diff(primes).astype(np.int64)
NP = len(primes)
# explicit classical bound p_n < n(ln n + lnln n), n>=6 (Rosser); use C0=2 cushion:
def p_upper(n):  # upper bound for the n-th prime (1-indexed), n >= 6
    return n * (math.log(n) + math.log(math.log(n))) if n >= 6 else 14.0
# check it on our range (sanity, not proof):
chk = all(primes[n-1] < p_upper(n) for n in range(6, NP, 25013))
print("\n(2) explicit p_n bound sanity on sieved range:", chk)
def B_triv(M):
    # delta_M <= sum_{j>=1} p_{M+j+1} 2^{-j} <= sum (A+j)(lnA + j) ... closed form:
    A = M + 2  # p_{M+j+1} <= pu(A+j) with pu(n) = n(ln n + lnln n) monotone
    lnA = math.log(A) + math.log(math.log(A))
    # sum_{j>=1} (A+j)(lnA + j) 2^{-j} = A*lnA*1 + ... use exact small sums:
    # sum 2^-j = 1, sum j 2^-j = 2, sum j^2 2^-j = 6
    return (A * lnA) + (A * 2) + (lnA * 2) + 6.0
# empirical check B_triv dominates actual delta:
def delta_num(i, terms=60):
    ssum = 0.0
    for j in range(1, terms + 1):
        if i + j < len(gaps): ssum += float(gaps[i + j]) * 2.0 ** (-j)
    return ssum
worst = max(delta_num(M) / B_triv(M) for M in range(100, 400000, 3011))
print("    max delta_M/B_triv(M) sampled = %.4f  (must be < 1)" % worst)

def certificate(N, b):
    # trap for pair (s<=N, b) at site N using T exact gaps + trivial tail bound
    B = B_triv(N + 60)  # generous: T <= 60
    T = max(4, math.ceil(math.log2(b * B / 2.0)) + 3)  # width <= 1/4
    if T > 60 or N + T + 1 >= len(gaps): return None
    H = Fraction(0)
    for i in range(1, T + 1): H += Fraction(int(gaps[N + i]), 1 << i)
    lo = b * H
    wid = Fraction(b) * Fraction(math.ceil(B * 2**20), 2**20) / (1 << T)
    hi = lo + wid
    # certificate iff [lo, hi] contains no even integer:
    k = math.floor(lo / 2)
    return not (lo <= 2 * (k + 1) <= hi)

print("    certificate density using ONLY trivial tail bound (head length T):")
for b in [5, 101, 999, 9999, 99999]:
    Ns = range(1000, 1_500_000, 10007)
    res = [certificate(N, b) for N in Ns]
    res = [r for r in res if r is not None]
    Bx = B_triv(1_500_000); T = math.ceil(math.log2(b * Bx / 2.0)) + 3
    print("      b=%6d: T=%2d  certificate at %5.1f%% of sampled sites (n=%d)"
          % (b, T, 100.0 * sum(res) / len(res), len(res)))

# ---------- (3) Maynard-tight self-defeat arithmetic -----------------------
print("\n(3) Thm-3.3-constructible sites: d 2^d <= eps ln x forces ratio -> 0")
print("    %-10s %-6s %-8s %-10s %-12s" % ("ln x", "eps", "d_max", "2^d", "(2^d)/ln x"))
for lnx in [20, 50, 100, 500, 1000, 10000]:
    for eps in [0.5]:
        dmax = 0
        while (dmax + 1) * 2 ** (dmax + 1) <= eps * lnx: dmax += 1
        print("    %-10d %-6.2f %-8d %-10d %-12.4f"
              % (lnx, eps, dmax, 2**dmax, (2.0**dmax) / lnx))
print("    (ratio 2^d/delta ~ (2^d)/ln x <= eps/d -> 0; b>=1 only shrinks it)")
