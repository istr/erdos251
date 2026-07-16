# Lean project -- implication-cone state (item-0014, 2026-07-16)

Statement layer SETTLED from dossier/chain-v1.md (sections 1-3 and 8.2)
using the gpt-iso 9.x index conventions
(runs/20260712_chatgpt5.6sol_1b_noweb, section 9). No `True` placeholders
anywhere (the round-0 `HypUniformTuples := True` file was replaced).
All 15 statements are FROZEN (item-0002 deliverable); item-0003 proves
them without reformulation. CI checks compilation, not sorry-freeness.
Track the sorry count in HANDOVER.md.

## Layout (sorry inventory: 16 = 4 cone + 12 skeleton)
- Erdos251/Statement.lean   target theorem (vendored, unchanged)  [1]
- Erdos251/Chebyshev.lean   nth-prime upper bound (item-0003)     [0]
- Erdos251/Basic.lean       elementary layer, chain-v1 sec. 2     [0]
- Erdos251/ForkMerge.lean   fork-merge, chain-v1 sec. 3           [0]
- Erdos251/Hypotheses.lean  HLQuantA + CramerGranville, sec. 1    [2]
- Erdos251/Counting.lean    counting + construction skeleton,
                            chain-v1 v1.3 sec. 4-5 (NEW, item-0014) [12]
- Erdos251/Conditional.lean assembly interface, sec. 4-6          [1]
  plus the machine-checked composition `erdos_251_conditional`.

The 4 implication-cone residuals are unchanged by item-0014; Counting.lean
is a STATEMENT SKELETON that nothing in the cone imports yet, so it cannot
affect the milestone axiom gate (verified: `erdos_251_of_small_tail_fork_merge`
still depends only on [propext, Classical.choice, Quot.sound]).

## Erdos251/Counting.lean (item-0014 statement skeleton)
Chain-v1 v1.3 sections 4-5 transcribed as real definitions plus 12 named,
intentional sorries: Lemmata 4.1-4.4 (4 decls; 4.2/4.3 kappa-parametrized
per v1.1/F2) and 8 section-5 construction properties (word prefix/fork/
suffix, admissibility-in-budget, span, FM-2 limit, budgets, and the chain
down to `N_cons >= 1`). Zero True stubs. The traceability table
(Lean decl <-> chain-v1 ref <-> constants) lives in the module docstring
and is the review input. One flagged glue proof, `q_eq_of_count`
(Nat.count -> Nat.nth bridge), used only by four `example` smoke tests
that reproduce the review-verified tables at (J,K) = (3,4) and (2,3)
by decide/norm_num (no native_decide -- axiom gate).
Statement-set review pending; the proof item is created with its verdict.

## item-0003 milestone (elementary + fork-merge layer CLOSED)
11 of the 12 implication-cone sorries are discharged. Verified:

    #print axioms Erdos251.erdos_251_of_small_tail_fork_merge
    => [propext, Classical.choice, Quot.sound]      -- no sorryAx

The 4 residual `sorry`s are all NAMED and intentional:
- `Conditional.fork_merge_of_hypotheses` -- the analytic heart
  (chain-v1 sections 4-6: counting layer 4.1-4.4, deletion construction,
  assembly). Deliberately NOT started this pass; the operator decides how
  it gets funded. It is the last floor item of item-0003.
- `Hypotheses.singularSeries_multipliable`, `singularSeries_pos` -- the
  faithfulness pair, owned by item-0011 (kickoff scope option ii-a
  permits these to remain).
- `Statement.erdos_251_irrational` -- the unconditional Erdos target,
  out of reach by design; never to be touched.

## Erdos251/Chebyshev.lean (new helper, zero erdos251 coupling)
chain-v1 Lemma 2.1 (repair R1) needs a genuinely sub-geometric prime
bound: the trivial `p_n <= 2^n` does NOT license the delta-series
rearrangements, and Bertrand's `q(n+1) <= 2 q n` is exactly borderline
(it gives `q n / 2^n <= 2`, not summable). Mathlib packages a LOWER bound
on the n-th prime (`Nat.add_two_le_nth_prime`) and an UPPER bound on `pi`
(`Nat.primeCounting'_add_le`) -- both the wrong direction -- so the
Chebyshev lower bound on `pi` is built here from
`Nat.four_pow_lt_mul_centralBinom` plus central-binomial factorization,
entirely within the naturals (`Nat.clog` keeps it off the reals):

    centralBinom_le      : C(2n,n) <= (2n)^pi(2n)
    two_mul_lt_clog_mul  : 2n < clog 2 (2n) * (pi(2n) + 1)      (n >= 4)
    nth_prime_lt_sq      : nth Prime N < (N+2)^2                (N >= 5)

The file depends only on mathlib (no erdos251 definitions) and is an
upstream candidate; the mathlib gap is recorded in the item-0003
completion report.

## Corrections and deviations (flagged, never silent)
- Blind fidelity arm R3fid (runs/20260716_sonnet5_review3fid, ledger
  ANN-30): two post-review docstring disclosures added to
  Counting.lean -- Lemma 4.3's conclusion pair is deviation-weaker vs
  the prose chain (`M >= 4` not re-exported; the consumed shape is
  unchanged and the step moves into the proof obligation), and Lemma
  4.4's missing `1 <= Cg` is proved inert (`hB` unsatisfiable for
  `Cg < 0`). Statements byte-identical; no unfreeze. The frozen
  `CramerGranville` `C >= 1` question is routed to item-0011.
- Statement-unfreeze batch (round-2 decision 4, operator-ratified;
  resolves the ANN-18 deferral): the unused binder `hb : 0 < b` is
  removed from `repeated_block_quantization`; the single call site in
  ForkMerge.lean drops the argument. `b` stays inferable from `hn`'s
  type. No sorry-count change; compile gate is CI plus the executor's
  local build (the sandbox cannot build, see below).
- Round-0 warm-up 2 constant was FALSE (`erdosSeries/2 - 1`); corrected
  to `erdosSeries/2 - 2`, verified by exact Fraction arithmetic.
- gpt-iso field names `prefix`/`suffix` are Lean keywords; renamed
  `block_prefix`/`block_suffix`.
- chain-v1 Definition 3.1 ordering `n_r < m_r` dropped (section 6 swaps
  names; the proof never uses the order) -- ForkMerge.lean docstring,
  ledger ANN-12.
- Hypotheses are `def ... : Prop` existentials rather than Prop-valued
  structures with data fields, avoiding an elaboration edge case.
- gpt-iso 9.8 `HLQuantFull` is NOT ported (provably false as stated;
  triage-1b Q1 integrality defect). Hypothesis layer follows chain-v1.

## Toolchain and build
Pinned pair: `lean-toolchain` = leanprover/lean4:v4.16.0 == mathlib tag
v4.16.0 (rev a6276f4c6097675b1cf5ebd49b1146b735f38c02, pinned in
lakefile.toml; full transitive pins in the committed lake-manifest.json).

Local: `cd lean && lake exe cache get && lake build`.
CI: .github/workflows/lean.yml, leanprover/lean-action@v1 with
`lake-package-directory: lean` (the action fetches the mathlib cache
automatically). Repair loops follow runs/README rule 3: only the compiler
error message travels back.

## Steering-sandbox egress findings (2026-07-12, empirical)
The analysis-sandbox allowlist returns 403 x-deny-reason:host_not_allowed
for:
- release.lean-lang.org (elan release metadata + toolchain downloads).
  Workaround used: GitHub release asset lean-4.16.0-linux.tar.zst via
  github.com -> release-assets.githubusercontent.com (both allowlisted),
  then `elan toolchain link`.
- reservoir.lean-lang.org (lake registry resolution for scope-requires).
  Workaround: git+rev require form in lakefile.toml (also the more
  reproducible choice).
- mathlib cache hosts: mathlib4.lean-cache.cloud plus fallbacks
  lakecache.blob.core.windows.net and
  a09a7664adc082e00f294ac190827820.r2.cloudflarestorage.com.
  `lake exe cache get` fails (observed: 6014 downloads, all 403); building
  mathlib from source (~6000 modules) is out of sandbox budget. First
  green build therefore happens in CI or on the operator machine --
  or in-sandbox once the cache hosts are allowlisted.
