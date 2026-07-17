# item-0005 session-1 steering notes (first-hand read, NOT extraction-agent output)

Status: interim working notes, 2026-07-17. Author: steering, first-hand read of
2512.01739v2.pdf pages 44-58 (Section 5 complete) and 24-26 (Theorem 3.1 +
Theorem 3.3). These notes seed the A1/A2 sections of dossier/tate-transfer.md.
Integrity: PDF sha256 ce10e83b... matches payloads/HASHES.txt @ bf5de42 (all
eight anchors verified this session).

## 0. TaTe Section 5 anatomy (first-hand, exact anchors)

Standing assumption: q sum_{h>=1} omega(h)/2^h == 0 (mod 1) for some q >= 1
(rationality, for contradiction). All constants may depend on q.

- (5.1) [S5.1 "Shifting and dilating", p.45]: reindex h as n+h, multiply by
  2^n: q sum_{h>=1} omega(n+h)/2^h == 0 (mod 1) for ALL n in N.
  TRANSLATED congruence family. This is verbatim our lattice layer
  (chain-v1 Lemma 2.3: b delta_n in Z for n >= s).
- Additivity identity [p.45, unnumbered display]: omega(pn) = omega(n) + 1 - 1_{p|n};
  for p | n: omega(n + ph) = omega(n/p + h) + 1 - 1_{p^2|n+ph}.
- (5.2) [p.45]: for p | n:
  q sum_{h>=1} omega(n+ph)/2^h == -q delta_p(n) (mod 1),
  where (5.3) delta_p(n) := sum_h 1_{p^2|n+ph}/2^h (negligible correction).
  Derivation: the DILATION of the digit position h -> ph is ABSORBED into the
  argument division n -> n/p via additivity; the "+1" contributes
  q sum_h 1/2^h = q == 0 (mod 1). Result: a TWO-parameter congruence family
  indexed by (n, p), p | n -- new sampling patterns of omega landing in the
  SAME lattice.
- (5.4)-(5.7) [S5.2 "Taking an alternating sum", p.45-46]: Hilbert cube of
  primes p_eps = p_0 + eps_1 v_1 + ... + eps_K v_K, all 2^K distinct primes
  (eps in {0,1}^K). n obeys congruences (5.5) n == sum_k k eps_k v_k (mod p_eps)
  and (5.6) n > sum_k k|v_k|. From (5.2) with p = p_eps:
  shifts (5.7) r_{eps,h} := p_eps h - sum_k k eps_k v_k = p_0 h + sum_k (h-k) eps_k v_k.
  KEY: r_{eps,h} is independent of eps_h for 1 <= h <= K (coefficient (h-k)
  vanishes at k = h) -- the BILINEAR structure in (h, eps) exists only because
  the shift was dilated by p_eps. Alternating sum over eps kills terms h <= K.
- (5.8) [p.46]: q sum_h [sum_eps (-1)^{|eps|} omega(n + r_{eps,h+K})]/2^{h+K}
  == -q sum_eps (-1)^{|eps|} delta_{p_eps}(...) (mod 1).
  AMPLIFICATION: nontrivial mod-1 constraint at scale 2^{-K}.
- (5.9)-(5.13) [S5.3, p.46-47]: n random in [x/2,x] obeying (5.5),(5.33);
  apply e(t); errors kappa_1 (5.10) [p^2-correction], kappa_2 (5.11) [tail
  h > H]. Using (1.1) omega(m) = sum_p 1_{p|m}:
  (5.12) E e(sum_p X_p) = 1 + O(kappa_1) + O(kappa_2), with
  (5.13) X_p := q sum_{1<=h<=H} sum_eps (-1)^{|eps|} 1_{p | n + r_{eps,h+K}} / 2^{h+K}.
  PER-PRIME LINEARIZATION of omega into near-independent Bernoulli components.
- (5.14)-(5.21) [S5.4, Theorem 5.1, p.47-49]: partition primes
  S_0 (small: p | W or p = p_eps; X_p deterministic via congruences on n),
  S_1 (medium: p <= R), S_2 (large R <= p < R_+ and very large p > R_+).
  kappa_3 := (E|sum_{S_2} X_p|^2)^{1/2} (5.14); kappa_4 (5.16), kappa_5 (5.17)
  moment-comparison vs independent copies X'_p. If kappa_1..5 = o(1) (5.18)
  then sum_{S_1} Var X_p << sum kappa_j (5.20); but direct computation
  [S5.11, p.53] Var X_p ~ 1/(2^K p), Mertens:
  sum_{S_1} Var X_p >> (log_2 R - log_2 W)/2^K >> 1 (5.21). Contradiction.
  Theorem 5.1 [p.49] packages the whole reduction.
- (5.22)-(5.30) parameters [S5.5, p.49]: K = floor(2 log_4 x/log 2) (log_j =
  j-th iterated log; so 2^K ~ (log_3 x)^2), H = floor(log_3^2 x),
  M = 2 floor(log_2 x), H_+ = floor(log_2^2 x), P = exp(log_3^3 x),
  L = log^{1/log_3 x} x, R = x^{1/log_2^2 x}, R_+ = x^{1/100}.
  Scale hierarchy (5.30).
- Lemma 5.2 [p.50]: existence of the prime cube p_eps in [P/2, P] with all
  r_{eps,h+K} distinct; proof = Hilbert cube lemma via Gowers norms:
  ||f||_{U^1} >> 1/log P for the prime indicator embedded in Z/(5P)Z, Gowers
  monotonicity ([53, (11.7)] = Tao-Vu) gives ||f||_{U^K} >> 1/log P, so a
  random cube is all-prime with prob >= (c/log P)^{2^K}; collisions O(2^{2K}H^2/P)
  killed by (5.31). UNCONDITIONAL; no sieve.
- (5.32)-(5.36) [S5.6, p.51]: W := prod |r - r'| discriminant; n uniform in
  [x/2,x] with (5.5) + (5.33) n == 0 (mod W^flat); by CRT n lives in an AP of
  spacing Q << exp(log_3^{O(1)} x) (5.34); equidistribution (5.35)
  E f(n) = bar f + O(u ||f||_infty / x^{1-o(1)}) for u-periodic f, u coprime Q.
  (5.36) X_p = O(1/2^K) for non-small p.
- kappa estimations: S5.7 kappa_1 << 2^K(1/P + 1/2^H) [p.52]. S5.8 kappa_2:
  uses omega(n) << log n crudely for h > H_+, and E omega << log_2 R_+ +
  log(H_+ K P) via Mertens for H < h <= H_+ [p.52]. S5.9 kappa_4 << M(2pi)^M P^M x^{-(1-o(1))}
  [p.53]. S5.10 kappa_5 << exp(O(log_2 R/2^K) - M) [p.53]. S5.11 variance
  lower bound [p.53]. S5.12 splits kappa_3 into (5.39) large and (5.40) very
  large primes [p.53]. S5.13 large primes: periodicity pp' <= R_+^2, mean zero
  from alternating factor, EX_pX_{p'} = O(R_+^2/x^{1-o(1)}), diagonal
  << (log_2 R_+ - log_2 R)/2^K = o(1) [p.54]. S5.14 very large primes: reduce
  (5.40) to (5.41)/(5.42); partition (R_+, 2x] into L intervals J_l;
  (5.43) 1_{p|n} rewritten via g_l = completely multiplicative,
  g_l(p) = 1_{p not in J_l}; E_l (two prime factors in J_l) sparse (5.44);
  reduces to E(g_l(n + r_{eps,h+K}) - delta_{l,x})(g_{l'}(n + r_{eps',h+K}) - delta_{l',x})
  << log^{-c} x  [p.55] -- THE Theorem 3.1 call: equidistributed case,
  L-script = log^c x, g_1 = g_l, g_2 = g_{l'}, two DISTINCT shifts
  r_{eps,h+K} != r_{eps',h+K} of size << HKP ~ exp((1+o(1)) log_3^3 x) (5.32),
  AP-spacing Q << log^{o(1)} x (via (5.34)), W-condition ok. Final counting
  input: Selberg sieve for sifted numbers in APs to moduli r = O(log^c x) [p.55-56].

## 1. Theorem 3.1 verbatim interface (p.24)

Theorem 3.1 (A quantitative correlation estimate). X >= 2; g_1, g_2: N -> C
1-BOUNDED MULTIPLICATIVE functions; 1 <= L-script <= log X; delta_N real for
X^{0.4} <= N <= X; ONE of:
 (i) Equidistributed case: g_1 real-valued and for all X^{0.4} <= N <= X,
     a, q in N: (3.1) sum_{N<n<=2N, n==a (mod q)} g_1(n) = (N/q) delta_N + O(N L-script^{-1});
     plus technical condition (3.2) g_1(p) = 1 for
     exp(log^{1/11} X) <= p <= exp(log^{1/10} X).
 (ii) Non-pretentious case: delta_N = 0 and (3.3)
     exp(M(g_1; X^2, log^{1/125} X)) >> L-script.
Conclusion: exists exceptional set E subset [sqrt X, X] with logarithmic
density (1/log X) int_E dt/t << L-script^{-c}, such that for any W in [L-script^c]
and integers b, h_1, h_2 = O(L-script^c) with h_1 != h_2:
(3.4) (W/N) sum_{N<n<=2N} (g_1(n+h_1) - delta_N) g_2(n+h_2) 1_{n==b (mod W)}
      << L-script^{-c}  for all N in [sqrt X, X] \ E.

Remark 3.2 bullets [p.24]: qualitative version with LOGARITHMIC averaging was
[50, Thm 1.3] (non-pretentious) and [54, Thm 1.4] (equidistributed); natural
averaging outside exceptional set first in [51]; L-script^{-c} error terms
first by Pilatte [42] (L-script = log X, W = 1, model case lambda); "the
arguments here will rely heavily upon those of Pilatte". Special case:
uniform Chowla-type bound for lambda(a_1 n + b_1) lambda(a_2 n + b_2),
a_i, b_i in [1, (log N)^c], a_1 b_2 != a_2 b_1.
Theorem 3.3 [p.25] = Pilatte's decoupling inequality (gain V^{0.51 J'} over
trivial V^{J'}): sifted prime classes P_i in (H_0, H), sum_{p in P_i} 1/p <= V,
correlations of products (1_{n==b_p (mod p)} - 1/p) against g_1(n) g_2(n + sigma p_1...p_{J'}).

CORRECTION to kickoff A2 presumption: shifts in Thm 3.1 are NOT "fixed
integer shifts" -- they are uniform up to O(L-script^c) (polylog in X), which
is exactly why Section 5 can use shifts of size exp(log_3^3 x). What IS fixed:
the number of correlated points (TWO). Remarks 4.2 [p.44, third bullet,
first-hand]: even THREE-point equations like omega(n)=omega(n+1)=omega(n+2)
"would require ... a version of Theorem 3.1 for triple correlations, which
does not appear to be within current technology."

## 2. A1 findings (draft, pre-stress-test)

(i) EXACT FIRST STEP OF SECTION 5 WITH NO p_n-ANALOGUE: the derivation of
(5.2) from (5.1) -- the absorption identity
  sum_h omega(n+ph)/2^h = sum_h omega(n/p+h)/2^h + sum_h 1/2^h - delta_p(n).
(5.1) itself HAS an exact analogue (chain-v1 Lemma 2.3; the kickoff already
records TaTe (5.1) = our lattice layer). Everything after (5.2) consumes
(5.2)'s two-parameter structure: the cube lives in the p-aspect, the bilinear
shift form r_{eps,h} = p_0 h + sum_k (h-k) eps_k v_k requires the dilation,
the alternating cancellation requires the bilinearity, the 2^{-K}
amplification requires the cancellation.

(ii) DILATION-LIKE FAMILIES FOR delta_n -- candidate-by-candidate:
 (a) Index shifts / block identities (chain-v1 Lemma 2.1-2.2): the recursion
     delta_{n+1} = 2 delta_n - g_{n+1} and its iterates
     delta_n = sum_{i<=T} g_{n+i} 2^{-i} + 2^{-T} delta_{n+T} generate affine
     maps delta_n -> 2^T delta_n - (Z-combination of gaps). These stay inside
     the ONE-parameter translated family {b delta_n in Z}_{n>=s}; they are
     the (5.1)-analogue, not a dilation. The value-side doubling (mult. by 2
     = binary digit shift) is common to both problems and already exhausted.
 (b) Subsequence/AP-decimation of the digit position: extracting
     sum_j g_{n+aj+c} 2^{-j} (a >= 2) from the full series requires the gap
     generating function E_n(z) = sum_h g_{n+h} z^h at z = roots-of-unity
     combinations of 2^{-1/a} (e.g. a = 2: z = +-1/sqrt 2; alternating
     variant: z = -1/2). Rationality of S constrains ONLY z = 1/2 (all n).
     The values at -1/2 or 2^{-1/2} are independent reals not constrained by
     rationality of S. REFUTED as a congruence source.
 (c) The reason omega escapes (b): TaTe's dilated series sum_h omega(n+ph)/2^h
     NEVER decimates the weights -- the dilation acts on the ARGUMENT of
     omega (sampling omega along an AP) while weights remain 2^{-h} at full
     density, and additivity converts the dilated sampling into translated
     sampling of omega(n/p + .) BEFORE any generating-function evaluation is
     needed. The p_n-side counterpart sum_h g_{n+ph} 2^{-h} (AP-sampling of
     the gap sequence, full-density weights) has NO identity converting it to
     translated form: that would require an exact functional equation for
     the prime sequence under index dilation (p_{an+c} in terms of p_n),
     which does not exist -- even conjecturally, p_{2n} ~ 2 p_n (1+o(1)) is
     asymptotic only, with error incompatible with exact mod-1 lattice
     membership.
 (d) Position-semigroup framing (candidate obstruction sentence): the engine
     requires the position variable of the binary expansion to range over a
     semigroup (N under multiplication by primes) carrying an arithmetic
     action that the digit-generating function intertwines EXACTLY (omega's
     complete additivity up to the explicit correction (5.3)). For
     S = sum p_n/2^n the position variable is the prime COUNT; the index set
     carries no arithmetic self-map with an exact, lattice-compatible effect
     on gap windows. The only exact identities available are the linear
     recursion delta_{n+1} = 2 delta_n - g_{n+1} and iterates -- a
     one-parameter family. A second parameter would need a new exact
     functional equation for n -> p_n, which is not merely unknown: any
     candidate (dilation of index, dilation of position, base change)
     evaluates gap data outside the 2^{-h} lattice (see (b)-(c)).

(iii) NOTE for stress-test (next session): candidate exotic routes to attack
this claim adversarially:
 - exact identities pi(p_n) = n, p_{pi(m)} <= m (Legendre duality);
 - splitting S by residues of p_n mod small m (Dirichlet decomposition);
 - rewriting S as integer-indexed series: S = sum_m c(m)/2^{pi-ish(m)}?
   (role reversal with sum 2^{-p_n}, whose digits ARE integer-indexed);
 - ScPu11-style polynomial cross-elimination (different engine, no dilation);
 - base-2 vs other bases; carry structure.
 The stress-test must check each produces either (A) no new exact congruence
 family, or (B) a family that feeds a Gowers-type amplification. Claim to
 falsify: "no transformation of the delta lattice yields a two-parameter
 exact congruence family."

## 3. A2 findings (draft)

Theorem 3.1 hypothesis-by-hypothesis vs gap/delta functionals:
 1. "g_1, g_2 multiplicative on N": VIOLATED fundamentally. Gap/delta
    functionals are indexed by prime count, not by an integer argument; the
    natural integer-indexed carriers of gap information are prime-indicator
    correlations (n, n+t both prime, none between), i.e. von-Mangoldt-type
    correlations = Hardy-Littlewood tuples = exactly Hypothesis-A territory.
    The prime indicator is not multiplicative; 1-boundedness is not the
    issue, multiplicativity is.
 2. "1-bounded": satisfied by indicator-type carriers, VIOLATED by g_n or
    delta_n as values (size ~ log n / unbounded), but this is secondary --
    normalizing does not restore multiplicativity.
 3. Averaging/equidistribution axiom (3.1): prime indicator satisfies
    Siegel-Walfisz-type equidistribution to small moduli, so the AXIOM is
    not the obstruction; the CONCLUSION (3.4) for prime indicators at two
    shifts is the open problem (two-point correlations of primes).
 4. Two-point limitation: even for omega-type (bounded multiplicative)
    functions, TaTe state three-point correlations are beyond current
    technology (Remarks 4.2, p.44). Our delta_n windows involve
    ~log_2(1/tolerance) ~ log log x CONSECUTIVE gap constraints, i.e.
    (log log x)-point correlations of prime indicators, with uniformity --
    precisely Hypothesis A shape. Distance from current unconditional
    technology: two steps (multiplicative -> prime indicator; 2-point ->
    k-point with k growing).
 5. What TaTe actually need 3.1 FOR (important for verdict precision): only
    to decorrelate sieve-type events "n + r has no prime factor in J_l" at
    two distinct shifts -- smooth-number/rough-number events, 1-bounded
    multiplicative by construction (5.43). The gap analogue would be
    decorrelating "prime at position" events -- not sieve events. The engine
    interface is honest: it consumes multiplicative structure ONLY.

## 4. Version check (kickoff method correction 2) -- partial, first-hand

- p.44 Remarks 4.2 (third bullet) contains: triple correlations "does not
  appear to be within current technology" -- this is about 3-point
  extensions of Thm 3.1, NOT about growing numerators.
- The "unlikely ... at our current level of understanding of analytic number
  theory" v1-attributed quote: extraction agent grepping v2 full text;
  first-hand grep of section 5 pages found nothing of that form. PENDING
  agent confirmation for the full text.
- "of comparable difficulty to the prime tuples conjecture": expected in
  Section 1/2 (Erdos-Straus small k context). PENDING extraction agent
  anchor. Motivation citations in tate-transfer.md must be re-based on
  these v2 anchors.

## 5. Structural verdict skeleton (to be stress-tested before write-up)

The obstruction (draft one-sentence form): TaTe's unconditional engine rests
on enlarging the translated congruence family (5.1) to the two-parameter
dilated family (5.2) via the exact additivity of omega under argument
multiplication, and this enlargement is what feeds the Hilbert-cube
alternating amplification (5.8) and reduces the analytic input to two-point
correlations of 1-bounded MULTIPLICATIVE functions (Theorem 3.1); for
S = sum p_n/2^n the congruence family cannot be enlarged -- the index of the
series is the prime count, which admits no exact arithmetic action, every
candidate second parameter (index dilation, position decimation, base
change) exits the 2-adic lattice that rationality controls, and the analytic
carriers of gap information are k-point prime-indicator correlations with
k ~ log log x, two structural levels beyond Theorem 3.1 (multiplicative ->
prime indicator, 2-point -> growing-k-point). Hence: exact structural
obstruction at (5.2); no unconditional transfer; the conditional route
(Hypothesis A) is precisely the statement that replaces the missing engine.

Consistency cross-checks done: Pratt's conditional proof (per literature.md
item 8a) uses general linear forms a_k n + b_k in Conjecture 1.2 -- i.e. the
CONDITIONAL route also needs the dilated (a_k = p) structure, consistent
with (5.2) being the load-bearing step [PENDING pratt extraction agent
confirmation that a_k dilation mirrors (5.2)].

## 6. Post-extraction corrections and additions (2026-07-17, after workflow
## wf_f8592994-33c, 9/9 agents, full files scratchpad/extract/*.md)

1. VERSION CHECK RESOLVED: "unlikely"/"at our current level" ABSENT from the
   whole of v2 (hyphenation-robust search, tate-irrat agent). v2 anchors to
   use: Remark 1.2, p.3 ("of comparable difficulty to the prime tuples
   conjecture (or the Sophie Germain conjecture...)", context = omega-barrier
   cases small k = 1,2 following Theorem 1.1 = Erdos #248 Erdos-Straus);
   Remarks 4.2 third bullet, p.44 (triple correlations "does not appear to be
   within current technology"). v2 NEVER mentions #251 or sum p_n/2^n.
   The v1-attributed quote must be flagged version-specific in the report.
2. PRATT CORRECTION (kickoff and my sec. 5 presumed a_k = p): the dilated
   forms are L_k(n) = (Q/k) n + 1, k <= K, Q = prod_{p<=K} p^{2 ceil(log K/
   log p)} -- factorization trick n_0 Q + k = k(n_0 Q/k + 1), omega additive,
   primality of the cofactor pins omega(n_0 Q + k) = omega(k) + 1. So
   Pratt's second parameter is ALSO argument-multiplicativity + additivity
   of omega, not literally prime dilation. Endgame: integer-tail T(N) (= b
   times our delta_N at t = 2) trapped in (0,1) at ONE engineered N; NOT
   digit periodicity. Numerator-scale margin: t^K vs polyloglog numerators;
   growing numerator g ~ log n forces K ~ log log x, violating BOTH the
   Conjecture 1.2 window (K <= 100 logloglog x) and singular-series bound
   (2.5) S >= (log x)^{-1} (true only for triple-log K). TWO independent
   walls: structural (additivity) and quantitative (window scale).
3. BENCHMARKS IDENTIFIED: [3] = Charamaras-Richter arXiv:2412.17583,
   [37] = Mangerel Discrete Anal. 2024. Single "too weak" occurrence,
   Subsec 1.3, p.4, verbatim: "In the absence of the prime tuples
   conjecture, known distributional results such as those in [37], [3]
   turned out to be too weak for our purposes." NO itemization of the
   failing property in the paper -- any itemization in our report must be
   marked inference.
4. TaTe SECTION 2 (Erdos-Straus): Maynard [40] cited only generically;
   theorem-level anchor is Polymath [45, Prop 4.2] + Pintz [44]; sieve
   dimension floor((1/C_0) log_2 x) GROWS with x. Thm 3.1 unused in S2.
5. PILATTE INTERFACE (no HeRa descent needed): Theorem 2.4 (p.8) emits an
   l^1-in-shift-tuples averaged correlation bound over d = p_1...p_J | n,
   J ~ eps^2 loglog H, gain (V_1...V_J)^{1/2} vs trivial V_1...V_J;
   multiplicativity of lambda consumed ONLY in Prop 3.1 and Thm 2.4 =>
   Thm 1.1 (paper says so, p.3); spectral core lambda-free; "appears to be
   best possible with current methods" (abstract); shifts always tied to
   divisibility d | n; no prime-indicator statement anywhere.
6. NEW A1 OBSERVATION (mine, from re-reading chain-v1 through the TaTe
   lens): chain-v1 Lemma 2.4 (quantization) IS a multi-parameter congruence
   family on our side: b(delta_{n+J} - delta_{m+J}) in 2^{J+1} Z whenever
   n, m share a length-J gap prefix. Contrast with TaTe (5.2): TaTe's second
   parameter (p | n) is ALGEBRAICALLY FREE (available for every n and every
   p | n, unconditionally, by identity), while our (n, m, J) family is
   CONFIGURATION-GATED: its index set is nonempty only where repeated gap
   words exist -- exactly the existence statements that are Hypothesis-A
   territory (or, unconditionally, the A3 question: can Maynard16-type
   cluster theorems supply ANY of these configurations?). This sharpens the
   obstruction: the transfer does not lack a congruence STRUCTURE, it lacks
   an unconditional SUPPLY of index pairs for it. -> feed to stress-test C4.

## 7. Benchmark "too weak" analysis (A2 completion; itemization = INFERENCE)

TaTe's sentence (Subsec 1.3, p.4) names [37] Mangerel and [3] CR25 without
itemizing. From the extractions, the concrete deltas between benchmark
supply and Section-5 demand (LABEL AS INFERENCE in the report):
- CR25 (Charamaras-Richter 2412.17583v2): Theorem A savings are
  (logloglog N)^{1/2}/(loglog N)^{1/6} with an intrinsic Erdos-Kac ceiling
  1/sqrt(loglog N) (paper's own remark, p.3); LOGARITHMIC averaging on the
  correlation side; shift exactly h = 1, no uniformity; k >= 3 open
  (their Conjectures 1.3-1.5). Section 5 needs log^{-c} x savings, shifts
  up to ~exp(log_3^3 x), AP-restriction W, natural averaging outside
  exceptional scales.
- Mangerel (2306.09929v4): Theorem 1.1 is qualitative log-density-0, NO
  rate, all affine data fixed before the limit, ineffective (contradiction
  against scale subsequence); paper itself flags the Cesaro upgrade as
  out of reach (Remark 1.2, tied to Tao's log-averaged two-point theorem).
- Both are TWO-POINT results about omega/Omega-type values; neither has
  the shift-uniform, W-restricted, power-saving form. Theorem 3.1
  (via Pilatte's decoupling) supplies exactly these four deltas.

## 8. A3 draft findings (pre-C4-integration)

Unconditional configuration inventory (extraction-anchored):
- Maynard15 (1311.4600v3): k FIXED before N -> infinity (Sec 3 convention,
  p.4; negative finding: no k-uniform statement in the paper). Engine
  Props 4.1-4.3; Thm 1.1 liminf(p_{n+m}-p_n) << m^3 e^{4m}.
- Maynard16 (1405.2593v2): the k-uniform engine. Thm 3.1: k <= (log x)^alpha,
  >= C^{-1} delta log k primes among k admissible forms, good-n density
  >> #A(x)/((log x)^k exp(Ck)); MOREOVER-clause: consecutive primes at
  cost exp(Ck^5), k <= (log x)^{1/5}, |b_i| <= (log x) k^{-2}. Thm 3.2:
  >> log y primes in y-windows, y down to (log x)^eps. Thm 3.3: m+1
  consecutive primes == a (mod q) within diameter eps log x, count
  >> pi(x)/(2q)^{exp(Cm)}. LIMITATION (p.3 remark + footnote 1,
  anchor for the parity wall): well-distribution hypotheses CANNOT force
  gap patterns; "one cannot hope for much more than several of the
  L_i(n) are primes in P".
- Lau26: uniform-in-k UPPER bounds omega(n+k) <= C log k simultaneously
  for all k >= 2 at i.o. n (Thm 1.1) -- upper-bound window configurations
  via GPY weights with decaying levels R_k = x^{c/k^50}.
- TaTe S2: smoothed GPY product sieve with dimension ~ (1/C_0) log_2 x
  (k ~ loglog x uniformity for omega-events, not gap words).

What FM (chain-v1 Def 3.1) needs vs what this supplies:
(a) Gap-word REPETITION at fixed length (FM-P with same word): ELEMENTARY
    pigeonhole, no sieve needed: among n <= N, discard the <= N/2 indices
    whose length-m window contains a gap > 2m log N (Chebyshev mass:
    #{j <= N: g_j > T} <= p_N/T ~ N log N/T); remaining vocabulary
    <= (m log N)^m, so some word recurs >= (N/2)/(m log N)^m -> infty
    times. For each fixed m; diagonalization gives J_r -> infty pairs.
    So REPETITION IS NOT THE BLOCKER (new observation this session).
(b) FM-F FORK PAIRING: needs joint i.o. occurrence of two DISTINCT words
    agreeing outside a 2-slot middle with (+gamma, -gamma) exchange.
    Pigeonhole pairs same-word occurrences only (gamma = 0 excluded by
    FM gamma >= 2). Prescribing exact distinct words = prescribing the
    full primality/compositeness pattern of two windows = tuple-level
    lower bounds; Maynard16's own limitation remark (p.3 + footnote 1) is
    the published anchor that Hypothesis-1-type sieve inputs cannot force
    this. PRECISE BLOCK 1.
(c) FM-1 END-TAIL: delta_{n+L} <= 2^K at the construction sites is an
    infinite-tail pointwise bound; sieve statements say nothing beyond
    their finite window; within the eight texts there is NO unconditional
    g_m << p_m^theta (theta < 1) to even make delta_m finite-crude
    (Hoheisel/BHP would be operator payload, outside the dossier).
    PRECISE BLOCK 2 (independent of (b); Hypothesis-B-shaped).
(d) Sub-target item-0010 (delta_n < 4 i.o.): delta_n < 4 with g >= 2
    means excess sum (g_{n+j}-2) 2^{-j} < 2, i.e. a run of near-twin gaps
    at prescribed early positions -- same wall as (b) (individual gap
    values not sieve-forceable; cluster diameters (log x)^eps give
    average in-cluster gaps far above 4... avg ~ y/log y for y-windows).
    A3 verdict shape: "route to new item" = document blockers (b)+(c);
    no unconditional sub-target reachable from the eight texts.

## 9. A4 draft findings

Lau S7 schema: [unconditional density thm for a set A (Tenenbaum pi_k)]
+ [Cramer-window conjecture: every window (x - W(x), x] meets A
(Conj 7: W = C log x sqrt(log_2 x); Conj 8: W = (log(x/2))^d)]
+ [elementary conversion] => conditional refutation of #679 (Thm 7.3);
Lemma 7.1 (Borel-Cantelli in the Bernoulli model) MOTIVATES the window
conjectures, is not used in the deduction.
Mirror: Hypothesis B is EXACTLY a Cramer-window conjecture in Lau's
format: A = primes, W(x) = C log^2 x ("every (x - C log^2 x, x] contains
a prime" <=> eventual pointwise g <= C log^2 p). Lau Lemma 7.1 applied to
the gap Bernoulli model (P(prime at n) = 1/log n) gives a.s.
limsup g_n/(f(p_n) log p_n) <= 1 with f = log, i.e. the model-side
justification of B -- same epistemic status as Lau's Conjectures 7/8.
Chain-v1 Lemma 4.4 (B => delta_nu <= 3 C_g ln^2 p_nu) is the exact
analogue of Lau's step-(5)/(6) elementary conversion.
A4 verdict shape: Lau S7 is a PUBLISHED METHODOLOGICAL PRECEDENT for
precisely the conditional-usage pattern of Hypothesis B (window
conjecture + model-side Borel-Cantelli justification + elementary
conversion to pointwise/window bounds); it SUPPORTS the respectability
of B's role; it yields size control only, no mod-1/digit content; it
neither derives nor weakens B. Possible follow-up-item candidate: state
the weakest site-local form of B that FM needs (tail bound only at
constructed sites; cf. chain-v1 8.3 two-word variance).

## 10. A1 stress-test adjudication (workflows wf_23ef3752-97d + continuation
## wf_ad5d8443-991; detail files scratchpad/stress/*.md)

VERDICT ACROSS ALL SIX ANGLES: CLAIM-A1 SURVIVES every falsification
attempt; three angles produced PROOF-LEVEL strengthenings; one angle
(C4) produced a genuinely new reduction (EXCH) that revises the A3
diagnosis and yields the sharpest follow-up target of the whole item.

- C1 (duality/role reversal): closed with a product-formula lemma on
  Z[1/2] (|z|_R |z|_2 >= 1): every bridge between the count-indexed
  lattice and integer-indexed prime series (T = sum_p 2^{-p}, 2T, etc.)
  carries a weight-conversion boundary term (kernel 2^{n-p_n}) at 2-adic
  valuation exponentially below lattice resolution; an in-class exact
  bridge would already force rationality of T -- unconditionally false
  (aperiodic prime-indicator digits) -- i.e. would prove #251 outright,
  not feed TaTe. New exact identities recorded (I1-I4, e.g.
  sum_{m>=0} 2^{-pi(m)} = S; sum_{m>=1} 2^{-pi(2m)} = S/2 - 3/4 via
  evenness of gaps -- affine in S, no new family). Checker: REPAIRED
  (sharper sentence with explicit threshold p_n - n > log2 b), verdict
  upheld; PSLQ exclusions at height 1e50/1e25 [numerical, not proof].
- C3 (decimation/combinations/2-adic/base change): RIGIDITY THEOREM:
  a linear functional sum beta_m g_m is rationality-forced into a
  lattice iff beta_m = C 2^{-m} eventually (+ finitely many
  corrections), i.e. lies in the Z[1/2]-span of {delta_n} + finite gap
  combinations. Trichotomy T1 (prime-blind in the value S) / T2 (not
  rationality-forced) / T3 (inside the span). 2-adic mirror: ZERO
  formal linkage (perturbation 3*2^M Z dense in 2^M Z_2); f(z) = sum
  p_n z^n not rational; base change factors through the value S.
  TaTe evade the trichotomy only because additivity collapses a T2
  functional onto T3 on the graph of omega(pn) = omega(n)+1-1_{p|n}.
  12/12 exact-arithmetic numerics. [Check pending in continuation run.]
- C4 (configuration family) -- REVISES my sec. 8 draft:
  (1) repetition of consecutive gap prefixes: unconditionally supplied,
  J up to c log x/loglog x, x^{1-o(1)} pairs (Chebyshev+Markov+
  pigeonhole; my sec. 8(a) confirmed and extended).
  (2) MY BLOCK 2 (FM-1 tail control) RETRACTED as a wall: Markov
  selection (delta <= D = O_A(log x) off density 1/A) closes all tail
  gates with J = ceil(log2(b D)), K = ceil(log2 D) = O(loglog x);
  Cramer-type pointwise control is needed only under sieve-first
  quantifier order (an order-of-quantifiers artifact, not a machinery
  requirement).
  (3) NEW Lemma C4.1 (EXCH, exchange contradiction; steering
  re-verified the logic first-hand: Lemma 2.4 lattice-lock + block
  identity + |d_1| >= 2 vs < 1): S = a/(2^s b) AND indices n, m >= s+1
  with (E1) J-prefix match, (E2) g_{n+J+1} != g_{m+J+1}, (E3) K-suffix
  match, (E4) delta-bounds D and 2^K at the four sites, (E5)
  b(D-2) < 2^{J+1} => contradiction. STRICTLY WEAKER than FM Def 3.1
  (no equal-sum fork, no gamma smallness). EXCH_b for all b =>
  irrationality with NO Hypothesis A and NO Hypothesis B; EXCH_1 =>
  item-0010 (S not in Z[1/2]). THE WALL IS CLAUSE (E2) SUPPLY ALONE:
  two tail-typical indices agreeing on a J-window before and K-window
  after a single DIFFERING position. Pigeonhole is structurally blind
  to variability ("sandwich rigidity" is counting-consistent);
  prescribing two distinct middles at fixed sides is a parity-blocked
  tuple lower bound; sieve site densities exp(-exp(Cm)) sit one
  exponential level below the 2^{-O(m)} rarity budget for the needed
  m ~ (2/log 2) loglog x. My sec. 8 expected diagnosis
  "consecutiveness + two-sided counts" is REFUTED: consecutiveness is
  free; two-sided counts sufficient but unnecessary. Numerics: EXCH
  configurations (b = 1) proliferate to 1e8 (e.g. (J,K)=(6,6) pair at
  x = 1e8, residual 2e-15). Suggested kernel reordering:
  EXCH < two-word variance < Hypothesis A (EXCH needs no B).
  [Check pending.]
- C5 (engine retarget): every engine-reachable series is VALUE-POSITION
  (digit support at prime-value-determined positions, bounded weights,
  Mertens-mass variance floor sum 1/p >> (log_3 x)^2); S and all
  carriers of its data are COUNT-POSITION; the reindexing m = p_n
  multiplies tails by unbounded 2^{m - pi(m)}, so no denominator makes
  the two lattices commensurable; pullback route (i) (engine-compatible
  f with sum (p_n - f(n))/2^n rational) is CIRCULAR (it presupposes the
  very second family CLAIM-A1 denies). Checker REPAIRED taxonomy (new
  engine-side extension: congruence-constrained covariant weights give
  exact dilated families for hybrid value-position series like
  sum omega(m) 1_{p_0|m} 2^{-m} -- does not break CLAIM-A1), verdict
  upheld. BY-PRODUCT worth a follow-up note: TaTe engine retargets
  unconditionally to subset series X_A = sum_{p in A} 1/(2^p - 1) for
  any A with sum_{p in A, p <= R} 1/p >> (log_3 x)^2 -- including
  gap-DEFINED A like {p_n : g_n <= 2 log p_n} [kappa bookkeeping
  UNVERIFIED] -- the engine's maximal unconditional reach, still
  value-position.
- C6 (wildcard): second rigidity theorem (forced functionals lie in
  closed Z-span of translated tails; infinitely-many-zero-coefficient
  functionals collapse to finite combinations). ScPu base-2: double
  wall (window localization costs Cramer-type bounds; aligned-
  denominator vacuity -- the recursion IS the cross-elimination).
  NEAR-MISS family: frac(delta_{n+l}) = frac(delta_n) for
  ord_b(2) | l -- two-parameter, algebraically free, but inside the
  deductive closure and AMPLIFICATION-INERT (rank-1 bilinear form;
  TaTe's 2^{-K} gain needs the (h-k) coupling that only dilation
  provides). Redirect: rationality + g << p^{0.525} [BHP -- OUTSIDE
  the eight texts, must be flagged] forces infinitely many exact
  coincidences delta_n = delta_m; missing engine input is an
  ANTI-coincidence (two-word variance) theorem, not configuration
  existence. Wall sentence: S lacks an exact intertwiner (Phi, u) with
  sum_h g_{Phi(n,h)} 2^{-h} = u delta_{tau(n)} + exactly-known sparse
  correction for a non-translational position map Phi; the prime-count
  index admits no exact non-translational self-map; by rigidity no
  formal transformation manufactures one. [Check pending.]
- C2 (position engineering): first run died on credit outage (numerics
  scripts survive); re-run + check in continuation workflow. [Pending.]

CONVERGENCE NOTE: C3 and C6 rigidity theorems, C1 product-formula
lemma, and C5 value/count-position dichotomy are four independent
derivations of the same structural fact from four different toolboxes;
C4's EXCH localizes what remains after accepting it. The obstruction
sentence for the report should be assembled from: C6's intertwiner
sentence (the WHY), C3's trichotomy (the formal-layer closure), C5's
position dichotomy (the reach boundary), C4's (E2) clause (the exact
residual wall on the configuration side).
