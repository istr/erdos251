from fractions import Fraction as F

# sieve primes
N = 400000
sieve = bytearray([1])*N
sieve[0]=sieve[1]=0
for i in range(2,int(N**0.5)+1):
    if sieve[i]: sieve[i*i::i]=bytearray(len(sieve[i*i::i]))
primes=[i for i in range(N) if sieve[i]]

# S = sum p_n / 2^n, exact partial with 300 terms + tail bracket
T=300
S_lo = sum(F(primes[n-1], 2**n) for n in range(1,T+1))
# tail upper bound: p_{n} <= p_T * 2^{n-T} is crude; use actual primes for T..T+60 then geometric
S_hi = S_lo + sum(F(primes[n-1],2**n) for n in range(T+1,T+61)) + F(primes[T+59],2**(T+60))*2
print("S in [%.30f, %.30f]" % (S_lo, S_hi))

# identity 1: S = 2 + sum_{k>=1} g_k 2^{-k}
G_lo = 2 + sum(F(primes[k]-primes[k-1], 2**k) for k in range(1,T+1))
print("2+sum g_k/2^k partial = %.30f" % G_lo)
print("diff (should be ~2^-300 scale): %.3e" % float(S_lo - G_lo))

# identity 2: dual form S = sum_{m>=0} 2^{-pi(m)}
# pi(m) via sieve
import itertools
pi=0; D=F(0)
M=2000
picount=[0]*(M+1)
c=0
for m in range(M+1):
    if m>=2 and sieve[m]: c+=1
    picount[m]=c
D = sum(F(1,2**picount[m]) for m in range(M+1))
print("sum_m 2^-pi(m) partial = %.30f" % D)

# identity 3: E = sum_{m even} 2^{-pi(m)} =? S/2 + 1/4
E = sum(F(1,2**picount[m]) for m in range(0,M+1,2))
print("E = %.30f" % E)
print("S/2+1/4 = %.30f" % (S_lo/2+F(1,4)))
print("E - (S/2+1/4) = %.3e" % float(E - (S_lo/2+F(1,4))))

# probe: d=3 decimation -- is the interval count g_k/3 + f(p_k mod 3, g_k mod 3) exact?
# count #{m = 0 mod 3 in [p_k, p_k+g_k)} and compare with a function of (p_k mod 3, g_k mod 3)
from collections import defaultdict
table=defaultdict(set)
for k in range(2,3000):
    p=primes[k-1]; g=primes[k]-primes[k-1]
    cnt=sum(1 for m in range(p,p+g) if m%3==0)
    table[(p%3,g%3)].add(cnt-g//3)
print("d=3 correction sets by (p_k mod 3, g_k mod 3):", dict(table))

# pigeonhole counting demo: values b*delta_n would occupy range ~ b*max delta; count distinct
# (cannot test coincidences under rationality; just show delta range vs index count scale)
import math
def delta(n, J=80):
    return sum((primes[n+j]-primes[n+j-1])/2**j for j in range(1,J))
NN=20000
ds=[delta(n) for n in range(NN,2*NN)]
print("delta range on [N,2N], N=%d: min %.3f max %.3f; indices N=%d vs range*b(b=1000): %.0f" %
      (NN, min(ds), max(ds), NN, 1000*(max(ds)-min(ds))))
