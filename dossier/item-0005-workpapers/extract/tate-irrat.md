# Extraction: Tao--Teravainen arXiv:2512.01739v2 -- irrationality strand
# (Theorem 1.3, Section 5, framing remarks)

Source: /home/istr/pro/erdos251/dossier/2512.01739v2.pdf (local copy, 61 pages).
Paper title: "QUANTITATIVE CORRELATIONS AND PRIME FACTORS" (running head), by
Terence Tao and Joni Teravainen.
Extraction method: pdftotext for location/search; all math-dense passages
transcribed from VISUAL page renders (Read tool, pages 3-5 and 44-56).
Notation note (paper's Section 1.6, p.10): log2 x := log log x, log3 x :=
log log log x, log4 x := log log log log x (ITERATED logs, not base-b logs).
X <<< Y means X = o(Y); X <<<< Y means X << Y^{o(1)}. e(x) := e^{2 pi i x}.
In this ASCII file "eps" = \epsilon, "omega" = \omega, "kappa_j" = \kappa_j,
"|eps|" = eps_1 + ... + eps_K, "1_{E}" = indicator.

--------------------------------------------------------------------------
## PART 0. VERSION CHECK (string searches over full pdftotext output)

Searched full text (7073 lines of pdftotext output; also a hyphenation-robust
search on the newline-stripped text).

1. String "unlikely" (case-insensitive, incl. hyphenated "un-likely" across
   line breaks): ZERO hits anywhere in v2.
2. String "at our current level" (and "current level"): ZERO hits anywhere
   in v2.
   => The quote "unlikely ... at our current level of understanding of
   analytic number theory", attributed to this paper by an earlier project
   note, is NOT PRESENT in v2. It either belongs to another version/source
   or is a misattribution. [Flagged.]
3. Occurrences of "current" in v2 -- exactly two, both in Remarks 4.2
   (third bullet), page 44, immediately preceding Section 5:
   VERBATIM (Remarks 4.2, third bullet, p.44):
   "The results for omega(n) = omega(n+1) can be adapted to other pairwise
   equations such as omega(n) = omega(n+h) for fixed h != 0 without
   significant modifications. However, to handle three-point equations such
   as omega(n) = omega(n+1) = omega(n+2) one would require, in addition to
   the previously mentioned extension of the methods to two dimensions, a
   version of Theorem 3.1 for triple correlations, which does not appear to
   be within current[footnote 8] technology. For similar reasons we are
   currently unable to remove the exceptional set in Theorem 1.7."
   Footnote 8 (p.44), VERBATIM: "Such methods may however be able to
   control partially relaxed versions of such equations, such as omega(n) =
   omega(n+1) = omega(n+2) + O(1), in which the contribution of large prime
   factors of n+2 can be ignored."
   => This "within current technology" remark is the closest v2 analogue of
   the alleged quote; it concerns TRIPLE correlations, not the
   irrationality result itself.
4. String "comparable difficulty": exactly ONE hit, Remark 1.2, page 3
   (in Section 1.2, directly after Theorem 1.1 = Erdos #248, the
   Erdos--Straus sieve-theoretic result). VERBATIM (Remark 1.2, p.3,
   second paragraph):
   "In [15] (see also [2, Problem #413], [14], [18], [29, Problem B8], and
   OEIS A005236), it was asked whether there are infinitely many n which
   were barriers for omega in the sense that omega(n-k) <= k for all
   1 <= k <= n. It may be that the methods of this paper can be pushed
   (particularly if one is more careful about how bounds depend on the
   sieve dimension) to establish[footnote 2] a result of this form for
   sufficiently large k; however, to handle small values of k, such as
   k = 1, 2, it seems that the problem is of comparable difficulty to the
   prime tuples conjecture (or the Sophie Germain conjecture that there are
   infinitely many primes p with 2p + 1 also prime), and we make no
   progress on it here."
   Footnote 2 (p.3), VERBATIM: "In fact, after the release of this
   preprint, bounds of the form omega(n +- k) <= Omega(n +- k) << log k
   were established for all 2 <= k <= n, by refining the methods of this
   paper; see [36]."
   Context note: the "comparable difficulty" sentence is about the
   omega-BARRIER problem for small k (Problem #413 context, following the
   Erdos--Straus Theorem 1.1), NOT about Theorem 1.3.

--------------------------------------------------------------------------
## PART 1. THEOREM 1.3 AND ALL INTRODUCTION REMARKS ON METHOD /
## EXTENSIONS / LIMITATIONS

### 1.1 Theorem statement

VERBATIM (Theorem 1.3, Section 1.3, p.4):
"Theorem 1.3 (Erdos #69). The series
(1.7)   \sum_{n=1}^{\infty} \frac{\omega(n)}{2^n} = \sum_p \frac{1}{2^p - 1}
        = 0.5169428... (OEIS A262153)
is irrational."

(Section 1.3 opens, VERBATIM, p.4: "An irrationality result. The motivation
in [18] for asking the above question was to resolve the following
irrationality problem, which we also establish in Section 5.")

### 1.2 Priority / history remarks (Section 1.3, p.4)

VERBATIM: "Recently, Theorem 1.3 was shown conditionally on a form of the
prime tuples conjecture in [46]; our result makes the irrationality
unconditional. This answers a question of Erdos ([12], [18, p. 61], [17,
p. 102], [2, Problem #69]); in [18, p.61] it is stated that 'it is very
annoying that (1.7) cannot be proven irrational', in comparison with
similar sums such as the Erdos--Borwein constant
\sum_{n=1}^\infty tau(n)/2^n = \sum_{n=1}^\infty 1/(2^n - 1) = 1.606695...
(OEIS A065442) which has long been known to be irrational [11]."
Reference [46] is: "K. Pratt. The irrationality of an infinite series
involving omega(n) under a prime tuples conjecture. J. Number Theory" (p.61).

### 1.3 Extension remarks (Section 1.3, p.4)

VERBATIM: "This result also establishes a single special case of the
conjecture ([12], [18, p. 62], [17, p. 105], [2, Problem #257]) that
\sum_{n in A} \frac{1}{2^n - 1} is irrational for any infinite set
A \subset N, namely the case when A is the set of primes. (The
aforementioned result from [11] corresponds to the case A = N.) It seems
likely that the arguments in this paper can also treat other sets A that
are sufficiently similar to the primes, but we do not pursue this question
here. The method can also be modified to establish the irrationality of
\sum_{n=1}^\infty \frac{\omega(n)}{b^n} for any integer base b >= 2; in
fact the case b > 2 is somewhat easier due to the faster convergence of
certain coefficients that arise in the analysis. A similar argument can
also establish the irrationality of
\sum_{n=1}^\infty \frac{\Omega(n)}{2^n} = \sum_{j=1}^\infty \sum_p
\frac{1}{2^{p^j} - 1} = 0.5895033...
(corresponding to the case of [2, Problem #257] where A is the set of prime
powers); we leave the details of such modifications to the interested
reader."

NOTE: the paper nowhere discusses \sum p_n/2^n (Erdos #251) or any series
whose n-th coefficient is the n-th prime; searches for "#251" produced no
hits (only #248, #257, #258, #69, #413, #647, #679, #864, #946 appear).

### 1.4 Method-overview remarks (Section 1.3, p.4)

VERBATIM: "To establish Theorem 1.3, upper bounds on consecutive values
omega(n+1), omega(n+2), ..., omega(n+H) of omega, such as (1.6), are
insufficient; some control on the distribution of various linear
combinations of such values (e.g., \sum_{h=1}^{H} \frac{\omega(n+h)}{2^h})
is needed. Furthermore, the contribution of large prime factors (e.g.,
p >= n^{1/100}) is no longer negligible and requires more delicate
analysis. If a sufficiently quantitative form of the prime tuples
conjecture is available, one can obtain quite good control on such values
for selected n; this is the strategy taken in [46]. In the absence of the
prime tuples conjecture, known distributional results such as those in
[37], [3] turned out to be too weak for our purposes. However, after
applying some manipulations of Gowers uniformity norm type to various
expressions relating to (1.7), we were able to arrive at a certain linear
combination of consecutive values of omega that could be adequately
controlled by a combination of Erdos--Kac-type results, as well as pairwise
correlation estimates for multiplicative functions; but the latter requires
a version of the recent strong quantitative results of Elliott-type due to
Pilatte [42] in order to keep the error terms under control."

Also (Section 1.4, p.4-5), VERBATIM: "It is the equidistributed case of
Theorem 3.1 that will be relevant for proving Theorem 1.3."

Supporting context (Section 1.3 end, p.4-5): the main correlation input is
an estimate of the form
\frac{W}{N} \sum_{N < n <= 2N} (g_1(n+h_1) - delta_N) g_2(n+h_2)
1_{n = b (mod W)} << Lcal^{-c}
"for all scales N outside of a small exceptional set and various 1-bounded
multiplicative functions g_1, g_2", with g_1 "equidistributed" or
"non-pretentious"; "See Theorem 3.1 for a precise (but somewhat technical)
statement." (Here Lcal is the calligraphic-L parameter, 1 <= Lcal << log N.)

--------------------------------------------------------------------------
## PART 2. ANATOMY OF SECTION 5 ("5. Application to an irrationality
## problem of Erdos", pp.44-56)

Section 5 opening, VERBATIM (p.44): "In this section we establish Theorem
1.3. As with [46], our arguments will proceed by understanding the
distribution of consecutive blocks omega(n+1), ..., omega(n+L) of the
prime counting function omega for some relatively small L; but without the
prime tuples conjecture, the control on this distribution will be quite
crude."

### STEP 0: Contradiction hypothesis (Section 5 preamble, p.44)

(a) Anchor: Section 5 preamble (unnumbered display), p.44.
(b) Input: assumed rationality.
(c) Output: VERBATIM: "Suppose for contradiction that the above sum is
    equal to a/q for some integers a, q >= 1, thus
    q \sum_{h=1}^{\infty} \frac{\omega(h)}{2^h} = 0 (mod 1).
    We view q as fixed, and allow all implicit constants to depend on q."
(d) No use of additivity/boundedness yet.
(e) No dilation yet.

### STEP 1: Subsection 5.1 "Shifting and dilating" (p.45)

(a) Anchors: (5.1), (5.2), (5.3); unnumbered identity displays between them.
(b) Inputs: Step 0 congruence; the additivity identity; geometric series
    q \sum_{h=1}^\infty 1/2^h = q = 0 (mod 1).
(c) Outputs:
    (5.1): q \sum_{h=1}^{\infty} \frac{\omega(n+h)}{2^h} = 0 (mod 1)
    "for any n in N." Derivation, VERBATIM: "Reindexing h as n+h for some
    natural number n and then multiplying by 2^n, we conclude that (5.1)."
    Then, VERBATIM: "To make use of these congruences, we exploit the
    additivity of omega to dilate the shift h. If p is a prime, we have the
    identity
        omega(pn) = omega(n) + 1 - 1_{p|n}
    for any natural number n, and hence if n is divisible by p,
        omega(n + ph) = omega(n/p + h) + 1 - 1_{p^2 | n+ph}."
    Applying (5.1) with n replaced by n/p and using q \sum 1/2^h = q = 0
    (mod 1):
    (5.2): q \sum_{h=1}^{\infty} \frac{\omega(n+ph)}{2^h} = -q delta_p(n)
    (mod 1) "whenever p | n", where
    (5.3): delta_p(n) := \sum_{h=1}^{\infty} \frac{1_{p^2 | n+ph}}{2^h}.
    VERBATIM: "In practice, delta_p(n) will be negligible for typical n and
    primes p that are not too small."
(d) THE additivity identity omega(pn) = omega(n) + 1 - 1_{p|n} is used HERE
    and is the engine of the whole section: it converts the shift-h
    congruence at n/p into a shift-ph congruence at n.
(e) THIS IS THE SHIFT DILATION: h -> ph, valid for each prime p dividing n,
    at the cost of the error term delta_p(n) (square divisibility).

### STEP 2: Subsection 5.2 "Taking an alternating sum to cancel terms"
### (pp.45-46)

(a) Anchors: (5.4), (5.5), (5.6), (5.7), (5.8); unnumbered displays.
(b) Inputs: (5.2) applied with p = p_eps for 2^K primes in a combinatorial
    cube; a choice of cube parameters (later supplied by Lemma 5.2).
(c) Outputs. VERBATIM framing: "Inspired by the theory of the Gowers
    uniformity norms, we now manipulate (5.2) to eliminate the role of the
    first few terms in h, at the cost of increasing the number of remaining
    terms."
    (5.4): p_eps := p_0 + eps_1 v_1 + ... + eps_K v_K, required to be
    "distinct primes for all eps = (eps_1,...,eps_K) in {0,1}^K".
    n is required to obey
    (5.5): n = \sum_{k=1}^{K} k eps_k v_k (mod p_eps) for all eps in
    {0,1}^K;
    (5.6): n > \sum_{k=1}^{K} k |v_k|.
    From (5.2) with p = p_eps and n - \sum_k k eps_k v_k in place of n:
    q \sum_{h=1}^\infty \frac{\omega(n + r_{eps,h})}{2^h}
      = -q delta_{p_eps}(n - \sum_{k=1}^K k eps_k v_k) (mod 1),
    where
    (5.7): r_{eps,h} := p_eps h - \sum_{k=1}^{K} k eps_k v_k
                      = p_0 h + \sum_{k=1}^{K} (h-k) eps_k v_k.
    Alternating sum over eps with weight (-1)^{|eps|}. KEY CANCELLATION,
    VERBATIM: "The point of doing this is that for 1 <= h <= K, the shift
    r_{eps,h} is independent of eps_h thanks to (5.7). As a consequence, we
    have \sum_{eps_h in {0,1}} (-1)^{eps_h} omega(n + r_{eps,h}) = 0, so
    the summand on the left-hand side vanishes for such h."
    Eliminating h = 1..K and reindexing:
    (5.8): q \sum_{h=1}^{\infty} \frac{\sum_{eps in {0,1}^K} (-1)^{|eps|}
    \omega(n + r_{eps,h+K})}{2^{h+K}}
      = -q \sum_{eps in {0,1}^K} (-1)^{|eps|} delta_{p_eps}(n -
      \sum_{k=1}^K k eps_k v_k) (mod 1).
    Applying "the Lipschitz function t -> e(t)":
    e( q \sum_{h=1}^\infty [\sum_eps (-1)^{|eps|} omega(n + r_{eps,h+K})]
       / 2^{h+K} ) = 1 + O( \sum_{eps} delta_{p_eps}(n - \sum_k k eps_k
       v_k) ).
(d) Additivity is inherited via (5.2); no boundedness used yet.
(e) Dilation role: each cube vertex eps supplies its own dilated shift
    system h -> p_eps h; the affine-in-eps structure of (5.7) is what makes
    r_{eps,h} independent of eps_h for h <= K (Gowers-cube cancellation in
    the SHIFT variable).

### STEP 3: Subsection 5.3 "Taking expectations and truncating" (p.46)

(a) Anchors: (5.9), (5.10), (5.11), (5.12), (5.13).
(b) Inputs: end display of Step 2; a random n obeying (5.5), (5.6)
    (distribution "to be determined", fixed in 5.6); decomposition (1.1)
    omega(n) = \sum_p 1_{p|n} (p.1 of paper).
(c) Outputs:
    (5.9): E e( q \sum_{h=1}^\infty \frac{\sum_eps (-1)^{|eps|}
    omega(n + r_{eps,h+K})}{2^{h+K}} ) = 1 + O(kappa_1), where
    (5.10): kappa_1 := \sum_{eps in {0,1}^K} E delta_{p_eps}(n -
    \sum_{k=1}^K k eps_k v_k) = \sum_{eps in {0,1}^K} \sum_{h=1}^\infty
    \frac{P(p_eps^2 | n + r_{eps,h})}{2^h}.
    Truncation at cutoff H ("to be chosen later") by Taylor expansion:
    E e( q \sum_{1<=h<=H} ... / 2^{h+K} ) = 1 + O(kappa_1) + O(kappa_2),
    (5.11): kappa_2 := \sum_{h>H} \frac{\sum_{eps in {0,1}^K}
    E omega(n + r_{eps,h+K})}{2^{h+K}}.
    VERBATIM: "Using (1.1), we can rewrite this as
    (5.12): E e( \sum_p X_p ) = 1 + O(kappa_1) + O(kappa_2)"
    "where for each prime p, X_p denotes the random variable
    (5.13): X_p := q \sum_{1<=h<=H} \sum_{eps in {0,1}^K} (-1)^{|eps|}
    \frac{1_{p | n + r_{eps,h+K}}}{2^{h+K}}."
(d) The decomposition of omega into prime indicators -- (1.1), an avatar of
    additivity -- is used exactly at (5.12)/(5.13): the whole exponential
    factors over primes p. (Boundedness NOT used; omega is unbounded.)
(e) No new dilation; the shifts r_{eps,h+K} are carried along.

### STEP 4: Prime-partition and kappa_3 (end of 5.3, p.47)

(a) Anchors: (5.14), (5.15); unnumbered two-line display before (5.14).
(b) Inputs: (5.12); a partition (hypothesized here, constructed in 5.5/5.6)
    "S_0 union-disjoint S_1 union-disjoint S_2 of the set of primes p into
    a core set S_1 and exceptional sets S_0, S_2, with the hypothesis that
    the X_p are deterministic constants X_p for p in S_0 (in practice, this
    will be accomplished by enforcing a congruence condition on n for each
    prime in S_0)."
(c) Outputs: by "Taylor expansion and Cauchy--Schwarz":
    E e(\sum_p X_p) = e(\sum_{p in S_0} X_p) E e(\sum_{p in S_1} X_p)
      + O(kappa_3), where
    (5.14): kappa_3 := ( E | \sum_{p in S_2} X_p |^2 )^{1/2}.
    (5.15): | E e( \sum_{p in S_1} X_p ) | = 1 + O(kappa_1) + O(kappa_2)
    + O(kappa_3).
    VERBATIM: "Obtaining an adequate control on kappa_3 will be somewhat
    delicate, particularly for very large primes where the correlation
    estimate of Theorem 3.1 is needed."
(d) None here.
(e) None here.

### STEP 5: Subsection 5.4 "Extracting a variance bound" (pp.47-49)
### -- the Erdos--Kac-type variance layer

(a) Anchors: (5.16), (5.17), (5.18), (5.19), (5.20); Theorem 5.1; several
    unnumbered displays.
(b) Inputs: (5.15); independent copies X'_p ("We let X'_p be a copy of X_p,
    but with the X'_p jointly independent in p"); even Taylor index M.
(c) Outputs:
    Comparison of E e(\sum_{S_1} X_p) with E e(\sum_{S_1} X'_p) by "Taylor
    expansion with remainder to some even index M", producing
    (5.16): kappa_4 := \sum_{m=0}^{M} \frac{(2 pi)^m}{m!}
    | E (\sum_{p in S_1} X_p)^m - E (\sum_{p in S_1} X'_p)^m |.
    Power-series inequality e^t + e^{-t} >= |t|^M / M! applied with
    t = 2 pi e \sum_{p in S_1} X'_p, using independence, gives (with
    M even) \frac{(2 pi)^M}{M!} ( E(\sum X_p)^M + E(\sum X'_p)^M )
    << kappa_4 + kappa_5, where
    (5.17): kappa_5 := \frac{ \prod_{p in S_1} E exp(2 pi e X_p) +
    \prod_{p in S_1} E exp(-2 pi e X_p) }{ e^M }.
    "By independence, (5.15), and the triangle inequality":
    | \prod_{p in S_1} E e(X_p) | = 1 + \sum_{j=1}^{5} O(kappa_j).
    Assuming
    (5.18): kappa_1, ..., kappa_5 = o(1)
    "as some asymptotic parameter x goes to infinity along some sequence",
    taking logarithms: \sum_{p in S_1} log \frac{1}{|E e(X_p)|} <<
    \sum_{j=1}^5 kappa_j. If additionally
    (5.19): X_p = o(1) for all p in S_1,
    then by Taylor expansion of the complex exponential (with a recentering
    theta in [-1/2,1/2], using 1 - cos(t) asymp t^2 for |t| <= (2 - 1/10)pi
    and 1 - t <= e^{-t}):
    |E e(X_p)| <= 1 - c E(X_p - theta)^2 <= 1 - c Var X_p <=
    exp(-c Var X_p) "for some constant c > 0, and hence
    (5.20): \sum_{p in S_1} Var X_p << \sum_{j=1}^{5} kappa_j."
    Then the reduction is packaged as:
    VERBATIM (Theorem 5.1, p.49): "Theorem 5.1 (Technical reduction).
    There exists a sequence of x going to infinity for which the following
    statement holds: there exist natural numbers K, H, M with M even,
    integers p_0 >= 1 and v_1, ..., v_K with p_eps := p_0 + eps_1 v_1 +
    ... + eps_K v_K distinct primes for all eps in {0,1}^K, a partition of
    the primes into disjoint sets S_0, S_1, S_2, and a random natural
    number n obeying (5.5), (5.6) -- all of which can depend on x -- such
    that (recalling (5.7)) the quantities kappa_1, ..., kappa_5 defined in
    (5.10), (5.11), (5.14), (5.16), (5.17) obey (5.18), but the random
    variables X_p defined in (5.13) are deterministic for p in S_0 and also
    obey the condition
    (5.21): \sum_{p in S_1} Var X_p >> 1."
    VERBATIM: "Indeed, it is clear that (5.18), (5.20), and (5.21) will
    contradict each other for x large enough."
(d) None directly (works at the level of the X_p).
(e) None.
    Erdos--Kac connection: the X_p are (signed, weighted) prime-divisor
    indicator statistics; the second-moment/variance method over
    approximately independent 1_{p|n+r} is exactly the Erdos--Kac-type
    layer announced in Section 1.3 ("controlled by a combination of
    Erdos--Kac-type results"). [Commentary cross-ref: Part 4, step E.]

### STEP 6: Subsection 5.5 "Selecting parameters" (pp.49-51)

(a) Anchors: (5.22)-(5.32); Lemma 5.2; hierarchy (5.30); (5.31);
    discriminant W display (unnumbered, p.51).
(b) Inputs: Theorem 5.1's statement to be established; x large.
(c) Outputs. Parameter choices (all logs iterated):
    (5.22): K := floor( 2 log4 x / log 2 )
    (5.23): H := floor( log3^2 x )
    (5.24): M := 2 floor( log2 x )
    (5.25): H_+ := floor( log2^2 x )
    (5.26): P := exp( log3^3 x )
    (5.27): L := log^{1/ log3 x} x
    (5.28): R := x^{1/ log2^2 x}
    (5.29): R_+ := x^{1/100}
    (5.30) hierarchy of scales, VERBATIM (one display, using <<< for
    "much less" = o(), <<<< for << Y^{o(1)}):
    "1 <<<< K <<<< log3 x asymp (log2 R_+ - log2 R) <<< H asymp 2^K
     <<< log P asymp log(H_+ K P) <<<< M asymp log2 R asymp log2 x
     <<< H_+ <<<< 2^H <<< P <<<< P^{2K}
     <<<< (HKP)^{2^{2K} H^2} <<< L <<< log x <<<< P^M <<< 2^{H_+} <<<< R
     <<<< R^M <<< R_+ <<< x."
    [TRANSCRIPTION-UNSURE: the exact placement of the <<< vs <<<< symbols
    inside (5.30); the ordering of the listed quantities is as displayed.]
    (5.31): 2^{2K} H^2 / P = 1/P^{1-o(1)} << ( o(1/log P) )^{2^K}.
    Shift classes, VERBATIM: "we divide the shifts h >= 1 into three
    classes: near shifts 1 <= h <= H; far shifts H < h <= H_+; and very far
    shifts h > H_+."
    LEMMA 5.2 (Hilbert cube / Gowers lemma), VERBATIM (p.50):
    "Lemma 5.2. There exist integers p_0, v_1, ..., v_K with p_0 >= 1 such
    that the integers p_0 + eps_1 v_1 + ... + eps_K v_K for eps in {0,1}^K
    are distinct primes in [P/2, P], and furthermore for all eps in
    {0,1}^K and near shifts 1 <= h <= H, the quantities r_{eps,h+K}
    (defined in (5.7)) are all distinct."
    Proof anatomy (p.50-51): VERBATIM opening: "This is an application of
    the 'Hilbert cube lemma', which we will utilize via the modern language
    of Gowers uniformity norms." There are asymp P/log P primes in
    [P/2, P]; embed in Z/(5P)Z; let f be the indicator of embedded primes;
    then ||f||_{U^1(Z/((5P)Z))} >> 1/log P; "Thus by monotonicity of the
    Gowers norms (see, e.g., [53, (11.7)])
    ||f||_{U^K(Z/((5P)Z))} >> 1/log P."
    ([53] = T. Tao and V. H. Vu, Additive Combinatorics, Cambridge Studies
    in Advanced Mathematics 105, 2010 -- confirms the reported Tao--Vu
    (11.7) citation.)
    Random tilde-p_0, tilde-v_1..tilde-v_K uniform in Z/(5P)Z: probability
    all 2^K cube points land on primes is >= (c/log P)^{2^K}; collision
    probabilities O(2^{2K}/P) (cube vertices) and O(2^{2K} H^2 / P) (the
    tilde-r_{eps,h+K} := tilde-p_eps h - \sum_k k eps_k tilde-v_k); by
    (5.31) a good tuple exists; lift from Z/((5P)Z) to Z ("the modulus 5P
    is large enough to prevent 'wraparound' from occurring"), giving
    genuine primes p_eps in [P/2, P] and distinct r_{eps,h+K}.
    (5.32): r_{eps,h+K} << (h+K) K P "for any eps in {0,1}^K and shifts
    h >= 1."
    Discriminant (unnumbered, p.51): W := \prod_{eps,eps' in {0,1}^K}
    \prod_{1<=h,h'<=H, (eps,h) != (eps',h')} | r_{eps,h+K} - r_{eps',h'+K} |,
    with W <= (O(HKP))^{2^{2K} H^2} <<<< exp(log3^{O(1)} x) <<< L <<< x.
    Prime classes, VERBATIM: "small primes in which p | W or p = p_eps for
    some eps in {0,1}^K; medium primes p <= R not dividing W and not equal
    to any of the p_eps; large primes R <= p < R_+; and very large primes
    p > R_+;" with "S_0 ... the set of small primes, S_1 ... the set of
    medium primes, and S_2 ... the set of large and very large primes."
(d) None.
(e) The Hilbert-cube lemma supplies the arithmetic-progression-of-primes
    structure {p_eps} that the dilation step needs: 2^K DISTINCT prime
    dilation factors forming an affine cube, so that Step 2's cancellation
    works.

### STEP 7: Subsection 5.6 "Constructing the random variable" (pp.51-52)

(a) Anchors: (5.33)-(5.36).
(b) Inputs: Lemma 5.2 output; parameter choices; CRT; prime number theorem.
(c) Outputs: "We select the random variable n uniformly at random among
    the integers in [x/2, x] that obey the congruences (5.5), as well as
    the additional congruence condition
    (5.33): n = 0 (mod W^flat), where W^flat := W / \prod_{eps in {0,1}^K}
    p_eps^{v_{p_eps}(W)}."
    ("In particular, p_eps does not divide W^flat for all eps, so (5.33) is
    automatically compatible with the congruences (5.5).")
    n is thus confined to an arithmetic progression Q of [x/2, x] with
    spacing Q obeying
    (5.34): Q << P^{2^K} W^flat <<<< exp(log3^{O(1)} x) <<< L <<< x.
    (5.35): E f(n) = fbar + O( u ||f||_infty / x^{1-o(1)} ) "for any
    u-periodic function f with mean fbar and supremum norm ||f||_infty,
    where u is coprime to Q."
    (5.6) is automatic since \sum_k k |v_k| << K^2 P << x/2 by (5.30).
    VERBATIM: "The congruence condition (5.33) also ensures that X_p is
    deterministic for all small primes p in S_0. For non-small primes
    p in S_1 union S_2, we have the bound
    (5.36): X_p = O(1/2^K)
    since all the shifts r_{eps,h+K} reduce to distinct residue classes
    mod p for eps in {0,1}^K and near shifts 1 <= h <= H, by definition of
    W, and the fact that p does not divide W^flat. In particular, (5.19)
    is obeyed."
(d) None new.
(e) None new. (The W-divisibility freeze makes small-prime contributions
    deterministic -- this is what realizes the S_0 part of Theorem 5.1.)

### STEP 8: Subsection 5.7 "Estimation of kappa_1" (p.52)

(a) Anchor: subsection 5.7; feeds (5.10) and (5.18).
(b) Inputs: (5.10), (5.5), (5.30).
(c) Output: near shifts: "the condition p_eps^2 | n - \sum_k k eps_k v_k
    + p_eps h restricts n to lie in a subprogression of Q of p_eps times
    the spacing", so P(p_eps^2 | n + r_{eps,h}) << 1/p_eps << 1/P; far or
    very far shifts: trivial bound <= 1. Hence
    kappa_1 << 2^K ( 1/P + 1/2^H ). "By (5.30) ... acceptable."
(d) None.
(e) None. (This is where the delta_p error of the dilation is retired.)

### STEP 9: Subsection 5.8 "Estimation of kappa_2" (p.52)

(a) Anchor: subsection 5.8; feeds (5.11) and (5.18).
(b) Inputs: (5.11), (5.32), (1.21) (additive splitting f = f_{<=w} +
    f_{w<.<=z} + f_{>z}), (5.35), (5.5), Mertens.
(c) Output: very far shifts h > H_+: "we use the very crude bound
    omega(n) << log n", giving contribution << (log x + log(P H_+))/2^{H_+}
    [TRANSCRIPTION-UNSURE: displayed as (log x + log(P H_+))/2^{H_+}; the
    preceding inline line reads omega(n + r_{eps,h+K}) << log x +
    log(h K P)]. Far shifts H < h <= H_+: "as n + r_{eps,h+K} = O(x) can
    have at most O(1) prime factors larger than R_+, we have
    omega_{>R_+}(n + r_{eps,h+K}) << 1"; small primes: "from the congruence
    condition (5.5) we have \sum_{p small} 1_{p | n + r_{eps,h+K}} =
    omega(r_{eps,h+K}) << log r_{eps,h+K} << log(H_+ K P)"; medium/large
    primes via (5.35): E 1_{p | n + r_{eps,h+K}} << 1/p + p/x^{1-o(1)} <<
    1/p, so by Mertens E omega(n + r_{eps,h+K}) << log2 R_+ + log(H_+ K P).
    Total: kappa_2 << (log2 R_+ + log(H_+ K P))/2^H + (log x +
    log(H_+ K P))/2^{H_+}; acceptable by (5.30).
(d) USES: (i) crude growth bound omega(n) << log n (unboundedness is
    harmless only because of the 2^{-h} decay); (ii) the BOUNDEDNESS of
    the number of very large prime factors: omega_{>R_+}(m) << 1 for
    m = O(x); (iii) additive decomposition (1.21) of omega by prime size.
(e) None.

### STEP 10: Subsection 5.9 "Estimation of kappa_4" (p.53)

(a) Anchor: subsection 5.9; feeds (5.16) and (5.18).
(b) Inputs: (5.35), (5.36), (5.30).
(c) Output: for 0 <= m <= M and medium p_1,...,p_m in S_1, p_1...p_m <=
    R^M; E X_{p_1}...X_{p_m} - E X'_{p_1}...X'_{p_m} <<
    R^M/(2^K x^{1-o(1)}) << 1/x^{1-o(1)}; inserting into (5.16):
    kappa_4 << M (2 pi)^M P^M / x^{1-o(1)}
    [TRANSCRIPTION-UNSURE: the displayed exponent base reads P^M in both
    the rendered page and pdftotext, although the preceding sentence bounds
    products of medium primes by R^M; both P^M and R^M are << x^{1/2} by
    (5.30) so the estimate is acceptable either way]. "By (5.30) ...
    acceptable."
(d) None.
(e) None. (This step justifies replacing X_p by independent copies:
    quasi-independence of divisibility events across distinct medium
    primes, via CRT/(5.35).)

### STEP 11: Subsection 5.10 "Estimation of kappa_5" (p.53)

(a) Anchors: (5.37), (5.38); feeds (5.17) and (5.18).
(b) Inputs: (5.36)/(5.19), (5.35), (5.30), Mertens.
(c) Output: exp(+-2 pi e X_p) = 1 +- 2 pi e X_p + O(|X_p|^2);
    (5.37): E X_p << p / x^{1-o(1)} = 1/x^{1-o(1)}
    (5.38): E |X_p|^2 asymp 1/(2^K p) + O(p/x^{1-o(1)}) asymp 1/(2^K p),
    so E exp(+-2 pi e X_p) = exp( O(1/(2^K p)) ), "and hence by Mertens'
    theorem and (5.17) we have kappa_5 << exp( O(log2 R / 2^K) - M )."
    Acceptable by (5.30). (Note: the closing sentence of 5.10 says "the
    contribution of kappa_4 to (5.18) is acceptable" -- an evident typo
    for kappa_5 in the paper.)
(d) None. (The 1/(2^K p) second moment is the Bernoulli(1/p) divisor-
    indicator calculation -- Erdos--Kac-type input.)
(e) None.

### STEP 12: Subsection 5.11 "Variance bound" (p.53) -- proves (5.21)

(a) Anchor: subsection 5.11.
(b) Inputs: (5.37), (5.38), (5.30), Mertens.
(c) Output: Var X_p asymp 1/(2^K p) for medium p, "so by Mertens' theorem
    \sum_{p in S_1} Var X_p >> (log2 R - log2 W)/2^K and the claim (5.21)
    follows from (5.30)."
(d) The positive variance comes from the genuinely random divisor
    indicators 1_{p | n + r_{eps,h+K}} -- the Erdos--Kac fluctuation.
(e) None.

### STEP 13: Subsection 5.12 "Estimation of kappa_3" -- splitting (p.53)

(a) Anchors: (5.39), (5.40).
(b) Inputs: (5.14), triangle inequality.
(c) Output: "The last remaining task required for Theorem 5.1 is to
    establish kappa_3 = o(1) given by (5.14). By (5.14) and the triangle
    inequality, we may split this into two subtasks, corresponding to the
    large and very large primes respectively:
    (5.39): E | \sum_{R < p <= R_+} X_p |^2 = o(1)
    (5.40): E | \sum_{R_+ < p <= 2x} X_p |^2 = o(1)
    (note that X_p will necessarily vanish for p > 2x)."
(d) None.
(e) None.

### STEP 14: Subsection 5.13 "Contribution of large primes to kappa_3"
### (p.54) -- proves (5.39)

(a) Anchor: subsection 5.13.
(b) Inputs: (5.36), (5.13), (5.35), Mertens, (5.30).
(c) Output: for distinct large primes R < p, p' <= R_+: "the product
    X_p X_{p'} is periodic in n with period p p' <= R_+^2, bounded by
    (5.36), and mean zero thanks to the alternating factor (-1)^{|eps|} in
    (5.13), so from (5.35) we have E X_p X_{p'} = O( R_+^2 / x^{1-o(1)} )."
    Expanding the square: E |\sum_{R<p<=R_+} X_p|^2 = \sum E|X_p|^2 +
    O( R_+^4 / x^{1-o(1)} ). "There are no collisions between the various
    congruence classes defining X_p in (5.13), and so by (5.35) one has
    E |X_p|^2 << 1/(p 2^K) + R_+/x^{1-o(1)}." Mertens then bounds the LHS
    of (5.39) by << R_+^4/x^{1-o(1)} + (log2 R_+ - log2 R)/2^K, and (5.30)
    concludes (5.39). (Note K asymp log4 x is chosen exactly so that
    2^K >> log2 R_+ - log2 R asymp log3 x... more precisely (5.30) records
    (log2 R_+ - log2 R) asymp log3 x <<< H asymp 2^K.)
(d) None new.
(e) The alternating cube factor (-1)^{|eps|} (the Gowers structure) is
    what makes the off-diagonal terms mean zero -- without the cube, large
    primes would contribute a main term here.

### STEP 15: Subsection 5.14 "Contribution of very large primes to
### kappa_3" (pp.54-56) -- proves (5.40); THE INVOCATION OF THEOREM 3.1

(a) Anchors: (5.41)-(5.45); unnumbered displays; the Theorem 3.1
    application paragraph (p.55); Selberg sieve paragraph (p.56).
(b) Inputs: Cauchy--Schwarz; the partition of (R_+, 2x] into L intervals;
    (5.44); (5.35)/(5.34); Theorem 3.1 (equidistributed case); (3.14);
    Selberg's sieve.
(c) Output chain:
    - "By inserting an alternating sum of 1/p and applying the
      Cauchy--Schwarz inequality, it will suffice to show that
      E | \sum_{eps in {0,1}^K} (-1)^{|eps|} \sum_{R_+ < p <= 2x}
      ( 1_{p | n + r_{eps,h+K}} - 1/p ) |^2 = o(2^{2K})
      for all near shifts 1 <= h <= H."
    - Fix h; on squaring it suffices to show
      (5.41): E | \sum_{R_+ < p <= 2x} (1_{p | n + r_{eps,h+K}} - 1/p) |^2
      << 1 for eps in {0,1}^K, and
      (5.42): E ( \sum_{R_+<p<=2x} (1_{p|n+r_{eps,h+K}} - 1/p) )
      ( \sum_{R_+<p'<2x} (1_{p'|n+r_{eps',h+K}} - 1/p') ) = o(1)
      for distinct eps, eps' in {0,1}^K. "The former claim (5.41) is easy
      since the expression in parentheses is bounded" (an n = O(x) has at
      most O(1) prime factors > R_+ = x^{1/100}).
    - Partition (R_+, 2x] into L subintervals J_l = (y_{l-1}, y_l],
      log2 y_l - log2 y_{l-1} asymp log2 x / L. For n = O(x):
      (5.43): \sum_{R_+ < p | n, p < 2x} 1_{p|n} = \sum_{l in [L]}
      ( 1 - g_l(n) + O(1_{n in E_l}) )
      "where, for each l in [L], g_l is the completely multiplicative
      function with g_l(p) := 1_{p not in J_l} for all primes p, and E_l is
      the set of n in [x/2, x] cap N for which there exist two primes
      y_{l-1} < p <= p' <= y_l which both divide n."
    - (5.44): (1/(x/2)) \sum_{x/2 <= n <= x} 1_{n in E_l} <<
      (log2 x / L)^2 ("The sets E_l are quite sparse: a standard
      application of Mertens' theorem").
    - delta_{l,x} := (1/(x/2)) \sum_{x/2 <= n <= x} g_l(n); taking means
      in (5.43) and subtracting:
      (5.45): \sum_{R_+ < p < 2x} ( 1_{p|n} - 1/p ) = - \sum_{l in [L]}
      ( g_l(n) - delta_{l,x} + O(1_{n in E_l}) ) + o(1).
    - Insert (5.45) (with n set to n + r_{eps,h+K} and n + r_{eps',h+K})
      into (5.42); E_l terms cost << E 1_{n + r_{eps,h+K} in E_l} <<
      Q (log2 x)^2 / L^2, net effect O(Q (log2 x)^2 / L) = o(1) by (5.30).
      Reduces (5.42) to
      \sum_{l, l' in [L]} E ( g_l(n + r_{eps,h+K}) - delta_{l,x} )
      ( g_{l'}(n + r_{eps',h+K}) - delta_{l',x} ),
      and by triangle inequality and (5.30) it suffices to show
      E ( g_l(n + r_{eps,h+K}) - delta_{l,x} )( g_{l'}(n + r_{eps',h+K})
      - delta_{l',x} ) << log^{-c} x
      "for some absolute constant c > 0 and all l, l' in [L]."
    - THEOREM 3.1 INVOCATION, VERBATIM (p.55): "Applying Theorem 3.1 (in
      the equidistributed case with Lcal = log^c x) with g_1 set to g_l and
      g_2 set to either g_{l'} or 1, and noting that importantly the
      spacing Q of the progression to which n is restricted is <<
      log^{o(1)} x by (5.34), we see that it will suffice (after
      restricting x to a subsequence) to show that
      \sum_{N < n <= 2N, n = a (mod r)} g_l(n) = (N/r) delta_{l,N}
      + O(N log^{-c} x)
      for some absolute constant c > 0 and all x^{0.4} <= N <= x and
      a, r in N, and similarly for g_{l'}." Reductions: (a,r) = 1 (using
      (3.14); "after worsening the lower bound on N to say x^{0.3} <= N"),
      r = O(log^c x) ("as the claim is trivial otherwise").
    - Verification by inclusion-exclusion (p.56): since J_l lies in
      (R_+, 2x] and R_+ = x^{1/100}, at most 101 prime factors from J_l:
      (1/N) \sum_{N<n<=2N} g_l(n) = \sum_{i=0}^{101} (-1)^i
      \sum_{p_1 < ... < p_i, p_1..p_i in J_l, p_1...p_i <= 2N}
      ( 1/(p_1...p_i) + O(1/N) ), and the same in APs mod r with error
      O(r/N) per term; it suffices that for all 0 <= i <= 101,
      \sum_{p_1<...<p_i, in J_l, p_1...p_i <= 2N} r/N << log^{-c} N.
      VERBATIM: "But by a simple application of Selberg's sieve there are
      only O(N log^{-1} N) numbers n <= 2N that are not divisible by any
      prime less than or equal to R_+, so the number of summands here is
      N log^{-1} N, and the claim follows since r = O(log^c x)." [END of
      Section 5.]
(d) BOUNDEDNESS use: the constraint that an integer O(x) has at most
    O(1) (concretely <= 101 after normalization) prime factors above
    R_+ = x^{1/100} is used twice: for (5.41) and for the i <= 101
    truncation of the inclusion-exclusion. This is the precise sense in
    which "boundedness" enters: not of omega itself, but of its very-large-
    prime part omega_{>R_+}.
(e) The shift pattern {r_{eps,h+K}} inherited from the dilation is what
    Theorem 3.1 must handle: two distinct shifted arguments n + r_{eps,h+K}
    and n + r_{eps',h+K} of 1-bounded multiplicative functions g_l --
    i.e., the dilation has been converted into a PAIR-correlation problem
    for multiplicative functions at distinct shifts, which is exactly the
    equidistributed case of Theorem 3.1 (Pilatte-type Elliott estimate).
    KAPPA_3 / VERY LARGE PRIMES (range p > R_+ = x^{1/100}) IS THE ONLY
    PLACE THEOREM 3.1 IS INVOKED IN SECTION 5 (p.55, subsection 5.14);
    large primes (5.13) needed only periodicity + (5.35); confirmed by
    grep: Theorem 3.1's occurrences inside Section 5 are at the (5.15)
    remark (p.47) and the invocation (p.55).

--------------------------------------------------------------------------
## PART 3. THE CONTRADICTION ENDGAME

What property of a rational number is refuted: NOT literal eventual
periodicity of binary digits, and not integrality of a single tail.
The refuted property is the TAIL CONGRUENCE SYSTEM: if
\sum_n omega(n)/2^n = a/q then for EVERY n
    q \sum_{h=1}^infty omega(n+h)/2^h = 0 (mod 1)     [(5.1), p.45]
(the q-scaled binary tail at every offset n is an integer). All of Section
5 manufactures from this a statistical impossibility. (Equivalently: (5.1)
says e( q \sum_{h} omega(n+h)/2^h ) = 1 identically in n; the proof shows
its expectation over a suitable random n has modulus bounded away from 1.)

Final chain with anchors:
1. Rationality => (5.1) for all n (Section 5 preamble + 5.1, p.44-45).
2. (5.1) + additivity identity + p | n => dilated congruences (5.2) with
   error delta_p(n) (5.3) (p.45).
3. Cube of primes p_eps (Lemma 5.2, p.50) + congruences (5.5) on n =>
   alternating identity (5.8); exponentiating: e(...) = 1 + O(sum of
   delta terms) (p.46).
4. Randomize n (5.6, p.51: uniform on [x/2,x] with (5.5), (5.33));
   expectations: (5.9) with kappa_1 error; truncate: kappa_2; factor over
   primes via (1.1): (5.12), E e(\sum_p X_p) = 1 + O(kappa_1) + O(kappa_2)
   (p.46).
5. Peel off deterministic small primes S_0 and exceptional S_2 (kappa_3):
   (5.15): |E e(\sum_{p in S_1} X_p)| = 1 + O(kappa_1 + kappa_2 + kappa_3)
   (p.47).
6. Compare to independent model (kappa_4, kappa_5):
   |\prod_{p in S_1} E e(X_p)| = 1 + \sum_{j=1}^5 O(kappa_j) (p.48).
7. kappa_1 ... kappa_5 = o(1) [(5.18), established in 5.7-5.14] and
   X_p = o(1) [(5.19), from (5.36)] => (5.20):
   \sum_{p in S_1} Var X_p << \sum_j kappa_j = o(1).
8. But the construction gives (5.21): \sum_{p in S_1} Var X_p >> 1
   (subsection 5.11, p.53).
9. VERBATIM (p.49): "Indeed, it is clear that (5.18), (5.20), and (5.21)
   will contradict each other for x large enough." This proves Theorem 5.1
   ex falso -- i.e., the assumed rationality is refuted; Theorem 1.3
   follows.
In one sentence: rationality forces the random phase e(\sum_p X_p) to
concentrate at 1 (modulus of expectation 1 - o(1)), while genuine
Erdos--Kac-type randomness of medium-prime divisor indicators forces a
variance >> 2^{-K} \sum_{medium p} 1/p >> 1, making |E e(...)| <= 
exp(-c \sum Var X_p) bounded away from 1: contradiction.

--------------------------------------------------------------------------
## PART 4. TRANSFER-RELEVANT OBSERVATIONS (extractor commentary)

[THIS ENTIRE PART IS COMMENTARY, NOT EXTRACTION. Statements about the
prime-index series S = \sum_n p_n / 2^n and the gap series
\sum_n g_n / 2^n, g_n = p_{n+1} - p_n, with tail
delta_n = \sum_{j>=1} g_{n+j} 2^{-j}, delta_{n+1} = 2 delta_n - g_{n+1},
are the extractor's observations for the downstream analysis. Anything not
sourced to the PDF is marked accordingly.]

Step-by-step analogue check (labels refer to Part 2 steps):

A. Step 0 + (5.1) (tail congruence for all offsets): AVAILABLE.
   If \sum g_n/2^n = a/q then q delta_n = q \sum_h g_{n+h}/2^h = 0 (mod 1)
   for all n -- same shift-by-n/multiply-by-2^n mechanism, using only
   geometric decay. The recursion delta_{n+1} = 2 delta_n - g_{n+1} is the
   exact analogue of the reindexing step. No obstruction here.

B. Step 1, dilation (5.2) via omega(pn) = omega(n) + 1 - 1_{p|n}:
   NO ANALOGUE -- THIS IS THE FIRST MISSING STEP.
   The entire dilation h -> ph rests on omega being an ADDITIVE function of
   its argument, so that the value at the dilated point pn is exactly
   expressible by the value at n (up to the bounded, sparse correction
   1 - 1_{p|n}, retired later as kappa_1). The gap coefficient g_n is
   indexed by prime COUNT, not by an integer with multiplicative
   structure; there is no known identity expressing g at a dilated index
   (g_{pn}, or g at the index of a dilated prime) in terms of g_n plus a
   controllable correction. Equivalently: omega's generating structure
   \sum_n omega(n) z^n = \sum_p z^p/(1-z^p) (additivity over p) has no
   counterpart for \sum_n p_n z^n. Without (5.2) there is no family of
   congruences indexed by a prime parameter, hence nothing for the cube /
   alternating-sum machinery to act on.

C. Step 2 (Gowers cube in shift space) and Step 6 / Lemma 5.2 (Hilbert
   cube of primes): DEPENDENT ON B, hence not reachable; but note the
   lemma itself is coefficient-agnostic (it is a statement about primes in
   [P/2, P] and would remain available as a tool if some substitute
   dilation existed).

D. Step 3, factorization E e(\sum_p X_p) via (1.1) omega = \sum_p 1_{p|.}:
   NO ANALOGUE. g_n admits no known decomposition into (approximately
   independent, individually small) arithmetically structured summands
   analogous to 1_{p | n + r}. One can write g_n as a count of integers
   between consecutive primes, but the resulting indicators (primality of
   individual integers near p_n) are exactly the objects whose joint
   distribution is prime-tuples-hard. [BACKGROUND-UNVERIFIED: standard
   status of prime tuples; consistent with the paper's own remark (Section
   1.3, p.4) that quantitative prime tuples would give "quite good control"
   on consecutive omega values -- for gaps the corresponding control IS the
   tuples conjecture.]

E. Step 5 + Steps 10-12 (Erdos--Kac variance layer): PARTIAL ANALOGUE AT
   BEST. The lower bound (5.21) comes from Bernoulli(1/p) divisor
   indicators with variance asymp 2^{-K}/p summing over medium primes
   (Mertens). For gaps, variance heuristics (Cramer/Gallagher-type)
   predict fluctuation of \sum_h g_{n+h}/2^h but no unconditional theorem
   supplies BOTH an upper bound forcing phase concentration AND a matching
   variance lower bound of the required shape. [BACKGROUND-UNVERIFIED.]
   Note also the endgame consumes E X_p and E X_p^2 to accuracy
   x^{-1+o(1)} via equidistribution in APs (5.35), which for gap data
   would demand prime-distribution inputs far beyond current unconditional
   results. [BACKGROUND-UNVERIFIED.]

F. Steps 13-15 (kappa_3, Theorem 3.1 for very large primes): NO ANALOGUE.
   The paper's pair-correlation input is for 1-BOUNDED MULTIPLICATIVE
   functions g_l at two distinct shifts (equidistributed case of Theorem
   3.1). The gap series has no reformulation in terms of bounded
   multiplicative functions; the corresponding correlation objects would
   be shifted prime-indicator correlations, i.e., prime tuples territory
   again. The paper itself states the boundary of its technology in
   adjacent problems: triple correlations are "not ... within current
   technology" (Remarks 4.2, p.44), and small-k barrier problems are "of
   comparable difficulty to the prime tuples conjecture" (Remark 1.2,
   p.3).

G. Endgame (Part 3): the contradiction template (tail congruences vs.
   anti-concentration of a random model) is in principle
   coefficient-agnostic: it needs (i) a family of exact congruences
   generated from rationality, rich enough to be averaged; (ii) an
   unconditional distributional theorem showing the averaged phase cannot
   concentrate. For S, (i) exists only in the single-parameter form A
   (offsets n; no second, dilation-type parameter), and (ii) would require
   unconditional anti-concentration for weighted gap sums \sum_h g_{n+h}/2^h
   mod 1/q -- not available. [BACKGROUND-UNVERIFIED.]

FIRST STEP WITH NO ANALOGUE: Step 1 = subsection 5.1's dilation identity
(5.2), which requires the additivity identity omega(pn) = omega(n) + 1 -
1_{p|n}. Everything after (5.2) -- the cube (5.4)-(5.8), the prime-indexed
random variables (5.13), the variance dichotomy (5.20) vs (5.21), and the
Theorem 3.1 input -- is built on the two-parameter (offset n, dilation
p_eps) congruence family that (5.2) creates. The prime-index/gap series has
the offset parameter only. In the extractor's assessment the method
transfers from (5.1) no further than (5.1) itself without a new idea
supplying either a dilation-type symmetry for g_n or a substitute second
parameter family of exact congruences.

[END OF FILE]
