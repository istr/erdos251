import Mathlib

/-!
# Basic objects (index conventions to be settled in item I1)

Paper convention: S = sum_{n>=1} p_n/2^n, gaps g_n = p_{n+1} - p_n,
tail transform delta_n = sum_{j>=1} g_{n+j}/2^j (geometric weighted average
of future gaps). Key identities (proved informally in dossier/runde0.md,
numeric check to 1e-147): sum g_n/2^n = S - 2 and delta_{n+1} = 2 delta_n - g_{n+1}.

These stubs are the intended Aristotle warm-up targets.
-/

namespace Erdos251

/-- The series, 0-indexed Lean convention (equals `2 * S` in paper convention). -/
noncomputable def SL : ℝ := ∑' n : ℕ, (Nat.nth Nat.Prime n : ℝ) / 2 ^ n

/-- Prime gap, 0-indexed: `gap 0 = p_2 - p_1 = 1`. -/
def gap (n : ℕ) : ℕ := Nat.nth Nat.Prime (n + 1) - Nat.nth Nat.Prime n

/-- Tail transform: weighted average of future gaps. -/
noncomputable def delta (n : ℕ) : ℝ := ∑' j : ℕ, (gap (n + j) : ℝ) / 2 ^ (j + 1)

/-- Warm-up 1: the series converges. -/
theorem summable_SL : Summable (fun n : ℕ => (Nat.nth Nat.Prime n : ℝ) / 2 ^ n) := by
  sorry

/-- Warm-up 2: gap series identity (paper: sum g_n/2^n = S - 2). -/
theorem gap_series_identity :
    (∑' n : ℕ, (gap n : ℝ) / 2 ^ (n + 1)) = SL / 2 - 1 := by
  sorry

/-- Warm-up 3: tail recursion delta_{n+1} = 2 delta_n - g_{n+1} (index-shifted). -/
theorem delta_recursion (n : ℕ) :
    delta (n + 1) = 2 * delta n - (gap n : ℝ) := by
  sorry

end Erdos251
