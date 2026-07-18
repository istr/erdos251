# item-0017 Session A completion report

Date: 2026-07-18. Executor: steering lineage (Claude Fable 5,
model id claude-fable-5), against kickoff v1 (operator-ratified,
ephemeral). Session A scope per kickoff Section 5: pin + 21 anchors,
extraction agents on the new texts, D0 complete, D2/M1 drafted.
Working dossier: dossier/e2prime-supply.md (v0 DRAFT, default name,
no operator override at ratification).

## 1. Gates (Section 6 predicates + D2 gate state)

- Pin: main had advanced 96dc30c -> 66adc54 (4 commits). Anchor
  roadmap/item-0010.md CHANGED (append-only 6-line M1+M2 landing
  note); STOP-AND-REPORT fired; operator ratified "Proceed, re-pin to
  66adc54" with the faithfulness watch active. All other anchors
  byte-identical (sha256: tate-transfer.md, adjudication,
  item-0017.md).
- Hashes: all 14 item-0017 PDFs verified against payloads/HASHES.txt;
  the three formerly unbooked lines are now committed at 7ca2388 and
  match the kickoff lines verbatim.
- 21-anchor census: 14 PDF hashes + 4 document anchors + 3 chain-v1
  read-only lemma anchors (Lemma 2.2, Lemma 2.4, two_le_delta --
  statements confirmed in chain-v1 @ 66adc54). COMPLETE.
- Prohibitions (kickoff Section 3): re-read, confirmed, observed (no
  lean/ edits, no chain-v1/tate-transfer edits, kickoff uncommitted,
  ASCII-only artifacts).
- D2 gate state: M1 DRAFTED (statement + proof skeleton, dossier
  Section 3.2); M2 NOT RUN; therefore D1 remains BLOCKED per the gate
  rule. No gate decision recorded yet (Session B).

## 2. Observations

### D0 (COMPLETE, dossier Section 2)

- Definitions D0.1-D0.5 fixed verbatim per kickoff (site filter with
  the A3(a)/(b) selection order; word map; side projection pi_M with
  default M = 1; SUP'_b and normal form SUP_b^norm).
- Theorem D0.6 (EXCH' consumption): proof re-executed from chain-v1
  Lemmas 2.2-2.5 + two_le_delta; SUP'_b for all odd b => S
  irrational; SUP'_1 => S not in Z[1/2].
- P1 (pigeonhole identity): C_sides - C_words = # ordered pi-matched
  differing-middle pairs; rigidity iff equality; Cauchy-Schwarz floor.
- P2 (weighted-clause bridge): on far-capped sites, the (E2') clause
  is equivalent to the nonvanishing of the integer invariant
  E = sum_j d_j 2^{M-j}; at M = 1 every collision qualifies
  (factor-2 margin via parity); at M >= 2 the invariant is strictly
  needed (standard failure example middles (2,8) vs (4,4)).
- P3 (depth accounting): explicit parameter map Par(b,x) with all
  constants named (A = ceil(32 C_0 log2 ln x), D = ceil(13 C_0 A
  ln x), J = ceil(log2 bD), K = ceil(log2 D)); site abundance
  |S_x| >= pi(x)/2; capacity |P| <= (A ln x/2)^{J+K} = x^{o(1)}.
  DEVIATION NOTE (flagged, not absorbed): the kickoff's
  "L ~ 2 log2 log x + O_b(1)" has second-order term
  2 log2 log2 ln x (unbounded), because the per-position gap filter
  forces A to grow like L. The "~" clause survives; every consumer
  uses only L = (2+o(1)) log2 ln x.
- Faithfulness watch EXECUTED vs lean/Erdos251/Exchange.lean @
  66adc54: divergence register FW-1..FW-4, dossier Section 2.6.
  FINDING F17.1: the landed ExchangeSupply1 is strictly normal-form
  (M = 1); only SUP_1^norm feeds it verbatim; supply target set
  ordered SUP_1^norm > SUP'_1 > SUP'_b.

### Extractions (COMPLETE: 14/14, zero failures)

dossier/item-0017-workpapers/extract/, anchored anatomies with
verbatim-quote discipline and TRANSCRIPTION-UNSURE flags (counts in
parentheses). One-line yields:
- pintz13-polignac (9): Lemma 3 verbatim ("<<_k", alpha^{-k}, plus
  "also valid if we assume only H << log N" -- asserted, not proved,
  there); T1 proof pattern fully anchored ((6.1)-(6.11)); DHL*(k,2)
  + P^- clause anchored; Lemma 4 regime H >= exp(k^{1/eta}).
- pintz10-singser (6): Theorem 1/1' verbatim; upper/asymptotic
  direction needs H >= exp(k^{1/eps}) (fails at exchange depths);
  LOWER-bound direction needs only H >= exp((1/eps) k/log k), which
  eventually holds at k ~ (2/ln 2) lnln x -- regime split recorded
  for D1.b.
- kuperberg22-singseries (9): Thm 1.1 regime CORRECTED vs kickoff --
  delta > 1/2 essential, so k << (log h)^{1/2-}; Thm 1.2
  growth-free; T_k is the ordered distinct-tuple sum; no
  singular-series second moment in the text (NOT FOUND); CRT-method
  barrier quote p. 11.
- moso04-shortintervals (8): R_k(h), V_k(q;h) asymptotics at FIXED
  k; only k-uniformity remark points to Granville-Soundararajan
  restrictions; the "S second moment at growing k" tool is confirmed
  absent from the primary text (D1.c will name it).
- merikoski18-limitpoints (8): T/3 verbatim (Cor 2); syndeticity
  FOUND verbatim (Cor 3 + rephrasing sentence); Chen substitution
  LOCATED at (1.6) p. 6: pairwise upper-sieve constant A = 4 -> 3.99
  via Chen's sieve / Prop 12 (feeds D1.d); blocks story is
  9 -> 5 -> 4 (measures T/8 -> T/4 -> T/3).
- pintz15-quarter (6): "9 -> 5/4 blocks" NOT FOUND -- conflation of
  k = 9 -> 5 VALUES beta_i with measure T/8 -> T/4; actual block
  count 4m+1 with >= m+1 forced prime-containing.
- bfm14-limitpoints (8): k = 8m^2+8m CONFIRMED verbatim (Thm 1.3);
  gap values never hit exactly (limit-point approximation along
  scale subsequences); uniform Maynard-Tao Thm 4.3 hypotheses
  anchored (W a small power of N -- NOTE: stronger than the
  kickoff's "W up to eps log N" phrasing; verify wording at D3 use).
- bftb14-consecutive (5): consecutivization is a composite-forcing
  trap (dedicated prime q_t per non-tuple offset); Cor 3 constant
  residue classes a mod D, D fixed; engine is Granville's Thm 6.2
  formulation; fixed-m, no counting uniformity.
- fmt15-chains (8): Thm 1 verbatim with absolute effective constant;
  NOTHING controlled at chain flanks (internal gaps only) -- T5/D3
  datum.
- bf15-erdosrankin (6): R(T) = log T log_2 T log_4 T/(log_3 T)^2;
  EXACT window confinement (P cap (n+x, n+y] = P cap n+H for every
  n == b (W)) -- strongest prescription mechanism in the corpus, at
  Erdos-Rankin scale, skeleton positions prescribed only to
  width-x/log x subintervals; scale class = compositions of first/
  second-kind functions (Defs 5.1/6.1).
- pintz14-gapdist (6): class F cap verified = Erdos-Rankin scale
  g(x) log x exactly; NO chain analogue of the normalizer theorems
  (NOT FOUND) -- T5 transport datum.
- gl20-heuristics (3): both models verbatim (basic Cramer p. 19,
  divisibility-corrected p. 20); flaw list; model-language
  exemplars -- D2 frame anchors resolved.
- hm88-chains (5): positive-measure limit-point cube theorem
  verbatim; matrix method prescribes only the AVERAGE gap ratio,
  counts boxes; NO explicit k-vs-x uniformity in the paper.
- maier85-matrix (4): rasterization-only extraction; matrix
  construction anchored; both selection steps are averaging
  pigeonholes -- counts, never gap values; modulus Q = x^{1/D}.

### D2 (M1 drafted)

Dossier Section 3: model M fixed (verbatim GL p. 19 anchor); M1
statement + proof skeleton with the two named Session B obligations
(covariance table, greedy-matching floor); kickoff's "x^{1-o(1)}
qualifying pairs" pinned to the disjoint-pair count (ordered count
x^{2-o(1)}). M2 pending (Session B), gate decision pending.

### D5.c (started early; gate prerequisite)

balance_stats.py written under item-0017-workpapers/stress/,
validated at x = 2e6 (reproduces the committed exchange-class counts
12 / 2 at (4,5,30) / (5,5,34)); 2e7 and 1e8 runs in flight.
Calibration data already landed: (a) naive model side-collision rate
underestimates reality ~3.4x per position (parity + clumping) -- M2
must carry this correction when compared to primes; (b) S-site
moments tame (S2/S1^2 in [1.32,1.51]); (c) lambda_w >> 1 everywhere
reachable (sub-1-mass corner) -- D5.c calibrates shapes, not the
asymptotic constant. Container probe (once): 1e8 in-core OK; 1e9
only with segmented sieve (D5.a decision deferred).

### Register state

U17.1 RESOLVED (syndeticity verified verbatim; "9 -> 5/4 blocks"
exposed as a conflation -- see dossier Section 8 for exact quotes).
U17.3 RESOLVED with a kickoff correction (delta > 1/2 constraint).
U17.4 RESOLVED (GL anchors). OPEN: U17.2 (C_sel heuristic -- D1.a),
U17.5 (pc_wordcount.py absent from committed tree; kickoff list
inexact), U17.6 (M1 skeleton obligations). Findings: F17.1
(normal-form-only Lean interface).

## 3. Follow-up candidates (none executed)

- Session B (next): M1 full proof; M2 computation + GATE DECISION
  recorded in dossier Section 1; then (gate permitting) D1.a
  (self-proved Selberg constant) and D1.b (Kuperberg averaging,
  regime gap stated); D5.a/c completion (2e7/1e8 tables into the
  dossier appendix; 1e9 segmented-sieve decision).
- Candidate for D3/D4 (Session C), noted from extractions: BF15's
  exact window confinement is the sharpest prescription mechanism in
  the corpus and deserves its own D3 row; Maier-matrix answer to D4
  is pre-shaped ("counts, never gap values" -- both selection steps
  are averaging pigeonholes).
- Bookkeeping candidate for the operator: kickoff seed-script list
  names pc_wordcount.py which does not exist in the committed tree
  (U17.5).
# item-0017 Session B completion report

Date: 2026-07-18. Executor: steering lineage (Claude Fable 5,
claude-fable-5), continuing the Session A run (compression at
steering discretion; gate order honored). Dossier:
dossier/e2prime-supply.md on branch item-0017.

## 1. Gates

- Section 6 predicates: unchanged from Session A (pin 66adc54
  ratified; hashes verified; prohibitions observed).
- D2 GATE: M1 + M2 COMPLETE and independently checked. DECISION:
  PASS WITH AMENDMENTS (dossier Section 3.4) -- the model balance
  closes a.s. along dyadic scales, so D1 is not architecturally
  dead; binding amendments F17.2 (room is (2 ln x)^M per middle
  position, NOT the kickoff's "(log x)^{2-o(1)}") and F17.3 (D1
  must run on the new aggregate filter D0.2'; the pinned
  per-position filter kills the floor route even in the model).
- Gate order: D2 completed before any D1 execution; D5.c empirical
  landing preceded D1-route trust (kickoff rule honored).

## 2. Observations

### D2 (COMPLETE)

- Theorem M1: model supply a.s. along dyadic scales -- x^{2-o(1)}
  ordered (E2')-pairs, x^{1-o(1)} disjoint pairs (explicit floor
  N_S (ln x)^{-2+o(1)}); full proof with covariance table and
  greedy-matching floor (U17.6 discharged).
- M2: expectation balance closes with relative room (2 ln x)^M;
  concentration; route audit produced the capacity-slack finding.
- Independent re-derivation pass: M1 checker CONFIRMED all
  constants (one proof refinement absorbed: residue-class dilution
  in the degree Chernoff); M2 checker PARTIAL on decimal places
  only (2.08104, theta(2) = 0.1146, theta(1.5) = 0.9447 -- all
  absorbed); no conclusion affected.

### New findings (F17.2-F17.8; dossier Sections 3-6)

- F17.2 room correction; F17.3 capacity-slack obstruction + the
  aggregate-filter repair D0.2' with threshold A' < 4 sqrt(2)/e =
  2.08104 and room exponent theta(A') = 1 - (2/ln 2) ln(e A'/4);
  P3.3' restores the kickoff's L = 2 log2 log x + O_b(1) form.
- F17.4 post-fix D1.a budget: room 2^{theta L/2} vs C_sel ~ 2^L L!.
- F17.5 (the session's sharpest new datum): collision-constant
  closure of the unweighted floor route. General threshold
  A'_crit = 2 sqrt(2)/(e gamma_2); the primes' gamma_2 exceeds the
  critical 1.0405 in every measurement (marginal 1.20/1.18 at
  2e6/2e7; vector-level 1.68/1.58/1.55 at 2e6/2e7/1e8) and at the
  heuristic asymptote E_even[S_2^2]/4 = 1.150481 (Euler product
  4.601923, CONFIRMED by direct summation 4.601842 at D = 2e6).
  The route is closed for the primes at every admissible A' > 1,
  independently of the sieve constant, invisibly to the model
  (gamma_2 = 1/2) -- HL clumping both supplies exchange
  configurations and defeats the max-entropy capacity floor. The
  margin is strikingly thin: 1.1505 vs 1.0405 (ratio 1.106).
- D1.b COMPLETE: Kuperberg Thm 1.1 regime gap is a full square
  (k linear in log h vs required k << (log h)^{1/2}); Thm 1.2's
  growth-free box average (3 log k)^k exceeds every polylog room;
  Pintz Lemma 4 upper direction fails at our depths while the
  lower direction holds (direction split recorded). The missing
  estimate "S second moment at growing k" confirmed absent from
  MoSo (fixed k) and Kuperberg (k << (log h)^{1/2}).
- D3 table drafted (pulled forward): per-mechanism reach rows
  T1-T6 + Maier matrix; blockers confirmed exhaustive for the
  corpus; the sparse-site Markov cost (F17.8) identified as the
  uniform mechanism behind every tail-typicality failure. F17.6:
  T5 transport dies at exactness + tail typicality, NOT at the
  (E5) b-D coupling the kickoff expected. F17.7: Pintz-Thm-5
  transplant reduces (E2)-supply to ONE missing input (HL-type
  class-count lower bound for a single matched-flank family) --
  the sharpest positive lead.
- D4 addenda drafted: Shiu circularity at the weighted clause
  killed by the M-invariant depth floor J+K >= (2+o(1)) log2 ln x
  (exact inequality recorded); pigeonhole blindness strictly
  finer at M >= 2 (E = 0 degeneracy); prescription burden
  M-invariant; Maier matrix joins the register (variability-blind
  + x^{1/D}-sparse columns).

### D5

- D5.c grid complete at 2e6/2e7/1e8 (dossier Section 7.1):
  reproduces the committed class counts (12/178/1287, 2/21/143,
  first (6,6,64) at 1e8); vector gamma_2 trend 1.68/1.58/1.55;
  S-site moments stable [1.32, 1.51]; scripts committed
  (balance_stats.py, d1c_gamma2.py).
- D5.b launched at 1e9 in-core (container probe: 88 GB free;
  ~6 GB peak): deeper firsts (7,7)/(8,8), b in {3,5} certificates
  honoring (E5), (6,6) continuity. Results land next commit.

### In flight

- D1.a: the self-proved k-uniform Selberg constant (workpaper
  d1a-selberg.md) by a max-effort agent; lands with the D1.a
  balance run in the next commit.

## 3. Follow-up candidates (none executed)

- Session C: finalize D1.a (verify the agent's derivation
  steering-side), D1.c (name the S-second-moment estimate
  precisely, assess MoSo machinery), D1.d (Chen-substitution
  reach statement); harvest D5.b; at least one new inline
  certificate into the dossier (acceptance clause).
- Session D: verdict Section 1, obstruction statement assembly
  (the acceptance-intent "named obstruction per blocker with exact
  quantitative gap" is now substantially pre-written by
  F17.3/F17.5/F17.7/F17.8 + D4), review payload build (strip
  script), R1/R2 blind reviews, adjudication, closure.
- For the operator (bookkeeping): U17.5 (pc_wordcount.py absent
  from tree); U17.7 (first project use of PNT, in P3.1' only).
# item-0017 Session C completion report

Date: 2026-07-18. Executor: steering lineage (Claude Fable 5,
claude-fable-5), same run as Sessions A-B (compression at steering
discretion). Dossier: dossier/e2prime-supply.md, branch item-0017.

## 1. Gates

- Section 6 predicates: unchanged (pin 66adc54 ratified; hashes
  verified; prohibitions observed; kickoff sha256 re-verified
  against ledger ANN-50's canonical value -- match).
- D2 gate: PASS (recorded Session B); order honored throughout.

## 2. Observations

### D1.a (COMPLETE; the heaviest deliverable of the item)

Workpaper item-0017-workpapers/d1a-selberg.md (618 lines,
self-contained): k-uniform Selberg upper bound
  N(X;H) <= C(k)(1+err) S(H) X/(ln X)^k,
  C(k) = 2((8k+2) e^{-gamma})^k,  err <= 20 k^2 lnln X/ln X,
valid for k <= (lnln X)^2, span <= (ln X)^2, X >= exp(exp(30));
optimized C*(k) <= (6.11)^k k! e^{1.45 sqrt k} for k >= 5. External
inputs: four Rosser-Schoenfeld inequalities only (numbering
memory-cited: U17.10); no Halberstam-Richert, no PNT. Honesty
layer: the self-contained constant exceeds the classical 2^k k! by
~(3.06)^k (inherent to the Rankin-truncation route; workpaper
Section 13 traces every factor). STEERING-VERIFIED by re-execution
of the core steps (Rankin tail, Delta >= 0.7543, Mertens assembly,
constant-gap ratios).
BALANCE RUN: in-regime (k = L+1, span fine), the max-S balance
fails by exp((1+o(1)) L ln L) already at S-term = 1 -- the
kickoff's predicted "2^L L!"-type failure, self-proved, and
robust (the classical constant fails identically). DOUBLE KILL
with F17.5 (which binds even at C_per = 1).

### D1.c / D1.d (COMPLETE)

- D1.c: "S second moment at growing k" named precisely (dossier
  4.4); its k = 2 ground truth IS the F17.5 constant 1.1505 -- the
  S-weighted repair funnels into HL lower bounds at matched flanks
  (blocker 2) with no constant to spare. MoSo confirmed fixed-k
  (centered moments, box domain); Kuperberg k << (log h)^{1/2};
  the tool gap is genuine AND its two-point value is exactly the
  closing constant.
- D1.d: Chen substitution mapped (dossier 4.5): a 0.25% pairwise
  gain, category-mismatched to both critical spots (true-mass
  closure not a sieve constant; per-word deficit super-exponential).
  Best current pairwise value 3.99 recorded. A located non-lever.

### D5.b (COMPLETE; x = 1e9 in-core, pi(1e9) = 50,847,534)

- FIRST b > 1 CERTIFICATES of the project: inline (7,6,44,3), gate
  126 < 256, d_1 = -24, residual -1.78e-15, HAND-VERIFIED gap by
  gap; (7,6,27,5) on the same sites (gate 125 < 256); 3 classes
  each. One constellation kills b in {1,3,5} (its 1-shift is a
  (6,6,64) b = 1 pair).
- Frontier: (7,7)/(8,8) have ZERO side collisions at 1e9 --
  consistent with the collision calculus (expected ~0.5); first
  (7,7) pairs predicted near 5e9-1e10 (executor-slot candidate).
- (6,6,64): 1 -> 29 classes from 1e8 to 1e9; widest pair spans
  anchors 267,737 vs 979,591,577.
- Acceptance clause's certificate sentence: DISCHARGED.

### Verdict

Section 1 v1 complete, all pending slots closed: obstruction
branch delivered with named obstruction per blocker and exact
quantitative gaps (V2/V3), architecture model-consistent (V1),
single sharpest residual isolated (V4: one HL-type class-count
lower bound at matched flanks; exclusion side available via D1-L),
interface order (V5), certificates (V6).

## 3. Follow-up candidates (none executed)

- Session D (next): payload build via strip_payload.py (drop-table
  refinement), R1 same-family fresh-role blind review (web OFF,
  payload + object only); then STOP-AND-REPORT to the operator:
  R2 cross-family review is operator-side by B2 architecture, and
  closure (emit-patch, ledger ANN, BET-07 note) waits on operator
  ratification of the verdict.
- Successor item candidate (from V4/F17.7): "matched-flank
  class-count lower bound" as its own research item (the
  adjudication-F2 anti-rigidity statement, now with the exclusion
  side pre-built and the exact budget known).
- Executor-slot candidate: (7,7) first-pair hunt at 5e9-1e10
  (segmented sieve).
# item-0017 Session D completion report + OPERATOR HANDOFF

Date: 2026-07-18. Executor: steering lineage (Claude Fable 5,
claude-fable-5), one continuous run for Sessions A-D (compression at
steering discretion; all binding gate orders honored). Branch:
item-0017 (five commits; main untouched). THIS REPORT IS A
STOP-AND-REPORT: everything below the "Operator package" line needs
operator action; nothing further is executed by this run.

## 1. Gates

- Section 6 predicates: held all session (pin 66adc54 operator-
  ratified at start; all 21 anchors; kickoff sha256 = ledger ANN-50
  canonical value; prohibitions observed -- no lean/ edits, no
  chain-v1/tate-transfer edits, kickoff uncommitted, roadmap
  untouched, ASCII-only artifacts).
- D2 gate: PASS with amendments (Session B), order honored.
- Review gate: R1 EXECUTED (blind, computation-mandatory);
  R2 operator-side, pending. Closure NOT executed (ratification-
  gated): no roadmap emit-patch, no ledger append.

## 2. Observations (Session D)

- Review object built with the committed deterministic strip script,
  leak-audited: payloads/item-0017-review-object-v1.md, sha256
  5a7a2647d11ec40d00b2d2ae2473bfdfd2a32a22ab731b7fe93dfe97b85fbb63.
- R1 (same-family fresh instance, web OFF, exactly payload+object):
  VERDICT "SOUND WITH REPAIRABLE ISSUES", confidence 0.89, ZERO
  FATAL. The full numeric spine reproduced independently (Euler
  product exact; both certificates to machine precision incl.
  primality/consecutiveness of all 32 printed primes; an
  INDEPENDENT full 1e9 census matching 29/3/3/0/0; every committed
  grid record). Review registered:
  payloads/item-0017-review-r1-v1.md.
- R1 findings: 1 MAJOR + 4 MINOR + 6 notes; every finding
  steering-RE-EXECUTED before absorption (checklist rule iv), all
  repaired in place with marked amendments (dossier Sections 2.5,
  2.7, 3.2, 3.3, 4.3): the one genuine lemma-level error was
  P3.2's threshold (N >= L+16 -> N >= 40(L+2)); the rest were a
  statement/proof factor 2, an exponent value-substitution, a
  vacuous abundance gloss near A' = 1, and an intermediate
  constant. NO verdict clause changed under repair (R1's
  assessment, re-confirmed clause-by-clause). R1's bonus
  measurement gamma_2(1e8) = 1.1711 adopted (decline toward the
  1.1505 asymptote continues).

## 3. Item state after Sessions A-D

The mandate's disjunction is discharged on the obstruction branch:
- Named obstruction per blocker with exact quantitative gaps
  (dossier Sections 4-6; F17.2-F17.8), the sharpest being the
  collision-constant closure F17.5 (E_even[S_2^2]/4 = 1.150481 vs
  critical 2 sqrt(2)/e = 1.040520; margin ratio 1.106) and the
  double-kill of D1.a (self-proved k-uniform Selberg constant,
  deficit exp((1+o(1)) L ln L)).
- Certificate layer extended: first b > 1 certificates (b = 3
  inline, hand- AND R1-verified; b = 5 same constellation; one
  constellation kills b in {1,3,5}); (7,7)/(8,8) frontier located
  at 1e9 with collision-calculus consistency; (6,6,64) 1 -> 29.
- The single residual (V4/F17.7): one HL-type matched-flank
  class-count lower bound at k ~ L; exclusion side pre-built by
  D1-L. Successor-item candidate.

## 4. Operator package (ACTION REQUIRED)

(a) R2 cross-family review (B2 architecture; cannot be run from
    this environment). Hand to a cross-family model EXACTLY these
    two files:
      payloads/item-0017-review-object-v1.md
        sha256 5a7a2647d11ec40d00b2d2ae2473bfdfd2a32a22ab731b7fe
        93dfe97b85fbb63
      payloads/item-0017-review-r2-payload-v1.md  (scope audit)
        sha256 f18f0bc02cc9808dbccb05ffbf014b2430d250bdce3be1c98
        da4a68805fdbdf6
    NOTE: the object is the SESSION-C state of the dossier (R1 and
    R2 review the same object; the post-R1 repairs are visible to
    the adjudication, not to R2 -- same-object blindness preserved).
    Optional per R1's confidence note: widen R2's file set with
    dossier/item-0017-workpapers/d1a-selberg.md (stripped) if you
    want the sieve-constant internals cross-audited.
(b) After R2 returns: adjudication (point-by-point disposition of
    R1+R2, v2 revision of the dossier if sustained findings
    require it) -- steering executes on request; then operator
    ratification of the verdict.
(c) Closure after ratification (NOT executed now): roadmap
    emit-patch (item-0017 done-move via the roadmap skill); ledger
    ANN append. Draft ANN body for your editing:
      "item-0017 Sessions A-D executed by steering lineage (Claude
      Fable 5, claude-fable-5, ultracode + workflows) in one run
      against kickoff v1 (sha 45591703..., operator-ratified;
      session-A STOP-AND-REPORT on the item-0010.md anchor delta
      ratified as re-pin to 66adc54). Branch item-0017: dossier
      e2prime-supply.md v1 (obstruction branch; D2 gate PASS;
      F17.1-F17.8; U17.1-U17.10), 14 anchored anatomies, committed
      workpapers (balance_stats, d1c_gamma2, d5b_deep,
      d1a-selberg 618-line self-contained k-uniform Selberg bound,
      strip_payload), D5 grid at 2e6..1e9 with the project's first
      b > 1 certificates, R1 blind computation audit (SOUND WITH
      REPAIRABLE ISSUES 0.89, zero fatal; all findings repaired,
      marked, registered). R2 cross-family + adjudication +
      ratification pending operator. K1 handshake honored (D0
      targets width 1 primarily; F17.1 converges with ANN-50 K1)."
(d) BET-07 relevance (resolve_by 2026-08-08, "unconditional
    progress", p = 0.03): this verdict is further evidence AGAINST
    unconditional progress (obstruction branch taken; the model
    gate PASS and the certificate layer are understanding progress,
    not unconditional theorem progress). Resolution is the
    operator's call, per the tate-transfer precedent.
(e) Bookkeeping flags for you: U17.5 (kickoff lists
    pc_wordcount.py, absent from the committed tree); U17.7 (first
    project use of PNT, P3.1' only); U17.10 (R-S equation numbers
    in d1a-selberg.md memory-cited; verify against the 1962 paper
    before any external circulation); payload hashes above not yet
    booked in payloads/HASHES.txt (operator-side sha256 canonical).
(f) Branch merge: item-0017 branch (5 commits) is ready for your
    review/merge at your discretion; main was never touched.

## 5. Follow-up candidates (none executed)

- Successor item: "matched-flank class-count lower bound" (the V4
  residual; adjudication-F2 anti-rigidity form; exclusion side and
  budgets pre-built).
- Executor slot: (7,7) first-pair hunt at 5e9-1e10 (segmented
  sieve).
- Lean extension layer (only if ever needed for consumption):
  weighted-(E2') generalization of ExchangeAt (per K1 and FW-1).

## 6. ADDENDUM (post-R2 adjudication + v2, same date)

R2 (GPT-5.6 Sol, cross-family) delivered operator-side:
payloads/item-0017-review-r2-v1.md, sha256
6fc1f7f7a469fa44e2b5b3154f3c2fa0c11f8cf0137914a8e598026c490889c0.
Verdict UNSOUND (0.96), 2 FATAL + 7 MAJOR, scope-audit class.

Adjudication executed (payloads/item-0017-adjudication-v1.md),
every disposition steering-re-executed:
- FATAL-2 SUSTAINED SUBSTANTIVELY (the one content error): v1-V4's
  claim that D1-L's exclusion budget absorbs the rigid-middle
  exclusion was FALSE (needs C_per(k+1) < c ln x; every displayed
  constant, classical 2^k k! included, is exp((1+o(1)) k ln k)
  >> ln x). V4/F17.7 rewritten; new finding F17.9 (growing-k
  exclusion-constant wall; a successor item needs a structurally
  different exclusion device, not a better Selberg constant).
- FATAL-1 SUSTAINED AS WORDING (item-0005 P1 pattern recurred):
  V2's "exactly closed" promoted the body's labeled
  heuristic+measured closure to an unconditional primes claim;
  rewritten; tensorization + growing-k compounding registered
  (U17.11).
- MAJOR-1 sustained (M1 concentration layer): repaired at sketch
  grade (truncation, insertion-Lipschitz, caps-conditioning);
  write-out debt U17.12.
- MAJOR-2/-6, MINOR-2: CONVERGENT with R1 m-3/M-1/m-1 -- three
  independent cross-family convergences on identical defects
  (process finding B3), all already repaired post-R1.
- MAJOR-3/4/5/7, MINOR-1/3/4, NOTE-2: sustained as wording; all
  executed in v2.
- Two minor corrections to R2 recorded (Euler-product exactness;
  headline-vs-body locus of the alleged inconsistency).

Dossier is now v2. Mandate outcome unchanged in kind (obstruction
branch; acceptance clause still discharged: named obstructions
with exact gaps, now honestly scoped, + certificate layer). The
verdict's strongest clauses now carry route/corpus/evidence scope
inline; the residual (V4) is a TRIPLE requirement.

OPERATOR DECISIONS NOW DUE:
(1) Ratification decision on the v2 verdict (or further revision
    instructions).
(2) Whether to show R2's reviewer the v2 delta for a closing
    comment (adjudication Section 6 option).
(3) Closure on ratification: roadmap emit-patch + ledger ANN
    (draft in Section 4(c) above, now also citing R2, the
    adjudication, F17.9, U17.11/12, and process findings B3-B5).
(4) payloads/HASHES.txt booking for: review object, R1/R2
    payloads, R1 review, R2 review, adjudication (sha256 list in
    Sections 4(a)/6 and the adjudication preamble).
(5) Untracked operator file deep-research-report.md (German
    literature survey on the S-weighted repair's input (ii);
    corroborates the D1.c gap beyond the corpus): left uncommitted
    and NOT absorbed into the dossier -- out-of-corpus evidence
    under the identification duty; absorb only after
    item-0004-style primary verification, at operator discretion.
