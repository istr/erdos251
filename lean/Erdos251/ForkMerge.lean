import Erdos251.Basic

/-!
# Fork-merge layer (chain-v1 section 3)

`ForkMergeAt` is chain-v1 Definition 3.1 -- the FABLE fork-merge with a
two-step `(+γ, -γ)` fork and exact re-merge -- NOT the single-fork variant
of gpt-iso template 9.5. Statement-level deviations from chain-v1 3.1,
both flagged pre-sign-off (ledger ANN-12):
* the ordering `n_r < m_r` is DROPPED: chain-v1 section 6 swaps names to
  match the fork orientation, which can invert the order, and the proof of
  Theorem 3.2 never uses it (`n ≠ m` is already implied by `2 ≤ γ` with
  `fork_up`).
* template field names `prefix`/`suffix` are Lean keywords; renamed to
  `block_prefix`/`block_suffix`.
Gap indices are Lean-0-indexed (paper `g_{n+i}, 1 ≤ i ≤ J` becomes
`SameBlock n m J`); `delta` indices carry over unchanged.
-/

namespace Erdos251

open Filter

/-- One fork-merge configuration (chain-v1 Definition 3.1: FM-P, FM-F,
FM-S, FM-1). -/
structure ForkMergeAt (n m J K γ : ℕ) : Prop where
  one_le_J : 1 ≤ J
  one_le_K : 1 ≤ K
  two_le_gamma : 2 ≤ γ
  even_gamma : Even γ
  block_prefix : SameBlock n m J
  fork_up : gap (n + J) = gap (m + J) + γ
  fork_down : gap (n + J + 1) + γ = gap (m + J + 1)
  block_suffix : SameBlock (n + J + 2) (m + J + 2) K
  tail_n : delta (n + J + 2 + K) ≤ 2 ^ K
  tail_m : delta (m + J + 2 + K) ≤ 2 ^ K

/-- Chain-v1 Definition 3.1 (FM), full form: a sequence of configurations
with `(γ_r + 4)/2^(J_r) → 0` (FM-2) and `min (n_r, m_r) → ∞` (FM-3). -/
def SmallTailForkMerge : Prop :=
  ∃ n m J K γ : ℕ → ℕ,
    (∀ r, ForkMergeAt (n r) (m r) (J r) (K r) (γ r)) ∧
    Tendsto (fun r => ((γ r : ℝ) + 4) / 2 ^ (J r)) atTop (nhds 0) ∧
    Tendsto (fun r => min (n r) (m r)) atTop atTop

/-- Chain-v1 Theorem 3.2, finite core (proof steps 1-5): ONE configuration
whose base points sit on the even lattice, with `b (γ + 4) < 2^(J+3)`, is
contradictory. Oddness of `b` is not needed here; it lives in producing
the lattice hypotheses (`rational_delta_eventually_lattice`). -/
theorem fork_merge_contradiction {b n m J K γ : ℕ} (hb : 0 < b)
    (hlat_n : ∃ zn : ℤ, (b : ℝ) * delta n = 2 * (zn : ℝ))
    (hlat_m : ∃ zm : ℤ, (b : ℝ) * delta m = 2 * (zm : ℝ))
    (hfm : ForkMergeAt n m J K γ)
    (hsmall : (b : ℝ) * ((γ : ℝ) + 4) < 2 ^ (J + 3)) : False := by
  obtain ⟨hJ, hK, hγ2, hγeven, hpre, hup, hdown, hsuf, htn, htm⟩ := hfm
  have hbpos : (0 : ℝ) < b := by exact_mod_cast hb
  have hγ : (2 : ℝ) ≤ (γ : ℝ) := by exact_mod_cast hγ2
  have h2Kpos : (0 : ℝ) < 2 ^ K := by positivity
  set Dend : ℝ := delta (n + J + 2 + K) - delta (m + J + 2 + K) with hDend
  -- Step 1: end tails. `2 ≤ delta ≤ 2^K` on both sides, so `|Dend| ≤ 2^K - 2 < 2^K`.
  have h2n : (2 : ℝ) ≤ delta (n + J + 2 + K) := two_le_delta (by omega)
  have h2m : (2 : ℝ) ≤ delta (m + J + 2 + K) := two_le_delta (by omega)
  have hDend_lt : |Dend| < 2 ^ K := by
    rw [hDend, abs_lt]
    constructor <;> linarith [htn, htm, h2n, h2m]
  -- Step 2: fork decomposition via the block identity at `n+J` and `m+J`.
  have hblk_n := delta_block (n + J) (K + 2)
  have hblk_m := delta_block (m + J) (K + 2)
  rw [show n + J + (K + 2) = n + J + 2 + K from by omega] at hblk_n
  rw [show m + J + (K + 2) = m + J + 2 + K from by omega] at hblk_m
  -- the block-code difference collapses to `γ * 2^K` (fork up/down, shared suffix)
  have hup_r : ((gap (n + J) : ℕ) : ℝ) = ((gap (m + J) : ℕ) : ℝ) + (γ : ℝ) := by
    rw [hup]; push_cast; ring
  have hdown_r : ((gap (n + J + 1) : ℕ) : ℝ) + (γ : ℝ) = ((gap (m + J + 1) : ℕ) : ℝ) := by
    rw [← hdown]; push_cast; ring
  have hSdiff : (∑ i ∈ Finset.range (K + 2), (2 : ℝ) ^ (K + 2 - 1 - i) * (gap (n + J + i) : ℝ))
      - (∑ i ∈ Finset.range (K + 2), (2 : ℝ) ^ (K + 2 - 1 - i) * (gap (m + J + i) : ℝ))
      = (γ : ℝ) * 2 ^ K := by
    rw [← Finset.sum_sub_distrib, Finset.sum_range_succ', Finset.sum_range_succ']
    have hzero : ∀ i ∈ Finset.range K,
        (2 : ℝ) ^ (K + 2 - 1 - (i + 1 + 1)) * (gap (n + J + (i + 1 + 1)) : ℝ)
          - (2 : ℝ) ^ (K + 2 - 1 - (i + 1 + 1)) * (gap (m + J + (i + 1 + 1)) : ℝ) = 0 := by
      intro i hi
      rw [Finset.mem_range] at hi
      have hg : gap (n + J + (i + 1 + 1)) = gap (m + J + (i + 1 + 1)) := by
        have h := hsuf i hi
        rw [show n + J + 2 + i = n + J + (i + 1 + 1) from by omega,
          show m + J + 2 + i = m + J + (i + 1 + 1) from by omega] at h
        exact h
      rw [hg]; ring
    rw [Finset.sum_eq_zero hzero]
    norm_num
    linear_combination (2 : ℝ) ^ (K + 1) * hup_r + (2 : ℝ) ^ K * hdown_r
  have h2K2 : (2 : ℝ) ^ (K + 2) * (delta (n + J) - delta (m + J)) = Dend + (γ : ℝ) * 2 ^ K := by
    rw [hDend, hblk_n, hblk_m]
    linear_combination hSdiff
  -- Step 3: fork closeness, `4 |Δfork| < 1 + γ`.
  have habs : |(2 : ℝ) ^ (K + 2) * (delta (n + J) - delta (m + J))| < 2 ^ K + (γ : ℝ) * 2 ^ K := by
    rw [h2K2]
    calc |Dend + (γ : ℝ) * 2 ^ K| ≤ |Dend| + |(γ : ℝ) * 2 ^ K| := abs_add _ _
      _ < 2 ^ K + (γ : ℝ) * 2 ^ K := by
          rw [abs_of_nonneg (by positivity : (0 : ℝ) ≤ (γ : ℝ) * 2 ^ K)]
          linarith [hDend_lt]
  have habs2 : (2 : ℝ) ^ K * (4 * |delta (n + J) - delta (m + J)|)
      < 2 ^ K * (1 + (γ : ℝ)) := by
    calc (2 : ℝ) ^ K * (4 * |delta (n + J) - delta (m + J)|)
        = |(2 : ℝ) ^ (K + 2) * (delta (n + J) - delta (m + J))| := by
          rw [abs_mul, abs_of_nonneg (by positivity : (0 : ℝ) ≤ (2 : ℝ) ^ (K + 2))]; ring
      _ < 2 ^ K + (γ : ℝ) * 2 ^ K := habs
      _ = 2 ^ K * (1 + (γ : ℝ)) := by ring
  have hfork4 : 4 * |delta (n + J) - delta (m + J)| < 1 + (γ : ℝ) :=
    (mul_lt_mul_left h2Kpos).mp habs2
  -- Step 4: lattice lock. `|b Δfork| < 2^(J+1)` forces the quantized `z` to vanish.
  obtain ⟨z, hz⟩ := repeated_block_quantization hb hlat_n hlat_m hpre
  have hbfork : |(b : ℝ) * (delta (n + J) - delta (m + J))| < 2 ^ (J + 1) := by
    rw [abs_mul, abs_of_nonneg (le_of_lt hbpos)]
    have h1 : (b : ℝ) * |delta (n + J) - delta (m + J)| ≤ (b : ℝ) * ((1 + (γ : ℝ)) / 4) :=
      mul_le_mul_of_nonneg_left (by linarith [hfork4]) (le_of_lt hbpos)
    have h2 : (b : ℝ) * ((1 + (γ : ℝ)) / 4) ≤ (b : ℝ) * (((γ : ℝ) + 4) / 4) :=
      mul_le_mul_of_nonneg_left (by linarith) (le_of_lt hbpos)
    have h3 : (b : ℝ) * (((γ : ℝ) + 4) / 4) < 2 ^ (J + 1) := by
      have hpow : (2 : ℝ) ^ (J + 3) = 4 * 2 ^ (J + 1) := by ring
      have he : (b : ℝ) * (((γ : ℝ) + 4) / 4) = ((b : ℝ) * ((γ : ℝ) + 4)) / 4 := by ring
      rw [he, div_lt_iff (by norm_num : (0 : ℝ) < 4)]
      linarith [hsmall, hpow]
    linarith [h1, h2, h3]
  have hz0 : z = 0 := by
    by_contra hzne
    have h1 : (1 : ℝ) ≤ |(z : ℝ)| := by
      have h : (1 : ℤ) ≤ |z| := Int.one_le_abs (by omega)
      exact_mod_cast h
    rw [hz, abs_mul, abs_of_nonneg (by positivity : (0 : ℝ) ≤ (2 : ℝ) ^ (J + 1))] at hbfork
    have h2pos : (0 : ℝ) < 2 ^ (J + 1) := by positivity
    have hle := mul_le_mul_of_nonneg_left h1 (le_of_lt h2pos)
    rw [mul_one] at hle
    linarith [hbfork, hle]
  have hb0 : (b : ℝ) * (delta (n + J) - delta (m + J)) = 0 := by rw [hz, hz0]; norm_num
  have hfork0 : delta (n + J) - delta (m + J) = 0 := by
    rcases mul_eq_zero.mp hb0 with h | h
    · exact absurd h (ne_of_gt hbpos)
    · exact h
  -- Step 5: contradiction. `Δfork = 0` forces `|Dend| = γ 2^K ≥ 2^(K+1)`, beating step 1.
  rw [hfork0, mul_zero] at h2K2
  have hDeq : Dend = -((γ : ℝ) * 2 ^ K) := by linarith [h2K2]
  rw [hDeq, abs_neg, abs_of_nonneg (by positivity : (0 : ℝ) ≤ (γ : ℝ) * 2 ^ K)] at hDend_lt
  have hmul : 2 * (2 : ℝ) ^ K ≤ (γ : ℝ) * 2 ^ K :=
    mul_le_mul_of_nonneg_right hγ (le_of_lt h2Kpos)
  linarith [hmul, hDend_lt, h2Kpos]

/-- Chain-v1 Theorem 3.2 plus section-6 glue: FM forces irrationality of
the 0-indexed series (hence of paper `S = erdosSeries / 2`). -/
theorem erdos_251_of_small_tail_fork_merge (hFM : SmallTailForkMerge) :
    Irrational erdosSeries := by
  obtain ⟨n, m, J, K, γ, hfm, h2, h3⟩ := hFM
  intro hmem
  obtain ⟨rr, hrr⟩ := hmem
  -- rationality of the 0-indexed series gives rationality of paper `S`
  have hS : IsRationalReal S :=
    ⟨rr / 2, by show ((rr / 2 : ℚ) : ℝ) = erdosSeries / 2; push_cast; rw [hrr]⟩
  obtain ⟨b, hb, hbodd, N, hlat⟩ := rational_delta_eventually_lattice hS
  have hb_pos : (0 : ℝ) < b := by exact_mod_cast hb
  have h8b : (0 : ℝ) < 8 / (b : ℝ) := by positivity
  -- (FM-2) and (FM-3): choose one configuration deep enough for both gates
  have e2 : ∀ᶠ r in atTop, ((γ r : ℝ) + 4) / 2 ^ (J r) < 8 / (b : ℝ) :=
    h2.eventually (gt_mem_nhds h8b)
  have e3 : ∀ᶠ r in atTop, N ≤ min (n r) (m r) := h3.eventually_ge_atTop N
  obtain ⟨r, hr2, hr3⟩ := (e2.and e3).exists
  have hnN : N ≤ n r := le_trans hr3 (min_le_left _ _)
  have hmN : N ≤ m r := le_trans hr3 (min_le_right _ _)
  have hsmall : (b : ℝ) * ((γ r : ℝ) + 4) < 2 ^ (J r + 3) := by
    rw [div_lt_div_iff (by positivity) hb_pos] at hr2
    have hpow : (2 : ℝ) ^ (J r + 3) = 8 * 2 ^ (J r) := by ring
    linarith [hr2, hpow]
  exact fork_merge_contradiction hb (hlat (n r) hnN) (hlat (m r) hmN) (hfm r) hsmall

end Erdos251
