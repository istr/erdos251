# EXTRACTION: Tristan Freiberg, "Strings of congruent primes in short intervals II"

Source (only evidence base): /home/istr/pro/erdos251/dossier/1110.6624v1.pdf
sha256 407336f47e7812aa7fa7319d4bda20e9feeb9ac40cc3a4c41c699b6ed2e5e997
Anchor line (payloads/HASHES.txt): https://arxiv.org/pdf/1110.6624v1
Bibliographic identity: arXiv:1110.6624v1 [math.NT] 30 Oct 2011
Extraction method: text-layer with render verification
Declared scope: PARTIAL: Sections 1-3 in full (Theorem 1.1, the Discussion, the construction (3.1)-(3.6), Lemmas 3.2-3.4 as statements with the proof of Lemma 3.4); Section 4's Selberg-Delange proof by named reference only, not transcribed

---

## 0. Transcription conventions

[extract note] ASCII-folded per AGENTS.md; displays are transcribed as printed inside
`$$` blocks, inline mathematics uses the repository inline delimiter, and page citations
are the printed page numbers, which coincide with the PDF pages 1-30.
[extract note] The anchored PDF carries a clean LaTeX-derived text layer. Transcription
was made from that layer and every quoted passage was verified against 200-dpi page
rasters of the page cited.
[extract note] The source prints the prime set of Section 3 in a calligraphic face,
transcribed here as $`\mathcal{P}(H)`$.
[extract note] The source prints a section sign before section numbers in
cross-references such as "[2, 6.2]" and "See 4". The sign is dropped in the ASCII
transcription below and the bare number retained, so "[2, 6.2]" reads as a reference to
section 6.2 of [2] and "See 4" as a reference to this paper's Section 4.
[extract note] The declared scope covers pp.1-13 up to the end of Section 3. The scope
boundary and what lies outside it are stated in Section 7 below.

---

## 1. Front matter (p.1, verbatim)

"STRINGS OF CONGRUENT PRIMES IN SHORT INTERVALS II"; "TRISTAN FREIBERG";
"arXiv:1110.6624v1 [math.NT] 30 Oct 2011"; "The author is supported by the Goran
Gustafsson Foundation (KVA)."

"ABSTRACT. Let $`p_1=2,p_2=3,\ldots`$ be the sequence of all primes. Let $`\epsilon`$ be
an arbitrarily small but fixed positive number, and fix a coprime pair of integers
$`q\ge3`$ and a. We will establish a lower bound for the number of primes $`p_r`$, up to
X, such that both $`p_{r+1}-p_r<\epsilon\log{p_r}`$ and
$`p_r\equiv p_{r+1}\equiv a\bmod q`$ simultaneously hold. As a lower bound for the number
of primes satisfying the latter condition, the bound we obtain improves upon a bound
obtained by D. Shiu."

## 2. Section 1, Introduction (pp.1-2, verbatim)

"1. INTRODUCTION. Let $`p_1=2,p_2=3,\ldots`$ be the sequence of all primes, and let
$`\epsilon`$ be an arbitrarily small but fixed positive number. In 2005 [3, 5],
Goldston, Pintz, and Yildirim made a significant breakthrough by proving that
$`p_{r+1}-p_r<\epsilon\log{p_r}`$ for infinitely many pairs $`p_r,p_{r+1}`$ of primes.
That is, for infinitely many r, the rth prime gap, $`p_{r+1}-p_r`$, is arbitrarily small
compared to the 'expected' gap of $`\log{p_r}`$. In 2006 [4] they extended their method
to prove an analogous result for primes in arithmetic progressions. Thus, given a
coprime pair of integers $`q\ge3`$ and a, if $`p'_1<p'_2<\cdots`$ is the sequence of all
primes congruent to $`a\bmod q`$, then for infinitely many pairs $`p'_m,p'_{m+1}`$, we
have $`p'_{m+1}-p'_m<\epsilon\log{p_m}`$."

"Given any such pair $`p'_m,p'_{m+1}`$, there may or may not be a third prime p, not
congruent to $`a\bmod q`$, such that $`p'_m<p<p'_{m+1}`$. Thus, either there are
infinitely many triples of primes $`p_r,p_{r+1},p_{r+2}`$, not necessarily in the same
arithmetic progression mod q, such that $`p_{r+2}-p_r<\epsilon\log{p_r}`$; or there are
infinitely many pairs of consecutive primes $`p_r,p_{r+1}`$ such that both
$`p_{r+1}-p_r<\epsilon\log{p_r}`$ and $`p_r\equiv p_{r+1}\equiv a\bmod q`$ simultaneously
hold. Presumably both statements are true, but one can only deduce that one of them is
true, and one does not know which one, from the result in [4]."

"Although we would like to prove the first statement, unfortunately it seems beyond reach
of the method of Goldston, Pintz, and Yildirim, at least at present. (See [5, 1, Question
3].) It is natural, then, to ask whether one can at least prove the second statement. In
so doing, one would establish a conjecture of Chowla that there are infinitely many pairs
of consecutive primes $`p_r,p_{r+1}`$ such that $`p_r\equiv p_{r+1}\equiv a\bmod q`$.
This conjecture was in fact already proved by D. Shiu in 2000 [10]."

"As it turns out, the ideas of Shiu can be combined with those of Goldston, Pintz, and
Yildirim to prove that there are indeed infinitely many pairs of consecutive primes
$`p_r,p_{r+1}`$ such that both $`p_{r+1}-p_r<\epsilon\log{p_r}`$ and
$`p_r\equiv p_{r+1}\equiv a\bmod q`$ simultaneously hold. We did this in [2], where we
also obtained a very weak quantitative result [2, 7]: there is a positive constant
$`A=A(q)`$, depending only on q, such that for all sufficiently large X,"
-- display (1.1), p.2:
$$\sum_{\substack{p_r\le X\cr p_{r+1}-p_r<\epsilon\log{p_r}\cr p_r\equiv p_{r+1}\equiv a\bmod q}}1\ge X^{1/3(\log{}\log{X})^{A}}.$$
"Our purpose here is to improve this lower bound to the following:"

"Theorem 1.1. Let $`p_1=2,p_2=3,\ldots`$ be the sequence of all primes. Fix any positive
number $`\epsilon`$, and fix a pair of coprime integers $`q\ge3`$ and a. There is an
absolute positive constant c such that, for all sufficiently large X,"
-- display (1.2), p.2:
$$\sum_{\substack{p_r\le X\cr p_{r+1}-p_r<\epsilon\log{p_r}\cr p_r\equiv p_{r+1}\equiv a\bmod q}}1\ge X^{1-c/\log{}\log{X}}.$$

"As a lower bound for the number of primes $`p_r`$ up to X for which
$`p_r\equiv p_{r+1}\equiv a\bmod q`$, (1.2) is, once X is sufficiently large, greater
than that obtained by Shiu [10, Theorem 2], namely $`X^{1-\varepsilon(X)}`$, where"
$$\varepsilon(X)=C_1(q)\left(\frac{\log{}\log{}\log{X}}{\log{}\log{X}}\right)^{1/\phi(q)}$$
"if $`a\equiv\pm1\bmod q`$, and"
$$\varepsilon(X)=C_2(q)\left(\frac{(\log{}\log{}\log{X})^{2}}{(\log{}\log{X})(\log{}\log{}\log{}\log{X})}\right)^{1/\phi(q)}$$
"otherwise. (Here, $`C_1(q)`$ and $`C_2(q)`$ are constants depending only on q.)"

## 3. Section 2, Discussion (pp.2-4, verbatim)

"2. Discussion. The way to incorporate the ideas of Shiu into the work of Goldston,
Pintz, and Yildirim is explained in [2, 2]. Basically, Goldston, Pintz, and Yildirim [4]
proved that for all sufficiently large N, there is at least one integer $`n\in(N,2N]`$
such that there are at least two primes of the form $`Qn+h`$, where: Q is a multiple of q
such that $`\log{QN}\sim\log{N}`$; h is in the set"
$$S=S(H):=\lbrace1\le h\le H:(Q,h)=1\ \text{and}\ h\equiv a\bmod q\rbrace;$$
"and $`H=\epsilon\log{N}`$. Goldston, Pintz, and Yildirim [4, (2.1) - (2.4)] took"
$$Q=Q(H):=q\prod_{p\in\mathcal{P}}p,$$
"where"
$$\mathcal{P}=\mathcal{P}(H):=\lbrace p\le H/(\log{H})^{2}\rbrace,$$
"but if we remove from $`\mathcal{P}`$ any subset of the primes in the interval
$`(\log{H},H/(\log{H})^{2}]`$, the key estimates [2, Proposition 3.2] still hold, with
one exception -- namely, we do not necessarily have [2, (2.2)]:
$`\lvert S\rvert\gg_q H\phi(Q)/Q`$."

"Our goal is to remove primes from $`\mathcal{P}`$ in such a way that we have the
following for the resulting Q: almost all of the integers $`h\in[1,H]`$ that are coprime
with Q are congruent to $`a\bmod q`$, in the sense that if"
$$T=T(H):=\lbrace1\le h\le H:(Q,h)=1\ \text{and}\ h\not\equiv a\bmod q\rbrace,$$
"then $`\lvert T\rvert=o(\lvert S\rvert)`$ as $`H\to\infty`$; and
$`\lvert S\rvert\gg_q H\phi(Q)/Q`$ for all sufficiently large H. Since $`Qn+h`$ is prime
only if $`(Q,h)=1`$, we could deduce from this that, for infinitely many of those n for
which $`(Qn,Qn+H]`$ contains at least two primes congruent to $`a\bmod q`$, among those
primes is a pair of consecutive primes. Indeed, we would be able to establish (1.2). (See
[2, 4, 7] for details.)"

"Based on a construction used by Shiu in [10], we defined such a set $`\mathcal{P}`$ in
[2, 6.2] (also see (3.1) - (3.4) below). In fact, denoting by
$`\mathcal{P}'=\mathcal{P}'(H)`$ the set considered by Shiu, we have
$`\mathcal{P}=\mathcal{P}'\cup\lbrace p\le\log{H}:p\equiv1\bmod q\rbrace`$. Since
$`\mathcal{P}'`$ is defined in such a way that it consists only of primes up to
$`H/(\log{H})^{2}`$, and contains all primes $`p\not\equiv1\bmod q`$ up to
$`\log{H}`$, $`\mathcal{P}`$ consists only of primes up to $`H/(\log{H})^{2}`$ and, in
particular, all primes up to $`\log{H}`$."

"However, in [2], we were only able to establish the following:
$`\lvert T\rvert\ll H/\log{H}`$ for all sufficiently large H;
$`H/\log{H}=o(H\phi(Q)/Q)`$; and there is a positive constant A, depending only on q,
such that for all sufficiently large Y, there is some
$`H\in[Y/(\log{Y})^{A},Y]`$ for which $`\lvert S\rvert\gg_q H\phi(Q)/Q`$. From this we
deduced (1.1) in [2, 7]."

"The reason we were not able to establish that $`\lvert S\rvert\gg_q H\phi(Q)/Q`$ for all
sufficiently large H in [2] is that we used [10, Lemma 2] (Lemma 6.2 in [2]): an
asymptotic for the number of integers up to H that are composed only of primes congruent
to 1 mod q. Defining $`Q'=Q'(H)`$ and $`S'=S'(H)`$ analogously to Q and S, but with
$`\mathcal{P}'`$ in place of $`\mathcal{P}`$, Shiu used this asymptotic to show that
$`\lvert S'\rvert\gg_q H\phi(Q')/Q'`$ for all sufficiently large H. In [2, 6], we took
this as our starting point, and then dealt with the extra primes
$`\lbrace p\le\log{H}:p\equiv1\bmod q\rbrace`$ in $`\mathcal{P}`$."

"What we need is an asymptotic for the number of integers, up to H, that are composed
only of primes both congruent to 1 mod q and greater than $`\log{H}`$. Much of this note
is devoted to establishing such a result (Lemma 3.3 below). Using this we are able to
show that $`\lvert S\rvert\gg_q H\phi(Q)/Q`$ for all sufficiently large H. Indeed, using
Lemma 3.4 (below) instead of [2, Lemma 6.5] in [2, 7], we are able to establish Theorem
1.1."

"We will show that the inequalities in Lemma 3.4 hold for q in a certain range depending
on H. This uniformity is not needed to prove Theorem 1.1, but it can be used to prove a
version of Theorem 1.1 in which q is allowed to tend very slowly to infinity with X. It
is hoped to publish an account of this, in which we will also consider 'strings' of more
than 2 congruent primes -- in longer intervals."

[extract note] The three footnotes of Section 2 are printed at the foot of pp.2-3.
Footnote 1 (p.2): "In fact, a lower bound for the number of such integers n, of the form
$`N/(\log{N})^{c}`$, c a positive constant, is implicit in the work of Goldston, Pintz,
and Yildirim." Footnote 2 (p.3): "Actually, if there happens to be an exceptional modulus
$`q_0\le N^{1/(\log{}\log{N})^{2}}`$, and if $`p_0`$ is its greatest prime factor, we
remove $`p_0`$ from the product defining Q, so that $`(Q,p_0)=1`$. See [4, Lemma 2] and
[2, 5] for details. We overlook this technical complication for the purposes of
simplifying the present discussion." Footnote 3 (p.3): "The fact that $`\mathcal{P}`$
contains all primes up to $`\log{H}`$ is used to show that, for a given k-tuple of linear
forms $`\mathcal{H}=\lbrace Qx+h_1,\ldots Qx+h_k\rbrace`$, $`h_i\in[1,H]`$,
$`(Q,h_1\cdots h_k)=1`$, we have
$`\mathfrak{S}(\mathcal{H})\sim(Q/\phi(Q))^{k}`$ as $`H\to\infty`$, where
$`\mathfrak{S}(\mathcal{H})`$ is the singular series for $`\mathcal{H}`$. See [2, Lemma
5.1] for details."

## 4. Section 3, Proof of Theorem 1.1 -- statements (pp.4-7)

"3. Proof of Theorem 1.1. Throughout this section, at each and every occurrence of O and
$`\ll`$, the implied constant is absolute. The letter c, by itself, always denotes an
absolute positive constant, possibly a different constant at each occurrence."

"Theorem 1.1 will follow from Lemma 3.4, below. Lemma 3.4 is a corollary of: Theorem 3.1,
which is a version of the Siegel-Walfisz theorem; Lemma 3.2, which is a version of
Mertens' theorem in which the primes are restricted to the arithmetic progression 1 mod
q; and Lemma 3.3, which gives an asymptotic for the number of integers, up to X, composed
only of primes that are both congruent to 1 mod q and greater than a power of
$`\log{X}`$."

"In each of the lemmas below, the estimates are shown to hold uniformly for q in a
certain range. We do not need this uniformity to prove Theorem 1.1 -- it would suffice to
use the prime number theorem for arithmetic progressions instead of Theorem 3.1, and
versions of Lemmas 3.2, 3.3, and 3.4 in which q is arbitrary but bounded."

"We use the Siegel-Walfisz theorem, in the following form, in the proofs of Lemmas 3.2
and 3.4:"

"Theorem 3.1 (Siegel-Walfisz). Fix a positive number A. For all sufficiently large X we
have, uniformly for integers q satisfying $`1\le q\le(\log{X})^{A}`$, the following
estimate:"
$$\sum_{\substack{p\le X\cr p\equiv1\bmod q}}1=\left(1+O\left(\frac{1}{\log{X}}\right)\right)\frac{X}{\phi(q)\log{X}}.$$

"Proof. Indeed, we have [9, 11.3, Corollary 11.20]:"
$$\sum_{\substack{p\le X\cr p\equiv a\bmod q}}1=\frac{\mathrm{li}(X)}{\phi(q)}+O\left(X\exp\left(-C_A\sqrt{\log{X}}\right)\right),$$
"uniformly for $`1\le q\le(\log{X})^{A}`$ and integers a coprime with q, where
$`C_A`$ is a positive constant depending only on A. The less precise and less general
statement of Theorem 3.1, which follows since
$`\mathrm{li}(X)=X/\log{X}+O(X/(\log{X})^{2})`$, is sufficient for our purposes."

"We will use the following version of Mertens' theorem in the proof of Lemma 3.4:"

"Lemma 3.2. Fix a positive number A. For all sufficiently large X we have, uniformly for
integers q satisfying $`1\le q\le(\log{X})^{A}`$, the following estimate:"
$$\prod_{\substack{p\le X\cr p\equiv1\bmod q}}\left(1-\frac{1}{p}\right)^{-1}=\left(1+O\left(\frac{1}{\log{X}}\right)\right)e^{\gamma/\phi(q)}c(q)(\log{X})^{\frac{1}{\phi(q)}},$$
"where $`\gamma=0.57721\ldots`$ is the Euler-Mascheroni constant, and $`c(q)`$ is a
positive constant depending only on q. We have $`c(1)=1`$ and $`c(2)=1/2`$."

"Proof. The case $`q=1`$ is Mertens' theorem, and the case $`q=2`$ follows at once from
this. We prove the result for $`3\le q\le(\log{X})^{A}`$ in 4, where $`c(q)`$ is given
explicitly."

"The following result, which reduces to [10, Lemma 2] in the case $`Y=1`$ (and q fixed),
is the key that allows us to establish the inequalities in Lemma 3.4 for all sufficiently
large H, rather than just for a certain sequence of H tending to infinity as in [2, 6]."

"Lemma 3.3. Fix a positive number A and a number $`\alpha\in(0,\frac{1}{2})`$. For all
sufficiently large X we have, uniformly for Y satisfying
$`1\le Y\le(\log{X})^{A}`$ and integers q satisfying
$`3\le q\le(\log{X})^{\alpha}`$, the following estimate:"
$$\sum_{\substack{n\le X\cr p\mid n\Rightarrow p\equiv1\bmod q\ \text{and}\ p>Y}}1=\left(1+O\left(\frac{(\log{}\log{X})^{c}}{(\log{X})^{1-2\alpha}}\right)\right)\frac{c(q)}{\Gamma(1/\phi(q))}\cdot\frac{X(\log{X})^{\frac{1}{\phi(q)}}}{\log{X}}\prod_{\substack{p\le Y\cr p\equiv1\bmod q}}\left(1-\frac{1}{p}\right),$$
"where $`c(q)`$ is the positive constant, depending only on q, in the statement of Lemma
3.2."

"Proof. See 4."

"Before stating Lemma 3.4, we need some definitions. Let a sufficiently large number H,
and a coprime pair of integers $`q\ge3`$ and a, be given. If $`a\equiv1\bmod q`$, let"
-- display (3.1), p.5:
$$\mathcal{P}(H):=\lbrace p\le\log{H}:p\equiv1\bmod q\rbrace\cup\lbrace p\le H/(\log{H})^{2}:p\not\equiv1\bmod q\rbrace.$$
"If $`a\not\equiv1\bmod q`$, define" -- display (3.2), p.6:
$$t(H):=\exp\left(\frac{(\log{H})(\log{}\log{}\log{H})}{2\log{}\log{H}}\right),$$
"and, noting that $`\log{H}<t(H)<H/t(H)<H/(\log{H})^{2}`$ for all sufficiently large H,
let" -- display (3.3), p.6:
$$\mathcal{P}(H):=\lbrace p\le\log{H}:p\equiv1\bmod q\rbrace$$
$$\cup\lbrace p\le H/(\log{H})^{2}:p\not\equiv1\bmod q\ \text{and}\ p\not\equiv a\bmod q\rbrace$$
$$\cup\lbrace t(H)<p\le H/(\log{H})^{2}:p\equiv1\bmod q\rbrace\cup\lbrace p\le H/t(H):p\equiv a\bmod q\rbrace.$$
"In other words, $`\mathcal{P}(H)`$ consists of all primes up to $`H/(\log{H})^{2}`$,
except for the primes"
$$\lbrace\log{H}<p\le t(H):p\equiv1\bmod q\rbrace\cup\lbrace H/t(H)<p\le H/(\log{H})^{2}:p\equiv a\bmod q\rbrace.$$
"In either case, set" -- display (3.4), p.6:
$$\tilde{Q}=\tilde{Q}(H;q,a):=q\prod_{p\in\mathcal{P}(H)}p,\qquad Q=Q(H;q,a):=q\prod_{\substack{p\in\mathcal{P}(H)\cr p\ne p_0}}p,$$
"where" -- display (3.5), p.6:
$$p_0=1\ \text{or}\ p_0\ \text{is a prime satisfying}\ p_0>\log{H}.$$
"(The minor technical complication of $`p_0`$ has to be accounted for in the proof of [4,
Theorem 1], and consequently in the proof of [2, Theorem 1.1]. It arises when taking into
consideration the possible existence of Siegel zeros -- see [4] for details.) Finally,
set" -- display (3.6), p.6:
$$S=S(H;q,a):=\lbrace1\le h\le H:(Q,h)=1\ \text{and}\ h\equiv a\bmod q\rbrace;$$
$$T=T(H;q,a):=\lbrace1\le h\le H:(Q,h)=1\ \text{and}\ h\not\equiv a\bmod q\rbrace.$$

"Lemma 3.4. Given a sufficiently large number H, and a coprime pair of integers
$`q\ge3`$ and a, let $`Q=Q(H;q,a)`$, $`S=S(H;q,a)`$, and $`T=T(H;q,a)`$ be as defined in
(3.1) - (3.6). (a) For all sufficiently large H we have, for integers q satisfying"
$$3\le q\le\frac{\log{}\log{H}}{\log{}\log{}\log{H}}$$
"and $`a\equiv1\bmod q`$, the inequality" -- display (3.7), p.6:
$$\lvert S\rvert-\lvert T\rvert\ge\frac{H}{\Gamma(1/\phi(q))}\left(\frac{\phi(Q)}{Q}\right).$$
"(b) For all sufficiently large H we have, for integers q satisfying"
$$3\le q\le\frac{\log{}\log{H}}{2\log{}\log{}\log{H}}$$
"and $`a\not\equiv1\bmod q`$ coprime with q, the inequality" -- display (3.8), p.7:
$$\lvert S\rvert-\lvert T\rvert\ge\frac{2}{5}\cdot\frac{H}{(1+\phi(q))\Gamma(1/\phi(q))}\left(\frac{\phi(Q)}{Q}\right).$$

## 5. Section 3, Proof of Theorem 1.1 (p.7, verbatim)

"Proof of Theorem 1.1. Fix an integer $`q\ge3`$, arbitrary but bounded, and an integer a
that is coprime with q. Let $`Q=Q(H;q,a)`$, $`S=S(H;q,a)`$, and $`T=T(H;q,a)`$ be as
defined in (3.1) - (3.6). In [2, 6.2], we showed that there is a positive constant A,
depending only on q, such that $`\lvert S\rvert-\lvert T\rvert\gg_q H\phi(Q)/Q`$ for some
$`H\in[Y/(\log{Y})^{A},Y]`$ and all sufficiently large Y. Using this, inter alia, we
established the lower bound (1.1) in [2, 7]. We also showed that if
$`\lvert S\rvert-\lvert T\rvert\gg_q H\phi(Q)/Q`$ for all sufficiently large H, then
(1.2) holds. Thus, Theorem 1.1 follows from Lemma 3.4, in the way described in [2, 7].
(Here, the constant implied by $`\gg_q`$ depends only on q.)"

## 6. Section 3, Proof of Lemma 3.4 (pp.7-13, verbatim)

"Proof of Lemma 3.4. Let H be a sufficiently large number, and let a coprime pair of
integers $`q\ge3`$ and a be given. Let $`\mathcal{P}(H)`$, $`t(H)`$,
$`\tilde{Q}=\tilde{Q}(H;q,a)`$, $`Q=Q(H;q,a)`$, $`p_0`$, $`S=S(H;q,a)`$, and
$`T=T(H;q,a)`$ be as defined in (3.1) - (3.6). We have" -- display (3.9), p.7:
$$\lvert T\rvert\ll\frac{H}{\log{H}}.$$
"This was shown in [2, 6.2], where $`q\ge3`$ was arbitrary but bounded. However, the
larger q is, the more primes there are that divide Q, hence the smaller the size of T. In
[2, 6.2], we actually bounded the size of T by counting: the primes up to H; the integers
of the form $`pp'`$, where $`p\in(H/(\log{H})^{2},H]`$ and
$`p'\in(\log{H},(\log{H})^{2}]`$; the integers up to H composed only of primes
$`p\le t(H)`$ (using a result of de Bruijn on smooth numbers); and, in the case
$`p_0\ne1`$, so that $`p_0>\log{H}`$ by (3.5), the multiples of $`p_0`$ up to H. Thus,
(3.9) indeed holds uniformly for $`q\ge3`$."

"Note that by definition of $`\tilde{Q}`$ and Q ((3.4), (3.5))," -- display (3.10), p.7:
$$\lvert S\rvert\ge\sum_{\substack{1\le h\le H\cr h\equiv1\bmod q\cr(\tilde{Q},h)=1}}1,$$
"and" -- display (3.11), p.7:
$$\phi(\tilde{Q})/\tilde{Q}\ge\left(1-\tfrac{1}{\log{H}}\right)\phi(Q)/Q.$$
"We will work mainly with $`\tilde{Q}`$."

"Now we suppose q satisfies $`3\le q\le(\log{H})^{\alpha}`$,
$`\alpha\in(0,\frac{1}{2})`$ given, and that $`a\equiv1\bmod q`$. Note that"
$$\log{\left(\frac{H}{(\log{H})^{2}}\right)}=(\log{H})\left(1+O\left(\frac{\log{}\log{H}}{\log{H}}\right)\right).$$
"Thus, by definition of $`\tilde{Q}`$ ((3.1), (3.4)), and two applications of Lemma 3.2,"
-- display (3.12), p.8:
$$\phi(\tilde{Q})/\tilde{Q}=\prod_{p\le H/(\log{H})^{2}}\left(1-\frac{1}{p}\right)\prod_{\substack{p\le H/(\log{H})^{2}\cr p\equiv1\bmod q}}\left(1-\frac{1}{p}\right)^{-1}\prod_{\substack{p\le\log{H}\cr p\equiv1\bmod q}}\left(1-\frac{1}{p}\right)$$
$$=\left(1+O\left(\frac{\log{}\log{H}}{\log{H}}\right)\right)e^{-\gamma(1-1/\phi(q))}c(q)\frac{(\log{H})^{\frac{1}{\phi(q)}}}{\log{H}}\prod_{\substack{p\le\log{H}\cr p\equiv1\bmod q}}\left(1-\frac{1}{p}\right),$$
"and so, by Lemma 3.3," -- display (3.13), p.8:
$$\sum_{\substack{1\le h\le H\cr h\equiv1\bmod q\cr(\tilde{Q},h)=1}}1\ge\sum_{\substack{1\le h\le H\cr p\mid h\Rightarrow p\equiv1\bmod q\ \text{and}\ p>\log{H}}}1=\left(1+O\left(\frac{(\log{}\log{H})^{c}}{(\log{H})^{1-2\alpha}}\right)\right)\frac{c(q)}{\Gamma(1/\phi(q))}\cdot\frac{H(\log{H})^{\frac{1}{\phi(q)}}}{\log{H}}\prod_{\substack{p\le\log{H}\cr p\equiv1\bmod q}}\left(1-\frac{1}{p}\right)$$
$$=\left(1+O\left(\frac{(\log{}\log{H})^{c}}{(\log{H})^{1-2\alpha}}\right)\right)\frac{e^{\gamma(1-1/\phi(q))}}{\Gamma(1/\phi(q))}H\phi(\tilde{Q})/\tilde{Q}.$$
"The left-hand side here is a lower bound for $`\lvert S\rvert`$ (3.10), so using the
second line of (3.13) with the bound $`\lvert T\rvert\ll H/\log{H}`$ (3.9), we obtain"
$$\frac{\lvert T\rvert}{\lvert S\rvert}\ll\frac{\Gamma(1/\phi(q))}{c(q)(\log{H})^{\frac{1}{\phi(q)}}}\prod_{\substack{p\le\log{H}\cr p\equiv1\bmod q}}\left(1-\frac{1}{p}\right)^{-1}.$$
"At this point we suppose that q is in the rather smaller range"
$$3\le q\le\frac{\log{}\log{H}}{\log{}\log{}\log{H}}.$$
"Then we may apply Lemma 3.2 to this last product to obtain"
$$\frac{\lvert T\rvert}{\lvert S\rvert}\ll\Gamma(1/\phi(q))\left(\frac{\log{}\log{H}}{\log{H}}\right)^{\frac{1}{\phi(q)}}\ll\phi(q)\left(\frac{\log{}\log{H}}{\log{H}}\right)^{\frac{1}{\phi(q)}},$$
"and so"
$$\log{(\lvert T\rvert/\lvert S\rvert)}\le O(1)+\log{\phi(q)}+\frac{1}{\phi(q)}(\log{}\log{}\log{H}-\log{}\log{H})$$
$$\le O(1)+\log{q}+\frac{1}{q}(\log{}\log{}\log{H}-\log{}\log{H})\le O(1)-\log{}\log{}\log{}\log{H}.$$
"Hence $`\lvert T\rvert/\lvert S\rvert\ll1/\log{}\log{}\log{H}`$, and combining this with
(3.10), (3.11), and (3.13), we obtain"
$$\lvert S\rvert-\lvert T\rvert\ge\left(1+O\left(\frac{1}{\log{}\log{}\log{H}}\right)\right)\frac{e^{\gamma(1-1/\phi(q))}}{\Gamma(1/\phi(q))}H\frac{\phi(Q)}{Q}.$$
"Noting that $`e^{\gamma(1-1/\phi(q))}\ge e^{\gamma/2}>1`$ we obtain (3.7) (for all
sufficiently large H), and the proof of part (a) is complete."

"Now we suppose $`a\not\equiv1\bmod q`$. Once again we suppose that
$`3\le q\le(\log{H})^{\alpha}`$, $`\alpha\in(0,\frac{1}{2})`$ given, until we want to
show that $`\lvert T\rvert/\lvert S\rvert=o(1)`$. Let us first of all show that"
-- display (3.14), p.9:
$$\phi(\tilde{Q})/\tilde{Q}=\left(1+O\left(\frac{\log{}\log{}\log{H}}{\log{}\log{H}}\right)\right)\times e^{-\gamma(1-1/\phi(q))}c(q)\cdot\frac{(\log{t(H)})^{\frac{1}{\phi(q)}}}{\log{H}}\prod_{\substack{p\le\log{H}\cr p\equiv1\bmod q}}\left(1-\frac{1}{p}\right).$$
"For by definition of $`\tilde{Q}`$ ((3.2) - (3.4))," -- display (3.15), p.9:
$$\phi(\tilde{Q})/\tilde{Q}=\prod_{p\le H/(\log{H})^{2}}\left(1-\frac{1}{p}\right)\prod_{\substack{\log{H}<p\le t(H)\cr p\equiv1\bmod q}}\left(1-\frac{1}{p}\right)^{-1}\prod_{\substack{H/t(H)<p\le H/(\log{H})^{2}\cr p\equiv a\bmod q}}\left(1-\frac{1}{p}\right)^{-1}.$$
"By Mertens' theorem (the case $`q=1`$ in Lemma 3.2)," -- display (3.16), p.9:
$$\prod_{p\le H/(\log{H})^{2}}\left(1-\frac{1}{p}\right)=\left(1+O\left(\frac{\log{}\log{H}}{\log{H}}\right)\right)\frac{e^{-\gamma}}{\log{H}}.$$
"Since $`\log{t(H)}=(\log{H})(\log{}\log{}\log{H})/(2\log{}\log{H})`$ by definition (3.2)
of $`t(H)`$, we certainly have
$`3\le q\le(\log{H})^{\frac{1}{2}}\le\log{t(H)}`$ for all sufficiently large H, so
applying Lemma 3.2 with $`A=1`$, we obtain" -- display (3.17), p.10:
$$\prod_{\substack{\log{H}<p\le t(H)\cr p\equiv1\bmod q}}\left(1-\frac{1}{p}\right)^{-1}=\left(1+O\left(\frac{\log{}\log{H}}{(\log{H})(\log{}\log{}\log{H})}\right)\right)\times e^{\gamma/\phi(q)}c(q)(\log{t(H)})^{\frac{1}{\phi(q)}}\prod_{\substack{p\le\log{H}\cr p\equiv1\bmod q}}\left(1-\frac{1}{p}\right).$$
"As for the third product on the right-hand side of (3.15), we have"
$$1\le\prod_{\substack{H/t(H)<p\le H/(\log{H})^{2}\cr p\equiv a\bmod q}}\left(1-\frac{1}{p}\right)^{-1}\le\prod_{H/t(H)<p\le H/(\log{H})^{2}}\left(1-\frac{1}{p}\right)^{-1},$$
"and so two further applications of Mertens' theorem, plus a short calculation using the
fact that $`\log{t(H)}=(\log{H})(\log{}\log{}\log{H})/(2\log{}\log{H})`$, reveal that"
-- display (3.18), p.10:
$$1\le\prod_{\substack{H/t(H)<p\le H/(\log{H})^{2}\cr p\equiv a\bmod q}}\left(1-\frac{1}{p}\right)^{-1}\le1+O\left(\frac{\log{}\log{}\log{H}}{\log{}\log{H}}\right).$$
"Combining (3.18), (3.17), (3.16), and (3.15) gives (3.14)."

"Next, we will show that" -- display (3.19), p.10:
$$\sum_{\substack{1\le h\le H\cr h\equiv a\bmod q\cr(\tilde{Q},h)=1}}1\ge\left(1+O\left(\frac{\log{}\log{}\log{H}}{\log{}\log{H}}\right)\right)\times\frac{\frac{1}{2}\left(1-\frac{1}{e}\right)}{1+\phi(q)}\cdot\frac{c(q)}{\Gamma(1/\phi(q))}\cdot\frac{H(\log{t(H)})^{\frac{1}{\phi(q)}}}{\log{H}}\prod_{\substack{p\le\log{H}\cr p\equiv1\bmod q}}\left(1-\frac{1}{p}\right).$$
"To this end we note, from the definition of $`\tilde{Q}`$ ((3.3), (3.4)), that if
$`h=pm`$, where $`p>H/t(H)`$ is a prime congruent to $`a\bmod q`$, and
$`m\le H/p<t(H)`$ is composed only of primes that are greater than $`\log{H}`$ and
congruent to $`1\bmod q`$, then $`h\equiv a\bmod q`$ and $`(\tilde{Q},h)=1`$. We
partition $`(H/t(H),H]`$ into sub-intervals"
$$I_l:=(e^{l-1}H/t(H),e^{l}H/t(H)],\qquad1\le l\le\log{t(H)},$$
"and deduce that" -- display (3.20), p.10:
$$\sum_{\substack{1\le h\le H\cr h\equiv a\bmod q\cr(\tilde{Q},h)=1}}1\ge\sum_{1\le l\le\log{t(H)}}\ \sum_{\substack{p\in I_l\cr p\equiv a\bmod q}}\ \sum_{\substack{m\le t(H)/e^{l}\cr p\mid m\Rightarrow p\equiv1\bmod q\ \text{and}\ p>\log{H}}}1.$$
"Now, for $`0\le l\le\log{t(H)}`$, we have"
$$\log{\left(\frac{e^{l}H}{t(H)}\right)}=(\log{H})\left(1+O\left(\frac{\log{t(H)}}{\log{H}}\right)\right)=(\log{H})\left(1+O\left(\frac{\log{}\log{}\log{H}}{\log{}\log{H}}\right)\right),$$
"because $`\log{t(H)}=(\log{H})(\log{}\log{}\log{H})/(2\log{}\log{H})`$ by definition
(3.2) of $`t(H)`$. In particular, since $`q\le(\log{H})^{\alpha}`$,
$`\alpha<\frac{1}{2}`$, we certainly have $`q\le\log{(e^{l}H/t(H))}`$ for all
sufficiently large H. Therefore we may apply Theorem 3.1 (Siegel-Walfisz), with
$`A=1`$, to obtain, for $`1\le l\le\log{t(H)}`$," -- display (3.21), p.11:
$$\sum_{\substack{p\in I_l\cr p\equiv a\bmod q}}1=\sum_{\substack{p\le e^{l}H/t(H)\cr p\equiv a\bmod q}}1-\sum_{\substack{p\le e^{l-1}H/t(H)\cr p\equiv a\bmod q}}1=\left(1+O\left(\frac{\log{}\log{}\log{H}}{\log{}\log{H}}\right)\right)\cdot\frac{1}{\phi(q)}\cdot\frac{H}{t(H)\log{H}}\left(1-\frac{1}{e}\right)e^{l}.$$
"Also, since $`\log{t(H)}=(\log{H})(\log{}\log{}\log{H})/(2\log{}\log{H})`$ by definition
(3.2) of $`t(H)`$, we have, for $`1\le l\le\frac{1}{2}\log{t(H)}`$, that
$`\log{H}=\left(\log{(t(H)/e^{l})}\right)^{1+o(1)}`$, where $`o(1)`$ is shorthand for
$`O(\log{}\log{}\log{H}/\log{}\log{H})`$. Thus, for
$`1\le l\le\frac{1}{2}\log{t(H)}`$ and all sufficiently large H, we have"
$$3\le q\le(\log{H})^{\alpha}\le\left(\log{(t(H)/e^{l})}\right)^{\beta},\qquad\beta:=\tfrac{1}{2}(\alpha+\tfrac{1}{2})\in(0,\tfrac{1}{2}).$$
"Therefore, for $`1\le l\le\frac{1}{2}\log{t(H)}`$, we may apply Lemma 3.3, with
$`\beta`$ in place of $`\alpha`$, and $`A=2`$, say, to obtain"
-- display (3.22), p.11:
$$\sum_{\substack{m\le t(H)/e^{l}\cr p\mid m\Rightarrow p\equiv1\bmod q\ \text{and}\ p>\log{H}}}1=\left(1+O\left(\frac{(\log{}\log{t(H)})^{c}}{(\log{t(H)})^{1-2\beta}}\right)\right)\frac{c(q)}{\Gamma(1/\phi(q))}\times\frac{t(H)}{e^{l}}\cdot\frac{\left(\log{(t(H)/e^{l})}\right)^{\frac{1}{\phi(q)}}}{\log{(t(H)/e^{l})}}\prod_{\substack{p\le\log{H}\cr p\equiv1\bmod q}}\left(1-\frac{1}{p}\right)$$
$$\ge\left(1+O\left(\frac{(\log{}\log{t(H)})^{c}}{(\log{t(H)})^{1-2\beta}}\right)\right)\frac{c(q)}{\Gamma(1/\phi(q))}\times\frac{t(H)}{e^{l}}\cdot\frac{(\log{t(H)})^{\frac{1}{\phi(q)}}}{\log{t(H)}}\left(1-\frac{l}{\log{t(H)}}\right)^{\frac{1}{\phi(q)}}\prod_{\substack{p\le\log{H}\cr p\equiv1\bmod q}}\left(1-\frac{1}{p}\right).$$
"Note that, since
$`\log{t(H)}=(\log{H})(\log{}\log{}\log{H})/(2\log{}\log{H})`$ by definition (3.2),"
$$\frac{(\log{}\log{t(H)})^{c}}{(\log{t(H)})^{1-2\beta}}\ll\frac{\log{}\log{}\log{H}}{\log{}\log{H}}$$
"for all sufficiently large H. Thus, combining (3.22) and (3.21) with (3.20), we obtain"
-- display (3.23), p.12:
$$\sum_{\substack{1\le h\le H\cr h\equiv a\bmod q\cr(\tilde{Q},h)=1}}1\ge\left(1+O\left(\frac{\log{}\log{}\log{H}}{\log{}\log{H}}\right)\right)\frac{c(q)}{\Gamma(1/\phi(q))}\cdot\frac{H(\log{t(H)})^{\frac{1}{\phi(q)}}}{\log{H}}\prod_{\substack{p\le\log{H}\cr p\equiv1\bmod q}}\left(1-\frac{1}{p}\right)$$
$$\times\left(1-\frac{1}{e}\right)\cdot\frac{1}{\phi(q)}\cdot\frac{1}{\log{t(H)}}\sum_{1\le l\le\frac{1}{2}\log{t(H)}}\left(1-\frac{l}{\log{t(H)}}\right)^{\frac{1}{\phi(q)}}.$$
"Finally,"
$$\sum_{1\le l\le\frac{1}{2}\log{t(H)}}\left(1-\frac{l}{\log{t(H)}}\right)^{\frac{1}{\phi(q)}}\ge\int_{1}^{\frac{1}{2}\log{t(H)}}\left(1-\frac{u}{\log{t(H)}}\right)^{\frac{1}{\phi(q)}}du$$
$$=\frac{\log{t(H)}}{1+\frac{1}{\phi(q)}}\left(\left(1-\frac{1}{\log{t(H)}}\right)^{1+\frac{1}{\phi(q)}}-\left(\frac{1}{2}\right)^{1+\frac{1}{\phi(q)}}\right)\ge\frac{\log{t(H)}}{1+\frac{1}{\phi(q)}}\left(\left(1-\frac{1}{\log{t(H)}}\right)^{2}-\frac{1}{2}\right)$$
$$=\frac{\log{t(H)}}{1+\frac{1}{\phi(q)}}\cdot\frac{1}{2}\left(1+O\left(\frac{1}{\log{t(H)}}\right)\right),$$
"and combining this with (3.23) gives (3.19)."

"Comparing (3.14) with (3.19), then using (3.10) and (3.11), we see that"
-- display (3.24), p.12:
$$\lvert S\rvert\ge\sum_{\substack{1\le h\le H\cr h\equiv a\bmod q\cr(\tilde{Q},h)=1}}1\ge\left(1+O\left(\frac{\log{}\log{}\log{H}}{\log{}\log{H}}\right)\right)\frac{\frac{1}{2}\left(1-\frac{1}{e}\right)}{1+\phi(q)}\cdot\frac{e^{\gamma(1-1/\phi(q))}}{\Gamma(1/\phi(q))}H\phi(\tilde{Q})/\tilde{Q}$$
$$\ge\left(1+O\left(\frac{\log{}\log{}\log{H}}{\log{}\log{H}}\right)\right)\frac{\frac{1}{2}\left(1-\frac{1}{e}\right)}{1+\phi(q)}\cdot\frac{e^{\gamma(1-1/\phi(q))}}{\Gamma(1/\phi(q))}H\phi(Q)/Q.$$
"Also, using the bound $`\lvert T\rvert\ll H/\log{H}`$ (3.9), and combining (3.10) with
(3.19), we obtain"
$$\frac{\lvert T\rvert}{\lvert S\rvert}\ll\frac{\phi(q)\Gamma(1/\phi(q))}{c(q)(\log{t(H)})^{\frac{1}{\phi(q)}}}\prod_{\substack{p\le\log{H}\cr p\equiv1\bmod q}}\left(1-\frac{1}{p}\right)^{-1}.$$
"At this point we suppose that q is in the rather smaller range"
$$3\le q\le\frac{1}{2}\cdot\frac{\log{}\log{H}}{\log{}\log{}\log{H}}.$$
"Then we may apply Lemma 3.2 to this last product to obtain"
$$\frac{\lvert T\rvert}{\lvert S\rvert}\ll\phi(q)\Gamma(1/\phi(q))\left(\frac{\log{}\log{H}}{\log{t(H)}}\right)^{\frac{1}{\phi(q)}}\ll(\phi(q))^{2}\left(\frac{\log{}\log{H}}{\log{t(H)}}\right)^{\frac{1}{\phi(q)}},$$
"and so, since
$`\log{t(H)}=(\log{H})(\log{}\log{}\log{H})/(2\log{}\log{H})`$ by (3.2),"
$$\log{(\lvert T\rvert/\lvert S\rvert)}\le O(1)+2\log{\phi(q)}+\frac{1}{\phi(q)}(\log{}\log{}\log{H}-\log{}\log{t(H)})$$
$$\le O(1)+2\log{q}+\frac{1}{q}\left(2\log{}\log{}\log{H}-\log{}\log{H}-\log{}\log{}\log{}\log{H}+O(1)\right)\le O(1)-2\log{}\log{}\log{}\log{H}.$$
"Hence $`\lvert T\rvert/\lvert S\rvert\ll1/(\log{}\log{}\log{H})^{2}`$, and, combining
this with the last inequality in (3.24), we obtain"
$$\lvert S\rvert-\lvert T\rvert\ge\left(1+O\left(\frac{1}{(\log{}\log{}\log{H})^{2}}\right)\right)\frac{\frac{1}{2}\left(1-\frac{1}{e}\right)}{1+\phi(q)}\cdot\frac{e^{\gamma(1-1/\phi(q))}}{\Gamma(1/\phi(q))}H\phi(Q)/Q.$$
"Noting that
$`\frac{1}{2}\left(1-\frac{1}{e}\right)e^{\gamma(1-1/\phi(q))}\ge\frac{1}{2}\left(1-\frac{1}{e}\right)e^{\gamma/2}=0.42\ldots>\frac{2}{5}`$,
we obtain (3.8) (for all sufficiently large H), and the proof of part (b) is complete."

## 7. Scope boundary

[extract note] The declared scope of this extract ends with the proof of Lemma 3.4, at
the foot of p.13. Two further sections are present in the source and lie outside that
scope: Section 4, headed "4. Proof of Lemmas 3.2 and 3.3", whose first page is p.13 and
which runs to p.29; and Section 5, headed "5. Acknowledgements", on p.29. A reference
list follows on pp.29-30 and the address block "Institutionen for matematik, KTH, 100 44
Stockholm, Sweden" with an e-mail address closes p.30. No content of Sections 4 and 5 is
transcribed or characterised here.

## 8. Uniformity ledger

- [extract note] Theorem 1.1 fixes $`\epsilon>0`$ and a coprime pair $`q\ge3`$, a, and
  asserts an absolute positive constant c in (1.2), for all sufficiently large X (p.2).
- [extract note] Theorem 3.1 and Lemma 3.2 are stated uniformly for
  $`1\le q\le(\log{X})^{A}`$ with A fixed, for all sufficiently large X (pp.4-5); Lemma
  3.2's $`c(q)`$ depends only on q, with $`c(1)=1`$ and $`c(2)=1/2`$.
- [extract note] Lemma 3.3 is stated uniformly for $`1\le Y\le(\log{X})^{A}`$ and
  $`3\le q\le(\log{X})^{\alpha}`$ with A fixed and
  $`\alpha\in(0,\frac{1}{2})`$ fixed, for all sufficiently large X (p.5); its $`c(q)`$ is
  the constant of Lemma 3.2.
- [extract note] Lemma 3.4 has two different q-ranges: part (a) requires
  $`3\le q\le\log{}\log{H}/\log{}\log{}\log{H}`$ and $`a\equiv1\bmod q`$ (p.6); part (b)
  requires $`3\le q\le\log{}\log{H}/(2\log{}\log{}\log{H})`$ and
  $`a\not\equiv1\bmod q`$ (p.7). Both are for all sufficiently large H.
- [extract note] Throughout Section 3 the constants implied by O and $`\ll`$ are stated
  absolute, and the letter c denotes an absolute positive constant, possibly different at
  each occurrence (p.4).
- [extract note] The source states that the uniformity in q is not needed for Theorem
  1.1: the prime number theorem for arithmetic progressions and bounded-q versions of
  Lemmas 3.2-3.4 would suffice (p.4).
- [extract note] The proof of Theorem 1.1 (p.7) fixes q "arbitrary but bounded"; the
  constant implied by $`\gg_q`$ there depends only on q.

## 9. Structural map

[extract note] 1. Theorem 1.1 (p.2) is proved on p.7 from Lemma 3.4 together with two
results imported from [2]: the range statement of [2, 6.2] and the implication of [2, 7]
that $`\lvert S\rvert-\lvert T\rvert\gg_q H\phi(Q)/Q`$ for all sufficiently large H gives
(1.2).
[extract note] 2. Theorem 3.1 (p.4) is derived from [9, 11.3, Corollary 11.20]; Lemma
3.2 (p.5) is stated with its q=1 and q=2 cases settled and the range
$`3\le q\le(\log{X})^{A}`$ deferred to Section 4; Lemma 3.3 (p.5) is stated with its
proof deferred to Section 4.
[extract note] 3. The construction (3.1)-(3.6) (pp.5-6) defines $`\mathcal{P}(H)`$ in two
cases, $`t(H)`$ by (3.2), $`\tilde{Q}`$ and Q by (3.4) with the $`p_0`$ clause (3.5), and
S and T by (3.6).
[extract note] 4. Lemma 3.4(a) (pp.7-9) invokes (3.9) (imported from [2, 6.2]), (3.10),
(3.11), Lemma 3.2 twice at (3.12), Lemma 3.3 at (3.13), and Lemma 3.2 again for the
$`\lvert T\rvert/\lvert S\rvert`$ bound.
[extract note] 5. Lemma 3.4(b) (pp.9-13) invokes (3.15) and Mertens' theorem at (3.16)
and (3.18), Lemma 3.2 at (3.17), giving (3.14); then the partition into $`I_l`$ at
(3.20), Theorem 3.1 at (3.21) and Lemma 3.3 at (3.22), giving (3.23) and then (3.19);
then (3.14), (3.19), (3.10) and (3.11) give (3.24), and Lemma 3.2 once more bounds
$`\lvert T\rvert/\lvert S\rvert`$.
[extract note] 6. The numerical step closing part (b) is
$`\frac{1}{2}(1-1/e)e^{\gamma/2}=0.42\ldots>\frac{2}{5}`$, printed on p.13.

## FLAGS

- sha256 of the local file matches the anchor line above, verified before the source was
  opened. TRANSCRIPTION-UNSURE passages: 0.
- V8 (this source): 30 PDF pages against a steering expectation of about 29-30; printed
  pagination 1-30 coincides with the PDF pages.
- V9 (this source): the first page of Section 4, "4. Proof of Lemmas 3.2 and 3.3", is
  p.13 of the anchored PDF, matching the steering read of the non-canonical copy.
- Divergence from the dispatch's Section 4.5 attention list: it named "Lemma 3.3
  (statement only is fine for its proof, the statement verbatim)". The source prints no
  proof of Lemma 3.3 in Section 3 at all -- the line after the statement is "Proof. See
  4." -- so the statement is all there is inside the declared scope.
- Divergence, same list: it named "the construction displays (3.1)-(3.6) including t(H)
  and the p_0 clause". Those are present as transcribed. The list did not name the
  displays (3.7)-(3.24), which the source also numbers inside Sections 3; all of them are
  transcribed above under the object-coverage rule.
- Divergence, same list: it named "the two epsilon(X) comparison displays" in Section 1.
  The source prints them unnumbered, immediately after Theorem 1.1 on p.2, and attributes
  them to Shiu [10, Theorem 2] with the case split $`a\equiv\pm1\bmod q`$ versus
  otherwise.
- The source prints a section sign before section numbers in cross-references; the
  transcription convention for it is stated in Section 0.
