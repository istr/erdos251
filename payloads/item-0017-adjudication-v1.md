# item-0017 adjudication v1 -- two adversarial reviews vs. dossier v1

Date: 2026-07-18. Adjudicator: steering (Claude Fable 5), per the B2
architecture. Reviews: R1 = same-family fresh instance, computation
audit (payloads/item-0017-review-r1-v1.md; SOUND WITH REPAIRABLE
ISSUES, 0.89, zero fatal); R2 = GPT-5.6 Sol, cross-family, scope
audit (payloads/item-0017-review-r2-v1.md; UNSOUND, 0.96). Both
blind against the SAME object (sha256 5a7a2647..., the Session-C
dossier state; R1's five findings were repaired post-R1, so R2
independently re-finding three of them is convergence, not overlap).
Discipline: every sustained-or-rejected disposition below was
steering-RE-EXECUTED (checklist rule iv) before being recorded.

## 1. Headline adjudication

R2's verdict "UNSOUND" is SUSTAINED AGAINST THE v1 VERDICT LAYER
(Section 1 wording) and NOT SUSTAINED against the computational
body: R2 itself grants "not about every local calculation", and R1's
independent re-computation reproduced the entire numeric spine.
Disposition summary:
- ONE finding invalidates actual mathematical content: R2 FATAL-2
  (the V4 "single missing input" claim). The v1 assertion that
  D1-L's exclusion budget absorbs the rigid-middle exclusion is
  FALSE, by the dossier's own constant: the exclusion inequality
  needs C*(k+1) * S-ratio < c ln x, and ln C*(k+1) =
  (1+o(1)) k ln k >> lnln x = ln ln x at k ~ (2/ln 2) lnln x --
  steering-re-executed and confirmed. The classical 2^k k! fails
  identically. V4 and F17.7 are REWRITTEN in v2; the corrected
  insight (the T1 transplant inherits the growing-k sieve-constant
  wall; the class lower bound is necessary but NOT sufficient) is
  registered as F17.9 with credit to R2.
- R2 FATAL-1 is sustained as the central WORDING overclaim (the
  item-0005 P1 pattern): the body's PROVABILITY/TRUTH split
  (Section 4.3) was correct and labeled, but V2's headline
  ("exactly closed", "the primes close the route") promoted the
  heuristic+measured conclusion to an unconditional primes-side
  assertion, and the unproved tensorization step (marginal gamma_2
  -> growing-window collision law) was load-bearing but unstated:
  now registered (U17.11) and the verdict downgraded to the
  route-specific, explicitly heuristic-and-measured closure. R2's
  internal-inconsistency charge is sustained against the V2
  headline, and REJECTED against the body: Section 4.3's "three
  surviving routes, each meeting a named blocker" is consistent
  with the unweighted-floor closure; the headline's breadth created
  the collision.
- R2 MAJOR-1 (model concentration) is sustained as a
  proof-completeness finding: the M1 a.s. statement relied on a
  Lipschitz/tail claim that was asserted, not executed. v2 adds the
  missing layer (delta-tail truncation lemma; insertion-Lipschitz
  argument for the site count under single-flip with index shift;
  the caps-conditioning estimate), and M1's status is stated as
  proved-with-appendix; the remaining formalization debt is
  registered (U17.12).
- R2 MAJOR-2 and MAJOR-6 and MINOR-2 are CONVERGENT with R1's m-3,
  M-1, m-1 respectively (three independent cross-family
  convergences on the same defects) -- all three were already
  repaired post-R1; dispositions: sustained, already repaired.
- R2 MAJOR-3/4/5/7 and MINOR-1/3/4: sustained as wording/scope
  repairs, all executed in v2 (see Section 3).
- R2's S1 support-classification table is adopted as
  substantially accurate, with two corrections recorded in
  Section 2.

After the v2 revision the verdict layer matches the body; the
mandate outcome is UNCHANGED IN KIND (obstruction branch, no
unconditional supply theorem) but its strongest clauses are now
explicitly route-relative, measurement-relative, and
heuristic-labeled, and V4's residual is a TRIPLE requirement, not a
single input.

## 2. Point-by-point

R2 FATAL-1 (V2 "exactly closed"). SUSTAINED AS WORDING + ONE
REGISTER ADDITION. Steering re-execution: the threshold calculus is
algebraically proved (R1 C2 concurs); the primes-side closure rests
on (i) measurements at the reported scales (marginal 1.2005/1.1808/
1.1711; vector 1.68/1.58/1.55), (ii) the HL-frame marginal asymptote
1.150481, (iii) an UNSTATED tensorization step: no theorem bounds
the (J+K)-window consecutive-gap collision constant below by the
marginal constant, nor keeps its geometric mean above critical as
J+K -> infinity. (iii) is now U17.11 and named inside F17.5.
Adopted narrower wording: R2's own proposal, essentially verbatim
(v2 V2). The sub-claim "S-weighted repair funnels with no constant
to spare" is likewise re-scoped: the k = 2 identity is exact; its
growing-k compounding is heuristic (was already flagged in 4.4's
"honest form" sentence; the flag now travels into the register,
U17.11(b)). REJECTED in part: R2's assertion that the finite direct
sum "is close to, not equal to" undermines the Euler product -- the
product value is exactly computable mathematics; only its ROLE as
the gap-law asymptote is heuristic (R2's own S1 table says this
correctly; MINOR-3's wording fix is adopted, the substance was
never in doubt).

R2 FATAL-2 (V4 "single missing input"). SUSTAINED SUBSTANTIVELY --
the one finding that changes mathematical content. Steering
re-execution: rigidity exclusion needs
  c S_H x/(ln x)^k  >  C_per(k+1) S_{H u d0} x/(ln x)^{k+1},
i.e. C_per(k+1) (S_{H u d0}/S_H) < c ln x. With
ln C*(k+1) = (1+o(1)) k ln k and k = (2/ln 2 + o(1)) lnln x:
k ln k ~ 2.885 lnln x (lnlnln x + 1.06) >> lnln x = ln(ln x):
C*(k+1)/ln x -> infinity. CONFIRMED. Moreover 2^k k! carries the
same exp((1+o(1)) k ln k) and fails identically: the exclusion
step of the T1 pattern works at FIXED k (Pintz's regime, where
C(k)/ln x -> 0 trivially in x) and breaks at growing k on the
constant, independent of which admissible sieve bound is used.
Also sustained: the tail-intersection requirement (the T1 anatomy's
own (b) clause, dropped from V4's summary) -- the class lower bound
must survive the (E4) caps in the filters-first order. v2: V4
rewritten as a TRIPLE requirement (class lower bound; extension
upper bound with constant o(ln x) at k ~ lnln x -- unavailable to
every displayed sieve input; tail intersection); F17.7 rewritten;
new finding F17.9 (the growing-k exclusion-constant wall) credited
to R2.

R2 MAJOR-1 (M1 dependency/concentration). SUSTAINED
(proof-completeness). Steering assessment of repairability, executed
in v2: (a) delta-tail truncation -- delta^M truncated at
J_0 = ceil(2 log2 ln x) + K positions changes the filter events by
probability o(1/x) per site (geometric tail beyond J_0 positions),
so all filters become finite-block events up to negligible error;
(b) N_S concentration -- single-flip of X_n inserts/deletes one
model prime; downstream gap WINDOWS are shifted copies, so the
filtered-site count changes by O(L) (only windows containing the
edit point change content); McDiarmid over the independent X_n with
c_n = O(L) gives deviation exp(-c mu^2/(x L^2)), ample at
mu ~ x/ln x; (c) the caps-conditioning 1+o(1) factors -- written as
an explicit two-sided estimate P(caps | window values under the
aggregate cap) = 1 - o(1) uniformly, since the caps depend on the
truncated tail beyond the window plus capped window values.
The pair count T keeps its second-moment (Chebyshev) treatment,
which never used Lipschitz arguments. Residual formalization debt
(fully rigorous write-out of (a)-(c) at referee grain): U17.12.
"Derivations withheld" for the 3.5 checkers: sustained as a
limitation of the in-run check protocol; recorded in Section 11.

R2 MAJOR-2 (A' > 1 vs A'' = 16). SUSTAINED; CONVERGENT with R1 m-3;
already repaired post-R1 (A''(A') scaling clause). No further
action.

R2 MAJOR-3 (depth floor premise). SUSTAINED AS WORDING: 6.1(a)
carries the tail-typical premise; V3 dropped it. v2 V3 and 6.3 add
the qualifier and the atypical-small-tail escape route is named
with its own cost (site-density/selection analysis, F17.8's
territory), per R2's proposed wording.

R2 MAJOR-4 ("confirmed EXHAUSTIVE"). SUSTAINED AS WORDING: no
coverage ledger over all 14 texts nor a composition-closure
argument exists. v2 adopts R2's narrower form ("every individually
mapped mechanism ... in the displayed implementation; no examined
composition ...; exhaustiveness over all compositions not
established").

R2 MAJOR-5 (impossibility-language sweep). SUSTAINED AS WORDING.
All nine S2-table sentences re-worded in v2 per R2's required
scopes (with the FATAL-1/2 rewrites subsuming four of them).

R2 MAJOR-6 (P3.2). SUSTAINED; CONVERGENT with R1 M-1; already
repaired post-R1 (threshold N >= 40(L+2), verified). R2's
alternative diagnosis (permit L near N) matches R1's
counterexamples. No further action.

R2 MAJOR-7 (certificate scoping). SUSTAINED AS WORDING: v2 splits
(i) hand-verified finite facts (gaps, flanks, middles, gates --
checkable from printed primes), (ii) script-computed quantities
(delta tails, class counts; independently recomputed by R1, which
R2 could not see), (iii) project-history claims ("first of the
project", "committed record" -- in-repo verifiable, not
blind-package verifiable). No content change.

R2 MINOR-1 ("every reachable x"). SUSTAINED; v2: "at every
reported measurement scale and grid point".
R2 MINOR-2 (/8 vs /16). CONVERGENT with R1 m-1; already repaired.
R2 MINOR-3 (product vs sum equality). SUSTAINED; v2: "agrees to
8.1e-5 at D = 2e6".
R2 MINOR-4 ("primes-specific"). SUSTAINED; v2 adopts "the tested
obstruction is absent in Model M; the model gate finds no
architectural contradiction at this level".
R2 NOTE-1. Adopted as supportive (the finite certificate core).
R2 NOTE-2. Adopted; v2 glosses the ">" as consumer-fit priority,
not logical strength.

R2 S3/S4 (discipline/quantifier sweeps). SUSTAINED where they
instantiate the findings above; the S4 filter-quantifier point
("does not quantify over different filter shapes") is absorbed
into the V2 rewrite.

Corrections to R2 recorded (both minor): (1) the Euler-product
value is exact mathematics, not heuristic (its application is);
(2) Section 4.3's survivor list was consistent with the body-level
closure claim -- the defect was the headline's breadth, not a
body-level contradiction.

## 3. Required revisions for v2 (complete list; ALL EXECUTED)

1. V2 rewritten to the route-specific, heuristic+measured closure
   (R2 FATAL-1 wording); U17.11 added (tensorization + growing-k
   moment compounding as named load-bearing open steps); F17.5
   statement carries the same scope inline.
2. V4 rewritten as the triple requirement; F17.7 rewritten; F17.9
   added (growing-k exclusion-constant wall; credit R2).
3. M1 completed with the truncation/insertion-Lipschitz/
   conditioning repairs (sketch-grade, explicitly labeled);
   U17.12 added (referee-grain write-out debt); M2.2's a.s. clause
   inherits the same appendix.
4. V3/6.3 tail-typicality qualifiers (R2 MAJOR-3).
5. Section 5 table summary narrowed (R2 MAJOR-4).
6. All S2-table sentences re-scoped (R2 MAJOR-5).
7. Certificate wording split three ways (R2 MAJOR-7).
8. MINOR-1/3/4 wordings; NOTE-2 gloss.
9. Section 11 records both dispositions; the convergence set
   {P3.2, /16, A''} noted as cross-family methodology datum.

## 4. Recommended verdict wording (v2, executed in the dossier)

Core sentence: "No unconditional (E2')-supply theorem is produced.
Within the D0.2/D0.2' max-entropy floor route the obstruction is
proved route-relative and measured above threshold at every
reported scale, with an HL-frame heuristic asymptote predicting
persistence (tensorization registered open, U17.11); the T1
transplant requires three inputs (class lower bound; growing-k
extension constant o(ln x), unavailable to every displayed sieve
bound, F17.9; tail intersection); the model gate finds no
architectural contradiction; certificates extend to the first
b > 1 sites."

## 5. Process findings (register candidates)

B3. Cross-family convergence: R1 and R2 independently found the
    identical three defects (P3.2 threshold, /16 floor, A''=16
    vacuity) from the same object -- the strongest process signal
    this project has recorded for the two-role review design.
B4. The verdict-layer/body-layer split failure mode recurred from
    item-0005 (P1 pattern): scope qualifiers present in the body
    were dropped exactly at the promotion into Section 1. Rule
    candidate: the verdict section must be diffed clause-by-clause
    against the body's support classes BEFORE the review gate, by
    a dedicated pass.
B5. In-run checker limitation: same-run checkers verified
    constants but could not audit dependency structure (R2
    MAJOR-1) -- computation audits need an explicit
    "dependency/conditioning" checklist item beyond constants.

## 6. Merge gate recommendation

Revise to v2 on the branch (EXECUTED, same commit series); operator
re-checks the diff; R2's reviewer may optionally be shown the v2
delta for a closing comment; then operator ratification decision on
the v2 verdict. The mandate's acceptance clause remains discharged
on the obstruction branch (named obstructions with exact
quantitative gaps -- now with honest scope -- plus the certificate
layer); BET-07 relevance unchanged (evidence against unconditional
progress).
