# Lean project (UNVERIFIED skeleton)

Authored in a sandbox without Lean toolchain access. Before first use (item I1):
1. Sync `lean-toolchain` with the pinned mathlib release you choose
   (copy mathlib's own `lean-toolchain`), and pin the mathlib require to a rev.
2. `lake exe cache get` then `lake build` locally; fix any bit-rot in the stubs
   (index conventions in Basic.lean are the likely friction point).
3. CI: `.github/workflows/lean.yml` uses leanprover/lean-action with
   `lake-package-directory: lean` -- verify the input name against the action's
   current README on first run.
Sorries are intentional (they are the work); CI checks compilation, not
sorry-freeness. Track the sorry count in HANDOVER.md.
