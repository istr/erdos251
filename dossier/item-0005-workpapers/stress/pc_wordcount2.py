import numpy as np, math
# Fast: distinct length-L gap words realized among ALL start sites, via np.unique
# on the (N-L, L) window matrix viewed as void rows. Question: is realized-word
# entropy linear in L (=> typical-gap capacity ~ log x/loglog x) or quadratic
# (=> product-bound worst-case capacity ~ sqrt(log x))?
for LIMIT in [20_000_000, 100_000_000]:
    sieve = np.ones(LIMIT+1, dtype=bool); sieve[:2] = False
    for i in range(2, int(LIMIT**0.5)+1):
        if sieve[i]: sieve[i*i::i] = False
    p = np.nonzero(sieve)[0].astype(np.int64)
    g = np.diff(p).astype(np.int32); M = len(g)
    VALID = M-200
    lnx = math.log(LIMIT)
    print(f"\nx={LIMIT:.0e}: pi={len(p)} lnx={lnx:.2f} log2(N)={math.log2(VALID):.2f} "
          f"sqrt(2log2N)={math.sqrt(2*math.log2(VALID)):.2f} (log x/loglog x)={lnx/math.log(lnx):.2f}")
    print(f"{'L':>3} {'#distinct':>12} {'log2':>7} {'bits/pos':>9}  <- constant bits/pos => linear entropy => log x/loglog x capacity")
    base = g[:VALID]
    prev_b = None
    for L in range(2, 17):
        # build (VALID-L, L) window matrix
        n = VALID - L
        W = np.empty((n, L), dtype=np.int32)
        for j in range(L):
            W[:, j] = base[j:j+n]
        Wv = np.ascontiguousarray(W).view([('', np.int32)]*L)
        ndist = len(np.unique(Wv))
        b = math.log2(ndist)
        marg = "" if prev_b is None else f"  d(log2)/dL={b-prev_b:.2f}"
        print(f"{L:>3} {ndist:>12} {b:>7.2f} {b/L:>9.3f}{marg}")
        prev_b = b
        if ndist == n:  # saturated: every window distinct, no more collisions
            print(f"     [saturated at L={L}: all {n} windows distinct -> collisions cease]")
            break
