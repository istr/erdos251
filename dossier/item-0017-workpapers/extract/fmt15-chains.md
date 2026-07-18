# EXTRACTION: Ford, Maynard, Tao, "Chains of large gaps between primes"

Source (only evidence base): /home/istr/pro/erdos251/dossier/1511.04468v1.pdf
arXiv:1511.04468v1 [math.NT] 13 Nov 2015. Authors as printed: KEVIN FORD,
JAMES MAYNARD, AND TERENCE TAO. 16 pages (printed pages 1-16; PDF page =
printed page). Affiliations (p. 16): Ford - Univ. of Illinois at
Urbana-Champaign; Maynard - Mathematical Institute, Oxford; Tao - UCLA.

Transcription conventions: ASCII only. Diacritics transliterated (Erdos,
Cramer, Schonhage, Westzynthius, Montreal). Math in LaTeX-like ASCII:
<= , >= , << and >> (Vinogradov), \asymp (X \asymp Y means X << Y << X),
~ (X ~ Y means X = (1+o(1))Y), O_{<=}(Y) means |error| <= Y (implied
constant 1, the paper's O_{<=} convention, Section 1.2). Iterated logs
follow the paper's footnote 1: log_2 x := log log x, log_3 x :=
log log log x, log_4 x := log log log log x. [z] := {n in N : 1 <= n <= z}
(Section 1.2). P(x) = product of primes up to x. vec(a) = (a_s mod s)_{s in
S} and vec(n) = (n_p mod p)_{p in P} denote the arrowed (vector-valued)
random tuples of the paper; boldface random variables are rendered plain
(z, N, n_p, ntilde_p, e_p, a). floor(.) = floor brackets. Anchors are
theorem/equation/section numbers; page numbers secondary. Everything up to
the final section is EXTRACTION (what the paper says); assessment appears
ONLY in the final marked COMMENTARY section. Paraphrase is marked
[PARAPHRASE].

---

## 1. ABSTRACT AND MAIN THEOREM (verbatim)

Abstract (p. 1), verbatim:

> "Let p_n denote the n-th prime, and for any k >= 1 and sufficiently
> large X, define the quantity
>   G_k(X) := max_{p_{n+k} <= X} min(p_{n+1} - p_n, ..., p_{n+k} - p_{n+k-1}),
> which measures the occurrence of chains of k consecutive large gaps of
> primes. Recently, with Green and Konyagin, the authors showed that
>   G_1(X) >> (log X log log X log log log log X) / (log log log X)
> for sufficiently large X. In this note, we combine the arguments in that
> paper with the Maier matrix method to show that
>   G_k(X) >> (1/k^2) (log X log log X log log log log X) / (log log log X)
> for any fixed k and sufficiently large X. The implied constant is
> effective and independent of k."

Main theorem (Theorem 1, Section 1, p. 2), verbatim:

> "Theorem 1. Let k >= 1 be fixed. Then for sufficiently large X, we have
>   G_k(X) >> (1/k^2) (log X log_2 X log_4 X) / (log_3 X).
> The implied constant is absolute and effective."

Definition restated in the introduction (Section 1, p. 1), verbatim:

> "Let p_n denote the n-th prime, and for any k >= 1 and sufficiently
> large X, let
>   G_k(X) := max_{p_{n+k} <= X} min(p_{n+1} - p_n, ..., p_{n+k} - p_{n+k-1}),
> denote the maximum gap between k consecutive primes less than X."

[PARAPHRASE note: the min runs over the k gaps among the k+1 consecutive
primes p_n, ..., p_{n+k}; so Theorem 1 produces k+1 consecutive primes
below X whose k intervening gaps are ALL >= c (1/k^2) log X log_2 X
log_4 X / log_3 X.]

Uniformity in k, as stated: the implied constant is "absolute and
effective" (Theorem 1, p. 2) and "effective and independent of k"
(abstract, p. 1); but the range of validity is "Let k >= 1 be fixed. Then
for sufficiently large X" (Theorem 1) and, in the introduction (p. 2):
"Now we turn to G_k(X) in the regime where k >= 1 is fixed, and X assumed
sufficiently large depending on k." NO version with k growing as a
function of X is stated anywhere in the paper (NOT FOUND in this text).

---

## 2. CONTEXT LADDER (verbatim, Section 1, p. 2)

> "The best lower bound currently is
>   G_1(X) >> (log X log_2 X log_4 X)/(log_3 X),
> for sufficiently large X and an effective implied constant, due to [11]."

> "This result may be compared against the conjecture G_1(X) \asymp
> log^2 X of Cramer [7] (see also [13]), or the upper bound G_1(X) <<
> X^{0.525} of Baker-Harman-Pintz [3], which can be improved to G_1(X) <<
> X^{1/2} log X on the Riemann hypothesis [6]."

> "Clearly G_k(X) <= G_1(X), and a naive extension of the probabilistic
> heuristics of Cramer [7] suggest that G_k(X) \asymp (1/k) log^2 X as
> X -> infty. The first non-trivial bound on G_k(X) for k >= 2 was by
> Erdos [9], who showed that
>   G_2(X)/log X -> infty
> as X -> infty. Using what is now known as the Maier matrix method,
> together with the arguments of Rankin [22] on G_1(X), Maier [14] showed
> that
>   G_k(X) >>_k (log X log_2 X log_4 X)/(log_3 X)^2
> for any fixed k >= 1 and a sequence of X going to infinity. Recently, by
> modifying Maier's arguments and using the more recent work on G_1(X) in
> [10], [18], this was improved by Pintz [19] to show that
>   G_k(X) / ( (log X log_2 X log_4 X)/(log_3 X)^2 ) -> infty
> for a sequence of X going to infinity."

Note the conjectured truth scales like 1/k while Theorem 1 gives 1/k^2.
The paper's own explanation (Section 1, p. 2), verbatim:

> "The intuitive reason for the 1/k^2 factor is that our method produces,
> roughly speaking, k primes distributed "randomly" inside an interval of
> length about (log X log_2 X log_4 X)/(log_3 X), and the narrowest gap
> between k independently chosen numbers in an interval of length L is
> typically of length about (1/k^2) L."

Siegel-zero removal and effectivity (Section 1, p. 2), verbatim:

> "Maier's original argument required one to avoid Siegel zeroes, which
> restricted his results to a sequence of X going to infinity, rather than
> all sufficiently large X. However, it is possible to modify his argument
> to remove the effect of any exceptional zeroes, which allows us to
> extend the result to all sufficiently large X and also to make the
> implied constant effective."

Relation to the long-gaps paper [11] (Ford-Green-Konyagin-Maynard-Tao,
"Long gaps between primes") (Section 1, p. 2), verbatim:

> "Our argument is based heavily on our previous paper [11], in particular
> using the hypergraph covering lemma from [11, Corollary 3] and the
> construction of sieve weights from [11, Theorem 5]. The main difference
> is in refining the probabilistic analysis in [11] to obtain good upper
> and lower bounds for certain sifted sets arising in the arguments in
> [11], whereas in the former paper only upper bounds were obtained."

Adjacent-work remark (Section 1, p. 3), verbatim:

> "We remark that in the recent paper [2], the methods from [11] were
> modified to obtain some information about the limit points of tuples of
> k consecutive prime gaps normalized by factors slightly slower than
> (log X log_2 X log_4 X)/(log_3 X); see Theorem 6.4 of that paper for a
> precise statement."

[Reference [2] = R. C. Baker, T. Freiberg, "Limit points and long gaps
between primes", preprint (p. 16).]

---

## 3. SIEGEL ZEROES (Section 2, pp. 4-5): effectivity apparatus

[PARAPHRASE of roles; key statements quoted.] To keep everything
effective, the paper avoids Siegel's theorem and Bombieri-Vinogradov
("we will not rely on ineffective results such as Siegel's theorem",
Section 1.2, p. 3) and instead uses the Landau-Page theorem.

Lemma 2.1 (Landau-Page theorem, p. 4), verbatim (statement head):

> "Let Q >= 100. Suppose that L(s, chi) = 0 for some primitive character
> chi of modulus at most Q, and some s = sigma + it. Then either
>   1 - sigma >> 1/log(Q(1+|t|)),
> or else t = 0 and chi is a quadratic character chi_Q, which is unique
> for any given Q. Furthermore, if chi_Q exists, then its conductor q_Q is
> square-free apart from a factor of at most 4, and obeys the lower bound
>   q_Q >> (log^2 Q)/(log_2^2 Q)."

Corollary 1 (p. 5), verbatim:

> "Let Q >= 100. Then there exists a quantity B_Q which is either equal to
> 1 or is a prime of size
>   B_Q >> log_2 Q
> with the property that
>   1 - sigma >> 1/log(Q(1+|t|))
> whenever L(sigma + it, chi) = 0 and chi is a character of modulus at
> most Q and coprime to B_Q."

Lemma 2.2 (Gallagher's prime number theorem, p. 5), verbatim:

> "Let q be a natural number, and suppose that L(s, chi) != 0 for all
> characters chi of modulus q and s with 1 - sigma <= delta/log(Q(1+it)),
> and some constant delta > 0. Then there is a constant D >= 1 depending
> only on delta such that
>   #{p prime : p <= x; p == a (mod q)} >> x/(phi(q) log x)
> for all (a, q) = 1 and x >= q^D."

[PRINTED-ODDITY: the hypothesis of Lemma 2.2 writes "log(Q(1+it))" with
capital Q although the modulus is q; transcribed as printed.]

The exceptional prime B_0 (later B_Q with Q = P(x)) is deleted from all
prime sets in the construction; "This will combine well with Corollary 1
once we remove the moduli divisible by the (possible) exceptional prime
B_Q." (p. 5).

---

## 4. THE KEY SIEVING RESULT AND THE MAIER MATRIX STEP (Section 3, pp. 5-8)

This is the heart of the chain mechanism (focus questions 2-4).

### 4.1 Theorem 2 (Sieving an interval), verbatim (pp. 5-6)

> "Theorem 2 (Sieving an interval). There is an absolute constants c > 0
> such that the following holds. Fix A >= 1 and epsilon > 0, and let x be
> sufficiently large depending on A and epsilon. Suppose y satisfies
> (3.1)   y = c (x log x log_3 x)/(log_2 x),
> and suppose that B_0 = 1 or that B_0 is a prime satisfying
>   log x << B_0 <= x.
> Then one can find a congruence class a_p mod p for each prime p <= x,
> p != B_0 such that the sieved set
>   T := {n in [y]\[x] : n !== a_p (mod p) for all p <= x, p != B_0}
> obeys the following size estimates:
>   - (Upper Bound) One has
> (3.2)   #T << A x/log x.
>   - (Lower Bound) One has
> (3.3)   #T >> A x/log x.
>   - (Upper bound in short intervals) For any 0 <= alpha <= beta <= 1,
>     one has
> (3.4)   #(T cap [alpha y, beta y]) << A(|beta - alpha| + epsilon) x/log x."

[PRINTED-ODDITY: "There is an absolute constants c > 0" as printed.]

Follow-up remark (p. 6), verbatim:

> "We remark that if one lowers y to be of order (x log x log_3 x)/
> (log_2 x)^2 rather than (x log x log_3 x)/(log_2 x), then this theorem
> is essentially [14, Lemma 6]. It is convenient to sieve [y]\[x] instead
> of [y] for minor technical reasons (we will use the fact that the
> residue class 0 mod p avoids all the primes in [y]\[x] whenever p <= x).
> The arguments in [11] already can give much of this theorem, with the
> exception of the lower bound (3.3), which is the main additional
> technical result of this paper that is needed to extend the results of
> that paper to longer chains."

### 4.2 Lemma 3.1 (the z-ensemble prime counts), verbatim (p. 6)

Setup sentence (p. 6): "We will prove Theorem 2 in later sections. In this
section, we show how this theorem implies Theorem 1. Here we shall use the
Maier matrix method, following the arguments in [14] closely (although we
will use probabilistic notation rather than matrix notation). Let k >= 1
be a fixed integer, let c_0 > 0 be a small constant, and let A >= 1 and
0 < epsilon < 1/2 be large and small quantities depending on k to be
chosen later."

> "Lemma 3.1. There exists an absolute constant D >= 1 such that, for all
> sufficiently large x, there exists a natural number B_0 which is either
> equal to 1 or a prime, with
> (3.5)   log x << B_0 <= x,
> and is such that the following holds. If one sets P := P(x)/B_0 (where
> we recall that P(x) is the product of the primes up to x), then one has
> (3.6)   #{z in [Z] : Pz + a prime} >> (log x/log Z) Z
> for all Z >= P^D and a in P coprime to P, and
> (3.7)   #{z in [Z] : Pz + a, Pz + b both prime} << (log x/log Z)^2 Z
> for all Z >= P^D and all distinct a, b in [P] coprime to P."

[TRANSCRIPTION-UNSURE: in the range condition of (3.6) the text layer
reads "a in P coprime to P" where (3.7) reads "a, b in [P]"; the intended
reading of (3.6) is presumably a in [P] (the interval), and the bracket
glyph is not clearly resolvable at this size.]

Proof inputs [PARAPHRASE]: (3.6) from Corollary 1 with Q := P(x) plus
Gallagher (Lemma 2.2) plus Mertens ((3.8): P/phi(P) \asymp log x, p. 7);
(3.7) "follows from standard upper bound sieves (cf. [14, Lemma 3])"
(p. 7, verbatim fragment). Only an UPPER bound is available for the
two-point count (3.7).

### 4.3 The Maier matrix derivation of Theorem 1, verbatim (p. 7)

> "Now set Z := P^D with x and D as in Lemma 3.1, and let z be chosen
> uniformly at random from [Z]. Let y, T and a_p mod p be as in Theorem 2.
> By the Chinese remainder theorem, we may find m in [P] such that
> m == -a_p (mod p) for all p <= x with p != B_0. Thus, zP + m + T consists
> precisely of those elements of zP + m + [y]\[x] that are coprime to P.
> In particular, any primes that lie in the interval zP + m + [y]\[x] lie
> in zP + m + T."

> "From (3.6) and Mertens' theorem we have
>   P(zP + m + a prime) >> (log x)/x
> for all a in T (we allow implied constants to depend on D). Similarly,
> from (3.7) and Mertens' theorem we have
> (3.9)   P(zP + m + a, zP(x) + m + b both prime) << ((log x)/x)^2
> for any distinct a, b in T."

[PRINTED-ODDITY: (3.9) writes "zP(x) + m + b" mixing P and P(x);
transcribed as printed.]

> "If we let N denote the number of primes in zP + m + T (or equivalently,
> in zP + m + [y]\[x]), we thus have from (3.2) and (3.3) that
>   E N >> A
> and
>   E N^2 << A^2.
> From this we see that with probability >> 1, we have
> (3.10)   A << N << A,
> where all implied constants are independent of epsilon and A. (This is
> because the contribution to E N when N is much larger than A is much
> smaller than A.)"

> "Next, if 0 <= alpha <= beta <= 1 and beta - alpha <= 2 epsilon, then
> from (3.9), (3.4) and the union bound we see that the probability that
> there are at least two primes in zP + m + [alpha y, beta y] is at most
>   O( (A epsilon x/log x)^2 ((log x)/x)^2 ) = O(A^2 epsilon^2).
> Note that one can cover [0,1] with O(1/epsilon) intervals of length at
> most 2 epsilon, with the property that any two elements a, b of [0,1]
> with |a - b| <= epsilon may be covered by at least one of these
> intervals. From this and the union bound, we see that the probability
> that zP + m + [y]\[x] contains two primes separated by at most
> epsilon y is bounded by O((1/epsilon) A^2 epsilon^2) = O(A^2 epsilon).
> In particular, if we choose epsilon to be a sufficiently small multiple
> of 1/A^2, we may find z in [Z] such that the interval zP + m + [y]\[x]
> contains >> A primes and has no prime gap less than epsilon y. If we
> choose A to be a sufficiently large multiple of k, we conclude that
>   G_k(ZP + m + y) >= epsilon y >> (1/k^2) y."

> "By Mertens' theorem, we have ZP + m + y << exp(O(x)), and Theorem 1
> then follows from (3.1)."

(p. 8, first line, verbatim, closing Section 3): "It remains to prove
Theorem 2. This is the objective of the remaining sections of the paper."

[PARAPHRASE summary of the mechanism: the chain of k large gaps is
obtained NOT by prescribing individual gaps but by (i) deterministically
sieving the template window [y]\[x] so the surviving set T has size
\asymp A x/log x AND is spread out ((3.4): no subwindow of length
epsilon y carries more than O(A epsilon x/log x) survivors); (ii)
translating by zP + m so that ALL primes of the translated window lie
inside the translated template; (iii) first/second-moment counting over
random z to get N \asymp A primes; (iv) a union bound killing any pair of
primes closer than epsilon y \asymp y/A^2. With A \asymp k and >> A >= k+1
primes in the window, some k+1 consecutive primes lie strictly inside it
and all k of their gaps are >= epsilon y.]

---

## 5. REDUCTION TO SIEVING PRIMES (Section 4, pp. 8-9)

Opening (p. 8), verbatim:

> "Theorem 2 concerns the problem of deterministically sieving an interval
> [y]\[x] of size (3.1) so that the sifted set T has certain size
> properties. We use a variant of the Erdos-Rankin method to reduce this
> problem to a problem of probabilistically sieving a set Q of primes in
> [y]\[x], rather than integers in [y]\[x]."

Definitions (p. 8), verbatim:

> "(4.1)   z := x^{log_3 x/(4 log_2 x)},
> and introduce the three disjoint sets of primes
> (4.2)   S := {s prime : log^{20} x < s <= z; s != B_0},
> (4.3)   P := {p prime : x/2 < p <= x; p != B_0},
> (4.4)   Q := {q prime : x < q <= y; q != B_0}.
> For residue classes vec(a) = (a_s mod s)_{s in S} and vec(n) =
> (n_p mod p)_{p in P}, define the sifted sets
>   S(vec(a)) := {n in Z : n !== a_s (mod s) for all s in S}
> and likewise
>   S(vec(n)) := {n in Z : n !== n_p (mod p) for all p in P}."

Theorem 3 (Sieving primes) (p. 8), verbatim:

> "Theorem 3 (Sieving primes). Let A >= 1 be a real number, let x be
> sufficiently large depending on A, and suppose that y obeys (3.1). Let
> B_0 be a natural number. Then there is a quantity
> (4.5)   A' \asymp A,
> and some way to choose the vectors vec(a) = (a_s mod s)_{s in S} and
> vec(n) = (n_p mod p)_{p in P} at random (not necessarily independent of
> each other), such that for any fixed 0 <= alpha < beta <= 1 (independent
> of x), one has with probability 1 - o(1) that
> (4.6)   #(Q cap S(vec(a)) cap S(vec(n)) cap (alpha y, beta y])
>           ~ A' |beta - alpha| x/log x.
> The o(1) decay rates in the probability error and implied in the ~
> notation are allowed to depend on A, alpha, beta."

Novelty sentence (p. 8), verbatim:

> "In [11, Theorem 2], a weaker version of this theorem was established in
> which B_0 was not present, and only the upper bound in (4.6) was proven.
> Thus, the main new contribution of this paper is the lower bound in
> (4.6)."

Derivation of Theorem 2 from Theorem 3 [PARAPHRASE with verbatim
fragments] (pp. 8-9): partition (0,1] into O(1/epsilon) intervals of
length between epsilon/2 and epsilon; apply Theorem 3 to each and to
(0,1); union bound; extend vec(a) to all p <= x by "setting a_p := n_p for
p in P and a_p := 0 for p not in S cup P" (p. 9, verbatim fragment); then

> "The elements of T, by construction, are not divisible by any prime in
> (0, log^{20} x] or in (z, x/2], except possibly for B_0. Thus, each
> element must either be a z-smooth number (i.e. a number with all prime
> factors at most z) times a power of B_0, or must consist of a prime
> greater than x/2, possibly multiplied by some additional primes that are
> all either at least log^{20} x or equal to B_0. However, from (3.1) we
> know that y = o(x log x), and by hypothesis we know that B_0 >> log x.
> Thus, we see that an element of T is either a z-smooth number times a
> power of B_0 or a prime in Q." (p. 9, verbatim)

The z-smooth exceptional set R is negligible (p. 9, verbatim): with
u := log y/log z ~ 4 log_2 x/log_3 x,

> "#R << log x * y e^{-u log u + O(u log log (u+2))}
>     = log x * y/log^{4+o(1)} x = o(x/log x)."

"Thus the contribution of R to T is negligible for the purposes of
establishing the bounds (3.2), (3.3), (3.4), and Theorem 2 follows from
(4.6)." (p. 9, verbatim).

---

## 6. HYPERGRAPH COVERING (Section 5, pp. 9-11)

Purpose (p. 9), verbatim: "In the previous section we reduced matters to
obtaining random residue classes vec(a), vec(n) such that the sifted set
Q cap S(vec(a)) cap S(vec(n)) is small. In this section we use a
hypergraph covering theorem from [11] to reduce the task to that of
finding random residue classes vec(n) that have large intersection with
Q cap S(vec(a))."

Theorem 4 (pp. 9-10), verbatim:

> "Theorem 4. Let x -> infty. Let P', Q' be sets of primes in (x/2, x] and
> (x, x log x], respectively, with #Q' > (log_2 x)^3. For each p in P',
> let e_p be a random subset of Q' satisfying the size bound
> (5.1)   #e_p <= r = O( (log x log_3 x)/(log_2^2 x) )   (p in P').
> Assume the following:
>   - (Sparsity) For all p in P' and q in Q',
> (5.2)   P(q in e_p) <= x^{-1/2 - 1/10}.
>   - (Uniform covering) For all but at most (1/(log_2 x)^2) #Q' elements
>     q in Q', we have
> (5.3)   sum_{p in P'} P(q in e_p) = C + O_{<=}( 1/(log_2 x)^2 )
>     for some quantity C, independent of q, satisfying
> (5.4)   (5/4) log 5 <= C << 1.
> Then for any positive integer m with
> (5.5)   m <= (log_3 x)/(log 5),
> we can find random sets e'_p subseteq Q' for each p in P' such that
>   #{q in Q' : q not in e'_p for all p in P'} ~ 5^{-m} #Q'
> with probability 1 - o(1). More generally, for any Q'' subset Q' with
> cardinality at least (#Q')/sqrt(log_2 x), one has
>   #{q in Q'' : q not in e'_p for all p in P'} ~ 5^{-m} #Q''
> with probability 1 - o(1). The decay rates in the o(1) and ~ notation
> are uniform in P', Q', Q''."
> "Proof. See [11, Corollary 3]."

Theorem 5 (Random construction) (p. 10), verbatim:

> "Theorem 5 (Random construction). Let x be a sufficiently real number,
> let B_0 be a natural number and suppose y satisfies (3.1). Then there is
> a quantity C with
> (5.6)   C \asymp 1/c
> with the implied constants independent of c, and some way to choose
> random vectors vec(a) = (a_s mod s)_{s in S} and vec(n) = (n_p)_{p in P}
> of congruence classes a_s mod s and integers n_p, obeying the following
> axioms:
>   - For every vec(a) in the essential range of vec(a), one has
>       P(q == n_p (mod p) | vec(a) = vec(a)) <= x^{-1/2 - 1/10}
>     uniformly for all p in P.
>   - For fixed 0 <= alpha < beta <= 1, we have with probability 1 - o(1)
>     that
> (5.7)   #(Q cap S(vec(a)) cap [alpha y, beta y])
>           ~ 80 c |beta - alpha| (x/log x) log_2 x.
>   - Call an element vec(a) in the essential range of vec(a) good if, for
>     all but at most x/(log x log_2 x) elements q in Q cap S(vec(a)), one
>     has
> (5.8)   sum_{p in P} P(q == n_p (mod p) | vec(a) = vec(a))
>           = C + O_{<=}( 1/(log_2 x)^2 ).
>     Then vec(a) is good with probability 1 - o(1)."

[PRINTED-ODDITY: "Let x be a sufficiently real number" as printed;
evidently "sufficiently large real number" intended.]

Derivation of Theorem 3 from Theorem 5 (p. 11), verbatim:

> "We now show why Theorem 5 implies Theorem 3. By (5.6), we may choose
> 0 < c < 1/2 small enough so that (5.4) holds. Let A >= 1 be a fixed
> quantity. Then we can find an integer m obeying (5.5) such that the
> quantity
>   A' := 5^{-m} x 80 c log_2 x
> is such that A' \asymp A with implied constants independent of A."

[Here "x" in the display is the multiplication sign as printed; A' =
5^{-m} * 80 c log_2 x. Since 5^{(log_3 x)/(log 5)} = log_2 x, the
admissible range of A' spans from \asymp 1 (m maximal) up to 16 c log_2 x
(m = 1). [PARAPHRASE arithmetic, not in the paper.]]

> "Suppose that we are in the probability 1 - o(1) event that vec(a) takes
> a value vec(a) which is good and such that (5.7) holds. On each
> sub-event vec(a) = vec(a) of this probability 1 - o(1) event, we may
> apply Theorem 4 (for the random variables n_p conditioned to this event)
> define the random variables n'_p on this event with the stated
> properties. For the remaining events vec(a) = vec(a), we set n'_p
> arbitrarily (e.g. we could set n'_p = 0). The claim (4.6) then follows
> from Corollary 4 and (5.7), thus establishing Theorem 3."

[PRINTED-ODDITY: "apply Theorem 4 ... define the random variables" is
missing a "to"; and "follows from Corollary 4" refers to a Corollary 4
that does not exist in this paper - the intended reference is evidently
Theorem 4 (= [11, Corollary 3]). Transcribed as printed.]

---

## 7. THE MAYNARD-TAO SIEVE WEIGHT (Section 6, pp. 11-16)

Admissibility (p. 11), verbatim: "If r is a natural number, an admissible
r-tuple is a tuple (h_1, ..., h_r) of distinct integers h_1, ..., h_r that
do not cover all residue classes modulo p, for any prime p. For instance,
the tuple (p_{pi(r)+1}, ..., p_{pi(r)+r}) consisting of the first r primes
larger than r is an admissible r-tuple."

Theorem 6 (Existence of good sieve weight) (p. 11), verbatim:

> "Theorem 6 (Existence of good sieve weight). Let x be a sufficiently
> large real number, let B_0 be an integer, and let y be any quantity
> obeying (3.1). Let P, Q be defined by (4.3), (4.4). Let r be a positive
> integer with
> (6.1)   r_0 <= r <= log^{c_0} x
> for some sufficiently small absolute constant c_0 and sufficiently large
> absolute constant r_0, and let (h_1, ..., h_r) be an admissible r-tuple
> contained in [2 r^2]. Then one can find a positive quantity
> (6.2)   tau >= x^{-o(1)}
> and a positive quantity u = u(r) depending only on r with
> (6.3)   u \asymp log r
> and a non-negative function w : P x Z -> R^+ supported on
> P x (Z cap [-y, y]) with the following properties:
>   - Uniformly for every p in P, one has
> (6.4)   sum_{n in Z} w(p, n) = (1 + O(1/log_2^{10} x)) tau y/log^r x.
>   - Uniformly for every q in Q and i = 1, ..., r, one has
> (6.5)   sum_{p in P} w(p, q - h_i p)
>           = (1 + O(1/log_2^{10} x)) tau (u/r) x/(2 log^r x).
>   - Uniformly for every h = O(y/x) that is not equal to any of the h_i,
>     one has
> (6.6)   sum_{q in Q} sum_{p in P} w(p, q - hp)
>           = O( (1/log_2^{10} x) tau (x/log^r x) (y/log x) ).
>   - Uniformly for all p in P and n in Z,
> (6.7)   w(p, n) = O(x^{1/3 + o(1)})."
> "Proof. See [11, Theorem 5]. We remark that the construction of the
> weights and the verification of the required estimates relies heavily on
> the previous work of the second author in [17]."

Footnote 2 (p. 12), verbatim: "The integer B_0 was not deleted from the
sets P or Q in that theorem, however it is easy to see (using (6.7)) that
deleting at most one prime from either P or Q will not significantly
worsen any of the estimates claimed by the theorem."

[Reference [17] = J. Maynard, "Dense clusters of primes in subsets",
preprint (p. 16); [16] = J. Maynard, "Small gaps between primes" is in
the bibliography. The weight w is the Maynard-Tao multidimensional sieve
weight from the long-gaps paper [11].]

Parameter choice (p. 12), verbatim:

> "We set r to be the maximum value permitted by Theorem 6, namely
> (6.8)   r := floor(log^{c_0} x)
> and let (h_1, ..., h_r) be the admissible r-tuple consisting of the
> first r primes larger than r, thus h_i = p_{pi(r)+i} for i = 1, ..., r.
> From the prime number theorem we have h_i = O(r log r) for i = 1,...,r,
> and so we have h_i in [2 r^2] for i = 1, ..., r if x is large enough
> (there are many other choices possible, e.g. (h_1, ..., h_r) =
> (1^2, 3^2, ..., (2r-1)^2))."

Random residue mechanics (pp. 12-13), verbatim (in sequence):

> "For each p in P, let ntilde_p denote the random integer with
> probability density
>   P(ntilde_p = n) := w(p, n) / sum_{n' in Z} w(p, n')
> for all n in Z (we will not need to impose any independence conditions
> on the ntilde_p)."

> "(6.9)   sum_{p in P} P(q = ntilde_p + h_i p)
>            = (1 + O(1/log_2^{10} x)) (u/r) (x/2y)
> for every q in Q and i = 1, ..., r,"

> "(6.10)  sum_{q in Q} sum_{p in P} P(q = ntilde_p + hp)
>            << (1/log_2^{10} x) (x/log x)
> for every h = O(y/x) not equal to any of the h_i."

> "(6.11)  P(ntilde_p = n) << x^{-1/2 - 1/6 + o(1)}
> for all p in P and n in Z."

> "We choose the random vector vec(a) := (a_s mod s)_{s in S} by selecting
> each a_s mod s uniformly at random from Z/sZ, independently in s and
> independently of the ntilde_p. The resulting sifted set S(vec(a)) is a
> random periodic subset of Z with density
>   sigma := prod_{s in S} (1 - 1/s)."

> "sigma = (1 + O(1/log_2^{10} x)) log(log^{20} x)/log z
>        = (1 + O(1/log_2^{10} x)) (80 log_2 x)/(log x log_3 x/log_2 x),
> so in particular we see from (3.1) that
> (6.12)  sigma y = (1 + O(1/log_2^{10} x)) 80 c x log_2 x.
> We also see from (6.8) that
> (6.13)  sigma^r = x^{o(1)}."

Correlation bound (Lemma 6.1, p. 13), verbatim:

> "Lemma 6.1. Let t <= log x be a natural number, and let n_1, ..., n_t be
> distinct integers of magnitude O(x^{O(1)}). Then one has
>   P(n_1, ..., n_t in S(vec(a))) = (1 + O(1/log^{16} x)) sigma^t.
> Proof. See [11, Lemma 5.1]."

Corollary 2 (p. 13), verbatim:

> "Corollary 2. For any fixed 0 <= alpha < beta <= 1, we have with
> probability 1 - o(1) that
> (6.14)  #(Q cap [alpha y, beta y] cap S(vec(a)))
>           ~ sigma |beta - alpha| y/log x
>           ~ 80 c |beta - alpha| (x/log x) log_2 x.
> Proof. See [11, Corollary 4], replacing Q with Q cap [alpha y, beta y]."

Conditioned residue classes (p. 13), verbatim:

> "(6.15)  X_p(vec(a)) := P(ntilde_p + h_i p in S(vec(a)) for all
>            i = 1, ..., r),
> and let P(vec(a)) denote the set of all the primes p in P such that
> (6.16)  X_p(vec(a)) = (1 + O_{<=}(1/log^3 x)) sigma^r."

> "We now define the random variables n_p as follows. Suppose we are in
> the event vec(a) = vec(a) for some vec(a) in the range of vec(a). If
> p in P\P(vec(a)), we set n_p = 0. Otherwise, if p in P(vec(a)), we
> define n_p to be the random integer with conditional probability
> distribution
> (6.17)  P(n_p = n | vec(a) = vec(a)) := Z_p(vec(a); n)/X_p(vec(a)),
>         Z_p(vec(a); n) = 1_{n + h_j p in S(vec(a)) for j = 1,...,r}
>           P(ntilde_p = n).
> with the n_p jointly conditionally independent on the event vec(a) =
> vec(a)."

[PARAPHRASE: so the random residue class n_p mod p is drawn with density
proportional to the Maynard-Tao weight w(p, .), CONDITIONED on the event
that all r translates n_p + h_j p survive the small-prime sieve
S(vec(a)). Each p in P thereby "covers" (with its residue class mod p) up
to r primes q = n_p + h_i p of Q; (6.9) and (6.5) say each q in Q is
covered with nearly equal total probability - the uniform-covering
hypothesis (5.3)/(5.8) that the hypergraph covering theorem needs.]

Verification lemmas (pp. 14-16) [statements verbatim, proofs paraphrased]:

> "Lemma 6.2. With probability 1 - O(1/log^3 x), P(vec(a)) contains all
> but O( (1/log^3 x)(x/log x) ) of the primes p in P. In particular,
> E #P(vec(a)) = #P (1 + O(1/log^3 x)). Proof. See [11, Lemma 5.3]."
(p. 14)

> "Lemma 6.3. With probability 1 - o(1) we have
> (6.19)  sigma^{-r} sum_{p in P(vec(a))} sum_{h << y/x, h not in
>           {h_1,...,h_r}} Z_p(vec(a); q - hp) << 1/log_2^3 x
> for all but at most x/(2 log x log_2 x) primes q in Q cap S(vec(a))."
(p. 14)

> "Lemma 6.4. With probability 1 - o(1), we have
> (6.21)  sigma^{-r} sum_{i=1}^r sum_{p in P(vec(a))}
>           Z_p(vec(a); q - h_i p)
>           = (1 + O(1/log_2^3 x)) (u/sigma) (x/2y)
> for all but at most x/(2 log x log_2 x) of the primes q in
> Q cap S(vec(a))."
(pp. 14-15)

[PARAPHRASE of proofs: Lemma 6.3 by Markov from the expectation bound
(6.20) (the r+1 integers q, q + h_1 p - hp, ..., q + h_r p - hp are
distinct, so Lemma 6.1 applies, then (6.10)); Lemma 6.4 by a first/second
moment computation over q ((6.22), (6.23)), using independent copies
(ntilde^(1)), (ntilde^(2)) and Chebyshev (Lemma 1.1): "the number of bad q
is << (sigma y/log x)(1/log_2^3 x) << x/(log x log_2^2 x) with probability
1 - O(1/log_2 x)" (p. 16, verbatim). TRANSCRIPTION note: in the display
(6.20) the excluded set is printed "{h_1, ..., h_k}" with subscript k
although r is meant [PRINTED-ODDITY]; also "susbtitute" on p. 15 as
printed.]

Conclusion of Theorem 5 (p. 16), verbatim:

> "We now conclude the proof of Theorem 5. We need to prove (6.18); this
> follows immediately from Lemma 6.3 and Lemma 6.4 upon noting that by
> (6.8), (6.3) and (6.12),
>   C := (u/sigma) (x/2y) ~ 1/c."

where (6.18) (p. 14), verbatim:

> "(6.18)  sigma^{-r} sum_{p in P(vec(a))} sum_h Z_p(vec(a); q - hp)
>            = C + O(1/log_2^3 x)."

---

## 8. WHAT IS CONTROLLED AT THE BOUNDARY OF THE CHAIN (focus 3)

Exhaustive check [PARAPHRASE with the load-bearing quotes above]:

1. The sieve template T lives ONLY in [y]\[x] (Theorem 2, p. 6: "T :=
   {n in [y]\[x] : ...}"). Nothing is sieved or counted in [x] (the low
   part) or above y.
2. All control is on primes INSIDE the translated window: "any primes
   that lie in the interval zP + m + [y]\[x] lie in zP + m + T" (p. 7)
   and "the interval zP + m + [y]\[x] contains >> A primes and has no
   prime gap less than epsilon y" (p. 7). "No prime gap less than
   epsilon y" refers to gaps between consecutive primes both lying in the
   window; the chain of k gaps is chosen among k+1 consecutive primes
   inside the window (possible since >> A >= k+1).
3. There is NO statement anywhere in the paper about: the gap between the
   last prime below zP + m + x and the first prime in the window; the gap
   between the last prime in the window and the first prime above
   zP + m + y; or the primes in zP + m + [x]. NOT FOUND in this text.
   The flanking gaps of the constructed block are completely
   uncontrolled: they can a priori be of any size >= 1 (below) and >= 1
   (above); the construction gives no lower or upper bound on them.
4. The only sub-window information inside the block is the count control:
   (3.4) (upper bound on T in [alpha y, beta y]) and (4.6)/(5.7)/(6.14)
   (two-sided asymptotic counts of sieve survivors / surviving primes of
   Q in sub-windows). There is no control of WHICH survivors are prime in
   a given sub-window, only first/second moments ((3.6), (3.7), (3.9),
   E N, E N^2).

---

## 9. SCALES AND LOCATION OF THE CHAIN (focus 4)

[PARAPHRASE, all anchors quoted above.]

- Internal scale: x -> infty is the sieving parameter; the window has
  length y - x ~ y with y = c x log x log_3 x/log_2 x ((3.1), p. 5).
- The site: the chain lives inside zP + m + [y]\[x], where P = P(x)/B_0
  (product of primes up to x, divided by the possible exceptional prime
  B_0, Lemma 3.1, p. 6), m in [P] is FIXED by the Chinese remainder
  theorem from the sieve residues (m == -a_p (mod p) for all p <= x,
  p != B_0; p. 7), and z is drawn uniformly at random from [Z] with
  Z := P^D, D >= 1 the absolute constant of Lemma 3.1/Lemma 2.2.
- Height: "By Mertens' theorem, we have ZP + m + y << exp(O(x))" (p. 8);
  so given a target X one takes x \asymp log X, converting y into
  (1/k^2) log X log_2 X log_4 X/log_3 X.
- Freedom in placement: the good event (3.10) plus the no-close-pair
  event has probability >> 1 minus O(A^2 epsilon) (p. 7), i.e. a
  positive proportion of z in [Z] produce a chain site. So the
  construction yields >> Z sites of the prescribed form zP + m +
  [y]\[x], all congruent to the same m modulo P and all sharing the SAME
  deterministic template T. There is no mechanism in the paper to place a
  site near a prescribed location beyond (a) choosing x (hence the height
  scale exp(O(x))) and (b) choosing among the good z in [Z]; which z are
  good is not identified, only counted. The result holds for ALL
  sufficiently large X (not just a sequence), precisely because the
  Siegel-zero obstruction was removed via B_0 (Section 1, p. 2, quoted in
  Part 2; Section 2).
- Dependence chain of parameters (p. 6): "Let k >= 1 be a fixed integer,
  let c_0 > 0 be a small constant, and let A >= 1 and 0 < epsilon < 1/2
  be large and small quantities depending on k to be chosen later"; then
  A = large multiple of k, epsilon = small multiple of 1/A^2 (p. 7), and
  Theorem 2 needs "x sufficiently large depending on A and epsilon"
  (p. 5). Theorem 3's o(1) rates "are allowed to depend on A, alpha,
  beta" (p. 8), and its alpha, beta must be "fixed ... (independent of
  x)" (p. 8). This is where the fixed-k restriction enters: no rate in
  k is quantified anywhere. NOT FOUND: any explicit admissible growth
  k = k(X).

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

1. What it supplies unconditionally. For every FIXED k and all
   sufficiently large X (threshold depending on k), a block of k+1
   consecutive primes below X whose k gaps are ALL >=
   c (1/k^2) log X log_2 X log_4 X/log_3 X, with c absolute and effective
   (Theorem 1, p. 2; abstract). This is a supply of "all-gaps-large"
   words of constant length - a one-sided largeness pattern, not a
   prescribed word. The gap sizes are pinned only from below (>=
   epsilon y) and collectively from above (they sum to < y); relative
   sizes within the block are uncontrolled (Section 4.3 above, p. 7
   derivation). So a "dominant weighted middle difference" cannot be
   prescribed inside one block by this construction as it stands.

2. Depth. The exchange configuration needs depth J, K ~ log_2 log(site
   height). FMT's Theorem 1 is stated for fixed k only ("Let k >= 1 be
   fixed", Theorem 1; "x sufficiently large depending on A and epsilon",
   Theorem 2; unquantified o(1) rates depending on A in Theorem 3).
   Even pushing the internal parameters optimistically: the hypergraph
   covering step caps the survivor scaling at A' = 5^{-m} * 80 c log_2 x
   with 1 <= m <= log_3 x/log 5 (p. 11 and (5.5)), so A (hence k) can be
   at most \asymp log_2 x = log log x in the INTERNAL variable x. Since
   the site height is H << exp(O(x)) (p. 8), i.e. x \asymp log H, this
   internal cap translates to k << log log log H = log_3 H, whereas the
   target depth is ~ log log H = log_2 H. The machinery is therefore one
   exponential short of the required depth even heuristically, and the
   PAPER only claims fixed k. It cannot supply exchange-depth chains.

3. Matched windows / two-site supply. The construction has one genuinely
   interesting multi-site feature: a positive proportion of z in [Z],
   Z = P^D, produce chain sites zP + m + [y]\[x] (p. 7, probability >> 1
   after choosing epsilon \asymp 1/A^2), and ALL these sites share the
   same deterministic template T and the same residue m mod P (Section 9
   above). So the SUPPORT of the prime pattern (the set of positions that
   can be prime) is exactly matched across >> Z sites - polynomially many
   sites in the height H \asymp P^{D+1}, vastly denser than
   Shiu-string-type site densities (blocker (iii)) FOR THIS COARSE word
   class. But the realized primality pattern inside T varies with z, and
   the paper controls it only by first moments ((3.6)), pair UPPER bounds
   ((3.7), (3.9)), and the resulting second-moment count (3.10). To force
   two sites to realize the SAME J-prefix/K-suffix gap word one would
   need LOWER bounds on prime-tuple correlations across the z-ensemble at
   prescribed offset patterns - exactly the parity-blocked tuple-type
   lower bound of blocker (ii). The paper's own two-point information is
   an upper-bound sieve ((3.7): "follows from standard upper bound
   sieves", p. 7) and cannot be reversed. So: no unconditional
   matched-window supply from this machinery; it reproduces, rather than
   circumvents, blocker (ii) at the two-site level.

4. What is new here relative to blocker (i) (pigeonhole blindness). The
   paper's self-declared main technical novelty is the LOWER bound (3.3)
   and the two-sided sub-window asymptotic (4.6) ("the main new
   contribution of this paper is the lower bound in (4.6)", p. 8; "the
   main additional technical result of this paper", p. 6). This is
   variability-aware control: it certifies that sieve survivors (and the
   surviving primes of Q, (5.7)/(6.14)) EQUIDISTRIBUTE across sub-windows
   [alpha y, beta y] at the correct density, not merely that some window
   is populated. Mechanically it comes from making the Maynard-Tao weight
   cover every q in Q with nearly equal total probability ((6.5), (6.9),
   (5.8)) and feeding this uniform covering into the Pippenger-Spencer
   hypergraph covering theorem (Theorem 4), whose output is uniform over
   ALL subsets Q'' of relative density >= 1/sqrt(log_2 x) (Theorem 4,
   final clause). That "uniform over subsets" clause is the transferable
   asset: any future exchange-site argument that needs "the sieve debris
   is equidistributed over sub-windows of the construction, with
   two-sided bounds" can cite this machinery (Theorems 3-6). It is
   count-level control only, though - it does not see gap WORDS.

5. Boundary. Nothing is controlled at the flanks of the constructed block
   (Section 8 above): the gaps entering and leaving the block are
   unconstrained in both directions. Any exchange configuration built on
   FMT blocks must keep both matched windows and the weighted middle
   strictly inside a single block; the block supplies at most k \asymp A
   gaps of known one-sided size, and k is constant (point 2).

6. Placement. The site location is rigid modulo P (fixed m from CRT,
   p. 7): no freedom to prescribe WHERE a chain occurs beyond the height
   scale exp(O(x)) and the unidentified positive proportion of good
   z in [Z]. Two FMT sites cannot be steered into a prescribed relative
   position (e.g. prescribed index offset in the gap word) by anything in
   this paper.

7. Net assessment for the exchange-configuration target: this paper
   supplies (a) unconditional constant-depth all-large-gap blocks with
   effective constants at every large height, and (b) a reusable
   two-sided equidistribution engine for sieve survivors in sub-windows
   (Theorems 2-6). It does NOT supply: exchange-depth (log_2 log x)
   chains; prescribed or matched gap words; middle-difference dominance;
   flank control; or positional control. Its two-site structure (shared
   template T across >> Z translates) is the closest approach to a
   matched-window supply, but converting shared support into shared
   realized words is precisely the parity-blocked tuple lower bound
   (blocker (ii)), which this machinery does not touch. The pointer worth
   following for relative-size (dominant-middle) control is the paper's
   own remark (p. 3) to Baker-Freiberg [2, Theorem 6.4] on limit points
   of tuples of k consecutive normalized prime gaps.

---

## FLAGS (consolidated)

1. [PRINTED-ODDITY] Theorem 2 (p. 5): "There is an absolute constants
   c > 0" as printed.
2. [PRINTED-ODDITY] Theorem 5 (p. 10): "Let x be a sufficiently real
   number" as printed (evidently "sufficiently large real number").
3. [PRINTED-ODDITY] p. 11: "we may apply Theorem 4 (for the random
   variables n_p conditioned to this event) define the random variables
   n'_p" (missing "to"), and "The claim (4.6) then follows from
   Corollary 4 and (5.7)" - no Corollary 4 exists in this paper; the
   intended reference is evidently Theorem 4.
4. [PRINTED-ODDITY] (3.9) (p. 7): "zP(x) + m + b" mixes P and P(x);
   transcribed as printed.
5. [PRINTED-ODDITY] Lemma 2.2 (p. 5): hypothesis written with
   "log(Q(1+it))" although the modulus is q.
6. [PRINTED-ODDITY] (6.20) (p. 14): excluded set printed as
   "{h_1, ..., h_k}" where {h_1, ..., h_r} is meant; also "susbtitute"
   (p. 15) as printed.
7. [TRANSCRIPTION-UNSURE] (3.6) (p. 6): range condition read as "a in P
   coprime to P" from the text layer; (3.7) has "a, b in [P]", so (3.6)
   likely intends a in [P]; bracket glyph not clearly resolvable.
8. [TRANSCRIPTION-UNSURE] sigma evaluation (p. 13): denominator
   transcribed as printed, "(80 log_2 x)/(log x log_3 x/log_2 x)", i.e.
   the stacked fraction log x log_3 x/log_2 x sits entirely in the
   denominator (equivalently sigma ~ 80 (log_2 x)^2/(log x log_3 x));
   confirmed consistent with (6.12) via y = c x log x log_3 x/log_2 x.
9. [PARAPHRASE] Proofs of Lemmas 6.3 and 6.4 (pp. 14-16) are summarized;
   their statements, the displays (6.18)-(6.23) sighted, and the closing
   Chebyshev sentence (p. 16) are quoted verbatim.
10. Commentary points 2 (internal cap k << log_2 x, translation to
    log_3 H), 3 (site density), and the A'-range arithmetic after (5.5)
    are extractor arithmetic built on quoted anchors, not claims of the
    paper.
