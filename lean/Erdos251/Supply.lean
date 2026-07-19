import Erdos251.Exchange

/-!
# Supply layer -- the abstract Lean supply integrator (item-0018 M2)

Formalises `dossier/relext-statements.md` v1.1 Section 7: the three named
Props of Section 7.1 (`MatchedFlankLower`, `RelExtensionUpper`,
`TailIntersection`) and the single M2 obligation

  `supply_of_triple : MatchedFlankLower -> RelExtensionUpper ->
     TailIntersection -> ExchangeSupply1`,

whose proof is exactly the Section 7.2 abundance-minus-rigidity pigeonhole
followed by the Section 7.3 `ExchangeAt` clause table. The three Props are
NAMED STATEMENTS ONLY (the `ExchangeSupply1` / `HLQuantA` pattern): none of
them is proved here; supplying them is the business of items 0019-0021.

## Index dictionary (ANN-50 / dossier T6, fixed for every statement here)

Lean `gap k` = paper `g_{k+1}`; Lean `delta k` = paper `delta_k` (no
shift). The Lean base index equals the paper anchor index; the shift lives
entirely inside `gap`. Concretely, at a site with base index `n`:

* paper word letter `w_i = g_{n+i}` (`1 <= i <= L`) = Lean `gap (n+i-1)`,
  so the window is `gap n, ..., gap (n+L-1)` with `L = J + 1 + K`;
* the middle `g_{n+J+1}` = Lean `gap (n+J)` -- exactly the `differ` slot
  of `ExchangeAt`;
* the far-cap index paper `n+L = n+J+1+K` = Lean `n+J+1+K` (`delta`
  carries no shift) -- exactly the `cap_far` slot of `ExchangeAt`;
* the anchor prime `p_n` = Lean `q (n-1)` (`q` is 0-indexed,
  `q 0 = 2 = p_1`), see `anchorPrime`.

## Parameter layer (kickoff v2 Section 3(d), hazard (v))

The depth/cap parameters `J, K, D` and the aggregate window budget enter
as fields of `SupplyParams`, as functions of the scale `x` (at the D0 pin
they are `D = ceil(13 C_0 A'' ln x)`, `J = K = ceil(log2 D)`, window
budget `A' L ln x` with `A' = 1.5`, `A'' = 48; the growth laws are NOT
encoded -- the integrator is uniform in them). The `b = 1` gate source is
P3.3'(i)-shaped: `D <= 2^J` is a definitional property of the parameter
layer (field `D_le_two_pow_J`), and the gate `(D : R) - 2 < 2^(J+1)` of
`ExchangeSupply1` is derived from it in the proof of `supply_of_triple`.
The three Props and the theorem are stated relative to a `SupplyParams`;
instantiating the fields at the D0 pin recovers the 7.1 displays verbatim.

## The filtered site set (D0.2', filters-first)

`filteredSites P s x` is the paper `S'^{(s)}_x` as a `Finset` over
`Finset.range (x+1)` (`consCount` pattern; the truncation loses nothing
since `n + 2 <= q n`, see `add_two_le_q`): sites `n >= 1` with anchor
prime `p_n <= x`, threshold `n >= s+1` (paper; the Section 7.3 dictionary
is the SINGLE threshold identification `s := t`), the aggregate window-sum
cap, and BOTH (E4) delta caps written byte-parallel to `ExchangeAt`'s
`cap_near` / `cap_far` fields (hazard (ii)), so that the 7.3 clause table
discharges by unfolding. The cap clauses are real inequalities (as in
`ExchangeAt`); the `Finset` filters take classical decidability
(`open scoped Classical`, `consCount` precedent), consistent with the
classical-three axiom budget.

## Classes, counts, families (RS.1)

`sideMatchAt` encodes the RS.1 matched-flank clauses via `gap`;
`classSites` is the class `F_P(S'^{(s)}_x)`, `classCount` is `N_P`,
`classCountMid` is `N_{P,d}`; `realizedFamily` (`Fam`) is the image of
the site set under `sideWordAt` (finiteness free), `multiFamily`
(`Fam_2`) its `N_P >= 2` part. `Nat` subtraction supplies the truncated
`(N - 1)_+` for free (hazard (iv): the delta/eps arithmetic of the
pigeonhole stays in `Q`, with casts at the comparison inequalities only;
real arithmetic appears only where D0.2' itself lives -- the cap and
window-budget clauses, as in `ExchangeAt` -- and in the single real cast
of the proof, the `ExchangeSupply1` gate).

## Statement-fidelity law (U18.5)

The 7.1 quantifier order is carried verbatim into each Prop; the
bracketed 7.1 audit notes travel as docstrings, never as hypotheses (in
particular `TailIntersection` carries NO `|S'| >= 1` clause -- hazard
(vi): positivity is delivered through `4 |S'| >= N` with `N >= 1` at
`x >= 2`).
-/

namespace Erdos251

noncomputable section

open scoped Classical

/-- The anchor prime of a site: paper `p_n` = Lean `q (n - 1)` (ANN-50 /
T6 dictionary: the Lean base index equals the paper anchor index and `q`
is 0-indexed). `Nat` subtraction totalises the definition at `n = 0`;
every use pairs it with the site clause `1 <= n`. -/
def anchorPrime (n : ℕ) : ℕ := q (n - 1)

/-- `n + 2 <= q n`: the 0-indexed primes grow at least linearly. This is
what makes the `Finset.range (x+1)` carrier of `sitePop` and
`filteredSites` lossless: `anchorPrime n <= x` with `1 <= n` forces
`n < x + 1`. -/
theorem add_two_le_q (n : ℕ) : n + 2 ≤ q n := by
  induction n with
  | zero =>
    have h : q 0 = 2 := by simp [q, Nat.nth_prime_zero_eq_two]
    omega
  | succ n ih =>
    have h := q_lt_succ n
    omega

/-- The site population `N` of D0: `pi(x)`, counted as the sites
`n >= 1` with anchor prime `p_n <= x`, over the lossless carrier
`Finset.range (x+1)` (`consCount` pattern; see `add_two_le_q`). -/
def sitePop (x : ℕ) : ℕ :=
  (Finset.filter (fun n : ℕ => 1 ≤ n ∧ anchorPrime n ≤ x)
    (Finset.range (x + 1))).card

/-- The population is positive from `x = 2` on (the site `n = 1` has
anchor prime `p_1 = 2`). This is where `TailIntersection` gets its bite
(hazard (vi)): `4 |S'| >= N >= 1`, so no `|S'| >= 1` clause is carried. -/
theorem one_le_sitePop {x : ℕ} (hx : 2 ≤ x) : 1 ≤ sitePop x := by
  have h2 : anchorPrime 1 = 2 := by simp [anchorPrime, q, Nat.nth_prime_zero_eq_two]
  have h1 : (1 : ℕ) ∈ Finset.filter (fun n : ℕ => 1 ≤ n ∧ anchorPrime n ≤ x)
      (Finset.range (x + 1)) :=
    Finset.mem_filter.mpr ⟨Finset.mem_range.mpr (by omega), le_refl 1, by omega⟩
  have hpos := Finset.card_pos.mpr ⟨1, h1⟩
  unfold sitePop
  omega

/-- Parameter layer (kickoff v2 Section 3(d)). The depth/cap parameters
`J, K, D` and the aggregate window budget `wbound` of the D0.2' filter,
as functions of the scale `x`; at the D0 pin `D = ceil(13 C_0 A'' ln x)`,
`J = K = ceil(log2 D)`, `wbound = A' L ln x` (`A' = 1.5`, `A'' = 48`,
`L = J + 1 + K`). The growth laws are not encoded; the integrator
consumes exactly three definitional properties:

* `one_le_J`, `one_le_K` -- `J, K >= 1` by construction (D0), feeding
  the fields of the same name in `ExchangeAt` (Section 7.3);
* `D_le_two_pow_J` -- P3.3'(i) `2^J >= D`, the `b = 1` gate source
  (hazard (v)): it yields `(D : R) - 2 < 2^(J+1)` in `supply_of_triple`. -/
structure SupplyParams where
  /-- Prefix depth `J` at scale `x` (D0: `ceil(log2 D)`). -/
  J : ℕ → ℕ
  /-- Suffix depth `K` at scale `x` (D0: `ceil(log2 D)`). -/
  K : ℕ → ℕ
  /-- Near-cap bound `D` at scale `x` (D0: `ceil(13 C_0 A'' ln x)`). -/
  D : ℕ → ℕ
  /-- Aggregate window budget at scale `x` (D0.2': `A' L ln x`). -/
  wbound : ℕ → ℝ
  /-- `J >= 1` by construction (D0); the `one_le_J` clause of 7.3. -/
  one_le_J : ∀ x, 1 ≤ J x
  /-- `K >= 1` by construction (D0); the `one_le_K` clause of 7.3. -/
  one_le_K : ∀ x, 1 ≤ K x
  /-- P3.3'(i): `2^J >= D` -- the `b = 1` gate source (hazard (v)). -/
  D_le_two_pow_J : ∀ x, D x ≤ 2 ^ J x

/-- Membership clauses of the D0.2' filtered site set `S'^{(s)}_x`
(filters-first; kickoff v2 Section 3(a)): site vocabulary `1 <= n` with
anchor prime `p_n <= x`; paper threshold `n >= s+1` (the 7.3 dictionary
sets `s := t`); the aggregate window-sum cap over the `L = J+1+K` window
gaps (paper `sum_{i=1..L} g_{n+i} <= A' L ln x`, the budget `W`); and the
two (E4) delta caps, written byte-parallel to `ExchangeAt`'s `cap_near` /
`cap_far` fields (hazard (ii)): `delta (n + J) <= D` and
`delta (n + J + 1 + K) <= 2 ^ K` (far index per ANN-50, hazard (iii)). -/
def memSiteFilter (J K D : ℕ) (W : ℝ) (s x n : ℕ) : Prop :=
  (1 ≤ n ∧ anchorPrime n ≤ x) ∧ s + 1 ≤ n ∧
    (∑ i ∈ Finset.range (J + 1 + K), (gap (n + i) : ℝ)) ≤ W ∧
    delta (n + J) ≤ D ∧
    delta (n + J + 1 + K) ≤ 2 ^ K

/-- The filtered site set `S'^{(s)}_x` of D0.2' as a `Finset`
(`consCount` pattern; the `Finset.range (x+1)` carrier is lossless by
`add_two_le_q`). All counts of this module default to this set (RS.1
`T = S'^{(s)}_x`, filters-first: the caps live INSIDE every count). -/
def filteredSites (P : SupplyParams) (s x : ℕ) : Finset ℕ :=
  Finset.filter (memSiteFilter (P.J x) (P.K x) (P.D x) (P.wbound x) s x)
    (Finset.range (x + 1))

/-- The site clauses, unpacked (D0.2' membership at the parameter fields
of `P`). The two delta caps are literally `ExchangeAt`'s `cap_near` /
`cap_far` shapes at `J = P.J x`, `K = P.K x`, `D = P.D x`. -/
theorem site_clauses {P : SupplyParams} {s x n : ℕ}
    (h : n ∈ filteredSites P s x) :
    (1 ≤ n ∧ anchorPrime n ≤ x) ∧ s + 1 ≤ n ∧
      (∑ i ∈ Finset.range (P.J x + 1 + P.K x), (gap (n + i) : ℝ)) ≤ P.wbound x ∧
      delta (n + P.J x) ≤ P.D x ∧
      delta (n + P.J x + 1 + P.K x) ≤ 2 ^ P.K x := by
  unfold filteredSites at h
  have h2 := (Finset.mem_filter.mp h).2
  unfold memSiteFilter at h2
  exact h2

/-- A side pair `P = (a, c)` of RS.1: the prefix word `a` (length `J`)
and the suffix word `c` (length `K`), as lists of gap values. -/
abbrev SidePair : Type := List ℕ × List ℕ

/-- The RS.1 matched-flank clauses via `gap` (7.6 vocabulary): `n`
realizes the side pair `(a, c)` when its next `a.length` gaps spell `a`
and the `c.length` gaps beyond the middle slot spell `c`. In paper terms
(ANN-50): `g_{n+i} = a_i` for `1 <= i <= J` and `g_{n+J+1+i} = c_i` for
`1 <= i <= K`; the slot `gap (n + a.length)` between the two flanks is
the middle `g_{n+J+1}`. -/
def sideMatchAt (a c : List ℕ) (n : ℕ) : Prop :=
  (∀ i, i < a.length → gap (n + i) = a.getD i 0) ∧
    (∀ i, i < c.length → gap (n + a.length + 1 + i) = c.getD i 0)

/-- The side pair realized at base index `n` with depths `(J, K)`: the
word map `n |-> P(n)` of RS.1, used to extract the realized family as an
image (kickoff v2 Section 3(a): finiteness free). -/
def sideWordAt (J K n : ℕ) : SidePair :=
  (List.ofFn (fun i : Fin J => gap (n + (i : ℕ))),
    List.ofFn (fun i : Fin K => gap (n + J + 1 + (i : ℕ))))

/-- `List.ofFn` against a pointwise `getD` description (helper for the
word-map / clause-match dictionary). -/
theorem ofFn_eq_iff {l : List ℕ} {f : ℕ → ℕ} :
    List.ofFn (fun i : Fin l.length => f (i : ℕ)) = l ↔
      ∀ i, i < l.length → f i = l.getD i 0 := by
  constructor
  · intro h i hi
    conv_rhs => rw [← h]
    rw [List.getD_eq_getElem _ _ (by simpa using hi), List.getElem_ofFn]
  · intro h
    refine List.ext_getElem (by simp) fun i h₁ h₂ => ?_
    rw [List.getElem_ofFn]
    have hf := h i h₂
    rwa [List.getD_eq_getElem _ _ h₂] at hf

/-- A side pair of the right shape is the word of `n` iff `n` matches its
clauses: the RS.1 class `F_P` is exactly the `sideWordAt` fiber of `P`. -/
theorem sideWordAt_eq_iff {J K n : ℕ} {w : SidePair}
    (h1 : w.1.length = J) (h2 : w.2.length = K) :
    sideWordAt J K n = w ↔ sideMatchAt w.1 w.2 n := by
  subst h1
  subst h2
  constructor
  · intro h
    have ha : List.ofFn (fun i : Fin w.1.length => gap (n + (i : ℕ))) = w.1 :=
      congrArg Prod.fst h
    have hc : List.ofFn
        (fun i : Fin w.2.length => gap (n + w.1.length + 1 + (i : ℕ))) = w.2 :=
      congrArg Prod.snd h
    exact ⟨ofFn_eq_iff.mp ha, ofFn_eq_iff.mp hc⟩
  · intro h
    exact Prod.ext_iff.mpr ⟨ofFn_eq_iff.mpr h.1, ofFn_eq_iff.mpr h.2⟩

/-- Every site matches its own word (reflexivity of the dictionary). -/
theorem sideMatchAt_sideWordAt (J K n : ℕ) :
    sideMatchAt (sideWordAt J K n).1 (sideWordAt J K n).2 n :=
  (sideWordAt_eq_iff (List.length_ofFn _) (List.length_ofFn _)).mp rfl

/-- The matched-flank class `F_P(S'^{(s)}_x)` of RS.1 as a `Finset`:
the filtered sites realizing the side pair `(a, c)`. -/
def classSites (P : SupplyParams) (a c : List ℕ) (s x : ℕ) : Finset ℕ :=
  Finset.filter (fun n => sideMatchAt a c n) (filteredSites P s x)

/-- Class membership, unpacked. -/
theorem mem_classSites {P : SupplyParams} {a c : List ℕ} {s x n : ℕ} :
    n ∈ classSites P a c s x ↔
      n ∈ filteredSites P s x ∧ sideMatchAt a c n := by
  unfold classSites
  exact Finset.mem_filter

/-- `N_P(S'^{(s)}_x)` of RS.1 (7.6 vocabulary `classCount`): the class
cardinality. -/
def classCount (P : SupplyParams) (a c : List ℕ) (s x : ℕ) : ℕ :=
  (classSites P a c s x).card

/-- `N_{P,d}(S'^{(s)}_x)` of RS.1 (7.6 vocabulary `classCountMid`): the
members of the class with middle `g_{n+J+1} = d`, the middle slot being
`gap (n + a.length)` per ANN-50. -/
def classCountMid (P : SupplyParams) (a c : List ℕ) (d : ℕ) (s x : ℕ) : ℕ :=
  (Finset.filter (fun n => gap (n + a.length) = d) (classSites P a c s x)).card

/-- The realized family `Fam(S'^{(s)}_x) = {P : N_P >= 1}` of RS.1, as
the image of the site set under the word map (kickoff v2 Section 3(a):
finiteness free). -/
def realizedFamily (P : SupplyParams) (s x : ℕ) : Finset SidePair :=
  (filteredSites P s x).image (fun n => sideWordAt (P.J x) (P.K x) n)

/-- Realized-family membership, unpacked. -/
theorem mem_realizedFamily {P : SupplyParams} {s x : ℕ} {w : SidePair} :
    w ∈ realizedFamily P s x ↔
      ∃ n ∈ filteredSites P s x, sideWordAt (P.J x) (P.K x) n = w := by
  unfold realizedFamily
  exact Finset.mem_image

/-- The multi-member family `Fam_2(S'^{(s)}_x) = {P : N_P >= 2}` of
RS.1. -/
def multiFamily (P : SupplyParams) (s x : ℕ) : Finset SidePair :=
  (realizedFamily P s x).filter (fun w => 2 ≤ classCount P w.1 w.2 s x)

/-- Realized side pairs have the parameter-layer flank depths. -/
theorem length_of_mem_realizedFamily {P : SupplyParams} {s x : ℕ}
    {w : SidePair} (hw : w ∈ realizedFamily P s x) :
    w.1.length = P.J x ∧ w.2.length = P.K x := by
  obtain ⟨n, -, rfl⟩ := mem_realizedFamily.mp hw
  unfold sideWordAt
  simp

/-- A realized class is nonempty (its image witness matches its own
word). -/
theorem classSites_nonempty {P : SupplyParams} {s x : ℕ} {w : SidePair}
    (hw : w ∈ realizedFamily P s x) :
    (classSites P w.1 w.2 s x).Nonempty := by
  obtain ⟨n, hn, rfl⟩ := mem_realizedFamily.mp hw
  exact ⟨n, mem_classSites.mpr ⟨hn, sideMatchAt_sideWordAt _ _ _⟩⟩

/-- RS.1 partition identity: `sum over P of N_P(T) = |T|` -- the side
pair partitions the site set (each site lies in exactly one class, the
fiber of its own word). Consumed by the 7.2 pigeonhole. -/
theorem card_filteredSites_eq_sum (P : SupplyParams) (s x : ℕ) :
    (filteredSites P s x).card
      = ∑ w ∈ realizedFamily P s x, classCount P w.1 w.2 s x := by
  classical
  have H : ∀ n ∈ filteredSites P s x,
      sideWordAt (P.J x) (P.K x) n ∈ realizedFamily P s x := fun n hn =>
    mem_realizedFamily.mpr ⟨n, hn, rfl⟩
  rw [Finset.card_eq_sum_card_fiberwise H]
  refine Finset.sum_congr rfl fun w hw => ?_
  obtain ⟨h1, h2⟩ := length_of_mem_realizedFamily hw
  unfold classCount classSites
  congr 1
  refine Finset.filter_congr fun n _ => ?_
  exact sideWordAt_eq_iff h1 h2

/-- A window gap is bounded by the window budget: the middle slot
`gap (n + J)` is one of the `L = J+1+K` window gaps, and the gaps are
nonnegative, so the aggregate cap bounds it. Feeds the window clause of
the selection restriction in the 7.2 pigeonhole. -/
theorem middle_le_wbound {P : SupplyParams} {s x n : ℕ}
    (h : n ∈ filteredSites P s x) :
    (gap (n + P.J x) : ℝ) ≤ P.wbound x := by
  obtain ⟨-, -, hwin, -, -⟩ := site_clauses h
  refine le_trans ?_ hwin
  exact Finset.single_le_sum (f := fun i => (gap (n + i) : ℝ))
    (fun i _ => by positivity) (Finset.mem_range.mpr (by omega))

/-- The middle-rigid canonical selection of the 7.2 pigeonhole: each side
pair selects the middle gap of the least member of its class (`0` when
the class is empty; on the realized family the class is nonempty,
`classSites_nonempty`). Under the rigidity assumption this realizes
`N_{P,d_P} = N_P` on every realized class; for singletons it selects the
unique middle. Proof-side device only -- the `RelExtensionUpper`
quantifier ranges over ALL restricted selections (hazard (i)). -/
def rigidSelect (P : SupplyParams) (s x : ℕ) : SidePair → ℕ := fun w =>
  if h : (classSites P w.1 w.2 s x).Nonempty then
    gap ((classSites P w.1 w.2 s x).min' h + w.1.length)
  else 0

/-- Evaluation of `rigidSelect` on a nonempty class. -/
theorem rigidSelect_eq {P : SupplyParams} {s x : ℕ} {w : SidePair}
    (h : (classSites P w.1 w.2 s x).Nonempty) :
    rigidSelect P s x w
      = gap ((classSites P w.1 w.2 s x).min' h + w.1.length) := by
  unfold rigidSelect
  exact dif_pos h

/-! ## The three named Props (7.1 v1.1; named statements ONLY)

Each docstring carries the 7.1 display and its bracketed audit note
verbatim (the notes travel as documentation, never as hypotheses). -/

/-- `MatchedFlankLower` (= candidate A3), 7.1 v1.1 display:

  exists delta > 0, forall s, exists x_2(s), forall x >= x_2(s):
    sum over P in Fam_2(S'^{(s)}_x) of N_P >= delta |S'^{(s)}_x|.

7.1 audit note: "the draft's extra clause `|S'| >= 1` is dropped --
positivity is TailIntersection's job, restoring the none-redundant claim.
The s-uniform delta is stronger than the threading needs (A3 necessity
note); adopted for the single 7.4 gate constant."

Encoding: `delta` is rational (7.6: avoids real-cast noise in the
pigeonhole); the counts are `Nat` sums, cast at the comparison only. -/
def MatchedFlankLower (P : SupplyParams) : Prop :=
  ∃ δ : ℚ, 0 < δ ∧ ∀ s : ℕ, ∃ x2 : ℕ, ∀ x : ℕ, x2 ≤ x →
    ((∑ w ∈ multiFamily P s x, classCount P w.1 w.2 s x : ℕ) : ℚ)
      ≥ δ * ((filteredSites P s x).card : ℚ)

/-- `RelExtensionUpper` (= candidate B2.reduced), 7.1 v1.1 display:

  forall eps > 0, exists x_4(eps), forall x >= x_4, forall s,
  forall selections (d_P):
    sum over P of (N_{P,d_P} - 1)_+ <= eps * sum over P of N_P.

7.1 audit note: "the o(ln x)/ln x gate is stated as the clean
relative-eps form; C_F(x) = eps ln x recovers the kickoff display."

Encoding (kickoff v2 Section 3(b), hazard (i)): the selection quantifier
ranges over ALL total functions `SidePair -> Nat` (adversarial; no
dependent choice over the family Finset), restricted on the realized
family by the even/window clauses -- middles are even, `>= 2` (RS.1
vocabulary) and within the aggregate window budget. `Nat` subtraction
supplies `(N-1)_+`; `eps` is rational, cast at the inequality only. -/
def RelExtensionUpper (P : SupplyParams) : Prop :=
  ∀ ε : ℚ, 0 < ε → ∃ x4 : ℕ, ∀ x : ℕ, x4 ≤ x → ∀ s : ℕ,
    ∀ d : SidePair → ℕ,
      (∀ w ∈ realizedFamily P s x,
        Even (d w) ∧ 2 ≤ d w ∧ ((d w : ℝ) ≤ P.wbound x)) →
      ((∑ w ∈ realizedFamily P s x,
          (classCountMid P w.1 w.2 (d w) s x - 1) : ℕ) : ℚ)
        ≤ ε * ((∑ w ∈ realizedFamily P s x, classCount P w.1 w.2 s x : ℕ) : ℚ)

/-- `TailIntersection` (= candidate C2 base form at the D0 pin), 7.1 v1.1
display:

  forall s, exists x_7(s), forall x >= x_7: |S'^{(s)}_x| >= N/4,

stated division-free as `4 |S'^{(s)}_x| >= N` (7.6 shape) with `N` the
site population `sitePop x = pi(x)`.

7.1 audit note: "1/4 is DELIVERED by C2 only under the D0 pin `A' = 1.5`,
`A'' = 48` (retention floor `7/24 - o(1) > 1/4` with margin); the
dossier's example `A'' = 12` gives only 1/6, and no `A''` suffices at
`A' <= 4/3` -- the pin is therefore part of the Prop's provenance. The
pigeonhole itself consumes only `|S'^{(s)}_x| >= 1`."

Hazard (vi): NO `|S'| >= 1` clause is carried (the M1 audit dropped it
deliberately); positivity is what this Prop itself supplies at `N >= 1`
via `4 |S'| >= N`, and `N >= 1` holds for `x >= 2`
(`one_le_sitePop`). -/
def TailIntersection (P : SupplyParams) : Prop :=
  ∀ s : ℕ, ∃ x7 : ℕ, ∀ x : ℕ, x7 ≤ x →
    4 * (filteredSites P s x).card ≥ sitePop x

/-- item-0018 M2, the single obligation (7.2 + 7.3): the three named
Props integrate to the exchange supply `ExchangeSupply1`.

Proof skeleton, per the kickoff v2 Section 3(c):

* 7.3 scale selection: fix the Lean threshold `t`, set paper `s := t`
  (the SINGLE threshold dictionary, MINOR-3), and take one
  `x = x2 + x4 + x7 + 2` beyond the three Prop thresholds at
  `eps = delta/4` (the 7.4 coupling) with `x >= 2` for `N >= 1`.
* 7.2 pigeonhole: SUPPOSE every realized class is middle-rigid. The
  canonical selection `rigidSelect` (least member's middle; the unique
  middle on singletons) is admissible for `RelExtensionUpper` and
  realizes `N_{P,d_P} = N_P`, so
  `sum (N_P - 1) >= (1/2) sum_{Fam_2} N_P >= (delta/2) |S'|` against the
  upper bound `(delta/4) sum N_P = (delta/4) |S'|` (RS.1 partition
  identity) -- incompatible at `|S'| >= 1` (TailIntersection plus
  `N >= 1`). Hence some class carries `n != m` with equal flanks and
  differing middles.
* 7.3 clause table: the pair yields `ExchangeAt n m J K D` field by
  field (flank matches -> `SameBlock`; the differing middle -> `differ`;
  the site filter's delta caps -> `cap_near`/`cap_far`, byte-parallel by
  construction; threshold `n, m >= s+1 >= t`), and the `b = 1` gate
  `(D : R) - 2 < 2^(J+1)` from the parameter layer's `2^J >= D`
  (P3.3'(i), hazard (v)). One witness per threshold discharges the
  `forall t` of `ExchangeSupply1` (M = 1 normal form throughout). -/
theorem supply_of_triple (P : SupplyParams)
    (hMFL : MatchedFlankLower P) (hREU : RelExtensionUpper P)
    (hTI : TailIntersection P) : ExchangeSupply1 := by
  intro t
  obtain ⟨δ, hδpos, hMFL'⟩ := hMFL
  obtain ⟨x2, hx2⟩ := hMFL' t
  obtain ⟨x4, hx4⟩ := hREU (δ / 4) (by positivity)
  obtain ⟨x7, hx7⟩ := hTI t
  -- 7.3 scale selection: one x beyond all three thresholds, and >= 2
  set x : ℕ := x2 + x4 + x7 + 2 with hxdef
  have hA := hx2 x (by omega)
  have hC := hx7 x (by omega)
  have hpop : 1 ≤ sitePop x := one_le_sitePop (by omega)
  have hScard : 1 ≤ (filteredSites P t x).card := by omega
  -- 7.2: abundance minus rigidity forces a same-class pair with
  -- distinct middles
  have hpair : ∃ w ∈ realizedFamily P t x, ∃ n ∈ classSites P w.1 w.2 t x,
      ∃ m ∈ classSites P w.1 w.2 t x,
        gap (n + w.1.length) ≠ gap (m + w.1.length) := by
    by_contra hcon
    push_neg at hcon
    -- the rigid selection is admissible for RelExtensionUpper
    have hrestr : ∀ w ∈ realizedFamily P t x,
        Even (rigidSelect P t x w) ∧ 2 ≤ rigidSelect P t x w ∧
          ((rigidSelect P t x w : ℝ) ≤ P.wbound x) := by
      intro w hw
      have hne := classSites_nonempty hw
      have hd := rigidSelect_eq hne
      have hmem := Finset.min'_mem _ hne
      have hS : (classSites P w.1 w.2 t x).min' hne ∈ filteredSites P t x :=
        (mem_classSites.mp hmem).1
      obtain ⟨⟨h1, -⟩, -, -, -, -⟩ := site_clauses hS
      have hev : Even (gap ((classSites P w.1 w.2 t x).min' hne + w.1.length)) :=
        gap_even (by omega)
      refine ⟨?_, ?_, ?_⟩
      · rw [hd]; exact hev
      · rw [hd]
        have hgp := gap_pos ((classSites P w.1 w.2 t x).min' hne + w.1.length)
        rcases hev with ⟨k, hk⟩
        omega
      · rw [hd, (length_of_mem_realizedFamily hw).1]
        exact middle_le_wbound hS
    -- RelExtensionUpper at eps = delta/4 (7.4 coupling)
    have hB := hx4 x (by omega) t (rigidSelect P t x) hrestr
    -- middle-rigidity: N_{P,d_P} = N_P on every realized class
    have hrigid : ∀ w ∈ realizedFamily P t x,
        classCountMid P w.1 w.2 (rigidSelect P t x w) t x
          = classCount P w.1 w.2 t x := by
      intro w hw
      have hne := classSites_nonempty hw
      unfold classCountMid classCount
      congr 1
      refine Finset.filter_eq_self.mpr fun n hn => ?_
      rw [rigidSelect_eq hne]
      exact hcon w hw n hn _ (Finset.min'_mem _ hne)
    -- the 7.2 sum chain, Nat side
    have hsum1 : (∑ w ∈ realizedFamily P t x,
          (classCountMid P w.1 w.2 (rigidSelect P t x w) t x - 1))
        = ∑ w ∈ realizedFamily P t x, (classCount P w.1 w.2 t x - 1) :=
      Finset.sum_congr rfl fun w hw => by rw [hrigid w hw]
    have hsum2 : (∑ w ∈ multiFamily P t x, (classCount P w.1 w.2 t x - 1))
        ≤ ∑ w ∈ realizedFamily P t x, (classCount P w.1 w.2 t x - 1) :=
      Finset.sum_le_sum_of_subset (Finset.filter_subset _ _)
    have hsum3 : (∑ w ∈ multiFamily P t x, classCount P w.1 w.2 t x)
        ≤ 2 * ∑ w ∈ multiFamily P t x, (classCount P w.1 w.2 t x - 1) := by
      rw [Finset.mul_sum]
      refine Finset.sum_le_sum fun w hw => ?_
      have h2 : 2 ≤ classCount P w.1 w.2 t x :=
        (Finset.mem_filter.mp hw).2
      omega
    have hpart := card_filteredSites_eq_sum P t x
    -- assemble in Q (hazard (iv): casts at the comparisons only)
    rw [hsum1, ← hpart] at hB
    have hq2 : ((∑ w ∈ multiFamily P t x, (classCount P w.1 w.2 t x - 1) : ℕ) : ℚ)
        ≤ ((∑ w ∈ realizedFamily P t x, (classCount P w.1 w.2 t x - 1) : ℕ) : ℚ) := by
      exact_mod_cast hsum2
    have hq3 : ((∑ w ∈ multiFamily P t x, classCount P w.1 w.2 t x : ℕ) : ℚ)
        ≤ 2 * ((∑ w ∈ multiFamily P t x, (classCount P w.1 w.2 t x - 1) : ℕ) : ℚ) := by
      exact_mod_cast hsum3
    have hcard1 : (1 : ℚ) ≤ ((filteredSites P t x).card : ℚ) := by
      exact_mod_cast hScard
    have hhalf : δ / 2 * 1 ≤ δ / 2 * ((filteredSites P t x).card : ℚ) :=
      mul_le_mul_of_nonneg_left hcard1 (by positivity)
    linarith [hA, hB, hq2, hq3, hhalf, hδpos]
  -- 7.3: the clause table, field by field
  obtain ⟨w, hw, n, hn, m, hm, hnm⟩ := hpair
  obtain ⟨hlen1, hlen2⟩ := length_of_mem_realizedFamily hw
  have hnS : n ∈ filteredSites P t x := (mem_classSites.mp hn).1
  have hmS : m ∈ filteredSites P t x := (mem_classSites.mp hm).1
  have hmatn : sideMatchAt w.1 w.2 n := (mem_classSites.mp hn).2
  have hmatm : sideMatchAt w.1 w.2 m := (mem_classSites.mp hm).2
  obtain ⟨-, hthrn, -, hnearn, hfarn⟩ := site_clauses hnS
  obtain ⟨-, hthrm, -, hnearm, hfarm⟩ := site_clauses hmS
  refine ⟨n, m, P.J x, P.K x, P.D x, by omega, by omega, ?_, ?_⟩
  · exact
      { one_le_J := P.one_le_J x
        one_le_K := P.one_le_K x
        block_prefix := fun i hi =>
          (hmatn.1 i (by rw [hlen1]; exact hi)).trans
            (hmatm.1 i (by rw [hlen1]; exact hi)).symm
        differ := by rw [← hlen1]; exact hnm
        block_suffix := fun i hi => by
          have h1 := hmatn.2 i (by rw [hlen2]; exact hi)
          have h2 := hmatm.2 i (by rw [hlen2]; exact hi)
          rw [hlen1] at h1 h2
          exact h1.trans h2.symm
        cap_near_n := hnearn
        cap_near_m := hnearm
        cap_far_n := hfarn
        cap_far_m := hfarm }
  · -- the b = 1 gate from the parameter layer's 2^J >= D (P3.3'(i))
    have hg : (P.D x : ℝ) ≤ 2 ^ P.J x := by
      exact_mod_cast P.D_le_two_pow_J x
    have hp : (0 : ℝ) < 2 ^ P.J x := by positivity
    rw [pow_succ]
    linarith

end

end Erdos251
