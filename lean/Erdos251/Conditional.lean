import Erdos251.Statement
import Erdos251.ForkMerge
import Erdos251.Hypotheses
import Erdos251.Counting

/-!
# Conditional target (chain-v1 THEOREM; counting, construction, assembly)

Replaces the round-0 placeholder file (`HypUniformTuples : Prop := True`
with `erdos_251_of_uniform_tuples`) -- item-0002: no `True` stubs.

`fork_merge_of_hypotheses` is the analytic heart (chain-v1 counting layer
4.1-4.4, deletion construction section 5, assembly section 6). The final
theorem is a genuine proof term over the two sorried layers, so the
top-level factorization
  `HLQuantA → CramerGranville → SmallTailForkMerge → Irrational`
is machine-checked already at the statement level.
-/

namespace Erdos251

/-! ### Proof-layer helpers for section 6 (item-0015 s6; not statements)

The assembly's three missing ingredients. Everything else it consumes is
already proved in `Counting.lean` (sections 4-5) and `ForkMerge.lean`
(section 3); these live here so `Counting.lean` stays untouched. -/

noncomputable section

open Filter

/-- `gamma = q_{i_0+1} - q_{i_0}` is even: both section-5 primes exceed
`L + 3 ≥ 3`, hence both are odd, and a difference of odds is even. -/
theorem cgamma_even (J K : ℕ) : Even (cgamma J K) := by
  have hodd : ∀ j, Odd (cprime (cL J K) j) := by
    intro j
    have hp : (cprime (cL J K) j).Prime := q_prime _
    have hgt := cprime_gt (cL J K) j
    exact hp.odd_of_ne_two (by omega)
  unfold cgamma
  exact Nat.Odd.sub_odd (hodd _) (hodd _)

/-- `2 ≤ gamma`: the enumeration is strictly monotone, so `gamma ≥ 1`, and
an even number `≥ 1` is `≥ 2`. -/
theorem two_le_cgamma (J K : ℕ) : 2 ≤ cgamma J K := by
  have hlt : cprime (cL J K) (cI J) < cprime (cL J K) (cI J + 1) :=
    cprime_lt_cprime _ (by omega)
  have h1 : 1 ≤ cgamma J K := by unfold cgamma; omega
  obtain ⟨k, hk⟩ := cgamma_even J K
  omega

/-- The prime-count below `√x` is unbounded along `x : ℕ`: `Nat.sqrt` and
`Nat.count` are both monotone, and at `x := (q B)^2` the count reaches
`B + 1` (`Nat.count_succ` at the prime `q B`, plus the count/nth bridge).
Supplies the eventual threshold (F5) and FM-3. -/
theorem tendsto_count_sqrt :
    Tendsto (fun x : ℕ => Nat.count Nat.Prime (Nat.sqrt x + 1)) atTop atTop := by
  refine tendsto_atTop_atTop_of_monotone ?_ ?_
  · intro a b hab
    exact Nat.count_monotone _ (by have := Nat.sqrt_le_sqrt hab; omega)
  · intro B
    refine ⟨q B * q B, ?_⟩
    have hc : Nat.count Nat.Prime (q B) = B := by
      simpa [q] using Nat.count_nth_of_infinite Nat.infinite_setOf_prime B
    rw [Nat.sqrt_eq, Nat.count_succ, if_pos (q_prime B), hc]
    omega

/-- An anchor whose prime exceeds `√x` has index at least
`count Prime (Nat.sqrt x + 1)`: the real bound casts down to
`Nat.sqrt x < q idx`, and `count` is monotone with `count (q idx) = idx`.
Used for both the `n₁`-threshold of the tail chain and FM-3. -/
theorem count_sqrt_le_of_anchor {x idx : ℕ} (h : Real.sqrt x < (q idx : ℝ)) :
    Nat.count Nat.Prime (Nat.sqrt x + 1) ≤ idx := by
  have hnat : Nat.sqrt x < q idx := by
    exact_mod_cast lt_of_le_of_lt Real.nat_sqrt_le_real_sqrt h
  have hc : Nat.count Nat.Prime (q idx) = idx := by
    simpa [q] using Nat.count_nth_of_infinite Nat.infinite_setOf_prime idx
  rw [← hc]
  exact Nat.count_monotone _ (by omega)

/-- FM-1, the one constant chain of section 6 (the rule-12 exposure):
`delta(anchor + L) ≤ 3 Cg (ln q(anchor + L - 1))²` (4.4) `≤ 3 Cg (L ln 2 + ln x)²`
(`q_add_le_two_pow`, `q idx ≤ x`) `≤ 3 Cg ((23/20) ln x)² = (1587/400) Cg (ln x)²
< 4 Cg (ln x)² = tailBudget ≤ 2^K` (cbudget). `3 (23/20)² = 3.9675 < 4` is the
margin 4.4's factor `3` (vs `4`) was designed to buy. The index stays
ℕ-subtraction-free via `nu := idx + (J + 1 + K)`, so the tail index is `nu + 1`. -/
theorem ctail_le {Cg : ℝ} (hCg : (1:ℝ) ≤ Cg) {n₁ : ℕ}
    (hdelta : ∀ n : ℕ, n₁ ≤ n → delta (n + 1) ≤ 3 * Cg * Real.log (q n) ^ 2)
    {x idx J K : ℕ} (hidx : n₁ ≤ idx) (hqx : q idx ≤ x)
    (hL1 : ((cL J K : ℝ) + 1 < 3 * Real.log (Real.log x)))
    (hF3 : 20 * Real.log (Real.log x) ≤ Real.log x)
    (hF4 : (1:ℝ) ≤ Real.log (Real.log x))
    (hbud : tailBudget Cg x ≤ 2 ^ K) :
    delta (idx + J + 2 + K) ≤ 2 ^ K := by
  have he : idx + J + 2 + K = (idx + (J + 1 + K)) + 1 := by omega
  rw [he]
  refine le_trans (hdelta _ (by omega)) ?_
  -- `ln x ≥ 20` (from F3/F4), hence `x ≥ 1` and the logs behave
  have hlogx : (20:ℝ) ≤ Real.log x := by linarith
  have hx1 : (1:ℝ) ≤ (x:ℝ) := by
    by_contra h
    push_neg at h
    have := Real.log_nonpos (by positivity) h.le
    linarith
  have hxpos : (0:ℝ) < (x:ℝ) := by linarith
  -- Bertrand: `q (idx + (J+1+K)) ≤ 2^(J+1+K) * q idx ≤ 2^(J+1+K) * x`
  have hq : (q (idx + (J + 1 + K)) : ℝ) ≤ 2 ^ (J + 1 + K) * (x:ℝ) := by
    have h1 : q (idx + (J + 1 + K)) ≤ 2 ^ (J + 1 + K) * q idx := q_add_le_two_pow _ _
    calc (q (idx + (J + 1 + K)) : ℝ) ≤ ((2 ^ (J + 1 + K) * q idx : ℕ) : ℝ) := by exact_mod_cast h1
      _ ≤ ((2 ^ (J + 1 + K) * x : ℕ) : ℝ) := by
          exact_mod_cast Nat.mul_le_mul_left _ hqx
      _ = 2 ^ (J + 1 + K) * (x:ℝ) := by push_cast; ring
  have hlog2 : Real.log 2 ≤ 1 := by have := Real.log_two_lt_d9; linarith
  have hlogq : Real.log (q (idx + (J + 1 + K))) ≤ ((J:ℝ) + 1 + K) + Real.log x := by
    have hpos : (0:ℝ) < (q (idx + (J + 1 + K)) : ℝ) := by exact_mod_cast (q_prime _).pos
    refine le_trans (Real.log_le_log hpos hq) ?_
    rw [Real.log_mul (by positivity) (by linarith), Real.log_pow]
    have hJK : (0:ℝ) ≤ (J:ℝ) + 1 + K := by positivity
    have : ((J + 1 + K : ℕ) : ℝ) * Real.log 2 ≤ ((J:ℝ) + 1 + K) := by
      push_cast
      nlinarith [Real.log_nonneg (by norm_num : (1:ℝ) ≤ 2)]
    push_cast at this ⊢
    linarith
  -- `L + 1 < 3 lnln x` (cbudget clause 4) and `20 lnln x ≤ ln x` (F3) give `(23/20) ln x`
  have hcL : ((cL J K : ℕ) : ℝ) = (J:ℝ) + 2 + K := by unfold cL; push_cast; ring
  rw [hcL] at hL1
  have hlogq2 : Real.log (q (idx + (J + 1 + K))) ≤ (23/20) * Real.log x := by linarith
  have hlogq_nn : (0:ℝ) ≤ Real.log (q (idx + (J + 1 + K))) := by
    refine Real.log_nonneg ?_
    have h2 : (2:ℝ) ≤ (q (idx + (J + 1 + K)) : ℝ) := by
      exact_mod_cast (q_prime (idx + (J + 1 + K))).two_le
    linarith
  have hsq : Real.log (q (idx + (J + 1 + K))) ^ 2 ≤ ((23/20) * Real.log x) ^ 2 :=
    pow_le_pow_left₀ hlogq_nn hlogq2 2
  have hchain : 3 * Cg * Real.log (q (idx + (J + 1 + K))) ^ 2 ≤ tailBudget Cg x := by
    unfold tailBudget
    nlinarith [hsq, hCg, sq_nonneg (Real.log x)]
  linarith [hchain, hbud]

end

open Filter in
/-- Chain-v1 sections 4-6: Hypotheses A and B produce a fork-merge
sequence (Bonferroni transfer 4.3, deletion construction 5, tail bound
4.4 from B, assembly 6). -/
theorem fork_merge_of_hypotheses (hA : HLQuantA) (hB : CramerGranville) :
    SmallTailForkMerge := by
  classical
  -- Setup: normalise Hypothesis B's constant to `Cg = max C 1 ≥ 1`
  obtain ⟨C, n0, hgap⟩ := hB
  set Cg : ℝ := max C 1 with hCgdef
  have hCg : (1:ℝ) ≤ Cg := le_max_right _ _
  have hgap' : ∀ n : ℕ, n0 ≤ n → (gap n : ℝ) ≤ Cg * Real.log (q n) ^ 2 := by
    intro n hn
    have hC : C ≤ Cg := le_max_left _ _
    nlinarith [hgap n hn, sq_nonneg (Real.log (q n))]
  obtain ⟨x1, hcons⟩ := constr_consCount_pos hA hCg
  obtain ⟨n1, hdelta⟩ := delta_le_of_gap_bound (Cg := Cg) hgap'
  obtain ⟨x2, hbudget⟩ := cbudget hCg
  -- The eventual basket (F1)-(F5), extracted once
  have hbasket : ∀ᶠ x : ℕ in atTop,
      x1 ≤ x ∧ x2 ≤ x ∧ 20 * Real.log (Real.log x) ≤ Real.log x ∧
        (1:ℝ) ≤ Real.log (Real.log x) ∧ n1 ≤ Nat.count Nat.Prime (Nat.sqrt x + 1) := by
    have hF3 : ∀ᶠ x : ℕ in atTop, 20 * Real.log (Real.log x) ≤ Real.log x := by
      filter_upwards [eventually_pow_loglog_le 1 20 (show (0:ℝ) < 1 by norm_num)] with x hx
      simpa using hx
    have hF4 : ∀ᶠ x : ℕ in atTop, (1:ℝ) ≤ Real.log (Real.log x) :=
      (Real.tendsto_log_atTop.comp
        (Real.tendsto_log_atTop.comp tendsto_natCast_atTop_atTop)).eventually_ge_atTop 1
    filter_upwards [eventually_ge_atTop x1, eventually_ge_atTop x2, hF3, hF4,
      tendsto_count_sqrt.eventually_ge_atTop n1] with x h1 h2 h3 h4 h5
    exact ⟨h1, h2, h3, h4, h5⟩
  rw [eventually_atTop] at hbasket
  obtain ⟨X, hX⟩ := hbasket
  have hrun : Tendsto (fun r : ℕ => X + r) atTop atTop :=
    tendsto_atTop_mono (fun r => Nat.le_add_left r X) tendsto_id
  -- Witnesses: `consCount ≥ 1` turns into an anchor index for each word
  have hwit : ∀ r : ℕ, ∃ a b : ℕ,
      (IsConsecRealization (cword (cJ Cg (X + r)) (cK Cg (X + r)))
          (cL (cJ Cg (X + r)) (cK Cg (X + r))) a ∧
        Real.sqrt ((X + r : ℕ) : ℝ) < (q a : ℝ) ∧ q a ≤ X + r) ∧
      (IsConsecRealization (cword' (cJ Cg (X + r)) (cK Cg (X + r)))
          (cL (cJ Cg (X + r)) (cK Cg (X + r))) b ∧
        Real.sqrt ((X + r : ℕ) : ℝ) < (q b : ℝ) ∧ q b ≤ X + r) := by
    intro r
    obtain ⟨hF1, -, -, -, -⟩ := hX (X + r) (by omega)
    obtain ⟨hpos, hpos'⟩ := hcons (X + r) hF1
    have hex : ∀ (w : ℕ → ℕ) (L : ℕ), 1 ≤ consCount w L (X + r) →
        ∃ c : ℕ, IsConsecRealization w L c ∧
          Real.sqrt ((X + r : ℕ) : ℝ) < (q c : ℝ) ∧ q c ≤ X + r := by
      intro w L h
      unfold consCount at h
      obtain ⟨c, hc⟩ := Finset.card_pos.mp h
      rw [Finset.mem_filter] at hc
      exact ⟨c, hc.2⟩
    obtain ⟨a, ha⟩ := hex _ _ hpos
    obtain ⟨b, hb⟩ := hex _ _ hpos'
    exact ⟨a, b, ha, hb⟩
  choose a b ha hb using hwit
  -- THE NAME SWAP (chain-v1 section 6): `n_FM := b` (the `w'`-anchor),
  -- `m_FM := a` (the `w`-anchor). `cword_fork` is stated in the natural
  -- order `(w, w')`; this binding is what turns it into FM-F's `(+γ, -γ)`.
  refine ⟨fun r => b r, fun r => a r, fun r => cJ Cg (X + r), fun r => cK Cg (X + r),
    fun r => cgamma (cJ Cg (X + r)) (cK Cg (X + r)), ?_, ?_, ?_⟩
  · intro r
    show ForkMergeAt (b r) (a r) (cJ Cg (X + r)) (cK Cg (X + r))
      (cgamma (cJ Cg (X + r)) (cK Cg (X + r)))
    obtain ⟨hF1, hF2, hF3, hF4, hF5⟩ := hX (X + r) (by omega)
    obtain ⟨hJ, hK, hbud3, hbud4, -, -, -, -⟩ := hbudget (X + r) hF2
    obtain ⟨hra, hqa_lo, hqa_hi⟩ := ha r
    obtain ⟨hrb, hqb_lo, hqb_hi⟩ := hb r
    set J := cJ Cg (X + r) with hJdef
    set K := cK Cg (X + r) with hKdef
    -- `cL J K` is by definition `J + 2 + K`; phrasing the realizations that way
    -- keeps every word-position side-goal pure linear arithmetic.
    have hgapa : ∀ i, i < J + 2 + K → gap (a r + i) = cword J K i := fun i hi =>
      hra i (Finset.mem_range.mpr hi)
    have hgapb : ∀ i, i < J + 2 + K → gap (b r + i) = cword' J K i := fun i hi =>
      hrb i (Finset.mem_range.mpr hi)
    -- the `n₁`-thresholds for the two tails, via the anchor/count bridge
    have hn1a : n1 ≤ a r := le_trans hF5 (count_sqrt_le_of_anchor hqa_lo)
    have hn1b : n1 ≤ b r := le_trans hF5 (count_sqrt_le_of_anchor hqb_lo)
    refine ⟨hJ, hK, two_le_cgamma _ _, cgamma_even _ _, ?_, ?_, ?_, ?_, ?_, ?_⟩
    · -- block_prefix: shared length-`J` prefix (cword_prefix)
      intro i hi
      rw [hgapb i (by omega), hgapa i (by omega), cword_prefix J K hJ hK i hi]
    · -- fork_up: `cword J K J + γ = cword' J K J`, read right-to-left
      rw [hgapb J (by omega), hgapa J (by omega)]
      exact ((cword_fork J K hJ hK).1).symm
    · -- fork_down: `cword J K (J+1) = cword' J K (J+1) + γ`
      show gap (b r + (J + 1)) + cgamma J K = gap (a r + (J + 1))
      rw [hgapb (J + 1) (by omega), hgapa (J + 1) (by omega)]
      exact ((cword_fork J K hJ hK).2).symm
    · -- block_suffix: shared length-`K` suffix at word positions `J+2, ..., L-1`
      intro i hi
      rw [show b r + J + 2 + i = b r + (J + 2 + i) from by omega,
        show a r + J + 2 + i = a r + (J + 2 + i) from by omega,
        hgapb (J + 2 + i) (by omega), hgapa (J + 2 + i) (by omega),
        cword_suffix J K hJ hK i hi]
    · -- tail_n (FM-1 at the `w'`-anchor)
      exact ctail_le hCg hdelta hn1b hqb_hi hbud4 hF3 hF4 hbud3
    · -- tail_m (FM-1 at the `w`-anchor)
      exact ctail_le hCg hdelta hn1a hqa_hi hbud4 hF3 hF4 hbud3
  · -- FM-2: `(γ + 4)/2^J → 0`, the section-5(iii) limit along the run
    exact (cfm2_tendsto hCg).comp hrun
  · -- FM-3: both anchors exceed `√x_r`, so `min` is squeezed by `tendsto_count_sqrt`
    refine tendsto_atTop_mono (fun r => ?_) (tendsto_count_sqrt.comp hrun)
    exact le_min (count_sqrt_le_of_anchor (hb r).2.1) (count_sqrt_le_of_anchor (ha r).2.1)

/-- Chain-v1 THEOREM on the 0-indexed sum (the Erdos #251 target
expression of `Statement.lean`): Hypotheses A and B imply irrationality. -/
theorem erdos_251_conditional (hA : HLQuantA) (hB : CramerGranville) :
    Irrational (∑' n : ℕ, (Nat.nth Nat.Prime n : ℝ) / 2 ^ n) :=
  erdos_251_of_small_tail_fork_merge (fork_merge_of_hypotheses hA hB)

end Erdos251
