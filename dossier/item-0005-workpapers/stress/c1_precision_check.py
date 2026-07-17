# Independent precision-check of the C1 obstruction + my own counter-attempts.
# All identity checks in exact rational arithmetic (Fraction), independent code
# path from c1_numerics.py.
from fractions import Fraction as F
import sympy, bisect

NP = 1200
primes = list(sympy.primerange(2, sympy.prime(NP) + 1))[:NP]
p = lambda n: primes[n - 1]
def pi(m):
    return bisect.bisect_right(primes, m)

# ---------------------------------------------------------------- check 1
# Transpose identity I1, reimplemented independently:
# sum_{m=0}^{p_{N+1}-1} 2^{-pi(m)}  ==  sum_{n<=N} p_n 2^{-n} + p_{N+1} 2^{-N}
def chk_I1(N):
    lhs = sum(F(1, 2 ** pi(m)) for m in range(0, p(N + 1)))
    rhs = sum(F(p(n), 2 ** n) for n in range(1, N + 1)) + F(p(N + 1), 2 ** N)
    return lhs == rhs
print("CHK1 I1 transpose:", all(chk_I1(N) for N in (1, 2, 4, 7, 13, 40, 90, 200)))

# ---------------------------------------------------------------- check 2
# Tail collapse I4: for p_n <= M < p_{n+1}, truncated at N:
#   sum_{M<m<p_{N+1}} 2^{-pi(m)} == 2^{-n}( (p_{n+1}-1-M) + delta_n^{(N)} )
# with delta_n^{(N)} = sum_{j=1}^{N-n} g_{n+j} 2^{-j}   (truncated delta).
def chk_I4(M, N):
    n = pi(M)
    lhs = sum(F(1, 2 ** pi(m)) for m in range(M + 1, p(N + 1)))
    dtr = sum(F(p(n + j + 1) - p(n + j), 2 ** j) for j in range(1, N - n + 1))
    rhs = F(1, 2 ** n) * (F(p(n + 1) - 1 - M, 1) + dtr)
    return lhs == rhs
print("CHK2 I4 tail=offset+delta:",
      all(chk_I4(M, N) for (M, N) in ((3, 9), (8, 10), (9, 10), (24, 40),
                                       (25, 40), (89, 80), (97, 80), (541, 300))))

# ---------------------------------------------------------------- check 3
# Gap series affine identity: sum_{n=1}^{N} g_n 2^{-n} = S_N + p_{N+1} 2^{-N} - 2
# (limit: sum g_n 2^-n = S - 2).  Needed for my decimation counter-attempt.
def chk_gap(N):
    lhs = sum(F(p(n + 1) - p(n), 2 ** n) for n in range(1, N + 1))
    rhs = sum(F(p(n), 2 ** n) for n in range(1, N + 1)) + F(p(N + 1), 2 ** N) - 2
    return lhs == rhs
print("CHK3 sum g_n 2^-n = S - 2 (finite form):",
      all(chk_gap(N) for N in (1, 2, 5, 17, 60, 300)))

# ---------------------------------------------------------------- check 4
# MY COUNTER-ATTACK 1a: mod-2 decimation of the ARGUMENT of the transpose
# form.  Claim: it is EXACT but collapses back to an affine function of S:
#   sum_{m>=1} 2^{-pi(2m)} = S/2 - 3/4.
# Finite check: compare partial sums at high precision.
import mpmath as mp
mp.mp.dps = 120
Nn = 380  # index depth
Sval = mp.mpf(0)
for n in range(1, Nn + 1):
    Sval += mp.mpf(p(n)) * mp.power(2, -n)
# tail of S below 2^-Nn * p_{Nn+1}: fine at dps 120 for ~110 digit agreement? no:
# 2^-380 ~ 10^-114. OK ~ 110 digits.
D2 = mp.mpf(0)
m = 1
while 2 * m < p(Nn + 1):
    D2 += mp.power(2, -pi(2 * m))
    m += 1
pred = Sval / 2 - mp.mpf(3) / 4
print("CHK4 mod-2 decimation affine in S: |D2 - (S/2 - 3/4)| =",
      mp.nstr(abs(D2 - pred), 5), " (should be ~2^-Nn level, i.e. < 1e-100)")

# ---------------------------------------------------------------- check 5
# MY COUNTER-ATTACK 1b: mod-4 decimation D4 = sum_m 2^{-pi(4m)}.
# If this were affine in S over low-height rationals, a second family COULD
# arise.  PSLQ (1, S, D4): expect NO low-height relation (p_n mod 4 enters).
mp.mp.dps = 400
Nn2 = 1150
S2 = mp.mpf(0)
for n in range(1, Nn2 + 1):
    S2 += mp.mpf(p(n)) * mp.power(2, -n)
D4 = mp.mpf(0)
m = 1
while 4 * m < p(Nn2 + 1):
    D4 += mp.power(2, -pi(4 * m))
    m += 1
rel = mp.pslq([mp.mpf(1), S2, D4], maxcoeff=10 ** 20, maxsteps=50000)
print("CHK5 PSLQ (1, S, D4) maxcoeff 1e20:", rel)
# also mod-2 decimation sanity through PSLQ (should FIND (3, -2, 4)):
D2b = mp.mpf(0)
m = 1
while 2 * m < p(Nn2 + 1):
    D2b += mp.power(2, -pi(2 * m))
    m += 1
rel2 = mp.pslq([mp.mpf(1), S2, D2b], maxcoeff=10 ** 20, maxsteps=50000)
print("CHK5b PSLQ (1, S, D2) (expect (3,-2,4) ~ D2 = S/2-3/4):", rel2)

# ---------------------------------------------------------------- check 6
# MY COUNTER-ATTACK 2: value-translation family sum_n pi(p_n + t) 2^{-n}
# = 2 + C_t,  C_t = sum_n c_{n,t} 2^{-n},  c_{n,t} = #{j>=1: p_{n+j} <= p_n+t}.
# For t = 2: c_{n,2} = 1_{g_n <= 2}.  PSLQ (1, S, C_2): expect NO low-height
# relation (twin-gap indicator is configuration data, not lattice data).
C2 = mp.mpf(0)
for n in range(1, Nn2 + 1):
    C2 += mp.mpf(1 if p(n + 1) - p(n) <= 2 else 0) * mp.power(2, -n)
rel3 = mp.pslq([mp.mpf(1), S2, C2], maxcoeff=10 ** 20, maxsteps=50000)
print("CHK6 PSLQ (1, S, C_2) maxcoeff 1e20:", rel3)

# ---------------------------------------------------------------- check 7
# Product-formula threshold arithmetic (Lemma 2): smallest nonzero |z| with
# z in (1/(b 2^n))Z is 1/(b 2^n); need 1/(b 2^n) > 2^{-p_n} i.e.
# p_n - n > log2 b for annihilation. Verify p_n - n is increasing/unbounded
# in the checked range (it is: p_n ~ n log n), report first n where
# p_n - n > 50 (covers b < 2^50).
n0 = next(n for n in range(1, NP) if p(n) - n > 50)
print("CHK7 threshold: p_n - n > 50 first at n =", n0, "(p_n =", p(n0), ")")

# ---------------------------------------------------------------- check 8
# Lemma 1(b) mechanics on a finite specimen: q' sum_h 1_P(m+h) 2^{-h} in Z
# would give 2^m q' T in Z.  Verify the rearrangement identity exactly:
# sum_{h=1}^{H} 1_P(m+h) 2^{-h} = 2^m ( T_{<=m+H} - T_{<=m} ) with
# T_{<=x} = sum_{p<=x} 2^{-p}.  Exact check.
def chk_L1b(mm, H):
    lhs = sum(F(1 if sympy.isprime(mm + h) else 0, 2 ** h) for h in range(1, H + 1))
    Tlo = sum(F(1, 2 ** q) for q in primes if q <= mm)
    Thi = sum(F(1, 2 ** q) for q in primes if q <= mm + H)
    return lhs == 2 ** mm * (Thi - Tlo)
print("CHK8 Lemma 1(b) rearrangement:",
      all(chk_L1b(mm, H) for (mm, H) in ((5, 30), (10, 64), (30, 100), (100, 200))))
