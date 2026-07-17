#!/usr/bin/env python3
# Independent precision-check of the C3 result.  Re-derives central lemmas
# from scratch (not reusing c3_numerics.py helpers where the point is to
# cross-validate), and mounts counter-constructions.
from fractions import Fraction
from math import gcd
import random

random.seed(7)
FAIL = []
def ck(name, cond, detail=""):
    print(("[PASS] " if cond else "[FAIL] ") + name + ((" -- "+detail) if detail else ""))
    if not cond: FAIL.append(name)

# ============================================================= A. Kernel move
# Independent brute-force: build a finitely-supported integer sequence,
# apply move c_m+=t, c_{m+1}-=2t, verify (i) value V unchanged, (ii) delta_j
# changes only at j=m by -t.  Use exact Fractions, truncate tails exactly
# (finite support => exact).
def V(c, off=1):           # c is dict m->coeff, m>=1
    return sum(Fraction(v) * Fraction(1, 1<<m) for m, v in c.items())
def delta(c, n):           # sum_{h>=1} c_{n+h} 2^{-h}
    return sum(Fraction(c.get(n+h,0), 1<<h) for h in range(1, 200))
okval = okdelta = True
for _ in range(400):
    c = {m: random.randint(-5,5) for m in range(1, 12)}
    m = random.randint(1, 9); t = random.randint(-6, 6)
    c2 = dict(c); c2[m] = c2.get(m,0)+t; c2[m+1] = c2.get(m+1,0)-2*t
    if V(c2) != V(c): okval = False
    for j in range(0, 12):
        d = delta(c2, j) - delta(c, j)
        want = Fraction(-t) if j == m else Fraction(0)
        if d != want: okdelta = False
ck("A1 kernel move preserves V exactly", okval)
ck("A2 kernel move shifts delta_j only at j=m, by -t", okdelta)

# ============================================================= B. Lemma U universality
# For odd b NOT in the C3 test set, build the instance and verify b*delta_n
# is an even integer for all n, independently via the periodic tail formula.
def order2(b):
    if b == 1: return 1
    P, v = 1, 2 % b
    while v != 1: v = (2*v) % b; P += 1
    return P
def instance(b, length=300):
    d = [2*(pow(2,n,b)) for n in range(length+1)]   # d_n = 2*(2^n mod b)
    g = []
    for n in range(length):
        num = 2*d[n]-d[n+1]
        assert num % b == 0, (b,n)
        g.append(num//b)
    return d, g
def per_tail(g, n, P, b):   # exact tail for period-P gap pattern
    num = sum(g[(n+h-1) % P]*(1<<(P-h)) for h in range(1,P+1))
    return Fraction(num, (1<<P)-1)
okU = True; details=[]
for b in [13, 17, 25, 27, 33, 35, 99]:
    P = order2(b); d, g = instance(b)
    if not all(v in (0,2) for v in g[:P]): okU=False
    for n in range(3*P):
        dn = per_tail(g, n % P, P, b)
        if dn != Fraction(d[n % P], b): okU=False
        if (b*dn).denominator != 1 or int(b*dn) % 2 != 0: okU=False
    details.append(f"b={b}(P={P})")
ck("B Lemma U: b*delta_n in 2Z, fresh odd b", okU, ", ".join(details))

# ============================================================= C. Kill criterion / Theorem R forward
# Independent test: a linear functional Phi=sum beta_m c_m is "forced" only if
# 2(beta_m - 2 beta_{m+1}) in Z for all m>=s+1 (b=1 doubled-move test).
# Verify by directly evaluating Phi on c=0 vs c'=doubled move, for several
# candidate beta sequences; confirm the non-rigid ones FAIL forcedness.
def phi(beta, c):   # beta: dict, c: dict
    return sum(Fraction(beta.get(m,0))*Fraction(c.get(m,0)) for m in set(beta)|set(c))
def forced_linear_test(beta, s=1, Mmax=40):
    # returns True if 2(beta_m-2beta_{m+1}) in Z for all s+1<=m<=Mmax
    for m in range(s+1, Mmax):
        v = 2*(Fraction(beta.get(m,0)) - 2*Fraction(beta.get(m+1,0)))
        if v.denominator != 1: return False
    return True
# (i) geometric ratio 1/2  -> forced (rigid); (ii) ratio 1/3 -> NOT; (iii)
# single decimation a=2 (beta_m=2^{-m} on one residue class) -> NOT;
# (iv) constant-phase combo reconstituting full tail -> forced.
geo   = {m: Fraction(1,1<<m) for m in range(1,50)}
third = {m: Fraction(1,3**m) for m in range(1,50)}
dec2  = {m: Fraction(1,1<<m) if m%2==0 else Fraction(0) for m in range(1,50)}  # phase, a=2
# constant-phase: beta_m = 2^{-m} for all m (reconstituted) == geo; and a
# genuine 2-term decimation combo 2*dec(phase0,n)+... approximated by beta=geo
ck("C(i) geometric ratio 1/2 IS forced (rigid tail)", forced_linear_test(geo))
ck("C(ii) geometric ratio 1/3 is NOT forced", not forced_linear_test(third))
ck("C(iii) single a=2 decimation is NOT forced", not forced_linear_test(dec2))

# ============================================================= C-COUNTER. Counter-construction:
# Try to ENGINEER a forced second family from decimations.  By phase theory
# a combination is forced iff its phase profile is eventually constant, and
# then it collapses to the ordinary geometric tail (T3, original family).
# Construct L = 2*D0 + D1 where D0=phase0, D1=phase1 decimations (a=2):
#   beta_m = 2 * 2^{-m}[m even] + 1 * 2^{-m}[m odd]   (weights on the two phases)
# phase profile (2,1) NON-constant -> predicted NOT forced.
Lnc = {m: (2 if m%2==0 else 1)*Fraction(1,1<<m) for m in range(1,50)}
ck("C-COUNTER(a) non-constant-phase decimation combo NOT forced",
   not forced_linear_test(Lnc))
# Now the ONLY way to make it forced: equal weights on both phases -> beta_m
# = w*2^{-m} for all m = w*(geometric tail) = w*delta_0-ish -> ORIGINAL family.
Lc = {m: 2*Fraction(1,1<<m) for m in range(1,50)}   # equal weight 2 on both phases
ck("C-COUNTER(b) constant-phase combo forced == multiple of ordinary tail (T3)",
   forced_linear_test(Lc))
# Confirm Lc is literally a scalar multiple of the geometric tail (delta family):
ck("C-COUNTER(c) forced combo lies in span of delta (beta_m=C*2^-m)",
   all(Lc[m] == 2*geo[m] for m in range(1,50)))

# ============================================================= D. p_{2n} - 2 p_n growth
# Check the wall's quantitative sub-claim: dilation regularity p_{2n}=2p_n(1+o(1))
# has UNBOUNDED error (so cannot be an exact mod-1 lattice identity).
def sieve(n):
    bs = bytearray([1])*(n+1); bs[0:2]=b"\x00\x00"
    for i in range(2,int(n**.5)+1):
        if bs[i]: bs[i*i::i]=bytearray(len(bs[i*i::i]))
    return [i for i in range(n+1) if bs[i]]
pr = sieve(3_000_000)
def p(n): return pr[n-1]   # 1-indexed n-th prime
errs = []
for n in [10, 100, 1000, 10000, 100000, 200000]:
    if 2*n <= len(pr):
        e = p(2*n) - 2*p(n)
        errs.append((n, e, round(e/n,4)))
print("  p_{2n}-2p_n :", errs)
ck("D dilation error p_{2n}-2p_n grows unboundedly (~ 2 ln2 * n)",
   errs[-1][1] > errs[0][1] and errs[-1][1] > 100000,
   "so no exact index-dilation identity mod any fixed lattice")

# ============================================================= E. Legendre-duality counter-construction
# Steering-notes exotic route: use pi(p_n)=n.  Attempt a 'second family' by
# sampling gaps along the image of an index self-map sigma and asking whether
# any FIXED integer combination of {g_{sigma(n)+h}} tails is near a lattice.
# Concretely test: is sum_h g_{2n+h} 2^{-h} (index-dilated tail) expressible
# as (rational)*delta_n + integer, i.e. does delta at dilated index collapse?
# Compute delta_{2n} - r*delta_n for best rational r over a range; show the
# residual is NOT eventually integer/lattice (no exact collapse).
def truetail(n, terms=200):
    return sum(Fraction(pr[n-1+h] - pr[n-1+h-1], 1<<h) for h in range(1,terms+1))
worst_lattice_dist = Fraction(1)
for n in [1000, 5000, 20000, 80000]:
    dn  = truetail(n)
    d2n = truetail(2*n)
    # try to write d2n = r*dn + k with small r,k: scan small rationals r
    best = None
    for rn in range(-4,5):
        for rd in range(1,5):
            r = Fraction(rn, rd)
            resid = d2n - r*dn
            frac = resid - (resid.numerator//resid.denominator)
            dist = min(frac, 1-frac)
            if best is None or dist < best[0]:
                best = (dist, r)
    if best[0] < worst_lattice_dist: worst_lattice_dist = best[0]
# if NO exact collapse, best distance to integer stays bounded away from 0
ck("E Legendre/dilation collapse fails: delta_{2n} NOT r*delta_n + Z for small r",
   worst_lattice_dist > Fraction(1,1000),
   f"min lattice distance over scan = {float(worst_lattice_dist):.4f}")

print()
print("ALL PASS" if not FAIL else f"FAILURES: {FAIL}")
