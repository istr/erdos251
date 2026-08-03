# EXTRACTION: Tristan Freiberg, "Strings of congruent primes in short intervals"

Source (only evidence base): /home/istr/pro/erdos251/dossier/1005.4703v2.pdf
sha256 c08c6582df18f42324d61d8568941dc81246ee3a6404fa929c1d0ce5eafdca49
Anchor line (payloads/HASHES.txt): https://arxiv.org/pdf/1005.4703v2
Bibliographic identity: arXiv:1005.4703v2 [math.NT] 26 Aug 2010
Extraction method: text-layer with render verification
Declared scope: FULL

---

## 0. Transcription conventions

[extract note] ASCII-folded per AGENTS.md; displays are transcribed as printed inside
`$$` blocks, inline mathematics uses the repository inline delimiter, and page citations
are the printed page numbers, which coincide with the PDF pages 1-24.
[extract note] The anchored PDF carries a clean LaTeX-derived text layer. Transcription
was made from that layer and every quoted passage was verified against 200-dpi page
rasters of the page cited.
[extract note] The source uses several distinguished alphabets: a calligraphic H for the
set of linear forms, transcribed $`\mathcal{H}`$; a calligraphic L for the weighted sum,
transcribed $`\mathcal{L}`$; a calligraphic P for the prime set of Section 5,
transcribed $`\mathcal{P}`$; a calligraphic S in Section 5 and calligraphic T and E in
Section 4, transcribed
$`\mathcal{S}`$, $`\mathcal{T}`$, $`\mathcal{E}`$; and a Fraktur S for the singular
series, transcribed $`\mathfrak{S}`$.
[extract note] The source prints no journal reference on the paper; it is an arXiv
preprint throughout.

---

## 1. Front matter (p.1, verbatim)

"STRINGS OF CONGRUENT PRIMES IN SHORT INTERVALS"; "TRISTAN FREIBERG";
"arXiv:1005.4703v2 [math.NT] 26 Aug 2010".

"ABSTRACT. Fix $`\epsilon>0`$, and let $`p_1=2,p_2=3,\ldots`$ be the sequence of all
primes. We prove that if $`(q,a)=1`$ then there are infinitely many pairs
$`p_r,p_{r+1}`$ such that $`p_r\equiv p_{r+1}\equiv a\bmod q`$ and
$`p_{r+1}-p_r<\epsilon\log{p_r}`$. The proof combines the ideas of Shiu [9] and
Goldston-Pintz-Yildirim [6]."

## 2. Section 1, Introduction (p.1, verbatim)

"1. INTRODUCTION. Fix any $`\epsilon>0`$. In 2005, Goldston, Pintz and Yildirim proved
[4, 6] that there are arbitrarily large x for which there are at least two primes in the
interval $`(x,x+\epsilon\log{x}]`$, thus establishing the longstanding conjecture that
there are infinitely many pairs of consecutive primes $`p_r,p_{r+1}`$ with
$`p_{r+1}-p_r<\epsilon\log{p_r}`$."

"In [5] they extended their original argument to prove that there are arbitrarily large
x for which there are at least two primes in the interval $`(x,x+\epsilon\log{x}]`$
which are both in the arithmetic progression $`a\bmod q`$, provided $`(q,a)=1`$. However
one cannot deduce that these are consecutive primes for there might be a prime
in-between them that is not $`\equiv a\bmod q`$. Hence one can only deduce that either
there are infinitely many pairs of consecutive primes $`p_r\equiv p_{r+1}\equiv a\bmod q`$
with $`p_{r+1}-p_r<\epsilon\log{p_r}`$, or that there are infinitely many triples of
consecutive primes $`p_r,p_{r+1},p_{r+2}`$ with $`p_{r+2}-p_r<\epsilon\log{p_r}`$.
Presumably both statements are true but one can only deduce that one of them is true,
and one does not know which one, from the result in [5]."

"In [9], Shiu proved an old conjecture of Chowla that there are infinitely many pairs of
consecutive primes $`p_r,p_{r+1}`$ which are both $`\equiv a\bmod q`$. Indeed he was
even able to extend this to k consecutive primes. In this paper we will combine the
methods of Goldston-Pintz-Yildirim and of Shiu to establish the following hybrid of
those results:"

"Theorem 1.1. Let $`q\ge3`$ and a be integers with $`(q,a)=1`$, and fix any
$`\epsilon>0`$. There exist infinitely many pairs of consecutive primes
$`p_r,p_{r+1}`$ such that $`p_r\equiv p_{r+1}\equiv a\bmod q`$ and
$`p_{r+1}-p_r<\epsilon\log{p_r}`$."

## 3. Section 2, Preliminaries (pp.2-4)

"2. Preliminaries. In this section we will state two key technical propositions, to be
proved in sections 4 and 5. The first proposition requires some preparation. We begin by
quoting the Landau-Page theorem, a proof of which can be found in [2, Chapter 14]. This
theorem is used to handle problems arising from possible irregularities in the
distribution of primes, hence in Bombieri-Vinogradov type theorems (see Lemma 4.2),
caused by potential Siegel zeros."

"Lemma 2.1 (Landau-Page theorem). There exists a constant c such that the following
holds for any $`Y>c`$. There is at most one integer $`q_0\le Y`$, and at most one real
primitive character $`\chi_0`$ mod $`q_0`$, such that"
$$L(1-\delta,\chi_0,q_0)=0\ \text{for some}\ \delta\le\frac{1}{3\log{Y}}.$$
"If $`q_0`$ exists, then $`q_0>(\log{Y})^2`$. We call $`\chi_0`$ an exceptional character
and $`q_0`$ an exceptional modulus."

"Throughout, we fix a number $`\epsilon>0`$, we let H be a real parameter tending
monotonically to infinity, and we set $`N:=\exp(H/\epsilon)`$, that is
$`H=\epsilon\log{N}`$. If there is an exceptional modulus
$`q_0:=q_0(H)\le\exp(H/\epsilon(\log{(H/\epsilon)})^2)=N^{1/(\log{}\log{N})^2}`$, let
$`p_0:=p_0(H)`$ be its greatest prime factor; otherwise let $`p_0=1`$."

"For all sufficiently large H, either" -- display (2.1), p.2:
$$p_0=1\ \text{or}\ p_0\ \text{is a prime with}\ p_0>\log{H}.$$
"To see this, note that all real primitive characters are products of Legendre symbols
with different odd primes, and possibly either the unique real character mod 4 or one of
the two primitive real characters mod 8. Thus if $`q_0`$ exists it is of the form
$`2^{\alpha}p_1\cdots p_k`$, where $`\alpha\le3`$ and the $`p_i`$'s are distinct odd
primes. If this is the case and $`p_0\le\log{H}`$, then the prime number theorem implies
$`q_0\ll\exp((1+o(1))\log{H})\ll\log{N}`$, but Lemma 2.1 states that
$`q_0>(\log{N}/(\log{}\log{N})^2)^2`$."

"We let $`Q:=Q(H)`$ be a positive integer, upon which we will impose the following
conditions:" -- displays (2.2)-(2.5), p.2:
$$Q\ \text{is composed only of primes}\ p\le H,$$
$$Q\ \text{is divisible by all primes}\ p\le\log{H},$$
$$Q\le\exp\left(cH/(\log{H})^2\right)\ \text{for some constant}\ c>0,$$
$$\text{if}\ p_0(H)\ne1\ \text{then}\ p_0(H)\ \text{does not divide}\ Q.$$
"We let" -- display (2.6), p.3:
$$\mathcal{H}:=\lbrace Qx+h_1,\ldots,Qx+h_k\rbrace,\qquad h_1,\ldots,h_k\in[1,H]\cap\mathbb{Z},$$
"denote a set of distinct linear forms, and we define" -- display (2.7), p.3:
$$\Lambda_R(n;\mathcal{H},j):=\frac{1}{j!}{\sum_{\substack{d\mid P(n;\mathcal{H})\cr d\le R}}}'\mu(d)(\log{R/d})^{j},$$
"where $`{\sum}'`$ denotes summation over indices coprime with $`Qp_0`$, and"
-- display (2.8), p.3:
$$P(n;\mathcal{H}):=(Qn+h_1)\cdots(Qn+h_k).$$
"Finally, we let"
$$\vartheta(n):=\begin{cases}\log{n}&\text{if n is prime,}\cr0&\text{otherwise.}\end{cases}$$

"Proposition 2.2. Given $`\epsilon>0`$ and sufficiently large H, let N and
$`p_0=p_0(H)`$ be as defined earlier, and let $`Q=Q(H)`$ be a positive integer
satisfying (2.2) - (2.5). Fix positive integers k and $`\ell`$, and let
$`\mathcal{H}=\lbrace Qx+h_1,\ldots,Qx+h_k\rbrace`$ be a set of distinct linear forms
with $`h_1,\ldots,h_k\in[1,H]\cap\mathbb{Z}`$ and $`(Q,h_1,\ldots,h_k)=1`$. Let
$`h\in[1,H]\cap\mathbb{Z}`$ and suppose $`(Q,h)=1`$, and let
$`R=N^{1/4-\epsilon'}`$ for some $`\epsilon'\in(0,1/4)`$. As $`H\to\infty`$, we have"
-- display (2.9), p.3:
$$\frac{1}{N}\left(\frac{\phi(Q)}{Q}\right)^{k}\sum_{N<n\le2N}\Lambda_R(n;\mathcal{H},k+\ell)^{2}\sim\binom{2\ell}{\ell}\frac{(\log{R})^{k+2\ell}}{(k+2\ell)!}$$
"and" -- display (2.10), p.3:
$$\frac{1}{N}\left(\frac{\phi(Q)}{Q}\right)^{k}\sum_{N<n\le2N}\vartheta(Qn+h)\Lambda_R(n;\mathcal{H},k+\ell)^{2}\sim\begin{cases}\dfrac{Q}{\phi(Q)}\dbinom{2\ell}{\ell}\dfrac{(\log{R})^{k+2\ell}}{(k+2\ell)!}&\text{if}\ Qx+h\notin\mathcal{H},\cr\dbinom{2(\ell+1)}{\ell+1}\dfrac{(\log{R})^{k+2\ell+1}}{(k+2\ell+1)!}&\text{if}\ Qx+h\in\mathcal{H}.\end{cases}$$

"Proposition 2.3. Let $`q\ge3`$ and a be integers with $`(q,a)=1`$, and for a given H,
let $`p_0=p_0(H)`$ be as defined earlier. There is an infinite sequence of integers
$`H_1<H_2<\ldots`$ such that for any i, taking $`H=H_i`$, there exists a positive integer
$`Q=Q(H)`$, divisible by q and satisfying (2.2) - (2.5), such that"
-- display (2.11), p.3:
$$\lvert S\rvert-\lvert T\rvert\gg_q H\left(\frac{\phi(Q)}{Q}\right),$$
"where" -- display (2.12), p.4:
$$S=S(H):=\lbrace h\in(0,H]:(Q,h)=1\ \text{and}\ h\equiv a\bmod q\rbrace,$$
$$T=T(H):=\lbrace h\in(0,H]:(Q,h)=1\ \text{and}\ h\not\equiv a\bmod q\rbrace.$$
"The implied constant in (2.11) depends at most on q."

## 4. Section 3, Proof of Theorem 1.1 (pp.4-5)

"3. Proof of Theorem 1.1. Fix integers $`q\ge3`$ and a with $`(q,a)=1`$. Recall that
$`H=\epsilon\log{N}`$, with $`\epsilon>0`$ fixed, and $`p_0`$ is the greatest prime
factor of the exceptional modulus $`q_0\le N^{1/(\log{}\log{N})^2}`$, if it exists,
otherwise $`p_0=1`$. We choose H, $`Q=Q(H)`$, $`S=S(H)`$, and $`T=T(H)`$ as in
Proposition 2.3, so that Q is divisible by q and satisfies (2.2) - (2.5), and"
-- display (3.1), p.4:
$$\frac{Q}{\phi(Q)}\frac{\lvert S\rvert-\lvert T\rvert}{\log{N}}\ge c(q)\epsilon$$
"for some constant $`c(q)>0`$, depending on q at most."

"We fix positive integers $`k,\ell`$ (to be specified later), and we let
$`\mathcal{H}=\lbrace Qx+h_1,\ldots,Qx+h_k\rbrace`$ be a set of distinct linear forms
such that, for each i, $`h_i\in[1,H]\cap a\bmod q`$ and $`(Q,h_i)=1`$. We let
$`R=N^{1/4-\epsilon'}`$ with $`0<\epsilon'<1/4`$ (to be specified later), and we put"
$$\mathcal{L}:=\frac{1}{N}\left(\frac{\phi(Q)}{Q}\right)^{k}\sum_{N<n\le2N}\left(\sum_{h\in S}\vartheta(Qn+h)-\sum_{h\in T}\vartheta(Qn+h)-\log{3QN}\right)\Lambda_R(n;\mathcal{H},k+\ell)^{2}.$$
"We now show that if $`\mathcal{L}>0`$ for a sequence of numbers N, tending to infinity,
then Theorem 1.1 follows."

"Let"
$$A_n:=\lbrace p\in(Qn,Qn+H]:p\equiv a\bmod q\rbrace=\lbrace p:p=Qn+h,h\in S\rbrace$$
$$B_n:=\lbrace p\in(Qn,Qn+H]:p\not\equiv a\bmod q\rbrace=\lbrace p:p=Qn+h,h\in T\rbrace.$$
"If $`\mathcal{L}>0`$, then there is some $`n\in(N,2N]`$ such that"
$$\lvert A_n\rvert\log{(Qn+H)}\ge\sum_{h\in S}\vartheta(Qn+h)>\sum_{h\in T}\vartheta(Qn+h)+\log{3QN}\ge\lvert B_n\rvert\log{Qn}+\log{3QN}.$$
"Now"
$$\lvert A_n\rvert\log{(1+H/Qn)}\le\lvert A_n\rvert H/Qn\le H^{2}/QN<\log{(3/2)}$$
"if N is sufficiently large, and so"
$$\log{(3/2)}+(\lvert A_n\rvert-\lvert B_n\rvert)\log{Qn}>\log{3QN}$$
"and hence, as $`n\le2N`$, $`\lvert A_n\rvert-\lvert B_n\rvert>1`$. But as these are
integers, $`\lvert A_n\rvert\ge\lvert B_n\rvert+2`$, and so, by the pigeonhole
principle, $`A_n`$ contains a pair of consecutive primes $`p_r,p_{r+1}`$. These primes
satisfy $`p_{r+1}-p_r<H<\epsilon\log{QN}<\epsilon\log{p_r}`$."

"Now, by our choice of $`\mathcal{H}`$, a straightforward application of Proposition 2.2
yields"
$$\mathcal{L}=\binom{2\ell}{\ell}\frac{(\log{R})^{k+2\ell}}{(k+2\ell)!}\times\left\lbrace\frac{Q}{\phi(Q)}\sum_{\substack{h\in S\cr Qx+h\notin\mathcal{H}}}1+\frac{2(2\ell+1)}{\ell+1}\frac{\log{R}}{k+2\ell+1}\sum_{\substack{h\in S\cr Qx+h\in\mathcal{H}}}1-\frac{Q}{\phi(Q)}\sum_{h\in T}1-(1+o(1))\log{3QN}\right\rbrace.$$
"We have"
$$\sum_{\substack{h\in S\cr Qx+h\in\mathcal{H}}}1=k,\qquad\sum_{\substack{h\in S\cr Qx+h\notin\mathcal{H}}}1=\lvert S\rvert-k,$$
"$`\log{R}=(1/4-\epsilon')\log{N}`$, and $`\log{3QN}\sim\log{N}`$ by (2.4), therefore"
$$\mathcal{L}=\binom{2\ell}{\ell}\frac{(\log{R})^{k+2\ell}}{(k+2\ell)!}\log{N}\times\left\lbrace\frac{Q}{\phi(Q)}\frac{\lvert S\rvert-\lvert T\rvert}{\log{N}}+\frac{2(2\ell+1)}{\ell+1}\frac{k}{k+2\ell+1}\left(\frac{1}{4}-\epsilon'\right)-(1+o(1))\right\rbrace.$$
"We have written $`o(1)`$ for $`kQ/(\phi(Q)\log{N})`$, because
$`Q/\phi(Q)\ll\log{}\log{Q}\ll\log{}\log{N}`$."

"By choosing $`\ell=[\sqrt{k}]`$ and k sufficiently large, the bracketed expression
$`\lbrace\cdots\rbrace`$ above is, by (3.1),"
$$\ge c(q)\epsilon+1-5\epsilon'-(1+o(1))=c(q)\epsilon-5\epsilon'-o(1).$$
"By choosing $`\epsilon'=c(q)\epsilon/10`$ (we may assume that $`\epsilon`$ is small
enough so that $`\epsilon'<1/4`$), we deduce that" -- display (3.2), p.5:
$$\mathcal{L}\gg_k c(q)\epsilon(\log{N})^{k+2\ell+1}$$
"holds if N is sufficiently large. By Proposition 2.3, we may choose H, equivalently N,
from a sequence of numbers tending to infinity, and Theorem 1.1 follows."

## 5. Section 4, Proof of Proposition 2.2 (pp.6-11)

"4. Proof of Proposition 2.2. The estimates (2.9) and (2.10) of Proposition 2.2 are
essentially the same as estimates already in the literature, so we will only outline a
proof of each of them, referring to [3] and [5] for details."

"Let $`Q=Q(H)`$ satisfy (2.2) and (2.3). For a set of distinct linear forms
$`\mathcal{H}`$, as in (2.6), and positive integers d, we define"
$$\Omega(d)=\Omega(d;\mathcal{H}):=\lbrace n\bmod d:P(n;\mathcal{H})\equiv0\bmod d\rbrace,$$
"where $`P(n;\mathcal{H})`$ is as in (2.8). A Chinese remainder theorem argument shows
that $`n\bmod d\in\Omega(d)`$ if and only if $`p^{r}\Vert P(n;\mathcal{H})`$ for every
$`p^{r}\Vert d`$, and so $`\lvert\Omega(d)\rvert`$ defines a multiplicative function of
d. Thus, if we define" -- display (4.1), p.6:
$$\lambda_R(d;j):=\begin{cases}\frac{1}{j!}\mu(d)(\log{R/d})^{j}&\text{if}\ d\le R,\cr0&\text{if}\ d>R,\end{cases}$$
"we see from (2.7) that" -- display (4.2), p.6:
$$\Lambda_R(n;\mathcal{H},j):=\frac{1}{j!}{\sum_{\substack{d\mid P(n;\mathcal{H})\cr d\le R}}}'\mu(d)(\log{R/d})^{j}={\sum_{n\bmod d\in\Omega(d)}}'\lambda_R(d;j).$$
"We call $`\mathcal{H}`$ admissible if $`\lvert\Omega(p)\rvert<p`$ for all p, and one can
prove that this is equivalent to $`\mathfrak{S}(\mathcal{H})\ne0`$, where"
$$\mathfrak{S}(\mathcal{H}):=\prod_{p}\left(1-\frac{\lvert\Omega(p)\rvert}{p}\right)\left(1-\frac{1}{p}\right)^{-k}$$
"is the singular series for $`\mathcal{H}`$."

"Lemma 4.1. Let H be a real number, let $`Q=Q(H)`$ be a positive integer satisfying
(2.2) and (2.3), and let $`\mathcal{H}`$ be as in (2.6), with k fixed. We have"
-- display (4.3), p.6:
$$\lvert\Omega(p)\rvert=k\quad\text{for all}\quad p>H.$$
"For $`k\le\log{H}`$, $`\mathcal{H}`$ is admissible if and only if
$`(Q,h_1\cdots h_k)=1`$. Moreover, as $`H\to\infty`$, for $`(Q,h_1\cdots h_k)=1`$ we
have" -- display (4.4), p.6:
$$\mathfrak{S}(\mathcal{H})\sim\left(\frac{Q}{\phi(Q)}\right)^{k}.$$

"Proof. For primes p that do not divide Q, we have"
$$\Omega(p)=\lbrace-h_1Q^{-1},\ldots,-h_kQ^{-1}\rbrace\bmod p,$$
"and hence $`1\le\lvert\Omega(p)\rvert\le\min(k,p)`$. For such p, we have
$`\lvert\Omega(p)\rvert=k`$ if and only if the $`-h_iQ^{-1}`$ are all distinct modulo p,
that is if and only if $`p\nmid\Delta`$, where"
$$\Delta=\Delta(\mathcal{H}):=\prod_{1\le i<j\le k}\lvert h_i-h_j\rvert.$$
"By (2.2), $`p>H`$ implies $`p\nmid Q`$, and since $`1\le\lvert h_i-h_j\rvert\le H`$ for
every i, j, $`p>H`$ also implies $`p\nmid\Delta`$, and hence
$`\lvert\Omega(p)\rvert=k`$. We have established (4.3)."

"If some prime p divides $`(Q,h_1\cdots h_k)`$, then
$`P(n;\mathcal{H})\equiv h_1\cdots h_k\equiv0\bmod p`$ for every $`n\bmod p`$, hence
$`\lvert\Omega(p)\rvert=p`$, and so $`\mathcal{H}`$ is not admissible if
$`(Q,h_1\cdots h_k)\ne1`$. If $`(Q,h_1\cdots h_k)=1`$, then
$`P(n;\mathcal{H})\equiv h_1\cdots h_k\not\equiv0\bmod p`$, and hence
$`\lvert\Omega(p)\rvert=0`$, for every p dividing Q. For every other p we have
$`1\le\lvert\Omega(p)\rvert\le\min(k,p)`$. Then for $`k\le\log{H}`$ and $`p\nmid Q`$, we
have $`1\le\lvert\Omega(p)\rvert\le k\le\log{H}<p`$ by (2.3), hence $`\mathcal{H}`$ is
admissible."

"Now assume H is large enough so that $`\log{H}\ge2k`$, and suppose
$`(Q,h_1\cdots h_k)=1`$. Then for (4.4), since $`\lvert\Omega(p)\rvert=0`$ if
$`p\mid Q`$, it suffices to show that" -- display (4.5), p.7:
$$\mathfrak{S}'(\mathcal{H}):=\prod_{p\nmid Q}\left(1-\frac{\lvert\Omega(p)\rvert}{p}\right)\left(1-\frac{1}{p}\right)^{-k}\sim1$$
"as H tends to infinity. We break $`\mathfrak{S}'(\mathcal{H})`$ into two products
according as $`p\mid\Delta`$ or $`p\nmid\Delta`$, and use the fact that
$`\lvert\Omega(p)\rvert=k`$ for $`p\nmid Q\Delta`$:" -- display (4.6), p.7:
$$\mathfrak{S}'(\mathcal{H})=\prod_{p\nmid Q}\left(1-\frac{k}{p}\right)\left(1+\frac{k-\lvert\Omega(p)\rvert}{p-k}\right)\left(1-\frac{1}{p}\right)^{-k}$$
$$=\prod_{p\nmid Q}\left(1-\frac{k}{p}\right)\left(1-\frac{1}{p}\right)^{-k}\prod_{\substack{p\nmid Q\cr p\mid\Delta}}\left(1+\frac{k-\lvert\Omega(p)\rvert}{p-k}\right).$$
"In this product $`p-k\ne0`$ because, by (2.3), $`p\nmid Q`$ implies
$`p>\log{H}\ge2k`$. For the same reason, the logarithm of the first product of the last
line of (4.6) is"
$$\sum_{p\nmid Q}\left\lbrace\left(-\frac{k}{p}-\frac{k^{2}}{2p^{2}}-\cdots\right)-k\left(-\frac{1}{p}-\frac{1}{2p^{2}}-\cdots\right)\right\rbrace\ll k^{2}\sum_{p>\log{H}}\frac{1}{p^{2}}\ll\frac{k^{2}}{\log{H}\log{}\log{H}}.$$
"For the second product, note that since $`k/\log{H}\le1/2`$, we have"
$$0<\frac{k-\lvert\Omega(p)\rvert}{p-k}\le\frac{k}{p-k}\le\frac{2k}{p}<1.$$
"Hence the logarithm of the second product is"
$$\le\sum_{\substack{p\mid\Delta\cr p>\log{H}}}\log{\left(1+\frac{k-\lvert\Omega(p)\rvert}{p-k}\right)}\ll\sum_{\substack{p\mid\Delta\cr p>\log{H}}}\frac{k}{p}\ll\frac{k}{\log{H}}\sum_{p\mid\Delta}1\ll\frac{k\log{\Delta}}{\log{H}\log{}\log{\Delta}}\ll\frac{k^{3}}{\log{}\log{H}}$$
"by the prime number theorem, because $`\Delta\le H^{\binom{k}{2}}`$. Exponentiating and
letting H tend to infinity yields (4.5)."

"We now assume all of the hypotheses of Proposition 2.2. The proof of (2.9) is almost
identical to the proof of Lemma 1 of [3], the only difference being that primes
$`p\mid Qp_0`$ are excluded from the representation of $`F(s_1,s_2;\Omega)`$, where"
$$F(s_1,s_2;\Omega):={\sum_{d_1,d_2}}'\mu(d_1)\mu(d_1)\frac{\lvert\Omega([d_1,d_2])\rvert}{[d_1,d_2]d_1^{s_1}d_2^{s_2}}=\prod_{p\nmid Qp_0}\left(1-\frac{\lvert\Omega(p)\rvert}{p}\left(\frac{1}{p^{s_1}}+\frac{1}{p^{s_2}}-\frac{1}{p^{s_1+s_2}}\right)\right)$$
"in the region of absolute convergence. Since $`\lvert\Omega(p)\rvert=k`$ for $`p>H`$ by
(4.3), we put"
$$G(s_1,s_2;\Omega):=F(s_1,s_2;\Omega)\left(\frac{\zeta(s_1+1)\zeta(s_2+1)}{\zeta(s_1+s_2+1)}\right)^{k}.$$
"In the proof of Lemma 1 of [3], $`G(0,0;\Omega)=\mathfrak{S}(\mathcal{H})`$, but in our
situation, we have"
$$G(0,0;\Omega)=\prod_{p\nmid Qp_0}\left(1-\frac{\lvert\Omega(p)\rvert}{p}\right)\prod_{p}\left(1-\frac{1}{p}\right)^{-k}=\mathfrak{S}(\mathcal{H})\prod_{p\mid p_0}\left(1-\frac{\lvert\Omega(p)\rvert}{p}\right)^{-1},$$
"because $`(Q,p_0)=1`$ and $`\lvert\Omega(p)\rvert=0`$ if $`p\mid Q`$. The last product
is $`\sim1`$ by (2.1). Now applying (4.4), and proceeding as in the proof of Lemma 1 of
[3], (2.9) is established."

"The proof of (2.10) follows that of Lemma 2 of [3] very closely: there is one important
difference concerning the error"
$$E^{*}(N,q):=\max_{x\le N}\max_{(a,q)=1}\left\lvert\sum_{\substack{p\le x\cr p\equiv a\bmod q}}\log{p}-\frac{x}{\phi(q)}\right\rvert.$$
"The usual Bombieri-Vinogradov theorem will not suffice here, but the next lemma, which
is Lemma 2 of [5], will."

"Lemma 4.2. Let Q be an integer and Y, M be numbers such that" -- display (4.7), p.8:
$$Q^{2}\le Y\le M,\qquad\exp\left(2\sqrt{\log{M}}\right)\le Y.$$
"If there is an exceptional modulus $`q_0\le Y`$, suppose $`p_0\nmid Q`$ for some
$`p_0\mid q_0`$; otherwise, let $`p_0=1`$. If" -- display (4.8), p.8:
$$R^{*}:=M^{1/2}Q^{-3}\exp\left(-\sqrt{\log{M}}\right),$$
"then we have, with explicitly calculable positive constants $`c_1`$ and $`c_2`$,"
-- display (4.9), p.9:
$$\sum_{\substack{D\le R^{*}\cr(D,Qp_0)=1}}E^{*}(M,QD)\le c_1\frac{M}{Q}\exp\left(-\frac{c_2\log{M}}{\log{Y}}\right).$$

"By (2.2) - (2.5), we see that (4.7) is satisfied with"
$$Y=\exp\left(2cH/(\log{H})^{2}\right)=N^{2c\epsilon(1+o(1))/(\log{}\log{N})^{2}},$$
"and $`M=3QN`$. We also have"
$$R^{2}=N^{1/2-2\epsilon'}\le R^{*}=(3QN)^{1/2}Q^{-3}\exp\left(-\sqrt{\log{3QN}}\right),$$
"for all sufficiently large N, and"
$$c_2\log{M}/\log{Y}=c_2(1+o(1))\log{N}/\log{Y}=c_2(1+o(1))(\log{}\log{N})^{2}/2c\epsilon.$$
"Letting $`c_3=c_2/12c\epsilon`$ and putting this into (4.9), we deduce from Lemma 4.2
that" -- display (4.10), p.9:
$${\sum_{D\le R^{2}}}'E^{*}(3QN,QD)\ll N(\log{N})^{-5c_3\log{}\log{N}}$$
"for all sufficiently large N."

"Now, abbreviating $`\lambda_R(d;k+\ell)`$ to $`\lambda_d`$, by (4.2) we have"
-- display (4.11), p.9:
$$\sum_{N<n\le2N}\vartheta(Qn+h)\Lambda_R(n;\mathcal{H},k+\ell)^{2}={\sum_{d_1,d_2}}'\lambda_{d_1}\lambda_{d_2}\sum_{\substack{N<n\le2N\cr[d_1,d_2]\mid P(n;\mathcal{H})}}\vartheta(Qn+h)$$
$$={\sum_{d_1,d_2}}'\lambda_{d_1}\lambda_{d_2}\sum_{\substack{m\bmod[d_1,d_2]\cr\in\Omega([d_1,d_2])}}\ \sum_{\substack{QN+h<p\le2QN+h\cr p\equiv h\bmod Q\cr p\equiv Qm+h\bmod[d_1,d_2]}}\log{p}.$$
"We may assume $`(Qm+h,[d_1,d_2])=(Q,[d_1,d_2])=1`$ in the last sum, so we define"
$$\Omega^{*}(d):=\Omega(d)\setminus\lbrace m\bmod d:(Qm+h,d)\ne1\rbrace.$$
"For $`d_1,d_2`$ with $`(Q,[d_1,d_2])=1`$ and
$`m\bmod[d_1,d_2]\in\Omega^{*}([d_1,d_2])`$, we let $`h_m\bmod Q[d_1,d_2]`$ be the
unique congruence class mod $`Q[d_1,d_2]`$ satisfying $`h_m\equiv h\bmod Q`$ and
$`h_m\equiv Qm+h\bmod[d_1,d_2]`$. Thus, the last sum in (4.11) is equal to"
$$\sum_{\substack{QN+h<p\le2QN+h\cr p\equiv h_m\bmod Q[d_1,d_2]}}\log{p}=\frac{2QN+h}{\phi(Q[d_1,d_2])}-\frac{QN+h}{\phi(Q[d_1,d_2])}+O\left(E^{*}(3QN,Q[d_1,d_2])\right),$$
"and (4.11) becomes" -- display (4.12), p.9:
$$\frac{QN}{\phi(Q)}\mathcal{T}^{*}+O(\mathcal{E}^{*}),$$
"with"
$$\mathcal{T}^{*}:={\sum_{d_1,d_2}}'\frac{\lambda_{d_1}\lambda_{d_2}\lvert\Omega^{*}([d_1,d_2])\rvert}{\phi([d_1,d_2])},\qquad\mathcal{E}^{*}:={\sum_{d_1,d_2}}'\lvert\lambda_{d_1}\lambda_{d_2}\rvert\lvert\Omega^{*}([d_1,d_2])\rvert E^{*}(3QN,Q[d_1,d_2]).$$
"Now from the definition (4.1) it is clear that
$`\lvert\lambda_d\rvert\le(\log{R})^{k+\ell}`$. Also, as we saw in the beginning of the
proof of Lemma 4.1, since $`(Q,h_1\cdots h_k)=1`$ we have $`\lvert\Omega(p)\rvert\le k`$
for all p, and so
$`\lvert\Omega^{*}(d)\rvert\le\lvert\Omega(d)\rvert\le k^{\omega(d)}`$ for squarefree d.
Thus"
$$\mathcal{E}^{*}\le(\log{R})^{2(k+\ell)}{\sum_{D\le R^{2}}}'\mu^{2}(D)k^{\omega(D)}E^{*}(3QN,QD)\sum_{[d_1,d_2]=D}1=(\log{R})^{2(k+\ell)}{\sum_{D\le R^{2}}}'\mu^{2}(D)(3k)^{\omega(D)}E^{*}(3QN,QD).$$
"By the trivial inequality"
$$E^{*}(3QN,QD)\ll\frac{QN\log{QN}}{QD}\ll\frac{N\log{N}}{D},$$
"and the Cauchy-Schwarz inequality, we have"
$${\sum_{D\le R^{2}}}'\mu^{2}(D)(3k)^{\omega(D)}E^{*}(3QN,QD)\ll\sqrt{N\log{N}}\left(\sum_{D\le R^{2}}\frac{\mu^{2}(D)(3k)^{2\omega(D)}}{D}\right)^{1/2}\left({\sum_{D\le R^{2}}}'E^{*}(3QN,QD)\right)^{1/2}.$$
"For positive integers $`\kappa`$, we have"
$$\sum_{D\le R^{2}}\frac{\mu^{2}(D)\kappa^{\omega(D)}}{D}=\sum_{d\cdots d_{\kappa}\le R^{2}}\frac{\mu^{2}(d_1)\cdots\mu^{2}(d_{\kappa})}{d_1\cdots d_{\kappa}}\ll(\log{R^{2}})^{\kappa}\ll(\log{N})^{\kappa},$$
"so combining and applying (4.10) yields" -- display (4.13), p.10:
$$\mathcal{E}^{*}\ll N\frac{(\log{N})^{2(k+\ell)+(3k)^{2}/2+1/2}}{(\log{N})^{-2c_3\log{}\log{N}}}\le N(\log{N})^{-c_3\log{}\log{N}}.$$

"We will now evaluate $`\mathcal{T}^{*}`$, assuming first that
$`Qx+h\notin\mathcal{H}`$. Let $`\mathcal{H}^{+}=\mathcal{H}\cup\lbrace Qx+h\rbrace`$
and observe that for $`p\nmid Q`$,"
$$\lvert\Omega^{*}(p)\rvert=\lvert\Omega(p;\mathcal{H}^{+})\rvert-1:=\lvert\Omega^{+}(p)\rvert-1.$$
"As with $`\lvert\Omega(d)\rvert`$, a Chinese remainder theorem argument shows that
$`\lvert\Omega^{*}(d)\rvert`$ defines a multiplicative function of d. Thus"
$$\lvert\Omega^{*}([d_1,d_2])\rvert=\prod_{p\mid[d_1,d_2]}\left(\lvert\Omega^{+}(p)\rvert-1\right),$$
"provided $`[d_1,d_2]`$ is squarefree and $`(Q,[d_1,d_2])=1`$, as is the case for
$`d_1,d_2`$ appearing in the sum defining $`\mathcal{T}^{*}`$."

"We now proceed as in the proof of Lemma 2 of [3]: again, the only modification necessary
is to $`G(0,0;\Omega^{+})`$. First note that"
$$\mathfrak{S}(\mathcal{H}^{+})=\prod_{p}\left(\frac{p-\lvert\Omega^{+}(p)\rvert}{p}\right)\left(\frac{p}{p-1}\right)\left(1-\frac{1}{p}\right)^{-k}=\prod_{p}\left(1-\frac{\lvert\Omega^{+}(p)\rvert-1}{p-1}\right)\left(1-\frac{1}{p}\right)^{-k}.$$
"By (4.3), $`\lvert\Omega^{+}(p)\rvert=\lvert\mathcal{H}^{+}\rvert=k+1`$ for $`p>H`$, and
if"
$$G(s_1,s_2;\Omega^{+}):=\prod_{p\nmid Qp_0}\left(1-\frac{\lvert\Omega^{+}(p)\rvert-1}{p-1}\left(\frac{1}{p^{s_1}}+\frac{1}{p^{s_1}}-\frac{1}{p^{s_1+s_2}}\right)\right)\cdot\left(\frac{\zeta(s_1+1)\zeta(s_2+1)}{\zeta(s_1+s_2+1)}\right)^{k},$$
"then"
$$G(0,0;\Omega^{+})=\prod_{p\nmid Qp_0}\left(1-\frac{\lvert\Omega^{+}(p)\rvert-1}{p-1}\right)\prod_{p}\left(1-\frac{1}{p}\right)^{-k}$$
$$=\mathfrak{S}(\mathcal{H}^{+})\prod_{p\mid Q}\left(1+\frac{1}{p-1}\right)^{-1}\prod_{p\mid p_0}\left(1-\frac{\lvert\Omega^{+}(p)\rvert-1}{p-1}\right)^{-1}\sim\left(\frac{Q}{\phi(Q)}\right)^{k},$$
"by Lemma 4.1 and (2.1). Therefore" -- display (4.14), p.11:
$$\mathcal{T}^{*}\sim\left(\frac{Q}{\phi(Q)}\right)^{k}\binom{2\ell}{\ell}\frac{(\log{R})^{k+2\ell}}{(k+2\ell)!}.$$
"We remark that since $`(Q,h)=(Q,h_1\cdots h_k)=1`$, $`\mathcal{H}^{+}`$ is admissible
(for all sufficiently large N) by Lemma 4.1, so we do not have to consider the other case
as in the proof of Lemma 2 in [3]. Combining (4.14) with (4.13) and (4.12) yields the
first case of (2.10). For the case $`Qx+h\in\mathcal{H}`$, we observe that, similarly to
(2.2) of [3], we have"
$$\sum_{N<n\le2N}\vartheta(Qn+h)\Lambda_R(n;\mathcal{H},k+\ell)^{2}=\sum_{N<n\le2N}\vartheta(Qn+h)\Lambda_R(n;\mathcal{H}\setminus\lbrace Qx+h\rbrace,k+\ell)^{2},$$
"so the above evaluation applies with the translation
$`k\mapsto k-1`$, $`\ell\mapsto\ell+1`$ to (4.14)."

[extract note] Two print slips of the source, both verified on the p.11 render and the
p.8 text: the definition of $`F(s_1,s_2;\Omega)`$ prints $`\mu(d_1)\mu(d_1)`$ with
$`d_1`$ twice, and the definition of $`G(s_1,s_2;\Omega^{+})`$ prints
$`1/p^{s_1}+1/p^{s_1}`$ with $`s_1`$ twice. Both are transcribed as printed.

## 6. Section 5, Proof of Proposition 2.3 (pp.11-20)

"5. Proof of Proposition 2.3. 5.1. Auxiliary lemmas. To prove Proposition 2.3, we will
use the following lemmas."

"Lemma 5.1. Fix integers q and a with $`(q,a)=1`$. There is a constant $`c(q,a)>0`$,
depending only on q and a, such that"
$$\prod_{\substack{p\le x\cr p\equiv a\bmod q}}\left(1-\frac{1}{p}\right)\sim\frac{c(q,a)}{(\log{x})^{1/\phi(q)}}$$
"as $`x\to\infty`$."

"Proof. This follows from the prime number theorem for arithmetic progressions. For a
more precise estimate, with the constant $`c(q,a)`$ given explicitly, see [10, Theorem
1]."

"Lemma 5.2. Let $`\mathcal{S}(x)`$ denote the set of positive integers which are
$`\le x`$ and composed only of primes $`p\equiv1\bmod q`$. There is a constant
$`c(q)>0`$, depending only on q, such that"
$$\lvert\mathcal{S}(x)\rvert=\left(c(q)+O\left(\frac{1}{\log{x}}\right)\right)\frac{x}{\log{x}}(\log{x})^{1/\phi(q)}.$$
"Proof. See [9, Lemma 3], in which the constant $`c(q)`$ is given explicitly."

"The next lemma concerns $`\Psi(x,y)`$, the number of positive integers which are
$`\le x`$ and free of prime factors $`>y`$ (y-smooth numbers). The ratio
$`\Psi(x,y)/x`$ depends essentially on $`u=\log{x}/\log{y}`$, and for u in a certain
range is approximated by $`\rho(u)`$, where $`\rho(u)`$ is the Dickman-de Bruijn
rho-function, defined as the continuous solution to" -- display (5.1), p.12:
$$\rho(u):=\begin{cases}1&0\le u\le1,\cr\frac{1}{u}\int_{u-1}^{u}\rho(t)\,dt&u>1.\end{cases}$$

"Lemma 5.3. The estimate" -- display (5.2), p.12:
$$\frac{\Psi(y^{u},y)}{y^{u}}=\rho(u)\left(1+O\left(\frac{\log{(u+2)}}{\log{y}}\right)\right)$$
"holds uniformly in the range" -- display (5.3), p.12:
$$y\ge3,\qquad1\le u\le\exp\left((\log{y})^{3/5-\delta}\right),$$
"where $`\delta`$ is any fixed positive number. The estimate" -- display (5.4), p.12:
$$\rho(u)=\exp\left(-u\log{u}-u\log{}\log{u}+O(u)\right)$$
"holds for $`u>3`$, and" -- display (5.5), p.12:
$$\frac{\Psi(y^{u},y)}{y^{u}}=\exp\left(-u\log{u}-u\log{}\log{u}+O(u)\right)$$
"holds uniformly in the range" -- display (5.6), p.13:
$$3<u\le y^{1-\delta}.$$
"Finally, as $`y\to\infty`$," -- display (5.7), p.13:
$$\frac{\Psi(y,(\log{y})^{A})}{y}=\frac{1}{y^{1/A+o(1)}}$$
"holds for any fixed number $`A>1`$."

"Proof. We refer to the survey article of Granville [7]. The asymptotic (5.2) was shown
to hold for the range (5.3) by Hildebrand [8]: see [7, (1.8), (1.10)]. Hildebrand [8]
also established that the less precise estimate"
$$\frac{\Psi(y^{u},y)}{y^{u}}=\rho(u)\exp\left(O_{\delta}\left(u\exp\left(-(\log{u})^{3/5-\delta}\right)\right)\right)$$
"holds, for any fixed number $`\delta>0`$, in the wider range (5.6). (See displayed
formulas [7, (1.11), (1.13)].) That (5.5) holds in the same range can be deduced from
(5.4). (The estimate (5.5) is less precise, but sufficient for our purposes.) For the
estimate (5.7), see [7, (1.14)]. The value of the Dickman-de Bruijn rho-function is
discussed in [7, 3.7 - 3.9], and (5.4) was proved by de Bruijn in [1]."

"Lemma 5.4. Let $`\mathcal{P}`$ be a subset of the primes. As $`y\to\infty`$, the
estimate" -- display (5.8), p.13:
$$\prod_{\substack{p\le y\cr p\in\mathcal{P}}}\left(1-\frac{1}{p}\right)\sum_{\substack{n>y^{u}\cr p\mid n\Rightarrow p\le y,\ p\in\mathcal{P}}}\frac{1}{n}\le(1+o(1))e^{-\gamma}\int_{u}^{\infty}\rho(v)\,dv.$$
"holds uniformly for u satisfying" -- display (5.9), p.13:
$$u\ge1,\qquad u=\exp\left((\log{y})^{3/5-\delta}\right),$$
"where $`\delta`$ is any fixed positive number."

"Proof. Define"
$$\varrho(x,y;\mathcal{P}):=\prod_{\substack{p\le y\cr p\in\mathcal{P}}}\left(1-\frac{1}{p}\right)\sum_{\substack{n\le x\cr p\mid n\Rightarrow p\le y,\ p\in\mathcal{P}}}\frac{1}{n}.$$
"If $`\ell\le y`$ is prime, then"
$$\varrho(x,y;\mathcal{P})=\prod_{\substack{p\le y\cr p\in\mathcal{P}\cup\lbrace\ell\rbrace}}\left(1-\frac{1}{p}\right)\cdot\left(1-\frac{1}{\ell}\right)^{-1}\sum_{\substack{n\le x\cr p\mid n\Rightarrow p\le y,\ p\in\mathcal{P}}}\frac{1}{n}.$$
"Now"
$$\left(1-\frac{1}{\ell}\right)^{-1}\sum_{\substack{n\le x\cr p\mid n\Rightarrow p\le y,\ p\in\mathcal{P}}}\frac{1}{n}=\left(1+\frac{1}{\ell}+\frac{1}{\ell^{2}}+\cdots\right)\sum_{\substack{n\le x\cr p\mid n\Rightarrow p\le y,\ p\in\mathcal{P}}}\frac{1}{n}\ge\sum_{\substack{m\le x\cr p\mid m\Rightarrow p\le y,\ p\in\mathcal{P}\cup\lbrace\ell\rbrace}}\frac{1}{m},$$
"because every m appearing in the last sum may be written as $`n\ell^{\alpha}`$ for some
$`\alpha\ge0`$ and some n appearing in the second last sum. Hence,"
$$\varrho(x,y;\mathcal{P})\ge\varrho(x,y;\mathcal{P}\cup\lbrace\ell\rbrace),$$
"and applying this inequality repeatedly, we obtain"
$$\varrho(x,y;\mathcal{P})\ge\prod_{p\le y}\left(1-\frac{1}{p}\right)\sum_{\substack{n\le x\cr p\mid n\Rightarrow p\le y}}\frac{1}{n}.$$
"Subtracting both sides from
$`\varrho(\infty,y;\mathcal{P})=1=\varrho(\infty,y;\lbrace p\le y\rbrace)`$, we deduce
that" -- display (5.10), p.14:
$$\prod_{\substack{p\le y\cr p\in\mathcal{P}}}\left(1-\frac{1}{p}\right)\sum_{\substack{n>x\cr p\mid n\Rightarrow p\le y,\ p\in\mathcal{P}}}\frac{1}{n}\le\prod_{p\le y}\left(1-\frac{1}{p}\right)\sum_{\substack{n>x\cr p\mid n\Rightarrow p\le y}}\frac{1}{n}.$$
"By partial summation," -- display (5.11), p.14:
$$\sum_{\substack{n>x\cr p\mid n\Rightarrow p\le y}}\frac{1}{n}=\int_{x}^{\infty}\frac{d\Psi(t,y)}{t}=-\frac{\Psi(x,y)}{x}+\int_{x}^{\infty}\frac{\Psi(t,y)}{t^{2}}\,dt\le\int_{x}^{\infty}\frac{\Psi(t,y)}{t^{2}}\,dt.$$
"Now we assume $`x=y^{u}`$, with u satisfying (5.9) and y tending to infinity. We will
divide the range of the last integral in (5.11) into three parts. First of all, fix any
$`\epsilon\in(0,1)`$ and suppose $`t\ge\exp(y^{\epsilon})`$, that is
$`y\le(\log{t})^{1/\epsilon}`$. By (5.7) we have"
$$\frac{\Psi(t,y)}{t^{2}}\le\frac{\Psi(t,(\log{t})^{1/\epsilon})}{t^{2}}=\frac{1}{t^{1+\epsilon+o(1)}}$$
"as t, and hence as y, tends to infinity. Thus, we may suppose y is large enough so that
$`\Psi(t,y)/t^{2}\le1/t^{1+\epsilon/2}`$, say, and" -- display (5.12), p.14:
$$\int_{\exp(y^{\epsilon})}^{\infty}\frac{\Psi(t,y)}{t^{2}}\,dt\le\int_{\exp(y^{\epsilon})}^{\infty}\frac{dt}{t^{1+\epsilon/2}}=\frac{2}{\epsilon\exp(\epsilon y^{\epsilon}/2)}.$$
"For the range $`x\le t\le\exp(y^{\epsilon})`$, the substitution $`t=y^{v}`$ yields"
-- display (5.13), p.14:
$$\int_{x}^{\exp(y^{\epsilon})}\frac{\Psi(t,y)}{t^{2}}\,dt=\log{y}\int_{u}^{y^{\epsilon}/\log{y}}\frac{\Psi(y^{v},y)}{y^{v}}\,dv.$$
"Next, we let $`u_1=2\exp\left((\log{y})^{3/5-\delta}\right)`$, and for
$`u_1\le v\le y^{\epsilon}`$, we use the estimate (5.5):"
$$\frac{\Psi(y^{v},y)}{y^{v}}=\exp\left(-v\log{v}-v\log{}\log{v}+O(v)\right)\le\frac{1}{v^{v}},$$
"where the last inequality holds for all sufficiently large v, hence for all sufficiently
large y. Thus" -- display (5.14), p.15:
$$\int_{u_1}^{y^{\epsilon}/\log{y}}\frac{\Psi(y^{v},y)}{y^{v}}\,dv\le\int_{u_1}^{\infty}\frac{dv}{v^{v}}\ll\frac{1}{u_1^{u_1}}$$
"for all sufficiently large y. For $`u\le v\le u_1`$, we use the estimate (5.2):"
-- display (5.15), p.15:
$$\int_{u}^{u_1}\frac{\Psi(y^{v},y)}{y^{v}}\,dv=\int_{u}^{u_1}\rho(v)\left(1+O\left(\frac{\log{(v+2)}}{\log{y}}\right)\right)dv=(1+o(1))\int_{u}^{\infty}\rho(v)\,dv-(1+o(1))\int_{u_1}^{\infty}\rho(v)\,dv.$$
"By (5.4) we have, similarly to (5.14), the estimate" -- display (5.16), p.15:
$$\int_{u_1}^{\infty}\rho(v)\,dv\le\int_{u_1}^{\infty}\frac{dv}{v^{v}}\ll\frac{1}{u_1^{u_1}}$$
"for all sufficiently large y. Combining (5.11) - (5.16), we see that"
-- display (5.17), p.15:
$$\int_{x}^{\infty}\frac{\Psi(t,y)}{t^{2}}\,dt=(1+o(1))\log{y}\int_{u}^{\infty}\rho(v)\,dv+O\left(u_1^{-u_1}\log{y}\right)$$
"for all sufficiently large y. Now by definition (5.1),"
$$\int_{u}^{\infty}\rho(v)\,dv\ge\int_{u}^{u+1}\rho(v)\,dv=(u+1)\rho(u+1),$$
"and by (5.4), $`u_1^{-u_1}=o((u+1)\rho(u+1))`$ as $`u_1\ge2u`$, and $`u_1`$ tends to
infinity with y. Therefore, combining (5.17) with (5.11) in fact gives"
-- display (5.18), p.15:
$$\sum_{\substack{n>y^{u}\cr p\mid n\Rightarrow p\le y}}\frac{1}{n}\le(1+o(1))\log{y}\int_{u}^{\infty}\rho(v)\,dv$$
"as $`y\to\infty`$, for u in the range (5.9). Finally, combining (5.18) with (5.10) and
applying Mertens' theorem, we obtain (5.8)."

"5.2. The proof of Proposition 2.3. We are now ready to define Q explicitly. The
construction is modelled on that of Shiu's [9]. For the rest of this section we let
$`q\ge3`$ and a be integers with $`(q,a)=1`$. If $`a\equiv1\bmod q`$, let"
$$\mathcal{P}(H):=\lbrace p\le\log{H}:p\equiv1\bmod q\rbrace\cup\lbrace p\le H/(\log{H})^{2}:p\not\equiv1\bmod q\rbrace,$$
"otherwise let"
$$\mathcal{P}(H):=\lbrace p\le\log{H}:p\equiv1\bmod q\rbrace\cup\lbrace p\le H/(\log{H})^{2}:p\not\equiv1,a\bmod q\rbrace$$
$$\cup\lbrace t(H)\le p\le H/(\log{H})^{2}:p\equiv1\bmod q\rbrace\cup\lbrace p\le H/t(H):p\equiv a\bmod q\rbrace,$$
"with"
$$t(H):=\exp\left(\frac{\log{H}\log{}\log{}\log{H}}{2\log{}\log{H}}\right),$$
"and put" -- display (5.19), p.16:
$$\tilde{Q}(H):=q\prod_{p\in\mathcal{P}(H)}p,\qquad Q=Q(H):=q\prod_{\substack{p\in\mathcal{P}(H)\cr p\ne p_0}}p.$$
"We check that (2.2) - (2.5) are indeed satisfied by Q: only (2.4) is not immediate, but
it follows from the prime number theorem."

"Analogously to (2.12), we define" -- display (5.20), p.16:
$$\tilde{S}(H):=\lbrace h\in(0,H]:(\tilde{Q}(H),h)=1\ \text{and}\ h\equiv a\bmod q\rbrace,$$
$$\tilde{T}(H):=\lbrace h\in(0,H]:(\tilde{Q}(H),h)=1\ \text{and}\ h\not\equiv a\bmod q\rbrace.$$
"Proposition 2.3 will follow from the next lemma."

"Lemma 5.5. Let H be a real parameter tending to infinity, and let $`\tilde{Q}(H)`$ be as
in (5.19). We have" -- display (5.21), p.16:
$$\lvert\tilde{T}(H)\rvert\ll\frac{H}{\log{H}}.$$
"Moreover, there is a constant $`A=A(q)`$, depending on q at most, such that for all
sufficiently large X, there is some H satisfying" -- display (5.22), p.16:
$$\frac{X}{(\log{X})^{A}}\le H\le X,$$
"such that" -- display (5.23), p.16:
$$\lvert\tilde{S}(H)\rvert\gg_q H\frac{\phi(\tilde{Q}(H))}{\tilde{Q}(H)}.$$
"The implied constant in (5.21) is absolute, and that in (5.23) depends on q at most."

"Proof of Proposition 2.3. Let $`S(H)`$ and $`T(H)`$ be as in (2.12). If $`p_0\ne1`$ then
by (2.1) there are at most $`H/p_0<H/\log{H}`$ multiples of $`p_0`$ in $`T(H)`$, so"
$$\lvert T(H)\rvert\ll\frac{H}{\log{H}}$$
"by (5.21). We also have $`\lvert S(H)\rvert\ge\lvert\tilde{S}(H)\rvert`$. An application
of Lemma 5.1 reveals that"
$$\frac{\phi(\tilde{Q}(H))}{\tilde{Q}(H)}=\prod_{p\in\mathcal{P}(H)}\left(1-\frac{1}{p}\right)\gg_q\begin{cases}\frac{1}{\log{H}}\left(\frac{\log{H}}{\log{}\log{H}}\right)^{1/\phi(q)}&\text{if}\ a\equiv1\bmod q,\cr\frac{1}{\log{H}}\left(\frac{\log{t(H)}}{\log{}\log{H}}\right)^{1/\phi(q)}&\text{if}\ a\not\equiv1\bmod q.\end{cases}$$
"Therefore, in either case, combining (5.21) and (5.23) gives"
$$\lvert S(H)\rvert-\lvert T(H)\rvert\gg\lvert\tilde{S}(H)\rvert-\lvert\tilde{T}(H)\rvert\gg_q H\frac{\phi(\tilde{Q}(H))}{\tilde{Q}(H)}\gg H\frac{\phi(Q(H))}{Q(H)}.$$
"Proposition 2.3 now follows from Lemma 5.5."

"Proof of Lemma 5.5. We assume $`a\not\equiv1\bmod q`$ as the case
$`a\equiv1\bmod q`$ is similar and simpler."

"There are $`\ll H/\log{H}`$ primes in $`\tilde{T}(H)`$, so let us count the composites
$`h\in\tilde{T}(H)`$. If $`h=pm`$ for some prime $`p>H/(\log{H})^{2}`$, with $`m>1`$,
then $`m<(\log{H})^{2}`$ is composed only of primes $`>\log{H}`$ and
$`\equiv1\bmod q`$, by the construction of $`\mathcal{P}(H)`$. Thus, m must be prime
itself, and $`p\le H/\log{H}`$. We partition
$`(H/(\log{H})^{2},H/\log{H}]`$ into sub-intervals
$`I_l=(e^{l-1}H/(\log{H})^{2},e^{l}H/(\log{H})^{2}]`$, and
$`(\log{H},(\log{H})^{2}]`$ into sub-intervals
$`J_l=(\log{H},(\log{H})^{2}/e^{l}]`$, $`1\le l\le\log{}\log{H}`$, and using the prime
number theorem, we deduce that the contribution from elements with a large prime factor
is at most"
$$\sum_{1\le l\le\log{}\log{H}}\ \sum_{\substack{p\in I_l\cr p\not\equiv1\bmod q}}\ \sum_{\substack{p'\in J_l\cr p\equiv1\bmod q}}1\ll\sum_{1\le l\le\log{}\log{H}}\frac{e^{l}H}{(\log{H})^{3}}\frac{(\log{H})^{2}}{e^{l}\log{}\log{H}}\ll\frac{H}{\log{H}}.$$
"If $`h=pm`$ with $`p\equiv a\bmod q`$, then $`p>H/t(H)`$, and $`m<t(H)`$ must be
composed only of primes $`\equiv1\bmod q`$, a contradiction as
$`h\not\equiv a\bmod q`$. The only elements left uncounted must be composed only of
primes $`p\equiv1\bmod q`$ with $`\log{H}<p<t(H)`$. By (5.5), the number of such
elements is at most"
$$\Psi(H,t(H))=H\exp\left(-u\log{u}-u\log{}\log{u}+O(u)\right),$$
"where"
$$u=\frac{\log{H}}{\log{t(H)}}=\frac{2\log{}\log{H}}{\log{}\log{}\log{H}}.$$
"Thus"
$$u\log{u}+u\log{}\log{u}+O(u)\sim u\log{u}\sim2\log{}\log{H},$$
"and so"
$$\Psi(H,t(H))\ll\frac{H}{\log{H}}.$$
"Combining these estimates yields (5.21)."

"Now suppose H is in the range (5.22). To bound the size of $`\tilde{S}(H)`$ from below
we will first do the same for"
$$S'(X):=\lbrace h\in(0,X]:(Q'(X),h)=1\ \text{and}\ h\equiv a\bmod q\rbrace,$$
"where"
$$Q'(X):=q\prod_{p\in\mathcal{P}'(X)}p,\qquad\mathcal{P}'(X):=\mathcal{P}(X)\setminus\lbrace p\le\log{X}:p\equiv1\bmod q\rbrace.$$
"Now $`pm\in S'(X)`$ if $`X/t(X)<p\equiv a\bmod q`$ and $`m\in\mathcal{S}(X/p)`$. We
partition $`(X/t(X),X]`$ into sub-intervals
$`I_l=(e^{l-1}X/t(X),e^{l}X/t(X)]`$, $`1\le l\le\log{t(X)}`$, and deduce, using the prime
number theorem for arithmetic progressions and Lemma 5.2, that"
-- display (5.24), p.18:
$$\lvert S'(X)\rvert\ge\sum_{1\le l\le\log{t(X)}}\ \sum_{\substack{p\in I_l\cr p\equiv a\bmod q}}\ \sum_{m\in\mathcal{S}(t(X)/e^{l})}1\gg_q\sum_{1\le l\le\frac{1}{2}\log{t(X)}}\frac{e^{l}X}{t(X)\log{X}}\cdot\frac{t(X)}{e^{l}\log{t(X)}}(\log{t(X)})^{1/\phi(q)}\gg\frac{X}{\log{X}}(\log{t(X)})^{1/\phi(q)}.$$
"Now, we may write any $`h\in S'(X)`$ uniquely as $`h=dm`$, where d is composed only of
primes $`p\le\log{X}`$ with $`p\equiv1\bmod q`$, and $`m\in\tilde{S}(X)`$. Thus, by
(5.24), there is a constant $`c_1(q)>0`$, depending on q at most, such that for all
sufficiently large X," -- display (5.25), p.18:
$$c_1(q)\frac{X}{\log{X}}(\log{t(X)})^{1/\phi(q)}\le\lvert S'(X)\rvert=\sum_{\substack{d\le X\cr p\mid d\Rightarrow p\le\log{X},\ p\equiv1\bmod q}}\ \sum_{\substack{m\le X/d\cr m\in\tilde{S}(X)}}1\le\sum_{\substack{d\le X\cr p\mid d\Rightarrow p\le\log{X},\ p\equiv1\bmod q}}\lvert\tilde{S}(X/d)\rvert.$$
"The inequality on the right is not immediate: in fact if $`Z\le X`$, then
$`\tilde{S}(X)\cap(0,Z]\subseteq\tilde{S}(Z)`$. To see this, first note that as all of
the functions used to define $`\mathcal{P}(X)`$ are monotonically increasing with X,"
$$\mathcal{P}(Z)\subseteq\mathcal{P}(X)\cup\lbrace t(Z)\le p\le t(X):p\equiv1\bmod q\rbrace.$$
"Suppose $`m\in\tilde{S}(X)\cap(0,Z]`$, but $`m\notin\tilde{S}(Z)`$. Then
$`p\in\mathcal{P}(Z)`$ for some $`p\mid m`$, but $`p\notin\mathcal{P}(X)`$, so
$`t(Z)\le p\le t(X)`$ and $`p\equiv1\bmod q`$. Since $`m\equiv a\not\equiv1\bmod q`$,
there must be some $`p'\mid m`$ with $`p'\not\equiv1\bmod q`$ and
$`p'\le m/p\le Z/t(Z)\le X/t(X)`$. Then $`p'\in\mathcal{P}(X)`$, a contradiction."

"Suppose for a contradiction that for some constant $`c_2(q)>0`$, depending on q at most,
we have" -- display (5.26), p.19:
$$\lvert\tilde{S}(H)\rvert\le\frac{c_1(q)}{3c_2(q)}\frac{H}{\log{X}}\left(\frac{\log{t(X)}}{\log{}\log{X}}\right)^{1/\phi(q)}$$
"for all H in the range (5.22). Then" -- display (5.27), p.19:
$$\sum_{\substack{d\le(\log{X})^{A}\cr p\mid d\Rightarrow p\le\log{X},\ p\equiv1\bmod q}}\lvert\tilde{S}(X/d)\rvert\le\frac{c_1(q)}{3c_2(q)}\frac{X}{\log{X}}\left(\frac{\log{t(X)}}{\log{}\log{X}}\right)^{1/\phi(q)}\sum_{\substack{d\le(\log{X})^{A}\cr p\mid d\Rightarrow p\le\log{X},\ p\equiv1\bmod q}}\frac{1}{d}$$
$$\le\frac{c_1(q)}{3c_2(q)}\frac{X}{\log{X}}\left(\frac{\log{t(X)}}{\log{}\log{X}}\right)^{1/\phi(q)}\prod_{\substack{p\le\log{X}\cr p\equiv1\bmod q}}\left(1-\frac{1}{p}\right)^{-1}\le\frac{c_1(q)}{3}\frac{X}{\log{X}}(\log{t(X)})^{1/\phi(q)},$$
"provided X is sufficiently large, and for a suitable choice of $`c_2(q)`$ (given by
Lemma 5.1)."

"Now, by the fundamental lemma of Brun's sieve, we have" -- display (5.28), p.19:
$$\lvert\tilde{S}(X/d)\rvert\ll\frac{X}{d}\prod_{p\in\mathcal{P}(X/d)}\left(1-\frac{1}{p}\right)$$
"for any d. If $`(\log{X})^{A}<d\le\sqrt{X}`$, then
$`\log{(X/d)}\asymp\log{X}`$, and applying Lemma 5.1 to the sieve upper bound (5.28), we
see that" -- display (5.29), p.19:
$$\sum_{\substack{(\log{X})^{A}<d\le\sqrt{X}\cr p\mid d\Rightarrow p\le\log{X},\ p\equiv1\bmod q}}\lvert\tilde{S}(X/d)\rvert\le c_3(q)\frac{X}{\log{X}}\left(\frac{\log{t(X)}}{\log{}\log{X}}\right)^{1/\phi(q)}\sum_{\substack{(\log{X})^{A}<d\le\sqrt{X}\cr p\mid d\Rightarrow p\le\log{X},\ p\equiv1\bmod q}}\frac{1}{d}$$
"for some constant $`c_3(q)>0`$. By lemmas 5.4 and 5.1 respectively, we have"
-- display (5.30), p.19:
$$\sum_{\substack{(\log{X})^{A}<d\le\sqrt{X}\cr p\mid d\Rightarrow p\le\log{X},\ p\equiv1\bmod q}}\frac{1}{d}\le\prod_{\substack{p\le\log{X}\cr p\equiv1\bmod q}}\left(1-\frac{1}{p}\right)^{-1}(1+o(1))e^{-\gamma}\int_{A}^{\infty}\rho(v)\,dv\le c_4(q)(\log{}\log{X})^{1/\phi(q)}\int_{A}^{\infty}\rho(v)\,dv$$
"for some constant $`c_4(q)>0`$. Now by (5.4),"
$$\int_{A}^{\infty}\rho(v)\,dv\to0\ \text{as}\ A\to\infty,$$
"so we may choose $`A=A(c_1(q),c_3(q),c_4(q))=A(q)`$ so that"
$$\int_{A}^{\infty}\rho(v)\,dv\le\frac{c_1(q)}{4c_3(q)c_4(q)}.$$
"For any such A, combining (5.29) and (5.30) yields" -- display (5.31), p.20:
$$\sum_{\substack{(\log{X})^{A}<d\le\sqrt{X}\cr p\mid d\Rightarrow p\le\log{X},\ p\equiv1\bmod q}}\lvert\tilde{S}(X/d)\rvert\le\frac{c_1(q)}{4}\frac{X}{\log{X}}(\log{t(X)})^{1/\phi(q)}.$$
"Finally, using Rankin's trick, we see that" -- display (5.32), p.20:
$$\sum_{\substack{\sqrt{X}<d\le X\cr p\mid d\Rightarrow p\le\log{X},\ p\equiv1\bmod q}}\lvert\tilde{S}(X/d)\rvert\le\sum_{\substack{\sqrt{X}<d\le X\cr p\mid d\Rightarrow p\le\log{X}}}\frac{X}{d}\left(\frac{d}{\sqrt{X}}\right)^{1/3}\le X^{5/6}\prod_{p\le\log{X}}\left(1-\frac{1}{p^{2/3}}\right)^{-1}$$
$$\le X^{5/6}\exp\left(\sum_{p\le\log{X}}\frac{3}{p^{2/3}}\right)\le X^{5/6}\exp\left(9(\log{X})^{1/3}\right)=X^{5/6+o(1)}$$
"by the prime number theorem."

"Combining (5.25), (5.27), (5.31), and (5.32), we obtain
$`c_1(q)\le2c_1(q)/3`$, which is absurd. We conclude that for all sufficiently large X,
there is some H in the range (5.22) for which"
$$\lvert\tilde{S}(H)\rvert\gg_q\frac{H}{\log{X}}\left(\frac{\log{t(X)}}{\log{}\log{X}}\right)^{1/\phi(q)}\gg\frac{H}{\log{H}}\left(\frac{\log{t(H)}}{\log{}\log{H}}\right)^{1/\phi(q)}.$$
"A final application of Lemma 5.1 shows that this is
$`\gg_q H\phi(\tilde{Q}(H))/\tilde{Q}(H)`$."

## 7. Section 6, A lower bound (pp.20-22)

"6. A lower bound. In this section we will show how to obtain a quantitative version of
Theorem 1.1. We will use the assumptions and notation of sections 3 - 5, and show that"
-- display (6.1), p.20:
$$\lvert\lbrace p_{r+1}\le Y:p_{r+1}\equiv p_r\equiv a\bmod q\ \text{and}\ p_{r+1}-p_r<\epsilon\log{p_r}\rbrace\rvert\ge Y^{1/3(\log{}\log{Y})^{A}}$$
"for all sufficiently large Y. Here $`A=A(q)`$ is the constant given in Lemma 5.5. This
lower bound could be improved by a sharpening of the range (5.22) for H."

"We will first prove that the estimate" -- display (6.2), p.20:
$$\sum_{N<n\le2N}\Lambda(n;\mathcal{H},k+\ell)^{4}\ll N(\log{N})^{19k+4\ell}$$
"holds, with an absolute implied constant. For by (4.1) and (4.2),"
-- display (6.3), p.21:
$$\sum_{N<n\le2N}\Lambda(n;\mathcal{H},k+\ell)^{4}={\sum_{d_1,\ldots,d_4}}'\lambda_{d_1}\cdots\lambda_{d_4}\sum_{\substack{N<n\le2N\cr[d_1,\ldots,d_4]\mid P(n;\mathcal{H})}}1$$
$$={\sum_{d_1,\ldots,d_4}}'\lambda_{d_1}\cdots\lambda_{d_4}\sum_{\substack{m\bmod[d_1,\ldots,d_4]\cr\in\Omega([d_1,\ldots,d_4])}}\ \sum_{\substack{N<n\le2N\cr n\equiv m\bmod[d_1,\ldots,d_4]}}1$$
$$\le\sum_{\substack{d_1,\ldots,d_4\cr\text{squarefree}}}\lvert\lambda_{d_1}\cdots\lambda_{d_4}\rvert\sum_{\substack{m\bmod[d_1,\ldots,d_4]\cr\in\Omega([d_1,\ldots,d_4])}}\left(\frac{N}{[d_1,\ldots,d_4]}+O(1)\right)\ll N(\log{R})^{4(k+\ell)}\sum_{\substack{d_1,\ldots,d_4\le R\cr\text{squarefree}}}\frac{\lvert\Omega([d_1,\ldots,d_4])\rvert}{[d_1,\ldots,d_4]}.$$
"To see the last inequality, note that
$`[d_1,\ldots,d_4]\le R^{4}=N^{1-4\epsilon'}=o(N)`$, and so
$`N/[d_1,\ldots,d_4]+O(1)\ll N/[d_1,\ldots,d_4]`$."

"As observed in Section 4, $`\lvert\Omega(d)\rvert\le k^{\omega(d)}`$ for squarefree d,
so" -- display (6.4), p.21:
$$\sum_{\substack{d_1,\ldots,d_4\le R\cr\text{squarefree}}}\frac{\lvert\Omega([d_1,\ldots,d_4])\rvert}{[d_1,\ldots,d_4]}\le\sum_{D\le R^{4}}\frac{\mu^{2}(D)k^{\omega(D)}}{D}\sum_{\substack{d_1,\ldots,d_4\cr[d_1,\ldots,d_4]=D}}1=\sum_{D\le R^{4}}\frac{\mu^{2}(D)(15k)^{\omega(D)}}{D}\le\prod_{p\le R^{4}}\left(1+\frac{15k}{p}\right)\ll(\log{R^{4}})^{15k}.$$
"Since $`R^{4}<N`$, combining (6.3) and (6.4) yields (6.2)."

"Now choose N so that (3.2) holds. If we restrict the outer sum in the definition of
$`\mathcal{L}`$ to those n for which $`(Qn,Qn+H]`$ contains a prime string
$`p_{r+1}\equiv p_r\equiv a\bmod q`$, we remove no positive terms. Thus, if
$`{\sum}^{*}`$ denotes this restricted sum, then" -- display (6.5), p.21:
$$\mathcal{L}\le\frac{1}{N}\left(\frac{\phi(Q)}{Q}\right)^{k}{\sum_{N<n\le2N}^{*}}\left(\sum_{h\in S}\vartheta(Qn+h)-\sum_{h\in T}\vartheta(Qn+h)-\log{3QN}\right)\Lambda_R(n;\mathcal{H},k+\ell)^{2}.$$
"For each $`n\in(N,2N]`$," -- display (6.6), p.21:
$$\sum_{h\in S}\vartheta(Qn+h)-\sum_{h\in T}\vartheta(Qn+h)-\log{3QN}\le H\log{3QN},$$
"and by the Cauchy-Schwartz inequality," -- display (6.7), p.22:
$${\sum_{N<n\le2N}^{*}}\Lambda_R(n;\mathcal{H},k+\ell)^{2}\le\left({\sum_{N<n\le2N}^{*}}1\right)^{1/2}\left(\sum_{N<n\le2N}\Lambda_R(n;\mathcal{H},k+\ell)^{4}\right)^{1/2}.$$
"Combining (6.5) - (6.7) yields"
$${\sum_{N<n\le2N}^{*}}1\ge N^{2}(Q/\phi(Q))^{2k}\mathcal{L}^{2}(H\log{3QN})^{-2}\left(\sum_{N<n\le2N}\Lambda_R(n;\mathcal{H},k+\ell)^{4}\right)^{-1}.$$
"Using $`H=\epsilon\log{N}`$, $`\log{3QN}=(1+o(1))\log{N}`$, and
$`Q/\phi(Q)\ge1`$, then applying (3.2) and (6.2), we see that the right-hand side is
$`\gg_{k,q}N/(\log{N})^{17k+2}`$. Since k depends on $`\epsilon`$, we may write"
-- display (6.8), p.22:
$${\sum_{N<n\le2N}^{*}}1\gg_{\epsilon,q}\frac{N}{(\log{N})^{B(\epsilon)}},$$
"where $`B(\epsilon)`$ is a constant depending on $`\epsilon`$."

"Now fix a large number Y, and let"
$$X:=\epsilon\left(1+\frac{2c\epsilon}{(\log{}\log{Y})^{2}}\right)^{-1}\log{Y},$$
"with $`c>0`$ fixed. By Lemma 5.5, we may choose H in the range"
$$X/(\log{X})^{A}\le H\le X$$
"so that (3.2), hence (6.1), holds with $`N=\exp(H/\epsilon)`$. By (2.4),"
$$3Q(H)N\le\exp\left(\frac{H}{\epsilon}+\frac{cH}{(\log{H})^{2}}\right)\le Y,$$
"because"
$$\frac{H}{\epsilon}+\frac{cH}{(\log{H})^{2}}=\frac{H}{\epsilon}\left(1+\frac{c\epsilon}{(\log{H})^{2}}\right)\le\frac{X}{\epsilon}\left(1+\frac{2c\epsilon}{(\log{}\log{Y})^{2}}\right)=\log{Y}.$$
"Here we have used $`\log{H}=(1+o(1))\log{X}=(1+o(1))\log{}\log{Y}`$. Also,"
$$\log{N}=H/\epsilon\ge X/\epsilon(\log{X})^{A}\ge\log{Y}/2(\log{}\log{Y})^{A}.$$
"Therefore, using (6.8) as a lower bound for the number of prime strings up to Y, we
deduce (6.1). (At best, we may have $`H=X`$, in which case we could deduce a lower bound
of $`Y^{1-c'/(\log{}\log{Y})^{2}}`$, for some constant $`c'>0`$.)"

[extract note] The source prints the fourth-moment sums of Section 6 as
$`\Lambda(n;\mathcal{H},k+\ell)`$ without the subscript R in (6.2) and (6.3), while the
same object is printed $`\Lambda_R`$ in (6.7) and everywhere in Sections 2-4; and the
lead-in to (6.7) prints "Cauchy-Schwartz". Both are transcribed as printed.

## 8. Section 7, Concluding remarks, and Section 8 (p.23, verbatim)

"7. Concluding remarks. Proposition 2.2 is similar to a special case of Propositions 1
and 2 of [5], which are used to prove that"
$$\liminf_{r\to\infty}\frac{p'_{r+\nu}-p'_{r}}{\phi(q)\log{p'_{r}}}\le e^{-\gamma}(\sqrt{\nu}-1)^{2},$$
"where $`p'_j`$ denotes the jth smallest prime in the arithmetic progression
$`a\bmod q`$, $`(q,a)=1`$. By considering
$`H_{\nu}=(\nu-1+\epsilon)\log{N}`$ instead of H, $`Q=Q(H_{\nu})`$ instead of
$`Q(H)`$, and"
$$\mathcal{L}_{\nu}:=\frac{1}{N}\left(\frac{\phi(Q)}{Q}\right)^{k}\sum_{N<n\le2N}\left(\sum_{h\in S}\vartheta(Qn+h)-\nu\sum_{h\in T}\vartheta(Qn+h)-\nu\log{3QN}\right)\Lambda_R(n;\mathcal{H},k+\ell)^{2}$$
"instead of $`\mathcal{L}`$, it is possible to prove that the interval
$`(Qn,Qn+H_{\nu}]`$ contains a string of $`\nu+1`$ consecutive primes
$`\equiv a\bmod q`$, for some $`n\in(N,2N]`$ and a sequence $`N\to\infty`$. It may be
feasible to prove a similar result with
$`H_{\nu}=(e^{-\gamma}(\sqrt{\nu}-1)^{2}+\epsilon)\log{N}`$."

"8. Acknowledgements. I would like to thank Andrew Granville, without whose help and
encouragement this work would not have materialized. For many productive discussions, my
thanks also to Jorge Jimenez Urroz, and my colleagues Farzad Aryan, Mohammad Bardestani,
Daniel Fiorilli and Kevin Henriot."

## 9. References as printed (pp.23-24, verbatim)

"[1] N. G. de Bruijn, 'The asymptotic behaviour of a function occurring in the theory of
primes', J. Indian Math. Soc. (N.S.) 15 (1951), 25-32. MR0043838 (13:326f) [2] H.
Davenport, Multiplicative number theory, 3rd edn (Revised and with a preface by H. L.
Montgomery; Springer-Verlag, New York, 2000). MR1790423 (2001f:11001) [3] D. A.
Goldston, Y. Motohashi, J. Pintz, and C. Y. Yildirim, 'Small gaps between primes exist',
Proc. Japan Acad. Ser. A Math. Sci. 82 (2006), 61-65. MR2222213 (2007a:11135) [4] D. A.
Goldston, J. Pintz, and C. Y. Yildirim, 'Primes in tuples I', Preprint, 2005,
http://arxiv.org/abs/math/0508185v1. [5] D. A. Goldston, J. Pintz, and C. Y. Yildirim,
'Primes in tuples III. On the difference $`p_{n+\nu}-p_n`$', Funct. Approx. Comment.
Math. 35 (2006), 79-89. MR2271608 (2008f:11102) [6] D. A. Goldston, J. Pintz, and C. Y.
Yildirim, 'Primes in tuples I', Ann. of Math. (2) 170 (2009), 819-862. MR2552109 [7] A.
Granville, 'Smooth numbers: computational number theory and beyond', Algorithmic number
theory: lattices, number fields, curves and cryptography (eds J. P. Buhler and P.
Stevenhagen), Mathematical Sciences Research Institute Publications 44 (Cambridge
University Press, Cambridge, 2008), 267-323. MR2467549 [8] A. Hildebrand, 'On the number
of positive integers $`\le x`$ and free of prime factors $`>y`$', J. Number Theory 22
(1986), 289-307. MR831874 (87d:11066) [9] D. K. L. Shiu, 'Strings of congruent primes',
J. London Math. Soc. (2) 61 (2000), 359-373. MR1760689 (2001f:11155) [10] K. S.
Williams, 'Mertens' theorem for arithmetic progressions', J. Number Theory 6 (1974),
353-359. MR0364137 (51:392)"

"Departement de mathematiques et de statistique / Universite de Montreal / CP 6128, succ.
Centre-ville / Montreal, Quebec H3C 3J7 / Canada"; "E-mail address:
freiberg@dms.umontreal.ca"

## 10. Uniformity ledger

- [extract note] $`\epsilon>0`$ is fixed once at the start of Section 2 and H tends
  monotonically to infinity with $`N=\exp(H/\epsilon)`$ (p.2); k and $`\ell`$ are fixed
  positive integers in Proposition 2.2 and are chosen in Section 3 as
  $`\ell=[\sqrt{k}]`$ with k sufficiently large (p.5).
- [extract note] Proposition 2.2 requires $`(Q,h_1,\ldots,h_k)=1`$, $`(Q,h)=1`$, and
  $`R=N^{1/4-\epsilon'}`$ with $`\epsilon'\in(0,1/4)`$ (p.3); the estimates are stated as
  $`H\to\infty`$ asymptotics, not as bounds valid for each H.
- [extract note] Proposition 2.3 does NOT give its conclusion for all large H: it gives
  an infinite sequence $`H_1<H_2<\ldots`$ along which a suitable Q exists (p.3), and its
  implied constant depends at most on q. Lemma 5.5 likewise supplies, for each
  sufficiently large X, some H in the range (5.22) (p.16).
- [extract note] The constant $`c(q)`$ of (3.1) and the constant $`A=A(q)`$ of Lemma 5.5
  depend on q at most (pp.4, 16); $`B(\epsilon)`$ in (6.8) depends on $`\epsilon`$
  (p.22).
- [extract note] Lemma 4.1's asymptotic (4.4) holds for $`k`$ fixed and
  $`(Q,h_1\cdots h_k)=1`$, with admissibility asserted for $`k\le\log{H}`$ (p.6).
- [extract note] Lemma 5.3's ranges are (5.3) for (5.2) and (5.6) for (5.5); Lemma 5.4's
  range is (5.9), and $`\delta`$ is any fixed positive number in both (pp.12-13).
- [extract note] The implied constant in (5.21) is stated absolute and that in (5.23)
  q-dependent (p.16); the implied constant in (6.2) is stated absolute (p.20).

## 11. Structural map

[extract note] 1. Theorem 1.1 (p.1) is proved in Section 3 (pp.4-5) from Proposition 2.2
and Proposition 2.3 via (3.1), the pigeonhole step, and (3.2).
[extract note] 2. Lemma 2.1 (p.2) is quoted from [2, Chapter 14] and is used to define
$`q_0`$, $`p_0`$ and (2.1); (2.1) is then invoked in Section 4 twice, at
$`G(0,0;\Omega)`$ and $`G(0,0;\Omega^{+})`$ (pp.8, 11), and in the proof of Proposition
2.3 (p.17).
[extract note] 3. Proposition 2.2 (p.3) is proved in Section 4 (pp.6-11): (2.9) via
Lemma 4.1 and the proof of Lemma 1 of [3]; (2.10) via Lemma 4.2, (4.10), (4.13), (4.14)
and the proof of Lemma 2 of [3].
[extract note] 4. Lemma 4.1 (p.6) is proved on pp.6-8 from (2.2), (2.3), (4.5), (4.6)
and the prime number theorem. Lemma 4.2 (p.8) is quoted as Lemma 2 of [5]; no argument
is printed.
[extract note] 5. Proposition 2.3 (p.3) is proved on p.17 from Lemma 5.5 and Lemma 5.1,
together with (5.21) and (5.23).
[extract note] 6. Lemma 5.5 (p.16) is proved on pp.17-20: (5.21) from the construction
of $`\mathcal{P}(H)`$, the prime number theorem and (5.5); the second assertion by
contradiction from (5.25), (5.27), (5.31) and (5.32), which invoke Lemma 5.2 (via
(5.24)), Lemma 5.1, Brun's sieve (5.28), Lemma 5.4 (via (5.30)) and Rankin's trick.
[extract note] 7. Lemma 5.1 (p.12) is attributed to the prime number theorem for
arithmetic progressions with [10, Theorem 1] for the explicit constant; Lemma 5.2 (p.12)
is attributed to [9, Lemma 3]; Lemma 5.3 (p.12) to [7] and [8]; neither carries a printed
argument. Lemma 5.4 (p.13) is proved on pp.13-15 from (5.10) - (5.18).
[extract note] 8. Section 6 (pp.20-22) derives (6.1) from (3.2) and (6.2), where (6.2)
follows from (6.3) and (6.4), and the passage from (6.5) - (6.7) to (6.8) uses
Cauchy-Schwarz; the choice of X and H at the end of the section converts (6.8) into
(6.1).
[extract note] 9. Section 7 (p.23) states, without printed proof, that replacing H by
$`H_{\nu}=(\nu-1+\epsilon)\log{N}`$ and $`\mathcal{L}`$ by $`\mathcal{L}_{\nu}`$ makes
it possible to prove that $`(Qn,Qn+H_{\nu}]`$ contains $`\nu+1`$ consecutive primes
$`\equiv a\bmod q`$, and records the $`e^{-\gamma}(\sqrt{\nu}-1)^{2}`$ target as a
feasibility remark.

## FLAGS

- sha256 of the local file matches the anchor line above, verified before the source was
  opened. TRANSCRIPTION-UNSURE passages: 0.
- V8 (this source): 24 PDF pages against a steering expectation of about 23-24; printed
  pagination 1-24 coincides with the PDF pages.
- Divergence from the dispatch's Section 4.4 attention list: it named "Section 2 whole --
  Lemma 2.1 (Landau-Page) through (2.12), Propositions 2.2 and 2.3", "displays
  (3.1)-(3.2)", "displays (4.1)-(4.14)", "Lemmas 5.1-5.5 and the construction displays
  (5.19)-(5.23)", and "displays (6.1)-(6.8)". All of those are present and transcribed.
  In addition the source numbers (5.1)-(5.18) and (5.24)-(5.32), which the list did not
  name; they are transcribed above under the object-coverage rule.
- Divergence, same list: it gave the pigeonhole passage as "|A_n| >= |B_n| + 2, and so,
  by the pigeonhole principle, A_n contains a pair of consecutive primes". The printed
  sentence, transcribed in Section 4 above and verified on the p.5 render, continues
  "$`p_r,p_{r+1}`$. These primes satisfy
  $`p_{r+1}-p_r<H<\epsilon\log{QN}<\epsilon\log{p_r}`$."
- Divergence, same list: it named "Lemma 4.1 and its singular series display". The
  singular series display is printed on p.6 immediately before Lemma 4.1, not inside it;
  Lemma 4.1's own displays are (4.3) and (4.4).
- Source print slips, recorded and not repaired in the quotations: $`\mu(d_1)\mu(d_1)`$
  in the definition of $`F(s_1,s_2;\Omega)`$ (p.8); $`1/p^{s_1}+1/p^{s_1}`$ in the
  definition of $`G(s_1,s_2;\Omega^{+})`$ (p.11); $`\Lambda`$ without the subscript R in
  (6.2) and (6.3) (pp.20-21); "Cauchy-Schwartz" at (6.7) (p.22); the summation condition
  $`d\cdots d_{\kappa}\le R^{2}`$ printed with no subscript on the first factor (p.10);
  the congruence condition of the third sum in the proof of Lemma 5.5 printed
  $`p\equiv1\bmod q`$, with no prime on the variable (p.17).
- The set of linear forms, the prime set of Section 5 and the singular series are printed
  in three different alphabets; the transcription convention for each is stated in
  Section 0.
