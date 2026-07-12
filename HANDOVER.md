# HANDOVER -- erdos251 (state after round 1, 2026-07-12)

Mission: public experiment attacking Erdos #251 (irrationality of
S = sum p_n/2^n) with frontier LLMs; goal is insight, not priority.
Operator: istr. Steering: Claude Fable 5 (fresh instance reads THIS first).

## Read order for a cold start
1. This file. 2. ledger.yaml (append-only decisions ANN-01..11, bets).
3. dossier/chain-v1.md (THE round-1 result). 4. dossier/triage-1b.md then
triage-1a.md (verdicts, review trail, methodology register).
5. runs/README.md rules 1-10. 6. roadmap: python3
/mnt/skills/user/roadmap-items/scripts/roadmap.py list --arc research.

## State
- Round 1 CLOSED analytically. 5 blind 1a runs (fable, gpt56sol A/B pair,
  two Gemini), 3 briefed 1b chains (gpt web/iso, fable), 2 blind
  cross-reviews (matrix crossed: fable chain SOUND-with-repairables 0.94;
  gpt-web chain UNSOUND, fatal Q1 integrality, repair known).
- dossier/chain-v1.md consolidates everything: fable spine, all seven
  review repairs executed, review-2 lesson as design rationale.
  Hypotheses: A (uniform two-sided tuple counts, 4 lnln x window) and
  B (Cramer-Granville). Awaiting OPERATOR SIGN-OFF -> resolves BET-04.
- BET-05 (Lean in round 1): not started; item-0002. BET-06/07 open.
- Gemini: demoted to measurement track (ANN-08, pre-registered before
  review verdicts). Review matrix ran without it.
- Steering blind-spot register (3 entries) and checklist: triage-1b end.

## Pending decisions (operator)
1. Sign-off on chain-v1 -> BET-04 resolution and Brier scoring.
2. Round-2 scope: item-0002 Lean bring-up (source: chain-v1 + gpt-iso
   9.x skeleton as index template); item-0004 literature verification
   (list below); two-word variance sub-target (item-0007 remark 8.3);
   optional thread post AFTER item-0004.
3. Whether to re-review the repaired gpt-web chain (not needed for bets).

## item-0004 verification list (accumulated)
ScPu11 identifiers (Acta Arith 126 (2007) vs arXiv:1105.1451 -- reviewer
flagged anachronism-suspicious); Kuperberg arXiv:2210.09775; Mertens /
Rosser-Schoenfeld / Hardy-Wright citations in chain-v1; mathlib module
names (expect Mathlib.Data.Nat.Nth, Mathlib.Data.Real.Irrational);
CPAP-3 status (still assumed open).

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
- Patches: git am -3, mboxes erdos251-followup2..10 in order; roadmap
  changes via the skill's emit-patch; steering author string
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
