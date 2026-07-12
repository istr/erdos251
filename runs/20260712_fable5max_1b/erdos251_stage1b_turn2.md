# Erdős #251 — Payload 1b (briefed), Turn 2: Primary objective delivered

## 0. Provenance and execution notes

- **sha256(1b_briefed.md)** = `5f6abc6f77e401ae040a60945d6b2b7060fd18913e8181edeea2b4a21394b4e4`
- sha256(transcript-turn-1.md) = `1c5a5ecb4899e4bb13210134f37be5038500369840ff088ddc73a1896f1d2a75` (continuation provenance)
- Web/research: **disabled**. Literature-dependent statements are marked `[CLASSICAL]` (elementary, proof sketch inline) or `[UNVERIFIED-LIT]` (briefing-carried, not load-bearing). No citations invented.
- Turn-1 reasoning was interrupted at the final verification of the lattice congruence `b(δ_{n+J} − δ_{m+J}) ∈ 2^{J+1}ℤ`. That verification is closed below (Claim **CL3**); the remainder of this document assembles the construction the turn-1 reasoning had already converged on (deletion fork with ρ = γ/4, Cramér clause HL-B, first-order Bonferroni). **Nothing was re-derived from scratch.**
- Status of the PRIMARY objective: **complete** — a precise `HL_quant ⇒ FM ⇒ (S irrational)` chain, with every implication proved (conditionally on HL_quant, which is stated exactly), structured along the requested Lean skeleton.

## 1. Executive summary

Assume S = Σ p_n/2^n = a/(2^s b) with b odd. Then bδ_n ∈ 2ℤ for n ≥ s+1, where δ_n = Σ_{j≥1} g_{n+j}2^{−j} (**CL2**). Two sites n, m ≥ s+1 whose gap words share a length-J prefix satisfy b(δ_{n+J} − δ_{m+J}) ∈ 2^{J+1}ℤ (**CL3**). The **fork–merge hypothesis (FM)** supplies site pairs whose gap words agree except on a 2-entry middle block with differences (+γ, −γ), followed by a length-K common suffix, with the end-tails ≤ 2^K and (γ+4)/2^J → 0. For such a pair, the prefix congruence forces exact δ-equality at the fork; the middle then forces |δ_{n+L} − δ_{m+L}| = γ·2^K ≥ 2^{K+1}, contradicting the end-tail bound (**CL6**). FM itself is produced by **HL_quant** = (A) a uniform quantitative Hardy–Littlewood tuple asymptotic for k ≤ 4 lnln x points, shifts ≤ (ln x)³, polylog error savings, plus (B) a Cramér–Granville gap clause g_ν ≤ C_g(ln p_ν)². Clause B empties the "bad-tail" set that killed all turn-1 conditioning attempts; the fork pairs are built by **deleting one of two adjacent primes** from a window of L+2 consecutive primes just above L+3 — an automatically admissible pair of consecutive-gap words within the lnln x budget (**CL12, CL14**). Clause B is provably not a polylog-error consequence of clause A (**CL13**), so the package genuinely has two axioms.

## 2. Notation and conventions

- p_n = n-th prime (p_1 = 2, 1-indexed in the mathematics); g_n = p_{n+1} − p_n. ℓ := ln x (natural logs throughout; "polylog" means ℓ^{O(1)}).
- S := Σ_{n≥1} p_n/2^n (converges: p_n ≤ 2^n by Bertrand). The Lean target sum Σ_{n≥0} (nth prime, 0-indexed)/2^n equals 2S; Irrational(2S) ⇔ Irrational(S).
- u_n := Σ_{k≥1} p_{n+k}/2^k = 2^n(S − Σ_{j≤n} p_j 2^{−j});  δ_n := u_n − p_{n+1} = Σ_{j≥1} g_{n+j}·2^{−j}.
- Rationality normal form: S = a/(2^s b), a ∈ ℤ, s ∈ ℕ, b odd ≥ 1.
- Gap word of length L at site n: (g_{n+1}, …, g_{n+L}); it is *consecutively realized* iff these are the actual consecutive prime gaps, i.e. p_{n+1+i} = p_{n+1} + h_i with h_i = w_1 + … + w_i and no other primes in (p_{n+1}, p_{n+1}+h_L).
- For a word w of length L: offset tuple H(w) := {0, h_1, …, h_L} (L+1 points). Admissible = misses ≥ 1 residue class mod every prime. Singular series 𝔖(H) := Π_p (1 − ν_H(p)/p)(1 − 1/p)^{−|H|}, ν_H(p) := #{h mod p : h ∈ H}.
- Briefing-fact usage tags: [B-I.1] Tao thread, [B-I.2] ScPu11, [B-I.3] adversarial telescoping, [B-II.X] stage-1a mechanism X, [B-III.1] primorial, [B-III.2] parity, [B-III.3] countermodel, [B-III.4] statistics no-go, [B-IV] empirics. Every use is marked inline and collected in §7.

## 3. CLAIMS ledger (contract item 1)

| id | statement (short form) | status | deps | conf |
|----|------------------------|--------|------|------|
| CL0 | Identities: δ_n = Σ_{j≥1} g_{n+j}2^{−j}; δ_{n+1} = 2δ_n − g_{n+1}; δ_n ≥ 2 (n ≥ 1); convergence via p_n ≤ 2^n. | proved | — | 1.00 |
| CL1 | `delta_block`: δ_n = Σ_{i=1}^{T} 2^{−i} g_{n+i} + 2^{−T} δ_{n+T} for all n, T. | proved | CL0 | 1.00 |
| CL2 | `rational_delta_eventually_lattice`: S = a/(2^s b), b odd ⇒ bδ_n ∈ ℤ (n ≥ s) and bδ_n ∈ 2ℤ (n ≥ s+1). [B-III.2 re-proved] | proved | CL0 | 1.00 |
| CL3 | `repeated_block_quantization` (the step turn-1 stopped at): n, m ≥ s+1, common gap prefix of length J ⇒ b(δ_{n+J} − δ_{m+J}) ∈ 2^{J+1}ℤ. | proved | CL1, CL2 | 1.00 |
| CL4 | Quantization dichotomy: CL3 + \|δ_{n+J} − δ_{m+J}\| < 2^{J+1}/b ⇒ δ_{n+J} = δ_{m+J}. | proved | CL3 | 1.00 |
| CL5 | FM statement (b-free, 2-entry middle block (+γ, −γ)); see §5. | definition | — | — |
| CL6 | `fork_merge_contradiction` / `erdos_251_of_small_tail_fork_merge`: FM ⇒ S irrational. | proved | CL1–CL4 | 0.98 |
| CL7 | HL_quant statement = clause A (uniform tuple asymptotic) + clause B (Cramér–Granville gap clause); see §4. [B-I.1 shape] | hypothesis (open conjecture) | — | — |
| CL-Ch | Chebyshev package: Π_{p≤n} p ≤ 4^n; π(x) ≥ x/(2ℓ) and π(x) ≤ 3x/ℓ (x ≥ x₁); p_k ≤ C_P k ln(k+2); Mertens Σ_{p≤y}1/p = lnln y + M + o(1), Π_{p≤y} p/(p−1) ≤ C ln y. `[CLASSICAL]`, sketches inline. | proved (classical) | — | 0.95 |
| CL8 | 𝔖(H) ≥ e^{−C_𝔖 k} for H a translate of k+1 primes all > k+2 (our tuples). | proved | CL-Ch | 0.92 |
| CL9 | One-point-extension sum: Σ_{t ∈ I} 𝔖(H∪{t})/𝔖(H) ≤ C₂ k(ln k)², I = even t in (0, span)∖H. Key: r_p < 1 for non-colliding p > 2(k+1). | proved | CL-Ch | 0.88 |
| CL10 | Consecutive-count lower bound: HL-A ⇒ N_cons(w; x) ≥ ¼𝔖(H(w)) x/ℓ^{L+1} ≥ 1 for the §6.5 words (Bonferroni r = 1). | proved conditional on HL-A | CL7A, CL8, CL9 | 0.90 |
| CL11 | Tail bound: HL-B ⇒ δ_ν ≤ 3C_g(ln p_ν)² for ν ≥ ν₁. (Bertrand + (a+b)² ≤ 2a²+2b².) | proved conditional on HL-B | CL7B | 0.95 |
| CL12 | Deletion construction: for each large x an admissible fork pair (w, w′) with parameters J, K, L, γ; prefix/middle/suffix structure exact; span ≤ C₁L ln L; both tuples admissible. [B-III.1 respected] | proved | CL-Ch | 0.95 |
| CL13 | Independence: clause B is not derivable from clause A at polylog error savings (needs ≈ e^{−c(ln x)^{3/2}} savings). | sketch | CL7 | 0.70 |
| CL14 | `hl_quant_implies_fm`: HL_quant ⇒ FM (parameter bookkeeping in §6.6). | proved conditional on HL_quant | CL10, CL11, CL12 | 0.90 |
| CL15 | `erdos_251_of_hl_quant`: HL_quant ⇒ S irrational ⇒ Lean target irrational. | proved conditional | CL14, CL6 | 0.90 |
| FS1 | Family-pigeonhole δ-conditioning (turn-1): dies by family tax e^{L lnln L} at the triple-log margin. | false-start | — | — |
| FS2 | Cauchy–Schwarz second moment on gaps: needs Σg² ≤ x^{1+o(1)} (RH-grade), still insufficient. | false-start | — | — |
| FS3 | Statistical (counting) version of the gap clause: same family tax. | false-start | — | — |
| FS4 | "One deletion = one differing gap": wrong — deletion yields two adjacent differing entries (+γ, −γ); repaired by the ρ = γ/4 middle block. | false-start (repaired) | — | — |
| FS5 | Prescribing the ~log₂x tail gaps exactly: entropy/birthday ceiling ≈ 2ℓ/(ln2·lnℓ); impossible. Resolved by clause B (BAD = ∅). | false-start (resolved) | — | — |

## 4. HL_quant, stated in full (contract item 2)

**Clause A (uniform quantitative Hardy–Littlewood tuple asymptotic).**
There exist x_A and, for some fixed A₀ ≥ 1, a constant C_A such that for all x ≥ x_A and **every** admissible tuple H = {0 = h_0 < h_1 < … < h_k} of even integers with

- (size budget) k + 1 ≤ 4 lnln x, and
- (shift budget) h_k ≤ (ln x)³,

the count π_H(x) := #{p ≤ x prime : p + h_i prime for all i} satisfies

  π_H(x) = 𝔖(H) · x/ℓ^{k+1} · (1 + E_H(x)), |E_H(x)| ≤ C_A ℓ^{−A₀},

uniformly in H within the budgets. (Any fixed A₀ ≥ 1 suffices for everything below; only two-sided bounds within a factor 2 are ever spent.) [B-I.1: window shape "k ≤ C lnln x, shifts ≤ (log x)³, polylog savings" — our C = 4.]

**Clause B (Cramér–Granville gap clause).**
There exist C_g ≥ 1 and ν₀ such that g_ν ≤ C_g (ln p_ν)² for all ν ≥ ν₀.

**Package.** HL_quant := (A) ∧ (B). Clause B is consistent with, and heuristically implied by, strongly uniform HL statistics (gap-λ·ln events with frequency e^{−λ}); but **CL13** shows it cannot be *derived* from clause A at polylog savings, so it is an independent axiom of the package. [B-III.4: some prime-specific input beyond counting statistics is unavoidable; clauses A and B are exactly the prime-specific inputs used.]

**Uniformity-spend register (every place HL_quant is used):**

| spend | clause | where | what is spent |
|-------|--------|-------|----------------|
| U1 | A | CL10, lower bound on π_{H(w)}(x), π_{H(w′)}(x) | tuples of size L+1 ≤ 3 lnln x; shifts ≤ span ≤ C₁L ln L ≪ ℓ ≪ ℓ³; relative error ≤ ½ |
| U2 | A | CL10, Bonferroni subtraction terms π_{H(w)∪{t}}(x) | tuples of size L+2 ≤ 4 lnln x (this is why the budget constant is 4, not 3); ≤ span/2 simultaneous tuples; upper bound within factor 2 |
| U3 | A | CL10, restriction to p ∈ (√x, x] | π_H(√x) ≤ √x is trivial; no HL input at √x needed |
| U4 | B | CL11 → FM-1 | pointwise gap bound at all ν ≥ ν₀; feeds δ_ν ≤ 3C_g(ln p_ν)², i.e., H(x) := 3C_g(ln 2x)² |
| U5 | A+B | CL14 | applied along any sequence x_r → ∞; nothing else |

No other step touches HL_quant; CL0–CL6 are unconditional.

## 5. FM — the fork–merge hypothesis (b-free final form; CL5)

**FM.** There exist sequences (n_r, m_r, J_r, K_r, γ_r, H_r)_{r≥1}, with L_r := J_r + 2 + K_r, such that for every r:

- (FM-0) γ_r ∈ ℤ, γ_r ≥ 2;
- (FM-P) g_{n_r+i} = g_{m_r+i} for 1 ≤ i ≤ J_r  (common prefix);
- (FM-F) g_{n_r+J_r+1} − g_{m_r+J_r+1} = +γ_r and g_{n_r+J_r+2} − g_{m_r+J_r+2} = −γ_r  (middle block);
- (FM-S) g_{n_r+i} = g_{m_r+i} for J_r+3 ≤ i ≤ L_r  (common suffix, length K_r);
- (FM-1) max(δ_{n_r+L_r}, δ_{m_r+L_r}) ≤ H_r ≤ 2^{K_r};

and moreover

- (FM-2) (γ_r + 4)/2^{J_r} → 0 as r → ∞;
- (FM-3) min(n_r, m_r) → ∞.

Design notes. (i) This is the deletion-fork variant of briefing mechanism G [B-II.G]: the middle block has length 2 with antisymmetric differences; its weighted value is ρ = γ/2 − γ/4 = γ/4 ≠ 0, which is what the contradiction amplifies. The variant is proved sound from scratch below (CL6); briefing G's proof is not cited as an ingredient. (ii) No strict-positivity/anti-concentration clause on δ is needed — the mechanism is immune to the exact-locking countermodel [B-III.3], exactly as the briefing predicted for fork–merge. (iii) b enters nowhere: (FM-2) is the b-free prefix-margin condition; for any fixed odd b it eventually yields 2^{J_r+1} > b(γ_r+4)/4. (iv) Windows at n_r and m_r may overlap or nest; no disjointness is used anywhere.

## 6. Main writeup: the proofs (contract item 3)

### 6.1 Elementary lattice layer (CL0–CL4) — unconditional

**CL0.** Convergence: p_n ≤ 2^n (Bertrand, induction from p_1 = 2), so Σ p_n 2^{−n} and all tails converge absolutely. From u_n = Σ_{k≥1} p_{n+k}2^{−k} and Σ_{k≥1}2^{−k} = 1:
δ_n = u_n − p_{n+1} = Σ_{k≥1}(p_{n+k} − p_{n+1})2^{−k} = Σ_{k≥2} 2^{−k} Σ_{j=1}^{k−1} g_{n+j} = Σ_{j≥1} g_{n+j} Σ_{k≥j+1} 2^{−k} = Σ_{j≥1} g_{n+j} 2^{−j}.
Recurrence: δ_{n+1} = Σ_{j≥1} g_{n+1+j}2^{−j} = 2(δ_n − g_{n+1}/2) = 2δ_n − g_{n+1}. Positivity: for n ≥ 1 and j ≥ 1, n+j ≥ 2 so g_{n+j} ≥ 2, hence δ_n ≥ 2. ∎

**CL1 (delta_block).** Truncate the series: δ_n = Σ_{i=1}^{T} 2^{−i} g_{n+i} + Σ_{j>T} 2^{−j} g_{n+j} and reindex the tail with j = T + i′ to get 2^{−T} δ_{n+T}. ∎

**CL2 (rational_delta_eventually_lattice).** Let S = a/(2^s b), b odd. For n ≥ s: 2^n b S = 2^{n−s} a ∈ ℤ, and b·Σ_{j≤n} p_j 2^{n−j} ∈ ℤ, so b u_n ∈ ℤ, so b δ_n = b u_n − b p_{n+1} ∈ ℤ. Parity [B-III.2, re-proved]: for n ≥ s, b δ_{n+1} = 2·(bδ_n) − b·g_{n+1}; g_{n+1} = p_{n+2} − p_{n+1} is a difference of odd primes (n+1 ≥ 2), hence even; b odd ⇒ b g_{n+1} even; 2(bδ_n) even. So bδ_{n+1} ∈ 2ℤ for all n ≥ s, i.e., bδ_m ∈ 2ℤ for all m ≥ s+1. ∎

**CL3 (repeated_block_quantization) — the verification turn-1 stopped at.** Let n, m ≥ s+1 with g_{n+i} = g_{m+i} for 1 ≤ i ≤ J. By CL1 applied at n and at m and subtracting, the identical prefix sums cancel:
δ_n − δ_m = 2^{−J}(δ_{n+J} − δ_{m+J}),  hence  b(δ_{n+J} − δ_{m+J}) = 2^{J} · (bδ_n − bδ_m).
By CL2, bδ_n, bδ_m ∈ 2ℤ (here n, m ≥ s+1 is used), so bδ_n − bδ_m ∈ 2ℤ and b(δ_{n+J} − δ_{m+J}) ∈ 2^{J+1}ℤ. ∎
(Remark: bδ_{n+J}, bδ_{m+J} are individually integers by CL2 since n+J, m+J ≥ s; the congruence above is the factor-2-sharpened threshold [B-III.2].)

**CL4 (dichotomy).** If additionally |δ_{n+J} − δ_{m+J}| < 2^{J+1}/b, then |b(δ_{n+J} − δ_{m+J})| < 2^{J+1}, and the only element of 2^{J+1}ℤ in (−2^{J+1}, 2^{J+1}) is 0. So δ_{n+J} = δ_{m+J}. ∎

### 6.2 CL6: FM ⇒ S irrational (fork_merge_contradiction)

Assume FM and suppose S = a/(2^s b), b odd. By (FM-3) and (FM-2) choose r with min(n_r, m_r) ≥ s+1 and (γ_r+4)/2^{J_r} < 8/b. Write n = n_r, m = m_r, J = J_r, K = K_r, γ = γ_r, L = J+2+K, H = H_r.

1. **End-tail closeness.** By (FM-1), δ_{n+L}, δ_{m+L} ∈ [2, H], so |δ_{n+L} − δ_{m+L}| ≤ H − 2 < H ≤ 2^K.  (strict)
2. **Fork decomposition.** CL1 at depth K+2 from positions n+J and m+J, subtracting and using (FM-F), (FM-S):
   δ_{n+J} − δ_{m+J} = 2^{−1}(+γ) + 2^{−2}(−γ) + 0 + 2^{−(K+2)}(δ_{n+L} − δ_{m+L}) = γ/4 + 2^{−(K+2)}(δ_{n+L} − δ_{m+L}).
3. **Fork closeness.** |δ_{n+J} − δ_{m+J}| < γ/4 + 2^{−(K+2)}·2^{K} = γ/4 + 1/4 = (γ+1)/4 < (γ+4)/4.
4. **Lattice lock.** By CL3 (n, m ≥ s+1, prefix (FM-P)): b(δ_{n+J} − δ_{m+J}) ∈ 2^{J+1}ℤ, and |b(δ_{n+J} − δ_{m+J})| < b(γ+4)/4 < 2^{J+1} by the choice of r. By CL4-logic the value is 0: δ_{n+J} = δ_{m+J}.
5. **Contradiction.** Step 2 with left side 0 gives δ_{n+L} − δ_{m+L} = −γ·2^{K}, so γ·2^{K} = |δ_{n+L} − δ_{m+L}| < H ≤ 2^K (step 1), i.e., γ < 1 — contradicting (FM-0) γ ≥ 2. ∎

Hence no representation S = a/(2^s b) exists: **S is irrational**, and so is the Lean sum 2S. (This proof of the top implication is packaged as `erdos_251_of_small_tail_fork_merge` in §8.)

### 6.3 Classical toolbox (CL-Ch) — `[CLASSICAL]`, sketches inline

(i) Π_{p≤n} p ≤ 4^n: induction via Π_{m+1<p≤2m+1} p | C(2m+1, m) ≤ 4^m. (ii) From 4^n/(2n+1) ≤ C(2n, n) = Π p^{e_p}, e_p ≤ ⌊log_p 2n⌋: 4^n/(2n+1) ≤ (2n)^{π(2n)}, so π(2n) ≥ n ln4/ln(2n) − 1, giving π(x) ≥ x/(2ℓ) for x ≥ x₁. (iii) π(x) ≤ 3x/ℓ for x ≥ x₁ from θ(x) ≤ x ln 4 (by (i)) and π(x) ≤ θ(x)/ln√x + √x. (iv) p_k ≤ C_P k ln(k+2): from (ii), k = π(p_k) ≥ p_k/(2 ln p_k); bootstrap p_k ≤ k² (large k) to get ln p_k ≤ 2 ln k, hence p_k ≤ 4 k ln k for k ≥ k₀; enlarge C_P for small k. (v) Mertens: Σ_{p≤y} 1/p = lnln y + M + o(1) and Π_{p≤y} p/(p−1) ≤ C ln y — classical elementary (partial summation over (i)-grade Chebyshev bounds). Constants are never optimized below; only existence of absolute constants is used.

### 6.4 Counting layer conditional on HL-A (CL8, CL9, CL10)

Throughout, H = H(w) = {0, h_1, …, h_L} is a translate of a set Q of k+1 = L+1 primes, all > k+2, with span D := h_L ≤ C₁ k ln k (this is the only type of tuple we ever feed to HL-A; see §6.5).

**CL8 (singular-series lower bound).** For p ≤ k+2: every element of Q is a prime > p, so 0 ∉ H mod p... more precisely all points ≢ −(translate) ≡ non-zero pattern; what matters: ν_H(p) ≤ p − 1, so the factor is ≥ (1/p)·(1−1/p)^{−(k+1)} ≥ 1/p; the product over p ≤ k+2 is ≥ e^{−θ(k+2)} ≥ 4^{−(k+2)} by CL-Ch(i). For k+2 < p ≤ 2(k+1): factor ≥ (1 − ν/p) ≥ 1/p ≥ 1/(2k+2); there are ≤ π(2k+2) ≤ 3(2k+2)/ln(2k+2) such primes (CL-Ch iii), so this block is ≥ (2k+2)^{−3(2k+2)/ln(2k+2)} = e^{−3(2k+2)} = e^{−O(k)}. For 2(k+1) < p ≤ D: (1 − ν/p) ≥ (1 − (k+1)/p) ≥ e^{−2(k+1)/p} and (1−1/p)^{−(k+1)} ≥ e^{(k+1)/p}, so the factor is ≥ e^{−(k+1)/p}; Σ_{2(k+1)<p≤D}(k+1)/p = (k+1)(lnln D − lnln 2(k+1) + o(1)) = o(k) since D ≤ C₁k ln k (Mertens). For p > D: ν_H(p) = k+1 (all offsets distinct mod p), and (1−(k+1)/p)(1−1/p)^{−(k+1)} ≥ e^{−(k+1)²/p²·C}; Σ_{p>D}(k+1)²/p² ≤ C(k+1)²/(D ln D) = O(k/ln²k) = o(k). Multiplying: 𝔖(H) ≥ e^{−C_𝔖 k} for an absolute C_𝔖. ∎

**CL9 (one-point extension sum).** For even t ∈ (0, D)∖H with H∪{t} admissible, let R_t := 𝔖(H∪{t})/𝔖(H) = Π_p r_p with r_p = [(p − ν_{H∪{t}}(p))/(p − ν_H(p))]·[p/(p−1)]. Two cases per prime: (collision, p | Π_{h∈H}(t−h)) ν_{H∪{t}} = ν_H and r_p = p/(p−1); (no collision) ν_{H∪{t}} = ν_H + 1 and r_p = (1 − 1/(p−ν_H))(1 + 1/(p−1)). Since ν_H ≥ 1, 1/(p−ν_H) ≥ 1/(p−1), so in the no-collision case r_p ≤ (1 − 1/(p−1))(1 + 1/(p−1)) = 1 − (p−1)^{−2} **< 1**. Hence
R_t ≤ Π_{p ≤ 2(k+1)} p/(p−1) · Π_{p > 2(k+1), p | Δ_t} p/(p−1),  Δ_t := Π_{h∈H} |t−h| ≤ D^{k+1}.
First product ≤ C ln k (Mertens). Second: each factor ≤ 1 + 1/(2k+1); the number of prime divisors > 2(k+1) of Δ_t is ≤ ln Δ_t/ln(2k+2) ≤ (k+1)·ln D/ln(2k) ≤ 3k for large k (D ≤ C₁k ln k), so the product is ≤ (1+1/(2k+1))^{3k} ≤ e². Therefore R_t ≤ C_R ln k, and summing over the ≤ D/2 ≤ C₁k ln k/2 admissible even t:
Σ_{t∈I} R_t ≤ C₂ k (ln k)². ∎

**CL10 (consecutive realizations from HL-A; Bonferroni r = 1).** Let w be a word as in §6.5 (length L, offsets H(w), span D ≤ C₁L ln L ≪ ℓ). For a prime p > D, the word w is consecutively realized starting at p iff (a) p + h is prime for all h ∈ H(w), and (b) p + t is composite for every even t ∈ (0, D)∖H(w) — odd t are automatic since p + t is even > 2. Hence, counting sites with p = p_{n+1} ∈ (√x, x] (note √x > D for large x):
N_cons(w; x) ≥ [π_{H(w)}(x) − π_{H(w)}(√x)] − Σ_{t∈I} #{√x < p ≤ x : p+h prime ∀h ∈ H(w)∪{t}}.
For inadmissible H(w)∪{t}: some prime q ≤ L+2 covers all residues, so q divides one of the p+h; since p > √x > q, that p+h is composite — the count is **0**. For admissible H(w)∪{t}: size L+2 ≤ 4 lnln x, shifts ≤ D ≤ ℓ³ — within HL-A's budget (spend U2) — so the count is ≤ 2𝔖(H(w)∪{t}) x/ℓ^{L+2}. Summing with CL9:
Σ_{t∈I} (…) ≤ 2𝔖(H(w)) x/ℓ^{L+1} · (Σ_t R_t)/ℓ ≤ 2𝔖(H(w)) x/ℓ^{L+1} · C₂L(ln L)²/ℓ = 𝔖(H(w)) x/ℓ^{L+1} · o(1),
since L ≍ lnln x. Also π_{H(w)}(√x) ≤ √x, and by HL-A (spend U1) π_{H(w)}(x) ≥ ½𝔖(H(w)) x/ℓ^{L+1}. By CL8, 𝔖(H(w)) x/ℓ^{L+1} ≥ x·e^{−C_𝔖(L+1) − (L+1)lnℓ} = x·e^{−O((lnℓ)²)} = x^{1−o(1)} ≫ √x. Hence for x ≥ x₃:
N_cons(w; x) ≥ ¼ 𝔖(H(w)) x/ℓ^{L+1} ≥ 1. ∎

### 6.5 CL12: the deletion construction (unconditional)

Fix x large; ℓ = ln x. Parameters (no circularity):
- H(x) := 3C_g (ln 2x)²  (C_g from clause B),
- K := ⌈log₂ H(x)⌉  (so 2^K ≥ H(x); K = (2/ln 2)·lnln x + O(1) ≈ 2.885 lnln x),
- J := ⌈4 log₂ (K + 20)⌉  (so 2^J ≥ (K+20)⁴; J = O(ln lnln x)),
- L := J + 2 + K,  i₀ := J + 2.

Let q_1 < q_2 < … < q_{L+2} be the first L+2 primes exceeding L+3, and γ_i := q_{i+1} − q_i. Define
A := {q_1,…,q_{L+2}} ∖ {q_{i₀}},  A′ := {q_1,…,q_{L+2}} ∖ {q_{i₀+1}},  γ := γ_{i₀} = q_{i₀+1} − q_{i₀}.
(Both deletions are interior: 2 ≤ i₀ and i₀+1 ≤ L+1, since K ≥ 1.) Each of A, A′ has L+1 points; let w, w′ be their consecutive-gap words (length L) and H(w) = A − q_1, H(w′) = A′ − q_1 their offset tuples. Then:

1. **Structure.** w_i = w′_i = γ_i for i ≤ i₀ − 2 = J (prefix); w_{J+1} = γ_{i₀−1}+γ_{i₀}, w′_{J+1} = γ_{i₀−1} (difference +γ); w_{J+2} = γ_{i₀+1}, w′_{J+2} = γ_{i₀}+γ_{i₀+1} (difference −γ); w_i = w′_i = γ_{i−1... } — explicitly γ_{i+1} for J+3 ≤ i ≤ L (suffix of length K). Both words have the same total span h_L = q_{L+2} − q_1. γ is even (difference of odd primes) and ≥ 2. All entries are even and ≥ 2.
2. **Admissibility of both tuples.** For a prime p ≤ L+2: every element of A (resp. A′) is a prime > L+3 > p, hence ≢ 0 (mod p): residue class of −q_1... after translation, the class (−q_1 mod p) is missed; in the untranslated form, class 0 is missed — either way one class is missed. For p > L+2: only L+1 < p points, so ≥ 1 class is missed. Both H(w), H(w′) admissible. (No equal-run or divisibility structure is imposed anywhere; the primorial obstruction [B-III.1] is respected by design — the words are generic consecutive-prime gap words, not fixed repeated values.)
3. **Span bound.** π(L+3) ≤ L+2, so q_{L+2} ≤ p_{2L+4} ≤ C_P(2L+4)ln(2L+6) ≤ C₁ L ln L (CL-Ch iv). Hence span D ≤ C₁L ln L ≈ C₁ lnln x · lnlnln x ≪ ℓ ≪ ℓ³, and γ ≤ D.
4. **Budgets.** L + 2 ≤ 3 lnln x for large x (since K ≈ 2.885 lnln x and J = O(lnlnln x)); with the Bonferroni point, tuple sizes ≤ L+2+1 ≤ 4 lnln x. ∎

### 6.6 CL11 and CL14: HL_quant ⇒ FM

**CL11 (tail bound from clause B).** For ν ≥ ν₀ with p_ν ≥ e^{3.5}: g_{ν+j} ≤ C_g(ln p_{ν+j})² and p_{ν+j} < 2^j p_ν (Bertrand), so ln p_{ν+j} < ln p_ν + j and
δ_ν = Σ_j 2^{−j} g_{ν+j} ≤ C_g Σ_j 2^{−j}(ln p_ν + j)² ≤ C_g [2(ln p_ν)² + 2Σ_j j²2^{−j}] = 2C_g(ln p_ν)² + 12 C_g ≤ 3C_g(ln p_ν)². ∎

**CL14 (assembly).** Fix x ≥ x₄ (absolute). Build (w, w′, J, K, L, γ) by CL12. By CL10 (spends U1–U3) pick sites n, m with p_{n+1}, p_{m+1} ∈ (√x, x] at which w, w′ are consecutively realized. Then:
- (FM-P/F/S/0) hold by CL12.1 — the realized consecutive gaps are exactly the word entries.
- (FM-1): p_{n+L} ≤ p_{n+1} + D ≤ 2x, so by CL11 (spend U4) δ_{n+L} ≤ 3C_g(ln 2x)² = H(x) ≤ 2^K; same at m. Take H_r := H(x).
- (FM-2): (γ+4)/2^J ≤ (C₁L ln L + 4)/(K+20)⁴ ≤ 3C₁/(K+20)² → 0, using L ≤ 2(K+20) and ln L ≤ K+20 for large x.
- (FM-3): n, m ≥ π(√x) → ∞.
Taking x_r := e^{e^r} (spend U5) produces the FM sequences. ∎

### 6.7 CL15: chain assembly

HL_quant ⇒ (CL14) FM ⇒ (CL6) S irrational ⇒ 2S = Σ_{n≥0} (Nat.nth Nat.Prime n)/2^n irrational. This is the full primary objective: **HL_quant ⇒ FM ⇒ Irrational(tsum …)**. ∎

## 7. Briefing-facts usage register (contract: "every use marked")

| tag | fact | how used |
|-----|------|----------|
| [B-I.1] | Tao thread: loglog windows, polylog control, entropy suggestion | shaped HL-A's budgets (k ≤ 4 lnln x within "C loglog x", shifts ≤ (log x)³); entropy tool not needed for the primary. `[UNVERIFIED-LIT]` as literature, but load is carried by our HL-A statement, not the paraphrase. |
| [B-I.2] | ScPu11 factorial-world engine | **not used** in the primary; tertiary route note in §10. `[UNVERIFIED-LIT]` |
| [B-I.3] | Adversarial telescoping negative result | budget avoided per instruction; no dependence. |
| [B-II.G] | Fork–merge mechanism | primary mechanism; re-proved from scratch in the 2-entry-middle variant (CL6); the stage-1a proof is not an ingredient. |
| [B-II.A/C/E/F] | Equal-run, H-sep, v2-blocks, word-powers | not used in the primary; E/F notes in §10. |
| [B-III.1] | Primorial obstruction | respected as a design constraint: no fixed equal-gap runs, no locking thresholds 2^J ≥ b·c at large J anywhere; CL12's words are generic consecutive-prime gap words. Not otherwise invoked. |
| [B-III.2] | Parity (bδ_n even for n ≥ s+1) | re-proved as CL2; the factor-2 sharpening 2^Jℤ → 2^{J+1}ℤ is exactly what CL3 spends and CL6 needs (b(γ+4)/4 < 2^{J+1}). |
| [B-III.3] | Exact-locking countermodel | validates FM's design: no anti-concentration clause on δ appears in FM; the contradiction comes from γ ≥ 2, a structural (word-level) fact, not a δ-positivity assumption. |
| [B-III.4] | Statistics no-go | motivates that the only inputs beyond elementary arithmetic are the two prime-specific clauses HL-A, HL-B. |
| [B-IV] | Empirics ≤ 3·10⁷ | consistency only, not load-bearing: 262,687 repeated J=6 patterns ⇒ fork-type configurations birthday-abundant, matching CL10's x^{1−o(1)} counts; the unique J=4 run with c = 30 = 5# confirms the primorial design constraint; min δ = 2.7943 ≥ 2 consistent with CL0. The finite exclusions (denominator > 10^298) are not used. |

## 8. Lean 4 skeleton (contract item 4) — statements, proofs `sorry`

Target (given): `theorem erdos_251 : Irrational (tsum fun n : Nat => (Nat.nth Nat.Prime n : Real) / 2 ^ n)`. The tsum equals 2S; the skeleton works with δ and transfers by `Irrational (2*S) ↔ Irrational S` (rational scaling).

```lean
import Mathlib

noncomputable section
open scoped BigOperators

/-- 0-indexed primes: `P 0 = 2`, so math `p_k = P (k-1)`. -/
def P (n : ℕ) : ℕ := Nat.nth Nat.Prime n
/-- Gap `G k = P (k+1) - P k`; math `g_m = G (m-1)`. -/
def G (n : ℕ) : ℕ := P (n + 1) - P n
/-- Weighted future-gap average; `delta n` = math `δ_n`. -/
def delta (n : ℕ) : ℝ := ∑' i : ℕ, (G (n + i) : ℝ) / 2 ^ (i + 1)

/-- CL1 -/
theorem delta_block (n T : ℕ) :
    delta n = (∑ i ∈ Finset.range T, (G (n + i) : ℝ) / 2 ^ (i + 1)) + delta (n + T) / 2 ^ T := by
  sorry

/-- CL2. Hypothesis: the target sum is rational, in normal form `a / (2^s * b)`, `b` odd. -/
theorem rational_delta_eventually_lattice
    (a : ℤ) (s b : ℕ) (hb : Odd b) (hb0 : 0 < b)
    (hS : (tsum fun n : ℕ => (P n : ℝ) / 2 ^ n) = (a : ℝ) / (2 ^ s * b)) :
    (∀ n ≥ s, ∃ z : ℤ, (b : ℝ) * delta n = z) ∧
    (∀ n ≥ s + 1, ∃ z : ℤ, (b : ℝ) * delta n = 2 * z) := by
  sorry

/-- CL3/CL4 -/
theorem repeated_block_quantization
    (a : ℤ) (s b : ℕ) (hb : Odd b) (hb0 : 0 < b)
    (hS : (tsum fun n : ℕ => (P n : ℝ) / 2 ^ n) = (a : ℝ) / (2 ^ s * b))
    (n m J : ℕ) (hn : s + 1 ≤ n) (hm : s + 1 ≤ m)
    (hpre : ∀ i, 1 ≤ i → i ≤ J → G (n + i - 1) = G (m + i - 1)) :
    (∃ z : ℤ, (b : ℝ) * (delta (n + J) - delta (m + J)) = 2 ^ (J + 1) * z) ∧
    (|delta (n + J) - delta (m + J)| < 2 ^ (J + 1) / b → delta (n + J) = delta (m + J)) := by
  sorry

/-- CL5: one fork–merge configuration (2-entry middle block `(+γ, −γ)`). -/
structure FMConfig where
  n m J K : ℕ
  γ : ℕ
  H : ℝ
  hγ : 2 ≤ γ
  hpre : ∀ i, 1 ≤ i → i ≤ J → G (n + i - 1) = G (m + i - 1)
  hfork₁ : (G (n + J) : ℤ) - G (m + J) = γ          -- position J+1 (0-based shift)
  hfork₂ : (G (n + J + 1) : ℤ) - G (m + J + 1) = -γ  -- position J+2
  hsuf : ∀ i, J + 3 ≤ i → i ≤ J + 2 + K → G (n + i - 1) = G (m + i - 1)
  htail : max (delta (n + (J + 2 + K))) (delta (m + (J + 2 + K))) ≤ H
  hHK : H ≤ 2 ^ K

/-- CL5 (FM): configurations with vanishing prefix margin and escaping sites. -/
def FM : Prop :=
  ∃ c : ℕ → FMConfig,
    Filter.Tendsto (fun r => min (c r).n (c r).m) Filter.atTop Filter.atTop ∧
    Filter.Tendsto (fun r => ((c r).γ + 4 : ℝ) / 2 ^ (c r).J) Filter.atTop (nhds 0)

/-- CL6 core: a single suitable configuration contradicts a fixed rational form. -/
theorem fork_merge_contradiction
    (a : ℤ) (s b : ℕ) (hb : Odd b) (hb0 : 0 < b)
    (hS : (tsum fun n : ℕ => (P n : ℝ) / 2 ^ n) = (a : ℝ) / (2 ^ s * b))
    (c : FMConfig) (hn : s + 1 ≤ c.n) (hm : s + 1 ≤ c.m)
    (hmargin : (b : ℝ) * (c.γ + 4) / 4 < 2 ^ (c.J + 1)) : False := by
  sorry

/-- CL6 wrap: FM ⇒ the target sum is irrational. -/
theorem erdos_251_of_small_tail_fork_merge (h : FM) :
    Irrational (tsum fun n : ℕ => (Nat.nth Nat.Prime n : ℝ) / 2 ^ n) := by
  sorry

/-- Clause A (schematic; singular series as an abstract lower-bound form is what is spent). -/
def HLQuantA : Prop :=
  ∃ x₀ : ℕ, ∃ cA : ℝ, 0 < cA ∧ ∀ x ≥ x₀,
    ∀ Hs : Finset ℕ, (0 ∈ Hs) → (∀ h ∈ Hs, Even h ∨ h = 0) →
      Hs.card ≤ 4 * Nat.log 2 (Nat.log 2 x) →  -- schematic lnln budget
      (Hs.max' ⟨0, ‹0 ∈ Hs›⟩ ≤ (Nat.log 2 x) ^ 3) →
      Admissible Hs →  -- placeholder predicate: misses a class mod every prime
      -- two-sided count within factor 2 of 𝔖(Hs)·x/(log x)^{card}:
      True := by exact trivial  -- statement stub; full form in prose §4
/- NOTE: `HLQuantA` above is a stub; formalizing 𝔖 and the two-sided count is routine
   but verbose. The proof chain only consumes the two-sided factor-2 bounds of §4. -/

def HLQuantB : Prop :=
  ∃ Cg ν₀ : ℕ, 0 < Cg ∧ ∀ ν ≥ ν₀, (G ν : ℝ) ≤ Cg * (Real.log (P ν)) ^ 2

theorem hl_quant_implies_fm (hA : HLQuantA) (hB : HLQuantB) : FM := by
  sorry

theorem erdos_251_of_hl_quant (hA : HLQuantA) (hB : HLQuantB) :
    Irrational (tsum fun n : ℕ => (Nat.nth Nat.Prime n : ℝ) / 2 ^ n) :=
  erdos_251_of_small_tail_fork_merge (hl_quant_implies_fm hA hB)
end
```

Formalization notes. (i) `delta_block`, `rational_delta_eventually_lattice`, `repeated_block_quantization`, `fork_merge_contradiction` are fully elementary (geometric series, tsum manipulation, ℤ-divisibility) — Mathlib-ready. (ii) `hl_quant_implies_fm` contains the analytic content (CL8–CL12, CL14); its unconditional sublemmas (CL8, CL9, CL12, CL-Ch) are finitary/elementary and formalizable; HL-A/HL-B enter only through the stated interfaces. (iii) The `HLQuantA` stub must be replaced by a faithful two-sided count statement with a concrete `singularSeries : Finset ℕ → ℝ`; this is bookkeeping, not mathematics.

## 9. CL13 (independence of clause B) and false-start register

**CL13 (sketch, conf 0.7).** To derive "no gap > λ below x" from clause-A-type tuple asymptotics one must certify that every interval (y, y+λ] contains a prime. Inclusion–exclusion over the ~λ/2 admissible positions in the interval, truncated at level r, needs r ≳ c·λ/ℓ terms before the alternating tail stabilizes below the main term e^{−(1+o(1))λ/ℓ·ln...}; each level-s term inherits the clause-A relative error but is inflated by binom(λ/2, s) ≈ e^{s ln λ}. For λ = C_g ℓ² (the clause-B scale) the accumulated inflation is e^{Θ(ℓ·lnℓ)}-grade against a main term of size e^{−Θ(ℓ)}; polylog savings ℓ^{−A₀} are hopeless — savings of order e^{−cℓ^{3/2}} (for the safer λ = ℓ^{5/2} version: tuple sizes ~ℓ^{3/2} and error e^{−cℓ^{3/2}}) would be required. Hence clause B is a genuinely independent axiom at the stated error strength. (This reproduces the turn-1 computation; statuses: computation checked at the exponent level, constants not chased.)

**False starts (all from turn-1, recorded per contract).**
- FS1: condition pattern counts on δ_{end} ≤ H via a family pigeonhole; family capacity e^{L lnln x − L lnlnln x·(1+o(1))} vs required e^{L lnln x + Θ(L)}: short by e^{Θ(L lnlnln x)} — fails at the triple-log margin, irreparably as x → ∞.
- FS2: bound E[δ | word] by Cauchy–Schwarz on Σ g²: needs Σ_{p≤x} g_p² ≤ x^{1+o(1)} (RH-grade `[UNVERIFIED-LIT]`); even then the H²-vs-N(P) budget fails.
- FS3: statistical version of clause B ("≤ x/ℓ^{A} exceptional gaps") re-imports FS1's family tax.
- FS4: assuming one deletion changes one gap; in fact it changes two adjacent gaps (+γ, −γ). Repaired by generalizing FM's middle block; the weighted fork value ρ = γ/4 ≠ 0 survives and the contradiction sharpens (γ < 1 vs γ ≥ 2).
- FS5: matching the ~log₂x-gap tails of two sites verbatim; entropy ceiling for repeats is ≈ 2ℓ/(ln2 · lnℓ) matched gaps — impossible. Resolved by clause B: with g_ν ≤ C_gℓ² pointwise the bad-tail set is empty and no matching beyond L is needed.
- (Avoided by briefing, not attempted: equal-run/locking hypotheses [B-III.1]; adaptive-denominator telescoping [B-I.3].)

## 10. Secondary and tertiary objectives — status

Per the payload's priority rule ("deliver the primary completely before polishing anything else"), the secondary/tertiary routes were **not executed** this stage. Route notes carried from turn-1:
- **Secondary, v2-blocks [B-II.E]:** the needed existence input — sites ν with v₂(C_{ν,T}) ≥ T+1 at T ≈ 2log₂p_ν — prescribes ~T binary carry conditions across T ≫ lnln x gaps; this lies **outside** any loglog-window HL budget, so HL_quant as stated cannot feed it. Clause B removes the δ-side obstruction but not the existence side. Deprioritized.
- **Secondary, word-powers [B-II.F]:** small repeat counts K of growing words evade the primorial obstruction [B-III.1]; end-δ control is now free via clause B (CL11), so the remaining need is a two-occurrence count of w^K-patterns — plausibly a CL10-style corollary of HL-A; worth executing at stage 2. Status: sketch.
- **Tertiary, entropy / base-2 ScPu11 [B-I.1, B-I.2]:** untouched; the CL10 counting layer would be the natural uniformization substrate. `[UNVERIFIED-LIT]` for the ScPu11 internals.

## 11. Where I am stuck (contract item 5)

Nothing is missing **inside** the conditional chain: every implication in `HL_quant ⇒ FM ⇒ Irrational(S)` is proved above, with the uniformity spends U1–U5 itemized. The exact missing ingredients are the two open axioms themselves:
1. **HL-A** — a uniform quantitative prime-tuple asymptotic for up to 4 lnln x points, shifts ≤ (ln x)³, with any fixed polylog saving. Open; far beyond current technology (even two-point lower bounds are open).
2. **HL-B** — g_ν ≤ C_g(ln p_ν)². Open (Cramér–Granville-type); and by CL13 it cannot be folded into HL-A at polylog savings. Any proof of the package must therefore attack B separately, or accept a stronger error regime (e^{−(ln x)^{1+ε}} savings), or enlarge windows to ~log₂x (contradicting the loglog shape [B-I.1]).
A genuine weakening worth pursuing at stage 2: replace HL-B by "δ_ν ≤ (ln p_ν)^{O(1)} for **at least two** sites realizing each of the two §6.5 words" — a far weaker, word-conditioned statement; FS1 shows naive conditioning fails, but the deletion pair is a *single fixed pair* of words per scale, so a bespoke two-word variance estimate (second moment of δ over occurrences of one fixed word) is the sharpest open sub-target this analysis isolates.

— End of report. (Stage 1b, revision 2, turn 2; deterministic serialization of the turn-1 reasoning plus the closing of CL3.)
