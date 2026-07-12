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
  sorry

/-- Chain-v1 Theorem 3.2 plus section-6 glue: FM forces irrationality of
the 0-indexed series (hence of paper `S = erdosSeries / 2`). -/
theorem erdos_251_of_small_tail_fork_merge (hFM : SmallTailForkMerge) :
    Irrational erdosSeries := by
  sorry

end Erdos251
