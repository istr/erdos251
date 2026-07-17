# C1 duality attack -- numerical verification layer (exact rational arithmetic
# where possible, high-precision PSLQ for dependence exclusion).
from fractions import Fraction as F
import sympy

# ---------------------------------------------------------------- primes
N_PRIMES = 900
primes = list(sympy.primerange(2, sympy.prime(N_PRIMES) + 1))
assert len(primes) >= N_PRIMES
primes = primes[:N_PRIMES]
p = lambda n: primes[n - 1]          # 1-indexed p_n
def pi(m):                           # prime counting
    import bisect
    return bisect.bisect_right(primes, m)

# ================================================================ I1
# Finite exact form: sum_{m=0}^{p_{N+1}-1} 2^{-pi(m)} = S_N + p_{N+1} 2^{-N}
# where S_N = sum_{n<=N} p_n 2^{-n}.  (Transpose/Fubini identity.)
def check_I1(N):
    lhs = sum(F(1, 2**pi(m)) for m in range(0, p(N + 1)))
    SN = sum(F(p(n), 2**n) for n in range(1, N + 1))
    rhs = SN + F(p(N + 1), 2**N)
    return lhs == rhs

I1_results = [check_I1(N) for N in (1, 2, 3, 5, 10, 25, 60, 120)]
print("I1 (S = sum_m 2^-pi(m), finite exact form):", I1_results)

# ================================================================ I2
# Finite exact form: sum_{m=1}^{M} pi(m) 2^{-m}
#                    = 2 sum_{p_n <= M} 2^{-p_n}  -  pi(M) 2^{-M}
def check_I2(M):
    lhs = sum(F(pi(m), 2**m) for m in range(1, M + 1))
    rhs = 2 * sum(F(1, 2**q) for q in primes if q <= M) - F(pi(M), 2**M)
    return lhs == rhs

I2_results = [check_I2(M) for M in (2, 3, 4, 10, 31, 100, 257, 600)]
print("I2 (sum pi(m)2^-m = 2T, finite exact form):", I2_results)

# ================================================================ I3
# Finite exact form: sum_{m=2}^{M} p_{pi(m)} 2^{-m} + p_{pi(M)} 2^{-M}
#                    = 2 sum_{n <= pi(M)} (p_n - p_{n-1}) 2^{-p_n},  p_0 := 0
def check_I3(M):
    lhs = sum(F(p(pi(m)), 2**m) for m in range(2, M + 1)) + F(p(pi(M)), 2**M)
    rhs = 2 * sum(F(p(n) - (p(n - 1) if n > 1 else 0), 2**p(n))
                  for n in range(1, pi(M) + 1))
    return lhs == rhs

I3_results = [check_I3(M) for M in (2, 3, 4, 10, 31, 100, 257, 600)]
print("I3 (largest-prime-below series, finite exact form):", I3_results)

# ================================================================ I4
# Tail identity: for p_n <= M < p_{n+1} (n = pi(M) >= 1), truncated at level N:
#   sum_{m=M+1}^{p_{N+1}-1} 2^{-pi(m)}
#   = (p_{n+1}-1-M) 2^{-n} + sum_{k=n+1}^{N} g_k 2^{-k}
# i.e. tail_M = 2^{-n} ( p_{n+1}-1-M + delta_n ) in the limit.
def check_I4(M, N):
    n = pi(M)
    lhs = sum(F(1, 2**pi(m)) for m in range(M + 1, p(N + 1)))
    rhs = F(p(n + 1) - 1 - M, 2**n) + sum(F(p(k + 1) - p(k), 2**k)
                                          for k in range(n + 1, N + 1))
    return lhs == rhs

I4_results = [check_I4(M, N) for (M, N) in
              ((2, 8), (4, 8), (9, 12), (10, 12), (25, 30), (97, 60), (100, 60))]
print("I4 (tail of transpose form = intra-run offset + delta):", I4_results)

# ================================================================ Mobius f
# f = mu * p (so that p_n = sum_{d|n} f(d)); show unbounded, full support.
def f(d):
    return sum(sympy.mobius(d // e) * p(e) for e in sympy.divisors(d))
fvals = [(d, f(d)) for d in range(1, 25)]
ok = all(sum(f(d) for d in sympy.divisors(n)) == p(n) for n in range(1, 40))
print("Mobius check sum_{d|n} f(d) = p_n:", ok)
print("f = mu*p values d=1..24:", fvals)
print("growth f(d)/p_d for d=18..24:",
      [round(f(d) / p(d), 3) for d in range(18, 25)])

# ================================================================ PSLQ
# Exclude small-height integer relations  c0 + c1 S + c2 T = 0  (and bilinear).
import mpmath as mp
mp.mp.dps = 1300   # ~4300 bits
BITS = 4200
# S = sum p_n 2^-n : tail after N terms < (p_{N+1}+2) 2^-N; N=1400 plenty? need
# p_n up to n ~ 4400 -> extend prime list.
primes_big = list(sympy.primerange(2, 45000))
S = mp.mpf(0)
n = 0
for q in primes_big:
    n += 1
    if n > 4400:
        break
    S += mp.mpf(q) * mp.power(2, -n)
T = mp.mpf(0)
for q in primes_big:
    if q > BITS + 50:
        break
    T += mp.power(2, -q)
print("S ~", mp.nstr(S, 30))
print("T ~", mp.nstr(T, 30))
rel_lin = mp.pslq([mp.mpf(1), S, T], maxcoeff=10**50, maxsteps=100000)
print("PSLQ linear (1,S,T), maxcoeff 1e50:", rel_lin)
rel_bil = mp.pslq([mp.mpf(1), S, T, S * T, S * S, T * T],
                  maxcoeff=10**25, maxsteps=100000)
print("PSLQ quadratic (1,S,T,ST,S^2,T^2), maxcoeff 1e25:", rel_bil)
