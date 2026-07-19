# item-0019 final report -- local quotient census + relative
# extension empirics at matched flanks

Run: single-milestone measurement campaign per roadmap/item-0019.md
(status: ratified) and the item-0019 kickoff v1 as amended by the
v1.1 delta (parallel execution amendment).  EXECUTOR lane, local
machine.  Model string: claude-fable-5 (Fable 5), reasoning high.
Web OFF throughout (corpus-only; local code execution only, runs
rule 6).  Zero edits under lean/; no lake invocation.

## 1. Gates (kickoff Section 7; outputs verbatim)

Pin record (rule 17/18): git rev-parse HEAD at session start =
c3fc09a521640c1cae0c99ae47c051de9fb768b0 = the Section 0 pin of
kickoff v1 EXACTLY.  No bookkeeping delta was present; the rule-18
clause was not exercised (HEAD == pin, zero commits ahead); the
session pinned to HEAD = pin.  Worktree pristine before work except
the two ephemeral operator instruction files (kickoff v1 and the
v1.1 delta; never committed, not run writes, per their own headers
and kickoff Section 5).

Kickoff hashes (operator-side booking is canonical; no
dispatch-supplied value was transmitted in-session to verify
against, so the disk hashes are recorded here for the operator to
book at the apply):

    sha256(item-0019-kickoff-v1.md) =
      54810faba2aff697e1da7d0f175f39829e44c561cde9f6ad6204fb41161c1bcc
    sha256(item-0019-kickoff-v1.1-delta.md) =
      242651991479dabc51207dcfdab66cad3fd783147ca9b866fd6d6c308c85b448

AMENDMENT RECORD (v1.1 delta D0, verbatim duty): the delta was
received mid-run, after the Section 7 validity predicates and the
Section 2 anchor reading were complete and BEFORE any filter-layer
code, measurement, or table existed.  Application was therefore
fully prospective: every measurement of this report was produced
under the amended execution strategy (parallel workers, chunked
delta); no phase was re-executed.  Phase state at reception: A
(predicates only) partially complete; B, C, D not started.

Validity predicates (all satisfied at the pin, re-run at close --
Section 10):

    git rev-parse HEAD == Section 0 pin              PASS (exact)
    git status --porcelain clean modulo kickoffs     PASS
    python3 lean/scripts/blocks.py check-frozen      PASS
      ("FROZEN BLOCKS: all byte-identical."; erdos_251_irrational,
       HLQuantA, CramerGranville all OK)
    python3 lean/scripts/blocks.py relocation-check  PASS
      ("RELOCATION CHECK PASSED", concatenation sha256
       af4615e1c92c4c070bb0217667777d2816571bf706b1a3034f2f3d83b5ea4388)
    sorry census: exactly lean/Erdos251/Statement.lean:1, all other
      files 0                                        PASS
    roadmap/item-0019.md contains "status: ratified" PASS
    d5b_deep.py and balance_stats.py present         PASS

Resource probe (rule 9 style, once at session start): 94 GB RAM
total / 85 GB available, 9 GB free disk on the work volume, 32
hardware threads (operator-supplied: 96 GB, i9-14900T 24C/32T; the
runner's probe governs per delta D1 -- no material disagreement).
Python 3.13.5, numpy 2.2.4, sympy 1.13.3.  Full x ladder incl. 1e9
in-core and the 3(h) stretch at 1e10 in-core released (delta D1);
the Section 6 DEGRADE path was NOT exercised.

Worker count (delta D2 duty): 8 workers (multiprocessing fork
pool); all partition boundaries are fixed functions of the data
(delta chunks of 4,000,000 sites; 64 side-word hash buckets; 4096-
pair exact-product chunks), merges in partition index order, so
every committed table is byte-identical for every worker count
including serial.  delta chunk-parallel smoke check (delta D3, 1e8
prefix): max abs difference parallel vs serial = 0.0e+00 (accept
< 1e-12) -- printed in tables/smoke_test.txt.

Index dictionary (ANN-50 / v1.1 T6, fixed): Lean gap k = paper
g_{k+1}; delta carries no shift; Lean base index = paper anchor
index.  Seed-script convention used by every script (identical
content): g[t] = paper g_{t+1}, delta[t] = paper delta_t; site t:
prefix g[t..t+J-1], middle g[t+J], suffix g[t+J+1..t+J+K]; caps
delta[t+J] <= D and delta[t+J+K+1] <= 2^K; window sum g[t..t+L-1],
L = J+1+K.  Site clauses (i) 1 <= n with anchorPrime p_n <= x and
(ii) s+1 <= n at s = 0 are automatic on the array carrier (every
sieved prime is <= x; t ranges from 1).  s = 0 is fixed for the
whole campaign; statistics are s-invariant up to O(1) sites (no s
grid).  Comparison convention (stated once): integer int64 window
sums are compared against the float64 cap W = A' L ln x by numpy
int64 <= float64 promotion; float64 delta is compared against the
integer caps D and 2^K.  delta uses the exact seed recurrence
(d5b_deep.py): delta[M-1] = 2.0, delta[t] = 0.5*(g[t]+delta[t+1]),
last 200 sites discarded; the delta-D3 chunk scheme reproduces the
serial values bit-exactly (smoke check above).

## 2. Writes-scope diff (git status --porcelain at close, verbatim)

    ?? dossier/item-0019-workpapers/
    ?? item-0019-kickoff-v1.1-delta.md
    ?? item-0019-kickoff-v1.md

Exactly the Section 5 allowed writes (the workpapers directory:
scripts, tables/, and this report) plus the two pre-existing
ephemeral operator instruction files (kickoff v1 and the v1.1
delta; never committed, not run writes, per kickoff Section 5 and
the delta header).  Nothing else.  The run commits nothing and
pushes nothing; raw intermediates live outside the repo in the
session scratch directory.

## 3. Deliverable map

Scripts (dossier/item-0019-workpapers/):
  common.py       shared build (sieve, gaps, seed-recurrence delta
                  with the D3 chunk scheme), D0.2/D0.2'/N^w filter
                  layer mirroring Supply.lean memSiteFilter, and
                  the bucketed class machinery (D2 determinism).
  census.py       Phase A/B driver: dictionary smoke test,
                  continuity + V1 reproduction, m1/m2/m4
                  aggregates, Fam_2 class dumps for m3.
  rho_census.py   m3 exact-rational local quotient census +
                  validation (T4 witnesses, rho_exact cross-check)
                  + HEURISTIC/U18.2 reference lines.
  m5_thinning.py  m5 (N^o world only; anchor firewall).
  stretch_77.py   3(h) stretch: (7,7,67) hunt at 5e9/1e10.
  consolidate.py  renders the committed ASCII tables from the raw
                  run outputs.

Committed tables (dossier/item-0019-workpapers/tables/):
  continuity.txt        3(a) continuity table + full V1 record
  smoke_test.txt        3(a) dictionary smoke test + delta smoke
  m1_class_sizes.txt    m1
  m2_concentration.txt  m2
  m3_rho_census.txt     m3
  m4_tails.txt          m4
  m5_thinning.txt       m5
  d_sensitivity.txt     3(a) D-sensitivity ((4,5,D), 1e8)
  readout_families.txt  r2 favorable-family densities + fit lines
  stretch.txt           3(h) stage records

Raw intermediates (sieve/gap/delta caches, per-x JSON aggregates,
Fam_2 npz dumps) live under the session scratch directory, are
UNCOMMITTED and regenerable.  Regeneration from a clean checkout
(deterministic, worker-count independent; ITEM0019_CACHE selects
the scratch directory):

    cd dossier/item-0019-workpapers
    python3 census.py 2000000 && python3 census.py 20000000
    python3 census.py 100000000 && python3 census.py 1000000000
    python3 rho_census.py validate
    python3 rho_census.py J K D   # per grid row, e.g. 4 5 30
    python3 m5_thinning.py
    python3 stretch_77.py
    python3 consolidate.py core && python3 consolidate.py m3 \
      && python3 consolidate.py m5

## 4. Continuity + V1 reproduction record (kickoff 3(a))

Dictionary smoke test (executed BEFORE any census row was
reported): the (7,6,44,3) certificate pair at x = 1e9 was
re-derived from the sieve -- both sites (gap indices t = 7113518
and t = 960168), all 16 printed primes per site, prefix
[4,2,16,2,10,12,18], middles 6 vs 30, suffix [20,12,4,14,6,4],
d_1 = -24, both (E5) gates (3*(44-2) = 126 < 256; b = 1 form
42 < 256), near/far deltas to printed precision (10.426/14.562 and
22.477/21.089), identity residual -1.78e-15 equal to the printed
record at display precision -- EVERY integer datum byte-identical
to the e2prime-supply 7.2 record (tables/smoke_test.txt, 24/24
PASS).  Both sites re-qualify at (7,6,27,5) (near deltas <= 27)
and both class counts are 3, matching the committed record.

Continuity table (tables/continuity.txt): every committed V1
anchor reproduces EXACTLY in the D0.2 column -- the four pi(x)
anchors (148933/1270607/5761455/50847534); sites, |W_L|, |P|,
off-diagonal C_words/C_sides, P1 pairs and exchange classes at
(4,5,30) and (5,5,34) for x = 2e6/2e7/1e8 (12/178/1287 and
2/21/143 classes; C_sides 76/778/5232 and 18/108/638); (6,6,64)
0/0/1 and 29 at 1e9; (7,7,67) and (8,8,67) zero classes at 1e9;
(7,6,44) and (7,6,27) 3 classes each at 1e9.  All 76 per-anchor
checks PASS (72 collision-layer anchors + 4 pi anchors; full
per-anchor record in the table).  STOP-AND-REPORT was not
triggered.

D0.2 vs D0.2' (the A3-evidence bridge; the continuity table is the
only place both filters appear): the aggregate window cap removes
0.4-1.2% of sites at 2e6, RISING within each row with x to
0.6-1.4% at 1e9 (e.g. (4,5,30): 1.15% -> 1.19% -> 1.31% -> 1.40%;
143787 -> 142130 at 2e6, 39514634 -> 38960934 at 1e9), and
removes NO exchange class at any grid point (class deltas all
zero; the class populations of the two filter worlds coincide on
this grid through 1e9).  The D0.2' column is the campaign baseline
everywhere below.

## 5. m1-m5 results (one subsection each; DECIDES clauses answered
## verbatim; heuristic lines labeled)

### 5.1 m1 -- class-size distribution (tables/m1_class_sizes.txt)

The realized class-size distribution is radically flat: max N_P on
the whole campaign is 4 (attained twice, (4,5,30) at 1e9); >= 99.75%
of sites lie in singleton classes at every grid point; Fam_2 is
carried almost entirely by N_P = 2 classes.

Fam_2 mass fraction delta_emp = sum_{Fam_2} N_P / |S'_x| (A3's
delta empirically), by row across the x ladder 2e6 -> 2e7 -> 1e8 ->
1e9:

    (4,5,30): 5.347e-04 -> 6.773e-04 -> 1.063e-03 -> 2.441e-03
    (5,5,34): 1.252e-04 -> 9.174e-05 -> 1.253e-04 -> 2.404e-04
    (6,6,64): 1.353e-05 -> 1.590e-06 -> 1.055e-06 -> 3.521e-06
    (7,6,44): 0 -> 0 -> 0 -> 4.079e-07
    (7,7,67), (8,8,67): 0 throughout (frontier nulls)

DECIDES (m1, verbatim): "A3 plausibility at fixed delta vs
delta(x) -> 0 across the x ladder" -- on the two statistically
live rows ((4,5,30), (5,5,34); 38-47404 Fam_2 classes) the Fam_2
mass fraction GROWS monotonically from 2e7 on, by factors 3.6x
and 2.6x from 2e7 to 1e9 ((5,5,34) dips once, 2e6 -> 2e7, before
rising).  The deep rows carry only 1-88 Fam_2 classes; their
fractions are Poisson-dominated and non-monotone ((6,6,64):
1.35e-5 -> 1.59e-6 -> 1.06e-6 -> 3.52e-6) while their ABSOLUTE
Fam_2 mass rises steeply at the last step (6 -> 176 sites at
(6,6,64)).  At no statistically populated point does a sustained
decay trend appear; the fixed-delta reading is the one the finite
data support.  (Finite-scale statement only; the deep rows are
frontier-sparse and say nothing yet.)

DECIDES (m1, verbatim): "whether candidate B1's multiplicity floor
(ln x)^{1+eps_0} is reachable anywhere below 1e9 (expected: no)"
-- NO.  The floor requires N_P > ln x ~ 20.7 at minimum; the
maximal realized multiplicity anywhere on the campaign is 4.  B1
is hereby recorded as DROPPED from the measurable set at item-0019
depths; F18.5's pending-m1 clause is discharged (the F18.5
rms ~ 2 corpus inference is confirmed: mass-weighted mean
multiplicity is 1.0001-1.0025 across the live rows).

### 5.2 m2 -- per-class middle concentration
### (tables/m2_concentration.txt)

REDUCED statistic red_P = (max_d N_{P,d} - 1)_+/N_P
(audit-corrected form; the un-reduced max_d N_{P,d}/N_P appears
only as the labeled DIAGNOSTIC column).  The mass-weighted average
over Fam_2 is the DIRECT finite-scale measurement of C_F(x)/ln x
for RelExtensionUpper (= B2.reduced, the BET-08 shape) under the
adversarial selection d_P = argmax_d N_{P,d} (selection
identification stated once, in the table header and here).

    row       x:    2e6      2e7      1e8      1e9
    (4,5,30) C_F/lnx: 0.34211  0.27121  0.25388  0.23641
             C_F:     4.96     4.56     4.68     4.90
    (5,5,34) C_F/lnx: 0.38889  0.30556  0.27586  0.26440
             C_F:     5.64     5.14     5.08     5.48

DECIDES (m2, verbatim): "B2 vs B3: is concentration uniform across
Fam_2 or does an exceptional sub-family carry it" -- concentration
is STRUCTURAL, not exceptional-family-driven: the red_P
distribution is two-point to within noise (red = 0, i.e. all
middles distinct, vs red = 1/2, i.e. an N_P = 2 class with a
repeated middle), the red = 0 share grows with x (0.32 -> 0.46 ->
0.49 -> 0.53 at (4,5,30)), and the top-decile concentration
classes carry only ~10% of Fam_2 mass and 14-21% of the reduced
mass at every grid point with >= 9 Fam_2 classes (the 1-3-class
points have single-class deciles and degenerate ratios).  No heavy exceptional
sub-family exists at these scales: B2.reduced needs no B3-style
exceptional-mass weakening on the measured range.  (At these
multiplicities the statistic is granular -- N_P = 2 forces red in
{0, 1/2}; the uniform-vs-exceptional question becomes sharp only
when class sizes grow; O3.)

### 5.3 m3 -- local quotient census (tables/m3_rho_census.txt)

Arithmetic discipline as frozen (kickoff 3(d)): per-(P,d) EXACT
integer products over odd p <= S0 (S0 = max realized span per row,
printed: 296/260/264/226 for the four live rows), shared EXACT
band product on (S0, Q], certified one-sided analytic tail (true
rho in [rho_Q e^{-eps_Q}, rho_Q], eps_Q = 0.51 k^2/Q -- the
k^2/(Q ln Q) shape via the elementary integer comparison
sum_{p>Q} p^{-2} < 1/Q; one-sided because every tail log-factor is
<= 0).  Q-stability at Q in {1e4, 1e5, 1e6}: PASS on every row
(the band ratios sit inside the certified widths).  VALIDATION:
the three T4 witnesses reproduce at printed precision through this
pipeline at Q = 1e6 (82.24 / 221.66 / 1060.34 -- 3/3 PASS), and
one census value per row cross-checks against a verbatim
budget_sheet.py rho_exact float evaluation at relative difference
<= 5.5e-14 (6/6 PASS).  rho is computed on realized classes and
realized middles only (RS.3 domain clause); off-domain zeros
encountered: 0.

Census shape: the realized-class rho distribution is strongly
right-shifted against the U18.2 d-mean reference 2 and is
SCALE-STABLE on the live row -- (4,5,30) means 14.4 / 13.1 / 13.1
/ 13.2 and medians ~10.5 across the whole ladder; (5,5,34) means
12.3-16.6; the sparse deep rows run hotter ((6,6,64) mean 27.4 at
1e9; (7,6,44) mean 33.3, median 17.3), i.e. realized deep
coincidences select CRT-aligned words.  Quantile tables per row
and x are committed in tables/m3_rho_census.txt.

Extreme types (CRT-alignment diagnosis): the top-10 rho classes at
(4,5,30), 1e9 reach rho = 119.0 = 5.7 ln x with residue profiles
showing full two-block alignment at p = 3 and p = 5 in ALL ten
profiles (nu_H = nu_pre = nu_suf = 2 and 4) and at p = 7 in six
of ten: the corrected-T4 / RS.3 worst-case mechanism
(block-aligned middles amplifying under the S(H_suf) division) is
realized in the wild, not only at constructed witnesses.  The
realized-class rho LEVEL grows with row depth (means 13.2 / 16.6
/ 27.4 / 33.3 at 1e9 across (4,5,30)/(5,5,34)/(6,6,64)/(7,6,44):
the sparse deep rows are the most aligned), while the extreme
order statistics are census-size-dominated (realized maxima
119.0/189.4/115.6/103.6 at 1e9).  This is the finite-scale face
of sup rho = (ln x)^{1-o(1)}: B1-type pointwise forms need their
(b1-rho) cap exactly as the audit repaired them.

Correlations (per-class mass-weighted rho_bar; Pearson/Spearman;
values quoted at the reference point (4,5,30), 1e9, the largest
census; full per-point table committed): with flank span
-0.04/-0.05; with min flank gap -0.05/-0.04; with small-prime
residue coverage +0.60/+0.64 (the alignment direction, as the
RS.3 structure predicts); with N^w cap-failure rates at the two
grid points with nonzero Fam_2 cap failures: -0.005/-0.000 (near,
(4,5,30) 1e8) and -0.012/-0.013 (near) / -0.013/-0.013 (far) at
(4,5,30) 1e9; with class mean tail delta |corr| <= 0.025 at the
populated grid points (>= 2610 classes; sparser points scatter
arbitrarily, down to -0.99 on a 3-class point).  rho against
concentration red_P: +0.33/+0.33 at the reference point.

DECIDES (m3, verbatim): "whether rho-normalization makes m2's
concentration collapse to a scale-free law" -- PARTIAL COLLAPSE,
in B2's favor: at (4,5,30) the q75 of y_P = red_P ln x /
rho(P,d*) is trend-free within +/-12% across three decades of x
(0.77/0.62/0.65/0.68) while q95 drifts upward (1.30 -> 1.35 ->
1.53 -> 1.61, +24%) and the median migrates into the growing atom
at y = 0 (the red = 0 share).  Where concentration is present it
is rho-proportional at an O(1) level, scale-free on the bulk with
a slowly widening extreme tail.  Short of proof, this is the
strongest finite-scale evidence the B2 C_F = O(1) heuristic could
get from this census (m3's DECIDES intent), scoped to the
measured range.

HEURISTIC/U18.2 lines (labeled in the committed table): the
even-conditioned in-window d-mean of rho per class is 1.68 -> 1.75
across the ladder at (4,5,30) (reference value 2; the direction of
the (1+o(1)) correction is toward the reference).  The middle-law
aggregate calibration ratio (observed realized-cell mass over the
law's prediction) is 1.56 -> 1.82 -> 1.91 -> 2.04 across the
ladder at (4,5,30); the sparse rows scatter without trend (e.g.
(5,5,34): 1.83 -> 1.55 -> 1.62 -> 1.69).  The Poisson-normalized
residuals have sd ~ 1.1 with a positively inflated mean from the
sub-1-mass corner (realized-cell selection forces N_{P,d} >= 1
against predictions << 1; the pred >= 1 pair counts from the
corrected-T4 sup regime are printed) -- at these multiplicities
the middle law is not pointwise testable; no law fit is claimed.

FU4 (optional sub-package): SKIPPED, declared: the in-window
admissible (P,d) space at the 1e8 grid depths is a ~C(137,9) ~
1e13 lattice-word enumeration, not a small search space; an EXACT
sup claim would need a branch-and-bound design that this campaign
does not owe.  The T4 witness lower bounds (82.24 at the 1e8
depths) and the realized census maxima above stand as the
committed finite-scale record.

### 5.4 m4 -- class-conditional tail statistics
### (tables/m4_tails.txt)

Count worlds per RS.4, never mixed: S' (D0.2', all caps inside)
and N^w (window cap only) in separate labeled columns; m5's N^o
world is in a separate file entirely (anchor firewall).

eps_C = 1 - sum_{Fam_2} N_P(S'_x)/sum_{Fam_2} N^w_P(x): ZERO at
every grid point with nonempty Fam_2 except (4,5,30) at 1e8
(1.9e-04) and 1e9 (1.9e-03) (undefined where Fam_2 is empty).
DECIDES (m4, verbatim): "is constant retention visible (C1's
eps_C < 1/2 finite-scale shadow)" -- YES, overwhelmingly:
retention exceeds 0.998 at every measured point; the delta caps
remove essentially no Fam_2 mass once the window cap has acted.

Cap-failure rates (N^w world): global near/far failure rates grow
with x to 1.2e-01/1.05e-01 at (4,5,30), 1e9; the Fam_2-conditional
rates are two orders smaller (6.4e-04/1.3e-03 there; 1.9e-04 near
at (4,5,30), 1e8; exactly zero at every other grid point with
nonempty Fam_2).  "Do the truncated-tail first-moment inputs
behave" -- YES: E_class[delta_{n+L}] over Fam_2 tracks the global
mean within ~1% at the populated 1e8/1e9 points of the live rows
((4,5,30) 1e9: 17.43 vs 17.25; (5,5,34): 17.32 vs 17.25; within
~7% at the small-sample 2e6/2e7 points), and the class-conditional
delta-tail histograms (committed in the table) sit inside the
global bulk with no tail excess -- matched-flank classes are
tail-typical, slightly tail-benign, never tail-adverse.  The deep
sparse rows drift tail-rich as expected of few-member classes
((7,6,44) 1e9: 23.10 vs 19.56 global; 20 sites total; (6,6,64)
1e8: 22.91 vs 17.33 on 6 sites) -- consistent with the
certificate-depth calibration of the T6 smoke test.

### 5.5 m5 -- small-span thinning calibration
### (tables/m5_thinning.txt; N^o world ONLY, anchor firewall)

Word set: at kappa = 1 the exhaustive within-budget enumeration
returns EMPTY at every k in {4,5,6,8} (budgets 4.83/7.17/9.73/
15.38): no admissible all-even gap word exists within the kappa =
1 span budget at these ranks -- itself the datum: A1's small-span
window at kappa = 1 is combinatorially empty here and first
populates at kappa = 2, where the lex-first admissible words have
spans 8/12/18/26 (deterministic word list printed in the table).

At kappa = 2 (10 words across k in {4,5,6,8}): N^o_consec =
N^o_tuple EXACTLY for every word with span <= 26 at both x = 1e8
and 1e9 (ratio 1.00000); the first strict thinning appears only at
k = 8, span = 30, x = 1e9 (ratios 0.625 and 0.769 on counts of
8 and 13).  For the short words consecutiveness is FORCED by
admissibility (an intermediate prime in the window would extend
the admissible constellation; e.g. for (2,4,2) the point p+4 is
divisible by 3 whenever the four tuple points are prime), so the
ratio is structurally 1, not statistically 1.  The
HEURISTIC/U18.1 exp(-span/ln x) Cramer reference line (0.20-0.68
on this range) under-predicts the observed ratios everywhere: the
finite-scale shadow of tau(A') is NOT yet visible at spans <= 30
-- the A1-vs-A1-typ boundary sits beyond the small-span windows
reachable at these k, consistent with F18.1's re-concentration of
the burden away from small-span transfer.  No asymptotic exponent
is fitted.

## 6. Go-signal readouts and the item-0020 gate verdict (3(g))

Support classes: every sentence below is MEASURED unless labeled
DESCRIPTIVE or HEURISTIC (rule 16(a) discipline; the labels
survive verbatim from the tables).

(r1) STABLE SMALL AVERAGED RELATIVE CONSTANT
     [cites tables/m2_concentration.txt].  MEASURED: the m2
     mass-weighted average (= C_F(x)/ln x under the adversarial
     argmax selection) DECLINES monotonically in x on the live
     rows: 0.342 -> 0.271 -> 0.254 -> 0.236 at (4,5,30), 0.389 ->
     0.306 -> 0.276 -> 0.264 at (5,5,34) (the deep rows are
     granularity-pinned near 1/3-1/2 on 1-88 classes and carry no
     trend); the implied C_F sits in [4.56, 5.64] on the live
     rows, far below the ln x gate value, roughly flat in x.
     VERDICT: the trend condition holds (declining) on the rows
     that can show a trend; the magnitude condition is QUALIFIED
     -- ~1/4, small against 1 but not << 1 at reachable x, and
     granularity-floored: at N_P = 2 the reduced statistic can
     only take values {0, 1/2}, so the average is pinned to half
     the repeated-middle mass share, and its decline is exactly
     the measured growth of the red = 0 share (0.32 -> 0.53).

(r2) FAVORABLE-FAMILY DENSITY
     [cites tables/readout_families.txt].  MEASURED: with the
     operative diagnostic definition F_fav(theta), the theta = 0
     family (all realized middles distinct) carries a GROWING
     share of Fam_2 mass across the ladder on the live rows:
     0.316 -> 0.458 -> 0.492 -> 0.526 at (4,5,30), 0.222 -> 0.389
     -> 0.448 -> 0.471 at (5,5,34); mass(F_fav)/|S'_x| grows 7.6x
     over the ladder (1.7e-4 -> 1.3e-3 at (4,5,30)).  DESCRIPTIVE fit
     line: the least-squares (ln x)^{-c} exponent on
     mass(F_fav)/mass(Fam_2) is c = -1.4 to -2.1, i.e. GROWTH,
     against the item-0021 reference decay ceiling c* = 4 ln 2 -
     2 = 0.7726 (D3(vi): a 3-4-point fit at ln x in [14.5, 20.7]
     fixes nothing asymptotic; the fit is DESCRIPTIVE only).
     VERDICT: favorable families are dense and densifying at
     every statistically live measured point (the deep rows are
     empty-to-single-class below 1e8 at theta = 0 and flat ~0.33
     at 1e8/1e9 on (6,6,64)); theta in {0, 1/4} coincide to
     within 2 classes (granularity), theta = 1/2 is the Fam_2
     bulk.

(r3) CAP/QUOTIENT DECORRELATION
     [cites tables/m3_rho_census.txt, m4_tails.txt,
     d_sensitivity.txt].  MEASURED: per-class rho_bar against N^w
     cap-failure rates: |corr| <= 0.013 (Pearson and Spearman) at
     the two grid points with nonzero Fam_2 cap failures
     ((4,5,30) at 1e8: near -0.005/-0.000; at 1e9: near
     -0.012/-0.013, far -0.013/-0.013); at every other grid point
     with nonempty Fam_2 the cap-failure rates are identically
     zero (trivially decorrelated -- no variance to correlate).
     rho_bar against class mean tail delta: |corr| <= 0.025 at
     the populated grid points (>= 2610 classes; sparser points
     scatter arbitrarily on tiny samples, down to -0.99 on a
     3-class point).  D-sensitivity: widening the near cap
     D = 30 -> 44 -> 67 at (4,5,30), 1e8 moves delta_emp by
     +0.3%, mw_red by -7%, and eps_C to 0 (d_sensitivity.txt) --
     the near cap is not shaping the class or quotient structure.
     Concentration itself correlates with rho at +0.33 at the
     reference point (4,5,30), 1e9 (the U18.2-direction coupling,
     expected; sparse points scatter from -0.11 to +0.58).
     VERDICT: cap events and local quotients are DECORRELATED at
     these scales; the C-layer filters and the B-layer quotient
     structure factor cleanly on the measured range.

GATE VERDICT (v1.1 Section 7.4, verbatim consumption).  From m1's
Fam_2-mass trend across the x ladder [cites
tables/m1_class_sizes.txt]: the Fam_2 mass fraction delta_emp is
NON-DECAYING on the statistically populated rows -- it GROWS
monotonically from 2e7 on at both live rows (factor 3.6x from 2e7
to 1e9 at (4,5,30); 2.6x at (5,5,34); trend table in Section
5.1), while the deep rows carry Poisson-dominated O(1)-O(10^2)
class counts with no stable fraction trend but steeply rising
absolute Fam_2 mass at the last ladder step.  On these data A3 is
plausible AT FIXED delta, and the gate
item-0020 must clear is the FIXED-DELTA gate:

    RelExtensionUpper with C_F(x) = o(ln x), quantitatively
    C_F(x) <= (1 - eps) (delta/2)(1 - eps_C) ln x,

with eps_C measured ~0 (Section 5.4).  The coupled gate C_F(x) =
o(delta(x) ln x) is NOT forced by any measured decay.  Honesty
scope (both-readings duty): the trend is measured at FIXED
sub-frontier rows (J,K,D); the D0-pinned parameter map couples
depth to x, and at the map's own depth the 1e9 data are
frontier-null (zero Fam_2 at (7,7)/(8,8)) -- the coupled-depth
delta(x) is therefore NOT directly measured, and along the
deepening diagonal the mass falls to zero at the frontier by
construction.  Within the statistically measurable range the decay hypothesis
finds no support at any populated point; if item-0020 needs the
coupled gate it must argue it, not read it off these data.  Quantitative caveat,
stated plainly: at 1e9 the measured C_F/ln x (~0.24) exceeds the
measured (delta_emp/2)(1 - eps_C) (~1.2e-3) by two orders -- the
exclusion inequality is far from closing at reachable x; what the
campaign certifies is the DIRECTION of both terms (delta rising,
C_F/ln x falling), not a finite-scale closure.  This subsection
feeds the BET-08 evidence base (resolve_by 2026-09-30); operator
judgment, no scoring.

S-WEIGHTING DEMOTION (mandatory sentence): no S-weighted or
whitened statistic was computed in this campaign; the DIAGNOSTICS
heading is accordingly empty, any such statistic appearing in
these workpapers is demoted to DIAGNOSTIC status by this
sentence, and U17.11(b) stays open (acceptance intent honored).

## 7. Stretch record (3(h); tables/stretch.txt)

EXECUTED (released by v1.1 delta D1/D4; run strictly after
3(a)-3(g) were complete and written).  (7,7,67) D0.2-style filter,
in-core stages at x = 5e9 and 1e10 with the D4 uint8 half-gap
packing (evenness and g < 512 guarded by asserts over the scanned
range), global join over the full prefix per stage, output sorted
by (packed side key, site index).

FIRST (7,7) PAIRS OF THE PROJECT -- the frontier datum lands
exactly where e2prime-supply 7.2 predicted (~0.5 expected pairs at
1e9, zero observed there; first pairs forecast at 5e9-1e10):

  x = 5e9  (pi = 234954223, 234265779 filtered sites): 2 exchange
  classes.
    Pair 1: flanks [22,2,4,12,12,20,6] | . | [6,6,2,10,30,8,22],
      middles 10 vs 100 (d_1 = -90), anchors 1558668469 (t =
      77500622) and 3236525029 (t = 155269232); identity residual
      0.0.
    Pair 2: flanks [10,12,2,34,12,8,42] | . | [18,6,30,24,6,12,2],
      middles 4 vs 34 (d_1 = -30), anchors 3866025649 (t =
      183897815) and 3538114189 (t = 169014085); identity residual
      1.78e-15.
  x = 1e10 (pi = 455052511, 453319251 filtered sites): 3 exchange
  classes -- both 5e9 classes persist under the global re-join,
  plus
    Pair 3: flanks [10,32,24,4,6,2,4] | . | [22,2,12,18,6,4,20],
      middles 14 vs 44 (d_1 = -30), anchors 8892469561 (t =
      406830912) and 1420107001 (t = 70939705) -- matched flanks
      across a factor 6.3 of anchor scale; identity residual 0.0.

Every certificate is printed in the d5b_deep exch_cert format in
tables/stretch.txt (17 primes per site, both (E4) caps, the (E5)
gate 65 < 256, d_1, identity residual) and was RE-VERIFIED
gap-by-gap and prime-by-prime (trial-division primality) from the
printed primes inside the run.  Max side-class size at both
stages is 2; repeated-side classes (any middles): 5 at 5e9, 10 at
1e10.  Stage walls 591 s and 1250 s at 8 workers.

Continuity note: the (7,7) collision calculus of e2prime 7.2
(expected side collisions N^2 (gamma_2^vec/ln x)^14 ~ 0.5 at 1e9)
is quantitatively confirmed one scale deeper: the observed ladder
0 / 5 / 10 repeated-side classes at 1e9 / 5e9 / 1e10 brackets the
prediction's growth curve, and the first exchange pairs appear
exactly inside the forecast window.  All three middles differ by
d_1 in {-30, -90}: even, nonzero, P2.1 factor-2 margin applies at
every pair.

## 8. Observations (O-n)

O1 (bit-faithfulness of the reproduction layer).  All 76 committed
   V1 anchors, the byte-level certificate, and the display-precision
   identity residual (-1.78e-15) reproduced on first attempt after
   the definitions were mirrored from the seed scripts and
   Supply.lean -- including through the D3 chunk-parallel delta
   (parallel-vs-serial max abs diff exactly 0.0).  The ANN-50/T6
   dictionary plus the exact seed recurrence is a complete
   reproduction interface; no hidden convention was discovered.

O2 (D0.2 -> D0.2' bridge is class-invisible).  The aggregate
   window cap removes 0.4-1.4% of sites and not a single exchange
   class anywhere on the grid through 1e9 (continuity table).  The
   committed D0.2-based collision records carry over to the D0.2'
   world unchanged at the class layer; A3-evidence continuity
   holds with zero repair.

O3 (granularity honesty).  Max class multiplicity on the whole
   campaign is 4 against ln x ~ 20.7: every concentration
   statistic is integer-granular (red_P in {0, 1/2} at N_P = 2),
   the middle law is not pointwise testable (sub-1-mass cells),
   and no measured number here approaches any asymptotic constant
   (the in-repo C = 12 mass floor stays vacuous below ~1e371;
   item-0018 O4 rows).  The campaign measures the ONSET of
   multiplicity structure, and the onset data all point the same
   way.

O4 (m5 structural ratio-1).  At span <= 26 consecutiveness of
   small-span tuples is FORCED (admissibility blocks interior
   primes), so N^o_consec = N^o_tuple exactly; the first genuine
   thinning appears at k = 8, span 30, 1e9, where the word first
   contains interior gaps wide enough to admit an intermediate
   prime.  The U18.1 exp(-span/ln x) reference line is not the
   operative description at these spans; tau(A') remains
   unmeasured (its window opens at larger k than the m5 word set
   reaches).

O5 (realized rho is alignment-selected).  Realized Fam_2 classes
   carry rho an order of magnitude above the U18.2 d-mean
   reference (medians ~10.5 vs 2), with full two-block alignment
   at p = 3 and 5 in every top-10 profile (and at p = 7 in most),
   and the mean rho strengthens with row depth (sparse deep rows
   are the most aligned).
   Matched-flank coincidence at finite scale IS CRT alignment in
   the observed regime -- consistent with the corrected T4 and
   directly relevant to what a B2 proof must average over.

O6 (in-run adversarial review).  A four-lens adversarial review of
   the measurement scripts against the frozen spec (indexing,
   statistics, arithmetic-discipline, determinism lenses; 11 raw
   findings, each adversarially re-verified by independent
   refutation agents) ran BEFORE the committed m3 tables were
   produced.  Repairs applied mid-review, each re-verified sound
   by the refutation pass: (i) log(0) crash in the HEURISTIC
   d-mean sweep at CRT-covered rotations -- fixed via the RS.3
   off-domain rho = 0 convention; (ii) binomial normalization of
   the middle-law residuals ill-posed where pred >= 1 (the
   corrected-T4 sup regime) -- switched to Poisson normalization
   with the pred >= 1 count printed; (iii) the d-mean sweep's
   exact-prime range extended to the sweep's own max span (the
   (S0, W] primes are not saturated for the largest unrealized
   d), with the band factor adjusted accordingly.  Adjudicated
   non-defects, recorded for transparency: the Fam_2 dump order
   is (hash-bucket, side-lex) rather than the v1.1-delta D2
   display key -- the binding D2 sentence is worker-count
   byte-identity, which holds, and every committed listing is
   explicitly keyed with no float tie firing; the side-word hash
   parity populates only the 32 even buckets (load balance only,
   zero correctness or determinism effect).  Final verdict of the
   review: zero findings survive against the code that produced
   the committed tables.

O7 (kickoff textual note for operator hygiene).  The kickoff's
   Section 0 scope note resolving the roadmap one-point-insert
   display against the frozen RS.3 two-block quotient worked as
   intended; no conflict with the v1.1 text was encountered
   anywhere in Section 3 execution (no U18.5 round-trip owed).

## 9. Follow-up candidates (F-n; described, never executed --
## the mandatory channel)

F1 (matched-depth delta ladder).  m1's delta_emp trend is measured
   at fixed rows; a successor measurement could run the
   collision-calculus diagonal (deepen (J,K) with x so expected
   side collisions stay ~constant) to probe the coupled-depth
   delta(x) the 7.4 gate sentence actually names.  Rule-15
   remark: priced by the m1 table rows along the matched-depth
   diagonal; no proof content.

F2 (alignment-constructed doubly-extendable pairs).  The m3
   extreme-type profiles (full alignment at p = 3, 5, 7) suggest
   constructing side pairs with >= 2 in-budget middles directly
   from aligned residue systems -- the concrete lead for U18.7 /
   FU2 (blocks with >= 2 uncovered shift classes mod every small
   prime).  Rule-15 remark: priced by the T4 sup rows.

F3 (exact rho sup, branch-and-bound).  FU4's exact in-window sup
   at 1e8 depths is a well-posed finite computation but needs a
   pruned search (per-prime factor upper bounds over residue
   systems), not enumeration (~1e13 words).  Rule-15 remark:
   priced by T4; the deliverable would replace the witness lower
   bounds by exact sups.

F4 (m5 at thinning-visible spans).  Re-run m5 at k in {12, 16,
   24} (kappa = 1 becomes nonempty near k = 12) where interior
   primes fit and tau(A') has a window; 1e9-1e10 reachable with
   the same bitset kernel.  Rule-15 remark: priced by the T5(c)
   tau rows.

F5 (Fam_2 growth-law measurement).  delta_emp at (4,5,30) grows
   ~2.3x per decade over the last two decades; a dedicated
   successor could measure the growth exponent against the
   collision-calculus prediction N (gamma_2^vec/ln x)^{J+K} to
   calibrate gamma_2^vec one scale deeper (continues the e2prime
   7.1 vector-constant series).  Rule-15 remark: priced by the
   continuity table plus e2prime 7.1's vector-constant rows.

## 10. Close gates

Re-run at close (kickoff Section 7 duty; all UNCHANGED -- this
item never touched lean/):

    python3 lean/scripts/blocks.py check-frozen  ->
      "FROZEN BLOCKS: all byte-identical."          PASS
    python3 lean/scripts/blocks.py relocation-check ->
      "RELOCATION CHECK PASSED"                     PASS
    sorry census: exactly lean/Erdos251/Statement.lean:1,
      every other file 0                            PASS
    mathlib pin a6276f4c6097675b1cf5ebd49b1146b735f38c02
      intact in lean/lake-manifest.json             PASS
    lean-toolchain trailing newline intact
      (file ends "...6.0\n")                        PASS
    git rev-parse HEAD = the Section 0 pin
      (c3fc09a5...; no commits made by the run)     PASS
    git status --porcelain = Section 2 verbatim     PASS

Committed data volume: tables/ total ~98 KB across 10 files, max
file 41 KB (m3_rho_census.txt) -- inside the ~200 KB per-file and
~2 MB total caps; no per-class raw dumps committed.

Review gate (staged per kickoff Section 8, operator decision):
R1-light = steering re-execution of the committed tables at
{2e6, 2e7, 1e8} (full) plus one 1e9 grid row, plus a determinism
check (by v1.1 delta D2 the tables are worker-count-agnostic, so
a serial steering rerun compares directly); rule-16(a) pass over
the r1-r3 / gate-verdict sentences.  An in-run rule-16(a)
clause-diff pass (adversarial, independent agents) was already
executed against the committed tables and its confirmed
scope/precision repairs are folded into Sections 4-6 of this
report; the operator pass remains staged as the binding one.  No
blind R2 is pre-staged; bookkeeping (ledger ANN, HASHES entries,
roadmap done-move, HANDOVER) is steering/operator post-run.
