# EXTRACTION: Adolf Hildebrand and Helmut Maier, "Gaps between prime numbers"

Source (only evidence base): /home/istr/pro/erdos251/dossier/S0002-9939-1988-0958032-5.pdf
sha256 3a8666eb99db96fcaca274d8824e415536d15d3467e1c16446b57cce649e3261
Anchor line (payloads/HASHES.txt): S0002-9939-1988-0958032-5.pdf
Bibliographic identity: Proc. Amer. Math. Soc. 104 (1988), no. 1, 1-9
Extraction method: render-based (200-dpi page rasters)
Declared scope: FULL

---

## 0. Transcription conventions

[extract note] ASCII-folded per AGENTS.md; displayed formulas are transcribed as
printed inside `$$` blocks, inline mathematics uses the repository inline
delimiter, and page citations are the printed journal page numbers.
[extract note] The anchored PDF carries a text layer, but it is OCR-derived and
corrupt in a way that touches every display (it renders $`\mathbf{R}^k`$ as
"Rfc", N as "TV", and $`p_{n+1}-p_n`$ as "Pn+i ~Pn"). Every character below was
read from 200-dpi page rasters; the text layer was used only to locate material
on the page and never as the source of a quotation.
[extract note] The PDF has 9 pages and the printed pagination runs 1-9.
[extract note] The source writes cardinalities with a doubled-stroke hash glyph;
those are transcribed as `\lvert ... \rvert` around the source's own set-builder
form.

---

## 1. Front matter (p.1, verbatim)

"PROCEEDINGS OF THE / AMERICAN MATHEMATICAL SOCIETY / Volume 104, Number 1,
September 1988"; "GAPS BETWEEN PRIME NUMBERS"; "ADOLF HILDEBRAND AND HELMUT
MAIER"; "(Communicated by Larry J. Goldstein)".

"ABSTRACT. Let $`d_n=p_{n+1}-p_n`$ denote the nth gap in the sequence of primes.
We show that for every fixed integer k and sufficiently large T the set of limit
points of the sequence
$`\lbrace(d_n/\log{n},\ldots,d_{n+k-1}/\log{n})\rbrace`$ in the cube $`[0,T]^k`$
has Lebesgue measure $`\ge c(k)T^k`$, where $`c(k)`$ is a positive constant
depending only on k. This generalizes a result of Ricci and answers a question
of Erdos, who had asked to prove that the sequence
$`\lbrace d_n/\log{n}\rbrace`$ has a finite limit point greater than 1."

"Received by the editors July 23, 1987 and, in revised form, August 26, 1987.";
"1980 Mathematics Subject Classification (1985 Revision). Primary 11N05.";
"Work supported by NSF grants."; "(c)1988 American Mathematical Society /
0002-9939/88 $1.00 + $.25 per page".

## 2. Section 1, Introduction (pp.1-2)

"1. Introduction. Let $`p_n`$ denote the nth prime, and let
$`d_n=p_{n+1}-p_n`$ be the nth gap between consecutive primes. The prime number
theorem implies that $`p_n\sim n\log{n}`$, as $`n\to\infty`$. Hence the average
size of a gap $`d_n`$ is $`\log{n}`$. However, there exist gaps that are much
larger than $`\log{n}`$. In fact, as was shown by Westzynthius [9], we have"
-- display (1), p.1:
$$\limsup_{n\to\infty}\frac{d_n}{\log{n}}=\infty.$$
"Erdos [2] proved that there exist infinitely many pairs of consecutive "large"
gaps $`(d_n,d_{n+1})`$. In [5] the second author extended this result to an
arbitrary number of consecutive gaps, showing that for any $`k\ge1`$"
-- display (2), p.1:
$$\limsup_{n\to\infty}\frac{\min(d_n,\ldots,d_{n+k-1})}{\log{n}}=\infty.$$
"Our knowledge about small gaps is less satisfactory. As a counterpart to (1),
one might expect that" -- display (3), p.1:
$$\liminf_{n\to\infty}\frac{d_n}{\log{n}}=0.$$
"This would follow, if the twin prime conjecture were true. The prime number
theorem trivially implies that the "lim inf" in (3) is at most 1. Erdos [1] was
the first to obtain" -- display (4), p.1:
$$\liminf_{n\to\infty}\frac{d_n}{\log{n}}\le c$$
"for some constant c strictly less than 1. A number of authors subsequently
reduced the value of c in (4), the current record being $`c=0.248\ldots`$ [6]. A
proof of (3), however, seems to be still out of reach."

"Let S denote the set of limit points of the sequence
$`\lbrace d_n/\log{n}\rbrace`$. A natural conjecture is that S consists of all
nonnegative real numbers and the point $`\infty`$. By (1), $`\infty`$ is indeed
a limit point of S, and Erdos' result (4) implies that S contains a real number
strictly less than 1. Erdos and Ricci [8] proved that S has in fact positive
Lebesgue measure. Erdos recently asked whether S contains a real number greater
than 1. The purpose of this note is to prove the following theorem, which
settles Erdos' question in the affirmative. Roughly speaking, the theorem
asserts that a positive proportion of all real numbers belong to S, and that an
analogous result holds for the limit points (in $`\mathbf{R}^k`$) of the
sequence" -- display (5), p.2:
$$\left(\frac{d_n}{\log{n}},\ldots,\frac{d_{n+k-1}}{\log{n}}\right)\qquad(n=1,2,3,\ldots).$$

### 2.1 THEOREM and COROLLARY (p.2, verbatim)

"THEOREM. Let k be a positive integer, and let $`S^{(k)}`$ be the set of limit
points in $`\mathbf{R}^k`$ of the sequence (5). Then we have, for any
sufficiently large number T,"
$$\lambda(S^{(k)}\cap[0,T]^k)\ge c(k)T^k,$$
"where $`\lambda(\cdots)`$ denotes the Lebesgue measure in $`\mathbf{R}^k`$ and
$`c(k)`$ is a positive constant depending only on k."

"The theorem immediately implies that the sequence
$`\lbrace d_n/\log{n}\rbrace`$ has arbitrarily large finite limit points, thus
answering the above-mentioned question of Erdos. In fact, noting that the set of
points $`(x_1,\ldots,x_k)`$ in $`[0,T]^k`$ satisfying
$`\min_{1\le i\le k}x_i<\varepsilon T`$ has Lebesgue measure
$`<k\varepsilon T^k`$, we obtain the following"

"COROLLARY. Let k be a positive integer and let
$`\varepsilon=\varepsilon(k)=c(k)/k`$, where $`c(k)`$ is the constant in the
theorem. Then, for every sufficiently large T, the sequence (5) has a limit
point in $`[\varepsilon T,T]^k`$."

"In particular, we obtain (2) as a consequence of the theorem."

### 2.2 The method paragraph (p.2, verbatim)

"For the proof of the theorem we shall use a method that was introduced by the
second author in [5] to prove (2). The key idea is to construct a matrix, whose
rows are intervals of consecutive integers, and which contains exceptionally few
primes. The gaps between consecutive primes in the rows of this matrix are
therefore larger than normal. One can in fact prescribe the ratio between the
average size of a gap in the matrix and that of a "normal" gap by an appropriate
choice of parameters. By letting this ratio be of order T, one obtains a large
number of gaps $`d_n`$, for which the ratio $`d_n/\log{n}`$ is not greater than
T, but also not substantially smaller than T. Using a sieve result, one can
moreover show that these ratios actually fill out a positive proportion of the
interval $`[0,T]`$. In this way, one obtains the assertion of the theorem for
the case $`k=1`$. A similar, though technically more complicated, argument
yields the general case."

## 3. Section 2, Lemmas (pp.2-5)

### 3.1 Attribution sentence and good-modulus definition (p.2, verbatim)

"2. Lemmas. The proof of the theorem follows closely the argument of [5]. In
this section we state four lemmas, all of which have their counterparts in [5].
We shall give a detailed proof only for the last lemma; the first three lemmas
are obtained by minor modifications of the proofs in [5]."

"Given a constant $`C>0`$, we call an integer $`q>1`$ a good modulus, if
$`L(s,\chi)\ne0`$ for all nonprincipal characters $`\chi`$ mod q and all
$`s=\sigma+it`$ satisfying"
$$\sigma>1-\frac{C}{\log{(q(\lvert t\rvert+1))}}.$$
"The following result can be derived from a large sieve type estimate of
Gallagher [3] (cf. [5, Lemma 2])."

### 3.2 LEMMA 1, LEMMA 2 (p.3, verbatim)

"LEMMA 1. Let q be a good modulus. Then we have, uniformly for $`x\ge q^{D}`$
and $`(a,q)=1`$,"
$$\pi(2x,q,a)-\pi(x,q,a)\gg\frac{x}{\varphi(q)\log{x}}.$$
"Here D is a constant $`>1`$ that depends only on the constant C implicit in the
definition of a good modulus."

"We shall apply this result with moduli q of the form"
$$P(z)=\prod_{p\le z}p.$$
"From Page's theorem on exceptional characters one can deduce (cf. [5, Lemma
1]):"

"LEMMA 2. If C is a sufficiently small constant, then there exist arbitrarily
large values z, for which $`q=P(z)`$ is a good modulus in terms of C."

### 3.3 LEMMA 3 (p.3, verbatim)

"The next lemma gives an upper bound for the number of prime g-tuples in
arithmetic progressions. It can be deduced from any sufficiently general sieve
upper bound, for example [4, Theorem 2.3]. The lemma generalizes Lemma 3 of [5],
which corresponds to the case $`g=2`$."

"LEMMA 3. Let g be a fixed positive integer. Let $`z\ge2`$ and
$`s_1,\ldots,s_g`$ be integers satisfying"
$$0<\lvert s_i-s_j\rvert\le z^2\qquad(1\le i<j\le g).$$
"Then, for any $`R\ge2`$, we have"
$$\lvert\lbrace1\le r\le R:rP(z)+s_i\ \text{prime for}\ i=1,\ldots,g\rbrace\rvert\ll_g\frac{R}{(V(z)\log{R})^{g}},$$
"where"
$$V(z)=\prod_{p\le z}\left(1-\frac{1}{p}\right)$$
"and the implied constant depends only on g."

### 3.4 LEMMA 4 (p.3, verbatim)

"Our final lemma is one of the key ingredients in our argument. It guarantees
the existence of intervals in which the number of integers n satisfying
$`(n,P(z))=1`$ is by a prescribed factor delta smaller than the expected number.
A similar result was proved in [5, Lemma 6]."

"LEMMA 4. Let $`K\ge2`$ and $`0<\delta<1`$ be fixed constants. Then, for all
sufficiently large numbers z, there exists a number y, $`1\le y\le2P(z)`$, such
that the estimate" -- display (6), p.3:
$$\lvert\lbrace y_1<n\le y_2:(n,P(z))=1\rbrace\rvert\asymp\delta V(z)(y_2-y_1)$$
"holds for all $`y_1,y_2`$ satisfying" -- display (7), p.3:
$$y\le y_1<y_2\le y+Kz,\quad y_2-y_1\ge\frac{z}{\log{z}}.$$
"Here the constants implied in the symbol "$`\asymp`$" are absolute."

### 3.5 Proof of Lemma 4, printed in full (pp.3-5, verbatim)

"PROOF. Let K, delta and z be given as in the lemma and set
$`K_1=2K^{1/\delta}`$. We shall prove the assertion of the lemma with
$`y=N+Kz`$, where N is the least positive solution to the system of congruences"
$$N\equiv-1\bmod p\quad(p\le K_1),\qquad N\equiv0\bmod p\quad(K_1<p\le z).$$
"Since $`1\le N\le P(z)`$, we have $`1\le y\le P(z)+Kz\le2P(z)`$, as required,
provided z is sufficiently large, as we may assume."

"The definition of N implies that for any integer n, $`(n,P(z))=1`$ holds if and
only if $`m=n-N`$ satisfies the conditions" -- display (*), p.4:
$$m\not\equiv1\bmod p\quad(p\le K_1),\qquad m\not\equiv0\bmod p\quad(K_1<p\le z).$$
"The left-hand side of (6) is therefore equal to the number of integers m,
$`y_1-N<m\le y_2-N`$, that satisfy (*). Hence, putting $`x_i=y_i-N`$, we see
that (6) is equivalent to" -- display (6)', p.4:
$$\lvert\lbrace x_1<m\le x_2:(*)\rbrace\rvert\asymp\delta V(z)(x_2-x_1),$$
"while the conditions (7) can be rewritten as" -- display (7)', p.4:
$$Kz\le x_1<x_2\le2Kz,\quad x_2-x_1\ge\frac{z}{\log{z}}.$$
"To prove (6)', we note that if $`z>2K`$, as we may assume, then a positive
integer $`m\le2Kz`$ satisfying (*) is either composed entirely of prime factors
$`\le K_1`$, or of the form" -- display (**), p.4:
$$m=dp,\quad p>z,\ dp\not\equiv1\bmod p'\ (p'\le K_1).$$
"The first alternative holds for at most $`(\log{(Kz)})^{A}`$ integers
$`m\le Kz`$, with a suitable $`A=A(K_1)`$. Hence, if z is sufficiently large,
those integers contribute a negligible amount to the left-hand side of (6)'. The
contribution of the remaining integers m (i.e., those satisfying (**)) is equal
to"
$$\lvert\lbrace x_1<m\le x_2:(**)\rbrace\rvert=\sum_{d\le x_2/z}S(d),$$
"where"
$$S(d)=\lvert\lbrace\max(x_1/d,z)<p\le x_2/d:dp\not\equiv1\bmod p'(p'\le K_1)\rbrace\rvert.$$
"For $`d\le x_1/z\ (\le2K\le K_1)`$, a straightforward application of the
Eratosthenes sieve and the prime number theorem for arithmetic progressions
shows that"
$$S(d)\asymp\prod_{\substack{p'\le K_1\cr p'\nmid d}}\left(1-\frac{1}{p'}\right)\frac{x_2-x_1}{d\log{z}}=V(K_1)\frac{x_2-x_1}{\varphi(d)\log{z}}\asymp\frac{V(z)(x_2-x_1)}{\varphi(d)\log{K_1}},$$
"provided z is sufficiently large and $`x_1`$ and $`x_2`$ satisfy (7)'.
Moreover, the upper bound implicit in this estimate remains valid for
$`x_1/z<d\le x_2/z`$. Since, by (7)', $`x_1/z`$ and $`x_2/z`$ are both of order
K, we obtain"
$$\sum_{d\le x_2/z}S(d)\asymp\left(\sum_{d\le x_1/z}\frac{1}{\varphi(d)}\right)\frac{V(z)(x_2-x_1)}{\log{K_1}}\asymp\frac{\log{K}}{\log{K_1}}V(z)(x_2-x_1)\asymp\delta V(z)(x_2-x_1),$$
"using the well-known estimate"
$$\sum_{d\le u}\frac{1}{\varphi(d)}\asymp\log{u}\qquad(u\ge2)$$
"and the definition of $`K_1`$. This proves (6)' and hence the lemma."

## 4. Section 3, Proof of the theorem (pp.5-8)

### 4.1 Reduction to a box count (p.5, verbatim)

"3. Proof of the theorem. We fix a positive integer k and a real number T, which
we may assume to be sufficiently large. In what follows, the constants implied
in the symbol "$`\ll`$" are allowed to depend on k, but not on T."

"For $`\varepsilon>0`$, define an epsilon-neighborhood of $`S^{(k)}`$ as"
$$S^{(k)}_{\varepsilon}=\left\lbrace(t_1,\ldots,t_k)\in\mathbf{R}^k:\max_{i=1}^{k}\lvert t_i-\bar{t}_i\rvert\le\varepsilon\ \text{for some}\ (\bar{t}_1,\ldots,\bar{t}_k)\in S^{(k)}\right\rbrace.$$
"We shall show that for every integer $`N\ge1`$ the bound" -- display (8), p.5:
$$\lambda(S^{(k)}_{1/N}\cap[0,T]^k)\ge c(k)T^k$$
"holds with a positive constant $`c(k)`$ independent of N and T. Since the sets
$`S^{(k)}_{1/N}`$ ($`N=1,2,3,\ldots`$) form a decreasing sequence of sets, whose
intersection is the closure of $`S^{(k)}`$ and hence $`S^{(k)}`$ itself (since
$`S^{(k)}`$, as a set of limit points, is a closed set), we have"
$$\lambda(S^{(k)}\cap[0,T]^k)=\lim_{N\to\infty}\lambda(S^{(k)}_{1/N}\cap[0,T]^k).$$
"Thus, the asserted bound follows from the bound (8), and it remains to prove
the latter one."

"We fix an integer $`N\ge1`$ and divide the cube $`[0,T]^k`$ into $`N^k`$ boxes"
-- display (9), p.5:
$$B(\mathbf{n})=\left[\frac{n_1-1}{N}T,\frac{n_1}{N}T\right]\times\cdots\times\left[\frac{n_k-1}{N}T,\frac{n_k}{N}T\right]$$
$$(\mathbf{n}=(n_1,\ldots,n_k),1\le n_i\le N).$$
"We call a box good if it contains a point of $`S^{(k)}`$. It is clear from the
definition of $`S^{(k)}_{\varepsilon}`$ that every good box is contained in the
set $`S^{(k)}_{1/N}\cap[0,T]^k`$. Since the boxes $`B(\mathbf{n})`$ are disjoint
apart from a set of volume (i.e., Lebesgue measure in $`\mathbf{R}^k`$) zero,
and each of these boxes has volume $`(T/N)^k`$, we have"
$$\lambda(S^{(k)}_{1/N}\cap[0,T]^k)\ge\lvert\lbrace\text{good boxes}\rbrace\rvert\cdot\left(\frac{T}{N}\right)^{k}.$$
"Thus, to obtain (8), it suffices to show" -- display (10), p.5:
$$\lvert\lbrace\text{boxes}\ B(\mathbf{n})\ \text{containing a point of}\ S^{(k)}\rbrace\rvert\ge c(k)N^k.$$

### 4.2 Parameter choices and the matrix (pp.5-6, verbatim)

"We now construct the matrix mentioned in the introduction. We fix a number z,
for which $`q=P(z)`$ is a good modulus in the sense of Lemma 2. The lemma
guarantees the existence of arbitrarily large numbers z with this property. We
then apply Lemma 4 with $`K=T`$ and $`\delta=c/T`$, where c is a constant
depending on k that will be specified presently. The hypotheses of the lemma are
satisfied, provided $`T>\max(2,c)`$ and z is sufficiently large in terms of T,
as we may assume."

"We therefore obtain a positive number $`y\le2P(z)`$, such that (6) holds,
whenever (7) is satisfied. We now define an integer matrix $`A=(a_{rs})`$ by"
$$a_{rs}=rP(z)+s\qquad(R<r\le2R,\ y<s\le y+Tz),$$
"where"
$$R=P(z)^{D-1},$$
"D being the constant of Lemma 1, applied with $`q=P(z)`$."

"We first estimate from below the number of primes in A. The columns in the
matrix A are the arithmetic progressions"
$$\lbrace x<n\le2x:n\equiv s\bmod q\rbrace,\qquad y<s\le y+Tz,$$
"where"
$$q=P(z),\qquad x=P(z)^{D}=RP(z).$$
"Only columns with $`(s,q)=(s,P(z))=1`$ can contain primes. By Lemma 4, the
number of such columns is"
$$\asymp\delta V(z)Tz=cV(z)z.$$
"Moreover, by Lemma 1 and our assumption that $`q=P(z)`$ is a good modulus, the
number of primes in each of these columns is"
$$\gg\frac{x}{\varphi(q)\log{x}}=\frac{x}{P(z)V(z)\log{P(z)^{D}}}\asymp\frac{R}{V(z)z},$$
"since"
$$\log{P(z)^{D}}=D\sum_{p\le z}\log{p}\asymp z.$$
"Hence the entire matrix A contains"
$$\gg cV(z)z\cdot\frac{R}{V(z)z}=cR$$
"primes, where the implied constant is absolute. If we now choose the constant c
sufficiently large, then we have" -- display (11), p.6:
$$\lvert\lbrace\text{primes in}\ A\rbrace\rvert\ge3kR.$$

### 4.3 Good rows and consecutive-prime tuples (p.6, verbatim)

"By (11), a row in A contains on average at least 3k primes. Call a row "good"
if it contains at least 2k primes, and "bad" otherwise. Since the matrix A has
$`[2R]-[R]\le R+1`$ rows, at most $`(R+1)(2k-1)`$ of the primes in A can be
located in bad rows. In view of (11), we therefore have" -- display (12), p.6:
$$\lvert\lbrace\text{primes in good rows of}\ A\rbrace\rvert\ge3kR-(2k-1)(R+1)\ge kR,$$
"provided $`R\ge2k`$, as we may assume."

"Next, we estimate the number of $`(k+1)`$-tuples" -- display (13), p.6:
$$(a_{rs_1},\ldots,a_{rs_{k+1}})=(p_n,\ldots,p_{n+k})$$
"of consecutive primes in the rows of our matrix. A row with $`m>k`$ primes
contains exactly $`m-k`$ such $`(k+1)`$-tuples. If the row is good, i.e., if
$`m\ge2k`$, then $`m-k\ge m/2`$, so that the number of $`(k+1)`$-tuples is at
least half the number of primes in the row. Thus, using (12), we see that"
-- display (14), p.6:
$$\lvert\lbrace\text{tuples (13) in}\ A\rbrace\rvert\ge\tfrac{1}{2}\lvert\lbrace\text{primes in good rows of}\ A\rbrace\rvert\ge\tfrac{1}{2}kR.$$

### 4.4 Normalized difference tuples (p.7, verbatim)

"With each of the $`(k+1)`$-tuples (13) we can associate a k-tuple of
differences between consecutive primes"
$$(a_{rs_2}-a_{rs_1},\ldots,a_{rs_{k+1}}-a_{rs_k})=(s_2-s_1,\ldots,s_{k+1}-s_k)$$
$$=(p_{n+1}-p_n,\ldots,p_{n+k}-p_{n+k-1})=(d_n,\ldots,d_{n+k-1})$$
"as well as a "normalized" k-tuple of differences" -- display (15), p.7:
$$\left(\frac{s_2-s_1}{\log{x}},\ldots,\frac{s_{k+1}-s_k}{\log{x}}\right)=\left(\frac{d_n}{\log{x}},\ldots,\frac{d_{n+k-1}}{\log{x}}\right).$$
"Since for every tuple (13)" -- display (16), p.7:
$$y<s_1<\cdots<s_{k+1}\le y+Tz$$
"and"
$$\log{x}=D\log{P(z)}\ge z,$$
"if, as we may assume, z is sufficiently large, each of the tuples (15) is
contained in the cube $`[0,T]^k`$, and hence in one of the $`N^k`$ boxes
$`B(\mathbf{n})`$ defined in (9). We shall show" -- display (17), p.7:
$$\lvert\lbrace\text{boxes}\ B(\mathbf{n})\ \text{containing a k-tuple (15)}\rbrace\rvert\gg N^k,$$
"where the implied constant depends only on k."

"Having proved (17), the proof of (10), and hence that of the theorem, can be
easily completed. To this end, we repeat the above construction with a sequence
of values z tending to infinity. By choosing a suitable subsequence and using
(17), we obtain a fixed collection of $`\gg N^k`$ boxes $`B(\mathbf{n})`$, each
of which contains a tuple (15) for all values z in this subsequence. Hence, each
of those boxes contains a limit point of the tuples (15). Since the elements
$`a_{rs}`$ of our matrix A have order of magnitude x, we have, for any k-tuple
(15) associated with a $`(k+1)`$-tuple (13),"
$$\log{x}\sim\log{a_{rs_1}}=\log{p_n}\sim\log{n}.$$
"Thus, every limit point of the tuples (15) is also a limit point of the tuples
(5), hence belongs to $`S^{(k)}`$, and (10) follows."

### 4.5 The per-box upper bound (pp.7-8, verbatim)

"To prove (17), we estimate from above the number of $`(k+1)`$-tuples (13), for
which the associated tuple (15) falls into a fixed box $`B(\mathbf{n})`$, i.e.,
which satisfies" -- display (18), p.7:
$$\frac{n_i-1}{N}T\log{x}\le s_{i+1}-s_i\le\frac{n_i}{N}T\log{x}\qquad(i=1,\ldots,k).$$
"We shall show that, for each of the boxes $`B(\mathbf{n})`$," -- display (19),
p.7:
$$\lvert\lbrace\text{tuples (13) in}\ A\ \text{satisfying (18)}\rbrace\rvert\ll RN^{-k},$$
"with the implied constant depending only on k. Since, by (14), the matrix A
contains $`\gg R`$ $`(k+1)`$-tuples (13), we see that (19) implies (17)."

"To obtain (19), we note that the number of $`(k+1)`$-tuples to be estimated is
at most equal to the number of tuples $`(a_{rs_1},\ldots,a_{rs_{k+1}})`$ in our
matrix, that consist entirely of primes (though not necessarily consecutive
primes), and where $`s_1,\ldots,s_{k+1}`$ are subject to (16) and (18). Such
tuples of primes can only exist, if" -- display (20), p.7:
$$(s_i,P(z))=1\qquad(i=1,\ldots,k+1).$$
"For fixed $`s_1,\ldots,s_{k+1}`$ satisfying (16), (18) and (20), the number of
such tuples is by Lemma 3"
$$\lvert\lbrace R<r\le2R:a_{rs_i}=rP(z)+s_i\ \text{prime for}\ i=1,\ldots,k+1\rbrace\rvert\ll\frac{R}{(V(z)\log{R})^{k+1}}\asymp\frac{R}{(V(z)z)^{k+1}}.$$
"Moreover, the number of tuples $`(s_1,\ldots,s_{k+1})`$ that satisfy (16), (18)
and (20) can be estimated by Lemma 4. To this end, we note that the conditions
(16) and (18) restrict $`s_1`$ to the interval $`(y,y+Tz]`$, and each of the
numbers $`s_i`$, $`2\le i\le k+1`$, to a subinterval of $`(y,y+Tz]`$ of length
$`(T\log{x})/N\asymp Tz/N`$ (which is $`\ge z/\log{z}`$ for sufficiently large
z). Lemma 4 therefore gives"
$$\lvert\lbrace(s_1,\ldots,s_{k+1}):(16),(18),(20)\rbrace\rvert\ll(\delta TzV(z))\left(\delta\frac{T}{N}zV(z)\right)^{k}=\frac{(czV(z))^{k+1}}{N^k}.$$
"Altogether, the number of $`(k+1)`$-tuples to be estimated in (19) is bounded
by"
$$\ll\frac{R}{(V(z)z)^{k+1}}\cdot\frac{(czV(z))^{k+1}}{N^k}\asymp\frac{R}{N^k},$$
"as required."

"The proof of the theorem is now complete."

## 5. Section 4, Concluding remarks (p.8, verbatim)

"4. Concluding remarks. Rankin [7] proved a stronger form of (1), namely"
$$\limsup_{n\to\infty}\frac{d_n}{L_0(n)}>0$$
"with"
$$L_0(n)=\frac{\log{n}\log_2{n}\log_4{n}}{(\log_3{n})^2},$$
"where $`\log_k{n}`$ denotes the k times iterated logarithm. An analogous
strengthening of (2) was proved in [5]. Thus, (1) and (2) remain valid, when the
function $`\log{n}`$ is replaced by any function $`L(n)`$ satisfying"
-- display (21), p.8:
$$\log{n}\le L(n)=o(L_0(n))\qquad(n\to\infty).$$
"One might therefore ask if one can similarly replace $`\log{n}`$ by $`L(n)`$ in
the definition of the set $`S^{(k)}`$ in the theorem. By modifying slightly the
present proof and using some additional arguments from [5] and [7], one can
indeed show that the result remains valid with any slowly oscillating function
$`L(n)`$ satisfying (21) in place of $`\log{n}`$."

"It is an open problem to find a specific real number that is a limit point of
the sequence $`\lbrace d_n/\log{n}\rbrace`$. Our method is, like earlier
methods, nonconstructive and yields only the existence of (sufficiently many)
limit points. To show that a given real number is a limit point of
$`\lbrace d_n/\log{n}\rbrace`$ would probably require completely new ideas."

## 6. References as printed (pp.8-9, verbatim)

"1. P. Erdos, On the difference between consecutive primes, Quart. J. Oxford 6
(1935), 124-128. 2. ___, Problems and results on the difference of consecutive
primes, Publ. Math. Debrecen 1 (1949-1950), 33-37. 3. P. X. Gallagher, A large
sieve density estimate near sigma = 1, Invent. Math. 11 (1970), 329-339. 4. H.
Halberstam and H.-E. Richert, Sieve methods, Academic Press, New York, 1974.
5. H. Maier, Chains of large gaps between consecutive primes, Adv. in Math. 39
(1981), 257-269. 6. ___, Small differences between prime numbers, Preprint.
7. R. A. Rankin, The difference between consecutive prime numbers, J. London
Math. Soc. 13 (1938), 242-247. 8. G. Ricci, Recherches sur l'allure de la suite
$`\lbrace(p_{n+1}-p_n)/\log{p_n}\rbrace`$, Colloque sur la Theorie des Nombres,
Bruxelles, 1955, pp. 93-106. 9. E. Westzynthius, Uber die Verteilung der Zahlen,
die zu den n ersten Primzahlen teilerfremd sind, Comm. Phys. Math. Helsingfors
25 (1931), 1-37."

"DEPARTMENT OF MATHEMATICS, UNIVERSITY OF ILLINOIS, URBANA, ILLINOIS 61801";
"DEPARTMENT OF MATHEMATICS, UNIVERSITY OF GEORGIA, ATHENS, GEORGIA 30602"

## 7. Uniformity ledger

- [extract note] $`c(k)`$ in the Theorem depends only on k, and the Corollary's
  $`\varepsilon(k)=c(k)/k`$ inherits that dependence (p.2); both statements
  quantify over sufficiently large T only, not over all T.
- [extract note] D in Lemma 1 depends only on the good-modulus constant C
  (p.3); Lemma 2 requires C to be sufficiently small (p.3).
- [extract note] The implied constant of Lemma 3 depends only on g (p.3); the
  constants implied by $`\asymp`$ in Lemma 4 are stated to be absolute (p.3).
- [extract note] Throughout Section 3 the constants implied by $`\ll`$ are
  allowed to depend on k but not on T (p.5), and (8) is asserted with $`c(k)`$
  independent of both N and T.
- [extract note] Lemma 4 is applied with $`K=T`$ and $`\delta=c/T`$, c depending
  on k, and z is required to be sufficiently large in terms of T (p.5).
- [extract note] The z's are not all large z: they are drawn from the set
  supplied by Lemma 2 (p.5), and the passage to limit points takes a
  subsequence of a sequence of such z tending to infinity (p.7).

## 8. Structural map

[extract note] 1. Lemma 1 (p.3) is stated as derivable from Gallagher [3] (cf.
[5, Lemma 2]); no proof is printed.
[extract note] 2. Lemma 2 (p.3) is stated as deducible from Page's theorem (cf.
[5, Lemma 1]); no proof is printed.
[extract note] 3. Lemma 3 (p.3) is stated as deducible from [4, Theorem 2.3]; no
proof is printed. Its statement uses $`P(z)`$ and $`V(z)`$ of p.3.
[extract note] 4. Lemma 4 (pp.3-5) is the only lemma proved here; the printed
proof invokes the congruence system for N (p.4), (*), (6)', (7)', (**), the
Eratosthenes sieve and the prime number theorem for arithmetic progressions
(p.4), and $`\sum_{d\le u}1/\varphi(d)\asymp\log{u}`$ (p.5).
[extract note] 5. The reduction of the Theorem to (10) (p.5) invokes (8), (9)
and the closedness of $`S^{(k)}`$.
[extract note] 6. The matrix construction (pp.5-6) invokes Lemma 2 (to fix z)
and Lemma 4 (with $`K=T`$, $`\delta=c/T`$); the column count invokes Lemma 4 and
the per-column prime count invokes Lemma 1.
[extract note] 7. (11) follows from those two counts, (12) from (11) by the
good/bad row split, and (14) from (12) via (13).
[extract note] 8. (19) invokes Lemma 3 (for fixed $`s_1,\ldots,s_{k+1}`$ subject
to (16), (18), (20)) and Lemma 4 (for the count of admissible tuples), pp.7-8.
[extract note] 9. (17) is derived from (19) together with (14) (p.7), and (10)
follows from (17) by the subsequence argument of p.7.
[extract note] 10. Section 4 (p.8) invokes Rankin [7] and [5] and states that
the theorem's conclusion survives replacing $`\log{n}`$ by any slowly
oscillating $`L(n)`$ satisfying (21).

## FLAGS

- sha256 of the local file matches the anchor line above; verified before the
  source was opened.
- TRANSCRIPTION-UNSURE passages: 0.
- V6 (this source): confirmed against the anchored bytes -- a text layer is
  present and is OCR-corrupted throughout, as the dispatch expected. Renders are
  the evidence base; the text layer was used for navigation only.
- V8 (this source): 9 PDF pages against a steering expectation of 9; printed
  pagination 1-9 coincides with the PDF pages.
- Divergence from the dispatch's Section 4.2 attention list: it named "displays
  (1)-(5)" for the Introduction. The source prints (1)-(5) there and continues
  the same single sequence to (21), plus the named displays (*), (**), (6)' and
  (7)'; all are transcribed above.
- Divergence, same list: it named "the good-modulus definition (p.2, the
  L(s,chi) zero-free condition, verbatim)". The source's condition is stated for
  NONPRINCIPAL characters only (p.2) -- a qualifier absent from the
  corresponding definition in Maier 1985, which says "all characters".
- Source cross-reference slip, noted alongside and not repaired in the quotation
  above: p.2 writes "Erdos and Ricci [8]" while entry [8] (p.9) is G. Ricci
  alone; Erdos appears as [1] and [2].
- The matrix modulus here is $`P(z)=\prod_{p\le z}p`$, non-strict (p.3).
