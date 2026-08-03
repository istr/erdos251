# item-0029 EXTRACT FIDELITY GRADE G3 (terminal, second cycle)

## 0. Session identity, pin, method, V-G3 outcomes

Lane: EXECUTOR (local workstation, Claude Code). Executor model string:
claude-fable-5. Web OFF, cloud OFF for the entire session. Date of run:
2026-08-03. This session is a FRESH executor session in the rule-26(3) sense:
it is none of the Sessions E, G, R, G2 or R2, inherits no context, notes,
renders or text-layer dumps from any of them, and did not read the withheld
executor-local `shiu00-strings.md`. Everything verified here was produced
inside this session from the anchored bytes.

Pin: this session pinned to the Section 0 pin of its ephemeral dispatch, which
equalled `git rev-parse HEAD` exactly; no rule-18 bookkeeping delta arose.

METHOD AFFIRMATION (dispatch Section 4.1, affirmed as executed).
`maier85-shortintervals.md` was graded against this session's own renders
only; that source has no text layer to use. `freiberg10-strings1.md` and
`freiberg11-strings2.md` were pre-compared against the text layer, and every
quotation and every display was then verified against the 200-dpi render of
the cited page before its row was closed. All 60 page rasters were produced
inside this session from the anchored bytes. Four page regions were
re-rendered at 400-500 dpi to settle single-glyph, delimiter and subscript
decisions -- the p.222 good-modulus region and the p.222 Lemma-2
constants-sentence region of Maier 1985 at 400 dpi; the (6.4) region of
1005.4703v2 p.21 at 500 dpi; and the (3.23) head region of 1110.6624v1 p.12
at 500 dpi -- and each is named in the section it settles.

This session repaired nothing, edited no extract, adjudicated nothing, and
consumed no extract content for item-0029 substance. The Shiu 2000 source and
the withheld Shiu extract were not opened, not read, not graded and not
hashed. `hildebrandmaier88-gaps.md` was not re-graded and its content was not
read.

The grade is over the FULL surface of each gradee. The eighteen sites
repaired across both cycles -- the fourteen G1 positions applied by Session R
and the four G2 positions applied by Session R2 -- were checked as ordinary
surface, neither privileged nor skipped, and every one is correct as applied.

The six governing readings fixed by the dispatch Frame (report-G Section 5 D1
a-c and report-G2 Section 5 D1 a-c) were consumed as fixed, not re-litigated;
no verdict below is founded on rejecting any of them, and none needed to be.

V-G3 outcomes:

| row | class | outcome |
| --- | --- | --- |
| V1 | gate | HOLDS. Fresh executor session; none of Sessions E, G, R, G2 or R2; no artefact, render, dump or note of any of them was present or read; the session scratchpad was empty at start. The withheld `shiu00-strings.md` was never opened, and neither was the Shiu source. Operator freshness confirmed at dispatch. |
| V2 | gate | THREE MATCHES. sha256 of each of the three local source PDFs equals its Section 2.1 anchor line, verified before any source was opened. The Hildebrand-Maier source was not needed; anchor line 105 (Shiu) stayed out of scope. |
| V3 | gate | HOLD. P1: HEAD equalled the pin, empty diff, no delta. P2: `status: ratified`. P3: ANN-20260802-96.yaml present, ledger validate passed at 96 entries. P4: the three gradees clean under `git status --short`, all three hashed grade-chain artifacts verify against their payloads/HASHES.txt lines. P5: no HASHES line carries any of the three gradee paths or either output path, and neither output file existed. |
| V4 | gate | 60 PAGES ON DISK before grading started: 6 + 24 + 30, rendered in this session at 200 dpi from the anchored bytes with `pdftoppm`, one invocation per source. Four region re-renders at 400-500 dpi, named above. |
| V5 | record | REPRODUCED, all three as expected. Maier 1985: `pdffonts` lists no fonts and `pdftotext` over the whole document returns 6 bytes, one form feed per page -- no text layer; expected state, not a stop (rule 9). 1005.4703v2 and 1110.6624v1: clean LaTeX-derived layers, usable for pre-comparison. |
| V6 | record | RECOUNT AGREES WITH THE REPORT-R2 SECTION 4 BASELINE IN EVERY COLUMN. Full table in Section 4 below. Multi-line closers 2 / 0 / 0 and surplus delimiter lines 3 / 1 / 1 exactly per the corrected report-G2 D3 reading: maier85 lines 15, 86 and 151 (the Section 0 conventions note plus the two closers), and in each Freiberg file only the line-15 conventions note. |

---

## 1. maier85-shortintervals.md

Source: Maier-Primes-in-short-intervals.pdf, printed pages 221-225 (PDF pages
1-5), PDF page 6 blank (0 pixels below intensity 200 out of 3866367, minimum
254). Declared scope FULL.

Surface counts checked: 11 verbatim-quoted numbered or named objects (THEOREM;
LEMMA 1; LEMMA 2 (Gallagher); LEMMA 3 (Buchstab); LEMMA 4; displays (1.1),
(2.1), (2.2), (2.3), (2.4), (3.1)); 30 `$$` display blocks; 43 explicit page
references across 17 section headings, 6 uniformity-ledger items and 9
structural-map lines; 20 [extract note] lines; 6 header fields; 6 FLAGS
bullets; 54 quotation-opening lines.

Scope sweep (S-f, FULL): PASSED. Every numbered or named object the source
prints appears in the extract -- the Theorem with all three assertions, Lemmas
1-4, the numbered displays (1.1), (2.1)-(2.4) and (3.1), every unnumbered
display on pp.221-225, the good-modulus definition, the sieve-function
definitions, the ACKNOWLEDGMENT, references 1-10 and the address block. No
omission.

Header fields (S-e): all six true. The absolute source path resolves to the
anchored file on this workstation; the sha256 equals the anchor line; the
bibliographic identity matches the journal line printed on p.221 and the
printed pagination 221-225; the declared method and scope are as booked. No
grade-state, no unresolvable deixis.

Absence checks (S-h): PASSED. No axis, gate, verdict, NOT-FOUND, grade-state
or project-object language. "Uniformity ledger" is a section title using the
common noun.

Displays and quotations (S-a, S-b): all 30 display blocks and all quoted prose
verified character-exact against the renders of pp.221-225. The p.222
good-modulus region was re-rendered at 400 dpi: the source does print the
vertical bar where the closing parenthesis is expected and does print the
outer bars of the displayed zero-free condition, exactly as the extract's note
states and transcribes. One legibility decision was settled at 400 dpi: the
faint mark between "Lemma" and "1" in the p.222 constants sentence "depend
only on C in Lemma 1" resolves as a scan speckle above the baseline, not a
printed character, so the extract's "Lemma 1" is exact.

Page references (S-c): all 43 correct, the repaired M2 range form
"(pp.223-224)" included. On this session's renders p.223 ends mid-sentence
with "In the sequel we assume that z -> infinity through a set" and p.224
opens with the good-modulus restriction and the z >= e^{cD} bound, so the
cited assumption straddles the break exactly as the range states.

Notes, map and uniformity ledger (S-d): all 6 uniformity-ledger items and all
9 structural-map lines are true and page-anchored. The conventions notes are
true: no text layer and no embedded fonts (`pdffonts` empty, reproduced this
session), six PDF pages with printed 221-225 on PDF 1-5 and a blank sixth
(pixel-counted this session), page citations by printed page number.

FLAGS (S-g): all 6 statements true. The repaired divergence bullet was checked
in both directions on the renders: the bracketed citation [3] appears nowhere
in the body of pp.221-225 and only as reference-list entry 3 on p.225, while
the name Gallagher is printed in the heading `LEMMA 2 (Gallagher).` in the
body of p.222. The strict-inequality primorial bullet is true: p.222 prints
P(z) as the product over p < z.

zero defects

VERDICT: CLEAN

---

## 2. freiberg10-strings1.md

Source: 1005.4703v2.pdf, printed pages 1-24 coinciding with the PDF pages.
Declared scope FULL.

Surface counts checked: 79 verbatim-quoted numbered or named objects (Theorem
1.1; Lemma 2.1; Propositions 2.2 and 2.3; Lemmas 4.1 and 4.2; Lemmas 5.1-5.5;
displays (2.1)-(2.12), (3.1)-(3.2), (4.1)-(4.14), (5.1)-(5.32), (6.1)-(6.8));
153 `$$` display blocks; 65 display page labels plus 116 explicit page
references across 13 section headings, 7 uniformity-ledger items and 9
structural-map lines; 22 [extract note] lines; 6 header fields; 7 FLAGS
bullets; 193 quotation-opening lines.

Scope sweep (S-f, FULL): PASSED. All 68 numbered displays are present, the
eighteen (5.1)-(5.18) and the nine (5.24)-(5.32) included; the eleven numbered
or named statements are present; Sections 1-8 and both reference pages are
covered, through the address block and e-mail line on p.24. No omission.

Header fields (S-e): all six true. No grade-state, no unresolvable deixis.

Absence checks (S-h): PASSED. No axis, gate, verdict, NOT-FOUND, grade-state
or project-object language anywhere. The FLAGS divergence bullets that name
the extraction brief are conformant under fixed reading 6; every source-side
claim they carry was verified true this session.

Page references (S-c): all 65 display page labels and all 116 explicit page
references correct, the five repaired at G1 included and re-confirmed --
Section 2 does run pp.2-4 with (2.12) printed on p.4; the first Section 4
invocation of (2.1) sits at the G(0,0;Omega) evaluation on p.8 and the second
at G(0,0;Omega^{+}) on p.11; the proof of Lemma 4.1 runs pp.6-8 with its
closing box on p.8; and the proof of Proposition 2.3, with its "If p_0 != 1
then by (2.1)" invocation, is printed on p.17.

Displays and quotations (S-a, S-b): all 153 display blocks and all quoted
prose verified character-exact against the renders of pp.1-24. The two sites
repaired across the cycles inside this surface are exact: the p.7 brace pair
of the log-of-first-product display encloses the two separately parenthesised
series exactly as printed (F2), and the third summation of (6.4) on p.21
carries both printed subscript rows -- the index row above the condition row
-- confirmed on a 500-dpi re-render of the region (F10). The six recorded
print slips of the source are transcribed as printed and none is silently
normalised: mu(d_1)mu(d_1) on p.8; the repeated 1/p^{s_1} on p.11; the
unsubscripted first factor of the summation condition on p.10; the unprimed
congruence variable in the third sum on p.17; the fourth-moment sums of (6.2)
and (6.3) printed without the subscript R on pp.20-21 while (6.7) prints it;
and "Cauchy-Schwartz" at the lead-in to (6.7) on p.22.

Notes, map and uniformity ledger (S-d): all 9 structural-map lines and all 7
uniformity-ledger items are true and page-anchored, the four repaired
locators included. The repaired alphabets note is true in every clause: the
calligraphic S first appears at Lemma 5.2 on p.12 inside Section 5 and again
on p.18, the calligraphic T and E are the starred error and main terms of
(4.12) on pp.9-11 inside Section 4, and a page sweep of pp.6-11 -- the whole
of Section 4, which ends on p.11 above the Section 5 heading -- finds no
calligraphic S anywhere. The two print-slip notes inside the body are true of
the renders.

FLAGS (S-g): all 7 statements true, the six-item print-slip list checked item
by item against the renders as above, and both attention-list divergence
bullets carrying only claims the renders confirm.

zero defects

VERDICT: CLEAN

---

## 3. freiberg11-strings2.md

Source: 1110.6624v1.pdf, printed pages 1-30 coinciding with the PDF pages.
Declared scope PARTIAL: Sections 1-3 in full; Section 4's Selberg-Delange
proof by named reference only, not transcribed.

Surface counts checked: 31 verbatim-quoted numbered or named objects (Theorem
1.1; Theorem 3.1 (Siegel-Walfisz); Lemmas 3.2, 3.3 and 3.4; displays
(1.1)-(1.2) and (3.1)-(3.24)); 69 `$$` display blocks; 26 display page labels
plus 62 explicit page references across 11 section headings, 7
uniformity-ledger items and 6 structural-map lines; 20 [extract note] lines;
6 header fields; 7 FLAGS bullets; 89 quotation-opening lines.

Scope boundary (S-f, PARTIAL): PASSED, and the boundary is exactly honoured.
Sections 1-3 are complete: the abstract, the whole of Sections 1 and 2
including all three footnotes at the feet of pp.2-3, the statements and
printed proofs of Theorem 3.1 and Lemmas 3.2-3.4 as the source gives them
(Lemma 3.3's printed proof line inside the scope being "Proof. See 4."), the
construction (3.1)-(3.6), the proof of Theorem 1.1 on p.7, and the full
printed proof of Lemma 3.4 in both parts, ending with the closing box and the
printed numerical step on p.13. All 26 numbered displays are present. Nothing
is transcribed from Section 4 beyond its printed heading, quoted as a named
reference in the scope-boundary section. The four factual claims of that
section are verified true against this session's renders: Section 4 headed
"4. Proof of Lemmas 3.2 and 3.3" begins on p.13 and ends on p.29, where the
proof of Lemma 3.3 closes; Section 5 headed "5. Acknowledgements" is on p.29;
the reference list occupies pp.29-30; and the address block "Institutionen
for matematik, KTH, 100 44 Stockholm, Sweden" with an e-mail address closes
p.30. Pages 14-28 carry no section heading, so no further section intervenes.

Header fields (S-e): all six true, including the declared PARTIAL scope
string, which matches what the extract does. No grade-state, no unresolvable
deixis.

Absence checks (S-h): PASSED. No axis, gate, verdict, NOT-FOUND, grade-state
or project-object language anywhere.

Page references (S-c): all 26 display page labels and all 11 section-heading
page spans correct.

Notes, map and uniformity ledger (S-d): all 6 structural-map lines and all 7
uniformity-ledger items are true and page-anchored, the p.13 location of the
closing numerical step included. The five Section 0 conventions notes are
true; the section-sign folding declaration holds at both its worked examples
and at every further printed occurrence checked ("[5, 1, Question 3]" on p.1,
"[2, 7]" and "[2, 2]" on p.2, "[2, 6.2]" and "[2, 4, 7]" on p.3, "in 4" on
p.5 and "See 4." on p.5), and the folding is invertible by the rule it
states. The footnote note is true: the three footnotes of Section 2 are
printed at the foot of pp.2-3.

FLAGS (S-g): all 7 statements true, including the V8 and V9 echoes, the three
divergence statements -- no printed proof of Lemma 3.3 inside the scope, the
displays (3.7)-(3.24) transcribed under the object-coverage rule, and the two
unnumbered epsilon(X) comparison displays printed immediately after Theorem
1.1 on p.2 with the a = +/-1 case split, attributed to Shiu -- and the
Section 0 pointer, which is conformant under the governing reading.

Displays and quotations (S-a, S-b): all 69 display blocks and all quoted
prose verified character-exact against the renders of pp.1-13. The four
repaired sites inside this surface are exact: the three p.11
parenthesisations restored at G1 (the outer pair on the 1+o(1) logarithm
identity, the nested pairs in the beta display, and the parenthesised
numerator argument of (3.22)) each reproduce the printed form, and the (3.23)
chain on p.12 carries the printed triple-sum first member -- outer index
restricted to one half log t(H), middle sum over p in I_l congruent to a,
inner sum with its three printed subscript rows wrapped into two `\substack`
rows per fixed reading 5 -- confirmed on a 500-dpi re-render of the head of
p.12, with the following display line byte-unchanged (G4).

zero defects

VERDICT: CLEAN

---

## 4. Recount against the report-R2 Section 4 baseline (V6)

| file | lines R2 / recount | objects R2 / recount | `$$` R2 / recount | UNSURE R2 / recount | notes R2 / recount | FLAGS R2 / recount |
| --- | --- | --- | --- | --- | --- | --- |
| maier85-shortintervals.md | 398 / 398 | 11 / 11 | 30 / 30 | 0 / 0 | 20 / 20 | 6 / 6 |
| freiberg10-strings1.md | 807 / 807 | 79 / 79 | 153 / 153 | 0 / 0 | 22 / 22 | 7 / 7 |
| freiberg11-strings2.md | 500 / 500 | 31 / 31 | 69 / 69 | 0 / 0 | 20 / 20 | 7 / 7 |

Every column agrees; no recount divergence entered the grade. The `$$` column
counts lines opening with the display delimiter, per the G1 Section 5
methodology; the TRANSCRIPTION-UNSURE column counts unsure markers, the
single literal occurrence per file being the FLAGS line that reports the
count. Multi-line-display closers, per the corrected report-G2 D3 reading:
2 / 0 / 0 (maier85 lines 86 and 151; neither Freiberg file contains a
multi-line display block). Surplus delimiter lines (delimiter not at line
start): 3 / 1 / 1, the Section 0 conventions note at line 15 in each file
plus the two maier85 closers.

---

## 5. Summary verdicts

```
maier85-shortintervals.md      VERDICT: CLEAN
freiberg10-strings1.md         VERDICT: CLEAN
freiberg11-strings2.md         VERDICT: CLEAN
```

Totals: 3 CLEAN, 0 DEFECTIVE, 0 defect rows. All seven classes (a)
transcription deviation, (b) page-reference error, (c) untrue or interpretive
note claim, (d) scope violation, (e) untrue header field, (f) forbidden
language and (g) untrue FLAGS statement are empty across all three extracts.

END OF GRADE RECORD G3
