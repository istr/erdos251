# EXTRACTION: Hildebrand and Maier, "Gaps Between Prime Numbers"

Source (only evidence base): /home/istr/pro/erdos251/dossier/S0002-9939-1988-0958032-5.pdf
Journal id: PROCEEDINGS OF THE AMERICAN MATHEMATICAL SOCIETY, Volume 104,
Number 1, September 1988 (article id S0002-9939-1988-0958032-5; copyright
line "(c)1988 American Mathematical Society 0002-9939/88 $1.00 + $.25 per
page"). Authors as printed: ADOLF HILDEBRAND AND HELMUT MAIER (Communicated
by Larry J. Goldstein). 9 pages (printed pages 1-9). Footnote p. 1:
"Received by the editors July 23, 1987 and, in revised form, August 26,
1987. 1980 Mathematics Subject Classification (1985 Revision). Primary
11N05. Work supported by NSF grants."

Transcription conventions: ASCII only. Diacritics transliterated (Erdos,
Westzynthius umlaut dropped: "Uber", Theorie). Math in LaTeX-like ASCII:
\asymp for the "same order" symbol, << and >> Vinogradov, <<_g means the
implied constant depends on g, \equiv for congruence, \phi(q) Euler phi
(paper prints varphi), \lambda(...) Lebesgue measure, d_n = p_{n+1} - p_n,
P(z) = prod_{p <= z} p, V(z) = prod_{p <= z}(1 - 1/p), log_k n = k times
iterated logarithm (paper's Section 4 usage). t-bar written \bar{t}.
Anchors are the paper's equation numbers (1)-(21), lemma numbers 1-4, and
section numbers; page numbers (printed = PDF page) secondary. The paper was
read from rasterized page images (older AMS typesetting); uncertain glyphs
carry inline [TRANSCRIPTION-UNSURE] flags.

Everything up to the final section is EXTRACTION (what the paper says).
Commentary appears ONLY in the final marked section.

---

## 1. ABSTRACT AND MAIN THEOREM (verbatim)

Abstract (p. 1), verbatim:

> "ABSTRACT. Let d_n = p_{n+1} - p_n denote the nth gap in the sequence of
> primes. We show that for every fixed integer k and sufficiently large T
> the set of limit points of the sequence {(d_n/log n, ...,
> d_{n+k-1}/log n)} in the cube [0,T]^k has Lebesgue measure >= c(k)T^k,
> where c(k) is a positive constant depending only on k. This generalizes a
> result of Ricci and answers a question of Erdos, who had asked to prove
> that the sequence {d_n/log n} has a finite limit point greater than 1."

Setup for the theorem (Section 1, p. 2), verbatim:

> "The purpose of this note is to prove the following theorem, which
> settles Erdos' question in the affirmative. Roughly speaking, the theorem
> asserts that a positive proportion of all real numbers belong to S, and
> that an analogous result holds for the limit points (in R^k) of the
> sequence
> (5)  ( d_n/log n, ..., d_{n+k-1}/log n )   (n = 1,2,3,...)."

THE THEOREM (Section 1, p. 2), verbatim:

> "THEOREM. Let k be a positive integer, and let S^{(k)} be the set of
> limit points in R^k of the sequence (5). Then we have, for any
> sufficiently large number T,
>   \lambda(S^{(k)} cap [0,T]^k) >= c(k)T^k,
> where \lambda(...) denotes the Lebesgue measure in R^k and c(k) is a
> positive constant depending only on k."

COROLLARY (Section 1, p. 2), verbatim, with its lead-in:

> "The theorem immediately implies that the sequence {d_n/log n} has
> arbitrarily large finite limit points, thus answering the above-mentioned
> question of Erdos. In fact, noting that the set of points (x_1,...,x_k)
> in [0,T]^k satisfying min_{1<=i<=k} x_i < \epsilon T has Lebesgue measure
> < k \epsilon T^k, we obtain the following"

> "COROLLARY. Let k be a positive integer and let \epsilon = \epsilon(k) =
> c(k)/k, where c(k) is the constant in the theorem. Then, for every
> sufficiently large T, the sequence (5) has a limit point in
> [\epsilon T, T]^k."

Immediately after (p. 2), verbatim: "In particular, we obtain (2) as a
consequence of the theorem."

---

## 2. INTRODUCTION CONTEXT (Section 1): the limit-point set S

Verbatim (p. 1):

> "Let p_n denote the nth prime, and let d_n = p_{n+1} - p_n be the nth gap
> between consecutive primes. The prime number theorem implies that p_n ~
> n log n, as n -> infty. Hence the average size of a gap d_n is log n.
> However, there exist gaps that are much larger than log n. In fact, as
> was shown by Westzynthius [9], we have
> (1)  limsup_{n->infty} d_n / log n = infty."

> "Erdos [2] proved that there exist infinitely many pairs of consecutive
> 'large' gaps (d_n, d_{n+1}). In [5] the second author extended this
> result to an arbitrary number of consecutive gaps, showing that for any
> k >= 1
> (2)  limsup_{n->infty} min(d_n, ..., d_{n+k-1}) / log n = infty."

[Reference [5] is H. Maier, "Chains of large gaps between consecutive
primes", Adv. in Math. 39 (1981), 257-269 -- the "chains" paper this note
generalizes; see References, p. 9.]

> "Our knowledge about small gaps is less satisfactory. As a counterpart to
> (1), one might expect that
> (3)  liminf_{n->infty} d_n / log n = 0.
> This would follow, if the twin prime conjecture were true. The prime
> number theorem trivially implies that the 'lim inf' in (3) is at most 1.
> Erdos [1] was the first to obtain
> (4)  liminf_{n->infty} d_n / log n <= c
> for some constant c strictly less than 1. A number of authors
> subsequently reduced the value of c in (4), the current record being
> c = 0.248... [6]. A proof of (3), however, seems to be still out of
> reach."

> "Let S denote the set of limit points of the sequence {d_n/log n}. A
> natural conjecture is that S consists of all nonnegative real numbers and
> the point infty. By (1), infty is indeed a limit point of S, and Erdos'
> result (4) implies that S contains a real number strictly less than 1.
> Erdos and Ricci [8] proved that S has in fact positive Lebesgue measure.
> Erdos recently asked whether S contains a real number greater than 1."

(The last block spans the p. 1 / p. 2 break.)

---

## 3. METHOD OVERVIEW (the Maier matrix, as the authors describe it)

Verbatim (Section 1, p. 2):

> "For the proof of the theorem we shall use a method that was introduced
> by the second author in [5] to prove (2). The key idea is to construct a
> matrix, whose rows are intervals of consecutive integers, and which
> contains exceptionally few primes. The gaps between consecutive primes in
> the rows of this matrix are therefore larger than normal. One can in fact
> prescribe the ratio between the average size of a gap in the matrix and
> that of a 'normal' gap by an appropriate choice of parameters. By letting
> this ratio be of order T, one obtains a large number of gaps d_n, for
> which the ratio d_n/log n is not greater than T, but also not
> substantially smaller than T. Using a sieve result, one can moreover show
> that these ratios actually fill out a positive proportion of the interval
> [0,T]. In this way, one obtains the assertion of the theorem for the case
> k = 1. A similar, though technically more complicated, argument yields
> the general case."

---

## 4. THE FOUR LEMMAS (Section 2, all verbatim)

Section opening (p. 2), verbatim: "The proof of the theorem follows
closely the argument of [5]. In this section we state four lemmas, all of
which have their counterparts in [5]. We shall give a detailed proof only
for the last lemma; the first three lemmas are obtained by minor
modifications of the proofs in [5]."

Good modulus definition (p. 2), verbatim:

> "Given a constant C > 0, we call an integer q > 1 a good modulus, if
> L(s, \chi) != 0 for all nonprincipal characters \chi mod q and all
> s = \sigma + it satisfying
>   \sigma > 1 - C / log(q(|t| + 1))."

Lead-in (p. 2), verbatim: "The following result can be derived from a
large sieve type estimate of Gallagher [3] (cf. [5, Lemma 2])."

> "LEMMA 1. Let q be a good modulus. Then we have, uniformly for x >= q^D
> and (a, q) = 1,
>   \pi(2x, q, a) - \pi(x, q, a) >> x / (\phi(q) log x).
> Here D is a constant > 1 that depends only on the constant C implicit in
> the definition of a good modulus."

(p. 3, verbatim): "We shall apply this result with moduli q of the form
P(z) = prod_{p <= z} p. From Page's theorem on exceptional characters one
can deduce (cf. [5, Lemma 1]):"

> "LEMMA 2. If C is a sufficiently small constant, then there exist
> arbitrarily large values z, for which q = P(z) is a good modulus in terms
> of C."

Lead-in (p. 3), verbatim: "The next lemma gives an upper bound for the
number of prime g-tuples in arithmetic progressions. It can be deduced from
any sufficiently general sieve upper bound, for example [4, Theorem 2.3].
The lemma generalizes Lemma 3 of [5], which corresponds to the case g = 2."

> "LEMMA 3. Let g be a fixed positive integer. Let z >= 2 and s_1, ..., s_g
> be integers satisfying
>   0 < |s_i - s_j| <= z^2   (1 <= i < j <= g).
> Then, for any R >= 2, we have
>   #{1 <= r <= R : rP(z) + s_i prime for i = 1,...,g}
>     <<_g R / (V(z) log R)^g,
> where
>   V(z) = prod_{p <= z} (1 - 1/p)
> and the implied constant depends only on g."

Lead-in (p. 3), verbatim: "Our final lemma is one of the key ingredients in
our argument. It guarantees the existence of intervals in which the number
of integers n satisfying (n, P(z)) = 1 is by a prescribed factor \delta
smaller than the expected number. A similar result was proved in
[5, Lemma 6]."

> "LEMMA 4. Let K >= 2 and 0 < \delta < 1 be fixed constants. Then, for all
> sufficiently large numbers z, there exists a number y, 1 <= y <= 2P(z),
> such that the estimate
> (6)  #{y_1 < n <= y_2 : (n, P(z)) = 1} \asymp \delta V(z)(y_2 - y_1)
> holds for all y_1, y_2 satisfying
> (7)  y <= y_1 < y_2 <= y + Kz,   y_2 - y_1 >= z / log z.
> Here the constants implied in the symbol '\asymp' are absolute."

NOTE (extraction fact, not commentary): the Buchstab function and any
Buchstab-type oscillation theorem are NOT mentioned anywhere in this paper.
Lemma 4's role is filled by an explicit congruence construction (next).

Proof of Lemma 4 (pp. 3-5), load-bearing steps verbatim:

> "PROOF. Let K, \delta and z be given as in the lemma and set
> K_1 = 2K^{1/\delta}. We shall prove the assertion of the lemma with
> y = N + Kz, where N is the least positive solution to the system of
> congruences
>   N \equiv -1 mod p   (p <= K_1),
>   N \equiv  0 mod p   (K_1 < p <= z)."

> "The definition of N implies that for any integer n, (n, P(z)) = 1 holds
> if and only if m = n - N satisfies the conditions
> (*)  { m !\equiv 1 mod p  (p <= K_1),
>      { m !\equiv 0 mod p  (K_1 < p <= z)."

(Paraphrase, marked as such: substituting x_i = y_i - N turns (6) into
(6)' #{x_1 < m <= x_2 : (*)} \asymp \delta V(z)(x_2 - x_1) and (7) into
(7)' Kz <= x_1 < x_2 <= 2Kz, x_2 - x_1 >= z/log z.)

> "To prove (6)', we note that if z > 2K, as we may assume, then a positive
> integer m <= 2Kz satisfying (*) is either composed entirely of prime
> factors <= K_1, or of the form
> (**)  m = dp,  p > z,  dp !\equiv 1 mod p'  (p' <= K_1)."

> "The first alternative holds for at most (log(Kz))^A integers m <= Kz,
> with a suitable A = A(K_1)." [TRANSCRIPTION-UNSURE: exponent glyph A and
> its argument (K_1) are small at rendering resolution.]

Counting the second alternative (p. 4), verbatim:

> "#{x_1 < m <= x_2 : (**)} = sum_{d <= x_2/z} S(d),
> where
>   S(d) = #{max(x_1/d, z) < p <= x_2/d : dp !\equiv 1 mod p' (p' <= K_1)}."

> "For d <= x_1/z (<= 2K <= K_1), a straightforward application of the
> Eratosthenes sieve and the prime number theorem for arithmetic
> progressions shows that
>   S(d) \asymp prod_{p' <= K_1, p' !| d} (1 - 1/p') (x_2 - x_1)/(d log z)
>        = V(K_1) (x_2 - x_1)/(\phi(d) log z)
>        \asymp V(z)(x_2 - x_1)/(\phi(d) log K_1),
> provided z is sufficiently large and x_1 and x_2 satisfy (7)'. Moreover,
> the upper bound implicit in this estimate remains valid for
> x_1/z < d <= x_2/z. Since, by (7)', x_1/z and x_2/z are both of order K,
> we obtain
>   sum_{d <= x_2/z} S(d)
>     \asymp ( sum_{d <= x_1/z} 1/\phi(d) ) V(z)(x_2 - x_1)/log K_1
>     \asymp (log K / log K_1) V(z)(x_2 - x_1)
>     \asymp \delta V(z)(x_2 - x_1),"

[TRANSCRIPTION-UNSURE: the middle members of the last two displays carry
small subscripts; the chain endpoints (\asymp \delta V(z)(x_2 - x_1)) are
clearly legible. Note log K / log K_1 = log K / ((1/\delta) log K + log 2)
\asymp \delta, which is the point of the choice K_1 = 2K^{1/\delta}.]

> "using the well-known estimate
>   sum_{d <= u} 1/\phi(d) \asymp log u   (u >= 2)
> and the definition of K_1. This proves (6)' and hence the lemma." (p. 5)

---

## 5. PROOF OF THE THEOREM (Section 3): full anatomy

### 5.1 Reduction to box counting

Opening (p. 5), verbatim:

> "We fix a positive integer k and a real number T, which we may assume to
> be sufficiently large. In what follows, the constants implied in the
> symbol '<<' are allowed to depend on k, but not on T."

> "For \epsilon > 0, define an \epsilon-neighborhood of S^{(k)} as
>   S_\epsilon^{(k)} = { (t_1,...,t_k) in R^k : max_{i=1}^{k}
>     |t_i - \bar{t}_i| <= \epsilon for some (\bar{t}_1,...,\bar{t}_k)
>     in S^{(k)} }."

> "We shall show that for every integer N >= 1 the bound
> (8)  \lambda(S_{1/N}^{(k)} cap [0,T]^k) >= c(k)T^k
> holds with a positive constant c(k) independent of N and T."
> [TRANSCRIPTION-UNSURE: subscript read as 1/N in all three occurrences on
> p. 5; since the boxes below have side T/N, a subscript T/N would fit the
> good-box inclusion better; transcribed as printed.]

> "Since the sets S_{1/N}^{(k)} (N = 1,2,3,...) form a decreasing sequence
> of sets, whose intersection is the closure of S^{(k)} and hence S^{(k)}
> itself (since S^{(k)}, as a set of limit points, is a closed set), we
> have
>   \lambda(S^{(k)} cap [0,T]^k)
>     = lim_{N->infty} \lambda(S_{1/N}^{(k)} cap [0,T]^k).
> Thus, the asserted bound follows from the bound (8), and it remains to
> prove the latter one."

> "We fix an integer N >= 1 and divide the cube [0,T]^k into N^k boxes
> (9)  B(n) = [ ((n_1 - 1)/N) T, (n_1/N) T ] x ... x
>             [ ((n_k - 1)/N) T, (n_k/N) T ]
>             (n = (n_1,...,n_k), 1 <= n_i <= N)."
> [TRANSCRIPTION-UNSURE: whether the interval endpoints are printed closed
> or half-open; the subsequent sentence "the boxes B(n) are disjoint apart
> from a set of volume ... zero" is consistent with closed boxes.]

> "We call a box good if it contains a point of S^{(k)}. It is clear from
> the definition of S_\epsilon^{(k)} that every good box is contained in
> the set S_{1/N}^{(k)} cap [0,T]^k. Since the boxes B(n) are disjoint
> apart from a set of volume (i.e., Lebesgue measure in R^k) zero, and each
> of these boxes has volume (T/N)^k, we have
>   \lambda(S_{1/N}^{(k)} cap [0,T]^k) >= #{good boxes} (T/N)^k.
> Thus, to obtain (8), it suffices to show
> (10)  #{boxes B(n) containing a point of S^{(k)}} >= c(k) N^k."

### 5.2 The matrix construction

(p. 5), verbatim:

> "We now construct the matrix mentioned in the introduction. We fix a
> number z, for which q = P(z) is a good modulus in the sense of Lemma 2.
> The lemma guarantees the existence of arbitrarily large numbers z with
> this property. We then apply Lemma 4 with K = T and \delta = c/T, where c
> is a constant depending on k that will be specified presently. The
> hypotheses of the lemma are satisfied, provided T > max(2, c) and z is
> sufficiently large in terms of T, as we may assume."

(p. 6), verbatim:

> "We therefore obtain a positive number y <= 2P(z), such that (6) holds,
> whenever (7) is satisfied. We now define an integer matrix A = (a_{rs})
> by
>   a_{rs} = rP(z) + s   (R < r <= 2R,  y < s <= y + Tz),
> where
>   R = P(z)^{D-1},
> D being the constant of Lemma 1, applied with q = P(z)."

Prime counting in the matrix (p. 6), verbatim:

> "We first estimate from below the number of primes in A. The columns in
> the matrix A are the arithmetic progressions
>   {x < n <= 2x : n \equiv s mod q},   y < s <= y + Tz,
> where
>   q = P(z),   x = P(z)^D = RP(z).
> Only columns with (s, q) = (s, P(z)) = 1 can contain primes. By Lemma 4,
> the number of such columns is
>   \asymp \delta V(z) Tz = c V(z) z."

> "Moreover, by Lemma 1 and our assumption that q = P(z) is a good modulus,
> the number of primes in each of these columns is
>   >> x/(\phi(q) log x) = x/(P(z) V(z) log P(z)^D) \asymp R/(V(z) z),
> since
>   log P(z)^D = D sum_{p <= z} log p \asymp z."

> "Hence the entire matrix A contains
>   >> c V(z) z * R/(V(z) z) = cR
> primes, where the implied constant is absolute. If we now choose the
> constant c sufficiently large, then we have
> (11)  #{primes in A} >= 3kR."

Good rows and consecutive-prime tuples (p. 6), verbatim:

> "By (11), a row in A contains on average at least 3k primes. Call a row
> 'good' if it contains at least 2k primes, and 'bad' otherwise. Since the
> matrix A has [2R] - [R] <= R + 1 rows, at most (R + 1)(2k - 1) of the
> primes in A can be located in bad rows. In view of (11), we therefore
> have
> (12)  #{primes in good rows of A} >= 3kR - (2k - 1)(R + 1) >= kR,
> provided R >= 2k, as we may assume."

> "Next, we estimate the number of (k+1)-tuples
> (13)  (a_{r s_1}, ..., a_{r s_{k+1}}) = (p_n, ..., p_{n+k})
> of consecutive primes in the rows of our matrix. A row with m > k primes
> contains exactly m - k such (k+1)-tuples. If the row is good, i.e., if
> m >= 2k, then m - k >= m/2, so that the number of (k+1)-tuples is at
> least half the number of primes in the row. Thus, using (12), we see that
> (14)  #{tuples (13) in A} >= (1/2) #{primes in good rows of A}
>         >= (1/2) kR."

### 5.3 Normalized difference tuples and the box-hitting count

(p. 7), verbatim:

> "With each of the (k+1)-tuples (13) we can associate a k-tuple of
> differences between consecutive primes
>   (a_{r s_2} - a_{r s_1}, ..., a_{r s_{k+1}} - a_{r s_k})
>     = (s_2 - s_1, ..., s_{k+1} - s_k)
>     = (p_{n+1} - p_n, ..., p_{n+k} - p_{n+k-1})
>     = (d_n, ..., d_{n+k-1})
> as well as a 'normalized' k-tuple of differences
> (15)  ( (s_2 - s_1)/log x, ..., (s_{k+1} - s_k)/log x )
>     = ( d_n/log x, ..., d_{n+k-1}/log x )."

> "Since for every tuple (13)
> (16)  y < s_1 < ... < s_{k+1} <= y + Tz
> and
>   log x = D log P(z) >= z,
> if, as we may assume, z is sufficiently large, each of the tuples (15) is
> contained in the cube [0,T]^k, and hence in one of the N^k boxes B(n)
> defined in (9). We shall show
> (17)  #{boxes B(n) containing a k-tuple (15)} >> N^k,
> where the implied constant depends only on k."

The z -> infty limit step (p. 7), verbatim:

> "Having proved (17), the proof of (10), and hence that of the theorem,
> can be easily completed. To this end, we repeat the above construction
> with a sequence of values z tending to infinity. By choosing a suitable
> subsequence and using (17), we obtain a fixed collection of >> N^k boxes
> B(n), each of which contains a tuple (15) for all values z in this
> subsequence. Hence, each of those boxes contains a limit point of the
> tuples (15). Since the elements a_{rs} of our matrix A have order of
> magnitude x, we have, for any k-tuple (15) associated with a
> (k+1)-tuple (13),
>   log x ~ log a_{r s_1} = log p_n ~ log n.
> Thus, every limit point of the tuples (15) is also a limit point of the
> tuples (5), hence belongs to S^{(k)}, and (10) follows."

### 5.4 The per-box upper bound (the sieve step)

(p. 7), verbatim:

> "To prove (17), we estimate from above the number of (k+1)-tuples (13),
> for which the associated tuple (15) falls into a fixed box B(n), i.e.,
> which satisfies
> (18)  ((n_i - 1)/N) T log x <= s_{i+1} - s_i <= (n_i/N) T log x
>         (i = 1,...,k)."

> "We shall show that, for each of the boxes B(n),
> (19)  #{tuples (13) in A satisfying (18)} << R N^{-k},
> with the implied constant depending only on k. Since, by (14), the matrix
> A contains >> R (k+1)-tuples (13), we see that (19) implies (17)."

> "To obtain (19), we note that the number of (k+1)-tuples to be estimated
> is at most equal to the number of tuples (a_{r s_1}, ..., a_{r s_{k+1}})
> in our matrix, that consist entirely of primes (though not necessarily
> consecutive primes), and where s_1, ..., s_{k+1} are subject to (16) and
> (18). Such tuples of primes can only exist, if
> (20)  (s_i, P(z)) = 1   (i = 1,...,k+1)."

(p. 8), verbatim:

> "For fixed s_1,...,s_{k+1} satisfying (16), (18) and (20), the number of
> such tuples is by Lemma 3
>   #{R < r <= 2R : a_{r s_i} = rP(z) + s_i prime for i = 1,...,k+1}
>     << R/(V(z) log R)^{k+1} \asymp R/(V(z) z)^{k+1}."

> "Moreover, the number of tuples (s_1,...,s_{k+1}) that satisfy (16), (18)
> and (20) can be estimated by Lemma 4. To this end, we note that the
> conditions (16) and (18) restrict s_1 to the interval (y, y + Tz], and
> each of the numbers s_i, 2 <= i <= k+1, to a subinterval of (y, y + Tz]
> of length (T log x)/N \asymp Tz/N (which is >= z/log z for sufficiently
> large z). Lemma 4 therefore gives
>   #{(s_1,...,s_{k+1}) : (16), (18), (20)}
>     << (\delta Tz V(z)) ( \delta (T/N) z V(z) )^k
>     = (c z V(z))^{k+1} / N^k."

> "Altogether, the number of (k+1)-tuples to be estimated in (19) is
> bounded by
>   << R/(V(z) z)^{k+1} * (c z V(z))^{k+1}/N^k \asymp R/N^k,
> as required.
> The proof of the theorem is now complete."

(Paraphrase, marked as such: the final \asymp absorbs c^{k+1} into the
k-dependent constant; c depends only on k via (11).)

---

## 6. CONCLUDING REMARKS (Section 4, verbatim)

> "Rankin [7] proved a stronger form of (1), namely
>   limsup_{n->infty} d_n / L_0(n) > 0
> with
>   L_0(n) = log n log_2 n log_4 n / (log_3 n)^2,
> where log_k n denotes the k times iterated logarithm. An analogous
> strengthening of (2) was proved in [5]. Thus, (1) and (2) remain valid,
> when the function log n is replaced by any function L(n) satisfying
> (21)  log n <= L(n) = o(L_0(n))   (n -> infty).
> One might therefore ask if one can similarly replace log n by L(n) in the
> definition of the set S^{(k)} in the theorem. By modifying slightly the
> present proof and using some additional arguments from [5] and [7], one
> can indeed show that the result remains valid with any slowly oscillating
> function L(n) satisfying (21) in place of log n."

> "It is an open problem to find a specific real number that is a limit
> point of the sequence {d_n/log n}. Our method is, like earlier methods,
> nonconstructive and yields only the existence of (sufficiently many)
> limit points. To show that a given real number is a limit point of
> {d_n/log n} would probably require completely new ideas."

---

## 7. REFERENCES (pp. 8-9, as printed, diacritics transliterated)

1. P. Erdos, On the difference between consecutive primes, Quart. J.
   Oxford 6 (1935), 124-128.
2. ---, Problems and results on the difference of consecutive primes,
   Publ. Math. Debrecen 1 (1949-1950), 33-37.
3. P. X. Gallagher, A large sieve density estimate near sigma = 1, Invent.
   Math. 11 (1970), 329-339.
4. H. Halberstam and H.-E. Richert, Sieve methods, Academic Press, New
   York, 1974.
5. H. Maier, Chains of large gaps between consecutive primes, Adv. in
   Math. 39 (1981), 257-269.
6. ---, Small differences between prime numbers, Preprint.
7. R. A. Rankin, The difference between consecutive prime numbers, J.
   London Math. Soc. 13 (1938), 242-247.
8. G. Ricci, Recherches sur l'allure de la suite {(p_{n+1} - p_n)/
   log p_n}, Colloque sur la Theorie des Nombres, Bruxelles, 1955,
   pp. 93-106. [TRANSCRIPTION-UNSURE: French title wording at small size.]
9. E. Westzynthius, Uber die Verteilung der Zahlen, die zu den n ersten
   Primzahlen teilerfremd sind, Comm. Phys. Math. Helsingfors 25 (1931),
   1-37.

Affiliations (p. 9): Department of Mathematics, University of Illinois,
Urbana, Illinois 61801; Department of Mathematics, University of Georgia,
Athens, Georgia 30602.

---

## COMMENTARY (assessment, NOT extraction)

### Focus 1: the exact main statement

The positive-measure set is S^{(k)} cap [0,T]^k, where S^{(k)} is the set
of LIMIT POINTS in R^k of the sequence (5) of normalized k-tuples
(d_n/log n, ..., d_{n+k-1}/log n) -- all k coordinates normalized by the
SAME log n, n the index of the leftmost gap (Theorem, p. 2; sequence (5),
p. 2). Quantifiers: k is a fixed positive integer chosen first; then "for
any sufficiently large number T" the measure bound \lambda >= c(k)T^k
holds, with c(k) depending only on k (and, by the Section 3 opening, all
implied constants may depend on k but not on T; the threshold "T >
max(2,c)" on p. 5 makes the T-threshold k-dependent since c = c(k)). The
project's shorthand "chains of normalized gaps, positive measure in
[0,T]^k" should be sharpened to: the LIMIT-POINT set of chains has measure
>= c(k)T^k in [0,T]^k. Effectivity: c(k) is never computed; the paper
itself declares the method "nonconstructive" and "yields only the
existence of (sufficiently many) limit points" (Section 4, p. 8). The
Corollary (p. 2) upgrades this to a limit point in [\epsilon T, T]^k with
\epsilon = c(k)/k -- all coordinates simultaneously large -- but at an
unspecified location.

### Focus 2: matrix anatomy and the (absent) Buchstab function

The anatomy, step by step (all anchors above): (a) pick z with q = P(z) a
good modulus -- Lemma 2, from Page's theorem; this is where the special
sparse z-sequence enters. (b) Lemma 4 with K = T, \delta = c/T builds a
translate (y, y + Tz] of prescribed P(z)-coprime DEFICIENCY: every
subinterval of length >= z/log z holds \asymp \delta V(z) x (expected
count) coprime residues -- proved by the explicit CRT construction N
\equiv -1 mod p (p <= K_1), N \equiv 0 mod p (K_1 < p <= z), K_1 =
2K^{1/\delta} (Section 4 above, pp. 3-5). (c) The matrix a_{rs} = rP(z)+s,
R < r <= 2R = 2P(z)^{D-1}, y < s <= y + Tz (p. 6): columns are APs mod
P(z) over (x, 2x], x = P(z)^D; \asymp cV(z)z live columns (Lemma 4) times
>> R/(V(z)z) primes per live column (Lemma 1) gives (11) >= 3kR primes,
hence (14) >= kR/2 chains of k consecutive gaps inside rows. (d) Each
chain's normalized gap tuple (15) lands in [0,T]^k since gaps <= Tz <=
T log x (16). (e) The sieve upper bound: per fixed column-tuple, Lemma 3
caps prime tuples by << R/(V(z)z)^{k+1}; Lemma 4's upper half caps
admissible column-tuples per box by (czV(z))^{k+1}/N^k; product (19) <<
R/N^k per box. (f) (14) + (19) force >> N^k hit boxes (17); a diagonal
subsequence in z makes >> N^k boxes hit for all z, so each holds a limit
point; log x ~ log n (p. 7) converts matrix normalization to the log n of
(5). On the focus question's premise: the Buchstab function and any
oscillation result for it are NOT FOUND in this text -- no occurrence on
any of the 9 pages. Its role in later Maier-method papers (short-interval
irregularities) is here played by Lemma 4, which is stronger for this
purpose: the density distortion \delta is PRESCRIBED (any fixed 0 < \delta
< 1), not inherited from Buchstab oscillation, at the price that the
distortion lives at specific translates y determined by CRT, inside the
special progression structure mod P(z).

### Focus 3: what is PRESCRIBED vs what is only COUNTED

Prescribed: exactly one scalar -- "the ratio between the average size of a
gap in the matrix and that of a 'normal' gap" (method paragraph, p. 2),
set to order T via \delta = c/T; plus the ambient cube [0,T]^k (16). Also
the normalization function has slack: any slowly oscillating L(n) with
log n <= L(n) = o(L_0(n)) works ((21), Section 4). Counted, not
prescribed: everything else. WHICH >> N^k boxes are hit is purely
existential ((17)); the method cannot force a nominated box, a specific
gap value, or a gap word at a nominated position/index n. The paper is
explicit that this is structural, not a presentational gap: "It is an open
problem to find a specific real number that is a limit point ... Our
method is, like earlier methods, nonconstructive ... To show that a given
real number is a limit point of {d_n/log n} would probably require
completely new ideas" (Section 4, p. 8). Note the asymmetry of the two
counting directions: the only LOWER bounds used are for total primes in
APs (Lemma 1) -- never for a prescribed pattern -- while per-pattern
control is an UPPER sieve bound (Lemma 3), which is parity-free. Pattern
diversity is then forced by global-lower-plus-per-class-upper ((14) vs
(19)). This sidesteps the parity obstruction entirely because no
prime-tuple lower bound is ever invoked.

### Focus 4: uniformity in k

k is fixed before all other parameters; there is NO explicit k = k(x)
range anywhere -- NOT FOUND in this text. The k-dependence enters at
least through: c = c(k) chosen "sufficiently large" so that (11) holds
(the absolute implied constant in >> cR forces c \asymp k); T > max(2, c)
(p. 5); R >= 2k (p. 12 step, p. 6); Lemma 3's implied constant <<_g with
g = k+1 (p. 3), whose growth in g is not tracked ("can be deduced from any
sufficiently general sieve upper bound"); and the Section 3 declaration
that all << constants may depend on k (p. 5). Moreover z must be
"sufficiently large in terms of T" (p. 5) and x = P(z)^D, so the theorem
is a fixed-k statement along a sparse implicit x-sequence. Nothing here
supports depth k growing with x, let alone k \asymp log_2 log x.

### Assessment against the exchange-configuration target

What the machinery CAN supply (unconditionally, fixed depth): within one
matrix at scale x = P(z)^D, it produces >= kR/2 chain sites (14), spread
over >> N^k boxes (17) with a per-box cap << R/N^k (19). Since R -> infty
while N, k stay fixed, pigeonhole over at most N^k occupied boxes yields
>= (kR/2)/N^k sites in SOME single box: many pairs of sites in (x, 2x]
whose entire k-word of normalized gaps agrees coordinatewise within T/N.
Further (extractor's arithmetic on top of (17), not in the paper): the hit
boxes have density >= c'(k) in the discrete cube {1..N}^k, so some line in
the middle-coordinate direction carries >= c'(k)N hit boxes, giving two
sites whose prefix and suffix coordinates agree within T/N each while the
middle normalized gaps differ by >= (c'(k)N - 1)(T/N) \asymp c'(k)T --
i.e., a matched-window pair with a dominant middle difference, with
dominance ratio \asymp c'(k)N tunable via N (c(k) is independent of N and
T, (8)). This is a genuine variability supply that plain pigeonhole cannot
see: blocker (i) is addressed by exactly the (14)-versus-(19) two-sided
count, and blocker (ii) is bypassed because only Lemma 3 upper bounds
touch patterns. Three hard caps remain. (1) DEPTH: everything is fixed-k;
at J, K \asymp log_2 log x the constants c(k), <<_{k+1} (Lemma 3), R >=
2k, T > c(k) are unquantified and the paper offers no rates -- the
depth-circularity of blocker (iii) reappears here as k-nonuniformity, and
this text does not break it. (2) RESOLUTION: matching is in units of
log x; per-coordinate absolute mismatch is \asymp (T/N) log x -> infty, so
exact gap-word equality, or 2-adically controlled mismatch, is not
obtainable from box membership; "matched windows" are only
approximate-ratio windows. (3) INDEX CONTROL: a site is located only via
p_n in (x, 2x]; the index n itself -- which sets the weight 2^{-n} in S =
sum p_n/2^n -- floats in a range of \asymp x/log x consecutive indices,
and the two same-box sites come at uncontrolled distinct indices; nothing
in the construction couples the site's gap word to its index. Bottom line:
this paper contributes the strongest available UNCONDITIONAL
abundance-plus-variability template at fixed depth (and the clean
structural lesson: force diversity via per-pattern sieve UPPER bounds
against a global prime LOWER bound), but it neither prescribes words nor
scales in depth, and its own Section 4 (p. 8) states the prescription
barrier as an open problem.
