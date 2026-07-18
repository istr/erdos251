# EXTRACTION: Granville-Lumley, "Primes in Short Intervals: Heuristics and Calculations"

Source (only evidence base): /home/istr/pro/erdos251/dossier/2009.05000v3.pdf
arXiv:2009.05000v3 [math.NT] 3 May 2021. Authors: Andrew Granville and Allysa
Lumley (Universite de Montreal / Centre recherche mathematiques, Montreal).
38 pages as printed (pp. 1-38; references end p. 38). Dedicated to the memory
of Lord Cherwell.

Transcription conventions: ASCII only. Diacritics transliterated (Cramer,
Erdos, Universite de Montreal, Westzynthius). Math in LaTeX-like ASCII:
\pi = prime counting function, \phi = Euler phi, \gamma = Euler-Mascheroni
constant, \omega(u) = Buchstab function (also \omega(p) = Hardy-Littlewood
local factor in Section 4.1; context disambiguates), \rho(u) = Dickman-de
Bruijn function, <= , >= , << (Vinogradov), ~ (asymptotic), \asymp, <~ and >~
for the paper's \lesssim and \gtrsim, prod, sum, int. The paper's blackboard
"Y" random variable is written Y. log_2 x here always written out as
log log x (the paper writes log log x in full). Anchors are section /
equation / proposition / figure / appendix identifiers; page numbers
(printed page = PDF page) are secondary aid.

Everything up to the final section is EXTRACTION (what the paper says).
Commentary appears ONLY in the final marked section.

---

## 1. ABSTRACT AND FRAMING (verbatim)

Abstract (p. 1), verbatim:

> "We formulate, using heuristic reasoning, conjectures for the range of the
> number of primes in intervals of length y around x, where y << (log x)^2.
> In particular we conjecture that the maximum grows surprisingly slowly as
> y ranges from log x to (log x)^2. We will exhibit the available data,
> showing that it somewhat supports our conjectures, though not so well that
> there may not be room for some modifications."

Central objects (Section 1, p. 1), verbatim:

> "We are interested in estimating the maximum and minimum number of primes
> in a length y sub-interval of (x, 2x], denoted by
>   M(x,y) := max_{X in (x,2x]} pi(X + y) - pi(X) and
>   m(x,y) := min_{X in (x,2x]} pi(X + y) - pi(X),
> respectively, so that
>   m(x,y) <= pi(X + y) - pi(X) <= M(x,y) whenever x < X <= 2x,
> and these bounds cannot be improved (by definition). It is widely believed
> that m(x,y) = 0 for y << (log x)^2 though we do not know the precise value
> of the implicit constant."

Framing of the two linear regimes (Section 1, pp. 1-2), verbatim:

> "Based on the (conjectured) size of admissible sets we believe that there
> exists a constant c > 0 such that
>   M(x,y) ~ y/log y
> for y <= c log x, as long as y -> infinity as x -> infinity (see sections
> 1.1, 4.1, 8.1 and 9.1). On the other hand, based on a modification of
> Cramer's probabilistic model [3] for the distribution of primes (which in
> turn is based on Gauss's observation that the primes have density
> 1/log x around x), we believe that
>   M(x,y) ~ sigma_+(A) y/log x
> for y = (log x)^A with A > 2, for some constant sigma_+(A) > 1, for which
> sigma_+(A) -> 1^+ as A -> infinity (see sections 1.5, 3.1, and 7.2)."

The "surprisingly slow" growth observation (Section 1, p. 2), verbatim:

> "At the end-points of this in-between interval, the above claims suggest
> that
>   M(x, log x) ~ log x/log log x whereas M(x, (log x)^2) \asymp log x,
> so M(x,y) does not seem to get much bigger as y grows from log x to
> (log x)^2; indeed it grows by only a factor of log log x. This is very
> different from before and after this interval: As y goes from 1 to log x
> we expect M(x,y) to grow by a factor of \asymp log x/log log x, and as y
> goes from (log x)^2 to (log x)^3 to grow by a similar factor of \asymp
> log x (and indeed for any subsequent interval of multiplicative length
> log x). This does not seem to have been previously observed."

The intermediate-range conjecture (Section 1, p. 2), verbatim:

> "Based on an appropriate heuristic we conjecture that if 1 < A < 2 then
>   M(x, (log x)^A) ~ (1/(2 - A)) . (log x/log log x);
> more precisely that if log x <= y = o((log x)^2) then
>   M(x,y) ~ log x / log( (log x)^2 / y ).   (1)"

The four ranges (Section 1, p. 3), verbatim:

> "In this article we will argue that there are four ranges of y in each of
> which we expect different behaviour for M(x,y), namely:
>   y << log x;  log x << y = o((log x)^2);  y \asymp (log x)^2;  and
>   y/(log x)^2 -> infinity with y <= x."

---

## 2. CONJECTURES BY RANGE (Sections 1.1-1.7, verbatim displays)

### 2.1 Very short intervals (Section 1.1, p. 3)

> "We believe that if y <= log x then
>   M(x,y) ~ y/log y   (2)
> provided x, y -> infinity. We will now formulate a more precise conjecture
> than this for y <= (1 - o(1)) log x: A set of integers A is admissible if
> for every prime p there is a residue class mod p that does not contain any
> element from the set (otherwise A is inadmissible). Let S(y) denote the
> maximum size of an admissible set A which is a subset of [1, y], so that
>   M(x,y) <= S(y) if x >= y
> (for if X < p_1 < ... < p_k <= X + y are primes then
> {p_1 - X, ..., p_k - X} is an admissible set). We believe that if
> y <= (1 - o(1)) log x then
>   M(x,y) = S(y).   (3)
> These two conjectures are consistent since it is believed that
> S(y) ~ y/log y."

Footnote 2 (p. 3), verbatim: "The 'o(1)' here can be interpreted as saying
that for any fixed epsilon > 0, if x is sufficiently large then (3) holds for
all y <= (1 - epsilon) log x."

Data commentary (p. 4, after Figure 1), verbatim:

> "Although we do believe that M(x,y) = S(y) for all y <= (1 - epsilon)
> log x, for all sufficiently large x, and perhaps even for all y <= log x
> for all x, we do not believe that this should be so for
> y > (1 + epsilon) log x and that the data we see here is an artifice of the
> relatively small values of x we can compute with."

### 2.2 Intermediate length intervals (Section 1.2, pp. 4-5)

> "log x <= y = o((log x)^2). In this range we believe that (1) holds:
>   M(x,y) ~ L(x,y) where L(x,y) := log x / log( (log x)^2 / y )."

Comparison to data (p. 5, paraphrase marked): they plot M(x,y) against
L(x,y) for x = 10^9..10^12 and note (verbatim): "The graph indicates that
our prediction provides a pretty good approximation to the data in the whole
range, though it is concave up whereas the data itself appears to yield a
curve that is concave down. We have no explanation for that."

### 2.3 The maximum on longer intervals y \asymp (log x)^2 (Section 1.3, pp. 5-6)

Verbatim (pp. 5-6):

> "Here we mean that y = t(log x)^2 for some fixed value of t. In this range
> we will need to define two implicit functions to formulate our conjectures
> for m(x,y) and M(x,y): For every given t > 0 consider the equation
>   u(log u - log t - 1) + t = 1.
> We will show that for every t > 0 there is a unique solution u_+(t) with
> u_+(t) > t. If 0 < t < 1 there is no solution in u in (0, t), so we let
> u_-(t) = 0. If t > 1 then there is a unique solution u_-(t) with
> 0 < u_-(t) < t. We believe that there exist constants c_-, c_+ > 0 such
> that if y = t(log x)^2 then
>   m(x,y) ~ u_-(c_- t) log x and M(x,y) ~ u_+(c_+ t) log x.   (4)
> We will see at the end of section 3 that c_+- are constants that can be
> defined in terms of sieving intervals. We know that c_+ >= 1.015... and
> c_- <= e^gamma / 2 = 0.890536..., and perhaps both of these inequalities
> should be equalities."

Footnote 3 (p. 6), verbatim: "We will assume that c_+ = 1.015... and
c_- = 0.8905... throughout for the purpose of comparing our conjectures to
our data. We will explain the significance of 1.015... at the end of
section 3."

Data commentary (pp. 6-7), verbatim: "It appears that this prediction is too
large by a factor of about 35% (and if c_+ is larger than 1.015 then the red
curve will be even further above the data). However we believe this is a
consequence of only calculating up to x = 10^12 and hopefully the data will
get closer to our curve the larger x gets." Footnote 4 (p. 7), verbatim:
"One referee asks whether we expect that u_+(c_+ t) log x >=
M(x, t(log x)^2) will persist for larger x; we have no idea how to make
predictions that are this precise, and doubt the value of trying to do so
given how far out our predictions currently are from the data!"

### 2.4 The minimum on longer intervals; maximal prime gap (Section 1.4, p. 7)

Verbatim:

> "The prediction (4) implies that if c_- t < 1 then m(x, t(log x)^2) = 0
> but not if c_- t > 1. That is, we conjecture the following lower bound for
> the maximal gap between consecutive primes:
>   max_{x < p_n <= 2x} p_{n+1} - p_n ~ c_-^{-1} (log x)^2
>     >= 2 e^{-gamma} (log x)^2;
> and it is feasible that we have equality here. This is larger than
> Cramer's original conjecture (that this maximal gap is ~ (log x)^2). As we
> will discuss, Cramer's reasoning is flawed by failing to take account of
> divisibility by small primes (a point originally made by the first author
> back in [9] and recently re-iterated by the in-depth analysis of Banks,
> Ford and Tao in [1].) However the data does not really support either
> conjecture, as the largest gap between consecutive primes that has been
> found is about .9206 (log x)^2 (a shortfall of around 22% from
> 2 e^{-gamma} approx 1.1229...)."

Figure 4 (p. 7): "(Known) record-breaking gaps between primes". Table of
p_n, p_{n+1} - p_n, (p_{n+1} - p_n)/log^2 p_n; last three rows: p_n =
19581334192423, gap 766, ratio .8178; p_n = 218209405436543, gap 906, ratio
.8311; p_n = 1693182318746371, gap 1132, ratio .9206.

Secondary-term discussion (p. 7), verbatim:

> "All such heuristics seem to suggest that the maximal gap between
> consecutive primes up to x should grow like log x (a log x + b log log x
> + c) for some constants a, b, c. The only possibilities for a seem to be
> a = 1 or 2 e^{-gamma}, though there are many possible guesses for b and c."

(p. 8, after Figure 5), verbatim: "The data for the largest gap between
consecutive primes is substantially smaller than our two predictions. No one
has suggested a good reason for this shortfall, though in appendix A we
explain how at least some of this shortfall is due to the use of asymptotic
estimates for primes and sieves, for relatively small values." Footnote 5
(p. 8), verbatim: "One referee correctly feels that it is inappropriate to
try to fit a justification to the data but, who knows, perhaps some
enterprising future researcher will see a clearly good reason for our
favourite candidate, log x (2 e^{-gamma} log x - 5 log log x + 6)."

### 2.5 Long intervals and Maier's theorem (Section 1.5, pp. 10-11)

Verbatim (p. 10):

> "y/(log x)^2 -> infinity. We believe that there exist continuous functions
> 0 < sigma_-(A) < 1 < sigma_+(A) for which sigma_-(A), sigma_+(A) -> 1 as
> A -> infinity, such that if y/(log x)^2 -> infinity then
>   m(x,y) ~ sigma_-(A) y/log x and M(x,y) ~ sigma_+(A) y/log x   (5)
> writing y = (log x)^A. Moreover we should take
>   c_- = sigma_-(2) and c_+ = sigma_+(2)
> above. We will obtain these conjectures from a discussion of sieve theory."

Selberg consistency and Maier (pp. 10-11), verbatim:

> "At first sight these conjectures seem to be inconsistent with Selberg's
> result that
>   pi(x + y) - pi(x) ~ y/log x
> for almost all x, assuming that y/(log x)^2 -> infinity (which he proved
> assuming the Riemann Hypothesis). However the 'almost all' in the
> statement allows for exceptions and in 1984, Maier [15] exhibited, for all
> A > 2, constants delta_+(A), delta_-(A) > 0 for which there is an infinite
> sequence of integers x_+ and x_- with
>   m(x_-, y_-) <~ delta_-(A) y_-/log x_- and
>   M(x_+, y_+) >~ delta_+(A) y_+/log x_+
> where y_+- = (log x_+-)^A. As far as we know it could be that
> sigma_-(A) = delta_-(A) and sigma_+(A) = delta_+(A) for each A, as we will
> discuss in sections 2.2 and 3."

### 2.6 Ratio statistic (Section 1.6, pp. 11-12)

Verbatim (p. 11): "we examine the ratio r_+(x,y) := M(x,2y)/M(x,y). Our
asymptotic predictions suggest that this looks like 2 + o(1) if
y <= (1/2) log x and if y/(log x)^2 -> infinity, and 1 + o(1) if
log x <= y = o((log x)^2). For y \asymp (log x)^2 our prediction for M(x,y)
is more complicated; indeed if y = t(log x)^2 then we predict that this
looks like rho_+(t) := u_+(2 c_+ t)/u_+(c_+ t)".

After Figure 7 (p. 10), verbatim: "We do not know what conclusions to draw
from this data!"

### 2.7 Summary of conjectures (Section 1.7, p. 12), verbatim

> "Fix epsilon > 0. If x is sufficiently large and y <= (1 - epsilon) log x
> then
>   M(x,y) = S(y).
> A weaker conjecture claims if y <= (1 - o(1)) log x and y -> infinity as
> x -> infinity then
>   M(x,y) ~ y/log y.
> If log x <= y = o((log x)^2) then
>   M(x,y) ~ L(x,y) where L(x,y) := log x / log( (log x)^2 / y ).
> We conjecture that there exist constants c_-, c_+ > 0 such that if
> y = t(log x)^2 then
>   m(x,y) ~ u_-(c_- t) log x and M(x,y) ~ u_+(c_+ t) log x,
> and we even have tentative guesses about the values of c_- and c_+.
> Moreover this suggests that
>   max_{x < p_n <= 2x} p_{n+1} - p_n ~ c_-^{-1} (log x)^2.
> Finally for any fixed A > 2 we believe that there exist continuous
> functions sigma_-(A) < 1 < sigma_+(A) such that if y = (log x)^A then
>   m(x,y) ~ sigma_-(A) y/log x and M(x,y) ~ sigma_+(A) y/log x."

---

## 3. UNCONDITIONAL RESULTS QUOTED (Section 2.1, pp. 12-13)

Verbatim (p. 12):

> "Following up the 2013 breakthrough by Yitang Zhang [24] on small gaps
> between primes, Maynard [17] and Tao [22] proved that there are shortish
> intervals that contain m primes for any fixed m. Their remarkable work
> implies that there exists a constant c > 0 such that for each y >= 2 we
> have
>   M(x,y) >= c log y if x is sufficiently large,
> which unfortunately is far smaller than what is conjectured here, in all
> ranges of y. However, before Zhang's work we could only say, for
> y << log x, that M(x,y) >= 1, and after Zhang only that M(x,y) >= 2, so
> these latest efforts are significant leap forward in our understanding."

Verbatim (p. 13):

> "Similarly Ford, Green, Konyagin, Maynard and Tao [6], following up on
> [5, 18], recently showed that
>   m(x,y) = 0 for some y >> (log x log log x log log log log x) /
>     (log log log x),
> and they believe their technique (which consists of looking only at
> divisibility by small primes) can be extended no further than y as large
> as (log x)(log log x)^{2+o(1)} which is far smaller than what is
> conjectured (here and previously)."

---

## 4. MAIER PHENOMENON IN SIEVING-CONSTANT FORM (Section 2.2, pp. 13-14)

Definitions (p. 13), verbatim:

> "Maier [15] proved that there can be surprisingly few or many primes in an
> interval of length (log x)^A with A > 2. His proof can be easily modified
> to express his result in terms of certain sieving constants: Define
>   S(x,y,z) := #{n in (x, x+y] : (n, P(z)) = 1}
> where P(z) := prod_{p <= z} p, and let
>   S^+(y,z) := max_x S(x,y,z) and S^-(y,z) := min_x S(x,y,z).
> For each fixed u >= 1 we define
>   sigma_+(u) := limsup_{z -> infinity} S^+(z^u, z) /
>     { prod_{p <= z} (1 - 1/p) . z^u }
>   and sigma_-(u) := liminf_{z -> infinity} S^-(z^u, z) /
>     { prod_{p <= z} (1 - 1/p) . z^u }."

Limits belief (p. 13), verbatim:

> "we state here that we believe that both the limsup's and the liminf's are
> actually limits so that
>   S^+(z^u, z) ~ sigma_+(u) prod_{p <= z} (1 - 1/p) . z^u and
>   S^-(z^u, z) ~ sigma_-(u) prod_{p <= z} (1 - 1/p) . z^u.   (6)"

Maier transfer (p. 13), verbatim:

> "Maier's proof in [15] can be modified to show that for y = (log x)^A and
> z = epsilon log x we have
>   M(x,y) >= {1 + o_{x->infinity}(1)} S^+(y,z) . e^gamma log z / log x
> which implies that there exist arbitrarily large x (= x_+) for which
>   M(x,y) >= {1 + o(1)} sigma_+(A) y/log x.
> Analogously that there are arbitrarily large x (= x_-) for which
>   m(x,y) <= {1 + o(1)} sigma_-(A) y/log x.
> If, as we believe, (6) holds then these estimates are true for all x."

Method self-description (pp. 13-14), verbatim:

> "In (5) we have conjectured that these bounds are 'best possible';
> paraphrasing, we are postulating that Maier's observation about the effect
> of small prime factors is the key issue in estimating the extreme number
> of primes in intervals with lengths significantly longer than (log x)^2.
> In fact our conjectures come from firstly sieving by small primes, and
> secondly looking at the tail probabilities of the binomial distribution
> that comes from a probabilistic model which takes account of divisibility
> by small primes."

---

## 5. SIEVE METHODS AND THEIR LIMITATIONS (Section 3, pp. 14-16)

Jurkat-Richert (p. 14), verbatim:

> "In 1965, Jurkat and Richert [14] showed that if y = z^u then
>   (f(u) + o(1)) . G(z) y <= S(A, z) <~ F(u) . G(z) y,   (7)
> where f(u) = e^gamma (omega(u) - rho(u)/u) and F(u) = e^gamma (omega(u) +
> rho(u)/u), and rho(u) and omega(u) are the Dickman-de Bruijn and Buchstab
> functions, respectively."

Iwaniec/Selberg optimality via Liouville examples (p. 14), paraphrase
marked: the sets A^{+-} = {n <= x : lambda(n) = -+1} (lambda = Liouville)
satisfy the sieve hypotheses with S(A^-, z) ~ f(u) G(z) #A^- and
S(A^+, z) ~ F(u) G(z) #A^+ (their display (8)), showing (7) is best
possible for the linear sieve. Hence (p. 14, verbatim):

> "Since our question (bounding S(x,y,z)) is an example of this linear sieve
> we deduce that
>   f(u) <= sigma_-(u) <= 1 <= sigma_+(u) <= F(u),"

Siegel-zero obstruction (p. 15), verbatim:

> "and we expect that all of these inequalities are strict. However, in
> [11], it is shown that if there are infinitely many 'Siegel zeros' then,
> in fact,
>   sigma_-(u) = f(u) and sigma_+(u) = F(u) for all u >= 1.
> Given that eliminating Siegel zeros seems like an intractable problem for
> now, we are stuck. However in this paper we are allowed to guess at the
> truth, though we know too few interesting examples to even take an
> educated guess as to the true values of sigma_-(u) and sigma_+(u)."

Footnote 7 (p. 15), verbatim: "That is, putative counterexamples to the
Generalized Riemann Hypothesis, the most egregious that cannot be ruled out
by current methods."

Lemma 1 (p. 15), verbatim:

> "Lemma 1. sigma_+(u) is non-increasing, sigma_-(u) is non-decreasing, and
> sigma_+(u), sigma_-(u) -> 1 as u -> infinity"

Its proof uses the fundamental lemma of the small sieve (p. 15, verbatim):
"S(x, z^u, z) = {1 + O(u^{-u})} prod_{p <= z} (1 - 1/p) . z^u so that
sigma_+(u), sigma_-(u) = 1 + O(u^{-u}) = 1 + o_{u->infinity}(1)."

Best bounds (Section 3.1, pp. 15-16), verbatim:

> "In Maier's paper he used the well-known fact that for all u >= 1,
>   #{n <= z^u : (n, P(z)) = 1} ~ omega(u) z^u / log z
> where omega(u) is the Buchstab function, defined by omega(u) = 1/u for
> 1 <= u <= 2, and (u omega(u))' = omega(u - 1) for all u >= 2. By Lemma 1
> we have
>   sigma_+(A) = max_{B >= A} sigma_+(B) >= e^gamma max_{B >= A} omega(B),
> and, similarly, sigma_-(A) <= e^gamma min_{B >= A} omega(B)."

Numerical values (p. 16), verbatim:

> "Nonetheless its global minimum occurs at u = 2 so that sigma_-(2) <=
> e^gamma omega(2) = e^gamma/2 (and we saw earlier that the linear sieve
> bounds give sigma_-(2) >= 0). We are most interested in sigma_+(2), which
> is bounded below by e^gamma max_{B >= 2} omega(B). This maximum occurs at
> B approx 2.75 with omega(B) approx 0.57, so that sigma_+(2) >= 1.015...
> (and we saw earlier that the linear sieve bounds give sigma_+(2) <=
> e^gamma = 1.78107...)"

> "In section 1.3 we have c_+ = sigma_+(2) and took this to be equal to
> 1.015... in our computations as this is the best lower bound known on
> sigma_+(2). Similarly in section 1.4 we have c_- = sigma_-(2) and took
> this to be equal to e^gamma/2 in our model as this is the best upper bound
> known on sigma_-(2). It could be that these are equalities, but there is
> little evidence either way."

Maier-Stewart improvement for sigma_-(A), small A (p. 16, paraphrase
marked): sieving [1, x], x = z^u, first with primes in (z^{1/v}, z] then
greedily with primes <= z^{1/v} gives sigma_-(A) <= min{e^gamma/2,
r_A(v_A)} for 1 <= A <= 2, where r_u(v) := v(rho(uv) + log u); minimized at
r'_u(v_u) = 0; if u = 1 + 1/Delta with 1/Delta = o(1) then v_u ~ log Delta /
log log Delta and r_u(v_u) ~ log Delta / (Delta log log Delta). "In [16]
this argument is extended to show that r_A(v_A) is the minimum exactly when
1 <= A <= 1.50046.... Unfortunately we are only really interested in
sigma_-(A) for A >= 2 in this article." (verbatim fragment, p. 16).

---

## 6. VERY SHORT INTERVALS AND THE TUPLES OBSTRUCTION (Section 4, pp. 17-19)

S(y) size (p. 17), verbatim:

> "How large is S(y)? One can show that the primes in (y, 2y] yield an
> admissible set and so S(y) >~ y/log y (by the prime number theorem). It is
> believed that
>   S(y) ~ y/log y
> but the best upper bound known is S(y) <~ 2y/log y (by the upper bound in
> (7)), and this upper bound seems unlikely to be significantly improved in
> the foreseable future (as we again run into the Siegel zero obstruction)."

Hensley-Richards and the 481-tuple (p. 17), verbatim:

> "One interesting theorem, due to Hensley and Richards, is that if y is
> sufficiently large then S(y) > pi(y) and so, if the prime k-tuplets
> conjecture is true then for all sufficiently large y there exist
> infinitely many intervals of length y that have more primes than the
> initial interval [1, y]. The known values of S(y) and bounds, can be found
> on http://math.mit.edu/~primegaps/ and from there we see that S(3432) >=
> 481 > pi(3432) = 480. Therefore we believe that there are infinitely many
> intervals of length 3432 containing exactly 481 primes, more than the 480
> primes <= 3432 found at 'the start'. However, finding such an interval
> (via methods based on this discussion) involves finding a prime 481-tuple,
> which would be an extraordinary challenge unless one is very lucky."

Westzynthius (pp. 17-18), verbatim: "By a simple sieving argument
Westzynthius showed in the 1930s that for any constant C > 0 there exist
intervals [x, x + C log x] which do not contain any primes. This argument is
easily modified to show that for any c > 0
  m(x, c log x) := min_{X in (x,2x]} (pi(X + c log x) - pi(X)) = 0
if x is sufficiently large."

Explicit prime k-tuplets conjecture (Section 4.1, p. 18), verbatim:

> "For a given admissible set of linear forms b_j n + a_j, j = 1, ..., k,
> Hardy and Littlewood [12] conjectured that
>   #{x < n <= 2x : Each b_j n + a_j is prime} ~
>     prod_p (1 - 1/p)^{-k} (1 - omega(p)/p) . x/(log x)^k,   (10)
> where omega(p) is the number of n (mod p) for which p divides
> prod_{j=1}^k (b_j n + a_j)."

Footnote 9 (p. 18), verbatim:

> "Surprisingly there is no way known to try to prove this. The best we know
> how to obtain, assuming the Generalized Riemann Hypothesis, is that if
> k = 1 then (10) holds for all x >= b^{1+epsilon}, though this can be
> obtained 'on average' unconditionally. Linnik's Theorem implies that there
> exists a constant lambda such that one can obtain a lower bound on the
> left-hand side of (10) once x >> b^lambda (and so there is a prime <<
> b^{lambda+1} in each reduced residue class mod b). In 2011, Xylouris [23]
> showed that we can take lambda = 4, the smallest lambda known-to-date"

Calibration of when tuples appear (pp. 18-19, paraphrase marked): For an
admissible A of size k = S(y) ~ alpha y/log y (alpha believed = 1), with
Q := prod_{a in A} a = e^{(alpha + o(1)) y} = k^{(1+o(1))k}, they estimate
the singular series to be (e^{O(1)} log k)^k and conclude (p. 19, verbatim):

> "So there exists a constant C > 0 such that the right-hand side of (10) is
> >= 1 when (C log k)^k x > (log x)^k. This certainly happens when x = k^{ck}
> for any fixed c > 1; that is, x > Q^{1+epsilon}."

> "Now if #{x < n <= 2x : Each n + a is prime, for each a in A} >= 1 then
> M(x,y) = S(y). From the above we might guess this holds when
> x > Q^{1+epsilon} where Q = e^{(1+o(1))y}; that is, if
> y <= (1 - o(1)) log x. Indeed we only need the above heuristic discussion
> to be roughly correct 'on average' over all such admissible sets, to
> support the conjecture in (9)."

(Equation (9), p. 17, verbatim: "M(x,y) = S(y) for all y <= {1 - o(1)}
log x;".) Footnote 10 (p. 19), verbatim: "This reasoning suggests that even
if we are pessimistic then we would simply change the range in (9) to
y <= (c + o(1)) log x for some constant c in (0, 1)."

---

## 7. CRAMER'S HEURISTIC AND ITS FLAW (Section 5, pp. 19-20) [FOCUS 1, 3]

Basic Cramer model (p. 19), verbatim:

> "Gauss noted from calculations of the primes up to 3 million, that the
> density of primes at around x is about 1/log x. Cramer used this as his
> basis for a heuristic to make predictions about the distribution of
> primes: Consider an infinite sequence of independent random variables
> (X_n)_{n >= 3} for which
>   Prob(X_n = 1) = 1/log n and Prob(X_n = 0) = 1 - 1/log n.
> By determining what properties are true with probability 1 + o(1) for the
> sequence of 0's and 1's given by X_3, X_4, ..., Cramer suggested that such
> properties must also be true of the sequence 1,0,1,0,1,0,0,0,1,... of 0's
> and 1's which is characteristic of the odd prime numbers."

What it gets right (p. 19), verbatim: "if N is sufficiently large then
S_N := sum_{n=3}^N X_n has mean int_2^N dt/log t + O(1) and roughly the same
variance, which suggests the conjecture that pi(N) = int_2^N dt/log t +
O(N^{1/2 + o(1)}); it is known that this conjecture is equivalent to the
Riemann Hypothesis."

The flaw (pp. 19-20), verbatim:

> "However Cramer's heuristic does have an obvious flaw: Since it treats all
> the random variables as independent, we have Prob(X_n = X_{n+1} = 1)
> approx 1/(log n)^2, so that
>   E( sum_{n=3}^{N-1} X_n X_{n+1} ) = int_2^N dt/(log t)^2 +
>     O(N^{1/2 + o(1)})
> with probability 1 + o(1), which, Cramer's heuristic suggests, implies
> that there are infinitely many prime pairs n, n + 1. But we have seen this
> is not so as {0, 1} is an inadmissible set. More dramatically this
> heuristic would even suggest that M(x,y) = y for all values of
> y <= {1 + o(1)} log x. From the previous section we know that this is
> false because M(x,y) <= S(y), as every pi(n, n + y] is restricted by those
> integers that are divisible by 'small' primes, that is primes <=
> y^{1+o(1)}. This heuristic also suggests that the primes are
> equi-distributed amongst all of the residue classes modulo a given integer
> q, rather than just the reduced classes."

The divisibility-corrected (modified Cramer) model (p. 20), verbatim:

> "It therefore makes sense to modify Cramer's probabilistic model for the
> primes to take account of divisibility by 'small' primes. The obvious way
> to proceed is to begin by sieving out the integers n that are divisible by
> a prime p <= z (perhaps with z = y), and then to apply an appropriate
> modification of Cramer's model to the remaining integers, that is the
> integers that have no prime factor <= z. The number of such integers up to
> x is
>   ~ kappa x where kappa = kappa(z) := prod_{p <= z} (1 - 1/p)
> if z = x^{o(1)}, and so the density of primes amongst such integers is
> 1/(kappa log x). We therefore proceed as follows:
>   Define P = P(z) := prod_{p <= z} p so that kappa(z) = phi(P)/P. We
> consider an infinite sequence of independent random variables
> (X_n)_{n >= 3} for which X_n = 0 if (n, P) > 1; and
>   Prob(X_n = 1) = 1/(kappa log n) and
>   Prob(X_n = 0) = 1 - 1/(kappa log n) if (n, P) = 1.
> With this model we can again accurately predict the prime number theorem
> (and the Riemann Hypothesis), as well as asymptotics for primes in
> arithmetic progressions, for prime pairs, and even for admissible prime
> k-tuplets (with k <= z). Moreover, this will allow us to obtain our
> predictions for maximal and minimal values of pi(x, x + y] (including the
> prediction for y << log x that we already deduced from assuming enough
> uniformity in the prime k-tuplets conjecture in section 4.1)."

Reduction to fixed parameters (p. 20), verbatim:

> "If n in (x, 2x] with (n, P) = 1 then Prob(X_n = 1) = 1/L +
> O(1/(L log x)) where L := kappa log x, so for convenience we will work
> with a model where each Prob(X_n = 1) = 1/L. There are, say, N integers in
> (X, X + y] that are coprime to P where, a priori, N could be any number
> between 0 and y (though we can refine that to 0 <= N <= S^+(y,z) <<
> y/log z by the sieve). We now develop a model where L and N are fixed:"

---

## 8. BINOMIAL TAIL MACHINERY (Sections 6-7, pp. 20-24) [FOCUS 2]

Setup (Section 6, pp. 20-21), verbatim: "Suppose that we have a sequence of
independent, identically distributed random variables X_1, ..., X_N with
P(X_n = 1) = 1/L and P(X_n = 0) = 1 - 1/L, where L is large. Let
Y := sum_{n <= N} X_n. Then Y is a binomially distributed random variable,
which is often denoted B(N, 1/L)."

Proposition 1 (p. 21), verbatim [the paper's blackboard Y written Y]:

> "Proposition 1. Suppose that N << L log x, and that L -> infinity as
> x -> infinity. If k_- = k_-(N, L, x) is the largest integer for which
>   P(Y < k_-) <= 1/x
> then
>   k_- = { 0                          if N <= {1 + o(1)} L log x;
>         { {delta_-(lambda) + o(1)} N/L   if N = {lambda + o(1)} L log x
>                                          with lambda > 1;
> where delta_- = delta_-(t) is the smallest positive solution to
> delta(log delta - 1) + 1 = 1/t.
>   If k_+ = k_+(N, L, x) is the smallest integer for which
>   P(Y >= k_+) <= 1/x.
> then
>   k_+ = { N                          if N <= log x/log L;
>         { {1 + o(1)} log x / log( L log x / N )
>                                      if log x/log L <= N = o(L log x);
>         { {delta_+(lambda) + o(1)} N/L   if N = {lambda + o(1)} L log x
>                                          with lambda > 0;
> where delta_+ = delta_+(t) is the largest positive solution to
> delta(log delta - 1) + 1 = 1/t. We observe that k_- <= k_+ << log x if
> N << L log x."

Proof mechanism (p. 21, paraphrase marked): P(Y = k) = binom(N,k)(1/L)^k
(1 - 1/L)^{N-k}; P(Y = N) = 1/L^N > 1/x iff N <= log x/log L; P(Y = 0) =
(1 - 1/L)^N = e^{-N/L + O(N/L^2)} > 1/x for N <= {L + O(1)} log x; Stirling
gives P(Y = k) = (eN/(kL))^k exp(-N/L + O(k^2/N + log k + k/L + N/L^2)),
and in the middle range P(Y = k) = (eN/(kL))^k x^{o(1)} = x^{-1+o(1)} iff
k ~ log x / log(L log x / N).

Footnote 11 (p. 21), verbatim: "To be more precise we obtain N <=
log x / (-log(1 - 1/L)) = (L - 1/2 - 1/(12L) + O(1/L^2)) log x."

Relative-entropy remark (p. 22), verbatim (excerpt):

> "There are well-known bounds on the tail of the binomial distribution
> (see, e.g., [4]) which can be used to obtain this last result:
>   (1/sqrt(8k(1 - k/N))) exp(-N D(k/N | 1/L)) <= {P(Y <= k) if k <= N/L;
>   P(Y >= k) if k >= N/L} <= exp(-N D(k/N | 1/L))
> where D(a|p) := a log(a/p) + (1 - a) log((1-a)/(1-p)) which is called the
> relative entropy in some circles"

and (verbatim): "Using these inequalities we would determine delta =
delta(t, L) from the functional equation L D(delta/L | 1/L) = (1/t)(1 +
O(log log x / log x)), which is slightly different, but yields delta(t, L) =
delta(t) + O((1/log delta(t))(1/L + log log x/log x)), a negligible
difference in the ranges we are concerned about."

Asymptotics (Section 7, pp. 22-23): u(t) = t delta(t) where delta_+- solve
f(delta) := 1 - delta log(e/delta) = 1/t (p. 22, verbatim display:
"f(delta) := 1 - delta log(e/delta) = 1/t"). Monotonicity: "u_+(t) is
increasing in t > 0 and u_-(t) is increasing in t >= 1" (p. 23, verbatim
fragment).

Estimates as t -> infinity (Section 7.1, p. 23), verbatim:

> "u_+(t) = t delta_+(t) = t + (2t)^{1/2} + 1/3 + 1/(9 . 2^{3/2} t^{1/2})
>   + O(1/t)
> u_-(t) = t delta_-(t) = t - (2t)^{1/2} + 1/3 - 1/(9 . 2^{3/2} t^{1/2})
>   + O(1/t),
> for large t. So if t is large and N = t L log x then, in Proposition 1,
>   k_+- = ( t +- (2t)^{1/2} + 1/3 - O(1/t^{1/2}) ) log x as t -> infinity."

[TRANSCRIPTION-UNSURE: in the k_+- display the third and fourth terms print
as "+ 1/3 - O(1/t^{1/2})"; the sign pattern of the O-term relative to +- is
as printed above.]

Estimates as t -> 0^+ (Section 7.3, p. 24), verbatim:

> "delta_+(t) = (1/t) / log( (1/t) / (e log 1/t) ) (1 + O( log log 1/t /
>   (log 1/t)^2 ))   (11)
> so that
>   u_+(t) = t delta_+(t) = (1/log(1/t)) (1 + O( log log 1/t / log 1/t ))
> and therefore
>   k_+ ~ u_+(t) log x ~ log x / log(1/t) as t -> 0^+."

And for t -> 1^+ (p. 24), verbatim: "k_- ~ u_-(t) log x ~
(t - 1) log x / log(1/(t-1)) as t -> 1^+, which -> 0 as t -> 1^+. This
suggests that k_- = 0 for N < {1 - o(1)} L log x but grows like
  (N - L log x) / (L log( N / (N - L log x) ))
for a small range near L log x which we denote by L log x < N <
{1 + o(1)} L log x."

Normal approximation FAILS in the tails (Section 7.2, p. 23), verbatim:

> "A random variable given as the sum of enough independent binomial
> distributions tends to look like the normal distribution, at least at the
> center of the distribution. However since we are looking here at tail
> probabilities, the explicit meaning of 'enough' is larger than we are used
> to."

> "Writing N = lambda L log x we have tau sigma ~ (2 lambda)^{1/2} log x.
> Therefore we might expect the maximum and minimum values of Y to be
> (lambda +- (2 lambda)^{1/2} + o(1)) log x. We see from section 7.1 that
> this is correct as lambda -> infinity (but not for fixed lambda)."

> "We can see this issue more simply: If k = kappa N/L with kappa > 1 then
> the binomial distribution gives
>   Prob(Y >= k) \asymp (1 - 1/L)^N binom(N,k) (1/(L-1)^k) =
>     exp( -(N/L)(kappa(log kappa - 1) + 1 + o(1)) )
> and the normal distribution (with the same mean and variance) gives
>   Prob(Y >= k) = exp( -(N/L)((1/2)(kappa - 1)^2 + o(1)) )
> and the main terms here are only the same when kappa -> 1^+."

NOTE (extraction-level observation): the word "Poisson" does not occur in
this paper; all tail calibration is done through the binomial B(N, 1/L)
directly (Proposition 1), with the normal approximation shown inadequate in
the tails (Section 7.2). A Poisson-approximation discussion is NOT FOUND in
this text.

---

## 9. APPLYING THE MODIFIED CRAMER HEURISTIC (Section 8, pp. 24-26) [FOCUS 1, 2]

General set-up (p. 24), verbatim:

> "Here is the general set-up. For some z <= y define P = P(z) :=
> prod_{p <= z} p so that P(z) = e^{(1+o(1))z} by the prime number theorem.
> For S(x,y,z) := #{n in (x, x + y] : (n, P(z)) = 1} (as in section 2.2) we
> define
>   I(N) = {X in (x, 2x] : S(X,y,z) = N}.
> for each integer N in the range 0 <= N <= S^+(y,z). Our heuristic is that
> the values
>   pi(X, X + y] for X in I(N),
> are distributed like the binomially distributed random variable
>   B(N, 1/L) where L = (phi(P)/P) log x."

Prediction scheme (p. 25), verbatim:

> "We therefore use Proposition 1 (with x there equal to #I(N)) to predict
> the value of
>   M_N(x,y) := max_{X in I(N)} pi(X, X + y]
> for each N with I(N) non-empty. From these predictions we obtain our
> predictions for
>   M(x,y) = max_N M_N(x,y)."

CRT periodicity of sieve patterns (p. 25), verbatim:

> "One can work out the details of this heuristic to make precise
> conjectures provided we can get a good estimate for log #I(N). This is
> not difficult when z <= epsilon log x: For each m, 0 <= m <= P - 1 we have
>   S(X,y,z) = S(m,y,z) whenever X == m (mod P(z)),
> since (X + j, P) = (m + j, P) for all j. Moreover these intervals
> (X, X + y] with X == m (mod P(z)) are all disjoint so can be considered to
> be independent. Therefore if N = S(m,y,z) then P = P(z) <= x^{epsilon +
> o(1)} and so
>   #I(N) >= #{X in (x, 2x] : X == m (mod P(z))} = x/P + O(1) >=
>     x^{1 - epsilon + o(1)}.
> Hence, when z is this small, the answer given by our heuristic depends
> only on the extreme values, S^-(y,z) and S^+(y,z)."

Limits of the scheme (p. 25), verbatim: "Getting a good estimate for
log #I(N) is not straightforward if z (and therefore y) is significantly
larger than log x. However one expects our heuristic to be more accurate the
larger z is, so we have to find the right balance in our selection of z."

Very short intervals (Section 8.1, p. 25), verbatim:

> "If y <= eta log x with 0 < eta < 1/2 small, then the above discussion
> suggests taking z = y. Hence S^+(y,z) = S^+(y,y) = S(y). For each m
> (mod P) we apply Proposition 1 with
>   N = S(m,y,y), L = (phi(P)/P) log x, and x replaced by x^{1-eta}.
> For given L and x, one obtains the largest value of k_+ in Proposition 1,
> when N is as large as possible. This happens here when N = S(y), which we
> believe is ~ y/log y and know is no more than twice this. Now L \asymp
> log x/log y and Proposition 1 then implies that k_+ = N = S(y) as long as
> S(y) <= (1 - eta + o(1)) log x/log L, which should be true for any fixed
> eta < 1/2 (and at worst for eta < 1/3). This supports the conjecture (9)
> in a range like y <= (1/2 - o(1)) log x."

Choice-of-z difficulty (Section 8.2, pp. 25-26). Footnote 12 (p. 25),
verbatim: "We do not wish to sieve with primes larger than the length of
the interval, since any larger primes cannot divide more than one element in
an interval of length y, so cannot be helpful in a sieve argument."
Verbatim (p. 26):

> "However we do not need to understand these sets so precisely, we only
> need to understand their size, that is, to have good estimates for
> log #I(N) for each N, but even this seems to be out of reach. Therefore
> this is the less desirable option (though we work through some of the
> details in Appendix C). In general, we do not know how to get good
> estimates for log #I(N) whenever z is substantially larger than log x."

> "These (for now insurmountable) issues, suggest that we should proceed as
> before, with a smallish value of z, so as to recover the sieved sets
> repeating predictably. Therefore we pre-sieve the intervals of length y
> with all of the primes <= z := epsilon log x, and then apply the modified
> Cramer model. There might be a substantial difference when sieving with
> the primes <= z, as opposed to y, though we hope not. If there is a
> substantial difference then this needs further investigation."

Main calibrated prediction (Section 8.3, p. 26). Setup, verbatim: "we may
cut to the chase by taking N_+ = S^+(y,z) =: e^{-gamma} (y/log z) c_+ and
L = (phi(P)/P) log x ~ e^{-gamma} log x/log log x". Then the boxed
Prediction, verbatim:

> "Prediction: Pre-sieving up to z = epsilon log x: If log x << y =
> o((log x)^2) then
>   M(x,y) = min{ S^+(y,z), {1 + o(1)} log x / log( (log x)^2 / y ) }.
> If y = lambda (log x)^2 with lambda > 0 then
>   M(x,y) ~ u_+(lambda c_+) log x and m(x,y) ~ u_-(lambda c_-) log x."

Large-lambda consistency (p. 26), verbatim: "If lambda is large and y =
lambda (log x)^2 then u_+(lambda c_+) = lambda c_+ + sqrt(2 lambda c_+) +
O(1), and so M(x, lambda (log x)^2) ~ c_+ y/log x as lambda -> infinity; and
analogously m(x, lambda (log x)^2) ~ c_- y/log x."

Deduction mechanics (p. 26, paraphrase marked): apply Proposition 1 to
predict M_j(x,y) for X == j (mod P), each class having #{X} = x/P + O(1) =
x^{1-o(1)} elements, and guess M(x,y) = max_j M_j(x,y).

---

## 10. WHICH CHOICES; REFINED GAP GUESSES (Section 9, pp. 27-28)

Section 9.1 (p. 27), verbatim:

> "In section 1.1, we predicted that if y <= c log x then M(x,y) = S(y).
> This was confirmed by one heuristic in section 4.1, and by a very
> different heuristic in section 8.1, giving us some confidence in this
> conclusion. From all three discussions it is not obvious what explicit
> constant one should take in place of the inexplicit 'c'. Our guess is that
> for any epsilon > 0 one has
>   M(x,y) = S(y) for y <= (1 - epsilon) log x,
> if x is sufficiently large, as well
>   M(x,y) ~ log x/log log x for (1 - epsilon) log x <= y <=
>     (1 + o(1)) log x.
> The 'o(1)' is inexplicit and our methods do not pinpoint the transition
> more accurately."

Also (p. 27), verbatim: "However these small x-values do suggest that c > 1
which we do not believe, since that would force contradictions to our
predictions for M(x,y) for larger y."

Section 9.2 (p. 27), verbatim:

> "In the range log x <= y = o((log x)^2) we have predicted (1) no matter
> whether we presieve up to z or up to y. One can revisit the heuristic
> arguments above to try to get a more accurate approximation: By (11) we
> believe that if y = lambda (log x)^2 with lambda -> 0 then
>   M(x,y) is better approximated by log x / log( (1/lambda) /
>     (e log 1/lambda) )."

[TRANSCRIPTION-UNSURE: in the last display the glyph before "log 1/lambda"
in the denominator could be "e" (Euler's number, as in equation (11)) or an
epsilon; by consistency with (11) it is transcribed as e.]

Section 9.3 (p. 27), verbatim:

> "Here we write y = (log x)^A with A >= 2 and understanding that if A = 2
> then y/(log x)^2 -> infinity. If (6) holds then Proposition 1 suggests
> that
>   M(x,y) ~ sigma_+(A) y/log x and m(x,y) ~ sigma_-(A) y/log x
> which is what we believe."

and (p. 27), on pre-sieving up to y instead, verbatim: "sigma_+(A) replaced
by max_{x < X <= 2x} #{j <= y : (X + j, P(y)) = 1} / ((phi(P(y))/P(y)) y).
(and sigma_-(A) by the analogous expression with the min). However we have
no idea how to study this ratio in this restricted range for X."

Section 9.4 (p. 28), verbatim fragment: "Now u_+(c_+ lambda) ~ c_+ lambda
as lambda -> infinity and so M(x,y) ~ c_+ y/log x. This implies, letting
lambda -> infinity and comparing this prediction to that in the last
subsection, that c_+ = sigma_+(2). ... This analogously yields that
c_- = sigma_-(2)."

Section 9.5, more precise max-gap guesses (p. 28), verbatim:

> "We can be more precise about our prediction for gaps between primes
> using the footnote in the proof of Proposition 1. The estimate there N <=
> (L - 1/2 + o(1)) log x with L = (phi(P)/P) log x which would suggest that
>   max_{x < p_n <= 2x} p_{n+1} - p_n approx c_-^{-1} log x ( log x -
>     (1/2)(P/phi(P)) ) approx c_-^{-1} log x ( log x - (1/2) log log x ).
> Here P = P(z) and c_- depend on z."

Cadwell variant (p. 28), verbatim:

> "Cadwell [2] presented a variant of Cramer's model. He took the viewpoint
> that certain aspects of the distribution of H := pi(2x) - pi(x) primes in
> (x, 2x] can be assumed to be like the distribution of H randomly selected
> integers in (x, 2x]. He very elegantly proved that the expected largest
> gap has length (x/(H+1))(1/1 + 1/2 + ... + 1/(H+1)). This can be used to
> predict that
>   max_{x < p_n <= 2x} p_{n+1} - p_n approx log(4x/e)(log x - log log x +
>     gamma).
> It is not clear how to incorporate divisibility by small primes into this
> argument, particularly working only with those intervals with an
> unexpectedly small number of integers left unsieved."

(p. 28), verbatim: "There are some similarities in these two conjectural
formulas but it is not clear which to choose and on what basis. We did see
in Figure 5 that the data suggests that one should subtract a larger
multiple of log log x in the formulas above but we have not found a
believable heuristic to do so, though finding a way to combine the two
heuristics would be a good start."

Section 10 (pp. 28-29, brief): same program for primes in arithmetic
progressions pi(qy; q, a), pre-sieving with primes <= z not dividing q;
expected number of primes ~ (q/phi(q)) y/log q; "We shall explore this in
detail, with copious calculations, in a subsequent article." (p. 29,
verbatim fragment).

---

## 11. APPENDIX A: MAX-GAP PREDICTION VS TRUTH AT log x = 40 (pp. 29-30)

Verbatim (p. 29):

> "We take log x = 40: The largest prime gap up to x is 1248 immediately
> following 218034721194214273. The Cramer prediction is 1600 and ours is
> 1797."

Refined computation (p. 29), verbatim fragments: sieving all intervals of
length 1600 by primes <= z = (1/2) log x = 20; "R(n) := #{X (mod P) :
S(X,y,z) = n} where n =: c_n (phi(P)/P) y"; with the referee's improvement
(replacing L by 1/(-log(1 - 1/L))), "This then suggests that y approx
max_n (37/c_n)(23.91 + log R(n)). as log(x/P) approx 23.91 (where we had
'40', which is log x, instead of '37', before the referee's suggestion)."

Result (p. 30), verbatim:

> "and from this we obtain a prediction of y = 1420, significantly smaller
> than either previous prediction, but still unaccountably larger than the
> truth."

(Footnote 14, p. 30, verbatim: "It was y = 1536 before the referee's
intervention.") And (p. 30), verbatim:

> "We see that there are about 1.71 million intervals mod P(20) of length
> 1420 which contain exactly 242 integers that are coprime to P(20). The
> probabilistic argument then suggests that some of the corresponding
> intervals in (x, 2x] contain no primes at all. If instead we work with
> P(25) then our prediction reduces a little but not much, and indeed we
> tried all the obvious possibilities but could not manipulate the variables
> to construct a prediction that would reduce 1420 to anywhere near the
> truth, namely 1248."

---

## 12. APPENDIX B: IS THE MODEL VALID? (pp. 30-35) [FOCUS 3]

Example B.1: x = 10^8, y = 340, z = 11 (so P(11) = 2310); S(X, 340, 11)
takes each value N between 68 and 73; #C(68) = 28, #C(69) = 228, #C(70) =
784, #C(71) = 820, #C(72) = 386, #C(73) = 64 (p. 31). Model value L =
(phi(P)/P) log x = 3.82767..., refined via "a better approximation to
x/(pi(2x) - pi(x)) is given by log 4x/e" to L = (phi(P)/P) log 4x/e =
3.90794... (p. 31, verbatim fragments). Data L(N) values 3.8665...-3.9418...
"which are all reasonably close to L (no more than about 1% out)." (p. 31,
verbatim fragment.)

Binomial comparison (p. 31), verbatim: "we graph I(N, h) compared to the
prediction binom(N, h) (1/L^h) (1 - 1/L)^{N-h} from the binomial
distribution."

Mean/variance table (p. 33, verbatim numbers): for N = 68, ..., 73:
Expected mean: 17.40, 17.66, 17.91, 18.17, 18.42, 18.68; Actual mean:
17.59, 17.76, 17.96, 18.14, 18.34, 18.52; Expected variance: 12.95, 13.14,
13.33, 13.52, 13.71, 13.90; Actual variance: 10.82, 10.93, 11.06, 11.17,
11.25, 11.34.

Diagnosis (p. 33), verbatim:

> "Although both the actual and expected means increase with N we see that
> the actual mean increases more slowly than the expected. More striking is
> that the actual variance, that is the variance given by the data, is far
> smaller than in our prediction. According to Montgomery and Soundararajan
> [20] we should have
>   sum_{X=x}^{2x} (psi(X + y) - psi(X) - y)^{2k} ~ y^k .
>     int_{t=x}^{2x} ( log( e^{-gamma} t / (2 pi y) ) + 1 )^k dt
> for log x <= y <= x^{1/2k}. Therefore the variance here (for the primes)
> is, more-or-less,
>   (y/(x (log x)^2)) . int_{t=x}^{2x} ( log( e^{-gamma} t / (2 pi y) )
>     + 1 ) dt = (y/log x) . log( 2 e^{-gamma} x / (pi y) ) / log x.
> Thus a first approximation gives mean y/log x approx 18.46 and variance
> approx 11.586. If we replace log x by log 4x/e (since this gives a more
> accurate description of the density of primes in [x, 2x]) then we get
> approx 18.08 and approx 11.11, respectively. This corresponds very well
> to the data."

Example B.2 (p. 33): x = 10^8, y = 500, z = 17, P(17) = 510510; S takes
values 84..97; "We see that there are very few such intervals for the
outlying h-values, and indeed the data for these h-values does not conform
to the patterns that we observe." (verbatim). Data variance approx 15.2-16.3
vs expected 17.7-19.9 (table p. 34); with Montgomery-Soundararajan and
log 4x/e: "the overall expected mean is 26.5858... and the new expected
variance is 15.8003..., which again is a pretty good fit with this data."
(p. 35, verbatim fragment.)

Conclusion of Appendix B (p. 35), verbatim:

> "The data in this appendix makes a compelling case that one should
> develop a different model, stemming from the binomial distribution, but in
> which the X_n are not independent. Instead, their dependence must imply
> that the number of primes in short intervals of length y between x and 2x
> satisfies the normal distribution with the variance predicted by
> Montgomery and Soundararajan, and then perhaps we might see what this new
> model might give for tail probabilities. We would thus revise our
> predictions for M(x,y), m(x,y) and the largest gaps between consecutive
> primes. We hope to return to this key topic in a further paper."

Footnote 15 (p. 35), verbatim: "Though hopefully only in the secondary
terms, so as not to invalidate the conjectures in this paper!"

---

## 13. APPENDIX C: PRE-SIEVING UP TO y (pp. 35-37, brief)

Setup (p. 35, paraphrase marked): P = P(y), #I(N) =: x^{theta_N};
max_N #I(N) >= x/(S(y)+1) >= x^{1-o(1)}; the heuristic is focused on N with
theta_N = 1 + o(1); N_* = largest such N, c_* := c_{N_*} where N =:
c_N (phi(P)/P) y. Overlapping intervals are handled by passing to I'(N), a
largest subset of disjoint intervals, losing only y^{O(1)} factors (p. 35).

Boxed predictions (p. 36), verbatim:

> "Predictions, by pre-sieving up to y: If log x << y <= (e^gamma/c_*)
> log x then
>   M(x,y) ~ c_* . e^{-gamma} y/log y.
> If (e^gamma/c_*) log x <= y = o((log x)^2) then
>   M(x,y) ~ log x / log( (log x)^2 / y ).
> Finally if y = lambda (log x)^2 with lambda > 0 then
>   M(x,y) ~ max_N c_N delta_+( c_N lambda / theta_N ) . y/log x."

Large-lambda form (p. 36), verbatim fragment: "M(x, lambda(log x)^2) ~
c_dagger y/log x as lambda -> infinity where c_dagger = max_N c_N where the
maximum is taken over all those c_N with theta_N >> 1."

Occam's razor (p. 36), verbatim:

> "These predictions are substantially more complicated than those obtained
> when pre-sieving up to epsilon log x. By Occam's razor, we choose to
> follow the other path though it is feasible that both would yield the same
> prediction if only we could at least partly resolve the relevant sieve
> questions (that is, determine the values of c_dagger, c_* and
> max_N{c_N : c_N <= u theta_N} for each u > 0)."

---

## 14. MODEL-LANGUAGE DISCIPLINE EXEMPLARS [FOCUS 4]

Collected verbatim phrasings showing how the paper separates model
statements from prime statements:

(a) Conjectures about primes always carry an explicit belief marker:
"It is widely believed that" (p. 1); "we believe that" (pp. 1-3, 5, 10,
etc.); "we conjecture a series of guesstimates" (p. 1); "Based on an
appropriate heuristic we conjecture that" (p. 2); "We believe that there
exist constants c_-, c_+ > 0 such that" (p. 6); "and perhaps both of these
inequalities should be equalities" (p. 6); "it is feasible that we have
equality here" (p. 7).

(b) Theorems are proved only about the model or the sieve, never about
primes-from-model: Proposition 1 (p. 21) is a statement purely about the
binomial random variable Y = B(N, 1/L); Lemma 1 (p. 15) is about the
sieving constants sigma_+-.

(c) The transfer step is always flagged as a heuristic: "Our heuristic is
that the values pi(X, X + y] for X in I(N), are distributed like the
binomially distributed random variable B(N, 1/L)" (Section 8, p. 24); "We
therefore use Proposition 1 ... to predict the value of M_N(x,y)" (p. 25);
boxed items are labelled "Prediction:" (pp. 26, 36); "Proposition 1
suggests that" (p. 27); "This can be used to predict that" (p. 28).

(d) Model parameters are named as model choices: "In our model we would
take L = (phi(P)/P) log x = 3.82767..." (Appendix B.1, p. 31); "We will
assume that c_+ = 1.015... and c_- = 0.8905... throughout for the purpose
of comparing our conjectures to our data" (footnote 3, p. 6); "took this to
be equal to e^gamma/2 in our model as this is the best upper bound known"
(p. 16).

(e) Uncertainty is stated, not smoothed over: "It could be that these are
equalities, but there is little evidence either way" (p. 16); "we are
stuck" (p. 15); "However in this paper we are allowed to guess at the
truth" (p. 15); "We do not know what conclusions to draw from this data!"
(p. 10); "we have no idea how to make predictions that are this precise"
(footnote 4, p. 7); "We have no explanation for that" (p. 5); "still
unaccountably larger than the truth" (p. 30); "though not so well that
there may not be room for some modifications" (Abstract, p. 1).

(f) Known-false model outputs are stated as such: "which, Cramer's
heuristic suggests, implies that there are infinitely many prime pairs
n, n + 1. But we have seen this is not so as {0, 1} is an inadmissible set"
(p. 20); "More dramatically this heuristic would even suggest that M(x,y) =
y for all values of y <= {1 + o(1)} log x. From the previous section we
know that this is false" (p. 20).

---

## COMMENTARY (assessment, NOT extraction)

Consuming context: the project needs an UNCONDITIONAL supply of two
prime-gap-word sites with matched J-prefix and K-suffix windows and a
dominant weighted middle difference, at depths J, K ~ log_2 log x (an
"exchange configuration"). Known blockers: (i) pigeonhole is blind to
variability, (ii) prescribing gap patterns is a parity-blocked tuple-type
lower bound, (iii) Shiu-string site densities (2q)^{-exp(Cm)} are circular
at the needed depth. Assessment of what this paper's machinery can and
cannot supply:

1. What is actually unconditional in this paper. Almost nothing about
primes: the paper is by design heuristics + data. The unconditional
components are: Proposition 1 (p. 21) - a theorem about the binomial
B(N, 1/L) only; Lemma 1 (p. 15) - monotonicity of the sieving constants
sigma_+-; the CRT periodicity of sieve patterns (Section 8, p. 25); the
Maier-type transfer M(x,y) >= {1+o(1)} sigma_+(A) y/log x along special
x_+ sequences for y = (log x)^A, z = epsilon log x (Section 2.2, p. 13);
and the quoted external theorems M(x,y) >= c log y (Maynard-Tao, Section
2.1, p. 12) and FGKMT m(x,y) = 0 for y >> log x log log x log_4 x / log_3 x
(Section 2.1, p. 13). Everything at the exchange configuration's working
depth (windows of ~ log log x gap letters, i.e., interval lengths around
log x . log log x, inside the paper's range log x << y = o((log x)^2)) is
explicitly conjectural: the only statement the paper makes there is the
prediction (1)/(Section 8.3 boxed Prediction, p. 26), flagged as heuristic.

2. The one genuinely useful unconditional supply: matched sieve-pattern
sites. Section 8 (p. 25) proves by CRT that S(X,y,z) = S(m,y,z) whenever
X == m (mod P(z)), with #I(N) >= x/P + O(1) >= x^{1-epsilon+o(1)} sites
when z <= epsilon log x. This is an unconditional mechanism producing
enormously many pairs of sites whose entire pre-sieved word (the pattern of
integers coprime to P(z) across a window of any length y = x^{o(1)})
matches EXACTLY - far stronger than matching a J-prefix and K-suffix. If
the exchange configuration could be run at the level of sieve words rather
than prime-gap words, this supplies the site pairs for free at density
x^{-epsilon}. The gap to the project's need is precisely that a matched
sieve word does not force a matched gap word: converting "same coprimality
pattern" into "same positions of actual primes" is the tuple-type step, and
the paper is blunt that this is unavailable - footnote 9, p. 18:
"Surprisingly there is no way known to try to prove this" (about
Hardy-Littlewood (10)), and p. 17: even exhibiting one interval realizing
S(3432) = 481 "involves finding a prime 481-tuple, which would be an
extraordinary challenge". This is blocker (ii) restated with anchors.

3. On blocker (i) (pigeonhole blind to variability): the paper's calibrated
variability scale at depth y = t(log x)^2 is k_+- = (t +- (2t)^{1/2} + 1/3
- O(1/t^{1/2})) log x (Section 7.1, p. 23), i.e., fluctuations of order
sqrt(t) log x primes between extreme sites - but this is a statement about
B(N, 1/L), transferred to primes only via the Section 8 heuristic. The only
unconditional variability theorem cited is Maier's (Sections 1.5 and 2.2):
it gives abnormal sites only for y = (log x)^A with A > 2 strictly (not the
intermediate range), only along special sequences x_+ and x_- which are
DIFFERENT for excess and deficit (so it does not hand you two comparable
sites in one dyadic block), and with constants sigma_+-(A) whose true
values are blocked by Siegel zeros (Section 3, p. 15: "we are stuck").
Nothing here converts model variance into an unconditional middle-difference
dominance at depth log_2 log x.

4. On blocker (iii) (circularity of site densities at depth): the paper
supplies two relevant calibration warnings. First, the FGKMT quote (Section
2.1, p. 13): methods "looking only at divisibility by small primes" are
believed to cap at y = (log x)(log log x)^{2+o(1)} - i.e., the known
unconditional small-prime toolkit dies just above the exchange window scale
log x . log log x. Second, the paper's own model fails quantitatively in
computable ranges even after divisibility correction: Appendix B (p. 33)
shows the independent-model variance (12.95-13.90) overshoots the true
variance (10.82-11.34), matched instead by Montgomery-Soundararajan; and
Appendix A's best refined max-gap prediction (1420) remains "unaccountably
larger than the truth" (1248) at log x = 40 (p. 30). So even MODEL-level
site frequencies at (log x)^2 depth are off by secondary terms in real
ranges; any project argument that borrows model densities for rare
configurations should treat them as upper-bound-shaped heuristics, not
inputs. The paper's own repair proposal - a dependent model with
Montgomery-Soundararajan variance (p. 35) - is deferred to future work and
would (their footnote 15) change secondary terms of the very tail
predictions relevant to gap configurations.

5. The Maier phenomenon correction (focus 3) is fully explicit here: the
naive Cramer model's failures are enumerated (Section 5, pp. 19-20: prime
pairs n, n+1; M(x,y) = y up to log x; equidistribution in all residue
classes), the corrected model is defined precisely (p. 20), and the
corrected predictions differ from Cramer's at the (log x)^2 scale by the
constants c_-^{-1} >= 2 e^{-gamma} = 1.1229... for max gaps (Section 1.4,
p. 7) and c_+ = sigma_+(2) >= 1.015 for maxima (Sections 1.3, 3.1). For the
project this is a template: any model-based sanity check on gap-word
frequencies at depth ~ log_2 log x must use the divisibility-corrected
model, and even that is known (Appendix B) to have the wrong dependence
structure.

6. Model-language discipline (focus 4): Section 14 above collects the
exemplars. The operative pattern to mirror: (a) prove theorems only about
the model object (Proposition 1 about B(N, 1/L)); (b) mark every transfer
with "our heuristic is that ... are distributed like ..." (p. 24) and label
outputs "Prediction:"; (c) name assumed constants as model assumptions
(footnote 3, p. 6); (d) state known-false model outputs as false (p. 20);
(e) record disagreement with data without rationalizing it ("unaccountably
larger", p. 30; "We have no explanation for that", p. 5). The project's
finding-layer prose about S = sum p_n/2^n should mirror exactly this
separation: binomial/model computations may be stated as lemmas; any claim
about actual gap words g_n must be marked conjectural unless it descends
from the short unconditional list in point 1.

7. Bottom line. This paper supplies: an unconditional matched-sieve-site
mechanism (Section 8 CRT periodicity) that solves the "matched windows"
half of the exchange configuration only at the sieve-word level; calibrated
(but model-only, and empirically imperfect) fluctuation scales at and below
(log x)^2 (Proposition 1, Section 7.1, Prediction 8.3); and precise
language discipline. It cannot supply the unconditional exchange
configuration itself: the sieve-word-to-gap-word conversion is the parity
wall (footnote 9, p. 18), the unconditional variability supply (Maier) is
at the wrong depth and wrong site structure (Section 2.2), and the paper
itself certifies that in the intermediate range log x << y = o((log x)^2)
nothing is known unconditionally beyond M(x,y) >= c log y and
Westzynthius-type m = 0 results (Sections 2.1, 4).
