# C6 wildcard stress-test of CLAIM-A1

Angle: C6 (wildcard -- everything not covered by C1 duality, C2 position
engineering, C3 decimation/2-adic/base change, C4 Lemma-2.4 + sieve supply,
C5 surrogate series). Date 2026-07-17. Author: C6 stress agent.
Evidence base: dossier/chain-v1.md, dossier/dissektion.md (esp. 3.4),
scratchpad/session1-steering-notes.md, scratchpad/extract/tate-irrat.md.
Numerics: scratchpad/stress/c6_numerics.py (all checks passed; see section 7).
Notation as in chain-v1: S = sum_{n>=1} p_n 2^{-n}, g_n = p_{n+1} - p_n,
delta_n = sum_{j>=1} g_{n+j} 2^{-j}, delta_{n+1} = 2 delta_n - g_{n+1};
rationality S = a/(2^s b), b odd, gives D_n := b delta_n in Z for n >= s
(Lemma 2.3).

VERDICT UP FRONT: CLAIM-A1 SURVIVES this angle. I did not falsify it.
The attack produced (i) a new RIGIDITY THEOREM (section 1) that upgrades the
claim from "no second family was found" to "no second family EXISTS in the
class of gap-linear functionals certified uniformly over integer-gap models",
(ii) a complete collapse analysis of every assigned wildcard probe
(sections 2-6), and (iii) one genuinely new derived structure -- rationality
unconditionally forces infinitely many EXACT tail coincidences delta_n =
delta_m (section 6) -- which redirects but does not break the claim.
The precise wall sentence is in section 8.

--------------------------------------------------------------------------
## 1. The certified-lattice rigidity theorem (main new tool)

The wildcard probes (Ostrowski numeration, exotic position samplings, base
reorganizations, factoradic value-side rewrites) all propose new LINEAR
functionals of the gap sequence claimed to be forced into a lattice by
rationality. The following theorem kills them all at once, and is, I
believe, the strongest formal statement of CLAIM-A1's content available.

SETUP. Fix s >= 1 and b odd. Model class M: all integer sequences
g = (g_m)_{m > s} with |g_m| <= 2^{m/2} (any subexponential bound works;
the actual prime gaps are in M by Hoheisel-type bounds, and positivity is
NOT assumed). For g in M put delta_n(g) = sum_{j>=1} g_{n+j} 2^{-j}
(absolutely convergent). Constraint set
    G := { g in M : b delta_s(g) in Z }.
(The recursion then gives b delta_n(g) in Z for ALL n >= s; G is the
formal shadow of "S rational" -- the actual gap sequence lies in G if S is
rational.) A FUNCTIONAL is F(g) = sum_{m>s} alpha_m g_m with real alpha_m,
sum_m |alpha_m| 2^{m/2} < infinity. F is CERTIFIED if there are b' >= 1
and c0 in R with b'(F(g) - c0) in Z for every g in G, i.e. F is forced
into a lattice by rationality UNIFORMLY over all integer-gap models.

THEOREM (rigidity). If F is certified then, with beta_m := b' 2^{m-s}
alpha_m:
 (i)  beta_m in Z for every m > s;
 (ii) beta_{m+1} == beta_m (mod 2^{m-s}) for every m > s.
Consequently b' F agrees, coefficient by coefficient, with
    beta_{s+1} * delta_s + sum_{j>s} z_j * delta_j,
      z_j := (beta_{j+1} - beta_j)/2^{j-s} in Z,
i.e. every certified functional lies in the coefficient-wise closure of
the Z-span of the translated family {delta_j}_{j>=s} (gaps themselves are
included: g_j = 2 delta_{j-1} - delta_j).

PROOF. Differences of the certification give b' F(h) in Z for every h in
the difference lattice D := {g - g' : g, g' in G}. Two families in D:
 (a) d_m := e_m - 2 e_{m+1} (m > s), where e_m is the m-th unit sequence.
     Check: delta_n(g + d_m) - delta_n(g) = 2^{-(m-n)} - 2*2^{-(m+1-n)} = 0
     for s <= n < m; = -1 (an integer) for n = m; = 0 for n > m. So
     g + d_m in G whenever g in G. Hence
        b'(alpha_m - 2 alpha_{m+1}) in Z  for all m > s.        (*)
 (b) 2 e_{s+1}: delta_s shifts by exactly 1, all constraints preserved.
     Hence 2 b' alpha_{s+1} in Z.                               (**)
Moreover every bounded-support h with delta_s(h) in Z lies in
Z*(2 e_{s+1}) + Z-span{d_m} (eliminate the top coordinate downward: a
bounded-support value-w vector minus w*(2 e_{s+1}) has dyadic value 0, and
value-0 vectors reduce by d's since Z[1/2] cap (1/b)Z = Z for odd b).
So (*) and (**) exhaust the bounded-support constraints. Now let
gamma_m := b' alpha_m mod Z in R/Z. By (*), gamma_m = 2 gamma_{m+1}; by
(**), 2 gamma_{s+1} = 0. Inductively gamma_m in 2^{-(m-s)} Z / Z, which is
(i); and (*) rewritten in the beta's is exactly (ii). The displayed
decomposition is then a formal resummation: b' alpha_m =
2^{-(m-s)} beta_{s+1} + sum_{s<j<m} 2^{-(m-j)} z_j.  QED

COROLLARY 1 (sparse-support annihilation). If a certified F has
infinitely many vanishing coefficients (any decimated, AP-sampled,
Ostrowski-digit-selected, or otherwise density-<1 sampling), then
b' alpha_j in Z for ALL j (chain (ii) through the zeros: beta_j == beta_M
== 0 mod 2^{j-s} for zeros M > j), and absolute convergence forces
alpha_j = 0 for all large j: F is (1/b') times a FINITE integer gap
combination, carrying no mod-1 information. No sparse sampling of the gap
sequence is ever lattice-certified.

COROLLARY 2 (scope of the claim). Any second congruence family must
either (A) exploit size bounds plus integrality (Lemma 2.5-style "small
integer is 0" arguments) -- this is exactly the configuration-gated
Lemma 2.4 world, angle C4, conditional on configuration supply -- or
(B) use an exact PRIME-SPECIFIC identity that is false for general
integer-gap models, i.e. shrink the model class M. The only exact
deterministic residue fact about prime gaps is parity (g_n even, n >= 2),
which is already absorbed as Lemma 2.3's parity clause (certifying over
even-gap models deepens each lattice by one 2-adic level and changes
nothing else). TaTe's (5.2) is precisely a type-(B) escape ON THEIR SIDE:
additivity omega(pn) = omega(n) + 1 - 1_{p|n} is an exact relation among
the "coefficients" omega(m), so their coefficient values are NOT free and
rigidity does not apply to them. The prime gaps have no known exact
relations at all; the remaining sections scan the known exact-identity
inventory of the primes and find nothing lattice-compatible.

--------------------------------------------------------------------------
## 2. Probe: Schlage-Puchta polynomial cross-elimination in base 2
##    (dissektion.md 3.4 blueprint; the assigned main probe)

ScPu Theorem 3 anatomy (per dissektion 3.4): in the FACTORIAL base,
(a) rationality forces near-integrality of the leading tail terms at every
n; (b) recursive cross-elimination over consecutive n (polynomial
coefficients in the gaps) cancels the leading growth, Lemma 5 keeping the
residue nontrivial; (c) Lemma 4 (Selberg sieve): no nonzero polynomial in
O(1) consecutive gaps vanishes for a positive proportion of n; (d) van der
Corput discrepancy finishes.

Two independent walls in base 2, both structural:

WALL 2.1 (localization cost). In base 1/m! the scaled tail
n! * tail = p_{n+1}^k/(n+1) + p_{n+2}^k/((n+1)(n+2)) + ... localizes to an
O(1) window UNCONDITIONALLY: the per-step weight ratio 1/(n+1) -> 0 beats
the polynomial numerator growth using only PNT-level bounds. In base 2 the
weight ratio is the constant 1/2 while gap numerators are unbounded, so
"near-integrality involves only the window (n, n+T]" requires
2^{-T} delta_{n+T} = o(1/b), i.e. T > log2(b delta_{n+T}): under
Cramer-Granville T ~ 2 log2 ln p_n (the runde0 (T) threshold, Hypothesis-B
territory); unconditionally (g << p^theta, theta ~ 0.525) T ~ theta*n --
a LINEAR window, useless. The ScPu engine's free localization is a
factorial-base gift with no base-2 counterpart.

WALL 2.2 (aligned-denominator vacuity -- the sharper wall). Even granting
localization, base-2 cross-elimination is EMPTY. The elimination operator
between consecutive constraints C_n: b delta_n in Z is the recursion
itself: 2*(b delta_n) - (b delta_{n+1}) = b g_{n+1}, and the residual
"b g_{n+1} in Z" is trivially true. Equivalently: the finite-window
content of C_n is the congruence
    b (g_{n+1} 2^{T-1} + ... + g_{n+T}) == -b delta_{n+T}  (mod 2^T),
which CONSTRAINS NOTHING about the window -- every residue class mod 2^T
is matched by the unknown integer b delta_{n+T} (it is a reconstruction
formula for the tail, not a constraint on the gaps). In ScPu the
elimination residual is nontrivial because the factorial weights introduce
a FRESH non-unit modulus n+1 at every step, transverse to the integrality
of the numerators; in base 2 the weight ratio 2 generates exactly the
2-adic filtration that Lemma 2.3 already exhausts. Elimination can only
reproduce the translated family.

ANSWER to the assigned question: the base-2 analogue of ScPu Lemma 4
("no nontrivial polynomial in ~log2 log n consecutive gaps vanishes for
almost all n") is a plausible STATEMENT -- sieve UPPER bounds survive at
window size k ~ log log n since all in-budget model masses are x^{1-o(1)}
(chain-v1 Lemma 4.1) -- but it is an ENGINE component (a contradiction
generator), not a congruence family; and in base 2 there is nothing to
feed it: by Wall 2.2 the would-be conspiracy polynomial produced by
elimination is identically satisfied. The ScPu route in base 2 is route D
of dissektion section 4 (a different engine, needing existence/lower-bound
input = Hypothesis-A territory), and yields NO second congruence family.
This is consistent with, and explains, dissektion 3.5.

--------------------------------------------------------------------------
## 3. Probe: exact functional equations of theta/psi transported to p_n

The exact identities available on the Chebyshev side: the von
Mangoldt/Riemann explicit formula psi(x) = x - sum_rho x^rho/rho - log 2pi
- (1/2) log(1 - x^{-2}) (exact off prime powers), the Weil explicit
formula (exact for admissible test functions), and the zeta functional
equation s <-> 1-s. Transport to p_n goes through inversion
(p_n = psi-or-theta inverse data) and produces, at best, an exact
expression delta_n = E_n({zeros}, archimedean integrals).

Lattice-level error analysis: rationality forces b E_n in Z -- but this is
the SAME family {b delta_n in Z} rewritten in analytic coordinates, not a
second family. To get a second family one would need an exact operator T
on the analytic side with T(E_n) again certified, i.e. an intertwining of
the functional equation with an endomorphism of the certified lattice.
The endomorphism ring of the value-side group Z[1/2]/Z is Z_2 (2-adic
multipliers); by the rigidity theorem the certified functionals are the
closed Z-span of the tails, on which the available exact self-maps are the
recursion (dyadic-affine) only. The functional equation rho <-> 1-rho acts
continuously on archimedean data and induces NO endomorphism of this
lattice: every transported identity carries the zero-sum term
sum_rho x^rho / rho, an unquantized real number of unit size whose
fractional part is unknown; unlike TaTe's correction delta_p(n) (an
EXACTLY KNOWN sparse series, retired as kappa_1), the transport error is
not exactly known and not provably integral. No congruence family
survives the transport. Same verdict for Chebyshev-divisibility identities
(prod_{n<p<=2n} p | C(2n,n), v_2(m!) = m - s_2(m)): they are exact but
MULTIPLICATIVE -- they quantize prime exponent vectors, and the log map to
the additive dyadic lattice destroys exactness (log p are Q-linearly
independent); no linear shadow in Z[1/2]/Z exists.

--------------------------------------------------------------------------
## 4. Probe: Ostrowski / alternative numeration systems

(a) Renumbering or re-digiting the INDEX (Zeckendorf/Ostrowski expansion
of the digit position, extracting digit subsequences along Beatty or
Ostrowski-admissible sets): every such extraction is a functional with
infinitely many vanishing coefficients; Corollary 1 annihilates it. This
subsumes and strengthens the C3 AP-decimation wall (steering notes 2(ii)b)
to ARBITRARY density-<1 samplings, not just APs.

(b) Changing the numeration of the VALUE side: every rational has a
TERMINATING factoradic expansion, so rationality of S is equivalent to
"factoradic digits of S eventually vanish". Computation: v_2(m!) = m -
s_2(m), so frac(m! * S) = frac(odd(m!) * 2^{v_2(m!)} S), i.e. the
factoradic constraint at level m is the image of the translated family
member at position v_2(m!) under multiplication by the ODD unit odd(m!).
Odd multipliers are Z_2-units acting inside the same certified lattice
(rigidity, Corollary 2): the factoradic reformulation is family one in
disguise, made WEAKER by the unit. No second family.

--------------------------------------------------------------------------
## 5. Probe: entropy / ergodic reformulations with EXACT output

The dynamical framing: the translated family is the orbit of the single
seed "b delta_s in Z" under the skew product x -> 2x - g_{n+1} (integer
inputs preserve (1/b)Z automatically). The exact -- as opposed to
statistical -- yield of the ergodic view is the doubling orbit mod b:
    D_{n+1} == 2 D_n (mod b),  hence  D_n == a 2^{n-s} (mod b),
giving EXACT PERIODICITY of the fractional parts: with ell any multiple of
ord_b(2),
    frac(delta_{n+ell}) = frac(delta_n),  equivalently
    delta_{n+ell} - delta_n in Z          for all n >= s.       (P)
(P) IS a two-parameter exact congruence family with an algebraically free
second parameter (every n, every ell in ord_b(2)*N; no configuration
gating). It is the closest thing to a (5.2)-analogue that exists, and a
literal-minded reading of CLAIM-A1 should record it. It does NOT falsify
the claim, for two reasons:
 1. It lies in the deductive closure of the stated family: (P) follows
    from {b delta_n in Z} + the recursion + gap integrality in two lines.
    CLAIM-A1's phrase "generated by the recursion" covers it.
 2. It is amplification-inert. TaTe's cube cancellation is COEFFICIENT
    cancellation: r_{eps,h} = p_0 h + sum_k (h-k) eps_k v_k has a genuine
    bilinear (h,eps) coupling (the (h-k) factor) because the second
    parameter acts by DILATION, multiplying the position variable; the
    alternating sum kills positions h <= K identically, regardless of
    omega's values, buying scale 2^{-K}. The second parameter of (P) acts
    by TRANSLATION: shifts r_{eps,h} = <eps,w> + h are affine with
    h-coefficient 1, the bilinear form is rank 1, and an alternating sum
    over a translation cube sum_eps (-1)^{|eps|} delta_{n + <eps,w>} has
    h-coefficient sum_eps (-1)^{|eps|} g_{n + <eps,w> + h}, which cancels
    only if the gap VALUES coincide across cube translates -- i.e. only on
    repeated-configuration events, which is exactly the C4 gate again.
    Value-cancellation vs coefficient-cancellation is the precise
    dichotomy; translations can never buy the 2^{-K} scale gain.
Beyond (P), ergodic/entropy machinery outputs statistics (positive
entropy, equidistribution), i.e. engines (Tao's route B), not congruences.

--------------------------------------------------------------------------
## 6. Probe: dual integer-indexed form and the product parameterization
##    (wildcard-specific; verified numerically)

Summing p_n = #{m >= 0 : pi(m) < n} against 2^{-n} gives the exact dual
form (numerics: agreement to 1e-88)
    S = sum_{m>=0} 2^{-pi(m)} = 2 + sum_{k>=1} g_k 2^{-k},
an INTEGER-indexed series with the arithmetic function in the EXPONENT,
and the product structure 2^{-pi(m)} = prod_{p<=m} (1/2). Write
F({x_p}) = sum_{m>=0} prod_{p<=m} x_p, so S = F(all x_p = 1/2). Probes:

 (a) Coordinate moves x_r -> 2^{-t} (r prime, t in Z): the exponent
     changes by (t-1) uniformly for all m >= r, so
     F' = head + 2^{1-t} (S - head): a dyadic-AFFINE image of S. The
     entire orbit of the product parameterization under power-of-2
     coordinate changes collapses into the affine orbit of S -- closure,
     not escape (consistent with rigidity).
 (b) Index decimation m == 0 (mod 2): since all p_k (k >= 2) are odd and
     g_k even, #{even m in [p_k, p_k + g_k)} = g_k/2 EXACTLY, giving
     sum_{m even} 2^{-pi(m)} = S/2 + 1/4 (verified numerically to 1e-88):
     again affine collapse -- the parity identity is the one deterministic
     residue fact of the primes, and it is already spent (Lemma 2.3
     parity).
 (c) Index decimation mod d >= 3: the interval count is g_k/d plus a
     correction which is a deterministic function of (p_k mod d, g_k
     mod d) (verified for d = 3: correction table {(2,2)->1, (1,1)->0,
     (2,0)->0, (1,0)->0}); the correction series sum_k rho(p_k mod d,
     g_k mod d) 2^{-k} is a primes-in-AP digit series NOT certified by
     rationality of S (and not certifiable, by rigidity, absent exact
     residue laws for primes mod d, which do not exist for d > 2).
So the one genuinely product-structured reindexing of S admits no
second family: its exact transformations are affine, and its non-affine
transformations import unquantized prime-residue data. TaTe's escape --
sampling the SAME series at dilated arguments and returning to the same
lattice point via additivity -- has no counterpart because pi (unlike
omega) satisfies no exact identity under argument dilation.

NEW DERIVED STRUCTURE (not a falsification; proof-level). Rationality
forces infinitely many EXACT tail coincidences unconditionally:
if S = a/(2^s b) then for every large N there exist n != m in [N, 2N]
with delta_n = delta_m EXACTLY.
Proof: D_n = b delta_n in Z (Lemma 2.3); unconditional gap bounds
g_k << p_k^theta for a fixed theta < 1 (Hoheisel-Ingham line, modern
value theta = 0.525, Baker-Harman-Pintz [classical, not in dossier;
any theta < 1 suffices]) give, via p_{n+j} <= p_n 2^j (Bertrand),
delta_n << p_n^theta * sum_j 2^{(theta-1)j} << p_n^theta = N^{theta+o(1)}.
So on [N, 2N] the N values D_n occupy << b N^{theta+o(1)} < N integer
slots: pigeonhole. QED
Note delta_n = delta_m is an infinite-precision quantization obtained with
NO prefix-matching hypothesis -- compare Lemma 2.4, which needs matched
length-J gap words to reach 2^{J+1}-quantization. What is missing to turn
a coincidence into a contradiction is an anti-coincidence input: the
vanishing difference series sum_j (g_{n+j} - g_{m+j}) 2^{-j} = 0 forces a
self-similar cascade of compensating gap differences at all dyadic scales,
and refuting THAT for the actual primes is precisely the two-word variance
kernel of chain-v1 section 8.3 -- conditional territory, but strictly
weaker-looking than full Hypothesis A. RECOMMENDATION: log this as a
C4-adjacent redirect ("rationality supplies coincidence configurations for
free; only the anti-coincidence theorem is missing"), feeding the 8.1
kernel ordering.

--------------------------------------------------------------------------
## 7. Numerical record (c6_numerics.py, this directory)

 - S = 3.674643966011328810594704918913... (300 exact terms + bracket).
 - S = 2 + sum g_k 2^{-k}: partials agree to 9.8e-88 (expected tail-cut
   residual; identity is provable by partial summation, exact).
 - S = sum_m 2^{-pi(m)} (m <= 2000): agrees to full displayed precision.
 - sum_{m even} 2^{-pi(m)} - (S/2 + 1/4) = 4.9e-88: exact identity
   confirmed.
 - d = 3 correction table is a deterministic function of
   (p_k mod 3, g_k mod 3), values as in section 6(c); the pairs (1,2),
   (2,1) are absent as they must be (p + g is prime, so g != -p mod 3).
 - Scale demo for the pigeonhole: on [N, 2N], N = 12000, delta-width is
   45.2 -- empirically ~(ln N)^2, far below the N^{0.525+o(1)} the
   unconditional bound guarantees; the pigeonhole bites asymptotically for
   any fixed b.

--------------------------------------------------------------------------
## 8. Verdict and the precise wall sentence

VERDICT: CLAIM-A1 SURVIVES angle C6. No wildcard transformation produces a
second, unconditionally-supplied, dilation-like exact congruence family;
the claim is in fact STRENGTHENED to a theorem within its natural formal
scope (section 1), and its wording should absorb two footnotes: the
deductive closure of family one contains the exact periodicity family (P)
of section 5 (two free parameters, but translational and
amplification-inert), and rationality itself supplies exact tail
coincidences (section 6, redirect to the two-word variance kernel).

THE WALL, in one precise sentence:
Every functional of the gap sequence that rationality of S forces into a
lattice uniformly over integer-gap models lies in the closed Z-span of the
translated tails {delta_j}_{j>=s} (rigidity theorem; sparse samplings are
annihilated outright), so a second congruence family would require an
exact prime-specific identity -- an identity of the primes that is linear
in dyadically-weighted gap windows and false for generic integer gaps --
and the entire known inventory of exact prime identities (parity of gaps,
Legendre/pi-inversion, Wilson, factorial/binomial 2-adic valuations,
Chebyshev divisibilities, explicit formulas and the zeta functional
equation) contains no such identity: parity is already spent in Lemma
2.3, the compositional and multiplicative identities have no linear
shadow in Z[1/2]/Z, and the analytic identities carry unquantized
archimedean terms; equivalently, what S lacks and sum omega(n)/2^n has is
an exact intertwiner (Phi, u) with sum_h g_{Phi(n,h)} 2^{-h} =
u * delta_{tau(n)} + (exactly-known sparse correction) for a
non-translational position map Phi -- for omega the pair (h -> ph,
argument division by p) exists by additivity; for the prime-count index no
exact non-translational self-map exists at all.

Sharpest residual opening found from this angle (for the roadmap, not a
falsification): the unconditional coincidence supply of section 6 shows
the missing engine input from the C6 direction is an anti-coincidence /
two-word variance statement (chain-v1 8.3), not full Hypothesis A, and
not configuration EXISTENCE (rationality provides that for free).

[END]
