# EXTRACTION: Banks-Freiberg-Maynard, "On Limit Points of the Sequence of Normalized Prime Gaps"

Source (only evidence base): /home/istr/pro/erdos251/dossier/1404.5094v2.pdf
arXiv:1404.5094v2 [math.NT] 20 Oct 2014 (sidebar stamp); "Date: October 21,
2014." (p. 1 footer). Authors as printed: WILLIAM D. BANKS, TRISTAN FREIBERG,
AND JAMES MAYNARD. 25 pages. Affiliations (p. 25): Banks and Freiberg,
Department of Mathematics, University of Missouri, Columbia MO, USA; Maynard,
Magdalen College, Oxford, UK.

Transcription conventions: ASCII only. Diacritics transliterated (Erdos,
Cramer, Yildirim, Westzynthius, Polya). Math in LaTeX-like ASCII: \beta,
\lambda = Lebesgue measure (also sieve weights \lambda_{d_1,...,d_k} in
Section 4.2, disambiguated by context), \phi = Euler function, \psi =
Chebyshev function, P = the set of primes (paper's blackboard-bold P),
1_P = prime indicator, H = calligraphic H (the k-tuple), H(n) =
{n+h_1,...,n+h_k}, P^+(q) = greatest prime factor, <= , >=, << (Vinogradov),
\asymp. The paper's iterated logarithm (Section 2, p. 4): "log_1 x =
max{1, log x} and log_{n+1} x = log_1(log_n x)", so log_2 = log log etc.
u x v written "u x v" only in the one flagged spot; otherwise products are
juxtaposed. Anchors are theorem/equation/section numbers as printed; page
numbers (printed page = PDF page) are secondary aid.

Everything up to the final section is EXTRACTION (what the paper says).
Commentary appears ONLY in the final marked section. Paraphrase is marked
"(paraphrase)".

---

## 1. ABSTRACT AND MAIN THEOREMS (verbatim)

Abstract (p. 1), verbatim:

> "Let p_n denote the nth smallest prime number, and let L denote the set of
> limit points of the sequence {(p_{n+1} - p_n)/log p_n}_{n=1}^infty of
> normalized differences between consecutive primes. We show that for k = 9
> and for any sequence of k nonnegative real numbers beta_1 <= beta_2 <= ...
> <= beta_k, at least one of the numbers beta_j - beta_i (1 <= i < j <= k)
> belongs to L. It follows that at least 12.5% of all nonnegative real
> numbers belong to L."

Theorem 1.1 (p. 2), verbatim:

> "THEOREM 1.1. Let d_n = p_{n+1} - p_n, where p_n denotes the nth smallest
> prime, and let L be the set of limit points of {d_n/log p_n}_{n=1}^infty.
> For any sequence of k = 9 nonnegative real numbers beta_1 <= beta_2 <= ...
> <= beta_k, we have
>   {beta_j - beta_i : 1 <= i < j <= k} cap L != emptyset.   (1.2)"

Corollary 1.2 (p. 2), verbatim (preceded by: "We have the following
corollary, which shows that at least 12.5% of nonnegative real numbers
belong to L."):

> "COROLLARY 1.2. Let L be as in Theorem 1.1, and let lambda be the Lebesgue
> measure on R. The following bound holds (with an ineffective o(1)):
>   lambda([0,T] cap L) >= (1 - o(1)) T/8   (T -> infty).   (1.3)
> The following effective bound also holds:
>   lambda([0,T] cap L) > T/22   (T > 0).   (1.4)"

Theorem 1.3 (p. 3), verbatim (preceded by: "We actually prove the following
more general result on 'chains' of gaps between primes, for which Theorem
1.1 is a stronger version of the special case m = 1."):

> "THEOREM 1.3. Let d_n = p_{n+1} - p_n, where p_n denotes the nth smallest
> prime. Fix an integer m >= 2, and let L_m be the set of limit points in
> [0, infty]^m of
>   { ( d_n/log p_n , ... , d_{n+m-1}/log p_{n+m-1} ) }_{n=1}^infty.
> Given beta = (beta_1, ..., beta_k) in R^k, let S_m(beta) be the set
>   { (beta_{J(2)} - beta_{J(1)}, ..., beta_{J(m+1)} - beta_{J(m)}) :
>     1 <= J(1) < ... < J(m+1) <= k }.
> For any sequence of k = 8m^2 + 8m nonnegative real numbers
>   beta_1 <= beta_2 <= ... <= beta_{8m^2+8m},
> we have
>   S_m(beta) cap L_m != emptyset.   (1.5)"

NOTE on the symbol k (paraphrase): in Theorems 1.1/1.3 k counts the
prescribed real numbers beta_i (k = 9, resp. k = 8m^2+8m). In Theorem 4.3
below, k is the SIZE of the admissible tuple H and is a "sufficiently large
multiple of (8m+1)(8m^2+8m)" -- a different, much larger quantity.

Proof of Corollary 1.2 (pp. 2-3), key verbatim steps:

> "Now let kappa >= 2 be the smallest integer such that for any sequence of
> kappa real numbers alpha_kappa >= ... >= alpha_1 >= 0, we have
> {alpha_j - alpha_i : 1 <= i < j <= kappa} cap L != emptyset. By Theorem
> 1.1 such a kappa exists and is at most 9. If kappa = 2 then L = [0,infty]."

Then (p. 3, verbatim): for hat-alpha_j witnessing minimality,

> "T_2 - T_1 <= sum_{j=1}^{kappa-1} lambda([T_1 - hat-alpha_j,
> T_2 - hat-alpha_j] cap L) <= (kappa - 1) lambda([0, T_2] cap L).
> This gives (1.3)."

and for the effective bound (p. 3, verbatim):

> "With kappa as above we have {alpha, 2 alpha, ..., (kappa-1) alpha} cap L
> != emptyset for every real number alpha >= 0 (take hat-alpha_j = j alpha
> for 1 <= j <= kappa). For any T >= 0, by subadditivity and positive
> homogeneity of Lebesgue measure, we have
>   lambda([0,T]) <= sum_{j=1}^{kappa-1} lambda([0,T] cap j^{-1} L)
>   = sum_{j=1}^{kappa-1} j^{-1} lambda([0, jT] cap L)
>   <= lambda([0, (kappa-1)T] cap L) sum_{j=1}^{kappa-1} j^{-1}.
> Replacing T by (kappa-1)^{-1} T and recalling that kappa <= 9, this gives
> (1.4)."

---

## 2. INTRODUCTION: PRIOR STATE OF THE ART (anchors p. 1-2)

Cramer-model conjecture (1.1) (p. 1, verbatim):

> "N^{-1} |{n <= N : d_n / log p_n in (alpha, beta]}| ~
>  int_alpha^beta e^{-t} dt   (N -> infty).   (1.1)"

Erdos conjecture, footnote 1 (p. 1, verbatim): "Erdos [5, p.4] wrote: 'It
seems certain that d_n/log n is everywhere dense in the interval
(0, infty).'" Main-text version (p. 1): "An approximation to (1.1) is the
conjecture of Erdos [5] that if L is the set of limit points of the sequence
{d_n / log p_n}_{n=1}^infty, then L = [0, infty]."

Known before this paper (p. 1-2), verbatim fragments:

> "It had already been established by Westzynthius [22] in 1931 that
> limsup_{n->infty} d_n/log p_n = infty."

> "In 2005, the groundbreaking work of Goldston-Pintz-Yildirim [10]
> established for the first time that liminf_{n->infty} d_n/log p_n = 0.
> Hence, 0 in L and infty in L, but no other limit point of L is known at
> present."

> "Hildebrand and Maier [11] were the first to show that L contains a limit
> point greater than 1. Indeed, they showed that there is a positive
> constant c such that lambda([0,T] cap L) >= cT holds for all sufficiently
> large T ... In fact, Hildebrand and Maier proved an m-dimensional analogue
> of this result for the limit points of 'chains' of m consecutive gaps
> between primes (see Theorem 1.3 below)."

> "Pintz [15] has shown that there is a small (ineffective) positive
> constant c such that L contains [0, c]. Most recently, Goldston and Ledoan
> [9] have shown that Erdos' method yields infinitely many limit points in
> intervals of the form [(1/C)(1 - (1/M) - eps), M] for any M > 1, where C
> is an overestimate in the sieve upper bound for the number of generalized
> twin primes (one can take C = 4). Further, Goldston and Ledoan have shown
> that there are infinitely many limit points in intervals such as
> [1/2000, 3/4]."

---

## 3. OUTLINE OF THE PROOF (Section 3, pp. 4-5)

Strategy sentence (p. 4, verbatim):

> "The idea underlying our proof of Theorem 1.3 is to combine a construction
> of Erdos [6] and Rankin [18] with the recent theorem of Maynard [13] and
> Tao."

(Footnote 3, p. 4, verbatim: "Tao (unpublished) independently discovered the
same method as Maynard around the same time.")

Erdos-Rankin sieve-out (p. 4, verbatim):

> "The Erdos-Rankin construction produces long intervals (n, n+z] containing
> only composite integers. This is accomplished by choosing a set of
> integers {a_p : p <= y}, one for each prime p <= y < z, so that for every
> integer g in (0, z], the congruence g == a_p mod p holds for at least one
> p <= y. By the Chinese remainder theorem one can find an integer b,
> uniquely determined modulo P(y) = prod_{p <= y} p, such that b == -a_p
> mod p for every p <= y. Now suppose n == b mod P(y) and n > y. For any
> g in (0, z] we have g == a_p mod p for some p | P(y), and so g + n ==
> a_p - a_p == 0 mod p; hence, g + n is composite for each g in (0, z]. In
> this situation we say that the progression b mod P(y) sieves out intervals
> of the form (n, n+z], where n == b mod z and n > y."

[TRANSCRIPTION-UNSURE: the last clause prints "where n == b mod z and
n > y"; from context "mod P(y)" is meant, transcribed as printed.]

> "Noting that log P(y) ~ y by the prime number theorem, the goal is to
> maximize the ratio z/y."

Maynard-Tao inside an arithmetic progression (p. 5, verbatim):

> "It turns out that in the Maynard-Tao theorem one can restrict n to lie in
> an arithmetic progression -- in fact this is a feature of its proof. Given
> a sufficiently large number N and a modulus W = prod_{p <= w} p, where w
> grows slowly with N, one can take n in (N, 2N] with n == b mod W,
> provided that b is an integer for which (b + h_i, W) = 1 for each i.
> Choosing the progression b mod W carefully, one can use it to sieve out
> all integers in intervals of the form (n, n+z] with n == b mod W except
> for the integers in H(n). Used in this way, the Maynard-Tao theorem
> produces consecutive m-tuples of primes in intervals of bounded length."

The paper's uniform extension (p. 5, verbatim):

> "In the present paper, we modify the above ideas to obtain consecutive
> primes in H(n) = {n + h_1, ..., n + h_k}, n in (N, 2N], with differences
> h_j - h_i \asymp log N. To do this, we give a uniform version of the
> Maynard-Tao theorem in which the elements of the k-tuple H =
> {h_1,...,h_k} are allowed to grow with N, and in which w can be as large
> as eps log N for a sufficiently small eps. This means that the modulus W
> is as large as a small power of N, and for reasons concerning level of
> distribution (see (4.2) et seq.), this extension of the Maynard-Tao
> theorem requires a modification of the Bombieri-Vinogradov theorem that
> exploits the fact that the arithmetic progressions with which we are
> concerned have moduli that are all multiples of the smooth integer W."

The partition refinement (p. 5, verbatim):

> "To obtain stronger quantitative results, we use a further modification of
> the Maynard-Tao theorem, which might be of independent interest. We show
> that given a partition H = H_1 cup ... cup H_{8m+1} of H into 8m+1 equal
> sized subsets, there are infinitely many n such that |H_j(n) cap P| >= 1
> for at least m+1 different values of j in {1,...,8m+1}, provided that the
> size of H is sufficiently large."

Selecting the tuple from unsifted primes (p. 5, verbatim):

> "We use a slight modification of the Erdos-Rankin construction to find an
> arithmetic progression b mod W that sieves out the integers in an interval
> (0, z], except for precisely k integers H = {h_1,...,h_k} subset (0, z]
> that constitute our admissible k-tuple. We want to choose H so that
> h_j - h_i ~ (beta_j - beta_i) log N for 1 <= i < j <= k, where beta_k >=
> ... >= beta_1 >= 0 are given."

Greedy sieve staging (p. 5, verbatim; this is the germ of the bin
construction detailed in Lemma 5.2):

> "As in the Erdos-Rankin construction, we select the integers
> {a_p : p <= y}, y <= z, in stages according to their size. We take
> 0 < y_1 < y_2 < y < z, say, where y_1 and y_2 are parameters to be chosen
> optimally later. First, we put a_p = 0 for primes p in (y_1, y_2]. Next,
> we use a 'greedy sieve' to choose the a_p optimally for the small primes
> 2 < p <= y_1, that is, we successively choose a_p so that g == a_p mod p
> for the maximum possible number of g in (0, z] that have remain 'unsifted'
> thus far. Since we do not know the congruence classes a_p mod p for the
> smallest primes, our approach does not work in general for all k-tuples
> H = {h_1,...,h_k}; we find it convenient to select our k-tuple only after
> sieving by primes p <= y_2. We choose the numbers h_i from among the
> primes in (y, z]. (This is why we do not use p = 2 'greedily' -- if we had
> a_2 = 1 then only even integers would remain unsifted.) It is clear that
> each h_i !== a_p mod p for all p in (y_1, y_2] since for those primes we
> have a_p = 0. We can also guarantee that h_i !== a_p mod p for the small
> primes p <= y_1 if we select primes h_i in a suitable arithmetic
> progression b mod P_1, where P_1 = prod_{2 < p <= y_1} p. We choose
> y_1 = (log y)^{1/4}, so such primes exist by (Page's version of) the prime
> number theorem for arithmetic progressions."

(Section 3 opens with, p. 4, verbatim: "For the sake of exposition we ignore
(only in this section) the possibility of Siegel zeros -- accounting for
this possibility introduces certain minor technical complications in parts
of the proof." Footnote 2 defines Siegel zero as "a real, simple zero of a
Dirichlet L-function (corresponding to a primitive character), in a region
that we can show is otherwise zero free.")

---

## 4. THE UNIFORM MAYNARD-TAO THEOREM (Section 4)

### 4.1 Preliminaries (pp. 6-7)

Admissibility (4.1) (p. 6, verbatim):

> "We say that a given k-tuple of integers H = {h_1,...,h_k} is admissible
> if
>   |{n mod p : prod_{i=1}^k (n + h_i) == 0 mod p}| < p   (p in P).  (4.1)"

Level of distribution (4.2) (p. 6, verbatim):

> "We say that the primes have level of distribution theta if for any given
> eps in (0, theta) and A > 0 one has, for all N > 2, the bound
>   sum_{q <= N^{theta - eps}} max_{(q,a)=1} | psi(N; q, a) -
>   psi(N)/phi(q) | <<_{eps,A} N/(log N)^A.   (4.2)"

> "The celebrated Bombieri-Vinogradov theorem [1, Theoreme 17] implies that
> the primes have level of distribution theta = 1/2, and the
> Elliott-Halberstam conjecture [4,7] asserts that the primes have level of
> distribution theta = 1."

Functionals I_k(F), J_{i,1-eta}(F) over the simplex, and M_{k,eta} (4.3)
(p. 6): (paraphrase) M_{k,eta} = sup sum_{i=1}^k J_{i,1-eta}(F) / I_k(F)
over square-integrable F supported on (1+eta)R_k = {(t_1,...,t_k) in
[0,1]^k : t_1 + ... + t_k <= 1 + eta}, not identically zero.

Maynard's input and Polymath refinements (pp. 6-7, verbatim):

> "Maynard [13, Proposition 4.2] has shown that for any given m there are
> infinitely many n with |H(n) cap P| >= m + 1, provided M_k = M_{k,0} >
> 2 theta^{-1} m, where theta is an admissible level of distribution for P.
> By [13, Proposition 4.3] one has M_5 > 2, M_105 > 4, and that M_k >
> log k - log log k - 2 for all sufficiently large k. A recent Polymath
> project [17, Theorem 3.9] has refined these bounds as follows:
>   M_54 > 4,   M_k >= log k - c,   (4.4)
> for some absolute constant c. Moreover, the Polymath project has refined
> the method of [13] slightly, allowing one to reduce the condition M_k >
> 2 theta^{-1} m to M_{k,eta} > 2 theta^{-1} m for some 0 <= eta <=
> theta^{-1} - 1. They have also [17, Theorem 3.13] produced the bound
>   M_{50,1/25} > 4.   (4.5)"

> "Therefore, if H(x) = {x + h_i}_{i=1}^k is any admissible k-tuple, then
> for infinitely many n we have |H(n) cap P| >= m + 1, provided k >= 50 in
> the case m = 1, and k >= e^{4m+c} in general. On the Elliott-Halberstam
> conjecture this holds provided k >= 5 in the case m = 1, and k >= e^{2m+c}
> in general."

Zero-free region for smooth moduli, Lemma 4.1 (p. 7, verbatim):

> "LEMMA 4.1. Let T >= 3 and let P >= T^{1/log_2 T}. Among all primitive
> characters chi mod q to moduli q satisfying q <= T and P^+(q) <= P, there
> is at most one for which L(s, chi) has a zero in the region
>   Re(s) > 1 - c/log P,  |Im(s)| <= exp( log P / sqrt(log T) ).   (4.6)
> where c is a (sufficiently small) positive absolute constant. If such a
> character chi mod q exists, then chi is real, L(s, chi) has just one zero
> in the region (4.6), which is real and simple, and
>   P^+(q) >> log q >> log_2 T.   (4.7)"

(Proof outline, p. 7: "Lemma 4.1 follows from Chang's bound [2] for
character sums to smooth moduli"; uses Chang [2, Theorem 5]
sum_{n <= u} chi(n) << u e^{-sqrt(log u)}, Polya-Vinogradov, and
[12, Lemmas 10-12].)

Exceptional modulus bookkeeping (p. 8, verbatim):

> "We fix an absolute constant c as in Lemma 4.1 and define
>   Z_T = P^+(q)   (4.8)
> if such an exceptional modulus q exists, and Z_T = 1 if no such modulus
> exists. For future reference, note that the bound (4.7) implies that,
> regardless of whether or not such a modulus exists, we have
>   Z_T/phi(Z_T) = 1 + O(1/log_2 T).   (4.9)"

### 4.2 Theorem 4.2: Modified Bombieri-Vinogradov (p. 8, verbatim)

> "THEOREM 4.2 (Modified Bombieri-Vinogradov theorem). Let N > 2. Fix any
> C > 0 and theta = 1/2 - delta in (0, 1/2). Fix eps > 0 and suppose q_0 is
> a squarefree integer satisfying q_0 < N^eps and P^+(q_0) <
> N^{eps/log_2 N}. If eps = eps(C, delta, c) is sufficiently small in terms
> of C, delta and the constant c in Lemma (4.1), then with Z_{N^{2 eps}} as
> in (4.8) we have
>   sum_{q < N^theta, q_0 | q, (q, Z_{N^{2 eps}}) = 1} max_{(q,a)=1}
>   | psi(N; q, a) - psi(N)/phi(q) | <<_{delta,C}
>   N / ( phi(q_0) (log N)^C ).   (4.10)"

Proof anatomy (paraphrase with anchors): rewrite via primitive characters;
explicit formula (4.12) [3, Sec. 19, (13)-(14)]; dyadic decomposition into
(4.13) with the zero-counting quantity N*(sigma, A, B, T); Montgomery's zero
density estimate [14, Theorem 12.2], quoted verbatim (p. 9):

> "N*(sigma, A, B, T) << (A^2 B^2 T)^{3(1-sigma)/(2-sigma)}
>  (log(ABT))^9.   (4.14)"

For m >= C' log_2 N (C' = (C+15)/delta) this suffices; for m <= C' log_2 N
the zero-free region of Lemma 4.1 covers the range (p. 10, verbatim):

> "By Lemma 4.1, if chi mod q is primitive with q < N^{2 eps} and P^+(q) <
> N^{2 eps / log_2 N^{2 eps}}, then L(s, chi) has no zeros in the region
> Re(s) > 1 - c log_2 N^{2 eps} / log N^{2 eps}, |Im(s)| <=
> exp( sqrt(log N^{2 eps}) / log_2 N^{2 eps} ), unless (q, Z_{N^{2 eps}})
> != 1."

[TRANSCRIPTION-UNSURE: in the displayed region on p. 10 the numerator/
denominator arrangement of the Re(s) bound reads "1 - c log_2 N^{2 eps} /
log N^{2 eps}" and the Im(s) bound "exp( sqrt(log N^{2 eps}) /
log_2 N^{2 eps} )"; the placement of the square root over "log N^{2 eps}"
only is as best legible.]

### 4.3 Theorem 4.3: the uniform two-partition Maynard-Tao theorem (p. 10, verbatim)

> "THEOREM 4.3. Let m, k and eps = eps(k) be fixed. If k is a sufficiently
> large multiple of (8m+1)(8m^2+8m) and eps is sufficiently small, there is
> some N(m, k, eps) such that the following holds for all N >= N(m,k,eps).
> With Z_{N^{4 eps}} given by (4.8), let
>   w = eps log N   and   W = prod_{p <= w, p !| Z_{N^{4 eps}}} p.   (4.15)
> Let H = {h_1,...,h_k} be an admissible k-tuple such that
>   0 <= h_1, ..., h_k <= N   (4.16)
> and
>   p | prod_{1 <= i < j <= k} (h_j - h_i)  ==>  p <= w.   (4.17)
> Let
>   H = H_1^{(1)} cup ... cup H_{8m+1}^{(1)}
>     = H_1^{(2)} cup ... cup H_{8m^2+8m}^{(2)}   (4.18)
> be two partitions of H into 8m+1 and 8m^2+8m sets of equal size
> respectively. Finally, let b be an integer such that
>   ( prod_{i=1}^k (b + h_i), W ) = 1.   (4.19)
> (i) There is some n_1 in (N, 2N] with n_1 == b mod W, and some set of m+1
> distinct indices {i_1^{(1)},...,i_{m+1}^{(1)}} subset {1,...,8m+1}, such
> that
>   |H_i^{(1)}(n_1) cap P| = 1   for all i in
>   {i_1^{(1)},...,i_{m+1}^{(1)}}.   (4.20)
> (ii) There is some n_2 in (N, 2N] with n_2 == b mod W, and some set of
> m+1 distinct indices {i_1^{(2)},...,i_{m+1}^{(2)}} subset
> {1,...,8m^2+8m}, such that
>   |H_i^{(2)}(n_2) cap P| = 1   for all i in
>   {i_1^{(2)},...,i_{m+1}^{(2)}},
>   |H_i^{(2)}(n_2) cap P| <= 1   for all i_1^{(2)} < i < i_{m+1}^{(2)}.
>   (4.21)"

Remarks following Theorem 4.3 (pp. 10-11, verbatim):

> "If we fix m, k and eta in [0,1) with M_{k,eta} - 4m > 0 (where M_{k,eta}
> is as in (4.3)), and if we assume the remaining hypotheses of Theorem 4.3
> hold (disregarding (4.18)), then we can show, for all N >= N(m,k,eps),
> that |H(n) cap P| >= m+1 for at least one n in (N, 2N] with n == b mod W.
> This follows from an essentially identical argument to that presented in
> [13,17], although there are two differences in our setting that
> potentially affect the argument. Namely, w is considerably larger here
> than in [13] or [17] (we take w = eps log N instead of w = log_3 N), and
> the elements of H here may vary with N."

> "However, this actually only leads to weaker versions of Theorems 1.1 and
> 1.3, for instance (cf. (4.4), (4.5)) with k = 50 instead of k = 9 in our
> main theorem (Theorem 1.1), which is concerned with the case m = 1 of
> Theorem 4.3. The proof of Theorem 4.3, given in Section 4.2, does not
> require such refined estimates as in [13,17], but does require an
> additional sieve upper bound, whose use had been considered by the authors
> of [17]."

> "We remark that with more significant modifications to the argument
> presented in [13,17], it is in principle possible to remove the
> requirement (4.17) from the statement of Theorem 4.3. We do not consider
> this here."

### 4.4 Key estimates (Section 4.2 of the paper, pp. 11-16)

Standing conventions (p. 11, verbatim): "k is fixed; delta > 0 and eps > 0
are fixed and satisfy 2 delta + 2 eps < 1/2 (as well as delta > 2 eps in
Lemma 4.6 (iii)); N is to be thought of as tending to infinity ...
Z_{N^{4 eps}} is given by (4.8); w, W, H = {h_1,...,h_k} and b are as in
(4.15) - (4.19). (Note that by the prime number theorem, W < N^{2 eps},
hence N^{2 delta} W < N^theta where theta < 1/2, and likewise if delta >=
2 eps then N^{1/2 - delta} W < N^theta where theta < 1/2.)"

Sieve weights (4.22) (p. 11, verbatim):

> "lambda_{d_1,...,d_k} =
>   ( prod_{i=1}^k mu(d_i) ) sum_{j=1}^J prod_{l=1}^k
>     F_{l,j}( log d_l / log N )   if (d_1 ... d_k, Z_{N^{4 eps}}) = 1,
>   0   otherwise,   (4.22)"

with support condition (p. 11, verbatim): "sup { sum_{l=1}^k t_l :
prod_{l=1}^k F_{l,j}(t_l) != 0 } <= delta, for each j in {1,...,J}. This
support condition implies lambda_{d_1,...,d_k} is supported on d_i with
prod_{i=1}^k d_i <= N^delta." Also "F(t_1,...,t_k) = sum_{j=1}^J
prod_{l=1}^k F'_{l,j}(t_l)" (F'_{l,j} the derivative), F symmetric, and
"B = (phi(W)/W) log N."

Lemma 4.4 (p. 12, verbatim statement condensed to its display):

> "LEMMA 4.4. If F_1,...,F_k, G_1,...,G_k : [0,infty) -> R are fixed smooth
> compactly supported functions, then
>   sum'_{d_1,...,d_k, d'_1,...,d'_k} prod_{j=1}^k
>   ( mu(d_j) mu(d'_j) / [d_j, d'_j] ) F_j(log d_j / log N)
>   G_j(log d'_j / log N) = (c + o(1)) B^{-k},
> where sum' denotes summation with the restriction that [d_1, d'_1], ...,
> [d_k, d'_k], W Z_{N^{4 eps}} are pairwise coprime, and
>   c = prod_{j=1}^k int_0^infty F'_j(t_j) G'_j(t_j) dt_j.
> The same holds if the denominators [d_j, d'_j] are replaced by
> phi([d_j, d'_j])."

Proof (p. 12, verbatim): "This is [17, Lemma 4.1] combined with the fact
that, by (4.9), (Z_{N^{4 eps}} / phi(Z_{N^{4 eps}}))^k = 1 + o(1)."

Lemma 4.5 (p. 12, verbatim; I_k, J_k, L_k defined just above it as the
standard square integrals, with L_k(F) the double-integrated square):

> "LEMMA 4.5. (i) We have
>   sum_{N < n <= 2N, n == b mod W} ( sum_{d_1,...,d_k, d_i | n + h_i}
>   lambda_{d_1,...,d_k} )^2 = (1 + o(1)) (N/W) B^{-k} I_k(F).
> (ii) For each j in {1,...,k}, we have
>   sum_{N < n <= 2N, n == b mod W} 1_P(n + h_j) ( ... )^2 =
>   (1 + o(1)) (N/W) B^{-k} J_k(F).
> (iii) For each pair j, l in {1,...,k}, j != l, we have
>   sum_{N < n <= 2N, n == b mod W} 1_P(n + h_j) 1_P(n + h_l) ( ... )^2
>   <= (4 + O(delta)) (N/W) B^{-k} L_k(F)."

(The "( ... )^2" is the same squared lambda-weight as in (i); paraphrase of
identical display.)

Proof anatomy of Lemma 4.5 (pp. 13-15), load-bearing points:

- (i): inner sum equals "N / ( W prod_{i=1}^k [d_i, d'_i] ) + O(1)" under
  pairwise-coprimality forced by b, the support of lambda, and (4.17)
  ("Since p does not divide prod_{i != j} (h_i - h_j) unless p <= w"); error
  "trivially contributes O(N^{2 delta + o(1)})" (p. 13).
- (ii): inner sum equals "( pi(2N + h_j) - pi(N + h_j) ) / ( phi(W)
  prod_{i=1}^k phi([d_i, d'_i]) ) + O(E(N; [d_1,d'_1] ... [d_k,d'_k] W))"
  (p. 13); the error is controlled by Cauchy-Schwarz and Theorem 4.2,
  yielding "<< N / ( W (log N)^{2k} )" (p. 14).
- (iii) new sieve upper bound (p. 14, verbatim):

> "we see there is no contribution unless d_j = d_l = 1. We first impose
> this restriction, and then use the sieve upper bound
>   1_P(n + h_l) <= ( sum_{e | n + h_l} mu(e) G( log e / log R ) )^2,
> for a smooth function G : [0,infty) -> R supported on [0, 1/4 - 2 delta],
> with G(0) = 1. (The use of such a bound was previously suggested in
> discussions of the Polymath 8b project.)"

  and (p. 15, verbatim): "Finally, we take G(t) to be a fixed smooth
  approximation to 1 - t/(1/4 - delta) supported on 1/4 - t with G(0) = 1
  and int_0^infty G'(t)^2 dt <= 4 + O(delta). This gives the result."
  [TRANSCRIPTION-UNSURE: "supported on 1/4 - t" as printed; presumably
  "supported on [0, 1/4 - delta]".]

Lemma 4.6 (p. 15, verbatim):

> "LEMMA 4.6. Let 0 < rho < 1. Then there is a fixed choice of J and
> F_{l,j} for l in {1,...,k}, j in {1,...,J}, with the required properties
> such that
>   J_k(F) >= (1 + O((log k)^{-1/2})) ( rho delta log k / k ) I_k(F),
>   L_k(F) <= (1 + O((log k)^{-1/2})) ( rho delta log k / k )^2 I_k(F)."

Proof ingredients (pp. 15-16, verbatim fragments): "This follows from the
method of [13, Proposition 4.3]." The test function F_k(t_1,...,t_k) =
prod g(k t_i) on sum t_i <= 1, with "g(t) = 1/(1 + At) if t in [0, T]",
"A = log k - 2 log log k, T = (e^A - 1)/A"; "The proof of [13, Proposition
4.3] shows that J_k(F_k) >= (1 + O((log k)^{-1/2})) (log k) I_k(F_k)/k";
the new computation gives "L_k(F_k) <= ( log k / k )^2 I_k(F_k)" (display,
p. 16); Stone-Weierstrass smoothing with F(t_1,...,t_k) approximating
F_k(rho delta t_1, ..., rho delta t_k) rescales I_k, J_k, L_k by
(delta rho)^k, (delta rho)^{k+1}, (delta rho)^{k+2} respectively (p. 16).

Deduction of Theorem 4.3 (pp. 16-17). Part (i) uses the weighted sum
(p. 16, display, verbatim):

> "S = sum_{N < n <= 2N} ( sum_{i=1}^k 1_P(n + h_i) - m -
>   sum_{j=1}^{8m+1} sum_{h, h' in H_j^{(1)}, h != h'} 1_P(n + h)
>   1_P(n + h') ) ( sum_{d_1,...,d_k, d_i | n + h_i for all i}
>   lambda_{d_1,...,d_k} )^2."

> "We note that if S > 0 then there must be at least one n that makes a
> positive contribution to the sum, and this occurs only when there exists
> m+1 elements h'_1, ..., h'_{m+1} of H each in different subsets H_i^{(1)}
> such that n + h'_j is prime for all 1 <= j <= m+1."

Evaluation (p. 17, verbatim): "By Lemmas 4.5 and 4.6, we see that for
k > k_0(m, delta), by choosing rho < 1 such that delta rho log k = 2m there
exists a choice of F such that

> S = (N/W) B^{-k} I_k(F) ( sum_{i=1}^k 2m/k - m - 4 sum_{j=1}^{8m+1}
>     sum_{h,h' in H_j, h != h'} (2m)^2/k^2 + O(delta) )
>   = (N/W) B^{-k} I_k(F) ( m/(1+8m) + 8m^2/k + O(delta) ).

Thus, S > 0 for delta sufficiently small, as required."

Part (ii) (p. 17, verbatim): analogous sum S' with partition into 8m^2+8m
sets and coefficient m + (m+1) sum ... 1_P(n+h) 1_P(n+h'):

> "If n makes a positive contribution to S' then we must have that the
> number of indices j for which |H_j^{(2)}(n) cap P| = 1 is at least
> m + 1 + mr, where r is the number of indices i for which
> |H_i^{(2)}(n) cap P| > 1. Thus in particular, there must be some set of
> m+1 indices i_1 < ... < i_{m+1} for which |H_i^{(2)}(n) cap P| = 1 for
> i = i_1, ..., i_{m+1}, and |H_i^{(2)}(n) cap P| = 0 for i_1 < i < i_{m+1}
> and i != i_1, ..., i_{m+1}. Applying Lemmas 4.5 and 4.6 and choosing
> delta rho log k = 2m as above, we find that S' > 0 for delta sufficiently
> small and N sufficiently large, so such an n must exist."

---

## 5. THE ERDOS-RANKIN TYPE CONSTRUCTION (Section 5, pp. 17-22)

Lemma 5.1 (p. 17, verbatim):

> "LEMMA 5.1. Let {h_1,...,h_k} be an admissible k-tuple, let S be a set of
> integers, and let P be a set of primes, such that for some x >= 2,
>   {h_1,...,h_k} subset S subset [0, x^2]   and
>   |{p in P : p > x}| > |S| + k.
> There is a set of integers {a_p : p in P} with the property that
>   {h_1,...,h_k} = S \ cup_{p in P} {g : g == a_p mod p}."

(Here P is the paper's script-P, a set of primes, not the set of all
primes; proof pp. 17-18 is elementary and iterative.)

Standard inputs recorded (p. 18): Mertens (5.1), (5.2); smooth-number bound
(5.3) verbatim:

> "Psi(x, y) << x (log x)^{-1}   (1 <= 2 log y <= (log x)(log_2 x)^{-1})."

Page's PNT for APs (5.4) (p. 19, verbatim):

> "sum_{x < p <= x+y, p == a mod q} log p = y/phi(q) +
>  O( x exp(-c' sqrt(log x)) )   (5.4)
> uniformly for 2 <= y <= x, q <= exp(c sqrt(log x)) and (q, a) = 1, except
> possibly if q is a multiple of a certain integer q_1 depending on x which,
> if it exists, satisfies P^+(q_1) >> log_2 x (the implicit constant also
> determined by c)."

Lemma 5.2 -- the tuple-manufacturing lemma (p. 19, verbatim):

> "LEMMA 5.2. Fix an integer k >= 1 and real numbers beta_k >= ... >=
> beta_1 >= 0. There is a number y(beta, k), depending only on
> beta_1,...,beta_k and k, such that the following holds. Let x, y, z be
> any numbers satisfying x >= 1, y >= y(beta, k) and
>   2y(1 + (1 + beta_k) x) <= 2z <= y (log_2 y)(log_3 y)^{-1}.   (5.5)
> Let Z be any (possibly empty) set of primes such that for all p' in Z,
>   sum_{p in Z, p >= p'} 1/p << 1/p' << 1/log z.   (5.6)
> There is a set {a_p : p <= y, p not in Z} and an admissible k-tuple
> {h_1,...,h_k} such that
>   {h_1,...,h_k} = ((0, z] cap Z) \ cup_{p <= y, p not in Z}
>     {g : g == a_p mod p}.   (5.7)
> Moreover, for 1 <= i < j <= k,
>   p | (h_j - h_i)  ==>  p <= y,   (5.8)
> and for 1 <= i <= k,
>   h_i = beta_i x y + y + O( y e^{-(log y)^{1/4}} ).   (5.9)"

[TRANSCRIPTION-UNSURE: in (5.7) the set difference base prints as
"((0, z] cap Z)" with a double-struck Z, i.e. (0,z] cap the INTEGERS Z,
not the exceptional prime set Z (script-Z); transcription: base set =
integers in (0, z].]

Proof anatomy of Lemma 5.2 (pp. 19-22), the bin construction:

(a) Parameters (p. 19, verbatim): "Let y_1, y_2, y and z be numbers such
that 2 < y_1 < y_2 < y < z < y_1 y_2 and 2 log y_1 <=
(log z)(log_2 z)^{-1}. (5.10)" Later fixed (p. 21, verbatim): "We will
presently require that y_1 <= c sqrt(log y), so we now assume that
y_1 = (log y)^{1/4}, y_2 = y (log_3 y)^{-1}, y < 2z <=
y (log_2 y)(log_3 y)^{-1}."

(b) Moduli products (p. 19, display): P_1 = prod_{2 < p <= y_1, p not in Z,
p != l} p; P_2 = prod_{y_1 < p <= y_2, p not in Z} p; P_3 = prod_{y_2 < p
<= y, p not in Z} p, "where in the definition of P_1, l is a prime
satisfying l >> log y_1 ... It is important to note that 2 does not divide
P_1."

(c) Medium primes sift (p. 20): "For p | P_2 we choose a_p = 0." The
surviving set N_1 = {h in (0, z] : (h, P_2) = 1} satisfies (p. 20,
verbatim): "|N_1| <= z log( log z / log y_2 ) + O( z / log y_2 )" via
(5.11), (5.3) and (5.1), refined to

> "|N_1| <= ( z / log y_2 ) ( log(z/y_2) + O(1) ).   (5.14)"

(d) Greedy sieve on small primes (p. 20, verbatim): "For p | P_1 we choose
a_p 'greedily' ... there exists an integer a_p such that |{g in S : g ==
a_p mod p}| >= |S|/p. ... we eventually obtain a set N_2 = N_1 \
cup_{p | P_1} {g : g == a_p mod p} whose cardinality satisfies the bound

> |N_2| <= |N_1| prod_{p | P_1} (1 - 1/p) <=
>   2 e^{-gamma} z (log(z/y_2) + O(1)) / ( (log y_1)(log y_2) ).   (5.15)"

(e) Surplus of large primes (p. 21, verbatim): with the above parameter
choices,

> "|{p in (y_2, y] : p not in Z}| - |N_2| >= (y / log y)(1 - e^{-gamma})
>   + O( y / ((log y)(log_3 y)) ).
> The right-hand side tends to infinity with y, and so
> |{p in (y_2, y] : p not in Z}| > |N_2| + k if y is sufficiently large in
> terms of k, as we now assume."

Then Lemma 5.1 (with P = primes dividing 2 l P_3) removes all of N_2
except a chosen k-tuple.

(f) Choosing the k-tuple in bins (pp. 21-22): the progression A mod P_1 is
defined by A == -1 or 1 mod p according as a_p == 1 mod p or not (p. 21);
"the primes h in (y, z] with h == A mod P_1 all lie in N_2" (p. 21).
Distinctness of prime divisors of differences (p. 21, verbatim):

> "if h and h' < h are any two such primes then p | h - h' ==> p | P_1 or
> p | (h - h')/P_1 ==> p <= max{y_1, z/P_1} < y if y is large enough, as we
> assume, so any k-tuple of primes {h_1,...,h_k} chosen in this way
> satisfies (5.8). Moreover, such a k-tuple of primes is admissible since
> min{h_1,...,h_k} > k (we assume that y > k)."

Prime supply in each bin via (5.4) with Delta = y e^{-(log y)^{1/4}}
(p. 22, verbatim):

> "We let Delta = y e^{-(log y)^{1/4}}. Thus,
>   sum_{u < p <= u + Delta, p == A mod P_1} log p >>
>   y exp( -3 (log y)^{1/4} )
> uniformly for y <= u <= z, and the left-hand side is a sum over at least
> k primes if y is sufficiently large in terms of k, as we now assume."

The bins themselves (p. 22, verbatim):

> "For 1 <= i <= k, let
>   u_i = beta_i x y + y,
> so that the intervals (u_i, u_i + Delta] are all contained in (y, z]. For
> each 1 <= i <= k in turn, we choose a prime h_i in (u_i, u_i + Delta]
> with h_i == A mod P_1 and h_i != h_j for any j < i. This is possible
> since each interval contains at least k primes that are congruent to
> A mod P_1. We see that the resulting set {h_1,...,h_k} is admissible
> since no element is congruent to a_p mod p for any prime p <= k.
> Moreover, h_i = u_i + O(Delta), which gives (5.9)."

[TRANSCRIPTION-UNSURE: "h_i != h_j for any j < i" -- the subscript
inequality prints with slight kerning; "j < i" is the sensible reading.
Also "for any prime p <= k" at the end: plausibly "p <= y" is meant; as
printed it reads p <= k.]

---

## 6. DEDUCTION OF THEOREMS 1.1 AND 1.3 (Section 6, pp. 22-24)

Deduction of Theorem 1.3 (pp. 22-23). Setup (p. 22, verbatim):

> "Fix k >= m >= 2 and eps = eps(k, m) in (0, 1), with k a sufficiently
> large multiple of (8m^2+8m)(8m+1), and eps sufficiently small, in the
> sense of Theorem 4.3. Fix real numbers beta_{8m^2+8m} >= ... >= beta_1
> >= 0. Let beta in R^k be given by
>   beta = (beta_1, ..., beta_1, beta_2, ..., beta_2, ..., beta_{8m^2+8m},
>           ..., beta_{8m^2+8m}),
> where there are k/(8m^2+8m) consecutive copies of each beta_i appearing
> in beta. Let N >= N(k, m, eps) (as in Theorem 4.3) and put
>   x = eps^{-1},   y = w = eps log N,   z = y (log_2 y)(2 log_3 y)^{-1}."

[TRANSCRIPTION-UNSURE: the first N-threshold prints "N >= N(m, k, eps)" or
"N(k, m, eps)"; argument order not fully legible, same quantity as Theorem
4.3.]

> "If N >= N(beta, k, m, eps) is large enough in terms of beta and k, then
> with y(beta, k) as in Lemma 5.2 we have
>   x > 1,  y >= y(beta, k),  2y(1 + (1 + beta_k)x) <= 2z <=
>   y (log_2 y)(log_3 y)^{-1}."

Exceptional-prime bookkeeping (p. 23, verbatim): "Let Z_{N^{4 eps}} be
given by (4.8) and let W = prod_{p <= w, p !| Z_{N^{4 eps}}} p. Let us
define Z by putting Z = emptyset if Z_{N^{4 eps}} = 1 and Z =
{Z_{N^{4 eps}}} if Z_{N^{4 eps}} != 1. Then (4.7) implies that the
condition (5.6) is satisfied since log z << log_2 N^eps."
[TRANSCRIPTION-UNSURE: last displayed comparison prints "log z <<
log_2 N^eps"; could be "log_2 N^{4 eps}".]

Conclusion of Lemma 5.2 (p. 23): there exist {a_p : p <= y, p not in Z}
and an admissible k-tuple with

> "{h_1,...,h_k} = ((0, z] cap Z) \ cup_{p <= y, p not in Z}
>  {g : g == a_p mod p}   (6.1)"

(same double-struck-Z reading as (5.7)), and

> "p | (h_j - h_i) ==> p <= y = w   (6.2)"

> "H = H_1 cup ... cup H_{8m^2+8m}   (6.3)
> such that for each j in {1,...,8m^2+8m} we have
>   h = (beta_j + eps + o(1)) log N   for all h in H_j.   (6.4)"

> "We let b be an integer satisfying b == -a_p mod p   (6.5)
> for all p <= y, p not in Z."

Application of Theorem 4.3(ii) (p. 23, paraphrase with verbatim core):
0 < h_i <= z < N gives (4.16); (6.2) and (6.3) give (4.17) and (4.18); by
(6.1) and (6.5), (prod (b + h_i), W) = 1, so (4.19) holds. "We conclude
that there exists some n in (N, 2N] with n == b mod W and some set
{i_1,...,i_{m+1}} such that |H_i(n) cap P| = 1 for all i in
{i_1,...,i_{m+1}}, |H_i(n) cap P| <= 1 for all i_1 < i < i_{m+1}."

The sieve-out identity (p. 23, verbatim):

> "For any n > y such that n == b mod W, (6.1) implies that
>   (n, n + z] cap P = H(n) cap P,
> because if g in (0, z] and g not in {h_1,...,h_k}, we have g + n ==
> a_p - a_p == 0 mod p for some p <= w with p not in Z. The primes in H(n)
> are therefore consecutive primes. Therefore there are indices J(1) < ...
> < J(m+1) for which |H_{J(i)}(n) cap P| = 1 and the primes counted here
> form a sequence of m+1 consecutive primes. Thus, by (6.4), and since
> N <= n + h_i <= 3N, we have for some r that
>   ( p_{r+i+1} - p_{r+i} ) / log p_{r+i} =
>   beta_{J(i+1)} - beta_{J(i)} + o(1),   (6.6)
> for 1 <= i <= m."

Limit-point extraction by pigeonhole (p. 23, verbatim):

> "Letting N tend to infinity, we see that for infinitely many r there
> exists some 1 <= J(1) < ... < J(m+1) <= 8m^2 + 8m such that (6.6) holds.
> Since there are at most O_k(1) distinct ways to choose the indices J(i),
> at least one pattern of indices occurs infinitely often. For that pattern
> we have (6.6) for infinitely many r, and so (beta_{J(2)} - beta_{J(1)},
> ..., beta_{J(m+1)} - beta_{J(m)}) in L_m."

Deduction of Theorem 1.1 (p. 24, verbatim):

> "The argument is essentially the same as that for Theorem 1.3, but uses
> part (i) Theorem 4.3 instead of part (ii). We take k to be a sufficiently
> large multiple of 9 x 17. Given beta_9 >= ... >= beta_1 >= 0, we
> construct H as before and form a partition H = H_1 cup ... cup H_9, so
> that each H_i has size k/9 and all elements of H_i have size (beta_i +
> eps + o(1)) log N. Applying part (i) of Theorem 4.3 (with m = 1) then
> shows that there is an n in (N, 2N] such that |H_i(n) cap P| >= 1,
> |H_j(n) cap P| >= 1 for some 1 <= i < j <= 9. As before, our
> construction shows that there are no other primes in [n, n + z], and so
> there must be two consecutive primes p_r, p_{r+1} of the form n + h,
> n + h' with h, h' in different sets H_i. But then we have
>   ( p_{r+1} - p_r ) / log p_r = beta_j - beta_i + o(1),
> for some i < j. Since this occurs for every large N, we obtain the
> result."

[TRANSCRIPTION-UNSURE: "a sufficiently large multiple of 9 x 17" -- the
printed factor is clearly "9 x 17" (= 153), although Theorem 4.3 with
m = 1 requires a multiple of (8m+1)(8m^2+8m) = 9 x 16 = 144; transcribed
exactly as printed.]

---

## 7. CONCLUDING REMARKS (Section 7, p. 24, verbatim)

> "If the statement of Theorem 4.2 held with an arbitrary fixed theta in
> (0,1), then one could apply a minor adaptation of the Maynard-Tao
> argument to show that given beta_1, ..., beta_5, there are infinitely
> many n such that at least two of the integers in {n + h_1, ..., n + h_5}
> are primes with h_i approx beta_i log n, and so we could take k = 5 in
> Theorem 1.1. This would give lambda([0,T] cap L) >= (1 - o(1)) T/4 as
> T -> infty, and lambda([0,T] cap L) >= 3T/25 for all T >= 0, in place of
> (1.3) and (1.4)."

> "We can replace the logarithm in (6.6), hence in Theorems 1.1 and 1.3, by
> a function f : [N_0, infty) -> [1, infty) that is a monotone, strictly
> increasing, unbounded and satisfies f(N) <= log N and f(2N) - f(N) << 1
> for all N >= N_0. In fact we can let f(N)/log N tend to infinity slowly
> (as fast as log_3 N / log_4 N)."

[TRANSCRIPTION-UNSURE: "we can let f(N)/log N tend to infinity slowly" as
printed; dimensionally this should be "log N / f(N) tend to infinity
slowly" (i.e. f slightly smaller than log N by a factor up to
log_3 N/log_4 N); transcribed as printed.]

> "It is possible to improve upon this, and it would be of interest to see
> how fast f(N) can grow while Theorem 1.1 remains valid. This question has
> recently been addressed by Pintz [16]."

References of load-bearing use (p. 24-25): [13] Maynard, "Small gaps
between primes", to appear Ann. of Math.; [17] Polymath, "Variants of the
Selberg sieve, and bounded intervals containing many primes"
(arXiv:1407.4897), 2014; [2] Chang, "Short character sums for composite
moduli"; [14] Montgomery, Topics in multiplicative number theory; [9]
Goldston-Ledoan "Limit points of normalized consecutive prime gaps," to
appear; [15] Pintz arXiv:1305.6289; [16] Pintz arXiv:1407.2213.

---

## COMMENTARY (assessment, NOT extraction)

Focus question answers, with anchors, then assessment against the
exchange-configuration target.

(1) Main theorems and the exact measure fraction. Theorem 1.1 (p. 2): for
any 9 nonnegative reals, some difference beta_j - beta_i lies in L (1.2).
Corollary 1.2 (p. 2): lambda([0,T] cap L) >= (1 - o(1)) T/8 ineffectively
(1.3) and > T/22 effectively (1.4); "12.5%" appears in the abstract and
above Corollary 1.2. Theorem 1.3 (p. 3): for chains of m consecutive
normalized gaps, with k = 8m^2 + 8m prescribed reals, some
consecutive-difference vector from S_m(beta) lies in L_m (1.5).

(2) The "bins" argument. The word "bins" does not occur in the text; the
structure is: (a) Lemma 5.2 builds, at scale y = eps log N, an
Erdos-Rankin residue system {a_p : p <= y, p not in Z} whose unsifted set
in (0, z] is EXACTLY a k-tuple of primes h_i placed in the disjoint
intervals ("bins") (u_i, u_i + Delta], u_i = beta_i x y + y, of width
Delta = y e^{-(log y)^{1/4}} (p. 22, displays after (5.16)); positional
accuracy (5.9). (b) In the deduction (Section 6), the beta-vector repeats
each target value k/(8m^2+8m) times, so the tuple clusters into 8m^2+8m
groups H_j at heights (beta_j + eps + o(1)) log N (6.3)-(6.4). (c) Theorem
4.3(ii) forces >= m+1 singly-occupied groups with no doubly-occupied group
in between (4.21). (d) The sieve-out identity (n, n+z] cap P = H(n) cap P
(p. 23) makes those primes consecutive, giving (6.6). (e) A pigeonhole
over the O_k(1) index patterns J, along N -> infty, yields one pattern
infinitely often, hence a point of L_m (p. 23).

(3) The uniform Maynard-Tao theorem. It is Theorem 4.3 (p. 10), proved in
this paper (Section 4.2, pp. 11-17), not cited from elsewhere. Uniformity:
w = eps log N, W = prod_{p <= w, p !| Z_{N^{4 eps}}} p (4.15), so W is a
small power of N; tuple entries may be as large as N (4.16); but m, k, eps
are FIXED and N >= N(m,k,eps). Extra hypotheses relative to classical
Maynard-Tao: the smoothness condition (4.17) on all differences h_j - h_i
(removable "in principle", p. 11), the equal-size partitions (4.18), and
the coprimality (4.19). The distribution input is Theorem 4.2 (p. 8), a
Bombieri-Vinogradov variant for moduli that are multiples of q_0 < N^eps
with P^+(q_0) < N^{eps/log_2 N}, coprime to the exceptional Z_{N^{2 eps}},
with the loss only phi(q_0) (4.10); it rests on Lemma 4.1 (Chang-based
zero-free region for smooth moduli, (4.6)-(4.7)).

(4) k = k(m) for chains. CONFIRMED VERBATIM: Theorem 1.3 (p. 3) reads "For
any sequence of k = 8m^2 + 8m nonnegative real numbers". The secondary
sources' formula is exactly this paper's count of prescribed reals. Note
the distinct tuple-size parameter: Theorem 4.3 needs the ACTUAL admissible
tuple H of size a sufficiently large multiple of (8m+1)(8m^2+8m) (p. 10),
and via (4.4) the general-m Maynard-Tao input needs k_tuple >= e^{4m+c}
(p. 7). Also the two partition cardinalities 8m+1 and 8m^2+8m in (4.18).

(5) Prescribed vs approximated; scales. Gap values are NEVER hit exactly:
(6.6) gives normalized gaps beta_{J(i+1)} - beta_{J(i)} + o(1), and
membership in L_m is extracted only as a limit along a subsequence of
scales on which one pigeonholed index pattern recurs (p. 23). Which
differences are realized is NOT chosen: only "at least one" pattern out of
S_m(beta) (Theorems 1.1/1.3). What IS prescribed exactly: the candidate
POSITIONS h_i, to accuracy O(y e^{-(log y)^{1/4}}) inside bins at
beta_i log N + eps log N (5.9), (6.4), and the total sieve-out of the
window: (n, n+z] cap P = H(n) cap P (p. 23). Scales: n in (N, 2N], primes
in (N, 3N] ("N <= n + h_i <= 3N", p. 23); window length z =
y (log_2 y)(2 log_3 y)^{-1} with y = eps log N, i.e. z \asymp
log N log_3 N / log_4 N -- a Rankin-factor beyond the mean gap. For
Theorem 1.1 the two-primes-in-different-bins event happens "for every
large N" (p. 24); the pair (i,j) may vary with N.

Assessment for the exchange-configuration target (two gap-word sites with
matched J-prefix/K-suffix windows and dominant weighted middle difference
at depths J, K ~ log_2 log x):

(A) What this machinery CAN supply, unconditionally:
  - Same-scale, same-residue PAIRS of sites: Theorem 4.3 produces n_1 and
    n_2 in (N, 2N], BOTH == b mod W, for the SAME tuple H and the same
    Erdos-Rankin system (4.20)-(4.21). By the sieve-out identity (p. 23),
    the windows (n_1, n_1+z] and (n_2, n_2+z] have IDENTICAL admissible
    skeletons: primes can only sit at the same relative offsets H at both
    sites. This is a genuine matched-window primitive: the composite
    structure (the "word alphabet" of allowed gap endpoints) is forced
    equal at two distinct sites at every large scale N.
  - Sharp positional prescription of the skeleton: bins of relative width
    e^{-(log y)^{1/4}} (p. 22), far finer than any fixed power of
    1/log log; the weighted "middle difference" can be made dominant BY
    CONSTRUCTION at the skeleton level, simply by choosing the beta_i
    (Lemma 5.2 allows arbitrary beta_k >= ... >= beta_1 >= 0 with z-window
    constraint (5.5)).
  - A counting inequality that is NOT blind pigeonhole: the S' device
    (p. 17) lower-bounds the number of singly-occupied groups by
    m + 1 + mr where r counts multiply-occupied groups -- a
    variability-sensitive weighted count. This partially answers blocker
    (i): Maynard-Tao weights can encode penalties on unwanted
    configurations (here: double occupancy between the endpoints) and
    still close positively, via the fourth functional L_k(F) and the
    Polymath-suggested sieve upper bound (p. 14). This is the one
    structural idea in the paper that goes beyond "some pattern occurs".

(B) What it CANNOT supply toward the target:
  - Occupancy is existential, not prescribable. (4.20)/(4.21) guarantee
    SOME m+1 occupied groups; which groups, and which of the k/(8m^2+8m)
    candidates inside a group, is uncontrolled. Matching a prescribed
    J-prefix and K-suffix occupancy at TWO sites is exactly a two-site
    prime-tuple lower bound -- the parity-blocked blocker (ii). The paper
    itself only ever extracts one recurring pattern by pigeonhole over
    O_k(1) patterns (p. 23), i.e. exactly the blindness of blocker (i) at
    the final step.
  - Depth is fixed, not ~ log_2 log x. Theorem 4.3 fixes m, k, eps before
    N ("Let m, k and eps = eps(k) be fixed", p. 10); the tuple size needed
    is >= e^{4m+c} (p. 7), so even formally, chain depth m growing like
    log_2 log x would demand tuple size (log log x)^{4/log 2 + o(1)} and,
    much worse, uniformity of Lemmas 4.4-4.6 and Theorem 4.2 in k, m
    growing with N. NO uniformity of m or k with N is claimed anywhere in
    this text (NOT FOUND). The o(1) in (6.6) and the thresholds
    N(m, k, eps), y(beta, k) are all fixed-parameter.
  - No site-count lower bound. Both parts of Theorem 4.3 assert "There is
    some n" in a progression b mod W of density W^{-1} ~ N^{-eps(1+o(1))};
    no lower bound on the NUMBER of such sites at scale N is stated, so
    Shiu-type density bookkeeping (blocker (iii)) is not improved by
    anything stated here; the sites live inside one sparse residue class
    chosen by the Erdos-Rankin system.
  - Gap values are approximate (o(1) in units of log N) and normalized by
    log p_r; exact rational/dyadic gap prescriptions (as a binary-digit
    argument would want) are out of reach of this scheme by design -- it
    manufactures limit points, not exact gap words.

(C) Net reading for the project: the exportable assets are (i) the
two-site/same-skeleton primitive (Theorem 4.3 with the sieve-out identity,
p. 23) -- the closest thing in the unconditional literature to "two sites
with matched windows", though matched only at the level of ALLOWED
positions, not realized gap words; (ii) the S'-type weighted count
(p. 17), showing Maynard-Tao weights can enforce structured occupancy
constraints (no interior double occupancy) rather than bare counts; (iii)
the modified Bombieri-Vinogradov for W-divisible moduli (Theorem 4.2) with
only a phi(q_0) loss, which is the enabling distribution input for any
scheme that wants sieve control inside an Erdos-Rankin-prepared residue
class at modulus N^eps. The fundamental gaps relative to the target remain
depth (fixed m vs m ~ log_2 log x) and pattern selection (pigeonhole /
parity), and this paper adds no mechanism against either at growing depth.
