import numpy as np, math
LIMIT = 100_000_000
sieve = np.ones(LIMIT+1, dtype=bool); sieve[:2] = False
for i in range(2, int(LIMIT**0.5)+1):
    if sieve[i]: sieve[i*i::i] = False
p = np.nonzero(sieve)[0].astype(np.int64)
g = np.diff(p); M = len(g)
delta = np.zeros(M); delta[M-1] = 2.0
for t in range(M-2, -1, -1): delta[t] = 0.5*(g[t] + delta[t+1])
VALID = M-200
gg = g.astype(np.int16)

def certs(J,K,D0,want_latest=False):
    twoK = 2**K; classes = {}
    for t in range(0, VALID-(J+K+2)):
        if delta[t+J] <= D0 and delta[t+J+K+1] <= twoK:
            key = gg[t:t+J].tobytes()+b"|"+gg[t+J+1:t+J+K+1].tobytes()
            mid = int(gg[t+J]); d = classes.get(key)
            if d is None: classes[key] = {mid:t}
            elif mid not in d: d[mid] = t
    multi = [d for d in classes.values() if len(d)>=2]
    if not multi: print("none"); return
    # pick pair with largest min site index if requested, else first
    pick = max(multi, key=lambda d: min(d.values())) if want_latest else multi[0]
    mids = sorted(pick)[:2]; t1,t2 = pick[mids[0]], pick[mids[1]]
    print(f"CERTIFICATE (J={J},K={K},D0={D0}, b=1 gate {D0-2}<{2**(J+1)}):")
    for lab,t in (("site n",t1),("site m",t2)):
        print(f"  {lab}: gap-seq index t={t}, primes p[t..t+{J+K+2}]:")
        print(f"    {list(p[t:t+J+K+3])}")
        print(f"    word: prefix {list(gg[t:t+J])} | middle {int(gg[t+J])} | suffix {list(gg[t+J+1:t+J+K+1])}")
        print(f"    delta[t+J]={delta[t+J]:.6f} (<= {D0}), delta[t+J+K+1]={delta[t+J+K+1]:.6f} (<= {twoK})")
    d1 = mids[0]-mids[1]
    lhs = delta[t1+J]-delta[t2+J]; rhs = d1/2 + 2**-(K+1)*(delta[t1+J+K+1]-delta[t2+J+K+1])
    print(f"  d1 = {d1}; identity residual = {lhs-rhs:.2e}; would-be forced |d1|<1 vs actual |d1|={abs(d1)}")
    print()

certs(6,6,64)
certs(5,5,34,want_latest=True)
