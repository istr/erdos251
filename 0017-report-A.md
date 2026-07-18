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
