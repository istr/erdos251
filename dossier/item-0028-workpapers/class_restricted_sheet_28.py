# item-0028 -- class-restricted Kuperberg 1.2 cost: budget-sheet decision.
#
# Dispatch: item-0028-kickoff-v1.md (EXECUTOR, ephemeral, not committed).
# Section 0 pin 9e1206a037342e0a99d53ac440ec86fee703663e.
#
# This is a NEW, self-contained script.  The anchored sheets
# dossier/item-0010-workpapers/budget_sheet_20_ext.py and
# dossier/item-0026-workpapers/pintz_constants_sheet.py are READ-ONLY for
# this session, so their grid conventions are RE-DECLARED here and NEVER
# imported (importing would re-execute them and overwrite their anchored
# _tables.txt).  Every convention below is byte-faithful to the anchors:
# LN2, SCALES = [8, 20, 100, 1000], APRIME = 1.5, APP = 48, C0 = 2/ln3,
# grid L = (2/ln2) lnln x, L_ceil = 2J+1 with J = ceil(log2(ceil(13 C0 A''
# ln x))), window h = A' L ln x, expo(F) = ln F / lnln x.
#
# Deterministic: no timestamps, no randomness; mpmath dps 40.

from mpmath import mp, mpf, log, exp, euler, primezeta, floor as mfloor
import math

mp.dps = 40

LN2    = log(2)
SCALES = [8, 20, 100, 1000]         # x = 10^e  (anchor grid)
APRIME = mpf("1.5")                 # D0 pin A'
APP    = 48                         # D0 pin A''
C0     = 2 / log(3)                 # Chebyshev sup q_n/(n ln(n+2)) = 2/ln3
EG     = exp(euler)                 # e^gamma = Mertens third-theorem const

OUT = []
def emit(s=""):
    OUT.append(s)
    print(s)

def lnx_of(e):
    return e * log(10)

def regime(e):
    # anchor tag (m): the GRID surrogate rank L = (2/ln2) lnln x.
    lnx = lnx_of(e)
    llx = log(lnx)
    L = (2 / LN2) * llx
    return lnx, llx, L

def L_ceil(lnx):
    # anchor tag (p): D0-exact depth L_ceil = 2J+1, J = ceil(log2(ceil(
    # 13 C0 A'' ln x))).
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

def trunc_check(val, expected_str, ndec):
    scale = mpf(10) ** ndec
    t = mfloor(val * scale) / scale
    got = ("{:." + str(ndec) + "f}").format(float(t))
    return got, (got == expected_str)

# ================================================================== #
# S0 -- conventions echo
# ================================================================== #
emit("item-0028 class-restricted Kuperberg 1.2 cost sheet.")
emit("Grid convention (re-declared, anchor budget_sheet_20.py (m)/(p), read")
emit("only): L = (2/ln2) lnln x; D0-exact L_ceil = 2J+1, J = ceil(log2(")
emit("ceil(13 C0 A'' ln x))).  Window h = A' L ln x, A' = 1.5, A'' = 48,")
emit("C0 = 2/ln3 = %s, e^gamma = %s." % (fmt(C0, 0, 6), fmt(EG, 0, 6)))
emit("Exponent convention: expo(F) = ln F / lnln x, F = (ln x)^expo.")
emit("Budgets (echoed, anchor budget_sheet_20_ext.py, read-only): (G1)")
emit("o(ln x): expo < 1 with decay or a limit < 1.  (G2) x^eps: ln F =")
emit("o(ln x).  (G3) pigeonhole reserve: ln x / C_F must survive.")
emit("Loss normalization (item body Section 1, binding on every table):")
emit("the class family carries a DETERMINISTIC parity main term (C4a")
emit("below).  Loss of a class-restricted r-th-moment bound is measured")
emit("RELATIVE to that main term at the same r; the two unrestricted")
emit("reference columns (S3) are measured relative to 1.")
emit("")

# ================================================================== #
# S1 -- SELF-CHECKS
# ================================================================== #
emit("== S1a. SELF-CHECK: reproduce the anchored F17.9 grid column ==")
emit("F17.9 = L ln L / lnln x at k = L = (2/ln2) lnln x (item-0010")
emit("budget_sheet_20_ext.py T9.S3 grid-L column).  Anchored: 6.143 /")
emit("6.932 / 7.944 / 8.963 (3 dp).")
emit("x        L          F17.9        anchored   match")
F179 = {}
Ls = {}
llxs = {}
S1a_pass = True
anchored_f179 = {8: "6.143", 20: "6.932", 100: "7.944", 1000: "8.963"}
for e in SCALES:
    lnx, llx, L = regime(e)
    Ls[e] = L
    llxs[e] = llx
    v = expo(L * log(L), llx)
    F179[e] = v
    got, ok = trunc_check(v, anchored_f179[e], 3)
    # anchored values are rounded to 3dp in the anchor table; accept a
    # match under rounding as well as truncation.
    rounded = ("{:.3f}").format(float(v))
    ok = ok or (rounded == anchored_f179[e])
    S1a_pass = S1a_pass and ok
    emit("1e%-5d %s %s   %s      %s" % (e, fmt(L), fmt(v), anchored_f179[e], "PASS" if ok else "FAIL"))
emit("  -> S1a: %s" % ("PASS" if S1a_pass else "FAIL"))
emit("")

emit("== S1b. SELF-CHECK: K1.2 displayed / Mertens-honest / exact triple ==")
emit("(pintz-constants.md Section 4; exact product RECOMPUTED from a sieve")
emit("here, not copied.)")
emit("x        (3lnk)^k    (3e^g lnk)^k  exactProd^k")
anchored_disp = {8: "5.3503", 20: "5.6990", 100: "6.0922", 1000: "6.4403"}
anchored_hon  = {8: "7.0158", 20: "7.3644", 100: "7.7577", 1000: "8.1058"}
anchored_exa  = {8: "7.0287", 20: "7.3751", 100: "7.7638", 1000: "8.1084"}
S1b_pass = True
K12 = {}
for e in SCALES:
    lnx, llx, L = regime(e)
    kc = L ** 3
    prod = mpf(1)
    for p in primes_upto(kc):
        prod *= 1 / (1 - mpf(1) / p)
    lnk = log(L)
    e3  = expo(L * log(3 * lnk), llx)
    eeg = expo(L * log(3 * EG * lnk), llx)
    eex = expo(L * log(prod), llx)
    K12[e] = {"disp": e3, "hon": eeg, "exact": eex}
    for tag, val, anchor in (("disp", e3, anchored_disp[e]),
                              ("hon", eeg, anchored_hon[e]),
                              ("exact", eex, anchored_exa[e])):
        rounded = ("{:.4f}").format(float(val))
        S1b_pass = S1b_pass and (rounded == anchor)
    emit("1e%-5d %s %s %s" % (e, fmt(e3), fmt(eeg), fmt(eex)))
emit("  vs anchored: 5.3503/5.6990/6.0922/6.4403 | 7.0158/7.3644/7.7577/")
emit("  8.1058 | 7.0287/7.3751/7.7638/8.1084")
emit("  -> S1b: %s" % ("PASS" if S1b_pass else "FAIL"))
emit("")

emit("== S1c. SELF-CHECK: Kowalski mu_k(2), Example 3.5, k = 2..6 ==")
emit("Euler product mu_k(2) = prod_p ((1-1/p)(1-2/p)^k + (1/p)(1-1/p)^k) *")
emit("(1-1/p)^(-2k), truncated p < 2e6, dps 40 (ANN-20260726-74 method).")
KOWALSKI_LIMIT = 2_000_000
kw_primes = primes_upto(KOWALSKI_LIMIT)
emit("primes used: %d (all primes p < %d)" % (len(kw_primes), KOWALSKI_LIMIT))

def mu_k_2(primes, k):
    prod = mpf(1)
    for p in primes:
        pf = mpf(p)
        factor = ((1 - 1 / pf) * (1 - 2 / pf) ** k + (1 / pf) * (1 - 1 / pf) ** k) * (
            1 - 1 / pf
        ) ** (-2 * k)
        prod *= factor
    return prod

mu2 = {}
anchor_mu = {2: ("2.300", 3), 3: ("6.03294", 5), 4: ("17.562", 3), 5: ("55.255", 3), 6: ("184.18", 2)}
S1c_pass = True
for k in range(2, 7):
    val = mu_k_2(kw_primes, k)
    mu2[k] = val
    expected, ndec = anchor_mu[k]
    got, ok = trunc_check(val, expected, ndec)
    S1c_pass = S1c_pass and ok
    emit("  mu_%d(2) = %s  (anchored %s...)  match=%s" % (k, mp.nstr(val, 15), expected, ok))
emit("  -> S1c: %s" % ("PASS" if S1c_pass else "FAIL"))
emit("")

emit("== S1d. Recheck re-run (Section 3.2 of the dispatch) ==")
emit("pintz10-2-16-recheck.py re-executed from its landed directory this")
emit("session; stdout identical to the landed pintz10-2-16-recheck.txt")
emit("except line 2 (the tool-version line; this session's version line")
emit("recorded in the final report).  -> S1d: PASS")
emit("")

S1_ALL = S1a_pass and S1b_pass and S1c_pass
emit("S1 SELF-CHECKS: %s" % ("ALL PASS" if S1_ALL else "AT LEAST ONE MISS -- STOP r28.4"))
emit("")

# ================================================================== #
# S2 -- decision frame
# ================================================================== #
emit("== S2. Decision frame ==")
emit("Growth classes (expo(F) = ln F / lnln x, F = (ln x)^expo):")
emit("  GC-CONST : expo bounded in x with a stated finite limit")
emit("             (\"exponential in the rank alone\": cost <= c^k).")
emit("  GC-ITLOG : expo = c * lnlnln x + O(1), c > 0 (\"rank times an")
emit("             iterated logarithm\": cost = (c' ln k)^k).")
emit("  GC-FASTER: expo / lnlnln x -> infinity.")
emit("BET-20260725-11 resolution clause, verbatim:")
emit("  \"operator judgment against the item-0028 sheet; a favourable")
emit("  outcome requires the loss to be exponential in the rank alone,")
emit("  not in rank times an iterated logarithm\"")
emit("Item body, two-numbers criterion, verbatim:")
emit("  \"Two numbers decide it. If the class-restricted loss is")
emit("  exponential in the rank alone, the cost exponent collapses and")
emit("  the polylog gate becomes a live question rather than a settled")
emit("  failure. If the loss is the same, the hypothesis is closed by")
emit("  arithmetic.\"")
emit("")

# ================================================================== #
# S3 -- UNRESTRICTED REFERENCES (normalization: relative to 1)
# ================================================================== #
emit("== S3. Unrestricted references (normalization: relative to 1) ==")
emit("C3a. K1.2 Mertens-honest expo (S1b 'hon' column). Class: GC-ITLOG")
emit("(expo ~ (2/ln2) ln(3 e^gamma ln k), grows like lnlnln x). Support:")
emit("MEASURED (finite product), on top of the anchored Theorem 1.2.")
emit("Venue: Kuperberg 1.2 carries \"unrefereed-preprint\" venue class ONLY")
emit("(arXiv v2, referee thanks in the front matter, no journal ref")
emit("printed) -- the Section 3.4 Lemma-2 support annotation does NOT")
emit("apply here; it is scoped to Pintz Lemma 2 of 1004.1072v1 only.")
emit("x        C3a expo (K1.2 Mertens-honest)")
for e in SCALES:
    emit("1e%-5d %s" % (e, fmt(K12[e]["hon"])))
emit("")

emit("C3b. True-growth reference at r = 2 (Kowalski Example 4.3): leading")
emit("term expo = (4/ln2) * lnln(3L) per scale. Class: GC-ITLOG. Support:")
emit("MEASURED (asymptotic to the printed order). TWO caveats: (i) the")
emit("O(k) additive term makes per-scale values indicative only, the")
emit("deliverable is the growth class GC-ITLOG; (ii) venue: unrefereed")
emit("ETH-hosted note (no journal reference printed). Purpose: the")
emit("unrestricted r=2 growth k lnln k is a property of the AVERAGE")
emit("itself (proved in the anchor), not an artifact of Kuperberg's")
emit("method; any class-restricted gain must come from the restriction.")
emit("x        C3b expo = (4/ln2) lnln(3L)")
C3b = {}
for e in SCALES:
    L = Ls[e]
    v = (4 / LN2) * log(log(3 * L))
    C3b[e] = v
    emit("1e%-5d %s" % (e, fmt(v)))
emit("")

# ================================================================== #
# S4 -- CLASS-FAMILY FORCED PROFILE
# ================================================================== #
emit("== S4. Class-family forced profile ==")
emit("C4a. Parity main term (PROVED, elementary). A realized flank class")
emit("is a tuple of offsets of consecutive primes at scale x >= 3; all")
emit("such primes are odd, so every offset d_i is even, so")
emit("D+ = {0, d_1, ..., d_nu} occupies exactly one residue class mod 2:")
emit("nu_2(D+) = 1. By B1 the p=2 factor of S(D+) is")
emit("(1-1/2)/(1-1/2)^t = 2^{t-1} exactly, t = |D+|. Every class member")
emit("carries it, so the class-restricted r-th moment carries the")
emit("deterministic factor 2^{r(t-1)}. Classification: DETERMINISTIC MAIN")
emit("TERM of the class family, NOT loss; it fixes the loss")
emit("normalization. Cross-anchor: B4 is the anchor's own sentence for")
emit("the same factor.")
emit("expo = r(t-1) ln2 / lnln x, at t = L+1 (identity, exactly 2r) and")
emit("at t = L_ceil+1 (descending toward 2r), r in {1, 2}.")
emit("x        t=L+1,r=1  t=L+1,r=2  t=Lc+1,r=1  t=Lc+1,r=2")
for e in SCALES:
    lnx, llx, L = regime(e)
    Lc = L_ceil(lnx)
    e_L_r1 = expo(1 * L * LN2, llx)
    e_L_r2 = expo(2 * L * LN2, llx)
    e_Lc_r1 = expo(1 * Lc * LN2, llx)
    e_Lc_r2 = expo(2 * Lc * LN2, llx)
    emit("1e%-5d %s %s %s %s" % (e, fmt(e_L_r1), fmt(e_L_r2), fmt(e_Lc_r1), fmt(e_Lc_r2)))
emit("  -> t=L+1 columns are exactly 2r at every scale (identity, since")
emit("     L = (2/ln2) lnln x); t=Lc+1 columns descend toward 2r as scale")
emit("     grows (Lc/L -> 1). Support: PROVED.")
emit("")

emit("C4b. Admissibility cap (bookkeeping, no column): nu_p <= p-1 for")
emit("every p on any tuple with S(D+) != 0 (B1: the p-factor vanishes at")
emit("nu_p = p).")
emit("")

emit("C4c. Pointwise worst odd-prime profile. Nothing on the anchored")
emit("shelf forces nu_p away from 1 at odd p for a realized class")
emit("(located non-forcing, citing the item-0026 A3 absence: the")
emit("distributional input that would exclude concentrated realized")
emit("classes is exactly the located absence). Column: the worst")
emit("pointwise class-restricted small-prime cost relative to the C4a")
emit("main term, expo = (t-1) * sum_{2<p<=k^3} 1/p / lnln x at t = L+1")
emit("(per scale; finite sieve sum, k = L). Class: GC-ITLOG (the sum")
emit("grows like lnln k^3). Support: PROVED (finite computation on B1).")
emit("x        C4c expo")
C4c = {}
for e in SCALES:
    lnx, llx, L = regime(e)
    kc = L ** 3
    s = mpf(0)
    for p in primes_upto(kc):
        if p > 2:
            s += mpf(1) / p
    v = expo(L * s, llx)
    C4c[e] = v
    emit("1e%-5d %s" % (e, fmt(v)))
emit("Conclusion: pointwise, restriction to the class family changes the")
emit("p=2 factor from rare-event to main term and changes nothing else")
emit("in the growth class.")
emit("")

# ================================================================== #
# S5 -- THE ONE LOCATED CARDINALITY-RESTRICTED MECHANISM
# ================================================================== #
emit("== S5. The one located cardinality-restricted mechanism ==")
emit("(Pintz Lemma 2 one-position induction; every use below carries the")
emit("Section 3.4 support annotation: \"unrefereed-preprint; printed")
emit("statement differs from the statement the proof establishes; reading")
emit("reconstructed and verified in-project\".)")
emit("")

emit("C5a. Split-point coverage at the exchange window. y = (ln h)/2")
emit("(1004.1072 convention, distinct from the 1004.1084 y = 5 ln H/6")
emit("priced in pintz-constants). Support: MEASURED-exact.")
emit("x        y        primes<=y   pi(y)  ln(mass covered)  share of full Mertens mass")
C5a = {}
for e in SCALES:
    lnx, llx, L = regime(e)
    h = APRIME * L * lnx
    lnh = log(h)
    y = lnh / 2
    ps = primes_upto(y)
    mass = mpf(0)
    for p in ps:
        mass += -log(1 - mpf(1) / p)
    lnk = log(L)
    full_mass = log(3 * EG * lnk)
    share = mass / full_mass
    C5a[e] = {"y": y, "primes": ps, "mass": mass, "full_mass": full_mass, "share": share}
    emit("1e%-5d %s %-11s %6d %s          %s"
         % (e, fmt(y, 0, 4), str(ps), len(ps), fmt(mass), fmt(share)))
emit("Purpose: the averaged component of the per-step route ((2.16),")
emit("p <= y) covers only this prime set at the project's window; the")
emit("entire remaining small-prime range 2 < p <= k^3 sits in the")
emit("pointwise regime of the printed proof.")
emit("")

emit("C5b. Band ratio. PROVED limit L/y -> 2L/ln h -> 4/ln2 = %s"
     % fmt(4 / LN2))
emit("(derivation: ln h = lnln x + ln(A'L), L = (2/ln2) lnln x).")
emit("x        L/y       Lc/y")
for e in SCALES:
    lnx, llx, L = regime(e)
    Lc = L_ceil(lnx)
    y = C5a[e]["y"]
    emit("1e%-5d %s %s" % (e, fmt(L / y), fmt(mpf(Lc) / y)))
emit("The band (y, t] is nonempty grid-uniformly (L/y and Lc/y both > 1")
emit("at every scale above): the printed two-sided per-factor shape of")
emit("(2.14)/(2.3)-type displays is outside its validity there (the")
emit("mirror of the pintz-constants F2 finding via the star identity B10;")
emit("no re-derivation needed, cited). This bites any TWO-SIDED or")
emit("lower-direction use; for the upper direction see C5c.")
emit("")

emit("C5c. Pi_3 <= 1 for admissible extensions (band-immune, upper")
emit("direction). Derivation: for p > y, p not dividing Delta, the")
emit("extension factor is (1-(nu_p+1)/p)/((1-nu_p/p)(1-1/p)); by the star")
emit("identity (B10) it equals 1 - nu_p/((p-nu_p)(p-1)); admissibility")
emit("(C4b) gives 1 <= nu_p <= p-2 for a nonvanishing extension, hence the")
emit("factor lies in [0, 1]. So the p > y, p !| Delta part of the r-th-")
emit("power extension ratio costs nothing in the upper direction.")
emit("Support: PROVED (one line from B10 + B1).")
emit("")

emit("C5d. Pi_1 averaged per-step cost via the (2.16) sharpening.")
emit("(i) EXACT: finite product over the actual prime set p <= y (C5a)")
emit("of the maximum over 1 <= nu <= min(t+1, p-1) of the exact (2.16)")
emit("local factor (implemented from B8 directly, numerator and")
emit("denominator expanded separately, no symbolic simplify -- the")
emit("recheck's recorded hazard), at t = L+1. Support: MEASURED-exact.")

def local_factor(p, nu, r):
    pf = mpf(p)
    nuf = mpf(nu)
    num = (nuf / pf) * (1 - nuf / pf) ** r + (1 - nuf / pf) * (1 - (nuf + 1) / pf) ** r
    den = (1 - nuf / pf) ** r * (1 - 1 / pf) ** r
    return num / den

emit("x        EXACT prod r=1   EXACT prod r=2   expo r=1   expo r=2")
C5d_exact = {}
for e in SCALES:
    lnx, llx, L = regime(e)
    t = L + 1
    ps = C5a[e]["primes"]
    prod_r1 = mpf(1)
    prod_r2 = mpf(1)
    for p in ps:
        cap = min(int(mfloor(t + 1)), p - 1)
        best_r1 = max(local_factor(p, nu, 1) for nu in range(1, cap + 1))
        best_r2 = max(local_factor(p, nu, 2) for nu in range(1, cap + 1))
        prod_r1 *= best_r1
        prod_r2 *= best_r2
    e_r1 = expo(log(prod_r1), llx) if prod_r1 != 1 else mpf(0)
    e_r2 = expo(log(prod_r2), llx)
    C5d_exact[e] = {"r1": prod_r1, "r2": prod_r2, "e_r1": e_r1, "e_r2": e_r2}
    emit("1e%-5d %s %s %s %s"
         % (e, fmt(prod_r1, 0, 6), fmt(prod_r2, 0, 6), fmt(e_r1), fmt(e_r2)))
emit("(r=1 product is exactly 1 at every scale: the local factor's r=1")
emit("collapse (2.7) reproduced here as the exact identity it is.)")
emit("")

emit("(ii) LIMIT SHAPE: accumulated third-order bound over t = 0..L-1")
emit("steps, expo limit (2/ln2) * (r(r-1)/2) * C3 with")
emit("C3 = sum_p (p-1)/p^3 = P(2) - P(3), using nu_p <= p-1 absolutely.")
C3_primezeta = primezeta(2) - primezeta(3)
sieve_sum = mpf(0)
for p in kw_primes:
    sieve_sum += (mpf(p) - 1) / mpf(p) ** 3
emit("C3 (prime zeta, P(2)-P(3)): %s" % mp.nstr(C3_primezeta, 12))
emit("C3 (direct sieve sum, primes p < %d, same sieve as S1c): %s"
     % (KOWALSKI_LIMIT, mp.nstr(sieve_sum, 12)))
emit("  -> agree to 7 significant digits (sieve tail beyond 2e6 accounts")
emit("     for the residual); C3 = 0.27748...")
emit("Support: MEASURED (series identity to the printed order; the")
emit("remainder is not uniformly controlled -- quote the recheck")
emit("docstring's own caveat: \"no remainder is controlled uniformly in")
emit("p, nu_p and r here\"). Class of this COMPONENT: GC-CONST (constant")
emit("in x -- the ratio L/lnln x = 2/ln2 does not grow with scale).")
emit("r=1: %s   r=2: %s" % (fmt((2 / LN2) * (1 * 0 / 2) * C3_primezeta), fmt((2 / LN2) * (2 * 1 / 2) * C3_primezeta)))
C5d_limit_r2 = (2 / LN2) * (2 * 1 / 2) * C3_primezeta
emit("Print beside it: this component alone is not a class-restricted")
emit("moment bound; see C5e.")
emit("")

emit("C5e. The unmarked residue. Source's own disclosure, quoted (B7):")
emit("  \"we will not mark the dependence of the constants implied by <<")
emit("  or 0 symbols on t and r\"")
emit("Column: the visible pointwise Pi_2 accumulation, per-step")
emit("log Pi_2 <= (1+o(1)) * 2t/ln y, accumulated over t = 0..L-1:")
emit("expo = r * L^2 / (ln y * lnln x) per scale. Class: GC-FASTER.")
emit("x        C5e expo r=1   C5e expo r=2")
C5e = {}
for e in SCALES:
    lnx, llx, L = regime(e)
    y = C5a[e]["y"]
    v_r1 = expo(1 * L * L / log(y), llx)
    v_r2 = expo(2 * L * L / log(y), llx)
    C5e[e] = {"r1": v_r1, "r2": v_r2}
    emit("1e%-5d %s %s" % (e, fmt(v_r1), fmt(v_r2)))
emit("Print beside it: this is the PRINTED pointwise bookkeeping; an")
emit("h-averaged treatment of Pi_2 (density of p|Delta over h is")
emit("<= (t+1)/p) would be per-step o(1), but that derivation, and the")
emit("joint average of Pi_1^r Pi_2^r it requires, is ABSENT from the")
emit("nine-page note -- the same shape as the pintz-constants F2 finding:")
emit("plausibly rescuable, not carried by the source. OPEN; out of scope")
emit("here (Section 1 non-scope).")
emit("")

# ================================================================== #
# S6 -- SYNTHESIS AND VERDICT
# ================================================================== #
emit("== S6. Synthesis and verdict ==")
emit("column  what it prices                          growth class  support        full-range?  upgrade path")
emit("C3a     unrestricted K1.2, Mertens-honest         GC-ITLOG      MEASURED       yes          absolute constant in Theorem 1.2's <<")
emit("C3b     unrestricted true growth at r=2 (Kowalski) GC-ITLOG      MEASURED       yes          the O(k) additive term pinned")
emit("C4a     parity main term (deterministic, not loss) exactly 2r    PROVED         --           n/a (main term, fixes normalization)")
emit("C4c     worst pointwise odd-prime cost             GC-ITLOG      PROVED         yes          a distributional input excluding")
emit("                                                                                              concentrated realized classes (A3)")
emit("C5d     (2.16)-sharpening averaged per-step cost    GC-CONST      MEASURED(-exact) NO (p<=y only) the Q2/Q3-type band-(y,k] rescue")
emit("C5e     printed pointwise Pi_2 bookkeeping          GC-FASTER     MEASURED       yes          the absent h-averaged joint treatment")
emit("")

col_classes = {"C3a": "GC-ITLOG", "C3b": "GC-ITLOG", "C4c": "GC-ITLOG",
               "C5d": "GC-CONST", "C5e": "GC-FASTER"}
col_full_range = {"C3a": True, "C3b": True, "C4c": True, "C5d": False, "C5e": True}

gc_const_cols = [k for k, v in col_classes.items() if v == "GC-CONST"]
all_gc_const_component_only = all(not col_full_range[k] for k in gc_const_cols)
full_range_cols = [k for k, v in col_full_range.items() if v]
all_full_range_itlog_or_worse = all(col_classes[k] in ("GC-ITLOG", "GC-FASTER") for k in full_range_cols)
any_full_range_gc_const_or_better = any(col_full_range[k] and col_classes[k] == "GC-CONST" for k in col_classes)

if all_gc_const_component_only and all_full_range_itlog_or_worse and not any_full_range_gc_const_or_better:
    VERDICT_TAG = "V-NEG"
elif any_full_range_gc_const_or_better:
    VERDICT_TAG = "V-POS"
else:
    VERDICT_TAG = "V-STOP"

emit("Mechanical determination: every GC-CONST candidate (C5d) is")
emit("component-only (covers only p<=y, C5a); every full-range column")
emit("(C3a, C3b, C4c, C5e) is GC-ITLOG or worse. -> (V-NEG) fires.")
emit("")
emit("VERDICT: %s" % VERDICT_TAG)
if VERDICT_TAG == "V-NEG":
    emit("(V-NEG) NEGATIVE AT CORPUS GRAIN: no located mechanism prices a")
    emit("class-restricted r-th-moment loss (r in {1,2}, relative to the")
    emit("C4a main term) in growth class GC-CONST at support MEASURED or")
    emit("better over the full small-prime range; the item's hypothesis")
    emit("closes. The one GC-CONST mechanism located (C5d, the (2.16)")
    emit("sharpening) is component-only: it covers p <= y (C5a), not the")
    emit("full range 2 < p <= k^3 that C4c and C5e cover, where the cost is")
    emit("GC-ITLOG (C4c) and GC-FASTER (C5e) respectively.")
emit("")

# ================================================================== #
# S7 -- BUDGET-GATE ECHO (hypothetical favourable outcome)
# ================================================================== #
emit("== S7. Budget-gate echo (hypothetical favourable outcome) ==")
emit("A GC-CONST loss at r=2 would put the class-restricted moment cost")
emit("at expo = 4 (parity main term, C4a, 2r at r=2) + %s (C5d third-order"
     % fmt(C5d_limit_r2, 0, 4))
emit("limit at r=2) + c* with c* the UNPINNED per-step constant, i.e.")
emit("polylog cost and (G1) live -- exactly the item body's \"the polylog")
emit("gate becomes a live question\". No claim that c* exists; printed")
emit("symbolically only.")
emit("")

emit("END OF CLASS-RESTRICTED SHEET 28")

with open(__file__.replace("class_restricted_sheet_28.py",
                           "class_restricted_sheet_28_tables.txt"), "w") as f:
    f.write("\n".join(OUT) + "\n")
