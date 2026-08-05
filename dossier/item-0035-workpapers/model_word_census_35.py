#!/usr/bin/env python3
# model_word_census_35.py -- item-0035 D2 enumeration script (dispatch
# Section 7). Enumerates the even-Cramer-smooth model gap system
#
#     q_1=2, q_2=3, q_3=5, q_4=7,
#     q_{n+1} = q_n + 2*ceil(ln(q_n)/2)   (n >= 4)
#
# up to q_n <= LIMIT (default 10**7) and censuses model flank classes
# at every rank k in {3,4,5,6} and every decomposition (J,K) with
# J+K+1 = k, J,K >= 1.
#
# EDGE-SAFE CEILING RULE (binding; kickoff Section 7): ceil(ln(q)/2)
# is decided by float log. Whenever the float value of ln(q)/2 lies
# within 1e-9 of an integer, the quantity is re-evaluated with the
# decimal module at precision >= 50 (here 60) and the ceiling is taken
# from the decimal value. For integer q >= 2, ln(q)/2 is never exactly
# an integer (e is transcendental), so the decimal branch always
# decides strictly. The number of decimal fallbacks is reported.
#
# SELF-CHECK (STOP 6 on mismatch): stretch boundaries are
# reconstructed INDEPENDENTLY of the recursion's per-q ceilings, from
# the value thresholds e^{2m}: the integer floors B_m = floor(e^{2m})
# are computed once with decimal at precision 60 (e^{2m} is
# irrational, so for integer q, q <= e^{2m} iff q <= B_m), and every
# recursion gap g_n with n >= 4 is cross-verified against the
# threshold interval: g_n = 2m must hold iff B_{m-1} < q_n <= B_m.
# Any mismatch is printed in full and the script exits nonzero.
#
# CONSISTENCY GATES (checked and reported):
#   (i)  max |mid(P)| over realized classes <= 2 for every (J,K); a
#        value >= 3 prints the full witness (V-COUNTER material) and
#        exits nonzero.
#   (ii) every class with exactly two realized middles has the
#        boundary form of the certificate's Section 5: exactly two
#        members, at consecutive sites i and i+1, both flanks
#        constant, left value w even, right value w+2, middles
#        exactly {w, w+2}, and i+J = t_w, the last index of the
#        value-w stretch. Any other shape exits nonzero (STOP 6).
#
# Deterministic: stdlib only, no network, single-threaded, no
# timestamps, no randomness, no dict-order dependence beyond
# insertion order over a fixed iteration; the emitted tables file
# model_word_census_35_tables.txt is byte-identical across runs
# (gate W6).

import math
import os
import sys
from decimal import Decimal, getcontext, ROUND_CEILING, ROUND_FLOOR

LIMIT = 10 ** 7
EDGE_EPS = 1e-9
OUT_NAME = "model_word_census_35_tables.txt"

getcontext().prec = 60

MEASURED_LINE = ("MEASURED; finite range only; no asymptotic claim "
                 "(q_n <= %d)" % LIMIT)


def ceil_half_ln(q, counters):
    """Edge-safe ceil(ln(q)/2) per the header rule."""
    x = math.log(q) / 2.0
    if abs(x - round(x)) < EDGE_EPS:
        counters["decimal_fallbacks"] += 1
        d = Decimal(q).ln() / 2
        return int(d.to_integral_value(rounding=ROUND_CEILING))
    return math.ceil(x)


def build_sequence(counters):
    q = [2, 3, 5, 7]
    while True:
        g = 2 * ceil_half_ln(q[-1], counters)
        nxt = q[-1] + g
        if nxt > LIMIT:
            break
        q.append(nxt)
    gaps = [q[i + 1] - q[i] for i in range(len(q) - 1)]
    return q, gaps


def thresholds(max_m):
    """B_m = floor(e^{2m}) for m = 0..max_m, via decimal prec 60."""
    out = {}
    for m in range(max_m + 1):
        e2m = Decimal(2 * m).exp()
        out[m] = int(e2m.to_integral_value(rounding=ROUND_FLOOR))
    return out


def self_check(q, gaps, lines):
    """Reconstruct stretch boundaries from value thresholds and
    cross-verify against the recursion's realized gap values."""
    max_m = max(gaps) // 2 + 1
    B = thresholds(max_m)
    bad = []
    for n in range(4, len(gaps) + 1):  # gap index n, 1-based
        g = gaps[n - 1]
        m = g // 2
        qn = q[n - 1]
        if not (B[m - 1] < qn <= B[m]):
            bad.append((n, qn, g, m, B[m - 1], B[m]))
    lines.append("SELF-CHECK (threshold reconstruction vs recursion):")
    lines.append("  thresholds B_m = floor(e^(2m)), m <= %d: %s"
                 % (max_m, " ".join("B_%d=%d" % (m, B[m])
                                    for m in range(max_m + 1))))
    if bad:
        lines.append("  MISMATCH (STOP 6) -- %d offending indices:" % len(bad))
        for row in bad:
            lines.append("    n=%d q_n=%d g_n=%d m=%d "
                         "expected (B_%d, B_%d] = (%d, %d]"
                         % (row[0], row[1], row[2], row[3],
                            row[3] - 1, row[3], row[4], row[5]))
        return False
    lines.append("  PASS: every gap g_n (4 <= n <= %d) satisfies "
                 "g_n = 2m with B_(m-1) < q_n <= B_m." % len(gaps))
    return True


def stretch_table(gaps, lines):
    """Maximal constant runs of the gap sequence (full sequence,
    n >= 1), with truncation flag on the last run."""
    runs = []
    start = 1
    for n in range(2, len(gaps) + 1):
        if gaps[n - 1] != gaps[start - 1]:
            runs.append((gaps[start - 1], start, n - 1))
            start = n
    runs.append((gaps[start - 1], start, len(gaps)))
    lines.append("STRETCH TABLE  [%s]" % MEASURED_LINE)
    lines.append("  value  first_n  last_n  length  note")
    for idx, (v, a, b) in enumerate(runs):
        note = ""
        if idx == len(runs) - 1:
            note = "truncated by range end"
        elif v == 1:
            note = "the named length-1 exception (g_1 = 1)"
        lines.append("  %5d  %7d  %6d  %6d  %s" % (v, a, b, b - a + 1, note))
    last_of_value = {}
    for v, a, b in runs[:-1]:
        last_of_value[v] = b
    return runs, last_of_value


def census(gaps, J, K, last_of_value, lines):
    """Census of model flank classes at decomposition (J,K).
    Returns True iff gates (i) and (ii) both pass."""
    k = J + K + 1
    n_sites = len(gaps) - k + 1
    classes = {}
    for i in range(1, n_sites + 1):
        a = tuple(gaps[i - 1:i - 1 + J])
        c = tuple(gaps[i + J:i + J + K])
        mid = gaps[i + J - 1]
        key = (a, c)
        rec = classes.get(key)
        if rec is None:
            rec = {"count": 0, "mids": {}}
            classes[key] = rec
        rec["count"] += 1
        if mid not in rec["mids"]:
            rec["mids"][mid] = [i, 0]
        rec["mids"][mid][1] += 1

    n_classes = len(classes)
    n_singleton = sum(1 for r in classes.values() if r["count"] == 1)
    two_mid = [(key, r) for key, r in classes.items()
               if len(r["mids"]) == 2]
    max_mid = max(len(r["mids"]) for r in classes.values())

    lines.append("")
    lines.append("CENSUS k=%d (J,K)=(%d,%d)  [%s]" % (k, J, K, MEASURED_LINE))
    lines.append("  sites: %d" % n_sites)
    lines.append("  realized classes: %d" % n_classes)
    lines.append("  singleton classes: %d" % n_singleton)
    lines.append("  classes with exactly two realized middles: %d"
                 % len(two_mid))
    lines.append("  max distinct realized middles over classes: %d"
                 % max_mid)

    ok = True

    # gate (i)
    if max_mid > 2:
        ok = False
        lines.append("  GATE (i) FAIL -- V-COUNTER MATERIAL, full witness:")
        for key, r in classes.items():
            if len(r["mids"]) >= 3:
                mids = sorted(r["mids"].items())
                lines.append("    (J,K)=(%d,%d) left=%s right=%s" %
                             (J, K, key[0], key[1]))
                for mv, (site, cnt) in mids:
                    lines.append("      middle %d at site %d (count %d)"
                                 % (mv, site, cnt))
    else:
        lines.append("  gate (i) PASS: max distinct middles <= 2")

    # gate (ii) + listing
    for key, r in sorted(two_mid, key=lambda kv: min(
            s for s, _ in kv[1]["mids"].values())):
        a, c = key
        mids = sorted(r["mids"].items())
        (m1, (s1, c1)), (m2, (s2, c2)) = mids
        w = a[0] if a else None
        boundary = None
        shape_ok = (
            r["count"] == 2 and c1 == 1 and c2 == 1
            and len(set(a)) == 1 and len(set(c)) == 1
            and a[0] % 2 == 0 and c[0] == a[0] + 2
            and (m1, m2) == (a[0], a[0] + 2)
            and s2 == s1 + 1
            and last_of_value.get(a[0]) == s1 + J
        )
        if a and len(set(a)) == 1:
            boundary = "%d->%d at n=%d" % (a[0], a[0] + 2,
                                           (last_of_value.get(a[0], -1)))
        lines.append("    two-middle class: left=%s right=%s boundary=%s"
                     % (list(a), list(c), boundary))
        lines.append("      middles {%d, %d}; witnessing sites i1=%d "
                     "(middle %d), i2=%d (middle %d); members=%d"
                     % (m1, m2, s1, m1, s2, m2, r["count"]))
        if not shape_ok:
            ok = False
            lines.append("      GATE (ii) FAIL (STOP 6): class does not "
                         "have the Section 5 boundary form")
    if ok and two_mid:
        lines.append("  gate (ii) PASS: every two-middle class has the "
                     "boundary form (2 members, consecutive sites, "
                     "constant flanks w / w+2, middles {w, w+2}, "
                     "i1+J = last index of the value-w stretch)")
    elif ok:
        lines.append("  gate (ii) PASS (vacuous: no two-middle class)")
    return ok


def main():
    counters = {"decimal_fallbacks": 0}
    lines = []
    lines.append("model_word_census_35_tables.txt -- item-0035 D2 output")
    lines.append("script: model_word_census_35.py (deterministic, stdlib "
                 "only, single-threaded, no network)")
    lines.append("model: q_1=2, q_2=3, q_3=5, q_4=7; "
                 "q_(n+1) = q_n + 2*ceil(ln(q_n)/2) for n >= 4")
    lines.append("range: q_n <= %d" % LIMIT)
    lines.append("EVERY TABLE IN THIS FILE IS %s" % MEASURED_LINE)
    lines.append("")

    q, gaps = build_sequence(counters)
    lines.append("sequence: %d terms q_n, %d gaps g_n; q_1=%d, q_2=%d, "
                 "q_3=%d, q_4=%d, q_5=%d; last q=%d; max gap=%d"
                 % (len(q), len(gaps), q[0], q[1], q[2], q[3], q[4],
                    q[-1], max(gaps)))
    lines.append("initial gaps g_1..g_8: %s" % gaps[:8])
    lines.append("decimal fallbacks triggered (edge-safe ceiling rule): %d"
                 % counters["decimal_fallbacks"])
    lines.append("")

    ok = self_check(q, gaps, lines)
    lines.append("")
    _, last_of_value = stretch_table(gaps, lines)

    all_gates = ok
    for k in (3, 4, 5, 6):
        for J in range(1, k - 1):
            K = k - 1 - J
            g_ok = census(gaps, J, K, last_of_value, lines)
            all_gates = all_gates and g_ok

    lines.append("")
    if all_gates:
        lines.append("ALL GATES PASS (self-check, gate (i), gate (ii) "
                     "over every (J,K)).")
    else:
        lines.append("GATE FAILURE PRESENT -- see lines above "
                     "(STOP 6 / V-COUNTER material).")
    lines.append("[%s]" % MEASURED_LINE)

    out_path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                            OUT_NAME)
    with open(out_path, "w") as fh:
        fh.write("\n".join(lines) + "\n")
    sys.stdout.write("\n".join(lines[-3:]) + "\n")
    return 0 if all_gates else 1


if __name__ == "__main__":
    sys.exit(main())
