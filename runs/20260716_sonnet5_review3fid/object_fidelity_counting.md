# Transcription-fidelity object: counting layer and deletion construction

Three parts. Part I is the prose source (sections 1, 2, 4, 5 of a
conditional-proof document; sections 3 and 6-9 exist but are outside
this object). Part II is a Lean 4 statement file claiming to transcribe
prose sections 4-5; it is the object under assessment. Part III is the
frozen Lean context Part II imports (NOT under assessment; provided so
every symbol resolves). Pointers in Part II to "section 6" refer to the
out-of-scope assembly and are to be treated as opaque.

---

## PART I -- prose source

## 1. Main statement

Notation: p_1 = 2 < p_2 = 3 < ... are the primes, g_n = p_{n+1} - p_n,
S = sum_{n>=1} p_n 2^{-n}, and for H = {0 = h_0 < h_1 < ... < h_k} a set of
even integers, pi_H(x) = #{p <= x : p + h_i prime for all i},
M_H(x) = S(H) x / (ln x)^{k+1} with S(H) the singular series. H is
admissible if for every prime q the offsets do not cover all residues
mod q.

HYPOTHESIS A (uniform two-sided tuple counts). There exists x_A such that
for all x >= x_A and every admissible H with k+1 <= 4 lnln x and
h_k <= (ln x)^3:
    (1/2) M_H(x) <= pi_H(x) <= 2 M_H(x).
Design note: all in-budget masses satisfy
M_H(x) >= x^{1-o(1)} >> 1 by Lemma 4.1, so a fixed two-sided factor is
integrality-safe. A relative-error demand on CONSECUTIVE-gap counts would
be unconditionally false (single-gap words near (ln x)^3 have model mass
e^{-(1+o(1))(ln x)^2} < 1, leaving no admissible integer count); this
document therefore DERIVES consecutiveness (Lemma 4.3) instead of assuming
counts for it. If one prefers an error form, |pi_H - M_H| <= (1/3)M_H + x^t
with fixed t < 1 also suffices verbatim.

HYPOTHESIS B (Cramer-Granville). There exist C_g >= 1 and nu_B such that
g_nu <= C_g (ln p_nu)^2 for all nu >= nu_B (C_g >= 1 is WLOG by
monotonicity; section 5 takes log2(4 C_g)).

THEOREM. Assume A and B. Then S is irrational, and so is the 0-indexed
variant sum_{n>=0} (Nat.nth Prime n)/2^n = 2S.

Remark on strength: the package is NOT circular, but clause
B is a global pointwise gap bound, materially stronger than a pure tuple
hypothesis. The sharpest known weakening target is the two-word variance
estimate of section 8.3.

## 2. Elementary layer

LEMMA 2.1 (convergence). p_n <= C_0 n ln(n+2) for all n, with an
absolute C_0 (Chebyshev; classical, e.g. Hardy-Wright, An Introduction to
the Theory of Numbers, Thm 8 area; citation verification pending). Hence sum p_n 2^{-n} converges absolutely, as do all tails
u_n = sum_{k>=1} p_{n+k} 2^{-k}, and
    delta_n := u_n - p_{n+1} = sum_{j>=1} g_{n+j} 2^{-j},
    delta_{n+1} = 2 delta_n - g_{n+1},  delta_n >= 2 for n >= 1.
(The absolute convergence licenses the rearrangement defining delta_n;
the bound p_n <= 2^n alone would not.)

LEMMA 2.2 (block identity). For T >= 1:
delta_n = sum_{i=1}^T g_{n+i} 2^{-i} + 2^{-T} delta_{n+T}.

LEMMA 2.3 (lattice and parity). Suppose S = a/(2^s b) with
a, s, b positive integers, b odd, and WLOG s >= 1 (the representation need
not be reduced: a/(2^0 b) = 2a/(2^1 b)). Then b delta_n is an integer for
all n >= s, and an EVEN integer for all n >= s+1.
Proof. 2^n b S = 2^{n-s} a and b sum_{j<=n} p_j 2^{n-j} are integers, so
b u_n and b delta_n = b u_n - b p_{n+1} are integers for n >= s. Parity:
for n >= s, b delta_{n+1} = 2(b delta_n) - b g_{n+1}, and g_{n+1} =
p_{n+2} - p_{n+1} is a difference of odd primes since n+1 >= s+1 >= 2,
hence even; b odd makes b g_{n+1} even. QED
(For s = 0 the step n = 0 would use g_1 = 1, which is odd; the WLOG
removes the edge.)

LEMMA 2.4 (quantization). If n, m >= s+1 share a common gap prefix,
g_{n+i} = g_{m+i} for 1 <= i <= J, then
b(delta_{n+J} - delta_{m+J}) is an integer multiple of 2^{J+1}.
Proof. Subtract Lemma 2.2 at n and m (prefix sums cancel):
delta_n - delta_m = 2^{-J}(delta_{n+J} - delta_{m+J}). Multiply by b and
use Lemma 2.3 (even lattice at n, m >= s+1). QED

LEMMA 2.5. An integer multiple of 2^{J+1} of absolute value < 2^{J+1}
is 0.

## 4. Counting layer (conditional on A; classical citations)

Throughout, l = ln x. "Consecutive realization of a gap word w =
(w_1,...,w_L) at n" means g_{n+i} = w_i for all i, equivalently: the L+1
primes p_{n+1}, ..., p_{n+L+1} occupy exactly the point set of w with no
prime in between.

LEMMA 4.1 (singular series lower bound). For admissible H of even offsets,
|H| = k+1, S(H) >= exp(-C k ln(k+2)). Consequently, in the budget of
Hypothesis A, M_H(x) >= x exp(-C k ln(k+2) - (k+1) lnln x) = x^{1-o(1)}.
Proof sketch: local factors at p <= k+2 are >= 1/p by
admissibility; at k+2 < p <= 2(k+1) crude bounds give a factor e^{-O(k)};
at 2(k+1) < p <= D the exponential estimates apply since nu/p < 1/2; at
p > D all offsets are distinct mod p and log-factors sum to o(k). Uses
Mertens' theorems (classical: Mertens 1874; Rosser-Schoenfeld 1962);
exact-constant verification pending. QED-sketch

LEMMA 4.2 (one-point extension sum). For any fixed kappa >= 1 there
is C_2 = C_2(kappa) such that for admissible H as above with span
D = h_k <= kappa k ln(k+2): the sum over even t in (0, D), t not in H,
H u {t} admissible, of S(H u {t})/S(H) is <= C_2 k (ln(k+2))^2.
Proof sketch: the local ratio at non-colliding p is
(1-(nu+1)/p)/((1-nu/p)(1-1/p)) <= 1 - (p-1)^{-2} < 1; colliding primes
p > 2(k+1) divide some t - h_i, each difference is <= D, so there are
at most (k+1) ln D / ln(2k+2) = O_kappa(k) of them, their reciprocals
sum to O_kappa(1) (each p - 1 > 2k+1), and their product of local
factors p/(p-1) is e^{O_kappa(1)}; primes <= 2(k+1) contribute
<= C ln(k+2) by Mertens; there are
<= D/2 <= (kappa/2) k ln(k+2) values of t, now BY HYPOTHESIS. QED-sketch
[Note: kappa-uniform bounds "number <= 3k" and "product <= e^2"
FAIL for large fixed kappa (H = {0, 10014}, t = 10010 = 2*5*7*11*13
has four colliding primes at k = 1; a highly composite t drives the
collision product past e^2 -- prod_{5<=p<=10^6} p/(p-1) = 8.202... >
e^2 = 7.389...; a sharper witness needs only kappa >= 405:
H = {0, 444}, t = 70, colliding primes {5, 7, 11, 17}); the O_kappa
forms above are the honest ones.]
[Note: the span hypothesis is NECESSARY, not cosmetic. For H = {0, D}
(k = 1) every admissible even t has ratio >= 1.2 (the p = 2 factor
alone is 2) and there are ~D/2 such t, so the sum grows like D against
a D-free right side; the unrestricted claim is FALSE.]

LEMMA 4.3 (consecutive lower bound; the transfer). Let w be a gap
word whose point set H(w) is admissible, |H(w)| = L+1 <= 4 lnln x - 1,
span <= kappa L ln(L+2) for a fixed kappa >= 1 (hence far inside the
(ln x)^3 budget of A). Under Hypothesis A, for all large x the number of
consecutive realizations of w with p_{n+1} in (sqrt x, x] is
    N_cons(w; x) >= (1/4) M_{H(w)}(x) >= 1.
Proof. A realization of the point set fails to be consecutive iff some
extra prime sits at an interior even offset t (odd offsets and p > D make
non-even positions composite for p > x^{1/2}). Inadmissible
extensions have count 0 unconditionally: a covering prime q <= L+2 < sqrt x
would have to divide a prime > sqrt x. Admissible extensions are in the
budget of A (L+2 points, +1 -- the cardinalities are L+1 and
L+2, and the budget constant 4 in A leaves slack; 3 would asymptotically
suffice). Union bound (exact, first Bonferroni level):
N_cons >= pi_H(x) - sum_t pi_{H u t}(x) - pi_H(sqrt x)
       >= (1/2) M_H - 2 sum_t M_{H u t} - sqrt x
       >= (1/2) M_H - 2 C_2(kappa) k (ln(k+2))^2 M_H / l - sqrt x
       >= (1/4) M_H,
using Lemma 4.2 (k = L; the span hypothesis here is exactly 4.2's),
M_{H u t} = S(H u t) x/l^{k+2}, and M_H >= x^{1-o(1)} >> sqrt x
(Lemma 4.1). QED
[Note: the wide form span <= (ln x)^3 is unprovable by this route
(Lemma 4.2's sum genuinely grows with the span) and heuristically false
outright for span >> ln x, where consecutive realizations carry a
Cramer-type e^{-span/ln x} thinning absent from M_H. Section 5(iii)
supplies exactly the narrow form.]
[EXPLICIT one-line lemma, stated here for the record even
though this architecture does not need a T_x identity: every start index
carries exactly one length-L gap word; only budget filters remove indices.]

LEMMA 4.4 (tail bound from B). Under Hypothesis B there is nu_1 with
delta_nu <= 3 C_g (ln p_nu)^2 for all nu >= nu_1.
Proof. g_{nu+j} <= C_g (ln p_{nu+j})^2, and p_{nu+j} < 2^j p_nu (Bertrand,
classical), so ln p_{nu+j} < ln p_nu + j; then
delta_nu <= C_g sum_j (ln p_nu + j)^2 2^{-j}
         <= C_g (2 (ln p_nu)^2 + 2 * 6) <= 3 C_g (ln p_nu)^2
for (ln p_nu)^2 >= 12, using (a+b)^2 <= 2a^2 + 2b^2 and
sum j^2 2^{-j} = 6. QED

## 5. The deletion construction

Fix x large. Set
    K = ceil(log2(4 C_g) + 2 log2 ln x),   J = ceil(4 log2(K + 20)),
    L = J + 2 + K,   H_x = 4 C_g (ln x)^2  (so 2^K >= H_x).
Let q_0 < q_1 < ... < q_{L+1} be the first L+2 primes exceeding L+3, put
i_0 = J + 1 (interior with slack: 1 <= i_0 and i_0 + 1 <= L since
J, K >= 1), gamma = q_{i_0+1} - q_{i_0} (even),
and define the two point sets
    A  = {q_0, ..., q_{L+1}} minus {q_{i_0+1}},
    A' = {q_0, ..., q_{L+1}} minus {q_{i_0}},
with gap words w, w' (each of length L); the 0-based point sets that
Lemma 4.3 and Hypothesis A receive are H(w) = A - q_0 and
H(w') = A' - q_0 (translation changes neither gaps nor
admissibility). Then:
(i) w and w' share the length-J prefix and the length-K suffix, and
their middle two entries differ by (-gamma, +gamma) in the natural
order (w, w'); section 6 swaps the names to give FM-F's (+gamma,
-gamma) orientation -- direct computation.
(ii) Both point sets are admissible: for p <= L+2 the residue class of 0
is unoccupied before translation (all q_j > L+3 > p), and for p > L+2
there are only L+1 < p points.
(iii) span <= q_{L+1} - q_0 <= C_1 L ln L, C_1 >= 1 fixed (Chebyshev
upper bound on
p_{2L+4}; classical), hence gamma <= C_1 L ln L and, since
L <= 2(K+20) and ln L <= K+20 for large x,
    (gamma + 4)/2^J <= 3 C_1 / (K+20)^2 -> 0.
(iv) Budgets: the words have L + 1 points with
L + 1 = (2/ln 2) lnln x + O(lnlnln x) < 3 lnln x eventually, meeting
Lemma 4.3's L + 1 <= 4 lnln x - 1 with room; one-point extensions then
have L + 2 <= 4 lnln x; span <= (ln x)^3 easily (the operative span
bound is (iii)).

---

## PART II -- Lean statement file under assessment

```lean
import Mathlib
import Erdos251.Basic
import Erdos251.Hypotheses

/-!
# Counting layer and deletion construction (prose sections 4-5)

STATEMENT SKELETON. Definitions are real; the lemmata are intentional,
named `sorry`s: the statement set is the object under transcription
assessment against Part I.

Source of truth: Part I of this object (prose sections 1, 2, 4, 5);
hypothesis-layer context in Part III.

## Index conventions (inherited from `Basic.lean`, unchanged)
* `q n = Nat.nth Nat.Prime n` is 0-indexed: `q 0 = 2 = ` paper `p_1`, so
  paper `p_ν` is `q (ν - 1)`.
* `gap n` = paper `g_{n+1}`; `delta n` = paper `delta_n` (no shift).
* Paper "consecutive realization of `w = (w_1,...,w_L)` at `n`" is
  `∀ j < L, gap (n + j) = w j` with the 0-indexed word `w j = ` paper
  `w_{j+1}`; the anchor prime `p_{n+1}` is `q n`.

## Traceability table

| Lean declaration                | prose ref                | constants / notes                                  |
|---------------------------------|--------------------------|----------------------------------------------------|
| `IsConsecRealization`           | sec. 4 preamble          | -- (definition)                                    |
| `wordPointSet`                  | sec. 4 preamble, 5       | -- ; 0-based `H(w)`, prefix sums (= `A - q_0`)     |
| `offsetSpan`                    | 4.2 `D = h_k`, 5(iii)    | -- ; `Finset.sup id`, total (0 on `∅`)             |
| `oneExtensions`                 | 4.2 range of `t`         | -- ; even `t ∈ (0, D)`, `t ∉ H`, `H ∪ {t}` adm.    |
| `consCount`                     | 4.3 `N_cons(w; x)`       | -- ; anchor `q n ∈ (√x, x]`                        |
| `singularSeries_lower_bound`    | LEMMA 4.1 (both clauses) | `C` (shared by both clauses; `0 < C` added)        |
| `oneExtension_sum_le`           | LEMMA 4.2                | `κ ≥ 1` explicit param, `C₂ = C₂(κ)`               |
| `consCount_lower_bound`         | LEMMA 4.3                | `κ ≥ 1` explicit param; factors `1/4`, `1`         |
| `delta_le_of_gap_bound`         | LEMMA 4.4                | `C_g` threaded explicitly; factor `3`              |
| `cK`, `cJ`, `cL`, `cI`          | sec. 5 constants         | `K`, `J`, `L = J+2+K`, `i_0 = J+1`       |
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
at the concrete tables `(J,K) = (3,4)` and `(2,3)`.

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
handoff object Lemma 4.3 and Hypothesis A receive;
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
(`= x^{1-o(1)}`, which is prose and is NOT transcribed).
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

/-- LEMMA 4.2 (one-point extension sum). For any fixed `κ ≥ 1`
there is `C₂ = C₂(κ)` such that for admissible `H` of even offsets with
span `D = h_k ≤ κ k ln(k+2)`, the sum over the one-point extensions of
`S(H ∪ {t})/S(H)` is `≤ C₂ k (ln(k+2))^2`.

The span hypothesis is NECESSARY, not cosmetic: for `H = {0,D}`
(`k = 1`) every admissible even `t` has ratio `≥ 1.2` (the `p = 2` factor
alone is 2) and there are `~D/2` such `t`, so the sum grows like `D`
against a `D`-free right side; the unrestricted form is FALSE. -/
theorem oneExtension_sum_le (κ : ℝ) (hκ : 1 ≤ κ) :
    ∃ C₂ : ℝ, ∀ H : Finset ℕ, 0 ∈ H → (∀ h ∈ H, Even h) → IsAdmissible H →
      (offsetSpan H : ℝ) ≤ κ * ((H.card : ℝ) - 1) * Real.log ((H.card : ℝ) + 1) →
      ∑ t ∈ oneExtensions H, singularSeries (insert t H) / singularSeries H
        ≤ C₂ * ((H.card : ℝ) - 1) * Real.log ((H.card : ℝ) + 1) ^ 2 := by
  sorry

/-- LEMMA 4.3 (consecutive lower bound; the transfer). Let `w` be a
gap word whose point set `H(w)` is admissible, `|H(w)| = L+1 ≤ 4 lnln x - 1`,
span `≤ κ L ln(L+2)` for a fixed `κ ≥ 1` (hence far inside A's `(ln x)^3`
budget). Under Hypothesis A, for all large `x`:
`N_cons(w; x) ≥ (1/4) M_{H(w)}(x) ≥ 1`.

The span hypothesis is 4.2's, with `k = L`: the wide form
`span ≤ (ln x)^3` is unprovable by this route and heuristically false
outright for `span ≫ ln x` (Cramer-type thinning absent from `M_H`).
Evenness of the offsets is not hypothesised: it follows from
admissibility, since `0 ∈ H(w)` and an odd offset would occupy both
classes mod 2. -/
theorem consCount_lower_bound (hA : HLQuantA) (κ : ℝ) (hκ : 1 ≤ κ) :
    ∃ x₀ : ℕ, ∀ x : ℕ, x₀ ≤ x → ∀ (w : ℕ → ℕ) (L : ℕ),
      IsAdmissible (wordPointSet w L) →
      (wordPointSet w L).card = L + 1 →
      ((L : ℝ) + 1) ≤ 4 * Real.log (Real.log x) - 1 →
      (offsetSpan (wordPointSet w L) : ℝ) ≤ κ * (L : ℝ) * Real.log ((L : ℝ) + 2) →
      modelMass (wordPointSet w L) x / 4 ≤ (consCount w L x : ℝ)
        ∧ 1 ≤ consCount w L x := by
  sorry

/-- LEMMA 4.4 (tail bound from B). Under Hypothesis B there is `ν_1` with
`delta_ν ≤ 3 C_g (ln p_ν)^2` for all `ν ≥ ν_1`.

Index map: paper `delta_ν` is `delta ν` and paper `p_ν` is `q (ν - 1)`,
so `ν = n + 1` gives the ℕ-subtraction-free form below. `C_g` is threaded
as an explicit parameter rather than re-existentialised, which is what
keeps the factor `3` meaningful (`∃ C, delta ≤ 3 * C * ...` would be
vacuous). The hypothesis is exactly the body of the frozen
`CramerGranville`, which binds `∃ C : ℝ` with no sign or size constraint;
the frozen definition is not touched. -/
theorem delta_le_of_gap_bound {Cg : ℝ} {n₀ : ℕ}
    (hB : ∀ n : ℕ, n₀ ≤ n → (gap n : ℝ) ≤ Cg * Real.log (q n) ^ 2) :
    ∃ n₁ : ℕ, ∀ n : ℕ, n₁ ≤ n → delta (n + 1) ≤ 3 * Cg * Real.log (q n) ^ 2 := by
  sorry

/-! ## Section 5: the deletion construction -/

/-- Section 5: `K = ceil(log2(4 C_g) + 2 log2 ln x)`. -/
def cK (Cg : ℝ) (x : ℕ) : ℕ :=
  Nat.ceil (Real.logb 2 (4 * Cg) + 2 * Real.logb 2 (Real.log x))

/-- Section 5: `J = ceil(4 log2(K + 20))`. -/
def cJ (Cg : ℝ) (x : ℕ) : ℕ := Nat.ceil (4 * Real.logb 2 ((cK Cg x : ℝ) + 20))

/-- Section 5: `L = J + 2 + K`, the common word length. -/
def cL (J K : ℕ) : ℕ := J + 2 + K

/-- Section 5: the deletion index `i_0 = J + 1`. Interior with slack: `1 ≤ i_0` and `i_0 + 1 ≤ L` since
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
`if`; `A` is not carried as a separate `Finset` . `cElem J K 0 = q_0`, and `t` ranges over `0..L`. -/
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

/-! ### Section 5 property lemmata -/

/-- Section 5(i), prefix: `w` and `w'` share the length-`J` prefix. -/
theorem cword_prefix (J K : ℕ) (hJ : 1 ≤ J) (hK : 1 ≤ K) :
    ∀ j < J, cword J K j = cword' J K j := by
  sorry

/-- Section 5(i), fork: the middle two entries differ by
`(-gamma, +gamma)` in the NATURAL order `(w, w')`. Section 6 swaps the
names to obtain FM-F's `(+gamma, -gamma)` orientation; the signs are not
"fixed" here. -/
theorem cword_fork (J K : ℕ) (hJ : 1 ≤ J) (hK : 1 ≤ K) :
    cword J K J + cgamma J K = cword' J K J ∧
      cword J K (J + 1) = cword' J K (J + 1) + cgamma J K := by
  sorry

/-- Section 5(i), suffix: `w` and `w'` share the length-`K` suffix, i.e.
the entries at word positions `J+2, ..., L-1`. -/
theorem cword_suffix (J K : ℕ) (hJ : 1 ≤ J) (hK : 1 ≤ K) :
    ∀ i < K, cword J K (J + 2 + i) = cword' J K (J + 2 + i) := by
  sorry

/-- Section 5(ii): both 0-based point sets are admissible -- for
`p ≤ L+2` the residue class of 0 is unoccupied before translation (all
`q_j > L+3 > p`), and for `p > L+2` there are only `L+1 < p` points --
together with section 5(iv)'s "the words have `L + 1` points". -/
theorem cword_admissible (J K : ℕ) (hJ : 1 ≤ J) (hK : 1 ≤ K) :
    (IsAdmissible (wordPointSet (cword J K) (cL J K)) ∧
        (wordPointSet (cword J K) (cL J K)).card = cL J K + 1) ∧
      (IsAdmissible (wordPointSet (cword' J K) (cL J K)) ∧
        (wordPointSet (cword' J K) (cL J K)).card = cL J K + 1) := by
  sorry

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

/-! ### Smoke tests (concrete tables)

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
```

---

## PART III -- frozen Lean context (not under assessment)

```lean
-- Base definitions (Basic.lean excerpt; index conventions
-- as documented in Part II)

/-- 0-indexed primes: `q 0 = 2`, `q 1 = 3`, ... (paper `p_{n+1}`). -/
def q (n : ℕ) : ℕ := Nat.nth Nat.Prime n

/-- Prime gap, 0-indexed: `gap n` = paper `g_{n+1}`; `gap 0 = 1`. -/
def gap (n : ℕ) : ℕ := q (n + 1) - q n

/-- Tail transform (= paper `delta_n`): weighted average of future gaps. -/
def delta (n : ℕ) : ℝ := ∑' j : ℕ, (gap (n + j) : ℝ) / 2 ^ (j + 1)

/-- Two indices carry the same length-`J` gap word (template 9.1). -/
def SameBlock (n m J : ℕ) : Prop := ∀ i, i < J → gap (n + i) = gap (m + i)

import Erdos251.Basic

/-!
# Hypothesis layer (prose section 1): `HLQuantA` and `CramerGranville`

FROZEN context for Part II; NOT under assessment. Hypothesis A counts
NONCONSECUTIVE admissible tuples; consecutiveness is DERIVED downstream
(Lemma 4.3), never assumed.

Faithfulness notes:
* the prose Hypothesis A displays a constant `C_A >= 1` that its
  inequality never uses; flagged as vestigial, not encoded.
* `singularSeries` is a `tprod`, which mathlib defaults to 1 when not
  `Multipliable`; for admissible `H` the product IS multipliable
  (`singularSeries_multipliable`), so the Lean `HLQuantA` matches the
  paper hypothesis.
-/

namespace Erdos251

noncomputable section

/-- Number of residue classes mod `p` occupied by `H`. -/
def nuMod (H : Finset ℕ) (p : ℕ) : ℕ :=
  (H.image (Nat.cast : ℕ → ZMod p)).card

/-- Admissibility: no prime has all of its residue classes occupied
(prose section 1). -/
def IsAdmissible (H : Finset ℕ) : Prop :=
  ∀ p : ℕ, p.Prime → nuMod H p < p

/-- Singular series `S(H) = ∏_p (1 - ν_H(p)/p) (1 - 1/p)^{-|H|}`. -/
def singularSeries (H : Finset ℕ) : ℝ :=
  ∏' p : Nat.Primes,
    (1 - (nuMod H (p : ℕ) : ℝ) / ((p : ℕ) : ℝ)) /
      (1 - 1 / ((p : ℕ) : ℝ)) ^ H.card

/-- Nonconsecutive tuple count `π_H(x) = #{a ≤ x : a + h prime ∀ h ∈ H}`
(with `0 ∈ H` this in particular forces `a` prime). -/
def tupleCount (H : Finset ℕ) (x : ℕ) : ℕ :=
  ((Finset.range (x + 1)).filter fun a => ∀ h ∈ H, (a + h).Prime).card

/-- Hardy-Littlewood model mass `M_H(x) = S(H) · x / (log x)^{|H|}`. -/
def modelMass (H : Finset ℕ) (x : ℕ) : ℝ :=
  singularSeries H * (x : ℝ) / Real.log x ^ H.card

/-- The singular-series product converges unconditionally for admissible
`H` (head factors positive by admissibility, tail log-factors
`O(|H|²/p²)`). Load-bearing for the faithfulness of `HLQuantA`; see the
module docstring. -/
theorem singularSeries_multipliable {H : Finset ℕ} (hH : IsAdmissible H) :
    Multipliable (fun p : Nat.Primes =>
      (1 - (nuMod H (p : ℕ) : ℝ) / ((p : ℕ) : ℝ)) /
        (1 - 1 / ((p : ℕ) : ℝ)) ^ H.card) := by
  sorry

/-- Positivity of the singular series for admissible `H`
(prose Lemma 4.1 direction; quantitative form `≥ e^{-Ck log k}` is
part of the counting layer). -/
theorem singularSeries_pos {H : Finset ℕ} (hH : IsAdmissible H) :
    0 < singularSeries H := by
  sorry

/-- HYPOTHESIS A (prose section 1): uniform two-sided tuple counts.
Window: `|H| ≤ 4 lnln x`, span `≤ (log x)^3`, even offsets containing 0,
factor 2 on both sides. -/
def HLQuantA : Prop :=
  ∃ x0 : ℕ, ∀ x : ℕ, x0 ≤ x →
    ∀ H : Finset ℕ, 0 ∈ H → (∀ h ∈ H, Even h) → IsAdmissible H →
      (H.card : ℝ) ≤ 4 * Real.log (Real.log x) →
      (∀ h ∈ H, (h : ℝ) ≤ Real.log x ^ 3) →
      modelMass H x / 2 ≤ (tupleCount H x : ℝ) ∧
        (tupleCount H x : ℝ) ≤ 2 * modelMass H x

/-- HYPOTHESIS B (prose section 1): Cramer-Granville pointwise gap
bound, in Lean gap indexing (`gap n` = paper `g_{n+1}`; equivalent as an
eventual statement). -/
def CramerGranville : Prop :=
  ∃ C : ℝ, ∃ n0 : ℕ, ∀ n : ℕ, n0 ≤ n →
    (gap n : ℝ) ≤ C * Real.log (q n) ^ 2

end

end Erdos251
```
