# item-0017 D5.b -- deeper firsts and b > 1 certificates at x = 1e9.
# Seed-script conventions (g[t] = paper g_{t+1}, delta[t] = paper delta_t;
# site t: prefix g[t..t+J-1], middle g[t+J], suffix g[t+J+1..t+J+K];
# caps delta[t+J] <= D0, delta[t+J+K+1] <= 2^K). Gates checked per row:
# b(D0-2) < 2^{J+1}. Container probe (rule 9) done in-session: 88 GB free;
# in-core at 1e9 is ~6 GB peak. First-pair certificates printed in the
# exch_cert.py format (primes, word, deltas, d1, identity residual).
import numpy as np, math, sys

LIMIT = int(float(sys.argv[1])) if len(sys.argv) > 1 else 1_000_000_000

sieve = np.ones(LIMIT + 1, dtype=bool); sieve[:2] = False
for i in range(2, int(LIMIT**0.5) + 1):
    if sieve[i]: sieve[i * i::i] = False
p = np.nonzero(sieve)[0].astype(np.int64)
del sieve
g64 = np.diff(p); M = len(g64)
g = g64.astype(np.int16); del g64
print(f"x = {LIMIT:.0e}: pi = {len(p)}, ln x = {math.log(LIMIT):.3f}", flush=True)

delta = np.zeros(M, dtype=np.float64); delta[M - 1] = 2.0
for t in range(M - 2, -1, -1):
    delta[t] = 0.5 * (g[t] + delta[t + 1])
VALID = M - 200

def scan(J, K, D0, b, want_pairs=2):
    twoK = float(2 ** K)
    gate = b * (D0 - 2) < 2 ** (J + 1)
    t = np.arange(1, VALID - (J + K + 2))
    ok = (delta[t + J] <= D0) & (delta[t + J + K + 1] <= twoK)
    sites = t[ok]; ns = len(sites)
    W = np.empty((ns, J + K + 1), dtype=np.int16)
    for j in range(J + K + 1): W[:, j] = g[sites + j]
    sideidx = list(range(J)) + list(range(J + 1, J + K + 1))
    Sm = np.ascontiguousarray(W[:, sideidx])
    v = Sm.view([('', np.int16)] * Sm.shape[1])
    order = np.argsort(v.ravel(), kind='stable')
    vs = v.ravel()[order]
    newgrp = np.empty(ns, dtype=bool); newgrp[0] = True
    newgrp[1:] = vs[1:] != vs[:-1]
    grp = np.cumsum(newgrp) - 1
    mids = W[:, J][order]
    # exchange classes: same side group, differing middles
    n_exch = 0; shown = 0
    print(f"(J,K,D0,b)=({J},{K},{D0},{b}) gate={gate}: sites={ns}, side classes={int(grp[-1]) + 1}", flush=True)
    i = 0
    starts = np.nonzero(newgrp)[0]
    ends = np.append(starts[1:], ns)
    for s0, e0 in zip(starts, ends):
        if e0 - s0 < 2: continue
        mm = mids[s0:e0]
        if np.all(mm == mm[0]): continue
        n_exch += 1
        if shown < want_pairs:
            shown += 1
            u = np.unique(mm)[:2]
            t1 = sites[order[s0:e0][mm == u[0]][0]]
            t2 = sites[order[s0:e0][mm == u[1]][0]]
            d1 = int(u[0]) - int(u[1])
            lhs = delta[t1 + J] - delta[t2 + J]
            rhs = d1 / 2 + 2.0**-(K + 1) * (delta[t1 + J + K + 1] - delta[t2 + J + K + 1])
            print(f"  CERT (b={b} gate {b*(D0-2)}<{2**(J+1)}):")
            for lab, tt in (("site n", t1), ("site m", t2)):
                print(f"    {lab}: t={tt}, primes {list(p[tt:tt + J + K + 3])}")
                print(f"      word: {list(g[tt:tt + J])} | {int(g[tt + J])} | {list(g[tt + J + 1:tt + J + K + 1])}")
                print(f"      delta[t+J]={delta[tt + J]:.6f} (<= {D0}), delta[t+J+K+1]={delta[tt + J + K + 1]:.6f} (<= {twoK:.0f})")
            print(f"    d1 = {d1}; identity residual = {lhs - rhs:.2e}", flush=True)
    print(f"  EXCHANGE classes: {n_exch}", flush=True)

# deeper firsts (b = 1): does (7,7) or (8,8) first-appear by 1e9?
scan(7, 7, 67, 1)
scan(8, 8, 67, 1)
# b > 1 certificates honoring (E5) b(D0-2) < 2^{J+1}
scan(7, 6, 44, 3)   # 3*42 = 126 < 256
scan(7, 6, 27, 5)   # 5*25 = 125 < 256
scan(6, 6, 64, 1)   # continuity row vs 1e8 (classes should grow past 1)
