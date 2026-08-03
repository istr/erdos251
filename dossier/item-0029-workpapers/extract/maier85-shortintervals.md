# EXTRACTION: Helmut Maier, "Primes in short intervals"

Source (only evidence base): /home/istr/pro/erdos251/dossier/Maier-Primes-in-short-intervals.pdf
sha256 df9614f464611eb4e83b43320c3b9ae8742c11bd5cb9706d2c15e28669b26efc
Anchor line (payloads/HASHES.txt): Maier-Primes-in-short-intervals.pdf
Bibliographic identity: Michigan Math. J. 32 (1985) 221-225
Extraction method: render-based (200-dpi page rasters)
Declared scope: FULL

---

## 0. Transcription conventions

[extract note] ASCII-folded per AGENTS.md; displayed formulas are
transcribed as printed inside `$$` blocks and inline mathematics uses the
repository inline delimiter.
[extract note] The anchored PDF carries no text layer and no embedded
fonts; every character below was read from 200-dpi page rasters, with
400-dpi re-renders of two regions of p.222 used to settle bracket glyphs.
[extract note] The PDF has 6 pages; pages 1-5 carry the printed journal
pages 221-225 and page 6 is blank.
[extract note] Page citations below are the printed journal page numbers.

---

## 1. Front matter (p.221, verbatim)

"PRIMES IN SHORT INTERVALS"

"Helmut Maier"

"Received May 11, 1984."

"Michigan Math. J. 32 (1985)."

## 2. Section 1, Introduction (p.221)

"1. Introduction. The distribution of primes in short intervals is an
important problem in the theory of prime numbers. The following question
is suggested by the prime number theorem: for which functions Phi is it
true that"

Display (1.1), p.221:

$$\pi(x+\Phi(x))-\pi(x)\sim\frac{\Phi(x)}{\log{x}}\quad(x\to\infty)?$$

"Heath-Brown [4] proved that one can choose
$`\Phi(x)=x^{7/12-\epsilon(x)}`$ ($`\epsilon(x)\to0`$, as
$`x\to\infty`$), which is a slight improvement of Huxley's result [5],
$`\Phi(x)=x^{7/12+\epsilon}`$ ($`\epsilon>0`$ fixed). The Riemann
hypothesis implies that one can take $`\Phi(x)=x^{1/2+\epsilon}`$. There
is a large gap between these upper bounds and the known lower bounds of
$`\Phi(x)`$. It follows from [9] that (1.1) is wrong if"

Unnumbered display, p.221:

$$\Phi(x)=\log{x}(\log{}\log{x}\,\log{}\log{}\log{}\log{x}/(\log{}\log{}\log{x})^2).$$

"A slight improvement is implicit in the author's paper [7]."

"On assumption of the Riemann hypothesis this gap can be narrowed
considerably if an exceptional set of x-values is admitted. In 1943, A.
Selberg [10] proved that, on assumption of the Riemann hypothesis, (1.1)
is true for almost all x if $`\Phi(x)/(\log{x})^2\to\infty`$
($`x\to\infty`$). By "for almost all values of x" is meant that
$`x\to\infty`$ through any sequence lying outside a certain exceptional
set $`\mathcal{E}`$ of x-values, for which the Lebesgue measure of
$`\mathcal{E}\cap(0,u]`$ is $`o(u)`$ for $`u\to\infty`$. It is known
unconditionally that (1.1) is true for almost all x if
$`\Phi(x)=x^{1/6+\epsilon}`$. This is implicit in the work of Huxley
[5]."

"A natural question is whether Selberg's result is true without
exceptions. The purpose of this paper is to show that exceptions do exist
even for functions $`\Phi(x)`$ growing considerably faster than
$`(\log{x})^2`$."

"We prove the following."

### 2.1 The Theorem (p.221, verbatim)

"THEOREM. Let $`\Phi(x)=(\log{x})^{\lambda_0}`$, $`\lambda_0>1`$. Then"

$$\limsup_{x\to\infty}\frac{\pi(x+\Phi(x))-\pi(x)}{\Phi(x)/\log{x}}>1
\quad\text{and}\quad
\liminf_{x\to\infty}\frac{\pi(x+\Phi(x))-\pi(x)}{\Phi(x)/\log{x}}<1.$$

"For the range $`1<\lambda_0<e^{\gamma}`$ we have even"

$$\limsup_{x\to\infty}\frac{\pi(x+\Phi(x))-\pi(x)}{\Phi(x)/\log{x}}\ge\frac{e^{\gamma}}{\lambda_0},$$

"where gamma denotes Euler's constant."

"Most of the principles of the proof already appear in [7]. At some
places however we need sharper estimates."

## 3. Section 2, Basic lemmas (pp.222-223)

### 3.1 The good-modulus definition (p.222, verbatim)

"2. Basic lemmas. Following [7] we call an integer $`q>1`$ a "good"
modulus if $`L(s,\chi\rvert\ne0`$ for all characters $`\chi`$ mod q and
all s with"

$$\sigma>1-C/\log{}\lvert q(\lvert t\rvert+1)\rvert.$$

[extract note] The source prints a vertical bar where a closing
parenthesis would stand in `L(s,chi)`, and prints the outer bars of the
displayed condition as shown; both were re-read at 400 dpi on p.222 and
are transcribed as printed.

"This definition depends on $`C>0`$. However, if C is sufficiently small,
then we have: For all $`q>1`$, either q is good or there is an
exceptional real zero of some quadratic character mod q. In the latter
case the exceptional zero and character are unique (Page's theorem, cf.
[8, Satz 6.9b])."

"We define $`P(z)=\prod_{p<z}p`$."

### 3.2 Lemma 1 (p.222, verbatim)

"LEMMA 1. There is a constant $`C>0`$ such that, in terms of C, there
exist arbitrarily large values of z for which the modulus $`P(z)`$ is
good."

"Proof. This is Lemma 1 of [7]."

"The constant C will be fixed throughout the rest of the paper such that
the conclusion of Lemma 1 is true."

### 3.3 Lemma 2 (Gallagher) (p.222, verbatim)

"LEMMA 2 (Gallagher). Let q be a good modulus. Then"

$$\pi(x+h,q,a)-\pi(x,q,a)=\frac{1}{\varphi(q)}(\mathrm{li}(x+h)-\mathrm{li}\,x)(1+O(e^{-cD}+e^{-\sqrt{\log{x}}})),$$

"provided $`(a,q)=1`$, $`x\ge q^{D}`$, and $`x/2\le h\le x`$, where
$`\log{q}\ge D\ge D_0`$. (Here the constant $`D_0>0`$ and the constant
implied in O( ) depend only on C in Lemma 1; $`c>0`$ is an absolute
constant.)"

"Proof. This follows if we combine the proof of Lemma 2 in [7] with the
prime number theorem in the form
$`\pi(x)=\mathrm{li}\,x(1+O(e^{-\sqrt{\log{x}}}))`$."

### 3.4 The sieve functions and Lemma 3 (Buchstab) (p.222, verbatim)

"We set"

$$\Phi(x,y)=\lvert\lbrace n\le x:(n,P(y))=1\rbrace\rvert,\qquad
W(z)=\prod_{p<z}\left(1-\frac{1}{p}\right).$$

"LEMMA 3 (Buchstab). Let $`\lambda>1`$. Then"

$$\lim_{z\to\infty}z^{-\lambda}W(z)^{-1}\Phi(z^{\lambda},z)=e^{\gamma}\omega(\lambda),$$

"where $`\omega(u)`$ is defined by"

Display (2.1), p.222:

$$\omega(u)=u^{-1},\quad1\le u\le2,$$
$$\frac{d}{du}(u\omega(u))=\omega(u-1),\quad u\ge2,$$

"and where the right-hand derivative has to be taken at $`u=2`$."

"Proof. This follows from [2] and from Mertens' formula"

$$\prod_{p<z}\left(1-\frac{1}{p}\right)\sim\frac{e^{-\gamma}}{\log{z}}.$$

"A uniform result has been proven in [1]."

### 3.5 Lemma 4 and its proof (p.223, verbatim)

"LEMMA 4. The function $`\omega(u)-e^{-\gamma}`$ changes sign in any
interval $`[a-1,a]`$, $`a\ge2`$."

"Proof. This has been established in [6] for the general sieve of
Eratosthenes. For the convenience of the reader, however, we give a more
specific argument which in [1] is already applied to the problem of the
convergence of $`\omega(u)`$, ($`u\to\infty`$)."

"We set"

$$h(u)=\int_0^{\infty}\exp\left(-ux-x+\int_0^{x}\frac{e^{-t}-1}{t}\,dt\right)dx.$$

"Then one easily checks that"

$$h\ \text{is analytic for}\ u>-1,$$

Display (2.2), p.223:

$$uh'(u-1)+h(u)=0,$$
$$h(u)\sim\frac{1}{u}\ \text{as}\ u\to\infty.$$

"Let $`f(a)=\int_{a-1}^{a}\omega(u)h(u)\,du+a\omega(a)h(a-1)`$. From
(2.1) and (2.2) it is easily verified that"

Display (2.3), p.223:

$$f'(a)=0\quad\text{for all}\ a\ge2.$$

"By [1] we have that $`\lim_{u\to\infty}\omega(u)=e^{-\gamma}`$.
Therefore $`f(a)\to e^{-\gamma}`$ as $`a\to\infty`$ which together with
(2.3) implies that"

Display (2.4), p.223:

$$\int_{a-1}^{a}\omega(u)h(u)\,du+a\omega(a)h(a-1)=e^{-\gamma}.$$

"Now let"

$$g(a)=\int_{a-1}^{a}h(u)\,du+ah(a-1).$$

"From (2.2) it is easily seen that $`g'(a)=0`$ for all $`a>0`$. Since
$`g(a)\to1`$ as $`a\to\infty`$, we have:"

$$\int_{a-1}^{a}h(u)\,du+ah(a-1)=1.$$

"This together with (2.4) gives:"

$$\int_{a-1}^{a}(\omega(u)-e^{-\gamma})h(u)\,du+a(\omega(a)-e^{-\gamma})h(a-1)=0.$$

"Since $`h>0`$ it follows that either $`\omega(u)\equiv e^{-\gamma}`$ in
$`[a-1,a]`$ or there is a sign-change of $`\omega(u)-e^{-\gamma}`$ in
$`[a-1,a]`$. But the first alternative would imply that
$`\omega(u)\equiv e^{-\gamma}`$ in $`[1,\infty)`$. This concludes the
proof of Lemma 4."

## 4. Section 3, Proof of the theorem (pp.223-225)

### 4.1 The scale restriction and the matrix (pp.223-224, verbatim)

"3. Proof of the theorem. We now fix an integer $`D\ge D_0`$ depending at
most on $`\epsilon>0`$ to be introduced later. In the sequel we assume
that $`z\to\infty`$ through a set of z for which $`P(z)`$ is a good
modulus in the sense of Lemma 1 and that $`z\ge e^{cD}`$, where c is the
constant in Lemma 2. We also choose an integer $`U=U(z)`$, such that
$`U\le P(z)`$."

"We consider the matrix"

$$\mathfrak{M}=(a_{rs}),\quad\text{where}$$
$$a_{rs}=s+rP(z),\quad1\le s\le U,\quad P(z)^{D-1}<r\le2P(z)^{D-1}.$$

"We want to estimate the number of primes in $`\mathfrak{M}`$ which we
denote by $`\pi(\mathfrak{M})`$."

"The rows of $`\mathfrak{M}`$ are intervals of U consecutive integers,
whereas the columns of $`\mathfrak{M}`$ are arithmetic progressions with
common difference $`P(z)`$. Only those columns for which $`(s,P(z))=1`$
contain primes. We call such columns admissible."

"The number of primes in an admissible column is, by Lemma 2:"

$$\pi(2P(z)^{D}+s,P(z),s)-\pi(P(z)^{D}+s,P(z),s)$$
$$=\frac{P(z)^{D}}{\varphi(P(z))\log{(P(z)^{D})}}(1+O(e^{-cD}))$$
$$=(P(z)^{D-1}/\log{(P(z)^{D})})W(z)^{-1}(1+O(e^{-cD})).$$

"Let the number of admissible columns be $`UW(z)c(U,z)`$. Then we have"

Display (3.1), p.224:

$$\pi(\mathfrak{M})=\frac{P(z)^{D-1}}{\log{(P(z)^{D})}}Uc(U,z)(1+O(e^{-cD})).$$

### 4.2 Conclusion of the proof (pp.224-225, verbatim)

"Now we can conclude the proof of the theorem. To prove the first part we
fix $`\lambda_1>\lambda_0`$ such that $`\omega(\lambda_1)>e^{-\gamma}`$,
which is possible by Lemma 4. We choose $`U=[z^{\lambda_1}]`$. By (3.1)
and Lemma 3 there is at least one row of $`\mathfrak{M}`$ with at least"

$$\frac{U}{\log{(P(z)^{D})}}e^{\gamma}\omega(\lambda_1)(1+O(e^{-cD}))\ \text{primes.}$$

"We now set $`l_0=\lbrace\log{(P(z)^{D})}\rbrace^{\lambda_0}`$ and divide
this row into $`K_0=[U/l_0]+1`$ subintervals of equal length
$`l_0(1+o(1))`$. At least one of these subintervals, say
$`(a_l,b_l]`$, contains at least"

$$r=\frac{U}{K_0(\log{(P(z)^{D})})}e^{\gamma}\omega(\lambda_1)(1+O(e^{-cD}))\ \text{primes.}$$

"We set $`x=a_l`$ and obtain $`(a_l,b_l]\subseteq(x,x+\Phi(x)]`$. Thus
the interval $`(x,x+\Phi(x)]`$ contains at least"

$$r=(\Phi(x)/\log{x})e^{\gamma}\omega(\lambda_1)(1+O(e^{-cD}))\ \text{primes.}$$

"For any given $`\epsilon>0`$ we can fix D such that
$`r\ge(\Phi(x)/\log{x})(e^{\gamma}\omega(\lambda_1)-\epsilon)`$, which
concludes the proof of the first part of the theorem."

"The third part immediately follows by observing that
$`\omega(u)=u^{-1}`$ for $`1\le u\le2`$. The proof of the second part is
completely analogous to the proof of the first part. We choose
$`\lambda_2>\lambda_0`$ such that $`\omega(\lambda_2)<e^{-\gamma}`$ and
set $`U=[z^{\lambda_2}]`$. There is at least one row of
$`\mathfrak{M}`$ with at most"

$$\frac{U}{\log{(P(z)^{D})}}e^{\gamma}\omega(\lambda_2)(1+O(e^{-cD}))\ \text{primes.}$$

"We set $`l_1=\lbrace\log{(2P(z)^{D})}\rbrace^{\lambda_0}`$ and divide
this row into $`K_1=[U/l_1]`$ subintervals of equal length. An easy
computation similar to the one above shows that at least one of these
subintervals contains an interval $`(x,x+\Phi(x)]`$ with at most
$`(\Phi(x)/\log{x})(e^{\gamma}\omega(\lambda_2)+\epsilon)`$ primes. This
concludes the proof."

"ACKNOWLEDGMENT. The author wishes to thank Professors H. L. Montgomery
and R. C. Vaughan for pointing out to him the proof of Lemma 4."

## 5. References as printed (p.225, verbatim)

"1. N. G. de Bruijn, On the number of uncancelled elements in the sieve
of Eratosthenes, Nederl. Akad. Wetensch. Proc. 53 (1950), 803-812.
2. A. A. Buchstab, Asymptotic estimates of a general number-theoretic
function (Russian), Mat.-Sb. (N.S.) 2(44) (1937), 1239-1246.
3. P. X. Gallagher, A large sieve density estimate near sigma = 1,
Invent. Math. 11 (1970), 329-339.
4. D. R. Heath-Brown, Differences between consecutive primes. Seminar on
Number Theory, 1979-80 (French), Exp. No. 14, Univ. Bordeaux I, Talence,
1980.
5. M. N. Huxley, On the difference between consecutive primes, Invent.
Math. 15 (1972), 164-170.
6. H. Iwaniec, The sieve of Eratosthenes-Legendre, Ann. Scuola Norm. Sup.
Pisa Cl. Sci. (4) 4 (1977), 257-268.
7. H. Maier, Chains of large gaps between consecutive primes, Adv. in
Math. 39 (1981), 257-269.
8. K. Prachar, Primzahlverteilung, Springer, Berlin, 1957.
9. R. A. Rankin, The difference between consecutive prime numbers, J.
London Math. Soc. 13 (1938), 242-247.
10. A. Selberg, On the normal density of primes in small intervals and
the difference between consecutive primes, Arch. Math. Naturvid. 47
(1943), 87-105."

"Department of Mathematics / University of Michigan / Ann Arbor, Michigan
48109"

## 6. Uniformity ledger

- [extract note] The constant C of the good-modulus definition is fixed
  once, by Lemma 1, and held for the rest of the paper (p.222).
- [extract note] In Lemma 2 the constant $`D_0>0`$ and the constant
  implied in $`O(\ )`$ depend only on C; $`c>0`$ is stated to be an
  absolute constant (p.222).
- [extract note] In Section 3 the integer $`D\ge D_0`$ depends at most on
  the $`\epsilon>0`$ introduced later (p.223).
- [extract note] The variable z is not free: the proof assumes
  $`z\to\infty`$ through the set of z for which $`P(z)`$ is a good
  modulus and $`z\ge e^{cD}`$ (pp.223-224), and Lemma 1 asserts only that
  such z exist arbitrarily large (p.222).
- [extract note] Lemma 3 is stated for fixed $`\lambda>1`$ as a limit in
  z, and the source records that a uniform result was proven in [1]
  (p.222).
- [extract note] The Theorem's third assertion is stated only for the
  range $`1<\lambda_0<e^{\gamma}`$ (p.221).

## 7. Structural map

[extract note] 1. Lemma 1 (p.222) is proved by reference to [7, Lemma 1]
only; no argument is printed here.
[extract note] 2. Lemma 2 (p.222) is proved by combining [7, Lemma 2]
with the prime number theorem; its statement invokes the good-modulus
definition of p.222.
[extract note] 3. Lemma 3 (p.222) is proved from [2] and Mertens'
formula; its statement invokes $`\Phi(x,y)`$, $`W(z)`$ and (2.1), all
defined on p.222.
[extract note] 4. Lemma 4 (p.223) invokes (2.1) and (2.2) at the step
establishing (2.3), and [1] at the step passing from (2.3) to (2.4).
[extract note] 5. The column count on p.224 invokes Lemma 2 and the
matrix definition of p.224.
[extract note] 6. Display (3.1) (p.224) is assembled from that column
count and the count of admissible columns.
[extract note] 7. The first part of the Theorem (p.224) invokes Lemma 4
(to fix $`\lambda_1`$), then (3.1) and Lemma 3.
[extract note] 8. The third part of the Theorem (p.224) invokes only the
first branch of (2.1).
[extract note] 9. The second part of the Theorem (pp.224-225) invokes
Lemma 4 (to fix $`\lambda_2`$), then (3.1) and Lemma 3, by the stated
analogy with the first part.

## FLAGS

- sha256 of the local file matches the anchor line above; verified before
  the source was opened.
- TRANSCRIPTION-UNSURE passages: 0.
- V5 (this source): confirmed against the anchored bytes -- `pdffonts`
  lists no fonts and `pdftotext` returns an empty text layer. The
  transcription is render-only.
- V8 (this source): the PDF has 6 pages against a steering expectation of
  6; printed pages 221-225 occupy PDF pages 1-5 and PDF page 6 is blank.
- Divergence from the Section 4.1 attention list of the dispatch: that
  list named "the smooth-number count it consumes" and "the
  Gallagher-input citation point". Both are present -- Lemma 3
  (Buchstab) and Lemma 2 (Gallagher) -- but the source attributes Lemma 2
  to [7, Lemma 2] plus the prime number theorem in its own proof line,
  and cites Gallagher only in the reference list as [3]; the bracketed
  citation [3] does not appear in the body of this paper, though the name
  Gallagher is printed in the heading of LEMMA 2 (p.222).
- The printed matrix modulus is $`P(z)=\prod_{p<z}p`$ with a strict
  inequality (p.222), not $`p\le z`$.
