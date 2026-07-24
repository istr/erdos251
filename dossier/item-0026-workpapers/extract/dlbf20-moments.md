# EXTRACTION: R. de la Breteche and D. Fiorilli, "On a conjecture of Montgomery and Soundararajan"

Source (only evidence base): /home/istr/pro/erdos251/dossier/2009.05760v1.pdf
arXiv:2009.05760v1 [math.NT]. The arXiv side-stamp on p. 1 reads "12 Sep
2020"; the paper's own footer reads "Date: September 15, 2020." (p. 1);
PDF CreationDate is 15 Sep 2020. See flag 1. Authors: R. de la Breteche
and D. Fiorilli. Affiliations (p. 15): de la Breteche -- Institut de
Mathematiques de Jussieu-Paris Rive Gauche, Universite de Paris, Sorbonne
Universite, CNRS UMR 7586, Case Postale 7012, F-75251 Paris CEDEX 13,
France (regis.delabreteche@imj-prg.fr); Fiorilli -- CNRS, Universite
Paris-Saclay, Laboratoire de mathematiques d'Orsay, 91405, Orsay, France
(daniel.fiorilli@universite-paris-saclay.fr). Page count: 15 (PDF page =
printed page throughout). No journal reference is printed on the paper (it
is a preprint). No grant footnote is printed.

Steering identification CONFIRMED against front matter: author and title
match "de la Breteche-Fiorilli, On a conjecture of Montgomery and
Soundararajan" exactly (accents transliterated).

---

## Transcription conventions

ASCII only. Diacritics transliterated (de la Breteche, Ozluk, Radziwill,
Erdos, Mobius, Teravainen). Mathematics in LaTeX-like ASCII. Anchors are
the paper's own numbering (Conjecture 1.1, Theorem 1.2, Corollaries
1.3/1.4, Remark 1.1, Lemmas 2.1/2.2/2.3, Proposition 3.1, equations
(1.1)-(2.12)); page numbers (printed = PDF page) are a secondary aid.

Symbol table (every non-obvious glyph):

- `psi(x)` = Chebyshev's function sum_{n<=x} Lambda(n); `Lambda(n)` = von
  Mangoldt function.
- `delta` = the relative interval length (Greek delta); the short interval
  is [x, x + delta*x] (or [x, x+delta*X] in Conjecture 1.1). `X`, `x` are
  the scale variables as printed (the paper uses both; Mn is stated in X,
  the pointwise/Omega statements in x).
- `eta` = a test function (Greek eta); `etahat` = its Fourier transform
  (paper writes eta with a wide hat). `eta'` = derivative.
- `kappa` = Greek kappa (decay-rate parameter); `calE_kappa` = the class
  of admissible test functions eta (paper's script E_kappa, subset of
  L^1(R)); `calU` = the set of admissible Phi (paper's script U).
- `Phi` = an averaging weight; `Phihat` = its Fourier transform.
- `mu_n` = the n-th moment of the standard Gaussian, (1.1); `mu_{2m}` =
  (2m)!/(2^m m!).
- `alpha(h)`, `beta(h)` = the two functionals (1.5).
- `rho` = beta + i*gamma = a non-trivial zero of the Riemann zeta function
  zeta(s); `gamma` = its imaginary part; `beta` = its real part (in the
  zeros context only). `N(T)` = zero-counting function (2.1).
- `calL_eta(delta/2)` = the main-term functional (paper's script L_eta);
  see the display defining it on p. 2.
- `Mn(X, delta; eta, Phi)` = the weighted n-th moment (defined p. 2).
- `Omega`, `Omega_{+-}` = Omega / Omega-plus-minus (the standard
  large-oscillation notation).
- `log_2 x` = log log x; `log_3 x` = log log log x (iterated logs, paper's
  subscript notation).
- `<=`,`>=` for the paper's slanted <=, >= ; `<<` for Vinogradov's ll;
  `~` for asymptotic; `subset` for containment; `in` for membership.
- `RH` = Riemann Hypothesis; `GRH` = Generalized RH; `HL` = Hardy-
  Littlewood.

Everything up to the COMMENTARY section is EXTRACTION (what the paper
says). Nothing evaluative appears before COMMENTARY.

---

## 1. FRONT MATTER AND ABSTRACT

Title (p. 1): "ON A CONJECTURE OF MONTGOMERY AND SOUNDARARAJAN".
Authors (p. 1): "R. DE LA BRETECHE AND D. FIORILLI".

Abstract (p. 1), verbatim:

> "We establish lower bounds for all weighted even moments of primes up to
> X in intervals which are in agreement with a conjecture of Montgomery
> and Soundararajan. Our bounds hold unconditionally for an unbounded set
> of values of X, and hold for all X under the Riemann Hypothesis. We also
> deduce new unconditional Omega-results for the classical prime counting
> function."

[The abstract already fixes the A6 signature: "unconditionally for an
unbounded set of values of X ... and hold for all X under the Riemann
Hypothesis." Extraction only; assessment deferred to COMMENTARY.]

---

## 2. SECTION 1 (Introduction): the conjecture and the objects

### 2.1 The Montgomery-Soundararajan conjecture

Gaussian moments (1.1), p. 1, verbatim:

> "mu_n := { (2m)!/(2^m m!)  if n = 2m for some m in N,
>          { 0              otherwise      (1.1)
> be the n-th moment of the Gaussian."

Conjecture 1.1 (Montgomery, Soundararajan), p. 1, verbatim (from image;
text layer scrambles superscripts):

> "Conjecture 1.1 (Montgomery, Soundararajan). Fix eps > 0. For each fixed
> n in N and uniformly for (log X)^{1+eps}/X <= delta <= 1/X^{eps},
>   (1/X) integral_1^X (psi(x + delta X) - psi(x) - delta X)^n / X^{n/2} dx
>       = (mu_n + o(1)) ( delta log(delta^{-1}) )^{n/2}.   (1.2)"

Surrounding sentence, p. 1, verbatim:

> "In the range X^{-1}(log X)^{1+eps} <= delta <= X^{-1+1/n}, Montgomery
> and Soundararajan [26, Theorem 3] have shown that (1.2) follows from a
> strong form of the Hardy-Littlewood prime k-tuple conjecture. They also
> mention that the conjecture could also hold whenever delta = o(1). For
> applications on the distribution of gaps between primes, see for
> instance [4]."

The paper's own contribution is announced (p. 1), verbatim:

> "In the current paper, we establish lower bounds for a weighted version
> of (1.2) for all even n, for values of delta that are relatively close
> to 1. In addition to being the first estimate on higher moments, we
> believe that our bounds are sharp up to a power-saving error term in
> delta (c.f. [26, Theorem 3])."

Method idea, p. 2, verbatim:

> "The key idea which will allow us to circumvent the need to understand
> spacing statistics and Diophantine properties (for higher moments) of
> zeros of the zeta function is a positivity argument in the explicit
> formula. Such an argument in conjunction with Parseval's identity has
> been successfully used in previous works on the variance (see e.g. [9]),
> however the novelty in the present paper is to avoid the need for
> Parseval's identity (in particular for higher moments)."

### 2.2 The test-function classes and the weighted count (the moments)

Class of test functions, p. 2, verbatim:

> "For any fixed kappa > 0, we define the class of test functions
> calE_kappa subset L^1(R) to be the set of all differentiable[fn1] even
> eta : R -> R such that for all t in R,
>   eta(t), eta'(t) << e^{-kappa|t|},      (1.3)
> moreover etahat(0) > 0 and for all xi in R we have that[fn2]
>   0 <= etahat(xi) << (|xi| + 1)^{-1} log(|xi| + 2)^{-2-kappa}.  (1.4)"

[fn1 (p. 2): "One can replace differentiability by a Lipschitz condition
if for instance eta is compactly supported in R and monotonous on R>=0."
fn2 (p. 2): "We can take for example eta = eta_0 star eta_0 for some
smooth and rapidly decaying eta_0."]

The weighted count (definition of the object being moment-averaged),
p. 2, verbatim:

> "We consider the following weighted version of x^{-1/2}(psi(x + delta x)
> - psi(x) - delta x). For eta in calE_kappa and delta < 2kappa, we define
>   psi_eta(x, delta) := sum_{n>=1} Lambda(n)/n^{1/2} * eta( delta^{-1}
>       log(n/x) )."

Main-term functional (p. 2), verbatim:

> "The expected main term for psi_eta(x, delta) is given by
>   integral_0^infty eta(delta^{-1} log(t/x)) / t^{1/2} dt
>       = x^{1/2} delta integral_R e^{delta w / 2} eta(w) dw,
> which we will denote by x^{1/2} delta calL_eta(delta/2) (note that for
> delta < kappa, calL_eta(delta/2) = calL_eta(-delta/2) = etahat(0) +
> O(delta))."

The set calU and the functionals alpha, beta (p. 2), verbatim:

> "We also consider the set calU of non-trivial even integrable functions
> Phi : R -> R such that Phi, Phihat >= 0 (in particular, Phi(0) > 0).
> Finally, for h : R -> R we define
>   alpha(h) := integral_R h(t) dt;   beta(h) := integral_R h(t)(log|t|)
>       dt,    (1.5)
> whenever these integrals converge."

The moment (p. 2), verbatim -- THIS IS THE PRECISE DEFINITION OF THE
MOMENTS (weight = Phi(log x / log X); normalization = x^{1/2} delta *
main-term subtracted, then n-th power, then log-averaged over x; moment
order = n):

> "Mn(X, delta; eta, Phi) := 1/((log X) integral_0^infty Phi) *
>   integral_1^infty Phi( log x / log X ) ( psi_eta(x, delta) - x^{1/2}
>   delta calL_eta(delta/2) )^n  dx/x."

Which weight: Phi(log x / log X), Phi in calU (even, non-negative Fourier
pair). Which normalisation: the centered/weighted count psi_eta(x,delta) -
x^{1/2} delta calL_eta(delta/2), i.e. Lambda(n)-1 in place of Lambda(n)
(p. 2: "Subtracting this main term is equivalent to summing Lambda(n) - 1
instead of Lambda(n) ... working with the measure d(psi(t) - t)"), with an
n^{-1/2}-weighted count in psi_eta. Which moment order: n; whether fixed or
may grow -- MAY GROW (see 2.3, Theorem 1.2 range and Corollary 1.3).

### 2.3 The main RH result (Theorem 1.2), verbatim with complete
quantifier order

Theorem 1.2 (p. 3), verbatim (transcribed from image; text layer scrambles
exponents), full quantifier order preserved:

> "Theorem 1.2. Assume RH, and let 0 < kappa < 1/2, eta in calE_kappa,
> Phi in calU. For n in N, X in R>=2, delta in (0, kappa), and in the range
>   n <= delta^{-1/2} (log(delta^{-1} + 2))^{1/2},
> we have that
>   (-1)^n Mn(X, delta; eta, Phi) >= mu_n delta^{n/2} ( alpha(etahat^2)
>       log(delta^{-1}) + beta(etahat^2) )^{n/2} ( 1 + O_{kappa,eta}(
>       n^2 delta / log(delta^{-1} + 2) ) )
>       + O_Phi( delta (K_eta log(delta^{-1} + 2))^n / log X ),   (1.6)
> where the implied constants and K_eta > 0 are independent of n, X and
> delta."

Remark 1.1 (p. 3), verbatim in the parts that fix ranges and prior art:

> "Remark 1.1. (1) For n = 2 and in the range X^{-c(eta,Phi)} <= delta <=
> 1, (1.6) implies a lower bound with the predicted main term as well as a
> secondary term conjectured in the work of Montgomery and Soundararajan
> [25, (2)]. Here, c(eta, Phi) > 0 is a constant."

> "(2) For n = 2m with m >= 2 and in the interval (log X)^{-1/(m-1)+o(1)}
> <= delta << 1, we obtain a lower bound which is in agreement with
> Conjecture 1.1."

> "(3) Goldston and Yildirim [14, 15] have computed the first three
> moments of a related quantity involving a major arcs approximation of
> Lambda(n), and deduced that in the range X <= x <= 2X, X^{-1}(log X)^{14}
> << delta <= X^{-6/7-eps} and under GRH, psi(x + delta X) - psi(x) -
> delta X = Omega_{+-}((delta x log x)^{1/2})."

[Remark 1.1(1) also enumerates prior n=2 art: Goldston-Montgomery RH upper
bound [11] in 0 < delta <= 1; Saffari-Vaughan unconditional upper bound
[34] in x^{-5/6+eps} <= delta <= 1; Goldston GRH lower bound [6,8] in
x^{-1} <= delta <= x^{-3/4} (unconditional for x^{-1} <= delta <=
x^{-1}(log x)^A); Ozluk [29] and Goldston-Yildirim [12,13] to arithmetic
progressions; Zaccagnini unconditional upper bound [38,39] in
x^{-5/6-eps} <= delta <= 1. Remark 1.1(4): function-field variance results
of Keating-Rudnick [22,24], Rodgers [32], and the geometric interpretation
of Hast-Matei [17].]

### 2.4 The unconditional / sparse-scale statement (Corollary 1.3)

Corollary 1.3 (p. 3-4), verbatim -- this is the axis-A6 carrier. The RH
form is stated first, then the exact unconditional clause. Full quantifier
order preserved.

> "Corollary 1.3. Let 0 < kappa < 1/2, eta in calE_kappa, and Phi in calU.
> Let moreover f : R>=0 -> (0, 1/2] be any function such that
> lim_{x->infty} f(x) = 0, and let delta in (0,1), m in N and X in R>=2 be
> such that either m = 1 and delta in (X^{-f(X)}, f(X)], or 2 <= m <=
> min( delta^{-1/2} (log(delta^{-1}+2))^{1/2} f(X)^{1/2}, log log X ) and
> delta in ( (log X)^{-1/(m-1)} (log log X)^4, f(X) ]. Then under RH we
> have that
>   M_{2m}(X, delta; eta, Phi) >= mu_{2m} delta^m ( alpha(etahat^2)
>       log(delta^{-1}) + beta(etahat^2) )^m ( 1 + O( f(X) +
>       1/(log(delta^{-1}))^2 ) ).    (1.7)"

The unconditional clause (p. 4), verbatim -- THE EXACT PHRASE
ESTABLISHING UNCONDITIONALITY ON AN UNBOUNDED SCALE SET, with its
surrounding sentence:

> "Unconditionally, there exists a sequence {X_j}_{j>=1} tending to
> infinity such that whenever X = X_j, (1.7) holds with m = 1 and delta in
> (X^{-f(X)}, f(X)]. The same statement holds in the range 2 <= m <=
> min(delta^{-1/2}, log log X) and delta in ( (log X)^{-1/(m-1)} (log log
> X)^4, f(X) ]."

Note the quantifier structure: the sequence {X_j} is chosen FIRST (does
not depend on delta or on which m); then FOR EACH X_j the bound (1.7)
holds for m = 1 uniformly over delta in (X^{-f(X)}, f(X)] (and for the
stated range of m >= 2). What is additionally true under RH: the SAME
lower bound (1.7) holds for ALL X in R>=2 (not merely on {X_j}), for the
larger m-range up to min(delta^{-1/2}(log(delta^{-1}+2))^{1/2} f(X)^{1/2},
log log X). So RH upgrades "some unbounded sequence {X_j}" to "all X", and
widens the admissible moment order.

### 2.5 The unconditional Omega-results for the classical prime count
(Corollary 1.4)

Framing sentence (p. 4), verbatim:

> "We now state our unconditional Omega-results for the usual prime
> counting function in short intervals psi(x + delta x) - psi(x) - delta x.
> Note that this quantity has standard deviation of order (delta x
> log(delta^{-1}+2))^{1/2}. We will show that psi(x+delta x) - psi(x) -
> delta x can be larger than an unbounded constant times this."

Corollary 1.4 (p. 4), verbatim (from image; the delta_j range and the two
Omega-lower-bounds), full quantifier order:

> "Corollary 1.4. Let eps > 0 be small enough. There exists a sequence
> {(x_j, delta_j)}_{j>=1} with
>   delta_j in [ eps (log_3 x_j)^{9/2} / ( (log x_j)^2 (log_2 x_j)^{5/2} ),
>       2 (log_3 x_j)^3 / (log_2 x_j)^2 ],
> lim_{j->infty} x_j = infinity, and such that
>   | psi(x_j + delta_j x_j) - psi(x_j) - delta_j x_j |
>       >> delta_j^{-1/4} (log(delta_j^{-1} + 2))^{1/4} * ( delta_j x_j
>       log(delta_j^{-1} + 2) )^{1/2}.
> If instead we require that delta_j in [ (log x_j)^{-7/2 - 3/(2M)},
> (log x_j)^{-1/(M+1)} ] for some large fixed M in Z>=2, then we can
> choose the sequence {(x_j, delta_j)}_{j>=1} in such a way that
>   | psi(x_j + delta_j x_j) - psi(x_j) - delta_j x_j |
>       >> M^{1/2} * ( delta_j x_j log(delta_j^{-1} + 2) )^{1/2}."

Here log_2 = log log, log_3 = log log log (paper's subscript convention).
The first Omega-result exceeds the standard deviation by the UNBOUNDED
factor delta_j^{-1/4}(log(delta_j^{-1}+2))^{1/4}; the second by the
arbitrarily-large FIXED factor M^{1/2}.

---

## 3. SECTION 2 (proof of Theorem 1.2): the analytic inputs

PARAPHRASE except quotes. The proof is via an explicit formula over zeros
of zeta plus a positivity/combinatorial extraction, not a sieve or a
tuple count. The three lemmas:

Zero-counting (2.1), p. 4, verbatim:

> "N(T) := #{rho : 0 <= Im(rho) <= T} = (T/2pi) log(T/(2pi e)) +
> O(log(T + 2)),   (2.1) which is valid for T >= 0."

Lemma 2.1 (explicit formula), p. 4-5, verbatim (heads of (2.2) and the
uniform RH bound (2.5)):

> "Lemma 2.1. Let 0 < kappa < 1/2 and eta in calE_kappa. For t >= 0 and
> 0 < delta < kappa we have the formulas
>   psi_eta(e^t, delta) - e^{t/2} delta calL_eta(delta/2) = -delta sum_rho
>       e^{(rho - 1/2)t} etahat( (delta/2pi)(rho - 1/2)/i ) + O_{kappa,eta}
>       (E_{kappa,eta}(t, delta));   (2.2)"

with the error function (2.4), p. 4, verbatim:

> "E_{kappa,eta}(t, delta) := { delta e^{-t/2} + log(delta^{-1}+2)
>       e^{-kappa t / delta}   if t >= 1,
>   { delta/t + log(delta^{-1}+2) e^{-kappa t/delta}   if delta <= t < 1,
>   { log(delta^{-1}+2)                                 if 0 <= t <= delta.
>   (2.4)"

and the uniform RH bound (2.5), p. 5, verbatim:

> "Under RH we have the uniform bound
>   psi_eta(e^t, delta) - e^{t/2} delta calL_eta(delta/2) <<_{kappa,eta}
>       log(delta^{-1} + 2).   (2.5)"

Lemma 2.2 (convergent sum over zeros -> main-term constants), p. 6,
verbatim (the statement; proof shows the constant C = 0):

> "Lemma 2.2. Let 0 < kappa < 1/2, and let h : R -> R be a measurable
> function such that for all xi in R, 0 <= h(xi) << (|xi| +
> 1)^{-2}(log(|xi| + 2))^{-2-kappa}, and for all t in R, hhat(t), hhat'(t)
> << e^{-kappa|t|}. For 0 < delta < 2kappa we have that
>   sum_rho h( (delta/2pi)(rho - 1/2)/i ) = alpha(h) delta^{-1}
>       log(delta^{-1}) + beta(h) delta^{-1} + O_{kappa,h}(1),   (2.8)
> where rho is running over the non-trivial zeros of the Riemann zeta
> function ..."

Lemma 2.3 (combinatorial lower bound), p. 7, verbatim:

> "Lemma 2.3. Let 0 < kappa < 1/2, eta in calE_kappa, and assume[fn4] RH.
> For delta in (0, kappa), m in N, and in the range m <= delta^{-1/2}
> (log(delta^{-1} + 2))^{1/2}, we have the lower bound
>   delta^{2m} sum_{gamma_1,...,gamma_{2m}, gamma_1+...+gamma_{2m}=0}
>       etahat(delta gamma_1/2pi) ... etahat(delta gamma_{2m}/2pi)
>   >= mu_{2m} delta^m ( alpha(etahat^2) log(delta^{-1}) + beta(etahat^2)
>       )^m ( 1 + O_{kappa,eta}( m^2 delta / log(delta^{-1} + 2) ) ),
> where the gamma_j are running over the imaginary parts of the non-trivial
> zeros of the Riemann zeta function."

[fn4 (p. 7), verbatim: "One can obtain a slightly weaker but unconditional
lower bound by applying (2.10) at the end of the argument."]

The combinatorial core (2.12), p. 7, verbatim (the involution count that
produces mu_{2m}):

> "M_{2m} := sum_{gamma_1,...,gamma_{2m}, gamma_1+...+gamma_{2m}=0}
>   etahat(delta gamma_1/2pi) ... etahat(delta gamma_{2m}/2pi) >= mu_{2m}
>   s_2^m - m(m-1) s_2^{m-2} s_4,   (2.12)
> where s_{2j} := sum_gamma |etahat(delta gamma / 2pi)|^{2j}."

PARAPHRASE: (p. 7) mu_{2m} arises as "the total number of ... involutions
pi : {1,...,2m} -> {1,...,2m} with no fixed points"; the diagonal
gamma_j = -gamma_{pi(j)} is forced by positivity of etahat and Phihat when
one keeps only the terms with gamma_1 + ... + gamma_n = 0 (p. 9). Odd n:
"the claimed estimate follows from discarding the sum over zeros entirely"
(p. 9). Even n: "by positivity of etahat and Phihat we may only keep the
terms for which gamma_1 + ... + gamma_n = 0, and apply Lemma 2.3" (p. 9).

---

## 4. SECTION 3 (proof of Corollaries 1.3 and 1.4): THE UNBOUNDED-SCALE
MECHANISM (highest-value anatomy)

PARAPHRASE except quotes. This is the axis-A6 machinery. Where does the
sparse scale sequence {X_j} / {(x_j, delta_j)} come from? Answer: a
Riemann-Hypothesis DICHOTOMY, "strongly inspired from the work of
Kaczorowski and Pintz [20]" (p. 9). It is NOT a pigeonhole over a
divergent sum, NOT a zero-density input, and NOT a moment being a lower
bound per se; it is an oscillation (Omega) transfer driven by a single
hypothetical zero off the critical line.

The dichotomy, in the authors' own frame (proof of Corollary 1.3, p. 11),
verbatim:

> "Proof of Corollary 1.3. If RH is true, then this is a particular case
> of Theorem 1.2. Let us then assume that RH is false. ... The claimed
> Omega-result then follows from Proposition 3.1."

So: on the "RH true" branch the statement holds for ALL X (Theorem 1.2);
on the "RH false" branch a hypothetical zero produces an unbounded
sequence of scales where the count oscillates. The union of the two
branches is unconditional but only on an unbounded SET of X (one cannot
name which branch holds, hence one cannot make the set all X, nor make it
effective).

The governing lemma (Proposition 3.1), p. 9, verbatim -- the object
studied and the existence of the sparse sequence:

> "We first need to establish the following proposition, which is strongly
> inspired from the work of Kaczorowski and Pintz [20]. We consider
>   F(x, delta; eta) := -delta sum_rho x^{rho - 1/2}/(rho - 1/2) *
>       etahat( (delta/2pi)(rho - 1/2)/i ),
> which is readily shown to be real-valued by grouping conjugate zeros."

> "Proposition 3.1. Assume that RH is false, and let eta in calE_kappa
> with 0 < kappa < 1/2. Then, there exists an absolute (ineffective)
> constant theta > 0 and a sequence {x_j}_{j>=1} tending to infinity such
> that for each j >= 1 and uniformly for x_j^{-theta} <= delta <=
> delta_eta, where delta_eta > 0 is small enough, we have that
>   F(x_j, delta; eta) > x_j^{theta}."

Anatomy of the Proposition 3.1 proof (p. 9-11), PARAPHRASE with quotes:

- Take "a zero rho_e = beta_e + i gamma_e of zeta(s) violating RH, of
  least positive imaginary part gamma_e, and such that there is no other
  zero of imaginary part equal to gamma_e but of greater real part"
  (p. 9). This single off-line zero drives everything.
- Introduce an (n-1)-fold antiderivative F_n(e^t, delta, Theta; eta) whose
  (n-1)-th derivative is F(e^t, delta; eta) - delta e^{Theta t} (p. 9).
  Sample t = c*n with c in a bounded window (c_0(eps), c_1(eps)), truncate
  the zero-sum at height U_eps, and show "F_n(e^t, delta, Theta; eta) = 0
  for many values of t (independently of delta), and then apply Rolle's
  theorem" (p. 9).
- A measure argument on the linear separating functions of pairs of zeros
  produces a subset S subset (c_0(eps), c_1(eps)) "of measure >= 1 which
  is a disjoint union of at most 2#{rho : zeta(rho)=0, 0<Im(rho)<=U_eps} +
  1 intervals" on which one zero rho_j dominates (p. 10). The dominant
  term is real-oscillatory: Re( e^{cn(rho_j - 1/2)}/(rho_j - 1/2)^n ) =
  ( e^{cn(beta_j - 1/2)} / |rho_j - 1/2|^n ) cos(nu_{j,c} n) (p. 11),
  giving at least 4 n lambda(S) >= 4 n zeros of F_n on [c_0 n, c_1 n].
- Rolle: "F(e^t, delta; eta) - delta e^{Theta t} has at least 3n zeros on
  this interval ... In the range e^{-theta t} <= delta, the result follows
  whenever 0 < theta < Theta/2." (p. 11).

Is the set effective? NO. Proposition 3.1 states theta is an "absolute
(ineffective) constant" (p. 9). The sequence {x_j} is a pure existence
statement contingent on the (hypothetical) off-line zero rho_e; the
authors never assert an effective location of any X_j. On the RH-true
branch the statement is for all X (no sequence needed). Hence the
UNBOUNDED-SET-OF-X clause is genuinely non-constructive: it is the OR of
"all X (if RH)" and "some ineffective unbounded {x_j} (if not RH)".

Does the mechanism depend on the moment being a LOWER bound? Only
indirectly. Proposition 3.1 is an Omega (oscillation) statement about the
signed quantity F(x, delta; eta); via Holder's inequality (p. 11) a large
|F| forces a large even moment M_{2m} from below:

> "By Holder's inequality we have that M_{2m}(X, delta; eta, Phi) >= ...
>   >= (c(Phi)/(log X) integral_0^infty Phi) integral_1^{X^{kappa(Phi)}} |
>       psi_eta(x, delta) - x^{1/2} delta calL_eta(delta/2) | dx/x, where
>   c(Phi), kappa(Phi) > 0." (p. 11)

So the moment lower bound is DERIVED FROM the oscillation bound; the
sparse-scale mechanism itself is an Omega-result mechanism (zeros of the
zeta function), and the "lower bound on moments" is a downstream
consequence of it via Holder, not its source.

Corollary 1.4's RH-true branch (p. 11-13), PARAPHRASE: on the RH-true
branch the authors argue by contradiction -- assume the count is bounded
by eps_0 times the claimed size uniformly on the delta-window, feed this
into (2.6)/Theorem 1.2, and derive a contradiction "as soon as the range
... contains an integer; this is clearly the case when eps_0 is small
enough and X is large enough" (p. 13). The RH-false branch "follows from
an adaptation of the proof of Proposition 3.1" with the weight
(1+delta)^rho - 1 in place of delta*etahat(...) and a one-sided-derivative
generalization of Rolle's theorem (p. 11-12).

---

## 5. UNIFORMITY LEDGER (what is uniform in what)

Fixed (never grows): kappa in (0, 1/2); the test functions eta in
calE_kappa and Phi in calU (chosen once); the functionals alpha(etahat^2),
beta(etahat^2); the absolute constant K_eta > 0 in (1.6) ("independent of
n, X and delta", p. 3); in Proposition 3.1 the ineffective absolute
constant theta > 0 and the threshold delta_eta > 0.

Grows:
- The moment order n (equivalently m, n = 2m). Theorem 1.2 admits
  n <= delta^{-1/2}(log(delta^{-1}+2))^{1/2}. Corollary 1.3 (RH) admits
  2 <= m <= min( delta^{-1/2}(log(delta^{-1}+2))^{1/2} f(X)^{1/2},
  log log X ). Unconditionally the m-range narrows to
  2 <= m <= min(delta^{-1/2}, log log X). So the growing parameter is
  capped at magnitude log log X (= log_2 X) in the unconditional and RH
  Corollary; the cap coincides in ORDER with log log X. This is the
  paper's only "rank-like" growing parameter, and it is a MOMENT ORDER, an
  exponent on a single short-interval prime count, not a tuple rank.
- The scale X (resp. x_j) -> infinity along the sequence.
- delta may shrink (window narrows), but only within the stated windows
  (never below X^{-f(X)} in Corollary 1.3 m=1; never below the (log x)^{-
  power} scales in Corollary 1.4).

Threshold dependencies:
- The main-term shape (1.6)/(1.7) depends on delta through
  alpha(etahat^2) log(delta^{-1}) + beta(etahat^2); the relative error is
  O(n^2 delta / log(delta^{-1}+2)) (Theorem 1.2) or O(f(X) +
  1/(log delta^{-1})^2) (Corollary 1.3).
- The RH branch removes the {X_j} restriction (all X) and enlarges the
  m-range by the factor f(X)^{1/2} inside the min.
- The unbounded sequence {X_j}/{x_j} is chosen BEFORE delta and BEFORE m
  (its existence is uniform over the stated delta-window for each fixed
  X_j); it is ineffective.

Constants absolute vs parameter-dependent: K_eta, theta, delta_eta are
absolute/eta-dependent but independent of (n, X, delta). The Holder
constants c(Phi), kappa(Phi) depend only on Phi. c(eta, Phi) in Remark
1.1(1) depends on (eta, Phi). All implied constants in (1.6) are
"independent of n, X and delta" (p. 3) except the explicitly
eta-/Phi-subscripted ones.

Window translation (absolute length): the short interval is [x, x+delta x]
(Corollaries) or [x, x+delta X] (Conjecture 1.1), i.e. ABSOLUTE window
length = delta * x (resp. delta * X). The admissible delta stays
"relatively close to 1" (p. 1): in Corollary 1.3 (m=1) delta ranges over
(X^{-f(X)}, f(X)], so the window delta*X ranges from X^{1-f(X)} (a near-
full power of X) down to f(X)*X ~ o(X); in Corollary 1.4 delta ~
(log_3 x)^3/(log_2 x)^2 or (log x)^{-1/(M+1)}..(log x)^{-7/2-3/(2M)}, so
delta*x ~ x*(log-power) -- still of order x up to log factors. In no
regime does the ABSOLUTE window fall to the near-logarithmic scale
(ln x)(lnln x): the shortest admissible window is a power (or near-power)
of x.

---

## 6. What the paper does NOT contain (mandatory NOT-FOUND probes)

Probe -- "upper bound" on the SAME moments (the weighted even moments
Mn): NOT FOUND in this text. The paper proves only LOWER bounds on its own
Mn (abstract: "We establish lower bounds for all weighted even moments";
p. 1: "we establish lower bounds for a weighted version of (1.2)"). The
string "upper bound" appears (p. 3, Remark 1.1(1)) ONLY for the n=2 second
moment of OTHER, unweighted variants, attributed to Goldston-Montgomery
[11], Saffari-Vaughan [34], and Zaccagnini [38,39]; the authors prove no
upper bound of their own. (They believe their lower bounds "sharp up to a
power-saving error term in delta (c.f. [26, Theorem 3])", p. 1, but state
no matching upper bound.)

Probe -- "growing moment order": FOUND. p. 3, Theorem 1.2: the range
"n <= delta^{-1/2} (log(delta^{-1} + 2))^{1/2}" permits n to grow with
delta; p. 3-4, Corollary 1.3: "2 <= m <= min(delta^{-1/2}
(log(delta^{-1}+2))^{1/2} f(X)^{1/2}, log log X)" (RH) and
"2 <= m <= min(delta^{-1/2}, log log X)" (unconditional). The moment order
is explicitly allowed to grow, up to order log log X.

Probe -- "tuple": FOUND only as the Hardy-Littlewood input, NOT as an
object the paper controls. p. 1, verbatim: "Montgomery and Soundararajan
[26, Theorem 3] have shown that (1.2) follows from a strong form of the
Hardy-Littlewood prime k-tuple conjecture." The only other occurrences of
"tuple" (p. 7) are "2m-tuples of zeros" of zeta -- combinatorial tuples of
zero-ordinates in Lemma 2.3, not prime k-tuples. The paper proves nothing
about prime tuples.

Probe -- "singular series" at growing rank: NOT FOUND in this text. The
string "singular series" does not occur anywhere; the k-tuple conjecture
is invoked only as the (external) hypothesis behind (1.2), with no
singular-series expansion, no product over primes, and no rank-k singular
series appearing in any statement or proof.

Probe -- any statement about CONSECUTIVE primes or gap words: NOT FOUND in
this text (body). "consecutive" occurs only in a reference title (p. 14,
[19] Huxley, "On the difference between consecutive primes"). "gap" occurs
only as an application pointer, p. 1 ("For applications on the distribution
of gaps between primes, see for instance [4]"), and in a reference title
(p. 13, [4]). No gap-word, no consecutive-prime statement, is proved.

Probe -- any class-normalised or conditional-on-a-pattern quantity: NOT
FOUND in this text. Every quantity (psi_eta, Mn, F, the Omega-results) is
an UNRESTRICTED short-interval prime-power count psi(x+delta x)-psi(x),
weighted only by n^{-1/2} and by the analytic test functions eta, Phi.
There is no normalisation by a residue class, no conditioning on a gap
pattern, no word-grain class mass. ("class" occurs only as "class of test
functions", p. 2, and "classical prime counting function", p. 1.)

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

C1. What this paper unconditionally supplies. On an unbounded sequence
{X_j} of scales (Corollary 1.3, p. 4) and on an unbounded sequence
{(x_j, delta_j)} (Corollary 1.4, p. 4), it supplies lower bounds on all
weighted even moments of the centered short-interval prime count
psi(x+delta x)-psi(x)-delta x, plus Omega-results that this count exceeds
an unbounded (or arbitrarily-large-fixed-M^{1/2}) multiple of its standard
deviation (delta x log(delta^{-1}+2))^{1/2}. Under RH the same holds for
ALL X. This is a genuine unconditional-on-a-sparse-scale-set result -- the
exact shape the project's A6 axis is looking for.

C2. The A6 mechanism, named. The sparse scale sequence is manufactured by
an RH DICHOTOMY (p. 11: "If RH is true, then this is a particular case of
Theorem 1.2. Let us then assume that RH is false ... follows from
Proposition 3.1"), "strongly inspired from the work of Kaczorowski and
Pintz [20]" (p. 9). Proposition 3.1 (p. 9) turns a single hypothetical
off-line zero into an ineffective unbounded {x_j} on which the signed sum
F(x, delta; eta) is > x_j^{theta}, via an antiderivative + Rolle's-theorem
zero-counting argument. It is NOT a pigeonhole over a divergent sum, NOT a
zero-density estimate; it is an Omega-oscillation transfer. Two structural
consequences for the project: (a) the set of good scales is INEFFECTIVE
(theta is "an absolute (ineffective) constant", p. 9) and is a pure
existence statement -- there is no s-uniformity and no naming of the
scales, which is precisely the A6 profile ("sparse scales, no
s-uniformity"); (b) the mechanism is analytic (zeros of zeta), so it does
NOT depend on the moment being a lower bound in any essential way -- the
moment lower bound is a downstream Holder consequence of the oscillation
bound (p. 11), and the primitive object is the Omega-result.

C3. Why it nonetheless does not close the project's need -- the grain. The
controlled object is the UNRESTRICTED prime count psi(x+delta x)-psi(x),
never a class mass N_{P,d} of consecutive-gap words. The paper has no
tuple, no consecutive-prime, no gap-word, and no class-normalised quantity
(Section 6 probes). The project's A3 grain is exactly what this paper does
not have; the A6 mechanism here lives on the wrong grain (prime counts,
not word masses).

C4. Why it does not close the project's need -- the window and the rank.
The absolute window is delta*x, and delta is "relatively close to 1"
(p. 1); the shortest admissible window is a power (or log-power times x)
of x, never the near-logarithmic (ln x)(lnln x) scale (Uniformity ledger,
window translation). And the growing parameter is the even-MOMENT ORDER n
(capped at order log log X), an exponent on a single short-interval count
-- not a rank of a k-fold consecutive-gap-word tuple. The order-magnitude
coincidence (moment order can reach ~ log log X ~ (1/const) lnln x) is
real but is a coincidence of magnitude, not of object: A1's rank is a
tuple/word rank, absent here.

C5. Direction and strength. The results are non-concentration in
DIRECTION (even-moment lower bounds and Omega-results are anti-
concentration statements: the count is provably spread away from its mean,
p. 4: "can be larger than an unbounded constant times [its standard
deviation]"), which is aligned with A4; and the STRENGTH exceeds constant
order (unbounded factor delta_j^{-1/4}(...)^{1/4}, or fixed M^{1/2},
Corollary 1.4), so A5 is cleared with room to spare. But a moment lower
bound / Omega-result is a LOWER bound on spread, not an upper bound on the
concentration at the modal middle; it does not by itself deliver "a fixed
proportion of site mass off its modal middle" without a complementary
upper bound the paper does not prove.

C6. Net for the item-0026 A6 question. This is a real unconditional prime-
side result on a genuinely sparse, ineffective, non-s-uniform scale set --
it locates and names the A6 mechanism (RH dichotomy a la Kaczorowski-
Pintz). But it clears A6, A5, A4 while failing A3 (grain), A2 (window), and
A1 (rank object). It is therefore NOT a carrier of the project's needed
statement; it is the clearest located exhibit of how the A6 axis can be
met unconditionally (on the wrong grain and window), which is exactly why
CG relaxes A5/A6 and not A1-A4.

Per-axis verdict:
- A1 (rank k ~ (2/ln2) lnln x): FAILS. The only growing parameter is the
  even-moment order n = 2m, an exponent on a single short-interval prime
  count, capped at order log log X; it is not a rank of consecutive-gap-
  word tuples, and no k-fold tuple structure appears.
- A2 (window h ~ (ln x)(lnln x)): FAILS. The absolute window is delta*x
  with delta "relatively close to 1" (down to X^{-f(X)} or (log x)^{-power}
  scales); the shortest admissible window is a power/near-power of x, never
  the near-logarithmic scale.
- A3 (grain = class masses of consecutive-gap words): FAILS. The object is
  the unrestricted prime-power count psi(x+delta x)-psi(x); no word grain,
  no class mass, no pattern conditioning anywhere.
- A4 (direction = upper / non-concentration): CLEARS. Even-moment lower
  bounds and the Omega-results are non-concentration statements (the count
  is provably not concentrated at its mean), which is the A4 direction --
  with the caveat that this is a lower bound on spread, not an upper bound
  on modal-middle concentration.
- A5 (strength: constant order suffices): CLEARS. The Omega-results give
  unbounded (delta_j^{-1/4}(...)^{1/4}) and arbitrarily-large-fixed
  (M^{1/2}) multiples of the standard deviation, exceeding constant order.
- A6 (density: sparse scales, no s-uniformity): CLEARS. The unconditional
  statements hold on an unbounded, ineffective, non-s-uniform sequence
  {X_j} / {(x_j, delta_j)} (Corollaries 1.3, 1.4), manufactured by an RH
  dichotomy (Proposition 3.1); under RH they upgrade to all X. This is the
  located unconditional sparse-scale mechanism.

Even-Cramer-smooth deterministic gap system (q_1=2, q_2=3, q_3=5, q_4=7,
q_{n+1}=q_n+2*ceil(ln q_n / 2)): UNTESTED. The paper's A6 mechanism is
purely analytic -- it is driven by hypothetical off-critical-line zeros of
the Riemann zeta function (Proposition 3.1) and by the explicit formula
over zeros (Lemma 2.1). It has no interpretation in, and the paper makes no
contact with, a deterministic combinatorial gap model; the paper never
tests its result against such a system. (A guess is not offered: the
mechanism has no zero-of-zeta analogue in the even-Cramer-smooth model, so
whether an analogous statement holds there is genuinely outside this
text.)

Does the paper CLEAR all six axes? NO -- it clears A4, A5, A6 and fails
A1, A2, A3. It is not a located carrier.

---

## FLAGS (consolidated)

1. [PRINTED-ODDITY] Date discrepancy: the arXiv side-stamp on p. 1 reads
   "12 Sep 2020", while the paper's own footer reads "Date: September 15,
   2020." and the PDF CreationDate is 15 Sep 2020. Both recorded; no
   bearing on content.
2. [TRANSCRIPTION-UNSURE, resolved-by-image] Conjecture 1.1 (1.2),
   Theorem 1.2 (1.6), Corollary 1.3 (1.7), and Corollary 1.4 (the delta_j
   range and both Omega-lower-bounds) carry stacked superscripts/subscripts
   (n/2 exponents, (log_3 x_j)^{9/2}/((log x_j)^2 (log_2 x_j)^{5/2}), the
   -7/2 - 3/(2M) exponent) that the pdftotext layers scramble. All were
   transcribed from the 200-dpi page images (pages 1, 3, 4) and cross-
   checked against the -layout text layer where legible. High confidence.
3. [TRANSCRIPTION-UNSURE, resolved-by-context] The iterated-log subscript
   convention log_2 x = log log x, log_3 x = log log log x is inferred from
   context (the paper uses "log log X" in Corollary 1.3 in words and
   "log_2 x_j", "log_3 x_j" in Corollary 1.4 in symbols, in mutually
   consistent roles); the paper does not print an explicit definition of
   the subscript.
4. [PRINTED-ODDITY] In Theorem 1.2 the left side is (-1)^n Mn, i.e. the
   sign is folded into the statement so that the bound is a lower bound on
   (-1)^n Mn (for even n this is Mn itself; the (-1)^n is what lets a
   single display cover all n). Transcribed as printed.
5. [PRINTED-ODDITY] Corollary 1.3's m=1 clause and Corollary 1.4's first
   sequence use OPEN-at-left, CLOSED-at-right delta-intervals
   (X^{-f(X)}, f(X)] and half-open [.,.]; brackets transcribed exactly as
   printed from the images.
6. In Lemma 2.1 the argument of etahat is printed as
   (delta/2pi)((rho-1/2)/i) in (2.2) and (delta/2pi)(rho/i) in (2.3); both
   forms transcribed as printed (the (2.3) variant drops the -1/2 shift,
   consistent with its different left-hand side).
7. The unconditional Corollary 1.3 clause narrows the RH m-range from
   min(delta^{-1/2}(log(delta^{-1}+2))^{1/2} f(X)^{1/2}, log log X) to
   min(delta^{-1/2}, log log X); transcribed as printed, the narrowing is
   the paper's (the f(X)^{1/2}(log(...))^{1/2} factor is dropped
   unconditionally).
