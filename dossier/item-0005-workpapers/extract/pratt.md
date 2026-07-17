# EXTRACTION: Pratt, "The irrationality of a prime factor series under a prime tuples conjecture"

Source: /home/istr/pro/erdos251/dossier/2409.15185v1.pdf (arXiv:2409.15185v1 [math.NT] 23 Sep 2024, 11 pages)
Author: Kyle Pratt (Brigham Young University). NSF grant DMS-2418328.
Extraction method: pdftotext for location + visual Read of all 11 rendered pages for formulas.
Convention: math transcribed in LaTeX-like ASCII tokens. Verbatim quotes are in "..." blocks
or indented displays and follow the printed text exactly (including the paper's own typos,
marked [sic]). Anchors are theorem/lemma/equation/section numbers; page numbers secondary.

NOTE ON NUMBERING: the paper has NO "Theorem 1.1". Its Section 1 contains Conjecture 1.1,
Conjecture 1.2, and the main result Theorem 1.3. (The task brief's "Theorem 1.1" corresponds
to Theorem 1.3 here.)

---

## 0. DOCUMENT MAP

- Sec. 1 (pp. 1-2): Introduction; Conjectures 1.1, 1.2; Theorem 1.3; notation.
- Sec. 2 (pp. 2-5): Proof of Theorem 1.3. Parameters (2.1)-(2.2); Proposition 2.1;
  proof of Thm 1.3 from Prop 2.1 (integer-tail contradiction); Lemma 2.2;
  proof of Prop 2.1 from Lemma 2.2; equations (2.3)-(2.5); lower bound on singular series.
- Sec. 3 (pp. 5-10): Proof of Lemma 2.2. Strategy paragraph; Rankin trick lambda^{omega};
  Lemma 3.1 (smoothing); Siegel-zero accounting; Brun sieve; main/error split (3.1)-(3.2);
  Sec. 3.1 error term R via Lemma 3.2 and zero-density, eqs (3.3)-(3.7);
  Sec. 3.2 main term M via Friedlander-Iwaniec and Shiu, eq (3.8); optimization lambda = 1/10.
- p. 11: references [1]-[15].

---

## 1. VERBATIM LOAD-BEARING STATEMENTS

### 1.1 Abstract (p. 1)

"Let omega(n) denote the number of distinct prime factors of n. Assuming a suitably
uniform version of the prime k-tuples conjecture, we show that the number

    \sum_{n=1}^{\infty} \frac{\omega(n)}{2^n}

is irrational. This settles (conditionally) a question of Erdos."

### 1.2 Setup for linear forms (Sec. 1, p. 1)

"Let L = {L_1, ..., L_K} be a set of distinct linear forms L_k(n) = a_k n + b_k, where the
coefficients a_k, b_k are positive integers. For a prime p, let omega_L(p) denote the number
of roots of \prod_{k=1}^{K} L_k(n) modulo p. We say L is admissible if omega_L(p) < p for
every prime p."

### 1.3 Conjecture 1.1 (p. 1), verbatim

"Conjecture 1.1 (Prime K-tuples conjecture). Let L = {L_1, ..., L_K} be an admissible set
of linear forms. Then there are infinitely many integers n such that L_1(n), ..., L_K(n)
are all prime."

### 1.4 Conjecture 1.2 (p. 2), verbatim, ALL quantifiers and windows

"Conjecture 1.2 (Quantitative prime K-tuples conjecture). Let L = {L_1, ..., L_K} be an
admissible set of linear forms, where L_k(n) = a_k n + b_k with the a_k, b_k positive
integers. Define the singular series

    \mathfrak{S}(L) = \prod_p \left(1 - \frac{\omega_L(p)}{p}\right)
                              \left(1 - \frac{1}{p}\right)^{-K}.

If x is sufficiently large, if a_k, b_k <= (\log\log x)^{100}, and if
K <= 100 \log\log\log x, then

    \sum_{\substack{n <= x \\ L_k(n) \text{ is prime for } 1 <= k <= K}} 1
      = (1 + o(1)) \mathfrak{S}(L) \frac{x}{(\log x)^K},

where o(1) denotes a quantity which goes to zero as x goes to infinity."

So the uniformity windows are exactly: coefficients a_k, b_k <= (log log x)^100;
number of forms K <= 100 log log log x; full asymptotic with (1+o(1)) constant.

### 1.5 Remarks following Conjecture 1.2 (p. 2), verbatim

"There has been recent progress on versions of Conjecture 1.2, in which several rather than
all of the L_k(n) are prime [11]."
([11] = Maynard, Dense clusters of primes in subsets, Compos. Math. 152 (2016).)

"The statement of Conjecture 1.2 suffices for our present work, but could be refined further.
There are various statements of a uniform prime tuples conjecture in the literature (e.g.
[10, Conjecture 1.3]), but usually only in the case in which L_k(n) = n + b_k for each k, so
that the coefficients a_k are all equal to one."
([10] = Kuperberg, Sums of singular series with large sets and the tail of the distribution
of primes, Q. J. Math. 74 (2023).)

This is the paper's explicit contrast with the literature: the uniform statements available
in print are for SHIFTED forms n + b_k only, while this proof requires general dilated forms
a_k n + b_k with a_k > 1 (see Sec. 2.4 below for where the dilation a_k = Q/k arises).

"Our main result is that Conjecture 1.2 has implications for one of the irrationality
questions of Erdos."

### 1.6 Theorem 1.3 (p. 2), verbatim (the paper's main theorem; there is no Theorem 1.1)

"Theorem 1.3. Assume Conjecture 1.2. Then, for every integer t >= 2, the number

    \sum_{n >= 1} \frac{\omega(n)}{t^n}        (1.1)

is irrational."

"Of course, we recover the result mentioned in the abstract by specializing t = 2."

### 1.7 Notation facts used without comment (Sec. 1, p. 2), verbatim excerpts

"We shall occasionally use without comment the fact that omega(n) << log n. We also use the
fact that omega is additive: given coprime positive integers m and n, we have
omega(mn) = omega(m) + omega(n)."

Other notation: floor/ceiling; n = a(q) means n = a (mod q); 1_{A(n)} indicator;
implied constants may depend on the series in (1.1) and the integer t.

### 1.8 Erdos background (Sec. 1, p. 1)

Erdos [2] proved \sum_{n>=1} tau(n)/t^n irrational for integer t >= 2, and noted that the
analogous results for \sum phi(n)/t^n, \sum sigma(n)/t^n, \sum omega(n)/t^n seem
"to present difficulties" (paper's footnote 1 points to erdosproblems.com/69, /249, /250).
The sigma(n) series is now known transcendental via Nesterenko [14]; phi and omega cases
open before this work.

---

## 2. PROOF ARCHITECTURE, SECTION 2 (reduction of Theorem 1.3)

### 2.1 Parameters, eq (2.1) and (2.2) (Sec. 2, p. 3), verbatim

"For large positive x, define positive integers K, L, Q by

    K = \lfloor 5 \log\log\log x \rfloor,   L = \lfloor 2 \log\log x \rfloor,
    Q = \prod_{p <= K} p^{2\lceil \log K / \log p \rceil}.     (2.1)

We note that k^2 | Q for every positive integer k <= K, and that

    (\log\log x)^{10 - o(1)} <= Q <= (\log\log x)^{20 + o(1)}   (2.2)

by the prime number theorem."

NOTE (extractor, structural): K is triple-log; this is exactly what keeps K inside the
window K <= 100 log log log x of Conjecture 1.2, and Q <= (log log x)^{20+o(1)} keeps the
dilation coefficients a_k = Q/k inside the window a_k <= (log log x)^{100}.

### 2.2 Proposition 2.1 (p. 3), verbatim

"Proposition 2.1. Assume Conjecture 1.2. Let x be large, and define K, L, Q as in (2.1).
Then there exists a positive integer n_0 <= x such that the following hold:
(1) n_0 Q/k + 1 is prime for every 1 <= k <= K,
(2) omega(n_0 Q + k) <= (\log\log x)^2 for K < k <= L,
(3) omega(n_0 Q + K + 1) > \frac{1}{10} \log\log x."

### 2.3 Proof of Theorem 1.3 assuming Proposition 2.1 (pp. 3-4)

Reduction mechanism: NOT binary-digit analysis; it is the classical integer-tail
(denominator-clearing) contradiction. Let

    alpha = alpha_t = \sum_{n >= 1} omega(n)/t^n

be the series (1.1). Assume for contradiction alpha = a/b in Q with a, b positive integers.
Then for any positive integer N,

    T(N) := b \sum_{k >= 1} \frac{omega(N+k)}{t^k}
          = b t^N \left( alpha - \sum_{n <= N} \frac{omega(n)}{t^n} \right)

"is an integer." (p. 3)

Set N = n_0 Q with n_0 from Proposition 2.1. Split T(n_0 Q) = S_1 + S_2 + S_3 (p. 3):

    S_1 = b \sum_{k <= K} omega(n_0 Q + k)/t^k,
    S_2 = b \sum_{K < k <= L} omega(n_0 Q + k)/t^k,
    S_3 = b \sum_{k > L} omega(n_0 Q + k)/t^k = O(\log x / t^L).

Head S_1 becomes EXACTLY computable (p. 3): "Since n_0 Q + k = k(n_0 Q/k + 1) and
gcd(k, n_0 Q/k + 1) = 1, we see by part (1) of Proposition 2.1 that

    S_1 = b \sum_{k <= K} omega(k)/t^k + b \sum_{k <= K} omega(n_0 Q/k + 1)/t^k
        = a - b \sum_{k > K} omega(k)/t^k + b \sum_{k <= K} 1/t^k
        = a + \frac{b}{t-1} + O(\log K / t^K)."

(The primality in part (1) forces omega(n_0 Q/k + 1) = 1 exactly; additivity of omega plus
the engineered factorization n_0 Q + k = k * (n_0 Q/k + 1) makes the first K numerators of
the tail exactly omega(k) + 1.)

Middle S_2 is small but bounded away from 0 (p. 3): "Parts (2) and (3) of Proposition 2.1
imply

    \frac{b \log\log x}{10 t^{K+1}} <= S_2 <= \frac{b L (\log\log x)^2}{t^K}."

Endgame contradiction (p. 4), verbatim:

"Hence T(n_0 Q) = a + b/(t-1) + S_2 + E is an integer, where E is some real number with
|E| << \log K / t^K. If b is not divisible by t - 1, then we obtain a contradiction since
S_2 = o(1), E = o(1) and b/(t-1) is not an integer. If b is divisible by t - 1 then we also
obtain a contradiction, for then S_2 + E is nonzero by the lower bound on S_2, but
S_2 + E = o(1)."

(Structural reading: the integer T(n_0 Q) is squeezed into (integer, integer + 1): the
fractional part S_2 + E lies strictly in (0,1) for large x. Note t^K = t^{5 log log log x}
= (log log x)^{5 \log t}; for t = 2 the upper bound S_2 <= bL(log log x)^2/t^K ~
(log log x)^{3 - 5\log 2} -> 0 needs 5 log 2 = 3.466... > 3, a genuinely tight margin.)

### 2.4 Lemma 2.2 (p. 4), verbatim -- the counting result; dilated linear forms appear here

"Lemma 2.2. Let x be large, and let K, Q be defined as in (2.1). For 1 <= k <= K, define
the linear form L_k(n) = n Q/k + 1. Let

    \mathfrak{S} := \prod_{p <= K} \left(1 - \frac{1}{p}\right)^{-K}
                    \prod_{p > K} \left(1 - \frac{K}{p}\right)
                                  \left(1 - \frac{1}{p}\right)^{-K}.

Then

    \sum_{\substack{n <= x \\ L_k(n) \text{ is prime for } 1 <= k <= K \\
                    omega(nQ + K + 1) <= \frac{1}{10}\log\log x}} 1
      <= \mathfrak{S} \frac{x}{(\log x)^K} (\log x)^{-c_0 + o(1)},

where c_0 = \frac{9 - \log 10}{10} = 0.6697...."

WHERE THE DILATED FORMS COME FROM: the forms are L_k(n) = (Q/k) n + 1, i.e. dilation
coefficients a_k = Q/k for k = 1, ..., K (Q as in (2.1), a product of prime powers over
p <= K; NOT single primes), and b_k = 1. The dilation is forced by the head-factorization
trick of Sec. 2.3: to write n_0 Q + k = k (n_0 Q/k + 1) one needs k | Q for all k <= K
(guaranteed by k^2 | Q), and then the primality condition on the cofactor n_0 Q/k + 1 is a
primality condition on the dilated form (Q/k) n + 1 at n = n_0. This is exactly why the
paper needs Conjecture 1.2 for general a_k n + b_k rather than the shifted-only (a_k = 1)
uniform statements in the literature (remark quoted in Sec. 1.5 above).

### 2.5 Proof of Proposition 2.1 assuming Lemma 2.2 (p. 4)

Verbatim: "The set of linear forms L = {L_k(n)}_{k=1}^K is admissible. Since
omega_L(p) = 0 for p <= K, and omega_L(p) = K for p > K, we find
\mathfrak{S}(L) = \mathfrak{S}."
(For p <= K: p | Q/k so L_k(n) = 1 mod p, no roots. For p > K: one root per form, all
distinct.)

It suffices to show that

    \mathcal{S} := \sum_{\substack{n <= x \\ L_k(n) \text{ prime for } 1<=k<=K \\
        omega(nQ+k) <= (\log\log x)^2 \text{ for } K<k<=L \\
        omega(nQ+K+1) > \frac{1}{10}\log\log x}} 1

is positive. By inclusion-exclusion (p. 4):

    \mathcal{S} >= [\sum_{n<=x, all L_k(n) prime} 1]
                 - [\sum_{n<=x, all L_k(n) prime, omega(nQ+K+1) <= (1/10)\log\log x} 1]
                 - \mathcal{E},

where

    \mathcal{E} = \sum_{\substack{n <= x \\ \exists k \in (K, L],\ omega(nQ+k) > (\log\log x)^2}} 1.

"By (2.1), (2.2), Conjecture 1.2, and Lemma 2.2, it therefore suffices to show that

    \mathcal{E} = o\left( \mathfrak{S} \frac{x}{(\log x)^K} \right).    (2.3)"

(Conjecture 1.2 gives the first count = (1+o(1)) S x/(log x)^K -- this is the ONLY place the
conjecture is invoked; Lemma 2.2 says the second count is smaller by (log x)^{-c_0+o(1)}.)

"Since tau(n) >= 2^{omega(n)},

    \mathcal{E} << L \sum_{m << xQ} tau(m) 2^{-(\log\log x)^2}
               << x L Q (\log x) 2^{-(\log\log x)^2}.    (2.4)

By crude estimation, we see that (2.4) implies (2.3) as long as, say,

    \mathfrak{S} >= (\log x)^{-1}.    (2.5)"

Lower bound on the singular series (p. 5): portion p <= K of the product is >= 1; split the
rest at 2K:

    \prod_{K < p <= 2K} (1 - K/p)(1 - 1/p)^{-K}
      >= \prod_{K < p <= 2K} (1 - K/(K+1))(1 - 1/(K+1))^{-K} >= K^{-K},

and for p > 2K:

    \prod_{p > 2K} (1 - K/p)(1 - 1/p)^{-K}
      >= \exp\left(- \sum_{p > 2K} \sum_{l >= 2} \frac{1}{l}\left(\frac{K}{p}\right)^l\right)
      >= \exp\left(- K^2 \sum_{p > 2K} \frac{1}{p^2}\right) >= e^{-K}.

"Therefore \mathfrak{S} >= K^{-2K}, and (2.5) follows, with plenty of room to spare, by
(2.1)." (p. 5)
(Note: K^{2K} = exp(10 (\log\log\log x)(\log(5\log\log\log x))(1+o(1))) = (\log x)^{o(1)},
so S is only sub-polynomially small in log x BECAUSE K is triple-log.)

"The remainder of the paper is devoted to proving Lemma 2.2." (p. 5)

---

## 3. PROOF ARCHITECTURE, SECTION 3 (proof of Lemma 2.2)

### 3.1 Strategy paragraphs (Sec. 3 opening, p. 5), verbatim

"Before beginning the proof of Lemma 2.2, we briefly describe the main ideas. First, by
using sieves, we may win a factor of \mathfrak{S}(\log x)^{-K+o(1)} from the fact that
L_k(n) is prime for 1 <= k <= K. Second, since integers n \asymp x typically have
omega(n) = (1 + o(1)) \log\log x, the condition that
omega(nQ + K + 1) <= \frac{1}{10} \log\log x is atypical. Indeed, we expect to save a
factor of (\log x)^{-c}, for some constant c > 0. If these two sources of savings are
'independent,' then we obtain the desired result."

"Of course, we encounter some technical difficults [sic] in executing this strategy. Our
method for controlling the condition omega(nQ + K + 1) <= \frac{1}{10} \log\log x, when
combined with a sieve, requires us to consider integrals involving Dirichlet L-functions to
fractional exponents. To maintain holomorphy, we only shift contours of integration in a
region devoid of zeros of these L-functions. Thus, obtaining good bounds on these integrals
requires the use of zero-free regions and zero-density estimates. Since K tends to infinity,
it is necessary to account for possible Siegel zeros in order to obtain sufficiently strong
error terms."

### 3.2 Rankin/moment step and change of variables (p. 5)

Dyadic reduction: suffices to show

    \mathcal{Z} := \sum_{\substack{x/2 < n <= x \\ L_k(n) \text{ prime for } 1<=k<=K \\
                       omega(nQ+K+1) <= \frac{1}{10}\log\log x}} 1
                <= \mathfrak{S} \frac{x}{(\log x)^K} (\log x)^{-c_0 + o(1)}.

Probabilistic/moment structure = Rankin's trick with a fractional moment of omega
(p. 5): "For lambda in (0,1), where lambda is a constant we choose later, we find

    1_{omega(nQ+K+1) <= \frac{1}{10}\log\log x}
       <= lambda^{omega(nQ+K+1) - \frac{1}{10}\log\log x}."

Change variables, writing n for nQ + K + 1:

    \mathcal{Z} <= (\log x)^{\frac{1}{10}\log(1/\lambda)}
       \sum_{\substack{xQ/2 < n <= 2xQ \\ n \equiv K+1 (Q) \\
             \frac{n-K-1}{k} + 1 \text{ is prime for } 1<=k<=K}} lambda^{omega(n)}.

Then (p. 6): let g = gcd(K+1, Q), observe g | n; define Q' = Q/g, K' = (K+1)/g; change
n -> gn:

    \mathcal{Z} <= (\log x)^{\frac{1}{10}\log(1/\lambda)}
       \sum_{\substack{xQ'/2 < n <= 2xQ' \\ n \equiv K'(Q') \\
             \frac{ng-K-1}{k} + 1 \text{ is prime for } 1<=k<=K}} lambda^{omega(gn)}.

"We note that gcd(K', Q') = 1. Since omega(gn) >= omega(n), we can replace
lambda^{omega(gn)} by lambda^{omega(n)} for an upper bound." (p. 6)

### 3.3 Lemma 3.1 (smoothing, p. 6), verbatim statement

"Lemma 3.1. There is a nonnegative smooth function W(x) which is compactly supported in
[1/4, 4], and which is equal to one in [1/2, 2]. Furthermore, the derivatives of W satisfy
|W^{(j)}(x)| << j^{3j}, where the implied constant is absolute. If we write W^{\dagger}(s)
for the Mellin transform of W, then W^{\dagger}(s) is entire, and there exists an absolute
constant c > 0 such that

    |W^{\dagger}(s)| << 4^{|\Re(s)|} \exp(-c|s|^{1/3})."

Proof ingredients (p. 6): construction from [9, appendix A] (Iwaniec), W(x) = G(x - 1/2)
with T = 1/2, U = 3/2, V = 1/4; |W^{(j)}(x)| << 4^j j! (2j/e)^j << j^{3j};
W^{\dagger}(s) = \int_0^\infty W(x) x^{s-1} dx entire; k-fold integration by parts gives
W^{\dagger}(s) = \frac{(-1)^k}{s(s+1)...(s+k-1)} \int_0^\infty W^{(k)}(x) x^{s+k-1} dx,
hence |W^{\dagger}(s)| << 4^{|\Re(s)|} 4^k k^{3k} \prod_{j=0}^{k-1} |s+j|^{-1}; choose
k = \lfloor \delta |s|^{1/3} \rfloor, delta > 0 small.

With W inserted: \mathcal{Z} <= (\log x)^{\frac{1}{10}\log(1/\lambda)}
\sum_{n \equiv K'(Q'), (ng-K-1)/k + 1 prime for 1<=k<=K} lambda^{omega(n)} W(n/(xQ')).

### 3.4 Siegel-zero accounting (pp. 6-7), verbatim

"We now account for potential Siegel zeros, following the strategy of [11]. For a suitable
positive constant c, there is at most one real primitive Dirichlet character chi_* to a
modulus q_* <= \exp((\log x)^{1/3}) for which L(s, chi_*) has a real zero beta which is
greater than 1 - \frac{c}{(\log x)^{1/3}} [1, p. 95]. If q_* exists, we let B be the
largest prime factor of q_*. By the class number formula, we have q_* >= (\log x)^{1/2},
say (see [1, p. 96, equation (12)]). As q_* is squarefree apart from a bounded power of
two, it follows that \log\log x << B <= \exp((\log x)^{1/3}). If no such q_* exists, we set
B = 1."

### 3.5 Brun sieve and main/error decomposition (p. 7)

Definitions (p. 7): "We define
L(n) := \prod_{k=1}^{K} (\frac{ng-K-1}{k} + 1),   X := x^{1/(\log\log x)^3},
P := \prod_{K^2 < p <= X} p,  and  V := 2\lfloor(\log\log x)^2\rfloor."

Since B <= X, Brun sieve ([7, p. 56, equation (6.6)], Friedlander-Iwaniec):

    \mathcal{Z} <= (\log x)^{\frac{1}{10}\log(1/\lambda)}
        \sum_{\substack{n \equiv K'(Q') \\ \gcd(L(n), P/B) = 1}} lambda^{omega(n)} W(n/(xQ'))
      <= (\log x)^{\frac{1}{10}\log(1/\lambda)}
        \sum_{n \equiv K'(Q')} lambda^{omega(n)} W(n/(xQ'))
        \sum_{\substack{d | L(n),\ d | P \\ (d,B)=1,\ omega(d) <= V}} \mu(d).

(The primality of all K forms is DROPPED to an upper-bound sieve of dimension K; the factor
(d,B)=1 removes the possible exceptional modulus from the sieve.)

Swap summation; key CRT observation (p. 7), verbatim: "Since d is squarefree and has no
prime divisors <= K^2, we see by the Chinese remainder theorem that d | L(n) if and only if
n lies in a particular set of reduced residue classes S(d) modulo d of size K^{omega(d)}."

Then Z <= (\log x)^{\frac{1}{10}\log(1/\lambda)} (\mathcal{M} + \mathcal{R}), where

    \mathcal{M} := \sum_{\substack{d|P \\ (d,B)=1 \\ omega(d)<=V}} \mu(d)
        \frac{K^{omega(d)}}{\varphi(Q'd)}
        \sum_{(n, Q'd)=1} lambda^{omega(n)} W\!\left(\frac{n}{xQ'}\right)      (3.1)

    \mathcal{R} := \sum_{\substack{d|P \\ (d,B)=1 \\ omega(d)<=V}} \mu(d)
        \sum_{v \in S(d)} \Big\{ \sum_{\substack{n \equiv K'(Q') \\ n \equiv v(d)}}
            lambda^{omega(n)} W\!\left(\frac{n}{xQ'}\right)
          - \frac{1}{\varphi(Q'd)} \sum_{(n, Q'd)=1}
            lambda^{omega(n)} W\!\left(\frac{n}{xQ'}\right) \Big\}.           (3.2)

"We note that Q' and d are coprime, so by the Chinese remainder theorem we may combine the
congruence conditions n = K'(Q') and n = v(d) into a single congruence condition modulo
Q'd." (p. 7)

### 3.6 Sec. 3.1: bounding the error term R (pp. 7-9)

Triangle inequality, worst residue class (p. 7):
|\mathcal{R}| <= \sum_{m <= Q'X^V, (m,B)=1} K^{omega(m)} E(m), where (p. 8)

    E(m) := \max_{(\gamma, m)=1} \Big| \sum_{n \equiv \gamma(m)} lambda^{omega(n)}
        W(n/(xQ')) - \frac{1}{\varphi(m)} \sum_{(n,m)=1} lambda^{omega(n)} W(n/(xQ')) \Big|.

"By Cauchy-Schwarz and the trivial bound E(m) << xQ'/m, we deduce

    |\mathcal{R}|^2 << x (\log x)^{3K^2} \mathcal{R}_1,    (3.3)

where \mathcal{R}_1 = \sum_{m <= Q'X^V, (m,B)=1} E(m)."
[TRANSCRIPTION-UNSURE: exponent read as 3K^2 from the rendered page; the pdftotext layer
prints "3K" with the superscript 2 possibly detached.]

Multiplicative characters detect the congruence; chi != chi_0; replace each chi mod m by the
primitive psi mod r inducing it; split r dyadically (p. 8):

    \mathcal{R}_1 << (\log x) \sup_{1 << R << Q'X^V} \sum_{\ell <= Q'X^V}
        \frac{1}{\varphi(\ell)} \sum_{\substack{r \asymp R \\ (r,B)=1}} \frac{1}{\varphi(r)}
        \sum^{*}_{\psi(r)} \Big| \sum_{(n,\ell)=1} lambda^{omega(n)} \psi(n)
            W\!\left(\frac{n}{xQ'}\right) \Big|,

starred sum = over primitive characters.

### 3.7 Lemma 3.2 (p. 8), verbatim -- the L^lambda character-sum bound

"Lemma 3.2. Let x be large, and let C \subseteq \mathbb{C} denote the region

    C = {u + iv : u >= 1/2, |v| <= (\log x)^{20}}.

For a primitive Dirichlet character psi (mod r) with r <= x^{1/3}, let sigma(psi) denote
the largest real part of a zero of L(s, psi) contained in C. If lambda in (0, 1/2],
x^{1/2} <= N <= x^2, and ell <= x^{O(1)}, then

    \Big| \sum_{(n,\ell)=1} lambda^{omega(n)} \psi(n) W\!\left(\frac{n}{N}\right) \Big|
      << r^{1/2} N^{\max(\frac{9}{10}, \sigma(\psi))}
         \prod_{p | \ell} \left(1 + \frac{3}{p^{9/10}}\right)."

Application, two cases by size of R (pp. 8-9):

Case R <= (1/10)\exp((\log x)^{1/3}): "since (r, B) = 1 the classical zero-free region (see
[1, Chapter 14]) implies sigma(psi) <= 1 - \frac{c}{(\log x)^{1/3}} for every psi, for some
constant c > 0." Then

    \mathcal{R}_1 << (\log x)^2 R^{3/2} (xQ')^{1 - c(\log x)^{-1/3}}
                 << x \exp(-\sqrt{\log x}).    (3.4)

(This is where excluding the exceptional modulus B pays: all remaining psi obey the
classical zero-free region even though K -> infinity.)

Case R >> \exp((\log x)^{1/3}): break over psi by value of sigma(psi). Contribution of psi
with sigma(psi) <= 9/10 is <= x^{9/10 + o(1)}. For sigma(psi) > 9/10 (p. 9):

    << \frac{(\log x)^{O(1)}}{R^{1/2}}
       \sum_{\substack{9/10 <= \beta <= 1 \\ \beta = \frac{9}{10} + \frac{j}{\log x},\ j >= 0}}
       x^{\beta} \sum_{r \asymp R} \sum^{*}_{\substack{\psi(r) \\
       \beta <= \sigma(\psi) < \beta + \frac{1}{\log x}}} 1.    (3.5)

"Let N(sigma, T, psi) denote the number of zeros rho of L(s, psi) satisfying
\Re(rho) >= beta and |\Im(rho)| <= T." [Paper's own wording; note it writes beta where the
argument is sigma.] If beta <= sigma(psi) then N(beta, (\log x)^{20}, psi) >= 1, so (3.5) is

    << \frac{(\log x)^{O(1)}}{R^{1/2}} \sup_{9/10 <= \beta <= 1} x^{\beta}
       \sum_{r \asymp R} \sum^{*}_{\psi(r)} N(\beta, (\log x)^{20}, \psi).

Zero-density input (p. 9): "By work of Montgomery [12, Theorem 12.2] we have

    \sum_{r \asymp R} \sum^{*}_{\psi(r)} N(\beta, (\log x)^{20}, \psi)
        << R^{5(1-\beta)} (\log x)^{O(1)}

since beta >= 9/10, and therefore

    \mathcal{R}_1 << x^{9/10+o(1)} + (\log x)^{O(1)} \frac{x}{R^{1/2}}
        \sup_{9/10 <= \beta <= 1} \left(\frac{x}{R^5}\right)^{\beta - 1}
        << \frac{x}{R^{1/3}}.    (3.6)"

"Taking (3.4) and (3.6) together shows |\mathcal{R}_1| << x \exp(-c(\log x)^{1/3}), for
some positive constant c. Inserting this bound in (3.3) then gives

    |\mathcal{R}| << x \exp(-(\log x)^{1/4}).    (3.7)"

### 3.8 Proof of Lemma 3.2 (p. 9): Mellin + fractional powers of L-functions

By Mellin inversion:

    \sum_{(n,\ell)=1} lambda^{omega(n)} \psi(n) W\!\left(\frac{n}{N}\right)
      = \frac{1}{2\pi i} \int_{c - i\infty}^{c + i\infty} N^s W^{\dagger}(s)
        \prod_{p | \ell} \left(1 + \frac{\lambda \psi(p)}{p^s - \psi(p)}\right)^{-1}
        A(s) L(s, \psi)^{\lambda} ds,

"where c > 1, and A(s) is an Euler product (depending on lambda and psi) that converges
absolutely for \Re(s) >= 9/10, and which is uniformly bounded in this region."
(This identity is the multiplicative-structure heart: \sum lambda^{omega(n)} psi(n) n^{-s}
= A(s) L(s,psi)^{lambda} x (coprimality factors); lambda^{omega} is multiplicative.)

Steps: truncate to |s| <= (\log x)^{10} by Lemma 3.1 (negligible cost); by definition of
sigma(psi), L(s,psi)^{lambda} is holomorphic for \Re(s) > sigma(psi) and
|\Im(s)| <= (\log x)^{20}; move integration line from c to
beta = \max(\frac{9}{10}, \sigma(\psi)) + \frac{1}{\log x}; triangle inequality on new
vertical and connecting horizontal segments. "Since 0 < lambda <= 1/2, the easy bound
[13, Lemma 10.15] implies

    |L(\sigma + it, \psi)^{\lambda}| << 1 + |L(\sigma + it, \psi)|^{1/2}
      << r^{\frac{1-\sigma}{2} + \varepsilon}(1 + |t|) << r^{1/2}(1 + |t|),

say. Also, for \Re(s) >= 9/10,

    \Big| \prod_{p|\ell} \Big(1 + \frac{\lambda\psi(p)}{p^s - \psi(p)}\Big)^{-1} \Big|
      <= \prod_{p|\ell} \Big(1 + \frac{\lambda}{p^{9/10} - 1 - \lambda}\Big)
      <= \prod_{p|\ell} \Big(1 + \frac{3}{p^{9/10}}\Big),

since lambda <= 1/2." (p. 9)

### 3.9 Sec. 3.2: evaluating the main term M (p. 10)

Rearrange (3.1):

    \mathcal{M} = \frac{1}{\varphi(Q')} \sum_{(n,Q')=1} lambda^{omega(n)}
        W\!\left(\frac{n}{xQ'}\right)
        \sum_{\substack{d|P \\ (d,Bn)=1 \\ omega(d)<=V}} \mu(d)
        \frac{K^{omega(d)}}{\varphi(d)}.

By [7, p. 56, equation (6.8)]: complete the truncated sum,

    \sum_{\substack{d|P \\ (d,Bn)=1 \\ omega(d)<=V}} \mu(d)\frac{K^{omega(d)}}{\varphi(d)}
      = \sum_{\substack{d|P \\ (d,Bn)=1}} \mu(d)\frac{K^{omega(d)}}{\varphi(d)}
        + O\Big( \sum_{\substack{d|P \\ omega(d)=V+1}} \frac{K^{omega(d)}}{\varphi(d)} \Big),

error bounded by

    \sum_{\substack{d|P \\ omega(d)=V+1}} \frac{K^{omega(d)}}{\varphi(d)}
      <= \frac{1}{(V+1)!} \Big( \sum_{K^2 < p <= X} \frac{K}{p-1} \Big)^{V+1}
      << \exp(-(\log\log x)^2).

Complete sum as Euler product:

    \sum_{\substack{d|P \\ (d,Bn)=1}} \mu(d)\frac{K^{omega(d)}}{\varphi(d)}
      = \prod_{\substack{K^2 < p <= X \\ p \nmid Bn}} \Big(1 - \frac{K}{p-1}\Big)
      = (1 + o(1)) \mathfrak{S} \prod_{p <= X} \Big(1 - \frac{1}{p}\Big)^{K}
        \times \prod_{\substack{p | Bn \\ K^2 < p <= X}} \Big(1 - \frac{K}{p-1}\Big)^{-1}
        \prod_{K < p <= K^2} \Big(1 - \frac{K}{p}\Big)^{-1}.

"By Mertens' theorem and some estimations, this is

    <= \mathfrak{S} \frac{(\log\log x)^{O(K)}}{(\log x)^K} e^{O(K)}
       \prod_{p | Bn} (1 + p^{-1/3})."

It follows that

    \mathcal{M} <= \mathfrak{S} \frac{(\log x)^{o(1)}}{(\log x)^K} \frac{1}{\varphi(Q')}
        \sum_{n \asymp xQ'} lambda^{omega(n)} \prod_{p|n} (1 + p^{-1/3}).

Shiu's Brun-Titchmarsh theorem for multiplicative functions ([15, Theorem 1]):

    \sum_{n \asymp xQ'} lambda^{omega(n)} \prod_{p|n}(1 + p^{-1/3})
      << \frac{xQ'}{\log x} \exp\Big( \sum_{p << xQ'} \frac{\lambda}{p}(1 + p^{-1/3}) \Big)
      << \frac{xQ'}{(\log x)^{1-\lambda}},

"and it follows that

    \mathcal{M} <= \mathfrak{S} \frac{x}{(\log x)^K} (\log x)^{-1+\lambda+o(1)}.    (3.8)"

(The (log x)^{-1+lambda} saving is the quantitative form of "omega(n) small is atypical":
the lambda-tilted count of ALL n of size xQ' is x/(log x)^{1-lambda}.)

### 3.10 Endgame of Lemma 2.2 (p. 10), verbatim

"Recalling from (2.5) that \mathfrak{S} >= (\log x)^{-1}, comparing (3.8) and (3.7) yields

    \mathcal{Z} <= \mathfrak{S} \frac{x}{(\log x)^K}
        (\log x)^{-1 + \lambda + \frac{1}{10}\log(1/\lambda) + o(1)}.

We choose the optimal lambda = 1/10 (which is suitable for Lemma 3.2) to conclude."

(-1 + 1/10 + (1/10)\log 10 = -(9 - \log 10)/10 = -c_0, matching Lemma 2.2. (2.5) is needed
so that the additive error (3.7), of size x\exp(-(\log x)^{1/4}), is dominated by
\mathfrak{S} x (\log x)^{-K-c_0}: since \mathfrak{S} >= (\log x)^{-1} and
(\log x)^{K+2} = \exp(O(\log\log\log x \cdot \log\log x)) << \exp((\log x)^{1/4}).)

---

## 4. REFERENCES CITED AT LOAD-BEARING POINTS (paper's numbering, p. 11)

- [1] Davenport, Multiplicative number theory (zero-free region, exceptional zero, class
  number formula: pp. 95-96, Ch. 14).
- [2]-[5] Erdos (and Erdos-Graham): origin of the problem.
- [7] Friedlander-Iwaniec, Opera de cribro (Brun sieve, eqs (6.6), (6.8) on p. 56).
- [9] Iwaniec, Lectures on the Riemann zeta function (smooth function construction,
  appendix A, Corollary A.2).
- [10] Kuperberg (uniform tuples statements, shifted forms only -- the contrast remark).
- [11] Maynard, Dense clusters of primes in subsets (several-of-K progress; Siegel-zero
  strategy followed in Sec. 3).
- [12] Montgomery, Topics in multiplicative number theory (Theorem 12.2, zero-density).
- [13] Montgomery-Vaughan (Lemma 10.15, convexity-type bound on L).
- [14] Nesterenko (sigma(n) series transcendental).
- [15] Shiu (Brun-Titchmarsh for multiplicative functions, Theorem 1).

---

## 5. TRANSFER-RELEVANT OBSERVATIONS (extractor commentary)

Everything in this section is commentary by the extractor, NOT content of the PDF.
Statements about the project's delta_n machinery and about Tao-Teravainen come from the
task context, not from this paper; the paper (Sep 2024) does not cite Tao-Teravainen.
[BACKGROUND-UNVERIFIED] applies to any literature claim below not anchored in the PDF.

### 5.1 Shape of the reduction (shared skeleton with the project's delta_n machinery)

Pratt's T(N) (Sec. 2.3 above, p. 3) is exactly the project's tail object: for t = 2 and
numerator sequence a_n, T(N) = b \sum_{k>=1} a_{N+k} 2^{-k} = b * (delta_N-analog). The
irrationality template is: rationality alpha = a/b => T(N) is an integer for EVERY N; then
engineer ONE N where T(N) visibly lies strictly between consecutive integers. No binary
digits, no periodicity argument, no measure theory: a single well-chosen N suffices.
The split S_1 + S_2 + S_3 (head / middle / far tail) is the natural decomposition of
delta_N, and the contradiction is "fractional part of T(N) is in (0,1)": head exactly known
(= a + b/(t-1) + tiny), middle o(1) but > 0, far tail negligible.

### 5.2 Where smallness/structure of omega(n) is load-bearing (and has no gap analog)

1. EXACT HEAD (Prop 2.1(1) + additivity, p. 3): omega(n_0 Q + k) = omega(k) +
   omega(n_0 Q/k + 1) = omega(k) + 1 because n_0 Q + k factors as k(n_0 Q/k + 1) and the
   cofactor is PRIME. Two properties of omega are used at once: complete additivity on
   coprime factorizations, and the fact that "prime" pins omega to its minimum value 1.
   The numerator of the series at the first K tail indices is thereby made deterministic.
   For the project series S = \sum p_n/2^n, equivalently \sum g_n/2^n, the numerator
   g_n = p_{n+1} - p_n is not a function of n's arithmetic (residue/factorization) data;
   no conjecture in the tuples family prescribes g at a GIVEN INDEX n. Prescribing the head
   of delta_n exactly would require knowing K consecutive prime gaps at a location specified
   by the prime-counting function itself. There is no analog of "prime => omega = 1".
2. SIZE HIERARCHY (Prop 2.1(2),(3) and S_2 bounds, p. 3): omega has typical size
   log log x, worst-case << log x. The middle sum S_2 is o(1) because
   L (log log x)^2 / t^K -> 0 with t^K = (log log x)^{5 log t} -- this needs the numerator
   at scale (log log x)^{O(1)}, i.e. DOUBLE-log scale, against a head length K at TRIPLE-log
   scale, which is the maximum allowed by Conjecture 1.2 (K <= 100 log log log x) and by the
   singular series lower bound S >= K^{-2K} >= (log x)^{-o(1)} (p. 5). For gaps,
   g_{n+k} has typical size ~ log p_n ~ log n (single-log scale). Then S_2-analog
   ~ (log n)/2^K requires K ~ log log n forms; at that K the singular series K^{-2K} is
   (log n)^{-Theta(log log log n)}, no longer >= (log x)^{-1} (breaks (2.5)), and K
   violates the uniformity window of Conjecture 1.2. The same wall appears in the crude
   bound (2.4) via tau(n) >= 2^{omega(n)}, which has no gap analog at all.
   So: BOTH the conjectural input window AND the sieve bookkeeping are calibrated to a
   numerator of at most polylog-log size. A growing single-log numerator overruns the
   entire architecture, not just one lemma.
3. MULTIPLICATIVITY IN THE ANALYTIC CORE (Sec. 3, Lemma 3.2 proof, p. 9): the Rankin
   tilt lambda^{omega(n)} is a multiplicative function, so
   \sum lambda^{omega(n)} psi(n) n^{-s} = A(s) L(s, psi)^{lambda}; the entire zero-free
   region / zero-density / Siegel-zero apparatus attaches to L(s,psi)^lambda. The atypical
   smallness of omega at ONE designated point (nQ + K + 1) is converted into a
   (log x)^{-c_0} saving this way. Prime gaps admit no Dirichlet-series Euler product;
   there is no known L-function whose fractional power encodes "g_n is atypically
   small/large". Any transfer would have to replace this by sieve-theoretic or
   Hardy-Littlewood-major-arc surrogates.

### 5.3 The dilated linear forms: what they are and why they matter for transfer

The forms are L_k(n) = (Q/k) n + 1, k = 1..K (Lemma 2.2, p. 4) -- dilations a_k = Q/k where
Q = \prod_{p <= K} p^{2\lceil\log K/\log p\rceil} (eq (2.1)); NOT a_k = p for single primes,
though every a_k is a product of prime powers over p <= K. The dilation is forced solely by
the head-factorization trick n_0 Q + k = k(n_0 Q/k + 1). The paper explicitly notes (p. 2,
quoted in Sec. 1.5) that the literature's uniform tuples statements cover only a_k = 1 and
that general a_k are needed here. Transfer note: any delta_n-style argument that wants
"N + k has a prescribed factorization shape for k <= K" will meet the same requirement --
uniformity in dilated coefficients of size ~ Q ~ (log log x)^{10..20}, which is precisely
why Conjecture 1.2's window (log log x)^{100} is chosen two orders beyond (2.2).

### 5.4 What survives for a growing-numerator series (extractor assessment)

- Survives: the T(N)/delta_N integer-tail template; the head/middle/tail split; the idea of
  engineering N by CRT divisibility (N = n_0 Q, k^2 | Q) so that consecutive N + k factor;
  the Siegel-zero-robust sieve bookkeeping (Sec. 3 is unconditional; only the LOWER-bound
  count uses Conjecture 1.2).
- Breaks: (i) exact head values (no gap analog of omega = 1 on primes); (ii) o(1) middle sum
  (numerator single-log vs t^K polyloglog -- the endgame "small but nonzero fractional
  part" becomes unreachable; a growing-numerator series needs an equidistribution /
  anti-concentration mod 1 endgame instead of a smallness endgame); (iii) the
  lambda^{omega} <-> L(s,psi)^lambda multiplicative bridge (no Euler product for gaps);
  (iv) the K-window: K <= O(log log log x) is hard-coded both in Conjecture 1.2 and in the
  singular-series lower bound S >= K^{-2K} vs (2.5).
- Relation to the project's delta recursion delta_{n+1} = 2 delta_n - g_{n+1}
  [context, not in PDF]: Pratt never iterates a recursion; he needs integrality of the tail
  at a single N. The recursion viewpoint and Pratt's viewpoint agree that rationality makes
  b delta_N integral (t = 2) for all N >= some N_0; Pratt's contribution is a mechanism to
  contradict integrality at one constructed N. A transfer attempt for S would look for: an
  n where the fractional part of delta_n is provably in (0,1) -- e.g. a window where all
  gaps g_{n+1..n+K} are known exactly (admissible constellation forced by a tuples-type
  conjecture) AND the remaining tail contribution mod 1 is controlled. The second half is
  the open structural gap; nothing in this paper addresses control of an unbounded-numerator
  tail mod 1.
