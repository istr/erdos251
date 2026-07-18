# EXTRACTION: Janos Pintz, "On the singular series in the prime k-tuple conjecture"

Source (only evidence base): /home/istr/pro/erdos251/dossier/1004.1084v1.pdf
arXiv:1004.1084v1 [math.NT] 7 Apr 2010. Author: Janos Pintz, Renyi
Mathematical Institute of the Hungarian Academy of Sciences, Budapest
(p. 4). 4 pages. Footnote p. 1: "Supported by OTKA Grants K72731, K67676
and ERC-AdG.228005."

Transcription conventions: ASCII only. Diacritics transliterated (Janos
Pintz, Yildirim, Cramer, Renyi, Realtanoda). Math in LaTeX-like ASCII:
the Gothic/Fraktur singular-series symbol \frakS is rendered plain "S";
the calligraphic set symbol is rendered "calH" (so "S(calH)" = singular
series of the set calH), while the plain "H" is the span/window length
as in the paper; nu_p, nu'_p subscripts as printed; <= , >= ; \prod,
\sum; \Pi_1, \Pi_2, \Pi_3 are the paper's three product factors in
(2.2); p !| n means p does not divide n (paper's p \nmid); Delta, eps
(the paper's varepsilon). log_2 H in (2.8) is transcribed as printed
(see flag 3). Anchors are equation numbers (1.1)-(2.8) and section
numbers 1-2 (the paper has NO numbered theorems beyond "Theorem 1" and
"Theorem 1'", no lemmas, no abstract); page numbers (printed = PDF page)
are secondary aid.

Everything up to the final section is EXTRACTION (what the paper says).
Commentary appears ONLY in the final marked section.

---

## 1. FRONT MATTER

Title (p. 1): "On the singular series in the prime k-tuple conjecture".
Author: "Janos Pintz" (with footnote * = grant support, quoted above).

The paper has NO abstract. It opens directly with Section 1.

---

## 2. SECTION 1 (setup and results), essentially complete verbatim

Opening (Section 1, p. 1), verbatim:

> "1. Gallagher's result [Gal] about the mean-value of the singular
> series
> (1.1)  S(calH) = \prod_p (1 - nu_p/p)(1 - 1/p)^{-k}
> over all k-element sets
> (1.2)  calH = {h_i}_{i=1}^{k},  h_i different,  h_i in [1, H]
> (where nu_p = nu_p(calH) denotes the number of residue classes
> occupied by calH mod p) played a crucial role in the proof of
> (1.3)  liminf_{n -> infty} (p_{n+1} - p_n)/log p_n = 0   [GPY],
> where p_n denotes the n-th prime."

Continuation (p. 1), verbatim:

> "However, a brief study of the works [GPY] or [GMPY] shows that
> actually we need a far weaker result: to show the existence of at
> least one admissible set |calH| = k_nu (i.e. nu_p < p for any prime p)
> for a series of k_nu -> infty and a C > 0 absolute constant with the
> property
> (1.4)  S_calH(H) := (1/H) \sum_{h=1}^{H} S(calH cup {h})/S(calH) >= C
>          for H > C_0(|calH|)."

Continuation (p. 1), verbatim:

> "In [Pin] we showed in a very simple way that (1.4) holds for a
> particular calH_k for any k, even for all individual even h (for odd h
> we had S(calH cup {h}) = 0). In the present note we prove beyond (1.4)
> that for any calH subset [1, H] we have S_calH(H) -> 1 if H -> infty,
> and investigate the rate of convergence depending on k. By induction
> on k, this implies Gallagher's result [Gal]
> (1.5)  \sum_{|calH|=k, calH subset [1,H]} S(calH) ~ H^k
>          for H -> infty,"

Continuation (top of p. 2), verbatim:

> "however, S_calH(H) -> 1 yields more information about the singular
> series than the global average (1.5)."

Theorem 1 (p. 2), verbatim:

> "Theorem 1. With the notation (1.1), (1.2), (1.4) we have for any
> sufficiently small eps > 0
> (1.6)  S_calH(H) = 1 + O(eps)   if H >= exp(k^{1/eps})."

First Remark (p. 2), verbatim:

> "Remark. The following relations can be proved in an even more simple
> way for every calH."

Theorem 1' (p. 2), verbatim:

> "Theorem 1'. With the notation (1.1)-(1.2) we have
> (1.7)  S_calH(H) >= 1 + O(eps)   if H >= exp( (1/eps) k/log k )
> and with some absolute constants c_1, c_2
> (1.8)  S_calH(H) >= c_1   if H >= exp( c_2 k/log k )."

Second Remark (p. 2), verbatim:

> "Remark. As mentioned in the introduction, for (1.3), but actually in
> most other applications for problems involving small gaps between
> primes and almost primes we need just lower estimates for the singular
> series. This fact gives an additional significance for simple proofs
> of lower estimates for expressions involving the singular series."

[This is ALL of Section 1. There are no other theorems, lemmas, or
corollaries in the paper.]

---

## 3. SECTION 2 (the proof), essentially complete verbatim

Setup (Section 2, p. 2), verbatim:

> "2. Let us study first the ratio S(calH')/S(calH) for a single
> calH' := calH cup {h}, h notin calH, with the notation
> (2.1)  nu'_p := nu_p(calH'),  y := 5 log H / 6,
>        P := \prod_{p <= y} p,  Delta := \prod_{i=1}^{k} (h - h_i)."

Factorization (p. 2), verbatim:

> "Then we have
> (2.2)  S(calH')/S(calH)
>          = \prod_p ( 1 - nu'_p/p ) / ( (1 - nu_p/p)(1 - 1/p) )
>          := \Pi_1 . \Pi_2 . \Pi_3
> [with \Pi_1 over p <= y; \Pi_2 over p > y, p | Delta; \Pi_3 over
> p > y, p !| Delta -- product ranges transcribed from the rendered
> page, see flag 4]."

Large primes not dividing Delta (p. 2), verbatim:

> "For p !| Delta we have nu'_p = nu_p + 1, otherwise nu'_p = nu_p,
> hence
> (2.3)  \Pi_3 = \prod_{p>y} ( 1 + O(k/p^2) ) = 1 + O( k/(y log y) ),"

Large primes dividing Delta (p. 3), verbatim:

> "(2.4)  \Pi_2 = \prod_{p>y, p|Delta} (1 - 1/p)^{-1}
>           = exp( O( \sum_{p>y, p|Delta} 1/p ) )."

PNT step (p. 3), verbatim:

> "Since by the Prime Number Theorem
>   \sum_{p|Delta} log p <= log Delta <= 2ky,
> the sum over 1/p in the error term is maximal if the relevant primes
> with p | Delta are as small as possible satisfying the inequality
> \sum_{p in P*} log p <= 2ky, consequently
> (2.5)  \sum_{p|Delta, p>y} 1/p <= \sum_{y<p<4ky} 1/p
>          <= log( log(5ky) / log y ) <= 2 eps."

Individual-h conclusion for the large-prime factors (p. 3), verbatim:

> "(2.3)-(2.5) imply that we have for any individual h
> (2.6)  \Pi_2 \Pi_3 (h) = 1 + O(eps)."

Averaging the small-prime factor (p. 3), verbatim:

> "We will now study the average of \Pi_1(h) for h <= H = MP + r,
> 0 <= r < P, M -> infty. Due to the periodicity of \Pi_1(h) (with
> period P) it is sufficient to average over h in [1, P]. For any
> p <= y we have exactly nu_p possibilities mod p for h with
> nu'_p = nu_p and p - nu_p with nu'_p = nu_p + 1. Consequently,
> (2.7)  (1/P) \sum_{h=1}^{P} \Pi_1(h)
>          = \prod_{p|P} { (nu_p/p)(1 - nu_p/p)
>              + (1 - nu_p/p)(1 - (nu_p+1)/p) }
>            / ( (1 - nu_p/p)(1 - 1/p) )
>          = 1."

Conclusion of Theorem 1 (p. 3), verbatim:

> "Formulas (2.2) and (2.6)-(2.7) prove (1.6)."

Proof of Theorem 1' (p. 3), verbatim:

> "To prove Theorem 1' we can replace (2.4)-(2.5) with the trivial
> relation Pi_2 >= 1, thereby obtaining
> (2.8)  Pi_2 Pi_3 (h) >= { 1 + O(eps)  if k/(log H log_2 H) = O(eps),
>                         { c_1         if k/(log H log_2 H) <= c_3.
> This, together with (2.7) proves Theorem 1'."

[This is ALL of Section 2 and ends the mathematical content of the
paper; p. 4 is references and the address block only.]

---

## 4. REFERENCES (p. 4), verbatim

> "[Gal] P. X. Gallagher,, On the distribution of primes in short
> intervals, Mathematika 23 (1976), 4-9."
[double comma after "Gallagher" as printed -- flag 2]

> "[GPY] D. A. Goldston, J. Pintz, C. Yildirim, Primes in tuples I,
> Annals of Math. (2) 170 (2009), 819-862."

> "[GMPY] D. A. Goldston, Y. Motohashi, J. Pintz, C. Y. Yildirim, Small
> gaps between primes exist, Proc. Japan Acad. Ser. A. Math. Sci. 82
> (2006), 61-65."

> "[Pin] J. Pintz, A note on small gaps between primes, preprint."

Address block (p. 4): Janos Pintz, Renyi Mathematical Institute of the
Hungarian Academy of Sciences, Budapest, Realtanoda u. 13-15, H-1053
Hungary, E-mail: pintz@renyi.hu.

---

## 5. METHOD ANATOMY (connective tissue; PARAPHRASE except quotes)

PARAPHRASE. The object controlled is the h-averaged extension ratio
S_calH(H) = (1/H) sum_{h<=H} S(calH cup {h})/S(calH) of (1.4), for an
arbitrary fixed k-element set calH subset [1,H]. The proof splits the
Euler product of the ratio (2.2) at y = 5 log H / 6 into:

- \Pi_1 (p <= y): periodic in h with period P = prod_{p<=y} p; its
  average over a full period is EXACTLY 1 by the local residue count
  (2.7) -- nu_p residues give nu'_p = nu_p, p - nu_p residues give
  nu'_p = nu_p + 1, and the two-term local average telescopes to
  (1 - nu_p/p)(1 - 1/p), cancelling the denominator. No error term.
- \Pi_3 (p > y, p !| Delta): each factor is 1 + O(k/p^2), so the
  product is 1 + O(k/(y log y)) (2.3) -- individually in h.
- \Pi_2 (p > y, p | Delta): controlled through log Delta <= 2ky and a
  worst-case packing of prime divisors just above y (PNT), giving the
  Mertens-type bound (2.5) sum_{p|Delta, p>y} 1/p <= 2 eps --
  individually in h. Here the span condition of Theorem 1 enters: with
  log y ~ log_2 H and H >= exp(k^{1/eps}) one has
  log(log(5ky)/log y) = O(eps).

Theorem 1 = (2.6) x (2.7): individual (1+O(eps)) control of
\Pi_2\Pi_3 times exact mean 1 of \Pi_1. Theorem 1' drops (2.4)-(2.5)
and uses only Pi_2 >= 1 (each factor (1-1/p)^{-1} > 1), so the span
threshold weakens to k/(log H log_2 H) bounded (2.8): this yields the
lower-bound-only statements (1.7), (1.8) at spans exponential in
k/log k instead of exp(k^{1/eps}).

Uniformity ledger (what is uniform in what):
- calH: arbitrary k-element subset of [1,H]; no admissibility
  hypothesis is stated in Theorem 1 or 1' (but see Commentary note C6:
  the ratio in (1.4) presupposes S(calH) != 0).
- k = |calH|: unbounded; the span thresholds are the only k-dependence:
  (1.6) H >= exp(k^{1/eps}); (1.7) H >= exp((1/eps) k/log k);
  (1.8) H >= exp(c_2 k/log k) with absolute c_1, c_2.
- The averaging length is the same H as the span containing calH
  ((1.2) and (1.4) use the same letter H); the average runs over ALL
  h <= H, not only h avoiding calH-collisions or parity classes.
- Gallagher's global mean (1.5), sum over all k-element calH in [1,H]
  of S(calH) ~ H^k, is recovered "by induction on k" (p. 1); the paper
  states this one sentence and does not spell the induction out.

What the paper does NOT contain (checked against the full 4-page text,
all pages sighted): no statement about extreme values of S(calH) (no
upper bounds on individual S, no maximal/minimal order); no variance or
higher-moment statement about S over calH or over h; no site counts or
tuple counts; no weighted sums over primes; no short-interval or
gap-word statement beyond the citation (1.3). "Extreme values":
NOT FOUND in this text. "Variance of the singular series": NOT FOUND in
this text. The only individual-h positivity information is the negative
example quoted from [Pin] (p. 1): for the particular calH_k, odd h give
S(calH cup {h}) = 0.

---

## COMMENTARY (assessment, NOT extraction)

Consuming context: the project needs an UNCONDITIONAL supply of two
prime-gap-word sites with matched J-prefix and K-suffix windows and a
dominant weighted middle difference, at depths J,K ~ log_2 log x (an
exchange configuration). Blockers: (i) pigeonhole blind to variability;
(ii) prescribed gap patterns = parity-blocked tuple-type lower bound;
(iii) Shiu-string site densities circular at the needed depth.

C1. What this paper unconditionally supplies. First-moment (h-averaged)
control of singular-series extension ratios, uniform in the set calH,
at spans that are CHEAP at our depth. By (1.8), S_calH(H) >= c_1
already for H >= exp(c_2 k/log k); by (1.7), >= 1 + O(eps) for
H >= exp((1/eps) k/log k); by (1.6), = 1 + O(eps) for
H >= exp(k^{1/eps}). At depth k = J + K ~ 2 log_2 log x, the threshold
exp(c_2 k/log k) is roughly exp(c' log_2 log x / log_3 log x), far
below any (log x)^c window -- so, unlike the Shiu-string densities of
blocker (iii), the singular-series input to a GPY/Maynard-type weight
at exchange depth is NOT circular: it is unconditionally ~ 1 on
average, with completely explicit span thresholds. If the exchange
construction ever routes through a weighted count whose main term
carries an averaged singular series over extension positions h (as in
(1.4), which is literally the input [GPY]/[GMPY] need per p. 1 and the
second Remark, p. 2), this note certifies that coefficient is bounded
below by an absolute constant, uniformly in the prefix/suffix tuple.

C2. What it cannot supply -- sites. Nothing here converts
singular-series positivity into a lower bound on the NUMBER of integers
realizing a fixed gap word: the paper contains no counting statement at
all (Section 5 ledger; the only prime-counting content is the cited
(1.3)). The step "positive singular series => positive site density" is
exactly the parity-blocked tuple lower bound of blocker (ii); this note
does not touch it, and its own Remark (p. 2) frames the singular series
as an input to small-gap detection (via [GPY]-type weighted averages
whose conclusion is disjunctive/pigeonhole), not as a site-supply
device.

C3. What it cannot supply -- variability. The theorems are averages
over h; blocker (i) (pigeonhole blind to variability) is therefore not
addressed but rather EXEMPLIFIED: the whole note is a sharpened
first-moment computation. Notably, ALL the h-variability of the ratio
S(calH cup {h})/S(calH) sits in the small-prime factor \Pi_1(h), which
the paper controls ONLY in mean ((2.7), exactly 1 over a period P);
individually \Pi_1(h) can vanish (inadmissible extension; cf. the odd-h
example from [Pin], p. 1). The large-prime factors are individually
tame ((2.6): \Pi_2\Pi_3(h) = 1 + O(eps)). So the paper cleanly
localizes WHERE singular-series variability lives (residues mod primes
p <= y ~ log H), but provides no second-moment or distributional
statement about it.

C4. A structurally interesting nugget: (2.7) is an EXACT identity --
the mean of \Pi_1 over a full period P = prod_{p<=y} p is exactly 1,
with no error term, for every calH. For an exchange configuration one
could imagine comparing two candidate sites by averaging extension
ratios over matched residue windows; (2.7) says the local (p <= y)
obstruction has exactly mean 1 for ANY tuple, i.e. matched J-prefix and
K-suffix windows have identical local mean behavior regardless of the
word. This is a (very weak but exact and unconditional) "matching"
statement at the level of local densities. It does not weight the
middle difference, and it says nothing about which residues h realize
the mean.

C5. Depth/rate bookkeeping against the target. The three span
thresholds order as exp(c_2 k/log k) < exp((1/eps) k/log k) <
exp(k^{1/eps}) (for small eps), anchors (1.8), (1.7), (1.6). At
k ~ log_2 log x all three are (log x)^{o(1)}; even the strongest
(asymptotic-1) form (1.6) costs only H >= exp((log_2 log x)^{1/eps}),
still (log x)^{o(1)} for any fixed eps. So the machinery is uniformly
usable at exchange depth; the binding constraints for the project
remain (ii) (no unconditional site counts from singular series) and (i)
(only mean-level information). Nothing in this note bears on the
dominant-weighted-middle-difference requirement: "weighted difference":
NOT FOUND in this text.

C6. Caveat on hypotheses (extractor observation, not in the paper):
the ratio S(calH cup {h})/S(calH) in (1.4) presupposes S(calH) != 0,
i.e. calH admissible; Theorems 1 and 1' do not state this hypothesis
(Theorem 1' is even prefaced "for every calH", first Remark p. 2). Any
transfer should add the admissibility hypothesis explicitly. Also note
the averaged quantity in (1.6)-(1.8) includes inadmissible extensions
h (which contribute 0), so the theorems implicitly bound the LOSS from
inadmissible h: their density cost is absorbed in the 1 + O(eps).

---

## FLAGS (consolidated)

1. The paper has NO abstract and no numbered sections beyond "1." and
   "2."; "Theorem 1" and "Theorem 1'" are the only labeled results.
2. [PRINTED-ODDITY] "[Gal] P. X. Gallagher,," -- double comma as
   printed (p. 4).
3. [TRANSCRIPTION-UNSURE, resolved-by-context] In (2.8) the
   denominators read "log H log_2 H" (rendered page and text layer
   agree). Interpretation of log_2 H as the iterated logarithm
   log log H is the extractor's (consistent with y log y where
   y = 5 log H/6, via (2.3)); the paper defines no log_2 notation.
4. [TRANSCRIPTION-UNSURE, resolved-by-image] The ranges of \Pi_1,
   \Pi_2, \Pi_3 under the three products in (2.2) (p <= y; p > y,
   p | Delta; p > y, p !| Delta) are taken from the rendered page; the
   pdftotext layer scrambles these subscripts. The reading is confirmed
   by their subsequent uses in (2.3) [\Pi_3, p > y], (2.4) [\Pi_2,
   p > y, p | Delta], and (2.7) [\Pi_1, p | P, P = prod_{p<=y} p].
5. [TRANSCRIPTION-UNSURE] In (2.5) the middle sum's range "y < p < 4ky"
   and the bound "log( log(5ky)/log y )" (outer log of a ratio of logs)
   are transcribed from the rendered page; small glyphs, but text layer
   agrees ("log \frac{log(5ky)}{log y}").
6. In (1.7) the paper writes a lower bound with an O-term,
   "S_calH(H) >= 1 + O(eps)"; the intended meaning >= 1 - C eps is the
   extractor's reading of standard usage, not stated in the paper.
7. In (2.8) the paper switches from \prod-with-subscript notation to
   inline "Pi_2 Pi_3 (h)" and "Pi_2 >= 1"; transcribed as printed.
8. The claim "By induction on k, this implies Gallagher's result [Gal]"
   (p. 1, before (1.5)) is asserted without proof in the note;
   transcribed verbatim, no detail exists in the text.
