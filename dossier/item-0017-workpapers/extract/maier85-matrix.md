# EXTRACTION: Helmut Maier, "Primes in short intervals"

Source (only evidence base): /home/istr/pro/erdos251/dossier/Maier-Primes-in-short-intervals.pdf
Journal id as printed on p. 221 (footnote): "Received May 11, 1984. Michigan Math. J. 32 (1985)."
Author as printed: Helmut Maier, Department of Mathematics, University of Michigan,
Ann Arbor, Michigan 48109 (address block, p. 225). Printed pages 221-225
(5 printed pages; the PDF has 6 pages, page 6 blank). SCAN WITH NO TEXT LAYER:
everything below was transcribed from page images (Read tool rasterization).

Transcription conventions: ASCII only. Math in LaTeX-like ASCII: \pi(x) = prime
counting function, \pi(x, q, a) = primes <= x congruent a mod q (comma notation
as printed), \Phi(x) = the short-interval length function of the theorem,
\Phi(x, y) = the sifting function |{n <= x : (n, P(y)) = 1}| (the paper overloads
\Phi; both uses transcribed as printed), P(z) = \prod_{p<z} p, W(z) =
\prod_{p<z} (1 - 1/p), \varphi = Euler phi, \omega(u) = Buchstab function,
\gamma = Euler's constant, li = logarithmic integral, [x] = integer part,
{...}^{\lambda} = brace grouping as printed, <= >= != for inequality/inequation
glyphs, oo = \infty. The matrix symbol printed as Fraktur M is transcribed as M.
Anchors are the paper's own numbered displays ((1.1), (2.1)-(2.4), (3.1)),
lemma/theorem labels, and section numbers; printed page numbers (221-225) are
the secondary anchor for unnumbered displays. Every formula was transcribed
from the raster images; inline [TRANSCRIPTION-UNSURE: ...] flags mark any glyph
not fully certain.

Everything up to the final section is EXTRACTION (what the paper says).
Commentary appears ONLY in the final marked section.

---

## 1. FRONT MATTER AND MAIN THEOREM (verbatim)

The paper has NO abstract; it opens directly with Section 1 (Introduction),
p. 221. Opening framing (Section 1, p. 221), verbatim:

> "1. Introduction. The distribution of primes in short intervals is an
> important problem in the theory of prime numbers. The following question is
> suggested by the prime number theorem: for which functions \Phi is it true
> that
>
> (1.1)  \pi(x + \Phi(x)) - \pi(x) ~ \Phi(x)/log x  (x -> oo)?"

Known bounds cited (p. 221), verbatim:

> "Heath-Brown [4] proved that one can choose \Phi(x) = x^{7/12 - \epsilon(x)}
> (\epsilon(x) -> 0, as x -> oo), which is a slight improvement of Huxley's
> result [5], \Phi(x) = x^{7/12 + \epsilon} (\epsilon > 0 fixed). The Riemann
> hypothesis implies that one can take \Phi(x) = x^{1/2 + \epsilon}. There is a
> large gap between these upper bounds and the known lower bounds of \Phi(x).
> It follows from [9] that (1.1) is wrong if
>
> \Phi(x) = log x (log log x log log log log x / (log log log x)^2)."

(Reference [9] is Rankin, "The difference between consecutive prime numbers",
J. London Math. Soc. 13 (1938), 242-247; see Section 6 below.) Continuation
(p. 221), verbatim:

> "A slight improvement is implicit in the author's paper [7]."

Selberg input (p. 221), verbatim:

> "On assumption of the Riemann hypothesis this gap can be narrowed consider-
> ably if an exceptional set of x-values is admitted. In 1943, A. Selberg [10]
> proved that, on assumption of the Riemann hypothesis, (1.1) is true for
> almost all x if \Phi(x)/(log x)^2 -> oo (x -> oo). By "for almost all values
> of x" is meant that x -> oo through any sequence lying outside a certain
> exceptional set E of x-values, for which the Lebesgue measure of
> E \cap (0, u] is o(u) for u -> oo. It is known unconditionally that (1.1) is
> true for almost all x if \Phi(x) = x^{1/6 + \epsilon}. This is implicit in
> the work of Huxley [5]."

[TRANSCRIPTION-UNSURE: the exceptional set symbol is a script/rounded capital E
in print, transcribed E.]

Purpose statement (p. 221), verbatim:

> "A natural question is whether Selberg's result is true without exceptions.
> The purpose of this paper is to show that exceptions do exist even for
> functions \Phi(x) growing considerably faster than (log x)^2.
> We prove the following."

MAIN THEOREM (p. 221), verbatim (the paper's only theorem; italics in
original for "Let ... Then" and the display conditions):

> "THEOREM. Let \Phi(x) = (log x)^{\lambda_0}, \lambda_0 > 1. Then
>
> lim sup_{x -> oo} (\pi(x + \Phi(x)) - \pi(x)) / (\Phi(x)/log x) > 1
> and
> lim inf_{x -> oo} (\pi(x + \Phi(x)) - \pi(x)) / (\Phi(x)/log x) < 1.
>
> For the range 1 < \lambda_0 < e^\gamma we have even
>
> lim sup_{x -> oo} (\pi(x + \Phi(x)) - \pi(x)) / (\Phi(x)/log x)
>   >= e^\gamma / \lambda_0,
>
> where \gamma denotes Euler's constant."

The proof (Section 3) refers to these as the "first part" (lim sup > 1),
"second part" (lim inf < 1), and "third part" (lim sup >= e^\gamma/\lambda_0).

Closing of the introduction (p. 221), verbatim:

> "Most of the principles of the proof already appear in [7]. At some places
> however we need sharper estimates."

(Reference [7] is Maier, "Chains of large gaps between consecutive primes",
Adv. in Math. 39 (1981), 257-269.)

---

## 2. SECTION 2, BASIC LEMMAS: GOOD MODULI AND GALLAGHER INPUT

Good modulus definition (Section 2, p. 222), verbatim:

> "2. Basic lemmas. Following [7] we call an integer q > 1 a "good" modulus if
> L(s, \chi) != 0 for all characters \chi mod q and all s with
>
> \sigma > 1 - C/log|q(|t|+1)|."

[TRANSCRIPTION-UNSURE: the print shows "L(s, \chi| != 0" with what appears to
be a vertical bar where a closing parenthesis is expected; transcribed as
L(s, \chi) != 0 (the only reading that parses). Also the log argument is
printed with outer vertical bars, "log|q(|t|+1)|"; possibly intended as
log(q(|t|+1)).]

Page's theorem dichotomy (p. 222), verbatim:

> "This definition depends on C > 0. However, if C is sufficiently small, then
> we have: For all q > 1, either q is good or there is an exceptional real
> zero of some quadratic character mod q. In the latter case the exceptional
> zero and character are unique (Page's theorem, cf. [8, Satz 6.9b])."

Definition (p. 222), verbatim: "We define P(z) = \prod_{p < z} p."

LEMMA 1 (p. 222), verbatim:

> "LEMMA 1. There is a constant C > 0 such that, in terms of C, there exist
> arbitrarily large values of z for which the modulus P(z) is good.
>
> Proof. This is Lemma 1 of [7]."

Followed by (p. 222, verbatim): "The constant C will be fixed throughout the
rest of the paper such that the conclusion of Lemma 1 is true."

LEMMA 2 (p. 222), verbatim:

> "LEMMA 2 (Gallagher). Let q be a good modulus. Then
>
> \pi(x + h, q, a) - \pi(x, q, a)
>   = (1/\varphi(q)) (li(x + h) - li x) (1 + O(e^{-cD} + e^{-\sqrt{log x}})),
>
> provided (a, q) = 1, x >= q^D, and x/2 <= h <= x, where log q >= D >= D_0.
> (Here the constant D_0 > 0 and the constant implied in O( ) depend only on C
> in Lemma 1; c > 0 is an absolute constant.)
>
> Proof. This follows if we combine the proof of Lemma 2 in [7] with the prime
> number theorem in the form \pi(x) = li x (1 + O(e^{-\sqrt{log x}}))."

(The Gallagher attribution points to reference [3]: P. X. Gallagher, "A large
sieve density estimate near \sigma = 1", Invent. Math. 11 (1970), 329-339; the
lemma itself is imported through Lemma 2 of [7].)

Sifting-function definitions (p. 222), verbatim:

> "We set
> \Phi(x, y) = |{n <= x : (n, P(y)) = 1}|,   W(z) = \prod_{p < z} (1 - 1/p)."

LEMMA 3 (p. 222), verbatim:

> "LEMMA 3 (Buchstab). Let \lambda > 1. Then
>
> lim_{z -> oo} z^{-\lambda} W(z)^{-1} \Phi(z^\lambda, z)
>   = e^\gamma \omega(\lambda),
>
> where \omega(u) is defined by
>
> (2.1)  \omega(u) = u^{-1},  1 <= u <= 2,
>        (d/du)(u \omega(u)) = \omega(u - 1),  u >= 2,
>
> and where the right-hand derivative has to be taken at u = 2.
>
> Proof. This follows from [2] and from Mertens' formula
>
> \prod_{p < z} (1 - 1/p) ~ e^{-\gamma} / log z.
>
> A uniform result has been proven in [1]."

([2] = Buchstab 1937, [1] = de Bruijn 1950; see Section 6.)

---

## 3. SECTION 2, LEMMA 4: OSCILLATION OF THE BUCHSTAB FUNCTION

LEMMA 4 (p. 223), verbatim:

> "LEMMA 4. The function \omega(u) - e^{-\gamma} changes sign in any interval
> [a - 1, a], a >= 2."

Proof anatomy (p. 223). Opening, verbatim:

> "Proof. This has been established in [6] for the general sieve of
> Eratosthenes. For the convenience of the reader, however, we give a more
> specific argument which in [1] is already applied to the problem of the
> convergence of \omega(u), (u -> oo)."

([6] = Iwaniec, "The sieve of Eratosthenes-Legendre", Ann. Scuola Norm. Sup.
Pisa Cl. Sci. (4) 4 (1977), 257-268.) The adjoint function (p. 223), verbatim:

> "We set
>
> h(u) = \int_0^oo exp(-ux - x + \int_0^x (e^{-t} - 1)/t dt) dx.
>
> Then one easily checks that
>
> (2.2)  h is analytic for u > -1,
>        u h'(u - 1) + h(u) = 0,
>        h(u) ~ 1/u as u -> oo."

(Internal consistency check performed during extraction: with f as below,
f'(a) = \omega(a)(h(a) + a h'(a - 1)), so (2.3) is exactly equivalent to the
middle line of (2.2); the transcription u h'(u-1) + h(u) = 0 is confirmed by
this cross-check.) Continuation (p. 223), verbatim:

> "Let f(a) = \int_{a-1}^a \omega(u) h(u) du + a \omega(a) h(a - 1). From
> (2.1) and (2.2) it is easily verified that
>
> (2.3)  f'(a) = 0 for all a >= 2.
>
> By [1] we have that lim_{u -> oo} \omega(u) = e^{-\gamma}. Therefore
> f(a) -> e^{-\gamma} as a -> oo which together with (2.3) implies that
>
> (2.4)  \int_{a-1}^a \omega(u) h(u) du + a \omega(a) h(a - 1) = e^{-\gamma}."

Then (p. 223), verbatim:

> "Now let
>
> g(a) = \int_{a-1}^a h(u) du + a h(a - 1).
>
> From (2.2) it is easily seen that g'(a) = 0 for all a > 0. Since g(a) -> 1
> as a -> oo, we have:
>
> \int_{a-1}^a h(u) du + a h(a - 1) = 1.
>
> This together with (2.4) gives:
>
> \int_{a-1}^a (\omega(u) - e^{-\gamma}) h(u) du
>   + a (\omega(a) - e^{-\gamma}) h(a - 1) = 0.
>
> Since h > 0 it follows that either \omega(u) == e^{-\gamma} in [a - 1, a] or
> there is a sign-change of \omega(u) - e^{-\gamma} in [a - 1, a]. But the
> first alternative would imply that \omega(u) == e^{-\gamma} in [1, oo).
> This concludes the proof of Lemma 4."

(== transcribes the printed identity sign.) Acknowledgment (p. 225), verbatim:

> "ACKNOWLEDGMENT. The author wishes to thank Professors H. L. Montgomery and
> R. C. Vaughan for pointing out to him the proof of Lemma 4."

---

## 4. SECTION 3: THE MAIER MATRIX CONSTRUCTION (proof of the theorem)

Setup (pp. 223-224), verbatim (sentence runs across the page break):

> "3. Proof of the theorem. We now fix an integer D >= D_0 depending at most
> on \epsilon > 0 to be introduced later. In the sequel we assume that z -> oo
> through a set of z for which P(z) is a good modulus in the sense of Lemma 1
> and that z >= e^{cD}, where c is the constant in Lemma 2. We also choose an
> integer U = U(z), such that U <= P(z)."

The matrix (p. 224), verbatim:

> "We consider the matrix
>
> M = (a_{rs}), where
> a_{rs} = s + r P(z),  1 <= s <= U,  P(z)^{D-1} < r <= 2 P(z)^{D-1}.
>
> We want to estimate the number of primes in M which we denote by \pi(M).
> The rows of M are intervals of U consecutive integers, whereas the columns
> of M are arithmetic progressions with common difference P(z). Only those
> columns for which (s, P(z)) = 1 contain primes. We call such columns
> admissible."

(M is Fraktur in print. Row r is the translate (r P(z), r P(z) + U] of the
initial window; there are P(z)^{D-1} rows and U columns. Paraphrase, this
sentence only.)

Column count via Lemma 2 (p. 224), verbatim:

> "The number of primes in an admissible column is, by Lemma 2:
>
> \pi(2 P(z)^D + s, P(z), s) - \pi(P(z)^D + s, P(z), s)
>   = (P(z)^D / (\varphi(P(z)) log(P(z)^D))) (1 + O(e^{-cD}))
>   = (P(z)^{D-1} / log(P(z)^D)) W(z)^{-1} (1 + O(e^{-cD}))."

(Consistency check: P(z)^D/\varphi(P(z)) = P(z)^{D-1} W(z)^{-1} because
\varphi(P(z))/P(z) = W(z); both printed lines agree.)

Total prime count (p. 224), verbatim:

> "Let the number of admissible columns be U W(z) c(U, z). Then we have
>
> (3.1)  \pi(M) = (P(z)^{D-1} / log(P(z)^D)) U c(U, z) (1 + O(e^{-cD}))."

(The number of admissible columns is exactly \Phi(U, z), so by Lemma 3 with
U = [z^\lambda], c(U, z) -> e^\gamma \omega(\lambda) as z -> oo. Paraphrase;
the paper invokes this as "By (3.1) and Lemma 3" in the next quote.)

First part: overshoot row selection (p. 224), verbatim:

> "Now we can conclude the proof of the theorem. To prove the first part we
> fix \lambda_1 > \lambda_0 such that \omega(\lambda_1) > e^{-\gamma}, which
> is possible by Lemma 4. We choose U = [z^{\lambda_1}]. By (3.1) and Lemma 3
> there is at least one row of M with at least
>
> (U / log(P(z)^D)) e^\gamma \omega(\lambda_1) (1 + O(e^{-cD})) primes."

Subinterval selection (p. 224), verbatim:

> "We now set l_0 = {log(P(z)^D)}^{\lambda_0} and divide this row into
> K_0 = [U/l_0] + 1 subintervals of equal length l_0 (1 + o(1)). At least one
> of these subintervals, say (a_l, b_l], contains at least
>
> r = (U / (K_0 (log(P(z)^D)))) e^\gamma \omega(\lambda_1) (1 + O(e^{-cD}))
> primes."

[TRANSCRIPTION-UNSURE: the subscript on (a_l, b_l] is a single italic letter
that could be l or i; transcribed l throughout, consistently with "x = a_l"
below.]

Landing the short interval (p. 224), verbatim:

> "We set x = a_l and obtain (a_l, b_l] \subseteq (x, x + \Phi(x)]. Thus the
> interval (x, x + \Phi(x)] contains at least
>
> r = (\Phi(x)/log x) e^\gamma \omega(\lambda_1) (1 + O(e^{-cD})) primes.
>
> For any given \epsilon > 0 we can fix D such that
> r >= (\Phi(x)/log x)(e^\gamma \omega(\lambda_1) - \epsilon), which
> concludes the proof of the first part of the theorem."

Third part (p. 224), verbatim:

> "The third part immediately follows by observing that \omega(u) = u^{-1}
> for 1 <= u <= 2."

(For 1 < \lambda_0 < e^\gamma one can take \lambda_1 in (\lambda_0, e^\gamma)
with \lambda_1 <= 2, so e^\gamma \omega(\lambda_1) = e^\gamma/\lambda_1 ->
e^\gamma/\lambda_0 as \lambda_1 -> \lambda_0; \omega(\lambda_1) > e^{-\gamma}
is automatic there since e^\gamma/\lambda_1 > 1. Paraphrase, this sentence
only; the paper gives only the one-line remark quoted above.)

Second part: undershoot (pp. 224-225), verbatim (display crosses the page
break to p. 225):

> "The proof of the second part is completely analogous to the proof of the
> first part. We choose \lambda_2 > \lambda_0 such that
> \omega(\lambda_2) < e^{-\gamma} and set U = [z^{\lambda_2}]. There is at
> least one row of M with at most
>
> (U / log(P(z)^D)) e^\gamma \omega(\lambda_2) (1 + O(e^{-cD})) primes.
>
> We set l_1 = {log(2 P(z)^D)}^{\lambda_0} and divide this row into
> K_1 = [U/l_1] subintervals of equal length. An easy computation similar to
> the one above shows that at least one of these subintervals contains an
> interval (x, x + \Phi(x)] with at most
> (\Phi(x)/log x)(e^\gamma \omega(\lambda_2) + \epsilon) primes. This
> concludes the proof."

---

## 5. QUANTITATIVE SKELETON (collected, with anchors)

Connective-tissue summary (paraphrase, each item anchored to the verbatim
quotes above):

- Modulus: Q = P(z) = \prod_{p < z} p, required to be a good modulus; good z
  exist arbitrarily large but only along an unspecified sequence (Lemma 1,
  p. 222).
- Scale: rows live at height x ~ P(z)^D, since P(z)^{D-1} < r <= 2 P(z)^{D-1}
  (matrix definition, p. 224); Lemma 2 needs x >= q^D and log q >= D >= D_0
  (p. 222); additionally z >= e^{cD} (p. 224).
- D is a FIXED integer chosen from \epsilon alone ("We now fix an integer
  D >= D_0 depending at most on \epsilon > 0", p. 223; "For any given
  \epsilon > 0 we can fix D", p. 224). All error terms are 1 + O(e^{-cD}),
  a fixed relative error, shrunk only by enlarging the fixed D.
- Row length: U = [z^{\lambda_1}] or [z^{\lambda_2}] with U <= P(z)
  (pp. 223-224); target window length l_0 = {log(P(z)^D)}^{\lambda_0}
  (p. 224) resp. l_1 = {log(2 P(z)^D)}^{\lambda_0} (p. 225), which is
  (log x)^{\lambda_0} (1 + o(1)) at the landing point x = a_l.
- Deviation source: e^\gamma \omega(\lambda) vs. 1, i.e. the Buchstab
  oscillation \omega(\lambda) - e^{-\gamma} of Lemma 4 (p. 223), entering
  through the admissible-column density c(U, z) -> e^\gamma \omega(\lambda)
  (Lemma 3, p. 222, applied at (3.1), p. 224).
- Selection: two pigeonhole steps, over rows and then over subintervals
  (both p. 224); both are pure averaging, no localization.

---

## 6. REFERENCES AS PRINTED (p. 225, verbatim, condensed lineation)

> "1. N. G. de Bruijn, On the number of uncancelled elements in the sieve of
> Eratosthenes, Nederl. Akad. Wetensch. Proc. 53 (1950), 803-812.
> 2. A. A. Buchstab, Asymptotic estimates of a general number-theoretic
> function (Russian), Mat.-Sb. (N.S.) 2(44) (1937), 1239-1246.
> 3. P. X. Gallagher, A large sieve density estimate near \sigma = 1, Invent.
> Math. 11 (1970), 329-339.
> 4. D. R. Heath-Brown, Differences between consecutive primes. Seminar on
> Number Theory, 1979-80 (French), Exp. No. 14, Univ. Bordeaux I, Talence,
> 1980.
> 5. M. N. Huxley, On the difference between consecutive primes, Invent.
> Math. 15 (1972), 164-170.
> 6. H. Iwaniec, The sieve of Eratosthenes-Legendre, Ann. Scuola Norm. Sup.
> Pisa Cl. Sci. (4) 4 (1977), 257-268.
> 7. H. Maier, Chains of large gaps between consecutive primes, Adv. in
> Math. 39 (1981), 257-269.
> 8. K. Prachar, Primzahlverteilung, Springer, Berlin, 1957.
> 9. R. A. Rankin, The difference between consecutive prime numbers,
> J. London Math. Soc. 13 (1938), 242-247.
> 10. A. Selberg, On the normal density of primes in small intervals and the
> difference between consecutive primes, Arch. Math. Naturvid. 47 (1943),
> 87-105."

---

## COMMENTARY (assessment, NOT extraction)

Consuming context: the project needs an UNCONDITIONAL supply of two
prime-gap-word sites with matched J-prefix and K-suffix windows and a
dominant weighted middle difference, at depths J, K ~ log2 log x (exchange
configuration), against blockers (i) pigeonhole blindness to variability,
(ii) parity-blocked gap-pattern prescription, (iii) circular Shiu-string
densities.

### Focus 1: the main theorem, exact constants and exponent conditions

Theorem, p. 221 (Section 1 above): for \Phi(x) = (log x)^{\lambda_0} with
\lambda_0 > 1, lim sup of (\pi(x + \Phi(x)) - \pi(x))/(\Phi(x)/log x) is > 1
and lim inf is < 1; and in the range 1 < \lambda_0 < e^\gamma (e^\gamma
approx 1.7811) the lim sup is >= e^\gamma/\lambda_0. Those are all the stated
constants; no numeric lim inf constant is stated in the theorem (the proof of
the second part actually delivers <= e^\gamma \omega(\lambda_2) + \epsilon for
any \lambda_2 > \lambda_0 with \omega(\lambda_2) < e^{-\gamma}, p. 225, but
the theorem records only "< 1"). Exponent condition \lambda_0 > 1 is sharp for
the method as run here: the window l_0 = {log(P(z)^D)}^{\lambda_0} must be
o(U) with U = z^{\lambda_i}, \lambda_i slightly above \lambda_0, and the
Buchstab deviation \omega(\lambda) - e^{-\gamma} is only nonzero for finite
\lambda; at \lambda_0 = 1 the paper has nothing new and cites Rankin [9] for
the failure of (1.1) at \Phi(x) = log x (log log x log log log log x /
(log log log x)^2) (p. 221).

### Focus 2: the matrix construction, step-anchored

(a) Matrix: M = (a_{rs}), a_{rs} = s + r P(z), 1 <= s <= U <= P(z),
P(z)^{D-1} < r <= 2 P(z)^{D-1} (p. 224). Rows = translates (r P(z),
r P(z) + U] of one window by consecutive multiples of the smooth modulus
P(z); columns = progressions s mod P(z). This is exactly a "progression
translates over a cycle of a smooth modulus" double array: r indexes the
translate, s the position in the window.
(b) Admissibility: a column contains primes only if (s, P(z)) = 1 (p. 224);
the admissible-position set is the SAME in every row.
(c) Analytic input: per admissible column, Lemma 2 (Gallagher, p. 222,
imported from Lemma 2 of [7] + PNT) gives (P(z)^{D-1}/log(P(z)^D)) W(z)^{-1}
(1 + O(e^{-cD})) primes, valid because P(z) is a good modulus (Lemma 1,
p. 222, resting on Page's theorem [8, Satz 6.9b]) and x ~ P(z)^D = q^D.
(d) Combinatorial input: the number of admissible columns is \Phi(U, z) =
U W(z) c(U, z), and Lemma 3 (Buchstab, p. 222) gives c(U, z) -> e^\gamma
\omega(\lambda) for U = [z^\lambda]; the W(z)^{-1} from (c) cancels the W(z)
from (d) in (3.1) (p. 224), so the density surplus/deficit is the pure factor
e^\gamma \omega(\lambda).
(e) Oscillation input: Lemma 4 (p. 223, the h(u)-adjoint argument, (2.2)-
(2.4)) guarantees BOTH signs: \lambda_1 with \omega(\lambda_1) > e^{-\gamma}
and \lambda_2 with \omega(\lambda_2) < e^{-\gamma} exist arbitrarily close to
any \lambda_0 (sign change in every [a-1, a]).
(f) Selection: pigeonhole over the P(z)^{D-1} rows (p. 224), then pigeonhole
over K_0 = [U/l_0] + 1 (resp. K_1 = [U/l_1]) subintervals of the selected row
(pp. 224-225); landing x = a_l.

### Focus 3: what the method can prescribe -- counts only, never gap values

No step forces gap VALUES. The two selection steps are pure averaging
("there is at least one row of M with at least ...", "At least one of these
subintervals, say (a_l, b_l], contains at least r ... primes", p. 224): they
assert existence of a row/subinterval meeting the AVERAGE, with both the row
index r and the landing point x = a_l existential and uncontrolled. The only
structure that is genuinely prescribed is the admissibility pattern
{s <= U : (s, P(z)) = 1} (p. 224) -- a divisibility skeleton that constrains
where primes CAN sit, identically in every row; occupancy of those slots is
controlled only in aggregate (per column, via Lemma 2, i.e. on average over
the P(z)^{D-1} rows). Consequently the output is a COUNT deviation in a
translated interval (x, x + \Phi(x)], from which gap information follows only
in averaged form (an interval with fewer than expected primes must contain
some gap above average size, etc.); no individual gap value, no gap word, and
no relative position of primes inside the window is ever fixed. This matches
the consuming context's blocker (ii): upgrading admissibility-pattern control
to occupancy-pattern control is exactly a prescribed-gap-pattern (tuple-type)
lower bound, which this paper never attempts.

### Focus 4: modulus/scale coupling and forced ranges

The modulus is Q = P(z) = \prod_{p < z} p, so log Q = \theta(z) ~ z
(Chebyshev/PNT; inference, not stated in the paper). Forced ranges, all from
the extraction: x >= q^D with log q >= D >= D_0 (Lemma 2, p. 222); the matrix
places x in (P(z)^D, 2 P(z)^D + U] (p. 224), so Q = x^{1/D} up to bounded
factors -- the modulus is a FIXED positive power of x, gigantic relative to
every other scale. The row length is U = [z^{\lambda_i}] <= P(z) (pp. 223-
224), i.e. U ~ (log Q)^{\lambda_i} ~ (log x / D)^{\lambda_i}; the target
window is l_0 = {log(P(z)^D)}^{\lambda_0} ~ (log x)^{\lambda_0} (p. 224). So
the hierarchy is: window (log x)^{\lambda_0} < row (log x)^{\lambda_1 or 2}
(strictly bigger exponent) << modulus Q = x^{1/D} << x. The sieve depth z
satisfies z ~ log x / D: the primes dividing the modulus go up to essentially
log x. Rigidity: D must remain a FIXED integer (chosen from \epsilon,
pp. 223-224), because the relative error is O(e^{-cD}) and Lemma 2 needs
x ~ q^D with D bounded; and z is confined to the sparse good-modulus sequence
of Lemma 1. Hence only lim sup/lim inf statements (a sparse x-sequence), never
a positive-density or all-x statement.

### Assessment against the exchange-configuration target

What this machinery CAN supply, unconditionally:
1. Variability itself -- the exact thing blocker (i) says pigeonhole cannot
   see. Lemma 4 plus (3.1) manufactures count deviations of a FIXED
   multiplicative size (e^\gamma \omega(\lambda_1) - \epsilon above,
   e^\gamma \omega(\lambda_2) + \epsilon below the expected \Phi/log x) at
   window length (log x)^{\lambda_0}, \lambda_0 > 1. The input is a zero-free
   region (Lemma 1/Page + Gallagher via [7]), not any gap statistic, so it is
   NON-circular in the sense of blocker (iii): nothing presupposed about gap
   words at the target depth.
2. Two site types at a COMMON scale and common modulus: the overshoot run
   (U = [z^{\lambda_1}]) and undershoot run (U = [z^{\lambda_2}]) use the
   same good z, same P(z), same row range P(z)^{D-1} < r <= 2 P(z)^{D-1};
   both sites land in (P(z)^D, 2 P(z)^D + U]. So Maier gives, for infinitely
   many scales, a PAIR of intervals of identical length ~ (log x)^{\lambda_0}
   at comparable height whose prime counts differ by the fixed factor pair
   (e^\gamma \omega(\lambda_1), e^\gamma \omega(\lambda_2)) -- a "dominant
   middle difference" in COUNT form.
3. A matched combinatorial skeleton for free: every row of a fixed matrix has
   the identical admissible-position word {s : (s, P(z)) = 1} out to any
   depth <= U. Any two rows agree on the full mod-P(z) sieve skeleton -- the
   closest object in this paper to "matched J-prefix and K-suffix windows",
   but at the level of where primes MAY occur, not where they DO.

What it CANNOT supply toward the target:
1. Word-level control: no step forces gap values (Focus 3), so matched
   prefix/suffix GAP WORDS at two sites are out of reach; converting the
   shared admissibility skeleton into shared occupancy is precisely the
   parity-blocked prescription problem (blocker (ii)). The paper's selection
   steps (pigeonhole, p. 224) actively discard location information.
2. Depth mismatch: the target depths J, K ~ log2 log x correspond to windows
   holding ~ log log x gaps, i.e. window length ~ log x times iterated-log
   factors -- the regime \lambda_0 = 1 + o(1), strictly below the theorem's
   \lambda_0 > 1 (Focus 1). At that scale the paper only cites Rankin [9]
   (p. 221) plus "a slight improvement ... implicit in [7]", which is
   one-sided (a single large gap, count zero) and not a two-site matched
   configuration. A Maier window at \lambda_0 > 1 contains ~
   (log x)^{\lambda_0 - 1} -> oo gaps, i.e. polynomially-in-log-x long words,
   far above the target depth; nothing in the method localizes a
   loglog-length subword.
3. Site alignment: within one matrix the deviation is one-sided (the sign of
   \omega(\lambda) - e^{-\gamma} is fixed once U is chosen); the two-sided
   pair needs two U-values, and the two landing points x = a_l are unrelated
   existential outputs -- there is no mechanism to place them at prescribed
   relative position, let alone with agreeing boundary words.
4. Supply density: sites exist only along the sparse good-z sequence (Lemma
   1) at heights x = Q^D with D fixed; per scale one gets one guaranteed row
   out of P(z)^{D-1}. This is an "infinitely many scales" supply, structurally
   similar in sparsity to (though not circular like) the Shiu-string densities
   of blocker (iii).

Net: Maier 1985 is the canonical unconditional variability engine -- it
defeats blocker (i) at window exponent \lambda_0 > 1 by importing variability
from the Buchstab oscillation through a smooth-modulus progression array, and
its matrix skeleton (identical admissible word across translates, p. 224) is
the natural template for producing two sites with matched CONSTRAINT windows.
But it prescribes counts, not words: it cannot force gap values, cannot reach
depth ~ log2 log x (its windows are (log x)^{\lambda_0}, \lambda_0 > 1), and
cannot align two sites' boundary words. For the exchange configuration it
supplies the middle-difference COUNT mechanism and the matched-skeleton
template, while the J-prefix/K-suffix OCCUPANCY matching remains exactly the
parity-blocked step it never performs.
