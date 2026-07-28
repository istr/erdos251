# item-0022 extract repair log -- Phase 2c-residual: the precedent drop and the S7 severance residuals

Phase 2c-residual of the item-0033 disposition chain. Executed by the
local executor under an ephemeral dispatch pinned to `3bdf48b`, never
committed; the operator apply is the ratifying commit.

**This is a repair-and-disposition pass, not a grade.** It hashes
nothing, it confers no standing, and it does not close item-0033. It
does two things: it removes the two precedent extracts from the
consumption surface on operator instruction, and it closes the
severance residuals that Phase 2c's S7 found and deliberately left
open. The grade that confers corpus standing is the re-grade, a
separate apply by a fresh session; see Section 8.

**Specification.** The Phase 2c-residual dispatch at pin `3bdf48b`,
which acts on two things Phase 2c landed: the operator's decision to
drop the two precedent extracts, and 2c's S7 finding that the
inventory's counts are a lower bound on severance rather than proof of
it.

**Fidelity authority.** The one region this pass edited was confirmed
with the anchored PDF open, before and after. No dropped report, no
kickoff dispatch, and no operator-held PDF was opened, at any point,
for any purpose.

**Tooling.** `pdftotext -layout` and `pdftotext` (raw) for the text
layer, `sha256sum` for anchor identity, `git rm` for the two deletions,
and the dispatch's Section 3 scan (which flattens line breaks before
matching) for severance evidence. No side-effecting script was run:
`extract-inventory.py` was deliberately not invoked, per 2c's Section
10.3 finding that it rewrites the inventory file in place.

---

## Section 0 -- preflight, all six predicates

| predicate | result |
| --- | --- |
| P1 -- `git diff --stat 3bdf48b..HEAD` empty or `roadmap/` only | PASS (empty; HEAD equals the pin) |
| P2 -- last ledger annotation is `ANN-20260728-79` | PASS |
| P3 -- `item-0033` ratified at position 1 of the global order | PASS |
| P4 -- both precedent extract files present at the pin | PASS, both present |
| P5 -- PDF sha256 for the repaired survivor equals header and booked line | PASS |
| P6 -- the two HANDOVER anchors each occur exactly once | PASS, 1 and 1 |

No rule-18 delta: HEAD equals the Section 0 pin
`3bdf48b0d3b32ae38008564efa2d4f35df8245f1`, and
`git diff --stat pin..HEAD` is empty.

P3 detail: `roadmap.py show item-0033` reports `status: ratified`,
rank 0100; `roadmap.py order` places it at position 1 and
`roadmap.py next` names it. Rank and order diverge deliberately, per
the standing ANN-72/ANN-73 reading recorded in `HANDOVER.md`.

P5 detail: this pass repaired exactly one survivor,
`kuperberg23-apsmooth.md`.

| extract | anchor | sha256 (prefix) | HASHES.txt line |
| --- | --- | --- | --- |
| kuperberg23-apsmooth.md | 2301.06095v1.pdf | c67fdd9c | 86 |

The file's sha256 equals both the value printed in the extract header
and the line booked in `payloads/HASHES.txt`, checked before any edit.
Only the prefix is reproduced here, per the convention of
`repair-log-2c.md`: this pass books no hash and nothing in it is an
anchoring record.

Working-tree state at the pin, disclosed because `git status
--porcelain` is a close gate: three untracked files predating this
apply sit under `dossier/item-0022-workpapers/`
(`pintz10-2-16-recheck.py`, `pintz10-2-16-recheck.txt`,
`pintz10-source-defects.md`, all dated 2026-07-26), plus the ephemeral
dispatch at the repository root. This pass created none of them,
touched none of them, and no surviving extract references any of them.

---

## Section 1 -- Lane A: the precedent drop

Both precedent extracts were deleted from
`dossier/item-0022-workpapers/extract/` on operator instruction:

- `precedent-p1-2605.22763.md` (118 lines at the pin)
- `precedent-p3-2601.07421.md` (71 lines at the pin)

The grounds, as the dispatch states them: they carry none of the
project's mathematics, their role was the experiment's own
meta-narrative, and precedent-p1 was the most entangled of the seven
with dropped objects -- it is the extract carrying S7-3, the second
uncounted `Appendix C.1` reference, on top of the class-(c) self-label
2c already deleted.

**The deletion changes the consumption surface, not the record.**
`extract/` is the directory both lanes consume from, so a dropped
object no longer sits where a later reader would pick it up. What
preserves that the two existed: git history, and the item-0022 records
that reference them by name -- the ANN-78 grade file, `repair-log-2c.md`,
`extract-inventory-r1.md` and the withdrawn checklist. None of those is
edited to erase the mention; they are timestamped records.

**Their two PDF anchor lines in `payloads/HASHES.txt` stay as
history.** Lines 87 (`2605.22763v2`) and 88 (`2601.07421v5`) are
untouched, append-only, and now name sources whose extracts were
dropped. `payloads/HASHES.txt` is byte-unchanged by this apply.

`extract/` file count: **7 -> 5**.

This also answers, in the affirmative-to-drop direction, the residual
question ANN-76 moved to item-0033 ("whether the two precedent
extracts stay in the corpus at all"). That question is carried as a
line in the HANDOVER open-operator-decisions block; **this pass did not
edit that line**, because Appendix B of the dispatch enumerates the
HANDOVER deltas exhaustively ("Required content, in this order, and
nothing else") and the budget allows no further HANDOVER edit. The new
B2 bullet records the drop; reconciling the open-decisions block is
bookkeeping left to the operator or to a later pass.

---

## Section 2 -- Lane B: the robust severance scan and the one residual repair

### 2.1 Why the scan was re-run rather than the inventory trusted

2c's S7-2 and S7-3 showed the inventory's single-line regex missing two
references: one split across a line break (`report` / `1's` in
kuperberg23) and one that was a second occurrence on a line already
counted (the Appendix C.1 reference in precedent-p1). Both survived all
three inventory axes, so an extract reporting 0/0/0 could still carry a
reference to a dropped object. **The zero was a lower bound on
severance, not proof of it.** The dispatch's scan flattens line breaks
before matching, so neither failure mode recurs.

### 2.2 The scan, before repair

Run from the repo root over all five survivors, exactly as the dispatch
prints it:

```
tr '\n' ' ' < "$f" | grep -oiE "report [123]|appendix c\.[0-9]|kickoff|operator-held|operator-verified|re-verified this session|against the dispatch"
```

| extract | hits before repair |
| --- | --- |
| bloomkuperberg23-oddmoments.md | (none) |
| kowalski-singser-dist.md | (none) |
| kuperberg21-oddmoments.md | (none) |
| kuperberg23-apsmooth.md | `report 1` |
| pintz10-patterns.md | (none) |

One hit, exactly the one the dispatch anticipated. The scan surfaced no
reference the dispatch did not name. In particular the header residues
the pattern also catches -- `operator-verified`, `re-verified this
session`, `against the dispatch` -- return nothing on any survivor,
which confirms 2c's Section 3.1 universal header repair took on all
five.

### 2.3 The repair

`kuperberg23-apsmooth.md`, Section 4 (NOT-FOUND probe), lines 80-81 at
the pin. The sentence read, across the break:

```
... on a parity-blocked flank class (report
1's "Input (i)"). This paper's results -- ...
```

The parenthetical attributes the probed concept to a dropped report.
Removed. The sentence now reads:

```
... on a parity-blocked flank class.
This paper's results -- ...
```

**What the probe states is unchanged.** It records that this paper
carries no Hardy-Littlewood-type lower bound for a prime-counting
function on a parity-blocked flank class; that negative stands on the
anchor alone and needed no addressee. Only the attribution to the
dropped object is gone.

Mechanical scope check, run as a word-level comparison of the file
against the pin with all line breaks flattened:

```
< class
< (report
< 1's
< "Input
< (i)").
---
> class.
```

That is the whole content delta of the file. Nothing else moved.

| check | result |
| --- | --- |
| line count | 89 -> 89 |
| `$$` display fences | identical, position and content |
| displays or numbered objects marked PASS by ANN-78 that changed | 0 |
| lines changed in the diff | 2 |

The two changed lines are the sentence carrying the residual and the
line the sentence's period moved onto. The paragraph below it was
deliberately **not** re-wrapped: the dispatch scopes a residual repair
to the reference and its immediate sentence, and leaving the following
lines byte-identical keeps the diff trivially auditable. The cost is
one short line mid-paragraph, which is cosmetic and is disclosed here
rather than absorbed by a reflow that would have touched four more
lines of prose the dispatch says not to touch.

### 2.4 The scan, after repair

| extract | hits at close |
| --- | --- |
| bloomkuperberg23-oddmoments.md | (none) |
| kowalski-singser-dist.md | (none) |
| kuperberg21-oddmoments.md | (none) |
| kuperberg23-apsmooth.md | (none) |
| pintz10-patterns.md | (none) |

Clean on all five. S4 does not fire.

---

## Section 3 -- PDF confirmation of the touched region

The dispatch requires the anchor open for any region edited, and
specifically requires the surrounding theorem-list transcription to be
confirmed faithful before and after, since ANN-78 passed it.

Read from `2301.06095v1.pdf` (19 pages, sha256 `c67fdd9c...`), pages 3
to 5 in the `-layout` text layer, plus a whole-document count:

| the extract's claim | what the anchor prints |
| --- | --- |
| Theorem 1.1 at p.3 | Theorem 1.1 stated on p.3, closing the section that defines `B_k` at (8) |
| Theorem 1.2 at p.4 | Theorem 1.2 stated on p.4, with its "In particular" clause and a separate `Remark.` paragraph below it |
| Theorem 1.3 at p.5 | Theorem 1.3 stated on p.5 |
| Theorem 1.5 at p.5 | Theorem 1.5 stated on p.5 |
| "the paper states no Theorem 1.4" | zero occurrences of the string "Theorem 1.4" in the whole PDF |

All five confirmed. The transcription is faithful before the edit and
after it; the edit did not reach it.

The probe's substantive negative was also re-checked against the same
pages, since the removed parenthetical sat inside it: Theorems 1.1,
1.2, 1.3 and 1.5, and the Lemma 1.4 between them, are asymptotic
formulas or estimates for sums of the singular series and its
restricted and smooth-weighted variants -- `V_k`, `R_k`, `V_2` -- and
none is a lower bound for a prime-tuple counting function. The probe
states this correctly.

**One observation for the re-grade, not a defect.** The numbering slot
1.4 in this paper is occupied by **Lemma 1.4** (p.5), which states the
`V_2` evaluation for the smooth-weight setting. The extract's sentence
"the paper states no Theorem 1.4" is literally true and was verified as
such by ANN-78's check A15 and again here. It is recorded only so that
a re-grader who greps for `1.4` and finds a hit does not read it as a
contradiction.

---

## Section 4 -- what a wider read-only sweep found

Beyond the dispatch's pattern, the five survivors were swept read-only
for a broader set of dropped-object, ephemeral and in-tree referents
(`dispatch`, `kickoff`, `report N`, `the report`, `checklist`,
`R1-NNN`, `STOP N`, `appendix X.N`, `operator-held`, `verdict
register`, `this session`). This is diligence, not mandate; it found
exactly one thing the Section 3 scan does not match.

**`kowalski-singser-dist.md`, FLAGS, second bullet.** The disclosure
that an earlier draft wrongly asserted the PDF contained two
concatenated documents ends "... made while tracking page ranges across
a large multi-document tool result in **this session**, not a property
of the file." The deictic points at the original extraction session,
which is an ephemeral referent no later reader can resolve.

**Not repaired here, and reported instead.** It is not a Section 3 hit,
and it is not a dropped-object residual: it attributes nothing to a
dropped report, kickoff dispatch or operator-held object, and the
disclosure it carries -- what the error was and how it was corrected --
remains fully checkable, since the correction is stated in the same
bullet and rests on PDF pages 1, 20 and 21. It is distinct in kind from
2c's Section 6.3 removals, which took out *falsified verification
assurances*; this assurance is not falsified. The re-grade should
decide whether the deictic is re-pointed to a pin or left as a
timestamped record. Repairing it here would have been a grading
decision, which this pass is not entitled to make.

Two further observations, both negative and both useful to the
re-grade's path-liveness axis:

- `pintz10-patterns.md` references "the item-0022 repair-r1 pass" and
  "item-0022 repair-r1's original Task C pass". Both resolve in-tree
  (`repair-log-r1.md`, `item-0022-repair-r1-report.md`), so they are
  live cross-references, not residuals.
- `kowalski-singser-dist.md` points at `kowalski-mu-recheck.py` /
  `.txt`; both exist and are tracked. No survivor points at any of the
  three untracked `pintz10-*` workpapers noted in Section 0.

---

## Section 5 -- STOP-AND-REPORT, all seven reported

| stop | fired | detail |
| --- | --- | --- |
| S1 | NO | HEAD equals the pin; `git diff --stat pin..HEAD` empty; no rule-18 delta. |
| S2 | NO | Both Appendix B anchors matched exactly once. |
| S3 | NO | Last annotation `ANN-20260728-79`; item-0033 ratified at position 1; both precedent extract files present at the pin. |
| S4 | NO | The Section 3 scan returns `(none)` on all five survivors at close. The one repair changed no display and no numbered object; it required no dropped, ephemeral or operator-held object to decide. |
| S5 | NO | Every gate reproduces its start-of-pass output except the two whose movement is the deliverable. See Section 6. |
| S6 | NO | No hash line added. No write to `roadmap/`, `lean/`, `runs/`, `writeup/`, the checklist, the grade file, the inventory file, `payloads/HASHES.txt`, or either precedent PDF anchor line. |
| S7 | **NO fidelity defect; one observation and one referred item** | With the anchor open, no fidelity defect ANN-78 failed to record was found in the region examined. Two things are logged for the re-grade and neither is a defect: the Lemma 1.4 numbering observation (Section 3) and the kowalski "this session" deictic (Section 4). |

S7 is reported as not firing in its own terms -- it is defined over
fidelity defects found with a survivor's PDF open, and this pass opened
one PDF over one region and found none. The two logged items are
recorded prominently anyway, because the re-grade is the pass entitled
to decide them.

---

## Section 6 -- gates

Run at start and at close, verbatim from the dispatch's Section 4.

| gate | start | close |
| --- | --- | --- |
| `blocks.py check-frozen` | all byte-identical | all byte-identical |
| `blocks.py relocation-check` | PASSED | PASSED |
| `grep -rnE '^\s*sorry\s*$' lean/Erdos251/` | 1 (`Statement.lean:21`) | 1 (`Statement.lean:21`) |
| `grep -c a6276f4c... lean/lake-manifest.json` | 1 | 1 |
| `tail -c 1 lean/lean-toolchain \| od -c` | `\n` | `\n` |
| `roadmap.py show item-0033` | ratified, rank 0100 | ratified, rank 0100 |
| `writeup_mapper.py check` | PASS | PASS |
| `mathjax_lint.py` | 139 files, 0 problems | 138 files, 0 problems -- **expected to move** |
| ASCII, extracts under `extract/` | 0 for all 7 | 0 for all 5 -- **file count expected to move** |
| ASCII, `HANDOVER.md` | 0 | 0 |
| ASCII, this repair log | n/a | 0 |
| `git status --porcelain` | 4 untracked, no tracked change | the writes of this apply, plus the same 4 untracked |

Two gates move and both movements are the deliverable, not a
regression. The `extract/` ASCII loop runs over two fewer files because
Lane A deleted two files; every file it does cover returns 0, as at
start. `mathjax_lint.py` covers one fewer file overall: minus the two
deleted extracts, plus this log. Zero problems at both ends, which is
the property the gate actually asserts.

No side-effecting command appears in the gate list, by the dispatch's
own design and 2c's Section 10.3 lesson. `extract-inventory.py` was not
run: it rewrites `extract-inventory-r1.md` in place, which S6 forbids,
and the severance evidence here is the Section 3 scan, which only
reads. The inventory file is therefore stale by construction against
the five-file `extract/` directory, and is left stale deliberately --
it is a timestamped record of the seven-extract state.

---

## Section 7 -- what this pass did not do

- It hashed nothing. Not an extract, not this log. `payloads/HASHES.txt`
  is byte-unchanged.
- It asserted no survivor is CLEAN. Standing is the re-grade's to
  confer.
- It did not open a dropped report, the kickoff dispatch, or an
  operator-held PDF.
- It did not re-grade a survivor. It confirmed exactly the region it
  edited, and nothing broader.
- It did not change a display or numbered object the ANN-78 grade
  marked PASS, in any file.
- It did not edit the grade file, the inventory file, the checklist, or
  any `payloads/HASHES.txt` line, including the two precedent PDF
  anchor lines.
- It did not re-verdict any claim row.
- It did not close item-0033.

---

## Section 8 -- the re-grade this pass hands off to

The five survivors are now **severance-complete**: the line-break-
tolerant scan is clean on all five, which is a strictly stronger
statement than the inventory's 0/0/0 and is the statement 2c's S7 said
was missing. They are **not graded**. Nothing here confers standing.

The re-grade is the following, separate apply:

- a **fresh executor session**, not this one, grading artifacts it did
  not produce, cross-family preferred;
- the **Phase 2b dispatch re-run over the five survivors**, pin bumped
  to this apply's commit, on the full ANN-78 fidelity surface, fresh,
  not as a diff against this log or against `repair-log-2c.md`;
- extended by the two axes 2c exposed and this pass does not settle:
  the robust dropped-object scan as an **independent** check, not
  trusting this log's word for it, and an **in-tree path-liveness
  check** on each extract's cross-references, since a CLEAN corpus
  extract must be both faithful to its source and internally consistent
  with the tree;
- it should not inherit the two page errors in the ANN-78 grade's own
  prose, recorded in `repair-log-2c.md` Section 10.2 and repeated here
  so they are not lost: reference [17] in `2312.09021v2.pdf` is printed
  on **p.37**, not p.38; and Section 5 of `2601.07421v5.pdf` begins on
  **p.10**, not p.9. Per the operator's standing choice both are left
  in the grade file as a timestamped record rather than edited;
- it should read Section 4 above before starting: the kowalski "this
  session" deictic is undischarged and is its call;
- on CLEAN it hashes the extract and the re-grade record.

**item-0033 closes when the five survivors are CLEAN and hashed and the
two precedents are dropped.** Five, not seven, is the acceptance now;
the drop is the disposition of the other two, and the close summary
records it as such. If the re-grade returns fewer than five CLEAN, the
shortfall is named and the item stays open.
