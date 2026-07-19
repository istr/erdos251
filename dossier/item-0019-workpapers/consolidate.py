# item-0019 -- consolidate raw run outputs (uncommitted cache) into
# the committed ASCII tables under tables/.
#
# Usage: python3 consolidate.py [core|m3|m5]   (default: core)
#   core -> tables/continuity.txt, smoke_test.txt, m1_class_sizes.txt,
#           m2_concentration.txt, m4_tails.txt, d_sensitivity.txt,
#           readout_families.txt
#   m3   -> tables/m3_rho_census.txt (from m3_<row>.json)
#   m5   -> tables/m5_thinning.txt   (from m5.json)
#
# All statistics are D0.2' unless the column header says otherwise
# (kickoff Section 4); the continuity table is the ONLY place D0.2 and
# D0.2' appear side by side.  Count worlds (RS.4) are always labeled:
# S' = S'_x (D0.2'), N^w = window-cap-only, N^o = m5 only (separate
# file, anchor firewall).

import numpy as np, math, json, os, sys
import common as C

TDIR = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                    "tables")
THETAS = [0.0, 0.25, 0.5]
CSTAR = 4 * math.log(2) - 2


def jload(x):
    f = os.path.join(C.CACHE, f"results_{x}.json")
    return json.load(open(f)) if os.path.exists(f) else None


def zload(J, K, D, x):
    f = os.path.join(C.CACHE, f"fam2_{J}_{K}_{D}_{x}.npz")
    if not os.path.exists(f):
        return None
    z = dict(np.load(f))
    return z if len(z['NP']) else None


def wfile(name, lines):
    os.makedirs(TDIR, exist_ok=True)
    path = os.path.join(TDIR, name)
    with open(path, "w") as f:
        f.write("\n".join(lines) + "\n")
    print(f"wrote {path} ({len(lines)} lines)")


def rows_for(x):
    rows = [f"{J},{K},{D}" for (J, K, D) in C.GRID]
    if x == 1_000_000_000:
        rows.append("8,8,67")
    return rows


def continuity():
    lines = [
        "item-0019 3(a): continuity table, D0.2-style (delta caps",
        "only, seed A = None world) vs D0.2' (aggregate window cap",
        "W = A' L ln x, A' = 1.5, + both delta caps).  The ONLY place",
        "both filters appear (kickoff Section 4).  V1 column: PASS =",
        "every committed anchor for that (row, x) reproduced exactly",
        "(e2prime-supply 7.1/7.2 committed records: sites, |W_L|,",
        "|P|, off-diagonal C_words/C_sides, P1 pairs, exchange",
        "classes, where recorded; '-' = no committed record).",
        "Columns: sites, exchange classes (>= 2 distinct middles),",
        "off-diagonal side collisions C_s; delta columns are",
        "D0.2 minus D0.2' (sites removed by the window cap).", ""]
    hdr = (f"{'row':>9} {'x':>6} | {'sites02':>9} {'cls':>5} "
           f"{'Cs_off':>7} | {'sites02p':>9} {'cls':>5} {'Cs_off':>7}"
           f" | {'d_sites':>8} {'d_cls':>5} | {'V1':>4}")
    lines.append(hdr)
    lines.append("-" * len(hdr))
    for x in C.XLADDER:
        r = jload(x)
        if not r:
            continue
        for row in rows_for(x):
            res = r['rows'].get(row)
            if not res:
                continue
            a, b = res['d02'], res['d02p']
            v1 = res.get('v1')
            v1s = ('PASS' if all(v[2] for v in v1.values())
                   else 'FAIL') if v1 else '-'
            lines.append(
                f"{row:>9} {x:>8.0e}" +
                f" | {a['ns']:>9} {a['cls']:>5} {a['cs']:>7} | "
                f"{b['ns']:>9} {b['cls']:>5} {b['cs']:>7} | "
                f"{a['ns'] - b['ns']:>8} {a['cls'] - b['cls']:>5} | "
                f"{v1s:>4}")
        lines.append("")
    # full V1 reproduction record
    lines += ["V1 reproduction record (every committed anchor,",
              "got = want required):"]
    PI_WANT = {2_000_000: 148933, 20_000_000: 1270607,
               100_000_000: 5761455, 1_000_000_000: 50847534}
    for x in C.XLADDER:
        r = jload(x)
        if not r:
            continue
        lines.append(
            f"  x={x:.0e} pi(x): got {r['pi']} want {PI_WANT[x]} "
            f"{'PASS' if r['pi'] == PI_WANT[x] else 'FAIL'}")
        for row, res in r['rows'].items():
            if 'v1' not in res:
                continue
            for k, v in res['v1'].items():
                lines.append(
                    f"  x={x:.0e} ({row}) {k}: got {v[0]} want {v[1]}"
                    f" {'PASS' if v[2] else 'FAIL'}")
    # window caps
    lines += ["", "window caps W = 1.5 L ln x (float64; int64 window "
              "sum <= W comparison):"]
    for x in C.XLADDER:
        r = jload(x)
        if not r:
            continue
        for row in rows_for(x):
            if row in r['rows'] and 'W' in r['rows'][row]:
                lines.append(f"  x={x:.0e} ({row}): "
                             f"W = {r['rows'][row]['W']:.6f}")
    wfile("continuity.txt", lines)


def smoke():
    r = jload(1_000_000_000)
    if not r or 'smoke_report' not in r['checks']:
        return
    lines = ["item-0019 3(a) dictionary smoke test (executed before",
             "any census row was reported; integer data matched",
             "byte-for-byte against the e2prime-supply 7.2 record):",
             ""] + r['checks']['smoke_report']
    lines += ["", f"pi(1e9) = {r['pi']} (committed: 50847534)",
              f"delta parallel-vs-serial smoke (1e8 prefix, v1.1 "
              f"delta D3): max abs diff = "
              f"{jload(100_000_000)['checks']['delta_smoke_maxabs']:.1e}"
              f" (accept < 1e-12)"]
    wfile("smoke_test.txt", lines)


def logbins(nph):
    """Class-size histogram, log-binned: [1],[2],[3-4],[5-8],..."""
    out = []
    lo = 1
    while lo < len(nph):
        hi = min(2 * lo - 1, len(nph) - 1) if lo > 1 else 1
        cnt = int(nph[lo:hi + 1].sum())
        mass = int(sum(i * nph[i] for i in range(lo, hi + 1)))
        if cnt:
            out.append((lo, hi, cnt, mass))
        lo = hi + 1
    return out


def m1():
    lines = [
        "item-0019 m1: class-size distribution on S'_x (D0.2' world)",
        "per grid row and x (v1.1 Section 8 m1, verbatim target).",
        "sf_cls / sf_mass = singleton fraction by class count / by",
        "site mass; F2mass = sum_{Fam_2} N_P; delta_emp = F2mass/|S'|",
        "(A3's delta empirically); mwm = mass-weighted mean",
        "multiplicity sum N_P^2 / sum N_P; maxNP = largest class.",
        "B1 floor line: (ln x)^{1+eps_0} vs maxNP (candidate B1's",
        "(b1-floor), reachable iff maxNP >= (ln x)^{1+eps_0} for some",
        "eps_0 > 0, i.e. iff maxNP > ln x at least).", ""]
    hdr = (f"{'row':>9} {'x':>8} | {'|S`|':>9} {'classes':>9} "
           f"{'sf_cls':>8} {'sf_mass':>8} | {'Fam2':>6} {'F2mass':>8} "
           f"{'delta_emp':>10} | {'mwm':>8} {'maxNP':>6} {'lnx':>6}")
    lines.append(hdr)
    lines.append("-" * len(hdr))
    hists = []
    for x in C.XLADDER:
        r = jload(x)
        if not r:
            continue
        lnx = r['lnx']
        for row in rows_for(x):
            res = r['rows'].get(row)
            if not res or 'd02p' not in res:
                continue
            b = res['d02p']
            nph = np.array(b['NP_hist'], dtype=np.int64)
            ns = b['ns']
            ncls = b['nP']
            nsing = int(nph[1]) if len(nph) > 1 else 0
            maxnp = int(np.nonzero(nph)[0].max()) if nph.any() else 0
            mwm = b['cs'] / ns + 1 if ns else float('nan')
            # cs is off-diagonal: sum NP^2 = cs + ns
            lines.append(
                f"{row:>9} {x:>8.0e} | {ns:>9} {ncls:>9} "
                f"{nsing / ncls:>8.5f} {nsing / ns:>8.5f} | "
                f"{b['f2_n']:>6} {b['f2_mass']:>8} "
                f"{b['f2_mass'] / ns:>10.3e} | "
                f"{mwm:>8.5f} {maxnp:>6} {lnx:>6.2f}")
            hists.append((row, x, logbins(nph)))
        lines.append("")
    lines += ["Class-size histograms (log-binned; classes / site "
              "mass):"]
    for row, x, h in hists:
        s = "  ".join(f"[{lo}-{hi}]:{c}/{m}" if hi > lo else
                      f"[{lo}]:{c}/{m}" for lo, hi, c, m in h)
        lines.append(f"  ({row}) x={x:.0e}: {s}")
    wfile("m1_class_sizes.txt", lines)


def m2():
    lines = [
        "item-0019 m2: per-class middle concentration on Fam_2",
        "(D0.2' world; v1.1 Section 8 m2, verbatim target).",
        "REDUCED statistic red_P = (max_d N_{P,d} - 1)_+ / N_P",
        "(audit-corrected form; B2.reduced / BET-08 shape).",
        "mw_red = mass-weighted average sum (max-1) / sum N_P over",
        "Fam_2 = DIRECT finite-scale measurement of C_F(x)/ln x for",
        "RelExtensionUpper under the adversarial selection",
        "d_P = argmax_d N_{P,d} (selection identification, stated",
        "once here).  C_F = mw_red * ln x.",
        "DIAGNOSTIC column (NOT the target): unreduced mass-weighted",
        "max_d N_{P,d}/N_P.  topdec = mass share of the top-decile",
        "concentration classes (by red_P desc, stable dump order on",
        "ties): N_P-mass share of Fam_2 mass / share of the total",
        "reduced mass sum(max-1).", ""]
    hdr = (f"{'row':>9} {'x':>8} | {'Fam2':>6} {'F2mass':>8} | "
           f"{'mw_red':>9} {'C_F':>8} | {'diag_unred':>10} | "
           f"{'topdec_mass':>11} {'topdec_red':>10}")
    lines.append(hdr)
    lines.append("-" * len(hdr))
    dist = []
    for x in C.XLADDER:
        r = jload(x)
        if not r:
            continue
        lnx = r['lnx']
        for row in rows_for(x):
            res = r['rows'].get(row)
            if not res or 'd02p' not in res:
                continue
            b = res['d02p']
            if b['f2_n'] == 0:
                lines.append(f"{row:>9} {x:>8.0e} | {0:>6} -- no "
                             f"Fam_2 classes")
                continue
            J, K, D = map(int, row.split(","))
            z = zload(J, K, D, x)
            NP = z['NP'].astype(np.float64)
            red = (z['maxNPd'] - 1.0) / NP
            mw = b['f2_red_num'] / b['f2_mass']
            undiag = b['f2_max_num'] / b['f2_mass']
            ndec = max(1, math.ceil(0.1 * len(red)))
            order = np.argsort(-red, kind='stable')[:ndec]
            tmass = float(NP[order].sum()) / b['f2_mass']
            tred = (float((z['maxNPd'][order] - 1).sum())
                    / max(b['f2_red_num'], 1))
            lines.append(
                f"{row:>9} {x:>8.0e} | {b['f2_n']:>6} "
                f"{b['f2_mass']:>8} | {mw:>9.5f} {mw * lnx:>8.4f} | "
                f"{undiag:>10.5f} | {tmass:>11.4f} {tred:>10.4f}")
            h0 = float((red == 0).sum()) / len(red)
            hm0 = float(NP[red == 0].sum()) / b['f2_mass']
            hh, _ = np.histogram(red, bins=np.linspace(0, 1, 11))
            hhm, _ = np.histogram(red, bins=np.linspace(0, 1, 11),
                                  weights=NP)
            dist.append((row, x, h0, hm0, hh, hhm,
                         float(NP.sum())))
        lines.append("")
    lines += ["red_P distribution (Fam_2 classes; frac(red = 0) by",
              "class / by mass, then deciles [0,.1),[.1,.2).. by",
              "class count and by N_P mass):"]
    for row, x, h0, hm0, hh, hhm, tm in dist:
        lines.append(f"  ({row}) x={x:.0e}: red=0: {h0:.4f}/{hm0:.4f}"
                     f"  bins: " +
                     " ".join(f"{c}" for c in hh) + " | mass " +
                     " ".join(f"{m:.0f}" for m in hhm))
    wfile("m2_concentration.txt", lines)


def m4():
    lines = [
        "item-0019 m4: class-conditional tail statistics (v1.1",
        "Section 8 m4).  TWO COUNT WORLDS, separate labeled columns,",
        "never mixed (RS.4): S' = D0.2' (all three caps inside);",
        "N^w = window-cap only (both delta caps dropped).",
        "E[dtail] = mean delta_{n+L}; cap-failure rates are N^w-world",
        "fractions failing the near (delta_{n+J} > D) / far",
        "(delta_{n+L} > 2^K) caps.  eps_C = 1 - sum_{Fam_2} N_P(S') /",
        "sum_{Fam_2} N^w_P (RS.4 retention aggregated over Fam_2 =",
        "Fam_2(S'_x); C1's eps_C < 1/2 shadow).  F_fav(theta) =",
        "{P in Fam_2 : red_P <= theta} (operative 3(g) definition,",
        "DIAGNOSTIC, not a candidate).", ""]
    hdr = (f"{'row':>9} {'x':>8} | {'S`E[dt]':>8} {'F2E[dt]':>8} | "
           f"{'Nw_near':>9} {'Nw_far':>9} {'F2_near':>9} "
           f"{'F2_far':>9} | {'eps_C':>8}")
    lines.append(hdr)
    lines.append("-" * len(hdr))
    hists = []
    for x in C.XLADDER:
        r = jload(x)
        if not r:
            continue
        for row in rows_for(x):
            res = r['rows'].get(row)
            if not res or 'd02p' not in res:
                continue
            b = res['d02p']
            nw = res['nw']
            gE = b['all_tail_sum'] / b['ns'] if b['ns'] else float('nan')
            f2E = (b['f2_tail_sum'] / b['f2_mass']
                   if b['f2_mass'] else float('nan'))
            gnear = nw['capn_tot'] / nw['ns']
            gfar = nw['capf_tot'] / nw['ns']
            if b['f2_n']:
                J, K, D = map(int, row.split(","))
                z = zload(J, K, D, x)
                nwNP = float(z['nw_NP'].sum())
                fnear = float(z['nw_capn'].sum()) / nwNP
                ffar = float(z['nw_capf'].sum()) / nwNP
                epsC = 1 - b['f2_mass'] / nwNP
                lines.append(
                    f"{row:>9} {x:>8.0e} | {gE:>8.4f} {f2E:>8.4f} | "
                    f"{gnear:>9.2e} {gfar:>9.2e} {fnear:>9.2e} "
                    f"{ffar:>9.2e} | {epsC:>8.5f}")
            else:
                lines.append(
                    f"{row:>9} {x:>8.0e} | {gE:>8.4f} {'-':>8} | "
                    f"{gnear:>9.2e} {gfar:>9.2e} {'-':>9} {'-':>9} | "
                    f"{'-':>8}")
            hists.append((row, x, res))
        lines.append("")
    # F_fav-conditional block (3(e) x 3(g))
    lines += ["F_fav(theta)-conditional (N^w cap-failure rates and",
              "S' tail means over the favorable sub-family):"]
    for x in C.XLADDER:
        r = jload(x)
        if not r:
            continue
        for row in rows_for(x):
            res = r['rows'].get(row)
            if not res or res['d02p']['f2_n'] == 0:
                continue
            J, K, D = map(int, row.split(","))
            z = zload(J, K, D, x)
            NP = z['NP'].astype(np.float64)
            red = (z['maxNPd'] - 1.0) / NP
            for th in THETAS:
                m = red <= th
                if not m.any():
                    continue
                nwNP = float(z['nw_NP'][m].sum())
                s = (f"  ({row}) x={x:.0e} theta={th}: "
                     f"classes={int(m.sum())} mass={int(NP[m].sum())}"
                     f" E[dt]={float(z['tail_sum'][m].sum()) / NP[m].sum():.4f}")
                if nwNP:
                    s += (f" Nw_near={float(z['nw_capn'][m].sum()) / nwNP:.2e}"
                          f" Nw_far={float(z['nw_capf'][m].sum()) / nwNP:.2e}")
                lines.append(s)
    # tail histograms
    edges = C.TAIL_EDGES
    lab = [f"[{edges[i]:.0f},{edges[i + 1]:.0f})"
           for i in range(len(edges) - 2)] + ["overflow"]
    lines += ["", "delta_{n+L} histograms (fixed bins; counts).",
              "Worlds labeled; Fam_2 = sites in Fam_2(S') classes:"]
    for row, x, res in hists:
        for k, name in [('sp_tail_hist', "S' global"),
                        ('sp_f2_tail_hist', "S' Fam_2"),
                        ('nw_tail_hist', "N^w global"),
                        ('nw_f2_tail_hist', "N^w Fam_2")]:
            h = np.array(res.get(k, []), dtype=np.int64)
            if not h.any():
                continue
            nz = np.nonzero(h)[0]
            s = " ".join(f"{lab[i]}:{h[i]}" for i in nz)
            lines.append(f"  ({row}) x={x:.0e} {name}: {s}")
    wfile("m4_tails.txt", lines)


def d_sensitivity():
    x = 100_000_000
    r = jload(x)
    if not r:
        return
    lines = [
        "item-0019 3(a) D-sensitivity table: (4,5,D), D in",
        "{30, 44, 67}, x = 1e8, D0.2' world (feeds 3(e)/3(g)",
        "decorrelation readout r3).", "",
        f"{'D':>4} | {'|S`|':>9} {'cls':>6} {'Fam2':>6} "
        f"{'F2mass':>8} {'delta_emp':>10} | {'mw_red':>9} | "
        f"{'eps_C':>8}"]
    for D in (30, 44, 67):
        res = r['rows'].get(f"4,5,{D}")
        if not res:
            continue
        b = res['d02p']
        z = zload(4, 5, D, x)
        nwNP = float(z['nw_NP'].sum())
        lines.append(
            f"{D:>4} | {b['ns']:>9} {b['cls']:>6} {b['f2_n']:>6} "
            f"{b['f2_mass']:>8} {b['f2_mass'] / b['ns']:>10.3e} | "
            f"{b['f2_red_num'] / b['f2_mass']:>9.5f} | "
            f"{1 - b['f2_mass'] / nwNP:>8.5f}")
    wfile("d_sensitivity.txt", lines)


def readout_families():
    lines = [
        "item-0019 3(g) r2 data: favorable-family density.",
        "F_fav(theta) = {P in Fam_2 : (max_d N_{P,d} - 1)_+/N_P <=",
        "theta} (operative definition, DIAGNOSTIC, not a candidate).",
        "mass() = sum N_P (S' world).  DESCRIPTIVE fit line: least-",
        "squares c in mass(F_fav)/mass(Fam_2) ~ (ln x)^{-c} across",
        "the x ladder (DESCRIPTIVE ONLY, D3(vi): no asymptotic",
        "claim); reference marker c* = 4 ln 2 - 2 = "
        f"{CSTAR:.4f} (item-0021 family window).", "",
        f"{'row':>9} {'x':>8} {'theta':>6} | {'cls':>6} {'mass':>8} "
        f"{'m/Fam2':>8} {'m/|S`|':>10}"]
    fits = {}
    for x in C.XLADDER:
        r = jload(x)
        if not r:
            continue
        for row in rows_for(x):
            res = r['rows'].get(row)
            if not res or res['d02p']['f2_n'] == 0:
                continue
            J, K, D = map(int, row.split(","))
            z = zload(J, K, D, x)
            NP = z['NP'].astype(np.float64)
            red = (z['maxNPd'] - 1.0) / NP
            b = res['d02p']
            for th in THETAS:
                m = red <= th
                mm = float(NP[m].sum())
                lines.append(
                    f"{row:>9} {x:>8.0e} {th:>6.2f} | "
                    f"{int(m.sum()):>6} {int(mm):>8} "
                    f"{mm / b['f2_mass']:>8.5f} {mm / b['ns']:>10.3e}")
                fits.setdefault((row, th), []).append(
                    (r['lnx'], mm / b['f2_mass']))
    lines += ["", "DESCRIPTIVE (ln x)^{-c} fit of mass(F_fav)/"
              "mass(Fam_2) (rows with >= 3 ladder points and all "
              "ratios in (0,1)):"]
    for (row, th), pts in sorted(fits.items()):
        pts = [(l, v) for l, v in pts if 0 < v < 1]
        if len(pts) < 3:
            continue
        xs = np.log([l for l, _ in pts])
        ys = np.log([v for _, v in pts])
        c = -float(np.polyfit(xs, ys, 1)[0])
        lines.append(f"  ({row}) theta={th}: c_fit = {c:+.3f}   "
                     f"[c* = {CSTAR:.4f}]  DESCRIPTIVE")
    wfile("readout_families.txt", lines)


def m3():
    lines = [
        "item-0019 m3: local quotient census rho(P,d) per RS.3,",
        "even-conditioned (p = 2 factor exactly 2), exact rational",
        "discipline per kickoff 3(d) (per-pair exact over odd",
        "p <= S0; shared exact band (S0, Q]; certified one-sided",
        "tail: true rho in [rho_Q e^{-eps_Q}, rho_Q], eps_Q = 0.51",
        "k^2/Q).  Q reference = 1e6.  Census over realized classes",
        "in Fam_2 and realized middles only (RS.3 domain clause).",
        "HEURISTIC lines labeled HEURISTIC/U18.2.", ""]
    for (J, K, D) in C.GRID + [(4, 5, 44), (4, 5, 67)]:
        f = os.path.join(C.CACHE, f"m3_{J}_{K}_{D}.json")
        if not os.path.exists(f):
            continue
        r = json.load(open(f))
        k = r['k']
        lines.append(f"== row (J,K,D) = ({J},{K},{D}), k = {k}, "
                     f"S0 = {r['S0']} ==")
        lines.append(
            "  Q-stability: band factors (S0,Q] and certified tail "
            "widths:")
        for Q in ("10000", "100000", "1000000"):
            lines.append(f"    Q = {int(Q):>7}: band = "
                         f"{r['bands'][Q]:.8f}, eps_Q = "
                         f"{r['eps'][Q]:.2e}")
        b6 = r['bands']['1000000']
        stab = all(abs(r['bands'][Q] / b6 - 1) <= r['eps'][Q]
                   + r['eps']['1000000'] for Q in ('10000', '100000'))
        lines.append(f"    stability within printed interval widths: "
                     f"{'PASS' if stab else 'FAIL'}")
        hdr = (f"  {'x':>8} {'pairs':>7} {'cls':>6} | {'mean':>8} "
               f"{'mass-mean':>9} | " +
               " ".join(f"q{q:>02}" for q in [1, 5, 25, 50, 75, 95,
                                              99]))
        lines.append(hdr)
        for x, xr in sorted(r['x'].items(), key=lambda kv: int(kv[0])):
            q = xr['rho_q']
            lines.append(
                f"  {int(x):>8.0e} {xr['npairs']:>7} "
                f"{xr['nclasses']:>6} | {xr['rho_mean']:>8.4f} "
                f"{xr['rho_mean_mass']:>9.4f} | " +
                " ".join(f"{q[str(qq)] if str(qq) in q else q[qq]:>7.3f}"
                         for qq in [1, 5, 25, 50, 75, 95, 99]))
        for x, xr in sorted(r['x'].items(), key=lambda kv: int(kv[0])):
            lines.append(f"  top-10 rho at x={int(x):.0e} (word = "
                         f"prefix | d | suffix; profile p: nu_H,"
                         f"nu_pre,nu_suf; CRT-alignment diagnosis):")
            for t in xr['top10']:
                prof = " ".join(f"{p}:{v[0]},{v[1]},{v[2]}"
                                for p, v in sorted(
                                    t['profile'].items(),
                                    key=lambda kv: int(kv[0])))
                lines.append(
                    f"    rho={t['rho']:>8.3f} {t['prefix']} | "
                    f"{t['d']} | {t['suffix']} NP={t['NP']} "
                    f"NPd={t['NPd']} span={t['span']} [{prof}]")
            c = xr['corr_rho_bar']
            lines.append(
                "  correlations of per-class mass-weighted rho_bar "
                "(Pearson/Spearman):")
            for name, v in c.items():
                lines.append(f"    vs {name:>18}: {v[0]:+.3f} / "
                             f"{v[1]:+.3f}")
            v = xr['corr_red_vs_rho_dstar']
            lines.append(f"    red_P vs rho(P,d*):  {v[0]:+.3f} / "
                         f"{v[1]:+.3f}")
            dm = xr['dmean_heuristic']
            lines.append(
                f"  HEURISTIC/U18.2 d-mean line (mean over ALL even "
                f"in-window d of rho(P,d), per class; reference "
                f"value 2): mean = {dm['mean']:.4f}, quantiles " +
                " ".join(f"q{q}={v:.3f}" for q, v in dm['q'].items()))
            z = xr['midlaw_z']
            lines.append(
                f"  HEURISTIC/U18.2 middle law N_(P,d)/N_P ~ "
                f"rho e^(-d/lnx)/ln x: Poisson-normalized residuals "
                f"(obs-mu)/sqrt(mu) "
                f"mean = {z['mean']:+.3g}, sd = {z['sd']:.3g}, "
                f"quantiles " +
                " ".join(f"q{q}={v:+.3g}" for q, v in z['q'].items())
                + f"; pred >= 1 on {z['pred_ge_1']} pairs"
                + "  [z inflated by sub-1-mass cells: every realized"
                " cell has N_(P,d) >= 1 vs mu << 1 -- the e2prime"
                " 7.1(c) corner; see aggregate line]")
            ma = xr.get('midlaw_aggregate')
            if ma:
                lines.append(
                    f"  HEURISTIC/U18.2 middle-law aggregate "
                    f"calibration on realized cells: obs {ma['obs']}"
                    f" vs pred {ma['pred']:.4f} (ratio "
                    f"{ma['ratio']:.3g}; the sub-1-mass corner --"
                    f" realized-cell selection, not a law test)")
            cq = xr['collapse_q']
            lines.append(
                f"  scale-free collapse y_P = red_P ln x / "
                f"rho(P,d*): mean = {xr['collapse_mean']:.4f}, "
                f"quantiles " +
                " ".join(f"q{q}={v:.3f}" for q, v in cq.items()))
        cc = r.get('crosscheck')
        if cc:
            lines.append(
                f"  cross-check vs budget_sheet rho_exact (float, "
                f"p < 1e6): H_pre={cc['H_pre']}, d={cc['d']}, "
                f"H_suf={cc['H_suf']}: pipeline {cc['pipeline']:.6f} "
                f"vs reference {cc['budget_sheet']:.6f} (rel "
                f"{cc['rel_diff']:.1e}) "
                f"{'PASS' if cc['ok'] else 'FAIL'}")
        lines.append("")
    wfile("m3_rho_census.txt", lines)


def m5():
    f = os.path.join(C.CACHE, "m5.json")
    if not os.path.exists(f):
        return
    rs = json.load(open(f))
    lines = [
        "item-0019 m5: small-span thinning calibration (v1.1 Section",
        "8 m5; kickoff 3(f)).  ENTIRELY N^o world (RS.4, consCount",
        "semantics: anchor prime q_n in (sqrt x, x], NO caps).",
        "ANCHOR FIREWALL (item-0018 report F3): consCount's anchor",
        "q n = p[n] differs by one from anchorPrime n = p[n-1]; m5",
        "tables are NEVER joined with m1-m4 tables on a site index.",
        "Word set: lexicographically first 3 admissible all-even gap",
        "words with span <= kappa (k-1) ln(k+1) (budget printed);",
        "EMPTY = no admissible all-even word within budget (itself a",
        "datum).  ratio = N^o_consec / N^o_tuple.",
        "HEURISTIC/U18.1 line: exp(-span/ln x) Cramer thinning; no",
        "asymptotic exponent is fitted.", "",
        f"{'x':>6} {'k':>3} {'kappa':>5} {'budget':>8} "
        f"{'word':<22} {'span':>5} | {'N_consec':>9} {'N_tuple':>9} "
        f"{'ratio':>8} | {'exp(-s/ln x)':>12}"]
    for r in rs:
        if r['word'] is None:
            lines.append(
                f"{r['x']:>6.0e} {r['k']:>3} {r['kappa']:>5} "
                f"{r['budget']:>8.3f} {'EMPTY':<22}")
            continue
        w = ",".join(map(str, r['word']))
        lines.append(
            f"{r['x']:>6.0e} {r['k']:>3} {r['kappa']:>5} "
            f"{r['budget']:>8.3f} {w:<22} {r['span']:>5} | "
            f"{r['ncons']:>9} {r['ntup']:>9} {r['ratio']:>8.5f} | "
            f"{r['cramer']:>12.5f}")
    wfile("m5_thinning.txt", lines)


if __name__ == '__main__':
    which = sys.argv[1] if len(sys.argv) > 1 else 'core'
    if which == 'core':
        continuity(); smoke(); m1(); m2(); m4()
        d_sensitivity(); readout_families()
    elif which == 'm3':
        m3()
    elif which == 'm5':
        m5()
