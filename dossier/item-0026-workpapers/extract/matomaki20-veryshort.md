# EXTRACTION: Kaisa Matomaki, "Almost primes in almost all very short intervals"

Source (only evidence base): /home/istr/pro/erdos251/dossier/2012.11565v3.pdf
sha256 676ac2ceafc1550d63d70e71b34d4b1ed84d41918e3f6178a252e6cf9f0f007d
(operator-verified; re-verified this session).
arXiv:2012.11565v3 [math.NT] 18 Jan 2022. 31 pages.
Author: Kaisa Matomaki, Department of Mathematics and Statistics,
University of Turku, 20014 Turku, Finland (address block, p. 31).
2010 Mathematics Subject Classification: 11N25, 11N36 (p. 1 footnote).
No journal reference printed on the paper (preprint form).
Grant/acknowledgment (p. 30): "The author was supported by Academy of
Finland grant no. 285894." Thanks to John Friedlander and Henryk Iwaniec
(discussions on [7, Chapter 6]), James Maynard and Maksym Radziwill
(alternative approach, Remark 2.2), Andrew Granville (Mikawa's work),
and the referee.

Front-matter check against steering identification: author "KAISA
MATOMAKI", title "ALMOST PRIMES IN ALMOST ALL VERY SHORT INTERVALS" --
MATCHES the steering identification (Matomaki, Almost primes in almost
all very short intervals). No deviation.

---

## Transcription conventions

ASCII only. Diacritics transliterated: Matomaki (Matomaki), Teravainen
(Teravainen), Erdos, Granville, Radziwill, Deshouillers, Iwaniec,
Mobius (Mobius). Anchors are the paper's own numbering: Theorem 1.1,
Lemma 4.x, Proposition 5.1, Lemma 5.3, equation numbers (1)-(57+),
Section numbers 1-7; page numbers (printed = PDF page, they coincide)
are a secondary aid.

Symbol table (every non-obvious glyph):

- Omega(n) : total number of prime factors of n, counted with
  multiplicity ("Omega(n)" in the paper is the capital-Omega function).
- omega(n) : number of DISTINCT prime factors of n.
- P_k number : integer n with Omega(n) <= k (at most k prime factors).
- E_k number : integer n with Omega(n) = k (exactly k prime factors).
- 1_{P} : indicator function of a claim P (so 1_{Omega(n)<=2}).
- Lambda(n) : von Mangoldt function.
- mu(n) : Mobius function.
- phi(n) : Euler totient (the paper writes varphi).
- Lambda, mu, phi as above; sigma, gamma, rho are smooth weights / sieve
  weights described in context.
- p, p_i : always a prime (paper's convention).
- P(z_0) := prod_{p < z_0} p (product of primes below z_0).
- H := h log X (the interval length); A(x) := (x - h log X, x] cap N.
- z, y, D, w, E, U : sieve levels defined in (10) and Section 2.
- lambda^{+}, lambda^{-} : upper / lower bound LINEAR sieve weights.
- rho^{+}, rho^{-} : upper / lower bound BETA-sieve weights (beta = 30).
- alpha^{+}, alpha^{-} : combined (vector-sieve) weights, (15)/(25).
- S(B, z) := #{ n in B : (n, P(z)) = 1 } (sifted count).
- e(u) := e(2*pi*i*u) transcribed as printed; see flag 1.
- gb, "g hat" = Fourier transform of g; "a bar" = inverse of a mod q.
- <= , >= , ~ (tends to / asymptotic), != ; "<<" is Vinogradov O,
  ">>" its lower-bound partner; "asymp" is the paper's "A << B << A"
  relation (printed as the double-tilde/asymp glyph).
- eps = varepsilon; eps' = a second small parameter in Section 3.
- gamma (in e^gamma, f(4)) = Euler's constant.
- Integrals int_{-inf}^{inf}, int_{X/2}^{X} as printed.
- tau(n) : divisor function (Lemma 4.1).
- p | n : p divides n; p !| n : p does not divide n;
  "p|n => p > X^{1/8}" is the constraint printed under the theorem sum.

Everything up to the COMMENTARY section is EXTRACTION (what the paper
says). Assessment appears ONLY in the marked COMMENTARY section.

---

## 1. FRONT MATTER AND ABSTRACT

Title (p. 1): "Almost primes in almost all very short intervals".
Author: "Kaisa Matomaki".

Abstract (p. 1), verbatim:

> "We show that as soon as h -> infinity with X -> infinity, almost all
> intervals (x - h log X, x] with x in (X/2, X] contain a product of at
> most two primes. In the proof we use Richert's weighted sieve, with
> the arithmetic information eventually coming from results of
> Deshouillers and Iwaniec on averages of Kloosterman sums."

---

## 2. SECTION 1 (Introduction): the parity passage and the sieve input

Opening (Section 1, p. 1), verbatim:

> "By probabilistic models, one expects that short intervals of the type
> (x - h log X, x] contain primes for almost all x in (X/2, X] as soon
> as h -> infinity with X -> infinity. Heath-Brown [12] has established
> this assuming simultaneously the Riemann hypothesis and the pair
> correlation conjecture for the zeros of the Riemann zeta function.
> Without such strong hypotheses we are rather far from this claim --
> the best result [14] today is that almost all intervals of length
> X^{1/20} contain primes."

Almost-prime background (p. 1), verbatim:

> "One can ask a similar question about almost-primes, i.e. P_k numbers
> that have at most k prime factors or E_k numbers that have exactly k
> prime factors. In the second case the best results are due to
> Teravainen [20] who showed that, for any eps > 0, almost all intervals
> of length (log log X)^{6+eps} log X contain an E_3 number and that
> almost all intervals of length (log X)^{3.51} contain an E_2-number."

THE PARITY-BARRIER PASSAGE (p. 1), verbatim and complete:

> "The case of P_k numbers is significantly easier than that of E_k
> numbers since the so called parity barrier does not apply; due to the
> parity barrier classical sieve methods based only on so called type I
> information cannot distinguish numbers having an even number of prime
> factors from those having an odd number of prime factors. In
> particular classical sieve methods can, in favourable circumstances,
> be used to show that a given set contains P_2 numbers, but to show
> that it contains E_2 numbers requires additional arithmetic
> information. For more information about the parity barrier, see e.g.
> [7, Section 16.4]."

The sieve-input lineage / stated aim (p. 1), verbatim:

> "Following Friedlander [8, 9], Friedlander and Iwaniec [7] showed that
> as soon as h -> infinity with X -> infinity, almost all intervals
> (x - h log X, x] contain P_19-numbers.
>   In [7, Between Corollary 6.28 and Proposition 6.29] Friedlander and
> Iwaniec discuss the possibility to improve their result. In particular
> they mention that using linear sieve theory and estimates for general
> bilinear forms of exponential sums with Kloosterman fractions from
> [6], one should be able to improve P_19 to P_3. Then they say that
> ''It would be interesting to get integers with at most two prime
> divisors''. This is the aim of the current note."

Notational conventions (p. 1), verbatim:

> "The letter p with or without subscripts always denotes a prime
> number. We write Omega(n) for the total number of prime factors of n
> and omega(n) for the number of distinct prime factors of n.
> Furthermore we write 1_P for the indicator function of a claim P."

---

## 3. THEOREM 1.1 (main result), verbatim

Theorem 1.1 (p. 2), verbatim [display confirmed against rendered page
image, see flag 4]:

> "Theorem 1.1. There exists a constant c > 0 such that the following
> holds. Let X >= 2 and 2 <= h <= X^{1/100}. Then
>       sum_{ x - h log X < n <= x, p|n => p > X^{1/8} } 1_{Omega(n)<=2}
>          >= c h
> for all x in (X/2, X] apart from an exceptional set of measure
> O(X/h)."

Consequence stated immediately after (p. 2), verbatim:

> "Hence, as soon as h -> infinity with X -> infinity, almost all
> intervals of length h log X contain P_2-numbers. Previously it was
> known, as a consequence of the work of Teravainen [20] on E_2 numbers,
> that almost all intervals of length (log X)^{3.51} contain
> P_2-numbers. Before Teravainen's work, the best result was due to
> Mikawa [17] who showed that as soon as h -> infinity with X, almost
> all intervals (x - h(log X)^5, x] contain P_2-numbers. On the other
> hand, by work of Wu [21] it is known that the interval
> (x - x^{101/232}, x] contains P_2 numbers for all sufficiently large
> x."

THE CORRESPONDING UPPER BOUND (p. 2), verbatim [this answers the
"upper bound" NOT-FOUND probe: it is FOUND]:

> "The corresponding upper bound
>       sum_{ x - h log X < n <= x, p|n => p > X^{1/8} } 1_{Omega(n)<=2}
>          = O(h)
> for all x in (X/2, X] apart from an exceptional set of measure O(X/h)
> follows immediately from [7, Corollary 6.28]."

So the two-sided statement is: for almost all x in (X/2, X], the count
of P_2 numbers (with no prime factor below X^{1/8}) in the interval
(x - h log X, x] is asymp h. The upper bound is not proved in this note;
it is quoted from Friedlander-Iwaniec [7, Corollary 6.28].

---

## 4. SETTING UP THE SIEVES (Section 2): Richert's weighted sieve

PARAPHRASE except quotes. The paper follows "Richert's [18] weighted
sieve following [7, Chapter 25]" (p. 4). This is a LINEAR (one-
dimensional) sieve: the sieve functions used are F(s), f(s), "the linear
sieve functions (see e.g. in [7, (12.1, 12.2)])" with the explicit
values (29) f(4) = e^gamma (log 3)/2 and, for 0 < s <= 3,
F(s) = 2 e^gamma / s -- these are the dimension-1 (linear) sieve
functions. The sieve dimension is FIXED at 1 throughout; there is no
dimension parameter and nothing in the argument is stated to tolerate a
growing sieve dimension.

Levels (Section 2, (10), p. 4), verbatim:

> "D := X^{5/9},   z := D^{1/4} = X^{5/36},   y := D^{9/10} = X^{1/2},"

and (p. 4)

> "w_n := 1 - sum_{ p|n, z<=p<2y } ( 1 - log p / log y )."

Richert weight reduction (Section 2, p. 4), verbatim:

> "The coefficients w_n have been chosen in such a way that we can prove
> that, for almost all x in (X/2, X],
> (11)  sum_{ n in A(x), (n,P(z))=1 } 1_{Omega(n)<=2}
>          >= (1/2) sum_{ n in A(x), (n,P(z))=1 } w_n
> and
> (12)  sum_{ n in A(x), (n,P(z))=1 } w_n >> h.
> If we can show that these two claims hold for all x in (X/2, X] apart
> from an exceptional set of size O(X/h), then Theorem 1.1 clearly
> follows."

Choice of sieve weights (Section 2, p. 5-6), verbatim (structure):

> "Let beta = 30, let delta > 0 be small and take w = X^delta and
> E = X^{1/1000}. Write also P(w,z) = prod_{w<=p<z} p and define
> D^+ := { d = p_1 ... p_r | P(w,z) : p_1 > p_2 > ... > p_r,
>          p_1 ... p_m p_m^2 < D for all odd m },
> D^- := { ... p_1 ... p_m p_m^2 < D for all even m },
> E^+ := { e = p_1 ... p_r | P(w) : ... p_1 ... p_m p_m^beta < E for all
>          odd m },
> E^- := { ... p_1 ... p_m p_m^beta < E for all even m }.
> Now define the upper and lower bound linear sieve weights
> lambda^{+-}_d = mu(d) 1_{d in D^{+-}} and the upper and lower bound
> beta-sieve weights rho^{+-}_e = mu(e) 1_{e in E^{+-}}, so that, for any
> n in N, (see e.g. [7, Equations (6.26) and (6.27) with A = {n}])
> (14)  sum_{d|n} lambda^-_d <= 1_{(n,P(w,z))=1} <= sum_{d|n} lambda^+_d,
>       sum_{e|n} rho^-_e   <= 1_{(n,P(w))=1}   <= sum_{e|n} rho^+_e."

Remark 2.1 (why two sieves), verbatim (p. 5):

> "Remark 2.1. The reason that we do not use only the linear sieve is
> that using beta-sieve (with e.g. beta = 30) to sieve out primes
> < X^delta makes getting certain mean square estimates (like (49)
> below) easier. However it is suggested in [7, between Corollary 6.28
> and Proposition 6.29] that one could prove such mean square estimates
> also for the linear sieve alone.
>   On the other hand, the reason that we do not use only the beta-sieve
> with beta = 30 is that the linear sieve leads to superior sieving
> results -- in particular our lower bound for (13) would be negative if
> we only used the beta-sieve."

Vector-sieve lower bound (Section 2, (14)-(15), p. 6-7): the paper cannot
multiply the two lower bounds directly (both may be negative), so it uses
"a lower bound for 1_{(n,P(z))=1} that is familiar from the vector sieve
(see e.g. [11, Lemma 10.1])" -- combining lambda^+ with rho^-. The
combined weights alpha^{+-}_{k} are defined at (15)/(25).

Reduction to a main term + error (Section 2, (26)-(27), p. 8), verbatim:

> "(26)  M(z,y) >> 1 / log X
> and that
> (27)  int_{X/2}^{X} | E^{+-}(x,y,z) |^2 dx << h X."

Remark 2.2 (non-optimization, alternatives), verbatim (p. 8):

> "Remark 2.2. We have not optimized the level of distribution or the
> sieve weights as the current set-up suffices for obtaining P_2-numbers.
> As pointed out to the author by James Maynard and Maksym Radziwill, it
> might be possible to alternatively use Greaves' most sophisticated
> weighted sieve [10] together with Bettin-Chandee [1] estimates for
> Kloosterman sums. In this alternative approach the estimation of S_2
> from Proposition 5.1 below would be simpler whereas the sieve weights
> and thereby the estimation of S_1 would become more complicated.
>   On the other hand, after the completion of this work, the author
> realised, thanks to a comment by Andrew Granville, that it would
> probably suffice to use Kloosterman sum estimates based on the Weil
> bound as Mikawa [17] does. This would again simplify the treatment of
> S_2. However, our results in Section 5 give better bilinear level of
> distribution in almost all short intervals, which might be of benefit
> for other applications, so we have decided to keep the current
> approach."

---

## 5. THE MAIN TERM (Section 3): where >> h comes from

PARAPHRASE except quotes. The main-term bound M(z,y) >> 1/log X gives,
via the identity (p. 8) "sum_{n in A(x),(n,P(z))=1} w_n
>= h log X * M(z,y) + E^-(x,y,z) - E^+(x,y,z)", the lower bound
sum w_n >> h log X * (1/log X) = h. The main-term inequality reduces
(Section 3, p. 9) to a linear-sieve integral evaluated at
[7, Section 25.3 with s = 4, u = 10/9, eta = 1]:

> "M(z,y)/V(z) >= f(4) - sum_{z<p<=y} (1 - log p / log y) F(log(D/p)/log z)
> / p - 100 eps'"

leading (after PNT, substitution t = D^alpha) to the closed integral
(p. 9), verbatim:

> "M(z,y)/V(z) >= (e^gamma/2) log 3
>    - 2 e^gamma int_{1/4}^{9/10} ( 1 - (10 alpha)/9 )
>      ( 1/(4(1-alpha)) ) ( d alpha / alpha ) - 200 eps'
>    = (e^gamma/2)[ log 3 ( 1 - (1/log 3) log 27 ) - (10/9) log(15/2) ]
>      - 200 eps'."

and the paper concludes (p. 10):

> "By a numerical calculation and (32) below we see that indeed
> M(z,y) >> 1/log X once eps' is small enough."

Crucial level-of-distribution remark (Section 1.2 outline, p. 3-4),
verbatim:

> "here it is important that the level of distribution U = X^{5/9} is a
> sufficiently large power of X; dealing with the error terms would be
> substantially simpler for U = X^{1/2-eps} but the main term would be
> negative and thus the result useless."

So the whole difficulty is pushing the level of distribution U = X^{5/9}
(equivalently D = X^{5/9}) beyond X^{1/2}; the error-term estimates (5),
(6), (27) are the price of that.

---

## 6. THE DESHOUILLERS-IWANIEC INPUT (Sections 4, 5, 6)

PARAPHRASE except quotes. The "additional arithmetic information" that
the parity passage says is required to reach P_2 (as opposed to P_2
being classically out of reach for E_2) enters through averages of
Kloosterman sums. Two lemmas carry it.

Lemma 4.4 (p. 11), verbatim [display confirmed against rendered page,
flag 4]:

> "Let us finally record two lemmas that we use to bound averages of
> Kloosterman fractions. The first one is [5, Lemma 1] with rho = 1.
> Lemma 4.4. Let C, D, U, V >= 1 and |c(u,v)| <= 1. Then, for any
> eps > 0,
>   sum_{1<=c<=C} sum_{1<=d<=D,(c,d)=1} sum_{1<=u<=U} sum_{1<=v<=V,(v,c)=1}
>       c(u,v) e( u * (v d bar) / c )
>   << (CDUV)^{1/2+eps} ( (CD)^{1/2}
>        + (U+V)^{1/4} ( C D (U+V)(C+V^2) + U V^2 D^2 )^{1/4} )."

Lemma 4.5 (p. 11-12), verbatim [display confirmed against rendered page,
flag 4]:

> "The second one is an immediate consequence of [4, Theorem 12].
> Lemma 4.5. Let C, D, N, R, S >= 1/2 and let b_{n,r,s} be bounded
> complex coefficients. Let g : R^2 -> R be a smooth compactly supported
> function such that
> (34)  ( d^{nu_1+nu_2} / d x_1^{nu_1} d x_2^{nu_2} ) g(x_1,x_2)
>          <<_{nu_1,nu_2} 1  for every nu_1, nu_2 >= 0.
> Then, for any eps > 0,
>   sum_{R<r<=2R,(r,s)=1} sum_{S<s<=2S} sum_{0<n<=N}
>     sum_{c,d, (rd,sc)=1} b_{n,r,s} g( c/C, d/D ) e( n * (r d bar)/(s c) )
>   << (CD)^eps (NRS)^{1/2+eps}
>      ( C S (RS+N)(C+DR) + C^2 D S sqrt{ (RS+N) R + D^2 N R / S } )^{1/2}."

Reference identification (verbatim, p. 30 References):
- [4] = "J.-M. Deshouillers and H. Iwaniec. Kloosterman sums and Fourier
  coefficients of cusp forms. Invent. Math., 70(2):219-288, 1982/83."
  (Lemma 4.5 is an immediate consequence of [4, Theorem 12].)
- [5] = "J.-M. Deshouillers and H. Iwaniec. Power mean-values for
  Dirichlet's polynomials and the Riemann zeta-function. II. Acta
  Arith., 43(3):305-312, 1984." (Lemma 4.4 = [5, Lemma 1] with rho = 1.)

Where they enter (Section 6, p. 15-16), verbatim:

> "In order to estimate S_2 we shall use Lemmas 4.4 and 4.5 that are
> consequences of the work of Deshouillers and Iwaniec [4] on averages
> of Kloosterman sums. The following two lemmas and their proofs have
> very much in common with [2, Theorems 5 and 7] and [3, 5]."

The reduction structure (Section 1.2 outline, p. 4), verbatim:

> "Such sums can be estimated using the work of Deshouillers and Iwaniec
> [4] and its consequences. To apply these results, one needs some
> factorability properties of the coefficients lambda^-_{u_j}. Here we
> can utilize the well-factorability of the linear sieve coefficients."

For the upper-bound sum (6), the paper does not use well-factorability
(u is smaller) but instead (Section 1.2, p. 4), verbatim:

> "we can decompose the prime p by Vaughan's identity and again finish by
> applying suitable bounds for averages of Kloosterman fractions. Also we
> will need to argue somewhat more carefully to avoid lambda^+_{p,u}
> depending on p, making it to depend only on a dyadic-type interval to
> which p belongs."

Type II range (Lemma 5.3, p. 16), verbatim (the sparsity/length
conditions under which S_2 is handled):

> "Lemma 5.3. Let 2 <= H <= X^{1/60}, and let g be a smooth compactly
> supported function satisfying (1). Let alpha_m, beta_n and gamma_q be
> bounded complex coefficients and M, N, Q >= 1. Assume that
> (40)  N <= M << X^{21/50}  and  max{ M N, Q } << X^{14/25}."

---

## 7. THE h -> infinity MECHANISM

PARAPHRASE except quotes. The theorem is uniform over 2 <= h <= X^{1/100}
(and internally Lemma 5.3 requires H = h log X <= X^{1/60}). The role of
h -> infinity is entirely in converting the exceptional-set measure into
"almost all": Theorem 1.1 holds "for all x in (X/2, X] apart from an
exceptional set of measure O(X/h)" (p. 2). The proof gets this from the
L^2 (mean-square) error bounds:

> "(5)  int_{X/2}^{X} ( sum_u lambda^-_u E_u(x) )^2 dx << h X"

and

> "(6)  int_{X/2}^{X} ( sum ( 1 - log p/log y ) sum_u lambda^+_{u,p}
>        E_{pu}(x) )^2 dx << h X"

(p. 4), equivalently (27) int_{X/2}^{X} |E^{+-}(x,y,z)|^2 dx << h X
(p. 8). By Chebyshev, the set of x where the error exceeds a fixed
multiple of the main term h has measure O(hX / h^2) = O(X/h). Hence:
h -> infinity (however slowly) makes O(X/h) = o(X), i.e. "almost all".

The paper does NOT give an explicit statement of "what breaks first if h
is held bounded". The extractor's reading (flagged, see FLAGS): if h is
bounded, O(X/h) is a positive proportion of (X/2, X], so the conclusion
degrades from "almost all x" to "a positive proportion of x", and the
statement "almost all intervals contain a P_2" fails; the internal
estimates (5)-(6), (27) remain valid (they are h-uniform), but the
exceptional set is no longer o(X). No lower threshold on the growth rate
of h is imposed anywhere: any h -> infinity suffices, so the window
H = h log X can be as short as (log X) * w(X) for ANY w(X) -> infinity.

---

## 8. UNIFORMITY LEDGER (highest-value subsection)

What is fixed, what grows, what depends on what:

- X : the large parameter, X -> infinity. Everything is measured against
  x in (X/2, X]. The theorem holds for every X >= 2.
- h : the free window multiplier, constrained 2 <= h <= X^{1/100}
  (Theorem 1.1); internally H = h log X <= X^{1/60} is used (Lemma 5.3).
  h is UNIFORM: the constant c > 0 in ">= c h" and the implied constant
  in "O(X/h)" are ABSOLUTE (independent of h and X). h may grow
  arbitrarily slowly; the only use of h -> infinity is to make the
  exceptional-set measure O(X/h) = o(X).
- Window H = h log X. Because any h -> infinity is admissible, the
  achievable window is (log X) times ANY function tending to infinity;
  in particular H can be taken ~ (log X)(log log X), or much shorter
  (e.g. (log X) log log log X). This is the "very short" of the title:
  strictly shorter than the (log X)^{3.51} window previously available
  for P_2 (via Teravainen) and the (log X)^5 of Mikawa.
- The counted object is a P_2 number: Omega(n) <= 2 with the additional
  local restriction p|n => p > X^{1/8}. The "2" is a FIXED constant, not
  a growing rank. There is no tuple-rank / k-parameter anywhere.
- Sieve dimension: FIXED at 1 (linear sieve; f(4), F(s)=2e^gamma/s are
  the dimension-1 functions). The beta-sieve (beta = 30) is used only to
  sieve small primes p < X^delta and to ease mean-square estimates
  (Remark 2.1). No parameter of the argument is permitted to carry a
  growing sieve dimension.
- Level of distribution D = U = X^{5/9} (> X^{1/2}) is the essential
  quantitative pressure: at U = X^{1/2-eps} the main term M(z,y) would be
  negative (p. 4, p. 5 Remark 2.1). All the Kloosterman-sum work exists
  to license this super-X^{1/2} level for almost all x.
- Levels (10): D = X^{5/9}, z = D^{1/4} = X^{5/36}, y = D^{9/10} = X^{1/2},
  w = X^delta, E = X^{1/1000}. delta is a fixed small parameter chosen
  in terms of eps'.
- Constants: c (Theorem 1.1) absolute; all O(.) and <<, >> implied
  constants absolute unless subscripted (subscript = allowed dependence,
  e.g. O_k, <<_{nu_1,nu_2}). eps, eps' are arbitrary fixed small reals;
  thresholds (e.g. "delta small enough in terms of eps'") depend only on
  eps'.
- The result holds for EVERY X >= 2 (all scales), not merely on a sparse
  or unbounded subsequence of scales. There is no scale-selection and no
  auxiliary parameter s to be uniform over.
- Direction: TWO-SIDED. Lower bound >= c h is proved here; the matching
  upper bound = O(h) is quoted from [7, Corollary 6.28]. Both hold for
  almost all x with the same exceptional measure O(X/h).

---

## 9. What the paper does NOT contain (mandatory NOT-FOUND probes, Sec 4.4)

- "E_2 in the conclusion (as opposed to P_2)": NOT FOUND in the
  conclusion. The theorem's conclusion is a P_2 statement
  (1_{Omega(n)<=2}, "at most two primes"). E_2 appears only in the
  Introduction as background and as the object explicitly set aside by
  the parity barrier: "classical sieve methods can, in favourable
  circumstances, be used to show that a given set contains P_2 numbers,
  but to show that it contains E_2 numbers requires additional
  arithmetic information" (p. 1). No E_2 lower bound is claimed anywhere.

- "upper bound": FOUND (p. 2). The corresponding upper bound
  "sum_{ x-h log X < n <= x, p|n=>p>X^{1/8} } 1_{Omega(n)<=2} = O(h) for
  all x in (X/2, X] apart from an exceptional set of measure O(X/h)
  follows immediately from [7, Corollary 6.28]." It is an upper bound on
  the COUNT of P_2 numbers in the interval, quoted (not proved) from
  Friedlander-Iwaniec; it is not a bound on any word-grain or gap-word
  object.

- "growing sieve dimension": NOT FOUND. The sieve dimension is fixed at
  1 (linear sieve); the auxiliary beta-sieve has fixed beta = 30. No
  part of the argument is stated to tolerate a growing dimension.

- "consecutive": NOT FOUND in this text. The paper counts almost-primes
  in an interval; it makes no statement about consecutive primes or
  consecutive integers with a property.

- "any word-grain or pattern-conditioned quantity": NOT FOUND. No gap
  word, no tuple, no prescribed pattern, no class mass N_{P,d} of
  consecutive-gap words, no admissible-tuple hypothesis appears. (Grep
  over the full text: "tuple", "gap", "word", "pattern", "consecutive"
  return no mathematical occurrence.) The object throughout is
  1_{Omega(n)<=2} summed over an interval.

Additional negatives (checked, not on the mandatory list): no variance
or second-moment statement about the COUNT of P_2 numbers (the L^2 bounds
(5),(6),(27) are on sieve error terms E^{+-}(x), not on the count of
almost-primes); no singular series; no statement on an unbounded/sparse
scale sequence (the result is for all X); no rank/depth parameter.

---

## COMMENTARY (assessment, NOT extraction)

Consuming-context block (quoted verbatim as required):

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

C1. What this paper unconditionally supplies. An UNCONDITIONAL two-sided
count of P_2 numbers (Omega(n) <= 2, no prime factor below X^{1/8}) in
"very short" intervals: for almost all x in (X/2, X], the count in
(x - h log X, x] is asymp h, valid for every 2 <= h <= X^{1/100} with
absolute constants, exceptional measure O(X/h). The window is genuinely
logarithmic-scale: H = h log X with h -> infinity arbitrarily slowly, so
H can be taken ~ (log X)(log log X) -- exactly the project's A2 window --
or shorter. No hypotheses (no RH, no pair correlation). The arithmetic
input is Deshouillers-Iwaniec Kloosterman-sum averages ([4, Theorem 12],
[5, Lemma 1]) pushing the level of distribution to X^{5/9} > X^{1/2}.

C2. Why it is not a carrier -- the grain (A3) and rank (A1). The counted
object is an almost-prime count, 1_{Omega(n) <= 2}, a prime-count-type
grain. It is NOT the class mass N_{P,d} of consecutive-gap words the
project needs. There is no gap word, no tuple, no pattern-conditioning
(Section 9). Equally, the "2" of P_2 is a fixed constant, not a growing
rank k ~ (2/ln 2) lnln x; the paper has no rank parameter and no
mechanism to let one grow (the sieve dimension is fixed at 1, Section 8).
Both A1 and A3 are CG-non-relaxable axes, and both fail, so this cannot
be the located carrier regardless of how well A2/A5/A6 clear.

C3. The direction axis (A4). The paper is nominally a LOWER bound
(interval contains a P_2), but it also records the matching upper bound
sum 1_{Omega(n)<=2} = O(h) for almost all x (p. 2, from [7, Corollary
6.28]). That upper bound is an upper-uniformity statement on the count of
P_2 numbers -- in FORM the "upper / non-concentration" direction the
project wants -- but on the wrong object (P_2 counts, not gap-word class
mass off a modal middle). It is a Gallagher/sieve-type uniform ceiling,
not a non-concentration of any distribution over middle slots.

C4. Strength (A5) and density (A6). The bounds are constant-order:
>= c h and = O(h) with absolute c and implied constant -- exactly the
"constant order suffices" strength A5 asks for. On density, the result is
STRONGER than the project needs: it holds for every X >= 2, i.e. on all
scales, not merely an unbounded sparse subsequence, and there is no
auxiliary parameter s to be uniform over. So A6 clears trivially (all
scales dominate any sparse subset). But A5 and A6 are the two axes CG
already relaxes, so clearing them carries no campaign weight; the binding
failures remain A1 (rank) and A3 (grain).

C5. Relation to the parity boundary the project keeps hitting. This paper
contains the cleanest located statement of that boundary in an author's
own words (Section 2, p. 1): P_2 is reachable by classical (type-I) sieve
methods precisely because "the parity barrier does not apply" to P_k,
whereas E_2 "requires additional arithmetic information." For the
project's word-grain, D0-depth site-mass question, this is the negative
diagnostic: the technology that makes very-short-interval almost-prime
counts unconditional (weighted sieve + Kloosterman averages) is exactly
the technology the parity barrier confines to P_k / type-I information,
and it does not transfer to a middle-slot statement about
consecutive-gap words (which is a pattern/parity-sensitive, E_k-side
object). The paper's own framing (its aim is Friedlander-Iwaniec's "at
most two prime divisors", p. 1) confirms the object is P_2, not any
gap-word or exchange configuration.

Per-axis verdict (exactly one of CLEARS / FAILS (reason) / NOT
APPLICABLE for each):

- A1 (rank k ~ (2/ln 2) lnln x): FAILS (no rank parameter; the "2" of
  P_2 is a fixed constant, sieve dimension fixed at 1, nothing grows).
- A2 (window h ~ (ln x)(lnln x)): CLEARS (H = h log X with any
  h -> infinity, so ~ (log X)(log log X) is admissible, indeed can be
  shorter).
- A3 (grain = class masses of consecutive-gap words, not prime counts):
  FAILS (grain is an almost-prime count 1_{Omega(n)<=2}; no gap word, no
  class mass, no pattern-conditioning).
- A4 (direction = upper / non-concentration): FAILS (the located upper
  bound O(h) is on P_2 COUNTS via [7, Cor. 6.28], not a non-concentration
  of gap-word class mass off a modal middle; the headline is a lower
  bound).
- A5 (strength = constant order suffices): CLEARS (bounds are asymp h
  with absolute constants).
- A6 (density = sparse scales, no s-uniformity): CLEARS (holds for every
  X >= 2, i.e. all scales; no s parameter to be uniform over).

Clears all six axes: NO (A1, A3, A4 fail; A1 and A3 are CG-non-relaxable).
Not a located carrier.

Even-Cramer-smooth deterministic gap system (q_1=2, q_2=3, q_3=5, q_4=7,
q_{n+1}=q_n+2*ceil(ln q_n / 2)): UNTESTED against it. The paper makes no
claim about any deterministic gap model; its object (counts of P_2
integers in genuine short intervals of the natural numbers) is orthogonal
to that construction, and nothing in the text bears on whether the result
would hold or fail there. Untested, not a guess.

---

## FLAGS (consolidated)

1. [PRINTED-ODDITY] The paper defines "e(u) := e(2*pi*i*u)" (p. 2), an
   apparent typo where e(.) is defined in terms of e (the intended
   meaning is e(u) := e^{2*pi*i*u}, the standard additive-character
   convention). Transcribed as printed.

2. [PRINTED-ODDITY] Acknowledgments (p. 30) read "The author is greatful
   to John Friedlander..." -- "greatful" as printed (for "grateful").

3. [TRANSCRIPTION-UNSURE, resolved-by-context] In (14)/(15) and (24)/(25)
   the products "d|P(w.z)" appear with a period rather than a comma
   between w and z in the pdftotext layer (should read P(w,z)); resolved
   by context (the set P(w,z) = prod_{w<=p<z} p is defined explicitly at
   Section 2 p. 5). Transcribed as P(w,z).

4. [TRANSCRIPTION-UNSURE, resolved-by-image] The multi-line displays --
   Theorem 1.1 and its upper-bound companion (p. 2), Lemma 4.4 and Lemma
   4.5 (p. 11-12) -- have subscripts and the Kloosterman argument
   e(u*(vd bar)/c), e(n*(rd bar)/(sc)) partly scrambled in the pdftotext
   layer. Theorem 1.1 and the p.2 upper bound were transcribed from the
   rendered page image (pdftoppm -r 200, page 2) and confirmed exact.
   Lemmas 4.4/4.5 were transcribed by cross-checking the -layout text
   layer against the rendered page; the bar over the modular inverse
   (d bar = inverse of d mod the relevant modulus, per Section 1.1
   convention) is rendered "d bar" here.

5. [TRANSCRIPTION-UNSURE, resolved-by-context] The definition sets
   D^{+-}, E^{+-} (Section 2, p. 5) use "p_1 ... p_m p_m^2 < D" and
   "p_1 ... p_m p_m^beta < E"; the exponents on the last factor (2 for
   the linear-sieve level condition, beta for the beta-sieve) are small
   glyphs but consistent with the standard Friedlander-Iwaniec
   well-factorable / beta-sieve construction referenced ([7, (6.26),
   (6.27)]). Transcribed as read.

6. Extractor observation (NOT in the paper): the "what breaks if h
   bounded" reading in Section 7 (exceptional set O(X/h) becomes a
   positive proportion, so "almost all" fails while the h-uniform
   estimates (5)-(6) survive) is the extractor's inference from the
   quoted measure bound, not a sentence the paper states. The paper only
   asserts the positive direction: h -> infinity => almost all.

7. The paper has an Abstract and numbered Sections 1-7 with Theorem 1.1,
   Propositions, and Lemmas; there is exactly one numbered theorem
   (Theorem 1.1). Sections 5-7 (Type I/II sums, proof of (27)) were read
   for the DEshouillers-Iwaniec entry points (Lemmas 4.4/4.5, Lemma 5.3,
   Proposition 5.1) but not transcribed display-by-display, as Section
   4.4 of the dispatch scopes this extract to the parity passage and the
   sieve input.
