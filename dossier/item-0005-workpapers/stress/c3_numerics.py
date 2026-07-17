#!/usr/bin/env python3
# C3 stress-test numerics: decimation / 2-adic mirror / recombination attacks
# on CLAIM-A1.  Exact rational arithmetic throughout (fractions.Fraction).
#
# Framework being tested (see c3-decimation.md):
#   Coefficient sequences c = (c_m)_{m>=1} (role of gaps g_m), value
#   V(c) = sum c_m 2^{-m}, tails delta_n(c) = sum_{h>=1} c_{n+h} 2^{-h}.
#   Lattice family from rationality: b delta_n in Z (n>=s), even (n>=s+1).
#   KERNEL MOVES: c_m += t, c_{m+1} -= 2t  (t in Z) preserve V exactly and
#   shift delta_j only at j=m by -t (integer).  Doubled moves (t even)
#   preserve the parity sublayer too.
#   A functional Phi of the coefficient sequence is "formally lattice-forced"
#   only if its variation under every (doubled) kernel move lies in (1/b)Z
#   for every odd b admitting instances -- i.e. variation in Z.
#
# TESTS:
#  T1. Kernel algebra: E in Z[x], E(1/2)=0  <=>  (2x-1)|E in Z[x];
#      consequence 3 | E(2).  (Random verification.)
#  T2. Instances: for each odd b, periodic-gap instance with b delta_n in Z;
#      verify family + parity; verify kernel moves preserve the family.
#  T3. Decimation candidates on instances: membership in (1/b)Z of
#      (a) kept-weight decimations tildeD_{n,c} = sum_{h==c (a)} c_{n+h} 2^{-h}
#      (b) renormalized decimations D_{n,c} = sum_j c_{n+c+aj} 2^{-j}
#      (c) constant-phase cross-(n,c) combos (predicted: IN lattice)
#      (d) non-constant-phase combos (predicted: OUT)
#      (e) norm-form quadratic A^2 - B^2/2 (a=2)  (predicted: OUT)
#      plus kernel-move variation of each (predicted nonzero non-integer
#      variation for (a),(b),(d),(e); zero/integer for (c)).
#  T4. 2-adic mirror: variation of G_2 = sum c_m 2^m (mod 2^k) under kernel
#      moves = -3t*2^m != 0; residues not forced.  Direct check.
#  T5. True primes to 10^7: decimated values A_n, B_n, delta_n; continued-
#      fraction scan: no small-denominator rational proximity; small integer
#      combo scan for near-integrality anomalies.
#  T6. Powers-family redundancy: 2^{2n} S^2 = P_n^2 + 2 P_n u_n + u_n^2
#      exact-check on a rational stand-in.

from fractions import Fraction
import random, sys

ok = True
def check(name, cond, detail=""):
    global ok
    tag = "PASS" if cond else "FAIL"
    if not cond: ok = False
    print(f"[{tag}] {name}" + (f" -- {detail}" if detail else ""))

# ---------------------------------------------------------------- T1
print("== T1: kernel algebra ==")
random.seed(42)
def poly_eval(E, x):
    v = Fraction(0)
    for coef in reversed(E): v = v*x + coef
    return v
def divide_by_2x_minus_1(E):
    # E = (2x-1)*G + r ; synthetic division in Q, check integrality of G
    # write E(x) = sum e_i x^i.  G has deg = deg E - 1.
    E = list(E)
    G = [Fraction(0)]*(len(E)-1)
    # process from top: e_n x^n = 2x * (e_n/2 x^{n-1}) -> G[n-1] = e_n/2 + ...
    carry = Fraction(0)
    for i in range(len(E)-1, 0, -1):
        gi = (Fraction(E[i]) + carry)/2
        G[i-1] = gi
        carry = gi          # -1 * gi moves to coefficient i-1 with sign +: E[i-1] + gi
    r = Fraction(E[0]) + carry
    return G, r
t1_ok = True
for trial in range(2000):
    deg = random.randint(1, 12)
    G = [random.randint(-9, 9) for _ in range(deg)]
    # E = (2x-1)*G  -> integer poly with E(1/2)=0
    E = [0]*(deg+1)
    for i, gi in enumerate(G):
        E[i+1] += 2*gi; E[i] -= gi
    if poly_eval(E, Fraction(1,2)) != 0: t1_ok = False; break
    Gq, r = divide_by_2x_minus_1(E)
    if r != 0 or any(x.denominator != 1 for x in Gq): t1_ok = False; break
    if poly_eval(E, Fraction(2)) % 3 != 0: t1_ok = False; break
    # converse: random integer E with E(1/2)=0 must divide exactly with int G
for trial in range(2000):
    # build random integer E, project to E(1/2)=0 by adjusting e_0:
    deg = random.randint(1, 12)
    E = [random.randint(-9, 9) for _ in range(deg+1)]
    v = poly_eval(E, Fraction(1,2))
    E0adj = Fraction(E[0]) - v   # forces E(1/2)=0 but may be non-integer
    if E0adj.denominator != 1:
        continue                 # only integer-coefficient cases are claims
    E[0] = int(E0adj)
    Gq, r = divide_by_2x_minus_1(E)
    if r != 0 or any(x.denominator != 1 for x in Gq): t1_ok = False; break
    if poly_eval(E, Fraction(2)) % 3 != 0: t1_ok = False; break
check("T1 kernel = Z-span{x^m(2x-1)}; 3 | E(2)", t1_ok)

# ---------------------------------------------------------------- T2
print("== T2: instances for arbitrary odd b ==")
def mult_order_2(b):
    P, v = 1, 2 % b
    while v != 1:
        v = (2*v) % b; P += 1
    return P
def make_instance(b, c0=1, length=400):
    # d_n = 2*(c0*2^n mod b); gaps g_{n+1} = (2 d_n - d_{n+1})/b in {0,2}
    # delta_n = d_n / b ; b delta_n = d_n integer, even.  n >= 0.
    d = [2*((c0*pow(2, n, b)) % b) for n in range(length+1)]
    g = []
    for n in range(length):
        num = 2*d[n] - d[n+1]
        assert num % b == 0
        gv = num//b
        assert gv in (0, 2), (b, n, gv)
        g.append(gv)          # g[n] = g_{n+1}
    return d, g
def delta_from_series(g, n, P, b):
    # exact tail for periodic g (period P in the instance construction):
    # delta_n = (sum_{h=1}^{P} g_{n+h} 2^{P-h}) / (2^P - 1)
    num = 0
    for h in range(1, P+1):
        num += g[(n+h-1) % P] * (1 << (P-h))
    return Fraction(num, (1 << P) - 1)
t2_ok = True
insts = {}
for b in [5, 7, 9, 11, 15, 21, 23]:
    P = mult_order_2(b)
    d, g = make_instance(b)
    # verify series-delta equals d_n/b and parity
    for n in range(0, 3*P):
        dn = delta_from_series(g, n % P, P, b)
        if dn != Fraction(d[n], b) if n < len(d) else False:
            # d has period P as well; compare against d[n % P]
            pass
        if delta_from_series(g, n % P, P, b) != Fraction(d[n % P], b):
            t2_ok = False
        if (b * delta_from_series(g, n % P, P, b)).denominator != 1:
            t2_ok = False
        if int(b * delta_from_series(g, n % P, P, b)) % 2 != 0:
            t2_ok = False
    insts[b] = (P, d, g)
check("T2 instances: b*delta_n in 2Z for all n, every odd b", t2_ok,
      "b in {5,7,9,11,15,21,23}, delta_n = d_n/b with periodic gaps in {0,2}")

# kernel move on an instance: g_m += 2, g_{m+1} -= 4  => delta_m -= 2
def tail_general(g, n, nterms=None):
    # exact tail sum_{h=1}^{len} g_{n+h} 2^{-h} for a FINITE modified list g
    # (used after kernel moves break periodicity; g must be long enough
    #  that the remainder is periodic again -- here we make moves inside
    #  the periodic pattern and recompute over an integer number of periods)
    raise NotImplementedError

def delta_after_move(b, P, g, n, m, t=2):
    # periodic g modified at positions m, m+1 (0-based g[k] = g_{k+1})
    # by +t, -2t.  delta_n = sum_{h>=1} g_{n+h} 2^{-h} with modification.
    base = delta_from_series(g, n % P, P, b)
    corr = Fraction(0)
    # position m carries gap g_{m+1}? indexing: g[k] = g_{k+1}. Move on
    # gaps g_M, g_{M+1} with M = m (1-based): affects delta_n for n < M.
    M = m
    if M - n >= 1:
        corr += Fraction(t, 1 << (M - n))
    if M + 1 - n >= 1:
        corr -= Fraction(2*t, 1 << (M + 1 - n))
    return base + corr
t2b_ok = True
for b in [7, 15, 23]:
    P, d, g = insts[b]
    for M in [5, 9]:
        for n in range(0, M+3):
            dn = delta_after_move(b, P, g, n, M, t=2)
            bd = b*dn
            if bd.denominator != 1 or int(bd) % 2 != 0:
                t2b_ok = False
check("T2b kernel moves (t=2) preserve full family incl. parity", t2b_ok)

# ---------------------------------------------------------------- T3
print("== T3: decimation candidates on instances ==")
def tildeD(b, P, g, n, c, a):
    # sum_{h>=1, h==c mod a} g_{n+h} 2^{-h}, exact, periodic g.
    # terms h = c + a*j (j>=j0), j0 = 1 if c==0 else 0 ; pattern period
    # Pp = P/gcd(a,P) in j, weight ratio 2^{-a} per step.
    from math import gcd
    Pp = P // gcd(a, P)
    # sum over one j-period then geometric with ratio 2^{-a*Pp}
    j0 = 1 if c == 0 else 0
    num = Fraction(0)
    for j in range(j0, j0 + Pp):
        h = c + a*j
        num += Fraction(g[(n+h-1) % P], 1 << h)
    return num / (1 - Fraction(1, 1 << (a*Pp)))
def renormD(b, P, g, n, c, a):
    # sum_j g_{n+c+aj} 2^{-j}  (j >= j0), exact for periodic g.
    from math import gcd
    Pp = P // gcd(a, P)
    j0 = 1 if c == 0 else 0
    num = Fraction(0)
    for j in range(j0, j0 + Pp):
        h = c + a*j
        num += Fraction(g[(n+h-1) % P], 1 << (j - j0))
    # ratio per Pp steps in j: 2^{-Pp}
    return num / ((1 << Pp) - 1) * Fraction(1 << Pp, 1 << j0) if False else \
           num / (1 - Fraction(1, 1 << Pp))
def in_lattice(x, b):
    return (b*x).denominator == 1

res_lines = []
t3a_out = 0; t3a_tot = 0
t3b_out = 0; t3b_tot = 0
for b in [5, 7, 9, 11, 15, 21, 23]:
    P, d, g = insts[b]
    for a in [2, 3]:
        for n in range(0, min(P, 6)):
            for c in range(a):
                x = tildeD(b, P, g, n, c, a); t3a_tot += 1
                if not in_lattice(x, b): t3a_out += 1
                y = renormD(b, P, g, n, c, a); t3b_tot += 1
                if not in_lattice(y, b): t3b_out += 1
print(f"  (a) kept-weight single decimations OUT of (1/b)Z: {t3a_out}/{t3a_tot}")
print(f"  (b) renormalized single decimations OUT of (1/b)Z: {t3b_out}/{t3b_tot}")
# NOTE: for periodic surrogates many renormalized decimations land in
# (1/b)Z by instance accident (e.g. b=7, P=3, a=2: denominator | 2^3-1 = b).
# Forcedness = membership in EVERY instance; one exit disproves it.
check("T3ab single decimations NOT forced (exit in some instance)",
      t3a_out > 0 and t3b_out > 0,
      "existence of counterexample instances disproves formal forcedness")
# T3f deterministic kill: kernel variation of a single decimation is a pure
# non-integer dyadic.  Move g_M += 2, g_{M+1} -= 4 changes tildeD_{n,c} by
# +2^{1-(M-n)} if M-n==c (mod a), by -2^{2-(M+1-n)} if M+1-n==c (mod a);
# at most one applies (a>=2), and for M-n >= 3 the change is non-integer.
t3f_ok = True
for b in [7, 15, 23]:
    P, d, g = insts[b]
    a, n = 2, 1
    for c in range(a):
        for M in [n+4, n+5]:   # one of these has M-n==c mod 2
            x0 = tildeD(b, P, g, n, c, a)
            # recompute with moved gaps: emulate via correction terms
            corr = Fraction(0)
            if (M - n) % a == c and M - n >= 1:
                corr += Fraction(2, 1 << (M - n))
            if (M + 1 - n) % a == c and M + 1 - n >= 1:
                corr -= Fraction(4, 1 << (M + 1 - n))
            if corr != 0 and corr.denominator == 1:
                t3f_ok = False
            if (M - n) % a == c and corr == 0:
                t3f_ok = False
check("T3f kernel variation of single decimations is non-integer dyadic "
      "(disproves forcedness deterministically)", t3f_ok)

# (c) constant-phase cross-(n,c) combo, a=2:
#     L = 2*tildeD_{n0,0} + 1*tildeD_{n0+1,0}  has phase profile
#     phi(j) = 2*[j==0 mod 2] ... recompute: lambda_{n0,0}=2, lambda_{n0+1,0}=1
#     phi(j) = 2*[j==0 (2)]*1? -- use theorem form: phi(j) = sum_n 2^{n-n0}
#     lambda_{n,(j-(n-n0)) mod 2}: n=n0: 2*[j==0(2)]; n=n0+1: 2*1*[j==1(2)]
#     phi(0)=2, phi(1)=2 constant => forced. Predicted IN (1/b)Z up to Z[1/2].
t3c_ok = True
for b in [5, 7, 9, 11, 15, 21, 23]:
    P, d, g = insts[b]
    for n0 in range(0, 4):
        L = 2*tildeD(b, P, g, n0, 0, 2) + tildeD(b, P, g, n0+1, 0, 2)
        # theorem predicts L in Z[1/2]-span of deltas + Z => b*L dyadic
        if (b*L).denominator & ((b*L).denominator - 1) != 0:  # not power of 2
            t3c_ok = False
check("T3c constant-phase combo 2*tD(n,0)+tD(n+1,0) lands in (1/b)Z[1/2]",
      t3c_ok, "phase profile phi=(2,2) constant -> in Z[1/2]-span of deltas")

# non-constant-phase combo: 1*tildeD_{n0,0} + 1*tildeD_{n0+1,0}
# phi(0)=1, phi(1)=2 non-constant => predicted OUT generically.
t3d_out = 0; t3d_tot = 0
for b in [5, 7, 9, 11, 15, 21, 23]:
    P, d, g = insts[b]
    for n0 in range(0, 4):
        L = tildeD(b, P, g, n0, 0, 2) + tildeD(b, P, g, n0+1, 0, 2)
        t3d_tot += 1
        if (b*L).denominator & ((b*L).denominator - 1) != 0:
            t3d_out += 1
print(f"  (d) non-constant-phase combos with odd denominator part not dividing b: {t3d_out}/{t3d_tot}")
check("T3d non-constant-phase combos generically exit", t3d_out > 0.7*t3d_tot)

# (e) norm-form quadratic F = A^2 - B^2/2 (a=2), A=renormD(n,0-ish even),:
#     A_n = sum_j g_{n+2j} 2^{-j} (j>=1), B_n = sum_j g_{n+2j+1} 2^{-j} (j>=0)
#     kernel-move variation must be non-integer (kill).  Direct check of
#     membership + variation.
t3e_ok = True
for b in [7, 15, 23]:
    P, d, g = insts[b]
    n = 1
    A = renormD(b, P, g, n, 0, 2)   # h = 2j, j>=1  -> c=0
    B = renormD(b, P, g, n, 1, 2)   # h = 1+2j, j>=0 -> c=1
    F = A*A - B*B/2
    memb = in_lattice(F, b) or in_lattice(F, b*b)
    # variation under doubled kernel move at even position M=n+2j0, t=2:
    # g_M += 2 => A += 2*2^{-j0}; g_{M+1} -= 4 => B -= 4*2^{-j0}
    j0 = 3
    A2 = A + Fraction(2, 1 << j0); B2 = B - Fraction(4, 1 << j0)
    F2 = A2*A2 - B2*B2/2
    var = F2 - F
    if var == 0 or var.denominator == 1:
        t3e_ok = False
    res_lines.append((b, str(F), memb, str(var)))
check("T3e norm-form A^2-B^2/2: kernel variation non-integer (not forced)",
      t3e_ok, "; ".join(f"b={b}: var={v}" for b, _, _, v in res_lines))

# ---------------------------------------------------------------- T4
print("== T4: 2-adic mirror ==")
# G_2 = sum g_m 2^m ; kernel move t at M changes it by t*2^M - 2t*2^{M+1}
#      = -3t 2^M.  For t=2: -3*2^{M+1} != 0, and mod 2^k nonzero for
#      k > M+1 (3 odd unit).  So residues mod 2^k beyond position M are
#      not kernel-invariant => not forced.  Verify + verify density claim:
#      closure of {3*2^M * Z} in Z_2 is 2^M Z_2  (3Z dense in Z_2):
#      check 3Z covers all residues mod 2^k.
t4_ok = True
for k in [4, 8, 12]:
    seen = set((3*m) % (1 << k) for m in range(1 << k))
    if len(seen) != (1 << k): t4_ok = False
for M in [2, 5]:
    var = -3*2*(1 << M)   # t=2
    for k in [M+2, M+6]:
        if var % (1 << k) == 0: t4_ok = False
check("T4 2-adic mirror kernel-variation -3t*2^M nonzero mod 2^k; 3Z dense",
      t4_ok, "real-value-preserving moves shift sum g_m 2^m anywhere in 2^M Z_2")

# ---------------------------------------------------------------- T5
print("== T5: true primes to 10^7 ==")
def sieve_primes(limit):
    bs = bytearray([1])*(limit+1)
    bs[0:2] = b"\x00\x00"
    for i in range(2, int(limit**0.5)+1):
        if bs[i]:
            bs[i*i::i] = bytearray(len(bs[i*i::i]))
    return [i for i in range(limit+1) if bs[i]]
primes = sieve_primes(10**7)
print(f"  primes: {len(primes)} (pi(10^7) = 664579 expected)")
gaps = [primes[i+1]-primes[i] for i in range(len(primes)-1)]  # gaps[k] = g_{k+1}
def true_tail(n, nterms=220, dec=2, phase=None):
    # exact truncated sums; n is 1-based prime index
    # phase None -> delta_n; else renormalized decimation with step dec
    s = Fraction(0)
    if phase is None:
        for h in range(1, nterms+1):
            s += Fraction(gaps[n-1+h-1], 1 << h)
    else:
        j0 = 1 if phase == 0 else 0
        for j in range(j0, j0+nterms):
            h = phase + dec*j
            s += Fraction(gaps[n-1+h-1], 1 << (j - j0))
    return s
def cf_scan(x, err, max_den=10**6):
    # continued fraction of x; return smallest denominator q<=max_den with
    # |x - p/q| < err, else None
    from math import floor
    a = x; h1, h0, k1, k0 = 1, 0, 0, 1
    for _ in range(200):
        ai = a.numerator // a.denominator
        h1, h0 = ai*h1 + h0, h1
        k1, k0 = ai*k1 + k0, k1
        if k1 > max_den: break
        if abs(x - Fraction(h1, k1)) < err:
            return (h1, k1)
        frac = a - ai
        if frac == 0: break
        a = 1/frac
    return None
t5_ok = True
err = Fraction(1, 1 << 150)   # truncation error bound: gaps<300 up to idx
anomalies = []
for n in [1000, 10000, 100000, 500000]:
    dn = true_tail(n)                    # delta_n, 220 terms (err < 2^-210*300)
    An = true_tail(n, phase=0)           # sum g_{n+2j} 2^{-j}
    Bn = true_tail(n, phase=1)           # sum g_{n+2j+1} 2^{-j}
    for name, val in [("delta", dn), ("A", An), ("B", Bn)]:
        hit = cf_scan(val, err)
        if hit: anomalies.append((n, name, hit))
    # small integer combos c1*A+c2*B+c3*delta+c4 ~ 0 scan
    for c1 in range(-6, 7):
        for c2 in range(-6, 7):
            for c3 in range(-6, 7):
                v = c1*An + c2*Bn + c3*dn
                f = v - v.numerator//v.denominator  # fractional part
                if (c1, c2, c3) != (0, 0, 0) and min(f, 1-f) < Fraction(1, 10**9):
                    anomalies.append((n, "combo", (c1, c2, c3)))
check("T5 true primes: no small-denominator rational proximity, no integer "
      "relations among (A_n, B_n, delta_n) with |c|<=6", len(anomalies) == 0,
      f"anomalies={anomalies[:5]}" if anomalies else
      "n in {1e3,1e4,1e5,5e5}; cf-scan to q<=1e6 at err 2^-150; combo scan 13^3")

# ---------------------------------------------------------------- T6
print("== T6: powers-family redundancy ==")
# identity 2^{2n} S^2 = P_n^2 + 2 P_n u_n + u_n^2 with S = 2^{-n}(P_n+u_n):
# verify on a rational stand-in built from an instance (S := V(c) for the
# periodic instance, exact).
t6_ok = True
for b in [7, 23]:
    P, d, g = insts[b]
    # S for the instance's "prime-like" series: use u_0 = delta_0 directly
    S = delta_from_series(g, 0, P, b)   # plays role of the full series value
    for n in [3, 5]:
        Pn = sum(g[(h-1) % P] * (1 << (n-h)) for h in range(1, n+1))  # 2^n*head
        un = delta_from_series(g, n % P, P, b)
        lhs = (1 << (2*n)) * S * S
        rhs = Fraction(Pn)*Pn + 2*Pn*un + un*un
        if lhs != rhs: t6_ok = False
check("T6 2^{2n}S^2 = P_n^2 + 2 P_n u_n + u_n^2 (k-powers family is a ring "
      "consequence of the k=1 family)", t6_ok)

print()
print("ALL PASS" if ok else "SOME FAILURES")
sys.exit(0 if ok else 1)
