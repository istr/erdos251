import Mathlib
import Erdos251.Basic
import Erdos251.Hypotheses
import Erdos251.Counting.Words
import Erdos251.Counting.SingularSeries
import Erdos251.Counting.Lemmata

/-!
# Lemma 4.3 layer: consecutive transfer, the Bonferroni cut, and the statement

The s4 structural core (next-prime characterization, prefix-sum point
sets, `mem_oneExtensions_of_prime_shift`), the s5 counting/analytic layers
(the five-term additive Bonferroni cut, the `tendsto_pow_loglog_div_log`
basket), and the frozen statement `consCount_lower_bound`.

RELOCATION ONLY (item-0016). The body below is byte-identical to
`Erdos251/Counting.lean` lines 959-1656 at commit
`6683ee0f009baeb5dd6e759f265544e7f91af23d`,
sha256 `fbb12b26407d5dd91ca7312fa25a51c8ec254b8a58c479d3329a36aebfcd6bb5`.
No statement, docstring, proof or name was changed. Provenance, the index
conventions, the traceability table and the module map live in the umbrella
`Erdos251/Counting.lean`.
-/

namespace Erdos251

noncomputable section

/-! ### Proof-layer helpers for Lemma 4.3 (item-0015 s4; not statements)

The STRUCTURAL CORE of T3 step 1 (kickoff v4's "combinatorial bound"), landed
verified ahead of the counting/analytic layers. Two halves, and they confirm the
kickoff's reconstruction on both of its flagged sub-claims:

* `isConsecRealization_of_primes` (via `q_add_eq_of_primes` and the next-prime
  characterization `q_succ_eq_of_no_prime_between`): if every point of `H(w)` is
  prime-shifted from the anchor `a = q n` and NO other offset in `(0, D)` is,
  then `n` realizes `w` consecutively. The induction runs on `Nat.count`, so the
  `Nat.nth`/`Nat.count` bridge is the only glue needed.
* `mem_oneExtensions_of_prime_shift`: the "bad" offsets are EXACTLY the ones
  Lemma 4.2 sums over. Parity kills the odd offsets (`even_of_prime_shift` --
  the kickoff's "no case needed"), and `admissible_of_primes` forces
  admissibility, needing only `a > |H| + 1` -- confirming the kickoff's estimate
  that this `x₀` is cheap (`√x > L + 2` suffices).

`even_of_admissible` discharges the 4.3 docstring's claim that evenness is not
hypothesised but follows from admissibility plus `0 ∈ H(w)`.

STILL OPEN above these (see HANDOVER): step 1's Finset card inequality, the
HLQuantA instantiations (steps 2-3, consuming this session's Lemma 4.2), the
crude `√x` bound (step 4), and the `x₀` assembly (step 5, two growth-rate
limits). The five-term cut is confirmed SOUND; it is not a one-session item.
-/

/-- The next-prime characterization of `q`: if `b` is prime, `b > q n`, and no
prime lies strictly between, then `b = q (n+1)`. -/
theorem q_succ_eq_of_no_prime_between {n a b : ℕ} (hqn : q n = a) (hb : b.Prime)
    (hab : a < b) (hgap : ∀ m, a < m → m < b → ¬ m.Prime) : q (n + 1) = b := by
  have ha : a.Prime := hqn ▸ q_prime n
  have hca : Nat.count Nat.Prime a = n := by
    rw [← hqn]; simpa [q] using Nat.count_nth_of_infinite Nat.infinite_setOf_prime n
  have hcb : Nat.count Nat.Prime b = n + 1 := by
    have key : ∀ m, a + 1 ≤ m → m ≤ b → Nat.count Nat.Prime m = n + 1 := by
      intro m
      induction m with
      | zero => omega
      | succ k ih =>
        intro hm1 hm2
        rcases Nat.lt_or_ge (a + 1) (k + 1) with h | h
        · have hnp : ¬ k.Prime := hgap k (by omega) (by omega)
          rw [Nat.count_succ, ih (by omega) (by omega), if_neg hnp]
        · have hk : k = a := by omega
          subst hk
          rw [Nat.count_succ, hca, if_pos ha]
    exact key b (by omega) le_rfl
  rw [q, ← hcb, Nat.nth_count hb]

/-- Evenness is not a hypothesis of Lemma 4.3: it FOLLOWS from admissibility.
`ν_H(2) < 2` means `H` occupies a single class mod 2, and `0 ∈ H` says it is
the even one. -/
theorem even_of_admissible {H : Finset ℕ} (h0 : 0 ∈ H) (hH : IsAdmissible H) :
    ∀ h ∈ H, Even h := by
  intro h hh
  have h2 := hH 2 Nat.prime_two
  rw [nuMod] at h2
  have hcast : (h : ZMod 2) = ((0 : ℕ) : ZMod 2) := by
    by_contra hne
    have hsub : ({((0 : ℕ) : ZMod 2), (h : ZMod 2)} : Finset (ZMod 2))
        ⊆ H.image (Nat.cast : ℕ → ZMod 2) := by
      intro z hz
      rw [Finset.mem_insert, Finset.mem_singleton] at hz
      rcases hz with rfl | rfl
      · exact Finset.mem_image.mpr ⟨0, h0, rfl⟩
      · exact Finset.mem_image.mpr ⟨h, hh, rfl⟩
    have hc : ({((0 : ℕ) : ZMod 2), (h : ZMod 2)} : Finset (ZMod 2)).card = 2 := by
      rw [Finset.card_insert_of_not_mem (by simpa [eq_comm] using hne), Finset.card_singleton]
    have := Finset.card_le_card hsub
    omega
  rw [Nat.cast_zero, ZMod.natCast_zmod_eq_zero_iff_dvd] at hcast
  exact Nat.even_iff.mpr (by omega)

/-- The prefix-sum enumeration of `wordPointSet` is monotone (no hypothesis). -/
theorem wordPointSet_sum_mono {w : ℕ → ℕ} {i j : ℕ} (hij : i ≤ j) :
    (∑ m ∈ Finset.range i, w m) ≤ ∑ m ∈ Finset.range j, w m :=
  Finset.sum_le_sum_of_subset (Finset.range_subset.mpr hij)

/-- `|H(w)| = L+1` forces the prefix sums to be STRICTLY increasing on `[0,L]`
(they are monotone, and the cardinality says they are injective). -/
theorem wordPointSet_sum_strictMono {w : ℕ → ℕ} {L : ℕ}
    (hcard : (wordPointSet w L).card = L + 1) {i j : ℕ} (hj : j ≤ L) (hij : i < j) :
    (∑ m ∈ Finset.range i, w m) < ∑ m ∈ Finset.range j, w m := by
  have hinj : Set.InjOn (fun j : ℕ => ∑ m ∈ Finset.range j, w m) (Finset.range (L + 1)) := by
    rw [← Finset.card_image_iff, ← wordPointSet, hcard, Finset.card_range]
  refine lt_of_le_of_ne (wordPointSet_sum_mono hij.le) (fun he => ?_)
  have := hinj (by simp; omega : i ∈ Finset.range (L + 1))
    (by simp; omega : j ∈ Finset.range (L + 1)) he
  omega

theorem mem_wordPointSet {w : ℕ → ℕ} {L : ℕ} {y : ℕ} :
    y ∈ wordPointSet w L ↔ ∃ j ≤ L, (∑ m ∈ Finset.range j, w m) = y := by
  rw [wordPointSet, Finset.mem_image]
  constructor
  · rintro ⟨j, hj, rfl⟩
    exact ⟨j, by simpa [Nat.lt_succ_iff] using hj, rfl⟩
  · rintro ⟨j, hj, rfl⟩
    exact ⟨j, Finset.mem_range.mpr (by omega), rfl⟩

/-- The span of `H(w)` is the LAST prefix sum. (The `e`-parametrized
`offsetSpan_wordPointSet` is the section-5 sibling of this; this form takes no
enumeration.) -/
theorem offsetSpan_wordPointSet_eq_sum {w : ℕ → ℕ} {L : ℕ} :
    offsetSpan (wordPointSet w L) = ∑ m ∈ Finset.range L, w m := by
  refine le_antisymm (Finset.sup_le (fun y hy => ?_)) ?_
  · obtain ⟨j, hj, rfl⟩ := mem_wordPointSet.mp hy
    exact wordPointSet_sum_mono hj
  · exact Finset.le_sup (f := id) (mem_wordPointSet.mpr ⟨L, le_rfl, rfl⟩)

/-- T3 step 1, the CORE transfer (induction half): if every point of `H(w)` is
prime-shifted from `a = q n` and no OTHER offset in `(0, D)` is, then the primes
following `a` are exactly `a + H(w)`, in order. -/
theorem q_add_eq_of_primes {w : ℕ → ℕ} {L n a : ℕ}
    (hcard : (wordPointSet w L).card = L + 1) (hqn : q n = a)
    (hprime : ∀ h ∈ wordPointSet w L, (a + h).Prime)
    (hnone : ∀ m, 0 < m → m < offsetSpan (wordPointSet w L) → m ∉ wordPointSet w L →
      ¬ (a + m).Prime) :
    ∀ j ≤ L, q (n + j) = a + ∑ m ∈ Finset.range j, w m := by
  intro j
  induction j with
  | zero => intro _; simpa using hqn
  | succ i ih =>
    intro hiL
    have hqi : q (n + i) = a + ∑ m ∈ Finset.range i, w m := ih (by omega)
    have hsi : (∑ m ∈ Finset.range i, w m) < ∑ m ∈ Finset.range (i + 1), w m :=
      wordPointSet_sum_strictMono hcard hiL (by omega)
    have hstep : q (n + i + 1) = a + ∑ m ∈ Finset.range (i + 1), w m := by
      refine q_succ_eq_of_no_prime_between hqi ?_ (by omega) ?_
      · exact hprime _ (mem_wordPointSet.mpr ⟨i + 1, hiL, rfl⟩)
      · intro y hy1 hy2
        obtain ⟨m, rfl⟩ : ∃ m, y = a + m := ⟨y - a, by omega⟩
        refine hnone m (by omega) ?_ ?_
        · rw [offsetSpan_wordPointSet_eq_sum]
          have hle : (∑ m ∈ Finset.range (i + 1), w m) ≤ ∑ m ∈ Finset.range L, w m :=
            wordPointSet_sum_mono hiL
          omega
        · intro hm
          obtain ⟨j, hj, hjm⟩ := mem_wordPointSet.mp hm
          -- `s i < s j < s (i+1)` is impossible for a strictly monotone `s`
          rcases Nat.lt_trichotomy j (i + 1) with h | h | h
          · have hle : (∑ m ∈ Finset.range j, w m) ≤ ∑ m ∈ Finset.range i, w m :=
              wordPointSet_sum_mono (by omega)
            omega
          · rw [h] at hjm; omega
          · have hle : (∑ m ∈ Finset.range (i + 1), w m) ≤ ∑ m ∈ Finset.range j, w m :=
              wordPointSet_sum_mono (by omega)
            omega
    rwa [show n + (i + 1) = n + i + 1 by ring]

/-- T3 step 1, the CORE transfer. -/
theorem isConsecRealization_of_primes {w : ℕ → ℕ} {L n a : ℕ}
    (hcard : (wordPointSet w L).card = L + 1) (hqn : q n = a)
    (hprime : ∀ h ∈ wordPointSet w L, (a + h).Prime)
    (hnone : ∀ m, 0 < m → m < offsetSpan (wordPointSet w L) → m ∉ wordPointSet w L →
      ¬ (a + m).Prime) :
    IsConsecRealization w L n := by
  have key := q_add_eq_of_primes hcard hqn hprime hnone
  intro i hi
  rw [Finset.mem_range] at hi
  have h1 : q (n + i) = a + ∑ m ∈ Finset.range i, w m := key i (by omega)
  have h2 : q (n + i + 1) = a + ∑ m ∈ Finset.range (i + 1), w m := by
    have := key (i + 1) (by omega)
    rwa [show n + (i + 1) = n + i + 1 by ring] at this
  have hsucc : (∑ m ∈ Finset.range (i + 1), w m) = (∑ m ∈ Finset.range i, w m) + w i :=
    Finset.sum_range_succ w i
  rw [gap, h1, h2, hsucc]
  omega

/-- If every shift `a + h` is prime and the anchor `a` exceeds every prime that
could cover a residue class, then `H` is admissible: a covering prime `p` would
divide the prime `a + h > p`. This is the `x₀` the kickoff flags as "cheap":
`a > √x > |H|+1` suffices. -/
theorem admissible_of_primes {H : Finset ℕ} {a : ℕ}
    (hprime : ∀ h ∈ H, (a + h).Prime)
    (hbig : ∀ p : ℕ, p.Prime → p ≤ H.card → p < a) :
    IsAdmissible H := by
  intro p hp
  by_contra hcon
  haveI : Fact p.Prime := ⟨hp⟩
  haveI : NeZero p := ⟨hp.pos.ne'⟩
  have hle : nuMod H p ≤ p := by
    rw [nuMod]
    have h := Finset.card_le_univ (H.image (Nat.cast : ℕ → ZMod p))
    rwa [ZMod.card p] at h
  have hnu : nuMod H p = p := by omega
  have huniv : H.image (Nat.cast : ℕ → ZMod p) = Finset.univ := by
    apply Finset.eq_univ_of_card
    rw [← nuMod, hnu, ZMod.card]
  have hmem : (-(a : ZMod p)) ∈ H.image (Nat.cast : ℕ → ZMod p) := by
    rw [huniv]; exact Finset.mem_univ _
  obtain ⟨h, hh, hcast⟩ := Finset.mem_image.mp hmem
  have hdvd : p ∣ a + h := by
    have hz : ((a + h : ℕ) : ZMod p) = 0 := by push_cast [hcast]; ring
    exact (ZMod.natCast_zmod_eq_zero_iff_dvd _ _).mp hz
  have heq : p = a + h := ((hprime h hh).eq_one_or_self_of_dvd p hdvd).resolve_left hp.ne_one
  -- `p` covers a class, so `p ≤ ν_H(p) = |image| ≤ |H|`, whence `p < a ≤ a + h = p`
  have hpH : p ≤ H.card := by
    have : nuMod H p ≤ H.card := Finset.card_image_le
    omega
  have := hbig p hp hpH
  omega

/-- The anchor is odd (it exceeds 2 and is prime), so a prime shift forces the
offset even. This is the kickoff's "odd `j` needs no case". -/
theorem even_of_prime_shift {a m : ℕ} (ha : a.Prime) (ha2 : 2 < a)
    (ham : (a + m).Prime) : Even m := by
  by_contra hodd
  rw [Nat.not_even_iff_odd] at hodd
  have haodd : Odd a := ha.odd_of_ne_two (by omega)
  have heven : Even (a + m) := haodd.add_odd hodd
  have := (Nat.Prime.even_iff ham).mp heven
  omega

/-- T3 step 1, the classification: an offset in `(0, D)` that is NOT a point of
`H` but whose shift is prime is necessarily a ONE-EXTENSION of `H`. Parity kills
the odd offsets; admissibility is forced by `admissible_of_primes`. So the only
"bad" offsets are the ones Lemma 4.2 sums over. -/
theorem mem_oneExtensions_of_prime_shift {H : Finset ℕ} {a m : ℕ}
    (h0 : 0 ∈ H) (hm0 : 0 < m) (hmD : m < offsetSpan H) (hmH : m ∉ H)
    (hprime : ∀ h ∈ H, (a + h).Prime) (ham : (a + m).Prime)
    (hbig : ∀ p : ℕ, p.Prime → p ≤ H.card + 1 → p < a) :
    m ∈ oneExtensions H := by
  classical
  have hains : ∀ h ∈ insert m H, (a + h).Prime := by
    intro h hh
    rcases Finset.mem_insert.mp hh with rfl | hh
    · exact ham
    · exact hprime h hh
  have ha : a.Prime := by simpa using hprime 0 h0
  have ha2 : 2 < a := by
    have := hbig 2 Nat.prime_two (by have := Finset.card_pos.mpr ⟨0, h0⟩; omega)
    omega
  rw [oneExtensions, Finset.mem_filter, Finset.mem_range]
  refine ⟨hmD, even_of_prime_shift ha ha2 ham, hm0, hmH, ?_⟩
  refine admissible_of_primes hains (fun p hp hpc => hbig p hp ?_)
  exact le_trans hpc (Finset.card_insert_le _ _)

/-! ### Proof-layer helpers for Lemma 4.3, the counting/analytic layers (item-0015 s5)

The five-term additive Bonferroni cut of the kickoff, completed above the s4
structural core. Three layers, in dependency order:

* `consCount_bonferroni` (step 1): the Finset card inequality, ADDITIVE by design
  (no `Nat` subtraction anywhere). `π_H(x)` splits three ways -- anchors below
  `√x`, anchors with a prime one-point extension, and the good anchors, which
  `isConsecRealization_of_primes` transfers into `N_cons` injectively via
  `Nat.count`.
* `modelMass_insert` (step 2): the one clean insert-algebra equation, kept
  division-shaped.
* `mul_log_sq_le` / `mul_log_le` (step 5's uniformity): the budget
  `|H| = L+1 ≤ 4 lnln x - 1` eliminates `L` in favour of `t = lnln x` ALONE, so
  every threshold below is independent of `(w, L)` as the kickoff requires. Both
  bound `ln (L+2) ≤ L+1 ≤ 4t` (`Real.log_le_sub_one_of_pos`), which collapses the
  kickoff's `ln(4t+2)` factors to pure powers of `t`; this is why one limit
  (`tendsto_pow_loglog_div_log`) serves the whole basket. The `L = 0` corner needs
  no case split, exactly as booked.

Rule-12 landing (steering, PRE-CLEARED): both closing clauses are monotone in `x`
and `x₀` is astronomical; the assembly is `Tendsto`/`eventually` extraction only
and never materializes an explicit `x₀`.
-/

/-- Bridge from `Nat.count` (computable) to `Nat.nth` (not), used by
`consCount_bonferroni` and by the section-5 smoke tests in
`Counting/Construction.lean`. Flagged as glue in the traceability table. -/
theorem q_eq_of_count {n p : ℕ} (hp : p.Prime) (hc : Nat.count Nat.Prime p = n) :
    q n = p := by
  rw [q, ← hc, Nat.nth_count hp]

/-- `0 ∈ H(w)` always: the empty prefix sum. -/
theorem zero_mem_wordPointSet {w : ℕ → ℕ} {L : ℕ} : 0 ∈ wordPointSet w L :=
  mem_wordPointSet.mpr ⟨0, Nat.zero_le _, by simp⟩

/-- `Nat.count Nat.Prime a < a` for prime `a`: the count misses `0 ∈ range a`,
which is not prime. Feeds the good branch's `n < x + 1`. -/
theorem count_lt_self_of_prime {a : ℕ} (ha : a.Prime) : Nat.count Nat.Prime a < a := by
  rw [Nat.count_eq_card_filter_range]
  have h0 : a ≠ 0 := ha.ne_zero
  have hsub : (Finset.range a).filter (fun x => Nat.Prime x) ⊂ Finset.range a :=
    Finset.ssubset_iff_of_subset (Finset.filter_subset _ _) |>.mpr
      ⟨0, Finset.mem_range.mpr (by omega), by simp [Nat.not_prime_zero]⟩
  simpa using Finset.card_lt_card hsub

/-- T3 STEP 1: the additive Bonferroni card inequality. Every admissible tuple
anchor `a ≤ x` is either small (`a ≤ √x`), or carries a prime one-point extension
(the offsets Lemma 4.2 sums over), or is the anchor of a consecutive realization
of `w`. The threshold `L + 2 ≤ √x` is the cheap one flagged by the s4 core: it
feeds `mem_oneExtensions_of_prime_shift`'s `hbig`. -/
theorem consCount_bonferroni {w : ℕ → ℕ} {L x : ℕ}
    (hcard : (wordPointSet w L).card = L + 1)
    (hthr : ((L : ℝ) + 2) ≤ Real.sqrt x) :
    tupleCount (wordPointSet w L) x
      ≤ consCount w L x + (Nat.sqrt x + 1)
        + ∑ m ∈ oneExtensions (wordPointSet w L), tupleCount (insert m (wordPointSet w L)) x := by
  classical
  set H := wordPointSet w L with hHdef
  have h0 : 0 ∈ H := zero_mem_wordPointSet
  rw [tupleCount]
  set S := (Finset.range (x+1)).filter (fun a => ∀ h ∈ H, (a+h).Prime) with hSdef
  set P1 : ℕ → Prop := fun a => ((a:ℝ) ≤ Real.sqrt x) with hP1def
  set P2 : ℕ → Prop := fun a => ∃ m ∈ oneExtensions H, (a+m).Prime with hP2def
  have hsplit1 : (S.filter P1).card + (S.filter (fun a => ¬ P1 a)).card = S.card :=
    Finset.filter_card_add_filter_neg_card_eq_card _
  set T := S.filter (fun a => ¬ P1 a) with hTdef
  have hsplit2 : (T.filter P2).card + (T.filter (fun a => ¬ P2 a)).card = T.card :=
    Finset.filter_card_add_filter_neg_card_eq_card _
  have hmemS : ∀ a, a ∈ S ↔ (a ≤ x ∧ ∀ h ∈ H, (a+h).Prime) := by
    intro a; rw [hSdef, Finset.mem_filter, Finset.mem_range]
    constructor
    · rintro ⟨h1, h2⟩; exact ⟨by omega, h2⟩
    · rintro ⟨h1, h2⟩; exact ⟨by omega, h2⟩
  -- BRANCH 1: the small anchors inject into `range (Nat.sqrt x + 1)`
  have hsmall : (S.filter P1).card ≤ Nat.sqrt x + 1 := by
    have hsub : S.filter P1 ⊆ Finset.range (Nat.sqrt x + 1) := by
      intro a ha
      rw [Finset.mem_filter] at ha
      have hle : (a:ℝ) ≤ Real.sqrt x := ha.2
      have hnat : a * a ≤ x := by
        have hsq := Real.sq_sqrt (by positivity : (0:ℝ) ≤ (x:ℝ))
        have : ((a*a : ℕ) : ℝ) ≤ ((x:ℕ):ℝ) := by
          push_cast
          nlinarith [Real.sqrt_nonneg (x:ℝ), Nat.cast_nonneg (α := ℝ) a]
        exact_mod_cast this
      exact Finset.mem_range.mpr (by have := Nat.le_sqrt.mpr hnat; omega)
    calc (S.filter P1).card ≤ (Finset.range (Nat.sqrt x + 1)).card := Finset.card_le_card hsub
      _ = Nat.sqrt x + 1 := Finset.card_range _
  -- BRANCH 2: the anchors with a prime one-point extension
  have hext : (T.filter P2).card ≤ ∑ m ∈ oneExtensions H, tupleCount (insert m H) x := by
    have hsub : T.filter P2 ⊆ (oneExtensions H).biUnion
        (fun m => (Finset.range (x+1)).filter (fun a => ∀ h ∈ insert m H, (a+h).Prime)) := by
      intro a ha
      rw [Finset.mem_filter] at ha
      obtain ⟨m, hm, hmp⟩ := ha.2
      have haT : a ∈ T := ha.1
      rw [hTdef, Finset.mem_filter] at haT
      obtain ⟨hax, hall⟩ := (hmemS a).mp haT.1
      refine Finset.mem_biUnion.mpr ⟨m, hm, ?_⟩
      rw [Finset.mem_filter, Finset.mem_range]
      exact ⟨by omega, (Finset.forall_mem_insert _ _ _).mpr ⟨hmp, hall⟩⟩
    calc (T.filter P2).card
        ≤ ((oneExtensions H).biUnion
            (fun m => (Finset.range (x+1)).filter
              (fun a => ∀ h ∈ insert m H, (a+h).Prime))).card := Finset.card_le_card hsub
      _ ≤ ∑ m ∈ oneExtensions H, ((Finset.range (x+1)).filter
            (fun a => ∀ h ∈ insert m H, (a+h).Prime)).card := Finset.card_biUnion_le
      _ = ∑ m ∈ oneExtensions H, tupleCount (insert m H) x := by
            refine Finset.sum_congr rfl (fun m _ => ?_); rw [tupleCount]
  -- BRANCH 3: the good anchors ARE consecutive realizations
  have hgood : (T.filter (fun a => ¬ P2 a)).card ≤ consCount w L x := by
    rw [consCount]
    have key : ∀ a ∈ T.filter (fun a => ¬ P2 a),
        a.Prime ∧ q (Nat.count Nat.Prime a) = a ∧ a ≤ x ∧ Real.sqrt x < (a:ℝ)
          ∧ IsConsecRealization w L (Nat.count Nat.Prime a) := by
      intro a ha
      rw [Finset.mem_filter] at ha
      obtain ⟨haT, hnP2⟩ := ha
      rw [hTdef, Finset.mem_filter] at haT
      obtain ⟨haS, hnP1⟩ := haT
      obtain ⟨hax, hall⟩ := (hmemS a).mp haS
      have hap : a.Prime := by simpa using hall 0 h0
      have hqn : q (Nat.count Nat.Prime a) = a := q_eq_of_count hap rfl
      have hsqlt : Real.sqrt x < (a:ℝ) := by
        simp only [hP1def, not_le] at hnP1; exact hnP1
      have hbig : ∀ p : ℕ, p.Prime → p ≤ H.card + 1 → p < a := by
        intro p hp hpc
        have hpR : (p:ℝ) ≤ (L:ℝ) + 2 := by
          rw [hcard] at hpc
          have : (p:ℝ) ≤ ((L+2 : ℕ) : ℝ) := by exact_mod_cast hpc
          push_cast at this; linarith
        have : (p:ℝ) < (a:ℝ) := by linarith
        exact_mod_cast this
      have hnone : ∀ m, 0 < m → m < offsetSpan H → m ∉ H → ¬ (a+m).Prime := by
        intro m hm0 hmD hmH ham
        exact hnP2 ⟨m, mem_oneExtensions_of_prime_shift h0 hm0 hmD hmH hall ham hbig, ham⟩
      exact ⟨hap, hqn, hax, hsqlt, isConsecRealization_of_primes hcard hqn hall hnone⟩
    refine Finset.card_le_card_of_injOn (fun a => Nat.count Nat.Prime a) ?_ ?_
    · intro a ha
      obtain ⟨hap, hqn, hax, hsqlt, hreal⟩ := key a ha
      rw [Finset.mem_filter, Finset.mem_range]
      show Nat.count Nat.Prime a < x + 1 ∧ _
      refine ⟨?_, hreal, ?_, ?_⟩
      · have := count_lt_self_of_prime hap; omega
      · rw [hqn]; exact hsqlt
      · rw [hqn]; exact hax
    · intro a ha b hb hab
      obtain ⟨hap, hqa, _⟩ := key a ha
      obtain ⟨hbp, hqb, _⟩ := key b hb
      simp only at hab
      rw [← hqa, ← hqb, hab]
  omega

/-- T3 STEP 2: the insert algebra of `M_H(x)`. Kept division-shaped (the kickoff's
"no `field_simp` storms"): the extra point costs exactly one power of `ln x` and
one singular-series ratio. -/
theorem modelMass_insert {H : Finset ℕ} {m x : ℕ} (hm : m ∉ H)
    (hS : singularSeries H ≠ 0) (hs : Real.log x ≠ 0) :
    modelMass (insert m H) x
      = modelMass H x * (singularSeries (insert m H) / singularSeries H) / Real.log x := by
  classical
  rw [modelMass, modelMass, Finset.card_insert_of_not_mem hm, pow_succ]
  field_simp
  ring

/-- Step 5's uniformity, the 4.2 side: at the budget maximum `L + 2 ≤ 4t` the
extension factor `L ln(L+2)²` is bounded by `64 t³`, free of `(w, L)`. -/
theorem mul_log_sq_le {Lr t : ℝ} (hL0 : 0 ≤ Lr) (ht : 1 ≤ t) (hLt : Lr + 2 ≤ 4 * t) :
    Lr * Real.log (Lr + 2) ^ 2 ≤ 64 * t ^ 3 := by
  have hlog0 : 0 ≤ Real.log (Lr + 2) := Real.log_nonneg (by linarith)
  have hlog : Real.log (Lr + 2) ≤ 4 * t := by
    have := Real.log_le_sub_one_of_pos (show (0:ℝ) < Lr + 2 by linarith)
    linarith
  have h1 : Real.log (Lr + 2) ^ 2 ≤ (4*t)^2 := by nlinarith
  nlinarith [sq_nonneg t]

/-- Step 5's uniformity, the 4.1 side: the whole exponent of `modelMass_ge_exp`
is bounded by `196 t²` inside the budget, free of `(w, L)`. -/
theorem mul_log_le {Lr t : ℝ} (hL0 : 0 ≤ Lr) (ht : 1 ≤ t) (hLt : Lr + 2 ≤ 4 * t) :
    12 * Lr * Real.log (Lr + 2) + (Lr + 1) * t ≤ 196 * t ^ 2 := by
  have hlog0 : 0 ≤ Real.log (Lr + 2) := Real.log_nonneg (by linarith)
  have hlog : Real.log (Lr + 2) ≤ 4 * t := by
    have := Real.log_le_sub_one_of_pos (show (0:ℝ) < Lr + 2 by linarith)
    linarith
  nlinarith

/-- `√(e^y) = e^{y/2}`; the ONE Real/Nat-free sqrt bridge of the mass clause. -/
theorem sqrt_exp (y : ℝ) : Real.sqrt (Real.exp y) = Real.exp (y / 2) := by
  rw [show y = y/2 + y/2 by ring, Real.exp_add, Real.sqrt_mul_self (Real.exp_nonneg _)]
  ring_nf

section Lemma43Limits

open Filter

/-- Step 5's ONE limit: `(lnln x)^n / ln x → 0` for every `n`. With `s = ln x` this
is `(ln s)^n = o(s)` (`Real.isLittleO_pow_log_id_atTop`) composed with `ln x → ∞`.
Both closing clauses of 4.3 reduce to this, at `n = 3` (the 4.2 extension fraction)
and `n = 2` (the 4.1 mass margin). -/
theorem tendsto_pow_loglog_div_log (n : ℕ) :
    Tendsto (fun x : ℕ => (Real.log (Real.log x))^n / Real.log x) atTop (nhds 0) := by
  have h1 : Tendsto (fun s : ℝ => (Real.log s)^n / s) atTop (nhds 0) :=
    (Real.isLittleO_pow_log_id_atTop (n := n)).tendsto_div_nhds_zero
  exact h1.comp (Real.tendsto_log_atTop.comp tendsto_natCast_atTop_atTop)

/-- The eventual form of the limit: any fixed multiple of `(lnln x)^n` is
eventually below any fixed positive multiple of `ln x`. `c` is NOT assumed
nonnegative -- Lemma 4.2 exports `C₂` with no sign. -/
theorem eventually_pow_loglog_le (n : ℕ) (c : ℝ) {ε : ℝ} (hε : 0 < ε) :
    ∀ᶠ x : ℕ in atTop, c * (Real.log (Real.log x))^n ≤ ε * Real.log x := by
  have hlog : ∀ᶠ x : ℕ in atTop, (1:ℝ) ≤ Real.log x :=
    (Real.tendsto_log_atTop.comp tendsto_natCast_atTop_atTop).eventually_ge_atTop 1
  have h := (tendsto_pow_loglog_div_log n).eventually
    (gt_mem_nhds (show (0:ℝ) < ε / (|c| + 1) by positivity))
  filter_upwards [h, hlog] with x hx hs
  have hs0 : (0:ℝ) < Real.log x := by linarith
  rw [div_lt_iff₀ hs0] at hx
  have hT0 : (0:ℝ) ≤ (Real.log (Real.log x))^n := pow_nonneg (Real.log_nonneg hs) n
  have hcabs : (0:ℝ) < |c| + 1 := by positivity
  calc c * (Real.log (Real.log x))^n
      ≤ (|c| + 1) * (Real.log (Real.log x))^n := by
        refine mul_le_mul_of_nonneg_right ?_ hT0
        have := le_abs_self c; linarith
    _ ≤ (|c| + 1) * (ε / (|c| + 1) * Real.log x) :=
        mul_le_mul_of_nonneg_left hx.le hcabs.le
    _ = ε * Real.log x := by field_simp

/-- The mass margin (step 5, LIMIT B), in the `(w, L)`-free shape the budget
supplies: `x e^{-196 (lnln x)²} ≥ 8(√x + 1)` eventually. Reduces to
`s/2 - 196 (ln s)² → ∞`, i.e. `(ln s)² = o(s)`. -/
theorem eventually_mass_margin :
    ∀ᶠ x : ℕ in atTop, 8 * (Real.sqrt x + 1)
      ≤ (x:ℝ) * Real.exp (-(196 * (Real.log (Real.log x))^2)) := by
  have hlog12 : ∀ᶠ x : ℕ in atTop, (12:ℝ) ≤ Real.log x :=
    (Real.tendsto_log_atTop.comp tendsto_natCast_atTop_atTop).eventually_ge_atTop 12
  filter_upwards [eventually_pow_loglog_le 2 196 (show (0:ℝ) < 1/4 by norm_num),
    hlog12, eventually_ge_atTop 1] with x hxe hs hx1
  have hx0 : (0:ℝ) < (x:ℝ) := by exact_mod_cast Nat.lt_of_lt_of_le Nat.zero_lt_one hx1
  have hx1R : (1:ℝ) ≤ (x:ℝ) := by exact_mod_cast hx1
  have hsqrt : Real.sqrt (x:ℝ) = Real.exp (Real.log x / 2) := by
    conv_lhs => rw [← Real.exp_log hx0]
    exact sqrt_exp _
  have hxexp : (x:ℝ) * Real.exp (-(196 * (Real.log (Real.log x))^2))
      = Real.exp (Real.log x - 196 * (Real.log (Real.log x))^2) := by
    rw [show Real.log x - 196 * (Real.log (Real.log x))^2
        = Real.log x + (-(196 * (Real.log (Real.log x))^2)) by ring,
      Real.exp_add, Real.exp_log hx0]
  have hsq1 : (1:ℝ) ≤ Real.sqrt x := by
    rw [show (1:ℝ) = Real.sqrt 1 by simp]; exact Real.sqrt_le_sqrt hx1R
  have hlog16 : Real.log 16 < 3 := by
    rw [show (16:ℝ) = 2^4 by norm_num, Real.log_pow]
    have := Real.log_two_lt_d9
    push_cast; linarith
  rw [hxexp]
  calc 8 * (Real.sqrt x + 1) ≤ 16 * Real.sqrt x := by linarith
    _ = Real.exp (Real.log 16) * Real.exp (Real.log x / 2) := by
        rw [Real.exp_log (by norm_num), hsqrt]
    _ = Real.exp (Real.log 16 + Real.log x / 2) := by rw [Real.exp_add]
    _ ≤ Real.exp (Real.log x - 196 * (Real.log (Real.log x))^2) := by
        rw [Real.exp_le_exp]; linarith

/-- Step 5's threshold basket (E1)-(E6), `Eventually.and`-ed for the single
`Filter.eventually_atTop` extraction of 4.3's `x₀`. Every clause is free of
`(w, L)`: the uniformity discipline of the kickoff. The pattern is `cbudget`'s. -/
theorem consCount_basket (κ : ℝ) (C₄ : ℝ) (xA : ℕ) :
    ∀ᶠ x : ℕ in atTop,
      3 ≤ x ∧ xA ≤ x ∧ (1:ℝ) ≤ Real.log (Real.log x)
      ∧ 128 * C₄ * (Real.log (Real.log x))^3 ≤ (1/8) * Real.log x
      ∧ 8 * (Real.sqrt x + 1) ≤ (x:ℝ) * Real.exp (-(196 * (Real.log (Real.log x))^2))
      ∧ 16 * κ * (Real.log (Real.log x))^2 ≤ Real.log x ^ 3
      ∧ 4 * Real.log (Real.log x) ≤ Real.sqrt x := by
  have hlog1 : ∀ᶠ x : ℕ in atTop, (1:ℝ) ≤ Real.log x :=
    (Real.tendsto_log_atTop.comp tendsto_natCast_atTop_atTop).eventually_ge_atTop 1
  have ht1 : ∀ᶠ x : ℕ in atTop, (1:ℝ) ≤ Real.log (Real.log x) :=
    ((Real.tendsto_log_atTop.comp
      (Real.tendsto_log_atTop.comp tendsto_natCast_atTop_atTop))).eventually_ge_atTop 1
  filter_upwards [eventually_ge_atTop 3, eventually_ge_atTop xA, ht1,
    eventually_pow_loglog_le 3 (128*C₄) (show (0:ℝ) < 1/8 by norm_num),
    eventually_mass_margin,
    eventually_pow_loglog_le 2 (16*κ) (show (0:ℝ) < 1 by norm_num),
    eventually_pow_loglog_le 1 8 (show (0:ℝ) < 1 by norm_num),
    hlog1] with x h3 hxA htt hB4 hB5 hB6 hB7 hs1
  refine ⟨h3, hxA, htt, hB4, hB5, ?_, ?_⟩
  · -- (E5): `16 κ t² ≤ s ≤ s³`
    have hsq : (1:ℝ) ≤ Real.log x ^ 2 := by nlinarith
    have : Real.log x ≤ Real.log x ^ 3 := by nlinarith
    linarith
  · -- (E6): `4t ≤ s/2 ≤ √x`, via `ln √x ≤ √x - 1`
    have hx0 : (0:ℝ) < (x:ℝ) := by
      have : (3:ℝ) ≤ (x:ℝ) := by exact_mod_cast h3
      linarith
    have hsq : Real.log (Real.sqrt x) ≤ Real.sqrt x - 1 :=
      Real.log_le_sub_one_of_pos (Real.sqrt_pos.mpr hx0)
    rw [Real.log_sqrt hx0.le] at hsq
    simp only [pow_one] at hB7
    linarith

end Lemma43Limits

set_option maxHeartbeats 400000 in
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

  classical
  obtain ⟨xA, hA'⟩ := hA
  obtain ⟨C₂, hC₂⟩ := oneExtension_sum_le κ hκ
  obtain ⟨x₀, hx₀⟩ := Filter.eventually_atTop.mp (consCount_basket κ (max C₂ 1) xA)
  refine ⟨x₀, fun x hx w L hadm hcard hbudget hspan => ?_⟩
  obtain ⟨h3, hxA, ht1, hB4, hB5, hB6, hB7⟩ := hx₀ x hx
  set C₄ := max C₂ 1 with hC₄def
  have hC₄1 : (1:ℝ) ≤ C₄ := le_max_right _ _
  have hC₄2 : C₂ ≤ C₄ := le_max_left _ _
  set H := wordPointSet w L with hHdef
  have hbonf : ((L:ℝ)+2) ≤ Real.sqrt x → tupleCount H x
      ≤ consCount w L x + (Nat.sqrt x + 1)
        + ∑ m ∈ oneExtensions H, tupleCount (insert m H) x := by
    rw [hHdef]; exact fun hthr => consCount_bonferroni hcard hthr
  have h0 : 0 ∈ H := by rw [hHdef]; exact zero_mem_wordPointSet
  clear_value H
  set s := Real.log x with hsdef
  set t := Real.log s with htdef
  -- basic positivity
  have hx3R : (3:ℝ) ≤ (x:ℝ) := by exact_mod_cast h3
  have hx0 : (0:ℝ) < (x:ℝ) := by linarith
  have hs0 : (0:ℝ) < s := Real.log_pos (by linarith)
  have heven : ∀ h ∈ H, Even h := even_of_admissible h0 hadm
  have hcardR : ((H.card : ℝ)) = (L:ℝ) + 1 := by rw [hcard]; push_cast; ring
  have hLt : (L:ℝ) + 2 ≤ 4 * t := by linarith
  have hL0 : (0:ℝ) ≤ (L:ℝ) := Nat.cast_nonneg _
  have hS0 : (0:ℝ) < singularSeries H := singularSeries_pos hadm
  have hM0 : (0:ℝ) < modelMass H x := by rw [modelMass]; positivity
  -- span control
  have hlog0 : (0:ℝ) ≤ Real.log ((L:ℝ)+2) := Real.log_nonneg (by linarith)
  have hlogL : Real.log ((L:ℝ)+2) ≤ 4*t := by
    have := Real.log_le_sub_one_of_pos (show (0:ℝ) < (L:ℝ)+2 by linarith); linarith
  have hspanS3 : (offsetSpan H : ℝ) ≤ s^3 := by
    have h1 : κ * (L:ℝ) * Real.log ((L:ℝ)+2) ≤ 16 * κ * t^2 := by
      have hL4t : (L:ℝ) ≤ 4*t := by linarith
      have step1 : (L:ℝ) * Real.log ((L:ℝ)+2) ≤ (4*t)*(4*t) :=
        mul_le_mul hL4t hlogL hlog0 (by linarith)
      nlinarith [mul_le_mul_of_nonneg_left step1 (show (0:ℝ) ≤ κ by linarith)]
    linarith
  have hoffH : ∀ h ∈ H, (h:ℝ) ≤ s^3 := by
    intro h hh
    have : (h:ℝ) ≤ (offsetSpan H : ℝ) := by exact_mod_cast Finset.le_sup (f := id) hh
    linarith
  have hcardA : ((H.card:ℝ)) ≤ 4*t := by rw [hcardR]; linarith
  -- HLQuantA lower on H
  have hlow := (hA' x hxA H h0 heven hadm hcardA hoffH).1
  -- the ratio sum
  have hratio : ∑ m ∈ oneExtensions H, singularSeries (insert m H) / singularSeries H
      ≤ 64 * C₄ * t^3 := by
    have hsp : (offsetSpan H : ℝ) ≤ κ * ((H.card : ℝ) - 1) * Real.log ((H.card : ℝ) + 1) := by
      rw [hcardR, show ((L:ℝ)+1)-1 = (L:ℝ) by ring, show ((L:ℝ)+1)+1 = (L:ℝ)+2 by ring]
      exact hspan
    have h := hC₂ H h0 heven hadm hsp
    rw [hcardR, show ((L:ℝ)+1)-1 = (L:ℝ) by ring, show ((L:ℝ)+1)+1 = (L:ℝ)+2 by ring] at h
    have hfac0 : (0:ℝ) ≤ (L:ℝ) * Real.log ((L:ℝ)+2)^2 := by positivity
    have hmono := mul_log_sq_le hL0 ht1 hLt
    calc ∑ m ∈ oneExtensions H, singularSeries (insert m H) / singularSeries H
        ≤ C₂ * (L:ℝ) * Real.log ((L:ℝ)+2)^2 := h
      _ = C₂ * ((L:ℝ) * Real.log ((L:ℝ)+2)^2) := by ring
      _ ≤ C₄ * ((L:ℝ) * Real.log ((L:ℝ)+2)^2) := mul_le_mul_of_nonneg_right hC₄2 hfac0
      _ ≤ C₄ * (64 * t^3) := mul_le_mul_of_nonneg_left hmono (by linarith)
      _ = 64 * C₄ * t^3 := by ring
  -- the extension sum
  have hsum : ∑ m ∈ oneExtensions H, (tupleCount (insert m H) x : ℝ)
      ≤ modelMass H x / 8 := by
    have hstep : ∀ m ∈ oneExtensions H, (tupleCount (insert m H) x : ℝ)
        ≤ 2 * (modelMass H x * (singularSeries (insert m H) / singularSeries H) / s) := by
      intro m hm
      rw [oneExtensions, Finset.mem_filter, Finset.mem_range] at hm
      obtain ⟨hmD, hmeven, hm0, hmH, hmadm⟩ := hm
      have h0' : 0 ∈ insert m H := Finset.mem_insert_of_mem h0
      have heven' : ∀ h ∈ insert m H, Even h :=
        (Finset.forall_mem_insert _ _ _).mpr ⟨hmeven, heven⟩
      have hcard' : ((insert m H).card : ℝ) = (L:ℝ)+2 := by
        rw [Finset.card_insert_of_not_mem hmH, hcard]; push_cast; ring
      have hcardA' : ((insert m H).card:ℝ) ≤ 4*t := by rw [hcard']; linarith
      have hoff' : ∀ h ∈ insert m H, (h:ℝ) ≤ s^3 := by
        intro h hh
        rcases Finset.mem_insert.mp hh with rfl | hh
        · have : (h:ℝ) ≤ (offsetSpan H : ℝ) := by exact_mod_cast hmD.le
          linarith
        · exact hoffH h hh
      have hup := (hA' x hxA (insert m H) h0' heven' hmadm hcardA' hoff').2
      rwa [modelMass_insert hmH (ne_of_gt hS0) (ne_of_gt hs0)] at hup
    calc ∑ m ∈ oneExtensions H, (tupleCount (insert m H) x : ℝ)
        ≤ ∑ m ∈ oneExtensions H, 2 * (modelMass H x
            * (singularSeries (insert m H) / singularSeries H) / s) := Finset.sum_le_sum hstep
      _ = (2 * modelMass H x / s)
            * ∑ m ∈ oneExtensions H, singularSeries (insert m H) / singularSeries H := by
          rw [Finset.mul_sum]
          refine Finset.sum_congr rfl (fun m _ => ?_)
          ring
      _ ≤ (2 * modelMass H x / s) * (64 * C₄ * t^3) := by
          refine mul_le_mul_of_nonneg_left hratio ?_
          positivity
      _ ≤ modelMass H x / 8 := by
          have hkey : (2 * modelMass H x / s) * (64 * C₄ * t^3)
              = (modelMass H x * (128 * C₄ * t^3)) / s := by ring
          rw [hkey, div_le_iff₀ hs0]
          nlinarith [mul_le_mul_of_nonneg_left hB4 hM0.le]
  -- the mass margin
  have hmass : 8 * (Real.sqrt x + 1) ≤ modelMass H x := by
    have hge := modelMass_ge_exp h3 h0 hadm
    rw [hcardR, show ((L:ℝ)+1)-1 = (L:ℝ) by ring, show ((L:ℝ)+1)+1 = (L:ℝ)+2 by ring] at hge
    have hexp : (x:ℝ) * Real.exp (-(196*t^2))
        ≤ (x:ℝ) * Real.exp (-(12*(L:ℝ)*Real.log ((L:ℝ)+2)) - ((L:ℝ)+1)*t) := by
      refine mul_le_mul_of_nonneg_left ?_ hx0.le
      rw [Real.exp_le_exp]
      have := mul_log_le hL0 ht1 hLt
      linarith
    linarith
  -- Bonferroni, cast to ℝ
  have hthr : ((L:ℝ)+2) ≤ Real.sqrt x := by linarith
  have hbonR : (tupleCount H x : ℝ) ≤ (consCount w L x : ℝ) + ((Nat.sqrt x:ℝ) + 1)
      + ∑ m ∈ oneExtensions H, (tupleCount (insert m H) x : ℝ) := by
    have hb := hbonf hthr
    have hc : ((tupleCount H x : ℕ) : ℝ) ≤ ((consCount w L x + (Nat.sqrt x + 1)
        + ∑ m ∈ oneExtensions H, tupleCount (insert m H) x : ℕ) : ℝ) := by exact_mod_cast hb
    push_cast at hc
    linarith
  have hnatsq : (Nat.sqrt x : ℝ) ≤ Real.sqrt x := by
    refine (Real.le_sqrt (by positivity) (by positivity)).mpr ?_
    have h := Nat.sqrt_le' x
    have h' : ((Nat.sqrt x ^ 2 : ℕ):ℝ) ≤ ((x:ℕ):ℝ) := by exact_mod_cast h
    push_cast at h'
    exact h'
  -- FINAL BALANCE
  have hfinal : modelMass H x / 4 ≤ (consCount w L x : ℝ) := by linarith
  refine ⟨hfinal, ?_⟩
  have h1 : (1:ℝ) ≤ (consCount w L x : ℝ) := by
    have := Real.sqrt_nonneg (x:ℝ); linarith
  exact_mod_cast h1

end

end Erdos251
