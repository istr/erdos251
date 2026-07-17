# Extraction: Pilatte, "Improved bounds for the two-point logarithmic Chowla conjecture"

Source (sole evidence base): /home/istr/pro/erdos251/dossier/2310.19357v2.pdf
arXiv:2310.19357v2 [math.NT], dated 1 Dec 2025 on the title page. Author: Cedric Pilatte. 66 pages.

Scope: INTERFACE-ONLY extraction (main theorems, corollaries on two-point
correlations, stated limitations). Proof internals (Sections 4-13, Appendices
A-C) are NOT anatomized; they are referenced only where the paper itself
describes the interface.

Method note: structure located via pdftotext; every verbatim quote below was
verified against visually rendered pages 1-12 (Read tool on the PDF, plus
200-dpi crops of pages 8 and 11 for equations (6), (7), Prop 3.4, Remark 3.5).
Pages 13-66 were surveyed by pdftotext only and NO quotes are taken from them.

Transliteration conventions (ASCII-only requirement): author/name diacritics
dropped (Radziwill, Teravainen, Matomaki, Erdos); math is transcribed in LaTeX
tokens; the paper's \leqslant / \geqslant are written \leq / \geq; blackboard
N, Z as \mathbb{N}, \mathbb{Z}; calligraphic P_j, D as \mathcal{P}_j,
\mathcal{D}. In-text citation numbers [5], [11], [14], [15], [22], [23], [24],
[25] are the paper's own bibliography keys, kept as printed.

---

## 1. Identification and abstract

Title (verbatim): "IMPROVED BOUNDS FOR THE TWO-POINT LOGARITHMIC CHOWLA
CONJECTURE"

Abstract (verbatim, p. 1):
"Let \lambda be the Liouville function, defined as \lambda(n) := (-1)^{\Omega(n)}
where \Omega(n) is the number of prime factors of n with multiplicity. In 2021,
Helfgott and Radziwill proved that
  \sum_{n \leq x} \frac{1}{n} \lambda(n)\lambda(n+1) \ll \frac{\log x}{(\log\log x)^{1/2}},
improving earlier results by Tao and Teravainen. We prove that
  \sum_{n \leq x} \frac{1}{n} \lambda(n)\lambda(n+1) \ll (\log x)^{1-c}
for some absolute constant c > 0. This appears to be best possible with
current methods."

---

## 2. Parameter setup (the hypotheses' function class, ranges, averaging)

Notation 2.1 (\varepsilon_1, H, H_0) (verbatim, Sec. 2.1, p. 7):
"Let \varepsilon_1 > 0 be a sufficiently small constant. Let H \in \mathbb{N}
be sufficiently large in terms of \varepsilon_1. Let
H_0 := \exp((\log H)^{1-\varepsilon_1})."

Definition 2.2 (J, \mathcal{P}_i, V_i, V) (verbatim, Sec. 2.1, p. 7):
"Let J be an integer satisfying 1 \leq J \leq \varepsilon_1^2 \log\log H.
For 1 \leq j \leq J, let \mathcal{P}_j be the set of all primes p such that
  C^{2j-2} < \frac{\log p}{\log H_0} < C^{2j-1},
where C := \exp(\varepsilon_1 (\log\log H)/(2J)).
For each 1 \leq j \leq J, we define V_j := \sum_{p \in \mathcal{P}_j} 1/p, and
we let V := \max_{1 \leq j \leq J} V_j."

Lemma 2.3 (verbatim, Sec. 2.1, pp. 7-8):
"The sets \mathcal{P}_j and parameters V_j satisfy the following properties:
(a) \mathcal{P}_1, ..., \mathcal{P}_J are disjoint subsets of (H_0, H);
(b) if (p_1, ..., p_J) \in \mathcal{P}_1 \times ... \times \mathcal{P}_J, then
    p_1 p_2 ... p_J < H and p_1 p_2 ... p_i < p_{i+1}^{1/10} for all
    1 \leq i < J;
(c) \varepsilon_1^{-1} \ll V \asymp \frac{\varepsilon_1 \log\log H}{J}
    \ll \varepsilon_1 \log\log H;
(d) V_1 V_2 ... V_J \asymp V^J \ll (\log H)^{c_0(\varepsilon_1)} where
    c_0(\varepsilon_1) := \varepsilon_1^2 \log(\frac{1}{2\varepsilon_1}).
    Moreover, in the special case where
    J = \lfloor \varepsilon_1^2 \log\log H \rfloor, we have
    V^J \asymp_{\varepsilon_1} (\log H)^{c_0(\varepsilon_1)}."

Notation 2.7 (\mathcal{D}, I_N, \mathcal{P}) (verbatim, Sec. 2.3, p. 8):
"To shorten the expressions, we define \mathcal{D} \subset (H_0, H) to be the
set of all products p_1 p_2 ... p_J with p_j \in \mathcal{P}_j for all
j \in [[J]]. We also write I_N := \mathbb{N} \cap (N, 2N] and
\mathcal{P} := \bigsqcup_{j=1}^{J} \mathcal{P}_j."
[Here [[J]] denotes the paper's double-bracket {1,...,J}, Sec. 1.4.]

Parameter table (Sec. 1.4, p. 6, transcribed):
  \varepsilon_1 : \varepsilon_1 > 0 sufficiently small (Notation 2.1)
  H   : H = H(\varepsilon_1) sufficiently large       (Notation 2.1)
  H_0 : H_0 = \exp((\log H)^{1-\varepsilon_1})        (Notation 2.1)
  J   : 1 \leq J \leq \varepsilon_1^2 \log\log H      (Definition 2.2)
  V_j : V_j = \sum_{p \in \mathcal{P}_j} 1/p \leq V   (Definition 2.2)
  V   : \varepsilon_1^{-1} \ll V \ll \varepsilon_1 \log\log H (Definition 2.2)
  N   : N \geq \exp((\log H)^{2.001})                 (Theorem 2.4)
  K   : K = \lfloor \log H \rfloor                    (Notation 5.2)
  L   : L = K^{1-10\varepsilon_1}                     (Notation 7.1)

---

## 3. Main theorem (the engine's emitted estimate)

Theorem 2.4 (verbatim, Sec. 2.2, p. 8):
"Let N be an integer such that \log N \geq (\log H)^{2.001}. Then
(6)  \sum_{(p_1,...,p_J) \in \mathcal{P}_1 \times ... \times \mathcal{P}_J}
     \sum_{\substack{n \in (N,2N] \\ p_1 ... p_J | n}}
     \lambda(n) \lambda(n + p_1 ... p_J)
     \leq e^{O(J)} (V_1 ... V_J)^{1/2} N."
NOTE (verified visually at 200 dpi): equation (6) carries NO absolute-value
bars; the left-hand side is the plain (signed) double sum. The absolute-value
strengthening is Remark 2.6 / eq. (7) below.

Remark 2.5 (verbatim, p. 8):
"Theorem 2.4 should be compared with the trivial bound \ll V_1 ... V_J N.
For J = 1, we recover the result of Helfgott and Radziwill [11]. Crucially,
however, our approach allows J to be as large as a small multiple of
\log\log H. By Lemma 2.3, this flexibility enables us to save a power of
\log H."

Remark 2.6 (verbatim, p. 8):
"In fact, our methods yield a slightly stronger estimate with absolute values:
(7)  \sum_{(p_1,...,p_J) \in \mathcal{P}_1 \times ... \times \mathcal{P}_J}
     \left| \sum_{\substack{n \in (N,2N] \\ p_1 ... p_J | n}}
     \lambda(n) \lambda(n + p_1 ... p_J) \right|
     \leq e^{O(J)} (V_1 ... V_J)^{1/2} N.
This follows by repeating the proof with arbitrary signs
c_{p_1,...,p_J} \in \{\pm 1\}, but for clarity we focus on the version in
Theorem 2.4, which suffices for our main application."
NOTE (verified visually): in (7) the bars enclose ONLY the inner sum over n;
the outer sum over the shift tuples is a sum of absolute values.

Shape summary of the emitted bound: averaging is over ALL shift tuples in the
full product set \mathcal{P}_1 \times ... \times \mathcal{P}_J (so over all
d = p_1...p_J \in \mathcal{D} \subset (H_0, H)); the inner n-sum is over a
dyadic block (N, 2N] RESTRICTED by the divisibility condition d | n; the gain
over the trivial bound V_1...V_J N is the square root (V_1...V_J)^{1/2}, up to
e^{O(J)}; uniformity in signs per shift tuple is available (Remark 2.6).

---

## 4. Headline corollary: two-point logarithmic Chowla

Theorem 1.1 (Logarithmic two-point Chowla correlations) (verbatim, p. 3):
"For some absolute constant c > 0,
  \sum_{n \leq x} \frac{1}{n} \lambda(n) \lambda(n+1) \ll (\log x)^{1-c}."

Consumption mechanics (proof of Theorem 1.1 assuming Theorem 2.4, Sec. 2.3,
p. 9; key identities, transcribed from the visually read page):
- Choice: J := \lfloor \varepsilon_1^2 \log\log H \rfloor,
  x := \exp((\log H)^6); by Lemma 2.3,
  (8) V^J \asymp_{\varepsilon_1} (\log H)^{\varepsilon_1^2 \log(\frac{1}{2\varepsilon_1})}.
- The multiplicativity step (verbatim sentence introducing it, p. 8): "We now
  show how a bound on this expression implies a bound on the two-point
  logarithmic Chowla conjecture. This step is due to Tao [22], and crucially
  relies on the multiplicativity of \lambda. Together with the proof of
  Proposition 3.1, this is the only place where the multiplicativity of
  \lambda is used - the rest of the paper will only use that \lambda is
  1-bounded."
- Identity (9): V_1 ... V_J \sum_{n \leq x} \frac{1}{n} \lambda(n)\lambda(n+1)
  = \sum_{d \in \mathcal{D}} \sum_{m \leq dx, d | m} \frac{1}{m}
  \lambda(m)\lambda(m+d),
  obtained from \lambda completely multiplicative and \lambda^2 = 1 via
  \sum_{n \leq x} \frac{1}{n}\lambda(n)\lambda(n+1)
  = d \sum_{m \leq dx, d|m} \frac{1}{m} \lambda(m)\lambda(m+d).
- Theorem 2.4 is then applied dyadically for \log N \geq (\log H)^3
  = \sqrt{\log x}, trivial bound below that, partial summation, final bound
  \ll \frac{1}{V^J}(e^{O(J)} V^{J/2} \log x + V^J \log H) \ll (\log x)^{1-c}.

---

## 5. Corollary at almost all scales (unweighted average)

Remark 2.8 (Two-point Chowla at almost all scales) (verbatim, p. 10):
"Our main result also implies an improved quantitative version of Chowla's
conjecture for two-point correlations at almost all scales. Namely, for all
2 < w \leq X, we have
(15)  \frac{1}{\log w} \int_{X/w}^{X} \left| \frac{1}{x} \sum_{n \leq x}
      \lambda(n)\lambda(n+1) \right| \frac{dx}{x} \ll \frac{1}{(\log w)^c},
where c > 0 is an absolute constant. In particular, we get
  \frac{1}{x} \sum_{n \leq x} \lambda(n)\lambda(n+1) \ll \frac{1}{(\log X)^{c/2}}
for all x \in [1, X] outside of a set E_X of logarithmic density
O((\log X)^{-c/2}).
This almost all scales result (15) follows from (7) by a straightforward
adaptation of the proof in [11, Section 8] (which in turn was inspired by
[24]) to our setting."
Footnote 1 (verbatim): "This means that \frac{1}{\log X} \int_1^X
1_{E_X}(x) \frac{dx}{x} \ll (\log X)^{-c/2}."

Other corollaries: the paper states NO further correlation corollaries. In
particular there is NO stated result for \omega(n) or for any multiplicative
function other than the Liouville \lambda (checked by grep over the full
pdftotext output for "multiplicative function", "corollar", "omega"). The only
generality statement is the unquantified remark quoted in Section 6 item (c)
below ("should generalise to a wider class of multiplicative functions").

---

## 6. Stated limitations (verbatim quotes)

(a) Abstract, p. 1: "This appears to be best possible with current methods."

(b) After Theorem 1.1, p. 3 (savings ceiling):
"It appears that saving a fixed power of the logarithm is the best that is
achievable with current techniques. Ultimately, our proof relies on the work
of Matomaki and Radziwill [14] on multiplicative functions in short intervals,
where the current state of the art only allows to save a small power of
\log x. The exploitation of multiplicativity using an idea of Tao [22] also
separately appears to limit our saving to a small power of \log x, because a
typical integer has O(\log x) divisors."

(c) After (b), p. 3 (function class):
"The methods of this paper should generalise to a wider class of
multiplicative functions through appropriate modifications. The complete
multiplicativity of \lambda is only used in Proposition 3.1 and in the proof
that Theorem 2.4 implies Theorem 1.1. The only other property of \lambda we
use is that it is 1-bounded (for Sections 2 and 3), but a weaker \ell^p bound
would suffice."

(d) After (c), p. 3 (averaging type):
"Our proof also yields an improved bound for the unweighted two-point
correlations (i.e. without logarithmic averaging) at almost all scales; see
Remark 2.8."

(e) Sec. 1.2, p. 4 (why single-prime shifts cap the saving; context: the
Helfgott-Radziwill matrix A over shifts by single primes p \in P):
"Using a high trace method, Helfgott and Radziwill [11] managed to obtain the
bound (\sum_{p \in P} 1/p)^{1/2+o(1)} for the largest eigenvalue of such a
matrix, which is essentially the best possible. Since \sum_{p \in P} 1/p \ll
\log\log x, this approach cannot yield a saving better than a power of
\log\log x over the trivial bound for two-point Chowla correlations."

(f) Sec. 1.2, p. 4 (shift size in the underlying reduction; verbatim):
"Using the multiplicativity of \lambda, Tao [22] showed that the problem of
bounding \sum_{n \leq x} \frac{1}{n}\lambda(n)\lambda(n+1) reduces to bounding
  E_{p \in P} \sum_{n \leq x} \lambda(n)\lambda(n+p)
  (1_{p|n} - \frac{1}{p}),
where P \subset [1, \exp(\sqrt{\log x})] is a set of primes."
And for the new approach: "In our new approach, we replace the average over
primes p \in P with an average over integers d = p_1 ... p_k that are products
of k primes, where k \asymp \log\log x." ... "We prove that all eigenvalues of
\widetilde{A}|_X are bounded by (\sum_{d \in D_k} 1/d)^{1/2+o(1)} in absolute
value. Since k \gg \log\log x, we can choose D_k so that
\sum_{d \in D_k} 1/d \gg (\log x)^c, which produces the exponential
improvement in Theorem 1.1."

(g) Remark 3.5, p. 11 (restriction to a dense subset is essential; optimality
of the spectral bound) (verbatim):
"The restriction to a dense subset X \subset I_N is essential. Indeed, the
full matrix A_{\mathbb{Z}} does have very large eigenvalues, which arise from
integers n \in I_N having an unusually large number of prime factors from
\mathcal{P}. For instance, if n \in I_N is such that
\omega_{\mathcal{P}_j}(n) \geq CV for every 1 \leq j \leq J, and v is the
standard basis vector corresponding to n, then
  \| A_{\mathbb{Z}} v \|_2 = ( \sum_m w_{\mathbb{Z}}(m,n)^2 )^{1/2}
  \geq ( \sum_{d \in \mathcal{D}, d|n} \prod_{p|d} (1 - \frac{1}{p})^2 )^{1/2}
  \gg ( \prod_{j=1}^{J} \omega_{\mathcal{P}_j}(n) )^{1/2}
  \gg C^{J/2} V^{J/2}.
Consequently, A_{\mathbb{Z}} possesses an eigenvalue of size at least
\gg C^{J/2} V^{J/2} in absolute value, exceeding the desired bound if C is
too large. This large eigenvalue directly reflects the exceptional
factorisation of n. The previous computation also shows that the eigenvalue
bound in Proposition 3.4 is optimal up to the e^{O(J)} factor."

---

## 7. Interface-level reformulations (spectral core, stated in Sections 3.1-3.2)

Proposition 3.1 (verbatim, Sec. 3.1, p. 10):
"Let N be an integer such that \log N \geq (\log H)^2. Let
  S_1 := \sum_{n \in I_N} \sum_{\substack{d \in \mathcal{D} \\ d | n}}
         \lambda(n)\lambda(n+d)
  and
  S_2 := \sum_{n \in I_N} \sum_{d \in \mathcal{D}} \lambda(n)\lambda(n+d)
         \prod_{p|d} ( 1_{p|n} - \frac{1}{p} ).
Then
  |S_1 - S_2| \ll \frac{N}{(\log H)^{1/2500}}."
Immediately following sentence (verbatim): "Proposition 3.1 is proved in
Appendix C, using the circle method and crucially relying on an estimate of
Matomaki, Radziwill and Tao [15]."

Definition 3.2 (w_Y, A_Y) (verbatim, Sec. 3.2, p. 10):
"For any set Y \subset \mathbb{Z}, let w_Y : I_N \times I_N \to \mathbb{R} be
the function defined by
  w_Y(m,n) := \prod_{p|d} ( 1_{p|n} - \frac{1}{p} )
              if |m - n| = d \in \mathcal{D} and m, n \in Y,
  and 0 otherwise.
Define A_Y to be the real symmetric matrix A_Y := (w_Y(m,n))_{m,n \in I_N}."
[Paper's footnote 2: entries indexed by I_N, not {1,...,N}.]

Proposition 3.4 (Spectral radius of restriction) (verbatim, Sec. 3.2, p. 11):
"Let N be an integer such that \log N \geq (\log H)^{2.001}. Then, there is a
subset X \subset I_N with |I_N \setminus X| \ll e^{-JV/3} N such that all
eigenvalues of (A_{\mathbb{Z}})|_X are bounded in absolute value by
e^{O(J)} V^{J/2}."

Framing sentence (verbatim, Sec. 3.2, p. 10): "To prove our main theorem, we
analyse the spectral properties of a matrix whose entries correspond to the
coefficients \prod_{p|d} (1_{p|n} - \frac{1}{p}) appearing in S_2. This key
step effectively suppresses the role of the Liouville function in the
problem."

Dependency graph (Figure 1, p. 5, transcribed): Theorem 1.1 <= Theorem 2.4;
Theorem 2.4 <= {Proposition 3.1, Proposition 3.4}; Proposition 3.1 <=
[15, Theorem 1.3]; Proposition 3.4 <= {Proposition 4.7, Proposition 4.5
(Ihara-Bass formula)}; Proposition 4.7 <= Proposition 5.3 (high trace bound);
Proposition 5.3 <= {Proposition 9.1, Proposition 10.10, Proposition 12.1}.

---

## 8. COMMENTARY (extractor's observations -- NOT from the paper)

Interface card for the Pilatte engine (inputs -> outputs):
- INPUT function class: a 1-bounded arithmetic function; complete
  multiplicativity consumed ONLY at two boundary points (Tao reduction
  Sec. 2.3 and Prop 3.1 via circle method + MRT [15, Thm 1.3]); the spectral
  core (Prop 3.4) is function-free -- it is a statement about a deterministic
  divisibility matrix, no \lambda involved.
- INPUT shifts: d = p_1...p_J, p_j from prescribed disjoint prime ranges
  \mathcal{P}_j subset (H_0, H), H_0 = exp((log H)^{1-eps_1}); J up to
  eps_1^2 log log H. Shift size d < H <= exp((log N)^{1/2.001}): tiny vs N.
  Shifts always enter WITH the divisibility constraint d | n (or its centred
  weight); no fixed-single-shift estimate is emitted.
- INPUT averaging: full average over all J-tuples of primes, dyadic n-blocks;
  Remark 2.6 upgrades to l^1 over shift tuples (arbitrary signs).
- OUTPUT: square-root-of-trivial saving e^{O(J)}(V_1...V_J)^{1/2}N per dyadic
  block (Thm 2.4/(7)); assembled via complete multiplicativity into
  (log x)^{1-c} for logarithmic two-point Chowla (Thm 1.1) and (log w)^{-c}
  at almost all scales (Remark 2.8).
- Relevance boundary for Erdos 251: the engine bounds correlations
  \lambda(n)\lambda(n+d) averaged over structured shifts d with d | n; it
  emits nothing about individual shifts, nothing about the von Mangoldt /
  prime-indicator class (its \lambda-free core still needs the two
  multiplicativity boundary steps to reach a Chowla-type conclusion), and its
  saving ceiling is a fixed small power of log x (stated limitation (b)).
