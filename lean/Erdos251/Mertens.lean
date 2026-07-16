import Mathlib

/-!
# The Mertens pack M1-M3 (upper clauses)

STANDALONE, MATHLIB-ONLY. This file depends on no `Erdos251` definition; the
`Erdos251` namespace is its only coupling to the project, and dropping it is
the whole of what an upstream port would change. Relocated verbatim out of
`Counting.lean` (item-0015 s3; ANN-38/ANN-39 sanctioned refactor: moves +
imports only, declaration names unchanged).

Mathlib has NO Mertens theorems at the pin, nor on master (steering-verified
full-tree, ANN-36); this pack is the project's first reusable
analytic-number-theory toolkit beyond `Chebyshev.lean`, and an upstream
candidate.

## Contents

| Declaration            | statement                                            |
|------------------------|------------------------------------------------------|
| `mertens_one_upper`    | `∑_{p ≤ N} (log p)/p ≤ log N + log 4`                |
| `mertens_second_upper` | `∑_{p ≤ P} 1/p ≤ lnln P + c₂`, leading coefficient 1 |
| `mertens_third_upper`  | `∏_{p ≤ P} (1 - 1/p)⁻¹ ≤ c₃ log P`, exponent 1       |

Constants are explicit and symbolic in M1's `b = log 4`
(`mertensB`, `mertensC2`, `mertensC3`); no integrals are used, and
`Mathlib.NumberTheory.AbelSummation` stays unused (M2 runs on the discrete
`Finset.sum_Ico_by_parts`).

## Route history (ANN-37)

The v3 DYADIC route to M2 is RETIRED: on a block `p ∈ (r^j, r^(j+1)]` the
two-sided M1 error `C` enters once per block over `j log r`, and couples to
the divergent harmonic sum over block indices, so it lands in the LEADING
coefficient -- `(1 + C/log r) lnln P` for every fixed ratio `r` (coefficient 4
with the crude primorial input). T2's frozen `log(k+2)^2` budget spends one log
on M3 and one on the span, so M3 needs exponent EXACTLY 1, i.e. M2 leading
coefficient EXACTLY 1.

The route below (kickoff v3.1) is discrete Abel summation
(`Finset.sum_Ico_by_parts`): the same M1 error couples instead to the
telescoping total weight variation `∑ (w i - w (i+1)) = w 2 - w P ≤ 1/log 2`,
which is bounded, so the error stays ADDITIVE and the leading coefficient is
exactly 1. Only M1's UPPER clause is consumed -- the nonnegative weight
differences keep any lower constant out entirely, so no M1-lower (hence no
factorial lower bound) is needed.
-/

namespace Erdos251

noncomputable section

/-- The primes `≤ N`, as a `Finset ℕ` (mathlib's primorial index set). -/
abbrev primesUpto (N : ℕ) : Finset ℕ := (Finset.range (N + 1)).filter Nat.Prime

/-- Chebyshev's factorial factorization, restricted to the primes that
actually occur: `N! = ∏_{p ≤ N} p^{v_p(N!)}`. Primes `p > N` do not divide
`N!`, so they contribute `p^0 = 1`. -/
theorem prod_primesUpto_pow_padicValNat (N : ℕ) :
    ∏ p ∈ primesUpto N, p ^ padicValNat p (Nat.factorial N) = Nat.factorial N := by
  have hfac : Nat.factorial N ≠ 0 := Nat.factorial_ne_zero N
  have hbig := Nat.prod_pow_prime_padicValNat (Nat.factorial N) hfac
    (Nat.factorial N + 1) (by omega)
  have hsub : ∏ p ∈ primesUpto N, p ^ padicValNat p (Nat.factorial N)
      = ∏ p ∈ (Finset.range (Nat.factorial N + 1)).filter Nat.Prime,
          p ^ padicValNat p (Nat.factorial N) := by
    refine Finset.prod_subset ?_ ?_
    · intro p hp
      rw [Finset.mem_filter, Finset.mem_range] at hp ⊢
      exact ⟨by have := Nat.self_le_factorial N; omega, hp.2⟩
    · intro p hp hnot
      rw [Finset.mem_filter, Finset.mem_range] at hp hnot
      have hpp : p.Prime := hp.2
      have hpN : N < p := by
        by_contra hc
        exact hnot ⟨by omega, hpp⟩
      have hnd : ¬ (p ∣ Nat.factorial N) := by
        rw [Nat.Prime.dvd_factorial hpp]; omega
      rw [padicValNat.eq_zero_of_not_dvd hnd, pow_zero]
  rw [hsub, hbig]

/-- Log form: `log N! = ∑_{p ≤ N} v_p(N!) log p`. -/
theorem log_factorial_eq (N : ℕ) :
    Real.log (Nat.factorial N : ℝ)
      = ∑ p ∈ primesUpto N, (padicValNat p (Nat.factorial N) : ℝ) * Real.log p := by
  have h := prod_primesUpto_pow_padicValNat N
  have hcast : ((∏ p ∈ primesUpto N, p ^ padicValNat p (Nat.factorial N) : ℕ) : ℝ)
      = ∏ p ∈ primesUpto N, ((p : ℝ) ^ padicValNat p (Nat.factorial N)) := by
    push_cast; ring
  calc Real.log (Nat.factorial N : ℝ)
      = Real.log ((∏ p ∈ primesUpto N, p ^ padicValNat p (Nat.factorial N) : ℕ) : ℝ) := by
        rw [h]
    _ = Real.log (∏ p ∈ primesUpto N, ((p : ℝ) ^ padicValNat p (Nat.factorial N))) := by
        rw [hcast]
    _ = ∑ p ∈ primesUpto N, Real.log ((p : ℝ) ^ padicValNat p (Nat.factorial N)) := by
        refine Real.log_prod _ _ (fun p hp => ?_)
        rw [Finset.mem_filter] at hp
        have : (0:ℝ) < (p:ℝ) := by exact_mod_cast hp.2.pos
        positivity
    _ = ∑ p ∈ primesUpto N, (padicValNat p (Nat.factorial N) : ℝ) * Real.log p :=
        Finset.sum_congr rfl (fun p _ => by rw [Real.log_pow])

/-- The `i = 1` term of Legendre's formula: `v_p(N!) ≥ ⌊N/p⌋`. -/
theorem padicValNat_factorial_ge_div {p N : ℕ} (hp : p.Prime) (hpN : p ≤ N) :
    N / p ≤ padicValNat p (Nat.factorial N) := by
  haveI : Fact p.Prime := ⟨hp⟩
  rw [padicValNat_factorial (b := Nat.log p N + 1) (by omega)]
  have h1 : (1:ℕ) ∈ Finset.Ico 1 (Nat.log p N + 1) := by
    rw [Finset.mem_Ico]
    exact ⟨le_rfl, by have := Nat.log_pos hp.one_lt hpN; omega⟩
  have := Finset.single_le_sum (f := fun i => N / p ^ i) (fun i _ => Nat.zero_le _) h1
  simpa using this

/-- `∑_{p ≤ N} log p = log N# ≤ N log 4` (ℕ-indexed form, for the Mertens pack). -/
theorem sum_log_primesUpto_le (N : ℕ) :
    ∑ p ∈ primesUpto N, Real.log p ≤ (N : ℝ) * Real.log 4 := by
  have hprod : ∑ p ∈ primesUpto N, Real.log (p : ℝ) = Real.log ((primorial N : ℕ) : ℝ) := by
    rw [primorial]
    push_cast
    rw [Real.log_prod]
    intro p hp
    rw [Finset.mem_filter] at hp
    have : (0:ℝ) < (p:ℝ) := by exact_mod_cast hp.2.pos
    exact ne_of_gt this
  rw [hprod]
  have h4R : ((primorial N : ℕ) : ℝ) ≤ (4:ℝ) ^ N := by exact_mod_cast primorial_le_4_pow N
  calc Real.log ((primorial N : ℕ) : ℝ) ≤ Real.log ((4:ℝ) ^ N) :=
        Real.log_le_log (by exact_mod_cast (primorial_pos N)) h4R
    _ = (N : ℝ) * Real.log 4 := by rw [Real.log_pow]

/-- MERTENS 1 (upper): `∑_{p ≤ N} (log p)/p ≤ log N + log 4`.

Chebyshev's log-factorial identity: `log N! = ∑_{p ≤ N} v_p(N!) log p`
(Legendre, `padicValNat_factorial`), `v_p(N!) ≥ ⌊N/p⌋ > N/p - 1`, and
`N! ≤ N^N`. Rearranged against `∑_{p ≤ N} log p ≤ N log 4`
(`primorial_le_4_pow`). Constant `c₁ = log 4`, explicit. No integrals. -/
theorem mertens_one_upper {N : ℕ} (hN : 1 ≤ N) :
    ∑ p ∈ primesUpto N, Real.log p / p ≤ Real.log N + Real.log 4 := by
  have hNR : (0:ℝ) < (N:ℝ) := by exact_mod_cast hN
  -- pointwise minorant of each Legendre term
  have hpt : ∀ p ∈ primesUpto N,
      ((N:ℝ)/(p:ℝ) - 1) * Real.log p
        ≤ (padicValNat p (Nat.factorial N) : ℝ) * Real.log p := by
    intro p hp
    rw [Finset.mem_filter, Finset.mem_range] at hp
    have hpp : p.Prime := hp.2
    have hpN : p ≤ N := by omega
    have hpR : (0:ℝ) < (p:ℝ) := by exact_mod_cast hpp.pos
    have hlogp : 0 ≤ Real.log p := Real.log_nonneg (by exact_mod_cast hpp.one_lt.le)
    have hdm := Nat.div_add_mod N p
    have hmod : N % p < p := Nat.mod_lt _ hpp.pos
    have hnat : N < p * (N / p) + p := by omega
    have hR : (N:ℝ) < (p:ℝ) * ((N / p : ℕ) : ℝ) + (p:ℝ) := by exact_mod_cast hnat
    have hfloor : (N:ℝ)/(p:ℝ) - 1 ≤ ((N / p : ℕ) : ℝ) := by
      rw [sub_le_iff_le_add, div_le_iff₀ hpR]
      linarith
    have hv : ((N / p : ℕ) : ℝ) ≤ (padicValNat p (Nat.factorial N) : ℝ) := by
      exact_mod_cast padicValNat_factorial_ge_div hpp hpN
    nlinarith [hlogp, hfloor, hv]
  -- assemble the two-sided squeeze on `log N!`
  have hsumeq : ∑ p ∈ primesUpto N, ((N:ℝ)/(p:ℝ) - 1) * Real.log p
      = (N:ℝ) * (∑ p ∈ primesUpto N, Real.log p / p) - ∑ p ∈ primesUpto N, Real.log p := by
    rw [Finset.mul_sum, ← Finset.sum_sub_distrib]
    exact Finset.sum_congr rfl (fun p _ => by ring)
  have hlow : (N:ℝ) * (∑ p ∈ primesUpto N, Real.log p / p) - ∑ p ∈ primesUpto N, Real.log p
      ≤ Real.log (Nat.factorial N : ℝ) := by
    rw [log_factorial_eq N, ← hsumeq]
    exact Finset.sum_le_sum hpt
  have hhigh : Real.log (Nat.factorial N : ℝ) ≤ (N:ℝ) * Real.log N := by
    have h1 : ((Nat.factorial N : ℕ) : ℝ) ≤ ((N:ℝ)) ^ N := by
      exact_mod_cast Nat.factorial_le_pow N
    calc Real.log (Nat.factorial N : ℝ) ≤ Real.log ((N:ℝ) ^ N) :=
          Real.log_le_log (by exact_mod_cast Nat.factorial_pos N) h1
      _ = (N:ℝ) * Real.log N := by rw [Real.log_pow]
  have hprim := sum_log_primesUpto_le N
  -- divide by `N > 0`
  have hkey : (N:ℝ) * (∑ p ∈ primesUpto N, Real.log p / p)
      ≤ (N:ℝ) * (Real.log N + Real.log 4) := by
    have hexp : (N:ℝ) * (Real.log N + Real.log 4)
        = (N:ℝ) * Real.log N + (N:ℝ) * Real.log 4 := by ring
    rw [hexp]
    linarith [hlow, hhigh, hprim]
  exact le_of_mul_le_mul_left hkey hNR

/-- MP-M2 weights `w i = (log i)⁻¹`. Junk values are load-bearing zeros:
`log 0 = log 1 = 0` and `(0:ℝ)⁻¹ = 0`, so `w 0 = w 1 = 0`. -/
def mw (i : ℕ) : ℝ := (Real.log i)⁻¹

/-- MP-M2 summand `g i = log i / i` on primes, `0` off them. -/
def mg (i : ℕ) : ℝ := if Nat.Prime i then Real.log i / i else 0

/-- `G (n+1) = A n = ∑_{p ≤ n} log p / p`: the partial sums of `g` ARE MP-M1's
left-hand side. -/
theorem sum_range_mg (n : ℕ) :
    ∑ i ∈ Finset.range (n + 1), mg i = ∑ p ∈ primesUpto n, Real.log p / p := by
  rw [primesUpto, Finset.sum_filter]
  exact Finset.sum_congr rfl (fun i _ => rfl)

/-- `G 2 = g 0 + g 1 = 0` kills the boundary term of the by-parts identity. -/
theorem sum_range_two_mg : ∑ i ∈ Finset.range 2, mg i = 0 := by
  norm_num [mg, Finset.sum_range_succ, Nat.not_prime_one]

/-- On a prime, `w i * g i = 1/i`; off a prime both sides vanish. -/
theorem mw_mul_mg (i : ℕ) : mw i * mg i = if Nat.Prime i then (1:ℝ) / i else 0 := by
  unfold mw mg
  split_ifs with h
  · have h2 : (2:ℝ) ≤ (i:ℝ) := by exact_mod_cast h.two_le
    have hlog : Real.log i ≠ 0 := ne_of_gt (Real.log_pos (by linarith))
    field_simp
  · ring

/-- Step 0: the target sum in Abel shape. -/
theorem sum_inv_primes_eq {P : ℕ} :
    ∑ p ∈ primesUpto P, (1:ℝ) / p = ∑ i ∈ Finset.Ico 2 (P + 1), mw i * mg i := by
  rw [primesUpto, Finset.sum_filter]
  rw [show (∑ i ∈ Finset.range (P+1), if Nat.Prime i then (1:ℝ)/i else 0)
      = ∑ i ∈ Finset.range (P+1), mw i * mg i from
    Finset.sum_congr rfl (fun i _ => (mw_mul_mg i).symm)]
  refine (Finset.sum_subset ?_ ?_).symm
  · intro i hi
    rw [Finset.mem_Ico] at hi
    rw [Finset.mem_range]
    omega
  · intro i hi hni
    rw [Finset.mem_range] at hi
    rw [Finset.mem_Ico] at hni
    have : i = 0 ∨ i = 1 := by omega
    rcases this with rfl | rfl <;> simp [mw_mul_mg, Nat.not_prime_one]

/-- STEP 1 (IDENT), discrete Abel summation via `Finset.sum_Ico_by_parts`.
Integral-free: `Mathlib.NumberTheory.AbelSummation` stays unused.

  `S(P) = A P / log P + ∑_{i ∈ Ico 2 P} (w i - w (i+1)) * A i` -/
theorem mertens_ident {P : ℕ} (hP : 2 ≤ P) :
    ∑ p ∈ primesUpto P, (1:ℝ) / p
      = mw P * (∑ p ∈ primesUpto P, Real.log p / p)
        + ∑ i ∈ Finset.Ico 2 P, (mw i - mw (i + 1)) * (∑ p ∈ primesUpto i, Real.log p / p) := by
  rw [sum_inv_primes_eq]
  have h := Finset.sum_Ico_by_parts mw mg (m := 2) (n := P + 1) (by omega)
  simp only [smul_eq_mul, Nat.add_sub_cancel] at h
  rw [h, sum_range_two_mg, sum_range_mg P]
  rw [show (∑ i ∈ Finset.Ico 2 P, (mw (i + 1) - mw i) * (∑ j ∈ Finset.range (i + 1), mg j))
      = ∑ i ∈ Finset.Ico 2 P, -((mw i - mw (i + 1)) * (∑ p ∈ primesUpto i, Real.log p / p)) from
    Finset.sum_congr rfl (fun i _ => by rw [sum_range_mg i]; ring)]
  rw [Finset.sum_neg_distrib]
  ring

/-- Generic `Ico` telescope in the `(F i - F (i+1))` orientation
(`Finset.sum_range_sub'` after the `Ico -> range` shift). -/
theorem telescope_Ico_sub' (F : ℕ → ℝ) {m n : ℕ} (h : m ≤ n) :
    ∑ i ∈ Finset.Ico m n, (F i - F (i + 1)) = F m - F n := by
  rw [Finset.sum_Ico_eq_sum_range]
  rw [show (∑ k ∈ Finset.range (n - m), (F (m + k) - F (m + k + 1)))
      = ∑ k ∈ Finset.range (n - m),
          ((fun j => F (m + j)) k - (fun j => F (m + j)) (k + 1)) from
    Finset.sum_congr rfl (fun k _ => by simp only []; rw [← Nat.add_assoc])]
  rw [Finset.sum_range_sub' (fun j => F (m + j))]
  simp only [Nat.add_zero]
  congr 2
  omega

/-- Generic `Ico` telescope in the `(F (i+1) - F i)` orientation. -/
theorem telescope_Ico_sub (F : ℕ → ℝ) {m n : ℕ} (h : m ≤ n) :
    ∑ i ∈ Finset.Ico m n, (F (i + 1) - F i) = F n - F m := by
  have h' := telescope_Ico_sub' F h
  rw [show (∑ i ∈ Finset.Ico m n, (F (i + 1) - F i))
      = -∑ i ∈ Finset.Ico m n, (F i - F (i + 1)) from by
    rw [← Finset.sum_neg_distrib]; exact Finset.sum_congr rfl (fun i _ => by ring)]
  rw [h']; ring

/-- STEP 2: the weights are antitone, so the `A i` coefficients are `≥ 0` --
this is what keeps MP-M1's error ADDITIVE (and its lower clause unused). -/
theorem mw_sub_nonneg {i : ℕ} (hi : 2 ≤ i) : 0 ≤ mw i - mw (i + 1) := by
  have h2 : (2:ℝ) ≤ (i:ℝ) := by exact_mod_cast hi
  have hlogi : 0 < Real.log i := Real.log_pos (by linarith)
  have hle : Real.log (i:ℝ) ≤ Real.log ((i:ℝ) + 1) := Real.log_le_log (by linarith) (by linarith)
  have hinv := inv_anti₀ hlogi hle
  unfold mw
  push_cast
  linarith

/-- STEP 5: the main-term inequality. `log i * (w i - w (i+1)) = 1 - 1/t` with
`t = log(i+1)/log i ≥ 1`, and `log t ≥ 1 - 1/t` (`Real.log_le_sub_one_of_pos`
at `1/t`, then `Real.log_inv`), while `log t` IS the `lnln` increment
(`Real.log_div`). -/
theorem mertens_main_step {i : ℕ} (hi : 2 ≤ i) :
    Real.log i * (mw i - mw (i + 1))
      ≤ Real.log (Real.log ((i:ℝ) + 1)) - Real.log (Real.log (i:ℝ)) := by
  have h2 : (2:ℝ) ≤ (i:ℝ) := by exact_mod_cast hi
  have hlogi : 0 < Real.log (i:ℝ) := Real.log_pos (by linarith)
  have hlogi1 : 0 < Real.log ((i:ℝ) + 1) := Real.log_pos (by linarith)
  have hle : Real.log (i:ℝ) ≤ Real.log ((i:ℝ) + 1) := Real.log_le_log (by linarith) (by linarith)
  set t : ℝ := Real.log ((i:ℝ) + 1) / Real.log (i:ℝ) with ht
  have ht1 : 1 ≤ t := by rw [ht, le_div_iff₀ hlogi]; linarith
  have ht0 : (0:ℝ) < t := by linarith
  have hlogt : 1 - 1/t ≤ Real.log t := by
    have h := Real.log_le_sub_one_of_pos (show (0:ℝ) < t⁻¹ by positivity)
    rw [Real.log_inv] at h
    have hinv : t⁻¹ = 1/t := (one_div t).symm
    rw [hinv] at h
    linarith
  have hlogteq : Real.log t = Real.log (Real.log ((i:ℝ) + 1)) - Real.log (Real.log (i:ℝ)) := by
    rw [ht, Real.log_div (ne_of_gt hlogi1) (ne_of_gt hlogi)]
  have hLHS : Real.log (i:ℝ) * (mw i - mw (i + 1)) = 1 - 1/t := by
    unfold mw
    push_cast
    rw [ht]
    field_simp
    ring
  rw [hLHS, ← hlogteq]
  exact hlogt

/-- MP-M1's upper constant `b`, as landed (`mertens_one_upper`). -/
def mertensB : ℝ := Real.log 4

/-- MP-M2's constant, SYMBOLIC in MP-M1's `b`:
`c₂ = 1 + b/log 2 - lnln 2`. Numerically `≈ 3.3665` (`lnln 2 ≈ -0.3665`). -/
def mertensC2 : ℝ := 1 + mertensB / Real.log 2 - Real.log (Real.log 2)

/-- MERTENS 2 (upper), LEADING COEFFICIENT EXACTLY 1:
`∑_{p ≤ P} 1/p ≤ lnln P + c₂` for `P ≥ 2`.

Discrete Abel summation (kickoff v3.1, ANN-37; the v3 dyadic route is retired
because its per-block MP-M1 error lands in the LEADING coefficient). Here the
same error couples instead to the telescoping total weight variation
`∑ (w i - w (i+1)) = w 2 - w P ≤ 1/log 2`, so it stays ADDITIVE. Only MP-M1's
UPPER clause is consumed: the nonnegative weight differences keep any lower
constant out entirely. Integral-free -- `Mathlib.NumberTheory.AbelSummation`
is unused. -/
theorem mertens_second_upper {P : ℕ} (hP : 2 ≤ P) :
    ∑ p ∈ primesUpto P, (1:ℝ) / p ≤ Real.log (Real.log P) + mertensC2 := by
  have hPR : (2:ℝ) ≤ (P:ℝ) := by exact_mod_cast hP
  have hlogP : 0 < Real.log (P:ℝ) := Real.log_pos (by linarith)
  have hb0 : (0:ℝ) ≤ mertensB := Real.log_nonneg (by norm_num)
  have hA : ∀ i : ℕ, 1 ≤ i → (∑ p ∈ primesUpto i, Real.log p / p) ≤ Real.log i + mertensB :=
    fun i hi => mertens_one_upper hi
  rw [mertens_ident hP]
  -- STEP 3, first term: `w P * A P ≤ 1 + b/log P`
  have hfirst : mw P * (∑ p ∈ primesUpto P, Real.log p / p)
      ≤ 1 + mertensB * (Real.log (P:ℝ))⁻¹ := by
    have hmwP : mw P = (Real.log (P:ℝ))⁻¹ := rfl
    have hmw0 : (0:ℝ) < mw P := by rw [hmwP]; positivity
    calc mw P * (∑ p ∈ primesUpto P, Real.log p / p) ≤ mw P * (Real.log P + mertensB) :=
          mul_le_mul_of_nonneg_left (hA P (by omega)) hmw0.le
      _ = 1 + mertensB * (Real.log (P:ℝ))⁻¹ := by rw [hmwP]; field_simp
  -- STEP 3, sum term: coefficients are `≥ 0`, so insert MP-M1 UPPER termwise
  have hsum : ∑ i ∈ Finset.Ico 2 P, (mw i - mw (i + 1)) * (∑ p ∈ primesUpto i, Real.log p / p)
      ≤ ∑ i ∈ Finset.Ico 2 P, (mw i - mw (i + 1)) * (Real.log i + mertensB) := by
    refine Finset.sum_le_sum (fun i hi => ?_)
    rw [Finset.mem_Ico] at hi
    exact mul_le_mul_of_nonneg_left (hA i (by omega)) (mw_sub_nonneg hi.1)
  have hsplit : ∑ i ∈ Finset.Ico 2 P, (mw i - mw (i + 1)) * (Real.log i + mertensB)
      = (∑ i ∈ Finset.Ico 2 P, Real.log i * (mw i - mw (i + 1)))
        + mertensB * (∑ i ∈ Finset.Ico 2 P, (mw i - mw (i + 1))) := by
    rw [Finset.mul_sum, ← Finset.sum_add_distrib]
    exact Finset.sum_congr rfl (fun i _ => by ring)
  -- STEP 4: the error telescope (exact, P-uniform)
  have htel1 : ∑ i ∈ Finset.Ico 2 P, (mw i - mw (i + 1)) = mw 2 - mw P :=
    telescope_Ico_sub' mw hP
  -- STEP 5: the main-term telescope
  have htel2 : ∑ i ∈ Finset.Ico 2 P, Real.log i * (mw i - mw (i + 1))
      ≤ Real.log (Real.log P) - Real.log (Real.log 2) := by
    calc ∑ i ∈ Finset.Ico 2 P, Real.log i * (mw i - mw (i + 1))
        ≤ ∑ i ∈ Finset.Ico 2 P, ((fun j : ℕ => Real.log (Real.log j)) (i + 1)
            - (fun j : ℕ => Real.log (Real.log j)) i) := by
          refine Finset.sum_le_sum (fun i hi => ?_)
          rw [Finset.mem_Ico] at hi
          have h := mertens_main_step hi.1
          simp only []
          push_cast
          exact h
      _ = Real.log (Real.log P) - Real.log (Real.log 2) := by
          rw [telescope_Ico_sub (fun j : ℕ => Real.log (Real.log j)) hP]
          norm_num
  have hmw2 : mw 2 = (Real.log 2)⁻¹ := by unfold mw; norm_num
  have hmwP : mw P = (Real.log (P:ℝ))⁻¹ := rfl
  have hbdiv : mertensB / Real.log 2 = mertensB * (Real.log 2)⁻¹ := div_eq_mul_inv _ _
  unfold mertensC2
  rw [hsplit] at hsum
  rw [htel1, hmw2, hmwP] at hsum
  rw [hbdiv]
  nlinarith [hfirst, hsum, htel2, hb0]

/-- MP-M3's constant, symbolic. Numerically `exp(4.3665) ≈ 78.8`. -/
def mertensC3 : ℝ := Real.exp (mertensC2 + 1)

/-- The `-log(1-1/p) - 1/p` tail, telescoped: `∑_{p ≤ P} 1/(p(p-1)) ≤ 1`
(compare with `∑_{m ≥ 2} 1/(m(m-1)) = 1`, which telescopes as
`1/(m-1) - 1/m`). -/
theorem sum_tail_le_one {P : ℕ} (hP : 2 ≤ P) :
    ∑ p ∈ primesUpto P, 1 / ((p:ℝ) * ((p:ℝ) - 1)) ≤ 1 := by
  have hsub : primesUpto P ⊆ Finset.Ico 2 (P + 1) := by
    intro p hp
    rw [primesUpto, Finset.mem_filter, Finset.mem_range] at hp
    rw [Finset.mem_Ico]
    exact ⟨hp.2.two_le, hp.1⟩
  have hnn : ∀ i ∈ Finset.Ico 2 (P + 1), i ∉ primesUpto P →
      0 ≤ 1 / ((i:ℝ) * ((i:ℝ) - 1)) := by
    intro i hi _
    rw [Finset.mem_Ico] at hi
    have h2 : (2:ℝ) ≤ (i:ℝ) := by exact_mod_cast hi.1
    have h1 : (0:ℝ) < (i:ℝ) - 1 := by linarith
    positivity
  refine le_trans (Finset.sum_le_sum_of_subset_of_nonneg hsub hnn) ?_
  -- telescope `1/(m(m-1)) = F m - F (m+1)` with `F m = 1/(m-1)`
  have hcong : ∑ i ∈ Finset.Ico 2 (P + 1), 1 / ((i:ℝ) * ((i:ℝ) - 1))
      = ∑ i ∈ Finset.Ico 2 (P + 1),
          ((fun j : ℕ => ((j:ℝ) - 1)⁻¹) i - (fun j : ℕ => ((j:ℝ) - 1)⁻¹) (i + 1)) := by
    refine Finset.sum_congr rfl (fun i hi => ?_)
    rw [Finset.mem_Ico] at hi
    have h2 : (2:ℝ) ≤ (i:ℝ) := by exact_mod_cast hi.1
    have hi0 : (i:ℝ) ≠ 0 := by linarith
    have hi1 : (i:ℝ) - 1 ≠ 0 := by linarith
    simp only []
    push_cast
    rw [show ((i:ℝ) + 1 - 1) = (i:ℝ) by ring]
    field_simp
    ring
  rw [hcong, telescope_Ico_sub' (fun j : ℕ => ((j:ℝ) - 1)⁻¹) (by omega)]
  have hP1 : (1:ℝ) ≤ (P:ℝ) := by
    have : (2:ℝ) ≤ (P:ℝ) := by exact_mod_cast hP
    linarith
  have hPinv : (0:ℝ) ≤ ((P:ℝ))⁻¹ := by positivity
  push_cast
  rw [show ((P:ℝ) + 1 - 1) = (P:ℝ) by ring]
  norm_num

/-- MERTENS 3 (upper), EXPONENT EXACTLY 1 on `log P`:
`∏_{p ≤ P} (1 - 1/p)⁻¹ ≤ c₃ log P` for `P ≥ 2`.

`log` of the product is `∑ -log(1-1/p) ≤ ∑ 1/(p-1) = ∑ 1/p + ∑ 1/(p(p-1))`
via `Real.log_le_sub_one_of_pos`; MP-M2 gives the first sum with coefficient 1
and `sum_tail_le_one` the second. Exponentiating, `exp(lnln P) = log P`, so the
exponent is 1 -- which is exactly what T2's frozen `log(k+2)^2` budget needs
(one log here, one from the span). -/
theorem mertens_third_upper {P : ℕ} (hP : 2 ≤ P) :
    ∏ p ∈ primesUpto P, (1 - 1 / (p:ℝ))⁻¹ ≤ mertensC3 * Real.log P := by
  have hPR : (2:ℝ) ≤ (P:ℝ) := by exact_mod_cast hP
  have hlogP : 0 < Real.log (P:ℝ) := Real.log_pos (by linarith)
  have hfac : ∀ p ∈ primesUpto P, (0:ℝ) < (1 - 1 / (p:ℝ))⁻¹ := by
    intro p hp
    rw [primesUpto, Finset.mem_filter] at hp
    have h2 : (2:ℝ) ≤ (p:ℝ) := by exact_mod_cast hp.2.two_le
    have : (0:ℝ) < 1 - 1 / (p:ℝ) := by rw [sub_pos, div_lt_one (by linarith)]; linarith
    positivity
  have hprodpos : (0:ℝ) < ∏ p ∈ primesUpto P, (1 - 1 / (p:ℝ))⁻¹ := Finset.prod_pos hfac
  -- pointwise: `-log(1-1/p) ≤ 1/p + 1/(p(p-1))`
  have hpt : ∀ p ∈ primesUpto P, Real.log ((1 - 1 / (p:ℝ))⁻¹)
      ≤ 1 / (p:ℝ) + 1 / ((p:ℝ) * ((p:ℝ) - 1)) := by
    intro p hp
    have hp' := hp
    rw [primesUpto, Finset.mem_filter] at hp'
    have h2 : (2:ℝ) ≤ (p:ℝ) := by exact_mod_cast hp'.2.two_le
    have h := Real.log_le_sub_one_of_pos (hfac p hp)
    have heq : (1 - 1 / (p:ℝ))⁻¹ - 1 = 1 / (p:ℝ) + 1 / ((p:ℝ) * ((p:ℝ) - 1)) := by
      have hp0 : (p:ℝ) ≠ 0 := by linarith
      have hp1 : (p:ℝ) - 1 ≠ 0 := by linarith
      field_simp
    linarith [h, heq.le, heq.ge]
  have hkey : Real.log (∏ p ∈ primesUpto P, (1 - 1 / (p:ℝ))⁻¹)
      ≤ Real.log (Real.log P) + mertensC2 + 1 := by
    rw [Real.log_prod _ _ (fun p hp => ne_of_gt (hfac p hp))]
    calc ∑ p ∈ primesUpto P, Real.log ((1 - 1 / (p:ℝ))⁻¹)
        ≤ ∑ p ∈ primesUpto P, (1 / (p:ℝ) + 1 / ((p:ℝ) * ((p:ℝ) - 1))) :=
          Finset.sum_le_sum hpt
      _ = (∑ p ∈ primesUpto P, 1 / (p:ℝ))
            + ∑ p ∈ primesUpto P, 1 / ((p:ℝ) * ((p:ℝ) - 1)) := Finset.sum_add_distrib
      _ ≤ (Real.log (Real.log P) + mertensC2) + 1 :=
          add_le_add (mertens_second_upper hP) (sum_tail_le_one hP)
      _ = Real.log (Real.log P) + mertensC2 + 1 := by ring
  calc ∏ p ∈ primesUpto P, (1 - 1 / (p:ℝ))⁻¹
      = Real.exp (Real.log (∏ p ∈ primesUpto P, (1 - 1 / (p:ℝ))⁻¹)) :=
        (Real.exp_log hprodpos).symm
    _ ≤ Real.exp (Real.log (Real.log P) + mertensC2 + 1) := Real.exp_le_exp.mpr hkey
    _ = mertensC3 * Real.log P := by
        unfold mertensC3
        rw [show Real.log (Real.log (P:ℝ)) + mertensC2 + 1
            = (mertensC2 + 1) + Real.log (Real.log (P:ℝ)) by ring,
          Real.exp_add, Real.exp_log hlogP]

end

end Erdos251
