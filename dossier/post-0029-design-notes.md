# Post-0029 design notes (steering; items 0035-0038 proposed)

Lane: STEERING (Claude Fable 5, analysis sandbox), 2026-08-04, on
operator instruction, authored at a pin equal to the ANN-98 apply
commit == HEAD of main. Emitted as part of a git am mbox; the
operator apply is the ratifying commit. Status of everything below:
PLANNING. These notes price and frame four proposed items; they are
drift-invariant planning artifacts in the sense of the roadmap-store
constitution -- the byte-exact execution contract for any of them is
authored ephemerally at dispatch time against the then-current pin,
never copied from here. Nothing here is a result. Support classes are
used as in the dossier: PROVED / PROVED-DOSSIER (existing artifacts),
RECORDED (quoted from an anchor), MEASURED, HEURISTIC (steering
reasoning in this note, to be established or destroyed by the item),
OPEN.

Source discipline: every source-facing sentence below cites the CLEAN
extracts under `dossier/item-0029-workpapers/extract/` (rule 26(4));
every project-facing sentence cites its in-tree anchor. The four
registered bets (BET-20260804-14..17, `ledger/bets.yaml`) are
registered with this apply, before any evidence exists, per the
ledger's registration rule ("bets are written here BEFORE evidence
arrives").

---

## 0. Context: what item-0029 left on the table

The Session M verdict (ANN-98) is V-NEG: the corpus yields no positive
proportion of word-grain flank classes with two distinct realized
middles, at any rank. The strongest supported family-axis shape,
verbatim from the S6 block of
`dossier/item-0029-workpapers/word-grain-adjudication.md`: "at fixed
rank on sparse scales: EXISTENCE of flank classes with two distinct
realized middles, derivably unbounded per-scale count, all but o(1)
of the tuple mass non-rigid, PROVED (finite algebra from
hildebrandmaier88-gaps.md (14), the Section 4.2 column count, Lemma 3
and Mertens; adjudication Section 5.2, sheet CM-5b)".

That PROVED object is new: the first word-grain non-rigidity mechanism
the project owns, at fixed rank. Two steering observations from the
verification of that derivation seed the first two notes; both are
HEURISTIC here and become items precisely so they stop being
heuristic:

1. The statement itself appears to FAIL in the even-Cramer-smooth
   model (Note EC-1): the model's monotone stretch structure caps
   distinct middles per fixed-rank class at two.
2. The derivation's own k-dependencies appear to admit slowly growing
   rank, with candidate ceilings one iterated logarithm or more below
   the exchange rank (Note RC-1a): the gap to the exchange point may
   be quantifiable rather than merely located.

The remaining two notes are hygiene and calibration made newly cheap
or newly urgent by the same close: the falsification machinery that
could threaten the frozen HLQuantA card is now fully in-corpus
(Note VA-1), and the Section J measurement campaign gains a
fixed-rank companion with a proved statement to calibrate against
(Note ME-1).

---

## 1. Note EC-1 (item-0035) -- separator instance certificate

### 1.1 Target statement

Certify the item-0029 fixed-rank conclusion as a STATEMENT-LEVEL
separator instance: a statement that is (a) proved for the primes
(unconditionally, from documented inputs, at every fixed rank
$`k\ge3`$ on sparse good-modulus scales) and (b) false in the
even-Cramer-smooth model. Part (a) exists (adjudication Section 5.2,
PROVED). Part (b) is the item: prove that in the model, at every
fixed rank $`k\ge3`$, every flank class carries AT MOST TWO distinct
realized middles, so "some class carries unboundedly many distinct
middles along a scale sequence" is false there.

The model, verbatim from
`dossier/item-0010-workpapers/separator-repricing.md` W3.1:

$$
q_1=2,\ q_2=3,\ q_3=5,\ q_4=7,\qquad
q_{n+1}=q_n+2\left\lceil\tfrac{\ln{}q_n}{2}\right\rceil\ (n\ge4)
$$

### 1.2 The steering sketch (HEURISTIC; disclosed at bet registration)

The model gap sequence is non-decreasing, constant $`=2m`$ on each
stretch $`q_n\in(e^{2m-2},e^{2m}]`$ (the one-line structural fact
F-MODEL already uses, adjudication Section 8). For a fixed-rank word
of $`J`$ left-flank gaps, one middle, $`K`$ right-flank gaps
($`J,K\ge1`$, $`J+K+1=k`$): if the left flank is constant $`2m`$ and
the right flank constant $`2m'`$, monotonicity forces either
$`m'=m`$ (the site sits inside one stretch, middle $`=2m`$, class
rigid) or $`m'=m+1`$ (the site straddles exactly one boundary, and
the middle gap is the boundary-adjacent gap, hence $`\in\lbrace
2m,2m'\rbrace`$: at most two realized middles). Mixed flank words
(a step inside a flank) pin the boundary position inside that flank
and force the middle entirely. So every fixed-rank model class
carries at most 2 distinct middles -- against the primes' derivably
unbounded count. The D0-depth precedent for exactly this class
structure is already PROVED-DOSSIER, verbatim from
`separator-repricing.md` W3.2: "classes number $`\sim\ln{}x/2`$ (one
size-2 class per realized gap-value step ...), carrying
$`O(\ln{}x)`$ non-rigid sites"; the item transports the argument to
fixed rank and writes it at dossier grade.

### 1.3 Deliverables, kill criterion, pricing

Deliverables: one short certificate workpaper (the model bound
PROVED; the pairing with the primes-side PROVED statement; an
explicit NON-TRANSFER paragraph: fixed rank only, no claim at the
growing D0 depth, no verdict on S1, (CG) or B2.pairs; a
both-readings entry); optionally a small enumeration script over the
model at $`k=3..6`$ whose outputs stay MEASURED-labeled finite
checks. Kill criterion (named now): if the model admits a fixed-rank
class with three or more distinct middles, the sketch is wrong, the
premise dies, and the item records the counterexample and stops --
that outcome resolves BET-14 NO and is itself a deliverable.

Rule-15 pricing: not engaged -- the statement is fixed-rank and no
exchange-regime constant enters; the note records this
non-engagement explicitly rather than silently. Cost: one small
session.

### 1.4 D3 ex-ante no-go audit (questions per the standing kickoff D3
### list, `dossier/relext-statements.md` Section 9)

(i) k!/2^k/exp(k log k) growth: none, fixed rank -- pass. (ii)
secretly at least as strong as an open HL uniformity: the target is
a negative statement about a deterministic model; nothing conjectural
is consumed -- pass. (iii) caps inside the count from the start: the
model enumeration is exact -- pass. (iv) unproved tensorization or
growing-k compounding presupposed: none -- pass. (v) marginal
statistics used as window statistics: per-class exact claims in a
deterministic system -- pass. (vi) finite measurement treated as an
asymptotic constant: the optional script is MEASURED-labeled and the
claim is proved for all large scales -- pass, with the label
mandatory. VERDICT: PASS.

### 1.5 Why this is worth a session

It converts F-MODEL's input-level failures into the project's first
concrete word-grain separator INSTANCE (wrong rank, right shape),
sharpening what the S1 hunt is looking for: the deciding fact of
W4.S1 asks for a statement that "fails in the even-Cramer-smooth
model", and this would be the first in-house specimen of that
property at word grain, with the exact mechanism of failure (AP
alignment and monotone stretches) named. Bet: BET-20260804-14,
p 0.90.

---

## 2. Note RC-1a (item-0036) -- rank-ceiling sheet

### 2.1 Target question

Price mechanically: how fast may $`k=k(x)`$ grow before the
adjudication Section 5.2 chain (tuple floor against per-middle
ceiling) stops closing, when every constant is carried k-uniformly
under NAMED hypotheses? Output: a ceiling $`k^{*}(x)`$ per hypothesis
row, its growth class in the item-0028 vocabulary, and the NAME of
the binding wall -- against the exchange rank
$`k=(2/\ln2+o(1))\ln\ln{}x`$.

### 2.2 The walls to price (each HEURISTIC until the sheet runs)

- W-A (Lemma 3 constant + Mertens power). The per-middle ceiling
  carries $`\ll_g`$ of hm88 Lemma 3 ("the implied constant depends
  only on g", extract Section 3.3) times $`(V(z)z)^{-k}`$; the
  divergence margin is
  $`\log`$-ratio $`\ \asymp\ \ln{}z-\ln{}C_{k+1}-(k-1)\ln{}T-k(\gamma+\ln\ln{}z)`$
  with $`\ln{}z\asymp\ln\ln{}x`$. Under the hypothesis rows
  $`C_g\le C^{g}`$ and $`C_g\le e^{cg\ln{}g}`$ (sieve-typical), and
  with the T, c coupling of W-C, the candidate ceiling is
  $`k^{*}\asymp\ln\ln{}x/\ln\ln\ln{}x`$ -- one iterated logarithm
  below the exchange rank, the GC-ITLOG distance class of the
  item-0028 verdict.
- W-B (Lemma 4 uniformization ledger). The printed Lemma 4 proof
  (extract Section 3.5) fixes $`K`$ and $`\delta`$ as constants and
  sets $`K_1=2K^{1/\delta}`$; its negligible clause bounds the
  $`K_1`$-smooth alternative by "at most $`(\log{(Kz)})^{A}`$
  integers ... with a suitable $`A=A(K_1)`$". Carried k-uniformly
  with $`K=T\asymp k`$, $`\delta=c/T`$, $`T/c=O(1)`$ one gets
  $`K_1=\mathrm{poly}(k)`$ and a smooth-count exponent
  $`A(K_1)\asymp\pi(K_1)`$, giving the candidate constraint
  $`\pi(K_1)\cdot\ln\ln{}z\lesssim\ln{}z`$, i.e. a candidate ceiling
  near $`(\ln\ln{}x)^{1/2+o(1)}`$ -- possibly BELOW W-A. Which of
  W-A/W-B binds is exactly what the sheet decides; the two are
  recorded as discriminanda, deliberately not bet on separately.
- W-C ((11)-side coupling). The matrix prime floor needs the Lemma-4
  constant $`c`$ large in k (extract Section 4.2: "If we now choose
  the constant c sufficiently large, then we have" display (11), with
  the average "at least 3k primes" per row), and Lemma 4 needs
  $`0<\delta=c/T<1`$, so $`T>c`$: T grows with k and feeds
  $`T^{k-1}`$ into W-A. The sheet prices the coupling explicitly
  instead of absorbing it.
- W-D (good-moduli and range checks). Lemma 3's spacing hypothesis
  $`\le z^{2}`$ against the window $`Tz`$; Lemma 1's $`x\ge q^{D}`$;
  the (14) floor's $`R\ge2k`$ clause -- cheap columns, listed for
  completeness.

### 2.3 Sheet design, non-scope, verdict rule

Grid and conventions: reuse the item-0028 sheet frame verbatim (D0
grid, expo convention, growth-class vocabulary, self-check
discipline; `dossier/item-0028-workpapers/class_restricted_sheet_28.py`
as the precedent). Candidate schedules to tabulate:
$`k\in\lbrace5,\ (\ln\ln{}x)^{1/2},\ \ln\ln{}x/\ln\ln\ln{}x,\ \beta\ln\ln{}x\rbrace`$.
Per hypothesis row and schedule: the margin exponent of every wall,
the binding wall's name, and the resulting growth class of
$`k^{*}(x)`$. Mechanical verdict rule fixed at kickoff time (byte-
fixed there, not here), of the S6 family: it must decide BET-15's
two halves ($`k^{*}\to\infty`$; $`k^{*}=o(\ln\ln{}x)`$) per row.

NON-SCOPE, binding: no proof work. The k-uniform re-derivation of
(11)/(14), the growing-K Lemma 4 and an explicit-constant Lemma 3
are the GATED SUCCESSOR RC-1b (Section 6), which would need a
Halberstam-Richert anchor as an operator-gated rule-26(5) extraction
event; this sheet consumes only what the CLEAN extracts document
plus named constant hypotheses, each labeled as a hypothesis row.

### 2.4 D3 audit

(i) the growth factors are the OBJECT of the sheet, priced not
consumed -- pass by construction. (ii) no HL-strength input; the
hypothesis rows are sieve-constant shapes, compared against nothing
conjectural; any row that would smuggle a uniformity stronger than
frozen HLQuantA is an immediate FLAG line the verdict rule must
carry -- pass with that guard. (iii) the per-middle ceiling is a cap
already inside the chain; the sheet keeps it explicit -- pass. (iv)
growing-k compounding: NOT presupposed; the uniformization debts of
(11)/(14)/Lemma 4 are listed as debts, which is the point -- pass
with the ledger mandatory. (v) marginal-vs-window: not engaged --
pass. (vi) finite-vs-asymptotic: the sheet is symbolic-asymptotic
with grid instantiation; grid values are labeled reference-only --
pass. VERDICT: PASS as a pricing item.

### 2.5 Value

Whatever the outcome, A3 stops being only a located absence: either
the ceiling is quantified (and the distance to the exchange rank
becomes a named, priced object, informing the route-C question and
RC-1b), or the chain dies at fixed rank under every named hypothesis
(and the matrix line is closed with a price tag). Bet:
BET-20260804-15, p 0.75. Cost: one item-0028-class session.

---

## 3. Note VA-1 (item-0037) -- vacuity audit of the frozen card

### 3.1 Target question

The round-1 theorem consumes HLQuantA at its frozen uniformity
(`lean/Erdos251/Hypotheses.lean`, the check-frozen block; per its
docstring the card is a two-sided factor-2 tuple count over all
large $`x`$, tuple size at most $`4\ln\ln{}x`$, even offsets
containing 0, offsets at most $`(\log{}x)^{3}`$ -- paraphrase, the
audit reads the Lean statement verbatim). The Maier-genre limitation
literature falsifies UNIFORM equidistribution statements; since
ANN-97 the founding falsification machinery is fully in-corpus as
CLEAN extracts. Q0: does any documented falsification instance
intersect the frozen card inside the card's own quantifier ranges?
If yes, the conditional theorem risks vacuity and T2 of the
counter-proof program is free; if no, the card is certified
consistent with the documented zones and the theorem's price is
real.

### 3.2 Method (corpus-only first pass)

Task A: enumerate the documented falsification mechanisms with their
exact scopes -- the maier85 oscillation Theorem (short intervals
$`(x,x+\Phi(x)]`$, $`\Phi(x)=(\log{x})^{\lambda_0}`$, $`\lambda_0>1`$,
per the extract's Theorem), the hm88 matrix rows ("intervals of
consecutive integers ... exceptionally few primes", extract Section
2.2) with their row length $`Tz`$ and sparse good-z scales, and the
Lemma-1/Lemma-2 good-moduli AP inputs both extracts consume. Task B:
map each mechanism against the card's quantifiers (global count over
$`n\le x`$ vs short-window statements; tuple size; offset span;
two-sided factor 2), and record per instance: DISJOINT (with the
separating quantifier named) or INTERSECTS (with the instance
written out) or UNDECIDED-IN-CORPUS (with the missing anchor named
-- the Friedlander-Granville AP-uniformity zone is the expected
candidate there, and its extraction is a separate operator-gated
rule-26(5) event, not this item). Mechanical verdict: CLEAR iff
every documented instance is DISJOINT; INTERSECTS iff any instance
is written out; else INCONCLUSIVE with the named anchor.

The HEURISTIC expectation, recorded for calibration: CLEAR. The
card's global-count form was chosen after triage-1b Q1 killed the
over-uniform variant, and the documented zones live in short windows
and sparse row sets that a global two-sided factor-2 count does not
see. The residual face nobody has checked -- and the reason this is
an audit, not a formality -- is the span-$`(\log{}x)^{3}`$ offset
range combined with tuple sizes near $`4\ln\ln{}x`$.

### 3.3 D3 audit and pricing

(i) none -- pass. (ii) this item IS question (ii) run in earnest
("secretly at least as strong as an open HL uniformity (compared
against frozen HLQuantA verbatim)" -- the standing D3 text), pointed
at the card itself -- pass by identity. (iii)-(v) not engaged --
pass. (vi) no measurement -- pass. VERDICT: PASS. Cost: one small-
to-medium session, corpus-only. Bet: BET-20260804-16, p 0.85.
Protection value: this is insurance on the exact statement item-0027
is scheduled to build a Lean integrator around, which is the
sequencing argument of Section 7.

---

## 4. Note ME-1 (item-0038) -- Section-J campaign plus fixed-rank census

### 4.1 Target

Execute the standing measurement specification of
`dossier/item-0010-workpapers/collision-gap-audit.md` Section J --
whose own binding first line is "Do not execute this campaign
without a later ratified dispatch" (this item, once ratified, is
that dispatch's warrant) -- rows J.1-J.6 exactly as specified, with
row 3 (admissible-middle multiplicity $`A_P`$) the headline: the
late-anchor site-mass distribution of $`A_P`$ is the one measurable
quantity that speaks to the T3 rigidity door of the counter-proof
program, and it is UNMEASURED.

Companion, separately labeled per Section J's own rule on
sub-frontier diagnostics: a FIXED-RANK census at $`k=3..5`$ --
class populations, $`N_{P,d}`$ spectra, distinct-middle histograms,
$`Q>0`$ counts -- giving the first nonzero-Q word-grain tables and a
finite-scale face for the item-0029 PROVED statement and the
(future) item-0035 model contrast.

### 4.2 Discipline and pricing

Binding: exact rational arithmetic where Section J demands it; the
ANN-63 reading cautions on every interpretation line; no row
promoted to an asymptotic constant (Section J: "no row may be
promoted to an asymptotic constant or proof"); measurement-only, no
verdict on S1, (CG) or B2.pairs. Compute: the frozen census range
(to $`10^{9}`$) is workstation-class per the existing runs; the
fixed-rank companion at $`k\le5`$ is cheaper than the D0 ladder
(shorter words, no depth coupling); the executor prices the exact
budget in the kickoff. D3: (vi) is the heart and is answered by the
Section J language quoted above -- pass with the labels mandatory;
(i)-(v) not engaged -- pass. Bet: BET-20260804-17, p 0.80 (the
$`A_P\ge2`$ majority claim; the Section H heuristic expects growth,
nothing is measured, which is the point).

---

## 5. What is deliberately NOT itemized here

- RC-1b, the growing-k theorem (k-uniform (11)/(14); Lemma 4 at
  growing K -- its full proof is printed in the extract, so the
  uniformization is checkable in-corpus; Lemma 3 with explicit
  g-dependence, which needs a Halberstam-Richert anchor as a
  rule-26(5) operator-gated event). GATED on the item-0036 verdict;
  priced there before any proof investment, per rule 15.
- The route-C design note (matrix as a relative S1 carrier /
  MatrixMiddleSpread; the rank-re-entry question Q0). GATED on
  item-0036 for the same reason: its make-or-break wall is the one
  the sheet prices.
- The anti-model certificate (a T-conforming diverse deterministic
  system with (CG) true, Beurling frame) -- parked; conceptual
  value, no current gate.
- The certified continued-fraction scan of the denominator floor
  (counter-proof door T1) -- parked insurance; cheap whenever
  wanted; must first read the method of the standing floor before
  superseding it.
- The LI-resonance exposition note for status.md -- parked;
  exposition only.

Each of these, if taken up, gets its own note and registration
first; none is scheduled by this file.

---

## 6. Priority proposal (PROPOSAL ONLY; scheduling is the operator's)

Proposed execution order once (and if) the operator ratifies the
four items:

1. item-0035 (EC-1) -- smallest, closes an open F-MODEL cell, first
   separator instance.
2. item-0036 (RC-1a) -- cheap sheet whose verdict gates RC-1b and
   the route-C note; highest strategy leverage per cost.
3. item-0037 (VA-1) -- insurance on the round-1 asset, newly cheap.
4. item-0027 -- unchanged content, see below.
5. item-0030 -- unchanged, the designated item-0010 re-scope feeder.
6. item-0038 (ME-1) -- compute-bound; its A_P output also informs
   the re-scope discussion before item-0010 runs.
7. then item-0010, item-0006, item-0024 as ordered today, with the
   gated successors (RC-1b, route-C note) decided after the
   item-0036 verdict.

On the operator's question whether item-0027 and item-0030 stay on
top: YES IN SUBSTANCE, with the cheap trio slotted ahead. Grounds:
(a) nothing in the item-0029 outcome weakens item-0027 -- its own
body records it as branch-agnostic ("Independent of the item-0026
outcome and needed in both branches") and the V-NEG outcomes make
the machine-checked interface MORE valuable, since an obstruction
verdict should be stated about a machine-checked route; (b) but
item-0037 is cheap insurance on the exact hypothesis item-0027
formalizes an integrator around, and cheap-before-expensive is the
right order for insurance; (c) items 0035/0036 are one-session-class
with outputs that shape route-C and RC-1b decisions the operator
will face right after; (d) item-0030 stays immediately after
item-0027 exactly as HANDOVER records it: the item-0010 re-scope is
"deliberately deferred until item-0030 returns", and nothing here
changes that. The counter-case, recorded: if the operator weights
Lean-lane momentum, running item-0027 first and the trio after costs
little -- none of the trio's outputs gates item-0027's content, only
its insurance ordering.

END OF POST-0029 DESIGN NOTES
