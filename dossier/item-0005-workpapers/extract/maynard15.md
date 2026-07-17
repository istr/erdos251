# Extraction: Maynard, "Small gaps between primes" (arXiv:1311.4600v3)

Source PDF: /home/istr/pro/erdos251/dossier/1311.4600v3.pdf (25 pages,
arXiv stamp "arXiv:1311.4600v3 [math.NT] 28 Oct 2019").
Scope per task: INTERFACE ONLY -- main theorems verbatim, k-uniformity,
citation targets for prime clusters in admissible tuples.
Method: structure located via pdftotext; all load-bearing statements below
were transcribed from VISUAL reads of pages 1-7 and 17-18 unless a
transcription flag says otherwise. Anchors are theorem/proposition/equation
numbers; page numbers are secondary aid only.

Paper structure: Sec 1 Introduction (Thms 1.1-1.4); Sec 2 An improved GPY
sieve method; Sec 3 Notation; Sec 4 Outline of the proof (Props 4.1-4.3,
derivation of all four theorems); Sec 5 Selberg sieve manipulations;
Sec 6 Smooth choice of y; Sec 7 Choice of smooth weight for large k
(proves Prop 4.3(3)); Sec 8 Choice of weight for small k (proves
Prop 4.3(1),(2)); Sec 9 Acknowledgements.

---

## 1. Main theorems (verbatim)

### Abstract (verbatim, p.1)

> "We introduce a refinement of the GPY sieve method for studying prime
> k-tuples and small gaps between primes. This refinement avoids previous
> limitations of the method, and allows us to show that for each k, the
> prime k-tuples conjecture holds for a positive proportion of admissible
> k-tuples. In particular, lim inf_n (p_{n+m} - p_n) < \infty for every
> integer m. We also show that lim inf(p_{n+1} - p_n) <= 600, and, if we
> assume the Elliott-Halberstam conjecture, that
> lim inf_n (p_{n+1} - p_n) <= 12 and lim inf_n (p_{n+2} - p_n) <= 600."

### Admissibility and the driving conjecture (Sec 1, p.1, verbatim)

> "We say that a set H = {h_1, ..., h_k} of distinct non-negative integers
> is 'admissible' if, for every prime p, there is an integer a_p such that
> a_p \not\equiv h (mod p) for all h \in H."

> "Conjecture (Prime k-tuples conjecture). Let H = {h_1, ..., h_k} be
> admissible. Then there are infinitely many integers n such that all of
> n + h_1, ..., n + h_k are prime."

### Level of distribution (eq. (1.3), p.1, verbatim modulo LaTeX retyping)

Given theta > 0, the primes have 'level of distribution theta' if, for
every A > 0:

  \sum_{q <= x^\theta} \max_{(a,q)=1} | \pi(x;q,a) - \pi(x)/\phi(q) |
    \ll_A x / (\log x)^A.                                        (1.3)

Footnote 1 (p.1, verbatim): "We note that different authors have given
slightly different names or definitions to this concept. For the purposes
of this paper, (1.3) will be our definition of the primes having level of
distribution theta."

### Theorem 1.1 (p.2, verbatim)

> "Theorem 1.1. Let m \in N. We have
>     lim inf_n (p_{n+m} - p_n) \ll m^3 e^{4m}."

Immediately following remarks (p.2, verbatim):
> "Terence Tao (private communication) has independently proven Theorem 1.1
> (with a slightly weaker bound) at much the same time."
> "We see that the bound in Theorem 1.1 is quite far from the conjectural
> bound of approximately m log m predicted by the prime m-tuples
> conjecture."

Generalization remark (p.2, between Thm 1.1 and Thm 1.2, verbatim):
> "Our proof naturally generalizes (but with a weaker upper bound) to many
> subsequences of the primes which have a level of distribution theta > 0.
> For example, we can show corresponding results where the primes are
> contained in short intervals [N, N + N^{7/12+\epsilon}] for any
> \epsilon > 0 or in an arithmetic progression modulo q \ll (\log N)^A.
> In particular, our method gives results for simultaneously prime values
> of linear functions, which might have specific interest. Given k distinct
> linear functions L_i(n) = a_i n + b_i (1 <= i <= k) with positive integer
> coefficients such that the product function \Pi(n) = \prod_{i=1}^k L_i(n)
> has no fixed prime divisor, the method presented here shows that there
> are infinitely many integers n such that at least
> (1/4 + o_{k->\infty}(1)) \log k of the L_i(n) are prime."

### Theorem 1.2 (p.2, verbatim) -- positive proportion statement

> "Theorem 1.2. Let m \in N. Let r \in N be sufficiently large depending on
> m, and let A = {a_1, a_2, ..., a_r} be a set of r distinct integers. Then
> we have
>
>   #{{h_1, ..., h_m} \subseteq A : for infinitely many n all of
>       n + h_1, ..., n + h_m are prime}
>   / #{{h_1, ..., h_m} \subseteq A}   \gg_m  1."

Following sentence (p.2, verbatim): "Thus a positive proportion of
admissible m-tuples satisfy the prime m-tuples conjecture for every m, in
an appropriate sense."

### Theorem 1.3 (p.3, verbatim)

> "Theorem 1.3. We have
>     lim inf_n (p_{n+1} - p_n) <= 600."

Following remark (p.3, verbatim):
> "We emphasize that the above result does not incorporate any of the
> technology used by Zhang to establish the existence of bounded gaps
> between primes. The proof is essentially elementary, relying only on the
> Bombieri-Vinogradov theorem."

### Theorem 1.4 (p.3, verbatim)

> "Theorem 1.4. Assume that the primes have level of distribution theta for
> every theta < 1. Then
>     lim inf_n (p_{n+1} - p_n) <= 12,
>     lim inf_n (p_{n+2} - p_n) <= 600."

Optimality remark after Thm 1.4 (p.3, verbatim):
> "Although the constant 12 of Theorem 1.4 appears to be optimal with our
> method in its current form, the constant 600 appearing in Theorem 1.3 and
> Theorem 1.4 is certainly not optimal. By performing further numerical
> calculations our method could produce a better bound, and also most of
> the ideas of Zhang's work (and the refinements produced by the polymath
> project) should be able to be combined with this method to reduce the
> constant further. We comment that the assumption of the Elliott-Halberstam
> conjecture allows us to improve the bound on Theorem 1.1 to O(m^3 e^{2m})."

---

## 2. Core interface: the engine propositions (Sec 4)

Setup (Sec 2 and Sec 4): GPY sum (eq. (2.1))
  S(N, \rho) = \sum_{N <= n < 2N} ( \sum_{i=1}^k \chi_P(n + h_i) - \rho ) w_n,
with non-negative weights w_n; S(N,\rho) > 0 for all large N implies
infinitely many n with at least floor(\rho + 1) of the n + h_i prime.
New multidimensional weights (eq. (2.4)):
  w_n = ( \sum_{d_i | n + h_i \forall i} \lambda_{d_1,...,d_k} )^2.
W-trick: w_n supported on n \equiv v_0 (mod W), W = \prod_{p <= D_0} p,
D_0 = \log\log\log N (eq. (4.1)). S_1, S_2 defined in (4.2), (4.3).

### Proposition 4.1 (p.5, verbatim)

> "Proposition 4.1. Let the primes have exponent of distribution theta > 0,
> and let R = N^{theta/2 - delta} for some small fixed delta > 0. Let
> \lambda_{d_1,...,d_k} be defined in terms of a fixed smooth function F by
>
>   \lambda_{d_1,...,d_k} = ( \prod_{i=1}^k \mu(d_i) d_i )
>     \sum_{ r_1,...,r_k : d_i | r_i \forall i, (r_i, W) = 1 \forall i }
>     \frac{ \mu( \prod_{i=1}^k r_i )^2 }{ \prod_{i=1}^k \phi(r_i) }
>     F( \frac{\log r_1}{\log R}, ..., \frac{\log r_k}{\log R} ),
>
> whenever ( \prod_{i=1}^k d_i, W ) = 1, and let \lambda_{d_1,...,d_k} = 0
> otherwise. Moreover, let F be supported on
> R_k = { (x_1, ..., x_k) \in [0,1]^k : \sum_{i=1}^k x_i <= 1 }. Then we
> have
>
>   S_1 = \frac{ (1 + o(1)) \phi(W)^k N (\log R)^k }{ W^{k+1} } I_k(F),
>   S_2 = \frac{ (1 + o(1)) \phi(W)^k N (\log R)^{k+1} }{ W^{k+1} \log N }
>         \sum_{m=1}^k J_k^{(m)}(F),
>
> provided I_k(F) != 0 and J_k^{(m)}(F) != 0 for each m, where
>
>   I_k(F) = \int_0^1 ... \int_0^1 F(t_1, ..., t_k)^2 dt_1 ... dt_k,
>   J_k^{(m)}(F) = \int_0^1 ... \int_0^1
>     ( \int_0^1 F(t_1, ..., t_k) dt_m )^2
>     dt_1 ... dt_{m-1} dt_{m+1} ... dt_k."

NOTE (faithful): Prop 4.1 says "exponent of distribution"; Prop 4.2 says
"level of distribution". Both phrases as printed.

### Proposition 4.2 (p.5, verbatim) -- THE cluster-production statement

> "Proposition 4.2. Let the primes have level of distribution theta > 0.
> Let delta > 0 and H = {h_1, ..., h_k} be an admissible set. Let I_k(F)
> and J_k^{(m)}(F) be given as in Proposition 4.1, and let S_k denote the
> set of Riemann-integrable functions F : [0,1]^k -> R supported on
> R_k = { (x_1, ..., x_k) \in [0,1]^k : \sum_{i=1}^k x_i <= 1 } with
> I_k(F) != 0 and J_k^{(m)}(F) != 0 for each m. Let
>
>   M_k = \sup_{F \in S_k} \frac{ \sum_{m=1}^k J_k^{(m)}(F) }{ I_k(F) },
>   r_k = \lceil \frac{ \theta M_k }{ 2 } \rceil.
>
> Then there are infinitely many integers n such that at least r_k of the
> n + h_i (1 <= i <= k) are prime. In particular,
> lim inf_n ( p_{n + r_k - 1} - p_n ) <= \max_{1 <= i,j <= k} (h_i - h_j)."

Proof mechanism (p.6): S = S_2 - \rho S_1 with \rho = \theta M_k / 2 -
\epsilon; floor(\rho + 1) = ceil(\theta M_k / 2) for \epsilon suitably
small.

### Proposition 4.3 (p.6, verbatim) -- the M_k lower bounds

> "Proposition 4.3. Let k \in N, and M_k be as given by Proposition 4.2.
> Then
>   (1) We have M_5 > 2.
>   (2) We have M_105 > 4.
>   (3) If k is sufficiently large, we have
>       M_k > \log k - 2 \log\log k - 2."

Proofs: part (3) in Sec 7 (concluding display (7.21)); parts (1),(2) in
Sec 8 via explicit polynomial F and eigenvalue computation:
(8.15) largest eigenvalue lambda ~= 4.0020697... > 4 for k = 105 (42 x 42
rational symmetric matrices, monomials (1 - P_1)^b P_2^c with b + 2c <= 11);
(8.16)-(8.17) for k = 5, P = (7/10)(1-P_1)P_2 + (1/14)(1-P_1)^2
+ (3/14)P_2 - (1-P_1) gives M_5 >= 1417255/708216 > 2.
[TRANSCRIPTION-UNSURE: (8.15)-(8.17) values transcribed from pdftotext of
p.24, not from a visual read; the fraction printed as "1 417 255 / 708 216".]

### How the theorems follow (Sec 4, p.6-7)

- Thm 1.3: k = 105, M_105 > 4 (Prop 4.3(2)), Bombieri-Vinogradov gives
  theta = 1/2 - epsilon, so theta*M_105/2 > 1; Prop 4.2 gives
  lim inf(p_{n+1} - p_n) <= diam(H); Engelsma's admissible 105-tuple with
  0 = h_1 < ... < h_105 = 600 (explicit set in footnote 2, p.6, credited
  to the website math.mit.edu/~primegaps maintained by Andrew Sutherland;
  full 105-element list printed in footnote, not copied here).
- Thm 1.4: theta = 1 - epsilon (Elliott-Halberstam); k = 105 gives
  theta*M_105/2 > 2, hence lim inf(p_{n+2} - p_n) <= 600; k = 5,
  H = {0, 2, 6, 8, 12}, M_5 > 2 gives lim inf(p_{n+1} - p_n) <= 12.
- Thm 1.1: see Section 3 of this extraction (large-k passage).
- Thm 1.2: counting argument on p.7 (see Section 4 of this extraction).

---

## 3. Uniformity in k (task point 2)

### 3a. Global convention: k is FIXED. Sec 3 Notation (p.4, verbatim)

> "We shall view k as a fixed integer, and H = {h_1, ..., h_k} as a fixed
> admissible set. In particular, any constants implied by the asymptotic
> notation o, O or \ll may depend on k and H. We will let N denote a large
> integer, and all asymptotic notation should be interpreted as referring
> to the limit N -> \infty."

CONSEQUENCE (extraction-level, direct reading): NO statement in this paper
allows the tuple size k to grow with x (= N). Every theorem and
proposition is asymptotic in N with k and H held fixed. There is no
explicit k-uniform version anywhere, including the final sections
(Secs 7-8 prove lower bounds on the functional M_k only; Sec 9 is
acknowledgements). Searched the full text for uniformity language;
the only hit is 3b below.

### 3b. The only "independent of k" passage: Sec 4, p.7 (verbatim)

> "Finally, we consider the case when k is large. For the rest of this
> section, any constants implied by asymptotic notation will be independent
> of k. By the Bombieri-Vinogradov theorem, we can take
> theta = 1/2 - epsilon. Thus, by Proposition 4.3, we have for k
> sufficiently large
>
> (4.5)  \frac{\theta M_k}{2} >= ( \frac{1}{4} - \frac{\epsilon}{2} )
>          ( \log k - 2 \log\log k - 2 ).
>
> We choose epsilon = 1/k, and see that \theta M_k / 2 > m if
> k >= C m^2 e^{4m} for some absolute constant C (independent of m and k).
> Thus, for any admissible set H = {h_1, ..., h_k} with k >= C m^2 e^{4m},
> at least m + 1 of the n + h_i must be prime for infinitely many
> integers n."

Continuation (p.7, verbatim): "We can choose our set H to be the set
{p_{\pi(k)+1}, ..., p_{\pi(k)+k}} of the first k primes which are greater
than k. This is admissible, since no element is a multiple of a prime less
than k (and there are k elements, so it cannot cover all residue classes
modulo any prime greater than k.) This set has diameter
p_{\pi(k)+k} - p_{\pi(k)+1} \ll k \log k. Thus
lim inf_n (p_{n+m} - p_n) \ll k \log k \ll m^3 e^{4m} if we take
k = \lceil C m^2 e^{4m} \rceil. This gives Theorem 1.1."

READING: this is uniformity of the CONSTANTS in k and m (so k may be
chosen as a function of m), NOT uniformity of k in x. For each m, the
value k = ceil(C m^2 e^{4m}) is fixed before N -> infinity. Note also
epsilon = 1/k, i.e. the level-of-distribution exponent slack depends on k,
which is legitimate only because k is fixed as N -> infinity.

### 3c. Where growth-rate information about k lives

- Prop 4.3(3): M_k > \log k - 2 \log\log k - 2 for k sufficiently large
  (proved Sec 7, display (7.21); choice A = log k - 2 log log k inside the
  proof). This is a statement about the functional M_k, uniform over all
  large k, with no reference to x.
- Sec 7 Remark after (7.2) (p.18, verbatim, limitation statement):
  "We expect that if F maximizes the ratio \sum_{m=1}^k J_k^{(m)}(F)/I_k(F),
  then F is an eigenfunction for L_k, and the corresponding eigenvalue is
  the value of ratio at F. Unfortunately the author has not been able to
  solve the eigenvalue equation for L_k when k > 2."
  [TRANSCRIPTION-UNSURE: "the value of ratio at F" is as printed
  (apparently missing "the" before "ratio").]
- [BACKGROUND-UNVERIFIED] Explicitly k-uniform-in-x versions of this
  machinery (k up to a small power of log x) appear only in later work
  (e.g. Maynard, "Dense clusters of primes in subsets", arXiv:1405.2593),
  not in this paper. A consumer needing k growing with x cannot cite
  1311.4600 for that and must go to the later literature.

---

## 4. What to cite for clusters of several primes in admissible tuples
   (task point 3)

- Cluster inside an arbitrary admissible tuple, quantitative: cite
  Proposition 4.2 (with M_k from Proposition 4.3). Statement: for primes
  of level of distribution theta and ANY admissible H = {h_1,...,h_k},
  infinitely many n have at least r_k = ceil(theta M_k / 2) primes among
  n + h_1, ..., n + h_k. With Bombieri-Vinogradov (theta = 1/2 - epsilon)
  and Prop 4.3(3): at least m+1 primes in every admissible k-tuple once
  k >= C m^2 e^{4m} (Sec 4, eq. (4.5) and following text, p.7).
- Headline consequence (m primes in a bounded interval, i.e. bounded
  p_{n+m} - p_n): cite Theorem 1.1.
- Bounded gaps unconditionally: Theorem 1.3 (<= 600); under
  Elliott-Halberstam: Theorem 1.4 (<= 12 for consecutive; <= 600 for
  p_{n+2} - p_n).
- Positive proportion of admissible m-tuples realizing the m-tuples
  conjecture: cite Theorem 1.2 (proof: counting argument, Sec 4, p.7,
  using k = ceil(C m^2 e^{4m}) and the sieve of A down to A_2 with
  #A_2 >= r \prod_{p <= k} (1 - 1/p) \gg_m r).
- Primes in subsequences / linear forms: no numbered theorem; only the
  prose remark on p.2 ("(1/4 + o_{k->\infty}(1)) log k of the L_i(n) are
  prime") -- a consumer should NOT cite this as a formal result of this
  paper; it is announced capability, proved elsewhere.
  [BACKGROUND-UNVERIFIED: the worked-out version is usually cited from
  Maynard 1405.2593.]

---

## COMMENTARY (extractor's observations -- NOT paper content)

INTERFACE CARD: Maynard 1311.4600v3 (max 15 lines)
1. Engine: Prop 4.1 (sieve asymptotics for S_1, S_2) + Prop 4.2
   (clusters: r_k = ceil(theta*M_k/2) primes in ANY admissible k-tuple)
   + Prop 4.3 (M_5 > 2, M_105 > 4, M_k > log k - 2 log log k - 2).
2. Headlines: Thm 1.1 (liminf p_{n+m}-p_n << m^3 e^{4m}); Thm 1.3 (600);
   Thm 1.4 (12 and 600 under EH); Thm 1.2 (positive proportion of
   admissible m-tuples).
3. Uniformity: k is FIXED relative to x throughout (Sec 3, verbatim).
   Only k-uniformity present: constants independent of k/m in Sec 4
   large-k passage (eq. 4.5), letting k = ceil(C m^2 e^{4m}) as a
   function of m only. No k -> infinity with x version exists here.
4. For erdos251 consumers: this paper gives clusters of m+1 primes in a
   window of diameter << m^2 e^{4m} log(m^2 e^{4m}) around infinitely
   many n -- but with NO control on the density/location of such n in
   [x, 2x], and no k growing with x. Quantitative frequency or
   short-interval localization must come from later k-uniform work.
