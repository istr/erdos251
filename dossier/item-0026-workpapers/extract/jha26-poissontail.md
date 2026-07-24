# EXTRACTION: Abhishek Jha, "The Poisson Tail Conjecture for Primes in Short Intervals"

Source (only evidence base): /home/istr/pro/erdos251/dossier/2605.23014v1.pdf
arXiv:2605.23014v1 [math.NT] 21 May 2026 (arXiv stamp on p. 1).
sha256 ccf3f21acb103235c817ea7ef8012c3554a31ad1ec3d69ba8630085f31b0b551
(operator-verified; re-verified this session).
Author: Abhishek Jha. Affiliation (address block, p. 29): Department of
Mathematics, 1409 West Green Street, University of Illinois, Urbana-
Champaign, Urbana, IL 61801, USA. Email: jha33@illinois.edu.
29 pages. No printed journal reference (arXiv preprint).
2020 Mathematics Subject Classification (p. 1): Primary 11N05, 11B83.
Grant/acknowledgment (Section 1.3, p. 7): "The author thanks his advisor,
Kevin Ford, for suggesting this problem and for many helpful discussions.
During the preparation of this work, the author was supported in part by
the National Science Foundation under grant DMS-2301264."

Printed page number = PDF page number throughout (title page is printed
p. 1 = PDF p. 1). Anchors are the paper's own numbering
(Theorem/Lemma/Proposition/Conjecture/Definition/equation/Section); page
numbers are a secondary aid.

---

## Transcription conventions

ASCII only. Diacritics transliterated: Cramer (Cramer), Erdos, de la
Breteche, Matomaki, Teravainen where they arise (none of the last three
appear in this paper). Mathematics rendered LaTeX-like in ASCII. Verbatim
passages are blockquoted with page numbers. Everything before the
COMMENTARY section is EXTRACTION (what the paper says); assessment lives
only under COMMENTARY.

### Symbol table (every non-obvious glyph)

- `calH` = the finite tuple/set the paper writes as calligraphic H, a
  finite subset of Z (the "tuple"). `|calH|` = its cardinality. `calH mod
  p` = the image of calH modulo p; `|calH mod p|` = number of residue
  classes it occupies.
- `calP` = the set of primes (calligraphic P). `calA` = the set A subset N
  (calligraphic A), the general sequence under study. `calR` = the
  Banks-Ford-Tao random set (calligraphic R). `calN` = a set of positive
  integers / the naturals (blackboard N).
- `frakS(calH)` = the singular series (Fraktur/German capital S) defined in
  (1.3). `frakS(H)=0` when |calH mod p| = p for some prime p.
- `Sz` = the randomly sifted set S_z = Z \ union_{p<=z}(a_p + pZ), with a_p
  a residue class mod p chosen uniformly at random, choices jointly
  independent. `Sz(y)` = [1,y] cap Sz; `Sz` (italic, context) = |Sz(y)|.
- `log_k x` = the k-fold iterated logarithm TRUNCATED AT ZERO: log_1 x :=
  max{0, log x}, log_k x := max{0, log(log_{k-1} x)} for k >= 2. CRITICAL:
  in THIS paper `log_2 x` means log log x (the iterated log), NOT (log x)^2.
  Thus `(log_2 x)^{-10}` = (log log x)^{-10}, and `log_3 x` = log log log x,
  `log_4 x` = log log log log x. This convention is stated on p. 4
  (transcribed below).
- `lambda` = the scaling parameter; window length is lambda*log x.
  `lambda'` and `lambda''` are the thresholds defined in (1.13).
- `MA(x;y)` = M_{calA}(x;y), the count (1.10) of n<=x in calA with the next
  y integers empty of calA (a "gap exceeding y" counter, index restricted
  to calA).
- `NA(x;y,k)` = N_{calA}(x;y,k), the count (1.11) of ALL n<=x with exactly
  k elements of calA in [n+1,n+y] (interval-content counter, unrestricted).
- `S(x,y,z)` = #{x<n<=x+y : n has no prime factor <= z}, the interval sieve
  function. `S^-(y,z) = min_x S(x,y,z) = min_{(a_p)} |(0,y] cap Sz|`.
- `f, F` = the lower/upper linear (Jurkat-Richert) sieve functions
  (coupled differential-delay equations, p. 4/PDF 4). `f^+(v), f^-(v)` =
  limsup / liminf of S^-(z^v,z)/(e^{-gamma} z^v/log z) as z->infty (p. 4).
- `omega` = Buchstab's function. `gamma` = Euler-Mascheroni constant.
- `Theta_z = prod_{p<=z}(1-1/p)`, `Theta_{x,y} = prod_{x<p<=y}(1-1/p)`,
  hat-`Theta` the same with (1-1/(p-1)) (Section 3, p. 13).
- `P, E` = probability, expectation; subscripted (P_Q, E_Q), (P_{c,d},
  E_{c,d}), (P_c, E_c), (P^0_Q, E^0_Q) as defined in Section 2.1 (p. 13).
- `<=`,`>=`,`~` (asymptotic, F~G means F=(1+o(1))G), `<<`/`>>` (Vinogradov),
  the both-sided-order symbol rendered `asymp`, `o(1)`, `O(.)`. Implied constants
  in O, <<, >>, asymp are absolute unless otherwise specified (p. 13).
- `e^{-lambda} lambda^k / k!` = Poisson(lambda) point mass at k.
- `int_a^b` = integral; `prod`, `sum`, `union`, `cap`, `emptyset`.

Where a display was scrambled by pdftotext it was transcribed from a
200-dpi page render and flagged [TRANSCRIPTION-UNSURE, resolved-by-image];
the layer of each hard transcription is recorded in FLAGS.

---

## 1. FRONT MATTER AND ABSTRACT

Title (p. 1): "THE POISSON TAIL CONJECTURE FOR PRIMES IN SHORT INTERVALS".
Author (p. 1): "ABHISHEK JHA".

Abstract (p. 1), verbatim (transcribed from text layer; math symbols
ASCII-ized):

> "In 1976, Gallagher showed that, conditional on the Hardy-Littlewood
> conjectures, the number of primes below x in a randomly chosen short
> interval of length lambda log x asymptotically follows a Poisson
> distribution with mean lambda. Correspondingly, the normalized gaps
> between consecutive primes follow an exponential distribution, provided
> that the scaling parameter lambda is fixed. We investigate the validity
> and limitations of the associated folklore Poisson Tail Conjecture as
> lambda is allowed to grow. For slowly growing lambda, and conditional on
> a strong variant of the Hardy-Littlewood conjectures, we establish
> asymptotics demonstrating that the local counting statistics rigorously
> align with these predictions. Furthermore, we identify a phase
> transition and explore the breakdown of these distributions for larger
> lambda, capturing the precise deviations when lambda grows slower than
> any fixed power of log x. The proof relies on a novel combination of
> extremal interval sieve estimates and concentration inequalities from
> probability."

---

## 2. INTRODUCTION (Section 1), setup and the assumed hypothesis

PARAPHRASE except quotes. The introduction fixes the Hardy-Littlewood
input and the counting functions; the load-bearing displays are quoted
complete.

### 2.1 The Hardy-Littlewood conjecture and Gallagher's Poisson law

The Hardy-Littlewood conjecture is stated (p. 1) as (1.2):

> "|{n <= x : n + h in P for all h in H}| = (S(H) + o(1)) int_2^x dt /
> log^{|H|} t   (x -> infinity)"

with the singular series (1.3), verbatim (p. 1):

> "S(H) := prod_p ( 1 - |H mod p|/p ) ( 1 - 1/p )^{-|H|}."

Gallagher's Poissonian consequence, (1.4) (p. 2), verbatim:

> "lim_{x->infinity} (1/x) |{n <= x : pi(n + lambda log x) - pi(n) = k}| =
> e^{-lambda} lambda^k / k!,"

stated "for fixed lambda > 0 and k >= 0, if (1.2) holds uniformly for
|H| = k and H subset [0, lambda log x]" (p. 2). Gallagher's analysis
"relies on the relation" (1.5) (p. 2), verbatim:

> "sum_{H in [0,y], |H|=k} S(H) ~ (y choose k)   (y -> infinity),"

"so that the singular series for sets of size k have an average value of
one" (p. 2).

### 2.2 The Poisson Tail Conjecture

Cramer's random model C (each n>=3 included independently with prob
1/log n) predicts (1.6) for growing lambda = o(log x), leading to
(p. 2, Conjecture 1.1), verbatim:

> "Conjecture 1.1. For any eps > 0 and 0 <= lambda <= (log x)^{1-eps}, we
> have
> sum_{p_n <= x, p_{n+1} - p_n >= lambda log x} 1  asymp  e^{-lambda}
> x/log x."   [equation (1.7)]

Context (p. 2, PARAPHRASE): Leung [16] proved a joint-Poisson statement
for primes in finitely many disjoint intervals n+I_1 log n, ..., n+I_r
log n; Kravitz-Woo-Xu [14] proved an averaged polynomial analog. The
obstacle to extending Gallagher's approach (p. 2): "standard methods for
estimating these sums of singular series are limited to ranges where
lambda is at most log log x (see [20])"; Kuperberg [15] pushed these to
their limits. Banks-Ford-Tao [1] instead model primes as survivors of a
random sieve.

### 2.3 The random set R and Proposition 1.2

The Banks-Ford-Tao random set R := {n >= e^2 : n in S_{z(n)}} satisfies an
analog of (1.2) uniformly with power-saving error. Proposition 1.2 (p. 3),
verbatim [display transcribed from page image, resolved-by-image]:

> "Proposition 1.2. Fix c in [1/2, 1). Almost surely, we have
> |{n <= x : n + h in R for all h in H}| = S(H) int_2^x dt/log^{|H|} t
>   + O( x^{ 1 - (1-c)/(8c^2 - 2c) + o(1) } )
> uniformly for all admissible tuples H satisfying |H| <= log^c x and in
> the range H subset [ 0, exp( log^{1-c} x / log_2 x ) ] where the constant
> implied by the O-symbol exists almost surely, though it is not uniformly
> bounded with respect to x."

For comparison the paper records the conjectured strong form for primes,
(1.9) (p. 3), verbatim:

> "|{n <= x : n + h in P for all h in H}| = S(H) int_2^x dt/log^{|H|} t
>   + O( x^{1/2 + o(1)} )   (x -> infinity)."

"This matches the error term in Proposition 1.2 when c = 1/2" (p. 3).

### 2.4 The two counting functions (1.10), (1.11)

Verbatim (p. 3):

> "M_A(x; y) := |{n <= x : n in A and [n+1, n+y] cap A = emptyset}|,"
> "N_A(x; y, k) := |{n <= x : |[n+1, n+y] cap A| = k}|."

Paper's own note on the asymmetry (p. 3), verbatim:

> "Note the intentional asymmetry between the definitions of M_A and N_A.
> For the quantity M_A(x;y), the index n is restricted to A to count the
> gaps between consecutive elements of the set that exceed length y. On the
> other hand, N_A(x;y,k) drops this restriction, measuring the frequency of
> short intervals [n+1, n+y] containing exactly k elements of A, sampled
> uniformly over all integers n <= x."

### 2.5 The assumed hypothesis HL[phi, psi] -- Definition 1.3

THE HYPOTHESIS ASSUMED. Definition 1.3 (p. 3), verbatim (text layer,
confirmed against page image):

> "Definition 1.3. Let phi and psi be unbounded real-valued functions. We
> say that A subset N satisfies HL[phi, psi] if the relation
> (1.12)  |{n <= x : n + h in A for all h in H}| = S(H) int_2^x dt /
>         log^{|H|} t + E(x, H)
> holds uniformly over all finite sets of integers H subset [0, phi(x)]
> with |H| <= psi(x), and the error term satisfies
> |E(x, H)| <= x e^{-psi(x)} log_2 x  for x >= x_0, where x_0 is some
> constant independent of H."

Immediately after (p. 4), verbatim: "Under the assumption that A = P, this
condition recovers the classical Hardy-Littlewood conjecture for primes."

So HL[phi, psi] is a UNIFORM Hardy-Littlewood conjecture with two explicit
knobs: phi(x) bounds the shift range (H subset [0, phi(x)]), psi(x) bounds
the tuple rank (|H| <= psi(x)), and the same psi controls the error via the
exponential factor e^{-psi(x)} (times log_2 x = log log x). Note log_2 x
here is the iterated logarithm, per the convention below.

### 2.6 The iterated-log convention and the thresholds (1.13)

Convention (p. 4), verbatim:

> "We let log_k x denote the k-fold iterated logarithm truncated at zero;
> that is log_1 x := max{0, log x} and log_k x := max{0, log(log_{k-1} x)}
> for k >= 2."

Equation (1.13) (p. 4), verbatim [transcribed from page image,
resolved-by-image; pdftotext scrambled the radicals]:

> "lambda' = lambda'(x) := exp( (1/sqrt(7)) sqrt( log_2 x * log_3 x ) )
>  and  lambda'' = lambda''(x) := exp( 4 log_2 x * log_4 x / log_3 x )."

---

## 3. MAIN RESULTS (Section 1, continued), verbatim

### 3.1 Theorem 1.4 -- exponential gap distribution (small lambda)

Theorem 1.4 (p. 4), verbatim [resolved-by-image]:

> "Theorem 1.4 (Hardy-Littlewood implies uniform exponential distribution).
> Assume that A subset N satisfies HL[ lambda log x, exp( sqrt( log_2 x *
> log_3 x ) ) ]. Then, for all sufficiently large x, we have
> M_A(x; lambda log x) = (x e^{-lambda} / log x) ( 1 + O( (log_2 x)^{-10} )
> ), uniformly for 0 < lambda <= lambda'."

Corollary 1.5 (p. 4), verbatim: the same asymptotic holds for the random
set R almost surely:

> "Corollary 1.5 (Exponential distribution for gaps in the random model).
> Almost surely, we have M_R(x; lambda log x) = (x e^{-lambda}/log x)( 1 +
> O( (log_2 x)^{-10} ) ), uniformly for 0 < lambda <= lambda' and for large
> x, where the implied constant depends only on that of Proposition 1.2."

### 3.2 Conjecture 1.6 (Kuperberg) and Theorem 1.7 -- Poisson statistics

Conjecture 1.6 (Kuperberg [15, Conjecture 1.7]) (p. 4), verbatim:

> "Conjecture 1.6. Let lambda = (log x)^{o(1)} and k << (log_2 x)^2. Then,
> (1.14)  |{n <= x : pi(n + lambda log x) - pi(n) = k}| ~ x e^{-lambda}
> lambda^k / k!   (x -> infinity)."

Theorem 1.7 (p. 4), verbatim [resolved-by-image]:

> "Theorem 1.7 (Hardy-Littlewood implies uniform Poisson statistics).
> Assume that A subset N satisfies HL[ lambda log x, exp( sqrt( log_2 x *
> log_3 x ) ) ]. Then, for all sufficiently large x, we have
> N_A(x; lambda log x, k) = x (e^{-lambda} lambda^k / k!)( 1 + O(
> (log_2 x)^{-10} ) ), uniformly for 1/sqrt(log x) <= lambda <= lambda' and
> non-negative integers k such that max{ k, k log(k/lambda) } <= lambda'."

Remark 1.8 (p. 5), verbatim: "We observe that Kuperberg restricted the
formulation of the conjecture to the regime k << (log_2 x)^2. Our theorem
shows that, under the relevant assumptions, the predicted asymptotic
behavior holds over a substantially wider range of k."

Remark 1.9 (p. 5), verbatim: "While the above theorem is stated for
lambda >= 1/sqrt(log x), analogous results for smaller lambda can be
obtained via a straightforward extension of our methods. We do not pursue
this here, as our primary focus lies in the larger ranges of lambda.
Additionally, for small lambda, the Brun-Titchmarsh theorem imposes a
barrier on the parameter k, restricting it to the range
k << lambda log x / log(lambda log_2 x)."

### 3.3 The interval sieve, and Proposition 1.10 (unconditional)

The interval sieve function (p. 4/5): "S(x, y, z) = #{x < n <= x + y : n
has no prime factor <= z}", with S^-(y,z) = min_x S(x,y,z) =
min_{(a_p)} |(0,y] cap S_z|. Jurkat-Richert [13] bounds (p. 4/PDF 4-5),
verbatim:

> "(1 + o(1)) e^{-gamma} F(v) z^v/log z >= S^-(z^v, z) >= (1 - o(1))
> e^{-gamma} f(v) z^v/log z   (z -> infinity),"

with f, F the coupled linear-sieve differential-delay functions
(f(v)<1<F(v) for all v; both tend to 1 as v->infinity). Following [11]:
"f^+(v) := limsup_{z->infinity} S^-(z^v,z)/(e^{-gamma} z^v/log z)" and
"f^-(v) := liminf ..." (v > 1). The paper records (p. 4): "It is immediate
from the definitions that f^+(v) >= f^-(v) >= f(v). Interestingly,
Granville [8, Corollary 1] proved that the lower bound is sharp, showing
f^-(v) = f(v) conditional on the existence of an infinite sequence of
Siegel zeros. In the other direction, considering random choices for the
residue classes a_p mod p gives the upper bound f^+(v) <= 1."

Proposition 1.10 (p. 4), verbatim -- an UNCONDITIONAL sieve fact (proof
"essentially due to Maier [12]", given in Section 2):

> "Proposition 1.10. For all v > 1, we have f^+(v) < 1."

### 3.4 Maximal-gap conjectures and Theorem 1.12 (very rapid growth)

Cramer conjectured limsup (p_{n+1}-p_n)/log^2 p_n = 1; Granville argued
this false and predicted limsup >= 2 e^{-gamma} = 1.12292...; Banks-Ford-
Tao [1] and Granville-Lumley [9] refined this (Conjecture 1.11, p. 5):
"limsup_{n->infinity} (p_{n+1}-p_n)/log^2 p_n = 1/f^-(2) >= 2 e^{-gamma}".

Theorem 1.12 (p. 6), verbatim [resolved-by-image; note both HL slots carry
the exponent c' (primed)]:

> "Theorem 1.12. Fix c, c' in (0,1) with c < c'. Assume that A subset N
> satisfies HL[ log^{1+c'} x, log^{c'} x ]. Set lambda := lambda(x) =
> log^c x. Then we have
> (x/log x) exp( -( f(1 + 1/c) + o_{c,c'}(1) ) lambda ) >= M_A(x; lambda
> log x) >= (x/log x) exp( -( f^+(1 + 1/c) + o_{c,c'}(1) ) lambda ),
> as x -> infinity. Moreover, the same bounds hold for N_A(x; lambda log x,
> 0) as well."

Remark 1.13 (p. 6), verbatim -- the ONLY sparse-scale (unbounded-sequence)
statement in the paper:

> "While we would expect f^+(v) = f^-(v) for v > 1, we can prove that the
> stronger bound obtained by replacing f^+ with f^- in the lower bound of
> the above theorem holds, but only for a sequence of values of x tending
> to infinity."

### 3.5 Theorem 1.14 -- the intermediate regime / phase transition

Transition text (p. 6), verbatim: "As c -> 0, the sieve functions
f(1 + 1/c) and f^+(1 + 1/c) both tend to 1. Hence, to capture the precise
deviations from the Poisson statistics when lambda grows slower than any
fixed power of log x, a different approach is required. ... Although our
current analysis does not isolate the exact threshold of the phase
transition, we can pinpoint the failure of the Poisson distribution for
sufficiently large lambda in this regime. As a direct consequence, this
proves that Conjecture 1.6 does not hold over its full conjectured range."

Theorem 1.14 (p. 6), verbatim [resolved-by-image; here both HL slots carry
the UNprimed exponent c]:

> "Theorem 1.14. Fix c in (0,1). Assume that A subset N satisfies HL[
> log^{1+c} x, log^c x ]. Let lambda = lambda(x) >= lambda'' (as defined in
> (1.13)) be a parameter such that u = (log_2 x)/log lambda -> infinity as
> x -> infinity. Then, for all sufficiently large x (depending only on c),
> we have
> M_A(x; lambda log x) = x e^{-lambda} exp[ lambda exp( -(1 + o(1)) u log u
> ) ]. Moreover, the same asymptotic holds for N_A(x; lambda log x, 0) as
> well."

Remark 1.15 (p. 6), verbatim (the 1/log x density-factor point):

> "Heuristically, one expects the asymptotic of M_A(x; lambda log x) to
> include an additional density factor of 1/log x relative to N_A(x; lambda
> log x, 0), reflecting the density of the initial element in A. However,
> in both Theorems 1.12 and 1.14, this logarithmic factor is completely
> absorbed by the large exponential error terms, making the bounds for
> M_A(x; lambda log x) and N_A(x; lambda log x, 0) identical up to the
> stated error."

Continuation of Remark 1.15 (p. 6), verbatim (the breakdown direction):

> "Furthermore, Theorem 1.14 explicitly shows the breakdown of the Poisson
> statistics for N_A and the corresponding exponential gap distribution for
> M_A. The Cramer-Gallagher heuristic predicts a density strictly
> proportional to e^{-lambda}. In contrast, our lower bound has the
> additional multiplicative factor of the order exp(lambda exp(-(1 + o(1))
> u log u)). As the lower bound on lambda ensures that u log u << log_3 x,
> this factor diverges to infinity as x -> infinity. Thus, the frequency of
> empty intervals in both settings exceeds the heuristic prediction."

---

## 4. DISCUSSION OF THE MAIN RESULTS (Section 1.1) -- PARAPHRASE except quotes

Three self-declared caveats (p. 6-7):

- "Optimizing the Hardy-Littlewood hypothesis" (quote, p. 6): "The
  assumptions underlying our results, specifically the conditions on the
  function psi in the hypothesis HL[phi, psi], can be sharpened. The
  admissible range for |H| can be made fully explicit in terms of lambda
  and weakened, as is implicitly shown within the proofs of these
  theorems." Error terms could also be optimized; the author prioritized
  clarity over the strongest estimates.

- "Uniformity in the Hardy-Littlewood conjectures" (quote, p. 6): "As
  illustrated by Proposition 1.2, it is expected that a wide class of
  integer sequences obeys Hardy-Littlewood type conjectures with a level of
  uniformity that far exceeds the assumptions required by our theorems. In
  particular, this strong degree of uniformity, capable of accommodating
  substantially larger tuples and shift ranges, is expected to hold for the
  sequence of prime numbers." (So the HL[phi,psi] hypothesis is conjectural
  for primes; only R is proven (Prop 1.2) to satisfy a form of it.)

- "Deriving the exponential distribution" (quote, p. 6-7): "For a fixed
  parameter lambda as in (1.1), the classical exponential gap distribution
  is known to follow directly from the Gallagher-type singular series
  averages in (1.5). However, in our regime where lambda is allowed to grow
  with x, transitioning from the Gallagher-type result to the gap
  distribution does not seem feasible. Specifically, as noted in Remark
  1.15, evaluating M_A involves an additional global density factor of
  1/log x."

Comparison with prior work (p. 6-7, PARAPHRASE + quote): the methods
resemble [1, Section 8] (Banks-Ford-Tao) but there lambda grows like log x,
whereas here "we deal with much smaller values of lambda, forcing a more
delicate treatment"; the gap distribution M_A "requires enforcing the
condition 0 in S_z throughout the sieving process," which "breaks the pure
martingale structure," circumvented by "a generalized variant of Azuma's
inequality (Lemma 2.8)." Whereas [1, Section 8] only needs a positive lower
bound on N_A(x; lambda log x, 0), "the proofs of Theorems 1.4 and 1.7
require a more careful analysis to bound the error terms."

Plan of paper (Section 1.2, p. 7): Section 2 = sieve + probability
preliminaries (extremal interval sieve, generalized Azuma); Section 3 =
random sieving estimates; Section 4 = Brun-type sieve proving Theorems 1.4
and 1.7 (small lambda, validity); Section 5 = Theorems 1.12 and 1.14
(breakdown, large/intermediate lambda); Section 6 = barriers and remarks.

---

## 5. PROOF-MACHINERY HIGHLIGHTS (Sections 2-5) -- PARAPHRASE except quotes

Only the items that bear on grain, direction, uniformity, and
unconditionality are recorded; the extract is not a line-by-line proof
transcription.

- Lemma 2.1 (fundamental lemma of the combinatorial sieve, from [4, Thm
  6.12]) and Lemma 2.2 (lower-bound sieve, [13, Theorem 5]) and Lemma 2.3
  (upper-bound sieve, [21, Theorem 3.8]) are UNCONDITIONAL sieve inputs.
  Lemma 2.2 gives S(A,P) >= (1-o(1)) e^{-gamma} f(u) y/log z.

- Lemma 2.4 (Brun's sieve, generalizing [1, Lemma 8.1]): the
  inclusion-exclusion inequalities T <= U_K (K-k even) and T >= U_K (K-k
  odd) that drive both counting functions. Lemma 2.5 (Probabilistic Brun's
  sieve) turns these into the master integral identities for N_A and the
  fixed-point (0 in S_z) count.

- Lemma 2.6 (Extremal interval sieve, [12, Proposition 3] =
  Hildebrand-Maier), verbatim (p. 11), UNCONDITIONAL:

> "For sufficiently large z, let y satisfy 2 <= y <= exp(sqrt(z)). We have
> S^-(y, z) <= y prod_{p<=z}(1 - 1/p)( 1 - exp( -(1 + o(1)) u log u ) ),
> where u = (log y)/log z."

  This is the oscillation input driving the breakdown Theorems 1.12/1.14;
  it produces a single anomalous residue-class choice, not a positive
  proportion (see Section 6 quote below).

- Proof of Proposition 1.10 (p. 11-12), UNCONDITIONAL: uses S(0,z^v,z) ~
  omega(v) z^v/log z (Buchstab), monotonicity of f^+, and [17, Lemma 4]
  (omega(v) - e^{-gamma} changes sign on every unit interval) to conclude
  f^+(v) <= e^{-gamma} min_{u>=v} omega(u) < 1.

- Lemma 2.7 (Azuma) and Lemma 2.8 (Generalized Azuma's inequality) --
  the two-sided concentration tool with a bias term d_j; Remark 2.9: "The
  bias term d_j in this generalized inequality is specifically tailored to
  handle the breakdown of the pure martingale structure later in our
  sieving process."

- Section 3 regime table (p. 13/14): the four regimes and their lambda
  ranges: Arbitrary (lambda >= 1/sqrt(log x), Section 3.3); Slow Growth
  (1/sqrt(log x) <= lambda <= lambda', Lemmas 3.1-3.4, Cor 3.8, Section 4);
  Rapid Growth (lambda > lambda'' with lambda = (log x)^{o(1)}, Lemmas 3.1,
  3.5, Section 5.2); Very Rapid Growth (lambda = log^c x, 0 < c < 1, Lemmas
  3.5, Section 5.1).

- Sections 5.1 and 5.2 prove Theorems 1.12 and 1.14; both are conditional
  on the stated HL hypothesis and both route the anomalous lower bound
  through a "single, unusual choice of residue classes" (see Section 6).

---

## 6. CONCLUDING REMARKS (Section 6), verbatim (p. 28)

> "As noted in the introduction, our current methods do not yet allow us to
> pinpoint the precise threshold of the phase transition for these
> distributions. We anticipate that a substantial improvement to the ranges
> in Theorems 1.4 and 1.7 will require a novel combination of the
> fundamental lemma (Lemma 2.1) with new probabilistic estimates capable of
> handling small primes. Currently, the probabilistic techniques utilized
> here and in [1] are effective only for somewhat larger primes, forcing us
> to apply the fundamental lemma up to a power of lambda. Overcoming this
> limitation remains a major obstacle for future improvements."

> "Conversely, strengthening the breakdown results in Theorems 1.12 and
> 1.14 relies on refining the extremal interval sieve estimates. By
> appealing to known irregularities in the sieving process, our current
> bounds in (5.12) and (5.14) exploit the fact that there exists a single,
> unusual choice of residue classes yielding a sieved set significantly
> smaller than its expected size. To push these limits further, it will be
> necessary to develop such methods capable of generating a large
> multiplicity of such extreme residue classes."

---

## Uniformity ledger

The single organizing fact: every stated asymptotic for the sequence A is
CONDITIONAL on A satisfying HL[phi, psi] for specified phi, psi (Definition
1.3). Only the random set R (Corollary 1.5, via Proposition 1.2) and the
pure sieve facts (Propositions 1.10, Lemma 2.6, Lemmas 2.1-2.3) are
established unconditionally, and none of the R-statements is about the
primes P.

Fixed vs growing:
- x -> infinity is the only genuine limit; all main theorems are "for all
  sufficiently large x" (Theorems 1.4, 1.7, 1.12) or "for a sequence of
  values of x tending to infinity" for the sharpened f^- lower bound only
  (Remark 1.13). No result is stated on a sparse/unbounded scale set except
  Remark 1.13.
- lambda = lambda(x) GROWS with x. Windows: y = lambda log x throughout.
  - Theorem 1.4 (M_A, exponential): 0 < lambda <= lambda' =
    exp((1/sqrt7) sqrt(log_2 x * log_3 x)); hypothesis HL[lambda log x,
    exp(sqrt(log_2 x * log_3 x))].
  - Theorem 1.7 (N_A, Poisson): 1/sqrt(log x) <= lambda <= lambda';
    SAME hypothesis; k constrained by max{k, k log(k/lambda)} <= lambda'.
  - Theorem 1.12 (breakdown, very rapid): lambda = log^c x (0<c<c'<1);
    hypothesis HL[log^{1+c'} x, log^{c'} x].
  - Theorem 1.14 (breakdown, intermediate): lambda >= lambda'' =
    exp(4 log_2 x log_4 x / log_3 x), lambda = (log x)^{o(1)}, u =
    (log_2 x)/log lambda -> infinity; hypothesis HL[log^{1+c} x, log^c x].
- rank k: appears only in N_A (Theorem 1.7) and is bounded by max{k, k
  log(k/lambda)} <= lambda'. Since lambda' = exp((1/sqrt7) sqrt(log_2 x
  log_3 x)) grows faster than any fixed power of log_2 x, the admissible k
  far exceeds Kuperberg's k << (log_2 x)^2 (Remark 1.8). M_A carries no
  rank parameter (it is the k=0 gap count, index restricted to A).
- phi (shift range) and psi (rank + error) are the two HL knobs. The error
  is |E(x,H)| <= x e^{-psi(x)} log_2 x, so a larger admissible rank psi
  forces a stronger (smaller) HL error. In Theorems 1.4/1.7, psi(x) =
  exp(sqrt(log_2 x * log_3 x)); phi(x) = lambda log x.

Constants: implied constants in O, <<, >>, asymp are ABSOLUTE unless
specified (Section 2.1, p. 13). Exceptions: Theorem 1.12/1.14 constants
"depend only on c" (and c') -- o_{c,c'}(1); Corollary 1.5 constant "depends
only on that of Proposition 1.2"; the Proposition 1.2 O-constant "exists
almost surely, though it is not uniformly bounded with respect to x."

Direction: Theorems 1.4 and 1.7 are two-sided (exact asymptotics with
relative error (log_2 x)^{-10}). Theorem 1.12 is two-sided but with a gap
between f and f^+ in the two exponents. Theorem 1.14 is an exact asymptotic
(with (1+o(1)) inside the double exponential). The breakdown is in the
EXCESS direction: empty-interval frequency EXCEEDS the e^{-lambda}
heuristic (Remark 1.15).

Object/grain: the controlled quantities are M_A(x;y) (count of gaps
exceeding y, index in A) and N_A(x;y,k) (count of integers whose length-y
right-window holds exactly k elements of A). For A=P these are prime-count
statistics of short intervals; they are NOT class masses of consecutive-
gap words.

---

## What the paper does NOT contain

Mandatory NOT-FOUND probes from the dispatch Section 4.5:

"unconditional main theorem": NOT FOUND for the primes / for a general
sequence A. Every main theorem (1.4, 1.7, 1.12, 1.14) is explicitly
conditional on A satisfying HL[phi, psi] (Definition 1.3), and HL for the
primes is only "expected" (Section 1.1, "Uniformity in the Hardy-Littlewood
conjectures", p. 6). The unconditional results in the text are (a)
Proposition 1.10 (f^+(v) < 1, all v>1), (b) the sieve lemmas 2.1-2.3 and
Lemma 2.6 (extremal interval sieve), and (c) Corollary 1.5 for the RANDOM
set R (unconditional as a statement about R, via Proposition 1.2, but not
about primes). No unconditional statement about the primes is present.

"consecutive": FOUND, but only for gaps-between-elements, not for a
gap-word grain. Abstract (p. 1): "the normalized gaps between consecutive
primes follow an exponential distribution." Page 3 (on M_A): "the index n
is restricted to A to count the gaps between consecutive elements of the
set that exceed length y." These are large-gap counts (M_A) and
interval-content counts (N_A); the paper contains no statement conditioned
on a prescribed pattern of consecutive gaps.

"word grain": NOT FOUND. No class mass N_{P,d} of consecutive-gap words, no
count of integers realizing a fixed gap word, appears. The grain is prime /
element counts (M_A, N_A).

"class normalisation": NOT FOUND. No quantity is normalised by a gap-word
class count or restricted to a fixed consecutive-gap pattern. The
normalisations present are the Poisson e^{-lambda} lambda^k/k! and the
global x/log x density.

"any statement on an unbounded scale sequence rather than all large x":
FOUND, in a single limited place -- Remark 1.13 (p. 6), verbatim: "we can
prove that the stronger bound obtained by replacing f^+ with f^- in the
lower bound of the above theorem holds, but only for a sequence of values
of x tending to infinity." This is a sparse-scale (unbounded-sequence)
statement, but (i) conditional on HL[log^{1+c'} x, log^{c'} x], (ii) in the
breakdown LOWER-bound (excess-frequency) direction, not an upper /
non-concentration statement, and (iii) about the k=0 empty-interval count.
All other results are stated for all sufficiently large x.

Additional negatives relevant to the consuming context:
- "singular series average at growing rank": the paper CITES that direct
  singular-series methods are "limited to ranges where lambda is at most
  log log x (see [20])" and that Kuperberg [15] pushed them further
  (p. 2), but proves no new singular-series average itself; its route
  bypasses S(H) fluctuations via the random sieve.
- "second moment / variance of the count": NOT FOUND (the probabilistic
  tool is Azuma-type concentration, Lemmas 2.7-2.8, not a variance
  computation of N_A or M_A over A).
- "middle-slot upper bound decoupled from the exact asymptotic": NOT FOUND
  as a standalone statement; the upper control at any k in Theorem 1.7 is
  the two-sided exact asymptotic, valid only in its stated lambda, k range.

---

## COMMENTARY (assessment, NOT extraction)

Consuming context (quoted verbatim from the dispatch):

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

C1. Headline. This is a CONDITIONAL paper, and its conditionality is the
governing fact for the project. Every asymptotic for a sequence A (Theorems
1.4, 1.7, 1.12, 1.14) assumes A satisfies HL[phi, psi] (Definition 1.3) --
a uniform Hardy-Littlewood conjecture with an explicit rank knob psi, shift
knob phi, and matched error x e^{-psi(x)} log_2 x. For the primes this
hypothesis is only "expected" (Section 1.1, p. 6). Therefore Jha supplies
NO unconditional averaged non-concentration statement about primes. What it
supplies is a precise map, on exactly the A1 x A2 (rank x window) axes, of
how strong a Hardy-Littlewood input is currently needed to force Poisson
statistics at a growing window -- which is the value the dispatch itself
assigns to this paper ("it fixes how strong a hypothesis is currently
needed at our scale").

C2. The phase transition (the paper's own novelty). In the Poisson regime
(Theorems 1.4/1.7) the local statistics are exactly Poisson/exponential up
to lambda <= lambda' = exp((1/sqrt7) sqrt(log_2 x log_3 x)). Once lambda is
a small fixed power of log x (Theorem 1.12, lambda = log^c x) or in the
intermediate regime (Theorem 1.14, lambda >= lambda'', lambda =
(log x)^{o(1)}) the Poisson law BREAKS, and the direction of breakdown is
EXCESS: "the frequency of empty intervals in both settings exceeds the
heuristic prediction" (Remark 1.15). This disproves Conjecture 1.6
(Kuperberg) over its full range (p. 6). The excess direction is the
opposite of the "keep mass off the modal middle" non-concentration the
project needs; the breakdown is concentration at the k=0 tail, not
anti-concentration at the middle.

C3. Why A3 (grain) fails and why that is decisive. The controlled objects
are M_A(x;y) (large-gap counts, index in A) and N_A(x;y,k) (integers with
exactly k elements of A in a length-y right-window). For A=P these are
prime-count statistics of short intervals -- the classical
"pi(n+lambda log x)-pi(n) = k" grain of (1.4). They are NOT class masses
N_{P,d} of consecutive-gap WORDS. The project's A3 axis is precisely the
transfer from interval/prime counts to word-grain realisations, and this
paper stays entirely on the interval-count side (the mandatory NOT-FOUND
probes "word grain" and "class normalisation" both return absent). Even if
A1, A2, A4, A5, A6 were favorable, A3 alone disqualifies the paper as a
carrier.

C4. What DOES align, axis by axis, taken structurally (i.e. ignoring
conditionality, which C1 already books as fatal):
- Rank (A1): Theorem 1.7 admits k with max{k, k log(k/lambda)} <= lambda',
  which comfortably contains k ~ (2/ln 2) log_2 x (that is the project's
  rank). So the RANK SCALE is reached (indeed exceeded, Remark 1.8).
- Window (A2): the window is y = lambda log x; the project's h ~ log x *
  log_2 x corresponds to lambda ~ log_2 x, which is inside the Poisson
  range lambda <= lambda' (since lambda' >> log_2 x). So the WINDOW SCALE
  is reached.
- Direction (A4): the Poisson-regime results are two-sided exact
  asymptotics, so they DO deliver an upper bound at every k in range,
  including the modal middle k ~ lambda; structurally the upper direction
  is present. Caveat: it is an equality inside a narrow regime, not a
  robust one-sided non-concentration bound, and the paper's genuinely NEW
  content (Theorems 1.12/1.14) is in the excess/concentration direction.
- Strength (A5): relative error O((log_2 x)^{-10}) is far stronger than the
  "constant order suffices" the project needs; A5 is over-satisfied.
- Density (A6): the main theorems hold for ALL sufficiently large x, which
  is a superset of any sparse/unbounded scale set; A6 is over-satisfied
  (the project only needs sparse scales). The one sparse-scale statement
  (Remark 1.13) is the exception, and it points the wrong way (C2).

C5. Even-Cramer-smooth test. The paper never considers the deterministic
gap system q_1=2, q_2=3, q_3=5, q_4=7, q_{n+1}=q_n+2*ceil(ln q_n/2); its
results are conditional on HL[phi,psi], which such a smoothed deterministic
sequence would presumably NOT satisfy with a genuine singular series. Since
the paper offers no verdict and I will not guess whether HL holds there or
whether the Poisson law would fail there, I record this as UNTESTED against
the even-Cramer-smooth model.

C6. Net supply for references.md. What is defensibly transcribable and
citable: (a) a CONDITIONAL uniform Poisson asymptotic for N_A(x; lambda
log x, k) and a conditional uniform exponential gap asymptotic for M_A(x;
lambda log x), at growing window lambda log x with lambda up to lambda' =
exp((1/sqrt7) sqrt(log_2 x log_3 x)); (b) an explicit phase transition
proving the Poisson law breaks (empty intervals in excess) once lambda is a
small power of log x, disproving Kuperberg Conjecture 1.6 over its full
range; (c) UNCONDITIONAL by-products: Proposition 1.10 (f^+(v)<1) and the
random-model Corollary 1.5. Nothing here is an unconditional prime-side
non-concentration/upper-uniformity statement, and nothing is at word grain.

Per-axis verdict (structural mapping; C1 books the overriding CONDITIONAL
failure separately):
- A1 (rank k ~ (2/ln 2) lnln x): CLEARS -- Theorem 1.7 admits k up to
  max{k, k log(k/lambda)} <= lambda', exceeding (2/ln 2) log_2 x.
- A2 (window h ~ (ln x)(lnln x)): CLEARS -- window lambda log x with
  lambda ~ log_2 x lies inside the Poisson range lambda <= lambda'.
- A3 (grain = consecutive-gap-word class masses N_{P,d}): FAILS -- the
  grain is interval/prime counts M_A, N_A, never word-class masses.
- A4 (direction = upper / non-concentration): CLEARS with caveat -- the
  Poisson-regime two-sided asymptotic supplies an upper bound at the middle
  slot, but the paper's own new content (Thm 1.12/1.14) is in the excess/
  concentration direction, the opposite of the needed non-concentration.
- A5 (strength = constant order suffices): CLEARS -- relative error
  (log_2 x)^{-10}, far beyond constant order.
- A6 (density = sparse scales, no s-uniformity): CLEARS -- results hold for
  all sufficiently large x, a superset of sparse scales.
- Overriding: NOT A CARRIER. Every A-axis result is CONDITIONAL on
  HL[phi,psi] (unproven for primes), and A3 fails on grain. clears_all_
  six_axes = false.
- Even-Cramer-smooth deterministic gap system: UNTESTED (the paper offers
  no verdict; guessing is disallowed).

---

## FLAGS (consolidated)

1. [TRANSCRIPTION-UNSURE, resolved-by-image] Equation (1.13) (p. 4):
   pdftotext scrambled the radicals and the (1/sqrt7) factor. Transcribed
   from a 200-dpi page render: lambda' = exp((1/sqrt7) sqrt(log_2 x *
   log_3 x)), lambda'' = exp(4 log_2 x * log_4 x / log_3 x). Text layer
   showed a broken "exp [sqrt] ... log2 x log3 x" fragment (layout line ~207).

2. [TRANSCRIPTION-UNSURE, resolved-by-image] Theorems 1.4 and 1.7 (p. 4):
   the HL argument "exp(sqrt(log_2 x * log_3 x))" and the relative error
   "(1 + O((log_2 x)^{-10}))" and the k-constraint "max{k, k log(k/lambda)}
   <= lambda'" were confirmed from the page render; the text layer split
   the square roots and the theorem headers ("Theorem 1.4 (Hardy-Littlewood
   ... implies ...)") across broken lines.

3. [TRANSCRIPTION-UNSURE, resolved-by-image] Theorem 1.12 (p. 6): both HL
   slots carry the PRIMED exponent c' -- HL[log^{1+c'} x, log^{c'} x] --
   confirmed from the page image; the text layer floated the prime marks
   onto a separate line (as floating prime marks) and rendered the exponents as unprimed
   "log1+c x, logc x" (layout lines ~328-330). Theorem 1.14 (p. 6) by
   contrast carries the UNprimed exponent c in both slots -- HL[log^{1+c}
   x, log^c x] -- also confirmed from the image. The c-vs-c' distinction
   between the two breakdown theorems is real, not a transcription artifact.

4. [TRANSCRIPTION-UNSURE, resolved-by-image] Proposition 1.2 (p. 3): the
   error exponent "1 - (1-c)/(8c^2 - 2c) + o(1)" and the shift range "H
   subset [0, exp(log^{1-c} x / log_2 x)]" were read from the page image;
   the text layer stacked the fraction and the exp-argument illegibly
   (layout lines ~161-168).

5. [PRINTED-ODDITY / convention] "log_2 x" throughout this paper denotes
   the ITERATED logarithm log log x (Definition on p. 4), NOT (log x)^2.
   Hence "(log_2 x)^{-10}" = (log log x)^{-10} and the HL error factor
   "e^{-psi(x)} log_2 x" carries log log x. This is the opposite of a
   common "log_2 = log base 2" or "log^2" reading and is flagged to prevent
   misinterpretation. Unlike the Pintz note (pintz10-singser.md flag 3),
   here the convention is stated explicitly by the author.

6. The abstract's arXiv stamp "arXiv:2605.23014v1 [math.NT] 21 May 2026"
   is printed vertically in the left margin of p. 1; date recorded as
   21 May 2026.

7. In (1.5) the paper writes the binomial "(y choose k)" as a stacked
   "y \\ k" in a large paren; transcribed as (y choose k) (text layer
   line ~77-78). No ambiguity.

8. Conjecture 1.11 (p. 5) writes "1/f^-(2) >= 2 e^{-gamma}" with a footnote
   chain "f^-(2) <= e^{gamma} omega(2) = e^{gamma}/2"; transcribed as
   printed. Not load-bearing for this extract.
