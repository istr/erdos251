# C5 stress-test: engine retargeting -- can a TaTe-compatible series X constrain S?

Task: falsify CLAIM-A1 by exhibiting a series X (or family) such that
(i) the TaTe engine (5.1) -> (5.2) -> cube -> variance -> Thm 3.1 applies to
X unconditionally, and (ii) irrationality or distributional properties of X
constrain S = sum_{n>=1} p_n 2^{-n} (equivalently the tails
delta_n = sum_j g_{n+j} 2^{-j}).

Author: C5 stress agent, 2026-07-17. Evidence base: dossier PDFs,
extract/tate-irrat.md, extract/tate-engine.md, extract/pratt.md,
session1-steering-notes.md, chain-v1.md. Numerical checks: python3/sympy,
primes < 4*10^5 (all eight checks PASSED; script inline in section 7).

VERDICT: ATTACK FAILS. CLAIM-A1 survives angle C5. The engine retargets
broadly (section 2 exhibits a genuinely new working retarget class), but
every reachable X decouples from S; the precise obstruction sentences are in
section 6.

--------------------------------------------------------------------------
## 1. The engine-compatibility class (what X can the engine digest?)

From the anatomy (tate-irrat.md Part 2), the engine consumes a series
X_f = sum_n f(n)/2^n through five interfaces:

(E1) TRANSLATED FAMILY (5.1): needs only f: N -> Z with f(n) = O(2^{n(1-eps)}).
     Available for essentially any integer numerator. (Same as our Lemma 2.3.)
(E2) ABSORPTION/DILATION (5.2): needs the exact identity
         f(p m) = f(m) + c_p - e_p(m),
     with c_p in Z INDEPENDENT of m (so q c_p sum_h 2^{-h} = q c_p == 0
     mod 1) and e_p(m) a sparse correction (TaTe: c_p = 1,
     e_p = 1_{p|m}; for Omega: c_p = 1, e_p = 0). This is the load-bearing
     interface: f must be additive under argument multiplication by every
     prime in a large range, up to a constant plus a sparse error.
(E3) CUBE (5.4)-(5.8): coefficient-agnostic (Lemma 5.2 is a statement about
     primes in [P/2,P]); inherits (E2).
(E4) LINEARIZATION + VARIANCE (5.12)-(5.21): needs f = sum_p c_p 1_{p|.}
     (+ prime-power corrections), with X_p = o(1) forcing the weights c_p
     to be o(2^K) = o((log_3 x)^2), and the variance lower bound (5.21)
     needing sum_{p medium, c_p != 0} c_p^2/p >> 2^K.
(E5) THM 3.1 (very large primes): needs the large-prime part of f to be
     expressible through 1-bounded completely multiplicative rough/smooth
     indicators g_l.

CONSEQUENCE (closure of the class): iterating (E2) over the prime
factorization, any engine-compatible f satisfies
    f(m) = sum_p c_p v_p-linear terms + bounded sparse corrections,
hence in particular
    (*) f(2m) - f(m) = c_2 + O(sparse bounded corrections),
and the value of the series is
    X_f in Z-span{ sum_p c_p/(2^p - 1) } + (explicitly rational terms).
Every engine-compatible series is a PRIME-VALUE-POSITION object: its binary
structure lives at digit positions p (prime values), with bounded weights.
S is a PRIME-COUNT-POSITION object: digit positions n (prime counts),
numerator p_n ~ n log n. The whole C5 question is whether any bridge
crosses between these two lattices. Sections 3-5: it does not.

--------------------------------------------------------------------------
## 2. A genuine working retarget (engine side succeeds; kept for the record)

CLAIM (engine transfer, checked at interface level, not written as a full
proof): for A a subset of the primes, define
    omega_A(m) := #{p in A : p | m},   X_A := sum_m omega_A(m)/2^m
                = sum_{p in A} 1/(2^p - 1).
Then the absorption identity holds EXACTLY (numerical check 4):
    omega_A(p m) = omega_A(m) + 1_{p in A} - 1_{p in A} 1_{p|m},
so for p | n:
    omega_A(n + ph) = omega_A(n/p + h) + 1_{p in A}(1 - 1_{p^2 | n+ph}),
and (5.2) transfers verbatim with c_p = 1_{p in A} (note the DILATION
primes p_eps need not lie in A; only the weight is A-restricted). The cube
(E3) is untouched; the linearization gives X_p supported on p in A; the
variance lower bound (5.21) needs
    sum_{p in A, W < p <= R} 1/p >> 2^K ~ (log_3 x)^2,
i.e. only a very mild density of A inside the primes; Thm 3.1's carriers
become g_l completely multiplicative with g_l(p) = 1_{p not in A cap J_l},
still 1-bounded multiplicative, with (3.2) satisfied since J_l subset
(R_+, 2x] is far above the (3.2) window. This matches TaTe's own extension
remark (Section 1.3, p.4: "other sets A that are sufficiently similar to
the primes", anchored in tate-irrat.md Part 1.3).

Instance with gap-flavored content: A = {p_n : g_n <= 2 log p_n} has,
unconditionally, index density >= 1/2 (Markov over sum of gaps; empirically
0.89, check 8) and divergent reciprocal sum, so [modulo the routine
re-verification of kappa_2/kappa_5 bookkeeping, flagged UNVERIFIED at full
proof level] the engine yields:
    sum_{n : g_n <= 2 log p_n} 1/(2^{p_n} - 1)  is irrational.
This is a new-looking, unconditional, gap-DEFINED irrationality statement.

WHY IT STILL FAILS (ii): the statement constrains the VALUE-position lattice
{2^{-p_n}} of the small-gap primes. Rationality of S constrains the
COUNT-position lattice {2^{-n}} through b delta_n in Z. There is no exact
map between the two: the reindexing m = p_n (function inversion n = pi(m))
moves digit positions from counts to values, and 2^{-pi(m)} is not a
rational multiple of 2^{-m}; no identity converts membership of b delta_n
in Z into rationality of any X_A. The retarget succeeds as an engine
application and says NOTHING about S.

SHARPER NEGATIVE (configuration-gating re-imported): if one tries to make A
encode gap data strongly enough to matter for S (e.g. A = lower twin
members, A = {p_n : g_n = g_{n+1}}, or any A whose infinitude/regularity is
the open input of chain-v1 section 4), the variance interface (E4) demands
sum_{p in A, p <= R} 1/p >> (log_3 x)^2 -- exactly an unconditional-supply
statement of Hypothesis-A type. Sparse gap-defined A (twins: Brun,
sum 1/p < infinity) fail (5.21) outright. So the only A the engine accepts
unconditionally are those too dense to encode nontrivial gap configurations,
and the A that would encode them re-import the conditional input. This
mirrors, on the C5 axis, the configuration-gating already recorded for
chain-v1 Lemma 2.4 (steering notes section 6, item 6).

--------------------------------------------------------------------------
## 3. Candidate direction 1: hybrid series sum_m omega(m) c_m / 2^m

(a) c_m = 1_P(m) (weight on prime positions): X = sum_p omega(p)/2^p =
    sum_p 2^{-p} = the prime constant. The dilated family is IDENTICALLY
    ZERO: for p | n, every n + ph is divisible by p and exceeds p, so
    1_P(n + ph) = 0 for all h >= 1 (check 7). The "second family"
    q sum_h f(n+ph)/2^h == 0 is thus TRUE UNCONDITIONALLY AND INDEPENDENTLY
    OF RATIONALITY -- it is not a constraint, so the alternating-cube
    amplification amplifies 0 == 0 and the variance dichotomy has no
    rationality-conditional input to contradict. VACUOUS-DILATION TRAP:
    weights supported on primes annihilate the dilated series.
(b) c_m = 1_{p_0 | m} (divisibility weight): absorption of the omega factor
    survives, but the weight transforms as 1_{p_0 | n + ph} = 1_{p_0 | h}
    (for p_0 | n, p != p_0): the dilated series becomes a sum over h == 0
    (mod p_0) -- POSITION DECIMATION, which is exactly the known lattice
    exit (steering notes section 2(b): needs the generating function at
    z = 2^{-1/p_0} roots-of-unity combinations, unconstrained by
    rationality). So divisibility weights convert dilation into decimation
    and die on the recorded obstruction.
(c) c_m = 1_P(m - t) (shifted-prime weight) or any weight without an exact
    m -> m/p covariance: the absorption identity must act on EVERY factor of
    the numerator simultaneously; omega(n+ph) 1_P(n+ph-t) absorbs only the
    omega factor, leaving a mixed object (translated numerator, AP-sampled
    weight) that is a tail of NO series -- (5.2) unreachable.
General sentence: a product numerator omega(m) c(m) is engine-compatible
iff c itself is engine-compatible; the engine-compatible weights are (up to
sparse corrections) constants on p-fibers, and then X collapses into the
class of section 1 -- value-position series with bounded weights, decoupled
from S.

--------------------------------------------------------------------------
## 4. Candidate direction 2: shifted-prime-argument series
##    X_t = sum_n omega(p_n + t)/2^n

(E1) holds. (E2) fails at the same point as for g_n, one level up: the
position variable is the prime count n, and absorption would need
f(n) = omega(p_n + t) at n in pZ expressed through f(n/p), i.e. an exact
identity for p_{pn} in terms of p_n; none exists (p_{2m} ~ 2 p_m is
asymptotic only; exactness fails at the first differences -- check 6 shows
p_{2m} - p_m has nonconstant sign-changing second differences, so it is not
even polynomial-plus-constant). Moreover, even GRANTING irrationality of
X_t by other means, the linkage to S is absent: omega(p_n + t) is not an
exact function of p_n modulo the 2^{-n} lattice; no Z-combination of
{X_t}_t and S telescopes into a provably rational series. Both (i) and (ii)
fail.

--------------------------------------------------------------------------
## 5. Candidate directions 3-4: gap-encoding weights at integer positions;
##    multi-series differences

(a) G(m) := gap containing m (= p_{k+1} - p_k for p_k <= m < p_{k+1}):
    X_G = sum_m G(m)/2^m is integer-indexed with gap numerators -- the most
    natural "position integer-indexed, weight encodes gap data" candidate.
    Exact identity (check 5):
        X_G = 2 sum_k g_k (2^{-p_k} - 2^{-p_{k+1}}),
    a VALUE-position series again. Engine: (E2) fails -- G(pm) is the gap
    containing pm, and m -> pm does not map gap intervals to gap intervals;
    no absorption identity, c_p does not exist. Linkage: rationality of S
    controls sum g_k 2^{-k} (count positions); X_G lives on sum
    (g_k - g_{k-1}) 2^{-p_k} (value positions); the transfer between the
    two is the function-inversion reindexing, not a lattice operation.
    Both (i) and (ii) fail.
(b) W_m := sum_{p_m <= j < p_{m+1}} omega(j) (omega mass of the m-th gap
    block; = numerator of sum_n omega(n) 2^{-pi(n)} at count position m):
    (E2) fails (interval structure has no m -> m/p covariance); and W_m
    does not determine g_m exactly, so even irrationality of that series
    leaves delta_n unconstrained.
(c) Abel-summation partners: the only exact integer-indexed rewritings of
    S itself are S = sum_{m>=0} 2^{-pi(m)} = 2 + sum_k g_k 2^{-k}
    (checks 1-2) -- both stay in the count-position lattice with the same
    missing second parameter; and the pi-numerator partner
    sum_m pi(m) 2^{-m} = 2 sum_p 2^{-p} (check 3) jumps to the
    value-position lattice but has numerator pi(m), for which (E2) fails
    (pi(pm) has no exact expression through pi(m)) -- and its value is the
    prime constant, already irrational classically with no consequence
    for S.
(d) Multi-series differences: the engine-compatible class is closed under
    Z-linear combinations (signed weights c_p work; variance uses c_p^2).
    So differences X_A - X_B add nothing beyond section 1's class. For a
    difference-system to constrain S one would need engine-compatible f
    with f - (p_n at count positions) provably-rational-in-sum. The only
    unconditional provably-rational family with the needed n log n growth
    headroom is polynomial numerators (sum P(n) 2^{-n} in Q for P in
    Z[n]); but (*) of section 1 forces f(2m) - f(m) = c_2 + bounded sparse,
    while p_{2m} - p_m - (P(2m) - P(m)) is unbounded-nonconstant for every
    polynomial P (degree <= 1 undershoots ~ m log m, degree >= 2
    overshoots; exactness already fails at second differences, check 6).
    No decomposition p_n = f(n) + (rational-series residue) exists.

--------------------------------------------------------------------------
## 6. Failure sentences (the deliverable)

MASTER SENTENCE. Every series X to which the TaTe engine applies has
numerator in the absorption class f(pm) = f(m) + c_p - (sparse correction)
with bounded integer weights, hence f(2m) - f(m) = c_2 + O(bounded sparse)
and X in Z-span{sum_p c_p/(2^p - 1)} + Q -- a prime-VALUE-position object;
linking any such X to S = sum p_n 2^{-n} would require either (i) an
engine-compatible f with sum_n (p_n - f(n))/2^n provably rational, which is
impossible because the only provably-rational residual family at the
required n log n growth is polynomial and p_{2m} - p_m - (P(2m) - P(m)) is
unbounded and nonconstant for every polynomial P while absorption forces
f(2m) - f(m) constant up to sparse bounded corrections, or (ii) a
rationality transfer across the reindexing m = p_n (n = pi(m)), which moves
digit positions between the count lattice {2^{-n}} and the value lattice
{2^{-p}} and is not an operation the 2-adic lattice supports (2^{-pi(m)} is
not a rational multiple of 2^{-m}); therefore every X reachable by the
engine decouples from S, and every X coupled to S breaks the engine at
(5.2) or (5.21).

Per-candidate sentences:
1. (subset series, section 2) The engine retargets unconditionally to
   X_A = sum_{p in A} 1/(2^p - 1) for any A subset of the primes with
   sum_{p in A, p <= R} 1/p >> (log_3 x)^2, but the conclusion constrains
   the value-position lattice of A and no identity converts b delta_n in Z
   into rationality of any X_A; A sparse enough to encode open gap
   configurations fails the variance floor (5.21) -- for twins,
   sum 1/p converges (Brun) -- re-importing exactly the conditional supply
   that CLAIM-A1 says is missing.
2. (prime-position weights, section 3a) Weights supported on primes make
   the dilated family identically zero (1_P(n + ph) = 0 for p | n, h >= 1),
   so the second family exists but is unconditionally true and carries no
   rationality-conditional constraint to amplify.
3. (divisibility weights, section 3b) Weights 1_{p_0 | m} transform under
   dilation into position decimation h == 0 (mod p_0), which exits the
   2-adic lattice at z = 2^{-1/p_0} exactly as recorded in steering notes
   section 2(b).
4. (shifted-prime arguments, section 4) f(n) = omega(p_n + t) fails
   absorption because p_{pn} admits no exact expression through p_n
   (p_{2m} - p_m is not polynomial-plus-constant), and no Z-combination of
   the X_t telescopes against S into a provably rational series.
5. (gap weights at integer positions, section 5a) The local-gap numerator
   G(m) satisfies X_G = 2 sum g_k (2^{-p_k} - 2^{-p_{k+1}}) exactly, i.e.
   it is secretly a value-position series, and G has no absorption identity
   because m -> pm does not respect gap intervals.

--------------------------------------------------------------------------
## 7. Numerical support (all PASSED; primes < 4*10^5, sympy)

1. S = sum_{m>=0} 2^{-pi(m)} (Abel partner; stays count-position). PASS.
2. S = 2 + sum_k g_k 2^{-k}. PASS.
3. sum_m pi(m) 2^{-m} = 2 sum_p 2^{-p}. PASS (0.8293650197... both sides).
4. omega_A(pm) = omega_A(m) + 1_{p in A} - 1_{p in A}1_{p|m}, 2000 random
   (m, p), A = {3,7,13,19,29}. PASS (exact).
5. sum_m G(m) 2^{-m} = 2 sum_k g_k(2^{-p_k} - 2^{-p_{k+1}}). PASS
   (0.7797627336972539 both sides).
6. Second differences of p_{2m} - p_m: [1,0,2,0,-4,6,-4,0,2,-2,4,-4,-2,10,
   -10,8,-4,0,0,0] -- nonconstant, sign-changing: not polynomial+constant.
7. 1_P(n + ph) = 0 for p | n, h in [1,30], 500 random (p, n). PASS.
8. A = {p_n : g_n <= 2 log p_n}: index density 0.8936; sum_{p in A} 1/p =
   2.5730 vs 2.8188 over all primes < 4*10^5 -- A carries almost the full
   Mertens mass, so (5.21) survives for this A (supporting section 2's
   engine-side claim), while twin-type A cannot.

--------------------------------------------------------------------------
## 8. Relation to CLAIM-A1

CLAIM-A1 asserts: no transformation produces a second, unconditionally
supplied, dilation-like exact family for S. Angle C5 attempted the
outflanking move: get the second family for a DIFFERENT series X and pull
its conclusion back to S. Outcome: the second family is available exactly
on the absorption class of section 1 (and does extend beyond TaTe's
literal series -- section 2 is a genuine unconditional enlargement, worth
recording), but the pullback map to S does not exist; every linkage
mechanism is blocked by one of: growth/additivity mismatch (master
sentence (i)), lattice reindexing (master sentence (ii)), vacuous
dilation (sentence 2), decimation exit (sentence 3), or variance-floor
configuration-gating (sentence 1). CLAIM-A1 is NOT falsified from this
angle; the C5 attack sharpens it: even the engine's maximal unconditional
reach (arbitrary dense prime subsets A, signed bounded weights) stays
inside the value-position lattice, one exact-function-inversion away from
S, and that inversion is precisely what no exact identity crosses.

[END]
