# Relative extension upper bound -- item-0020 verdict object (v1)

Date: 2026-07-19. Author: item-0020 runner (executor lane, Claude
Code, operator machine; model string claude-fable-5, reasoning
high), against item-0020-kickoff-v1 (operator-supplied, ephemeral,
never committed; operator-side sha256 canonical). Web OFF
(corpus-only); local code execution only (runs rule 6). Structure
per kickoff Section 5; rule-16(a) discipline: every verdict
sentence in Section 1 carries its support class inline
(proved / measured / heuristic / model-only, plus the strictly
weaker labels assessment / recorded / status used as explicit
demotions).

## 0. Scope, pin, anchors

Pin: the kickoff Section 0 pin (git 17deadb3...; HEAD == pin exactly
at session start, no rule-18 delta, PARALLEL-0022 clause not
exercised). Anchors: the nine Section 2 sha256 anchors, verified
byte-identical at session start and re-verified at close (run
report Section W5). Evidence base: the repo at the pin plus the
ANN-50 payload corpus; the two 2026-07-18 operator reports are
firewalled and cited nowhere. Scope: the B2.reduced proof campaign
(roadmap item-0020); statement shape D5-frozen; primary proof
burden the FL-1 RESTRICTED selection form; grade target: dossier
grade, Lean out of scope (lean/ read-only, untouched).

Companion workpapers: dossier/item-0020-workpapers/
{working-notes.md, mechanism-inventory.md, budget_sheet_20.py,
budget_sheet_20_tables.txt, proofs.md, audit-record.md,
item-0020-final-report.md}. Sheet references "T-n" below are
budget_sheet_20_tables.txt tables.

## 1. VERDICT (one page; support class per sentence)

The gate sentence of record (item-0019 final report Section 6,
quoted verbatim): "RelExtensionUpper with C_F(x) = o(ln x),
quantitatively C_F(x) <= (1 - eps) (delta/2)(1 - eps_C) ln x."

ANSWER: NOT CLEARED. RelExtensionUpper remains open; the run's
outcome is (S-) with a substantial proved partial layer
[assessment; the items below carry the support classes].

1. (S-) is delivered in full: every mechanism of the W1 inventory
   ends in PROVED, OBSTRUCTED(exact gap), REDUCED(named statement)
   or DEFERRED(named inputs) -- M7 via its recorded merge into
   M1/M2 (SUBSUMED) -- per the register in Sections 3 and 5
   [proved/recorded; sheet T7].
2. NEW PROVED (asymptotic, dossier grade): MatchedFlankLower (the
   7.1 A-input, candidate A3) holds at the D0 pin with delta = 1/2,
   s-uniformly -- by cardinality: the realized side-pair family has
   capacity x^{o(1)} (P3.3'(iv) pattern) against site mass
   |S'| >= N/4 (TailIntersection), so singleton mass is o(|S'|)
   [proved; Section 4 Theorem 1; crossover honesty T2: the proof
   condition opens near x ~ 1e100-1e107 at the ceil-honest D0
   depths (scale marker ~1e25), nothing claimed at reachable
   scales, where measured delta_emp ~ 2.4e-3 (measured, direction
   only)].
3. Consequence for the program: at dossier grade the supply triple
   of Section 7 (relext-statements) now hangs on RelExtensionUpper
   ALONE -- MatchedFlankLower is proved (item 2), TailIntersection
   was already proved (C2 base form); the machine-checked
   integrator supply_of_triple awaits exactly one supplier
   [proved + recorded status; the Lean Props themselves remain
   statements-only by design].
4. The 7.4 ledger consequence: eps_C does not enter this run's
   chain at all (7.4(s2) applies only to window-only detours; the
   C1/C3 chains have none), so with delta = 1/2 proved the
   pigeonhole consumption point is eps_REU = delta/4 = 1/8; the
   gate-sentence display at the conservative eps_C < 1/2 lands in
   the same class, (1-eps)^2/64 [proved arithmetic; T5].
5. NEW REDUCED(named statement): RelExtensionUpper follows --
   unrestricted selections, hence a fortiori the FL-1 restricted
   form -- from the NEW selection-free, singleton-inert candidate
   B2.pairs (the class-normalized relative pair statement,
   Section 2), with eps_REU = sqrt(eps_pair); the reduction carries
   NO k- or x-dependent constant [proved; Section 4 Theorem 3].
   The pigeonhole closes from B2.pairs at eps_pair = 1/64
   [proved arithmetic; T5].
6. The kickoff's designated M1 sufficient condition
   W2 = o(|S'^{(s)}_x|) is FALSE at the D0 depths: unconditionally
   W2/|S'| >= |S'|/cap_L - 1 = x^{1-o(1)} [proved; Section 4
   Theorem 2; finite-scale vacuity rows T3]. The un-normalized
   relative form W2 <= eps V2 does not imply RelExtensionUpper
   [proved; exact configuration, T4]. B2.pairs is the repaired
   lane; its normalization is forced, not stylistic [proved].
7. BARRIER (located obstruction, B1 discipline): the entire
   unconditional identity layer consumed by this program -- RS.1
   identities, capacity bounds, Chebyshev/PNT/Markov aggregates,
   retention, parameter arithmetic (list T, Section 4 Theorem 4) --
   holds verbatim in an explicit even Cramer-smooth deterministic
   gap system in which every realized class outside a transitional
   subfamily of absolute site mass O(L ln x) = o(|S'|) -- an o(1)
   SHARE, not o(1) mass -- is middle-rigid, and both
   RelExtensionUpper and B2.pairs are false [proved; statement
   audit-weakened to exactly what the verification proves -- the
   transitional boundary classes are non-rigid, audit-verified;
   the completeness-of-T reading ("the entire layer consumed by
   this program") is the U20.4 INVENTORY claim, not part of the
   theorem].
   No proof from T alone can exist; every route must consume an
   input that FAILS in this model -- the salient family being
   middle-slot distributional inputs [proved]. The gluing variant
   shows adjoining any finite set of measured facts changes
   nothing [proved].
8. B2.pairs itself is OPEN [status]; its truth is supported by the
   F17.2 relative room (2 ln x)^1 [model-derived/heuristic] and by
   the m2/m3 measured direction (repeated-middle mass share
   declining 0.68 -> 0.47 at (4,5,30), 0.78 -> 0.53 at (5,5,34),
   through 1e9; rho-collapse O(1) on the bulk) [measured, direction
   only, granularity-floored (O3); no finite-scale closure claim:
   at 1e9 the measured stratum-2 analogues (W2-grain ~0.47,
   B2.pairs Q-grain ~0.24) sit 1.2-1.5 orders above the 1/64
   consumption point (E3 duty)]. Alignment honesty (body qualifier
   carried verbatim): the heuristic margin thins to (ln x)^{o(1)}
   on CRT-aligned mass, whose coupled-depth share is unmeasured
   (U20.1/U20.2).
9. Coupled gate: no route of this run needed C_F = o(delta(x) ln x);
   FL-2 was never triggered [recorded]. Statement shape: unchanged;
   U18.5 was never engaged [recorded]. No STOP-AND-REPORT condition
   fired [recorded].
10. Calibration: BET-08's (S+) did not resolve this run and the
    p = 0.07 stance is unrevised by us; what changed is the
    surviving-target surface: one named statement (B2.pairs) now
    stands between the corpus and ExchangeSupply1 at dossier grade
    [assessment].

## 2. Regime and vocabulary (pointers, no copies)

D0 pin, RS.1-RS.4, 7.1 Props: dossier/relext-statements.md
(Sections 1, 3, 7). Pair-count dictionary (W2 = C_words,off,
V2 = C_sides,off vs e2prime D0.3): working-notes.md Section 5.
Capacity pattern: e2prime-supply P3.3'(iv). The NEW candidate, in
the relext-statements Section 4 pattern:

CANDIDATE B2.pairs (class-normalized relative pair concentration;
selection-free; singleton-inert). For every eps > 0 there is
x_8(eps) such that for all x >= x_8 and all s >= 0:

    sum over P in Fam(S'^{(s)}_x) of
      (1/N_P) * sum over even d >= 2 of N_{P,d} (N_{P,d} - 1)
    <=  eps * |S'^{(s)}_x|.

Quantifier prefix: forall eps exists x_8 forall x forall s (x_8
s-free, matching RelExtensionUpper's s-inside-x order). Constant
dependence: D0 pins only. Normalization: counting ratio; no rho
reference. Division safe (N_P >= 1 on Fam); inner sum vanishes on
singletons (F18.3 compliant). D3(i)-(vi): sheet T7 (all pass; (ii)
note: no implication either way against frozen HLQuantA, compared
by text). Empirical contact: the N_P = 2 stratum of B2.pairs'
numerator is exactly m2's repeated-middle pair mass (measured
declining; direction only).

## 3. Mechanism chapters (statement-grain target; sheet verdict;
## route narrative; outcome)

M1 (global pair counting, the designated lane; sheet T1-T5).
Anchored form M1.a refuted (Theorem 2): OBSTRUCTED, exact gap
W2/|S'| >= x^{1-o(1)} against the needed o(1) -- the pair-vs-site
mismatch at astronomical multiplicities, F20.1. Relative form M1.b
insufficient as consumer (T4 configuration; F20.2). Lane repaired
to B2.pairs; reduction PROVED (Theorem 3). The lane's residual
question is B2.pairs itself: REDUCED(B2.pairs). Union-sieve closure
attempts pay exp((1+o(1)) 2k ln 2k) against (2 ln x)^1 room: gap
(ln x)^{5.77 lnlnln x + O(1)}, F20.3 [proved arithmetic on the
route constants; the route is thereby dead, T1].

M2 (relative Selberg; sheet T6 M2(a)-(c)). OBSTRUCTED: wall w1's
span hypothesis is necessary and covers a vanishing sliver
(ratio rows 5.9 -> 541); full-rank route pays exp((1+o(1)) k ln k)
(F17.9 verbatim); the relative route's carrier (class-level
equidistribution at growing rank, NI-M2) does not exist in the
corpus. Exact gap: NI-M2, named. F20.4.

M3 (averaging/order-of-summation; the run's engine). PROVED
deliveries: Theorem 1 (A3.card), Theorem 2 + corollary (M1.a
falsity, V2 floor), Theorem 4 (barrier). Exhausted at its own
barrier: middle-slot-blind by construction; cannot reach the
target. Outcome: PROVED (partials) + the barrier as its reach
limit.

M4 (bilinear/dispersion; sheet T6 M4(a)). OBSTRUCTED: the
dispersion expansion consumes a word-grain upper mean value
theorem (NI-M4); the corpus's S-moment shelf (D1.b, consumed
verbatim) is a full regime square away (Kuperberg Thm 1.1) or
superpolylog (Thm 1.2 box bound; Pintz Lemma 4 direction split).
Exact gap: NI-M4, named. F20.5.

M5 (local quotient control / B3 fallback; sheet T6 M5). DEFERRED
(CONDITIONAL): statement shape recorded with its two named inputs
-- NI-M5a (alignment-mass bound <= 1/8 at some rho-cap R = o(ln x),
cap-blind ex-ante family rule; E1 binds: the realized population is
alignment-selected, "typical rho" definitions inadmissible) and
NI-M5b (= OI-B1, the capped-domain middle law). No in-corpus proof
surface; no proof investment (rule-15 discipline). Empirical note
(E2): no exceptional sub-family exists on the measured range
[measured, direction only].

M6 (signed exclusion weights; sheet T1/T7). OBSTRUCTED at word
rank (F17.9 verbatim; pair variant hits the T1 trap row);
class-level signed systems are middle-blind (merge into M3, hit
the barrier); extension-position signed systems are M2 route (ii)
(inherit NI-M2). F20.6. Merges recorded, not silent.

M7 (one-extension specificity). SUBSUMED: contributes the
dimension-1 room calculus ((2 ln x)^1, F17.2) that makes B2.pairs
plausible [model-derived], and the honesty row that aligned classes
erode the margin to (ln x)^{o(1)} (sup rho = (ln x)^{1-o(1)},
RS.3 corrected T4) [proved at witness grain in the anchored
item-0018 budget T4].
No standalone statement; carrier absent (NI-M2). Outcome recorded
in M1/M2's registers (SUBSUMED; the sup-rho witness citation is
the anchored item-0018 budget T4, RS.3 -- exempt from this
document's T-n convention).

## 4. Proof layer ((S+) not achieved; the proved partial results,
## referee grain)

The full referee-grain write-ups, with every consumed input named
and cited, are in item-0020-workpapers/proofs.md (audit-repaired
copy; in-run adversarial audit record in audit-record.md):

  Theorem 1 (A3.card = MatchedFlankLower at the pin, delta = 1/2,
    s-uniform, asymptotic). proofs.md Claim C1.
  Theorem 2 (M1.a falsity; V2 floor corollary). proofs.md Claim C2.
  Theorem 3 (B2.pairs => RelExtensionUpper, unrestricted,
    eps_REU = sqrt(eps_pair)). proofs.md Claim C3.
  Theorem 4 (identity-layer barrier; even Cramer-smooth model;
    finite-scale gluing). proofs.md Claim C4.

Consumed corpus inputs (all dossier-grade proved): RS.1 identities;
TailIntersection at the pin (= P3.3'(ii) repaired, A'' = 48);
P3.3'(iv) capacity pattern; Chebyshev C_0 inversion; gap parity;
PNT (via P3.1'-class citation). Nothing conditional, no HL input,
no heuristic is load-bearing anywhere in Theorems 1-4.

## 5. Obstruction register F20.n (per mechanism; the exact
## quantitative gap)

F20.1 (M1.a). W2 = o(|S'|) is FALSE: W2/|S'| >=
      |S'|/cap_L - 1 >= x^{1-o(1)} at the D0 depths (scale marker
      crossover ~1e28; proof-condition, ceil-honest depths,
      ~1e103-1e110; T2/T3). Gap between the anchored display and
      truth: a factor x^{1-o(1)}.
F20.2 (M1.b). W2 <= eps V2 does not imply RelExtensionUpper:
      configuration C(t) (t rigid 2-classes + one spread t-class)
      has W2/V2 = 2/(t+1) -> 0 while the reduced selection sum is
      mass/3 (T4, exact integers). The gap is the class-size skew;
      normalization (B2.pairs) repairs it exactly.
F20.3 (M1/M6 pair-sieve closure). Any union sieve at pair rank
      pays exp((1+o(1)) 2k ln 2k) = (ln x)^{5.77(lnlnln x)(1+o(1))}
      against relative room (2 ln x)^1: deficit superpolylog,
      exponent ratio rows 15.3 -> 21.3 on the grid (T1).
F20.4 (M2). w1 (necessary span hypothesis) covers a 1/ratio =
      o(1) window sliver (ratios 5.9 -> 541, T6); the full-rank
      constant is the F17.9 class; the relative carrier NI-M2
      (class-level equidistribution at rank k ~ 2.885 lnln x) is
      absent from the corpus. Gap: NI-M2 in full.
F20.5 (M4). The dispersion cross-term needs NI-M4 (word-grain
      upper mean value theorem at rank k, span A' L ln x); nearest
      shelf tools miss by a regime square (k ~ (log h) vs required
      k <= (log h)^{1/2}) or by a superpolylog box constant
      ((3 log k)^k). Gap: NI-M4 in full.
F20.6 (M6). Signed/inclusion-exclusion positivity at word rank
      costs the T1 constant class exp((1+o(1)) r ln r), r in
      {k, 2k}: F17.9 verbatim; remaining variants merge (M3: hits
      F20.7; M2(ii): hits F20.4).
F20.7 (all mechanisms; the layer barrier). The named unconditional
      list T holds in the even Cramer-smooth model where the
      target fails at the maximal order (LHS >= (1-o(1))|S'|;
      the exact maximum |S'| - |Fam| is missed by the ~ln x/2
      non-rigid boundary classes): every future route must consume an
      input that FAILS in that model (salient family: middle-slot
      distributional inputs); T-only routes are dead a priori.
      (Located obstruction w.r.t. T; no impossibility claim.)

## 6. UNVERIFIED register U20.n

U20.1 B2.pairs (Section 2) is OPEN. Heuristic support: the F17.2
      room and the pair-grain analogue of U18.2 (per-class middle
      collision rate ~ rho-average / ln x) -- U18.2-class, never
      load-bearing; measured support: m2/m3 direction only.
      Alignment honesty: on CRT-aligned mass the heuristic margin
      thins to (ln x)^{o(1)} (RS.3 sup-rho); B2.pairs' truth needs
      the aligned mass share to stay o(1)-compatible -- unmeasured
      at coupled depth (U20.2).
U20.2 Aligned-mass share at coupled depth (feeds NI-M5a and the
      U20.1 honesty clause): unmeasured; m3's fixed-row shares
      [measured] do not transfer (E1: alignment grows with depth).
U20.3 Theorem 3's sqrt-loss sharpness remark (proofs.md C3(c)) is
      configuration-sketch grade, not referee grade; the THEOREM
      is unaffected (the remark only says the loss is not slack).
U20.4 Theorem 4's tool list T is the named list; the claim "every
      unconditional fact consumed anywhere in this program's
      chains is in T" is an inventory claim audited against the
      run's own chains and the anchored counting layer -- any
      future unconditional corpus fact outside T re-opens the
      inventory, not the theorem.
U20.5 q_n = (1+o(1)) n ln n for the C4 recursion is consumed at
      standard-comparison grade (elementary ODE comparison,
      written at sketch grain in proofs.md; a fully spelled
      version is FU-grade write-out debt).

## 7. Follow-up candidates (rule-15 remarks attached; described,
## never executed)

FU1 Formalize MatchedFlankLower's cardinality proof (Theorem 1)
    toward deleting one hypothesis of the machine-checked chain.
    Rule-15: constants are capacity-only (sheet-clean); the Lean
    cost is P3.3'(ii)-formalization (real analysis: window Markov
    + PNT-class input) -- a large but bounded formalization item.
FU2 Successor proof item on B2.pairs (the surviving named target):
    the natural first sessions are (a) the pair-grain rho calculus
    on the m3 census (exact, in-corpus data), (b) subfamily
    closures under NI-M5a-style caps with the B3 ledger. Rule-15:
    B2.pairs' own sheet row is empty; all cost sits in the named
    inputs.
FU3 Measurement successor: the B2.pairs empirical eps at 1e9/1e10
    per class-size stratum (the m2 statistic is its N_P = 2
    stratum; the reduction makes the FULL statistic the right
    target). Rule-15: same kernel as m2, one extra pass; decides
    nothing asymptotic (O3), calibrates the 1/64 consumption
    point's distance.
FU4 Matched-depth delta(x) diagonal (item-0019 F1, re-endorsed
    unchanged; FL-2's separate successor).
FU5 Operator/steering: D5-standing update -- A3's status line in
    relext-statements Section 4.A ("OPEN for the primes") is
    superseded by Theorem 1 for the D0-pinned map; a v1.2
    statement-layer erratum plus BET-08 evidence-base note is
    operator bookkeeping (U18.5 round-trip NOT required: no shape
    changed; this is a status upgrade, not an amendment).
