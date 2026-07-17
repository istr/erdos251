import Mathlib
import Erdos251.Hypotheses
import Erdos251.Mertens
import Erdos251.Counting.Words
import Erdos251.Counting.SingularSeries
import Erdos251.Counting.OneExtension

/-!
# Lemmata 4.1 and 4.2 (the statements)

The two statements are together in one module because the item-0014
statement set clustered them under a single heading and the item-0016
split is order-preserving by design (a pure relocation: no declaration
moved past another). Their machinery lives in `SingularSeries.lean` and
`OneExtension.lean`; Lemmata 4.3 and 4.4 sit with their own machinery for
the same order-preserving reason.

RELOCATION ONLY (item-0016). The body below is byte-identical to
`Erdos251/Counting.lean` lines 866-958 at commit
`6683ee0f009baeb5dd6e759f265544e7f91af23d`,
sha256 `fb36ae17e2c92bdabaa500fcd45c6b7e92dfda052253e589a5f4ac04bf14e135`.
No statement, docstring, proof or name was changed. Provenance, the index
conventions, the traceability table and the module map live in the umbrella
`Erdos251/Counting.lean`.
-/

namespace Erdos251

noncomputable section

/-! ## Section 4: the counting lemmata (conditional on A; classical citations) -/

/-- LEMMA 4.1 (singular series lower bound). For admissible `H` of even
offsets with `|H| = k+1`: `S(H) ≥ exp(-C k ln(k+2))`; consequently, in
the budget of Hypothesis A, `M_H(x) ≥ x exp(-C k ln(k+2) - (k+1) lnln x)`
(`= x^{1-o(1)}`, which is prose and is NOT transcribed -- see the report).
Both clauses share the single constant `C`, as in the paper; `k = |H| - 1`
and `k + 2 = |H| + 1`. `0 < C` is added (equivalent: the bound is monotone
in `C`) and flagged. -/
theorem singularSeries_lower_bound :
    ∃ C : ℝ, 0 < C ∧
      (∀ H : Finset ℕ, 0 ∈ H → (∀ h ∈ H, Even h) → IsAdmissible H →
        Real.exp (-(C * ((H.card : ℝ) - 1) * Real.log ((H.card : ℝ) + 1)))
          ≤ singularSeries H) ∧
      (∃ x₀ : ℕ, ∀ x : ℕ, x₀ ≤ x →
        ∀ H : Finset ℕ, 0 ∈ H → (∀ h ∈ H, Even h) → IsAdmissible H →
          (H.card : ℝ) ≤ 4 * Real.log (Real.log x) →
          (∀ h ∈ H, (h : ℝ) ≤ Real.log x ^ 3) →
          (x : ℝ) * Real.exp (-(C * ((H.card : ℝ) - 1) * Real.log ((H.card : ℝ) + 1))
              - (H.card : ℝ) * Real.log (Real.log x))
            ≤ modelMass H x) := by
  refine ⟨12, by norm_num, fun H h0 _ hH => singularSeries_ge_exp h0 hH,
    ⟨3, fun x hx H h0 _ hH _ _ => modelMass_ge_exp hx h0 hH⟩⟩

/-- LEMMA 4.2 (one-point extension sum; v1.1). For any fixed `κ ≥ 1`
there is `C₂ = C₂(κ)` such that for admissible `H` of even offsets with
span `D = h_k ≤ κ k ln(k+2)`, the sum over the one-point extensions of
`S(H ∪ {t})/S(H)` is `≤ C₂ k (ln(k+2))^2`.

The span hypothesis is NECESSARY, not cosmetic (v1.1/F2): for `H = {0,D}`
(`k = 1`) every admissible even `t` has ratio `≥ 1.2` (the `p = 2` factor
alone is 2) and there are `~D/2` such `t`, so the sum grows like `D`
against a `D`-free right side; the unrestricted form is FALSE. -/
theorem oneExtension_sum_le (κ : ℝ) (hκ : 1 ≤ κ) :
    ∃ C₂ : ℝ, ∀ H : Finset ℕ, 0 ∈ H → (∀ h ∈ H, Even h) → IsAdmissible H →
      (offsetSpan H : ℝ) ≤ κ * ((H.card : ℝ) - 1) * Real.log ((H.card : ℝ) + 1) →
      ∑ t ∈ oneExtensions H, singularSeries (insert t H) / singularSeries H
        ≤ C₂ * ((H.card : ℝ) - 1) * Real.log ((H.card : ℝ) + 1) ^ 2 := by
  classical
  set Ex : ℝ := Real.exp ((2 + Real.log κ / Real.log 4) / 2) with hEx
  refine ⟨2 * κ * mertensC3 * Ex, ?_⟩
  intro H h0 _ hH hspan
  have hEx0 : (0:ℝ) < Ex := Real.exp_pos _
  have hC3 : (0:ℝ) < mertensC3 := Real.exp_pos _
  have hκ0 : (0:ℝ) < κ := by linarith
  have hcard1 : 1 ≤ H.card := Finset.card_pos.mpr ⟨0, h0⟩
  have hk1 : (1:ℝ) ≤ (H.card : ℝ) := by exact_mod_cast hcard1
  have hlogk1 : (0:ℝ) ≤ Real.log ((H.card : ℝ) + 1) := Real.log_nonneg (by linarith)
  rcases (oneExtensions H).eq_empty_or_nonempty with hemp | hNE
  · -- `k = 0` corner and any empty range: both sides degenerate, RHS `≥ 0`
    rw [hemp, Finset.sum_empty]
    have hC0 : (0:ℝ) ≤ 2 * κ * mertensC3 * Ex := by positivity
    exact mul_nonneg (mul_nonneg hC0 (by linarith)) (sq_nonneg _)
  · obtain ⟨t0, ht0⟩ := hNE
    have hD2 : 2 ≤ offsetSpan H := by
      rw [oneExtensions, Finset.mem_filter, Finset.mem_range] at ht0
      omega
    have hDR : (2:ℝ) ≤ (offsetSpan H : ℝ) := by exact_mod_cast hD2
    -- the span hypothesis forces `|H| ≥ 2`: at `|H| = 1` it reads `D ≤ 0`
    have hk2 : 2 ≤ H.card := by
      by_contra h
      have hc : H.card = 1 := by omega
      rw [hc] at hspan
      norm_num at hspan
      linarith
    have hk : (2:ℝ) ≤ (H.card : ℝ) := by exact_mod_cast hk2
    set B : ℝ := mertensC3 * Real.log (2 * (H.card : ℝ)) * Ex with hB
    have hlog2k : (0:ℝ) ≤ Real.log (2 * (H.card : ℝ)) := Real.log_nonneg (by linarith)
    have hB0 : (0:ℝ) ≤ B := by rw [hB]; positivity
    have hpre0 : (0:ℝ) ≤ κ * ((H.card : ℝ) - 1) * Real.log ((H.card : ℝ) + 1) := by
      apply mul_nonneg (mul_nonneg hκ0.le (by linarith)) hlogk1
    calc ∑ t ∈ oneExtensions H, singularSeries (insert t H) / singularSeries H
        ≤ ∑ _t ∈ oneExtensions H, B :=
          Finset.sum_le_sum (fun t ht => singularSeries_ratio_le hκ hH hk2 hspan ht)
      _ = ((oneExtensions H).card : ℝ) * B := by rw [Finset.sum_const, nsmul_eq_mul]
      _ ≤ (offsetSpan H : ℝ) * B := by
          refine mul_le_mul_of_nonneg_right ?_ hB0
          have hle : (oneExtensions H).card ≤ offsetSpan H := by
            rw [oneExtensions]
            calc (Finset.filter _ (Finset.range (offsetSpan H))).card
                ≤ (Finset.range (offsetSpan H)).card := Finset.card_filter_le _ _
              _ = offsetSpan H := Finset.card_range _
          exact_mod_cast hle
      _ ≤ (κ * ((H.card : ℝ) - 1) * Real.log ((H.card : ℝ) + 1)) * B :=
          mul_le_mul_of_nonneg_right hspan hB0
      _ ≤ (κ * ((H.card : ℝ) - 1) * Real.log ((H.card : ℝ) + 1))
            * (mertensC3 * (2 * Real.log ((H.card : ℝ) + 1)) * Ex) := by
          refine mul_le_mul_of_nonneg_left ?_ hpre0
          rw [hB]
          exact mul_le_mul_of_nonneg_right
            (mul_le_mul_of_nonneg_left (log_two_card_le hk2) hC3.le) hEx0.le
      _ = _ := by ring

end

end Erdos251
