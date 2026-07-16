import Mathlib
import Erdos251.Basic
import Erdos251.Hypotheses

/-!
# Counting layer and deletion construction (chain-v1 v1.3, sections 4-5)

STATEMENT SKELETON (item-0014). Definitions are real; the lemmata are
intentional, named `sorry`s. No proof investment happens here: the
statement set is the deliverable and the review object. Nothing in this
file is used by the landed implication cone, and nothing here touches the
frozen files.

Source of truth: `dossier/chain-v1.md` v1.4 (citation-hygiene amendment
of v1.3, ANN-31; statements and mathematics unchanged), sha256
`6bcb1425271a3d55db955f1c63c3b7b205c2fc7a6a93625bc688afdea778ec0b`,
sections 4 (Lemmata 4.1-4.4) and 5 (deletion construction); interface
conventions from section 8.2 and the landed `Hypotheses.lean`.

## Index conventions (inherited from `Basic.lean`, unchanged)
* `q n = Nat.nth Nat.Prime n` is 0-indexed: `q 0 = 2 = ` paper `p_1`, so
  paper `p_ν` is `q (ν - 1)`.
* `gap n` = paper `g_{n+1}`; `delta n` = paper `delta_n` (no shift).
* Paper "consecutive realization of `w = (w_1,...,w_L)` at `n`" is
  `∀ j < L, gap (n + j) = w j` with the 0-indexed word `w j = ` paper
  `w_{j+1}`; the anchor prime `p_{n+1}` is `q n`.

## Traceability table (MANDATORY, item-0014 kickoff v2)

| Lean declaration                | chain-v1 v1.3 ref        | constants / notes                                  |
|---------------------------------|--------------------------|----------------------------------------------------|
| `IsConsecRealization`           | sec. 4 preamble          | -- (definition)                                    |
| `wordPointSet`                  | sec. 4 preamble, 5       | -- ; 0-based `H(w)`, prefix sums (= `A - q_0`)     |
| `offsetSpan`                    | 4.2 `D = h_k`, 5(iii)    | -- ; `Finset.sup id`, total (0 on `∅`)             |
| `oneExtensions`                 | 4.2 range of `t`         | -- ; even `t ∈ (0, D)`, `t ∉ H`, `H ∪ {t}` adm.    |
| `consCount`                     | 4.3 `N_cons(w; x)`       | -- ; anchor `q n ∈ (√x, x]`                        |
| `singularSeries_lower_bound`    | LEMMA 4.1 (both clauses) | `C` (shared by both clauses; `0 < C` added)        |
| `oneExtension_sum_le`           | LEMMA 4.2 (v1.1)         | `κ ≥ 1` explicit param, `C₂ = C₂(κ)`               |
| `consCount_lower_bound`         | LEMMA 4.3 (v1.1)         | `κ ≥ 1` explicit param; factors `1/4`, `1`         |
| `delta_le_of_gap_bound`         | LEMMA 4.4                | `C_g` threaded explicitly; factor `3`              |
| `cK`, `cJ`, `cL`, `cI`          | sec. 5 constants         | `K`, `J`, `L = J+2+K`, `i_0 = J+1` (v1.1/F1)       |
| `tailBudget`                    | sec. 5 `H_x`             | `H_x = 4 C_g (ln x)^2`                             |
| `primeIdxAbove`, `cprime`       | sec. 5 `q_0 < ... < q_{L+1}` | first `L+2` primes exceeding `L+3`             |
| `cElem`, `cElem'`               | sec. 5 `A`, `A'`         | monotone enumerations; the deletion IS the `if`    |
| `cword`, `cword'`, `cgamma`     | sec. 5 `w`, `w'`, `gamma`| `gamma = q_{i_0+1} - q_{i_0}`                      |
| `q_eq_of_count`                 | -- (glue, PROVED)        | flagged: `Nat.nth`/`Nat.count` bridge, smoke tests |
| `cword_prefix`                  | sec. 5(i) prefix         | length `J`                                         |
| `cword_fork`                    | sec. 5(i) fork           | natural order `(w, w')`: `(-gamma, +gamma)`        |
| `cword_suffix`                  | sec. 5(i) suffix         | length `K`                                         |
| `cword_admissible`              | sec. 5(ii) + 5(iv) card  | both words; `|H(w)| = L+1`                         |
| `cspan_le`                      | sec. 5(iii)              | `C_1 ≥ 1`; supplies 4.3's `κ := C_1`               |
| `cfm2_tendsto`                  | sec. 5(iii) limit        | `(gamma+4)/2^J → 0` (FM-2 shape)                   |
| `cbudget`                       | sec. 5 "x large", 5(iv)  | `J, K ≥ 1`; `2^K ≥ H_x`; `lnln x` windows          |
| `constr_consCount_pos`          | 4.3 ∘ 5, sec. 6 entry    | the chain down to `N_cons ≥ 1`                     |

Glue proofs (flagged): `q_eq_of_count` only. Smoke tests: four `example`s
reproducing the review-verified tables `(J,K) = (3,4)` and `(2,3)`.

## Amendment context (provenance, NOT statements -- v1.3 bracket notes)
* v1.1/F1: `i_0 = J + 1`. The v1.0 value `J + 2` made section 5(i) false
  (prefix `J+1`, suffix `K-1`, fork one slot late) and cost FM-1 a factor
  2 that section 6 cannot supply. Surfaced by this item's session 1.
* v1.1/F2: Lemma 4.2's span hypothesis `D ≤ κ k ln(k+2)` is NECESSARY,
  not cosmetic: for `H = {0, D}` (`k = 1`) every admissible even `t` has
  ratio `≥ 1.2` and there are `~D/2` of them, so the unrestricted v1.0
  claim is FALSE. Lemma 4.3 inherits the narrowed span; section 5(iii)
  supplies exactly the narrow form.
* v1.2: Lemma 4.2's sketch (not its statement) lost its κ-uniform
  "≤ 3k collisions / product ≤ e^2" bounds; the STATEMENT is unaffected.
-/

namespace Erdos251

noncomputable section

/-! ## Section 4 preamble: gap words, their point sets, consecutive counts -/

/-- Paper (section 4 preamble): "consecutive realization of a gap word
`w = (w_1,...,w_L)` at `n`" means `g_{n+i} = w_i` for all `i`.
0-indexed here: `w j` is paper `w_{j+1}` and `gap (n + j)` is paper
`g_{n+j+1}`. Bounded quantifier over `Finset.range L` (decidability). -/
def IsConsecRealization (w : ℕ → ℕ) (L n : ℕ) : Prop :=
  ∀ i ∈ Finset.range L, gap (n + i) = w i

/-- The 0-based point set `H(w)` of a gap word `w` of length `L`: the
`L+1` prefix sums `{0, w_1, w_1+w_2, ...}` (section 4 preamble). For the
section-5 words this is exactly `A - q_0` / `A' - q_0`, the 0-based
handoff object Lemma 4.3 and Hypothesis A receive (v1.2, re-review R2);
translation is absorbed by taking prefix sums, so no translation lemma is
needed. `0 ∈ wordPointSet w L` always (the empty prefix sum). -/
def wordPointSet (w : ℕ → ℕ) (L : ℕ) : Finset ℕ :=
  Finset.image (fun j : ℕ => ∑ i ∈ Finset.range j, w i) (Finset.range (L + 1))

/-- The span `D = h_k` of an offset set (Lemma 4.2, section 5(iii)):
the largest offset. Total by `Finset.sup id` (`= 0` on `∅`); for the
`H` of interest `0 ∈ H`, so this is the paper's `max`. -/
def offsetSpan (H : Finset ℕ) : ℕ := H.sup id

open scoped Classical in
/-- The range of `t` in Lemma 4.2: even `t ∈ (0, D)` with `D = h_k` the
span, `t ∉ H`, and `H ∪ {t}` admissible. -/
def oneExtensions (H : Finset ℕ) : Finset ℕ :=
  Finset.filter (fun t : ℕ => Even t ∧ 0 < t ∧ t ∉ H ∧ IsAdmissible (insert t H))
    (Finset.range (offsetSpan H))

open scoped Classical in
/-- `N_cons(w; x)` (Lemma 4.3): the number of consecutive realizations of
`w` whose anchor prime `p_{n+1} = q n` lies in `(√x, x]`. The outer
`Finset.range (x+1)` loses nothing: `n < q n ≤ x` forces `n < x + 1`. -/
def consCount (w : ℕ → ℕ) (L x : ℕ) : ℕ :=
  (Finset.filter
    (fun n : ℕ => IsConsecRealization w L n ∧ Real.sqrt x < (q n : ℝ) ∧ q n ≤ x)
    (Finset.range (x + 1))).card

/-! ## Section 4: the counting lemmata (conditional on A; classical citations) -/

/-- LEMMA 4.1 (singular series lower bound). For admissible `H` of even
offsets with `|H| = k+1`: `S(H) ≥ exp(-C k ln(k+2))`; consequently, in
the budget of Hypothesis A, `M_H(x) ≥ x exp(-C k ln(k+2) - (k+1) lnln x)`
(`= x^{1-o(1)}`, which is prose and is NOT transcribed -- see the report).
Both clauses share the single constant `C`, as in the paper; `k = |H| - 1`
and `k + 2 = |H| + 1`. `0 < C` is added (equivalent: the bound is monotone
in `C`) and flagged. -/
theorem singularSeries_lower_bound :
    ∃ C : ℝ, 0 < C ∧
      (∀ H : Finset ℕ, 0 ∈ H → (∀ h ∈ H, Even h) → IsAdmissible H →
        Real.exp (-(C * ((H.card : ℝ) - 1) * Real.log ((H.card : ℝ) + 1)))
          ≤ singularSeries H) ∧
      (∃ x₀ : ℕ, ∀ x : ℕ, x₀ ≤ x →
        ∀ H : Finset ℕ, 0 ∈ H → (∀ h ∈ H, Even h) → IsAdmissible H →
          (H.card : ℝ) ≤ 4 * Real.log (Real.log x) →
          (∀ h ∈ H, (h : ℝ) ≤ Real.log x ^ 3) →
          (x : ℝ) * Real.exp (-(C * ((H.card : ℝ) - 1) * Real.log ((H.card : ℝ) + 1))
              - (H.card : ℝ) * Real.log (Real.log x))
            ≤ modelMass H x) := by
  sorry

/-- LEMMA 4.2 (one-point extension sum; v1.1). For any fixed `κ ≥ 1`
there is `C₂ = C₂(κ)` such that for admissible `H` of even offsets with
span `D = h_k ≤ κ k ln(k+2)`, the sum over the one-point extensions of
`S(H ∪ {t})/S(H)` is `≤ C₂ k (ln(k+2))^2`.

The span hypothesis is NECESSARY, not cosmetic (v1.1/F2): for `H = {0,D}`
(`k = 1`) every admissible even `t` has ratio `≥ 1.2` (the `p = 2` factor
alone is 2) and there are `~D/2` such `t`, so the sum grows like `D`
against a `D`-free right side; the unrestricted form is FALSE. -/
theorem oneExtension_sum_le (κ : ℝ) (hκ : 1 ≤ κ) :
    ∃ C₂ : ℝ, ∀ H : Finset ℕ, 0 ∈ H → (∀ h ∈ H, Even h) → IsAdmissible H →
      (offsetSpan H : ℝ) ≤ κ * ((H.card : ℝ) - 1) * Real.log ((H.card : ℝ) + 1) →
      ∑ t ∈ oneExtensions H, singularSeries (insert t H) / singularSeries H
        ≤ C₂ * ((H.card : ℝ) - 1) * Real.log ((H.card : ℝ) + 1) ^ 2 := by
  sorry

/-- LEMMA 4.3 (consecutive lower bound; the transfer; v1.1). Let `w` be a
gap word whose point set `H(w)` is admissible, `|H(w)| = L+1 ≤ 4 lnln x - 1`,
span `≤ κ L ln(L+2)` for a fixed `κ ≥ 1` (hence far inside A's `(ln x)^3`
budget). Under Hypothesis A, for all large `x`:
`N_cons(w; x) ≥ (1/4) M_{H(w)}(x) ≥ 1`.

The span hypothesis is 4.2's, with `k = L` (v1.1/F2): the wide v1.0 form
`span ≤ (ln x)^3` is unprovable by this route and heuristically false
outright for `span ≫ ln x` (Cramer-type thinning absent from `M_H`).
Evenness of the offsets is not hypothesised: it follows from
admissibility, since `0 ∈ H(w)` and an odd offset would occupy both
classes mod 2.

Disclosure (blind fidelity arm R3fid): the conclusion pair is strictly
WEAKER than the prose chain `N_cons ≥ (1/4) M ≥ 1`, which additionally
exports `M ≥ 4`. The pair is exactly what `constr_consCount_pos`
consumes; the `M ≥ 4` step becomes part of this lemma's proof
obligation via 4.1's in-budget mass bound. Accepted deviation-weaker
(ANN-30). -/
theorem consCount_lower_bound (hA : HLQuantA) (κ : ℝ) (hκ : 1 ≤ κ) :
    ∃ x₀ : ℕ, ∀ x : ℕ, x₀ ≤ x → ∀ (w : ℕ → ℕ) (L : ℕ),
      IsAdmissible (wordPointSet w L) →
      (wordPointSet w L).card = L + 1 →
      ((L : ℝ) + 1) ≤ 4 * Real.log (Real.log x) - 1 →
      (offsetSpan (wordPointSet w L) : ℝ) ≤ κ * (L : ℝ) * Real.log ((L : ℝ) + 2) →
      modelMass (wordPointSet w L) x / 4 ≤ (consCount w L x : ℝ)
        ∧ 1 ≤ consCount w L x := by
  sorry

/-! ### Proof-layer helpers for Lemma 4.4 (item-0015; not statements) -/

/-- Bertrand step for the prime enumeration: the next prime is at most
twice the current one. Bertrand gives a prime `p ∈ (q m, 2 q m]`; the
count/nth bridge places `q (m+1)` at or below it. -/
theorem q_succ_le_two_mul (m : ℕ) : q (m + 1) ≤ 2 * q m := by
  have hqm2 : 2 ≤ q m := (q_prime m).two_le
  obtain ⟨p, hp, hlt, hle⟩ := Nat.exists_prime_lt_and_le_two_mul (q m) (by omega)
  have hcqm : Nat.count Nat.Prime (q m) = m := by
    simpa [q] using Nat.count_nth_of_infinite Nat.infinite_setOf_prime m
  have hcqm1 : Nat.count Nat.Prime (q m + 1) = m + 1 := by
    rw [Nat.count_succ, hcqm, if_pos (q_prime m)]
  have hmono : m + 1 ≤ Nat.count Nat.Prime p := by
    rw [← hcqm1]; exact Nat.count_monotone _ (by omega)
  have hcp1 : m + 1 < Nat.count Nat.Prime (p + 1) := by
    rw [Nat.count_succ, if_pos hp]; omega
  have hnth : Nat.nth Nat.Prime (m + 1) < p + 1 := Nat.nth_lt_of_lt_count hcp1
  have : q (m + 1) ≤ p := by simpa [q] using Nat.lt_succ_iff.mp hnth
  omega

/-- Iterated Bertrand: `q (n + k) ≤ 2^k * q n`. -/
theorem q_add_le_two_pow (n k : ℕ) : q (n + k) ≤ 2 ^ k * q n := by
  induction k with
  | zero => simp
  | succ k ih =>
    calc q (n + (k + 1)) ≤ 2 * q (n + k) := q_succ_le_two_mul (n + k)
      _ ≤ 2 * (2 ^ k * q n) := by have := ih; omega
      _ = 2 ^ (k + 1) * q n := by ring

/-- Log form of the iterated Bertrand bound:
`log (q (n+1+j)) ≤ log (q n) + (j+1)` (using `log 2 ≤ 1`). -/
theorem log_q_shift_le (n j : ℕ) :
    Real.log (q (n + 1 + j)) ≤ Real.log (q n) + ((j : ℝ) + 1) := by
  have hqnpos : (0 : ℝ) < (q n : ℝ) := by exact_mod_cast (q_prime n).pos
  have hbound : q (n + 1 + j) ≤ 2 ^ (j + 1) * q n := by
    have h := q_add_le_two_pow n (1 + j)
    have e1 : n + (1 + j) = n + 1 + j := by ring
    have e2 : (2 : ℕ) ^ (1 + j) = 2 ^ (j + 1) := by rw [Nat.add_comm]
    rw [e1, e2] at h; exact h
  have hcast : (q (n + 1 + j) : ℝ) ≤ 2 ^ (j + 1) * (q n : ℝ) := by
    calc (q (n + 1 + j) : ℝ) ≤ ((2 ^ (j + 1) * q n : ℕ) : ℝ) := by exact_mod_cast hbound
      _ = 2 ^ (j + 1) * (q n : ℝ) := by push_cast; ring
  have hlogle : Real.log (q (n + 1 + j)) ≤ Real.log (2 ^ (j + 1) * (q n : ℝ)) :=
    Real.log_le_log (by exact_mod_cast (q_prime (n + 1 + j)).pos) hcast
  rw [Real.log_mul (by positivity) (ne_of_gt hqnpos), Real.log_pow] at hlogle
  have hlog2 : Real.log 2 ≤ 1 := by
    have := Real.log_le_sub_one_of_pos (by norm_num : (0 : ℝ) < 2); linarith
  have hj0 : (0 : ℝ) ≤ (j : ℝ) + 1 := by positivity
  have hstep : (↑(j + 1) : ℝ) * Real.log 2 ≤ (j : ℝ) + 1 := by
    push_cast; nlinarith [mul_nonneg hj0 (sub_nonneg.mpr hlog2)]
  linarith [hlogle, hstep]

/-- LEMMA 4.4 (tail bound from B). Under Hypothesis B there is `ν_1` with
`delta_ν ≤ 3 C_g (ln p_ν)^2` for all `ν ≥ ν_1`.

Index map: paper `delta_ν` is `delta ν` and paper `p_ν` is `q (ν - 1)`,
so `ν = n + 1` gives the ℕ-subtraction-free form below. `C_g` is threaded
as an explicit parameter rather than re-existentialised, which is what
keeps the factor `3` meaningful (`∃ C, delta ≤ 3 * C * ...` would be
vacuous). The hypothesis is exactly the body of the frozen
`CramerGranville`, which binds `∃ C : ℝ` with no sign or size constraint;
the frozen definition is not touched. The missing `1 ≤ Cg` (which prose's
"Under Hypothesis B" supplies) is INERT: `gap n ≥ 1` always, while
`Cg * log (q n)^2 < 0` for `Cg < 0`, so `hB` is unsatisfiable there and
the broadened statement licenses nothing false (proved by the R3fid arm,
ANN-30). The `C ≥ 1` faithfulness question for the frozen definition
itself is item-0011's. -/
theorem delta_le_of_gap_bound {Cg : ℝ} {n₀ : ℕ}
    (hB : ∀ n : ℕ, n₀ ≤ n → (gap n : ℝ) ≤ Cg * Real.log (q n) ^ 2) :
    ∃ n₁ : ℕ, ∀ n : ℕ, n₁ ≤ n → delta (n + 1) ≤ 3 * Cg * Real.log (q n) ^ 2 := by
  -- `Cg > 0` is forced by `hB` (ANN-30 inertness): `1 ≤ gap n₀ ≤ Cg log(q n₀)²`.
  have hCg0 : 0 < Cg := by
    have hg1 : (1 : ℝ) ≤ (gap n₀ : ℝ) := by exact_mod_cast gap_pos n₀
    have hb := hB n₀ le_rfl
    have hlogpos : 0 < Real.log (q n₀) :=
      Real.log_pos (by exact_mod_cast (q_prime n₀).one_lt)
    nlinarith [hb, hg1, mul_pos hlogpos hlogpos]
  -- summability infrastructure
  have hgeom : Summable (fun j : ℕ => (1 : ℝ) / 2 ^ (j + 1)) := by
    have hg' : Summable (fun j : ℕ => (1 / 2 : ℝ) ^ (j + 1)) :=
      (summable_nat_add_iff (f := fun n : ℕ => (1 / 2 : ℝ) ^ n) 1).mpr
        (summable_geometric_of_lt_one (by norm_num) (by norm_num))
    exact hg'.congr (fun j => by rw [div_pow, one_pow])
  have hnorm : ‖(1 / 2 : ℝ)‖ < 1 := by
    rw [Real.norm_of_nonneg (by norm_num : (0 : ℝ) ≤ 1 / 2)]; norm_num
  have hBsum : Summable (fun j : ℕ => ((j : ℝ) + 1) ^ 2 / 2 ^ (j + 1)) := by
    have h2 : Summable (fun j : ℕ => (j : ℝ) ^ 2 * (1 / 2) ^ j) :=
      summable_pow_mul_geometric_of_norm_lt_one 2 hnorm
    have h1 : Summable (fun j : ℕ => (j : ℝ) ^ 1 * (1 / 2) ^ j) :=
      summable_pow_mul_geometric_of_norm_lt_one 1 hnorm
    have h0 : Summable (fun j : ℕ => (1 / 2 : ℝ) ^ j) :=
      summable_geometric_of_lt_one (by norm_num) (by norm_num)
    have hsum : Summable (fun j : ℕ => ((j : ℝ) + 1) ^ 2 * (1 / 2) ^ j) := by
      have e : (fun j : ℕ => ((j : ℝ) + 1) ^ 2 * (1 / 2) ^ j)
          = (fun j : ℕ => (j : ℝ) ^ 2 * (1 / 2) ^ j + 2 * ((j : ℝ) ^ 1 * (1 / 2) ^ j)
              + 1 * (1 / 2) ^ j) := by
        funext j; ring
      rw [e]; exact (h2.add (h1.mul_left 2)).add (h0.mul_left 1)
    have hBsum' : Summable (fun j : ℕ => ((j : ℝ) + 1) ^ 2 * (1 / 2 : ℝ) ^ (j + 1)) := by
      have e : (fun j : ℕ => ((j : ℝ) + 1) ^ 2 * (1 / 2 : ℝ) ^ (j + 1))
          = (fun j : ℕ => (1 / 2) * (((j : ℝ) + 1) ^ 2 * (1 / 2) ^ j)) := by
        funext j; rw [pow_succ']; ring
      rw [e]; exact hsum.mul_left _
    exact hBsum'.congr (fun j => by rw [div_pow, one_pow, mul_one_div])
  set B := ∑' j : ℕ, ((j : ℝ) + 1) ^ 2 / 2 ^ (j + 1) with hBdef
  have hB0 : 0 ≤ B := tsum_nonneg (fun j => by positivity)
  -- choose `n₁ ≥ n₀` with `log(q n)² ≥ 2B` (since `log(q n) → ∞`)
  have hq_top : Filter.Tendsto (fun n : ℕ => (q n : ℝ)) Filter.atTop Filter.atTop :=
    Filter.tendsto_atTop_mono (fun n => by exact_mod_cast q_strictMono.le_apply)
      (tendsto_natCast_atTop_atTop (R := ℝ))
  have hlog_top : Filter.Tendsto (fun n : ℕ => Real.log (q n)) Filter.atTop Filter.atTop :=
    Real.tendsto_log_atTop.comp hq_top
  have hev := hlog_top.eventually_ge_atTop (2 * B + 1)
  rw [Filter.eventually_atTop] at hev
  obtain ⟨n₁', hn₁'⟩ := hev
  refine ⟨max n₁' n₀, fun n hn => ?_⟩
  have hloge : 2 * B + 1 ≤ Real.log (q n) := hn₁' n (le_trans (le_max_left _ _) hn)
  have hnn0 : n₀ ≤ n := le_trans (le_max_right _ _) hn
  have hlog1 : 1 ≤ Real.log (q n) := by linarith
  have hn2B : 2 * B ≤ Real.log (q n) ^ 2 := by
    nlinarith [hloge, hlog1, sq_nonneg (Real.log (q n) - 1)]
  -- pointwise bound on the `delta` summand
  have hfg : ∀ j : ℕ, (gap (n + 1 + j) : ℝ) / 2 ^ (j + 1)
      ≤ (2 * Cg * Real.log (q n) ^ 2) / 2 ^ (j + 1)
        + (2 * Cg) * (((j : ℝ) + 1) ^ 2 / 2 ^ (j + 1)) := by
    intro j
    have hden : (0 : ℝ) < 2 ^ (j + 1) := by positivity
    have hb1 : (gap (n + 1 + j) : ℝ) ≤ Cg * Real.log (q (n + 1 + j)) ^ 2 :=
      hB (n + 1 + j) (by omega)
    have hlog := log_q_shift_le n j
    have hlog0 : 0 ≤ Real.log (q (n + 1 + j)) :=
      Real.log_nonneg (by exact_mod_cast (q_prime _).one_lt.le)
    have hs0 : 0 ≤ Real.log (q n) :=
      Real.log_nonneg (by exact_mod_cast (q_prime _).one_lt.le)
    have hsq : Real.log (q (n + 1 + j)) ^ 2
        ≤ 2 * Real.log (q n) ^ 2 + 2 * ((j : ℝ) + 1) ^ 2 := by
      nlinarith [hlog, hlog0, hs0, sq_nonneg (Real.log (q n) - ((j : ℝ) + 1))]
    have hnum : (gap (n + 1 + j) : ℝ)
        ≤ 2 * Cg * Real.log (q n) ^ 2 + 2 * Cg * ((j : ℝ) + 1) ^ 2 :=
      calc (gap (n + 1 + j) : ℝ) ≤ Cg * Real.log (q (n + 1 + j)) ^ 2 := hb1
        _ ≤ Cg * (2 * Real.log (q n) ^ 2 + 2 * ((j : ℝ) + 1) ^ 2) :=
            mul_le_mul_of_nonneg_left hsq hCg0.le
        _ = 2 * Cg * Real.log (q n) ^ 2 + 2 * Cg * ((j : ℝ) + 1) ^ 2 := by ring
    rw [← mul_div_assoc, div_add_div_same, div_le_div_iff_of_pos_right hden]
    linarith [hnum]
  -- summability of the majorant and its tsum
  have hg1sum : Summable (fun j : ℕ => (2 * Cg * Real.log (q n) ^ 2) / 2 ^ (j + 1)) :=
    (hgeom.mul_left _).congr (fun j => mul_one_div _ _)
  have hg2sum : Summable (fun j : ℕ => (2 * Cg) * (((j : ℝ) + 1) ^ 2 / 2 ^ (j + 1))) :=
    hBsum.mul_left _
  have hg1tsum : ∑' j : ℕ, (2 * Cg * Real.log (q n) ^ 2) / 2 ^ (j + 1)
      = 2 * Cg * Real.log (q n) ^ 2 := by
    conv_rhs => rw [← tsum_geometric_two' (2 * Cg * Real.log (q n) ^ 2)]
    exact tsum_congr (fun j => by rw [div_div, ← pow_succ'])
  have hg2tsum : ∑' j : ℕ, (2 * Cg) * (((j : ℝ) + 1) ^ 2 / 2 ^ (j + 1)) = 2 * Cg * B := by
    rw [tsum_mul_left, ← hBdef]
  -- assemble
  have key : delta (n + 1) ≤ 2 * Cg * Real.log (q n) ^ 2 + 2 * Cg * B :=
    calc delta (n + 1) = ∑' j : ℕ, (gap (n + 1 + j) : ℝ) / 2 ^ (j + 1) := rfl
      _ ≤ ∑' j : ℕ, ((2 * Cg * Real.log (q n) ^ 2) / 2 ^ (j + 1)
            + (2 * Cg) * (((j : ℝ) + 1) ^ 2 / 2 ^ (j + 1))) :=
          tsum_le_tsum hfg (summable_gap_shift (n + 1)) (hg1sum.add hg2sum)
      _ = ∑' j : ℕ, (2 * Cg * Real.log (q n) ^ 2) / 2 ^ (j + 1)
            + ∑' j : ℕ, (2 * Cg) * (((j : ℝ) + 1) ^ 2 / 2 ^ (j + 1)) :=
          tsum_add hg1sum hg2sum
      _ = 2 * Cg * Real.log (q n) ^ 2 + 2 * Cg * B := by rw [hg1tsum, hg2tsum]
  have hBbound : 2 * Cg * B ≤ Cg * Real.log (q n) ^ 2 := by
    nlinarith [mul_le_mul_of_nonneg_left hn2B hCg0.le]
  linarith [key, hBbound]

/-! ## Section 5: the deletion construction -/

/-- Section 5: `K = ceil(log2(4 C_g) + 2 log2 ln x)`. -/
def cK (Cg : ℝ) (x : ℕ) : ℕ :=
  Nat.ceil (Real.logb 2 (4 * Cg) + 2 * Real.logb 2 (Real.log x))

/-- Section 5: `J = ceil(4 log2(K + 20))`. -/
def cJ (Cg : ℝ) (x : ℕ) : ℕ := Nat.ceil (4 * Real.logb 2 ((cK Cg x : ℝ) + 20))

/-- Section 5: `L = J + 2 + K`, the common word length. -/
def cL (J K : ℕ) : ℕ := J + 2 + K

/-- Section 5: the deletion index `i_0 = J + 1` (v1.1/F1; the v1.0 value
was `J + 2`). Interior with slack: `1 ≤ i_0` and `i_0 + 1 ≤ L` since
`J, K ≥ 1`. -/
def cI (J : ℕ) : ℕ := J + 1

/-- Section 5: `H_x = 4 C_g (ln x)^2`, the end-tail budget (`2^K ≥ H_x`;
consumed by FM-1 in section 6). -/
def tailBudget (Cg : ℝ) (x : ℕ) : ℝ := 4 * Cg * Real.log x ^ 2

/-- The index of the first prime exceeding `L + 3`: there are exactly
`Nat.count Nat.Prime (L+4)` primes `≤ L+3`, so `q` at this index is the
smallest prime `> L + 3`. -/
def primeIdxAbove (L : ℕ) : ℕ := Nat.count Nat.Prime (L + 4)

/-- Section 5: `q_j`, the `j`-th of the first `L+2` primes exceeding
`L+3` (`j = 0, ..., L+1`). Named `cprime` because `q` is taken by the
0-indexed prime enumeration of `Basic.lean`. -/
def cprime (L j : ℕ) : ℕ := q (primeIdxAbove L + j)

/-- Monotone enumeration of the section-5 point set
`A = {q_0, ..., q_{L+1}} \ {q_{i_0+1}}`: it is `q_t` for `t ≤ i_0` and
`q_{t+1}` beyond, i.e. it skips exactly `q_{i_0+1}`. The deletion IS this
`if`; `A` is not carried as a separate `Finset` (see the report's
definitional choices). `cElem J K 0 = q_0`, and `t` ranges over `0..L`. -/
def cElem (J K t : ℕ) : ℕ :=
  if t ≤ cI J then cprime (cL J K) t else cprime (cL J K) (t + 1)

/-- Monotone enumeration of `A' = {q_0, ..., q_{L+1}} \ {q_{i_0}}`:
`q_t` for `t < i_0` and `q_{t+1}` beyond, skipping exactly `q_{i_0}`. -/
def cElem' (J K t : ℕ) : ℕ :=
  if t < cI J then cprime (cL J K) t else cprime (cL J K) (t + 1)

/-- Section 5: the gap word `w` of `A`, 0-indexed, of length `L`. -/
def cword (J K : ℕ) (j : ℕ) : ℕ := cElem J K (j + 1) - cElem J K j

/-- Section 5: the gap word `w'` of `A'`, 0-indexed, of length `L`. -/
def cword' (J K : ℕ) (j : ℕ) : ℕ := cElem' J K (j + 1) - cElem' J K j

/-- Section 5: `gamma = q_{i_0+1} - q_{i_0}` (even). -/
def cgamma (J K : ℕ) : ℕ := cprime (cL J K) (cI J + 1) - cprime (cL J K) (cI J)

/-! ### Glue (PROVED, flagged) -/

/-- Bridge from `Nat.count` (computable) to `Nat.nth` (not), used only by
the smoke tests below. Flagged as glue in the traceability table. -/
theorem q_eq_of_count {n p : ℕ} (hp : p.Prime) (hc : Nat.count Nat.Prime p = n) :
    q n = p := by
  rw [q, ← hc, Nat.nth_count hp]

/-! ### Proof-layer helpers (item-0015; not statements) -/

/-- Strict monotonicity of the section-5 prime enumeration in its index:
`cprime L = q ∘ (primeIdxAbove L + ·)` and `q` is strictly monotone. -/
theorem cprime_lt_cprime (L : ℕ) {i j : ℕ} (h : i < j) :
    cprime L i < cprime L j := by
  unfold cprime
  exact q_strictMono (by omega)

/-- Every section-5 prime exceeds `L + 3`: `cprime L 0` is `q` at index
`Nat.count Nat.Prime (L+4)`, the least prime index whose value is `≥ L+4`
(`Nat.le_nth_count`), and `cprime L` is monotone in the index. -/
theorem cprime_gt (L j : ℕ) : L + 3 < cprime L j := by
  have h0 : L + 4 ≤ cprime L 0 := by
    have h := Nat.le_nth_count Nat.infinite_setOf_prime (L + 4)
    simpa [cprime, q, primeIdxAbove] using h
  have hmono : cprime L 0 ≤ cprime L j := by
    rcases Nat.eq_zero_or_pos j with rfl | hj
    · exact le_rfl
    · exact (cprime_lt_cprime L hj).le
  omega

/-- Telescoping prefix sum of the gap word of a strictly monotone
enumeration `e`: `∑_{i<j} (e (i+1) - e i) = e j - e 0`. -/
theorem psum_telescope {e : ℕ → ℕ} (he : Monotone e) (j : ℕ) :
    (∑ i ∈ Finset.range j, (e (i + 1) - e i)) = e j - e 0 := by
  induction j with
  | zero => simp
  | succ j ih =>
    rw [Finset.sum_range_succ, ih]
    have h1 : e 0 ≤ e j := he (Nat.zero_le j)
    have h2 : e j ≤ e (j + 1) := he (Nat.le_succ j)
    omega

/-- `cElem J K` is strictly monotone (each successive value is the next
prime or the one after, always increasing). -/
theorem cElem_strictMono (J K : ℕ) : StrictMono (cElem J K) := by
  intro a b hab
  simp only [cElem, cI]
  split_ifs <;> exact cprime_lt_cprime _ (by omega)

/-- `cElem' J K` is strictly monotone. -/
theorem cElem'_strictMono (J K : ℕ) : StrictMono (cElem' J K) := by
  intro a b hab
  simp only [cElem', cI]
  split_ifs <;> exact cprime_lt_cprime _ (by omega)

/-- Each `cElem` value is prime (it is a `q`-value). -/
theorem cElem_prime (J K t : ℕ) : (cElem J K t).Prime := by
  simp only [cElem, cprime]; split_ifs <;> exact q_prime _

/-- Each `cElem'` value is prime. -/
theorem cElem'_prime (J K t : ℕ) : (cElem' J K t).Prime := by
  simp only [cElem', cprime]; split_ifs <;> exact q_prime _

/-- Each `cElem` value exceeds `L + 3` where `L = cL J K`. -/
theorem cElem_gt (J K t : ℕ) : cL J K + 3 < cElem J K t := by
  simp only [cElem]; split_ifs <;> exact cprime_gt _ _

/-- Each `cElem'` value exceeds `L + 3`. -/
theorem cElem'_gt (J K t : ℕ) : cL J K + 3 < cElem' J K t := by
  simp only [cElem']; split_ifs <;> exact cprime_gt _ _

/-- Admissibility and cardinality of the point set of a gap word coming
from a strictly monotone prime enumeration `e` all of whose values exceed
`L + 3`. Both section-5 words are instances (`e = cElem` / `cElem'`).

Card: the point map `j ↦ e j - e 0` is strictly monotone, hence injective
on `range (L+1)`. Admissibility, `p` prime: if `L + 2 < p` then
`ν ≤ |H| = L+1 < p`; otherwise the residue class `-(e 0)` mod `p` is
unoccupied, because every point is `e j - e 0` with `e j` a prime `> p`,
so `(e j : ZMod p) ≠ 0`. -/
theorem wordPointSet_admissible {L : ℕ} {w e : ℕ → ℕ} (he : StrictMono e)
    (hw : ∀ j, w j = e (j + 1) - e j)
    (hep : ∀ t, (e t).Prime) (heg : ∀ t, L + 3 < e t) :
    IsAdmissible (wordPointSet w L) ∧ (wordPointSet w L).card = L + 1 := by
  have hfun : (fun j => ∑ i ∈ Finset.range j, w i) = (fun j => e j - e 0) := by
    funext j
    rw [show (∑ i ∈ Finset.range j, w i) = ∑ i ∈ Finset.range j, (e (i + 1) - e i) from
        Finset.sum_congr rfl (fun i _ => hw i)]
    exact psum_telescope he.monotone j
  have hset : wordPointSet w L
      = Finset.image (fun j => e j - e 0) (Finset.range (L + 1)) := by
    unfold wordPointSet; rw [hfun]
  have hm : StrictMono (fun j => e j - e 0) := by
    intro a b hab
    have hlt := he hab
    have h0 := he.monotone (Nat.zero_le a)
    simp only; omega
  have hcard : (wordPointSet w L).card = L + 1 := by
    rw [hset, Finset.card_image_of_injective _ hm.injective, Finset.card_range]
  refine ⟨?_, hcard⟩
  intro p hp
  unfold nuMod
  by_cases hpL : L + 2 < p
  · calc ((wordPointSet w L).image (Nat.cast : ℕ → ZMod p)).card
        ≤ (wordPointSet w L).card := Finset.card_image_le
      _ = L + 1 := hcard
      _ < p := by omega
  · push_neg at hpL
    haveI : Fact p.Prime := ⟨hp⟩
    haveI : NeZero p := ⟨hp.pos.ne'⟩
    have hp0 : 0 < p := hp.pos
    have hmiss : (-(e 0 : ZMod p)) ∉ (wordPointSet w L).image (Nat.cast : ℕ → ZMod p) := by
      rw [Finset.mem_image]
      rintro ⟨x, hxH, hx⟩
      rw [hset, Finset.mem_image] at hxH
      obtain ⟨j, _, rfl⟩ := hxH
      have hge : e 0 ≤ e j := he.monotone (Nat.zero_le j)
      rw [Nat.cast_sub hge] at hx
      have hzero : (e j : ZMod p) = 0 := by linear_combination hx
      have hdvd : p ∣ e j := (ZMod.natCast_zmod_eq_zero_iff_dvd (e j) p).mp hzero
      rcases (hep j).eq_one_or_self_of_dvd p hdvd with h1 | h1
      · exact hp.ne_one h1
      · have := heg j; omega
    have hsub : (wordPointSet w L).image (Nat.cast : ℕ → ZMod p)
        ⊆ Finset.univ.erase (-(e 0 : ZMod p)) := by
      intro y hy
      rw [Finset.mem_erase]
      exact ⟨fun h => hmiss (h ▸ hy), Finset.mem_univ y⟩
    have hle := Finset.card_le_card hsub
    rw [Finset.card_erase_of_mem (Finset.mem_univ _), Finset.card_univ, ZMod.card] at hle
    omega

/-! ### Section 5 property lemmata -/

/-- Section 5(i), prefix: `w` and `w'` share the length-`J` prefix. -/
theorem cword_prefix (J K : ℕ) (hJ : 1 ≤ J) (hK : 1 ≤ K) :
    ∀ j < J, cword J K j = cword' J K j := by
  intro j hj
  simp only [cword, cword', cElem, cElem', cI]
  split_ifs <;> omega

/-- Section 5(i), fork: the middle two entries differ by
`(-gamma, +gamma)` in the NATURAL order `(w, w')`. Section 6 swaps the
names to obtain FM-F's `(+gamma, -gamma)` orientation; the signs are not
"fixed" here (v1.2, re-review R2). -/
theorem cword_fork (J K : ℕ) (hJ : 1 ≤ J) (hK : 1 ≤ K) :
    cword J K J + cgamma J K = cword' J K J ∧
      cword J K (J + 1) = cword' J K (J + 1) + cgamma J K := by
  have mA : cprime (cL J K) J < cprime (cL J K) (J + 1) := cprime_lt_cprime _ (by omega)
  have mB : cprime (cL J K) (J + 1) < cprime (cL J K) (J + 1 + 1) := cprime_lt_cprime _ (by omega)
  have mC : cprime (cL J K) (J + 1 + 1) < cprime (cL J K) (J + 1 + 1 + 1) := cprime_lt_cprime _ (by omega)
  refine ⟨?_, ?_⟩ <;>
    · simp only [cword, cword', cgamma, cElem, cElem', cI]
      split_ifs <;> omega

/-- Section 5(i), suffix: `w` and `w'` share the length-`K` suffix, i.e.
the entries at word positions `J+2, ..., L-1`. -/
theorem cword_suffix (J K : ℕ) (hJ : 1 ≤ J) (hK : 1 ≤ K) :
    ∀ i < K, cword J K (J + 2 + i) = cword' J K (J + 2 + i) := by
  intro i hi
  simp only [cword, cword', cElem, cElem', cI]
  split_ifs <;> omega

/-- Section 5(ii): both 0-based point sets are admissible -- for
`p ≤ L+2` the residue class of 0 is unoccupied before translation (all
`q_j > L+3 > p`), and for `p > L+2` there are only `L+1 < p` points --
together with section 5(iv)'s "the words have `L + 1` points". -/
theorem cword_admissible (J K : ℕ) (hJ : 1 ≤ J) (hK : 1 ≤ K) :
    (IsAdmissible (wordPointSet (cword J K) (cL J K)) ∧
        (wordPointSet (cword J K) (cL J K)).card = cL J K + 1) ∧
      (IsAdmissible (wordPointSet (cword' J K) (cL J K)) ∧
        (wordPointSet (cword' J K) (cL J K)).card = cL J K + 1) := by
  refine ⟨wordPointSet_admissible (cElem_strictMono J K) (fun j => rfl)
      (cElem_prime J K) (cElem_gt J K),
    wordPointSet_admissible (cElem'_strictMono J K) (fun j => rfl)
      (cElem'_prime J K) (cElem'_gt J K)⟩

/-- Section 5(iii): `span ≤ q_{L+1} - q_0 ≤ C_1 L ln L` with `C_1 ≥ 1`
fixed (Chebyshev upper bound on `p_{2L+4}`; classical), hence
`gamma ≤ C_1 L ln L`. The last two clauses are the span hypothesis of
Lemma 4.3 in the shape that lemma consumes; the assembly instantiates
`κ := C_1` (legitimate since `ln L ≤ ln (L+2)`). -/
theorem cspan_le :
    ∃ C₁ : ℝ, 1 ≤ C₁ ∧ ∀ J K : ℕ, 1 ≤ J → 1 ≤ K →
      ((cprime (cL J K) (cL J K + 1) : ℝ) - (cprime (cL J K) 0 : ℝ)
          ≤ C₁ * (cL J K : ℝ) * Real.log (cL J K)) ∧
        ((cgamma J K : ℝ) ≤ C₁ * (cL J K : ℝ) * Real.log (cL J K)) ∧
        ((offsetSpan (wordPointSet (cword J K) (cL J K)) : ℝ)
          ≤ C₁ * (cL J K : ℝ) * Real.log ((cL J K : ℝ) + 2)) ∧
        ((offsetSpan (wordPointSet (cword' J K) (cL J K)) : ℝ)
          ≤ C₁ * (cL J K : ℝ) * Real.log ((cL J K : ℝ) + 2)) := by
  sorry

/-- Section 5(iii), the limit: `(gamma + 4)/2^J ≤ 3 C_1/(K+20)^2 → 0`,
using `L ≤ 2(K+20)` and `ln L ≤ K+20` for large `x`. Stated in the shape
`SmallTailForkMerge`'s (FM-2) consumes. -/
theorem cfm2_tendsto {Cg : ℝ} (hCg : 1 ≤ Cg) :
    Filter.Tendsto
      (fun x : ℕ => ((cgamma (cJ Cg x) (cK Cg x) : ℝ) + 4) / 2 ^ cJ Cg x)
      Filter.atTop (nhds 0) := by
  sorry

/-- Section 5 "Fix x large" together with section 5(iv) (budgets):
eventually `J, K ≥ 1` (which section 5 needs for `i_0` to be interior),
`2^K ≥ H_x` (the parenthetical of the section-5 display, consumed by
FM-1), `L + 1 < 3 lnln x`, Lemma 4.3's window `L + 1 ≤ 4 lnln x - 1`, the
one-point extension window `L + 2 ≤ 4 lnln x`, and `span ≤ (ln x)^3`
(the operative span bound is 5(iii)). The asymptotic
`L + 1 = (2/ln 2) lnln x + O(lnlnln x)` of 5(iv) is prose and is not
transcribed; the `< 3 lnln x` clause is its operative content. -/
theorem cbudget {Cg : ℝ} (hCg : 1 ≤ Cg) :
    ∃ x₀ : ℕ, ∀ x : ℕ, x₀ ≤ x →
      1 ≤ cJ Cg x ∧ 1 ≤ cK Cg x ∧
      tailBudget Cg x ≤ 2 ^ cK Cg x ∧
      ((cL (cJ Cg x) (cK Cg x) : ℝ) + 1 < 3 * Real.log (Real.log x)) ∧
      ((cL (cJ Cg x) (cK Cg x) : ℝ) + 1 ≤ 4 * Real.log (Real.log x) - 1) ∧
      ((cL (cJ Cg x) (cK Cg x) : ℝ) + 2 ≤ 4 * Real.log (Real.log x)) ∧
      ((offsetSpan (wordPointSet (cword (cJ Cg x) (cK Cg x)) (cL (cJ Cg x) (cK Cg x))) : ℝ)
        ≤ Real.log x ^ 3) ∧
      ((offsetSpan (wordPointSet (cword' (cJ Cg x) (cK Cg x)) (cL (cJ Cg x) (cK Cg x))) : ℝ)
        ≤ Real.log x ^ 3) := by
  sorry

/-- The chain down to the consecutive count being at least 1: Lemma 4.3
applied to the section-5 words, with `κ := C_1` from 5(iii) and the
budgets of 5(ii)/5(iv). This is the entry point section 6 uses to produce
the two fork-merge anchors `n_x`, `m_x`. -/
theorem constr_consCount_pos (hA : HLQuantA) {Cg : ℝ} (hCg : 1 ≤ Cg) :
    ∃ x₀ : ℕ, ∀ x : ℕ, x₀ ≤ x →
      1 ≤ consCount (cword (cJ Cg x) (cK Cg x)) (cL (cJ Cg x) (cK Cg x)) x ∧
        1 ≤ consCount (cword' (cJ Cg x) (cK Cg x)) (cL (cJ Cg x) (cK Cg x)) x := by
  sorry

/-! ### Smoke tests (ENCOURAGED by the kickoff; review-verified tables)

`(J, K) = (3, 4)`: `L = 9`, `i_0 = 4`, `q_0..q_{L+1} = 13, 17, 19, 23,
29, 31, 37, 41, 43, 47, 53`; `gamma = 2`, prefix `(4, 2, 4)`, suffix
`(4, 2, 4, 6)`. `(J, K) = (2, 3)`: `gamma = 4`. Proved by `decide` /
`norm_num` / `rw`; no `native_decide` (axiom gate). -/

example : cgamma 3 4 = 2 := by
  have h9 : q 9 = 29 := q_eq_of_count (by norm_num) (by decide)
  have h10 : q 10 = 31 := q_eq_of_count (by norm_num) (by decide)
  simp only [cgamma, cprime, cL, cI, primeIdxAbove, show Nat.count Nat.Prime 13 = 5 by decide]
  norm_num [h9, h10]

example : cgamma 2 3 = 4 := by
  have h7 : q 7 = 19 := q_eq_of_count (by norm_num) (by decide)
  have h8 : q 8 = 23 := q_eq_of_count (by norm_num) (by decide)
  simp only [cgamma, cprime, cL, cI, primeIdxAbove, show Nat.count Nat.Prime 11 = 4 by decide]
  norm_num [h7, h8]

/-- Prefix table at `(J, K) = (3, 4)`: `w` starts `(4, 2, 4)`. -/
example : cword 3 4 0 = 4 ∧ cword 3 4 1 = 2 ∧ cword 3 4 2 = 4 := by
  have h5 : q 5 = 13 := q_eq_of_count (by norm_num) (by decide)
  have h6 : q 6 = 17 := q_eq_of_count (by norm_num) (by decide)
  have h7 : q 7 = 19 := q_eq_of_count (by norm_num) (by decide)
  have h8 : q 8 = 23 := q_eq_of_count (by norm_num) (by decide)
  refine ⟨?_, ?_, ?_⟩ <;>
    simp only [cword, cElem, cI, cprime, cL, primeIdxAbove,
      show Nat.count Nat.Prime 13 = 5 by decide] <;>
    norm_num [h5, h6, h7, h8]

/-- Suffix table at `(J, K) = (3, 4)`: `w` ends `(4, 2, 4, 6)` at word
positions `J+2, ..., L-1 = 5, ..., 8`. -/
example : cword 3 4 5 = 4 ∧ cword 3 4 6 = 2 ∧ cword 3 4 7 = 4 ∧ cword 3 4 8 = 6 := by
  have h11 : q 11 = 37 := q_eq_of_count (by norm_num) (by decide)
  have h12 : q 12 = 41 := q_eq_of_count (by norm_num) (by decide)
  have h13 : q 13 = 43 := q_eq_of_count (by norm_num) (by decide)
  have h14 : q 14 = 47 := q_eq_of_count (by norm_num) (by decide)
  have h15 : q 15 = 53 := q_eq_of_count (by norm_num) (by decide)
  refine ⟨?_, ?_, ?_, ?_⟩ <;>
    simp only [cword, cElem, cI, cprime, cL, primeIdxAbove,
      show Nat.count Nat.Prime 13 = 5 by decide] <;>
    norm_num [h11, h12, h13, h14, h15]

end

end Erdos251
