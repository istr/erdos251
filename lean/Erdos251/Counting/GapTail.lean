import Mathlib
import Erdos251.Basic

/-!
# Lemma 4.4: the delta tail bound

`delta_le_of_gap_bound` and its `q`-growth helpers. This module is a
dependency island: it uses nothing from the rest of the counting layer,
only `q`/`delta` from `Erdos251/Basic.lean`.

RELOCATION ONLY (item-0016). The body below is byte-identical to
`Erdos251/Counting.lean` lines 1657-1826 at commit
`6683ee0f009baeb5dd6e759f265544e7f91af23d`,
sha256 `e73d586f1d350ba599755bc8e40be84e1faff2eb12c388fb51c6b4b0ddab48f9`.
No statement, docstring, proof or name was changed. Provenance, the index
conventions, the traceability table and the module map live in the umbrella
`Erdos251/Counting.lean`.
-/

namespace Erdos251

noncomputable section

/-! ### Proof-layer helpers for Lemma 4.4 (item-0015; not statements) -/

/-- Bertrand step for the prime enumeration: the next prime is at most
twice the current one. Bertrand gives a prime `p ∈ (q m, 2 q m]`; the
count/nth bridge places `q (m+1)` at or below it. -/
theorem q_succ_le_two_mul (m : ℕ) : q (m + 1) ≤ 2 * q m := by
  have hqm2 : 2 ≤ q m := (q_prime m).two_le
  obtain ⟨p, hp, hlt, hle⟩ := Nat.exists_prime_lt_and_le_two_mul (q m) (by omega)
  have hcqm : Nat.count Nat.Prime (q m) = m := by
    simpa [q] using Nat.count_nth_of_infinite Nat.infinite_setOf_prime m
  have hcqm1 : Nat.count Nat.Prime (q m + 1) = m + 1 := by
    rw [Nat.count_succ, hcqm, if_pos (q_prime m)]
  have hmono : m + 1 ≤ Nat.count Nat.Prime p := by
    rw [← hcqm1]; exact Nat.count_monotone _ (by omega)
  have hcp1 : m + 1 < Nat.count Nat.Prime (p + 1) := by
    rw [Nat.count_succ, if_pos hp]; omega
  have hnth : Nat.nth Nat.Prime (m + 1) < p + 1 := Nat.nth_lt_of_lt_count hcp1
  have : q (m + 1) ≤ p := by simpa [q] using Nat.lt_succ_iff.mp hnth
  omega

/-- Iterated Bertrand: `q (n + k) ≤ 2^k * q n`. -/
theorem q_add_le_two_pow (n k : ℕ) : q (n + k) ≤ 2 ^ k * q n := by
  induction k with
  | zero => simp
  | succ k ih =>
    calc q (n + (k + 1)) ≤ 2 * q (n + k) := q_succ_le_two_mul (n + k)
      _ ≤ 2 * (2 ^ k * q n) := by have := ih; omega
      _ = 2 ^ (k + 1) * q n := by ring

/-- Log form of the iterated Bertrand bound:
`log (q (n+1+j)) ≤ log (q n) + (j+1)` (using `log 2 ≤ 1`). -/
theorem log_q_shift_le (n j : ℕ) :
    Real.log (q (n + 1 + j)) ≤ Real.log (q n) + ((j : ℝ) + 1) := by
  have hqnpos : (0 : ℝ) < (q n : ℝ) := by exact_mod_cast (q_prime n).pos
  have hbound : q (n + 1 + j) ≤ 2 ^ (j + 1) * q n := by
    have h := q_add_le_two_pow n (1 + j)
    have e1 : n + (1 + j) = n + 1 + j := by ring
    have e2 : (2 : ℕ) ^ (1 + j) = 2 ^ (j + 1) := by rw [Nat.add_comm]
    rw [e1, e2] at h; exact h
  have hcast : (q (n + 1 + j) : ℝ) ≤ 2 ^ (j + 1) * (q n : ℝ) := by
    calc (q (n + 1 + j) : ℝ) ≤ ((2 ^ (j + 1) * q n : ℕ) : ℝ) := by exact_mod_cast hbound
      _ = 2 ^ (j + 1) * (q n : ℝ) := by push_cast; ring
  have hlogle : Real.log (q (n + 1 + j)) ≤ Real.log (2 ^ (j + 1) * (q n : ℝ)) :=
    Real.log_le_log (by exact_mod_cast (q_prime (n + 1 + j)).pos) hcast
  rw [Real.log_mul (by positivity) (ne_of_gt hqnpos), Real.log_pow] at hlogle
  have hlog2 : Real.log 2 ≤ 1 := by
    have := Real.log_le_sub_one_of_pos (by norm_num : (0 : ℝ) < 2); linarith
  have hj0 : (0 : ℝ) ≤ (j : ℝ) + 1 := by positivity
  have hstep : (↑(j + 1) : ℝ) * Real.log 2 ≤ (j : ℝ) + 1 := by
    push_cast; nlinarith [mul_nonneg hj0 (sub_nonneg.mpr hlog2)]
  linarith [hlogle, hstep]

/-- LEMMA 4.4 (tail bound from B). Under Hypothesis B there is `ν_1` with
`delta_ν ≤ 3 C_g (ln p_ν)^2` for all `ν ≥ ν_1`.

Index map: paper `delta_ν` is `delta ν` and paper `p_ν` is `q (ν - 1)`,
so `ν = n + 1` gives the ℕ-subtraction-free form below. `C_g` is threaded
as an explicit parameter rather than re-existentialised, which is what
keeps the factor `3` meaningful (`∃ C, delta ≤ 3 * C * ...` would be
vacuous). The hypothesis is exactly the body of the frozen
`CramerGranville`, which binds `∃ C : ℝ` with no sign or size constraint;
the frozen definition is not touched. The missing `1 ≤ Cg` (which prose's
"Under Hypothesis B" supplies) is INERT: `gap n ≥ 1` always, while
`Cg * log (q n)^2 < 0` for `Cg < 0`, so `hB` is unsatisfiable there and
the broadened statement licenses nothing false (proved by the R3fid arm,
ANN-30). The `C ≥ 1` faithfulness question for the frozen definition
itself is item-0011's. -/
theorem delta_le_of_gap_bound {Cg : ℝ} {n₀ : ℕ}
    (hB : ∀ n : ℕ, n₀ ≤ n → (gap n : ℝ) ≤ Cg * Real.log (q n) ^ 2) :
    ∃ n₁ : ℕ, ∀ n : ℕ, n₁ ≤ n → delta (n + 1) ≤ 3 * Cg * Real.log (q n) ^ 2 := by
  -- `Cg > 0` is forced by `hB` (ANN-30 inertness): `1 ≤ gap n₀ ≤ Cg log(q n₀)²`.
  have hCg0 : 0 < Cg := by
    have hg1 : (1 : ℝ) ≤ (gap n₀ : ℝ) := by exact_mod_cast gap_pos n₀
    have hb := hB n₀ le_rfl
    have hlogpos : 0 < Real.log (q n₀) :=
      Real.log_pos (by exact_mod_cast (q_prime n₀).one_lt)
    nlinarith [hb, hg1, mul_pos hlogpos hlogpos]
  -- summability infrastructure
  have hgeom : Summable (fun j : ℕ => (1 : ℝ) / 2 ^ (j + 1)) := by
    have hg' : Summable (fun j : ℕ => (1 / 2 : ℝ) ^ (j + 1)) :=
      (summable_nat_add_iff (f := fun n : ℕ => (1 / 2 : ℝ) ^ n) 1).mpr
        (summable_geometric_of_lt_one (by norm_num) (by norm_num))
    exact hg'.congr (fun j => by rw [div_pow, one_pow])
  have hnorm : ‖(1 / 2 : ℝ)‖ < 1 := by
    rw [Real.norm_of_nonneg (by norm_num : (0 : ℝ) ≤ 1 / 2)]; norm_num
  have hBsum : Summable (fun j : ℕ => ((j : ℝ) + 1) ^ 2 / 2 ^ (j + 1)) := by
    have h2 : Summable (fun j : ℕ => (j : ℝ) ^ 2 * (1 / 2) ^ j) :=
      summable_pow_mul_geometric_of_norm_lt_one 2 hnorm
    have h1 : Summable (fun j : ℕ => (j : ℝ) ^ 1 * (1 / 2) ^ j) :=
      summable_pow_mul_geometric_of_norm_lt_one 1 hnorm
    have h0 : Summable (fun j : ℕ => (1 / 2 : ℝ) ^ j) :=
      summable_geometric_of_lt_one (by norm_num) (by norm_num)
    have hsum : Summable (fun j : ℕ => ((j : ℝ) + 1) ^ 2 * (1 / 2) ^ j) := by
      have e : (fun j : ℕ => ((j : ℝ) + 1) ^ 2 * (1 / 2) ^ j)
          = (fun j : ℕ => (j : ℝ) ^ 2 * (1 / 2) ^ j + 2 * ((j : ℝ) ^ 1 * (1 / 2) ^ j)
              + 1 * (1 / 2) ^ j) := by
        funext j; ring
      rw [e]; exact (h2.add (h1.mul_left 2)).add (h0.mul_left 1)
    have hBsum' : Summable (fun j : ℕ => ((j : ℝ) + 1) ^ 2 * (1 / 2 : ℝ) ^ (j + 1)) := by
      have e : (fun j : ℕ => ((j : ℝ) + 1) ^ 2 * (1 / 2 : ℝ) ^ (j + 1))
          = (fun j : ℕ => (1 / 2) * (((j : ℝ) + 1) ^ 2 * (1 / 2) ^ j)) := by
        funext j; rw [pow_succ']; ring
      rw [e]; exact hsum.mul_left _
    exact hBsum'.congr (fun j => by rw [div_pow, one_pow, mul_one_div])
  set B := ∑' j : ℕ, ((j : ℝ) + 1) ^ 2 / 2 ^ (j + 1) with hBdef
  have hB0 : 0 ≤ B := tsum_nonneg (fun j => by positivity)
  -- choose `n₁ ≥ n₀` with `log(q n)² ≥ 2B` (since `log(q n) → ∞`)
  have hq_top : Filter.Tendsto (fun n : ℕ => (q n : ℝ)) Filter.atTop Filter.atTop :=
    Filter.tendsto_atTop_mono (fun n => by exact_mod_cast q_strictMono.le_apply)
      (tendsto_natCast_atTop_atTop (R := ℝ))
  have hlog_top : Filter.Tendsto (fun n : ℕ => Real.log (q n)) Filter.atTop Filter.atTop :=
    Real.tendsto_log_atTop.comp hq_top
  have hev := hlog_top.eventually_ge_atTop (2 * B + 1)
  rw [Filter.eventually_atTop] at hev
  obtain ⟨n₁', hn₁'⟩ := hev
  refine ⟨max n₁' n₀, fun n hn => ?_⟩
  have hloge : 2 * B + 1 ≤ Real.log (q n) := hn₁' n (le_trans (le_max_left _ _) hn)
  have hnn0 : n₀ ≤ n := le_trans (le_max_right _ _) hn
  have hlog1 : 1 ≤ Real.log (q n) := by linarith
  have hn2B : 2 * B ≤ Real.log (q n) ^ 2 := by
    nlinarith [hloge, hlog1, sq_nonneg (Real.log (q n) - 1)]
  -- pointwise bound on the `delta` summand
  have hfg : ∀ j : ℕ, (gap (n + 1 + j) : ℝ) / 2 ^ (j + 1)
      ≤ (2 * Cg * Real.log (q n) ^ 2) / 2 ^ (j + 1)
        + (2 * Cg) * (((j : ℝ) + 1) ^ 2 / 2 ^ (j + 1)) := by
    intro j
    have hden : (0 : ℝ) < 2 ^ (j + 1) := by positivity
    have hb1 : (gap (n + 1 + j) : ℝ) ≤ Cg * Real.log (q (n + 1 + j)) ^ 2 :=
      hB (n + 1 + j) (by omega)
    have hlog := log_q_shift_le n j
    have hlog0 : 0 ≤ Real.log (q (n + 1 + j)) :=
      Real.log_nonneg (by exact_mod_cast (q_prime _).one_lt.le)
    have hs0 : 0 ≤ Real.log (q n) :=
      Real.log_nonneg (by exact_mod_cast (q_prime _).one_lt.le)
    have hsq : Real.log (q (n + 1 + j)) ^ 2
        ≤ 2 * Real.log (q n) ^ 2 + 2 * ((j : ℝ) + 1) ^ 2 := by
      nlinarith [hlog, hlog0, hs0, sq_nonneg (Real.log (q n) - ((j : ℝ) + 1))]
    have hnum : (gap (n + 1 + j) : ℝ)
        ≤ 2 * Cg * Real.log (q n) ^ 2 + 2 * Cg * ((j : ℝ) + 1) ^ 2 :=
      calc (gap (n + 1 + j) : ℝ) ≤ Cg * Real.log (q (n + 1 + j)) ^ 2 := hb1
        _ ≤ Cg * (2 * Real.log (q n) ^ 2 + 2 * ((j : ℝ) + 1) ^ 2) :=
            mul_le_mul_of_nonneg_left hsq hCg0.le
        _ = 2 * Cg * Real.log (q n) ^ 2 + 2 * Cg * ((j : ℝ) + 1) ^ 2 := by ring
    rw [← mul_div_assoc, div_add_div_same, div_le_div_iff_of_pos_right hden]
    linarith [hnum]
  -- summability of the majorant and its tsum
  have hg1sum : Summable (fun j : ℕ => (2 * Cg * Real.log (q n) ^ 2) / 2 ^ (j + 1)) :=
    (hgeom.mul_left _).congr (fun j => mul_one_div _ _)
  have hg2sum : Summable (fun j : ℕ => (2 * Cg) * (((j : ℝ) + 1) ^ 2 / 2 ^ (j + 1))) :=
    hBsum.mul_left _
  have hg1tsum : ∑' j : ℕ, (2 * Cg * Real.log (q n) ^ 2) / 2 ^ (j + 1)
      = 2 * Cg * Real.log (q n) ^ 2 := by
    conv_rhs => rw [← tsum_geometric_two' (2 * Cg * Real.log (q n) ^ 2)]
    exact tsum_congr (fun j => by rw [div_div, ← pow_succ'])
  have hg2tsum : ∑' j : ℕ, (2 * Cg) * (((j : ℝ) + 1) ^ 2 / 2 ^ (j + 1)) = 2 * Cg * B := by
    rw [tsum_mul_left, ← hBdef]
  -- assemble
  have key : delta (n + 1) ≤ 2 * Cg * Real.log (q n) ^ 2 + 2 * Cg * B :=
    calc delta (n + 1) = ∑' j : ℕ, (gap (n + 1 + j) : ℝ) / 2 ^ (j + 1) := rfl
      _ ≤ ∑' j : ℕ, ((2 * Cg * Real.log (q n) ^ 2) / 2 ^ (j + 1)
            + (2 * Cg) * (((j : ℝ) + 1) ^ 2 / 2 ^ (j + 1))) :=
          tsum_le_tsum hfg (summable_gap_shift (n + 1)) (hg1sum.add hg2sum)
      _ = ∑' j : ℕ, (2 * Cg * Real.log (q n) ^ 2) / 2 ^ (j + 1)
            + ∑' j : ℕ, (2 * Cg) * (((j : ℝ) + 1) ^ 2 / 2 ^ (j + 1)) :=
          tsum_add hg1sum hg2sum
      _ = 2 * Cg * Real.log (q n) ^ 2 + 2 * Cg * B := by rw [hg1tsum, hg2tsum]
  have hBbound : 2 * Cg * B ≤ Cg * Real.log (q n) ^ 2 := by
    nlinarith [mul_le_mul_of_nonneg_left hn2B hCg0.le]
  linarith [key, hBbound]

end

end Erdos251
