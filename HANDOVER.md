# HANDOVER -- erdos251 (round 2 in motion, 2026-07-16; round 1 closed and scored 2026-07-15)

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
- Round-2 decisions ratified 2026-07-16 (ANN-27, followup27): fidelity
  arm instrument STAGED in runs/_staging_review3fid (payload
  review_3_fidelity, deterministic strip script, object Parts I-III,
  wrapper verbatim, config; steering hashes staged, operator sha256
  canonical); item-0015 (heart proof item) proposed and ordered after
  item-0004, double-gated; statement-unfreeze batch LANDED (unused hb
  dropped from repeated_block_quantization, ANN-18 deferral resolved,
  inventory unchanged); R2 archive gap CLOSED (a70390f transcript,
  b32759d strip-script restore).
- item-0004 DONE 2026-07-16 (ANN-28): literature verification via
  research-mode steering session; report at dossier/literature.md;
  BET-06 scored NO (brier 0.01) -- no prior art, niche unoccupied;
  item-0015 gate (b) cleared.
- item-0014 CLOSED 2026-07-16 (ANN-30): blind fidelity arm
  (claude-sonnet-5, runs/20260716_sonnet5_review3fid) FAITHFUL with
  documented deviations, 0.85, zero unfaithful; two new findings
  adjudicated (4.3 conclusion deviation-weaker flagged; 4.4 missing
  1<=Cg proved inert, C>=1 question routed to item-0011). Instrument
  lesson booked: deliver Phase B in turn 2 on future two-phase arms.
- chain-v1 at v1.4 (ANN-31, citation hygiene only; sha
  6bcb1425...78ec0b); the ANN-28 queue item is discharged.
  Sorry inventory unchanged: 16.
- item-0015 session 1 COMPLETE on branch item-0015-counting-proofs
  (f4cc82b, ANN-33): T1-T5 proved, Counting 12 -> 7, statements
  steering-verified byte-identical; canary positive (both Hypotheses
  sorries reduce to one summability obligation; one bridge lemma
  verified at pin, one unverified-at-pin). Inventory after merge: 11.
- s2 Chebyshev risk resolved in-tree: Chebyshev.lean has
  centralBinom_le (hard half); s2 extracts pi(x) >= c x/log x.

## Pending decisions and gates (operator), round 2
1. MERGE the session-1 PR (branch item-0015-counting-proofs, f4cc82b)
   -- the merge is the ratification of the session-1 work (steering
   adjudication: ANN-33, all checks PASS). CI on the merge is the
   compile gate.
2. Request kickoff v2 (session 2). Proposed scope: cspan_le (in-tree
   Chebyshev route), cfm2_tendsto, cbudget; plus the item-0011
   summability arm -- folded into s2 or as its own small arm
   (operator choice signals with the request).
3. BET-07 resolution by 2026-08-08 (operator judgment).
3. OPTIONAL (operator): public thread post now unblocked (BET-06 NO;
   do NOT inherit the problem page's [Er58b] all-k attribution; the
   thread already carries AI-assisted mathematics, ANN-29) and/or set
   the could-be-formalisable / working-on-formalising flags on the
   problem page (both currently None -- minimal-footprint public
   claim); alerts per report recommendation 1 (arXiv math.NT
   irrationality+prime+2^n; erdosproblems.com/251 watch) PLUS the
   LLM-hunter repo (ANN-32): poll
   github.com/mehmetmars7/Erdosproblems-llm-hunter for commits
   touching attacks/erdos/ or docs/data/erdos_data.js on id 251 --
   the rendered page is a JS shell, blind to fetchers. Contamination
   note: that venue is public LLM-generated #251 material; web-ON
   runs must treat it as such.

## item-0004 RESOLVED (2026-07-16)
Full report: dossier/literature.md (ANN-28; original artifact
operator-held). All ten list items verdicted; BET-06 scored NO
(brier 0.01, binary mean 0.183 -> 0.149). Forum verbatims RESOLVED by
operator browser check (ANN-29; addendum in literature.md): Tao and
Alfaiz confirmed, Vjeko_Kovac telescoping post + reply now verbatim,
steering re-executed the algebra. Still UNVERIFIED: Hardy-Wright
theorem number (physical volume), Pratt Conjecture 1.2 numeric window
(full-text check). CPAP-3 and Erdos #251 confirmed OPEN; no prior art
for the target implication; 0 claimed proofs on the page.

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
