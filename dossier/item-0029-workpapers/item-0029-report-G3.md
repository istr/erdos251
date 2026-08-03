# item-0029 SESSION G3 (terminal re-grade, second cycle) -- run report

Lane: EXECUTOR (local workstation, Claude Code). Web OFF, cloud OFF for the
entire session. Executor model: claude-fable-5. Date of run: 2026-08-03; the
operator decision opening this second cycle was taken 2026-08-02 and is
ratified at ANN-20260802-96.

This session is FRESH in the rule-26(3) sense: it is none of the Sessions E,
G, R, G2 or R2, inherits no context, notes, renders or text-layer dumps from
any of them, and did not read the withheld executor-local
`shiu00-strings.md`. Everything it verified against was produced inside this
session from the anchored bytes.

## 0. Pin and rule-18 delta

P1 outcome, verbatim from the session-start check:

```
$ git rev-parse HEAD
1ecbf9142afa56879228fd2f0d0496eb2c0e065f
$ git status --short
?? item-0029-kickoff-G3-v1.md
```

HEAD equals the Section 0 pin exactly, so the first branch of P1 holds and NO
RULE-18 DELTA ARISES. The only untracked path at session start was the
ephemeral kickoff, which is never committed.

P2: `roadmap/item-0029.md` frontmatter reads `status: ratified`. Holds.

P3: `ledger/annotations/ANN-20260802-96.yaml` exists (10091 bytes) and
`python3 scripts/ledger_check.py validate` passed at 96 entries. Holds.

P4: the three gradees exist under `dossier/item-0029-workpapers/extract/`
exactly as committed at the pin -- `git status --short` reports nothing under
that path -- and the three hashed grade-chain artifacts verified against
their payloads/HASHES.txt lines before any source was opened:
`hildebrandmaier88-gaps.md` at `9d0d8bc0...6dfffa`, `extract-grades-G1.md` at
`0739f84c...71c5c7`, `extract-grades-G2.md` at `f4c564b6...63aab1`. Holds.

P5: the grep for the three gradee paths and both output paths over
payloads/HASHES.txt returned exit status 1, and neither
`extract-grades-G3.md` nor `item-0029-report-G3.md` existed ("Datei oder
Verzeichnis nicht gefunden"). Holds. The ANN collision check ran with it:
no annotation file with sequence number 97 existed at session start.

## 1. Gates at start and close

Every Section 8 gate ran twice, once before any render or output file was
made and once after all outputs existed. Verbatim close-run outputs; the two
gates whose output depends on whether the commit exists are recorded in
their post-commit form, which is the state a later session can reproduce:

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
  11 post-pin entr(ies), out of scope here, covered by append-only
RELOCATION CHECK PASSED -- concatenation is byte-identical to the old body.

$ python3 scripts/ledger_check.py validate
  97 entries, sequence numbers up to 97, 13 bets
  4 grandfathered malformed refs (allowlist size 4)
VALIDATE: passed.

$ python3 scripts/ledger_check.py append-only --base <the Section 0 pin>
APPEND-ONLY: 1 change(s) under ledger/annotations over 1ecbf9142afa56879228fd2f0d0496eb2c0e065f..HEAD, additions only.

$ python3 scripts/writeup_mapper.py check --manifest writeup/sources.yml
PASS

$ python3 scripts/mathjax_lint.py
MATHJAX LINT: 157 file(s) checked, 0 problem(s)

$ python3 .agents/skills/roadmap-items/scripts/roadmap.py show item-0029
status: ratified

ASCII check: 0 non-ASCII bytes in each new or edited file of this apply
(extract-grades-G3.md, this report, ANN-20260803-97.yaml, HANDOVER.md,
payloads/HASHES.txt).

sha256 recheck of the three hashed grade-chain artifacts against
payloads/HASHES.txt (byte-untouched proof):
dossier/item-0029-workpapers/extract/hildebrandmaier88-gaps.md: OK
dossier/item-0029-workpapers/extract-grades-G1.md: OK
dossier/item-0029-workpapers/extract-grades-G2.md: OK

sha256 recheck of every line appended by this apply against disk:
dossier/item-0029-workpapers/extract/maier85-shortintervals.md: OK
dossier/item-0029-workpapers/extract/freiberg10-strings1.md: OK
dossier/item-0029-workpapers/extract/freiberg11-strings2.md: OK
dossier/item-0029-workpapers/extract-grades-G3.md: OK

duplicate-identifier check over payloads/HASHES.txt:
114 identifiers, 114 distinct, no duplicates.

$ git diff --name-only <the Section 0 pin>..HEAD
HANDOVER.md
dossier/item-0029-workpapers/extract-grades-G3.md
dossier/item-0029-workpapers/item-0029-report-G3.md
ledger/annotations/ANN-20260803-97.yaml
payloads/HASHES.txt
```

The apply is exactly the five files of Section 9 of the kickoff. Start-run
differences, all expected and all mechanical: `mathjax_lint` reported 155
files at start against 157 at close (the grade record and this report);
`ledger_check.py relocation-check` reported 10 post-pin entries at start
against 11 at close (ANN-97); `validate` reported 96 entries at start
against 97 at close; `append-only`, the four appended-line rechecks, the
duplicate-identifier check and `git diff --name-only` are close-only.
`roadmap.py show item-0029` reported `status: ratified` at both runs,
invoked at `.agents/skills/roadmap-items/scripts/roadmap.py`. No `lake`
invocation was made. No extract file was opened for writing at any point.

## 2. Verification table V-G3

| row | class | outcome |
| --- | --- | --- |
| V1 | gate | HOLDS. Fresh executor session; none of Sessions E, G, R, G2 or R2; no artefact, render, dump or note of any of them was present or read; the session scratchpad was empty at start (0 files). The withheld `shiu00-strings.md` was never opened, and neither was the Shiu source. Operator freshness confirmed at dispatch. |
| V2 | gate | THREE MATCHES. `sha256sum` over the three needed local PDFs returned exactly the Section 2.1 anchor lines: `df9614f4...26efc` for Maier-Primes-in-short-intervals.pdf, `c08c6582...dca49` for 1005.4703v2.pdf, `407336f4...5e997` for 1110.6624v1.pdf. Verified before any source was opened. The Hildebrand-Maier source was not needed and not opened; anchor line 105 (Shiu) stayed out of scope. |
| V3 | gate | HOLD. P1 through P5 all hold; see Section 0. |
| V4 | gate | 60 PAGES ON DISK BEFORE GRADING STARTED: 6 + 24 + 30, rasterised in this session at 200 dpi from the anchored bytes with `pdftoppm`, one invocation per source. Four page regions were re-rendered at 400-500 dpi for the single-glyph, delimiter and subscript decisions -- Maier 1985 p.222 twice (the good-modulus region and the Lemma-2 constants sentence) at 400 dpi, 1005.4703v2 p.21 (the (6.4) region) at 500 dpi, and 1110.6624v1 p.12 (the (3.23) head) at 500 dpi -- each named in the record section it settles. |
| V5 | record | REPRODUCED AS EXPECTED. Maier 1985: `pdffonts` lists no fonts at all and `pdftotext` over the whole document returns 6 bytes, one form feed per page and 0 non-whitespace bytes -- no text layer. This is the expected state, not a stop (rule 9). 1005.4703v2 and 1110.6624v1: clean LaTeX-derived layers, usable for pre-comparison; every quotation and display was nevertheless closed against the render of its cited page. |
| V6 | record | RECOUNT AGREES WITH THE REPORT-R2 SECTION 4 BASELINE IN EVERY COLUMN for all three files: lines 398 / 807 / 500, quoted objects 11 / 79 / 31, display blocks 30 / 153 / 69, TRANSCRIPTION-UNSURE 0 / 0 / 0, [extract note] lines 20 / 22 / 20, FLAGS bullets 6 / 7 / 7, multi-line closers 2 / 0 / 0 and surplus delimiter lines 3 / 1 / 1 per the corrected D3 reading (the surplus lines are line 15 in each file plus maier85 lines 86 and 151). No divergence, so no recount finding entered the grade. |

## 3. Grade summary

| extract | verdict | defects |
| --- | --- | --- |
| maier85-shortintervals.md | CLEAN | 0 |
| freiberg10-strings1.md | CLEAN | 0 |
| freiberg11-strings2.md | CLEAN | 0 |

Three CLEAN, zero DEFECTIVE, zero defect rows. All seven defect classes are
empty across all three extracts. The full per-extract surface record is
`dossier/item-0029-workpapers/extract-grades-G3.md`; this report does not
restate it.

Per Section 4.4 of the dispatch, four HASHES lines were appended: one per
CLEAN extract in Section 2.2 order, then one for the grade record. Each was
re-verified against disk after the append and the one-line-per-file
invariant was re-checked over the whole file (114 identifiers, 114
distinct).

All eighteen sites repaired across both cycles -- the fourteen G1 positions
of Session R and the four G2 positions of Session R2 -- were re-checked as
ordinary surface, neither privileged nor skipped, and every one is correct
as applied.

## 4. Surface statistics

Totals checked across the three gradees, by dispatch surface class:

| class | surface | total checked |
| --- | --- | --- |
| S-a | verbatim-quoted numbered or named objects | 121 (11 / 79 / 31) |
| S-a | quotation-opening lines carrying quoted prose | 336 (54 / 193 / 89) |
| S-b | `$$` display blocks | 252 (30 / 153 / 69) |
| S-c | explicit page references | 221 (43 / 116 / 62), of which 91 are per-display page labels (65 / 26) beyond maier85's inline labels |
| S-d | [extract note] lines | 62 (20 / 22 / 20), including 24 structural-map lines and 20 uniformity-ledger items |
| S-e | header fields | 18 (6 per extract) |
| S-f | scope sweeps | 2 FULL completeness sweeps plus 1 PARTIAL boundary check |
| S-g | FLAGS statements | 20 (6 / 7 / 7) |
| S-h | absence sweeps | 3, one per extract |

The two FULL sweeps found no omission: all 11 objects of Maier 1985 and all
79 of 1005.4703v2 are present, the latter checked object by object against a
mechanical enumeration of the 68 numbered displays and 11 named statements
before the render pass began. The PARTIAL boundary of
`freiberg11-strings2.md` is exactly honoured -- Sections 1-3 complete with
all 26 numbered displays, nothing from Section 4 beyond its printed heading
quoted as a named reference, all four factual claims of the scope-boundary
section verified true against the renders of pp.13, 29 and 30, and pp.14-28
checked to carry no intervening section heading. Class (d) is empty.

The S-h sweeps returned no axis, gate, verdict, NOT-FOUND, grade-state or
project-object language in any of the three.

## 5. Deviations and surprises

D1. ONE JUDGMENT CALL ON A PAGE ANCHOR, disclosed with its reasoning so a
later session can overrule it against the record rather than re-derive it.
The seventh uniformity-ledger item of `freiberg10-strings1.md` says "the
implied constant in (6.2) is stated absolute (p.20)". Display (6.2) is
printed on p.20; the sentence that states it -- "We will first prove that
the estimate (6.2) holds, with an absolute implied constant" -- begins on
p.20 with the display inside it and completes at the head of p.21. This
session read the parenthetical as locating the display the claim names,
which is on the cited page, and did not fire. That reading is consistent
with both prior grades: the G1 and G2 passes each verified this item as
true and page-anchored, and G2 did so in the same session in which it fired
M2 on the straddle standard -- the operative difference being that at M2
NEITHER distinguishing component of the cited claim sat on the cited page,
while here the named display itself does. No fixed reading governs this
surface either way.

D2. THE VERDICT MOVED FROM 0 CLEAN TO 3 CLEAN AND NOTHING ELSE MOVED. The
four G2 rows were the only deviations the G2 pass had left; all four
repairs reproduce the printed forms exactly, at 500 dpi where a subscript
row or delimiter decision required it, and the full-surface re-check found
no new deviation anywhere -- no transcription drift beside the repaired
sites, no page-reference slip, no untrue note or FLAGS clause. Both prior
grade passes plus the two repair passes have now each covered this surface
without surfacing a residual, which is what the terminal outcome rests on.

D3. TWO TYPOGRAPHY OBSERVATIONS WERE CLASSED AS LAYOUT UNDER FIXED READING
1 AND NOT GRADED: the upright differential in the printed "du" of the p.12
integral of 1110.6624v1, which the extract renders in the default italic
face with the character sequence unchanged; and the em-dashes of both
Freiberg sources, folded to ASCII double hyphens per the extracts' Section
0 conventions. Neither changes a character of the wording or of the
mathematics in the fixed readings' sense.

D4. A SCAN SPECKLE ON p.222 OF MAIER 1985 WAS SETTLED AT 400 DPI: the faint
mark between "Lemma" and "1" in the constants sentence is above the
baseline, attaches to no character box, and does not recur in either other
occurrence of "Lemma 1" on the page; it is not a printed character and the
extract's transcription is exact.

D5. NO FIDELITY DOUBT ABOUT ANY HASHED FILE AROSE. The five item-0022
extracts and `hildebrandmaier88-gaps.md` were not opened;
`extract-grades-G1.md` and `extract-grades-G2.md` were read as governing
texts and all three grade-chain artifacts still verify against their hash
lines at close. r29G3.6 did not trigger.

## 6. STOP conditions

All ten reported by name, none fired.

- r29G3.1 validity failure: NOT FIRED. P1 held on its first branch (HEAD
  equalled the pin), P2 ratified, P3 present and validating, P4 clean
  targets and three hash matches, P5 no prior lines and no prior outputs.
- r29G3.2 source-hash mismatch: NOT FIRED. Three matches, checked before
  any source was opened.
- r29G3.3 freshness breach: NOT FIRED. The scratchpad was empty at session
  start; all 60 renders, all four region re-renders and both text-layer
  dumps used here were produced in this session from the anchored bytes;
  the withheld extract was never opened.
- r29G3.4 scope pressure: NOT FIRED. No step required editing an extract,
  re-grading `hildebrandmaier88-gaps.md`, opening the Shiu source or
  extract, network access, a source beyond the three, or a Lean edit.
- r29G3.5 envelope breach: NOT FIRED. `extract-grades-G3.md` is 297 lines
  inside 100-800; this report is inside 120-450. Neither was padded or
  trimmed to fit.
- r29G3.6 fidelity doubt about a hashed file: NOT FIRED. None arose; see
  D5.
- r29G3.7 consumption drift: NOT FIRED. No extract content was used for
  item-0029 substance. No axis, no positive-proportion gate, no named
  finding, and no comparison to a project object appears in the grade
  record or in this report.
- r29G3.8 ANN sequence collision: NOT FIRED. No annotation with sequence
  number 97 existed at session start; the computed next number is 97.
- r29G3.9 close-gate failure: NOT FIRED. All Section 8 gates are green at
  close; see Section 1.
- r29G3.10 instruction unsatisfiable or internally divergent: NOT FIRED.
  All three gradees were graded to a verdict inside the session, so the
  Section 10 UNGRADED fallback was not needed. No finding was proposed
  that would rest on rejecting one of the six fixed readings; the readings
  were applied as fixed at every site they reach (the label-spanning
  displays of Maier 1985 under reading 4, the reflowed subscript rows of
  both Freiberg extracts under reading 5, the Section 0 folding
  declarations under reading 2, the unfolded alphabet renderings under
  reading 3, the layout linearisation of multi-line chains under reading
  1, and the FLAGS divergence bullets under reading 6).

## 7. Budget reconciliation

| task | dispatch estimate | actual |
| --- | --- | --- |
| V-G3 table, gates at start, 60-page render pass | mechanical | as estimated; one `pdftoppm` invocation per source, four high-dpi region crops. |
| completeness sweeps (S-f) over the three sources | FIRST per source; omissions are the costliest class to find late | done first per source (for 1005.4703v2 as a mechanical enumeration of all 79 objects before the render pass) and returned nothing in all three cases; class (d) is empty. |
| quotation/display verification (S-a..S-c) | the bulk: 121 quoted objects, 252 display blocks, ~1705 extract lines against 60 rendered pages | as estimated in volume and the bulk of the session; every page of all three sources was read against its extract section in order. Zero deviations. |
| notes/maps/headers/FLAGS (S-d, S-e, S-g, S-h) | 62 note lines, three structural maps, the six-item slip list; both prior grades found half or more of their defect mass here and in the display fine structure | every line came back true this time; the cost was verification that confirmed rather than overturned, including the pp.6-11 no-calligraphic-S sweep, the pp.14-28 no-heading sweep and the pp.29-30 boundary renders. |
| record, report, ANN, HANDOVER, close gates | mechanical | as estimated. |

All three gradees were graded to a verdict; none was left UNGRADED. No
proof work, no computation beyond hashing, rendering, pixel counting and
linting; no Lean, no network, no roadmap edit, no extract content consumed
for item-0029 substance. The only object out of reach remains the Shiu
extract, which is not in the tree and which this session was directed to
leave alone.

## 8. Terminality

THE OPERATOR-OPENED SECOND CYCLE ENDS WITH THIS SESSION. The outcome that
occurred is the first of the outcomes the Frame names, and its clause is
restated here verbatim: "3 CLEAN (hash all three + the record; the second
cycle closes fully and Session M has the full four-extract surrogate set)".

All three gradees are CLEAN and hashed by this apply, and each NOW CARRIES
CORPUS STANDING as a source surrogate for both lanes (rule 26(4)),
alongside `hildebrandmaier88-gaps.md` on the standing ANN-93 conferred.
Session M may consume the full four-extract surrogate set. No DEFECTIVE
remainder exists, so no further operator decision on extract disposition is
required; the Shiu exclusion of ANN-92 is untouched by this session and
remains the operator's standing question. This session neither took nor
prejudged any Session M step.
