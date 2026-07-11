import Erdos251.Statement

/-!
# Conditional target (item A2)

`HypUniformTuples` is a PLACEHOLDER (`True`). Pinning down the precise
uniform quantitative prime-tuples hypothesis is itself part of item A2;
until then the conditional theorem below is exactly as hard as the
unconditional one. Do not report progress against this file while the
placeholder stands.
-/

namespace Erdos251

/-- TODO(A2): replace by the precise uniform prime-tuples hypothesis. -/
def HypUniformTuples : Prop := True

theorem erdos_251_of_uniform_tuples (h : HypUniformTuples) :
    Irrational (∑' n : ℕ, (Nat.nth Nat.Prime n : ℝ) / 2 ^ n) := by
  sorry

end Erdos251
