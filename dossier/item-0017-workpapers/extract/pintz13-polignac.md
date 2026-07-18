# EXTRACTION: Pintz, "Polignac Numbers, Conjectures of Erdos on Gaps between Primes, Arithmetic Progressions in Primes, and the Bounded Gap Conjecture"

Source (only evidence base): /home/istr/pro/erdos251/dossier/1305.6289v1.pdf
arXiv:1305.6289v1 [math.NT] 27 May 2013. Author: Janos PINTZ, Renyi
Mathematical Institute of the Hungarian Academy of Sciences, Budapest,
Realtanoda u. 13-15, H-1053 Hungary, e-mail: pintz@renyi.hu. 14 pages
(pp. 1-11 text, pp. 12-14 references). Footnote p. 1: "Supported by OTKA
grants K 100291, NK 104183 and ERC-AdG. 228005."

Transcription conventions: ASCII only. Diacritics transliterated (Erdos,
Yildirim, Turan, Renyi, Revesz, Gyory, Cramer). Math in LaTeX-like ASCII:
<= , >= , << (Vinogradov, "\ll"), <<_k (implied constant depends on k),
\prod, \sum, liminf/limsup, phi = Euler phi, mu = Moebius mu. The paper's
Gothic \mathfrak{S}(H) (singular series) is written S(H); the paper's
script-P (set of primes) is written P; the paper's calligraphic H (tuple)
is written H; script D_s, D_w kept as D_s, D_w; vartheta (distribution
level) written theta. d_n = p_{n+1} - p_n. P^-(m) = smallest prime factor
of m. Anchors are theorem/equation/section numbers as printed; page numbers
(printed = PDF page) are secondary aid. Everything up to the final marked
section is EXTRACTION (what the paper says); paraphrase is explicitly
marked [PARAPHRASE]. Commentary appears ONLY in the final marked section.

---

## 1. ABSTRACT AND INTRODUCTION (verbatim)

Abstract (p. 1), verbatim:

> "In the present work we prove a number of surprising results about gaps
> between consecutive primes and arithmetic progressions in the sequence of
> generalized twin primes which could not have been proven without the
> recent fantastic achievement of Yitang Zhang about the existence of
> bounded gaps between consecutive primes. Most of these results would have
> belonged to the category of science fiction a decade ago. However, the
> presented results are far from being immediate consequences of Zhang's
> famous theorem: they require various new ideas, other important
> properties of the applied sieve function and a closer analysis of the
> methods of Goldston-Pintz-Yildirim, Green-Tao, and Zhang, respectively."

Section 1.1 (p. 1), verbatim:

> "Very recently Yitang Zhang, in a fantastic breakthrough solved the
> Bounded Gap Conjecture, a term formulated in recent works of mine, often
> in collaboration with D. Goldston and C. Yildirim. Let p_n denote the
> n^th prime, P the set of all primes and
> (1.1)  d_n = p_{n+1} - p_n
> the n^th difference between consecutive primes."

> "Theorem A (Y. Zhang [28, 2013]). liminf_{n->infty} d_n <= 7 * 10^7."

> "Theorem B ([11, 2009]). If the primes have a distribution level
> theta > 1/2, then with a suitable explicit constant C(theta) we have
> (1.2)  liminf_{n->infty} d_n <= C(theta).
> If the Elliott-Halberstam Conjecture (EH) is true, i.e. theta = 1 or, at
> least, theta > 0.971 then
> (1.3)  liminf_{n->infty} d_n <= 16."

Level of distribution (p. 2), verbatim:

> "We say that theta is a level of distribution of primes if
> (1.4)  \sum_{q <= X^{theta - eps}} max_{a, (a,q)=1}
>        | \sum_{p == a (mod q), p <= X} log p - X/phi(q) |
>        <<_{A,eps} X/(log X)^A
> for any A, eps > 0."

Zhang's two devices (p. 2), verbatim:

> "Zhang could not prove (1.4) with a level > 1/2 but showed that
> (i) it is possible to neglect in (1.4) all moduli q with a prime divisor
> > X^b, where b is any constant, and
> (ii) managed to show for these smooth moduli a result which is similar
> but weaker than the analogue of (1.4) with theta = 1/2 + 1/584, which,
> however suits to apply our method of Theorem B."

Purpose sentence (p. 2), verbatim:

> "The purpose of the present work is to show that most of these
> conditional results can be shown unconditionally using Zhang's fantastic
> result [28, 2013] or in some sense, his method, coupled with other
> ideas."

---

## 2. SECTION 2: HISTORY AND ALL MAIN THEOREMS (verbatim)

### 2.1 Approximations to the Twin Prime Conjecture (Section 2.1, p. 2)

> "Twin Prime Conjecture. liminf_{n->infty} d_n = 2."

Delta_1 := liminf_{n->infty} d_n / log n (eq. (2.1), p. 2). Hardy and
Littlewood 1926 (unpublished, see [24, 1940]) showed Delta_1 <= 2/3 under
GRH. Erdos [5, 1940] first unconditionally: "(2.2) Delta_1 < 1 - c_0,
c_0 > 0" "with an unspecified but explicitly calculable positive constant
c_0." Then (p. 2):

> "(2.3)  Delta_1 < 0.4666  (Bombieri, Davenport [1, 1966]),
>  (2.4)  Delta_1 < 0.2485  (H. Maier [17, 1988])."

> "Theorem C ([11, 2009]). Delta_1 = 0."

> "Theorem D ([12, 2010]). We have
> (2.5)  liminf_{n->infty} d_n / ( (log n)^{1/2} (log log n)^2 ) < infty."

> "Theorem E ([21, 2013]).
> (2.6)  liminf_{n->infty} d_n / ( (log n)^{3/7} (log log n)^{4/7} )
>        < infty."

(p. 3): "In a joint work with B. Farkas and Sz. Gy. Revesz [9, 2013] we
also showed that essential new ideas are necessary to improve (2.6)."

### 2.2 Polignac numbers (Section 2.2, p. 3), verbatim

> "Definition 1. A positive even number 2k is a strong Polignac number, or
> briefly a Polignac number if d_n = 2k for infinitely many values of n."

> "Definition 2. A positive even number 2k is a weak Polignac number if it
> can be written as the difference of two primes in an infinitude of ways."

> "The set of (strong) Polignac numbers will be denoted by D_s, the set of
> weak Polignac numbers by D_w. (We have trivially D_s <= D_w.)"

[The containment symbol printed is a "subset or equal" sign; rendered here
as <= . -- PARAPHRASE note only.]

> "Polignac's Conjecture ([23, 1849]). Every positive even integer is a
> (strong) Polignac number."

> "Proposition. The following three statements are equivalent:
> (i) the Bounded Gap Conjecture is true;
> (ii) there is at least one (strong) Polignac number, i.e. |D_s| >= 1;
> (iii) there is at least one weak Polignac number, i.e. |D_w| >= 1."

Framing sentence (p. 3), verbatim: "The above very simple proposition
shows that the Bounded Gap Conjecture itself leaves still many problems
open about Polignac numbers or weak Polignac numbers, but solves the
crucial problem that their set is nonempty. We will prove several
unconditional results about the density and distribution of (strong)
Polignac numbers."

> "Theorem 1. There exists an explicitly calculable constant c such that
> for N > N_0 we have at least cN Polignac numbers below N, i.e. Polignac
> numbers have a positive lower asymptotic density."

> "Theorem 2. There exists an ineffective constant C' such that every
> interval of type [M, M + C'] contains at least one Polignac number."

> "Remark. As mentioned earlier, the term Polignac number means always
> strong Polignac numbers."

### 2.3 The normalized value distribution of d_n (Section 2.3, p. 4)

> "The Prime Number Theorem implies
> (2.7)  lim_{N->infty} (1/N) \sum d_n / log n = 1,"

[The summation range is not printed under the Sigma in (2.7).
TRANSCRIPTION-UNSURE: presumably n <= N.]

> "so it is natural to investigate the series d_n/log n. Denoting by J the
> set of limit points of d_n/log n, Erdos [7, 1955] conjectured
> (2.8)  J = { d_n / log n }' = [0, infty]."

(p. 4): "While Westzynthius [27, 1931] proved more than 80 years ago that
infty in J, no finite limit point was known until 2005 when we showed the
Small Gap Conjecture, i.e. Theorem C [11, 2009], which is equivalent to
0 in J." And: "Interestingly enough Erdos [7, 1955] and Ricci [25, 1954]
proved independently about 60 years ago that J has a positive Lebesgue
measure. What I can show is a weaker form of Erdos's conjecture (2.8)."

> "Theorem 3. There is an ineffective constant c > 0 such that
> (2.9)  [0, c] subset J."

(p. 4): "Kalman Gyory asked me at the Turan Memorial Conference in
Budapest, 2011 whether it is possible to find a form of the above result
which gives answers about the more subtle value-distribution of d_n if we
use a test-function f(n) <= log n, f(n) -> infty as n -> infty."

> "Definition 3. Let F denote the class of functions f : Z^+ -> R^+ with a
> slow oscillation, when for every eps > 0 we have an N(eps) > 0 such that
> (2.10)  (1 - eps) f(N) <= f(n) <= (1 + eps) f(N)  for  N <= n <= 2N,
>         N > N(eps)."

> "Theorem 4. For every function f in F, f(n) <= log n,
> lim_{n->infty} f(n) = infty we have an ineffective constant c_f > 0 such
> that
> (2.11)  [0, c_f] subset J_f := { d_n / f(n) }'."

### 2.4 Comparison of two consecutive values of d_n (Section 2.4, p. 4)

(p. 4): "Erdos and Turan proved 65 years ago [8, 1948] that d_{n+1} - d_n
changes sign infinitely often. This was soon improved by Erdos [6, 1948]
to
(2.12)  liminf_{n->infty} d_{n+1}/d_n < 1 < limsup_{n->infty}
d_{n+1}/d_n."

> "Erdos [7, 1955] wrote seven years later: 'One would of course
> conjecture that
> (2.13)  liminf_{n->infty} d_{n+1}/d_n = 0,
>         limsup_{n->infty} d_{n+1}/d_n = infty,
> but these conjectures seem very difficult to prove.'
> In Section 6 I will show this in a much stronger form:"

> "Theorem 5. We have
> (2.14)  liminf_{n->infty} (d_{n+1}/d_n) / (log n)^{-1} < infty
> and
> (2.15)  limsup_{n->infty} (d_{n+1}/d_n) / log n > 0."

### 2.5 Arithmetic progressions in the sequence of generalized twin primes (Section 2.5, p. 5)

> "Theorem 6. There is a d <= 7 x 10^7 such that there are arbitrarily
> long arithmetic progressions of primes with the property that
> p' = p + d is the prime following p for each element of the
> progression."

---

## 3. SECTION 3: PREPARATION -- DHL(k,2), DHL*(k,2), MAIN THEOREM

### 3.1 Admissibility and singular series (Section 3, p. 5), verbatim

> "All the proofs use some modified form of the conjecture of Dickson [3,
> 1904] about k-tuples of primes. (His original conjecture referred for
> linear forms with integer coefficients.) Let H = {h_i}_{i=1}^k be a
> k-tuple of different non-negative integers. We call H admissible, if
> (3.1)  P_H(n) = \prod_{i=1}^k (n - h_i)
> has no fixed prime divisor, that is, if the number nu_p(H) of residue
> classes covered by H mod p satisfies
> (3.2)  nu_p(H) < p  for  p in P.
> This is equivalent to the fact that the singular series
> (3.3)  S(H) = \prod_p (1 - nu_p(H)/p) (1 - 1/p)^{-k} > 0."

[TRANSCRIPTION-UNSURE: the sign inside the product in (3.1) reads as a
minus, (n - h_i), while (3.5) below clearly prints (n + h_i); the glyph in
(3.1) is small and could be a plus.]

> "Hardy and Littlewood [16, 1923], probably unaware of Dickson's
> conjecture, formulated a quantitative version of it, according to which
> (3.4)  pi_H(x) = \sum_{n <= x, n + h_i in P (1 <= i <= k)} 1
>        = (S(H) + o(1)) x / log^k x."

### 3.2 DHL(k,2) (Section 3, p. 5), verbatim

> "Conjecture DHL (k,2). If H is an admissible k-tuple, then n + H
> contains at least two primes for infinitely many values of n."

(p. 5): "It is clear that if DHL(k,2) is proved for any k (or even for
any single k-tuple H_k), then the Bounded Gap Conjecture is true.
DHL(k,2) was shown very recently by Y. T. Zhang [28, 2013] for
k >= k_0 = 3.5 x 10^6 and this implied his Theorem A, the infinitude of
gaps of size <= 7 * 10^7."

Why DHL(k,2) is not enough (pp. 5-6), verbatim:

> "However, results of this type cannot exclude the existence of other
> primes and therefore give information on numbers expressible as
> difference of two primes, in the optimal case of Zhang's very strong
> Theorem A prove the existence of many weak Polignac numbers. However,
> they do not provide more information about (strong) Polignac numbers
> than the very deep fact that D_s != emptyset and they do not help in
> showing any of Theorems 1-6."

(p. 6, continuing): "For example, in case of Theorem 6 they do not yield,
let say, 4-term arithmetic progressions of primes and a bounded number d
such that p + d should also be prime for all four elements of the
progression (even if we do not require that p and p + d should be
consecutive primes)."

### 3.3 DHL*(k,2) -- the definition (Section 3, p. 6), verbatim

> "In view of Zhang's recent result the stronger form of Conjecture
> DHL(k,2) will obtain already the name Theorem DHL*(k,2) for large enough
> k and can be formulated as follows, first still as a conjecture for
> k < 3.5 * 10^6.
> Let P^-(m) denote the smallest prime factor of m."

> "Conjecture DHL* (k,2). Let k >= 2 and H = {h_i}_{i=1}^k be any
> admissible k-tuple, N in Z^+, eps > 0 sufficiently small (eps < eps_0)
> (3.5)  H subset [0,H],  H <= eps log N,
>        P_H(n) = \prod_{i=1}^k (n + h_i).
> We have then positive constants c_1(k) and c_2(k) such that the number
> of integers n in [N,2N) such that n + H contains at least two
> consecutive primes and almost primes in each components (i.e.
> P^-(P_H(n)) > n^{c_1(k)}) is at least
> (3.6)  c_2(k) S(H) N / log^k N  for N > N_0(H)."

[Note: the same letter H denotes both the tuple (calligraphic in print)
and the window length (italic in print); transcription keeps both as H,
context disambiguates. The three gains over DHL(k,2), verbatim (p. 6):]

> "One can see that we have a looser condition than in DHL(k,2) as far as
> the elements of H are allowed to tend to infinity as fast as eps log N.
> On the other hand we get stronger consequences as
> (i) we can prescribe that the two primes n + h_i and n + h_j in our
> k-tuple should be consecutive;
> (ii) we have almost primes in each component n + h_i;
> (iii) we get the lower estimate (3.6) for the number of the required n's
> with the above property.
> The condition n in [N,2N) makes usually no problem but in case of the
> existence of Siegel zeros some extra care is needed if we would like to
> have effective results (see Section 8 for this)."

### 3.4 MAIN THEOREM (Section 3, p. 6), verbatim

> "MAIN THEOREM. Conjecture DHL*(k,2) is true for k >= 3.5 * 10^6."

Proof opening (p. 6), verbatim: "Since this result contains Zhang's
Theorem and even more, it is easy to guess that a self contained proof
would be hopelessly long (and difficult). We therefore try to describe
only the changes compared to different earlier works."

The four pillars [PARAPHRASE of pp. 6-7 structure, with verbatim quotes]:

Pillar 1 (p. 6), verbatim: "The first pillar of Zhang's work is the
method of proof of our Theorem B. Although he supposes H as a constant
the method of proof of Theorem B (see Propositions 1 and 2 in [11, 2009])
allow beyond H << log N (required by (3.5) above) the much looser
condition H << N^{1/4 - eps} for any eps > 0."

Pillar 2 (pp. 6-7), verbatim: "The second pillar of Zhang's work is to
show that distribution of primes according to non-smooth moduli, i.e.
without any prime divisor > N^b for any fixed small constant b, can be
neglected. As mentioned in the Introduction we showed this already much
earlier in a joint work with Y. Motohashi [18, 2008]. This work also
supposed H to be a constant but the only place where actually more care
is needed in the proof is (3.11) of [18, 2008]. On the other hand,
allowing here the condition
(3.7)  H << log N,
the same simple argument as in Section 6 of [11, 2009] adds an additional
error term
(3.8)  k^2 log log log R << log log log R
to the right-hand side of (3.11) of [18, 2008] which is far less than the
present error term log R_0 = log R/(log log R)^5. Otherwise the proof
works without any change, everything remains uniform under our condition
(3.7) above."

[TRANSCRIPTION-UNSURE: display (3.8) as printed appears to read
"k^2 log log log R << log log log R", which is odd (same quantity on both
sides up to k^2); small glyphs -- the right-hand side might differ.]

Remark after (3.8) (p. 7), verbatim:

> "Remark. The crucial Lemmas 3 and 4 of our work [18, 2008] contain an
> additional factor gamma(n,H). However, by the definition (4.17) of [18,
> 2008] we have gamma(n,H) = 1 if P^-(P_H(n)) > R^eta for any fixed
> eta > 0. In such a way the extra factor gamma(n,H) does not affect the
> validity of our Lemma 2 below since the asymptotic provided by Lemma 3
> for the right-hand side of (3.11) (and similarly the analogue of it for
> primes, Lemma 4) is the same as if we used the constant weight 1 instead
> of gamma(n,H)."

Pillar 3 (p. 7), verbatim: "No change is required in the third pillar of
Zhang's work where he proves some sort of extension of the
Bombieri-Vinogradov theorem for smooth moduli and the residue classes
appearing by the method of Theorem B."

Pillar 4 = Lemmas 1-2 (p. 7), introduction verbatim: "However, the proof
of Theorem DHL*(k,2) (for k large enough, k >= 3.5 * 10^6) requires a
further important idea, namely Lemmas 3-4 of the author's work [19,
2010]. This we formulate now as"

---

## 4. LEMMAS 1-4 (Section 3, pp. 7-8), verbatim

> "Lemma 1. Let N^{c_0} < R <= sqrt(N/p) (log N)^{-C}, p in P,
> p < R^{C_0} with a sufficiently small positive c_0 and sufficiently
> large C. Then we have with the notation
> (3.9)  Lambda_R(n; H, k + ell) = 1/(k + ell)!
>        \sum_{d <= R, d | P_H(n)} mu(d) (log R/d)^{k + ell}
>        (ell <= k)
> the relation
> (3.10)  \sum_{n in [N,2N), p | P_H(n)} Lambda_R(n; H, k + ell)^2
>         <<_k (log p / (p log R))
>         \sum_{n in [N,2N)} Lambda_R(n; H, k + ell)^2."

[TRANSCRIPTION-UNSURE: the exponent in "p < R^{C_0}" -- the subscripted
letter could be capital C_0 or lower-case c_0; only c_0 ("sufficiently
small") and C ("sufficiently large") are introduced in the hypothesis
clause.]

> "Lemma 1 immediately implies"

> "Lemma 2. Let N^{c_0} < R <= N^{1/(2+eta)} (log N)^{-C}, eta > 0. We
> have then
> (3.11)  \sum_{n in [N,2N), P^-(P_H(n)) < R^{eta}}
>         Lambda_R(n; H, k + ell)^2
>         <<_k eta \sum_{n in [N,2N)} Lambda_R(n; H, k + ell)^2."

> "Remark. Lemmas 1 and 2 were already proved in [19, 2010] under the
> loose condition H << log N."

Interpretation sentence (p. 7), verbatim:

> "Lemma 2 asserts that numbers n where P_H(n) has a prime factor
> < R^{eta} (equivalently < N^b) with a small enough value of eta (or b)
> might be neglected, since the weight used in all proofs is actually of
> type (3.9). The value of eta (or b) depends on k."

(p. 7): "These results play a crucial role in the common generalization
of the Green-Tao theorem and of our Theorem B (cf. [19, 2010]) and also
in the proof that prime gaps < eps log p form a positive proportion of
all gaps for any eps > 0 (proved in a joint work with Goldston and
Yildirim)."

### Lemma 3 -- the Selberg-sieve upper bound (Section 3, p. 7), verbatim

Lead-in sentence (p. 7), verbatim: "These four pillars lead finally to
the stronger form of Theorem DHL*(k,2) if we combine it with a standard
assertion following from Selberg's sieve, which we can formulate in this
special case as"

> "Lemma 3. Let 0 < alpha < 1/2 be any constant. Then
> (3.12)  \sum_{n in [N,2N), P^-(P_H(n)) > N^{alpha}} 1
>         <<_k (N alpha^{-k} / log^k N) S(H)."

Proof (p. 8), verbatim:

> "Proof. This is Theorem 5.1 of [15, 1974] or Theorem 2 in Sec. 2.2.2 of
> [13, 2001]. This is also valid if we assume only H << log N."

[The section sign in "Sec. 2.2.2" is a printed paragraph symbol. The two
sources, from the References (p. 13): [15] H. Halberstam, H.-E. Richert,
Sieve methods, Academic Press, New York, 1974; [13] G. Greaves, Sieves in
Number Theory, Springer, Berlin, 2001.]

### Lemma 4 -- Gallagher-type averaging of singular series (p. 8), verbatim

> "We further need a generalization of Gallagher's theorem proved by the
> author which we formulate as"

> "Lemma 4. Let H_k be an arbitrary admissible k-tuple with
> (3.13)  H = H_k <= [0, H].
> Then we have for any eta > 0
> (3.14)  S_H(H) := (1/H) \sum_{h=1}^{H} S(H union h)/S(H) = 1 + O(eta)
> if
> (3.15)  H >= exp(k^{1/eta})."

> "Proof. This is Theorem 1 of [20, 2010]."

[[20] = J. Pintz, On the singular series in the prime k-tuple conjecture,
arXiv: 1004.1084v1 [math.NT] (References p. 13). The containment in
(3.13) is the same "subset or equal" sign as before.]

> "Remark. As it is easy to see Lemma 4 implies Gallagher's classical
> theorem [10, 1976] on the singular series."

---

## 5. PROOF OF THE MAIN THEOREM: THE CONSECUTIVIZATION MECHANISM (Section 3, pp. 8-9), verbatim

Step 1 -- two primes + almost primes with lower bound (p. 8), verbatim:

> "Combining the proofs of Theorems A and B (in the modified forms
> mentioned above) with the assertion of Lemma 2 we obtain under the
> weaker condition (3.6), i.e. for all admissible k-tuples
> H_k = {h_i}_{i=1}^k, h_i < h_{i+1},
> (3.16)  H = H_k <= [0, eps log N],
> at least
> (3.17)  c_2(k) S(H) N / log^k N
> numbers n in [N,2N) such that n + H contains at least two primes and
> almost primes in each components, i.e.
> (3.18)  P^-(P_H(n)) > n^{c_1(k)}.
> However, we must show the same with consecutive primes as well."

Step 2 -- pigeonhole over prime-position patterns V (p. 8), verbatim:

> "We can define for any subset V of {1,2,...,k} the set
> (3.19)  V(N) = { n in [N,2N) :  n + h_i in P <=> i in V }.
> Since k is bounded the number of possible subsets V is also bounded,
> therefore we can choose a V_0 such that
> (3.20)  V_0 subset {1,2,...,k},  |V_0| >= 2,
>         |V_0(N)| >= c_3(k) S(H) N / log^k N."

[The relation in (3.19) is printed as a double arrow (if and only if):
n + h_i is prime exactly for the indices i in V.]

Step 3 -- choose adjacent hits, get compositeness at intermediate tuple
positions (p. 8), verbatim:

> "Choosing two arbitrary consecutive elements i, j in V_0(N) with i < j
> we have at least
> (3.21)  c_3(k) S(H) N / log^k N
> numbers n in [N,2N) such that for any mu in (i,j)
> (3.22)  n + h_mu not in P."

[TRANSCRIPTION-UNSURE: "i, j in V_0(N)" as printed; logically i, j are
consecutive elements of the index set V_0, not of V_0(N).]

Step 4 -- excluding primes at NON-tuple positions between the hits
(pp. 8-9), verbatim:

> "We have to assure, however, additionally that for a positive
> proportion of these numbers n we have also
> (3.23)  n + h not in P  for  h not in H,  h_i < h < h_j."

> "Applying Lemma 3 for all these values h and summing up we arrive at
> the conclusion that
> (3.24)  \sum_{n in [N,2N), P^-(P_H(n)) > n^{c_1(k)}}
>         \sum_{h, h_i < h < h_j, n + h in P} 1
>         <= C_4(k) (N / log^{k+1} N) \sum_{h_i < h < h_j} S(H union h)
>         <= 2 C_4(k) N eps S(H) / log^k N
> by Lemma 4. This shows that if eps was chosen sufficiently small
> depending on k, i.e.
> (3.25)  eps < eps_0(k)
> then our original primes n + h_i and n + h_j are consecutive for at
> least
> (3.26)  c_5(k) S(H) N / log^k N
> elements n in [N,2N), thereby showing our Main Theorem."

---

## 6. SECTION 4: POLIGNAC NUMBERS (proofs of Theorems 1 and 2), pp. 9-10

Proof of Theorem 1 (Section 4, p. 9), verbatim:

> "1. Proof of Theorem 1.
> The fact that DHL*(k,2) implies the positivity of the asymptotic lower
> density of Polignac numbers is expressed as Corollary 1 of [19, 2010]
> with the value
> (4.1)  (1/(k(k-1))) \prod_{p <= k} (1 - 1/p)
> and proved in Section 11. The above value is about e^{-gamma}/(k^2 log
> k) for large values of k. (If k -> infty, they are asymptotically
> equal.)"

[The "Section 11" refers to [19, 2010]. -- PARAPHRASE note.]

Proof of Theorem 2 (Section 4, pp. 9-10), verbatim:

> "1. Proof of Theorem 2.
> We again suppose DHL*(k,2) for k >= k_0.
> The reasoning is more intricate in this case and the resulting value C
> is ineffective. The trivial relation
> (4.2)  h_k - h_1 >= (k-1) min_{i>j} (h_i - h_j)  (h_i < h_{i+1})
> even gives the impression that the best we can prove about localization
> of Polignac numbers is an interval of type
> (4.3)  [M, (k-1)M]."

[The section number "1." is printed twice on p. 9 (both proofs are headed
"1."); transcribed as printed.]

> "Let us suppose that Theorem 2 is false. Then we have for any C_0 > 0
> an infinite series of intervals
> (4.4)  I_nu := [M_nu, M_nu + C_nu],  M_nu > C_nu > 4 M_{nu-1},
>        M_1 > C_0
> such that
> (4.5)  D_s intersect ( union_{nu=1}^{infty} I_nu ) = emptyset.
> For p > k we have clearly
> (4.6)  nu_p(H_k) < p  for  p in P,
> so we have no problem of choosing an admissible system H_k in a
> sufficiently long interval (e.g. if C_k is large enough). Let
> (4.7)  H_k := {h_nu}_{nu=1}^k,
>        h_nu in I'_nu := [M_nu + C_nu/2, M_nu + C_nu]."

(p. 10), verbatim:

> "For h_nu in I_nu, h_mu in I_mu, nu < mu we have then
> (4.8)  h_mu - h_nu in [M_mu + C_mu/2 - 2M_{mu-1}, M_mu + C_mu]
>        subset I_mu.
> Since in case of k >= k_0 at least one of the numbers
> (4.9)  h_mu - h_nu  (1 <= nu < mu <= k)
> can be written as a difference of two consecutive primes, (4.8)
> contradicts to (4.5) and thus proves our theorem."

[TRANSCRIPTION-UNSURE: presence/absence of prime marks on "I_nu, I_mu" in
the first line of (4.8)'s hypothesis; the lower endpoint M_mu + C_mu/2 -
2M_{mu-1} requires h_mu in I'_mu as defined in (4.7).]

---

## 7. SECTION 5: THE NORMALIZED VALUE DISTRIBUTION OF d_n (proofs of Theorems 3-4), p. 10

Verbatim:

> "1. Proof of Theorems 3-4.
> Since Theorem 4 implies Theorem 3 it is sufficient to prove the latter.
> The structure of the proof will follow that of Theorem 2 proved in the
> previous section. Suppose that Theorem 4 is false. In this case we have
> for a sufficiently small c* > 0 an infinite series of intervals
> (5.1)  J_nu = [c_nu, c_nu + delta_nu],  c_nu > 4 delta_nu > 20
>        c_{nu+1},  c_1 < c*
> such that for K large enough
> (5.2)  { d_n / f(n) }_{n=N}^{infty} intersect
>        ( union_{nu=1}^{K} J_nu ) = emptyset,  where N = N(K) > 0.
> Let
> (5.3)  I_nu(n) := [c_nu f(n), (c_nu + delta_nu) f(n)],
>        nu = 1,2,...,K.
> Then we have
> (5.4)  d_n not in union_{nu=1}^{K} I_nu(n)  for  nu = 1,2,...,K,
>        n in [N,2N),  N > N(k)."

[TRANSCRIPTION-UNSURE: "N > N(k)" in (5.4) with lower-case k as printed;
elsewhere the parameter is N(K).]

> "Using our Main Theorem, similarly to (4.7) we can construct an
> admissible k-tuple H_k = {h_nu}_{nu=1}^k with 3.5 * 10^6 <= k <= K such
> that h_1 > h_2 > ... > h_k and with a sufficiently small eps > 0
> (5.5)  h_nu in I'_nu(N) := [ (c_nu + delta_nu/2)(1 + eps) f(N),
>        (c_nu + delta_nu)(1 - eps) f(N) ].
> For h_mu in I'_mu, h_nu in I'_nu, mu < nu we have for
> N > max(N(K), N_0(eps))
> (5.6)  h_mu - h_nu in [ (c_mu + delta_mu/2 - 2 c_{mu+1})(1 + eps) f(N),
>        (c_mu + delta_mu)(1 - eps) f(N) ] := I*_mu(N).
> Since we have for any 1 <= mu < nu <= k_0 and any n in [N,2N)
> (5.7)  I*_mu(N) subset I_mu(n),
> the fact that by the Main Theorem h_mu - h_nu = d_n for some
> n in [N,2N), 1 <= mu < nu <= k_0 contradicts to (5.4) and thus proves
> Theorems 3 and 4."

---

## 8. SECTION 6: COMPARISON OF TWO CONSECUTIVE VALUES OF d_n (proof of Theorem 5), p. 11

This is the "one side constructed, partner generic by exclusion" section.
Complete transcription, verbatim:

> "1. Proof of Theorem 5.
> Since the proof of the two inequalities are completely analogous, we
> will only prove the second one. The basis of it is the Main Theorem
> proved in Section 3. We can start with an arbitrary admissible k-tuple
> H = H_k = {h_i}_{i=1}^k, h_1 < h_2 < ... < h_k with k >= 3.5 * 10^6.
> Let with a fixed sufficiently small c_1(k) define
> (6.1)  B(i,j,N) = { n <= N, n + h_i in P, n + h_j in P,
>        P^-(P_H(n)) > n^{c_1(k)} },
> (6.2)  T = { (i,j); j > i, limsup_{N->infty}
>        |B(i,j,N)| log^k N / N > 0 }
> and let us choose the pair (i,j) with maximal value of j, afterwards
> that with maximal value of i < j. Then for any h_mu in (h_i, h_j)
> (i.e. i < mu < j) we have clearly
> (6.3)  limsup_{N->infty} |B(mu,j,N)| log^k N / N = 0
> so all components n + h_mu between n + h_i and n + h_j are almost
> always composite if n in B(i,j,N) and N = N_nu -> infty through a
> suitable sequence N_nu."

> "On the other hand if we have an arbitrary h in (h_i, h_j), h not in H,
> then the assumption n + h in P implies for H^+ = H union h
> (6.4)  P^-(P_{H^+}(n)) > n^{c_1(k)}.
> However, by Lemma 3 the number of such n <= N is for all N
> (6.5)  <<_{k,c_1} S(H union {h}) N / log^{k+1} N
>        <<_{k,c_1} S(H) N log h_k / log^{k+1} N
>        <<_{k,c_1,H} N / log^{k+1} N.
> This, together with (6.3) shows that we have at least
> (6.6)  (c_1(k,H) + o(1)) N / log^k N
> values n <= N with n + h_i, n + h_j being consecutive primes for some
> sequence N = N_nu -> infty."

[TRANSCRIPTION-UNSURE: the constant in (6.6) is printed as c_1(k,H),
colliding notationally with the almost-primality exponent c_1(k) of
(6.1); transcribed as printed.]

> "Let us consider now these differences. Let
> (6.7)  n + h_i = p_nu in P,  n + h_j = p_{nu+1} in P,
>        d_nu = h_j - h_i << 1
> where
> (6.8)  log n ~ log nu ~ log N.
> Suppose now that the second inequality of Theorem 5 is false. Then we
> have for all those values of nu with an arbitrary eps > 0 for
> N > N(eps)
> (6.9)  d_{nu+1} <= d_nu eps log N <= C eps log N,  C = h_k - h_1.
> The already quoted sieve of Selberg (Lemma 3) gives an upper estimate
> how often this might happen for any particular value
> (6.10)  d_{nu+1} = d <= C eps log N.
> Adding it up until C eps log N we obtain at most
> (6.11)  <<_{k,c_1} (N / log^{k+1} N) \sum_{h=1}^{C eps log N}
>         S(H union h)
>         <<_{k,c_1} S(H) C N eps / log^k N
> by Lemma 4. This means that in view of (6.6) this cannot hold for all
> N = N_nu -> infty. This contradiction proves Theorem 5."

---

## 9. SECTION 7: PROOF OF THEOREM 6 (p. 12), verbatim

> "Proof of Theorem 6.
> In this case we have to use again our crucial Main Theorem and the rest
> of the machinery executed in Section 7 of [19, 2010]. This yields the
> combination of Zhang's theorem with that of Green and Tao [14, 2008]."

[This is the entire Section 7.]

---

## 10. SECTION 8: "HOW TO MAKE ZHANG'S THEOREM EFFECTIVE?" (p. 12), verbatim

> "Our last point is that in its original form Zhang's theorem is
> ineffective since it uses Siegel's theorem. His result and similarly to
> it all results of the present work can be made effective in the
> following way.
> According to the famous theorem of Landau-Page there is at most one
> real primitive character chi with a modulus q (and the characters
> induced by it) which might cause ineffectivity in the
> Bombieri-Vinogradov theorem, and this modulus has to satisfy
> (8.1)  (log X)^2 <= q <= (log X)^{omega(X)}
> for any omega(X) -> infty as X -> infty. This modulus can cause any
> problem only in the case
> (8.2)  q | P_H(n).
> However, our Lemma 3 says that we can neglect all numbers n with
> (8.3)  P^-(P_H(n)) < n^{c_1(k)},
> so (prescribing additionally q does-not-divide d in the definition
> (3.9) of Lambda_R(n; H, k, ell)) both Zhang's theorem and all our
> present results become effective."

[TRANSCRIPTION-UNSURE: (i) "our Lemma 3 says that we can neglect all
numbers n with (8.3)" as printed; logically the neglect-of-small-prime-
factor statement is Lemma 2 (Lemma 3 is the upper-bound count of the
non-neglected n). (ii) The argument list "Lambda_R(n; H, k, ell)" appears
printed with a comma between k and ell, whereas (3.9) defines
Lambda_R(n; H, k + ell).]

> "Remark. It is an interesting phenomenon that in the sieving process
> yielding bounded gaps between primes and in all our present results we
> can choose
> (8.4)  lambda_d = 0
> if d has either a prime divisor
> (8.5)  > N^{c'(k)}
> or if it has a prime divisor
> (8.6)  < N^{c''(k)}."

---

## 11. REFERENCES SIGHTED (pp. 12-14) [PARAPHRASE list, titles abridged]

[1] Bombieri-Davenport, Proc. Roy. Soc. Ser. A 293 (1966). [2] van der
Corput, Math. Ann. 116 (1939). [3] Dickson, Messenger of Math. (2) 33
(1904). [4] Elliott-Halberstam, Symposia Mathematica Vol. 4 (1970).
[5] Erdos, Duke Math. J. 6 (1940), 438-441. [6] Erdos, Bull. Amer. Math.
Soc. (1948), 885-889. [7] Erdos, Teoria dei Numeri, Math. Congr. Varenna
1954, 8 pp., 1955. [8] Erdos-Turan, Bull. Amer. Math. Soc. 54 (1948),
371-378. [9] Farkas-Pintz-Revesz, on the optimal weight function in the
GPY method, submitted. [10] Gallagher, Mathematika 23 (1976), 4-9.
[11] Goldston-Pintz-Yildirim, Primes in tuples. I, Ann. of Math. (2) 170
(2009), no. 2, 819-862. [12] Goldston-Pintz-Yildirim, Primes in tuples.
II, Acta Math. 204 (2010), no. 1, 1-47. [13] Greaves, Sieves in Number
Theory, Springer, Berlin, 2001. [14] Green-Tao, Ann. of Math. (2) 167
(2008), no. 2, 481-547. [15] Halberstam-Richert, Sieve methods, Academic
Press, New York, 1974. [16] Hardy-Littlewood, Acta Math. 44 (1923),
1-70. [17] Maier, Michigan Math. J. 35 (1988), 323-344.
[18] Motohashi-Pintz, A smoothed GPY sieve, Bull. London Math. Soc. 40
(2008), no. 2, 298-310. [19] Pintz, in: An irregular mind. Szemeredi is
70. Bolyai Soc. Math. Stud. 21, Springer, 2010, pp. 525-559. [20] Pintz,
On the singular series in the prime k-tuple conjecture, arXiv:1004.1084v1
[math.NT]. [21] Pintz, Turan Memorial, de Gruyter, Berlin, to appear.
[22] Pintz, Erdos Centennial, Bolyai Soc. Math. Stud., Springer, 2013,
to appear. [23] de Polignac, Nouv. Ann. Math. 8 (1849), 423-429.
[24] Rankin, Proc. Cambridge Philos. Soc. 36 (1940), 255-266.
[25] Ricci, Riv. Mat. Univ. Parma 5 (1954), 3-54. [26] Vinogradov,
Doklady Akad. Nauk. SSSR 15 (1937), 291-294. [27] Westzynthius, Comm.
Phys. Math. Helsingfors (5) 25 (1931), 1-37. [28] Ytang Zhang, Bounded
gaps between primes, Ann. of Math., to appear. ["Ytang" as printed.]

---

## FLAGS (consolidated)

1. [TRANSCRIPTION-UNSURE] (3.1): sign inside the product, (n - h_i) as
   read from the page, vs. (n + h_i) clearly printed in (3.5); the (3.1)
   glyph is small.
2. [TRANSCRIPTION-UNSURE] Lemma 1 hypothesis "p < R^{C_0}": capital vs.
   lower-case c_0 in the exponent is not certain; only c_0 (small) and C
   (large) are introduced in the hypothesis text.
3. [TRANSCRIPTION-UNSURE] (3.8) as printed appears to have
   "log log log R" on BOTH sides ("k^2 log log log R << log log log R"),
   which is self-inconsistent as an error-term bound; small print.
4. [TRANSCRIPTION-UNSURE] (3.20)-(3.21) context: "consecutive elements
   i, j in V_0(N)" as printed; logically i, j in V_0.
5. [TRANSCRIPTION-UNSURE] (4.8) hypothesis line: prime marks on I_nu,
   I_mu not clearly legible; (4.7) defines h_nu in I'_nu.
6. [TRANSCRIPTION-UNSURE] (5.4): "N > N(k)" with lower-case k as
   printed; presumably N(K).
7. [TRANSCRIPTION-UNSURE] (6.6): constant printed "(c_1(k,H) + o(1))",
   colliding with the exponent name c_1(k) in (6.1).
8. [TRANSCRIPTION-UNSURE] Section 8: "our Lemma 3 says that we can
   neglect all numbers n with (8.3)" -- role-wise this is Lemma 2;
   transcribed as printed. Also "Lambda_R(n; H, k, ell)" vs. (3.9)'s
   "Lambda_R(n; H, k + ell)".
9. [TRANSCRIPTION-UNSURE] (2.7): summation range under Sigma not
   printed.
10. Note: the paper reuses the letter H for the tuple (calligraphic) and
    the window length (italic), and reuses "1." as the section-item
    number for both proofs in Section 4; transcribed as printed.

---

## COMMENTARY (assessment, NOT extraction)

Consuming context: the project needs an UNCONDITIONAL supply of two
prime-gap-word sites with matched J-prefix and K-suffix windows and a
dominant weighted middle difference, at depths J,K ~ log2 log x (exchange
configuration), against known blockers (i) pigeonhole blindness to
variability, (ii) parity-blocked tuple-type lower bounds for prescribed
gap patterns, (iii) circular Shiu-string densities at depth.

### Focus 1: Lemma 3, its uniformity and its source

Lemma 3 (Section 3, eq. (3.12), p. 7) is exactly the qualitative
Selberg-sieve upper bound: for any constant 0 < alpha < 1/2,
\sum_{n in [N,2N), P^-(P_H(n)) > N^alpha} 1 <<_k (N alpha^{-k}/log^k N)
S(H). Uniformity as claimed by the paper: the implied constant depends on
k only (Vinogradov subscript k in (3.12)); the alpha-dependence is
explicit (alpha^{-k}); and the proof note extends validity to tuples of
diameter H << log N ("This is also valid if we assume only H << log N",
p. 8) -- i.e. uniformity over admissible H in windows up to a constant
times log N is asserted, not proved, in this paper. Source cited for the
proof: "Theorem 5.1 of [15, 1974] or Theorem 2 in Sec. 2.2.2 of [13,
2001]" (p. 8), i.e. Halberstam-Richert, Sieve methods (1974), Theorem
5.1, or Greaves, Sieves in Number Theory (2001), Sec. 2.2.2, Theorem 2.
Caution for project use: the k-dependence of the <<_k constant is not
made explicit anywhere in this paper, and the H << log N extension
carries no proof here; both must be re-proved in-project if k is to grow
(the paper always uses fixed k >= 3.5*10^6). This matches the project
plan (secondhand cite for the qualitative form only).

### Focus 2: the "one side constructed, partner generic by exclusion" pattern

The pattern occurs twice, with full quantitative detail extracted above.

(a) Inside the Main Theorem proof (Section 3, (3.16)-(3.26), pp. 8-9).
Constructed event: >= c_2(k) S(H) N/log^k N integers n in [N,2N) with
two primes in n + H and almost-primality P^-(P_H(n)) > n^{c_1(k)}
((3.16)-(3.18); the lower bound is GPY/Zhang-type, i.e. the
Selberg-weighted first/second moment method of Theorems A and B plus
Lemma 2 -- pre-Maynard-Tao but of the same "constructed event lower
bound" type). Pigeonhole (3.19)-(3.20) fixes a prime-position pattern V_0
(|V_0| >= 2) still carrying c_3(k) S(H) N/log^k N sites; adjacent hits
i,j in V_0 make intermediate TUPLE positions composite by definition of
V(N) (iff in (3.19), giving (3.22)). What is summed: Lemma 3 applied to
the (k+1)-tuple H union h for EVERY non-tuple position h_i < h < h_j and
summed over h ((3.24)): total <= C_4(k)(N/log^{k+1} N) sum_h S(H union
h) <= 2 C_4(k) N eps S(H)/log^k N, where the singular-series sum over
the window is controlled by Lemma 4 (Gallagher-type averaging, needing
window length H >= exp(k^{1/eta}) for a 1 + O(eta) average, (3.14)-
(3.15)). Budget condition: eps < eps_0(k) ((3.25)) makes the exclusion
term o(the constructed count), leaving c_5(k) S(H) N/log^k N sites where
n + h_i, n + h_j are CONSECUTIVE primes (3.26).

(b) Proof of Theorem 5 (Section 6, p. 11) -- the sharpest instance.
Constructed event: B(i,j,N) (6.1) with (i,j) maximal in T (6.2), giving
(6.3): all tuple components strictly between the two hits are almost
always composite; stray primes at non-tuple h in (h_i,h_j) are counted
by Lemma 3 via the (k+1)-tuple H^+ = H union h, legitimized by the P^-
clause (6.4), at cost <<_{k,c_1,H} N/log^{k+1} N each (6.5), giving
(6.6): >= (c_1(k,H)+o(1)) N/log^k N sites n <= N with n + h_i = p_nu,
n + h_j = p_{nu+1} consecutive primes and d_nu = h_j - h_i << 1
((6.7)-(6.8)), along a sequence N = N_nu -> infty. Rigid continuation
excluded: if the NEXT gap always satisfied d_{nu+1} <= C eps log N
(6.9), then summing Lemma 3 over all candidate values d <= C eps log N
((6.10)-(6.11)) bounds such sites by <<_{k,c_1} S(H) C N eps / log^k N;
for eps small this contradicts the constructed lower bound (6.6). Hence
a positive proportion of the constructed bounded-gap sites are followed
by a gap > eps' log N: limsup (d_{nu+1}/d_nu)/log nu > 0 (Theorem 5,
(2.15)). Note the density-of-Polignac-numbers proof itself (Theorem 1)
is NOT in Section 6: it is delegated to Corollary 1 of [19, 2010] with
explicit density value (4.1) (Section 4, p. 9).

Assessment for the exchange target: this is a genuine, UNCONDITIONAL
(post-Zhang) template for "construct one letter, force the neighbor
generic by summed upper bounds". It supplies sites with a two-letter
contrast word (bounded letter d_nu << 1 followed by a letter
> eps' log N) at density >> N/log^k N along a subsequence N_nu. That is
suffix control of depth exactly 1, obtained WITHOUT prescribing the
partner gap (so it sidesteps blocker (ii) for that single letter: the
partner is generic-large by exclusion, not a prescribed tuple event).

### Focus 3: DHL*(k,2), the P^- clause, and consecutivization

Definition: Conjecture DHL*(k,2) (Section 3, p. 6, quoted in full in
Part 3.3 above): for admissible k-tuples in windows H <= eps log N
(3.5), at least c_2(k) S(H) N/log^k N integers n in [N,2N) such that
n + H contains at least two CONSECUTIVE primes and almost primes in each
component, i.e. P^-(P_H(n)) > n^{c_1(k)} (3.6). Main Theorem: true for
k >= 3.5*10^6 (p. 6). The three announced gains over DHL(k,2) --
consecutiveness, almost-primality of every component, and a lower bound
on the count -- are itemized (i)-(iii) on p. 6.

The P^- clause is the load-bearing device twice over. First, it
certifies that between the two prime hits every tuple component n + h_mu
is composite-but-almost-prime (smallest prime factor > n^{c_1(k)}), so
compositeness at those positions is not an accident of small prime
factors but survives with the site count. Second -- the mechanism that
makes the exclusion sums WORK -- if a stray n + h (h not in H) is prime,
then the extended tuple H^+ = H union h inherits the almost-primality:
P^-(P_{H^+}(n)) > n^{c_1(k)} (6.4). Hence the stray-prime event embeds
into the Lemma-3-countable event for a (k+1)-tuple, giving the
1/log^{k+1} N penalty per adjoined position ((6.5), (3.24)) -- one full
log below the site density 1/log^k N, so a window of eps log N adjoined
positions is affordable ((3.24) final bound, (6.11)). Consecutivization
= constructed two primes + pigeonholed pattern V_0 + P^--enabled summed
Selberg exclusion of all intermediate positions, tuple ((3.22)/(6.3))
and non-tuple ((3.23)-(3.24)/(6.4)-(6.5)). Section 8 reuses the same
clause to expel the potential Siegel modulus q ((8.1)-(8.3), q | P_H(n)
impossible when P^-(P_H(n)) > n^{c_1(k)} exceeds the (log X)^{omega(X)}
range of q), making all results effective except where openly declared
ineffective (Theorems 2-4).

### Focus 4: main theorems and ineffectivity

All main statements are extracted verbatim in Parts 1-3 above: Theorems
A-E (background, pp. 1-3), Theorems 1-6 (pp. 3-5), Proposition (p. 3),
Definitions 1-3, Polignac's Conjecture, Conjecture DHL(k,2), Conjecture
DHL*(k,2), MAIN THEOREM. Ineffectivity remarks, verbatim locations:
Theorem 2 "an ineffective constant C'" (p. 3); Theorem 3 "an ineffective
constant c > 0" (p. 4); Theorem 4 "an ineffective constant c_f > 0"
(p. 4); Theorem 2 proof: "The reasoning is more intricate in this case
and the resulting value C is ineffective" (p. 9); Theorem 1 by contrast
has "an explicitly calculable constant c" (p. 3). Section 8 (p. 12)
explains that Zhang's theorem and "all our present results" can be made
effective via the P^- clause plus prescribing q does-not-divide d in
(3.9); the ineffectivity of Theorems 2-4 is of a different kind -- it
comes from the compactness/contradiction structure of their proofs
(infinite families of intervals (4.4), (5.1) with no effective bound on
where the contradiction materializes), not from Siegel zeros.

### What this machinery can and cannot supply toward the exchange configuration

CAN supply, unconditionally:
1. The qualitative summed-Selberg exclusion template at one-letter depth:
   Lemma 3 + Lemma 4 + P^- clause ((3.24), (6.4)-(6.11)). The per-
   position cost 1/log^{k+1} N vs. site density 1/log^k N gives exactly
   one log of budget: any exclusion window of length <= eps log N
   positions is affordable. This is the paper's precise quantitative
   expression of "partner generic by exclusion".
2. Sites with a dominant one-sided contrast: bounded constructed letter
   followed by a generic letter > eps' log N (Theorem 5 via (6.6) vs.
   (6.11)) -- a primitive relevant to "dominant weighted middle
   difference", since it manufactures adjacent letters with ratio
   >> log N without prescribing the large letter.
3. Localization-by-construction of the realized gap value: Theorems 2-4
   show the constructed letter d = h_mu - h_nu can be steered into
   prescribed dyadic-type intervals ((4.7)-(4.9), (5.5)-(5.7)), i.e.
   coarse letter-value control (up to the pigeonhole over pairs).

CANNOT supply (with anchors):
1. Depth. Every controlled object here is ONE gap (the pair of
   consecutive primes) plus ONE neighbor gap (Section 6). Matched
   J-prefix and K-suffix windows at depth J,K ~ log2 log x would need
   ~ J+K prescribed consecutive primes; the mechanism prescribes exactly
   two ((3.5)-(3.6), item (i) p. 6). Nothing in the paper iterates the
   consecutivization to words of length > 1; Theorem 6 (Section 7,
   p. 12) chains sites along an arithmetic progression but each site
   still carries the same single gap d.
2. Pigeonhole blindness is present, not overcome. Which pair (i,j)
   realizes the gap is chosen by pigeonhole over the bounded family of
   patterns V ((3.19)-(3.20): "Since k is bounded the number of possible
   subsets V is also bounded") or by maximality in T ((6.2)); the value
   h_j - h_i is then whatever the surviving pattern gives, within (4.3)-
   type localization only. This is exactly blocker (i): no variability
   or matching control across two distinct sites. No statement in the
   paper compares, matches, or pairs two sites' gap environments.
3. k-uniformity. The entire Section 3 proof is for FIXED k >= 3.5*10^6:
   c_1(k), c_2(k), c_3(k), C_4(k), c_5(k), eps_0(k) are untracked
   functions of k, and step (3.20) uses boundedness of 2^k outright. At
   the project depth one would want k growing (~ log2 log x letters);
   additionally the Gallagher budget (3.15), H >= exp(k^{1/eta}),
   collides with the DHL* window cap H <= eps log N ((3.5)) as soon as
   k^{1/eta} > log log N -- with k ~ log2 log x ~ 1.44 log log x this
   forces eta >= 1, degenerating the 1 + O(eta) averaging (3.14). So
   even the exclusion side of the template needs a re-proved,
   k-uniform Lemma 3/Lemma 4 pair before it can run at exchange depth.
   (This quantitative collision is my computation from (3.5)+(3.15), not
   a statement in the paper.)
4. Word-value prescription remains parity/tuple-blocked. The lower-bound
   side ((3.16)-(3.17)) is inherited from Zhang/GPY and produces "at
   least two primes SOMEWHERE in the tuple", never a prescribed gap
   word; the paper's own framing concedes this (pp. 5-6: DHL(k,2)-type
   results "cannot exclude the existence of other primes...", and the
   fix (i)-(iii) on p. 6 only upgrades to consecutiveness of one pair).
5. Subsequence caveat: Theorem 5's supply (6.6) exists only along
   N = N_nu -> infty chosen via limsup in (6.2); density statements at
   ALL scales (which two-site matching at a common x would want) are not
   provided. Theorems 2-4 are additionally ineffective (p. 3, p. 4,
   p. 9).

Net: the paper is the canonical source for (a) the allowed secondhand
qualitative Lemma 3 cite (Halberstam-Richert Thm 5.1 / Greaves Sec.
2.2.2 Thm 2, with the H << log N extension asserted p. 8), and (b) the
exact one-log budget accounting by which a constructed two-prime site
survives summed Selberg exclusion of an eps log N window of rigid
continuations ((3.24), (6.11) + (3.14)-(3.15)). It supplies depth-1
suffix contrast, not matched-depth J/K windows, and its pigeonhole steps
reproduce, rather than evade, the project's blocker (i).
