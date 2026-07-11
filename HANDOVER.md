# HANDOVER -- erdos251

Regenerated: 2026-07-11. Budget: keep this file under ~1500 tokens.
Acceptance test: a cold instance with this file plus the referenced artifacts
is fully operational without any prior conversation.

## 1. Goal and status (one paragraph)

Research pilot on Erdős Problem #251 (irrationality of S = sum p_n/2^n).
Round 0 (analysis) and the thread/[ScPu11] dissection are DONE and archived.
The working target is the conditional theorem "uniform quantitative prime
tuples hypothesis implies S irrational" (Tao sketched the idea 2025-10-07;
nobody has executed it; novelty risk assessed at 0.10). Two-stage round 1 is
designed and ready to dispatch: stage 1a blind (class-B payload), stage 1b
briefed (class-C payload), across three frontier provers, plus optional
control arm 1a0. Lean project is scaffolded but UNVERIFIED (item I1).

## 2. Canonical artifacts

- dossier/runde0.md        frozen pre-dissection analysis (class B source)
- dossier/dissektion.md    thread + ScPu11 findings, scoring (class C source)
- payloads/1a0_control.md  class A payload (optional arm)
- payloads/1a_blind.md     class B payload (stage 1a)
- payloads/1b_briefed.md   class C payload (stage 1b)
- payloads/HASHES.txt      sha256 of all payloads; copy into run configs
- runs/README.md           run protocol (stateless, repair, blind review)
- lean/                    Lake project; 5 sorries total: erdos_251_irrational,
                           summable_SL, gap_series_identity, delta_recursion,
                           erdos_251_of_uniform_tuples (hypothesis = placeholder)
- ledger.yaml              bets: 3 scored, 4 open (BET-20260711-04..07)
- roadmap/                 items item-0001..0006, all status proposed
                           (0001 round-1 runs, 0002 Lean bring-up, 0003
                           conditional theorem, 0004 literature verification,
                           0005 TaTe transfer, 0006 adaptivity threshold).
                           Execution order intentionally EMPTY until the
                           operator ratifies; then schedule via
                           roadmap.py reorder (suggested: 0001, 0002, 0003,
                           0004, 0005, 0006).

## 3. Next action (exactly one)

Execute item-0001: dispatch payloads/1a_blind.md (verify sha256 against
payloads/HASHES.txt) as stateless runs to the three provers per runs/README;
archive each run under runs/<date>_<model>_1a/. Only after all 1a outputs are
archived, dispatch payloads/1b_briefed.md as stage 1b.

## 4. Firewall map (contamination classes)

Class A = statement only; B = A + runde0; C = B + dissection briefing.

| Artifact                 | may enter 1a0 | 1a  | 1b  | review |
| dossier/runde0.md        | no            | via payload | via payload | as needed |
| dossier/dissektion.md    | no            | NO  | via payload | as needed |
| payloads/1a0_control.md  | yes           | no  | no  | no |
| payloads/1a_blind.md     | no            | yes | no  | no |
| payloads/1b_briefed.md   | no            | NO  | yes | no |
| producer transcripts     | no            | no  | no  | NO (blind review) |

Hard rule: stage-1a/1a0 runs must never see class-C material (Tao comment,
variant construction, ScPu11 briefing). Reviews are blind to producer
reasoning until the verdict is archived.

## 5. Ledger snapshot (open bets)

- BET-04: informal conditional proof lands in round 1 -- p = 0.65
- BET-05: Lean-verified implication same round -- p = 0.45
- BET-06: implication already exists in literature -- p = 0.10 (gate: item A1)
- BET-07: unconditional progress within 4 weeks -- p = 0.03

## 6. Glossary (canonical objects; do not re-derive, do not rename)

- S        sum_{n>=1} p_n/2^n, approx 3.674643966...; Lean sum = 2S (0-index)
- g_n      prime gap p_{n+1} - p_n
- u_n      tail sum_{k>=1} p_{n+k}/2^k; recursion u_{n+1} = 2 u_n - p_{n+1}
- delta_n  u_n - p_{n+1} = sum_j g_{n+j}/2^j; weighted future-gap average;
           recursion delta_{n+1} = 2 delta_n - g_{n+1}; >= 2; ~ log n
- Lemma L  for every J: equal-gap runs of length J, aftermath O(log p_n),
           first occurrence N(J) with log N(J) = o(2^J)  =>  S irrational
- Routes   A squeeze (Lean backbone) / B entropy (Tao) / D elimination
           (ScPu11 base-2 uniformization); C variant ladder = calibration only
- CPAP     consecutive primes in arithmetic progression (run of equal gaps)
- Stages   1a0 control (class A) / 1a blind (B) / 1b briefed (C) / review
- Scoring  Brier, registered in ledger.yaml BEFORE evidence

## 7. Session hygiene

Sessions are crash-only: anything durable goes to files immediately; this
HANDOVER is regenerated at every checkpoint; repair loops carry only compiler
errors; reviewer contexts stay clean of producer reasoning.
