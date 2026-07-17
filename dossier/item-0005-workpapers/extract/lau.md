# EXTRACTION: Lau, "On the Number of Prime Factors of Consecutive Integers"

Source (only evidence base): /home/istr/pro/erdos251/dossier/2604.15042v2.pdf
arXiv:2604.15042v2 [math.NT] 24 Jun 2026. Author: Cheuk Fung (Joshua) Lau,
Mathematical Institute, University of Oxford. 37 pages. MSC 11N56 (11N36).

Transcription conventions: ASCII only. Diacritics transliterated (Erdos,
Teravainen, Cramer, Yildirim). Math in LaTeX-like ASCII: \omega, \Omega, \tau,
\nu_p, <= , >= , << (Vinogradov), >> , \asymp, log_2 x = log log x (the paper's
Section 4 notation: log_j x denotes the j-fold iterated logarithm). (y)_+ =
max{y,0}. \nu_p(n) = p-adic valuation. [m_1,...,m_k] = lcm, (m_1,...,m_k) =
gcd (Section 4, pp. 4-5). Anchors are theorem/equation/section numbers;
page numbers (printed = PDF page) are secondary aid.

Everything up to the final section is EXTRACTION (what the paper says).
Commentary appears ONLY in the final marked section.

---

## 1. ABSTRACT AND MAIN THEOREMS (verbatim)

Abstract (p. 1), verbatim:

> "We prove that there are infinitely many n such that \omega(n + k) << log k
> for all integers k >= 2. This improves on a result of Tao and Teravainen
> (2025), who has O(k) in place of O(log k). As corollaries, we make progress
> on a number of questions posed by Erdos. The proof is based on a
> quantitative refinement of the Tao-Teravainen probabilistic argument,
> combining a more efficient sieve procedure with stronger exponential
> concentration-of-measure estimates. Moreover, we formulate a conjecture on
> integers with many prime factors based on Cramer-type random models.
> Assuming this conjecture, the main bound is essentially sharp."

Introduction framing (Section 1, p. 2), verbatim:

> "Question. Given a function f : N -> N, are there infinitely many integers
> n such that \omega(n + k) <= f(k) for all integers k >= 1?"

> "Here \omega(n) = \sum_{p|n} 1 is the number of distinct prime factors of
> n, and one can ask similar questions for the closely related functions
> \Omega(n) := \sum_{p^j|n} 1 (the number of prime factors counting
> multiplicity) or \tau(n) := \sum_{d|n} 1 (the number of divisors of n). One
> can also ask for \omega(n - k) <= f(k) for all 1 <= k < n, which has
> essentially the same difficulty."

Theorem 1.1 (Section 1, p. 2), verbatim:

> "Theorem 1.1. There exists a positive constant C such that, for infinitely
> many positive integers n, one has \omega(n + k) <= \Omega(n + k) <= C log k
> for every integer k >= 2."

Preceded by (p. 2, verbatim): "In this paper, we prove the following result,
which is an improvement on Theorem 1.1 of Tao and Teravainen (2025)." And:
"Conjecture 1 was recently solved by Tao and Teravainen (2025, Theorem 1.1)."

Corollary 1.2 (Section 1, p. 3), verbatim:

> "Corollary 1.2. There is an absolute constant C such that there are
> infinitely many n satisfying \tau(n + k) << k^C for all integers k >= 2."

Context sentence (p. 3): "As a corollary of Theorem 1.1, we have a weaker
version of Conjecture 3 (Erdos Problem #826)."

Theorem 1.3 (Section 1, p. 3), verbatim:

> "Theorem 1.3. There exists a positive constant C such that, for infinitely
> many positive integers n, one has \omega(n - k) <= \Omega(n - k) <= C log k
> for every integer 1 < k < n."

Preceded by (p. 3): "With the same proof, a version of Theorem 1.1 for n - k
also holds."

Corollary 1.4 (Section 1, p. 3), verbatim:

> "Corollary 1.4. There are infinitely many n such that
> \omega(n - k) <= k
> for all integers 1 << k < n."

Preceded by (p. 3): "Using Theorem 1.3, we immediately obtain a corollary,
which is a weaker version of Conjecture 2 (Erdos Problem #413)."

Limitation remark (Section 1, p. 3), verbatim:

> "Theorem 1.3 misses the first part of Conjecture 4 (Erdos Problem #679) by
> a log log k factor, and misses the last part by a constant. Moreover,
> Conjecture 6 disproves the first claim in Conjecture 4 (Erdos Problem
> #679)."

---

## 2. WHAT IMPROVES FROM O(k) TO O(log k), AND WHERE

The quantity that improves is the uniform-in-k upper bound on
\omega(n + k) (and \Omega(n + k)) for the infinitely many good n:
Tao-Teravainen (2025, their Theorem 1.1, = Conjecture 1 here, Erdos #248)
achieve \omega(n+k) <= \Omega(n+k) << k; Lau's Theorem 1.1 (Section 1, p. 2)
achieves <= C log k. Stated in: Abstract (p. 1, quoted above) and the
sentence before Theorem 1.1 (p. 2, quoted above).

Mechanism, as stated in Section 2 (Outline, pp. 3-4):

(a) Random n on [x,2x] weighted by a product of independent Selberg-type
sieves (Section 2, p. 3, verbatim): "we choose n in [x, 2x] with probability
proportional to
  w(n) := 1_{p|n \forall p <= 0.15 log x} \prod_{k=1}^{K} w_{R_k}(n + k)^2,
where w_{R_k}(n + k) are sieve weights of Goldston-Pintz-Yildirim type and
K = (log x)^{1/1000}."

(b) Polynomially decaying sieve levels (Section 2, p. 4, verbatim): "we
choose a polynomial decay for the sieve levels:
  R_k = x^{c/k^{50}}
for a small constant c > 0. This choice of polynomial decay is a
quantitative refinement of Tao and Teravainen (2025) and is essential for
the sharp bounds required in Theorem 1.1."

(c) Typical count heuristic (Section 2, p. 4, verbatim): "we exploit the
fact that a typical integer with no prime factors below R_k has roughly
  log( log x / log R_k ) approx log(k^{50}/c) \asymp log k
prime factors. To ensure that all n + k simultaneously exhibit this typical
behavior, we prove a strong concentration of measure result. Specifically,
we show that the number of prime factors \omega(n + k) satisfies a central
limit theorem-type bound under the sieve weights, with mean and variance
proportional to log(log x / log R_k)."

(d) THE decisive quantitative step, eq. (2.2) (Section 2, p. 4, verbatim):

> "From this concentration, we deduce that the probability of the tail event
> is small:
> (2.2)  P(\omega(n + k) >= C log k) << e^{-c' C log k} = 1/k^{c' C}.
> To establish (2.2), we derived an upper bound for the exponential moment.
> By contrast, Tao and Teravainen (2025) obtained a comparable bound for
> P(\omega(n + k) >= C k) using second-moment estimates. This perspective
> plays an important role in enabling our quantitative refinement. By
> choosing C sufficiently large, we ensure this probability is less than
> 1/(100 k^2), allowing the sum in (2.1) to converge and remain less than 1."

where (2.1) (Section 2, p. 3) is: \sum_{k=2}^{\infty}
P(\omega(n + k) >= C log k) < 1 for a sufficiently large constant C.
(p. 3: terms with k >= x^{1/100} "are handled by trivial bounds"; "The main
challenge lies in the range k < x^{1/100}.")

So: the improvement is carried by replacing second-moment tail bounds
(giving P(\omega(n+k) >= Ck) small) with high/exponential-moment
concentration (Lemma 5.3 moments of order s_i up to A log k, then Chebyshev
with s ~ log k), stated in Section 2 around (2.2) and implemented in
Sections 5-6.

---

## 3. THE CONJECTURE LADDER (Conjectures 1-6, verbatim)

All from Section 1, pp. 2-3. Identification sentence (p. 2, verbatim):
"These are listed as Erdos Problem #248, #413, #826 and #679 respectively on
the website erdosproblems maintained by Thomas Bloom cataloguing problems
posed by Erdos." [i.e. Conjecture 1 = #248, Conjecture 2 = #413,
Conjecture 3 = #826, Conjecture 4 = #679; the paper introduces them "in
increasing order of difficulty".]

> "Conjecture 1 (Erdos (1974), Tao and Teravainen (2025)). There are
> infinitely many n such that
>   \omega(n + k) <= \Omega(n + k) << k
> for all integers k >= 1."

> "Conjecture 2 (Erdos (1979)). There are infinitely many n such that
>   \omega(n - k) <= k
> for all integers 1 <= k < n."

> "Conjecture 3 (Erdos (1974)). There are infinitely many n such that
> \tau(n + k) << k for all integers k >= 1."

> "Conjecture 4 (Erdos (1979)). For epsilon > 0, there are infinitely many n
> such that
>   \omega(n - k) <= (1 + epsilon) log k / log log k
> for all integers 1 <<_epsilon k < n. Moreover, there are infinitely many n
> such that
>   \Omega(n - k) <= (1 + epsilon) log k / log 2
> for all integers 1 <<_epsilon k < n."

[Conjecture 4 IS the paper's rendering of Erdos Problem #679; Section 7's
title is "Conditional Falsity of Erdos Problem #679".]

Sharpness conjectures (from random models; p. 2: "Using random models, we
conjecture this is best possible up to a constant."):

> "Conjecture 5. Theorem 1.1 is best possible up to a constant, that is, for
> any epsilon > 0 and n sufficiently large in terms of epsilon, there exists
> integers k_1, k_2 >= 2 such that \omega(n + k_1) > (1 - epsilon) log k_1
> and \Omega(n + k_2) > (1 - epsilon) log k_2 / log 2."

> "Conjecture 6. Theorem 1.3 is best possible up to a constant, that is, for
> any epsilon > 0 and n sufficiently large in terms of epsilon, there exists
> integers 1 < k_1, k_2 < n such that \omega(n - k_1) > (1 - epsilon) log k_1
> and \Omega(n - k_2) > (1 - epsilon) log k_2 / log 2."

(p. 3, before Conjecture 6: "We also speculate that the analogous version of
Conjecture 5 holds.")

---

## 4. PROOF INTERFACE (Sections 5-6): the reduction chain

Chain: Theorem 1.1 <= Proposition 5.1 <= Proposition 5.2 <= Lemma 5.3
(via Chebyshev on high moments, using Lemma 5.4) <= Proposition 5.5
(<= Lemmas 6.1-6.5). Closing sentence (Section 6.5 end, p. 34, verbatim):
"Together with Lemmas 6.1, 6.2, 6.3, and 6.4, we proved Proposition 5.5, and
thus Theorem 1.1 as well."

Proposition 5.1 (Section 5, p. 5), verbatim:

> "Proposition 5.1. For any sufficiently large constant C and sufficiently
> large x in terms of C, we may construct a random variable n taking values
> in [x, 2x] such that for every integer 2 <= k <= x^{1/100},
> (5.1)  P(\Omega(n + k) > C log k) < 6/(pi^2 k^2)."

[Proof of Theorem 1.1 from Prop 5.1 (p. 5): union bound over
2 <= k <= x^{1/100}; for x^{1/100} < k <= 2x trivially \Omega(n+k) <=
log(n+k)/log 2 <= (300/log 2) log k, and for k > 2x <= (2/log 2) log k;
choose C = max{C_0, 300/log 2}.]

Proposition 5.2 (Section 5, pp. 5-6), verbatim:

> "Proposition 5.2. Let C_2 >= 4. Then, for C_1 sufficiently large
> (depending on C_2), there exists a constant A = A(C_2) > 0 such that the
> following holds.
> For all sufficiently large x in R^+ (in terms of A), and for all integers
> 2 <= k <= x^{1/100}, define the parameters
>   w := 0.15 log x,  T := x^{1/10A log k},
> and
>   R_k := { x^{1/100k^{50}}, if k <= (log x)^{1/1000},
>          { w,               if (log x)^{1/1000} < k <= x^{1/100}.
> Then one can construct a random variable n taking values in the interval
> [x, 2x] such that, with probability 1, the integer n is divisible by p^4
> for every prime p <= w. Moreover, the following additional properties hold:
> (5.2)  P(\omega_{w < . <= R_k}(n + k) >= C_1 log k) << 1/(C_2^2 k^2),
> (5.3)  P( \sum_{R_k < p <= T} (1_{p|n+k} - 1/p) >= C_1 log k )
>          << 1/(C_2^2 k^2),
> (5.4)  P( \sum_{j>=2} \sum_{w < p <= T} 1_{p^j|n+k} >= C_1 log k )
>          << 1/(C_2^2 k^2),
> (5.5)  P( \sum_{p <= w, p^4 | k} (\nu_p(n + k) - \nu_p(k))_+ >= C_1 log k )
>          <= 3/(2 pi^2 k^2).
> Here the implied constants are absolute constants and do not depend on A,
> C_1, or C_2."

[Proof of 5.1 from 5.2 (pp. 6-7): decompose \Omega(n+k) into the four
sums plus <= 11 A log k primes p > T plus \Omega(k) <= 2 log k terms;
Mertens gives \sum_{R_k<p<=T} 1/p << log(log T/log R_k) <= 54 log k for
k <= (log x)^{1/1000} resp. < 1000 log k above (eq. (5.6), p. 7); choose
C := 12A + 4C_1 + 1002 and pigeonhole.]

Lemma 5.3 (Section 5, p. 8), verbatim (the high-moment interface; note the
reduction sentence p. 8: "Using Chebyshev's inequality ... we will reduce
Proposition 5.2 to upper bounds on high moments."):

> "Lemma 5.3. Suppose A > 1, 2 <= k <= x^{1/100} and log k <= s_1, s_2, s_3
> <= A log k are integers. Then for any x in R^+ sufficiently large in terms
> of A and epsilon, define the parameters
>   w := 0.15 log x,  T := x^{1/10A log k},
> and
>   R_k := { x^{1/100k^{50}}, if k <= (log x)^{1/1000},
>          { w,               if (log x)^{1/1000} < k <= x^{1/100}.
> Then one can construct a random variable n taking values in the interval
> [x, 2x] such that, with probability 1, the integer n is divisible by p^4
> for every prime p <= w. Moreover, the following additional properties hold
> for some constant C_3 >= 3:
> (5.7)  E | \sum_{w < p <= R_k} 1_{p|n+k} |^{s_1} << (2 C_3 s_1)^{s_1},
> (5.8)  E | \sum_{R_k < p <= T} (1_{p|n+k} - 1/p) |^{2 s_2}
>          << (132 A log k)^{2 s_2},
> (5.9)  E | \sum_{j>=2} \sum_{w < p <= T} 1_{p^j|n+k} |^{s_3}
>          << ( max{ 4 e^2 C_3, 968 (A log k / s_3)^2 } s_3 )^{s_3},
> (5.10) P(\nu_p(n + k) - \nu_p(k) >= h_p \forall p in P)
>          <= 2 ( \prod_{p in P} p^{-h_p} + x^{-0.3} ),
> for any P subseteq {p <= w : p^4 | k}, and h_p in Z^+ for p in P. Here the
> implied constants are absolute and independent of A."

[These s-th moments with s_i up to A log k are exactly the "exponential
moment" bounds behind (2.2). In the proof of Prop 5.2 (p. 9) the paper sets
A = sqrt(2 log(C_2 e^2 C_3)/ log 2) > 1 (transcribed from mangled text
layer [TRANSCRIPTION-UNSURE] on the exact expression).]

Lemma 5.4 (Stirling numbers of the second kind) (Section 5, p. 8), verbatim:

> "Lemma 5.4 (Stirling numbers of the second kind). For integers s >= 1 and
> 1 <= t <= s, the Stirling number of the second kind {s \atop t} is the
> number of ways to partition a set of s labelled objects into t nonempty
> unlabelled boxes. It satisfies the bound
>   {s \atop t} << (s / log s)^s
> for all sufficiently large s and 1 <= t <= s, and the relation
>   \sum_{j=1}^{2s} {2s \atop j} m!/(m - j)! = m^{2s}
> for all integers m >= 2s."
> [Proof cites Rennie and Dobson (1969) and Graham (1994).]

Proposition 5.5 (Section 5, p. 11), verbatim (the core sieve interface):

> "Proposition 5.5. For A > 1, 3 <= s_1, s_2, s_3 <= A log k integers, x in
> R^+ a positive real sufficiently large in terms of A and epsilon, and
> 2 <= k <= x^{1/100} a positive integer, define the parameters
>   w := 0.15 log x,  T := x^{1/10A log k},  K := (log x)^{1/1000},
>   K_+ := x^{1/100},
> and
>   R_k := { x^{1/100k^{50}}, if k <= K,
>          { w,               if K < k <= K_+.
> Then we may construct a random variable n taking values in [x, 2x]
> satisfying the following properties:
> (A) With probability 1, n is divisible by p^4 for any prime p <= w.
> (B) If 1 <= k <= K_+, 1 <= j <= s_2, and R_k < p_1, ..., p_j <= T are
>     distinct primes, then
>       P(p_1 ... p_j | n + k) << 8^{s_2} / (p_1 ... p_j).
> (C) If 1 <= k <= K and 1 <= j <= s_1, then there is a constant C_3 >= 3
>     such that
>       \sum_{w < p_1,...,p_j <= R_k, p_i mutually distinct}
>         P(p_1 ... p_j | n + k) << (C_3 log s_1)^{s_1}.
> (D) If 1 <= k <= K_+, 1 <= j <= s_3, a_1, ..., a_j >= 2, and
>     w < p_1, ..., p_j <= T are distinct primes, then
>       P(p_1^{a_1} ... p_j^{a_j} | n + k)
>         = P(p_1 ... p_j | n + k) / (p_1^{a_1 - 1} ... p_j^{a_j - 1})
>           + O(x^{-0.1}).
> (E) If 1 <= k <= K_+, P subseteq {p <= w : p^4 | k}, and h_p in Z^+ for
>     p in P, then
>       P(\nu_p(n + k) - \nu_p(k) >= h_p \forall p in P)
>         <= 2 ( \prod_{p in P} p^{-h_p} + x^{-0.3} ).
> Here all implied constants are absolute and independent of A."

Section 6 lemma skeleton (roles; setups sighted on pp. 21, 26, 29, 32, 34;
statements partly run past those pages, so conclusions below are PARAPHRASE,
not verbatim, except where quoted):

- Definition of the weight (Section 6.1, p. 21, verbatim): "\nu(n) =
  1_{n in [x,2x]} 1_{W|n} \prod_{k=1}^{K} ( \sum_{(d,P(w))=1, d|n+k}
  \mu(d) eta~(log d / log R_k) )^2" with W = \prod_{p <= w} p^4; n is drawn
  from [x,2x] with density \nu(n)/\sum_{n'} \nu(n') (p. 21: "In particular,
  Proposition 5.5(A) holds."). P_{k*}(d_*) := \sum_n \nu(n) 1_{d_*|n+k*},
  P_{k*}(1) := \sum_n \nu(n).
- Lemma 6.1 (Section 6.2, p. 21): master asymptotic evaluation, eq. (6.2):
  P_{k*}(d_*) written as an explicit main term (a 2K-fold integral over
  t_k, t'_k with |t_k|,|t'_k| <= (log x)^{0.2}, factors (W/phi(W))^K,
  \prod_k (1+it_k)(1+it'_k)/((2+i(t_k+t'_k)) log R_k), local factors
  E_{k*,d_*,p}(t,t') for p | d_*) plus error O( (4^s x/(W d_*))
  exp(-c' log^{0.1} x) ). Local factors: E_{k*,d_*,p} = (1/p)(1 -
  p^{-(1+it_{k*,p})/log R_{k*,p}})(1 - p^{-(1+it'_{k*,p})/log R_{k*,p}}) if
  p | d_* and exists 1 <= k <= K with p | k_* - k; and E = 1/p if p | d_*
  and p does not divide k_* - k for all 1 <= k <= K. (Transcribed from
  p. 21; formula dense - see flag.)
- Lemma 6.2 (Section 6.3, p. 26) proves Proposition 5.5(B): divisor
  probability bound P(d_* | n + k_*) << 8^s/d_* via P_{k*}(d_*)/P_{k*}(1)
  (conclusion visible p. 29 top: "P(d_* | n + k_*) = P_{k*}(d_*)/P_{k*}(1)
  << 8^s/d_*, as required."; also "P_{k*}(1) = (1+o(1))
  x/(W \prod_{k=1}^K log R_k) (c_0 W/phi(W))^K" on p. 29).
- Lemma 6.3 (Section 6.4, p. 29) proves Proposition 5.5(C): the
  zeta-factor / Dirichlet-series computation giving
  (C_3 log s_1)^{s_1}-type bounds; ends (p. 32): "Thus, we are done with
  the choice C_3 = 32 log(4/c) and in particular C_3 >= 3."
- Lemma 6.4 (Section 6.5, p. 32) proves Proposition 5.5(D): prime-power
  divisor probabilities; proof ends p. 34 via Chinese Remainder Theorem
  computation, error << R_1^2 ... R_K^2 O(1)^K << x^{0.25}, "acceptable
  since W << x^{0.6} and x^{0.25} << x^{0.85}/W".
- Lemma 6.5 (Section 6.6, p. 34) proves Proposition 5.5(E), verbatim
  conclusion: "P(\nu_p(n + k_*) - \nu_p(k_*) >= h_p \forall p in P) <=
  2( \prod_{p in P} p^{-h_p} + x^{-0.3} )." Proof (p. 35) is a direct
  divisor-sum computation with q = W lcm([d_1,d'_1],...,[d_K,d'_K]) and
  q' = q \prod_{p in P} p^{e_p + h_p - 4}, using q <= x^{0.7} and
  e_p = \nu_p(k_*) >= 4.

---

## 5. SECTION 7 ANATOMY: "Conditional Falsity of Erdos Problem #679"

Section title (Section 7, p. 35): "7. Conditional Falsity of Erdos Problem
#679". The problem itself, as given by the paper, is Conjecture 4
(Section 1, p. 2; verbatim in Part 3 above), labeled "(Erdos Problem #679)"
at p. 3 and implicitly throughout Section 7 via "Conjecture 4".

Step 0 - Cramer model setup (Section 7, p. 35 bottom - p. 36 top), verbatim:

> "A famous conjecture of Cramer (1936) states that if p_n denotes the n-th
> prime number, then
>   p_{n+1} - p_n << (log p_n)^2."
> "This conjecture comes from modelling primes with independent Bernoulli
> random variables (X_n)_{n>=3} with P(X_n = 1) = 1/log n and the following
> lemma."

Step 1 - Borel-Cantelli lemma for Bernoulli models (Lemma 7.1, Section 7,
p. 36), verbatim:

> "Lemma 7.1. Let f : R^+ -> R be a smooth function such that f(n) -> infty
> as n -> infty and f^{(j)} <<_j x^{-j} for all j >= 1. Let (X_n)_{n>=1} be
> a sequence of independent Bernoulli random variables with P(X_n = 1) =
> 1/f(n). Let S_1 < S_2 < ... be indices such that X_{S_k} = 1 for all
> k >> 1. Then, with probability 1
>   limsup_{k -> infty} (S_{k+1} - S_k) / (f(S_k) log S_k) <= 1."
> "Proof. This follows from the Borel-Cantelli lemma."

[Note: the mixing of variable names n and x in "f^{(j)} <<_j x^{-j}" is as
printed in the paper. The proof is given only by the one-line citation of
Borel-Cantelli; no further detail appears.]

Step 2 - unconditional density input (Theorem 7.2, Section 7, p. 36).
Setup sentence, verbatim: "For k in N, let pi_k(x) to denote the number of
integers not greater than x with exactly k distinct prime factors. We quote
the following result in Tenenbaum (2015, Chapter II.6)."

> "Theorem 7.2. Let A > 0. Uniformly for x >= 3 and 1 <= k <= A log_2 x, we
> have
>   pi_k(x) >>_A (x / log x) (log_2 x)^{k-1} / (k-1)!."

Step 3 - density corollary + motivation (Section 7, p. 36), verbatim:

> "By putting k = ceil(log_2 x) into Theorem 7.2 and using Stirling's
> approximation, we see that
>   pi_k(x) >> x / sqrt(log_2 x).
> Therefore, using Lemma 7.1 we are motivated to conjecture the following."

[The k in "k = ceil(log_2 x)" is rendered with ceiling brackets in the
paper.]

Step 4 - Conjecture 7 (Section 7, p. 36), verbatim:

> "Conjecture 7. For epsilon > 0, let A := {n : \omega(n) >= epsilon
> log_2 n} and B := {n : \Omega(n) >= epsilon log_2 n}. Then there is a
> constant C such that for x in R^+ sufficiently large, we have
>   A cap ( x - C log x sqrt(log_2 x), x ],
>   B cap ( x - C log x sqrt(log_2 x), x ]  != emptyset."

[I.e. both intersections are nonempty: every window of length
C log x sqrt(log_2 x) ending at x contains an element of A and one of B.
The window length matches Lemma 7.1 with f(S) ~ reciprocal density
~ log S sqrt(log_2 S) coming from pi_k(x) >> x/sqrt(log_2 x); the paper
does not spell this calibration out beyond the motivation sentence.]

Step 5 - bridge + Conjecture 8 (Section 7, p. 36), verbatim:

> "In fact, a weaker version of Conjecture 7 suffices to disprove
> Conjecture 4."

> "Conjecture 8. Let A := {n : \omega(n) >= C_0 log_2 n / log_3 n}. Then
> for some C_0 >= 1, there is a constant 1 <= d < C_0 such that for x in
> R^+ sufficiently large, we have
>   A cap ( x - (log(x/2))^d, x ] != emptyset."

Step 6 - the conditional refutation computation (Section 7, p. 36),
verbatim:

> "We see that Conjecture 8 immediately implies the falsity of Conjecture 4.
> Indeed, for every n in R^+ sufficiently large, by Conjecture 8 there
> exists constants C_0, d with 1 <= d < C_0 such that
>   \omega(n - k) >= C_0 log_2(n - k) / log_3(n - k)
> for some 1 <= k <= (log(n/2))^d. Note
>   C_0 log_2(n - k)/log_3(n - k)
>     >= C_0 log_2(n/2)/log_3(n/2)
>     >= C_0 log(k^{1/d})/log_2(k^{1/d})
>     >= C_0 log k / ( d (log log k - log d) )
>     >= ( 1 + (C_0/d - 1) ) log k / log log k,
> with C_0/d - 1 > 0. Therefore, we disproved Conjecture 4."

[Structure of the step: Conjecture 8 places an element of A =
{\omega(n) >= C_0 log_2 n / log_3 n} in the window (n - (log(n/2))^d, n];
writing it as n - k with 1 <= k <= (log(n/2))^d, monotonicity converts the
threshold C_0 log_2(n-k)/log_3(n-k) into (1 + delta) log k/ log log k with
delta = C_0/d - 1 > 0, contradicting the first display of Conjecture 4 for
epsilon < delta. The window-hitting hypothesis is used for EVERY large n,
so no exceptional n survives - this kills the "there are infinitely many n"
form of Conjecture 4.]

Step 7 - packaged statement (Theorem 7.3, Section 7, p. 36), verbatim:

> "Theorem 7.3. Assume Conjecture 8. Then, there exists delta > 0 such that
> for every sufficiently large n in N, there exists 1 << k < n such that
> \omega(n - k) > (1 + delta) log k / log log k."

Step 8 - closing remark (Section 7, p. 37), verbatim:

> "Using an analogous argument, Conjecture 7 proves Conjecture 6."

[This is the entire content of Section 7 apart from the references. Note
the Borel-Cantelli input (Lemma 7.1) is used ONLY to motivate Conjectures
7/8 (it justifies the Cramer-type window length in the random model); the
deduction Conjecture 8 => Theorem 7.3 is elementary and unconditional given
the conjecture. Theorem 7.2 (Tenenbaum) is the unconditional density fact
making the conjectured window lengths plausible.]

References cited in Section 7 (p. 37): Cramer (1936) [1]; Tenenbaum (2015)
[8]; also in the bibliography: Erdos (1974) [2], Erdos (1979) [3], Graham
(1994) [4], Maynard (2015) "Small gaps between primes" [5], Rennie-Dobson
(1969) [6], Tao-Teravainen (2025) arXiv:2512.01739 [7].

---

## 6. SEARCH FOR ERDOS #251-TYPE MATERIAL (task 4)

Searched the full pdftotext dump (5391 lines, all 37 pages) for:
"irrational", "2^n" (and the mangled "2n" power forms), "binary", "digit",
"numerator", "series", "#251", "251", "p_n"/"pn", "prime gap", "gaps
between", "consecutive prime", "prime number", "Cram", and all "#" problem
numbers.

Result: NO mention anywhere of growing numerators, prime-index series,
sum p_n/2^n, irrationality, binary/base-2 digits of a series, or Erdos
problem #251. The Erdos problem numbers appearing in the paper are exactly
#248, #413, #826, #679 (p. 2, p. 3, Section 7 title).

The only occurrences of the n-th prime p_n and of prime gaps are:
1. Section 7, p. 35 (quoted in full above): the Cramer conjecture
   "p_{n+1} - p_n << (log p_n)^2" and the Bernoulli model sentence.
2. Bibliography items [1] Cramer (1936) "On the order of magnitude of the
   difference between consecutive prime numbers" and [5] Maynard (2015)
   "Small gaps between primes" (p. 37). Maynard's paper is not discussed in
   any prose I located; it appears only as a bibliography entry.
   [TRANSCRIPTION-UNSURE: I did not find a citation of [5] in the body via
   the text layer; a visually hidden citation cannot be fully excluded.]

Conclusion: the paper contains no remark bearing directly on Erdos #251 /
sum p_n/2^n targets. Its only bridge toward prime-gap statements is the
Section 7 Cramer-model schema.

---

## 7. TRANSFER-RELEVANT OBSERVATIONS (extractor commentary)

This section is COMMENTARY, not extraction.

1. Section 7's schema is: (i) an unconditional density theorem for a target
   set A (Theorem 7.2); (ii) a Cramer-type window conjecture calibrated by
   the Bernoulli model via Borel-Cantelli (Lemma 7.1): A meets every
   interval (x - H(x), x]; (iii) an elementary deduction that for EVERY
   large n some n - k with k <= H(n) lies in A, refuting a "for all k"
   smallness statement. Only step (ii) is conjectural.

2. The schema transfers formally to prime-gap windows: taking A = primes
   (density 1/log x [BACKGROUND-UNVERIFIED, standard PNT]) and f(n) = log n
   in Lemma 7.1 is literally the Cramer setup the paper opens Section 7
   with, giving model-a.s. limsup (p_{k+1}-p_k)/(log p_k log p_k) <= 1.
   A window conjecture "every (x - C(log x)^2, x] contains a prime" yields,
   unconditionally given the conjecture, g_n << (log p_n)^2 for ALL n,
   hence a uniform conditional bound delta_n = \sum_j g_{n+j} 2^{-j} <<
   (log p_{2n})^2 (crude domination) [BACKGROUND-UNVERIFIED arithmetic, not
   from the paper]. So Lau-Section-7-style reasoning CAN produce
   conditional statements about the delta_n tail - but only one-sided
   size/upper-bound control of windows of gaps.

3. What it does NOT give: the schema controls occurrence of A-elements in
   windows, i.e. largeness/smallness thresholds; it says nothing about the
   distribution of delta_n mod 1, digit patterns, or eventual periodicity -
   the quantities an irrationality argument for S = sum p_n/2^n needs. The
   paper's own use is purely negative (refute Conjecture 4) or sharpness
   (Conjecture 7 => Conjecture 6).

4. Lemma 7.1's proof-by-Borel-Cantelli operates entirely inside the random
   model; an analogous model statement "delta_n is a.s. equidistributed
   mod 1 in the Cramer model" would be a Section-7-style motivation for a
   #251 window conjecture, but nothing of the sort appears in the paper.

5. The O(k) -> O(log k) machinery (Sections 5-6) concerns sieve-weighted
   random n and concentration for \omega(n + k); its interface (Prop 5.5)
   is about divisor probabilities P(d | n + k), not about primes in short
   intervals, and offers no direct handle on g_n or delta_n.

---

## FLAGS (consolidated)

1. [PRINTED-ODDITY] Lemma 7.1 hypothesis mixes variables as printed:
   "f(n) -> infty as n -> infty and f^{(j)} <<_j x^{-j}". Transcribed
   verbatim; the x/n mismatch is in the paper.
2. [TRANSCRIPTION-UNSURE, resolved-by-context] Conjecture 8 window read as
   (log(x/2))^d, i.e. the fraction x/2 sits inside the log (stacked
   fraction in the PDF). Confirmed by the subsequent deduction, which uses
   k <= (log(n/2))^d and log_2(n/2); a reading ((log x)/2)^d is visually
   close but inconsistent with the argument.
3. [PRINTED-ODDITY] Lemma 5.3 and Proposition 5.5 preambles say
   "sufficiently large in terms of A and epsilon" although no epsilon
   occurs in either statement. Transcribed verbatim.
4. [PARAPHRASE] Lemmas 6.1-6.4 statements/conclusions partly run past the
   pages read visually (21, 26, 29, 32); their roles and conclusions are
   summarized, with only the sighted fragments quoted. Lemma 6.5's
   conclusion was sighted and is quoted.
5. [TRANSCRIPTION-UNSURE] The constant A = sqrt(2 log(C_2 e^2 C_3)/log 2)
   in the proof of Prop 5.2 (p. 9) was transcribed from the mangled text
   layer, not verified visually.
6. [TRANSCRIPTION-UNSURE] (5.9) inner summation range w < p <= T: small
   glyphs; cross-checked against the text layer (which reads "w < p <= T")
   and against (5.4); residual risk minimal.
7. [TRANSCRIPTION-UNSURE] In the Step 6 inequality chain the third
   denominator "d (log log k - log d)" is transcribed from the rendered
   page; the "- log d" term is legible but small.
8. [TRANSCRIPTION-UNSURE] Absence of a body citation of Maynard (2015) [5]
   was checked via the text layer only.
9. [BACKGROUND-UNVERIFIED] In the commentary section: PNT density of
   primes, and the crude domination delta_n << (log p_{2n})^2 under a
   Cramer window conjecture, are extractor background, not paper content.
10. Note: Lemma 6.1's formula (6.2) and local factors E_{k*,d*,p} are
    transcribed from a dense display (p. 21); exponents of the form
    p^{-(1+it_{k*,p})/log R_{k*,p}} carry minor transcription risk
    [TRANSCRIPTION-UNSURE].
