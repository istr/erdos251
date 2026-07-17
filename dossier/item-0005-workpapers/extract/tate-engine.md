# item-0005 extraction: Tao-Teravainen arXiv:2512.01739v2
# "Quantitative correlations and prime factors" -- correlation engine (Thm 3.1) and sieve strand (Sec 2)

Source: /home/istr/pro/erdos251/dossier/2512.01739v2.pdf (61 pages, v2).
Method: pdftotext for locating anchors; all load-bearing formulas transcribed
from VISUAL page reads (pages 3-4, 24-26, 46-51, 55 read as rendered images).
Page numbers are secondary aids; primary anchors are theorem/equation/section
numbers.

ASCII transcription conventions (declared up front):
- \sum, \prod, \int, \frac written as LaTeX tokens or plain ASCII.
- "<<" = \ll (big-O), ">>" = \gg, "~=" = \asymp (comparable).
- The paper (Subsection 1.6) uses TWO strengthened order symbols: one meaning
  "X = o(Y)" and one meaning "X << Y^{o(1)}". I write them "<<<" (X = o(Y))
  and "<<<<" (X << Y^{o(1)}). [TRANSCRIPTION-UNSURE: which printed glyph
  (\lll vs doubled \ll\ll) carries which of the two meanings; the DEFINITIONS
  in Subsection 1.6 are unambiguous: "We write X ~= Y for X << Y << X,
  X <<< Y for X = o(Y), and X <<<< Y for X << Y^{o(1)}" (transcribed with my
  symbol assignment).]
- Calligraphic L in Section 3 written \mathcal{L}; the plain L of Section 5
  (number of subintervals, eq. (5.27)) is a DIFFERENT quantity, written L.
- log_2 x = log log x, log_3 x, log_4 x are iterated logs (Subsection 1.6).
- M(g; X, Q) is the pretentious-distance quantity, definition (1.18), p. 10:
  M(g; X, Q) := inf_{|t| <= X; q <= Q; chi (mod q)} D(g, n -> chi(n) n^{it}; X)^2,
  where D(f,g;X) := ( \sum_{p <= X} (1 - Re(f(p) conj(g(p))))/p )^{1/2}
  (definition displayed just before (1.17), p. 9).
  M(g; X) := inf_{|t| <= X} D(g, n -> n^{it}; X)^2 is (1.17).

====================================================================
## 1. THEOREM 3.1 -- VERBATIM STATEMENT AND HYPOTHESIS ANATOMY
====================================================================

### 1.1 Verbatim statement (Theorem 3.1, Section 3, p. 24; transcribed from
### rendered page)

"Theorem 3.1 (A quantitative correlation estimate). Let X >= 2. Suppose that
g_1, g_2 : N -> C are 1-bounded multiplicative functions. Let
1 <= \mathcal{L} <= \log X and \delta_N be real numbers for all
X^{0.4} <= N <= X, obeying one of the following two axioms:

(i) (Equidistributed case) g_1 is real-valued and for all X^{0.4} <= N <= X
and a, q \in N one has the equidistribution bound

(3.1)   \sum_{N < n <= 2N, n \equiv a (mod q)} g_1(n)
          = \frac{N}{q} \delta_N + O(N \mathcal{L}^{-1}).

Furthermore, we assume the technical condition

(3.2)   g_1(p) = 1

whenever \exp(\log^{1/11} X) <= p <= \exp(\log^{1/10} X).

(ii) (Non-pretentious case) One has \delta_N = 0 for all X^{0.4} <= N <= X,
as well as the non-pretentious inequality

(3.3)   \exp(M(g_1; X^2, \log^{1/125} X)) >> \mathcal{L}.

Let c > 0 be a sufficiently small absolute constant. Then, there exists a set
\mathcal{E} \subset [\sqrt{X}, X] satisfying the logarithmic density bound

        \frac{1}{\log X} \int_{\mathcal{E}} \frac{dt}{t} << \mathcal{L}^{-c}

such that for any W \in [\mathcal{L}^c] and integers b, h_1, h_2 =
O(\mathcal{L}^c) with h_1 \neq h_2, we have

(3.4)   \frac{W}{N} \sum_{N < n <= 2N} (g_1(n + h_1) - \delta_N)
               g_2(n + h_2) 1_{n \equiv b (mod W)} << \mathcal{L}^{-c}

for all N \in [\sqrt{X}, X] \setminus \mathcal{E}."

### 1.2 Hypothesis anatomy (clause by clause; interface reading, no
### paraphrase of any hypothesis -- each clause above is quoted verbatim)

- FUNCTION CLASS: "g_1, g_2 : N -> C are 1-bounded multiplicative functions"
  (Thm 3.1 preamble). In case (i) additionally "g_1 is real-valued"; g_2 has
  NO extra hypothesis in either case (only 1-bounded multiplicative). In case
  (ii) g_1 may be complex but must satisfy (3.3) (non-pretentiousness w.r.t.
  twisted characters chi(n) n^{it} with modulus q <= log^{1/125} X and
  |t| <= X^2).
- EQUIDISTRIBUTION QUALITY (case (i)): error O(N \mathcal{L}^{-1}) in (3.1),
  required UNIFORMLY for ALL moduli q \in N and ALL residues a \in N
  (including non-primitive a, see Remarks 3.2 second bullet, quoted below),
  and for ALL scales X^{0.4} <= N <= X.
- TECHNICAL SMALL-PRIME CONDITION (case (i) only): (3.2), g_1(p) = 1 on the
  window \exp(\log^{1/11} X) <= p <= \exp(\log^{1/10} X).
- AVERAGING TYPE: NATURAL (uniform) averaging \frac{1}{N}\sum_{N < n <= 2N}
  in the conclusion (3.4) -- NOT logarithmic; the exceptional set
  \mathcal{E} of scales is measured in LOGARITHMIC density
  (\frac{1}{\log X}\int_{\mathcal{E}} dt/t << \mathcal{L}^{-c}).
- SHIFTS: h_1, h_2 are integers with h_1 != h_2, allowed to be as large as
  O(\mathcal{L}^c); since \mathcal{L} can be taken up to \log X, shifts up to
  a small power of \log X are permitted, UNIFORMLY (the bound (3.4) holds
  "for any W \in [\mathcal{L}^c] and integers b, h_1, h_2 = O(\mathcal{L}^c)").
  The shifts are not fixed: they may grow with X within this range.
- CONGRUENCE UNIFORMITY: conclusion holds restricted to any progression
  n = b (mod W) with W <= \mathcal{L}^c, with the natural normalization W/N.
- ERROR QUALITY of conclusion: << \mathcal{L}^{-c}, i.e. a small power of
  \mathcal{L} (at best a small power of \log X). Valid for all scales
  N \in [\sqrt{X}, X] outside \mathcal{E}.

### 1.3 Remarks 3.2 (pp. 24-25) -- verbatim, all three bullets

Bullet 1 (history + Pilatte attribution + status of (3.2)):
"A qualitative version of this theorem (with o(1) type error terms), using
logarithmic averaging instead of natural averaging outside of an exceptional
set, was established in [50, Theorem 1.3] (in the non-pretentious case) and
[54, Theorem 1.4] (in the equidistributed case). The ability to replace
logarithmic averaging with natural averaging outside of an exceptional set
was first observed (in the non-pretentious case) in [51]. The
\mathcal{L}^{-c} type error terms were first obtained by Pilatte [42] (with
\mathcal{L} = \log X and W = 1) in the model case of the Liouville function
\lambda (which is both equidistributed and non-pretentious), which improved
on [1] and [50]; the arguments here will rely heavily upon those of Pilatte.
The technical condition (3.2) at small primes can most likely be weakened or
even dropped with some additional work, but in any event this condition is
satisfied in our applications, so we retain it for this paper."

Bullet 2 (residue classes; identification of \delta_N):
"Note that in the equidistributed case (i) we permit a to share a common
factor with q; thus it asserts that g_1 is quantitatively equidistributed in
both primitive and non-primitive residue classes of moduli of size
O(\mathcal{L}). As noted in [54, Remark 1.3], this type of definition
includes all sufficiently non-pretentious 1-bounded multiplicative functions.
Note also that by setting q = 1 in (3.1) we have
(3.5)  \delta_N = \frac{1}{N} \sum_{N < n <= 2N} g_1(n) + O(\mathcal{L}^{-1})
       = O(1)."

Bullet 3 (uniform Chowla special case, p. 25):
"It is also worth noting that Theorem 3.1 contains as a special case the
following uniform bound for Chowla-type averages: For some constant c > 0,
for any a_1, a_2, b_1, b_2 \in [1, (\log N)^c] \cap N with
a_1 b_2 \neq a_2 b_1 we have
  \frac{1}{N} \sum_{n <= N} \lambda(a_1 n + b_1) \lambda(a_2 n + b_2)
     << (\log N)^{-c}
for all N \in [2, \infty) \setminus \mathcal{E} with \mathcal{E} satisfying
\frac{1}{\log X} \int_{[1,X] \cap \mathcal{E}} \frac{dt}{t} << (\log X)^{-c}
for all X >= 2. This follows from Theorem 3.1(ii) with W = a_1 a_2 since the
Liouville function \lambda satisfies (3.3) by [39, equation (1.12)] and since
we can write \lambda(a_1 n + b_1)\lambda(a_2 n + b_2) =
\lambda(a_1)\lambda(a_2)\lambda(a_1 a_2 n + a_2 b_1)\lambda(a_1 a_2 n + a_1 b_2)."

### 1.4 Companion statements in Section 3 consumed downstream

- Theorem 3.3 (Pilatte's decoupling inequality), Subsection 3.1, p. 25:
  the key internal tool for Theorem 3.1 (quoted in Part 2 below). Consumed
  INSIDE Section 3 only (at (3.16), via line "Now, (3.14) follows..." p. 31
  region); not directly invoked by Sections 4-5.
- Equation (3.14), Subsection 3.2, p. 29 (stability of mean values):
  "(3.14)  \frac{1}{N} \sum_{N < n <= 2N} g(n)
           - \frac{P}{N} \sum_{N/P < n <= 2N/P} g(n)
           << ( \frac{\log 2P}{\log N} )^{1/4} = otilde(1),"
  stated for real 1-bounded multiplicative g via "[38, (13)] combined with
  telescopic summation" (text before (3.14)); accompanying claim (3.13):
  "\delta_{N/P} = \delta_N + otilde(1)" whenever 1 <= P <= H and
  \sqrt{X} <= N <= X. Here otilde(1) is the Section 3 notation (3.8):
  "Y = otilde(Z) if Y = O(Z \mathcal{L}^{-c'})" for some constant c' > 0
  independent of c.
  CONSUMED BY SECTION 5: p. 55, "By dividing out common factors of a, r (and
  using (3.14)) we may assume without loss of generality that (a, r) = 1
  (after worsening the lower bound on N to say x^{0.3} <= N)."
- Subsection 3.7 "Application to smooth numbers" (pp. 34+) deduces Theorem
  1.8 from Theorem 3.1 -- a Section 3-internal application, not used by
  Section 5.
- Section 5 otherwise consumes ONLY Theorem 3.1 itself, in the
  equidistributed case (i) with \mathcal{L} = \log^c x (see Part 3.4 below).
- Section 4 consumes Theorem 3.1 in the NON-pretentious case: "Hence, (4.9)
  implies the desired bound (4.8) by the non-pretentious case of Theorem 3.1"
  (Subsection 4.1, p. 36 region; pdftotext line anchor).

====================================================================
## 2. WHERE PILATTE ENTERS, AND WHAT TAO-TERAVAINEN ADD
====================================================================

### 2.1 Reference identification

Bibliography entry (p. 61): "[42] C. Pilatte. Improved bounds for the
two-point logarithmic Chowla conjecture. arXiv e-prints, page
arXiv:2310.19357, October 2023."
So arXiv:2310.19357 = reference [42].

### 2.2 Entry points of [42]

(a) Introduction, Subsection 1.3, p. 4: "...but the latter requires a version
of the recent strong quantitative results of Elliott-type due to Pilatte [42]
in order to keep the error terms under control. Indeed, the main result of
[42] gives the Chowla-type bound
  \frac{1}{N} \sum_{n <= N} \lambda(n) \lambda(n+1) << \log^{-c} N
for almost all scales N (where 'almost all' is in the sense of logarithmic
density), where c > 0 is a small absolute constant, improving upon previous
results towards the Chowla conjecture in [1], [51], [52], [50]."

(b) Remarks 3.2 bullet 1 (quoted fully in 1.3 above): "The \mathcal{L}^{-c}
type error terms were first obtained by Pilatte [42] (with \mathcal{L} =
\log X and W = 1) in the model case of the Liouville function \lambda ...;
the arguments here will rely heavily upon those of Pilatte."

(c) Subsection 3.1, p. 25: "A key tool in the proof of Theorem 3.1 will be
Pilatte's decoupling inequality." Verbatim statement (transcribed from
rendered p. 25):

"Theorem 3.3 (Pilatte's decoupling inequality). Let \epsilon_1 > 0 be a
sufficiently small absolute constant. Let H > 0 be sufficiently large in
terms of \epsilon_1. Let J \in [\epsilon_1^2 \log_2 H] and set
H_0 := \exp(\log^{1-\epsilon_1} H) and C := \exp(\epsilon_1 (\log_2 H)/(2J)).
For i \in [J], let \mathcal{P}_i be the set of all primes p with
   C^{2i-2} < \frac{\log p}{\log H_0} < C^{2i-1}
(so in particular H_0 < p < H), and let V >= 2 be such that
(3.6)   \sum_{p \in \mathcal{P}_i} \frac{1}{p} <= V
for all i \in [J]. Then, for integer N >= \exp(\log^{2.01} H), any interval
I of length N, any residue classes b_p (mod p) for each prime p, any
1-bounded functions g_1, g_2 : Z -> C, and any indices
1 <= i_1 < ... < i_{J'} <= J with J' \in [J], one has
  \sum_{(p_1,...,p_{J'}) \in \mathcal{P}_{i_1} \times ... \times \mathcal{P}_{i_{J'}}}
  | \sum_{n \in I} (1_{n \equiv b_{p_1} (mod p_1)} - \frac{1}{p_1}) ...
    (1_{n \equiv b_{p_{J'}} (mod p_{J'})} - \frac{1}{p_{J'}})
    g_1(n) g_2(n + \sigma p_1 ... p_{J'}) |
  << V^{0.51 J'} N
for \sigma \in \{-1, +1\}."

Followed by (p. 25): "As noted in [42, Remark 2.5], the trivial triangle
inequality bound here is basically of the form V^{J'} N, so the point is the
gain of V^{-0.49 J'}."

### 2.3 What Tao-Teravainen say they modify (p. 26, verbatim list)

"In the model case where g_1 = g_2 = \lambda, I = I_N := [N+1, 2N] and
J' = J, this claim is essentially [42, Theorem 2.4] (or more precisely, the
key input S_2 << e^{O(J)} V^{J/2} N in the proof of that theorem in [42, end
of Section 3]), after incorporating [42, Remark 2.6]. Thus, we need to adapt
the arguments so that
 (i) The functions g_1, g_2 are not required to be equal to each other;
 (ii) The functions g_1, g_2 are not required to be equal to the Liouville
      function \lambda;
 (iii) The length N interval I is not required to be equal to I_N; and
 (iv) The number J' of sets \mathcal{P}_{i_k} of primes is not required to
      be J."

How each is handled (pp. 26-27, condensed with verbatim key phrases):
- (ii): "straightforward, as the deduction of the decoupling inequality from
  the key spectral radius bound [42, Proposition 3.4] does not use any
  property of \lambda other than 1-boundedness (as long as g_1, g_2 are
  equal)."
- (iv): "also straightforward to implement, as the only property required of
  the sets \mathcal{P}_i of primes in the proof (besides [42, Lemma 2.3(b)])
  is that they are disjoint subsets of (H_0, H) with
  1 << \sum_{p \in \mathcal{P}_i} 1/p <= V."
- (iii): "the fact that I = I_N is used in precisely two places in [42], both
  involving estimates from [41]" -- both fixed by expanding moments and using
  [41, Lemma (3.10)] ([41] = Norton, "On the number of restricted prime
  factors of an integer. I", Ill. J. Math. 20 (1976)).
- (i): "requires a little more care, as the arguments in [42] rely heavily on
  the fact that a certain adjacency matrix is Hermitian ...; allowing
  g_1 \neq g_2 will break this symmetry. However, this can be addressed by
  the standard technique of 'doubling up' a directed graph to create an
  undirected graph." (p. 27: introduces a double cover
  \tilde{I} := I \times \{-1,+1\}, proves analogues of [42, Proposition 3.4],
  [42, Proposition 4.7] via the Ihara-Bass formula "as in [42, Section 4]",
  reduces to a high trace bound as in [42, Proposition 5.3]; "The crucial
  bound in [42, Lemma 5.4] continues to hold in our setting"; the alternating
  signs of shifts "only serves to improve the bound".)
- Acknowledgements (p. 9): "We thank Cedric Pilatte for helpful discussions
  and suggestions, especially with regards to the modifications to his
  arguments required to establish Theorem 3.1".
- Additionally, Subsection 3.4 (p. 31 region): in the proof of the short
  exponential sum estimate (3.18), "In the non-pretentious case (ii), this
  follows from [39, Theorem 1.7]. The equidistributed case was previously
  considered in [54, Lemma 3.6, Lemma 3.7], but with slightly different
  quantitative conclusions than are needed here." ([39] =
  Matomaki-Radziwill-Tao, An averaged form of Chowla's conjecture.)

====================================================================
## 3. SPLIT OF PRIME SIZES; kappa_1..kappa_5; WHICH TOOL SERVES WHICH RANGE
====================================================================

NOTE ON THE TASK PHRASE "kappa_1, kappa_2, kappa_3 ranges": in the paper the
kappa_j are ERROR TERMS (five of them, kappa_1..kappa_5), not prime ranges.
The prime-size splits are separate. Both are given below with anchors. It IS
correct that Theorem 3.1 serves the very-large-prime range (via kappa_3).

### 3.1 Section 2 split (sieve strand; Section 2, pp. 11-12)

Shift scales (Section 2, after (2.1), p. 11): "K := \frac{1}{C_0} \log_2 x,
K_+ := \log x" for a large constant C_0; shifts divided into
"near shifts 1 <= k <= K; far shifts K < k <= K_+; and very far shifts
k > K_+."
Scale (2.2): R_k := x^{1/100^k} for 1 <= k <= K, and R_k := w for
K < k <= K_+, where (2.3) w := \log^{1/2} x. (2.4): for near shifts,
\log^{0.9} x <= \log R_k <= \log x. (Superscript 100^k confirmed visually on
p. 3: "sieving n + k to mostly avoid being divisible by primes less than
x^{1/100^k}".)
Prime classes for a given near/far shift (p. 11, verbatim bullet list):
 "- tiny primes p <= w.
  - small primes w < p <= k. (This class will be empty if k <= w.)
  - medium primes w < p <= R_k. (This class will be empty if k is a far
    shift.)
  - large primes max(k, R_k) < p <= R_1.
  - very large primes p > R_1."
Role (p. 12): "It will be the medium and large primes which require the most
attention; the very large and tiny primes are easy to handle, and the small
primes, while posing some technical difficulties with regards to
sieve-theoretic estimates, will not make a major contribution to
\omega(n+k)." Figure 1 caption (p. 12): "We perform an exact sieve at tiny
primes and a Selberg type sieve at medium primes, in order to ensure
\omega(n+k) <<_{C_0} k with high probability for all shifts k."
In Section 2 the very large primes p > R_1 contribute O(1) prime factors
trivially (Subsection 2.1: "Omega_{>R_1}(n+k) = O(1)"). Theorem 3.1 is NOT
used in Section 2 at all.

### 3.2 Section 5 split (irrationality strand; Subsection 5.5, pp. 49-51)

Parameters (5.22)-(5.29), p. 49 (visual):
  (5.22) K := floor( 2 \log_4 x / \log 2 )
  (5.23) H := floor( \log_3^2 x )
  (5.24) M := 2 floor( \log_2 x )
  (5.25) H_+ := floor( \log_2^2 x )
  (5.26) P := \exp( \log_3^3 x )
  (5.27) L := \log^{1/\log_3 x} x
  (5.28) R := x^{1/\log_2^2 x}
  (5.29) R_+ := x^{1/100}
Hierarchy (5.30), p. 49 [TRANSCRIPTION-UNSURE on the exact strength-symbol at
each step; ordering itself is certain]:
  1 <<< K <<<< \log_3 x ~= (\log_2 R_+ - \log_2 R) <<< H ~= 2^K
  <<< \log P ~= \log(H_+ K P) <<<< M ~= \log_2 R ~= \log_2 x <<< H_+
  <<<< 2^H <<<< P <<<< P^{2^K} <<<< (HKP)^{2^{2K} H^2} <<< L <<< \log x
  <<<< P^M <<<< 2^{H_+} <<<< R <<<< R^M <<<< R_+ <<< x.

Shift classes (p. 50): "we divide the shifts h >= 1 into three classes:
near shifts 1 <= h <= H; far shifts H < h <= H_+; and very far shifts
h > H_+."

Prime classes (p. 51, verbatim): "Again similarly to Section 2, we divide the
set of primes into four classes:
  - small primes in which p | W or p = p_\epsilon for some
    \epsilon \in \{0,1\}^K;
  - medium primes p <= R not dividing W and not equal to any of the
    p_\epsilon;   [footnote 9: 'The terminology here is not completely
    ordered, as it is possible for medium primes to occasionally be less than
    some of the small primes; but this will not affect the arguments.']
  - large primes R <= p < R_+; and
  - very large primes p > R_+;
and set S_0 to be the set of small primes, S_1 to be the set of medium
primes, and S_2 to be the set of large and very large primes."
Here W is the discriminant (p. 51):
  W := \prod_{\epsilon,\epsilon' \in \{0,1\}^K}
       \prod_{1 <= h, h' <= H, (\epsilon,h) \neq (\epsilon',h')}
       | r_{\epsilon,h+K} - r_{\epsilon',h'+K} |,
  with W <= (O(HKP))^{2^{2K} H^2} << \exp(\log_3^{O(1)} x) <<<< L <<<< x,
and p_\epsilon := p_0 + \epsilon_1 v_1 + ... + \epsilon_K v_K are the 2^K
Hilbert-cube primes in [P/2, P] produced by Lemma 5.2 (p. 50; proof via
Gowers-norm monotonicity, "Hilbert cube lemma").
Shifts r_{\epsilon,h} defined in (5.7), p. 46:
  r_{\epsilon,h} := p_\epsilon h - \sum_{k=1}^K k \epsilon_k v_k
                 = p_0 h + \sum_{k=1}^K (h - k) \epsilon_k v_k,
with trivial bound (5.32): r_{\epsilon,h+K} << (h+K) K P.

### 3.3 The five error terms kappa_1..kappa_5 (all visual, pp. 46-48)

Random variable (5.13), p. 47:
  X_p := q \sum_{1 <= h <= H} \sum_{\epsilon \in \{0,1\}^K}
         (-1)^{|\epsilon|} \frac{1_{p | n + r_{\epsilon,h+K}}}{2^{h+K}}.
(n = random integer, uniform on [x/2, x] subject to congruences (5.5) and
(5.33) n = 0 (mod W^flat); spacing bound (5.34):
Q << P^{2^K} W^flat << \exp(\log_3^{O(1)} x) <<<< L <<<< x.)

  (5.10) kappa_1 := \sum_{\epsilon \in \{0,1\}^K} E \delta_{p_\epsilon}(
           n - \sum_{k=1}^K k \epsilon_k v_k )
         = \sum_{\epsilon \in \{0,1\}^K} \sum_{h=1}^{\infty}
           \frac{P(p_\epsilon^2 | n + r_{\epsilon,h})}{2^h}.
  (5.11) kappa_2 := \sum_{h > H} \frac{ \sum_{\epsilon \in \{0,1\}^K}
           E \omega(n + r_{\epsilon,h+K}) }{2^{h+K}}.
  (5.14) kappa_3 := ( E | \sum_{p \in S_2} X_p |^2 )^{1/2}.
  (5.16) kappa_4 := \sum_{m=0}^{M} \frac{(2\pi)^m}{m!}
           | E ( \sum_{p \in S_1} X_p )^m - E ( \sum_{p \in S_1} X'_p )^m |.
  (5.17) kappa_5 := \frac{ \prod_{p \in S_1} E \exp(2\pi e X_p)
           + \prod_{p \in S_1} E \exp(-2\pi e X_p) }{ e^M }.
(X'_p = jointly independent copies of X_p, Subsection 5.4.)

### 3.4 Theorem 5.1 (Technical reduction) -- verbatim (p. 49, visual)

"Theorem 5.1 (Technical reduction). There exists a sequence of x going to
infinity for which the following statement holds: there exist natural numbers
K, H, M with M even, integers p_0 >= 1 and v_1, ..., v_K with
p_\epsilon := p_0 + \epsilon_1 v_1 + ... + \epsilon_K v_K distinct primes for
all \epsilon \in \{0,1\}^K, a partition of the primes into disjoint sets
S_0, S_1, S_2, and a random natural number n obeying (5.5), (5.6) -- all of
which can depend on x -- such that (recalling (5.7)) the quantities
kappa_1, ..., kappa_5 defined in (5.10), (5.11), (5.14), (5.16), (5.17) obey
(5.18), but the random variables X_p defined in (5.13) are deterministic for
p \in S_0 and also obey the condition
(5.21)   \sum_{p \in S_1} Var X_p >> 1.
Indeed, it is clear that (5.18), (5.20), and (5.21) will contradict each
other for x large enough."
((5.18) is "kappa_1, ..., kappa_5 = o(1)"; (5.20) is
"\sum_{p \in S_1} Var X_p << \sum_{j=1}^5 kappa_j".)

### 3.5 Which tool serves which range (Section 5)

- SMALL primes S_0: congruence (5.33) n = 0 (mod W^flat) makes X_p
  DETERMINISTIC (p. 51: "The congruence condition (5.33) also ensures that
  X_p is deterministic for all small primes p \in S_0"); they are peeled off
  exactly, no analytic tool.
- MEDIUM primes S_1 (p <= R): the CORE set. Tools: exact periodicity of the
  indicators plus the spacing relation (5.35) (E f(n) = mean + O(u ||f||_inf
  / x^{1-o(1)}) for u-periodic f, u coprime to Q), giving (5.37)
  E X_p << 1/x^{1-o(1)}, (5.38) E|X_p|^2 ~= 1/(2^K p), hence Var X_p ~=
  1/(2^K p); Mertens' theorem gives \sum_{p \in S_1} Var X_p >>
  (\log_2 R - \log_2 W)/2^K (Subsections 5.10-5.11, p. 53), establishing
  (5.21). kappa_4, kappa_5 (independence-comparison and moment-tail errors)
  are controlled for medium primes in Subsections 5.9-5.10 by elementary
  moment/exponential-moment computations.
- LARGE primes R <= p < R_+ (inside S_2, i.e. inside kappa_3, subtask
  (5.39)): Subsection 5.13, p. 54 -- elementary: for distinct large primes
  "the product X_p X_{p'} is periodic in n with period p p' <= R_+^2 ...
  and mean zero thanks to the alternating factor (-1)^{|\epsilon|} in
  (5.13)", plus E|X_p|^2 << 1/(2^K p) + R_+/x^{1-o(1)} and Mertens; total
  << R_+^4/x^{1-o(1)} + (\log_2 R_+ - \log_2 R)/2^K = o(1) by (5.30).
  NO correlation machinery needed.
- VERY LARGE primes p > R_+ (inside kappa_3, subtask (5.40)): Subsection
  5.14, pp. 54-56. THIS is where Theorem 3.1 enters. Statement (p. 47):
  "Obtaining an adequate control on kappa_3 will be somewhat delicate,
  particularly for very large primes where the correlation estimate of
  Theorem 3.1 is needed."
  Mechanism (pp. 54-55): reduce (5.40) by Cauchy-Schwarz to the diagonal
  (5.41) (trivial) and the off-diagonal (5.42); partition (R_+, 2x] into L
  subintervals J_l with \log_2 y_l - \log_2 y_{l-1} ~= (\log_2 x)/L; write
  (5.43)  \sum_{R_+ < p < 2x} 1_{p|n}
          = \sum_{l \in [L]} (1 - g_l(n) + O(1_{n \in E_l}))
  "where, for each l \in [L], g_l is the completely multiplicative function
  with g_l(p) := 1_{p \notin J_l} for all primes p, and E_l is the set of
  n \in [x/2, x] \cap N for which there exist two primes
  y_{l-1} < p <= p' <= y_l which both divide n" (p. 55, verbatim); E_l sparse
  by (5.44) (Mertens); \delta_{l,x} := (1/(x/2)) \sum_{x/2 <= n <= x} g_l(n);
  then reduce to
  "E (g_l(n + r_{\epsilon,h+K}) - \delta_{l,x})
     (g_{l'}(n + r_{\epsilon',h+K}) - \delta_{l',x}) << \log^{-c} x
  for some absolute constant c > 0 and all l, l' \in [L]" (p. 55).
  Application sentence (p. 55, verbatim): "Applying Theorem 3.1 (in the
  equidistributed case with \mathcal{L} = \log^c x) with g_1 set to g_l and
  g_2 set to either g_{l'} or 1, and noting that importantly the spacing Q of
  the progression to which n is restricted is << \log^{o(1)} x by (5.34), we
  see that it will suffice (after restricting x to a subsequence) to show
  that
    \sum_{N < n <= 2N, n \equiv a (mod r)} g_l(n)
      = \frac{N}{r} \delta_{l,N} + O(N \log^{-c} x)
  for some absolute constant c > 0 and all x^{0.4} <= N <= x and a, r \in N,
  and similarly for g_{l'}."
  The required equidistribution (3.1) for g_l is then verified UNCONDITIONALLY
  by inclusion-exclusion over at most 101 primes of J_l (p. 56; the primes in
  J_l exceed R_+ = x^{1/100}, so at most 101 of them can divide n <= 2N... --
  displayed sums \sum_{i=0}^{101} (-1)^i \sum_{p_1 < ... < p_i, p_j \in J_l}
  with error O(r/N) terms).
  NOTE: the shifts fed into Theorem 3.1 here are r_{\epsilon,h+K} <<
  (h+K)KP << \exp(\log_3^{O(1)} x) = \log^{o(1)} x (by (5.32), (5.30)) --
  i.e. GROWING shifts, accommodated because Theorem 3.1 allows h_1, h_2 =
  O(\mathcal{L}^c) with \mathcal{L} = \log^c x. The technical condition (3.2)
  holds because g_l(p) = 1 for all p <= R_+ = x^{1/100}, and the window in
  (3.2) lies far below x^{1/100}.
  The exceptional-scale set of Theorem 3.1 is absorbed because Theorem 5.1
  only requires "a sequence of x going to infinity" ("after restricting x to
  a subsequence", p. 55).

====================================================================
## 4. SECTION 2 ANATOMY AT INTERFACE LEVEL (ERDOS-STRAUS STRAND)
====================================================================

### 4.1 What Section 2 proves

Theorem 1.1, stated Subsection 1.2 (p. 3), proved in Section 2 (pp. 11-24).
Verbatim (visual, p. 3):
"Theorem 1.1 (Erdos #248). There exists an absolute constant C > 0 such that
for infinitely many positive integers n, for all positive integers k we have
(1.6)   \omega(n + k) <= \Omega(n + k) <= Ck.
In particular, by (1.5) we have \tau(n + k) <= 2^{Ck} for such n for all
positive integers k."
Context (p. 3): "settles a conjecture of Erdos and Straus [13], [2, Problem
#248], also stated by Erdos and Graham [18, p.61]". Erdos-Graham quote
(p. 3): "We just know too little about sieves to handle such a question
('we' here means not just us but the collective wisdom (?) of our poor
struggling human race)".

### 4.2 Where the Maynard-type sieve enters

- Intro attribution (p. 3): "it turns out that a variant of the Maynard sieve
  [40], which was introduced several decades after that paper, can establish
  this result (via an approach similar to that in [44], [45])."
  [40] = "J. Maynard. Small gaps between primes. Ann. Math. (2),
  181(1):383-413, 2015." (bibliography, p. 61). [44] = Pintz ("Are there
  arbitrarily long arithmetic progressions in the sequence of twin
  primes?"), [45] = Polymath ("Variants of the Selberg sieve, and bounded
  intervals containing many primes", Res. Math. Sci. 1 (2014)).
- Precise entry point, Subsection 2.2 (p. 16, verbatim): "Here we will use a
  variant of the Maynard sieve [40], and more specifically a product of K
  smoothed Selberg sieves of Goldston-Pintz-Yildirim-type, and perform
  calculations similar to those in [44], [45, Proposition 4.2], which
  roughly speaking would correspond to the case in which K was replaced by a
  bounded quantity."
  IMPORTANT INTERFACE FACT: no NUMBERED theorem of Maynard's paper [40] is
  invoked; [40] is cited generically for the sieve variant. The
  theorem-level citation is [45, Proposition 4.2] (Polymath), and only as
  "calculations similar to".
- Sieve weight (Subsection 2.2, p. 16): nu(n) := 1_{[x,2x]}(n) 1_{W | n}
  \prod_{1 <= k <= K} ( \sum_{d \in N_{>w}, d | n+k} \mu(d)
  \tilde{eta}( \log d / \log R_k ) )^2, with W := \prod_{p <= w} p^2 (tiny
  prime multiplier; NOTE: this Section 2 "W" is unrelated to Section 3's
  modulus W or Section 5's discriminant W), and \tilde{eta}(u) :=
  e^{-u} eta(u), eta a Gevrey-class-2 smooth cutoff with Fourier decay
  (2.12) \hat{eta}(t) << \exp(-c |t|^{1/2}). n is drawn with density
  nu(n) / \sum_{n'} nu(n').

### 4.3 Parameter uniformity

- Strategy quote (Subsection 1.2, p. 3, verbatim, visual): "the main
  difficulty is to establish (1.6) in the range k <= \frac{1}{C_0} \log_2 x
  for a large constant C_0. Here we perform a Maynard-type sieve (in fact, a
  product of smooth one-dimensional Selberg sieves) on [x, 2x], sieving
  n + k to mostly avoid being divisible by primes less than x^{1/100^k} for
  1 <= k <= \frac{1}{C_0} \log_2 x. ... The main technical issue is that the
  dimension floor(\frac{1}{C_0} \log_2 x) of the sieve is growing slowly
  with x, in contrast with most other applications of Maynard-type sieves in
  which the sieve dimension is bounded; but the dimension growth turns out to
  be sufficiently slow that a suitably careful computation of main terms and
  error terms still lets one close the argument."
- Absorption device (Section 2, p. 11): "(2.5) Y = otilde(Z) means
  Y = O(Z \log^{-c} x) for some absolute constant c > 0 (with c independent
  of C_0)" and "A key point is that any factor of the form O(1)^K can be
  harmlessly absorbed into a otilde(.) error term if C_0 is large enough.
  Roughly speaking, this will allow us to safely utilize K-dimensional
  sieves in our analysis."
- Interface axioms (pp. 12-13): Section 2 reduces Theorem 1.1 to
  constructing a random n in [x, 2x] with:
  (i) a.s. divisible by p^2 for every tiny prime p <= w;
  (ii) for near/far shifts and 1 <= j <= 4 large primes:
       P(p_1 ... p_j | n + k) ~ 1/(p_1 ... p_j) (up to 1 + otilde(1));
  (iii) for near shifts, 1 <= j <= 2 medium primes:
       P(p_1 ... p_j | n + k) << \prod_i (1/p_i) (\log p_i / \log R_k)^2;
  (iv) prime-power correction axiom with error O(x^{-0.1}) (p. 13).
  Verification: moment method, "we will rely primarily on the second and
  fourth moments" (p. 3): second moment (2.8) for medium primes, fourth
  moment (2.9) for large primes, second moment (2.10) for large primes
  (Subsection 2.1, pp. 13-15).

### 4.4 The remark comparing small-k cases to the prime tuples conjecture

Remark 1.2 (pp. 3-4), final paragraph, verbatim (visual):
"In [15] (see also [2, Problem #413], [14], [18], [29, Problem B8], and OEIS
A005236), it was asked whether there are infinitely many n which were
barriers for \omega in the sense that \omega(n - k) <= k for all
1 <= k <= n. It may be that the methods of this paper can be pushed
(particularly if one is more careful about how bounds depend on the sieve
dimension) to establish[footnote 2] a result of this form for sufficiently
large k; however, to handle small values of k, such as k = 1, 2, it seems
that the problem is of comparable difficulty to the prime tuples conjecture
(or the Sophie Germain conjecture that there are infinitely many primes p
with 2p + 1 also prime), and we make no progress on it here."
Footnote 2 (p. 3): "In fact, after the release of this preprint, bounds of
the form \omega(n +- k) <= \Omega(n +- k) << \log k were established for all
2 <= k <= n, by refining the methods of this paper; see [36]." ([36] =
"C. F. Lau. On the number of prime factors of consecutive integers, 2026.",
bibliography p. 61.)
Also first paragraph of Remark 1.2 (p. 3): the [14]/[2, Problem #679]
variant "appears to be beyond the capability of our methods to show".
Related quantitative remark: Remark 2.1 (p. 24): the set of good n <= x "can
be lower bounded by x \exp(-c \log_2^2 x) for some absolute constant c > 0".

====================================================================
## 5. THE "TOO WEAK" BENCHMARK QUOTES ([3] AND [37])
====================================================================

### 5.1 Identification from bibliography (pp. 59, 61)

"[3] D. Charamaras and F. K. Richter. Asymptotic independence of Omega(n)
and Omega(n + 1) along logarithmic averages. arXiv e-prints, page
arXiv:2412.17583, December 2024."
"[37] A. P. Mangerel. On equal consecutive values of multiplicative
functions. Discrete Anal., 2024:20, 2024. Id/No 12."

### 5.2 The single "too weak" occurrence (Subsection 1.3, p. 4)

Grep of the full text finds exactly ONE occurrence of "too weak". Full
passage with surrounding sentences (verbatim, checked against rendered
p. 4):
"To establish Theorem 1.3, upper bounds on consecutive values
\omega(n+1), \omega(n+2), ..., \omega(n+H) of \omega, such as (1.6), are
insufficient; some control on the distribution of various linear
combinations of such values (e.g., \sum_{h=1}^{H} \omega(n+h)/2^h) is
needed. Furthermore, the contribution of large prime factors (e.g.,
p >= n^{1/100}) is no longer negligible and requires more delicate analysis.
If a sufficiently quantitative form of the prime tuples conjecture is
available, one can obtain quite good control on such values for selected n;
this is the strategy taken in [46]. In the absence of the prime tuples
conjecture, known distributional results such as those in [37], [3] turned
out to be too weak for our purposes. However, after applying some
manipulations of Gowers uniformity norm type to various expressions relating
to (1.7), we were able to arrive at a certain linear combination of
consecutive values of \omega that could be adequately controlled by a
combination of Erdos-Kac-type results, as well as pairwise correlation
estimates for multiplicative functions; but the latter requires a version of
the recent strong quantitative results of Elliott-type due to Pilatte [42]
in order to keep the error terms under control."

### 5.3 What property is "too weak" -- what the paper itself says

The paper does NOT itemize, in that sentence, which specific property of
[37], [3] fails; the deficiency must be read off from the surrounding
sentences (all quoted above) and from the paper's other characterizations of
[3]:
- What is needed (same paragraph): "some control on the distribution of
  various linear combinations of such values (e.g.,
  \sum_{h=1}^{H} \omega(n+h)/2^h)", plus handling of "the contribution of
  large prime factors (e.g., p >= n^{1/100})", which "is no longer
  negligible".
- What [3] provides (Subsection 1.1, p. 3, verbatim): "in the recent work
  [3] it was shown that any bounded observables f(Omega(n)), g(Omega(n+1))
  are asymptotically decoupled if n is drawn from a logarithmically weighted
  distribution rather than from a uniform one. Such recent results are
  powered by progress on (logarithmically averaged) versions of the Elliott
  conjecture [50], [52], [51], [35], [54], [1], [42]."
- What replaced them (Remarks 3.2 bullet 1, quoted in 1.3): the prior
  Elliott-type inputs had "o(1) type error terms" and used "logarithmic
  averaging"; the paper needs \mathcal{L}^{-c} (power-of-log) errors,
  natural averaging outside an exceptional set of scales, and uniformity in
  W and in the shifts h_1, h_2 up to O(\mathcal{L}^c) -- supplied by
  Theorem 3.1 following Pilatte [42].
- Cross-check (Remarks 4.2, second bullet, p. 44): the two-dimensional local
  limit theorem sketched there "would in particular provide an alternative
  proof of the results in [3] (and improve the upper bound result in
  [26, Theoreme 3])" -- i.e., the paper's machinery strictly exceeds [3].
[EXTRACTOR NOTE, not paper text: combining these anchors, "too weak" refers
to (a) qualitative o(1) error decay -- no log-power rate -- and (b)
logarithmic (not natural) averaging, and (c) pairwise-only decoupling of
bounded observables without the shift/congruence uniformity needed for the
linear combinations \sum_h \omega(n+h)/2^h and for large prime factors. The
paper does not single out one of (a)-(c) explicitly.]

### 5.4 Related limitation quote (triple correlations)

Remarks 4.2, third bullet (p. 44, verbatim): "However, to handle three-point
equations such as \omega(n) = \omega(n+1) = \omega(n+2) one would require,
in addition to the previously mentioned extension of the methods to two
dimensions, a version of Theorem 3.1 for triple correlations, which does not
appear to be within current technology. For similar reasons we are currently
unable to remove the exceptional set in Theorem 1.7."

====================================================================
## 6. TRANSFER-RELEVANT OBSERVATIONS (extractor commentary)
====================================================================
[COMMENTARY -- everything in this section is the extractor's analysis, NOT
paper content. Context: Erdos #251 asks whether S = \sum_n p_n / 2^n is
irrational; equivalently (partial summation) one studies the gap series
\sum_n g_n / 2^n, g_n = p_{n+1} - p_n, via the tail
delta_n = \sum_{j>=1} g_{n+j} 2^{-j}, delta_{n+1} = 2 delta_n - g_{n+1}.
Question: which Theorem 3.1 hypotheses would a gap/delta functional satisfy
or violate, clause by clause.]

1. "g_1, g_2 : N -> C are 1-bounded multiplicative functions".
   VIOLATED, and this is the load-bearing violation. The engine's input must
   be multiplicative in the INTEGER argument n. Tao-Teravainen never feed
   \omega itself into Theorem 3.1; they exploit the ADDITIVE decomposition
   \omega(n) = \sum_p 1_{p|n} and the conversion step (5.43), which rewrites
   the very-large-prime part of \omega as \sum_l (1 - g_l(n) + O(1_{n in
   E_l})) with g_l(p) = 1_{p \notin J_l} completely multiplicative,
   1-bounded, real. The gap g_n = p_{n+1} - p_n (indexed by prime count) and
   the tail delta_n have NO known decomposition into local (mod p)
   divisibility data of an integer variable; g_n is neither bounded, nor
   multiplicative, nor a finite combination of bounded multiplicative
   functions in any known way. Without an analogue of (5.43) for gaps, the
   engine has no entry point. This is a structural gap, not an error-term
   gap.

2. "1-bounded". VIOLATED by g_n directly (gaps are unbounded, average
   ~ \log p_n). Tao-Teravainen sidestep unboundedness of \omega the same
   way boundedness enters for them: only indicators 1_{p|n} (bounded) are
   correlated, and the 2^{-h} weights plus alternating sums keep each X_p =
   O(2^{-K}) (5.36). A delta_n-analogue would need bounded local pieces of
   the PRIME INDICATOR (n prime or not), not of divisibility; but 1_P is not
   multiplicative and \Lambda is unbounded and not 1-bounded, so neither fits
   the class. Any transfer would have to route prime-location information
   through some bounded multiplicative proxy; the paper offers no such
   device (its Remark 4.2 bullets show even 2-dim/3-point extensions of the
   EXISTING class are open).

3. Equidistribution hypothesis (3.1) with error O(N \mathcal{L}^{-1}),
   all a, q. SATISFIABLE for divisor-window functions (the paper verifies it
   for g_l unconditionally by inclusion-exclusion over <= 101 large primes,
   p. 56). For any prime-indicator-flavored functional the analogous input
   would be equidistribution of PRIMES in APs uniformly to modulus
   ~ \mathcal{L} with log-power error -- available (Siegel-Walfisz) for
   fixed log-power moduli, BUT the class obstacle in (1) precedes this: the
   engine cannot accept the prime indicator at all. Note (3.1) is required
   for ALL q, including q ~ \mathcal{L}; for the delta_n recursion one would
   rather need control of g_n along the PRIME index n, a quantity with no
   modulus structure.

4. Technical condition (3.2), g_1(p) = 1 for exp(log^{1/11} X) <= p <=
   exp(log^{1/10} X). SATISFIED trivially by window functions supported on
   primes > x^{1/100} (as in Section 5); any functional carrying information
   at primes of size exp(log^{1/10-ish} X) violates it, but Remarks 3.2 says
   it "can most likely be weakened or even dropped with some additional
   work". Not the binding constraint.

5. Non-pretentious case (ii) (\delta_N = 0, (3.3)). Serves twisted
   observables e(alpha \omega(n))-type (Section 4, non-pretentious use at
   (4.8)-(4.9)). A gap/delta functional supplies no multiplicative twist to
   which (3.3) could apply. Irrelevant unless a multiplicative encoding of
   gaps is found first.

6. Shift range h_1, h_2 = O(\mathcal{L}^c), h_1 != h_2. FAVORABLE for
   transfer in one respect: Section 5 already uses GROWING shifts
   r_{\epsilon,h+K} << exp(log_3^{O(1)} x) = log^{o(1)} x -- comparable to
   the average prime gap scale ~ log x is NOT reached, but within a factor.
   For a gap functional one would want correlations at shifts up to ~ log x
   (average gap) or beyond; \mathcal{L}^c with \mathcal{L} = \log X caps
   shifts at \log^{c} X with c SMALL (unspecified absolute constant), i.e.
   strictly below the average gap scale. If a transfer needed shifts of size
   exactly ~ log x, the uniformity in Theorem 3.1 as stated is (slightly)
   too narrow; this would be a quantitative, not structural, obstruction.

7. Averaging type and error quality. The conclusion is a natural average
   over N < n <= 2N with log-power error, valid off a log-density-small set
   of scales. For irrationality-by-contradiction one needs only infinitely
   many good n / good x (Theorem 5.1: "There exists a sequence of x going to
   infinity"); the exceptional-scale format transfers cleanly to delta_n
   arguments that need only infinitely many n. The log-power error is enough
   in Section 5 ONLY because the target statement was reduced (via the
   alternating-cube trick, Subsection 5.2, and the variance framework
   (5.18)/(5.20)/(5.21)) to o(1)-variance statements over ~ 2^K = log-ish
   many terms with 2^{-K} normalization. delta_n itself demands exponential
   precision (delta_n is a 2-adic-type tail); no log-power estimate can see
   it directly. Any transfer must first reproduce the reduction that
   replaces exponential precision by a bounded-variance contradiction
   (Section 5's kappa framework), i.e. find an analogue of the congruence
   identity (5.1)+(5.5) and the alternating sum (5.8) for gaps. The
   engine-facing residue of that reduction is exactly the off-diagonal
   second moment (5.42) -- THAT is the shape a gap-transfer would need to
   reach: E (F(n + r) - mean)(F'(n + r') - mean') << log^{-c} x for
   1-bounded multiplicative F, F' and distinct log^{o(1)}-size shifts.

8. Congruence uniformity W <= \mathcal{L}^c. SATISFIABLE: Section 5 needed
   Q << log^{o(1)} x (5.34) and Theorem 3.1 grants moduli up to
   \mathcal{L}^c = log^{c^2} x. A delta-approach pinning small-prime data of
   n via congruences of similarly modest modulus fits; anything requiring
   moduli of polynomial size in x is far outside the engine.

9. Summary verdict (extractor): the correlation engine's hypotheses are
   calibrated to inputs of the form "completely multiplicative 1-bounded
   window functions of an integer variable", produced from ADDITIVE prime-
   factor counts by (5.43). The gap/delta functional of Erdos #251 fails
   the function-class clauses (1)-(2) at the decomposition step, before any
   error-term or uniformity clause is tested; the uniformity clauses (3),
   (6), (7), (8) would be adequate or nearly adequate if (and only if) a
   bounded-multiplicative encoding of prime-gap information existed. The
   paper's own boundary markers point the same way: the 3-point limitation
   (Remarks 4.2, "does not appear to be within current technology") and the
   barrier Remark 1.2 ("comparable difficulty to the prime tuples
   conjecture" for small k) both flag that prime-LOCATION (as opposed to
   prime-FACTOR-count) statistics are outside the engine's reach.

[END COMMENTARY]

====================================================================
## APPENDIX: ANCHOR -> PAGE MAP (secondary aid; pages of the PDF file)
====================================================================
Theorem 1.1: p. 3. Remark 1.2 + footnote 2: p. 3. Theorem 1.3: p. 4.
"too weak" passage: p. 4. Pretentious distance (1.17)-(1.18): pp. 9-10.
Section 2 shift/prime classes, (2.2)-(2.6): p. 11; Figure 1: p. 12;
axioms (i)-(iv): pp. 12-13; Subsection 2.2 sieve construction: p. 16;
Remark 2.1: p. 24. Theorem 3.1: p. 24. Remarks 3.2: pp. 24-25.
Theorem 3.3: p. 25. Adaptation items (i)-(iv): p. 26; double cover: p. 27.
(3.8): p. 27. (3.13)-(3.14): p. 29. Subsection 3.4 ([39, Thm 1.7]): p. 31.
Subsection 3.7 (Thm 1.8 deduction): p. 34. Non-pretentious use of Thm 3.1
in Section 4 (after (4.9)): p. 36. Remarks 4.2 (incl. triple correlation
limitation): p. 44. Section 5 start: p. 44. (5.7)-(5.12),
kappa_1, kappa_2: p. 46. (5.13)-(5.15), kappa_3: p. 47. kappa_4, kappa_5,
(5.16)-(5.19): p. 48. Theorem 5.1, parameters (5.22)-(5.30): p. 49.
Lemma 5.2, shift classes: p. 50. Prime classes, W, (5.33)-(5.36): p. 51.
Subsection 5.13 (large primes): p. 54. Subsection 5.14 + Theorem 3.1
application + g_l definition: pp. 54-55; equidistribution verification for
g_l: p. 56. Bibliography: [3] p. 59; [36]-[46] p. 61; [50]-[54] p. 61.
