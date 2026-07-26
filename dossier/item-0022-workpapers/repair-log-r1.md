# item-0022 repair r1 -- per-row change log

Per item-0022-repair-r1.md Section 5: one entry per changed row -- row
id, what changed, before/after text, and the failure label that
motivated it. `absorption-checklist.md` was edited in place (legitimate:
the artifact is unratified and uncommitted, no append-only rule has
attached).

---

## R1-001

**What changed:** the row's Note was extended to record that its own
top-level footnote (arXiv:math/0409258) is now RESOLVED-ON-SHELF, and
that all four of its decomposed sub-claims (not three) are now
CONFIRMED. The row's own disposition header (`(synthesis -- see
decomposition)`) and its lack of an independent Governing sentence are
UNCHANGED -- this row remains a pure synthesis pointer, not a
freestanding quoted claim.

**Before (Note, relevant clause):** "...three of four are CONFIRMED
against anchors in the Section 2 set, one (the Kuperberg large-sets
$`T_k(h)`$ claim, R1-013) remains STOP 7.5."

**After (Note, relevant clause):** "[repair r1] All four are now
CONFIRMED; the row's own top-level footnote (math/0409258) is also
RESOLVED-ON-SHELF as of this repair pass (same resolution as
R1-002/R1-007)."

**Failure label motivating the change:** Task B (generalized
RESOLVED-ON-SHELF), applied by cross-reference from R1-002/R1-007/R1-013.
No independent Task A check applies to this row (no Governing sentence
of its own).

---

## R1-002

**What changed:** disposition changed from `(unverdicted -- STOP 7.5)`
to `CONFIRMED`. Full row body rewritten: added Anchoring class
RESOLVED-ON-SHELF citing three anchors (moso04-shortintervals.md for
direction 1, kuperberg22-singseries.md for direction 2, existing anchor
2 for direction 3), three Governing sentence quotes (one per direction,
each verbatim from its own extract), Support class `proved`, and a Note
recording the one-to-one mapping of report 1's three-way taxonomy onto
three distinct papers plus the Task A display-identity recheck result
(PASS for all three).

**Before (header + disposition):** `### R1-002 | T2 | mathematical |
(unverdicted -- STOP 7.5)`, with `Anchoring class: NONE -- STOP 7.5
(footnote points to arXiv:math/0409258, not a Section 2 anchor).`

**After (header + disposition):** `### R1-002 | T2 | mathematical |
CONFIRMED [repair r1: was STOP 7.5, resolved via generalized
RESOLVED-ON-SHELF]`, with three Anchoring class / Extract / Governing
sentence blocks (one per direction) as detailed in
absorption-checklist.md.

**Failure label motivating the change:** Task B (generalized
RESOLVED-ON-SHELF). Task A display-identity recheck applied to the
newly-written row: PASS (each quote located verbatim under its own
paper's own theorem heading; no cross-object confusion found).

---

## R1-007

**What changed:** the row's own footnote citation (arXiv:math/0409258),
previously left as an acknowledged STOP-7.5 gap alongside an
independent CONFIRMED verdict via a substitute anchor (anchor 3), is now
ALSO directly resolved via RESOLVED-ON-SHELF (moso04-shortintervals.md
IS the Montgomery-Soundararajan paper itself). The `Anchor:` /
`Anchor sha256:` fields were replaced with an `Anchoring class:` field
naming the shelf extract as primary and anchor 3 as secondary
corroboration. The Governing sentence field was extended to quote
Theorem 2 directly from moso04-shortintervals.md. The Note was rewritten
to record a display-identity finding: report 1's "im selben Theorem"
phrasing implies the Granville-Soundararajan uniformity remark sits
inside Theorem 2, but the extract shows it printed immediately after
Theorem 1, preceding Theorem 2 -- flagged as a minor phrasing looseness,
not a verdict-changing error. Verdict (CONFIRMED) is UNCHANGED.

**Before (Anchor field):** "Anchor: https://arxiv.org/pdf/2109.03767v3
(NOT the report's own named citation for this sentence, which is
arXiv:math/0409258 -- see Note)."

**After (Anchoring class field):** "Anchoring class: RESOLVED-ON-SHELF
..., citing dossier/item-0017-workpapers/extract/moso04-shortintervals.md
... -- this IS the Montgomery-Soundararajan paper itself, report 1's own
named source for this sentence. Secondary anchor (independent
corroboration already on record): ... anchor 3 ..."

**Failure label motivating the change:** Task B (generalized
RESOLVED-ON-SHELF) for the primary citation upgrade. Task A
display-identity recheck applied to the newly-added citation surfaced a
genuine, minor adjacency imprecision in report 1's own "im selben
Theorem" phrasing (R-DISPLAY-adjacent, but not row-vs-extract -- the
row's OWN characterization slightly misdescribes the anchor's theorem
boundary). Recorded in the Note; verdict unchanged since the underlying
mathematical content (the Rk(h) formula and the uniformity restriction)
is accurate regardless of which theorem number formally carries the
remark.

---

## R1-013

**What changed:** disposition changed from `(unverdicted -- STOP 7.5)`
to `CONFIRMED`. Full row body rewritten: Anchoring class RESOLVED-ON-SHELF
citing kuperberg22-singseries.md, Governing sentence quoting Theorem 1.1
and Theorem 1.2 verbatim from that extract, Support class `proved`, Note
recording the exact match and the Task A display-identity recheck
result (PASS).

**Before (header + disposition):** `### R1-013 | T2 | mathematical |
(unverdicted -- STOP 7.5)`, with `Anchoring class: NONE -- STOP 7.5.
Footnote 6 points to https://arxiv.org/pdf/2210.09775, which is already
hashed on the general shelf ... but is NOT one of this item's ten
Section 2 anchors and is not covered by Appendix C.`

**After (header + disposition):** `### R1-013 | T2 | mathematical |
CONFIRMED [repair r1: was STOP 7.5, resolved via generalized
RESOLVED-ON-SHELF]`, with Anchoring class / Governing sentence blocks as
detailed in absorption-checklist.md.

**Failure label motivating the change:** Task B (generalized
RESOLVED-ON-SHELF). Task A display-identity recheck applied to the
newly-written row: PASS (row's object -- Theorem 1.1 + Theorem 1.2 --
matches the extract's own Section 2 heading exactly; neighbouring
objects, the abstract before and Section 3's T_k(h)-variants discussion
after, are distinct).

---

## R1-015

**What changed:** NO change to the row's verdict, Claim, Gloss, Anchor,
Governing sentence, Support class, or Corrected form -- all UNCHANGED.
One paragraph was APPENDED to the Note recording that
item-0022-repair-r1.md Section 4 (Task C) supplied a proposed correction
to CONFIRMED, that this proposal was checked against the primary anchor
via the one PDF touch the repair dispatch itself permitted before any
rewrite (per its own instruction that "a steering-supplied quote is a
pointer, never the evidence"), and that the check did not support the
proposed correction -- the anchor's text layer shows the identical
exponent (2) in both Lemma 1's and Lemma 2's displayed formulas. No
repair was applied.

**Before:** Note ended at "...recorded CORRECTED per rule 4.3's
no-strengthening requirement regardless of intent."

**After:** the same text, followed by a new paragraph beginning
"[repair r1, Task C] item-0022-repair-r1.md Section 4 supplied a
proposed correction of this row to CONFIRMED..." (full text in
absorption-checklist.md).

**Failure label motivating the change:** none in the row-vs-extract
sense (Task A's mechanical check on the ORIGINAL row passes: the row's
quoted Governing sentence is verbatim present in
extract/pintz10-patterns.md under the object it names, "Lemma 2"). The
change here is not a Task A repair but a direct response to Task C's
explicit branch instruction, which itself anticipated and authorized
this outcome ("Steering read them from page images; the extract is the
artifact of record, and a steering-supplied quote is a pointer, never
the evidence"). See item-0022-repair-r1-report.md Section 4 for the full
evidence chain and STOP adjudication.

---

## R1-026

**What changed:** the row's header disposition changed from `(synthesis
-- 3/4 sub-claims CONFIRMED, 1/4 STOP 7.5)` to `(synthesis -- 4/4
sub-claims CONFIRMED [repair r1, was 3/4])`. The body's `Anchoring
class` field and Note were rewritten: sub-claim (a) now cites the
RESOLVED-ON-SHELF moso04 extract in addition to anchor 3; sub-claim (c)
changed from STOP 7.5 to CONFIRMED via the same kuperberg22 extract as
R1-013; sub-claim (b) is annotated with a pointer to R1-015's repair-r1
Task C finding (unchanged verdict, re-confirmed). Support class
clarified as covering all four sub-claims (was "the three confirmed
sub-claims").

**Before (header):** `### R1-026 | T1 | mathematical | (synthesis -- 3/4
sub-claims CONFIRMED, 1/4 STOP 7.5)`

**After (header):** `### R1-026 | T1 | mathematical | (synthesis -- 4/4
sub-claims CONFIRMED [repair r1, was 3/4])`

**Failure label motivating the change:** Task B (generalized
RESOLVED-ON-SHELF), by cross-reference from R1-007 and R1-013.

---

## Addendum (2026-07-26, same day, after the r1 report was first issued)

The operator supplied two further documents at the repo root,
`Pintz_Lemma2_Image_Analysis_Report.pdf` and
`Pintz_Lemmas_1_and_2_Report.pdf` (both self-described AI-assisted
analyses of the same anchor, dated 26 July 2026), and asked that Task C
be reconsidered in light of them. Per this project's standing rule that
operator-supplied or AI-generated reports are never themselves evidence
for a verdict, neither document was cited as a source; both served only
to prompt a further independent re-reading of the primary anchor,
specifically of material not previously transcribed or not previously
connected to the exponent question: equation (2.16) (the local-average
computation completing the proof that (2.11) opens) and the logical
force of the r=1 remark against a fixed-exponent-2 reading. A fresh
`pdftotext -layout -f 7 -l 8` run on `dossier/1004.1072v1.pdf`
independently confirmed that (2.16) carries the exponent r explicitly
and repeatedly (not 2), matching (2.11), and that the r=1 remark is
logically incoherent unless Lemma 2's own exponent genuinely depends on
r. This reverses the conclusion of the original Task C pass above.

### extract/pintz10-patterns.md

**What changed:** Section 2.3 was extended with the (2.12)-(2.16)
transcription and a worked-through induction deriving the general-r
bound from (2.11) and (2.16); Section 4 (uniformity ledger), Section 5
(NOT-FOUND probe), and Section 6 (COMMENTARY) were rewritten to record
that Lemma 2, read as a whole document (name, constant, threshold, r=1
remark, and proof), states and proves a genuine general-r moment bound,
with the printed exponent "2" in the isolated display (2.10) recorded
as an apparent typesetting anomaly rather than silently corrected or
silently ignored. FLAGS was extended with a revision-provenance note
naming the two operator-supplied documents and stating plainly that
they are not cited as evidence.

**Before (Section 6, relevant clause):** "The anchor's Lemma 2 does not
state this: the exponent on S(D+) is fixed at 2 throughout; r is an
unrelated, proof-internal ratio-exponent."

**After (Section 6, relevant clause):** "The most coherent reading of
the anchor as a whole ... is that Lemma 2 states, and its proof
establishes, [a general-r bound] ... The printed (2.10) ... is best read
as an apparent typesetting carry-over from Lemma 1's own display."

**Failure label motivating the change:** this is the "Extract wrong"
branch of Task C's own branch logic (Section 4: "Extract wrong: STOP
r1.5... that changes the review-gate decision rather than the row"),
determined only now, on the strength of (2.16) and the r=1 remark, which
the original extract had not adequately incorporated into its
commentary. The transcription of what (2.10) literally prints is
UNCHANGED and remains accurate; what changed is the extract's assessment
of what Lemma 2 as a whole establishes.

### absorption-checklist.md, row R1-015

**What changed:** disposition reversed from `CORRECTED` to `CONFIRMED
[reversed post-repair-r1]`. Governing sentence field extended to quote
the r=1 remark and the (2.11)/(2.16) proof material directly. Corrected
form field removed (no longer applicable). Note field rewritten to
state the coherent-reading conclusion. A full, non-destructive revision
history was appended recording all three passes (original item-0022
session: CORRECTED; repair r1 Task C: proposal to reverse checked and
not applied; this addendum: reversed to CONFIRMED) so no prior finding
is silently erased.

**Failure label motivating the change:** same as above -- an
extract-level assessment error, now corrected, discovered only after
incorporating (2.16) and the r=1 remark's logical force.

### absorption-checklist.md, row R1-026

**What changed:** sub-claim (b)'s note updated to point to R1-015's
full revision history and state it is now CONFIRMED as a genuine
general-r bound, rather than "re-examined ... continues to hold."

### absorption-checklist.md, Section 5 (consolidated table) and Section 7 (follow-ups)

**What changed:** the R1-015 table row updated to reflect the reversed
verdict; follow-up item 5 rewritten to record the full history rather
than describing the (now superseded) "checked twice, stands" conclusion.

## Files NOT changed (status as of the original Task C pass, superseded by the addendum above for `extract/pintz10-patterns.md`)

`extract/pintz10-patterns.md` was NOT changed by the original Task C
pass. Task C's branch logic ("Extract correct, row wrong: repair the
row. Extract wrong: STOP r1.5") did not resolve cleanly to either branch
at that time: the direct anchor check found the extract's original
transcription accurate and the repair dispatch's own proposed correction
unsupported. **This file WAS subsequently changed by the addendum
above**, once (2.16) and the r=1 remark were incorporated; see the
addendum's own entry for `extract/pintz10-patterns.md` and
item-0022-repair-r1-report.md's Section 4 addendum for the close-hash
accounting.

`item-0022-final-report.md` was NOT edited, per Section 5's explicit
instruction ("It is the record of the original run, and a record that
gets amended after the fact stops being one").

No file outside `dossier/item-0022-workpapers/` was touched.
