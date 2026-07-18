# EXTRACTION: Merikoski, "Limit points of normalized prime gaps"

Source (only evidence base): /home/istr/pro/erdos251/dossier/1811.03008v3.pdf
arXiv:1811.03008v3 [math.NT] 2 Mar 2021. Author: JORI MERIKOSKI (as printed;
address block p. 32: Department of Mathematics and Statistics, University of
Turku, FI-20014 University of Turku, Finland; jori.e.merikoski@utu.fi).
32 pages; printed page numbers 1-32 coincide with PDF pages. Title as
printed on p. 1: "LIMIT POINTS OF NORMALIZED PRIME GAPS". Section 6 (p. 26)
states "The above text agrees with the published version of the article"
and then adds a correction, i.e. v3 = published text + erratum section.

Transcription conventions: ASCII only. Diacritics transliterated (Erdos,
Yildirim, Matomaki, Zurich, Cramer, Liege, Westzynthius as printed). Math in
LaTeX-like ASCII: \mu, \phi, \omega (Buchstab), \Lambda, \nu, \tau_k,
\beta_i, \alpha, \delta, \epsilon, \gamma (Euler-Mascheroni), <=, >=,
<< (Vinogradov), >>, \asymp, != for "not equal", emptyset. L denotes the
paper's blackboard-bold IL (set of limit points); P denotes blackboard-bold
primes; 1_P is the characteristic function of the primes. log_2 = iterated
log (paper's usage, e.g. P >= T^{1/log_2 T}). P(w) := prod_{p <= w} p;
P^-(d), P^+(d) smallest/largest prime factor; binom(v,2) = v choose 2.
The paper consistently prints "Lebesque" for "Lebesgue"
[TRANSCRIPTION-UNSURE: rendered glyphs read "Lebesque" everywhere; kept as
printed]. Anchors are theorem/equation/section numbers; page numbers
(printed = PDF) secondary.

Everything up to the final section is EXTRACTION (what the paper says).
Commentary appears ONLY in the final marked section.

---

## 1. ABSTRACT AND MAIN THEOREMS (verbatim)

Abstract (p. 1), verbatim:

> "We show that at least 1/3 of positive real numbers are in the set of limit
> points of normalized prime gaps. More precisely, if p_n denotes the nth
> prime and L is the set of limit points of the sequence
> {(p_{n+1} - p_n)/log p_n}_{n=1}^infty, then for all T >= 0 the Lebesque
> measure of L cap [0, T] is at least T/3. This improves the result of Pintz
> (2015) that the Lebesque measure of L cap [0, T] is at least (1/4 - o(1))T,
> which was obtained by a refinement of the previous ideas of Banks,
> Freiberg, and Maynard (2015). Our improvement comes from using Chen's
> sieve to give, for a certain sum over prime pairs, a better upper bound
> than what can be obtained using Selberg's sieve. Even though this
> improvement is small, a modification of the arguments Pintz and Banks,
> Freiberg, and Maynard shows that this is sufficient. In addition, we show
> that there exists a constant C such that for all T >= 0 we have
> L cap [T, T + C] != emptyset, that is, gaps between limit points are
> bounded by an absolute constant."

[TRANSCRIPTION-UNSURE: the abstract's "(2015)" year-style citations and the
phrase "the arguments Pintz and Banks, Freiberg, and Maynard" (apparently
missing an "of") are transcribed as rendered.]

Contents (p. 1): 1. Introduction and main results (1); 2. Modified
Bombieri-Vinogradov Theorem (7); 3. Chen's sieve upper bound for prime
pairs (12); 4. Modified Maynard-Tao sieve (22); 5. Proof of Theorem 1 (24);
6. A correction to the proofs of Lemmata 15 and 16 (26); References (31).

Introduction framing (Section 1, p. 1), verbatim:

> "(1.1)  (1/N) |{ n <= N : (p_{n+1} - p_n)/log p_n in [a, b] }|
>           ~ int_a^b e^{-u} du,   N -> infty."

> "To approach (1.1), consider the following conjecture of Erdos [5]: if L
> denotes the set limit points of the sequence
> {(p_{n+1} - p_n)/log p_n}_{n=1}^infty, then L = [0, infty]. By the 1931
> result of Westzynthius [19] we know that infty in L, and from the seminal
> work of Goldston, Pintz and Yildirim [10] it follows that 0 in L. Besides
> 0 and infty no other real number is known to be in L."

Prior-results paragraph (Section 1, p. 2), verbatim:

> "It is known that L has a positive Lebesque measure (Erdos [5] and Ricci
> [17]). Goldston and Ledoan [9] extended the method of Erdos to show that
> intervals of certain specific form, e.g. [1/8, 2], contain limit points.
> In addition, Pintz [15] has shown that there is an ineffective constant c
> such that [0, c] subseteq L (by applying the ground-breaking work of Zhang
> [21] on bounded gaps between primes)."

> "Note that L is Lebesque-measurable since it is a closed set. Hildebrand
> and Maier [11] showed that there exists a positive constant c such that
> the Lebesque measure of L cap [0, T] is at least cT for all sufficiently
> large T. Following the breakthrough of Maynard [12] on bounded gaps
> between primes, it was proved by Banks, Freiberg and Maynard [2] that this
> holds with c = 1/8 - o(1), that is, asymptotically at least 1/8 of
> positive real numbers are limit points. Pintz [14] improved this to
> c = 1/4 - o(1) by modifying the argument of [2]; this was shown by Pintz
> for more general normalizations also. This was then extended to more
> general and especially larger normalizing factors than log p_n by Freiberg
> and Baker [1], by combining the arguments with the work of Ford, Green,
> Konyagin, Maynard, and Tao [6] on long prime gaps."

Theorem 1 (Section 1, p. 2), verbatim:

> "Theorem 1. Let beta_1 <= beta_2 <= beta_3 <= beta_4 be any real numbers.
> Then
>   L cap { beta_j - beta_i :  1 <= i < j <= 4 } != emptyset."

Paragraph after Theorem 1 (p. 2), verbatim (block-count history):

> "The proof of this will be given in Section 5. We note that [2, Theorem
> 1.1] gives this for nine real numbers in place of four, and [14, Theorem
> 1] is the same but for five real numbers. Using the same argument as in
> the proof of [2, Corollary 1.2] this implies that the Lebesque measure of
> L cap [0, T] is >= (1/3 - o(1))T as T -> infty, where the o(1) is
> ineffective. Using a more elaborate construction based on similar ideas we
> will show below"

Corollary 2 (Section 1, p. 2), verbatim:

> "Corollary 2. For all T > 0 we have
>   mu(L cap [0, T]) >= T/3,
> where mu denotes the Lebesque measure on R."

Bridge sentence to Corollary 3 (p. 2), verbatim:

> "Another way to approach the conjecture that L = [0, infty] would be to
> show that for any given positive real x we can find a limit point close to
> x; using Theorem 1, we will show below that gaps between limit points are
> bounded by an absolute (ineffective) constant (note that this actually
> follows already from [2, Theorem 1.1], as is evident from the proof):"

Corollary 3 (Section 1, p. 2), verbatim:

> "Corollary 3. There exists a constant C >= 0 such that for all T >= 0 we
> have
>   L cap [T, T + C] != emptyset."

SYNDETICITY sentence (Section 1, p. 2, directly after Corollary 3),
verbatim:

> "In the language of combinatorics, a set A subseteq [0, infty] is called
> syndetic if there is a constant C such that every interval of length C
> intersects with A (cf. [3], for example). Thus, Corollary 3 can be
> rephrased as saying that the set of limit points L is syndetic."

Remark 1 (Section 1, p. 3), verbatim:

> "Remark 1. By similar ideas as in the work of Baker and Freiberg [1], one
> can extend our results to other normalizations of prime gaps, replacing
> log p_n by a function which can grow somewhat quicker than the logarithm
> (cf. [1, Theorem 6.2] for what normalizations are allowed). We have
> restricted our attention to the logarithmic normalization to avoid having
> to define cumbersome notation, with the hope that this makes the article
> more accessible."

---

## 2. THE MEASURE AND SYNDETICITY REDUCTIONS (Sections 1.1-1.2)

Proposition 4 (Section 1.1, p. 3), verbatim (Corollary 2 = Theorem 1 +
Proposition 4 with k = 4, giving T/(k-1) = T/3):

> "Proposition 4. Let k >= 2 and let B subseteq [0, infty) be any
> Lebesque-measurable set satisfying the following property: for any real
> numbers beta_1 <= beta_2 <= ... <= beta_k we have
>   B cap { beta_j - beta_i :  1 <= i < j <= k } != emptyset.
> Then for any T > 0 we have
>   mu(B cap [0, T]) >= T/(k - 1)."

The proof (pp. 3-4) is an elementary covering argument: inductively chosen
r_j, s_j with S_j := {s > r_{j-1} : Delta(r_0,...,r_{j-1}, s) cap B =
emptyset}, s_j := inf S_j, where Delta(beta_1,...,beta_m) := {beta_j -
beta_i : 1 <= i < j <= m}; the assumption forces termination after at most
k - 1 steps, [r_j, s_{j+1}) subseteq union_{i=0}^{j} (B + r_i), and (1.2)
plus telescoping gives (p. 4, verbatim conclusion):

> "Hence, for any T > 0 we have mu([0, T) cap B) >= T/(lambda + 1) -
> epsilon >= T/(k - 1) - epsilon by using lambda + 1 <= l <= k - 1. Since
> epsilon > 0 can be made arbitrarily small, we have mu([0, T) cap B) >=
> T/(k - 1)."

Section 1.2 header sentence (p. 4), verbatim:

> "Proof of Corollary 3. Corollary 3 follows from Theorem 1 using the
> following general proposition. This is also proved in the work of
> Bergelson, Furstenberg, and Weiss [3, Section 1, second paragraph] but we
> give our own different proof of this."

Proposition 5 (Section 1.2, p. 4), verbatim:

> "Proposition 5. Let B subseteq [0, infty) be any set satisfying the
> following property: there exists an integer k >= 2 such that for any real
> numbers beta_1 <= beta_2 <= ... <= beta_k we have
>   B cap { beta_j - beta_i :  1 <= i < j <= k } != emptyset.
> Then there exists a constant C >= 0 (ineffective) such that for all
> T >= 0 we have
>   B cap [T, T + C] != emptyset."

Lemma 6 (Section 1.2, p. 4), verbatim:

> "Lemma 6. Let B subseteq [0, infty) satisfy the assumptions of
> Proposition 5. Let w be any given function such that w(T) -> infty as
> T -> infty, and w(T) > 0 for T > 0. Then there exists a constant C,
> depending only on the choice of w, such that for all T > C we have
>   B cap [T - w(T), T] != emptyset."

(Proofs pp. 4-5: contradiction via A_1 < A_2 < ... < A_{k-1} with
w(A_1) < ... < w(A_{k-1}) and A_j < w(A_{j+1}), eqs. (1.3)-(1.5); setting
beta_0 := 0, beta_j := A_j puts all differences into
union_j [A_j - w(A_j), A_j], contradicting the difference-set hypothesis.
Proposition 5 follows by building a step function w from a hypothetical
sequence of empty windows. The ineffectivity of C is structural: C comes
from this compactness/contradiction argument.)

---

## 3. OUTLINE ANATOMY (Section 1.3): WHERE CHEN'S SIEVE ENTERS, EQ. (1.6)

Outline, step 1 - modified Erdos-Rankin clearing (Section 1.3, p. 5),
verbatim:

> "Let N be large and suppose we are given an admissible K-tuple
> H = {h_1, ..., h_K} with h_j <= C log N for all j for some large C. Then
> by a variant of the Erdos-Rankin construction (cf. [2, Section 5]), one
> can show that there is an integer b and a smooth modulus W < N^epsilon
> such that for any N < n <= 2N with n == b (W), if there are prime numbers
> in the interval [n, n + C log N], then they must belong to the set n + H."

Outline, step 2 - Maynard-Tao with block anti-concentration (p. 5),
verbatim:

> "By using the Maynard-Tao sieve, we can show that there exists
> N < n <= 2N with n == b (W) such that n + H contains prime numbers once
> K = |H| is large enough. Furthermore, suppose that we have a partition
> H = H_1 cup H_2 cup ... cup H_M into M sets of equal size. Then we can
> show that there exists a constant A such that for any integer a >= 1, if
> M = ceil(Aa) + 1, then for at least a + 1 distinct indices j the set
> n + H_j contains a prime number. That is, the prime numbers that we find
> by the Maynard-Tao sieve are not too much concentrated on any particular
> set n + H_j."

THE PAIRWISE UPPER-SIEVE SPOT, eq. (1.6) (Section 1.3, p. 6), verbatim:

> "The constant A is determined by how well we can control sums over prime
> pairs; more precisely, it is the best constant so that for all distinct
> h, h' in H we can show the bound
> (1.6)  sum_{N < n <= 2N, n == b (W)} 1_P(n + h) 1_P(n + h')
>          ( sum_{d_1,...,d_K : d_i | n + h_i} lambda_{d_1,...,d_K} )^2
>          <= (A + o(1)) X,
> where X is the expected main term and lambda_{d_1,...,d_K} are sieve
> weights of Maynard-Tao type supported on d_1 ... d_K <= N^delta for some
> small delta > 0. In [2, Section 4], Selberg's upper bound sieve is used to
> show this for A = 4. We improve this to A = 3.99 by using Chen's sieve
> [4], [13] (cf. Proposition 12 below)."

Why A < 4 suffices - the block/pigeonhole bookkeeping (p. 6), verbatim:

> "The reason why this small improvement is sufficient is as follows: we
> choose a = 100 so that ceil(3.99a) + 1 = 4a, and partition our tuple
>   H = H_1 cup H_2 cup H_3 cup H_4,   H_i = union_{j=1}^{a} H_{ij},
>   i in {1, 2, 3, 4}.
> Then we find N < n <= 2N with n == b (W) such that for at least a + 1
> distinct (i, j) the set n + H_{ij} contains a prime number. Thus, by the
> pigeon-hole principle we must have at least two indices i != i' such that
> both n + H_i, n + H_{i'} contain primes. By the restriction n == b (W)
> given by the modified Erdos-Rankin construction, we then know that there
> are two consecutive primes, one in n + H_i and one in n + H_{i'}, for
> some i != i'. For beta_1 <= beta_2 <= beta_3 <= beta_4 as in Theorem 1,
> it is then enough to choose H_i so that for all h in H_i we have
> h = (beta_i + o(1)) log N. From this argument we see that the exact
> numerical value of A = 3.99 is not important, what matters is that A is
> strictly less than 4."

Roadmap sentence (p. 6), verbatim:

> "To show the bound (1.6) with A = 3.99, we require a Bombieri-Vinogradov
> type equidistribution result for primes, where the moduli run over some
> multiples of W < N^epsilon. The possibility of exceptional zeros of
> L-functions causes some technical problems, but the result [2, Theorem
> 4.2] turns out to be sufficient. Since we are using Chen's sieve, we also
> need to extend this to almost-primes; this is done in Section 2. In
> Section 3 we apply Chen's sieve to obtain the required bound (1.6) for
> prime pairs (Proposition 12). We then state and prove in Section 4 the
> precise version of the Maynard-Tao sieve which we will use (Proposition
> 18), and in Section 5 we prove our main result Theorem 1."

Remark 2 - thresholds and the parity obstruction (Section 1.3, p. 6),
verbatim:

> "Remark 2. By the same argument, if we could show the bound (1.6) with
> any constant A < 3 in place of 3.99, we would obtain Theorem 1 with
> sequence of four real numbers replaced by three. This in turn would give
> that mu(L cap [0, T]) >= T/2. Similarly, if we had (1.6) with any
> constant A < 2 in place of 3.99, we could show that L = [0, infty], which
> is the conjecture of Erdos. However, by the parity principle this should
> be just as hard as obtaining a lower bound for such a sum over prime
> pairs, which would immediately imply L = [0, infty] (cf. [7, Chapter 16]
> for a quantitative version due to Bombieri of the parity principle)."

Acknowledgements (p. 7) name supervisor Kaisa Matomaki, Emmanuel Kowalski,
ETH Zurich, James Maynard ("for bringing the article [2] to my attention"),
Pavel Zorin-Kranich, the referee; Magnus Ehrnrooth Foundation grant.

---

## 4. EQUIDISTRIBUTION INPUTS (Section 2): MODIFIED BOMBIERI-VINOGRADOV

Opening (Section 2, p. 7), verbatim:

> "As was outlined above, we need to show an upper bound of type (1.6) for
> prime pairs, where the modulus W can be as large as N^epsilon. For this
> purpose we require a modified version of the Bombieri-Vinogradov Theorem.
> Before stating this we need the following lemma on exceptional zeros of
> Dirichlet L-functions (this is [2, Lemma 4.1]):"

Lemma 7 (Section 2, p. 7), verbatim:

> "Lemma 7. Let T >= 3 and P >= T^{1/log_2 T}. For a sufficiently small
> constant c > 0, there is at most one modulus q <= T with P^+(q) <= P and
> one primitive character chi modulo q such that the function L(s, chi) has
> a zero in the region
>   Re(s) >= 1 - c/log P,   |Im(s)| <= exp( log P / sqrt(log T) ).
> If such a character chi mod q exists, then it is real, L(s, chi) has at
> most one zero in the above region, which is then real and simple, and
>   P^+(q) >> log q >> log_2 T."

Exceptional-modulus marker (2.1) (p. 7), verbatim: "Z_T = P^+(q)", "and we
set Z_T = 1 if no such modulus exists."

Proposition 8 (Section 2, pp. 7-8), verbatim:

> "Proposition 8. (Modified Bombieri-Vinogradov). Let N > 2 and fix
> constants C > 0, epsilon > 0, and delta > 0. Let q_0 < N^epsilon be a
> square-free integer with P^+(q_0) < N^{epsilon/log_2 N}. Then for epsilon
> small enough we have
>   sum_{q <= N^{1/2 - delta}, q_0 | q, (q, Z_{N^{2 epsilon}}) = 1}
>     max_{(a,q)=1} | sum_{n <= N, n == a (q)} Lambda(n)
>       - (1/phi(q)) sum_{n <= N} Lambda(n) |
>   <<_{delta,C}  N / (phi(q_0) log^C N)."

(The paper states this "is [2, Theorem 4.2]", p. 7.)

Lemma 9 (Section 2, p. 8), verbatim:

> "Lemma 9. With the same notations and assumptions as in Proposition 8 we
> have
> (2.2)  sup_{A,B : AB <= N^{1/2-delta}, A <= q_0}
>          sum_{A < a <= 2A, a | q_0}
>          sum_{B <= b <= 2B, (b, q_0 Z_{N^{2 epsilon}}) = 1} (1/phi(b))
>          sum'_{chi (ab)} | sum_{n <= N} Lambda(n) chi(n) |
>          <<_C  N / log^C N,
> where sum' denotes the sum over primitive characters modulo ab."

[TRANSCRIPTION-UNSURE: the stacked conditions under the sup/sums in (2.2)
are small; read as "A, B with AB <= N^{1/2-delta}, A <= q_0" and inner
ranges "A < a <= 2A, a|q_0" and "B <= b <= 2B, (b, q_0 Z_{N^{2epsilon}}) =
1".] Provenance sentence (p. 8, verbatim): "From the proof of [2, Theorem
4.2] we obtain the following lemma, which we require for the proof of
Proposition 11 below".

Lemma 10 (Section 2, p. 8), verbatim:

> "Lemma 10. (Large sieve for multiplicative characters). For any sequence
> c_n of complex numbers and for any M, N >= 1 we have
>   sum_{q <= Q} (q/phi(q)) sum'_{chi (q)}
>     | sum_{M < n <= M+N} c_n chi(n) |^2  <=  (Q^2 + N) sum_n |c_n|^2."

(Source cited: "the large sieve for multiplicative characters, which
follows from Theorem 9.10 of [7]", p. 8.)

Almost-prime setup (Section 2, p. 8), verbatim:

> "To state the equidistribution result for almost-primes, we need to set
> up some notation: fix 0 < alpha < 1/2, and let N^alpha << A_1 <<
> N^{1-alpha}, for sufficiently large N. Define
> (2.3)  Lambda_0(n) := (f * g)(n),
> where f(m) = 1_P(m)(log m) 1_{m <= A_1}, and g is any function such that
> |g(n)| << 1, and g(n) != 0 only if P^-(n) >= N^alpha and n asymp N/A_1.
> Note that then Lambda_0(n) is supported on almost-primes n << N."

Proposition 11 (Section 2, p. 8), verbatim:

> "Proposition 11. (Modified Bombieri-Vinogradov for almost-primes). Let
> N > 2 and fix constants C > 0, epsilon > 0, and delta > 0. Let
> q_0 < N^epsilon be a square-free integer with P^+(q_0) <
> N^{epsilon/log_2 N}. Let Lambda_0(n) be as in (2.3). Then for all small
> enough epsilon we have
>   sum_{q <= N^{1/2-delta}, q_0 | q, (q, Z_{N^{2 epsilon}}) = 1}
>     max_{(a,q)=1} | sum_{n == a (q)} Lambda_0(n)
>       - (1/phi(q)) sum_n Lambda_0(n) |
>   <<_{delta,C}  N / (phi(q_0) log^C N)."

Proof anatomy (pp. 8-12, PARAPHRASE): expand into characters; replace chi
by the inducing primitive chi' mod q'; split (2.5)-(2.6) by the coprimality
corrections h_1 = 1, h_2(n,d) = 1_{(n,d)>1}; the cases i = 2 or j = 2 are
handled by dyadic decomposition, Cauchy-Schwarz and Lemma 10 giving
<< N^{1 - alpha/3} (p. 10); the main case i = j = 1 (2.8) extracts the
factor 1/phi(q_0) exactly as in [2, Theorem 4.2] (p. 10), then for
B >= N^epsilon uses Cauchy-Schwarz + Lemma 10 (<< N^{1-epsilon}, p. 11),
and for B < N^epsilon replaces f(m) by Lambda(m) 1_{m <= A_1} (error
<< N^{1-alpha/3}) and applies Lemma 9 with A_1 in place of N (using
AB < N^{2 epsilon} < A_1^{1/2-delta}), eq. (2.9) and following displays
(pp. 11-12), ending <<_C N/log^{C+5} N.

---

## 5. CHEN'S SIEVE UPPER BOUND FOR PRIME PAIRS (Section 3) - THE
SUBSTITUTION SPOT

Section opening (Section 3, p. 12), verbatim:

> "In this section we will apply Chen's sieve to obtain an upper bound for
> prime pairs, which is 3.99 times the expected main term. As will become
> apparent in the next section, the exact numerical value of this constant
> does not matter, only that it is stricly less than four. To state the
> result, we first need to set up some notation from [2]."

[TRANSCRIPTION-UNSURE: "stricly" appears as printed (typo for "strictly").]

Maynard-Tao weight setup (Section 3, p. 12), verbatim:

> "(3.1)  lambda_{d_1,...,d_K} =
>   { ( prod_{i=1}^K mu(d_i) ) sum_{j=1}^J prod_{l=1}^K
>       F_{l,j}( log d_l / log N ),   if (d_1 ... d_K, Z_{N^{4 epsilon}}) = 1,
>   { 0,                              otherwise,
> for some fixed J, where F_{l,j} : [0, infty) -> R are smooth compactly
> supported functions, not identically zero, satisfying a support condition
> (3.2)  sup { sum_{l=1}^K t_l : prod_{l=1}^K F_{l,j}(t_l) != 0 } <= delta
> for all j = 1, 2, ..., J for some small delta > 0. Note that this implies
> that lambda_{d_1,...,d_K} are supported on d_1 ... d_K <= N^delta."

F(t_1,...,t_K) := sum_{j=1}^J prod_{l=1}^K F'_{l,j}(t_l), and (3.3)
L_K(F) := int...int ( int int F(t_1,...,t_K) dt_{K-1} dt_K )^2
dt_1...dt_{K-2} (p. 12; also given as the explicit double sum over j, j'
of F_{K-1,j}(0)F_{K-1,j'}(0)F_{K,j}(0)F_{K,j'}(0) times products of
int F'_{l,j} F'_{l,j'}). Normalizers (p. 12):

> "W := prod_{p <= epsilon log N, p not| Z_{N^{4 epsilon}}} p,
>  B := (phi(W)/W) log N."

The substitution sentence (Section 3, p. 12 bottom), verbatim:

> "Using the above notation, we have that [2, Lemma 4.6 (iii)] holds with
> the constant 4 replaced by 3.99 :"

Proposition 12 (Section 3, p. 13), verbatim:

> "Proposition 12. For all sufficiently large N the following holds:
> Let H = {h_1, ..., h_K} subseteq [0, N] be an admissible K-tuple such
> that
> (3.4)  P^+( prod_{1 <= i < j <= K} (h_j - h_i) ) <= epsilon log N.
> Let b be an integer such that
>   ( prod_{j=1}^K (b + h_j), W ) = 1.
> Then for all distinct h_j, h_l in H we have
>   S := sum_{N < n <= 2N, n == b (W)} 1_P(n + h_j) 1_P(n + h_l)
>          ( sum_{d_1,...,d_K : d_i | n + h_i} lambda_{d_1,...,d_K} )^2
>        <= (3.99 + O(delta)) (N/W) B^{-K} L_K(F)."

THE EXACT SELBERG -> CHEN SWITCH (p. 13, directly after Proposition 12),
verbatim:

> "The proof in [2, Lemma 4.6 (iii)] uses Selberg's sieve combined with the
> Modified Bombieri-Vinogradov Theorem. Our improvement comes from using
> Chen's sieve instead of Selberg's sieve. Similarly as in [2, Lemma 4.6
> (iii)], we first note that we may replace
>   ( sum_{d_1,...,d_K : d_i | n + h_i} lambda_{d_1,...,d_K} )^2   by
>   nu_{H,j,l}(n) := ( sum_{d_1,...,d_K : d_i | n + h_i, d_j = d_l = 1}
>     lambda_{d_1,...,d_K} )^2 1_{((n+h_j)(n+h_l), Z_{N^{4 epsilon}}) = 1}
> in the sum S."

Chen-inequality provenance (p. 13), verbatim:

> "We then require the following weighted sieve inequality of Chen type
> (this is essentially Lemma 4.1 of [20], which is in there attributed to
> Chen [4]; according to Wu, the idea that this simple sieve inequality is
> sufficient is due to Pan [13])."

Lemma 13 (Section 3, p. 13), verbatim:

> "Lemma 13. Let 0 < alpha < beta < 1/4, Y := N^alpha, and Z := N^beta.
> Then S <= S_1 - S_2/2 + S_3/2, where
>   S_1 := sum_{N < n <= 2N, n == b (W)} 1_P(n + h_j)
>            1_{(n + h_l, P(Y)) = 1} nu_{H,j,l}(n)
>   S_2 := sum_{Y < p <= Z} sum_{N < n <= 2N, n == b (W), p | n + h_l}
>            1_P(n + h_j) 1_{(n + h_l, P(Y)) = 1} nu_{H,j,l}(n),   and
>   S_3 := sum_{N < n <= 2N, n == b (W)} 1_P(n + h_j)
>            sum_{Y < p < q < r <= Z} sum_{(s, P(q)) = 1}
>            1_{n + h_l = pqrs} nu_{H,j,l}(n)."

Proof identity (3.5) (p. 13), verbatim:

> "(3.5)  1_{(n, P(Z)) = 1} <= 1_{(n, P(Y)) = 1}
>   - (1/2) sum_{Y < p <= Z} 1_{p|n} 1_{(n, P(Y)) = 1}
>   + (1/2) sum_{Y < p < q < r <= Z} sum_{(s, P(q)) = 1} 1_{n = pqrs}."

with the combinatorial check (pp. 13-14, verbatim): "For (n, P(Y)) > 1 this
is obvious, so let (n, P(Y)) = 1 and denote k = sum_{Y < p <= Z} 1_{p|n}.
If k = 0, then both sides of (3.5) are equal to one. For k >= 1 the
left-hand side is zero. If k = 1, then the right-hand side is 1 - 1/2 + 0 =
1/2 > 0. For k >= 2 the right-hand side is 1 - k/2 + (k - 2)/2 = 0, since
in the last sum p and q are fixed and there are k - 2 ways to choose r."

Remark 3 (p. 14), verbatim:

> "Remark 3. Note that beta < 1/4 implies that in the sum S_3 we have
> s >> N/(pqr) > N^{1/4} > q. The above lemma holds also for beta >= 1/4,
> but then we sometimes may have s = 1 in the sum S_3."

Linear sieve functions (p. 14): F_lin, f_lin defined by the
delay-differential system (sF_lin(s))' = f_lin(s-1), (sf_lin(s))' =
F_lin(s-1) with sF_lin(s) = 2e^gamma for 1 <= s <= 3, sf_lin(s) = 0 for
s <= 2; recorded value (verbatim): "for 2 <= s <= 4  f_lin(s) =
2e^gamma log(s-1)/s." Lemma 14 (Linear sieve, p. 14, from "[7, Chapters 11
and 12]"), conclusion verbatim:

> "sum_n a_n 1_{(n, P(z)) = 1} <= (F_lin(s) + O(log^{-1/6} D)) X
>    prod_{p <= z} (1 - g(p)) + sum_{d <= D, d squarefree} |r_d|,
>  sum_n a_n 1_{(n, P(z)) = 1} >= (f_lin(s) - O(log^{-1/6} D)) X
>    prod_{p <= z} (1 - g(p)) - sum_{d <= D, d squarefree} |r_d|."

(hypotheses: g multiplicative, 0 <= g(p) < 1, level D >= 2, z = D^{1/s},
s >= 1, one-sided density condition prod_{w <= p < z} (1 - g(p))^{-1} <=
(log z/log w)(1 + L/log w).)

Lemma 15 (Section 3, p. 15), verbatim:

> "Lemma 15. We have
>   S_1 <= (F_lin(1/(2 alpha)) + O(delta)) / (alpha e^gamma)
>          (N/W) B^{-K} L_K(F)"

Proof interface (3.6)-(3.7) (p. 15): g(p) := 1/(p-1) if p not| W
Z_{N^{4 epsilon}}, 0 if p | W Z_{N^{4 epsilon}}; and (verbatim):

> "(3.7)  sum_{N < n <= 2N} 1_P(n + h_j) 1_{n == b (W)} nu_{H,j,l}(n)
>   = (1 + o(1)) (N/(phi(W) log N)) B^{-K+2} L_K(F)
>   = (1 + o(1)) (N/W) B^{-K+1} L_K(F)."

> "(to show this we just expand the square in nu_{H,j,l}(n), swap the order
> of summation, and use the Proposition 8 with moduli
> [d_1, d_1'] ... [d_K, d_K'] W <= N^{3 delta} similarly as in [2, Lemma
> 4.6]). Hence, by the upper bound of the linear sieve (Lemma 14 with level
> of distribution D = N^{1/2 - 4 delta}, sifting up to Y = N^alpha) we get"

then Mertens (p. 15): prod_{p <= Y} (1 - g(p)) = (1 + o(1))
W/(phi(W) e^gamma log Y). Error-term control (pp. 16-17): with E(N, q) :=
max_{(a,q)=1} | pi(2N + h_j; q, a) - pi(N + h_j; q, a) - (pi(2N + h_j) -
pi(N + h_j))/phi(q) | for (q, Z_{N^{4 epsilon}}) = 1 (set = 0 otherwise),
Cauchy-Schwarz and Proposition 8 give (p. 17, verbatim conclusion):
"sum_{q <= N^{1/2-2 delta}, (q, W Z_{N^{4 epsilon}}) = 1} tau_{3K}(q)
E(N, qW) ... <<_{K,C} N/(W log^C N), which is sufficient."

Lemma 16 (Section 3, p. 17), verbatim:

> "Lemma 16. We have
>   S_2 >= ((1 - O(delta))/(alpha e^gamma))
>          int_alpha^beta f_lin( (1/2 - t)/alpha ) (dt/t)
>          (N/W) B^{-K} L_K(F)."

Proof (pp. 17-18): S_2 = sum_{Y < p <= Z} S_{2,p}; lower bound of the
linear sieve applied to each S_{2,p} with "level of distribution
D = N^{1/2-4 delta}/p and shifting up to Y = N^alpha"
[TRANSCRIPTION-UNSURE: "shifting" as printed, presumably "sifting"];
summing over p and passing to the integral by z = N^t (p. 18, verbatim
final display chain):

> "S_2 >= ((1 - O(delta))/(alpha e^gamma)) ( sum_{Y < p <= Z} (1/p)
>   f_lin( log N^{1/2}/p / log Y ) ) (N/W) B^{-K} L_K(F)
>   >= ((1 - O(delta))/(alpha e^gamma)) ( int_{Y < z <= Z}
>   f_lin( (log N^{1/2}/z) / log Y ) dz/(z log z) ) (N/W) B^{-K} L_K(F)
>   >= ((1 - O(delta))/(alpha e^gamma)) int_alpha^beta
>   f_lin( (1/2 - t)/alpha ) (dt/t) (N/W) B^{-K} L_K(F)"

Buchstab input (p. 18), verbatim:

> "For the next Lemma we need the Buchstab function, defined as the
> continuous solution to the delay-differential equation
>   s omega(s) = 1, if 1 <= s <= 2,   (s omega(s))' = omega(s - 1), if
>   s > 2.
> Then by [7, Lemma 12.1] for any N^epsilon < z < N we have
> (3.8)  sum_{N < n <= 2N} 1_{(n, P(z)) = 1} = (1 + o(1))
>          omega(log N / log z) N/log z,   N -> infty."

Lemma 17 (Section 3, p. 18), verbatim:

> "Lemma 17. We have
>   S_3 <= (4 + O(delta)) int_{alpha < u_1 < u_2 < u_3 < beta}
>          omega( (1 - u_1 - u_2 - u_3)/u_2 )
>          (du_1 du_2 du_3 / (u_1 u_2^2 u_3)) (N/W) B^{-K} L_K(F)."

The switching step (p. 18), verbatim:

> "Proof. Here we apply the switching, to sieve out the prime divisors of
> n + h_j rather than n + h_l; define
>   a_n := sum_{Y < p < q < r <= Z} sum_{(s, P(q)) = 1} 1_{n = pqrs}
> so that
>   S_3 = sum_{N < n <= 2N, n == b (W)} 1_P(n + h_j) a_{n + h_l}
>         nu_{H,j,l}(n).
> We use a similar Selberg upper bound sieve as in [2, Lemma 4.6] (we could
> just as well use the linear sieve upper bound as in the above but the
> argument is slightly simpler this way); let G : [0, infty) -> R be a
> smooth function supported on [0, 1/4 - 2 delta] with G(0) = 1."

Then (p. 19, verbatim): "By essentially the same argument as in the proof
of [2, Lemma 4.6 (iii)], choosing the function G optimally gives
(3.9)  S_3 <= (4 + O(delta)) (log N / N) ( sum_{N < n <= 2N} a_n )
(N/W) B^{-K} L_K(F) + O(R)," with R an error sum over E_0(N, [d_1,d_1']...
[d_K,d_K'][e,e']W), E_0(N, d) := max_{(a,d)=1} | sum_{N+h_l < n <= 2N+h_l,
n == a (d)} a_n - (1/phi(d)) sum a_n |, e, e' <= N^{1/4-2 delta} from the
support of G. The error is reduced (pp. 19-20) to
"sum_{d <= N^{1/2-2 delta}, (d, W Z_{N^{4 epsilon}}) = 1} |E_0(N, dW)|
<<_C N/(W log^C N)", shown via finer-than-dyadic decomposition (3.10),
(3.11) (removing cross-conditions Y < p < q, intervals I_j = (A_j,
lambda A_j], lambda = 1 + log^{-2C} N), replacement of P(m) = 1_P(m)
1_{m in (A_1, lambda A_1]} by f(m)/log A_1 with f(m) := P(m) log m, and
finally (p. 20, verbatim): "we obtain by Proposition 11 that
sum_{d <= N^{1/2-2 delta}, (d, W Z_{N^{4 epsilon}}) = 1} |E_0(N, dW)| <<_C
N/(W log^C N), which suffices by the previous remarks to bound the error
term R in (3.9)."

Main term of S_3 (p. 21, verbatim final display of the Lemma 17 proof):

> "sum_{N < n <= 2N} a_n = ... = (1 + o(1)) (N/log N)
>   int_{alpha < u_1 < u_2 < u_3 < beta}
>   omega( (1 - u_1 - u_2 - u_3)/u_2 ) du_1 du_2 du_3 / (u_1 u_2^2 u_3)
> after the change of variables z_j = N^{u_j}."

PROOF OF PROPOSITION 12 - THE NUMERICS (Section 3, p. 21), verbatim:

> "Proof of Proposition 12. Combining Lemmata 13, 15, 16 and 17 we obtain
>   S <= (Omega_1 - Omega_2 + Omega_3 + O(delta)) (N/W) B^{-K} L_K(F),
> where
>   Omega_1 = F_lin(1/(2 alpha)) / (alpha e^gamma),
>   Omega_2 = (1/(2 alpha e^gamma)) int_alpha^beta
>             f_lin( (1/2 - t)/alpha ) (dt/t),   and
>   Omega_3 = 2 int_{alpha < u_1 < u_2 < u_3 < beta}
>             omega( (1 - u_1 - u_2 - u_3)/u_2 )
>             du_1 du_2 du_3 / (u_1 u_2^2 u_3).
> We choose alpha = 1/7 and beta = 3/14 (so that (1/2 - t)/alpha >= 2 in
> the integral defining Omega_2). For this choice we get
>   Omega_1 = 7 F_lin(7/2) / e^gamma
>     = 2 ( 3 F_lin(3)/e^gamma + int_3^{7/2} f_lin(s - 1)/e^gamma ds )
>     = 4 + 4 int_3^{7/2} ( log(s - 2)/(s - 1) ) ds  <=  4.19,
>   Omega_2 = (7/(2 e^gamma)) int_{1/7}^{3/14} f_lin(7/2 - 7t) (dt/t)
>     = 7 int_{1/7}^{3/14} ( log(7/2 - 7t - 1) / (7/2 - 7t) ) (dt/t)
>     >=  0.279,
> and
>   Omega_3 = 2 int_{1/7 < u_1 < u_2 < u_3 < 3/14}
>     omega( (1 - u_1 - u_2 - u_3)/u_2 ) du_1 du_2 du_3 / (u_1 u_2^2 u_3)
>     <=  0.076.
> Hence, Omega_1 - Omega_2 + Omega_3 < 3.99."

Remark 4 (p. 21), verbatim:

> "Remark 4. The upper bound for the integral in Omega_3 was computed using
> Python 7.3; the code is available at http://codepad.org/2emT1dHN. The
> choice of exponents alpha = 1/7 and beta = 3/14 has not been optimized
> since this is not relevant to our application."

[TRANSCRIPTION-UNSURE: "Python 7.3" as printed (presumably a typo for a
Python 2.7.3-type version string).]

---

## 6. MODIFIED MAYNARD-TAO SIEVE (Section 4): BLOCK BOOKKEEPING

Proposition 18 (Section 4, p. 22), verbatim:

> "Proposition 18. (Modified Maynard-Tao sieve). Let K be a sufficiently
> large multiple of 4. Let epsilon > 0 be sufficiently small. Then for all
> sufficiently large N the following holds:
> Let Z_{N^{4 epsilon}} be as in (2.1) and define
>   W := prod_{p <= epsilon log N, p not| Z_{N^{4 epsilon}}} p;
> Let H = {h_1, ..., h_K} subseteq [0, N] be an admissible K-tuple such
> that
>   P^+( prod_{1 <= i < j <= K} (h_j - h_i) ) <= epsilon log N
> Let b be an integer such that
>   ( prod_{j=1}^K (b + h_j), W ) = 1.
> Let
>   H = H_1 cup H_2 cup H_3 cup H_4
> be a partition of H into four sets of equal size. Then there is an
> integer n in [N, 2N] with n == b (W) such that n + H_i contains a prime
> number for at least two distinct indices i in {1, 2, 3, 4}."

Reduction sentence (p. 22, verbatim): "To prove the above proposition we
will show that it suffices to prove the following seemingly weaker"

Proposition 19 (Section 4, pp. 22-23), verbatim:

> "Proposition 19. Let a >= 1 be an integer and let K be a sufficiently
> large multiple of ceil(3.99a) + 1. Let epsilon > 0 be sufficiently small.
> Then for all sufficiently large N the following holds:
> Let Z_{N^{4 epsilon}} be as in (2.1) and define
>   W := prod_{p <= epsilon log N, p not| Z_{N^{4 epsilon}}} p.
> Let H = {h_1, ..., h_K} subseteq [0, N] be an admissible K-tuple such
> that
>   P^+( prod_{1 <= i < j <= K} (h_j - h_i) ) <= epsilon log N
> Let b be an integer such that
>   ( prod_{j=1}^K (b + h_j), W ) = 1.
> Let
>   H = H_1 cup H_2 cup ... cup H_{ceil(3.99a)+1}
> be a partition of H into ceil(3.99a) + 1 sets of equal size. Then there
> is an integer n in [N, 2N] with n == b (W) and a set of a + 1 distinct
> indices {j_1, j_2, ..., j_{a+1}} subseteq {1, 2, ..., ceil(3.99a) + 1}
> such that n + H_j contains a prime number for every
> j in {j_1, j_2, ..., j_{a+1}}."

Proof of Proposition 18 using Proposition 19 (p. 23), verbatim:

> "We take a = 100 so that ceil(3.99a) + 1 = 4a. By taking a larger K if
> necessary, we may suppose that K is sufficiently large multiple of 4a.
> Given a partition H = H_1 cup H_2 cup H_3 cup H_4 as in Proposition 18,
> we take a further partition
>   H_i = H_{i1} cup H_{i2} cup ... cup H_{ia}
> into sets of equal sizes for all i in {1, 2, 3, 4}. Then by Proposition
> 19 there is an integer n in [N, 2N] with n == b (W) so that for at least
> a + 1 distinct sets H_{ij} the set n + H_{ij} contains a prime number. By
> the pigeon-hole principle this implies that n + H_i contains a prime
> number for at least two distinct indices i in {1, 2, 3, 4}."

Proof of Proposition 19 (pp. 23-24) - the Pintz-refined positive-linear-
combination device. Setup (p. 23), verbatim:

> "We use Pintz's refined version of the argument in [2] (cf. proof of [14,
> Theorem 3] and especially [1, Theorem 5.4]): using the notations of [1],
> let us denote M := ceil(3.99a) + 1, and let mu, mu' be positive real
> numbers with (defining binom(1,2) = 0)
> (4.1)  mu' = max_{v in N} ( v - mu binom(v, 2) ).
> For any integer n consider
> (4.2)  sum_{j=1}^M ( sum_{h in H_j} 1_P(n + h)
>          - mu sum_{{h,h'} subseteq H_j, h != h'}
>            1_P(n + h) 1_P(n + h') ).
> If there are at most a indices j such that n + H_j contains a prime, then
> the sum (4.2) is at most mu' a."

and (p. 23, verbatim): "Therefore, the proposition follows once we show
that

> sum_{N < n <= 2N, n == b (W)} ( sum_{h in H} 1_P(n + h) - mu' a
>   - mu sum_{j=1}^M sum_{{h,h'} subseteq H_j, h != h'}
>     1_P(n + h) 1_P(n + h') )
>   ( sum_{d_1,...,d_K : d_i | n + h_i} lambda_{d_1,...,d_K} )^2  >  0."

Evaluation (p. 23, verbatim): "Let Sigma denote the above sum. Using [2,
Lemma 4.6 (i),(ii)] to evaluate the first two sums, and Proposition 12 to
bound the third, we obtain that Sigma is bounded from below by

> (1 + O(delta)) (N/(W B^K)) ( K J_K(F) - mu' a I_K(F)
>   - 3.99 mu M binom(K/M, 2) L_K(F) ),"

where (p. 24) I_K(F), J_K(F), L_K(F) are the integrals in [2, Lemma 4.6]
(L_K same as (3.3)). By [2, Lemma 4.7], for any rho in (0,1) there is F
with (p. 24, verbatim):

> "J_K(F) >= (1 + O(log^{-1/2} K)) (rho delta log K / K) I_K(F),
>  L_K(F) <= (1 + O(log^{-1/2} K)) ( rho delta log K / K )^2 I_K(F)."

Hence (4.3): Sigma >= S (1 + O(delta)) N W^{-1} B^{-K} I_K(F) with
(p. 24, verbatim):

> "S := rho delta log K - mu' a
>       - 3.99 mu M binom(K/M, 2) ( rho delta log K / K )^2,
> if we pick K large enough so that log^{-1/2} K < delta. Choosing
> mu = 1/L for some positive integer L we observe that mu' = (1 + L)/2,
> the maximum (4.1) being obtained at v = L and v = 1 + L. Define the
> quantity X by XM := rho delta log K. Then by using 3.99 <= (M - 1)/a we
> obtain
>   S = XM - ((1 + L)/2) a - 3.99 (M/L) binom(K/M, 2) (XM/K)^2
>     >= XM - ((1 + L)/2) a - ((M - 1)/a)(M/L)(K^2/(2M^2))(XM/K)^2
>     = XM - ((1 + L)/2) a - ((M - 1)/a)(X^2 M / (2L))
>     = a/(2(M - 1)) > 0,
> for X = aL/(M - 1) and L = M, requiring that K is large enough so that
> rho < 1 for this choice of X."

(The place where the Chen constant enters the bookkeeping is exactly the
"3.99 mu M binom(K/M,2) L_K(F)" term and the inequality
"3.99 <= (M - 1)/a"; with M = ceil(3.99a) + 1 this is what forces the
choice M - 1 = ceil(3.99a), i.e. one fewer block per unit reduction
below 4. PARAPHRASE of the mechanism visible in the displays above.)

---

## 7. PROOF OF THEOREM 1 (Section 5): ERDOS-RANKIN CLEARING AND THE
FOUR-VALUE MENU

Section opening (Section 5, p. 24), verbatim:

> "Theorem 1 now follows by the same argument as in [2, Section 6], using
> our Proposition 18 in place of [2, Theorem 4.3]; for this we need the
> modified Erdos-Rankin construction given by [2, Lemma 5.2] which states:"

Lemma 20 (Section 5, pp. 24-25), verbatim:

> "Lemma 20. Let K >= 1 and beta_K >= beta_{K-1} >= ... >= beta_1 >= 0.
> Then there is a real number y(beta, K) such that the following holds:
> Let x, y, z be any real numbers such that x >= 1, y >= y(beta, K), and
>   2y(1 + (1 + beta_K)x) <= 2z <= y (log_2 y)(log_3 y)^{-1}.
> Let Z be any (possibly empty) set of primes such that for any q in Z we
> have
>   sum_{p in Z, p >= q} 1/p << 1/q << 1/log z.
> Then there is a set of integers {a_p : p <= y, p not in Z} and an
> admissible K-tuple {h_1, h_2, ..., h_K} such that
>   {h_1, h_2, ..., h_K} = ((0, z] cap Z') \ union_{p <= y, p not in Z}
>     {m : m == a_p (p)},
>   P^+( prod_{1 <= i < j <= K} (h_j - h_i) ) <= y,
> and for all i = 1, 2, ..., K
>   h_i = beta_i x y + y + O( y e^{-log^{1/4} y} )."

[TRANSCRIPTION-UNSURE: in the displayed set equation the paper writes
"((0, z] cap Z)" with blackboard-bold Z = the integers; transcribed here
as Z' to avoid clash with the exceptional-prime set Z of the same lemma.
The two are typographically distinct in the PDF (blackboard bold vs
calligraphic).]

Application parameters (Section 5, p. 25), verbatim:

> "Given beta_1 <= beta_2 <= beta_3 <= beta_4 as in Theorem 1 and any
> sufficiently large N, we will apply the above lemma with
>   x := 1/epsilon,   y := epsilon log N,
>   z := y (log_2 y)(2 log_3 y)^{-1},
>   beta := {beta_1, ..., beta_1, beta_2, ..., beta_2, beta_3, ...,
>            beta_3, beta_4, ..., beta_4},
> where epsilon > 0 is sufficiently small and each beta_i is repeated K/4
> times for some sufficiently large K == 0 (4); by translation we may
> assume beta_1 >= 0. We let Z := {Z_{N^{4 epsilon}}} if
> Z_{N^{4 epsilon}} > 1, and Z = emptyset otherwise (recall (2.1) for the
> definition of Z_T)."

yielding (5.1) (p. 25): H = ((0, z] cap Z') \ union_{p <= epsilon log N,
p != Z_{N^{4 epsilon}}} {m : m == a_p (p)}, with P^+(prod (h_j - h_i)) <=
epsilon log N, and (verbatim):

> "such that there is a partition H = H_1 cup H_2 cup H_3 cup H_4 into
> sets of equal sizes so that for all i = 1, 2, 3, 4 and for all h in H_i
>   h = (beta_i + epsilon + o(1)) log N."

Endgame (p. 25), verbatim:

> "Let b be an integer satisfying
>   b == -a_p (p)   for all   p <= epsilon log N, p != Z_{N^{4 epsilon}}.
> Then the assumptions of Proposition 18 are satisfied, so that the
> proposition yields two indices 1 <= i < j <= 4 and an integer
> n in [N, 2N] with n == b (W) such that both n + H_i and n + H_j contain
> a prime number. Furthermore, since n == b (W), by (5.1) we have
>   P cap (n, n + z] subseteq n + H.
> Thus, for some 1 <= i < j <= 4, there are consecutive primes
> p, q in n + H such that
>   p = (beta_i + epsilon + o(1)) log N,   and
>   q = (beta_j + epsilon + o(1)) log N.
> Since this holds for all sufficiently large N, we obtain that for some
> 1 <= i < j <= 4 we have beta_j - beta_i in L."

---

## 8. SECTION 6 (v3 ERRATUM): CORRECTION TO LEMMATA 15 AND 16

Opening (Section 6, p. 26), verbatim:

> "The above text agrees with the published version of the article.
> Unfortunately there is a mistake in the proofs of Lemmata 15 and 16
> (thanks to Jacques Benatar for pointing this out to me). Namely, in the
> remainder r_d, if we write [display of r_d] then the first sum in the
> brackets is empty if (d, d_i) > 1 for some i but the second sum is not
> empty. Note that this problem does not happen in our argument for S_3 (or
> in the proof of [2, Lemma 6(iii)]) where the Selberg sieve is used,
> thanks to the fact that the Selberg sieve weights are readily of the same
> form as the Maynard-Tao sieve weights. That is, the linear sieve we have
> used is not immediately compatible with the Maynard-Tao sieve. In this
> section we explain how to fix this issue. As is so often the case, the
> fundamental lemma of the sieve comes to the rescue. The idea is to handle
> small prime factors with Selberg type sieve weights (in the spirit of the
> fundamental lemma of the sieve), so that in the linear sieve g(d) and r_d
> will be supported on numbers with no small prime factors so that the
> contribution from the part where (d, d_i) > 1 is negligible."

Second issue (p. 26), verbatim:

> "Yet another problem is caused by the possible prime Z_{N^{4 epsilon}}.
> This is not a problem for the upper bounds of S_1 and S_3 but for the
> lower bound S_2 we cannot simply ignore Z_{N^{4 epsilon}} as we have done
> above. This is resolved as follows. For any y > 1 we define
>   P_0(y) := prod_{p <= y, p not| Z_{N^{4 epsilon}}} p."

and (p. 26, verbatim): "We just have to note that the conclusion of Lemma
13 remains valid if we replace P(Y), P(Z), and P(q) respectively by
P_0(Y), P_0(Z), and P_0(q)."

Fix apparatus (pp. 26-28): y_1 := exp(log^{1/3} N), y_2 := N^{delta^2};
preliminary Selberg-type weights (p. 26, verbatim):

> "rho(n) := ( sum_{e | (n, P_0(y_1))} mu(e) G( log e / log N ) )^2,
> where G : [0, infty) -> [0, 1] is a smooth function supported on
> [0, 2 delta^2] and such that G(u) = 1 for u in [0, delta^2]."

Lemma 21 (p. 27), verbatim:

> "Lemma 21. With the above notations, we have
>   1_{(n, P_0(y_1)) = 1} = rho(n) + O( tau(n)^2 psi(n; y_1, y_2) )
> where psi(n; y_1, y_2) is the characteristic function of the set
>   { n : exists d | n, d in [y_2, y_1 y_2], d | P_0(y_1) }."

Lemma 22 (p. 27), verbatim:

> "Lemma 22. For any 2 <= z <= y we have
>   sum_{n ~ y, P^+(n) < z} 1 << y e^{-u/2},
> where u := log y / log z."

The modified sums (p. 28): S_1' and S_2' with the extra factor rho(n) and
sifting condition 1_{(n + h_l, P(y_1, Y)) = 1}, P(y_1, Y) :=
prod_{y_1 < p <= Y} p; error contribution E(N) controlled by Holder plus
Lemma 22: E(N) <<_C (log^{-C} N) N/W (p. 28). Key positivity remark
(p. 28, verbatim): "Notice here that crucially rho(n) >= 0, so that we can
still apply the linear sieve."

Lemma 23 (p. 28), verbatim:

> "Lemma 23. We have
>   S_1' <= (F_lin(1/(2 alpha)) + O(delta)) / (alpha e^gamma)
>           (N/W) B^{-K} L_K(F)"

with g now supported away from small primes (p. 28): g(p) := 1/(p - 1) if
p > y_1, 0 if p <= y_1; the (d, d_i) = c > y_1 contamination is bounded
trivially (p. 29) by << N log^{O(1)} N / (W y_1^{1/2}) <<_C N/(W log^C N).
New main-term evaluation (6.2) (p. 29, verbatim):

> "(6.2)  sum_{N < n <= 2N} 1_P(n + h_j) 1_{n == b (W)} rho(n)
>           nu_{H,j,l}(n)
>         = (1 + o(1)) prod_{epsilon log N < p <= y_1} (1 - 1/p)
>           (N/(phi(W) log N)) B^{-K+2} L_K(F),
> where the difference compared to (3.7) is the coefficient rho(n), which
> will result in the (expected) extra factor
> prod_{epsilon log N < p <= y_1} (1 - p^{-1}) on the right-hand side."

This requires Lemma 24 (p. 29), a generalization of [2, Lemma 4.5] (or
[16, Lemma 4.1], Polymath), applied with k = K - 2, verbatim statement:

> "Lemma 24. Let y_1 := exp(log^{1/3} N). Let F_0, ..., F_k, G_0, ..., G_k
> : [0, infty) -> R be fixed smooth compactly supported functions. Denote
> B := (log N) phi(W)/W  Then
>   sum'_{d_1,...,d_k, d_1',...,d_k', e, e' | P_0(y_1)}
>     ( mu(e) mu(e') / [e, e'] ) F_0( log e / log N ) G_0( log e' / log N )
>     prod_{j=1}^k ( mu(d_j) mu(d_j') / [d_j, d_j'] )
>       F_j( log d_j / log N ) G_j( log d_j' / log N )
>   = (c + o(1)) B^{-k} prod_{epsilon log N < p <= y_1} (1 - 1/p),
> where sum' denotes restriction that [e, e'], [d_1, d_1'], ...,
> [d_k, d_k'], Z_{N^{2 epsilon}} W are pairwise coprime, and
>   c = F_0(0) G_0(0) prod_{j=1}^k int F_j(t_j) G_j(t_j) dt_j.
> The same holds if [e, e'] and [d_j, d_j'] are replaced by phi([e, e'])
> and phi([d_j, d_j'])."

[TRANSCRIPTION-UNSURE: the exceptional-prime subscript in Lemma 24's
coprimality restriction reads Z_{N^{2 epsilon}} (elsewhere in Section 3 it
is Z_{N^{4 epsilon}}); transcribed as printed.]

Proof of Lemma 24 (p. 30, PARAPHRASE): contour/Fourier argument as in [16,
Lemma 4.1] with the extra local factor L(xi_0, xi_0') =
zeta_0(1 + (2 + i xi_0 + i xi_0')/log N) / ( zeta_0(1 + (1 + i xi_0)/log N)
zeta_0(1 + (1 + i xi_0')/log N) ), zeta_0(s) := prod_{epsilon log N < p <=
y_1} (1 - p^{-s})^{-1}; since |xi_j| <= sqrt(log N) and y_1 =
exp(log^{1/3} N), L(xi_0, xi_0') = (1 + o(1)) prod_{epsilon log N < p <=
y_1} (1 - 1/p) (p. 30, sighted display), and the rest is as in [16].
Section closes (p. 31) by rerunning the Lemma 15 computation for S_1':
the product prod_{y_1 < p <= Y} (1 - 1/(p-1)) times
prod_{epsilon log N < p <= y_1} (1 - 1/p) recombines to
prod_{p <= Y} (1 - 1/p) W/phi(W) "by Merten's theorem since Y = N^alpha",
recovering the SAME bound as Lemma 15 (final display, p. 31): S_1' <=
(F_lin(1/(2 alpha)) + O(delta))/(alpha e^gamma) (N/W) B^{-K} L_K(F).
The paper states the details for S_2' are the same (p. 28: "We now show
how to handle S_1', the details are the same for S_2'.").

---

## 9. REFERENCES AS PRINTED (pp. 31-32, abbreviated to id + role)

[1] Baker-Freiberg, Q. J. Math. 67(2):233-260, 2016 (larger
normalizations; Theorem 5.4 used in Prop 19 proof). [2] Banks-Freiberg-
Maynard, Proc. Lond. Math. Soc. (3) 113(4):515-539, 2016 (the base
argument; Theorem 1.1 = nine numbers; Lemmas 4.1, 4.5, 4.6, 4.7, 5.2,
Theorems 4.2, 4.3 all imported). [3] Bergelson-Furstenberg-Weiss 2006
(syndeticity proposition also proved there). [4] Chen, Sci. Sinica
21(6):701-739, 1978. [5] Erdos 1955. [6] Ford-Green-Konyagin-Maynard-Tao,
J. Amer. Math. Soc. 31(1):65-105, 2018. [7] Friedlander-Iwaniec, Opera de
cribro (linear sieve Ch. 11-12, Buchstab Lemma 12.1, large sieve Theorem
9.10, parity Ch. 16). [8] Gallagher, Mathematika 23(1):4-9, 1976.
[9] Goldston-Ledoan 2015. [10] Goldston-Pintz-Yildirim, Ann. of Math.
170(2):819-862, 2009. [11] Hildebrand-Maier, Proc. Amer. Math. Soc.
104(1):1-9, 1988. [12] Maynard, Ann. of Math. 181(1):383-413, 2015.
[13] Pan, Sci. Sinica 23(11):1368-1377, 1980. [14] Pintz, "A note on the
distribution of normalized prime gaps", arXiv:1510.04577 (five numbers,
1/4 - o(1)). [15] Pintz, Polignac numbers..., 2016. [16] Polymath, Res.
Math. Sci. 1:Art. 12, 83, 2014. [17] Ricci 1956. [18] Soundararajan 2007.
[19] Westzynthius 1931. [20] Wu, Acta Arith. 114(3):215-273, 2004
(Chen's double sieve; Lemma 4.1 = the paper's Lemma 13 source).
[21] Zhang, Ann. of Math. 179(3):1121-1174, 2014.

---

## COMMENTARY (assessment, NOT extraction)

Focus question 1 (main theorems / the T/3 constant). VERIFIED. The
project's note "at least T/3 of [0,T] are limit points" is exactly
Corollary 2 (p. 2): mu(L cap [0, T]) >= T/3 for ALL T > 0, clean constant
1/3, no o(1) - obtained from Theorem 1 (four numbers, six-element
difference menu) via the general covering Proposition 4 (p. 3) with k = 4:
T/(k - 1) = T/3. The weaker route via [2, Corollary 1.2] gives only
(1/3 - o(1))T with ineffective o(1) (p. 2). Note the abstract's "at least
1/3 of positive real numbers" is the density gloss of Corollary 2.

Focus question 2 (Chen-sieve substitution, for D1.d). LOCATED EXACTLY.
The pairwise upper-sieve spot is eq. (1.6) (p. 6): the sum over
N < n <= 2N, n == b (W) of 1_P(n+h) 1_P(n+h') weighted by the SQUARE of
Maynard-Tao sieve weights, bounded by (A + o(1)) X. Selberg's upper bound
sieve gives A = 4 ([2, Section 4], as stated on p. 6); Merikoski proves
A = 3.99 (Proposition 12, p. 13; announced p. 12 as "[2, Lemma 4.6 (iii)]
holds with the constant 4 replaced by 3.99"). The switch sentence is on
p. 13: "Our improvement comes from using Chen's sieve instead of Selberg's
sieve." The mechanism is the Chen/Pan/Wu weighted inequality Lemma 13
(p. 13): S <= S_1 - S_2/2 + S_3/2, with S_1 bounded by the linear sieve
upper bound (Lemma 15: Omega_1 = F_lin(1/(2 alpha))/(alpha e^gamma) <=
4.19 at alpha = 1/7), S_2 bounded BELOW by the linear sieve (Lemma 16:
Omega_2 >= 0.279), and the switched sum S_3 (sieving n + h_j instead of
n + h_l over n + h_l = pqrs) bounded by Selberg + Buchstab (Lemma 17:
Omega_3 <= 0.076), giving Omega_1 - Omega_2 + Omega_3 <= 4.19 - 0.279 +
0.076 = 3.987 < 3.99 (proof of Proposition 12, p. 21). So the best current
constant at this pairwise upper-sieve spot in THIS paper is 3.99 (really
<= 3.987 before rounding), with alpha = 1/7, beta = 3/14 explicitly NOT
optimized (Remark 4, p. 21). The equidistribution input needed for the
switched term is the new Proposition 11 (modified Bombieri-Vinogradov for
almost-prime convolutions f * g, p. 8). Thresholds (Remark 2, p. 6): any
A < 3 would yield three numbers and T/2; any A < 2 would yield
L = [0, infty] but "by the parity principle this should be just as hard as
obtaining a lower bound for such a sum over prime pairs". For D1.d intake:
the improvable window between 3.987 and the parity floor 2 is what this
line of work has to spend, at ~1 block per unit.

Focus question 3 (syndeticity). FOUND, VERBATIM. Corollary 3 (p. 2):
"There exists a constant C >= 0 such that for all T >= 0 we have
L cap [T, T + C] != emptyset", followed immediately by "Corollary 3 can be
rephrased as saying that the set of limit points L is syndetic" (p. 2).
The unverified secondary-source claim is thus CONFIRMED against the
primary text, with three caveats the project should carry: (a) the
syndetic set is L, the set of limit VALUES of g_n/log p_n in [0, infty] -
this says nothing about gaps between prime-gap SITES; (b) the constant C
is ineffective (stated in the bridge sentence p. 2 and in Proposition 5,
p. 4 - the proof is a compactness contradiction via Lemma 6); (c) the
paper itself notes syndeticity "actually follows already from [2, Theorem
1.1]" (p. 2) and is also in Bergelson-Furstenberg-Weiss [3] (p. 4), so it
is not specific to the 4-block improvement.

Focus question 4 (blocks bookkeeping, "9 -> 5/4"). VERIFIED as
9 -> 5 -> 4. Anchor (p. 2): "[2, Theorem 1.1] gives this for nine real
numbers in place of four, and [14, Theorem 1] is the same but for five
real numbers." So BFM = 9 numbers (measure 1/8 via T/(k-1)), Pintz [14] =
5 numbers (1/4), this paper = 4 numbers (1/3). The internal bookkeeping:
Proposition 18 (p. 22) partitions H into 4 equal blocks and finds >= 2
prime-occupied blocks; its proof (p. 23) refines to M = ceil(3.99a) + 1 =
400 sub-blocks with a = 100 and pigeonholes a + 1 = 101 prime-occupied
sub-blocks back into the 4 top blocks. The block count is tied to the
pairwise constant by M - 1 >= 3.99 a (used as "3.99 <= (M - 1)/a" on
p. 24): block count = ceil(A a) + 1, so A < 4 buys 4 blocks where A = 4
only bought 5 (Pintz) and the original argument 9 (BFM). There is no
"5/4-block" fractional object in this text; the correct reading of the
secondary phrase is the chain 9 -> 5 -> 4.

Focus question 5 (uniform sieve inputs). The complete input list, with
uniformity:
 (i) Modified Bombieri-Vinogradov = Proposition 8 (pp. 7-8) = [2, Theorem
 4.2]: level N^{1/2 - delta}, all moduli DIVISIBLE by a fixed square-free
 q_0 < N^epsilon with P^+(q_0) < N^{epsilon/log_2 N} (this is how the huge
 smooth Erdos-Rankin modulus W rides along), coprime to the exceptional
 marker Z_{N^{2 epsilon}} (Lemma 7 = [2, Lemma 4.1], Landau-Page type);
 loss only phi(q_0) in the bound.
 (ii) Proposition 11 (p. 8), NEW here: the same statement for almost-prime
 weights Lambda_0 = f * g, f supported on primes <= A_1, g on P^-(n) >=
 N^alpha, n asymp N/A_1 - needed because Chen's switched term S_3 counts
 n + h_l = pqrs. Proved from Lemma 9 (primitive-character remnant of [2,
 Theorem 4.2]'s proof) plus the multiplicative large sieve (Lemma 10 =
 [7, Theorem 9.10]).
 (iii) Maynard-Tao machinery imported wholesale from [2]: Lemma 4.6
 (i),(ii) (linear and pair counts under the sieve weights), Lemma 4.7
 (J_K/I_K >= rho delta log K/K, L_K/I_K <= (rho delta log K/K)^2, p. 24),
 assembled via Pintz's positive-linear-combination device (4.1)-(4.2)
 ([14, Theorem 3], [1, Theorem 5.4]).
 (iv) Modified Erdos-Rankin construction = Lemma 20 (p. 24) = [2, Lemma
 5.2]: produces the admissible K-tuple INSIDE a cleared window (0, z],
 z = y(log_2 y)/(2 log_3 y), y = epsilon log N, with positions h_i =
 beta_i x y + y + O(y e^{-log^{1/4} y}) and smooth difference products
 P^+(prod (h_j - h_i)) <= y (condition (3.4) feeding the W-coprimality of
 the sieve moduli).
 (v) Linear sieve (Lemma 14, [7, Ch. 11-12]) and Buchstab counts ((3.8),
 [7, Lemma 12.1]); plus the v3 erratum's fundamental-lemma preconditioning
 rho(n) (Lemmas 21-24, Section 6) to make the linear sieve compatible with
 Maynard-Tao weights - a technical point worth remembering if the project
 ever composes a linear sieve with Maynard-Tao weights: the naive
 composition of remainders is WRONG (Section 6, p. 26) and needs the
 P_0(y_1)-smooth-part Selberg preweight.

Assessment against the consuming target (unconditional exchange
configuration: two prime-gap-word sites, matched J-prefix and K-suffix
windows, dominant weighted middle difference, depths J, K ~ log_2 log x):

1. What the machinery CAN supply, unconditionally. (a) Sites: for every
large N, an n in [N, 2N] and a CLEARED window (n, n + z], z asymp
epsilon log N log_2 log N-ish (Lemma 20 with y = epsilon log N), in which
ALL primes lie in the prescribed position set n + H (p. 25: "P cap
(n, n + z] subseteq n + H") - this is a genuine unconditional
window-shaping device: it forbids primes off the template. (b) At least
two of four position-clusters (values (beta_i + epsilon + o(1)) log N)
contain primes (Proposition 18), hence one consecutive-prime pair whose
normalized gap lies in the 6-element menu {beta_j - beta_i}. (c) Since
this holds for every large N, pigeonholing over N gives ONE fixed pair
(i, j) realized for infinitely many N: an unconditional infinite supply
of sites with the SAME approximate single normalized gap - i.e., matched
one-letter middles. This is the strongest matched-site supply in the
surveyed BFM/Pintz/Merikoski line.

2. What it CANNOT supply, and why, in the paper's own terms. (a) No word
control: the argument guarantees >= 2 occupied clusters but has NO upper
control on which OTHER template positions are prime; the gap word inside
the cleared window is undetermined beyond one consecutive pair. Occupancy
is forced only from below (Maynard-Tao positivity), never coordinatewise
- so J-prefix/K-suffix windows around the middle gap cannot be matched by
this device. (b) Pigeonhole blindness (project blocker (i)) is structural
here: WHICH pair (i, j) occurs is chosen by the pigeonhole in Proposition
18/19 and by the pigeonhole over N; nothing steers it. (c) Prescribing
even the single middle difference exactly (rather than from a menu) is
identified by the paper itself as parity-blocked: Remark 2 (p. 6) says
A < 2 in (1.6) would give L = [0, infty] but "by the parity principle
this should be just as hard as obtaining a lower bound for such a sum
over prime pairs" - the project's blocker (ii), stated at the exact spot
D1.d cares about. Matching a J-prefix AND K-suffix is a fortiori a
tuple-type lower bound (many simultaneous prime pairs), deeper into
parity territory. (d) Depth mismatch: the sites live at one gap of size
asymp log N with 4 prescribed values; the target needs ~ J + K ~
log_2 log x consecutive gaps per site. The only multi-gap statement
available is negative (all primes in the window sit on the template),
which constrains gap words from below (each gap is a sum of consecutive
template spacings) but not which template spacings are realized.

3. Transferable assets worth logging. (a) The 3.99 constant (Prop 12) is
the current best pairwise upper-sieve constant at a Maynard-Tao-weighted
prime-pair sum with Erdos-Rankin-compatible moduli; any project
computation that needs "sum over sites of 1_P 1_P under MT measure <= A x
main term" should cite A = 3.99, not 4 (D1.d). (b) Proposition 11 (BV for
f * g almost-primes uniform in a q_0-divisibility family) is a reusable
unconditional equidistribution input, independent of the limit-point
application. (c) The block calculus "constant A at the pair spot ==>
ceil(Aa) + 1 blocks ==> menu size = block count, measure T/(blocks - 1)"
(pp. 6, 23-24) quantifies exactly how much a future improvement at the
pairwise spot buys: each unit below A = 4 removes one block; the parity
floor A = 2 corresponds to menu size 2, i.e. full L = [0, infty], and
NOTHING in this machinery approaches word-level (two-pair) control. (d)
The Erdos-Rankin clearing (Lemma 20) is the one device here that shapes a
whole window rather than a point, and is the natural candidate if the
project wants "desert + template" scaffolding around candidate exchange
sites; but its window length is asymp log N (log_3/log_4 factors aside),
far below the g_n-word depth the exchange configuration needs at
J, K ~ log_2 log x per site - and it prescribes where primes MAY be, not
where they ARE.

Bottom line: this paper supplies, unconditionally, matched SINGLE-gap
sites from a finite menu inside cleared log N-scale windows, the best
current pairwise upper-sieve constant (3.99, unoptimized 3.987), and an
explicit statement that anything stronger at the pair spot is
parity-equivalent to prime-pair lower bounds. It supplies no mechanism
for multi-gap word prescription, hence cannot by itself produce the
J-prefix/K-suffix matched exchange configuration; its role for the
project is as (i) the D1.d constant reference, (ii) a template for
"menu + pigeonhole" site production and its exact limits, and (iii) a
warning label, in the author's own words, on where parity bites.

---

## FLAGS (consolidated)

1. [TRANSCRIPTION-UNSURE] "Lebesque" (for Lebesgue) is transcribed as
   rendered throughout (abstract, p. 2, Proposition 4).
2. [TRANSCRIPTION-UNSURE] Abstract citation style "Pintz (2015)", "Banks,
   Freiberg, and Maynard (2015)" and the phrase "the arguments Pintz and
   Banks, Freiberg, and Maynard" (missing "of") transcribed as rendered.
3. [PRINTED-ODDITY] p. 12: "stricly less than four" (typo) as printed.
4. [PRINTED-ODDITY] p. 21, Remark 4: "Python 7.3" as printed.
5. [TRANSCRIPTION-UNSURE] p. 17 (Lemma 16 proof): "shifting up to
   Y = N^alpha" as printed (presumably "sifting").
6. [TRANSCRIPTION-UNSURE] Lemma 9 / eq. (2.2): stacked constraints under
   sup and sums are small print; read as AB <= N^{1/2-delta}, A <= q_0,
   a | q_0, (b, q_0 Z_{N^{2 epsilon}}) = 1.
7. [TRANSCRIPTION-UNSURE] Lemma 24: coprimality list includes
   Z_{N^{2 epsilon}} (not 4 epsilon) as printed; possible internal
   inconsistency in the paper.
8. [TRANSCRIPTION-UNSURE] Lemma 20: "((0, z] cap Z)" uses blackboard-bold
   Z (integers), renamed Z' in this transcript to avoid collision with
   the exceptional-prime set Z of the same lemma.
9. [PARAPHRASE] Proof anatomies of Proposition 11 (pp. 8-12), Lemma 17
   error handling (pp. 19-20), and Lemma 24 (p. 30) are summarized with
   only sighted displays quoted; all statements and all numeric constants
   (3.99, 4.19, 0.279, 0.076, alpha = 1/7, beta = 3/14, a = 100, M = 400)
   are quoted verbatim from the rendered pages.
10. Note: the arithmetic 4.19 - 0.279 + 0.076 = 3.987 in the commentary is
    extractor arithmetic on the paper's quoted bounds; the paper itself
    only states "Omega_1 - Omega_2 + Omega_3 < 3.99" (p. 21).
