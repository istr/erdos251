"""Precision-check numerics for the C5 obstruction sentence repair.

Checks:
 R1. Weighted absorption identity (pointwise, exact):
     for p0, p distinct primes, p*p0 | n, h >= 1:
       omega(n+p*h) * 1_{p0 | n+p*h}
         == (omega(n//p + h) + 1 - 1_{p^2 | n+p*h}) * 1_{p0 | h}
 R2. Series-level (5.2)-analogue for the weighted series, as an exact
     real identity (pre-mod-1), truncated tail:
       sum_h omega(n+p*h) 1_{p0|n+p*h} 2^-h
         == sum_h omega(n//p+h) 1_{p0 | n//p + h} 2^-h
            + 1/(2^p0 - 1) - sum_{p0|h} 1_{p^2|n+p*h} 2^-h
     (uses p0 | n//p, so the first RHS term is the translated family
      of the SAME weighted series at argument n//p.)
 R3. Value of X_{p0} = sum_m omega(m) 1_{p0|m} 2^-m
         == 1/(2^p0-1) + sum_{p != p0} 1/(2^{p*p0}-1)
     (value-position character of the weighted series).
 R4. Telescoping rational family: r(n) = 2u(n) - u(n+1), u integer,
     u(n) = o(2^n)  =>  sum r(n) 2^-n = u(1).  Test u(n)=n^2 and
     u(n)=p_n (the latter reproduces sum (2p_n - p_{n+1}) 2^-n = p_1 = 2).
     This kills 'the only provably-rational residual family is polynomial'.
 R5. Re-verify file checks: (5) X_G identity, (3) sum pi(m)2^-m = 2 sum_p 2^-p,
     (6) second differences of p_{2m}-p_m nonconstant sign-changing.
 R6. Small-denominator scan: S - sum_p 1/(2^p-1) close to no rational with
     denominator <= 10^6 (supports absence of accidental degeneracy only).
"""
from sympy import primerange, primepi, factorint, isprime
from fractions import Fraction
import math, random

PMAX = 200000
PRIMES = list(primerange(2, PMAX))
random.seed(251)

def omega(m):
    return len(factorint(m))

# ---------- R1: pointwise weighted absorption ----------
fail = 0
for _ in range(400):
    p0, p = random.sample(PRIMES[:60], 2)
    k = random.randint(1, 50)
    n = p * p0 * k
    h = random.randint(1, 40)
    lhs = omega(n + p * h) * (1 if (n + p * h) % p0 == 0 else 0)
    rhs = (omega(n // p + h) + 1 - (1 if (n + p * h) % (p * p) == 0 else 0)) \
          * (1 if h % p0 == 0 else 0)
    if lhs != rhs:
        fail += 1
        print("R1 FAIL", p0, p, n, h, lhs, rhs)
print("R1 weighted absorption identity:", "PASS" if fail == 0 else "FAIL")

# ---------- R2: series-level exact identity (Fraction arithmetic) ----------
H = 220  # truncation; numerators omega ~ small, tail < (H)*2^-H negligible; use exact Fractions and compare truncations of both sides with identical support
ok = True
for (p0, p, k) in [(3, 5, 7), (5, 2, 9), (3, 2, 11), (7, 11, 2), (5, 3, 4)]:
    n = p * p0 * k
    lhs = sum(Fraction(omega(n + p * h) * (1 if (n + p * h) % p0 == 0 else 0), 2**h)
              for h in range(1, H + 1))
    t1 = sum(Fraction(omega(n // p + h) * (1 if (n // p + h) % p0 == 0 else 0), 2**h)
             for h in range(1, H + 1))
    t2 = sum(Fraction(1, 2**h) for h in range(1, H + 1) if h % p0 == 0)
    t3 = sum(Fraction(1 if (n + p * h) % (p * p) == 0 else 0, 2**h)
             for h in range(1, H + 1) if h % p0 == 0)
    rhs = t1 + t2 - t3
    if lhs != rhs:
        ok = False
        print("R2 FAIL at", p0, p, n, float(lhs - rhs))
print("R2 series-level dilated family identity (truncated, exact Fractions):",
      "PASS" if ok else "FAIL")

# ---------- R3: value-position closed form of X_{p0} ----------
from mpmath import mp, mpf
mp.dps = 60
for p0 in (3, 5):
    M = 3000
    x = mpf(0)
    for m in range(p0, M + 1, p0):
        x += omega(m) * mpf(2) ** (-m)
    closed = mpf(2) ** (-p0) / (1 - mpf(2) ** (-p0))
    for p in PRIMES:
        if p == p0:
            continue
        e = p * p0
        if e > M:
            break
        closed += 1 / (mpf(2) ** e - 1)
    print("R3 p0=%d  |X_p0 - closed| = %s" % (p0, mp.nstr(abs(x - closed), 5)),
          "PASS" if abs(x - closed) < mpf(2) ** (-M + 50) else "FAIL")

# ---------- R4: telescoping rational families ----------
N = 300
u = lambda n: n * n
s4 = sum(Fraction(2 * u(n) - u(n + 1), 2**n) for n in range(1, N + 1))
# exact value = u(1) - u(N+1)/2^N -> u(1); check against partial boundary
print("R4a u=n^2: partial + boundary == u(1):",
      "PASS" if s4 + Fraction(u(N + 1), 2**N) == u(1) else "FAIL")
ps = list(primerange(2, 10**7))
NP = 200
s4b = sum(Fraction(2 * ps[n - 1] - ps[n], 2**n) for n in range(1, NP + 1))
print("R4b u=p_n: sum(2p_n - p_{n+1})2^-n + p_{N+1}2^-N == 2:",
      "PASS" if s4b + Fraction(ps[NP], 2**NP) == 2 else "FAIL")

# ---------- R5: re-verify file checks 3,5,6 ----------
M = 3000
lhs5 = mpf(0)
for m in range(2, M):
    # G(m) = gap containing m: p_k <= m < p_{k+1}
    k = primepi(m)
    if k == 0:
        continue
    pk = ps[k - 1]
    pk1 = ps[k]
    lhs5 += (pk1 - pk) * mpf(2) ** (-m)
rhs5 = mpf(0)
for k in range(1, len(ps)):
    if ps[k - 1] > M:
        break
    rhs5 += 2 * (ps[k] - ps[k - 1]) * (mpf(2) ** (-ps[k - 1]) - mpf(2) ** (-ps[k]))
print("R5-G |lhs-rhs| =", mp.nstr(abs(lhs5 - rhs5), 5),
      "PASS" if abs(lhs5 - rhs5) < mpf(2) ** (-M + 60) else "FAIL")

lhs3 = sum(int(primepi(m)) * mpf(2) ** (-m) for m in range(1, M))
rhs3 = 2 * sum(mpf(2) ** (-p) for p in ps if p < M)
print("R5-pi |lhs-rhs| =", mp.nstr(abs(lhs3 - rhs3), 5),
      "PASS" if abs(lhs3 - rhs3) < mpf(2) ** (-M + 60) else "FAIL")

d = [ps[2 * m - 1] - ps[m - 1] for m in range(1, 30)]
dd = [d[i + 2] - 2 * d[i + 1] + d[i] for i in range(len(d) - 2)]
print("R5-6 second differences of p_2m - p_m:", dd[:20],
      "PASS (nonconstant, sign-changing)" if len(set(dd)) > 2 and min(dd) < 0 < max(dd) else "FAIL")

# ---------- R6: small-denominator scan for S - W ----------
mp.dps = 80
S = sum(ps[n - 1] * mpf(2) ** (-n) for n in range(1, 260))
W = sum(1 / (mpf(2) ** p - 1) for p in ps if p < 300)
x = S - W
best = (1, abs(x - mp.floor(x + 0.5)))
from mpmath import mpf as _m
frac = x - mp.floor(x)
# continued-fraction convergents of frac up to denominator 10^6
a = frac
num0, den0, num1, den1 = 0, 1, 1, 0
val = frac
conv = []
for _ in range(40):
    ai = int(mp.floor(val))
    num0, num1 = num1, ai * num1 + num0
    den0, den1 = den1, ai * den1 + den0
    if den1 > 10**6:
        break
    conv.append((num1, den1, abs(frac - mpf(num1) / den1)))
    fp = val - ai
    if fp == 0:
        break
    val = 1 / fp
worst = min(c[2] * c[1] ** 2 for c in conv[1:]) if len(conv) > 1 else None
print("R6 S-W best convergent quality min(q^2*err) over q<=1e6:",
      mp.nstr(worst, 5) if worst is not None else "n/a",
      "(no small-denominator rational accident if >> 0; support-only)")
print("S =", mp.nstr(S, 30), " W =", mp.nstr(W, 30))
