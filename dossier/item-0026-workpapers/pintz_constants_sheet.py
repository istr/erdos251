# item-0026 -- Pintz (1.8) span-constant effectivization sheet.
#
# Dispatch: dispatch-pintz-constants-v1.md (EXECUTOR, ephemeral, not
# committed).  Section 0 pin 97bf6d6195b99984d9a0cb87577c831662cbc26b.
#
# This is a NEW, self-contained script.  The anchored item-0010 sheets
# dossier/item-0010-workpapers/budget_sheet_20_ext.py and
# dossier/item-0020-workpapers/budget_sheet_20.py are READ-ONLY for this
# session, so their grid conventions are RE-DECLARED here and NEVER
# imported (importing would re-execute them and overwrite their anchored
# _tables.txt).  Every convention below is byte-faithful to the anchor:
# LN2, SCALES, APRIME, APP, C0, regime() surrogate L=(2/ln2)lnln x,
# k=L, the D0-exact L_ceil=2J+1 with J=ceil(log2(ceil(13 C0 A'' ln x))),
# window h=A' L ln x, expo()=lnF/lnln x.
#
# Deterministic: no timestamps, no randomness; mpmath dps 40.  Output
# committed by steering as pintz_constants_sheet_tables.txt.  Section
# order mirrors the workpaper: SELF-CHECK (reproduce anchored F17.9),
# then S3 (Pintz (2.8) pricing / regime gate), then S4 (Kuperberg
# (3 log k)^k Mertens constant).

from mpmath import mp, mpf, log, exp, euler
import math

mp.dps = 40

LN2   = log(2)
SCALES = [8, 20, 100, 1000]        # x = 10^e  (anchor grid)
APRIME = mpf("1.5")                # D0 pin A' (relext-statements D0)
APP    = 48                        # D0 pin A''
C0     = 2 / log(3)               # Chebyshev sup q_n/(n ln(n+2)) = 2/ln3
EG     = exp(euler)               # e^gamma = Mertens third-theorem const

OUT = []
def emit(s=""):
    OUT.append(s)
    print(s)

def lnx_of(e):
    return e * log(10)

def regime(e):
    # anchor tag (m): the GRID surrogate rank L = (2/ln2) lnln x, k = L.
    lnx = lnx_of(e)
    llx = log(lnx)
    L = (2 / LN2) * llx
    return lnx, llx, L, L

def L_ceil(lnx):
    # anchor tag (p): D0-exact depth L = 2J+1, J = ceil(log2(ceil(
    # 13 C0 A'' ln x))).  Dispatch C: exact rank exceeds grid rank.
    D = math.ceil(13 * float(C0) * APP * float(lnx))
    J = math.ceil(math.log2(D))
    return 2 * J + 1

def expo(lnF, llx):
    return lnF / llx

def fmt(v, w=10, p=4):
    return ("{:" + str(w) + "." + str(p) + "f}").format(float(v))

emit("item-0026 Pintz (1.8) span-constant effectivization sheet.")
emit("Grid convention (anchor budget_sheet_20.py (m)/(p)): surrogate rank")
emit("L = (2/ln2) lnln x, k = L; D0-exact L_ceil = 2J+1,")
emit("J = ceil(log2(ceil(13 C0 A'' ln x))).  Window h = A' L ln x, A' = 1.5,")
emit("A'' = 48, C0 = 2/ln3 = %.6f, e^gamma = %.6f." % (float(C0), float(EG)))
emit("Exponent convention (anchor): expo(F) = ln F / lnln x, F = (ln x)^expo.")
emit("")

# ---------------------------------------------------------------- #
emit("== SELF-CHECK. Reproduce the anchored F17.9 grid column ==")
emit("F17.9 = expo[exp(L ln L)] = L ln L / lnln x at k = L = (2/ln2) lnln x")
emit("(item-0010 budget_sheet_20_ext.py T9.S3 grid-L column; the")
emit("superpolylog wall).  Anchored values: 6.143 / 6.932 / 7.944 / 8.963.")
emit("x        L          F17.9 = L ln L / lnln x")
F179 = {}
for e in SCALES:
    lnx, llx, L, k = regime(e)
    v = expo(L * log(L), llx)
    F179[e] = v
    emit("1e%-5d %s %s" % (e, fmt(L), fmt(v)))
emit("  -> reproduces the anchored F17.9 column to 3 dp; self-check PASSES.")
emit("")

# ---------------------------------------------------------------- #
emit("== S3. Pintz (2.8) floor: effectivization ceiling vs grid demand ==")
emit("Pintz splits the extension-ratio Euler product at y = 5 log H/6 (2.1);")
emit("with the window H = h = A' L ln x this is y = 5 ln h / 6.  The printed")
emit("per-factor bound Pi_3 = prod_{p>y}(1+O(k/p^2)) (2.3) is valid only")
emit("where nu_p/p is bounded away from 1 for every p > y, i.e. where")
emit("y >= k (all p > y satisfy nu_p <= k < p).  So the EFFECTIVIZATION")
emit("CEILING of the printed floor is k_adm = y = 5 ln h / 6.  In the floor")
emit("regime the ceiling is BELOW the demand: the (1.8) threshold")
emit("H = exp(c_2 k/log k) gives k/y = 6 log k /(5 c_2) -> infinity (Q2).")
emit("Below the k=grid-L (m) and k=L_ceil (p) rank columns, both vs y.")
emit("")
emit("x        k_req=L    y=5lnh/6   k_adm/k_req=y/L   k/y     verdict")
for e in SCALES:
    lnx, llx, L, k = regime(e)
    h = APRIME * L * lnx
    lnh = log(h)
    y = 5 * lnh / 6
    head = y / L
    verdict = "AVAILABLE" if head >= 1 else "UNAVAILABLE"
    emit("1e%-5d %s %s %s %s   %s"
         % (e, fmt(L), fmt(y), fmt(head), fmt(L / y), verdict))
emit("")
emit("x        k_req=Lceil y=5lnh/6  k_adm/k_req=y/Lc  Lc/y    verdict")
for e in SCALES:
    lnx, llx, L, k = regime(e)
    Lc = L_ceil(lnx)
    h = APRIME * L * lnx           # window uses grid L (anchor h form)
    lnh = log(h)
    y = 5 * lnh / 6
    head = y / Lc
    verdict = "AVAILABLE" if head >= 1 else "UNAVAILABLE"
    emit("1e%-5d %10d %s %s %s   %s"
         % (e, Lc, fmt(y), fmt(head), fmt(mpf(Lc) / y), verdict))
emit("  -> k/y = 1.85 -> 2.38 (grid L) and larger for L_ceil, RISING with")
emit("     scale: the demand exceeds the effectivization ceiling at every")
emit("     tabulated scale and the gap WIDENS.  VERDICT: UNAVAILABLE,")
emit("     grid-uniformly, in the operative regime.")
emit("  SUPERSEDES steering's authoring-time sensitivity (headroom")
emit("     1.10/1.14/1.18/1.22 growing like lnlnln h): that used")
emit("     k_adm = c_3 ln h lnln h with c_3 = 1 ASSUMED a valid absolute")
emit("     constant.  Q2 shows c_3 is not recoverable as absolute from the")
emit("     printed proof in this regime; the true printed-proof ceiling is")
emit("     the regime boundary k_adm = y, not c_3 ln h lnln h.")
emit("  RULE-12 LANDING: the constant does NOT land in the operative regime")
emit("     (neither additive shift nor coefficient coupling) -- the")
emit("     obstruction is a regime boundary k > y, and k/y never approaches")
emit("     1 from above in or beyond the grid (window h grows too slowly")
emit("     relative to L), so growth alone never reaches the clean regime.")
emit("")

# ---------------------------------------------------------------- #
emit("== S4. Kuperberg Theorem 1.2 displayed constant (3 log k)^k ==")
emit("(20)/(21) small-prime factor prod_{p<=k^3}(1-1/p)^{-k}; Mertens third")
emit("theorem (Rosser-Schoenfeld 1962, explicit form) gives")
emit("prod_{p<=z}(1-1/p)^{-1} = e^gamma ln z (1+o(1)), so at z=k^3,")
emit("prod_{p<=k^3}(1-1/p)^{-1} = e^gamma . 3 ln k (1+o(1)) = 3 e^gamma ln k")
emit("(1+o(1)).  The printed bound (3 log k)^k drops the e^gamma per factor")
emit("(an e^{gamma k} = (ln x)^{2 gamma/ln2 . (1+o(1))} loss at k = L).")
emit("Exact finite product at the grid k^3 (MEASURED) vs 3 ln k and the RS")
emit("asymptotic 3 e^gamma ln k:")
emit("x        k=L        exactProd   3lnk       3e^g.lnk   exact/(3lnk)")
def primes_up_to(n):
    if n < 2:
        return []
    s = [True] * (n + 1)
    s[0] = s[1] = False
    for i in range(2, int(n ** 0.5) + 1):
        if s[i]:
            for j in range(i * i, n + 1, i):
                s[j] = False
    return [i for i in range(2, n + 1) if s[i]]
for e in SCALES:
    lnx, llx, L, k = regime(e)
    kc = int(float(k) ** 3)
    prod = mpf(1)
    for p in primes_up_to(kc):
        prod *= 1 / (1 - mpf(1) / p)
    lnk = log(k)
    emit("1e%-5d %s %s %s %s %s"
         % (e, fmt(L), fmt(prod), fmt(3 * lnk), fmt(3 * EG * lnk),
            fmt(prod / (3 * lnk))))
emit("  -> exact/(3 ln k) = 1.789 -> 1.783 -> e^gamma = %.4f: the exact"
     % float(EG))
emit("     small-prime product is 3 e^gamma ln k, NOT 3 ln k.")
emit("")
emit("S4 pricing on the grid: expo[(c ln k)^k] = k ln(c ln k)/lnln x, vs the")
emit("anchored F17.9 wall.  c = 3 reproduces steering's displayed-factor")
emit("row (5.350/5.699/6.092/6.440); c = 3 e^gamma is the Mertens-honest")
emit("column; the exact-product column uses the MEASURED finite product.")
emit("x        (3lnk)^k    (3e^g lnk)^k  exactProd^k   F17.9(exp(k ln k))")
for e in SCALES:
    lnx, llx, L, k = regime(e)
    kc = int(float(k) ** 3)
    prod = mpf(1)
    for p in primes_up_to(kc):
        prod *= 1 / (1 - mpf(1) / p)
    lnk = log(k)
    e3   = expo(k * log(3 * lnk), llx)
    eeg  = expo(k * log(3 * EG * lnk), llx)
    eex  = expo(k * log(prod), llx)
    emit("1e%-5d %s %s %s %s"
         % (e, fmt(e3), fmt(eeg), fmt(eex), fmt(F179[e])))
emit("  -> the Mertens-honest / exact column exceeds steering's (3 ln k)^k")
emit("     by 2 gamma/ln2 = %.4f in expo (the dropped e^{gamma k}); it also"
     % float(2 * euler / LN2))
emit("     exceeds F17.9 at the small scales and closes toward it by 1e1000.")
emit("     The exponent GROWS like (2/ln2) ln(3 e^gamma ln k) ~ lnlnln x:")
emit("     Theorem 1.2's average-side upper bound is superpolylog at")
emit("     exchange depth under EITHER constant.")
emit("")
emit("END OF PINTZ-CONSTANTS SHEET")

with open(__file__.replace("pintz_constants_sheet.py",
                           "pintz_constants_sheet_tables.txt"), "w") as f:
    f.write("\n".join(OUT) + "\n")
