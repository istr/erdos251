from fractions import Fraction as F
import numpy as np, math

# ============================================================
# INDEPENDENT re-derivation checks of the C6 rigidity theorem
# and the near-miss family (P), by a precision-check agent.
# ============================================================

# ---- A. (P) family: exact tail periodicity under a SYNTHETIC rational S ----
# Build a "rational" scenario: choose b odd, s, integer gaps, integer seed D_s,
# propagate D_{n+1} = 2 D_n - b g_{n+1}. Then delta_n = D_n/b and we test
#   frac(delta_{n+ell}) = frac(delta_n)  for ord_b(2) | ell.
def ord2(b):
    if b == 1: return 1
    k, x = 1, 2 % b
    while x != 1:
        x = (x*2) % b; k += 1
    return k

for b in [3, 5, 7, 15, 17]:
    s = 2
    rng = np.random.default_rng(0)
    gaps = {n: int(2*rng.integers(1, 8)) for n in range(s+1, s+400)}  # even integer gaps
    D = {s: 4}                     # arbitrary integer seed D_s = b*delta_s in Z
    for n in range(s, s+399):
        D[n+1] = 2*D[n] - b*gaps[n+1]
    delta = {n: F(D[n], b) for n in D}
    L = ord2(b)
    ok = True
    for n in range(s, s+399-3*L):
        for ell in (L, 2*L, 3*L):
            if (delta[n+ell] - delta[n]).denominator != 1:   # must be an integer
                ok = False
    print(f"(P) b={b} ord_b(2)={L}: frac(delta_(n+ell))==frac(delta_n) for ord|ell : {ok}")
    # and CHECK it FAILS for ell NOT a multiple of ord (generic b): pick ell=1 if ord>1
    if L > 1:
        bad = any((delta[n+1]-delta[n]).denominator != 1 for n in range(s, s+50))
        print(f"        control: some frac(delta_(n+1))!=frac(delta_n) (expected True for ord>1): {bad}")

# ---- B. rigidity beta-chain: a TAIL functional is certified; a DILATION is not ----
# functional F(g)=sum alpha_m g_m ; beta_m = b'*2^{m-s}*alpha_m ; certified iff
# (i) beta_m in Z and (ii) beta_{m+1} == beta_m (mod 2^{m-s}).
s, bp = 3, 1
def betachain(alpha, lo, hi):
    beta = {m: bp*F(2**(m-s))*alpha.get(m, F(0)) for m in range(lo, hi)}
    vi, vii = [], []
    for m in range(lo, hi):
        if beta[m].denominator != 1: vi.append(m)
    for m in range(lo, hi-1):
        if beta[m].denominator==1 and beta[m+1].denominator==1:
            if (beta[m+1]-beta[m]) % (2**(m-s)) != 0: vii.append(m)
        else:
            vii.append(m)
    return vi, vii

# B1: the tail delta_j itself: alpha_m = 2^{-(m-j)} for m>j, else 0  (j=6)
j = 6
alpha_tail = {m: F(1, 2**(m-j)) for m in range(j+1, 40)}
vi, vii = betachain(alpha_tail, j+1, 40)
print(f"\n(rigidity) TAIL delta_{j}: (i)-violations {vi}  (ii)-violations {vii}  -> certified iff both empty")

# B2: a Z-combination of tails delta_4 + 3*delta_9 (should be certified)
alpha_comb = {}
for (jj, c) in [(4,1),(9,3)]:
    for m in range(jj+1, 40): alpha_comb[m] = alpha_comb.get(m, F(0)) + c*F(1, 2**(m-jj))
vi, vii = betachain(alpha_comb, 5, 40)
print(f"(rigidity) delta_4 + 3 delta_9        : (i)-violations {vi}  (ii)-violations {vii}")

# B3: dilated sampling Phi(n,h)=n+2h  (alpha at n0+2h = 2^-h), NOT a tail -> not certified
n0, H = 10, 8
alpha_dil = {}
for h in range(1, H+1): alpha_dil[n0+2*h] = alpha_dil.get(n0+2*h, F(0)) + F(1, 2**h)
vi, vii = betachain(alpha_dil, n0+1, n0+2*H+1)
print(f"(rigidity) DILATION n0+2h            : (i)-violations {vi}\n"
      f"                                       (ii)-violations {vii}  -> nonempty = NOT certified")

# ---- C. coincidence pigeonhole: slots b*N^theta vs N indices (needs theta<1) ----
LIMIT = 5_000_000
sieve = np.ones(LIMIT+1, dtype=bool); sieve[:2]=False
for i in range(2,int(LIMIT**0.5)+1):
    if sieve[i]: sieve[i*i::i]=False
p = np.nonzero(sieve)[0].astype(np.int64); g = np.diff(p); M=len(g)
delta = np.zeros(M); delta[M-1]=2.0
for t in range(M-2,-1,-1): delta[t]=0.5*(g[t]+delta[t+1])
for NN in [4000, 16000, 64000]:
    seg = delta[NN:2*NN]
    width = seg.max()-seg.min()
    print(f"\n(coincidence) N={NN}: delta-width={width:.2f}, (lnN)^2={math.log(NN)**2:.1f}, "
          f"N^0.525={NN**0.525:.0f}; forces coincidence for b < N/width = {NN/width:.0f}")
