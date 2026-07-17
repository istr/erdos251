import Mathlib
import Erdos251.Hypotheses
import Erdos251.Mertens
import Erdos251.Counting.Words
import Erdos251.Counting.SingularSeries

/-!
# Lemma 4.2 layer: one-point extensions and the singular-series ratio

Insert algebra (`nuMod_insert`, `log_singularFactor_insert_sub_le`), the
collision-prime machinery of session 4 (`collPrimes`, `bigCollPrimes`, the
squarefree-divisor / omega(d) counting), and the assembled ratio bound
`singularSeries_ratio_le`. The frozen 4.2 statement itself lives in
`Erdos251/Counting/Lemmata.lean`.

RELOCATION ONLY (item-0016). The body below is byte-identical to
`Erdos251/Counting.lean` lines 448-865 at commit
`6683ee0f009baeb5dd6e759f265544e7f91af23d`,
sha256 `c6a3029172a615391b823ec53e8b734c43893c03a9eef12db6fa2600cbaf7745`.
No statement, docstring, proof or name was changed. Provenance, the index
conventions, the traceability table and the module map live in the umbrella
`Erdos251/Counting.lean`.
-/

namespace Erdos251

noncomputable section

/-! ### Proof-layer helpers for Lemma 4.2 (item-0015 s3; not statements)

T2 step (a) of kickoff v3 section 4: the per-prime ratio analysis, which is
4.2's foundation. The remaining steps (b)-(d) -- collision primes are `< span`,
the split at `k+2` (SMALL via MP-M3, LARGE via the squarefree-divisor
expansion), and the assembly -- are session 4's.

The `k = 0` edge flagged "TEST THIS FIRST" by the kickoff is DISCHARGED:
`offsetSpan {0} = 0` (by `decide`), so `oneExtensions {0} = ∅` and the frozen
statement reads `0 ≤ 0` there. The frozen 4.2 is not false at `k = 0`.
-/

/-- T2 step (a), the dichotomy: adding one point moves `ν` by `0` or `1`. -/
theorem nuMod_insert (H : Finset ℕ) (t p : ℕ) :
    nuMod (insert t H) p = nuMod H p ∨ nuMod (insert t H) p = nuMod H p + 1 := by
  unfold nuMod
  rw [Finset.image_insert]
  by_cases h : (t : ZMod p) ∈ H.image (Nat.cast : ℕ → ZMod p)
  · left; rw [Finset.insert_eq_self.mpr h]
  · right; rw [Finset.card_insert_of_not_mem h]

/-- T2 step (a): the per-prime log-ratio of the singular-series factors.
COLLISION (`ν' = ν`) contributes exactly `-log(1-1/p) = log(1 + 1/(p-1))`;
NEW (`ν' = ν+1`) contributes `≤ 0`. The NEW algebra is
`(1-ν/p)(1-1/p) - (1-(ν+1)/p) = ν/p² ≥ 0`. -/
theorem log_singularFactor_insert_sub_le {H : Finset ℕ} {t : ℕ}
    (hins : IsAdmissible (insert t H)) (hH : IsAdmissible H) (ht : t ∉ H) (p : Nat.Primes) :
    Real.log ((1 - (nuMod (insert t H) (p:ℕ) : ℝ) / ((p:ℕ):ℝ)) /
        (1 - 1/((p:ℕ):ℝ)) ^ (insert t H).card)
      - Real.log ((1 - (nuMod H (p:ℕ) : ℝ) / ((p:ℕ):ℝ)) /
        (1 - 1/((p:ℕ):ℝ)) ^ H.card)
      ≤ (if nuMod (insert t H) (p:ℕ) = nuMod H (p:ℕ)
          then -Real.log (1 - 1/((p:ℕ):ℝ)) else 0) := by
  have hp : (p : ℕ).Prime := p.2
  set P : ℝ := ((p : ℕ) : ℝ) with hPdef
  have hP2 : (2:ℝ) ≤ P := by rw [hPdef]; exact_mod_cast hp.two_le
  have hP0 : (0:ℝ) < P := by linarith
  have hcard : (insert t H).card = H.card + 1 := Finset.card_insert_of_not_mem ht
  -- positivity of both numerators (admissibility) and of the common denominator
  have hnum : (0:ℝ) < 1 - (nuMod H (p:ℕ) : ℝ) / P := by
    have h : (nuMod H (p:ℕ) : ℝ) < P := by rw [hPdef]; exact_mod_cast hH _ hp
    rw [sub_pos, div_lt_one hP0]; exact h
  have hnum' : (0:ℝ) < 1 - (nuMod (insert t H) (p:ℕ) : ℝ) / P := by
    have h : (nuMod (insert t H) (p:ℕ) : ℝ) < P := by rw [hPdef]; exact_mod_cast hins _ hp
    rw [sub_pos, div_lt_one hP0]; exact h
  have hden : (0:ℝ) < 1 - 1 / P := by rw [sub_pos, div_lt_one hP0]; linarith
  -- split both logs; the `(1-1/p)` powers collapse to a single factor
  rw [Real.log_div (ne_of_gt hnum') (by positivity), Real.log_div (ne_of_gt hnum) (by positivity),
    Real.log_pow, Real.log_pow, hcard]
  push_cast
  have hkey : Real.log (1 - (nuMod (insert t H) (p:ℕ) : ℝ) / P)
      - ((H.card : ℝ) + 1) * Real.log (1 - 1/P)
      - (Real.log (1 - (nuMod H (p:ℕ) : ℝ) / P) - (H.card : ℝ) * Real.log (1 - 1/P))
      = (Real.log (1 - (nuMod (insert t H) (p:ℕ) : ℝ) / P)
          - Real.log (1 - (nuMod H (p:ℕ) : ℝ) / P)) - Real.log (1 - 1/P) := by ring
  rw [hkey]
  rcases nuMod_insert H t (p:ℕ) with hcoll | hnew
  · -- COLLISION: exact equality
    rw [if_pos hcoll, hcoll]
    simp
  · -- NEW: the ratio is `≤ 1`, i.e. the log-difference is `≤ 0`
    rw [if_neg (by omega)]
    have hnu0 : (0:ℝ) ≤ (nuMod H (p:ℕ) : ℝ) := Nat.cast_nonneg _
    have hstep : (1:ℝ) - (nuMod (insert t H) (p:ℕ) : ℝ) / P
        ≤ (1 - (nuMod H (p:ℕ) : ℝ) / P) * (1 - 1/P) := by
      rw [hnew]
      push_cast
      have hdiff : (1 - (nuMod H (p:ℕ) : ℝ) / P) * (1 - 1/P)
          - (1 - ((nuMod H (p:ℕ) : ℝ) + 1) / P) = (nuMod H (p:ℕ) : ℝ) / P ^ 2 := by
        field_simp
        ring
      have hq : (0:ℝ) ≤ (nuMod H (p:ℕ) : ℝ) / P ^ 2 := by positivity
      linarith [hdiff, hq]
    have hlog := Real.log_le_log hnum' hstep
    rw [Real.log_mul (ne_of_gt hnum) (ne_of_gt hden)] at hlog
    linarith

/-! ### Proof-layer helpers for Lemma 4.2, steps (b)-(d) (item-0015 s4)

T2 (b): a collision prime divides some `t - h`, so it is `≤ D` -- this is what
makes the LARGE range in (c) FINITE. (c): split at `P = 2|H|`; SMALL is a
direct, `t`-independent instantiation of MP-M3 (one `log(k+2)` of the budget),
LARGE is counted by `card_primeFactors_gt_le` applied to `n = ∏_{h ∈ H} |t-h|`
(Euclid: `n`'s prime factors above `P` are exactly `t`'s LARGE collision
primes; `n ≤ D^{|H|}`). (d): sum over `t`, using `#oneExtensions H ≤ D` -- one
`log(k+2)` from SMALL, one from the span, giving the squared log.

Rule-12 error landing (settled BEFORE building, and re-checked in-session on
the ACTUAL frozen span formula, κ ∈ {1, 10, 48}): the LARGE contribution is
`≤ log D / (2 log P) ≤ (2 + log κ / log 4)/2` -- ADDITIVE in the exponent,
κ-dependent, free of `t`, and NON-GROWING in `|H|` (`log_span_le`). No
leading-coefficient coupling of the kind that killed the s3 dyadic route.
-/

/-- T2 (c) LARGE, load-bearing counting lemma. -/
theorem card_primeFactors_gt_le {n P : ℕ} (hn : n ≠ 0) :
    P ^ (n.primeFactors.filter (fun p => P < p)).card ≤ n := by
  set S := n.primeFactors.filter (fun p => P < p) with hS
  have h1 : P ^ S.card ≤ ∏ p ∈ S, p := by
    rw [← Finset.prod_const]
    refine Finset.prod_le_prod' ?_
    intro i hi
    rw [hS, Finset.mem_filter] at hi
    omega
  have h2 : (∏ p ∈ S, p) ∣ ∏ p ∈ n.primeFactors, p :=
    Finset.prod_dvd_prod_of_subset _ _ _ (Finset.filter_subset _ _)
  have h3 : (∏ p ∈ n.primeFactors, p) ∣ n := Nat.prod_primeFactors_dvd n
  exact h1.trans (Nat.le_of_dvd (Nat.pos_of_ne_zero hn) (h2.trans h3))

/-- The arithmetic content of T2 (b): a collision prime for `H ∪ {t}` divides
`t - h` for some `h ∈ H`. This is the `nuMod_insert` case split, read off in
the form both (b) and (c)-LARGE consume. -/
theorem collision_dvd {H : Finset ℕ} {t p : ℕ}
    (hcoll : nuMod (insert t H) p = nuMod H p) :
    ∃ h ∈ H, p ∣ ((t : ℤ) - (h : ℤ)).natAbs := by
  have hmem : (t : ZMod p) ∈ H.image (Nat.cast : ℕ → ZMod p) := by
    by_contra h
    rw [nuMod, Finset.image_insert, Finset.card_insert_of_not_mem h, ← nuMod] at hcoll
    omega
  obtain ⟨h, hhH, hcast⟩ := Finset.mem_image.mp hmem
  refine ⟨h, hhH, ?_⟩
  have hmod : h ≡ t [MOD p] := (ZMod.natCast_eq_natCast_iff _ _ _).mp hcast
  have hdvdZ : (p : ℤ) ∣ (t : ℤ) - (h : ℤ) := Nat.modEq_iff_dvd.mp hmod
  have := Int.natAbs_dvd_natAbs.mpr hdvdZ
  simpa using this

/-- T2 (b): a collision prime divides some `t - h`, hence is at most the span.
This is what makes the LARGE range in (c) finite. -/
theorem collision_prime_le_span {H : Finset ℕ} {t p : ℕ}
    (htH : t ∉ H) (ht : t < offsetSpan H) (hcoll : nuMod (insert t H) p = nuMod H p) :
    p ≤ offsetSpan H := by
  obtain ⟨h, hhH, hdvd⟩ := collision_dvd hcoll
  have hne : ((t : ℤ) - (h : ℤ)).natAbs ≠ 0 := by
    have : t ≠ h := fun e => htH (e ▸ hhH)
    omega
  have hle : ((t : ℤ) - (h : ℤ)).natAbs ≤ offsetSpan H := by
    have hhle : h ≤ offsetSpan H := Finset.le_sup (f := id) hhH
    omega
  exact le_trans (Nat.le_of_dvd (Nat.pos_of_ne_zero hne) hdvd) hle

/-- The collision primes of the extension `H ∪ {t}`: by T2 (b) all of them
lie at or below the span, so this Finset carries the whole log-ratio. -/
def collPrimes (H : Finset ℕ) (t : ℕ) : Finset Nat.Primes :=
  (primesLe (offsetSpan H)).filter (fun p => nuMod (insert t H) (p : ℕ) = nuMod H (p : ℕ))

theorem log_singularSeries_eq {H : Finset ℕ} (hH : IsAdmissible H) :
    Real.log (singularSeries H)
      = ∑' p : Nat.Primes, Real.log ((1 - (nuMod H (p : ℕ) : ℝ) / ((p : ℕ) : ℝ)) /
          (1 - 1 / ((p : ℕ) : ℝ)) ^ H.card) := by
  rw [singularSeries,
    ← Real.rexp_tsum_eq_tprod _ (singularFactor_pos hH) summable_log_singularFactor,
    Real.log_exp]

/-- T2 (b)+(a) combined: the whole log-ratio is carried by the collision primes,
each contributing exactly `-log(1 - 1/p)`; the NEW primes drop out (`≤ 0`). -/
theorem log_ratio_le_sum_collPrimes {H : Finset ℕ} {t : ℕ}
    (hH : IsAdmissible H) (hins : IsAdmissible (insert t H))
    (htH : t ∉ H) (ht : t < offsetSpan H) :
    Real.log (singularSeries (insert t H) / singularSeries H)
      ≤ ∑ p ∈ collPrimes H t, -Real.log (1 - 1 / ((p : ℕ) : ℝ)) := by
  set g : Nat.Primes → ℝ := fun p =>
    if nuMod (insert t H) (p : ℕ) = nuMod H (p : ℕ)
      then -Real.log (1 - 1 / ((p : ℕ) : ℝ)) else 0 with hg
  have hsupp : ∀ p : Nat.Primes, p ∉ collPrimes H t → g p = 0 := by
    intro p hp
    rw [hg]
    by_cases hc : nuMod (insert t H) (p : ℕ) = nuMod H (p : ℕ)
    · exact absurd (Finset.mem_filter.mpr
        ⟨mem_primesLe.mpr (collision_prime_le_span htH ht hc), hc⟩) hp
    · simp [hc]
  have hgsum : Summable g := summable_of_ne_finset_zero hsupp
  have hdiff : Summable (fun p : Nat.Primes =>
      Real.log ((1 - (nuMod (insert t H) (p : ℕ) : ℝ) / ((p : ℕ) : ℝ)) /
          (1 - 1 / ((p : ℕ) : ℝ)) ^ (insert t H).card)
        - Real.log ((1 - (nuMod H (p : ℕ) : ℝ) / ((p : ℕ) : ℝ)) /
          (1 - 1 / ((p : ℕ) : ℝ)) ^ H.card)) :=
    summable_log_singularFactor.sub summable_log_singularFactor
  rw [Real.log_div (ne_of_gt (singularSeries_pos hins)) (ne_of_gt (singularSeries_pos hH)),
    log_singularSeries_eq hins, log_singularSeries_eq hH,
    ← tsum_sub summable_log_singularFactor summable_log_singularFactor]
  calc _ ≤ ∑' p : Nat.Primes, g p :=
        tsum_le_tsum (fun p => log_singularFactor_insert_sub_le hins hH htH p) hdiff hgsum
    _ = ∑ p ∈ collPrimes H t, g p := tsum_eq_sum (fun p hp => hsupp p hp)
    _ = _ := Finset.sum_congr rfl (fun p hp => by
        rw [hg]; exact if_pos (Finset.mem_filter.mp hp).2)

/-- T2 (c) SMALL: bound the collision primes `≤ P` by ALL primes `≤ P` and
apply MP-M3 directly. `t`-independent, worst-case-over-count; contributes
exactly the one `log(k+2)` factor of the target budget. -/
theorem sum_primesLe_neg_log_le {P : ℕ} (hP : 2 ≤ P) :
    ∑ p ∈ primesLe P, -Real.log (1 - 1 / ((p : ℕ) : ℝ))
      ≤ Real.log (mertensC3 * Real.log P) := by
  have hfac : ∀ n ∈ primesUpto P, (0:ℝ) < (1 - 1 / (n : ℝ))⁻¹ := by
    intro n hn
    rw [primesUpto, Finset.mem_filter] at hn
    have h2 : (2:ℝ) ≤ (n : ℝ) := by exact_mod_cast hn.2.two_le
    have : (0:ℝ) < 1 - 1 / (n : ℝ) := by rw [sub_pos, div_lt_one (by linarith)]; linarith
    positivity
  have hprodpos : (0:ℝ) < ∏ n ∈ primesUpto P, (1 - 1 / (n : ℝ))⁻¹ := Finset.prod_pos hfac
  calc ∑ p ∈ primesLe P, -Real.log (1 - 1 / ((p : ℕ) : ℝ))
      = ∑ n ∈ primesUpto P, -Real.log (1 - 1 / (n : ℝ)) :=
        sum_primesLe_eq (fun n => -Real.log (1 - 1 / (n : ℝ)))
    _ = ∑ n ∈ primesUpto P, Real.log ((1 - 1 / (n : ℝ))⁻¹) :=
        Finset.sum_congr rfl (fun n _ => (Real.log_inv _).symm)
    _ = Real.log (∏ n ∈ primesUpto P, (1 - 1 / (n : ℝ))⁻¹) :=
        (Real.log_prod _ _ (fun n hn => ne_of_gt (hfac n hn))).symm
    _ ≤ Real.log (mertensC3 * Real.log P) :=
        Real.log_le_log hprodpos (mertens_third_upper hP)

/-- The LARGE part of the collision primes for `t`: those above the split. -/
def bigCollPrimes (H : Finset ℕ) (t P : ℕ) : Finset Nat.Primes :=
  (collPrimes H t).filter (fun p => ¬ ((p : ℕ) ≤ P))

/-- T2 (c) LARGE, reciprocal sum: every `p > P` has `p - 1 ≥ P`, so each
factor's log is `≤ 1/P`. -/
theorem sum_bigCollPrimes_le {H : Finset ℕ} {t P : ℕ} (hP : 1 ≤ P) :
    ∑ p ∈ bigCollPrimes H t P, -Real.log (1 - 1 / ((p : ℕ) : ℝ))
      ≤ ((bigCollPrimes H t P).card : ℝ) * (1 / (P : ℝ)) := by
  have hPR : (1:ℝ) ≤ (P : ℝ) := by exact_mod_cast hP
  calc ∑ p ∈ bigCollPrimes H t P, -Real.log (1 - 1 / ((p : ℕ) : ℝ))
      ≤ ∑ _p ∈ bigCollPrimes H t P, (1 / (P : ℝ)) := by
        refine Finset.sum_le_sum (fun p hp => ?_)
        rw [bigCollPrimes, Finset.mem_filter] at hp
        have hgt : P < (p : ℕ) := by omega
        have hpR : (P : ℝ) + 1 ≤ ((p : ℕ) : ℝ) := by exact_mod_cast hgt
        have hp2 : (2:ℝ) ≤ ((p : ℕ) : ℝ) := by exact_mod_cast p.2.two_le
        have hden : (0:ℝ) < 1 - 1 / ((p : ℕ) : ℝ) := by
          rw [sub_pos, div_lt_one (by linarith)]; linarith
        have h := Real.log_le_sub_one_of_pos (show (0:ℝ) < (1 - 1 / ((p : ℕ) : ℝ))⁻¹ by positivity)
        rw [Real.log_inv] at h
        have heq : (1 - 1 / ((p : ℕ) : ℝ))⁻¹ - 1 = 1 / (((p : ℕ) : ℝ) - 1) := by
          have h0 : ((p : ℕ) : ℝ) ≠ 0 := by linarith
          have h1 : ((p : ℕ) : ℝ) - 1 ≠ 0 := by linarith
          field_simp
        rw [heq] at h
        have hle : 1 / (((p : ℕ) : ℝ) - 1) ≤ 1 / (P : ℝ) := by
          apply one_div_le_one_div_of_le (by linarith); linarith
        linarith
    _ = _ := by rw [Finset.sum_const, nsmul_eq_mul]

/-- T2 (c) LARGE, the count. Apply `card_primeFactors_gt_le` to
`n = ∏_{h ∈ H} |t - h|`: by Euclid the LARGE collision primes of `t` are
exactly the prime factors of `n` above `P`, and `n ≤ D^{|H|}` since every
factor is `≤ D`. -/
theorem card_bigCollPrimes_pow_le {H : Finset ℕ} {t P : ℕ}
    (htH : t ∉ H) (ht : t < offsetSpan H) (hP : 1 ≤ P) :
    P ^ (bigCollPrimes H t P).card ≤ offsetSpan H ^ H.card := by
  set n : ℕ := ∏ h ∈ H, ((t : ℤ) - (h : ℤ)).natAbs with hn
  have hfacne : ∀ h ∈ H, ((t : ℤ) - (h : ℤ)).natAbs ≠ 0 := by
    intro h hhH
    have : t ≠ h := fun e => htH (e ▸ hhH)
    omega
  have hn0 : n ≠ 0 := Finset.prod_ne_zero_iff.mpr hfacne
  -- the LARGE collision primes sit inside `n`'s prime factors above `P`
  have himg : (bigCollPrimes H t P).image (fun p : Nat.Primes => (p : ℕ))
      ⊆ n.primeFactors.filter (fun p => P < p) := by
    intro m hm
    rw [Finset.mem_image] at hm
    obtain ⟨p, hp, rfl⟩ := hm
    rw [bigCollPrimes, collPrimes, Finset.mem_filter, Finset.mem_filter] at hp
    obtain ⟨⟨_, hc⟩, hgt⟩ := hp
    obtain ⟨h, hhH, hdvd⟩ := collision_dvd hc
    refine Finset.mem_filter.mpr ⟨Nat.mem_primeFactors.mpr ⟨p.2, ?_, hn0⟩, by omega⟩
    exact hdvd.trans (Finset.dvd_prod_of_mem _ hhH)
  have hcard : (bigCollPrimes H t P).card ≤ (n.primeFactors.filter (fun p => P < p)).card := by
    calc (bigCollPrimes H t P).card
        = ((bigCollPrimes H t P).image (fun p : Nat.Primes => (p : ℕ))).card :=
          (Finset.card_image_of_injective _ (fun a b h => Subtype.ext h)).symm
      _ ≤ _ := Finset.card_le_card himg
  -- `n ≤ D^|H|`: every factor is at most the span
  have hnle : n ≤ offsetSpan H ^ H.card := by
    rw [hn, ← Finset.prod_const]
    refine Finset.prod_le_prod' (fun h hhH => ?_)
    have hhle : h ≤ offsetSpan H := Finset.le_sup (f := id) hhH
    omega
  calc P ^ (bigCollPrimes H t P).card ≤ P ^ (n.primeFactors.filter (fun p => P < p)).card :=
        Nat.pow_le_pow_right hP hcard
    _ ≤ n := card_primeFactors_gt_le hn0
    _ ≤ _ := hnle

/-- The κ-constant of T2: `log D ≤ (2 + log κ / log 4) · log P` at the split
`P = 2|H|`. This is where the error LANDS ADDITIVE (rule 12): the bound is
`κ`-dependent but free of `t` and non-growing in `|H|`. -/
theorem log_span_le {H : Finset ℕ} {κ : ℝ} (hκ : 1 ≤ κ) (hk2 : 2 ≤ H.card)
    (hD2 : 2 ≤ offsetSpan H)
    (hspan : (offsetSpan H : ℝ) ≤ κ * ((H.card : ℝ) - 1) * Real.log ((H.card : ℝ) + 1)) :
    Real.log (offsetSpan H) ≤ (2 + Real.log κ / Real.log 4) * Real.log (2 * H.card) := by
  have hk : (2:ℝ) ≤ (H.card : ℝ) := by exact_mod_cast hk2
  have hDR : (2:ℝ) ≤ (offsetSpan H : ℝ) := by exact_mod_cast hD2
  have hlogk1 : 0 < Real.log ((H.card : ℝ) + 1) := Real.log_pos (by linarith)
  have hκ0 : (0:ℝ) < κ := by linarith
  have hlogκ : 0 ≤ Real.log κ := Real.log_nonneg hκ
  have hlog4 : (0:ℝ) < Real.log 4 := Real.log_pos (by norm_num)
  -- `log(2|H|) ≥ log 4`, and it dominates each of the three pieces of `log D`
  have hlogP4 : Real.log 4 ≤ Real.log (2 * (H.card : ℝ)) :=
    Real.log_le_log (by norm_num) (by linarith)
  have hlogPpos : 0 < Real.log (2 * (H.card : ℝ)) := lt_of_lt_of_le hlog4 hlogP4
  -- `log D ≤ log κ + log |H| + log log(|H|+1)`
  have hDle : (offsetSpan H : ℝ) ≤ κ * (H.card : ℝ) * Real.log ((H.card : ℝ) + 1) := by
    nlinarith [hspan, hlogk1.le, hκ0.le]
  have hsplit : Real.log (offsetSpan H)
      ≤ Real.log κ + Real.log (H.card : ℝ) + Real.log (Real.log ((H.card : ℝ) + 1)) := by
    have := Real.log_le_log (by linarith : (0:ℝ) < (offsetSpan H : ℝ)) hDle
    rwa [Real.log_mul (by positivity) (ne_of_gt hlogk1), Real.log_mul (ne_of_gt hκ0)
      (by positivity)] at this
  -- piece 1: `log κ ≤ (log κ / log 4) · log P`
  have h1 : Real.log κ ≤ (Real.log κ / Real.log 4) * Real.log (2 * (H.card : ℝ)) := by
    rw [div_mul_eq_mul_div, le_div_iff₀ hlog4]
    nlinarith [hlogκ, hlogP4]
  -- piece 2: `log |H| ≤ log P`
  have h2 : Real.log (H.card : ℝ) ≤ Real.log (2 * (H.card : ℝ)) := by
    exact Real.log_le_log (by linarith) (by linarith)
  -- piece 3: `log log(|H|+1) ≤ log(|H|+1) ≤ log P`
  have h3 : Real.log (Real.log ((H.card : ℝ) + 1)) ≤ Real.log (2 * (H.card : ℝ)) := by
    have ha : Real.log (Real.log ((H.card : ℝ) + 1)) ≤ Real.log ((H.card : ℝ) + 1) :=
      Real.log_le_log hlogk1
        (by linarith [Real.log_le_sub_one_of_pos (by linarith : (0:ℝ) < (H.card : ℝ) + 1)])
    have hb : Real.log ((H.card : ℝ) + 1) ≤ Real.log (2 * (H.card : ℝ)) :=
      Real.log_le_log (by linarith) (by linarith)
    linarith
  have hexp : (2 + Real.log κ / Real.log 4) * Real.log (2 * (H.card : ℝ))
      = (Real.log κ / Real.log 4) * Real.log (2 * (H.card : ℝ))
        + 2 * Real.log (2 * (H.card : ℝ)) := by ring
  rw [hexp]
  linarith [hsplit, h1, h2, h3]

/-- `log(2|H|) ≤ 2 log(|H|+1)`, since `2|H| ≤ (|H|+1)²`. Converts the split's
natural log scale onto the frozen statement's `log(k+2)`. -/
theorem log_two_card_le {H : Finset ℕ} (hk2 : 2 ≤ H.card) :
    Real.log (2 * (H.card : ℝ)) ≤ 2 * Real.log ((H.card : ℝ) + 1) := by
  have hk : (2:ℝ) ≤ (H.card : ℝ) := by exact_mod_cast hk2
  rw [show (2:ℝ) * Real.log ((H.card : ℝ) + 1) = Real.log (((H.card : ℝ) + 1) ^ 2) by
    rw [Real.log_pow]; push_cast; ring]
  exact Real.log_le_log (by linarith) (by nlinarith)

/-- T2 (c)+(d), per `t`: SMALL × LARGE. Both factors are `t`-INDEPENDENT --
SMALL is a worst-case-over-count instantiation of MP-M3, LARGE is bounded by
the κ-constant. -/
theorem singularSeries_ratio_le {H : Finset ℕ} {t : ℕ} {κ : ℝ} (hκ : 1 ≤ κ)
    (hH : IsAdmissible H) (hk2 : 2 ≤ H.card)
    (hspan : (offsetSpan H : ℝ) ≤ κ * ((H.card : ℝ) - 1) * Real.log ((H.card : ℝ) + 1))
    (ht : t ∈ oneExtensions H) :
    singularSeries (insert t H) / singularSeries H
      ≤ mertensC3 * Real.log (2 * (H.card : ℝ))
          * Real.exp ((2 + Real.log κ / Real.log 4) / 2) := by
  classical
  rw [oneExtensions, Finset.mem_filter, Finset.mem_range] at ht
  obtain ⟨htD, _, ht0, htH, hins⟩ := ht
  set P : ℕ := 2 * H.card with hPdef
  set A : ℝ := 2 + Real.log κ / Real.log 4 with hA
  have hk : (2:ℝ) ≤ (H.card : ℝ) := by exact_mod_cast hk2
  have hD2 : 2 ≤ offsetSpan H := by omega
  have hP1 : 1 ≤ P := by omega
  have h2k : ((P : ℕ) : ℝ) = 2 * (H.card : ℝ) := by rw [hPdef]; push_cast; ring
  rw [← h2k]
  have hlog4 : (0:ℝ) < Real.log 4 := Real.log_pos (by norm_num)
  have hlogP4 : Real.log 4 ≤ Real.log ((P : ℕ) : ℝ) := by
    rw [h2k]; exact Real.log_le_log (by norm_num) (by linarith)
  have hlogPpos : 0 < Real.log ((P : ℕ) : ℝ) := lt_of_lt_of_le hlog4 hlogP4
  have hA0 : 0 ≤ A := by
    have : 0 ≤ Real.log κ / Real.log 4 := div_nonneg (Real.log_nonneg hκ) hlog4.le
    rw [hA]; linarith
  -- LARGE: the count, from `P^card ≤ D^|H|` and `log D ≤ A log P`
  have hcount : ((bigCollPrimes H t P).card : ℝ) ≤ (H.card : ℝ) * A := by
    have hpow := card_bigCollPrimes_pow_le htH htD hP1
    have hpowR : ((P : ℝ)) ^ (bigCollPrimes H t P).card ≤ ((offsetSpan H : ℝ)) ^ H.card := by
      exact_mod_cast hpow
    have hPpos : (0:ℝ) < (P : ℝ) := by rw [h2k]; linarith
    have hlog := Real.log_le_log (by positivity) hpowR
    rw [Real.log_pow, Real.log_pow] at hlog
    have hlogD := log_span_le hκ hk2 hD2 hspan
    rw [← h2k, ← hA] at hlogD
    have : ((bigCollPrimes H t P).card : ℝ) * Real.log ((P : ℕ) : ℝ)
        ≤ (H.card : ℝ) * A * Real.log ((P : ℕ) : ℝ) := by
      calc ((bigCollPrimes H t P).card : ℝ) * Real.log ((P : ℕ) : ℝ)
          ≤ (H.card : ℝ) * Real.log (offsetSpan H : ℝ) := hlog
        _ ≤ (H.card : ℝ) * (A * Real.log ((P : ℕ) : ℝ)) := by
            apply mul_le_mul_of_nonneg_left hlogD (by linarith)
        _ = _ := by ring
    exact le_of_mul_le_mul_right (by linarith) hlogPpos
  -- LARGE: the reciprocal sum, `≤ card / P ≤ A / 2`
  have hbig : ∑ p ∈ bigCollPrimes H t P, -Real.log (1 - 1 / ((p : ℕ) : ℝ)) ≤ A / 2 := by
    refine le_trans (sum_bigCollPrimes_le hP1) ?_
    rw [h2k, mul_one_div, div_le_div_iff₀ (by linarith) (by norm_num : (0:ℝ) < 2)]
    nlinarith [hcount, hk]
  -- SMALL: all collision primes `≤ P`, bounded by ALL primes `≤ P`, via MP-M3
  have hsmall : ∑ p ∈ (collPrimes H t).filter (fun p : Nat.Primes => (p : ℕ) ≤ P),
      -Real.log (1 - 1 / ((p : ℕ) : ℝ)) ≤ Real.log (mertensC3 * Real.log P) := by
    refine le_trans (Finset.sum_le_sum_of_subset_of_nonneg ?_ ?_)
      (sum_primesLe_neg_log_le (P := P) (by omega))
    · intro p hp
      rw [Finset.mem_filter] at hp
      exact mem_primesLe.mpr hp.2
    · intro p _ _
      have hp2 : (2:ℝ) ≤ ((p : ℕ) : ℝ) := by exact_mod_cast p.2.two_le
      have hden : (0:ℝ) < 1 - 1 / ((p : ℕ) : ℝ) := by
        rw [sub_pos, div_lt_one (by linarith)]; linarith
      have : Real.log (1 - 1 / ((p : ℕ) : ℝ)) ≤ 0 :=
        Real.log_nonpos hden.le (by rw [sub_le_self_iff]; positivity)
      linarith
  -- assemble the per-`t` bound and exponentiate
  have hC3 : (0:ℝ) < mertensC3 := Real.exp_pos _
  have hMpos : (0:ℝ) < mertensC3 * Real.log ((P : ℕ) : ℝ) := by positivity
  have hlogratio : Real.log (singularSeries (insert t H) / singularSeries H)
      ≤ Real.log (mertensC3 * Real.log ((P : ℕ) : ℝ)) + A / 2 := by
    refine le_trans (log_ratio_le_sum_collPrimes hH hins htH htD) ?_
    rw [← Finset.sum_filter_add_sum_filter_not (collPrimes H t) (fun p : Nat.Primes => (p : ℕ) ≤ P)]
    exact add_le_add hsmall hbig
  have hratio0 : (0:ℝ) < singularSeries (insert t H) / singularSeries H :=
    div_pos (singularSeries_pos hins) (singularSeries_pos hH)
  calc singularSeries (insert t H) / singularSeries H
      = Real.exp (Real.log (singularSeries (insert t H) / singularSeries H)) :=
        (Real.exp_log hratio0).symm
    _ ≤ Real.exp (Real.log (mertensC3 * Real.log ((P : ℕ) : ℝ)) + A / 2) :=
        Real.exp_le_exp.mpr hlogratio
    _ = mertensC3 * Real.log ((P : ℕ) : ℝ) * Real.exp (A / 2) := by
        rw [Real.exp_add, Real.exp_log hMpos]

end

end Erdos251
