import Erdos251.Basic

/-!
# Hypothesis layer (chain-v1 section 1): `HLQuantA` and `CramerGranville`

DEFINED, not stubbed (chain-v1 8.2). This file replaces the round-0
placeholder `HypUniformTuples : Prop := True` -- item-0002's "no `True`
stubs" requirement.

Design (review-2 lesson, chain-v1 section 1): Hypothesis A counts
NONCONSECUTIVE admissible tuples, whose in-budget model masses are
`x^{1-o(1)} ≫ 1` (chain-v1 Lemma 4.1), so a fixed two-sided factor 2 is
integrality-safe. The gpt-iso template 9.8 (`HLQuantFull`) demands relative
accuracy on exact gap cylinders and is provably false as stated
(triage-1b: same Q1 defect as the gpt-web chain); it is deliberately NOT
ported. Consecutiveness is DERIVED downstream (chain-v1 Lemma 4.3), never
assumed.

Faithfulness notes:
* chain-v1's Hypothesis A displays a constant `C_A ≥ 1` that its
  inequality never uses; flagged as vestigial (ledger ANN-12), not encoded.
* `singularSeries` is a `tprod`, which mathlib defaults to 1 when not
  `Multipliable`; for admissible `H` the product IS multipliable
  (`singularSeries_multipliable`), so the Lean `HLQuantA` matches the
  paper hypothesis.
-/

namespace Erdos251

noncomputable section

/-- Number of residue classes mod `p` occupied by `H`. -/
def nuMod (H : Finset ℕ) (p : ℕ) : ℕ :=
  (H.image (Nat.cast : ℕ → ZMod p)).card

/-- Admissibility: no prime has all of its residue classes occupied
(chain-v1 section 1). -/
def IsAdmissible (H : Finset ℕ) : Prop :=
  ∀ p : ℕ, p.Prime → nuMod H p < p

/-- Singular series `S(H) = ∏_p (1 - ν_H(p)/p) (1 - 1/p)^{-|H|}`. -/
def singularSeries (H : Finset ℕ) : ℝ :=
  ∏' p : Nat.Primes,
    (1 - (nuMod H (p : ℕ) : ℝ) / ((p : ℕ) : ℝ)) /
      (1 - 1 / ((p : ℕ) : ℝ)) ^ H.card

/-- Nonconsecutive tuple count `π_H(x) = #{a ≤ x : a + h prime ∀ h ∈ H}`
(with `0 ∈ H` this in particular forces `a` prime). -/
def tupleCount (H : Finset ℕ) (x : ℕ) : ℕ :=
  ((Finset.range (x + 1)).filter fun a => ∀ h ∈ H, (a + h).Prime).card

/-- Hardy-Littlewood model mass `M_H(x) = S(H) · x / (log x)^{|H|}`. -/
def modelMass (H : Finset ℕ) (x : ℕ) : ℝ :=
  singularSeries H * (x : ℝ) / Real.log x ^ H.card

/-! ### Proof-layer helpers (item-0015; not statements) -/

section SingularSeriesProofHelpers

open Filter

/-- Above the span of `H`, reduction mod `p` is injective on `H`, so `H`
occupies exactly `|H|` residue classes. (No primality needed.) -/
theorem nuMod_eq_card_of_sup_lt {H : Finset ℕ} {p : ℕ} (hlarge : H.sup id < p) :
    nuMod H p = H.card := by
  unfold nuMod
  apply Finset.card_image_of_injOn
  intro a ha b hb hab
  have hA : a < p := lt_of_le_of_lt (Finset.le_sup (f := id) ha) hlarge
  have hB : b < p := lt_of_le_of_lt (Finset.le_sup (f := id) hb) hlarge
  have h := congrArg ZMod.val hab
  rwa [ZMod.val_cast_of_lt hA, ZMod.val_cast_of_lt hB] at h

/-- Each local factor is positive, by admissibility (`ν_H(p) < p`) and `p ≥ 2`. -/
theorem singularFactor_pos {H : Finset ℕ} (hH : IsAdmissible H) (p : Nat.Primes) :
    0 < (1 - (nuMod H (p : ℕ) : ℝ) / ((p : ℕ) : ℝ)) /
      (1 - 1 / ((p : ℕ) : ℝ)) ^ H.card := by
  have hp : (p : ℕ).Prime := p.2
  have h2 : (2:ℝ) ≤ ((p : ℕ) : ℝ) := by exact_mod_cast hp.two_le
  have hnum : 0 < 1 - (nuMod H (p : ℕ) : ℝ) / ((p : ℕ) : ℝ) := by
    have hlt : (nuMod H (p : ℕ) : ℝ) < ((p : ℕ) : ℝ) := by exact_mod_cast hH _ hp
    rw [sub_pos, div_lt_one (by linarith)]
    exact hlt
  have hden : (0:ℝ) < 1 - 1 / ((p : ℕ) : ℝ) := by
    rw [sub_pos, div_lt_one (by linarith)]; linarith
  positivity

/-- First-order log estimate: for `|x| ≤ 1/2` the linear term `x` captures
`-log (1 - x)` up to a quadratic error. The `n = 1` case of
`Real.abs_log_sub_add_sum_range_le`. -/
theorem abs_add_log_one_sub_le {x : ℝ} (h : |x| ≤ 1/2) :
    |x + Real.log (1 - x)| ≤ 2 * x ^ 2 := by
  have h1 : |x| < 1 := lt_of_le_of_lt h (by norm_num)
  have key := Real.abs_log_sub_add_sum_range_le h1 1
  rw [Finset.sum_range_one] at key
  norm_num at key
  refine key.trans ?_
  rw [div_le_iff₀ (by linarith)]
  nlinarith [sq_nonneg x, abs_nonneg x]

/-- `∑_p 1/p²` converges. -/
theorem summable_one_div_prime_sq :
    Summable (fun p : Nat.Primes => (1:ℝ) / ((p : ℕ) : ℝ) ^ 2) := by
  have h := Nat.Primes.summable_rpow.mpr (show (-2:ℝ) < -1 by norm_num)
  refine h.congr (fun p => ?_)
  have hp0 : (0:ℝ) < ((p : ℕ) : ℝ) := by exact_mod_cast p.2.pos
  rw [show (-2:ℝ) = -((2:ℕ):ℝ) by norm_num, Real.rpow_neg hp0.le, Real.rpow_natCast]
  simp [one_div]

/-- Only finitely many primes lie below any bound. -/
theorem finite_primes_le (N : ℕ) : {p : Nat.Primes | (p : ℕ) ≤ N}.Finite := by
  have h : {p : Nat.Primes | (p : ℕ) ≤ N}
      = (fun p : Nat.Primes => (p : ℕ)) ⁻¹' (Set.Iic N) := rfl
  rw [h]
  exact Set.Finite.preimage (Nat.Primes.coe_nat_injective.injOn) (Set.finite_Iic N)

/-- Tail bound `|log factor_p| ≤ (2|H|² + 2|H|)/p²` for every prime `p`
exceeding both the span of `H` and `2|H|`. The linear terms of the two logs
cancel exactly; admissibility is NOT needed here. -/
theorem abs_log_singularFactor_le {H : Finset ℕ} (p : Nat.Primes)
    (hlarge : max (H.sup id) (2 * H.card) < (p : ℕ)) :
    |Real.log ((1 - (nuMod H (p : ℕ) : ℝ) / ((p : ℕ) : ℝ)) /
      (1 - 1 / ((p : ℕ) : ℝ)) ^ H.card)|
      ≤ (2 * (H.card : ℝ) ^ 2 + 2 * (H.card : ℝ)) * (1 / ((p : ℕ) : ℝ) ^ 2) := by
  have hp : (p : ℕ).Prime := p.2
  set P : ℝ := ((p : ℕ) : ℝ) with hPdef
  set k : ℝ := (H.card : ℝ) with hkdef
  have hP2 : (2:ℝ) ≤ P := by rw [hPdef]; exact_mod_cast hp.two_le
  have hP0 : (0:ℝ) < P := by linarith
  have hk0 : (0:ℝ) ≤ k := Nat.cast_nonneg _
  have hspan : H.sup id < (p : ℕ) := lt_of_le_of_lt (le_max_left _ _) hlarge
  have h2k : 2 * H.card < (p : ℕ) := lt_of_le_of_lt (le_max_right _ _) hlarge
  have h2kR : 2 * k < P := by rw [hkdef, hPdef]; exact_mod_cast h2k
  rw [nuMod_eq_card_of_sup_lt hspan]
  have hx1 : |k / P| ≤ 1/2 := by
    rw [abs_of_nonneg (by positivity), div_le_iff₀ hP0]; linarith
  have hx2 : |1 / P| ≤ 1/2 := by
    rw [abs_of_nonneg (by positivity), div_le_iff₀ hP0]; linarith
  have hnum : (0:ℝ) < 1 - k / P := by
    have : k / P < 1 := by rw [div_lt_one hP0]; linarith
    linarith
  have hden : (0:ℝ) < 1 - 1 / P := by
    have : 1 / P < 1 := by rw [div_lt_one hP0]; linarith
    linarith
  rw [Real.log_div (ne_of_gt hnum) (by positivity), Real.log_pow]
  have e1 := abs_add_log_one_sub_le hx1
  have e2 := abs_add_log_one_sub_le hx2
  have hAB : Real.log (1 - k / P) - k * Real.log (1 - 1 / P)
      = (k / P + Real.log (1 - k / P)) - k * (1 / P + Real.log (1 - 1 / P)) := by ring
  rw [hAB]
  have habs : |k * (1 / P + Real.log (1 - 1 / P))| = k * |1 / P + Real.log (1 - 1 / P)| := by
    rw [abs_mul, abs_of_nonneg hk0]
  calc |(k / P + Real.log (1 - k / P)) - k * (1 / P + Real.log (1 - 1 / P))|
      ≤ |k / P + Real.log (1 - k / P)| + |k * (1 / P + Real.log (1 - 1 / P))| := abs_sub _ _
    _ = |k / P + Real.log (1 - k / P)| + k * |1 / P + Real.log (1 - 1 / P)| := by rw [habs]
    _ ≤ 2 * (k / P) ^ 2 + k * (2 * (1 / P) ^ 2) :=
        add_le_add e1 (mul_le_mul_of_nonneg_left e2 hk0)
    _ = (2 * k ^ 2 + 2 * k) * (1 / P ^ 2) := by field_simp; ring

/-- The log-series converges, by cofinite comparison with `(2|H|²+2|H|)/p²`.
Unconditional: admissibility plays no role in convergence. -/
theorem summable_log_singularFactor {H : Finset ℕ} :
    Summable (fun p : Nat.Primes => Real.log
      ((1 - (nuMod H (p : ℕ) : ℝ) / ((p : ℕ) : ℝ)) /
        (1 - 1 / ((p : ℕ) : ℝ)) ^ H.card)) := by
  apply Summable.of_norm_bounded_eventually
    (fun p : Nat.Primes =>
      (2 * (H.card : ℝ) ^ 2 + 2 * (H.card : ℝ)) * (1 / ((p : ℕ) : ℝ) ^ 2))
    (summable_one_div_prime_sq.mul_left _)
  rw [eventually_cofinite]
  apply Set.Finite.subset (finite_primes_le (max (H.sup id) (2 * H.card)))
  intro p hp
  simp only [Set.mem_setOf_eq] at hp ⊢
  by_contra hcon
  push_neg at hcon
  exact hp (by rw [Real.norm_eq_abs]; exact abs_log_singularFactor_le p hcon)

end SingularSeriesProofHelpers

/-- The singular-series product converges unconditionally for admissible
`H` (head factors positive by admissibility, tail log-factors
`O(|H|²/p²)`). Load-bearing for the faithfulness of `HLQuantA`; see the
module docstring. -/
theorem singularSeries_multipliable {H : Finset ℕ} (hH : IsAdmissible H) :
    Multipliable (fun p : Nat.Primes =>
      (1 - (nuMod H (p : ℕ) : ℝ) / ((p : ℕ) : ℝ)) /
        (1 - 1 / ((p : ℕ) : ℝ)) ^ H.card) := by
  exact Real.multipliable_of_summable_log _ (singularFactor_pos hH) summable_log_singularFactor

/-- Positivity of the singular series for admissible `H`
(chain-v1 Lemma 4.1 direction; quantitative form `≥ e^{-Ck log k}` is
part of the counting layer). -/
theorem singularSeries_pos {H : Finset ℕ} (hH : IsAdmissible H) :
    0 < singularSeries H := by
  rw [singularSeries,
    ← Real.rexp_tsum_eq_tprod _ (singularFactor_pos hH) summable_log_singularFactor]
  exact Real.exp_pos _

/-- HYPOTHESIS A (chain-v1 section 1): uniform two-sided tuple counts.
Window: `|H| ≤ 4 lnln x`, span `≤ (log x)^3`, even offsets containing 0,
factor 2 on both sides. -/
def HLQuantA : Prop :=
  ∃ x0 : ℕ, ∀ x : ℕ, x0 ≤ x →
    ∀ H : Finset ℕ, 0 ∈ H → (∀ h ∈ H, Even h) → IsAdmissible H →
      (H.card : ℝ) ≤ 4 * Real.log (Real.log x) →
      (∀ h ∈ H, (h : ℝ) ≤ Real.log x ^ 3) →
      modelMass H x / 2 ≤ (tupleCount H x : ℝ) ∧
        (tupleCount H x : ℝ) ≤ 2 * modelMass H x

/-- HYPOTHESIS B (chain-v1 section 1): Cramer-Granville pointwise gap
bound, in Lean gap indexing (`gap n` = paper `g_{n+1}`; equivalent as an
eventual statement). -/
def CramerGranville : Prop :=
  ∃ C : ℝ, ∃ n0 : ℕ, ∀ n : ℕ, n0 ≤ n →
    (gap n : ℝ) ≤ C * Real.log (q n) ^ 2

end

end Erdos251
