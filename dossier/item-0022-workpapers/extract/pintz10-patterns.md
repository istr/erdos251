# EXTRACTION: Janos Pintz, "Patterns of primes"

Source (only evidence base): /home/istr/pro/erdos251/dossier/1004.1072v1.pdf
sha256 74824028eb50c322f43da700fcb31fe10ce91272fe8e73695e9a4f82df22053b
(operator-verified; re-verified this session).
arXiv:1004.1072v1 [math.NT] [arXiv preprint] 7 Apr 2010. Author(s): Janos
Pintz, Renyi Mathematical Institute of the Hungarian Academy of Sciences,
Budapest. 9 pages. PDF metadata: Creator "LaTeX with hyperref package",
Producer "dvips + GPL Ghostscript GIT PRERELEASE 9.22", CreationDate
"Tue Nov 2 19:34:44 2021 CET" (a re-render/timestamp artifact of the
arXiv PDF pipeline; the arXiv submission date printed on the paper itself
is 7 Apr 2010). No journal reference is printed on the paper; it is an
arXiv preprint throughout.

Front-matter identification CONFIRMED against the dispatch: author
"Janos Pintz", title "Patterns of primes", arXiv:1004.1072v1. No
deviation.

---

## Transcription conventions

ASCII-folded per AGENTS.md (Janos, Erdos rendered without diacritics).
No transcription-unsure passages were encountered; the text layer of
this PDF is clean LaTeX output with no scrambled displays.

---

## 1. Front matter (verbatim)

"arXiv:1004.1072v1 [math.NT] 7 Apr 2010 / Patterns of primes / Janos
Pintz [footnote:] Supported by OTKA Grants K72731, K67676 and
ERC-AdG.228005."

## 2. Statements cited by item-0022's reports (verbatim, in reading order)

### 2.1 The Theorem actually invoked (report 1's "uniform Gallagher w.r.t. k" claim)

This is Lemma 2 and its r=1 remark, p.6-7:

"**Lemma 2.** For fixed nu, r and H > H0(nu, r) we have

$$S(\nu, r) = \sum_{D \subset [1,H]} S^2(D^+) \le c_8(\nu, r) H^\nu.$$

**Remark.** The condition H > H0(nu, r) and H > H0(nu) is naturally not
necessary if we do not care about the values of the constants c7(nu) and
c8(nu, r).

**Remark.** In case of r = 1 we will additionally show, similarly to
(2.9), S(nu, r) ~ H^nu as H -> infinity. This slightly modified form
implies easily the original Gallagher's theorem too, by dividing all
possible nu+1-tuples according to the smallest element of it and using
that S(H) is invariant under translation."

Proof close, p.8: "(2.14)-(2.16) together prove the lemma, while for r =
1, in order to obtain ~ instead of <<, it is enough to observe that the
numerator after the product sign equals exactly 1 for each prime p, and
the contribution of the incomplete period, the interval [RP+1, RP+r], is
<= P = O(H) by the prime number theorem, since y = log H / 2."

### 2.2 Lemma 1 (the fixed-tuple-size special case, r absent)

p.6: "**Lemma 1.** For fixed nu and any H > H0(nu) we have

$$\sum_{\substack{D \subset [1,H] \\ |D|=\nu}} S^2(D^+) \le c_7(\nu) H^\nu.$$

**Remark.** The above lemma is somewhat analogous to Gallagher's theorem
$$\sum_{D\subset[1,H], |D|=\nu} \mathfrak{S}(D) \sim H^\nu,$$
the difference being the non-essential appearance of D+ = D union {0} in
place of D and the more essential change in the exponent: two instead of
one."

### 2.3 What "r" denotes in Lemma 2's proof, and the exponent glyph in (2.10)

p.6-7, opening the proof of Lemma 2: "We will prove in fact a little bit
more. Namely, the fact that extending every concrete admissible D union
{0} of size t+1 >= 1 with just one element running over [1,H] the square
of the singular series will be larger at most by a factor depending on
t. In such a way, (2.10) follows by induction from

$$S^*(t,r,D) := \sum_{1\le h\le H,\, h\notin D} \left(\frac{\mathfrak{S}(D^+\cup\{h\})}{\mathfrak{S}(D^+)}\right)^r \ll H$$

where D+ is any admissible set of size t+1 and, as in the following, we
will not mark the dependence of the constants implied by << or O symbols
on t and r."

p.7 (continued, the local averaging computation, eq. (2.12)-(2.16)),
transcribed via `pdftotext -layout` on pages 7-8 of the anchor (the same
tool touch used throughout this repair pass, re-run to settle this
question independently of any operator-supplied material):

"$`\nu_p'=\nu_p(D^+\cup\{h\}), \nu_p=\nu_p(D^+), y=\frac{\log H}{2},
P=\prod_{p\le y}p, \Delta:=\prod_i(h-d_i).`$" (2.12); the ratio
$`\mathfrak{S}(D^+\cup\{h\})/\mathfrak{S}(D^+)`$ is split into
$`\prod_1\cdot\prod_2\cdot\prod_3`$ over $`p\le y`$, $`p>y,p\mid\Delta`$,
and $`p>y,p\nmid\Delta`$ respectively (2.13); $`\prod_3=1+O(1/y)`$ (2.14)
and $`\log\prod_2\ll1/\log y`$ (2.15); then, verbatim:

"If H = RP + r, 0 <= r < P then Π₁(h) is periodic with period P. ...
Consequently

(2.16)
$$\frac{1}{P}\sum_{h=1}^P \Pi_1(h) = \prod_{p\mid P}
\frac{\frac{\nu_p}{p}\left(1-\frac{\nu_p}{p}\right)^r +
\left(1-\frac{\nu_p}{p}\right)\left(1-\frac{\nu_p+1}{p}\right)^r}
{\left(1-\frac{\nu_p}{p}\right)^r\left(1-\frac1p\right)^r}
= \prod_{p\mid P}\frac{1-\frac{r(\nu_p+1)}{p}+O(p^{-2})}{1-\frac{r(\nu_p+1)}{p}+O(p^{-2})}
= \prod_{p\mid P}\left(1+O(p^{-2})\right) = O(1).$$"

The local-average identity (2.16) carries the exponent **r**, applied
directly to $`(1-\nu_p/p)`$ and $`(1-(\nu_p+1)/p)`$ at every prime
$`p\mid P`$ -- the identical genuine moment-order parameter as (2.11),
not the fixed value 2. This is independent of, and reinforces, (2.11)'s
own use of r: the two displays are the two halves of one continuous
computation (2.11 sets up the quantity to be bounded; 2.12-2.16 bound
it), and both are written for general r throughout.

**Revision (this line added after the item-0022 repair-r1 pass; see
FLAGS below for full provenance).** An earlier version of this Section
2.3 concluded from (2.11) alone that r was purely a proof-internal
ratio-exponent, unrelated to Lemma 2's own displayed moment order (fixed
at 2 per the literal glyph in (2.10)). That conclusion did not weigh
(2.16) or the r=1 remark quoted in Section 2.1 above. Read together,
(2.11), (2.12)-(2.16), and the r=1 remark are decisive: the induction
these equations carry out is a genuine general-r moment induction (see
the derivation below), and the r=1 remark -- "In case of r=1 we will
additionally show... S(nu,r)~H^nu... implies... Gallagher's theorem" --
is logically incoherent under a reading where Lemma 2's own exponent is
fixed at 2 regardless of r (there would be no meaningful "case r=1" to
speak of if the exponent never actually depended on r). See Section 6
for the resulting reconciliation of this with the literal glyph printed
in (2.10).

**The induction, worked through explicitly.** Multiplying (2.11)
through by $`\mathfrak{S}(D^+)^r`$: $`\sum_h
\mathfrak{S}(D^+\cup\{h\})^r \ll H\cdot\mathfrak{S}(D^+)^r`$. Define
$`M_{t,r}(H):=\sum_{D\subset[1,H],|D|=t}\mathfrak{S}(D^+)^r`$. Summing
the previous display over all admissible t-element D, and using that
every admissible (t+1)-element set is obtained exactly t+1 times (once
per choice of which element is the newly adjoined h):
$`(t+1)M_{t+1,r}(H)\ll H\cdot M_{t,r}(H)`$, so
$`M_{t+1,r}(H)\ll\frac{H}{t+1}M_{t,r}(H)`$. The base case is
$`M_{0,r}(H)=\mathfrak{S}(\{0\})^r=1`$. Iterating for
$`t=0,\ldots,\nu-1`$ gives $`M_{\nu,r}(H)\ll_{\nu,r}H^\nu`$, i.e.
$`\sum_{D\subset[1,H],|D|=\nu}\mathfrak{S}(D^+)^r\ll_{\nu,r}H^\nu`$ --
a genuine general-r moment bound, for every fixed r, not only r=2. This
derivation uses nothing beyond (2.11) and (2.16) as printed (both
independently re-verified via pdftotext this session) and standard
counting; it is not sourced from any operator-supplied material.

## 3. Method anatomy (paraphrase except quotes)

Section 1 states the main theorem: under a distribution-level hypothesis
$`\vartheta>1/2`$ on the primes, there is a bounded even $`d\le
C_1(\vartheta)`$ such that the set of primes p with $`p,p+d`$ both prime
contains arbitrarily long arithmetic progressions (building on
Green-Tao and Goldston-Pintz-Yildirim). Section 2 proves a quantitative
strengthening: for any $`\eta>0`$, $`\nu,m`$ natural numbers, there is a
set of $`\nu`$-tuples of admissible differences of size $`\gg
\log^\nu N`$, each realizing $`\gg N^2/\log^m N`$ length-$`m`$
arithmetic progressions of $`(\nu{+}1)`$-tuples of primes. The proof
reduces (via Selberg's sieve, Cauchy-Schwarz, and Lemma 1/Lemma 2's
bound on $`\sum \mathfrak{S}^2(D^+)`$) to bounding this sum of squared
singular series over $`\nu`$-subsets of $`[1,H]`$, which is exactly the
statement extracted in Sections 2.1-2.3 above.

## 4. Uniformity ledger

- Lemma 1's constant $`c_7(\nu)`$ depends only on $`\nu`$; requires
  $`H>H_0(\nu)`$.
- Lemma 2's constant $`c_8(\nu,r)`$ depends on both $`\nu`$ and the
  general moment order r; requires $`H>H_0(\nu,r)`$ (paper notes this
  threshold is an artifact of not tracking constants, not a mathematical
  necessity).
- The bound $`\sum_{D\subset[1,H],|D|=\nu}\mathfrak{S}(D^+)^r
  \ll_{\nu,r}H^\nu`$ holds for every fixed r (Section 2.3's induction);
  the r=1 case is upgraded from $`\ll`$ to $`\sim`$ (an asymptotic),
  per the proof-close text quoted in Section 2.1 ("for r=1... it is
  enough to observe that the numerator after the product sign equals
  exactly 1 for each prime p").
- No claim in this paper gives a bound uniform in $`\nu`$ (i.e., letting
  the tuple rank grow); $`\nu`$ is fixed throughout Sections 1-2.

## 5. NOT-FOUND probe

Checked and NOT present in this paper: any growing-$`\nu`$ or
growing-tuple-rank asymptotic; no statement of a "per-position" constant
of the form $`(1+o(1))^k`$; no claim uniform in r (the implied constants
$`c_8(\nu,r)`$, $`H_0(\nu,r)`$ depend on r throughout).

**Revised** (see Section 2.3 and Section 6): a general-r moment bound
$`\sum_D\mathfrak{S}(D^+)^r\ll_{\nu,r}H^\nu`$ IS established by this
paper's proof, for every fixed r -- this was wrongly recorded as
NOT-FOUND in an earlier version of this extract; see Section 6 for the
correction and its provenance.

## 6. COMMENTARY (assessment, not extraction)

**The printed display (2.10) versus the lemma the proof establishes.**
Equation (2.10) as literally displayed (Section 2.1 above, "$`S(\nu, r)
= \sum_{D \subset [1,H]} S^2(D^+) \le c_8(\nu, r) H^\nu`$") shows the
exponent 2 on $`\mathfrak{S}(D^+)`$ -- matching Lemma 1's exponent
verbatim -- and shows no "$`|D|=\nu`$" restriction under the summation
sign, unlike Lemma 1's display (2.8), which carries `|D|=nu` on its own
second summation line (Section 2.2 above). Both of these features of
the DISPLAY are independently re-verified this session via
`pdftotext -layout` (Section 0 provenance below), and were already noted
correctly in the original version of this extract for the exponent, but
the missing cardinality condition was not flagged until this revision.

Taken as an isolated, self-contained display, (2.10) is internally
inconsistent with the rest of the same lemma and proof: (a) the r=1
remark immediately following it ("In case of r=1 we will additionally
show... S(nu,r)~H^nu... implies... Gallagher's theorem") has no content
if the exponent never actually depends on r; (b) the proof (2.11) and
the local-average computation (2.16) both carry the exponent r
explicitly and repeatedly, and the induction they support (worked
through in Section 2.3 above) genuinely establishes a general-r bound,
not a bound fixed at r=2; (c) without the `|D|=nu` restriction, the sum
over ALL D subset [1,H] (of every size) would be dominated by the
largest-size terms and could not satisfy an $`H^\nu`$ bound for a fixed
$`\nu`$ -- the restriction is mathematically necessary for (2.10) to
hold as any kind of true statement, exactly as it is required (and
printed) in Lemma 1.

The most coherent reading of the anchor as a whole -- lemma name
$`S(\nu,r)`$, constant $`c_8(\nu,r)`$, threshold $`H_0(\nu,r)`$, the
r=1 remark, and the proof (2.11)-(2.16) -- is that Lemma 2 states, and
its proof establishes,

$$S(\nu,r) = \sum_{\substack{D\subset[1,H]\\|D|=\nu}} \mathfrak{S}(D^+)^r \le c_8(\nu,r) H^\nu$$

for every fixed $`\nu,r`$, of which Lemma 1 is exactly the case $`r=2`$
and the r=1 remark is exactly the case $`r=1`$ (recovering Gallagher's
theorem as an asymptotic). The printed (2.10) -- exponent 2, no
`|D|=nu` -- is best read as an apparent typesetting carry-over from
Lemma 1's own display, not as a separate, narrower mathematical
statement that the rest of the lemma and its proof then silently ignore.

**Report 1's claim, reassessed.** Report 1 paraphrases this material as
"fuer festes nu und festes r $`\sum \mathfrak{S}(D^+)^r \le
c(\nu,r)H^\nu`$, und insbesondere fuer r=2 also ein quadratischer
Mittelwert im festen-nu-Regime kontrolliert wird" ("in the fixed-nu
regime" -- consistent with the `|D|=nu` restriction, even though report
1 does not spell out the summation domain explicitly). This matches the
coherent reading above. See the corresponding checklist row (R1-015)
for the revised CONFIRMED verdict this supports, reversing this
extract's and that row's earlier CORRECTED disposition.

## FLAGS

- No sha256 mismatch, no TRANSCRIPTION-UNSURE passages.
- **Revision provenance (2026-07-26, after item-0022 repair-r1's
  original Task C pass).** The operator supplied two documents,
  `Pintz_Lemma2_Image_Analysis_Report.pdf` and
  `Pintz_Lemmas_1_and_2_Report.pdf` (both self-described AI-assisted
  analyses, dated 26 July 2026), arguing that the printed exponent in
  (2.10) is a typographical slip and that Lemma 2 is intended as a
  general-r bound. Per this project's standing rule that
  operator-commissioned or AI-generated reports are never themselves
  evidence for a verdict, neither document is cited as a source in this
  extract; both served only to prompt a fresh, independent re-reading
  of the primary anchor. That re-reading (fresh `pdftotext -layout` on
  pages 6-8, reproduced in Section 2.3 above) independently confirmed
  the exponent-r content of (2.16), which this extract had not
  previously transcribed, and the logical force of the r=1 remark
  against a fixed-exponent-2 reading, which this extract had not
  previously connected to the (2.10) question. The revision above rests
  on that independent re-reading of the anchor, not on the two
  documents' own conclusions.
- The originally recorded transcription of (2.10) itself (exponent "2",
  no visible `|D|=nu`) is UNCHANGED and re-confirmed accurate as a
  transcription of what the display literally prints; what changed is
  the COMMENTARY's assessment of what Lemma 2, read as a whole
  document, establishes and was intended to state.
