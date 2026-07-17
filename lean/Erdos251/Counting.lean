import Erdos251.Counting.Words
import Erdos251.Counting.SingularSeries
import Erdos251.Counting.OneExtension
import Erdos251.Counting.Lemmata
import Erdos251.Counting.ConsecTransfer
import Erdos251.Counting.GapTail
import Erdos251.Counting.Construction

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

/-! ## Module map (item-0016)

This file is a thin umbrella: its body was split into the themed modules
imported above, so every downstream import (`Erdos251/Conditional.lean`,
`Erdos251.lean`) is unchanged and every declaration keeps its name and its
`Erdos251` namespace.

The split is a PURE relocation. Each module's body is byte-identical to a
contiguous line range of this file at commit
`6683ee0f009baeb5dd6e759f265544e7f91af23d`,
and the seven bodies concatenated in the import order above reproduce the
old body exactly (lines 77-2756, sha256
`f14032ebd791dcf096b19f33186af5e4c79a54b58d20607db3e03d4bbd507c86`).
No declaration moved past another, no statement, docstring, proof or name
was touched, and the sorry inventory and axiom gate are unchanged.

| module (`Erdos251/Counting/`) | chain-v1 v1.4 | holds |
|---------------------|--------------------|--------------------------------|
| `Words`             | sec. 4 preamble    | the five definitions above     |
| `SingularSeries`    | Lemma 4.1 layer    | Euler-product split, `primesLe` bridge, `singularSeries_ge_exp`, `modelMass_ge_exp` |
| `OneExtension`      | Lemma 4.2 layer    | insert algebra, collision primes, `singularSeries_ratio_le` |
| `Lemmata`           | Lemmata 4.1, 4.2   | the two statements themselves  |
| `ConsecTransfer`    | Lemma 4.3 layer    | prime-shift transfer, Bonferroni cut, limits, `consCount_lower_bound` |
| `GapTail`           | Lemma 4.4          | `delta_le_of_gap_bound` (imports `Basic` only) |
| `Construction`      | sec. 5             | constants, words, 5(i)-5(iv), `constr_consCount_pos`, smoke tests |

`Lemmata` carries the 4.1 and 4.2 statements together because the item-0014
statement set clustered them under one heading; the order-preserving split
keeps them there. Lemmata 4.3 and 4.4 sit with their own machinery for the
same reason. The relocation is re-checkable at any time with
`python3 lean/scripts/blocks.py relocation-check`.
-/
