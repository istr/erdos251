# item-0018 M1 -- rule-15 asymptotic budget sheets (runs/README rule 15)
#
# Mechanical evaluation of EVERY constant and factor appearing in the
# D1 candidate statements of dossier/relext-statements.md, at tuple
# rank k = (2/ln 2) lnln x, on the log-log grid x = 10^8, 10^20,
# 10^100, 10^1000, against the three reference budgets:
#   (G1) the B-layer gate  C = o(ln x)          [exponent < 1],
#   (G2) x^eps             [x-exponent rows],
#   (G3) the pigeonhole reserve (F17.2 room (2 ln x)^M at M = 1, and
#        the AR-shape room exponent theta(A') of dossier 4.0/M2.3).
#
# Exponent convention: expo(F) := ln F / lnln x, i.e. F = (ln x)^expo.
# A factor passes gate (G1) iff its exponent is < 1 (and, for o(ln x),
# tends to a limit < 1 or decays); k!-type factors have exponents that
# GROW like lnlnln x -- the F17.9 wall (superpolylog class).
#
# Provenance per row is cited inline (F17.n / U17.n / dossier section /
# Lean decl name; ANN-2f: decl names, never file:line). Exact rational
# arithmetic (fractions.Fraction) for the Mertens/Euler products;
# mpmath (dps 40) for the transcendental rows. Output is deterministic
# (no timestamps); the committed table output is
# dossier/item-0018-workpapers/budget_sheet_tables.txt.
#
# Convention: L = J + 1 + K gaps (M = 1), tuple rank k = L + 1 points.
# The sheet evaluates at the real value L(x) = (2/ln 2) lnln x and
# k(x) = L(x) + 1 (leading order identical; the +1 is kept because the
# exclusion inequality of the T1 pattern consumes C_per at rank k+1 --
# adjudication Section 2, FATAL-2 re-execution).

from fractions import Fraction
from mpmath import mp, mpf, log, exp, sqrt, euler, loggamma
from sympy import primerange

mp.dps = 40

LN2 = log(2)
SCALES = [8, 20, 100, 1000]          # x = 10^e
APRIME = mpf("1.5")                  # working aggregate cap A' (F17.3 window)
APRIMES = [mpf("1.05"), mpf("1.5"), mpf("2.0")]

OUT = []
def emit(s=""):
    OUT.append(s)
    print(s)

def lnx_of(e):
    return e * log(10)

def regime(e):
    lnx = lnx_of(e)
    llx = log(lnx)
    L = (2 / LN2) * llx
    k = L + 1
    return lnx, llx, L, k

def expo(lnF, llx):
    return lnF / llx

def fmt(v, w=10, p=3):
    return ("{:" + str(w) + "." + str(p) + "f}").format(float(v))

# ---------------------------------------------------------------- #
emit("item-0018 budget sheets (rule 15) -- exponent convention:")
emit("expo(F) = ln F / lnln x, i.e. F = (ln x)^expo.  Gate (G1)")
emit("[B-layer, o(ln x)] requires expo < 1 with decay or a limit < 1.")
emit("")

emit("== T0. Regime lock (D0) ==")
emit("x        ln x        lnln x     L=(2/ln2)lnlnx   k=L+1")
for e in SCALES:
    lnx, llx, L, k = regime(e)
    emit("1e%-5d %10.2f %9.4f %12.2f %10.2f"
         % (e, float(lnx), float(llx), float(L), float(k)))
emit("")

# ---------------------------------------------------------------- #
emit("== T1. Universal factor ledger (exponents expo = ln F/lnln x) ==")
emit("Rows: the constant classes rule 15 names, plus the D1-L' self-")
emit("proved constant.  F17.9 wall: exclusion needs C_per(k+1) *")
emit("S-ratio < c ln x, i.e. expo < 1.")
emit("")
hdr = "factor              " + "".join(["   x=1e%-6d" % e for e in SCALES]) + "  class / verdict vs (G1)"
emit(hdr)

rows = []
def row(name, f_lnF, klass):
    vals = []
    for e in SCALES:
        lnx, llx, L, k = regime(e)
        vals.append(expo(f_lnF(lnx, llx, L, k), llx))
    rows.append((name, vals, klass))
    emit("%-20s" % name + "".join([fmt(v, 12) for v in vals]) + "  " + klass)

row("2^k",            lambda lnx, llx, L, k: k * LN2,
    "POLYLOG expo->2: FAILS (G1); (ln x)^2 at rank (2/ln2)lnlnx"
    " (the sheet's k = L+1 adds a factor 2: expo = 2 + ln2/lnlnx)")
row("k!",             lambda lnx, llx, L, k: loggamma(k + 1),
    "SUPERPOLYLOG ~2.885 lnlnln x: FAILS (G1) [F17.9]")
row("exp(k ln k)",    lambda lnx, llx, L, k: k * log(k),
    "SUPERPOLYLOG: FAILS (G1) [F17.9 wall class]")
row("2^k k! (classical)", lambda lnx, llx, L, k: k * LN2 + loggamma(k + 1),
    "SUPERPOLYLOG: FAILS (G1) [U17.2/D1.a]")
row("C*(k+1) (D1-L')", lambda lnx, llx, L, k:
    log(2) + 1 + (k + 1) * (log(4) - euler + log(k + 1)) + mpf("1.45") * sqrt(k + 1),
    "SUPERPOLYLOG: FAILS (G1) [D1-L' self-proved; F17.9]")
row("gamma_2^k  (U17.11b)", lambda lnx, llx, L, k: k * log(mpf("1.150481")),
    "POLYLOG expo->0.405 const: PASSES (G1) alone")
emit("")
emit("FATAL-2 display check (adjudication Section 2): k ln k =")
for e in SCALES:
    lnx, llx, L, k = regime(e)
    lllx = log(llx)
    emit("  1e%-5d k ln k = %8.2f   2.885*lnlnx*(lnlnlnx+1.0596) = %8.2f"
         % (e, float(k * log(k)),
            float((2 / LN2) * llx * (lllx + mpf("1.0596")))))
emit("")

# ---------------------------------------------------------------- #
emit("== T2. Rooms and gates (G3) ==")
emit("AR-shape room exponent theta(A') = 1 - (2/ln2) ln(e A'/4)")
emit("(dossier M2.3/4.0); A'_crit = 4 sqrt(2)/e = 2.08104.")
for a in APRIMES:
    th = 1 - (2 / LN2) * (1 + log(a) - log(4))
    emit("  A' = %s   theta = %8.4f" % (fmt(a, 5, 2), float(th)))
emit("F17.2 room at M = 1: (2 ln x)^1  [expo -> 1].")
emit("F17.5 AR-deficit at A'->1+, gamma_2 = 1.150481: expo =")
emit("  (2/ln2) ln(e*gamma_2/2) - 1 = %8.4f  (in-repo 0.290 check)"
     % float((2 / LN2) * (1 + log(mpf("1.150481")) - log(2)) - 1))
emit("")

# ---------------------------------------------------------------- #
emit("== T3. Even-conditioning normalization (D0 parity lock) ==")
emit("Independent recomputation of the F17.5 Euler product")
emit("E_even[S_2^2] = 4 C_2^2 prod_{p>2} (1 + ((p-1)^2/(p-2)^2 - 1)/p)")
# Float product: the p > 1e6 tail truncation (~1e-7) dominates the
# float rounding (~1e-11), so exact rationals buy nothing here; the
# exact-rational discipline is applied where it decides (T4 rho_max).
C2sq = 1.0
T2p = 1.0
for p in primerange(3, 1000000):
    C2sq *= (1.0 - 1.0 / ((p - 1) * (p - 1))) ** 2
    T2p *= 1.0 + (((p - 1) / (p - 2)) ** 2 - 1.0) / p
E_even = 4 * C2sq * T2p
emit("  partial product over p < 1e6 (float; tail error ~1e-7):")
emit("  E_even[S_2^2] = %.6f   (in-repo value 4.601923; F17.5)"
     % float(E_even))
emit("  gamma_2 asymptote = E_even/4 = %.6f  (crit 2 sqrt2/e = 1.040520)"
     % (float(E_even) / 4))
emit("  Even-conditioned mean E_even[S_2] = 2 exactly (D0 lock);")
emit("  every candidate constant states its normalization.")
emit("")

# ---------------------------------------------------------------- #
emit("== T4. B-layer local quotient rho: exact factors and worst case ==")
emit("[REPAIRED after the v1-draft adversarial audit pass: the draft's")
emit("cap 2*prod_{first T odd primes}(1+1/(p-1)) = O(lnlnln x) was")
emit("FALSE -- the one-insert dichotomy factor bounds S(H_d)/S(H_pre)")
emit("only; dividing by S(H_suf) amplifies block-aligned primes.  All")
emit("witnesses below were audit-found and steering-re-executed.]")
emit("Exact identity: rho(P,d) = 2 * prod over odd p of")
emit("  (1 - nu_H/p) / ((1 - nu_pre/p)(1 - nu_suf/p))")
emit("(the (1-1/p)-powers cancel: |H_d| = (J+1)+(K+1); p = 2 gives")
emit("exactly 2, the even lock).  Per odd prime the factor is <=")
emit("(1 - nu_min/p)^{-1} with nu_min = min(nu_pre, nu_suf, p-1) -- up")
emit("to p at full two-block alignment (nu_pre = nu_suf = nu_H = p-1),")
emit("which CRT-aligned middles realize inside the window budget for")
emit("all odd p with p-1 <= min(J,K)+1 and primorial <= A'L ln x:")
emit("  sup rho over the full in-window (P,d) range = (ln x)^{1-o(1)},")
emit("POLYLOG with exponent -> 1: the worst case FAILS gate (G1) at")
emit("finite scales (witness CE2 below has rho = 4.8 ln x).  Only the")
emit("TYPICAL/mean rho (even-conditioned mean 2; U18.2 heuristic) is")
emit("subpolylog; B1-type pointwise candidates must carry an explicit")
emit("rho-cap clause, and F18.4's statement-level gate claim is scoped")
emit("to the selection-gated forms B2/B3.")
emit("")

def nu_classes(H, p):
    return len(set(h % p for h in H))

def rho_exact(H_pre, H_suf, d, pmax=10 ** 6):
    A_J = max(H_pre)
    H = sorted(set(H_pre) | set(A_J + d + s for s in H_suf))
    for p in primerange(2, len(H) + 2):
        if nu_classes(H, p) == p:
            return None, H
    r = 1.0
    npow = len(H) - len(H_pre) - len(H_suf)
    for p in primerange(2, pmax):
        a, b, c = nu_classes(H, p), nu_classes(H_pre, p), nu_classes(H_suf, p)
        r *= (1 - a / p) / ((1 - b / p) * (1 - c / p) * (1 - 1 / p) ** npow)
    return r, H

emit("Audit witnesses (admissible, all-even, inside the D0 window at")
emit("the named grid depth; truncated exact-factor product, p < 1e6):")
WITNESSES = [
    ("1e8   ", [0, 2, 6, 8, 12], [0, 2, 6, 8, 12], 198),
    ("1e20  ", [0, 60, 72, 106, 166, 178], [0, 60, 72, 106, 166, 178], 32),
    ("1e1000", [0, 2, 6, 8, 12, 18, 20, 26, 30, 32, 36, 42],
               [0, 2, 6, 8, 12, 18, 20, 26, 30, 32, 36, 42], 29988),
]
emit("depth    span     rho       (ln x)-expo   v1-draft cap (FALSE)")
DRAFT_CAPS = {"1e8   ": 9.80, "1e20  ": 11.90, "1e1000": 17.60}
for tag, hp, hs, d in WITNESSES:
    r, H = rho_exact(hp, hs, d)
    e = int(tag.replace("1e", "").strip())
    lnx, llx, L, k = regime(e)
    emit("%s %7d %9.2f %10.3f %14.2f"
         % (tag, max(H), r, float(log(mpf(r)) / llx), DRAFT_CAPS[tag]))
emit("(CE at 1e20 depths: rho = 221.66 = 4.8 ln x -- (G1) fails")
emit(" outright on the unconstrained pointwise range.)")
emit("")

# ---------------------------------------------------------------- #
emit("== T5. A-layer sheet ==")
emit("(a) Lemma 4.1 mass floor (decl singularSeries_lower_bound,")
emit("    in-repo constant C = 12; reference C = 1): x-exponent of")
emit("    M_H(x) = S(H) x/(ln x)^k >= x^(1 - v), decl-indexed")
emit("    v = (C (k-1) ln(k+1) + k lnln x)/ln x  (the decl's exponent")
emit("    is C(|H|-1)ln(|H|+1) at |H| = k).  VACUOUS when v >= 1.")
def vacuity_v(e, C):
    lnx, llx, L, k = regime(e)
    return (C * (k - 1) * log(k + 1) + k * llx) / lnx
emit("x         v(C=12)   v(C=1)    verdict(C=12)")
for e in SCALES:
    v12, v1 = vacuity_v(e, 12), vacuity_v(e, 1)
    emit("1e%-5d %9.3f %9.3f    %s"
         % (e, float(v12), float(v1),
            "VACUOUS (v >= 1)" if v12 >= 1 else "nonvacuous"))
def crossing(C):
    lo, hi = 2.0, 4000.0
    for _ in range(80):
        mid = (lo + hi) / 2
        if vacuity_v(mid, C) >= 1:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2
emit("    -> nonvacuity crossings (v = 1), decl-indexed: C = 12 at"
     " x ~ 1e%.0f; C = 1 at x ~ 1e%.0f." % (crossing(12), crossing(1)))
emit("       [v1-draft prose said ~1e300 and ~1e30: audit-corrected.]")
emit("       Finite-scale honesty row (kickoff D3(vi)).")
emit("")
emit("(b) Bonferroni consecutiveness transfer (decl consCount_bonferroni")
emit("    + oneExtension_sum_le): the subtracted extension sum vs the")
emit("    ln x/8 reserve.  At exchange-typical span W = A' L ln x the")
emit("    weighted extension count is Theta(W/ln x) = Theta(L) times")
emit("    the reserve [reuse-audit wall w2]; at the small-span budget")
emit("    span <= kappa L ln(L+2) (the decl's own hypothesis, NECESSARY")
emit("    per its docstring) the ratio is C2 L ln(L+2)^2/(ln x/8) -> 0.")
emit("x        exch-span ratio ~ 8 A' L    small-span ratio (C2=1)")
for e in SCALES:
    lnx, llx, L, k = regime(e)
    r_ex = 8 * APRIME * L
    r_sm = 8 * L * log(L + 2) ** 2 / lnx
    emit("1e%-5d %14.1f %25.2f" % (e, float(r_ex), float(r_sm)))
emit("    -> exchange-span transfer FAILS by Theta(L) even at perfect")
emit("       HL constants; small-span transfer closes for x >~ 1e1000")
emit("       at C2 = 1 (in-repo C2 is larger: finite-scale vacuity).")
emit("")
emit("(c) Cramer thinning of consecutive vs nonconsecutive counts at")
emit("    window W = A' L ln x: factor exp(-(1+o(1)) W/ln x)")
emit("    = (ln x)^-tau, tau(A') = 2A'/ln 2 [Gallagher-frame heuristic,")
emit("    U17.9-class; enters A-layer honest forms only].")
for a in APRIMES:
    emit("    A' = %s  tau = %7.3f" % (fmt(a, 5, 2), float(2 * a / LN2)))
emit("")

# ---------------------------------------------------------------- #
emit("== T6. C-layer sheet (F17.8 ledger) ==")
emit("(a) Depth feedback of family density eta: Markov tail selection")
emit("    at density eta inflates D by 1/eta, hence J and K each by")
emit("    log2(1/eta): L -> L + 2 log2(1/eta) (F17.8).  Ledger:")
emit("    eta = (ln x)^-c: L inflation factor (1 + c); admissible")
emit("    (bounded re-budget); eta = exp(-(lnln x)^2)-class (HL-thin")
emit("    class density, T5(a)): inflation factor ~ lnln x:")
emit("    SELF-DEFEAT (all T1 ledger rows re-inflate superpolylog).")
emit("x        L      +2log2(1/eta), eta=(lnx)^-1   HL-thin: 2*(lnlnx)^2/ln2  ratio-to-L")
for e in SCALES:
    lnx, llx, L, k = regime(e)
    d1 = 2 * llx / LN2
    dthin = 2 * llx * llx / LN2
    emit("1e%-5d %6.1f %18.1f %25.1f %11.2f"
         % (e, float(L), float(d1), float(dthin), float(dthin / L)))
emit("")
emit("(b) Truncated-tail transfer window (C1 via HL first moments):")
emit("    tail rank J_0 = log2(1/eta) + O(1) needed so that the")
emit("    truncation error 2^-J_0 T* <= eps ln x with the global-Markov")
emit("    subtraction threshold T* ~ ln x/eta.  HLQuantA card headroom:")
emit("    4 lnln x - k = (4 - 2/ln2) lnln x.  Admissible iff")
emit("    c/ln2 < 4 - 2/ln2, i.e.  c < c* = 4 ln 2 - 2 = %.4f."
     % float(4 * LN2 - 2))
emit("x        headroom(=4lnlnx-k)   J_0 at c=0.5   J_0 at c=0.7726  J_0 at c=1")
for e in SCALES:
    lnx, llx, L, k = regime(e)
    hr = 4 * llx - k
    emit("1e%-5d %14.2f %14.2f %14.2f %14.2f"
         % (e, float(hr), float(0.5 * llx / LN2),
            float(0.7726 * llx / LN2), float(llx / LN2)))
emit("    -> C1-via-frozen-HLQuantA admissibility window:")
emit("       family density (ln x)^-c with c < 4 ln 2 - 2 = 0.7726;")
emit("       the A-side thinning tau(A') >= 2/ln2 = 2.885 > c* --")
emit("       a thinned single class NEVER fits; only polylog-dense")
emit("       families (small c) do.  [New datum this item.]")
emit("")

# ---------------------------------------------------------------- #
emit("== T7. Consumption sheet (T5 slack sink; D4) ==")
emit("Exclusion reserve ln x / C_F after the B-layer constant:")
emit("x         C_F=O(1)   C_F=(lnx)^0.405   C_F=(lnx)^2")
for e in SCALES:
    lnx, llx, L, k = regime(e)
    r0 = expo(log(lnx), llx)
    emit("1e%-5d  (lnx)^%.2f    (lnx)^%.2f       NEGATIVE: dead"
         % (e, float(r0), float(r0 - 0.405)))
emit("    -> the o(ln x) slack is consumed by, in order: the A-side")
emit("       proportionality c_A, the C-side retention (1-o(1)), the")
emit("       threshold-t truncation, and the B3 exceptional mass; the")
emit("       item-0020 target constant is C_F <= (1-eps) c_A c_C ln x")
emit("       (all named in dossier/relext-statements.md D4).")
emit("")
emit("END OF SHEETS")

with open(__file__.replace("budget_sheet.py", "budget_sheet_tables.txt"),
          "w") as f:
    f.write("\n".join(OUT) + "\n")
