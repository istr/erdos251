import numpy as np, math

def build(limit):
    sieve = np.ones(limit+1, dtype=bool); sieve[:2] = False
    for i in range(2, int(limit**0.5)+1):
        if sieve[i]: sieve[i*i::i] = False
    p = np.nonzero(sieve)[0].astype(np.int64)
    g = np.diff(p); M = len(g)
    delta = np.zeros(M); delta[M-1] = 2.0
    for t in range(M-2, -1, -1): delta[t] = 0.5*(g[t] + delta[t+1])
    return p, g.astype(np.int16), delta, M-200

def scan(g, delta, VALID, J, K, D0, b=1):
    twoK = 2**K; classes = {}; n_sites = 0
    for t in range(0, VALID-(J+K+2)):
        if delta[t+J] <= D0 and delta[t+J+K+1] <= twoK:
            n_sites += 1
            key = g[t:t+J].tobytes()+b"|"+g[t+J+1:t+J+K+1].tobytes()
            mid = int(g[t+J]); d = classes.get(key)
            if d is None: classes[key] = {mid:t}
            elif mid not in d: d[mid] = t
    multi = {k:d for k,d in classes.items() if len(d)>=2}
    # largest min-anchor among exchange classes (shows they keep appearing)
    mx = max((min(d.values()) for d in multi.values()), default=None)
    gate = b*(D0-2) < 2**(J+1)
    return n_sites, len(classes), len(multi), mx, gate

for LIMIT in [2_000_000, 20_000_000, 100_000_000]:
    p, g, delta, VALID = build(LIMIT)
    print(f"x = {LIMIT:.0e}: pi = {len(p)}, 4ln x = {4*math.log(LIMIT):.0f}")
    for (J,K,D0) in [(4,5,30),(5,5,34),(6,6,64),(7,7,67),(8,8,67)]:
        ns, nc, ne, mx, gate = scan(g, delta, VALID, J, K, D0)
        pmx = p[mx+J] if mx is not None else None
        print(f"  (J,K,D0)=({J},{K},{D0}) gate_b1={gate}: sites={ns}, classes={nc}, EXCHANGE={ne}, latest-appearing pair anchor p ~ {pmx}")
    print()
