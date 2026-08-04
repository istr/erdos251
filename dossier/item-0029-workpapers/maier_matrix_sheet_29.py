# item-0029 -- Maier matrix at word grain: rule-15 sheet (Session M).
#
# Dispatch: item-0029-kickoff-M-v1.md (EXECUTOR, ephemeral, not committed).
# Section 0 pin 7bed96ac7bd688025342d76dddf507a70682b09b.
#
# This is a NEW, self-contained script.  The anchored sheets
# dossier/item-0020-workpapers/budget_sheet_20.py,
# dossier/item-0010-workpapers/budget_sheet_20_ext.py,
# dossier/item-0026-workpapers/pintz_constants_sheet.py and
# dossier/item-0028-workpapers/class_restricted_sheet_28.py are READ-ONLY
# for this session, so their grid conventions are RE-DECLARED here and
# NEVER imported (importing would re-execute them and overwrite their
# anchored _tables.txt).  Conventions, byte-faithful to the anchors:
# SCALES = [8, 20, 100, 1000], APRIME = 1.5, APP = 48, C0 = 2/ln3,
# grid L = (2/ln2) lnln x, L_ceil = 2J+1 with J = ceil(log2(ceil(13 C0
# A'' ln x))), window h = A' L ln x, expo(F) = ln F / lnln x.
#
# Source layer: the four graded-clean-and-hashed extracts under
# dossier/item-0029-workpapers/extract/ (rule 26(4)); every method-side
# figure cites its extract display.  Structural (non-numeric)
# determinations live in word-grain-adjudication.md; this sheet carries
# their priced components (kickoff Section 4.4).
#
# Deterministic: no timestamps, no randomness; float arithmetic only,
# fixed-format printing.  Two runs emit byte-identical tables (V7 S1c).

import math

LN2 = math.log(2.0)
SCALES = [8, 20, 100, 1000]         # x = 10^e (anchor grid)
APRIME = 1.5                        # D0 pin A'
APP = 48                            # D0 pin A''
C0 = 2.0 / math.log(3.0)            # Chebyshev sup q_n/(n ln(n+2))
EULER_GAMMA = 0.5772156649015329

OUT = []


def emit(s=""):
    OUT.append(s)
    print(s)


def lnx_of(e):
    return e * math.log(10.0)


def regime(e):
    lnx = lnx_of(e)
    llx = math.log(lnx)
    L = (2.0 / LN2) * llx
    return lnx, llx, L


def L_ceil(lnx):
    D = math.ceil(13.0 * C0 * APP * lnx)
    J = math.ceil(math.log2(D))
    return 2 * J + 1


def expo(lnF, llx):
    return lnF / llx


def fmt(v, w=10, p=4):
    return ("{:" + str(w) + "." + str(p) + "f}").format(float(v))


def primes_upto(n):
    n = int(n)
    if n < 2:
        return []
    s = bytearray([1]) * (n + 1)
    s[0] = s[1] = 0
    for i in range(2, int(n ** 0.5) + 1):
        if s[i]:
            for j in range(i * i, n + 1, i):
                s[j] = 0
    return [i for i in range(2, n + 1) if s[i]]


def theta(z):
    # Chebyshev theta(z) = sum_{p <= z} ln p, exact sieve.
    return sum(math.log(p) for p in primes_upto(z))


def trunc_str(val, ndec):
    scale = 10 ** ndec
    t = math.floor(val * scale) / scale
    return ("{:." + str(ndec) + "f}").format(t)


# ================================================================== #
# S0 -- conventions echo
# ================================================================== #
emit("item-0029 Maier-matrix word-grain rule-15 sheet (Session M).")
emit("Grid convention (re-declared, anchors read-only): L = (2/ln2)")
emit("lnln x; D0-exact L_ceil = 2J+1, J = ceil(log2(ceil(13 C0 A''")
emit("ln x))).  Window h = A' L ln x, A' = 1.5, A'' = 48, C0 = 2/ln3 =")
emit("%s.  Exponent convention: expo(F) = ln F / lnln x," % fmt(C0, 0, 6))
emit("F = (ln x)^expo.  Budgets (echoed, read-only anchors): (G1)")
emit("o(ln x): expo < 1 with decay or a limit < 1.  (G2) x^eps: ln F =")
emit("o(ln x).  (G3) pigeonhole reserve: ln x / C_F must survive.")
emit("Growth classes (item-0028 vocabulary, binding): GC-CONST expo")
emit("bounded with a stated finite limit; GC-ITLOG expo = c lnlnln x +")
emit("O(1); GC-FASTER expo / lnlnln x -> infinity; DETERMINISTIC /")
emit("MEASURED-exact as in class_restricted_sheet_28.py.")
emit("Exchange evaluation point: rank k = (2/ln2 + o(1)) lnln x, window")
emit("A' L ln x, on the D0 grid (kickoff Section 2.3).")
emit("")

# ================================================================== #
# S1 -- SELF-CHECKS (V7)
# ================================================================== #
emit("== S1a. SELF-CHECK: reproduce the anchored F17.9 grid column ==")
emit("F17.9 = L ln L / lnln x at k = L (pintz-constants.md Section 3")
emit("self-check; anchored 6.143 / 6.932 / 7.944 / 8.963 at 3 dp).")
emit("x        L          F17.9        anchored   match")
anchored_f179 = {8: "6.143", 20: "6.932", 100: "7.944", 1000: "8.963"}
F179 = {}
Ls = {}
llxs = {}
lnxs = {}
S1a_pass = True
for e in SCALES:
    lnx, llx, L = regime(e)
    lnxs[e], llxs[e], Ls[e] = lnx, llx, L
    v = expo(L * math.log(L), llx)
    F179[e] = v
    got = trunc_str(v, 3)
    rounded = "{:.3f}".format(v)
    ok = (got == anchored_f179[e]) or (rounded == anchored_f179[e])
    S1a_pass = S1a_pass and ok
    emit("1e%-5d %s %s   %s      %s"
         % (e, fmt(L), fmt(v), anchored_f179[e], "PASS" if ok else "FAIL"))
emit("  -> S1a: %s" % ("PASS" if S1a_pass else "FAIL"))
emit("")

emit("== S1b. SELF-CHECK: method-side printed numeric (named) ==")
emit("Chosen quantity: the Lemma 3.4(b) closing numeric of")
emit("freiberg11-strings2.md (Section 6, p.13; structural-map note 6):")
emit("  (1/2)(1 - 1/e) e^(gamma/2) = 0.42... > 2/5.")
v = 0.5 * (1.0 - math.exp(-1.0)) * math.exp(EULER_GAMMA / 2.0)
got2 = trunc_str(v, 2)
S1b_pass = (got2 == "0.42") and (v > 2.0 / 5.0)
emit("computed: %s ; truncated 2 dp: %s (source prints 0.42...);"
     % (fmt(v, 0, 6), got2))
emit("exceeds 2/5: %s" % ("True" if v > 0.4 else "False"))
emit("  -> S1b: %s" % ("PASS" if S1b_pass else "FAIL"))
emit("")

emit("== S1c. Re-run stability ==")
emit("Established outside this script: two full runs emit byte-identical")
emit("tables files (recorded in item-0029-report-M.md).  -> S1c: see")
emit("report.")
emit("")

S1_ALL = S1a_pass and S1b_pass
emit("S1 SELF-CHECKS (in-script): %s"
     % ("ALL PASS" if S1_ALL else "AT LEAST ONE MISS -- STOP r29M.9"))
emit("")

# ================================================================== #
# CM-1 -- native-regime map
# ================================================================== #
emit("== CM-1. Native-regime map vs the exchange evaluation point ==")
emit("Documented native parameters (citations in parentheses):")
emit("  maier85: modulus P(z) = prod_{p<z} p, rows r in (P^{D-1},")
emit("  2P^{D-1}], row length U = [z^lambda], lambda > 1 fixed, x ~")
emit("  P(z)^D (maier85-shortintervals.md Sections 4.1-4.2).")
emit("  hm88: modulus P(z) = prod_{p<=z} p, R = P(z)^{D-1}, row length")
emit("  T z, T fixed, x = P(z)^D, log x = D sum_{p<=z} log p ~ z")
emit("  (hildebrandmaier88-gaps.md Section 4.2).")
emit("  freiberg10/11: rows (Qn, Qn+H], n in (N, 2N], H = eps log N,")
emit("  Q the Shiu-type modulus (freiberg10-strings1.md (2.6)/(5.19);")
emit("  freiberg11-strings2.md (3.1)-(3.6)).")
emit("Native rank is FIXED in every source: 'every fixed integer k'")
emit("(hm88 abstract; the Theorem prints 'Let k be a positive")
emit("integer'), 'Fix positive integers k and ell' (freiberg10")
emit("Prop. 2.2); the exchange point demands k = L growing.  A")
emit("non-instantiable map is itself a priced finding (kickoff CM-1).")
emit("x        k_req=L    k_req=Lc   k_adm(source)  window A'L lnx")
Lcs = {}
for e in SCALES:
    lnx, llx, L = lnxs[e], llxs[e], Ls[e]
    Lc = L_ceil(lnx)
    Lcs[e] = Lc
    emit("1e%-5d %s %10d   O(1) fixed     %s"
         % (e, fmt(L), Lc, fmt(APRIME * L * lnx, 12, 1)))
emit("Rank mismatch ratio k_req/k_adm is unbounded (grows like lnln x):")
emit("the native regime does not reach the exchange point on the rank")
emit("axis at any scale.  Support: RECORDED (fixed-k quantifiers are")
emit("the sources' own; no numeric k_adm exists to tabulate).")
emit("")
emit("Window reachability (native row length vs exchange window):")
emit("  hm88 ratio (T z)/(A' L ln x) = (T/D)/(A' L) at z ~ ln x / D --")
emit("  T, D fixed: the native row is SHORTER by a growing lnln-factor.")
emit("  maier85 U = z^lambda covers the window iff lambda >= lambda*;")
emit("  lambda* = ln(A' L ln x)/ln(z) at reference z = ln x / D, D = 2.")
emit("x        hm88 (T/D)/(A'L) at T/D=1   maier85 lambda* (D=2 ref)")
for e in SCALES:
    lnx, llx, L = lnxs[e], llxs[e], Ls[e]
    z_ref = lnx / 2.0
    lam_star = math.log(APRIME * L * lnx) / math.log(z_ref)
    emit("1e%-5d %s                 %s"
         % (e, fmt(1.0 / (APRIME * L)), fmt(lam_star)))
emit("maier85's fixed lambda > 1 covers the exchange window once")
emit("lambda >= lambda*, and lambda* decreases toward 1 with scale:")
emit("the WINDOW axis is natively reachable (the regime-filter reading")
emit("of the item-0026 record); the rank axis is not.  Support:")
emit("MEASURED (this table) on the documented parameter shapes.")
emit("")

# ================================================================== #
# CM-2 -- distributional input range vs mapped demand
# ================================================================== #
emit("== CM-2. Distributional inputs: admissible range vs mapped demand ==")
emit("Inputs as documented (Task A element A-2 of the adjudication):")
emit("  (i) good-modulus AP counts: maier85 Lemma 2 (x >= q^D, h ~ x),")
emit("  hm88 Lemma 1 (uniform x >= q^D); good moduli exist on a sparse")
emit("  z-set only (maier85 Lemma 1, hm88 Lemma 2).  Natively")
emit("  self-consistent; no k enters -- but the word-grain application")
emit("  needs the tuple layer below, which is fixed-k.")
emit("  (ii) hm88 Lemma 3 (sieve upper bound, '<<_g', g fixed).")
emit("  (iii) freiberg10 Lemma 4.2 (BV variant, moduli QD <= R*) with")
emit("  the (4.13) accumulation exponent 2(k+ell) + (3k)^2/2 + 1/2")
emit("  against the (4.10) saving (log N)^{-5 c3 loglog N}, c3 fixed.")
emit("Mapped demand at k = L, ell = [sqrt(L)] (exchange rank):")
emit("x        (4.13)-exponent at k=L    available saving exponent")
for e in SCALES:
    lnx, llx, L = lnxs[e], llxs[e], Ls[e]
    ell = math.floor(math.sqrt(L))
    demand = 2.0 * (L + ell) + (3.0 * L) ** 2 / 2.0 + 0.5
    emit("1e%-5d %s              5 c3 lnln x = %s c3"
         % (e, fmt(demand, 12, 1), fmt(5.0 * llx)))
emit("The demanded polylog discount exponent grows like 4.5 L^2 (GC-")
emit("FASTER); the documented saving carries a FIXED c3 (freiberg10")
emit("(4.10), c3 = c2/(12 c eps)).  The documented range does not meet")
emit("the mapped demand at the exchange rank.  Support: PROVED (finite")
emit("arithmetic on the documented exponents of (4.10)/(4.13)).")
emit("")

# ================================================================== #
# CM-3 -- per-member weight/sieve losses at the exchange rank
# ================================================================== #
emit("== CM-3. Weight/sieve k-dependent factors at the exchange rank ==")
emit("CM-3a. GPY weight normalization (k+2 ell)! (freiberg10 (2.9)/")
emit("(2.10) denominators), mapped to k = L, ell = [sqrt(L)]:")
emit("expo = ln((k+2 ell)!)/lnln x -- the rule-15 'hidden k!' class.")
emit("x        expo((L+2l)!)   F17.9 wall   rule-15")
for e in SCALES:
    lnx, llx, L = lnxs[e], llxs[e], Ls[e]
    ell = math.floor(math.sqrt(L))
    v = expo(math.lgamma(L + 2 * ell + 1.0), llx)
    emit("1e%-5d %s %s   NO-GO (G1: expo > 1 at every scale)"
         % (e, fmt(v), fmt(F179[e])))
emit("Class: GC-ITLOG (expo = (2/ln2) lnlnln x + O(1)), the F17.9 / T1")
emit("family exp((1+o(1)) k ln k); the (G1) NO-GO stands because expo")
emit("exceeds 1 at every scale and does not decay.  Support: MEASURED")
emit("(lgamma) on the documented display.")
emit("")
emit("CM-3b. Fourth-moment row-count discount (log N)^{19k+4 ell}")
emit("(freiberg10 (6.2)), mapped to k = L:")
emit("x        expo = 19L+4l   rule-15")
for e in SCALES:
    lnx, llx, L = lnxs[e], llxs[e], Ls[e]
    ell = math.floor(math.sqrt(L))
    emit("1e%-5d %s   NO-GO (GC-FASTER)" % (e, fmt(19.0 * L + 4.0 * ell)))
emit("Support: PROVED arithmetic on the documented exponent.")
emit("")
emit("CM-3c. hm88 Lemma 3 implied constant '<<_g' at g = L+1: the")
emit("source documents fixed g only; the standard growing-rank sieve")
emit("constant is the F17.9 wall exp((1+o(1)) k ln k) (S1a column,")
emit("6.14 -> 8.96, all > 1).  UNDOCUMENTED at growing rank; priced by")
emit("reference class.  Support: RECORDED (fixed-g quantifier is the")
emit("source's own) + the anchored F17.9 reference column (S1a).")
emit("")

# ================================================================== #
# CM-4 -- documented row counts vs word-grain populations
# ================================================================== #
emit("== CM-4. Documented counts vs word-grain populations ==")
emit("Project comparators, quoted (collision-gap-audit.md C.1):")
emit("  F = x^{o(1)} (family capacity), N = x^{1-o(1)} (site")
emit("  population).  Tabulated: expo_F = (J+K) ln(e A' L ln x /")
emit("  (2(J+K)))/lnln x at J+K = L_ceil - 1; expo_N = (ln x - ln(8 C0")
emit("  ln x))/lnln x.")
emit("x        expo_F(cap)   expo_N(pop)")
for e in SCALES:
    lnx, llx, L = lnxs[e], llxs[e], Ls[e]
    JK = Lcs[e] - 1
    capln = JK * math.log(math.e * APRIME / 2.0 * L * lnx / JK)
    popln = lnx - math.log(8.0 * C0 * lnx)
    emit("1e%-5d %s %s" % (e, fmt(expo(capln, llx)), fmt(expo(popln, llx))))
emit("Documented method-side favourable-row counts (per scale):")
emit("  freiberg10 (6.8): >> N/(log N)^{B(eps)}, printed chain gives")
emit("  B = 17k+2 at fixed k (share discount expo = 17k+2);")
emit("  freiberg11 (1.2): >= X^{1-c/loglog X} strings up to X, all")
emit("  large X, c absolute (share-of-primes discount expo below, at")
emit("  reference c = 1, marked as reference).")
emit("x        f10 expo (k=5 ref)  f10 expo (k=L)  f11 expo (c=1 ref)")
for e in SCALES:
    lnx, llx, L = lnxs[e], llxs[e], Ls[e]
    f10_fix = 17.0 * 5.0 + 2.0
    f10_L = 17.0 * L + 2.0
    f11 = lnx / (llx * llx) - 1.0
    emit("1e%-5d %s %s %s"
         % (e, fmt(f10_fix, 14), fmt(f10_L, 15), fmt(f11, 14)))
emit("(f11 column: exact share-of-primes discount expo c lnx/(lnln x)^2")
emit("- 1, the -1 from the 1/ln X in pi(X); c = 1 reference.)")
emit("Reading: every documented favourable-row count is a DECAYING")
emit("proportion of its row population (polylog discount at fixed k;")
emit("GC-FASTER discount at k = L); none is a positive proportion of")
emit("any family count, and none allocates counts to word-grain")
emit("classes (adjudication Q-CORR).  The proportion arithmetic against")
emit("c * F needs an allocation step the corpus does not document; raw")
emit("magnitude is not the blocker.  Support: PROVED arithmetic on the")
emit("documented exponents; allocation absence RECORDED (Q-CORR).")
emit("")

# ================================================================== #
# CM-5 -- per-family multiplicity and the pigeonhole reserve
# ================================================================== #
emit("== CM-5. Per-family multiplicity; two-distinct-middles reserve ==")
emit("Documented multiplicity control: hm88 (11) >= 3kR primes in A;")
emit("(12) >= kR in good rows; (14) >= kR/2 consecutive-(k+1)-tuples;")
emit("(19) <= C R/N^k tuples per value box.  No per-word or per-class")
emit("lower bound is documented in any extract.")
emit("")
emit("CM-5a. Pigeonhole margins on the (14) tuple floor (finite algebra;")
emit("adjudication Section 5.2).  ln R = (D-1) theta(z), z = ln x / D;")
emit("reference D = 2, T = 5, k = 5; theta exact (sieve).  Two distinct")
emit("capacities, priced separately: COMPLETE-word margin ln(k R/2) -")
emit("k ln(T z) (positive forces some complete word -- flanks AND")
emit("middle -- realized twice); FLANK-word margin ln(k R/2) -")
emit("(k-1) ln(T z) (positive forces some flank word realized twice,")
emit("middles unconstrained).  Exchange column: flank margin at k=Lc.")
emit("x        complete k=5    flank k=5      flank k=Lc")
Vs = {}
for e in SCALES:
    lnx, llx, L = lnxs[e], llxs[e], Ls[e]
    z = lnx / 2.0
    th = theta(z)
    V = 1.0
    for p in primes_upto(z):
        V *= (1.0 - 1.0 / p)
    Vs[e] = V
    lnR = th  # (D-1) theta(z) at D = 2
    mw = math.log(5.0 / 2.0) + lnR - 5.0 * math.log(5.0 * z)
    m5 = math.log(5.0 / 2.0) + lnR - 4.0 * math.log(5.0 * z)
    kc = Lcs[e]
    mc = math.log(kc / 2.0) + lnR - (kc - 1.0) * math.log(5.0 * z)
    emit("1e%-5d %s %s %s"
         % (e, fmt(mw, 14, 2), fmt(m5, 13, 2), fmt(mc, 13, 2)))
emit("Reading: both fixed-k margins tend to +infinity ((D-1)theta(z)")
emit("~ z beats k ln(Tz)); on the grid the flank margin is positive")
emit("from 1e20 and the complete-word margin from 1e100.  At k = L_ceil")
emit("the tuple floor (14) is itself undocumented (fixed-k constants),")
emit("so that column prices arithmetic only, not a documented")
emit("statement.  Support: PROVED (finite algebra from (14) and the")
emit("capacity counts) at fixed k; RECORDED absence at growing k.")
emit("")
emit("CM-5b. Two-distinct-middles margin (the per-middle ceiling route,")
emit("adjudication Section 5.2).  For a fixed middle, members of one")
emit("flank class are capped by (admissible s_1 count ~ c V(z) z, hm88")
emit("Section 4.2) x (Lemma 3 at g = k+1: << R/(V(z) log R)^{k+1},")
emit("log R ~ z), i.e. <= C'_k R/(V(z) z)^k uniformly in the middle;")
emit("the flank pigeonhole floor M >= k R/(2 (Tz)^{k-1}) then forces")
emit("distinct middles once margin = ln(k/2) + k ln(V(z) z) -")
emit("(k-1) ln(T z) - ln(C'_k) > 0.  Asymptotically margin =")
emit("ln z - k lnln z + O_{k,T}(1) -> +infinity at every fixed k:")
emit("distinct middles are FORCED at fixed rank on all large good z")
emit("(PROVED from (14), the Section 4.2 column count, Lemma 3 and")
emit("Mertens).  Grid values at C'_k = 1, k = 5, T = 5 (reference;")
emit("Lemma 3's <<_g constant is undocumented, so grid signs are")
emit("reference-only while the divergence is PROVED):")
emit("x        V(z)       distinct-middles margin (ref)")
for e in SCALES:
    lnx, llx, L = lnxs[e], llxs[e], Ls[e]
    z = lnx / 2.0
    V = Vs[e]
    mdm = (math.log(5.0 / 2.0) + 5.0 * math.log(V * z)
           - 4.0 * math.log(5.0 * z))
    emit("1e%-5d %s %s" % (e, fmt(V, 0, 6), fmt(mdm, 14, 2)))
emit("The margin's divergence onset at these reference constants lies")
emit("far beyond the grid (ln z must beat k lnln z + O(1)); no grid")
emit("scale certifies the forcing numerically.  What remains absent at")
emit("EVERY rank: any family-population control that would convert the")
emit("forced existence into a proportion of F^ms(x); and at the")
emit("exchange rank k = L the whole chain is undocumented (CM-3).  The")
emit("middle-slot non-concentration carrier named by the S1 deciding")
emit("fact (separator-repricing.md W4.S1) is absent in its exchange-")
emit("rank, D0-window form; at fixed rank Lemma 3 + Lemma 4 supply the")
emit("surrogate used here.  Support: PROVED (asymptotic) + MEASURED")
emit("(reference grid values) + RECORDED (absences).")
emit("")

# ================================================================== #
# CM-6 -- scale-sequence structure
# ================================================================== #
emit("== CM-6. Scale-sequence structure, priced against A6 ==")
emit("Documented scale sets: maier85 -- z with P(z) good, 'arbitrarily")
emit("large values' (Lemma 1; sparse); hm88 -- same set (Lemma 2) plus")
emit("a subsequence for the limit-point step (p.7); freiberg10 -- one")
emit("H per window [X/(log X)^A, X] (Lemma 5.5); freiberg11 -- ALL")
emit("sufficiently large H (Lemma 3.4), removing the sparseness for")
emit("the string count (1.2).")
emit("A6 relaxation (sparse scales suffice, no s-uniformity): every")
emit("documented scale density MEETS the item's scale demand -- the")
emit("density axis is the one axis the method clears natively, and")
emit("freiberg11 clears it in the all-large-x form a fortiori.  Priced")
emit("consequence: no scale-density cost enters any column above; the")
emit("failing axes are rank (CM-1/CM-3), allocation/grain (CM-4/CM-5),")
emit("never density.  Support: RECORDED (documented quantifiers).")
emit("")

# ================================================================== #
# S6 -- the mechanical verdict rule and its application
# ================================================================== #
S6_BLOCK = """S6 VERDICT RULE (item-0029). Emit V-POS (positive proportion at
corpus grain) if and only if ALL of:
(a) Q-SHAPE = SHAPE-POSITIVE-PROPORTION at support proved-in-source
    or PROVED (finite algebra in this workpaper from statements the
    consumable extracts document, each cited), with the constant
    c > 0 independent of the scale, on an unbounded scale sequence;
(b) the counted property in (a) is two members of one family with
    equal flanks and distinct middles -- the property itself, not a
    proxy -- at the same support;
(c) Q-CORR = CORR-ESTABLISHED at support proved-in-source or PROVED,
    including the consecutiveness clause, OR the family object of (a)
    is itself already the word-grain flank class of the fixed
    definitions;
(d) every load-bearing constant and factor of the chain (a)-(c)
    appears as a sheet column with a growth class, and none is an
    immediate rule-15 no-go at the exchange evaluation point.
Otherwise emit V-NEG (bounded existence or weaker, at corpus grain):
name, for each failing clause, the exact failing element, and
classify the failure STRUCTURAL (the documented schema's own steps
yield only the weaker shape) or EVIDENTIAL (the corpus does not
document the needed step in either direction). In every outcome,
record the STRONGEST shape the corpus does support, with its axis
(A-7 taxonomy), its support class, and its citations.

CLAUSE-BY-CLAUSE DETERMINATION (mechanical; structural inputs from
word-grain-adjudication.md Sections 4-5, priced inputs from the CM
columns of maier_matrix_sheet_29_tables.txt):
(a) FAILS. Q-SHAPE is not SHAPE-POSITIVE-PROPORTION: no documented
    counting step, and no finite algebra licensed from documented
    statements, yields a lower bound c * F^ms(x), c > 0
    scale-independent, on families carrying two distinct realized
    middles, for any family notion at any rank
    (hildebrandmaier88-gaps.md (11)-(19) reach value-space boxes and
    tuple totals; freiberg10-strings1.md (3.2)/(6.8) and
    freiberg11-strings2.md (1.2) reach favourable-row counts; no
    extract documents family-population control either way).  What
    IS derivable (adjudication Section 5.2, PROVED): at every fixed
    k on the sparse good-modulus scales, the (14) tuple floor
    against the per-middle ceiling (Lemma 3 with the Section 4.2
    column count) forces flank classes carrying two -- derivably,
    unboundedly many -- DISTINCT realized middles: existence with
    growing count, short of every proportion form.  Failure class:
    EVIDENTIAL for the proportion step, with the PROVED fixed-k
    existence recorded below as the strongest family-axis shape.
(b) FAILS. The corpus's only positive-proportion conclusion
    (hildebrandmaier88-gaps.md Theorem, p.2) counts boxes of
    normalized difference tuples in [0,T]^k -- Lebesgue measure on
    the VALUE axis -- a proxy, not two members of one family with
    equal flanks and distinct middles.  Failure class: STRUCTURAL
    (the documented steps yield the value-axis shape, not the
    property).
(c) FAILS. Q-CORR = CORR-NOT-ESTABLISHED: the documented family index
    fixes the admissible offset set, never the realized flank word;
    no documented statement forces two family members to share flank
    words of consecutive prime gaps at the D0 depth J+K = L-1
    (missing elements named in adjudication Section 4); and no family
    object of (a) is itself the word-grain flank class of the fixed
    definitions.  Failure class: EVIDENTIAL.
(d) FAILS at the exchange evaluation point.  The load-bearing
    k-dependent factors of the documented chain, mapped to rank
    k = L = (2/ln2) lnln x, are immediate rule-15 no-gos: the GPY
    normalization (k+2 ell)! is the exp((1+o(1)) k ln k) class
    (CM-3a, expo 7.2 -> 9.8 > 1 at every scale, (G1) fails); the
    fourth-moment discount (log N)^{19k+4 ell} and the BV exponent
    4.5 k^2 are GC-FASTER (CM-3b, CM-2); the native regimes are
    fixed-k and do not reach the point (CM-1).  Failure class:
    STRUCTURAL (the documented schema's own normalizations carry the
    factors).

VERDICT: V-NEG (bounded existence or weaker, at corpus grain).
STRONGEST SUPPORTED SHAPES (recorded per the rule's final clause):
VALUE axis -- SHAPE-POSITIVE-PROPORTION of the limit-point cube:
lambda(S^(k) cap [0,T]^k) >= c(k) T^k, proved-in-source (assembly
printed, Lemmas 1-3 by reference), hildebrandmaier88-gaps.md Theorem
(p.2), fixed k, sparse scales.  ROW-COUNT axis --
SHAPE-DECAYING-PROPORTION of favourable rows, proved-in-source:
>> N/(log N)^{B(eps)} rows per scale (freiberg10-strings1.md (6.8))
and >= X^{1-c/loglog X} strings up to X for all large X
(freiberg11-strings2.md (1.2); Lemmas 3.2/3.3 proofs outside the
declared extract scope, by named reference).  FAMILY axis -- at
fixed rank on sparse scales: EXISTENCE of flank classes with two
distinct realized middles, derivably unbounded per-scale count, all
but o(1) of the tuple mass non-rigid, PROVED (finite algebra from
hildebrandmaier88-gaps.md (14), the Section 4.2 column count, Lemma
3 and Mertens; adjudication Section 5.2, sheet CM-5b) -- the
decisive objection's bounded-existence-type shape, sharpened; no
proportion of F^ms(x) is derivable either way at any rank, and at
the D0 depth k = L nothing is derivable (fixed-k, CM-1/CM-3)."""

# Mechanical application: the rule's boolean structure over the four
# clause outcomes established above (data mirrors the block text).
CLAUSES = {"a": False, "b": False, "c": False, "d": False}
VERDICT = "V-POS" if all(CLAUSES.values()) else "V-NEG"
assert VERDICT == "V-NEG"
assert "VERDICT: V-NEG" in S6_BLOCK

emit("== S6. Mechanical verdict rule and application (byte-identical")
emit("with the Verdict section of word-grain-adjudication.md) ==")
emit("")
for line in S6_BLOCK.split("\n"):
    emit(line)
emit("")
emit("END OF MAIER MATRIX SHEET 29")

with open(__file__.replace("maier_matrix_sheet_29.py",
                           "maier_matrix_sheet_29_tables.txt"), "w") as f:
    f.write("\n".join(OUT) + "\n")
