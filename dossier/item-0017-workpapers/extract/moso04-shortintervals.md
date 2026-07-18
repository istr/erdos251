# EXTRACTION: Montgomery & Soundararajan, "Primes in Short Intervals"

Source (only evidence base): /home/istr/pro/erdos251/dossier/0409258v1.pdf
arXiv:math/0409258v1 [math.NT] 15 Sep 2004. Authors: Hugh L. Montgomery,
K. Soundararajan (both Dept. of Math., Univ. of Michigan, Ann Arbor, as
printed on p. 29). 29 pages. "Dedicated to Freeman Dyson, with best wishes
on the occasion of his eightieth birthday." (p. 1). 1991 MSC 11N05, 11M26,
11P45, 11N69. Key words (p. 1): "primes, zeros of the Riemann zeta function,
pair correlation, Cramer's model, random matrix theory." Typeset by AMS-TeX.

Transcription conventions: ASCII only. Diacritics transliterated (Cramer,
Erdos, Pal Erdos -> Pal Erdos). Math in LaTeX-like ASCII: \psi, \Lambda,
\Lambda_0(n) = \Lambda(n) - 1, \mu, \phi, \nu_p, <=, >=, << (Vinogradov),
<<_k (implied constant depends on k), \asymp, e(theta) = e^{2 pi i theta},
||theta|| = distance to nearest integer, eps for epsilon, delta for delta.
S(D) denotes the paper's fraktur-S singular series \frakS(\mathcal{D});
S_0(D) denotes \frakS_0(\mathcal{D}); these are DISTINCT from the roman
S(q_1,...,q_k;h) of eq. (51) and the exponential sum S(alpha) of Section 4
(name clash is in the paper; I keep the paper's letters). A denotes both the
constant A = 2 - C_0 - log 2pi (Theorem 2) and the arithmetic sum
A(q_1,...,q_k) of Lemma 3 (clash in the paper). C_0 = Euler's constant.
mu_k = 1*3*...*(k-1) for k even, 0 for k odd. [d_1,...,d_k] = lcm,
(a,b) = gcd. Anchors are the paper's equation numbers (1)-(72), Lemma/
Theorem numbers, and section numbers 0-4; page numbers (printed = PDF page)
are secondary aid. Everything up to the final marked section is EXTRACTION
(what the paper says); paraphrase is marked as such. Commentary appears ONLY
in the final marked section.

---

## 1. ABSTRACT (verbatim, p. 1)

> "Abstract. Contrary to what would be predicted on the basis of Cramer's
> model concerning the distribution of prime numbers, we develop evidence
> that the distribution of psi(x + H) - psi(x), for 0 <= x <= N, is
> approximately normal with mean ~ H and variance ~ H log N/H, when
> N^delta <= H <= N^{1-delta}."

[Here "H log N/H" is H log(N/H), as the body text and Conjecture 1 make
explicit.]

---

## 2. INTRODUCTION SETUP: CRAMER MODEL, SINGULAR SERIES (Section 0, pp. 1-3)

Opening (Section 0, p. 1), verbatim:

> "Cramer [4] modeled the distribution of prime numbers by independent
> random variables X_n (for n >= 3) that take the value 1 (n is 'prime')
> with probability 1/log n and take the value 0 (n is 'composite') with
> probability 1 - 1/log n. If p_n denotes the n-th prime number this model
> predicts that
>   lim_{N->infty} (1/N) card{n : 1 <= n <= N, p_{n+1} - p_n > c log p_n}
>     = e^{-c}
> for all fixed positive real numbers c."

Hardy-Littlewood input (Section 0, p. 1), verbatim:

> "Gallagher [6] showed that the above follows from Hardy & Littlewood's
> [10, p. 61] quantitative version of the prime k-tuple conjecture: If
> D = {d_1, d_2, ..., d_k} is a set of k distinct integers, then
> (1)  sum_{n<=x} prod_{i=1}^k Lambda(n + d_i) = (S(D) + o(1)) x
> as x -> infty where S(D) is the singular series
> (2)  S(D) = sum_{q_1,...,q_k, 1<=q_i<infty} ( prod_{i=1}^k
>        mu(q_i)/phi(q_i) ) sum_{a_1,...,a_k, 1<=a_i<=q_i, (a_i,q_i)=1,
>        sum a_i/q_i in Z} e( sum_{i=1}^k a_i d_i / q_i )"

Product form (p. 2), verbatim:

> "where e(theta) = e^{2 pi i theta}. Hardy & Littlewood showed that the
> right hand side above may be written more transparently as
> (3)  = prod_p (1 - 1/p)^{-k} (1 - nu_p(D)/p)
> where nu_p(D) denotes the number of distinct residue classes modulo p
> found among the members of D. (See the remarks following the proof of
> Lemma 3 in Sec 2.) Since nu_p(D) = k for all sufficiently large p, the
> product (3) is absolutely convergent. Hence its value is 0 if and only if
> there is a prime p for which nu_p(D) = p."

Gallagher's Poisson statement (p. 2), verbatim (display unnumbered):

> "Gallagher [6] showed that from (1) it follows that
>   int_2^X ( psi(x + lambda log x) - psi(x) )^k dx
>     ~ m_k(lambda) X (log X)^k
> when lambda asymp 1. Here m_k(lambda) = E(Y^k) is the k-th moment of a
> Poisson random variable Y with parameter lambda, and a asymp b means that
> a/b lies between two positive absolute constants. Thus the distribution of
> pi(x + h) - pi(h) is approximately Poisson when h asymp log X, as
> predicted by the Cramer model."

[TRANSCRIPTION-UNSURE: "pi(x + h) - pi(h)" is as I read the print; the
intended object is plainly pi(x+h) - pi(x).] [Note the name clash:
m_k(lambda) here vs m_k(q;h) in (10).]

Program of the paper (p. 2), verbatim:

> "In this paper we investigate the distribution of primes in longer
> intervals. Let H = H(N) be a function of N such that H = o(N) and
> H/log N -> infty as N -> infty. The Cramer model predicts that the
> distribution of psi(n + H) - psi(n) (for n <= N) is approximately normal
> with mean ~ H and variance ~ H log N. Assuming a strong form of the
> Hardy-Littlewood conjecture (1) we will show that this prediction holds
> in the range where H/log N -> infty and log H/log N -> 0 as N -> infty.
> In the range N^delta <= H <= N^{1-delta} we provide evidence showing that
> the Cramer model is incorrect, and conjecture instead that the
> distribution of psi(n + H) - psi(n) is approximately normal with mean ~ H
> and variance ~ H log(N/H)."

Normalization to Lambda_0 (p. 2), verbatim:

> "When h asymp log x, the moments of psi(x + h) - psi(x) and of
> psi(x + h) - psi(x) - h are of the same order of magnitude. However, for
> larger h one would expect that the moments of psi(x + h) - psi(x) to be
> far larger than those of psi(x + h) - psi(x) - h. We obtain our
> conclusions on the distribution of psi(x + h) - psi(x) by analyzing these
> latter, more delicate moments. To facilitate this study, we set
> Lambda_0(n) = Lambda(n) - 1, with the result that
>   psi(x + h) - psi(x) - h = sum_{x < n <= x+h} Lambda_0(n).
> Thus the main term is eliminated at the outset, which simplifies our
> calculations considerably. We recast (1) in an equivalent form that
> pertains to Lambda_0(n): If d_1, ..., d_k are distinct integers, then
> (4)  sum_{n<=x} prod_{i=1}^k Lambda_0(n + d_i) = (S_0(D) + o(1)) x
> as x -> infty where S_0(D) is related to S(D) by the identities
> (5)  S_0(D) = sum_{J subseteq D} (-1)^{card J} S(J),
> (6)  S(D) = sum_{J subseteq D} S_0(J)."

p. 3, verbatim: "Here it is to be understood that S_0(emptyset) =
S(emptyset) = 1."

---

## 3. THE SINGULAR-SERIES SUMS R_k(h), V_k(q;h) AND THE UNCONDITIONAL
## THEOREMS 1-2 (pp. 3-4)

Gallagher's mean value and the definition of R_k(h) (p. 3), verbatim:

> "One of the main steps in Gallagher's argument is to show that
> (7)  sum_{d_1,...,d_k, 1<=d_i<=h, d_i distinct} S(D) ~ h^k
> as h -> infty. There are binom(h,k) subsets D under consideration, but
> each one occurs k! times in the above sum. Thus the above asserts that the
> mean value of S(D) tends to 1 as h -> infty. Correspondingly, we need to
> estimate the quantities
> (8)  R_k(h) = sum_{d_1,...,d_k, 1<=d_i<=h, d_i distinct} S_0(D)."

> "From (2) and (5) we see that
> (9)  S_0(D) = sum_{q_1,...,q_k, 1<q_i<infty} ( prod_{i=1}^k
>        mu(q_i)/phi(q_i) ) sum_{a_1,...,a_k, 1<=a_i<=q_i, (a_i,q_i)=1,
>        sum a_i/q_i in Z} e( sum_{i=1}^k a_i d_i/q_i )."

[Note: the only difference from (2) is the condition 1 < q_i, i.e. all
q_i > 1.]

The Montgomery-Vaughan bridge quantity (p. 3), verbatim:

> "The task of estimating averages of this expression is quite challenging,
> but our burden is substantially lightened by work of Montgomery & Vaughan
> [16] concerning a strikingly similar quantity. Let
> (10)  m_k(q;h) = sum_{n=1}^q ( sum_{m=1, (m+n,q)=1}^h 1 - h phi(q)/q )^k
> be the k-th centered moment of the number of reduced residues (mod q) in
> an interval. Lemma 2 of Montgomery & Vaughan asserts that
> (11)  m_k(q;h) = q (phi(q)/q)^k V_k(q;h)
> where
> (12)  V_k(q;h) = sum_{d_1,...,d_k, 1<=d_i<=h} sum_{q_1,...,q_k, 1<q_i|q}
>         ( prod_{i=1}^k mu(q_i)/phi(q_i) ) sum_{a_1,...,a_k, 1<=a_i<=q_i,
>         (a_i,q_i)=1, sum a_i/q_i in Z} e( sum_{i=1}^k a_i d_i/q_i )."

[CRITICAL STRUCTURAL POINT, stated in the paper at p. 16 (quoted in Part 7
below): in V_k the d_i are NOT required to be distinct, whereas in R_k they
are; also in V_k the moduli q_i run over divisors > 1 of a fixed q, while
in R_k they are unrestricted (> 1). The bulk of the proof of Theorem 2 is
the bridge.]

Small k (p. 3), verbatim:

> "When k = 1, the conditions in the innermost sum cannot be fulfilled, and
> thus V_1(q;h) = 0. When k = 2, the conditions in the innermost sum
> require that q_1 = q_2 = a_1 + a_2. Thus
> (13)  V_2(q;h) = sum_{d|q, d>1} mu(d)^2/phi(d)^2 sum_{a=1, (a,d)=1}^d
>         |E(a/d)|^2"

[TRANSCRIPTION-UNSURE: the condition "q_1 = q_2 = a_1 + a_2" is as printed;
the intended meaning is q_1 = q_2 and q_1 | a_1 + a_2.]

> "where
> (14)  E(alpha) = sum_{m=1}^h e(m alpha)."   (p. 4)

Prior state of the art (p. 4), verbatim:

> "Montgomery & Vaughan showed that
>   V_k(q;h) <<_k (hq/phi(q))^{k/2} ( 1 + O( h^{-1/(7k)}
>     (q/phi(q))^{2^k + k/2} ) )
> for each positive integer k. Unfortunately, this is not quite sharp
> enough for our present purposes, so our first job is to refine the
> above."

THEOREM 1 (p. 4), verbatim:

> "Theorem 1. In the above notation,
> (15)  V_k(q;h) = mu_k V_2(q;h)^{k/2} + O_k( h^{k/2 - 1/(7k)}
>         ( q/phi(q) )^{2^k + k/2} )
> for every positive integer k, where mu_k = 1 * 3 *** (k-1) if k is even,
> and mu_k = 0 if k is odd."

The uniformity-in-k remark (p. 4, immediately after Theorem 1), verbatim:

> "Here the main term is the k-th moment of a normal random variable with
> expectation 0 and variance V_2(q;h). We remark that the work of
> Granville & Soundararajan [7] (see Sec 6a) places restrictions on the
> uniformity (in k) with which (15) can possibly hold. With Theorem 1 in
> hand, we are able to estimate the R_k(h)."

[TRANSCRIPTION-UNSURE / PRINTED-ODDITY: the citation numeral "[7]" is as I
read it, but in the reference list (p. 28) item 7 is D. A. Goldston,
"Linnik's theorem on Goldbach numbers in short intervals", while
Granville & Soundararajan, "An uncertainty principle for arithmetic
sequences" is item 9. The named authors are unambiguous: the restriction
reference is the Granville-Soundararajan uncertainty-principle paper,
whatever the numeral.]

THEOREM 2 (p. 4), verbatim:

> "Theorem 2. Let h be an integer, h > 1, and suppose that R_k(h) is
> defined as in (8). Then
>   R_k(h) = mu_k (-h log h + Ah)^{k/2} + O_k( h^{k/2 - 1/(7k) + eps} )
> for any nonnegative integer k, where A = 2 - C_0 - log 2pi and C_0
> denotes Euler's constant."

Small-k precision (p. 4), verbatim:

> "For the smallest values of k, one can be more precise, since it is clear
> that R_0(h) = 1, and that R_1(h) = 0. Also, from (5) and (48) we know
> that
> (16)  R_2(h) = -h log h + Ah + O(h^{1/2+eps})."

Refined Gallagher estimate (p. 4), verbatim:

> "From (6) it follows that the left hand side of (7) is
>   sum_{r=0}^k binom(k,r) R_r(h) (h-r)(h-r-1)...(h-k+1).
> Hence we obtain Gallagher's estimate (7) in the more precise form
> (17)  sum_{d_1,...,d_k, 1<=d_i<=h, d_i distinct} S(D)
>         = h^k - binom(k,2) h^{k-1} log h
>           + binom(k,2)(1 - C_0 - log 2pi) h^{k-1} + O(h^{k-3/2+eps})."

---

## 4. MOMENTS OF psi AND THE CONDITIONAL RESULTS (pp. 5-6)

Moment definition (p. 5), verbatim:

> "We put
> (18)  M_K(N;H) = sum_{n=1}^N ( psi(n+H) - psi(n) - H )^K,
> and note that this is
> (19)  = sum_{n=1}^N ( sum_{h=1}^H Lambda_0(n+h) )^K
>       = sum_{h_1,...,h_K, 1<=h_i<=H} sum_{n=1}^N prod_{i=1}^K
>         Lambda_0(n + h_i).
> Here the h_i are not necessarily distinct, but once the distinct values
> have been identified, and their multiplicities accounted for, we can
> appeal to (4). The quantities R_k(h) arise in the main term. Thus from
> Theorem 2 we can derive an asymptotic estimate for the above, provided
> that the error term in (4) is sufficiently small and H is not too large."

THEOREM 3 (p. 5), verbatim:

> "Theorem 3. Let E_k(x;D) be defined by the relation
>   sum_{n<=x} prod_{i=1}^k Lambda(n + d_i) = S(D) x + E_k(x;D),
> and suppose that
> (20)  E_k(x;D) << N^{1/2+eps}
> uniformly for 1 <= k <= K, 0 <= x <= N, and distinct d_i satisfying
> 1 <= d_i <= H. Then
>   M_K(N;H) = mu_K H^{K/2} int_1^N ( log x/H + B )^{K/2} dx
> (21)    + O( N (log N)^{K/2} H^{K/2} ( H/log N )^{-1/(8K)}
>           + H^K N^{1/2+eps} )
> uniformly for log N <= H <= N^{1/K}, where B = 1 - C_0 - log 2pi and C_0
> denotes Euler's constant."

[In the integrand, "log x/H + B" is log(x/H) + B, as the K-even endgame of
the proof (p. 26, Part 8 below) shows.]

RH remark (p. 5), verbatim:

> "In the case k = 1, the set D is a singleton, S(D) = 1, and the
> hypothesis that E_1(N;{1}) << N^{1/2+eps} is equivalent to the Riemann
> Hypothesis (RH)."

Weakened-hypothesis remark (p. 5), verbatim:

> "In place of (20) if we assume only that E_k(x;D) << E for some
> E >= N^{1/2+eps} then (21) holds with the modified error term
>   O( N (log N)^{K/2} H^{K/2} ( H/log N )^{-1/(8K)} + H^K E )."

Distinctness-bridging remark (p. 5), verbatim:

> "We note that in deriving Theorem 3 from Theorem 2, we start with h_i
> that are not necessarily distinct, and must reduce to distinct d_i, which
> is the reverse of the problem encountered in deriving Theorem 2 from
> Theorem 1, where we start with distinct d_i, and want to appeal to an
> estimate involving not necessarily distinct m_i."

[TRANSCRIPTION-UNSURE: the final "m_i" is as I read the print; contextually
the not-necessarily-distinct variables in (12) are called d_i.]

> "Since the mu_K are the moments of a normal random variable with mean 0
> and variance 1 we deduce from Theorem 3 the following Corollary."  (p. 5)

COROLLARY 1 (p. 6), verbatim:

> "Corollary 1. Let H = H(N) be a function of N such that
>   H/log N -> +infty,   log H / log N -> 0
> as N -> infty. Assume that the hypothesis (20) holds for arbitrarily
> large K. Then the distribution of psi(n+H) - psi(n) - H for n <= N is
> approximately normal with mean 0 and variance H log N, in the sense that
> the proportion of n <= N for which
>   psi(n+H) - psi(n) - H <= c sqrt(H log N)
> tends to Phi(c) as N -> infty, uniformly for |c| <= C. Here
> Phi(u) = (1/sqrt(2pi)) int_{-infty}^u e^{-v^2/2} dv is the cumulative
> distribution function of a normal random variable with mean 0 and
> variance 1."

[TRANSCRIPTION-UNSURE: the radical in "c sqrt(H log N)" is small in the
scan; the normalization by sqrt of the variance is forced by the statement
"variance H log N".]

Limited-moments remark and the conjectures (p. 6), verbatim:

> "For larger H, Theorem 3 furnishes only a limited number of moments and
> we cannot deduce a distribution result. However we expect that the
> contributions of the E_k(x;D) cancel sufficiently so as not to overwhelm
> the main term:"

> "Conjecture 1. For each positive integer K,
>   M_K(N;H) = (mu_K + o(1)) N ( H log N/H )^{K/2}
> uniformly for (log N)^{1+delta} <= H <= N^{1-delta}."

> "This implies the weaker"

> "Conjecture 2. Suppose that (log N)^{1+delta} <= H <= N^{1-delta}. The
> distribution of psi(x+H) - psi(x) for 0 <= x <= N is approximately
> normal with mean H and variance H log N/H."

> "Certainly Conjecture 2 does not hold when H asymp N, but perhaps it
> holds whenever H = o(N). It would be interesting to investigate more
> thoroughly what happens in this range."

Zeta-zeros interpretation (pp. 6-7), verbatim (support context):

> "Hardy & Littlewood [10] provided heuristics that point toward the
> quantitative prime k-tuple conjecture (1). In Sec 4 we argue in the same
> spirit to obtain indications in favor of Conjecture 1."

> "We recall that Goldston & Montgomery [8] showed that if RH is true, then
> the stronger form (F(alpha) ~ 1) of the Pair Correlation Conjecture as
> formulated by Montgomery [13] is equivalent to the case K = 2 of the
> Conjecture above. In the same spirit, Chan [3] has shown (assuming RH)
> that Conjecture 1 is equivalent to the assertion that
> (22)  int_1^X ( sum_{0 < gamma <= T} cos(gamma log x) )^k dx
>         = (mu_k + o(1)) X ( T/(4pi) log T )^{k/2}."

(p. 7, paraphrase, connective:) The paper then notes the random-matrix
analogue of (22) via Rains [19] (Re Trace A^M for U(N) Haar matrices is
distributed exactly as a sum of N independent cos(2 pi X_n), whose k-th
moment is ~ mu_k (N/2)^{k/2} for k even), and numerical evidence: Brent
[2] for (1) and "the stronger hypothesis (20)"; Odlyzko [18] and
Forrester & Odlyzko [5] for local zero statistics; "The authors [15] have
reported on numerical evidence in support of the conjectures. Finally,
Chan [3; pp. 36, 49, 63] has assembled evidence in favor of (22)."
(verbatim fragments, p. 7).

---

## 5. CRAMER-MODEL FAILURE (pp. 7-8)

Verbatim (p. 7):

> "Cramer's model suggests that
> (23)  pi(x + (log x)^a) - pi(x) ~ (log x)^{a-1}
> as x -> infty with a fixed, a > 2. This, however, is known to be false,
> since Maier [11] showed that
>   limsup_{x->infty} ( pi(x + (log x)^a) - pi(x) ) / (log x)^{a-1} > 1,
>   liminf_{x->infty} ( pi(x + (log x)^a) - pi(x) ) / (log x)^{a-1} < 1
> for any fixed a > 0 (for general results of this nature see Granville &
> Soundararajan [7])."

[The two-line limsup/liminf rendering above expands the paper's single
display "lim-bar ... >< 1"; the inequality symbol is printed as a stacked
"greater-than over less-than". TRANSCRIPTION-UNSURE on the citation
numerals: "Maier [11]" and "Granville & Soundararajan [7]" are as I read
them, but the reference list has Maier at [12], Hausman & Shapiro at [11],
Goldston at [7], Granville & Soundararajan at [9].]

> "Presumably (23) is valid for most x, and the exceptions discovered by
> Maier are quite rare. Indeed Selberg [18] showed that on RH, (23) holds
> if a > 2 for almost all x, and Corollary 1 shows on hypothesis (20) that
> (23) holds if a > 1 for almost all x."   (p. 7)

[TRANSCRIPTION-UNSURE: "Selberg [18]" as printed; Selberg is item [20] in
the list, [18] is Odlyzko.]

> "As for longer intervals, suppose that alpha is fixed, 0 < alpha < 1.
> Cramer's model would predict that psi(x + x^alpha) - psi(x) - x^alpha is
> approximately normally distributed with mean 0 and variance
> X^alpha log X as x runs over the range X <= x <= 2X. Our Conjecture 1
> predicts normal distribution, but with a variance that is smaller by a
> factor of 1 - alpha. Thus it seems that in this range, Cramer's model is
> not just occasionally inaccurate, but instead is actually inaccurate on
> average."   (pp. 7-8)

---

## 6. METHOD ANATOMY A: PROOF OF THEOREM 1 (Section 1, pp. 8-12)

LEMMA 1 (p. 8), verbatim (the Montgomery-Vaughan "basic inequality"):

> "Montgomery & Vaughan [16] devised a useful basic inequality (their
> Lemma 1), which we now quote."
> "Lemma 1. Let r_1,...,r_k be squarefree integers, set r = [r_1,...,r_k],
> and suppose that any prime dividing r divides at least two of the r_i.
> Then for any complex-valued functions G_1,...,G_k defined on (0,1] we
> have
>   | sum_{b_1,...,b_k, 1<=b_i<=r_i, sum b_i/r_i in Z} prod_{i=1}^k
>     G_i(b_i/r_i) |
>   <= (1/r) prod_{i=1}^k ( r_i sum_{b_i=1}^{r_i} |G_i(b_i/r_i)|^2 )^{1/2}."

LEMMA 2 (p. 8), verbatim (the paper's new variant):

> "Montgomery & Vaughan [17] have derived several variants of the above; an
> exposition of such variants is found in Chapter 8 of Montgomery [14]. For
> our present purposes a different type of variant is useful."
> "Lemma 2. Let q_1,...,q_k be squarefree integers, each one strictly
> greater than 1, and put d = [q_1,...,q_k]. Let G be a complex-valued
> function defined on (0,1), and suppose that G_0 is a nondecreasing
> function on the positive integers such that
> (24)  sum_{a=1}^{q-1} |G(a/q)|^2 <= q G_0(q)
> for all squarefree integers q > 1. Then
>   | sum_{a_1,...,a_k, 0<a_i<q_i, sum a_i/q_i in Z} prod_{i=1}^k
>     G(a_i/q_i) |  <=  (1/d) prod_{i=1}^k q_i G_0(q_i)^{1/2}."

(Proof of Lemma 2, pp. 8-9, paraphrase: write q_i = r_i s_i with
r_i = (q_i, prod_{j\ne i} q_j) and the s_i pairwise coprime; the condition
sum a_i/q_i in Z forces s_i | a_i; substituting a_i = s_i b_i reduces the
sum to the Lemma-1 shape over b_i/r_i; if some r_i = 1 the sum is empty;
apply Lemma 1 with G_i = G extended by G(1) = 0, then (24) and
monotonicity of G_0, using (1/r) prod r_i = (1/d) prod q_i.)

Main body (p. 9), verbatim:

> "We now begin the main body of the proof of Theorem 1. We take k to be
> fixed, so that the dependence of implicit constants on k is suppressed.
> If k is odd, then the desired estimate is already found in (18) of
> Montgomery & Vaughan [16]. Thus we may assume that k is even. From (12)
> and (14) it is clear that
>   V_k(q;h) = sum_{q_1,...,q_k, 1<q_i|q} ( prod_{i=1}^k
>     mu(q_i)/phi(q_i) ) sum_{a_1,...,a_k, 1<=a_i<=q_i, (a_i,q_i)=1,
>     sum a_i/q_i in Z} prod_{i=1}^k E(a_i/q_i)."

Pairing reduction (p. 9), verbatim:

> "In Lemmas 7 and 8 of Montgomery & Vaughan [16], it is shown that all
> contributions to the above are
>   << h^{k/2 - 1/(7k)} ( q/phi(q) )^{2^k + k/2},
> except for those terms for which the q_i are equal in pairs, with no
> further equalities among the q_i. There are (k-1)(k-3)...3*1 = mu_k ways
> in which this pairing can occur. Take the pairing to be q_i = q_{k/2+i},
> and set b_i = a_i + a_{k/2+i}. Thus the terms that remain to be estimated
> are precisely
> (25)  mu_k sum_{q_1,...,q_{k/2}, 1<q_i|q, q_i distinct} prod_{i=1}^{k/2}
>         mu(q_i)^2/phi(q_i)^2 sum_{b_1,...,b_{k/2}, 1<=b_i<=q_i,
>         sum b_i/q_i in Z} prod_{i=1}^{k/2} J(b_i, q_i)
> where
> (26)  J(b,r) = sum_{a=1, (a,r)=1, (b-a,r)=1}^r E(a/r) E((b-a)/r)."

Dropping distinctness of the q_i (p. 10), verbatim:

> "First we show that the condition that the q_i should be distinct in (25)
> can be dropped. To see this, put F(alpha) = min(h, 1/||alpha||) where
> ||theta|| = min_{n in Z} |theta - n| is the distance from theta to the
> nearest integer. Thus
> (27)  |E(alpha)| <= F(alpha)
> for all alpha. Let Q denote the set of those k-tuples (q_1,...,q_k) such
> that 1 < q_i|q for all i, and with the property that among the q_i there
> are three or more of them that are equal. In proving their Lemma 8 (see
> the treatment of T_3), Montgomery & Vaughan [16] establish that
>   sum_{q in Q} ( prod_{i=1}^k |mu(q_i)|/phi(q_i) )
>     sum_{a_1,...,a_k, 1<=a_i<=q_i, (a_i,q_i)=1, sum a_i/q_i in Z}
>     prod_{i=1}^k F(a_i/q_i)
>   << h^{k/2 - 1/(7k)} ( q/phi(q) )^{2^k + k/2}."

Then (p. 10), paraphrase with verbatim displays: since this majorizes the
difference between (25) and the same expression without the distinctness
condition (eq. (28)), one continues with (28); sorting by the number j of
indices i with 0 < b_i < q_i (the rest having b_i = q_i) gives

> "(29)  mu_k sum_{j=0}^{k/2} binom(k/2, j) V_2(q;h)^{k/2-j} W_j(q;h)
> where W_0(q;h) = 1 and
> (30)  W_j(q;h) = sum_{q_1,...,q_j, 1<q_i|q} prod_{i=1}^j
>         mu(q_i)^2/phi(q_i)^2 sum_{b_1,...,b_j, 0<b_i<q_i,
>         sum b_i/q_i in Z} prod_{i=1}^j J(b_i, q_i).
> Here the term j = 0 gives the desired main term. Thus it remains to show
> that the other terms are smaller."

J(b,r) estimates (pp. 10-11), verbatim conclusions:

> "(31)  J(b,r) << (r^2/b) log 2b"      [range: 0 < b <= r/2 and r < h]
> "(32)  J(b,r) << rh"                  [range: 0 < b <= r/h and r >= h]
> "(33)  J(b,r) << (r^2/b) log(2bh/r)"  [range: r/h < b <= r/2 and r >= h]
> "(34)  sum_{0<b<r} J(b,r)^2 << r^3 min(r,h)."

(Each of (31)-(33) is proved by splitting the a-sum into ranges where one
of E(a/r), E((b-a)/r) is near a peak, using (27); "Here half the ranges of
a have been omitted, since by symmetry they contribute the same amount as
the listed sums." (p. 11, verbatim). From (31): if r < h then
sum_{0<b<r} J(b,r)^2 << r^4; from (32)-(33): if r >= h then << r^3 h;
together (34).)

W_j bound (p. 11), verbatim:

> "On taking G_0(r) = Chr^2 in Lemma 2, we find that
>   sum_{b_1,...,b_j, 0<b_i<q_i, sum b_i/q_i in Z} prod_{i=1}^j
>     J(b_i, q_i) << (1/d) prod_{i=1}^j ( q_i^2 h^{1/2} ),
> and hence
>   W_j(q;h) << h^{j/2} sum_{d|q} (1/d) ( sum_{r|d}
>     mu(r)^2 r^2/phi(r)^2 )^j
>   = h^{j/2} prod_{p|q} ( 1 + (1/p)( 1 + p^2/(p-1)^2 )^j )
>   << h^{j/2} ( q/phi(q) )^{2^j}."

[The G_0(r) = Chr^2 is "C h r^2", C an absolute constant; legitimate by
(34) since r^3 min(r,h) <= r * (C h r^2).]

V_2 upper bound (pp. 11-12), verbatim:

> "To apply this in (29), we need also a bound for V_2(q;h). To this end we
> note that
>   V_2(q;h) <= sum_{d|q} mu(d)^2/phi(d)^2 sum_{a=1}^{d-1} F(a/d)^2
>     << h sum_{d|q} mu(d)^2 d/phi(d)^2
>     = h prod_{p|q} ( 1 + p/(p-1)^2 ) << h q/phi(q)."
> "(By a different method it can be shown that V_2(q;h) <= hq/phi(q). See
> Hausman & Shapiro [11] and (3) of Montgomery & Vaughan [16].)"

Conclusion (p. 12), verbatim:

> "From (30) we see that W_1(q;h) = 0, since the inner sum is empty. On
> applying the above estimates for 2 <= j <= k/2, we see that the
> expression (29) is
>   mu_k V_2(q;h)^{k/2} + O( h^{k/2-1} ( q/phi(q) )^{2^k} ).
> Here the error term is majorized by that in (15), so the proof is
> complete."

---

## 7. METHOD ANATOMY B: PROOF OF THEOREM 2 (Section 2, pp. 12-22)

LEMMA 3 (p. 12), verbatim (the Hardy-Littlewood local machinery):

> "Lemma 3. (Hardy-Littlewood) Let
>   A(q_1,...,q_k) = sum_{a_1,...,a_k, 1<=a_i<=q_i, (a_i,q_i)=1,
>     sum a_i/q_i in Z} e( sum_{i=1}^k d_i a_i / q_i ).
> If q_i = q_i' q_i'' with ( prod q_i', prod q_i'' ) = 1, then
> (35)  A(q_1,...,q_k) = A(q_1',...,q_k') A(q_1'',...,q_k'').
> For any prime number p,
> (36)  sum_{q_1,...,q_k, q_i|p} prod_{i=1}^k ( mu(q_i)/phi(q_i) )
>         A(q_1,...,q_k) = ( 1 - 1/p )^{-k} ( 1 - nu_p(D)/p )
> where nu_p(D) is the number of distinct residue classes modulo p found
> among the members of D = {d_1,...,d_k}. Finally,
> (37)  sum_{q_1,...,q_k, 1<=q_i<infty} prod_{i=1}^k
>         ( mu(q_i)^2/phi(q_i) ) |A(q_1,...,q_k)| < infty."

(Proof anatomy, pp. 12-14, paraphrase with verbatim key values: (35) by
CRT on reduced residues. (36) by inserting the p-th roots-of-unity
detector: with each q_i in {1,p}, the r-sum yields factors
(1 - (1/(p-1)) sum_{0<a<p} e(a(d_i - r)/p)), the innermost sum being p-1
or -1 "according as r == d_i (mod p), or not"; there are nu_p(D) values of
r giving a zero factor, and the remaining p - nu_p(D) values each give
(p/(p-1))^k, whence (p - nu_p(D))/p * (p/(p-1))^k. For (37): by (35) the
sum with moduli restricted to q_i | Q factors over p | Q, eq. (38); put
D-script = prod_{i<j} (d_j - d_i) [the paper writes "Put D =
prod_{i<j}(d_j - d_i)", a THIRD use of the letter D]; for p not dividing
this discriminant the d_i are distinct mod p and the local factor is
computed exactly: for the configuration q_i = p for i in J, card J = j,
the value is
   "= (1/p)( j(p-1)(-1)^{j-1} + (p-j)(-1)^j ) = (-1)^{j-1}(j-1)."
(p. 13, verbatim), so |A| = |j-1| and the p-factor is
   1 + sum_{j=2}^k binom(k,j) (j-1)/(p-1)^j     (p. 14, display),
whose product over p converges.)

Consequences (p. 14), verbatim:

> "(39)  sum_{q_1,...,q_k, q_i|Q} prod_{i=1}^k ( mu(q_i)/phi(q_i) )
>          A(q_1,...,q_k) = prod_{p|Q} ( 1 - 1/p )^{-k}
>          ( 1 - nu_p(D)/p )
> for any positive integer Q."

> "Thus the expressions (2) and (3) are equal."   [via (37), (39), taking
> Q = prod_{p<=y} p, y -> infty; displays on p. 14]

> "Suppose that 1 <= d_i <= h for all i. Then nu_p(D) = k for all primes
> p > h, and thus if y >= h, then
> (40)  prod_{p>y} ( 1 - 1/p )^{-k} ( 1 - nu_p(D)/p )
>         = prod_{p>y} ( 1 + O_k(1/p^2) ) = 1 + O_k( 1/(y log y) ).
> Since nu_p(D) >= 1 for all p, it is evident that
> (41)  prod_{p<=h} ( 1 - 1/p )^{-k} ( 1 - nu_p(D)/p )
>         <<_k (log h)^{k-1}.
> On combining this with (40), we see that
> (42)  S(D) << (log h)^{k-1}.
> From (5) it follows additionally that
> (43)  S_0(D) << (log h)^{k-1}."

Truncated singular series (p. 15), verbatim:

> "From (39)-(41) we see that if 1 <= d_i <= h for all i and y >= h, then
> (44)  S(D) = sum_{q_1,...,q_k, p|q_i => p<=y} prod_{i=1}^k
>         ( mu(q_i)/phi(q_i) ) A(q_1,...,q_k) + O_k( (log y)^{k-2} / y ).
> By combining this with (5), we see also that
> (45)  S_0(D) = sum_{q_1,...,q_k, q_i>1, p|q_i => p<=y} prod_{i=1}^k
>         ( mu(q_i)/phi(q_i) ) A(q_1,...,q_k) + O_k( (log y)^{k-2} / y )."

LEMMA 4 (p. 15), verbatim (the k=2 evaluation):

> "Lemma 4. Let E(alpha) be defined as in (14). If q is divisible by every
> prime number p <= h^2, then
> (46)  sum_{d|q} mu(d)^2/phi(d)^2 ( sum_{a=1, (a,d)=1}^d |E(a/d)|^2
>         - phi(d) h ) = h^2 - h log h + Bh + O( h^{1/2+eps} )
> where B = 1 - C_0 - log 2pi and C_0 denotes Euler's constant."

(Proof anatomy, pp. 15-16, paraphrase with verbatim fragments:
|E(alpha)|^2 = sum_{|m|<=h} (h - |m|) e(m alpha); the a-sum becomes
sum_{|m|<=h} (h-|m|) c_d(m) with c_d(m) Ramanujan's sum; c_d(0) = phi(d),
c_d(-m) = c_d(m); the LHS of (46) equals
"2 sum_{m=1}^h (h-m) sum_{d|q} mu(d)^2/phi(d)^2 c_d(m)"; the d-sum is
"prod_{p|q} (1 + c_p(m)/(p-1)^2) = prod_{p|q, p|m} (1 + 1/(p-1))
prod_{p|q, p not| m} (1 - 1/(p-1)^2)"; since q contains all p <= h^2 the
main term is exactly the pair singular series:
"= prod_{p|m} (1 - 1/p)^{-2} (1 - 1/p) x prod_{p not| m} (1 - 1/p)^{-2}
(1 - 2/p) = S({0,m})" (p. 16, top display) plus O(1/h^2). Then, verbatim:)

> "Goldston [7] has shown that
> (47)  2 sum_{m=1}^h (h - m) S({0,m}) = h^2 - h log h + Bh
>         + O( h^{1/2+eps} ),
> so we have the stated estimate."
> "It is worth noting that (47) can also be written in the form
> (48)  sum_{d_1,d_2, 1<=d_i<=h, d_1 != d_2} S({d_1,d_2})
>         = h^2 - h log h + Bh + O( h^{1/2+eps} )."

> "The term d = 1 contributes h^2 - h to the left hand side of (46). Thus
> if q is divisible by every prime not exceeding h^2, then
> (49)  sum_{d|q, d>1} mu(d)^2/phi(d)^2 ( sum_{a=1, (a,d)=1}^d
>         |E(a/d)|^2 - phi(d) h ) = -h log h + Ah + O( h^{1/2+eps} )
> where A = 2 - C_0 - log 2pi."   (p. 16)

Main body of the proof of Theorem 2 (p. 16), verbatim:

> "We now begin the main body of the proof of Theorem 2. We apply (45)
> with y = h^{k+1}, and set Q = prod_{p<=y} p. Thus
> (50)  R_k(h) = sum_{q_1,...,q_k, 1<q_i, q_i|Q} prod_{i=1}^k
>         ( mu(q_i)/phi(q_i) ) S(q_1,...,q_k;h) + O(1)
> where
> (51)  S(q_1,...,q_k;h) = sum_{d_1,...,d_k, 1<=d_i<=h, d_i distinct}
>         sum_{a_1,...,a_k, 1<=a_i<=q_i, (a_i,q_i)=1, sum a_i/q_i in Z}
>         e( sum_{i=1}^k a_i d_i/q_i )."

> "By comparing (50) with (12) we find that if the condition that the d_i
> should be distinct were omitted, then the main term in (50) would be
> exactly V_k(Q;h). The bulk of our argument is devoted to an effort to
> remove this condition."   (pp. 16-17)

Distinctness removal: the delta-symbol / partition calculus (p. 17),
verbatim fragments plus paraphrase:

> "Put delta_{i,j} = 1 if d_i = d_j, delta_{i,j} = 0 otherwise. Thus
>   prod_{1<=i<j<=k} (1 - delta_{i,j}) = { 1 if the d_i are distinct;
>                                        { 0 otherwise."

(Paraphrase: expanding the product gives a signed sum of delta-products;
delta-products are grouped into equivalence classes indexed by partitions
P = {S_1,...,S_M} of {1,...,k}, each class containing a unique canonical
Delta_P = prod_{m=1}^M prod_{i<j, i,j in S_m} delta_{i,j}; with weight)

> "w(P) = sum_{Delta ~ Delta_P} (-1)^{|Delta|}"

(the paper concludes:)

> "(52)  S(q_1,...,q_k;h) = sum_P w(P) sum_{a_1,...,a_k, 1<=a_i<=q_i,
>          (a_i,q_i)=1, sum a_i/q_i in Z} prod_{m=1}^M
>          E( sum_{i in S_m} a_i/q_i )
> where P = {S_1,...,S_M}."

> "If there is a prime p such that p|q_i for exactly one i, then the
> condition sum a_i/q_i in Z cannot be fulfilled with (a_i,q_i) = 1, so the
> sum (52) is empty, and hence S(q_1,...,q_k;h) = 0. We therefore assume
> that each prime dividing [q_1,...,q_k] divides at least two of the q_i."
> (p. 17)

Partition bookkeeping (pp. 17-18, paraphrase): M-script = {1,...,M};
M_1 = singleton parts (m_1 = card), M_2 = parts of size >= 2 (m_2 = card),
N_1 = union of singleton parts (n_1 = card), N_2 = union of larger parts
(n_2 = card); m_1 + m_2 = M, n_1 + n_2 = k, m_1 = n_1. Partitions with
some part of size >= 3 are error terms: bound each singleton factor by
F(a_i/q_i) via (27) and each larger-part factor trivially by
"|E( sum_{i in S_m} a_i/q_i )| <= h" (p. 18, verbatim), then apply Lemma 1,
giving (53); with (p. 18, verbatim)

> "(54)  sum_{a=1}^{q-1} F(a/q)^2 << q min(q,h),"

the expression (53) is "<< (q_1...q_k/[q_1,...,q_k]) h^{n_1/2 + m_2}"
(p. 18, verbatim). Then (p. 18, verbatim):

> "The n_2 members of N_2 are partitioned into m_2 sets, each one
> containing at least two members, and at least one containing 3 or more
> numbers. Thus
>   n_2 = sum_{m in M_2} card S_m >= 1 + 2 sum_{m in M_2} 1 = 1 + 2 m_2,
> and hence
>   n_1/2 + m_2 <= (n_1 + n_2 - 1)/2 = (k-1)/2."

The k-dependent modulus sum (p. 19), verbatim (LOAD-BEARING for the
growing-k question):

> "We also observe that
>   sum_{q_1,...,q_k, q_i|Q} ( prod_{i=1}^k mu(q_i)^2/phi(q_i) )
>     (q_1 ... q_k) / [q_1,...,q_k]
>   <= sum_{d|Q} (1/d) ( sum_{q|d} q/phi(q) )^k
>   = sum_{d|Q} prod_{p|d} ... = prod_{p|Q} ( 1 + (1/p)( 1 +
>     p/(p-1) )^k ) <<_k (log h)^{2^k}."

[TRANSCRIPTION-UNSURE: the middle members of this chain are dense; the
first and last members, in particular the final bound <<_k (log h)^{2^k},
are clearly legible.]

> "Thus we have shown that
> (55)  R_k(h) = sum_{P, card S_m <= 2} w(P) sum_{q_1,...,q_k, 1<q_i|Q}
>         prod_{i=1}^k ( mu(q_i)/phi(q_i) ) sum_{a_1,...,a_k, 1<=a_i<=q_i,
>         (a_i,q_i)=1, sum a_i/q_i in Z} prod_{m=1}^M
>         E( sum_{i in S_m} a_i/q_i )  +  O( h^{(k-1)/2 + eps} )."
> (p. 19)

Doubleton partitions (p. 19), verbatim:

> "Suppose that the partition P consists of j doubleton sets and k - 2j
> singleton sets. Since no other delta-product is equivalent to Delta_P,
> and |Delta_P| = j, so w(P) = (-1)^j. The number of such partitions is
>   binom(k, 2j) (2j)!/(j! 2^j).
> Since the q_i are interchangeable, we multiply by the above factor, and
> restrict our attention to one such partition: doubletons {i, i+j} for
> 1 <= i <= j and singletons {i} for 2j+1 <= i <= k. Thus the main term in
> (55) is
> (56)  sum_{0<=j<=k/2} (-1)^j binom(k,2j) ( (2j)!/(j! 2^j) )
>         sum_{q_1,...,q_k, 1<q_i|Q} prod_{i=1}^k ( mu(q_i)/phi(q_i) )
>         sum_{a_1,...,a_k, 1<=a_i<=q_i, (a_i,q_i)=1, sum a_i/q_i in Z}
>         prod_{i=1}^j E( a_i/q_i + a_{i+j}/q_{i+j} )
>         prod_{i=2j+1}^k E( a_i/q_i )."

The doubleton convolution H(b/r) (p. 19), verbatim:

> "For 1 <= i <= j, let b_i and r_i be defined by the relations
>   b_i/r_i == a_i/q_i + a_{i+j}/q_{i+j} (mod 1), 1 <= b_i <= r_i,
>   (b_i, r_i) = 1,
> and put
> (57)  H(b/r) = E(b/r) sum_{d_1,d_2, 1<d_i|Q} ( mu(d_1)mu(d_2) /
>         (phi(d_1)phi(d_2)) ) sum_{c_1,c_2, 1<=c_i<=d_i, (c_i,d_i)=1,
>         c_1/d_1 + c_2/d_2 == b/r (mod 1)} 1."

Separation by ell = number of r_i > 1 (p. 20), verbatim:

> "(58)  sum_{ell=0}^j binom(j, ell) H(1)^{j-ell} M(ell)
> where
>   M(ell) = sum_{r_1,...,r_ell, 1<r_i|Q} sum_{b_1,...,b_ell, 1<=b_i<=r_i,
>     (b_i,r_i)=1} prod_{i=1}^ell H(b_i/r_i) sum_{q_{2j+1},...,q_k,
>     1<q_i|Q} sum_{a_{2j+1},...,a_k, 1<=a_i<=q_i, (a_i,q_i)=1,
>     sum a_i/q_i + sum b_i/r_i in Z} prod_{i=2j+1}^k
>     ( mu(q_i)/phi(q_i) ) E( a_i/q_i ).
> We note that M(0) = V_{k-2j}(Q;h)."

[TRANSCRIPTION-UNSURE: the subscript of V in "M(0) = V_{k-2j}(Q;h)"
renders ambiguously (could be misread as 2k-j); k-2j is forced by (12) and
by the appearance of V_{k-2j}(Q;h) in (60).]

ell > 0 absorbed into the error (pp. 20-21), paraphrase with verbatim
fragments: if a prime divides exactly one of r_1,...,r_ell,
q_{2j+1},...,q_k the sum vanishes; so every prime divisor of
d = [q_{2j+1},...,q_k, r_1,...,r_ell] divides at least two, and Lemma 1
gives (59): M(ell) bounded by a product of quadratic means of |H(b/r_i)|
and F(a/q_i). H(b/r) is then estimated via CRT (d_i = s_i t_i, s_i | r,
t_i | Q/r; conditions force [s_1,s_2] = r, t_1 = t_2, f_1 + f_2 == 0
(mod t_1)), giving (p. 21, verbatim):

> "H(b/r) << F(b/r) ( 3^{omega(r)} / r ) prod_{p|Q} ( 1 + 1/(p-1) )
>   << F(b/r) ( 3^{omega(r)} / r ) log h ."

[TRANSCRIPTION-UNSURE: the intermediate member of this chain; the final
form F(b/r) 3^{omega(r)} r^{-1} log h is clearly legible.]

> "By (54) it follows that
>   sum_{b=1}^{r-1} | H(b/r) |^2 << (h/r) 9^{omega(r)} (log h)^2 ."
> (p. 21, verbatim)

> "On inserting this and (54) in (59), we find that
>   M(ell) << ... << h^{(k-2j+ell)/2} (log h)^ell sum_{d|Q} (1/d)
>     ( sum_{r|d} 3^{omega(r)} )^ell ( sum_{q|d} q/phi(q) )^{k-2j}
>   <= h^{(k-2j+ell)/2} (log h)^ell prod_{p|Q} ( 1 + 4^{k-2j+ell}/p )
>   << h^{(k-2j+ell)/2 + eps}."
> (p. 21, verbatim modulo the elided first member)

[TRANSCRIPTION-UNSURE: middle members of the M(ell) chain; the final bound
h^{(k-2j+ell)/2+eps} and the factor prod_{p|Q}(1 + 4^{k-2j+ell}/p) are
legible. Note this absorption of prod_{p|Q}(1 + 4^{k-2j+ell}/p) into h^eps
is another fixed-k step: the product is of size (log y)^{4^{k-2j+ell}}.]

> "From (57) we see that
>   H(1) = h sum_{d|Q, d>1} mu(q)^2/phi(q).
> Hence the expression (58) is
>   ( h sum_{d|Q, d>1} mu(q)^2/phi(q) )^j V_{k-2j}(Q;h)
>     + O( h^{(k-1)/2+eps} )."
> (p. 21, verbatim)

[PRINTED-ODDITY: the summation variable is printed d, the summand uses
mu(q)^2/phi(q); in (60) the same sum is printed with d throughout.]

Assembly (p. 22), verbatim:

> "On inserting this in (56), we find that
> (60)  R_k(h) = sum_{0<=j<=k/2} binom(k,2j) ( (2j)!/(j! 2^j) )
>         ( -h sum_{d|Q, d>1} mu(d)^2/phi(d) )^j V_{k-2j}(Q;h)
>         + ( h^{(k-1)/2 + eps} )."

[PRINTED-ODDITY: the final error term appears without an O( ) as printed.]

> "We are at last prepared to make our appeal to Theorem 1. If k is odd
> then k - 2j is odd, so there is no main term. Suppose that k is even.
> Then the main term is
>   sum_{0<=j<=k/2} binom(k,2j) ( (2j)!/(j! 2^j) ) ( -h sum_{d|Q, d>1}
>     mu(d)^2/phi(d) )^j ( (k-2j)! / ( (k/2-j)! 2^{k/2-j} ) )
>     V_2(Q;h)^{k/2-j}
>   = ( k! / ( (k/2)! 2^{k/2} ) ) sum_{j=0}^{k/2} binom(k/2, j)
>     V_2(Q;h)^{k/2-j} ( -h sum_{d|Q, d>1} mu(d)^2/phi(d) )^j
>   = mu_k ( V_2(Q;h) - h sum_{d|Q, d>1} mu(d)^2/phi(d) )^{k/2}
> by the binomial theorem.
>   By (49) we see that the above is
>   mu_k ( -h log h + Ah )^{k/2} + O( h^{(k-1)/2 + eps} ).
> This gives the stated result."

[Note: (49) applies because Q = prod_{p <= y} p with y = h^{k+1} >= h^2,
and V_2(Q;h) - h sum_{d|Q,d>1} mu(d)^2/phi(d) is exactly the left side of
(49) by (13). Connective paraphrase.]

---

## 8. METHOD ANATOMY C: PROOF OF THEOREM 3 (Section 3, pp. 22-26)

Low moments (p. 22), verbatim:

> "Clearly M_0(N;H) = N. Thus we have the case K = 0 of (21)
> unconditionally, and with no error term. It is also convenient to
> dispose of the case K = 1 before proceeding to the main argument. Since
> S({h}) = 1, it follows from our hypothesis (20) that
> sum_{n=1}^N Lambda(n+h) = N + O(N^{1/2+eps}). Hence
> sum_{n=1}^N Lambda_0(n+h) << N^{1/2+eps}, and thus by (19) we see that
> M_1(N;H) << H N^{1/2+eps}, which suffices."

Fixed-K declaration (p. 22), verbatim:

> "From now on we assume that K is fixed, K >= 2, and we ignore possible
> dependence of implicit contstants on K."   ["contstants" sic]

Multiplicity expansion (pp. 22-23), verbatim fragments plus paraphrase:
Let D = {d_1,...,d_k} be k distinct integers, 1 <= d_i <= H; suppose the
h_i in (19) take the values d_i with multiplicities M_i; then the right
hand side of (19) is (61), a sum over k, over compositions
(M_1,...,M_k), M_i >= 1, sum M_i = K, with multinomial weight
binom(K; M_1...M_k)/k!, of sum over distinct d_i and n of
prod Lambda_0(n+d_i)^{M_i}. "For positive integers m we put
Lambda_m(n) = Lambda(n)^m Lambda_0(n)" (p. 22, verbatim); the binomial
theorem gives Lambda_0(n)^M = sum_{m=0}^{M-1} (-1)^{M-m-1}
binom(M-1, m) Lambda_m(n) (p. 22, display), leading to (62) with

> "(63)  L_k(m) = sum_{d_1,...,d_k, 1<=d_i<=H, d_i distinct} sum_{n=1}^N
>          prod_{i=1}^k Lambda_{m_i}(n + d_i)."   (p. 23)

Splitting by m_i = 0 vs m_i > 0 (p. 23): K-script = {1,...,k}, H-script =
{i : m_i >= 1} with h = card, I-script = {i : m_i = 0} with k - h = card.
The identity

> "prod_{i in I} Lambda_0(n+d_i) prod_{i in H} Lambda(n+d_i)
>   = sum_{J, I subseteq J subseteq K} prod_{i in J} Lambda_0(n + d_i)"
> (p. 23, display, paraphrased indexing)

plus hypothesis (20) gives (p. 23, verbatim):

> "sum_{n<=x} prod_{i in I} Lambda_0(n+d_i) prod_{i in H} Lambda(n+d_i)
>   = x sum_{J, I subseteq J subseteq K} S_0(D_J) + O( N^{1/2+eps} )
> uniformly for 0 <= x <= N where D_J = {d_i : i in J}."

Partial summation converts Lambda to Lambda_m weights: (64), (65) (pp.
23-24); "For m > 0, Lambda_m(n) is nonzero only when n is a primepower,
and Lambda_m(n) = Lambda(n) (log n)^{m-1} (log n - 1) if n is prime"
(p. 24, verbatim); prime powers contribute << N^{1/2+eps}, giving (66).
Then (p. 24, verbatim):

> "(67)  sum_{i in H} m_i = sum_{i=1}^k m_i <= sum_{i=1}^k (M_i - 1)
>          = K - k ."

> "If x >= 1 and 1 <= d <= H, then log(x+d) = log x + O(d/x) = log x +
> O(H/x)."  (p. 24, verbatim)

> "I_m(N) = int_1^N prod_{i in H} ( (log x)^{m_i - 1} (log x - 1) ) dx."
> (p. 24, display; m in bold in the paper)

> "On assembling our estimates, we find that
>   sum_{n=1}^N prod_{i=1}^k Lambda_{m_i}(n+d_i)
>     = ( sum_{J, I subseteq J subseteq K} S_0(D_J) )
>       ( I_m(N) + O( H (log N)^{K-k} ) ) + O( N^{1/2+eps} )."
> (p. 24, verbatim)

> "By (43) we see that the first error term is << H (log N)^K
> << N^{1/K+eps} << N^{1/2+eps}, since H <= N^{1/K} and K >= 2."
> (p. 25, verbatim)

Summing over distinct d_i, using Theorem 2 as an a-priori bound (p. 25),
verbatim:

> "Once the d_i have been chosen for i in J, there are
> (H-j)(H-j-1)...(H-k+1) ways of choosing the remaining d_i. Hence the
> above is
>   = I_m(N) sum_{J, I subseteq J subseteq K} R_j(H)(H-j)...(H-k+1)
>     + O( H^k N^{1/2+eps} ).
> The product in the sum is H^{k-j} + O(H^{k-j-1}). By Theorem 2 we know
> that R_j(H) << (H log H)^{j/2}, and using this we see that (isolating
> the term J = I)
>   sum_{J} R_j(H)(H-j)...(H-k+1)
>     = R_{k-h}(H)( H^h + O(H^{h-1}) )
>       + O( sum_{k-h+1<=j<=k} (H log H)^{j/2} H^{k-j} )
>     = R_{k-h}(H) H^h + O( (H log H)^{(k-h+1)/2} H^{h-1} ).
> Therefore
> (68)  L_k(m) = I_m(N) ( R_{k-h}(H) H^h + O( (H log H)^{(k-h+1)/2}
>         H^{h-1} ) ) + O( H^k N^{1/2+eps} )."

Size bookkeeping (p. 25), verbatim:

> "(69)  K = sum_{i=1}^k M_i = sum_{i in H} M_i + sum_{i in I} M_i
>          >= 2 card H + card I = 2h + (k-h) = h + k .
> By (67) we see that
> (70)  I_m(N) ~ N (log N)^{sum_{i in H} m_i} << N (log N)^{K-k}."

> "First we show that terms for which h + k < K contribute a negligible
> amount to (62). Since R_{k-h}(H) << (H log H)^{(k-h)/2} by Theorem 2, it
> follows from (68), (69), and (70) that
>   L_k(m) << N (log N)^{K-k} (H log H)^{(k-h)/2} H^h + H^k N^{1/2+eps}
>     << N (log N)^K ( H/log N )^{(k+h)/2} ( log H/log N )^{(k-h)/2}
>        + H^K N^{1/2+eps}."   (p. 25)

> "Thus the contribution of these terms to (62) is
> (71)  << N (log N)^K ( H/log N )^{(K-1)/2} + H^K N^{1/2+eps}."  (p. 26)

The main (h + k = K) terms (p. 26), verbatim:

> "Finally we consider those terms in (62) for which h + k = K. Since
> h <= k, it follows that k >= K/2. We also have card H = h = K - k, and
> card I = k - h = 2k - K. Since equality holds in (69), it follows that
> M_i = 2 for all i in H and that M_i = 1 for all i in I. Thus
> m_i = M_i - 1 for all i, and for such m we have
>   I_m(N) = int_1^N (log x - 1)^{K-k} dx = I_{K-k}(N),
> say."

> "(72)  M_K(N;H) = sum_{K/2<=k<=K} ( K! / (k! 2^{K-k}) )
>          binom(k, K-k) I_{K-k}(N) R_{2k-K}(H) H^{K-k}
>          + O( N (log N)^K ( H/log N )^{(K-1)/2} )
>          + O( H^K N^{1/2+eps} )."

[Between the two displays the paper computes L_k(m) for these m and notes
"Once k is selected, there are precisely binom(k, K-k) ways of choosing
the set H" (p. 26, verbatim fragment).]

Endgame (p. 26), verbatim:

> "Suppose that K is odd. Then so also is 2k - K, and hence by Theorem 2
> the main terms in (72) are << N (log N)^{K/2} H^{K/2 - 1/(7K) + eps}.
> Thus in this case
>   M_K(N;H) << N (log N)^{K/2} H^{K/2 - 1/(7K)+eps}
>     + N (log N)^K ( H/log N )^{(K-1)/2} + H^K N^{1/2+eps}
>   << N (log N)^{K/2} H^{K/2} ( H/log N )^{-1/(8K)} + H^K N^{1/2+eps}."

> "Suppose that K is even. By Theorem 2 it follows that
>   M_K(N;H) = H^{K/2} sum_{k=K/2}^K ( K! / (k! 2^{K-k}) )
>     binom(k, K-k) mu_{2k-K} I_{K-k}(N) ( -log H + A )^{k - K/2}
>     + O( N (log N)^{K/2} H^{K/2} ( H/log N )^{-1/(8K)}
>       + H^K N^{1/2+eps} ).
> Since mu_k = k!/((k/2)! 2^{k/2}) when k is even, on writing k = K/2 +
> ell we see that the main term above is
>   mu_K H^{K/2} sum_{ell=0}^{K/2} binom(K/2, ell) I_{K/2 - ell}(N)
>     ( -log H + A )^ell.
> On taking the sum inside the integral, we obtain the stated result by
> the binomial theorem."

[Connective note, paraphrase: inside the integral the binomial theorem
gives (log x - 1 - log H + A)^{K/2} = (log(x/H) + B)^{K/2} with
B = A - 1 = 1 - C_0 - log 2pi, which is the main term of (21).]

---

## 9. SECTION 4: HEURISTICS IN THE MANNER OF HARDY & LITTLEWOOD
## (pp. 27-28)

Setup (p. 27), paraphrase with verbatim fragments: S(alpha) =
sum_{n=1}^N Lambda(n) e(n alpha); by PNT in progressions "S(a/q) ~
mu(q) N/phi(q) provided that q is not too large as a function of N"; by
partial summation "S(alpha) ~ mu(q) M(alpha - a/q)/phi(q) for alpha near
a/q, where M(beta) = sum_{n=1}^N e(n beta)". With E(alpha) =
sum_{m=1}^h e(m alpha), the product S(alpha)E(-alpha) is approximately
sum_n (sum_{m=1}^h Lambda(m+n)) e(n alpha); subtracting the a = q = 1
term:

> "sum_{n=1}^N ( sum_{m=1}^h Lambda(m+n) - h ) e(n alpha)
>   =. sum_{1<q<=N} ( mu(q)/phi(q) ) sum_{a=1, (a,q)=1}^q
>      E(a/q) M(alpha - a/q)."   (p. 27, display; "=." is the paper's
>      dotted equality)

The k-fold convolution of the left side F(alpha) with itself, evaluated at
alpha = 0, "follow[ing] Hardy & Littlewood in assuming that the main term
arises by the alignment of the peaks in the multiple integral" (p. 27,
verbatim fragment), yields:

> "sum_{n=1}^N ( sum_{m=1}^h Lambda(m+n) - h )^k ~ N
>   sum_{q_1,...,q_k, 1<q_i<=N} ( prod_{i=1}^k mu(q_i)/phi(q_i) )
>   sum_{a_1,...,a_k, 1<=a_i<=q_i, (a_i,q_i)=1, sum a_i/q_i in Z}
>   prod_{i=1}^k E(a_i/q_i)."   (p. 27, display)

Diagonal analysis (p. 28), verbatim:

> "We note that |E(beta)| asymp h if ||beta|| <= 1/h, and that
> E(beta) << 1/||beta|| if ||beta|| >= 1/h. The asymptotic size of the
> right hand side above could be determined by using the techniques used
> to prove Theorem 1. At this point we are content to argue more
> informally. If k is odd then the terms do not make a very significant
> contribution. On the other hand, when k is even, we find 'diagonal
> terms' in which the q_i are equal in pairs, with the corresponding a_i
> being the negatives of each other. The pairings can be made in
> (k-1)(k-3)...3*1 = mu_k ways, so the contribution of these terms is
>   mu_k N sum_{q_1,...,q_{k/2}, 1<q_i<=N} prod_{i=1}^{k/2}
>     ( mu(q_i)^2/phi(q_i)^2 sum_{a_i=1, (a_i,q_i)=1}^{q_i}
>     |E(a_i/q_i)|^2 )
>   = mu_k N ( sum_{1<q<=N} mu(q)^2/phi(q)^2 sum_{a=1, (a,q)=1}^q
>     |E(a/q)|^2 )^{k/2}."

> "If there are further equalities among the q_i beyond this pairing, then
> the combinatorics must be adjusted, but such configurations contribute a
> lesser amount. Likewise, that the non-diagonal terms contribute a lesser
> amount can be demonstrated by using the techniques we used to prove
> Theorem 1. If q < h then the inner sum above is
> << sum_{0<a<q} ||a/q||^{-2} << q^2, but if q >= h then the inner sum is
> approximately h phi(q). Since
>   sum_{q<=y} mu(q)^2/phi(q) = log y + O(1),
> it follows that the expression to be estimated is
>   ~ mu_k N ( h log N/h )^{k/2},
> which supports the Conjecture."   (p. 28)

---

## 10. UNIFORMITY IN k: ALL EXPLICIT STATEMENTS AND INTERNAL
## k-DEPENDENCE (focus question 4)

Explicit remarks (all verbatim, quoted in full above):

1. p. 4, after Theorem 1: "We remark that the work of Granville &
   Soundararajan [7] (see Sec 6a) places restrictions on the uniformity
   (in k) with which (15) can possibly hold." [Reference = the
   Granville-Soundararajan uncertainty-principle paper, item 9 of the
   list; numeral as printed is 7. This is the paper's ONLY explicit
   remark about obstacles to k growing.]
2. p. 6: "For larger H, Theorem 3 furnishes only a limited number of
   moments and we cannot deduce a distribution result."
3. p. 9 (proof of Theorem 1): "We take k to be fixed, so that the
   dependence of implicit constants on k is suppressed."
4. p. 22 (proof of Theorem 3): "From now on we assume that K is fixed,
   K >= 2, and we ignore possible dependence of implicit contstants
   on K."

Range-of-k inventory for each result (statements verbatim in Parts 3-4):

- Theorem 1 (15): "for every positive integer k", with O_k error;
  constants not tracked (see remark 3 above). The error carries the
  factor (q/phi(q))^{2^k + k/2} and the saving h^{-1/(7k)}, both
  degrading as k grows.
- Theorem 2: "for any nonnegative integer k", with O_k(h^{k/2 - 1/(7k)
  + eps}); the proof's k-dependence enters at least through: y = h^{k+1}
  and Q = prod_{p<=y} p (p. 16); the bound <<_k (log h)^{2^k} (p. 19);
  the factor prod_{p|Q}(1 + 4^{k-2j+ell}/p) absorbed into h^eps (p. 21);
  and Theorem 1's error via (60).
- Theorem 3 / (21): K enters the hypothesis (20) ("uniformly for
  1 <= k <= K"), the admissible range log N <= H <= N^{1/K}, and the
  error factor (H/log N)^{-1/(8K)}; K fixed (remark 4).
- Corollary 1: requires "(20) holds for arbitrarily large K", but each K
  is used at fixed value; the H-range is log H/log N -> 0.
- Conjecture 1: "For each positive integer K" -- fixed K, uniformity
  only in H.

There is NO theorem in the paper in which k (or K) grows with h (or N).
A "second moment of singular series at growing k" statement is NOT FOUND
in this text; the k = 2 second-moment statements are (16), (47), (48),
(49), unconditional with error O(h^{1/2+eps}).

---

## 11. NOT FOUND ITEMS (searched for, absent)

The following, relevant to the consuming project, do NOT occur anywhere
in the paper (verified against all 29 pages):

- Prime gaps g_n = p_{n+1} - p_n appear ONLY in the Cramer-model display
  on p. 1 (card{n <= N : p_{n+1} - p_n > c log p_n} ~ e^{-c} N); no
  theorem about gaps or gap patterns is stated or proved.
- No statement about words/blocks of consecutive gaps, tuples of
  consecutive primes, Shiu strings, or congruence patterns of consecutive
  primes.
- No irrationality, base-2/binary digits, series sum p_n/2^n, or Erdos
  problem numbers of any kind.
- No lower-bound existence statements for prime configurations
  (everything about actual primes is conditional on (20)); no parity
  discussion.
- No uniform-in-k version of Theorems 1-3 and no quantified k(h) -> infty
  regime (only the restriction remark, Part 10 item 1).

References (pp. 28-29), 20 items; those load-bearing above: [4] Cramer
1936; [6] Gallagher, Mathematika 23 (1976) 4-9; [7] Goldston, Glasgow
Math. J. 32 (1990) 285-297; [9] Granville & Soundararajan, "An
uncertainty principle for arithmetic sequences", preprint (arxiv.org);
[10] Hardy & Littlewood, Acta Math. 44 (1922) 1-70; [11] Hausman &
Shapiro, Comm. Pure App. Math. 26 (1973) 539-547; [12] Maier, Michigan
Math. J. 32 (1985) 221-225; [16] Montgomery & Vaughan, "On the
distribution of reduced residues", Annals of Math. 123 (1986) 311-333;
[20] Selberg, Collected papers I, 1989, 160-178.

---

## FLAGS (consolidated)

1. [TRANSCRIPTION-UNSURE] Citation numerals on pp. 4, 7 as printed
   ("Granville & Soundararajan [7]", "Maier [11]", "Selberg [18]")
   conflict with the reference list ([9], [12], [20]); author names are
   unambiguous in all three places.
2. [TRANSCRIPTION-UNSURE] Corollary 1: radical in "c sqrt(H log N)" is
   small in the scan (p. 6).
3. [TRANSCRIPTION-UNSURE] p. 2: "pi(x+h) - pi(h)" as printed (intended
   pi(x+h) - pi(x)).
4. [TRANSCRIPTION-UNSURE] p. 3, before (13): "q_1 = q_2 = a_1 + a_2" as
   printed (intended q_1 = q_2, q_1 | a_1 + a_2).
5. [TRANSCRIPTION-UNSURE] p. 5 remark: "not necessarily distinct m_i"
   (contextually d_i).
6. [TRANSCRIPTION-UNSURE] p. 19 modulus-sum chain and p. 21 H(b/r) and
   M(ell) chains: middle members dense; first/last members (in
   particular <<_k (log h)^{2^k}, F(b/r) 3^{omega(r)} r^{-1} log h,
   h^{(k-2j+ell)/2+eps}) clearly legible.
7. [TRANSCRIPTION-UNSURE] p. 20: "M(0) = V_{k-2j}(Q;h)" subscript
   rendering; k-2j forced by (12) and (60).
8. [PRINTED-ODDITY] p. 21: "H(1) = h sum_{d|Q,d>1} mu(q)^2/phi(q)"
   mixes d and q; (60) prints d throughout.
9. [PRINTED-ODDITY] (60): final error term "( h^{(k-1)/2+eps} )" printed
   without O( ).
10. [PRINTED-ODDITY] p. 22: "contstants" sic.
11. [PARAPHRASE] marked inline throughout: proofs of Lemmas 2-4, the
    partition bookkeeping (pp. 17-18), the CRT analysis of H(b/r)
    (pp. 20-21), the Lambda_m partial-summation steps (pp. 23-24), and
    Section 4 connective tissue. All quantitative claims are quoted
    verbatim with anchors.

---

## COMMENTARY (assessment, NOT extraction)

This section answers the focus questions and assesses transfer value for
the project target: an UNCONDITIONAL supply of two prime-gap-word sites
with matched J-prefix and K-suffix windows and dominant weighted middle
difference, at depths J, K ~ log2 log x ("exchange configuration").

(C1) Answers to the focus questions.

Focus 1 (main results and hypotheses). Unconditional: Theorem 1 (eq.
(15), p. 4) and Theorem 2 (p. 4), plus (16), (17), (42)-(49) -- these are
pure arithmetic statements about singular-series averages, no RH or
Hardy-Littlewood input. Conditional: Theorem 3 (eqs. (20)-(21), p. 5)
assumes a uniform Hardy-Littlewood k-tuple asymptotic with square-root
error for all 1 <= k <= K, all x <= N, all distinct shifts d_i <= H --
and its k = 1 case is already equivalent to RH (p. 5 remark). Corollary 1
(p. 6) needs (20) for arbitrarily large K. Conjectures 1-2 (p. 6) are the
paper's variance-H log(N/H) normality conjectures for
(log N)^{1+delta} <= H <= N^{1-delta}.

Focus 2 (singular-series moment machinery). The objects are S(D) (2)/(3),
S_0(D) (5)/(6)/(9), R_k(h) (8) (moments of S_0 over DISTINCT k-tuples in
[1,h]), and V_k(q;h) (12) (same shape, d_i NOT distinct, moduli dividing
q), tied to the reduced-residue moments m_k(q;h) by (10)-(11). Exact
asymptotics proved: (15) V_k = mu_k V_2^{k/2} + O_k(h^{k/2-1/(7k)}
(q/phi(q))^{2^k+k/2}); Theorem 2: R_k(h) = mu_k(-h log h + Ah)^{k/2}
+ O_k(h^{k/2-1/(7k)+eps}); (16)/(48): the k = 2 case with error
O(h^{1/2+eps}); (17): the refined Gallagher mean. Range of k: FIXED in
every theorem ("for every positive integer k" with untracked O_k;
explicit fixed-k declarations p. 9, p. 22). No growing-k statement exists
in the paper (Part 10, Part 11).

Focus 3 (method). Theorem 1: Montgomery-Vaughan basic inequality (Lemma
1, p. 8) plus the new variant Lemma 2 (p. 8, hypothesis (24)); pairing
reduction imported from MV Lemmas 7-8; J(b,r) bounds (26), (31)-(34);
W_j bound << h^{j/2}(q/phi(q))^{2^j} (p. 11). Theorem 2: Hardy-Littlewood
local factorization (Lemma 3, (35)-(37)); truncation (44)-(45) at
y = h^{k+1}; Lemma 4's Ramanujan-sum evaluation (46) resting on
Goldston's unconditional (47); the delta-symbol/partition calculus
removing the distinctness condition ((52)-(56)); the doubleton
convolution H(b/r) analysis ((57)-(59), pp. 20-21); binomial assembly
(60) feeding Theorem 1 and (49). Theorem 3: multiplicity/partition
expansion (61)-(63), Lambda_m partial summation (64)-(67), a priori use
of Theorem 2 as upper bound and as asymptotic ((68)-(72)).

Focus 4 (uniformity in k). One explicit remark: p. 4, restrictions on
uniformity in k of (15) from the Granville-Soundararajan uncertainty
principle. All proofs fix k; the visible internal k-dependence is
DOUBLY EXPONENTIAL: (q/phi(q))^{2^k + k/2} in (15), <<_k (log h)^{2^k}
at p. 19, prod_{p|Q}(1 + 4^{k-2j+ell}/p) at p. 21, plus the vanishing
saving h^{-1/(7k)}. See Part 10.

(C2) What the machinery CAN supply toward the exchange target.

(a) An unconditional, precise "variability meter" -- at the MODEL level.
Theorem 2 with (16)/(48) is exactly a "moments of the singular series"
theorem: the S_0-sums over k-tuples behave like Gaussian moments with
(signed) variance -h log h + Ah. This is the strongest known
unconditional quantification of the tuple-to-tuple variability that
plain pigeonhole is blind to (project blocker (i)): it says the
Hardy-Littlewood weights of h-window configurations fluctuate with
standard deviation ~ sqrt(h log h) around mean values given by (17),
with net pairwise ANTI-correlation (R_2 < 0). If the project can phrase
its "dominant weighted middle difference" as a functional of
singular-series weights over the two windows, Theorem 2 (fixed k) and
(48) (k = 2) are usable off-the-shelf inputs with power-saving errors.

(b) Reusable combinatorics. The distinct-vs-nondistinct bridge
((52)-(60), (61)-(63)) is prime-free bookkeeping (partitions, signed
weights w(P) = (-1)^j on doubleton partitions) and transfers verbatim to
any moment computation over matched tuple windows.

(c) A calibration warning the project should import: Conjecture 1 /
Section 4 say the true variance of interval counts is H log(N/H), not
Cramer's H log N -- i.e., Cramer-model heuristics OVERESTIMATE
variability once windows are polynomially long (pp. 7-8, "inaccurate on
average"). At the project's short depths (windows of polylog length)
the Gallagher Poisson regime (p. 2 display) is the relevant model
statement instead -- but that display is itself conditional on (1).

(C3) What it CANNOT supply.

(a) No unconditional sites. Every statement about actual primes
(Theorem 3, Corollary 1, the a > 1 almost-all version of (23)) is
conditional on (20), whose k = 1 case is RH and whose general case is a
uniform two-sided tuple asymptotic -- precisely the parity-blocked
object of project blocker (ii). The paper never attempts unconditional
lower bounds for prime configurations, so it contributes nothing to
breaking parity; it PRESUPPOSES the broken form as hypothesis (20).

(b) No gap-word control. R_k(h)/V_k(q;h) average over shift SETS
{d_1,...,d_k}; nothing constrains consecutive-gap words or orderings.
Converting "psi-increment moments" into "gap-word site supply" is
exactly the step the paper does not (and cannot, unconditionally) take.

(c) No Shiu-type or growing-k tool. NOT FOUND (Part 11): nothing on
strings/congruence patterns, and no k growing with h anywhere.

(C4) Depth calibration against J, K ~ log2 log x [extractor arithmetic,
not paper content]. The proof of Theorem 2 survives with k growing only
while its worst k-dependent factors stay below the main term
mu_k (h log h)^{k/2} ~ exp((k/2)(log h + log log h) + O(k log k)). The
displayed losses (log h)^{2^k} (p. 19) and (q/phi(q))^{2^k + k/2} with
q/phi(q) asymp log y asymp k log h (p. 16) are exp(2^k log log h)-sized:
they stay subordinate only while 2^k <~ k log h / log log h, i.e.
k <~ log2 log h + O(log2 log2 h). Consequences: (i) if the project's
window length h is polylogarithmic in x (log h asymp log log x), the
method's ceiling is k ~ log2 log log x -- an exponential level BELOW the
needed depth log2 log x; (ii) only if h can be taken as a fixed power of
x (log h asymp log x) does the ceiling k ~ log2 log x match the target
depth, and then only at the boundary, with all O_k constants untracked
and with the p. 4 Granville-Soundararajan restriction standing as a
proved-elsewhere obstruction to full uniformity of (15). So even the
model-level "second moment at growing k" is NOT delivered by this paper
at exchange depth; it would require reproving Theorem 2 with explicit
constants and restructured error terms, and the paper's own remark warns
that (15) cannot hold with unlimited uniformity.

(C5) An unconditional NEGATIVE datum relevant to supply arguments: the
Maier theorem quoted at (23) (p. 7) -- for ANY fixed a > 0 the count
pi(x + (log x)^a) - pi(x) oscillates around its expected value
(log x)^{a-1} in limsup/liminf -- means any exchange-supply argument
requiring regular prime counts in polylog windows AT ALL sites is
unconditionally false; only almost-all/positive-density formulations can
survive (cf. "Presumably (23) is valid for most x", p. 7, and the
conditional almost-all versions of Selberg and Corollary 1). This
sharpens how the project's "supply of two sites" must be quantified:
density of good sites, never universality.

(C6) Net assessment. The paper is the canonical source for exact,
unconditional singular-series moment asymptotics at FIXED k (Theorems
1-2, (16), (17), (48)), i.e. for the model-level second-moment tool the
project seeks -- but it does not supply (and explicitly cautions
against expecting) uniformity in k at anything approaching exchange
depth, and it supplies no unconditional prime-side sites at all: the
prime side is gated entirely by hypothesis (20), which contains RH at
k = 1 and the parity-blocked tuple asymptotics beyond.
