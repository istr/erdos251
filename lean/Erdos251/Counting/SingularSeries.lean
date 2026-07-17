import Mathlib
import Erdos251.Hypotheses
import Erdos251.Mertens

/-!
# Lemma 4.1 layer: singular-series and model-mass lower bounds

The Mertens-free Euler-product split of item-0015 session 1 (head at
`P0 = 2|H|` via `primorial_le_4_pow`, one-sided tail), the `primesLe`
index bridge to `Mertens.primesUpto`, and the two lower bounds
`singularSeries_ge_exp` / `modelMass_ge_exp` that Lemma 4.1 and Lemma 4.3
consume. The statements of Lemmata 4.1 and 4.2 live in
`Erdos251/Counting/Lemmata.lean` -- see the module map in the umbrella.

RELOCATION ONLY (item-0016). The body below is byte-identical to
`Erdos251/Counting.lean` lines 116-447 at commit
`6683ee0f009baeb5dd6e759f265544e7f91af23d`,
sha256 `e89360467893310d7054d3b459c479c258612dbab41cfa6bc39e5f4592b86dc0`.
No statement, docstring, proof or name was changed. Provenance, the index
conventions, the traceability table and the module map live in the umbrella
`Erdos251/Counting.lean`.
-/

namespace Erdos251

noncomputable section

/-! ### Proof-layer helpers for Lemma 4.1 (item-0015; not statements)

The Mertens-free route of session 3: split the Euler product at
`P₀ = 2|H|`. The head is controlled by `primorial_le_4_pow` (no Mertens),
the tail by the ONE-SIDED sibling of `abs_log_singularFactor_le` in which
the linear terms cancel one-sidedly under `ν ≤ |H|` (no span condition).
-/

/-- HEAD (`p ≤ P₀`): admissibility gives `ν ≤ p-1`, hence `1 - ν/p ≥ 1/p`;
`(1-1/p)^k ≤ 1` only helps, so the factor is `≥ 1/p` and its log `≥ -log p`.
No span condition. -/
theorem log_singularFactor_head_ge {H : Finset ℕ} (hH : IsAdmissible H) (p : Nat.Primes) :
    -Real.log ((p : ℕ) : ℝ)
      ≤ Real.log ((1 - (nuMod H (p : ℕ) : ℝ) / ((p : ℕ) : ℝ)) /
          (1 - 1 / ((p : ℕ) : ℝ)) ^ H.card) := by
  have hp : (p : ℕ).Prime := p.2
  set P : ℝ := ((p : ℕ) : ℝ) with hPdef
  have hP2 : (2:ℝ) ≤ P := by rw [hPdef]; exact_mod_cast hp.two_le
  have hP0 : (0:ℝ) < P := by linarith
  have hnu : (nuMod H (p:ℕ) : ℝ) + 1 ≤ P := by
    have h : nuMod H (p:ℕ) < (p:ℕ) := hH _ hp
    rw [hPdef]; exact_mod_cast h
  have hden0 : (0:ℝ) < 1 - 1 / P := by rw [sub_pos, div_lt_one hP0]; linarith
  have hden1 : (1 - 1 / P) ^ H.card ≤ 1 :=
    pow_le_one₀ hden0.le (by have : (0:ℝ) < 1 / P := by positivity
                             linarith)
  have hdenpow : (0:ℝ) < (1 - 1 / P) ^ H.card := by positivity
  have hnum : (1:ℝ) / P ≤ 1 - (nuMod H (p:ℕ) : ℝ) / P := by
    rw [le_sub_iff_add_le, div_add_div_same, div_le_one hP0]
    linarith
  have hfac : (1:ℝ) / P ≤ (1 - (nuMod H (p:ℕ) : ℝ) / P) / (1 - 1 / P) ^ H.card := by
    rw [le_div_iff₀ hdenpow]
    have h1 : (1:ℝ) / P * (1 - 1 / P) ^ H.card ≤ 1 / P * 1 :=
      mul_le_mul_of_nonneg_left hden1 (by positivity)
    linarith
  have := Real.log_le_log (by positivity : (0:ℝ) < 1 / P) hfac
  rwa [Real.log_div one_ne_zero (ne_of_gt hP0), Real.log_one, zero_sub] at this

/-- TAIL (`p > 2|H|`): the ONE-SIDED sibling of `abs_log_singularFactor_le`
with `ν ≤ |H|` in place of `ν = |H|`, valid for ALL `p > 2|H|` with NO span
condition (and no admissibility). The linear terms cancel one-sidedly:
`log(1-ν/p) - k log(1-1/p) ≥ log(1-k/p) + k/p ≥ -2(k/p)²`. -/
theorem log_singularFactor_tail_ge {H : Finset ℕ} (p : Nat.Primes)
    (hlarge : 2 * H.card < (p : ℕ)) :
    -(2 * (H.card : ℝ) ^ 2 * (1 / ((p : ℕ) : ℝ) ^ 2))
      ≤ Real.log ((1 - (nuMod H (p : ℕ) : ℝ) / ((p : ℕ) : ℝ)) /
          (1 - 1 / ((p : ℕ) : ℝ)) ^ H.card) := by
  have hp : (p : ℕ).Prime := p.2
  set P : ℝ := ((p : ℕ) : ℝ) with hPdef
  set k : ℝ := (H.card : ℝ) with hkdef
  have hP2 : (2:ℝ) ≤ P := by rw [hPdef]; exact_mod_cast hp.two_le
  have hP0 : (0:ℝ) < P := by linarith
  have hk0 : (0:ℝ) ≤ k := Nat.cast_nonneg _
  have h2kR : 2 * k < P := by rw [hkdef, hPdef]; exact_mod_cast hlarge
  -- `ν ≤ |H|` unconditionally (no admissibility, no span)
  have hnu : (nuMod H (p:ℕ) : ℝ) ≤ k := by
    rw [hkdef]; exact_mod_cast Finset.card_image_le
  have hnu0 : (0:ℝ) ≤ (nuMod H (p:ℕ) : ℝ) := Nat.cast_nonneg _
  have hkP : k / P < 1 / 2 := by rw [div_lt_div_iff₀ hP0 (by norm_num)]; linarith
  have hkP0 : (0:ℝ) ≤ k / P := by positivity
  have hnumk : (0:ℝ) < 1 - k / P := by linarith
  have hnumnu : (0:ℝ) < 1 - (nuMod H (p:ℕ) : ℝ) / P := by
    have : (nuMod H (p:ℕ) : ℝ) / P ≤ k / P := by gcongr
    linarith
  have hden0 : (0:ℝ) < 1 - 1 / P := by rw [sub_pos, div_lt_one hP0]; linarith
  -- split the log
  rw [Real.log_div (ne_of_gt hnumnu) (by positivity), Real.log_pow]
  -- (a) numerator: monotone in `ν ≤ k`
  have hA : Real.log (1 - k / P) ≤ Real.log (1 - (nuMod H (p:ℕ) : ℝ) / P) := by
    apply Real.log_le_log hnumk
    have : (nuMod H (p:ℕ) : ℝ) / P ≤ k / P := by gcongr
    linarith
  -- (b) denominator: `-log(1-1/p) ≥ 1/p`
  have hB : Real.log (1 - 1 / P) ≤ -(1 / P) := by
    have := Real.log_le_sub_one_of_pos hden0; linarith
  -- (c) quadratic control of the surviving `log(1-k/P) + k/P`
  have hx : |k / P| ≤ 1/2 := by rw [abs_of_nonneg hkP0]; linarith
  have hC := abs_add_log_one_sub_le hx
  have hC' : -(2 * (k / P) ^ 2) ≤ k / P + Real.log (1 - k / P) := (abs_le.mp hC).1
  have hsq : 2 * (k / P) ^ 2 = 2 * k ^ 2 * (1 / P ^ 2) := by field_simp
  have hkB : k * (1 / P) ≤ k * (-(Real.log (1 - 1 / P))) :=
    mul_le_mul_of_nonneg_left (by linarith) hk0
  have hkPeq : k * (1 / P) = k / P := by ring
  rw [← hsq]
  linarith [hA, hC', hkB, hkPeq]

/-- The head Finset: the primes `≤ N`, as a `Finset Nat.Primes`.

The `Nat.Primes`-indexed twin of `Mertens.lean`'s canonical `primesUpto`, which
`primesLe_image` bridges onto. Both are needed and neither is redundant: the
singular series is a `tprod` over `Nat.Primes`, so its head must be indexed
there, while the Mertens pack is `Finset ℕ`-indexed (mathlib's `primorial`
convention) and must stay project-free. `primesLe` cannot join it: it is built
from `finite_primes_le` (`Hypotheses.lean`). Every shared fact is proved ONCE,
over `primesUpto`, and transported here across the bridge (ANN-39). -/
def primesLe (N : ℕ) : Finset Nat.Primes := (finite_primes_le N).toFinset

theorem mem_primesLe {N : ℕ} {p : Nat.Primes} : p ∈ primesLe N ↔ (p : ℕ) ≤ N := by
  simp [primesLe, finite_primes_le]

/-- THE BRIDGE: the head Finset coerces onto `primesUpto` (= mathlib's
primorial index set). The coercion is injective, so `Finset.sum_image`
transports `primesUpto` facts to `primesLe` (`sum_primesLe_eq`). -/
theorem primesLe_image (N : ℕ) :
    (primesLe N).image (fun p : Nat.Primes => (p : ℕ)) = primesUpto N := by
  ext n
  simp only [primesUpto, Finset.mem_image, Finset.mem_filter, Finset.mem_range, mem_primesLe]
  constructor
  · rintro ⟨p, hp, rfl⟩; exact ⟨by omega, p.2⟩
  · rintro ⟨hn, hnp⟩; exact ⟨⟨n, hnp⟩, by simp [mem_primesLe]; omega, rfl⟩

/-- TRANSPORT: any `ℕ`-indexed summand sums the same over `primesLe` and over
`primesUpto`. This is the one-way valve of the unification: a fact is proved
over `primesUpto` (mathlib-only, upstreamable) and lands here for free. -/
theorem sum_primesLe_eq {M : Type*} [AddCommMonoid M] (f : ℕ → M) {N : ℕ} :
    ∑ p ∈ primesLe N, f (p : ℕ) = ∑ n ∈ primesUpto N, f n := by
  rw [← primesLe_image N]
  exact (Finset.sum_image (fun a _ b _ h => Subtype.ext h)).symm

/-- HEAD SUM: `∑_{p ≤ N} log p = log N# ≤ N log 4` (`primorial_le_4_pow`). No Mertens.

The `Nat.Primes`-indexed transport of `sum_log_primesUpto_le` (`Mertens.lean`)
across the bridge; the primorial argument itself is proved there and not
repeated here (ANN-39 unification). "No Mertens" still holds: the cited input
is the primorial bound the pack itself runs on, not one of M1-M3. -/
theorem sum_log_primesLe_le (N : ℕ) :
    ∑ p ∈ primesLe N, Real.log ((p : ℕ) : ℝ) ≤ (N : ℝ) * Real.log 4 := by
  rw [sum_primesLe_eq (fun n => Real.log (n : ℝ))]
  exact sum_log_primesUpto_le N

/-- TAIL SUM: `∑_{p > N} 1/p² ≤ 1/N`, by comparison with `∑_{n > N} 1/n²`
along the (injective) prime-to-ℕ map (`sum_Ioc_inv_sq_le_sub`). Integral-free. -/
theorem tsum_compl_primesLe_inv_sq_le {N : ℕ} (hN : N ≠ 0) :
    ∑' p : ↑((primesLe N : Finset Nat.Primes) : Set Nat.Primes)ᶜ,
        (1 / (((p : Nat.Primes) : ℕ) : ℝ) ^ 2) ≤ 1 / (N : ℝ) := by
  have hNR : (0:ℝ) < (N : ℝ) := by exact_mod_cast Nat.pos_of_ne_zero hN
  refine tsum_le_of_sum_le (summable_one_div_prime_sq.subtype _) (fun T => ?_)
  -- explicitly typed to avoid the subtype-coercion elaboration trap
  let φ : ↑((primesLe N : Finset Nat.Primes) : Set Nat.Primes)ᶜ → ℕ := fun p => (p.1 : ℕ)
  have hgt : ∀ p : ↑((primesLe N : Finset Nat.Primes) : Set Nat.Primes)ᶜ, N < φ p := by
    intro p
    have h := p.2
    rw [Set.mem_compl_iff, Finset.mem_coe, mem_primesLe] at h
    simp only [φ]
    omega
  have hginj : ∀ x ∈ T, ∀ y ∈ T, φ x = φ y → x = y := by
    intro x _ y _ h
    exact Subtype.ext (Subtype.ext h)
  set T' : Finset ℕ := Finset.image φ T with hT'
  have hsum : ∑ p ∈ T, (1 / (((p : Nat.Primes) : ℕ) : ℝ) ^ 2)
      = ∑ n ∈ T', (1 / (n : ℝ) ^ 2) := by
    rw [hT', Finset.sum_image hginj]
  rw [hsum]
  rcases T'.eq_empty_or_nonempty with hE | hNE
  · rw [hE, Finset.sum_empty]; positivity
  · set M := T'.sup id with hM
    have hmemN : ∀ n ∈ T', N < n ∧ n ≤ M := by
      intro n hn
      refine ⟨?_, Finset.le_sup (f := id) hn⟩
      rw [hT', Finset.mem_image] at hn
      obtain ⟨p, _, rfl⟩ := hn
      exact hgt p
    have hsub : T' ⊆ Finset.Ioc N M := fun n hn => Finset.mem_Ioc.mpr (hmemN n hn)
    have hNM : N ≤ M := by
      obtain ⟨n, hn⟩ := hNE
      have := hmemN n hn; omega
    calc ∑ n ∈ T', (1 / (n : ℝ) ^ 2) ≤ ∑ n ∈ Finset.Ioc N M, (1 / (n : ℝ) ^ 2) :=
          Finset.sum_le_sum_of_subset_of_nonneg hsub (fun i _ _ => by positivity)
      _ = ∑ n ∈ Finset.Ioc N M, (((n : ℝ) ^ 2)⁻¹) :=
          Finset.sum_congr rfl (fun i _ => one_div _)
      _ ≤ ((N:ℝ))⁻¹ - ((M:ℝ))⁻¹ := sum_Ioc_inv_sq_le_sub hN hNM
      _ ≤ 1 / (N : ℝ) := by
          rw [one_div]
          have : (0:ℝ) ≤ ((M:ℝ))⁻¹ := by positivity
          linarith

/-- The `k = 0` corner: `0 ∈ H` and `|H| = 1` force `H = {0}`, where every
local factor is `(1-1/p)/(1-1/p)^1 = 1`, so `S = 1`. This is EXACTLY the
target at `k = 0` (`exp(-C·0·log 2) = 1`), so the corner cannot be absorbed
into the generic bound -- it needs equality. -/
theorem singularSeries_singleton_zero : singularSeries {0} = 1 := by
  rw [singularSeries]
  have h : ∀ p : Nat.Primes,
      (1 - (nuMod {0} (p : ℕ) : ℝ) / ((p : ℕ) : ℝ)) /
        (1 - 1 / ((p : ℕ) : ℝ)) ^ ({0} : Finset ℕ).card = 1 := by
    intro p
    have hp : (p : ℕ).Prime := p.2
    have hP2 : (2:ℝ) ≤ ((p : ℕ) : ℝ) := by exact_mod_cast hp.two_le
    have hden : (0:ℝ) < 1 - 1 / ((p : ℕ) : ℝ) := by
      rw [sub_pos, div_lt_one (by linarith)]; linarith
    have hnu : nuMod {0} (p : ℕ) = 1 := by
      unfold nuMod; simp
    rw [hnu]
    simp only [Finset.card_singleton, pow_one, Nat.cast_one]
    rw [div_self (ne_of_gt hden)]
  rw [tprod_congr h, tprod_one]

/-- T1 CLAUSE 1 (the real content), Mertens-free. Head `p ≤ 2|H|`:
`≥ 1/primorial(2|H|) ≥ 4^{-2|H|}`. Tail `p > 2|H|`: one-sided linear
cancellation, `≥ -2|H|² ∑_{p>2|H|} 1/p² ≥ -|H|`. Explicit constant `C = 10`. -/
theorem singularSeries_ge_exp {H : Finset ℕ} (h0 : 0 ∈ H) (hH : IsAdmissible H) :
    Real.exp (-(12 * ((H.card : ℝ) - 1) * Real.log ((H.card : ℝ) + 1)))
      ≤ singularSeries H := by
  have hne : H.Nonempty := ⟨0, h0⟩
  have hcard1 : 1 ≤ H.card := Finset.card_pos.mpr hne
  rcases Nat.lt_or_ge H.card 2 with hc1 | hc2
  · -- k = 0 corner: H = {0}
    have hc : H.card = 1 := by omega
    have hH0 : H = {0} := by
      obtain ⟨a, ha⟩ := Finset.card_eq_one.mp hc
      rw [ha] at h0 ⊢
      rw [Finset.mem_singleton] at h0
      rw [h0]
    rw [hH0, singularSeries_singleton_zero]
    rw [hH0] at hc
    rw [hc]
    norm_num
  · -- k ≥ 1: the generic bound
    set P₀ := 2 * H.card with hP₀
    have hP₀0 : P₀ ≠ 0 := by omega
    rw [singularSeries,
      ← Real.rexp_tsum_eq_tprod _ (singularFactor_pos hH) summable_log_singularFactor]
    apply Real.exp_le_exp.mpr
    rw [← sum_add_tsum_compl (s := primesLe P₀) summable_log_singularFactor]
    -- HEAD: `≥ -log(primorial P₀) ≥ -P₀ log 4`
    have hhead : -((P₀:ℝ) * Real.log 4)
        ≤ ∑ p ∈ primesLe P₀, Real.log ((1 - (nuMod H (p : ℕ) : ℝ) / ((p : ℕ) : ℝ)) /
            (1 - 1 / ((p : ℕ) : ℝ)) ^ H.card) := by
      calc -((P₀:ℝ) * Real.log 4) ≤ -(∑ p ∈ primesLe P₀, Real.log ((p:ℕ):ℝ)) := by
            linarith [sum_log_primesLe_le P₀]
        _ = ∑ p ∈ primesLe P₀, (-Real.log ((p:ℕ):ℝ)) := by rw [Finset.sum_neg_distrib]
        _ ≤ _ := Finset.sum_le_sum (fun p _ => log_singularFactor_head_ge hH p)
    -- TAIL: one-sided cancellation, `≥ -2|H|² · (1/P₀) = -|H|`
    have htail : -((H.card : ℝ))
        ≤ ∑' p : ↑((primesLe P₀ : Finset Nat.Primes) : Set Nat.Primes)ᶜ,
            Real.log ((1 - (nuMod H ((p : Nat.Primes) : ℕ) : ℝ) / (((p : Nat.Primes) : ℕ) : ℝ)) /
              (1 - 1 / (((p : Nat.Primes) : ℕ) : ℝ)) ^ H.card) := by
      have hsummin : Summable (fun p : ↑((primesLe P₀ : Finset Nat.Primes) : Set Nat.Primes)ᶜ =>
          -(2 * (H.card:ℝ)^2 * (1 / (((p : Nat.Primes) : ℕ) : ℝ)^2))) :=
        ((summable_one_div_prime_sq.subtype _).mul_left _).neg
      have hpt : ∀ p : ↑((primesLe P₀ : Finset Nat.Primes) : Set Nat.Primes)ᶜ,
          -(2 * (H.card:ℝ)^2 * (1 / (((p : Nat.Primes) : ℕ) : ℝ)^2))
            ≤ Real.log ((1 - (nuMod H ((p : Nat.Primes) : ℕ) : ℝ) / (((p : Nat.Primes) : ℕ) : ℝ)) /
              (1 - 1 / (((p : Nat.Primes) : ℕ) : ℝ)) ^ H.card) := by
        intro p
        apply log_singularFactor_tail_ge
        have h := p.2
        rw [Set.mem_compl_iff, Finset.mem_coe, mem_primesLe] at h
        omega
      have hcard0 : (0:ℝ) ≤ 2 * (H.card:ℝ)^2 := by positivity
      have hkey : ∑' p : ↑((primesLe P₀ : Finset Nat.Primes) : Set Nat.Primes)ᶜ,
          -(2 * (H.card:ℝ)^2 * (1 / (((p : Nat.Primes) : ℕ) : ℝ)^2))
            = -(2 * (H.card:ℝ)^2 * ∑' p : ↑((primesLe P₀ : Finset Nat.Primes) : Set Nat.Primes)ᶜ,
                (1 / (((p : Nat.Primes) : ℕ) : ℝ)^2)) := by
        rw [tsum_neg, tsum_mul_left]
      have hP₀R : ((P₀:ℕ):ℝ) = 2 * (H.card:ℝ) := by rw [hP₀]; push_cast; ring
      calc -((H.card : ℝ)) = -(2 * (H.card:ℝ)^2 * (1 / ((P₀:ℕ):ℝ))) := by
            rw [hP₀R]
            have : (0:ℝ) < (H.card:ℝ) := by exact_mod_cast hcard1
            field_simp
            ring
        _ ≤ -(2 * (H.card:ℝ)^2 * ∑' p : ↑((primesLe P₀ : Finset Nat.Primes) : Set Nat.Primes)ᶜ,
                (1 / (((p : Nat.Primes) : ℕ) : ℝ)^2)) := by
            have := tsum_compl_primesLe_inv_sq_le (N := P₀) hP₀0
            nlinarith [this, hcard0]
        _ = ∑' p : ↑((primesLe P₀ : Finset Nat.Primes) : Set Nat.Primes)ᶜ,
              -(2 * (H.card:ℝ)^2 * (1 / (((p : Nat.Primes) : ℕ) : ℝ)^2)) := hkey.symm
        _ ≤ _ := tsum_le_tsum hpt hsummin (summable_log_singularFactor.subtype _)
    -- the constant: `10 (k) log(k+2) ≥ 2(k+1) log 4 + (k+1)` for `k ≥ 1`
    have harith : -(12 * ((H.card : ℝ) - 1) * Real.log ((H.card : ℝ) + 1))
        ≤ -((P₀:ℝ) * Real.log 4) + -((H.card : ℝ)) := by
      have hc2R : (2:ℝ) ≤ (H.card:ℝ) := by exact_mod_cast hc2
      have hl2 : (0.69:ℝ) < Real.log 2 := by linarith [Real.log_two_gt_d9]
      have hlog4 : Real.log 4 = 2 * Real.log 2 := by
        rw [show (4:ℝ) = 2^2 by norm_num, Real.log_pow]; push_cast; ring
      have hlogc : Real.log 2 ≤ Real.log ((H.card:ℝ) + 1) :=
        Real.log_le_log (by norm_num) (by linarith)
      have hP₀R : ((P₀:ℕ):ℝ) = 2 * (H.card:ℝ) := by rw [hP₀]; push_cast; ring
      rw [hP₀R, hlog4]
      nlinarith [hlogc, hl2, hc2R,
        mul_nonneg (by linarith : (0:ℝ) ≤ (H.card:ℝ) - 1)
          (by linarith : (0:ℝ) ≤ Real.log ((H.card:ℝ) + 1) - Real.log 2),
        mul_nonneg (by linarith : (0:ℝ) ≤ (H.card:ℝ) - 2)
          (by linarith : (0:ℝ) ≤ Real.log 2 - 0.69)]
    linarith [hhead, htail, harith]

/-- The clause-2 bridge: `exp(-k·lnln x) = (ln x)^{-k}` for `ln x > 0`. -/
theorem exp_neg_card_loglog {x : ℕ} (hx : (0:ℝ) < Real.log x) (k : ℕ) :
    Real.exp (-((k : ℝ) * Real.log (Real.log x))) = (Real.log x ^ k)⁻¹ := by
  rw [← Real.rpow_natCast (Real.log x) k, ← Real.rpow_neg hx.le, Real.rpow_def_of_pos hx]
  ring_nf

/-- T1 CLAUSE 2: clause 1 plus algebra. `M_H(x) = S(H)·x/(ln x)^{|H|}` and
`exp(-|H|·lnln x) = (ln x)^{-|H|}`, so the claim reduces to clause 1 pointwise.
Threshold `x₀ = 3` (only `ln x > 0` is needed). -/
theorem modelMass_ge_exp {x : ℕ} (hx : 3 ≤ x) {H : Finset ℕ} (h0 : 0 ∈ H)
    (hH : IsAdmissible H) :
    (x : ℝ) * Real.exp (-(12 * ((H.card : ℝ) - 1) * Real.log ((H.card : ℝ) + 1))
        - (H.card : ℝ) * Real.log (Real.log x))
      ≤ modelMass H x := by
  have hx1 : (1:ℝ) < (x:ℝ) := by
    have : (3:ℕ) ≤ x := hx
    have : (3:ℝ) ≤ (x:ℝ) := by exact_mod_cast this
    linarith
  have hs : (0:ℝ) < Real.log x := Real.log_pos hx1
  have hspow : (0:ℝ) < Real.log x ^ H.card := by positivity
  have hxnn : (0:ℝ) ≤ (x:ℝ) := by positivity
  have hclause1 := singularSeries_ge_exp h0 hH
  rw [modelMass]
  rw [show (-(12 * ((H.card : ℝ) - 1) * Real.log ((H.card : ℝ) + 1))
      - (H.card : ℝ) * Real.log (Real.log x))
      = (-(12 * ((H.card : ℝ) - 1) * Real.log ((H.card : ℝ) + 1)))
        + (-((H.card : ℝ) * Real.log (Real.log x))) by ring,
    Real.exp_add, exp_neg_card_loglog hs]
  rw [div_eq_mul_inv]
  rw [show (x:ℝ) * (Real.exp (-(12 * ((H.card : ℝ) - 1) * Real.log ((H.card : ℝ) + 1)))
      * (Real.log x ^ H.card)⁻¹)
      = (Real.exp (-(12 * ((H.card : ℝ) - 1) * Real.log ((H.card : ℝ) + 1))) * (x:ℝ))
        * (Real.log x ^ H.card)⁻¹ by ring]
  apply mul_le_mul_of_nonneg_right _ (by positivity)
  exact mul_le_mul_of_nonneg_right hclause1 hxnn

/-! ### The Mertens pack M1-M3: relocated to `Erdos251/Mertens.lean`

Landed here by item-0015 s3, moved out by the ANN-38/ANN-39 refactor: the pack
depends on no `Erdos251` definition, so it lives standalone as an upstream
candidate. `import Erdos251.Mertens` above keeps `primesUpto`,
`mertens_one_upper`, `mertens_second_upper`, `mertens_third_upper` and their
constants (`mertensB`, `mertensC2`, `mertensC3`) visible here unqualified, as
before -- T2 (c) SMALL consumes M3.
-/

end

end Erdos251
