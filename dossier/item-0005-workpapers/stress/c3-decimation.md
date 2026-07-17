# C3 stress-test: decimation, linear combinations, 2-adic mirror, base
# change, convolutions -- attack on CLAIM-A1

Status: attack executed and FAILED to falsify CLAIM-A1; refutation (a)
of the steering notes is STRENGTHENED to a rigidity theorem with a
unified kill criterion. Author: C3 subagent, 2026-07-17. Evidence:
chain-v1.md (Lemmas 2.1-2.5), session1-steering-notes.md (secs 0-2, 6),
extract/tate-irrat.md (TaTe (5.1)-(5.3), Parts 3-4). Numerics: exact
rational arithmetic, primes to 10^7, script c3_numerics.py in this
directory; ALL PASS (12/12 checks).

## 0. Notation and scope

Coefficient sequences c = (c_m)_{m>=1} of integers (the role of the gaps
g_m = p_{m+1} - p_m); value V(c) = sum_m c_m 2^{-m}; tails
delta_n(c) = sum_{h>=1} c_{n+h} 2^{-h}, recursion
delta_{n+1} = 2 delta_n - c_{n+1}. Rationality of S = sum p_n 2^{-n},
S = a/(2^s b) with b odd, s >= 1 WLOG, gives the FAMILY
    (F)  b delta_n in Z for n >= s,  b delta_n in 2Z for n >= s+1
(chain-v1 Lemma 2.3). "Forced" (= "unconditionally supplied by
rationality" in CLAIM-A1's sense, formal layer) means: a functional Phi
of the coefficient sequence such that b Phi(c) in Z for EVERY integer
sequence c and odd b satisfying (F). The distinction between the formal
layer and prime-specific identities is handled in section 6; TaTe's own
second family (5.2) lives on the prime-specific side, and section 6
identifies the exact object that side would require for S.

## 1. The kernel framework (the unified kill criterion)

LEMMA K (kernel of the value map). Let e be a finitely supported integer
sequence with sum_m e_m 2^{-m} = 0. Then e is a Z-combination of the
elementary patterns k^{(m)} = (-1 at m, +2 at m+1), m >= 1.
Proof. E(x) = sum e_m x^m in Z[x] (after clearing the index offset)
vanishes at x = 1/2, so (2x-1) | E over Q; 2x-1 is primitive, so by
Gauss's lemma E = (2x-1) G with G in Z[x]; and (2x-1) x^m is the pattern
(-1 at m, +2 at m+1). QED
COROLLARY K2. E(1/2) = 0 with E in Z[x] implies 3 | E(2) (E(2) = 3 G(2)).
[Numerics T1: 4000 random cases, PASS.]

KERNEL MOVES. The move c_m += t, c_{m+1} -= 2t (t in Z) preserves V(c)
exactly and changes delta_j only at j = m, by -t. Hence: t in Z
preserves the integrality layer of (F); t in 2Z preserves the parity
layer as well. The moves with t in 2Z, m >= s+1, act on the instance set
of (F) for each fixed b. [Numerics T2b: PASS.]

LEMMA U (universality over b). Every odd b >= 1 admits instances of (F):
put d_n = 2 (2^n mod b), g_{n+1} = 2*[2 (2^n mod b) >= b] in {0,2}; then
delta_n = d_n / b (the recursion's unique bounded solution is the tail
series), so b delta_n = d_n in 2Z for all n >= 0. The instance set is
closed under doubled kernel moves. [Numerics T2: b in {5,7,9,11,15,21,
23}, PASS.]

KILL CRITERION. If Phi is forced, then for every odd b, every instance
c, and every doubled kernel move at m >= s+1, b (Phi(c') - Phi(c)) in Z;
ranging over all b (Lemma U; b = 1 included), Phi(c') - Phi(c) in Z. A
functional whose variation under some doubled kernel move is a
non-integer is NOT forced. For linear Phi = sum_m beta_m c_m the
variation at m is 2(beta_m - 2 beta_{m+1}), so forcedness requires
    beta_m - 2 beta_{m+1} in (1/2) Z for all m >= s+1.

THEOREM R (rigidity of the translated family). Let Phi = sum beta_m c_m
with beta_m -> 0 (any summable decay). Phi is forced if and only if
there are C in Q, M >= s+1, and z_m in (1/2)Z (z_m = 0 for m >= M) with
    beta_m = C 2^{-m} + z_m,
i.e. Phi is a Z[1/2]-multiple of a tail delta_{M-1} plus a
(1/2)Z-combination of finitely many coordinates. In particular every
forced linear functional lies in the Z[1/2]-span of the family (F)
itself plus finite integer combinations of gaps: THE TRANSLATED FAMILY
IS LINEARLY RIGID -- it has no forced linear enlargement at all.
Proof. (=>) The kill criterion gives beta_m - 2 beta_{m+1} in (1/2)Z
for all m >= s+1. Since beta_m -> 0, eventually |beta_m - 2 beta_{m+1}|
<= |beta_m| + 2|beta_{m+1}| < 1/2, and a half-integer of absolute value
< 1/2 is 0: beta_m = 2 beta_{m+1} EXACTLY for m >= some M, i.e.
beta_m = C 2^{-m} for m >= M with C := 2^M beta_M. For m < M set
z_m := beta_m - C 2^{-m}; then z_m - 2 z_{m+1} = beta_m - 2 beta_{m+1}
in (1/2)Z (the C-parts cancel), and z_M = 0, so backward induction
gives z_m in (1/2)Z. (<=) direct from (F) and integrality of the c_m,
for C in the dyadic lattice compatible with the parity layer. QED

Bookkeeping remark: the exact denominator constraints on C and the z_m
(factors of 2 from the parity layer and from evenness of gaps of odd
primes) are routine and do not affect the structural conclusion: no
linear functional outside the Z[1/2]-span of the family (F) plus finite
coordinate combinations is forced.

## 2. Candidate 1: decimation of the digit position (the assigned target)

Kept-weight decimations: tildeD_{n,c} = sum_{h == c mod a, h >= 1}
c_{n+h} 2^{-h}. Renormalized decimations: D_{n,c} = sum_j c_{n+c+aj}
2^{-j}.

2.1 CROSS-INDEX RECURSION (new, exact): with indices mod a,
    tildeD_{n+1,c} = 2 tildeD_{n, c+1} - [c == 0 mod a] c_{n+1}.
So the whole two-parameter array {tildeD_{n,c}} is generated from one
a-vector by an affine phase-rotating map: the apparent second parameter
c is consumed by translation. (This is the refined form of the delta
recursion; it already suggests no new content.)

2.2 RIGIDITY FOR DECIMATED COMBINATIONS. A rational combination
L = sum_{n,c} lambda_{n,c} tildeD_{n,c} has coefficient of c_M
    beta_M = 2^{-M} phi_M,  phi_M := sum_n 2^n lambda_{n,(M-n) mod a},
and phi_M is a-periodic in M beyond the support of the lambda's (the
PHASE PROFILE). By Theorem R, L is forced iff phi is eventually
CONSTANT, and then L is a Z[1/2]-combination of the delta_n plus finite
gap terms. Every single tildeD_{n,c} has phase profile supported on one
residue class (non-constant): NOT forced. The only weight systems that
return to the lattice are exactly those that reconstitute full-density
tails. [Numerics T3a: 152/175 instance exits; T3c: a constant-phase
cross-n combo (phi = (2,2)) lands in (1/b)Z[1/2] as predicted; T3d:
24/28 non-constant combos exit; T3f: deterministic kernel-variation
kill, PASS.]

2.3 RENORMALIZED DECIMATIONS ARE NEVER FORCED (in any nonzero rational
combination over c, fixed n). Two proofs. (i) Kernel: beta decays by
factor 1/2 per a steps of the index, while Theorem R requires factor
1/2 per single step; only C = 0 is compatible, forcing all weights 0.
(ii) Galois: with t = 2^{-1/a}, the combination is a Q-combination of
the a evaluations E_n(zeta t), zeta^a = 1, of the gap generating
function E_n(z) = sum_h c_{n+h} z^h; killing all of them needs a
rational polynomial of degree < a vanishing at all roots of x^a - 2,
which is irreducible (Eisenstein at 2): impossible; and no combination
reproduces the constrained point z = 1/2. This upgrades steering-notes
refutation (a) from "single decimations exit" to "NO rational
recombination of shifted decimations re-enters, except those that
factor through the delta_n themselves."

2.4 GALOIS-NORM (multiplicative) RECOMBINATION. The norm trick converts
irrational-point evaluations into 1/2-point evaluations of NEW integer
series: e.g. a = 2, E_n(t) E_n(-t) evaluated at t = 2^{-1/2} equals
A_n^2 - B_n^2/2 with A_n = sum_j c_{n+2j} 2^{-j}, B_n = sum_j
c_{n+2j+1} 2^{-j} -- an integer-coefficient series in u = t^2 evaluated
at u = 1/2. But its value is not tied to S: under the doubled kernel
move at n+2j0 the value moves by 2^{1-j0}(A_n + B_n) + O(4^{-j0}),
generically a non-integer: NOT forced. [Numerics T3e: variations
153/112, 29/48, 29217/32752 for b = 7, 15, 23: PASS.] The same kill
applies to any polynomial functional of decimated values, since the
kernel moves act triangularly on (A_n, B_n, delta_n) with non-lattice
increments.

## 3. Candidate 2: 2-adic (Hensel) reinterpretations

3.1 The series sum p_n 2^{-n} DIVERGES in Q_2 (|p_n 2^{-n}|_2 >= 2^n
-> infinity except on the sparse set where 2 | p_n, i.e. n = 1); the
2-adic mirrors sum_m p_m 2^m and sum_m g_m 2^m converge in Z_2. Do
their residues become a second congruence family under rationality of
the REAL value? NO, with a complete formal proof:

PROPOSITION M (formal independence of the two places). For every M, the
set of values sum_m c'_m 2^m attainable by integer sequences c' that
(i) agree with c below M and (ii) have the SAME real value V(c') = V(c)
is dense in sum_m c_m 2^m + 2^M Z_2. Hence no residue of the 2-adic
mirror beyond position M is determined by the real value, let alone by
its rationality.
Proof. Value-preserving finite perturbations are exactly the kernel
combinations E = (2x-1) G (Lemma K), and their 2-adic effect is
E(2) = 3 G(2), with G ranging over x^M Z[x]: the effect group is
3 * 2^M Z. Since 3 is odd, 3Z is dense in Z_2 (3Z mod 2^k covers all
residues), so 3 * 2^M Z is dense in 2^M Z_2; infinite sums of moves at
increasing positions realize every element of the closure while keeping
the real value convergent and equal. QED
[Numerics T4: density of 3Z mod 2^k and non-vanishing of the move
variation -3t 2^m mod 2^k: PASS.]

Note the cute exact obstruction: value-preserving moves shift the
mirror by multiples of 3 * 2^M -- a nonzero, ODD-unit multiple; there
is no partial linkage (3 is invertible in Z_2), so the linkage between
the real and 2-adic values of the same coefficient stream is EXACTLY
ZERO beyond the shared low-index coefficients themselves.

3.2 What the 2-adic view DOES yield: a rewrite of the SAME family.
With T_n := b sum_{i=0}^{n-1} p_{n-i} 2^i (the reversed-window sum),
rationality gives b u_n + T_n = 2^{n-s} a, hence
    b u_n == - b sum_{i=0}^{n-s-1} p_{n-i} 2^i  (mod 2^{n-s}).
The "Hensel lift" of the recursion d_{n+m} = 2^m d_n - b sum_i 2^{m-i}
g_{n+i} says the same: the low bits of b delta_{n+m} are determined by
the RECENT gaps -- a moving-window congruence, i.e. the translated
one-parameter family again, 2-adically spelled. No second parameter
appears: the window index n is the same translation parameter.

3.3 Loophole closed: could both the real and 2-adic values be values of
one rational function (which WOULD link them)? f(z) = sum p_n z^n is
not a rational function: otherwise p_n = sum_i Q_i(n) lambda_i^n; the
radius of convergence 1 (p_n^{1/n} -> 1) forces max |lambda_i| = 1 and
p_n = sum_{|lambda_i| = 1} Q_i(n) lambda_i^n + o(1); with d = max deg
Q_i on the unit circle, p_n n^{-d} is a bounded almost-periodic
function plus o(1); d = 0, 1 contradict p_n / n -> infinity (PNT, or
just Chebyshev p_n >> n log n), and d >= 2 forces p_n n^{-d} -> 0,
while the Cesaro mean of |sum_{deg = d} c_i lambda_i^n|^2 equals
sum |c_i|^2 > 0 (distinct unit lambda_i): contradiction. Rationality of
the single VALUE S carries no tendency toward rationality of the
FUNCTION f, so the argument stands independent of the contradiction
hypothesis.

## 4. Candidate 3: base change

4.1 Re-expansions in base 2 (the composition semigroup). There is a
rich semigroup of exact integer re-expansions of S: for phi in Z[[t]]
with phi(0) = 0, integer coefficients, and phi(1/2) = 1/2 (examples:
phi_k(t) = t^k/(1-t)^{k-1} for every k >= 1; 2t^2; all compositions),
g = f o phi has integer coefficients c_m (binomial-weighted prime sums,
e.g. c_m = sum_n binom(m-n-1, n-1) p_n for phi_2) and g(1/2) = S. Each
re-expansion yields a translated family {b v_m in Z} for its tails v_m
-- a promising-looking "second family" that is in fact VACUOUS:

PROPOSITION I (invariance of the family under re-expansion). If
S = sum_m c_m 2^{-m} is ANY expansion with integer coefficients and
integer partial-sum structure, its tails satisfy v_m = 2^m S - I_m with
I_m in Z, hence v_m == u_m (mod Z) UNCONDITIONALLY (rational or not):
distinct integer expansions of the same real at the same point have
tailwise-integer-equal families. The lattice family is an invariant of
the pair (S, evaluation point 1/2), not of the expansion. No
re-expansion can produce a second family.

4.2 Base b' != 2. For 3^m S the partial sums 3^m sum_{n<=N} p_n 2^{-n}
are not integers (dyadic denominators survive); the Lemma-2.3 splitting
fails, and frac(3^m S) has no explicit prime-local expression: the
functional factors through the VALUE S alone (see trichotomy, sec. 6),
carrying no per-coefficient structure. Base 4 (digit grouping
c_m = 2 p_{2m-1} + p_{2m}) gives exactly the even-index subfamily
{delta_{2m}}: nothing new. Non-integer bases exit rationality.

## 5. Candidate 4: products, powers, convolutions with lacunary rationals

Multiplication by a rational r (lacunary or not) is a Z[1/2]-linear
operation on the family: r S's tails are Z[1/2]-combinations of the
u_n mod Z. Cauchy powers: S^k is rational with odd denominator part
b^k, and the induced family on the k-fold convolution coefficients
q^(k)_j = sum_{i_1+...+i_k=j} p_{i_1}...p_{i_k} is an INTEGER-RING
consequence of the k = 1 family:
    2^{2n} S^2 = P_n^2 + 2 P_n u_n + u_n^2,   P_n = sum_{j<=n} p_j
    2^{n-j},
so b^2 * (2^{2n} S^2) in Z follows from b u_n in Z by ring operations
alone (and odd translates by doubling). [Numerics T6: exact identity
check on instances, PASS.] General principle: the constrained values
form a ring (integers are closed under + and *), so the entire
rational-operations orbit of S -- translations, rational multiples,
powers, rational convolutions -- generates NO constraint outside the
integer-polynomial closure of the original family. Contrast: TaTe (5.2)
is NOT in the polynomial closure of (5.1)'s values; it needs the
additivity identity of omega, an input external to the value ring.
Products with irrational lacunary numbers lose rationality: no family.

## 6. Why omega escapes and what exactly is missing (TaTe comparison)

TRICHOTOMY. Every C3-type functional Phi of the coefficient stream
falls into exactly one of:
 (T1) Phi factors through the value S: constrained by rationality but
      PRIME-BLIND -- a function of the one unknown rational a/(2^s b),
      it samples no new prime data (base-b' digits, frac(3^m S), ...);
 (T2) Phi fails kernel invariance: prime-sensitive but UNCONSTRAINED --
      not a consequence of rationality (all decimations, renormalized
      or kept, non-constant-phase recombinations, Galois norms, 2-adic
      mirror residues, ...);
 (T3) Phi is kernel-invariant without factoring through S: by Theorem R
      (linear) and the ring argument (polynomial), Phi lies in the
      Z[1/2]-span / integer-polynomial closure of the ORIGINAL family.

TaTe's (5.2) evades the trichotomy because it is not a functional of an
abstract coefficient stream: the specific sequence omega satisfies
omega(pn) = omega(n) + 1 - 1_{p|n}, which makes the prima-facie-T2
functional sum_h omega(n+ph) 2^{-h} (dilated sampling) EQUAL to a T3
member (the translated tail at n/p) + integer + summable correction
delta_p(n). The coefficient stream lies on the graph of an exact
arithmetic identity, and on that graph T2 collapses into T3 -- this
collapse is the entire source of the second parameter, and everything
downstream (cube, bilinear shifts, 2^{-K} amplification, variance
dichotomy) consumes it.

For S the corresponding object would have to be: an exact identity,
valid for the true gap sequence, equating some dilated/decimated
sampling functional of the gaps (a T2 object) with a Z[1/2]-combination
of translated tails (a T3 object) modulo Z plus a correction that is
summable and retirable at TaTe's kappa_1-step. Such an identity is an
exact functional equation for n -> p_n under an index self-map. None
exists even conjecturally: the only known regularity of p_n under index
dilation is asymptotic (p_{2n} = 2 p_n (1 + o(1)), error of order
n log-ish), incompatible with membership in a fixed discrete lattice.
(The C3 numerics support the absence of accidental exact structure:
continued-fraction and small-integer-relation scans of decimated gap
tails A_n, B_n, delta_n at n up to 5*10^5, primes to 10^7, find no
small-denominator proximity and no integer relations; T5 PASS.)

## 7. Numerics summary

Script: c3_numerics.py (this directory), exact Fraction arithmetic,
python3; primes sieved to 10^7 (pi = 664579, matches). 12/12 PASS:
 T1  kernel = Z-span{x^m (2x-1)}; 3 | E(2) (4000 random cases).
 T2  instances for b in {5,7,9,11,15,21,23}: b delta_n in 2Z exactly.
 T2b doubled kernel moves preserve the full family incl. parity.
 T3a/b single decimations exit (1/b)Z in instances (152/175 kept-
     weight, 62/175 renormalized; instance accidents for the rest are
     expected -- forcedness requires membership in EVERY instance).
 T3f deterministic kill: kernel variation of any single decimation is a
     non-integer dyadic.
 T3c constant-phase cross-n combination lands in (1/b)Z[1/2] (rigidity
     theorem's converse direction).
 T3d non-constant-phase combinations exit (24/28).
 T3e norm-form A^2 - B^2/2: kernel variation non-integer (3 instances).
 T4  3Z dense in Z_2; mirror variation -3t 2^m nonzero mod 2^k.
 T5  true primes: no rational proximity (denominators <= 10^6, error
     2^-150) and no integer relations (|c| <= 6) among A_n, B_n,
     delta_n at n in {10^3, 10^4, 10^5, 5*10^5}.
 T6  2^{2n} S^2 = P_n^2 + 2 P_n u_n + u_n^2 exactly on instances.

## 8. Verdict

CLAIM-A1 SURVIVES angle C3. The attack produced no second family; it
produced instead a stronger obstruction than the one on record.

STRENGTHENED REFUTATION (the precise sentence). Every functional of
the gap stream reachable by the C3 toolbox -- digit-position decimation
with kept or renormalized weights, arbitrary rational recombination of
shifted decimations, Galois-norm recombination, 2-adic mirroring and
Hensel lifting, base change, integer re-expansion of S via the
composition semigroup {phi in Z[[t]] : phi(1/2) = 1/2}, and Cauchy
products/powers/convolutions with rationals -- either (T1) factors
through the single unknown value S and samples no prime data, or (T2)
changes by a non-integer under some value-preserving kernel move
(c_m, c_{m+1}) -> (c_m + 2, c_{m+1} - 4) -- the moves that, by Gauss's
lemma applied to 2x - 1, generate the annihilator of the constraint
family -- and is therefore not a consequence of rationality, or (T3)
has eventually-geometric coefficient tail beta_m = C 2^{-m} and lies in
the Z[1/2]-span (linear case; Theorem R) or integer-polynomial closure
(product case) of the original translated family {b delta_n in Z}; a
TaTe-(5.2)-like second family would require an exact identity, valid
for the true prime sequence, equating a T2 functional (dilated or
decimated gap sampling) with a T3 functional modulo Z up to a summable
correction -- i.e. an exact functional equation for n -> p_n under an
index self-map -- and no such identity exists, the known dilation
regularity p_{2n} = 2 p_n (1 + o(1)) being asymptotic with error far
exceeding any fixed lattice spacing.

Residual escape routes NOT closed by C3 (out of scope, for the ledger):
(i) prime-specific exact identities outside the linear/polynomial
formal layer cannot be excluded wholesale -- C3 pins the exact shape
any such identity must have (T2 = T3 mod Z + summable correction), so
any future candidate can be tested against the kernel criterion in one
line; (ii) the configuration-gated multi-parameter family of chain-v1
Lemma 2.4 (repeated gap words) is C4 territory; C3's rigidity theorem
confirms it is the ONLY multi-parameter structure available on the
formal layer, since its index pairs live exactly where the phase
profiles of two windows coincide.

[END]
