import Mathlib

/-!
# Erdős Problem 251 -- target statement

Vendored and adapted from google-deepmind/formal-conjectures (Apache-2.0),
file `FormalConjectures/ErdosProblems/251.lean`. The original frames the
problem as `answer(sorry) ↔ Irrational (...)`; we state the conjectured
direction (Erdős: irrational) as the target.

Indexing note: `Nat.nth Nat.Prime 0 = 2 = p_1`, so the sum below equals
`2 * S` where `S = ∑_{n ≥ 1} p_n / 2^n` (paper convention, S ≈ 3.67464...).
Irrationality of the two is equivalent.
-/

namespace Erdos251

/-- Erdős Problem #251, conjectured direction. -/
theorem erdos_251_irrational :
    Irrational (∑' n : ℕ, (Nat.nth Nat.Prime n : ℝ) / 2 ^ n) := by
  sorry

end Erdos251
