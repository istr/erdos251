# item-0036 -- rank-ceiling sheet for the matrix word-grain mechanism.
#
# Dispatch: item-0036-kickoff-v1.md (EXECUTOR, ephemeral, not committed).
# Section 0 pin 15aff75830f008b6bc38fc90cf4867600171d871.
#
# This is a NEW, self-contained script.  The anchored sheets
# dossier/item-0029-workpapers/maier_matrix_sheet_29.py and
# dossier/item-0028-workpapers/class_restricted_sheet_28.py are
# READ-ONLY for this session, so their grid conventions are RE-DECLARED
# here and NEVER imported (importing would re-execute them and overwrite
# their anchored _tables.txt).  Conventions, byte-faithful to the
# anchors: LN2, SCALES = [8, 20, 100, 1000], APRIME = 1.5, APP = 48,
# C0 = 2/ln3, grid L = (2/ln2) lnln x, L_ceil = 2J+1 with J =
# ceil(log2(ceil(13 C0 A'' ln x))), window h = A' L ln x,
# expo(F) = ln F / lnln x.
#
# Source layer (runs/README rule 26(4)): the graded-clean-and-hashed
# extracts named in the kickoff Section 2 are the only source
# surrogates; every source-facing figure cites its (q)-row of the
# kickoff Section 3 / workpaper Section 1.  Structural derivations live
# in rank-ceiling-sheet.md; this sheet carries their priced columns.
#
# Deterministic: no timestamps, no randomness; mpmath dps 40; two
# invocations emit byte-identical tables (gate W6).

from mpmath import mp, mpf, log, exp, euler
import bisect
import math

mp.dps = 40

LN2    = log(2)
SCALES = [8, 20, 100, 1000]         # x = 10^e  (anchor grid)
APRIME = mpf("1.5")                 # D0 pin A'
APP    = 48                         # D0 pin A''
C0     = 2 / log(3)                 # Chebyshev sup q_n/(n ln(n+2)) = 2/ln3
EG     = exp(euler)                 # e^gamma = Mertens third-theorem const
BETA   = 2 / LN2                    # exchange-rank coefficient

OUT = []


def emit(s=""):
    OUT.append(s)
    print(s)


def lnx_of(e):
    return e * log(10)


def regime(e):
    # anchor tag: the GRID surrogate rank L = (2/ln2) lnln x.
    lnx = lnx_of(e)
    llx = log(lnx)
    L = (2 / LN2) * llx
    return lnx, llx, L


def L_ceil(lnx):
    # D0-exact depth L_ceil = 2J+1, J = ceil(log2(ceil(13 C0 A'' ln x))).
    D = math.ceil(13 * float(C0) * APP * float(lnx))
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
    return sum(log(p) for p in primes_upto(z))


def sieve_V(z):
    # V(z) = prod_{p <= z} (1 - 1/p), exact sieve product ((q1) V(z)).
    V = mpf(1)
    for p in primes_upto(z):
        V *= (1 - mpf(1) / p)
    return V


def margin_general(k, T, lnC, V, z):
    # The k-uniform (q10) chain margin (workpaper Section 3.1):
    #   ln(k/2) + k ln(V(z) z) - (k-1) ln(T z) - ln C_{k+1}
    # floor M >= kR/(2 (Tz)^{k-1}) from (q7)/(q10) against the
    # per-middle ceiling C_{k+1} c V(z) z * R/(V(z) z)^{k+1} from
    # (q1)+(q5)+(q8); the c = 3k and (z/log R)^{k+1} conversion
    # factors ((q5) asymp licence) contribute -ln(a_0 c) = O(k),
    # subdominant to k lnln z at every priced schedule; they sit
    # outside the displayed margin (workpaper Section 3.1).
    return log(k / mpf(2)) + k * log(V * z) - (k - 1) * log(T * z) - lnC


# The V-36 verdict rule, byte-fixed at kickoff time (kickoff Section 1);
# this literal lands byte-identically here (RC-6) and in workpaper
# Section 5 (gate W9).
V36_BLOCK = """V-36 VERDICT RULE (item-0036). Semantics: k*(x; H) is the ceiling of
the DOCUMENTED item-0029 Section 5.2 derivation chain (the (q10)
quotations) carried k-uniformly under hypothesis row H: the supremum
over admissible couplings (T = lambda c with lambda > 1 fixed, per
(q2)/(q4); c the (q6) constant at reference c = 3k, the absolute
constant of the (q5)/(q6) chain disclosed undocumented) of the
largest rank schedule k(x) for which EVERY chain step closes by
finite algebra from the Section 3 quotations, the row-H bound on the
Lemma-3 constant at g = k+1, and the PROVED-elementary smooth-count
line of RC-4 -- every inequality either PROVED (finite algebra) or
listed as a DEBT in the RC-4/RC-5 uniformization ledger, with no
emitted class resting on a DEBT.
Hypothesis rows: H-EXP: C_g <= C^g (absolute C > 1); H-FACT:
C_g <= exp(c_H g ln g) (absolute c_H > 0); both applied to the
Lemma-3 implied constant at g = k+1.
Per row H emit:
(P1) DIVERGES iff the sheet exhibits ONE admissible lambda and ONE
     named schedule phi_H(x) -> infinity with every chain step
     closing at k(x) = phi_H(x) (sufficiency side); phi_H displayed.
(P2) MISSES iff the sheet exhibits a named envelope
     psi_H(x) = o(lnln x) such that the (q10) margin inequality -- a
     step of the chain itself -- fails asymptotically for every
     k(x) >= psi_H(x) and every fixed lambda > 1 (necessity side);
     psi_H displayed.
NAME the binding wall on each side: the necessity wall (lambda-free)
and the sufficiency wall as a function of lambda, with the
lambda -> 1 boundary listed as a DEBT wherever it moves the wall.
FLAG GUARD (binding; design-note D3(ii)): if closing any step under
any row would require an equidistribution or tuple-count uniformity
stronger than the frozen HLQuantA card consumes, emit FLAG naming
row and step and do not emit (P1)/(P2) for that row (STOP r36.6); no
column consumes the HLQuantA card in any direction.
EMISSION: V-DIV-BELOW iff (P1) and (P2) both hold on BOTH rows;
V-BOUNDED iff (P1) fails on any row (name row and wall); V-REACHES
iff (P2) fails on any row (name row and wall); V-UNDECIDABLE iff any
needed column is missing, any growth class is ambiguous, or a
required envelope cannot be exhibited by finite algebra (STOP
r36.7). Grid values are reference-only (MEASURED), never
load-bearing for (P1)/(P2). BET-20260804-15 material: the (P1)/(P2)
pair per row IS the bet's two halves; scoring is operator judgment,
never in-run."""

# The mechanical application (RC-6); byte-identical with workpaper
# Section 5 alongside the rule block (gate W9).
V36_APPLICATION = """V-36 CLAUSE-BY-CLAUSE APPLICATION (mechanical; every PROVED support
below is finite algebra in rank-ceiling-sheet.md Section 3 from the
Section-1 quotation rows, the row-H bound at g = k+1 and the RC-4
smooth-count line; grid columns of this file are reference-only).
COUPLING (RC-2, both rows): T = lambda c, c = 3k reference, delta =
1/lambda; admissible iff lambda > 1 ((q2)'s 0 < delta < 1) and
T > max(2, c) ((q4)); both hold for every fixed lambda > 1 at every
k >= 1, and (q2)'s K >= 2 holds at K = T = 3 lambda k.
ROW H-EXP (C_g <= C^g, absolute C > 1, applied at g = k+1):
(P1) HOLDS. Exhibit lambda = 2 and phi_EXP(x) = (lnln x)^{1/4} ->
     infinity.  Every chain step closes at k = phi_EXP in the
     rule's own either-PROVED-or-DEBT sense: the RC-2 constraints
     (PROVED); the RC-3 margin tends to +infinity (PROVED,
     workpaper Section 3.1 (S1)); the RC-4 smooth-count constraint
     closes with room, its left side being O((lnln x)^{1/2}
     lnlnln x) = o(lnln x) (PROVED, Section 3.2 (S2)); the RC-5
     range checks close (PROVED, Section 3.4); the Lemma-4
     carriage clauses stand as the named DEBTS d1-d4, consumed as
     proved inputs nowhere.
(P2) HOLDS. Envelope psi_EXP(x) = (3/4) lnln x/lnlnln x = o(lnln x):
     the (q10) margin, carried with the row bound at g = k+1, tends
     to -infinity for every k(x) >= psi_EXP(x) and every fixed
     lambda > 1 (PROVED, lambda-free, workpaper Section 3.1 (N1)).
ROW H-FACT (C_g <= exp(c_H g ln g), absolute c_H > 0, at g = k+1):
(P1) HOLDS. Same coupling lambda = 2, same schedule phi_FACT(x) =
     (lnln x)^{1/4}: the row constant adds c_H (k+1) ln(k+1) =
     o(lnln x) at this schedule and every step still closes in the
     same sense (PROVED, Section 3.1 (S1)).
(P2) HOLDS. psi_FACT(x) = (3/4) lnln x/lnlnln x: the row constant
     only deepens the margin failure (PROVED, lambda-free, Section
     3.1 (N1)).
BINDING WALLS. Necessity side, lambda-free: W-A (Lemma-3 constant +
Mertens power) -- the (q10) margin dies at k = (theta*_H + o(1))
lnln x/lnlnln x with theta*_EXP = 1/2 and theta*_FACT = 1/(2 + c_H)
(Section 3.1 (N2)); no admissible coupling moves it.  Sufficiency
side, as a function of lambda: W-B (Lemma-4 uniformization, the
smooth-count constraint) -- at every fixed lambda > 1 the chain's
certified closure reaches the class (lnln x/lnlnln x)^{1/lambda}
and is no longer derivable above it, so W-B binds strictly below
W-A at every fixed lambda; the lambda -> 1 boundary moves the
sufficiency wall toward the W-A class and is DEBT (d5).  W-C
prices the coupling that feeds both walls (T = 3 lambda k); W-D
never binds (RC-5).
FLAG GUARD: checked step by step against the frozen HLQuantA card
(strength comparison only, card read via blocks.py-verified state,
quoted into no column): the chain consumes single-prime AP counts on
good moduli ((q5)), a sieve UPPER bound with a named hypothesis row
on its constant ((q1), rows H), a prime-free integer-sieve statement
((q2)/(q3)) and the elementary smooth count -- no equidistribution
or tuple-count uniformity at or beyond the card's strength enters in
any direction, and no column consumes the card.  NO FLAG; STOP r36.6
not fired.
EMISSION: V-DIV-BELOW -- (P1) and (P2) both hold on BOTH rows: on
every named hypothesis row the priced chain closes on a named
diverging schedule and its (q10) margin fails on a named envelope
psi_H = o(lnln x); the ceiling k*(x; H) diverges yet misses the
exchange rank k = (2/ln2 + o(1)) lnln x on both rows.  Per fixed
lambda the ceiling class is (lnln x/lnlnln x)^{1/lambda} (W-B); the
lambda-supremum approaches, and never attains, the class
lnln x/lnlnln x, and everything at or above psi_H fails at every
coupling (W-A).  DEBT ledger d1-d5 stands (RC-4); no emitted class
rests on a DEBT as a proved input (the closing clause's own
either-PROVED-or-DEBT sense; the strict all-PROVED alternative
reading is recorded in the run report and workpaper Section 11).
Grid values reference-only (MEASURED), never
load-bearing for (P1)/(P2).  BET-20260804-15 material: the per-row
(P1)/(P2) pairs above are the bet's two halves; BET-20260804-15
stays OPEN for operator judgment against this sheet; no bet is
scored in-run."""

# ================================================================== #
# RC-0 -- conventions block
# ================================================================== #
emit("item-0036 rank-ceiling sheet for the matrix word-grain mechanism.")
emit("== RC-0. Conventions block ==")
emit("Grid convention (re-declared, anchors read-only): L = (2/ln2)")
emit("lnln x; D0-exact L_ceil = 2J+1, J = ceil(log2(ceil(13 C0 A''")
emit("ln x))).  Window h = A' L ln x, A' = 1.5, A'' = 48, C0 = 2/ln3 =")
emit("%s, e^gamma = %s." % (fmt(C0, 0, 6), fmt(EG, 0, 6)))
emit("Exponent convention: expo(F) = ln F / lnln x, F = (ln x)^expo.")
emit("Growth classes (item-0028 vocabulary, binding): GC-CONST expo")
emit("bounded with a stated finite limit; GC-ITLOG expo = c lnlnln x +")
emit("O(1); GC-FASTER expo / lnlnln x -> infinity; DETERMINISTIC /")
emit("MEASURED-exact as in class_restricted_sheet_28.py.")
emit("Exchange evaluation point: rank k = (2/ln2 + o(1)) lnln x, window")
emit("A' L ln x, on the D0 grid.")
emit("D0 substitution for asymptotic columns (the A2 CM-5 convention,")
emit("z = ln x / D at reference D = 2): ln z = (1+o(1)) lnln x,")
emit("lnln z = (1+o(1)) lnlnln x.  Shorthand below: u = lnln x,")
emit("v = lnlnln x.")
emit("Rank-schedule vocabulary for k(x) (the (q14) candidate list, the")
emit("sheet's ceiling classes stated against it): RANK-CONST (k fixed);")
emit("RANK-SQRT ((lnln x)^{1/2}); RANK-ITBELOW (lnln x/lnlnln x, one")
emit("iterated logarithm below the exchange rank); RANK-EXCHANGE")
emit("(beta lnln x, grid reference beta = 2/ln2).")
emit("(P1)/(P2) predicate definitions, verbatim from V-36:")
p12 = V36_BLOCK.split("Per row H emit:\n")[1].split("\nNAME")[0]
for line in p12.split("\n"):
    emit(line)
emit("")

# ================================================================== #
# RC-1 -- SELF-CHECKS (any miss STOP r36.4)
# ================================================================== #
emit("== RC-1/S1a. SELF-CHECK: reproduce the anchored CM-5b table ==")
emit("Anchor: maier_matrix_sheet_29_tables.txt CM-5b (read-only): V(z)")
emit("to 6dp and the distinct-middles margin (ref) to 2dp at C'_k = 1,")
emit("k = 5, T = 5 (the anchor's reference point; T = 5 predates the")
emit("RC-2 coupling and is reproduced here as an anchor check only).")
anch_V = {8: "0.228571", 20: "0.163588", 100: "0.114770", 1000: "0.079316"}
anch_m = {8: "-10.68", 20: "-11.44", 100: "-11.60", 1000: "-11.14"}
Vs = {}
zs = {}
lnxs = {}
llxs = {}
Ls = {}
S1a_pass = True
emit("x        V(z)       margin(ref)   anchored           match")
for e in SCALES:
    lnx, llx, L = regime(e)
    lnxs[e], llxs[e], Ls[e] = lnx, llx, L
    z = lnx / 2
    zs[e] = z
    V = sieve_V(z)
    Vs[e] = V
    mdm = log(mpf(5) / 2) + 5 * log(V * z) - 4 * log(5 * z)
    sV = "{:.6f}".format(float(V))
    sm = "{:.2f}".format(float(mdm))
    ok = (sV == anch_V[e]) and (sm == anch_m[e])
    S1a_pass = S1a_pass and ok
    emit("1e%-5d %s %s %s / %s   %s"
         % (e, sV, fmt(mdm, 13, 2), anch_V[e], anch_m[e],
            "PASS" if ok else "FAIL"))
emit("  -> S1a: %s" % ("PASS" if S1a_pass else "MISS"))
emit("")

emit("== RC-1/S1b. SELF-CHECK: Mertens sanity, as authored ==")
emit("Authored check (kickoff RC-1): |V(z) e^gamma ln z - 1| <= 0.02 at")
emit("z = ln x / 2 for all four scales (sieve product).")
S1b_pass = True
S1b_surr = True
emit("x        V(z)e^g*lnz   |.-1|      <=0.02    <=0.10(surrogate)")
for e in SCALES:
    z = zs[e]
    dev = abs(Vs[e] * EG * log(z) - 1)
    ok = dev <= mpf("0.02")
    oks = dev <= mpf("0.10")
    S1b_pass = S1b_pass and ok
    S1b_surr = S1b_surr and oks
    emit("1e%-5d %s %s   %s      %s"
         % (e, fmt(Vs[e] * EG * log(z), 11, 6), fmt(dev, 9, 6),
            "PASS" if ok else "MISS", "PASS" if oks else "MISS"))
emit("  -> S1b as authored: %s" % ("PASS" if S1b_pass else "MISS"))
emit("Determination: UNSATISFIABLE-AS-AUTHORED.  The deviation is a")
emit("property of the anchored bytes plus finite arithmetic, not of any")
emit("implementation: the anchored CM-5b V(z) column (S1a, reproduced")
emit("exactly) times e^gamma ln z equals 0.9039 / 0.9139 / 0.9702 /")
emit("0.9957, so no implementation can meet 0.02 at the three smaller")
emit("scales -- the Mertens (q9) error term at z = 9.21..115.13 is")
emit("3..10 percent.  The check's sanity function (catch gross errors:")
emit("wrong log base, wrong gamma, off-by-e) is discharged by the")
emit("attainable surrogate tolerance 0.10 above, labeled as the")
emit("executor's surrogate, NOT the authored check.  STOP r36.4 FIRES")
emit("on the authored reading and is resolved as a named deviation of")
emit("the rule-17 unsatisfiable-as-authored class in the run report;")
emit("V-36 makes every grid value reference-only, so no emitted class")
emit("rests on this check in either form.")
emit("")

emit("== RC-1/S1c. SELF-CHECK: formula identity ==")
emit("The sheet's general k-uniform margin function margin_general(k, T,")
emit("ln C, V, z) = ln(k/2) + k ln(V z) - (k-1) ln(T z) - ln C,")
emit("instantiated at (k = 5, T = 5, C'_k = 1), against the S1a margins")
emit("(2dp).")
S1c_pass = True
emit("x        general(5,5,1)   S1a margin   match")
for e in SCALES:
    g = margin_general(mpf(5), mpf(5), mpf(0), Vs[e], zs[e])
    sg = "{:.2f}".format(float(g))
    ok = (sg == anch_m[e])
    S1c_pass = S1c_pass and ok
    emit("1e%-5d %s %s   %s"
         % (e, fmt(g, 14, 2), fmt(mpf(anch_m[e]), 10, 2),
            "PASS" if ok else "FAIL"))
emit("  -> S1c: %s" % ("PASS" if S1c_pass else "MISS"))
emit("")

emit("== RC-1/S1d. Envelope consistency at the grid (reference-only) ==")
emit("Exhibited sufficiency schedule phi_H(x) = (lnln x)^{1/4} (both")
emit("rows, lambda = 2) against the necessity envelope psi_H(x) =")
emit("(3/4) lnln x/lnlnln x (both rows).")
S1d_pass = True
emit("x        u=lnln x   v=lnlnln x   phi_H      psi_H      phi<psi")
for e in SCALES:
    u = llxs[e]
    v = log(u)
    phi = u ** (mpf(1) / 4)
    psi = mpf(3) / 4 * u / v
    ok = phi < psi
    S1d_pass = S1d_pass and ok
    emit("1e%-5d %s %s %s %s   %s"
         % (e, fmt(u), fmt(v, 12), fmt(phi), fmt(psi),
            "PASS" if ok else "FAIL"))
emit("  -> S1d: %s" % ("PASS" if S1d_pass else "MISS"))
emit("")
emit("RC-1 SUMMARY: S1a PASS, S1b MISS-AS-AUTHORED (unsatisfiable;")
emit("surrogate PASS; r36.4 deviation record in the run report), S1c")
emit("PASS, S1d PASS.")
emit("")

# ================================================================== #
# RC-2 -- W-C coupling
# ================================================================== #
emit("== RC-2. W-C coupling (T = lambda c; reference c = 3k) ==")
emit("Reference c = 3k: (q6) chooses c large enough that the (q5)/(q6)")
emit("chain yields >= 3kR primes; the chain's implied constant is")
emit("absolute ((q6)) and its VALUE is undocumented, so c = 3k is the")
emit("reference at absolute constant 1, disclosed undocumented.")
emit("Documented constraints, tabulated: 0 < delta < 1 forces lambda > 1")
emit("((q2)); T > max(2, c) ((q4)) holds since T = lambda c > c and")
emit("T = 3 lambda k > 2 at k >= 1; K = T >= 2 ((q2)).  delta =")
emit("c/T = 1/lambda ((q4) coupling).")
emit("lambda   delta=1/lambda   T at k=5   T at k = beta u (1e1000)")
kref_e = 1000
for lam in [mpf("1.25"), mpf("1.5"), mpf(2), mpf(3)]:
    Tk5 = 3 * lam * 5
    TkL = 3 * lam * BETA * llxs[kref_e]
    emit("%s %s %s %s"
         % (fmt(lam, 6, 2), fmt(1 / lam, 14, 4), fmt(Tk5, 10, 2),
            fmt(TkL, 16, 2)))
emit("Symbolic in the asymptotic columns: lambda > 1 fixed, T =")
emit("3 lambda k, delta = 1/lambda.  Support: RECORDED ((q2)/(q4)/(q6))")
emit("+ PROVED (the tabulated implications are one-line algebra).")
emit("")

# ================================================================== #
# RC-3 -- W-A necessity wall
# ================================================================== #
emit("== RC-3. W-A (Lemma-3 constant + Mertens power): NECESSITY ==")
emit("The k-uniform (q10) margin, decomposed by term (derivation")
emit("displayed in workpaper Section 3.1):")
emit("  margin(k) = ln(k/2) + k ln(V(z) z) - (k-1) ln(T z) - ln C_{k+1}")
emit("  = ln z                      [single surviving positive bulk]")
emit("  + ln(k/2)                   [O(ln k), subdominant]")
emit("  - k (gamma + lnln z - eps(z))   [(q9): ln V(z) = -gamma -")
emit("                               lnln z + eps(z), eps(z) -> 0; the")
emit("                               strict/non-strict product mismatch")
emit("                               (q9) vs (q1) is O(1/z), absorbed]")
emit("  - (k-1)(ln k + ln(3 lambda))    [RC-2 coupling T = 3 lambda k]")
emit("  - ln C_{k+1}                [row H at g = k+1]")
emit("On the D0 substitution the necessity envelope psi_H(x) =")
emit("(3/4) lnln x/lnlnln x kills the margin for every k >= psi_H and")
emit("every fixed lambda > 1, both rows (PROVED, Section 3.1 (N1));")
emit("the critical coefficient is theta*_EXP = 1/2 and theta*_FACT =")
emit("1/(2 + c_H) (Section 3.1 (N2)), lambda-free.")
emit("Grid instantiation (reference-only, MEASURED): margin at the four")
emit("(q14) schedules, lambda = 2 reference (T = 6k), row reference")
emit("constants H-EXP: C = e (ln C_{k+1} = k+1); H-FACT: c_H = 1")
emit("(ln C_{k+1} = (k+1) ln(k+1)); beta = 2/ln2.")
SCHED_NAMES = ["k=5", "k=u^{1/2}", "k=u/v", "k=beta*u"]


def schedules(e):
    u = llxs[e]
    v = log(u)
    return [mpf(5), u ** (mpf(1) / 2), u / v, BETA * u]


for row, lnC_of in [("H-EXP (C=e ref)", lambda k: k + 1),
                    ("H-FACT (c_H=1 ref)", lambda k: (k + 1) * log(k + 1))]:
    emit("row %s:" % row)
    emit("x        " + "".join("%-15s" % n for n in SCHED_NAMES))
    for e in SCALES:
        vals = []
        for k in schedules(e):
            m = margin_general(k, 6 * k, lnC_of(k), Vs[e], zs[e])
            vals.append(fmt(m, 13, 2))
        emit("1e%-5d %s" % (e, " ".join(vals)))
emit("Reading: negative throughout the grid at every schedule --")
emit("consistent with the anchored CM-5b onset finding (divergence onset")
emit("far beyond the grid); no grid sign is load-bearing.  The PROVED")
emit("content is asymptotic: at fixed k the margin tends to +infinity")
emit("(the anchored (q10) conclusion), at k >= psi_H it tends to")
emit("-infinity (this sheet's (P2)).  Support: PROVED (asymptotic")
emit("classes) + MEASURED (grid values, reference-only).")
emit("")

# ================================================================== #
# RC-4 -- W-B sufficiency wall and the uniformization DEBT ledger
# ================================================================== #
emit("== RC-4. W-B (Lemma-4 uniformization): SUFFICIENCY ==")
emit("K_1 = 2K^{1/delta} ((q3)) at the RC-2 coupling K = T, delta =")
emit("1/lambda: K_1 = 2T^lambda = 2(3 lambda k)^lambda.")
emit("PROVED-elementary smooth-count line (proved in workpaper Section")
emit("3.2): the number of K_1-smooth integers in [1, Y] is at most")
emit("(1 + log2 Y)^{pi(K_1)} (exponent-vector count).  It replaces the")
emit("(q3) clause 'at most (log(Kz))^A ... with a suitable A = A(K_1)',")
emit("whose A is undocumented at growing K_1 -- no emitted class rests")
emit("on that clause.")
emit("Sufficiency constraint (the uniformized negligible-clause of the")
emit("(q3) proof at the smallest (7)-window z/log z):")
emit("  pi(K_1) lnln(Kz) <= (1 - eps) ln(delta V(z) z / log z)")
emit("expanded on D0: left side ~ pi(K_1) lnlnln x, right side ~")
emit("(1 - eps) lnln x; with pi(K_1) <= K_1 = 2(3 lambda k)^lambda the")
emit("constraint is k^lambda lnlnln x <~ lnln x, i.e. the per-lambda")
emit("ceiling class")
emit("  k*_{W-B}(x; lambda) = (lnln x/lnlnln x)^{1/lambda}")
emit("(PROVED closure strictly below the class at every fixed lambda >")
emit("1; above it, closure is no longer derivable from the licensed")
emit("pi-inputs -- the CERTIFIED-CLOSURE ceiling, workpaper Section")
emit("3.2; the true boundary is reference-only).")
emit("Ceiling per lambda reference value (class exponent 1/lambda):")
emit("lambda   1/lambda   ceiling class")
for lam in [mpf("1.25"), mpf("1.5"), mpf(2), mpf(3)]:
    emit("%s %s   (lnln x/lnlnln x)^{%s}"
         % (fmt(lam, 6, 2), fmt(1 / lam, 8, 4), fmt(1 / lam, 0, 4)))
emit("Symbolic in lambda: exponent 1/lambda -> 1 as lambda -> 1+ (the")
emit("W-A class); the boundary is DEBT (d5).")
emit("Grid instantiation (reference-only, MEASURED-exact pi): lambda =")
emit("2 reference, K = 6k, K_1 = 2(6k)^2 = 72 k^2; LHS = pi(K_1)")
emit("lnln(Kz); RHS0 = ln(delta V(z) z/log z) (eps = 0 reference).")
emit("row/scale table at the four (q14) schedules:")
emit("x        sched      K_1        pi(K_1)  LHS        RHS0")
lam2 = mpf(2)
maxK1 = 0
cells = []
for e in SCALES:
    for name, k in zip(SCHED_NAMES, schedules(e)):
        K1 = 2 * (3 * lam2 * k) ** lam2
        maxK1 = max(maxK1, int(K1) + 1)
        cells.append((e, name, k, K1))
_plist = primes_upto(maxK1)


def pi_of(x):
    return bisect.bisect_right(_plist, int(x))


for (e, name, k, K1) in cells:
    K = 3 * lam2 * k
    z = zs[e]
    lhs = pi_of(K1) * log(log(K * z))
    rhs = log((1 / lam2) * Vs[e] * z / log(z))
    emit("1e%-5d %-10s %s %8d %s %s"
         % (e, name, fmt(K1, 10, 1), pi_of(K1), fmt(lhs, 10, 2),
            fmt(rhs, 9, 2)))
emit("Reading: the constraint fails at every grid cell (RHS0 is O(1) at")
emit("grid scales while LHS is already large at k = 5) -- the")
emit("sufficiency regime, like the CM-5b divergence onset, lies far")
emit("beyond the grid; reference-only, no grid sign load-bearing.")
emit("")
emit("DEBT LEDGER (each row names the documented clause it suspends; no")
emit("emitted class rests on any row):")
emit("(d1) the (q2) fixed-constants clause ('Let K >= 2 and 0 < delta <")
emit("     1 be fixed constants') under growing K, delta.")
emit("(d2) the (q2) absolute-asymp clause ('the constants implied in")
emit("     the symbol asymp are absolute') under growing K, delta.")
emit("(d3) the (q4) 'z is sufficiently large in terms of T' threshold")
emit("     as T = T(k(x)) grows along a schedule.")
emit("(d4) the unmarked uniformity of 'the prime number theorem for")
emit("     arithmetic progressions' in the (q3) proof as K_1 grows.")
emit("     Finite observation (PROVED range arithmetic): K_1 stays")
emit("     polylog in z on every schedule the sheet prices --")
emit("     ln K_1 / lnln z at k = beta u, lambda = 2:")
for e in SCALES:
    u = llxs[e]
    K1 = 2 * (6 * BETA * u) ** 2
    emit("     1e%-5d ln K_1 = %s, lnln z = %s, ratio %s"
         % (e, fmt(log(K1), 8, 3), fmt(log(log(zs[e])), 8, 3),
            fmt(log(K1) / log(log(zs[e])), 8, 3)))
emit("     (ratio -> lambda = 2 at k = beta u; K_1 is constant at fixed")
emit("     k and polylog in z on every priced schedule).")
emit("(d5) the lambda -> 1 boundary wherever it moves the binding wall")
emit("     (it moves W-B: exponent 1/lambda -> 1).")
emit("")

# ================================================================== #
# RC-5 -- W-D cheap columns
# ================================================================== #
emit("== RC-5. W-D range checks (cheap columns) ==")
emit("(a) R >= 2k ((q7)): ln R = (D-1) theta(z) at D = 2 vs ln(2k),")
emit("    per schedule.")
emit("(b) T <= z, i.e. Tz <= z^2 ((q1) spacing via (q8)): T = 6k at")
emit("    lambda = 2 reference vs z.")
emit("(c) Lemma-1 range x = q^D: met by construction ((q5) environment,")
emit("    x = P(z)^D).  RECORDED, k-free.")
emit("(d) (7)-window length: Tz >= z/log z iff T >= 1/log z; T > 2")
emit("    ((q4)) closes it.  PROVED, k-free.")
emit("Per schedule at the grid (lambda = 2 reference; schedule order")
emit("k = 5 / u^{1/2} / u/v / beta u; P = PASS, F = FAIL):")
emit("x        ln R       z          (a) per schedule   (b) per schedule")
for e in SCALES:
    z = zs[e]
    lnR = theta(z)
    a_marks = []
    b_marks = []
    for k in schedules(e):
        a_marks.append("P" if lnR > log(2 * k) else "F")
        b_marks.append("P" if 6 * k <= z else "F")
    emit("1e%-5d %s %s %-18s %s"
         % (e, fmt(lnR, 10, 2), fmt(z, 10, 2),
            "/".join(a_marks), "/".join(b_marks)))
emit("Asymptotically (PROVED): (a) closes at every schedule k = O(u)")
emit("since ln R ~ z ((q5) display) while ln 2k = O(ln u); (b) closes")
emit("since T = 3 lambda k = O(lnln x) = o(z); (d) closes since T > 2.")
emit("Grid reading: (b) FAILS at most schedules on the two small scales")
emit("(z = 9.21 / 23.03 there sits below T = 6k already at k = 5) and")
emit("clears from 1e100 -- late scale entry, the same pattern as the")
emit("RC-3/RC-4 onsets; reference-only, no grid sign load-bearing.")
emit("Asymptotically W-D never binds on any priced schedule.")
emit("")

# ================================================================== #
# RC-6 -- assembly and verdict
# ================================================================== #
emit("== RC-6. Assembly and verdict ==")
emit("Per-row exhibits (PROVED in workpaper Section 3; S1d grid check):")
emit("  H-EXP:  phi_EXP(x) = (lnln x)^{1/4} at lambda = 2 (every RC-2..")
emit("          RC-5 step closes); psi_EXP(x) = (3/4) lnln x/lnlnln x.")
emit("  H-FACT: phi_FACT(x) = (lnln x)^{1/4} at lambda = 2 (same")
emit("          coupling; the row constant is o(lnln x) there);")
emit("          psi_FACT(x) = (3/4) lnln x/lnlnln x.")
emit("Binding walls: necessity W-A (lambda-free, theta*_EXP = 1/2,")
emit("theta*_FACT = 1/(2+c_H)); sufficiency W-B (per fixed lambda,")
emit("class (lnln x/lnlnln x)^{1/lambda}; lambda -> 1 boundary = d5).")
emit("FLAG guard: NO FLAG (record in workpaper Section 7).")
emit("")
for line in V36_BLOCK.split("\n"):
    emit(line)
emit("")
for line in V36_APPLICATION.split("\n"):
    emit(line)
emit("")
emit("END OF RANK CEILING SHEET 36")

with open(__file__.replace("rank_ceiling_sheet_36.py",
                           "rank_ceiling_sheet_36_tables.txt"), "w") as f:
    f.write("\n".join(OUT) + "\n")
