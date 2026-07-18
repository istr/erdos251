# EXTRACTION: Kuperberg, "Sums of Singular Series with Large Sets and the Tail of the Distribution of Primes"

Source (only evidence base): /home/istr/pro/erdos251/dossier/2210.09775v2.pdf
arXiv:2210.09775v2 [math.NT] 15 Jun 2023. Author: Vivian Kuperberg. 20 pages
(as printed: body pp. 1-19, references p. 20). Funding footnote p. 1: "The
author is supported by NSF GRFP grant DGE-1656518 as well as the NSF
Mathematical Sciences Research Program through the grant DMS-2202128, and
would like to thank Kannan Soundararajan for many helpful comments and
discussions, as well as the anonymous referee for many helpful comments."

Transcription conventions: ASCII only. Diacritics transliterated (L'Hopital,
Cramer if any). Math in LaTeX-like ASCII: S(H) denotes the singular series
\frakS(\calH) of the paper; H denotes the set \calH = {h_1,...,h_k};
nu_H(p) the number of occupied residue classes mod p; D_H = prod_{i<j}
(h_i - h_j); 1_P = indicator of the primes; Lambda = von Mangoldt; {r ell}
= Stirling number of the second kind (Stirling2(r,ell)); sigma(r,ell) =
number of surjective maps [1,r] ->> [1,ell]; li_k(x) = int_2^x dy/(log y)^k;
phi = Euler phi; mu = Moebius; omega(q) = number of prime factors of q;
<= , >= , << (Vinogradov), <<_delta (implied constant depends on delta),
~ (asymptotic). "log^k x" = (log x)^k. Anchors are theorem/equation/section
numbers as printed; page numbers (printed page = PDF page) are secondary.
The paper uses both epsilon glyphs (\epsilon and \varepsilon); both are
transcribed "epsilon"/"eps" here without distinction.

Everything up to the final section is EXTRACTION (what the paper says).
Commentary appears ONLY in the final marked section.

---

## 1. ABSTRACT AND INTRODUCTION SETUP (verbatim)

Abstract (p. 1), verbatim:

> "In 1976, Gallagher showed that the Hardy--Littlewood conjectures on prime
> k-tuples imply that the distribution of primes in log-size intervals is
> Poissonian. He did so by computing average values of the singular series
> constants over different sets of a fixed size k contained in an interval
> [1, h] as h -> infty, and then using this average to compute moments of
> the distribution of primes. In this paper, we study averages where k is
> relatively large with respect to h. We then apply these averages to the
> tail of the distribution. For example, we show, assuming appropriate
> Hardy--Littlewood conjectures and in certain ranges of the parameters,
> the number of intervals [n, n + lambda log x] with n <= x containing at
> least k primes is << x exp(-k/(lambda e))."

Section 1 opening (p. 1), verbatim:

> "The Hardy--Littlewood prime k-tuple conjectures state that if
> H = {h_1,...,h_k} is a set of k distinct integers, then as x -> infty,
> (1)  sum_{n<=x} prod_{i=1}^k Lambda(n + h_i) = (S(H) + o(1)) x,
> where S(H) is the singular series
> (2)  S(H) = prod_{p prime} (1 - nu_H(p)/p) / (1 - 1/p)^k,
> and nu_H(p) denotes the number of distinct residue classes modulo p
> occupied by the elements of H."

Gallagher's average (p. 1), verbatim:

> "For example, in [3], Gallagher showed that the Hardy--Littlewood
> conjectures imply that the distribution of primes in log-size intervals is
> Poissonian. He did so by showing that for fixed k and as h -> infty,
> (3)  sum_{h_1,...,h_k <= h, distinct} S(h_1,...,h_k)
>        ~ sum_{h_1,...,h_k <= h, distinct} 1,
> so that singular series for sets of size k have value 1 on average as
> their elements grow large."

Montgomery--Soundararajan sentence (p. 1), verbatim (see Section 9 below):

> "In [10], Montgomery and Soundararajan computed second-order terms of this
> average in order to show that, assuming a version of the Hardy--Littlewood
> conjectures with a stronger error term, primes in somewhat longer
> intervals obey an appropriate Gaussian distribution. For both of these
> analyses, k is fixed throughout."

Framing of the present paper (Section 1, p. 2), verbatim:

> "What about when k is not fixed? Here we study sums of singular series for
> sets of size k with elements in [1, h], where k -> infty as h -> infty.
> Put another way, we study the rate at which the average value of S(H)
> converges to 1, in order to extend Gallagher's proof to larger k."

---

## 2. MAIN THEOREMS 1.1 AND 1.2 WITH EXACT REGIMES (verbatim) [FOCUS 1]

Theorem 1.1 (Section 1, p. 2), verbatim:

> "Theorem 1.1. Fix delta > 1/2, and let h, k in N with
> k = O((log h)^{1-delta}). Let T_k(h) be given by
> (4)  T_k(h) := sum_{h_1,...,h_k <= h, distinct} S(h_1,...,h_k),
> Then there exists a beta > 0, dependent only on delta > 1/2, with
>   T_k(h) = h^k + O(h^{k-beta})."

Immediately following paragraph (p. 2), verbatim:

> "In particular, Theorem 1.1 states that (3) holds whenever
> k = O((log h)^{1-delta}) for some delta > 1/2. One might expect the
> average value of 1 to extend to still larger k; for example, it is
> reasonable to conjecture that (3) would hold whenever k = O((log h)^2).
> For arbitrarily large k, Theorem 1.2 provides a bound on the average
> value of k-term singular series over sets with elements in [1, h]."

Theorem 1.2 (Section 1, p. 2), verbatim:

> "Theorem 1.2. Let k, h in N, with no conditions on their relative growth
> rates. Define T_k(h) by (4). Then
> (5)  T_k(h) << h^k prod_{p <= k^3} 1/(1 - 1/p)^k << h^k (3 log k)^k."

Immediately following paragraph (p. 2), verbatim:

> "This upper bound is likely much weaker than the truth, but it has the
> advantage of bounding the average value only in terms of k. Instead of
> taking p <= k^3, in our proof we can take p <= k^{2+eps} for any eps > 0,
> which has the effect of replacing the 3^k in the final bound with a
> (2+eps)^k. However, the final bound is in any case e^{O(k log log k)}.
> Theorems 1.1 and 1.2 are proven in Section 2."

VERIFICATION AGAINST THE PROJECT'S NOTES (extraction-level check, both
displays re-read from p. 2 of the PDF):
- Theorem 1.1: the regime is EXACTLY "Fix delta > 1/2, and let h, k in N
  with k = O((log h)^{1-delta})", with beta = beta(delta) > 0 and
  conclusion T_k(h) = h^k + O(h^{k-beta}). The project's claim
  "Thm 1.1 needs k = O((log h)^{1-delta})" is CORRECT, with the essential
  additional constraint delta > 1/2 (so k is below (log h)^{1/2}); the
  asymptotic (3) is thereby established for k = O((log h)^{1-delta}),
  delta > 1/2, only.
- Theorem 1.2: the statement is EXACTLY "with no conditions on their
  relative growth rates" and display (5): T_k(h) << h^k prod_{p<=k^3}
  (1-1/p)^{-k} << h^k (3 log k)^k. The project's claim "T_k(h) << h^k
  (3 log k)^k with NO growth condition" is CORRECT verbatim.

---

## 3. DEFINITION OF T_k(h) AND VARIANTS [FOCUS 2]

Primary definition, eq. (4) (Theorem 1.1, p. 2), verbatim (repeated):

> "(4)  T_k(h) := sum_{h_1,...,h_k <= h, distinct} S(h_1,...,h_k),"

Reading (supported by the surrounding text and by the main term h^k):
the sum is over ORDERED k-tuples (h_1,...,h_k) of pairwise DISTINCT
positive integers, each at most h, UNWEIGHTED; S is evaluated on the
underlying set. The count of such tuples is h^k(1+O(k^2/h)) (each
unordered set counted k! times), consistent with the main term h^k in
Theorem 1.1 and with (3), whose right-hand side is
sum_{h_1,...,h_k <= h, distinct} 1. In Section 3 the same convention
appears with explicit lower limit, e.g. "sum_{1 <= h_1,...,h_ell <= h,
distinct}" (p. 14). No unordered variant, no weight, and no
non-distinct variant of T_k(h) is defined anywhere in the paper.

Auxiliary variant S_k(h) (proof of Theorem 1.2, p. 12), verbatim:

> "Let S_k(h) refer to the sums above, so that
>   S_k(h) := sum_{1 <= h_1,...,h_k <= h, distinct} (k choose 2)^{-1}
>     sum_{1<=i<j<=k} exp( 2 (k choose 2)
>       sum_{p | (h_i - h_j), p > k^3} 1/p )."

Related non-distinct sums appear only in the moment computations, where
sums over not-necessarily-distinct r-tuples are decomposed via Stirling
numbers into sums over distinct ell-tuples (p. 14, display quoted in
Section 7 below; and p. 8, N(vec nu) = number of k-tuples of "not
necessarily distinct" integers occupying prescribed residue-class counts).

---

## 4. THE UNIFORM HARDY-LITTLEWOOD CONJECTURE (input hypothesis)

Preceding sentence (Section 1, p. 3), verbatim:

> "Since k = |H| grows with x in our setting, our results rely on a version
> of the Hardy--Littlewood conjectures which admits uniformity in the size
> of the set H; we state this version here."

Conjecture 1.3 (p. 3), verbatim:

> "Conjecture 1.3 (Hardy--Littlewood k-tuples conjecture, uniform version).
> There exist two absolute constants eps > 0 and C > 0 such that for all x,
> for all k <= (log log x)^3, and for all admissible tuples
> H = {h_1,...,h_k} subset [0, (log x)^2],
> (7)  | sum_{n<=x} 1_P(n+h_1) ... 1_P(n+h_k) - S(H) li_k(x) | <= C x^{1-eps}.
> Equivalently, for possibly different values of eps and C,
> (8)  | sum_{n<=x} Lambda(n+h_1) ... Lambda(n+h_k) - S(H) x | <= C x^{1-eps}."

> "Here li_k(x) is the k-th logarithmic integral, given by
> li_k(x) := int_2^x dy/(log y)^k."

Discussion of plausibility/breakdown (p. 3), verbatim:

> "When k = 10, this conjecture would suggest that for x = 5500, the error
> term above is bounded by Cx^{1-eps} for some eps and some C. For several
> sets of size 10, computer tests found that bounds of (log x)^6 x^{1/2}
> held for all x <= 5500; in fact this and other tests for small values of
> k suggest that the error term is far smaller, and for example may be
> bounded by Cx^{1/2}(log x)^k in this range of k and h. It is also likely
> possible to extend the range of k and h in this conjecture; if k is as
> large as log x, then li_k(x) is small enough that the conjecture is not
> so meaningful, but it is difficult to say when Hardy--Littlewood
> convergencee should break down."
> [TRANSCRIPTION-UNSURE: "convergencee" is as rendered; presumably a typo
> for "convergence".]

---

## 5. CONDITIONAL MOMENT AND TAIL RESULTS (verbatim) [FOCUS 4]

Bridge sentence (p. 3), verbatim:

> "Gallagher's proof in [3] that the distribution of primes in log-size
> intervals is (conditionally) Poissonian proceeds by computing moments.
> One strategy towards understanding the tail of the distribution is to
> estimate higher moments of the distribution, or equivalently, to
> understand how quickly the r th moment of the distribution of primes
> converges to the r th moment of a Poisson distribution. Using Conjecture
> 1.3 as well as Theorems 1.1 and 1.2, we can prove the following result
> on moments of the distribution of primes."

Theorem 1.4 (p. 3), verbatim:

> "Theorem 1.4. Assume Conjecture 1.3. Let x > 0, and assume that
> h = lambda log x and that r << (log h)^{1-delta} for some delta > 1/2.
> Define the r th moment m_r(x,h) of the distribution of primes in
> intervals of size h by
> (9)  m_r(x,h) = (1/x) sum_{n<=x} (pi(n+h) - pi(n))^r .
> Then
>   m_r(x,h) = ( sum_{ell=1}^{r} {r ell} lambda^ell ) (1 + o(1)),
> where {r ell} denotes the Stirling numbers of the second kind.
> Remark. Note that lambda need not be fixed as x -> infty."

Corollary 1.5 (p. 4), verbatim:

> "Corollary 1.5. Assume Conjecture 1.3. Let x > 0 and set h = lambda log x,
> where lambda(x) is nondecreasing as x -> infty. Let
> k << (log h)^{1-delta} for some delta > 1/2 and assume that
> k/(lambda+1) -> infty as x -> infty. Let I(x;k,h) be given by
> (10)  I(x;k,h) := # { n <= x : pi(n+h) - pi(n) >= k } .
> If lambda >= 1, then as x -> infty,
>   I(x;k,h) << x exp( - k/(lambda e) ).
> Otherwise,
>   I(x;k,h) << x exp( - k/((lambda+1) e) )."

Corollary 1.6 (p. 4), verbatim:

> "Corollary 1.6. Assume Conjecture 1.3. Let x > 0, and assume that
> h = lambda log x; let k = k(x) be an integer with no growth rate
> assumptions. Let I(x;k,h) be defined as in (10). Then for any
> delta > 1/2, as x -> infty,
>   I(x;k,h) <<_delta x exp( (log h)^{1-delta} ( log(lambda+1)
>     + (1-delta) log log h - log k ) )."

Following example (p. 4), verbatim:

> "For example, taking k = log h, Corollary 1.6 says that for all
> delta > 1/2, assuming Conjecture 1.3,
>   I(x; log h, h) <<_delta x exp( (log h)^{1-delta}
>     ( log lambda - delta log log h ) )."

Maynard comparison (p. 4), verbatim:

> "In [9], Maynard proves lower bounds on the same problem, showing that
> for any x, y >= 1 there are >> x exp(-sqrt(log x)) integers n <= x such
> that pi(n+y) - pi(n) >> log y, which in this case corresponds to the
> condition that there are >> log log x primes in intervals of width
> lambda log x. Both upper and lower bounds are reasonably far from the
> Poisson prediction in (6)."

where (6) (p. 2), verbatim:

> "(6)  (1/x) # { n <= x : pi(n + lambda log x) - pi(n) >= log log x }
>   approx (e lambda)^{log log x} e^{-lambda} / (log log x)^{log log x}."

Poisson-extension speculation (p. 4), verbatim:

> "It seems reasonable to conjecture that the Poisson prediction should
> still hold when k ~ log h or k ~ (log h)^2, and perhaps even larger. At
> this point, both upper and lower bounds are far from matching this
> conjecture."

Conjecture 1.7 (p. 4), verbatim:

> "Conjecture 1.7. Let x > 1 and let h = lambda log x, with
> lambda = o((log x)^eps) for all eps > 0. Let k << (log h)^2. Define
> (11)  pi_k(x;h) := # { n <= x : pi(n+h) - pi(n) = k }.
> Then pi_k(x;h) ~ x lambda^k e^{-lambda} / k! as x -> infty."

---

## 6. UNCONDITIONAL RESULTS (verbatim) [FOCUS 4]

Setup paragraph (p. 4), verbatim:

> "In Section 4, we prove unconditional bounds on the tail of the
> distribution of primes. For these arguments we use a Selberg sieve bound
> instead of applying the Hardy--Littlewood conjectures. The Selberg sieve
> bound for prime k-tuples has an extra factor of 2^k k! from the
> Hardy--Littlewood prediction. This factor is larger than our bound on
> the average of k-term singular series in Theorem 1.2, so the following
> unconditional bound is weaker than the moment bounds in Theorem 1.4.
> However, this weaker bound applies for much larger moments; in
> particular, for the r th moment when r = o((log x)^{1/4})."

Theorem 1.8 (p. 4), verbatim:

> "Theorem 1.8. Let x > 0, let h = lambda log x = o(x) and let
> r = o((log x)^{1/4}). Define the r th moment m_r(x,h) of the distribution
> of primes in intervals of size h as in (9). Then
>   m_r(x,h) << (lambda+1)^r r^{2r} e^{O(r log log r)}."

Corollary 1.9 (p. 5), verbatim:

> "Corollary 1.9. Let x > 0, let h = lambda log x, where lambda is a
> nondecreasing function of x. Let k be an integer dependent on x and
> assume that k = o((log x)^{1/6}) and that k/lambda -> infty as
> x -> infty. Define I(x;k,h) as in (10). Then for some constant C,
>   I(x;k,h) << x exp( - sqrt( k/((lambda+1)e) ) 2^{C/2}
>     ( log ( k/((lambda+1)e) ) )^{-C/2} )."

Prediction and Conjecture 1.10 (p. 5), verbatim:

> "It may also be possible to achieve weaker, yet nontrivial, bounds for
> larger k, along the lines of the bounds in Corollary 1.6. We predict that
> the bound in Corollary 1.5 should hold for any k << (log h)^2, instead
> of merely k << (log h)^{1-delta}."

> "Conjecture 1.10. Let x > 1 and let h = lambda log x, with
> lambda = o((log x)^eps) for all eps > 0. Let k << (log h)^2, and define
> pi_k(x;h) as in (11). Then pi_k(x;h) << x exp(-k/(lambda e)) as
> x -> infty."

Perspective paragraph for lambda = 1 (p. 5), verbatim:

> "To put these results in perspective, let us consider the case when
> lambda = 1, i.e. primes in intervals of width log x. In [3], Gallagher
> shows that for fixed k, the number of n <= x such that the interval
> (n, n + log x] contains exactly k primes is asymptotic to the Poisson
> prediction x/(e k!), assuming the Hardy--Littlewood conjectures.
> Unconditionally, Gallagher shows in [3] that the number of n <= x such
> that (n, n + log x] contains exactly k primes is <~ x e^{-Ck}, for an
> absolute constant C."
> [Transcription note: "<~" renders the paper's \lesssim glyph.]

> "We instead consider the probability that an interval (n, n + log x]
> contains at least log log x primes. In this case, the Poisson prediction
> for the probability that an interval contains log log x primes is
> (log x) e^{-1} / (log log x)^{log log x}, which for any A > 0 is
> << 1/(log x)^A. In [9], Maynard proves a lower bound; namely, that at
> least >> x exp(-sqrt(log x)) intervals (n, n + log x], with n <= x,
> contain >> log log x primes. In Corollary 1.6 we show that, assuming the
> uniform Hardy--Littlewood conjectures, for all delta > 1/2, the number of
> n <= x such that (n, n + log x] contains at least log log x primes is
> <<_delta x exp( - delta log log log x (log log x)^{1-delta} ).
> Unconditionally, we show in Corollary 1.9 that there exists C > 0 such
> that the number of (n, n + log x] containing at least log log x primes
> is << x exp( - sqrt(2^C / e) (log log x)^{1/2}
> (log log log x - 1)^{-C/2} )."
> [TRANSCRIPTION-UNSURE: in the last display the placement of the "- 1"
> inside "(log log log x - 1)^{-C/2}" and the exact form "sqrt(2^C/e)" are
> small-type; transcribed from the rendered page.]

> "When k is slightly smaller than log log x, that is, when
> k << (log h)^{1-delta}, Corollary 1.5 achieves the bound of
> 1/(log x)^A with A = 1/(lambda e). Bounding this probability by
> 1/(log x)^A for any A > 0 may be within reach even if the Poisson
> prediction itself is not. On the other hand, many questions concerning
> the tail of the distribution of primes are quite delicate, especially
> concerning the maximum and minimum number of primes in an interval of a
> certain size. For example, in [7], Maier proved that intervals of size
> (log x)^A for A > 2 can contain surprisingly few or surprisingly many
> primes. For more information, see [4]. The tail of the distribution of
> primes is also studied in [2]."

Granville--Lumley context (p. 2), verbatim:

> "In [4], Granville and Lumley conjecture that if y <= log x and
> x, y -> infty, the lim sup of the number of primes in intervals
> (x, x+y] is ~ y/log y, and if log x <= y = o((log x)^2), the lim sup
> should be given by (log x) / log( (log x)^2 / y ). They also formulate
> conjectures for larger intervals."

Gallagher fixed-lambda Poisson statement (p. 2), verbatim:

> "The expected number of primes in such an interval is much smaller; for
> a constant lambda, there are on average lambda primes in an interval
> (x, x + lambda log x], and Gallagher [3] showed that for fixed
> lambda > 0, assuming the Hardy--Littlewood conjectures,
>   lim_{x->infty} (1/x) # { n <= x :
>     pi(n + lambda log x) - pi(n) = k } = lambda^k e^{-lambda} / k! ."

---

## 7. METHOD ANATOMY, SECTION 2: PROOF OF THEOREM 1.1 [FOCUS 3]

Section 2 opener (p. 5), verbatim: "In this section, we prove Theorems 1.1
and 1.2. We begin with Theorem 1.1, whose proof closely follows Gallagher's
original proof in [3]."

### 7a. Local factors and their bounds

(p. 5, verbatim:) "Proof of Theorem 1.1, following Gallagher. Let
nu_H(p) := # H mod p. For a set H = {h_1,...,h_k}, write
D_H = prod_{i<j} (h_i - h_j), so that nu_H(p) = k unless p | D_H. Define

>   a(p, nu) := ( p^k - nu p^{k-1} - (p-1)^k ) / (p-1)^k ,

so that the p th factor of S(H) is given by
(1 - nu_H(p)/p)/(1 - 1/p)^k = 1 + a(p, nu_H(p))." (continuation p. 6.)

(p. 6, verbatim:) "For any prime p > k,

>   a(p,k) = sum_{j=2}^{k} (p-1)^{-j} (k choose j) (1-j) << k^2 (p-1)^{-2}.

This and a similar computation for nu < k shows that for p > k,

> (12)  |a(p,nu)| << { k^2 (p-1)^{-2}  if nu = k ;
>                    { k^2 (p-1)^{-1}  if nu < k .

For p <= k,

> (13)  |a(p,nu)| = | -1 + (1 - nu/p)/(1-1/p)^k | <= (1 - 1/p)^{-k}
>         < e^{2k/p},

since (1-1/p)^{-k} = exp( k sum_{j=1}^{infty} 1/(j p^j) )
< exp( k / (p(1-1/p)) ) <= exp(2k/p)."

(p. 6, verbatim:) "For squarefree q, write
a_H(q) := prod_{p|q} a(p, nu_H(p)), so that

>   S(H) = prod_{p<=k} (1 - nu_H(p)/p)/(1-1/p)^k
>     sum_{q>=1, p|q => p>k} mu^2(q) a_H(q)."

### 7b. Tail of the q-sum: Rankin's trick and the delta > 1/2 constraint

(p. 6, verbatim:) "Using the bounds on a(p,nu), for any x,

>   sum_{q>x, p|q => p>k} |a_H(q)| <= sum_{q>x, p|q => p>k}
>     mu^2(q) (C k^2)^{omega(q)} / phi^2(q) * phi((q, D_H)),

where omega(q) is the number of prime factors of q and C is an absolute
positive constant." Then, "Writing q = de with d | D_H and (e, D_H) = 1,
this is

> (14)  sum_{d|D_H, p|d => p>k} mu^2(d) (Ck^2)^{omega(d)} / phi(d)
>         sum_{e > x/d, (e,D_H)=1, p|e => p>k}
>           mu^2(e) (Ck^2)^{omega(e)} / phi^2(e)."

"Apply Rankin's trick to bound the inner sum, so that for any choice of
fixed alpha with 0 < alpha < 1, [inner sum] <= sum_{e>=1, (e,D_H)=1,
p|e => p>k} (e/(x/d))^alpha mu^2(e)(Ck^2)^{omega(e)}/phi^2(e). By
multiplicativity, this is

>   = (d/x)^alpha prod_{p>k, p !| D_H} (1 + C k^2 p^alpha / (p-1)^2)
>     <= (d/x)^alpha exp( C k^2 sum_{p>k} p^alpha/(p-1)^2 )
>     << (d/x)^alpha e^{C k^{1+alpha}}."

[TRANSCRIPTION-UNSURE: the product's subscript condition "p !| D_H"
(p does not divide D_H) is small type; forced mathematically by the
condition (e, D_H) = 1.]

THE delta > 1/2 CONSTRAINT (p. 7 top), verbatim:

> "Since 1/2 < delta < 1, we can choose alpha > 0 small enough that
> (1-delta)(2+2 alpha) + alpha < 1, which also implies that
> (1-delta)(1+alpha) < 1."

(p. 7, verbatim, the chain that uses it:) "Plugging the bound for the inner
sum into (14), we get that (14) is

>   << sum_{d|D_H} mu^2(d)(Ck^2)^{omega(d)}/phi(d) (d/x)^alpha
>       e^{Ck^{1+alpha}}
>    = (e^{Ck^{1+alpha}}/x^alpha) sum_{d|D_H}
>       mu^2(d)(Ck^2)^{omega(d)} d^alpha / phi(d).

For any d <= D_H, we have that d/phi(d) << log log D_H, so that this
expression becomes

>   << (e^{Ck^{1+alpha}}/x^alpha)(log log D_H) sum_{d|D_H}
>       mu^2(d)(Ck^2)^{omega(d)} d^alpha / d
>    = (e^{Ck^{1+alpha}}/x^alpha)(log log D_H)
>       prod_{p|D_H} (1 + Ck^2/p^{1-alpha}).

Since (1-delta)(1+alpha) < 1, e^{Ck^{1+alpha}}/x^alpha <<_eps
h^eps/x^alpha. Moreover, the quantity D_H is at most h^{(k choose 2)},
since it is a product of (k choose 2) quantities h_i - h_j, each of which
are < h. Thus log log D_H <= log log h^{(k choose 2)} << log log h, so in
fact the product of all terms outside the product are <<_eps
h^eps/x^alpha. It remains to understand the product, which is bounded by

>   prod_{p|D_H} (1 + Ck^2/p^{1-alpha})
>     <= exp( sum_{p|D_H} Ck^2/p^{1-alpha} )
>     <= exp( 2Ck^2 sum_{p <= (k choose 2) log h} 1/p^{1-alpha} ).

The sum over primes satisfies

>   sum_{p <= (k choose 2) log h} 1/p^{1-alpha}
>     = ( (k choose 2)^alpha (log h)^alpha )
>       / ( alpha log( (k choose 2) log h ) ) (1 + o(1)),

for example by applying partial summation and L'Hopital's rule, so that

>   exp( 2Ck^2 sum_{p <= (k choose 2) log h} 1/p^{1-alpha} )
>     << exp( (4Ck^2/alpha) (k choose 2)^alpha (log h)^alpha / log log h )
>     << exp( (4C/(2^alpha alpha)) k^{2+2alpha} (log h)^alpha / log log h )
>     << exp( (4C/(2^alpha alpha)) (log h)^{(1-delta)(2+2alpha)+alpha}
>          / log log h ).

Since (1-delta)(2+2alpha)+alpha < 1, this quantity is <<_eps h^eps, so
(14) is <<_eps h^{2 eps}/x^alpha, say. Set x = h^{1/2}, and choose
eps > 0 small enough that 2 eps < (1/2) alpha."

### 7c. Main term: CRT counting and the Gallagher cancellation A(q) = 0

(p. 7 bottom, verbatim:) "This is true for any set H = {h_1,...,h_k}, so
it follows that

> (15)  T_k(h) = sum_{q<=x, p|q => p>k} sum_{r>=1, p|r => p<=k}
>          sum_{h_1,...,h_k<=h, distinct} a_H(qr)
>        + O( (h^{2 eps}/x^alpha) sum_{h_1,...,h_k<=h, distinct}
>          prod_{p<=k} (1 - nu_H(p)/p)/(1-1/p)^k ),

where we have additionally expanded the terms of the product with p <= k
into the sum over r." (last clause from p. 8 top.)

Error term of (15) (p. 8), verbatim: "First consider the error term in
(15), which by (13) is

>   << (h^{2 eps}/x^alpha) h^k prod_{p<=k} ( e^{2k/p} )
>   << (h^{2 eps}/x^alpha) h^k e^{2k sum_{p<=k} 1/p}
>   << (h^{2 eps}/x^alpha) h^k e^{O(k log log k)}
>   << (h^{2 eps}/x^alpha) h^k e^{(log h)^{1-delta/2}}
>   << (h^{2 eps}/x^alpha) h^{k + o_delta(1)}."

[TRANSCRIPTION-UNSURE: the intermediate exponent "(log h)^{1-delta/2}";
the display is small; the final bound h^{k+o_delta(1)} is clear.]

(p. 8, verbatim:) "Now consider the main term. The sum over
h_1,...,h_k <= h in the main term of (15) can also be written as

>   sum_{vec nu = (nu_p)_{p|qr}, nu_p <= min{p-1,k}}
>     prod_{p|qr} a(p, nu_p) ( N(vec nu) + O(k h^{k-1}) ),

where N(vec nu) is the number of k-tuples of not necessarily distinct
integers h_1,...,h_k with 1 <= h_1,...,h_k <= h which occupy exactly
nu_p residue classes mod p for each p|qr. We can estimate N(vec nu) by
counting for each p|qr the number of h_1,...,h_k mod p that occupy
exactly nu_p residue classes and applying the Chinese Remainder Theorem.
Thus

>   N(vec nu) = prod_{p|qr} (p choose nu_p) sigma(k, nu_p)
>     ( h/(qr) + O(1) )^k,

where sigma(k,j) denotes the number of surjective maps [1,k] ->> [1,j];
we also have sigma(k,j) = j! {k j}, where {k j} is the Stirling number of
the second kind."

(p. 8, verbatim:) "Since x = h^{1/2} and prod_{p<=k} p = e^{O(k)}
= e^{O((log h)^{1-delta})} = h^{o(1)}, for any q <= x and r with all
prime factors <= k,

>   sum_{j=0}^{k-1} (h/(qr))^j (k choose j) << k^2 (h/(qr))^{k-1}.

Thus the inner sum in the main term of (15) is

> (16)  (h/(qr))^k A(qr) + O( k^2 (h/(qr))^{k-1} B(qr) )
>         + O( k h^{k-1} C(qr) ),"

[TRANSCRIPTION-UNSURE: "for any q <= x" -- the bound variable after
"for any q <=" is small type; read as x (the truncation parameter set to
h^{1/2}), consistent with the summation range q <= x in (15).]

with (p. 9, verbatim):

> "A(qr) = sum_{vec nu = (nu_p)_{p|qr}, nu_p <= min{p-1,k}}
>    prod_{p|qr} a(p, nu_p) (p choose nu_p) sigma(k, nu_p),
>  B(qr) = sum_{vec nu = (nu_p)_{p|qr}, nu_p <= min{p-1,k}}
>    prod_{p|qr} |a(p, nu_p)| (p choose nu_p) sigma(k, nu_p),  and
>  C(qr) = sum_{vec nu = (nu_p)_{p|qr}, nu_p <= min{p-1,k}}
>    prod_{p|qr} |a(p, nu_p)|."

THE CANCELLATION (p. 9), verbatim:

> "Just as in [3], A(q) = 0 for q > 1, and A(1) = 1."

[This single identity is where all cancellation in the singular-series
average comes from: the signed local sums sum_{nu} a(p,nu)(p choose nu)
sigma(k,nu) vanish at every prime p, so the entire main term collapses to
the q = 1 term (h/(qr))^k A(1) = h^k. Everything else in the proof is
absolute-value bookkeeping of B and C. Bracketed sentence is PARAPHRASE.]

### 7d. Error bookkeeping: C(qr) and B(qr)

(p. 9, verbatim:) "Now consider C(qr), which can be estimated using the
bounds (12) and (13) for a(p,nu). Write

>   C(qr) = prod_{p|qr} ( sum_{nu=1}^{min{p-1,k}} |a(p,nu)| ).

If p > k, the p th factor is << p k^2/(p-1), whereas if p <= k, this
factor is << p e^{2k/p}. Thus

> (17)  C(qr) <= (C_1 k^2)^{omega(q)} (q/phi(q)) C_1^{omega(r)} r
>         e^{2k sum_{p|r} 1/p},

for some absolute constant C_1, where without loss of generality
C_1 >= 1."

(p. 9, verbatim:) "After summing (17) over all q and r, the contribution
to T_k(h) from the factors coming from C(qr) in (16) is bounded by

>   << k h^{k-1} sum_{q<=x, p|q => p>k} sum_{r>=1, p|r => p<=k}
>        (C_1 k^2)^{omega(q)} (q/phi(q)) C_1^{omega(r)} r
>        e^{2k sum_{p|r} 1/p}
>   << k h^{k-1} prod_{p<=k} (1 + C_1 p e^{2k/p})
>        sum_{q<=x, p|q => p>k} (C_1 k^2)^{omega(q)} q/phi(q)
> (18)  << k h^{k-1} (2C_1)^{pi(k)} e^{sum_{p<=k} log p}
>        e^{2k sum_{p<=k} 1/p}
>        sum_{q<=x, p|q => p>k} (C_1 k^2)^{omega(q)} q/phi(q).

The terms outside the sum are << h^{k-1+o(1)} in the range where
k << (log h)^{1-delta}. We now examine the inside sum using Rankin's
trick. First note that q/phi(q) << log log q << log log h for
q <= x = h^{1/2}, so we may omit q/phi(q) from the sum while only losing
a factor of h^{o(1)}. Thus for any 0 < gamma < 2,

>   sum_{q<=x, p|q => p>k} (C_1 k^2)^{omega(q)} q/phi(q)
>     <= h^{o(1)} sum_{q, p|q => k<p<=x} (C_1 k^2)^{omega(q)}
>          (x/q)^{2-gamma}
>     << h^{o(1)} x^{2-gamma} prod_{k<p<=x} (1 + C_1 k^2 / p^{2-gamma})
>     << h^{o(1)} x^{2-gamma} exp( sum_{k<p<=x} C_1 k^2 / p^{2-gamma} )
>     << h^{o(1)} x^{2-gamma} exp( C_2 k^{1+gamma} / log k ),

for a possibly different positive constant C_2 > 0. We can now choose any
gamma > 0 such that (1-delta)(1+gamma) < 1; for example, choose
gamma = alpha. Then since x = h^{1/2} and k << (log h)^{1-delta},

> (19)  sum_{q<=x, p|q => p>k} (C_1 k^2)^{omega(q)} q/phi(q)
>         << h^{o(1)} x^{2-alpha} exp( C_2 k^{1+alpha} / log k )
>         << h^{1-alpha/2+o_delta(1)}.

Plugging (19) into (18) shows that the contribution to T_k(h) from the
factors corresponding to C(qr) is << h^{k-alpha/2+o_delta(1)}."
(pp. 9-10.)

(p. 10, verbatim:) "Finally, consider B(qr). Just as with C(qr), B(qr) is
multiplicative, and the p th factor of B(qr) is given by

>   sum_{nu=1}^{min{p-1,k}} |a(p,nu)| (p choose nu) sigma(k,nu),

which by (13), (12), and the fact that
sum_{nu=1}^{p} (p choose nu) sigma(k,nu) = p^k, is

>   << { k^2 p^k/(p-1)   if p > k ;
>      { e^{2k/p} p^k    if p <= k .

Thus for some absolute constant C_2 >= 1, and after summing over all q
and r, the contribution to T_k(h) from the B(qr) factors in (16) is

>   << sum_{q<=x, p|q => p>k} sum_{r>=1, p|r => p<=k}
>        k^2 (h/(qr))^{k-1} ((C_2 k^2)^{omega(q)} q^k / phi(q))
>        C_2^{omega(r)} r^k e^{2k sum_{p|r} 1/p}
>   << k^2 h^{k-1} sum_{q<=x, p|q => p>k} ((C_2 k^2)^{omega(q)} q/phi(q))
>        prod_{p<=k} (1 + C_2 e^{2k/p} p).

For k << (log h)^{1-delta}, the product over p <= k is

>   prod_{p<=k} (1 + C_2 e^{2k/p} p) << (2C_2)^k prod_{p<=k} e^{2k/p} p
>     = (2C_2)^k exp( sum_{p<=k} 2k/p + log p )
>     << (2C_2)^k e^{3k log log k} = h^{o_delta(1)},"

(p. 11, verbatim:) "so the overall sum is

>   << k^2 h^{k-1+o_delta(1)} sum_{q<=x, p|q => p>k}
>        (C_2 k^2)^{omega(q)} q/phi(q).

Applying (19) with the same choice of gamma shows that the contribution
to T_k(h) from the B(qr) factors is << h^{k-alpha/2+o_delta(1)}."

### 7e. Conclusion of the proof of Theorem 1.1 (p. 11), verbatim

> "Combining the contributions from A(1), the sums over q and r of B(qr)
> and C(qr), and the error term in (15), we get that
>   T_k(h) = h^k + O( h^{k-alpha/2+o_delta(1)}
>     + (h^{2 eps}/x^alpha) h^{k+o_delta(1)} ),
> which for x = h^{1/2} is h^k + O(h^{k-beta}) for
> beta < (1/2) alpha - 2 eps. Our choice of alpha depends only on delta,
> so beta also depends only on delta, as desired."

---

## 8. BARRIER AT LARGER k, AND THEOREM 1.2 (Lemma 2.1) [FOCUS 3, 5]

THE BARRIER PARAGRAPH (p. 11, immediately after the Thm 1.1 proof),
verbatim:

> "The techniques relying on the Chinese Remainder Theorem break down for
> larger k, where they do not give a bound with the correct power of h. We
> will now turn to Theorem 1.2, which bounds T_k(h) for any k where the
> dependence on h is h^k, which is approximately the number of terms in
> the sum. In other words, Theorem 1.2 provides a bound that is uniform in
> h on the average value of k-term singular series for sets with elements
> that are at most h. The proof of Theorem 1.2 relies on Lemma 2.1, which
> is a uniform bound on S(H) for H subset [1, h] satisfying the conditions
> of Theorem 1.2."

Lemma 2.1 (p. 11), verbatim (the k-uniformity carrier for Theorem 1.2):

> "Lemma 2.1. Let H = {h_1,...,h_k} be a set of distinct integers. Define
> S(H) as in (2). Then
> (20)  S(H) << prod_{p<=k^3} 1/(1-1/p)^k
>         prod_{p>k^3} (1-k/p)/(1-1/p)^k
>         (k choose 2)^{-1} sum_{1<=i<j<=k}
>           exp( 2 (k choose 2) sum_{p|(h_i-h_j), p>k^3} 1/p )."

Proof skeleton (pp. 11-12), displays verbatim:

> "By definition,
>   S(H) = prod_{p prime} (1 - nu_H(p)/p)/(1-1/p)^k
>     <= prod_{p prime, p<=k^3} 1/(1-1/p)^k
>        prod_{p prime, p>k^3} (1 - nu_H(p)/p)/(1-1/p)^k
> (21) = prod_{p<=k^3} 1/(1-1/p)^k prod_{p>k^3} (1-k/p)/(1-1/p)^k
>        prod_{p|Delta(H), p>k^3} (p - nu_H(p))/(p - k)."

[TRANSCRIPTION-UNSURE: the symbol in the last product's condition is
rendered Delta(H); by its role it is the same discriminant-type quantity
as D_H = prod_{i<j}(h_i - h_j).]

(p. 12, verbatim:) "Rewrite the product inside via

>   prod_{p|Delta(H), p>k^3} (p - nu_H(p))/(p - k)
>     <= exp( sum_{p|Delta(H), p>k^3} (k - nu_H(p))/(p - k) )
>     << exp( 2 sum_{1<=i<j<=k} sum_{p|(h_i-h_j), p>k^3} 1/p )
>     <= (k choose 2)^{-1} sum_{1<=i<j<=k}
>          exp( 2 (k choose 2) sum_{p|(h_i-h_j), p>k^3} 1/p ),

where the last step comes from Jensen's inequality; plugging this into
(21) yields the result."
[TRANSCRIPTION-UNSURE: the numerator in the first exponential,
(k - nu_H(p)) vs (p - nu_H(p)): the print is small; (k - nu_H(p)) is the
mathematically forced reading of (p-nu)/(p-k) = 1 + (k-nu)/(p-k)
<= exp((k-nu)/(p-k)), and matches the next line which bounds k - nu_H(p)
by the number of pairs (i,j) with p | (h_i - h_j).]

Proof of Theorem 1.2 (pp. 12-13). After summing (20) over H (display
p. 12) and defining S_k(h) (quoted in Section 3 above), the chain (p. 13),
verbatim:

> "S_k(h) << (k choose 2)^{-1} sum_{1<=i<j<=k}
>    sum_{1<=h_1,...,h_k<=h, distinct}
>      exp( 2 (k choose 2) sum_{p|(h_i-h_j), p>k^3} 1/p )
>  << (k choose 2)^{-1} sum_{1<=i<j<=k} sum_{h_i,h_j<=h, distinct}
>      exp( 2 (k choose 2) sum_{p|(h_i-h_j), p>k^3} 1/p ) h^{k-2}
>  = h^{k-2} sum_{ell<=h} (h - ell)
>      exp( 2 (k choose 2) sum_{p|ell, p>k^3} 1/p )
>  <= h^{k-1} sum_{ell<=h}
>      exp( 2 (k choose 2) sum_{p|ell, p>k^3} 1/p )."

(p. 13, verbatim:) "The sum over ell is a sum over a multiplicative
function f_k(ell), with f_k(p^j) = 1 if p <= k^3 and
f_k(p^j) = exp(k(k-1)/p) if p > k^3, regardless of j. The function
f_k(ell) satisfies f_k(ell) = sum_{d|ell} g_k(d), where g_k is a
multiplicative function given by g_k(p^j) = 0 if p <= k^3 or j >= 2 and
g_k(p) = exp(k(k-1)/p) - 1 for p > k^3 prime. Then

>   sum_{ell<=h} f_k(ell) = sum_{ell<=h} sum_{d|ell} g_k(d)
>     = sum_{d<=h} g_k(d) floor(h/d) <= h sum_{d=1}^{infty} g_k(d)/d.

The sum over d can be rewritten as

>   prod_{p>k^3} ( 1 + (exp(k(k-1)/p) - 1)/p )
>     = exp( sum_{p prime, p>k^3} sum_{j>=1} (1/p) (k(k-1)/p)^j )
>     < exp( sum_{p prime, p>k^3} sum_{j>=1} 1/p^{1+j/3} ).

The sum in the exponent is bounded by a constant independent of k, and
thus the sum over d is bounded by a constant independent of k, so that
S_k(h) << h^k."
[TRANSCRIPTION-UNSURE: the middle relation is printed with an "=" sign
between the product and the first exp(...); as an identity it can only be
an upper bound (log(1+x) <= x and dropping j! from the expansion of
exp(y)-1); transcribed as printed.]

(p. 13, verbatim:) "Finally, return to the contribution from the small
primes and T_k(h), which is bounded by

>   T_k(h) << h^k prod_{p<=k^3} 1/(1-1/p)^k << h^k (3 log k)^k,

as desired."

[PARAPHRASE, mechanism summary: Theorem 1.2 uses NO cancellation at all --
Lemma 2.1 bounds each S(H) by absolute values (small primes trivially by
(1-1/p)^{-k}, large primes by an exponential of sum of 1/p over
p | (h_i-h_j), p > k^3, convexified by Jensen), and the average over H
of the resulting multiplicative weight is O(h^k) because
g_k(p) = exp(k(k-1)/p) - 1 is supported on p > k^3 where k(k-1)/p <
p^{-1/3}. The (3 log k)^k loss is exactly Mertens for the discarded
small-prime factor prod_{p<=k^3}(1-1/p)^{-k}.]

---

## 9. SECTION 3 ANATOMY: MOMENTS FROM SINGULAR-SERIES AVERAGES [FOCUS 4]

Section 3 header sentence (p. 13), verbatim: "Throughout, consider an
interval of size h = lambda log x. Fix delta > 1/2 and assume that
r << (log h)^{1-delta}. We begin with the proof of Theorem 1.4."

(p. 14, verbatim:) "The r th moment m_r(x,h), defined in (9), is given by

>   m_r(x,h) = sum_{1<=h_1,...,h_r<=h} (1/x) sum_{n<=x}
>     1_P(n+h_1) ... 1_P(n+h_r)
>   = sum_{ell=1}^{r} (sigma(r,ell)/ell!)
>     sum_{1<=h_1,...,h_ell<=h, distinct} (1/x) sum_{n<=x}
>     1_P(n+h_1) ... 1_P(n+h_ell),

where sigma(r,ell) is the number of surjective maps [1,r] ->> [1,ell],
and sigma(r,ell)/ell! = {r ell}, the Stirling number of the second kind."

(p. 14, verbatim:) "Apply Conjecture 1.3 to replace the sum over
correlations of primes with a sum over singular series, yielding

>   m_r(x,h) = sum_{ell=1}^{r} {r ell} (1/(log x)^ell)
>     sum_{1<=h_1,...,h_ell<=h, distinct}
>     ( S({h_1,...,h_ell}) + o(1) ).

Estimating this moment now depends on the average of the singular series
constants, and in particular how quickly this average converges to 1. We
apply our results from Section 2 bounding sums of singular series for
large sets, and in particular Theorem 1.1, which requires our assumption
that r << (log h)^{1-delta}. For larger r, one could also apply the
weaker result in Theorem 1.2 to yield a weaker moment bound."

(p. 14, verbatim:) "By Theorem 1.1, for any ell <= r << (log h)^{1-delta}
and for some beta > 0 dependent only on delta > 1/2,

>   sum_{1<=h_1,...,h_ell<=h, distinct} S(h_1,...,h_ell)
>     = h^ell + O(h^{ell-beta}).

Then for any r << (log h)^{1-delta},

>   m_r(x,h) = sum_{ell=1}^{r} {r ell} (1/(log x)^ell)
>       ( h^ell + O(h^{ell-beta}) )
>     + o( sum_{ell=1}^{r} (1/(log x)^ell) {r ell} h^ell )
>   = ( sum_{ell=1}^{r} {r ell} lambda^ell ) (1 + o(1)),

where the error term is uniform in r. This completes the proof of
Theorem 1.4."

Proof of Corollary 1.5 (pp. 14-15), verbatim:

> "Let r << (log h)^{1-delta}. Applying a Markov bound to the r th moment
> m_r(x,h), we get that
>   I(x;k,h) <= (x/k^r) m_r(x,h) << (x/k^r) sum_{ell=1}^r {r ell}
>     lambda^ell.
> As shown in [11, Theorem 3], Stirling numbers of the second kind are
> bounded above by {r ell} <= (1/2)(r choose ell) ell^{r-ell}, so
>   I(x;k,h) << (x/k^r) sum_{ell=1}^r (r choose ell) ell^{r-ell}
>     lambda^ell << (x/k^r)(lambda + r)^r."

(p. 15, verbatim:) "If lambda >= 1, then as x -> infty eventually
k/lambda >= lambda e/(lambda - 1), which in turn implies that we can
choose r = k/(lambda e) and get (lambda + r)^r <= (lambda r)^r. With this
choice of r, we thus get I(x;k,h) << x e^{-k/(lambda e)}, as desired.
Meanwhile if lambda < 1, we can choose r = k/((lambda+1)e) to get the
desired result, since (lambda + r)^r <= ((lambda+1) r)^r."
[TRANSCRIPTION-UNSURE: "lambda e/(lambda - 1)" as printed; degenerate at
lambda = 1 exactly, as printed.]

(p. 15, verbatim:) "Corollary 1.6 follows via the same argument as the
proof of Corollary 1.5, but where r is taken to be (log h)^{1-delta}."

Proof of Theorem 1.8 (p. 15), key displays verbatim:

> "For our choice of h and r, the error term in Theorem 4.1 is O(1).
> Applying Theorem 4.1, the r th moment is then bounded by
>   m_r(x,h) << sum_{ell=1}^{r} (sigma(r,ell)/(ell! (log x)^ell))
>     sum_{1<=h_1,...,h_ell<=h, distinct} (2+eps)^ell ell! S(H)
>   << sum_{ell=1}^{r} {r ell} ell! (1/(log x)^ell) (2+eps)^ell h^ell
>     e^{O(ell log log ell)},
> where the last step follows by applying Theorem 1.2. Since
> h = lambda log x, this sum is then
>   << r! (2+eps)^r e^{O(r log log r)} sum_{ell=1}^{r} {r ell}
>     lambda^ell."

(p. 16, verbatim:) "As seen in the proof of Corollary 1.5,
sum_{ell=1}^r {r ell} lambda^ell <= (lambda+r)^r <= ((lambda+1)r)^r, so
that

>   m_r(x,h) << r! (2+eps)^r e^{O(r log log r)} (lambda+1)^r r^r
>     << r^{2r} e^{O(r log log r)} (lambda+1)^r,

which gives the result."

Proof of Corollary 1.9 (p. 16), verbatim:

> "In this case, we know unconditionally from Theorem 1.8 that
>   I(x;k,h) <= (x/k^r) m_r(x,h)
>     << (x/k^r)(lambda+1)^r r^{2r} e^{O(r log log r)}.
> Hence there exists some constant C > 0 with
>   I(x;k,h) << (x/k^r)(lambda+1)^r r^{2r} e^{C r log log r}
>     = x exp( r log((lambda+1)/k) + 2r log r + C r log log r ).
> Choose r = ( k/((lambda+1)e) )^{1/2} 2^{C/2}
>   ( log( k/((lambda+1)e) ) )^{-C/2}, so that
>   log r = (1/2) log( k/((lambda+1)e) ) + (C/2) log 2
>     - (C/2) log log( k/((lambda+1)e) ),  and
>   log log r = log(1/2) + log( log( k/((lambda+1)e) )
>     - C log log( k/((lambda+1)e) ) + C log 2 )
>   <= log(1/2) + log log( k/((lambda+1)e) ),
> where the inequality holds for large enough x since k/lambda -> infty.
> Plugging in these expressions for log r and log log r gives
>   r log((lambda+1)/k) + 2r log r + C r log log r <= -r,
> so that I(x;k,h) << x e^{-r}, which completes the proof."

---

## 10. SECTION 4 ANATOMY: k-UNIFORM SELBERG SIEVE [FOCUS 3, 4]

Theorem 4.1 (p. 15), verbatim:

> "Theorem 4.1. Let x >= 2, let k = o((log x)^{1/4}), and let
> H = {h_1,...,h_k} be a set of k distinct natural numbers. For any
> eps > 0,
>   |{ n <= x : n + h_i prime for all i }|
>     <= (2+eps)^k k! S(H) (x / log^k x)
>        ( 1 + O( ( log log(3x) + k^4 + k log log(3|D_H|) ) / log x ) ),
> where D_H := prod_{i<j} (h_i - h_j)."

> "Theorem 4.1 extends the work of Klimov in [6], who shows an analogous
> bound for k fixed as x -> infty." (p. 15.)

Section 4.1 setup (p. 16), verbatim: "Selberg's sieve has previously been
used to bound the frequency of prime k-tuples; see for example [5], which
we will refer to throughout this section, as well as [1] and [6]. In [5],
Halberstam and Richert proceed along a very similar calculation, with the
only material difference being that we are not taking k to be a constant
in terms of the other parameters, and thus we keep track of the
dependence on k throughout. We proceed along the lines of [5, Theorem
5.7]."

Notation (p. 16, verbatim in substance): A := { prod_{i=1}^k (n+h_i) :
n <= x }; A_d = number of elements of A divisible by d, A_d =
(nu_H(d)/d) x + O(nu_H(d)) with nu_H(d) = prod_{p|d} nu_H(p);
R_d = A_d - (nu_H(d)/d) x, so |R_d| <= nu_H(d);
"(22) S(A;P,z) := |{ a : a in A, (a, P(z)) = 1 }|." with
P(z) := prod_{p<=z} p.

Halberstam--Richert conditions (p. 17), verbatim:

> "(R)    |R_d| <= nu_H(d) if mu(d) != 0;
>  (Omega_1)  0 <= nu_H(p)/p <= 1 - 1/alpha_1 for some constant
>    alpha_1 >= 1;
>  (Omega_2(kappa,L))  -L <= sum_{w<=p<z} (nu_H(p) log p)/p
>    - kappa log(z/w) <= alpha_2 for any z >= w >= 2."
> "For the final condition, alpha_2 and L are constants, each >= 1, which
> are independent of z and w. For our purposes, we will need to keep track
> of the values alpha_1, alpha_2, and L, and in particular their
> dependence on k."

Lemma 4.2 (p. 17), verbatim (the k-uniformity carrier for the sieve):

> "Lemma 4.2. For a set H = {h_1,...,h_k} and nu_H, D_H, A, A_d, and R_d
> defined as above, the conditions (R), (Omega_1), and (Omega_2(kappa,L))
> are satisfied with alpha_1 = k+1, alpha_2 = O(k), kappa = k, and
> L = k log log(3|D_H|)."

Its proof (p. 17), key displays verbatim: "We also have nu_H(p)/p <=
min{k, p-1}/p <= 1 - 1/(k+1), so that (Omega_1) is satisfied with
alpha_1 = k+1." And: "By [5, Lemma 5.1], for any natural number n,
sum_{p|n} (log p)/p << log log(3n), so

>   sum_{w<=p<z} (nu_H(p) log p)/p >= k log(z/w) - O(k)
>     - sum_{p|D_H} (k/p) log p
>     >= k log(z/w) - O(k) - O(k log log(3|D_H|)),

and thus (Omega_2(kappa,L)) is satisfied with kappa = k, alpha_2 = O(k)
and L = O(k log log(3|D_H|))."

Lemma 4.3 (p. 17), verbatim:

> "Lemma 4.3 (After Lemma 5.4 from [5]). Fix a set H = {h_1,...,h_k}, and
> define nu_H, g(d), G(x,z), and W(z). Let L = k log log(3|D_H|), and let
> z > 0 be a number such that for sufficiently large constants B_L and
> B_k, L <= (1/B_L) log z and k^2 <= (1/B_k) log z. Then
>   1/G(z) = W(z) e^{gamma k} Gamma(k+1)
>     ( 1 + O( (L + k^4)/log z ) )."

where (p. 17): "For d squarefree, let g(d) = nu_H(d) / ( d prod_{p|d}
(1 - nu_H(p)/p) ), let G(z) = sum_{d<z} mu(d)^2 g(d), and more generally
for any x define G(x,z) = sum_{d<x, d|P(z)} mu(d)^2 g(d), so that
G(z) = G(z,z). Let W(z) = prod_{p<z} (1 - nu_H(p)/p)."

Key intermediate bounds in the proof of Lemma 4.3:

(p. 18, verbatim:) "by [5, Equation (2.3.11)] we have for any
2 <= a <= b that

> (23)  sum_{a<=p<b} g(p) <= k log( log b / log a ) + alpha_2/log a
>         + (alpha_1 alpha_2 / log a)( k + alpha_2/log a )
>       = k log( log b / log a ) + O( k^3 / log a ),

which implies that

>   sum_{sqrt(x/d)<=p<min{x/d,z}, p !| d} (g(p) nu_H(p)/p) log p
>     <= alpha_2 sum_{...} g(p)
>     << alpha_2 k + alpha_2^2 + alpha_1 alpha_2^2 k + alpha_1 alpha_2^3
>     << k^4."

(p. 18, verbatim:) "This expression is identical to what appears in
[5, Page 149] in the proof of Lemma 5.4, except that the factor of L in
the error term is replaced by a factor of L + k^4. The rest of the proof
applies to our situation without change, except for replacing factors of
L in the error term with L + k^4, so that, as in [5, Equations (3.10) and
(3.13)], we get

>   G(z) = ( 1/( S(H) Gamma(k+1) ) ) (log z)^k
>     ( 1 + O( (L + k^4)/log z ) )."

(p. 18, verbatim:) "By following the proof of [5, Lemma 5.2] and using
(23) in place of [5, Equation (2.3.4)], we get that for some constant
C in R,

> (24)  C L/log a <= sum_{a<=p<b} nu_H(p)/p - kappa sum_{a<=p<b} 1/p
>         <= O( k^3 / log a )."

(p. 19, verbatim:) "Note that by (Omega_1) and [5, Equation (2.3.9)], we
have sum_{a<=p<b} g^2(p) = O(k^4/log a). Thus, by following the proof of
[5, Lemma 5.3] and using (24), we get that

>   prod_{p>=z} ( 1 - nu_H(p)/p )^{-1} ( 1 - 1/p )^k
>     = 1 + O( (L + k^4)/log z ).

This implies that

> (25)  W(z) = S(H) ( e^{-gamma k} / (log z)^k )
>         ( 1 + O( (L + k^4)/log z ) ),

which corresponds to [5, Equation (5.2.5)] and completes the proof."

Theorem 4.4 (p. 19), verbatim:

> "Theorem 4.4 (Theorem 3.1, Halberstam--Richert, [5]). Using the
> notation of this section, with S(A;P,z) defined in (22) and satisfying
> (R) and (Omega_1), we have
>   S(A;P,z) <= x/G(z) + z^2/W^3(z)."

Endgame of Theorem 4.1 (p. 19), verbatim:

> "Applying Lemma 4.3 yields
>   S(A;P,z) <= x W(z) e^{gamma k} Gamma(k+1)
>     ( 1 + O( (L+k^4)/log z ) ) + x z^2/(x W^3(z)).
> By equation (2.3.12) in [5],
>   1/W(z) << e^{O(k^3)} (log z)^k,
> which implies that
>   z^2/W^3(z) = x W(z) z^2/(x W^4(z))
>     = x W(z) O( z^2 (log z)^{4k} e^{O(k^3)} / x ),
> and thus
>   S(A;P,z) <= x W(z) ( e^{gamma k} Gamma(k+1)
>     ( 1 + O( (L+k^4)/log z ) )
>     + O( z^2 (log z)^{4k} e^{O(k^3)} / x ) ).
> Plugging in (25), we get
>   S(A;P,z) <= Gamma(k+1) S(H) ( x/(log z)^k )
>     ( 1 + O( (L+k^4)/log z )
>     + O( z^2 (log z)^{4k} e^{O(k^3)} / x ) ).
> Set z = x^{1/(2+eps)} to complete the proof, keeping in mind that
> k = o((log x)^{1/4})."

[PARAPHRASE: the (2+eps)^k in Theorem 4.1 is exactly ((log x)/(log z))^k
= (2+eps)^k from z = x^{1/(2+eps)}; the k! is Gamma(k+1) from the
k-dimensional Selberg sieve main term; the range k = o((log x)^{1/4})
is what keeps the error factors (L+k^4)/log z and
z^2 (log z)^{4k} e^{O(k^3)}/x under control (k^4/log z = o(1) requires
k = o((log z)^{1/4}); the constraint k^2 <= (1/B_k) log z of Lemma 4.3
is weaker).]

---

## 11. SECOND MOMENTS OF SINGULAR SERIES: LOCATION OF MATERIAL [FOCUS 4]

A statement titled "second moment of singular series" (i.e. an asymptotic
or bound for sums of S(H)^2, or for sums of (S(H) - 1)^2) is NOT FOUND in
this text. What the paper contains that is adjacent:

1. The Montgomery--Soundararajan sentence (p. 1, quoted verbatim in
   Section 1 above): "[10] ... computed second-order terms of this
   average" (i.e. lower-order terms of the FIRST moment of S over tuples,
   used for Gaussian distribution of primes in longer intervals), "k is
   fixed throughout."
2. Moments of the distribution of PRIMES in short intervals (not of the
   singular series): Theorem 1.4 (conditional, r << (log h)^{1-delta},
   Poisson moments; p. 3), Theorem 1.8 (unconditional,
   r = o((log x)^{1/4}); p. 4), with tails Corollaries 1.5, 1.6
   (conditional; p. 4) and 1.9 (unconditional; p. 5), all quoted verbatim
   in Sections 5 and 6 above.

Reference [10] (p. 20): "H. L. Montgomery and K. Soundararajan, Primes in
short intervals, Comm. Math. Phys. 252 (2004), no. 1-3, 589-617."
Reference [3] (p. 20): "P. X. Gallagher, On the distribution of primes in
short intervals, Mathematika 23 (1976), no. 1, 4-9."

---

## 12. REMARKS ON THE BARRIER AT LARGER k: CONSOLIDATED [FOCUS 5]

All barrier-flavored statements in the paper, with anchors:

1. (p. 2, after Thm 1.1, verbatim above, Section 2): "One might expect the
   average value of 1 to extend to still larger k; for example, it is
   reasonable to conjecture that (3) would hold whenever
   k = O((log h)^2)." -- i.e. the author expects the true threshold at
   (log h)^2, not the proven (log h)^{1/2 - }.
2. (p. 7, verbatim above, Section 7b): the proof needs
   "(1-delta)(2+2 alpha) + alpha < 1", possible exactly because
   "1/2 < delta < 1". This is the precise technical origin of the
   delta > 1/2 restriction: the Rankin-trick bound
   exp(c k^2 (log h)^alpha / log log h) on prod_{p|D_H}(1+Ck^2 p^{alpha-1})
   must be h^{o(1)}, and k^2 = (log h)^{2(1-delta)} forces
   2(1-delta) < 1. The same shape recurs at (19) via
   "(1-delta)(1+gamma) < 1" (p. 10).
3. (p. 11, verbatim above, Section 8): "The techniques relying on the
   Chinese Remainder Theorem break down for larger k, where they do not
   give a bound with the correct power of h." -- the stated reason
   Theorem 1.1's method stops and Theorem 1.2's absolute-value method
   (no cancellation, (3 log k)^k loss) takes over.
4. (p. 3, verbatim above, Section 4): on the input conjecture itself:
   "if k is as large as log x, then li_k(x) is small enough that the
   conjecture is not so meaningful, but it is difficult to say when
   Hardy--Littlewood convergencee [sic] should break down."
5. (p. 4, verbatim above, Section 5): "It seems reasonable to conjecture
   that the Poisson prediction should still hold when k ~ log h or
   k ~ (log h)^2, and perhaps even larger. At this point, both upper and
   lower bounds are far from matching this conjecture."
6. (p. 5, verbatim above, Section 6): "We predict that the bound in
   Corollary 1.5 should hold for any k << (log h)^2, instead of merely
   k << (log h)^{1-delta}." (Conjectures 1.7 and 1.10 formalize the
   (log h)^2 range.)
7. (p. 2, verbatim above, Section 2): Theorem 1.2's bound "is likely much
   weaker than the truth"; optimizing the small-prime cutoff only
   improves 3^k to (2+eps)^k, "the final bound is in any case
   e^{O(k log log k)}."

---

## 13. REFERENCES (p. 20, complete list, verbatim titles)

1. J. Friedlander and H. Iwaniec, Opera de cribro, AMS Colloquium
   Publications, vol. 57, 2010.
2. S. Funkhouser, D. A. Goldston, and A. H. Ledoan, Distribution of large
   gaps between primes, Irregularities in the distribution of prime
   numbers, Springer, Cham, 2018, pp. 45-67.
3. P. X. Gallagher, On the distribution of primes in short intervals,
   Mathematika 23 (1976), no. 1, 4-9.
4. A. Granville and A. Lumley, Primes in short intervals: Heuristics and
   calculations, arXiv:2009.05000, 2020.
5. H. Halberstam and H.-E. Richert, Sieve methods, LMS Monographs No. 4,
   Academic Press, 1974.
6. N. I. Klimov, Combination of elementary and analytic methods in the
   theory of numbers, Uspehi Mat. Nauk (N.S.) 13 (1958), no. 3 (81),
   145-164.
7. H. Maier, Primes in short intervals, Michigan Math. J. 32 (1985),
   no. 2, 221-225.
8. J. Maynard, Small gaps between primes, Ann. of Math. (2) 181 (2015),
   no. 1, 383-413.
9. J. Maynard, Dense clusters of primes in subsets, Compos. Math. 152
   (2016), no. 7, 1517-1554.
10. H. L. Montgomery and K. Soundararajan, Primes in short intervals,
    Comm. Math. Phys. 252 (2004), no. 1-3, 589-617.
11. B. C. Rennie and A. J. Dobson, On Stirling numbers of the second
    kind, J. Combinatorial Theory 7 (1969), 116-121.
12. Y. Zhang, Bounded gaps between primes, Ann. of Math. (2) 179 (2014),
    no. 3, 1121-1174.

---

## FLAGS (consolidated)

1. [TRANSCRIPTION-UNSURE] p. 3, "Hardy--Littlewood convergencee should
   break down": double-e as rendered; presumably a typo for
   "convergence".
2. [TRANSCRIPTION-UNSURE] p. 5, Corollary 1.9 discussion for lambda = 1:
   the display "x exp(-sqrt(2^C/e)(log log x)^{1/2}
   (log log log x - 1)^{-C/2})" is small type; inner "- 1" placement
   transcribed from the rendered page.
3. [TRANSCRIPTION-UNSURE] p. 6, Rankin product subscript "p !| D_H"
   (p not dividing D_H): small type, forced by the coprimality condition
   on e.
4. [TRANSCRIPTION-UNSURE] p. 8, error-term chain: intermediate exponent
   read as e^{(log h)^{1-delta/2}}.
5. [TRANSCRIPTION-UNSURE] p. 8, "for any q <= x and r with all prime
   factors <= k": the bound on q is small type; read as x.
6. [TRANSCRIPTION-UNSURE] p. 11, eq. (21): the discriminant symbol in
   "p | Delta(H)" is rendered Delta(H); same object as D_H by role.
7. [TRANSCRIPTION-UNSURE] p. 12, first display of the Lemma 2.1 proof:
   numerator (k - nu_H(p)) in the exponential, mathematically forced but
   small type.
8. [TRANSCRIPTION-UNSURE] p. 13, the "=" between the Euler product and
   exp(sum ...) in the Theorem 1.2 proof: printed "="; as an identity it
   can only be "<=".
9. [PRINTED-ODDITY] p. 15, Corollary 1.5 proof: threshold
   "k/lambda >= lambda e/(lambda-1)" is degenerate at lambda = 1 exactly,
   as printed.
10. [PARAPHRASE] markers: bracketed mechanism summaries after the
    A(q) = 0 quote (Section 7c), after the Theorem 1.2 proof (Section 8),
    and after the Theorem 4.1 endgame (Section 10) are extractor
    connective tissue, so marked.

---

## COMMENTARY (assessment, NOT extraction)

Consuming context: the project needs an UNCONDITIONAL supply of two
prime-gap-word sites with matched J-prefix and K-suffix windows and a
dominant weighted middle difference, at depths J, K ~ log_2 log x (an
"exchange configuration"). Known blockers: (i) pigeonhole is blind to
variability, (ii) prescribing gap patterns is a parity-blocked tuple-type
lower bound, (iii) Shiu-string site densities (2q)^{-exp(Cm)} are
circular at the needed depth. Assessment of what this paper's machinery
can and cannot supply:

1. Answers to the focus questions are in Sections 2 (regimes, verified
   against the p. 2 displays), 3 (T_k(h) definition), 7-8 and 10 (method
   anatomy), 11 (second moments: NOT FOUND as such), 12 (barriers).

2. Depth calibration to the exchange target. The project's depth is
   J, K ~ log_2 log x, i.e. word length ~ log log x; a gap word of that
   length sits inside a window of size roughly sum of ~log log x typical
   gaps ~ (log log x)(log x), and a tuple prescribing it has
   k ~ log log x elements. Kuperberg's two-sided (asymptotic) control of
   singular-series averages, Theorem 1.1 (p. 2), holds only for
   k = O((log h)^{1-delta}), delta > 1/2; with h of size (log x)^{O(1)}
   that is k << (log log x)^{1/2 - }, which is BELOW the needed depth
   k ~ log log x by a power. Above that, only the one-sided Theorem 1.2
   (p. 2) survives, with a multiplicative loss (3 log k)^k =
   e^{O(k log log k)} -- at k ~ log log x this loss is
   e^{O(log log x log log log x)} = (log x)^{o(1)}... wait, that is
   (log x)^{O(log log log x / log log x) * log log x}; concretely
   (3 log k)^k with k = log log x is exp(log log x * log(3 log log log x))
   = (log x)^{log(3 log log log x)}, i.e. a (log x)^{O(log_4 x)} factor:
   super-constant but sub-polynomial in log x. So at exchange depth the
   paper gives upper bounds on singular-series averages with a slowly
   divergent loss, and NO matching lower bound or asymptotic. (This
   arithmetic is extractor calibration, not paper content.)

3. What the machinery CAN supply toward the target, unconditionally:
   exclusively UPPER bounds. (a) Theorem 4.1 (p. 15) is a genuinely
   k-uniform Selberg-sieve upper bound (2+eps)^k k! S(H) x / log^k x for
   prime k-tuple counts, valid for k = o((log x)^{1/4}) -- comfortably
   covering k ~ log log x. Together with Theorem 1.2 it yields Theorem
   1.8 and Corollary 1.9 (pp. 4-5): unconditional upper bounds on the
   number of n <= x whose window (n, n + lambda log x] holds at least k
   primes. For the exchange program these are budget/rarity constraints
   on candidate site populations (e.g. they cap how many
   log log x-dense windows can exist), which is useful for ruling out
   strategies that would need dense sites in abundance, and for
   quantifying counting measures in an averaging argument. (b) The
   k-uniformity technology itself is portable: Lemma 4.2 and Lemma 4.3
   (p. 17) show exactly which Halberstam--Richert constants
   (alpha_1 = k+1, alpha_2 = O(k), kappa = k, L = k log log(3|D_H|))
   control the k-dependence, and Lemma 2.1 (p. 11) is a clean standalone
   uniform upper bound on a single S(H) with the pair-interaction
   structure sum_{p | (h_i - h_j), p > k^3} 1/p made explicit -- the
   natural tool if one needs to bound singular series of a PRESCRIBED
   gap-word tuple at depth log log x.

4. What it CANNOT supply, and how that maps onto the blockers. The paper
   contains no lower bound of any kind on counts of prime tuples or of
   dense intervals; its only cited lower-bound input is Maynard [9]
   (p. 4 and p. 5, quoted in Sections 5-6 above): >> x exp(-sqrt(log x))
   windows of size log x with >> log log x primes. That supplies MANY
   sites with the right prime COUNT at the right depth, but with no
   control whatsoever of the gap word inside the window -- blocker (ii)
   (parity-blocked prescription) is untouched, since Selberg-sieve
   machinery here is used strictly for upper bounds, and the
   cancellation identity A(q) = 0 (p. 9) that drives Theorem 1.1 is an
   averaging identity over ALL tuples, not a handle on individual words.
   The moment method (Theorems 1.4/1.8) sees only pi(n+h) - pi(n), a
   count statistic that aggregates over all gap words with the same
   number of primes; it is structurally blind to prefix/suffix matching
   and to the weighted middle difference of the exchange configuration
   -- a quantitative instance of blocker (i) (pigeonhole/moments blind
   to variability). Nothing in the paper addresses site densities of
   prescribed strings, so blocker (iii) is simply out of scope.

5. Conditional route, for contrast. Conjecture 1.3 (p. 3) is stated
   uniformly for k <= (log log x)^3 and h_i <= (log x)^2 -- ranges that
   comfortably contain exchange-depth tuples (k ~ log log x, window
   (log x)^{1+o(1)}). Under Conjecture 1.3, individual gap-word counts
   at exchange depth become computable to relative accuracy governed by
   the singular series, and Theorem 1.4's Poisson moments follow for
   r << (log h)^{1-delta}. So this paper is a precise witness of the
   conditional/unconditional gap the project already assumes: the
   uniform-HL hypothesis buys word-level control at the needed depth,
   while the unconditional toolbox (Selberg sieve + Theorem 1.2) buys
   only upper bounds with e^{O(k log log k)} slack.

6. Barrier diagnosis relevant to the project. The delta > 1/2 threshold
   in Theorem 1.1 is not an artifact of the statement but of the
   quantitative structure: k^2 pair interactions times a p^{-(1-alpha)}
   prime sum over p <= (k choose 2) log h forces
   (1-delta)(2+2alpha)+alpha < 1 (p. 7), i.e. k << (log h)^{1/2-}. Any
   project use of "Gallagher-type cancellation at depth log_2 log x in
   windows h ~ (log x)^{O(1)}" must either beat this k^2-interaction
   bottleneck or accept the one-sided Theorem 1.2 regime. The author's
   own expectation (pp. 2, 4-5, Conjectures 1.7/1.10) is that the truth
   extends to k = O((log h)^2), but explicitly flags that "both upper
   and lower bounds are far from matching this conjecture" (p. 4).

7. Net assessment: this paper supplies (unconditional) rarity caps and
   k-uniform sieve/singular-series UPPER bound technology at and beyond
   exchange depth, plus a sharp map of where two-sided control dies
   (k ~ (log h)^{1/2}); it supplies NO unconditional existence mechanism
   for even one prescribed-gap-word site, let alone two matched ones.
   Its value to item-0017 is as a quantitative boundary marker and as a
   toolbox (Lemma 2.1; Lemmas 4.2-4.3; Theorem 4.1) for the upper-bound
   side of any counting ledger in an exchange-configuration argument.
