# Runde 0 dossier -- Erdős Problem #251 (FROZEN, pre-dissection state)

Status: frozen as of 2026-07-11. Contamination class B. This document reflects
the state of analysis BEFORE the problem thread was read. Do not edit; later
findings live in `dissektion.md`.

## 0. Problem

Is S = sum_{n>=1} p_n / 2^n irrational? (p_n = n-th prime, p_1 = 2.)
Erdős conjectured yes [Er88c]; he proved the factorial analogue
sum p_n / n! irrational [Er58b]. Decimal expansion of S: OEIS A098990.
Lean statement exists in google-deepmind/formal-conjectures (note: 0-indexed
`Nat.nth Nat.Prime`, so the Lean sum equals 2S; irrationality equivalent).

Known neighborhood technology (as of 2026-07-11, pre-thread):
- Pratt proved irrationality of sum omega(n)/2^n = sum_p 1/(2^p - 1)
  CONDITIONAL on a uniform version of the prime k-tuples conjecture [Pr24].
- Tao and Teräväinen proved the same UNCONDITIONALLY [TaTe25].
- AI systems are active and landing results in this exact cluster
  (Aristotle at #264, Aletheia at #1051, multi-model teams at #263).

## 1. Normalization onto the gap object

Write g_n = p_{n+1} - p_n. Telescoping gives the exact identity

    sum_{n>=1} g_n / 2^n = S - 2.                                   (I1)

Define the tail u_n = sum_{k>=1} p_{n+k} / 2^k. Then

    u_{n+1} = 2 u_n - p_{n+1}.                                      (I2)

Define delta_n := u_n - p_{n+1} = sum_{j>=1} g_{n+j} / 2^j. This is the
geometric weighted average of FUTURE gaps (weights sum to 1), so

    delta_n >= 2 for all n >= 1,  delta_n ~ log n on average,       (I3)
    delta_{n+1} = 2 delta_n - g_{n+1}.                              (I4)

Rationality structure: if S = a / (2^s b) with b odd, then b * delta_n is an
integer for ALL n >= s; conversely a SINGLE n with b * delta_n integral makes
S rational. All identities verified numerically to 1e-147 (section 6).

## 2. Calibration points (what any proof MUST do)

- sum n / 2^n = 2 is rational despite strictly increasing numerators. Any
  argument using only growth, monotonicity, or averages of p_n is dead on
  arrival. A proof must use gap IRREGULARITY.
- sum 2^{-p_n} is trivially irrational (density-0 support beats periodicity).
  The entire difficulty of #251 sits in the CARRIES.
- Erdős's own remark: in the generalization sum p_n / (g_1 ... g_n) the
  example g_n = p_n + 1 yields a rational value, so growth conditions on
  denominators are necessary there. Base 2 is the hardest case.

## 3. Autopsy 1: the congruence trap (vacuity of the "for all n" condition)

With d_n = b * delta_n, identity (I4) gives d_{n+1} = 2 d_n - b g_{n+1}:
integrality propagates FORWARD automatically. The apparently infinite family
of conditions collapses to a single one; backwards one only gets 2-adic parity
conditions which vanish into the unknown factor 2^s. Consequence: NO congruence
pattern on the gaps can be extracted from the rationality assumption. (A
tempting "window sums are congruent to 2^n c mod 2^T - 1, hence g_{n+T} = g_n
mod 2^T - 1" argument collapses exactly here: the congruence is a tautology of
the recursion, not a constraint. Only SIZE arguments carry.)

## 4. Main route: the CPAP squeeze

Assume b * delta_n integral. A run of J equal gaps c starting after index n
(i.e., J+1 consecutive primes in arithmetic progression, "CPAP") gives exactly

    delta_n - c = 2^{-J} (delta_{n+J} - c).                          (Q)

If 0 < |delta_{n+J} - c| < 2^J / b then 0 < |delta_n - c| < 1/b with c an
integer -- contradiction. Since |delta_{n+J} - c| is typically of size log n,
the required run length is

    J > log2 log n + log2 b + O(1).                                  (T)

Edge case delta_{n+J} = c exactly: handle via maximal runs and the first
deviating gap (technical branch, to be settled in Lean).

Autopsy 2: finitely many numerical runs cannot give unconditional exclusions
of small denominators -- the unknown 2^s part means a run at position n only
constrains s <= n. One needs runs of EVERY length in infinite supply.

Autopsy 3 (quantifier check): a fixed run length J also fails even with
infinitude, because the aftermath delta_{n+J} ~ log n grows with height while
2^J stays fixed. Resolving the quantifiers correctly yields:

SUFFICIENT LEMMA L. For every J there exist runs of J equal consecutive gaps
with aftermath control |delta_{n+J} - c| <= C log p_n, whose first occurrence
height N(J) satisfies log N(J) = o(2^J). Then S is irrational.

Headroom: in the Cramér random model the first length-J run appears at
log N(J) ~ J log J, doubly exponentially below the o(2^J) budget; L is
heuristically overwhelmingly true. Unconditionally, Maynard-type sieves give
clusters and fixed-residue runs (Shiu), but to my knowledge NOT equal-gap runs
of growing length with any effective bound. Whether even "g_n = g_{n+1}
infinitely often" (CPAP-3) is known unconditionally is UNVERIFIED -- flagged
as diligence item 1. L follows from a sufficiently uniform Hardy-Littlewood
prime tuples conjecture (consecutiveness via inclusion-exclusion; aftermath
control via conditioning -- presumably exactly where Pratt spends uniformity
next door).

## 5. Side route: digit-automaton view (speculative)

Rationality means the binary digit stream of S is eventually periodic. Huge
gaps (Ford-Green-Konyagin-Maynard-Tao scale) export the low-order bits of
individual primes into the digit stream; periodicity would couple prime bits
to index residues. Smells like Bombieri-Vinogradov territory; not developed.

## 6. Numerics (first 1,857,859 primes, p_max = 29,999,999)

- S = 3.674643966011328778995676309... ; identity (I1) verified: the two
  sides differ by 1.09e-147 at 500-term truncation, 160-digit precision.
- Continued fraction of S starts [3, 1, 2, 13, 1, 1, 2, 7, 1, 2, 1, 2, 18, 2,
  15, 1, 1, 5, 5, 1, 2, 1]: no early giant partial quotient, no suspiciously
  close small rational (hygiene only, proves nothing).
- Longest equal-gap runs in window: J=4 (c=30) at n=654,926, p_n=9,843,019,
  where log2 log p_n = 4.01; several J=3 runs. At the J=4 run the squeeze
  identity (Q) holds numerically on the nose: |delta_start - c| = 0.293 =
  2^{-4} |delta_end - c|. Interpretation: the mechanism is sound and the
  available run sits exactly AT the b=1 threshold; the shortfall is purely
  quantitative (run supply), matching Lemma L.

## 7. Attack routes as of Runde 0

A. CPAP squeeze (section 4): conditional target "uniform tuples => #251",
   Lean-friendly skeleton.
B. Digit/statistical side view (section 5): undeveloped.
C. Variant ladder for calibration: 1/2^{p_n} (trivial), p_n/2^{n^2} (lacunary,
   easy), p_n/B^n (expected equally hard), conditional versions (target).

## 8. Pre-registered bets (Runde 0, superseded by ledger.yaml)

- P(round 1 yields a Lean-verified conditional implication) = 0.5
- P(the implication already exists in literature or the variant writeup) = 0.35
- P(unconditional progress within 4 weeks) = 0.03-0.05

## References (verified pre-dissection)

[Er58b] P. Erdős, Sur certaines séries à valeur irrationnelle,
        Enseign. Math. (2) 4 (1958), 93-100.
[Er88c] P. Erdős, as cited on erdosproblems.com/251.
[Pr24]  Pratt, conditional irrationality of sum omega(n)/2^n, as cited on
        erdosproblems.com (uniform prime k-tuples hypothesis).
[TaTe25] Tao, Teräväinen, unconditional irrationality of sum_p 1/(2^p-1),
        as cited on erdosproblems.com.
Site:   T. F. Bloom, Erdős Problem #251, https://www.erdosproblems.com/251,
        accessed 2026-07-11.
