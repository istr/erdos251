# HANDOVER -- erdos251 (state after item-0003 session 1 milestone, 2026-07-15)

Mission: public experiment attacking Erdos #251 (irrationality of
S = sum p_n/2^n) with frontier LLMs; goal is insight, not priority.
Operator: istr. Steering: Claude Fable 5 (fresh instance reads THIS first).

## Read order for a cold start
1. This file. 2. ledger.yaml (append-only decisions ANN-01..20, bets).
3. dossier/chain-v1.md (THE round-1 result, v1.1 after ANN-20). 4. dossier/triage-1b.md then
triage-1a.md (verdicts, review trail, methodology register).
5. runs/README.md rules 1-11. 6. roadmap: python3
/mnt/skills/user/roadmap-items/scripts/roadmap.py list --arc research.
7. lean/README.md (implication-cone state, sorry inventory, egress findings).

## State
- Round 1 CLOSED analytically. 5 blind 1a runs (fable, gpt56sol A/B pair,
  two Gemini), 3 briefed 1b chains (gpt web/iso, fable), 2 blind
  cross-reviews (matrix crossed: fable chain SOUND-with-repairables 0.94;
  gpt-web chain UNSOUND, fatal Q1 integrality, repair known).
- dossier/chain-v1.md consolidates everything: fable spine, all seven
  review repairs executed, review-2 lesson as design rationale.
  Hypotheses: A (uniform two-sided tuple counts, 4 lnln x window) and
  B (Cramer-Granville). Awaiting OPERATOR SIGN-OFF -> resolves BET-04.
  Two statement-level flags recorded in ANN-12 (Def 3.1 n<m ordering vs
  section-6 name swap; vestigial C_A in Hypothesis A); steering offers a
  v1.1 amendment patch on request.
- Lean: item-0002 CLOSED 2026-07-12, CI GREEN on main (followup11 + CI
  repair followup13; roadmap done via followup12). Statement layer from
  chain-v1 (sections 1-3, 8.2) in gpt-iso 9.x index conventions; round-0
  True stub removed; HLQuantA and CramerGranville DEFINED; exactly 15
  intentional sorries, 0 stubs (per-file inventory: lean/README.md);
  round-0 warm-up gap_series_identity constant corrected (-2, was -1;
  exact-arithmetic verified). Pins: lean-toolchain leanprover/lean4:
  v4.16.0 == mathlib v4.16.0 rev a6276f4c, lake-manifest.json committed.
  CI checks compilation only (sorries allowed); repair loops per
  runs/README rule 3 (only the compiler error travels back).
- item-0003 session 1 MILESTONE landed 2026-07-15 (PR #1, rebased onto
  main, tip 46abc8b): Basic + ForkMerge + new Chebyshev.lean sorry-free;
  #print axioms erdos_251_of_small_tail_fork_merge = the classical
  three, no sorryAx -- the deterministic half of chain-v1 (sections 2-3)
  is machine-checked. Inventory now 4 NAMED residuals (Conditional 1 =
  the analytic heart, Hypotheses 2, Statement 1); per-file map in
  lean/README.md. Items 0012/0013 closed; steering static review,
  gates verbatim, and three new elaboration traps: ANN-18.
- item-0014 session 1: STOP-AND-REPORT (correct per contract). Two
  chain-v1 defects found pre-Lean and steering-verified numerically:
  section-5 i_0 off-by-one (F1) and Lemma 4.2 false unrestricted (F2).
  chain-v1 amended to v1.1 (changelog in its section 9; ANN-20); the
  landed Lean is untouched -- both findings live in unformalized
  sections 4-6 prose. Targeted blind re-review of v1.1 sections 4-6
  ORDERED; item-0014 kickoff v2 follows the verdict. Blind-spot
  register entry 4 + checklist rule (iv): triage-1b end.
- BET-05 resolve_by (end of round 1) passed BEFORE the green build
  landed: scoring is an operator call (p 0.45). BET-06/07 open.
- Gemini: demoted to measurement track (ANN-08, pre-registered before
  review verdicts). Review matrix ran without it.
- Steering blind-spot register (3 entries) and checklist: triage-1b end.

## Next: skeleton path for the analytic heart (operator decision (a))
item-0003 stays ratified and open as INTEGRATOR: its floor (ANN-14,
option ii-a) is met except fork_merge_of_hypotheses -- chain-v1 sections
4-6, deliberately unstarted. The ANN-14 gates still govern its eventual
closure: (A) #print axioms erdos_251_conditional without sorryAx, (B)
inventory = the 3 named residuals. Kickoff v2 was RETIRED by design at
the merge (its validity predicate covers lean/, which moved); heart work
gets a fresh ephemeral instruction when it starts. Chosen path (ANN-18):
item-0014 (proposed, rank 0009) freezes the section 4-5 interfaces --
counting Lemmata 4.1-4.4 plus deletion-construction -- as sorried
statements in Erdos251/Counting.lean, then a BLIND CROSS-REVIEW of the
statement set before any proof investment (item-0002 precedent: the
round-0 constant was caught at statement level). The multi-session proof
item is created only with the review verdict. To start: ratify
item-0014, reorder it before item-0003, author the kickoff ephemerally
against the then-current pin. Faithfulness pair stays owned by
item-0011 (contingent, unscheduled) and is a natural co-target of the
same review.

## Pending decisions (operator)
1. Dispatch the targeted blind re-review of chain-v1 v1.1 sections 4-6
   (ANN-20): cross-family (ChatGPT temp chat, web OFF), review_1b
   payload pattern, object sha = operator hash of dossier/chain-v1.md
   at the followup20 tip. Steering supplies the wrapper on request.
   item-0014 kickoff v2 follows the verdict. Round-2 sequencing
   afterwards: item-0004 literature verification (list below);
   two-word variance sub-target = item-0007 (remark 8.3); optional
   thread post AFTER item-0004.
2. Sign-off on chain-v1 v1.1 -> BET-04 resolution and Brier scoring,
   gated on 1. Scoring context: review-1 (0.94, zero fatal) carries two
   post-hoc misses in exactly the amended layer (ANN-20). The Lean
   statement-unfreeze batch (unused hb, ANN-18) rides after sign-off.
3. BET-05 scoring (resolve_by passed pre-green).
4. CI gate split shipped as the LAST followup18 commit (droppable):
   confirm keep/drop after the first Actions run on main.
5. Optional: allowlist the mathlib cache hosts (list in lean/README.md)
   to enable in-sandbox green builds.
6. Whether to re-review the repaired gpt-web chain (not needed for bets).

## item-0004 verification list (accumulated)
ScPu11 identifiers (Acta Arith 126 (2007) vs arXiv:1105.1451 -- reviewer
flagged anachronism-suspicious); Kuperberg arXiv:2210.09775; Mertens /
Rosser-Schoenfeld / Hardy-Wright citations in chain-v1; mathlib module
names (expect Mathlib.Data.Nat.Nth, Mathlib.Data.Real.Irrational);
CPAP-3 status (still assumed open).

## Steering sandbox notes (empirical, 2026-07-12)
- Background processes do NOT survive tool-call boundaries; run long
  jobs foreground with timeout, or chunk them.
- Egress blocks (403 host_not_allowed): release.lean-lang.org,
  reservoir.lean-lang.org, all three mathlib cache hosts (full list and
  workarounds: lean/README.md). Working toolchain recipe: GitHub release
  asset lean-4.16.0-linux.tar.zst (apt-get install zstd first) + elan
  toolchain link; pre-clone mathlib shallow at the tag into
  lean/.lake/packages/mathlib, then lake update resolves the small deps
  and writes the manifest; cache get fails, so CI is the compile gate.
- lake update strips the trailing newline of lean-toolchain; restore via
  git checkout before committing.
- Sorry inventory: grep -cE '^\s*sorry\s*$' (docstring mentions of the
  word otherwise pollute counts).
- Lean elaboration pitfall that cost one CI round: dot-notation
  s.image f / s.filter p elaborates f/p BEFORE s, so unannotated lambda
  binders can be captured by ascriptions instead of inserting coercions;
  use explicitly typed functions like (Nat.cast : Nat -> ZMod p).
- Three more traps from item-0003 session 1 (details ANN-18):
  summable_nat_add_iff .mpr needs (f := ...); nlinarith heartbeats are
  cumulative in assembled proofs; congr 1 auto-reduces Nat-subtraction
  exponents -- prefer explicit omega rewrites.

## Protocol essentials (learned the hard way)
- Operator-side sha256 is the ONLY canonical integrity layer. Model
  self-hashes: OpenAI and Anthropic reliable WITH tools; Gemini anon
  chats have no tools (rule 9); never demand tool-dependent outputs in
  tool-less environments (confabulation trap).
- claude.ai normal chats are never class-clean for this operator
  (memory); use incognito. ChatGPT temp chats for reviews.
- German wrapper flips some outputs to German (sampling-level, Q5);
  wrappers are part of the effective input -- record verbatim in configs.
- Reviews: payload payloads/review_1b.md (generic, two-phase); reviewer
  gets EXACTLY payload + object, never steering triage; cross-family
  assignment; web OFF (public repo now contains answer keys).
- Multi-turn continuations allowed; feed back only the model's own
  trace, record its sha (fable pattern; fs resets happen).
- Patches: git am -3, mboxes erdos251-followup2..20 in order; roadmap
  changes via the skill's emit-patch against a baseline snapshot taken
  BEFORE the move; steering author string
  "Claude Fable 5 (steering) <fable5-steering@localhost>".
- Audits: word-boundary greps (substring false-positive incident).
- Steering checklist additions: evaluate family-quantified clauses at
  extreme members; check integrality/positivity/sub-1-mass corners;
  flag unstated load-bearing steps instead of silently supplying them.

## Experiment questions snapshot
Q2 wall: one statistical kernel, four ordered forms (chain-v1 8.1/8.3).
Q3: 3 basins over 5 blind runs; diversity is sample-level (GPT A/B pair).
Q4: briefing = route lock + execution; web bought literature grounding.
Q5: language sampling-level; anchor propagation; confabulated checksums
vs honest declines; overclaim language vs audited status; role-induced
blindness (fresh same-family reviewer caught what steering missed).
Traces live in the private trace repo; sha commitments in run configs.
