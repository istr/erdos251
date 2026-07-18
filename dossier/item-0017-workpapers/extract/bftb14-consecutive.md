# EXTRACTION: Banks, Freiberg, Turnage-Butterbaugh, "Consecutive Primes in Tuples"

Source (only evidence base): /home/istr/pro/erdos251/dossier/1311.7003v3.pdf
arXiv:1311.7003v3 [math.NT] 19 Oct 2014. Authors as printed: WILLIAM D.
BANKS, TRISTAN FREIBERG, AND CAROLINE L. TURNAGE-BUTTERBAUGH. 6 pages
(pp. 1-5 text + references, p. 6 addresses; University of Missouri x2,
University of Mississippi). Footnote p. 1: "Date: October 21, 2014. CLT-B is
supported by a GAANN fellowship (grant no. P200A90092)."
[TRANSCRIPTION-UNSURE: grant number small print]

Transcription conventions: ASCII only. Diacritics transliterated (Erdos,
Turan, Granville unaffected). Math in LaTeX-like ASCII: calligraphic
\mathcal{H}, \mathcal{A}, \mathcal{B}, \mathcal{S} rendered H, A, B, S;
\delta_j for the gap symbols; <= , >= for inequalities; \equiv / \not\equiv
for congruences; | for "divides"; \prod, \sum; "in" for set membership;
"subseteq" for inclusion; \nu_j for the subset-index symbols; e^{...} for
exponentials; {x + b_j}_{j=1}^k for tuple notation. Anchors are
theorem/corollary/equation/section numbers as printed ((1)-(5) are the
paper's only numbered displays); page numbers (printed = PDF page) are
secondary aid.

Everything up to the final section is EXTRACTION (what the paper says).
Commentary appears ONLY in the final marked section.

---

## 1. ABSTRACT (verbatim)

Abstract (p. 1), verbatim:

> "In a stunning new advance towards the Prime k-tuple Conjecture, Maynard
> and Tao have shown that if k is sufficiently large in terms of m, then for
> an admissible k-tuple H(x) = {gx + h_j}_{j=1}^k of linear forms in Z[x],
> the set H(n) = {gn + h_j}_{j=1}^k contains at least m primes for
> infinitely many n in N. In this note, we deduce that H(n) =
> {gn + h_j}_{j=1}^k contains at least m consecutive primes for infinitely
> many n in N. We answer an old question of Erdos and Turan by producing
> strings of m + 1 consecutive primes whose successive gaps
> delta_1, ..., delta_m form an increasing (resp. decreasing) sequence. We
> also show that such strings exist with delta_{j-1} | delta_j for
> 2 <= j <= m. For any coprime integers a and D we find arbitrarily long
> strings of consecutive primes with bounded gaps in the congruence class
> a mod D."

---

## 2. SETUP AND THE ENGINE THEOREM (Section 1, verbatim)

Admissibility definition (Section 1, p. 1), verbatim:

> "We say that a k-tuple of linear forms in Z[x], denoted by
>   H(x) = {g_j x + h_j}_{j=1}^k,
> is admissible if the associated polynomial f_H(x) =
> \prod_{1<=j<=k}(g_j x + h_j) has no fixed prime divisor, that is, if the
> inequality
>   #{n mod p : f_H(n) \equiv 0 mod p} < p
> holds for every prime number p. In this note we consider only k-tuples for
> which
>   g_1, ..., g_k > 0  and  \prod_{1<=i<j<=k} (g_i h_j - g_j h_i) != 0. (1)"

Context sentence (p. 1), verbatim: "One form of the Prime k-tuple Conjecture
asserts that if H(x) is admissible and satisfies (1), then H(n) =
{g_j n + h_j}_{j=1}^k is a k-tuple of primes for infinitely many n in N.
Recently, Maynard [5] and Tao have made great strides towards proving this
form of the Prime k-tuple Conjecture, which rests among the greatest
unsolved problems in number theory. The following formulation of their
remarkable theorem has been given by Granville [3, Theorem 6.2]."

THE ENGINE THEOREM (unnumbered "Theorem (Maynard-Tao)", Section 1, p. 1),
verbatim:

> "Theorem (Maynard-Tao). For any m in N with m >= 2 there is a number k_m,
> depending only on m, such that the following holds for every integer
> k >= k_m. If {g_j x + h_j}_{j=1}^k is admissible and satisfies (1), then
> {g_j n + h_j}_{j=1}^k contains m primes for infinitely many n in N. In
> fact, one can take k_m to be any number such that k_m log k_m > e^{8m+4}."

Constants ladder (Section 1, pp. 1-2), verbatim:

> "Zhang [10, Theorem 1] was the first to prove that
> liminf_{n->infty}(p_{n+1} - p_n) is bounded; he showed that for an
> admissible k-tuple H(x) = {x + b_j}_{j=1}^k there exist infinitely many
> integers n such that H(n) contains at least two primes, provided that
> k >= 3.5 x 10^6. Zhang's proof was subsequently refined in a polymath
> project [7, Theorem 2.3] to the point where one could take k_2 = 632 (at
> least in the case of monic linear forms). Maynard [5, Propositions 4.2,
> 4.3] has shown that one can take k_2 = 105 and k_m = cm^2 e^{4m} in the
> Maynard-Tao theorem, where c is an absolute (and effective) constant.
> Another polymath project [8, Theorem 3.2] has since refined Maynard's work
> so that one can take k_2 = 50 and k_m = ce^{(4-28/157)m}. (In [5,8], only
> tuples of monic linear forms are treated explicitly, although the results
> should extend to general linear forms as considered in [3].)"

[TRANSCRIPTION-UNSURE: the exponent "(4-28/157)m" in k_m = ce^{(4-28/157)m}
is small print; the digits 28/157 are as read from the rendered page.]

Attribution sentence (p. 2), verbatim: "We are grateful to Granville for
pointing out to us that Corollary 1 (below) can now be proved."

---

## 3. MAIN THEOREM AND COROLLARIES (verbatim)

Lead-in (p. 2), verbatim: "The following theorem establishes the existence
of m-tuples that infinitely often represent strings of consecutive prime
numbers."

> "Theorem 1. Let m, k in N with m >= 2 and k >= k_m, where k_m is as in the
> Maynard-Tao theorem. Let b_1, ..., b_k be distinct integers such that
> {x + b_j}_{j=1}^k is admissible, and let g be any positive integer coprime
> with b_1 ... b_k. Then, for some subset {h_1, ..., h_m} subseteq
> {b_1, ..., b_k}, there are infinitely many n in N such that
> gn + h_1, ..., gn + h_m are consecutive primes."

Prior-work note (p. 2), verbatim: "A special case of Theorem 1, with m = 2,
g = 1 (and the weaker bound k_2 >= 3.5 x 10^6), has already been established
in recent work of Pintz [6, Main Theorem], which is based on Zhang's method
but uses a different argument to the one presented here."

Gap-run definition (p. 2), verbatim: "let us call a sequence
(delta_j)_{j=1}^m of positive integers a run of consecutive prime gaps if
  delta_j = d_{r+j} = p_{r+j+1} - p_{r+j}   (1 <= j <= m)
for some natural number r, where p_n denotes the n-th smallest prime. The
following corollary of Theorem 1 answers an old question of Erdos and Turan
[1] (see also Erdos [2] and Guy [4, A11])."

> "Corollary 1. For every m >= 2 there are infinitely many runs
> (delta_j)_{j=1}^m of consecutive prime gaps with delta_1 < ... < delta_m,
> and infinitely many runs with delta_1 > ... > delta_m."

Strengthening (p. 2), verbatim:

> "Moreover, in the proof (see Section 2) we construct infinitely many runs
> (delta_j)_{j=1}^m of consecutive prime gaps with
>   delta_1 + ... + delta_{j-1} < delta_j   (2 <= j <= m),
> and infinitely many runs with
>   delta_j > delta_{j+1} + ... + delta_m   (1 <= j <= m - 1)."

Divisibility variant lead-in (p. 3), verbatim: "Using a similar argument, we
can impose a divisibility requirement amongst gaps between consecutive
primes as well."

> "Corollary 2. For every m >= 2 there are infinitely many runs
> (delta_j)_{j=1}^m of consecutive prime gaps such that
> delta_{j-1} | delta_j for 2 <= j <= m, and infinitely many runs such that
> delta_{j+1} | delta_j for 1 <= j <= m - 1."

Strengthening (p. 3), verbatim: "In the proof (see Section 2) we construct
infinitely many runs (delta_j)_{j=1}^m of consecutive prime gaps with
delta_1 ... delta_{j-1} | delta_j for 2 <= j <= m, and infinitely many runs
with delta_m delta_{m-1} ... delta_{j+1} | delta_j for 1 <= j <= m - 1."

Residue-class lead-in (p. 3), verbatim: "As another application of
Theorem 1, in Section 2 we prove the following extension of a result of
Shiu [9] on consecutive primes in a given congruence class."

> "Corollary 3. Let a and D >= 3 be coprime integers. For every m >= 2,
> there are infinitely many r in N such that p_{r+1} \equiv p_{r+2} \equiv
> ... \equiv p_{r+m} \equiv a mod D and p_{r+m} - p_{r+1} <= DC_m, where
> C_m is a constant depending only on m."

Shiu context (p. 3), verbatim: "Shiu [9] attributes to Chowla the
conjecture that there are infinitely many pairs of consecutive primes p_r
and p_{r+1} with p_r \equiv p_{r+1} \equiv a mod D (see also [4, A4]), and
proved the above result without the constraint p_{r+m} - p_{r+1} <= DC_m."

[These five statements -- Theorem (Maynard-Tao), Theorem 1, Corollaries
1-3 -- are ALL the theorem-like statements in the paper. There are no
lemmas or propositions; Section 2 "Proofs" contains only the four proofs.]

---

## 4. THE CONSECUTIVIZATION MECHANISM (Proof of Theorem 1, Section 2,
pp. 3-4, essentially complete verbatim)

Step 1 - normalization (p. 3), verbatim: "Replacing each b_j with b_j + gN
for a suitable integer N, we can assume without loss of generality that
  1 < b_1 < ... < b_k."

Step 2 - the trap primes (p. 3), verbatim:

> "Let S be the set of integers t such that 1 <= t <= b_k,
> t not in {b_1, ..., b_k}. Let {q_t : t in S} be distinct primes coprime to
> g such that t \not\equiv b_j mod q_t for all t in S, 1 <= j <= k. By the
> Chinese remainder theorem we can find an integer a such that
>   ga + t \equiv 0 mod q_t   (t in S),   (2)
> and therefore
>   ga + b_j \not\equiv 0 mod q_t   (t in S, 1 <= j <= k).   (3)"

Step 3 - the shifted tuple (p. 3), verbatim:

> "Consider the k-tuple
>   A(x) = {gQx + ga + b_j}_{j=1}^k   where   Q = \prod_{t in S} q_t.
> In view of (3) and the fact that gcd(g, b_1 ... b_k) = 1, we have
> gcd(gQ, ga + b_j) = 1 for each j, and since {x + b_j}_{j=1}^k is
> admissible, it follows that the k-tuple A(x) is also admissible. Moreover,
> A(x) satisfies (1) (with g_j = gQ and h_j = ga + b_j) as the integers
> b_1, ..., b_k are distinct and gQ >= 1."

Step 4 - THE INTERVAL TRAP (pp. 3-4), verbatim:

> "For every N in N, the congruences (2) and our choices of Q and a imply
> that
>   g(QN + a) + t \equiv 0 mod q_t   (t in S).
> Consequently, any prime number in the interval
> [g(QN + a) + b_1, g(QN + a) + b_k] must lie in A(n). Let m' be the largest
> integer for which there exists a subset {h_1, ..., h_{m'}} subseteq
> {b_1, ..., b_k} with the property that the numbers
>   g(QN + a) + h_i   (1 <= i <= m')   (4)
> are simultaneously prime for infinitely many N in N. Since k >= k_m we can
> apply the Maynard-Tao theorem with A(x) to deduce that m' >= m."

[TRANSCRIPTION-UNSURE: "must lie in A(n)" -- the argument variable glyph;
the surrounding quantifier is "For every N in N", so A(N) may be intended;
transcribed as printed.]

Step 5 - maximality forces consecutiveness (p. 4), verbatim:

> "By the maximal property of m', it must be the case that for all
> sufficiently large N in N, if the numbers in (4) are all prime, then
> g(QN + a) + b_j is composite for every b_j in
> {b_1, ..., b_k}\{h_1, ..., h_{m'}}. Hence, for infinitely many N in N, the
> interval [g(QN + a) + b_1, g(QN + a) + b_k] contains precisely m' primes,
> namely, the numbers {gn + h_i}_{i=1}^{m'} with n = QN + a."

[End of proof of Theorem 1. PARAPHRASE of the mechanism in one sentence:
every integer position t in the window [1, b_k] that is NOT a tuple offset
is pre-killed by a dedicated fixed prime q_t (via the single arithmetic
progression n = QN + a mod Q), so the only prime candidates in the interval
of length b_k - b_1 are the tuple values themselves; the Maynard-Tao engine
guarantees m of them are simultaneously prime infinitely often, and the
extremal choice of m' converts "at least m primes among the tuple" into
"precisely m' >= m primes in the interval", i.e. consecutive primes.
NOTE (extraction of an absence): the proof yields ONE FIXED subset
{h_1, ..., h_{m'}} that recurs for infinitely many N -- the final sentence
names a single subset for the whole infinite family of sites. No count,
density, or localization of the infinitely many N is stated anywhere.]

---

## 5. GAP-WORD CONSTRUCTIONS (Proofs of Corollaries 1-2, Section 2,
pp. 4-5, verbatim)

Proof of Corollary 1 (p. 4), verbatim:

> "Let m >= 2, and let k >= k_{m+1}. Let A(x) = {x + 2^j}_{j=1}^k, which is
> easily seen to be admissible. By Theorem 1, there exists an (m+1)-tuple
>   B(x) = {x + 2^{\nu_j}}_{j=1}^{m+1} subseteq A(x)
> such that B(n) is an (m + 1)-tuple of consecutive primes for infinitely
> many n. Here, 1 <= \nu_1 < ... < \nu_{m+1} <= k. For such n, writing
>   B(n) = {n + 2^{\nu_j}}_{j=1}^{m+1} = {p_{r+1}, ..., p_{r+m+1}}
> with some integer r, we have
>   delta_j = d_{r+j} = p_{r+j+1} - p_{r+j} = 2^{\nu_{j+1}} - 2^{\nu_j}
>     (1 <= j <= m).
> Then
>   \sum_{i=1}^{j-1} delta_i = \sum_{i=1}^{j-1} (2^{\nu_{i+1}} - 2^{\nu_i})
>     = 2^{\nu_j} - 2^{\nu_1} < 2^{\nu_{j+1}} - 2^{\nu_j} = delta_j
>     (2 <= j <= m).
> Hence, delta_{j-1} <= delta_1 + ... + delta_{j-1} < delta_j for each j,
> which proves the first statement. To obtain runs of consecutive prime gaps
> with delta_j > delta_{j+1} + ... + delta_m >= delta_{j+1}, consider
> instead the admissible k-tuple {x - 2^j}_{j=1}^k. This completes the
> proof."

Proof of Corollary 2 (pp. 4-5), verbatim:

> "Let m >= 2, and let k >= k_{m+1}. Put Q = \prod_{p<=k} p, and define the
> sequence b_1, ..., b_k inductively as follows. Let
>   b_1 = 0,  b_2 = Q,  b_3 = 2Q,
> and for any j >= 3 let
>   b_j = b_{j-1} + \prod_{1<=s<t<=j-1} (b_t - b_s).
> Note that
>   (b_{u+1} - b_u) | (b_{v+1} - b_v)   (v >= u >= 1).   (5)
> Now put A(x) = {x + b_j}_{j=1}^k, and observe that A(x) is admissible
> since Q divides each integer b_j. By Theorem 1, there exists an
> (m + 1)-tuple
>   B(x) = {x + b_{\nu_j}}_{j=1}^{m+1} subseteq A(x)
> such that B(n) is an (m + 1)-tuple of consecutive primes for infinitely
> many n. Here, 1 <= \nu_1 < ... < \nu_{m+1} <= k. For any such n, writing
>   B(n) = {n + b_{\nu_j}}_{j=1}^{m+1} = {p_{r+1}, ..., p_{r+m+1}}
> with some integer r, we have
>   delta_j = d_{r+j} = p_{r+j+1} - p_{r+j} = b_{\nu_{j+1}} - b_{\nu_j}
>     (1 <= j <= m).
> Then
>   \prod_{i=1}^{j-1} delta_i
>     = \prod_{i=1}^{j-1} (b_{\nu_{i+1}} - b_{\nu_i})
>     | \prod_{1<=s<t<=\nu_j} (b_t - b_s) = b_{\nu_j + 1} - b_{\nu_j}
> if 2 <= j <= m. On the other hand, using (5) we see that
>   (b_{\nu_j + 1} - b_{\nu_j})
>     | \sum_{i=\nu_j}^{\nu_{j+1} - 1} (b_{i+1} - b_i)
>     = b_{\nu_{j+1}} - b_{\nu_j} = delta_j.
> Hence, delta_1 ... delta_{j-1} | delta_j for 2 <= j <= m, which proves the
> first statement. To obtain runs of consecutive prime gaps with
> delta_m delta_{m-1} ... delta_{j+1} | delta_j for 1 <= j <= m - 1,
> consider instead the admissible k-tuple {x - b_j}_{j=1}^k. The corollary
> is proved."

[Index-notation note: b_{\nu_j + 1} means the b-sequence element at index
\nu_j + 1 (successor index), distinct from b_{\nu_{j+1}} (the next chosen
index). The recursion "for any j >= 3" is consistent with the given
b_3 = 2Q: j = 3 gives b_3 = b_2 + (b_2 - b_1) = 2Q.
[TRANSCRIPTION-UNSURE: "j >= 3" vs "j >= 4" in the recursion quantifier;
either reading yields the same sequence.]]

---

## 6. THE CONSTANT-RESIDUE-CLASS PATTERN (Proof of Corollary 3, Section 2,
p. 5, verbatim; plus Acknowledgements)

Proof of Corollary 3 (p. 5), verbatim:

> "Let m >= 2, and let k >= k_m. Let {x + a_j}_{j=1}^k be any admissible
> k-tuple with a_1 < ... < a_k, and put b_j = Da_j + a for 1 <= j <= k; then
> {x + b_j}_{j=1}^k is also admissible. Since gcd(D, b_j) = gcd(D, a) = 1
> for each j, we can apply Theorem 1 with g = D to conclude that there is a
> subset {h_1, ..., h_m} subseteq {b_1, ..., b_k} such that
> Dn + h_1, ..., Dn + h_m are consecutive primes for infinitely many n in N;
> as such primes lie in the arithmetic progression a mod D and are contained
> in an interval of length b_k - b_1 = D(a_k - a_1), the corollary follows."

Acknowledgements (p. 5), verbatim:

> "In the first draft of this manuscript, we proved Theorem 1 under the
> assumption that k >= exp(e^{12m}). We thank Andrew Granville for showing
> that k need not be larger than the number k_m in the Maynard-Tao theorem
> and for simplifying our original proof of Theorem 1. We also thank Gergely
> Harcos, James Maynard, and the referee for providing helpful comments on
> our earlier drafts."

References (p. 5), abbreviated transcription (paraphrase of bibliographic
data): [1] Erdos-Turan, "On some new questions on the distribution of prime
numbers", BAMS 54:371-378, 1948. [2] Erdos, "On the difference of
consecutive primes", BAMS 54:885-889, 1948. [3] Granville, "Primes in
intervals of bounded length", BAMS, to appear. [4] Guy, Unsolved problems
in number theory, 3rd ed., 2004. [5] Maynard, "Small gaps between primes",
Ann. of Math. (2), to appear. [6] Pintz, "Polignac numbers, conjectures of
Erdos on gaps between primes arithmetic progressions in primes, and the
bounded gap conjecture", arXiv:1305.6289, 14pp., 2013. [7] Polymath, "New
equidistribution estimates of Zhang type, and bounded gaps between primes",
arXiv:1402.0811, 165pp., 2014. [8] Polymath, "Variants of the Selberg
sieve, and bounded intervals containing many primes", arXiv:1407.4897,
79pp., 2014. [9] Shiu, "Strings of congruent primes", J. London Math. Soc.
(2) 61(2):359-373, 2000. [10] Zhang, "Bounded gaps between primes", Ann. of
Math. (2), 179(3):1121-1174, 2014.

---

## 7. EXPLICIT ABSENCES (searched for, NOT FOUND)

Checked against the full 6-page text (all pages read visually):

1. Site counts / densities: NO count of the sites n (or N, or r) below a
   threshold x appears anywhere. Every existence statement in the paper is
   of the form "for infinitely many n in N" (Theorem 1, Corollaries 1-3,
   Maynard-Tao theorem as quoted). There is no density function, no
   lower-bound counting function, no "positive proportion", no
   x-uniformity in any statement.
2. Shiu-type density costs: NOT FOUND in this text. No expression of the
   shape (2q)^{-exp(Cm)} or any other quantitative site density occurs.
   Shiu [9] is cited only qualitatively (p. 3, quoted above in Part 3): his
   result is stated to lack the diameter constraint, and no density from
   [9] is reproduced.
3. Modulus growth in Corollary 3: NOT ADDRESSED. D is a fixed integer
   coprime to a with D >= 3; no statement allows D to grow with any other
   parameter, and no uniformity in D is claimed.
4. Growth of m with x: NOT ADDRESSED. m is fixed throughout; the engine
   theorem is invoked for fixed m and fixed tuple only.
5. Erdos #251 material (sum p_n/2^n, irrationality, binary digits,
   weighted gap sums): NOT FOUND in this text. The paper's Erdos references
   are the Erdos-Turan monotone-gap-run question [1], [2], and Guy [4, A11],
   [4, A4] only.
6. The only quantitative constants in the entire paper are: k_m log k_m >
   e^{8m+4}; k >= 3.5 x 10^6; k_2 = 632; k_2 = 105; k_m = cm^2 e^{4m};
   k_2 = 50; k_m = ce^{(4-28/157)m}; k >= exp(e^{12m}) (superseded first
   draft); the diameter bounds p_{r+m} - p_{r+1} <= DC_m and
   b_k - b_1 = D(a_k - a_1); and the trap data Q = \prod_{t in S} q_t,
   interval length b_k - b_1 (all quoted verbatim above).

---

## COMMENTARY (assessment, NOT extraction)

Assessment of what this machinery can and cannot supply toward the
project's target: an UNCONDITIONAL supply of two prime-gap-word sites with
matched J-prefix and K-suffix windows and a dominant weighted middle
difference, at depths J, K ~ log2 log x.

1. What the consecutivization trap actually is (Part 4, eqs. (2)-(4)). For
   each non-tuple offset t in the window [1, b_k], a dedicated fixed prime
   q_t kills g n + t along the single arithmetic progression n = QN + a
   (mod Q = \prod q_t). So inside [gn + b_1, gn + b_k] the prime positions
   are a SUBSET of the designed offsets, and Maynard-Tao makes >= m of them
   prime infinitely often. Consecutiveness costs no density input at all --
   it is pure congruence engineering plus the maximality trick for m'
   (Part 4, Step 5). In particular the Shiu-string circularity (blocker
   iii) is neither used nor relieved: this paper carries NO site densities
   whatsoever (Part 7, items 1-2).

2. The single most transferable structural fact: the proof of Theorem 1
   delivers ONE FIXED subset {h_1, ..., h_{m'}} such that for infinitely
   many N the trapped interval contains PRECISELY the primes
   {gn + h_i}_{i=1}^{m'} (Part 4, Step 5, verbatim). Hence unconditionally:
   infinitely many sites whose ENTIRE interior gap word is the SAME fixed
   word (h_2 - h_1, ..., h_{m'} - h_{m'-1}). Two sites with identical
   interior words -- the matched-window half of an exchange configuration
   -- come for free, and not by pigeonhole (so blocker (i), pigeonhole
   blindness to variability, is bypassed for the interior word). The two
   fatal shortfalls for the exchange target: (a) the matched words are
   identical THROUGHOUT the trap, so the needed dominant middle DIFFERENCE
   cannot live inside the trapped interval; it would have to come from the
   boundary gaps (prime preceding gn + b_1, prime following gn + b_k),
   which the method leaves completely uncontrolled; (b) zero counting: the
   sites are "infinitely many N" in one AP (Part 7, item 1), with no
   density to feed a weighted-sum or pigeonhole-over-scales argument.

3. Parity status (blocker ii). The mechanism never prescribes WHICH subset
   becomes prime -- m' and {h_i} are extremal, not chosen -- so it does not
   collide with the parity obstruction; conversely it cannot prescribe an
   exact gap word. The paper's workaround is subset-invariant tuple design:
   choose {b_j} so that EVERY (m+1)-subset of offsets yields the wanted
   word property. Realized instances: powers of 2 giving superincreasing
   words delta_1 + ... + delta_{j-1} < delta_j (Cor 1 proof, Part 5);
   iterated-product b_j giving full divisibility chains
   delta_1 ... delta_{j-1} | delta_j (Cor 2 proof, Part 5); AP images
   b_j = Da_j + a giving all gaps \equiv 0 mod D (Cor 3 proof, Part 6);
   plus mirrored variants via {x - b_j}. For the exchange target this is
   the reusable design principle: one would need a tuple family in which
   every delivered subset PAIR (across two traps) automatically has matched
   prefix/suffix blocks and a controlled middle discrepancy -- nothing of
   that sort is attempted in the paper, and the boundary-gap problem of
   point 2(a) remains even then.

4. The residue-class pattern (focus 3). Corollary 3 (Part 3): any class
   a mod D with gcd(a, D) = 1, D >= 3 FIXED; m consecutive primes all
   \equiv a mod D within diameter p_{r+m} - p_{r+1} <= DC_m, where the
   proof gives C_m = a_k - a_1 for any chosen admissible k_m-tuple
   (Part 6), i.e. C_m of order the narrowest admissible k_m-tuple diameter,
   k_m ~ e^{8m+4}/log per the engine theorem (this size estimate is
   extractor background, not paper content [BACKGROUND-UNVERIFIED]).
   Site count: "infinitely many r in N", nothing more. Specialized to
   D = 2^K (odd a), this yields runs of m consecutive primes whose m - 1
   consecutive gaps are ALL divisible by 2^K with run diameter <= 2^K C_m
   -- a 2-adically aligned gap word directly of the matched-window type the
   project needs at depth K. But K is frozen (no modulus growth, Part 7,
   item 3), so depth K ~ log2 log x is out of reach from the statement as
   printed.

5. Depth budget (focus 4). The engine invoked is Granville's formulation
   [3, Theorem 6.2] of Maynard-Tao for general (non-monic) linear forms
   satisfying (1), with k_m log k_m > e^{8m+4} (Part 2), plus the recorded
   refinements k_m = cm^2 e^{4m} [5] and k_m = ce^{(4-28/157)m} [8]
   (monic-forms caveat quoted in Part 2). All uniformity is: fixed m, fixed
   tuple, infinitely many n. To reach window depths J, K ~ log2 log x one
   needs m ~ log2 log x growing with x, hence k ~ exp(cm) ~ polylog x and
   x-uniform engine statements (primes in [x, 2x], tuples with offsets
   growing with x) -- a quantitative regime this note never enters. The
   note is an unconditional consecutivization ADAPTER on top of a fixed-m
   engine; upgrading the supply to growing depth requires replacing the
   engine invocation (e.g. by counting versions of Maynard's machinery),
   not the adapter, whose congruence trap itself scales harmlessly (the
   trap primes q_t and modulus Q depend only on the tuple, not on x).

6. Net verdict for the exchange configuration: this paper supplies, at
   FIXED depth, unconditional infinite families of sites with (i) identical
   interior gap words (Theorem 1 proof), (ii) designable subset-invariant
   word structure (Cors 1-2), (iii) 2^K-aligned gap runs of bounded
   diameter (Cor 3 with D = 2^K). It supplies NO site counts, NO boundary
   gap control, NO growing depth, and NO middle-difference mechanism. Its
   value to the project is the trap + maximality template (consecutiveness
   for free, evading parity by extremal subset choice) and the
   subset-invariant design trick -- both compatible in principle with a
   quantitative engine swap, which is exactly the part this paper does not
   provide.

---

## FLAGS (consolidated)

1. [TRANSCRIPTION-UNSURE] "must lie in A(n)" in Step 4 of the proof of
   Theorem 1 (p. 3): argument glyph n vs N; context quantifies over N.
   Transcribed as printed.
2. [TRANSCRIPTION-UNSURE] Exponent "(4-28/157)m" in the Polymath [8]
   constant k_m = ce^{(4-28/157)m} (p. 2): small print digits.
3. [TRANSCRIPTION-UNSURE] Recursion quantifier "for any j >= 3" in the
   proof of Corollary 2 (p. 4): could be j >= 4; both readings give the
   same sequence since b_3 = 2Q = b_2 + (b_2 - b_1).
4. [TRANSCRIPTION-UNSURE] Grant number "P200A90092" in the p. 1 footnote:
   small print.
5. [PRINTED-ODDITY] Abstract uses a single leading coefficient g
   (H(x) = {gx + h_j}) while Section 1 defines general g_j; both as
   printed.
6. [PARAPHRASE] markers: the one-sentence mechanism summary in Part 4, the
   index-notation note in Part 5, and the references block in Part 6 are
   marked paraphrase; everything else in Parts 1-6 quoted is verbatim.
7. [BACKGROUND-UNVERIFIED] In commentary item 4: the size estimate
   C_m ~ narrowest admissible k_m-tuple diameter with k_m ~ e^{8m+4}/log
   is extractor arithmetic on top of the quoted engine constant, not paper
   content.
