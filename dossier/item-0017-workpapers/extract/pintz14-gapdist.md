# EXTRACTION: Janos Pintz, "On the distribution of gaps between consecutive primes"

Source (only evidence base): /home/istr/pro/erdos251/dossier/1407.2213v2.pdf
arXiv:1407.2213v2 [math.NT] 24 Sep 2014 (as printed on the arXiv sidebar of
p. 1). Author: Janos Pintz, Alfred Renyi Institute of Mathematics, Hungarian
Academy of Sciences, Budapest (affiliation block, p. 22). 22 pages. No
journal id printed. NOTE: the paper has NO abstract as printed; p. 1 opens
directly with "1 Introduction".

Transcription conventions: ASCII only. Diacritics transliterated (Erdos,
Pintz as printed "Janos Pintz", Yildirim, Cramer, Konjagin, Westzynthius).
Math in LaTeX-like ASCII: d_n = p_{n+1} - p_n; log_j x denotes the j-fold
iterated logarithm (the paper's log_nu n); log^2 N = (log N)^2 (superscript,
distinguished carefully from log_2 N = log log N); <= , >= ; << (Vinogradov);
f nearrow infty = the paper's "f(x) increasing monotonically to infinity"
arrow; {a_n}' = derived set (set of limit points) as in the paper's prime
notation (1.2); [a,b] closed interval; P = set of primes; H = the paper's
calligraphic H (admissible tuple); L = the paper's calligraphic L in (3.18);
R, R', Rtilde, Rtilde' = the paper's calligraphic/tilde sets in (6.6);
nmid = "does not divide". Anchors are theorem/equation/section numbers;
page numbers (printed = PDF page) are secondary aid. Everything up to the
final marked section is EXTRACTION (what the paper says); paraphrase is
marked [PARAPHRASE] and used only for connective tissue.

---

## 1. NO ABSTRACT; INTRODUCTION SETUP (verbatim)

There is no abstract. Opening of Section 1 (p. 1), verbatim:

> "The recent dramatic new developments in the study of bounded gaps between
> primes, reached by Zhang [Zha], Maynard [May1] and Tao [Pol8B] made other
> old conjectures about the distribution of primegaps
> (1.1)  d_n = p_{n+1} - p_n,  P = {p_i}_{i=1}^infty the set of all primes
> accessible. One of the most interesting such conjectures was formulated in
> 1954 by Erdos [Erd2] as follows. Let J denote the set of limit points of
> d_n / log n, i.e.
> (1.2)  J = { d_n / log n }'.
> Then J = [0, infty]."

(p. 1, verbatim): "While Westzynthius [Wes] proved already in 1931 the
relation

> (1.3)  limsup_{n->infty} d_n/log n = infty  i.e.  infty in J,

no finite limit point was known until 2005, when in a joint work of
Goldston, Yildirim and the author [GPY1] it was shown that

> (1.4)  liminf_{n->infty} d_n/log n = 0  i.e.  0 in J.

On the other hand, Erdos [Erd2] and Ricci [Ric] proved simultaneously and
independently about 60 years ago that J has positive Lebesgue measure."

(p. 2, verbatim): "In a recent work D. Banks, T. Freiberg and J. Maynard
showed [BFM] that more than 2% of all nonnegative real numbers belong to J."

Prior result of the author defining the function class (p. 2), verbatim:

> "The author has shown [Pin3] that for any f(n) <= log n, f(n) nearrow
> infty (i.e. f(n) -> infty, f(n) is monotonically increasing) satisfying
> for any epsilon
> (1.5)  (1 - epsilon) f(N) <= f(n) <= (1 + epsilon) f(N)
>          if n in [N, 2N], N > N_0(epsilon)
> we have an ineffective constant c_f such that
> (1.6)  [0, c_f] subset J_f := { d_n / f(n) }'."

The Erdos-Rankin function (p. 2), verbatim:

> "The 76-year-old result of Rankin, the estimate (log_nu n denotes the
> nu-fold iterated logarithmic function)
> (1.7)  limsup_{n->infty} (d_n/log n)/g(n) >= C_0,
>        g(x) = log_2 x log_4 x / (log_3 x)^2
> was apart from the value of the constant C_0 still until August 2014 the
> best known lower estimate for large values of d_n. (The original value
> C_0 = 1/3 of Rankin was improved in four steps, finally to C_0 = 2e^gamma
> by the author [Pin2].) Then in two days two different new proofs appeared
> by Ford-Green-Konjagin-Tao [FGKT] and Maynard [May2] in the arXiv, proving
> Erdos's famous USD 10,000 conjecture according to which (1.7) holds with
> an arbitrarily large constant C_0."

Motivating questions (p. 2), verbatim:

> "This raises the question whether the relation (1.6) can be improved to
> functions of type f(x) = omega(x) log x with omega(x) -> infty and whether
> perhaps even omega(x) = c_1 g(x) can be reached with some absolute
> constant c_1, or, following the mentioned new developments, with an
> arbitrarily large c_1 as well."

> "Another question is whether for some function f(n) we can reach
> (1.8)  [0, infty] = J_f,
> i.e. the original conjecture of Erdos with the function f(n) in place of
> log n."

(p. 2-3, verbatim): "Using our notation (1.1), (1.5)-(1.7), we will show the
following results, which, although do not show the original conjecture
J_{log n} = [0, infty] of Erdos, but in several aspects approximate it and
in other aspects they go even further." And (p. 3, verbatim): "Since the
first version of this paper was written before the groundbreaking works
[FGKT] and [May2] we will present the formulation and proofs of the original
version of our results in the Introduction and Sections 3-5, while the
formulation of the improved stronger versions appear in Section 2 and the
needed changes in the proofs in Section 6, in this case the changes refer to
the mentioned work of Maynard [May2]."

---

## 2. MAIN THEOREMS (verbatim)

Theorem 1 (p. 3), verbatim:

> "Theorem 1. There exists an absolute constant c_0 such that for any
> function f(x) nearrow infty, satisfying (1.5) and
> (1.9)  f(x) <= c_0 g(x) log x
> we have with a suitable (ineffective) constant c_f
> (1.10)  [0, c_f] subset J_f := { d_n / f(n) }'."

Theorem 2 (p. 3), verbatim:

> "Theorem 2. Let us consider a sequence of functions {f_i(x)}_{i=1}^infty
> satisfying (1.5), (1.9), f(x) nearrow infty and
> (1.11)  f_{i+1}(x)/f_i(x) -> infty  as  x -> infty  for every i.
> Then apart from at most 98 functions f_i(x) we have
> (1.12)  [0, infty] = J_{f_i} = { d_n / f_i(n) }'."

[PRINTED-ODDITY: the hypothesis says "f(x) nearrow infty", presumably
meaning each f_i(x) nearrow infty; transcribed as printed.]

Preceding sentence for Theorem 3 (p. 3), verbatim: "Answering a question
raised in a recent work of Banks, Freiberg and Maynard [BFM] we show that
the method of [BFM] works also if we normalize the primegaps in place of
log n with any function not exceeding the Erdos-Rankin function."

Theorem 3 (p. 3), verbatim:

> "Theorem 3. Suppose f(x) nearrow infty and satisfies (1.5) and (1.9).
> Then for any sequence of k >= 50 non-negative real numbers beta_1 <
> beta_2 < ... < beta_k at least one of the numbers {beta_j - beta_i;
> 1 <= i < j <= k} belongs to J_f. Consequently more than 2% of all
> non-negative real numbers belong to J_f."

Theorem 4 (p. 4), preceded by (verbatim): "As a by-product the method also
gives a different new proof for the following result of Helmut Maier [Mai1]
proved in 1981 by his famous matrix method:"

> "Theorem 4. For any natural number m we have with the notation (1.7)
> (1.13)  limsup_{h->infty} min(d_{n+1}, ..., d_{n+m}) / (g(n) log n) > 0."

[PRINTED-ODDITY: the limsup subscript is "h -> infty" as printed, although
the running variable is n; transcribed verbatim.]

Corollary 1 (p. 4), preceded by (verbatim): "An immediate corollary of
Theorem 2 is the following"

> "Corollary 1. Let eta(x) -> 0 be an arbitrary function. If eta(x)F(x)
> nearrow infty, F(x) nearrow infty, both functions F(x) and eta(x)F(x)
> satisfy (1.5) and (1.9), then we have a function f(x) nearrow infty,
> (1.14)  eta(x)F(x) <= f(x) <= F(x),
> for which
> (1.15)  [0, infty] = J_f := { d_n / f(n) }'."

Interpretive paragraph after Corollary 1 (p. 4), verbatim:

> "This means that although we can not show Erdos's conjecture for the
> natural normalizing function log n, changing it a little bit, it will be
> already true for some function xi(n) log n, where xi(n) tends to 0 (or
> alternatively we can require xi(n) -> infty) arbitrarily slowly (even if
> this is not a natural normalization)."

---

## 3. SECTION 2: STRONGER FORMS (the g_0 upgrade), verbatim

(p. 4), verbatim: "We will use in the formulation and proof of our results
the work of J. Maynard [May2] which implicitly defines an unspecified but
actually explicitly calculable omega_0(x) function with the property

> (2.1)  lim_{x->infty} omega_0(x) = infty,

such that defining (cf. (1.7))

> (2.2)  g_0(x) = omega_0(x) g(x) = omega_0(x) log_2 x log_4 x/(log_3 x)^2,

the result (1.7) holds with g_0(n) in place of g(n)."

(p. 5), verbatim: "J. Maynard further mentions in the Remark at the end of
his paper that he hopes to obtain his result with omega_0(x) =
(log_2 x)^{1+o(1)} which would be the limit of the Erdos-Rankin method."

(p. 5), verbatim: "We mention that such an improvement would almost surely
lead to an improvement of our results too, since the mentioned idea (to
show the same results with a uniformity in the variable k of [May2] for k
as large as k asymp (log x)^alpha) would leave the structure of the proof
unchanged."

The five stronger statements (p. 5), verbatim:

> "Theorem 1'. Theorem 1 holds with g(x) replaced by g_0(x) in (1.9).
> Theorem 2'. Theorem 2 holds with g(x) replaced by g_0(x) in (1.9).
> Theorem 3'. Theorem 3 holds with g(x) replaced by g_0(x) in (1.9).
> Theorem 4'. Theorem 4 holds with g(x) replaced by g_0(x) in (1.9).
> Corollary 1'. Corollary 1 holds with g(x) replaced by g_0(x) in (1.9)."

---

## 4. SECTION 3: THE MAYNARD-TAO INPUT AND THE INEFFECTIVITY SOURCE

Admissibility (p. 5), verbatim: "We call H_m = {h_1, ..., h_m} an
admissible m-tuple if 0 <= h_1 < ... < h_m and H_m does not occupy all
residue classes mod p for any prime p."

Landau-Page theorem (p. 5), verbatim (this is the ineffectivity source):

> "Theorem. If c_1 is a suitable positive constant, N arbitrary, there is
> at most one primitive character chi to a modulus r <= N: for which
> L(s, chi) has a real zero beta satisfying
> (3.1)  beta > 1 - c_1/log N."

(p. 5), verbatim: "Such an exceptional character chi must be real, which
means also that its conductor r is squarefree, apart from the possibility
that the prime 2 appears in the factorization of r with an exponent 2 or 3.
We have also

> (3.2)  beta < 1 - c_2/(sqrt(r) log^2 r) [Dav, p. 96],
>        beta < 1 - c_3/sqrt(r)  [Pin1, GS]

with effective absolute constants c_2, c_3 > 0." And (p. 6), verbatim: "We
remark that (3.1) and the second inequality of (3.2) imply

> (3.3)  r >= c_4 log^2 N

and for the greatest prime factor q_0 of r

> (3.4)  q_0 >= 2 log_2 N - c_5 > log_2 N  if  N > N_0,

with effective absolute constants c_4, c_5 > 0."

Reformulated Maynard-Tao theorem (p. 6). Framing sentence, verbatim: "We
will slightly reformulate Theorem 4.2 of [BFM] which itself is an improved
reformulation of the original Maynard-Tao theorem. We remark that in order
to obtain Theorems 1-3 (with a constant C larger than 50, respectively with
a proportion less than 1/50 = 2%) one could use also the more complicated
method of Zhang [Zha]. However, to obtain a new proof of Theorem 4 we need
the Maynard-Tao method."

> "Theorem (Maynard-Tao). Let k = k_m be an integer, epsilon =
> epsilon(k, n) > 0 be sufficiently small, N > N_0(epsilon, k, m). Further,
> let
> (3.5)  k + 1 < C_6(epsilon) < h_1 < h_2 < ... < h_k <= N,
>        H = H_k = {h_i}_{i=1}^k admissible,
> (3.6)  Delta(H) := prod_{1<=i<j<=k} (h_j - h_i),
>        ( q_0 prod_{i=1}^k h_i, Delta(H) ) = 1,  Delta(H) < N^epsilon.
> (3.7)  For m = 2 let k = 50
> and generally let
> (3.8)  k_m = C_7 e^{5m}
> with suitably chosen constants C_7 and C_6(epsilon), depending on
> epsilon. Then we have at least m primes among n + H_k = {n + h_i}_{i=1}^k
> for some n in (N, 2N]."

[TRANSCRIPTION-UNSURE: "epsilon = epsilon(k, n)" is as printed in both the
rendered page and the text layer; almost certainly a misprint for
epsilon(k, m), given "N > N_0(epsilon, k, m)".]

Remark 1 (p. 6), verbatim:

> "Remark 1. In the proof of our Theorems 1-4 we will have
> (3.9)  h_k <= g(N) log N < log^2 N,
> thus the second condition of (3.6) will be trivially fulfilled."

Remark 2 (p. 7), verbatim:

> "Remark 2. In the mentioned applications we will choose the values h_i as
> primes, so the first condition of (3.6) will be equivalent to
> (3.10)  q_0 nmid h_j - h_i, h_t nmid h_j - h_i for any t in [1, k],
>         1 <= i < j <= k.
> Since in the applications the only other condition will be with some
> functions xi_i(N) to have
> (3.11)  h_i = (1 + o(1)) xi_i(N),  xi_i(N) << g(N) log N
> it will make no problem to choose step by step primes h_i satisfying
> (3.9)-(3.10). Also h_i in P, h_i > k assures that H_k is admissible."

The z-congruence framework (p. 7), verbatim: "The Maynard-Tao method
assures the existence of at least m primes among numbers of the form

> (3.12)  n + h_i (1 <= i <= k) with n == z (mod W)

with any z in [1, W] and for some n in (N, 2N], N sufficiently large, if

> (3.13)  ( prod_{i=1}^k (z + h_i), W ) = 1.

The pure existence of such a z follows from the admissibility of H_m but
its actual choice is crucial in the applications."

Compatibility conditions (p. 7), verbatim: "In order for the method of
Maynard-Tao and Banks-Freiberg-Maynard [BFM] to work we must assure still
(see [BFM]) with a sufficiently large C_8(epsilon)

> (3.14)  Delta(H) = prod_{1<=i<j<=k} (h_j - h_i) | W;
>         prod_{p <= C_8(epsilon)} p | W

and for the possibly existing greatest prime factor q_0 of the possibly
existing exceptional modulus r,

> (3.15)  q_0 nmid W (if such a modulus r, and so q_0 exists);

further (P^+(n) will denote the greatest prime factor of n)

> (3.16)  P^+(W) < N^{epsilon/log_2 N},  W < N^{2epsilon}."

The key target property (p. 8), verbatim:

> "If we succeed to show the existence of a pair (z, W) with (3.13)-(3.16)
> and the crucial additional property that with a suitable c_9(epsilon)
> (3.17)  (z + s, W) > 1  if  s notin H,  1 < s <= c_9(epsilon) g(N) log N,
> then we can assure that all numbers z + s with (3.17) have a prime
> divisor p | W. Consequently all n + s, s != h_i, s in
> (1, c_9(epsilon) g(N) log N] will be composite if n in (N, 2N]."

(p. 8, verbatim): "In order to achieve this, we will use the Erdos-Rankin
method. After this we can show Theorems 1-4 with suitable choices of H_k."

Erdos-Rankin parameters (p. 8), verbatim: "We will choose the following
parameters (p will always denote primes), H = H_i, c_10(epsilon) =
2 c_9(epsilon)/epsilon,

> (3.18)  L = epsilon log N,  v = log^3 L,
>         U = c_10(epsilon) g(e^L) L > c_9(epsilon) g(N) log N,
> (3.19)  y = exp( (1/(k+5)) log L log_3 L / log_2 L ),
> (3.20)  P_1 = prod*_{p <= v} p,
> (3.21)  P_2 = prod*_{v < p <= y} p,
> (3.22)  P_3 = prod*_{y < p <= L/2} p,
> (3.23)  P_4 = prod*_{L/2 < p <= L} p,

where prod*_p means

> (3.24)  p notin H' := H cup {q_0}."

[PRINTED-ODDITY: "H = H_i" is as printed (presumably H = H_k).]
[TRANSCRIPTION-UNSURE: in (3.18), "v = log^3 L" -- the text layer reads
"v = log3 L"; the rendered page shows the cube of log L, consistent with
log v ~ 3 log_2 L used at (4.12). A reading v = log_3 L (triple iterated
log) is inconsistent with (4.12) "(log v/log y)" asymptotics.]

> "(3.25)  W_0 = P_1 P_2 P_3 P_4,
>          W = [ prod*_{p <= L} p, Delta_0(H) ] = [P_1 P_2 P_3 P_4,
>          Delta_0(H)]
> where Delta_0(H) denotes the squarefree part of Delta(H). This choice of
> W clearly satisfies both conditions of (3.16) by the Prime Number Theorem
> if we additionally require the condition valid in all applications:
> (3.26)  h_k <= log^2 N."

---

## 5. SECTION 4: THE ERDOS-RANKIN SIEVE OF THE WINDOW (anatomy)

[PARAPHRASE of structure, with verbatim load-bearing steps.] The residue
class z mod W is built prime-by-prime so that every s in (1, U] outside H
shares a factor with W:

Step 1 (p. 9), verbatim: "(4.1) z == 0 (mod P_1 P_3). This implies by
v L/2 > U that (4.2) (z + s, P_1 P_3) = 1 (1 < s <= U) if and only if
(s, P_1 P_3) = 1, that is, if and only if either

> (4.3)  s = p q_0^alpha prod_{i=1}^k h_i^{alpha_i} (alpha >= 0,
>        alpha_1 >= 0, ..., alpha_m >= 0) and p > L/2

or

> (4.4)  s is composed only of primes p | P_2 q_0 prod_{i=1}^k h_i."

[PRINTED-ODDITY: "alpha_m" in (4.3) as printed, presumably alpha_k.]

Step 2 (pp. 9-10): smooth-number count. Lemma 1 (p. 10), verbatim:

> "Lemma 1. Let Psi(x, y) denote the number of positive integers n <= x
> which are composed only of primes <= y. For y <= x, y -> infty,
> x -> infty we have
> (4.5)  Psi(x, y) <= x exp[ - log x (log_3 y / log y)
>        + (1 + o(1)) log_2 y ].
> This is a slightly simplified form of Lemma 5 of [Mai1]."

Applying it (p. 10), verbatim conclusion of (4.6): the number of s <= U
with (4.4) is

> "<< U/log^2 U <= C_11 (pi(L) - pi(L/2)) / log U"

"which will be negligible compared with the numbers of s <= U with (4.3)."
Count of the main class (p. 10), (4.7), verbatim final bounds:

> "A'_0 <= (1+o(1)) U/log U (1 + 1/q_0 + 1/q_0^2 + ...)
>   prod_{i=1}^k (1 + 1/h_i + 1/h_i^2 + ...)
>   ~ U/log U (1 - 1/q_0)^{-1} prod_{i=1}^m (1 - 1/h_i)^{-1} <= 2U/log U
> if C_6(epsilon) was chosen sufficiently large depending on k."

Step 3 (p. 11): greedy sieving by primes p | P_2 avoiding the forbidden
classes (4.8) z_{p_j} + h_i != 0 (mod p_j); stopping rule (4.9)
A'_{j-1} <= L/(5 log L); the loss from avoiding k residue classes is
controlled by (4.10)

> "k ceil(U/y) (log_2 L)^{k+1} < L/log^{10} L < A'_{j-1}/(2 (log L)^8)"

and each step retains (4.11)

> "A'_j < A'_{j-1} (1 - (1 - 1/(2(log L)^8))/p_j)
>       < A_j (1 - 1/p_j)^{1 - (log L)^{-8}}."

Final residual set (p. 12), (4.12), verbatim final chain:

> "A* < A'_0 prod_{v<p<=y} (1 - 1/p)^{1-(log L)^{-8}}
>    ~ A'_0 (log v/log y)^{1-(log L)^{-8}}
>    ~ A'_0 (3(k+5) log_2^2 L / (log L log_3 L))
>    < 7kU/(log U g(e^L)) < 7k c_10(epsilon) L / log L
>    < (pi(L) - pi(L/2))/3."

Step 4 (p. 12), verbatim: "we obtain finally that using the prime factors
of P_2, with a suitable choice of z_p for these primes we can already reach
for the numbers s with 1 < s <= U, (z + s, P_1 P_3) = 1 apart from an
exceptional set S of size at most (pi(L) - pi(L/2))/2 the crucial relations

> (4.13)  (z + s, P_2) > 1  if  s notin H,  s notin S
> and
> (4.14)  (z + s, P_2) = 1  if  s in H,  s notin S."

Step 5 (p. 12), verbatim: "Then by |S| < (pi(L) - pi(L/2))/2 we can easily
find for any s in S a suitable prime p | P_4 = {p in (L/2, L], p notin H}
with p nmid prod_{i=1}^k (s - h_i) and consequently a z_p (mod p) with

> (4.16)  z_p + s == 0 (mod p) for s in S',
>         z_p + t != 0 (mod p) for t in H."

Step 6 (p. 13): the remaining primes ((i) p in H -> p > C_6(epsilon);
(ii) p = q_0 -> p >= log_2 N (if q_0 <= W); (iii) remaining unused p | P_4
-> p > L/2; (iv) p | W/W_0 -> p > L) only need (4.18) z_p != -t (mod p) if
t in H, "But this makes no problem since |H| = k <
min{C_6(epsilon), log_2 N, L/2} by (3.5)." (p. 13, verbatim)

Outcome (p. 13), verbatim:

> "So we finally determined a z mod W with the property that for s in
> (1, U] we have
> (4.19)  (z + s, W) = 1  if and only if  s in H.
> Consequently if n == z (mod W), then
> (4.20)  (n + s, W) = 1  if and only if  s in H."

---

## 6. SECTION 5: THE TRANSPORT PROOFS OF THEOREMS 1-4

### 6.1 The summary supply statement

(p. 13), verbatim: "We summarize the results of Sections 3 and 4 with the
aim of applications in Theorems 1-4. Let k, m, epsilon be chosen satisfying
(5.1), let epsilon = epsilon(k, m) > 0 be a sufficiently small constant,
N > N_0(epsilon, k, m):

> (5.1)  k = 50, m = 2  or  k_m = C_7 e^{5m}.

Let H = {h_i}_{i=1}^k subset P satisfying

> (5.2)  [h_t, q_0] nmid prod_{1<=i<j<=k} (h_j - h_i)  for any t in [1, m],
>        q_0 defined in (3.1)-(3.4),
> (5.3)  k + 1 < C_6(epsilon) < h_1 < ... < h_k <= log^2 N,
> (5.4)  U = c_9(epsilon) g(N) log N,
>        g(N) = log_2 N log_4 N / log_3^2 N,  N' = pi(N).

Then we can find suitable values of

> (5.5)  W < N^epsilon,  z (mod W)

and an n in [N', 2N') such that we have at least m primes among n + h_i and
all numbers of the form n + s are composite if s in (1, U] \ H."

[PRINTED-ODDITY: "t in [1, m]" in (5.2) as printed; (3.10) had t in [1,k].]
[PARAPHRASE, bookkeeping note: N' = pi(N) converts to prime-index scale:
for gap indices n in [N', 2N') = [pi(N), 2pi(N)) the primes p_n run over
approximately [N, 2N), so the same letter n is used both for the shifted
integer of (3.12) (n in (N, 2N]) and for the gap index in (5.7)-(5.12);
by (1.5), f(n) = (1 + O(epsilon)) f(N') throughout the block. The paper
does not spell this out beyond the definition N' = pi(N) in (5.4).]

First Remark (p. 14), verbatim (load-bearing for window control):

> "Remark. This implies that all (at least m) primes in the interval
> (n+1, n+U) are of the form n + h_j, h_j in H."

Second Remark (p. 14), verbatim (elimination of epsilon): "We used the
introduction of the variable epsilon since it was formulated in this way in
[BFM]. However, since there is an exact connection (5.1) between k and m
and epsilon depends just on k and m, in the applications we can write in
(5.3) C_6'(k) instead of C_6(epsilon), C_8'(k) in place of C_8(epsilon) in
(3.14) and c_9'(k) instead of c_9(epsilon) in (5.4), c_10'(k) instead of
c_10(epsilon) before (3.18), further c_11'(k) in place of epsilon in (5.5).
Similarly we can choose L = c_12(k) log N with a small c_12(k) in (3.18).
Additionally, if m = 2, k = 50, these are just absolute constants (which is
the case in Theorems 1, 2 and 3)."

### 6.2 Proof of Theorem 1: the calibrated 50-interval contradiction

(p. 14), verbatim: "In order to prove Theorem 1, suppose, in contrary to
its assertion, that we have a sequence of 50 positive numbers c*_nu,
delta_nu (1 <= nu <= 50) satisfying with two constants c*, N* > 0

> (5.6)  J_nu := [c*_nu, c*_nu + delta_nu],
>        c*_nu > 4 delta_nu > 20 c*_{nu+1},  c*_1 < c*,
> (5.7)  { d_n / f(n) }_{n=N*}^infty cap ( U_{nu=1}^{50} J_nu ) = emptyset.

Let

> (5.8)  I_nu(n) := [ c*_nu f(n), (c*_nu + delta_nu) f(n) ]
>        for nu = 1, 2, ..., 50.

Then

> (5.9)  d_n notin U_{nu=1}^{50} I_nu(n)  for nu = 1, 2, ..., 50,
>        n in [N', 2N'), N' > N*."

[TRANSCRIPTION-UNSURE: the asterisk on c*_{nu+1} in "20 c*_{nu+1}" of
(5.6); the text layer prints "20 c_{nu+1}" but the rendered page shows the
starred constant, and the calibration only makes sense between starred
constants.]

(p. 15), verbatim: "We will choose now the primes h_1 < h_2 < ... < h_50
consecutively, satisfying (5.2)-(5.3) and a sufficiently small epsilon > 0,
N' > max(N_0(epsilon), N*)

> (5.10)  h_nu in I'_{51-nu}(n) := [ (c*_{51-nu} + delta*_{51-nu}/2)
>         (1 + epsilon) f(N'), (c*_{51-nu} + delta_{51-nu})(1 - epsilon)
>         f(N') ].

This choice (for nu = 1, ..., 50) is easily assured by the Prime Number
Theorem if epsilon was chosen sufficiently small, N_0(epsilon) sufficiently
large depending on all c*_nu, delta_nu (1 <= nu <= 50) and epsilon. So we
have for 1 <= nu < mu <= 50 for large enough N'

> (5.11)  h_mu - h_nu in [ (c*_{51-mu} + delta_{51-mu}/2 - 2 c*_{52-mu})
>         (1 + epsilon) f(N'), (c*_{51-mu} + delta_{51-mu})(1 - epsilon)
>         f(N') ] := I*_{51-mu}(n) subset I_{51-mu}(n).

This contradicts to (5.9) since we have for at least one pair of
consecutive primes

> (5.12)  d_n = h_mu - h_nu,  n in [N', 2N')  q.e.d."

[PRINTED-ODDITY: the star on delta*_{51-nu} in (5.10) appears only there;
delta_nu is unstarred elsewhere.]

[PARAPHRASE of the mechanism: the c*_nu decrease geometrically by (5.6), so
for ANY pair nu < mu the difference h_mu - h_nu (the smaller entry h_nu
being at scale c*_{51-nu} <= c*_{52-mu} <= c*_{51-mu}/20 relative to
h_mu) lands in the designated interval I_{51-mu}(n) indexed by the LARGER
element mu alone. Since the machinery guarantees at least 2 primes among
the 50 candidates and no other primes in the window (first Remark, p. 14),
some pair of candidates are consecutive primes and their gap d_n falls in
one of the 50 forbidden intervals -- contradiction. Which of the 50
intervals is hit is not controlled.]

### 6.3 Proof of Theorem 2 (transport across a chain of normalizers)

(p. 15), verbatim: "Now we turn to the proof of Theorem 2. Let us suppose
that we have 50 functions with f_i(x) nearrow infty, satisfying (1.5),
(1.9), (1.11) and 50 intervals

> (5.13)  J_nu := [c*_nu, c*_nu + delta_nu],
>         I_nu(n) := [c*_nu f_nu(n), (c*_nu + delta) f_nu(n)]

such that with a sufficiently large N* we have

> (5.14)  d_n notin U_{nu=1}^{50} I_nu(n)  for nu = 1, ..., 50,
>         n in [N', 2N'), N' > N*.

Then, analogously to (5.10)-(5.11) we can choose the primes h_1 < h_2 <
h_50 with (5.2)-(5.3), epsilon > 0 and N > max(N_0(epsilon), N*) so that

> (5.15)  h_nu in I'_nu(n) := [ (c*_nu + delta_nu/2)(1 + epsilon)
>         f_nu(N'), (c*_nu + delta_nu)(1 - epsilon) f_nu(N') ].

This implies for sufficiently large N' by (1.11) for any 1 <= nu < mu <= 50

> (5.16)  h_mu - h_nu in [ c*_mu (1 + epsilon) f_mu(N),
>         (c*_mu + delta_mu)(1 - epsilon) f_mu(N) ] subset I_mu(n)

and we obtain again a contradiction to (5.14). q.e.d."

[PRINTED-ODDITY: "(c*_nu + delta)" in (5.13) (delta without subscript) and
"f_mu(N)" in (5.16) (N vs N') as printed.]
[PARAPHRASE: here the scale separation is provided not by geometric
calibration of the c*_nu but by the growth condition (1.11)
f_{i+1}/f_i -> infty: h_nu at scale f_nu(N') is negligible against
f_mu(N') for nu < mu, so again every pair difference lands in the interval
indexed by the larger element. Note the proof derives a contradiction from
50 exceptional functions; the theorem statement allows at most 98
exceptional functions, matching the two-case proof of Theorem 2' in
Section 6 (99 functions, split 1-50 and 50-99, p. 20).]

### 6.4 Proof of Theorem 3 (arbitrary difference patterns)

(p. 16), verbatim: "The first assertion of Theorem 3 follows immediately
from our summary in (5.1)-(5.5) if we choose simply h_1 < h_2 < ... < h_50
satisfying (5.2)-(5.3) and for n in [N', 2N') with

> (5.17)  h_i = beta_i f(N') (1 + O(1/log_2 N')).

The consequence about the at least 2% density of J_f follows in the same
way as in the proof of Corollary 1.2 of [BFM]."

### 6.5 Proof of Theorem 4 (the chain version)

(p. 16), verbatim: "Finally, Theorem 4 is also an obvious corollary of our
summary (5.1)-(5.5). Namely, if for n in [N', 2N') we choose for
i in [1, k_m]

> (5.18)  h_i = i * (U/(k_m + 1)) (1 + O(1/log U))   (k_m = C_7 e^{5m})

with (5.2)-(5.5) then we have in the interval (n + 1, n + U) at least m and
at most k_m primes, all among n + h_i (1 <= i <= k_m). Consequently we get
at least m consecutive primegaps each of size at least

> (5.19)  U/(2(k_m + 1)) >= c_12(k) g(n) log n
>         with g(n) = log_2 n log_4 n / log_3^2 n.  q.e.d."

---

## 7. SECTION 6: TRANSPORT TO THE g_0 SCALE (Theorems 1'-4', Corollary 1')

Two-case split (p. 16), verbatim: "We first remark that apart from Theorem
2 we worked in all proofs (cf. our present Section 5) within a given
interval [N', 2N'] where N' was any sufficiently large constant and we
worked with an H_k tuple satisfying

> (6.1)  H_k = {h_i}_{i=1}^k  with  h_i asymp f(N').

Thus we will consider first the proofs of Theorems 1', 3', 4'. We will
distinguish two cases as follows.

> Case 1.  f(N') < log N' (log_2 N')^{1/2}."

(p. 17), verbatim: "In this case the assertions of Theorems 1', 3', 4'
follow directly from Theorems 1, 3, 4 for the specific interval [N', 2N'].

> Case 2.  f(N') >= log N' (log_2 N')^{1/2}.

In this case we will use the method of [May2], and will describe the needed
changes compared to [May2]. We will use (6.1) which in this case implies

> (6.2)  h_i >> (log N')(log_2 N')^{1/2}  (i = 1, 2, ..., k)."

Maynard large-gap notation (p. 17), verbatim: "In order to follow [May2] we
will change our notation and choose with a given small epsilon_0

> (6.3)  z = epsilon_0 log N',  x = L,  P_y = prod_{p <= y} p,
>        y = exp( (1 - epsilon_0) log x log_3 x / log_2 x ),
>        z = x/log_2 x,  U = C_U x log y / log_2 x,

where C_0 is an arbitrarily large constant as in [May2], independent of
epsilon_0."

[PRINTED-ODDITY: (6.3) defines z twice (z = epsilon_0 log N' and
z = x/log_2 x) and the constant is written C_U in the display but C_0 in
the following sentence; all as printed.]

Initial residue choices (p. 17), verbatim:

> "(6.4)  a_p = 0 for every prime p in (y, z], p != q_0,
> (6.5)  a_p = 1 for every prime p <= y, p != q_0."

Survivor sets (p. 17), verbatim:

> "(6.6)  R = {mp <= U : p > z, m is y-smooth, (mp - 1, P_y) = 1},
>  Rtilde = {m p q_0 <= U : p > z, m is y-smooth, (m p q_0 - 1, P_y) = 1},
>  R' = {m <= U : m is y-smooth, (m - 1, P_y) = 1},
>  Rtilde' = {m q_0 <= U : m is y-smooth, (m q_0 - 1, P_y) = 1}."

Counting inputs (pp. 17-18), verbatim:

> "(6.7)  |R' cup Rtilde'| << x/(log x)^{1+epsilon}."

> "(6.8)  #{z < p <= V : (mp - 1, P_y) = 1} = ((V - z)/log x)
>         prod_{p <= y, p nmid m} ((p-2)/(p-1)) (1 + o(1))"
for V in [z + z/log x, x (log x)^2], "and in particular for even
m <= U(1 - 1/log x)/z

> (6.9)  |R_m| = (2 e^{-gamma} U (1 + o(1)) / (m (log x)(log y)))
>        ( prod_{p>2} p(p-2)/(p-1)^2 ) ( prod_{p|m, p>2} (p-1)/(p-2) )."

> "(6.10)  |Rtilde_m| << U/(q_0 m log x log y) << U/(m log^2 x log y),
> which is negligible compared to (6.9)."  (using "q_0 >= log_2 N'",
p. 18, verbatim)

Goal (p. 18), verbatim: "we should have, similarly to (3.18)

> (6.12)  (a + s, W) > 1  if  s notin H,  1 < s <= U."

with (6.11) W := P_x/q_0. Choice of H (p. 18), verbatim:

> "(6.13)  h_i in P,  (h_i - 1, q_0 P_y) = 1
> and use (6.2) additionally. This means that h_i == 0 (mod p) for some
> p in (y, z] will not occur and we will have
> (6.14)  h_i in R_1  (i = 1, 2, ..., k)."

Size flexibility (p. 19), verbatim: "Since any other essential requirements
for h_i in Sections 3-5 are concerning only the size of h_i requiring

> (6.15)  xi_i(N) <= h_i <= xi_i(N)(1 + eta_i)

for some sufficiently small eta_i independent of N, with some functions
xi_i(N), we can always fulfil these conditions with proper choice of the
primes h_i satisfying (6.13), due to the relations (6.8)-(6.9), which mean
that we have sufficiently large sets to choose {h_i}_{i=1}^k."

Protection of the fixed tuple H*_k (p. 19), verbatim: "After choosing our
set H = {h_i}_{i=1}^k satisfying the requirements of Sections 3-5 for a
given value of N we will denote it by H*_k = {h*_i}_{i=1}^{k*} and consider
it fixed. ... We will choose the set H = {h_1, ..., h_k} in [May2] disjoint
to our H*_k* (and also k will be sufficiently large compared to k* while
our k* will be equal to 50, 99 or k = k(m) in Theorem 4'). The change in
the choice of the probabilities of choosing a mod q in I_1 subseteq
[x/2, x] will be that in contrast to (4.1) of [May2] we will set
(mu*_{1,q}(a) will denote the new probabilities, alpha*_{1,q} the new
normalizing number to have sum_{a(q)} mu*_{1,q}(a) = 1)

> (6.16)  mu*_{1,q}(a) := 0  if  exists i in [1, k*],
>         a + h*_i == 0 (mod q),
> (6.17)  mu*_{1,q}(a) := mu_{1,q}(a) * alpha*_{1,q}/alpha_{1,q}
>         otherwise."

(p. 19), verbatim: "In this way we can avoid that by the random choice of
a_q modulo q we should have q | n + h*_i for n == a (mod W) for some
i in [1, k*], since we give 0 probability to those a_q in (6.16). ... This
means that none of the h*_i in R_1 will be sieved out (with probability 1)
by the above random sieve procedure. On the other hand we have to show
that, similarly to the end of Section 6 on p. 13 of [May2], for all but
o_k(|R_1|) primes p_0 in R_1 the expected number sum_q mu*_{1,q}(p_0) of
times p_0 in R_1 is chosen will remain >> delta log k if p_0 notin H* as in
[May2] in case of the original choice of mu_{1,q}(p_0)."

The at-most-one-q lemma (p. 20), verbatim: "How many different q's do we
have at most in I_1 subseteq [x/2, x] with

> (6.20)  p_0 == h*_i (mod q)?

The answer is simple: at most one. If we had, namely, (6.20) for
q = q_1, q_2 in I_1 (q_1 != q_2), then this would imply by
q_1 q_2 >= x^2/4 > U >= max(p_0, h*_i)

> (6.21)  p_0 == h*_i (mod q_1 q_2),
> consequently
> (6.22)  p_0 = h*_i in H*."

(p. 20), verbatim: "So the remaining question is reduced to show that if we
delete at most k* = O(1) terms from the original sum sum_q mu_{1,q}(p_0)
the sum will be still >> delta log k. But this follows already from the
trivial relation mu_{m,q}(a) <= 1 ... (k can be chosen sufficiently large
compared with k*.) This completes the proof of Theorems 1', 3', 4' (and
thereby Corollary 1')."

Theorem 2' (p. 20), verbatim: "In case of Theorem 2' we consider a given N'
and distinguish the following two cases. Let us consider a sequence of 99
exceptional functions.

> Case 1*.  f_50(N') < log N' (log_2 N')^{1/2}.
> In this case the proof of the original Theorem 2 can be applied to the
> increasing subset {f_i(x)}_{i=1}^{50}.
> Case 2*.  f_50(N') >= log N' (log_2 N')^{1/2}.
> In this case the new method of [May2] together with the changes of the
> present section yields the result for the increasing subset
> {f_i(x)}_{i=50}^{99}.

Thus, in both cases we obtain a contradiction if we suppose for an
increasing sequence of at least 99 functions that the relation (1.12)
fails."

Remark 3 (p. 21), verbatim:

> "Remark 3. With some extra effort it would also be possible to show
> Theorem 2' with 49 instead of 98."

Remark 4 (p. 21), verbatim (effectivity):

> "Remark 4. If we define additionally
> (6.23)  lambda_{d_1,...,d_k,e_1,...,e_k} = 0  if
>         q_0 | prod_{i=1}^k (d_i e_i),
> then the whole result can be made effective. (We remark that actually we
> have a loss of size 1 + O(1/q_0) = 1 + o(1) due to (6.23) but this does
> not affect the validity of the argument.)"

Acknowledgement (p. 21), verbatim: "The author would like to express his
sincere gratitude to Imre Z. Ruzsa, who called his attention that a
possible combination of the methods of Erdos-Rankin and Zhang-Maynard-Tao
might lead to stronger results about gaps between consecutive primes."

---

## 8. TARGETED SEARCHES (negative results)

Searched the full text layer (1023 lines, all 22 pages) for: "irrational",
"binary", "digit", "2^n", "#251", "series", "sum p_n". Result: NOT FOUND in
this text. The paper contains nothing on Erdos #251, the series
sum p_n/2^n, irrationality, or digit representations.

Chain statements: the ONLY several-consecutive-gaps results are Theorem 4 /
Theorem 4' (Sections 1-2) with proof at (5.18)-(5.19) (Section 5) -- m
consecutive gaps all LARGE (each >= c_12(k) g(n) log n), m a fixed natural
number. There is NO chain version of the limit-point/normalizer statements
(no simultaneous prescription of several consecutive normalized gap ratios
d_{n+1}/f, d_{n+2}/f, ...): NOT FOUND in this text. The reference [Mai1]
(H. Maier, "Chains of large gaps between consecutive primes", Adv. in Math.
39 (1981)) supplies the compared prior chain result (p. 4 and p. 22).

Explicit scales for the limit points: NOT FOUND. All conclusions are
derived-set / limsup statements ((1.2), (1.10), (1.12), (1.13), (1.15));
the proofs are by contradiction over arbitrary dyadic index windows
[N', 2N') (see (5.7)/(5.9), (5.14)) and identify no explicit sequence n_j
along which a given limit point is attained, nor which of the 50 calibrated
intervals is hit in a given window ((5.11)-(5.12) pigeonhole).

---

## COMMENTARY (assessment, NOT extraction)

Answers to the focus questions, then an assessment against the project's
exchange-configuration target.

FOCUS 1 (main theorems; exact class F; exact conclusions). All main
theorems are transcribed verbatim in Sections 2-3 above. The class F is:
f(x) nearrow infty (monotone increase to infinity), the dyadic
slow-variation condition (1.5) ((1-epsilon)f(N) <= f(n) <= (1+epsilon)f(N)
on [N, 2N] for N > N_0(epsilon), for any epsilon), and the growth cap
(1.9): f(x) <= c_0 g(x) log x, where g(x) = log_2 x log_4 x/(log_3 x)^2 is
the Erdos-Rankin function (1.7); in the stronger forms (Theorems 1'-4',
Corollary 1', Section 2) the cap is f(x) <= c_0 g_0(x) log x with
g_0 = omega_0 g, omega_0 -> infty implicit in Maynard [May2] (2.1)-(2.2).
So the project's note "f grows at most like a specific scale" is verified
with the exact scale g(x) log x (Rankin scale), NOT "f << R" for any
unstructured R; and f must also satisfy the structural conditions
(monotone + (1.5)). The conclusion for a SINGLE given f is only
[0, c_f] subset J_f with c_f ineffective (Theorem 1, (1.10)) -- not
J_f = [0, infty]. Full [0, infty] = J_f is reached only (a) for all but at
most 98 members of any chain with f_{i+1}/f_i -> infty (Theorem 2,
(1.11)-(1.12); 49 possible per Remark 3), or (b) for SOME unspecified f
squeezed between eta(x)F(x) and F(x) (Corollary 1, (1.14)-(1.15)).
Theorem 3 gives the difference-pattern/2%-density universality for every f
in the class.

FOCUS 2 (transport/universality mechanism). The mechanism has five
separable stages, each with a clean anchor:
(i) Maynard-Tao supply: >= m primes among n + H_k for some n in (N, 2N],
    in a prescribed residue class n == z (mod W) provided (3.13); k = 50
    for m = 2, k_m = C_7 e^{5m} in general (Theorem (Maynard-Tao),
    (3.5)-(3.8), (3.12)-(3.13), p. 6-7).
(ii) Erdos-Rankin window sieve: construction of (z, W), W < N^{2epsilon},
    with (z + s, W) = 1 iff s in H for all s in (1, U],
    U = c_9(epsilon) g(N) log N ((3.17), Section 4 steps (4.1)-(4.16),
    outcome (4.19)-(4.20)). This forces every non-designated position in
    the length-U window to be composite and is what caps the class F at
    the Rankin scale (1.9) -- the cap is exactly the reach of the
    Erdos-Rankin method, upgraded to g_0 via Maynard's [May2] sieve in
    Section 6 (Case 2, (6.3)-(6.22)).
(iii) Summary interface: for suitable H = {h_i} subset P with
    h_k <= log^2 N there is n with >= m primes among n + h_i and ALL
    primes of (n+1, n+U) among the designated sites ((5.1)-(5.5) and the
    first Remark, p. 14).
(iv) Free placement: the designated sites h_i are primes chosen by PNT in
    any prescribed windows of relative width epsilon at scale f(N')
    ((5.10), (5.15), (5.17), (5.18); size-only requirement (3.11)/(6.15)).
    This is where an arbitrary normalizer f enters: sites are placed at
    positions beta * f(N').
(v) Blindness-robust calibration: since it is unknown WHICH >= m of the k
    candidates are prime, the site pattern is designed so that EVERY pair
    difference h_mu - h_nu lands in a designated target: geometric decay
    of the interval scales for Theorem 1 ((5.6), (5.10)-(5.11)); scale
    separation f_{i+1}/f_i -> infty for Theorem 2 ((5.15)-(5.16));
    all-pairs difference set for Theorem 3 ((5.17)); equal spacing for
    Theorem 4 ((5.18)-(5.19)). Transport from normalization f to another
    normalization is nothing deeper than re-placing the free sites at the
    new scale and re-calibrating; the two proof engines are switched by
    the threshold f(N') vs log N' (log_2 N')^{1/2} (Section 6, Case 1 /
    Case 2, p. 16-17).

FOCUS 3 (chain versions). Theorem 4 = (1.13) (and Theorem 4') is the only
chain statement: for any FIXED natural m, infinitely often m consecutive
gaps d_{n+1}, ..., d_{n+m} are simultaneously >= c g(n) log n. It costs
k_m = C_7 e^{5m} candidate sites (3.8) inside one window of length
U asymp g(N) log N, with equal spacing (5.18) making every realized
consecutive-gap at least U/(2(k_m+1)) (5.19) regardless of which sites
fire. No chain version of the limit-point theorems exists in the paper
(Section 8 above). The statement is for fixed m with N > N_0(epsilon,k,m)
(Maynard-Tao preamble, p. 6); no uniformity of m in N is claimed anywhere.

FOCUS 4 (ineffectivity / subsequence caveats). (a) c_f in Theorem 1 is
declared ineffective in the statement itself ("suitable (ineffective)
constant c_f", (1.10)); the source is the possibly existing exceptional
(Landau-Page/Siegel) modulus r with greatest prime factor q_0
((3.1)-(3.4)), which must be dodged by W ((3.15), (3.24)) and by the tuple
conditions ((3.6), (3.10), (5.2)). Remark 4 (p. 21) states the whole
result CAN be made effective by zeroing the sieve weights lambda when
q_0 | prod d_i e_i (6.23), at a 1 + O(1/q_0) loss. (b) Limit points are
NOT achieved along explicit scales: every conclusion is a derived-set or
limsup statement; the proof contradicts a hypothesized avoidance on ALL
index windows [N', 2N') with N' > N* ((5.7), (5.9), (5.14)), so it shows
each sufficiently large dyadic window contains SOME hit of SOME one of 50
calibrated intervals, with no control of which interval, which pair
(mu, nu) fires (5.12), or where in [0, c_f] the produced limit point sits.
This is pigeonhole-blindness in exactly the project's sense.

ASSESSMENT AGAINST THE EXCHANGE-CONFIGURATION TARGET (two prime-gap-word
sites with matched J-prefix and K-suffix windows, dominant weighted middle
difference, depths J, K ~ log_2 log x, unconditional):

What the machinery CAN supply, unconditionally:
1. Single-window total gap-environment control at Rankin scale: an n such
   that the interval (n+1, n+U), U asymp g(N) log N, contains >= m and
   <= k_m primes, ALL located among k_m freely pre-placed sites h_i
   (first Remark p. 14; (5.17)-(5.18)). Inside such a window every
   realized gap word is a word in differences of prescribed h's. This is
   a genuine unconditional site-supply device that is NOT of Shiu-string
   type and is NOT circular: its inputs are the Erdos-Rankin sieve
   ((3.18)-(3.26), Section 4) and Maynard-Tao, with all parameters at
   scale log N / g(N) log N, nowhere a (2q)^{-exp(Cm)} density.
2. Blindness-robust design: the calibration devices (v) above ((5.6),
   (5.11); (5.18)) show how to neutralize pigeonhole-blindness (project
   blocker (i)) for SIZE statements: design the candidate configuration so
   every possible firing pattern yields the desired conclusion. If the
   exchange configuration can be reformulated so that every outcome of the
   Maynard-Tao selection inside one window produces an admissible pair of
   sites with dominant middle difference, blocker (i) is bypassed rather
   than solved. The equal-spacing variant (5.18) is the natural template:
   all realized middle differences are near-multiples of U/(k_m+1), which
   gives approximate CONGRUENCE/size structure of the middle difference
   without knowing the firing pattern.
3. Parity-compliance template: the paper never lower-bounds a prescribed
   gap pattern (which would be the parity-blocked tuple bound, project
   blocker (ii)); it forces the COMPLEMENT composite (a sieve upper-bound
   task, (4.19)-(4.20)) and only counts >= m primes among k_m candidates
   (Maynard-Tao). The price is exponential: k_m = C_7 e^{5m} (3.8). This
   confirms the project's diagnosis and exhibits the only currently
   unconditional channel and its exact cost.

What the machinery CANNOT supply toward the target:
4. No two-site coupling: the construction produces ONE window per scale;
   nothing anywhere in the paper couples two distinct sites n, n~ so as to
   match gap words (prefix/suffix) between them. Matched J-prefix and
   K-suffix windows at two sites are simply outside the method's
   expressive range: even inside one window the realized word depends on
   the unknown firing pattern, and outside the window (below n+1, above
   n+U) the adjacent gaps are entirely uncontrolled.
5. Depth mismatch for chains: matched windows at depth J, K ~ log_2 log x
   would need ~ log_2 log x consecutive controlled gaps at each site.
   The only chain result (Theorem 4) is for FIXED m; pushing m to grow
   with N is not attempted, and the exponential candidate cost
   k_m = C_7 e^{5m} against the window diameter cap h_k <= log^2 N
   ((3.9)/(3.26)) would cap any hypothetical uniformization at
   m <~ (2/5) log_2 N [extractor arithmetic, not in the paper -- the same
   order as log_2 log x up to constant, so the obstruction is a missing
   uniform-in-m Maynard-Tao theorem with explicit N_0(epsilon, k, m)
   dependence, not a hard scale barrier]. The paper itself flags only the
   easier uniformity "in the variable k of [May2] for k asymp
   (log x)^alpha" as structure-preserving (p. 5).
6. No location control / density: the supply is existence-only ("for some
   n in (N, 2N]", Maynard-Tao theorem p. 6), one site per dyadic block,
   with ineffective location unless the Remark 4 (6.23) modification is
   traced through; no positive density of good n is stated, so the device
   cannot directly feed a counting or measure argument over sites.
7. Gap sizes are Rankin-large: all gaps produced/controlled are at scale
   f(N') in [roughly log N (for the trivial lower end of J_f) up to
   c_0 g_0(N) log N]. The exchange target concerns the fine structure of
   typical-scale words; this machinery lives at the large-deviation end
   and controls only ratios d_n/f(n) hitting prescribed intervals along
   unspecified subsequences.

Net: the paper supplies (unconditionally) the strongest known
one-window/site device -- complete knowledge of WHERE primes can sit in a
window of length asymp g(N) log N plus a guaranteed count -- and two
transferable design tricks against blockers (i) and (ii); it supplies
nothing toward two-site word matching, typical-scale words, depth
~ log_2 log x chains, or effective/explicit site locations.

---

## FLAGS (consolidated)

1. No abstract exists in the paper; extraction starts from Section 1.
2. [TRANSCRIPTION-UNSURE] "epsilon = epsilon(k, n)" in the Maynard-Tao
   theorem (p. 6): printed "n", almost certainly "m".
3. [PRINTED-ODDITY] Theorem 4 (1.13): limsup subscript "h -> infty".
4. [PRINTED-ODDITY] Theorem 2 hypothesis "f(x) nearrow infty" (for
   f_i(x)); (5.13) "(c*_nu + delta)" missing subscript; (5.16) "f_mu(N)"
   vs f_mu(N'); (4.3) "alpha_m >= 0" vs alpha_k; (3.18) "H = H_i";
   (5.2) "t in [1, m]" vs [1, k]; (6.3) double definition of z and
   C_U vs C_0. All transcribed as printed.
5. [TRANSCRIPTION-UNSURE] (5.6): asterisk on c*_{nu+1} in
   "4 delta_nu > 20 c*_{nu+1}" -- text layer drops the star, rendered page
   appears starred; calibration logic requires starred.
6. [TRANSCRIPTION-UNSURE] (3.18): v = log^3 L (cube) rather than log_3 L
   (iterated); resolved by the (4.12) asymptotics log v ~ 3 log_2 L.
7. [PRINTED-ODDITY] (5.10): stray star on delta*_{51-nu} (only occurrence
   of a starred delta).
8. [PARAPHRASE] The N' = pi(N) integer-vs-gap-index bookkeeping in
   Section 5 (see the marked note in Section 6.1 above) is my reading; the
   paper conflates the two uses of n without comment.
9. Theorem 2 states "at most 98" while the Section 5 proof contradicts 50
   exceptional functions and the Section 6 proof (Theorem 2') contradicts
   99; Remark 3 says 49 would be possible for Theorem 2' "with some extra
   effort". Transcribed as printed; the 98 in the unified statement
   matches the 99-function two-case argument.
10. In the commentary, the cap m <~ (2/5) log_2 N for hypothetical
    uniform-in-m chains is extractor arithmetic from (3.8) + (3.26), NOT a
    claim of the paper.
