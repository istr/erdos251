# Payload 1a0 (contamination class A) -- control arm

## Rules
- Do not use web search or external tools. Reason from this document only.
- You may use mathematical knowledge from memory, but label every
  literature-based claim as UNVERIFIED unless you can prove it inline.
- Never invent citations.

## Task
Erdős Problem #251. Let p_n denote the n-th prime (p_1 = 2). Decide, or make
rigorous partial progress on: is

    S = sum_{n>=1} p_n / 2^n

irrational? (Erdős conjectured yes.) Lean 4 target statement (0-indexed
Nat.nth, so the Lean sum equals 2S; irrationality is equivalent):

    theorem erdos_251 : Irrational (tsum fun n : Nat => (Nat.nth Nat.Prime n : Real) / 2 ^ n)

Acceptable deliverables, in descending value: (1) unconditional results;
(2) a fully precise conditional theorem under a hypothesis you state exactly;
(3) a new reduction or equivalence, with proof; (4) rigorous refutation of a
natural proof strategy. Modifying the problem (other bases, other denominator
sequences) counts as calibration only, not progress.

## Output contract
1. CLAIMS ledger: for each claim an id, exact statement, status in
   {proved, sketch, heuristic, false-start}, dependencies, confidence in [0,1].
2. Main writeup referencing claim ids.
3. Lemma statements in Lean-ready form where feasible.
4. A section "Where I am stuck" naming the exact missing ingredient.
