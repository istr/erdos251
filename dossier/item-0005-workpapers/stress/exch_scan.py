import numpy as np, math, sys

LIMIT = 20_000_000
sieve = np.ones(LIMIT+1, dtype=bool); sieve[:2] = False
for i in range(2, int(LIMIT**0.5)+1):
    if sieve[i]: sieve[i*i::i] = False
p = np.nonzero(sieve)[0].astype(np.int64)
N = len(p)
g = np.diff(p)              # g[t] = p[t+1]-p[t], t=0..N-2 ; math: g_{t+1}
M = len(g)
print(f"pi({LIMIT}) = {N}, gaps = {M}, ln x = {math.log(LIMIT):.3f}")

# delta_code[t] = sum_{j>=1} g[t+j-1] 2^{-j}  (tail whose FIRST gap is g[t])
# math: delta_{n} with n+1 <-> t  i.e. delta_code[t] = delta_{t}  (0-based shift consistent throughout)
delta = np.zeros(M)
delta[M-1] = 2.0
for t in range(M-2, -1, -1):
    delta[t] = 0.5*(g[t] + delta[t+1])
VALID = M - 200   # discard last 200 sites (delta seed influence <= maxgap*2^-200)

gg = g.astype(np.int16)

def scan(J, K, D0, b=1, quiet=False):
    # site t carries: prefix g[t..t+J-1], middle g[t+J], suffix g[t+J+1..t+J+K]
    # tail conditions: delta[t+J] <= D0 (both fork tails), delta[t+J+K+1] <= 2**K (end tails)
    # gate for denominator b: b*(D0-2) < 2^{J+1}
    gate_ok = b*(D0-2) < 2**(J+1)
    twoK = 2**K
    n_sites = 0
    classes = {}
    for t in range(0, VALID - (J+K+2)):
        if delta[t+J] <= D0 and delta[t+J+K+1] <= twoK:
            n_sites += 1
            key = gg[t:t+J].tobytes() + b"|" + gg[t+J+1:t+J+K+1].tobytes()
            mid = int(gg[t+J])
            d = classes.get(key)
            if d is None: classes[key] = {mid: t}
            elif mid not in d: d[mid] = t
    n_cls = len(classes)
    multi = [d for d in classes.values() if len(d) >= 2]
    n_exch = len(multi)
    if not quiet:
        print(f"J={J} K={K} D0={D0} b={b} gate(b*(D0-2)<2^(J+1)): {gate_ok}")
        print(f"  controlled sites: {n_sites}, classes: {n_cls}, classes with >=2 distinct middles (exchange): {n_exch}")
    if n_exch:
        d = multi[0]
        mids = sorted(d)[:2]
        t1, t2 = d[mids[0]], d[mids[1]]
        d1 = mids[0]-mids[1]
        lhs = delta[t1+J] - delta[t2+J]
        rhs = d1/2 + 2**-(K+1)*(delta[t1+J+K+1]-delta[t2+J+K+1])
        if not quiet:
            print(f"  example pair: t={t1}, t'={t2} (p_anchor ~ {p[t1+J]}, {p[t2+J]})")
            print(f"    prefix  = {list(gg[t1:t1+J])}")
            print(f"    middles = {mids[0]} vs {mids[1]}  (d1 = {d1})")
            print(f"    suffix  = {list(gg[t1+J+1:t1+J+K+1])}")
            print(f"    delta[t+J]={delta[t1+J]:.4f}, delta[t'+J]={delta[t2+J]:.4f} (<= D0={D0})")
            print(f"    delta[t+J+K+1]={delta[t1+J+K+1]:.4f}, delta[t'+J+K+1]={delta[t2+J+K+1]:.4f} (<= 2^K={twoK})")
            print(f"    identity check: lhs-rhs = {lhs-rhs:.2e} (Lemma 2.2 subtraction)")
            print(f"    |d1| = {abs(d1)} >= 2, while merge would force |d1| = 2^-K|Delta_end| < 1 -> contradiction engine OK")
    return n_sites, n_cls, n_exch

# Markov check: average delta and tail-control density at D = 4 ln x
D_markov = 4*math.log(LIMIT)
frac = np.mean(delta[:VALID] <= D_markov)
print(f"mean delta = {np.mean(delta[:VALID]):.3f} (~ln x?), P(delta <= 4 ln x = {D_markov:.1f}) = {frac:.4f}\n")

# b=1 gates (item-0010 scale), small windows, per-site D0=30 < 2^(J+1)=32
scan(4, 5, 30, b=1)
print()
# blanket Markov-style D = 4 ln x ~ 67: needs J >= 7 for b=1
scan(7, 7, 67, b=1)
print()
# larger b: b=7 needs b*(D0-2) < 2^(J+1): 7*28=196 < 2^8: J=7, D0=30
scan(7, 7, 30, b=7)
print()
# stress: how far can J+K grow before collisions die at this x?
for JK in [(9,9),(11,11),(13,13)]:
    scan(JK[0], JK[1], 67 if 67 < 2**(JK[0]+1) else 30, b=1, quiet=False); print()
