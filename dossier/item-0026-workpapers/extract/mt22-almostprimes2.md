# EXTRACTION: Kaisa Matomaki and Joni Teravainen, "Almost primes in almost all short intervals II"

Source (only evidence base): /home/istr/pro/erdos251/dossier/2207.05038v2.pdf
sha256 93aa865f7699da179305dbf14935016b4e092d75a5d7cb1ecac651c59067380d (operator-verified; re-verified this session).
arXiv:2207.05038v2 [math.NT] 1 Feb 2023. 26 pages (A4). Creator: LaTeX
with hyperref; producer pdfTeX-1.40.21; PDF built 2 Feb 2023.
Authors: Kaisa Matomaki and Joni Teravainen (front matter, p. 1;
transliterated -- printed "Matomaki", "Teravainen" carry an a-diaeresis).
Affiliation (p. 26, address block): both "Department of Mathematics and
Statistics, University of Turku, 20014 Turku, Finland." Email addresses:
ksmato@utu.fi and joni.p.teravainen@gmail.com.
2020 Mathematics Subject Classification (footnote p. 1): 11N05, 11N36.
No printed journal reference on the paper (arXiv preprint).
Grant footnote (Subsection 1.2, p. 3, "Acknowledgments"): "KM was
supported by Academy of Finland grant no. 285894. JT was supported by
Academy of Finland grant no. 340098. We thank the referee for numerous
helpful suggestions."

Steering identification CONFIRMED against front matter: authors and title
match "Matomaki--Teravainen, Almost primes in almost all short intervals
II". No deviation.

---

## Transcription conventions

ASCII only. Diacritics transliterated: Matomaki, Teravainen, Deshouillers,
Iwaniec, Lindelof, Halasz, Jutila, Motohashi, Wolke, Vinogradov, Korobov,
Buchstab, Selberg, Radziwill, Renyi. Mathematics is rendered LaTeX-like in
ASCII. Anchors are the paper's own numbering (Theorem/Lemma/Proposition,
equation numbers (1.1)-(7.1), Section/Subsection numbers 1-7); page numbers
(printed = PDF page throughout, 1-26) are a secondary aid. Every quoted
passage is a verbatim blockquote with its page number.

Symbol table (every non-obvious glyph):

- E_2, E_3    numbers with exactly two, exactly three prime factors.
- P_2         numbers with AT MOST two prime factors ("almost primes").
- E_k         numbers with exactly k prime factors.
- p, q, p_j, q_j   always denote primes (Notation, p. 4).
- n ~ y       shorthand for y < n <= 2y (Notation, p. 4).
- <<, >>      Vinogradov asymptotic notation (paper prints the curly
              << / >>). "A << B" means A = O(B). Subscripts as printed:
              <<_A, <<_eps, <<_eta record the dependence of the implied
              constant.
- ~ (over =)  asymptotic equivalence (limit of ratio = 1); "x(log x)^..."
              under a sqrt sign is written sqrt(x)(log x)^... .
- rho^-(n)    the minorant function (2.3), rho^-(n) <= 1_P(n).
- 1_P(n)      indicator that n is prime (1_{n in P}).
- 1_A         indicator of the claim/set A.
- P(z)        = prod_{p<z} p (Notation, p. 4).
- rho(n,z)    = 1_{(n,P(z))=1} (Notation, p. 4); n has no prime factor < z.
- mu          Mobius function; d_k the k-fold divisor function, d := d_2.
- Lambda(n)   von Mangoldt function (Section 6).
- omega(u)    Buchstab's function (defined p. 6): omega(u)=1/u for
              1<=u<=2, extended by d/du(u omega(u)) = omega(u-1) for u>=2.
- delta_A     = (log X)^{-10A}; delta_A-adic intervals (N,(1+delta_A)N].
- sigma, sigma_1, sigma_2   large-value exponents; |M(1+it)| ~ M^{-sigma}.
- theta       = (log M_1)/(log X) (5.11).
- N(sigma,T)  number of zeros of the Riemann zeta-function zeta in
              {b+it : b >= sigma, |t| <= T} (p. 1-2).
- calM        a script-M set of integers (Lemma 3.4); |calM| its cardinality.
- Uu, Tt, Ff, Cc   calligraphic sets/collections: Uu,Tt subsets of the
              t-line; Ff a set of O(exp((log log X)^5)) functions; the
              exceptional set is printed with a script X (rendered Xx here).
- a_n, alpha_m, beta_n, epsilon_m   Dirichlet-polynomial coefficients.
- k!          factorial (appears bounding coefficients of P_1(s)^k).
- eps         the paper's epsilon (small fixed parameter); eta a separate
              small parameter in Lemma 3.4.

Everything up to the COMMENTARY section is EXTRACTION (what the paper
says). Nothing evaluative appears before COMMENTARY. Method-anatomy prose
is marked "PARAPHRASE except quotes".

---

## 1. FRONT MATTER AND ABSTRACT

Title (p. 1): "ALMOST PRIMES IN ALMOST ALL SHORT INTERVALS II".
Authors (p. 1): "KAISA MATOMAKI AND JONI TERAVAINEN".

Abstract (p. 1), verbatim:

> "We show that, for almost all x, the interval (x, x + (log x)2.1 ]
> contains products of exactly two primes. This improves on a work of
> the second author that had 3.51 in place of 2.1. To obtain this
> improvement, we prove a new type II estimate. One of the new
> innovations is to use Heath-Brown's mean value theorem for sparse
> Dirichlet polynomials."

---

## 2. SECTION 1 (Introduction): problem, main theorems

Opening (Section 1, p. 1), verbatim:

> "We shall study the distribution of E2 numbers, i.e. numbers with
> exactly two prime factors, in almost all short intervals. This problem
> has been studied in previous works of Heath-Brown [6], Motohashi [16],
> Wolke [20], Harman [4], and the second author [18]."

The "almost all" definition (p. 1), verbatim:

> "The best known result [18, Theorem 3] gives that, for almost all x,
> the interval (x, x + (log x)3.51 ] contains E2 numbers (here, and in
> the rest of the paper, we say that a property P (x) holds for almost
> all x if the measure of x in [1, X] for which P (x) fails is o(X) as
> X -> infinity). In this paper, we strengthen this result by replacing
> the exponent 3.51 by 2.1. In the theorem and later, pj always denotes
> a prime."

### 2.1 Theorem 1.1 (main result), verbatim (p. 1)

> "Theorem 1.1. There exist constants c0 > 0 and delta > 0 such that the
> following holds. Let X >= 3. Then, for all but << X/(log X)^delta
> integers x in [2, X], we have
>   |{p1 p2 in (x, x + (log x)2.1 ] : (log x)1.09 < p1 <= (log x)1.1 }|
>        >= c0 (log x)1.1 ."

[Display confirmed from the rendered page image (p. 1) as well as the text
layer; the "<<" in "all but << X/(log X)^delta" was a gap in the text
layer, resolved by image. Flag 1.]

Correct-order remark (p. 1), verbatim:

> "One can show that the lower bound in Theorem 1.1 is of the correct
> order of magnitude, although it is only for those E2 numbers that have
> a prime factor in a certain superdyadic interval."

Barrier discussion (p. 1-2): the paper records that the limit of the
approaches of [4, 18] was exponent 3 + eps, reachable in [4] only under a
slight strengthening of the density hypothesis (1.1) N(sigma,T) <<
T^{(2-delta)(1-sigma)+o(1)}; and that Selberg [17] gives, under the Riemann
hypothesis, primes in almost all (x, x+(log x)^{2+eps}], hence E2 numbers
too (p. 2), verbatim:

> "Theorem 1.1 gets somewhat close to the exponent of 2 + eps, which
> seems to be the barrier for E2 numbers even under the Riemann
> hypothesis. In fact, as discussed in Section 6, in order to obtain
> 2 + eps for E2 numbers, it suffices to assume the Lindelof hypothesis
> which of course is a weaker assumption than the Riemann hypothesis."

Comparison to P_2 and E_3 (p. 2), verbatim:

> "In addition to E2 numbers, also P2 numbers that have at most two prime
> factors are called almost primes. The question of short interval
> distribution for these is significantly easier since classical sieve
> methods are applicable. Indeed, the first author [13] has recently
> shown that, for almost all x, the interval (x, x + h(x) log x] contains
> P2 numbers, provided only that h(x) -> infinity as x -> infinity."

> "For E3 numbers, i.e. numbers with exactly three prime factors, much
> shorter intervals can be reached than for E2 numbers; the second author
> showed in [18] that, for almost all x, the interval
> (x, x + (log x)(log log x)6+eps ] contains E3 -numbers. On the other
> hand, for the primes, the best known result due to Jia [11] gives that,
> for almost all x, the interval (x, x + x1/20 ] contains primes. Hence
> we understand the short interval distribution of Ek numbers for k >= 2
> significantly better than that of the primes."

### 2.2 Theorem 1.2 (E_3 in ALL intervals), verbatim (p. 2)

> "Theorem 1.2. For all large enough x, the interval
> (x, x + sqrt(x)(log x)1.55 ] contains E3 numbers."

Context (p. 2), verbatim:

> "As far as we are aware, Theorem 1.2 is the first result on E3 numbers
> in all intervals of length sqrt(x)(log x)c . It would be possible to
> similarly adapt also earlier works on E2 numbers in almost all short
> intervals, such as [18] or [4], to produce a result of this shape, but
> with a larger value of c."

(For E_2 in all intervals, the paper notes it is not aware of results
below x^{0.525} of Baker--Harman--Pintz [1], p. 2.)

### 2.3 Proof ideas (Subsection 1.1, PARAPHRASE except quotes; p. 2-3)

PARAPHRASE. Harman's sieve gives a minorant rho^-(n) <= 1_P(n); Perron's
formula reduces to mean squares of Dirichlet polynomials. The stated target
(p. 2, "for some eps > 0"), verbatim in structure:

> "integral_{X^{1/1000}}^{X/h} |P1 (1 + it)|2 |P (1 + it)|2 dt <<
> 1/(log X)2+eps , where h = (log X)2.1 , P1 (s) := sum_{p1 ~ P1} 1/p1^s,
> P (s) := sum_{X/(2P1) <= n <= 4X/P1} rho^-(n)/n^s , and
> P1 = (log X)1.1 (as well as other very similar claims)."

The range [X^{1/1000}, X/h] is split as T union U by the size of P_1(s):
T := {t : |P_1(1+it)| <= P_1^{-eps}} handled by a pointwise bound and an
improved mean value theorem (Lemma 3.3). Over U the minorant is split into
type I, type I/II, type II sums (Proposition 2.2). The type II integrals
have the form integral_U |P1|^2 |M1|^2 |M2|^2 dt with M1 in
[X^{eps/2}, X^{2/11}]; U is split into U_{sigma1,sigma2} by the sizes of
|M1|, |M2|. The novel step (p. 3):

> "When sigma_j <= 49/206 - 10eps for j = 1 or j = 2, we are able to use
> Jutila's [12] large value estimate to obtain a satisfactory bound (see
> Proposition 4.2). We deal with the case sigma_1, sigma_2 > 49/206 - 10eps
> in Section 5.3. There (utilizing an idea from [14]) we use the
> definitions of U_{sigma1,sigma2} and U to see that
>   |U_{sigma1,sigma2}| <= M2^{2 sigma2} P1^{2k eps} integral ... ,
> where we have chosen k so that P1^k = X^{1-o(1)}. Now the coefficients
> of P1(s)^k are supported on P1 = (log X)1.1 -smooth numbers, so they
> have a very sparse support (of size X^{1-1/1.1+o(1)} by standard
> estimates on smooth numbers). At this point, we invoke a mean value
> theorem for sparse Dirichlet polynomials proven recently by Heath-Brown
> [8] (see Lemma 3.4 below)."

---

## 3. SECTION 2 (The minorant function): the variance estimate

The minorant rho^-(n) is built from Buchstab's identity (1.2) with
z = X^{2/11}. The two discarded (nonnegative) terms give (p. 4-5):

Definition (2.3), verbatim (p. 5):

> "rho^-(n) := rho(n, z) - sum_{n=qm, z<=q<2X^{1/2}} rho(m, z)
>   + sum_{n=q1 q2 m, z<=q2<q1<X^{1/4-2eps}, q1 q2^4 < X^{1-2eps}} rho(m, z)
>   - sum_{n=q1 q2 q3 m, z<=q3<q2<q1<X^{1/4-2eps}, q1 q2^4 < X^{1-2eps}}
>       rho(m, z)."

Divisor-type bound (2.4), verbatim (p. 5):

> "|rho^-(n)| <= 4 ((log(3X))/(log z))^3 rho(n, z) << rho(n, z)."

### 3.1 Theorem 2.1 (the variance estimate that yields Theorem 1.1), verbatim (p. 5-6)

> "Theorem 2.1. Let eps > 0 be sufficiently small, let X >= 3,
> h = (log X)c with c = 2.1, and h1 = X^{99/100}. Let
> (2.5)   a in [c - 1 - 1/10000, c - 1],   and   P1 = (log X)a .
> The function rho^-(n) defined in (2.3) with z = X^{2/11} satisfies the
> following three conditions.
>  (i) For every n in [2X^{1/2}, 3X], we have rho^-(n) <= 1_P(n).
>  (ii) Once X is large enough we have, for all x in (X, 2X],
>       sum_{x < p1 n <= x+h1, p1 ~ P1} rho^-(n) >= h1/(200 log P1 log X).
> (iii) We have
>   (2.6)  (1/X) integral_X^{2X} (1/h sum_{x<p1 n<=x+h, p1~P1} rho^-(n)
>            - (1/h1) sum_{x<p1 n<=x+h1, p1~P1} rho^-(n))^2 dx
>          << 1/(log X)^{2+eps} ."

Crucial-gain remark (p. 6), verbatim:

> "We also remark that a bound of << 1/(log X log P1)^2 for the left-hand
> side of (2.6) would be easy to prove; crucially, we must beat this
> bound."

### 3.2 Theorem 1.1 from Theorem 2.1 (Subsection deduction, p. 5-6)

PARAPHRASE except quotes. Summing Theorem 2.1(ii) over choices of P_1 gives
(2.7): (1/h1) sum ... rho^-(n) >= gamma/log X for all x in (X,2X], with
gamma > 0; Cauchy--Schwarz and (2.6) give (2.8) with (log X)^{2+eps/2}. The
exceptional set (p. 6), verbatim:

> "Xx := {x >= 2 : (1/(log x)^c) sum_{x<p1 n<=x+(log x)^c,
>   (log x)^{c-1-1/1000}<p1<=(log x)^{c-1}} 1_P(n) < gamma/(2(log x))}
>   intersect N."

> "Using the inequality 1_P(n) >= rho^-(n) and combining (2.7) and (2.8),
> we see that |Xx intersect (X, 2X]| << X/(log X)^{eps/2}. The claim now
> follows by summing over dyadic intervals."

Positivity input for Theorem 2.1(ii) (Subsection 2.1, p. 6-7): the discarded
Buchstab sums are converted, via the prime number theorem in short
intervals over length h_2 = X^{99/100}/p_1, to Buchstab-omega integrals
1 - I_2(eps) - I_4(eps) + o(1); a numerical calculation gives
I_4(eps) < 0.0004 and I_2(0) <= 0.99, yielding the factor 0.009 in (ii)
(footnote 1, p. 7: "The Mathematica code for computing the integral can be
found along with the arXiv submission of this paper.").

### 3.3 Proposition 2.2 (decomposition of the minorant), verbatim (p. 7)

> "Proposition 2.2 (Decomposition of the minorant). Let eps > 0 be fixed
> and small enough, and let A >= 5. Let X >= 3,
> z0 = exp((log X)/(log log X)3), and z = X^{2/11}. Let rho^- be as in
> (2.3). Let Y in (X^{1-eps/100}, X/2]. Then there exists a set F
> (depending on X and Y ) consisting of O(exp((log log X)5)) functions
> f : N -> C such that
>   rho^-(n) 1_{n in (Y/2,4Y]} = sum_{f in F} f(n) + cn ,
> where cn are supported on (Y/4, 8Y ] and satisfy
>   (2.10)  sum_n |cn|2 <<_A Y/log^A X ."

The three types (Proposition 2.2(i)-(iii), p. 7), verbatim ranges:

> "(i) (Type I case) f(n) = sum_{n=m1 m2, m1~M1, M2<m2<=(1+delta_A)M2}
>   alpha_{m1} with M1 <= X^{1/2+eps} and M1 M2 in (Y/2, 4Y]."

> "(ii) (Type I/II case) f(n) = sum_{n=m1 m2 m3, m1~M1, m2~M2,
>   M3<m3<=(1+delta_A)M3} alpha_{m1} beta_{m2} with
>   M1^2 M2 <= X^{1-eps}, M2 <= X^{1/4-eps}, and M1 M2 M3 in (Y/2, 4Y]."

> "(iii) (Type II case) For some R in {1, ..., floor(log z / log z0)},
>   f(n) = sum_{n=m1 m2, M1<m1<=(1+delta_A)^R M1, m2~M2} alpha_{m1}
>   beta_{m2} with X^{eps/2} <= M1 <= z, M1 M2 in (Y/2, 4Y], and
>   (2.11) alpha_m = sum_{m=q1...qR, Qj<qj<=Qj(1+delta_A)} 1, where
>   Qj in [z0, z) and Q1 ... QR = M1."

(Proposition 2.2 follows from Lemma 2.3, a Buchstab iteration with acceptable
mean-square error terms cn, p. 8-12. z_0 = exp((log X)/(log log X)^3),
D = exp((log X)/(log log X)); L = floor(log(4X)/log z_0). Not reproduced
in full; the type-II sparsity in (2.11) is the load-bearing feature.)

---

## 4. SECTION 3 (Mean value theorems)

### 4.1 Lemma 3.1 (reduction to Dirichlet polynomials), verbatim (p. 12)

> "Lemma 3.1 (Reduction to Dirichlet polynomials). Let X >= 3,
> T0 = X^{1/1000} and let eps > 0 be small enough but fixed. Let c = 2.1,
> h = (log X)c, a in [c-1-1/10000, c-1], and P1 = (log X)a. Define
>   P1(s) := sum_{p1~P1} 1/p1^s , P(s) := sum_{X/(2P1)<n<=4X/P1}
>            rho^-(n)/n^s .
> Suppose that, for any T >= X/h,
>   integral_{T0}^T |P1(1+it)|2 |P(1+it)|2 dt <<
>       T/(X/h) . 1/(log X)^{2+eps} .
> Then (2.6) holds."

### 4.2 Lemma 3.2, Lemma 3.3 (standard and improved MVT), verbatim (p. 12)

> "Lemma 3.2 (Mean value theorem for Dirichlet polynomials). Let
> N, T >= 1 and A(s) = sum_{n<=N} an n^{-s}. Then
>   integral_{-T}^T |A(it)|2 dt = (2T + O(N)) sum_{n<=N} |an|2 ."

> "Lemma 3.3 (Improved mean value theorem). Let N, T >= 1 and
> A(s) = sum_{n<=N} an n^{-s}. Then
>   integral_{-T}^T |A(it)|2 dt << T sum_{n<=N} |an|2
>       + T sum_{0<|k|<=N/T} sum_{n<=N} |an||an+k| ."

(Proof note, p. 12: from [10, Lemma 7.1] with Y = 10T, x_m = (1/2pi) log m.
The second, off-diagonal, term is what "works better when a_n has sparse
support.")

### 4.3 Lemma 3.4 (Heath-Brown's sparse mean value estimate), verbatim (p. 12-13) -- MANDATORY

> "Lemma 3.4 (Heath-Brown's sparse mean value estimate). Let
> T >= M >= 1, let calM subset [M, T] be a set of integers, and let
> N >= 2. Let M(s) = sum_{m in calM} epsilon_m m^{-s} with
> |epsilon_m| <= 1 and A(s) = sum_{n~N} an n^{-s} for some an in R. Then
> we have, for any eta > 0,
>   (3.1)  integral_{-T}^T |M(1+it)|2 |A(1+it)|2 dt <<_eta
>     ( (|calM|/M)^2 + (NT)^eta ( |calM|T/(M^2 N)
>          + |calM|^{7/4} T^{3/4}/(M^2 N) ) ) max_n |an|2 .
> Moreover, if N >= T^{2/3} or |calM| <= T^{1/3}, the third term on the
> right-hand side of (3.1) can be deleted."

[Display (3.1) confirmed from the rendered page image (p. 13); the "<<_eta"
and the three fraction terms were verified against the image. Proof (p. 13):
"This follows quickly from [8, Theorem 4] ... Now the claim follows from
[8, Theorem 4(iii)] (with eta/2 in place of eta)." Reference [8] is
D. R. Heath-Brown, "The differences between consecutive smooth numbers,"
Acta Arith. 184(3):267-285, 2018. Flag 2.]

### 4.4 Lemma 3.5 (Watt / Deshouillers--Iwaniec twisted moments), verbatim (p. 13)

> "Lemma 3.5. Let A, N, N', T >= 1 with N < N' <= 2N. Let
> N(s) = sum_{N<n<=N'} n^{-s}, A(s) = sum_{m~A} am m^{-s} with an complex
> numbers, and let eps > 0.
>  (i) (Watt's theorem) We have
>   integral_{T/2}^T |N(1+it)|4 |A(1+it)|2 dt <<
>     T^eps ( (T + A^2 T^{1/2})/(N^2 A) + (T + A)/(T^4 A) ) max_m |am|2 .
>  (ii) (Deshouillers--Iwaniec theorem) We have
>   integral_{T/2}^T |N(1+it)|4 |A(1+it)|2 dt <<
>     T^eps ( (T + A^2 T^{1/2} + A^{5/4} T^{3/4})/(N^2 A)
>       + (T + A)/(T^4 A) ) (1/A) sum_{m~A} |am|2 ."

Remark 3.6 (p. 14), verbatim (why (ii) is preferred for type I):

> "Although the A dependence is weaker in Lemma 3.5(ii) than in Lemma
> 3.5(i), the fact that Lemma 3.5(ii) involves the l2 norm of the
> coefficient sequence rather than the maximum makes it more suited for
> our type I estimates in Section 5.1, where we essentially end up taking
> A(s) = P1(s)^k with P1(s) = sum_{p~P1} p^{-s} and P1^k ~ T^{1/10}."

---

## 5. SECTION 4 (Large values) -- the new type II estimate

### 5.1 Lemma 4.1 ("density hypothesis" for Dirichlet polynomials), verbatim (p. 14)

> "Lemma 4.1 (''Density hypothesis'' for Dirichlet polynomials). Let
> eps > 0 be small but fixed, and let T >= N >= 2. Let
> N(s) = sum_{n~N} an n^{-s} with an divisor-bounded. Assume that
>   T^{1-eps/10} >= N >= T^{9/11-10eps}   and   5eps <= sigma <=
>   49/206 - 5eps.
> Then we have
>   |{t in [-T, T] : |N(1+it)| > N^{-sigma}}| << T^{2sigma - eps^2/5} ."

Proof (p. 14): Jutila's large values estimate [10, Theorem 9.10] with k = 7,
G = sum_{n~N} |an|^2/n^2 << (log N)^{O(1)}/N, V = N^{-sigma}; the three-term
Jutila bound collapses to T^{2sigma - eps^2/5}. [Confirmed from rendered
image p. 14.]

### 5.2 Proposition 4.2 (the NEW type II estimate), verbatim (p. 14-15) -- MANDATORY

> "Proposition 4.2 (Type II estimate). Let eps > 0 be small enough but
> fixed. Let T >= 3, and let
>   M1(s) = sum_{m1~M1} alpha_{m1}/m1^s   and   M2(s) = sum_{m2~M2}
>           beta_{m2}/m2^s
> with M1 M2 = T (log T)^{O(1)} and with (alpha_{m1}) and (beta_{m2})
> divisor-bounded. Suppose that
>   T^{eps/5} <= M1 <= T^{2/11+eps}
> and
>   sigma = 49/206 - 10eps.
> Let U subset [0, T] be a measurable set such that, for each t in U, one
> has either |M1(1+it)| >= M1^{-sigma} or |M2(1+it)| >= M2^{-sigma}. Then
>   (4.1)  integral_U |M1(1+it)|2 |M2(1+it)|2 dt <<
>     T^{-eps^2/10} + (log T)^{O(1)} sup_{t in U} |M1(1+it)|2 ."

[Statement confirmed from rendered image (p. 14-15). "The new type II
estimate" the abstract advertises is Proposition 4.2; its engine is
Lemma 4.1 (Jutila) plus, in Section 5.3, Lemma 3.4 (Heath-Brown sparse).]

Remark 4.3 (p. 15), verbatim -- what sigma controls:

> "The key aspect in Proposition 4.2 is the value of sigma, which we want
> to maximize, as the value of sigma eventually plays an important role
> in determining our exponent c in Theorem 2.1 in Subsection 5.3."

> "In [18], integrals of the type (4.1) were estimated by using a
> pointwise bound on M1(1+it) and the Halasz--Montgomery inequality on
> the sparse mean square of M2(1+it), whereas in the proof of Proposition
> 4.2 we obtain stronger estimates by first splitting the integral into
> pieces according to the sizes of M1(1+it), M2(1+it) and then applying
> Jutila's large values estimate."

Proof of Proposition 4.2 (p. 15): partition T = T1 union T2 union T3;
T1 handled by discrete mean value theorem giving |T1| << T^{50eps}; the
Halasz--Montgomery inequality on T1 gives << (log T)^{O(1)} sup |M1|^2;
T2 split into T2,sigma1,sigma2 with the key bound
|T2,sigma1,sigma2| << T^{2 min{sigma1,sigma2} - eps^2/5} from Lemma 4.1
(applied to M1^ell in [T^{5/6-eps}, T^{1-eps/2}] if sigma1<=sigma2, else to
M2 of length in [T^{9/11-eps}(log T)^{-O(1)}, T^{1-eps/5}(log T)^{O(1)}]),
yielding integral over T2 << T^{-eps^2/10}.

---

## 6. SECTION 5.3 -- WHERE THE EXPONENT 2.1 IS FORCED

This is the mandatory "where is 2.1 forced" locus. PARAPHRASE except
quotes; the governing displays are transcribed complete.

Setup (Subsection 5.3, p. 20): F(s) = M1(s) M2(s), type II, with
X^{eps/2} <= M1 <= z = X^{2/11}, M1 M2 in (X/(2P1), 4X/P1], and alpha_{m1}
the R-fold smooth-support coefficients from (2.11). U is split as
U1 union U2 union U3 by the sizes of |M1|,|M2| against the threshold
exponent 49/206 - 10eps (5.7). U1 is killed by the Vinogradov--Korobov
zero-free region ((5.6): sup |M1(1+it)| << exp(-2(log X)^{1/10}));
U3 trivially. Only U2 (both |Mj| in the "medium" band, sigma_j > 49/206-10eps)
survives, split into U2,sigma1,sigma2 (5.7). The reduction (p. 20):

> "(5.8)  |U2,sigma1,sigma2| << M1^{2 sigma1} M2^{2 sigma2}
>         exp(-(log log X)7)."

The amplifier is M(s) = P1(s)^k/k! with k = ceil(log T1 / log(2P1)), so
M = P1^k in [T1/(2^k P1), T1/2^k], and calM = the k-fold products of primes
in (P1, 2P1] -- all 2P1-smooth, giving (p. 20-21), verbatim:

> "|calM| <= M^{1-1/a+o(1)}"

by the smooth-number bound [9, (1.14)], and (5.9) |M(1+it)| >=
M^{-eps/10}/k! >= M^{-eps/10-1/a+o(1)} for all t in U.

FIRST bound (via Lemma 3.4, N = M2), giving (5.10) (p. 21), verbatim:

> "(5.10)  M^{eps/5} << M1^{2 sigma1}/T1^{eps^2}   and   M1^{1-2 sigma1}
>          << T1^{-eps/3} M^{1-1/a}."

> "Since M in [T1^{1-eps^2}, T1], M1 >= T1^{eps/2} and
> sigma1 > 49/206-10eps > 1/5+2eps, the first claim always holds when eps
> is sufficiently small. The second claim holds for sufficiently small
> eps when
>   a > 1/(1 - theta(1 - 2 sigma1) - eps),
> where we have denoted
>   (5.11)  theta = (log M1)/(log X) in [eps/2, 2/11]."

> "Hence we can from now on assume that
>   (5.12)  theta(1 - 2 sigma1) >= 1 - 1/a - eps   and   sigma1 in
>           [49/206 - 10eps, 1/2)."

SECOND bound (via the M1^{10} / M route, p. 21), verbatim:

> "Since M1 <= T1^{2/11+eps/2}, the second term dominates when a <= 11/10.
> Hence (5.8) holds if
>   T1^{1/a+4eps} <= M1^{5-8 sigma1} M2^{2 sigma2}.
> Recalling (5.11) and that sigma2 >= 49/206 - 10eps, this holds if
>   (5-8 sigma1) theta + (1-theta) . 2 . 49/206 > 1/a + 25eps
>   <=> 4(1-2 sigma1) theta + 49/103 + theta(1 - 2 . 49/206)
>        > 1/a + 25eps."

The optimization (p. 22), verbatim -- the last three steps that pin 2.1:

> "Now the left-hand side is increasing in theta (since sigma1 < 1/2), so
> using (5.12) it suffices to have
>   4 - 4/a - 4eps + 49/103 + (1 - 1/a - eps)(1 - 2.49/206)/(1 - 2 sigma1)
>     > 1/a + 25eps.
> Since sigma1 >= 49/206 - 10eps, this holds if
>   6/a < 5 + 49/103 - 100eps,
> which in turn holds for eps > 0 small enough if
>   a > 103/94 + 100eps.
> But 103/94 < 1.1 - 1/10000, and the claim follows."

THE BINDING CONSTRAINT. The exponent is c = a + 1 (h = (log X)^c,
P_1 = (log X)^a, a in [c-1-1/10000, c-1]). The type II argument closes only
for a > 103/94 + 100eps ~ 1.0957..., and it needs a <= 11/10 (so that "the
second term dominates," p. 21). Since 103/94 < 1.1 - 1/10000, one may take
a just below 1.1, hence c = a + 1 just below 2.1; the paper fixes c = 2.1,
a in [2.1-1-1/10000, 1.1] = [1.1-1/10000, 1.1]. Two constraints are
simultaneously near-binding and jointly force 2.1:

- theta <= 2/11: the type II variable M1 ranges only up to z = X^{2/11}
  (the Harman-sieve level in Proposition 2.2(iii) / Lemma 4.1's window),
  so theta = (log M1)/(log X) <= 2/11 (5.11); the left side of the
  optimization is increasing in theta, so theta = 2/11 is used.
- sigma = 49/206 - 10eps: the large-value threshold in Proposition 4.2,
  inherited from Jutila's estimate in Lemma 4.1 (valid for
  5eps <= sigma <= 49/206 - 5eps); sigma1 is pushed to its minimum
  49/206 - 10eps.

These are exactly the two quantities isolated in Remark 5.2 (p. 22),
verbatim, which gives the general exponent formula:

> "Remark 5.2. We note that in general if one had Proposition 4.2 with
> sigma in place of 49/206 and theta in place of 2/11 (with
> 1/5 + 2eps <= sigma <= 1/2), then the first part of the argument in
> Subsection 5.3 would imply that one can deal with type II sums with one
> variable from [X^{eps/2}, X^theta] with the exponent
>   (5.13)  c = 1 + 1/(1 - theta(1 - 2 sigma) - eps)
> in Theorem 2.1 (with a in [c - 1 - eps^2, c - 1] in place of (2.5))."

[Numerically, theta = 2/11 and sigma = 49/206 give 1 - 2sigma = 108/206 =
54/103, theta(1-2sigma) = (2/11)(54/103) = 108/1133 ~ 0.0953, so
c = 1 + 1/(1 - 0.0953 - eps) -> 2.105... as eps -> 0, i.e. 2.1. Any
improvement of EITHER theta (a longer type-II window) OR sigma (a better
large-value / density input) lowers c below 2.1 via (5.13). Extractor
arithmetic, flagged; the paper states only (5.13) and a > 103/94.]

Remark 5.3 (p. 22): the authors note the argument is deliberately not
optimized ("our relatively clean argument already gives a very substantial
improvement over [18]"), and list amplification of Jutila's result and
better use of M1, M2 shape/length as available improvements.

---

## 7. SECTION 6 (Heath-Brown identity variants) and SECTION 7 (E_3, all intervals)

Section 6 (p. 22-24) redoes the argument with Heath-Brown's identity in
place of Harman's sieve. Unconditionally (L = 3) it gives the WEAKER
exponent (6.1) with h = (log x)^{2+3/13+eps}, a = 1 + 3/13, via (5.13) with
theta = 1/3, sigma = 7/32 - 10eps (the latter from Bourgain's zero-density
estimate [2, Lemma 4.60]) (p. 23-24), verbatim:

> "Now we have in (5.13) theta = 1/3 and sigma = 7/32 - 10eps which, after
> adjusting eps, gives Theorem 2.1 with c = 2 + 3/13 + eps."

Under the Lindelof hypothesis (L = ceil(1/eps)) it gives c = 2 + eps
(p. 24, Subsection 6.2), via (5.13) with theta = eps, or theta in
(eps, 1/2-eps] and sigma = 1/2 - eps.

Section 7 (p. 24-25) proves Theorem 1.2 (E_3 in all intervals): with
a = 1.1, c = 1 + a/2 = 1.55, h = sqrt(x)(log x)^{1.55}, P_1 = (log x)^a,
p_2 ~ sqrt(x/P1)/2, the same minorant (with X = sqrt(x P1),
z = (sqrt(x P1))^{2/11}) and the same Dirichlet-polynomial reduction reduce
(7.1) to "essentially the claim (5.2) that was proved in Section 5 (after
adjusting eps and replacing X with sqrt(x P1))" (p. 25).

---

## 8. UNIFORMITY LEDGER

WHAT IS FIXED (absolute, independent of X):
- The E_2 object rank: exactly two prime factors p_1 p_2. Never grows.
- c = 2.1 (Theorem 1.1/2.1); c = 1.55 (Theorem 1.2). Absolute.
- The threshold exponents 2/11 (sieve level z = X^{2/11}), 49/206 (large-
  value / Jutila threshold), 9/11 (lower length in Lemma 4.1), 7/32
  (Bourgain variant, Section 6), 103/94 and 11/10 (the a-window). All
  absolute rationals.
- eps: a single small FIXED parameter chosen once and held; delta = delta(eps)
  in Theorem 1.1 and the exceptional-set exponent depend on it but eps does
  NOT tend to 0 with X inside any single application.
- eta in Lemma 3.4: free but fixed; c_0, delta, gamma in Theorem 1.1/2.1:
  absolute positive constants.
- A >= 5 in Proposition 2.2 / Lemma 2.3: a fixed parameter taken
  "sufficiently large"; implied constants carry <<_A.

WHAT GROWS WITH X (auxiliary, NOT an object rank):
- a := P_1 = (log X)^a with a in [1.1 - 1/10000, 1.1]: P_1 -> infinity, but
  a is a FIXED exponent in [c-1-1/10000, c-1] (2.5).
- k in the amplifier M = P_1^k: chosen so P_1^k = X^{1-o(1)} (Section 5.3)
  or P_1^k ~ T^{1/10} (Section 5.1) or T^{eps/2} (5.2); k ~ log X / log log X
  -> infinity. This is a Dirichlet-polynomial power, NOT a tuple rank.
- R in {1,...,floor(log z / log z0)} (Proposition 2.2(iii)) and
  L = floor(log(4X)/log z0) (Lemma 2.3(ii)): number of smooth factors /
  Buchstab iterations; grow like log log X (z0 = exp(log X/(log log X)^3)).
  Bounded so that ((log 4X)/(log z0)+1)^{2L} = (log X)^{o(1)} (p. 11).
- |F| = O(exp((log log X)^5)) functions in the decomposition (2.10).
- z0 = exp((log X)/(log log X)^3), D = exp((log X)/(log log X)): grow with X.

THRESHOLD DEPENDENCIES (which forces which):
- delta_A = (log X)^{-10A} sets the granularity of the delta_A-adic splits;
  A is chosen after eps.
- The final exponent c = 2.1 is forced by (5.13) c = 1 + 1/(1-theta(1-2sigma)
  -eps) with theta = 2/11 (sieve level) and sigma = 49/206 (Jutila
  threshold). Both are near-binding; improving either lowers c. Section 6
  shows the SAME formula (5.13) with (theta,sigma) = (1/3, 7/32) gives the
  weaker unconditional 2 + 3/13, and (theta,sigma) = (eps, 1/2) gives 2 + eps
  under Lindelof.
- The h_1 = X^{99/100} long window (2.5) is the reference against which the
  short-window count is compared in the variance (2.6); it is X-power-scale,
  not log-scale.

CONSTANTS ABSOLUTE vs PARAMETER-DEPENDENT:
- c_0, delta, gamma (Theorem 1.1/2.1): absolute.
- Implied constants in (2.6), (2.10), Lemmas 3.4/3.5, Prop 4.2: absolute or
  <<_A / <<_eps / <<_eta as printed; none depend on x within an interval.
- The count lower bound in Theorem 1.1 is c_0 (log x)^{1.1}: a POWER of
  log x, absolute constant c_0; it is a LOWER bound on the number of E_2
  numbers p_1 p_2 in (x, x+(log x)^{2.1}] carrying a prime factor p_1 in
  ((log x)^{1.09}, (log x)^{1.1}].

---

## 9. WHAT THE PAPER DOES NOT CONTAIN (mandatory NOT-FOUND probes, Section 4.2)

"primes (as opposed to E_2 / almost primes) in the conclusion": NOT FOUND in
this text. The conclusion of Theorem 1.1 is about E_2 numbers p_1 p_2, and
of Theorem 1.2 about E_3 numbers p_1 p_2 p_3. Primes appear only in
background/motivation: Selberg's conditional prime result (p. 2) and Jia's
unconditional (x, x+x^{1/20}] for primes (p. 2), both cited to contrast, and
the explicit statement "we understand the short interval distribution of Ek
numbers for k >= 2 significantly better than that of the primes" (p. 2).

"consecutive": NOT FOUND in this text as a statement of the paper. The word
occurs only inside cited reference titles: [1] "The difference between
consecutive primes. II", [8] "The differences between consecutive smooth
numbers", [17] "... the difference between consecutive primes" (p. 25-26).
No two-point / coincidence / consecutive-object statement is proved.

"gap": NOT FOUND in this text. No prime-gap or gap-word quantity appears in
any statement; the paper counts E_2 (E_3) numbers in an interval, never
differences between them.

"upper bound on the count of E_2 numbers": NOT FOUND as a proven statement.
Theorem 1.1 gives only a LOWER bound (>= c_0 (log x)^{1.1}). The single
gesture toward matching size is the unproven remark (p. 1): "One can show
that the lower bound in Theorem 1.1 is of the correct order of magnitude,
although it is only for those E2 numbers that have a prime factor in a
certain superdyadic interval." No upper bound on |{p_1 p_2 in interval}| is
stated or proved.

"second moment or variance of the count": FOUND. Theorem 2.1(iii), the
variance estimate (2.6), IS a mean-square (second-moment) statement -- but
of the MINORANT-weighted short-interval count against its long-window
average, averaged over x in [X, 2X], used as the tool that yields the
lower-bound Theorem 1.1. Verbatim (p. 5-6):

> "(2.6)  (1/X) integral_X^{2X} (1/h sum_{x<p1 n<=x+h, p1~P1} rho^-(n)
>   - (1/h1) sum_{x<p1 n<=x+h1, p1~P1} rho^-(n))^2 dx << 1/(log X)^{2+eps}."

It is NOT a variance/second moment of the count of E_2 numbers themselves
(the sum is over the minorant rho^-, and the object weighted is p_1 n with
p_1 ~ P_1, not a full E_2 count), and it is an upper bound on that variance,
not a lower bound or a limiting distribution.

"any parameter playing the role of a growing tuple rank": NOT FOUND. The
arithmetic object has fixed rank (2 for E_2, 3 for E_3). The parameters that
grow with X -- k (amplifier power P_1^k), L, R (numbers of smooth
factors/Buchstab iterations), |F| -- are Dirichlet-polynomial and
decomposition depths, not a rank of the counted object; none appears in the
conclusion, and none is a tuple dimension.

Additional located absences relevant to the project (extractor-checked
across all 26 pages): no singular series and no Hardy--Littlewood
tuple-correlation constant appears anywhere; "singular series": NOT FOUND in
this text. No class-normalised or gap-word-conditioned quantity; "word
grain": NOT FOUND in this text. No unbounded/sparse scale sequence: the
results hold for ALMOST ALL x in [1, X] (all but << X/(log X)^delta), i.e.
a density-1 set for every large X, not a thin scale set.

---

## COMMENTARY (assessment, NOT extraction)

Consuming context (quoted verbatim from the dispatch, Section 4):

> The project needs an unconditional averaged middle-slot non-concentration
> / upper-uniformity statement at rank k = (2/ln 2 + o(1)) lnln x, window
> h = A'L ln x ~ (ln x)(lnln x), of strength enough to keep a fixed
> proportion of D0-depth site mass off its modal middle on some unbounded
> scale sequence per s -- a statement that fails in the even-Cramer-smooth
> model.  Six axes: A1 rank; A2 window; A3 grain (class masses N_{P,d} of
> consecutive-gap words, not prime counts); A4 direction (upper /
> non-concentration); A5 strength (constant order suffices); A6 density
> (sparse scales, no s-uniformity).  A1-A4 are not relaxed by CG; A5 and A6
> are.

C1. What this paper unconditionally supplies. An UNCONDITIONAL result that,
for almost all x in [1, X] (exceptional set << X/(log X)^delta), the
interval (x, x + (log x)^{2.1}] contains E_2 numbers -- in fact >=
c_0 (log x)^{1.1} of them carrying a prime factor p_1 in
((log x)^{1.09}, (log x)^{1.1}] (Theorem 1.1). The engine is a genuinely
power-saving variance bound in short intervals (Theorem 2.1(iii), (2.6):
mean-square deviation << 1/(log X)^{2+eps}, explicitly "beating"
1/(log X log P_1)^2, p. 6). The window (log x)^{2.1} is a fixed POWER of
log, the smallest achieved unconditionally for E_2. This is the located
unconditional short-interval result nearest to the logarithmic scale.

C2. What it does NOT supply -- rank (A1) and grain (A3). The object has
FIXED rank two. There is no growing tuple rank anywhere in the conclusion
(Section 9). The grain is a count of integers of a fixed multiplicative type
(E_2 = p_1 p_2), NOT class masses N_{P,d} of consecutive-gap words. Nothing
here bears on a rank k ~ (2/ln 2) lnln x, and nothing produces or bounds a
gap-word class mass; the two growing internal parameters (the amplifier
power k with P_1^k = X^{1-o(1)}, and the smooth-factor count L,R ~ lnln x)
are Dirichlet-polynomial decomposition depths that never surface as an
object rank.

C3. What it does NOT supply -- window (A2). The window is (log x)^{2.1},
i.e. exponent 2.1 in log x, which is polynomially LARGER than the target
h ~ (ln x)(lnln x) ~ (ln x)^{1+o(1)}. The paper's own companion facts sharpen
the miss: E_3 reaches (log x)(log log x)^{6+eps} ([18], quoted p. 2) and
P_2 reaches h(x) log x for any h -> infinity ([13], quoted p. 2) -- both AT
or below the target window -- but for E_2 the barrier is 2 + eps even under
RH (p. 2), and 2.1 is what unconditional methods reach. So the A2 target is
attained by the neighbouring E_3/P_2 lines, not by this E_2 theorem.

C4. Direction (A4) and strength (A5). The central estimate (2.6) has exactly
the A4 shape: it is an UPPER bound on an x-averaged mean-square fluctuation
of a short-interval count -- a non-concentration / upper-uniformity
statement. Its strength is a power-of-log saving (<< (log X)^{-2-eps}),
which is MORE than the "constant order suffices" the target permits under
A5. So in isolation A4 and A5 are met, and comfortably. The catch is that
this non-concentration is of the E_2-minorant count (wrong grain A3, wrong
rank A1, wrong window A2), so the A4/A5 match does not transfer to the
needed object.

C5. Density (A6). The result holds for ALMOST ALL x (density-1 complement,
X/(log X)^delta), unconditionally. This is strictly STRONGER than the A6
target, which only asks for an unbounded/sparse scale sequence with no
s-uniformity (A6 is the CG-relaxed axis). So A6 clears with room to spare.

C6. Where 2.1 is forced, restated for the campaign. The exponent is
c = 1 + 1/(1 - theta(1 - 2 sigma) - eps) (Remark 5.2, (5.13)) with the two
near-binding inputs theta = 2/11 (the Harman-sieve type-II level z = X^{2/11})
and sigma = 49/206 (the Jutila large-value threshold in Lemma 4.1 /
Proposition 4.2); the closing inequality is a > 103/94 + 100eps with
103/94 < 1.1 - 1/10000, and c = a + 1 (p. 22). Improving EITHER the type-II
window theta OR the large-value exponent sigma lowers c; the paper reaches
2 + eps only by trading the sieve for the Lindelof hypothesis (Section 6).
For the project this fixes the price of the logarithmic window on the E_2
line: it is a large-value/sieve-level bottleneck at fixed rank two, not a
rank phenomenon, and it is unrelated to any middle-slot word-mass
non-concentration.

Per-axis verdict:
- A1 (rank k ~ (2/ln2) lnln x): FAILS (object rank is fixed at two; no
  growing tuple rank in the conclusion, Section 9).
- A2 (window h ~ (ln x)(lnln x)): FAILS (window is (log x)^{2.1}, a power of
  log larger than (ln x)^{1+o(1)}; E_3/P_2 neighbours reach the target, this
  E_2 theorem does not).
- A3 (grain = consecutive-gap word class masses): FAILS (grain is a count of
  E_2 integers of fixed multiplicative type, not gap-word class masses; no
  word-grain quantity, Section 9).
- A4 (direction = upper / non-concentration): CLEARS in form (Theorem
  2.1(iii)/(2.6) is an x-averaged upper bound on a short-interval variance =
  non-concentration), but coupled to the wrong grain/rank/window.
- A5 (strength = constant order suffices): CLEARS (delivers a power-of-log
  saving << (log X)^{-2-eps}, exceeding the constant-order requirement).
- A6 (density = sparse scales, no s-uniformity): CLEARS, and exceeds it
  (holds for almost all x, complement << X/(log X)^delta, unconditionally).

Not all six axes clear (A1, A2, A3 fail); this is NOT a located carrier.

Even-Cramer-smooth deterministic gap system (q_1=2, q_2=3, q_3=5, q_4=7,
q_{n+1}=q_n+2*ceil(ln q_n / 2)): UNTESTED against it. The paper's object is
the count of E_2 (E_3) integers in a genuine short interval, a
multiplicative-arithmetic statement; it never considers a deterministic gap
model, and its conclusion is not a gap-word statistic that the model could
be evaluated on. The paper contains nothing that would either hold or fail
in that system. (Untested, per instruction, not guessed.)

---

## FLAGS (consolidated)

1. [TRANSCRIPTION-UNSURE, resolved-by-image] Theorem 1.1 (p. 1): the
   "<<" in "for all but << X/(log X)^delta" dropped to a blank gap in the
   pdftotext -layout layer; resolved from the rendered page image (p. 1).
   The inequality body (>= c_0 (log x)^{1.1}, ranges (log x)^{1.09} <
   p_1 <= (log x)^{1.1}) agrees between text layer and image.

2. [TRANSCRIPTION-UNSURE, resolved-by-image] Lemma 3.4 (3.1), p. 12-13: the
   "<<_eta" subscript and the three right-hand fractions ((|calM|/M)^2,
   |calM|T/(M^2 N), |calM|^{7/4} T^{3/4}/(M^2 N)) were verified against the
   rendered image (p. 13); the text layer split the display across the page
   fold and dropped the Vinogradov symbol.

3. [TRANSCRIPTION-UNSURE, resolved-by-image] Proposition 4.2 (4.1), p. 14-15,
   and the entire 2.1-forcing chain (5.9)-(5.13), a > 103/94, p. 20-22:
   all "<<"/">=" relations and exponents (2/11, 49/206, 103/94, 11/10)
   confirmed against rendered images (p. 14, 21, 22).

4. [PRINTED-ODDITY] Throughout, Vinogradov notation is the curly "<<"/">>"
   (paper's Notation, p. 4). Rendered as "<<"/">>" here. Subscripts <<_A,
   <<_eps, <<_eta transcribed as printed.

5. [PRINTED-ODDITY] The exceptional set in the Theorem 1.1 deduction (p. 6)
   is printed with a script/calligraphic X; transcribed as "Xx" to
   distinguish it from the scale variable X. Likewise script-M is "calM",
   script-U/T/F are "Uu"/"Tt"/"Ff".

6. Extractor arithmetic (NOT in the paper), flagged in Section 6: the
   numerical evaluation of (5.13) at (theta,sigma) = (2/11, 49/206) giving
   c -> 2.105... is the extractor's, to make the "2.1" explicit; the paper
   states only the closed form (5.13), the inequality a > 103/94 + 100eps,
   and "103/94 < 1.1 - 1/10000" (p. 22).

7. The footnote 1 (p. 7) refers to Mathematica code accompanying the arXiv
   submission (for I_2(0) <= 0.99, I_4(eps) < 0.0004); that code is NOT in
   the PDF and was not consulted (session discipline).
