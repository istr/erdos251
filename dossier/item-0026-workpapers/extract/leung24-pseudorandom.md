# EXTRACTION: Sun-Kai Leung, "Pseudorandomness of primes at large scales"

Source (only evidence base): /home/istr/pro/erdos251/dossier/2407.05380v2.pdf
sha256 019b27fdd1506ed0c796bdf49c68d138fbf099ef2dd6223868667d8306d7e890
(operator-verified; re-verified in session).
arXiv:2407.05380v2 [math.NT] 23 Nov 2024. 13 pages (PDF page = printed
page). Author: Sun-Kai Leung. Affiliation (p. 13): Departement de
mathematiques et de statistique, Universite de Montreal, CP 6128 succ.
Centre-Ville, Montreal, QC H3C 3J7, Canada; e-mail
sun.kai.leung@umontreal.ca. 2020 MSC: 11N05; 60G55 (footnote, p. 1). No
journal reference printed on the paper (preprint). No grant/funding
footnote; only an Acknowledgements paragraph (p. 12, quoted below).
Producer: pdfTeX-1.40.25; created 26 Nov 2024.

Front-matter identity vs steering identification: MATCHES. Steering said
"Leung, Pseudorandomness of primes at large scales"; the title line
(p. 1) reads "PSEUDORANDOMNESS OF PRIMES AT LARGE SCALES", author
"SUN-KAI LEUNG".

---

## Transcription conventions and symbol table

ASCII only. Diacritics transliterated (Cramer, Teravainen, Tafula,
Erdos, de la Breteche where they occur). Mathematics in LaTeX-like
ASCII. Anchors are the paper's own numbering (Definition/Conjecture/
Theorem/Corollary/Proposition/Lemma/equation/section); page numbers are
a secondary aid. Displays that the pdftotext layer scrambles were
transcribed from 200 dpi page renders (see FLAGS); each hard display
records its source layer.

Symbol table (every non-obvious glyph):

- `frakS(calH;q)` -- the Gothic/Fraktur singular series \mathfrak{S} of
  the set calH relative to modulus q; `frakS(calH)` -- the classical
  (q = 1 flavour) singular series. The paper uses the same Fraktur S for
  both, distinguished by the ";q" argument.
- `calH` -- the script set H = {h_i} of shifts (Conjecture 1.1); also
  the multiple-lattice shift set in Proposition 3.1 and Lemma 3.1.
- `calI = {I_i}_{i=1}^r`, `calJ`-family `{J_i}_{i=1}^r` -- the finite
  collection of disjoint intervals in (0, infinity).
- `phi(q)` -- Euler totient.
- `v_p(calH) := #{h in calH (mod p)}` -- number of residue classes mod p
  occupied by calH (the paper's nu-analogue).
- `1_P` -- the prime indicator function.
- `xi`, `xi_n` -- point processes; `delta_{X_n}` the Dirac point mass at
  X_n; `xi(A)` the number of points of xi in A.
- `p_i` -- "the i-th least prime after n" (Corollary 2.1); `p_i(q,a)` --
  "the i-th least prime which is congruent to a (mod q)" (Corollary 2.2).
  These are CONSECUTIVE primes indexed from n (resp. from 0 in the class
  a mod q).
- `Stir(k,j)` -- Stirling number of the second kind, printed as the
  curly-brace binomial-like symbol { k \atop j } = "the number of ways to
  partition a set of k objects into j non-empty subsets" (p. 3).
- `diam(calI) := sup(union_i I_i) - inf(union_i I_i)` -- diameter of the
  interval collection (p. 3).
- `xtil := x/(phi(q) log q)` -- the tilde normalisation of Section 4
  (printed x-with-tilde).
- `HL[q]`, `HL[1]` -- the q-variant (resp. classical q = 1) of the
  Hardy-Littlewood prime k-tuple conjecture (Conjecture 1.1).
- `l_1,...,l_r` -- lattice ranks in Proposition 3.1; `|l| := l_1+...+l_r`.
- `|k| := k_1+...+k_r`; `k = (k_1,...,k_r)`.
- `-->d` convergence in distribution; `-->vd` vague convergence of random
  measures. `Poisson(lambda)` a Poisson random variable of mean lambda.
- `Sigma_1, Sigma_2, Sigma_{1,1}, Sigma_{1,2}` -- the proof sums of
  Section 4; `Sigma*_{a (mod q)}` sum over reduced residues a mod q.
- `mu^2(d)` -- squarefree indicator; `w(d) := #{p : p | d}`.
- `<<`, `<<_k` -- Vinogradov, with subscripted dependence of the implied
  constant; `o_{...}(1)` little-o with subscripted parameter dependence.

Everything up to the COMMENTARY section is EXTRACTION (what the paper
says). Nothing evaluative appears before COMMENTARY.

---

## 1. FRONT MATTER and ABSTRACT

Title (p. 1): "Pseudorandomness of primes at large scales".
Author (p. 1): "Sun-Kai Leung".

Abstract (p. 1), verbatim:

> "Abstract. Assuming a q-variant of the prime k-tuple conjecture
> uniformly, we compute mixed moments of the number of primes in disjoint
> short intervals and progressions, respectively. This involves
> estimating the mean of singular series along products of lattices,
> which is of independent interest. As a consequence, we establish the
> convergence of both sequences of suitably normalized primes to a
> standard Poisson point process."

Opening framing (Section 1, p. 1), verbatim (the parity local
obstruction is stated here):

> "One of the biggest challenges is that, despite being a deterministic
> sequence of natural numbers, primes exhibit highly pseudorandom
> behavior, apart from some obvious "local obstructions" (see [Tao08, p.
> 194]), such as the absence of consecutive primes other than the pair
> {2, 3} due to parity. Therefore, natural questions arise: to what
> extent are primes pseudorandom at appropriate larger scales? Can such
> pseudorandomness be rigorously justified?"

---

## 2. SECTION 1 (Introduction): definitions and the assumed conjecture

Definition 1.1 (Standard Poisson point process) (p. 1), verbatim:

> "Definition 1.1 (Standard Poisson point process). A point process
> xi = sum_{n=1}^{infinity} delta_{X_n} (or {X_n}_{n=1}^{infinity} by
> abuse of notation) on (0, infinity) is called a standard Poisson point
> process if for any integer r >= 1 and collection of disjoint intervals
> {I_i}_{i=1}^r in (0, infinity), we have
>   P( xi(I_i) = k_i, 1 <= i <= r )
>       = prod_{i=1}^r e^{-|I_i|} |I_i|^{k_i} / k_i! ,
> where xi(A) := #{n >= 1 : X_n in A} is the number of points in the
> subset A subset-of (0, infinity)."

Definition 1.2 (Convergence in distribution) (p. 2), verbatim
[resolved-by-image, p. 2]:

> "Definition 1.2 (Convergence in distribution). Let xi, xi_1, xi_2, ...
> be point processes on (0, infinity). Then we say xi_n converges to xi
> in distribution as n -> infinity if xi_n -->vd xi as random measures.
> Equivalently, for any integer r >= 1 and any collection of disjoint
> xi-continuity intervals {I_i}_{i=1}^r in (0, infinity), we have the
> convergence in distribution
>   (xi_n(I_1), ..., xi_n(I_r)) -->d (xi(I_1), ..., xi(I_r))
> as n -> infinity."

Conjecture 1.1 -- THE ASSUMED HARDY-LITTLEWOOD VARIANT (p. 2), verbatim
and complete, with full quantifier order [resolved-by-image, p. 2]:

> "Conjecture 1.1 (q-variant of Hardy-Littlewood prime k-tuple conjecture
> (HL[q])). Given integers k, q, H >= 1, let N >> phi(q) log q be an
> integer and calH subset-of [0, H] be a set consisting of k distinct
> multiples of q which is admissible, i.e., v_p(calH) := #{h in calH
> (mod p)} < p for any prime p. Then as N -> infinity, we have
>   sum_{1<=n<=N, (n,q)=1} prod_{h in calH} 1_P(n + h)
>     = (1 + o_{k,calH}(1)) frakS(calH; q)
>          sum_{1<=n<=N, (n,q)=1} ( prod_{h in calH} log(n + h) )^{-1} ,
> where 1_P is the prime indicator function, and frakS(calH; q) is the
> singular series defined as the Euler product
>   (phi(q)/q)^{-k} prod_{p !| q} (1 - 1/p)^{-k} (1 - v_p(calH)/p) ."

Immediately after (p. 2), verbatim:

> "Note that frakS(calH; q) = (phi(q)/q)^{-1} frakS(calH), where
>   frakS(calH) := prod_p (1 - 1/p)^{-k} (1 - v_p(calH)/p)
> is the classical singular series."

[Extractor note, non-evaluative: HL[1] is the q = 1 case of Conjecture
1.1 and is the hypothesis of Theorem 2.1 / Corollary 2.1; HL[q] is the
hypothesis of Theorem 2.2 / Corollary 2.2. The uniformity demanded is in
H over a stated finite range (see Theorems below), NOT in k or in the
number of intervals.]

Prior results recalled (p. 2), verbatim (Gallagher's Poisson law for
interval prime counts):

> "Assuming HL[1] with sufficient uniformity, Gallagher [Gal76] showed
> that the prime count in short intervals has a Poissonian limiting
> distribution. More precisely, if lambda > 0, then for any integer
> k >= 0, we have
>   lim_{N->infinity} (1/N) #{N < n <= 2N : pi(n+H) - pi(n) = k}
>       = e^{-lambda} lambda^k / k! ,
> where H = lambda log N, i.e., we have the convergence in distribution to
> a Poissonian random variable with parameter lambda
>   pi(n + H) - pi(n) -->d Poisson(lambda)."

And (p. 2, into p. 3), verbatim (the author's own prior progression
result, and the Montgomery-Soundararajan Gaussian regime):

> "For longer intervals, assuming HL[1] with a power-saving error term,
> Montgomery and Soundararajan [MS04] showed that the prime count in
> short intervals has a Gaussian limiting distribution ... Inspired by
> their work, assuming HL[q] with a power-saving error term, the author
> [Leu24] recently computed moments of the number of primes not exceeding
> N in progressions to a common large modulus q as a (mod q) varies.
> Consequently, depending on the size of phi(q) with respect to N, the
> prime count exhibits a Gaussian or Poissonian law. In particular, if
> lambda > 0, then for any integer k >= 0, we have
>   lim_{N->infinity} (1/phi(q)) |{a (mod q) : pi(N; q, a) = k}|
>       = e^{-lambda} lambda^k / k! ,
> where N = lambda phi(q) log q ..."

Notation paragraph (p. 3), verbatim:

> "Notation. Throughout the paper, we use the standard big O, little o
> notations, and the Vinogradov notation <<, where the implied constants
> depend only on the subscripted parameters. We denote sum*_{a (mod q)}
> as the sum over reduced residues modulo q. We also write sum_{x_i} for
> sum_{x_1,...,x_r} to simplify notation, unless otherwise specified."

---

## 3. SECTION 2 (Main results): the mixed-moment theorems

Preamble (p. 3), verbatim (defines diam and the Stirling number):

> "Analogous to [Gal76], [MS04] and [Leu24], to establish the convergence
> in distribution of point processes, we compute mixed moments of the
> number of primes in short intervals and short progressions
> respectively. To state our main results, let us denote
> diam(calI) := sup union_{1<=i<=r} I_i - inf union_{1<=i<=r} I_i as the
> diameter of the collection of disjoint intervals calI = {I_i}_{i=1}^r
> in (0, infinity), and Stir(k, j) as the Stirling number of the second
> kind, i.e., the number of ways to partition a set of k objects into j
> non-empty subsets."

Theorem 2.1 -- MIXED MOMENTS FOR SHORT INTERVALS (p. 3), verbatim and
complete, with full quantifier order [resolved-by-image, p. 3]:

> "Theorem 2.1. Given an integer r >= 1, let calI = {I_i}_{i=1}^r be a
> collection of disjoint intervals in (0, infinity). Suppose HL[1] holds
> for 1 <= H <= diam(calI) uniformly. Then for all integers k_1, ..., k_r
> >= 0, we have
>   lim_{N->infinity} (1/N) sum_{N<n<=2N} prod_{i=1}^r
>       ( #{ p > n : (p - n)/log N in I_i } )^{k_i}
>     = prod_{i=1}^r ( sum_{j_i=1}^{k_i} Stir(k_i, j_i) |I_i|^{j_i} ) ."

Theorem 2.2 -- MIXED MOMENTS FOR SHORT PROGRESSIONS (p. 3), verbatim and
complete [resolved-by-image, p. 3]:

> "Theorem 2.2. Given an integer r >= 1, let calI = {I_i}_{i=1}^r be a
> collection of disjoint intervals in (0, infinity). Suppose HL[q] holds
> for 1 <= H <= diam(calI) phi(q) log q uniformly. Then for all integers
> k_1, ..., k_r >= 0, we have
>   lim_{q->infinity} (1/phi(q)) sum*_{a (mod q)} prod_{i=1}^r
>       ( #{ p == a (mod q) : p/(phi(q) log q) in I_i } )^{k_i}
>     = prod_{i=1}^r ( sum_{j_i=1}^{k_i} Stir(k_i, j_i) |I_i|^{j_i} ) ."

Remark 2.1 (p. 3), verbatim:

> "Remark 2.1. It is, in fact, easier and considered more natural to
> compute factorial moments rather than ordinary moments in this context.
> However, we opt for the latter to ensure compatibility with the
> existing literature."

Transition (p. 3), verbatim:

> "Applying the method of moments, by Definitions 1.1 and 1.2, the
> convergence of both sequences of suitably normalized primes in short
> intervals and short progressions to a standard Poisson point process is
> an immediate consequence."

Corollary 2.1 -- POISSON POINT PROCESS, SHORT INTERVALS (p. 3-4),
verbatim [resolved-by-image, pp. 3-4]:

> "Corollary 2.1. Given an integer r >= 1, let calI = {I_i}_{i=1}^r be a
> collection of disjoint intervals in (0, infinity). Suppose HL[1] holds
> for 1 <= H <= diam(calI) uniformly. Then for all integers k_1, ..., k_r
> >= 0, we have
>   lim_{N->infinity} (1/N) #{ N < n <= 2N :
>       #{ p > n : (p - n)/log N in I_i } = k_i, 1 <= i <= r }
>     = prod_{i=1}^r e^{-|I_i|} |I_i|^{k_i} / k_i! ,
> i.e., the point process { (p_i(n) - n)/log N }_{i=1}^{infinity}, for
> N < n <= 2N chosen uniformly at random, converges in distribution to
> the standard Poisson point process as N -> infinity, where p_i denotes
> the i-th least prime after n. In particular, by taking r = 1 and
> I_1 = (0, lambda], we recover [Gal76, Theorem 1]."

Corollary 2.2 -- POISSON POINT PROCESS, SHORT PROGRESSIONS (p. 4),
verbatim [resolved-by-image, p. 4]:

> "Corollary 2.2. Given an integer r >= 1, let calI = {I_i}_{i=1}^r be a
> collection of disjoint intervals in (0, infinity). Suppose HL[q] holds
> for 1 <= H <= diam(calI) phi(q) log q uniformly. Then for all integers
> k_1, ..., k_r >= 0, we have
>   lim_{q->infinity} (1/phi(q)) #{ a (mod q) :
>       #{ p == a (mod q) : p/(phi(q) log q) in I_i } = k_i, 1 <= i <= r }
>     = prod_{i=1}^r e^{-|I_i|} |I_i|^{k_i} / k_i! ,
> i.e., the point process { p_i(q,a)/(phi(q) log q) }_{i=1}^{infinity},
> for a (mod q) chosen uniformly at random, converges in distribution to
> the standard Poisson point process as q -> infinity, where p_i(q, a)
> denotes the i-th least prime which is congruent to a (mod q). In
> particular, by taking r = 1 and I_1 = (0, lambda], we recover [Leu24,
> Corollary 1.2]."

Remarks 2.2 and 2.3 (pp. 4) paraphrase (NOT quoted in full): both are
"frequency side" analogues on the GUE / sine-kernel side -- Remark 2.2
recalls the conjecture that { (log T / 2pi)(gamma_n - t) } converges to
the sine-kernel process (zeta zeros); Remark 2.3 the Dirichlet
L-function analogue. Neither adds a proved statement.

Structure remark (p. 4), verbatim:

> "The proofs of Theorems 2.1 and 2.2 share the same structure, although
> the latter is more technical due to additional changes of variables. To
> avoid repetition, this paper includes only the proof of Theorem 2.2."

---

## 4. SECTION 3 (Estimates of singular series): the UNCONDITIONAL core

Framing (p. 4), verbatim (the word "unconditional" is the author's):

> "As observed in [Gal76], while primes exhibit "local" correlations,
> leading to those singular series defined in Conjecture 1.1, such
> correlations diminish "globally" as the classical singular series is 1
> on average over hypercubes. Similarly, the following (unconditional)
> proposition, which is a "multidimensional" version of [Leu24, Lemma
> 6.1] but without an explicit error term, lies at the crux of the mixed
> moment computation."

Proposition 3.1 -- SINGULAR-SERIES MEAN ALONG A PRODUCT OF LATTICES
(p. 4), verbatim and complete, with full quantifier order
[resolved-by-image, p. 4]:

> "Proposition 3.1. Given integers q, r >= 1, let {J_i}_{i=1}^r be a
> collection of disjoint intervals in (0, infinity) with
> min_{1<=i<=r} |J_i|/q -> infinity as min_{1<=i<=r} |J_i| -> infinity.
> Then for any (b, q) = 1 and l_1, ..., l_r >= 1, we have
>   sum ... sum_{ h_1^{(i)},...,h_{l_i}^{(i)} in J_i distinct,
>                 h_1^{(i)} == ... == h_{l_i}^{(i)} == b (mod q) }
>       frakS(calH; q)
>     = (1 + o_{l_1,...,l_r}(1)) prod_{i=1}^r ( |J_i|/phi(q) )^{l_i}
> as min_{1<=i<=r} |J_i| -> infinity, where
> calH = { h_1^{(i)}, ..., h_{l_i}^{(i)} }_{i=1}^r, i.e., the singular
> series frakS(calH; q) is, on average, (phi(q)/q)^{-(l_1+...+l_r)} along
> a product of lattices of ranks l_1, ..., l_r."

Lemma 3.1 -- UNCONDITIONAL UPPER BOUND ON AN INDIVIDUAL SINGULAR SERIES
(p. 7), verbatim [resolved-by-image, p. 7]:

> "Lemma 3.1. Given integers k, q >= 1, let H >= 2q be an integer and
> calH subset-of [0, H] be a set consisting of k distinct multiples of q.
> Then
>   frakS(calH) <<_k ( log(H/q) )^{k-1} ."

Method anatomy of Section 3 (PARAPHRASE except quotes; from the text
layer and the p. 5 render):

- Proposition 3.1 proof follows Gallagher [Gal76] (simplification
  [For16]). One writes (1 - 1/p)^{-k}(1 - v_p(calH)/p) =: 1 + a(p,
  v_p(calH)), a(d;calH) := prod_{p|d} a(p, v_p(calH)), giving the
  absolutely convergent expansion frakS(calH;q) = sum_{d, (d,q)=1}
  mu^2(d) a(d; calH). Summing over the lattice points and truncating at
  D = min_i (|J_i|/q)^{1/2} (eq. (3.1)-(3.4)); the p-th "local factor"
  A(p) vanishes for d > 1 by two Gallagher binomial identities (p. 8 of
  [Gal76]), so A(d) = 1 iff d = 1. The main term prod_i (|J_i|/(phi(q)))
  ^{l_i} survives. The tail bound is (p. 5), verbatim:

  > "sum_{d>D, (d,q)=1} mu^2(d) S'(d) <<_{l,eps} (D|J|)^eps |J| / (q^r D),"

  with J := prod_{i=1}^r J_i. The whole error is o_{l_1,...,l_r}(1); NO
  explicit power saving is retained (contrast [Leu24, Lemma 6.1], which
  had one).
- Lemma 3.1 proof: split the Euler product at p = H/q; for p > H/q with
  p !| q one has v_p(calH) = k (distinct multiples of q), so that tail is
  1 + O_k( (H/q log(H/q))^{-1} ); the p <= H/q part is <<_k
  log^{k-1}(H/q) by Mertens.

---

## 5. SECTION 4 (Proof of Theorem 2.2) and SECTION 5 (Statistics)

Section 4 (pp. 6-11) proves Theorem 2.2 only. PARAPHRASE except quotes.
The normalisation convention (p. 6), verbatim:

> "To lighten the notation, we adopt the convention xtil := x/(phi(q) log
> q). Without loss of generality, we assume I_i = (alpha_i, beta_i] with
> 0 < alpha_1 < beta_1 < ... < alpha_r < beta_r and k_i >= 1 for
> i = 1, ..., r."

Anatomy (PARAPHRASE): the k_i-th ordinary moment is expanded into
factorial moments via Stirling numbers (Stir(k_i, j_i) j_i!), then
opened as ordered j_i-tuples of primes in class a mod q inside I_i. Two
changes of variables (n_i = n + h_i; primes p = n + d) reduce the sum to
a prime-tuple count over admissible shift-sets, which splits as
Sigma_1 + Sigma_2 by whether the effective interval Ialpha,beta;d,h
exceeds qtil. Sigma_2 (short effective interval) is bounded by a Selberg
sieve upper bound plus Lemma 3.1 and shown negligible; Sigma_1 splits
into Sigma_{1,1} (admissible shift-set) and Sigma_{1,2} (non-admissible,
bounded trivially by |k| and negligible). On Sigma_{1,1} the assumed
HL[q] (uniformly for the stated finite shift range) replaces the
prime-tuple count by (1 + o_{k,alpha,beta}(1)) frakS(.;q) times the
reciprocal-log weight; Proposition 3.1 then evaluates the singular-series
average, yielding the product of Stirling moments. The Selberg-sieve
input is cited as (p. 9):

> "by a simple application of the Selberg sieve (see [IK04, Theorem 6.7]
> for instance)"

The HL[q] application is stated (p. 10), verbatim (note the finite,
config-fixed shift range in which uniformity is invoked):

> "Finally, suppose {h_i + d_1^{(i)}, ..., h_i + d_{j_i}^{(i)}}_{i=1}^r is
> admissible. Then assuming HL[q] uniformly for 0 <= h_i + d_1^{(i)}, ...,
> h_i + d_{k_i}^{(i)} <= (beta_r - alpha_1) phi(q) log q, we have ..."

Section 5 "Some statistics" (pp. 11-12): two numerical illustrations
(Figures 1, 2) with N = 100000 (short intervals) and q = 100000 (short
progressions), plotting the first few normalized primes for four sample
n (resp. a) taken from digits of pi. No new theorem.

Acknowledgements (p. 12), verbatim:

> "The author is grateful to Andrew Granville for his advice and
> encouragement. He would also like to thank Tony Haddad and Brad Rodgers
> for helpful discussions, Cihan Sabuncu and Christian Tafula for their
> careful proofreading, as well as the anonymous referee for valuable
> comments and corrections."

Key references (p. 12-13): [Gal76] Gallagher, On the distribution of
primes in short intervals, Mathematika 23.1 (1976) 4-9; [MS04]
Montgomery-Soundararajan, Primes in short intervals, Comm. Math. Phys.
252 (2004) 589-617; [Leu24] S.-K. Leung, Moments of primes in
progressions to a large modulus, 2024, arXiv:2402.07941; [For16] K.
Ford, Simple proof of Gallagher's singular series sum estimate, 2016,
arXiv:1108.3861; [Gra95] Granville, Harald Cramer and the distribution of
prime numbers, 1995; [IK04] Iwaniec-Kowalski, Analytic number theory.

---

## 6. UNIFORMITY LEDGER (highest-value subsection)

What is FIXED, what GROWS, which thresholds depend on which, constants
absolute vs parameter-dependent. (All statements sourced to the displays
above.)

- Number of intervals r: FIXED. Every statement opens "Given an integer
  r >= 1" and then takes the single limit N -> infinity (Theorems 2.1,
  Cor 2.1) or q -> infinity (Theorems 2.2, Cor 2.2, Prop 3.1). r is a
  constant chosen BEFORE the limit; it does NOT grow with N, x, or q.
- Moment orders k_1,...,k_r (Theorems) / lattice ranks l_1,...,l_r
  (Prop 3.1): FIXED integers, chosen before the limit. "for all integers
  k_1,...,k_r >= 0" is a pointwise-in-(k_1,...,k_r) statement, one limit
  per fixed tuple; there is NO claim uniform in k_i or growing with x.
- The o(1) / implied constants are PARAMETER-DEPENDENT, never absolute:
  Conjecture 1.1 error is o_{k,calH}(1) (depends on rank k and the whole
  set calH); Theorem 2.2's internal asymptotic is o_{k,alpha,beta}(1);
  Prop 3.1 is o_{l_1,...,l_r}(1); Lemma 3.1 and the sieve bounds are
  <<_k. So all uniformity is INSIDE a fixed configuration; none survives
  letting the configuration grow.
- The uniformity that IS demanded of the hypothesis is in H only, over a
  FINITE range tied to the fixed configuration: Theorem 2.1 needs HL[1]
  "for 1 <= H <= diam(calI) uniformly"; Theorem 2.2 needs HL[q] "for
  1 <= H <= diam(calI) phi(q) log q uniformly". diam(calI) is a fixed
  constant (the interval collection is fixed), so these windows are
  Theta(log N) and Theta(phi(q) log q) respectively -- a single log
  scale, NOT (log x)(log log x).
- Window / scale of the point process: for intervals, the normalisation
  is (p - n)/log N with p in an interval of length lambda log N, i.e.
  window = lambda log N, lambda = |I| fixed; Gallagher's scale. For
  progressions, p/(phi(q) log q), window Theta(phi(q) log q).
- Conditional vs unconditional split. CONDITIONAL on HL[1]/HL[q]:
  Theorems 2.1, 2.2 and Corollaries 2.1, 2.2 (the mixed moments and the
  Poisson convergence). UNCONDITIONAL: Proposition 3.1 (singular-series
  mean along a product of lattices) and Lemma 3.1 (upper bound
  frakS(calH) <<_k (log(H/q))^{k-1}). The paper explicitly labels
  Proposition 3.1 "(unconditional)".
- Grain. The counted object is a PRIME COUNT in an interval / class,
  #{p > n : (p-n)/log N in I_i} and #{p == a (mod q) : ...}; the average
  is over the base point n (resp. residue a). The unconditional inputs
  average the SINGULAR SERIES frakS over lattice shift-sets. Neither is a
  class mass of consecutive-gap words; there is no gap-word / pattern
  bookkeeping.
- Mode of convergence: convergence in distribution of point processes =
  convergence of all finite-dimensional distributions (Definition 1.2),
  obtained by the method of moments (Remark 2.1 / transition, p. 3). The
  limit is a single-parameter limit (N or q -> infinity), NOT along a
  sparse subsequence; it is over ALL large N (resp. all large q).
- Direction: the theorems are two-sided ASYMPTOTIC EQUALITIES (moments
  converge to the exact Poisson-moment product); they are not one-sided
  upper/non-concentration bounds. The only one-sided statement is Lemma
  3.1, an upper bound on the MAGNITUDE of an individual singular series
  (not on any site-mass concentration).

---

## 7. What the paper does NOT contain

Answering the Section 4.6 mandatory NOT-FOUND probes.

"unconditional statement": FOUND (partial). The MAIN results (Theorems
2.1, 2.2; Corollaries 2.1, 2.2) are CONDITIONAL on HL[1]/HL[q]. The
unconditional content is exactly Proposition 3.1 and Lemma 3.1. Located
quote (p. 4): "the following (unconditional) proposition ... lies at the
crux of the mixed moment computation." (Proposition 3.1 is a
singular-series mean; Lemma 3.1 an upper bound frakS(calH) <<_k
(log(H/q))^{k-1}.) No unconditional statement about prime counts, Poisson
convergence, or non-concentration exists in the paper.

"growing configuration size": NOT FOUND in this text. The number of
intervals r and all moment orders/ranks (k_i, l_i) are fixed integers
quantified before the single limit; no parameter of the configuration is
permitted to grow with N, q, or x, and no uniformity in r or k_i is
claimed anywhere.

"consecutive primes": FOUND. (i) The parity local obstruction, p. 1:
"the absence of consecutive primes other than the pair {2, 3} due to
parity." (ii) The limiting point processes are built from consecutive
primes: Corollary 2.1, "where p_i denotes the i-th least prime after n";
Corollary 2.2, "where p_i(q, a) denotes the i-th least prime which is
congruent to a (mod q)." However, the paper proves nothing about the
consecutive-gap SEQUENCE beyond that these ordered primes converge, after
normalisation, to a Poisson point process (conditionally on HL).

"gap words": NOT FOUND in this text. There is no consecutive-gap word, no
gap-pattern class, and no class mass N_{P,d}; the counted quantities are
interval/class prime counts and lattice-averaged singular series, never a
pattern-conditioned count.

Additional located absences (checked against the full 13-page text, all
pages sighted):
- "upper bound" on the mixed moments or on a prime count: NOT FOUND (the
  moments are asymptotic equalities; the only upper bound is Lemma 3.1,
  on frakS magnitude).
- "sparse" / "unbounded scale sequence" / almost-all-x: NOT FOUND; all
  limits are over ALL large N or ALL large q.
- rank ~ log log x, or any k growing like (2/ln2) log log x: NOT FOUND.
- window ~ (log x)(log log x): NOT FOUND; windows are Theta(log N) and
  Theta(phi(q) log q).
- variance/second-moment error term for the counts as a separate object:
  NOT FOUND (the "moments" here ARE the object, but with no error term:
  Prop 3.1 deliberately drops the explicit error of [Leu24, Lemma 6.1]).

---

## COMMENTARY (assessment, NOT extraction)

Consuming context (quoted verbatim from the dispatch, Section 4):

```text
The project needs an unconditional averaged middle-slot non-concentration
/ upper-uniformity statement at rank k = (2/ln 2 + o(1)) lnln x, window
h = A'L ln x ~ (ln x)(lnln x), of strength enough to keep a fixed
proportion of D0-depth site mass off its modal middle on some unbounded
scale sequence per s -- a statement that fails in the even-Cramer-smooth
model.  Six axes: A1 rank; A2 window; A3 grain (class masses N_{P,d} of
consecutive-gap words, not prime counts); A4 direction (upper /
non-concentration); A5 strength (constant order suffices); A6 density
(sparse scales, no s-uniformity).  A1-A4 are not relaxed by CG; A5 and A6
are.
```

C1. What this paper unconditionally supplies. Exactly two facts, both
about the singular series (not about primes): Proposition 3.1, that the
mean of frakS(calH;q) over a product of r lattices of fixed ranks
l_1,...,l_r inside intervals J_i is (1 + o(1)) prod_i (|J_i|/phi(q))^{l_i}
as min|J_i| -> infinity; and Lemma 3.1, that an individual classical
singular series of a k-element set of multiples of q in [0,H] is <<_k
(log(H/q))^{k-1}. These are the multidimensional Gallagher average and a
crude size bound. Both hold for all large scales and carry only
config-dependent constants (o_{l_1,...,l_r}, <<_k). Everything Poissonian
in the paper -- the mixed moments (Theorems 2.1, 2.2) and the point-
process convergence (Corollaries 2.1, 2.2) -- is CONDITIONAL on HL[1] or
HL[q] holding uniformly over a finite window tied to the fixed interval
collection.

C2. Relation to the target's grain (A3) and direction (A4). The object
here is a prime COUNT in an interval or residue class, and the
unconditional inputs average the singular series over lattices. Neither
is a class mass of consecutive-gap words; there is no pattern-conditioned
count. The conclusions are two-sided asymptotic equalities (moments equal
the exact Poisson moments), the opposite shape to a one-sided
non-concentration / upper-uniformity bound. Lemma 3.1 is one-sided but
bounds the MAGNITUDE of frakS, not the concentration of any site mass
near a modal middle. So on the two axes CG does not relax, grain and
direction, this paper is off-target.

C3. Relation to rank (A1) and window (A2). The only "rank-like"
parameters are r (number of intervals) and the moment orders k_i / lattice
ranks l_i, and all are FIXED before the single limit; the paper makes no
statement uniform in them, let alone one with a rank growing like
(2/ln2) log log x. This is the whole answer to the focus question: the
number of intervals is FIXED, not growing with x. The windows are
Theta(log N) (Gallagher's lambda log N) and Theta(phi(q) log q), a single
log, not the (log x)(log log x) window the project needs.

C4. Where it does over-deliver -- the two soft axes. On density (A6) the
unconditional Proposition 3.1 holds for ALL large scales, strictly
stronger than the sparse/unbounded-scale existence the target would
accept. On strength (A5) it delivers an exact asymptotic (1 + o(1)),
stronger than the constant-order strength the target would accept. So the
axes that CG relaxes are precisely the ones this paper clears; the binding
failures are the hard axes A1-A4. That is the same verdict pattern the
consuming context anticipates ("A1-A4 are not relaxed by CG; A5 and A6
are"): this work sits entirely on the relaxed side and misses the
unrelaxed side.

C5. Usable fragment, if any. The only piece a middle-slot construction
could touch is Proposition 3.1's exact lattice-average of the singular
series: it certifies, unconditionally and on all large scales, that
matched interval families have the SAME first-order singular-series mean
regardless of the shift-set, with no error obstruction. But it is a mean
(first moment) over lattices at FIXED rank; it says nothing about the
distribution of frakS across shift-sets, nothing about gap words, and
nothing about primes without HL. It cannot by itself keep D0-depth site
mass off its modal middle. "non-concentration": NOT FOUND in this text.

Per-axis verdict (exactly one tag each):

- A1 rank (k ~ (2/ln2) lnln x): FAILS. r and k_i/l_i are fixed integers
  quantified before the limit; nothing grows with x, no log-log-scale
  rank appears.
- A2 window (h ~ (ln x)(lnln x)): FAILS. Windows are Theta(log N) and
  Theta(phi(q) log q); a single log, diam(calI) fixed.
- A3 grain (class masses of consecutive-gap words): FAILS. Grain is
  interval/class prime counts and lattice-averaged singular series, not
  gap-word class masses.
- A4 direction (upper / non-concentration): FAILS. Conclusions are
  two-sided moment equalities / Poisson convergence; the sole one-sided
  bound (Lemma 3.1) bounds singular-series magnitude, not site
  concentration.
- A5 strength (constant order suffices): CLEARS (vacuously). The
  unconditional content is an exact asymptotic (Prop 3.1), stronger than
  constant order -- but on the wrong object, so this clearance does not
  advance the carrier.
- A6 density (sparse scales, no s-uniformity): CLEARS (vacuously). The
  unconditional Proposition 3.1 holds for all large scales, stronger than
  a sparse-scale existence -- again on the wrong object.

Does the paper clear ALL six axes? NO. It fails A1, A2, A3, A4 (the axes
CG does not relax); it is not a located unconditional carrier.

Even-Cramer-smooth deterministic gap system (q_1=2, q_2=3, q_3=5, q_4=7,
q_{n+1}=q_n+2*ceil(ln q_n / 2)): UNTESTED against it. The paper considers
no deterministic gap model at all; its Poisson results are conditional on
HL and heuristically motivated by "the modified Cramer model (see [Gra95,
pp. 23-24])" (p. 1), but it never states or tests behaviour in the
specified even-Cramer-smooth system. (Its two unconditional facts,
Proposition 3.1 and Lemma 3.1, are arithmetic statements about the true
singular series and are model-independent; they neither invoke nor
contradict the deterministic system.) This is a genuine "untested", not a
guess.

---

## FLAGS (consolidated)

1. [TRANSCRIPTION-UNSURE, resolved-by-image] All theorem/corollary/
   proposition/conjecture displays with Stirling numbers, product-of-sum
   structure, or stacked subscripts (Conjecture 1.1, Theorems 2.1 & 2.2,
   Corollaries 2.1 & 2.2, Proposition 3.1, Lemma 3.1, and the tail bound
   (3.2)) were transcribed from 200/150 dpi renders of pp. 2, 3, 4, 5, 7;
   the pdftotext -layout layer scrambles the Stirling-brace symbol and the
   multi-line summation conditions. The text layer was used to
   cross-check every one and agreed on content.

2. [PROCESS-NOTE / verification] A first 200 dpi render of PDF page 3
   ("pg-03.png") displayed foreign content (an "Assume RH ... M_n(X,
   delta; eta, Phi)" theorem, i.e. not this paper). Cross-checking against
   pdftotext -f 3 -l 3 (which correctly returned this paper's Theorems
   2.1/2.2) exposed the render as a stale/corrupt image; a fresh render at
   150 dpi returned the correct Leung page 3. The verbatim page-3 displays
   above are taken from the CORRECT fresh render, confirmed against the
   text layer. No content from any other PDF entered this extract. Flagged
   because it is exactly the kind of silent cross-file contamination the
   session discipline forbids.

3. [PRINTED-ODDITY] The Stirling number of the second kind is printed in
   the curly-brace notation { k \atop j } (not S(k,j)); rendered here as
   Stir(k, j) with the paper's own gloss "the number of ways to partition
   a set of k objects into j non-empty subsets" (p. 3).

4. [PRINTED-ODDITY] The singular series uses the Fraktur \mathfrak{S} for
   BOTH frakS(calH; q) and frakS(calH); the two are distinguished only by
   the presence/absence of the ";q" argument (p. 2). No separate glyph.

5. [TRANSCRIPTION-UNSURE, resolved-by-context] In Conjecture 1.1 the
   error subscript reads o_{k,H}(1) where "H" is the script set calH (the
   k-element shift-set), not the integer window H of the same clause;
   transcribed as o_{k,calH}(1). The reading is forced by the sentence
   (the error can only depend on the tuple, and H the integer is the
   ambient bound).

6. The main Poisson results are CONDITIONAL on HL[1]/HL[q]; only
   Proposition 3.1 and Lemma 3.1 are unconditional. Recorded here (not an
   oddity, but load-bearing for the axis verdict) so the conditional /
   unconditional boundary is not lost.
