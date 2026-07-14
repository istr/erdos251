import Mathlib

/-!
# Elementary layer (chain-v1 sections 2-3 interface)

Index conventions (SETTLED, item-0002; verified 2026-07-12 by exact
Fraction arithmetic in the steering sandbox):
* `q n = Nat.nth Nat.Prime n` is 0-indexed: `q 0 = 2 = p_1` (paper).
* `gap n = q (n+1) - q n` equals paper `g_{n+1}`; `gap 0 = 1` is the
  unique odd gap; `gap n` is even for `n ≥ 1`.
* `delta n = ∑' j, gap (n+j) / 2^(j+1)` equals paper `delta_n` with NO
  index shift (the gap-index shift is absorbed by the `j+1` weight).
* `erdosSeries = ∑' n, q n / 2^n = 2 * S` (paper `S = ∑_{n≥1} p_n 2^{-n}`).

CORRECTED here (round-0 skeleton claimed `erdosSeries/2 - 1`, which is
false by exactly 1): `∑' n, gap n / 2^(n+1) = erdosSeries/2 - 2`.

Names and statement shapes follow the gpt-iso 9.x index template
(runs/20260712_chatgpt5.6sol_1b_noweb section 9); content follows
dossier/chain-v1.md. Every `sorry` is intentional open work (the
statements are the item-0002 deliverable; proofs are rounds 2+).
No `True` placeholders exist anywhere in this project.
-/

namespace Erdos251

noncomputable section

/-- 0-indexed primes: `q 0 = 2`, `q 1 = 3`, ... (paper `p_{n+1}`). -/
def q (n : ℕ) : ℕ := Nat.nth Nat.Prime n

/-- Prime gap, 0-indexed: `gap n` = paper `g_{n+1}`; `gap 0 = 1`. -/
def gap (n : ℕ) : ℕ := q (n + 1) - q n

/-- Tail transform (= paper `delta_n`): weighted average of future gaps. -/
def delta (n : ℕ) : ℝ := ∑' j : ℕ, (gap (n + j) : ℝ) / 2 ^ (j + 1)

/-- The 0-indexed target series; equals `2 * S` in paper convention. -/
def erdosSeries : ℝ := ∑' n : ℕ, (q n : ℝ) / 2 ^ n

/-- Paper `S = ∑_{n≥1} p_n 2^{-n} ≈ 3.67464...`. -/
def S : ℝ := erdosSeries / 2

/-- Rationality of a real number (template 9.3 helper). -/
def IsRationalReal (x : ℝ) : Prop := ∃ r : ℚ, (r : ℝ) = x

/-- Two indices carry the same length-`J` gap word (template 9.1). -/
def SameBlock (n m J : ℕ) : Prop := ∀ i, i < J → gap (n + i) = gap (m + i)

/-- Warm-up 1: the series converges. Needs the Chebyshev bound
`p_n ≤ C n log n` (chain-v1 Lemma 2.1, repair R1); the trivial
`p_n ≤ 2^n` would NOT suffice for the rearrangements downstream
(review-1 A04/A12). -/
theorem summable_erdosSeries :
    Summable (fun n : ℕ => (q n : ℝ) / 2 ^ n) := by
  sorry

/-- Warm-up 2 (constant CORRECTED from the round-0 skeleton): gap series
identity, paper `∑ g_n 2^{-n} = S - 2`. Exact-arithmetic check 2026-07-12:
the finite identity `∑_{n<T} gap n/2^{n+1} = SL_{T+1} - SL_T/2 - 2` holds
exactly for all tested `T`; the round-0 constant `-1` is off by 1. -/
theorem gap_series_identity :
    (∑' n : ℕ, (gap n : ℝ) / 2 ^ (n + 1)) = erdosSeries / 2 - 2 := by
  sorry

/-- Warm-up 3: tail recursion, paper `delta_{n+1} = 2 delta_n - g_{n+1}`
(the Lean gap index absorbs the shift). -/
theorem delta_recursion (n : ℕ) :
    delta (n + 1) = 2 * delta n - (gap n : ℝ) := by
  sorry

/-- `q` is strictly monotone (Nat.nth on the infinite prime predicate). -/
theorem q_strictMono : StrictMono q :=
  Nat.nth_strictMono Nat.infinite_setOf_prime

/-- Each `q n` is prime. -/
theorem q_prime (n : ℕ) : (q n).Prime := Nat.prime_nth_prime n

/-- Gaps are positive (`Nat.nth` is strictly monotone on the infinite
predicate `Nat.Prime`). -/
theorem gap_pos (n : ℕ) : 0 < gap n := by
  have h : q n < q (n + 1) := q_strictMono (Nat.lt_succ_self n)
  simpa [gap] using Nat.sub_pos_of_lt h

/-- Gaps are even from index 1 on (differences of odd primes);
`gap 0 = 1` is the unique odd gap. -/
theorem gap_even {n : ℕ} (hn : 1 ≤ n) : Even (gap n) := by
  have h0 : q 0 < q n := q_strictMono (by omega)
  have h1 : q n < q (n + 1) := q_strictMono (Nat.lt_succ_self n)
  have hle : 2 ≤ q 0 := (q_prime 0).two_le
  have hodd_n : Odd (q n) := (q_prime n).odd_of_ne_two (by omega)
  have hodd_n1 : Odd (q (n + 1)) := (q_prime (n + 1)).odd_of_ne_two (by omega)
  simpa [gap] using Nat.Odd.sub_odd hodd_n1 hodd_n

/-- `2 ≤ delta n` for `n ≥ 1` (all summed gaps are `≥ 2`). The guard is
sharp: `delta 0 = S - 2 ≈ 1.6746 < 2`. Chain-v1 Lemma 2.1. -/
theorem two_le_delta {n : ℕ} (hn : 1 ≤ n) : 2 ≤ delta n := by
  sorry

/-- Block identity (chain-v1 Lemma 2.2, in template-9.2 orientation;
verified exactly on truncations for `n < 25`, `J < 12`). -/
theorem delta_block (n J : ℕ) :
    delta (n + J)
      = (2 : ℝ) ^ J * delta n
        - ∑ i ∈ Finset.range J, (2 : ℝ) ^ (J - 1 - i) * (gap (n + i) : ℝ) := by
  sorry

/-- Chain-v1 Lemma 2.3 in template-9.3 shape: if `S` is rational, then for
some odd `b > 0` the even lattice `b * delta n ∈ 2ℤ` holds eventually.
Threshold bookkeeping recomputed for the 0-indexed sum (chain-v1 8.2):
rational `erdosSeries = A/(2^σ B)` gives `S = A/(2^(σ+1) B)`, so the paper
WLOG `s ≥ 1` (repair R2) is automatic and `N = σ + 2` works. -/
theorem rational_delta_eventually_lattice (hS : IsRationalReal S) :
    ∃ b : ℕ, 0 < b ∧ Odd b ∧
      ∃ N : ℕ, ∀ n, N ≤ n → ∃ z : ℤ, (b : ℝ) * delta n = 2 * (z : ℝ) := by
  sorry

/-- Chain-v1 Lemma 2.4 in template-9.4 shape: a shared length-`J` gap
prefix quantizes the `delta` difference into `2^(J+1) ℤ / b` (the block
codes of `delta_block` cancel; the base difference lies in `2ℤ / b`). -/
theorem repeated_block_quantization {b n m J : ℕ} (hb : 0 < b)
    (hn : ∃ zn : ℤ, (b : ℝ) * delta n = 2 * (zn : ℝ))
    (hm : ∃ zm : ℤ, (b : ℝ) * delta m = 2 * (zm : ℝ))
    (hblock : SameBlock n m J) :
    ∃ z : ℤ,
      (b : ℝ) * (delta (n + J) - delta (m + J)) = 2 ^ (J + 1) * (z : ℝ) := by
  sorry

end

end Erdos251
