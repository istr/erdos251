# C2 stress-test: Pratt-style position engineering -- attack on CLAIM-A1

Status: attack executed and FAILED to falsify CLAIM-A1. The single-site
(Pratt) route reduces provably to the finite denominator-exclusion
computation already on record (chain-v1 8.4); it is sound but non-uniform,
and every mechanism that would make it uniform is one of the known walls.
Author: C2 subagent, 2026-07-17. Evidence base: extract/pratt.md (Pratt
2409.15185v1), extract/maynard16.md (Thm 3.3), chain-v1.md, session1-
steering-notes.md, sibling files c1-duality.md / c3-decimation.md /
c4-quantization.md / c6-wildcard.md. Numerics (mine, this directory):
c2_depth_growth.py, c2_selfdefeat.py, primes to 1e8, exact where it matters;
predecessor scripts c2_synth.py, c2_residue.py, c2_runs.py re-run and
confirmed. Notation as in chain-v1: p_n n-th prime, g_n = p_{n+1}-p_n,
S = sum p_n 2^{-n}, delta_n = sum_{j>=1} g_{n+j} 2^{-j}, delta_{n+1} =
2 delta_n - g_{n+1}, delta_n >= 2 (n>=1); rationality S = a/(2^s b), b odd,
s >= 1 WLOG gives b delta_n in Z for n >= s, in 2Z for n >= s+1 (Lemma 2.3).

## 0. Executive summary and verdict

VERDICT: NO_TRANSFER. Pratt-style single-site position engineering supplies
no unconditional second exact congruence family and no unconditional
irrationality contradiction for S. What it supplies -- and all it supplies --
is, for each FIXED denominator (s, b), a finite arithmetic certificate that
that particular (s, b) is impossible: exactly the exclusion loop of chain-v1
8.4. It has no b-uniform engine, and each of the three natural ways to build
one is a named wall.

The reason is a clean structural mismatch with Pratt's proof. Pratt's engine
has two legs at ONE constructed index N = n_0 Q:
  (P-head) an EXACT head: omega(N+k) = omega(k) + 1 for k <= K, forced by
     the engineered factorization N+k = k(n_0 Q/k + 1) (needs k^2 | Q, a CRT
     construction on the argument) plus additivity of omega and primality of
     the cofactor. This collapses the head S_1 = b sum_{k<=K} omega(N+k)/t^k
     to the LOCATION-INDEPENDENT constant a + b/(t-1) + O(log K / t^K).
  (P-tail) a trapped tail: the middle/far tail is o(1) but bounded below by a
     single atypically-large value omega(N+K+1), landing the integer T(N) in
     (integer, integer+1). Contradiction.
For t = 2, t-1 = 1 so a + b/(t-1) = a + b is an integer and the entire
contradiction is carried by (P-tail): "fractional part of T(N) in (0,1)".

For S = sum p_n 2^{-n} both legs fail, independently:

 WALL 1 (no exact head). The tail numerator g_{N+k} is NOT a function of the
   arithmetic of any integer; it is a difference of consecutive primes
   indexed by the prime COUNT. No construction of the index N pins actual gap
   values, so the head b sum_{k<=K} g_{N+k} 2^{-k} cannot be collapsed to a
   location-independent constant. There is no analog of "prime => omega = 1".

 WALL 2 (residue engineering self-defeats). The ONLY residue data on gaps
   that touches the 2-adic lattice {b delta_n in 2Z} is gaps mod 2^d; residues
   mod odd m live at a decoupled place (C3 Prop M) and yield no tail
   information. The b-free way to pin the low bits is a string of d+1
   consecutive primes congruent mod 2^d (Maynard 1405.2593 Thm 3.3,
   UNCONDITIONAL, depth d up to ~ (1-eps) log2 log x). But Thm 3.3's diameter
   clause p_{n+m}-p_n <= eps log x forces the d run-gaps (each >= 2^d) to
   satisfy d 2^d <= eps log x, hence 2^d <= eps log x / d, while the forced
   lower bound delta_{n+d} >= 2^d/b sits against a forward tail delta_{n+d}
   that is GENERIC ~ log x (Thm 3.3 says nothing about forward gaps). Ratio
   2^d/delta_{n+d} <= eps/(bd) -> 0: the constructible deep site never beats
   its own generic tail. (Numerics: ratio -> 0 for tight strings; searched
   coincidental depth-4 sites cap at ratio 3.11 below 1e8, excluding only b in
   {1,3}.)

 WALL 3 (no tail bound + non-uniformity). Trapping delta_N strictly between
   two consecutive lattice points of spacing 2/b (the general parity trap)
   needs delta_N known to precision < 2/b: an exact head over T ~ log2(b) +
   O(1) positions AND a pointwise UPPER bound on the forward tail
   delta_{N+T}. The dossier contains no unconditional pointwise gap upper
   bound at all (session notes A3(c)); and even granting one, the trap is a
   per-(s,b) finite computation whose precision demand T ~ log2 b grows with
   b, with no engine to range over all (s,b) at once. Trapping into (0,2) is
   dead a priori: delta_N >= 2 (numerics min 2.35), so b delta_N >= 2b >= 2.

Pratt escapes the analogous non-uniformity because (P-head) is
location-independent: for the FIXED b of the rationality hypothesis, ONE
existence statement (n_0 exists in [1,x] for large x, via the tuples
conjecture) discharges the whole contradiction. The gap-side substitute for
"the magic n_0 exists" is a prescribed-constellation existence statement --
Hypothesis A. That is the missing input, and it is conditional.

## 1. The Pratt template, transcribed to the delta lattice

Pratt's reduction (pratt.md Sec 2.3) for numerator sequence c_n and base t:
assume alpha = sum c_n t^{-n} = a/b; then for every N,
   T(N) := b sum_{k>=1} c_{N+k} t^{-k} = b t^N (alpha - sum_{n<=N} c_n t^{-n})
is an integer. Engineer ONE N with T(N) provably in (integer, integer+1).

For t = 2, c_n = g_n this is exactly b delta_N (Lemma 2.3): rationality makes
b delta_N an integer (even, N >= s+1) for EVERY N -- the translated family.
The single-site program is: find ONE constructed N at which the actual
b delta_N is provably NOT an even integer, or is squeezed off the even
lattice. Two levers, mirroring (P-head)/(P-tail):

 (L-div)  b-free divisibility lever: force b delta_N == 0 (mod 2^d) by a
    construction independent of b, then delta_N >= 2^d/b. Contradiction if the
    actual (forward) delta_N < 2^d/b.
 (L-trap) general lattice lever: know delta_N to precision < 2/b via an exact
    head plus a forward-tail bound, then confine b delta_N to an open interval
    of length < 2 containing no even integer.

Both are single-index, Pratt-shaped. Sections 3-4 dispatch them. Section 2
records why the head that both want is unavailable.

## 2. WALL 1: the exact head has no gap analog

Pratt's head is exact because omega is a function of the integer N+k and the
construction pins that integer's factorization: N+k = k(n_0 Q/k+1) with
n_0 Q/k+1 prime, whence omega(N+k) = omega(k) + omega(n_0 Q/k+1) = omega(k)+1
(additivity + primality). Two facts about omega-as-a-function-of-its-argument
are consumed: complete additivity on coprime factors, and "prime pins the
value to its minimum 1".

The gap g_{N+k} = p_{N+k+1} - p_{N+k} is not a function of the arithmetic of
N+k, nor of any single integer. It is determined by the LOCATIONS of two
consecutive primes, i.e. by primality on a whole interval, and it is indexed
by the prime count N+k (which is pi(p_{N+k}), not an arithmetic argument).
Consequences:
 - No engineered index N yields a symbolic value for g_{N+k}. (One CAN compute
   g_{N+k} for a SPECIFIC known N = pi(x) by sieving near x, but that is
   computation of a specific site, not a location-independent identity; it
   drops us into the per-(s,b) finite loop of section 4, not a proof.)
 - Residue engineering (Dirichlet, CRT on values, Shiu/Maynard strings) can
   pin g_{N+k} mod m but never its value. And the only m that reaches the
   lattice is a power of 2 (section 3); pinning mod an odd m is q-adic data
   orthogonal to the 2-adic constraint (this is C3 Proposition M: the value-
   preserving kernel moves shift the odd-place data by an odd unit, so the
   real/rational lattice and the mod-m gap residues are formally independent).
This is the exact statement, for the head, of CLAIM-A1's "no dilation-like
exact family": Pratt's second, exact input (the additivity identity) exists on
the omega side and has no counterpart on the gap side (matching C3's T2=T3
collapse analysis and C6's "no exact non-translational self-map of the
prime-count index").

## 3. WALL 2: the value-residue lever (L-div) self-defeats

3.1 The identity (verified, c2_synth.py / c2_residue.py, both PASS). If the run
g_{N+1}, ..., g_{N+d} are all == 0 (mod 2^d) and b delta_N in Z, then
   b delta_{N+d} = 2^d (b delta_N) - b sum_{i=1}^d g_{N+i} 2^{d-i} == 0 (mod 2^d),
because each g_{N+i} 2^{d-i} == 0 (mod 2^{2d-i}) with 2d-i >= d. Since
delta_{N+d} > 0, b delta_{N+d} is a positive multiple of 2^d, so
   delta_{N+d} >= 2^d / b.                                             (3.1)
A site of "depth d" (equivalently d+1 consecutive primes congruent mod 2^d)
refutes any (s, b) with s <= N+d and b < 2^d / delta_{N+d}. This is the
strongest b-FREE single-site lever: r = 0 is the residue that maximizes the
forced lower bound, so nothing about the low-bit residue does better without
knowing b.

3.2 The unconditional supply of depth, and its built-in self-defeat. Depth is
unconditionally available: Maynard 1405.2593 Theorem 3.3 (verbatim,
maynard16.md 4.2) gives, for m <= c_eps loglog x, q <= (log x)^{1-eps},
(a,q)=1, at least pi(x)/(2q)^{exp(Cm)} primes p_n with
   p_n == ... == p_{n+m} == a (mod q)  and  p_{n+m} - p_n <= eps log x.
Take q = 2^d, m = d: a string of d+1 consecutive primes congruent mod 2^d,
depth d up to ~ (1-eps) log2 log x, UNCONDITIONALLY, at indices -> infinity.

But the same theorem's DIAMETER clause kills the lever. The d run-gaps are
each divisible by 2^d, hence each >= 2^d, so
   d 2^d <= sum of run gaps = p_{n+d} - p_n <= eps log x,   i.e. 2^d <= eps log x / d.
Meanwhile the forced bound (3.1) is compared against the ACTUAL forward tail
delta_{N+d}, which Theorem 3.3 does not constrain at all: it is generic,
delta_{N+d} ~ log x. Hence
   ratio := 2^d / delta_{N+d}  <=  (eps log x / d) / (c log x)  =  O(eps/d)  ->  0.
The constructible deep site's forced bound sits a factor ~ d/eps BELOW its own
generic forward tail. No contradiction; the lever self-defeats. (Rigorous
arithmetic in c2_selfdefeat.py: for log x in {20,50,100,500,1000} the max
constructible depth is 2,2,3,4,4 and the ratio is 0.20,0.08,0.08,0.032,0.016.)

3.3 Why searched sites do slightly better, and why it does not grow. A depth-d
run need not be diameter-tight; a coincidental run of large 2-adic gaps
followed by a small-gap tail gives ratio > 1. This is what a brute search
finds -- but it is precisely a two-part event (a high-2-adic run AND a small
forward tail co-located), i.e. a prescribed constellation, not a Theorem-3.3
output. Census to 1e8 (c2_depth_growth.py, c2_selfdefeat.py):
 - Max searchable depth is 4 below 1e8 (d=5 absent). Best-ratio site (chosen
   to minimize the forward tail): anchor p = 8218897, run gaps [16,48,32,16]
   (diameter 112 = 7 log x, NOT tight), forward gaps [2,10,2,10,14],
   delta_end = 5.14, ratio 3.11 -> excludes only odd b in {1,3}, and only for
   s <= that index.
 - The ratio distribution: at d=4 only 62.5% of the 24 sites even have ratio
   > 1, and 4.2% (one site) have ratio > 3; at d=3, 8.4% have ratio > 1; at
   d=2, 0.1%. Median forward tail at every depth is ~ 13-16 ~ log x: depth
   does NOT come bundled with a small tail.
 - Across cutpoints X = 1e6..1e8 the best ratio went 2.07, 2.20, 3.11, 3.11,
   3.11 -- it STALLED once depth stalled at 4. There is no unconditional
   mechanism forcing depth-with-small-tail to infinity; that is Hypothesis-A
   territory (co-located congruent string + twin-ish run).

Net: (L-div) unconditionally reaches only b in {1, 3} at present scale, and
its asymptotics for CONSTRUCTIBLE sites are ratio -> 0. It cannot beat a
growing b, and it settles only s <= (site index). This is the census
predecessor's finding, now given its mechanism (the Theorem-3.3 diameter
clause) and its rigorous asymptotic (ratio -> 0), correcting the census note's
open "IF n >= s" into a structural ceiling.

## 4. WALL 3: the general lattice lever (L-trap) is the finite exclusion loop

4.1 Trapping into (0,2) is impossible. delta_N = sum_{j>=1} g_{N+j} 2^{-j}
>= 2 sum 2^{-j} = 2 (all tail gaps of odd primes are >= 2), strictly > 2 in
practice (numerics: min sampled delta_n = 2.35). So b delta_N >= 2b >= 2 for
every odd b: the interval (0,2) is a priori empty of b delta_N. The assigned
sub-question "trap b delta_N in (0,2)" is answered NO unconditionally.

4.2 The general parity trap = per-(s,b) certificate. For FIXED (s,b), compute
the exact head H = sum_{i<=T} g_{N+i} 2^{-i} from primes near p_N (finite
sieve), so delta_N in [H, H + 2^{-T} B] once delta_{N+T} <= B; then b delta_N
in [bH, bH + b 2^{-T} B]. If this interval, of width b 2^{-T} B, has length
< 2 and contains no even integer, then b delta_N (even, N >= s+1) cannot exist:
(s,b) refuted. Width < 2 requires 2^T > bB/2, i.e. T > log2(bB) - 1. This is
EXACTLY the chain-v1 8.4 exclusion computation ("certified distance 2^{-18.2}
at width <= b*32*2^{-2000}"): a finite certificate per (s,b). It reaches
b <= 99999, s <= 1,857,459 on record. Two reasons it is not a proof, both
structural:
 (a) It needs a rigorous forward-tail bound B on delta_{N+T} (WALL 3 proper).
     8.4 gets B by extending the actual prime computation ~ 2000 gaps past N
     (so the tail beyond is <= 2^{-2000} * (largest computed gap)); this is a
     finite, sieve-bounded certificate. Unconditionally, the dossier has NO
     pointwise gap upper bound to bound delta_{N+T} beyond the computed range
     (session notes A3(c); Baker-Harman-Pintz g << p^0.525 is outside the
     dossier and, being polynomial-size, would need T ~ theta N -- a LINEAR
     window, useless, cf. C6 Wall 2.1). So the lever is intrinsically a
     bounded computation, not an asymptotic theorem.
 (b) It is per-(s,b) and the precision demand T ~ log2(bB) grows with b, so
     ever-larger b needs ever-deeper certified tails; there is no b-uniform
     engine. Covering all (s,b) would need a single existence statement
     producing, for each b, a site whose head + trapped tail lands off the
     lattice -- and pinning the head at an existence-only site is WALL 1, while
     pinning the tail small at that site is the co-located constellation of
     3.3, i.e. Hypothesis A.

4.3 The atypical-value Pratt lever also has no gap analog. Pratt's (P-tail)
needs ONE atypically LARGE numerator omega(N+K+1) to keep S_2 nonzero, and the
middle SMALL to keep it < 1. Large gaps exist unconditionally (Erdos-Rankin;
outside dossier), but a large gap g_{N+K+1} only LOWER-bounds delta (delta_N >=
2^{-K} g_{N+K+1}/2): it inflates b delta_N, and "large" traps no parity.
Trapping needs an UPPER bound on the tail delta_{N+K}, i.e. ALL forward gaps
small -- a run of near-twin gaps -- which is unconditional-tech-blocked (and
the small-tail half of 3.3's constellation). The asymmetry is exact: Pratt's
large-omega works only because his HEAD is already an exact constant, so a
provably-nonzero-but-small remainder completes an integer + (0,1) squeeze; with
no exact head, an atypical gap value gives a one-sided size bound and no
squeeze.

## 5. The assigned sub-attacks, itemized

(i) "Primes in residue classes pin p_n mod m on engineered subsequences --
   does any exact tail evaluation follow?" NO. Pinning p_{N+k} mod m pins
   g_{N+k} mod m. For m odd this is q-adic data decoupled from the 2-adic
   lattice (C3 Prop M); no tail evaluation. For m = 2^d it pins the low d bits
   of b delta_N to a residue r; the b-free optimum r = 0 gives only the lower
   bound (3.1), which self-defeats (WALL 2). No EXACT evaluation of delta_N
   ever follows: exact evaluation needs the whole forward gap sequence (no
   closed form for primes) or a two-sided trap (WALL 3). CRT across several
   odd moduli multiplies q-adic data that never re-enters the 2-adic place.
   Dirichlet/Linnik give one prime per class, not consecutive-prime control;
   consecutive control is Shiu/Maynard (WALL 2).

(ii) "Trap b delta_N in (0,2)": NO, delta_N >= 2 (4.1).

(iii) "Force parity contradictions at ONE constructed N": only as a per-(s,b)
   finite certificate (4.2), reproducing chain-v1 8.4; no b-uniform version,
   and the b-free divisibility version reaches only b in {1,3} at 1e8 (WALL 2).

(iv) Engineered arithmetic progressions of primes (Green-Tao) and prescribed
   residue PATTERNS: Green-Tao APs are not consecutive primes, so they pin no
   gap. Prescribing which residues consecutive primes occupy (hence gaps mod q
   as VALUES, not just == 0) is a prescribed-tuple lower bound -- parity-
   blocked (Maynard16 footnote 1: equidistribution cannot force gap patterns).
   Maynard16 Thm 3.1 "Moreover" gives consecutive primes inside an admissible
   offset set but leaves the realized sub-pattern (hence the gap word)
   uncontrolled: containing-set mod q, never the pattern.

## 6. Numerics summary (this directory)

 c2_synth.py (predecessor, re-run): run-divisibility identity (3.1) verified
   on a synthetic rational series; b delta_n integral (n>=s), even (n>=s+1);
   control (gaps 2,4,6) fails 2^3-divisibility as it must. PASS.
 c2_residue.py (predecessor, re-run): residue-pinning master congruence
   b delta_{n+J} == -b A_w (mod 2^{J+1}) over n in [s+1,s+19], J<=11, ALL
   PASS; pair-trap arithmetic forced for b in {1,3,5,85}. PASS.
 c2_runs.py (predecessor, re-run): census to 3e7, max depth d=4, best site
   [32,16,32,16]. Reproduced.
 c2_depth_growth.py (mine): census to 1e8, best-RATIO sites (tail-minimizing).
   Best ratios by cutpoint 1e6..1e8: 2.07, 2.20, 3.11, 3.11, 3.11 (stalls with
   depth). Best site excludes only odd b in {1,3}, s <= index.
 c2_selfdefeat.py (mine): (A) at depth d the forward-tail median is ~ log x and
   ratio>1 is a small-fraction coincidence (d=2: 0.1%, d=3: 8.4%, d=4: 62.5%);
   (B) deepest strings have forward tails from 5.1 (ratio 3.11) to 34.8 (ratio
   0.46) -- depth is uncorrelated with small tail; (C) min delta_n = 2.35 >= 2;
   (D) Maynard-tight construction gives ratio 2^d/delta -> 0 rigorously.

## 7. Verdict and the precise obstruction sentence

VERDICT: NO_TRANSFER. CLAIM-A1 SURVIVES angle C2, with its single-site
diagnosis sharpened: Pratt-style position engineering is not merely
"unavailable" but reduces provably to the sound-but-finite denominator
exclusion of chain-v1 8.4, and each of its three natural completions is a
named wall (no exact head; residue engineering self-defeats via the
Theorem-3.3 diameter clause; no unconditional tail bound + per-(s,b) non-
uniformity).

THE PRECISE OBSTRUCTION SENTENCE (deliverable). Pratt's contradiction at a
single engineered index N = n_0 Q rests on an EXACT head omega(N+k) =
omega(k)+1 -- forced by the argument-factorization N+k = k(n_0 Q/k+1) together
with additivity of omega and primality of the cofactor, which collapses the
head to the location-independent constant a + b/(t-1) so that one existence
statement discharges the whole trap for the fixed denominator b -- and for
S = sum p_n 2^{-n} this exact head has no analog because the tail numerator
g_{N+k} is a difference of consecutive primes indexed by the prime count, not a
function of the arithmetic of N+k, so no construction of the index pins gap
values; the only residue control that reaches the 2-adic lattice {b delta_n in
2Z} is congruence of the run-gaps modulo 2^d (unconditionally suppliable to
depth d ~ log2 log x by Maynard 1405.2593 Theorem 3.3), and that theorem's own
diameter clause forces d 2^d <= eps log x, holding the b-free divisibility
bound delta_{N+d} >= 2^d/b a factor ~ d/eps BELOW the generic forward tail
delta_{N+d} ~ log x, so the value-residue trap self-defeats (ratio 2^d/delta_N
-> 0 on constructible sites, empirically <= 3.11 -> b in {1,3} on searched
sites below 1e8); the alternative -- trapping delta_N strictly inside the
even-lattice spacing 2/b -- is impossible into (0,2) since delta_N >= 2, and
otherwise demands both a pointwise upper bound on the forward tail (absent from
the dossier's unconditional inventory) and a small-gap forward run co-located
with the congruent string, i.e. a two-part prescribed constellation that is
exactly Hypothesis A; consequently single-site position engineering yields only
the per-(s,b) finite certificate already recorded (chain-v1 8.4), sound but
carrying no b-uniform engine, and the missing input is precisely the
gap-side substitute for Pratt's "the magic index exists" -- a prescribed-
constellation existence statement of Hypothesis-A strength.

WHAT WOULD SUFFICE (minimal conditional form). A single-site proof needs an
unconditional statement of the shape: for every s and every odd b there exists
an index N >= s+1 with (a) g_{N+1..N+T} PRESCRIBED (or the head b sum_{i<=T}
g_{N+i} 2^{-i} pinned mod 2^{ceil(log2 b)+2}) and (b) a forward-tail upper
bound delta_{N+T} <= B with b 2^{-T} B < 2 placing b delta_N off the even
lattice -- i.e. an existence-of-configuration theorem giving simultaneously a
prescribed head window and a bounded (small) forward tail at one index of
arbitrarily large 2-adic depth. This is strictly Hypothesis-A shaped (prescribed
consecutive-gap data on a window plus a bounded tail), hence conditional; the
b-free specialization (Maynard Thm 3.3 depth) is unconditionally available but,
by the diameter clause, too weak by a factor d/eps. No object between "Maynard
Thm 3.3 depth" (too weak) and "Hypothesis A" (sufficient) is provided by any of
the eight dossier texts.

Relation to siblings: C2's single-site route is the s <= N, one-index
degeneration of C4's two-site exchange -- where C4 needs anti-rigidity (EXCH_b:
variability at matched sides), C2 needs the even weaker-looking but still
conditional "prescribed head + bounded tail at one deep index"; both bottom out
in configuration EXISTENCE, which rationality does not supply for free (C6
supplies coincidences delta_n = delta_m for free, but not prescribed ones).
C1/C3/C6 rigidity already forbid a purely-formal second family; C2 confirms the
prime-specific single-site escape is the finite exclusion and nothing more.

[END]
