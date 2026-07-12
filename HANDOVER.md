# HANDOVER -- erdos251 (state after round 1 + item-0002, 2026-07-12)

Mission: public experiment attacking Erdos #251 (irrationality of
S = sum p_n/2^n) with frontier LLMs; goal is insight, not priority.
Operator: istr. Steering: Claude Fable 5 (fresh instance reads THIS first).

## Read order for a cold start
1. This file. 2. ledger.yaml (append-only decisions ANN-01..13, bets).
3. dossier/chain-v1.md (THE round-1 result). 4. dossier/triage-1b.md then
triage-1a.md (verdicts, review trail, methodology register).
5. runs/README.md rules 1-10. 6. roadmap: python3
/mnt/skills/user/roadmap-items/scripts/roadmap.py list --arc research.
7. lean/README.md (bring-up state, sorry inventory, egress findings).

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
- BET-05 resolve_by (end of round 1) passed BEFORE the green build
  landed: scoring is an operator call (p 0.45). BET-06/07 open.
- Gemini: demoted to measurement track (ANN-08, pre-registered before
  review verdicts). Review matrix ran without it.
- Steering blind-spot register (3 entries) and checklist: triage-1b end.

## Next item: item-0003 (ratified, next in order)
Conditional theorem: precise hypothesis statement + complete informal
proof + Lean formalization of the implication. Acceptance intent:
non-circularity check; proof survives blind cross-review; implication
file builds sorry-free modulo the stated hypothesis. Profile:
class=largest, reasoning=high (advisory). Sources: chain-v1 (spine and
8.2 interface) plus the landed lean/ tree -- the 15-sorry map IS the
work plan. Steering scope reading (CONFIRM WITH OPERATOR at kickoff):
"sorry-free modulo hypothesis" covers the implication cone, i.e. Basic
(9) + ForkMerge (2) + Conditional (1) = 12 sorries to eliminate; the two
Hypotheses faithfulness lemmata (singularSeries_multipliable/_pos) and
the unconditional Statement target stay open unless the operator says
otherwise. Author the byte-exact kickoff instruction ephemerally against
the operator HEAD pin; do not store it in the repo (skill convention).

## Pending decisions (operator)
1. Sign-off on chain-v1 -> BET-04 resolution and Brier scoring (see the
   two ANN-12 flags above; amendment patch v1.1 on request).
2. BET-05 scoring (resolve_by passed pre-green).
3. Round-2 sequencing after item-0003: item-0004 literature verification
   (list below); two-word variance sub-target = item-0007 (remark 8.3);
   optional thread post AFTER item-0004.
4. Optional: allowlist the mathlib cache hosts (list in lean/README.md)
   to enable in-sandbox green builds.
5. Whether to re-review the repaired gpt-web chain (not needed for bets).

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
- Patches: git am -3, mboxes erdos251-followup2..14 in order; roadmap
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
