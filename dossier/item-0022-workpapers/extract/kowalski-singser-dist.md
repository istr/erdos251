# EXTRACTION: Emmanuel Kowalski, "Averages of Euler products, distribution of singular series and the ubiquity of Poisson distribution"

Source (only evidence base): /home/istr/pro/erdos251/dossier/singular-series-distribution.pdf
sha256 378433db556a2e83236f83a946d15178fe431e08f81511764325cce361b27920
(operator-verified; re-verified this session).
No arXiv identifier or version marker is printed on this PDF; it is
hosted at the author's ETH Zurich personal page as a standalone note.
[preprint/note, no journal reference printed] Undated in the printed
text (PDF CreationDate "Sun Jun 16 16:09:41 2019 CEST", which is a file
timestamp, not an authored date). Author(s): Emmanuel Kowalski, ETH
Zurich - D-MATH, Raemistrasse 101, 8092 Zurich, Switzerland. 30 pages.
PDF metadata: Creator "TeX", Producer "pdfTeX-1.40.19", CreationDate
"Sun Jun 16 16:09:41 2019 CEST". No journal reference is printed on the
paper.

Front-matter identification CONFIRMED against the dispatch: author
"Emmanuel Kowalski", title as printed on PDF page 1 ("AVERAGES OF EULER
PRODUCTS, DISTRIBUTION OF SINGULAR SERIES AND THE UBIQUITY OF POISSON
DISTRIBUTION"), URL
people.math.ethz.ch/~kowalski/singular-series-distribution.pdf. No
deviation: PDF page numbering matches the paper's own printed page
numbers 1-30 exactly (verified directly against PDF page 1, page 20,
and page 21).

---

## Transcription conventions

ASCII-folded (Soundararajan, Elliott-Halberstam untouched since already
ASCII). No TRANSCRIPTION-UNSURE passages encountered.

---

## 1. Front matter (verbatim)

"AVERAGES OF EULER PRODUCTS, DISTRIBUTION OF SINGULAR SERIES AND THE
UBIQUITY OF POISSON DISTRIBUTION / EMMANUEL KOWALSKI / Abstract. We
discuss in some detail the general problem of computing averages of
convergent Euler products, and apply this to examples arising from
singular series for the k-tuple conjecture and more general problems of
polynomial representation of primes. We show that the 'singular series'
for the k-tuple conjecture have a limiting distribution when taken over
k-tuples with (distinct) entries of growing size. We also give
conditional arguments that would imply that the number of twin primes
(or more general polynomial prime patterns) in suitable short intervals
are asymptotically Poisson distributed."

Affiliation line (last page of the paper): "ETH ZURICH - D-MATH,
RAEMISTRASSE 101, 8092 ZURICH, SWITZERLAND / Email address:
kowalski@math.ethz.ch"

## 2. Statements cited by item-0022's reports (verbatim, in reading order)

### 2.1 Definition of the singular series (S(h))

p.1: "The singular series associated with h is defined as the Euler
product

$$\mathfrak{S}(h) = \prod_p \left(1-\frac{\nu_p(h)}{p}\right)\left(1-\frac{1}{p}\right)^{-k} = \prod_p \left(1-\frac{\nu_p(h)-1}{p-1}\right)\left(1-\frac{1}{p}\right)^{1-k}$$

which is absolutely convergent."

### 2.2 Theorem 1.1 (existence of the moments $`\mu_k(m)`$)

p.5: "**Theorem 1.1.** Let $`k\ge1`$ be fixed. For any complex number
$`m\in\mathbf{C}`$ with $`\mathrm{Re}(m)\ge0`$, there exists a complex
number $`\mu_k(m)`$ such that

$$\lim_{h\to+\infty}\frac{1}{h^k}\sum^*_{|h|\le h}\mathfrak{S}(h)^m = \mu_k(m).$$

Moreover, for m, k >= 1 both integers, we have the symmetry property

$$\mu_k(m)=\mu_m(k);$$

in addition, we have $`\mu_1(m)=1`$ for all integers $`m\ge1`$, and hence
$`\mu_k(1)=1`$ for all $`k\ge1`$.

The last statement ($`\mu_k(1)=1`$) is of course Gallagher's theorem
(1.5); our proof is not intrinsically different, but maybe more
enlightening."

### 2.3 Gallagher's theorem, as restated by this anchor (the mu_k(1)=1 baseline)

p.5, eq. (1.5): "A result of Gallagher [Ga] states that

$$\lim_{h\to+\infty}\frac{1}{h^k}\sum^*_{|h|\le h}\mathfrak{S}(h) = 1,$$

for any fixed k, as $`h\to+\infty`$, where $`|h|=\max h_i`$ and
$`\sum^*`$ restricts to k-tuples with distinct components."

### 2.4 The explicit k=2 core: mu_k(2) closed form and numerical value (Example 3.5)

p.15, Example 3.5: "Let m = 2. We find (using the symmetry property)
that the mean-square of $`\mathfrak{S}(h)`$ is given by

$$\lim_{h\to+\infty}\frac{1}{h^k}\sum^*_{|h|\le h}\mathfrak{S}(h)^2 = \mu_k(2),$$

where

$$\mu_k(2) = \prod_p \left(\left(1-\frac1p\right)\left(1-\frac2p\right)^k + \frac1p\left(1-\frac1p\right)^k\right)\left(1-\frac1p\right)^{-2k}.$$

In particular, we find (using Pari/GP for instance):

$$\mu_2(2)=2.300\ldots \qquad \mu_3(2)=6.03294\ldots \qquad \mu_4(2)=17.562\ldots \qquad \mu_5(2)=55.255\ldots \qquad \mu_6(2)=184.18\ldots$$

Note that the second (and higher) moments increase quickly with k (as
proved in Proposition 4.1 in the next section). This is explained
intuitively by the fact that $`\mathfrak{S}(h)`$ is often zero: for
instance, the 2-factor of $`\mathfrak{S}(h)`$ is zero unless all $`h_i`$
are of the same parity, which happens with probability $`2^{1-k}`$ only
(for those, of course, the 2-factor is very large, equal to
$`2^{k-1}`$)."

### 2.5 Growth rate of the moments (Proposition 4.1 and Example 4.3)

p.15, Proposition 4.1: "For any fixed $`k\ge1`$, we have

$$\log \mu_k(m) = km \log\log 3m + O(m), \qquad m\ge1,$$

where the implied constant depends on k."

p.18, Example 4.3: "As a corollary of Proposition 4.1 and symmetry, we
have

$$\log \mu_k(2) = 2k\log\log 3k + O(k)$$

for $`k\ge1`$."

## 3. Method anatomy (paraphrase except quotes)

Sections 2-3 build a general framework (Proposition 2.1) for averaging
Euler products $`\prod_p(1+X_p)`$ against a "model" independent Euler
product $`\prod_p(1+Y_p)`$, and apply it (Section 3) to prove Theorem
1.1 by comparing $`\mathfrak{S}(h)`$'s per-prime factors $`X_p(h) =
a(p,\nu_p(h))`$ against a random model $`Y_p = a(p,\rho_p)`$ on
$`\Omega_2 = \prod_p(\mathbf{Z}/p\mathbf{Z})^k`$, giving the closed-form
limit (3.10):
$`\mu_k(m) = \prod_p(1-1/p)^{-km}\mathbf{E}_2((1-\rho_p/p)^m)`$.
Section 4 proves the almost-exponential growth rate of these moments
(Proposition 4.1) by splitting the product at $`p<km`$ and $`p\ge km`$
and bounding each range. Section 5 proves a Poisson-distribution result
(Theorem 1.3) for prime k-tuple counts in short intervals, conditional
on a uniform Bateman-Horn hypothesis, via the same Proposition 2.1
machinery.

## 4. Uniformity ledger

- Theorem 1.1's moments $`\mu_k(m)`$ exist for each *fixed* k as
  $`h\to\infty`$; the theorem gives no uniformity claim as k grows.
- The symmetry $`\mu_k(m)=\mu_m(k)`$ holds for m, k both positive
  integers (not for general complex m).
- Proposition 4.1's growth rate $`\log\mu_k(m)=km\log\log3m+O(m)`$ has
  an implied constant depending on k; it is an m-asymptotic (or, by
  symmetry, a k-asymptotic) for FIXED k (resp. fixed m), not a joint
  double-asymptotic uniform in both.
- The $`2^{1-k}`$ parity-vanishing probability is exact for every fixed
  k (an elementary consequence of the 2-adic factor of
  $`\mathfrak{S}(h)`$), not an asymptotic statement.

## 5. NOT-FOUND probe

Checked and NOT present in this paper: any statement of a
"per-position" constant of the form $`(1+o(1))^k`$ for the unconditional
or parity-conditioned second moment in a growing-k regime (Proposition
4.1 and Example 4.3 show the opposite: $`\mu_k(2)`$ grows like
$`\exp(2k\log\log3k)`$, i.e. faster than any fixed exponential in k);
no statement about a "flanked" or "aggregated simplex" domain; no
Montgomery-Soundararajan $`R_k(h)`$ theorem (that result is cited only
in this paper's own bibliography, entry [MS], and is not restated or
proved here). The explicit even-class-conditioned ratio
$`\mathbb{E}_{\mathrm{even}}[\mathfrak{S}^2]/\mathbb{E}_{\mathrm{even}}[\mathfrak{S}]^2
= 1.1504807723\ldots`$ that report 1 states is NOT itself printed in
this paper; it is report 1's own arithmetic derivation from the
ingredients extracted in Sections 2.2 and 2.4 above (independently
re-derived and re-executed in kowalski-mu-recheck.py/.txt).

## 6. COMMENTARY (assessment, not extraction)

This anchor supplies every ingredient report 1 uses for the k=2
obstruction (mu_2(1)=1, the explicit mu_k(2) Euler product, its
numerical value, and the parity-vanishing mechanism), but the specific
"even-class-conditioned" ratio is report 1's own elementary derivation,
not a quotation. The derivation is correct: conditioning a random
variable that is 0 with probability $`1-q`$ and equal to a random $`X`$
with probability q (here $`q=2^{1-k}=1/2`$ at k=2) on the nonzero event
multiplies both the mean and the second moment by $`1/q=2`$, which
reproduces exactly report 1's $`\mathbb{E}_{\mathrm{even}}[\mathfrak{S}_2]=2`$,
$`\mathbb{E}_{\mathrm{even}}[\mathfrak{S}_2^2]=2\mu_2(2)`$.

## FLAGS

- No sha256 mismatch, no TRANSCRIPTION-UNSURE passages.
- An earlier draft of this extract wrongly asserted that this PDF
  contained two concatenated documents (a ChatGPT-style transcript
  followed by the Kowalski paper). That was a mistake made while
  tracking page ranges across a large multi-document tool result in
  this session, not a property of the file. Corrected after directly
  re-reading PDF page 1, page 20, and page 21 in isolation: this file
  is Kowalski's own 30-page paper throughout, with PDF page numbers
  matching its printed page numbers 1-30 exactly.
