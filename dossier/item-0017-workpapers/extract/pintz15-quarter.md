# EXTRACTION: Janos Pintz, "A note on the distribution of normalized prime gaps"

Source (only evidence base): /home/istr/pro/erdos251/dossier/1510.04577v1.pdf
arXiv:1510.04577v1 [math.NT] 15 Oct 2015 (sidebar stamp on p. 1). Author:
Janos Pintz, Renyi Mathematical Institute of the Hungarian Academy of
Sciences, Budapest (address block, p. 7). 7 pages. Footnote p. 1:
"Supported by OTKA Grants NK104183, K100291 and ERC-AdG. 321104."

Transcription conventions: ASCII only. Diacritics transliterated (Erdos,
Pintz as printed, Janos, Yildirim, Westzynthius, Renyi, Realtanoda,
Freiberg). Math in LaTeX-like ASCII: d_n = p_{n+1} - p_n, <= , >= , << ,
\asymp (asymp), binom(l,2) = l choose 2, prod = product, sum = summation,
1_P = indicator of the prime set P (paper's blackboard-bold P), lambda_{d_1,
...,d_k} = Maynard-Tao sieve weights, log_v n = v-times iterated logarithm
(paper's own convention, stated after (2.3)). J' -type prime marks denote
the set of limit points (the paper writes {.}' for limit-point set).
epsilon, alpha, beta, gamma, delta, rho (paper prints varrho), ell spelled
out. Anchors are equation/theorem/section numbers; page numbers (printed =
PDF page) are secondary aid.

Everything up to the final marked section is EXTRACTION (what the paper
says). Commentary appears ONLY in the final marked section.

NOTE: the paper has NO abstract as printed. Page 1 goes directly from the
title and author to "1 Introduction". So the "abstract" slot of this
extraction is occupied by the introduction's framing claims, quoted
verbatim.

---

## 1. SECTION 1 (Introduction): setting and prior results (verbatim)

Opening (Section 1, p. 1), verbatim:

> "The Prime Number Theorem implies that the average value of
> (1.1)   d_n = p_{n+1} - p_n
> is (1 + o(1)) log p_n if n in [N, 2N], for example, where P = {p_i}_{i=1}^infty
> is the set of primes. This motivates the investigation of the sequence
> {d_n / log p_n}_{n=1}^infty or {d_n / log n}_{n=1}^infty (which is
> asymptotically equal). Erdos formulated the conjecture that the set of its
> limit points
> (1.2)   J = { d_n / log n }' = [0, infty]."

Erdos citation (Section 1, p. 1), verbatim:

> "He writes in [Erd 1955]: 'It seems certain that d_n / log n is everywhere
> dense in (0, infty)' (after mentioning the conjecture
> liminf_{n->infty} d_n / log n = 0). The fact that infty in J was proved
> already in 1931 by Westzynthius [Wes 1931]."

Prior knowledge on J (Section 1, p. 1), verbatim:

> "In 2005 Goldston, Yildirim and the author [GPY 2006], [GPY 2009] showed
> 0 in J which is the hitherto only concrete known element of J. On the
> other hand already 60 years ago Ricci [Ric 1954] and Erdos [Erd 1955]
> proved (simultaneously and independently) that J has a positive Lebesgue
> measure. A partial result towards the full conjecture (1.2) was shown by
> the author in [Pin 2013arX] according to which there exists an ineffective
> constant c such that
> (1.3)   [0, c] subset J."

BFM input (Section 1, p. 2), verbatim:

> "In a recent work W. Banks, T. Freiberg and J. Maynard [BFM 2014arX]
> proved that for any sequence of k = 9 nonnegative real numbers
> beta_1 <= beta_2 <= ... <= beta_k we have
> (1.4)   { beta_j - beta_i : 1 <= i < j <= k } cap J != emptyset.
> As a corollary they obtained that if lambda denotes the Lebesgue measure,
> then
> (1.5)   lambda([0, T] cap J) >= (1 + o(1)) T / 8."

---

## 2. SECTION 2 (Generalization and Improvement): the class F and BOTH main results (verbatim)

Purpose sentence (Section 2, p. 2), verbatim:

> "The purpose of this note is to generalize this result for the case when
> d_n is normalized by a rather general function f(n) -> infty, that is to
> consider instead of J the more general case of the set of limit points
> (2.1)   J_f = { d_n / f(n) }'
> where we require from f to belong to the class F below."

Definition of the class F (Section 2, p. 2), verbatim:

> "Definition. A function f(n) nearly-increasing-to infty [printed as
> f(n) with a rising arrow to infty] belongs to F if for any epsilon > 0
> (2.2)   (1 - epsilon) f(N) <= f(n) <= (1 + epsilon) f(N)
>         for n in [N, 2N], N > N_0,
> further if
> (2.3)   f(n) << log n log_2 n log_4 n / (log_3 n)^2
> where log_v n denotes the v-times iterated logarithm."

Interpretation + the improvement claim (Section 2, p. 2), verbatim:

> "The first condition means that f(n) is slowly oscillating, while the
> second one that it does not grow more quickly than the Erdos-Rankin
> function, which until the recent dramatic new developments by Maynard
> [May 2014arX], Ford-Green-Konyagin-Tao [FGKT 2014arX], and
> Ford-Green-Konyagin-Maynard-Tao [FGKMT 2014arX] described the largest
> known gap between consecutive primes. The improvement means that it is
> sufficient to work with k = 5 values of beta_i in (1.4) instead of k = 9
> values. As an immediate corollary we obtain a lower bound (1 + o(1))T/4
> instead of (1.5) for the Lebesgue measure of the more general set
> [0, T] cap J_f."

MAIN THEOREM (Theorem 1, Section 2, p. 3), verbatim:

> "Theorem 1. If f in F, then for any sequence of k = 5 nonnegative real
> numbers beta_1 <= beta_2 <= ... <= beta_k we have
> (2.4)   { beta_j - beta_i : 1 <= i < j <= k } cap J_f != emptyset."

MAIN COROLLARY (Corollary 2, Section 2, p. 3), verbatim:

> "Corollary 2. If f in F, then
> (2.5)   lambda([0, T] cap J) >= (1 + o(1)) T / 4."

[TRANSCRIPTION-UNSURE / PRINTED-ODDITY: (2.5) prints "J", not "J_f",
although the hypothesis is "f in F" and the preceding page promises the
bound "for the Lebesgue measure of the more general set [0, T] cap J_f"
(Section 2, p. 2, quoted above). The intended set is evidently J_f; the
printed statement has bare J.]

So: the "(1/4 - o(1))T result" carried in the project notes corresponds
exactly to (2.5): lambda([0,T] cap J(_f)) >= (1 + o(1)) T/4, i.e. the
lower-bound constant is (1 + o(1))/4, improving BFM's (1 + o(1))/8 of
(1.5). The statement is a Lebesgue-measure lower bound for the set of
limit points of d_n/f(n) inside [0,T]; it is NOT a density statement about
n-sites.

Remarks following Corollary 2 (Section 2, p. 3), verbatim:

> "In an earlier work [Pin 2013arX] we showed that for any f in F there
> exists an ineffective constant c_f such that [0, c_f] subset J_f. We
> further remark that since beta_i can be arbitrarily large, Theorem 1
> includes the improvement of the Erdos-Rankin function given in (2.3)
> proved recently in [May 2014arX] and [FGKT 2014arX]. (We note that the
> proof uses some refinement of the argument of [May 2014arX], so it does
> not represent an independent new proof.)"

> "In connection with the original Erdos conjecture for general f in F we
> remark that it was proved in [Pin 2014arX] that the conjecture is in some
> sense valid for almost all functions f in F. More precisely it was shown
> in [Pin 2014arX] that if {f_n}_1^infty in F with
> lim_{x->infty} f_{n+1}(x)/f_n(x) = infty, then
> (2.6)   J_{f_n} = [0, infty]
> apart from at most 98 exceptional functions f_n."

---

## 3. SECTION 3 (Proof): the engine theorem (verbatim) and reduction strategy

Opening of Section 3 (p. 3), verbatim:

> "The generalization for the case f in F instead of the single case
> f = log n runs completely analogously to the proofs in [Pin 2014arX] so
> we will only describe how to improve k = 9 to k = 5 in Theorem 1 which
> leads to the improved Corollary 2 in the same simple way as described in
> the Introduction of the work of Banks, Freiberg and Maynard
> [BFM 2014arX]."

> "The result will follow from the following improvement of Theorem 4.3 of
> their work. Let Z be given by (4.8) of [BFM 2014arX]."

[PARAPHRASE marker: Z, and later B, I_k(F), gamma, delta, rho(varrho),
H_i(n), lambda_{d_1,...,d_k} are all inherited from [BFM 2014arX] notation
and are NOT redefined in this note. The note is notationally parasitic on
BFM throughout Section 3.]

THE ENGINE (Theorem 3, Section 3, pp. 3-4), verbatim:

> "Theorem 3. Let m, k and epsilon = epsilon(k) be fixed. If k is a
> sufficiently large multiple of 4m + 1 and epsilon is sufficiently small,
> there is some N(m, k, epsilon) such that the following holds for
> N >= N(m, k, epsilon) with
> (3.1)   w = epsilon log N,   W = prod_{p <= w, p | Z} p.
> [TRANSCRIPTION-UNSURE: the condition under the product prints as
> "p <= w, p|Z"; at this glyph size the stroke could be | (divides) or a
> crossed nmid (does not divide). Z is defined only by reference to (4.8)
> of BFM 2014arX and is not restated in this note.]
> Let H = {h_1, ..., h_k} be an admissible k-tuple (that is it does not
> cover all residue classes mod p for any prime p) such that
> (3.2)   0 <= h_1 < ... < h_k <= N
> and
> (3.3)   p | prod_{1 <= i < j <= k} (h_j - h_i)  ==>  p <= w.
> Let H = H_1 cup ... cup H_{4n+1} be a partition of H into 4m + 1 sets of
> equal size and let b be an integer with
> [TRANSCRIPTION-UNSURE: the last subscript in the displayed union prints
> as "4n+1"; the same sentence and (3.6) say the partition has 4m + 1
> parts, so "4n+1" appears to be a typo for "4m+1" in the source.]
> (3.4)   ( prod_{i=1}^k (b + h_i), W ) = 1.
> Then there is some n in (N, 2N] with n == b (mod W) and some set of
> distinct indices {i_1, ..., i_{m+1}} subseteq {1, ..., 4m + 1} such that
> (3.5)   | H_i(n) cap P | >= 1   for all i in {i_1, ..., i_{m+1}}."

[PARAPHRASE: H_i(n) is nowhere defined in this note; per BFM usage it is
the shifted block {n + h : h in H_i}. So (3.5) says: at least m + 1 of the
4m + 1 blocks of the tuple, shifted by n, each contain at least one prime.]

Remark after Theorem 3 (Section 3, p. 4), verbatim:

> "Remark. The original analogous statement (4.20) of [BFM 2014arX] should
> have been stated with >= 1 instead of = 1 (oral communication of James
> Maynard). This form is enough to imply their Corollary 1.2 or our
> Corollary 2."

---

## 4. SECTION 3 (Proof): the modified Maynard-Tao computation (verbatim)

The deduction change (Section 3, p. 4), verbatim:

> "The needed change in the Deduction of Theorem 4.3 is the following.
> First, using 4m + 1 | k we write
> (3.6)   H = H_1 cup ... cup H_{4m+1}
> as a partition of H into 4m + 1 sets each of size k/(4m + 1). Instead of
> the quantity S in [BFM 2014arX] we introduce with a new parameter
> alpha = alpha(m) the new quantity S(alpha), where alpha will be chosen
> relatively small (we will see that alpha(m) = 1/(5m) is a good choice,
> for example). Thus, let with a further parameter beta
> (3.7)   S(alpha, beta) = sum_{N < n <= 2N} ( sum_{i=1}^k 1_P(n + h_i)
>           - beta m
>           - alpha sum_{j=1}^{4m+1} sum_{h, h' in H_j, h != h'}
>             1_P(n + h) 1_P(n + h') )
>           x ( sum_{d_1,...,d_k : d_i | n + h_i forall i}
>               lambda_{d_1,...,d_k} )^2"
> [TRANSCRIPTION-UNSURE: in (3.7) the inner-sum condition prints as
> "h != h'_2" (a stray subscript-2 glyph after h'); the parallel condition
> in (3.13) prints cleanly as "h != h'", which is the reading adopted.
> Also the second indicator prints as "1_P(n + h)'" with the prime mark
> after the closing parenthesis; read as 1_P(n + h').]

Pairs convention + beta choice (Section 3, p. 5), verbatim:

> "where under the summation sign we consider unordered pairs h, h' in H_j.
> Let
> (3.8)   beta = beta(alpha) = max_{ell in Z^+} ( ell - alpha binom(ell, 2) )."

The block-capping logic (Section 3, p. 5), verbatim:

> "Then the contribution of any set H_j to S(alpha, beta) = S(alpha) is at
> most beta, so if we have for every n in (N, 2N] at most m sets of the
> form H_j with
> (3.9)   sum_{h in H_j} 1_P(n + h) > 0,
> then consequently
> (3.10)  S(alpha) <= 0."

THE PARAMETER DEPARTURE FROM BFM (Section 3, p. 5), verbatim:

> "In contrary to the choice varrho in (0, 1) and delta varrho log k = 2m
> of [BFM 2014arX] we will choose now delta varrho log k much larger
> (3.11)  delta varrho log k = u := (4m + 1)/(4 alpha),
>         alpha = 1/(5m),  varrho in (0, 1).
> This implies with an easy calculation
> (3.12)  beta = (5m + 1)/2."

The main-term evaluation (Section 3, p. 5), verbatim:

> "Using the same argument for the estimation of the negative double sum as
> [BFM 2014arX] we obtain a choice of a function F such that
> (3.13)  S(alpha) = (N/W) B^{-k} I_k(F) ( sum_{i=1}^k (u/k)(1 + O(gamma))
>           - beta m
>           - 4 alpha sum_{j=1}^{4m+1} sum_{h, h' in H_j, h != h'}
>             (u^2/k^2)(1 + O(delta + gamma)) )
>         = (N/W) B^{-k} I_k(F) ( u(1 + O(gamma)) - (5m + 1)m/2
>           - (4(4m + 1)/(5m)) binom(k/(4m + 1), 2)
>             (u^2/k^2)(1 + O(delta + gamma)) )."

The positivity computation (Section 3, p. 5), verbatim:

> "By the above choice of the parameters in (3.11) we have from (3.13) with
> gamma = (log k)^{-1/2}
> (3.14)  S(alpha) W B^k / (N I_k(F))
>           >= 5m(4m + 1)(1 + O(gamma))/4 - (5m + 1)m/2
>              - 5m(4m + 1)(1 + O(delta + gamma))/8
>           = m(1 + O(m(delta + gamma)))/8 > 0,"

Conclusion (Section 3, p. 6), verbatim:

> "which contradicts to (3.10). In order to see the validity of the last
> inequality we can choose
> (3.15)  m < (log k)^{1/4}  <==>  delta asymp ( m^2 / log k )
> which implies m gamma = o(1) and m delta = o(1). This contradiction
> proves our Theorem 1. Corollary 2 follows from it in the same way as
> Corollary 1.2 from Theorem 1.1 in [BFM 2014arX]."

[TRANSCRIPTION-UNSURE: the "<==>" in (3.15) is as printed (a double-headed
double arrow between the constraint on m and the calibration of delta);
the logical role appears to be "choose m, delta coupled so that both hold",
but the arrow itself is transcribed verbatim.]

[PARAPHRASE, arithmetic check by extractor: with alpha = 1/(5m), (3.11)
gives u = 5m(4m+1)/4; the three terms of (3.14) are then
5m(4m+1)/4 - (5m+1)m/2 - 5m(4m+1)/8 = m/8, matching the printed
m(1 + O(m(delta+gamma)))/8. The whole gain over BFM is engineered here:
the within-block pair-penalty alpha caps each block's contribution at
beta = (5m+1)/2 (by (3.8): ell primes in one block contribute
ell - alpha binom(ell,2) <= beta), so S(alpha) > 0 forces MORE THAN m
blocks to contain a prime, i.e. at least m + 1 of 4m + 1 blocks. The
block-hit ratio is thus (m+1)/(4m+1) -> 1/4 as m -> infty, versus the
ratio behind BFM's T/8. The note nowhere spells out the final k=5
pigeonhole; it defers it to "the same simple way as described in the
Introduction of ... [BFM 2014arX]" (Section 3, p. 3).]

---

## 5. FOCUS QUESTION 2: block/bin bookkeeping and the "9 -> 5/4 blocks" phrase

The phrase "9 -> 5/4 blocks reduction" is NOT FOUND in this text. No
sentence combines "9", "5/4", and "blocks". What the paper actually
states, verbatim, is the following, and the secondary-source phrase is
evidently a conflation of two separate printed facts:

(a) A reduction from k = 9 to k = 5 VALUES beta_i (not blocks):
"The improvement means that it is sufficient to work with k = 5 values of
beta_i in (1.4) instead of k = 9 values." (Section 2, p. 2); and "we will
only describe how to improve k = 9 to k = 5 in Theorem 1" (Section 3,
p. 3).

(b) A measure-constant improvement 1/8 -> 1/4 (which reads as "T/8 ->
T/4", plausibly garbled to "5/4"): (1.5) lambda([0,T] cap J) >=
(1 + o(1)) T/8 (BFM, Section 1, p. 2) versus (2.5) lambda([0,T] cap J)
>= (1 + o(1)) T/4 (Corollary 2, p. 3).

The actual block count in the proof is neither 9 nor 5: the k-tuple H is
partitioned into 4m + 1 blocks of equal size k/(4m + 1) ((3.6), p. 4;
Theorem 3, pp. 3-4), of which at least m + 1 are guaranteed to contain a
prime ((3.5), p. 4). The improvement mechanism over BFM is the penalized
sieve quantity S(alpha) with within-block prime-pair penalty alpha =
1/(5m) ((3.7), p. 4), the cap beta = beta(alpha) = max_ell (ell - alpha
binom(ell,2)) = (5m+1)/2 ((3.8) p. 5, (3.12) p. 5), and the much larger
parameter choice "In contrary to the choice varrho in (0,1) and
delta varrho log k = 2m of [BFM 2014arX] we will choose now
delta varrho log k much larger" with u = (4m+1)/(4 alpha) ((3.11), p. 5).
Positivity (3.14) against the cap (3.10) forces >= m + 1 prime-containing
blocks out of 4m + 1; the ratio (m+1)/(4m+1) -> 1/4 underlies both the
k = 5 and the T/4 statements [the ratio limit is extractor arithmetic;
the paper states only the displayed formulas].

---

## 6. FOCUS QUESTION 3: method anatomy (inputs and control)

(a) Uniform Maynard-Tao input. The engine is Theorem 3 (pp. 3-4), an
"improvement of Theorem 4.3" of [BFM 2014arX] (p. 3), i.e. a Maynard-Tao
sieve statement with weights lambda_{d_1,...,d_k} ((3.7)), W-trick
w = epsilon log N, W = prod_{p <= w, p|Z} p ((3.1),
[TRANSCRIPTION-UNSURE on the divisibility glyph]), admissible k-tuple
with ALL pairwise differences w-smooth ((3.3)), and congruence site
n == b (mod W) with (prod (b + h_i), W) = 1 ((3.4)). The uniformity in f
comes for free: "The generalization for the case f in F instead of the
single case f = log n runs completely analogously to the proofs in
[Pin 2014arX]" (p. 3). The large-gaps input is acknowledged as not
independent: "(We note that the proof uses some refinement of the
argument of [May 2014arX], so it does not represent an independent new
proof.)" (p. 3). Constraint on the block parameter: m < (log k)^{1/4}
((3.15), p. 6).

(b) How gap ratios / gap values are controlled. Only through the limit
point mechanism: Theorem 3 places >= 1 prime in each of some m + 1 of the
4m + 1 blocks H_i(n) ((3.5)); the positions h_i are free subject to
(3.2)-(3.3), so the blocks can be centered near prescribed points
beta_i f(N) [PARAPHRASE: this calibration step is NOT in this note; it is
deferred, verbatim, to "the same simple way as described in the
Introduction of the work of Banks, Freiberg and Maynard [BFM 2014arX]"
(p. 3), and "Corollary 2 follows from it in the same way as Corollary 1.2
from Theorem 1.1 in [BFM 2014arX]" (p. 6)]. Consequently some difference
beta_j - beta_i of the 5 prescribed values is realized as a limit point
of d_n/f(n) ((2.4)). Which difference is realized is not, and cannot be,
selected by the method (pigeonhole over the binom(5,2) = 10 differences).

(c) What is quantified and what is not. Quantified: the number of blocks
(4m + 1), the guaranteed hit count (m + 1), the cap beta = (5m+1)/2, the
sieve main term (3.13)-(3.14), the measure bound (1 + o(1))T/4 ((2.5)).
NOT quantified anywhere in the note: any lower bound on the density (in
N) of qualifying sites n; any localization of WHICH blocks receive
primes; any upper bound (exactness) on prime counts per block -- indeed
the Remark (p. 4) records that BFM's "= 1" claim had to be weakened to
">= 1". The earlier interval result is explicitly "ineffective"
((1.3) p. 1 and "an ineffective constant c_f" p. 3).

---

## 7. REFERENCES AS PRINTED (pp. 6-7, abbreviated to id + locator)

[BFM 2014arX] Banks, Freiberg, Maynard, "On limit points of the sequence
of normalized prime gaps", arXiv:1404.5094v2 [math.NT] 20 Oct. 2014.
[Erd 1955] Erdos, "Some problems on the distribution of prime numbers",
Teoria dei Numeri, Math Congr. Varenna, 1954, 8 pp., 1955.
[FGKT 2014arX] Ford, Green, Konyagin, Tao, "Large gaps between
consecutive prime numbers", arXiv:1408.4505, 20 Aug. 2014.
[FGKMT 2014arX] Ford, Green, Konyagin, Maynard, Tao, "Long gaps between
primes", arXiv:1412.5029v1, 16 Dec. 2014.
[GPY 2009] Goldston, Pintz, Yildirim, "Primes in tuples I", Ann. of Math.
(2) 170 (2009), 819-862.
[GPY 2006] Goldston, Pintz, Yildirim, "Primes in Tuples III: On the
difference p_{n+nu} - p_n", Funct. Approx. Comment. Math. 35 (2006),
79-89.
[May 2014arX] Maynard, "Large gaps between primes", arXiv:1408.5110
[math.NT], 21 Aug. 2014.
[Pin 2013arX] Pintz, "Polignac Numbers, Conjectures of Erdos on Gaps
between Primes, Arithmetic Progressions in Primes, and the bounded Gap
Conjecture", arXiv:1305.6289v1 [math.NT], 27 May 2013.
[Pin 2014arX] Pintz, "On the distribution of gaps between consecutive
primes", arXiv:1407.2213v1, 8 July 2014.
[Ric 1954] Ricci, "Sull'andamento della differenza di numeri primi
consecutivi", Riv. Mat. Univ. Parma 5 (1954), 3-54.
[Wes 1931] Westzynthius, "Uber die Verteilung der Zahlen, die zu der n
ersten Primzahlen teilerfremd sind", Comm. Phys. Math. Helsingfors (5)
25 (1931), 1-37.

There is no mention anywhere in the note of Erdos problem #251,
irrationality, sum p_n/2^n, binary digits, or Shiu strings. The note's
only objects are d_n/f(n) limit points and the Maynard-Tao block engine.

---

## COMMENTARY (assessment, NOT extraction)

Target restated: the project needs an UNCONDITIONAL supply of two
prime-gap-word sites with matched J-prefix and K-suffix windows and a
dominant weighted middle difference, at depths J, K ~ log_2 log x, and
must route around (i) pigeonhole blindness to variability, (ii) the
parity block on prescribing gap patterns, (iii) circular Shiu-string
densities.

1. What this paper CAN supply. Unconditionally, for ANY normalization
f in F -- and F reaches from arbitrarily slowly growing f up to the
Erdos-Rankin function ((2.2)-(2.3), p. 2) -- among any 5 prescribed
values beta_1 <= ... <= beta_5, some difference beta_j - beta_i is a
limit point of d_n/f(n) (Theorem 1, (2.4)). A limit point means
infinitely many sites n with d_n/f(n) arbitrarily close to a single
common value: that is, an unconditional infinite supply of PAIRS (indeed
infinite families) of sites whose SINGLE normalized middle gap matches to
within any tolerance. Corollary 2 ((2.5)) says such matchable values fill
at least measure (1 + o(1))T/4 of [0,T]. For the exchange configuration,
this is precisely and only the "dominant weighted middle difference"
ingredient in embryo: two sites with a matched single gap size, at any
prescribed normalization scale, including scales relevant near depth
log_2 log x since f may grow arbitrarily slowly (f only needs to increase
to infinity, (2.2)).

2. What it CANNOT supply: everything about words. The engine (Theorem 3,
(3.5)) guarantees >= 1 prime in each of SOME m + 1 of 4m + 1 blocks. It
gives (a) no control over WHICH blocks are hit, (b) no upper bounds --
interloper primes between and inside blocks are unconstrained -- and
(c) no second-site correlation. Hence no J-prefix/K-suffix gap-word
matching of any depth can be extracted: the method controls one gap
value per site (via the BFM deduction), never a word of consecutive
gaps. The matched-window half of the exchange configuration is entirely
outside this machinery.

3. Blocker (i) (pigeonhole blindness) is not routed around; it is
load-bearing here. Theorem 1 is itself a pigeonhole over the 10
differences of 5 values -- the method cannot select the realized
difference -- and Theorem 3's conclusion is an unlocalized (m+1)-subset
of blocks. The paper's improvement (BFM's 1/8 -> 1/4 via the alpha-
penalty (3.7)-(3.8) and the large parameter choice (3.11)) sharpens the
pigeonhole ratio but does not change its blind character.

4. Blocker (ii) (parity / no exact prescription) has a documented
witness in this text: the Remark (p. 4) that BFM's (4.20) "should have
been stated with >= 1 instead of = 1 (oral communication of James
Maynard)". Even the original authors' exact-count formulation had to be
retracted to a lower bound. This is textual confirmation that the
Maynard-Tao block method delivers one-sided (>= 1) prime placement only,
which is exactly the form of control that cannot prescribe a gap word.

5. Blocker (iii) (site densities at depth): untouched. The note proves
limit-point and measure-of-limit-values statements with NO lower bound on
the density of qualifying n; its antecedent interval result [0, c_f]
subset J_f is explicitly ineffective (p. 1 (1.3), p. 3). Shiu strings do
not appear. Nothing here substitutes for, or de-circularizes, a
site-density supply at depth log_2 log x.

6. Reusable levers, precisely two. (A) The f-uniformity of the whole
apparatus (class F, (2.2)-(2.3)): matched middle-gap pairs can be
manufactured at any slowly-varying normalization, so the "dominant
middle" scale of an exchange configuration can be tuned freely. (B) The
alpha-penalized block accounting ((3.7), (3.8), (3.10) vs (3.14)): a
transferable device for converting Maynard-Tao positivity into "at least
r of B blocks are hit" with hit ratio r/B -> 1/4 (here (m+1)/(4m+1),
constraint m < (log k)^{1/4}, (3.15)). If an exchange-supply argument is
ever built on block architectures, 1/4 is the best block-hit ratio this
note's bookkeeping yields; but the selection of which blocks, and any
suffix/prefix word structure, must come from elsewhere.

7. On the project's UNVERIFIED phrase "9 -> 5/4 blocks reduction": it
should be corrected in project notes to two separate facts, per Section 5
above: 9 -> 5 VALUES beta_i (p. 2, p. 3), and T/8 -> T/4 MEASURE
constant ((1.5) -> (2.5)); the proof's blocks number 4m + 1 with m + 1
guaranteed hits. No "5/4 blocks" statement exists in the text.
