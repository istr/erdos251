# Payload 1b (contamination class C) -- briefed stage

## Rules
- Web access per run config; if unavailable, label literature-based claims
  UNVERIFIED unless proved inline. Never invent citations.
- Distinguish clearly: proved / sketch / heuristic.

## Task
Erdős Problem #251. Let p_n denote the n-th prime (p_1 = 2). Target: rigorous
progress on the irrationality of

    S = sum_{n>=1} p_n / 2^n.

PRIMARY OBJECTIVE of this stage: a complete, precise proof of the conditional
theorem

    (uniform quantitative prime tuples hypothesis)  ==>  S is irrational,

with the hypothesis stated exactly (name the uniformity range and every place
it is spent), structured so that the implication is formalizable in Lean 4.
Lean target (0-indexed Nat.nth; the Lean sum equals 2S):

    theorem erdos_251 : Irrational (tsum fun n : Nat => (Nat.nth Nat.Prime n : Real) / 2 ^ n)

Secondary objectives, in order: (a) an entropy/statistical variant of the
proof; (b) uniformization of the ScPu11 elimination engine (below) to base 2;
(c) sharp identification of what breaks unconditionally.

## Frozen prior analysis (identical to blind stage)

Notation: gaps g_n = p_{n+1} - p_n.

1. Identities (elementary, verified numerically to 1e-147):
   - sum_{n>=1} g_n / 2^n = S - 2.
   - Tail u_n = sum_{k>=1} p_{n+k}/2^k satisfies u_{n+1} = 2 u_n - p_{n+1}.
   - delta_n := u_n - p_{n+1} = sum_{j>=1} g_{n+j}/2^j, the geometric weighted
     average of future gaps; delta_n >= 2; delta_n ~ log n on average;
     delta_{n+1} = 2 delta_n - g_{n+1}.
   - If S = a/(2^s b), b odd, then b delta_n is integral for all n >= s;
     conversely a single such n makes S rational.
2. Calibration: sum n/2^n = 2 kills growth/monotonicity/average arguments;
   sum 2^{-p_n} is trivially irrational; the difficulty is the carries.
3. Vacuity warning: d_{n+1} = 2 d_n - b g_{n+1} propagates integrality
   forward; no congruence pattern on gaps follows from rationality. Only size
   arguments carry.
4. Squeeze: a run of J equal gaps c after index n gives
   delta_n - c = 2^{-J}(delta_{n+J} - c); with aftermath 0 < |...| < 2^J/b,
   contradiction. Threshold J > log2 log n + log2 b + O(1). Sufficient lemma
   L: for every J, runs of length J with aftermath O(log p_n) and first
   occurrence height N(J) with log N(J) = o(2^J). Cramér: log N(J) ~ J log J.
5. Numerics: S = 3.674643966011328778995676...; CF starts
   [3,1,2,13,1,1,2,7,...]; longest observed run J=4 (c=30) at p = 9,843,019,
   log2 log p = 4.01; squeeze identity numerically exact; the run sits at the
   b=1 threshold. Shortfall is quantitative.

## Briefing (dissection findings, 2026-07-11)

1. T. Tao (problem thread, 2025-10-07, paraphrase): partial summation reduces
   the problem to irrationality of sum g_n/2^n; a sufficiently quantitative
   and uniform prime tuples conjecture, giving statistical control over
   windows of about log log n consecutive gaps (each typically of size about
   log n), could rule out periodicity of the binary expansion; Shannon
   entropy suggested as a possible tool. This matches the frozen analysis in
   frame, conditional source, and window scale. Nobody has executed it.

2. Variant resolved (thread, 2026-04-15, Kovač with GPT-5.4 Pro): the
   g_1...g_n GENERALIZATION on the problem page has a negative answer by
   telescoping: pick integers c_n with c_{n+1} = c_n g_n - p_n
   (c_{n+1} == -p_n mod c_n), c_n slowly growing, g_n = (c_{n+1}+p_n)/c_n.
   WARNING: this exploits adversarial freedom in choosing denominators; it
   says NOTHING about the original (fixed base 2). Do not spend budget there.

3. [ScPu11] = J.-C. Schlage-Puchta, Acta Arith. 126 (2007) 295-303,
   arXiv:1105.1451 (operator may attach the PDF). Theorem 2: digit
   concatenation (carry-free projection; Mahler/Bundschuh lineage). Theorem 3
   proves 1, S_0, S_1, ... Q-linearly independent for S_k = sum p_n^k/n!,
   via an engine directly relevant here:
   (a) rationality forces near-integrality of leading tail terms at every n
       (factorial base: O(1) gaps suffice);
   (b) recursive cross-elimination over consecutive n with polynomial gap
       coefficients cancels leading growth (an algebraic lemma keeps the
       residue nontrivial);
   (c) Selberg-sieve upper bounds: no nonzero polynomial in O(1) consecutive
       gaps vanishes on a positive proportion of n (unconditional
       anti-conspiracy for bounded windows);
   (d) van der Corput discrepancy contradiction.
   In base 2 the same scheme needs control UNIFORM in window size
   k ~ log log n (Tao's phrase), and the squeeze/entropy routes additionally
   need pattern EXISTENCE (lower bounds, i.e. Hardy-Littlewood input), which
   Selberg upper bounds do not give.

4. Route ranking for this stage:
   A. Squeeze (formalization backbone): prove lemma L from your precisely
      stated uniform tuples hypothesis (consecutiveness via inclusion-
      exclusion over the tuple; aftermath control via conditioning), then
      L => irrationality with the edge case delta_{n+J} = c handled.
   B. Entropy (robustness check): derive positive entropy rate of the gap
      window process from the same hypothesis; conclude non-periodicity.
   D. Elimination (stretch): uniformize the ScPu11 engine to base 2 and
      identify the exact hypothesis strength it needs.
   Deliver A completely before polishing B or D.

## Output contract
1. CLAIMS ledger: id, exact statement, status {proved, sketch, heuristic,
   false-start}, dependencies, confidence in [0,1].
2. The hypothesis, stated in full, in both prose and Lean-ready form.
3. Main writeup referencing claim ids; every use of the hypothesis marked.
4. Lean-ready lemma statements for the whole chain (identities are already
   stubbed in the project as summable_SL, gap_series_identity,
   delta_recursion).
5. "Where I am stuck": the exact missing ingredient, if any.
