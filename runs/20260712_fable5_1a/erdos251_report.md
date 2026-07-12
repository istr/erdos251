# Erdős Problem #251 — Is S = Σ pₙ/2ⁿ irrational? Consolidated report

**Task file:** `1a_blind.md` — **sha256:** `482f56ab95bbd912a68b3ade54d4de87cffb721ffda5f6016efdf18023a78fce`
**Prior reasoning trace:** `trace.md` — sha256 `801abb86022984e5e5c5e04a58f80f041c8c00721371c819f9fcf85f8f137a24`
**Constraints honored:** no web search / no external research; all literature inputs are flagged `[LIT-UNVERIFIED]`; all computations executed locally (sieve to 3·10⁷, exact rational arithmetic where labelled). Date of run: 2026-07-12.

**Bottom line.** The problem remains **open**; no unconditional resolution is claimed. The consolidated deliverables are: (a) several **precise conditional theorems** with fully proved implications and an exact account of where Hardy–Littlewood-type uniformity is spent; (b) **new proved reductions** (master criterion, doubling-map equivalence, parity refinement, two-window pigeonhole reduction, primorial obstruction); (c) **rigorous refutations** of four natural strategies, including a correction of the dossier's own item 4 (Cramér calibration); (d) a verified numerical layer (finite exclusions, explicitly labelled as verification/calibration, not asymptotic progress).

---

## 0. Reconciliation of the two interrupted attempts

Attempt 1 built the identity/criterion framework, proved the **vacuity theorem** (no finite certificate can exist), derived the **two-window pigeonhole reduction** on top of Maynard–Tao, and set up elementary tail bounds plus the full numerical plan. Attempt 2 re-derived the same identities (fully consistent), then added the **parity refinement** (factor-2 improvement of every squeeze threshold), the **lower bound δₙ > 8/3**, the **refutation of the J = 1 route for odd b ≥ 7**, the **primorial obstruction** with the corrected Cramér landscape, the clean conditional **Hypothesis (P)**, and the **δ < 4 route** for the dyadic sub-problem. The two attempts contradict each other nowhere; attempt 2 corrects the *dossier* (item 4) and refines attempt 1's Lemma-L framing.

Two factual corrections produced by this consolidation run:

1. **Aftermath at the CPAP-5.** The trace (following the dossier's "sits exactly at the b = 1 threshold") expected |δ_{n+4} − 30| ≈ 15.6, marginally below 2⁴ = 16. The rigorous computation gives **δ_{n+4} = 25.306609138765…** (enclosure width < 10⁻²⁹), i.e. **|δ_{n+4} − 30| = 4.693390861…**, comfortably inside (0, 16). The dossier's "threshold" statement is correct only in the sense J = 4 ≈ log₂ log p; the *realized* aftermath is far from marginal, so the dyadic squeeze exclusion of §9.3 is decisive, not borderline. The squeeze identity itself verifies on the nose: δₙ − 30 = −0.293336929 = (δ_{n+4} − 30)/16.
2. **Dossier item 4 ("Cramér model gives log N(J) ~ J log J — vast headroom").** False for large J; see §7. The correct Cramér-calibrated profile is doubly exponential, log N(J) = e^{(1/2+o(1))J}, with razor-thin (but positive) headroom against 2^J.

---

## 1. Claims ledger

Status codes: **P** proved here (self-contained), **P\*** proved here computer-assisted with exact rational arithmetic, **R** reduction/implication proved here (hypothesis open), **V** verified numerically (rigor level stated), **H** heuristic (labelled), **F** refuted here, **LIT** literature input, unverified by rule.

| id | statement | status | deps | conf |
|----|-----------|--------|------|------|
| C1 | uₙ := Σ_{k≥1} p_{n+k}2^{−k} = p_{n+1} + δₙ with δₙ := Σ_{j≥1} g_{n+j}2^{−j}; Σ_{n≥1} gₙ2^{−n} = S − 2; δ_{n+1} = 2δₙ − g_{n+1}; δₙ ≥ 2; S = 2 + Σ_{n≤K} gₙ2^{−n} + 2^{−K}δ_K | P | — | 0.99 |
| C2 | p_k ≤ 4k ln k for all k ≥ 4 | P (inline Chebyshev-binomial for k ≥ 18; finite check 4–17; verified to k = 1,857,859: 0 violations) | — | 0.97 |
| C3 | Tail bounds: δ_μ ≤ 4[(M+1)ln M + 1 + 3/M], M = μ+2; 0 < S − Σ_{k≤N}p_k2^{−k} ≤ 4·2^{−N}[(N+2)ln(N+1)+2] | P | C2 | 0.97 |
| C4 | Criterion: S = a/(2^s b) in lowest terms (b odd) ⟹ bδₙ ∈ ℤ ∀ n ≥ s; conversely one n with bδₙ ∈ ℤ (b odd) ⟹ S ∈ ℚ. Master criterion: S irrational ⟺ ∀ odd b ∀ n: bδₙ ∉ ℤ ⟺ δ₁ irrational | P | C1 | 0.98 |
| C5 | {δₙ} = {2ⁿS}: the fractional parts are the doubling-map orbit of S; S rational ⟺ ({δₙ}) eventually periodic (period ord_b 2); exact coincidence δ_N = δ_M (N > M) ⟺ (2^N − 2^M)S ∈ ℤ ⟺ M ≥ s and ord_b(2) | N − M | P | C1,C4 | 0.97 |
| C6 | Squeeze: g_{n+1} = … = g_{n+J} = c ⟹ δₙ − c = 2^{−J}(δ_{n+J} − c). Theorem (L\*) ⟹ irrational, see §6 | P/R | C1,C4 | 0.97 |
| C7 | Parity refinement: mₙ := bδₙ ∈ ℤ for n ≥ s forces mₙ even ∀ n ≥ s+1; all squeeze/two-window thresholds improve from 2^J/b to 2^{J+1}/b | P | C4 | 0.96 |
| C8 | Vacuity/steering theorem: every finite even gap prefix (no consecutive 2s, growth ~ ln j, counting ~ x/ln x allowed) extends to a tail making Σ qₙ2^{−n} equal to **any** prescribed rational; hence **no finite certificate exists** and no proof can use only growth rate + PNT-type counting statistics | P | — | 0.93 |
| C9 | δₙ > 8/3 for all n ≥ 3; the unique minimizer (2,4)^∞ of the relaxed problem is inadmissible mod 5 | P | — | 0.97 |
| C10 | δₙ > 17580233/6291456 = 2.794302781… for all n ≥ 3 (DP over mod-{3,5,7} admissible sequences, horizon 22, exact rationals). Essentially sharp: δ₄ = 2.794303456… < 14/5 (exact enclosure), attained at p₅ = 11, whose class (2 mod 3, 1 mod 5, 4 mod 7) is the DP minimizing class | P\* | C9 method | 0.95 |
| C11 | The (J,c) = (1,2) squeeze can never certify any odd b ≥ 7; for b = 5 it would need δ ∈ (2.7943028, 2.8) at arbitrarily large twin sites (recurrence of the 8-gap head (2,4,2,4,6,2,6,4)); for b ∈ {1,3} it needs twin-clustering events — all open | P (refutation) + R | C7,C10 | 0.96 |
| C12 | Hypothesis (P): ∀ε > 0, infinitely many n with g_{n+1} = g_{n+2} = 6 and 0 < |δ_{n+2} − 6| < ε. **Theorem: (P) ⟹ S irrational** | R (implication P) | C4,C6,C7 | 0.97 |
| C13 | Primorial obstruction: a J-run of gap c with p_{n+1} > J+1 forces q | c for every prime q ≤ J+1, hence c ≥ (J+1)# | P | — | 0.98 |
| C14 | Exact: {x ≤ 30000 : x# ≤ 2^x} = {2,3,4,5,6,8,9,10,12,15,16,28}; so x# > 2^x for all 29 ≤ x ≤ 30000 **exactly**; for x > 30000 via θ(x) ≥ 0.92x [LIT-CLASSICAL Chebyshev, unverified] | P\*+LIT | — | 0.97 |
| C15 | Corrected Cramér calibration: for J ≥ 28, a squeeze-usable J-run forces δ_{n+J} ≥ (J+1)# − 2^{J+1} (an e^{(1+o(1))J} gap-desert immediately after the run); under Cramér this forces log p ≥ e^{(1/2−o(1))J}, so log N(J) = e^{(1/2+o(1))J} — doubly exponential, not J log J; still o(2^J) with exponent margin 0.5 vs ln 2 = 0.693. The desert sits exactly at the Cramér-extremal (log p)² scale. **Dossier item 4 corrected.** | H (calibration; the forcing step is P given C13) | C7,C13,C14 | 0.85 |
| C16 | For every J, some J-pattern of consecutive gaps repeats infinitely often (Maynard–Tao bounded clusters [LIT-UNVERIFIED, conf 0.97] + pigeonhole) | R+LIT | — | 0.95 |
| C17 | Two-window reduction: equal J-patterns at n, m ⟹ δₙ − δ_m = 2^{−J}(δ_{n+J} − δ_{m+J}); under rationality (n,m ≥ s+1): b(δ_{n+J} − δ_{m+J}) ∈ 2^{J+1}ℤ. **Theorem: H-sep ⟹ S irrational** (§6.2) | P/R | C4,C7,C16 | 0.96 |
| C18 | Standard uniform Hardy–Littlewood is insufficient to derive (P)/(L\*)/H-sep: controlling δ needs prescribing K ≍ log₂ p gaps (tuple size ≍ ε·log x, diameter ≍ log²x), the regime where the naive HL asymptotic is self-inconsistent [LIT-UNVERIFIED, Granville–Soundararajan-type]. Exact missing input: anti-concentration of δ at pattern sites (§8) | R+LIT | C3 | 0.85 |
| C19 | Maynard-cluster smallness route refuted: forcing δₙ = O(1) via clusters needs m primes in an interval of length o(2^m); best known is e^{(3.8+o(1))m} [LIT-UNVERIFIED] | F+LIT | — | 0.90 |
| C20 | Dyadic route: if δₙ ∉ ℤ for a single n then v₂(denominator) > n. If S = a/2^s then δₙ is an even integer ≥ 4 for every n ≥ s+1; hence any n ≥ s+1 with δₙ < 4 is a contradiction; "δₙ < 4 infinitely often ⟹ S ∉ ℤ[1/2]" | P | C4,C7,C9 | 0.97 |
| C21 | Numerics package §9 (R1–R23, S1–S4): exact/interval-rigorous where stated, float-grade where stated | V | C2,C3 | 0.98 |
| C22 | The problem remains open; nothing here resolves it unconditionally | meta | — | 1.0 |

---

## 2. Setup and proved identities (C1)

Let p₁ = 2 < p₂ = 3 < … be the primes, gₙ = p_{n+1} − pₙ, S = Σ_{n≥1} pₙ2^{−n} (converges by C2). Define the tail functionals

  uₙ = Σ_{k≥1} p_{n+k} 2^{−k},  δₙ = Σ_{j≥1} g_{n+j} 2^{−j}.

**Identities (all proved by elementary rearrangement, absolutely convergent):**
uₙ = p_{n+1} + δₙ; Σ_{n≥1} gₙ2^{−n} = S − 2; δ_{n+1} = 2δₙ − g_{n+1} (equivalently δₙ = (g_{n+1} + δ_{n+1})/2); δₙ ≥ 2 for n ≥ 1 (all gaps g_m ≥ 2 for m ≥ 2); and the finite decomposition S = 2 + Σ_{n=1}^{K} gₙ2^{−n} + 2^{−K}δ_K, which is the exact form used by all numerics. Numerical spot checks: recursion holds to 10⁻⁹ across the range; the K = 40 decomposition reproduces S to full float precision; {2¹⁰S} = {δ₁₀} = 0.835421196 (§9.6).

**Elementary growth (C2, C3).** p_k ≤ 4k ln k for k ≥ 4: by the Chebyshev binomial bound π(x) ≥ 0.6x/ln x for x ≥ 200 (from (2m)^{π(2m)} ≥ C(2m,m) ≥ 4^m/(2m+1)), if p_k > 4k ln k then k = π(p_k) ≥ π(4k ln k) > k for k ≥ 18, contradiction; k = 4,…,17 checked directly; additionally verified for every k ≤ 1,857,859 (zero violations). This yields the two proved tail bounds of C3 used to make every computation below an interval enclosure: δ_μ ≤ 4[(M+1)ln M + 1 + 3/M] with M = μ+2, and 0 < S − S_N ≤ 4·2^{−N}[(N+2)ln(N+1)+2].

## 3. Master criterion, doubling map, and the vacuity theorem

**Criterion (C4).** If S = a/(2^s b) in lowest terms with b odd, then for n ≥ s, b·2ⁿS ∈ ℤ and 2ⁿ·Σ_{k≤n}p_k2^{−k} ∈ ℤ, so b·uₙ ∈ ℤ, so **bδₙ ∈ ℤ for all n ≥ s**. Conversely, a single n with bδₙ ∈ ℤ (b odd) makes uₙ, hence S, rational with odd denominator part dividing b and 2-part ≤ n. Because integrality propagates forward through m_{n+1} = 2mₙ − bg_{n+1} (mₙ = bδₙ), one instance is equivalent to all later instances. Hence the **master criterion**:

> S is irrational ⟺ for every odd b ≥ 1 and every n ≥ 1, bδₙ ∉ ℤ ⟺ δ₁ is irrational.

**Doubling map (C5).** {δₙ} = {2ⁿS} (from S = Sₙ + uₙ2^{−n} and uₙ = p_{n+1} + δₙ). So rationality of S is precisely eventual periodicity of the binary shift orbit, with eventual period d = ord_b(2). Exact coincidences classify cleanly: δ_N = δ_M (N > M) ⟺ (2^N − 2^M)S ∈ ℤ ⟺ M ≥ s and ord_b(2) | N − M. These are used verbatim in §6.

**Vacuity theorem (C8) — no finite certificate.** Fix any odd b, any n₀, any target rational τ = k/b (τ in the reachable range), and any finite gap prefix. There is an infinite continuation by even gaps h_j ≥ 2, avoiding consecutive (2,2), with h_j = ln j + O(1) and counting function Q(x) = (1+o(1))x/ln x, such that the resulting δ_{n₀} equals τ exactly — greedy binary steering: write h_j = base_j + 2ε_j with ε_j ∈ {0,1}; each ε_j moves the tail sum by 2^{1−j}, and the invariant "remaining deficit ∈ [0, 2^{1−j})" can be maintained at every step, so the deficit converges to 0 and δ_{n₀} = τ. Consequences: (i) rationality of such series is a **tail property**, never decidable from finitely many gaps; (ii) **no proof of Erdős #251 can use only** the growth rate pₖ ~ k ln k, evenness, absence of (2,2), and PNT-type counting — a sequence with all those properties can have rational sum. Any successful proof must use finer prime-specific structure. This is a rigorous refutation of an entire strategy class (deliverable class 4) and also confirms the dossier's "vacuity warning" in the strongest form.

## 4. Parity refinement (C7)

Suppose bδ_s ∈ ℤ. Since every gap g_m with m ≥ 2 is even, m_{n+1} = 2mₙ − bg_{n+1} is even for every n ≥ s, i.e. **mₙ = bδₙ ∈ 2ℤ for all n ≥ s+1**. Mod 4 there is no further fixed pattern (the residue is dictated by g mod 4, which is not constrained), so a factor 2 is the full extractable gain. Effect: in every squeeze/two-window argument below, the contradiction window widens from 2^J/b to **2^{J+1}/b** at the cost of requiring indices ≥ s+1 instead of ≥ s.

## 5. Lower bounds for δ and the death of the J = 1 route (C9, C10, C11)

For n ≥ 3 (so p_{n+1} ≥ 7) the tail gaps are even, ≥ 2, with no two consecutive 2s (p, p+2, p+4 cannot all be prime unless p = 3). Minimizing Σ x_j2^{−j} under exactly these constraints gives value **8/3**, attained only by (2,4)^∞; that pattern forces the residues p+0, p+2, p+6, p+8, p+12, p+14 to cover all classes mod 5, impossible for p > 5, hence **δₙ > 8/3 strictly** (C9).

Adding the mod-3, mod-5, mod-7 covering constraints and running an exact-rational DP (horizon 22, tail bounded below by 8/3, alphabet up to 30, minimized over the allowed residue classes of p) gives the certified bound (C10):

> **δₙ > 17580233/6291456 = 2.794302781… for all n ≥ 3.**

This is essentially sharp: the true infimum is δ₄ = 2.794303456… (< 14/5, exact enclosure), realized right after p₅ = 11 by the gap head (2,4,2,4,6,2,6,4,…) — and 11's congruence class (2 mod 3, 1 mod 5, 4 mod 7) is exactly the class the DP identifies as minimizing. In the data, min_{n≥10} δₙ = 2.891567 (at n = 781,928, p = 11,900,501) and min_{n≥10⁶} δₙ = 2.906770.

**Refutation (C11).** The (J,c) = (1,2) squeeze needs a twin gap g_{n+1} = 2 at n ≥ s+1 with 0 < |δ_{n+1} − 2| < 4/b (parity threshold). Since δ − 2 > 0.794302781 always, this is **impossible for every odd b ≥ 7** (4/7 < 0.7943). For b = 5 the window is (2.7943028, 2.8) — nonempty, and actually attained by the sequence at n = 4, so no all-n lower bound can ever close it; certifying b = 5 this way would need the 8-gap head (2,4,2,4,6,2,6,4) (a prime-octuplet-type constellation) recurring at arbitrarily large heights — open. For b ∈ {1,3} one needs δ_{n+1} < 2 + 4/b at twin sites infinitely often — open even granting the twin prime conjecture, because it demands *clusters* after the twin. This kills the simplest imaginable certificate scheme for all but three denominators and pins down exactly what those three would cost.

## 6. Runs, two windows, and the conditional theorems

### 6.1 Equal-run squeeze (C6) and Theorem A

If g_{n+1} = … = g_{n+J} = c then δₙ − c = 2^{−J}(δ_{n+J} − c) (telescoping the recursion). Combined with C4 + C7:

> **Hypothesis (L\*).** For every T ≥ 1 there exist n ≥ T, J ≥ 1 and an even c with g_{n+1} = … = g_{n+J} = c and 0 < |δ_{n+J} − c| < 2^{J+1}/T.
>
> **Theorem A. (L\*) ⟹ S is irrational.** Proof: if S = a/(2^s b), apply (L\*) with T = max(s+1, b): then b(δₙ − c) ∈ 2ℤ, so b(δ_{n+J} − c) = 2^J·b(δₙ − c) ∈ 2^{J+1}ℤ, yet 0 < b|δ_{n+J} − c| < b·2^{J+1}/T ≤ 2^{J+1} — no such element of 2^{J+1}ℤ exists. ∎

A specialization with fixed parameters, the cleanest conditional statement of this report:

> **Hypothesis (P).** For every ε > 0 there are infinitely many n with g_{n+1} = g_{n+2} = 6 and 0 < |δ_{n+2} − 6| < ε.
>
> **Theorem B. (P) ⟹ S is irrational** (C12). Proof: given S = a/(2^s b), take ε = 8/b and an instance with n ≥ s+1: b(δ_{n+2} − 6) = 4·b(δₙ − 6) ∈ 8ℤ but 0 < b|δ_{n+2} − 6| < 8. ∎

(P) asserts CPAP-3s with common difference 6 whose weighted aftermath approaches 6 without hitting it — an equidistribution statement supported by Cramér/Hardy–Littlewood heuristics, with no modular obstruction (deviations of both signs around 6 are admissible), but open; note even the *existence* of infinitely many CPAP-3 is open unconditionally [LIT-UNVERIFIED status: treated as open per dossier].

### 6.2 Two-window pigeonhole reduction (C16, C17) and Theorem C

Maynard–Tao [LIT-UNVERIFIED, conf 0.97]: for every m there is C(m) with p_{n+m} − pₙ ≤ C(m) infinitely often. At such n all m−1 consecutive gaps are ≤ C(m); by pigeonhole **some fixed (m−1)-pattern of gaps repeats infinitely often** — so pattern repetition is unconditional (modulo the cited theorem), no CPAP needed. If the same J-pattern occurs at n and m, the shared prefix gives the **two-window identity** δₙ − δ_m = 2^{−J}(δ_{n+J} − δ_{m+J}); under rationality with n,m ≥ s+1: b(δ_{n+J} − δ_{m+J}) ∈ 2^{J+1}ℤ. Thus aftermaths at repeat sites live on a coset grid of spacing 2^{J+1}/b — they either coincide exactly (classified by C5: ord_b(2) | n − m) or separate by ≥ 2^{J+1}/b.

> **Hypothesis H-sep.** For every T ≥ 1 there exist J ≥ 1 and two occurrences n, m ≥ T of one J-gap-pattern with 0 < |δ_{n+J} − δ_{m+J}| < 2^{J+1}/T.
>
> **Theorem C. H-sep ⟹ S is irrational.** Same one-line contradiction as Theorem A. ∎

H-sep replaces "runs exist" (open) by "repeats exist" (essentially free) and moves the entire difficulty into the analytic separation of two aftermath values — a pair-correlation/anti-concentration statement.

## 7. The primorial obstruction and the corrected Cramér landscape (C13, C14, C15)

**Obstruction (C13, proved).** In a J-run g_{n+1} = … = g_{n+J} = c with p_{n+1} > J+1, the J+1 primes p_{n+1}+jc (0 ≤ j ≤ J) are consecutive; for any prime q ≤ J+1 with q ∤ c the residues p_{n+1}+jc cover all classes mod q as j runs over 0,…,q−1 ⊆ {0,…,J}, so some term is a proper multiple of q — impossible. Hence every prime q ≤ J+1 divides c and **c ≥ (J+1)#**. The lone J = 4 run in the data has c = 30 = 5# exactly — the primorial fingerprint sitting in the dossier's own numerics.

**Exact size comparison (C14).** Computed exactly: x# ≤ 2^x precisely for x ∈ {2,3,4,5,6,8,9,10,12,15,16,28} within x ≤ 30000; so **x# > 2^x for all x ≥ 29** in that range (and beyond via Chebyshev θ(x) ≥ 0.92x > x ln 2 [LIT-CLASSICAL, unverified inline]).

**Consequence for the squeeze (proved given C13/C7).** For J ≥ 28, any run passing the squeeze window |δ_{n+J} − c| < 2^{J+1}/b forces δ_{n+J} ≥ (J+1)# − 2^{J+1} = e^{(1+o(1))J}: an *exponential-in-J gap desert* must start immediately after the run (some gap of size ≳ (J+1)#/4 within O(J) steps, by the geometric weighting). Unconditionally this forces p_n > (J+1)#/4; under Cramér-type maximal-gap bounds g ≪ (log p)² it forces **log pₙ ≥ e^{(1/2−o(1))J}**, i.e. first-usable-occurrence height log N(J) = e^{(1/2+o(1))J} — *doubly exponential in J*. The required desert length e^{(1+o(1))J} then equals (log p)^{2} at that height: usable configurations sit **exactly at the Cramér-extremal scale**. Headroom against the budget 2^J = e^{J ln 2} survives with exponent margin ln 2 − 1/2 ≈ 0.19 — positive but razor-thin, and the mechanism is a fine-tuned large-deviation event, not typicality.

**Correction of dossier item 4 (C15).** The dossier's calibration "log N(J) ~ J log J, vastly smaller than 2^J — vast headroom" is wrong for large J: it ignored c ≥ (J+1)# ≫ 2^J. For fixed b, only finitely many J admit "typicality-grade" runs at all (those with (J+1)# ≲ 2^{J+1}/b, a subset of {J+1 ∈ {2,…,6,8,9,10,12,15,16,28}} even for b = 1), and inside these the aftermath must still land in a width-2^{J+1}/b interval around c — probability ≍ 2^{J+1}/(b log p) per run under Cramér. **Conclusion: for every odd b, the run-squeeze route requires an equidistribution/anti-concentration event; mere typicality never suffices.** This is the honest, corrected shape of the conditional pathway, and it is exactly what (P), (L\*) and H-sep encode.

## 8. Where Hardy–Littlewood uniformity is actually spent (C18) — and two dead routes

**What would be needed.** To *derive* (P)/(L\*)/H-sep one must control δ_{n+J} — an infinite-tail functional — at run/repeat sites. The proved truncation (C3) reduces δ to its first K gaps with error 2^{−K}·O(m log m) (elementary) or 2^{−K}·O(p^θ) (any Hoheisel θ < 1 [LIT-UNVERIFIED]); hitting a window of width 2^{J+1}/b needs K ≈ log₂ p + log₂(b) − J: i.e. prescribing a tuple of **k ≍ ε·log x primes with diameter ≍ log²x**. Standard uniform Hardy–Littlewood conjectures are stated for fixed k (or k growing very slowly); at k ≍ log x the naive singular-series main term is known to be self-inconsistent (maximal-deviation phenomena, Granville–Soundararajan-type [LIT-UNVERIFIED, conf 0.8]). So: **no combination of standard HL-uniform statements yields the conditional hypotheses**; the exact missing input is
> anti-concentration of the aftermath functional at pattern sites: for a fixed admissible (J,c) (e.g. (2,6)), the values δ_{n+J} at run sites are not eventually confined to the lattice (1/b)ℤ for any b — quantitatively, they enter (c, c+ε) \ {c} for every ε > 0 —
which is a second-moment/pair-correlation statement (Gallagher-type for growing k [LIT-UNVERIFIED]) rather than a counting statement. This answers the dossier's deliverable (2) precisely: the hypothesis cannot be phrased as "HL uniform in k ≤ (log x)^{1−δ}"; it must include tail-functional equidistribution.

**Dead route 1 (C19).** Forcing δₙ = O(1) via prime clusters: δₙ ≤ H_m + 2^{−m}·δ_{n+m} needs m primes in an interval of length o(2^m); the best known cluster diameter is C(m) = e^{(3.8+o(1))m} [LIT-UNVERIFIED] — exponentially too large, and even the conjectural optimum m log m only reproduces typical size. Refuted as a route to smallness.

**Dead route 2.** Digit/normality arguments: by C5 they are *equivalent restatements* (eventual periodicity of the shift orbit), not independent leverage; and C8 shows no digit-blocking argument can run on statistics alone.

**Dyadic sub-problem (C20).** If S = a/2^s then δₙ is an integer for all n ≥ s and an **even** integer ≥ 4 for n ≥ s+1 (parity + C9). Hence: a single n with δₙ ∉ ℤ proves v₂(q) > n for the denominator q; and "δₙ < 4 for arbitrarily large n" ⟹ S ∉ ℤ[1/2]. The latter hypothesis needs g_{n+1} ∈ {2,4} plus a controlled window of ≈ log₂ pₙ subsequent gaps — quadruplet-type clustering, open even under the twin prime conjecture (this is the **joint-control bottleneck**: pattern *and* tail functional simultaneously). Data: 1907 sites with δₙ < 4 below 3·10⁷, the largest at n = 1,856,254 (p = 29,972,729, δ = 3.9412).

## 9. Numerical verification layer (C21) — all finite; verification/calibration, not progress

Environment: pure Python, sieve of Eratosthenes to 3·10⁷ (π(3·10⁷) = 1,857,859; max gap 210), backward recursion for δ (float, certified error < 10⁻⁹ for n ≤ 1,857,757), exact `Fraction` arithmetic wherever a claim is labelled rigorous; every tail is bounded by the proved C3 inequalities. Total runtime ≈ 17 s.

**9.1 Dossier cross-checks (all pass).** S = 3.674643966011328778995676309084029411677797588779437328312205… — first **597 decimals certified** by the exact enclosure (N = 2000, width < 10⁻⁵⁹⁸); matches the dossier's digits. Certified continued fraction prefix [3; 1,2,13,1,1,2,7,1,2,1,2,18,2,15,1,1,5,5,1,2,1,1,9] — matches and extends the dossier's list. Identities verified (§2). Runs census below 3·10⁷: 3768 maximal runs of J ≥ 3, distributed {(3,6): 2580, (3,12): 789, (3,18): 292, (3,24): 47, (3,30): 55, (3,36): 3, (3,42): 1, (4,30): 1}; every run has 6 | c, every J ≥ 4 run has 30 | c (primorial fingerprint); first J = 3 run at 251 (c = 6); the **unique J = 4 run** starts at 9,843,019 — the CPAP-5 (9843019, 9843049, 9843079, 9843109, 9843139), verified prime and consecutive; π(9,843,019) = 654,926, so the run index is n = 654,925.

**9.2 Rigorous rational exclusions.**
- *Continued-fraction bound:* the simplest rational in the certified enclosure has a 299-digit denominator ⟹ **any rational equal to S has denominator q > 10²⁹⁸.**
- *(s,b)-grid at one deep site:* at n_site = 1,857,459 (p = 29,993,149), δ computed as an exact fraction from 300 gaps with tail < 5.3·10⁻⁷⁸: for **every odd b ≤ 99,999**, bδ misses ℤ by ≥ 3.4·10⁻⁶ ≫ b·tail ⟹ **S ≠ a/(2^s b) for all s ≤ 1,857,459 and all odd b ≤ 99,999** (in particular v₂-exclusion to 2^{1,857,459} for the dyadic case b = 1).

**9.3 The squeeze in action (rigorous; corrected value).** At the CPAP-5: δ_{n+4} = 25.306609138765… (exact-fraction enclosure, error < 10⁻²⁹), so |δ_{n+4} − 30| = 4.693390861… ∈ (0, 16). If S = a/2^s with s ≤ n = 654,925 then δ_{n+4} − 30 ∈ 16ℤ \ {0} — contradiction ⟹ **S ≠ a/2^s for every s ≤ 654,925**, using only the 5 run primes plus 140 subsequent gaps. This illustrates the mechanism's leverage (145 local gaps ⇒ a 2^{654,925}-scale exclusion); the direct method of 9.2 is stronger but "reads" the same kind of local data. The squeeze identity verifies exactly: δₙ − 30 = −0.293336929 = (δ_{n+4} − 30)/16.

**9.4 Two-window demonstration (float-grade calibration).** J = 6 over all 1,857,749 windows: 262,687 patterns repeat; minimal nonzero aftermath difference 1.709·10⁻⁶, between n = 230,801 (p = 3,208,657) and m = 768,764 (p = 11,686,027), shared pattern (22,8,4,2,28,6). Modulo float verification, this single pair excludes all odd b ≤ 74,788,752 for s ≤ 230,800 — a live demonstration that H-sep-type near-coincidences are abundant in data (birthday scaling), exactly as the reduction predicts.

**9.5 δ-landscape.** min_{n≥3} δₙ = δ₄ = 2.794303456 (< 14/5, exact); min_{n≥10} = 2.891567 at n = 781,928; min_{n≥10⁶} = 2.906770 at n = 1,604,468; the DP bound 2.794302781 (C10) is 6.8·10⁻⁷ below the true infimum. p_k ≤ 4k ln k: zero violations up to k = 1,857,859. Primorial table: §7.

**9.6 Identity spot checks.** {2¹⁰S} = {δ₁₀} = 0.835421196; S = 2 + Σ_{n≤40} gₙ2^{−n} + 2^{−40}δ₄₀ to full precision; recursion δ_{n+1} = 2δₙ − g_{n+1} exact on sampled windows.

*Per the task contract, all of 9.1–9.6 is finite verification/calibration. None of it constitutes asymptotic progress on the open problem, and the report does not claim otherwise.*

## 10. Lean-ready statements (plausible Lean 4 / Mathlib style — **not compiled**)

`Nat.nth Nat.Prime` is 0-indexed (`Nat.nth Nat.Prime 0 = 2`), so the target series equals Σ_{n≥0} p_{n+1}/2ⁿ = 2S; irrationality is equivalent.

```lean
-- Target (open):
theorem erdos_251 :
    Irrational (tsum fun n : ℕ => (Nat.nth Nat.Prime n : ℝ) / 2 ^ n) := sorry

noncomputable def Sser : ℝ := ∑' n : ℕ, (Nat.nth Nat.Prime n : ℝ) / 2 ^ n
def gap (n : ℕ) : ℕ := Nat.nth Nat.Prime (n + 1) - Nat.nth Nat.Prime n
noncomputable def delta (n : ℕ) : ℝ := ∑' j : ℕ, (gap (n + j) : ℝ) / 2 ^ (j + 1)
-- (delta n here is δ_{n+1} of the report; index shift is notational only.)

lemma summable_prime_div_pow_two :
    Summable (fun n : ℕ => (Nat.nth Nat.Prime n : ℝ) / 2 ^ n) := sorry
lemma delta_ge_two (n : ℕ) : 2 ≤ delta n := sorry
lemma delta_rec (n : ℕ) : delta (n + 1) = 2 * delta n - gap (n + 1) := sorry
lemma delta_gt_eight_thirds {n : ℕ} (hn : 2 ≤ n) : 8 / 3 < delta n := sorry
lemma frac_orbit (n : ℕ) : Int.fract (2 ^ (n + 1) * Sser) = Int.fract (delta n) := sorry

-- Master criterion:
theorem rational_iff_delta :
    (∃ q : ℚ, (Sser : ℝ) = q) ↔ ∃ b : ℕ, Odd b ∧ 0 < b ∧ ∃ n k : ℤ, (b : ℝ) * delta n.toNat = k := sorry

-- Squeeze identity:
lemma squeeze {n J : ℕ} {c : ℕ} (h : ∀ i < J, gap (n + i) = c) :
    delta n - c = (delta (n + J) - c) / 2 ^ J := sorry

-- Hypothesis (P) and the conditional theorem:
def HypP : Prop :=
  ∀ ε > (0 : ℝ), ∀ N : ℕ, ∃ n ≥ N, gap n = 6 ∧ gap (n + 1) = 6 ∧
    0 < |delta (n + 1) - 6| ∧ |delta (n + 1) - 6| < ε
theorem hypP_implies_irrational (hP : HypP) :
    Irrational (∑' n : ℕ, (Nat.nth Nat.Prime n : ℝ) / 2 ^ n) := sorry
```

The proofs of `delta_rec`, `frac_orbit`, `squeeze`, `rational_iff_delta` and `hypP_implies_irrational` are the elementary arguments of §§2–6 and should formalize with standard `tsum` manipulation; `delta_gt_eight_thirds` needs the (3,5,7)-covering combinatorics of §5.

## 11. Where I am stuck (exact bottleneck)

The master criterion reduces everything to: **for every odd b, exhibit arbitrarily large n with bδₙ ∉ ℤ.** Every certificate mechanism discovered (equal-run squeeze, two-window separation, δ < 4 dyadic route) reduces further to one shape of event: *place the infinite-tail functional δ, at a site carrying a prescribed finite gap pattern, into a prescribed interval of length ≈ 2^{J+1}/b.* The obstruction is structural: sieve technology (Maynard–Tao and descendants) controls finite windows of primes and does so magnificently — it hands us the patterns for free (§6.2) — but provides zero control over the weighted infinite tail δ at those sites; and the vacuity theorem (§3) proves that finite-window control alone can *never* suffice, since any finite window is consistent with any rational value of the tail. Hardy–Littlewood-type inputs would need to operate at tuple size ≍ ε log x, precisely where their asymptotics are unreliable (§8). So the missing lemma is an **anti-concentration / equidistribution statement for δ at pattern sites** — Hypothesis (P) is its minimal clean instance, H-sep its pattern-repeat variant. I could not prove any instance, for any single odd b ≥ 7 at arbitrary height, nor even the dyadic case S ∉ ℤ[1/2]; the latter already requires quadruplet-type joint clustering that is open under the twin prime conjecture. Sub-targets that would constitute genuine progress, in increasing strength: (i) S ∉ ℤ[1/2]; (ii) (P) restricted to one b (equivalently: δ at CPAP-3 sites is not eventually in (1/b)ℤ); (iii) a pair-correlation bound for aftermaths at repeated patterns strong enough for H-sep. False starts refuted along the way, so nobody retries them: growth/statistics-only proofs (C8), the Maynard-cluster smallness route (C19), the J = 1 squeeze for odd b ≥ 7 (C11), and "typicality" run-squeezes for large J (C13–C15).

## 12. Deliverable classification (per the dossier's ranking)

1. **Unconditional results:** structural lemmas C1–C5, C7, C9, C10 (computer-assisted exact), C13, C14; no unconditional progress on irrationality itself — the problem stays open (C22).
2. **Precise conditional theorems:** Theorems A ((L\*)), B ((P)), C (H-sep), each with the exact hypothesis, the parity-sharpened thresholds, and the exact statement of where HL-uniformity fails to reach them (C18).
3. **New reductions/equivalences with proof:** master criterion & doubling-map dictionary (C4, C5), two-window pigeonhole reduction (C17), parity refinement (C7), primorial obstruction with corrected calibration (C13–C15), dyadic δ<4 reduction (C20).
4. **Rigorous refutations of natural strategies:** vacuity theorem (C8), J = 1 route for b ≥ 7 (C11), cluster route (C19), and the correction of the dossier's own Cramér-headroom claim (C15).

Numerical items (§9) are labelled throughout as finite verification/calibration.
