import Mathlib
import Erdos251.Chebyshev

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
dossier/chain-v1.md. The statements are the item-0002 deliverable and are
FROZEN; item-0003 discharges all nine of this file's proofs as stated.
No `True` placeholders exist anywhere in this project.

`summable_erdosSeries` rests on `Erdos251/Chebyshev.lean` (chain-v1
Lemma 2.1 / repair R1): a sub-geometric prime bound is genuinely needed
here, since `p_n ≤ 2^n` -- and equally Bertrand's `q(n+1) ≤ 2 q n` -- is
exactly borderline for `∑ q n / 2^n`.
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

/-- `q` is strictly monotone (Nat.nth on the infinite prime predicate). -/
theorem q_strictMono : StrictMono q :=
  Nat.nth_strictMono Nat.infinite_setOf_prime

/-- Each `q n` is prime. -/
theorem q_prime (n : ℕ) : (q n).Prime := Nat.prime_nth_prime n

/-- `q n < q (n+1)`. -/
theorem q_lt_succ (n : ℕ) : q n < q (n + 1) := q_strictMono (Nat.lt_succ_self n)

/-- Warm-up 1: the series converges. Needs the Chebyshev bound
`p_n ≤ C n log n` (chain-v1 Lemma 2.1, repair R1); the trivial
`p_n ≤ 2^n` would NOT suffice for the rearrangements downstream
(review-1 A04/A12). -/
theorem summable_erdosSeries :
    Summable (fun n : ℕ => (q n : ℝ) / 2 ^ n) := by
  have hnorm : ‖(1 / 2 : ℝ)‖ < 1 := by
    rw [Real.norm_of_nonneg (by norm_num : (0 : ℝ) ≤ 1 / 2)]; norm_num
  have h0 : Summable (fun n : ℕ => (1 / 2 : ℝ) ^ n) :=
    summable_geometric_of_lt_one (by norm_num) (by norm_num)
  have h1 : Summable (fun n : ℕ => (n : ℝ) ^ 1 * (1 / 2) ^ n) :=
    summable_pow_mul_geometric_of_norm_lt_one 1 hnorm
  have h2 : Summable (fun n : ℕ => (n : ℝ) ^ 2 * (1 / 2) ^ n) :=
    summable_pow_mul_geometric_of_norm_lt_one 2 hnorm
  -- majorant `(n+7)^2 / 2^(n+5)` is summable (polynomial × geometric)
  have hg : Summable (fun n : ℕ => ((n : ℝ) + 7) ^ 2 * (1 / 2) ^ n) := by
    have e : (fun n : ℕ => ((n : ℝ) + 7) ^ 2 * (1 / 2) ^ n)
        = (fun n : ℕ => (n : ℝ) ^ 2 * (1 / 2) ^ n
            + 14 * ((n : ℝ) ^ 1 * (1 / 2) ^ n) + 49 * (1 / 2) ^ n) := by
      funext n; ring
    rw [e]; exact (h2.add (h1.mul_left 14)).add (h0.mul_left 49)
  have hmaj : Summable (fun n : ℕ => ((n : ℝ) + 7) ^ 2 / 2 ^ (n + 5)) := by
    have e : (fun n : ℕ => ((n : ℝ) + 7) ^ 2 / 2 ^ (n + 5))
        = (fun n : ℕ => (1 / 2 : ℝ) ^ 5 * (((n : ℝ) + 7) ^ 2 * (1 / 2) ^ n)) := by
      funext n; ring
    rw [e]; exact hg.mul_left _
  -- pointwise domination on the shifted tail, then unshift
  have hbound : ∀ n : ℕ,
      (q (n + 5) : ℝ) / 2 ^ (n + 5) ≤ ((n : ℝ) + 7) ^ 2 / 2 ^ (n + 5) := by
    intro n
    have hden : (0 : ℝ) < 2 ^ (n + 5) := by positivity
    have hlt : q (n + 5) < (n + 5 + 2) ^ 2 := nth_prime_lt_sq (by omega)
    have hcast : (q (n + 5) : ℝ) ≤ ((n : ℝ) + 7) ^ 2 := by
      have h : (q (n + 5) : ℝ) ≤ (((n + 5 + 2) ^ 2 : ℕ) : ℝ) :=
        Nat.cast_le.mpr (Nat.le_of_lt hlt)
      push_cast at h; nlinarith [h]
    rw [div_le_div_iff₀ hden hden]
    exact mul_le_mul_of_nonneg_right hcast hden.le
  have key : Summable (fun n : ℕ => (q (n + 5) : ℝ) / 2 ^ (n + 5)) :=
    Summable.of_nonneg_of_le (fun n => by positivity) hbound hmaj
  exact (summable_nat_add_iff 5).mp key

/-- Summability of the shifted prime tail `q(n+k)/2^k` (each `n`). -/
theorem summable_q_shift (n : ℕ) :
    Summable (fun k : ℕ => (q (n + k) : ℝ) / 2 ^ k) := by
  have hshift : Summable (fun k : ℕ => (q (k + n) : ℝ) / 2 ^ (k + n)) :=
    (summable_nat_add_iff (f := fun m : ℕ => (q m : ℝ) / 2 ^ m) n).mpr summable_erdosSeries
  have e : (fun k : ℕ => (q (n + k) : ℝ) / 2 ^ k)
      = (fun k : ℕ => (2 : ℝ) ^ n * ((q (k + n) : ℝ) / 2 ^ (k + n))) := by
    funext k
    rw [show n + k = k + n from by ring, pow_add]
    field_simp
    ring
  rw [e]; exact hshift.mul_left _

/-- Summability of the `delta`-defining gap tail (each `n`). -/
theorem summable_gap_shift (n : ℕ) :
    Summable (fun j : ℕ => (gap (n + j) : ℝ) / 2 ^ (j + 1)) := by
  -- dominated by `q(n+1+j)/2^(j+1)`, itself a scaled shift of `summable_q_shift`
  have hmaj : Summable (fun j : ℕ => (q (n + 1 + j) : ℝ) / 2 ^ (j + 1)) := by
    have e : (fun j : ℕ => (q (n + 1 + j) : ℝ) / 2 ^ (j + 1))
        = (fun j : ℕ => (1 / 2 : ℝ) * ((q (n + 1 + j) : ℝ) / 2 ^ j)) := by
      funext j; rw [pow_succ]; ring
    rw [e]; exact (summable_q_shift (n + 1)).mul_left _
  refine Summable.of_nonneg_of_le (fun j => by positivity) (fun j => ?_) hmaj
  have hle : gap (n + j) ≤ q (n + j + 1) := by
    rw [gap]; omega
  have : (gap (n + j) : ℝ) ≤ (q (n + 1 + j) : ℝ) := by
    have : (gap (n + j) : ℝ) ≤ (q (n + j + 1) : ℝ) := Nat.cast_le.mpr hle
    rwa [show n + j + 1 = n + 1 + j from by ring] at this
  gcongr

/-- Head split of `delta` (one step of chain-v1 Lemma 2.2):
`delta n = gap n / 2 + delta (n+1) / 2`. -/
theorem delta_eq_head_add (n : ℕ) :
    delta n = (gap n : ℝ) / 2 + (1 / 2) * delta (n + 1) := by
  have hsum := summable_gap_shift n
  have hd : delta n = ∑' j : ℕ, (gap (n + j) : ℝ) / 2 ^ (j + 1) := rfl
  have hd1 : delta (n + 1) = ∑' j : ℕ, (gap (n + 1 + j) : ℝ) / 2 ^ (j + 1) := rfl
  rw [hd, tsum_eq_zero_add hsum, hd1, ← tsum_mul_left]
  congr 1
  · norm_num
  · apply tsum_congr
    intro j
    rw [show n + (j + 1) = n + 1 + j from by ring]
    ring

/-- Warm-up 2 (constant CORRECTED from the round-0 skeleton): gap series
identity, paper `∑ g_n 2^{-n} = S - 2`. Exact-arithmetic check 2026-07-12:
the finite identity `∑_{n<T} gap n/2^{n+1} = SL_{T+1} - SL_T/2 - 2` holds
exactly for all tested `T`; the round-0 constant `-1` is off by 1. -/
theorem gap_series_identity :
    (∑' n : ℕ, (gap n : ℝ) / 2 ^ (n + 1)) = erdosSeries / 2 - 2 := by
  have hq : Summable (fun n : ℕ => (q n : ℝ) / 2 ^ n) := summable_erdosSeries
  have hA : Summable (fun n : ℕ => (q (n + 1) : ℝ) / 2 ^ (n + 1)) :=
    (summable_nat_add_iff (f := fun m : ℕ => (q m : ℝ) / 2 ^ m) 1).mpr hq
  have hB : Summable (fun n : ℕ => (q n : ℝ) / 2 ^ (n + 1)) := by
    refine (hq.mul_left (1 / 2)).congr (fun n => ?_)
    rw [pow_succ]; ring
  have hsplit : (∑' n : ℕ, (gap n : ℝ) / 2 ^ (n + 1))
      = (∑' n, (q (n + 1) : ℝ) / 2 ^ (n + 1)) - (∑' n, (q n : ℝ) / 2 ^ (n + 1)) := by
    rw [← tsum_sub hA hB]
    apply tsum_congr
    intro n
    rw [← sub_div, gap, Nat.cast_sub (q_lt_succ n).le]
  have hAval : (∑' n, (q (n + 1) : ℝ) / 2 ^ (n + 1)) = erdosSeries - 2 := by
    have h := tsum_eq_zero_add hq
    have hq0 : (q 0 : ℝ) / 2 ^ 0 = 2 := by simp [q, Nat.nth_prime_zero_eq_two]
    have he : erdosSeries = ∑' n : ℕ, (q n : ℝ) / 2 ^ n := rfl
    rw [hq0] at h
    rw [he]; linarith
  have hBval : (∑' n, (q n : ℝ) / 2 ^ (n + 1)) = erdosSeries / 2 := by
    have e : (∑' n, (q n : ℝ) / 2 ^ (n + 1)) = ∑' n, (1 / 2 : ℝ) * ((q n : ℝ) / 2 ^ n) := by
      apply tsum_congr; intro n; rw [pow_succ]; ring
    rw [e, tsum_mul_left]
    show (1 / 2 : ℝ) * erdosSeries = erdosSeries / 2
    ring
  rw [hsplit, hAval, hBval]; ring

/-- Warm-up 3: tail recursion, paper `delta_{n+1} = 2 delta_n - g_{n+1}`
(the Lean gap index absorbs the shift). -/
theorem delta_recursion (n : ℕ) :
    delta (n + 1) = 2 * delta n - (gap n : ℝ) := by
  have h := delta_eq_head_add n
  linarith

/-- Gaps are positive (`Nat.nth` is strictly monotone on the infinite
predicate `Nat.Prime`). -/
theorem gap_pos (n : ℕ) : 0 < gap n := by
  simpa [gap] using Nat.sub_pos_of_lt (q_lt_succ n)

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
  have hsum := summable_gap_shift n
  have hgeom : Summable (fun j : ℕ => (1 / 2 : ℝ) ^ j) :=
    summable_geometric_of_lt_one (by norm_num) (by norm_num)
  have hle : ∀ j : ℕ, (1 / 2 : ℝ) ^ j ≤ (gap (n + j) : ℝ) / 2 ^ (j + 1) := by
    intro j
    have h2 : 2 ≤ gap (n + j) := by
      have hev : Even (gap (n + j)) := gap_even (by omega)
      have hpos : 0 < gap (n + j) := gap_pos _
      rcases hev with ⟨k, hk⟩; omega
    have heq : (1 / 2 : ℝ) ^ j = 2 / 2 ^ (j + 1) := by
      rw [div_pow, one_pow, pow_succ]; ring
    rw [heq]
    gcongr
    exact_mod_cast h2
  calc (2 : ℝ) = ∑' j : ℕ, (1 / 2 : ℝ) ^ j := by
        rw [tsum_geometric_of_lt_one (by norm_num) (by norm_num)]; norm_num
    _ ≤ ∑' j : ℕ, (gap (n + j) : ℝ) / 2 ^ (j + 1) := tsum_le_tsum hle hgeom hsum
    _ = delta n := rfl

/-- Block identity (chain-v1 Lemma 2.2, in template-9.2 orientation;
verified exactly on truncations for `n < 25`, `J < 12`). -/
theorem delta_block (n J : ℕ) :
    delta (n + J)
      = (2 : ℝ) ^ J * delta n
        - ∑ i ∈ Finset.range J, (2 : ℝ) ^ (J - 1 - i) * (gap (n + i) : ℝ) := by
  induction J with
  | zero => simp
  | succ J ih =>
    have hrec : delta (n + (J + 1)) = 2 * delta (n + J) - (gap (n + J) : ℝ) := by
      rw [show n + (J + 1) = (n + J) + 1 from by ring]; exact delta_recursion (n + J)
    have hsum : (2 : ℝ) * ∑ i ∈ Finset.range J, (2 : ℝ) ^ (J - 1 - i) * (gap (n + i) : ℝ)
        = ∑ i ∈ Finset.range J, (2 : ℝ) ^ (J - i) * (gap (n + i) : ℝ) := by
      rw [Finset.mul_sum]
      apply Finset.sum_congr rfl
      intro i hi
      rw [Finset.mem_range] at hi
      rw [← mul_assoc, ← pow_succ', show J - 1 - i + 1 = J - i from by omega]
    have htarget : ∑ i ∈ Finset.range (J + 1), (2 : ℝ) ^ (J + 1 - 1 - i) * (gap (n + i) : ℝ)
        = (∑ i ∈ Finset.range J, (2 : ℝ) ^ (J - i) * (gap (n + i) : ℝ)) + (gap (n + J) : ℝ) := by
      rw [Finset.sum_range_succ]
      have e1 : ∀ i ∈ Finset.range J,
          (2 : ℝ) ^ (J + 1 - 1 - i) * (gap (n + i) : ℝ)
            = (2 : ℝ) ^ (J - i) * (gap (n + i) : ℝ) := by
        intro i hi; rw [Finset.mem_range] at hi
        rw [show J + 1 - 1 - i = J - i from by omega]
      rw [Finset.sum_congr rfl e1]
      congr 1
      rw [show J + 1 - 1 - J = 0 from by omega, pow_zero, one_mul]
    rw [hrec, ih, htarget, pow_succ', mul_sub, hsum]
    ring

/-- Chain-v1 Lemma 2.3 in template-9.3 shape: if `S` is rational, then for
some odd `b > 0` the even lattice `b * delta n ∈ 2ℤ` holds eventually.
Threshold bookkeeping recomputed for the 0-indexed sum (chain-v1 8.2):
rational `erdosSeries = A/(2^σ B)` gives `S = A/(2^(σ+1) B)`, so the paper
WLOG `s ≥ 1` (repair R2) is automatic and `N = σ + 2` works. -/
theorem rational_delta_eventually_lattice (hS : IsRationalReal S) :
    ∃ b : ℕ, 0 < b ∧ Odd b ∧
      ∃ N : ℕ, ∀ n, N ≤ n → ∃ z : ℤ, (b : ℝ) * delta n = 2 * (z : ℝ) := by
  obtain ⟨rr, hrr⟩ := hS
  have hS_eq : (rr : ℝ) = erdosSeries / 2 := hrr
  -- `delta 0 = S - 2` (gap_series_identity), hence rational
  have hdelta0 : delta 0 = ((rr - 2 : ℚ) : ℝ) := by
    have h1 : delta 0 = ∑' j : ℕ, (gap j : ℝ) / 2 ^ (j + 1) := by
      show (∑' j : ℕ, (gap (0 + j) : ℝ) / 2 ^ (j + 1)) = _
      simp
    rw [h1, gap_series_identity, ← hS_eq]
    push_cast; ring
  set r : ℚ := rr - 2 with hr_def
  -- 2-adic decomposition of the denominator: `r.den = 2^σ * B`, `B` odd
  obtain ⟨σ, B, hB_odd, hden_eq⟩ := Nat.exists_eq_two_pow_mul_odd r.den_nz
  have hB_pos : 0 < B := by
    rcases Nat.eq_zero_or_pos B with h | h
    · rw [h, mul_zero] at hden_eq; exact absurd hden_eq r.den_nz
    · exact h
  refine ⟨B, hB_pos, hB_odd, σ + 2, ?_⟩
  -- integrality of `B * delta J` for `J ≥ σ` (delta_block at 0 + 2-adic bound)
  have hint : ∀ J : ℕ, σ ≤ J → ∃ z : ℤ, (B : ℝ) * delta J = (z : ℝ) := by
    intro J hJ
    have hblk : delta J
        = (2 : ℝ) ^ J * delta 0
          - ∑ i ∈ Finset.range J, (2 : ℝ) ^ (J - 1 - i) * (gap i : ℝ) := by
      have h := delta_block 0 J
      simpa using h
    have hMcast : ∑ i ∈ Finset.range J, (2 : ℝ) ^ (J - 1 - i) * (gap i : ℝ)
        = ((∑ i ∈ Finset.range J, 2 ^ (J - 1 - i) * gap i : ℕ) : ℝ) := by
      push_cast; ring
    have hQ : (B : ℚ) * (2 ^ J * r) = ((2 ^ (J - σ) * r.num : ℤ) : ℚ) := by
      have hnum : r * ((r.den : ℕ) : ℚ) = (r.num : ℚ) := Rat.mul_den_eq_num r
      have hdenQ : ((r.den : ℕ) : ℚ) = 2 ^ σ * (B : ℚ) := by
        rw [hden_eq]; push_cast; ring
      have hsplit : (2 : ℚ) ^ J = 2 ^ (J - σ) * 2 ^ σ := by
        rw [← pow_add]; congr 1; omega
      calc (B : ℚ) * (2 ^ J * r) = 2 ^ (J - σ) * (r * (2 ^ σ * (B : ℚ))) := by
            rw [hsplit]; ring
        _ = 2 ^ (J - σ) * (r * ((r.den : ℕ) : ℚ)) := by rw [hdenQ]
        _ = 2 ^ (J - σ) * (r.num : ℚ) := by rw [hnum]
        _ = ((2 ^ (J - σ) * r.num : ℤ) : ℚ) := by push_cast; ring
    have hR : (B : ℝ) * (2 ^ J * (r : ℝ)) = ((2 ^ (J - σ) * r.num : ℤ) : ℝ) := by
      exact_mod_cast hQ
    refine ⟨2 ^ (J - σ) * r.num
        - ((B * ∑ i ∈ Finset.range J, 2 ^ (J - 1 - i) * gap i : ℕ) : ℤ), ?_⟩
    rw [hblk, hMcast, hdelta0, mul_sub, hR]
    push_cast
    ring
  -- evenness: one recursion step, using that `gap` is even from index 1 on
  intro n hn
  obtain ⟨n', rfl⟩ : ∃ n', n = n' + 1 := ⟨n - 1, by omega⟩
  have hn'σ : σ ≤ n' := by omega
  have hn'1 : 1 ≤ n' := by omega
  obtain ⟨z', hz'⟩ := hint n' hn'σ
  obtain ⟨k, hk⟩ := gap_even hn'1
  refine ⟨z' - (B * k : ℕ), ?_⟩
  have hgap : ((gap n' : ℕ) : ℝ) = 2 * (k : ℝ) := by rw [hk]; push_cast; ring
  have hmain : (B : ℝ) * delta (n' + 1) = 2 * ((z' : ℝ) - (B : ℝ) * (k : ℝ)) := by
    rw [delta_recursion n', hgap]
    linear_combination 2 * hz'
  rw [hmain]; push_cast; ring

/-- Chain-v1 Lemma 2.4 in template-9.4 shape: a shared length-`J` gap
prefix quantizes the `delta` difference into `2^(J+1) ℤ / b` (the block
codes of `delta_block` cancel; the base difference lies in `2ℤ / b`). -/
theorem repeated_block_quantization {b n m J : ℕ}
    (hn : ∃ zn : ℤ, (b : ℝ) * delta n = 2 * (zn : ℝ))
    (hm : ∃ zm : ℤ, (b : ℝ) * delta m = 2 * (zm : ℝ))
    (hblock : SameBlock n m J) :
    ∃ z : ℤ,
      (b : ℝ) * (delta (n + J) - delta (m + J)) = 2 ^ (J + 1) * (z : ℝ) := by
  obtain ⟨zn, hzn⟩ := hn
  obtain ⟨zm, hzm⟩ := hm
  refine ⟨zn - zm, ?_⟩
  -- the block codes cancel: a shared prefix makes the two sums identical
  have hsum : ∑ i ∈ Finset.range J, (2 : ℝ) ^ (J - 1 - i) * (gap (n + i) : ℝ)
      = ∑ i ∈ Finset.range J, (2 : ℝ) ^ (J - 1 - i) * (gap (m + i) : ℝ) := by
    apply Finset.sum_congr rfl
    intro i hi
    rw [Finset.mem_range] at hi
    rw [hblock i hi]
  have hdiff : delta (n + J) - delta (m + J) = 2 ^ J * (delta n - delta m) := by
    rw [delta_block n J, delta_block m J, hsum]; ring
  rw [hdiff]
  have hexp : (b : ℝ) * (2 ^ J * (delta n - delta m))
      = 2 ^ J * ((b : ℝ) * delta n - (b : ℝ) * delta m) := by ring
  rw [hexp, hzn, hzm]
  push_cast
  ring

end

end Erdos251
