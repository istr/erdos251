# item-0010 W4 -- separator re-pricing extension to the item-0020
# rule-15 budget sheet (runs/README rule 15; item-0010 kickoff v2 W4).
#
# This is the "budget_sheet_20.py extension" of the kickoff Section 8
# output list.  It is a NEW, self-contained script: the anchored sheet
# dossier/item-0020-workpapers/budget_sheet_20.py (Section 2 anchor,
# sha256 bbce2f583f0a1f158b7fc5f13ca120b5388be642c585bbbdac5e6be5c5558b0d)
# is READ-ONLY for this session, so its conventions are RE-DECLARED here
# (never imported: importing would re-execute it and overwrite the
# anchored budget_sheet_20_tables.txt).  Every convention below is
# byte-faithful to the anchor: LN2, SCALES, APRIME, EA2 = e A'/2,
# regime(), expo(), cap_ln().  New tables T8-T11 re-price the three
# separator families of proofs.md Claim C4 SCOPE against the WEAKER
# endpoints CG (collision-gap-audit.md C.4 / ANN-20260722-58) and
# ExAnteWeightedMiddleContractionAlongScales (ANN-20260723-59), at the
# same evaluation rank k = (2/ln 2 + o(1)) lnln x, against the same
# three budgets (G1) o(ln x), (G2) x^eps, (G3) pigeonhole reserve.
#
# Deterministic: no timestamps, no randomness; output committed as
# budget_sheet_20_ext_tables.txt.  mpmath dps 40; loggamma for the
# proved binomial cap C(M,r).  Intermediate values printed (rule-9).

from mpmath import mp, mpf, log, exp, loggamma
import math

mp.dps = 40

LN2 = log(2)
SCALES = [8, 20, 100, 1000]          # x = 10^e  (anchor grid)
APRIME = mpf("1.5")                  # D0 pin A' (relext-statements D0)
APP = 48                             # D0 pin A''
EA2 = exp(1) * APRIME / 2            # capacity base constant e A'/2 = 3e/4
C0 = 2 / log(3)                      # Chebyshev constant sup q_n/(n ln(n+2))
#                                      = 2/ln3 attained at q_1 = 2 (proofs.md C4)

OUT = []
def emit(s=""):
    OUT.append(s)
    print(s)

def lnx_of(e):
    return e * log(10)

def regime(e):
    # DISCLOSURE (B7 / anchor budget_sheet_20.py (m)/(p) split): L below is
    # the GRID surrogate L = (2/ln2) lnln x (leading order; anchor tag (m),
    # "the grid convention; NOT the proof condition").  The D0-EXACT proof
    # depth is L = 2J+1, J = ceil(log2(ceil(13 C_0 A'' ln x))) (anchor tag
    # (p), shipped there as L_ceil()).  Exact L exceeds grid L by ~3.7x
    # (1e8) .. ~2.0x (1e1000).  This sheet DISCLOSES the surrogate; it does
    # NOT switch to L_ceil (deferred).  T10's depths() already runs exact.
    lnx = lnx_of(e)
    llx = log(lnx)
    L = (2 / LN2) * llx
    k = L + 1
    return lnx, llx, L, k

def expo(lnF, llx):
    return lnF / llx

def cap_ln(lnx, L, r):
    # displayed simplex capacity ln((e A'/2)(L/r) ln x)^r  (anchor T2)
    return r * log(EA2 * (mpf(L) / r) * lnx)

def fmt(v, w=12, p=3):
    return ("{:" + str(w) + "." + str(p) + "f}").format(float(v))

emit("item-0010 W4 separator re-pricing -- extension of the anchored")
emit("item-0020 budget sheet (conventions re-declared, anchor read-only).")
emit("Exponent convention (anchor): expo(F) = ln F / lnln x, F = (ln x)^expo.")
emit("Gate (G1) o(ln x): expo < 1 with decay or a limit < 1.  (G2) x^eps:")
emit("ln F = o(ln x).  (G3) pigeonhole reserve: ln x / C_F must survive.")
emit("Evaluation rank k = L+1 = (2/ln 2 + o(1)) lnln x.  A' = 1.5, A'' = 48,")
emit("C_0 = 2/ln 3 = %.6f.  EA2 = e A'/2 = %.6f." % (float(C0), float(EA2)))
emit("")
emit("L-CONVENTION (disclosure, B7; anchor budget_sheet_20.py (m)/(p) split):")
emit("L is the GRID surrogate L = (2/ln2) lnln x (anchor tag (m): 'the grid")
emit("convention; NOT the proof condition').  The D0-EXACT proof depth is")
emit("L = 2J+1, J = ceil(log2(ceil(13 C_0 A'' ln x))) (anchor tag (p),")
emit("shipped as L_ceil).  Grid vs exact L on the grid (surrogate factor):")
for e in SCALES:
    lnx = float(lnx_of(e))
    Dex = math.ceil(13 * float(C0) * APP * lnx)
    Jex = math.ceil(math.log2(Dex))
    Lex = 2 * Jex + 1
    Lgd = float((2 / LN2) * log(lnx))
    emit("  1e%-5d grid L = %6.2f   exact L = 2J+1 = %3d   factor %.2f"
         % (e, Lgd, Lex, Lex / Lgd))
emit("Blocks pricing on grid L: T9.S3 (m=L, cost L ln L) and T9.S2 (k_req =")
emit("grid L, window h = A' L ln x).  T10 uses the ceil-honest depths()")
emit("(exact).  This pass DISCLOSES only; it does NOT switch to L_ceil")
emit("(deferred to a later dispatch).")
emit("")

# ---------------------------------------------------------------- #
emit("== T8. Endpoint demand ledger (the three endpoints; strength /")
emit("==     uniformity / scale-density triple that SUFFICES) ==")
emit("Downstream pigeonhole (7.2) closes at eps_REU = delta/4 = 1/8 with")
emit("delta = 1/2 (A3.card, PROVED).  The pair coefficient c := Q/N-share.")
emit("")
emit(" endpoint        strength (on Q/N)     uniformity-in-s   scale-density")
emit(" --------------  -------------------   ---------------   -------------")
emit(" B2.pairs        c -> 0 (any eps>0);   one x_8(eps),     all large x")
emit("  (baseline)     minimal that feeds    UNIFORM in s      (eventual)")
emit("                 pigeonhole: c<1/16    (s inside x)")
emit("                 (=(delta/2)^2), slack")
emit("                 c=1/64=(delta/4)^2")
emit(" CG              c<1 fixed (eta_s=1-c   NONE (eta_s may   SPARSE: one")
emit("  (weakest)      >0); constant-order,   depend on s)      favorable x")
emit("                 NOT c->0                                 per X, per s")
emit("                                                          (liminf<1)")
emit(" Contraction     per-class N_Pd <=      NONE (eta_s per   SPARSE:")
emit("  (=>CG)         (1-kappa_P)N_P+1 on    fixed s)          unbounded")
emit("                 ex-ante G, + saving                      scales per s")
emit("                 sum kappa_P N_P>=eta_s N")
emit("")
emit("Demand order (weakest -> strongest): CG < Contraction < B2.pairs.")
emit("CG does NOT consume: any s-uniform constant; any all-large-x claim;")
emit("any global x-threshold; eps->0; MatchedFlankLower or RelExtensionUpper")
emit("at integration time.  Contraction additionally does NOT consume the")
emit("rho cap R = o(log x) (ANN-59: old proof device, not a logical")
emit("requirement).  BOTH CG-routes DO consume item-0020's F/N -> 0 (SF).")
emit("")

# ---------------------------------------------------------------- #
emit("== T9. Separator re-pricing against CG (and Contraction). ==")
emit("Question W4: does relaxing B2.pairs -> CG (drop eps->0, drop")
emit("s-uniformity, drop all-large-x) reduce ANY separator's cost?")
emit("Principle: a cost that depends on the tuple RANK m (set by the D0")
emit("exchange geometry) is INVARIANT under the relaxation; only a cost")
emit("that depends on strength/uniformity/scale-density can drop.")
emit("")
emit("-- T9.S3  Maynard-class bounded-gap input (anchored 1311.4600). --")
emit("Fails in the barrier model (all model gaps -> infinity): genuine")
emit("separator.  Cost to realize a SPECIFIED length-(L-1) matched-flank")
emit("word twice with distinct middles = cluster/density loss at cluster")
emit("size m ~ L: exp((1+o(1)) m ln m) (T6 M3(c); T1 class).  Rank m ~ L")
emit("is D0-FORCED, independent of the endpoint's strength.")
emit("[B7: m=L below is the GRID surrogate L; the D0-exact rank m ~ 2J+1")
emit(" is larger (factor ~3.7x..2.0x), so this understates the superpolylog")
emit(" cost -- the STILL-BINDING verdict is unaffected.]")
emit("x        m=L        expo[exp(m ln m)]   vs (G1)/(G2)")
for e in SCALES:
    lnx, llx, L, k = regime(e)
    cost = L * log(L)
    emit("1e%-5d %10.3f %14.3f        SUPERPOLYLOG: FAILS (G1); PASSES (G2): cost x^{o(1)}"
         % (e, float(L), float(expo(cost, llx))))
emit("  -> ln F = L ln L ~ 2.885 lnln x . lnlnln x = o(ln x): the cost is")
emit("     x^{o(1)}, so it PASSES (G2) x^eps; it FAILS only the tight budget")
emit("     (G1) superpolylog-in-(ln x).  Non-survival rests on (G1) / the")
emit("     D0-forced unbounded rank m ~ L, NOT on (G2).")
emit("  -> same superpolylog class as the anchor T1 exp(k ln k) row")
emit("     (expo ~ 2.885 lnlnln x).  Bounded-rank Maynard (fixed m) is")
emit("     affordable but CANNOT realize a growing-length flank word, so")
emit("     it never populates a D0-depth class with a twin.  The relaxation")
emit("     to CG removes eps->0 / s-uniformity / all-large-x, NONE of which")
emit("     is the binding cost: the binding cost is the rank m ~ L.")
emit("     VERDICT: superpolylog rank cost STILL BINDING under CG.")
emit("")
emit("-- T9.S2  Second-moment gap statistic (Montgomery-Soundararajan; --")
emit("   corpus tool nearest = Kuperberg 2210.09775, D1.b). --")
emit("Fails in the model (Cramer-defying variance H log(N/H)).  Nearest")
emit("corpus tool admits rank k_adm ~ (log h)^{1/2} at window h; the")
emit("exchange needs k_req = (2/ln 2) lnln x at window h = A' L ln x.")
emit("[B7: k_req = grid L and h = A' L ln x use the GRID surrogate L; the")
emit(" D0-exact L = 2J+1 is larger, widening k_req/k_adm -- the regime")
emit(" square-out is only strengthened, verdict unaffected.]")
emit("x        k_req      k_adm=(ln h)^0.5   ratio k_req/k_adm")
for e in SCALES:
    lnx, llx, L, k = regime(e)
    h = APRIME * L * lnx
    k_req = (2 / LN2) * llx
    k_adm = (log(h)) ** mpf("0.5")
    emit("1e%-5d %10.3f %14.3f %16.3f"
         % (e, float(k_req), float(k_adm), float(k_req / k_adm)))
emit("  -> ratio ~ (lnln x)^{1/2} -> infinity: a REGIME square-out that is")
emit("     independent of endpoint strength.  MS's own interval regime")
emit("     N^delta <= H <= N^{1-delta} (H polynomial) does not even reach")
emit("     the log-size middle window.  The constant-order demand of CG")
emit("     does NOT close a regime gap.  VERDICT: regime-blocked under CG;")
emit("     corpus-status gap (literature-only, not a word-grain tool)")
emit("     also binding.")
emit("")
emit("-- T9.S1  Middle-slot equidistribution / upper-uniformity --")
emit("   (NI-M2 class-equidistribution, NI-M4 word-grain mean value). --")
emit("Fails in the model (model middle is rigid).")
emit("[B5 repair: the prior draft priced this row at local-cost expo 0.000")
emit(" and read it as 'passes every budget, ABSENCE not cost'.  That")
emit(" conflated the bounded PER-INSERT rho factor with the CUMULATIVE")
emit(" ALIGNED cost.  Split three ways against its own anchor:]")
emit("(1) PROVED pointwise aligned envelope.  The worst-case singular-")
emit("    series factor over CRT-aligned in-window middles is")
emit("    sup rho = (ln x)^{1-o(1)} (POLYLOG, expo -> 1; relext-statements")
emit("    RS.3 l.270 / l.1303, PROVED-DOSSIER), (G1)-FAILING at finite")
emit("    scales.  Anchored witnesses (relext-statements T4 l.783-785,")
emit("    MEASURED; exact-factor product p < 1e6):")
emit("      depth     rho        (ln x)-expo")
emit("      1e8        82.24      1.514")
emit("      1e20      221.66      1.410")
emit("      1e1000   1060.34      0.900   (expo descends toward 1 from above)")
emit("(2) HEURISTIC typical mean.  The Gallagher-frame even-conditioned")
emit("    d-mean of rho is 2 (HEURISTIC at growing k; U18.2,")
emit("    relext-statements l.277-280) -- a heuristic, not a proved cost.")
emit("(3) OPEN averaged carrier and cost.  Dimension-1 supplies only the")
emit("    bounded PER-INSERT rho factor (M7); averaging rho away to a")
emit("    proved bounded CUMULATIVE cost needs NI-M2/NI-M4, ABSENT from")
emit("    the corpus (F20.4/F20.5) -- the very carrier S1 is recorded as")
emit("    lacking.")
emit("component            grade         budget status")
emit("pointwise envelope   PROVED-DOSS   expo -> 1: (G1)-FAILS (polylog)")
emit("typical mean = 2     HEURISTIC     not a proved cost")
emit("averaged carrier     OPEN          ABSENT (F20.4/F20.5)")
emit("  -> CG relaxes the DEMANDED strength (full equidistribution, o(1)")
emit("     error -> constant-order non-concentration on sparse scales per")
emit("     s -- strictly weaker) but neither manufactures the missing")
emit("     averaged carrier nor cancels the polylog pointwise aligned")
emit("     cost.  So the block is NOT 'passes every budget' and NOT")
emit("     'absence rather than cost': the aligned cumulative cost is")
emit("     polylog ((G1)-failing) UNLESS the absent NI-M2/NI-M4 carrier")
emit("     supplies the averaging.  VERDICT: S1 OPEN -- right shape,")
emit("     carrier absent, aligned cost polylog; UNDECIDABLE at corpus")
emit("     grain under CG.")
emit("")

# ---------------------------------------------------------------- #
emit("== T10. CG-route rule-12 landing: the F/N -> 0 (SF) onset. ==")
emit("Every CG-route consumes item-0020 F(x,s)/N(x,s) -> 0.  The proved")
emit("cap F <= cap_{J+K} beats the population comparator")
emit("P_0(x) = x/(8 C_0 ln x) = x ln3/(16 ln x) only at astronomical x.")
emit("D0 ceil-honest depths: D=ceil(13 C_0 A'' ln x), J=K=ceil(log2 D),")
emit("r=2J, L=2J+1, M=floor(A' L ln x/2).  Displayed cap U = exp(cap_ln);")
emit("proved binomial cap B = C(M,r).  Permanent crossover = last ln x")
emit("with cap >= P_0 (D0 jumps cause temporary crossings then resets).")

def depths(lnx):
    D = math.ceil(13 * float(C0) * APP * float(lnx))
    J = math.ceil(math.log2(D))
    r = 2 * J
    L = 2 * J + 1
    return J, r, L

def lnP0(lnx):
    # ln P_0 = ln x - ln(8 C_0) - lnln x
    return float(lnx) - math.log(8 * float(C0)) - math.log(float(lnx))

def ln_binom(M, r):
    return float(loggamma(M + 1) - loggamma(r + 1) - loggamma(M - r + 1))

def onset(which):
    # which in {"displayed","binomial"}: return first x beyond which cap<P_0 permanently
    last_ge = None
    t = 3.0
    step = 0.01
    while t <= 500.0:
        J, r, L = depths(t)
        M = math.floor(float(APRIME) * L * t / 2)
        if which == "displayed":
            lc = float(cap_ln(mpf(t), L, r))
        else:
            lc = ln_binom(M, r)
        if lc >= lnP0(t):
            last_ge = t
        t = round(t + step, 2)
    cross = None if last_ge is None else round(last_ge + step, 2)
    return cross

for which, label in [("binomial", "proved binomial cap C(M,r)"),
                     ("displayed", "displayed cap ((3e/4)(L/r)ln x)^r")]:
    cross = onset(which)
    if cross is None:
        emit("  %-38s no permanent crossover in scan" % label)
    else:
        emit("  %-38s permanent cap<P_0 at ln x ~ %.2f (x ~ 1e%.1f)"
             % (label, cross, cross / math.log(10)))
emit("  -> anchored audit values (ANN-20260724-62/63, independently")
emit("     re-verified): proved binomial 1.20e105, displayed 3.53e106.")
emit("     RULE-12 LANDING: the o(1) in F/N = x^{-1+o(1)} lands as an")
emit("     ADDITIVE threshold shift (the ~1e105-1e106 onset), NOT as a")
emit("     leading-coefficient coupling (anchor T3 landing row).  Hence")
emit("     every CG-route is Eventually/Tendsto-extraction only, with no")
emit("     concrete materialization in any reachable range.")
emit("")

# ---------------------------------------------------------------- #
emit("== T11. Pigeonhole-reserve (G3) check for a hypothetical S1 CG-proof. ==")
emit("If S1 existed and drove constant-order non-concentration, the")
emit("consumption would be the C3 reduction (B2.pairs=>REU) shape: NO k-")
emit("or x-dependent constant (anchor T5 row (a): NONE).  Reserve after a")
emit("constant-order C_F: ln x / C_F with C_F = O(1) is (ln x)^{1-o(1)}.")
emit("x        reserve expo (C_F=O(1))    reserve expo (C_F=(ln x)^2, dead)")
for e in SCALES:
    lnx, llx, L, k = regime(e)
    # reserve = ln x / C_F; expo(reserve) = ln(reserve)/lnln x.
    # C_F=O(1): ln(reserve)=lnln x - O(1), expo -> 1.  C_F=(ln x)^2:
    # reserve=(ln x)^{-1}, expo -> -1 < 0 (dead).
    emit("1e%-5d %14.3f %28s"
         % (e, float(expo(llx, llx)), "expo -1: dead"))
emit("  -> a constant-order middle law leaves full reserve; the (G3)")
emit("     reserve is never S1's binding constraint.  S1's block is the")
emit("     absent averaged carrier TOGETHER WITH the polylog pointwise")
emit("     aligned cost against (G1) (T9.S1, B5), not the (G3) reserve.")
emit("     (An (abs)-route S1 with a per-word sieve constant (ln x)^2-")
emit("     class is dead, as in the anchor.)")
emit("")
emit("END OF EXTENSION SHEETS")

with open(__file__.replace("budget_sheet_20_ext.py",
                           "budget_sheet_20_ext_tables.txt"), "w") as f:
    f.write("\n".join(OUT) + "\n")
