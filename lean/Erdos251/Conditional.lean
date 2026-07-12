import Erdos251.Statement
import Erdos251.ForkMerge
import Erdos251.Hypotheses

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

/-- Chain-v1 sections 4-6: Hypotheses A and B produce a fork-merge
sequence (Bonferroni transfer 4.3, deletion construction 5, tail bound
4.4 from B, assembly 6). -/
theorem fork_merge_of_hypotheses (hA : HLQuantA) (hB : CramerGranville) :
    SmallTailForkMerge := by
  sorry

/-- Chain-v1 THEOREM on the 0-indexed sum (the Erdos #251 target
expression of `Statement.lean`): Hypotheses A and B imply irrationality. -/
theorem erdos_251_conditional (hA : HLQuantA) (hB : CramerGranville) :
    Irrational (∑' n : ℕ, (Nat.nth Nat.Prime n : ℝ) / 2 ^ n) :=
  erdos_251_of_small_tail_fork_merge (fork_merge_of_hypotheses hA hB)

end Erdos251
