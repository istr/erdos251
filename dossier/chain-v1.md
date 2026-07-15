# Conditional irrationality of S = sum p_n/2^n -- consolidated chain, v1.2

STATUS: conditional theorem. Hypotheses A and B below are open, standard-
shaped conjectures; everything else is proved here or cited as classical.
This document consolidates round 1 of the erdos251 experiment: primary
source is the fable-5 stage-1b chain (sha e5f818af...c7a6560), which
survived blind cross-review (gpt-5.6-sol, "SOUND with repairable issues",
0.94, sha 4a2e2eab...6329d209) with zero fatal findings; all seven listed
repairs are EXECUTED here (mapping in section 9). Design rationale absorbs
the fatal finding of review 2 (fresh fable-5 on the gpt-web chain, sha
50efe768...236e64): no clause of this document demands relative counting
accuracy at consecutive-gap level, where model masses drop below 1.
Consolidation: steering (Claude Fable 5), 2026-07-12; amendments v1.1 and
v1.2 2026-07-15 (changelog in section 9; ANN-20, ANN-22). Erdos #251.

## 1. Main statement

Notation: p_1 = 2 < p_2 = 3 < ... are the primes, g_n = p_{n+1} - p_n,
S = sum_{n>=1} p_n 2^{-n}, and for H = {0 = h_0 < h_1 < ... < h_k} a set of
even integers, pi_H(x) = #{p <= x : p + h_i prime for all i},
M_H(x) = S(H) x / (ln x)^{k+1} with S(H) the singular series. H is
admissible if for every prime q the offsets do not cover all residues
mod q.

HYPOTHESIS A (uniform two-sided tuple counts). There exists x_A such that
for all x >= x_A and every admissible H with k+1 <= 4 lnln x and
h_k <= (ln x)^3:
    (1/2) M_H(x) <= pi_H(x) <= 2 M_H(x).
Design note (review-2 lesson): all in-budget masses satisfy
M_H(x) >= x^{1-o(1)} >> 1 by Lemma 4.1, so a fixed two-sided factor is
integrality-safe. A relative-error demand on CONSECUTIVE-gap counts would
be unconditionally false (single-gap words near (ln x)^3 have model mass
e^{-(1+o(1))(ln x)^2} < 1, leaving no admissible integer count); this
document therefore DERIVES consecutiveness (Lemma 4.3) instead of assuming
counts for it. If one prefers an error form, |pi_H - M_H| <= (1/3)M_H + x^t
with fixed t < 1 also suffices verbatim.

HYPOTHESIS B (Cramer-Granville). There exist C_g >= 1 and nu_B such that
g_nu <= C_g (ln p_nu)^2 for all nu >= nu_B (C_g >= 1 is WLOG by
monotonicity; section 5 takes log2(4 C_g)).

THEOREM. Assume A and B. Then S is irrational, and so is the 0-indexed
variant sum_{n>=0} (Nat.nth Prime n)/2^n = 2S.

Remark on strength (review-1 P1): the package is NOT circular, but clause
B is a global pointwise gap bound, materially stronger than a pure tuple
hypothesis. The sharpest known weakening target is the two-word variance
estimate of section 8.3.

## 2. Elementary layer

LEMMA 2.1 (convergence; repair R1). p_n <= C_0 n ln(n+2) for all n, with an
absolute C_0 (Chebyshev; classical, e.g. Hardy-Wright, An Introduction to
the Theory of Numbers, Thm 8 area; citation verification tracked in
item-0004). Hence sum p_n 2^{-n} converges absolutely, as do all tails
u_n = sum_{k>=1} p_{n+k} 2^{-k}, and
    delta_n := u_n - p_{n+1} = sum_{j>=1} g_{n+j} 2^{-j},
    delta_{n+1} = 2 delta_n - g_{n+1},  delta_n >= 2 for n >= 1.
(The absolute convergence licenses the rearrangement defining delta_n;
the bound p_n <= 2^n alone would not -- review-1 A04/A12.)

LEMMA 2.2 (block identity). For T >= 1:
delta_n = sum_{i=1}^T g_{n+i} 2^{-i} + 2^{-T} delta_{n+T}.

LEMMA 2.3 (lattice and parity; repair R2). Suppose S = a/(2^s b) with
a, s, b positive integers, b odd, and WLOG s >= 1 (the representation need
not be reduced: a/(2^0 b) = 2a/(2^1 b)). Then b delta_n is an integer for
all n >= s, and an EVEN integer for all n >= s+1.
Proof. 2^n b S = 2^{n-s} a and b sum_{j<=n} p_j 2^{n-j} are integers, so
b u_n and b delta_n = b u_n - b p_{n+1} are integers for n >= s. Parity:
for n >= s, b delta_{n+1} = 2(b delta_n) - b g_{n+1}, and g_{n+1} =
p_{n+2} - p_{n+1} is a difference of odd primes since n+1 >= s+1 >= 2,
hence even; b odd makes b g_{n+1} even. QED
(For s = 0 the step n = 0 would use g_1 = 1, which is odd; the WLOG
removes the edge -- review-1 A17.)

LEMMA 2.4 (quantization). If n, m >= s+1 share a common gap prefix,
g_{n+i} = g_{m+i} for 1 <= i <= J, then
b(delta_{n+J} - delta_{m+J}) is an integer multiple of 2^{J+1}.
Proof. Subtract Lemma 2.2 at n and m (prefix sums cancel):
delta_n - delta_m = 2^{-J}(delta_{n+J} - delta_{m+J}). Multiply by b and
use Lemma 2.3 (even lattice at n, m >= s+1). QED

LEMMA 2.5. An integer multiple of 2^{J+1} of absolute value < 2^{J+1}
is 0.

## 3. Fork-merge and its contradiction

DEFINITION 3.1 (FM). There exist sequences n_r, m_r, J_r >= 1, K_r >= 1,
even gamma_r >= 2, such that with L_r = J_r + 2 + K_r:
(FM-P) g_{n_r+i} = g_{m_r+i} for 1 <= i <= J_r;
(FM-F) g_{n_r+J_r+1} = g_{m_r+J_r+1} + gamma_r and
       g_{n_r+J_r+2} = g_{m_r+J_r+2} - gamma_r;
(FM-S) g_{n_r+J_r+2+i} = g_{m_r+J_r+2+i} for 1 <= i <= K_r;
(FM-1) delta_{n_r+L_r} <= 2^{K_r} and delta_{m_r+L_r} <= 2^{K_r};
(FM-2) (gamma_r + 4)/2^{J_r} -> 0;
(FM-3) min(n_r, m_r) -> infinity.
The statement is b-free; exact-hit immunity is structural (step 4 below
USES exact equality; strictness comes from delta >= 2, not from any
"tail differs from an integer" clause -- confirmed by both reviews, P7).
[v1.1: the v1.0 order requirement n_r < m_r is dropped -- it conflicted
with the section-6 name swap (ANN-12 flag 1); no step of Theorem 3.2
uses an order, and FM-F with gamma_r >= 2 already forces n_r != m_r.]

THEOREM 3.2 (FM implies irrationality). Assume FM. Then S is irrational.
Proof. Suppose S = a/(2^s b), b odd, s >= 1 (Lemma 2.3). By (FM-2) and
(FM-3) choose r with min(n_r, m_r) >= s+1 and (gamma+4)/2^J < 8/b, i.e.
b(gamma+4)/4 < 2^{J+1}; write n, m, J, K, gamma, L = J+2+K.
1. End tails. By (FM-1) and delta >= 2 (Lemma 2.1):
   |Delta_end| := |delta_{n+L} - delta_{m+L}| <= 2^K - 2 < 2^K.
2. Fork decomposition. By Lemma 2.2 at n+J and m+J, using (FM-F), (FM-S):
   delta_{n+J} - delta_{m+J} = gamma/2 - gamma/4 + 2^{-(K+2)} Delta_end
                             = gamma/4 + 2^{-(K+2)} Delta_end.
3. Fork closeness. |delta_{n+J} - delta_{m+J}| < gamma/4 + 1/4 =
   (gamma+1)/4 < (gamma+4)/4.
4. Lattice lock. Lemma 2.4 puts b(delta_{n+J} - delta_{m+J}) in
   2^{J+1} Z; its absolute value is < b(gamma+4)/4 < 2^{J+1}; Lemma 2.5
   forces delta_{n+J} = delta_{m+J}.
5. Contradiction. Then gamma/4 = -2^{-(K+2)} Delta_end, so
   |Delta_end| = gamma 2^K >= 2^{K+1}, contradicting step 1. QED

## 4. Counting layer (conditional on A; classical citations)

Throughout, l = ln x. "Consecutive realization of a gap word w =
(w_1,...,w_L) at n" means g_{n+i} = w_i for all i, equivalently: the L+1
primes p_{n+1}, ..., p_{n+L+1} occupy exactly the point set of w with no
prime in between.

LEMMA 4.1 (singular series lower bound). For admissible H of even offsets,
|H| = k+1, S(H) >= exp(-C k ln(k+2)). Consequently, in the budget of
Hypothesis A, M_H(x) >= x exp(-C k ln(k+2) - (k+1) lnln x) = x^{1-o(1)}.
Proof sketch (review-1 A36-A40): local factors at p <= k+2 are >= 1/p by
admissibility; at k+2 < p <= 2(k+1) crude bounds give a factor e^{-O(k)};
at 2(k+1) < p <= D the exponential estimates apply since nu/p < 1/2; at
p > D all offsets are distinct mod p and log-factors sum to o(k). Uses
Mertens' theorems (classical: Mertens 1874; Rosser-Schoenfeld 1962) --
repair R3: these are now CITED, not asserted bare; exact-constant
verification tracked in item-0004. QED-sketch

LEMMA 4.2 (one-point extension sum; v1.1). For any fixed kappa >= 1 there
is C_2 = C_2(kappa) such that for admissible H as above with span
D = h_k <= kappa k ln(k+2): the sum over even t in (0, D), t not in H,
H u {t} admissible, of S(H u {t})/S(H) is <= C_2 k (ln(k+2))^2.
Proof sketch (review-1 A41-A43): the local ratio at non-colliding p is
(1-(nu+1)/p)/((1-nu/p)(1-1/p)) <= 1 - (p-1)^{-2} < 1; colliding primes
p > 2(k+1) divide some t - h_i, each difference is <= D, so there are
at most (k+1) ln D / ln(2k+2) = O_kappa(k) of them, their reciprocals
sum to O_kappa(1) (each p - 1 > 2k+1), and their product of local
factors p/(p-1) is e^{O_kappa(1)}; primes <= 2(k+1) contribute
<= C ln(k+2) by Mertens; there are
<= D/2 <= (kappa/2) k ln(k+2) values of t, now BY HYPOTHESIS. QED-sketch
[v1.2: the earlier sketch asserted the kappa-uniform bounds "number
<= 3k" and "product <= e^2"; both FAIL for large fixed kappa
(H = {0, 10014}, t = 10010 = 2*5*7*11*13 has four colliding primes at
k = 1; a highly composite t drives the collision product past e^2 --
prod_{5<=p<=10^6} p/(p-1) = 8.202... > e^2 = 7.389...). Found by the
blind re-review R2, steering-re-executed; the lemma STATEMENT is
unaffected. ANN-22.]
[v1.1/F2: the span hypothesis is NECESSARY, not cosmetic. For H = {0, D}
(k = 1) every admissible even t has ratio >= 1.2 (the p = 2 factor alone
is 2) and there are ~D/2 such t, so the sum grows like D against a
D-free right side; the unrestricted v1.0 claim is FALSE. Surfaced by the
item-0014 skeleton pass and steering-verified numerically (ANN-20);
review-1 A41-A43 had passed the v1.0 form.]

LEMMA 4.3 (consecutive lower bound; the transfer; v1.1). Let w be a gap
word whose point set H(w) is admissible, |H(w)| = L+1 <= 4 lnln x - 1,
span <= kappa L ln(L+2) for a fixed kappa >= 1 (hence far inside the
(ln x)^3 budget of A). Under Hypothesis A, for all large x the number of
consecutive realizations of w with p_{n+1} in (sqrt x, x] is
    N_cons(w; x) >= (1/4) M_{H(w)}(x) >= 1.
Proof. A realization of the point set fails to be consecutive iff some
extra prime sits at an interior even offset t (odd offsets and p > D make
non-even positions composite for p > x^{1/2} -- review-1 A44). Inadmissible
extensions have count 0 unconditionally: a covering prime q <= L+2 < sqrt x
would have to divide a prime > sqrt x. Admissible extensions are in the
budget of A (L+2 points, +1 -- repair R5: the cardinalities are L+1 and
L+2, and the budget constant 4 in A leaves slack; 3 would asymptotically
suffice). Union bound (exact, first Bonferroni level):
N_cons >= pi_H(x) - sum_t pi_{H u t}(x) - pi_H(sqrt x)
       >= (1/2) M_H - 2 sum_t M_{H u t} - sqrt x
       >= (1/2) M_H - 2 C_2(kappa) k (ln(k+2))^2 M_H / l - sqrt x
       >= (1/4) M_H,
using Lemma 4.2 (k = L; the span hypothesis here is exactly 4.2's),
M_{H u t} = S(H u t) x/l^{k+2}, and M_H >= x^{1-o(1)} >> sqrt x
(Lemma 4.1). QED
[v1.1/F2: the span hypothesis is narrowed from the v1.0 form
span <= (ln x)^3. The wide form is unprovable by this route (Lemma 4.2's
sum genuinely grows with the span) and heuristically false outright for
span >> ln x, where consecutive realizations carry a Cramer-type
e^{-span/ln x} thinning absent from M_H. Section 5(iii) supplies exactly
the narrow form.]
[EXPLICIT one-line lemma per review-2 P2, stated here for the record even
though this architecture does not need a T_x identity: every start index
carries exactly one length-L gap word; only budget filters remove indices.]

LEMMA 4.4 (tail bound from B). Under Hypothesis B there is nu_1 with
delta_nu <= 3 C_g (ln p_nu)^2 for all nu >= nu_1.
Proof. g_{nu+j} <= C_g (ln p_{nu+j})^2, and p_{nu+j} < 2^j p_nu (Bertrand,
classical), so ln p_{nu+j} < ln p_nu + j; then
delta_nu <= C_g sum_j (ln p_nu + j)^2 2^{-j}
         <= C_g (2 (ln p_nu)^2 + 2 * 6) <= 3 C_g (ln p_nu)^2
for (ln p_nu)^2 >= 12, using (a+b)^2 <= 2a^2 + 2b^2 and
sum j^2 2^{-j} = 6. QED

## 5. The deletion construction

Fix x large. Set
    K = ceil(log2(4 C_g) + 2 log2 ln x),   J = ceil(4 log2(K + 20)),
    L = J + 2 + K,   H_x = 4 C_g (ln x)^2  (so 2^K >= H_x).
Let q_0 < q_1 < ... < q_{L+1} be the first L+2 primes exceeding L+3, put
i_0 = J + 1 (v1.1; interior with slack: 1 <= i_0 and i_0 + 1 <= L since
J, K >= 1), gamma = q_{i_0+1} - q_{i_0} (even),
and define the two point sets
    A  = {q_0, ..., q_{L+1}} minus {q_{i_0+1}},
    A' = {q_0, ..., q_{L+1}} minus {q_{i_0}},
with gap words w, w' (each of length L); the 0-based point sets that
Lemma 4.3 and Hypothesis A receive are H(w) = A - q_0 and
H(w') = A' - q_0 (translation changes neither gaps nor
admissibility; re-review R2, v1.2). Then:
(i) w and w' share the length-J prefix and the length-K suffix, and
their middle two entries differ by (-gamma, +gamma) in the natural
order (w, w'); section 6 swaps the names to give FM-F's (+gamma,
-gamma) orientation -- direct computation (review-1 A53; orientation
corrected v1.2, re-review R2).
[v1.1/F1: i_0 corrected from the v1.0 value J + 2, under which the words
share a length-(J+1) prefix and only a length-(K-1) suffix, the fork
sits one slot late, claim (i) fails (at K = 1 the shared suffix even
collapses to 0), and FM-1 downstream loses a factor 2 that section 6
cannot supply (its tails are <= H_x <= 2^K only). With i_0 = J + 1
claim (i) is true as written; verified numerically over several (J, K)
pairs (ANN-20). Review-1 A53 had passed the v1.0 value.]
(ii) Both point sets are admissible: for p <= L+2 the residue class of 0
is unoccupied before translation (all q_j > L+3 > p), and for p > L+2
there are only L+1 < p points (review-1 A54).
(iii) span <= q_{L+1} - q_0 <= C_1 L ln L, C_1 >= 1 fixed (Chebyshev
upper bound on
p_{2L+4}; classical), hence gamma <= C_1 L ln L and, since
L <= 2(K+20) and ln L <= K+20 for large x,
    (gamma + 4)/2^J <= 3 C_1 / (K+20)^2 -> 0.
(iv) Budgets: the words have L + 1 points with
L + 1 = (2/ln 2) lnln x + O(lnlnln x) < 3 lnln x eventually, meeting
Lemma 4.3's L + 1 <= 4 lnln x - 1 with room; one-point extensions then
have L + 2 <= 4 lnln x; span <= (ln x)^3 easily (the operative span
bound is (iii)).

## 6. Assembly: proof of the Theorem

Assume A and B. For each large x build w, w' as in section 5. By
Lemma 4.3 (span hypothesis met with kappa = C_1 via section 5(iii)) there
are consecutive realizations of w at some n_x and of w'
at some m_x, both with anchor prime in (sqrt x, x]; the words differ at
position J+1, so n_x differs from m_x; swap names so the (+gamma, -gamma)
orientation matches (FM-F). Conditions:
(FM-P/F/S) hold by section 5(i).
(FM-1): the end-tail indices n_x + L, m_x + L have anchor primes <= x
times e^{o(1)}, so by Lemma 4.4 (B) both end tails are
<= 3 C_g (ln x + o(ln x))^2 <= H_x <= 2^K for large x -- pointwise, no
site selection needed.
(FM-2): section 5(iii). (FM-3): anchors exceed sqrt x, so indices tend to
infinity.
Running x through any sequence tending to infinity yields FM;
Theorem 3.2 concludes. For the 0-indexed Lean target, irrationality of S
gives irrationality of 2S. QED

## 7. What is NOT claimed (repairs R4, R7)

- No logical independence of B from A is claimed. What is true: the naive
  inclusion-exclusion route from tuple counts with polylogarithmic error
  savings does not reach pointwise gap bounds of Cramer-Granville type
  (exponent bookkeeping; review-1 A65). Whether some other derivation of B
  from an A-type package exists is open.
- No claim that the Lean skeleton compiles or that the analytic layer is
  "routine bookkeeping". Section 8.2 is an interface sketch; the real
  formalization is item-0002.
- Hypothesis A's truth and Hypothesis B's truth are open; A is
  standard-shaped (uniform Hardy-Littlewood with modest window growth),
  B is the classical Cramer-Granville conjecture.

## 8. Remarks and open targets

8.1 Kernel ordering (round-1 synthesis). The residual statistical content
of ALL round-1 architectures is one kernel in ordered formulations:
B (pointwise gaps) > per-cylinder tail moments > two-word variance;
the model-side entropy clause (Q2 of the gpt-web arm) is orthogonal and
plausibly provable, but this consolidation does not need it.
8.2 Lean interface (repair R6). Target theorem on 2S with thresholds
recomputed for the 0-indexed sum; hypothesis structures HLQuantA,
CramerGranville to be DEFINED, not stubbed; skeleton names retained:
delta_block, rational_delta_eventually_lattice,
repeated_block_quantization, fork_merge_contradiction,
erdos_251_of_small_tail_fork_merge. No `True` placeholders.
8.3 Sharpest weakening target: replace B by a second-moment bound for
delta over the consecutive realizations of ONE fixed word (two-word
variance); this would move the package to pure tuple-type statements.
8.4 The empirical layer (primes below 3e7) is consistent with abundance
of the constructed configurations; finite exclusions on record:
denominator > 10^298; no denominator 2^s b with s <= 1,857,459 and odd
b <= 99,999.

## 9. Provenance and repair mapping

Sources: fable-5 1b chain e5f818af...c7a6560 (primary); reviews
4a2e2eab...6329d209 (object: this chain's source) and 50efe768...236e64
(object: gpt-web chain 32128bc2...ea6b10, fatal Q1 finding absorbed as
design rationale in section 1); gpt-iso chain d60b460c...c8eefa
(architecture comparison). Repairs executed: R1 -> Lemma 2.1;
R2 -> Lemma 2.3 (wlog s >= 1); R3 -> citations in Lemmas 4.1/4.2 and
Bertrand/Chebyshev uses (verification item-0004); R4 -> section 7;
R5 -> Lemma 4.3 and section 5(iv); R6 -> section 8.2; R7 -> sections 1
and 7. Steering verification: complete for sections 2, 3, 6; section 5
was CLAIMED complete in v1.0 yet contained F1 (see changelog) -- the
claim itself was an overclaim, logged as blind-spot register entry 4;
sketch-level with reviewer concurrence for 4.1/4.2. Blind-review trail
and adjudications: dossier/triage-1b.md; append-only decisions:
ledger.yaml.

AMENDMENT v1.1 (2026-07-15, ANN-20). Both F-findings were surfaced by
the item-0014 statement-skeleton pass and steering-verified numerically
before amending; review-1 had passed both v1.0 forms.
- F1: section 5 deletion index corrected to i_0 = J + 1 (v1.0: J + 2,
  which broke claim (i) by one slot -- prefix J+1, suffix K-1 -- and
  cost FM-1 a factor 2 that section 6 cannot supply).
- F2: span hypotheses added. Lemma 4.2 now requires
  D <= kappa k ln(k+2) (the unrestricted form is FALSE: H = {0, D}
  family, sum ~ D/2); Lemma 4.3 now requires span <= kappa L ln(L+2)
  (the (ln x)^3 form is unprovable by this route and heuristically
  false under Cramer-type thinning). Section 6 instantiates kappa = C_1
  via section 5(iii).
- ANN-12 flag 1 resolved: Definition 3.1's order requirement n_r < m_r
  dropped (conflicted with the section-6 name swap; nothing uses it).
- ANN-12 flag 2 resolved: vestigial C_A removed from Hypothesis A,
  re-syncing the text with the frozen Lean HLQuantA, which never bound
  it. The one remaining Lean-side statement flag (unused hb : 0 < b in
  repeated_block_quantization, ANN-18) stays deferred to a Lean
  statement-unfreeze batch after sign-off.

AMENDMENT v1.2 (2026-07-15, ANN-22). Source: blind re-review R2
(anchor-stripped object, computation-mandatory payload review_2a;
verdict SOUND with repairable issues, 0.90, zero fatal); all findings
steering-re-executed before amending. Repairs:
- Lemma 4.2 sketch: the kappa-uniform collision bounds ("<= 3k",
  "product <= e^2") replaced by O_kappa(k) / e^{O_kappa(1)} with the
  reviewer-supplied argument; counterexamples recorded in the lemma
  note. Statement unaffected (exhaustive small search consistent).
- Section 5 claim (i): fork orientation corrected to (-gamma, +gamma)
  in the natural word order; section 6's name swap supplies FM-F.
- Section 5: explicit 0-based normalization H(w) = A - q_0 for the
  handoff to Lemma 4.3 / Hypothesis A.
- Hypothesis B: C_g >= 1 made explicit (WLOG; section 5 takes
  log2(4 C_g)). Section 5(iii): C_1 >= 1 fixed, so section 6's
  kappa = C_1 is licit.
- Section 5(iv): base/extension cardinalities stated precisely
  (L + 1 word points; L + 2 with the extension).
Not executed by design: full write-ups of the 4.1/4.2 sketches --
their honest closure is the Lean counting layer (item-0014 path),
which supersedes prose sketches.
