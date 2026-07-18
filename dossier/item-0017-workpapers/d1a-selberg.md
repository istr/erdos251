# D1-L: A k-uniform Selberg-sieve upper bound with fully explicit constant

Workpaper for dossier item 0017, task D1.a. Self-contained proof; ASCII only.
Status: complete derivation. All constants explicit. No use of
Halberstam-Richert Theorem 5.1 or any black-box sieve theorem.

External inputs are ONLY: Rosser-Schoenfeld 1962 explicit Mertens/Chebyshev
bounds (listed in Section 2 with the exact inequalities used), and elementary
facts about multiplicative functions proved inline. The prime number theorem
is NOT needed anywhere below.

## 0. Statement

CONVENTION (exponent). H has k elements; a k-tuple of simultaneous primes is
counted against (ln X)^k. The consuming project realizes (L+1)-point sets by
L-gap words and counts against (ln x)^(L+1); there k = L+1, so the exponent
conventions agree: k points <-> (ln X)^k.

Let H = { h_1 < h_2 < ... < h_k } be a set of k >= 1 integers, s = h_k - h_1
its span. For a prime p let nu(p) = #{ h mod p : h in H } (number of occupied
residue classes). H is ADMISSIBLE if nu(p) <= p - 1 for every prime p.
Normalize h_1 = 0 (translating n by h_1 changes the count below by at most s,
which is absorbed into the error term; see Remark 11.3). The singular series
is

    S(H) = prod_p ( 1 - nu(p)/p ) * ( 1 - 1/p )^(-k)      (converges, Lemma 3.3).

Write N(X;H) = #{ n <= X : n + h_1, ..., n + h_k are all prime }.

THEOREM D1-L. Let gamma = 0.577216... be Euler's constant. Suppose

    (H1)  H admissible, h_1 = 0, k >= 1;
    (H2)  k <= (lnln X)^2;
    (H3)  s = h_k - h_1 <= (ln X)^2;
    (H4)  X >= X_0 := exp(exp(30))   (absolute; see Remark 11.2).

Then

    N(X;H) <= C(k) * ( 1 + err(X,k) ) * S(H) * X / (ln X)^k,

with the fully explicit constant

    C(k) = 2 * ( (8k+2) * e^(-gamma) )^k        [ = 2 * (4.4917 k + 1.1230)^k ]

and the fully explicit error term

    err(X,k) <= 20 * k^2 * lnln X / ln X   ( <= 20 (lnln X)^5 / ln X = o(1) ).

Comparison forms of the constant (Section 13):
    C(1) = 11.230;   C(k) <= (12.4)^k * k! / sqrt(k)   for k >= 2.

COROLLARY D1-L' (optimized parameters; Section 12). For k >= 5, under the
same hypotheses, C(k) may be replaced by

    C*(k) = 2e * ( 4 e^(-gamma) k )^k * e^(1.45 sqrt(k))
          <= (6.11)^k * k! * e^(1.45 sqrt(k)).

HONESTY NOTE. The classical (Halberstam-Richert) constant is 2^k k! (1+o(1)).
Our C(k) is larger by a factor which is asymptotically (2 e^(1-gamma))^k *
e^(O(sqrt k)) ~ (3.06)^k e^(O(sqrt k)) in the Corollary, and ~ (6.11)^k in the
clean Theorem. Section 13 traces exactly where each factor arises and why the
gap to 2^k k! is inherent to the self-contained (Rankin-truncation) route used
here.

## 1. Notation and standing conventions

- p always denotes a prime; ln is the natural logarithm.
- P(w) = prod_{p <= w} p.
- mu = Moebius function; omega(d) = number of distinct prime factors;
  all sieve variables d, r, m, e are positive squarefree integers.
- Pi(n) = prod_{i=1}^{k} (n + h_i).
- nu is extended multiplicatively to squarefree d: nu(d) = prod_{p|d} nu(p).
- F(d) = nu(d)/d;  g(d) = prod_{p|d} nu(p) / (p - nu(p))   (well defined for
  squarefree d by admissibility: 1 <= nu(p) <= p-1, so 0 < g(p) <= p-1).
- Level R and smoothness parameter z are fixed in Section 11:
      R = X^(1/2) * (ln X)^(-2k),   z = R^(1/u),   u = 4k + 1.
- G = sum over squarefree d < R of mu^2(d) g(d)   (the main quadratic-form sum;
  note every prime factor of d < R is < R, so no smoothness condition is
  needed at level R).
- t := lnln X  when convenient. (H2) reads k <= t^2, (H4) reads t >= 30.

## 2. External inputs (Rosser-Schoenfeld 1962, "Approximate formulas for some
##    functions of prime numbers", Illinois J. Math. 6)

With B = 0.261497... (Mertens constant):

  (RS1)  sum_{p <= x} 1/p  <  lnln x + B + 1/(2 ln^2 x)      for x > 286.
         We use it only at x = R >= 286, giving
         sum_{p < R} 1/p <= lnln R + 0.262.

  (RS2)  sum_{p <= x} (ln p)/p  <  ln x                      for x > 1.
         [R-S (3.24).]

  (RS3)  prod_{p <= x} (1 - 1/p)^(-1)  >  e^gamma (ln x) (1 - 1/(2 ln^2 x))
         for x >= 285.   [R-S Theorem 7.]

  (RS4)  theta(x) = sum_{p <= x} ln p  <  1.01624 x          for all x > 0.
         [R-S Theorem 9.]

Elementary inequalities, proved by calculus, used without further comment:

  (E1)  |ln(1-x) + x| <= x^2            for 0 <= x <= 1/2;
  (E2)  1 - x >= e^(-2x)                for 0 <= x <= 1/2;
  (E3)  (1-x)^(-1) <= e^(2x)            for 0 <= x <= 1/2;
  (E4)  e^t - 1 <= t e^t                for t >= 0;
  (E5)  k! >= (k/e)^k                   (from e^k >= k^k/k!);
  (E6)  k! >= sqrt(2 pi k) (k/e)^k      (Stirling, standard; used only for
                                         the cosmetic forms of C(k)).

## 3. Elementary lemmas on nu and S(H)

LEMMA 3.1 (values of nu).
 (a) 1 <= nu(p) <= min(k, p-1) for every p (the lower bound because the class
     -h_1 mod p is always occupied; the upper bounds by counting and by
     admissibility).
 (b) If p > s then nu(p) = k.
PROOF of (b): for i != j, 0 < |h_i - h_j| <= s < p, so p does not divide
h_i - h_j; hence the h_i are pairwise distinct mod p and occupy exactly k
classes. (In particular p >= k automatically: k distinct classes exist mod p,
so p >= k.)  []

LEMMA 3.2 (local factors far out). For p >= 2k and p > s (so nu(p) = k,
k/p <= 1/2):

    | ln( (1 - k/p) (1 - 1/p)^(-k) ) |  <=  2 k^2 / p^2.

PROOF. ln(1-k/p) = -k/p + delta_1 with |delta_1| <= (k/p)^2 by (E1);
-k ln(1-1/p) = k/p + delta_2 with |delta_2| <= k/p^2 by (E1) applied with
x = 1/p <= 1/2. Sum: |delta_1 + delta_2| <= k^2/p^2 + k/p^2 <= 2k^2/p^2.  []

LEMMA 3.3 (singular series: convergence and explicit lower bound).
S(H) converges absolutely, S(H) > 0, and

    S(H) >= e^(-2.6 k),   hence   S(H)^(-1) <= e^(3k).

PROOF. Split the defining product at 2k (and recall s-large primes have
nu = k).
 (i) p <= 2k: the factor is (1 - nu(p)/p)(1-1/p)^(-k) >= (1 - (p-1)/p) * 1
     = 1/p. Hence prod_{p <= 2k} factor >= prod_{p <= 2k} 1/p
     = e^(-theta(2k)) >= e^(-1.01624 * 2k) >= e^(-2.033 k) by (RS4).
 (ii) p > 2k: nu(p) <= k, so 1 - nu(p)/p >= 1 - k/p > 1/2 and, as in
     Lemma 3.2, ln[(1 - nu(p)/p)(1-1/p)^(-k)] >= ln(1-k/p) + k/p
     >= -(k/p)^2 by (E1). Summing, sum_{p > 2k} (k/p)^2
     <= k^2 sum_{n > 2k} n^(-2) <= k^2/(2k) = k/2.
     So prod_{p > 2k} factor >= e^(-k/2).
Convergence: for p > max(s, 2k) the log-factor is O(k^2/p^2) by Lemma 3.2,
summable; the finitely many remaining factors are nonzero by admissibility.
Total: S(H) >= e^(-2.033k - 0.5k) >= e^(-2.6k).  []

## 4. Step 1: reduction to a sifted count

Let R be as in Section 1 (fixed in Section 11; only R <= X^(1/2) is used
here). If n <= X and all n + h_i are prime and n + h_1 = n > R, then every
n + h_i is a prime exceeding R, hence Pi(n) has no prime factor <= R:
gcd(Pi(n), P(R)) = 1. The number of n <= X with n <= R is at most R.
Therefore

  (4.1)   N(X;H) <= R + Sift,   Sift := #{ n <= X : gcd(Pi(n), P(R)) = 1 }.

## 5. Step 2: Selberg's quadratic form

Let (lambda_d) be any real numbers indexed by squarefree d < R, with
lambda_1 = 1 (support: squarefree d < R; automatically d | P(R)). For n
counted in Sift, the only squarefree d < R with d | Pi(n) is d = 1 (any
prime factor of such d would be a prime factor of Pi(n) below R), so

    sum_{d < R, d | Pi(n)} lambda_d = lambda_1 = 1.

Since squares are nonnegative,

  (5.1)   Sift <= sum_{n <= X} ( sum_{d < R, d | Pi(n)} lambda_d )^2
               =  sum_{d1, d2 < R} lambda_{d1} lambda_{d2}
                    #{ n <= X : [d1,d2] | Pi(n) },

where [d1,d2] = lcm. Note [d1,d2] is squarefree and [d1,d2] < R^2.

## 6. Step 3: congruence counting and the remainder r_d

LEMMA 6.1. For squarefree d,

    #{ n <= X : d | Pi(n) } = X * nu(d)/d + r_d,   |r_d| <= nu(d).

PROOF. For each p | d, p | Pi(n) iff n lies in one of the nu(p) classes
-h_i mod p. By CRT the solutions n mod d form exactly nu(d) = prod_{p|d}
nu(p) residue classes mod d. Each class meets [1, X] in between
floor(X/d) and floor(X/d)+1 integers, i.e. X/d + theta with |theta| <= 1.
Summing over the nu(d) classes gives the claim.  []

Inserting Lemma 6.1 into (5.1):

  (6.2)   Sift <= X * Q + E,

  (6.3)   Q = sum_{d1,d2 < R} lambda_{d1} lambda_{d2} * F([d1,d2]),
              F(d) = nu(d)/d,

  (6.4)   E <= sum_{d1,d2 < R} |lambda_{d1} lambda_{d2}| * nu([d1,d2]).

## 7. Step 4: diagonalization; min Q = 1/G

All sums over d, r, m below run over SQUAREFREE integers < R (resp. as
indicated). Since nu is multiplicative and nu >= 1 on squarefree numbers,
F([d1,d2]) = F(d1) F(d2) / F(m) with m = gcd(d1,d2).

Key identity: for squarefree m,

  (7.1)   1/F(m) = m/nu(m) = prod_{p|m} p/nu(p)
                 = prod_{p|m} ( 1 + (p - nu(p))/nu(p) )
                 = sum_{r | m} 1/g(r),

since 1/g(r) = prod_{p|r} (p - nu(p))/nu(p). (Admissibility makes every
term finite and positive.) Substituting (7.1) into (6.3) and noting that
r | gcd(d1,d2) iff r | d1 and r | d2:

  (7.2)   Q = sum_{r < R} (1/g(r)) * u_r^2,
          u_r := sum_{d < R, r | d} lambda_d F(d).

The linear map (lambda_d) -> (u_r) on the finite index set {squarefree
d < R} is invertible: ordering indices by divisibility it is triangular
with diagonal entries F(d) != 0. Explicitly (verified by substitution and
sum_{t | e/d} mu(t) = [e = d]):

  (7.3)   lambda_d F(d) = sum_{r < R, d | r} mu(r/d) u_r.

Constraint in u-coordinates: since sum_{r | d} mu(r) = [d = 1],

  (7.4)   sum_{r < R} mu(r) u_r
            = sum_{d < R} lambda_d F(d) sum_{r | d} mu(r) = lambda_1 = 1.

By Cauchy-Schwarz, for ANY admissible weight vector,

    1 = ( sum_r mu(r) u_r )^2
      <= ( sum_r u_r^2 / g(r) ) * ( sum_r mu(r)^2 g(r) ) = Q * G,

  (7.5)   G := sum_{squarefree r < R} mu^2(r) g(r).

Hence Q >= 1/G always, with equality iff u_r = mu(r) g(r) / G. By
invertibility of (7.3) this u is realized by an (explicit) weight vector
with lambda_1 = 1 (by (7.4), automatically). WE CHOOSE THESE OPTIMAL
WEIGHTS from now on. Thus

  (7.6)   Q = 1/G.

## 8. Step 5: the optimal weights satisfy |lambda_d| <= 1

Insert u_r = mu(r) g(r)/G into (7.3), write r = d m with m squarefree,
gcd(m, d) = 1, so mu(r/d) mu(r) = mu(m) mu(d) mu(m) = mu(d) mu^2(m) and
g(r) = g(d) g(m):

  (8.1)   lambda_d = mu(d) * ( g(d)/F(d) ) * G_d(R/d) / G,
          G_d(x) := sum_{squarefree m < x, gcd(m,d) = 1} mu^2(m) g(m),

and g(d)/F(d) = prod_{p|d} [ nu(p)/(p - nu(p)) * p/nu(p) ]
             = prod_{p|d} p/(p - nu(p)) = prod_{p|d} (1 + g(p)).

CLAIM:  G >= prod_{p|d} (1 + g(p)) * G_d(R/d), hence |lambda_d| <= 1.

PROOF. Consider pairs (a, m) with a | d and m counted in G_d(R/d). Then
r := a m is squarefree (a | d squarefree, gcd(m,d) = 1) and
r = a m <= d m < d * (R/d) = R, so r is counted in G, with
mu^2(r) g(r) = g(a) g(m). The map (a,m) -> am is injective: a = gcd(r,d)
and m = r/a are recovered from r. Therefore

    G >= sum_{a | d} g(a) * G_d(R/d) = prod_{p|d} (1 + g(p)) * G_d(R/d). []

In particular lambda_1 = G_1(R)/G = 1, consistent.

## 9. Step 6: the error term E

By |lambda_d| <= 1 (Step 5), nu([d1,d2]) <= nu(d1) nu(d2) (as nu >= 1 and
nu([d1,d2]) nu(gcd) = nu(d1) nu(d2)), and nu(d) <= k^omega(d) (Lemma 3.1):

  (9.1)  E <= ( sum_{squarefree d < R} nu(d) )^2,

  sum_{d < R} mu^2(d) nu(d) <= R * sum_{d < R} mu^2(d) nu(d)/d
    <= R * prod_{p < R} (1 + k/p) <= R * exp( k * sum_{p < R} 1/p )
    <= R * exp( k (lnln R + 0.262) )              [by (RS1), R >= 286]
    =  R * ( e^0.262 * ln R )^k <= R * (1.30 ln R)^k.

Hence, using ln R <= ln X,

  (9.2)  E <= R^2 * (1.30 ln X)^(2k) <= R^2 * (1.69)^k (ln X)^(2k).

## 10. Step 7: lower bound for G (the core)

Recall G = sum_{squarefree d < R} mu^2(d) g(d), and let z = R^(1/u) with a
parameter u >= 1 (u = 4k+1 in the Theorem; re-optimized in Section 12).
All terms are positive, so restricting the support to z-smooth d gives

  (10.1)  G >= G_z(R) := sum_{d < R, d | P(z)} mu^2(d) g(d)
             = G_z(inf) - Tail,

  G_z(inf) := sum_{d | P(z)} mu^2(d) g(d) = prod_{p <= z} (1 + g(p))
            = prod_{p <= z} (1 - nu(p)/p)^(-1),

  Tail := sum_{d | P(z), d >= R} mu^2(d) g(d).

### 10a. Rankin bound for the tail

For any sigma > 0, 1 <= (d/R)^sigma on d >= R, so

    Tail <= R^(-sigma) * prod_{p <= z} (1 + g(p) p^sigma).

Divide by G_z(inf) factorwise:
(1 + g p^sigma)/(1 + g) = 1 + g (p^sigma - 1)/(1 + g) <= 1 + g (p^sigma - 1)
<= exp( g(p) (p^sigma - 1) ). Take sigma = c/ln z with 0 < c <= 1; for
p <= z, by (E4), p^sigma - 1 = e^(sigma ln p) - 1 <= sigma (ln p)
e^(sigma ln p) <= e^c sigma ln p. Also R^(-sigma) = e^(-c u) since
ln R = u ln z. Hence

  (10.2)  Tail <= G_z(inf) * exp( -c u + c e^c L / ln z ),
          L := sum_{p <= z} g(p) ln p.

### 10b. Bounding L

Split at 2k.
 (i) p <= 2k: g(p) = nu(p)/(p - nu(p)) <= (p-1)/1 = p - 1. So
     sum_{p <= 2k} g(p) ln p <= ln(2k) * sum_{p <= 2k} (p-1)
     <= ln(2k) * (k^2 + 2) <= 2 k^2 ln(2k)
     (sum of primes <= 2k is at most 2 + sum of odd numbers <= 2k
      = k^2 + 2 <= 2k^2 for k >= 2; for k = 1 check directly:
      g(2) <= 1, contribution <= ln 2 <= 2 ln 2).
 (ii) 2k < p <= z: nu(p) <= k, so g(p) <= k/(p-k) <= 2k/p. By (RS2),
     sum_{2k < p <= z} (2k/p) ln p <= 2k ln z.
Total:

  (10.3)  L <= 2 k ln z + 2 k^2 ln(2k).

Combining (10.2)-(10.3):

  (10.4)  Tail <= G_z(inf) * exp( -Delta ),
          Delta := c u - 2 c e^c k - 2 c e^c k^2 ln(2k) / ln z.

### 10c. Main choice of parameters and the 1/2

Take c = 1/2, u = 4k + 1, and impose

  (C1)   ln z >= 17 k^2 ln(2k)        [verified in Section 11].

Then 2 c e^c k = e^(1/2) k = 1.6487 k, c u = 2k + 1/2, and the last term of
Delta is at most e^(1/2)/17 <= 0.097, so

    Delta >= (2 - 1.6487) k + 0.5 - 0.097 = 0.3513 k + 0.403 >= 0.7543,

whence exp(-Delta) <= 0.471 < 1/2 and, by (10.1),

  (10.5)  G >= (1/2) * G_z(inf).

(For large k this 1/2 improves itself to (1 - e^(-0.35 k - 0.4))^(-1) -> 1;
we keep 1/2 for a clean constant. See Section 13.)

### 10d. Evaluation of G_z(inf) via Mertens and the singular series

Impose (verified in Section 11):

  (C2)   z > s,  z > 2k,  z >= 285.

Write G_z(inf) = prod_{p <= z} (1 - 1/p)^(-k) / S_{<=z},
S_{<=z} := prod_{p <= z} (1 - nu(p)/p)(1 - 1/p)^(-k). By (C2) every p > z
has nu(p) = k (Lemma 3.1(b)) and p > 2k, so Lemma 3.2 gives

    | ln( S(H) / S_{<=z} ) | <= sum_{p > z} 2 k^2/p^2
       <= 2 k^2 * sum_{n > z} n^(-2) <= 2 k^2 * (2/z) = 4 k^2 / z,

hence S_{<=z} <= S(H) e^(4 k^2/z). By (RS3) and (E2) (x = 1/(2 ln^2 z)):

    prod_{p <= z} (1 - 1/p)^(-k) >= ( e^gamma ln z )^k (1 - 1/(2 ln^2 z))^k
       >= ( e^gamma ln z )^k * exp( -k / ln^2 z ).

Combining with (10.5):

  (10.6)  G >= (1/2) * S(H)^(-1) * ( e^gamma ln z )^k
               * exp( - 4 k^2/z - k/ln^2 z ).

## 11. Step 8: choice of R, verification of (C1)-(C2), and assembly

Fix

    R = X^(1/2) (ln X)^(-2k),    z = R^(1/u),    u = 4k + 1.

Throughout write t = lnln X; hypotheses (H2),(H4) give k <= t^2, t >= 30.

### 11a. Elementary consequences of (H2)-(H4)

  (P1)  2 k lnln X <= 2 t^3 <= (ln X)/20, i.e. 40 t^3 <= e^t (at t = 30:
        40 * 27000 = 1.08e6 <= e^30 = 1.07e13; and e^t/t^3 is increasing
        for t >= 3). Hence

           ln R = (1/2) ln X - 2k lnln X >= 0.45 ln X,
           delta := 4 k lnln X / ln X <= 1/10 <= 1/2.

  (P2)  ln z = ln R / (4k+1) >= 0.45 ln X/(5k) = 0.09 ln X / k
        >= 0.09 e^t / t^2.

  (C1)  holds: need ln z >= 17 k^2 ln(2k); it suffices that
        0.09 e^t/t^2 >= 17 t^4 ln(2 t^2), i.e. e^t >= 189 t^6 ln(2 t^2).
        At t = 30: RHS = 189 * 7.29e8 * 7.50 = 1.03e12 <= 1.07e13 = e^30;
        and e^t/(t^6 ln(2t^2)) is increasing for t >= 30.

  (C2)  holds: ln z >= 0.09 e^t/t^2 >= 1.19e9 (t = 30, k <= t^2), while
        ln s <= 2t <= 60 (by (H3)), ln(2k) <= ln(2 t^2) <= 8, ln 285 < 6.
        So z > s, z > 2k, z >= 285. Also R >= 286 (used in (RS1)) and
        z >= 285 (used in (RS3)).

  (P3)  4 k^2/z + k/ln^2 z <= k^2 lnln X / ln X. Indeed:
        4 k^2/z = 4 k^2 e^(-ln z) <= (1/2) k^2 t/e^t since ln z >= 1.19e9;
        k/ln^2 z <= k (k/(0.09 ln X))^2 = 124 k^3/(ln X)^2
        <= (1/2) k^2 t / ln X iff 248 k <= t ln X, true since
        248 t^2 <= t e^t for t >= 30.

### 11b. Main term

By (6.2), (7.6), (10.6):

    Sift <= X/G + E
         <= 2 S(H) ( e^gamma ln z )^(-k) X exp( 4k^2/z + k/ln^2 z ) + E.

Since ln z = ln R/(4k+1):

    ( e^gamma ln z )^(-k) = ( (4k+1) e^(-gamma) )^k (ln R)^(-k).

By (P1) and (E3) (x = delta <= 1/2):

    (ln R)^(-k) = (2/ln X)^k (1 - delta)^(-k)
               <= (2/ln X)^k exp( 8 k^2 lnln X / ln X ).

Hence, with theta_1 := 8 k^2 lnln X/ln X + 4 k^2/z + k/ln^2 z,

  (11.1)  X/G <= 2 ( (8k+2) e^(-gamma) )^k S(H) X (ln X)^(-k) e^(theta_1)
              =  C(k) S(H) X (ln X)^(-k) e^(theta_1),

and by (P3), theta_1 <= 9 k^2 lnln X / ln X <= 9 t^5/e^t <= 2.05e-5 < 0.69.

### 11c. Error terms relative to the main term

Denote M := C(k) S(H) X (ln X)^(-k). Note C(k) >= 2 (as (8k+2)e^(-gamma)
= 4.49k + 1.12 >= 1) and S(H)^(-1) <= e^(3k) (Lemma 3.3).

E-term: by (9.2), R^2 = X (ln X)^(-4k), so

    E/M <= X (1.69)^k (ln X)^(-2k) * (ln X)^k e^(3k) / (2 X)
        = (1/2) ( 1.69 e^3 / ln X )^k <= ( 34 / ln X )^k <= 34/ln X.

R-term (from (4.1)): R/M <= X^(1/2) (ln X)^k e^(3k) / (2X)
    <= X^(-1/2) ( e^3 ln X )^k <= X^(-1/4),
since k (3 + lnln X) <= t^2 (3 + t) <= (ln X)/4 for t >= 30
(t = 30: 900 * 33 = 29700 <= e^30/4 = 2.7e12; increasing thereafter).

### 11d. Proof of Theorem D1-L

By (4.1), (11.1), 11c:

    N(X;H) <= M ( e^(theta_1) + (34/ln X)^k + X^(-1/4) )
           =: M (1 + err(X,k)),

    err(X,k) <= ( e^(theta_1) - 1 ) + (34/ln X)^k + X^(-1/4)
             <= 2 theta_1 + 34/ln X + X^(-1/4)       [(E4), theta_1 <= 0.69]
             <= 18 k^2 lnln X/ln X + 34/ln X + X^(-1/4).

Since k^2 lnln X >= 30, we have 34/ln X <= 1.2 k^2 lnln X/ln X, and
X^(-1/4) is smaller still; hence

    err(X,k) <= 20 k^2 lnln X / ln X <= 20 (lnln X)^5 / ln X.

This proves the Theorem with C(k) = 2 ( (8k+2) e^(-gamma) )^k.  []

REMARK 11.1 (cosmetic forms of C(k)). C(1) = 2 * 10 e^(-gamma) = 11.230.
For k >= 2: (8k+2)^k = (8k)^k (1 + 1/(4k))^k <= (8k)^k e^(1/4), and by (E6)
k^k <= k! e^k / sqrt(2 pi k), so

    C(k) <= 2 e^(1/4) (8 e^(1-gamma))^k k!/sqrt(2 pi k)
         = (2.568/sqrt(2 pi k)) * (12.21)^k k!
         <= (12.4)^k k!/sqrt(k)     for k >= 2,

since 2.568/sqrt(2 pi) = 1.0245 <= (12.4/12.21)^k = (1.0156)^k for k >= 2.
Using only the elementary (E5) instead: C(k) <= 2 e^(1/4) (8 e^(1-gamma))^k k!
<= 2.6 * (12.3)^k k! for all k >= 1.

REMARK 11.2 (the constant X_0). X_0 = exp(exp(30)) is chosen only so that
every inequality in 11a and 11c holds with k as large as (lnln X)^2 and
s as large as (ln X)^2. It is grossly wasteful: for any FIXED k and s, the
proof works as soon as (P1), (C1), (C2), and the 11c inequalities hold,
which happens for far smaller X (roughly ln X >= max(40 k ln k * u,
350 k^2 ln(2k) u, 21 u ln s, 250) with u = 4k+1). We do not optimize X_0.

REMARK 11.3 (normalization h_1 = 0). For general h_1, apply the Theorem to
H - h_1 = {0, h_2 - h_1, ...} (same nu, same S(H), same span) and note that
#{n <= X: n + h_i all prime} differs from the count for the translated set
by at most s <= (ln X)^2 <= X^(1/4), already absorbed into err in 11d.

## 12. Step 9: optimized parameters (proof of Corollary D1-L')

Let k >= 5. Re-run Section 10c with

    c = k^(-1/2)  (so 0 < c <= 1/2),
    u* = 2 e^c k + 0.8932/c      [0.8932 = ln 2 + 0.2],

and z* = R^(1/u*). Since e^c <= 1 + c + c^2 for 0 <= c <= 1,

  (12.1)  u* <= 2k + 2 sqrt(k) + 2 + 0.8932 sqrt(k) <= 2k + 2.9 sqrt(k) + 2,

and u* <= 4k + 1 for k >= 4 (2.9 sqrt(k) + 1 <= 2k), so z* >= z and all of
(C2), (P2), (P3) hold a fortiori with z* in place of z. For the Delta-term:
c u* = 2 c e^c k + 0.8932, so

    Delta* = 0.8932 - 2 c e^c k^2 ln(2k)/ln z*,

and since ln z* >= ln z >= 17 k^2 ln(2k) by (C1), the subtracted term is at
most 2 e k^(1/2) k^2 ln(2k) / (17 k^2 ln 2k) -- more precisely
2 c e^c k^2 ln(2k)/ln z* <= (2 e / (17 sqrt(k))) <= 0.15 for k >= 5. Hence
Delta* >= 0.7432 > ln 2, exp(-Delta*) <= 0.476 < 1/2, and (10.5), (10.6)
hold with z* in place of z.

Assembly as in 11b with u* in place of 4k+1:

    X/G <= 2 ( 2 u* e^(-gamma) )^k S(H) X (ln X)^(-k) e^(theta_1).

By (12.1), 2 u* <= 4k (1 + 1.45/sqrt(k) + 1/k), so

    ( 2 u* e^(-gamma) )^k <= ( 4 e^(-gamma) k )^k (1 + 1.45/sqrt(k) + 1/k)^k
                          <= ( 4 e^(-gamma) k )^k e^( 1.45 sqrt(k) + 1 ).

Error bookkeeping (11c, 11d) is unchanged (it never used the value of u
beyond u >= 1 and ln z >= 0.09 ln X/k, both still true since u* <= 4k+1).
Hence Corollary D1-L' holds with

    C*(k) = 2 e ( 4 e^(-gamma) k )^k e^(1.45 sqrt(k))
          = 2 e ( 2.2465 k )^k e^(1.45 sqrt(k)).

Cosmetic form: by (E6), k^k <= k! e^k/sqrt(2 pi k), so

    C*(k) <= ( 2.2465 e )^k k! e^(1.45 sqrt(k)) * 2e/sqrt(2 pi k)
          <= (6.11)^k k! e^(1.45 sqrt(k))     for k >= 5,

since 2 e/sqrt(2 pi k) = 5.437/sqrt(6.283 k) <= 0.97 for k >= 5 and
2.2465 e = 6.1065 <= 6.11.  []

## 13. Constant accounting

Final constant (Theorem): C(k) = 2 * ( (8k+2) e^(-gamma) )^k. Factor by
factor, with the step that produced it:

  (A) Prefactor 2  -- Step 10c, eq. (10.5): we discard the Rankin tail by
      showing Tail <= 0.471 G_z(inf) and keep half of G_z(inf). Loss is
      really (1 - e^(-0.3513 k - 0.403))^(-1), i.e. -> 1 exponentially in
      k; we quote the worst case k = 1. NOT a k-th-power loss.

  (B) 2^k  (inside (8k+2)^k = 2^k (4k+1)^k) -- Step 11b: ln R = ln X/2 -
      o(ln X), i.e. sieve level R = X^(1/2 - o(1)) forced by the error
      term E <= R^2 (1.3 ln R)^(2k) (Step 9). This is the CLASSICAL and
      essentially unavoidable 2^k of the Selberg upper-bound sieve at
      level X^(1/2).

  (C) (4k+1)^k  -- Step 10a-10c (Rankin truncation): G is lower-bounded
      through its z-smooth part with z = R^(1/u), u = 4k+1, and the Euler
      product over p <= z yields only (e^gamma ln z)^k =
      (e^gamma ln R/u)^k. Versus the ideal G ~ S^(-1) (ln R)^k/k!
      (Halberstam-Richert Thm 5.1, OFF LIMITS here), we pay
        2 (u e^(-gamma))^k / k!  ~  2 (4 e^(1-gamma))^k/sqrt(2 pi k)
                               =  2 (6.106)^k / sqrt(2 pi k).
      Root cause: the tail bound (10.4) forces c u > 2 c e^c k, i.e.
      u > 2k(1 + o_c(1)); even at the theoretical floor u = 2k the method
      loses (2 e^(1-gamma))^k = (3.053)^k against 2^k k!. So:
        - reducible part of (C): from u = 4k+1 down to u ~ 2k + 2.9 sqrt(k)
          (Section 12), recovering (2 + o(1))^k, at the price of
          e^(1.45 sqrt(k));
        - irreducible part (for THIS method): (2 e^(1-gamma))^k ~ 3.05^k.
      A genuinely sharper G-lower bound (contour integration or the H-R
      iteration argument, both out of scope by the task's citation rules)
      would be needed to reach 2^k k! (1 + o(1)).

  (D) e^(-gamma k)  -- Step 10d, Mertens (RS3). It partially offsets (C);
      it is already folded into the displayed C(k).

  (E) k!  -- does NOT appear in our C(k) at all; it appears only in the
      cosmetic comparisons C(k) <= (12.4)^k k!/sqrt(k) (Remark 11.1) and
      C*(k) <= (6.11)^k k! e^(1.45 sqrt(k)) (Section 12), both obtained
      from k^k >= k!-type bounds (E5)/(E6), i.e. our bound is genuinely of
      shape (c_0 k)^k = c_0'^k k! * e^(O(sqrt k)) and the task's fallback
      target "(c_0)^k k!" is met with c_0 = 12.4 (clean) resp.
      c_0 = 6.11 * e^(1.45/sqrt(k)) (optimized).

  (F) err(X,k) <= 20 k^2 lnln X/ln X  -- Step 11d. Components:
        8 k^2 lnln X/ln X * 2   from (ln R)^(-k) vs (2/ln X)^k, i.e. from
                                the (ln X)^(-2k) safety factor in R (Step 11b);
        4k^2/z + k/ln^2 z       from the singular-series cutoff and Mertens
                                error (Step 10d), negligible;
        (34/ln X)^k             congruence remainders E (Steps 9, 11c);
        X^(-1/4)                the initial reduction N <= R + Sift (Step 4).
      err = o(1) uniformly for k <= (lnln X)^2, s <= (ln X)^2, and more
      generally whenever k^2 lnln X = o(ln X).

  (G) Hypothesis usage. (H3) (span) enters ONLY through (C2): z > s, which
      makes nu(p) = k for p > z (Lemma 3.1(b)); any s with
      ln s <= 0.09 ln X/k - 1 would do, so s <= (ln X)^2 is far from tight.
      (H2) enters through (C1) (ln z >= 17 k^2 ln 2k) and 11c; the proof
      really only needs k^3 ln k = o(ln X)-type conditions, and (H2)+(H4)
      is a clean sufficient pair with ABSOLUTE X_0.

  (H) Normalization of weights: |lambda_d| <= 1 is PROVED (Step 8, via the
      divisor-pairing inequality G >= prod_{p|d}(1+g(p)) G_d(R/d)); the
      remainder bound |r_d| <= nu(d) is PROVED (Lemma 6.1). No unproven
      normalization is used anywhere.

## 14. Summary of validity

    Statement proved:  N(X;H) <= C(k) (1 + err) S(H) X/(ln X)^k,
    C(k) = 2 ((8k+2) e^(-gamma))^k   [ <= (12.4)^k k!/sqrt(k), k >= 2 ],
    C*(k) = 2e (4 e^(-gamma) k)^k e^(1.45 sqrt k)  for k >= 5,
    err <= 20 k^2 lnln X/ln X,
    valid for: H admissible, k <= (lnln X)^2, span <= (ln X)^2,
               X >= exp(exp(30))  (absolute).

    Exponent convention: k-point set <-> (ln X)^k; consuming project's
    L-gap words (L+1 points) <-> (ln x)^(L+1), i.e. k = L+1.

    External inputs: RS1-RS4 (Rosser-Schoenfeld 1962) only. PNT not used.
    Not used: Halberstam-Richert Thm 5.1 or any packaged sieve bound.

