import Mathlib
import Erdos251.Basic
import Erdos251.Hypotheses
import Erdos251.Counting.Words
import Erdos251.Counting.ConsecTransfer

/-!
# Section 5: the deletion construction

The section-5 constants (`cK`, `cJ`, `cL`, `cI`, `tailBudget`), the two
word enumerations `cElem` / `cElem'` (the deletion IS the `if`), the
constants layer around the `Nat.ceil . logb 2` idiom, the property lemmata
5(i)-5(iv), the chain `constr_consCount_pos` down to `N_cons >= 1`, and the
four review-verified smoke tests.

RELOCATION ONLY (item-0016). The body below is byte-identical to
`Erdos251/Counting.lean` lines 1827-2756 at commit
`6683ee0f009baeb5dd6e759f265544e7f91af23d`,
sha256 `099b2988a1da9e3322f915229c01acd298979021ab87d74c90076f81124ca97c`.
No statement, docstring, proof or name was changed. Provenance, the index
conventions, the traceability table and the module map live in the umbrella
`Erdos251/Counting.lean`.
-/

namespace Erdos251

noncomputable section

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

/-! ### Glue (PROVED, flagged): `q_eq_of_count` relocated

Moved UP to the Lemma 4.3 proof-layer helpers (item-0015 s5) with statement,
docstring and proof unchanged: `consCount_bonferroni` is its first consumer and
Lean requires it declared earlier. It remains the project's ONLY glue proof, as
the traceability table records; the smoke tests below still consume it. Same
discipline as the ANN-38/39/40 relocation note above. -/

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
  obtain ⟨C₁, hC₁, hspan⟩ := cspan_le
  obtain ⟨x₃, h43⟩ := consCount_lower_bound hA C₁ hC₁
  obtain ⟨x₄, hbud⟩ := cbudget hCg
  refine ⟨max x₃ x₄, fun x hx => ?_⟩
  -- `cbudget` bundles 4.3's window clause `L + 1 ≤ 4 lnln x - 1` verbatim
  obtain ⟨hJ, hK, -, -, hbudget, -, -, -⟩ := hbud x (le_trans (le_max_right _ _) hx)
  obtain ⟨⟨hadm, hcard⟩, ⟨hadm', hcard'⟩⟩ := cword_admissible (cJ Cg x) (cK Cg x) hJ hK
  -- 5(iii)'s last two clauses ARE 4.3's span hypothesis at `κ := C₁`
  obtain ⟨-, -, hsp, hsp'⟩ := hspan (cJ Cg x) (cK Cg x) hJ hK
  have hx3 : x₃ ≤ x := le_trans (le_max_left _ _) hx
  exact ⟨(h43 x hx3 _ _ hadm hcard hbudget hsp).2,
    (h43 x hx3 _ _ hadm' hcard' hbudget hsp').2⟩

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
