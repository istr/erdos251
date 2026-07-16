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

/-! ### Proof-layer helpers for Lemma 4.1 (item-0015; not statements)

The Mertens-free route of session 3: split the Euler product at
`P₀ = 2|H|`. The head is controlled by `primorial_le_4_pow` (no Mertens),
the tail by the ONE-SIDED sibling of `abs_log_singularFactor_le` in which
the linear terms cancel one-sidedly under `ν ≤ |H|` (no span condition).
-/

/-- HEAD (`p ≤ P₀`): admissibility gives `ν ≤ p-1`, hence `1 - ν/p ≥ 1/p`;
`(1-1/p)^k ≤ 1` only helps, so the factor is `≥ 1/p` and its log `≥ -log p`.
No span condition. -/
theorem log_singularFactor_head_ge {H : Finset ℕ} (hH : IsAdmissible H) (p : Nat.Primes) :
    -Real.log ((p : ℕ) : ℝ)
      ≤ Real.log ((1 - (nuMod H (p : ℕ) : ℝ) / ((p : ℕ) : ℝ)) /
          (1 - 1 / ((p : ℕ) : ℝ)) ^ H.card) := by
  have hp : (p : ℕ).Prime := p.2
  set P : ℝ := ((p : ℕ) : ℝ) with hPdef
  have hP2 : (2:ℝ) ≤ P := by rw [hPdef]; exact_mod_cast hp.two_le
  have hP0 : (0:ℝ) < P := by linarith
  have hnu : (nuMod H (p:ℕ) : ℝ) + 1 ≤ P := by
    have h : nuMod H (p:ℕ) < (p:ℕ) := hH _ hp
    rw [hPdef]; exact_mod_cast h
  have hden0 : (0:ℝ) < 1 - 1 / P := by rw [sub_pos, div_lt_one hP0]; linarith
  have hden1 : (1 - 1 / P) ^ H.card ≤ 1 :=
    pow_le_one₀ hden0.le (by have : (0:ℝ) < 1 / P := by positivity
                             linarith)
  have hdenpow : (0:ℝ) < (1 - 1 / P) ^ H.card := by positivity
  have hnum : (1:ℝ) / P ≤ 1 - (nuMod H (p:ℕ) : ℝ) / P := by
    rw [le_sub_iff_add_le, div_add_div_same, div_le_one hP0]
    linarith
  have hfac : (1:ℝ) / P ≤ (1 - (nuMod H (p:ℕ) : ℝ) / P) / (1 - 1 / P) ^ H.card := by
    rw [le_div_iff₀ hdenpow]
    have h1 : (1:ℝ) / P * (1 - 1 / P) ^ H.card ≤ 1 / P * 1 :=
      mul_le_mul_of_nonneg_left hden1 (by positivity)
    linarith
  have := Real.log_le_log (by positivity : (0:ℝ) < 1 / P) hfac
  rwa [Real.log_div one_ne_zero (ne_of_gt hP0), Real.log_one, zero_sub] at this

/-- TAIL (`p > 2|H|`): the ONE-SIDED sibling of `abs_log_singularFactor_le`
with `ν ≤ |H|` in place of `ν = |H|`, valid for ALL `p > 2|H|` with NO span
condition (and no admissibility). The linear terms cancel one-sidedly:
`log(1-ν/p) - k log(1-1/p) ≥ log(1-k/p) + k/p ≥ -2(k/p)²`. -/
theorem log_singularFactor_tail_ge {H : Finset ℕ} (p : Nat.Primes)
    (hlarge : 2 * H.card < (p : ℕ)) :
    -(2 * (H.card : ℝ) ^ 2 * (1 / ((p : ℕ) : ℝ) ^ 2))
      ≤ Real.log ((1 - (nuMod H (p : ℕ) : ℝ) / ((p : ℕ) : ℝ)) /
          (1 - 1 / ((p : ℕ) : ℝ)) ^ H.card) := by
  have hp : (p : ℕ).Prime := p.2
  set P : ℝ := ((p : ℕ) : ℝ) with hPdef
  set k : ℝ := (H.card : ℝ) with hkdef
  have hP2 : (2:ℝ) ≤ P := by rw [hPdef]; exact_mod_cast hp.two_le
  have hP0 : (0:ℝ) < P := by linarith
  have hk0 : (0:ℝ) ≤ k := Nat.cast_nonneg _
  have h2kR : 2 * k < P := by rw [hkdef, hPdef]; exact_mod_cast hlarge
  -- `ν ≤ |H|` unconditionally (no admissibility, no span)
  have hnu : (nuMod H (p:ℕ) : ℝ) ≤ k := by
    rw [hkdef]; exact_mod_cast Finset.card_image_le
  have hnu0 : (0:ℝ) ≤ (nuMod H (p:ℕ) : ℝ) := Nat.cast_nonneg _
  have hkP : k / P < 1 / 2 := by rw [div_lt_div_iff₀ hP0 (by norm_num)]; linarith
  have hkP0 : (0:ℝ) ≤ k / P := by positivity
  have hnumk : (0:ℝ) < 1 - k / P := by linarith
  have hnumnu : (0:ℝ) < 1 - (nuMod H (p:ℕ) : ℝ) / P := by
    have : (nuMod H (p:ℕ) : ℝ) / P ≤ k / P := by gcongr
    linarith
  have hden0 : (0:ℝ) < 1 - 1 / P := by rw [sub_pos, div_lt_one hP0]; linarith
  -- split the log
  rw [Real.log_div (ne_of_gt hnumnu) (by positivity), Real.log_pow]
  -- (a) numerator: monotone in `ν ≤ k`
  have hA : Real.log (1 - k / P) ≤ Real.log (1 - (nuMod H (p:ℕ) : ℝ) / P) := by
    apply Real.log_le_log hnumk
    have : (nuMod H (p:ℕ) : ℝ) / P ≤ k / P := by gcongr
    linarith
  -- (b) denominator: `-log(1-1/p) ≥ 1/p`
  have hB : Real.log (1 - 1 / P) ≤ -(1 / P) := by
    have := Real.log_le_sub_one_of_pos hden0; linarith
  -- (c) quadratic control of the surviving `log(1-k/P) + k/P`
  have hx : |k / P| ≤ 1/2 := by rw [abs_of_nonneg hkP0]; linarith
  have hC := abs_add_log_one_sub_le hx
  have hC' : -(2 * (k / P) ^ 2) ≤ k / P + Real.log (1 - k / P) := (abs_le.mp hC).1
  have hsq : 2 * (k / P) ^ 2 = 2 * k ^ 2 * (1 / P ^ 2) := by field_simp
  have hkB : k * (1 / P) ≤ k * (-(Real.log (1 - 1 / P))) :=
    mul_le_mul_of_nonneg_left (by linarith) hk0
  have hkPeq : k * (1 / P) = k / P := by ring
  rw [← hsq]
  linarith [hA, hC', hkB, hkPeq]

/-- The head Finset: the primes `≤ N`, as a `Finset Nat.Primes`. -/
def primesLe (N : ℕ) : Finset Nat.Primes := (finite_primes_le N).toFinset

theorem mem_primesLe {N : ℕ} {p : Nat.Primes} : p ∈ primesLe N ↔ (p : ℕ) ≤ N := by
  simp [primesLe, finite_primes_le]

/-- The head Finset coerces onto mathlib's primorial index set. -/
theorem primesLe_image (N : ℕ) :
    (primesLe N).image (fun p : Nat.Primes => (p : ℕ))
      = (Finset.range (N + 1)).filter Nat.Prime := by
  ext n
  simp only [Finset.mem_image, Finset.mem_filter, Finset.mem_range, mem_primesLe]
  constructor
  · rintro ⟨p, hp, rfl⟩; exact ⟨by omega, p.2⟩
  · rintro ⟨hn, hnp⟩; exact ⟨⟨n, hnp⟩, by simp [mem_primesLe]; omega, rfl⟩

/-- `∏_{p ≤ N} p = N#`. -/
theorem prod_primesLe (N : ℕ) : ∏ p ∈ primesLe N, (p : ℕ) = primorial N := by
  have h : ∏ p ∈ (primesLe N).image (fun p : Nat.Primes => (p : ℕ)), p
      = ∏ p ∈ primesLe N, (p : ℕ) :=
    Finset.prod_image (fun a _ b _ h => Subtype.ext h)
  rw [← h, primesLe_image, primorial]

/-- HEAD SUM: `∑_{p ≤ N} log p = log N# ≤ N log 4` (`primorial_le_4_pow`). No Mertens. -/
theorem sum_log_primesLe_le (N : ℕ) :
    ∑ p ∈ primesLe N, Real.log ((p : ℕ) : ℝ) ≤ (N : ℝ) * Real.log 4 := by
  have hprod : ∑ p ∈ primesLe N, Real.log ((p : ℕ) : ℝ)
      = Real.log ((primorial N : ℕ) : ℝ) := by
    rw [← prod_primesLe N]
    push_cast
    rw [Real.log_prod]
    intro p _
    have : (0:ℝ) < ((p : ℕ) : ℝ) := by exact_mod_cast p.2.pos
    exact ne_of_gt this
  rw [hprod]
  have h4 : primorial N ≤ 4 ^ N := primorial_le_4_pow N
  have h4R : ((primorial N : ℕ) : ℝ) ≤ (4:ℝ) ^ N := by exact_mod_cast h4
  calc Real.log ((primorial N : ℕ) : ℝ) ≤ Real.log ((4:ℝ) ^ N) :=
        Real.log_le_log (by exact_mod_cast (primorial_pos N)) h4R
    _ = (N : ℝ) * Real.log 4 := by rw [Real.log_pow]

/-- TAIL SUM: `∑_{p > N} 1/p² ≤ 1/N`, by comparison with `∑_{n > N} 1/n²`
along the (injective) prime-to-ℕ map (`sum_Ioc_inv_sq_le_sub`). Integral-free. -/
theorem tsum_compl_primesLe_inv_sq_le {N : ℕ} (hN : N ≠ 0) :
    ∑' p : ↑((primesLe N : Finset Nat.Primes) : Set Nat.Primes)ᶜ,
        (1 / (((p : Nat.Primes) : ℕ) : ℝ) ^ 2) ≤ 1 / (N : ℝ) := by
  have hNR : (0:ℝ) < (N : ℝ) := by exact_mod_cast Nat.pos_of_ne_zero hN
  refine tsum_le_of_sum_le (summable_one_div_prime_sq.subtype _) (fun T => ?_)
  -- explicitly typed to avoid the subtype-coercion elaboration trap
  let φ : ↑((primesLe N : Finset Nat.Primes) : Set Nat.Primes)ᶜ → ℕ := fun p => (p.1 : ℕ)
  have hgt : ∀ p : ↑((primesLe N : Finset Nat.Primes) : Set Nat.Primes)ᶜ, N < φ p := by
    intro p
    have h := p.2
    rw [Set.mem_compl_iff, Finset.mem_coe, mem_primesLe] at h
    simp only [φ]
    omega
  have hginj : ∀ x ∈ T, ∀ y ∈ T, φ x = φ y → x = y := by
    intro x _ y _ h
    exact Subtype.ext (Subtype.ext h)
  set T' : Finset ℕ := Finset.image φ T with hT'
  have hsum : ∑ p ∈ T, (1 / (((p : Nat.Primes) : ℕ) : ℝ) ^ 2)
      = ∑ n ∈ T', (1 / (n : ℝ) ^ 2) := by
    rw [hT', Finset.sum_image hginj]
  rw [hsum]
  rcases T'.eq_empty_or_nonempty with hE | hNE
  · rw [hE, Finset.sum_empty]; positivity
  · set M := T'.sup id with hM
    have hmemN : ∀ n ∈ T', N < n ∧ n ≤ M := by
      intro n hn
      refine ⟨?_, Finset.le_sup (f := id) hn⟩
      rw [hT', Finset.mem_image] at hn
      obtain ⟨p, _, rfl⟩ := hn
      exact hgt p
    have hsub : T' ⊆ Finset.Ioc N M := fun n hn => Finset.mem_Ioc.mpr (hmemN n hn)
    have hNM : N ≤ M := by
      obtain ⟨n, hn⟩ := hNE
      have := hmemN n hn; omega
    calc ∑ n ∈ T', (1 / (n : ℝ) ^ 2) ≤ ∑ n ∈ Finset.Ioc N M, (1 / (n : ℝ) ^ 2) :=
          Finset.sum_le_sum_of_subset_of_nonneg hsub (fun i _ _ => by positivity)
      _ = ∑ n ∈ Finset.Ioc N M, (((n : ℝ) ^ 2)⁻¹) :=
          Finset.sum_congr rfl (fun i _ => one_div _)
      _ ≤ ((N:ℝ))⁻¹ - ((M:ℝ))⁻¹ := sum_Ioc_inv_sq_le_sub hN hNM
      _ ≤ 1 / (N : ℝ) := by
          rw [one_div]
          have : (0:ℝ) ≤ ((M:ℝ))⁻¹ := by positivity
          linarith

/-- The `k = 0` corner: `0 ∈ H` and `|H| = 1` force `H = {0}`, where every
local factor is `(1-1/p)/(1-1/p)^1 = 1`, so `S = 1`. This is EXACTLY the
target at `k = 0` (`exp(-C·0·log 2) = 1`), so the corner cannot be absorbed
into the generic bound -- it needs equality. -/
theorem singularSeries_singleton_zero : singularSeries {0} = 1 := by
  rw [singularSeries]
  have h : ∀ p : Nat.Primes,
      (1 - (nuMod {0} (p : ℕ) : ℝ) / ((p : ℕ) : ℝ)) /
        (1 - 1 / ((p : ℕ) : ℝ)) ^ ({0} : Finset ℕ).card = 1 := by
    intro p
    have hp : (p : ℕ).Prime := p.2
    have hP2 : (2:ℝ) ≤ ((p : ℕ) : ℝ) := by exact_mod_cast hp.two_le
    have hden : (0:ℝ) < 1 - 1 / ((p : ℕ) : ℝ) := by
      rw [sub_pos, div_lt_one (by linarith)]; linarith
    have hnu : nuMod {0} (p : ℕ) = 1 := by
      unfold nuMod; simp
    rw [hnu]
    simp only [Finset.card_singleton, pow_one, Nat.cast_one]
    rw [div_self (ne_of_gt hden)]
  rw [tprod_congr h, tprod_one]

/-- T1 CLAUSE 1 (the real content), Mertens-free. Head `p ≤ 2|H|`:
`≥ 1/primorial(2|H|) ≥ 4^{-2|H|}`. Tail `p > 2|H|`: one-sided linear
cancellation, `≥ -2|H|² ∑_{p>2|H|} 1/p² ≥ -|H|`. Explicit constant `C = 10`. -/
theorem singularSeries_ge_exp {H : Finset ℕ} (h0 : 0 ∈ H) (hH : IsAdmissible H) :
    Real.exp (-(12 * ((H.card : ℝ) - 1) * Real.log ((H.card : ℝ) + 1)))
      ≤ singularSeries H := by
  have hne : H.Nonempty := ⟨0, h0⟩
  have hcard1 : 1 ≤ H.card := Finset.card_pos.mpr hne
  rcases Nat.lt_or_ge H.card 2 with hc1 | hc2
  · -- k = 0 corner: H = {0}
    have hc : H.card = 1 := by omega
    have hH0 : H = {0} := by
      obtain ⟨a, ha⟩ := Finset.card_eq_one.mp hc
      rw [ha] at h0 ⊢
      rw [Finset.mem_singleton] at h0
      rw [h0]
    rw [hH0, singularSeries_singleton_zero]
    rw [hH0] at hc
    rw [hc]
    norm_num
  · -- k ≥ 1: the generic bound
    set P₀ := 2 * H.card with hP₀
    have hP₀0 : P₀ ≠ 0 := by omega
    rw [singularSeries,
      ← Real.rexp_tsum_eq_tprod _ (singularFactor_pos hH) summable_log_singularFactor]
    apply Real.exp_le_exp.mpr
    rw [← sum_add_tsum_compl (s := primesLe P₀) summable_log_singularFactor]
    -- HEAD: `≥ -log(primorial P₀) ≥ -P₀ log 4`
    have hhead : -((P₀:ℝ) * Real.log 4)
        ≤ ∑ p ∈ primesLe P₀, Real.log ((1 - (nuMod H (p : ℕ) : ℝ) / ((p : ℕ) : ℝ)) /
            (1 - 1 / ((p : ℕ) : ℝ)) ^ H.card) := by
      calc -((P₀:ℝ) * Real.log 4) ≤ -(∑ p ∈ primesLe P₀, Real.log ((p:ℕ):ℝ)) := by
            linarith [sum_log_primesLe_le P₀]
        _ = ∑ p ∈ primesLe P₀, (-Real.log ((p:ℕ):ℝ)) := by rw [Finset.sum_neg_distrib]
        _ ≤ _ := Finset.sum_le_sum (fun p _ => log_singularFactor_head_ge hH p)
    -- TAIL: one-sided cancellation, `≥ -2|H|² · (1/P₀) = -|H|`
    have htail : -((H.card : ℝ))
        ≤ ∑' p : ↑((primesLe P₀ : Finset Nat.Primes) : Set Nat.Primes)ᶜ,
            Real.log ((1 - (nuMod H ((p : Nat.Primes) : ℕ) : ℝ) / (((p : Nat.Primes) : ℕ) : ℝ)) /
              (1 - 1 / (((p : Nat.Primes) : ℕ) : ℝ)) ^ H.card) := by
      have hsummin : Summable (fun p : ↑((primesLe P₀ : Finset Nat.Primes) : Set Nat.Primes)ᶜ =>
          -(2 * (H.card:ℝ)^2 * (1 / (((p : Nat.Primes) : ℕ) : ℝ)^2))) :=
        ((summable_one_div_prime_sq.subtype _).mul_left _).neg
      have hpt : ∀ p : ↑((primesLe P₀ : Finset Nat.Primes) : Set Nat.Primes)ᶜ,
          -(2 * (H.card:ℝ)^2 * (1 / (((p : Nat.Primes) : ℕ) : ℝ)^2))
            ≤ Real.log ((1 - (nuMod H ((p : Nat.Primes) : ℕ) : ℝ) / (((p : Nat.Primes) : ℕ) : ℝ)) /
              (1 - 1 / (((p : Nat.Primes) : ℕ) : ℝ)) ^ H.card) := by
        intro p
        apply log_singularFactor_tail_ge
        have h := p.2
        rw [Set.mem_compl_iff, Finset.mem_coe, mem_primesLe] at h
        omega
      have hcard0 : (0:ℝ) ≤ 2 * (H.card:ℝ)^2 := by positivity
      have hkey : ∑' p : ↑((primesLe P₀ : Finset Nat.Primes) : Set Nat.Primes)ᶜ,
          -(2 * (H.card:ℝ)^2 * (1 / (((p : Nat.Primes) : ℕ) : ℝ)^2))
            = -(2 * (H.card:ℝ)^2 * ∑' p : ↑((primesLe P₀ : Finset Nat.Primes) : Set Nat.Primes)ᶜ,
                (1 / (((p : Nat.Primes) : ℕ) : ℝ)^2)) := by
        rw [tsum_neg, tsum_mul_left]
      have hP₀R : ((P₀:ℕ):ℝ) = 2 * (H.card:ℝ) := by rw [hP₀]; push_cast; ring
      calc -((H.card : ℝ)) = -(2 * (H.card:ℝ)^2 * (1 / ((P₀:ℕ):ℝ))) := by
            rw [hP₀R]
            have : (0:ℝ) < (H.card:ℝ) := by exact_mod_cast hcard1
            field_simp
            ring
        _ ≤ -(2 * (H.card:ℝ)^2 * ∑' p : ↑((primesLe P₀ : Finset Nat.Primes) : Set Nat.Primes)ᶜ,
                (1 / (((p : Nat.Primes) : ℕ) : ℝ)^2)) := by
            have := tsum_compl_primesLe_inv_sq_le (N := P₀) hP₀0
            nlinarith [this, hcard0]
        _ = ∑' p : ↑((primesLe P₀ : Finset Nat.Primes) : Set Nat.Primes)ᶜ,
              -(2 * (H.card:ℝ)^2 * (1 / (((p : Nat.Primes) : ℕ) : ℝ)^2)) := hkey.symm
        _ ≤ _ := tsum_le_tsum hpt hsummin (summable_log_singularFactor.subtype _)
    -- the constant: `10 (k) log(k+2) ≥ 2(k+1) log 4 + (k+1)` for `k ≥ 1`
    have harith : -(12 * ((H.card : ℝ) - 1) * Real.log ((H.card : ℝ) + 1))
        ≤ -((P₀:ℝ) * Real.log 4) + -((H.card : ℝ)) := by
      have hc2R : (2:ℝ) ≤ (H.card:ℝ) := by exact_mod_cast hc2
      have hl2 : (0.69:ℝ) < Real.log 2 := by linarith [Real.log_two_gt_d9]
      have hlog4 : Real.log 4 = 2 * Real.log 2 := by
        rw [show (4:ℝ) = 2^2 by norm_num, Real.log_pow]; push_cast; ring
      have hlogc : Real.log 2 ≤ Real.log ((H.card:ℝ) + 1) :=
        Real.log_le_log (by norm_num) (by linarith)
      have hP₀R : ((P₀:ℕ):ℝ) = 2 * (H.card:ℝ) := by rw [hP₀]; push_cast; ring
      rw [hP₀R, hlog4]
      nlinarith [hlogc, hl2, hc2R,
        mul_nonneg (by linarith : (0:ℝ) ≤ (H.card:ℝ) - 1)
          (by linarith : (0:ℝ) ≤ Real.log ((H.card:ℝ) + 1) - Real.log 2),
        mul_nonneg (by linarith : (0:ℝ) ≤ (H.card:ℝ) - 2)
          (by linarith : (0:ℝ) ≤ Real.log 2 - 0.69)]
    linarith [hhead, htail, harith]

/-- The clause-2 bridge: `exp(-k·lnln x) = (ln x)^{-k}` for `ln x > 0`. -/
theorem exp_neg_card_loglog {x : ℕ} (hx : (0:ℝ) < Real.log x) (k : ℕ) :
    Real.exp (-((k : ℝ) * Real.log (Real.log x))) = (Real.log x ^ k)⁻¹ := by
  rw [← Real.rpow_natCast (Real.log x) k, ← Real.rpow_neg hx.le, Real.rpow_def_of_pos hx]
  ring_nf

/-- T1 CLAUSE 2: clause 1 plus algebra. `M_H(x) = S(H)·x/(ln x)^{|H|}` and
`exp(-|H|·lnln x) = (ln x)^{-|H|}`, so the claim reduces to clause 1 pointwise.
Threshold `x₀ = 3` (only `ln x > 0` is needed). -/
theorem modelMass_ge_exp {x : ℕ} (hx : 3 ≤ x) {H : Finset ℕ} (h0 : 0 ∈ H)
    (hH : IsAdmissible H) :
    (x : ℝ) * Real.exp (-(12 * ((H.card : ℝ) - 1) * Real.log ((H.card : ℝ) + 1))
        - (H.card : ℝ) * Real.log (Real.log x))
      ≤ modelMass H x := by
  have hx1 : (1:ℝ) < (x:ℝ) := by
    have : (3:ℕ) ≤ x := hx
    have : (3:ℝ) ≤ (x:ℝ) := by exact_mod_cast this
    linarith
  have hs : (0:ℝ) < Real.log x := Real.log_pos hx1
  have hspow : (0:ℝ) < Real.log x ^ H.card := by positivity
  have hxnn : (0:ℝ) ≤ (x:ℝ) := by positivity
  have hclause1 := singularSeries_ge_exp h0 hH
  rw [modelMass]
  rw [show (-(12 * ((H.card : ℝ) - 1) * Real.log ((H.card : ℝ) + 1))
      - (H.card : ℝ) * Real.log (Real.log x))
      = (-(12 * ((H.card : ℝ) - 1) * Real.log ((H.card : ℝ) + 1)))
        + (-((H.card : ℝ) * Real.log (Real.log x))) by ring,
    Real.exp_add, exp_neg_card_loglog hs]
  rw [div_eq_mul_inv]
  rw [show (x:ℝ) * (Real.exp (-(12 * ((H.card : ℝ) - 1) * Real.log ((H.card : ℝ) + 1)))
      * (Real.log x ^ H.card)⁻¹)
      = (Real.exp (-(12 * ((H.card : ℝ) - 1) * Real.log ((H.card : ℝ) + 1))) * (x:ℝ))
        * (Real.log x ^ H.card)⁻¹ by ring]
  apply mul_le_mul_of_nonneg_right _ (by positivity)
  exact mul_le_mul_of_nonneg_right hclause1 hxnn

/-! ### Proof-layer helpers: the Mertens pack M1-M3 (item-0015 s3; not statements)

Mathlib has NO Mertens theorems at the pin, nor on master (steering-verified
full-tree, ANN-36); this pack is the project's first reusable
analytic-number-theory toolkit beyond `Chebyshev.lean`. It depends only on
mathlib (no erdos251 definitions), so it is relocatable there and is an
upstream candidate (ANN-36; routed through the report, not moved mid-session).

Route history (ANN-37). The v3 DYADIC route to M2 is RETIRED: on a block
`p ∈ (r^j, r^(j+1)]` the two-sided M1 error `C` enters once per block over
`j log r`, and couples to the divergent harmonic sum over block indices, so it
lands in the LEADING coefficient -- `(1 + C/log r) lnln P` for every fixed
ratio `r` (coefficient 4 with the crude primorial input). T2's frozen
`log(k+2)^2` budget spends one log on M3 and one on the span, so M3 needs
exponent EXACTLY 1, i.e. M2 leading coefficient EXACTLY 1.

The route below (kickoff v3.1) is discrete Abel summation
(`Finset.sum_Ico_by_parts`): the same M1 error couples instead to the
telescoping total weight variation `∑ (w i - w (i+1)) = w 2 - w P ≤ 1/log 2`,
which is bounded, so the error stays ADDITIVE and the leading coefficient is
exactly 1. Integral-free: `Mathlib.NumberTheory.AbelSummation` is unused.
Only M1's UPPER clause is consumed -- the nonnegative weight differences keep
any lower constant out entirely, so no M1-lower (hence no factorial lower
bound) is needed.
-/

/-- The primes `≤ N`, as a `Finset ℕ` (mathlib's primorial index set). -/
abbrev primesUpto (N : ℕ) : Finset ℕ := (Finset.range (N + 1)).filter Nat.Prime

/-- Chebyshev's factorial factorization, restricted to the primes that
actually occur: `N! = ∏_{p ≤ N} p^{v_p(N!)}`. Primes `p > N` do not divide
`N!`, so they contribute `p^0 = 1`. -/
theorem prod_primesUpto_pow_padicValNat (N : ℕ) :
    ∏ p ∈ primesUpto N, p ^ padicValNat p (Nat.factorial N) = Nat.factorial N := by
  have hfac : Nat.factorial N ≠ 0 := Nat.factorial_ne_zero N
  have hbig := Nat.prod_pow_prime_padicValNat (Nat.factorial N) hfac
    (Nat.factorial N + 1) (by omega)
  have hsub : ∏ p ∈ primesUpto N, p ^ padicValNat p (Nat.factorial N)
      = ∏ p ∈ (Finset.range (Nat.factorial N + 1)).filter Nat.Prime,
          p ^ padicValNat p (Nat.factorial N) := by
    refine Finset.prod_subset ?_ ?_
    · intro p hp
      rw [Finset.mem_filter, Finset.mem_range] at hp ⊢
      exact ⟨by have := Nat.self_le_factorial N; omega, hp.2⟩
    · intro p hp hnot
      rw [Finset.mem_filter, Finset.mem_range] at hp hnot
      have hpp : p.Prime := hp.2
      have hpN : N < p := by
        by_contra hc
        exact hnot ⟨by omega, hpp⟩
      have hnd : ¬ (p ∣ Nat.factorial N) := by
        rw [Nat.Prime.dvd_factorial hpp]; omega
      rw [padicValNat.eq_zero_of_not_dvd hnd, pow_zero]
  rw [hsub, hbig]

/-- Log form: `log N! = ∑_{p ≤ N} v_p(N!) log p`. -/
theorem log_factorial_eq (N : ℕ) :
    Real.log (Nat.factorial N : ℝ)
      = ∑ p ∈ primesUpto N, (padicValNat p (Nat.factorial N) : ℝ) * Real.log p := by
  have h := prod_primesUpto_pow_padicValNat N
  have hcast : ((∏ p ∈ primesUpto N, p ^ padicValNat p (Nat.factorial N) : ℕ) : ℝ)
      = ∏ p ∈ primesUpto N, ((p : ℝ) ^ padicValNat p (Nat.factorial N)) := by
    push_cast; ring
  calc Real.log (Nat.factorial N : ℝ)
      = Real.log ((∏ p ∈ primesUpto N, p ^ padicValNat p (Nat.factorial N) : ℕ) : ℝ) := by
        rw [h]
    _ = Real.log (∏ p ∈ primesUpto N, ((p : ℝ) ^ padicValNat p (Nat.factorial N))) := by
        rw [hcast]
    _ = ∑ p ∈ primesUpto N, Real.log ((p : ℝ) ^ padicValNat p (Nat.factorial N)) := by
        refine Real.log_prod _ _ (fun p hp => ?_)
        rw [Finset.mem_filter] at hp
        have : (0:ℝ) < (p:ℝ) := by exact_mod_cast hp.2.pos
        positivity
    _ = ∑ p ∈ primesUpto N, (padicValNat p (Nat.factorial N) : ℝ) * Real.log p :=
        Finset.sum_congr rfl (fun p _ => by rw [Real.log_pow])

/-- The `i = 1` term of Legendre's formula: `v_p(N!) ≥ ⌊N/p⌋`. -/
theorem padicValNat_factorial_ge_div {p N : ℕ} (hp : p.Prime) (hpN : p ≤ N) :
    N / p ≤ padicValNat p (Nat.factorial N) := by
  haveI : Fact p.Prime := ⟨hp⟩
  rw [padicValNat_factorial (b := Nat.log p N + 1) (by omega)]
  have h1 : (1:ℕ) ∈ Finset.Ico 1 (Nat.log p N + 1) := by
    rw [Finset.mem_Ico]
    exact ⟨le_rfl, by have := Nat.log_pos hp.one_lt hpN; omega⟩
  have := Finset.single_le_sum (f := fun i => N / p ^ i) (fun i _ => Nat.zero_le _) h1
  simpa using this

/-- `∑_{p ≤ N} log p = log N# ≤ N log 4` (ℕ-indexed form, for the Mertens pack). -/
theorem sum_log_primesUpto_le (N : ℕ) :
    ∑ p ∈ primesUpto N, Real.log p ≤ (N : ℝ) * Real.log 4 := by
  have hprod : ∑ p ∈ primesUpto N, Real.log (p : ℝ) = Real.log ((primorial N : ℕ) : ℝ) := by
    rw [primorial]
    push_cast
    rw [Real.log_prod]
    intro p hp
    rw [Finset.mem_filter] at hp
    have : (0:ℝ) < (p:ℝ) := by exact_mod_cast hp.2.pos
    exact ne_of_gt this
  rw [hprod]
  have h4R : ((primorial N : ℕ) : ℝ) ≤ (4:ℝ) ^ N := by exact_mod_cast primorial_le_4_pow N
  calc Real.log ((primorial N : ℕ) : ℝ) ≤ Real.log ((4:ℝ) ^ N) :=
        Real.log_le_log (by exact_mod_cast (primorial_pos N)) h4R
    _ = (N : ℝ) * Real.log 4 := by rw [Real.log_pow]

/-- MERTENS 1 (upper): `∑_{p ≤ N} (log p)/p ≤ log N + log 4`.

Chebyshev's log-factorial identity: `log N! = ∑_{p ≤ N} v_p(N!) log p`
(Legendre, `padicValNat_factorial`), `v_p(N!) ≥ ⌊N/p⌋ > N/p - 1`, and
`N! ≤ N^N`. Rearranged against `∑_{p ≤ N} log p ≤ N log 4`
(`primorial_le_4_pow`). Constant `c₁ = log 4`, explicit. No integrals. -/
theorem mertens_one_upper {N : ℕ} (hN : 1 ≤ N) :
    ∑ p ∈ primesUpto N, Real.log p / p ≤ Real.log N + Real.log 4 := by
  have hNR : (0:ℝ) < (N:ℝ) := by exact_mod_cast hN
  -- pointwise minorant of each Legendre term
  have hpt : ∀ p ∈ primesUpto N,
      ((N:ℝ)/(p:ℝ) - 1) * Real.log p
        ≤ (padicValNat p (Nat.factorial N) : ℝ) * Real.log p := by
    intro p hp
    rw [Finset.mem_filter, Finset.mem_range] at hp
    have hpp : p.Prime := hp.2
    have hpN : p ≤ N := by omega
    have hpR : (0:ℝ) < (p:ℝ) := by exact_mod_cast hpp.pos
    have hlogp : 0 ≤ Real.log p := Real.log_nonneg (by exact_mod_cast hpp.one_lt.le)
    have hdm := Nat.div_add_mod N p
    have hmod : N % p < p := Nat.mod_lt _ hpp.pos
    have hnat : N < p * (N / p) + p := by omega
    have hR : (N:ℝ) < (p:ℝ) * ((N / p : ℕ) : ℝ) + (p:ℝ) := by exact_mod_cast hnat
    have hfloor : (N:ℝ)/(p:ℝ) - 1 ≤ ((N / p : ℕ) : ℝ) := by
      rw [sub_le_iff_le_add, div_le_iff₀ hpR]
      linarith
    have hv : ((N / p : ℕ) : ℝ) ≤ (padicValNat p (Nat.factorial N) : ℝ) := by
      exact_mod_cast padicValNat_factorial_ge_div hpp hpN
    nlinarith [hlogp, hfloor, hv]
  -- assemble the two-sided squeeze on `log N!`
  have hsumeq : ∑ p ∈ primesUpto N, ((N:ℝ)/(p:ℝ) - 1) * Real.log p
      = (N:ℝ) * (∑ p ∈ primesUpto N, Real.log p / p) - ∑ p ∈ primesUpto N, Real.log p := by
    rw [Finset.mul_sum, ← Finset.sum_sub_distrib]
    exact Finset.sum_congr rfl (fun p _ => by ring)
  have hlow : (N:ℝ) * (∑ p ∈ primesUpto N, Real.log p / p) - ∑ p ∈ primesUpto N, Real.log p
      ≤ Real.log (Nat.factorial N : ℝ) := by
    rw [log_factorial_eq N, ← hsumeq]
    exact Finset.sum_le_sum hpt
  have hhigh : Real.log (Nat.factorial N : ℝ) ≤ (N:ℝ) * Real.log N := by
    have h1 : ((Nat.factorial N : ℕ) : ℝ) ≤ ((N:ℝ)) ^ N := by
      exact_mod_cast Nat.factorial_le_pow N
    calc Real.log (Nat.factorial N : ℝ) ≤ Real.log ((N:ℝ) ^ N) :=
          Real.log_le_log (by exact_mod_cast Nat.factorial_pos N) h1
      _ = (N:ℝ) * Real.log N := by rw [Real.log_pow]
  have hprim := sum_log_primesUpto_le N
  -- divide by `N > 0`
  have hkey : (N:ℝ) * (∑ p ∈ primesUpto N, Real.log p / p)
      ≤ (N:ℝ) * (Real.log N + Real.log 4) := by
    have hexp : (N:ℝ) * (Real.log N + Real.log 4)
        = (N:ℝ) * Real.log N + (N:ℝ) * Real.log 4 := by ring
    rw [hexp]
    linarith [hlow, hhigh, hprim]
  exact le_of_mul_le_mul_left hkey hNR

/-- MP-M2 weights `w i = (log i)⁻¹`. Junk values are load-bearing zeros:
`log 0 = log 1 = 0` and `(0:ℝ)⁻¹ = 0`, so `w 0 = w 1 = 0`. -/
def mw (i : ℕ) : ℝ := (Real.log i)⁻¹

/-- MP-M2 summand `g i = log i / i` on primes, `0` off them. -/
def mg (i : ℕ) : ℝ := if Nat.Prime i then Real.log i / i else 0

/-- `G (n+1) = A n = ∑_{p ≤ n} log p / p`: the partial sums of `g` ARE MP-M1's
left-hand side. -/
theorem sum_range_mg (n : ℕ) :
    ∑ i ∈ Finset.range (n + 1), mg i = ∑ p ∈ primesUpto n, Real.log p / p := by
  rw [primesUpto, Finset.sum_filter]
  exact Finset.sum_congr rfl (fun i _ => rfl)

/-- `G 2 = g 0 + g 1 = 0` kills the boundary term of the by-parts identity. -/
theorem sum_range_two_mg : ∑ i ∈ Finset.range 2, mg i = 0 := by
  norm_num [mg, Finset.sum_range_succ, Nat.not_prime_one]

/-- On a prime, `w i * g i = 1/i`; off a prime both sides vanish. -/
theorem mw_mul_mg (i : ℕ) : mw i * mg i = if Nat.Prime i then (1:ℝ) / i else 0 := by
  unfold mw mg
  split_ifs with h
  · have h2 : (2:ℝ) ≤ (i:ℝ) := by exact_mod_cast h.two_le
    have hlog : Real.log i ≠ 0 := ne_of_gt (Real.log_pos (by linarith))
    field_simp
  · ring

/-- Step 0: the target sum in Abel shape. -/
theorem sum_inv_primes_eq {P : ℕ} :
    ∑ p ∈ primesUpto P, (1:ℝ) / p = ∑ i ∈ Finset.Ico 2 (P + 1), mw i * mg i := by
  rw [primesUpto, Finset.sum_filter]
  rw [show (∑ i ∈ Finset.range (P+1), if Nat.Prime i then (1:ℝ)/i else 0)
      = ∑ i ∈ Finset.range (P+1), mw i * mg i from
    Finset.sum_congr rfl (fun i _ => (mw_mul_mg i).symm)]
  refine (Finset.sum_subset ?_ ?_).symm
  · intro i hi
    rw [Finset.mem_Ico] at hi
    rw [Finset.mem_range]
    omega
  · intro i hi hni
    rw [Finset.mem_range] at hi
    rw [Finset.mem_Ico] at hni
    have : i = 0 ∨ i = 1 := by omega
    rcases this with rfl | rfl <;> simp [mw_mul_mg, Nat.not_prime_one]

/-- STEP 1 (IDENT), discrete Abel summation via `Finset.sum_Ico_by_parts`.
Integral-free: `Mathlib.NumberTheory.AbelSummation` stays unused.

  `S(P) = A P / log P + ∑_{i ∈ Ico 2 P} (w i - w (i+1)) * A i` -/
theorem mertens_ident {P : ℕ} (hP : 2 ≤ P) :
    ∑ p ∈ primesUpto P, (1:ℝ) / p
      = mw P * (∑ p ∈ primesUpto P, Real.log p / p)
        + ∑ i ∈ Finset.Ico 2 P, (mw i - mw (i + 1)) * (∑ p ∈ primesUpto i, Real.log p / p) := by
  rw [sum_inv_primes_eq]
  have h := Finset.sum_Ico_by_parts mw mg (m := 2) (n := P + 1) (by omega)
  simp only [smul_eq_mul, Nat.add_sub_cancel] at h
  rw [h, sum_range_two_mg, sum_range_mg P]
  rw [show (∑ i ∈ Finset.Ico 2 P, (mw (i + 1) - mw i) * (∑ j ∈ Finset.range (i + 1), mg j))
      = ∑ i ∈ Finset.Ico 2 P, -((mw i - mw (i + 1)) * (∑ p ∈ primesUpto i, Real.log p / p)) from
    Finset.sum_congr rfl (fun i _ => by rw [sum_range_mg i]; ring)]
  rw [Finset.sum_neg_distrib]
  ring

/-- Generic `Ico` telescope in the `(F i - F (i+1))` orientation
(`Finset.sum_range_sub'` after the `Ico -> range` shift). -/
theorem telescope_Ico_sub' (F : ℕ → ℝ) {m n : ℕ} (h : m ≤ n) :
    ∑ i ∈ Finset.Ico m n, (F i - F (i + 1)) = F m - F n := by
  rw [Finset.sum_Ico_eq_sum_range]
  rw [show (∑ k ∈ Finset.range (n - m), (F (m + k) - F (m + k + 1)))
      = ∑ k ∈ Finset.range (n - m),
          ((fun j => F (m + j)) k - (fun j => F (m + j)) (k + 1)) from
    Finset.sum_congr rfl (fun k _ => by simp only []; rw [← Nat.add_assoc])]
  rw [Finset.sum_range_sub' (fun j => F (m + j))]
  simp only [Nat.add_zero]
  congr 2
  omega

/-- Generic `Ico` telescope in the `(F (i+1) - F i)` orientation. -/
theorem telescope_Ico_sub (F : ℕ → ℝ) {m n : ℕ} (h : m ≤ n) :
    ∑ i ∈ Finset.Ico m n, (F (i + 1) - F i) = F n - F m := by
  have h' := telescope_Ico_sub' F h
  rw [show (∑ i ∈ Finset.Ico m n, (F (i + 1) - F i))
      = -∑ i ∈ Finset.Ico m n, (F i - F (i + 1)) from by
    rw [← Finset.sum_neg_distrib]; exact Finset.sum_congr rfl (fun i _ => by ring)]
  rw [h']; ring

/-- STEP 2: the weights are antitone, so the `A i` coefficients are `≥ 0` --
this is what keeps MP-M1's error ADDITIVE (and its lower clause unused). -/
theorem mw_sub_nonneg {i : ℕ} (hi : 2 ≤ i) : 0 ≤ mw i - mw (i + 1) := by
  have h2 : (2:ℝ) ≤ (i:ℝ) := by exact_mod_cast hi
  have hlogi : 0 < Real.log i := Real.log_pos (by linarith)
  have hle : Real.log (i:ℝ) ≤ Real.log ((i:ℝ) + 1) := Real.log_le_log (by linarith) (by linarith)
  have hinv := inv_anti₀ hlogi hle
  unfold mw
  push_cast
  linarith

/-- STEP 5: the main-term inequality. `log i * (w i - w (i+1)) = 1 - 1/t` with
`t = log(i+1)/log i ≥ 1`, and `log t ≥ 1 - 1/t` (`Real.log_le_sub_one_of_pos`
at `1/t`, then `Real.log_inv`), while `log t` IS the `lnln` increment
(`Real.log_div`). -/
theorem mertens_main_step {i : ℕ} (hi : 2 ≤ i) :
    Real.log i * (mw i - mw (i + 1))
      ≤ Real.log (Real.log ((i:ℝ) + 1)) - Real.log (Real.log (i:ℝ)) := by
  have h2 : (2:ℝ) ≤ (i:ℝ) := by exact_mod_cast hi
  have hlogi : 0 < Real.log (i:ℝ) := Real.log_pos (by linarith)
  have hlogi1 : 0 < Real.log ((i:ℝ) + 1) := Real.log_pos (by linarith)
  have hle : Real.log (i:ℝ) ≤ Real.log ((i:ℝ) + 1) := Real.log_le_log (by linarith) (by linarith)
  set t : ℝ := Real.log ((i:ℝ) + 1) / Real.log (i:ℝ) with ht
  have ht1 : 1 ≤ t := by rw [ht, le_div_iff₀ hlogi]; linarith
  have ht0 : (0:ℝ) < t := by linarith
  have hlogt : 1 - 1/t ≤ Real.log t := by
    have h := Real.log_le_sub_one_of_pos (show (0:ℝ) < t⁻¹ by positivity)
    rw [Real.log_inv] at h
    have hinv : t⁻¹ = 1/t := (one_div t).symm
    rw [hinv] at h
    linarith
  have hlogteq : Real.log t = Real.log (Real.log ((i:ℝ) + 1)) - Real.log (Real.log (i:ℝ)) := by
    rw [ht, Real.log_div (ne_of_gt hlogi1) (ne_of_gt hlogi)]
  have hLHS : Real.log (i:ℝ) * (mw i - mw (i + 1)) = 1 - 1/t := by
    unfold mw
    push_cast
    rw [ht]
    field_simp
    ring
  rw [hLHS, ← hlogteq]
  exact hlogt

/-- MP-M1's upper constant `b`, as landed (`mertens_one_upper`). -/
def mertensB : ℝ := Real.log 4

/-- MP-M2's constant, SYMBOLIC in MP-M1's `b`:
`c₂ = 1 + b/log 2 - lnln 2`. Numerically `≈ 3.3665` (`lnln 2 ≈ -0.3665`). -/
def mertensC2 : ℝ := 1 + mertensB / Real.log 2 - Real.log (Real.log 2)

/-- MERTENS 2 (upper), LEADING COEFFICIENT EXACTLY 1:
`∑_{p ≤ P} 1/p ≤ lnln P + c₂` for `P ≥ 2`.

Discrete Abel summation (kickoff v3.1, ANN-37; the v3 dyadic route is retired
because its per-block MP-M1 error lands in the LEADING coefficient). Here the
same error couples instead to the telescoping total weight variation
`∑ (w i - w (i+1)) = w 2 - w P ≤ 1/log 2`, so it stays ADDITIVE. Only MP-M1's
UPPER clause is consumed: the nonnegative weight differences keep any lower
constant out entirely. Integral-free -- `Mathlib.NumberTheory.AbelSummation`
is unused. -/
theorem mertens_second_upper {P : ℕ} (hP : 2 ≤ P) :
    ∑ p ∈ primesUpto P, (1:ℝ) / p ≤ Real.log (Real.log P) + mertensC2 := by
  have hPR : (2:ℝ) ≤ (P:ℝ) := by exact_mod_cast hP
  have hlogP : 0 < Real.log (P:ℝ) := Real.log_pos (by linarith)
  have hb0 : (0:ℝ) ≤ mertensB := Real.log_nonneg (by norm_num)
  have hA : ∀ i : ℕ, 1 ≤ i → (∑ p ∈ primesUpto i, Real.log p / p) ≤ Real.log i + mertensB :=
    fun i hi => mertens_one_upper hi
  rw [mertens_ident hP]
  -- STEP 3, first term: `w P * A P ≤ 1 + b/log P`
  have hfirst : mw P * (∑ p ∈ primesUpto P, Real.log p / p)
      ≤ 1 + mertensB * (Real.log (P:ℝ))⁻¹ := by
    have hmwP : mw P = (Real.log (P:ℝ))⁻¹ := rfl
    have hmw0 : (0:ℝ) < mw P := by rw [hmwP]; positivity
    calc mw P * (∑ p ∈ primesUpto P, Real.log p / p) ≤ mw P * (Real.log P + mertensB) :=
          mul_le_mul_of_nonneg_left (hA P (by omega)) hmw0.le
      _ = 1 + mertensB * (Real.log (P:ℝ))⁻¹ := by rw [hmwP]; field_simp
  -- STEP 3, sum term: coefficients are `≥ 0`, so insert MP-M1 UPPER termwise
  have hsum : ∑ i ∈ Finset.Ico 2 P, (mw i - mw (i + 1)) * (∑ p ∈ primesUpto i, Real.log p / p)
      ≤ ∑ i ∈ Finset.Ico 2 P, (mw i - mw (i + 1)) * (Real.log i + mertensB) := by
    refine Finset.sum_le_sum (fun i hi => ?_)
    rw [Finset.mem_Ico] at hi
    exact mul_le_mul_of_nonneg_left (hA i (by omega)) (mw_sub_nonneg hi.1)
  have hsplit : ∑ i ∈ Finset.Ico 2 P, (mw i - mw (i + 1)) * (Real.log i + mertensB)
      = (∑ i ∈ Finset.Ico 2 P, Real.log i * (mw i - mw (i + 1)))
        + mertensB * (∑ i ∈ Finset.Ico 2 P, (mw i - mw (i + 1))) := by
    rw [Finset.mul_sum, ← Finset.sum_add_distrib]
    exact Finset.sum_congr rfl (fun i _ => by ring)
  -- STEP 4: the error telescope (exact, P-uniform)
  have htel1 : ∑ i ∈ Finset.Ico 2 P, (mw i - mw (i + 1)) = mw 2 - mw P :=
    telescope_Ico_sub' mw hP
  -- STEP 5: the main-term telescope
  have htel2 : ∑ i ∈ Finset.Ico 2 P, Real.log i * (mw i - mw (i + 1))
      ≤ Real.log (Real.log P) - Real.log (Real.log 2) := by
    calc ∑ i ∈ Finset.Ico 2 P, Real.log i * (mw i - mw (i + 1))
        ≤ ∑ i ∈ Finset.Ico 2 P, ((fun j : ℕ => Real.log (Real.log j)) (i + 1)
            - (fun j : ℕ => Real.log (Real.log j)) i) := by
          refine Finset.sum_le_sum (fun i hi => ?_)
          rw [Finset.mem_Ico] at hi
          have h := mertens_main_step hi.1
          simp only []
          push_cast
          exact h
      _ = Real.log (Real.log P) - Real.log (Real.log 2) := by
          rw [telescope_Ico_sub (fun j : ℕ => Real.log (Real.log j)) hP]
          norm_num
  have hmw2 : mw 2 = (Real.log 2)⁻¹ := by unfold mw; norm_num
  have hmwP : mw P = (Real.log (P:ℝ))⁻¹ := rfl
  have hbdiv : mertensB / Real.log 2 = mertensB * (Real.log 2)⁻¹ := div_eq_mul_inv _ _
  unfold mertensC2
  rw [hsplit] at hsum
  rw [htel1, hmw2, hmwP] at hsum
  rw [hbdiv]
  nlinarith [hfirst, hsum, htel2, hb0]

/-- MP-M3's constant, symbolic. Numerically `exp(4.3665) ≈ 78.8`. -/
def mertensC3 : ℝ := Real.exp (mertensC2 + 1)

/-- The `-log(1-1/p) - 1/p` tail, telescoped: `∑_{p ≤ P} 1/(p(p-1)) ≤ 1`
(compare with `∑_{m ≥ 2} 1/(m(m-1)) = 1`, which telescopes as
`1/(m-1) - 1/m`). -/
theorem sum_tail_le_one {P : ℕ} (hP : 2 ≤ P) :
    ∑ p ∈ primesUpto P, 1 / ((p:ℝ) * ((p:ℝ) - 1)) ≤ 1 := by
  have hsub : primesUpto P ⊆ Finset.Ico 2 (P + 1) := by
    intro p hp
    rw [primesUpto, Finset.mem_filter, Finset.mem_range] at hp
    rw [Finset.mem_Ico]
    exact ⟨hp.2.two_le, hp.1⟩
  have hnn : ∀ i ∈ Finset.Ico 2 (P + 1), i ∉ primesUpto P →
      0 ≤ 1 / ((i:ℝ) * ((i:ℝ) - 1)) := by
    intro i hi _
    rw [Finset.mem_Ico] at hi
    have h2 : (2:ℝ) ≤ (i:ℝ) := by exact_mod_cast hi.1
    have h1 : (0:ℝ) < (i:ℝ) - 1 := by linarith
    positivity
  refine le_trans (Finset.sum_le_sum_of_subset_of_nonneg hsub hnn) ?_
  -- telescope `1/(m(m-1)) = F m - F (m+1)` with `F m = 1/(m-1)`
  have hcong : ∑ i ∈ Finset.Ico 2 (P + 1), 1 / ((i:ℝ) * ((i:ℝ) - 1))
      = ∑ i ∈ Finset.Ico 2 (P + 1),
          ((fun j : ℕ => ((j:ℝ) - 1)⁻¹) i - (fun j : ℕ => ((j:ℝ) - 1)⁻¹) (i + 1)) := by
    refine Finset.sum_congr rfl (fun i hi => ?_)
    rw [Finset.mem_Ico] at hi
    have h2 : (2:ℝ) ≤ (i:ℝ) := by exact_mod_cast hi.1
    have hi0 : (i:ℝ) ≠ 0 := by linarith
    have hi1 : (i:ℝ) - 1 ≠ 0 := by linarith
    simp only []
    push_cast
    rw [show ((i:ℝ) + 1 - 1) = (i:ℝ) by ring]
    field_simp
    ring
  rw [hcong, telescope_Ico_sub' (fun j : ℕ => ((j:ℝ) - 1)⁻¹) (by omega)]
  have hP1 : (1:ℝ) ≤ (P:ℝ) := by
    have : (2:ℝ) ≤ (P:ℝ) := by exact_mod_cast hP
    linarith
  have hPinv : (0:ℝ) ≤ ((P:ℝ))⁻¹ := by positivity
  push_cast
  rw [show ((P:ℝ) + 1 - 1) = (P:ℝ) by ring]
  norm_num

/-- MERTENS 3 (upper), EXPONENT EXACTLY 1 on `log P`:
`∏_{p ≤ P} (1 - 1/p)⁻¹ ≤ c₃ log P` for `P ≥ 2`.

`log` of the product is `∑ -log(1-1/p) ≤ ∑ 1/(p-1) = ∑ 1/p + ∑ 1/(p(p-1))`
via `Real.log_le_sub_one_of_pos`; MP-M2 gives the first sum with coefficient 1
and `sum_tail_le_one` the second. Exponentiating, `exp(lnln P) = log P`, so the
exponent is 1 -- which is exactly what T2's frozen `log(k+2)^2` budget needs
(one log here, one from the span). -/
theorem mertens_third_upper {P : ℕ} (hP : 2 ≤ P) :
    ∏ p ∈ primesUpto P, (1 - 1 / (p:ℝ))⁻¹ ≤ mertensC3 * Real.log P := by
  have hPR : (2:ℝ) ≤ (P:ℝ) := by exact_mod_cast hP
  have hlogP : 0 < Real.log (P:ℝ) := Real.log_pos (by linarith)
  have hfac : ∀ p ∈ primesUpto P, (0:ℝ) < (1 - 1 / (p:ℝ))⁻¹ := by
    intro p hp
    rw [primesUpto, Finset.mem_filter] at hp
    have h2 : (2:ℝ) ≤ (p:ℝ) := by exact_mod_cast hp.2.two_le
    have : (0:ℝ) < 1 - 1 / (p:ℝ) := by rw [sub_pos, div_lt_one (by linarith)]; linarith
    positivity
  have hprodpos : (0:ℝ) < ∏ p ∈ primesUpto P, (1 - 1 / (p:ℝ))⁻¹ := Finset.prod_pos hfac
  -- pointwise: `-log(1-1/p) ≤ 1/p + 1/(p(p-1))`
  have hpt : ∀ p ∈ primesUpto P, Real.log ((1 - 1 / (p:ℝ))⁻¹)
      ≤ 1 / (p:ℝ) + 1 / ((p:ℝ) * ((p:ℝ) - 1)) := by
    intro p hp
    have hp' := hp
    rw [primesUpto, Finset.mem_filter] at hp'
    have h2 : (2:ℝ) ≤ (p:ℝ) := by exact_mod_cast hp'.2.two_le
    have h := Real.log_le_sub_one_of_pos (hfac p hp)
    have heq : (1 - 1 / (p:ℝ))⁻¹ - 1 = 1 / (p:ℝ) + 1 / ((p:ℝ) * ((p:ℝ) - 1)) := by
      have hp0 : (p:ℝ) ≠ 0 := by linarith
      have hp1 : (p:ℝ) - 1 ≠ 0 := by linarith
      field_simp
    linarith [h, heq.le, heq.ge]
  have hkey : Real.log (∏ p ∈ primesUpto P, (1 - 1 / (p:ℝ))⁻¹)
      ≤ Real.log (Real.log P) + mertensC2 + 1 := by
    rw [Real.log_prod _ _ (fun p hp => ne_of_gt (hfac p hp))]
    calc ∑ p ∈ primesUpto P, Real.log ((1 - 1 / (p:ℝ))⁻¹)
        ≤ ∑ p ∈ primesUpto P, (1 / (p:ℝ) + 1 / ((p:ℝ) * ((p:ℝ) - 1))) :=
          Finset.sum_le_sum hpt
      _ = (∑ p ∈ primesUpto P, 1 / (p:ℝ))
            + ∑ p ∈ primesUpto P, 1 / ((p:ℝ) * ((p:ℝ) - 1)) := Finset.sum_add_distrib
      _ ≤ (Real.log (Real.log P) + mertensC2) + 1 :=
          add_le_add (mertens_second_upper hP) (sum_tail_le_one hP)
      _ = Real.log (Real.log P) + mertensC2 + 1 := by ring
  calc ∏ p ∈ primesUpto P, (1 - 1 / (p:ℝ))⁻¹
      = Real.exp (Real.log (∏ p ∈ primesUpto P, (1 - 1 / (p:ℝ))⁻¹)) :=
        (Real.exp_log hprodpos).symm
    _ ≤ Real.exp (Real.log (Real.log P) + mertensC2 + 1) := Real.exp_le_exp.mpr hkey
    _ = mertensC3 * Real.log P := by
        unfold mertensC3
        rw [show Real.log (Real.log (P:ℝ)) + mertensC2 + 1
            = (mertensC2 + 1) + Real.log (Real.log (P:ℝ)) by ring,
          Real.exp_add, Real.exp_log hlogP]

/-! ### Proof-layer helpers for Lemma 4.2 (item-0015 s3; not statements)

T2 step (a) of kickoff v3 section 4: the per-prime ratio analysis, which is
4.2's foundation. The remaining steps (b)-(d) -- collision primes are `< span`,
the split at `k+2` (SMALL via MP-M3, LARGE via the squarefree-divisor
expansion), and the assembly -- are session 4's.

The `k = 0` edge flagged "TEST THIS FIRST" by the kickoff is DISCHARGED:
`offsetSpan {0} = 0` (by `decide`), so `oneExtensions {0} = ∅` and the frozen
statement reads `0 ≤ 0` there. The frozen 4.2 is not false at `k = 0`.
-/

/-- T2 step (a), the dichotomy: adding one point moves `ν` by `0` or `1`. -/
theorem nuMod_insert (H : Finset ℕ) (t p : ℕ) :
    nuMod (insert t H) p = nuMod H p ∨ nuMod (insert t H) p = nuMod H p + 1 := by
  unfold nuMod
  rw [Finset.image_insert]
  by_cases h : (t : ZMod p) ∈ H.image (Nat.cast : ℕ → ZMod p)
  · left; rw [Finset.insert_eq_self.mpr h]
  · right; rw [Finset.card_insert_of_not_mem h]

/-- T2 step (a): the per-prime log-ratio of the singular-series factors.
COLLISION (`ν' = ν`) contributes exactly `-log(1-1/p) = log(1 + 1/(p-1))`;
NEW (`ν' = ν+1`) contributes `≤ 0`. The NEW algebra is
`(1-ν/p)(1-1/p) - (1-(ν+1)/p) = ν/p² ≥ 0`. -/
theorem log_singularFactor_insert_sub_le {H : Finset ℕ} {t : ℕ}
    (hins : IsAdmissible (insert t H)) (hH : IsAdmissible H) (ht : t ∉ H) (p : Nat.Primes) :
    Real.log ((1 - (nuMod (insert t H) (p:ℕ) : ℝ) / ((p:ℕ):ℝ)) /
        (1 - 1/((p:ℕ):ℝ)) ^ (insert t H).card)
      - Real.log ((1 - (nuMod H (p:ℕ) : ℝ) / ((p:ℕ):ℝ)) /
        (1 - 1/((p:ℕ):ℝ)) ^ H.card)
      ≤ (if nuMod (insert t H) (p:ℕ) = nuMod H (p:ℕ)
          then -Real.log (1 - 1/((p:ℕ):ℝ)) else 0) := by
  have hp : (p : ℕ).Prime := p.2
  set P : ℝ := ((p : ℕ) : ℝ) with hPdef
  have hP2 : (2:ℝ) ≤ P := by rw [hPdef]; exact_mod_cast hp.two_le
  have hP0 : (0:ℝ) < P := by linarith
  have hcard : (insert t H).card = H.card + 1 := Finset.card_insert_of_not_mem ht
  -- positivity of both numerators (admissibility) and of the common denominator
  have hnum : (0:ℝ) < 1 - (nuMod H (p:ℕ) : ℝ) / P := by
    have h : (nuMod H (p:ℕ) : ℝ) < P := by rw [hPdef]; exact_mod_cast hH _ hp
    rw [sub_pos, div_lt_one hP0]; exact h
  have hnum' : (0:ℝ) < 1 - (nuMod (insert t H) (p:ℕ) : ℝ) / P := by
    have h : (nuMod (insert t H) (p:ℕ) : ℝ) < P := by rw [hPdef]; exact_mod_cast hins _ hp
    rw [sub_pos, div_lt_one hP0]; exact h
  have hden : (0:ℝ) < 1 - 1 / P := by rw [sub_pos, div_lt_one hP0]; linarith
  -- split both logs; the `(1-1/p)` powers collapse to a single factor
  rw [Real.log_div (ne_of_gt hnum') (by positivity), Real.log_div (ne_of_gt hnum) (by positivity),
    Real.log_pow, Real.log_pow, hcard]
  push_cast
  have hkey : Real.log (1 - (nuMod (insert t H) (p:ℕ) : ℝ) / P)
      - ((H.card : ℝ) + 1) * Real.log (1 - 1/P)
      - (Real.log (1 - (nuMod H (p:ℕ) : ℝ) / P) - (H.card : ℝ) * Real.log (1 - 1/P))
      = (Real.log (1 - (nuMod (insert t H) (p:ℕ) : ℝ) / P)
          - Real.log (1 - (nuMod H (p:ℕ) : ℝ) / P)) - Real.log (1 - 1/P) := by ring
  rw [hkey]
  rcases nuMod_insert H t (p:ℕ) with hcoll | hnew
  · -- COLLISION: exact equality
    rw [if_pos hcoll, hcoll]
    simp
  · -- NEW: the ratio is `≤ 1`, i.e. the log-difference is `≤ 0`
    rw [if_neg (by omega)]
    have hnu0 : (0:ℝ) ≤ (nuMod H (p:ℕ) : ℝ) := Nat.cast_nonneg _
    have hstep : (1:ℝ) - (nuMod (insert t H) (p:ℕ) : ℝ) / P
        ≤ (1 - (nuMod H (p:ℕ) : ℝ) / P) * (1 - 1/P) := by
      rw [hnew]
      push_cast
      have hdiff : (1 - (nuMod H (p:ℕ) : ℝ) / P) * (1 - 1/P)
          - (1 - ((nuMod H (p:ℕ) : ℝ) + 1) / P) = (nuMod H (p:ℕ) : ℝ) / P ^ 2 := by
        field_simp
        ring
      have hq : (0:ℝ) ≤ (nuMod H (p:ℕ) : ℝ) / P ^ 2 := by positivity
      linarith [hdiff, hq]
    have hlog := Real.log_le_log hnum' hstep
    rw [Real.log_mul (ne_of_gt hnum) (ne_of_gt hden)] at hlog
    linarith

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
  refine ⟨12, by norm_num, fun H h0 _ hH => singularSeries_ge_exp h0 hH,
    ⟨3, fun x hx H h0 _ hH _ _ => modelMass_ge_exp hx h0 hH⟩⟩

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

/-- `clog₂((n+2)^2) ≤ 2 clog₂(n+2)`: squaring at most doubles the
binary ceiling logarithm (`(n+2)^2 ≤ (2^{clog₂(n+2)})^2 = 2^{2 clog₂(n+2)}`). -/
private theorem clog_sq_le (n : ℕ) :
    Nat.clog 2 ((n + 2) ^ 2) ≤ 2 * Nat.clog 2 (n + 2) := by
  apply (Nat.le_pow_iff_clog_le (by norm_num)).mp
  calc (n + 2) ^ 2 ≤ (2 ^ Nat.clog 2 (n + 2)) ^ 2 :=
        Nat.pow_le_pow_left (Nat.le_pow_clog (by norm_num) _) 2
    _ = 2 ^ (2 * Nat.clog 2 (n + 2)) := by rw [← pow_mul, Nat.mul_comm]

/-- Chebyshev extraction, ℕ form (the log bootstrap). For `n ≥ 5`:
`q n ≤ 2 clog₂(n+2) (n+1)`.

Write `N = q n = 2m+1` (`N ≥ q 5 = 13` is an odd prime). Chebyshev's
`two_mul_lt_clog_mul` at `m` gives `N - 1 < clog₂(N-1) (π(N-1) + 1)`, and
`π(N-1) = count Prime N = n` by `Nat.count_nth_of_infinite`. The crude
bound `nth_prime_lt_sq` (`N < (n+2)^2`) is fed back in to replace
`clog₂(N-1)` by `2 clog₂(n+2)` -- this is what breaks the circularity. -/
private theorem q_le_clog_mul {n : ℕ} (hn : 5 ≤ n) :
    q n ≤ 2 * Nat.clog 2 (n + 2) * (n + 1) := by
  have hq5 : q 5 = 13 := q_eq_of_count (by norm_num) (by decide)
  have hN13 : 13 ≤ q n := by
    calc (13 : ℕ) = q 5 := hq5.symm
      _ ≤ q n := q_strictMono.monotone hn
  have hodd : q n % 2 = 1 := by
    rcases (q_prime n).eq_two_or_odd with h | h
    · omega
    · exact h
  obtain ⟨m, hm2⟩ : ∃ m, 2 * m + 1 = q n := ⟨q n / 2, by omega⟩
  have hm4 : 4 ≤ m := by omega
  have hcheb := two_mul_lt_clog_mul m hm4
  have hcount : Nat.primeCounting (2 * m) = n := by
    have e : Nat.primeCounting (2 * m) = Nat.count Nat.Prime (2 * m + 1) := rfl
    rw [e, hm2]
    simpa [q] using Nat.count_nth_of_infinite Nat.infinite_setOf_prime n
  rw [hcount] at hcheb
  have hsq : q n < (n + 2) ^ 2 := nth_prime_lt_sq hn
  have hclog : Nat.clog 2 (2 * m) ≤ 2 * Nat.clog 2 (n + 2) := by
    calc Nat.clog 2 (2 * m) ≤ Nat.clog 2 ((n + 2) ^ 2) := Nat.clog_mono_right 2 (by omega)
      _ ≤ 2 * Nat.clog 2 (n + 2) := clog_sq_le n
  have hkey : 2 * m < 2 * Nat.clog 2 (n + 2) * (n + 1) :=
    lt_of_lt_of_le hcheb (Nat.mul_le_mul hclog (le_refl (n + 1)))
  omega

/-- The single ℕ→ℝ bridge: `clog₂ m ≤ 2 ln m` for `m ≥ 8`.

`Nat.pow_pred_clog_lt_self` gives `2^{c-1} < m`, i.e. `c < ln m / ln 2 + 1`;
`m ≥ 8` gives `ln m ≥ 3 ln 2`, which absorbs the `+1` with room to spare
(`c < 1.925 ln m`). Reduced to `Real.log_two_gt_d9`. -/
private theorem clog_le_two_log {m : ℕ} (hm : 8 ≤ m) :
    (Nat.clog 2 m : ℝ) ≤ 2 * Real.log m := by
  have hl0 : (0 : ℝ) < Real.log 2 := by linarith [Real.log_two_gt_d9]
  have hc1 : 1 ≤ Nat.clog 2 m := Nat.clog_pos (by norm_num) (by omega)
  have hlt : 2 ^ (Nat.clog 2 m - 1) < m := Nat.pow_pred_clog_lt_self (by norm_num) (by omega)
  have hltR : (2 : ℝ) ^ (Nat.clog 2 m - 1) < (m : ℝ) := by exact_mod_cast hlt
  have hlog : ((Nat.clog 2 m : ℝ) - 1) * Real.log 2 < Real.log m := by
    have h := Real.log_lt_log (by positivity : (0 : ℝ) < 2 ^ (Nat.clog 2 m - 1)) hltR
    rw [Real.log_pow, Nat.cast_sub hc1] at h
    push_cast at h
    linarith
  have hlog8 : 3 * Real.log 2 ≤ Real.log m := by
    have h8 : Real.log 8 ≤ Real.log m :=
      Real.log_le_log (by norm_num) (by exact_mod_cast hm)
    have he : Real.log 8 = 3 * Real.log 2 := by
      rw [show (8 : ℝ) = 2 ^ 3 by norm_num, Real.log_pow]; push_cast; ring
    linarith
  have h2l1 : (0 : ℝ) ≤ 2 * Real.log 2 - 1 := by linarith [Real.log_two_gt_d9]
  have h3l2 : (0 : ℝ) ≤ 3 * Real.log 2 - 2 := by linarith [Real.log_two_gt_d9]
  have hp1 : (0 : ℝ) ≤ (Real.log m - 3 * Real.log 2) * (2 * Real.log 2 - 1) :=
    mul_nonneg (by linarith) h2l1
  have hp2 : (0 : ℝ) ≤ Real.log 2 * (3 * Real.log 2 - 2) := mul_nonneg hl0.le h3l2
  have hLl : Real.log m + Real.log 2 ≤ 2 * Real.log m * Real.log 2 := by nlinarith [hp1, hp2]
  have key : (Nat.clog 2 m : ℝ) * Real.log 2 < (2 * Real.log m) * Real.log 2 := by
    nlinarith [hlog, hLl]
  exact (lt_of_mul_lt_mul_right key hl0.le).le

/-- Chebyshev extraction (the `q n = O(n ln n)` upper bound), in the shape
section 5(iii) consumes: `q n ≤ 4 (n+1) ln(n+2)` for all `n ≥ 4`.

`n ≥ 6` is `q_le_clog_mul` composed with `clog_le_two_log` at `m = n+2 ≥ 8`;
`n = 4, 5` are the numeric values `q 4 = 11`, `q 5 = 13` against
`ln(n+2) ≥ ln 4 = 2 ln 2 > 1.386`. The constant `4` is not sharp
(the truth is `~1`); slack is deliberate. -/
theorem q_le_mul_log : ∃ C : ℝ, 1 ≤ C ∧ ∀ n : ℕ, 4 ≤ n →
    (q n : ℝ) ≤ C * ((n : ℝ) + 1) * Real.log ((n : ℝ) + 2) := by
  refine ⟨4, by norm_num, ?_⟩
  intro n hn
  have hlog2 : (1.386 : ℝ) < 2 * Real.log 2 := by linarith [Real.log_two_gt_d9]
  rcases Nat.lt_or_ge n 6 with hn6 | hn6
  · have hlog4 : 2 * Real.log 2 ≤ Real.log ((n : ℝ) + 2) := by
      have hle : (4 : ℝ) ≤ (n : ℝ) + 2 := by
        have : (4 : ℝ) ≤ (n : ℝ) := by exact_mod_cast hn
        linarith
      have h := Real.log_le_log (by norm_num : (0 : ℝ) < 4) hle
      rw [show (4 : ℝ) = 2 ^ 2 by norm_num, Real.log_pow] at h
      push_cast at h
      linarith
    interval_cases n
    · have h4 : q 4 = 11 := q_eq_of_count (by norm_num) (by decide)
      rw [h4]; norm_num at hlog4 ⊢; linarith [hlog4, hlog2]
    · have h5 : q 5 = 13 := q_eq_of_count (by norm_num) (by decide)
      rw [h5]; norm_num at hlog4 ⊢; linarith [hlog4, hlog2]
  · have h1 : q n ≤ 2 * Nat.clog 2 (n + 2) * (n + 1) := q_le_clog_mul (by omega)
    have h2 : (Nat.clog 2 (n + 2) : ℝ) ≤ 2 * Real.log ((n : ℝ) + 2) := by
      have h := clog_le_two_log (m := n + 2) (by omega)
      push_cast at h
      exact h
    have h1R : (q n : ℝ) ≤ 2 * (Nat.clog 2 (n + 2) : ℝ) * ((n : ℝ) + 1) := by
      have h := (Nat.cast_le (α := ℝ)).mpr h1
      push_cast at h
      linarith
    have hn1 : (0 : ℝ) ≤ (n : ℝ) + 1 := by positivity
    have h3 := mul_le_mul_of_nonneg_right h2 hn1
    nlinarith [h1R, h3]
/-- Endpoint lemma (section 5(iii) input): the span of the point set of a
gap word coming from a strictly monotone enumeration `e` is the full
endpoint difference `e L - e 0`. The point set is the `L+1` prefix sums
`P_0, ..., P_L`; `P_0 = 0` is the min and `P_j = e j - e 0` telescopes
(`psum_telescope`), so the sup is attained at `j = L`. -/
theorem offsetSpan_wordPointSet {L : ℕ} {w e : ℕ → ℕ} (he : StrictMono e)
    (hw : ∀ j, w j = e (j + 1) - e j) :
    offsetSpan (wordPointSet w L) = e L - e 0 := by
  have hfun : (fun j => ∑ i ∈ Finset.range j, w i) = (fun j => e j - e 0) := by
    funext j
    rw [show (∑ i ∈ Finset.range j, w i) = ∑ i ∈ Finset.range j, (e (i + 1) - e i) from
        Finset.sum_congr rfl (fun i _ => hw i)]
    exact psum_telescope he.monotone j
  have hset : wordPointSet w L
      = Finset.image (fun j => e j - e 0) (Finset.range (L + 1)) := by
    unfold wordPointSet; rw [hfun]
  rw [offsetSpan, hset, Finset.sup_image]
  apply le_antisymm
  · apply Finset.sup_le
    intro j hj
    rw [Finset.mem_range] at hj
    have : e j ≤ e L := he.monotone (by omega)
    simp only [Function.comp_apply, id_eq]
    omega
  · exact Finset.le_sup (f := id ∘ (fun j => e j - e 0))
      (Finset.mem_range.mpr (Nat.lt_succ_self L))

/-- `cElem J K 0 = q_0` (the `if` takes its `then` branch at `t = 0`). -/
theorem cElem_zero (J K : ℕ) : cElem J K 0 = cprime (cL J K) 0 := by
  simp [cElem, cI]

/-- `cElem J K L = q_{L+1}` (the `if` takes its `else` branch at `t = L`,
since `L = J+2+K > J+1 = i_0`): the deletion does not move the top point. -/
theorem cElem_top (J K : ℕ) : cElem J K (cL J K) = cprime (cL J K) (cL J K + 1) := by
  simp only [cElem, cI, cL]
  rw [if_neg (by omega)]

/-- `cElem' J K 0 = q_0` (`0 < i_0`). -/
theorem cElem'_zero (J K : ℕ) : cElem' J K 0 = cprime (cL J K) 0 := by
  simp [cElem', cI]

/-- `cElem' J K L = q_{L+1}` (`L ≥ i_0`). -/
theorem cElem'_top (J K : ℕ) : cElem' J K (cL J K) = cprime (cL J K) (cL J K + 1) := by
  simp only [cElem', cI, cL]
  rw [if_neg (by omega)]

/-- Section 5(iii): the span of `w` is the full prime window `q_{L+1} - q_0`
-- the deleted interior point moves neither endpoint. -/
theorem cspan_eq (J K : ℕ) :
    offsetSpan (wordPointSet (cword J K) (cL J K))
      = cprime (cL J K) (cL J K + 1) - cprime (cL J K) 0 := by
  rw [offsetSpan_wordPointSet (w := cword J K) (e := cElem J K) (cElem_strictMono J K)
      (fun j => rfl), cElem_zero, cElem_top]

/-- Section 5(iii): the span of `w'` is the same window `q_{L+1} - q_0`. -/
theorem cspan'_eq (J K : ℕ) :
    offsetSpan (wordPointSet (cword' J K) (cL J K))
      = cprime (cL J K) (cL J K + 1) - cprime (cL J K) 0 := by
  rw [offsetSpan_wordPointSet (w := cword' J K) (e := cElem' J K) (cElem'_strictMono J K)
      (fun j => rfl), cElem'_zero, cElem'_top]

/-- Index arithmetic: the top of the section-5 prime window sits at
`q`-index `primeIdxAbove L + (L+1) ≤ 2L+5`, since
`primeIdxAbove L = Nat.count Nat.Prime (L+4) ≤ L+4` (`Nat.count_le`). -/
theorem cprime_top_le_q (L : ℕ) : cprime L (L + 1) ≤ q (2 * L + 5) := by
  have hidx : primeIdxAbove L ≤ L + 4 := by
    unfold primeIdxAbove; exact Nat.count_le _
  unfold cprime
  exact q_strictMono.monotone (by omega)

/-- The Chebyshev extraction in window shape: `q_{2L+5} ≤ 12 C L ln L` for
`L ≥ 4`. Absorbs the two edge estimates `2L+6 ≤ 4L` and
`ln(2L+7) ≤ 3 ln L` (the latter from `2L+7 ≤ L^3`, valid at `L = 4`:
`15 ≤ 64`); both are deliberately slack, per the section's constant
budget (`C₁` absorbs everything). -/
theorem q_window_le {C : ℝ} (hC : 1 ≤ C)
    (hq : ∀ n : ℕ, 4 ≤ n → (q n : ℝ) ≤ C * ((n : ℝ) + 1) * Real.log ((n : ℝ) + 2))
    (L : ℕ) (hL : 4 ≤ L) :
    (q (2 * L + 5) : ℝ) ≤ 12 * C * (L : ℝ) * Real.log (L : ℝ) := by
  have hLR : (4 : ℝ) ≤ (L : ℝ) := by exact_mod_cast hL
  have hlogL : 0 < Real.log (L : ℝ) := Real.log_pos (by linarith)
  have h1 := hq (2 * L + 5) (by omega)
  push_cast at h1
  have hcube : (2 * (L:ℝ) + 5 + 2) ≤ (L : ℝ) ^ 3 := by
    have h16 : 16 * (L : ℝ) ≤ (L : ℝ) ^ 3 := by
      nlinarith [hLR, mul_nonneg (mul_nonneg (by linarith : (0:ℝ) ≤ (L:ℝ))
        (by linarith : (0:ℝ) ≤ (L:ℝ) - 4)) (by linarith : (0:ℝ) ≤ (L:ℝ) + 4)]
    linarith
  have hlog3 : Real.log (2 * (L:ℝ) + 5 + 2) ≤ 3 * Real.log (L : ℝ) := by
    calc Real.log (2 * (L:ℝ) + 5 + 2) ≤ Real.log ((L : ℝ) ^ 3) :=
          Real.log_le_log (by linarith) hcube
      _ = 3 * Real.log (L : ℝ) := by rw [Real.log_pow]; push_cast; ring
  have hlin : 2 * (L:ℝ) + 5 + 1 ≤ 4 * (L : ℝ) := by linarith
  calc (q (2 * L + 5) : ℝ) ≤ C * (2 * (L:ℝ) + 5 + 1) * Real.log (2 * (L:ℝ) + 5 + 2) := h1
    _ ≤ C * (4 * (L:ℝ)) * (3 * Real.log (L : ℝ)) := by
        apply mul_le_mul
        · exact mul_le_mul_of_nonneg_left hlin (by linarith)
        · exact hlog3
        · exact Real.log_nonneg (by linarith)
        · positivity
    _ = 12 * C * (L : ℝ) * Real.log (L : ℝ) := by ring

/-! #### Constants layer: the `Nat.ceil ∘ logb 2` idiom of section 5 -/

/-- The defining property of the `ceil ∘ logb 2` idiom used by both
section-5 constants: rounding the exact base-2 exponent UP makes the
power dominate. Supplies 5(iv)'s `2^K ≥ H_x` and 5(iii)'s `2^J ≥ (K+20)^4`. -/
theorem le_two_pow_ceil_logb {z : ℝ} (hz : 0 < z) :
    z ≤ 2 ^ (Nat.ceil (Real.logb 2 z)) := by
  calc z = (2:ℝ) ^ (Real.logb 2 z) :=
        (Real.rpow_logb (by norm_num) (by norm_num) hz).symm
    _ ≤ (2:ℝ) ^ ((Nat.ceil (Real.logb 2 z) : ℕ) : ℝ) :=
        (Real.rpow_le_rpow_left_iff (by norm_num)).mpr (Nat.le_ceil _)
    _ = 2 ^ (Nat.ceil (Real.logb 2 z)) := Real.rpow_natCast _ _

/-- `K = ceil(log2(4 C_g) + 2 log2 ln x)` is exactly `ceil(log2 H_x)`: the
two `logb` terms recombine into the single tail budget `H_x = 4 C_g (ln x)^2`. -/
theorem cK_eq_ceil_logb {Cg : ℝ} (hCg : 1 ≤ Cg) {x : ℕ} (hx : Real.log x ≠ 0) :
    cK Cg x = Nat.ceil (Real.logb 2 (tailBudget Cg x)) := by
  have h4Cg : (4 : ℝ) * Cg ≠ 0 := by positivity
  have hsq : Real.log x ^ 2 ≠ 0 := pow_ne_zero _ hx
  have he : Real.logb 2 (tailBudget Cg x)
      = Real.logb 2 (4 * Cg) + 2 * Real.logb 2 (Real.log x) := by
    unfold tailBudget Real.logb
    rw [show (4 : ℝ) * Cg * Real.log x ^ 2 = (4 * Cg) * Real.log x ^ 2 by ring,
      Real.log_mul h4Cg hsq, Real.log_pow]
    push_cast; ring
  rw [cK, he]

/-- Section 5(iv)'s tail-budget clause: `H_x ≤ 2^K`, direct from the
`ceil ≥ exact exponent` property. -/
theorem tailBudget_le_two_pow_cK {Cg : ℝ} (hCg : 1 ≤ Cg) {x : ℕ}
    (hx : Real.log x ≠ 0) : tailBudget Cg x ≤ 2 ^ cK Cg x := by
  rw [cK_eq_ceil_logb hCg hx]
  refine le_two_pow_ceil_logb ?_
  have hsq : Real.log x ^ 2 > 0 := by positivity
  unfold tailBudget; nlinarith

/-- The FM-2 input: `2^J ≥ (K+20)^4`, since `J = ceil(4 log2(K+20))` and
`4 log2 y = log2 (y^4)`. -/
theorem pow_le_two_pow_cJ {Cg : ℝ} (x : ℕ) :
    ((cK Cg x : ℝ) + 20) ^ 4 ≤ 2 ^ cJ Cg x := by
  have he : 4 * Real.logb 2 ((cK Cg x : ℝ) + 20)
      = Real.logb 2 (((cK Cg x : ℝ) + 20) ^ 4) := by
    unfold Real.logb
    rw [Real.log_pow]; push_cast; ring
  rw [cJ, he]
  exact le_two_pow_ceil_logb (by positivity)

/-- `4 log2 y ≤ y + 17` for `y > 0`: the crude `J = O(log K) ≪ K` estimate
of 5(iii). Via `log (y/8) ≤ y/8 - 1` (`Real.log_le_sub_one_of_pos`) and
`log 8 = 3 log 2`; reduced to `Real.log_two_gt_d9` (only `log 2 > 1/2` is
used, so the slack is large). -/
theorem four_logb_le {y : ℝ} (hy : 0 < y) : 4 * Real.logb 2 y ≤ y + 17 := by
  have hl2 : (0.5 : ℝ) < Real.log 2 := by linarith [Real.log_two_gt_d9]
  have h := Real.log_le_sub_one_of_pos (show (0:ℝ) < y / 8 by positivity)
  rw [Real.log_div hy.ne' (by norm_num),
    show Real.log 8 = 3 * Real.log 2 by
      rw [show (8:ℝ) = 2 ^ 3 by norm_num, Real.log_pow]; push_cast; ring] at h
  -- `log y ≤ y/8 + 3 log 2 - 1`; multiply out against `log 2 > 1/2`
  rw [Real.logb, ← mul_div_assoc, div_le_iff₀ (by linarith : (0:ℝ) < Real.log 2)]
  nlinarith [h, hl2, hy, mul_pos hy (by linarith : (0:ℝ) < Real.log 2 - 0.5)]

/-- Scaled refinement of `four_logb_le`: the linear coefficient can be made
as small as we like at the cost of an additive `4m`. Via
`log (y/2^m) ≤ y/2^m - 1` and `log (2^m) = m log 2` (exact, so no numeric
bound on any log other than `Real.log_two_gt_d9`'s `log 2 > 1/2` is used).
Used with `m = 9` in `cJ_le`, where `8/2^9 = 1/64` is the slack that makes
`L + 1 < 3 lnln x` (rather than merely `< 3.03 lnln x`) come out. -/
theorem four_logb_le_scaled (m : ℕ) {y : ℝ} (hy : 0 < y) :
    4 * Real.logb 2 y ≤ (8 / 2 ^ m) * y + 4 * m := by
  have hl2 : (0.5 : ℝ) < Real.log 2 := by linarith [Real.log_two_gt_d9]
  have hP : (0:ℝ) < 2 ^ m := by positivity
  have h := Real.log_le_sub_one_of_pos (show (0:ℝ) < y / 2 ^ m by positivity)
  rw [Real.log_div hy.ne' (by positivity), Real.log_pow] at h
  -- `log y - m log 2 ≤ y/2^m - 1`; divide by `log 2 > 1/2`
  rw [Real.logb, ← mul_div_assoc, div_le_iff₀ (by linarith : (0:ℝ) < Real.log 2)]
  have hkey : 0 ≤ (y / 2 ^ m) * (8 * Real.log 2 - 4) :=
    mul_nonneg (by positivity) (by linarith)
  have hexp : (8 / 2 ^ m) * y = (y / 2 ^ m) * 8 := by field_simp; ring
  rw [hexp]
  nlinarith [h, hl2, hkey]

/-- `2 log2 z ≤ 2.8854 ln z` for `ln z ≥ 0`: the base change `logb 2 = log / log 2`
against `2/ln 2 = 2.885390...`, reduced to `Real.log_two_gt_d9`. -/
theorem two_logb_le_of_nonneg {z : ℝ} (hz : 0 ≤ Real.log z) :
    2 * Real.logb 2 z ≤ 2.8854 * Real.log z := by
  have hl2 : (0.6931471803:ℝ) < Real.log 2 := Real.log_two_gt_d9
  have hl2p : (0:ℝ) < Real.log 2 := by linarith
  rw [Real.logb, ← mul_div_assoc, div_le_iff₀ hl2p]
  nlinarith [mul_nonneg hz (by linarith : (0:ℝ) ≤ 2.8854 * Real.log 2 - 2)]

/-- `A := log2 (4 C_g) > 0`, since `C_g ≥ 1` forces `4 C_g ≥ 4 > 1`. This is
what makes the `K`-ceiling argument nonnegative with no threshold on `x`. -/
theorem logb_four_Cg_pos {Cg : ℝ} (hCg : 1 ≤ Cg) : 0 < Real.logb 2 (4 * Cg) :=
  Real.logb_pos (by norm_num) (by linarith)

/-- `K ≤ A + 2.8854 lnln x + 1`, where `A = log2 (4 C_g)`: `Nat.ceil y < y + 1`
on the (nonnegative) defining argument, then `two_logb_le_of_nonneg`. -/
theorem cK_le {Cg : ℝ} (hCg : 1 ≤ Cg) {x : ℕ} (hx : 1 ≤ Real.log x) :
    (cK Cg x : ℝ) ≤ Real.logb 2 (4 * Cg) + 2.8854 * Real.log (Real.log x) + 1 := by
  have hA := logb_four_Cg_pos hCg
  have ht0 : 0 ≤ Real.log (Real.log x) := Real.log_nonneg hx
  have hnn0 : 0 ≤ Real.logb 2 (Real.log x) := Real.logb_nonneg (by norm_num) hx
  have h2 : 2 * Real.logb 2 (Real.log x) ≤ 2.8854 * Real.log (Real.log x) :=
    two_logb_le_of_nonneg ht0
  rw [cK]
  have hnn : 0 ≤ Real.logb 2 (4 * Cg) + 2 * Real.logb 2 (Real.log x) := by linarith
  have := (Nat.ceil_lt_add_one hnn).le
  linarith

/-- Section 5's `K ≥ 1`, for `ln x ≥ 1`: the ceiling argument is `> 0`. -/
theorem one_le_cK {Cg : ℝ} (hCg : 1 ≤ Cg) {x : ℕ} (hx : 1 ≤ Real.log x) : 1 ≤ cK Cg x := by
  have hA := logb_four_Cg_pos hCg
  have hnn0 : 0 ≤ Real.logb 2 (Real.log x) := Real.logb_nonneg (by norm_num) hx
  rw [cK, Nat.one_le_ceil_iff]
  linarith

/-- `J ≤ (1/64)(A + 2.8854 lnln x + 21) + 37`: `Nat.ceil y < y + 1`, `logb`
monotonicity against `cK_le`, then `four_logb_le_scaled` at `m = 9`. -/
theorem cJ_le_scaled {Cg : ℝ} (hCg : 1 ≤ Cg) {x : ℕ} (hx : 1 ≤ Real.log x) :
    (cJ Cg x : ℝ)
      ≤ (1/64) * (Real.logb 2 (4 * Cg) + 2.8854 * Real.log (Real.log x) + 21) + 37 := by
  have hA := logb_four_Cg_pos hCg
  have ht0 : 0 ≤ Real.log (Real.log x) := Real.log_nonneg hx
  have hcK := cK_le hCg hx
  have hc : (0:ℝ) ≤ (cK Cg x : ℝ) := Nat.cast_nonneg _
  set u := Real.logb 2 (4 * Cg) + 2.8854 * Real.log (Real.log x) + 21 with hudef
  have hu0 : (0:ℝ) < u := by rw [hudef]; linarith
  have hcKu : (cK Cg x : ℝ) + 20 ≤ u := by rw [hudef]; linarith
  have hcK20 : (0:ℝ) < (cK Cg x : ℝ) + 20 := by linarith
  have h1 : (cJ Cg x : ℝ) ≤ 4 * Real.logb 2 ((cK Cg x : ℝ) + 20) + 1 := by
    rw [cJ]
    refine (Nat.ceil_lt_add_one ?_).le
    have : (0:ℝ) ≤ Real.logb 2 ((cK Cg x : ℝ) + 20) :=
      Real.logb_nonneg (by norm_num) (by linarith)
    linarith
  have h2 : Real.logb 2 ((cK Cg x : ℝ) + 20) ≤ Real.logb 2 u :=
    Real.logb_le_logb_of_le (by norm_num) hcK20 hcKu
  have h3 := four_logb_le_scaled 9 hu0
  norm_num at h3
  linarith

/-- 5(iv)'s operative asymptotic, in the crude form the budget needs:
`L + 1 ≤ 1.015625 A + 2.930484375 lnln x + 41.328125 < 3 lnln x` once
`lnln x ≥ 16 A + 640`. The coefficient `2.9304... < 3` is the whole point;
the threshold is taken deliberately late. -/
theorem cL_lt {Cg : ℝ} (hCg : 1 ≤ Cg) {x : ℕ} (hx : 1 ≤ Real.log x)
    (ht : 16 * Real.logb 2 (4 * Cg) + 640 ≤ Real.log (Real.log x)) :
    ((cL (cJ Cg x) (cK Cg x) : ℝ) + 1 < 3 * Real.log (Real.log x)) := by
  have hA := logb_four_Cg_pos hCg
  have hcK := cK_le hCg hx
  have hcJ := cJ_le_scaled hCg hx
  have hL : ((cL (cJ Cg x) (cK Cg x) : ℕ) : ℝ) = (cJ Cg x : ℝ) + 2 + (cK Cg x : ℝ) := by
    rw [cL]; push_cast; ring
  rw [hL]
  linarith

/-- The ℕ-side crude span bound shared by `cword` and `cword'` (their spans
are the same expression, by `cspan_eq` / `cspan'_eq`): the prime window sits
below index `2L+5`, and `p_N < (N+2)^2`. -/
theorem cspan_lt_sq (J K : ℕ) :
    cprime (cL J K) (cL J K + 1) - cprime (cL J K) 0 < (2 * cL J K + 7) ^ 2 := by
  have h1 : cprime (cL J K) (cL J K + 1) - cprime (cL J K) 0
      ≤ cprime (cL J K) (cL J K + 1) := Nat.sub_le _ _
  have h2 : cprime (cL J K) (cL J K + 1) ≤ q (2 * cL J K + 5) := cprime_top_le_q _
  have h3 : q (2 * cL J K + 5) < (2 * cL J K + 5 + 2) ^ 2 := nth_prime_lt_sq (by omega)
  have h4 : (2 * cL J K + 5 + 2) ^ 2 = (2 * cL J K + 7) ^ 2 := by ring_nf
  omega

/-- `(2L+7)^2 ≤ (ln x)^3` for `ln x ≥ 44`, given `L + 1 < 3 lnln x`: chain
`2L+7 ≤ 6 lnln x + 7 ≤ 6 ln x + 1` (via `lnln x ≤ ln x - 1`) and
`(6s+1)^2 ≤ s^3` for `s ≥ 44`. Deliberately crude — `(lnln x)^2` against
`(ln x)^3` leaves enormous room. -/
theorem cube_bound {x : ℕ} (L : ℕ) (hx : (44:ℝ) ≤ Real.log x)
    (hL : (L : ℝ) + 1 < 3 * Real.log (Real.log x)) :
    ((2 * L + 7 : ℕ) : ℝ) ^ 2 ≤ Real.log x ^ 3 := by
  have hs0 : (0:ℝ) < Real.log x := by linarith
  have hs1 : (1:ℝ) ≤ Real.log x := by linarith
  have hlog : Real.log (Real.log x) ≤ Real.log x - 1 := Real.log_le_sub_one_of_pos hs0
  have ht0 : 0 ≤ Real.log (Real.log x) := Real.log_nonneg hs1
  have hLR : (0:ℝ) ≤ (L : ℝ) := Nat.cast_nonneg _
  have hcast : ((2 * L + 7 : ℕ) : ℝ) = 2 * (L : ℝ) + 7 := by push_cast; ring
  rw [hcast]
  have h1 : 2 * (L : ℝ) + 7 ≤ 6 * Real.log x + 1 := by linarith
  have h2 : (0:ℝ) ≤ 2 * (L : ℝ) + 7 := by linarith
  have h3 : (2 * (L : ℝ) + 7) ^ 2 ≤ (6 * Real.log x + 1) ^ 2 := by nlinarith [h1, h2]
  have h4 : (6 * Real.log x + 1) ^ 2 ≤ Real.log x ^ 3 := by
    nlinarith [hx, mul_nonneg (by linarith : (0:ℝ) ≤ Real.log x - 44) (sq_nonneg (Real.log x)),
      mul_nonneg (by linarith : (0:ℝ) ≤ Real.log x - 44) (by linarith : (0:ℝ) ≤ Real.log x)]
  linarith

/-- `1 ≤ J` UNCONDITIONALLY: `K + 20 ≥ 20 > 1`, so `logb 2 (K+20) > 0`
and the `ceil` of a positive real is at least 1. -/
theorem one_le_cJ {Cg : ℝ} (x : ℕ) : 1 ≤ cJ Cg x := by
  rw [cJ]
  apply Nat.lt_ceil.mpr
  have hK0 : (0:ℝ) ≤ (cK Cg x : ℝ) := Nat.cast_nonneg _
  have hpos : (0:ℝ) < Real.logb 2 ((cK Cg x : ℝ) + 20) :=
    Real.logb_pos (by norm_num) (by linarith)
  push_cast
  linarith

/-- `J = O(log K) ≪ K`, in the crude form `J ≤ K + 38` that 5(iii) needs
(via `four_logb_le` and `⌈y⌉₊ < y + 1`). -/
theorem cJ_le {Cg : ℝ} (x : ℕ) : (cJ Cg x : ℝ) ≤ (cK Cg x : ℝ) + 38 := by
  have hK0 : (0:ℝ) ≤ (cK Cg x : ℝ) := Nat.cast_nonneg _
  have hpos : (0:ℝ) ≤ 4 * Real.logb 2 ((cK Cg x : ℝ) + 20) := by
    have := Real.logb_pos (b := 2) (x := (cK Cg x : ℝ) + 20) (by norm_num) (by linarith)
    linarith
  have hceil := Nat.ceil_lt_add_one hpos
  have hfl := four_logb_le (y := (cK Cg x : ℝ) + 20) (by linarith)
  rw [cJ]
  linarith

/-- `L ≤ 2(K+20)` (from `cJ_le`). -/
theorem cL_le {Cg : ℝ} (x : ℕ) :
    (cL (cJ Cg x) (cK Cg x) : ℝ) ≤ 2 * ((cK Cg x : ℝ) + 20) := by
  have h := cJ_le (Cg := Cg) x
  rw [cL]; push_cast; linarith

/-- `ln L ≤ K + 20` (from `cL_le`, `ln 2 ≤ 1` and `ln u ≤ u - 1`). -/
theorem log_cL_le {Cg : ℝ} (x : ℕ) :
    Real.log (cL (cJ Cg x) (cK Cg x) : ℝ) ≤ (cK Cg x : ℝ) + 20 := by
  have hK0 : (0:ℝ) ≤ (cK Cg x : ℝ) := Nat.cast_nonneg _
  have hL2 : (2:ℝ) ≤ (cL (cJ Cg x) (cK Cg x) : ℝ) := by
    rw [cL]; push_cast
    have : (0:ℝ) ≤ (cJ Cg x : ℝ) := Nat.cast_nonneg _
    linarith
  have hstep : Real.log (cL (cJ Cg x) (cK Cg x) : ℝ)
      ≤ Real.log (2 * ((cK Cg x : ℝ) + 20)) :=
    Real.log_le_log (by linarith) (cL_le x)
  have hmul : Real.log (2 * ((cK Cg x : ℝ) + 20))
      = Real.log 2 + Real.log ((cK Cg x : ℝ) + 20) :=
    Real.log_mul (by norm_num) (by linarith)
  have hlog2 : Real.log 2 ≤ 1 := by
    have := Real.log_le_sub_one_of_pos (by norm_num : (0:ℝ) < 2); linarith
  have hlogu : Real.log ((cK Cg x : ℝ) + 20) ≤ ((cK Cg x : ℝ) + 20) - 1 :=
    Real.log_le_sub_one_of_pos (by linarith)
  rw [hmul] at hstep
  linarith

/-- `K → ∞` as `x → ∞`: its `logb`-of-`log` argument diverges and `ceil`
is monotone. Unconditional in `C_g` (the `logb 2 (4 C_g)` term is an
additive constant). Supplies both `1 ≤ K` eventually and FM-2's decay. -/
theorem cK_tendsto {Cg : ℝ} :
    Filter.Tendsto (fun x : ℕ => (cK Cg x : ℝ)) Filter.atTop Filter.atTop := by
  have hlogx : Filter.Tendsto (fun x : ℕ => Real.log x) Filter.atTop Filter.atTop :=
    Real.tendsto_log_atTop.comp tendsto_natCast_atTop_atTop
  have hloglog : Filter.Tendsto (fun x : ℕ => Real.log (Real.log x))
      Filter.atTop Filter.atTop := Real.tendsto_log_atTop.comp hlogx
  have hlogb : Filter.Tendsto (fun x : ℕ => Real.logb 2 (Real.log x))
      Filter.atTop Filter.atTop := by
    unfold Real.logb
    exact Filter.Tendsto.atTop_div_const (by positivity) hloglog
  have harg : Filter.Tendsto
      (fun x : ℕ => Real.logb 2 (4 * Cg) + 2 * Real.logb 2 (Real.log x))
      Filter.atTop Filter.atTop :=
    Filter.tendsto_atTop_add_const_left _ _ (hlogb.const_mul_atTop (by norm_num))
  exact Filter.tendsto_atTop_mono (fun x => Nat.le_ceil _) harg

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
  obtain ⟨C, hC1, hq⟩ := q_le_mul_log
  refine ⟨12 * C, by linarith, fun J K hJ hK => ?_⟩
  set L := cL J K with hLdef
  have hL4 : 4 ≤ L := by simp only [hLdef, cL]; omega
  have hLR : (4 : ℝ) ≤ (L : ℝ) := by exact_mod_cast hL4
  have hlogL : 0 < Real.log (L : ℝ) := Real.log_pos (by linarith)
  -- the master bound: the top of the prime window, via index `≤ 2L+5`
  have htop : (cprime L (L + 1) : ℝ) ≤ 12 * C * (L : ℝ) * Real.log (L : ℝ) := by
    have hnat : cprime L (L + 1) ≤ q (2 * L + 5) := cprime_top_le_q L
    have hc : (cprime L (L + 1) : ℝ) ≤ (q (2 * L + 5) : ℝ) := by exact_mod_cast hnat
    exact hc.trans (q_window_le hC1 hq L hL4)
  have hzero_nn : (0 : ℝ) ≤ (cprime L 0 : ℝ) := by positivity
  have hlogmono : Real.log (L : ℝ) ≤ Real.log ((L : ℝ) + 2) :=
    Real.log_le_log (by linarith) (by linarith)
  have hCL_nn : (0 : ℝ) ≤ 12 * C * (L : ℝ) := by nlinarith
  refine ⟨by linarith, ?_, ?_, ?_⟩
  · -- conjunct 2: `gamma` is one gap inside the window, so `≤ q_{L+1}`
    have h1 : cgamma J K ≤ cprime L (L + 1) := by
      have hstep : cprime (cL J K) (cI J + 1) ≤ cprime L (L + 1) := by
        rcases Nat.lt_or_ge (cI J + 1) (L + 1) with h | h
        · exact (cprime_lt_cprime _ h).le
        · have he : cI J + 1 = L + 1 := by simp only [hLdef, cL, cI] at h ⊢; omega
          rw [← hLdef] at *; rw [he]
      exact le_trans (by simp only [cgamma, ← hLdef]; exact Nat.sub_le _ _) hstep
    have h2 : (cgamma J K : ℝ) ≤ (cprime L (L + 1) : ℝ) := by exact_mod_cast h1
    linarith
  · -- conjunct 3: the span of `w`, via the endpoint lemma, then `ln L ≤ ln (L+2)`
    rw [cspan_eq J K, ← hLdef]
    have hsub : ((cprime L (L + 1) - cprime L 0 : ℕ) : ℝ) ≤ (cprime L (L + 1) : ℝ) := by
      exact_mod_cast Nat.sub_le (cprime L (L + 1)) (cprime L 0)
    nlinarith [hsub, htop, hlogmono, hCL_nn]
  · -- conjunct 4: identical, for `w'`
    rw [cspan'_eq J K, ← hLdef]
    have hsub : ((cprime L (L + 1) - cprime L 0 : ℕ) : ℝ) ≤ (cprime L (L + 1) : ℝ) := by
      exact_mod_cast Nat.sub_le (cprime L (L + 1)) (cprime L 0)
    nlinarith [hsub, htop, hlogmono, hCL_nn]

/-- Section 5(iii), the limit: `(gamma + 4)/2^J ≤ 3 C_1/(K+20)^2 → 0`,
using `L ≤ 2(K+20)` and `ln L ≤ K+20` for large `x`. Stated in the shape
`SmallTailForkMerge`'s (FM-2) consumes. -/
theorem cfm2_tendsto {Cg : ℝ} (hCg : 1 ≤ Cg) :
    Filter.Tendsto
      (fun x : ℕ => ((cgamma (cJ Cg x) (cK Cg x) : ℝ) + 4) / 2 ^ cJ Cg x)
      Filter.atTop (nhds 0) := by
  obtain ⟨C₁, hC₁, hspan⟩ := cspan_le
  have hcK : Filter.Tendsto (fun x : ℕ => (cK Cg x : ℝ)) Filter.atTop Filter.atTop :=
    cK_tendsto
  have hden : Filter.Tendsto (fun x : ℕ => ((cK Cg x : ℝ) + 20) ^ 2)
      Filter.atTop Filter.atTop := by
    refine Filter.tendsto_atTop_mono (fun x => ?_)
      (Filter.tendsto_atTop_add_const_right _ 20 hcK)
    have hK0 : (0:ℝ) ≤ (cK Cg x : ℝ) := Nat.cast_nonneg _
    nlinarith
  -- the majorant `3 C₁ / (K+20)^2 → 0`
  have hmaj : Filter.Tendsto (fun x : ℕ => 3 * C₁ / ((cK Cg x : ℝ) + 20) ^ 2)
      Filter.atTop (nhds 0) := Filter.Tendsto.div_atTop tendsto_const_nhds hden
  refine tendsto_of_tendsto_of_tendsto_of_le_of_le' tendsto_const_nhds hmaj ?_ ?_
  · -- nonnegativity of the LHS is free
    filter_upwards with x
    positivity
  · filter_upwards [hcK.eventually_ge_atTop 1] with x hx1
    have hK1 : 1 ≤ cK Cg x := by exact_mod_cast hx1
    have hJ1 : 1 ≤ cJ Cg x := one_le_cJ x
    obtain ⟨-, hgam, -, -⟩ := hspan (cJ Cg x) (cK Cg x) hJ1 hK1
    set K : ℝ := (cK Cg x : ℝ) with hKdef
    have hK20 : (21:ℝ) ≤ K + 20 := by rw [hKdef]; linarith
    have hL2 : (2:ℝ) ≤ (cL (cJ Cg x) (cK Cg x) : ℝ) := by
      rw [cL]; push_cast
      have h1 : (0:ℝ) ≤ (cJ Cg x : ℝ) := Nat.cast_nonneg _
      have h2 : (0:ℝ) ≤ (cK Cg x : ℝ) := Nat.cast_nonneg _
      linarith
    have hlognn : 0 ≤ Real.log (cL (cJ Cg x) (cK Cg x) : ℝ) :=
      Real.log_nonneg (by linarith)
    -- `gamma ≤ C₁ L ln L ≤ C₁ · 2(K+20) · (K+20) = 2 C₁ (K+20)^2`
    have hgam2 : (cgamma (cJ Cg x) (cK Cg x) : ℝ) ≤ 2 * C₁ * (K + 20) ^ 2 := by
      calc (cgamma (cJ Cg x) (cK Cg x) : ℝ)
          ≤ C₁ * (cL (cJ Cg x) (cK Cg x) : ℝ) * Real.log (cL (cJ Cg x) (cK Cg x) : ℝ) := hgam
        _ ≤ C₁ * (2 * (K + 20)) * (K + 20) := by
            apply mul_le_mul _ (log_cL_le x) hlognn (by nlinarith)
            exact mul_le_mul_of_nonneg_left (cL_le x) (by linarith)
        _ = 2 * C₁ * (K + 20) ^ 2 := by ring
    have h4 : (4:ℝ) ≤ C₁ * (K + 20) ^ 2 := by nlinarith
    have hnum : (cgamma (cJ Cg x) (cK Cg x) : ℝ) + 4 ≤ 3 * C₁ * (K + 20) ^ 2 := by linarith
    have hpow : (K + 20) ^ 4 ≤ 2 ^ cJ Cg x := pow_le_two_pow_cJ x
    calc ((cgamma (cJ Cg x) (cK Cg x) : ℝ) + 4) / 2 ^ cJ Cg x
        ≤ (3 * C₁ * (K + 20) ^ 2) / (K + 20) ^ 4 :=
          div_le_div₀ (by nlinarith) hnum (by positivity) hpow
      _ = 3 * C₁ / (K + 20) ^ 2 := by field_simp; ring

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
  have hA := logb_four_Cg_pos hCg
  -- the two thresholds: `ln x ≥ 44` (span) and `lnln x ≥ 16 A + 640` (the `< 3 lnln x` clause)
  have hs_top : Filter.Tendsto (fun x : ℕ => Real.log x) Filter.atTop Filter.atTop :=
    Real.tendsto_log_atTop.comp (tendsto_natCast_atTop_atTop (R := ℝ))
  have ht_top : Filter.Tendsto (fun x : ℕ => Real.log (Real.log x)) Filter.atTop Filter.atTop :=
    Real.tendsto_log_atTop.comp hs_top
  have hev1 := hs_top.eventually_ge_atTop (44:ℝ)
  have hev2 := ht_top.eventually_ge_atTop (16 * Real.logb 2 (4 * Cg) + 640)
  rw [Filter.eventually_atTop] at hev1 hev2
  obtain ⟨x₁, hx₁⟩ := hev1
  obtain ⟨x₂, hx₂⟩ := hev2
  refine ⟨max x₁ x₂, fun x hx => ?_⟩
  have hs : (44:ℝ) ≤ Real.log x := hx₁ x (le_trans (le_max_left _ _) hx)
  have ht : 16 * Real.logb 2 (4 * Cg) + 640 ≤ Real.log (Real.log x) :=
    hx₂ x (le_trans (le_max_right _ _) hx)
  have hs1 : (1:ℝ) ≤ Real.log x := by linarith
  have ht1 : (1:ℝ) ≤ Real.log (Real.log x) := by linarith
  have h4 := cL_lt hCg hs1 ht
  -- the span clause, shared by `w` and `w'` via their common span expression
  have hspan : ∀ w : ℕ → ℕ,
      offsetSpan (wordPointSet w (cL (cJ Cg x) (cK Cg x)))
          = cprime (cL (cJ Cg x) (cK Cg x)) (cL (cJ Cg x) (cK Cg x) + 1)
            - cprime (cL (cJ Cg x) (cK Cg x)) 0 →
      ((offsetSpan (wordPointSet w (cL (cJ Cg x) (cK Cg x))) : ℝ) ≤ Real.log x ^ 3) := by
    intro w hw
    rw [hw]
    have hnat := cspan_lt_sq (cJ Cg x) (cK Cg x)
    have hcast : ((cprime (cL (cJ Cg x) (cK Cg x)) (cL (cJ Cg x) (cK Cg x) + 1)
        - cprime (cL (cJ Cg x) (cK Cg x)) 0 : ℕ) : ℝ)
          ≤ ((2 * cL (cJ Cg x) (cK Cg x) + 7 : ℕ) : ℝ) ^ 2 := by
      have : ((cprime (cL (cJ Cg x) (cK Cg x)) (cL (cJ Cg x) (cK Cg x) + 1)
          - cprime (cL (cJ Cg x) (cK Cg x)) 0 : ℕ) : ℝ)
            ≤ (((2 * cL (cJ Cg x) (cK Cg x) + 7) ^ 2 : ℕ) : ℝ) := by
        exact_mod_cast hnat.le
      simpa using this
    exact le_trans hcast (cube_bound _ hs h4)
  exact ⟨one_le_cJ x, one_le_cK hCg hs1,
    tailBudget_le_two_pow_cK hCg (by linarith : Real.log x ≠ 0), h4, by linarith, by linarith,
    hspan _ (cspan_eq _ _), hspan _ (cspan'_eq _ _)⟩

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
