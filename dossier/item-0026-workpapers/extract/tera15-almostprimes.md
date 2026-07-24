# EXTRACTION: Joni Teravainen, "Almost primes in almost all short intervals"

Source (only evidence base): /home/istr/pro/erdos251/dossier/1510.06005v2.pdf
sha256 05cc130e898b1e6b60bc096713eb67f83e2d4c0e96bc715797338817d9a52ddb
(operator-verified; re-verified this session).
arXiv:1510.06005v2 [math.NT] 20 Apr 2016. Author: Joni Teravainen
(Teravainen), Department of Mathematics and Statistics, University of
Turku, 20014 Turku, Finland; Email: joni.p.teravainen@utu.fi (p. 40).
40 pages. Creator: LaTeX with hyperref; Producer: pdfTeX-1.40.12;
CreationDate Thu Apr 21 03:09:02 2016 CEST. No journal reference printed
on the paper (reference [15] Matomaki-Radziwill is marked "To appear in
Ann. of Math."). Grant footnote (Section 1.1, p. 4): "While working on
this project, the author was supported by the Vilho, Yrjo and Kalle
Vaisala foundation of the Finnish Academy of Science and Letters." The
author thanks his supervisor Kaisa Matomaki and the referee (p. 4).

Front-matter identification CONFIRMED against steering: author "Joni
Teravainen", title "Almost primes in almost all short intervals",
arXiv:1510.06005v2. No deviation.

---

## Transcription conventions

ASCII only. Diacritics transliterated: Teravainen (Terajvajinen ->
Teravainen), Matomaki, Radziwill, Yildirim (Yildirim), Vaisala,
Vinogradov, Halasz, Mobius. Mathematics in LaTeX-like ASCII. Anchors are
the paper's own numbering (Theorem 1-5, Lemma 1-16, Proposition 1-8,
equations (1)-(16), Remark 1-10, Sections 1-6); printed page number =
PDF page number throughout (verified: printed p. N is PDF page N), given
as a secondary aid. Everything above COMMENTARY is EXTRACTION; anything
evaluative appears only in COMMENTARY.

Symbol table (every non-obvious glyph):

- E_k : the set of positive integers having exactly k (distinct, in the
  theorem conclusions) prime factors; "product of exactly k distinct
  primes". P_k : products of no more than k primes.
- log_k X : the k-th iterated logarithm (log applied k times). "Here
  log_l is the l-th iterated logarithm" (Theorem 2, p. 2). NOT log base
  k. So log_k X in (1) = the k-fold iterate.
- log^c X = (log X)^c ; log^{3.51} x = (log x)^{3.51}. loglog x = log
  log x = log_2 x (second iterate).
- P_1, ..., P_{k-1} : the prime-support thresholds defined in Theorem 4.
- p, q, p_i, q_i : primes (reserved). d, k, l, m, n : positive integers.
- nu(.) : number of DISTINCT prime divisors. mu(.) : Mobius. Lambda(.) :
  von Mangoldt. d_r(m) : number of solutions of a_1...a_r = m in
  positive integers. omega(.) : Buchstab's function.
- P(z) = prod_{p<z} p ; S(A, P, z) counts the numbers in A coprime to
  P(z) (sieve function).
- eps (epsilon) : "always small enough but fixed" (p. 4). C_1, C_2, ... :
  "unspecified, positive, absolute constants" (p. 4). C_k : a positive
  constant depending on k (Theorem 2).
- n ~ X means X <= n < 2X (p. 4). 1_S : indicator of the set S.
- << , >> : Vinogradov (<< is O(.)); X asymp Y (paper writes "X ~~ Y",
  the two-sided <<>>) "is shorthand for X << Y << X" (p. 4). Here I write
  "asymp" for that two-sided relation and "~" only for genuine asymptotic
  equality (as in the abstract's "asymptotically equal").
- sigma : real part of s = sigma + it. zeta(s), zeta'(s) : Riemann zeta
  and derivative. "zeta sums": partial sums of zeta or zeta' of the form
  sum_{n~N} n^{-s} or sum_{n~N} (log n) n^{-s} (p. 4).
- alpha_1, alpha_2 : exponents controlling large-value sets of Dirichlet
  polynomials (Sections 4, 6; Remark 10). F(s), M_i(s), N_i(s), P(s),
  K(s) : Dirichlet polynomials. Sigma_1(h), Sigma_2(h), Sigma_3(h) : the
  three sums in the proof of Theorem 5 (Section 6.2-6.3).
- psi(x) : an arbitrary function tending to infinity (in cited P_k
  results). lambda (Poisson intensity) in the heuristic on p. 2.

Displays (1), (2) and Remark 10's fraction were scrambled in both
pdftotext -layout and -raw layers; they are transcribed from
pdftoppm -r 200 page images of printed pages 2, 3, 39 and flagged
[TRANSCRIPTION-UNSURE, resolved-by-image]. Plain prose came from the
-layout text layer.

---

## 1. FRONT MATTER and ABSTRACT (p. 1), verbatim

Title (p. 1): "Almost primes in almost all short intervals". Author
(p. 1): "Joni Teravainen".

Abstract (p. 1), verbatim:

> "Let Ek be the set of positive integers having exactly k prime
> factors. We show that almost all intervals [x, x + log^{1+eps} x]
> contain E3 numbers, and almost all intervals [x, x + log^{3.51} x]
> contain E2 numbers. By this we mean that there are only o(X) integers
> 1 <= x <= X for which the mentioned intervals do not contain such
> numbers. The result for E3 numbers is optimal up to the eps in the
> exponent. The theorem on E2 numbers improves a result of Harman, which
> had the exponent 7 + eps in place of 3.51. We also consider general Ek
> numbers, and find them on intervals whose lengths approach log x as
> k -> infinity."

Note: the abstract states the E3 window as log^{1+eps} x; the E3
Theorem 1 (below) states the sharper explicit window
(loglog x)^{6+eps} log x, which is <= log^{1+eps} x. Both are the
author's; see C-note and FLAGS.

---

## 2. SECTION 1 (Introduction): the five theorems, verbatim

### 2.1 Context sentences (p. 1-2), verbatim (selected)

> "Since Wolke's work [21], the essential question has been minimizing
> the number c such that almost all intervals [x, x + log^c x] contain
> an Ek number, meaning that all but o(X) such intervals with integer
> x in [1, X] contain such a number. Wolke showed in 1979 that the value
> c = 5 * 10^6 is admissible for E2 numbers. This was improved to
> c = 7 + eps for E2 numbers by Harman [9] in 1982." (p. 1)

> "To the author's knowledge, Harman's exponent for E2 numbers was the
> best one known also for Ek numbers with k >= 3." (p. 1)

> "There is however a crucial difference between Ek and Pk numbers, since
> the Ek numbers are subject to the famous parity problem, and hence
> cannot be dealt with using only classical combinatorial sieves, which
> are the basis of the arguments on Pk numbers. Therefore, the Ek numbers
> are also a much closer analog of primes than the Pk numbers." (p. 1)

> "For E2 numbers, under the density hypothesis, Harman's argument from
> [9] would give the exponent c = 3 + eps." (p. 2)

> "In this paper, we establish the exponent c = 1 + eps for E3 numbers
> and the exponent c = 3.51 for E2 numbers. Our results for E2, E3 and
> Ek numbers are stated as follows." (p. 2)

Footnote 1 (p. 1), verbatim:

> "In fact, introducing into Harman's argument the widest known density
> hypothesis region sigma >= 25/32, due to Bourgain [2] from 2000, would
> give c = 6.86."

### 2.2 Theorem 1 (E3), verbatim (p. 2)

> "Theorem 1. Almost all intervals [x, x + (loglog x)^{6+eps} log x]
> contain a product of exactly three distinct primes."

CONFIRMS the "E3 window (loglog X)^{6+eps} log X" the dispatch asked to
check: it is exactly the printed window of Theorem 1 (with loglog =
second iterated log). No correction needed.

### 2.3 Theorem 2 (general Ek, k >= 4), verbatim (p. 2)

> "Theorem 2. For any integer k >= 4, there exists Ck > 0 such that
> almost all intervals [x, x + (log_{k-1} x)^{Ck} log x] contain a
> product of exactly k distinct primes. Here log_l is the l-th iterated
> logarithm."

### 2.4 Theorem 3 (E2), verbatim (p. 2)

> "Theorem 3. Almost all intervals [x, x + log^{3.51} x] with x <= X
> contain a product of exactly two distinct primes."

### 2.5 Theorem 4 (the general Ek mean-value statement) -- THE central display

Verbatim (p. 2), transcribed from the page-2 image
[TRANSCRIPTION-UNSURE, resolved-by-image]; the sum subscripts and the
exponent tower were scrambled in both text layers:

> "Theorem 4. Let X be large enough, k >= 3 a fixed integer, and eps > 0
> small enough but fixed. Define the numbers P_1, ..., P_{k-1} by setting
> P_{k-1} = (log X)^{eps^{-2}}, P_{k-2} = (loglog X)^{6+10*sqrt(eps)} and
> P_j = (log P_{j+1})^{eps^{-1}} for 1 <= j <= k-3. For
> P_1 log X <= h <= X, we have
>
>   | (1/h) * SUM_{ x <= p_1...p_k <= x+h ;  P_i <= p_i <= P_i^{1+eps}, i <= k-1 } 1
>     - (1/X) * SUM_{ X <= p_1...p_k <= 2X ;  P_i <= p_i <= P_i^{1+eps}, i <= k-1 } 1 |
>   <<  1 / ( (log X) (log_k X) )                                        (1)
>
> for almost all x <= X."

Full quantifier order, as printed: X large enough; k >= 3 FIXED; eps > 0
small enough but fixed; then the tower P_1,...,P_{k-1} is DEFINED from X
and k (top P_{k-1} = (log X)^{eps^{-2}}; the specific slot
P_{k-2} = (loglog X)^{6+10 sqrt(eps)}; and downward
P_j = (log P_{j+1})^{eps^{-1}} for 1 <= j <= k-3); then for EVERY h in
the range P_1 log X <= h <= X, the discrepancy bound (1) holds "for
almost all x <= X" (all but o(X) integers x <= X). Both sums restrict
each of the FIRST k-1 prime factors p_i to the dyadic-ish window
[P_i, P_i^{1+eps}]; the k-th factor p_k is unrestricted beyond the
product-size condition. The left sum counts p_1...p_k in the short
interval [x, x+h]; the right sum counts them in the dyadic block
[X, 2X], normalised by X.

Immediately after (p. 2):

> "In the theorem above, the average over the dyadic interval is
> >> 1/log X by the prime number theorem, so Theorems 1 and 2 indeed
> follow from Theorem 4."

So the mean (right term) is asymp 1/log X, and (1) forces the short-
interval count/h to equal it up to o(1/log X); positivity of the short
count for almost all x is what yields "contains an Ek number". The
k-dependence of the window enters ONLY through P_1 (the bottom of the
tower): h >= P_1 log X, and P_1 is the (k-2)-fold-nested log built from
the fixed slots P_{k-1}, P_{k-2}. For k=3: P_1 = P_{k-2} =
(loglog X)^{6+10 sqrt(eps)}, giving window asymp (loglog X)^{6+O(sqrt eps)} log X,
i.e. Theorem 1's (loglog x)^{6+eps} log x. For k >= 4 the extra nesting
P_j = (log P_{j+1})^{eps^{-1}} down to P_1 = log_{k-1}-scale gives
Theorem 2's window (log_{k-1} x)^{C_k} log x. [The exact identification
P_1 asymp (log_{k-1} X)^{C_k} is the mechanism by which "the lengths
approach log x as k -> infinity" -- each added prime factor replaces the
governing threshold by one more iterated logarithm.]

### 2.6 Theorem 5 (the E2 mean-value statement), verbatim

Verbatim (p. 3), from the page-3 image
[TRANSCRIPTION-UNSURE, resolved-by-image]:

> "Theorem 5. Let X be large enough, P_1 = log^a X with a = 2.51, eps > 0
> fixed, and P_1 log X <= h <= X. We have
>
>   (1/h) * SUM_{ x <= p_1 p_2 <= x+h ;  P_1 <= p_1 < P_1^{1+eps} } 1
>   >>  (1/X) * SUM_{ X <= p_1 p_2 <= 2X ;  P_1 <= p_1 <= P_1^{1+eps} } 1   (2)
>
> for almost all x <= X."

Quantifier order: X large; a = 2.51 (so P_1 = (log X)^{2.51}); eps > 0
fixed; h in [P_1 log X, X]; conclusion (2) for almost all x <= X. Unlike
(1), display (2) is a ONE-SIDED lower bound (>>): the short count is at
least a constant times the dyadic mean, not pinned to it. Note the
printed asymmetry in the p_1 range: the short (left) sum has
P_1 <= p_1 < P_1^{1+eps} (strict at the top), the dyadic (right) sum has
P_1 <= p_1 <= P_1^{1+eps} (non-strict). Transcribed as printed; see
FLAGS.

### 2.7 Remark 1 and Remark 2 (p. 3), verbatim

> "Remark 1. Since h >= P_1 log X, we have the dependence c = a + 1
> between the exponent a in Theorem 5 and the smallest exponent c for
> which we can show that the interval [x, x + log^c x] contains an E2
> number almost always."

(a = 2.51 => c = 3.51, matching Theorem 3.)

> "Remark 2. Note that Theorems 4 and 5 tell us that there are
> >> h/log X Ek numbers in almost all intervals [x, x + h], where h and
> k are as in one of the theorems. However, we are not quite able to
> find Ek numbers on intervals [x, x + psi(x) log x] with psi tending to
> infinity arbitrarily slowly, unlike in the result of Friedlander and
> Iwaniec on Pk numbers. In addition, our bound for the number of
> exceptional values is at best << x/log^eps x and often weaker, while
> the methods used in [10], [13] and [20] for primes in almost all short
> intervals have a tendency to give the bound << x/log^A x for any A > 0,
> when they work. The limit of our method for E2 numbers is the exponent
> 3 + eps, as will be seen later, so proving for example unconditionally
> the analog of Selberg's result for E2 numbers would require some
> further ideas."

Remark 2 supplies (a) the COUNT: >> h/log X Ek numbers in almost all
[x, x+h] (a lower bound on the count, not merely one number), and (b)
the EXCEPTIONAL-SET bound: at best << x/log^eps x integers x fail, and
"often weaker". This is the exceptional-set-versus-window statement.

---

## 3. METHOD ANATOMY (connective tissue; PARAPHRASE except quotes)

PARAPHRASE. The engine is an adaptation of Matomaki-Radziwill [15]
("Multiplicative functions in short intervals. To appear in Ann. of
Math.", ref [15], p. 40). The author replaces the multiplicative
function by the indicator of p_1...p_k with p_i drawn from the windows
[P_i, P_i^{1+eps}] and reduces the short-interval-vs-dyadic comparison
(1)/(2) to mean-value bounds for Dirichlet polynomials. Quote (p. 3-4):

> "using similar techniques, and replacing the multiplicative function
> with the indicator function of the numbers p_1 ... p_k, with p_i primes
> from carefully chosen intervals, allows us to find Ek numbers on
> intervals [x, x+h], with h/log x growing very slowly. In this setting,
> we can apply various mean, large and pointwise value results for
> Dirichlet polynomials, some of which work specifically with primes or
> the zeta function, but not with general multiplicative functions (such
> as Watt's theorem on the twisted moment of the Riemann zeta function,
> a large values theorem from [15] for Dirichlet polynomials supported on
> primes, and Vinogradov's zero-free region)." (p. 3-4)

Structure of the paper (from the -layout text):
- Section 1 Introduction (Theorems 1-5, Remarks 1-2); 1.1
  Acknowledgements, 1.2 Notation.
- Section 2 Preliminary lemmas: 2.1 Reduction to mean values of
  Dirichlet polynomials; 2.2 Factorizations for Dirichlet polynomials;
  2.3 Bounds for Dirichlet polynomials; 2.4 Moments of Dirichlet
  polynomials; 2.5 Sieve estimates. (Lemmas 1-14, Propositions 1-4.)
- Section 3 Mean squares of Dirichlet polynomials.
- Section 4 Proof of Theorem 4; 4.1 A corollary on products of two
  primes (the intermediate c = 5 + eps for E2). Proposition 5.
- Section 5: 5.1 Exponent pairs; 5.2 Lemmas on sieve weights
  (Lemma 15). Propositions 5-6 area.
- Section 6 Proof of Theorem 5: 6.1 Mean square bounds related to
  Theorem 5 (Propositions 6, 7); 6.2 Cases of Sigma_1(h) and Sigma_2(h)
  (Proposition 8); 6.3 Case of Sigma_3(h) (Lemma 16); ends with
  Remark 10.

### 3.1 The named inputs and where each binds (PARAPHRASE except quotes)

- Watt's theorem (twisted fourth moment of zeta sums). Stated as Lemma 9
  (p. 8): "Lemma 9. (Watt). Let T >= T_0 >= T^eps, ..." (full display is
  notation-heavy; not reproduced). It is "reduced to Watt's original
  twisted moment result [19]" (p. 8). Binds throughout: the mean-square
  bounds of Propositions 3, 6, 7, 8 "resort to the Watt-type
  Proposition" and "the conditions in A2 make it possible to apply Watt's
  theorem" (pp. 8, 31, 34). Used for E_k for all k >= 2.
- A large values theorem for prime-supported Dirichlet polynomials, from
  [15] (Matomaki-Radziwill): cited as an input specific to primes
  (p. 4).
- Vinogradov's zero-free region (p. 4).
- Heath-Brown's decomposition (Lemma 10, generalized Vaughan identity,
  ref [11]): "Heath-Brown's decomposition (Lemma 10) enables splitting
  the polynomial corresponding to p_2 as (log X)^{O(1)} sums" (p. 20).
- Halasz-Montgomery inequality (Lemma 5), used for the complement bounds
  (p. 20-21).
- Sieve methods (Section 2.5; Buchstab's function omega; the sieve
  S(A, P, z)) -- "similar to those ... applied to finding primes in
  short intervals for example in [10], [13] and [20]" (p. 4).
- Exponent pairs (Section 5.1) -- an E2-ONLY ingredient. Quote (p. 27):
  "we benefit from the theory of exponent pairs and Jutila's large
  values theorem" (p. 4); and Section 5.1: "each new exponent pair
  improves the exponent c for E2 numbers by approximately 0.02" (p. 27);
  the concrete input is that "(12/6, 1/2)"... [the specific exponent pair
  is (1/6, 1/2)-family; "This follows immediately from the fact that
  (1/6, 1/2) is an exponent pair", p. 27, see FLAGS for the scrambled
  fraction].
- Jutila's large values theorem (ref [14]): Lemma 7 (p. 8), "(Jutila's
  large values theorem)", "improves on the better known Huxley's large
  values" theorem (p. 8). Binds in the E2 argument: "Jutila's large
  values theorem (Lemma 7) applied with F(s) = M_1(s)^l" (p. 25) and
  "utilize Jutila's large values theorem" for |U'| (p. 34). It is an
  E2-specific escalation; for E_k (k >= 3) the argument "do[es] not
  appeal to Jutila's large values theorem, but to Lemma 6" (p. 35).

### 3.2 The intermediate c = 5 + eps for E2 (Section 4.1, p. 20), verbatim

> "As a byproduct of the methods above, we arrive at the exponent
> c = 5 + eps for products of two primes, which already replicates
> Mikawa's exponent for P2 numbers."

with F(s) = sum_{p_1 p_2 ~ X, P_1 <= p_1 < P_1^{1+eps}} (p_1 p_2)^{-s}
and P_1 = log^a X, a = 4 + eps there (p. 20). The reduction from 5 + eps
to 3.51 is "the rest of the paper" (p. 4) and requires exponent pairs +
Jutila + Watt refinements.

### 3.3 Remark 10: the c = 3 + eps LIMIT of the method (p. 39), verbatim

From the page-39 image [TRANSCRIPTION-UNSURE, resolved-by-image]:

> "Remark 10. We can now observe that c = 3 + eps is the limit of this
> method. Indeed, we are forced to take alpha_2 <= 1/4 in the type II
> case, because nothing nontrivial is known about the large values of
> Dirichlet polynomials beyond this region, and consequently
> a = 1/(2 alpha_2) + eps >= 2 + eps and c >= 3 + eps."

This locates the binding constraint for E2: the type-II large-value
budget alpha_2 <= 1/4 forces a = 1/(2 alpha_2) + eps >= 2 + eps, hence
(via Remark 1's c = a + 1) c >= 3 + eps. The value a = 2.51 achieved in
Theorem 5 is above the barrier a = 2; the gap 2.51 - 2 = 0.51 is the
distance from the method's own floor.

---

## 4. Uniformity ledger

WHAT IS FIXED. The rank k is a FIXED integer throughout (Theorem 4:
"k >= 3 a fixed integer"; Theorem 2: "For any integer k >= 4"; Theorem 5:
k = 2). It is never coupled to x. The quantity eps > 0 is "always small
enough but fixed" (p. 4) and enters the window exponents. a = 2.51 is a
fixed constant (Theorem 5). The exponent pair, sieve dimension, and the
number of prime slots k are all fixed before X -> infinity.

WHAT GROWS (with X, k fixed). The thresholds P_1, ..., P_{k-1}, all
functions of X: P_{k-1} = (log X)^{eps^{-2}} (largest), P_{k-2} =
(loglog X)^{6+10 sqrt(eps)}, and P_j = (log P_{j+1})^{eps^{-1}} nested
downward, so P_1 is the smallest and is of size (roughly)
(log_{k-1} X)^{C_k}. The window lower bound h >= P_1 log X grows with X;
h ranges up to X.

THRESHOLD DEPENDENCE.
- The window's k-dependence lives ENTIRELY in P_1 (the base of the
  tower). For k=3, P_1 = (loglog X)^{6+10 sqrt(eps)} => window asymp
  (loglog X)^{6+O(sqrt eps)} log X (Theorem 1: (loglog x)^{6+eps} log x).
  For k >= 4, P_1 = (log_{k-1} X)^{C_k} => window (log_{k-1} x)^{C_k}
  log x (Theorem 2). "the lengths approach log x as k -> infinity"
  because each extra factor adds one iterated logarithm to the base
  threshold. But this is a family of statements INDEXED by fixed k, NOT
  a single statement with k = k(x).
- C_k (Theorem 2) is positive, depends on k, and is NOT made explicit as
  a formula; it arises from the eps^{-1}-nesting of the P_j tower. The
  constants C_1, C_2, ... are "unspecified, positive, absolute" (p. 4);
  C_k carries k-dependence.
- The saving in (1) is 1/((log X)(log_k X)) -- k enters the saving only
  through the single extra iterated-log factor log_k X (WEAK
  k-dependence in strength). The saving in (2) is only constant order
  (>>), no explicit rate.
- The exceptional set: "at best << x/log^eps x and often weaker"
  (Remark 2). So the density-1 conclusion ("almost all x") is quantified
  as all-but-<< x/log^eps x, MUCH weaker than the << x/log^A x typical
  of prime short-interval methods.
- e_2 barrier: c >= 3 + eps unconditionally (Remark 10), from
  alpha_2 <= 1/4; achieved value a = 2.51 (c = 3.51).

CONSTANTS ABSOLUTE vs PARAMETER-DEPENDENT. C_1, C_2, ... absolute
(p. 4); C_k depends on k; the implied constants in << of (1)/(2) are
absolute given (k, eps) fixed but are not claimed uniform as k -> infinity
or eps -> 0. eps must be sent to 0 AFTER X -> infinity (it is fixed);
there is no joint (X, eps) or (X, k) uniformity statement.

DIRECTION. (1) is a TWO-SIDED discrepancy bound (absolute value <<
saving): for almost all x the short count/h equals the dyadic mean up to
o(1/log X); this contains BOTH an upper and a lower bound on the short
count. (2) is a ONE-SIDED lower bound (>>) only.

---

## 5. What the paper does NOT contain (mandatory NOT-FOUND probes, Section 4.3)

"primes" in the conclusion (as opposed to E_k / almost primes): NOT
FOUND in this text. Every theorem conclusion is about E_k numbers --
"contain a product of exactly three distinct primes" (Th 1), "exactly k
distinct primes" (Th 2), "exactly two distinct primes" (Th 3), and
counts of p_1...p_k (Th 4, 5). The word "primes" appears only in
motivation, in cited results (Selberg, Jia, GPY), and as the building
blocks p_i; no conclusion asserts an interval contains a prime. (The
author states the E_k problem is "a much closer analog of primes than
the Pk numbers", p. 1, but proves nothing about primes themselves.)

"consecutive": NOT FOUND in this text as a statement. The word
"consecutive" occurs only inside reference titles [1] Baker-Harman-Pintz
"difference between consecutive primes", [6] and [7] GPY, [18] Selberg
(p. 39-40). No theorem, lemma or remark concerns consecutive primes or
consecutive-gap words.

any two-point or coincidence statement: NOT FOUND in this text. All
results are one-point interval-occupancy / interval-count statements for
a single E_k object type; there is no correlation, coincidence,
two-shift, or pattern-of-two statement.

any upper bound: FOUND (partially), and this is the relevant nuance for
axis A4. Theorem 4 display (1) IS an upper bound on a discrepancy:
"| (1/h) SUM_short - (1/X) SUM_dyadic | << 1/((log X)(log_k X))" (p. 2),
which yields an upper bound on the short-interval count of E_k numbers
(with the P_i-window restriction, k fixed) for almost all x. There is
also, within proofs, use of "upper bound sieve weights" (p. 33) and
"the upper bound can be considered similarly" (p. 30). There is NO
standalone theorem stating an upper bound on the NUMBER of E_k numbers
of the sieve-Gallagher type as a headline result; the upper bound is the
two-sided-discrepancy half of Theorem 4. There is no upper bound on
class masses of gap words.

any statement valid for all x rather than almost all x: NOT FOUND in
this text. Every conclusion is "for almost all x <= X" / "almost all
intervals" (all but o(X), or all but << x/log^eps x). No pointwise-in-x
(every x) interval-occupancy statement appears.

ADDITIONAL located absences relevant to the six axes:
- No class-normalised or gap-word-conditioned quantity ("N_{P,d}",
  consecutive-gap words): NOT FOUND. The grain is a count of integers
  n = p_1...p_k in an interval, with the p_i restricted to fixed
  windows; it is a prime-factorisation count, not a consecutive-gap-word
  class mass.
- No singular series and no growing tuple rank: NOT FOUND (k fixed;
  no Hardy-Littlewood constant appears).
- No sparse/unbounded-scale statement in place of density-1: the results
  are density-1 in x ("almost all"), which is stronger than a sparse
  scale sequence; "sparse scales" / "unbounded scale sequence": NOT
  FOUND as a hypothesis (not needed -- the conclusion is uniform over
  almost all x).

---

## COMMENTARY (assessment, NOT extraction)

Consuming context (quoted verbatim from the dispatch, Section 4):

> "The project needs an unconditional averaged middle-slot non-concentration
> / upper-uniformity statement at rank k = (2/ln 2 + o(1)) lnln x, window
> h = A'L ln x ~ (ln x)(lnln x), of strength enough to keep a fixed
> proportion of D0-depth site mass off its modal middle on some unbounded
> scale sequence per s -- a statement that fails in the even-Cramer-smooth
> model.  Six axes: A1 rank; A2 window; A3 grain (class masses N_{P,d} of
> consecutive-gap words, not prime counts); A4 direction (upper /
> non-concentration); A5 strength (constant order suffices); A6 density
> (sparse scales, no s-uniformity).  A1-A4 are not relaxed by CG; A5 and A6
> are."

C1. What this paper unconditionally supplies. An UNCONDITIONAL,
density-1-in-x comparison between the short-interval count and the
dyadic-mean count of E_k numbers with prescribed prime-factor windows,
at a window h that reaches (log x) times a slowly growing factor:
Theorem 4 gives, for each fixed k >= 3, |short/h - dyadic/X| <<
1/((log X)(log_k X)) for almost all x, at h >= P_1 log X with
P_1 = (log_{k-1} X)^{C_k}; for k=3 the window is (loglog x)^{6+eps}
log x. This is the located result closest in SHAPE to the project's
A1 x A2 pair -- a rank-like index k coupled to a window that approaches
log x. It is fully unconditional (Watt, Jutila, Heath-Brown, sieves,
Vinogradov region; no RH, no density hypothesis). It even carries the
count (>> h/log X E_k numbers, Remark 2) and the exceptional-set bound
(<< x/log^eps x, Remark 2).

C2. Why it is not the carrier -- rank (A1). The decisive mismatch. In
this paper k is a FIXED integer; the window's dependence on k is a family
of statements indexed by fixed k, not a single statement with
k = k(x) ~ (2/ln 2) lnln x. The whole tower P_1,...,P_{k-1} and the
constant C_k are defined with k held fixed before X -> infinity; nothing
in the text lets k grow with x (the phrase "approach log x as
k -> infinity" is an OUTER limit over the family, taken after each x-limit).
The project needs the rank welded to x at the Erdos-Kac rate; this paper
supplies no such coupling. A1 is the primary failure.

C3. Why it is not the carrier -- grain (A3). The grain is a count of
integers with exactly k prime factors from fixed windows -- a
prime-factorisation count, not a class mass N_{P,d} of consecutive-gap
words. The project's object is the mass of gap-pattern words at D0 depth;
Teravainen's object is |{n in [x,x+h] : n = p_1...p_k, p_i in windows}|.
There is no transfer here from an E_k interval-count to a gap-word class
mass; A3 fails at the level of what is being counted.

C4. Direction (A4) is favourable in form. Unlike a pure existence or
lower-bound result, Theorem 4 is a TWO-SIDED discrepancy bound: its
absolute-value display is genuinely an UPPER bound on |short count -
mean|, hence an upper/non-concentration-usable statement about the E_k
count for almost all x. So on the direction axis alone the paper is of
the wanted type (upper/non-concentration), which is why it is worth
recording. But the object it bounds (A3) and the rank regime (A1) are
wrong, so the favourable direction does not rescue it. Theorem 5 (E2) is
only one-sided (>>), so E2 does NOT even clear A4; the two-sided form is
special to Theorem 4 (E_k, k >= 3).

C5. Strength (A5) and density (A6) -- the CG-relaxed axes -- are cleared
with room to spare, which confirms these are not the binding axes.
Strength: Theorem 4's saving 1/((log X)(log_k X)) is far stronger than
the constant order the project would accept; A5 CLEARS. Density: the
conclusion holds for almost all x (all but o(X), indeed all but
<< x/log^eps x), which is stronger than "some unbounded scale sequence",
so a fortiori supplies a sparse scale set with no s-uniformity needed;
A6 CLEARS. That both soft axes clear while A1 and A3 fail is exactly the
signature the dispatch predicts: this paper misses on the axes CG does
NOT relax.

C6. The E2 barrier is orthogonal to our need but worth logging. Remark 10
fixes the method's unconditional floor at c = 3 + eps (from
alpha_2 <= 1/4, "nothing nontrivial is known about the large values of
Dirichlet polynomials beyond this region"), with a = 2.51 achieved. This
is a window-scale statement about E2 at a FIXED power of log; it neither
grows the rank nor touches gap-word grain, so it does not bear on the
carrier question. It does record that even the E2 window here
(log^{3.51} x) is a fixed power of log, far ABOVE the A2 target
(log x)(loglog x); only the E_k (k>=3) family reaches the (log x)(loglog
x)-scale window, and only at fixed k.

Per-axis verdict (this paper):
- A1 rank: FAILS. k is a fixed integer, never coupled to x; no statement
  with k ~ (2/ln 2) lnln x. The window's k-dependence is an outer limit
  over a fixed-k family, not an x-coupled rank.
- A2 window: CLEARS (borderline, E_k side only). For k = 3, Theorem 4/1
  operate at h asymp (log x)(loglog x)^{6+eps}, of the target
  (ln x)(lnln x)-family (log x times a lnln power); the multiplier is a
  higher power than the target's (lnln x)^1, and the E2 window
  (log^{3.51} x) is far larger, but the log-window regime is reached.
- A3 grain: FAILS. Object is a prime-factorisation interval count of E_k
  numbers, not a class mass N_{P,d} of consecutive-gap words.
- A4 direction: CLEARS (Theorem 4 only). The two-sided |.| << saving of
  (1) is an upper/non-concentration-type bound on the E_k count for
  almost all x. (Theorem 5 / E2 is one-sided and would FAIL A4.)
- A5 strength: CLEARS. Saving 1/((log X)(log_k X)) far exceeds the
  constant order that suffices.
- A6 density: CLEARS. Holds for almost all x (all but << x/log^eps x),
  stronger than an unbounded sparse scale sequence with no s-uniformity.

Even-Cramer-smooth deterministic gap system (q_1=2, q_2=3, q_3=5, q_4=7,
q_{n+1}=q_n+2*ceil(ln q_n / 2)): UNTESTED against it. The paper's object
is an unconditional analytic count of E_k numbers in short intervals via
Dirichlet-polynomial mean values; it makes no statement about
deterministic consecutive-gap-word class masses, so there is nothing in
the text that could be evaluated in that model. Untested (not a guess):
no display in this paper predicts or is contradicted by the
even-Cramer-smooth construction.

Overall: does NOT clear all six axes (A1 and A3 fail; A2 borderline).
Not a located carrier.

---

## FLAGS (consolidated)

1. [TRANSCRIPTION-UNSURE, resolved-by-image] Theorem 4 display (1),
   p. 2: the two sum subscripts (P_i <= p_i <= P_i^{1+eps}, i <= k-1;
   product-size conditions) and the exponent tower P_{k-1} =
   (log X)^{eps^{-2}}, P_{k-2} = (loglog X)^{6+10 sqrt(eps)},
   P_j = (log P_{j+1})^{eps^{-1}} were scrambled in both pdftotext
   -layout and -raw. Transcribed from the 200-dpi page-2 image; the
   right-hand side reads 1/((log X)(log_k X)). Reading cross-checked by
   the immediately following sentence "the average over the dyadic
   interval is >> 1/log X" and by Theorem 1's window matching k=3.
2. [TRANSCRIPTION-UNSURE, resolved-by-image] Theorem 5 display (2),
   p. 3: transcribed from the page-3 image. The short (left) sum has the
   STRICT top P_1 <= p_1 < P_1^{1+eps} while the dyadic (right) sum has
   the NON-STRICT P_1 <= p_1 <= P_1^{1+eps}. This asymmetry is as
   printed (also present, scrambled, in the raw layer); flagged as a
   likely typo but transcribed faithfully.
3. [TRANSCRIPTION-UNSURE, resolved-by-image] Remark 10, p. 39: the
   fraction "a = 1/(2 alpha_2) + eps" and "alpha_2 <= 1/4" were rendered
   as "a = 2 alpha1 2 + eps" and "alpha2 <= 14" by pdftotext. Read from
   the page-39 image; the arithmetic (alpha_2 = 1/4 => 1/(2 alpha_2) = 2
   => a >= 2 + eps => c >= 3 + eps) confirms the reading.
4. [PRINTED-ODDITY] Abstract states the E3 window as log^{1+eps} x while
   Theorem 1 states the sharper (loglog x)^{6+eps} log x. Both are the
   author's; (loglog x)^{6+eps} log x <= log^{1+eps} x, so the abstract
   gives the weaker round-number form. No contradiction, recorded for
   fidelity.
5. [TRANSCRIPTION-UNSURE, resolved-by-context] Section 5.1 exponent-pair
   line (p. 27): pdftotext renders the exponent pair as "( 126 , 21 )";
   read in context as the exponent pair (1/6, 1/2) (standard; the text
   says "This follows immediately from the fact that (1/6,1/2) is an
   exponent pair"). Not re-imaged; low load on the E_k focus.
6. [TRANSCRIPTION-UNSURE, resolved-by-context] Lemma 7 (Jutila) and
   Lemma 9 (Watt) full displays (pp. 8) are notation-dense and partly
   scrambled in the text layer; they are cited by label and role here,
   not transcribed verbatim, as they are inputs rather than the focus
   E_k statement. Their NAMES and roles ("Jutila's large values
   theorem", "Watt('s theorem)") are confirmed from the -layout layer
   and the reference list [14], [19].
7. [PRINTED-ODDITY] p. 3-4 the phrase "nearly nearly lossless" (doubled
   "nearly") appears in the text layer; transcribed as printed in the
   method-anatomy quote source (not reproduced above).
8. The intermediate E2 exponent c = 5 + eps (Section 4.1) uses
   P_1 = log^a X with a = 4 + eps there, distinct from the a = 2.51 of
   Theorem 5; both transcribed as printed (pp. 20, 3).
