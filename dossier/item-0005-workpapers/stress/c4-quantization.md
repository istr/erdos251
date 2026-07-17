# C4 stress-test: the configuration-gated family (chain-v1 Lemma 2.4)
# Unconditional supply audit + the exchange reduction

Status: stress-test deliverable, 2026-07-17. Angle C4 of the item-0005
CLAIM-A1 falsification sweep. Evidence base: scratchpad/extract/maynard15.md,
maynard16.md, lau.md; session1-steering-notes.md; dossier/chain-v1.md.
Everything not from these is derived below with proof-level care or flagged.
Numerics: exch_scan.py, exch_growth.py, exch_cert.py in this directory,
primes to 1e8.

## 0. Executive summary

CLAIM-A1 is NOT falsified, but its C4 diagnosis is WRONG in two of its three
clauses and must be corrected:

1. The "configuration gate" of the Lemma-2.4 family is unconditionally OPEN:
   repeated consecutive-gap prefixes of length J(x) up to c log x / loglog x
   exist below x by pure pigeonhole (Chebyshev-level input, no sieve),
   infinitely often, J -> infinity. The second family's index set is NOT the
   supply problem.
2. The tail-size requirement (ii) does NOT need Cramer-type control. Average
   (Markov/Chebyshev) tail control -- delta_nu <= C log x outside a set of
   index density 1/A -- closes every size gate of the fork-merge machinery at
   2-adic depth J, K = O(loglog x), because the machinery only needs tails at
   FOUR sites and those can be selected typical. Cramer-type pointwise
   control (chain-v1 Hypothesis B) is needed only when sites are handed over
   by a SIEVE (sparse-first, select-later); selection-first arguments get
   tails for free.
3. The actually missing step is a single, precisely statable existence
   statement (EXCH below): two tail-typical indices whose consecutive-gap
   words agree on a J-window before and a K-window after ONE position where
   they differ, with J,K ~ log2 log x. This is strictly weaker than
   chain-v1's Hypothesis A + B package (no prescribed words, no pointwise gap
   bound, no two-sided counts), it is not a prescribed-tuple statement and
   hence not visibly parity-blocked, it is abundantly true numerically and in
   the Cramer model -- and no unconditional theorem in the evidence base
   implies it. That, and only that, is where the C4 route stops.

The expected obstruction sentence of the task brief ("consecutive-ness +
two-sided counts") is therefore refuted as a diagnosis: consecutiveness is
free for selection arguments (and even sieve-accessible: Maynard 1405.2593
Thm 3.1 "Moreover" clause, Thm 3.3), and two-sided counts are not needed for
any clause except the middle-difference clause, for which they are
sufficient but far from necessary. Precise final sentences in section 8.

## 1. Inventory: strongest unconditional configuration statements on record

From maynard15.md (Maynard, arXiv:1311.4600, "Small gaps between primes"):
- Prop 4.2 + Prop 4.3: for any admissible k-tuple H, infinitely many n with
  at least m+1 = ceil(theta M_k/2) of n+h_i prime; with Bombieri-Vinogradov,
  m+1 primes once k >= C m^2 e^{4m}. k is FIXED relative to x (Sec 3
  notation, verbatim in extraction). No consecutiveness, no control of WHICH
  h_i, no density-in-[x,2x] statement beyond "infinitely many".
- Thm 1.2: positive proportion of admissible m-tuples realize the m-tuples
  conjecture. Same limitations.

From maynard16.md (Maynard, arXiv:1405.2593, "Dense clusters"):
- Thm 3.1: k-uniform to k <= (log x)^alpha; >= C^{-1} delta log k of k
  linear forms prime at >> #A(x)/((log x)^k exp(Ck)) points n.
- Thm 3.1 "Moreover" clause: same with the primes CONSECUTIVE, for P = all
  primes, common slope a << 1, offsets |b_i| <= (log x)/k^2,
  k <= (log x)^{1/5}, at cost exp(Ck^5) in the count. So: unconditional
  strings of ~ log k CONSECUTIVE primes with prescribed CONTAINING SET of
  offsets -- but the realized sub-pattern (which b_i are the primes, hence
  the gap word) is NOT prescribed.
- Thm 3.2: >> log y primes in some length-y windows, >> x exp(-sqrt(log x))
  window sites, any y.
- Thm 3.3 (Shiu strings): m+1 consecutive primes all == a (mod q), diameter
  <= eps log x, uniformly m <= c_eps loglog x, q <= (log x)^{1-eps}, count
  >> pi(x)/(2q)^{exp(Cm)}; positive proportion of primes for fixed m, q.
  This is the strongest unconditional CONSECUTIVE-pattern theorem on record;
  the gap word is constrained only mod q and by total diameter, never
  pinned.
- Footnote-1 example after Thm 3.1 (extraction lines 161-167): Hypothesis-1
  style equidistribution alone can never force specific gap patterns (a
  Hyp-1-satisfying prime subset with no gaps of size 2 exists). Relevant
  below: pattern-prescription is not just unavailable, it is impossible at
  the axiom level the sieve machinery consumes.

From lau.md (Lau, arXiv:2604.15042): upper-bound configurations only
(omega(n+k) <= C log k for all k >= 2 at infinitely many n); the Section-7
Cramer-window schema produces one-sided window statements from conjectures;
nothing exact, nothing about equalities of gap words. No supply relevant to
Lemma 2.4 beyond motivation.

k-uniformity summary: maximal unconditional CONSECUTIVE string length is
O(loglog x) (Thm 3.3's m <= c_eps loglog x; Thm 3.1-Moreover's log k with
k <= (log x)^{1/5}), with site-density guarantees decaying like
(2q)^{-exp(Cm)} resp. (log x)^{-k} exp(-Ck^5).

## 2. The exchange reduction (new; supersedes the FM fork for this angle)

Notation as in chain-v1: g_n = p_{n+1}-p_n, delta_n = sum_{j>=1} g_{n+j}2^{-j},
delta_n >= 2 for n >= 1, Lemma 2.2 block identity, Lemma 2.3 lattice
(S = a/(2^s b), b odd, s >= 1 WLOG => b delta_n in Z for n >= s, even for
n >= s+1), Lemma 2.4 quantization.

LEMMA C4.1 (exchange contradiction). Let S = a/(2^s b), b odd, s >= 1.
Suppose there exist n, m >= s+1, J, K >= 1 and D >= 4 with:
 (E1) g_{n+i} = g_{m+i} for 1 <= i <= J            [prefix match]
 (E2) g_{n+J+1} != g_{m+J+1}                        [middle differs]
 (E3) g_{n+J+1+i} = g_{m+J+1+i} for 1 <= i <= K     [suffix match]
 (E4) delta_{n+J} <= D, delta_{m+J} <= D,
      delta_{n+J+K+1} <= 2^K, delta_{m+J+K+1} <= 2^K [tails]
 (E5) b(D-2) < 2^{J+1}                              [gate]
Then contradiction. Hence no such configuration exists for any rational S.

Proof. By (E1) and Lemma 2.4 (n, m >= s+1): b(delta_{n+J}-delta_{m+J}) in
2^{J+1} Z. By (E4) and delta >= 2: |delta_{n+J}-delta_{m+J}| <= D-2, so by
(E5) the multiple is 0: delta_{n+J} = delta_{m+J}. Now expand both by
Lemma 2.2 with T = K+1 and subtract; (E3) kills terms i = 2..K+1:
  0 = d_1/2 + 2^{-(K+1)} (delta_{n+J+K+1} - delta_{m+J+K+1}),
d_1 := g_{n+J+1}-g_{m+J+1}. By (E4), |delta_{n+J+K+1}-delta_{m+J+K+1}|
<= 2^K - 2, so |d_1| <= (2^K-2)/2^K < 1. But d_1 is a nonzero difference of
even gaps (indices >= 2), so |d_1| >= 2. Contradiction. QED

Remarks. (a) This strictly weakens chain-v1 Definition 3.1: no (+gamma,
-gamma) equal-sum fork, no coupling of gamma to 2^J beyond (E5), middle
length 1. (b) General-M version: replace (E2) by a length-M middle with
discrepancy d = (d_1..d_M) whose dyadic sum sum_i d_i 2^{M-i} != 0 (then
|sum_i d_i 2^{-i}| >= 2^{1-M} beats the forced bound < 2^{-M}); gate becomes
b(D'-2) < 2^{J+1} with D' >= the middle-inflated tail bound. M = 1 makes the
nonvanishing automatic; use it. (c) The contradiction step after the forced
equality is b-free.

DEFINITION (EXCH_b). For every s there exist n, m >= s+1 and J, K, D
satisfying (E1)-(E5) for this b [with D unrestricted, e.g. D = C log p_n and
J = ceil(log2(bD)), K = ceil(log2 D)].

COROLLARY C4.2. (i) EXCH_1 => S has no representation a/2^s: item-0010
target (S not in Z[1/2]) modulo nothing else. A SINGLE (E1)-(E5)
configuration with min(n,m) >= s+1 refutes the single denominator 2^s.
(ii) (for all b odd: EXCH_b) => S irrational. No Hypothesis A, no
Hypothesis B, no counting layer: chain-v1 sections 4-6 are replaced
entirely by the supply statement.

## 3. Supply audit against the task's three requirements

### (i) Repeated consecutive gap prefixes: UNCONDITIONALLY SUPPLIED

Pigeonhole, no sieve. Fix x, N = pi(x). Chebyshev (chain-v1 Lemma 2.1 cite):
sum_{nu<=N} delta_nu <= 6 C_0 N log N (proof: interchange, telescope
sum_{nu<=N} g_{nu+j} = p_{N+j+1}-p_{j+1} <= C_0(N+j+1)log(N+j+2), split
j <= N and j > N; the j > N block sums to O(1)). Markov: all but N/A
indices nu <= N have delta_nu <= 6 C_0 A log N =: D. At such sites every
window entry obeys g_{nu+i} <= 2^i delta_nu <= 2^i D, so the number of
distinct length-J words realized at controlled sites is at most
prod_{i<=J} 2^{i-1} D = D^J 2^{J(J-1)/2}. For J <= c log x/loglog x this is
< N/(2A): two (in fact x^{1-o(1)}) controlled indices share a length-J
consecutive-gap prefix. Infinitely often, J(x) -> infinity. Consecutiveness
is free: the words ARE segments of the actual gap sequence (selection, not
construction). Additionally Maynard16 Thm 3.3 + pigeonhole supplies
STRUCTURED repeats (all entries == 0 mod q) for fixed m, q at positive
density. So the "configuration gate" of the second family is open
unconditionally -- CLAIM-A1's C4 clause ("nonempty only where repeated gap
words exist", insinuating conditional supply) is true but inoperative:
repetition is not what is scarce.

### (ii) 2-adic depth J vs tail size: SUPPLIED ON AVERAGE, at the exact
### depths needed

The brief presumed "Cramer-type tail control" (delta <= 2^K at distance
J+2+K) is the bottleneck. False for this route. The machinery needs tails at
FOUR sites only, and Markov selection provides delta <= D = 6 C_0 A log N at
all but 4N/A indices (four conditions at fixed offsets). Choosing
K = ceil(log2 D) and J = ceil(log2 (bD)) closes (E4)-(E5) with total window
J+1+K ~ (2/log 2) loglog x + log2 b + O_A(1). At these window lengths the
word space has size exp(O((loglog x)^2)) = x^{o(1)}, so pigeonhole over
controlled sites yields x^{1-o(1)} indices sharing prefix AND suffix with
all four tail conditions -- i.e. clauses (E1)+(E3)+(E4)+(E5) hold
simultaneously for enormous families of pairs, unconditionally. Cramer-type
pointwise bounds enter chain-v1 only because its sites come from Hypothesis
A (sieve-prescribed, sparse-first): a sparse site family of density rho
cannot be intersected with a Markov-typical set unless rho > 1/A, and
enlarging A inflates D hence K exponentially in 1/rho (see section 4). The
order of quantifiers -- select-typical-then-classify vs
construct-sparse-then-hope -- is the entire content of requirement (ii).

### (iii) Infinitely often: YES for everything except (E2)

The pigeonhole families above exist below every x, with min index
-> infinity (choose the pair among indices > any s; the count x^{1-o(1)}
dwarfs any initial segment). What does NOT follow: that some pair in one of
these families has DIFFERENT middle gaps. That is clause (E2), the exchange
clause, and it is the unique unsupplied ingredient.

## 4. Why the known theorems cannot supply (E2)

(a) Pigeonhole is structurally blind to (E2). Rationality of S plus Lemma
C4.1 implies the following "sandwich rigidity": for every side-pair (u, v)
of lengths (J, K), ALL controlled sites carrying sides (u, v) have the SAME
middle gap. Rigidity is logically consistent with every counting fact used
in section 3 (it merely says the realized-word set is the graph of a
function of the sides); no pigeonhole can refute a statement that only
constrains WHICH words repeat, not HOW MANY.

(b) Sieve clusters output unprescribed patterns. Maynard15 Prop 4.2 and
Maynard16 Thm 3.1(+Moreover)/3.2/3.3 all deliver "at least m of these k
positions are (consecutive) primes" or "some word with entries == 0 mod q";
in every case the realized gap word ranges over an uncontrolled family. Two
runs of the same theorem may always realize the same word; nothing forces
variability at FIXED sides. Prescribing both words u.a.v and u.a'.v (which
would trivially give (E2)) is a prescribed-tuple lower bound -- exactly
what the parity problem blocks, and what Hypothesis A assumes.

(c) The sparse-site intersection wall (quantitative). To use Shiu strings
(Thm 3.3) as sites: needed window length J+K+1 ~ (2/log 2) loglog x forces
string length m >= that, so site density guarantee is
>> pi(x) exp(-exp(Cm) log 2q) = pi(x) exp(-(log x)^{Cc} log 2q). To
intersect with Markov typicality the exceptional density 1/A must be below
this, so A >= exp((log x)^{Cc'}), hence D = 6 C_0 A log N and
K = ceil(log2 D) ~ (log x)^{Cc'} -- but sieve strings have length only
O(loglog x) << K. Circular; the route closes. In words: sieve site
densities for length-m consecutive strings decay like exp(-exp(Cm)) while
the Markov tail budget tolerates only rarity 2^{-O(m)}; the mismatch is one
full exponential level and is invariant under all parameter juggling I
could find. For FIXED m, q the densities are positive and intersection
works -- but fixed m is below the gate (E5) forever (D <= 2^{J+1}/b needs
J ~ log2 log x growing).

(d) Parity: the precise placement. Consecutiveness is NOT intrinsically
parity-blocked: it is a negative condition, sieve-accessible by upper
bounds (Maynard16 delivers it unconditionally in the Moreover clause and
Thm 3.3), and selection arguments bypass it altogether. What parity blocks
is prescribed-word lower bounds (both fork words of chain-v1 section 5, or
u.a.v and u.a'.v here). But (E2) does not require prescription: it asks for
VARIABILITY at matched sides, an anti-rigidity statement quantified over an
x^{1-o(1)}-sized family. This is strictly weaker than any prescribed count
(Hypothesis A implies it with room to spare) and is not of the form the
parity obstruction speaks to. It is, however, a correlation statement about
two SITES of the gap sequence (agree sidewise, differ centrally), and no
current unconditional technology addresses inter-site word correlations at
all -- the structural analogy to TaTe holds at a higher level: TaTe's
second family came from an exact IDENTITY (free second parameter); ours
would come from an EXISTENCE statement (exchange supply), and identities
are unconditional while existences of this type are, today, not.

(e) Follower-dichotomy probe (best selection-side attempt to force (E2),
recorded because its failure mode is instructive). For a gap value v
occurring infinitely often let F(v) be the set of values w with (v, w)
occurring consecutively infinitely often; F(v) is nonempty by pigeonhole.
If |F(v)| >= 2 for some recurrent v, we get middle-variability at J = 1 --
useless, since gate (E5) at J = 1 needs tails D < 4 + 2/b, i.e.
twin-density futures, unavailable. If |F(v)| = 1 for ALL recurrent v, the
forced-follower orbit gives arbitrarily long PRESCRIBED repeated prefixes
(strengthening (i)) but never a divergence-with-remerge; and no PNT
contradiction arises because the eventually-thresholds n_0(v_k) grow along
the orbit, blocking full periodicity. Either horn lands exactly at the same
wall: variability is only obtainable where the gates are not, and matched
long windows around a divergence are obtainable nowhere. The irreducible
missing object is re-merge after divergence at controlled depth.

## 5. Numerical support (primes to 1e8; scripts in this directory)

Facts established by exch_scan.py / exch_growth.py / exch_cert.py:
- mean delta_nu ~ 15.7 at x = 2e7 (~ log x, as the Markov bound predicts);
  P(delta <= 4 log x) = 0.9999.
- Exchange configurations satisfying ALL of (E1)-(E5) with b = 1 exist and
  proliferate: at gates (J,K,D) = (4,5,30): 12 classes at x = 2e6, 178 at
  2e7, 1287 at 1e8 (superlinear in pi(x), as the collision count
  N^2/wordspace predicts); at (5,5,34): 2 / 21 / 143; at (6,6,64): first
  appearance at x = 1e8 (1 class). Latest-appearing pairs sit near x
  (e.g. anchor p ~ 97240609 at x = 1e8), supporting infinitude.
- Certificate at (6,6,64), b=1 gate 62 < 128: prefix [8,12,12,6,4,18],
  suffix [6,4,2,10,18,2], middles 8 vs 38 (d_1 = -30), at primes
  74863199... vs 41357909..., all four tails within gates; the Lemma 2.2
  subtraction identity checks to 2e-15. Under any S = a/2^s with
  s+1 <= min index (~ 2.5e6), Lemma C4.1 would force |d_1| < 1 against
  |d_1| = 30.
- The feasible window J+K at fixed x is capacity-limited by the entropy
  race: collisions die at J+K ~ 10 (x = 2e6) / ~11 (2e7) / ~12-13 (1e8),
  i.e. capacity ~ 2 log2 N / H2(gap distribution), which grows like
  log x/loglog x -- asymptotically far above the needed
  ~ (2/log 2) loglog x. The gates and the supply cross over permanently at
  moderate x; only clause (E2) at those scales is unproven.

Model check [derived, standard]: in a Cramer model every fixed side-pair
with sides of total length ~ (2/log 2) loglog x has conditional middle-gap
entropy >> 1, so EXCH_b holds a.s. with x^{1-o(1)} exchange pairs below x.
Rigidity is wildly false in the model; nothing known transfers this to the
primes.

## 6. Relation to chain-v1 (what this buys the project)

- EXCH is a new conditional route STRICTLY WEAKER than chain-v1's A + B:
  Hypothesis A alone implies EXCH_b for every b (realize u.a.v and u.a'.v as
  two admissible-set words via Lemma 4.3's argument), and B is not needed at
  all (Markov replaces it). Any future counting technology that yields
  anti-rigidity -- e.g. a lower bound for the number of DISTINCT length-L
  words realized at typical sites that exceeds the number of realized
  side-pairs -- proves irrationality outright through Lemma C4.1.
- Sharpest sub-target on offer (item-0010 route): EXCH_1. A single
  (E1)-(E5) configuration with min(n,m) > s kills denominator 2^s; the 1e8
  scan already re-derives (mechanically, and by a mechanism independent of
  chain-v1 8.4's 2-adic computation) exclusions up to s ~ 2.5e6.
- Suggested falsification target for future sessions: the anti-rigidity
  counting statement "#realized L-words at controlled sites >
  #realized (J,K)-side-pairs at controlled sites, L = J+1+K ~ 3 loglog x"
  -- a purely combinatorial statement about the gap sequence that implies
  EXCH by pigeonhole, prescribes nothing, and might be within reach of
  moment methods one day (it is a variance-type statement, cf. chain-v1
  8.3's two-word variance kernel; the kernel ordering of chain-v1 8.1
  should be extended by: EXCH < two-word variance < A).

## 7. What would falsify CLAIM-A1 from here

CLAIM-A1's operative clause ("no unconditionally-supplied second exact
family; no unconditional counterpart of amplification/dichotomy") would be
falsified by an unconditional proof of EXCH_b (or just EXCH_1 for the
item-0010 fragment). The exchange contradiction needs no Gowers-type
amplification and no variance dichotomy: the 2-adic lattice does the
amplification for free (depth 2^{J+1} from a length-J match). This session
could not prove EXCH and identified the exact reason (section 4); the claim
survives, re-diagnosed.

## 8. Precise final sentences (the deliverable)

1. The index set of the second family (chain-v1 Lemma 2.4) is
   unconditionally infinite: by Chebyshev + Markov + pigeonhole, for every
   large x there are x^{1-o(1)} pairs n, m <= pi(x) sharing a length-J
   consecutive gap prefix AND a length-K gap suffix separated by one middle
   position, with all four relevant tails delta <= D = O_A(log x), at
   depths J = ceil(log2 bD), K = ceil(log2 D); consecutiveness and
   two-sided counts are NOT the missing step.
2. The unbridgeable step, exactly: NO unconditional theorem (not Maynard
   1311.4600 Prop 4.2/Thm 1.1-1.4; not Maynard 1405.2593 Thm 3.1 with its
   consecutive "Moreover" clause, Thm 3.2, Thm 3.3; not Lau 2604.15042; not
   any selection argument) yields two such indices whose MIDDLE gaps
   differ (clause (E2)): sieve theorems output patterns from uncontrolled
   families and cannot force variability at fixed sides, prescribing both
   middle values is a parity-blocked prescribed-tuple lower bound, and
   sieve site densities exp(-exp(Cm)) for the required string length
   m ~ (2/log 2) loglog x lie one exponential level below the 2^{-O(m)}
   rarity budget that Markov tail-selection tolerates.
3. Consequently the C4 route reduces Erdos #251 to the single unconditional
   statement EXCH_b (section 2) -- strictly weaker than chain-v1's A+B,
   free of Cramer-type hypotheses, parity-agnostic, numerically abundant
   from x ~ 10^6 on -- and stops there; CLAIM-A1 survives with its
   diagnosis corrected from "configuration-gated supply of repeated words"
   to "unsupplied exchange (divergence-with-remerge) configurations".
