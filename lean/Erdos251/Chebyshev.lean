import Mathlib

/-!
# Chebyshev upper bound on the n-th prime (item-0003 support)

chain-v1 Lemma 2.1 (repair R1): the trivial `p_n ≤ 2^n` bound does NOT
license the rearrangements the `delta`-series identities need. This file
proves a genuine sub-geometric bound `q n ≤ (n+2)^2` (all `n`) via the
central binomial coefficient (Chebyshev's method). Mathlib packages lower
bounds on the n-th prime and upper bounds on `π` -- both the wrong
direction -- so the Chebyshev lower bound on `π` is built here from
`Nat.four_pow_lt_mul_centralBinom` and central-binomial factorization.

The single downstream consumer is `Erdos251.summable_erdosSeries`.
-/

namespace Erdos251

open Nat Finset

/-- Central binomial factorization bound: `C(2n,n) ≤ (2n)^{π(2n)}`. Each
prime power `p^{v_p}` dividing `C(2n,n)` is `≤ 2n`
(`Nat.pow_factorization_choose_le`), and there are `π(2n)` such primes. -/
theorem centralBinom_le (n : ℕ) (hn : 1 ≤ n) :
    Nat.centralBinom n ≤ (2 * n) ^ Nat.primeCounting (2 * n) := by
  have h2n : 0 < 2 * n := by omega
  have hprod : ∏ p ∈ Nat.primesBelow (2 * n + 1),
          p ^ (Nat.centralBinom n).factorization p = Nat.centralBinom n := by
    conv_rhs => rw [← Nat.prod_pow_factorization_centralBinom n]
    apply Finset.prod_subset
    · intro p hp
      exact Finset.mem_range.mpr (Nat.mem_primesBelow.mp hp).1
    · intro p hp hpP
      have hnp : ¬ p.Prime := fun hpr =>
        hpP (Nat.mem_primesBelow.mpr ⟨Finset.mem_range.mp hp, hpr⟩)
      rw [Nat.factorization_eq_zero_of_non_prime _ hnp, pow_zero]
  rw [← hprod]
  calc ∏ p ∈ Nat.primesBelow (2 * n + 1),
          p ^ (Nat.centralBinom n).factorization p
      ≤ ∏ _p ∈ Nat.primesBelow (2 * n + 1), (2 * n) := by
        apply Finset.prod_le_prod'
        intro p _
        rw [Nat.centralBinom_eq_two_mul_choose]
        exact Nat.pow_factorization_choose_le h2n
    _ = (2 * n) ^ (Nat.primesBelow (2 * n + 1)).card := by rw [Finset.prod_const]
    _ = (2 * n) ^ Nat.primeCounting (2 * n) := by
        rw [Nat.primesBelow_card_eq_primeCounting']; rfl

/-- Chebyshev lower bound on `π`: for `n ≥ 4`,
`2n < clog₂(2n) · (π(2n) + 1)`. Combines `centralBinom_le` with the
lower bound `4^n < n · C(2n,n)` and `2n ≤ 2^{clog₂(2n)}`. -/
theorem two_mul_lt_clog_mul (n : ℕ) (hn : 4 ≤ n) :
    2 * n < Nat.clog 2 (2 * n) * (Nat.primeCounting (2 * n) + 1) := by
  have hcb : Nat.centralBinom n ≤ (2 * n) ^ Nat.primeCounting (2 * n) :=
    centralBinom_le n (by omega)
  have h4 : 4 ^ n < n * Nat.centralBinom n := Nat.four_pow_lt_mul_centralBinom n hn
  have hstep : (2 : ℕ) ^ (2 * n) < (2 * n) ^ (Nat.primeCounting (2 * n) + 1) := by
    have h4eq : (4 : ℕ) ^ n = 2 ^ (2 * n) := by
      rw [show (4 : ℕ) = 2 ^ 2 from rfl, ← pow_mul]
    rw [← h4eq]
    calc 4 ^ n < n * Nat.centralBinom n := h4
      _ ≤ n * (2 * n) ^ Nat.primeCounting (2 * n) := Nat.mul_le_mul (le_refl n) hcb
      _ ≤ (2 * n) * (2 * n) ^ Nat.primeCounting (2 * n) :=
            Nat.mul_le_mul (by omega) (le_refl _)
      _ = (2 * n) ^ (Nat.primeCounting (2 * n) + 1) := by rw [pow_succ']
  have hle : (2 * n) ^ (Nat.primeCounting (2 * n) + 1)
      ≤ 2 ^ (Nat.clog 2 (2 * n) * (Nat.primeCounting (2 * n) + 1)) := by
    calc (2 * n) ^ (Nat.primeCounting (2 * n) + 1)
        ≤ (2 ^ Nat.clog 2 (2 * n)) ^ (Nat.primeCounting (2 * n) + 1) :=
          Nat.pow_le_pow_left (Nat.le_pow_clog (by norm_num) _) _
      _ = 2 ^ (Nat.clog 2 (2 * n) * (Nat.primeCounting (2 * n) + 1)) := by rw [← pow_mul]
  have hlt : (2 : ℕ) ^ (2 * n)
      < 2 ^ (Nat.clog 2 (2 * n) * (Nat.primeCounting (2 * n) + 1)) :=
    lt_of_lt_of_le hstep hle
  exact (Nat.pow_lt_pow_iff_right (by norm_num)).mp hlt

/-- `(N+2)^2 ≤ 2^{N+1}` for `N ≥ 5` (polynomial beats the exponent). -/
theorem sq_le_two_pow {N : ℕ} (hN : 5 ≤ N) : (N + 2) ^ 2 ≤ 2 ^ (N + 1) := by
  induction N, hN using Nat.le_induction with
  | base => norm_num
  | succ N hN ih =>
    have hstep : (N + 3) ^ 2 ≤ 2 * (N + 2) ^ 2 := by nlinarith [hN]
    calc (N + 1 + 2) ^ 2 = (N + 3) ^ 2 := by ring
      _ ≤ 2 * (N + 2) ^ 2 := hstep
      _ ≤ 2 * 2 ^ (N + 1) := by omega
      _ = 2 ^ (N + 1 + 1) := (pow_succ' 2 (N + 1)).symm

/-- Eventual polynomial bound on the n-th prime (chain-v1 Lemma 2.1,
repair R1): `nth Prime N < (N+2)^2` for `N ≥ 5`. The genuine Chebyshev
content the trivial `p_n ≤ 2^n` bound cannot supply. -/
theorem nth_prime_lt_sq {N : ℕ} (hN : 5 ≤ N) :
    Nat.nth Nat.Prime N < (N + 2) ^ 2 := by
  set n := ((N + 2) ^ 2 - 1) / 2 with hn_def
  -- basic size facts about 2n
  have hsq_ge : 9 ≤ (N + 2) ^ 2 := by nlinarith [hN]
  have h2n_hi : 2 * n + 1 ≤ (N + 2) ^ 2 := by
    rw [hn_def]; omega
  have hn4 : 4 ≤ n := by rw [hn_def]; omega
  -- Chebyshev bound at n
  have hcheb := two_mul_lt_clog_mul n hn4
  -- clog 2 (2n) ≤ N + 1
  have hclog : Nat.clog 2 (2 * n) ≤ N + 1 := by
    have h1 : Nat.clog 2 (2 * n) ≤ Nat.clog 2 ((N + 2) ^ 2) :=
      Nat.clog_mono_right 2 (by omega)
    have h2 : Nat.clog 2 ((N + 2) ^ 2) ≤ N + 1 :=
      (Nat.le_pow_iff_clog_le (by norm_num)).mp (sq_le_two_pow hN)
    omega
  -- π(2n) > N
  have hcount : N < Nat.primeCounting (2 * n) := by
    by_contra hcon
    push_neg at hcon
    have hb : 2 * n < (N + 1) * (Nat.primeCounting (2 * n) + 1) :=
      lt_of_lt_of_le hcheb (Nat.mul_le_mul hclog (le_refl _))
    have hb2 : (N + 1) * (Nat.primeCounting (2 * n) + 1) ≤ (N + 1) * (N + 1) :=
      Nat.mul_le_mul (le_refl _) (by omega)
    have hlt2n : 2 * n < (N + 1) * (N + 1) := lt_of_lt_of_le hb hb2
    have hlo : (N + 2) ^ 2 ≤ 2 * n + 2 := by rw [hn_def]; omega
    nlinarith [hlt2n, hlo]
  -- primeCounting (2n) = count Prime (2n+1); lift by monotonicity to (N+2)^2
  have hcount' : N < Nat.count Nat.Prime ((N + 2) ^ 2) := by
    have hmono : Nat.count Nat.Prime (2 * n + 1) ≤ Nat.count Nat.Prime ((N + 2) ^ 2) :=
      Nat.count_monotone Nat.Prime h2n_hi
    have : Nat.primeCounting (2 * n) = Nat.count Nat.Prime (2 * n + 1) := rfl
    omega
  exact Nat.nth_lt_of_lt_count hcount'

end Erdos251
