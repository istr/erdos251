# EXTRACTION: Baker-Freiberg, "Limit Points and Long Gaps Between Primes"

Source (only evidence base): /home/istr/pro/erdos251/dossier/1510.08054v1.pdf
arXiv:1510.08054v1 [math.NT] 27 Oct 2015. Authors: Roger Baker (Brigham Young
University) and Tristan Freiberg (University of Waterloo). 27 pages. The
printed date line on p. 1 reads "Date: June 1, 2021." (despite the arXiv v1
stamp of 27 Oct 2015; both are as printed in this PDF).

Transcription conventions: ASCII only. Diacritics transliterated (Erdos,
Cramer, Yildirim, Westzynthius). Math in LaTeX-like ASCII: log_2 T = log log T,
log_3 T = log log log T "and so on" (paper's footnote 2, p. 2); <= , >= ,
<< (Vinogradov), >> , \asymp (X \asymp Y iff X << Y << X, Section 2, p. 4),
O_<=(Y) = O(Y) with implied constant 1 (Section 2, p. 4), ~ means
X = (1+o(1))Y. P = set of all primes; p_n = n-th smallest prime;
d_n := p_{n+1} - p_n. a(b) := {a + bc : c in Z} (residue class). n + H :=
{n + q : q in H}. #S = cardinality. Boldface random variables are rendered
with a leading asterisk-free plain name and noted as random in context;
vectors as \vec a = (a_s(s))_{s in S}. ceil(.) = ceiling. Anchors are
theorem/equation/section numbers; page numbers (printed = PDF page) are
secondary aid.

Everything up to the final section is EXTRACTION (what the paper says).
Commentary appears ONLY in the final marked section.

---

## 1. ABSTRACT AND HEADLINE THEOREM (verbatim)

Abstract (p. 1), verbatim:

> "Let d_n := p_{n+1} - p_n, where p_n denotes the nth smallest prime, and
> let R(T) := log T log_2 T log_4 T/(log_3 T)^2 (the "Erdos-Rankin"
> function). We consider the sequence (d_n/R(p_n)) of normalized prime gaps,
> and show that its limit point set contains at least 25% of nonnegative real
> numbers. We also show that the same result holds if R(T) is replaced by any
> "reasonable" function that tends to infinity more slowly than
> R(T) log_3 T. We also consider "chains" of normalized prime gaps. Our
> proof combines breakthrough work of Maynard and Tao on bounded gaps between
> primes with subsequent developments of Ford, Green, Konyagin, Maynard and
> Tao on long gaps between consecutive primes."

So THE exact Erdos-Rankin normalization used (abstract p. 1, repeated p. 2):

> "R(T) := log T log_2 T log_4 T/(log_3 T)^2"

with footnote 2 (p. 2): "We define log_2 T := log log T, log_3 T :=
log log log T and so on."

Theorem 1.1 (Section 1, p. 2), verbatim:

> "Theorem 1.1. Let d_n := p_{n+1} - p_n, where p_n denotes the nth smallest
> prime, and let L_{R_1} denote the set of limit points in [0, infty] of the
> sequence (d_n/R_1(p_n))_{p_n >= T_0}, where
>   R_1(T) := log T log_2 T / log_3 T
> and T_0 is large enough so that log_3 T_0 >= 1. Given any five nonnegative
> real numbers alpha_1, ..., alpha_5 with alpha_1 <= ... <= alpha_5, we have
> {alpha_j - alpha_i : 1 <= i < j <= 5} cap L_{R_1} != emptyset."

Measure consequences (Section 1, p. 2), verbatim:

> "As in [1, Corollary 1.2], one may deduce from Theorem 1.1 that, with
> lambda denoting the Lebesgue measure on R,
> (1.1)  lambda([0, X] cap L_{R_1}) >= X/(4(1 + 1/2 + 1/3 + 1/4))  (X >= 0),
> and (with an ineffective o(1)),
> (1.2)  lambda([0, X] cap L_{R_1}) >= (1 - o(1))X/4  (X -> infty)."

[Note 4(1 + 1/2 + 1/3 + 1/4) = 25/3, so (1.1) is (3/25)X; (1.2) is the 25%.]

Conditional improvement (Section 1, pp. 2-3), verbatim:

> "As we will see, assuming a certain variant of the Elliott-Halberstam
> conjecture (cf. Hypothesis 5.3 below), one has {alpha_2 - alpha_1,
> alpha_3 - alpha_1, alpha_3 - alpha_2} cap L_{R_1} != emptyset for any three
> nonnegative real numbers alpha_1 <= alpha_2 <= alpha_3, with corresponding
> improvements to (1.1) and (1.2) (viz. 2 = 3 - 1 replaces 4 = 5 - 1)."

Positioning of the paper (Section 1, p. 2), verbatim:

> "Ford, Green, Konyagin, Maynard and Tao [4] have actually shown that, for
> infinitely many n, d_n >> R(p_n) log_3 p_n. The purpose of this paper is to
> fully integrate the work of the five-author paper [4] into the study of
> limit points of normalized prime gaps initiated in [1, 10, 11]. In so
> doing, we extend the aforementioned result of Pintz in three ways."

> "First, we show that the normalizing function R(T) may be replaced by any
> "reasonable" function that tends to infinity more slowly than
> R(T) log_3 T, for example R_1(T) = log T log_2 T / log_3 T. Second, we show
> that the 25% may conditionally be improved to 33 1/3 % or even 50% on a
> certain conjecture concerning the level of distribution of the primes.
> Third, we also consider "chains" of normalized, consecutive gaps between
> primes (cf. Theorem 6.4)."

Prior state of the art, verbatim (Section 1, pp. 1-2):

> "Hildebrand and Maier [7] showed in 1988 that a positive (but unspecified)
> proportion of nonnegative real numbers are limit points of
> (d_n/log p_n). More recently, the second author, Banks and Maynard [1] have
> shown that in fact at least 12.5% of nonnegative real numbers are limit
> points of (d_n/log p_n)."

> "Ford, Green, Konyagin, and Tao [3], and (independently) Maynard [9], have
> settled the notorious "Erdos-Rankin problem" by showing that infty is a
> limit point of (d_n/R(p_n)), where R(T) := log T log_2 T log_4 T/
> (log_3 T)^2."

> "Using basically the same strategy as in [1], and the work of Ford, Green,
> Konyagin, and Tao [3], Pintz [10, 11] has shown that at least 25% of
> nonnegative real numbers are limit points of (d_n/R(p_n)). In fact, Pintz's
> result is that the same statement holds if the normalizing function R(T) is
> replaced by any function -- subject to certain technical conditions -- that
> tends to infinity no faster than R(T), for example
> log T log_2 T/(log_3 T)^2."

Examples of admissible normalizations (Section 1, p. 2), verbatim:

> "Precisely what we mean by a "reasonable" function is best explained in
> context, so we defer the statement of our main result to Section 6 (cf.
> Theorem 6.2). Examples of "reasonable" functions are log_6 T, sqrt(log T),
> log_2 T/sqrt(log_3 T), (log T)^{7/9}, log T, R(T), R_1(T) and
> R_1(T) log_5 T. Any one of these could replace R_1(T) in the following
> special case of Theorem 6.2, which will serve as a placeholder."

---

## 2. PROOF STRATEGY (Section 3, verbatim anatomy)

Section 3, p. 4, verbatim:

> "Let x be a large number and set y := cx log x log_2 x/log_3 x, where
> c > 0 is a certain small constant. Ford, Green, Konyagin, Maynard and Tao
> [4] show that if C is large enough, then there exists a vector
> (c_p(p))_{p <= Cx} of residue classes for which
>   ((x, y] cap Z) \ Union_{p <= Cx} c_p(p) = emptyset.
> Thus, if b(W) is the residue class modulo W := prod_{p <= Cx} p =
> e^{(1+o(1))Cx} for which b == -c_p(p) for each p <= Cx, then for
> n == b(W) with n + x > Cx,
>   P cap (n + x, n + y] = emptyset."

[PRINTED-ODDITY: this Section 3 display has y := cx log x log_2 x/log_3 x,
whereas the operative definition (4.1) in Section 4 (and its recall in the
proof of Theorem 6.2, p. 24) is y := cx log x log_3 x/log_2 x, i.e. with
log_2 x and log_3 x exchanged. Both transcribed verbatim; (4.1) is the one
used in all quantitative estimates.]

> "We generalize this slightly by proving that if H is any set of K primes
> in (x, y] with K <= log x (say), the residue classes may be chosen so that
>   ((x, y] cap Z) \ Union_{p <= Cx} c_p(p) = H
> and hence
>   P cap (n + x, n + y] = P cap n + H.
> Note that H, being a set of K <= log x primes greater than
> p_K = O(K log K), is admissible."

> "Now let M >= 2 be an integer with M | K and let H = H_1 cup ... cup H_M
> be a partition of H into M subsets of equal size. As was shown in [1],
> with M = 9, a smaller choice of y and a minor technical condition on H,
> the Maynard-Tao sieve method establishes that for large N, there exists
> n in (N, 2N] cap b(W) and a pair i < j for which
>   #(P cap n + H_i), #(P cap n + H_j) >= 1,
> provided K is sufficiently large and W <= N^eta for some small eta."

> "Choosing j - i to be minimal, we obtain a pair of consecutive primes in
> n + H. We may carefully choose our primes in H so that the spacings
> between them grow faster than x/log x but slower than y."

> "Actually, for reasons related to level of distribution and "Siegel"
> zeros, we require that W not be a multiple of a certain putative
> "exceptional" modulus less than N^{O(eta)}. The largest prime divisor p'
> of this exceptional modulus, if it exists, satisfies
> p' >> log_2 N^eta >> log x. For this reason, we introduce a set Z of
> "unusable" primes, which has the properties of {p'}. Their effect is
> negligible." (pp. 4-5)

> "Pintz [11] has very recently given an elegant simplification of part of
> this argument, which we take advantage of in this paper, and which shows
> that one can take M = 5." (p. 5)

---

## 3. THE ERDOS-RANKIN HALF (Section 4: modified Ford-Green-Konyagin-Maynard-Tao)

### 3.1 Parameters and the sieving theorem

Section 4.1, p. 5, verbatim:

> "(4.1)  y := cx (log x log_3 x)/(log_2 x),
> where c is a certain (small) fixed positive constant, and
> (4.2)  z := x^{log_3 x/(4 log_2 x)}.
> We then define
> (4.3)  S := {s prime : (log x)^20 < s <= z},
> (4.4)  P := {p prime : x/2 < p <= x},
> (4.5)  Q := {q prime : x < q <= y}."

> "For vectors of residue classes \vec a := (a_s(s))_{s in S} and \vec b :=
> (b_p(p))_{p in P}, we define sifted sets
>   S(\vec a) := Z \ Union_{s in S} a_s(s)  and  S(\vec b) := Z \
>   Union_{p in P} b_p(p)."

> "(4.6)  #Q = (y/log x)(1 + O(log_2 x/log x)).
> Finally, let K be any natural number satisfying
> (4.7)  K <= log x.
> By (4.6), we may suppose x is large enough so that Q contains at least K
> primes. Since p_K << K log K, we may also suppose that p_K <= x. We fix any
> (4.8)  H := {q_1, ..., q_K} subseteq Q  with  #H = K.
> Note that H, being a set of K primes larger than p_K, is an admissible
> set."

Theorem 4.1 (Sieving for primes) (Section 4.1, p. 5), verbatim:

> "Theorem 4.1 (Sieving for primes). For all sufficiently large x, there
> exist vectors of residue classes \vec a = (a_s(s))_{s in S} and \vec b =
> (b_p(p))_{p in P} such that H subseteq S(\vec a) cap S(\vec b) and
> (4.9)  #(Q cap S(\vec a) cap S(\vec b)) << x/log x,
> where the implied constant is absolute."

Relation to [4] (p. 5), verbatim: "The only difference between Theorem 4.1
and [4, Theorem 2] is our additional requirement that H subseteq S(\vec a)
cap S(\vec b). Unsurprisingly, the proof of Theorem 4.1 follows that of
[4, Theorem 2] very closely, even verbatim in many parts."

Unusable primes (p. 6, verbatim): "We now introduce a set Z of "unusable"
primes with the property that for any p' in Z,
(4.10)  sum_{p >= p', p in Z} 1/p << 1/p' << 1/log x."

Corollary 4.2 (Section 4, p. 6), verbatim (the full-window confinement):

> "Corollary 4.2. Let C be a sufficiently large but fixed positive constant.
> For all sufficiently large x, there exists a vector of residue classes
> (c_p(p))_{p <= Cx, p notin Z} such that
>   H = (Z cap (x, y]) \ Union_{p <= Cx, p notin Z} c_p(p)."

Lemma 4.3 (= [1, Lemma 5.1]; p. 6), verbatim:

> "Lemma 4.3. Let H, T be sets of integers, P a set of primes, such that for
> some x >= 2, H subseteq T subseteq [0, x^2] and #{p in P : p > x} >
> #H + #T. If H is admissible then there exists a vector of residue classes
> (gamma_p(p))_{p in P} such that H = T \ Union_{p in P} gamma_p(p)."

Deduction of Corollary 4.2 (pp. 6-7), paraphrase (marked): enlarge the sifted
sets to S_Z(\vec a), S_Z(\vec b) (ignoring unusable primes); the leftover set
T := (Z cap (x,y]) \ Union_{p <= x, p notin Z} c_p(p) with c_p = a_p on
S \ Z, b_p on P \ Z, 0 on L \ Z (L := primes in [2, (log x)^20] cup
(z, x/2]) decomposes into cases (1) n divisible by a prime p' > x/2 -- these
lie in Q cap S_Z cap S_Z, count << x/log x (4.12); (2) n divisible by a
prime p' in (z, x/2] -- forces p' in Z, count << y sum_{p > z, p in Z} 1/p
<< y/z = o(x/log x) (4.13); (3) n z-smooth -- "As shown in [4, Theorem 2
et seq.], smooth number estimates give #{n in T : (3) holds} = o(x/log x)"
(4.14, verbatim conclusion). Then K + #T << x/log x, choose C with
#{p prime : p in (x, Cx], p notin Z} > K + #T, and apply Lemma 4.3 to sift
T down to exactly H.

### 3.2 The random construction (Theorem 4.4) and its engine

Theorem 4.4 (Random construction) (Section 4, pp. 7-8), verbatim:

> "Theorem 4.4 (Random construction). Let x be sufficiently large. There
> exists a positive number C with
> (4.15)  C \asymp 1/c,
> the implied constants being independent of c, a set of positive integers
> {h_1, ..., h_r} with r <= sqrt(log x), and random vectors \vec a =
> (a_s(s))_{s in S} and \vec n = (n_p)_{p in P} of residue classes a_s(s)
> and integers n_p respectively, satisfying the following.
> (i) For every \vec a = (a_s(s))_{s in S} in the essential range of \vec a,
>     we have H cap a_s(s) = emptyset (s in S).
> (ii) For every \vec n = (n_p(p))_{p in P} in the essential range of
>     \vec n, we have H cap n_p(p) = emptyset (p in P).
> (iii) For every \vec a in the essential range of \vec a, we have
>     P(q in e_p(\vec a) | \vec a = \vec a) <= x^{-3/5} (p in P),
>     where e_p(\vec a) := {n_p + h_i p : i <= r} cap Q cap S(\vec a).
> (iv) With probability 1 - o(1), we have
> (4.16)  #(Q cap S(\vec a)) ~ 80cx (log_2 x)/(log x).
> (v) Call an element \vec a in the essential range of \vec a "good" if,
>     for all but at most x/(log x log_2 x) elements q in Q cap S(\vec a),
>     one has
> (4.17)  sum_{p in P} P(q in e_p(\vec a) | \vec a = \vec a)
>           = C + O_<=(1/(log_2 x)^2).
>     Then \vec a is good with probability 1 - o(1)."

Proof skeleton of Theorem 4.4 (Section 4.2, pp. 8-18), quantitative anchors:

- (4.18) r := floor((log x)^{1/5}); h_i := (2i - 1)^2 for i <= r (p. 8).
- Lemma 4.5 (Existence of a good sieve weight; "a special case of
  [4, Theorem 5]", p. 8), verbatim conclusions: there exist tau >= x^{o(1)}
  and u \asymp log_2 x (4.19), and w : P x Z -> R^+ supported on
  P x [-y, y] with
  (4.20) sum_{n in Z} w(p, n) = (1 + O(1/(log_2 x)^10)) tau y/(log x)^r
  uniformly for p in P;
  (4.21) sum_{p in P} w(p, q - h_i p)
         = (1 + O(1/(log_2 x)^10)) tau (u/r) x/(2 (log x)^r)
  uniformly for q in Q and i <= r;
  (4.22) w(p, n) = O(x^{1/3 + o(1)}).
  [This w is the FGKMT weight: it concentrates n_p so that the r-tuple
  {n_p + h_i p} hits Q.]
- w_H(p, n) := w(p, n) if H cap n(p) = emptyset, 0 otherwise (p. 9);
  Lemma 4.6: (4.20)-(4.22) survive with w_H in place of w, q in Q \ H.
  [This is the H-protecting modification: the random translates never touch
  the prescribed primes H.]
- Random n~_p with P(n~_p = n) := w_H(p, n)/sum_{n'} w_H(p, n');
  (4.23) sum_{p in P} P(q = n~_p + h_i p) = 1_{Q\H}(q)
         (1 + O(1/(log_2 x)^10)) (u/r) (x/2y)  (q in Q, i <= r);
  (4.24) P(n~_p = n) << x^{-2/3 + o(1)};
  (4.25) P(H cap n~_p(p) != emptyset) = 0  (p in P). (p. 9)
- \vec a: each a_s(s) uniform on Omega_H(s) := (Z/sZ) \ {q(s) : q in H}
  (4.26), independent; "Note, then, that for any random vector \vec a,
  H subseteq S(\vec a)." (p. 9). Densities: sigma_H := prod_{s in S}
  (1 - 1/#Omega_H(s)) = sigma (1 + O(1/(log x)^19)) (4.27), sigma :=
  prod_{s in S}(1 - 1/s); (4.28) sigma y = (1 + O(1/(log_2 x)^10))
  80cx log_2 x; (4.29) sigma^r = x^{o(1)}. (p. 10)
- (4.30) X_p(\vec a) := P(n~_p + h_i p in S(\vec a) for all i <= r);
  (4.31) P(\vec a) := {p in P : X_p(\vec a) =
  (1 + O_<=(1/(log x)^6)) sigma^r}; Z_p(\vec a; n) :=
  1_{(n + h_j p in S(\vec a) forall j <= r)} P(n~_p = n); conditional law
  (4.32) P(n_p = n | \vec a = \vec a) = Z_p(\vec a; n)/X_p(\vec a), n_p
  jointly conditionally independent; n_p = 0 if p notin P(\vec a). (p. 10)
- Second-moment lemmas: Lemma 4.7 (p. 11; sifting probabilities
  P(n_1,...,n_t in S(\vec a)) = (1 + O(1/(log x)^16)) sigma^t for distinct
  n_i of magnitude x^{O(1)}, t <= log x, H cap {n_i} = emptyset); Lemma 4.8
  (p. 12; P(\vec a) contains all but O(#P/(log x)^3) of P w.p.
  1 - O(1/log x)); Lemma 4.9 (p. 14); Lemma 4.10 (pp. 14-16, first and
  second moments of U(q, \vec a) := sigma^{-r} sum_{i <= r} sum_{p in P}
  Z_p(\vec a; q - h_i p)); "We now specify that the quantity C in Theorem
  4.4 is C := ux/(2 sigma y), so that C \asymp 1/c." (p. 16, verbatim);
  Lemma 4.11 (p. 16; U(q, \vec a) = (1 + O_<=(1/(log_2 x)^3)) C for all but
  at most x/(2 log x log_2 x) primes q in Q cap S(\vec a), w.p. 1 - o(1));
  Lemma 4.12 (p. 17).

### 3.3 The hypergraph covering step and proof of Theorem 4.1

Lemma 4.13 ("a special case of [4, Corollary 3]", Section 4.3, p. 18),
verbatim:

> "Lemma 4.13. Let Q' be a set of primes with #Q' > (log_2 x)^3. For each
> p in P, let e_p be a random subset of Q' with
>   #e_p <= r,  P(q in e_p) <= x^{-3/5}  (q in Q').
> Suppose that for all but at most #Q'/(log_2 x)^2 elements q in Q', we have
>   sum_{p in P} P(q in e_p) = C + O_<=(1/(log_2 x)^2),
> where C is independent of q and
> (4.48)  (5/4) log 5 <= C << 1.
> Suppose that for any distinct q_1, q_2 in Q',
> (4.49)  sum_{p in P} P(q_1, q_2 in e_p) <= x^{-1/20}.
> [TRANSCRIPTION-UNSURE: the summation subscript in (4.49) renders as "P 1"
> in the text layer, possibly P'; the verification on p. 19 sums over
> p in P.]
> Then for any positive integer m with
>   m <= log_3 x/log 5,
> we can find random sets e'_p subseteq Q' for each p in P such that e'_p is
> either empty or is in the essential range of e_p, and
> (4.50)  #{q in Q' : q notin e'_p for all p in P} ~ 5^{-m}(#Q'),
> with probability 1 - o(1)."

Deduction of Theorem 4.1 (p. 19), key lines verbatim: "By (4.15), we may
choose c small enough so that (4.48) holds. Take m = floor(log_3 x/log 5)."
Then with Q' = Q cap S(\vec a), e_p = e_p(\vec a): "Recalling (4.16),
#{q in Q' : q notin e'_p for all p in P} ~ 5^{-m} #(Q cap S(\vec a))
<< x/log x with probability 1 - o(1)." [5^{-m} \asymp 1/log_2 x kills the
log_2 x factor in (4.16).] "The bound (4.9) follows on setting b_p = n'_p
for a specific \vec n' = (n~'_p) for which this bound holds. That H is
contained in S(\vec a) cap S(\vec b) follows from parts (i) and (ii) of
Theorem 4.4."

---

## 4. THE MAYNARD-TAO HALF (Section 5) AND THE LEVEL-OF-DISTRIBUTION KNOB

Definition 5.1 (Section 5, p. 19), verbatim:

> "Definition 5.1. We consider functions of the form f_1 : [T_1, infty) ->
> [x_1, infty), with T_1, x_1 >= 1. Let us say that such a function f_1 is
> "of the first kind" if and only if (i) it is a strictly increasing
> bijection, (ii) f_1(T) <= log T for T >= T_1, (iii) f_1(2T)/f_1(T) -> 1 as
> T -> infty and (iv) for 0 < eta <= 1, there exists L_eta >= 1 such that
> f_1(T)/f_1(T^eta) -> L_eta as T -> infty."

Definition 5.2 (p. 19), verbatim:

> "Definition 5.2. We consider (possibly empty) sets Z(T), T >= 2, of primes
> less than or equal to T. Let us that such a set is "repulsive" if and only
> if for any p' in Z(T), sum_{p in Z(T), p >= p'} 1/p << 1/p' <<
> 1/log_2 T."

[PRINTED-ODDITY: "Let us that" (missing "say") is as printed.]

Discrepancy functional (p. 19): Delta(v; a(D)) := sum_{n == a(D)} v(n) -
(1/phi(D)) sum_{(n,D)=1} v(n).

Hypothesis 5.3 (Section 5, pp. 19-20), verbatim (the EH-variant knob):

> "Hypothesis 5.3. Fix theta in (0, 1] and a function f_1 : [T_1, infty) ->
> [x_1, infty) of the first kind. For any given A > 0 and delta in
> (0, theta), if eta = eta(A, delta) in (0, theta - delta) is a sufficiently
> small, fixed number then, for N >= T_1^{1/eta}, there is a repulsive
> subset Z := Z(N^{4 eta}) of the primes less than or equal to N^{4 eta}
> such that, with W := prod_{p <= N^eta, p notin Z} p and Z :=
> prod_{p in Z} p, we have
>   sum_{r <= N^theta/(N^delta W), (r, WZ) = 1, r squarefree}
>     max_{N <= M <= 2N} max_{(rW, a) = 1}
>     |Delta(1_P 1_{(M, M+N]}; a(rW))|  <<_{delta, A}  N/(phi(W)(log N)^A)."

Theorem 5.4 (Section 5, p. 20), verbatim (the block-occupancy engine):

> "Theorem 5.4. Fix theta in (0, 1] and a function f_1 : [T_1, infty) ->
> [x_1, infty) of the first kind. Suppose that Hypothesis 5.3 holds. Fix a
> positive integer a. In the notation of Hypothesis 5.3, if K = K_{theta,a}
> is a sufficiently large integer multiple of ceil((2/theta)a) + 1, if
> A = A_K is sufficiently large and if delta = delta_{theta,a} is
> sufficiently small, then the following holds for N >= N(T_1, K, eta). Let
> H := {H_1, ..., H_K} subseteq [0, N] be an admissible set of K distinct
> integers for which prod_{1 <= i < j <= K} (H_j - H_i) is
> f_1(N^eta)-smooth, and let b be an integer such that
>   (prod_{i=1}^{K} (b + H_i), W) = 1.
> Then for any partition
>   H = H_1 cup ... cup H_{ceil((2/theta)a)+1}
> of H into ceil((2/theta)a) + 1 sets of equal size, there exists some
> n in (N, 2N] cap b(W), and a + 1 distinct indices i_1, ..., i_{a+1} in
> {1, ..., ceil((2/theta)a) + 1}, such that
>   #(P cap n + H_{i_1}), ..., #(P cap n + H_{i_{a+1}}) >= 1."

Theorem 5.5 (p. 20), verbatim (the unconditional case):

> "Theorem 5.5. Hypothesis 5.3, and therefore the statement of Theorem 5.4,
> holds with theta = 1/2 and any function f_1 : [T_1, infty) -> [x_1, infty)
> of the first kind."

Proof anchors (pp. 20-22): "That Hypothesis 5.3 holds with theta = 1/2 and
any function f_1 ... of the first kind is a consequence of Lemma 4.1 and
Theorem 4.2 of [1]." (verbatim, p. 20). "We prove Theorem 5.4 by following
Pintz's [11] modification to the proof of Theorem 4.3 (i) in [1]." (p. 20).
"Only the unconditional case theta = 1/2 is considered in [1, 11], whereas
here we are considering theta <= 1. To do this, we need to note that on
Hypothesis 5.3, the term 4 + O(delta) may be replaced by (2/theta) +
O(delta) on the right-hand side of the inequality in [1, Lemma 4.5 (iii)].
In the proof of this lemma in [1, Section 4.2], the support of the smooth
function G : [0, infty) -> R, which is [0, 1/4 - 2 delta], may be replaced
by [0, (theta/2) - 2 delta], and the rest of the proof may be carried out,
mutatis mutandis." (verbatim, p. 20).

Pintz-style counting observation (p. 21), paraphrase (marked): with
mu' := max_{v in N}(v - mu binom(v, 2)) (= (1/2)(1 + 1/mu) when mu is a
reciprocal of a positive integer), if #(P cap n + H_j) = 0 for all but at
most a of the subsets H_j, then sum_{j} {sum_{H in H_j} 1_P(n + H) - mu
sum_{H != H' in H_j} 1_P(n+H) 1_P(n+H')} <= mu' a; so positivity of
sum_{H in H} 1_P(n+H) - mu' a - mu sum_j sum_{H != H' in H_j} ... forces
#(P cap n + H_j) >= 1 for at least a + 1 subsets.

Parameter ladder in the proof (p. 21), verbatim:

> "Fix any positive integer a and let M = M_{theta,a} be the integer
> satisfying M - 2 < (2/theta) a <= M - 1. Let iota = iota_{theta,a} be a
> small, fixed quantity to be specified. Set delta = delta_{theta,a} :=
> iota^2/(aM). Let K = K_{theta,a} be the integer satisfying
> e^{aM^2/(delta(M-1))} < K <= e^{aM^2/(delta(M-1))} + M and M | K. Finally,
> let rho := (aM^2/(M-1))/(delta log K) < 1."

Weighted sum (p. 21): S := sum_{N < n <= 2N, n == b(W)} {sum_{H in H}
1_P(n+H) - ((1+M)/2) a - (1/M) sum_{j=1}^{M} sum_{H != H' in H_j}
1_P(n+H) 1_P(n+H')} nu_H(n), with nu_H(n) := (sum_{d_i | n + H_i forall i}
lambda_{d_1,...,d_K})^2, "where (lambda_{d_1,...,d_K}) is the Maynard-Tao
sieve as used in [1, Section 4]" (p. 22). Final lower bound (p. 22,
verbatim): "S >= (aM^2/(M-1))(1 + O(iota/(aM))) - ((1+M)/2) a -
(aM^2/(2(M-1)))(1 + O(iota/(aM))) = a(1 + O(iota))/(2(M-1)). Taking iota
sufficiently small gives S > 0" [S here is the normalized
fraktur-S = S N^{-1} W B^K I_K(F)^{-1} rearranged; transcription of the
normalization: "define fraktur-S by the relation S = fraktur-S N W^{-1}
B^{-K} I_K(F), with B and I_K(F) as defined in [1, Section 4.2]", p. 22;
xi = (log K)^{-1/2}].

---

## 5. MAIN THEOREM (Section 6): SCALES, MEASURES, CHAINS

Definition 6.1 (Section 6, p. 22), verbatim:

> "Definition 6.1. We consider functions f_2 : [x_2, infty) -> [z_2, infty),
> with x_2, z_2 >= 1. Let us say that such a function f_2 is "of the second
> kind" if and only if (i) it is a strictly increasing bijection, (ii)
>   (x/log x)/f_2(x) -> 0  and  f_2(x)/(x log x log_3 x/log_2 x) -> 0
> as x -> infty and (iii) for any C > 0, f_2(Cx)/(C f_2(x)) -> 1 as
> x -> infty."

[TRANSCRIPTION-UNSURE: in (iii) the text layer prints "Cf(x)" for the
denominator; from context (applied to f_2 throughout, e.g. p. 25) it is
C f_2(x).]

Theorem 6.2 (Section 6, pp. 22-23), verbatim (THE main theorem):

> "Theorem 6.2. Fix theta in (0, 1] and a function f_1 : [T_1, infty) ->
> [x_1, infty) of the first kind, and suppose Hypothesis 5.3 holds. Fix a
> function f_2 : [x_1, infty) -> [z_2, infty) of the second kind and let
> f := f_2 o f_1. Let d_n := p_{n+1} - p_n, where p_n denotes the nth
> smallest prime, and let L_f denote the set of limit points in [0, infty]
> of the sequence (d_n/f(p_n))_{p_n >= T_1}. Then given any
> ceil(2/theta) + 1 nonnegative real numbers alpha_1, ...,
> alpha_{ceil(2/theta)+1} with alpha_1 <= ... <= alpha_{ceil(2/theta)+1},
> we have
> (6.1)  {alpha_j - alpha_i : 1 <= i < j <= ceil(2/theta) + 1} cap L_f
>          != emptyset.
> Consequently, letting lambda denote the Lebesgue measure on R, we have
> (6.2)  lambda([0, X] cap L_f) >= c_1(theta) X  (X >= 0)
> and
> (6.3)  lambda([0, X] cap L_f) >= (1 - o(1)) c_2(theta) X  (X -> infty),
> where
> (6.4)  c_1(theta) := (ceil(2/theta)(1 + 1/2 + ... + 1/ceil(2/theta)))^{-1}
>        and  c_2(theta) := 1/ceil(2/theta)."

Table 1 (p. 23), verbatim content ("Possible values of ceil(2/theta) + 1,
c_1(theta) and c_2(theta)"):

  theta in [1/2, 2/3): ceil(2/theta) + 1 = 5,  c_1 = 3/25,  c_2 = 1/4
  theta in [2/3, 1):   ceil(2/theta) + 1 = 4,  c_1 = 2/11,  c_2 = 1/3
  theta = 1:           ceil(2/theta) + 1 = 3,  c_1 = 1/3,   c_2 = 1/2

Deduction of Theorem 1.1 (p. 23), verbatim:

> "In view of Theorem 5.5, we may unconditionally apply Theorem 6.2 with
> theta = 1/2 and any function f_1 : [T_1, infty) -> [x_1, infty) of the
> first kind. Let f_1 : [e^{e^e}, infty) -> [e^e, infty) be given by
> f_1(T) = log T, and let f_2 : [e^e, infty) -> [e^{e+1}, infty) be given by
> f_2(x) = x log x/log_2 x. Then f_1 is of the first kind, f_2 is of the
> second kind and f_2 o f_1(T) = R_1(T) = log T log_2 T/log_3 T for
> T >= e^{e^e}."

Lemma 6.3 (Section 6, p. 23), verbatim (skeleton placement + smoothness):

> "Lemma 6.3. Let K be a natural number and let K = K_1 + ... + K_M be a
> partition of K. Let x and y be real numbers such that K <= y/x <= log x.
> If x is sufficiently large, then for any M (possibly overlapping)
> subintervals (v_i, v_i + x/log x] subseteq (x, y], i <= M, there exist M
> pairwise disjoint sets of primes H_i subseteq (v_i, v_i + x/log x] with
> |H_i| = K_i, such that if H_1 cup ... cup H_M = {q_1, ..., q_K}, then
> prod_{1 <= i < j <= K} (q_j - q_i) is x-smooth."

Proof mechanism (pp. 23-24), paraphrase (marked): take D the integer with
y/x <= D < 1 + y/x and select the q's among primes == 1 (mod D) in each
subinterval (PNT for APs, [2, Section 22 (4)], supplies >= K of them since
K <= log x); then for two such primes q < q', q' - q <= y and q' == q (D)
force every prime divisor of q' - q to divide D < 1 + log x or be
<= y/D <= x; hence x-smooth.

Proof of Theorem 6.2 (pp. 24-25) -- the site anatomy, key steps verbatim:

> "In accordance with Theorem 5.4 (in which we take a = 1), let K = K_theta
> be a sufficiently large integer multiple of ceil(2/theta) + 1, let
> A = A_K be sufficiently large and delta = delta_theta and eta =
> eta(A, K) be sufficiently small." (p. 24)

> "In accordance with Corollary 4.2, let C be a sufficiently large but fixed
> positive constant and let x be a sufficiently large number. Suppose, as we
> may, that Cx >= x_1, and (cf. Definition 5.1 (i)) set
>   N := (f_1^{-1}(Cx))^{1/eta}.
> Thus, Cx = f_1(N^eta) and N tends to infinity with x." (p. 24)

> "By Definition 5.1 (iv) there exists L_eta >= 1 such that f_1(N)/x ->
> C L_eta as x -> infty. Fix nonnegative real numbers alpha_1, ...,
> alpha_{ceil(2/theta)+1} with alpha_1 <= ... <= alpha_{ceil(2/theta)+1}
> and set
> (6.5)  beta_i := alpha_i C L_eta,  i <= ceil(2/theta) + 1." (p. 24)

> "Fix a function f_2 : [x_2, infty) -> [z_2, infty) of the second kind and
> consider the intervals
> (6.6)  (x + beta_i f_2(x), x + beta_i f_2(x) + x/log x],
>          i <= ceil(2/theta) + 1.
> Recall that y := cx log x log_3 x/log_2 x, where c > 0 is a certain
> constant (cf. (4.1)). By Definition 6.1 (ii) we have x/log x = o(f_2(x))
> and f_2(x) = o(y). Suppose, then, that x is large enough (in terms of
> beta_{ceil(2/theta)+1}) so that the intervals in (6.6) are all contained
> in (x, y]." (p. 24)

> "In accordance with Lemma 6.3, choose ceil(2/theta) + 1 pairwise disjoint
> sets of primes H_i of equal size, with
> (6.7)  H_i subseteq (x + beta_i f_2(x), x + beta_i f_2(x) + x/log x],
>          i <= ceil(2/theta) + 1.
> Thus, letting H := H_1 cup ... cup H_{ceil(2/theta)+1} =: {q_1, ...,
> q_K}, we have that prod_{1 <= i < j <= K} (q_j - q_i) is x-smooth, and
> hence f_1(N^eta)-smooth (we may suppose that C >= 1)." (p. 24)

> "As K is fixed we may of course suppose that K <= log x and p_K <= x, so
> that (4.7) is satisfied and H, being a set of K primes larger than p_K,
> is admissible. We may of course also suppose that y <= N, so that
> H subseteq [0, N]. Thus, H satisfies each of the hypotheses of Theorem
> 5.4." (p. 24)

Repulsive-set compatibility (pp. 24-25), verbatim: "Let Z(N^eta) be as in
Hypothesis 5.3, so that Z(N^eta) is repulsive (cf. Definition 5.2), and
note that since x <= f_1(N^eta) <= log N^eta (cf. Definition 5.1 (ii)),
sum_{p in Z(N^eta), p >= p'} 1/p << 1/p' << 1/log_2 N^eta <=
1/log f_1(N^eta) <= 1/log x. Thus, (4.10) is satisfied with Z = Z(N^eta).
Therefore, by Corollary 4.2 there exists a vector of residue classes
(c_p(p))_{p <= f_1(N^eta), p notin Z(N^eta)} such that
(6.8)  H = (Z cap (x, y]) \ Union_{p <= f_1(N^eta), p notin Z(N^eta)}
c_p(p)."

> "Let b(W) be the arithmetic progression modulo W :=
> prod_{p <= f_1(N^eta), p notin Z(N^eta)} p such that b == -c_p(p) for all
> primes p <= f_1(N^eta) with p notin Z(N^eta). By (6.8) we have
> (prod_{i=1}^{K} (b + q_i), W) = 1." (p. 25)

> "Each hypothesis of Theorem 5.4 now accounted for, we conclude that there
> is some n in (N, 2N] cap b(W), and a pair of indices i_1, i_2 in
> {1, ..., ceil(2/theta) + 1}, i_1 < i_2, such that #(P cap n + H_{i_1})
> >= 1 and #(P cap n + H_{i_2}) >= 1. If there are more than two such
> indices, we take i_2 - i_1 to be minimal." (p. 25)

> "Thus, if p is the largest prime in P cap n + H_{i_1} and p' is the
> smallest prime in P cap n + H_{i_2}, then p and p' are consecutive, that
> is, p = p_t and p' = p_{t+1} for some t. Indeed, by (6.8) and the
> definition of b(W), for any n == b(W) with n + x >= f_1(N^eta) we have
>   P cap (n + x, n + y] = P cap n + H." (p. 25)

> "By (6.7) and (6.5), and since x/log x = o(f_2(x)), we have
>   p_{t+1} - p_t = (beta_{i_2} - beta_{i_1}) f_2(x) + O(x/log x)
>                 = (alpha_{i_2} - alpha_{i_1} + o(1)) C L_eta f_2(x).
> Since there are only O(1/theta^2) distinct pairs of indices from which
> i_1 and i_2 may be chosen, we deduce that there exists a single pair
> i_1 < i_2 such that, for arbitrarily large N, we have
>   p_{t+1} - p_t = (alpha_{i_2} - alpha_{i_1} + o(1)) C L_eta f_2(x),
> for some pair of consecutive primes p_t, p_{t+1} in (N, N + y] subseteq
> (N, 3N]." (p. 25)

> "Finally, using Definition 5.1 (i), (iii) and (iv) and Definition 6.1 (i)
> and (iii), we find that C L_eta f_2(x) ~ f_2(f_1(N)) ~ f_2(f_1(3N)). We
> conclude that
>   (p_{t+1} - p_t)/f_2(f_1(p_t)) = (1 + o(1))(alpha_j - alpha_i).
> We deduce (6.2) and (6.3) by using the argument of [1, Corollary 1.2]."
> (p. 25)

Chains (Section 6, pp. 25-26). Lead-in, verbatim: "As in [1, Theorem 1.3],
we may also consider "chains" of normalized, consecutive gaps between
primes. Using essentially the same argument as above, but using (the
unconditional) Theorem 4.3 (ii) of [1] in place of Theorem 5.4, one may
verify the following result."

Theorem 6.4 (pp. 25-26), verbatim:

> "Theorem 6.4. Fix any integer a with a >= 2. Fix functions f_1 :
> [T_1, infty) -> [x_1, infty) and f_2 : [x_1, infty) -> [z_2, infty) of the
> first and second kinds respectively, and let f := f_2 o f_1. Let d_n :=
> p_{n+1} - p_n, where p_n denotes the nth smallest prime, and let L_{a,f}
> denote the set of limit points in [0, infty]^a of the sequence of
> "chains"
>   ( d_n/f(p_n), ..., d_{n+a-1}/f(p_{n+a-1}) )
> for p_n >= T_1. Given alpha = (alpha_1, ..., alpha_K) in R^K, let
> S_a(alpha) be the set
>   { (alpha_{J(2)} - alpha_{J(1)}, ..., alpha_{J(a+1)} - alpha_{J(a)}) :
>       1 <= J(1) < ... < J(a+1) <= K }.
> For any 8a^2 + 16a nonnegative real numbers alpha_1 <= ... <=
> alpha_{8a^2+16a}, we have S_a(alpha) cap L_{a,f} != emptyset."

[TRANSCRIPTION-UNSURE: the final symbol renders in the text layer as "Laf";
the object defined in the statement is L_{a,f}, so it is transcribed as
L_{a,f}.]

Closing remarks (Section 6, p. 26), verbatim:

> "Let us call a function "reasonable" if it is of the form f_2 o f_1,
> where f_1 is a function of the first kind and f_2 is a function of the
> second kind. Theorem 6.4 shows that for any a there are infinitely many
> chains of consecutive prime gaps with d_n, ..., d_{n+a-1} > f(p_n) for any
> reasonable function f. There are reasonable functions f for which
> f(T)/(R(T) log_3 T) tends to 0 arbitrarily slowly (recall that R(T) =
> log T log_2 T log_4 T/(log_3 T)^2 is the Erdos-Rankin function). We
> believe that in a forthcoming paper [5], Ford, Maynard and Tao show that
> for any a there are infinitely many chains of consecutive prime gaps with
> d_n, ..., d_{n+a-1} >> R(p_n) log_3 p_n."

---

## 6. SCALE FLEXIBILITY: WHAT NORMALIZATIONS ARE COVERED (extraction summary with anchors)

- The normalization family is exactly f = f_2 o f_1 ("reasonable", p. 26)
  with f_1 of the first kind (Definition 5.1: strictly increasing bijection,
  f_1(T) <= log T, f_1(2T)/f_1(T) -> 1, f_1(T)/f_1(T^eta) -> L_eta) and f_2
  of the second kind (Definition 6.1: strictly increasing bijection,
  (x/log x)/f_2(x) -> 0 AND f_2(x)/(x log x log_3 x/log_2 x) -> 0,
  f_2(Cx)/(C f_2(x)) -> 1).
- Bottom of the covered range: the p. 2 examples list begins "log_6 T,
  sqrt(log T), log_2 T/sqrt(log_3 T)" -- arbitrarily slowly growing scales
  are included (but every reasonable f tends to infinity, since f_1, f_2 are
  increasing bijections onto [x_1, infty), [z_2, infty)).
- Top of the covered range: "any "reasonable" function that tends to
  infinity more slowly than R(T) log_3 T" (abstract, p. 1; p. 2); "There
  are reasonable functions f for which f(T)/(R(T) log_3 T) tends to 0
  arbitrarily slowly" (p. 26). The cap f_2(x) = o(x log x log_3 x/log_2 x)
  (Definition 6.1 (ii)) is exactly the sieve length (4.1): the proof needs
  f_2(x) = o(y) so the intervals (6.6) fit inside the sieved window (x, y]
  (p. 24). At the cap scale itself the only known statement quoted is FGKMT:
  "for infinitely many n, d_n >> R(p_n) log_3 p_n" (p. 2), i.e. the single
  limit point infty.
- Bottom constraint mechanism: (x/log x)/f_2(x) -> 0 (Definition 6.1 (ii))
  is what makes the placement error O(x/log x) in p_{t+1} - p_t negligible
  (p. 25: "since x/log x = o(f_2(x))"). The x/log x is the subinterval
  width in Lemma 6.3/(6.6).
- Intermediate scales: log T, (log T)^{7/9}, sqrt(log T), R(T), R_1(T),
  R_1(T) log_5 T are all named as covered examples (p. 2). NO obstruction to
  intermediate scales is stated anywhere in the text; the stated boundary is
  only the upper edge R(T) log_3 T (abstract; p. 26). The only structural
  restrictions on the normalization are the regularity conditions of
  Definitions 5.1 and 6.1 (bijectivity, slow variation, the f_1 <= log T
  cap, and the two-sided growth window on f_2).
- The fraction achieved does not depend on the scale: 25% (c_2 = 1/4)
  unconditionally at every reasonable scale (Theorem 6.2 + Theorem 5.5 with
  theta = 1/2, Table 1); 33 1/3% for theta in [2/3, 1), 50% at theta = 1
  under Hypothesis 5.3 (Table 1, p. 23; p. 2).

---

## 7. WHAT IS PRESCRIBED EXACTLY VS ONLY AS LIMIT POINTS (extraction summary with anchors)

Prescribed EXACTLY (deterministically, for the constructed n):

1. Window confinement: "P cap (n + x, n + y] = P cap n + H" (Section 3,
   p. 4; proved form: (6.8) + b(W), p. 25). Every integer in the length-
   (y - x) window other than the K prescribed sites n + q_i is composite,
   by construction (each is covered by a residue class c_p(p), p <=
   f_1(N^eta), p notin Z(N^eta)). This holds for EVERY n == b(W) with
   n + x >= f_1(N^eta) (p. 25), not just the Maynard-Tao-selected n.
2. The skeleton H itself: any K primes in (x, y] subject to (4.7)
   K <= log x (Theorem 4.1/(4.8)); in the main proof additionally placed in
   the prescribed subintervals (6.6)/(6.7) of width x/log x at offsets
   beta_i f_2(x), with all pairwise differences x-smooth (Lemma 6.3).
3. Block sizes: the partition into ceil((2/theta)a) + 1 equal blocks
   (Theorem 5.4).

Guaranteed but NOT located (existence via Maynard-Tao weight positivity):

4. Occupancy: "there exists some n in (N, 2N] cap b(W), and a + 1 distinct
   indices i_1, ..., i_{a+1} ... such that #(P cap n + H_{i_1}), ...,
   #(P cap n + H_{i_{a+1}}) >= 1" (Theorem 5.4). WHICH blocks are occupied,
   and which sites within a block are prime, is not controlled; only
   ">= 1" per occupied block.

Obtained only as LIMIT POINTS along subsequences:

5. The pair identity: "Since there are only O(1/theta^2) distinct pairs of
   indices from which i_1 and i_2 may be chosen, we deduce that there
   exists a single pair i_1 < i_2 such that, for arbitrarily large N, we
   have p_{t+1} - p_t = (alpha_{i_2} - alpha_{i_1} + o(1)) C L_eta f_2(x)"
   (p. 25). I.e. only SOME difference alpha_j - alpha_i out of the
   binom(ceil(2/theta)+1, 2) prescribed candidates is realized -- the
   pigeonhole cannot say which.
6. The gap value: realized only as (1 + o(1))(alpha_j - alpha_i) after
   normalization ("(p_{t+1} - p_t)/f_2(f_1(p_t)) = (1 + o(1))
   (alpha_j - alpha_i)", p. 25): an asymptotic equality along the
   subsequence of good N, never an exact integer gap.
7. Chains: same structure with a-tuples; some difference-vector from
   S_a(alpha), alpha of length 8a^2 + 16a, is a limit point in
   [0, infty]^a (Theorem 6.4); a is a FIXED integer >= 2 ("Fix any integer
   a with a >= 2"), with K and all parameters depending on a (in Theorem
   5.4: K = K_{theta,a}, e^{aM^2/(delta(M-1))} < K, p. 21) -- no statement
   with a growing as a function of x/N appears anywhere in the text.

---

## 8. SEARCH FOR ERDOS #251-TYPE MATERIAL

Searched the full text dump (1541 lines, all 27 pages) for: "irrational",
"2^n", "binary", "digit", "series", "251", "sum p", "numerator". Result:
NOTHING -- the paper contains no mention of irrationality, base-2/binary
expansions, the series sum p_n/2^n, or Erdos problem #251. Its subject is
exclusively the limit-point set of normalized gap sequences (d_n/f(p_n))
and chains thereof. NOT FOUND in this text: any statement about digits,
weighted gap sums, or gap-word repetition/matching.

---

## COMMENTARY (assessment, NOT extraction)

Consuming context: the project needs an UNCONDITIONAL supply of two
prime-gap-word sites with matched J-prefix and K-suffix windows and a
dominant weighted middle difference, at depths J, K ~ log_2 log x
("exchange configuration"). Known blockers: (i) pigeonhole is blind to
variability, (ii) prescribing gap patterns is a parity-blocked tuple-type
lower bound, (iii) Shiu-string site densities (2q)^{-exp(Cm)} are circular
at the needed depth. Assessment of what this paper's machinery can and
cannot supply:

1. What it CAN supply unconditionally -- exact skeleton confinement. The
   genuinely strongest deliverable here is Corollary 4.2 / (6.8) + the
   b(W) congruence (p. 25): for every n == b(W) in (N, 2N], the ENTIRE
   prime word of the window (n + x, n + y] is confined to a freely
   prescribed K-site skeleton n + H, K up to log x (4.7), with y - x
   \asymp x log x log_3 x/log_2 x (4.1). This is an exact, deterministic,
   upper-bound-type statement (everything off-skeleton is composite by
   CRT), obtained WITHOUT Shiu-type density losses -- so blocker (iii) does
   not apply to the confinement half. Since x \asymp f_1(N^eta) <= eta
   log N (p. 24), the capacity K <= log x \asymp log_2 N far exceeds the
   needed word depth ~ log_2 log(site scale). If an exchange argument can
   be reformulated to need only "primes occur nowhere except at these
   prescribed offsets", Section 4 is a real unconditional supply line, and
   Lemma 6.3 even lets one build the skeleton with exactly repeated
   difference patterns in two separated subintervals (its only structural
   tax: all pairwise differences must be x-smooth, and sites sit in
   subintervals of width x/log x).

2. What it CANNOT supply -- occupancy control, hence no matched words. The
   prime half of the word is delivered only by Theorem 5.4 (+ 5.5): at
   least a + 1 of 4a + 1 blocks (theta = 1/2, a = 1: 2 of 5) contain
   >= 1 prime. Which blocks, and which skeleton sites inside a block, is
   pigeonholed ("a single pair i_1 < i_2 ... for arbitrarily large N",
   p. 25) -- precisely blocker (i) reappearing at the block level. Exact
   occupancy prescription (all sites of a block prime, or a specified
   occupancy pattern = a specified gap word) would be a tuple-type lower
   bound, which the machinery deliberately never attempts -- consistent
   with blocker (ii); the paper's product only ever asserts "#(P cap
   n + H_i) >= 1" (Theorem 5.4). Consequently the paper cannot produce two
   sites with MATCHED J-prefix and K-suffix gap words: even at a single
   site the realized word inside (n + x, n + y] is undetermined beyond
   membership in the skeleton's difference semigroup.

3. Middle-difference supply is asymptotic, not exact. What recurs
   infinitely often is p_{t+1} - p_t = (alpha_j - alpha_i + o(1)) C L_eta
   f_2(x) (p. 25) -- a multiplicative (1 + o(1)) at a scale f_2(x) that
   tends to infinity. The absolute error o(f_2(x)) is unbounded, so two
   sites produced by the theorem never have provably EQUAL middle gaps,
   only asymptotically proportional ones. An exchange configuration
   requiring exact integer equality of prefix/suffix words with an exactly
   quantified middle difference cannot be extracted from limit-point
   statements of this shape. Conversely, if the exchange argument can
   tolerate (1 + o(1))-matched middles at a common divergent scale with
   uncontrolled surroundings, Theorem 6.2 supplies pairs (indeed infinite
   families) of such sites at ANY reasonable scale from log_6 T up to
   o(R(T) log_3 T) (Section 6; p. 2 examples), 25% of target values
   unconditionally.

4. Depth mismatch for chains. The chain version (Theorem 6.4) is the
   closest object to a "gap word": a consecutive normalized gaps
   simultaneously close to a prescribed difference vector. But a is a
   fixed constant (a >= 2), the Maynard-Tao K explodes like
   e^{aM^2/(delta(M-1))} (p. 21), and no a = a(x) -> infty version is
   stated. The consuming target depth J, K ~ log_2 log x is a growing
   depth; nothing in this paper controls words of growing length. (The
   skeleton-confinement half DOES scale to K ~ log x sites; it is the
   occupancy half that is stuck at constant depth.)

5. Site density. The good sites n live in (N, 2N] cap b(W) with W =
   prod_{p <= f_1(N^eta), p notin Z} p = e^{(1 + o(1)) f_1(N^eta)}, and
   the paper proves existence (S > 0, p. 22), not a positive density of
   good n within the progression. So this machinery gives no usable count
   of exchange-candidate sites per dyadic block -- for a summability-driven
   argument (weights 2^{-n} in S = sum p_n/2^n) one gets "infinitely many
   scales N", with no control over which scales, since the o(1)'s and the
   pigeonholed pair only stabilize along an unspecified subsequence.

6. Net assessment against the target. Toward the exchange configuration
   this paper contributes: (a) an unconditional, non-circular skeleton-
   confinement primitive at depth up to K ~ log x sites with prescribable
   geometry (Cor 4.2, Lemma 6.3, (6.8)) -- the strongest known-to-this-
   paper substitute for Shiu strings, free of blocker (iii); (b) an
   unconditional recurrence of prescribed-size middles at every reasonable
   divergent scale (Theorem 6.2, Table 1). It does NOT contribute: exact
   gap words, matched prefix/suffix windows, occupancy patterns (parity,
   blocker (ii)), growing-depth chains, or site densities; and its own
   selection step inherits pigeonhole blindness (blocker (i)) in the form
   "there exists a single pair i_1 < i_2 ... for arbitrarily large N"
   (p. 25). The scales it serves (f -> infty) also sit above the bounded-
   gap regime that dominates the binary-weighted tail of S; nothing here
   addresses gaps of bounded size (Maynard-Tao is used only through block
   occupancy, not through bounded-gap conclusions).
