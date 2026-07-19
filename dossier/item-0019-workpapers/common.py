# item-0019 -- shared build + filter + class machinery.
#
# Seed-script conventions (dossier/item-0017-workpapers/stress, ANN-50 /
# v1.1 T6 dictionary, identical content): g[t] = paper g_{t+1} = Lean
# gap t; delta[t] = paper delta_t (no shift); site t = paper n = t;
# prefix g[t..t+J-1], middle g[t+J], suffix g[t+J+1..t+J+K]; near cap
# delta[t+J] <= D, far cap delta[t+J+K+1] <= 2^K; window sum
# g[t..t+L-1], L = J+1+K, capped at W = A' L ln x (D0.2', A' = 1.5).
# COMPARISON CONVENTION (stated once, kickoff 3(a)): the window sum is
# int64; the cap W is float64; the comparison is numpy int64 <= float64
# (int64 promoted to float64, IEEE round-to-nearest).  The delta caps
# compare float64 delta against the integer caps D and 2^K.
#
# delta uses the seed recurrence (d5b_deep.py): delta[M-1] = 2.0;
# delta[t] = 0.5*(g[t] + delta[t+1]) -- chunk-parallel per kickoff
# v1.1 delta D3: fixed chunks (functions of M only, never of worker
# count), each chunk computed by the UNCHANGED backward recursion over
# chunk + 200-gap right halo seeded 2.0; halo part dropped.  One-sided
# halo error <= maxgap * 2^-200; smoke check vs serial on the 1e8
# prefix is printed by census.py once.
#
# Site clauses (i) 1 <= n, anchorPrime p_n <= x and (ii) s+1 <= n with
# s = 0 are automatic on the array carrier (every sieved prime is <= x
# and t >= 1); noted once in the report, no s grid (s-invariance up to
# O(1) sites).
#
# Class machinery (kickoff v1.1 delta D2): sites are partitioned into
# NBUCKETS = 64 fixed buckets by a deterministic hash of the side gap
# word (a function of the data only, never of the worker count); each
# bucket is processed independently (one lexsort by (side word, middle,
# site index) -- numeric lexicographic order); merges run in bucket
# index order.  Committed outputs are therefore byte-identical for
# every worker count, including serial.

import numpy as np, math, os
from multiprocessing import Pool

CACHE = os.environ.get(
    "ITEM0019_CACHE",
    "/tmp/claude-1000/-home-istr-pro-erdos251/"
    "0ffe0bc5-11b7-44de-aa72-699e70dbfbf9/scratchpad/cache")

APRIME = 1.5      # D0.2' aggregate window constant A' (D0 pin)
WORKERS = 8       # kickoff v1.1 delta D2 default
NBUCKETS = 64     # fixed partition count (function of nothing)
DELTA_CHUNK = 4_000_000   # fixed delta chunk length (function of M only)
DELTA_HALO = 200          # seed-script discard depth = halo length

# fixed tail-delta histogram bin edges (delta_{n+L}); the last bin is
# the overflow
TAIL_EDGES = np.array([float(v) for v in range(0, 65, 2)]
                      + [96.0, 128.0, 192.0, 256.0, 1e18])

GRID = [(4, 5, 30), (5, 5, 34), (6, 6, 64), (7, 6, 44), (7, 7, 67)]
XLADDER = [2_000_000, 20_000_000, 100_000_000, 1_000_000_000]


def sieve_primes(limit):
    s = np.ones(limit + 1, dtype=bool)
    s[:2] = False
    for i in range(2, int(limit ** 0.5) + 1):
        if s[i]:
            s[i * i::i] = False
    return s


def _delta_serial(gl, M):
    dl = [0.0] * M
    dl[M - 1] = 2.0
    for t in range(M - 2, -1, -1):
        dl[t] = 0.5 * (gl[t] + dl[t + 1])
    return dl


_G_FOR_DELTA = None  # fork-inherited read-only global


def _delta_chunk(args):
    lo, hi, M = args
    g = _G_FOR_DELTA
    end = min(hi + DELTA_HALO, M)
    gl = g[lo:end].tolist()
    m = len(gl)
    dl = [0.0] * m
    dl[m - 1] = 2.0
    for t in range(m - 2, -1, -1):
        dl[t] = 0.5 * (gl[t] + dl[t + 1])
    return lo, dl[:hi - lo]


def delta_parallel(g, workers=WORKERS):
    """Chunk-parallel seed recurrence (v1.1 delta D3).  Chunk
    boundaries depend on M and DELTA_CHUNK only.  The last chunk holds
    the true seed at M-1; every other chunk is seeded 2.0 at the end
    of its 200-gap right halo, exactly as the serial code seeds at
    M-1."""
    global _G_FOR_DELTA
    M = len(g)
    chunks = [(lo, min(lo + DELTA_CHUNK, M), M)
              for lo in range(0, M, DELTA_CHUNK)]
    delta = np.empty(M, dtype=np.float64)
    if len(chunks) == 1 or workers <= 1:
        delta[:] = _delta_serial(g.tolist(), M)
        return delta
    _G_FOR_DELTA = g
    with Pool(min(workers, len(chunks))) as pool:
        for lo, part in pool.imap_unordered(_delta_chunk, chunks):
            delta[lo:lo + len(part)] = part
    _G_FOR_DELTA = None
    return delta


def build(x, workers=WORKERS):
    """p (int64), g (int16), delta (float64), VALID for primes <= x.
    Cached in CACHE (raw intermediates, uncommitted, regenerable)."""
    os.makedirs(CACHE, exist_ok=True)
    fp = os.path.join(CACHE, f"p_{x}.npy")
    fg = os.path.join(CACHE, f"g_{x}.npy")
    fd = os.path.join(CACHE, f"delta_{x}.npy")
    if os.path.exists(fd):
        return (np.load(fp), np.load(fg), np.load(fd),
                len(np.load(fg)) - 200)
    p = np.nonzero(sieve_primes(x))[0].astype(np.int64)
    g64 = np.diff(p)
    assert int(g64.max()) < 32000
    g = g64.astype(np.int16)
    del g64
    delta = delta_parallel(g, workers)
    np.save(fp, p); np.save(fg, g); np.save(fd, delta)
    return p, g, delta, len(g) - 200


def site_range(VALID, J, K):
    """t = 1 .. VALID-(J+K+2)-1 inclusive (seed-script range)."""
    return np.arange(1, VALID - (J + K + 2), dtype=np.int64)


def window_sums(g, t, L):
    cs = np.concatenate(([0], np.cumsum(g, dtype=np.int64)))
    return cs[t + L] - cs[t]


def filter_d02(delta, t, J, K, D):
    """D0.2-style (seed A = None world): the two delta caps only."""
    return (delta[t + J] <= D) & (delta[t + J + K + 1] <= float(2 ** K))


def filter_d02p(g, delta, t, J, K, D, lnx):
    """D0.2' (campaign baseline): window-sum cap + both delta caps."""
    L = J + 1 + K
    W = APRIME * L * lnx
    return filter_d02(delta, t, J, K, D) & (window_sums(g, t, L) <= W)


def filter_nw(g, t, J, K, lnx):
    """N^w world (RS.4): window-sum cap ONLY, both delta caps dropped."""
    L = J + 1 + K
    W = APRIME * L * lnx
    return window_sums(g, t, L) <= W


# ---------------------------------------------------------------- #
# Bucketed class machinery (v1.1 delta D2)

_CTX = {}  # fork-inherited read-only context for bucket workers


def _side_hash(g, sites, J, K):
    """Deterministic bucket id per site from the side gap word only
    (prefix g[t..t+J-1], suffix g[t+J+1..t+J+K]).  A function of the
    data and fixed constants; identical side words always share a
    bucket."""
    h = np.zeros(len(sites), dtype=np.uint64)
    for j in list(range(J)) + list(range(J + 1, J + 1 + K)):
        h = h * np.uint64(1000003) + g[sites + j].astype(np.uint64)
    return (h % np.uint64(NBUCKETS)).astype(np.int64)


def _bucket_worker(b):
    """Process one bucket: group by side word, collect class records.

    Context (fork-inherited): g, delta, J, K, sp_sites (S' world),
    nw_sites (N^w world or None), nw_capn, nw_capf (per-N^w-site cap
    failure flags), sp_bucket, nw_bucket (bucket id per site), and
    want_fam2 / tail_idx flags.
    """
    C = _CTX
    g, delta, J, K = C['g'], C['delta'], C['J'], C['K']
    L = J + 1 + K
    side_cols = list(range(J)) + list(range(J + 1, L))

    def group(sites):
        """lexsort sites of this bucket by (side word, middle, site);
        return sorted sites, side matrix, mids, side-run starts,
        word-run starts."""
        ns = len(sites)
        W = np.empty((ns, L), dtype=np.int16)
        for j in range(L):
            W[:, j] = g[sites + j]
        S = W[:, side_cols]
        mid = W[:, J].astype(np.int64)
        keys = (sites, mid) + tuple(S[:, j] for j in
                                    reversed(range(J + K)))
        order = np.lexsort(keys)
        S = S[order]; mid = mid[order]; ssites = sites[order]
        news = np.empty(ns, dtype=bool)
        news[0] = True
        news[1:] = np.any(S[1:] != S[:-1], axis=1)
        neww = news.copy()
        neww[1:] |= (mid[1:] != mid[:-1])
        return ssites, S, mid, news, neww

    out = {}
    sp = C['sp_sites'][C['sp_bucket'] == b]
    ns = len(sp)
    out['ns'] = ns
    if ns == 0:
        return b, out
    ssites, S, mid, news, neww = group(sp)
    cls_start = np.nonzero(news)[0]
    cls_end = np.append(cls_start[1:], ns)
    NP = (cls_end - cls_start).astype(np.int64)
    wrd_start = np.nonzero(neww)[0]
    wrd_end = np.append(wrd_start[1:], ns)
    NW = (wrd_end - wrd_start).astype(np.int64)
    out['C_words'] = int(np.sum(NW ** 2))
    out['C_sides'] = int(np.sum(NP ** 2))
    out['n_words'] = len(NW)
    out['n_sides'] = len(NP)
    # distinct middles / max N_{P,d} per side class
    wrd_of_cls = np.searchsorted(cls_start, wrd_start, side='right') - 1
    nmid = np.bincount(wrd_of_cls, minlength=len(NP))
    out['n_exch'] = int(np.sum(nmid >= 2))
    out['NP_hist'] = np.bincount(NP)
    maxNPd = np.zeros(len(NP), dtype=np.int64)
    np.maximum.at(maxNPd, wrd_of_cls, NW)
    out['sum_NP'] = int(NP.sum())
    if not C.get('want_fam2'):
        return b, out
    # Fam_2 records (N_P >= 2), in bucket-local side-lex order
    f2 = np.nonzero(NP >= 2)[0]
    tail = delta[ssites + L]
    tail_sum = np.add.reduceat(tail, cls_start) if ns else np.array([])
    near = delta[ssites + J]
    near_sum = np.add.reduceat(near, cls_start)
    rec = dict(
        sides=S[cls_start[f2]].astype(np.int16),
        NP=NP[f2],
        maxNPd=maxNPd[f2],
        nmid=nmid[f2].astype(np.int64),
        tail_sum=tail_sum[f2],
        near_sum=near_sum[f2],
        first_site=ssites[cls_start[f2]],
    )
    # realized (d, N_{P,d}) per Fam_2 class, flattened
    f2set = np.zeros(len(NP), dtype=bool)
    f2set[f2] = True
    wsel = f2set[wrd_of_cls]
    # map class index -> dense Fam_2 index
    dense = -np.ones(len(NP), dtype=np.int64)
    dense[f2] = np.arange(len(f2))
    rec['mid_cls'] = dense[wrd_of_cls[wsel]]
    rec['mid_val'] = mid[wrd_start[wsel]]
    rec['mid_cnt'] = NW[wsel]
    out['fam2'] = rec
    # aggregate m2/m4 accumulators over Fam_2
    out['f2_n'] = len(f2)
    out['f2_mass'] = int(NP[f2].sum())
    out['f2_red_num'] = int((maxNPd[f2] - 1).sum())
    out['f2_max_num'] = int(maxNPd[f2].sum())
    out['f2_tail_sum'] = float(tail_sum[f2].sum())
    out['all_tail_sum'] = float(tail.sum())
    # Fam_2-conditional tail histogram over S'-world class sites
    cls_of_site = np.searchsorted(cls_start,
                                  np.arange(ns), side='right') - 1
    f2site = f2set[cls_of_site]
    out['sp_f2_tail_hist'] = np.histogram(tail[f2site],
                                          bins=TAIL_EDGES)[0]
    # N^w world join (window-cap-only counts for the same side pairs)
    if C.get('nw_sites') is not None:
        nw = C['nw_sites'][C['nw_bucket'] == b]
        if len(nw):
            wsites, wS, wmid, wnews, _ = group(nw)
            wstart = np.nonzero(wnews)[0]
            wNP = np.diff(np.append(wstart, len(nw))).astype(np.int64)
            capn = (delta[wsites + J] > C['D']).astype(np.int64)
            capf = (delta[wsites + L] >
                    float(2 ** K)).astype(np.int64)
            capn_sum = np.add.reduceat(capn, wstart)
            capf_sum = np.add.reduceat(capf, wstart)
            wtail = delta[wsites + L]
            wtail_sum = np.add.reduceat(wtail, wstart)
            # match Fam_2 side words against N^w side classes
            key = {}
            sb = rec['sides'].tobytes()
            row = 2 * (J + K)  # bytes per side row (int16)
            for i in range(len(f2)):
                key[sb[i * row:(i + 1) * row]] = i
            nwNP = np.zeros(len(f2), dtype=np.int64)
            nwcapn = np.zeros(len(f2), dtype=np.int64)
            nwcapf = np.zeros(len(f2), dtype=np.int64)
            nwtail = np.zeros(len(f2), dtype=np.float64)
            match = -np.ones(len(wstart), dtype=np.int64)
            wsb = np.ascontiguousarray(wS[wstart]).tobytes()
            for i in range(len(wstart)):
                j = key.get(wsb[i * row:(i + 1) * row])
                if j is not None:
                    match[i] = j
                    nwNP[j] = wNP[i]
                    nwcapn[j] = capn_sum[i]
                    nwcapf[j] = capf_sum[i]
                    nwtail[j] = wtail_sum[i]
            rec['nw_NP'] = nwNP
            rec['nw_capn'] = nwcapn
            rec['nw_capf'] = nwcapf
            rec['nw_tail_sum'] = nwtail
            # N^w-world Fam_2-conditional tail histogram
            wcls_of_site = np.searchsorted(
                wstart, np.arange(len(nw)), side='right') - 1
            wf2site = match[wcls_of_site] >= 0
            out['nw_f2_tail_hist'] = np.histogram(
                wtail[wf2site], bins=TAIL_EDGES)[0]
        else:
            for k in ('nw_NP', 'nw_capn', 'nw_capf', 'nw_tail_sum'):
                rec[k] = np.zeros(len(f2),
                                  dtype=np.float64 if 'tail' in k
                                  else np.int64)
    return b, out


def class_census(g, delta, sites, J, K, D, nw_sites=None,
                 want_fam2=False, workers=WORKERS):
    """Bucketed class census.  Returns (aggregate dict, fam2 dict or
    None).  Aggregates are exact sums over buckets merged in bucket
    index order; fam2 arrays are concatenated in bucket index order
    (deterministic for every worker count)."""
    global _CTX
    _CTX = dict(g=g, delta=delta, J=J, K=K, D=D,
                sp_sites=sites,
                sp_bucket=_side_hash(g, sites, J, K),
                nw_sites=nw_sites,
                nw_bucket=(_side_hash(g, nw_sites, J, K)
                           if nw_sites is not None else None),
                want_fam2=want_fam2)
    results = {}
    if workers <= 1:
        for b in range(NBUCKETS):
            bb, out = _bucket_worker(b)
            results[bb] = out
    else:
        with Pool(workers) as pool:
            for bb, out in pool.imap_unordered(_bucket_worker,
                                               range(NBUCKETS)):
                results[bb] = out
    _CTX = {}
    agg = dict(ns=0, C_words=0, C_sides=0, n_words=0, n_sides=0,
               n_exch=0, sum_NP=0, f2_n=0, f2_mass=0, f2_red_num=0,
               f2_max_num=0, f2_tail_sum=0.0, all_tail_sum=0.0)
    agg['sp_f2_tail_hist'] = np.zeros(len(TAIL_EDGES) - 1, np.int64)
    agg['nw_f2_tail_hist'] = np.zeros(len(TAIL_EDGES) - 1, np.int64)
    hist = np.zeros(1, dtype=np.int64)
    fam2 = {k: [] for k in ('sides', 'NP', 'maxNPd', 'nmid',
                            'tail_sum', 'near_sum', 'first_site',
                            'mid_cls', 'mid_val', 'mid_cnt',
                            'nw_NP', 'nw_capn', 'nw_capf',
                            'nw_tail_sum')} if want_fam2 else None
    fam2_off = 0
    for b in range(NBUCKETS):
        out = results[b]
        for k in agg:
            if k in out:
                agg[k] += out[k]
        if 'NP_hist' in out:
            h = out['NP_hist']
            if len(h) > len(hist):
                hist = np.concatenate(
                    [hist, np.zeros(len(h) - len(hist), np.int64)])
            hist[:len(h)] += h
        if want_fam2 and 'fam2' in out:
            rec = out['fam2']
            for k in fam2:
                if k == 'mid_cls':
                    fam2[k].append(rec[k] + fam2_off)
                else:
                    fam2[k].append(rec[k])
            fam2_off += len(rec['NP'])
    agg['NP_hist'] = hist
    if want_fam2:
        fam2 = {k: (np.concatenate(v) if v else np.array([]))
                for k, v in fam2.items()}
    return agg, fam2
