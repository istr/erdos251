# EXTRACTION: Maynard, "Dense clusters of primes in subsets"

Source: /home/istr/pro/erdos251/dossier/1405.2593v2.pdf
(arXiv:1405.2593v2 [math.NT] 16 Dec 2014, 35 pages, James Maynard).
Scope: INTERFACE ONLY -- main theorem(s), hypotheses, uniformity ranges,
application theorems relevant to consecutive primes / clusters / congruence
patterns, and the weight-level key proposition. Extracted from visual reads of
PDF pages 1-7, cross-checked against pdftotext.

Transliteration conventions (source uses non-ASCII symbols; this file is ASCII):
- Calligraphic A, P, L (the set of integers, set of primes, set of linear
  functions) are written A, P, L. Blackboard-bold P (all primes) is written PP.
- Blackboard N is written N. Calligraphic S(xi;D) is written S(xi;D).
- Fraktur singular series \frakS_B(L) is written S_B(L); the singular series
  \frakS(L) of the introduction is written S(L).
- Greek letters and math are given as LaTeX tokens: \varphi (Euler totient,
  printed as phi in the paper), \theta, \alpha, \delta, \epsilon, \rho, \xi,
  \eta, \Delta, \gg, \ll, \sum, \prod, \int.
- "#X" = cardinality of X, as in the paper. "1_X" = indicator function of X.
- Verbatim quotes are faithful up to this transliteration; line breaks inside
  displayed formulas are flattened.

---

## 1. Setup and definitions

### 1.1 Admissible sets (Section 1, p. 1)

Verbatim (Section 1, first paragraph):
"Let L = {L_1, ..., L_k} be a set of distinct linear functions
L_i(n) = a_i n + b_i (1 <= i <= k) with coefficients in the positive integers.
We say such a set is admissible if \prod_{i=1}^k L_i(n) has no fixed prime
divisor (that is, for every prime p there is an integer n_p such that
\prod_{i=1}^k L_i(n_p) is coprime to p)."

Stated aim (Section 1, last paragraph, verbatim):
"The aim of this paper is to show that the flexibility of the method introduced
in [13] allows us to prove weak analogues of these generalizations of Dickson's
conjecture. In particular, if A and P \cap L(A) are well-distributed in
arithmetic progressions, then we can obtain a lower bound close to the expected
truth for the number of n \in A, n <= x such that several of the L_i(n) are
primes in P, and we can show this estimate holds with some uniformity in the
size of a_i, b_i and k."

### 1.2 Counting notation, equation (2.1) (Section 2, p. 2)

Verbatim (display (2.1)): "Given a set of integers A, a set of primes P, and a
linear function L(n) = l_1 n + l_2, we define

  A(x) = {n \in A : x <= n < 2x},
  A(x; q, a) = {n \in A(x), n \equiv a (mod q)},
  L(A) = {L(n) : n \in A},
  \varphi_L(q) = \varphi(|l_1| q) / \varphi(|l_1|),
  P_{L,A}(x) = L(A(x)) \cap P,
  P_{L,A}(x; q, a) = L(A(x; q, a)) \cap P."

---

## 2. Hypothesis 1 (Section 2, p. 2) -- the well-distribution hypothesis

Context sentence (verbatim): "This paper will focus on sets which satisfy the
following hypothesis, which is given in terms of (A, L, P, B, x, \theta) for L
an admissible set of linear functions, B \in N, x a large real number, and
0 < \theta < 1."

Verbatim statement:

"Hypothesis 1. (A, L, P, B, x, \theta). Let k = #L.
(1) A is well-distributed in arithmetic progressions: We have
    \sum_{q <= x^\theta} max_a | #A(x; q, a) - #A(x)/q |
      \ll #A(x) / (log x)^{100 k^2}.
(2) Primes in L(A) \cap P are well-distributed in most arithmetic
    progressions: For any L \in L we have
    \sum_{q <= x^\theta, (q,B)=1} max_{(L(a),q)=1}
      | #P_{L,A}(x; q, a) - #P_{L,A}(x)/\varphi_L(q) |
      \ll #P_{L,A}(x) / (log x)^{100 k^2}.
(3) A is not too concentrated in any arithmetic progression: For any
    q < x^\theta we have
    #A(x; q, a) \ll #A(x)/q."

Remark following Hypothesis 1 (verbatim, p. 2):
"We expect to be able to show this Hypothesis holds (for all large x, some
fixed \theta > 0 and some B < x^{O(1)} with few prime factors) for sets A, P
where we can establish 'Siegel-Walfisz' type asymptotics for arithmetic
progressions to small moduli, and a large sieve estimate to handle larger
moduli."

Also (verbatim, p. 2): "We note that the recent work of Benatar [2] showed the
existence of small gaps between primes for sets which satisfy similar
properties to those considered here."

---

## 3. Main theorem: Theorem 3.1 (Section 3, p. 2)

Verbatim statement:

"Theorem 3.1. Let \alpha > 0 and 0 < \theta < 1. Let A be a set of integers,
P a set of primes, L = {L_1, ..., L_k} an admissible set of k linear
functions, and B, x integers. Let the coefficients L_i(n) = a_i n + b_i \in L
satisfy 1 <= a_i, b_i <= x^\alpha for all 1 <= i <= k, and let
k <= (log x)^\alpha and 1 <= B <= x^\alpha.
  There is a constant C depending only on \alpha and \theta such that the
following holds. If k >= C and (A, L, P, B, x, \theta) satisfy Hypothesis 1,
and if \delta > (log k)^{-1} is such that

  (1/k) (\varphi(B)/B) \sum_{L \in L} (\varphi(a_i)/a_i) #P_{L,A}(x)
    >= \delta #A(x) / log x,

then

  #{n \in A(x) : #({L_1(n), ..., L_k(n)} \cap P) >= C^{-1} \delta log k}
    \gg #A(x) / ( (log x)^k exp(C k) ).

Moreover, if P = PP, k <= (log x)^{1/5} and all L \in L have the form
a n + b_i with |b_i| <= (log x) k^{-2} and a \ll 1, then the primes counted
above can be restricted to be consecutive, at the cost of replacing exp(C k)
with exp(C k^5) in the bound."

[Note on notation inside the quote: in the displayed hypothesis the summand is
printed exactly as \varphi(a_i)/a_i with L ranging over L, i.e. a_i is the
leading coefficient of the summation variable L = L_i; this index mismatch is
in the original.]

### 3.1 Parameter uniformity ranges of Theorem 3.1, as stated

- Coefficients: 1 <= a_i, b_i <= x^\alpha (all i).
- Number of functions: k <= (log x)^\alpha; also k >= C (C = C(\alpha, \theta)).
- Sifting/level modulus: 1 <= B <= x^\alpha (B an integer).
- Density parameter: \delta > (log k)^{-1} with the displayed lower bound on
  the average prime density of P over L(A).
- Conclusion: \gg #A(x) / ((log x)^k exp(Ck)) integers n \in A(x) with at
  least C^{-1} \delta log k of L_1(n), ..., L_k(n) in P.
- Consecutive-primes variant: requires P = PP (all primes), k <= (log x)^{1/5},
  L_i(n) = a n + b_i (common leading coefficient), |b_i| <= (log x) k^{-2},
  a \ll 1; the count bound weakens exp(Ck) -> exp(Ck^5).
- From the proof (Section 6, p. 7, display (6.1), verbatim): "We first note
  that by passing to a subset of L, it is sufficient to show that in the
  restricted range C <= k <= (log x)^{1/5} we have the weaker bound
  (6.1) #{n \in A(x) : #({L_1(n), ..., L_k(n)} \cap P) >= C^{-1} \delta log k}
  \gg #A(x) / ((log x)^k exp(C k^5)). The main result then follows with a
  suitably adjusted value of C."

### 3.2 Remarks accompanying Theorem 3.1 (Section 3, p. 3)

Effectivity (verbatim): "All implied constants in Theorem 3.1 are effectively
computable if the implied constants in Hypothesis 1 for (A, L, P, B, x,
\theta) are."

Limitation remark (verbatim): "We note that Theorem 3.1 can show that several
of the L_i(n) are primes for sets A, P where it is not the case that there are
infinitely many n \in A such that all of the L_i(n) are primes in P. For
example, if P = {p_{2n} : n \in N} is the set of primes of even index and
A = N, then we would expect P to be equidistributed in the sense of
Hypothesis 1. However, there are clearly no integers n such that
n, n + 2 \in P, and so the analogue of the twin prime conjecture does not hold
in this case. Similarly if P is restricted to the union of arithmetic
progressions in short intervals[fn 1]. Therefore without extra assumptions on
our sets A, P we cannot hope for a much stronger statement than several of the
L_i(n) are primes in P."

Footnote 1 (p. 3, verbatim) [TRANSCRIPTION-UNSURE: small print; the condition
"n \equiv i (mod 5)" is as printed but is plausibly a typo for "p \equiv i
(mod 5)" in the source]: "For example, one could take
P = \cup_{x=2^j} \cup_{i <= x^{1/4}/2}
{x + (2i - 1) x^{3/4} < p <= x + 2i x^{3/4} : n \equiv i (mod 5)}. This set is
equidistributed in the sense of Hypothesis 1, but also has no gaps of size 2."

Sparse sets remark (verbatim): "We also note that Theorem 3.1 can apply to
very sparse sets A, and no density assumptions are required beyond the
estimates of Hypothesis 1. Of course, for such sets the major obstacle is in
establishing Hypothesis 1."

---

## 4. Application theorems (Section 3, pp. 3-4)

### 4.1 Theorem 3.2 -- many primes in short intervals

Verbatim: "Theorem 3.2. For any x, y >= 1 there are \gg x exp(-\sqrt{log x})
integers x_0 \in [x, 2x] such that

  \pi(x_0 + y) - \pi(x_0) \gg log y."

Remark (verbatim, p. 3): "Theorem 3.2 is non-trivial in the region
y = o(log x) (and y sufficiently large), when typically there are no primes in
the interval [x, x + y]. For such values of y, it shows that there are many
intervals of length y containing considerably more than the typical number of
primes. By comparison, a uniform version of the prime k-tuples conjecture
would suggest that for small y there are intervals [x, x + y] containing
\gg y / log y primes. For large fixed y, we recover the main result of [13],
that liminf_n (p_{n+m} - p_n) \ll_m 1 for all m."

(Abstract, verbatim, for the derived form: "we show there are infinitely many
intervals of length (log x)^\epsilon containing \gg_\epsilon log log x primes".)

### 4.2 Theorem 3.3 -- strings of m congruent consecutive primes in a short window

Verbatim: "Theorem 3.3. Fix \epsilon > 0 and let x > x_0(\epsilon, q). There
is a constant c_\epsilon > 0 (depending only on \epsilon) such that uniformly
for m <= c_\epsilon log log x, q <= (log x)^{1-\epsilon} and (a, q) = 1 we
have

  #{p_n <= x : p_n \equiv ... \equiv p_{n+m} \equiv a (mod q),
     p_{n+m} - p_n <= \epsilon log x}
   \gg_\epsilon \pi(x) / (2q)^{exp(C m)}.

Here C > 0 is a fixed constant."

Remarks (verbatim, p. 3): "Theorem 3.3 extends a result of Shiu [17] which
showed the same result but with a lower bound \gg x^{1-\epsilon(x)} for
\epsilon(x) \approx C_q m (log log x)^{-1/\varphi(q)} in the shorter range
m \ll (log log x)^{1/\varphi(q)-\epsilon} and without the constraint
p_{n+m} - p_n <= \epsilon log x, and a result of Freiberg [5] which showed for
fixed a, q, \epsilon infinitely many n such that
p_{n+1} \equiv p_n \equiv a (mod q) and p_{n+1} - p_n <= \epsilon log p_n."

"We see that for fixed m, q, Theorem 3.3 shows a positive proportion of primes
p_n are counted (and so our lower bound is of the correct order of magnitude).
In particular, for a positive proportion of primes p_n we have[fn 2]
p_n \equiv p_{n+1} \equiv ... \equiv p_{n+m} \equiv a (mod q) and
p_{n+m} - p_n <= \epsilon log p_n. This extends a result of Goldston, Pintz
and Yildirim [7] which showed a positive proportion of p_n have
p_{n+1} - p_n <= \epsilon log p_n."

Footnote 2 (verbatim): "This disproves the conjecture
#{p_n <= x : p_n \equiv p_{n+1} \equiv 1 (mod 4)} = o(\pi(x)) of Knapowski
and Turan [10]."

### 4.3 Theorem 3.4 -- clusters of primes among linear forms in short intervals

Verbatim: "Theorem 3.4. Fix m \in N and \epsilon > 0. There exists a
k = exp(O(m)), such that for x > x_0(\epsilon, m) and
x^{7/12+\epsilon} <= y <= x and for any admissible set L = {L_1, ..., L_k}
where L_i(n) = a_i n + b_i with 1 <= a_i \ll (log x)^{1/\epsilon} and
0 <= b_i \ll x we have

  #{n \in [x, x + y] : at least m of L_i(n) are prime} \gg y / (log x)^k."

Remarks (verbatim, p. 4): "Theorem 3.4 relies on a Bombieri-Vinogradov type
theorem for primes in intervals of length x^{7/12+\epsilon}, the best such
result being due to Timofeev [19]. By adapting Hypothesis 1 to allow for
weighted sums instead of #P_{L,A}(x), we could use presumably the results of
[8] and [11] to extend this to the wider range x^{0.525} <= y <= x."

"Theorem 3.4 explicitly demonstrates the claim from [13] that the method also
shows the existence of bounded gaps between primes in short intervals, and for
linear functions. We note that we would expect the lower bound to be of size
y/(log x)^m, and so our bound is smaller that the expected truth by a factor
of a fixed power of log x. It appears such a loss is an unavoidable feature of
the method when looking at bounded length intervals." [sic: "smaller that" is
as printed]

### 4.4 Theorem 3.5 -- primes with prescribed Chebotarev/Artin splitting type

Verbatim: "Theorem 3.5. Let K/Q be a Galois extension of Q with discriminant
\Delta_K. There exists a constant C_K depending only on K such that the
following holds. Let C \subseteq Gal(K/Q) be a conjugacy class in the Galois
group of K/Q, and let

  P = {p prime : p \nmid \Delta_K, [ (K/Q) / p ] = C},

where [ (K/Q) / . ] denotes the Artin symbol. Let m \in N and
k = exp(C_K m). For any fixed admissible set L = {L_1, ..., L_k} of k linear
functions L_i(n) = a_i n + b_i with (a_i, \Delta_K) = 1 for each
1 <= i <= k, we have

  #{x <= n <= 2x : at least m of L_1(n), ..., L_k(n) are in P}
    \gg x / (log x)^{exp(C_K m)},

provided x >= x_0(K, L)."

### 4.5 Uniformity limitation for Theorems 3.4 / 3.5 (Section 3, p. 4)

Verbatim: "As with Theorem 3.4, we only state the result for fixed m, because
it relies on other work which establishes the Bombieri-Vinogradov type
estimates of Hypothesis 1, and these results only save an arbitrary power of
log x. One would presume these results can be extended to save
exp(-c \sqrt{log x}) or similar (having excluded some possible bad moduli),
which would allow uniformity for m <= \epsilon log log x, but we do not pursue
this here. Similarly, the implied constant in the lower bounds of Theorem 3.4
and Theorem 3.5 is not effective as stated, but presumably a small
modification to the underlying results would allow us to obtain an effective
bound."

(Context for Theorem 3.5's Hypothesis-1 input, from the proof, Section 6,
p. 11: "Murty and Murty [14] have then established the key estimate (2) of
Hypothesis 1 with any \theta < min(1/2, 2/#G), where G = Gal(K/Q)". For
Theorem 3.4 the proof takes "P = PP, A = [x, x + y], B = 1,
\theta = 1/30 - \epsilon". For Theorem 3.2 the proof establishes "Hypothesis 1
holds for (A, L, P, B, x, 1/3)" -- transcribed from the pdftotext layer of the
proofs, secondary anchors only.)

---

## 5. Key Proposition 6.1 (Section 6, pp. 6-7) -- the weight-level interface

This is the proposition a consumer would use to build custom applications
(all of Theorems 3.1-3.5 are derived from it; verbatim, p. 6: "The proof of
theorems 3.1-3.5 relies on the following key proposition.").

Verbatim statement:

"Proposition 6.1. Let \alpha > 0 and 0 < \theta < 1. Let A be a set of
integers, P a set of primes, L = {L_1, ..., L_k} an admissible set of k
linear functions, and B, x integers. Assume that the coefficients
L_i(n) = a_i n + b_i \in L satisfy |a_i|, |b_i| <= x^\alpha and a_i != 0 for
all 1 <= i <= k, and that k <= (log x)^\alpha and 1 <= B <= x^\alpha. Let
x^{\theta/10} <= R <= x^{\theta/3}. Let \rho, \xi satisfy
k (log log x)^2 / (log x) <= \rho, \xi <= \theta/10, and define

  S(\xi; D) = {n \in N : p|n ==> (p > x^\xi or p|D)}.

There is a constant C depending only on \alpha and \theta such that the
following holds. If k >= C and (A, L, P, B, x, \theta) satisfy Hypothesis 1,
then there is a choice of nonnegative weights w_n = w_n(L) satisfying

  w_n \ll (log R)^{2k} \prod_{i=1}^{k} \prod_{p | L_i(n), p \nmid B} 4

such that
(1) We have
    \sum_{n \in A(x)} w_n = (1 + O(1/(log x)^{1/10}))
      (B^k/\varphi(B)^k) S_B(L) #A(x) (log R)^k I_k.
(2) For any L(n) = a_L n + b_L \in L with L(n) > R on [x, 2x], we have
    \sum_{n \in A(x)} 1_P(L(n)) w_n
      >= (1 + O(1/(log x)^{1/10})) (B^{k-1}/\varphi(B)^{k-1}) S_B(L)
         (\varphi(|a_L|)/|a_L|) #P_{L,A}(x) (log R)^{k+1} J_k
       + O( (B^k/\varphi(B)^k) S_B(L) #A(x) (log R)^{k-1} I_k ).
(3) For L = a_0 n + b_0 \notin L and D <= x^\alpha, if \Delta_L != 0 we have
    \sum_{n \in A(x)} 1_{S(\xi;D)}(L(n)) w_n
      \ll \xi^{-1} (\Delta_L/\varphi(\Delta_L)) (D/\varphi(D))
          (B^k/\varphi(B)^k) S_B(L) #A(x) (log R)^{k-1} I_k,
    where
      \Delta_L = |a_0| \prod_{j=1}^{k} |a_0 b_j - b_0 a_j|.
(4) For L \in L we have
    \sum_{n \in A(x)} ( \sum_{p | L(n), p < x^\rho, p \nmid B} 1 ) w_n
      \ll \rho^2 k^4 (log k)^2 (B^k/\varphi(B)^k) S_B(L) #A(x) (log R)^k I_k.

Here I_k, J_k are quantities depending only on k, and S_B(L) is a quantity
depending only on L, and these satisfy

  S_B(L) = \prod_{p \nmid B} (1 - #{1 <= n <= p : p | \prod_{i=1}^k L_i(n)}/p)
             (1 - 1/p)^{-k} \gg 1/exp(O(k)),
  I_k = \int_0^\infty ... \int_0^\infty F^2(t_1, ..., t_k) dt_1 ... dt_k
      \gg (2k log k)^{-k},
  J_k = \int_0^\infty ... \int_0^\infty
          ( \int_0^\infty F(t_1, ..., t_k) dt_k )^2 dt_1 ... dt_{k-1}
      \gg ((log k)/k) I_k,

for a smooth function F = F_k : R^k -> R depending only on k. Moreover, if
all functions L \in L are of the form L = a n + b_L, for some fixed a and
b_L \ll log x/(k log k), then for \eta >= (log x)^{-9/10}, we have

  \sum_{b \ll \eta log x, L(n) = a n + b} \Delta_L/\varphi(\Delta_L)
    \ll \eta (log x)(log k).

Here the implied constants depend only on \theta, \alpha, and the implied
constants from Hypothesis 1."

---

## 6. Global notation conventions (Section 4, p. 4)

Verbatim: "We shall view 0 < \theta < 1 and \alpha > 0 as fixed real
constants. All asymptotic notation such as O(.), o(.), \ll, \gg should be
interpreted as referring to the limit x -> \infty, and any constants (implied
by O(.) or denoted by c, C with subscripts) may depend on \theta, \alpha but
no other variable, unless otherwise noted. We will adopt the main assumptions
of Theorem 3.1 throughout. In particular we will view A, P as given sets of
integers and primes respectively and k = #L will be the size of
L = {L_1, ..., L_k} an admissible set of integer linear functions, and the
coefficients a_i, b_i \in Z of L_i(n) = a_i n + b_i, satisfy
|a_i|, |b_i| <= x^\alpha and a_i != 0. B <= x^\alpha will be an integer, and
x, k will always to be assumed sufficiently large (in terms of \theta,
\alpha)."

---

## 7. Citation guide (factual mapping, no interpretation)

- k-uniform cluster statement for a well-distributed subset of primes /
  integers: cite Theorem 3.1 (uniform in k <= (log x)^\alpha, coefficients
  <= x^\alpha, B <= x^\alpha, \delta > (log k)^{-1}).
- k-uniform CONSECUTIVE-prime clusters (P = PP): cite the "Moreover" clause of
  Theorem 3.1 (k <= (log x)^{1/5}, common leading coefficient a \ll 1,
  |b_i| <= (log x) k^{-2}, cost exp(Ck) -> exp(Ck^5)).
- y-uniform "many primes in an interval of length y" (\gg log y primes): cite
  Theorem 3.2.
- m- and q-uniform strings of m+1 congruent consecutive primes with diameter
  <= \epsilon log x: cite Theorem 3.3 (m <= c_\epsilon log log x,
  q <= (log x)^{1-\epsilon}); positive-proportion corollary in the remark
  after Theorem 3.3 and footnote 2 (Knapowski-Turan disproof).
- Fixed-m clusters in short intervals [x, x+y], y >= x^{7/12+\epsilon}: cite
  Theorem 3.4.
- Fixed-m clusters with Chebotarev condition: cite Theorem 3.5.
- Custom applications at the sieve-weight level: cite Proposition 6.1
  (conclusions (1)-(4) with R in [x^{\theta/10}, x^{\theta/3}]).

---

## COMMENTARY (extractor's observations -- NOT from the paper)

### Interface card (max 15 lines)

1. Engine: Thm 3.1 turns Hypothesis 1 (BV-type level-\theta equidistribution
   of A and of P on L(A), plus non-concentration) into >= C^{-1} \delta log k
   primes of P among k linear forms at \gg #A(x)/((log x)^k exp(Ck)) points.
2. Fully uniform in k up to (log x)^\alpha; \delta may decay to 1/log k, so
   it tolerates P of relative density (log k)^{-1} inside L(A)-primes.
3. Consecutive-primes mode exists but only for P = all primes, common slope
   a \ll 1, offsets |b_i| <= (log x)/k^2, k <= (log x)^{1/5}: this is the
   clause an erdos251 gap-pattern argument would need for controlling
   g_n-blocks (clusters force log k primes in a window of diameter
   <= max b_i - min b_i <= log x / k^2, i.e. o(log x) average-gap windows).
4. Quantitative price: density of good n is (log x)^{-k} exp(-Ck^5) --
   doubly-exponentially far from all-n statements; no upper-bound control on
   the other L_i(n), and no positivity structure beyond "at least m primes".
5. For binary-expansion arguments (delta_n tails) the usable outputs are
   Thm 3.2 (\gg log y primes in length-y windows, y = o(log x)) and Thm 3.3
   (m+1 consecutive primes, same residue class, diameter <= \epsilon log x,
   for a positive proportion of n when m, q fixed).
6. Caveats: Thm 3.4/3.5 constants ineffective as stated; Thm 3.1 effective
   iff Hypothesis-1 constants are; footnote-1 example shows Hypothesis 1
   alone cannot force specific gap patterns (no size-2 gaps possible).

### Extraction quality notes

- All statements in Sections 2-3 and Proposition 6.1 were transcribed from
  visually rendered pages 1-7 and cross-checked against the pdftotext layer;
  the two sources agree everywhere checked.
- One [TRANSCRIPTION-UNSURE] item: footnote 1 on p. 3 (small print; and the
  printed "n \equiv i (mod 5)" looks like a source typo for "p \equiv i").
- The \varphi(a_i)/a_i vs. L \in L index mismatch in Thm 3.1's displayed
  hypothesis is in the original (noted inline in Section 3 above).
- Proofs (Sections 6-9) were not extracted beyond the secondary anchors noted
  in Sections 3.1 and 4.5; target was interface only.
