# Payload 1a (contamination class B) -- blind stage

## Rules
- Do not use web search or external tools. Reason from this document only.
- You may use mathematical knowledge from memory, but label every
  literature-based claim as UNVERIFIED unless you can prove it inline.
- Never invent citations. Distinguish clearly: proved / sketch / heuristic.

## Task
Erdős Problem #251. Let p_n denote the n-th prime (p_1 = 2). Decide, or make
rigorous partial progress on: is

    S = sum_{n>=1} p_n / 2^n

irrational? (Erdős conjectured yes; he proved the factorial analogue
sum p_n/n! irrational in 1958.) Lean 4 target (0-indexed Nat.nth, so the Lean
sum equals 2S; irrationality equivalent):

    theorem erdos_251 : Irrational (tsum fun n : Nat => (Nat.nth Nat.Prime n : Real) / 2 ^ n)

Acceptable deliverables, in descending value: (1) unconditional results;
(2) a fully precise conditional theorem under a hypothesis you state exactly
(e.g. a quantitative form of the Hardy-Littlewood prime tuples conjecture --
if so, state the exact uniformity you need and where you spend it);
(3) a new reduction or equivalence, with proof; (4) rigorous refutation of a
natural proof strategy. Modifying the problem (other bases, other denominator
sequences) counts as calibration only, not progress.

## Prior analysis (frozen dossier, use or challenge it)

Notation: gaps g_n = p_{n+1} - p_n.

1. Identities (all elementary, verified numerically to 1e-147):
   - sum_{n>=1} g_n / 2^n = S - 2.
   - Tail u_n = sum_{k>=1} p_{n+k}/2^k satisfies u_{n+1} = 2 u_n - p_{n+1}.
   - delta_n := u_n - p_{n+1} = sum_{j>=1} g_{n+j}/2^j is the geometric
     weighted average of future gaps; delta_n >= 2; delta_n ~ log n on
     average; delta_{n+1} = 2 delta_n - g_{n+1}.
   - If S = a/(2^s b), b odd, then b delta_n is an integer for all n >= s;
     conversely a single such n makes S rational.

2. Calibration: sum n/2^n = 2 is rational despite increasing numerators, so
   growth/monotonicity/average arguments cannot suffice; a proof must use gap
   irregularity. sum 2^{-p_n} is trivially irrational; the difficulty is
   entirely in the carries.

3. Vacuity warning (verified): with d_n = b delta_n, the recursion
   d_{n+1} = 2 d_n - b g_{n+1} propagates integrality forward automatically.
   The "for all n" conditions collapse to one; NO congruence pattern on gaps
   follows from assuming rationality. Only size arguments carry.

4. Squeeze mechanism: a run of J equal gaps c after index n (J+1 consecutive
   primes in arithmetic progression) gives delta_n - c = 2^{-J}(delta_{n+J} - c).
   If 0 < |delta_{n+J} - c| < 2^J/b, contradiction with b delta_n integral.
   Typical aftermath |delta_{n+J} - c| ~ log n forces J > log2 log n + log2 b
   + O(1). Quantifier care: fixed J fails (aftermath grows with height);
   finitely many runs fail (unknown 2^s part). Sufficient lemma L: for every J
   there are runs of length J with aftermath O(log p_n) whose first occurrence
   height N(J) satisfies log N(J) = o(2^J). Cramér model: log N(J) ~ J log J,
   vast headroom. Unconditional status of even CPAP-3 ("g_n = g_{n+1}
   infinitely often"): UNVERIFIED.

5. Numerics (primes below 3e7): S = 3.674643966011328778995676...;
   continued fraction starts [3,1,2,13,1,1,2,7,1,2,1,2,18,2,15,...];
   longest equal-gap run J=4 (c=30) at p = 9,843,019 where log2 log p = 4.01,
   and the squeeze identity holds numerically on the nose -- the available
   run sits exactly at the b=1 threshold. The shortfall is quantitative.

You may attack via this frame, or via a genuinely different route (for
instance: statistical/entropy properties of the binary digit stream;
elimination schemes over consecutive n; anything else). Independent routes
are explicitly valued.

## Output contract
1. CLAIMS ledger: for each claim an id, exact statement, status in
   {proved, sketch, heuristic, false-start}, dependencies, confidence in [0,1].
2. Main writeup referencing claim ids.
3. Lemma statements in Lean-ready form where feasible (the identities above
   and any hypothesis you introduce).
4. A section "Where I am stuck" naming the exact missing ingredient.
