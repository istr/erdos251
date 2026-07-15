# HANDOVER -- erdos251 (round 2 cold start; round 1 closed and scored, 2026-07-15)

Mission: public experiment attacking Erdos #251 (irrationality of
S = sum p_n/2^n) with frontier LLMs; goal is insight, not priority.
Operator: istr. Steering: Claude Fable 5 (fresh instance reads THIS first).

## Read order for a cold start
1. This file. 2. ledger.yaml (append-only; ANN-01..26; bets: 5 scored,
2 open). 3. dossier/chain-v1.md (v1.3, SIGNED OFF -- the round-1
result). 4. dossier/triage-2a.md and triage-2b.md (R2 adjudications),
then triage-1b.md end (methodology register: blind spots 1-5, checklist
rules i-iv) and triage-1a.md. 5. runs/README.md rules 1-11.
6. roadmap: python3 /mnt/skills/user/roadmap-items/scripts/roadmap.py
list --arc research. 7. lean/README.md (16-sorry map: 4 implication
residuals + 12 skeleton statements).

## Round-1 record (closed, scored)
- Result: chain-v1 v1.3 -- conditional theorem "Hypothesis A (uniform
  HL-type tuple counts) + Hypothesis B (Cramer-Granville) => S
  irrational". THREE blind reviews, zero fatal (review-1 0.94, R2a
  ChatGPT 0.90, R2b Fable 0.88); all found gaps repairable-class and
  EXECUTED (v1.1: F1 i_0 off-by-one + F2 Lemma-4.2 span necessity;
  v1.2: R2a repairs incl. kappa-honest 4.2 sketch; v1.3: R2b repairs
  incl. effectivity declaration). Cross-arm disagreement set: EMPTY.
  Empirical layer independently re-executed and STRENGTHENED
  (denominator > 10^1050).
- Bets: BET-04 YES brier 0.1225; BET-05 NO brier 0.2025; mean brier of
  the four scored binary bets 0.183 (coin-flip baseline 0.25). The
  YES declaration = the formal v1.3 sign-off (ANN-25). Open: BET-06
  (implication already in literature, p 0.10 -- GATES ANY PUBLIC
  CLAIM, resolves via item-0004) and BET-07 (unconditional progress,
  p 0.03, to 2026-08-08).
- Lean: deterministic half (chain-v1 sections 2-3) MACHINE-CHECKED --
  Basic, ForkMerge, Chebyshev sorry-free; #print axioms on
  erdos_251_of_small_tail_fork_merge = the classical three; CI
  enforces this on every push (required axiom gate, confirmed green).
  Items 0001/0002/0012/0013 done.
- Methodology dividends, all ledgered: statement-formalization plus
  mandatory computation caught what prose review missed twice
  (F1/F2); computation-mandatory payloads produced both R2 findings;
  anchor-stripped review objects held blind; role-not-family (ANN-10)
  confirmed a second time on the review side; five blind-spot
  register entries with checklist rules (i)-(iv).

## Current state (round-2 opening position)
- item-0014 statement skeleton LANDED (main 5144918): Counting.lean
  with real definitions (deletion construction, 0-based handoff via
  prefix sums, kappa-parametrized interfaces) and 12 intentional
  sorried statements; four proved smoke tests reproduce the
  review-verified word tables; fourth independent F1 confirmation
  (121/121 over (J,K) in [1,11]^2). Steering transcription-fidelity
  review: PASS with documented deviations (ANN-26). item-0014 stays
  OPEN on its ratified acceptance letter: blind cross-review of the
  statement set BEFORE any proof investment.
- item-0003 stays ratified integrator; its floor (ANN-14, ii-a) is
  met except fork_merge_of_hypotheses -- the analytic heart, chain-v1
  sections 4-6, now with its full interface skeleton beneath it.
- item-0011 (Hypotheses faithfulness pair) contingent, unscheduled.
- Inventory on main: 16 sorries = 3 pre-existing residuals
  (Conditional 1, Hypotheses 2) + Statement 1 + Counting 12.

## Pending decisions (operator), round 2
1. item-0014 closure: dispatch the blind transcription-fidelity arm
   (RECOMMENDED: table-driven object = Counting.lean + chain-v1 v1.3
   sections 4-5; cheap, and the natural Sonnet debut on
   low-silent-cost work per the model-ladder plan) OR declare the
   acceptance intent met by R2a/R2b plus the steering pass. Then
   done-move + closure ANN (executor model attribution).
2. Heart funding (the ANN-18 successor decision, now concrete):
   create the multi-session PROOF item for fork_merge_of_hypotheses
   consuming the skeleton -- interface decisions already logged: a
   concrete transcribed form of 4.1's x^{1-o(1)} (M_H >= 4 and
   M_H >> sqrt x at explicit thresholds) and the O_kappa(k) collision
   count replacing the retracted 3k/e^2 -- OR pause the heart for
   item-0004 / item-0007.
3. item-0004 literature verification: resolves BET-06 and gates any
   public claim; the optional thread post comes AFTER it. List below.
4. Lean statement-unfreeze batch on request (unused hb in
   repeated_block_quantization, ANN-18; builds warn on it).
5. Archive the R2 run dirs if not yet done (R2a: ChatGPT UI citation
   tokens note; R2b: turn-2 continuation, above-hash-line self-hash).
6. BET-07 resolution by 2026-08-08 (operator judgment).

## item-0004 verification list (accumulated)
ScPu11 identifiers (Acta Arith 126 (2007) vs arXiv:1105.1451 --
anachronism-suspicious); Kuperberg arXiv:2210.09775; Mertens /
Rosser-Schoenfeld / Hardy-Wright / Bertrand citations in chain-v1;
Cramer-Granville standard formulation; Erdos #251 problem-number
mapping; CPAP-3 status (still assumed open). Mathlib names
Nat.nth/Nat.count/Mathlib.Data.Real.Irrational are now empirically
confirmed in-tree; the R2 arms marked all external citations
UNVERIFIED (web OFF), so this item is the designated closure.

## Steering sandbox notes (empirical)
- Background processes do NOT survive tool-call boundaries; container
  can be DOWN whole turns (rule 9 register, incident 2026-07-13/14):
  probe once, stage textually, ship on recovery.
- Egress blocks and the toolchain workaround recipe: lean/README.md.
  These are SANDBOX-specific; the executor machine builds locally
  (elan + cache work there), so local lake build is a real gate.
- lake update strips the trailing newline of lean-toolchain; restore
  before committing. Sorry inventory: grep -cE '^\s*sorry\s*$'.
- Lean elaboration traps, cumulative: dot-notation s.image f
  elaborates f before s (use explicitly typed functions);
  summable_nat_add_iff .mpr needs (f := ...); nlinarith heartbeats
  are cumulative in assembled proofs; congr 1 auto-reduces
  Nat-subtraction exponents (prefer omega rewrites); `open scoped
  Classical in` must PRECEDE the docstring (ANN-26).

## Protocol essentials (learned the hard way)
- Operator-side sha256 is the ONLY canonical integrity layer; model
  self-hashes reliable only WITH tools; never demand tool-dependent
  outputs in tool-less environments.
- claude.ai normal chats are never class-clean for this operator
  (memory); incognito or API for stage runs; ChatGPT temp chats for
  cross-family reviews; Gemini demoted (ANN-08). Displayed reasoning
  threads are DERIVED renderings -- trace_artifact_layer register,
  runs/README rule 11.
- Reviews: computation-MANDATORY payloads (review_2a pattern);
  anchor-stripped objects with deterministic, committed strip
  scripts; reviewer gets EXACTLY payload + object; web OFF; wrappers
  verbatim in configs (German wrapper flips outputs, Q5).
- Patches: git am -3, mboxes erdos251-followup2..26 in order; roadmap
  changes via the skill's emit-patch against a baseline snapshot
  taken BEFORE the move; steering author string
  "Claude Fable 5 (steering) <fable5-steering@localhost>".
- Kickoffs: ephemeral, byte-exact against a pin, path-scoped validity
  predicates (bookkeeping must not false-alarm the executor); M2
  completion-report shape (Gates verbatim / Observations / Follow-up
  candidates) is standing; closure ANNs carry the executor model.
- Checklist (triage-1b register, rules i-iv): extreme family members;
  integrality/positivity/sub-1-mass corners; flag unstated
  load-bearing steps; RE-EXECUTE every claimed direct computation --
  including amendment-adjacent lines; reading is not verification.

## Experiment questions snapshot
Q2 kernel ordering unchanged (chain-v1 8.1). Q3: route diversity is
sample-level; the two R2 arms found the same defect via different
witnesses. Q4: formalization pressure is itself a review instrument
(F1/F2, the 4.2-sketch constants); briefing = route lock. Q5:
language sampling-level (wrapper effects, steering-thread diglossia
datum, layer undetermined); anchor propagation is real and
anchor-stripping works; confabulated checksums vs honest declines;
calibration now has NUMBERS (review confidences 0.94/0.90/0.88 vs
finding counts; operator brier 0.183). Traces live in the private
trace repo; sha commitments in run configs; artifact layers per
rule 11.
