# item-0029 word-grain adjudication (Session M)

Lane: EXECUTOR (local workstation, Claude Code; model string
claude-fable-5). Dispatch: `item-0029-kickoff-M-v1.md` (ephemeral,
never committed; the operator apply is the ratifying commit).
Section 0 pin `7bed96ac7bd688025342d76dddf507a70682b09b` == HEAD at
session start. Web OFF, cloud OFF; no PDF opened; the withheld
`shiu00-strings.md` never opened. Source layer (rule 26(4)): the four
graded-clean-and-hashed extracts under
`dossier/item-0029-workpapers/extract/` are the only source
surrogates consumed, each verified against its `payloads/HASHES.txt`
line before first consumption; every source-facing claim cites its
extract, every project-facing claim its in-tree anchor. Support
classes: proved-in-source / stated-without-proof-in-source /
conditional-in-source / absent-from-corpus (Task A vocabulary);
PROVED (finite algebra here, from documented statements); RECORDED;
MEASURED (a sheet value); OPEN. Companion sheet:
`maier_matrix_sheet_29.py` emitting
`maier_matrix_sheet_29_tables.txt` (the CM columns cited below).

---

## 1. Verification table V-M (outcomes; one-line table in the report)

Gates V1-V3 and V7 HOLD (freshness; twelve hash verifications;
P1-P5; sheet self-checks) -- one line each in `item-0029-report-M.md`
Section 2. The record rows, precisions kept, not absorbed:

- V4: CONFIRMED on all four booked purposes. (a) hm88: the matrix
  method at k consecutive gaps with the VALUE-axis conclusion
  $`\lambda(S^{(k)}\cap[0,T]^k)\ge c(k)T^k`$ (Theorem, p.2).
  (b) freiberg10: Shiu-modelled construction with GPY weights
  (Section 5.2; (2.7)), the pigeonhole step (Section 3), Prop. 2.3,
  the row count ((6.8)). (c) freiberg11: the all-large-H
  strengthening (Lemma 3.4), count $`X^{1-c/\log{}\log{}X}`$ ((1.2));
  precision: in-scope Lemma 3.3 carries only "Proof. See 4." -- the
  Selberg-Delange attribution lives in the scope declaration, not a
  transcribed passage. (d) maier85: the oscillation Theorem (p.221),
  the matrix (Section 4.1), the good-modulus input; precision
  (extract FLAGS): Lemma 2 is headed "(Gallagher)" but its proof line
  cites [7, Lemma 2] plus the prime number theorem; the bracketed [3]
  does not appear in the body.
- V5: CONFIRMED. The freiberg11 header declares the PARTIAL scope,
  Section 7 the boundary; honoured -- no clause rests on
  Section-4-only content beyond its named reference.
- V6: CONFIRMED. W4.U20.4 reads as quoted ("statements about gap
  *size* and about the limit-point set of *normalized* gaps, not
  positive-proportion coincidences of a growing-length [...] integer
  flank word realized twice with distinct middles", elision marked);
  `literature-consolidation.md` Section 2: "A3 fails for all seven
  anchors." Held as PRIOR only; determinations were made against the
  extracts.

---

## 2. Fixed definitions and the question

The word-grain vocabulary is fixed against `collision-gap-audit.md`
B.1: a WORD-GRAIN FLANK CLASS is a realized flank class $`P`$
(members share one left flank word of $`J`$ and one right flank word
of $`K`$ consecutive prime gaps; $`N_{P,d}`$ counts members with
middle gap $`d`$); "two distinct realized middles" means $`d\ne e`$
with $`N_{P,d}\ge1`$ and $`N_{P,e}\ge1`$. Governing display,
verbatim from `collision-gap-audit.md` B.3:

$$
 \boxed{
 N-F-Q
 =\sum_P\frac2{N_P}\sum_{d<e}N_{P,d}N_{P,e}\ge0.
 }
$$

with consequence 3 verbatim: "$`Q<N-F`$ if and only if some realized
class contains two different realized middles." The exchange
evaluation point is rank $`k=(2/\ln2+o(1))\ln\ln{}x`$, window
$`A'L\ln{}x`$, on the D0 grid, parameter map re-declared in the
sheet. The item's single gate is adjudicated in Section 6.

---

## 3. Task A -- the schema, reconstructed from the four extracts

### A-1 The matrix construction per source

1. `maier85-shortintervals.md` Section 4.1 (proved-in-source,
   definitional), verbatim display ($`\mathfrak{M}=(a_{rs})`$):
   $$a_{rs}=s+rP(z),\quad1\le s\le U,\quad P(z)^{D-1}<r\le2P(z)^{D-1}.$$
   with $`P(z)=\prod_{p<z}p`$ (strict inequality; extract FLAGS),
   $`U=U(z)\le P(z)`$; "The rows of $`\mathfrak{M}`$ are intervals of U
   consecutive integers, whereas the columns of $`\mathfrak{M}`$ are
   arithmetic progressions with common difference $`P(z)`$."
2. `hildebrandmaier88-gaps.md` Section 4.2 (proved-in-source,
   definitional): $`a_{rs}=rP(z)+s`$ for $`R<r\le2R`$,
   $`y<s\le y+Tz`$, $`R=P(z)^{D-1}`$, $`P(z)=\prod_{p\le z}p`$
   (non-strict; extract FLAGS), y supplied by Lemma 4 with $`K=T`$,
   $`\delta=c/T`$. Method sentence (Section 2.2, verbatim): "The key
   idea is to construct a matrix, whose rows are intervals of
   consecutive integers, and which contains exceptionally few primes."
3. `freiberg10-strings1.md` Sections 2-3, 5.2 (proved-in-source,
   definitional): rows $`(Qn,Qn+H]`$, $`n\in(N,2N]`$,
   $`H=\epsilon\log{N}`$; modulus the Shiu-type $`Q=Q(H)`$ of (5.19)
   (the primes of $`\mathcal{P}(H)`$ except $`p_0`$, times q); offsets
   split into S and T ((2.12)). `freiberg11-strings2.md` (3.1)-(3.6)
   restates it with the $`t(H)`$ window (3.2) and $`p_0`$ clause (3.5).

### A-2 The distributional input each source consumes

1. `maier85-shortintervals.md` Section 3.3 (stated-without-proof-in-
   source; the printed proof line is a reference to [7, Lemma 2] plus
   the prime number theorem): Lemma 2, the AP prime count
   $`\pi(x+h,q,a)-\pi(x,q,a)=\frac{1}{\varphi(q)}(\mathrm{li}(x+h)-\mathrm{li}\,x)(1+O(e^{-cD}+e^{-\sqrt{\log{x}}}))`$
   for good modulus q, $`(a,q)=1`$, $`x\ge q^{D}`$, $`x/2\le h\le x`$,
   $`\log{q}\ge D\ge D_0`$. Good moduli only; Lemma 1 (Section 3.2, by
   reference to [7, Lemma 1]) supplies "arbitrarily large values of z
   for which the modulus $`P(z)`$ is good".
2. `hildebrandmaier88-gaps.md` Section 3.2 (stated-without-proof-in-
   source, "can be derived from a large sieve type estimate of
   Gallagher [3] (cf. [5, Lemma 2])"): Lemma 1, uniformly for
   $`x\ge q^{D}`$, $`(a,q)=1`$:
   $`\pi(2x,q,a)-\pi(x,q,a)\gg x/(\varphi(q)\log{x})`$; Lemma 2
   (Page): arbitrarily large good z. Section 3.3 (stated-without-
   proof-in-source, from [4, Theorem 2.3]): Lemma 3, for fixed g,
   $`0<\lvert s_i-s_j\rvert\le z^{2}`$, $`R\ge2`$:
   $$\lvert\lbrace1\le r\le R:rP(z)+s_i\ \text{prime for}\ i=1,\ldots,g\rbrace\rvert\ll_g\frac{R}{(V(z)\log{R})^{g}}.$$
   Section 3.4-3.5 (proved-in-source): Lemma 4, the $`\delta`$-thin
   coprime window -- an integer-sieve statement, prime-free.
3. `freiberg10-strings1.md` Sections 3-5: Prop. 2.2 ((2.9), (2.10);
   proved-in-source as an outline -- the source: "we will only
   outline a proof of each of them, referring to [3] and [5] for
   details" -- via Lemma 4.1 with the $`Qp_0`$ exclusion); Lemma 4.2
   (the BV variant, "which is Lemma 2 of [5]";
   stated-without-proof-in-source), range (4.7)/(4.8), saving
   (4.9)/(4.10); Lemma 2.1 (Landau-Page, quoted from [2, Chapter 14]).
4. `freiberg11-strings2.md` Section 3 (in scope): Theorem 3.1
   (Siegel-Walfisz, from [9, 11.3, Corollary 11.20]), uniform for
   $`1\le q\le(\log{X})^{A}`$; Lemma 3.2 (Mertens in 1 mod q; q=1,2
   settled in scope, the $`3\le q`$ range deferred to Section 4) and
   Lemma 3.3 (integers with all prime factors $`\equiv1\bmod q`$ and
   $`>Y`$; "Proof. See 4."), both proofs outside the declared scope;
   Lemma 3.4 (proved-in-source from 3.1-3.3).

### A-3 The averaging step

1. `maier85-shortintervals.md` Section 4.1 (proved-in-source): the
   column counts assemble the matrix total (3.1); the per-row average
   is compared against the Buchstab/Mertens expectation
   $`e^{\gamma}\omega(\lambda)`$ (Lemma 3).
2. `hildebrandmaier88-gaps.md` Section 4.2 (proved-in-source): columns
   $`\asymp cV(z)z`$ (Lemma 4), per-column count $`\gg R/(V(z)z)`$
   (Lemma 1), hence (11); Section 4.3, verbatim: "By (11), a row in A
   contains on average at least 3k primes."
3. `freiberg10-strings1.md` Section 3 (proved-in-source): the
   weighted average $`\mathcal{L}`$ over $`n\in(N,2N]`$ of
   $`\sum_{h\in S}\vartheta(Qn+h)-\sum_{h\in T}\vartheta(Qn+h)-\log{3QN}`$
   with weight $`\Lambda_R^{2}`$, evaluated by Prop. 2.2 and driven
   positive by (3.1), giving (3.2).

### A-4 The existence-extraction step (the decisive objection's target)

1. `maier85-shortintervals.md` Section 4.2 (proved-in-source),
   verbatim: "By (3.1) and Lemma 3 there is at least one row of
   $`\mathfrak{M}`$ with at least" [the average] "primes." -- averaging
   to ONE row, then one subinterval $`(a_l,b_l]`$ of that row. Output
   per scale: one interval.
2. `hildebrandmaier88-gaps.md` Sections 4.3-4.5 (proved-in-source):
   majority counting -- good rows hold $`\ge2k`$ primes, (12) gives
   $`\ge kR`$ primes in good rows, (14) at least $`\tfrac12kR`$
   consecutive-(k+1)-tuples; the per-box ceiling (19) $`\ll RN^{-k}`$
   converts the total into (17): $`\gg N^k`$ hit boxes in value
   space. The lower-bound mechanism is count-over-cap: a total
   divided by a per-cell ceiling forces many DISTINCT cells hit.
3. `freiberg10-strings1.md` Section 3 (proved-in-source), verbatim:
   "If $`\mathcal{L}>0`$, then there is some $`n\in(N,2N]`$ such
   that" [the S-mass beats the T-mass plus $`\log{3QN}`$] --
   pigeonhole to ONE row per scale; Section 6 strengthens the count
   via Cauchy-Schwarz against (6.2), giving (6.8):
   $`{\sum}^{*}1\gg_{\epsilon,q}N/(\log{N})^{B(\epsilon)}`$.

### A-5 The multiplicity structure

Documented quantitative bounds, complete list (each proved-in-source
in its extract): hm88 (11) ($`\ge3kR`$ primes), (12) ($`\ge kR`$ in
good rows), (14) ($`\ge\tfrac12kR`$ tuples), (19) ($`\ll RN^{-k}`$
per box), (17) ($`\gg N^k`$ boxes); freiberg10 (3.2), (6.2) (fourth
moment $`\ll N(\log{N})^{19k+4\ell}`$), (6.8) (rows
$`\gg N/(\log{N})^{B(\epsilon)}`$), (6.1); freiberg11 (1.2) (strings
up to X $`\ge X^{1-c/\log{}\log{X}}`$, all sufficiently large X). A
lower bound on the number of good rows (as against the primes they
hold), a per-word or per-class realization lower bound, and any
count of favourable objects per family are absent-from-corpus.
CM-4/CM-5 price these counts against the word-grain populations.

### A-6 The consecutiveness mechanism

1. Interval rows (maier85, hm88): rows are intervals of consecutive
   integers, so in-row primes are consecutive primes; hm88 (13)
   reads tuples
   $`(a_{rs_1},\ldots,a_{rs_{k+1}})=(p_n,\ldots,p_{n+k})`$ "of
   consecutive primes in the rows" directly (proved-in-source).
   Cost: none beyond the row structure.
2. The S/T-imbalance pigeonhole (freiberg10 Section 3,
   proved-in-source), verbatim:
   "$`\lvert A_n\rvert\ge\lvert B_n\rvert+2`$, and so, by the
   pigeonhole principle, $`A_n`$ contains a pair of consecutive
   primes $`p_r,p_{r+1}`$." Cost: the modulus must make "almost all
   of the integers $`h\in[1,H]`$ that are coprime with Q ...
   congruent to $`a\bmod q`$" (freiberg11 Section 2, verbatim), paid
   in admissible-column density ((3.14)) and, in freiberg10, in scale
   density (A-8).
3. Shiu-origin content is second-hand only (ANN-92): the Freiberg
   extracts carry the construction "modelled on that of Shiu's [9]"
   (freiberg10 Section 5.2), Lemma 5.2 = [9, Lemma 3], Shiu's set
   $`\mathcal{P}'`$ with $`\lvert S'\rvert\gg_q H\phi(Q')/Q'`$
   (freiberg11 Section 2), and Shiu's Theorem 2 count
   $`X^{1-\varepsilon(X)}`$ with both $`\varepsilon(X)`$ displays
   (freiberg11 Section 1). Anything deeper is OUT-OF-REACH (r29M.5;
   recorded, not load-bearing for any S6 clause).

### A-7 The output-axis taxonomy

1. maier85 Theorem (proved-in-source): oscillation of the normalized
   short-interval count -- VALUE axis, limsup/liminf form; no
   proportion of any family.
2. hm88 Theorem (proved-in-source; assembly printed, Lemmas 1-3 by
   reference per A-2): "positive proportion" is Lebesgue measure of
   the limit-point set in $`[0,T]^k`$ -- VALUE axis; the good-row
   step is majority counting inside the proof, and no family-axis
   proportion is stated.
3. freiberg10 Theorem 1.1 (proved-in-source): existence; Section 6:
   COUNT axis, a decaying share of the row population.
4. freiberg11 Theorem 1.1 (proved-in-source within declared scope):
   COUNT axis, all large X. No source states a ROW/FAMILY-axis
   positive proportion or any word-grain class-mass statement (the
   A3 absence, confirmed here at method grain).

### A-8 The scale structure

1. maier85 (proved-in-source): z through the good-modulus set
   ("arbitrarily large values", Lemma 1 -- a sparse sequence),
   $`z\ge e^{cD}`$, $`x\sim P(z)^{D}`$.
2. hm88 (proved-in-source): z from Lemma 2's set, then "a suitable
   subsequence" for the limit-point step (p.7).
3. freiberg10 (proved-in-source): Prop. 2.3's infinite H-sequence;
   Lemma 5.5 gives one $`H\in[X/(\log{X})^{A},X]`$ per large X --
   the sparseness (6.1) inherits, forced by the fixed-modulus
   asymptotic imported from [9, Lemma 3] (Lemma 5.2).
4. freiberg11 (proved-in-source in scope): Lemma 3.4 holds "for all
   sufficiently large H", removing the sparseness; the replacement
   input is the uniform Lemma 3.3 (proof outside scope).

---

## 4. Q-CORR -- the correspondence determination

**Outcome: CORR-NOT-ESTABLISHED.** The structural claim under test,
verbatim from the item: "the matrix method fixes residues modulo a
primorial and varies the row index, so a row family is shaped like a
flank class with many members, and the large-sieve density input the
method consumes is a statement about exactly that family."

Against the Task A record, with the kickoff 2.3 definitions fixed:

1. What the family index fixes. In every documented construction
   the row index at fixed modulus fixes the ADMISSIBLE OFFSET SET
   and nothing else: maier85 "Only those columns for which
   $`(s,P(z))=1`$ contain primes" (Section 4.1); hm88 (20);
   freiberg10 (2.12). Word-grain class membership requires sharing
   REALIZED flank words; no documented statement identifies, or
   transfers between, the two.
2. Matching flanks are not controlled by any documented statement:
   the only documented control over realized words is one-sided (hm88
   Lemma 3 and (19) are UPPER bounds); a lower bound for a PRESCRIBED
   word -- what would let the family index pin a flank word -- is
   absent-from-corpus.
3. Consecutiveness at flank length is not forced. The documented
   mechanisms (A-6) act inside one row; no documented step forces the
   flank word of $`J+K=L-1`$ gaps at the D0 depth
   $`J=K=(1+o(1))\log_2{}\ln{}x`$ to repeat across members. The
   Section 5.2 algebra forces repeated words -- distinct middles
   included -- at FIXED rank only; it reaches no growing depth
   (fixed-k quantifiers; CM-1).

Missing elements, named: (m1) matching flanks not controlled (no
per-word lower bound in the corpus); (m2) the family index fixes
admissible offsets, not the flank word; (m3) consecutiveness not
forced at growing flank length. The claim's second half is confirmed
as far as it goes -- the density inputs ARE statements about the row
family (hm88 Lemma 1 counts primes in exactly those columns) -- but
that family is not a word-grain flank class, and no documented
statement makes it one.

---

## 5. Q-SHAPE -- the output-shape determination

**Outcome (Section 5.2 Determination): not SHAPE-POSITIVE-PROPORTION
anywhere; PROVED existence with growing count at fixed rank; nothing
derivable at the growing D0 depth. The property throughout is itself,
never a proxy: two members of ONE family, equal flanks, distinct
middles.**

### 5.1 What the documented counting steps alone yield

1. Row families (the structural claim's candidate): one favourable
   row per scale (maier85 Section 4.2; freiberg10 Section 3 -- the
   characteristic pigeonhole output);
   $`\gg N/(\log{N})^{B(\epsilon)}`$ rows per scale (freiberg10
   (6.8)), a DECAYING share; $`\ge X^{1-c/\log{}\log{X}}`$ strings,
   all large X (freiberg11 (1.2)), a decaying share of $`\pi(X)`$.
   "Favourable" always means many primes in the row (hm88) or a
   consecutive pair within $`\epsilon\log{p_r}`$ (freiberg) -- never
   the two-distinct-middles property.
2. Value boxes (hm88): (17) yields $`\gg N^k`$ boxes hit, converted
   into $`\lambda(S^{(k)}\cap[0,T]^k)\ge c(k)T^k`$ -- a proportion OF
   VALUE SPACE, fixed k, sparse scales (proved-in-source). Distinct
   boxes certify distinct gap-VECTOR values at coarse resolution;
   equal flanks with distinct middles is an exact-integer coincidence
   that box membership neither implies nor excludes.
3. Word-grain flank classes at D0 depth: never mentioned; no
   class-mass bound $`N_{P,d}`$ either way (the A3 absence).

### 5.2 The finite-algebra check (PROVED): what is forced, where it stops

Two derivations were carried out from documented statements; the
second was located by this session's adversarial verification pass
(disclosed in the run report) and corrects the draft's weaker
reading.

1. Repeated words. From hm88 (14) ($`\ge\tfrac12kR`$ consecutive-
   (k+1)-tuples in A at fixed k; distinct tuples have distinct anchor
   primes, the rows being disjoint intervals) against the crude
   capacities ($`\le(Tz)^{k}`$ complete gap words, $`\le(Tz)^{k-1}`$
   flank words): both floor-to-capacity ratios tend to infinity,
   since $`\log{R}=(D-1)\sum_{p\le z}\log{p}\asymp z`$ while
   $`k\log{(Tz)}=O(\log{z})`$. At fixed k on large good z, some
   complete word is realized twice and some flank word $`\varphi`$
   carries $`M\ge kR/(2(Tz)^{k-1})`$ members (CM-5a prices both
   margins at the k=5 reference).
2. Distinct middles ARE forced at fixed rank. For a FIXED middle d,
   members of the $`\varphi`$-class are (row, position) pairs: the
   position is capped by the admissible-column count $`\asymp cV(z)z`$
   (hm88 Section 4.2, via Lemma 4; members satisfy (20)); for each
   fixed position, Lemma 3 at $`g=k+1`$ caps the rows by
   $`\ll R/(V(z)\log{R})^{k+1}\asymp R/(V(z)z)^{k+1}`$ (spacings
   $`\le Tz\le z^{2}`$; applied at 2R). The members-per-middle
   ceiling is $`C'_k R/(V(z)z)^{k}`$, uniform in d; against the
   floor:
   $$
    \frac{M}{C'_kR/(V(z)z)^{k}}\ \gg_k\
    \frac{(V(z)z)^{k}}{(Tz)^{k-1}}\ \asymp\
    \frac{z}{T^{k-1}(e^{\gamma}\log{z})^{k}}\longrightarrow\infty
   $$
   (Mertens, quoted in maier85 Section 3.4). On all large good z the
   heavy flank class cannot concentrate on one middle: it carries
   derivably $`\gg z/(\log{z})^{k}`$ DISTINCT realized middles. The
   same ceiling gives more: single-middle classes hold at most
   $`(Tz)^{k-1}C'_kR/(V(z)z)^{k}=o(R)`$ tuples, so all but $`o(1)`$
   of the (14) tuple mass lies in non-rigid classes, whose per-scale
   count is $`\gg_k V(z)^{k}z^{k-1}\to\infty`$ for $`k\ge2`$. PROVED
   (finite algebra from (14), the Section 4.2 column count, Lemma 3
   and Mertens; CM-5b prices the margin, divergence PROVED).

The derivation stops in two places:

1. No proportion, at any rank. No documented statement bounds
   $`F^{\mathrm{ms}}(x)`$ below or relates the non-rigid count to it:
   the SHARE is undetermined in either direction. The input that
   would decide it at the exchange rank is the S1 deciding fact,
   verbatim from `separator-repricing.md` W4.S1:
   "an unconditional averaged middle-slot non-concentration /
   upper-uniformity statement at rank $`k=(2/\ln2+o(1))\ln\ln{}x`$,
   window $`A'L\ln{}x`$, of strength enough to keep a fixed proportion
   of $`D0`$-depth site mass off its modal middle on some unbounded
   scale sequence per $`s`$ -- a statement that fails in the
   even-Cramer-smooth model." Scope of that absence, corrected: at
   FIXED rank the corpus's own Lemma 3 + Lemma 4 supply the
   middle-slot upper-uniformity surrogate used above; the quoted
   carrier is absent in its exchange-rank, D0-window,
   proportion-bearing form.
2. Nothing at the exchange rank. At depth $`k=L`$ the tuple floor
   (14) is undocumented (fixed-k constants; CM-1) and the mapped
   k-dependent factors are immediate rule-15 no-gos (CM-3, CM-2):
   neither derivation reaches the exchange point.

Determination. For the fixed-k matrix word classes -- the closest
documented family notion -- documented steps plus licensed finite
algebra yield an EXISTENCE statement with derivably growing
per-scale count of two-distinct-middle families (meeting and
exceeding SHAPE-BOUNDED-EXISTENCE's $`O(1)`$ guarantee) and
determine NO proportion of $`F^{\mathrm{ms}}(x)`$ either way. At the
growing word-grain depth nothing is derivable:
**SHAPE-NOT-DERIVABLE** there. Both bucket readings of the fixed-k
outcome give the SAME S6 clause (a) outcome -- not
SHAPE-POSITIVE-PROPORTION -- so no r29M.8 stop arises; both are
stated per that rule's discipline.

---

## 6. Verdict

Rule text and application below byte-identical with the tables' S6
block (kickoff Section 4.5).

```text
S6 VERDICT RULE (item-0029). Emit V-POS (positive proportion at
corpus grain) if and only if ALL of:
(a) Q-SHAPE = SHAPE-POSITIVE-PROPORTION at support proved-in-source
    or PROVED (finite algebra in this workpaper from statements the
    consumable extracts document, each cited), with the constant
    c > 0 independent of the scale, on an unbounded scale sequence;
(b) the counted property in (a) is two members of one family with
    equal flanks and distinct middles -- the property itself, not a
    proxy -- at the same support;
(c) Q-CORR = CORR-ESTABLISHED at support proved-in-source or PROVED,
    including the consecutiveness clause, OR the family object of (a)
    is itself already the word-grain flank class of the fixed
    definitions;
(d) every load-bearing constant and factor of the chain (a)-(c)
    appears as a sheet column with a growth class, and none is an
    immediate rule-15 no-go at the exchange evaluation point.
Otherwise emit V-NEG (bounded existence or weaker, at corpus grain):
name, for each failing clause, the exact failing element, and
classify the failure STRUCTURAL (the documented schema's own steps
yield only the weaker shape) or EVIDENTIAL (the corpus does not
document the needed step in either direction). In every outcome,
record the STRONGEST shape the corpus does support, with its axis
(A-7 taxonomy), its support class, and its citations.

CLAUSE-BY-CLAUSE DETERMINATION (mechanical; structural inputs from
word-grain-adjudication.md Sections 4-5, priced inputs from the CM
columns of maier_matrix_sheet_29_tables.txt):
(a) FAILS. Q-SHAPE is not SHAPE-POSITIVE-PROPORTION: no documented
    counting step, and no finite algebra licensed from documented
    statements, yields a lower bound c * F^ms(x), c > 0
    scale-independent, on families carrying two distinct realized
    middles, for any family notion at any rank
    (hildebrandmaier88-gaps.md (11)-(19) reach value-space boxes and
    tuple totals; freiberg10-strings1.md (3.2)/(6.8) and
    freiberg11-strings2.md (1.2) reach favourable-row counts; no
    extract documents family-population control either way).  What
    IS derivable (adjudication Section 5.2, PROVED): at every fixed
    k on the sparse good-modulus scales, the (14) tuple floor
    against the per-middle ceiling (Lemma 3 with the Section 4.2
    column count) forces flank classes carrying two -- derivably,
    unboundedly many -- DISTINCT realized middles: existence with
    growing count, short of every proportion form.  Failure class:
    EVIDENTIAL for the proportion step, with the PROVED fixed-k
    existence recorded below as the strongest family-axis shape.
(b) FAILS. The corpus's only positive-proportion conclusion
    (hildebrandmaier88-gaps.md Theorem, p.2) counts boxes of
    normalized difference tuples in [0,T]^k -- Lebesgue measure on
    the VALUE axis -- a proxy, not two members of one family with
    equal flanks and distinct middles.  Failure class: STRUCTURAL
    (the documented steps yield the value-axis shape, not the
    property).
(c) FAILS. Q-CORR = CORR-NOT-ESTABLISHED: the documented family index
    fixes the admissible offset set, never the realized flank word;
    no documented statement forces two family members to share flank
    words of consecutive prime gaps at the D0 depth J+K = L-1
    (missing elements named in adjudication Section 4); and no family
    object of (a) is itself the word-grain flank class of the fixed
    definitions.  Failure class: EVIDENTIAL.
(d) FAILS at the exchange evaluation point.  The load-bearing
    k-dependent factors of the documented chain, mapped to rank
    k = L = (2/ln2) lnln x, are immediate rule-15 no-gos: the GPY
    normalization (k+2 ell)! is the exp((1+o(1)) k ln k) class
    (CM-3a, expo 7.2 -> 9.8 > 1 at every scale, (G1) fails); the
    fourth-moment discount (log N)^{19k+4 ell} and the BV exponent
    4.5 k^2 are GC-FASTER (CM-3b, CM-2); the native regimes are
    fixed-k and do not reach the point (CM-1).  Failure class:
    STRUCTURAL (the documented schema's own normalizations carry the
    factors).

VERDICT: V-NEG (bounded existence or weaker, at corpus grain).
STRONGEST SUPPORTED SHAPES (recorded per the rule's final clause):
VALUE axis -- SHAPE-POSITIVE-PROPORTION of the limit-point cube:
lambda(S^(k) cap [0,T]^k) >= c(k) T^k, proved-in-source (assembly
printed, Lemmas 1-3 by reference), hildebrandmaier88-gaps.md Theorem
(p.2), fixed k, sparse scales.  ROW-COUNT axis --
SHAPE-DECAYING-PROPORTION of favourable rows, proved-in-source:
>> N/(log N)^{B(eps)} rows per scale (freiberg10-strings1.md (6.8))
and >= X^{1-c/loglog X} strings up to X for all large X
(freiberg11-strings2.md (1.2); Lemmas 3.2/3.3 proofs outside the
declared extract scope, by named reference).  FAMILY axis -- at
fixed rank on sparse scales: EXISTENCE of flank classes with two
distinct realized middles, derivably unbounded per-scale count, all
but o(1) of the tuple mass non-rigid, PROVED (finite algebra from
hildebrandmaier88-gaps.md (14), the Section 4.2 column count, Lemma
3 and Mertens; adjudication Section 5.2, sheet CM-5b) -- the
decisive objection's bounded-existence-type shape, sharpened; no
proportion of F^ms(x) is derivable either way at any rank, and at
the D0 depth k = L nothing is derivable (fixed-k, CM-1/CM-3).
```

Honest-scope paragraph (mirroring the item-0028 close): this
adjudication decides the item's single gate only; it records NO
verdict on the separator S1, on (CG), on B2.pairs, or on the
item-0010 campaign state; the S1 deciding fact is quoted as the name
of an absent exchange-rank input, neither re-priced nor upgraded.

---

## 7. Finding F-CONS -- consecutiveness survival

**Finding: the consecutiveness constraint SURVIVES the method at
pair grain inside one row (proved-in-source; longer strings
stated-without-proof-in-source), and at FIXED rank it survives to
matched flank words across members, distinct middles included
(Section 5.2, PROVED); it is NOT established to survive at word
grain -- the extension to the growing D0 depth is absent-from-
corpus.**

(i) The documented mechanism and its cost. Two mechanisms (A-6): the
interval-row mechanism (in-row primes are consecutive primes; hm88
(13); no cost beyond the construction) and the S/T-imbalance
pigeonhole (freiberg10 Section 3; freiberg11 Lemma 3.4, all-large-H).
Support: proved-in-source in both Freiberg extracts (scope note
applies); Shiu-origin provenance second-hand throughout (A-6(3)).
Cost: admissible-column density (the modulus thins coprime offsets
until $`\lvert T\rvert=o(\lvert S\rvert)`$; freiberg11 (3.9)/(3.19))
and, in the freiberg10 form, scale density (Prop. 2.3), which
freiberg11 removes.

(ii) Extension to the full flank word with matching flanks. Upward
from one pair the corpus documents only $`\nu+1`$-strings in one
row, stated-without-proof-in-source (freiberg10 Section 7, "it is
possible to prove"), and nothing about equality of gap words across
sites. By the Section 5.2 algebra the matched-flank form IS
reachable at fixed rank on sparse scales, distinct middles included
(PROVED); it is never reachable at the growing D0 depth (fixed-k
quantifiers; CM-1), where any extension inherits the CM-3 no-gos.
No documented cost exists for the depth extension because the step
itself is undocumented.

Shiu-2000-only content: nothing in this finding rests on it; what
it uses is carried at second hand by the Freiberg extracts (A-6(3));
OUT-OF-REACH recorded for anything deeper (r29M.5).

---

## 8. Finding F-MODEL -- even-Cramer-smooth failure of the inputs

Item body, verbatim: "Model failure is already established for the
method's classical result, so if the positive-proportion question
resolves favourably the separator requirement is met without further
work. Record it as a separate finding rather than assuming it
transfers." The model (verbatim from `separator-repricing.md` W3.1):

$$
q_1=2,\ q_2=3,\ q_3=5,\ q_4=7,\qquad
q_{n+1}=q_n+2\left\lceil\tfrac{\ln{}q_n}{2}\right\rceil\ (n\ge4)
$$

Structural fact used throughout (PROVED, one line): for $`n\ge4`$
and $`q_n\in(e^{2m-2},e^{2m}]`$ the increment is exactly $`2m`$, so
the model sequence from $`q_4`$ on is, within each such range, an AP
segment of difference $`2m`$ ("a stretch"), each stretch
multiplicatively long; and
$`\pi_{\mathrm{model}}(X)=(1+o(1))X/\ln{}X`$. The PRIORS, quoted,
neither re-derived nor assumed to transfer (W4.U20.4): the Maier row
-- "yes (model is smooth; Maier shows short-interval oscillation)"
-- and the limit-point category row -- "**yes** (normalized gap
$`\to1`$, so the limit-point set is the single point
$`\lbrace1\rbrace`$ of measure $`0`$; the unconditional
positive-measure limit-point statements fail)".

The A-2 inputs, each adjudicated against the model:

1. Good-modulus AP equidistribution (maier85 Lemma 2; hm88 Lemma 1):
   FAILS in the model, PROVED. Fix any modulus q with $`3\mid q`$
   (every hm88-form $`P(z)`$, $`z\ge3`$; maier85's strict product,
   $`z>3`$). For each of the unboundedly many m with $`3\mid m`$,
   choose x with $`(x,2x]`$ inside the increment-2m stretch: all
   model primes there lie in one AP of difference
   $`2m\equiv0\bmod3`$, hence in ONE residue class mod 3, so every
   class $`a\bmod q`$ in a different residue mod 3 receives $`O(1)`$
   model primes against the demanded
   $`\gg x/(\varphi(q)\log{x})\to\infty`$: the "uniformly for
   $`x\ge q^{D}`$" clause fails at unboundedly many x.
2. Siegel-Walfisz (freiberg11 Theorem 3.1): FAILS in the model,
   PROVED. At $`X=e^{2m}`$, $`3\mid m`$, the final stretch carries a
   $`1-e^{-2}+o(1)\ge4/5`$ fraction of all model primes up to X, all
   in one class mod 3, so
   $`\min(N_1(X),N_2(X))\le(0.14+o(1))\,\pi_{\mathrm{model}}(X)`$
   against the demanded $`(\tfrac12+o(1))\pi_{\mathrm{model}}(X)`$
   for both coprime classes j mod 3.
3. GPY correlations with their documented consequence (freiberg10
   Prop. 2.2 with Section 3): FAIL in the model, PROVED. The
   documented consequence of $`\mathcal{L}>0`$ is two primes in one
   interval of length $`H=\epsilon\log{N}`$; model gaps satisfy
   $`g_n=2\lceil\ln{}q_n/2\rceil\ge\ln{}q_n`$, so for fixed
   $`\epsilon<1`$ no such interval holds two model primes at large
   scale: the conclusion, hence the package it rests on, fails.
4. The sieve upper bound (hm88 Lemma 3): FAILS in the model, PROVED
   (the model is too concentrated for it, not too thin). Take z
   large, $`P=P(z)`$, $`R=P^{D-1}`$, and the increment-2m stretch
   covering at least half of $`(P^{D},2P^{D}]`$ ($`\ln2<2`$);
   $`2m\le z^{2}`$ eventually, and the model primes there are exactly
   the AP elements $`a_0+j\cdot2m`$ in range. P and $`2m`$ are both
   even, so $`d:=\gcd(P,2m)\ge2`$; pick $`s_1\equiv a_0\bmod d`$,
   $`s_2=s_1+2m`$ (spacing $`\le z^{2}`$). The r with
   $`rP+s_1\equiv a_0\bmod 2m`$ form an AP of density
   $`d/2m\ge1/m`$, each in-stretch one making BOTH $`rP+s_i`$ model
   primes: count $`\ge R/(2m)-O(1)`$ against the ceiling
   $`\ll_2 R/(V(z)\log{R})^{2}\asymp R(\log{z})^{2}/z^{2}`$ (Lemma 3
   at parameter 2R). Since $`m\asymp Dz/2`$ and
   $`z^{2}/(\log{z})^{2}\gg Dz`$, the g=2 instance is false at all
   large z.
5. The delta-thin-window input (hm88 Lemma 4): does NOT fail -- a
   prime-free statement about integers coprime to $`P(z)`$. RECORDED.
6. Landau-Page bookkeeping (freiberg10 Lemma 2.1) and the Mertens-AP
   / smooth-AP inputs (freiberg11 Lemmas 3.2/3.3): OPEN/untested --
   the former has no elementary model translate (an L-function
   statement), the latter two were not adjudicated here (their head
   consumer, Theorem 3.1, already fails by item 2).

Consequence, recorded in the V-NEG outcome: the schema's lower-bound
and equidistribution inputs -- and even its tuple-level upper bound
-- fail in the model, so a favourable word-grain resolution built on
this schema WOULD have met the separator requirement's
failure-in-model criterion. It did not resolve favourably: no
separator delivery is claimed, and nothing transfers the
classical-result priors to the word-grain application.

---

## 9. Rule-16(a) pass (clause-vs-body diff, run before hand-off)

Each S6 clause outcome diffed against the body's support classes:
(a) the not-SHAPE-POSITIVE-PROPORTION outcome, the PROVED fixed-k
existence and the EVIDENTIAL class for the proportion step are
Section 5.2's own determinations, carried with their qualifiers
(fixed rank, sparse scales, reference constants, no F^ms control);
the existence statement is recorded, not upgraded to any proportion.
(b) the hm88 value-axis shape carries proved-in-source, identical to
A-7(2); "STRUCTURAL" classifies the failure mode, not a support
class. (c) CORR-NOT-ESTABLISHED with Section 4's three absences at
absent-from-corpus; the fixed-k analogue's PROVED grade keeps its
qualifiers. (d) the CM-2/CM-3 no-gos carry the sheet's own grades.
The strongest-supported shapes keep the freiberg11 scope qualifier
and the fixed-rank/no-proportion qualifiers verbatim. No verdict
clause strengthens a body support class; no body scope qualifier is
dropped. Checked clause by clause before hand-off.

---

## 10. Both-readings appendix

- The verdict (V-NEG). *Supporting:* all four extracts read in
  full; every counting step enumerated in A-4/A-5 with display ids;
  the finite-algebra routes carried out and provably stopping at the
  named places; the pricing reproduces anchored columns exactly.
  *Contradicting:* the corpus is four papers (Shiu 2000 excluded by
  the ANN-92 operator decision); a positive-proportion word-grain
  form could exist outside it or by new proof work -- corpus grain,
  not an impossibility theorem.
- The structural claim. *Supporting the decision to test it:* the
  density inputs really are about the row family (Q-CORR item 1),
  and the Section 5.2 algebra shows the matrix DOES populate word
  classes, non-rigid ones included, at fixed rank. *Contradicting:*
  the family index fixes admissible offsets, not realized words; the
  contrary literature reading (V6 prior) is confirmed.
- F-CONS. *Supporting:* the pair mechanism is proved-in-source in
  two independent forms (interval rows; S/T imbalance), the
  fixed-rank matched-flank extension PROVED here. *Contradicting:*
  the nu-string extension is stated-without-proof-in-source; the
  D0-depth extension is absent entirely; Shiu's own counting sits
  behind the ANN-92 exclusion.
- F-MODEL. *Supporting:* the failures are elementary, each from the
  stretch structure or the minimum gap. *Contradicting:* items 5-6
  show the model does not fail everything -- one input holds, two
  families stay OPEN/untested; the finding names inputs, not the
  schema as a unit.
- The A6/scale axis. *Supporting the method:* scale density is the
  one axis the method clears natively (CM-6), freiberg11 in the
  all-large-x form. *Contradicting:* it moves no failing axis.

---

## 11. Residual uncertainty

- The Shiu exclusion stands: every Shiu-origin statement here is
  second-hand through the Freiberg extracts; a rule-26(5) re-opening
  is the operator's alone (r29M.5; no S6 clause was blocked on it).
- freiberg10 Section 7 (nu+1 strings) is
  stated-without-proof-in-source; nothing here rests on it.
- The freiberg11 Lemmas 3.2/3.3 proofs sit outside the declared
  extract scope (named reference "See 4"); Theorem 1.1's grade
  carries that qualifier wherever cited.
- The CM-5a exchange column prices arithmetic on an undocumented
  floor; the CM-5b grid values carry the reference constant
  $`C'_k=1`$ (Lemma 3's $`\ll_g`$ constant is undocumented), so only
  the divergence, not any grid sign, is PROVED.
- The two F-MODEL families left OPEN/untested could be adjudicated
  by further work; neither direction moves the S6 outcome.
- BET-20260725-12 binds and stays OPEN; resolution is operator
  judgment against this finding (no bet is scored here).

END OF WORD-GRAIN ADJUDICATION (item-0029, Session M)
