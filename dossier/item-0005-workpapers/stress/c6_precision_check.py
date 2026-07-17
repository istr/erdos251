from fractions import Fraction as F
from collections import defaultdict

# ---- sieve ----
N = 600000
sieve = bytearray([1]) * N
sieve[0] = sieve[1] = 0
for i in range(2, int(N**0.5) + 1):
    if sieve[i]:
        sieve[i*i::i] = bytearray(len(sieve[i*i::i]))
primes = [i for i in range(N) if sieve[i]]
print("pi(%d) = %d" % (N, len(primes)))

# ---- CHECK 1 (exact, matched truncation): dual identity ----
# claim: sum_{m=0}^{p_K - 1} 2^{-pi(m)}  ==  sum_{k=1}^{K-1} p_k 2^{-k} + p_K 2^{1-K}
K = 200
pK = primes[K-1]
c = 0
A = F(0)
for m in range(pK):
    if m >= 2 and sieve[m]:
        c += 1
    A += F(1, 2**c)
rhs = sum(F(primes[k-1], 2**k) for k in range(1, K)) + F(primes[K-1], 2**(K-1))
print("CHECK1 dual identity exact:", A == rhs)

# ---- CHECK 2 (exact): even decimation  E_K == A_K/2 + 1/4 ----
c = 0
E = F(0)
for m in range(pK):
    if m >= 2 and sieve[m]:
        c += 1
    if m % 2 == 0:
        E += F(1, 2**c)
print("CHECK2 even-decimation exact:", E == A/2 + F(1,4))

# ---- CHECK 3: d=3 correction determinism + forbidden pairs ----
table = defaultdict(set)
for k in range(2, 40000):
    p = primes[k-1]; g = primes[k] - primes[k-1]
    cnt = sum(1 for m in range(p, p+g) if m % 3 == 0)
    table[(p % 3, g % 3)].add(cnt - g//3)
det = all(len(v) == 1 for v in table.values())
print("CHECK3 d=3 table:", dict((k, sorted(v)) for k, v in sorted(table.items())),
      "deterministic:", det, "forbidden (1,2)/(2,1) absent:",
      (1,2) not in table and (2,1) not in table)

# ---- CHECK 4: delta-width on [N,2N], N=12000 (file claims 45.2) ----
def delta(n, J=100):  # 1-indexed n; g_{n+j} = primes[n+j] - primes[n+j-1]
    return sum((primes[n+j] - primes[n+j-1]) / 2**j for j in range(1, J))
NN = 12000
ds = [delta(n) for n in range(NN, 2*NN)]
import math
print("CHECK4 delta-width on [12000,24000]: %.1f (ln N)^2 = %.1f ; max delta %.2f" %
      (max(ds) - min(ds), math.log(NN)**2, max(ds)))

# ---- CHECK 5: rigidity difference vectors are genuinely in G ----
# d_m = e_m - 2 e_{m+1}: delta_n(d_m) = 0 for n<m, -1 at n=m, 0 for n>m
# 2 e_{s+1}: delta_s = 1. Verify symbolically at finite truncation with Fractions.
def delta_of(seq, n, top):
    # seq: dict m->value, delta_n = sum_{j>=1} seq[n+j] 2^{-j}
    return sum(F(seq.get(n+j, 0), 2**j) for j in range(1, top - n + 1))
s = 3
for m in [5, 9]:
    dm = {m: 1, m+1: -2}
    vals = [delta_of(dm, n, m+2) for n in range(s, m+2)]
    ok = all(v == (F(-1) if n == m else F(0)) for n, v in zip(range(s, m+2), vals))
    print("CHECK5 d_%d tails:" % m, ok)
print("CHECK5 2e_{s+1}: delta_s =", delta_of({s+1: 2}, s, s+2))

# ---- CHECK 6: beta-chain kills a dilated functional (Phi(n,h)=n+2h) ----
# alpha_m = 2^{-h} at m=n0+2h (h=1..H), minus u*2^{-(m-tau)} for m>tau, tau=n0, u=1.
# rigidity (ii) requires beta_{m+1} == beta_m mod 2^{m-s}; verify failure.
n0, u, H, s0, bprime = 10, 1, 6, 3, 1
alpha = defaultdict(F)
for h in range(1, H+1):
    alpha[n0 + 2*h] += F(1, 2**h)
for m in range(n0+1, n0 + 2*H + 1):
    alpha[m] -= F(u, 2**(m - n0))
beta = {m: bprime * F(2**(m - s0)) * alpha[m] for m in range(n0+1, n0+2*H+1)}
viol = []
for m in range(n0+1, n0+2*H):
    d = beta[m+1] - beta[m]
    intgr = (beta[m].denominator == 1 and beta[m+1].denominator == 1)
    div = intgr and (d % (2**(m - s0)) == 0)
    if not (intgr and div):
        viol.append(m)
print("CHECK6 dilated-functional beta-chain violations at m =", viol, "(nonempty = certified impossible)")

# ---- CHECK 7: coincidence pigeonhole scale ----
# b*delta_n occupies <= b*width integer slots vs NN indices: report crossover
width = max(ds) - min(ds)
print("CHECK7 pigeonhole: N=%d indices vs b*width slots; forces coincidence for all b < %.0f" %
      (NN, NN / width))
