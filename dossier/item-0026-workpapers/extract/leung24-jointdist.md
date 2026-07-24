# EXTRACTION: Sun-Kai Leung, "Joint distribution of primes in multiple short intervals"

Source (only evidence base): /home/istr/pro/erdos251/dossier/2401.04000v4.pdf
sha256 bbc3bf4724844976fbb5dd345dd647d56139c33e45c195ab136d95ec01a20c31
(operator-verified; re-verified this session, matches).
arXiv:2401.04000v4 [math.NT] 3 Feb 2026. 43 pages. A4.
Author: Sun-Kai Leung, Departement de mathematiques et de statistique,
Universite de Montreal, CP 6128 succ. Centre-Ville, Montreal, QC H3C 3J7,
Canada. Email: sun.kai.leung@umontreal.ca (p. 43).
2020 Mathematics Subject Classification (p. 1): 11M26, 11N05, 60F05.
No printed journal reference on the PDF (arXiv preprint).
Grant footnote (Acknowledgements, p. 42): "The latter part of this work
was supported by the Swedish Research Council under grant no. 2016-06596
while the author was in residence at Institut Mittag-Leffler in Djursholm,
Sweden during the semester of Winter 2024."

Front-matter check vs steering identification: MATCHES. Author is
Sun-Kai Leung; title is "Joint distribution of primes in multiple short
intervals" exactly as steered. Target filename leung24-jointdist.md kept.

---

## Transcription conventions

ASCII only. Diacritics transliterated (Renyi, de la Breteche, Teravainen,
Erdos, Universite, Montreal, Departement, Mittag-Leffler). Mathematics in
LaTeX-like ASCII. Anchors are the paper's own numbering (Theorem/
Proposition/Corollary/Lemma/Definition/Remark/Conjecture/equation/
Section); page numbers (printed = PDF page here, since printed page 1 is
PDF page 1) are a secondary aid.

Symbol table (every non-obvious glyph):

- psi(x) := sum_{n <= x} Lambda(n)  -- Chebyshev weighted prime-power
  count (von Mangoldt weighting log p on prime powers p^k).
- Lambda(n) := log p if n = p^k for an integer k >= 1, else 0.
- pi(x) := #{p <= x}  -- unweighted prime count (used only in the
  arithmetic-progression race discussion, NOT in the short-interval
  results).
- delta > 0  -- the (relative) interval half/length parameter; interval
  length is delta*x. "sufficiently small delta" throughout.
- x, X  -- x in [2, X]; X -> infinity is the ambient limit.
- t = (t_1, ..., t_r) in R^r  -- shift vector; interval j is centered at
  (1 + t_j*delta)x. Disjointness imposed as |t_j - t_k| >= 1 for j != k.
- r >= 1  -- the NUMBER OF INTERVALS (the configuration size / rank
  analogue).
- [r] := {1, ..., r}.
- E(x; delta, t) := (1/sqrt(x)) [ psi((1+t*delta)x + (1/2)delta*x)
  - psi((1+t*delta)x - (1/2)delta*x) - delta*x ]  -- normalized
  deviation of the weighted count in one interval. Bold E(x;delta,t) is
  the r-tuple (E(x;delta,t_1), ..., E(x;delta,t_r)).
- Etilde(x; delta, t) := (E(x;delta,t_1)/sqrt(V_1), ...,
  E(x;delta,t_r)/sqrt(V_r))  -- renormalized (unit-variance) deviation.
  Rendered "Etilde" for the tilde-E of the paper.
- w(s) = w(s; delta, t) := (1/s)[ (1 + (t + 1/2)delta)^s
  - (1 + (t - 1/2)delta)^s ]  (eq. (2.1)); w_j(s) := w(s; delta, t_j).
- rho = 1/2 + i*gamma  -- nontrivial zero of the Riemann zeta function at
  height gamma (RH assumed, so real part exactly 1/2).
- gamma (bare)  -- ordinate of a zeta zero; sums "sum_gamma" and
  "sum_{gamma > 0}" run over these.
- gamma_Q  -- the Euler-Mascheroni constant (paper writes gamma with a
  blackboard-bold Q subscript to avoid collision with the zero-ordinate
  gamma; see FLAG 1). Numerically 0.5772...
- N(T) := #{0 < gamma <= T}  -- zero-counting function.
- N(0, C)  -- multivariate Gaussian, mean vector 0, covariance matrix C.
- Cov_jk = Cov_jk(delta, t) := sum_gamma w_j(rho) w_k(rho)  -- covariance
  entry; V_j := Cov_jj is the j-th variance.
- Delta(t) := (1/2)[ (t+1)log(t+1) - 2t log t + (t-1)log(t-1) ]
  (eq. (2.2))  -- second-order central difference of f(t)=(1/2)t log t.
- C = (c_jk)_{r x r} with c_jk := Cov_jk / sqrt(V_j V_k)  -- the
  "correlation matrix" (unit diagonal). [In Corollary 1.1 the symbol C is
  the explicit 2x2 correlation matrix; det C its determinant.]
- T_S := 1 + max_{j in S} |t_j|  (for S a subset of [r]); T := T_{[r]}.
- P^log_x(...) , E^log_x(...)  -- logarithmic-density probability /
  expectation over x in [2, X] with weight dx/x (Definition 2.1).
- mu_{delta,t}  -- the logarithmic limiting distribution of E(x;delta,t).
- U_gamma  -- i.i.d. random variables uniform on the unit circle T.
- Phi(R) := (2pi)^{-r/2} integral_R exp(-(1/2)||x||^2) dx  -- standard
  Gaussian measure of R.
- rho(delta; t), rho_s(delta; t)  -- prime-race ordering densities
  (Section 3 / Section 9).
- <eps, gamma> := sum_{j=1}^k eps_j gamma_j  -- alternating inner product
  in the QLI conjecture (Section 10).
- meas(B)  -- Lebesgue measure of Borel B.
- <<  means "= O(.)"; f <> g (rendered) means f asymptotic to constants
  times g both sides; ->  limit; ~  asymptotic.

Everything above COMMENTARY is EXTRACTION (what the paper says). Nothing
evaluative appears before the COMMENTARY section.

---

## 1. FRONT MATTER AND ABSTRACT

Title (p. 1): "Joint distribution of primes in multiple short intervals".
Author (p. 1): "Sun-Kai Leung".

Abstract (p. 1), verbatim:

> "Assuming the Riemann hypothesis (RH) and the linear independence
> conjecture (LI), we show that the weighted count of primes in multiple
> short intervals follows a multivariate Gaussian distribution with weak
> negative correlations. As an application, we obtain short-interval
> analogues of many results in the literature on the Shanks-Renyi prime
> number race, including a sharp phase transition: biased races between
> primes in short intervals emerge once the number of intervals exceeds
> an explicit critical threshold. Our result is new even for a single
> moving interval, particularly under a quantitative formulation of the
> linear independence conjecture (QLI)."

Contents (p. 1): 1. Introduction; Notation and convention; Symbol index;
2. Preliminaries; 3. Main results; 4. Useful lemmas; 5. Proof of
Proposition 2.1; 6. Proof of Proposition 2.2; 7. Proof of Theorem 3.1;
8. Proof of Theorem 3.2; 9. Proof of corollaries; 10. Primes in shorter
intervals; 11. Open questions; Acknowledgements; References.

Governing hypotheses stated once (p. 1-2): the results assume RH and LI;
Section 10 additionally assumes QLI (Conjecture 10.1). LI = "the linear
independence over Q of the positive ordinates of the nontrivial zeros"
(p. 2). The paper explicitly contrasts this with the Montgomery-
Soundararajan route: "Instead of the pair correlation conjecture -- an
analytic assumption -- we adapt the method of Rubinstein and Sarnak
[RS94], assuming the linear independence over Q ... an algebraic
condition." (p. 2).

Window regime, stated in the introduction (p. 2), verbatim:

> "As we shall see, given a large X and x in [2, X], suppose
> h = h(x) = delta*x, where delta > 0 is small but independent of X,
> which is beyond the conjectural range of Montgomery and Soundararajan
> stated above. Then the distribution of psi(x + h) - psi(x) as
> x in [2, X] varies (in logarithmic scale) remains Gaussian under RH and
> LI (see Theorem 3.1 and Theorem 3.2 with r = 1)."

So the base window is a POSITIVE PROPORTION of x: h = delta*x with delta
small but FIXED (independent of X). Section 10 shrinks it, but only to
delta > (log X)^{-eps} (still h > x (log X)^{-eps}); see Section 6 below.

---

## 2. THE COVARIANCE / CORRELATION STRUCTURE (the focus deliverable)

### 2.1 Definitions (Section 2, p. 4-5)

The single-interval normalized deviation (Section 2, p. 4), verbatim:

> "E(x; delta, t) := (1/sqrt(x)) ( psi((1 + t*delta)x + (1/2)delta*x)
>   - psi((1 + t*delta)x - (1/2)delta*x) - delta*x ),
> i.e., the normalized deviation of the weighted prime count in the short
> interval of length delta*x centered at (1 + t*delta)x."

Disjointness convention (p. 4), verbatim: "To simplify our discussion, we
also require that |t_j - t_k| >= 1 whenever j != k, i.e., the intervals
are disjoint."

The Mellin kernel (eq. (2.1), p. 4), verbatim:

> "w(s) = w(s; delta, t) := (1/s) [ (1 + (t + 1/2)delta)^s
>   - (1 + (t - 1/2)delta)^s ]"   (2.1)
> "and write w_j(s) := w(s; delta, t_j) for j = 1, ..., r."

Logarithmic limiting distribution (Definition 2.1, p. 4): E^log_x(f(Y(x)))
:= lim_{X->inf} (1/log X) integral_2^X f(Y(x)) dx/x = lim_{U->inf}
(1/U) integral_1^U f(Y(e^u)) du = integral_{R^r} f(y) dmu(y), for all
bounded continuous f; then mu(B) := P^log_x(Y(x) in B).

### 2.2 Proposition 2.1 -- limiting law and covariance formula (p. 4-5)

Verbatim:

> "Proposition 2.1. Let r >= 1, delta > 0 and t in R^r be fixed. Assume
> RH and LI. Then E(x; delta, t) has a logarithmic limiting distribution
> mu_{delta,t} on R^r. Furthermore, it is an absolutely continuous
> probability measure corresponding to the R^r-valued random vector
> X_{delta,t} = (X_{delta,t_1}, ..., X_{delta,t_r}), where
>   X_{delta,t} := Re( 2 sum_{gamma > 0} w(rho) U_gamma )
> with the sum running over the positive ordinates of the nontrivial
> zeros, and {U_gamma}_{gamma>0} being a sequence of independent random
> variables uniformly distributed on the unit circle T. Moreover, the
> covariance matrix of X_{delta,t} is real symmetric with the (j, k)-entry
> being
>   Cov_jk = Cov_jk(delta, t) := sum_gamma w_j(rho) w_k(rho)."

"To lighten the notation, for j = 1, ..., r, we denote the variance
Cov_jj by V_j." (p. 5)

### 2.3 Proposition 2.2 -- the EXPLICIT covariance shape (p. 5)

This is the covariance structure the steering focus asks for. Verbatim,
with complete hypotheses:

> "Proposition 2.2. Assume RH and LI. Let delta > 0 be sufficiently small
> and T = T_{j,k} <= delta^{-1/2} (log(1/delta))^{-1}. Then
>   Cov_jk = { delta log(1/delta) + (1 - gamma_Q - log 2pi)delta
>                + O( T delta (log(1/delta))^2 )        if j = k,
>            { - Delta(|t_j - t_k|) delta
>                + O( T delta (log(1/delta))^2 )        if j != k,
> where
>   Delta(t) := (1/2)[ (t+1)log(t+1) - 2t log t + (t-1)log(t-1) ]   (2.2)
> i.e., the second order central difference of the function
> f(t) = (1/2) t log t."

Remark 2.2 (p. 5), verbatim: "In particular, if delta > 0 is sufficiently
small, then V_j = Cov_jj <= delta log(1/delta) for j = 1, ..., r."

Structure of the off-diagonal (p. 5), verbatim:

> "Note that Delta(1) = log 2 and Delta(|t_j - t_k|) is always positive.
> Moreover, as |t_j - t_k| -> infinity, we have Delta(|t_j - t_k|) -> 0+
> monotonically. More precisely, we have (see Lemma 4.2)
>   Delta(|t_j - t_k|) = (1 + o(1)) / (2 |t_j - t_k|).
> Thus, primes in disjoint short intervals obey a Coulomb-like law: they
> repel each other, albeit weakly, with an intensity approximately
> inversely proportional to their separation."

Key reading (all-verbatim above): the DIAGONAL variance is
V_j = delta log(1/delta) + (secondary term) -- POSITIVE, of size
~ delta log(1/delta). The OFF-DIAGONAL covariance is
- Delta(|t_j - t_k|) delta -- NEGATIVE, of size ~ delta (a factor
1/log(1/delta) smaller than the diagonal). Hence the correlation
c_jk = Cov_jk / sqrt(V_j V_k) has size ~ - Delta(|t_j - t_k|)/log(1/delta),
i.e. O(1/log(1/delta)) and NEGATIVE. This is the "weak negative
correlation".

Provenance note: Proposition 2.2 display transcribed from the
`pdftotext -layout` layer, cross-checked against the page-2 rendered image
for the twin display in Corollary 1.1; the two agree on the constant
(1 - gamma_Q - log 2pi)delta. The diagonal error term reads
O(T delta (log(1/delta))^2) in the layout layer.

Remark 2.3 (p. 5), PARAPHRASE except quote: two-point correlations are
reducible to variances via the polarization identity xz =
(1/2)[(x+y+z)^2 - (x+y)^2 - (y+z)^2 + y^2] applied to three consecutive
weighted-count differences, "providing a quick explanation for the
repulsion. However, since higher mixed moments cannot be determined from
pure moments, it is unclear a priori whether the weighted prime count in
short intervals follows a multivariate normal distribution." (verbatim,
p. 5). This flags that the Gaussianity (Theorems 3.1/3.2) is a genuine
higher-moment computation, not a consequence of the covariance alone.

Remark 2.4 (p. 5-6): the secondary constant matches Montgomery-
Soundararajan [MS02]: (1/X) integral_1^X (psi(x+H) - psi(x) - H)^2 dx
= H log(X/H) - (gamma_Q + log 2pi + o(1)) H for X^eps <= H <= X^{1/2-eps},
under a uniform Hardy-Littlewood prime k-tuple conjecture (verbatim
display, p. 6).

### 2.4 The bivariate special case (Corollary 1.1, p. 2-3)

Verbatim (front-matter statement; normalization denominator confirmed
from the page-2 rendered image, FLAG 2):

> "Corollary 1.1. Assume RH and LI. Given a Borel subset B subset R^2,
> define
>   S_{X,delta;B} := { x in [2, X] :
>     ( psi(x) - psi(x - delta*x) - delta*x,
>       psi(x + delta*x) - psi(x) - delta*x )
>     / sqrt( ( delta log(1/delta) + (1 - gamma_Q - log 2pi)delta ) x )
>       in B }.
> Then for any delta > 0 sufficiently small, we have
>   lim_{X->inf} (1/log X) integral_{S_{X,delta;B}} dx/x
>     = (1 / (2pi sqrt(det C))) integral_B exp(-(1/2) <C^{-1} x, x>) dx
>       + O( 1 / log^2(1/delta) )
> with the covariance matrix
>   C = [ [ 1 ,               - log 2 / log(1/delta) ],
>         [ - log 2 / log(1/delta) ,               1 ] ]."

Immediately after (p. 3), verbatim: "In particular, primes in two
neighboring intervals are aware of and avoid each other."

Reading: the 2x2 correlation matrix has unit diagonal and off-diagonal
- log 2 / log(1/delta) (using Delta(1) = log 2). Anti-concentration in
form: neighboring counts avoid each other, weakly.

---

## 3. MAIN THEOREMS (Section 3, p. 6-7)

### 3.1 Theorem 3.1 (p. 6), verbatim with complete quantifier order

> "Theorem 3.1. Assume RH and LI. Given a sufficiently small delta > 0 and
> an integer r >= 1 for which r / log(1/delta) is sufficiently small, let
> T = T_{[r]} <= delta^{-1/10} and B subset R^r be a Borel subset. Then
>   P^log_x( Etilde(x; delta, t) in B )
>     = (1 / ((2pi)^{r/2} (det C)^{1/2})) integral_B
>         exp( -(1/2) <C^{-1} x, x> ) dx
>       + O( r^4 T^3 ( 1/sqrt(2pi) + O( log(2r)/log(1/delta) ) )^r
>              ( (1/delta) log(1/delta) )^{-1} meas(B) ),
> where C = (c_jk)_{r x r} is the 'correlation matrix' with entries
>   c_jk = c_jk(delta, t) := Cov_jk / sqrt(V_j V_k),
> i.e., the renormalized deviation of the weighted count of primes in
> multiple short intervals of length delta*x is asymptotically normal with
> mean 0 and covariance matrix C."

(Displays transcribed from the page-6 rendered image; text layer scrambled
the nested O-terms. FLAG 3.)

Follow-up sentence (p. 6), verbatim: "Although the error term here depends
on the Borel set, the estimate can be made uniform over all such sets,
provided that r is small, i.e., there are not too many intervals."

### 3.2 Theorem 3.2 (p. 6-7), verbatim with complete quantifier order

> "Theorem 3.2. Assume RH and LI. Given a sufficiently small delta > 0 and
> an integer 1 <= r <= log(1/delta) / log log(1/delta), let
> T = T_{[r]} <= delta^{-1/10} and B subset R^r be a Borel subset. Then
>   P^log_x( Etilde(x; delta, t) in B )
>     = (1 / ((2pi)^{r/2} (det C)^{1/2})) integral_B
>         exp( -(1/2) <C^{-1} x, x> ) dx
>       + O( (r^4 T^3 / (2pi)^{r/2}) ( (1/delta) log(1/delta) )^{-1}
>              min{ meas(B), ( 20 log(1/delta) )^{r/2} } ).
> In particular, the total variation distance satisfies
>   sup_{B subset R^r : B Borel}
>     | P^log_x( Etilde(x; delta, t) in B ) - P( N(0, C) in B ) |
>       << r^4 T^3 delta ( (10/pi) log(1/delta) )^{r/2 - 1},
> where N(0, C) is an r-dimensional Gaussian random variable with mean 0
> and covariance matrix C."

(Transcribed from page-6/7 rendered images; FLAG 3.)

### 3.3 The number-of-intervals regime (A1 grain, verbatim)

The configuration size r is EXPLICITLY ALLOWED TO GROW, with a stated
ceiling. Collecting the quantifiers:

- Theorem 3.1: r >= 1 with r / log(1/delta) "sufficiently small".
- Theorem 3.2: 1 <= r <= log(1/delta) / log log(1/delta).

The paper states the growth limitation and its source (Section 3, p. 9),
verbatim:

> "Unfortunately, a Berry-Esseen type argument imposes a limitation on the
> number of intervals r not exceeding log(1/delta) / log log(1/delta). By
> employing either Stein's method or the Lindeberg type method (see [HL18]
> and [FHL19] respectively), it is certainly plausible to extend the range
> of r up to a smaller power of delta^{-1}, thus enabling the existence of
> extremely biased r-way prime number races. However, as our primary
> objective is to prove Theorems 3.1 and 3.2, specifically in establishing
> a good upper bound on the total variation distance, we opt for the
> Fourier analytic approach."

So: r grows, but tied to delta (the window parameter), with ceiling
log(1/delta)/loglog(1/delta). Since delta is fixed (base regime) or
> (log X)^{-eps} (Section 10), log(1/delta) is at most O(loglog X), so r
is bounded or grows only at loglog X / logloglog X scale AT MOST, and
only by shrinking delta.

---

## 4. CONSEQUENCES: NEGATIVE CORRELATION AND THE PHASE TRANSITION
   (Section 3, p. 7-9)

Governing sentence (p. 7), verbatim: "As mentioned after Proposition 2.2,
the correlation between primes in two disjoint short intervals is
asymptotically inversely proportional to their separation, and is
negative. Therefore, informally speaking, the weighted prime counts in
multiple short intervals resemble jointly normal point charges."

Corollary 3.1 (p. 7, r and T bounded), the all-same-sign probabilities,
verbatim:

> "P^log_x( E(x;delta,t_1), E(x;delta,t_2), ..., E(x;delta,t_r) > 0 )
>   = 1/2^r - (1/2^{r-2}) . (1 / (2pi log(1/delta)))
>       sum_{1 <= j < k <= r} Delta(|t_j - t_k|)
>     + O_{r,T}( 1 / log^2(1/delta) ),
> and similarly
>   P^log_x( E(x;delta,t_1), ..., E(x;delta,t_r) < 0 )
>   = 1/2^r - (1/2^{r-2}) . (1 / (2pi log(1/delta)))
>       sum_{1 <= j < k <= r} Delta(|t_j - t_k|)
>     + O_{r,T}( 1 / log^2(1/delta) ),
> i.e., it is less likely that the normalized deviations of weighted prime
> counts in short intervals are either all positive or all negative, as
> one might expect."

This is the anti-concentration/non-concentration statement in cleanest
form: the joint-sign probability is pushed BELOW the independent value
1/2^r by an amount proportional to the aggregated pairwise repulsion.

Large-deviation corollary (Corollary 3.2, p. 8): for r, T bounded,
P^log_x( ||Etilde(x;delta,t)|| > V ) = (2pi)^{-r/2} integral_{||x||>V}
exp(-(1/2)||x||^2) dx + O_{r,T}(1/log^2(1/delta)).

The phase transition (Section 3, p. 8-9), extracted verbatim in
fragments:

> "Corollary 3.4. Assume RH and LI. Given a sufficiently small delta > 0
> and an integer 2 <= r <= log(1/delta)/log log(1/delta), if
> T_{[r]} <= delta^{-1/10}, then
>   rho(delta; t) = (1/r!)( 1 + O( r log r / log(1/delta) ) ).
> In particular, as delta -> 0+, all r-way prime number races remain
> asymptotically unbiased, as long as r = o( log(1/delta)/log log(1/delta)
> )."

The biased regime (Corollary 3.6, p. 9), verbatim:

> "Corollary 3.6. Assume RH and LI. Given a sufficiently small delta > 0
> and an integer log(1/delta)/log log(1/delta) << r <=
> log(1/delta)/log log(1/delta), there exists an absolute constant
> eta_0 > 0 and t in R^r such that
>   rho(delta; t) <= exp( - eta_0 . r log log(1/delta) / log(1/delta) )
>                     . (1/r!)."

[FLAG 4: the two ends of the printed range for r in Corollary 3.6 both
render as log(1/delta)/loglog(1/delta) in the text layer, i.e. the lower
bound reads "log(1/delta)/loglog(1/delta) << r <=
log(1/delta)/loglog(1/delta)". The intended lower endpoint is almost
certainly a smaller expression -- context (p. 9, the pinned-critical-
threshold discussion) puts the transition at r asymptotic to
log(1/delta)/loglog(1/delta) -- but I transcribe the printed glyphs and do
not reconstruct.]

Corollary 3.5 (p. 8-9) gives an intermediate upper bound on the leading-s
race density rho_s(delta;t) <= exp( o(1) - (2 - eps) .
(log(r/s)/log(1/delta)) sum_{1<=j<k<=s} Delta(|t_j-t_k|) ) . ((r-s)!/r!),
under a separation hypothesis |t_j - t_k| >= log(1/delta) when
max{j,k} > s.

Critical-threshold sharpening (p. 9), verbatim: "In contrast to [HL18,
Theorem 1.2] and [FHL19, Theorem 1.2], where the phase transition lies
within [log q/(log log q)^4, log q], we can pinpoint the critical
threshold in our setting, owing to the transparent correlation structure
(see Lemma 4.2) and refined estimates for the determinant and inverse of
almost identity matrices (see Lemma 8.1)."

---

## 5. SUPPORTING LEMMAS (Section 4, p. 9-10)

Lemma 4.1 (p. 9), verbatim: "Let delta > 0 be sufficiently small. Then for
|x| <= 1 and |y| > 10, we have w(s) = w(x + iy) << 10 . min( y*delta,
1/|s| )." (bound on the Mellin kernel).

Lemma 4.2 (p. 9-10), verbatim: "For t >= 1, we have Delta(t) < 1. Also, as
t -> infinity, we have Delta(t) = (1/2 + o(1)) t^{-1}."

Lemma 4.3 (Riemann-von Mangoldt formula, p. 10), verbatim: "Let T >= 2.
Then N(T) = (T/2pi) log(T/2pi) - T/2pi + O(log T)." [Cited to Dav80, p.98;
this is the only UNCONDITIONAL classical input, background not a result.]

Method note (Section 5 onward, PARAPHRASE): Proposition 2.1 is proved via
the explicit formula (Lemma 5.1, under RH) relating psi to zeta zeros,
then the Rubinstein-Sarnak limiting-distribution machinery under LI
(the paper notes [ANS14, Theorem 4] would also apply). Proposition 2.2
computes the covariance sum_gamma w_j(rho)w_k(rho) against the
Riemann-von Mangoldt density. Theorems 3.1/3.2 are moment/Berry-Esseen
Fourier arguments; the r-ceiling in Theorem 3.2 comes from the
Berry-Esseen step (see the verbatim quote in Section 3.3 above).

---

## 6. SECTION 10 -- SHORTER INTERVALS UNDER QLI (p. 36-41)

Motivation (p. 36), verbatim: "One unfortunate drawback of the
Rubinstein-Sarnak approach is the qualitative nature of the LI hypothesis,
which prevents achieving uniformity of delta in X for x in [X, 2X].
Therefore, to address shorter intervals, i.e., delta = delta(X) -> 0 as
X -> infinity, we shall propose the following conjecture."

Conjecture 10.1 (QLI) (p. 36), verbatim:

> "Conjecture 10.1 (Quantitative linear independence conjecture (QLI)).
> Let k >= 2. Then there exists a constant c_k > k such that for any
> eps in {+/-1}^k, we have
>   #{ gamma in [0, T]^k : 0 < |<eps, gamma>| <= T^{-c_k} }
>     = o_k( N(T)^{k/2} )     (10.1)
> as T -> infinity, where <eps, gamma> := sum_{j=1}^k eps_j gamma_j."

Theorem 10.1 (single moving interval under QLI) (p. 36), verbatim:

> "Theorem 10.1. Assume RH, LI and QLI. Given real numbers U, delta > 0
> for which delta = o(1) but log(1/delta) = o(log U) as U -> infinity. If
> u in [U, 2U] is chosen uniformly at random, then as U -> infinity, we
> have convergence in distribution to a standard Gaussian
>   Etilde(e^u; delta, 0)  -->(d)  N(0, 1),
> where we recall that
>   Etilde(x; delta, 0) = (1 / sqrt( V(delta,0) . x ))
>     ( psi(x + (1/2)delta*x) - psi(x - (1/2)delta*x) - delta*x )
> with V(delta,0) = sum_gamma |w(rho)|^2, i.e., for any fixed real numbers
> alpha < beta, we have
>   lim_{U->inf} (1/U) meas{ x in [U, 2U] : Etilde(e^u; delta, 0)
>     in (alpha, beta] }
>     = (1/sqrt(2pi)) integral_alpha^beta exp(-t^2/2) dt."

Window translation: "log(1/delta) = o(log U)" with "delta = o(1)" means
delta may be as small as (log U)^{-eps} for any eps > 0 (stated at p. 3
and p. 36: "the normality persists as long as delta > (log X)^{-eps} for
any eps > 0"). So even the sharpest (conditional-on-QLI) reach of the
paper is an interval length h = delta*x > x (log X)^{-eps}: still a
near-macroscopic window, vastly longer than any power of log x.

Remark (end of Section 10 / Section 11 setup, p. 41), verbatim:
"Assuming QLI, it is plausible to compute the mixed moments of
Etilde(e^u; delta, t) for r >= 2 and establish a multidimensional analog
of Theorem 10.1. However, we refrain from" [pursuing it here].

Contrast with Montgomery-Soundararajan (p. 41), PARAPHRASE except quote:
the M-S conjecture requires H/log N -> infinity and log H/log N -> 0;
"Our Theorem 10.1, on the other hand," reaches down to
delta > (log X)^{-eps}.

Section 11 (Open questions, p. 41-42), PARAPHRASE: raises how the
transition from natural to logarithmic density occurs, and other open
directions; no new theorem.

---

## 7. UNIFORMITY LEDGER (what is uniform in what)

Fixed vs growing:

- delta > 0: the PRIMARY small parameter. Base results (Prop 2.1/2.2,
  Cor 1.1, Cor 3.1): delta "sufficiently small but INDEPENDENT of X"
  (a fixed positive proportion window h = delta*x). Section 10 (under
  QLI): delta = delta(X) -> 0 but only as slow as delta > (log X)^{-eps}.
  Everything else scales in log(1/delta).
- r (number of intervals): GROWS, but capped. Theorem 3.1 needs
  r/log(1/delta) small; Theorem 3.2 needs r <= log(1/delta)/loglog(1/delta)
  (the Berry-Esseen ceiling). Since log(1/delta) is bounded (base) or
  O(loglog X) (Section 10), r is effectively bounded or grows at most like
  loglog X / logloglog X, and ONLY by shrinking delta. r is coupled to
  the window, not free.
- t = shift vector: |t_j - t_k| >= 1 (disjointness). T = T_{[r]} =
  1 + max|t_j| is constrained: Prop 2.2 needs T <= delta^{-1/2}/log(1/delta);
  Thms 3.1/3.2 need T <= delta^{-1/10}. So the intervals must sit within a
  bounded multiplicative neighborhood of x controlled by delta.
- Ambient limit is X -> infinity via the logarithmic density dx/x over
  x in [2, X] (Definition 2.1); the statements hold for ALL large X (full
  logarithmic density), NOT on a sparse/exceptional scale set.

Thresholds and their dependence:

- Diagonal variance V_j ~ delta log(1/delta) + (1 - gamma_Q - log2pi)delta;
  off-diagonal covariance ~ - Delta(|t_j-t_k|) delta. Correlation
  c_jk ~ - Delta(|t_j-t_k|)/log(1/delta) = O(1/log(1/delta)), negative.
- Error terms in Thms 3.1/3.2 carry explicit r, T, delta dependence
  (r^4 T^3, powers of log(1/delta)); the constant in <<, and the O_{r,T}
  in the corollaries, are absolute up to their named subscripts.
- Delta(t): absolute function; Delta(1)=log2, Delta(t) in (0,1) for t>=1,
  Delta(t) ~ 1/(2t) as t->inf. No hidden parameter dependence.

Constants absolute vs parameter-dependent:

- gamma_Q (Euler-Mascheroni) and log2pi are absolute; they enter the
  secondary variance term.
- c_k in QLI (Conjecture 10.1) is k-dependent (c_k > k), and the o_k(.) is
  k-dependent.
- The critical-threshold constants (eta, eta_0 in Cor 3.5/3.6) are
  absolute per their statements.

Nothing unconditional at the level of the main results: EVERY main
theorem, proposition, and corollary assumes RH and LI (Section 10 adds
QLI). The only unconditional statements are the classical background
lemmas (Lemma 4.3 Riemann-von Mangoldt; the elementary Lemmas 4.1-4.2 on
w and Delta).

---

## 8. WHAT THE PAPER DOES NOT CONTAIN (mandatory NOT-FOUND probes, 4.7)

The mandatory Section-4.7 probes are: unconditional statement; unweighted
counts; growing configuration size; consecutive primes. Plus the standing
4.7 focus items (covariance shape, number of intervals fixed or growing,
weighting) which ARE found and are extracted above.

- "unconditional statement": NOT FOUND in this text (for any prime-side
  result). Every proposition, theorem, and corollary is stated "Assume RH
  and LI" (Section 10 adds QLI). The only unconditional statements are the
  classical background Lemma 4.3 (Riemann-von Mangoldt) and the elementary
  Lemmas 4.1-4.2; there is no unconditional statement about primes in
  short intervals. Confirmed by the abstract ("Assuming the Riemann
  hypothesis (RH) and the linear independence conjecture (LI)") and by the
  hypothesis line of each result.

- "unweighted counts": NOT FOUND in this text for the short-interval
  results. The object throughout the short-interval theorems is the
  WEIGHTED count psi(x+h) - psi(x) = sum log p (von Mangoldt). The
  unweighted pi appears only in the arithmetic-progression race
  background (p. 7: "pi(x; q, a) := #{p <= x : p = a (mod q)}"), never as
  the object of a short-interval theorem. No pi(x+h) - pi(x) statement
  exists.

- "growing configuration size": FOUND. The number of intervals r is
  permitted to grow. Theorem 3.2 (p. 6), verbatim: "an integer
  1 <= r <= log(1/delta)/log log(1/delta)". The Berry-Esseen ceiling and
  the aspiration to push further are stated (p. 9): "a Berry-Esseen type
  argument imposes a limitation on the number of intervals r not exceeding
  log(1/delta)/log log(1/delta) ... it is certainly plausible to extend
  the range of r up to a smaller power of delta^{-1}". So r grows, but
  tied to the window parameter delta and capped, not a free tuple rank.

- "consecutive primes": NOT FOUND in this text. The paper studies weighted
  counts in intervals; it never discusses consecutive primes, gaps between
  consecutive primes, or gap words. "gap word" / "consecutive-gap":
  NOT FOUND in this text. The word "consecutive" appears only in
  "three consecutive intervals" (p. 8, describing adjacent intervals, not
  primes).

Additional targeted negatives relevant to the six axes:

- "class masses" / "N_{P,d}" / gap-word grain: NOT FOUND in this text. The
  grain is a weighted PRIME COUNT per interval, not a mass of
  consecutive-gap words.
- "singular series" at growing rank: NOT FOUND as an object here; the
  Hardy-Littlewood k-tuple conjecture is cited only as the (rival) input
  used by Montgomery-Soundararajan (p. 2, p. 6), not assumed or used by
  this paper.
- "sparse scale" / "exceptional set of x" / "almost all x": NOT FOUND; the
  results hold on the FULL logarithmic density for all large X, so no
  sparse-scale mechanism exists here.
- "upper bound on class masses" / one-sided middle-slot bound: NOT FOUND
  as such; the paper's non-concentration content is the joint-sign
  probability push (Cor 3.1) and the total-variation bound (Thm 3.2), both
  about weighted counts, not word masses.

---

## COMMENTARY (assessment, NOT extraction)

Consuming context (quoted verbatim from the dispatch):

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

C1. What this paper supplies (conditionally). Under RH + LI, a complete
distributional theory of the WEIGHTED prime count psi(x+h)-psi(x) in
r disjoint short intervals of length h = delta*x, x in [2,X], on the
logarithmic density: a multivariate Gaussian limit (Thms 3.1/3.2) with an
explicit covariance (Prop 2.2). The diagonal variance is
~ delta log(1/delta); the off-diagonal covariance is - Delta(|t_j-t_k|)delta,
so the correlation is ~ - Delta(|t_j-t_k|)/log(1/delta), NEGATIVE and of
size O(1/log(1/delta)) (Delta(1)=log2; Delta(t)~1/(2t)). The "weak
negative correlation" is a genuine anti-concentration statement in form:
Corollary 3.1 shows the joint all-same-sign probability sits strictly
below the independent 1/2^r by an amount proportional to the aggregated
pairwise repulsion sum Delta(|t_j-t_k|). This is the closest object in
this paper to the project's A4 direction.

C2. Why it is not the carrier the project needs -- the window (A2). The
project's window is h ~ (ln x)(lnln x), i.e. delta = h/x ~
(ln x)(lnln x)/x -> 0 astronomically fast (delta far below any negative
power of log x). This paper's base results FIX delta bounded away from 0
(h a positive proportion of x). Even the sharpest conditional extension
(Theorem 10.1, under the additional QLI) reaches only delta > (log X)^{-eps},
i.e. h > x(log X)^{-eps} -- still a near-macroscopic window, incomparably
longer than (log x)(loglog x). The paper's covariance shape delta log(1/delta)
is meaningless at the project's delta, where log(1/delta) ~ log x and the
whole calibration (T <= delta^{-1/10}, the O(1/log(1/delta)) corrections)
degenerates. A2 fails hard.

C3. The grain (A3). This paper's grain is a weighted PRIME COUNT per
interval (psi differences, von Mangoldt weight), not a class mass N_{P,d}
of consecutive-gap words. There is no gap-word, tuple-type, or
class-normalised quantity anywhere (Section 8 NOT-FOUND). A3 fails.

C4. The rank (A1). The configuration size r does grow (up to
log(1/delta)/loglog(1/delta)), which is structurally the rank analogue and
is exactly the "whole question" the focus asks. But this ceiling is TIED
to the window parameter delta and, at the project's delta ~ x^{-1}(...),
is not a free rank at the (2/ln2)lnln x scale with the matching window;
it is a count of macroscopic intervals. The growth exists but in the wrong
coupling and the wrong regime, so as a match to A1 (rank ~ (2/ln2)lnln x
AT window h ~ (ln x)(lnln x)) it fails.

C5. Direction, strength, density (A4, A5, A6). A4: the paper genuinely
supplies a non-concentration/anti-concentration statement (negative
correlation; joint-sign suppression) -- in FORM this is the right
direction, though the object is prime counts not word masses. A5: strength
is not the obstruction -- the paper delivers a sharp Gaussian with an
explicit O(1/log(1/delta)) correlation and a total-variation bound; constant
order certainly suffices and is exceeded. A6: the density axis is the ONE
place the paper is stronger than needed -- it holds on the FULL logarithmic
density for all large X, not merely on a sparse scale sequence, so the
sparse-scale / no-s-uniformity relaxation is not even required. But A5 and
A6 are precisely the axes CG relaxes, so clearing them is not decisive; the
binding axes A1-A4 are the ones that fail (A2, A3 hard; A1 by regime;
A4 only in form, wrong object).

C6. Conditionality is the top-level disqualifier. The project needs an
UNCONDITIONAL statement. Every main result here assumes RH and LI (and QLI
in Section 10). There is no unconditional prime-side statement at all
(Section 8). So even setting aside the axis mismatches, this paper cannot
be a located unconditional carrier.

C7. What it is worth to the references entry. This is the cleanest located
statement that, CONDITIONALLY (RH+LI), the weighted prime counts in
multiple short intervals are jointly Gaussian with an explicit weakly
NEGATIVE correlation -log2/log(1/delta) (neighboring) and more generally
-Delta(|t_j-t_k|)/log(1/delta); the number of intervals is permitted to
grow up to log(1/delta)/loglog(1/delta). It documents that the
anti-concentration direction (A4) is realizable for prime-count grain at
macroscopic-to-mildly-shrinking windows under a strong hypothesis -- a
useful negative datum on the A2/A3 axes and a positive-in-form datum on A4.

Per-axis verdict:

- A1 (rank ~ (2/ln2)lnln x): FAILS (the growing parameter is the count of
  disjoint macroscopic intervals, capped at log(1/delta)/loglog(1/delta)
  and coupled to the window parameter, not a tuple rank at lnln x scale
  with the matching short window).
- A2 (window h ~ (ln x)(lnln x)): FAILS (window is h = delta*x with delta
  fixed, or > (log X)^{-eps} under QLI; incomparably longer than the
  target).
- A3 (grain = class masses of consecutive-gap words): FAILS (grain is a
  weighted prime count psi(x+h)-psi(x), not word masses).
- A4 (direction upper / non-concentration): CLEARS in form (explicit weak
  negative correlation and joint-sign suppression = anti-concentration),
  with the caveat that the object is prime counts, not middle-slot word
  mass.
- A5 (constant-order strength suffices): CLEARS (sharp Gaussian with
  explicit O(1/log(1/delta)) correlation and total-variation bound; more
  than constant order is delivered).
- A6 (sparse scales, no s-uniformity): CLEARS (holds on the full
  logarithmic density for all large X; sparse-scale relaxation not needed).

Even-Cramer-smooth deterministic gap system (q_1=2, q_2=3, q_3=5, q_4=7,
q_{n+1}=q_n+2*ceil(ln q_n / 2)): UNTESTED. The paper never considers any
deterministic gap model; its negative correlation is derived from the
zeta-zero structure under LI and is silent on such a system. Whether the
Gaussian-with-negative-correlation conclusion would fail in the
even-Cramer-smooth model is not addressed here, and I do not guess.

Overall: does NOT clear all six axes (A1, A2, A3 fail; and every main
result is conditional on RH+LI). Not a located unconditional carrier.

---

## FLAGS (consolidated)

1. [PRINTED-ODDITY] The Euler-Mascheroni constant is printed as gamma with
   a blackboard-bold Q subscript ("gamma_Q"; notation list p. 3 defines it
   as the Euler-Mascheroni constant). The subscript appears to disambiguate
   from the bare gamma used for zeta-zero ordinates (rho = 1/2 + i*gamma).
   Rendered "gamma_Q" throughout. Remark 10.2 (p. 36) drops the "log" and
   prints "(1 - gamma - 2pi)delta" where "(1 - gamma_Q - log 2pi)delta" is
   meant (consistent with Cor 1.1 and Prop 2.2); transcribed as the
   evident typo, not corrected in the extract body.

2. [TRANSCRIPTION-UNSURE, resolved-by-image] The normalization denominator
   in Corollary 1.1, sqrt( (delta log(1/delta) + (1 - gamma_Q - log2pi)
   delta) x ), and the explicit 2x2 correlation matrix C = [[1,
   -log2/log(1/delta)],[-log2/log(1/delta),1]], were scrambled in the
   text layer and read from the page-2 rendered image (p2-02.png at
   r=200).

3. [TRANSCRIPTION-UNSURE, resolved-by-image] The nested O-terms in the
   error bounds of Theorem 3.1 (the (1/sqrt(2pi) + O(log2r/log(1/delta)))^r
   factor and the ((1/delta)log(1/delta))^{-1} meas(B) factor), the
   Theorem 3.2 error term (r^4 T^3/(2pi)^{r/2} ... min{meas(B),
   (20 log(1/delta))^{r/2}}), and the total-variation bound
   r^4 T^3 delta ((10/pi)log(1/delta))^{r/2-1}, were read from the
   page-6 and page-7 rendered images (leungp-06.png, leungp-07.png). The
   text layer scrambled the fraction/exponent nesting.

4. [TRANSCRIPTION-UNSURE] In Corollary 3.6 (p. 9) both endpoints of the
   printed range for r render identically as
   log(1/delta)/loglog(1/delta), giving the vacuous-looking
   "log(1/delta)/loglog(1/delta) << r <= log(1/delta)/loglog(1/delta)".
   The lower endpoint is presumably a smaller expression (the surrounding
   text describes the transition AT r ~ log(1/delta)/loglog(1/delta)), but
   I transcribe the printed glyphs and do not reconstruct the intended
   lower bound.

5. [PRINTED-ODDITY] The paper uses r/log(1/delta) "sufficiently small" as
   a qualitative hypothesis in Theorem 3.1 (no explicit constant), while
   Theorem 3.2 gives the explicit ceiling r <= log(1/delta)/loglog(1/delta);
   transcribed as printed.

6. [PRINTED-ODDITY] Remark 2.1 (p. 4) prints a multiplicative-interval
   endpoint "[exp((t-1/2)delta)x, exp(t+1/2)delta)x]" with an unbalanced
   bracket/paren (an "exp(t+1/2)delta)x" where "exp((t+1/2)delta)x" is
   meant); transcribed structure noted, not corrected.
