# item-0019 -- Phase A/B driver: filter layer, dictionary smoke test,
# continuity + V1 reproduction, m1/m2/m4 aggregates, Fam_2 class dumps
# for m3 (rho_census.py).
#
# Usage: python3 census.py <x>        (x in the ladder; 1e9 also runs
#                                      the dictionary smoke test)
# Raw outputs (uncommitted, regenerable): results_<x>.json and
# fam2_<J>_<K>_<D>_<x>.npz under $ITEM0019_CACHE; committed ASCII
# tables are produced by consolidate.py from these.
#
# Worlds (RS.4, never mixed): d02 = D0.2-style (delta caps only, seed
# A = None world; continuity + V1 anchors); d02p = D0.2' (campaign
# baseline S'_x); nw = N^w (window cap only).  m5 lives in m5_thinning
# (N^o world, anchor firewall; never joined on a site index).

import numpy as np, math, json, os, sys, time
import common as C

TAIL_EDGES = C.TAIL_EDGES

# V1 anchors (e2prime-supply 7.1/7.2, committed records; kickoff S.2)
V1 = {
    (2_000_000, 4, 5, 30): dict(ns=143787, nW=143761, nP=143749,
                                cw=52, cs=76, p1=24, cls=12),
    (2_000_000, 5, 5, 34): dict(ns=145248, nW=145241, nP=145239,
                                cw=14, cs=18, p1=4, cls=2),
    (2_000_000, 6, 6, 64): dict(ns=148703, nW=148702, nP=148702,
                                cw=2, cs=2, p1=0, cls=0),
    (2_000_000, 7, 7, 67): dict(ns=148711, cls=0),
    (20_000_000, 4, 5, 30): dict(ns=1162405, nW=1162194, nP=1162016,
                                 cw=422, cs=778, p1=356, cls=178),
    (20_000_000, 5, 5, 34): dict(ns=1190922, nW=1190889, nP=1190868,
                                 cw=66, cs=108, p1=42, cls=21),
    (20_000_000, 6, 6, 64): dict(ns=1269901, nW=1269900, nP=1269900,
                                 cw=2, cs=2, p1=0, cls=0),
    (100_000_000, 4, 5, 30): dict(ns=4978302, nW=4976976, nP=4975689,
                                  cw=2654, cs=5232, p1=2578, cls=1287),
    (100_000_000, 5, 5, 34): dict(ns=5161256, nW=5161080, nP=5160937,
                                  cw=352, cs=638, p1=286, cls=143),
    (100_000_000, 6, 6, 64): dict(ns=5754075, nW=5754073, nP=5754072,
                                  cw=4, cs=6, p1=2, cls=1),
    (100_000_000, 7, 7, 67): dict(ns=5758932, cls=0),
    (1_000_000_000, 6, 6, 64): dict(cls=29),
    (1_000_000_000, 7, 7, 67): dict(cls=0),
    (1_000_000_000, 8, 8, 67): dict(cls=0),
    (1_000_000_000, 7, 6, 44): dict(cls=3),
    (1_000_000_000, 7, 6, 27): dict(cls=3),
}
PI_X = {2_000_000: 148933, 20_000_000: 1270607,
        100_000_000: 5761455, 1_000_000_000: 50847534}

# (7,6,44,3) certificate record (e2prime-supply 7.2, verbatim ints)
CERT = dict(
    J=7, K=6, D=44,
    t1=7113518,
    primes1=[125063227, 125063231, 125063233, 125063249, 125063251,
             125063261, 125063273, 125063291, 125063297, 125063317,
             125063329, 125063333, 125063347, 125063353, 125063357,
             125063369],
    prefix=[4, 2, 16, 2, 10, 12, 18], mid1=6,
    suffix=[20, 12, 4, 14, 6, 4],
    t2=960168,
    primes2=[14824987, 14824991, 14824993, 14825009, 14825011,
             14825021, 14825033, 14825051, 14825081, 14825101,
             14825113, 14825117, 14825131, 14825137, 14825141,
             14825147],
    mid2=30, d1=-24,
    delta1=(10.426, 14.562), delta2=(22.477, 21.089),
)


def jclean(o):
    if isinstance(o, dict):
        return {k: jclean(v) for k, v in o.items()}
    if isinstance(o, (list, tuple)):
        return [jclean(v) for v in o]
    if isinstance(o, np.ndarray):
        return o.tolist()
    if isinstance(o, (np.integer,)):
        return int(o)
    if isinstance(o, (np.floating,)):
        return float(o)
    return o


def tail_hist(vals):
    h, _ = np.histogram(vals, bins=TAIL_EDGES)
    return h.astype(np.int64)


def smoke_test(p, g, delta, VALID, x, report):
    """Kickoff 3(a): re-derive the (7,6,44,3) certificate pair and
    match the printed record byte-for-byte on the integer data."""
    J, K, D = CERT['J'], CERT['K'], CERT['D']
    L = J + 1 + K
    ok = True

    def chk(label, got, want):
        nonlocal ok
        good = (got == want)
        ok &= good
        report.append(f"  {label}: {'PASS' if good else 'FAIL'}"
                      + ("" if good else f" got={got} want={want}"))

    for tt, primes, mid, dn, df in (
            (CERT['t1'], CERT['primes1'], CERT['mid1'],
             CERT['delta1'][0], CERT['delta1'][1]),
            (CERT['t2'], CERT['primes2'], CERT['mid2'],
             CERT['delta2'][0], CERT['delta2'][1])):
        chk(f"t={tt} primes", list(p[tt:tt + J + K + 3]), primes)
        chk(f"t={tt} prefix", list(map(int, g[tt:tt + J])),
            CERT['prefix'])
        chk(f"t={tt} middle", int(g[tt + J]), mid)
        chk(f"t={tt} suffix", list(map(int, g[tt + J + 1:tt + J + 1 + K])),
            CERT['suffix'])
        near, far = delta[tt + J], delta[tt + J + K + 1]
        chk(f"t={tt} near delta (3dp)", round(float(near), 3), dn)
        chk(f"t={tt} far delta (3dp)", round(float(far), 3), df)
        chk(f"t={tt} near cap <= {D}", bool(near <= D), True)
        chk(f"t={tt} far cap <= {2**K}", bool(far <= float(2 ** K)),
            True)
        chk(f"t={tt} near delta <= 27 (b=5 row)", bool(near <= 27),
            True)
    d1 = CERT['mid1'] - CERT['mid2']
    chk("d1", d1, CERT['d1'])
    chk("(E5) gate b=3: 3*(D-2) < 2^(J+1)",
        f"{3 * (D - 2)}<{2 ** (J + 1)}: {3 * (D - 2) < 2 ** (J + 1)}",
        "126<256: True")
    chk("(E5) gate b=1: (D-2) < 2^(J+1)",
        f"{D - 2}<{2 ** (J + 1)}: {D - 2 < 2 ** (J + 1)}",
        "42<256: True")
    t1, t2 = CERT['t1'], CERT['t2']
    lhs = delta[t1 + J] - delta[t2 + J]
    rhs = d1 / 2 + 2.0 ** -(K + 1) * (delta[t1 + J + K + 1]
                                      - delta[t2 + J + K + 1])
    resid = lhs - rhs
    report.append(f"  identity residual = {resid:.2e} "
                  f"(printed record -1.78e-15)")
    ok &= abs(resid) < 1e-12
    # both sites are in the D0.2-filtered site set and share the class
    t = C.site_range(VALID, J, K)
    okf = C.filter_d02(delta, t, J, K, D)
    sset = set(t[okf].tolist())
    chk("t1 in filtered sites", t1 in sset, True)
    chk("t2 in filtered sites", t2 in sset, True)
    report.append(f"  SMOKE TEST OVERALL: {'PASS' if ok else 'FAIL'}")
    return ok


def run_row(g, delta, VALID, x, J, K, D, lnx, dump_tag):
    L = J + 1 + K
    t = C.site_range(VALID, J, K)
    res = {}
    # D0.2-style world (continuity + V1 anchors)
    s02 = t[C.filter_d02(delta, t, J, K, D)]
    agg02, _ = C.class_census(g, delta, s02, J, K, D)
    res['d02'] = dict(ns=agg02['ns'],
                      nW=agg02['n_words'], nP=agg02['n_sides'],
                      cw=agg02['C_words'] - agg02['ns'],
                      cs=agg02['C_sides'] - agg02['ns'],
                      p1=agg02['C_sides'] - agg02['C_words'],
                      cls=agg02['n_exch'])
    # D0.2' world (campaign baseline) + N^w join
    W = C.APRIME * L * lnx
    wsum = C.window_sums(g, t, L)
    okw = wsum <= W
    sP = t[C.filter_d02(delta, t, J, K, D) & okw]
    sW = t[okw]
    agg, fam2 = C.class_census(g, delta, sP, J, K, D, nw_sites=sW,
                               want_fam2=True)
    res['W'] = W
    res['d02p'] = dict(ns=agg['ns'],
                       nW=agg['n_words'], nP=agg['n_sides'],
                       cw=agg['C_words'] - agg['ns'],
                       cs=agg['C_sides'] - agg['ns'],
                       p1=agg['C_sides'] - agg['C_words'],
                       cls=agg['n_exch'],
                       NP_hist=agg['NP_hist'],
                       f2_n=agg['f2_n'], f2_mass=agg['f2_mass'],
                       f2_red_num=agg['f2_red_num'],
                       f2_max_num=agg['f2_max_num'],
                       f2_tail_sum=agg['f2_tail_sum'],
                       all_tail_sum=agg['all_tail_sum'])
    # N^w-world global statistics (vector ops over ALL N^w sites; the
    # bucket join only serves the per-class columns)
    res['nw'] = dict(ns=len(sW),
                     capn_tot=int((delta[sW + J] > D).sum()),
                     capf_tot=int((delta[sW + L]
                                   > float(2 ** K)).sum()),
                     tail_tot=float(delta[sW + L].sum()))
    # per-site tail histograms (Fam_2-conditional ones from buckets)
    res['sp_tail_hist'] = tail_hist(delta[sP + L])
    res['nw_tail_hist'] = tail_hist(delta[sW + L])
    res['sp_f2_tail_hist'] = agg['sp_f2_tail_hist']
    res['nw_f2_tail_hist'] = agg['nw_f2_tail_hist']
    np.savez_compressed(
        os.path.join(C.CACHE, f"fam2_{dump_tag}.npz"), **fam2)
    return res


def main(x):
    t0 = time.time()
    p, g, delta, VALID = C.build(x)
    lnx = math.log(x)
    print(f"x = {x:.0e}: pi = {len(p)}, ln x = {lnx:.3f}, "
          f"build {time.time() - t0:.0f}s", flush=True)
    assert len(p) == PI_X[x], f"pi(x) mismatch: {len(p)}"
    # one-time delta smoke check (v1.1 delta D3) at the 1e8 prefix
    out = dict(x=x, pi=len(p), lnx=lnx, workers=C.WORKERS,
               rows={}, checks={})
    if x == 100_000_000:
        ds = np.array(C._delta_serial(g.tolist(), len(g)))
        dp = C.delta_parallel(g)
        md = float(np.max(np.abs(ds - dp)))
        print(f"delta parallel-vs-serial smoke (1e8): "
              f"max abs diff = {md:.1e}", flush=True)
        out['checks']['delta_smoke_maxabs'] = md
        assert md < 1e-12
        del ds, dp
    rows = C.GRID[:]
    if x == 1_000_000_000:
        rows.append((8, 8, 67))
    if x == 100_000_000:
        rows += [(4, 5, 44), (4, 5, 67)]
    for (J, K, D) in rows:
        t1 = time.time()
        res = run_row(g, delta, VALID, x, J, K, D, lnx,
                      f"{J}_{K}_{D}_{x}")
        # V1 reproduction check (committed anchors only)
        key = (x, J, K, D)
        if key in V1:
            want = V1[key]
            got = res['d02']
            res['v1'] = {k: [got[k], want[k], got[k] == want[k]]
                         for k in want}
            bad = [k for k in want if got[k] != want[k]]
            if bad:
                print(f"V1 MISMATCH at {key}: " +
                      ", ".join(f"{k} got {got[k]} want {want[k]}"
                                for k in bad), flush=True)
        print(f"  ({J},{K},{D}): d02 sites={res['d02']['ns']} "
              f"cls={res['d02']['cls']} | d02p sites={res['d02p']['ns']} "
              f"cls={res['d02p']['cls']} fam2={res['d02p']['f2_n']} "
              f"[{time.time() - t1:.0f}s]", flush=True)
        out['rows'][f"{J},{K},{D}"] = res
    # extra class-count rows for the smoke package at 1e9
    if x == 1_000_000_000:
        for (J, K, D) in [(7, 6, 27)]:
            t = C.site_range(VALID, J, K)
            s02 = t[C.filter_d02(delta, t, J, K, D)]
            agg02, _ = C.class_census(g, delta, s02, J, K, D)
            res = dict(d02=dict(ns=agg02['ns'], cls=agg02['n_exch']))
            key = (x, J, K, D)
            res['v1'] = {'cls': [agg02['n_exch'], V1[key]['cls'],
                                 agg02['n_exch'] == V1[key]['cls']]}
            out['rows'][f"{J},{K},{D}"] = res
            print(f"  ({J},{K},{D}): d02 sites={agg02['ns']} "
                  f"cls={agg02['n_exch']}", flush=True)
        rep = [f"Dictionary smoke test (7,6,44,3) at x = 1e9 "
               f"(D0.2-style filter, seed conventions):"]
        ok = smoke_test(p, g, delta, VALID, x, rep)
        out['checks']['smoke_ok'] = bool(ok)
        out['checks']['smoke_report'] = rep
        print("\n".join(rep), flush=True)
    with open(os.path.join(C.CACHE, f"results_{x}.json"), "w") as f:
        json.dump(jclean(out), f, indent=1)
    print(f"TOTAL {time.time() - t0:.0f}s", flush=True)


if __name__ == '__main__':
    main(int(float(sys.argv[1])))
