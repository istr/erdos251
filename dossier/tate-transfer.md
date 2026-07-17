# Tao-Teravainen transfer assessment -- item-0005 verdict (v2)

Date: 2026-07-17. Author: steering (Claude Fable 5), item-0005 executed
against kickoff v1 (main @ bf5de42). Payload integrity: all eight PDF
sha256 anchors re-verified against payloads/HASHES.txt this session.
Method: steering first-hand read of TaTe Section 5 (complete) and
Theorem 3.1/3.3; nine per-paper extraction agents (anchored anatomies,
verbatim-quote discipline); six-angle adversarial stress-test of the
lead hypothesis, each angle independently precision-checked. Mandate
(roadmap/item-0005.md): "Written verdict whether the unconditional
method for the sum over primes of 1/(2^p-1) extends toward sum p_n/2^n
and what breaks"; acceptance_intent: "Verdict names the exact
structural obstruction or a concrete transfer plan".

v2 revision note: this version implements the eight required revisions
of payloads/item-0005-adjudication-v1.md Section 3, adjudicating two adversarial
reviews of v1 (R1 = Fable, fresh instance, falsification attempt no. 7;
R2 = ChatGPT, cross-family), both registered as hashed payloads (see
Section 9). No mathematical result changed: the core computations (EXCH,
the rigidity theorem, the product-formula lemma) survive both reviews
and gain a sharpening (R1's one-generator observation, adopted below).
What changed is scope: several v1 sentences overclaimed relative to what
the eight-text evidence base actually supports, and are narrowed here to
the covered claim. See Section 9 for the point-by-point disposition.

Working papers (angle analyses c1..c6, numerics scripts, extraction
files) were authored in the volatile session scratchpad; every
load-bearing result is absorbed into this document, the two decisive
numerical certificates are inlined in full, and the complete working
set is preserved UNTRACKED under dossier/item-0005-workpapers/
(operator disposition: keep/commit per F5, or delete).

## 1. Verdict

NO UNCONDITIONAL TRANSFER EXISTS IN THE EVIDENCE BASE, AND THE FAILURE
IS STRUCTURAL. Scope of this claim (narrowed from v1 under adversarial
review, payloads/item-0005-adjudication-v1.md P1): no verbatim transfer of the
Tao-Teravainen (TaTe, arXiv:2512.01739v2) method is exhibited; the
linear formal layer of rationality consequences is fully classified
(rigidity, O2); every examined nonlinear repair architecture funnels
into an exchange-type requirement (EXCH', O4); no unconditional
transfer plan of any kind exists in the eight texts. NOT claimed: a
no-go theorem over all conceivable reductions -- that would require a
necessity proof this report does not have. The Tao-Teravainen
unconditional proof that sum_n omega(n)/2^n is irrational (their
Theorem 1.3, Erdos #69) does not transfer to S = sum_n p_n/2^n under
any architecture examined. Seven independent falsification attempts
against this verdict all failed (six same-session angles plus R1, a
fresh-instance cross-check), five of them closing with proof-level
rigidity statements. The obstruction is structural, not quantitative,
and is named by the following four layers, each carrying an explicit
scope qualifier per the review disposition (Section 9).

O1 (first breaking step). TaTe's engine turns rationality into the
translated congruence family (5.1): q sum_h omega(n+h)/2^h == 0 (mod 1)
for ALL n -- for S this layer EXISTS (it is verbatim the project's
lattice layer, chain-v1 Lemma 2.3: b delta_n in Z for n >= s). The
first step with no p_n-analogue is the derivation of (5.2) from (5.1):
the exact additivity identity omega(pn) = omega(n) + 1 - 1_{p|n}
absorbs a dilation of the binary-digit position (h -> ph) into a
division of the argument (n -> n/p), yielding the second,
algebraically free congruence parameter (p ranges over all p | n):
    (5.2)  q sum_h omega(n+ph)/2^h == -q delta_p(n) (mod 1),  p | n,
with delta_p(n) (5.3) an exactly-known sparse correction. Everything
downstream consumes (5.2): the Hilbert cube of 2^K primes p_eps
(Lemma 5.2, Gowers-monotonicity, cites Tao-Vu (11.7)) lives in the
p-aspect; the bilinear shift form (5.7)
r_{eps,h} = p_0 h + sum_k (h-k) eps_k v_k -- whose (h-k) factor makes
r_{eps,h} independent of eps_h at h = k and so drives the alternating
cancellation and the 2^{-K} amplification (5.8) -- exists only because
the shift was dilated; the per-prime linearization (5.13) uses
omega = sum_p 1_{p|.} (their (1.1)); the variance dichotomy
((5.18)/(5.20) vs (5.21), packaged as Theorem 5.1) then contradicts
rationality. For S the summand's argument is the prime-count index n,
which admits no exact arithmetic self-map: no analogue of (5.2) can be
derived, so the cube, the amplification, and the dichotomy are all
unreachable.

O2 (formal-layer closure; why the formal linear layer admits no second
family). SCOPE (payloads/item-0005-adjudication-v1.md P6): this rigidity result
classifies the LINEAR formal layer only -- linear functionals
sum_m beta_m g_m of the gap sequence. Polynomial/nonlinear consequences
of rationality (e.g. products b^2(delta_{n+u}-delta_n)(delta_{n+v}-delta_n)
in Z, R2's observation) are integer but are NOT linear gap functionals
and are NOT classified by this theorem; O2 makes no nonlinear no-go
claim. The nonlinear evidence for the verdict is separate: the funnel
finding that every EXAMINED nonlinear repair architecture (including
translation cubes, R1's angle 1 / the dossier's own rank-1 observation
below) lands in EXCH'-type requirements (O4). Closure topology
(specified per R2's formal complaint): the closed Z-span is taken in
the sense of coefficientwise limits of finite integer combinations of
{delta_j} -- no norm or convergence structure beyond this is invoked or
needed. Stress-tested rigidity theorem (angles C3 and C6, independently
proved and independently re-derived by checker agents, and re-derived a
third time by R1 via the one-generator argument below): every linear
functional sum_m beta_m g_m of the gap sequence that rationality of S
certifies into a lattice uniformly over integer-gap models lies in this
closed Z-span of the translated tails {delta_j}; any functional with
infinitely many vanishing coefficients (every decimation or sparse
sampling) collapses to a finite integer gap combination. Consequently
the exact congruence families rationality supplies unconditionally are
{b delta_n in Z}_{n>=s} together with its deductive closure. That
closure does contain one genuine two-parameter family -- the tail
periodicity frac(delta_{n+l}) = frac(delta_n) for ord_b(2) | l -- but
it is amplification-INERT: its second parameter acts by translation
(rank-1 shift form, digit coefficient identically 1), so alternating
cubes cancel only on gap-VALUE coincidences (configuration-gated),
and never buy the 2^{-K} scale gain that TaTe's dilation cube buys
through the (h-k) coupling. Decimations of the digit position exit the
lattice provably (they evaluate the gap generating function at z =
-1/2 or 2^{-1/a}, unconstrained by rationality); the 2-adic mirror
carries zero formal linkage; base change and products factor through
the value S. A second family outside the closure would require an
exact prime-specific identity linear in dyadically weighted gap
windows -- an exact functional equation for n -> p_n under an index
self-map -- and none exists (p_{2n} - 2 p_n is asymptotic-only, with
error incompatible with any mod-1 lattice tolerance).

R1 sharpening (adopted, payloads/item-0005-adjudication-v1.md P7, steering
re-verified): the recursion delta_n = 2 delta_{n-1} - g_n makes
b delta_s in Z forward-generate the whole family {b delta_n in Z}_{n>=s}
automatically -- the family is deductively equivalent to the single
congruence b delta_s in Z. Rationality therefore supplies exactly ONE
lattice bit on the formal layer; everything downstream of it is
translation. The tail periodicity strengthens correspondingly to
b delta_n == 2^{n-s} b delta_s (mod b), verified directly from the
recursion. This is the arithmetic content behind "amplification-INERT"
above: TaTe's gain comes entirely from (5.2), a genuinely new
arithmetic input via omega's functional equation, which has no
counterpart in the abstract gap model.

O3 (engine reach; value-position vs count-position). The analytic
engine's interface is Theorem 3.1: two-point correlations of 1-BOUNDED
MULTIPLICATIVE functions, shifts h_1 != h_2 up to O(L^c), progression
restriction W in [L^c], natural averaging outside a log-density L^{-c}
exceptional-scale set -- used in Section 5 only at (5.42)-(5.45), to
decorrelate the sieve events "no prime factor in J_l" at two shifts.
SCOPE (payloads/item-0005-adjudication-v1.md P3, sustained against v1): Theorem
3.1 itself classifies no numerators, and the interface excludes
nothing a priori -- TaTe feed it only auxiliary completely multiplicative
sieve indicators g_l(p) = 1_{p not in J_l} at (5.43)-(5.45), introduced
late, not omega(n) directly. The dossier's claim is narrower and about
KNOWN reductions only: every known reduction reaching the engine does
so through additivity-type covariance (f(pm) = f(m) + c_p - sparse,
bounded weights, Mertens-mass variance floor sum_{p in A, p <= R} 1/p
>> (log_3 x)^2) -- hence binary digit support at positions determined
by prime VALUES for every reduction examined. No alternative reduction
of S terminating in admissible auxiliary correlations is exhibited,
and every one examined in this stress-test funnels into an (E2')-type
requirement (O4). Likewise the (loglog x)-point control clause below is
claimed only for the reductions examined, not as a classification of
the interface (R2's cube-order observation is correct and consistent
with TaTe's own architecture: formal term count, here 2^K shifts, is
not the same as required correlation order, which the algebraic cube
structure reduces to two points).

S and every carrier of its data (p_n, g_n, delta_n) are
prime-COUNT-position objects; the reindexing m = p_n multiplies tails
by the unbounded factors 2^{m - pi(m)}, so no single denominator makes
the count lattice commensurable with any value lattice found for the
examined reductions. Bridge-class definition (replacing the v1
overclaim, payloads/item-0005-adjudication-v1.md P2): call a map a
RATIONALITY-TRANSFERRING bridge if it is an exact identity expressing S
as a function of a count-indexed quantity (here T = sum_p 2^{-p}) such
that rationality of S would force rationality of that quantity. Exact
count<->value identities of a WEAKER kind do exist as reindexings --
e.g. S = sum_m 2^{-pi(m)} (Section 2, C1) -- and are not claimed
impossible; what is claimed is only about the transfer-lemma class just
defined. Within that class, the product formula on Z[1/2]
(|z|_R |z|_2 >= 1 for z != 0) shows: any bridge of the defined kind
would already force rationality of T = sum_p 2^{-p}, which is
unconditionally false (its digits are the aperiodic prime indicator) --
i.e. a successful bridge in this class would BE a proof of #251, not a
TaTe feed. This closure statement, not a blanket impossibility claim,
is the load-bearing content of O3's bridge argument. Gap functionals
also sit two structural levels beyond Theorem 3.1's interface for every
reduction examined: they are prime-indicator (not multiplicative)
correlations, and the examined reductions need (loglog x)-point control
where TaTe themselves state that even three-point equations "would
require ... a version of Theorem 3.1 for triple correlations, which
does not appear to be within current technology" (Remarks 4.2, third
bullet).

O4 (the exact unconditional residue). After O1-O3, the stress-test
localized everything the transfer question still needs to ONE
configuration statement, now stated in its general (EXCH') form
(payloads/item-0005-adjudication-v1.md P4, CONSTRUCTIVE GAIN adopted from R2).
Exchange lemma, general form (EXCH'; the C4 configuration EXCH below is
its normal form, not its definition; STATED HERE AS A FINDING, not
adopted into chain-v1): if S = a/(2^s b) (b odd) and a prefix argument
has forced delta_t = delta_u for indices t, u >= s (via (E1)+(E4)+(E5)
below, or any other route to the same conclusion), then ANY
configuration at offset L with
  (E2') |sum_{1<=i<=L} (g_{t+i} - g_{u+i}) 2^{-i}|
        > 2^{-L} |delta_{t+L} - delta_{u+L}|
(a dominant weighted word difference at matched context) contradicts
rationality of S. The Hamming-distance-1 case -- a single differing
gap flanked by matching prefix and suffix windows -- is the NORMAL FORM
used for the certificates below, not the only admissible configuration;
average separation, several controlled differences, or other
weightings of (E2') all suffice equally. Its normal-form instantiation,
EXCH (produced by angle C4, proof re-derived independently twice, and a
third time by R1): if there are indices n, m >= s+1 with
  (E1) g_{n+i} = g_{m+i} for 1 <= i <= J   (J-prefix match),
  (E2) g_{n+J+1} != g_{m+J+1}              (one differing gap; the
       Hamming-distance-1 case of (E2')),
  (E3) g_{n+J+1+i} = g_{m+J+1+i} for 1 <= i <= K  (K-suffix match),
  (E4) delta_{n+J}, delta_{m+J} <= D and
       delta_{n+J+K+1}, delta_{m+J+K+1} <= 2^K,
  (E5) b(D-2) < 2^{J+1},
then contradiction. (Proof: (E1) + chain-v1 Lemma 2.4 put
b(delta_{n+J} - delta_{m+J}) in 2^{J+1}Z; (E4)+(E5) force
delta_{n+J} = delta_{m+J}; the Lemma 2.2 subtraction at offset K+1
with (E3) gives 0 = d_1/2 + 2^{-(K+1)}(Delta_end). Gaps are even, and
delta_n = sum_{i>=1} g_{n+i} 2^{-i} >= 2 UNCONDITIONALLY for n >= 1,
every contributing gap being >= 2 (chain-v1 two_le_delta); hence
each of the two end-tails in Delta_end lies in [2, 2^K] and
|Delta_end| <= 2^K - 2 < 2^K, giving |d_1| <= 2^{-K}(2^K-2) < 1 sharp
(this closes R2's |d_1| <= 1 observation, sustained against the v1
proof prose which asserted the bound without stating the lower tail;
R2's parity patch |d_1| >= 2 -- d_1 is a nonzero difference of even
gaps -- is also valid and gives the same contradiction). EXCH_b for all
odd b implies S irrational with NO Hypothesis A and NO Hypothesis B;
EXCH_1 alone implies item-0010 (S not in Z[1/2]). Requirements (E1),
(E3), (E4), (E5) are UNCONDITIONALLY suppliable at the needed depths
J, K ~ log2 log x (word repetition: Chebyshev + Markov + pigeonhole,
capacity O(sqrt(log x)) by direct product count and ~ log x/loglog x
on gap-capped sites, both far above the need; tails: Markov selection,
delta <= O_A(log x) off density 1/A); the same three blockers below
apply verbatim to the general clause (E2'), not only to its
Hamming-distance-1 normal form -- none of them is sensitive to how the
word difference is distributed across the window, only to whether ANY
sufficiently weighted difference at matched context can be produced
unconditionally.

THE WALL IS CLAUSE (E2') -- exactness is RELATIVE TO THE LATTICE LAYER,
not a global necessity claim (payloads/item-0005-adjudication-v1.md P4,
R2 sustained: EXCH is proved sufficient; necessity beyond the lattice
layer is not proved and is not asserted here). R1's contraposition
gives the correct framing: WITHIN the lattice layer, rationality of S
forces sandwich rigidity at typical matched-flank pairs (the middle
gap value is pinned by its two-sided context), so a tail-dominant
weighted word difference at matched context is the only contradiction
lever available THERE -- this is a statement about what the lattice
layer's own structure permits, not about every conceivable route to
irrationality. No unconditional statement in the evidence base produces
two tail-typical indices satisfying (E2') at the needed depth. Pigeonhole
is structurally blind to variability ("sandwich rigidity" cannot be
refuted by counting); prescribing a distinct, sufficiently weighted
middle-window difference at fixed matched sides is a parity-blocked
tuple-type lower bound -- Maynard 1405.2593's Section 3 limitation
remark and footnote 1 are cited here as a statement about the
UNCONDITIONAL TOOL CLASS (well-distribution hypotheses cannot force
gap patterns), not as a statement about the primes themselves (R2's
caveat, adopted); and the quantitative Shiu-string route is circular
(site density (2q)^{-exp(Cm)} at m ~ (2/log 2) loglog x forces tail
depths that exceed the string length by an exponential level).

Summary sentence answering acceptance_intent: the exact structural
obstruction is the absence of any exact non-translational self-map of
the prime-count index -- equivalently, of any exact intertwiner
(Phi, u) with sum_h g_{Phi(n,h)} 2^{-h} = u delta_{tau(n)} +
exactly-known sparse correction for a non-translational position map
Phi -- which TaTe possess for omega as (5.2) via additivity and which
is provably (rigidity, O2, linear layer only) not manufacturable for S
on the formal linear layer; the residual unconditional gap, relative to
that lattice layer, is the exchange-supply statement (E2') of O4, a
two-site weighted word-correlation lower bound outside every
unconditional technique examined in the eight texts -- not a proven
necessity over all possible reductions. No unconditional transfer plan
is exhibited in the evidence base; the sharpest CONDITIONAL bridge is
EXCH', which is strictly weaker than the chain's Hypothesis A + B
package.

BET-07 relevance (resolve_by 2026-08-08, "unconditional progress",
p = 0.03): this verdict is evidence AGAINST unconditional progress via
the TaTe route; note that EXCH/certificates below are understanding
progress, not unconditional theorem progress. Resolution is the
operator's call.

## 2. Axis A1 -- dilation axis (primary; lead hypothesis STRESS-TESTED)

Lead hypothesis (CLAIM-A1): rationality of S yields exactly one
unconditionally available exact congruence family (the translated
family), and no transformation produces a second, dilation-like one.
Deliverables (i)-(iii) of the kickoff:

(i) First Section-5 step with no p_n-analogue: the (5.2)-derivation
    (O1). (5.1) itself transfers verbatim (chain-v1 Lemma 2.3).
    Independently confirmed by the tate-irrat extraction agent's
    step-by-step anatomy (its commentary reached the same step blind).

(ii) Existence of ANY dilation-like family for delta_n: REFUTED up to
    deductive closure, by six independent falsification angles, each
    ending in a proof or a precise wall (all verdicts survived
    max-effort precision-checks; C1/C5 checker verdicts REPAIRED =
    sentence sharpened, verdict upheld):
    - C1 duality/role reversal (pi(p_n) = n, S = sum_m 2^{-pi(m)},
      T = sum_p 2^{-p}): closed by the product-formula lemma (O3);
      boundary terms joining index-scale to value-scale weights
      (kernel 2^{n-p_n}) are lattice-empty; an in-class bridge would
      prove #251 outright. By-product identities: S = sum_m 2^{-pi(m)};
      sum_m pi(m) 2^{-m} = 2T; sum_{m>=1} 2^{-pi(2m)} = S/2 - 3/4
      (evenness of gaps; affine in S, no new family).
    - C2 Pratt-style position engineering: Pratt's exact head
      omega(N+k) = omega(k) + 1 (argument factorization
      N+k = k(n_0 Q/k + 1), additivity, primality of the cofactor;
      Pratt Prop 2.1) has no gap analogue -- g_{N+k} is indexed by
      prime count, no construction of the index pins gap values. The
      strongest unconditional trap -- run-gaps == 0 mod 2^d from
      Maynard 1405.2593 Thm 3.3 (d+1 consecutive primes congruent
      mod 2^d), forcing delta_{N+d} >= 2^d/b -- SELF-DEFEATS: the
      theorem's diameter clause p_{n+m} - p_n <= eps log x forces
      d 2^d <= eps log x, holding the forced bound a factor >= d/eps
      below the generic forward tail delta ~ log x (ratio -> 0 on
      constructible sites; empirically <= 3.11 below 1e8). The
      (0,2)-trap is dead a priori (delta_n >= 2). Single-site
      engineering reduces to the finite per-(s,b) exclusions already
      on record (chain-v1 8.4).
    - C3 decimation/combinations/2-adic/base change: rigidity theorem
      + trichotomy (O2); kernel moves (c_m, c_{m+1}) -> (c_m + 2t,
      c_{m+1} - 4t) generate the full annihilator (Gauss's lemma on
      2x - 1); 12/12 exact-arithmetic numerics, independently re-run.
    - C4 configuration family: see O4; also corrected two prior
      steering presumptions (repetition supply and tail control are
      NOT walls -- see Axis A3).
    - C5 engine retargeting: value/count-position dichotomy (O3);
      every engine-reachable X decouples from S; pullback route
      "engine-compatible f with sum (p_n - f(n))/2^n rational" is
      CIRCULAR (it presupposes the second family CLAIM-A1 denies).
      By-product: the TaTe engine retargets unconditionally to subset
      series X_A = sum_{p in A} 1/(2^p - 1) for any A with Mertens
      mass sum_{p in A, p <= R} 1/p >> (log_3 x)^2, including
      gap-DEFINED A such as {p_n : g_n <= 2 log p_n} [kappa
      bookkeeping UNVERIFIED]; still value-position, no #251 content.
    - C6 wildcard (ScPu cross-elimination base-2, theta/psi transport,
      numeration systems, ergodic-exact): second rigidity proof; ScPu
      double wall (window localization costs Cramer-type input;
      aligned-denominator vacuity -- the recursion IS the
      cross-elimination); the near-miss periodicity family (O2) found
      and shown amplification-inert.

(iii) Obstruction as a precise sentence: the summary sentence of
    Section 1 (intertwiner form), with O2 (rigidity, linear layer) as
    its formal-layer proof and O4/(E2') as the lattice-layer-relative
    residual.

## 3. Axis A2 -- engine interface

Theorem 3.1 hypotheses (verbatim-anchored): g_1, g_2: N -> C 1-bounded
MULTIPLICATIVE; either (i) equidistributed case -- g_1 real, (3.1)
sum_{N<n<=2N, n==a (mod q)} g_1(n) = (N/q) delta_N + O(N L^{-1}) for
all a, q, plus technical (3.2) g_1(p) = 1 on
exp(log^{1/11} X) <= p <= exp(log^{1/10} X) -- or (ii) non-pretentious
case (3.3); conclusion (3.4): correlation at shifts h_1 != h_2 =
O(L^c), modulus W in [L^c], natural averaging, error L^{-c}, all
scales N in [sqrt X, X] outside an exceptional set of log-density
L^{-c}.

Kickoff-presumption corrections: shifts are NOT fixed integers --
uniformity up to O(L^c) is exactly what lets Section 5 use shifts of
size << HKP ~ exp((1+o(1)) log_3^3 x) (their (5.32)) on progressions
of spacing Q << log^{o(1)} x (their (5.34)). What IS fixed is the
number of correlated points: two. TaTe: three-point equations are
already beyond current technology (Remarks 4.2, third bullet).

Violated by gap/delta functionals: MULTIPLICATIVITY of the correlated
functions (the binding clause; gap carriers are prime-indicator
correlations = Hardy-Littlewood territory; 1-boundedness and the
equidistribution axiom are not the binding issues), and the two-point
limitation vs the needed ~ log2 log x-point control. Theorem 3.1 is
consumed in Section 5 ONLY at subsection 5.14 ((5.42)-(5.45)):
decorrelating the completely multiplicative sieve functions
g_l(p) = 1_{p not in J_l} at two distinct shifts, for the very large
primes p > R_+ = x^{1/100} inside kappa_3; final input a Selberg sieve
count in progressions to moduli r = O(log^c x).

Benchmarks: TaTe Subsection 1.3: "In the absence of the prime tuples
conjecture, known distributional results such as those in [37], [3]
turned out to be too weak for our purposes." [3] = Charamaras-Richter
arXiv:2412.17583v2, [37] = Mangerel arXiv:2306.09929v4 (Discrete
Anal. 2024). TaTe do NOT itemize the failing property; the following
delta is INFERENCE from the benchmark texts: CR25 Theorem A has only
(log_3 N)^{1/2}/(log_2 N)^{1/6} savings (own stated ceiling
1/sqrt(log_2 N), Erdos-Kac), logarithmic averaging on the correlation
side, shift exactly h = 1, k >= 3 open (their Conjectures 1.3-1.5);
Mangerel Theorem 1.1 is qualitative log-density-0, rate-free, fixed
affine data, ineffective (Remark 1.2 flags the Cesaro upgrade as out
of reach). Theorem 3.1 (via Pilatte's decoupling, their Theorem 3.3,
gain V^{0.51 J'} vs trivial V^{J'}) supplies precisely the four
missing properties: log-power savings, shift uniformity to L^c,
W-restriction, natural averaging outside exceptional scales. Pilatte
interface (2310.19357v2 Theorem 2.4 / Theorem 1.1): shifts are always
tied to the divisibility d | n, output is an l^1-averaged correlation
over prime-product shift tuples; multiplicativity of lambda is
consumed only at two boundary steps (their Section 2.3 remark); "This
appears to be best possible with current methods" (abstract). No
prime-indicator-class statement is emitted anywhere in the engine
stack -- the interface reading is unambiguous; the kickoff's
Helfgott-Radziwill descent was not needed.

## 4. Axis A3 -- sieve/subset axis

Inventory (anchors): Maynard 1311.4600 -- k FIXED relative to x
(Section 3 notation convention); engine Props 4.1-4.3; Theorem 1.1
liminf(p_{n+m} - p_n) << m^3 e^{4m}; no k-uniform statement in the
paper. Maynard 1405.2593 -- the k-uniform engine: Theorem 3.1
(k <= (log x)^alpha, >= C^{-1} delta log k primes among k admissible
forms, good-site density >> #A(x)/((log x)^k exp(Ck)); Moreover
clause: CONSECUTIVE primes at cost exp(Ck) -> exp(Ck^5) for
k <= (log x)^{1/5}, |b_i| <= (log x) k^{-2}); Theorem 3.2 (>> log y
primes in y-windows down to y = (log x)^eps); Theorem 3.3 (m+1
consecutive primes == a (mod q), diameter <= eps log x, count
>> pi(x)/(2q)^{exp(Cm)}, m <= c_eps log_2 x); limitation remark +
footnote 1 (Section 3): Hypothesis-1-type well-distribution cannot
force gap patterns. Lau 2604.15042 -- uniform-in-k UPPER bounds
(Theorem 1.1: i.o. n with Omega(n+k) <= C log k for ALL k >= 2;
improvement O(k) -> O(log k) over TaTe's Theorem 1.1 second-moment
route, via GPY weights with decaying levels R_k = x^{c/k^50},
exponential-moment concentration (2.2)). TaTe Section 2 -- smoothed
GPY product sieve of dimension ~ (1/C_0) log_2 x; theorem-level anchor
Polymath [45, Prop 4.2] (Maynard [40] cited only generically).

Findings (two steering presumptions corrected by the stress-test):
(a) Repetition of consecutive gap words is UNCONDITIONALLY FREE
    (elementary): restrict to start-sites whose length-L window gaps
    are all <= A log x (all but o(1) of sites by Chebyshev + Markov,
    since sum_{n<=N} g_n ~ p_N ~ N log N); the realized word space is
    then <= (A log x/2)^L = x^{o(1)} for L = O(log x/log_2 x), so
    below every x some word of length L recurs on x^{1-o(1)} site
    pairs. Depth capacity ~ log x/log_2 x dwarfs the operative need
    J, K ~ log2 log2 x. No sieve input needed; consecutiveness is
    free because these are selection, not construction, arguments.
(b) Tail control at sites is NOT a wall: Markov selection supplies
    delta <= D = O_A(log x) off density 1/A, closing all EXCH gates
    (E4)/(E5) at J = ceil(log2(b D)), K = ceil(log2 D). Cramer-type
    pointwise input (Hypothesis-B-shaped) is required only under a
    sieve-first order of quantifiers (sparse sieve sites first, tails
    second) -- an order-of-quantifiers artifact, not a machinery
    requirement.
(c) What the sieve axis CANNOT supply is exactly (E2') (see O4): the
    parity problem enters not at consecutiveness (a negative
    condition, upper-bound-sieve territory) and not at counts, but at
    PRESCRIBING a distinct, sufficiently weighted middle-window
    difference at fixed matched sides -- a prescribed-tuple lower
    bound. Maynard16's own limitation remark is the published anchor,
    read as a statement about the unconditional tool class (Section 1
    revision), not about the primes themselves. The kickoff's expected
    blocker ("parity kills sieve asymptotics"; "consecutiveness") is
    hereby sharpened: existence-only outputs DO suffice for everything
    except the exchange clause.
(d) Reference consumer item-0010 (S not in Z[1/2]): reduces to EXCH_1
    (one exchange configuration per s). The direct delta_n < 4 route
    stays blocked (it needs runs of near-twin gaps at prescribed
    early positions -- same (E2)-type wall); the EXCH_1 reduction is
    strictly easier and is the recommended reformulation target.
    Verdict for A3 per kickoff option: route to a new item (F2/F6
    below), no unconditional sub-target reachable from the eight
    texts.

Numerical reality of EXCH configurations (b = 1; primes to 1e8;
independently re-run and verified): class counts grow superlinearly --
(J,K,D) = (4,5,30): 12 / 178 / 1287 classes at x = 2e6 / 2e7 / 1e8;
(5,5,34): 2 / 21 / 143; first (6,6,64) pair at 1e8. Inline
certificate (5,5,34), gate b(D-2) = 32 < 2^6 = 64: site n at gap index
5049413, primes 86930887, 86930897, 86930903, 86930927, 86930929,
86930939, 86930941, 86930953, 86930957, 86930969, 86930989, 86930999,
86931001 -- word prefix [10,6,24,2,10], middle 2, suffix
[12,4,12,20,10], delta_{n+J} = 6.307, delta_{n+J+K+1} = 17.678; site m
at gap index 5566504, primes 96411391, 96411401, 96411407, 96411431,
96411433, 96411443, 96411451, 96411463, 96411467, 96411479, 96411499,
96411509, 96411527 -- same prefix and suffix, middle 8,
delta_{m+J} = 9.356, delta_{m+J+K+1} = 20.793; d_1 = -6, identity
residual 4.4e-16; a rational S = a/2^s with s + 1 <= 5049413 would
force |d_1| < 1. Second certificate (6,6,64): anchors 74863199 (gaps
[8,12,12,6,4,18 | 8 | 6,4,2,10,18,2]) vs 41357909 (same sides, middle
38), d_1 = -30, residual 1.8e-15. These certify that exchange
configurations exist in nature and proliferate; what is missing is
only a THEOREM that they persist at all depths (clause (E2) supply).

## 5. Axis A4 -- Cramer-model cross-check

Lau Section 7 ("Conditional Falsity of Erdos Problem #679") schema:
unconditional density theorem (Tenenbaum-type pi_k lower bound, his
Theorem 7.2) + Cramer-window conjecture (his Conjecture 7: every
window (x - C log x sqrt(log_2 x), x] meets the omega-dense set; or
weaker Conjecture 8 with window (log(x/2))^d) + elementary conversion
=> conditional refutation (his Theorem 7.3); his Lemma 7.1
(Borel-Cantelli in the Bernoulli model) MOTIVATES the window
conjectures and is not used in the deduction. Full-text search:
Lau never mentions #251, sum p_n/2^n, or growing-numerator series.

Mirror finding: the project's Hypothesis B is EXACTLY a Cramer-window
conjecture in Lau's format -- A = primes, window W(x) = C log^2 x
("every (x - C log^2 x, x] contains a prime" <=> eventual pointwise
g_nu <= C (ln p_nu)^2) -- and chain-v1 Lemma 4.4 (B => delta_nu <=
3 C_g (ln p_nu)^2) is the exact analogue of Lau's elementary
conversion step. Lau's Lemma 7.1 applied to the gap Bernoulli model
(P(prime at n) = 1/log n) gives a.s. limsup g_n/(log p_n * log p_n)
<= 1 -- the model-side justification of B, with the same epistemic
status as Lau's Conjectures 7/8. VERDICT: Lau Section 7 is a
published methodological precedent for precisely the conditional-usage
pattern of Hypothesis B (window conjecture + model-side Borel-Cantelli
justification + elementary conversion); it supports the
respectability of B's role in the chain; it yields size control only,
no mod-1/digit content; it neither derives nor weakens B. Post-EXCH
note: the stress-test shows the chain's B-dependence is itself
removable (EXCH needs no B; Markov tails replace Lemma 4.4 at the
sites) -- recorded as follow-up F1/F6, no chain change made here.

## 6. Motivation re-base (kickoff method correction 2, executed)

The quote "unlikely ... at our current level of understanding of
analytic number theory", carried by roadmap/item-0005.md and
dossier/literature.md item 8(b) as TaTe's limitation statement, is
ABSENT from arXiv:2512.01739v2: hyphenation-robust full-text search
finds zero hits for "unlikely" and for "at our current level". It is
VERSION-SPECIFIC (v1/HTML provenance, not re-verifiable from the
dossier). v2 anchors to use instead:
- Remark 1.2 (after Theorem 1.1 = Erdos #248): the small-k omega-
  barrier cases are "of comparable difficulty to the prime tuples
  conjecture (or the Sophie Germain conjecture ...)".
- Remarks 4.2, third bullet: a triple-correlation version of
  Theorem 3.1 "does not appear to be within current technology".
- Subsection 1.3: the "[37], [3] ... too weak for our purposes"
  sentence (Section 3 of this report).
v2 never mentions Erdos #251 or sum p_n/2^n; the sharpest published
statement of our obstruction remains indirect (the two anchors above),
and this report (Section 1) now carries the exact statement.
Operator action suggested (NOT executed here): update the motivation
note in roadmap/item-0005.md and literature.md item 8(b) via the
roadmap workflow.

## 7. UNVERIFIED register

U1. Benchmark "too weak" itemization (Section 3): inference from the
    benchmark texts; TaTe do not itemize. 
U2. C5 by-product (subset series X_A, gap-defined A): engine kappa
    bookkeeping asserted by analogy, not re-executed; UNVERIFIED.
U3. C6's coincidence redirect (rationality + g << p^0.525 => i.o.
    exact coincidences delta_n = delta_m) uses Baker-Harman-Pintz,
    OUTSIDE the eight anchored texts: flagged, not load-bearing for
    the verdict (no other stress-test result relies on out-of-dossier
    material; the C4 check explicitly audited this).
U4. PSLQ/integer-relation exclusions (C1, heights 1e50/1e25; C3
    scans): numerical exclusion, not proof.
U5. Extraction-layer TRANSCRIPTION-UNSURE flags (kept with the
    volatile extraction files; the ones touching quoted anchors):
    TaTe scale-hierarchy (5.30) strength glyphs; TaTe kappa_4 display
    P^M vs R^M (possible paper typo, harmless under (5.30)); Pratt
    (3.3) exponent 3K^2 vs 3K; Lau Conjecture 8 window
    (log(x/2))^d glyph; Maynard15 (8.15)-(8.17) from text layer.
    None is load-bearing for Sections 1-5.
U6. Rigidity theorems (O2), product-formula lemma (O3), EXCH lemma
    (O4), and the C2 self-defeat argument: session-proved by
    max-effort agents AND independently re-derived by separate
    checker agents (plus steering's own re-derivation of EXCH), with
    exact-arithmetic numerics; NOT yet blind-reviewed outside this
    session. Review gate below.
U7. Inherited open flags unchanged by this item: Hardy-Wright theorem
    number (chain-v1 Lemma 2.1); Tao/Alfaiz forum verbatims resolved
    earlier by operator screenshot (literature.md addendum).

## 8. Follow-up item candidates (described only; NO items created,
## NO chain-v1 changes, NO Lean changes made by this item)

F1. EXCH kernel adoption: assess replacing the chain-v1 8.1 kernel
    ordering by EXCH < two-word variance < Hypothesis A (EXCH needs
    neither A nor B); would amend chain-v1 (blind-review gate per
    project practice). Content: the O4 lemma + supply analysis.
F2. Anti-rigidity target (the sharpest new attack surface): prove the
    combinatorial statement "#realized L-words at gap-capped sites
    exceeds #realized side-pairs, L ~ 3 log2 log x", which implies
    (E2) supply by pigeonhole -- a counting statement about word
    diversity, possibly weaker than any tuple conjecture; even its
    Cramer-model version (where EXCH holds a.s. with x^{1-o(1)}
    pairs) is currently informal.
F3. item-0010 re-scope: restate the goal as EXCH_1 (kill each
    denominator 2^s via one exchange configuration) instead of
    delta_n < 4 i.o.; strictly easier, certificate-backed at small
    depth.
F4. Motivation re-base execution (Section 6): roadmap/item-0005.md
    and literature.md 8(b) via the roadmap workflow; flag the v1
    quote as version-specific.
F5. Lemma bank: preserve the session identities and rigidity
    statements (S = sum_m 2^{-pi(m)}; sum_m pi(m) 2^{-m} = 2T;
    sum_{m>=1} 2^{-pi(2m)} = S/2 - 3/4; rigidity theorem; kernel-move
    annihilator; product-formula bridge lemma; periodicity family +
    inertness; EXCH + certificates) as a dossier appendix before the
    scratchpad expires.
F6. C5 by-product write-up (optional, low priority): unconditional
    irrationality of subset series sum_{p in A} 1/(2^p - 1) for
    Mertens-mass gap-defined A, after verifying kappa bookkeeping
    (U2) -- a small standalone result adjacent to TaTe's own "other
    sets A" remark; value-position, no #251 content.

## 9. Review response (v2)

The Section 9 (v1) review gate was executed: two adversarial reviews of
the verdict payload (Section 1 + this document), R1 (Fable, fresh
instance, falsification attempt no. 7) and R2 (ChatGPT, cross-family),
both against the same payload, both blind to each other. Full
adjudication: payloads/item-0005-adjudication-v1.md. Disposition, credited by
point:

- R1 found NO defect: it independently re-derived EXCH (including the
  delicate 2^{J+1} divisibility), sharpened O2 with the one-generator
  observation and the mod-b tail periodicity (both adopted into O2
  above), and supplied the contraposition framing (adopted into O4).
- R2 found FIVE scope defects, four sustained as WORDING overclaims
  (P1, P3, P4, P6) with the intended narrower claim already present in
  the v1 text one clause away, and one sustained as a genuine gap in
  the v1 proof prose (P5, the |d_1| bound). R2 also supplied the
  (E2') weighted generalization (P4), adopted as the definition of
  EXCH' above, with the old (E2) demoted to its normal form. R2's O3
  "bridge impossible outright" challenge (P2) is sustained as worded;
  the dossier's own C1 by-product identities are exact count<->value
  reindexings, so the bridge claim is narrowed to a formally-defined
  transfer-lemma class (O3 above) for which the #251 closure argument
  is unaffected. R2 found no defect in EXCH's mathematical content, in
  the rigidity theorem's core claim, or in the eight-text anchor
  register.
- Neither review challenges any of the eight paper anchors, the
  numerical certificates (Section 4), or the core computations. The
  mathematical core (EXCH/EXCH', the rigidity theorem, the
  product-formula lemma) now has three independent confirmations:
  the executor proofs, R1's re-derivations, and steering's own
  Lean/manual checks (payloads/item-0005-adjudication-v1.md preamble).

Both reviews are registered as hashed payloads: payloads/item-0005-
review-r1-fable.md, payloads/item-0005-review-r2-chatgpt.md (sha256 in
payloads/HASHES.txt).

## 10. Review gate (v1, executed; see Section 9 for disposition)

Per kickoff: one fresh-instance blind review of Section 1 (verdict)
only, probe-axis text detached, is RECOMMENDED before this verdict is
treated as load-bearing for BET-07 resolution or public phrasing;
operator decides whether to spend it. The highest-value review
targets are the rigidity theorem (O2) and the EXCH supply/wall
analysis (O4), which carry the most novel deductive weight. EXECUTED
(v2): see Section 9 for the disposition of both reviews.
