# item-0029 SESSION G2 (terminal re-grade) -- run report

Lane: EXECUTOR (local workstation, Claude Code). Web OFF, cloud OFF for the
entire session. Executor model: claude-opus-5. Date of run: 2026-08-02.

This session is FRESH in the rule-26(3) sense: it is none of the Sessions E, G
or R, inherits no context, notes, renders or text-layer dumps from any of them,
and did not read the withheld executor-local `shiu00-strings.md`. Everything it
verified against was produced inside this session from the anchored bytes.

## 0. Pin and rule-18 delta

P1 outcome, verbatim from the session-start check:

```
$ git rev-parse HEAD
e7a467e79d5c973914416c477369da9ff0fbaab0
$ git diff e7a467e79d5c973914416c477369da9ff0fbaab0..HEAD --name-only
(no output)
$ git status --short
?? item-0029-kickoff-G2-v1.md
?? item-0029-kickoff-R-v1.md
```

HEAD equals the Section 0 pin exactly, so the first branch of P1 holds and NO
RULE-18 DELTA ARISES. The only untracked paths at session start were the two
ephemeral kickoffs, which are never committed.

P2: `roadmap/item-0029.md` frontmatter reads `status: ratified`. Holds.

P3: `ledger/annotations/ANN-20260802-94.yaml` exists (9752 bytes) and
`python3 scripts/ledger_check.py validate` passed at 94 entries. Holds.

P4: the three gradees exist under `dossier/item-0029-workpapers/extract/`
exactly as committed at the pin -- `git status --short` reports nothing under
that path -- and both hashed session-G artifacts verified against
`payloads/HASHES.txt` lines 108 and 109 before any source was opened:
`hildebrandmaier88-gaps.md` at `9d0d8bc0...6dfffa` and `extract-grades-G1.md`
at `0739f84c...5e71c5c7`. Holds.

P5: the grep for the five identifiers over `payloads/HASHES.txt` returned exit
status 1 on 109 lines, and neither `extract-grades-G2.md` nor
`item-0029-report-G2.md` existed ("Datei oder Verzeichnis nicht gefunden").
Holds.

## 1. Gates at start and close

Every Section 8 gate was run twice, once before any render or output file was
made and once after all outputs existed. Verbatim close-run outputs:

```
$ python3 lean/scripts/blocks.py check-frozen
  OK   erdos_251_irrational               lean/Erdos251/Statement.lean:18
  OK   HLQuantA                           lean/Erdos251/Hypotheses.lean:199
  OK   CramerGranville                    lean/Erdos251/Hypotheses.lean:210

FROZEN BLOCKS: all byte-identical.

$ python3 lean/scripts/blocks.py relocation-check
RELOCATION CHECK PASSED -- concatenation is byte-identical to the old body.
  (old body @ 6683ee0  2681 lines  sha256 af4615e1c92c4c070bb0217667777d2816571bf706b1a3034f2f3d83b5ea4388)

$ grep -rnE '^\s*sorry\s*$' lean/Erdos251/
lean/Erdos251/Statement.lean:21:  sorry

$ grep -c a6276f4c6097675b1cf5ebd49b1146b735f38c02 lean/lake-manifest.json
1

$ tail -c 1 lean/lean-toolchain | od -c
0000000  \n
0000001

$ python3 scripts/ledger_check.py relocation-check
  86 pinned entries, ascending sequence order
  9 post-pin entr(ies), out of scope here, covered by append-only
RELOCATION CHECK PASSED -- concatenation is byte-identical to the old body.

$ python3 scripts/ledger_check.py validate
  95 entries, sequence numbers up to 95, 13 bets
  4 grandfathered malformed refs (allowlist size 4)
VALIDATE: passed.

$ python3 scripts/ledger_check.py append-only --base <the Section 0 pin>
APPEND-ONLY: 1 change(s) under ledger/annotations over e7a467e79d5c973914416c477369da9ff0fbaab0..HEAD, additions only.

$ python3 scripts/writeup_mapper.py check --manifest writeup/sources.yml
PASS

$ python3 scripts/mathjax_lint.py
MATHJAX LINT: 155 file(s) checked, 0 problem(s)

$ python3 .agents/skills/roadmap-items/scripts/roadmap.py show item-0029
status: ratified

ASCII check: 0 non-ASCII bytes in each of the three new files of this apply
(extract-grades-G2.md, item-0029-report-G2.md, ANN-20260802-95.yaml) and in
the two edited files (HANDOVER.md, payloads/HASHES.txt).

sha256 recheck of the two hashed session-G artifacts against payloads/HASHES.txt
(byte-untouched proof):
dossier/item-0029-workpapers/extract/hildebrandmaier88-gaps.md: OK
dossier/item-0029-workpapers/extract-grades-G1.md: OK

sha256 recheck of every line appended by this apply against disk:
dossier/item-0029-workpapers/extract-grades-G2.md: OK

duplicate-identifier check over payloads/HASHES.txt:
110 identifiers, 110 distinct, no duplicates.

$ git diff --name-only <the Section 0 pin>..HEAD
HANDOVER.md
dossier/item-0029-workpapers/extract-grades-G2.md
dossier/item-0029-workpapers/item-0029-report-G2.md
ledger/annotations/ANN-20260802-95.yaml
payloads/HASHES.txt
```

The apply is exactly the five files of Section 9. The two paths left untracked
are the ephemeral kickoffs, which are never committed. The two gates whose
output depends on whether the commit exists are recorded above in their
post-commit form, which is the state a later session can reproduce:
`append-only` reads 1 change over the pin..HEAD range, additions only (it reads
0 while the outputs are still uncommitted), and `git diff --name-only` is empty
before the commit.

Start-run differences, all expected and all mechanical: `mathjax_lint` reported
153 files at start against 155 at close (the grade record and this report);
`ledger_check.py relocation-check` reported 8 post-pin entries at start against
9 at close (ANN-95); `ledger_check.py validate` reported 94 entries at start
against 95 at close; and `append-only` is a close-only gate and was not run at
start, as were the two HASHES rechecks and the duplicate-identifier check, the
last two licensed only because a line was appended. `roadmap.py show item-0029`
reported `status: ratified` at both runs. The roadmap tool was invoked at
`.agents/skills/roadmap-items/scripts/roadmap.py`. No `lake` invocation was
made. No extract file was opened for writing at any point.

## 2. Verification table V-G2

| row | class | outcome |
| --- | --- | --- |
| V1 | gate | HOLDS. Fresh executor session; not Session E, not Session G, not Session R; no artefact, render, dump or note of any of them was present or read; the session scratchpad was empty at start, 0 files. The withheld `shiu00-strings.md` was never opened, and neither was the Shiu source. Operator freshness confirmed at dispatch. |
| V2 | gate | THREE MATCHES. `sha256sum` over the three needed local PDFs returned exactly the Section 2.1 anchor lines: `df9614f4...26efc` for Maier-Primes-in-short-intervals.pdf, `c08c6582...dca49` for 1005.4703v2.pdf, `407336f4...5e997` for 1110.6624v1.pdf. Verified before any source was opened. The Hildebrand-Maier source was not needed and not opened; anchor line 105 (Shiu) stayed out of scope. |
| V3 | gate | HOLD. P1 through P5 all hold; see Section 0. |
| V4 | gate | 60 PAGES ON DISK BEFORE GRADING STARTED: 6 + 24 + 30, rasterised in this session at 200 dpi from the anchored bytes with `pdftoppm`, one invocation per source. Nine page regions were later re-rendered at 400-500 dpi to settle single-glyph, delimiter and subscript decisions -- Maier 1985 p.222 and the p.223/p.224 break (three crops), 1005.4703v2 pp.10, 17 and 21, and 1110.6624v1 p.11 (three regions) and p.12 -- each named in the row it settles. |
| V5 | record | REPRODUCED AS EXPECTED. Maier 1985: `pdffonts` lists no fonts at all and `pdftotext` over the whole document returns 6 bytes, one form feed per page -- no text layer. This is the expected state, not a stop (rule 9). 1005.4703v2 and 1110.6624v1: clean LaTeX-derived Computer Modern layers, usable for pre-comparison; every quotation and display was nevertheless closed against the render of its cited page. |
| V6 | record | RECOUNT AGREES WITH THE REPORT-R SECTION 4 BASELINE IN EVERY COLUMN for all three files: lines 398 / 806 / 499, quoted objects 11 / 79 / 31, display blocks 30 / 153 / 68, TRANSCRIPTION-UNSURE 0 / 0 / 0, [extract note] lines 20 / 22 / 20, FLAGS bullets 6 / 7 / 7, surplus delimiter lines 3 / 1 / 1. No divergence, so no recount finding entered the defect tables. One PROSE gloss of the baseline is corrected in Section 4 of the record without moving any number; see D3 below. |

## 3. Grade summary

| extract | verdict | defects |
| --- | --- | --- |
| maier85-shortintervals.md | DEFECTIVE | 1 |
| freiberg10-strings1.md | DEFECTIVE | 2 |
| freiberg11-strings2.md | DEFECTIVE | 1 |

Zero CLEAN, three DEFECTIVE, 4 defect rows. By class: (a) transcription
deviation 2, (b) page-reference error 1, (c) untrue or interpretive note claim
1. Classes (d) scope violation, (e) untrue header field, (f) forbidden language
and (g) untrue FLAGS statement are empty across all three extracts.

Every defect row -- file, extract line, source page, class, verbatim is-state,
verbatim should-state, and the finding that establishes it -- is in
`dossier/item-0029-workpapers/extract-grades-G2.md`. This report does not
restate it.

Per Section 4.4 of the dispatch, zero CLEAN means exactly one appended HASHES
line: the grade record's own. The three DEFECTIVE extracts got no line.

All fourteen sites Session R repaired were re-checked as ordinary surface --
neither privileged nor skipped -- and every one is correct as applied. None of
the four new rows sits at a repaired site; all four are surface the G1 pass
covered and passed.

## 4. Surface statistics

Totals checked across the three gradees, by dispatch surface class:

| class | surface | total checked |
| --- | --- | --- |
| S-a | verbatim-quoted numbered or named objects | 121 (11 / 79 / 31) |
| S-a | quotation-opening lines carrying quoted prose | 336 (54 / 193 / 89) |
| S-b | `$$` display blocks | 251 (30 / 153 / 68) |
| S-c | explicit page references | 221 (43 / 116 / 62), of which 97 are per-display page labels |
| S-d | [extract note] lines | 62 (20 / 22 / 20), including 24 structural-map lines and 20 uniformity-ledger items |
| S-e | header fields | 18 (6 per extract) |
| S-f | scope sweeps | 2 FULL completeness sweeps plus 1 PARTIAL boundary check |
| S-g | FLAGS statements | 20 (6 / 7 / 7) |
| S-h | absence sweeps | 3, one per extract |

The two FULL sweeps found no omission: all 68 numbered displays of
1005.4703v2 and all eleven of its numbered or named statements are present, as
are all 11 objects of Maier 1985. The PARTIAL boundary of
`freiberg11-strings2.md` is exactly honoured -- Sections 1-3 complete with all
26 numbered displays, nothing from Section 4 beyond its printed heading quoted
as a named reference, and all four factual claims of the scope-boundary section
verified true against the renders of pp.13, 29 and 30, with pp.14-28 checked to
carry no intervening section heading. Class (d) is empty.

The S-h sweeps returned no axis, gate, verdict, NOT-FOUND, grade-state or
project-object language in any of the three. The ledger identifier that carried
G1's defect F1 is gone from `freiberg10-strings1.md`.

The two ranges report-R O1 named as unverified were checked without prejudice
and are TRUE as printed: Section 4 of 1005.4703v2 runs pp.6-11, ending on p.11
above the "5. Proof of Proposition 2.3" heading, and Lemma 5.5 is proved on
pp.17-20, its closing box on p.20 above the "6. A lower bound" heading.

## 5. Deviations and surprises

D1. THREE JUDGMENT CALLS, disclosed with their reasoning so a later session can
overrule them against the record rather than re-derive them. None of the three
rests on rejecting a fixed reading of report-G Section 5 D1; each sits in
surface those readings do not reach.

(a) AN EQUATION LABEL SPANNING A MULTI-LINE DISPLAY IS LAYOUT. On p.223 of
Maier 1985 the label (2.2) sits to the left of a three-line display group whose
lines are "h is analytic for u > -1,", the functional equation, and the
asymptotic. Three evenly spaced lines make "aligned with the middle line" and
"vertically centred on the group" the same position, so the render cannot
decide whether the number covers two lines or three; the extract labels the
lower two. The fixed reading (a) draws its line at "whether the printed
delimiter separates layout rows or binds operands", and nothing here binds
operands: no character of the wording or the mathematics changes either way.
Not fired. The extract handles (2.1) on p.222 the same way, so the treatment is
at least internally consistent.

(b) A REFLOWED SUBSCRIPT ROW IS LAYOUT; A DROPPED ONE IS NOT. Several sums in
both Freiberg sources print three-row subscripts, and the extracts wrap them
into two rows -- for instance "m <= t(H)/e^l", "p | m => p == 1 mod q", "and
p > log H" becomes two `\substack` rows with the third clause carried onto the
second. Nothing printed is absent; the split point moves. That is the same
class as a line break reflowed into a separator and was not graded. Defect F10
is the other case: there a whole printed row, the index row "d_1,...,d_4" of
the third sum in (6.4) on p.21, is simply not in the extract, and S-a names
summation bounds. The line drawn is content-present versus content-absent, not
row-count.

(c) THE FLAGS DIVERGENCE BULLETS THAT NAME THE EXTRACTION BRIEF ARE NOT
FORBIDDEN LANGUAGE. All three extracts carry FLAGS bullets of the form
"Divergence from the dispatch's Section 4.x attention list: ...". They name a
process object no in-tree reader can open, which is why the call is disclosed.
They were not fired, for two reasons. Rule 27 requires the extract to declare
its extraction method and scope, so an extract documenting where its own brief
and the source diverge is documenting the declared method rather than importing
a project verdict; and every such bullet's substance is a checkable claim about
the source, all of which were verified true here. The contrast with G1's F1 is
the operative one: F1 was fired because its sentence was not a claim about the
source at all and named a ledger entry that goes stale. This reading also
matters because `hildebrandmaier88-gaps.md` is CLEAN and hashed and, per the G1
record's own description of its FLAGS, carries V-finding echoes of the same
family; firing here would have put a hashed artifact in doubt, which r29G2.6
routes rather than answers. No doubt arose, because the reading holds on its
merits.

D2. THE DEFECT MASS MOVED, AND THE DEFECTS THAT SURVIVED ARE THE QUIET KIND. G1
found 13 rows over four extracts, seven of them in notes, maps, headings and
FLAGS. After the repair, the four rows left are two dropped fragments inside
display blocks, one page locator understated by a page, and one false section
attribution inside a conventions note. What they have in common is that each
reads as correct in isolation: the (6.4) sum is well formed without its index
row, the (3.23) chain is true without its middle member, "(p.223)" points at a
page where the sentence does begin, and the calligraphic-S convention is
correctly stated except for where it applies. A reader of the extract cannot
detect any of them without the source, which is exactly the failure mode rule
26 names.

D3. THE V6 BASELINE'S NUMBERS HOLD BUT ONE OF ITS GLOSSES DOES NOT. The
surplus-delimiter count is 3 / 1 / 1 as the baseline states, but those lines are
not all "closers of multi-line blocks". In `maier85-shortintervals.md` two of
the three are closers (lines 86 and 151) and the third is the Section 0
conventions note at line 15 that mentions the delimiter inside a code span; in
each Freiberg extract the single surplus line is that same Section 0 note, and
neither file contains a multi-line display block at all. The true
multi-line-closer counts are 2 / 0 / 0. This is recorded in Section 4 of the
grade record and NOT as a defect row: the gloss lives in report-R and the G1
record, neither of which is a gradee, and no extract asserts it.

D4. THE THREE REPAIRED DISPLAY SITES AND THE R-A MOVE WERE RE-VERIFIED AT HIGH
RESOLUTION AND ARE EXACT. The p.7 brace pair, the p.10 unsubscripted factor and
the p.17 unprimed variable of 1005.4703v2, and all three p.11 parenthesisations
of 1110.6624v1, reproduce the printed forms character for character. The moved
section-sign declaration is true of the source at every example it names, and
the one authorized wording change report-R O3 discloses -- "above" fitted to
"below" -- is true in the sentence's new position, since the transcription does
follow Section 0.

D5. NO FIDELITY DOUBT ABOUT ANY HASHED FILE AROSE. `hildebrandmaier88-gaps.md`
and the five item-0022 extracts were not opened; `extract-grades-G1.md` was
read as a governing text and both it and the Hildebrand-Maier extract still
verify against their hash lines at close. r29G2.6 did not trigger.

## 6. STOP conditions

All ten reported by name, none fired.

- r29G2.1 validity failure (P1 content-path delta, P2, P3, P4, P5): NOT FIRED.
  HEAD equalled the pin with an empty diff, item-0029 was ratified, ANN-94
  existed and validated, the three gradees were clean under the extract path
  and both hashed artifacts verified, and no HASHES line carried any of the
  five identifiers with neither output file present.
- r29G2.2 source-hash mismatch on any needed source (V2): NOT FIRED. All three
  matched, checked before any source was opened.
- r29G2.3 freshness breach or reuse of Session E, G or R renders, dumps or
  notes, or any read of the withheld shiu00-strings.md: NOT FIRED. The
  scratchpad was empty at session start; all 60 renders, all nine region
  re-renders and both text-layer dumps used here were produced in this session
  from the anchored bytes; the withheld extract was never opened.
- r29G2.4 scope pressure: NOT FIRED. No step required editing an extract,
  re-grading `hildebrandmaier88-gaps.md`, opening the Shiu source or extract,
  network access, a source beyond the three, or a Lean edit. The four defects
  were recorded, not repaired.
- r29G2.5 envelope breach, either direction: NOT FIRED. `extract-grades-G2.md`
  is inside 100-800 and this report is inside 120-450. Neither was padded or
  trimmed to fit.
- r29G2.6 fidelity doubt about a hashed file: NOT FIRED. None arose; see D5.
  The one place where it could have -- D1(c) -- was resolved on its merits
  without reaching the hashed extract.
- r29G2.7 consumption drift: NOT FIRED. No extract content was used for
  item-0029 substance. No axis, no positive-proportion gate, no named finding,
  and no comparison to a project object appears in the grade record or in this
  report.
- r29G2.8 ANN sequence collision: NOT FIRED.
  `ledger/annotations/ANN-20260802-95.yaml` did not exist at session start; the
  computed next number is 95.
- r29G2.9 close-gate failure: NOT FIRED. All Section 8 gates are green at
  close; see Section 1.
- r29G2.10 instruction unsatisfiable or internally divergent, including a
  finding founded only on rejecting one of the three fixed D1 readings: NOT
  FIRED. All three gradees were graded to a verdict inside the session, so the
  Section 10 UNGRADED fallback was not needed. None of the four defect rows
  requires rejecting a fixed reading: F10 and G4 are absent printed content
  rather than layout choices, M2 is a page locator, and F11 is a false section
  attribution. Reading (b) was applied as fixed and the R-A declaration was
  read as conformant; reading (c) was applied as fixed to the undeclared
  calligraphic H and Fraktur S of `freiberg11-strings2.md`, which are faithful
  unfolded renderings and were not graded as folding patterns.

## 7. Budget reconciliation

| task | dispatch estimate | actual |
| --- | --- | --- |
| V-G2 table, gates at start, 60-page render pass | mechanical | as estimated; one `pdftoppm` invocation per source, no re-runs. The nine high-dpi region crops were taken from the anchored bytes rather than upscaled. |
| completeness sweeps (S-f) over the three sources | FIRST per source; omissions are the costliest class to find late | done first per source and returned nothing in all three cases; class (d) is empty. The advice held in the sense that it cost little and closed the costliest class early. |
| quotation and display verification (S-a to S-c) | the bulk: 121 quoted objects, 251 display blocks, ~1703 extract lines against 60 rendered pages | as estimated in volume and the bulk of the session. Two defects, both found by reading a printed display against its transcription rather than by any check that could be automated. |
| notes, maps, headers, FLAGS (S-d, S-e, S-g, S-h) | 62 note lines, three structural maps, the O1 ranges, the six-item slip list; the G1 run found more than half its defect mass exactly here | half the defect mass again, two of four rows. The O1 ranges and the six-item slip list all came back true, so the cost here was verification that confirmed rather than overturned; the two rows came from a uniformity-ledger locator and a conventions note. |
| record, report, ANN, HANDOVER, close gates | mechanical | as estimated. |

All three gradees were graded to a verdict; none was left UNGRADED. No proof
work, no computation beyond hashing, rendering, pixel counting and linting; no
Lean, no network, no roadmap edit. The only object out of reach remains the
Shiu extract, which is not in the tree and which this session was directed to
leave alone.

## 8. Terminality

THE ANN-20260801-91 CYCLE IS SPENT WITH THIS SESSION. The outcome that occurred
is the second of the two the Frame names, and its clause is restated here
verbatim: "mixed or 0 CLEAN (hash the CLEAN subset + the record; the loop closes
with the DEFECTIVE remainder carrying NO standing, "direct attention at most",
and the decision on what happens to them -- run Session M on the CLEAN subset,
or open a NEW operator-gated cycle -- is the OPERATOR'S, booked as an open
question in the ANN, not resolved by this session). There is no second repair
inside this cycle under any outcome."

The CLEAN subset is empty, so the only line appended is the grade record's own.
The three DEFECTIVE extracts carry no standing and neither lane may consume
them. The CLEAN surrogate set Session M may consume is
`hildebrandmaier88-gaps.md` alone, on the standing ANN-93 conferred. The
operator question is booked in ANN-20260802-95 with its two alternatives named
and neither chosen. No further repair pass may run without a new operator-gated
decision, and this session neither took nor prejudged that decision.
