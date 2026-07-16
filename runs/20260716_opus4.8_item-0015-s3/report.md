# item-0015 session 3 -- completion report (M2 shape)

Executor: Claude Opus 4.8 (1M context). Date: 2026-07-16.
Kickoffs: item-0015-kickoff-v3.md, superseded on the MP-M2 route only by
kickoff-v3.1-delta-m2-abel.md (both ephemeral, never committed).
Branch: `item-0015-s3`, four executor commits, `Counting.lean` only.

**Outcome: T1 proved; the Mertens pack M1-M3 proved with the sharp constant;
T2's foundation (step (a)) proved and its `k = 0` edge discharged. The v3
dyadic MP-M2 route was caught defective mid-session, retired by steering
(ANN-37), and the v3.1 discrete-Abel replacement executed to completion.
T2 (b)-(d), T3, T4 remain for session 4 -- now unblocked.**

Executor commits:

    2dc3f65  T2 step (a) ratio analysis + k=0 edge discharged
    bea34c5  MP pack complete -- M2 (discrete Abel) + M3, coefficient exactly 1
    a40f7ad  MP/M1 mertens_one_upper + dyadic-route defect (M2 STOP)
    1776014  prove T1 singularSeries_lower_bound (4.1, Mertens-free)

## Gates verbatim

| Gate | Status |
|---|---|
| Statements, defs, docstrings, smoke examples, all prior proofs byte-identical | **PASS** -- zero deleted lines vs the v3.1 anchor `b7259038`; the only deleted line vs the original pin `807b6b7` is T1's discharged `-  sorry` |
| Helpers in marked proof-layer sections | **PASS** -- three new marked sections (4.1, Mertens pack, 4.2) |
| Strict sorry grep decreases | **PASS** -- 6 -> 5 (Counting 4 -> 3) |
| Axiom gate | **PASS** -- `erdos_251_of_small_tail_fork_merge`, `singularSeries_lower_bound`, `mertens_one_upper`, `mertens_second_upper`, `mertens_third_upper`, `log_singularFactor_insert_sub_le`, `nuMod_insert` all `[propext, Classical.choice, Quot.sound]`, no `sorryAx` |
| Local build | **PASS** -- `lake build` green, no `lake update`, `lean-toolchain` newline intact |
| Unprovable-as-frozen -> STOP | **Not triggered.** No frozen statement is implicated, at any point |

Sorry inventory: 5 = Counting 3 + Conditional 1 + Statement 1. The surviving
Counting sorries are exactly `oneExtension_sum_le` (4.2),
`consCount_lower_bound` (4.3), `constr_consCount_pos`.

**Pin note.** The v3 pin `807b6b7` is not main's tip and never was: s2 was
*rebased* onto main (`e8b743b..4d3503f`), so main's Lean tree is byte-identical
to it. HANDOVER's pending-decision 1 ("MERGE branch item-0015-s2") is already
discharged; only the sha is stale. The v3.1 anchor `b7259038` = HEAD~3 at
receipt, as stated.

**v3.1 validity predicate: held.** (a) pin `b7259038` confirmed; (b) MP-M1 as
landed has the required upper shape with threshold `N >= 1` (better than the
required 2), so the section-3 threshold-split adaptation was not needed;
(c) no dyadic MP-M2 partials existed to discard. All delta mathlib names
verified at the pin (`inv_le_inv_of_le` is deprecated -> `inv_anti0` used).

## Observations

### T1 `singularSeries_lower_bound` (4.1) -- PROVED, `C = 12`

Mertens-free route as specified. Head `p <= P0 = 2|H|` via `primorial_le_4_pow`;
tail via a new one-sided sibling of `abs_log_singularFactor_le` needing neither
the span condition nor admissibility (only `nu <= |H|`), giving
`log factor >= -2(|H|/p)^2`, summed against `sum_Ioc_inv_sq_le_sub`. Net
`S(H) >= exp(-2|H| log 4 - |H|)`.

* **`C = 10` does not close; `C = 12` does.** With only `Real.log_two_gt_d9` as
  numeric log input, `C >= 6.87` suffices via `log(k+2) >= log 3`, but the far
  cheaper `log(k+2) >= log 2` needs `C >= 12`. Took the cheaper bound.
* **The `k = 0` corner needs equality, not slack.** The kickoff offers "check
  separately *or* note `k log(k+2) = 0`" -- only the first works. At `k = 0` the
  target is `exp(0) = 1`, so the generic bound (`~0.023`) is useless; `H = {0}`
  forces `S = 1` exactly (`singularSeries_singleton_zero`).
* **hCg pattern, twice.** Clause 2's budget hypotheses are unused as predicted.
  *Additionally, not predicted:* **evenness is unused in both clauses** --
  `singularSeries_ge_exp` needs only `0 in H` and admissibility. Clause 2's
  threshold is `x0 = 3`.

### MP pack M1-M3 -- PROVED, sorry-free, sharp

MP-M1 (`mertens_one_upper`), `c1 = log 4`:
`sum_{p <= N} log p / p <= log N + log 4` for `N >= 1`. Kickoff correction:
**`Nat.Prime.factorization_factorial` does not exist at the pin**; Legendre's
formula is `padicValNat_factorial`.

MP-M2 (`mertens_second_upper`), **leading coefficient EXACTLY 1**:
`sum_{p <= P} 1/p <= lnln P + c2`, `c2 = 1 + b/log 2 - lnln 2` (symbolic in
MP-M1's `b`; numerically 3.3665).

MP-M3 (`mertens_third_upper`), **exponent EXACTLY 1 on log**:
`prod_{p <= P} (1 - 1/p)^-1 <= c3 log P`, `c3 = exp(c2 + 1)` (numerically 78.77).

Integral-free as required: `Mathlib.NumberTheory.AbelSummation` unused.
Depends only on mathlib -- relocatable to `Chebyshev.lean`, upstream candidate
(ANN-36; routed through this report, not moved mid-session).

**MP-M1's LOWER clause is not needed and was never built.** The nonnegative
weight differences keep any lower constant out of the estimate entirely (v3.1
section 3 refinement -- confirmed in the build). The factorial lower bound
`N! >= (N/e)^N` flagged as a cost in the interim report is therefore OFF the
critical path. Mathlib carries no elementary form of it (`Stirling.lean` is
asymptotic only), so this is a real saving.

### The dyadic MP-M2 defect (executor-caught, adjudicated ANN-37)

Recorded for the methodology register. The v3 dyadic route bounds
`1/p <= (log p / p)/(j log r)` on `p in (r^j, r^(j+1)]`. Even with MP-M1
telescoped in both directions the block sum of `log p / p` is only
`<= log r + C`, `C > 0` the sum of MP-M1's two error constants, so
`sum_{block} 1/p <= (1 + C/log r)/j` -- coefficient **strictly > 1** for every
fixed ratio `r`, because the error couples to the divergent harmonic sum over
block indices and thus lands in the LEADING coefficient. With the crude
primorial input the coefficient is 4. Numerics (executor, then steering
re-executed): route gives `4/j` against a true block sum `~1/j`; at `P = 2^20`,
route bound 14.69 vs true 2.89 vs `lnln P = 2.63`.

Load-bearing, not cosmetic: T2's frozen `log(k+2)^2` budget spends one log on
MP-M3 and one on the span, so MP-M3 needs exponent `<= 1`, i.e. MP-M2
coefficient exactly 1. The v3 text silently dropped the coefficient. **The
frozen 4.2 statement was never implicated** -- the defect was kickoff-layer.

The v3.1 fix is structural, not a patch: discrete Abel couples the SAME MP-M1
error to the telescoping total weight variation
`sum (w i - w (i+1)) = w 2 - w P <= 1/log 2`, which is bounded, so the error
stays ADDITIVE.

### T2 `oneExtension_sum_le` (4.2) -- foundation proved, (b)-(d) open

* **`k = 0` edge DISCHARGED** (kickoff's "TEST THIS FIRST"): `offsetSpan {0} = 0`
  by `decide`, so `oneExtensions {0} = empty` and the frozen statement reads
  `0 <= 0`. Not false at `k = 0`.
* **Step (a) PROVED**: `nuMod_insert` (nu moves by 0 or 1) and
  `log_singularFactor_insert_sub_le` (the per-prime log-ratio is
  `<= if nu' = nu then -log(1-1/p) else 0`): COLLISION contributes exactly
  `log(1 + 1/(p-1))`, NEW contributes `<= 0`.
* Remaining: (b) collision primes `< span`; (c) split at `k+2` -- SMALL via
  MP-M3, LARGE via the squarefree-divisor expansion; (d) assembly. **(c)-LARGE
  is the substantial piece**: a sieve-theoretic divisor expansion over a
  variable prime set with `omega(d)` counting, materially larger than anything
  landed this session.

### Ledger position for session 4 (kickoff section 5)

T3's five-term Bonferroni ledger was not entered; all five terms are missing.
T3 needs T2; T2 now needs only (b)-(d).

## Re-execution record (checklist rule iv)

Nothing below was taken on the kickoff's word:

* v3 dyadic block bound vs true block sums -- **defect found** (see above).
* Kickoff 4(a) algebra `(p-nu-1)p <= (p-nu)(p-1) iff 0 <= nu`: re-derived,
  `RHS - LHS = nu` -- **confirmed**.
* v3.1 (IDENT): re-executed to machine precision at
  `P in {2, 10, 97, 1000, 12345, 250000}` -- **confirmed**.
* v3.1 Step 4 exact cancellation: `= b/log 2 = 2.0` exactly -- **confirmed**.
* v3.1 Step 5 pointwise inequality: `i in [2, 200000)`, zero violations --
  **confirmed**.
* Final MP-M2 / MP-M3 bounds at all check points -- **confirmed**.
* MP-M3 empirical exponent vs `log P`: **0.9937** (ratio flat at 0.0226 from
  `P = 1e3` to `2.5e5`) -- exponent 1 confirmed, which is what T2 needs.
* `k = 0` edge of frozen 4.2: verified in Lean, not just numerically.

## Follow-up candidates

1. **MP is upstream-ready.** M1-M3 depend only on mathlib and are the project's
   first reusable analytic-number-theory toolkit beyond `Chebyshev.lean`.
   ANN-36 books MP as an upstream candidate; the gap is real on master.
   Relocation to `Chebyshev.lean` deliberately not done mid-session per v3.1
   section 5.
2. **Unfreeze candidates (deferred, hCg class).** 4.1 clause 2's two budget
   hypotheses *and* both clauses' evenness hypothesis are unused. Evenness is
   the more interesting datum: unused in 4.1 but a genuine hypothesis of
   `HLQuantA`, so this is not a symmetric drop.
3. **Duplication to tidy.** T1's head sum is indexed over `Finset Nat.Primes`
   (`primesLe`), MP's over `Finset Nat` (`primesUpto`); both prove the same
   primorial bound. T1 was not refactored (committed and green); a session-4
   cleanup could unify on the Nat form.
4. **HANDOVER staleness.** Pending-decision 1 should be struck (merge already
   discharged via rebase), and the v3 pin sha corrected.
5. **Method note worth keeping** (alongside the ANN-35 `log_two_gt_d9` scaling
   note): when a kickoff's route carries an O(1) error through a divergent sum,
   check WHERE the error lands before building -- leading coefficient vs
   additive constant is the whole question, and it is cheap to settle
   numerically in advance. That check is what caught the dyadic defect.

`fork_merge_of_hypotheses` untouched, as scoped.
