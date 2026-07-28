# item-0022 extract repair log -- the two 2d bounces, repaired to the re-grade's specs

Phase 2d-repair of the item-0033 disposition chain. Executed by the local
executor (Claude Opus 5, `claude-opus-5[1m]`) on 2026-07-28 against pin
`2229c55416bd950bc5c067366c3ca65900fd0eb6`, under an ephemeral dispatch
that was never committed; the operator apply is the ratifying commit.

**This is a repair pass, not a grade.** It hashes nothing, it edits no
header, it confers no standing, and it does not close item-0033. It
performs the four fixes the re-grade record `extract-grades-r2.md`
specifies in its Section 11, with the anchored PDFs open, and nothing
else. Standing on the two repaired extracts is the terminal re-grade's to
confer; see Section 6.

**Specification.** `extract-grades-r2.md` Section 11, in the tree at the
pin and unmodified since it. This log re-transcribes no repair text from
the dispatch: each fix was worked from the record's own spec with the
anchor open at the location the spec names.

**Fidelity authority.** Every region edited was confirmed against the
anchored PDF, at the page the spec names and at the pages the repaired
text now cites. No dropped extract, no ephemeral dispatch, and no
operator-held object was opened, at any point, for any purpose. The
untracked steering workpaper `pintz10-source-defects.md` was not consulted.

**Tooling.** `pdftotext -layout` for the text layer, `sha256sum` for
anchor and frozen-extract identity, and the re-grade's line-break-
flattening dropped-object scan. No side-effecting script was run;
`extract-inventory.py` was deliberately not invoked, per the standing
finding that it rewrites the inventory file in place.

---

## Section 0 -- preflight, all seven predicates

| predicate | result |
| --- | --- |
| P1 -- `git diff --stat 2229c55..HEAD` empty or `roadmap/` only | PASS (empty; HEAD equals the pin) |
| P2 -- last ledger annotation is `ANN-20260728-81` | PASS |
| P3 -- `item-0033` ratified at position 1 | PASS |
| P4 -- `extract-grades-r2.md` present and unmodified since the pin | PASS |
| P5 -- the three PDF sha256 match header and booked line | PASS, three for three |
| P6 -- the three CLEAN extracts still match their ANN-81 hash lines | PASS, three for three |
| P7 -- the two HANDOVER anchors each occur exactly once | PASS, 1 and 1 |

No rule-18 delta: HEAD equals the Section 0 pin and
`git diff --stat pin..HEAD` is empty. No commit, bookkeeping or
otherwise, landed past the pin.

P3 detail: `roadmap.py show item-0033` reports `status: ratified`, rank
0100; `roadmap.py order` places it at position 1 and `roadmap.py next`
names it. Rank and order diverge deliberately, per the standing
ANN-72/ANN-73 reading recorded in `HANDOVER.md`.

P4 detail: `git diff --stat pin -- extract-grades-r2.md` is empty and the
file is not listed by `git status --porcelain`.

P5 detail, the three anchors this pass opened:

| anchor | sha256 (prefix) | `payloads/HASHES.txt` line | why opened |
| --- | --- | --- | --- |
| `dossier/2301.06095v1.pdf` | `c67fdd9c` | 86 | kuperberg23's own anchor |
| `dossier/2210.09775v2.pdf` | `653dcd73` | 21 | the cross-referenced anchor named in kuperberg23's header |
| `dossier/1004.1072v1.pdf` | `74824028` | 82 | pintz10's own anchor |

Each value equals both the sha256 printed in the extract header and the
line booked in `payloads/HASHES.txt`, checked before any edit. Only
prefixes are reproduced here: this pass books no hash and nothing in it
is an anchoring record. `2210.09775v2` was verified for identity only;
no content of it was read, because no repair depends on it.

P6 detail, the frozen-CLEAN baseline, recomputed at start:

```
9125824e...  bloomkuperberg23-oddmoments.md   HASHES.txt:92
2177b805...  kowalski-singser-dist.md         HASHES.txt:93
50beadb8...  kuperberg21-oddmoments.md        HASHES.txt:94
```

Working-tree state at the pin, disclosed because `git status
--porcelain` is a close gate: the same three untracked steering
workpapers of 2026-07-26 sit under `dossier/item-0022-workpapers/`
(`pintz10-2-16-recheck.py`, `pintz10-2-16-recheck.txt`,
`pintz10-source-defects.md`), plus this pass's own ephemeral dispatch at
the repository root. This pass created none of them and touched none of
them.

---

## Section 1 -- Lane A: the four repairs

Four edits, all prose or citation. No display, numbered object,
transcription or NOT-FOUND probe that the re-grade exhibited as verified
was changed.

### 1.1 `kuperberg23-apsmooth.md` -- the display (9) description

Section 2.1, the Theorem 1.2 sentence, lines 55-58 at the pin.

Before:

```
p.4, Theorem 1.2 (the corresponding asymptotic for $`R_k(h;r,c_1,\ldots,c_k)`$)
sums over partitions of $`[1,k]`$ into doubleton and singleton blocks,
with the doubleton part again organized by perfect matchings $`\sigma \in
\mathcal{B}(j+1,\ldots,k-j)`$ of the remaining indices (eq. (9)).
```

After:

```
p.4, Theorem 1.2 (the corresponding asymptotic for $`R_k(h;r,c_1,\ldots,c_k)`$)
sums, for each $`0\le j\le k/2`$, over the partitions
$`P=\lbrace S_1,\ldots,S_{k-j}\rbrace`$ of $`[1,k]`$ that refine the
congruence-class sets $`C_\ell`$ of p.3 and consist of $`j`$ doubleton
blocks $`S_1,\ldots,S_j`$ and $`k-2j`$ singleton blocks
$`S_{j+1},\ldots,S_{k-j}`$. The perfect matchings
$`\sigma\in\mathcal{B}(j+1,\ldots,k-j)`$ appearing in eq. (9) pair the
singleton blocks $`S_{j+1},\ldots,S_{k-j}`$; the $`j`$ doubleton blocks
are carried by the separate factor
$`\left(\frac{h}{r}\sum_{d\mid Q,\,d>1}\frac{\mu(d)^2}{\phi(d)}\right)^j`$
of the same summand (eq. (9)).
```

**Checked against `2301.06095v1.pdf`, three locations.**

- **p.4, display (9) and its summation conditions.** The conditions read
  `0 <= j <= k/2`; `P` refines `{C_l}_{l in [1,k]}`,
  `P = {S_1, ..., S_{k-j}}`, `|S_m| = 2` for all `1 <= m <= j`,
  `|S_m| = 1` for all `j < m <= k-j`. The summand carries the factor
  `( (h/r) sum_{d|Q, d>1} mu(d)^2/phi(d) )^j` and then
  `sum_{sigma in B(j+1,...,k-j)} prod_{(i1,i2) in sigma} V_2(Q,h;r,c(S_{i1}),c(S_{i2}))`.
  So the partition carries `j` doubleton blocks indexed 1..j and `k-2j`
  singleton blocks indexed `j+1..k-j`, and the matching ranges over the
  index set `{j+1,...,k-j}` -- the singleton blocks. The doubleton blocks
  are carried by the separate `j`-th power factor.
- **p.6, the closing clause of the smooth-weight analogue (16).** "where
  the sum is taken over partitions of [1, k] where each part has either 1
  or 2 elements, and for |Sm| = 1, fSm denotes fj where j in Sm." The
  paired argument is defined only for singleton blocks, which confirms
  the reading independently.
- **p.3, the two notations the repaired sentence now names.**
  `C_l := {i : c_i = l mod r}` is defined at the foot of p.3 and the
  refinement relation `P refines {C_l}` at the head of p.4; and
  "for a set of integers `{a_1,...,a_k}`, we will denote by
  `B(a_1,...,a_k)` the set of matchings of `{a_1,...,a_k}` into pairs",
  also p.3, which is what makes `B(j+1,...,k-j)` a matching of the
  singleton-block indices.

**Two changes inside this one sentence, both disclosed.** The spec's fix
is the singleton/doubleton correction. The rewrite additionally names the
refinement condition `P refines {C_l}`, which the original sentence
omitted. That omission was not a false statement and the re-grade did not
list it; it is folded in because the sentence was being rewritten anyway
and because a description of (9) that drops the refinement is incomplete
about the summation range. Both changes are within the repaired span and
are the same class. Nothing else in this extract moved.

### 1.2 `pintz10-patterns.md`, fix 1 -- the misidentified main theorem

Section 3 (Method anatomy), first sentence, lines 176-184 at the pin.

Before:

```
Section 1 states the main theorem: under a distribution-level hypothesis
$`\vartheta>1/2`$ on the primes, there is a bounded even $`d\le
C_1(\vartheta)`$ such that the set of primes p with $`p,p+d`$ both prime
contains arbitrarily long arithmetic progressions (building on
Green-Tao and Goldston-Pintz-Yildirim). Section 2 proves a quantitative
strengthening: for any $`\eta>0`$, ...
```

After (the whole first paragraph is replaced; the second half's content
is retained and re-pointed):

```
Section 1 surveys the results this note builds on -- Green-Tao and the
conditional Goldston-Pintz-Yildirim bounded-gap theorem [GPY2] (both
p.1), the author's own cited preprint "Theorem [Pin]" (p.2), and
"Theorem [GPY3]" (p.3). "Theorem [Pin]" -- under a distribution-level
hypothesis $`\vartheta>1/2`$ on the primes, there is a bounded even
$`d\le C_1(\vartheta)`$ such that the set of primes p with $`p,p+d`$
both prime contains arbitrarily long arithmetic progressions -- is a
cited prior preprint of the same author, listed at p.9 as "[Pin] J.
Pintz, Are there arbitrarily long arithmetic progressions in the
sequence of twin primes? preprint, arxiv math.NT", and is NOT this
note's own theorem.

This note's own result is the unconditional Theorem stated at p.4 and
proved in Section 2 (heading "2 Proof of the Theorem", p.5): for any
$`\eta>0`$, $`\nu,m`$ natural numbers, there is a set of
$`\nu`$-tuples of admissible differences of size $`\gg \log^\nu N`$
(1.17), each realizing $`\gg N^2/\log^m N`$ length-$`m`$ arithmetic
progressions of $`(\nu{+}1)`$-tuples of primes (the Corollary, p.4).
The proof reduces ...
```

**Checked against `1004.1072v1.pdf`, five locations.**

- **p.1.** "Theorem (Green-Tao). The primes contain arbitrarily long
  arithmetic progressions." and "Theorem ([GPY2]). If the primes have a
  distribution level theta > 1/2 ... then there exists a positive even
  d <= C_1(theta) and infinitely many pairs of primes (1.3) p, p + d in
  P." Both on p.1, as the repaired text now says.
- **p.2.** "The author showed recently that a combination of the two
  above results is possible ... Theorem [Pin]. If the primes have a
  distribution level theta > 1/2 then there exists a positive even
  d <= C_1(theta) such that the set P(d) of primes p satisfying (1.3)
  contains arbitrarily long arithmetic progressions." This is the
  statement the extract had presented as the note's own main theorem. It
  is cited, and it is conditional.
- **p.3.** "Theorem [GPY3]. Unconditionally we have Delta*_1 = 0; further
  the Elliott-Halberstam conjecture [EH] implies Delta*_2 = 0."
- **p.4.** "The aim of this note is to show that the method of the
  mentioned work [GPY3] can be modified to yield ... The exact
  formulation of our result to be proved is as follows. Theorem. Let eta
  > 0 be any positive constant, nu and m natural numbers. Then we have a
  positive constant c(eta, nu) ... such that for any N > N_0(eta, nu, m)
  we have a set D_{N nu} of nu-tuples ... (1.17) |D_{N nu}| >= c(eta,
  nu) log^nu N and every element of D_{N nu} satisfies (1.15) and
  (1.16)." Immediately below it: "Corollary Under the above conditions,
  if (d_i)_{i=1}^nu in D_{N nu} then the set P(d_1,...,d_nu) of primes
  contains at least c'(eta, nu, m) N^2/log^m N arithmetic progressions of
  length m." **This Theorem carries no distribution-level hypothesis: it
  is unconditional.**
- **p.5.** The section heading "2 Proof of the Theorem".
- **p.9, References.** "[Pin] J. Pintz, Are there arbitrarily long
  arithmetic progressions in the se- quence of twin primes? preprint,
  arxiv math.NT". The repaired text quotes it with the line-break
  hyphenation joined ("sequence"), the same de-hyphenation the extract
  already applies elsewhere ("ac-cording" to "according", Section 2.1).

**The "quantitative strengthening" framing is dropped, not carried
over.** The p.4 Theorem is not a strengthening of [Pin]'s statement: it
is a different, unconditional statement about the density of realizable
difference tuples. The repaired text says only what the anchor supports
-- that Section 2 proves the p.4 Theorem -- and preserves the second
half's content, which the re-grade checked separately and passed.

**One new verbatim quotation is added** (the p.9 References entry). It is
new transcription surface and the terminal re-grade should check it as
such; it is exhibited above against the anchor.

### 1.3 `pintz10-patterns.md`, fix 2 -- the unmarked elision

Section 2.2, between Lemma 1's display and the "somewhat analogous"
Remark.

The spec allows either an ellipsis or a quotation of the intervening
Remark. **This pass quotes it**, because the Remark is a scope statement
about Lemma 1's own hypothesis -- it says H need not be the H of (2.2) --
and quoting preserves that scope where an ellipsis would only signal its
absence. Section 2.1 of the same extract already quotes the analogous
pair of Remarks under Lemma 2, so this makes the two sections uniform.

Inserted, verbatim:

```
**Remark.** The parameter H can be arbitrary here, not just that given in
(2.2).
```

**Checked against `1004.1072v1.pdf` p.6.** The source order is: "Lemma 1.
For fixed nu and any H > H_0(nu) we have (2.8) ...", then "Remark. The
parameter H can be arbitrary here, not just that given in (2.2).", then
"Remark. The above lemma is somewhat analogous to Gallagher's theorem
(2.9) ...". The extract now presents all three in that order, with no
elision left to mark.

**This is also new transcription surface** -- one sentence -- and is
exhibited above.

### 1.4 `pintz10-patterns.md`, fix 3 -- the over-broad page citation

Section 2.1, lead-in line 41 at the pin.

```
-This is Lemma 2 and its r=1 remark, p.6-7:
+This is Lemma 2 and its r=1 remark, p.6:
```

**Checked against `1004.1072v1.pdf` p.6.** Lemma 2, its display (2.10),
the "The condition H > H_0(nu, r) ..." Remark and the "In case of r = 1
..." Remark are all on p.6; p.6 continues into "Proof of Lemma 2" and
breaks mid-sentence into p.7. The quoted block is entirely on p.6. The
section heading, which already reads "(p.6)", is unchanged.

**The `p.6-7` at Section 2.3 line 86 is correct and was not touched:**
that passage -- the opening of the proof of Lemma 2 and (2.11) -- does
straddle the page break, confirmed on the same read.

---

## Section 2 -- mechanical scope

| measure | `kuperberg23-apsmooth.md` | `pintz10-patterns.md` |
| --- | --- | --- |
| line count, before | 89 | 279 |
| line count, after | 96 | 291 |
| `$$` display fences, before | 2 (1 display block) | 12 (6 display blocks) |
| `$$` display fences, after | 2 (1 display block) | 12 (6 display blocks) |
| displays changed | 0 | 0 |
| numbered objects changed | 0 | 0 |
| transcriptions altered | 0 | 0 (2 short quotations added) |
| NOT-FOUND probes changed | 0 | 0 |
| header lines changed | 0 | 0 |
| edits | 1 | 3 |

`git diff --stat` for the whole apply's extract edits: two files changed,
36 insertions, 17 deletions. Every display fence in both files is
byte-identical in position and content to the pin; the fence counts above
are the mechanical confirmation the dispatch asks for.

**Dropped-object scan at close**, the re-grade's robust form with line
breaks flattened, over both repaired extracts:

```
== dossier/item-0022-workpapers/extract/kuperberg23-apsmooth.md
  (none)
== dossier/item-0022-workpapers/extract/pintz10-patterns.md
  (none)
```

The repair introduced no reference to a dropped object.

**Frozen-CLEAN gate at close.** The three CLEAN extracts were re-hashed
after the writes; all three still equal their ANN-81 lines
(`payloads/HASHES.txt` lines 92-94). They are byte-unchanged.

---

## Section 3 -- the header question: left, and why

The re-grade flagged (its Section 10(a) and O1) that all five survivor
headers carry "fidelity repair applied per the ANN-78 grade
(`extract-grades-r1.md`) at this pin; re-grade pending", that the "at
this pin" deixis is unresolvable, and that "re-grade pending" went stale
on the three CLEAN extracts when ANN-81 landed.

**No header was edited by this pass, on the dispatch's instruction, and
the disposition is leave-and-document.** The reasons, recorded so a later
pass does not re-open them:

- The re-grade itself adjudicated "at this pin" as tolerable and
  non-blocking, and three prior passes accepted it.
- The stale "re-grade pending" cannot be fixed on the three CLEAN
  extracts without editing hashed files, which would either break the
  append-only rule or add a second `payloads/HASHES.txt` line for a path
  that has appeared once -- an invariant that file has held over its
  whole history. A cosmetic process-note is not worth either.
- Grade-state does not belong in an extract header. It belongs in the
  ledger and the grade record, which carry it authoritatively. The
  header's job is provenance -- source path and sha256 -- which is stable
  and correct on all five.

So all five headers stay uniform and as-is, and the clause is superseded
by the ledger grades rather than edited. The header-design lesson -- an
extract's provenance header carries source and hash only, never
grade-state and never an unresolvable deixis -- is routed to item-0034
and needs no edit to these five to apply going forward.

---

## Section 4 -- STOP-AND-REPORT, all seven reported

| stop | fired | detail |
| --- | --- | --- |
| S1 | NO | HEAD equals the pin; `git diff --stat pin..HEAD` empty; no rule-18 delta; no commit past the pin. |
| S2 | NO | Both Appendix B anchors matched exactly once. |
| S3 | NO | Last annotation `ANN-20260728-81`; item-0033 ratified at position 1; `extract-grades-r2.md` unmodified since the pin; all three CLEAN hashes matched at start. |
| S4 | NO | Every cited PDF location exists and is legible. No repair was abandoned for want of a readable location, and no fix changed a display or numbered object the re-grade passed. |
| S5 | NO | Every gate reproduces its start-of-pass output except the ones whose movement is the deliverable; the frozen-CLEAN gate and the bounced-span scan both pass. See Section 5. |
| S6 | NO | No hash line added. No header edited. No CLEAN extract touched. No write to the grade record, the inventory, the checklist, `roadmap/`, `lean/`, `runs/`, `writeup/` or `payloads/HASHES.txt`. All three PDF sha256 matched. |
| S7 | **NO defect found; two in-span disclosures** | With both anchors open no fidelity defect beyond the Section 3 spec was found on either bounced extract, and none on the three CLEAN extracts, which were not opened for grading and are frozen. Two things are disclosed rather than hidden: the refinement condition folded into the kuperberg23 sentence (Section 1.1), which is an in-span completeness item of the same class, not a separate defect; and the two short verbatim quotations added to pintz10 (Sections 1.2 and 1.3), which are new transcription surface for the terminal re-grade and are exhibited against the anchor here. |

S7 is reported as not firing in its own terms. It is defined over
fidelity defects found beyond the spec, and this pass, reading
`2301.06095v1` at pp.3-4 and p.6 and `1004.1072v1` at pp.1-9, found
none. The three CLEAN extracts were not read for defects at all: they
are frozen and any finding on them would be logged, never repaired.

---

## Section 5 -- gates

Run at start and at close, verbatim from the dispatch's Section 4.

| gate | start | close |
| --- | --- | --- |
| `blocks.py check-frozen` | all byte-identical (3 blocks) | all byte-identical (3 blocks) |
| `blocks.py relocation-check` | PASSED | PASSED |
| `grep -rnE '^\s*sorry\s*$' lean/Erdos251/` | 1 (`Statement.lean:21`, baseline) | 1 (`Statement.lean:21`, baseline) |
| `grep -c a6276f4c... lean/lake-manifest.json` | 1 | 1 |
| `tail -c 1 lean/lean-toolchain \| od -c` | `\n` | `\n` |
| `roadmap.py show item-0033` | ratified, rank 0100 | ratified, rank 0100 |
| `writeup_mapper.py check` | PASS | PASS |
| `mathjax_lint.py` | 139 files, 0 problems | 140 files, 0 problems -- **file count moves by this log** |
| ASCII, all five extracts under `extract/` | 0 0 0 0 0 | 0 0 0 0 0 |
| ASCII, `HANDOVER.md` | 0 | 0 |
| ASCII, this repair log | n/a | 0 |
| `git status --porcelain` | 4 untracked, no tracked change | the writes of this apply, plus the same 4 untracked |

One gate's file count moves and the movement is this log's own creation,
not a regression; zero problems at both ends is the property the gate
asserts. All five extracts are ASCII-only at close, the two edited and
the three untouched.

**Frozen-CLEAN gate**: PASS, three for three (Section 2).
**Bounced-span scan**: `(none)` on both repaired extracts (Section 2).

No side-effecting command appears in the gate list.
`extract-inventory.py` was not run and `extract-inventory-r1.md` stays
stale by construction, as a timestamped record of the seven-extract
state.

---

## Section 6 -- the terminal re-grade this pass hands off to

The two extracts are **repaired**. They are **not graded**, and nothing
here confers standing. Neither appears in `payloads/HASHES.txt`.

The terminal re-grade is the following, separate apply:

- a **fresh executor session**, not this one -- an executor must not
  grade its own repair;
- **scoped as the re-grade record authorizes**: the repaired spans, plus
  a fresh robust dropped-object scan and a fresh in-tree path-liveness
  check on both extracts. `extract-grades-r2.md` Sections 8 and 9
  exhibit everything else in both files as verified, so the terminal
  re-grade confirms the repairs against the PDFs and re-runs the two
  axes; it does **not** re-grade the three CLEAN extracts, whose grades
  stand at ANN-81;
- it should check, specifically, the four repaired regions listed in
  Section 1 above and the three new spans disclosed there: the
  refinement clause in kuperberg23, and the two short quotations added
  to pintz10 (the p.6 Remark and the p.9 References entry);
- on CLEAN it hashes the two repaired extracts -- neither is in
  `payloads/HASHES.txt`, so these are new lines, not duplicates -- and
  hashes the terminal record, which is then the terminal determination.

**item-0033's acceptance is met when five extracts are CLEAN and hashed
-- three at ANN-81, two at the terminal entry -- and the two precedents
are dropped.** The close is the operator's separate roadmap apply, and
the close summary records the header disposition of Section 3 above. If
either repaired extract bounces again, item-0033 stays open and the
cycle repeats on that one.
