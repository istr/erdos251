import Erdos251.Basic
import Erdos251.ForkMerge

/-!
# Exchange layer -- EXCH_1 and the dyadic sub-target `S ∉ ℤ[1/2]`

FINDING layer, item-0010. This module is deliberately **NOT** part of the
chain-v1 section numbering (chain-v1 is the conditional-irrationality
route through Hypotheses A/B). It formalises the Tao--Teravainen transfer
verdict's exchange lemma, `dossier/tate-transfer.md` Section 1 **O4**
(clauses (E1)--(E5), normal form EXCH), and its consequence
`EXCH_1 ⟹ item-0010` recorded there and in ledger **ANN-49**. The verdict
is a research finding (unconditional-transfer assessment for the TaTe
method), not a proved chain link; this module machine-checks the one
*reduction* the finding isolates.

## What is proved here (milestone 1)

* `ExchangeAt n m J K D` -- the EXCH normal form of O4 as a clause bundle:
  two indices `n, m` sharing a length-`J` gap prefix, differing in exactly
  ONE gap (the Hamming-distance-1 case of (E2')), then sharing a length-`K`
  gap suffix, with near/far `delta` caps (E4). See the structure docstring
  for the clause-by-clause map to the paper's (E1)--(E4).
* `ExchangeSupply1 : Prop` -- the statement-layer supply (pattern of
  `HLQuantA`): for every threshold `t` an exchange configuration with
  base points `≥ t` and the `b = 1` gate (E5). This is item-0017's
  consumption target; it is a NAMED Prop, never proved here (non-goal).
* `exchange_contradiction` / `exchange_contradiction_1` -- one exchange
  configuration beyond depth `s` contradicts `S = a / 2^s`.
* `dyadic_of_exchange_supply : ExchangeSupply1 → ¬ IsDyadic S`, i.e.
  `S ∉ ℤ[1/2]`.

## Relation to `fork_merge_contradiction` (declared deviation)

Steering's independent check (item-0005 adjudication preamble / P8 register)
recorded a *structural correspondence* between O4's EXCH and
`ForkMerge.fork_merge_contradiction`. That correspondence is at the level
of the **proof skeleton and the shared toolkit** -- the `2^(J+1)`
divisibility lock (`repeated_block_quantization`), the block identity
(`delta_block`), the unconditional floor `2 ≤ delta` (`two_le_delta`), and
the `|Δ_end| ≤ 2^K - 2 < 2^K` end-tail bound. It is NOT an instance
relation: `ForkMergeAt` is the FABLE two-step `(+γ, -γ)` fork -- two
differing gaps that re-merge, with the base-`delta` magnitude bound supplied
by fork closeness -- whereas EXCH is Hamming-distance-1 -- one differing
gap, that same magnitude bound supplied instead by the caps (E4). Both then
feed the identical gate + `2^(J+1)`-lattice lock that pins the base
difference to `0`; the configurations, and the end-games after the pin (a
collapsed block-code `γ·2^K` vs a single differing gap), differ in kind, and
no bridge `ExchangeAt → ForkMergeAt` exists (it would force `γ = 0` against
`2 ≤ γ`). `exchange_contradiction` is therefore the Hamming-distance-1
**sibling** of `fork_merge_contradiction`, proved directly from the same
`Basic.lean` lemmas rather than by calling it. This matches the verdict's
own certificates, which are Hamming-distance-1 sites
(`dossier/tate-transfer.md` Section 4: `(5,5,34)` middle 2 vs 8,
`(6,6,64)` middle 8 vs 38).

Index conventions are `Basic.lean`'s: Lean `gap k` = paper `g_{k+1}`, Lean
`delta k` = paper `delta_k` (no shift). Under these, Lean `gap (n+J)` is the
paper differing gap `g_{n+J+1}` of (E2), and the far cap index
`n + J + 1 + K` is the paper `n+J+K+1` of (E4).
-/

namespace Erdos251

noncomputable section

/-- Membership in `ℤ[1/2]` (the dyadic rationals): `x = a / 2^s` for some
integer `a` and exponent `s`. `item-0010`'s target is `¬ IsDyadic S`. -/
def IsDyadic (x : ℝ) : Prop := ∃ (a : ℤ) (s : ℕ), (a : ℝ) / 2 ^ s = x

/-- EXCH, the O4 normal form as a clause bundle (Hamming-distance-1 case of
the general (E2')). Paper `↔` Lean, using `gap k = g_{k+1}`, `delta k =
delta_k`:

* `one_le_J`, `one_le_K` -- positive prefix/suffix depths.
* `block_prefix : SameBlock n m J` -- **(E1)** the length-`J` gap prefix
  agrees: paper `g_{n+i} = g_{m+i}`, `1 ≤ i ≤ J`.
* `differ : gap (n+J) ≠ gap (m+J)` -- **(E2)** the single differing gap,
  paper `g_{n+J+1} ≠ g_{m+J+1}`.
* `block_suffix : SameBlock (n+J+1) (m+J+1) K` -- **(E3)** the length-`K`
  gap suffix agrees, paper `g_{n+J+1+i} = g_{m+J+1+i}`, `1 ≤ i ≤ K`.
* `cap_near_n`, `cap_near_m : delta (·+J) ≤ D` -- **(E4)** near caps,
  paper `delta_{n+J}, delta_{m+J} ≤ D`.
* `cap_far_n`, `cap_far_m : delta (·+J+1+K) ≤ 2^K` -- **(E4)** far caps,
  paper `delta_{n+J+K+1}, delta_{m+J+K+1} ≤ 2^K`.

The gate **(E5)** `b (D-2) < 2^(J+1)` is a separate hypothesis of the
contradiction theorems (as `hsmall` is for `fork_merge_contradiction`),
so the same bundle serves every odd `b`. -/
structure ExchangeAt (n m J K D : ℕ) : Prop where
  one_le_J : 1 ≤ J
  one_le_K : 1 ≤ K
  block_prefix : SameBlock n m J
  differ : gap (n + J) ≠ gap (m + J)
  block_suffix : SameBlock (n + J + 1) (m + J + 1) K
  cap_near_n : delta (n + J) ≤ D
  cap_near_m : delta (m + J) ≤ D
  cap_far_n : delta (n + J + 1 + K) ≤ 2 ^ K
  cap_far_m : delta (m + J + 1 + K) ≤ 2 ^ K

/-- EXCH_1 supply, the statement-layer Prop (item-0017's target; pattern of
`HLQuantA`). For every threshold `t`, an exchange configuration whose base
points both sit at or beyond `t`, carrying the `b = 1` gate (E5)
`(D - 2) < 2^(J+1)`. Threshold-uniformity is what lets `item-0010` pick a
site beyond any prescribed dyadic depth `s` (the s-uniformization: take
`t = s + 2`). NEVER proved here -- supplying it is exactly the `b = 1`
case of item-0017. -/
def ExchangeSupply1 : Prop :=
  ∀ t : ℕ, ∃ n m J K D : ℕ,
    t ≤ n ∧ t ≤ m ∧ ExchangeAt n m J K D ∧ ((D : ℝ) - 2 < 2 ^ (J + 1))

/-- Dyadic specialisation of the rational-to-lattice layer (`Basic.lean`
`rational_delta_eventually_lattice`) to denominators `2^s`, with the odd
part `b = 1` baked in. If `S = a / 2^s` then `delta n ∈ 2ℤ` for every
`n ≥ s + 2`.

The proof mirrors `rational_delta_eventually_lattice` (integrality of
`delta J` for `J ≥ s` via `delta_block` at `0` plus the dyadic
denominator, then one `delta_recursion` step using `gap`-evenness for the
factor 2), but keeps `b = 1` explicit rather than extracting the odd part
of a general rational denominator. -/
theorem dyadic_delta_even_lattice {a : ℤ} {s : ℕ} (hS : (a : ℝ) / 2 ^ s = S) :
    ∀ n : ℕ, s + 2 ≤ n → ∃ z : ℤ, delta n = 2 * (z : ℝ) := by
  -- `delta 0 = S - 2 = a/2^s - 2 = (a - 2^(s+1))/2^s`
  have hS2 : erdosSeries / 2 = (a : ℝ) / 2 ^ s := by
    have hSdef : S = erdosSeries / 2 := rfl
    rw [← hSdef, hS]
  set c : ℤ := a - 2 ^ (s + 1) with hc
  have hδ0 : delta 0 = (c : ℝ) / 2 ^ s := by
    have h1 : delta 0 = ∑' j : ℕ, (gap j : ℝ) / 2 ^ (j + 1) := by
      show (∑' j : ℕ, (gap (0 + j) : ℝ) / 2 ^ (j + 1)) = _
      simp
    rw [h1, gap_series_identity, hS2, hc]
    have hpos : (0 : ℝ) < 2 ^ s := by positivity
    push_cast
    field_simp
    ring
  -- integer lattice for `J ≥ s`
  have hint : ∀ J : ℕ, s ≤ J → ∃ z : ℤ, delta J = (z : ℝ) := by
    intro J hJ
    have hblk : delta J
        = (2 : ℝ) ^ J * delta 0
          - ∑ i ∈ Finset.range J, (2 : ℝ) ^ (J - 1 - i) * (gap i : ℝ) := by
      have h := delta_block 0 J; simpa using h
    have hpow : (2 : ℝ) ^ J * delta 0 = ((2 ^ (J - s) * c : ℤ) : ℝ) := by
      rw [hδ0]
      have hsplit : (2 : ℝ) ^ J = 2 ^ (J - s) * 2 ^ s := by
        rw [← pow_add]; congr 1; omega
      have hpos : (0 : ℝ) < 2 ^ s := by positivity
      rw [hsplit]; push_cast; field_simp; ring
    refine ⟨2 ^ (J - s) * c
        - (∑ i ∈ Finset.range J, 2 ^ (J - 1 - i) * (gap i : ℤ)), ?_⟩
    rw [hblk, hpow]; push_cast; ring
  -- evenness: one recursion step using `gap`-parity from index 1 on
  intro n hn
  obtain ⟨n', rfl⟩ : ∃ n', n = n' + 1 := ⟨n - 1, by omega⟩
  have hn's : s ≤ n' := by omega
  have hn'1 : 1 ≤ n' := by omega
  obtain ⟨z', hz'⟩ := hint n' hn's
  obtain ⟨k, hk⟩ := gap_even hn'1
  refine ⟨z' - (k : ℤ), ?_⟩
  have hgap : (gap n' : ℝ) = 2 * (k : ℝ) := by rw [hk]; push_cast; ring
  rw [delta_recursion n', hz', hgap]; push_cast; ring

/-- The finite EXCH core (O4 normal form), for any `b > 0`: one exchange
configuration whose base points `n, m` sit on the even lattice `b·delta ∈
2ℤ`, together with the gate (E5) `b (D-2) < 2^(J+1)`, is contradictory.

Proof (Hamming-distance-1 sibling of `fork_merge_contradiction`, same
toolkit): the shared prefix quantizes `b(delta(n+J) - delta(m+J)) ∈
2^(J+1)ℤ` (`repeated_block_quantization`); the near caps (E4) with `2 ≤
delta` and the gate (E5) force that lattice element to `0`, so `delta(n+J) =
delta(m+J)`; the block identity over the next `K+1` gaps
(`delta_block`), with the suffix (E3) collapsing all but the single
differing gap, gives `0 = 2^K·d + Δ_end` where `d = gap(n+J) - gap(m+J)`
and `Δ_end` is the far-tail difference; the far caps (E4) with `2 ≤ delta`
give `|Δ_end| < 2^K`, hence `|d| < 1`, contradicting `d ≠ 0` (the differing
gap). -/
theorem exchange_contradiction {b n m J K D : ℕ} (hb : 0 < b)
    (hlat_n : ∃ z : ℤ, (b : ℝ) * delta n = 2 * (z : ℝ))
    (hlat_m : ∃ z : ℤ, (b : ℝ) * delta m = 2 * (z : ℝ))
    (hEx : ExchangeAt n m J K D)
    (hgate : (b : ℝ) * ((D : ℝ) - 2) < 2 ^ (J + 1)) :
    False := by
  obtain ⟨hJ, hK, hpre, hdiff, hsuf, hcapn, hcapm, hfarn, hfarm⟩ := hEx
  have hbpos : (0 : ℝ) < b := by exact_mod_cast hb
  -- unconditional floors `2 ≤ delta` at the four working indices
  have h2n : (2 : ℝ) ≤ delta (n + J) := two_le_delta (by omega)
  have h2m : (2 : ℝ) ≤ delta (m + J) := two_le_delta (by omega)
  have h2fn : (2 : ℝ) ≤ delta (n + J + 1 + K) := two_le_delta (by omega)
  have h2fm : (2 : ℝ) ≤ delta (m + J + 1 + K) := two_le_delta (by omega)
  -- Step A: prefix quantization into `2^(J+1)ℤ`
  obtain ⟨z, hz⟩ := repeated_block_quantization hlat_n hlat_m hpre
  -- Step B: the near caps + gate force `delta(n+J) = delta(m+J)`
  have hfork_small : |(b : ℝ) * (delta (n + J) - delta (m + J))| < 2 ^ (J + 1) := by
    have hdlt : |delta (n + J) - delta (m + J)| ≤ (D : ℝ) - 2 := by
      rw [abs_le]
      exact ⟨by linarith [h2n, hcapm], by linarith [hcapn, h2m]⟩
    rw [abs_mul, abs_of_nonneg hbpos.le]
    calc (b : ℝ) * |delta (n + J) - delta (m + J)|
        ≤ (b : ℝ) * ((D : ℝ) - 2) := mul_le_mul_of_nonneg_left hdlt hbpos.le
      _ < 2 ^ (J + 1) := hgate
  have hz0 : z = 0 := by
    by_contra hzne
    have h1 : (1 : ℝ) ≤ |(z : ℝ)| := by
      have h : (1 : ℤ) ≤ |z| := Int.one_le_abs (by omega)
      exact_mod_cast h
    rw [hz, abs_mul, abs_of_nonneg (by positivity : (0 : ℝ) ≤ (2 : ℝ) ^ (J + 1))] at hfork_small
    have h2pos : (0 : ℝ) < 2 ^ (J + 1) := by positivity
    have hle := mul_le_mul_of_nonneg_left h1 h2pos.le
    rw [mul_one] at hle
    linarith [hfork_small, hle]
  have hforkeq : delta (n + J) = delta (m + J) := by
    have hb0 : (b : ℝ) * (delta (n + J) - delta (m + J)) = 0 := by rw [hz, hz0]; simp
    rcases mul_eq_zero.mp hb0 with h | h
    · exact absurd h (ne_of_gt hbpos)
    · linarith [h]
  -- Step C: block identity over the next `K+1` gaps; suffix collapses all
  -- but the single differing gap, leaving `Δ_end = -(2^K · d)`.
  have hSig : (∑ i ∈ Finset.range (K + 1), (2 : ℝ) ^ (K + 1 - 1 - i) * (gap (n + J + i) : ℝ))
      - (∑ i ∈ Finset.range (K + 1), (2 : ℝ) ^ (K + 1 - 1 - i) * (gap (m + J + i) : ℝ))
      = 2 ^ K * ((gap (n + J) : ℝ) - (gap (m + J) : ℝ)) := by
    rw [← Finset.sum_sub_distrib, Finset.sum_range_succ']
    have hzero : ∀ i ∈ Finset.range K,
        (2 : ℝ) ^ (K + 1 - 1 - (i + 1)) * (gap (n + J + (i + 1)) : ℝ)
          - (2 : ℝ) ^ (K + 1 - 1 - (i + 1)) * (gap (m + J + (i + 1)) : ℝ) = 0 := by
      intro i hi
      rw [Finset.mem_range] at hi
      have hg : gap (n + J + (i + 1)) = gap (m + J + (i + 1)) := by
        have h := hsuf i hi
        rwa [show n + J + 1 + i = n + J + (i + 1) from by omega,
          show m + J + 1 + i = m + J + (i + 1) from by omega] at h
      rw [hg]; ring
    rw [Finset.sum_eq_zero hzero, zero_add,
      show K + 1 - 1 - 0 = K from by omega, Nat.add_zero, Nat.add_zero]
    ring
  have hblk_n := delta_block (n + J) (K + 1)
  have hblk_m := delta_block (m + J) (K + 1)
  rw [show n + J + (K + 1) = n + J + 1 + K from by omega] at hblk_n
  rw [show m + J + (K + 1) = m + J + 1 + K from by omega] at hblk_m
  have hDend : delta (n + J + 1 + K) - delta (m + J + 1 + K)
      = -(2 ^ K * ((gap (n + J) : ℝ) - (gap (m + J) : ℝ))) := by
    rw [hblk_n, hblk_m, hforkeq]; linear_combination -hSig
  -- Step D: the far caps bound `|Δ_end| < 2^K`, hence `|d| < 1`, but `d ≠ 0`.
  have hDend_lt : |delta (n + J + 1 + K) - delta (m + J + 1 + K)| < 2 ^ K := by
    rw [abs_lt]
    exact ⟨by linarith [h2fn, hfarm], by linarith [hfarn, h2fm]⟩
  rw [hDend, abs_neg, abs_mul, abs_of_nonneg (by positivity : (0 : ℝ) ≤ (2 : ℝ) ^ K)] at hDend_lt
  have h2Kpos : (0 : ℝ) < 2 ^ K := by positivity
  have hd_ge1 : (1 : ℝ) ≤ |(gap (n + J) : ℝ) - (gap (m + J) : ℝ)| := by
    -- a distance-≥-1 fact for two distinct naturals, by parity-free casework
    rcases Nat.lt_or_ge (gap (n + J)) (gap (m + J)) with h | h
    · have hle : (gap (n + J) : ℝ) ≤ (gap (m + J) : ℝ) := by exact_mod_cast h.le
      have h1 : (gap (n + J) : ℝ) + 1 ≤ (gap (m + J) : ℝ) := by exact_mod_cast h
      rw [abs_of_nonpos (by linarith)]; linarith
    · have hgt : gap (m + J) < gap (n + J) := lt_of_le_of_ne h fun hh => hdiff hh.symm
      have hle : (gap (m + J) : ℝ) ≤ (gap (n + J) : ℝ) := by exact_mod_cast h
      have h1 : (gap (m + J) : ℝ) + 1 ≤ (gap (n + J) : ℝ) := by exact_mod_cast hgt
      rw [abs_of_nonneg (by linarith)]; linarith
  have hcontra := mul_le_mul_of_nonneg_left hd_ge1 h2Kpos.le
  rw [mul_one] at hcontra
  linarith [hDend_lt, hcontra]

/-- EXCH_1 (b = 1): one exchange configuration with base points beyond the
dyadic depth `s` contradicts `S = a / 2^s`. The s-uniformization is
`s + 2 ≤ min n m` (the even lattice `delta ∈ 2ℤ` at the base points needs
`n, m ≥ s + 2`; cf. `dyadic_delta_even_lattice`). -/
theorem exchange_contradiction_1 {a : ℤ} {s n m J K D : ℕ}
    (hS : (a : ℝ) / 2 ^ s = S)
    (hn : s + 2 ≤ n) (hm : s + 2 ≤ m)
    (hEx : ExchangeAt n m J K D)
    (hgate : (D : ℝ) - 2 < 2 ^ (J + 1)) :
    False := by
  have hlat := dyadic_delta_even_lattice hS
  refine exchange_contradiction (b := 1) one_pos ?_ ?_ hEx ?_
  · obtain ⟨z, hz⟩ := hlat n hn; exact ⟨z, by simpa using hz⟩
  · obtain ⟨z, hz⟩ := hlat m hm; exact ⟨z, by simpa using hz⟩
  · simpa using hgate

/-- item-0010, milestone 1: the exchange supply kills every dyadic
denominator, i.e. `S ∉ ℤ[1/2]`. -/
theorem dyadic_of_exchange_supply (h : ExchangeSupply1) : ¬ IsDyadic S := by
  rintro ⟨a, s, hS⟩
  obtain ⟨n, m, J, K, D, hn, hm, hEx, hgate⟩ := h (s + 2)
  exact exchange_contradiction_1 hS hn hm hEx hgate

/-! ### Certificate schema (milestone 2)

A single exchange site is an unconditional exclusion device: it kills every
dyadic representation `a / 2^s` whose depth its base points cover. This is
the "machine-checked form and scalable schema" the item-0010 mandate asks
for. Discharging its hypotheses at the verdict's numerical sites is a
kernel-budget wall on two independent axes -- see the report / the
`exchange_site_excludes` docstring. The existing finite-exclusion layer
(denominator `> 10^1050`) already dominates these ranges numerically; the
value here is the checked reduction shape, reusable by any future
site-production route. -/

/-- Certificate schema: one exchange site (with its `b = 1` gate) excludes
`S = a / 2^s` for **every** `s` with `s + 2 ≤ min n m` -- an unconditional
`S ≠ a / 2^s` over the whole s-range the site's depth covers.

Instantiating this at the verdict's certificates `(5,5,34)` (gap index
`5049413`, primes `≈ 8.69·10^7`) and `(6,6,64)` (anchor `74863199`) in the
kernel hits two walls, both without `native_decide` (standing policy):
(i) the gap-word clauses (E1)--(E3) need `q = Nat.nth Nat.Prime` at index
`≈ 5·10^6`, i.e. a prime count below `≈ 8.7·10^7`, not kernel-reducible;
(ii) the `delta` caps (E4) are infinite tails needing an analytic bound
(Cramér--Granville / Markov selection), not finite computation. Both are
recorded as budget walls; no site is landed unconditionally in-kernel. -/
theorem exchange_site_excludes {n m J K D : ℕ} (hEx : ExchangeAt n m J K D)
    (hgate : (D : ℝ) - 2 < 2 ^ (J + 1)) :
    ∀ (a : ℤ) (s : ℕ), s + 2 ≤ n → s + 2 ≤ m → (a : ℝ) / 2 ^ s ≠ S := by
  intro a s hn hm hSeq
  exact exchange_contradiction_1 hSeq hn hm hEx hgate

end

end Erdos251
