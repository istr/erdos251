import Erdos251.Basic

/-!
# Hypothesis layer (chain-v1 section 1): `HLQuantA` and `CramerGranville`

DEFINED, not stubbed (chain-v1 8.2). This file replaces the round-0
placeholder `HypUniformTuples : Prop := True` -- item-0002's "no `True`
stubs" requirement.

Design (review-2 lesson, chain-v1 section 1): Hypothesis A counts
NONCONSECUTIVE admissible tuples, whose in-budget model masses are
`x^{1-o(1)} ≫ 1` (chain-v1 Lemma 4.1), so a fixed two-sided factor 2 is
integrality-safe. The gpt-iso template 9.8 (`HLQuantFull`) demands relative
accuracy on exact gap cylinders and is provably false as stated
(triage-1b: same Q1 defect as the gpt-web chain); it is deliberately NOT
ported. Consecutiveness is DERIVED downstream (chain-v1 Lemma 4.3), never
assumed.

Faithfulness notes:
* chain-v1's Hypothesis A displays a constant `C_A ≥ 1` that its
  inequality never uses; flagged as vestigial (ledger ANN-12), not encoded.
* `singularSeries` is a `tprod`, which mathlib defaults to 1 when not
  `Multipliable`; for admissible `H` the product IS multipliable
  (`singularSeries_multipliable`), so the Lean `HLQuantA` matches the
  paper hypothesis.
-/

namespace Erdos251

noncomputable section

/-- Number of residue classes mod `p` occupied by `H`. -/
def nuMod (H : Finset ℕ) (p : ℕ) : ℕ :=
  (H.image fun h => (h : ZMod p)).card

/-- Admissibility: no prime has all of its residue classes occupied
(chain-v1 section 1). -/
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
(chain-v1 Lemma 4.1 direction; quantitative form `≥ e^{-Ck log k}` is
part of the counting layer). -/
theorem singularSeries_pos {H : Finset ℕ} (hH : IsAdmissible H) :
    0 < singularSeries H := by
  sorry

/-- HYPOTHESIS A (chain-v1 section 1): uniform two-sided tuple counts.
Window: `|H| ≤ 4 lnln x`, span `≤ (log x)^3`, even offsets containing 0,
factor 2 on both sides. -/
def HLQuantA : Prop :=
  ∃ x0 : ℕ, ∀ x : ℕ, x0 ≤ x →
    ∀ H : Finset ℕ, 0 ∈ H → (∀ h ∈ H, Even h) → IsAdmissible H →
      (H.card : ℝ) ≤ 4 * Real.log (Real.log x) →
      (∀ h ∈ H, (h : ℝ) ≤ Real.log x ^ 3) →
      modelMass H x / 2 ≤ (tupleCount H x : ℝ) ∧
        (tupleCount H x : ℝ) ≤ 2 * modelMass H x

/-- HYPOTHESIS B (chain-v1 section 1): Cramer-Granville pointwise gap
bound, in Lean gap indexing (`gap n` = paper `g_{n+1}`; equivalent as an
eventual statement). -/
def CramerGranville : Prop :=
  ∃ C : ℝ, ∃ n0 : ℕ, ∀ n : ℕ, n0 ≤ n →
    (gap n : ℝ) ≤ C * Real.log (q n) ^ 2

end

end Erdos251
