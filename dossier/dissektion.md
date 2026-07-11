# Dissektion -- thread erdosproblems.com/251 and [ScPu11] (contamination class C)

Date: 2026-07-11. Source: full comment thread (4 comments, screenshot provided
by operator) plus [ScPu11] full text (arXiv:1105.1451). This document must NOT
reach stage-1a/1a0 runs.

## 1. Scoring of the pre-registration (see ledger.yaml, BET-20260711-01..03)

- Content class: outcome H2 -- the variant resolved is Erdős's g_1...g_n
  generalization, NEGATIVELY, by construction. Object predicted correctly,
  direction (disproof vs conditional proof) not anticipated.
  Categorical Brier 0.71 vs uniform baseline 0.80: modest edge.
- Meta bet "writeup contains a delta-like tail object" (p = 0.60): TRUE.
  Kovač's recursion c_{n+1} = c_n g_n - p_n IS the tail recursion (I2) in
  base g_n. Brier 0.16. Grading ambiguity acknowledged and resolved by strict
  textual reading.
- Meta bet "cites Zhang-Maynard or BHP" (p = 0.50): FALSE, elementary
  construction. Brier 0.25.

## 2. The four comments

1. T. Tao, 2025-10-07 (paraphrase): partial summation reduces the problem to
   the irrationality of sum (p_{n+1} - p_n)/2^n. A sufficiently quantitative
   AND uniform version of the prime tuples conjecture might resolve it, if it
   gives statistical control over windows of about log log n consecutive
   prime gaps (typical size about log n), enough to rule out periodicity of
   the binary expansion. Shannon entropy theory suggested as a possible tool.
2. Alfaiz, 2026-04-15: pointer to [ScPu11], "Theorem 2 seems related".
3. V. Kovač, 2026-04-15: negative answer to the LAST conjecture on the page
   (the g_1...g_n generalization) via telescoping: choose positive integers
   c_n with c_{n+1} = c_n g_n - p_n, i.e. c_{n+1} == -p_n (mod c_n), keep c_n
   slowly but steadily growing, set g_n = (c_{n+1} + p_n)/c_n; the series
   telescopes to an integer. ChatGPT 5.4 Pro worked out proof and writeup with
   minimal orchestration. Notes Erdős may have intended increasing g_n.
4. N. Sothanaphan, 2026-04-15: standard verification found no issues; the
   construction is somewhat stronger than g_n = o(p_n); asks what the BEST
   provable statement is.

Community status boxes: nobody working on the problem, nobody formalizing.

## 3. Findings, ranked

### 3.1 Tao's comment is the treasure (frame convergence)

Same reduction as (I1), same conditional source (uniform quantitative tuples),
same window scale: log log n consecutive gaps matches the runde0 squeeze
threshold (T) J >~ log2 log n exactly. Runde 0 is externally validated in
frame and scale; PRIORITY of the idea is Tao's (Oct 2025). Our niche is
EXECUTION: nine months later nobody has carried it out. Tao's addition we did
not have: the ENTROPY route -- show the digit process has positive entropy,
hence cannot be eventually periodic. More robust than the squeeze (typical
behavior instead of a specific configuration), but Lean-hostile (mathlib
entropy support is thin).

### 3.2 The variant is an adversarial-freedom exploit

The construction weaponizes exactly the vacuity observed in runde0 Autopsy 1:
"integrality propagates, so no leverage against the adversary" becomes "let
the adversary run the propagation and win". Zero carry content, zero gap
content; the difficulty of the original is bypassed, not dented.
Meta-lesson for problem selection: a wiki "variant solved (yellow)" flag can
systematically overstate proximity to the original.

### 3.3 Sothanaphan's question and the bounded-g sketch (UNVERIFIED)

Ten-minute sketch: with an adaptive choice keeping c_n in a band of width
comparable to p_n, even BOUNDED g_n (values in {2,...,5}) may admit rational
sums via the same telescope; the covering argument over the band needs care
(the candidate values 2 c_n - p_n, 3 c_n - p_n, ... are spaced c_n apart).
If it holds, the true dividing line in the generalization is ADAPTIVITY vs
fixed structure, not growth. Status: UNVERIFIED, item A4.

### 3.4 [ScPu11] is not a novelty threat; it is the engine blueprint

J.-C. Schlage-Puchta, "The irrationality of some number theoretical series",
Acta Arith. 126 (2007) 295-303, arXiv:1105.1451. Contents:

- Theorem 1 / Proposition 1: the numbers sum [n^lambda]/n! for non-integer
  lambda, together with 1 and e, are Q-linearly independent; image properties.
- Theorem 2 (the one flagged in the thread): digit CONCATENATION. If
  alpha = 0.f(1)f(2)f(3)... in base b (b not a proper power), f nondecreasing,
  f(n+1)/f(n) ~ g(n) with g nondecreasing and g(n+1)/g(n) -> 1, and alpha is
  rational, then g -> c, c is a power of b, and f(n+1) = c f(n) + O(1).
  Mahler/Bundschuh lineage. Relevance: this is the CARRY-FREE projection of
  our problem (digit blocks do not overlap). It confirms the runde0
  calibration: the entire difficulty of #251 sits in the carries.
- Theorem 3: 1, S_0, S_1, S_2, ... are Q-linearly independent, where
  S_k = sum p_n^k / n!. Historical catch: per ScPu11, Erdős proved only k = 1
  in print; the problem page attributes all k to [Er58b]. Correction candidate
  for a later thread post.
- Proof machinery of Theorem 3 (the blueprint):
  (a) rationality forces near-integrality of leading tail terms at every n
      (factorial base: per-step decay 1/n, so O(1) many gaps suffice);
  (b) recursive CROSS-ELIMINATION over consecutive n (F^{(i+1)} built from
      F^{(i)}(n) and F^{(i)}(n+1) with polynomial coefficients in the gaps)
      cancels leading growth; Lemma 5 (algebra) keeps the residue nontrivial;
  (c) Lemma 4 (via Selberg sieve upper bounds, Lemma 3): no nonzero polynomial
      in consecutive gaps vanishes for a positive proportion of n --
      an UNCONDITIONAL anti-conspiracy statement for O(1)-size gap windows;
  (d) Lemma 6 (van der Corput + PNT): discrepancy bound contradicting the
      forced near-integrality.

### 3.5 Why base 2 is harder, in one line

Per-step decay 1/2 instead of 1/n means the near-integrality condition at
height n involves windows of ~ log2 log n gaps (runde0 (T)) instead of O(1),
so the ScPu11 engine needs sieve/tuples control UNIFORM in window size
k ~ log log n -- exactly Tao's phrase "sufficiently quantitative and uniform".
Note also: Selberg gives upper bounds; the squeeze and entropy routes need
EXISTENCE of patterns (lower bounds), i.e. full Hardy-Littlewood input.

## 4. Route table after dissection

A. CPAP squeeze (runde0): narrow, Lean-friendly. Conditional formalization
   runs through this.
B. Entropy / statistical (Tao): robust, informal-first, Lean-hostile.
D. Elimination-uniformization (ScPu11 scheme in base 2): blueprint exists;
   main open engineering: uniformity in k ~ log log n, lower-bound input.
(C from runde0, the variant ladder, is retired to calibration duty.)

## 5. Updated bets

See ledger.yaml BET-20260711-04..07: informal conditional proof in round 1
p = 0.65; Lean-verified same round p = 0.45; implication already exists
p = 0.10; unconditional progress in 4 weeks p = 0.03.
