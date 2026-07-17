import Mathlib
import Erdos251.Basic
import Erdos251.Hypotheses

/-!
# Section-4 preamble: gap words, point sets, consecutive counts

The chain-v1 section-4 preamble definitions: `IsConsecRealization`,
`wordPointSet`, `offsetSpan`, `oneExtensions`, `consCount`. Everything
else in the counting layer is stated over these.

RELOCATION ONLY (item-0016). The body below is byte-identical to
`Erdos251/Counting.lean` lines 77-115 at commit
`6683ee0f009baeb5dd6e759f265544e7f91af23d`,
sha256 `b2c98102733ced95085e1af5764f035027ae788f935d7b710e28878416c3dcf9`.
No statement, docstring, proof or name was changed. Provenance, the index
conventions, the traceability table and the module map live in the umbrella
`Erdos251/Counting.lean`.
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

end

end Erdos251
