# item-0019 m3 -- local quotient census (kickoff 3(d); RS.3, exact
# rational discipline).
#
# rho(P,d) = S(H(a,d,c)) / (S(H_pre(a)) S(H_suf(c))), even-conditioned
# (p = 2 factor exactly 2; RS.3).  |H| = k = (J+1)+(K+1) always (the
# translated suffix block sits strictly above the prefix block), so the
# (1-1/p)-powers cancel and the odd-prime factor is exactly
#     (1 - nu_H/p) / ((1 - nu_pre/p)(1 - nu_suf/p))
#   = (p - nu_H) p / ((p - nu_pre)(p - nu_suf)).
#
# Arithmetic discipline (kickoff 3(d), made operational):
#  - odd p <= S0 (S0 = max realized full-word span of the row across
#    the x ladder, printed): per-(P,d) EXACT integer products
#    N_c = prod (p - nu_H) p, D_c = prod (p - nu_pre)(p - nu_suf).
#  - (S0, Q]: nu's saturate (nu_H = k, nu_pre = J+1, nu_suf = K+1 for
#    p > span), one shared per-row EXACT integer band product.
#  - p > Q: certified one-sided tail.  For p > span the log-factor is
#    log(1-k/p) - log(1-a/p) - log(1-b/p) = -sum_{m>=2}
#    (k^m - a^m - b^m)/(m p^m) with a+b = k, hence <= 0 and
#    >= -(k^2/(2 p^2))/(1 - k/p).  Elementary comparison
#    sum_{p > Q} 1/p^2 < sum_{n > Q} 1/n^2 < 1/Q gives the certified
#    bound: true rho in [rho_Q * exp(-eps_Q), rho_Q] with
#    eps_Q = 0.51 k^2 / Q (the k^2/(Q ln Q) shape up to the elementary
#    integer-comparison slack; one-sided because the tail factors are
#    all <= 1).
#  - Q-stability line: Q in {1e4, 1e5, 1e6}.
#  - presentation floats: rho = 2 * float(N_c/D_c) * float(band(Q));
#    the two correctly-rounded conversions add <= 2 ulp, orders below
#    both the printed precision and eps_Q (noted once here).
#
# Validation (kickoff 3(d)): the three T4 witnesses at Q = 1e6 to
# their printed precision, plus one census value cross-checked against
# a verbatim budget_sheet.py rho_exact float evaluation.
#
# Determinism (v1.1 delta D2): pair order is the npz dump order
# (bucket index, then side-lex, then middle) -- a function of the data
# only; parallel chunks are fixed 4096-pair slices merged in slice
# order; every committed line is worker-count independent.

import numpy as np, math, json, os, sys, time
from fractions import Fraction
from multiprocessing import Pool
import common as C

QGRID = [10_000, 100_000, 1_000_000]
QREF = 1_000_000
PROFILE_PRIMES = [3, 5, 7, 11, 13]

_ODD_PRIMES_1E6 = None


def odd_primes(hi):
    global _ODD_PRIMES_1E6
    if _ODD_PRIMES_1E6 is None:
        _ODD_PRIMES_1E6 = np.nonzero(C.sieve_primes(QREF))[0][1:]
    return _ODD_PRIMES_1E6[_ODD_PRIMES_1E6 <= hi]


def nu_counts(pts, p):
    """Distinct residue count per row of pts (n, k) mod p."""
    r = np.sort(pts % p, axis=1)
    return 1 + (np.diff(r, axis=1) > 0).sum(axis=1)


_EX = {}


def _exact_chunk(args):
    lo, hi = args
    P = _EX
    nuH, nuA, nuB, primes = (P['nuH'][lo:hi], P['nuA'][lo:hi],
                             P['nuB'][lo:hi], P['primes'])
    out = []
    for i in range(hi - lo):
        n = 1
        d = 1
        hrow, arow, brow = nuH[i], nuA[i], nuB[i]
        for j, p in enumerate(primes):
            da = (p - int(arow[j])) * (p - int(brow[j]))
            if da == 0:
                # inadmissible block (possible only for classes whose
                # every member sits at a tiny anchor <= p): off-domain,
                # rho := 0 by the RS.3 convention; counted and printed
                n, d = 0, 1
                break
            n *= (p - int(hrow[j])) * p
            d *= da
        out.append((n, d))
    return lo, out


def exact_pair_products(nuH, nuA, nuB, primes, workers=C.WORKERS):
    """Per-pair exact integer products over odd p <= S0 (fixed 4096-
    pair chunks, merged in chunk order)."""
    global _EX
    n = len(nuH)
    _EX = dict(nuH=nuH, nuA=nuA, nuB=nuB, primes=[int(p) for p in primes])
    chunks = [(lo, min(lo + 4096, n)) for lo in range(0, n, 4096)]
    res = [None] * len(chunks)
    if workers <= 1 or len(chunks) <= 1:
        for ci, ch in enumerate(chunks):
            res[ci] = _exact_chunk(ch)[1]
    else:
        with Pool(workers) as pool:
            for lo, out in pool.imap_unordered(_exact_chunk, chunks):
                res[lo // 4096] = out
    _EX = {}
    nums, dens = [], []
    for r in res:
        for (a, b) in r:
            nums.append(a)
            dens.append(b)
    return nums, dens


def tree_prod(vals):
    """Balanced product tree over a list of ints (exact; the order of
    multiplication does not change the product)."""
    if not vals:
        return 1
    while len(vals) > 1:
        vals = [vals[i] * vals[i + 1] if i + 1 < len(vals)
                else vals[i] for i in range(0, len(vals), 2)]
    return vals[0]


def band_product(J, K, k, p_lo, p_hi):
    """Exact integer band product over odd primes p_lo < p <= p_hi of
    (p-k) p / ((p-(J+1))(p-(K+1)))."""
    ps = odd_primes(p_hi)
    ps = ps[ps > p_lo].tolist()
    n = tree_prod([(p - k) * p for p in ps])
    d = tree_prod([(p - (J + 1)) * (p - (K + 1)) for p in ps])
    return n, d


def spearman(a, b):
    def rank(v):
        order = np.argsort(v, kind='stable')
        r = np.empty(len(v))
        r[order] = np.arange(len(v))
        # midranks for ties
        sv = v[order]
        i = 0
        rr = r.copy()
        while i < len(sv):
            j = i
            while j + 1 < len(sv) and sv[j + 1] == sv[i]:
                j += 1
            rr[order[i:j + 1]] = 0.5 * (i + j)
            i = j + 1
        return rr
    ra, rb = rank(a), rank(b)
    return pearson(ra, rb)


def pearson(a, b):
    a = a - a.mean()
    b = b - b.mean()
    den = math.sqrt(float((a * a).sum()) * float((b * b).sum()))
    return float((a * b).sum()) / den if den > 0 else float('nan')


def load_row(J, K, D):
    """Load Fam_2 dumps for the row across the ladder; build the
    (P,d) pair census arrays."""
    data = {}
    for x in C.XLADDER:
        f = os.path.join(C.CACHE, f"fam2_{J}_{K}_{D}_{x}.npz")
        if not os.path.exists(f):
            continue
        z = dict(np.load(f))
        if len(z['NP']) == 0:
            continue
        data[x] = z
    return data


def pair_arrays(z, J, K):
    """Per-pair (class, d) geometry: point sets and features."""
    sides = z['sides'].astype(np.int64)
    pre = sides[:, :J]
    suf = sides[:, J:]
    Hpre = np.concatenate([np.zeros((len(sides), 1), np.int64),
                           np.cumsum(pre, axis=1)], axis=1)
    Hsuf = np.concatenate([np.zeros((len(sides), 1), np.int64),
                           np.cumsum(suf, axis=1)], axis=1)
    AJ = Hpre[:, -1]
    CK = Hsuf[:, -1]
    ci = z['mid_cls'].astype(np.int64)
    d = z['mid_val'].astype(np.int64)
    Hp = Hpre[ci]
    Hs = Hsuf[ci] + (AJ[ci] + d)[:, None]
    H = np.concatenate([Hp, Hs], axis=1)
    span = AJ[ci] + d + CK[ci]
    return dict(Hpre=Hpre, Hsuf=Hsuf, AJ=AJ, CK=CK,
                ci=ci, d=d, H=H, span=span,
                pre=pre, suf=suf)


def rho_for_x(z, geo, J, K, S0, bandf, workers=C.WORKERS):
    """Exact census at one x: returns per-pair rho floats (Q = 1e6
    reference) and per-pair exact ints for spot checks."""
    k = J + K + 2
    primes = odd_primes(S0)
    npair = len(geo['d'])
    nuH = np.empty((npair, len(primes)), np.int16)
    nuA = np.empty((npair, len(primes)), np.int16)
    nuB = np.empty((npair, len(primes)), np.int16)
    for j, p in enumerate(primes.tolist()):
        nuH[:, j] = nu_counts(geo['H'], p)
        nuA[:, j] = nu_counts(geo['Hpre'], p)[geo['ci']]
        nuB[:, j] = nu_counts(geo['Hsuf'], p)[geo['ci']]
    nums, dens = exact_pair_products(nuH, nuA, nuB, primes, workers)
    rho = np.array([2.0 * float(Fraction(n, d)) * bandf
                    for n, d in zip(nums, dens)])
    return rho, nums, dens, nuH, nuA, nuB, primes


def dmean_line(z, geo, J, K, S0, bandf, W, workers=C.WORKERS):
    """HEURISTIC/U18.2 reference: per-class mean of rho over ALL even
    in-window middles d (2 <= d <= W - flankspan).  Float log-domain;
    labeled heuristic in every table.

    The sweep reaches spans up to W, which can exceed the max
    REALIZED span S0, so the exact per-p loop runs over odd p <= W
    and the saturated contribution of the extra primes in (S0, W] is
    divided out of the (S0, Q] band factor first (they cannot be
    assumed saturated for the largest unrealized d)."""
    k = J + K + 2
    primes = [int(p) for p in odd_primes(max(S0, int(W)))]
    lnband = math.log(bandf) + math.log(2.0)
    for p in primes:
        if p > S0:
            lnband -= (math.log((p - k) * p)
                       - math.log((p - (J + 1)) * (p - (K + 1))))
    nP = len(z['NP'])
    means = np.zeros(nP)
    for i in range(nP):
        AJ = int(geo['AJ'][i])
        CK = int(geo['CK'][i])
        dmax = int(W - AJ - CK)
        if dmax < 2:
            means[i] = float('nan')
            continue
        ds = np.arange(2, dmax + 1, 2, dtype=np.int64)
        lg = np.full(len(ds), lnband)
        bad = False
        for p in primes:
            rpre = np.unique(geo['Hpre'][i] % p)
            rsuf = np.unique(geo['Hsuf'][i] % p)
            a = len(rpre)
            b = len(rsuf)
            if a == p or b == p:
                bad = True  # off-domain block (tiny-anchor class)
                break
            mpre = 0
            for r in rpre.tolist():
                mpre |= 1 << r
            msuf = 0
            for r in rsuf.tolist():
                msuf |= 1 << r
            full = (1 << p) - 1
            fac = np.empty(p)
            for r in range(p):
                rot = ((msuf << r) | (msuf >> (p - r))) & full
                nu = (mpre | rot).bit_count()
                # nu = p: inadmissible middle -> rho(P,d) = 0 exactly
                fac[r] = (math.log((p - nu) * p)
                          - math.log((p - a) * (p - b))
                          if nu < p else -1e300)
            lg += fac[(AJ + ds) % p]
        means[i] = (float(np.mean(np.exp(np.maximum(lg, -700.0))
                                  * (lg > -690)))
                    if not bad else float('nan'))
    return means


def _dmean_chunk(args):
    lo, hi = args
    P = _EX
    z, geo, J, K, S0, bandf, W = (P['z'], P['geo'], P['J'], P['K'],
                                  P['S0'], P['bandf'], P['W'])
    sub_geo = {k2: (v[lo:hi] if k2 in ('Hpre', 'Hsuf', 'AJ', 'CK')
                    else v) for k2, v in geo.items()}
    sub_z = {'NP': z['NP'][lo:hi]}
    return lo, dmean_line(sub_z, sub_geo, J, K, S0, bandf, W, 1)


def dmean_parallel(z, geo, J, K, S0, bandf, W, workers=C.WORKERS):
    global _EX
    n = len(z['NP'])
    _EX = dict(z=z, geo=geo, J=J, K=K, S0=S0, bandf=bandf, W=W)
    chunks = [(lo, min(lo + 1024, n)) for lo in range(0, n, 1024)]
    out = np.zeros(n)
    if workers <= 1 or len(chunks) <= 1:
        for ch in chunks:
            lo, part = _dmean_chunk(ch)
            out[lo:lo + len(part)] = part
    else:
        with Pool(workers) as pool:
            for lo, part in pool.imap_unordered(_dmean_chunk, chunks):
                out[lo:lo + len(part)] = part
    _EX = {}
    return out


# ------------------------------------------------------------------ #
# Validation layer

def rho_exact_budget_sheet(H_pre, H_suf, d, pmax=10 ** 6):
    """VERBATIM float reference from item-0018 budget_sheet.py
    (rho_exact), sympy primerange semantics."""
    from sympy import primerange

    def nu_classes(H, p):
        return len(set(h % p for h in H))

    A_J = max(H_pre)
    H = sorted(set(H_pre) | set(A_J + d + s for s in H_suf))
    for p in primerange(2, len(H) + 2):
        if nu_classes(H, p) == p:
            return None, H
    r = 1.0
    npow = len(H) - len(H_pre) - len(H_suf)
    for p in primerange(2, pmax):
        a, b, c = (nu_classes(H, p), nu_classes(H_pre, p),
                   nu_classes(H_suf, p))
        r *= (1 - a / p) / ((1 - b / p) * (1 - c / p)
                            * (1 - 1 / p) ** npow)
    return r, H


def witness_rho(H_pre, H_suf, d):
    """T4 witness through THIS pipeline at Q = 1e6: exact rational
    over odd p <= span, saturated exact band (span, 1e6]."""
    A_J = max(H_pre)
    H = sorted(set(H_pre) | set(A_J + d + s for s in H_suf))
    span = max(H)
    k, a, b = len(H), len(H_pre), len(H_suf)
    Hn = np.array([H]);  An = np.array([H_pre]);  Bn = np.array([H_suf])
    nums, dens = [], []
    for p in odd_primes(span).tolist():
        nH = int(nu_counts(Hn, p)[0])
        nA = int(nu_counts(An, p)[0])
        nB = int(nu_counts(Bn, p)[0])
        nums.append((p - nH) * p)
        dens.append((p - nA) * (p - nB))
    ps = odd_primes(QREF)
    for p in ps[ps > span].tolist():
        nums.append((p - k) * p)
        dens.append((p - a) * (p - b))
    return 2.0 * float(Fraction(tree_prod(nums), tree_prod(dens)))


def validate():
    print("m3 validation (kickoff 3(d)):")
    W = [("1e8", [0, 2, 6, 8, 12], [0, 2, 6, 8, 12], 198, 82.24),
         ("1e20", [0, 60, 72, 106, 166, 178],
          [0, 60, 72, 106, 166, 178], 32, 221.66),
         ("1e1000", [0, 2, 6, 8, 12, 18, 20, 26, 30, 32, 36, 42],
          [0, 2, 6, 8, 12, 18, 20, 26, 30, 32, 36, 42], 29988,
          1060.34)]
    allok = True
    for tag, hp, hs, d, want in W:
        got = witness_rho(hp, hs, d)
        ok = round(got, 2) == want
        allok &= ok
        print(f"  T4 witness {tag}: pipeline rho = {got:.2f}, "
              f"printed = {want:.2f}: {'PASS' if ok else 'FAIL'}")
    return allok


# ------------------------------------------------------------------ #

def process_row(J, K, D, out_json):
    t0 = time.time()
    k = J + K + 2
    data = load_row(J, K, D)
    if not data:
        print(f"({J},{K},{D}): no Fam_2 classes anywhere -- skipped")
        return None
    geos = {x: pair_arrays(z, J, K) for x, z in data.items()}
    S0 = int(max(int(g['span'].max()) for g in geos.values()))
    res = dict(J=J, K=K, D=D, S0=S0, k=k, x={})
    # shared band products and tail widths
    bands = {}
    for Q in QGRID:
        n, d = band_product(J, K, k, S0, Q)
        bands[Q] = float(Fraction(n, d))
    res['bands'] = {str(Q): bands[Q] for Q in QGRID}
    res['eps'] = {str(Q): 0.51 * k * k / Q for Q in QGRID}
    print(f"({J},{K},{D}) S0 = {S0}, band(S0,1e6] = {bands[QREF]:.6f},"
          f" eps_1e6 = {res['eps'][str(QREF)]:.2e}", flush=True)
    for x, z in sorted(data.items()):
        geo = geos[x]
        lnx = math.log(x)
        L = J + 1 + K
        Wcap = C.APRIME * L * lnx
        rho, nums, dens, nuH, nuA, nuB, primes = rho_for_x(
            z, geo, J, K, S0, bands[QREF])
        NP = z['NP'].astype(np.int64)
        NPd = z['mid_cnt'].astype(np.int64)
        ci = geo['ci']
        d = geo['d']
        xres = dict(npairs=len(rho), nclasses=len(NP),
                    off_domain_zero=int((rho == 0).sum()))
        # census statistics (unweighted over realized (P,d) pairs;
        # mass-weighted mean labeled)
        qs = [1, 5, 25, 50, 75, 95, 99]
        xres['rho_mean'] = float(rho.mean())
        xres['rho_mean_mass'] = float((rho * NPd).sum() / NPd.sum())
        xres['rho_q'] = {q: float(np.percentile(rho, q)) for q in qs}
        # top-10 by rho (desc), ties by side-lex dump order
        top = np.argsort(-rho, kind='stable')[:10]
        toplist = []
        for i in top.tolist():
            c = int(ci[i])
            prof = {}
            for p in PROFILE_PRIMES:
                jj = int(np.searchsorted(primes, p))
                if jj < len(primes) and primes[jj] == p:
                    prof[p] = [int(nuH[i, jj]), int(nuA[i, jj]),
                               int(nuB[i, jj])]
            toplist.append(dict(
                rho=float(rho[i]),
                prefix=z['sides'][c][:J].tolist(),
                d=int(d[i]),
                suffix=z['sides'][c][J:].tolist(),
                NP=int(NP[c]), NPd=int(NPd[i]),
                span=int(geo['span'][i]), profile=prof))
        xres['top10'] = toplist
        # per-class quantities for correlations / collapse
        # d* = argmax_d N_{P,d}, smallest d on ties (adversarial
        # selection identification, stated once here)
        order = np.lexsort((d, -NPd, ci))
        first = np.unique(ci[order], return_index=True)[1]
        dstar_idx = order[first]  # one pair index per class
        cls_of = ci[dstar_idx]
        rho_dstar = np.zeros(len(NP))
        rho_dstar[cls_of] = rho[dstar_idx]
        rho_bar = np.zeros(len(NP))
        np.add.at(rho_bar, ci, rho * NPd)
        rho_bar /= NP
        red = (z['maxNPd'].astype(np.float64) - 1) / NP
        xres['collapse_y'] = None
        y = red * lnx / np.where(rho_dstar > 0, rho_dstar, np.nan)
        xres['collapse_q'] = {q: float(np.nanpercentile(y, q))
                              for q in [5, 25, 50, 75, 95]}
        xres['collapse_mean'] = float(np.nanmean(y))
        # flank features
        span_fl = (geo['AJ'] + geo['CK']).astype(np.float64)
        mingap = np.minimum(geo['pre'].min(axis=1),
                            geo['suf'].min(axis=1)).astype(np.float64)
        cov = np.zeros(len(NP))
        nprof = 0
        for p in PROFILE_PRIMES[:4]:
            jj = int(np.searchsorted(primes, p))
            if jj < len(primes) and primes[jj] == p:
                covp = (nuA[:, jj].astype(np.float64)
                        + nuB[:, jj]) / (2.0 * p)
                cv = np.zeros(len(NP))
                cv[ci[dstar_idx]] = covp[dstar_idx]
                cov += cv
                nprof += 1
        cov /= max(nprof, 1)
        # m4 per-class columns (RS.4 worlds kept separate)
        nwNP = z['nw_NP'].astype(np.float64)
        wmask = nwNP > 0
        capn_rate = np.divide(z['nw_capn'], nwNP, out=np.zeros_like(
            nwNP), where=wmask)
        capf_rate = np.divide(z['nw_capf'], nwNP, out=np.zeros_like(
            nwNP), where=wmask)
        tail_mean = z['tail_sum'] / NP
        corr = {}
        for name, v in [('span_flank', span_fl[cls_of]),
                        ('min_gap', mingap[cls_of]),
                        ('coverage', cov),
                        ('capfail_near', capn_rate),
                        ('capfail_far', capf_rate),
                        ('tail_mean', tail_mean),
                        ('concentration_red', red)]:
            m = np.isfinite(v) & np.isfinite(rho_bar)
            corr[name] = [pearson(rho_bar[m], v[m]),
                          spearman(rho_bar[m], v[m])]
        xres['corr_rho_bar'] = corr
        xres['corr_red_vs_rho_dstar'] = [
            pearson(red, rho_dstar), spearman(red, rho_dstar)]
        # HEURISTIC/U18.2 lines
        dm = dmean_parallel(z, geo, J, K, S0, bands[QREF], Wcap)
        m = np.isfinite(dm)
        xres['dmean_heuristic'] = dict(
            mean=float(np.mean(dm[m])) if m.any() else float('nan'),
            q=({q: float(np.percentile(dm[m], q))
                for q in [5, 25, 50, 75, 95]} if m.any() else {}))
        # Normalized residuals of the heuristic middle law.  POISSON
        # normalization z = (obs - mu)/sqrt(mu), mu = N_P * pred: the
        # binomial (1 - pred) factor is ill-posed here because pred =
        # rho e^{-d/lnx}/ln x exceeds 1 on high-rho realized pairs at
        # these scales (corrected-T4 sup regime) and its clamp
        # dominates the statistic; the pred >= 1 count is reported.
        pred = rho * np.exp(-d / lnx) / lnx
        mu = NP[ci] * pred
        with np.errstate(divide='ignore', invalid='ignore'):
            zres = (NPd - mu) / np.sqrt(mu)
        mm = np.isfinite(zres)
        xres['midlaw_z'] = dict(
            mean=float(zres[mm].mean()), sd=float(zres[mm].std()),
            pred_ge_1=int((pred >= 1).sum()),
            q={q: float(np.percentile(zres[mm], q))
               for q in [5, 25, 75, 95]})
        # aggregate calibration of the same heuristic law (the z's
        # are dominated by sub-1-mass cells at these multiplicities:
        # every realized cell has N_{P,d} >= 1 against predictions
        # << 1, the e2prime 7.1(c) corner), reported alongside:
        xres['midlaw_aggregate'] = dict(
            obs=int(NPd.sum()),
            pred=float((NP[ci] * pred).sum()),
            ratio=float(NPd.sum() / (NP[ci] * pred).sum()))
        res['x'][str(x)] = xres
        print(f"  x={x:.0e}: pairs={len(rho)} classes={len(NP)} "
              f"rho mean={xres['rho_mean']:.3f} "
              f"med={xres['rho_q'][50]:.3f} "
              f"[{time.time() - t0:.0f}s]", flush=True)
    # budget_sheet rho_exact cross-check on one census value:
    # deterministic pick = the largest-N_{P,d} pair (ties: dump order)
    # at the largest x of the row
    xmax = max(data)
    z = data[xmax]
    geo = geos[xmax]
    NPd = z['mid_cnt'].astype(np.int64)
    i = int(np.argmax(NPd))
    c = int(geo['ci'][i])
    hp = [0] + np.cumsum(z['sides'][c][:J]).astype(int).tolist()
    hs = [0] + np.cumsum(z['sides'][c][J:]).astype(int).tolist()
    dd = int(geo['d'][i])
    ref, _ = rho_exact_budget_sheet(hp, hs, dd)
    mine = witness_rho(hp, hs, dd)
    rel = abs(mine - ref) / ref
    res['crosscheck'] = dict(x=xmax, H_pre=hp, H_suf=hs, d=dd,
                             budget_sheet=ref, pipeline=mine,
                             rel_diff=rel, ok=bool(rel < 1e-8))
    print(f"  rho_exact cross-check: pipeline {mine:.6f} vs "
          f"budget_sheet {ref:.6f} (rel {rel:.1e}) "
          f"{'PASS' if rel < 1e-8 else 'FAIL'}", flush=True)
    with open(out_json, 'w') as f:
        json.dump(res, f, indent=1)
    return res


if __name__ == '__main__':
    if sys.argv[1] == 'validate':
        ok = validate()
        sys.exit(0 if ok else 1)
    J, K, D = map(int, sys.argv[1:4])
    process_row(J, K, D,
                os.path.join(C.CACHE, f"m3_{J}_{K}_{D}.json"))
