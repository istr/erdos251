# Relative extension statement layer -- item-0018 M1 (v1.1; post-R2)

Date: 2026-07-19. Author: item-0018 runner (steering lineage, Claude
Fable 5, model string claude-fable-5), against kickoff v1 (operator-
supplied, ephemeral, never committed; disk sha256 44c07d99...60f818).
Pin: main = 32b91ea92d73cfb667a5e85c4f6f4db27ba0474a (kickoff Section
0). PIN RECORD (deviation note, checklist-rule-iii style): the
kickoff's Section 7 first predicate still reads HEAD == 8cb5086 (the
ANN-51-time pin, at which the kickoff was first authored with steering
sha256 57655d5a...); the file on disk is a post-bookkeeping revision
whose Section 0 re-pins to 32b91ea, and git diff 8cb5086..32b91ea
touches ONLY bookkeeping (reports, HANDOVER, ledger, roadmap,
runs/README) -- every read-only anchor of Section 2 is byte-identical
across both states, and runs/README rule 15, which this item binds to,
exists only at 32b91ea. Per the item-0017 precedent ("kickoff
read-only anchors unchanged ... so session A pins to" the new HEAD)
the session pins to 32b91ea; recorded here and in the run report, not
silently absorbed. All other Section 7 predicates PASS verbatim
(frozen blocks byte-identical; relocation check PASSED; sorry
inventory exactly Statement.lean = 1; roadmap/item-0018.md status:
ratified).

Scope: MILESTONE M1 ONLY -- statement layer. NO proofs of analytic
inputs are attempted; success is statement precision. Zero lean/
edits. Web OFF (corpus-only). Out-of-corpus firewall honored: the two
2026-07-18 operator reports are not cited; the k = 2 inflation
constant enters only through the in-repo F17.5 Euler product,
independently recomputed in the budget sheet (T3).

Discipline: B1 obstruction language throughout (located obstructions,
never impossibility; scope qualifiers inline). Citations by decl name,
never file:line (ANN-2f). Index convention (ANN-50): Lean gap k =
paper g_{k+1}; delta carries no shift. Findings F18.n and unverified
register U18.n in Sections 9-10, never emptied silently.

Companion workpapers: dossier/item-0018-workpapers/budget_sheet.py and
its companion output budget_sheet_tables.txt (rule-15 sheets; table
references "budget Tn" below; commit is operator post-run
bookkeeping). Report: 0018-report-M1.md. Arithmetic discipline in the
sheets: exact rational where it decides (T4 exact local factors at
small primes), float/mpmath where tail truncation dominates (T3
Euler product; stated per table). REVIEW RECORD: this document was
adversarially audited at draft state by a nine-agent pass (Section
9a); every sustained finding -- including one FATAL repair to the
RS.3 worst-case quotient bound and one FATAL re-scope of the F18.2
sufficiency claim -- was steering-re-executed and folded in before
this v1 was fixed.
R2 RECORD (v1.1): a blind cross-family adversarial scope audit was
executed against the redacted object (payloads/
item-0018-review-r2-v1.md; SOUND WITH REPAIRABLE ISSUES, 0.94, zero
FATAL, 9 MAJOR / 5 MINOR); every sustained finding is repaired in
place with [R2 repair] marks; dispositions in
payloads/item-0018-adjudication-v1.md and Section 9b. The D5
selection, the 7.1 Props, and the 7.2/7.3 design are UNCHANGED
(reviewer-confirmed, NOTE-2/3/4).

## 0. Mission, target shapes, shape register

The dossier-v2 V4 triple (verdict clause V4, adjudication Section 2
FATAL-2) is the object: (i) a matched-flank class lower bound at
k ~ L = (2+o(1)) log2 ln x; (ii) a relative one-position extension
upper bound with effective constant o(ln x) at k ~ lnln x; (iii) a
tail-intersection statement in the filters-first order. This document
produces exactly quantified candidate statements for each input layer,
whose conjunction yields ExchangeSupply1 by the prose-level,
machine-checkable design of Section 7 (D4), a rule-15 budget sheet and
an ex-ante no-go audit per candidate, a reuse audit against the
machine-checked Counting layer, and a selection verdict (Section 8,
D5) fixing the item-0019/0020/0021 targets and the M2 Lean shapes.

TWO TARGET SHAPES, both kept alive until D5 (kickoff D1):

- EX (exclusion form; T1 transplant): class abundance + extension
  concentration bound => the class cannot be middle-rigid => two
  members with equal flanks and distinct middle gaps. The wall
  calculus it must clear is the FATAL-2 re-execution (adjudication
  Section 2): C_per(k+1) * S-ratio < c ln x, with
  ln C*(k+1) = (1+o(1)) k ln k >> lnln x at k = (2/ln 2 + o(1))
  lnln x (F17.9).
- AR (anti-rigidity counting form): the P1 counting positivity
  C_sides - C_words > 0 on the filtered site set (dossier P1;
  "sandwich rigidity" contraposition).

PROVENANCE NOTE on the "F2" tag (recorded, not absorbed): the kickoff
Section 2 attributes the anti-rigidity counting form to the item-0005
adjudication. In payloads/item-0005-adjudication-v1.md the
anti-rigidity CONTENT is Section 2 P4 (R1's contraposition: within
the lattice layer, rationality forces sandwich rigidity at typical
matched-flank pairs), while the entry literally labeled F2 (Section
6) is the Lean-module follow-up candidate; the phrase
"adjudication-F2 form" in dossier V4 reads most naturally as the
item-0017 adjudication's FATAL-2 counting display. Both anchors are
carried above; the mathematical object is the same in all readings
(equal flanks, differing middles, certified by counting), so no
content ambiguity arises. Shape map EX <-> AR: Section 7.5.

## 1. D0 -- regime lock (binding for every candidate)

Fixed once; every symbol, its growth, its consumer role. Paper-side
notation is dossier D0 (chain-v1 conventions); the aggregate filter
D0.2' with parameter map Par'(1,x) is the working frame (F17.3 binds
the counting routes to it; the per-position filter D0.2 is dead on
the floor routes by capacity slack even in Model M).

  symbol   value / growth                       consumer role
  ------   ----------------------------------  ----------------------
  x        -> infinity; scales chosen per       one x per threshold s
           threshold (Section 7.3)              feeds ExchangeSupply1
  N        pi(x); sites n with p_n <= x         site population
  s        depth threshold; sites n >= s+1      Lean t-threading:
           (paper); SINGLE dictionary s := t     t <= n, t <= m
           per 7.3; the downstream dyadic
           consumer itself calls t = s+2 (FW-3)
           [R2 repair, MINOR-3]
  A'       fixed, in (1, 4 sqrt(2)/e)           aggregate window cap
           (working value 1.5)                  sum g_{n+i} <= A'L lnx
  A''      working value 48; the repaired       tail-cap scale; the
           P3.3'(ii) clause demands only        pin makes the site
           A'' > 2A'/(A'-1) = 6, but the        retention floor
           TailIntersection constant N/4        1 - 2/3 - 2/48 =
           (7.1) needs 1 - 1/A' - 2/A'' > 1/4:  7/24 - o(1) > 1/4
           PINNED here (audit repair; the       hold with margin
           dossier's example A'' = 12 gives
           only 1/6)
  D        ceil(13 C_0 A'' ln x)                (E4) near cap
  J        ceil(log2 D) = (1+o(1)) log2 ln x    prefix depth; (E5)
                                                gate 2^J >= D
  K        ceil(log2 D) = (1+o(1)) log2 ln x    suffix depth; far cap
                                                2^K >= D
  M        1 (K1 handshake; weighted M >= 2     Hamming-1 normal form
           is an extension layer, OUT OF        feeds ExchangeAt
           SCOPE for this item)                 verbatim (F17.1/FW-1)
  L        J + 1 + K = (2+o(1)) log2 ln x       word length (gaps)
  k        L + 1 = |H(a,d,c)| =                 tuple rank; rule-15
           (2/ln2 + o(1)) lnln x                evaluation point
  S'_x     D0.2' filtered site set (window      filters-first: caps
           sum cap + BOTH (E4) delta caps)      are INSIDE all counts
  S'^{(s)} S'_x cap {n >= s+1}                  threshold restriction

Depth premise (V3, carried verbatim with its qualifier): the depth
floor J + K >= (2+o(1)) log2 ln x is (E4)/(E5)-forced on TAIL-TYPICAL
routes (D >= typical delta ~ ln x). A route using atypically-small-
tail sites exits this floor and instead owes a separate
density-versus-depth analysis with the F17.8 sparse-site cost; that
escape is priced, not dropped, in candidate C2's ledger clause and
budget T6.

PARITY / NORMALIZATION LOCK (binding; trap T2). Matched-flank gap
words are all-even (every gap g_m, m >= 2, is even): the
parity-blocked class. The conditioning normalization is fixed ONCE:
even-conditioned singular-series moments carry the factor 2. At
k = 2: conditioned mean E_even[S_2] = 2; conditioned second moment
E_even[S_2^2] = 4.601923 = 4 * 1.150481 (F17.5 Euler product,
independently recomputed in budget T3 to the printed precision;
gamma_2 asymptote 1.150481, critical value 2 sqrt(2)/e = 1.040520).
EVERY candidate constant below states which normalization it uses;
all rho-quotients of this document are even-conditioned (their p = 2
factor is exactly 2, RS.3).

Rule-15 evaluation point: k = (2/ln 2) lnln x on the grid x = 1e8,
1e20, 1e100, 1e1000 (budget T0). Standing conversions: at rank
exactly (2/ln 2) lnln x, 2^rank = (ln x)^2; the sheet's working
rank k = L + 1 carries one extra factor 2 (exponent rows read
2 + ln2/lnln x); k! and exp((1+o(1)) k ln k) are
superpolylogarithmic with exponent ~ 2.885 lnlnln x (budget T1); the
even-conditioned compounding constant gamma_2^k = (ln x)^{0.405+o(1)}
(polylog, exponent 2 log2(1.150481)).

## 2. T6 dictionary smoke test (executed BEFORE D1; trap T6)

Object: the 1e9 b = 3 certificate site (J,K,D0,b) = (7,6,44,3) with
d_1 = -24 (dossier Section 7.2), re-derived in D0 notation from the
printed primes (16 consecutive primes per site, primality and
consecutiveness re-checked computationally this run).

- D0.1 word map at anchor index t (anchor prime p_t): the printed
  gap sequences decompose as prefix_J = (4,2,16,2,10,12,18), middle
  6 (n-site) vs 30 (m-site), suffix_K = (20,12,4,14,6,4): pi_1-match
  with d_1 = 6 - 30 = -24, even and nonzero, so the P2.1 factor-2
  margin applies; E = d_1 (M = 1).
- (E5) gates from the printed data: b = 3: 3*(44-2) = 126 < 2^8 =
  256; b = 1 form: 42 < 256.
- ANN-50 dictionary (the known hazard, checked both directions):
  paper w_i = g_{t+i} = Lean gap (t+i-1); the middle w_{J+1} =
  g_{t+J+1} = Lean gap (t+J) -- exactly the differ clause slot of
  ExchangeAt; the far-cap index paper t+L = t+J+1+K = Lean n+J+1+K
  (delta carries no shift). The Lean base index equals the paper
  anchor index; the shift lives entirely inside gap.
- Depth calibration: the certificate's J+K = 13 vs 2 log2 ln(1e9) =
  8.75 -- the certificate sits deeper than the typical-depth
  envelope, consistent with the Section 7.2 frontier datum (zero
  (7,7) collisions at 1e9).

All checks PASS; the dictionary is fixed as above for every statement
below. (Delta tail values are d5b_deep.py script outputs,
independently recomputed by R1 in the item-0017 review; they are not
re-derived here -- T6 is a notation test, not a computation audit.)

## 3. Statement-layer definitions (RS.n; used verbatim by D1-D5)

DEFINITION RS.1 (side pair, class, class counts). For J, K >= 1 an
even side pair is P = (a, c), a = (a_1..a_J), c = (c_1..c_K), all
entries even, >= 2. For a finite index set T (DEFAULT T = S'^{(s)}_x:
filters-first, caps inside) define the matched-flank class and counts
    F_P(T) = { n in T : g_{n+i} = a_i (1 <= i <= J),
                        g_{n+J+1+i} = c_i (1 <= i <= K) },
    N_P(T) = |F_P(T)|,
    N_{P,d}(T) = |{ n in F_P(T) : g_{n+J+1} = d }|   (d even >= 2).
Identities (used repeatedly): sum_d N_{P,d}(T) = N_P(T) EXACTLY (the
middle partitions the class), and sum over P of N_P(T) = |T| EXACTLY
(the side pair partitions the site set). Realized family Fam(T) =
{P : N_P >= 1}; multi-member family Fam_2(T) = {P : N_P >= 2}. When T
is omitted it is S'^{(s)}_x and the argument is written (x).

DEFINITION RS.2 (block point sets; tuple dictionary). H_pre(a) =
{0, a_1, a_1+a_2, ..., A_J} (J+1 points, A_J = sum a_i); H_suf(c) =
{0, c_1, ..., C_K} (K+1 points); for even d >= 2 the full-word tuple
    H(a,d,c) = H_pre(a) u (A_J + d + H_suf(c)),
|H(a,d,c)| = L + 1 = k (all points even, 0 in H). A class member
with middle d is a consecutive realization of the length-L word
(a, d, c) in the sense of decl IsConsecRealization, with point set
H(a,d,c) = wordPointSet of that word.

DEFINITION RS.3 (local quotient rho; the kickoff's B-layer quotient,
factored via the insert algebra). For P = (a,c) and even d:
    rho(P,d) := S(H(a,d,c)) / ( S(H_pre(a)) * S(H_suf(c)) ),
the two-block correlation quotient (S = singularSeries). DOMAIN
[R2 repair, MINOR-4]: defined when S(H_pre(a)) and S(H_suf(c)) are
positive (admissible blocks); NOTE: any block realized by primes
exceeding p omits residue 0 mod p, so every side pair realized at
large anchors is admissible with positive block singular series;
off-domain set rho := 0 by convention (unused: B1's cap clause and
m3 range over realized classes, and an inadmissible H(a,d,c) has
N_{P,d} = 0 at large anchors). Structure,
even-conditioned: the p = 2 factor is exactly 2 (all point sets
occupy one class mod 2; the factor is 2^{|H|-1} over 2^{J} * 2^{K}).
For odd p the factor is computed by iterating the one-point insert
dichotomy over the K+1 translated suffix points: each insert
multiplies the log by the decl-level dichotomy of nuMod_insert /
log_singularFactor_insert_sub_le -- COLLISION prime (occupied class
hit again): factor (1 + 1/(p-1))-type, log difference exactly
-log(1 - 1/p); NEW class: factor <= 1. The per-insert step is
machine-checked (those decls are sorry-free in-repo); the (K+1)-fold
composition and the two-block bookkeeping are prose (reuse audit,
Section 6). EXACT LOCAL FORM (audit repair; the v1-draft's
first-T-odd-primes cap was FALSE and is retracted, Section 9a): per
odd prime the factor of rho is
    (1 - nu_H/p) / ((1 - nu_pre/p)(1 - nu_suf/p))
(the (1-1/p)-powers cancel since |H(a,d,c)| = (J+1)+(K+1)), bounded
by (1 - nu_min/p)^{-1} with nu_min = min(nu_pre, nu_suf, p-1) --
which reaches p at full two-block alignment, NOT the one-insert
dichotomy value (1+1/(p-1)): the insert telescope bounds only
S(H_d)/S(H_pre), and the division by S(H_suf) amplifies aligned
primes. WORST CASE over the full in-window (P,d) range: CRT-aligned
middles realize the factor p for every odd p with p-1 <= min(J,K)+1
and primorial inside the window budget, so
    sup rho = (ln x)^{1-o(1)}   (POLYLOG, exponent -> 1),
and at finite scales the sup even exceeds ln x (budget T4 witnesses,
steering-re-executed: rho = 82.24 at the 1e8 depths vs the retracted
cap 9.80; rho = 221.66 = 4.8 ln x at the 1e20 depths -- gate (G1)
fails outright on the unconstrained pointwise range). Consequence:
pointwise B-candidates carry an explicit rho-cap clause (B1's
(b1-rho)); the aligned classes are left to the family-averaged forms,
whose gate constants never reference rho. TYPICAL BEHAVIOR (distinct
from the sup): the Gallagher-frame even-conditioned d-mean of rho is
2 (heuristic at growing k; U18.2), so the heuristic middle law is
N_{P,d}/N_P ~ rho(P,d) e^{-d/ln x} / ln x.

DEFINITION RS.4 (capped vs window counts; the C-layer split). N_P and
N_{P,d} default to T = S'^{(s)}_x (all three filter clauses). The
window-only variants N^w_P, N^w_{P,d} take T = the sites with p_n <=
x, n >= s+1, and the window-sum cap only (NO delta caps). The
uncapped-anchor variants N^o (used only in the A1 reuse audit) are
consCount semantics: anchor prime in (sqrt x, x], no caps at all.

## 4. D1 -- candidate set

Binding order honored: D0 and T6 above precede this section; per
candidate, the rule-15 budget sheet (Section 5 pointers into budget
T1-T7) was computed BEFORE the no-go audit (Section 5a) and before
any refinement; the audit pass and its adjudication are Section 9.

Every candidate carries: full quantifier prefix, uniformity range,
constant dependence, normalization, consumer-fit note. Statements are
about the primes; heuristic support is labeled where cited and never
load-bearing for the statement's meaning. Variant-count note
(deviation register): the kickoff's 2-3-variants-per-layer window is
read as counting primary candidates (A: A1/A2/A3; B: B1/B2/B3; C:
C1/C2), with A1-typ, B1', B2.reduced, C1'/C1'' as sub-variants of
their primaries -- recorded rather than silently assumed.

### 4.A A-layer (matched-flank class lower bounds)

CANDIDATE A1 (HLQuantA-conditional per-class form; the reuse-audit
target). Assume HLQuantA (frozen decl, verbatim). For every kappa >=
1 there exists x_0 = x_0(kappa) such that for all x >= x_0, for every
even side pair P = (a,c) at the D0 depths J(x), K(x), and every even
d >= 2 such that H = H(a,d,c) satisfies
    (h1) IsAdmissible H,
    (h2) offsetSpan H <= kappa (k-1) ln(k+1)     [small-span budget],
it holds that
    N^o_{P,d}(x) >= (1/4) * modelMass(H, x)  and  N^o_{P,d}(x) >= 1.
Uniformity: over ALL (P, d) satisfying (h1)-(h2) simultaneously at
each x (single x_0; matches the decl's quantifier order). Constant
dependence: 1/4 absolute; the mass floor via decl
singularSeries_lower_bound carries the in-repo C = 12 (budget T5(a),
decl-indexed exponent C(k-1)ln(k+1): nonvacuous only near x ~ 1e371;
reference C = 1 near x ~ 1e45 -- finite-scale honesty row, D3(vi);
audit-corrected from the draft's ~1e300/~1e30). Normalization: none
(absolute count vs model mass).
STATUS: PROVED-conditional -- this IS decl consCount_lower_bound
instantiated verbatim (card L+1, budget (L+1) <= 4 lnln x - 1 holds
at D0 depths since 2/ln2 < 4; span (h2) is the decl's own
hypothesis). The A-layer at SMALL SPAN is consumed machinery: the
kickoff's DESIRED outcome, delivered on the small-span instance.
NONVACUITY of (h1)-(h2): take k consecutive primes beyond k as the
point set (admissible: no prime p <= k has all classes covered since
the points are coprime residues avoiding 0 mod each p <= k in a
window of primes > k; p > k never covered by k points); its span is
<= C_0' k ln k by Chebyshev; its gap word is all-even (all points
are odd primes).
MIDDLE FLEXIBILITY (audit repair; the draft's abundance claim was
FALSE and is retracted, Section 9a): replacing d by d' translates
the ENTIRE suffix block, so admissibility of H(a,d',c) is a
condition on the shift class of d' mod every small prime -- not a
one-added-point condition. For the consecutive-primes construction
above both blocks miss exactly ONE class mod each small p, leaving
one good shift class per prime; the in-budget count of admissible
alternative middles then COLLAPSES (audit-computed and
steering-re-executed: exactly 1 admissible in-budget middle -- the
original d itself -- at k = 24, kappa = 2, and the count is
nonincreasing in k at kappa = 10 as well). DISPLAYED INSTANCE [R2
repair, MAJOR-9: reproducible from this text; adjudication
re-executed]: the 24 consecutive primes 29..137, balanced split
J = K = 11, block spans A_J + C_K = 102, original middle d = 6,
budget 2*23*ln 25 = 148.07, candidate middles d' even in [2, 46]:
exactly d' = 6 is admissible. (Adjudication scan over ALL splits
J = 1..21 of the same run: balanced and near-balanced splits give
exactly 1; the near-degenerate splits J in {1, 19, 20, 21} give
2-4 -- see U18.7's adjudication note.) Whether side pairs with
>= 2 admissible in-budget middles exist at every rank ("doubly
extendable in-budget side pairs") is OPEN and is registered as
U18.7; no construction is exhibited here.
CONSUMER-FIT NOTE (the two-word route and where it strands):
CONDITIONAL ON U18.7 (a doubly-extendable in-budget side pair at the
working rank), applying A1 at the SAME P with two middles d != d'
produces, for every threshold s and x >= max(x_0, threshold scale),
two sites n, m with matched flanks and differing middles and
n, m >= s+1 -- the differ clause WITHOUT any B-layer input. What it
does NOT produce: the (E4) caps (N^o is uncapped, RS.4). The class is HL-thin (HL-PREDICTED relative density
e^{-Theta((lnln x)^2)}; the mass floor is the lower half of that
scale), and the C-layer window for thin classes is closed FOR THIS
RECORDED ROUTE (the frozen-card truncated-tail transfer; F18.2,
budget T6(b); no all-routes impossibility is claimed [R2 repair,
MAJOR-5]): the
truncated-tail transfer inside the frozen HLQuantA card budget admits
family density (ln x)^{-c} only for c < c* = 4 ln 2 - 2 = 0.7726,
while a thin class sits at quasi-polylog sparsity. So the two-word
route is exactly T3-shaped: it closes under a Hypothesis-B-shaped
pointwise cap and its ENTIRE unconditional residual is the sparse-
site tail clause (F17.8) -- now with the HL-conditional part fully
consumed machinery rather than a trap construction. This sharpens,
and is consistent with, the T3 row of the dossier D3 table.
A1-typ (exchange-typical-span variant; named open input OI-A1;
exact candidate, heuristically motivated [R2 repair, MAJOR-3: the
draft hedged between the unthinned display and a thinned one; the
candidate below is the single exact statement]). Assume HLQuantA
(frozen decl, verbatim). CANDIDATE: for every eps > 0 there exists
x_0' = x_0'(eps) such that for all x >= x_0', for every even side
pair P = (a,c) at the D0 depths and every even d >= 2 such that
H = H(a,d,c) satisfies (h1) IsAdmissible H and
    (h2') offsetSpan H <= A' L ln x     [D0 window budget],
it holds that
    N^o_{P,d}(x) >= (1/4) (ln x)^{-tau(A')(1+eps)} modelMass(H, x),
with tau(A') = 2A'/ln 2 fixed. Uniformity: over all (P, d)
satisfying (h1)-(h2') simultaneously at each x (single threshold).
Constant dependence: 1/4 absolute; tau(A') from the D0 pin A'
alone; x_0' depends on eps and the D0 pins only. Normalization:
none. STATUS: OPEN; NOT derivable from the landed machinery (reuse
audit Section 6, walls w1/w2); the exponent tau(A') is MOTIVATED
by the U18.1 Cramer thinning heuristic (U17.9-class, budget T5(c))
-- the motivation is heuristic, the statement is exact and may be
false. Kept as a statement target only; no candidate below
consumes it; its finite-scale shadow is the m5 measurement.

CANDIDATE A2 (family abundance; unconditional; proved at dossier
level). For every s >= 0 and x >= x_1' (P3.3' threshold): 
    sum over P in Fam(S'^{(s)}_x) of N_P = |S'^{(s)}_x|
      >= (1 - (1+o(1))/A' - 2/A'') N - s - o(N).
Quantifier prefix: forall s, forall x >= x_1'(s-free; the -s term
absorbs the threshold), the displayed inequality. Constants:
Chebyshev C_0 (P3.2) + PNT for the window-sum mean (P3.1'; U17.7
scope); A''(A') per the repaired abundance clause. Normalization:
none. STATUS: the equality is the RS.1 partition identity; the
inequality is P3.3'(ii) (repaired form) -- unconditional.
CONSUMER-FIT: the denominator of B2 and the population floor of the
pigeonhole (Section 7); carries the caps (filters-first) and the
threshold. Trap-T1 check: quantifies over the realized family of ONE
filtered set -- no admissible-tuple universal quantifier anywhere.

CANDIDATE A3 (positive-proportion / quantile form; the abundance
content the pigeonhole needs). There exists delta > 0 and for every
s >= 0 an x_2(s) such that for all x >= x_2(s):
    sum over P in Fam_2(S'^{(s)}_x) of N_P >= delta * |S'^{(s)}_x|,
i.e. at least a delta-proportion of filtered sites beyond the
threshold have a flank twin in the same filtered set (equivalently:
the mass of multi-member classes is a positive proportion).
Variants: A3(m): with Fam_2 replaced by {P : N_P >= m(x)} for a
specified multiplicity floor m(x) (consumed by B1's truth window,
see B1). Quantifier order: delta uniform in s (exists delta, forall
s, forall large x). NECESSITY NOTE (audit repair): the t-threading
of 7.3 needs only an x-free delta(s) PER s (RelExtensionUpper's
s-quantifier sits inside its x-quantifier, so the 7.2 pigeonhole
closes per s at eps = delta(s)/4); the s-uniform placement is
strictly stronger and is adopted for the single s-free 7.4 gate
constant and the m1 measurement target, not by necessity.
Constant dependence: delta absolute. Normalization: none.
STATUS: OPEN for the primes. Support (audit-corrected provenance):
the Model M analogue at delta = 1 - o(1) is PLAUSIBLY DERIVABLE
from the Theorem M1 toolkit but only after four steps NOT written
in the corpus [R2 repair, MAJOR-7]: (1) a uniform LOWER bound on
the per-word match probability (M1(e) is an upper/dilution
device), (2) a per-site lower-tail argument after the
residue-class dilution, (3) the Par -> Par' / per-position ->
aggregate filter adaptation, (4) the degree-to-Fam_2-mass
conversion. It is NOT STATED in M1 -- M1's recorded clauses
(i)/(ii) certify only a (ln x)^{-2+o(1)} twinned-site fraction; no
derivation is supplied here; registered as write-out debt U18.6,
and no PROVED tag is claimed. Primes-side evidence measured (exchange-class counts
12/178/1287 and 2/21/143 across 2e6/2e7/1e8; (6,6,64) classes
1 -> 29 from 1e8 to 1e9; all measured on the D0.2-style site sets of
dossier 7.1, not on S'_x -- evidence class, not proof; asymptotic
persistence sits next to the open tensorization step U17.11(a) and
is NOT claimed.
CONSUMER-FIT: exactly the A-input of the family pigeonhole (Section
7.2); strictly weaker than any HL-type class law (no per-class
asymptotics asserted); its natural proof routes run through the
parity-blocked class laws (blocker 2) -- route hardness recorded, not
absorbed into statement strength. D3(v) note: the measured support is
partly marginal-level (gamma_2); the statement is window-level; the
gap is flagged as evidence class, not statement defect.

### 4.B B-layer (relative one-position extension upper bounds)

SHAPE DECOMPOSITION (binding for all B candidates; F18.3). Every
B-layer statement has two sub-shapes:
  (abs) absolute-normalized: N_{P,d} <= C_abs * S(H(a,d,c)) x /
        (ln x)^k -- a per-word sieve bound. The F17.9 wall applies
        VERBATIM to C_abs: every displayed sieve constant (the
        self-proved C*(k), the classical 2^k k!) is
        exp((1+o(1)) k ln k) = superpolylog (budget T1) and fails
        the o(ln x) gate at exchange rank. F17.9 is proved only
        against k-uniform per-word constants: (abs) is the shape it
        kills.
  (rel) relative: N_{P,d} <= (C_rel/ln x) N_P -- the consumable
        shape. rel = abs / (class lower bound): any proof of (rel)
        THROUGH (abs) imports the wall; a direct proof of (rel)
        (ratio or exchange devices at site level, global pair
        counting) is the F17.9-evading lane and is exactly the
        item-0020 mandate.
All B candidates below are stated in (rel) form; their budget sheets
tabulate the statement constants (typical rho subpolylog under the
U18.2 heuristic; sup over the unconstrained range polylog and
(G1)-failing at finite scales -- corrected T4; hence B1's mandatory
rho-cap clause) and the displayed-route constants (superpolylog; the
wall) -- the wall is a ROUTE property; the statement-level gate is
passable by the selection-gated forms B2/B3, whose constants never
reference rho (F18.4, audit-scoped).

CANDIDATE B1 (pointwise, with multiplicity floor and quotient cap).
Parameters of the candidate: a floor exponent eps_0 > 0 and a
quotient cap R(x) with R(x) = o(ln x). For every eps > 0 there is
x_3(eps; eps_0, R) such that for all x >= x_3, every s >= 0, every
P in Fam(S'^{(s)}_x) with
    (b1-floor) N_P >= (ln x)^{1+eps_0},
and every even d in [2, A' L ln x] with
    (b1-rho)   rho(P,d) <= R(x),
it holds that
    N_{P,d}(x) <= ((rho(P,d) + eps) / ln x) * N_P(x).
Constant dependence: rho(P,d) explicit per RS.3 (even-conditioned).
The (b1-rho) cap is MANDATORY (audit repair, Section 9a): the sup of
rho over the unconstrained in-window range is (ln x)^{1-o(1)} and
exceeds ln x at finite scales (RS.3 corrected form; budget T4
witnesses), so an uncapped pointwise form has empty content on
CRT-aligned classes; those classes are carried by the
family-averaged forms below, whose gate constants never reference
rho.
STATEMENT-PRECISION FINDING (F18.5; domain-qualified [R2 repair,
MINOR-1]): WITHOUT the floor (b1-floor) the capped pointwise form
is FALSE at any scale where a small class has a realized middle
inside the rho <= R(x) domain (the uncapped o(ln x)-constant form
is false for every sufficiently small realized class):
sum_d N_{P,d} = N_P forces some N_{P,d} >= N_P/#realized-middles,
and a singleton class with an in-domain realized middle has
N_{P,d} = N_P = 1 > (C/ln x) N_P. Integer
counts have Poisson-scale fluctuations in any truth model, so
pointwise (rho + eps)-precision requires per-cell means -> infinity:
hence the floor. Empirical calibration (audit-corrected statistic:
NO class-size distribution exists in the corpus -- measuring it is
exactly m1): the 7.1 pair aggregates imply small typical
multiplicities among collision classes (5232 ordered off-diagonal
side collisions over >= 1287 collision classes at (4,5,30), x = 1e8:
root-mean-square multiplicity ~ 2), far below the floor: B1's truth
window is EXPECTED-INACCESSIBLE at reachable x (pending m1), and
item-0019 must measure averaged forms instead (Section 8,
measurement spec m1/m2).
B1' (bounded-constant variant; closed form [R2 repair, MINOR-5]):
THERE EXIST an absolute constant C_rel >= 1 and, for the fixed
candidate parameters (eps_0, R), a threshold x_3'(eps_0, R) such
that the B1 conclusion holds for all x >= x_3' with (rho + eps)
replaced by C_rel * rho (consumption survives any
C_rel with C_rel * R(x) = o(ln x) on the (b1-rho)-capped domain; no
room exists outside the cap -- corrected T4). B1' is the form the
consumer actually needs; the (rho+eps)
precision form is kept as the sharp target and flagged D3(ii)
(plausibly open-HL-adjacent in precision; the C_rel form is not).
STATUS: OPEN (named open input OI-B1: the relative middle law).
CONSUMER-FIT: implies per-class anti-rigidity outright on classes in
its window (max_d N_{P,d} < N_P once C_rel R(x) < ln x, on the
capped domain), the strongest per-class conclusion of the family;
but its window excludes both the small-multiplicity population the
finite-scale aggregates indicate AND the CRT-aligned classes outside
(b1-rho), so it CANNOT be the sole B-layer input at any finite stage
of the argument -- selection consequence in D5.

CANDIDATE B2 (family-averaged, selection form; closed eps-form
[R2 repair, MAJOR-1: the kickoff-verbatim rate display quantified
eps without using it and used C_F without quantifying it; the
closed form below IS the candidate, the rate reading is derived
notation]). Selection form (B2.plain): for every eps > 0 there is
x_4(eps) such that for all x >= x_4, all s >= 0, and EVERY
selection function P |-> d_P (even, d_P <= A' L ln x) on
Fam(S'^{(s)}_x):
    sum over P of N_{P, d_P}  <=  eps * sum over P of N_P.
RATE NOTATION (derived, not part of the proposition): for any
proof delivering the display, C_F(x) := ln x times the sup over
(s, selections) of the realized ratio satisfies C_F(x) = o(ln x);
the kickoff display "<= (C_F(x)/ln x) sum N_P, gate C_F = o(ln x)"
is recovered with this C_F.
The adversarial-selection quantifier is what the rigidity pigeonhole
consumes (the rigid middle is adversarial); a fixed-selection or
fixed-d variant is strictly weaker and NOT sufficient for D4.
ENTANGLEMENT FINDING (F18.3): B2.plain is not a pure upper-bound
statement: choosing d_P realized gives LHS >= |Fam|, so B2.plain
forces |Fam| <= eps * sum N_P for every eps eventually, i.e.
average class multiplicity -> infinity -- abundance content
smuggled into an upper-bound shape [R2 repair: eps-form reading]. The pure-concentration isolate
is the REDUCED form (B2.reduced), the selected candidate (closed
eps-form, identical to the 7.1 Prop [R2 repair, MAJOR-1]):
    for every eps > 0 there is x_4(eps) such that for all x >= x_4,
    all s >= 0, and every selection (d_P):
    sum over P of ( N_{P, d_P} - 1 )_+  <=  eps * sum over P of N_P.
B2.reduced is singleton-inert ((N-1)_+ = 0 there), carries no
abundance content, and still contradicts rigidity given A3 (Section
7.2). Constant dependence: none beyond the D0 pins (the derived rate
C_F is o(ln x) by construction) [R2 repair, MAJOR-1];
normalization: none (counting ratio). Budget: the gate line is
(G1); the heuristic value of C_F on the Gallagher frame is O(1)
(max-concentration of the middle law; U18.2-status), tabulated
against the reserve in budget T7.
STATUS: OPEN (named open input OI-B2 = the item-0020 target; ANN-52
BET-08 registers exactly this shape "per the item-0018 selection
verdict", which Section 8 fixes).
CONSUMER-FIT: the exact B-input of the family pigeonhole; evades
F17.9's k-uniform per-word hypothesis BY SHAPE (averaged, relative,
selection-quantified); the designated structurally-different
exclusion device lane is global pair counting (Section 7.5).

CANDIDATE B3 (quantile fallback; closed form [R2 repair,
MAJOR-2]). There exists ONE fixed nonnegative function C_q with
C_q(x)/ln x -> 0 -- independent of eps, s and the selection, with
dependence on the D0 pins alone -- such that: for every eps > 0
there is x_5(eps) with: for all x >= x_5, s >= 0, there is an
exceptional sub-family E subset Fam(S'^{(s)}_x) with
    sum over P in E of N_P <= eps * sum over all P of N_P,
such that for every P outside E and every even d <= A' L ln x:
    N_{P,d}(x) <= (C_q(x)/ln x) * N_P(x) + 1. The +1 makes the per-class clause
singleton-inert (statement-precision repair, same mechanism as
F18.5); the eps-mass exceptional clause is the quantile weakening.
STATUS: OPEN (weaker than B2.reduced: derivable from it up to the
+1 bookkeeping via a Markov-selected NONEMPTY exceptional family --
not with E empty; audit-corrected). CONSUMER-FIT: drop-in
replacement for
B2.reduced in the pigeonhole at the price of an explicit eps-mass
subtraction in the slack ledger (Section 7.4); the fallback if
item-0020's device controls typical classes only.

### 4.C C-layer (tail intersection, filters-first)

CANDIDATE C1 (family-aggregate cap retention; audit-repaired
display -- the draft's per-class forall-P form is NOT supported by
the recorded reduction and is demoted to the mass-floor variant
C1'' below). [R2 repair, MAJOR-4: the family is now an EX ANTE
rule; the draft's FF(x) left the s-dependence and cap-independence
unpinned, admitting a circular post-cap selection and the empty
family.] For a NAMED family rule (s, x) |-> FF_{s,x}, a set of
side pairs declared CAP-BLIND: membership is determined by P, x, s
and window-only data (RS.4's N^{w,(s)}-world and word data) alone,
independent of the two delta-cap outcomes; rules with
sum over P in FF_{s,x} of N^{w,(s)}_P(x) = 0 are excluded. The
candidate, for that ONE named rule: there is eps_C < 1/2 and x_6
with: for all x >= x_6, s >= 0:
    sum over P in FF_{s,x} of N_P(S'^{(s)}_x)
      >= (1 - eps_C) * sum over P in FF_{s,x} of N^{w,(s)}_P(x)
(RS.4: left side carries both (E4) delta caps; right side the
window cap only; the threshold s is explicit on BOTH sides).
eps_C and x_6 may depend on the rule and the D0 pins, not on s or
x. C1' (asymptotic variant): eps_C = eps_C(x) -> 0.
C1'' (per-class variant): the forall-P form, admissible ONLY
under an explicit per-class mass floor N^{w,(s)}_P >= mu(x) *
sum_FF N^{w,(s)}_P (the deep-tail budget below then reads against
the CLASS mass. [R2 repair, MAJOR-8: the draft's blanket density
claim used an unstated side-class upper bound; scoped form:] the
HL-PREDICTED density of a single exchange-rank class is
~ (ln x)^{-(k-1)} -- a model-level scale; no proved upper bound is
displayed, and a proved one would itself carry a growing-k sieve
constant (F17.9-adjacent); for any class whose density is
INDEPENDENTLY known to be exp(-Theta((lnln x)^2)), the needed tail
rank ~ (k-1) lnln x/ln2 >> the headroom: per-class C1'' is
unreachable BY THIS ROUTE for such classes -- audit finding,
re-scoped).
Constant dependence: eps_C explicit; the consumption in D4 needs
only eps_C < 1/2 (constant retention), NOT o(1). Normalization:
none. DEFINITION (eta): the family site-density is eta_s(x) :=
(sum over P in FF_{s,x} of N^{w,(s)}_P(x)) / N -- TRUE window
mass, not model mass; the distinction is load-bearing below. [R2
repair, MAJOR-4: threshold-explicit.]
STATUS: OPEN; REDUCTION RECORD (this item; audit-re-scoped): C1 for
a family of site-density eta reduces, via Markov INSIDE the family
mass, to family-conditional truncated-tail first moments at
extension ranks j <= J_0 = log2(1/eta) + O(1) (numerators bounded by
nonconsecutive tupleCount upper bounds, i.e. HLQuantA-upper shapes),
PLUS a global Markov subtraction at threshold T* ~ ln x / eta for
the deep tail (P3.2-type at shifted positions; P3.2's stated range
0 <= r <= L needs a trivial position-shift extension to r = L + J_0,
recorded). Within the FROZEN HLQuantA card budget (|H| <= 4 lnln x)
the rank headroom is (4 - 2/ln2) lnln x, so the route REQUIRES
family density (ln x)^{-c} with
    c < c* = 4 ln 2 - 2 = 0.7726...   (F18.2; budget T6(b)):
a NECESSITY budget. It is NOT sufficient (audit FATAL, sustained and
steering-re-executed): two further named inputs are consumed by any
closure of this route --
  (n1) a middle/near-word profile cap on the family: the near cap
       delta_{n+J} >= d/2 is WORD-determined, and the window cap
       admits middles up to A' L ln x > 2D for all large x (L grows
       against fixed A''), so a family whose mass sits on
       middle-heavy members has retention -> 0 at ANY density; the
       route needs the family mass carried by members with
       word-determined near-tail component <= (1 - eps) D;
  (n2) mass comparability: the conditional first moments are
       normalized by the family's TRUE window mass; bounding them by
       HLQuantA-upper NUMERATORS requires the true mass to be
       comparable to the model mass -- supplied by
       consCount_lower_bound ONLY at small span (walls w1/w2), open
       at typical span (U18.1's thinning is the predicted gap,
       (ln x)^{tau(A')}).
Consequences (re-scoped): (i) polylog-dense families with c < c*
AND (n1)-(n2) are the route's viable window -- conditional
machinery-plus-prose, NOT unconditional; (ii) a single HL-thin
class (density e^{-Theta((lnln x)^2)}) is OUTSIDE the c* budget by
an unbounded margin -- the A1 two-word route strands here
unconditionally (its T3-parallel residual); (iii) under the U18.1
thinning heuristic, even the thinned typical-span A-mass (tau(A')
= 2A'/ln2 >= 2.885 > c*) lies outside THIS ROUTE's c* window as a
single class [R2 repair, MAJOR-5: route- and heuristic-scoped]:
for the recorded route, C-layer viability is a FAMILY property,
not a class property. This is the quantitative form of
V4(iii) for this statement set.
D3(v) note (audit-scoped): the 2^{-j}-weighted summation step adds
first moments -- no marginal-to-window law there (Markov is
linear); the adjudication covers THAT step only. The
conditional-normalization step is where (n2) lives, named above.

CANDIDATE C2 (positive-density filters-first form with the F17.8
ledger; the proved layer plus the priced escape). Base form
(unconditional, proved at dossier level): for every s and x >= x_1':
    |S'^{(s)}_x| >= (1 - (1+o(1))/A' - 2/A'') N - s - o(N),
with BOTH (E4) caps inside the definition of S'_x (filters-first is
definitional, not transferred). This is P3.3'(ii) again, read as the
C-layer supply: on the full site population the tail intersection is
FREE at the D0 depths (Markov at D = ceil(13 C_0 A'' ln x)).
LEDGER CLAUSE (F17.8, explicit; trap T4-compatible: the caps are
per-site inequalities at exact positions, checkable per site): if a
route restricts to a sub-population of site-density eta(x) BEFORE
tail selection, then unconditional Markov selection inflates D by
1/eta, hence J and K by log2(1/eta) each and L by 2 log2(1/eta),
and EVERY rule-15 row re-evaluates at the inflated rank k' = L'+1:
  - eta = (ln x)^{-c}, fixed c: L' = (1+c) L (budget T6(a)):
    bounded re-budget; ADMISSIBLE (and additionally c < c* if C1's
    HLQuantA window is wanted on the same family);
  - eta = e^{-Theta((lnln x)^2)} (HL-thin class): L'/L ~ lnln x:
    SELF-DEFEAT (every superpolylog row re-inflates; budget T6(a)
    ratio column);
  - eta below any (ln x)^{-O(1)}: outside every window in this
    document.
STATUS: base form PROVED (unconditional); ledger clause is
arithmetic on top of F17.8 (standing fact). CONSUMER-FIT: supplies
(E4) verbatim and the b = 1 gate via Par' (2^J >= D: P3.3'(i));
every candidate above is stated ON S'^{(s)}_x, so C2's base form is
what makes filters-first a property of the whole statement set
rather than a per-candidate obligation.

## 5. D2 -- budget sheets (rule 15; per candidate, computed before
## the audit and before any refinement)

Script and companion tables: dossier/item-0018-workpapers/
budget_sheet.py, budget_sheet_tables.txt (deterministic; exact
local-factor arithmetic where it decides (T4 witnesses), float where
tail truncation dominates (T3), mpmath dps 40 elsewhere; stated per
table). Grid: x = 1e8, 1e20, 1e100, 1e1000 at k = (2/ln2) lnln x.
Per-candidate pointers (every k- or x-dependent constant
appearing in a candidate's BOUND appears in at least one row; the
x-free lock choices A', A'', kappa, delta, eps_C, eps_0 and
C1(n1)'s fixed profile margin enter through their consumers' rows;
the free SPECIFICATION parameters m(x) (A3(m)) and mu(x) (C1'')
are consumer-declared inputs without independent rows -- their
budget effect enters through the B1 floor/T7 reserve and the C1''
rank display respectively [R2 repair, MAJOR-9]):

  A1: T5(a) mass-floor vacuity (C = 12 vs C = 1); T5(b) small-span
      extension-sum reserve ratio (closes only near 1e1000 at
      C2 = 1: finite-scale vacuity recorded); T6(a)/(b) thin-class
      ledger rows (the c* window it strands on). Verdict rows:
      no forbidden growth in any upper-bound slot; lower-bound
      losses are k^{-Ck}-type and priced.
  A1-typ: T5(c) thinning tau(A'); T1 wall rows for every displayed
      transfer route.
  A2/C2: T0 regime; site-abundance constants are x-free (Chebyshev/
      PNT); no k-dependent factor at all.
  A3: no constants beyond delta (absolute); T1 gamma_2^k row bounds
      the compounding any S-weighted proof route would import
      ((ln x)^{0.405}: polylog, passes (G1) alone -- the route cost
      is elsewhere, U17.11).
  B1/B1': T4 exact-factor rho table (audit-repaired: sup over the
      unconstrained range is polylog and (G1)-FAILING at finite
      scales -- witnesses steering-re-executed; hence the (b1-rho)
      cap clause; typical rho subpolylog under U18.2, heuristic);
      T1 rows for the (abs) route constants (superpolylog: the
      F17.9 wall); T7 reserve after C_rel R(x).
  B2/B3: T7 consumption sheet (reserve ln x / C_F; the C_F =
      (ln x)^2-column shows why (abs)-derived constants are dead);
      T1 as for B1.
  C1: T6(b) truncated-tail window (headroom vs J_0 columns; the
      c* = 4 ln 2 - 2 = 0.7726 line); T5(a) for the thin-class
      density it excludes.
  C2: T6(a) depth-feedback ledger (inflation factors per eta-class).

Cross-checks embedded in the sheet: 2^rank = (ln x)^2 at rank
(2/ln2) lnln x (T1; the sheet's k = L+1 adds a factor 2); the
FATAL-2 display k ln k vs 2.885 lnln x (lnlnln x + 1.06) tabulated
side by side (T1; a comparison of the exact value with the
adjudication's asymptotic display, not a re-derivation claim);
theta(A') and the F17.5 deficit exponent 0.290 reproduced (T2); the
F17.5 Euler product recomputed to 4.601923 (T3).

### 5a. Decisive rows (verbatim from budget_sheet_tables.txt;
### steering re-executed byte-identically, ANN-53) [R2 repair,
### MAJOR-9: self-containedness for review]

T4 witnesses:
Audit witnesses (admissible, all-even, inside the D0 window at
the named grid depth; truncated exact-factor product, p < 1e6):
depth    span     rho       (ln x)-expo   v1-draft cap (FALSE)
1e8        222     82.24      1.514           9.80
1e20       388    221.66      1.410          11.90
1e1000   30072   1060.34      0.900          17.60
(CE at 1e20 depths: rho = 221.66 = 4.8 ln x -- (G1) fails
 outright on the unconstrained pointwise range.)


T5(a) vacuity crossings:
    -> nonvacuity crossings (v = 1), decl-indexed: C = 12 at x ~ 1e371; C = 1 at x ~ 1e45.

T5(b) w2 ratio rows (exchange-span vs small-span):
x        exch-span ratio ~ 8 A' L    small-span ratio (C2=1)
1e8              100.9                     20.03
1e20             132.6                     12.67
1e100            188.3                      4.50
1e1000           268.1                      0.79
    -> exchange-span transfer FAILS by Theta(L) even at perfect
       HL constants; small-span transfer closes for x >~ 1e1000
       at C2 = 1 (in-repo C2 is larger: finite-scale vacuity).

T6(b) c* window:
    subtraction threshold T* ~ ln x/eta.  HLQuantA card headroom:
    4 lnln x - k = (4 - 2/ln2) lnln x.  Admissible iff
    c/ln2 < 4 - 2/ln2, i.e.  c < c* = 4 ln 2 - 2 = 0.7726.
x        headroom(=4lnlnx-k)   J_0 at c=0.5   J_0 at c=0.7726  J_0 at c=1
1e8               2.25           2.10           3.25           4.20
1e20              3.27           2.76           4.27           5.53
1e100             5.06           3.92           6.06           7.85
1e1000            7.63           5.58           8.63          11.17
    -> C1-via-frozen-HLQuantA admissibility window:
       family density (ln x)^-c with c < 4 ln 2 - 2 = 0.7726;
       the A-side thinning tau(A') >= 2/ln2 = 2.885 > c* --
       a thinned single class NEVER fits; only polylog-dense
       families (small c) do.  [New datum this item.]

T7 exclusion reserve:
== T7. Consumption sheet (T5 slack sink; D4) ==
Exclusion reserve ln x / C_F after the B-layer constant:
x         C_F=O(1)   C_F=(lnx)^0.405   C_F=(lnx)^2
1e8      (lnx)^1.00    (lnx)^0.59       NEGATIVE: dead
1e20     (lnx)^1.00    (lnx)^0.59       NEGATIVE: dead
1e100    (lnx)^1.00    (lnx)^0.59       NEGATIVE: dead

## 6. Reuse audit -- candidates onto the machine-checked Counting
## layer (decl names per ANN-2f; frozen blocks read-only)

  decl (module)                      candidate   verdict
  ---------------------------------  ----------  --------------------
  consCount (Counting/Words)         A1          CONSUMED (the count
                                                 object of A1 is
                                                 consCount verbatim)
  consCount_lower_bound              A1          CONSUMED at small
  (Counting/ConsecTransfer;                      span: A1 IS this
  HLQuantA-conditional)                          decl instantiated;
                                                 see walls below for
                                                 exchange span
  consCount_bonferroni               A1          CONSUMED inside the
  (Counting/ConsecTransfer)                      decl above; the
                                                 skeleton is span-
                                                 free, the sum term
                                                 is not (wall w2)
  isConsecRealization_of_primes      A1, D4      CONSUMED (transfer
  (Counting/ConsecTransfer)                      core; also the M2
                                                 dictionary pattern)
  mem_oneExtensions_of_prime_shift   A1          CONSUMED (bad-offset
  (Counting/ConsecTransfer)                      classification)
  oneExtension_sum_le                A1, C1      CONSUMED at small
  (Counting/Lemmata)                             span; its span
                                                 hypothesis is wall
                                                 w1 at exchange span
                                                 (NECESSARY per its
                                                 own docstring)
  nuMod_insert (Counting/            RS.3, B*    CONSUMED per-insert;
  OneExtension)                                  the (K+1)-fold
                                                 composition for rho
                                                 is prose (M2-layer
                                                 candidate)
  log_singularFactor_insert_sub_le   RS.3, B*    CONSUMED per-insert
  (Counting/OneExtension)                        (collision/new
                                                 dichotomy = the rho
                                                 factor algebra)
  singularSeries, tupleCount,        RS.2/3,     CONSUMED (statement
  modelMass (Hypotheses)             A1, C1      vocabulary; C1's
                                                 tail moments bound
                                                 by tupleCount upper
                                                 shapes)
  HLQuantA (frozen)                  A1, C1      READ-ONLY hypothesis
                                                 by name; never
                                                 strengthened (D3(ii)
                                                 checks below)
  CramerGranville (frozen)           A1 note     READ-ONLY; names the
                                                 Hypothesis-B-shaped
                                                 escape of the
                                                 two-word route
  erdos_251_irrational (frozen)      --          untouched

THE TWO WALLS at exchange-typical span (the reuse audit's negative
half; both quantified in budget T5(b)):
  w1 (span hypothesis): oneExtension_sum_le requires span <=
     kappa (k-1) ln(k+1); the D0 window budget is A' L ln x,
     larger by the factor ~ ln x / ln k. The hypothesis is NECESSARY
     (the decl's docstring exhibits the unrestricted form as FALSE:
     ratio sum growing like the span), so this is not a missing
     lemma but a true regime boundary of the landed statement.
  w2 (transfer size): even granting PERFECT two-sided HL constants,
     the Bonferroni subtraction at window W = A' L ln x has genuine
     weighted size Theta(W/ln x) = Theta(L) times the ln x/8
     reserve (ratio rows 101 -> 268 across the grid): the
     consecutiveness transfer at exchange span fails on the true
     size of the extension term, not on any sieve constant. [Scope
     tag, audit-added: the LOWER-bound half of "true size" -- that
     the ratio sum really is Theta(W/ln x) -- is the growing-k
     mean-2 heuristic, U18.2-class; w1 is the PROVED half of the
     wall.] The honest exchange-span class law needs the Cramer
     thinning factor absent from modelMass (the decl's own
     docstring flags exactly this for span >> ln x).
CONSEQUENCE (F18.1): the kickoff's reuse-audit question "is A1
derivable from consCount_lower_bound-style machinery?" has a SPLIT
answer: YES verbatim at small span (A-layer becomes consumed
machinery there; the unconditional burden moves to B + C exactly
as the kickoff's desired-outcome clause anticipates), NO at
exchange-typical span (wall w1 proved; wall w2 heuristic-predicted
under U18.2 [R2 repair, MAJOR-6]; both tabulated) -- and the
small-span route re-concentrates the entire unconditional burden
onto the C-layer at thin density, where F18.2 closes the RECORDED
ROUTE's window [R2 repair, MAJOR-5].
The desired outcome is therefore booked as a reduction WITH ITS
PRICE TAG, not as a free consumption.

## 7. D4 -- consumer implication design (the prose spec M2 will
## formalize; over D3 PASS/CONDITIONAL candidates only)

Selected inputs (from D5): A2 + A3 (A-side), B2.reduced (B-side),
C2 base form (C-side, definitional) with C1 as the frontier for
restricted families. All counts on T = S'^{(s)}_x per RS.1.

### 7.1 The three named Props (final names = kickoff working names;
### D4's call, exercised: they are kept)

  MatchedFlankLower  (= A3):
    exists delta > 0, forall s, exists x_2(s), forall x >= x_2(s):
      sum over P in Fam_2(S'^{(s)}_x) of N_P >= delta |S'^{(s)}_x|.
    [Audit repair: the draft's extra clause |S'| >= 1 is dropped --
    positivity is TailIntersection's job, restoring the
    none-redundant claim below. The s-uniform delta is stronger
    than the threading needs (A3 necessity note); adopted for the
    single 7.4 gate constant.]
  RelExtensionUpper  (= B2.reduced):
    forall eps > 0, exists x_4(eps), forall x >= x_4, forall s,
    forall selections (d_P):
      sum over P of (N_{P,d_P} - 1)_+ <= eps * sum over P of N_P.
    [The o(ln x)/ln x gate is stated as the clean relative-eps form;
    C_F(x) = eps ln x recovers the kickoff display.]
  TailIntersection   (= C2 base form at the D0 pin):
    forall s, exists x_7(s), forall x >= x_7:
      |S'^{(s)}_x| >= N/4.
    [Audit repair: 1/4 is DELIVERED by C2 only under the D0 pin
    A' = 1.5, A'' = 48 (retention floor 7/24 - o(1) > 1/4 with
    margin); the dossier's example A'' = 12 gives only 1/6, and no
    A'' suffices at A' <= 4/3 -- the pin is therefore part of the
    Prop's provenance. The pigeonhole itself consumes only
    |S'^{(s)}_x| >= 1.]

None of the three is redundant: MatchedFlankLower is relative to
|S'|, RelExtensionUpper is relative to the class masses,
TailIntersection makes |S'| positive and proportional so the two
relative statements have a population to bite on, and carries the
caps definitionally.

### 7.2 The pigeonhole (trap T3, made explicit -- the F2
### anti-rigidity content)

Fix s; let x >= max(x_2(s), x_4(delta/4), x_7(s)). SUPPOSE no side
pair P has two sites n != m in F_P(S'^{(s)}_x) with g_{n+J+1} !=
g_{m+J+1}. Then every realized class is middle-rigid: all members of
F_P share one middle d_P (for singletons, d_P is the unique middle).
This defines a selection P |-> d_P with N_{P,d_P} = N_P for every P.
Then
    sum over P of (N_{P,d_P} - 1)_+ = sum over P of (N_P - 1)
      >= (1/2) sum over P in Fam_2 of N_P            [N-1 >= N/2 at
                                                      N >= 2]
      >= (delta/2) |S'^{(s)}_x|                       [MFL]
      = (delta/2) sum over P of N_P                   [RS.1 identity],
contradicting RelExtensionUpper at eps = delta/4 (which bounds the
same sum by (delta/4) sum N_P; note sum N_P = |S'^{(s)}_x| >= 1 by
TailIntersection, so the two bounds are strictly incompatible).
Hence some
class carries n != m with equal flanks (E1)+(E3) and differing
middles (E2): the abundance-minus-rigidity pigeonhole, displayed.
(With B3 in place of B2.reduced: subtract the exceptional mass first;
the contradiction survives if eps_B3 <= delta/4 and C_q = o(ln x) --
the coupled gate recorded in 7.4.)

### 7.3 ExchangeAt instantiation and t-threading (scale selection
### spelled)

Given the pair (n, m) from 7.2 at parameters Par'(1,x):
  one_le_J, one_le_K:   J, K >= 1 by construction (D0).
  block_prefix:         SameBlock n m J <=> paper g_{n+i} = g_{m+i},
                        1 <= i <= J: the class prefix match (RS.1,
                        via the T6 dictionary).
  differ:               Lean gap(n+J) = paper g_{n+J+1}: the middle;
                        differs by 7.2.
  block_suffix:         SameBlock (n+J+1) (m+J+1) K: the class
                        suffix match.
  cap_near_n/m:         delta_{n+J}, delta_{m+J} <= D: membership in
                        S'_x (D0.2' near cap).
  cap_far_n/m:          delta_{n+L}, delta_{m+L} <= 2^K: membership
                        in S'_x (far cap; 2^K >= D makes it implied
                        but it is carried verbatim, P3.3'(i)).
  gate:                 (D : R) - 2 < 2^{J+1}: P3.3'(i), 2^J >= D.
  thresholds:           n, m >= s+1 >= t for the Lean threshold t
                        with s := t (FW-3: the forall-threshold form
                        absorbs the +1/+2 offset bookkeeping; the
                        b = 1 consumer's s+2 is covered by
                        quantifying over every t).
Scale selection: for each threshold t, ONE x (any x >= the max in
7.2 with s = t) witnesses the existential of ExchangeSupply1; the
Prop's forall-t is discharged by repeating the selection per t.
Output: ExchangeSupply1 verbatim (M = 1 normal form throughout;
FW-1/F17.1 respected -- no (E2')-to-normal-form post-processing is
ever needed because the class construction IS Hamming-1).

### 7.4 The exclusion inequality and the slack ledger (trap T5:
### where o(ln x) goes)

In C_F-form the contradiction of 7.2 reads: rigidity would force
    C_F(x) >= (delta/2) ln x.
So the o(ln x) gate is consumed, in order:
  (s1) the A-side proportionality delta/2 (MatchedFlankLower's
       constant; a fixed positive factor);
  (s2) the C-side retention: if the A- or B-side proofs detour
       through window-only counts, C1's (1 - eps_C) multiplies
       delta (eps_C < 1/2 suffices: the design never needs o(1)
       retention);
  (s3) the B3 exceptional mass, if B3 replaces B2.reduced: needs
       eps_B3 <= delta/4 (coupled gate);
  (s4) the threshold truncation: absorbed in x_2(s) (A2's -s term),
       never in the constants.
ITEM-0020's REAL TARGET CONSTANT (the answer the kickoff demands):
prove RelExtensionUpper with ANY C_F(x) = o(ln x); quantitatively,
C_F(x) <= (1 - eps) (delta/2) (1 - eps_C) ln x for some eps > 0
already closes with A3's delta. If item-0019 measures delta(x) -> 0
on realized data (A3 failing at fixed delta), the coupled gate
C_F(x) = o(delta(x) ln x) replaces it -- the measurement decides
which gate item-0020 must clear (Section 8).

### 7.5 Shape map EX <-> AR (kept alive to D5, as mandated)

  EX object                          AR object
  ---------------------------------  --------------------------
  A3 twin mass (Fam_2 N_P-mass)      C_sides floor (P1(d)
                                     Cauchy-Schwarz / S-weighted
                                     variants; F17.5 battleground)
  B2.reduced / B3 concentration      C_words control: per-class
                                     Cauchy-Schwarz gives
                                     sum_d N_{P,d}^2 <=
                                     (max_d N_{P,d}) N_P, so
                                     B3-per-class + A-floor =>
                                     C_sides - C_words > 0
  7.2 pigeonhole                     P1(a) positivity reading
The AR direction of the map is exact (the displayed Cauchy-Schwarz
step); the EX direction recovers only the max-form (AR positivity
does not localize which class carries the pair -- P1(c)'s
cardinality form does, at the price of the |W| > |P| input). The
GLOBAL PAIR-COUNTING lane for item-0020 lives on the AR side: bound
sum over P of (N_{P,d_P} - 1)_+ by word-collision pair counts
against side-collision pair counts, so that no per-word sieve
constant (hence no F17.9 wall) ever appears; this is the
structurally-different exclusion device the F17.9 finding demands.

### 7.6 M2 Lean-shape sketches (statement patterns only; NO Lean
### written this run; pattern of HLQuantA / ExchangeSupply1)

Vocabulary layer (defs, consCount-pattern, all Finset-filtered cards
over Finset.range (x+1) with decidable gap-equality clauses):
  sideMatchAt (a c : List N) (n : N) : Prop  -- RS.1 clauses via gap
  classCount (a c) (s x : N) : N             -- N_P(S'^{(s)}_x); the
    filter clauses of D0.2' enter as the delta- and window-cap
    predicates already definable from gap/delta (Basic.lean) exactly
    as in ExchangeAt's cap fields
  classCountMid (a c) (d) (s x : N) : N      -- N_{P,d}
  (N_{P,d_P} - 1)_+ sums: Finset.sum over a Finset of realized side
    pairs (extracted as an image of the site set: finiteness free).
Props (statement layer, named, never proved in M2):
  MatchedFlankLower : Prop :=
    exists delta : Q, 0 < delta and forall s, exists x2, forall
    x >= x2, (twin-mass sum) * 1 >= delta * (filtered-site count)
    [rational delta avoids real-cast noise in the pigeonhole; casts
    only at the gate comparison]
  RelExtensionUpper : Prop :=
    forall epsnum epsden ..., (the eps-form of 7.1 with rational
    eps), quantified over selection FUNCTIONS d : sidePair -> N
    restricted to the realized family (a Finset -> the selection is
    a dependent choice over a Finset: encode as forall d-functions,
    classical choice not needed for the statement)
  TailIntersection : Prop :=
    forall s, exists x7, forall x >= x7, 4 * (filtered count) >= N
    (delivered by C2 only under the D0 pin A' = 1.5, A'' = 48; the
    7.1 audit note travels with the Prop).
Theorem (M2's single obligation, sorry-free target):
  supply_of_triple : MatchedFlankLower -> RelExtensionUpper ->
    TailIntersection -> ExchangeSupply1
Proof skeleton = 7.2 + 7.3: finite pigeonhole over the realized-
family Finset (sum manipulations: Finset.sum_le_sum,
card_nsmul_le_sum; the (N-1)_+ algebra), then the clause table of
7.3 (each ExchangeAt field from a filter or class clause; the gate
from 2^J >= D as a Nat.cast inequality). Estimated axiom footprint:
classical three, as consCount_lower_bound. Known M2 hazards, named
now: (i) the selection-function quantifier must range over ALL
functions on the realized family (adversarial), not a chosen one --
statement-side, cost-free; (ii) the D0.2' filter set needs a
definitional module (S'_x as a Finset with the three cap clauses);
(iii) the ANN-50 shift enters ONLY in the 7.3 dictionary (T6 fixes
it); (iv) delta/eps arithmetic stays in Q until the final cast.

## 8. D5 -- selection verdict

PRIORITY-ORDERED CANDIDATE TRIPLE (consumer-fit ordering with the
F17.1-style gloss: ">" is fit for the landed consumer chain, NOT
logical strength -- B1 gives the strongest POINTWISE conclusion on
its restricted domain but is not logically comparable with the
averaged forms [R2 repair, MINOR-2], and is ranked last):
  A-layer:  A3 (with A2 as its proved denominator layer)
            > A1 (small-span, HLQuantA-conditional; consumed
              machinery per word, but its two-word instantiation is
              additionally gated by U18.7 and it strands at
              thin-class C, F18.2)
            > A1-typ (open; thinning-corrected; statement target
              only).
  B-layer:  B2.reduced > B3 > B1'/B1 (B1's truth window is
            multiplicity-gated and rho-capped -- F18.5 and the
            corrected T4 -- and expected-inaccessible at reachable
            x pending m1; it cannot be the sole B-input at finite
            stages).
  C-layer:  C2 base form (proved; definitional filters-first)
            > C1 aggregate form for polylog-dense families (c*
              necessity budget PLUS the named closure inputs
              (n1)/(n2); conditional, F18.2 re-scoped)
            > C1'' per-class / per-thin-class (unreachable at
              exchange rank by the recorded route; blocked,
              recorded).
M2 formalizes: MatchedFlankLower + RelExtensionUpper +
TailIntersection => ExchangeSupply1 per Section 7 (shapes 7.1/7.6).

MEASUREMENT SPEC for item-0019 (exactly which measurements decide
between B1/B2/B3 and calibrate the pipeline; rational arithmetic,
primes to 1e9, (7,7) hunt as stretch per the roadmap):
  m1  class-size distribution on S'_x across a (J,K) grid spanning
      the collision frontier: singleton fraction, Fam_2 mass
      (= A3's delta empirically), mass-weighted mean multiplicity.
      DECIDES: A3 plausibility at fixed delta vs delta(x) -> 0
      (which 7.4 gate item-0020 must clear); whether B1's
      multiplicity floor is reachable anywhere below 1e9 (expected:
      no -- then B1 is dropped from the measurable set).
  m2  per-class middle concentration on Fam_2: the empirical
      REDUCED statistic (max_d N_{P,d} - 1)_+/N_P (audit-corrected:
      the reduced form is what B2.reduced gates) and its
      mass-weighted average
      = a DIRECT finite-scale measurement of C_F(x)/ln x
      (B2.reduced's constant). DECIDES B2 vs B3 (is concentration
      uniform or does an exceptional family carry it?).
  m3  local quotient census: rho(P,d) per RS.3 (exact rational per
      realized class; the (K+1)-fold insert-algebra product),
      compared against the corrected T4 exact-factor witnesses
      (including the CRT-aligned tail) and the
      even-conditioned mean-2 heuristic at growing k (U18.2).
      DECIDES: whether rho-normalization makes m2's concentration
      collapse to a scale-free law (the strongest evidence B2's
      C_F = O(1) heuristic could get short of proof).
  m4  class-conditional tail statistics: E_class[delta_{n+L}] and
      cap-failure rates vs the global means. DECIDES: C1's eps_C
      empirically (is constant retention visible?), and whether the
      truncated-tail reduction's first-moment inputs behave.
  m5  small-span thinning calibration: consCount-style consecutive
      counts vs tupleCount at matched small-span words -- the
      finite-scale shadow of tau(A') (U18.1) and the A1-vs-A1-typ
      boundary.
PROOF TARGET for item-0020 (fixing the BET-08 statement shape):
B2.reduced (= RelExtensionUpper, 7.1 form) with any C_F(x) =
o(ln x), by a global pair-counting / AR-side device (7.5) that never
instantiates a per-word sieve constant; dossier grade; Lean not
required. Fallback shape: B3 with the coupled gate of 7.4(s3).
TRANSFER TARGET for item-0021 (audit-re-scoped): C1 in its
AGGREGATE form (ex-ante family rule per the repaired C1 definition
[R2 MAJOR-4]) on polylog-dense families -- the c* = 4 ln 2 - 2
necessity budget PLUS the two named closure inputs: (n1) the
middle/near-word profile cap and (n2) the true-vs-model mass
comparability (F18.2) -- with the F17.8 ledger of C2 as the item's
spine; the deliverable is the tail-capped filters-first transfer at
family level, with (n1)/(n2) either proved on the target family or
carried as named conditions.
M2 KICKOFF PREREQUISITES (all delivered here): the three Prop shapes
(7.1) and their Lean statement patterns (7.6); the vocabulary def
list; the pigeonhole's finite-arithmetic inventory; the T6
dictionary; the hazards register 7.6(i)-(iv). M2 waits for the M1
review gate per the kickoff's Section 9.

BOTH-SHAPES CLOSURE (kickoff D1's mandate discharged): EX is
selected for the consumer chain and M2 (Finset pigeonhole,
Lean-friendly); AR is selected as item-0020's proof-device lane
(7.5); the map between them is exact in the direction the design
consumes. Neither shape is dropped.

## 9. D3 -- ex-ante no-go audit (verdicts; audited adversarially,
## adjudication in Section 9a)

Questions per kickoff D3: (i) k!/2^k/exp(k log k) growth; (ii)
secretly at least as strong as an open HL uniformity (compared
against frozen HLQuantA verbatim); (iii) caps inside the count from
the start; (iv) unproved tensorization (U17.11(a)) or growing-k
compounding (U17.11(b)) presupposed; (v) marginal statistics used as
window statistics; (vi) finite measurement treated as an asymptotic
constant.

  cand  (i)    (ii)   (iii)  (iv)   (v)    (vi)   VERDICT
  ----  -----  -----  -----  -----  -----  -----  -----------------
  A1    pass   pass   FLAG   pass   pass   note   CONDITIONAL
                                                  (HLQuantA; caps
                                                  owed to C-layer)
  A1typ pass   note   FLAG   pass   note   pass   CONDITIONAL(OI-A1)
  A2    pass   pass   pass   pass   pass   pass   PASS (proved)
  A3    pass   pass   pass   note   note   pass   CONDITIONAL
                                                  (OI-A3: window
                                                  collision
                                                  abundance)
  B1    pass   FLAG   pass   pass   pass   note   CONDITIONAL
                                                  (OI-B1); eps-form
                                                  demoted; floor AND
                                                  rho-cap mandatory
                                                  (F18.5; corrected
                                                  T4)
  B1'   pass   pass   pass   pass   pass   pass   CONDITIONAL(OI-B1;
                                                  on the capped
                                                  domain only)
  B2    pass   pass   pass   pass   pass   pass   CONDITIONAL
                                                  (OI-B2 = item-0020
                                                  target); reduced
                                                  form selected
                                                  (F18.3)
  B3    pass   pass   pass   pass   pass   pass   CONDITIONAL(OI-B2
                                                  fallback)
  C1    pass   pass   pass   pass   note   pass   CONDITIONAL
                                                  (HLQuantA + c*
                                                  necessity budget
                                                  + (n1)/(n2),
                                                  F18.2; aggregate
                                                  form only)
  C2    pass   pass   pass   pass   pass   pass   PASS (base form
                                                  proved; ledger
                                                  clause priced)

Notes behind the table (per candidate, in writing, as mandated):
  A1(i): the exp(-C k ln(k+2)) mass floor is a LOSS IN A LOWER
    BOUND -- rule 15's forbidden classes concern constants in
    upper-bound/exclusion slots; the loss is priced (T5(a)),
    including its finite-scale vacuity (D3(vi) note: the C = 12
    floor is vacuous below ~1e371; no finite measurement is being
    passed off as the constant -- the reverse: the symbolic
    constant is exhibited as finite-scale-vacuous).
  A1(ii): conditional on HLQuantA BY NAME; consCount_lower_bound is
    a proved consequence of it, so no hidden strengthening; the
    admissibility/span hypotheses restrict, never extend.
  A1(iii): FLAG sustained by design -- N^o is uncapped; the caps
    are owed to the C-layer and the thin-class window is CLOSED
    (F18.2): the flag is the finding, recorded, not absorbed.
  A1typ(ii)/(v): the thinning factor's status is heuristic
    (U18.1); it enters the honest STATEMENT of an open target, not
    a claim.
  A3(iv)/(v): the model-side support uses tensorized collision laws
    (that is why it is support, not proof -- U17.11(a) named); the
    statement itself asserts no product structure. The marginal-
    to-window evidence gap is flagged as evidence class.
  B1(ii): the (rho + eps)-precision pointwise form at growing k is
    plausibly open-HL-adjacent (a relative asymptotic of
    HL-precision on consecutive counts); it does NOT formally imply
    HLQuantA (different statistic: class-relative vs absolute
    nonconsecutive), so the classification is FLAG + demotion to
    B1' rather than FAIL(ii). Comparison executed against the
    frozen HLQuantA text: no implication either direction is
    claimed anywhere in this document.
  B1(vi): the empirical inaccessibility of the truth window (class
    counts up to 1287 at reachable x; multiplicities not in the
    corpus, rms ~ 2 inferred) is recorded so that no item-0019
    measurement is mistaken for a B1 constant.
  B2: the selection-quantifier and the reduced form remove the two
    audit risks the plain form carried (abundance entanglement
    F18.3 is a statement-hygiene finding, not a no-go); no per-word
    constant appears in the statement, so (i) passes structurally.
  C1(v): first moments add; the per-position means are summed with
    absolutely convergent weights -- no marginal law is promoted to
    a window law on THAT step (the flag checked and does not fire
    there; the conditional-normalization step carries the named
    input (n2) instead -- see C1's reduction record; recorded
    because the route superficially resembles the U17.8 pattern).
  C2: the ledger clause is arithmetic on F17.8; the base form is
    Chebyshev/PNT-only.

D3(i) GLOBAL RECORD (Section 5 binding-order rule): NO B-layer
candidate FAILS D3(i) at statement level -- the F17.9 wall lives
entirely in the (abs) proof-route sub-shape (F18.4). The kickoff's
contingency branch (every-B-fails => obstruction-shaped statement
record) is therefore NOT triggered; the averaged forms were checked
first, as instructed, and they are where the statement layer
concentrates.

## 9a. Audit adjudication record (EXECUTED)

A nine-agent adversarial audit pass (five per-candidate auditors,
one independent budget-sheet re-execution in the project's 3.5-pass
discipline, one quantifier/arithmetic pass, one corpus-fidelity
pass, one completeness critic) was run against this document at
draft state; every FATAL/MAJOR finding was steering-RE-EXECUTED
before disposition (checklist rule iv). Sustained and repaired in
place, with the repair sites marked "audit repair/audit-corrected"
inline:
- FATAL (5-of-9-agent convergence): the RS.3/T4 worst-case rho cap
  was FALSE (insert telescope bounds S(H_d)/S(H_pre) only; the
  S(H_suf) division amplifies CRT-aligned primes; witnesses rho =
  82.24 / 221.66 / 1060.3 at grid depths, steering-re-executed; sup
  = (ln x)^{1-o(1)}, (G1)-failing at finite scales). Repairs: RS.3,
  budget T4 re-derived, B1's (b1-rho) cap, B1'/F18.4/D3 re-scopes.
- FATAL (C-auditor): F18.2/C1 had upgraded the correct c* NECESSITY
  budget to sufficiency ("closes exactly"); refuted structurally
  (word-determined near-tail component: middle-heavy families of
  any density have retention -> 0). Repairs: C1 aggregate display,
  named closure inputs (n1)/(n2), C1'' per-class demotion, F18.2
  rewrite, item-0021 target re-scope.
- MAJOR (4x convergent): A3's model support mis-tagged PROVED
  against Theorem M1 clauses that certify only a (ln x)^{-2+o(1)}
  twinned-site fraction; downgraded to derivable-from-toolkit,
  write-out debt U18.6.
- MAJOR (3x convergent): TailIntersection's N/4 not delivered under
  the draft lock; repaired by the D0 pin A'' = 48.
- MAJOR (3x convergent): "class sizes 1-29" misread class COUNTS;
  corrected to the aggregate-inferred rms ~2 statistic, pending m1.
- MAJOR: A1's middle-flexibility abundance claim false for the
  exhibited construction (exactly one in-budget middle at k = 24,
  steering-re-executed); demoted to U18.7, two-word route gated.
- MAJOR: the delta-uniform-in-s necessity claim on MFL was false;
  reworded (per-s x-free delta suffices).
- MINOR/NOTE (all executed): vacuity crossings 1e371/1e45
  (decl-indexed), the 2^k rank-convention cell, B3's E-empty
  implication, the P3.3'(i) citation slip, the RS.1 site-partition
  identity, m2's reduced statistic, m3's comparison curve, the w2
  heuristic tag, arithmetic-discipline self-description, P3.2
  position-shift extension note, variant-count deviation note
  (Section 4 preamble).
No D5 selection, the 7.2 pigeonhole, the 7.3 instantiation table,
or the M2 implication design changed under adjudication; the
verdict-table diff against the body's support classes (rule-16(a)
analogue) was re-run after the repairs. Full disposition detail in
the run report (0018-report-M1.md, Observations).

## 9b. R2 adjudication record (EXECUTED)

Blind cross-family adversarial scope audit (payload S1-S9) against
the four-redaction object: verdict SOUND WITH REPAIRABLE ISSUES,
confidence 0.94, ZERO FATAL, 9 MAJOR / 5 MINOR / 7 NOTE. All
FATAL/MAJOR-class dispositions steering-re-executed before repair
(payloads/item-0018-adjudication-v1.md). Sustained and repaired in
place with [R2 repair] marks: MAJOR-1/2 (B2/B3 closed eps- and
fixed-rate forms), MAJOR-3 (A1-typ written as one exact candidate),
MAJOR-4 (C1 ex-ante cap-blind family rule, threshold-explicit),
MAJOR-5 (route/heuristic scoping of the thin-class closure
language, three sites), MAJOR-6 (w2's heuristic half qualified in
F18.1 and the Section 6 consequence), MAJOR-7 (U18.6/A3 "derivable"
downgraded to plausibly-derivable with the four missing steps
named), MAJOR-8 (C1'' side-class density claim scoped to
independently-known density), MAJOR-9 (Section 5 pointer narrowed;
Section 5a decisive rows embedded; the k = 24 middle computation
displayed with data and adjudication-re-executed), MINOR-1..5
(F18.5 domain qualifier; D5 comparability gloss; single threshold
dictionary; RS.3 positivity domain; B1' existential constant).
Reviewer-confirmed UNCHANGED: the D5 selection, the 7.1 Props, the
7.2 pigeonhole, the 7.3 instantiation (NOTE-2/3/4); both PROVED
tags sustained (NOTE-1); the 9a rho retraction independently
re-derived (NOTE-7). New adjudication observation: doubly-
extendable in-budget side pairs EXIST at k = 24 at degenerate
aspect (U18.7 note). Process observation B6: third recurrence of
the verdict-promotion pattern (item-0005 P1, item-0017 FATAL-1,
here MAJOR-5/6) -- the same-family rule-16(a) passes (in-run and
steering) missed it, the cross-family audit caught it.

## 10. Findings register (F18.n)

F18.1 (reuse audit, Section 6): SPLIT answer to the kickoff's A1
      question. consCount_lower_bound consumes the A-layer VERBATIM
      at small span (span <= kappa (k-1) ln(k+1)); at
      exchange-typical span the transfer is blocked by wall w1
      (the PROVED, necessary span hypothesis of
      oneExtension_sum_le) and, under the U18.2 growing-k mean
      heuristic, by wall w2 (the predicted Theta(L)-oversized
      extension term against the ln x/8 reserve,
      sieve-constant-independent) -- both tabulated in budget
      T5(b) [R2 repair, MAJOR-6: w2's lower-bound half is
      U18.2-class per the Section 6 scope tag]. The small-span consumption re-concentrates the
      unconditional burden on the C-layer at thin density.
F18.2 (C-layer window; budget T6(b); audit-re-scoped): within the
      frozen HLQuantA card budget, the truncated-tail C1 transfer
      REQUIRES family density (ln x)^{-c} with c < c* = 4 ln 2 - 2
      = 0.7726... -- a NECESSITY budget, not sufficiency; closure
      additionally consumes the named inputs (n1) middle/near-word
      profile cap and (n2) true-vs-model mass comparability (C1's
      reduction record), and reaches the AGGREGATE retention form
      only (per-class C1'' is unreachable at exchange rank by this
      route). Under the U18.1 thinning heuristic the A-side thinning
      tau(A') = 2A'/ln 2 >= 2.885 exceeds c* for every admissible
      A', so no single thinned typical-span class fits THIS
      ROUTE's window [R2 repair, MAJOR-5]: for the recorded route,
      C-layer viability is a family property. Quantitative form of
      V4(iii) for this statement set.
F18.3 (B-layer hygiene): the family-averaged selection form
      B2.plain smuggles abundance (average multiplicity >=
      ln x/C_F) inside an upper-bound shape; the reduced form with
      (N_{P,d_P} - 1)_+ isolates pure concentration and still
      closes the pigeonhole given A3. Statement-design rule: B
      inputs must be singleton-inert.
F18.4 (F17.9 locus sharpened; audit-scoped): the o(ln x) statement
      gate is passable -- by the SELECTION-GATED forms B2/B3, whose
      constants are bounded by the gate by construction and never
      reference rho; the superpolylog wall enters ONLY through the
      absolute-normalized proof sub-shape (per-word sieve
      constants). For the pointwise forms the claim holds only on
      B1's (b1-rho)-capped domain: the unconstrained rho sup is
      polylog and (G1)-failing at finite scales (corrected T4),
      with only the TYPICAL rho subpolylog (U18.2 heuristic).
      F17.9's "structurally different exclusion device" mandate
      remains a constraint on proof routes, not on the existence
      of gate-passing statements.
F18.5 (pointwise falsity window): WITHOUT a multiplicity floor,
      the rho-CAPPED pointwise form is false whenever a small
      class has a realized middle inside the rho <= R(x) domain,
      and the uncapped constant-o(ln x) form is false for every
      sufficiently small realized class [R2 repair, MINOR-1:
      domain-qualified] (sum_d N_{P,d} = N_P forces concentration
      at integer granularity); the honest pointwise form carries
      N_P >= (ln x)^{1+eps_0} (and, post-audit, the (b1-rho)
      cap). Corpus support for inaccessibility
      (audit-corrected statistic): no class-size census exists in
      the corpus; the 7.1 aggregates imply rms multiplicity ~ 2
      among collision classes at 1e8, far below the floor --
      pointwise B-inputs are expected-unmeasurable at item-0019
      depths, pending m1.

## 11. UNVERIFIED register (U18.n)

U18.1 The Cramer thinning factor exp(-(1+o(1)) W/ln x) for
      consecutive-vs-nonconsecutive counts at window W (tau(A')
      rows, budget T5(c)): Gallagher-frame heuristic (U17.9 class);
      used only inside the honest form of the OPEN target A1-typ
      and the m5 measurement design; never load-bearing.
U18.2 Even-conditioned d-mean of rho(P,d) equal to 2 (1+o(1)) at
      growing k (RS.3 consumer conversion; B2's C_F = O(1)
      heuristic): proved nowhere in the corpus at k ~ lnln x (the
      D1.b regime gap; upper direction fails for every displayed
      tool); k = 2 instance classical. Measurement target m3.
U18.3 B1's truth-window analysis (F18.5's Poisson-granularity
      argument) is a truth-model heuristic used to REstrict a
      candidate (adding a floor), never to assert one; a model-M
      verification of the floor's necessity/sufficiency is a
      cheap Session-B-style check for a successor run (not
      executed here: model work is out of this kickoff's scope).
U18.4 The nonvacuity construction for A1's hypothesis set
      (consecutive-primes-beyond-k tuples; middle flexibility
      count) is elementary and written at proof-sketch grain in
      Section 4.A; a referee-grain write-out belongs to the first
      run that consumes A1 (registered as write-out debt, U17.12
      pattern).
U18.5 Sections 7.6's Lean-shape sketches are statement-pattern
      forecasts; M2 may discover encoding frictions (the hazards
      register 7.6(i)-(iv)); any Prop-shape change at M2 must
      round-trip through a D5 amendment, not be absorbed silently.
U18.6 The Model-M analogue of A3 at delta = 1 - o(1): PLAUSIBLY
      derivable from the Theorem M1 toolkit only after (1) a
      uniform lower bound on the per-word match probability, (2) a
      post-dilution lower-tail argument, (3) the Par -> Par'
      filter adaptation, (4) the degree-to-Fam_2-mass conversion
      -- none written in the corpus [R2 repair, MAJOR-7]; NOT
      stated in M1, whose recorded clauses certify only a
      (ln x)^{-2+o(1)} twinned-site fraction. Write-out debt
      (audit finding, 4x convergent; R2-sustained scope); until
      discharged, A3 carries no PROVED model tag.
U18.7 Doubly-extendable in-budget side pairs: existence, at every
      working rank, of an even side pair with >= 2 admissible
      middles inside the (h2) span budget. OPEN; the consecutive-
      primes construction has exactly ONE in-budget middle at
      k = 24 (kappa = 2; audit-computed, steering-re-executed) and
      the count is nonincreasing in k. Gates A1's two-word route
      (consumer-fit note); candidate engineering target for a
      successor run (blocks with >= 2 uncovered shift classes mod
      every small prime). [Adjudication note, steering-re-executed
      2026-07-19: at k = 24, kappa = 2, the near-degenerate splits
      J in {1, 19, 20, 21} of the SAME prime run 29..137 admit 2-4
      in-budget middles (balanced splits: exactly 1) -- existence
      of doubly-extendable pairs at k = 24 is thereby WITNESSED at
      degenerate aspect; uniform existence at balanced aspect and
      growing rank remains OPEN, and few-point suffix blocks being
      weakly shift-constrained is the concrete lead for FU2.]
