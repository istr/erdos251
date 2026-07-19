# item-0020 W2 -- rule-15 asymptotic budget sheets for the B2.reduced
# proof campaign (runs/README rule 15; kickoff v1 Section 3 W2).
#
# Mechanical evaluation of every k- or x-dependent constant carried by
# the W1 mechanism inventory (M1-M7), at tuple rank k = (2/ln 2) lnln x
# on the grid x = 1e8, 1e20, 1e100, 1e1000, against (G1) o(ln x),
# (G2) x^eps, (G3) the pigeonhole reserve ln x / C_F (T7 pattern).
# Helper conventions and several rows are REUSED from the anchored
# item-0018 script dossier/item-0018-workpapers/budget_sheet.py
# (sha256 129b39fb..., Section 2 anchor; reuse encouraged by the
# kickoff). Exponent convention: expo(F) = ln F / lnln x.
#
# Deterministic: no timestamps, no randomness; output committed as
# budget_sheet_20_tables.txt. Exact integers/rationals where they
# decide (T4 counterexample; crossover bisection over ln x is float
# but printed to 3 significant figures with monotone verification).
# mpmath dps 40 elsewhere. Intermediate values are printed (rule-9
# capacity note: partial steering re-execution must be meaningful).

from mpmath import mp, mpf, log, exp, sqrt, loggamma

mp.dps = 40

LN2 = log(2)
SCALES = [8, 20, 100, 1000]          # x = 10^e
APRIME = mpf("1.5")                  # D0 pin A' (relext-statements D0)
APP = 48                             # D0 pin A''
EA2 = exp(1) * APRIME / 2            # capacity base constant e A'/2

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

emit("item-0020 budget sheets (rule 15) -- exponent convention:")
emit("expo(F) = ln F / lnln x, i.e. F = (ln x)^expo.  Gate (G1)")
emit("[o(ln x)] requires expo < 1 with decay or a limit < 1.")
emit("Vocabulary: W2 = C_words,off, V2 = C_sides,off, cap_r =")
emit("P3.3'(iv)-pattern simplex capacity (see W0 working notes).")
emit("")

# ---------------------------------------------------------------- #
emit("== T0. Regime lock (D0; identical to item-0018 T0) ==")
emit("x        ln x        lnln x     L=(2/ln2)lnlnx   k=L+1")
for e in SCALES:
    lnx, llx, L, k = regime(e)
    emit("1e%-5d %10.2f %9.4f %12.2f %10.2f"
         % (e, float(lnx), float(llx), float(L), float(k)))
emit("")

# ---------------------------------------------------------------- #
emit("== T1. Factor ledger incl. the MANDATORY M1 trap row ==")
emit("(kickoff W2(b): the rank-2k pair-sieve constant, tabulated so")
emit("no pair-level route imports it silently.  Reference rows from")
emit("the item-0018 T1 ledger repeated for comparison.)")
emit("")
hdr = ("factor               " + "".join(["   x=1e%-6d" % e for e in SCALES])
       + "  class / verdict vs (G1)")
emit(hdr)

def row(name, f_lnF, klass):
    vals = []
    for e in SCALES:
        lnx, llx, L, k = regime(e)
        vals.append(expo(f_lnF(lnx, llx, L, k), llx))
    emit("%-21s" % name + "".join([fmt(v, 12) for v in vals]) + "  " + klass)

row("2^k", lambda lnx, llx, L, k: k * LN2,
    "POLYLOG expo->2: FAILS (G1) [item-0018 T1]")
row("exp(k ln k)", lambda lnx, llx, L, k: k * log(k),
    "SUPERPOLYLOG: FAILS (G1) [F17.9 wall class]")
row("exp(2k ln 2k) TRAP", lambda lnx, llx, L, k: 2 * k * log(2 * k),
    "SUPERPOLYLOG, ~2x the k-rank row asymptotically (2.4-2.6x at")
emit("%-21s" % "" + " " * 48
     + "  the tabulated scales, where the O(1) term dominates the")
emit("%-21s" % "" + " " * 48
     + "  5.77 lnlnln x term): the rank-2k union-sieve")
emit("%-21s" % "" + " " * 48
     + "  constant of any pair-level sieve (M1/M6 pair routes);")
emit("%-21s" % "" + " " * 48
     + "  exceeds the (2 ln x)^1 relative room (F17.2) by")
emit("%-21s" % "" + " " * 48
     + "  (ln x)^{5.77 lnlnln x + O(1)}: DOA on every G-budget")
row("gamma_2^k (U17.11b)", lambda lnx, llx, L, k: k * log(mpf("1.150481")),
    "POLYLOG expo->0.405: PASSES (G1) alone [item-0018 T1]")
emit("")
emit("Trap-vs-room display (M1 mandatory line): ln[exp(2k ln 2k)] vs")
emit("ln[2 ln x] (the F17.2 room at M = 1):")
for e in SCALES:
    lnx, llx, L, k = regime(e)
    emit("  1e%-5d  2k ln 2k = %9.2f    ln(2 ln x) = %7.3f   ratio %8.1f"
         % (e, float(2 * k * log(2 * k)), float(log(2 * lnx)),
            float(2 * k * log(2 * k) / log(2 * lnx))))
emit("")

# ---------------------------------------------------------------- #
emit("== T2. Capacity and crossover ledger (M3 engine; A3.card and")
emit("==     the M1.a falsity both consume these rows) ==")
emit("cap_r <= ((e A'/2)(L/r) ln x)^r, e A'/2 = %.4f at the D0 pin"
     % float(EA2))
emit("(P3.3'(iv) pattern; side capacity r = J+K = L-1, full-word")
emit("capacity r = L).  Exponents expo = ln cap / lnln x, GRID")
emit("convention L = (2/ln2) lnln x (leading order):")
emit("x        expo(cap_{J+K})   expo(cap_L)   lnx-budget: ln N/lnln x")
for e in SCALES:
    lnx, llx, L, k = regime(e)
    r1 = L - 1
    c1 = r1 * log(EA2 * (L / r1) * lnx)
    c2 = L * log(EA2 * lnx)
    lnN = lnx - llx          # N >= x/ln x lower-bound convention
    emit("1e%-5d %12.2f %14.2f %16.2f"
         % (e, float(expo(c1, llx)), float(expo(c2, llx)),
            float(expo(lnN, llx))))
emit("  -> cap rows are (lnln x)-linear in expo (quasi-polylog,")
emit("     x^{o(1)}); the ln N budget row overtakes them past the")
emit("     marker crossover below (between the 1e20 and 1e100 grid")
emit("     points): the capacity argument's asymptotic regime.")
emit("")
emit("Crossover scales.  Two condition conventions, labeled exactly")
emit("[audit repair: the v1-draft mixed them and mislabeled the")
emit("continuous depth proxy as 'D0-honest']:")
emit("  (m)  scale MARKER:  8 cap <= x/ln x, leading-order depth")
emit("       L = (2/ln2) lnln x (the grid convention; NOT the proof")
emit("       condition);")
emit("  (p)  the PROOF condition of C1/C2 step (4):")
emit("       8 cap <= x/(2 C_0 ln x)  (Chebyshev floor I4), at the")
emit("       CEIL-honest D0 depths J = K = ceil(log2(ceil(13 C_0")
emit("       A'' ln x))), L = J+1+K.")
emit("Each scan verifies a single sign change over ln x in [3, 3000]")
emit("(step 0.05) and prints the first qualifying ln x:")

import math

def cap_ln(lnx, L, r):
    return r * log(EA2 * (mpf(L) / r) * lnx)

def L_grid(lnx):
    return float((2 / LN2) * log(lnx))

def L_ceil(C0):
    def f(lnx):
        D = math.ceil(13 * C0 * APP * float(lnx))
        J = math.ceil(math.log2(D))
        return 2 * J + 1
    return f

def first_crossing(Lfun, full_word, C0):
    # condition: ln 8 + cap_ln <= ln x - lnln x - [ln(2 C_0) if C0]
    prev_ok = None
    found = None
    flips = 0
    t = 3.0
    while t <= 3000.0:
        L = Lfun(t)
        r = L if full_word else L - 1
        rhs = t - math.log(t) - (math.log(2 * C0) if C0 else 0.0)
        ok = float(log(8) + cap_ln(mpf(t), L, r)) <= rhs
        if prev_ok is not None and ok != prev_ok:
            flips += 1
            if ok and found is None:
                found = t
        prev_ok = ok
        t = round(t + 0.05, 2)
    return found, flips

for tag, Lfun, fullw, C0 in [
        ("(m) A3.card side-cap, marker            ", L_grid, False, None),
        ("(m) M1.a-falsity full-cap, marker       ", L_grid, True, None),
        ("(p) A3.card side-cap, ceil D0, C_0 = 1  ", L_ceil(1), False, 1),
        ("(p) A3.card side-cap, ceil D0, C_0 = 2  ", L_ceil(2), False, 2),
        ("(p) M1.a-falsity full-cap, ceil D0, C_0=1", L_ceil(1), True, 1),
        ("(p) M1.a-falsity full-cap, ceil D0, C_0=2", L_ceil(2), True, 2),
]:
    t, flips = first_crossing(Lfun, fullw, C0)
    emit("  %s ln x ~ %7.2f  (x ~ 1e%d)  sign changes: %d"
         % (tag, t, round(t / math.log(10)), flips))
emit("  -> finite-scale honesty (D3(vi)): the marker crossings sit")
emit("     at x ~ 1e25-1e28; the PROOF-condition crossings at the")
emit("     ceil-honest D0 depths sit at x ~ 1e100-1e110 (C_0 in")
emit("     {1,2}).  NOTHING at item-0019 scales (<= 1e10) is")
emit("     claimed; the m1 measured delta_emp ~ 2.4e-3 at 1e9 sits")
emit("     far below the asymptotic delta = 1/2 and is cited as")
emit("     direction only.")
emit("")

# ---------------------------------------------------------------- #
emit("== T3. M1.a falsity sheet (W2 vs |S'|; W3 claim C2) ==")
emit("Unconditional chain: W2 >= |S'|^2/cap_L - |S'| (Cauchy-Schwarz")
emit("on full-word fibers), |S'| >= N/4 (TailIntersection at pin).")
emit("Ratio ledger; column prints ln(|S'|/cap_L) ~ ln(W2_floor/|S'|)")
emit("once |S'| >> cap_L (negative entries mean the floor is vacuous")
emit("at that scale):")
emit("x        ln(|S'|/cap_L)   i.e. factor")
for e in SCALES:
    lnx, llx, L, k = regime(e)
    v = (lnx - llx - log(4)) - cap_ln(lnx, L_grid(lnx), L_grid(lnx))
    tagv = "e^%+.0f" % float(v)
    emit("1e%-5d %12.1f      %s" % (e, float(v), tagv))
emit("  -> negative at 1e8 and 1e20 (vacuous below the T2 crossovers:")
emit("     marker x ~ 1e28, proof-condition x ~ 1e103-1e110), then")
emit("     e^{+127} at 1e100, e^{+2105} at 1e1000: W2/|S'| ->")
emit("     infinity.  The kickoff's M1 sufficient condition")
emit("     W2 = o(|S'|) is FALSE for all large x at the D0 depths.")
emit("Rule-12 landing row (kickoff W2(c)): the two additive terms in")
emit("the chain (-|S'| from the diagonal, -cap_{J+K} from |Fam| in")
emit("the A3.card step) land as ADDITIVE constants against divergent")
emit("main terms (ratios above; x^{o(1)} vs x^{1-o(1)}): no leading-")
emit("coefficient coupling anywhere in this run's chains.  Settled by")
emit("the printed ratios; no dyadic summation appears (contrast the")
emit("ANN-37 pattern rule 12 polices).")
emit("")

# ---------------------------------------------------------------- #
emit("== T4. M1.b insufficiency (statement-level counterexample; ==")
emit("==     numeric settlement, exact integers) ==")
emit("Configuration family C(t): t classes of size 2, each middle-")
emit("rigid (both members share one middle), plus ONE class of size")
emit("m = t with all middles distinct.  Exact counts:")
emit("  mass = 3t;  LHS(adversarial argmax selection) = t;")
emit("  W2 = 2t (ordered);  V2 = 2t + t(t-1).")
emit("t          W2/V2        LHS/mass   (M1.b holds at eps if")
for t in [10, 1000, 10 ** 6]:
    W2 = 2 * t
    V2 = 2 * t + t * (t - 1)
    emit("%-8d %10.6f %12.6f    W2/V2 <= eps)"
         % (t, W2 / V2, (t) / (3 * t)))
emit("  -> W2/V2 -> 0 while the reduced selection sum stays at")
emit("     mass/3: the un-normalized relative pair statement (M1.b)")
emit("     does NOT imply RelExtensionUpper.  (Abstract-configuration")
emit("     counterexample to the IMPLICATION, not a primes claim.)")
emit("     Registered F20.2; repaired by the class-normalized form")
emit("     B2.pairs, whose consumption is exact (W3 claim C3).")
emit("     Check vs B2.pairs on C(t): normalized numerator =")
emit("     t*(2/2) + (1/t)*0 = t = eps-share 1/3 of mass: B2.pairs")
emit("     correctly REFUSES this configuration (no false positive).")
emit("")

# ---------------------------------------------------------------- #
emit("== T5. B2.pairs consumption sheet (eps bookkeeping, gate ==")
emit("==     arithmetic, anti-vacuity floor, T7 reserve) ==")
emit("Reduction bookkeeping (W3 claim C3): REU-eps = sqrt(pair-eps),")
emit("i.e. x_4(eps) := x_8(eps^2).  Constants carried by the")
emit("reduction: NONE (Cauchy-Schwarz only; kickoff W2(a) row =")
emit("empty).  FIXED-DELTA gate arithmetic at the ledger value")
emit("delta = 1/2 (A3.card, s-uniform) [audit repair: one eps_C")
emit("convention]:  eps_C provenance: 7.4(s2) applies eps_C ONLY")
emit("when an A- or B-side proof detours through window-only")
emit("counts; the C1 and C3 chains count on S'^{(s)}_x throughout")
emit("(no N^w detour), so eps_C does not enter this run's chain at")
emit("all.  The pigeonhole coupling (supply_of_triple / 7.4)")
emit("consumes REU at eps = delta/4 = 1/8, so")
emit("  pair-eps = (delta/4)^2 = 1/64")
emit("closes the 7.2 pigeonhole against A3.card + TailIntersection.")
emit("(The gate SENTENCE display at the conservative consumption")
emit("eps_C < 1/2 lands in the same class, (1-eps)^2/64; the m4")
emit("measured eps_C ~ 0 is direction only and enters no constant,")
emit("D3(vi).)  Both-readings duty: measured 1e9 stratum-2")
emit("analogues: repeated-middle (W2-grain) mass share ~0.47; the")
emit("class-normalized (Q-grain, B2.pairs) analogue ~0.24 -- both")
emit("DECLINING in x, both far above the 1/64 consumption point at")
emit("reachable scales; direction only, no finite-scale closure")
emit("claim (E3).")
emit("Anti-vacuity floor (statement sanity): every class has")
emit("max_d N_{P,d} >= N_P/m_mid with m_mid = floor(A' L ln x/2)")
emit("in-window even middles, so on classes with N_P >= 2 m_mid the")
emit("adversary gets (max-1)_+ >= N_P/(2 m_mid), hence C_F >=")
emit("(1/(A'L)) * [mass share of classes with N_P >= 2 m_mid]: no")
emit("gate below C_F ~ 1/L is available; B2.reduced's forall-eps")
emit("form is consistent with this floor (eps fixed, x -> infinity).")
emit("x        1/(A'L)      vs (1-eps)/4 gate at eps=0.1")
for e in SCALES:
    lnx, llx, L, k = regime(e)
    emit("1e%-5d %10.5f %12.3f" % (e, float(1 / (APRIME * L)), 0.225))
emit("T7 reserve (item-0018 T7 pattern): C_F = O(1) or o(ln x)")
emit("leaves reserve ln x / C_F = (ln x)^{1-o(1)}: consumption")
emit("unchanged from the anchored sheet; no new sink introduced by")
emit("the reduction (sqrt is monotone: o(1) -> o(1)).")
emit("")

# ---------------------------------------------------------------- #
emit("== T6. M2 / M4 / M5 rows ==")
emit("M2(a) wall-w1 span ratio (item-0018 T5(b) pattern): exchange-")
emit("span vs the oneExtension_sum_le budget kappa (k-1) ln(k+1):")
emit("x        A'L lnx / [2(k-1)ln(k+1)]   (kappa = 2)")
for e in SCALES:
    lnx, llx, L, k = regime(e)
    emit("1e%-5d %14.1f" % (e, float(APRIME * L * lnx / (2 * (k - 1) * log(k + 1)))))
emit("  -> the span budget covers a 1/ratio = o(1) sliver of the")
emit("     window; realized side spans concentrate at Theta(L ln x)")
emit("     (P3.1' mean + m3 span data): route (e1) reaches a")
emit("     vanishing mass share.  M2(b): route (i) constant =")
emit("     exp((1+o(1)) k ln k), T1 row, DOA.  M2(c): route (ii)")
emit("     carrier NI-M2 (class-level equidistribution at growing")
emit("     rank): NOT in the corpus (checked against the Section 2")
emit("     anchor list; frozen HLQuantA has no upper content).")
emit("M4(a): the dispersion cross-term needs a word-grain upper mean")
emit("value theorem (NI-M4); available S-moment tools (D1.b anchors,")
emit("consumed verbatim): Kuperberg Thm 1.1 regime k <= (log h)^{1/2}")
emit("vs ours k = (2/ln2 + o(1)) log h -- a full square out;")
emit("Thm 1.2 box bound (3 log k)^k = superpolylog (expo ~")
emit("2.885 ln(3 ln k)); Pintz Lemma 4 upper direction needs")
emit("log H >= k^{1/eta} > k vs ours log H ~ (ln2/2) k.  All three")
emit("gaps as documented in D1.b; nothing new opens at pair level.")
emit("Against the (2 ln x)^1 relative room (F17.2): every listed")
emit("tool misses it by at least a polylog square or a superpolylog")
emit("factor.")
emit("M3(c) literature-shelf pricing (feeds the C4 barrier SCOPE):")
emit("bounded-gap / clustering inputs (Maynard-class, anchored")
emit("1311.4600) are inputs OUTSIDE the C4 tool list T (they fail")
emit("in the barrier model: all model gaps -> infinity); their")
emit("quantitative cost at growing rank is the T1 superpolylog")
emit("class (exp((1+o(1)) m ln m)-type density losses at cluster")
emit("size m ~ L): they extend T's reach only at bounded rank, not")
emit("at the D0 depths.")
emit("M5: B3 ledger price eps_B3 <= delta/4 = 1/8 at delta = 1/2")
emit("(s-uniform).  NI-M5a (alignment-mass bound at R = o(ln x)):")
emit("OPEN; m3 direction: top-decile-rho classes carry ~10% of Fam_2")
emit("mass at every populated grid point (<= 1/8: DIRECTIONALLY")
emit("compatible), but alignment level GROWS with row depth (E1/O5)")
emit("and the coupled-depth share is unmeasured: no consumption.")
emit("NI-M5b = OI-B1 (capped-domain middle law): OPEN (B1 dropped")
emit("from the measurable set by m1).")
emit("")

# ---------------------------------------------------------------- #
emit("== T7. D3(i)-(vi) matrix (kickoff W2(d); one line each, ==")
emit("==     verbatim question order) and verdicts ==")
emit("Answers for the two NEW named statements and the six mechanism")
emit("routes.  Notation: pass / FLAG / FAIL / note.")
emit("")
emit("B2.pairs (the M1.c reduced statement):")
emit(" (i)   pass -- no k-dependent constant appears in the statement")
emit("       or its consumption (Cauchy-Schwarz only).")
emit(" (ii)  note -- upper-relative shape; frozen HLQuantA (lower,")
emit("       absolute, span-gated) neither implies nor is implied by")
emit("       it; the pair-grain analogue of U18.2 is its truth")
emit("       heuristic, flagged, never load-bearing.")
emit(" (iii) pass -- all counts on S'^{(s)}_x, caps inside (RS.1).")
emit(" (iv)  pass -- no tensorization or compounding presupposed.")
emit(" (v)   pass -- statement is window-level throughout.")
emit(" (vi)  pass -- m2/m3 cited as direction only (T5 both-readings")
emit("       row); no measured number enters any constant.")
emit("A3.card (the M3.1 statement):")
emit(" (i)   pass -- constants are (e A'/2)^{J+K} capacity, polylog-")
emit("       free in the CONCLUSION (delta = 1/2 absolute).")
emit(" (ii)  pass -- consumes only proved corpus inputs (P3.3'(ii)/")
emit("       (iv), RS.1); no HL content in any direction.")
emit(" (iii) pass -- S'^{(s)}_x counts, caps inside.")
emit(" (iv)  pass.  (v) pass.  (vi) note -- crossover rows in T2:")
emit("       the statement is asymptotic; finite-scale vacuity is")
emit("       printed, never hidden.")
emit("Mechanism routes, six lines each, verbatim question order")
emit("[audit repair: the v1-draft gave first-failure lines only]:")
emit("M1.a (W2 = o(|S'|); statement FALSE by T3, verdict NO-GO):")
emit(" (i) pass (no constants)  (ii) moot (statement false)")
emit(" (iii) pass  (iv) moot  (v) moot  (vi) moot.")
emit("M1.b (W2 <= eps V2; statement open, consumer NO-GO by T4):")
emit(" (i)   pass -- no k- or x-dependent constant in the statement.")
emit(" (ii)  note -- pair-grain relative upper; no implication either")
emit("       way against frozen HLQuantA (lower, absolute), by text.")
emit(" (iii) pass -- counts on S'^{(s)}_x, caps inside.")
emit(" (iv)  pass.  (v) pass.  (vi) pass (m2 cited direction only).")
emit("M2 (relative Selberg; NO-GO(w1 + NI-M2)):")
emit(" (i)   FAIL on route (i): exp((1+o(1)) k ln k) per-word class.")
emit(" (ii)  FAIL-adjacent on route (ii): NI-M2 is beyond-HLQuantA")
emit("       upper/equidistribution content (compared by text).")
emit(" (iii) pass as stated (counts on S').  (iv) moot after (i)/(ii).")
emit(" (v) moot.  (vi) moot.")
emit("M3 (averaging engine; GO for its delivered statements):")
emit(" (i) pass  (ii) pass (consumes proved corpus inputs only)")
emit(" (iii) pass  (iv) pass  (v) pass  (vi) note (T2 crossover")
emit(" honesty rows printed; asymptotic-only).")
emit("M4 (dispersion; NO-GO(NI-M4)):")
emit(" (i)   pass at statement level (no constant yet named).")
emit(" (ii)  FAIL-adjacent: NI-M4 is strictly-beyond-HLQuantA upper")
emit("       mean-value content at rank k.")
emit(" (iii) pass.  (iv) FLAG -- a product-form reference profile")
emit("       mu_P would presuppose tensorization (U17.11(a)); any")
emit("       executed variant must state mu_P non-product or pay it.")
emit(" (v)   note -- mu_P from marginal middle laws would be a")
emit("       marginal-as-window promotion; forbidden without proof.")
emit(" (vi)  pass.")
emit("M5 (B3 on rho-capped family; CONDITIONAL(NI-M5a, NI-M5b),")
emit("DEFERRED):")
emit(" (i)   pass -- C_q(x) = R(x) = o(ln x) by the cap clause.")
emit(" (ii)  FLAG -- NI-M5b is OI-B1 (open-HL-adjacent in its sharp")
emit("       form per the B1(ii) record; the C_rel form is not);")
emit("       NI-M5a is a density statement, no HL strength.")
emit(" (iii) pass -- family rule is cap-blind ex-ante, counts on S'.")
emit(" (iv)  pass.")
emit(" (v)   note -- transferring m3's fixed-row aligned-mass shares")
emit("       to coupled depth would be marginal-as-window; that is")
emit("       exactly why NI-M5a counts as unmeasured (E1).")
emit(" (vi)  FLAG -- coupled-depth aligned-mass share unmeasured; no")
emit("       finite number may enter the eps_B3 <= 1/8 ledger check.")
emit("M6 (signed weights; NO-GO(F17.9)/merged):")
emit(" (i) FAIL at word rank (T1 rows; rank-2k trap for the pair")
emit(" variant)  (ii) moot  (iii) moot  (iv) moot  (v) moot")
emit(" (vi) moot.  Surviving variants are M2(ii)/M3 rows above.")
emit("M7 (one-extension specificity; subsumed into M1 room calculus):")
emit(" (i)-(vi): inherits M1.c's matrix for the room calculus it")
emit(" feeds and M2's (ii) for the missing carrier NI-M2; no")
emit(" separate statement exists to audit.")
emit("")
emit("== PRIORITY ORDER (W2 output; one-paragraph justifications ==")
emit("==     in the final report Section W2) ==")
emit(" 1. M3 engine: prove A3.card, the V2 floor, the M1.a falsity,")
emit("    the barrier (all sheet-clean, zero forbidden constants).")
emit(" 2. M1.c: prove the B2.pairs => RelExtensionUpper reduction")
emit("    (sheet-clean); register B2.pairs as the successor target")
emit("    with its D3 matrix.")
emit(" 3. M1.c-closure attempts on B2.pairs: union-sieve (T1 trap")
emit("    row: quantified NO-GO), identity-layer (M3.3 barrier:")
emit("    quantified NO-GO): register obstructions F20.n.")
emit(" 4. M5: record CONDITIONAL statement shape + named inputs;")
emit("    no proof investment (no in-corpus surface).")
emit(" M2, M4, M6: registered NO-GO with exact gaps; no investment.")
emit("")
emit("END OF SHEETS")

with open(__file__.replace("budget_sheet_20.py", "budget_sheet_20_tables.txt"),
          "w") as f:
    f.write("\n".join(OUT) + "\n")
