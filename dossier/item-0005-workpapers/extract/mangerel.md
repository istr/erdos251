# EXTRACTION: Mangerel, "On Equal Consecutive Values of Multiplicative Functions"

Source: /home/istr/pro/erdos251/dossier/2306.09929v4.pdf
arXiv:2306.09929v4 [math.NT] 4 Nov 2024. Published: Discrete Analysis, 2024:12, 20 pp.
Author: Alexander P. Mangerel. Received 19 June 2023; Revised 4 January 2024;
Published 11 November 2024. DOI: 10.19086/da.125450.

Method note: located via pdftotext; all displayed formulas below were transcribed
from visually rendered pages (Read tool, pages 2-10), not from pdftotext output.
Everything in Sections A-J below is faithful extraction from the PDF (verbatim
quotes marked as such). Commentary appears ONLY in the final marked section K.

Notation used in transcription: N = positive integers, C = complex numbers,
R = reals, Z = integers, U = closed unit disc (paper writes blackboard U),
D(f,g;x) = the pretentious distance (paper writes blackboard D),
1_{cond} = indicator, != means "not equal", \nmid = "does not divide".

---

## A. Abstract (page 1, verbatim)

"Let f : N -> C be a multiplicative function for which

    \sum_{p : |f(p)| != 1} 1/p = \infty.

We show under this condition alone that for any integer h != 0 the set

    {n \in N : f(n) = f(n + h) != 0}

has logarithmic density 0. We also prove a converse result, along with an
application to the Fourier coefficients of holomorphic cusp forms.
The proof involves analysing the value distribution of f using the compositions
|f|^{it}, relying crucially on various applications of Tao's theorem on
logarithmically-averaged correlations of non-pretentious multiplicative
functions. Further key inputs arise from the inverse theory of sumsets in
continuous additive combinatorics."

[Note: page 1 carries the journal template artifacts "(c) 2024 P. Erdos,
J. Hastad, L. Lovasz, and A. C-C. Yao" (license line, not authorship) and
"Key words and phrases: keyword, keyword, etc." (unfilled placeholder).]

## B. Framing before the main theorem (Section 1, pages 2-3)

Definition (footnote 1, page 2, verbatim): "The density of a set A \subseteq N
is defined by lim_{x->\infty} |A \cap [1,x]|/x, provided the limit exists. The
upper density of f is given by the same definition with lim sup in place of lim."

Precedent quoted in Section 1 (page 2): Erdos-Pomerance-Sarkozy [4] proved for
the divisor function d that

    |{n <= x : d(n) = d(n+1)}| \ll x / \sqrt{\log\log x},

"and thus d(n) = d(n+1) occurs on a set of natural density 0." Also [8]
(Klurman-Mangerel) showed for a weight-k arithmetically normalised holomorphic
cuspidal eigenform phi without CM for SL_2(Z) that
{n \in N : a_phi(n) = a_phi(n+h) != 0} has natural density 0 for every h >= 1.

Scope statement (Section 1, page 3, verbatim): "where f : N -> C is an
arbitrary multiplicative function, provided only that |f(p)| != 1 sufficiently
often (in a precise sense). While we are unable to establish that this set has
natural density 0, we do prove that it is a thin set in a weaker sense."

## C. Main theorem (Theorem 1.1, page 3, verbatim)

"Theorem 1.1. Let f_1, f_2 : N -> C be multiplicative functions and let h >= 1.
Assume that

    \sum_{p : |f_1(p)| != 1} 1/p = \infty.                              (1)

Let a, b \in N, c, d \in Z with ad - bc != 0 and (a,b) = (c,d) = 1. Let also
C \in C \ {0}. Then the set

    {n \in N : f_1(an + b) = C f_2(cn + d) != 0}

has logarithmic density 0, i.e., we have

    \frac{1}{\log x} \sum_{\substack{n <= x \\ f_1(an+b) f_2(cn+d) != 0}}
        \frac{1_{f_1(an+b) = C f_2(cn+d)}}{n} = o(1).                   (2)"

[Extraction note, not commentary: the variable h >= 1 is introduced in the
statement but does not occur again within the statement of Theorem 1.1; the
affine forms an+b, cn+d play the role of n, n+h. See flag list.]

Interface facts visible in the statement itself:
- Hypothesis on f_1 only: divergence condition (1). No hypothesis on f_2 beyond
  multiplicativity. No boundedness or growth hypothesis on either function.
- Averaging: logarithmic (weight 1/n, normalisation 1/log x).
- Conclusion: o(1) as x -> \infty with NO stated rate. All parameters
  a, b, c, d, C (and h) are FIXED before the limit; no uniformity in any
  parameter is asserted.

## D. Limitation remarks attached to Theorem 1.1 (page 3, verbatim)

"Remark 1.2. Ideally, we would like to prove the same result with the notion of
'logarithmic density' replaced by 'natural density'. Unfortunately, we are
(unconditionally) limited in this matter by the fact that the linchpin of our
proof, Tao's theorem on logarithmically-averaged binary correlations of
multiplicative functions (see Theorem 2.2 below) has not been proven for
Cesaro-averaged binary correlations. The corresponding result is, however,
expected to hold by a conjecture due to Elliott (see [17] for a discussion),
and assuming Elliott's conjecture our result would immediately be upgraded in
this way.

While a Cesaro-averaged result of this kind is known at almost every scale x
(see [18, Cor. 1.13]), this variant would be incompatible with our objectives,
since in order to prove Theorem 1.1 we already need to restrict our attention
to an arbitrary infinite subsequence of scales which may not intersect with the
'good' scales of such a theorem."

"Remark 1.3. The non-vanishing condition f_1(an+b) f_2(cn+d) != 0 is
necessary^3 in this theorem. Indeed, take any complex-valued multiplicative
function f and define \tilde{f} := \mu^2 f. Then \tilde{f} is supported on
squarefree integers. For any fixed, distinct primes p_1, p_2 not dividing
ac(ad - bc) the set

    {n \in N : \tilde{f}(an+b) = \tilde{f}(cn+d)}

contains the positive density set

    {n \in N : p_1^2 | (an+b),   p_2^2 | (cn+d)}.

For any n in this subset both an + b and cn + d are not squarefree, and hence
\tilde{f}(an+b) = 0 = \tilde{f}(cn+d)."
(Footnote 3: "We thank the anonymous referee for pointing out this simple
construction.")

"Remark 1.4. When f_1, f_2 are completely multiplicative, the condition
(a,b) = (c,d) = 1 may be dropped, as we may always reduce to the coprime case
(by adjusting the value of C)."

## E. Comparison with Elliott-Kish; quantitative "1% world" version (page 4, verbatim)

"Theorem 1.1 can be compared with the main result of [2]. There, Elliott and
Kish prove that if f : N -> C is completely multiplicative and

    f(an+b) = C f(cn+d) != 0 for all n >= n_0,

where ad - bc != 0 and C \in C \ {0}, then there is a Dirichlet character \chi
of some modulus m = m(a,b,c,d) such that

    f(p) = \chi(p) for all p \nmid m.

When f_1 = f_2 = f our result addresses the '1% world' version of their
problem, showing that if the (logarithmic) proportion of n that satisfy the
equation is >= \delta, for \delta > 0 a small parameter, then

    \sum_{p : |f(p)| != 1} 1/p < \infty.                                (3)

While this is consistent with the result in [2], in our setting no further
structural information about f can possibly be gleaned, and in particular f
need not behave like a Dirichlet character, or even be pretentious (see Section
2.1 for the relevant definition)! Indeed, it is known for instance [17, Cor.
1.7] that the Mobius function \mu satisfies

    \mu(n) = \mu(n+1) != 0 on a set of logarithmic density
        \frac{1}{2} \prod_p (1 - 2/p^2),

and it is well-known that \mu is non-pretentious."

[Interface fact: the quantitative content of the paper is a dichotomy -- log
proportion >= delta at infinitely many scales forces convergence of the sum
(3). No rate linking delta to the conclusion is stated at theorem level.]

## F. Converse result (Proposition 1.5, page 4, verbatim)

"Proposition 1.5. Let f : N -> R \ {0} be a multiplicative function for which
(3) holds. Then there is a u \in {-1, +1} such that

    \limsup_{x \to \infty} \frac{1}{\log x} \sum_{n <= x}
        \frac{1_{f(n) = u f(n+2)}}{n} > 0."

(Stated for the single case of affine maps n, n+2; text preceding it:
"In fact, we may obtain the following (elementary) converse for real-valued f;
for simplicity we constrain ourselves to a single case of affine maps an + b
and cn + d.")

## G. Application to cusp forms (pages 4-5)

Recovered result (display (4), page 4, verbatim):
"Theorem 1.1 allows us to recover the result

    \lim_{x \to \infty} \frac{1}{\log x}
        \sum_{\substack{n <= x \\ a_\phi(n) a_\phi(n+h) != 0}}
        \frac{1_{a_\phi(n) = a_\phi(n+h)}}{n} = 0                       (4)

for the sequence of Fourier coefficients (a_\phi(n))_n of any holomorphic cusp
form without CM for SL_2(Z). While this is weaker than what is proved in [8],
(4) may be shown without appealing to an effective version of the Sato-Tate
theorem such as that found in [19]. As such, we may avoid having to apply the
deep theorems of Newton-Thorne [14] on the functoriality of symmetric power
lifts of holomorphic cusp forms. Indeed, our proof (see Section 5) requires
nothing more than:
  - the prime number theorem for Rankin-Selberg L-functions, and
  - Deligne's bound for the prime-indexed Fourier coefficients |a_\phi(p)|,
both of which apply (at least conjecturally and in some cases unconditionally)
to the sequence of coefficients of the standard L-function of a broader
collection of cuspidal automorphic forms."

"Corollary 1.6. Let h >= 1 be fixed and let \phi_1, \phi_2 be holomorphic cusp
forms for the full modular group. Then the set

    {n \in N : a_{\phi_1}(n) = a_{\phi_2}(n + j) != 0 for some 1 <= |j| <= h}

has logarithmic density 0."

"Remark 1.7. Note that the claim is trivial if, say, \phi_1 is assumed to have
CM. In this case, it is known [16] that

    |{n <= X : a_{\phi_1}(n) != 0}| \asymp \frac{X}{\sqrt{\log X}},

which necessarily implies that {n \in N : a_{\phi_1}(n) = a_{\phi_2}(n+h) != 0}
has logarithmic density 0."

"Remark 1.8. A result like Corollary 1.6 may be proved for the sequences of
coefficients (a_{\pi_j}(n))_n of the standard L-functions of fixed cuspidal
automorphic representations \pi_j for GL_{m_j}, m_j >= 1, with unitary central
character (j = 1, 2), assuming that at least one of \pi_1, \pi_2 satisfies the
Generalised Ramanujan Conjecture (see e.g. [13, Sec. 1.3.1] for relevant
preliminaries). We leave this extension to the interested reader."

Proof of Corollary 1.6 (Section 5, page 18): reduces to verifying (1) for
a_phi; uses the Rankin-Selberg PNT in the form (display (26), page 18)

    \sum_{p <= X} |\lambda_\phi(p)|^2 \log p = X + O(X e^{-c \sqrt{\log X}}),
        \lambda_\phi(n) := a_\phi(n) / n^{(k-1)/2},  c = c_\phi > 0,

plus Deligne's bound |a_\phi(p)| <= 2 p^{(k-1)/2}, concluding
\sum_{p <= x, |a_\phi(p)| != 1} 1/p >= c \log\log x + O(1) with c = 1/(10 log 2).
Theorem 1.1 is then applied separately "to each of the equations
a_\phi(n) = a_\phi(n + j), 1 <= |j| <= h" (finitely many fixed shifts).

## H. Proof strategy (Section 1.1.2, pages 5-6) -- structure of the argument

Contradiction hypothesis (display (5), page 5, verbatim): "We will assume for
the sake of contradiction the existence of a (small) parameter
\delta \in (0,1) and an infinite increasing sequence (x_j)_j such that

    \frac{1}{\log x_j} \sum_{\substack{n <= x_j \\ f_1(an+b) f_2(cn+d) != 0}}
        \frac{1_{f_1(an+b) = C f_2(cn+d)}}{n} >= \delta,  \quad j >= 1.   (5)"

Mechanism (page 6): define the archimedean projections

    |f|_t(n) := |f(n)|^{it} if f(n) != 0;  0 if f(n) = 0,

a multiplicative function with values in U, and g(n) := A log|f(n)| (additive
on {n : f(n) != 0}), A >= 1 a parameter. Note f(n) = f(n+h) != 0 implies
g(n) = g(n+h), and |f|_{2\pi A t}(n) = e(t g(n)). Via a Fourier analytic
identity, (5) yields a bounded set X \subset R of positive Lebesgue measure
with, for each y \in X,

    \frac{1}{\log x_k} \Big| \sum_{n <= x_k}
        \frac{|f|_{2\pi A y}(n) |f|_{-2\pi A y}(n+h)}{n} \Big| \gg_\delta 1.

Verbatim (page 6): "For each of these y \in X, Tao's theorem implies the
existence of a Dirichlet character \chi_y of conductor depending only on
\delta, and t_y \in R of controlled size such that f_y pretends to be a twisted
character \chi_y(n) n^{i t_y} (see Section 2.1 for a relevant definition). By
passing to a positive measure subset X' of X if needed we may assume that
\chi_y is the same for all y, and so we focus on studying the dependence of t_y
on y.
Using an idea going back to Halasz [6] and subsequently refined by Ruzsa [15],
we show that the mapping y |-> t_y extends to an entire interval I and is
uniformly approximated on I by a linear function y |-> r y for some r \in R
depending at most on \delta. In this way we find that for most primes p <= x_k
and for all y \in I,

    |f(p)|^{2\pi i A y} \approx p^{2\pi i t_y} \approx p^{2\pi i r y},

and thus that |f(p)|^A \approx p^r for 'typical' primes p. Since A is
arbitrarily large, we deduce that |f(p)| = 1 outside of a sparse set of primes,
which contradicts our assumption (1)."

## I. Key external input: Tao's theorem (Section 2.2, page 9, verbatim)

"Theorem 2.2 (Tao's theorem on binary correlations). Let \eta > 0, and let
a, c \in N, b, d \in Z with ad - bc != 0. Let g_1, g_2 : N -> U be 1-bounded
multiplicative functions with the property that for some x >= x_0(\eta) we have

    \frac{1}{\log x} \Big| \sum_{n <= x}
        \frac{g_1(an+b) g_2(cn+d)}{n} \Big| >= \eta.

Then for each j = 1, 2 there is a real number t_j = t_{j,x} with t_j =
O_\eta(x) and a primitive Dirichlet character \psi_j = \psi_{j,x} with
conductor O_\eta(1) such that

    \sum_{p <= x} \frac{1 - Re(g_j(p) \overline{\psi_j}(p) p^{-i t_j})}{p}
        = O_\eta(1)."

[Transcription double-checked visually: the bound on t_j reads O_\eta(x), and
t_j, \psi_j carry subscript x, i.e. they may depend on the scale x. Attribution
in text: "the following theorem of Tao [17]", where [17] = T. Tao, "The
logarithmically-averaged Chowla and Elliott conjectures for two-point
correlations."]

Error-term quality of this input: all constants are of the ineffective form
O_\eta(1) / O_\eta(x); the character and t_j are scale-dependent; conclusion is
a pretentious-distance bound O_\eta(1), not a rate.

Supporting standard result (Lemma 2.1, page 8, verbatim):
"Lemma 2.1. Let \epsilon > 0 and let x >= x_0(\epsilon). If 10 <= |t| <= x^2
then

    D(n^{it}, 1; x)^2 >= (1/3 - \epsilon) \log\log x.                   (9)

Moreover, if |t| <= 10 then

    D(n^{it}, 1; x)^2 = \log(1 + |t| \log x) + O(1).                    (10)"

(Proof note, page 8, verbatim: "Since we could not locate a proof of this
precise statement in the literature, we give one here.")

Pretentious distance (Section 2.1, page 7): for f, g : N -> U and x >= 2,

    D(f, g; x) := ( \sum_{p <= x} \frac{1 - Re(f(p) \overline{g}(p))}{p} )^{1/2},
    D(f, g; \infty) := \lim_{x \to \infty} D(f, g; x),

with 0 <= D(f,g;x)^2 <= 2 \log\log x + O(1); "f pretends to be g" iff
D(f,g;\infty) < \infty; triangle inequalities (6), (7), and (8):
D(f^m, g^m; x) <= m D(f, g; x) for m >= 1.

## J. Main technical engine (Proposition 3.1 and Remark 3.2, page 10, verbatim)

"Proposition 3.1. Let f_1, f_2 : N -> C be multiplicative functions, and
suppose f_1 satisfies

    \sum_{p : f_1(p) = 0} 1/p < \infty, \qquad
    \sum_{p : |f_1(p)| != 1} 1/p = \infty.                              (11)

Let a, c \in N, b, d \in Z and C \in C, with C(ad - bc) != 0. Suppose there is
a \delta > 0 and an infinite increasing sequence (x_j)_j such that for each
j >= 1,

    \frac{1}{\log x_j} \sum_{\substack{n <= x_j \\ f_1(an+b) f_2(cn+d) != 0}}
        \frac{1_{f_1(an+b) = C f_2(cn+d)}}{n} >= \delta.               (12)

Then if j >= j_0(\delta) and A >= 1 there is a parameter
r_j = r_j(A) \in [-x_j^2, x_j^2] such that if \delta^{-2} <= B \ll_\delta 1
then

    \sum_{\substack{p <= x_j \\ |f_1(p)|^A / p^{r_j} \notin [e^{-2/B}, e^{2/B}]}}
        \frac{1}{p} \ll_\delta 1,                                       (13)

the bound (13) being independent of A."

"Remark 3.2. As is suggested by the hypotheses of Proposition 3.1, we will be
able to assume in the sequel that

    \sum_{p : f_1(p) = 0} \frac{1}{p} < \infty,                         (14)

as otherwise Theorem 1.1 is essentially trivial.
Indeed, as the function 1_{f_1(n) != 0} is multiplicative, it follows that

    \sum_{n <= x} \frac{1_{f_1(n) != 0}}{n}
      \ll \prod_{p <= x} \Big(1 + \frac{1_{f_1(p) != 0}}{p}\Big)
      \ll (\log x) \exp\Big( \sum_{p <= x} \frac{1_{f_1(p) != 0} - 1}{p} \Big)
      = o(\log x)

whenever \sum_{p : f_1(p) = 0} p^{-1} = \infty. This implies that
{n : f_1(an+b) = C f_2(cn+d) != 0} has logarithmic density 0 for any fixed
a, b, c, d, C as in the theorem."

Related variant (Remark 1.9, page 7, verbatim): "In the recent work [11], we
considered the variant problem of bounding the size of sets

    {n <= x : f(n+a) = f(n) + b},  where ab != 0, x >= 1,

for f an integer-valued multiplicative function. We used this together with the
work in the present paper to obtain a partial classification of all unbounded
multiplicative functions f : N -> N for which the set

    {n \in N : |f(n+1) - f(n)| <= C},

i.e., the set of n for which the gaps between consecutive values of f(n) is
bounded by some C > 0, has positive upper density.
Unlike in the homogeneous (i.e., a = 0) problem considered in this paper,
examples do exist where the number of such solutions has positive density
(e.g., take a = b = 1, then f(n) = n is such an example). In addition to the
'archimedean' projections |f(n)|^{it} applied here, we also consider
corresponding 'non-archimedean' projections \chi(f(n)), for \chi a Dirichlet
character to a suitably chosen modulus q >= 1. The application of these latter
projections were developed in connection to the present paper, but thanks to a
neat observation by the anonymous referee these turned out to be unnecessary
here."

---

## K. COMMENTARY (extractor's observations -- NOT from the paper)

### K.1 Interface card

- INPUT CLASS: f_1, f_2 : N -> C arbitrary multiplicative functions;
  only quantitative hypothesis: \sum_{p : |f_1(p)| != 1} 1/p = \infty (on f_1
  alone). No boundedness, no growth condition, no pretentiousness condition.
- STATEMENT SHAPE: for FIXED affine forms an+b, cn+d (ad - bc != 0, coprimality
  (a,b) = (c,d) = 1 unless completely multiplicative) and FIXED constant C != 0,
  the coincidence set {n : f_1(an+b) = C f_2(cn+d) != 0} has LOGARITHMIC
  density 0.
- AVERAGING: logarithmic only ((1/log x) \sum 1/n). Natural (Cesaro) density
  version explicitly out of reach unconditionally (Remark 1.2); available under
  Elliott's conjecture; almost-all-scales Cesaro variants are stated to be
  incompatible with the proof (which needs an arbitrary subsequence of scales).
- SHIFT UNIFORMITY: none. Every parameter (a, b, c, d, C; the shift h in the
  special case (n, n+h)) is fixed before x -> \infty. Corollary 1.6 covers only
  finitely many shifts 1 <= |j| <= h with h fixed, by applying Theorem 1.1
  separately to each shift. No statement lets the shift grow with x, and no
  uniformity over shift classes is claimed anywhere in the paper.
- ERROR-TERM QUALITY: purely qualitative o(1) in (2); no rate in terms of x,
  delta, or the divergence speed of (1). The proof is by contradiction against
  an infinite subsequence of scales (display (5)), so implied constants are
  ineffective. The quantitative core (Proposition 3.1 / the "1% world"
  statement (3)) is a dichotomy: log-proportion >= delta at infinitely many
  scales forces \sum_{p:|f(p)| != 1} 1/p < \infty; the conclusion (13) has
  \ll_\delta bounds with unspecified delta-dependence inherited from Tao's
  theorem's O_\eta(1) (ineffective in eta).
- KEY EXTERNAL INPUT: Tao's log-averaged binary correlation theorem
  (Theorem 2.2), with scale-dependent t_{j,x} = O_\eta(x) and conductor
  O_\eta(1); this single input forces both the log averaging and the
  ineffectivity.
- CONVERSE: Proposition 1.5 shows the divergence hypothesis (1) is essentially
  sharp for real-valued nonvanishing f (positive log density of coincidences
  f(n) = u f(n+2) when (3) holds).

### K.2 Which aspects are plausibly the "too weak" ones (from this text alone)

The phrase "too weak for our purposes" is from the citing paper, not this PDF;
based only on what this PDF states, the candidate weaknesses are:

1. Logarithmic density only, not natural density; explicitly flagged as an
   unconditional barrier in Remark 1.2 (linchpin Theorem 2.2 unavailable for
   Cesaro averaging). Any application needing Cesaro counts or
   summation-by-parts along all scales cannot use Theorem 1.1 directly.
2. No quantitative rate: conclusion (2) is o(1) with no decay function. The
   introduction itself contrasts this with the explicit sieve bound
   x/\sqrt{\log\log x} of Erdos-Pomerance-Sarkozy for d(n) = d(n+1). Any
   argument needing a summable (over shifts or scales) bound on the density of
   coincidence sets gets nothing usable from the theorem as stated.
3. No uniformity in the shift/affine data: the o(1) depends on the fixed
   a, b, c, d, C in an unspecified way; nothing is claimed for h growing with
   x, nor for averages over h. (Corollary 1.6: finitely many fixed shifts.)
4. Ineffectivity: proof by contradiction over an unspecified infinite scale
   sequence, plus O_\eta(1) constants from Tao's theorem; no effective x_0.
5. The hypothesis class is |f(p)| != 1 on a divergent set of primes -- the
   method's engine is the archimedean projections |f|^{it}, i.e. it detects
   MODULUS deviations from 1. It gives nothing when |f(p)| = 1 for (almost)
   all p, and the converse Proposition 1.5 shows density-zero then genuinely
   fails, so this boundary is intrinsic, not an artifact.

### K.3 Relevance posture toward item-0005 (labeled commentary)

[BACKGROUND-UNVERIFIED]: The Tao-Teravainen irrationality paper is not part of
this evidence base; how they use or reject this benchmark must be read from
their own text. From this PDF alone: the deliverable here is a
qualitative, log-averaged, fixed-shift, ineffective density-zero statement for
coincidences of multiplicative functions, whose engine (Tao's two-point
log-averaged correlation theorem) caps both the averaging mode and the
effectivity. An irrationality argument in the style of digit/tail control
typically needs quantitative, shift-uniform bounds summable over scales; on the
face of the statements extracted above, items K.2 (1)-(4) are exactly the axes
on which such an application would find Theorem 1.1 "too weak".
