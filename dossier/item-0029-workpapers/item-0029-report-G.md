# item-0029 SESSION G (fidelity grade) -- run report

Lane: EXECUTOR (local workstation, Claude Code). Web OFF, cloud OFF for the
entire session. Executor model: claude-opus-5. Date of run: 2026-08-02.

## 0. Pin and rule-18 delta

P1 outcome, verbatim from the session-start check:

```
$ git rev-parse HEAD
4b4f5f2999441d9a0474c9ffa85976a5f8b973df
$ git status --short
?? item-0029-kickoff-G-v1.md
$ git diff 4b4f5f2999441d9a0474c9ffa85976a5f8b973df..HEAD --name-only
(no output)
```

HEAD equals the Section 0 pin exactly, so the first branch of P1 holds and NO
RULE-18 DELTA ARISES. The only untracked path at session start was the ephemeral
kickoff itself, which is never committed.

P2: `roadmap/item-0029.md` frontmatter reads `status: ratified`. Holds.

P3: `ledger/annotations/ANN-20260801-92.yaml` exists (9766 bytes) and
`python3 scripts/ledger_check.py validate` passed. Holds.

P4: the four extract files exist under
`dossier/item-0029-workpapers/extract/` exactly as committed at the pin --
`git status --short` reports nothing under that path -- and
`dossier/item-0029-workpapers/extract/shiu00-strings.md` is NOT tracked:
`git check-ignore -v` resolves it to `.gitignore:11`, and it is absent from
`git ls-files`. Holds.

P5: `payloads/HASHES.txt` at session start contained NO line whose identifier
column matched `item-0029-workpapers`; the grep returned exit status 1 on 107
lines. No prior partial hashing. Holds.

## 1. Gates at start and close

Every Section 8 gate was run twice, once before any output file was created and
once after all outputs existed. Verbatim close-run outputs:

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
  7 post-pin entr(ies), out of scope here, covered by append-only
RELOCATION CHECK PASSED -- concatenation is byte-identical to the old body.

$ python3 scripts/ledger_check.py validate
  93 entries, sequence numbers up to 93, 13 bets
  4 grandfathered malformed refs (allowlist size 4)
VALIDATE: passed.

$ python3 scripts/ledger_check.py append-only --base <the Section 0 pin>
APPEND-ONLY: 0 change(s) under ledger/annotations over 4b4f5f2999441d9a0474c9ffa85976a5f8b973df..HEAD, additions only.

$ python3 scripts/writeup_mapper.py check --manifest writeup/sources.yml
PASS

$ python3 scripts/mathjax_lint.py
MATHJAX LINT: 151 file(s) checked, 0 problem(s)

$ python3 .agents/skills/roadmap-items/scripts/roadmap.py show item-0029
status: ratified

ASCII check: 0 non-ASCII bytes in each of the three new files of this apply
(extract-grades-G1.md, item-0029-report-G.md, ANN-20260802-93.yaml) and in the
two edited files (HANDOVER.md, payloads/HASHES.txt).

sha256sum recheck of every appended line against the file on disk:
dossier/item-0029-workpapers/extract/hildebrandmaier88-gaps.md: OK
dossier/item-0029-workpapers/extract-grades-G1.md: OK

duplicate-identifier check over payloads/HASHES.txt:
109 identifiers, 109 distinct, no duplicates.
```

Start-run differences, all expected and all mechanical: `mathjax_lint` reported
149 files at start against 151 at close (the grade record and this report);
`ledger_check.py relocation-check` reported 6 post-pin entries at start against 7
at close (ANN-93); `ledger_check.py validate` reported 92 entries at start
against 93 at close; `append-only` is a close-only gate and was not run at start;
and the HASHES rechecks are close-only and licensed only because lines were
appended. `roadmap.py show item-0029` reported `status: ratified` at both runs.
The roadmap tool was invoked at `.agents/skills/roadmap-items/scripts/roadmap.py`.
No `lake` invocation was made.

## 2. Verification table V-G

| row | class | outcome |
| --- | --- | --- |
| V1 | gate | HOLDS. This is a new executor session. It is not the Session E session, inherits none of its context, notes, renders or text-layer dumps, and did not read the withheld `shiu00-strings.md`. The session scratchpad was empty at start; no Session E artefact exists anywhere reachable. Operator freshness confirmed at dispatch. |
| V2 | gate | FOUR MATCHES. `sha256sum` over the four local PDFs returned exactly the Section 2.1 anchor lines: `3a8666eb...e3261` for S0002-9939-1988-0958032-5.pdf, `df9614f4...26efc` for Maier-Primes-in-short-intervals.pdf, `c08c6582...dca49` for 1005.4703v2.pdf, `407336f4...5e997` for 1110.6624v1.pdf. Verified before any source was opened. |
| V3 | gate | HOLD. P1 through P5 all hold; see Section 0. |
| V4 | gate | 69 PAGES ON DISK before grading started: 9 + 6 + 24 + 30, all rasterised in this session at 200 dpi from the anchored bytes with `pdftoppm`. Four page regions were later re-rendered at 300-500 dpi to settle single-glyph decisions -- p.222 of Maier 1985 and pp.7, 10 and 17 of 1005.4703v2 -- each named in the defect row it settles. |
| V5 | record | ALL THREE EXPECTATIONS REPRODUCED INDEPENDENTLY. Maier 1985: `pdffonts` lists no fonts at all and `pdftotext` over the whole document returns 6 bytes -- one separator per page, no text layer. This is the expected state, not a stop (rule 9). Hildebrand-Maier 1988: one embedded CID TrueType subset, LOUMNL+TimesNewRomanPSMT, Identity-H, carrying an OCR-derived layer that is corrupt throughout; this session's own dump renders `R^k` as "Rfc", `N` as "TV" and `p_{n+1}-p_n` as "Pn+i ~Pn", all three at the exact places ANN-92 named. Renders were the evidence base and the layer was used only to locate passages. 1005.4703v2 and 1110.6624v1: clean LaTeX-derived layers, usable for pre-comparison. |
| V6 | record | 9 / 6 / 24 / 30 in Section 2.1 line order, matching expectation. Maier's six PDF pages carry printed pages 221-225 on PDF pages 1-5; PDF page 6 is blank, with 0 pixels below intensity 200 out of 3866367. |
| V7 | record | RECOUNT AGREES IN EVERY COLUMN for all four files: lines 397 / 492 / 804 / 497, quoted objects 11 / 31 / 79 / 31, display blocks 30 / 59 / 153 / 68, TRANSCRIPTION-UNSURE 0 / 0 / 0 / 0, [extract note] lines 20 / 20 / 22 / 19. No divergence, so no recount finding entered the defect tables. The full table is Section 5 of the grade record. |

## 3. Grade summary

| extract | verdict | defects |
| --- | --- | --- |
| maier85-shortintervals.md | DEFECTIVE | 1 |
| hildebrandmaier88-gaps.md | CLEAN | 0 |
| freiberg10-strings1.md | DEFECTIVE | 9 |
| freiberg11-strings2.md | DEFECTIVE | 3 |

One CLEAN, three DEFECTIVE, 13 defect rows. By class: (a) transcription
deviation 6, (b) page-reference error 5, (c) untrue or interpretive note claim 1,
(g) untrue FLAGS statement 1. Classes (d) scope violation, (e) untrue header
field and (f) forbidden language are empty across all four extracts.

Every defect row -- file, extract line, source page, class, verbatim is-state,
verbatim should-state, and the finding that establishes it -- is in
`dossier/item-0029-workpapers/extract-grades-G1.md`. That record is the object a
repair session works from; this report does not restate it.

Per Section 4.4 of the dispatch, one HASHES line was appended for the single
CLEAN extract and one for the grade record, in that order. The three DEFECTIVE
extracts got no line.

## 4. Surface statistics

Totals checked across the four extracts, by dispatch surface class:

| class | surface | total checked |
| --- | --- | --- |
| S-a | verbatim-quoted numbered or named objects | 152 (11 / 31 / 79 / 31) |
| S-a | quotation-opening lines carrying quoted prose | 431 (54 / 95 / 193 / 89) |
| S-b | `$$` display blocks | 310 (30 / 59 / 153 / 68) |
| S-c | explicit page references | 289 (42 / 71 / 114 / 62), of which 116 are per-display page labels |
| S-d | [extract note] lines | 81 (20 / 20 / 22 / 19), including 34 structural-map lines and 26 uniformity-ledger items |
| S-e | header fields | 24 (6 per extract) |
| S-f | scope sweeps | 3 FULL completeness sweeps plus 1 PARTIAL boundary check |
| S-g | FLAGS statements | 28 (6 / 8 / 7 / 7) |
| S-h | absence sweeps | 4, one per extract |

The S-f sweeps found no omission in any of the three FULL extracts, and the
PARTIAL boundary of `freiberg11-strings2.md` is exactly honoured: Sections 1-3
are complete, nothing is transcribed from Section 4 beyond its printed heading
quoted as a named reference, and all four factual claims of that extract's
scope-boundary section were verified true against the renders of pp.13, 29 and
30.

The S-h sweeps returned no axis, gate, verdict, NOT-FOUND or grade-state language
in any extract. The single hit worth naming is the ledger identifier inside
`freiberg10-strings1.md`, recorded as defect F1 under class (c) because the same
sentence's substantive failure is that it is not a claim about the source.

## 5. Deviations and surprises

D1. THREE JUDGMENT CALLS ON WHAT THE SURFACE INCLUDES, disclosed with their
reasoning so that a later session can overrule them against the record rather
than re-derive them.

(a) LAYOUT IS NOT GRADED; MATHEMATICAL GROUPING IS. Dispatch S-a enumerates the
character surface as wording, mathematical symbols, sub/superscripts, inequality
directions, summation bounds, congruence signs, primes and accents on variables,
and numbering labels. A Markdown transcription must linearise a printed page, and
the linearisation choices the four extracts make -- a separator standing for a
hard line break in a masthead or address block, a period joining a display
section heading to the paragraph it heads, small capitals rendered as capitals,
italics dropped, and a large brace that groups two separately parenthesised
CONDITION LINES of a multi-line display replaced by horizontal spacing -- change
no character of the wording or of the mathematics and were not graded. Delimiters
that carry mathematical grouping INSIDE a single expression were graded, because
dropping or substituting one changes what the expression says: that is what
defects F2, G1, G2 and G3 are. The line between the two is whether the printed
delimiter separates layout rows or binds operands.

(b) THE SECTION-SIGN FOLDING OF `freiberg11-strings2.md` WAS NOT FIRED. That
extract drops the printed section sign from cross-references such as "[2, 6.2]"
and "See 4", and declares the folding in its FLAGS rather than in its Section 0.
Dispatch S-a says the extract's own declared conventions "(its Section 0)" are
the folding standard and that a folding used but not declared there is a class
(a) defect. The clause reads two ways: as a requirement that conventions be
declared, or as a requirement that they be declared in that section. This session
took the first reading and did not fire. The reason is that the harm the clause
guards against -- a lossy transformation a reader cannot invert, which is the
silently-wrong-corpus failure of rule 26 -- does not occur here: the convention is
stated in the extract, and any reader of the extract can invert the folding. The
other three extracts declare their conventions in Section 0, and
`freiberg10-strings1.md` explicitly points its FLAGS reader back there, so the
house pattern is clear and a repair session may wish to move the sentence anyway.

(c) A FAITHFUL ALPHABET MAPPING THAT IS NOT DECLARED WAS NOT FIRED.
`freiberg11-strings2.md` declares only its calligraphic prime-set convention in
Section 0, then uses a calligraphic H for the set of linear forms and a Fraktur S
for the singular series inside footnote 3. Both render as the source prints them,
so nothing is folded and nothing is lost; this is not a folding pattern and was
not graded as one.

D2. THE HEAVIEST DEFECT CLASS WAS NOT THE ONE THE BUDGET PREDICTED. The dispatch
put the bulk on quotation and display verification and called the notes, maps,
headers and FLAGS "small but every line counts". Of the 13 defect rows, 6 are
transcription deviations and 7 are in exactly that small surface: five
page-reference errors inside structural-map lines and a section heading, one
non-source note claim, one untrue FLAGS statement. Rule 26(1)'s sentence that "a
display-and-quotation grade does not reach the prose glosses; those are where the
item-0022 2d bounces were" is confirmed by this run at better than half the
defect mass.

D3. TWO SOURCE PRINT SLIPS WERE SILENTLY NORMALISED IN ONE EXTRACT. Defects F3
and F4 are places where 1005.4703v2 prints a missing subscript (p.10) and an
unprimed variable (p.17), and `freiberg10-strings1.md` supplies the intended form
without recording the slip. This matters more than its size suggests: the same
extract transcribes four OTHER print slips of the same source exactly as printed
and lists them in FLAGS, so a consumer reading the extract would reasonably infer
that the two normalised sites are what the source prints. Both were settled on
300-dpi and 500-dpi region re-renders rather than on the 200-dpi page rasters,
because the missing subscript is a single glyph.

D4. THE ONE DEFECT IN `maier85-shortintervals.md` IS SELF-CONTRADICTED BY THE
SAME BULLET. The FLAGS statement that the string "Gallagher" does not appear in
the body sits two lines below that bullet's own phrase "Lemma 2 (Gallagher)", and
the extract transcribes the printed heading `LEMMA 2 (Gallagher).` at line 133.
Recorded as class (g) rather than class (c) because the location is FLAGS.

D5. EVERY DIVERGENCE THE FOUR EXTRACTS FLAG AGAINST THE DISPATCH ATTENTION LISTS
SURVIVES A FRESH READING. ANN-92 left that question open. All of them were
re-checked against this session's renders: the Hildebrand-Maier display sequence
does run (1)-(21) plus (*), (**), (6)' and (7)'; its good-modulus condition is
restricted to nonprincipal characters where Maier 1985 says all characters; p.2
does print "Erdos and Ricci [8]" against a p.9 entry [8] of G. Ricci alone;
1005.4703v2 does number (5.1)-(5.18) and (5.24)-(5.32) beyond the named range and
does print its singular-series display before rather than inside Lemma 4.1;
1110.6624v1 prints no proof of Lemma 3.3 inside the declared scope and prints the
two comparison displays unnumbered. None was overturned.

D6. NO FIDELITY DOUBT ABOUT ANY OF THE FIVE OLD HASHED item-0022 EXTRACTS AROSE
(r29G.6 not triggered). None was opened; none needed to be.

## 6. STOP conditions

All ten reported by name, none fired.

- r29G.1 validity failure (P1 content-path delta, P2, P3, P4, P5): NOT FIRED.
  HEAD equalled the pin with no delta at all, item-0029 was ratified, ANN-92
  existed and validated, the four extracts were clean and the Shiu extract
  untracked, and no HASHES line carried any of the five identifiers.
- r29G.2 source-hash mismatch on any of the four (V2): NOT FIRED. All four
  matched, checked before any source was opened.
- r29G.3 freshness breach or reuse of Session E renders, dumps or the withheld
  shiu00-strings.md: NOT FIRED. The scratchpad was empty at session start; all 69
  renders and all text-layer dumps used here were produced in this session from
  the anchored bytes; the withheld extract was never opened.
- r29G.4 scope pressure: NOT FIRED. No step required editing an extract, opening
  the Shiu source or extract, network access, a fifth source, or a Lean edit. The
  one-character defects of F3 and F4 were recorded, not repaired.
- r29G.5 envelope breach: NOT FIRED. extract-grades-G1.md is 551 lines inside
  100-800; this report is inside 120-400. Neither was padded or trimmed to fit.
- r29G.6 fidelity doubt about an old hashed item-0022 extract: NOT FIRED. None
  arose; see D6.
- r29G.7 consumption drift: NOT FIRED. No extract content was used for item-0029
  substance. No axis, no positive-proportion gate, no named finding, and no
  comparison to a project object appears in the grade record or in this report.
- r29G.8 ANN sequence collision: NOT FIRED. `ledger/annotations/ANN-20260802-93.yaml`
  did not exist at session start; the computed next number is 93.
- r29G.9 close-gate failure: NOT FIRED. All Section 8 gates are green at close;
  see Section 1.
- r29G.10 instruction unsatisfiable or internally divergent: NOT FIRED. No
  divergence between the kickoff and the scopes and methods booked in ANN-92 was
  found. The kickoff's V6 expectation of 9 / 6 / 24 / 30 is the four-source
  restriction of ANN-92's five-source 9 / 6 / 15 / 24 / 30 and agrees with it.

## 7. Budget reconciliation

| task | dispatch estimate | actual |
| --- | --- | --- |
| V-G table, gates at start, 69-page render pass | mechanical | as estimated; one pass, no re-runs needed. The render pass took one `pdftoppm` invocation per source. |
| completeness sweeps (S-f) first per source | do these FIRST; omissions are the costliest defect class to find late | done first per source and returned nothing in all four cases. The advice held in the sense that it cost little and closed the costliest class early; class (d) is empty. |
| quotation and display verification (S-a to S-c) | the bulk: ~152 quoted objects, 310 display blocks, ~2190 extract lines against 69 rendered pages | as estimated in volume and it was the bulk of the session. Six defects. Four page regions had to be re-rendered at 300-500 dpi for single-glyph decisions, which the dispatch anticipated as a legibility allowance rather than a typography one. |
| notes, maps, headers, FLAGS (S-d, S-e, S-g, S-h) | ~81 note lines plus four structural maps; small but every line counts | the phrase understated it: seven of thirteen defects are here. Verifying a structural-map page range costs a page lookup each, and five of those lookups came back wrong. |
| record, report, ANN, HANDOVER, close gates | mechanical | as estimated. |

All four extracts were graded to a verdict; none was left UNGRADED. No proof
work, no computation beyond hashing, rendering, pixel counting and linting; no
Lean, no network. The only shortfall to name is not a shortfall of the work: the
Shiu extract could not be graded because it is not in the tree, which ANN-92
already booked and which this session was directed to leave alone.
