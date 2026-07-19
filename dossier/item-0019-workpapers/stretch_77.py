# item-0019 3(h) STRETCH -- (7,7) first-pair hunt at 5e9-1e10
# (kickoff v1 3(h) as amended by v1.1 delta D4).
#
# D0.2-style filter (delta caps only, seed A = None world) at
# (J,K,D) = (7,7,67): continuity with the committed 1e9 null row.
# STAGES (D4): full passes at x = 5e9 and x = 1e10; the join scope is
# GLOBAL per stage (the full prefix 0..x is sorted/grouped, never only
# the increment), so an old-site/new-site first pair cannot be missed.
#
# KEY PACKING (D4): all window gaps in the scanned range are even and
# < 512 -- GUARDED by an assert, not assumed -- so the 14 side
# half-gaps pack as uint8 into 16 bytes (2 zero pad) = 2 x uint64 per
# side word.  Sort by (packed side key, site index) via np.lexsort;
# byte-identical output for every worker count (v1.1 delta D2: the
# only parallel stage is the delta recursion, whose chunks are fixed
# functions of M).
#
# Certificates print in the d5b_deep.py exch_cert format (primes,
# word, deltas, both (E4) caps, (E5) gate, d_1, identity residual) and
# are re-verified gap-by-gap from the printed primes.  A null result
# is the datum: reached x and site count are reported.
#
# In-core budget (v1.1 delta D1): conservative peak ~35 GB at 1e10.

import numpy as np, math, os, sys, time
import common as C

J = K = 7
D0 = 67
L = J + 1 + K


def build_big(x):
    """Sieve + gaps + chunk-parallel delta at stretch scale (no disk
    cache: regenerable, RAM is the budget here)."""
    t0 = time.time()
    s = C.sieve_primes(x)
    p = np.nonzero(s)[0].astype(np.int64)
    del s
    g64 = np.diff(p)
    assert int(g64.max()) < 512, "gap packing guard (D4)"
    g = g64.astype(np.int16)
    del g64
    # evenness guard over the scanned range (t >= 1)
    assert not (np.asarray(g[1:]) & 1).any(), "even-gap guard (D4)"
    delta = C.delta_parallel(g)
    print(f"x = {x:.0e}: pi = {len(p)}, build {time.time()-t0:.0f}s",
          flush=True)
    return p, g, delta, len(g) - 200


def certificate(p, g, delta, t1, t2, out):
    """d5b_deep-format certificate + gap-by-gap re-verification from
    the printed primes."""
    twoK = float(2 ** K)
    u1, u2 = int(g[t1 + J]), int(g[t2 + J])
    d1 = u1 - u2
    lhs = delta[t1 + J] - delta[t2 + J]
    rhs = d1 / 2 + 2.0 ** -(K + 1) * (delta[t1 + J + K + 1]
                                      - delta[t2 + J + K + 1])
    out.append(f"  CERT (b=1 gate {D0 - 2}<{2 ** (J + 1)}):")
    for lab, tt in (("site n", t1), ("site m", t2)):
        primes = [int(v) for v in p[tt:tt + J + K + 3]]
        word_p = [int(v) for v in g[tt:tt + J]]
        word_m = int(g[tt + J])
        word_s = [int(v) for v in g[tt + J + 1:tt + J + K + 1]]
        out.append(f"    {lab}: t={tt}, primes {primes}")
        out.append(f"      word: {word_p} | {word_m} | {word_s}")
        out.append(f"      delta[t+J]={delta[tt + J]:.6f} (<= {D0}), "
                   f"delta[t+J+K+1]={delta[tt + J + K + 1]:.6f} "
                   f"(<= {twoK:.0f})")
        # re-verify gap-by-gap from the printed primes
        gg = [primes[i + 1] - primes[i] for i in range(len(primes) - 1)]
        assert gg[:J] == word_p and gg[J] == word_m \
            and gg[J + 1:J + 1 + K] == word_s, "certificate reverify"
        for q in primes:
            assert q >= 2 and all(q % r for r in
                                  range(2, math.isqrt(q) + 1)), \
                f"primality reverify {q}"
    out.append(f"    d1 = {d1}; identity residual = {lhs - rhs:.2e}")
    out.append("    gap-by-gap + primality re-verification: PASS")


def stage(x, outlines):
    p, g, delta, VALID = build_big(x)
    t0 = time.time()
    t = C.site_range(VALID, J, K)
    ok = C.filter_d02(delta, t, J, K, D0)
    sites = t[ok]
    del t, ok
    ns = len(sites)
    # pack 14 side half-gaps into 2 x uint64 (16 bytes, 2 zero pad)
    W8 = np.zeros((ns, 16), dtype=np.uint8)
    for jj, col in enumerate(list(range(J)) + list(range(J + 1, L))):
        W8[:, jj] = (g[sites + col].astype(np.int16) // 2).astype(
            np.uint8)
    keys = W8.view(np.uint64).reshape(ns, 2)
    del W8
    order = np.lexsort((sites, keys[:, 1], keys[:, 0]))
    k0 = keys[order, 0]
    k1 = keys[order, 1]
    ssites = sites[order]
    del keys, order, sites
    new = np.empty(ns, dtype=bool)
    new[0] = True
    new[1:] = (k0[1:] != k0[:-1]) | (k1[1:] != k1[:-1])
    starts = np.nonzero(new)[0]
    ends = np.append(starts[1:], ns)
    sizes = ends - starts
    outlines.append(f"x = {x:.0e}: pi = {len(p)}, "
                    f"(7,7,67) D0.2-style sites = {ns}, "
                    f"side classes = {len(starts)}, "
                    f"max class size = {int(sizes.max())}")
    n_exch = 0
    for s0, e0 in zip(starts[sizes >= 2], ends[sizes >= 2]):
        mm = g[ssites[s0:e0] + J]
        if np.all(mm == mm[0]):
            continue
        n_exch += 1
        uu = np.unique(mm)[:2]
        t1 = int(ssites[s0:e0][mm == uu[0]][0])
        t2 = int(ssites[s0:e0][mm == uu[1]][0])
        certificate(p, g, delta, t1, t2, outlines)
    outlines.append(f"x = {x:.0e}: EXCHANGE classes "
                    f"(>= 2 distinct middles): {n_exch}"
                    + ("  [FIRST (7,7) PAIR(S) FOUND]" if n_exch
                       else "  [null result -- the datum]"))
    outlines.append(f"  repeated-side classes (any middles): "
                    f"{int((sizes >= 2).sum())}; stage wall "
                    f"{time.time() - t0:.0f}s")
    del p, g, delta, k0, k1, ssites
    return n_exch


def main():
    outlines = ["item-0019 3(h) stretch: (7,7,67) first-pair hunt",
                "(D0.2-style filter; stages per v1.1 delta D4;",
                "global join per stage; certificates re-verified",
                "gap-by-gap from printed primes).", ""]
    printed = 0
    for x in (5_000_000_000, 10_000_000_000):
        stage(x, outlines)
        outlines.append("")
        for ln in outlines[printed:]:
            print(ln, flush=True)
        printed = len(outlines)
    with open(os.path.join(C.CACHE, "stretch.txt"), "w") as f:
        f.write("\n".join(outlines) + "\n")


if __name__ == '__main__':
    main()
