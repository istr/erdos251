# item-0018 M1 completion report -- relative extension statement layer

Date: 2026-07-19. Runner: steering lineage, fresh instance; model
string claude-fable-5 (Claude Fable 5), ultracode + workflows,
reasoning high (execution_profile per roadmap/item-0018.md). Kickoff:
item-0018-kickoff-v1.md, disk sha256
44c07d99a1f00730d58a643469042b2f155a798990b61a987388c684b960f818
(operator-side sha256 canonical; see the pin/hash record below).
Web OFF honored: no network/literature tool was invoked at any point
(corpus-only); local code execution used throughout (python3, sympy,
mpmath) per runs/README rule 6; the in-run adversarial audit used
nine local subagents (workflow fan-out), each itself corpus-only.
Out-of-corpus firewall honored: the two 2026-07-18 operator reports
are cited nowhere; the k = 2 inflation constant enters only through
the in-repo F17.5 Euler product, independently recomputed (budget
T3).

## 1. Gates (Section 7 of the kickoff; outputs verbatim)

- git rev-parse HEAD
    32b91ea92d73cfb667a5e85c4f6f4db27ba0474a
- python3 lean/scripts/blocks.py check-frozen
    OK erdos_251_irrational / HLQuantA / CramerGranville;
    "FROZEN BLOCKS: all byte-identical."
- python3 lean/scripts/blocks.py relocation-check
    "RELOCATION CHECK PASSED -- concatenation is byte-identical to
    the old body."
- grep -rcE '^\s*sorry\s*$' lean/Erdos251 --include='*.lean'
    lean/Erdos251/Statement.lean:1; every other file 0.
- roadmap/item-0018.md: status: ratified.

PIN / HASH RECORD (deviation, not silently absorbed). The kickoff's
Section 7 first predicate reads HEAD == 8cb5086... while its own
Section 0 pins main = 32b91ea... (the actual HEAD). Resolution
executed: the kickoff on disk is a post-bookkeeping revision of the
version ANN-51 records (steering sha256 57655d5a..., authored at pin
8cb5086); git diff 8cb5086..32b91ea touches ONLY bookkeeping (report
shards, HANDOVER, ledger, HASHES, roadmap, runs/README) -- every
Section 2 read-only anchor is byte-identical across both states, and
runs/README rule 15, which this kickoff binds to, exists only at
32b91ea. Per the item-0017 precedent ("kickoff read-only anchors
unchanged ... session A pins to" the new HEAD) the session pinned to
32b91ea; the stale Section 7 line and the superseded ANN-51 steering
hash are recorded here for the operator to reconcile (the operator-
side sha256 of the REVISED kickoff, 44c07d99..., should enter the
bookkeeping at close; steering cannot self-certify it).

## 2. Writes-scope diff (worktree at close; exhaustive)

git status --porcelain:
    ?? dossier/item-0018-workpapers/     (budget_sheet.py +
                                          budget_sheet_tables.txt)
    ?? dossier/relext-statements.md      (v1, the M1 deliverable)
    ?? item-0018-kickoff-v1.md           (operator's own ephemeral
                                          file; pre-existing, not a
                                          run write, never committed)
    plus this report, 0018-report-M1.md.
Exactly the Section 6 writes and NOTHING else: zero edits under
lean/, ledger.yaml, roadmap/, payloads/, runs/, HANDOVER.md.
Deliverable hashes (steering-computed; operator sha256 canonical):
    relext-statements.md
      be3b9e625d7c9b39417e626504d471407ade0596682e80803e20c9abd28e09c8
    budget_sheet.py
      129b39fbd2926e7e8ab56a26ac85d84bfc148dde97779ad04ef2809ba946530d
    budget_sheet_tables.txt
      e4e070d721f564dd728ffb4a633a00ef476bca08e739dd37ad9aa8fbc4cfd302

## 3. Run structure (kickoff Section 9 split, honored in one run)

Session A equivalent: D0 regime lock + T6 dictionary smoke test
(executed BEFORE D1; the (7,6,44,3) certificate re-derived from the
printed primes, primality/consecutiveness re-checked, ANN-50
dictionary fixed, both (E5) gates verified) + D1 candidate drafting.
Session B equivalent: per-candidate rule-15 budget sheets (committed
script + tables) BEFORE the no-go audit; then a NINE-AGENT
adversarial audit pass against the drafted document (five
per-candidate refuters, an independent budget re-execution in the
3.5-pass discipline, a quantifier/arithmetic pass, a corpus-fidelity
pass, a completeness critic), adjudicated with every FATAL/MAJOR
steering-re-executed before disposition (checklist rule iv).
Session C equivalent: D4 consumer design + D5 selection verdict +
repairs folded in + this report. Binding order D0 -> D1 -> (D2 then
D3 per candidate) -> D4 -> D5 was honored; the in-run audit is the
M1-internal quality pass, NOT the operator-side M1 review gate
(Section 6 below).

## 4. Observations

O1 (mandate outcome). The M1 statement layer is DELIVERED: eight
   primary candidates with sub-variants (A1/A2/A3; B1/B2/B3 with
   B2.reduced; C1/C2), each with full quantifier prefix, uniformity
   range, constant dependence, normalization, rule-15 budget sheet,
   and a written six-question no-go audit; a reuse audit over all
   eleven named Counting decls; the D4 derivation Selected-A +
   Selected-B + Selected-C => ExchangeSupply1 with the pigeonhole
   displayed (trap T3), the t-threading spelled, the b = 1 gate
   production from Par', and the T5 slack ledger; the D5 selection
   verdict fixing item-0019 measurements (m1-m5), the item-0020
   proof target (B2.reduced at C_F = o(ln x) -- matching the
   BET-08 registration's deferential shape clause), the item-0021
   transfer target (C1 aggregate, c* necessity budget + named
   closure inputs), and the M2 prerequisites (three Props named
   MatchedFlankLower / RelExtensionUpper / TailIntersection, with
   Lean statement patterns and a hazards register; no Lean
   written). Both target shapes (exclusion form; anti-rigidity
   counting form) were kept alive to D5 and mapped onto each other
   (Section 7.5 of the deliverable).
O2 (headline mathematical findings, F18.1-F18.5). (1) The
   kickoff's reuse-audit question has a SPLIT answer:
   consCount_lower_bound consumes the A-layer VERBATIM at small
   span; at exchange-typical span the transfer is blocked by two
   quantified walls (the decl's own NECESSARY span hypothesis; a
   Theta(L)-oversized extension term against the ln x/8 reserve,
   sieve-constant-independent). (2) A new quantitative window:
   within the frozen HLQuantA card budget the truncated-tail
   C-layer transfer REQUIRES family density (ln x)^{-c} with
   c < c* = 4 ln 2 - 2 = 0.7726 (necessity; closure needs two
   further named inputs), and the A-side thinning tau(A') >= 2.885
   exceeds c*: C-layer viability is a family property. (3) The
   family-averaged B-form must be stated in the reduced
   (N_{P,d_P} - 1)_+ form: the plain form smuggles abundance.
   (4) F17.9's locus is sharpened: the o(ln x) statement gate is
   passable by selection-gated forms; the superpolylog wall is a
   property of per-word-sieve proof routes. (5) The pointwise
   B-form is FALSE without a multiplicity floor and (post-audit) a
   quotient cap; its truth window is expected-unmeasurable at
   reachable scales, pending m1. NO B-layer candidate fails D3(i)
   at statement level: the kickoff's obstruction-record contingency
   branch was NOT triggered; the averaged forms were checked first
   as instructed and are where the layer concentrates.
O3 (in-run audit disposition; the strongest process datum of the
   run). The nine-agent pass returned 3 FATAL / 17 MAJOR / 44
   MINOR / 27 NOTE findings; after steering re-execution the
   sustained core was: [FATAL, 5-agent convergence] the draft's
   worst-case bound on the two-block quotient rho was FALSE (the
   machine-checked insert telescope bounds S(H_d)/S(H_pre) only;
   dividing by S(H_suf) lets CRT-aligned classes reach rho =
   (ln x)^{1-o(1)}, exceeding ln x at finite scales -- witnesses
   rho = 82.24/221.66/1060.3 at the grid depths, all
   steering-re-executed); [FATAL] the draft had promoted the c*
   NECESSITY budget to sufficiency ("closes exactly"); [MAJOR
   convergences] an A3 model-support provenance promotion, the
   TailIntersection constant failing under the draft parameter
   lock, a class-COUNT-vs-class-SIZE corpus misread, a false
   middle-flexibility abundance claim (exactly ONE admissible
   in-budget middle at k = 24 for the exhibited construction), and
   a false quantifier-necessity claim. ALL repaired in place with
   marked amendments (deliverable Section 9a); the D5 selection,
   the 7.2 pigeonhole, the 7.3 instantiation table, and the M2
   design survived every finding. Process echo of item-0017 B3:
   independent same-object convergence (5x on the rho defect, 4x
   on the A3 provenance, 3x on TailIntersection and the
   count-vs-size misread) is again the strongest signal; and the
   rho defect is EXACTLY the rule-15 target class (a fixed-k
   per-insert constant silently promoted to a growing-k two-block
   setting) -- caught this time at statement stage, pre-proof, by
   the adversarial layer the rule prescribes.
O4 (finite-scale honesty rows). The in-repo Lemma 4.1 constant
   C = 12 makes the HLQuantA-conditional class floor vacuous below
   x ~ 1e371 (C = 1: ~1e45), and the small-span Bonferroni closure
   at C2 = 1 opens only near 1e1000: the conditional A-layer is an
   asymptotic statement layer, not a computational one, at every
   reachable scale. Recorded per D3(vi) so no item-0019 measurement
   is mistaken for these constants.
O5 (kickoff textual defects found, for the operator's kickoff-v2
   hygiene): the stale Section 7 HEAD predicate (Section 1 above);
   the Section 2 attribution of the anti-rigidity counting form to
   "item-0005 adjudication F2" (the content is item-0005 P4 +
   item-0017 FATAL-2; the item-0005 Section-6 F2 is the Lean-module
   follow-up) -- handled as a provenance note in the deliverable's
   Section 0, no content ambiguity.

## 5. Follow-up candidates (described only; never silently executed)

FU1 U18.6 write-out: the Model-M A3 analogue at delta = 1 - o(1)
    (per-site lower-tail Chernoff + M1(e) dilution); one short
    model session, would upgrade A3's support tag.
FU2 U18.7 engineering: side pairs with >= 2 admissible in-budget
    middles at every rank (blocks leaving >= 2 uncovered shift
    classes mod every small prime); gates A1's two-word route.
FU3 U18.3 model check: the B1 multiplicity-floor necessity/
    sufficiency in Model M (cheap Session-B-style check).
FU4 T4 extremal refinement: the exact sup of rho over in-window
    admissible (P,d) at the grid depths (small search space at
    1e8; would replace the witness lower bounds by the true sup).
FU5 Kickoff v2 (M2): prerequisites fully staged in the
    deliverable's Sections 7.1/7.6/8; M2 waits on the M1 review
    gate and operator kickoff, per the kickoff's own Section 0.

## 6. M1 review-gate preparation (B2 architecture; execution is an
## operator decision, not this run)

Rule 16(a) status: the verdict tables (deliverable Section 9) were
diffed against the body's support classes in-run, AFTER the audit
repairs (deliverable Section 9a). Strip-relevant anchors for the
review object build (the object is dossier/relext-statements.md;
the strip should retain statement text and verdicts, withhold the
9a adjudication narrative if a blind R2 is wanted):
- R1 (light budget-sheet re-execution): budget_sheet.py +
  budget_sheet_tables.txt; the T4 witness configurations (exact
  block data are printed in the script); the T6 smoke-test data
  (certificate primes are in dossier Section 7.2, in-corpus);
  re-execution targets: T0-T7 rows, the c* algebra, the vacuity
  crossings 1e371/1e45, the witness rho values.
- R2 (load-bearing cross-family scope audit): Section 4 quantifier
  prefixes and uniformity claims; Section 9 verdicts vs body
  support classes; the F18.n scope sentences (esp. F18.2's
  necessity-vs-sufficiency line and F18.4's domain scoping);
  Section 7.1 Prop shapes vs their claimed provenance (A3/
  B2.reduced/C2-at-pin); the deliverable's own audit-repair marks
  as declared-amendment sites.
- Dependencies the reviewer needs read-only: lean/Erdos251/
  Exchange.lean, Hypotheses.lean, Counting/{Words, Lemmata,
  ConsecTransfer, OneExtension}.lean (decl statements);
  dossier/e2prime-supply.md Sections 1, 2, 3.2-3.3, 4.3-4.5, 6,
  7.1-7.2, 8, 9; both adjudication payloads; runs/README rules
  15-16.
# item-0018 M2 completion report -- abstract Lean supply integrator

Date: 2026-07-19. Runner: EXECUTOR lane, fresh instance; model string
claude-fable-5 (Claude Fable 5), ultracode + workflows. Kickoff:
item-0018-kickoff-v2.md, disk sha256
50d429a4f86091da7c171d1afb3f2bb46090168c189f11a3ac1fe3fbb73ee604,
byte-identical to the steering sha256 recorded in ANN-54 and HANDOVER
2k (operator-side sha256 canonical). Web OFF honored: no
network/literature tool invoked at any point; local lake builds only.
mathlib PINNED at a6276f4c (ANN-36); no `lake update`; lean-toolchain
untouched (trailing newline verified intact before and after the
run). The in-run adversarial fidelity review used a six-lens
workflow fan-out (six reviewers + two refuters per finding, 18
agents total), each agent corpus-only.

## 1. Gates (kickoff Section 7; outputs verbatim)

- lake build (AFTER the edits)
    "Build completed successfully." Zero warnings introduced: the
    only warnings in the full build are the pre-existing baseline
    replays (Statement.lean:19 `declaration uses 'sorry'` -- the
    intentional target statement; Basic.lean:90 info `Try this:
    ring_nf`; Counting/Construction.lean unused-variable warnings at
    691/701/713/723/787). Erdos251/Supply.lean itself compiles with
    zero warnings.
- grep -rcE '^\s*sorry\s*$' lean/Erdos251 --include='*.lean'
    lean/Erdos251/Statement.lean:1; every other file 0 (strict
    inventory UNCHANGED; the three Props are named statements,
    supply_of_triple is proved; no new sorry anywhere).
- #print axioms Erdos251.supply_of_triple
    'Erdos251.supply_of_triple' depends on axioms: [propext,
    Classical.choice, Quot.sound]
- python3 lean/scripts/blocks.py check-frozen
    OK erdos_251_irrational / HLQuantA / CramerGranville;
    "FROZEN BLOCKS: all byte-identical."
- python3 lean/scripts/blocks.py relocation-check
    "RELOCATION CHECK PASSED -- concatenation is byte-identical to
    the old body."
- git status --porcelain (worktree at close; exhaustive)
     M lean/Erdos251.lean
    ?? 0018-report-M2.md
    ?? item-0018-kickoff-v2.md
    ?? lean/Erdos251/Supply.lean
    Exactly the Section 5 writes and NOTHING else (the kickoff line
    is the operator's own ephemeral input file, pre-existing, never
    committed, not a run write). lean/Erdos251.lean carries exactly
    one added line, `import Erdos251.Supply`.

PIN / HASH RECORD (deviation, not silently absorbed; item-0017 /
M1-report precedent). The kickoff Section 0 pins main = e0f6ee4a...,
and Section 6 demands HEAD == that pin; actual HEAD at session start
was 20ef744 (the M1 gate-close bookkeeping commit). The two
predicates of the kickoff are jointly unsatisfiable as authored: the
Section 0 preamble instructs the runner to verify the kickoff sha256
against ANN-54, and ANN-54 exists only at 20ef744 (verified: `git
show e0f6ee4:ledger.yaml` contains no ANN-54). Resolution executed:
`git diff e0f6ee4..20ef744` touches ONLY bookkeeping (HANDOVER.md,
ledger.yaml, payloads/HASHES.txt) -- zero edits under lean/ or
dossier/, so every Section 2 read-only anchor is byte-identical
across both states, and the kickoff sha256 verified exactly against
both ANN-54 and HANDOVER 2k. The session pinned to 20ef744; recorded
here for the operator to reconcile at close.

## 2. Deliverable

lean/Erdos251/Supply.lean (new module, imported from the root file):

- Definitional layer (kickoff 3(a)): `anchorPrime` (paper p_n =
  Lean q (n-1), ANN-50/T6), `add_two_le_q` (carrier losslessness),
  `sitePop` (N = pi(x) as a range-(x+1) filtered card),
  `memSiteFilter` / `filteredSites` (S'^{(s)}_x: population,
  threshold s+1 <= n, aggregate window cap, and the two (E4) delta
  caps written byte-parallel to ExchangeAt's cap_near/cap_far),
  `SidePair` / `sideMatchAt` (RS.1 clauses via gap) / `sideWordAt`
  (word map), `classSites` (F_P), `classCount` (N_P),
  `classCountMid` (N_{P,d}), `realizedFamily` (Fam, as the image of
  the site set: finiteness free), `multiFamily` (Fam_2), the RS.1
  side-pair partition identity `card_filteredSites_eq_sum`, and the
  window-slot bound `middle_le_wbound`. Nat subtraction supplies
  (N-1)_+ throughout.
- Parameter layer (kickoff 3(d), hazard (v)): `SupplyParams` with
  fields J K D : Nat -> Nat, wbound : Nat -> Real and the three
  consumed definitional properties one_le_J, one_le_K,
  D_le_two_pow_J (P3.3'(i), the b = 1 gate source). The growth laws
  of the D0 pin are NOT encoded; the integrator is uniform in the
  parameter pack, and instantiating the fields at the D0 pin
  recovers the 7.1 displays.
- The three named Props (7.1 v1.1, statements ONLY, never proved):
  `MatchedFlankLower`, `RelExtensionUpper`, `TailIntersection`, each
  carrying its bracketed 7.1 audit note as a docstring, never as a
  hypothesis.
- The single M2 obligation, proved sorry-free on the classical
  three: `supply_of_triple (P : SupplyParams) : MatchedFlankLower P
  -> RelExtensionUpper P -> TailIntersection P -> ExchangeSupply1`,
  proof = the 7.2 pigeonhole (canonical rigid selection
  `rigidSelect`, RS.1 partition identity, the (N-1)_+ >= N/2 step at
  N >= 2, eps = delta/4 coupling per 7.4) + the 7.3 clause table
  (field-by-field ExchangeAt construction, thresholds via the single
  dictionary s := t, gate from 2^J >= D).

## 3. Statement-fidelity table (7.1 clause <-> Lean clause)

The steering fidelity diff at ratification reads this table. Lean
snippets are quoted from the Prop bodies in Supply.lean.

MatchedFlankLower (= A3):

  7.1: exists delta > 0             | ∃ δ : ℚ, 0 < δ ∧ ...
       (rational per 7.6)           |   (Q, not R: 7.6 "rational
                                    |   delta avoids real-cast
                                    |   noise"; s-uniform, before s)
  7.1: forall s, exists x_2(s)      | ∀ s : ℕ, ∃ x2 : ℕ,
                                    |   (x2 after s: may depend on s)
  7.1: forall x >= x_2(s)           | ∀ x : ℕ, x2 ≤ x →
  7.1: sum over P in Fam_2 of N_P   | (∑ w ∈ multiFamily P s x,
                                    |   classCount P w.1 w.2 s x : ℕ)
  7.1: >= delta |S'^{(s)}_x|        | ((...) : ℚ) ≥ δ *
                                    |   ((filteredSites P s x).card
                                    |   : ℚ)  [casts at the
                                    |   comparison only]
  audit note (|S'| >= 1 dropped;    | docstring only; NO such clause
  s-uniform delta)                  |   in the Prop

RelExtensionUpper (= B2.reduced):

  7.1: forall eps > 0               | ∀ ε : ℚ, 0 < ε →
  7.1: exists x_4(eps)              | ∃ x4 : ℕ,  (before x AND s:
                                    |   uniform in s)
  7.1: forall x >= x_4, forall s    | ∀ x : ℕ, x4 ≤ x → ∀ s : ℕ,
  7.1: forall selections (d_P)      | ∀ d : SidePair → ℕ, (∀ w ∈
       (kickoff 3(b): total         |   realizedFamily P s x, Even
       functions restricted by the  |   (d w) ∧ 2 ≤ d w ∧ ((d w :
       even/window clauses on the   |   ℝ) ≤ P.wbound x)) →
       realized family;             |   [adversarial: ALL total
       adversarial, hazard (i))     |   functions; restriction =
                                    |   RS.1 middle vocabulary
                                    |   "even >= 2" + window budget]
  7.1: sum over P of (N_{P,d_P}     | (∑ w ∈ realizedFamily P s x,
       - 1)_+                       |   (classCountMid P w.1 w.2
                                    |   (d w) s x - 1) : ℕ)
                                    |   [Nat sub = (N-1)_+]
  7.1: <= eps * sum over P of N_P   | ((...) : ℚ) ≤ ε * ((∑ w ∈
                                    |   realizedFamily P s x,
                                    |   classCount P w.1 w.2 s x :
                                    |   ℕ) : ℚ)
  audit note (C_F(x) = eps ln x     | docstring only
  recovers the kickoff display)     |

TailIntersection (= C2 base form at the D0 pin):

  7.1: forall s, exists x_7(s)      | ∀ s : ℕ, ∃ x7 : ℕ,
  7.1: forall x >= x_7              | ∀ x : ℕ, x7 ≤ x →
  7.1: |S'^{(s)}_x| >= N/4          | 4 * (filteredSites P s x).card
       (7.6 shape: 4|S'| >= N,      |   ≥ sitePop x  [division-free
       division-free)               |   Nat form; N = sitePop x =
                                    |   pi(x)]
  audit note (1/4 delivered by C2   | docstring only; NO |S'| >= 1
  only under A' = 1.5, A'' = 48;    |   clause (hazard (vi))
  pigeonhole consumes only          |
  |S'| >= 1)                        |

Site filter S'^{(s)}_x (D0.2', Section 1 table) <-> memSiteFilter:

  sites n with p_n <= x             | 1 ≤ n ∧ anchorPrime n ≤ x
                                    |   (anchorPrime n = q (n-1))
  n >= s+1 (threshold; s := t)      | s + 1 ≤ n
  sum_{i=1..L} g_{n+i} <= A'L ln x  | (∑ i ∈ Finset.range (J+1+K),
                                    |   (gap (n+i) : ℝ)) ≤ W
                                    |   [W = wbound x; ANN-50: the
                                    |   window is gap n ..
                                    |   gap (n+L-1)]
  delta_{n+J} <= D ((E4) near)      | delta (n + J) ≤ D
                                    |   [byte-parallel to cap_near]
  delta_{n+L} <= 2^K ((E4) far)     | delta (n + J + 1 + K) ≤ 2 ^ K
                                    |   [byte-parallel to cap_far;
                                    |   far index per ANN-50]

7.3 clause table <-> the ExchangeAt construction in supply_of_triple:

  one_le_J / one_le_K               | P.one_le_J x / P.one_le_K x
  block_prefix (RS.1 prefix match)  | flank matches via sideMatchAt
                                    |   + length rewrite -> SameBlock
                                    |   n m J
  differ (middles differ, 7.2)      | gap (n + J) ≠ gap (m + J) from
                                    |   the pigeonhole pair
  block_suffix (RS.1 suffix match)  | SameBlock (n+J+1) (m+J+1) K
  cap_near_n/m, cap_far_n/m         | verbatim the filter clauses
  thresholds n, m >= s+1 >= t       | t + 1 ≤ n (site clause at
       (s := t, MINOR-3)            |   s := t), hence t ≤ n
  gate (D : R) - 2 < 2^{J+1} from   | derived from D_le_two_pow_J
       P3.3'(i) 2^J >= D            |   (the only real cast)
  scale selection: one x per t      | x := x2 + x4 + x7 + 2 (also
       beyond the three thresholds  |   x >= 2 for N >= 1)
       at eps = delta/4 (7.4)       |

## 4. In-run adversarial review

Six-lens workflow fan-out on the finished module (18 agents,
corpus-only): six independent reviewers -- Prop statement fidelity;
definitional-layer fidelity incl. an ANN-50/T6 certificate
re-derivation; proof content of supply_of_triple vs the displayed
7.2/7.3 route; parameter layer + adversarial vacuity/satisfiability;
hazards (i)-(vi) + writes-contract compliance; Lean-side encoding
soundness (coercions, Nat-sub traps, getD defaults, image/length
coherence) -- then TWO adversarial refuters per finding
(default-refute discipline; sustained = both confirm).

Raised: 0 FATAL, 0 MAJOR, 6 MINOR. Sustained: 1 MINOR
(documentation only) -- the rigidSelect docstring parenthetical
"(0 off the realized family)" mis-described the code's fallback
condition (the 0-branch fires when the CLASS is empty; the two
conditions differ on wrong-length side pairs, where sideMatchAt is
vacuous; zero mathematical impact since the selection is consulted
only on the realized family). REPAIRED in place (docstring
reworded); a second imprecision flagged by two lenses independently
(the module-header claim "the single real cast is the
ExchangeSupply1 gate", refuted at severity but accurate as a
friction) was tightened in the same pass. All gates re-run green
after the repairs; axiom print unchanged. The four refuted MINORs:
classical-vs-"DECIDABLE" wording of kickoff 3(a) (recorded as O4);
D0-pin small-x guards (recorded under F2); binder `P : SupplyParams`
vs the dossier's side-pair symbol P (naming friction; the Lean uses
`w` for side pairs); and a duplicate of the header-cast wording.

Notable clean-lens results: the reviewer for Prop fidelity verified
the selection-restriction encoding is semantically EQUIVALENT to the
unrestricted 7.1 display (an inadmissible d-value forces
classCountMid = 0, contributing nothing to the Nat-sub sum, and any
selection patches to an admissible one without decreasing the LHS),
so the restriction neither breaks the 7.2 consumption nor burdens
the item-0020 supply direction; the vacuity lens confirmed the D0
instantiation is not blocked by any Lean shape.

## 5. Observations

O1 (mandate outcome). M2 is DELIVERED: the machine checks the 7.2
   pigeonhole and the 7.3 instantiation; the three Props are named
   statements only (ExchangeSupply1 pattern), and
   dyadic_of_exchange_supply composes downstream so that the triple
   now machine-checks all the way to `S not in Z[1/2]` conditional on
   the three named inputs.
O2 (parameter layer, hazard (v) disposition). The b = 1 gate was
   sourced WITHOUT touching any 7.1 shape: D <= 2^J is a
   definitional property (field `D_le_two_pow_J`) of `SupplyParams`,
   and the gate (D : R) - 2 < 2^(J+1) follows in two lines. No
   STOP-AND-REPORT was triggered anywhere in the run; U18.5 was
   never engaged.
O3 (kickoff self-inconsistency, process). The Section 0 pin and the
   Section 0 hash-verification instruction cannot both hold (the
   recording commit necessarily advances HEAD past the pin). This is
   the second consecutive kickoff with a pin/bookkeeping race
   (M1: stale Section 7 HEAD predicate; here: Section 0 pin vs
   ANN-54 presence). A rule-17 amendment fixing the convention "the
   pin means the last pre-bookkeeping content state; HEAD may be
   ahead by bookkeeping-only commits, runner verifies the diff is
   bookkeeping-only" would close the recurrence.
O4 (classical decidability). The site filter's window/delta cap
   clauses are real inequalities (as ExchangeAt's cap fields, per
   hazard (ii)), so the Finset filters take classical decidability
   (file-level `open scoped Classical`; `consCount` precedent at the
   per-def level). This is exactly why the axiom print carries
   Classical.choice; the statement layer itself needs no choice
   (7.6: the selection quantifier is over total functions).

## 6. Follow-up candidates (mandatory channel; frictions that did
## NOT force a STOP)

F1 (selection-restriction encoding). Kickoff 3(b) restricts
   selections "by the even/window clauses on the realized family"
   without fixing the clause list. Encoded as: Even (d w), 2 <= d w
   (RS.1 middle vocabulary "d even >= 2"), and (d w : R) <=
   wbound x (the aggregate window budget as the per-slot bound; the
   proof shows any realized middle satisfies it via
   `middle_le_wbound`). A restriction makes RelExtensionUpper a
   WEAKER hypothesis, i.e. supply_of_triple is the stronger
   integrator; the item-0020 supplier decides whether it wants the
   restricted or the unrestricted form -- if unrestricted, the
   restriction hypothesis is simply not consumed by the supplier's
   client and can be dropped by a one-line statement change plus
   deleting `hrestr` from the proof. Flagged for the item-0020
   kickoff.
F2 (parameter-pack strength). supply_of_triple quantifies over ALL
   SupplyParams (with the three consumed properties), not only the
   D0-pinned growth laws. This is the maximal-strength reading of
   kickoff 3(d) ("J, K, D and the window bound enter as the
   definitional-module parameters") and costs nothing; the D0 pin
   is one instantiation. If steering prefers a pinned parameter
   object (encoding D = ceil(13 C_0 A'' ln x) etc.), that is an
   additive layer on top -- no change to this module needed. Note
   for that layer (review lens 4): the literal pin formulas violate
   one_le_J/one_le_K at x in {0, 1} (ln x <= 0), so the pinned
   fields need small-x guards (e.g. max 1 (...)); harmless, since
   every Prop threshold can absorb small x.
F3 (anchor dictionary). The population clause uses anchorPrime n =
   q (n - 1) (paper p_n; T6: "the Lean base index equals the paper
   anchor index"), with Nat subtraction totalized at n = 0 and the
   site vocabulary clause 1 <= n carried alongside. Note the
   Counting layer's consCount labels q n (= p_{n+1}) as its anchor;
   RS.4 already firewalls the two conventions (consCount semantics
   are the N^o variants only), but a future reuse audit crossing the
   two layers must re-check the off-by-one.
F4 (TailIntersection population form). N is encoded as sitePop x
   (a range-(x+1) filtered card equal to pi(x), same index
   vocabulary as the site set) rather than mathlib's
   Nat.primeCounting; chosen for the 7.6 "consCount-pattern"
   uniformity and to keep the TailIntersection comparison inside one
   vocabulary. An equivalence lemma sitePop = Nat.primeCounting is
   a candidate for the eventual C2 supplier if it wants to consume
   mathlib PNT-adjacent results.

## 7. Review gate

Per kickoff Section 8: the M2 review gate is Lean + CI plus the
steering statement-fidelity diff (Section 3 above) -- operator
decision at completion. Bookkeeping (ledger, HASHES, roadmap
done-move, HANDOVER) is steering/operator post-run; nothing was
committed by this run.
