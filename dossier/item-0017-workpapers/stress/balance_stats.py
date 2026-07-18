# item-0017 D5.c -- the D1 balance statistics, measured (rule-12 landing).
# On S_x(A,D) (dossier/e2prime-supply.md D0.2, M = 1) compute per (J,K,D0,A):
#   |S_x|, |W_L|, |P|, C_words, C_sides, C_sides - C_words (P1 pair count),
#   exchange class count (sides with >= 2 distinct middles),
#   empirical singular-series site statistics (D1.c: mean/2nd moment of
#   S(H_w) over sampled sites), and the D1.a per-word comparison
#   lambda_w = N_w (ln x)^{L+1} / (S(H_w) x) on the sampled words.
# Index conventions of the seed scripts (item-0005-workpapers/stress):
#   g[t] = paper g_{t+1}, delta[t] = paper delta_t; site t = paper n = t;
#   prefix g[t..t+J-1], middle g[t+J], suffix g[t+J+1..t+J+K];
#   near cap delta[t+J] <= D0, far cap delta[t+J+K+1] <= 2^K.
# Sites start at t = 1 (paper n >= 1, D0 fidelity); last 200 discarded
# (delta seed influence <= maxgap * 2^-200).
import numpy as np, math, sys

SAMPLE_TARGET = 20000  # sites sampled for singular-series statistics
PCUT = 1_000_000       # tail cutoff for singular series (error ~ k^2/(PCUT ln PCUT))

def build(limit):
    sieve = np.ones(limit + 1, dtype=bool); sieve[:2] = False
    for i in range(2, int(limit**0.5) + 1):
        if sieve[i]: sieve[i * i::i] = False
    p = np.nonzero(sieve)[0].astype(np.int64)
    g = np.diff(p); M = len(g)
    delta = np.zeros(M); delta[M - 1] = 2.0
    for t in range(M - 2, -1, -1): delta[t] = 0.5 * (g[t] + delta[t + 1])
    return p, g.astype(np.int32), delta, M - 200

def small_primes(n):
    s = np.ones(n + 1, dtype=bool); s[:2] = False
    for i in range(2, int(n**0.5) + 1):
        if s[i]: s[i * i::i] = False
    return np.nonzero(s)[0].astype(np.int64)

SP = small_primes(PCUT)
LOG1M = np.log1p(-1.0 / SP)  # ln(1 - 1/p), aligned with SP

def tail_suffix(k):
    # SUFF[i] = sum_{j >= i} [ ln(1 - k/SP[j]) - k ln(1 - 1/SP[j]) ],
    # valid at indices with SP[i] > k (only such i are ever queried:
    # the query span is >= 2L > k = L+1 for L >= 2). Entries at
    # SP <= k are masked to 0 and never enter a queried suffix.
    safe = SP > k
    arr = np.where(safe, np.log1p(np.where(safe, -k / SP, 0.0)) - k * LOG1M, 0.0)
    return np.concatenate((np.cumsum(arr[::-1])[::-1], [0.0]))

def sing_series(word, suff, k):
    # H = {0, c_1, ..., c_L} cumulative sums; k = L+1 points
    H = np.concatenate(([0], np.cumsum(word))).astype(np.int64)
    span = int(H[-1])
    lg = 0.0
    i0 = int(np.searchsorted(SP, span, side='right'))
    for q in SP[:i0]:
        nu = len(np.unique(H % q))
        if nu == q: return 0.0  # inadmissible
        lg += math.log1p(-nu / q) - k * math.log1p(-1.0 / q)
    lg += float(suff[i0])
    return math.exp(lg)

def uniq_counts(mat):
    # row-wise unique with counts via void view (pc_wordcount2 convention)
    v = np.ascontiguousarray(mat).view([('', mat.dtype)] * mat.shape[1])
    _, inv, cnt = np.unique(v, return_inverse=True, return_counts=True)
    return inv.ravel(), cnt

def stats(p, g, delta, VALID, lnx, x, J, K, D0, A, sample=True):
    L = J + 1 + K; twoK = float(2 ** K)
    tmax = VALID - (J + K + 2)
    t = np.arange(1, tmax)
    ok = (delta[t + J] <= D0) & (delta[t + J + K + 1] <= twoK)
    if A is not None:
        cap = A * lnx
        bad = (g[: tmax + L] > cap).astype(np.int32)
        Pb = np.concatenate(([0], np.cumsum(bad)))
        ok &= (Pb[t + L] - Pb[t]) == 0  # all L window gaps <= A ln x
    sites = t[ok]; ns = len(sites)
    if ns == 0:
        print(f"  (J,K,D0,A)=({J},{K},{D0},{A}): 0 sites"); return
    # window matrices
    W = np.empty((ns, L), dtype=np.int32)
    for j in range(L): W[:, j] = g[sites + j]
    sideidx = list(range(J)) + list(range(J + 1, L))
    Sm = W[:, sideidx]
    inv_w, cnt_w = uniq_counts(W)
    inv_s, cnt_s = uniq_counts(Sm)
    C_words = int(np.sum(cnt_w.astype(np.int64) ** 2))
    C_sides = int(np.sum(cnt_s.astype(np.int64) ** 2))
    nW = len(cnt_w); nP = len(cnt_s)
    # exchange classes: sides carrying >= 2 distinct (side,middle) words
    # map each distinct word -> its side class: take first occurrence rows
    first_rows = np.zeros(nW, dtype=np.int64)
    first_rows[inv_w[::-1]] = np.arange(ns)[::-1]  # first occurrence index
    wside = inv_s[first_rows]                      # side-class per distinct word
    cls_counts = np.bincount(wside, minlength=nP)  # distinct middles per side class
    n_exch_classes = int(np.sum(cls_counts >= 2))
    pairs = C_sides - C_words  # P1: ordered pi-matched differing-middle pairs
    print(f"  (J,K,D0,A)=({J},{K},{D0},{A}) L={L}: sites={ns}, |W_L|={nW}, |P|={nP}")
    print(f"    C_words={C_words}, C_sides={C_sides}, P1 pairs (C_s-C_w)={pairs}, exch classes={n_exch_classes}")
    print(f"    balance floors: |S|^2/|P|={ns * ns / nP:.3e} vs C_words={C_words:.3e} "
          f"(Cauchy-Schwarz slack C_sides/(|S|^2/|P|)={C_sides * nP / (ns * ns):.3f})")
    # model calibration: (2 ln x)^(J+K) side-collision prediction (D2/M2)
    pred = ns * ns * (2 * lnx) ** (-(J + K))
    print(f"    model M pred off-diag C_sides ~ |S|^2 (2 ln x)^-(J+K) = {pred:.3e} "
          f"(actual off-diag {C_sides - ns})")
    if not sample: return
    # singular-series site statistics (D1.c) + per-word lambda (D1.a) on a site sample
    step = max(1, ns // SAMPLE_TARGET)
    sub = np.arange(0, ns, step)
    suff = tail_suffix(L + 1)
    Svals = np.array([sing_series(W[i], suff, L + 1) for i in sub])
    nz = Svals > 0
    lam = None
    m1, m2 = float(np.mean(Svals)), float(np.mean(Svals ** 2))
    # lambda_w = N_w (ln x)^{L+1} / (S(H_w) x) for the sampled sites' words
    Nw_of_site = cnt_w[inv_w[sub]]
    with np.errstate(divide='ignore'):
        lam = np.where(nz, Nw_of_site * lnx ** (L + 1) / (np.maximum(Svals, 1e-300) * x), np.inf)
    lamf = lam[nz]
    print(f"    S-site sample (n={len(sub)}, step={step}): mean S={m1:.4f}, mean S^2={m2:.4f}, "
          f"S2nd/S1st^2={m2 / m1 / m1 if m1 > 0 else float('nan'):.3f}, inadmissible frac={float(np.mean(~nz)):.4f}")
    print(f"    lambda_w = N_w (ln x)^(L+1)/(S x): mean={float(np.mean(lamf)):.3e}, "
          f"median={float(np.median(lamf)):.3e}, max={float(np.max(lamf)):.3e}")

if __name__ == '__main__':
    LIMIT = int(float(sys.argv[1])) if len(sys.argv) > 1 else 100_000_000
    p, g, delta, VALID = build(LIMIT)
    lnx = math.log(LIMIT)
    print(f"x = {LIMIT:.0e}: pi = {len(p)}, ln x = {lnx:.3f}, 4 ln x = {4 * lnx:.1f}")
    grid = [(4, 5, 30), (5, 5, 34), (6, 6, 64), (7, 7, 67), (8, 8, 67)]
    for (J, K, D0) in grid:
        for A in (None, 8, 4):
            stats(p, g, delta, VALID, lnx, LIMIT, J, K, D0, A,
                  sample=(A is None))
        print()
