# item-0029 EXTRACT FIDELITY GRADE G2 (terminal)

## 0. Session identity, pin, method, V-G2 outcomes

Lane: EXECUTOR (local workstation, Claude Code). Executor model string:
claude-opus-5. Web OFF, cloud OFF for the entire session. Date of run:
2026-08-02. This session is a FRESH executor session in the rule-26(3) sense:
it is none of the Sessions E, G or R, inherits no context, notes, renders or
text-layer dumps from any of them, and did not read the withheld
executor-local `shiu00-strings.md`. Everything verified here was produced
inside this session from the anchored bytes.

Pin: this session pinned to the Section 0 pin of its ephemeral dispatch, which
equalled `git rev-parse HEAD` exactly; no rule-18 bookkeeping delta arose.

METHOD AFFIRMATION (dispatch Section 4.1, affirmed as executed).
`maier85-shortintervals.md` was graded against this session's own renders only;
that source has no text layer to use. `freiberg10-strings1.md` and
`freiberg11-strings2.md` were pre-compared against the text layer, and every
quotation and every display was then verified against the 200-dpi render of the
cited page before its row was closed. All 60 page rasters were produced inside
this session from the anchored bytes. Nine page regions were re-rendered at
400-500 dpi to settle single-glyph, delimiter and subscript decisions -- p.222
and the p.223/p.224 break of Maier 1985; pp.10, 17 and 21 of 1005.4703v2; and
p.11 (three regions) and p.12 of 1110.6624v1 -- and each is named in the row it
settles.

This session repaired nothing, edited no extract, adjudicated nothing, and
consumed no extract content for item-0029 substance. The Shiu 2000 source and
the withheld Shiu extract were not opened, not read, not graded and not hashed.
`hildebrandmaier88-gaps.md` was not re-graded and its content was not read.

The grade is over the FULL surface of each gradee, not merely the fourteen
sites Session R repaired; those fourteen were checked as ordinary surface and
each was found correctly applied.

V-G2 outcomes:

| row | class | outcome |
| --- | --- | --- |
| V1 | gate | HOLDS. Fresh executor session; not Session E, G or R; no artefact, render, dump or note of any of them was present or read; the session scratchpad was empty at start (0 files). |
| V2 | gate | THREE MATCHES. sha256 of each of the three local source PDFs equals its Section 2.1 anchor line, verified before any source was opened. |
| V3 | gate | HOLD. P1: HEAD equalled the pin, empty diff, no delta. P2: `status: ratified`. P3: ANN-20260802-94.yaml present, ledger validate passed. P4: the three gradees clean under `git status --short`, both hashed session-G artifacts verify against HASHES lines 108 and 109. P5: no HASHES line carries any of the five identifiers, and neither output file existed. |
| V4 | gate | 60 PAGES ON DISK before grading started: 6 + 24 + 30, rendered in this session at 200 dpi from the anchored bytes with `pdftoppm`. |
| V5 | record | REPRODUCED, all three as expected. Maier 1985: `pdffonts` lists no fonts and `pdftotext` over the whole document returns 6 bytes, one form feed per page, i.e. no text layer; expected state, not a stop (rule 9). 1005.4703v2 and 1110.6624v1: clean LaTeX-derived Computer Modern layers, usable for pre-comparison. |
| V6 | record | RECOUNT AGREES WITH THE REPORT-R BASELINE IN EVERY COLUMN. Full table in Section 4 below. One refinement of the baseline's PROSE, not of its numbers, is recorded there. |

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

Absence checks (S-h): PASSED. No axis, gate, verdict, NOT-FOUND, grade-state or
project-object language. "Uniformity ledger" is a section title using the
common noun.

Displays and quotations (S-a, S-b): all 30 display blocks and all quoted prose
verified character-exact against the renders of pp.221-225. The p.222
good-modulus region was re-rendered at 500 dpi: the source does print
`L(s,chi|` with a vertical bar where the closing parenthesis is expected, and
does print the displayed zero-free condition with the outer bars, exactly as
the extract's own note at line 107 states.

FLAGS (S-g): all 6 statements true, including the repaired divergence bullet.
The bracketed citation [3] appears nowhere in the body of pp.221-225 and only
as reference-list entry 3 on p.225, while `LEMMA 2 (Gallagher).` is printed in
the body of p.222; the repaired sentence states exactly that.

Notes, map and uniformity ledger (S-d): all 9 structural-map lines are true and
page-anchored, as are five of the six uniformity-ledger items. The sixth is
defective.

Page references (S-c): 42 of the 43 correct. The one exception is the same
site, recorded below.

### Defect table

| # | file | extract line | source page | class |
| --- | --- | --- | --- | --- |
| M2 | maier85-shortintervals.md | 345-348 | 223 | (b) page-reference error |

M2 is-state, verbatim:

```
- [extract note] The variable z is not free: the proof assumes
  $`z\to\infty`$ through the set of z for which $`P(z)`$ is a good
  modulus and $`z\ge e^{cD}`$ (p.223), and Lemma 1 asserts only that such
  z exist arbitrarily large (p.222).
```

M2 finding: the cited assumption straddles the p.223/p.224 break. Page 223 ends
mid-sentence with "In the sequel we assume that z -> infinity through a set";
page 224 opens with "of z for which P(z) is a good modulus in the sense of
Lemma 1 and that z >= e^{cD}, where c is the constant in Lemma 2." Both
distinguishing components of the cited claim -- the restriction to good moduli
and the bound on z -- are printed on p.224 and on no part of p.223, which
carries only Lemma 4, its proof, and that opening clause. Confirmed on 400-dpi
re-renders of the foot of p.223 and the head of p.224. The parenthetical is a
fact locator, not a section pointer: the second parenthetical of the same
sentence, "(p.222)", locates Lemma 1's statement, which is entirely on p.222,
and uniformity-ledger item 3 names its section in words ("In Section 3") and
still gives the page of the fact. The extract itself ranges this passage
correctly elsewhere -- its section heading at line 231 reads "(pp.223-224,
verbatim)" -- and structural-map line 375 uses the range form "(pp.224-225)"
for a two-page object, so the single page number here is a slip rather than a
declared convention. Consequence for a consumer: rule 26(4) makes this extract
the primary anchor for the analysis lane, which would cite p.223 for material
printed on p.224.

M2 should-state, verbatim:

```
- [extract note] The variable z is not free: the proof assumes
  $`z\to\infty`$ through the set of z for which $`P(z)`$ is a good
  modulus and $`z\ge e^{cD}`$ (pp.223-224), and Lemma 1 asserts only that
  such z exist arbitrarily large (p.222).
```

VERDICT: DEFECTIVE (1 defect)

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
covered. No omission.

Header fields (S-e): all six true.

Absence checks (S-h): PASSED. The ledger identifier that carried G1's defect F1
is gone; nothing else in the file names a project object, an axis, a gate, a
verdict, a NOT-FOUND or a grade-state.

Page references (S-c): all 65 display page labels and all 116 explicit page
references correct, the five repaired at G1 included. Section 4 does run
pp.6-11 and the proof of Lemma 5.5 does occupy pp.17-20, so the two ranges
report-R O1 flagged as unverified are TRUE as printed: p.11 carries the end of
Section 4 and the "5. Proof of Proposition 2.3" heading, and p.20 carries the
closing box of the Lemma 5.5 proof above the "6. A lower bound" heading.

FLAGS (S-g): all 7 statements true. The six-item print-slip list was checked
item by item against the renders and every item holds: `mu(d_1)mu(d_1)` on p.8;
`1/p^{s_1} + 1/p^{s_1}` on p.11; the fourth-moment sums printed without the
subscript R in (6.2) on p.20 and (6.3) on p.21; "Cauchy-Schwartz" at the
lead-in to (6.7) on p.22; the unsubscripted first factor of the summation
condition on p.10, confirmed at 500 dpi; and the unprimed variable in the third
summation condition on p.17, confirmed at 500 dpi. Report-R O2's list ORDER is
layout under the governing reading and was not graded.

Displays and quotations (S-a, S-b): 152 of the 153 display blocks and all
quoted prose verified character-exact against the renders of pp.1-24. The three
displays repaired at G1 -- the brace pair on p.7, the unsubscripted factor on
p.10 and the unprimed variable on p.17 -- now reproduce the printed forms
exactly. One display deviates (F10).

Notes, map and uniformity ledger (S-d): all 9 structural-map lines and all 7
uniformity-ledger items are true and page-anchored. Of the six conventions and
observation notes, five are true; one carries a false section attribution
(F11).

### Defect table

| # | file | extract line | source page | class |
| --- | --- | --- | --- | --- |
| F10 | freiberg10-strings1.md | 632 | 21 | (a) transcription deviation |
| F11 | freiberg10-strings1.md | 20-25 | 12 | (c) untrue or interpretive note claim |

F10 is-state, verbatim:

```
$$\sum_{\substack{d_1,\ldots,d_4\le R\cr\text{squarefree}}}\frac{\lvert\Omega([d_1,\ldots,d_4])\rvert}{[d_1,\ldots,d_4]}\le\sum_{D\le R^{4}}\frac{\mu^{2}(D)k^{\omega(D)}}{D}\sum_{[d_1,\ldots,d_4]=D}1=\sum_{D\le R^{4}}\frac{\mu^{2}(D)(15k)^{\omega(D)}}{D}\le\prod_{p\le R^{4}}\left(1+\frac{15k}{p}\right)\ll(\log{R^{4}})^{15k}.$$
```

F10 finding: in display (6.4) on p.21 the third summation carries a TWO-ROW
subscript -- the index row "d_1,...,d_4" above the condition row
"[d_1,...,d_4]=D". The extract prints the condition row only, dropping the
printed index row. Confirmed on a 500-dpi re-render of the p.21 region, where
both rows are unambiguous. This is not a layout reflow: a whole printed row of
a summation bound is absent, and S-a names summation bounds explicitly. The
same extract reproduces two-row subscripts with `\substack` throughout,
including twice inside the immediately preceding display (6.3) at lines 623-625,
and it correctly prints a ONE-row subscript at line 326 where the analogous sum
on p.10 is printed with one row -- so the extract's own standard is to mirror
the printed rows, and this site departs from it.

F10 should-state, verbatim:

```
$$\sum_{\substack{d_1,\ldots,d_4\le R\cr\text{squarefree}}}\frac{\lvert\Omega([d_1,\ldots,d_4])\rvert}{[d_1,\ldots,d_4]}\le\sum_{D\le R^{4}}\frac{\mu^{2}(D)k^{\omega(D)}}{D}\sum_{\substack{d_1,\ldots,d_4\cr[d_1,\ldots,d_4]=D}}1=\sum_{D\le R^{4}}\frac{\mu^{2}(D)(15k)^{\omega(D)}}{D}\le\prod_{p\le R^{4}}\left(1+\frac{15k}{p}\right)\ll(\log{R^{4}})^{15k}.$$
```

F11 is-state, verbatim:

```
[extract note] The source uses several distinguished alphabets: a calligraphic H for the
set of linear forms, transcribed $`\mathcal{H}`$; a calligraphic L for the weighted sum,
transcribed $`\mathcal{L}`$; a calligraphic P for the prime set of Section 5,
transcribed $`\mathcal{P}`$; calligraphic S, T and E in Section 4, transcribed
$`\mathcal{S}`$, $`\mathcal{T}`$, $`\mathcal{E}`$; and a Fraktur S for the singular
series, transcribed $`\mathfrak{S}`$.
```

F11 finding: the calligraphic S is not used in Section 4. It first appears in
Lemma 5.2 on p.12, "Let S(x) denote the set of positive integers which are <= x
and composed only of primes p == 1 mod q", and again on p.18 in the proof of
Lemma 5.5; both sites are inside Section 5. Section 4 occupies pp.6-11 and
prints no calligraphic S anywhere on those six pages: its distinguished letters
are the calligraphic H, the calligraphic T and E of the p.9-10 error and main
terms, and the Fraktur S of the singular series. The extract's own
transcription confirms the reading -- its four occurrences of `\mathcal{S}` are
at lines 385, 388, 553 and 558, all inside the Section 5 material, and none in
the Section 4 material at lines 195-369. The claims about the calligraphic H,
the calligraphic L, the calligraphic P, the calligraphic T and E and the
Fraktur S are all true; only the section attribution of the S is false, and it
is false in a note whose neighbouring clause ("the prime set of Section 5")
shows the note is meant to be section-specific.

F11 should-state, verbatim:

```
[extract note] The source uses several distinguished alphabets: a calligraphic H for the
set of linear forms, transcribed $`\mathcal{H}`$; a calligraphic L for the weighted sum,
transcribed $`\mathcal{L}`$; a calligraphic P for the prime set of Section 5,
transcribed $`\mathcal{P}`$; a calligraphic S in Section 5 and calligraphic T and E in
Section 4, transcribed
$`\mathcal{S}`$, $`\mathcal{T}`$, $`\mathcal{E}`$; and a Fraktur S for the singular
series, transcribed $`\mathfrak{S}`$.
```

VERDICT: DEFECTIVE (2 defects)

---

## 3. freiberg11-strings2.md

Source: 1110.6624v1.pdf, printed pages 1-30 coinciding with the PDF pages.
Declared scope PARTIAL: Sections 1-3 in full; Section 4's Selberg-Delange proof
by named reference only, not transcribed.

Surface counts checked: 31 verbatim-quoted numbered or named objects (Theorem
1.1; Theorem 3.1 (Siegel-Walfisz); Lemmas 3.2, 3.3 and 3.4; displays
(1.1)-(1.2) and (3.1)-(3.24)); 68 `$$` display blocks; 26 display page labels
plus 62 explicit page references across 11 section headings, 7
uniformity-ledger items and 6 structural-map lines; 20 [extract note] lines; 6
header fields; 7 FLAGS bullets; 89 quotation-opening lines.

Scope boundary (S-f, PARTIAL): PASSED, and the boundary is exactly honoured.
Sections 1-3 are complete: the abstract, the whole of Sections 1 and 2
including all three footnotes, the statements and printed proofs of Theorem 3.1
and Lemmas 3.2-3.4 as the source gives them, the construction (3.1)-(3.6), the
proof of Theorem 1.1, and the full printed proof of Lemma 3.4 in both parts,
ending with the closing box on p.13. All 26 numbered displays are present.
Nothing is transcribed from Section 4 beyond its printed heading, quoted as a
named reference in the scope-boundary section. The four factual claims of that
section are verified true against the renders: Section 4 headed "4. Proof of
Lemmas 3.2 and 3.3" begins on p.13 and ends on p.29, where the proof of Lemma
3.3 closes; Section 5 headed "5. Acknowledgements" is on p.29; the reference
list occupies pp.29-30; and the address block "Institutionen for matematik,
KTH, 100 44 Stockholm, Sweden" with an e-mail address closes p.30. Pages 14-28
carry no section heading, so no further section intervenes.

Header fields (S-e): all six true, including the declared PARTIAL scope string,
which matches what the extract does.

Absence checks (S-h): PASSED. No axis, gate, verdict, NOT-FOUND, grade-state or
project-object language anywhere.

Page references (S-c): all 26 display page labels and all 11 section-heading
page spans correct, "(pp.4-7)" for the statements, "(p.7)" for the proof of
Theorem 1.1 and "(pp.7-13)" for the proof of Lemma 3.4 included.

Notes, map and uniformity ledger (S-d): all 6 structural-map lines and all 7
uniformity-ledger items are true and page-anchored, the two-page ranges
"(pp.7-9)" and "(pp.9-13)" for parts (a) and (b) of the Lemma 3.4 proof
included, and the p.13 location of the closing numerical step. The footnote
note is true: the three footnotes of Section 2 are printed at the foot of
pp.2-3. The five Section 0 conventions notes are true, the section-sign
declaration moved there by position R-A included: the source does print a
section sign immediately before the section number in the cross-references
rendered by the extract as "[5, 1, Question 3]" on p.1, "[2, 7]" and "[2, 2]"
on p.2, "[2, 6.2]" and "[2, 4, 7]" on p.3, and "See 4" on p.5, so both worked
examples the declaration gives are printed as it describes and the folding is
invertible by the rule it states.

FLAGS (S-g): all 7 statements true, including the V8 and V9 echoes, the three
divergence statements and the Section 0 pointer, which is conformant under the
governing reading.

Displays and quotations (S-a, S-b): 67 of the 68 display blocks and all quoted
prose verified character-exact against the renders of pp.1-13. The three sites
repaired at G1, all on p.11, now reproduce the printed parenthesisation
exactly, each re-checked at 500 dpi. One display deviates (G4).

### Defect table

| # | file | extract line | source page | class |
| --- | --- | --- | --- | --- |
| G4 | freiberg11-strings2.md | 390 | 12 | (a) transcription deviation |

G4 is-state, verbatim:

```
$$\sum_{\substack{1\le h\le H\cr h\equiv a\bmod q\cr(\tilde{Q},h)=1}}1\ge\left(1+O\left(\frac{\log{}\log{}\log{H}}{\log{}\log{H}}\right)\right)\frac{c(q)}{\Gamma(1/\phi(q))}\cdot\frac{H(\log{t(H)})^{\frac{1}{\phi(q)}}}{\log{H}}\prod_{\substack{p\le\log{H}\cr p\equiv1\bmod q}}\left(1-\frac{1}{p}\right)$$
```

G4 finding: display (3.23) on p.12 is a three-line chain. Its first line prints
the left-hand sum, then the relation sign, then a TRIPLE SUM -- over
"1 <= l <= (1/2) log t(H)", over "p in I_l" with "p == a mod q", and over
"m <= t(H)/e^l" with "p | m => p == 1 mod q and p > log H" -- of the summand 1.
The second line then bounds that triple sum below by the main term, and the
third line carries the trailing factor. The extract omits the triple sum
entirely, joining the left-hand sum directly to the main term. Confirmed on a
400-dpi re-render of the head of p.12, where all three summation signs and
their subscript rows are unambiguous. The omitted member is not a repetition of
(3.20): (3.20) on p.10 runs its outer index to "log t(H)" while (3.23) restricts
it to "(1/2) log t(H)", and that restricted range is what the third line's sum
then re-uses. The deviation is a slip rather than a policy, because the very
next display (3.24) on the same page is the same shape -- a chain whose first
member is a sum over the same three-row condition -- and the extract reproduces
that one complete at line 400.

G4 should-state, verbatim (line 390 becomes two lines; line 391 is unchanged):

```
$$\sum_{\substack{1\le h\le H\cr h\equiv a\bmod q\cr(\tilde{Q},h)=1}}1\ge\sum_{1\le l\le\frac{1}{2}\log{t(H)}}\ \sum_{\substack{p\in I_l\cr p\equiv a\bmod q}}\ \sum_{\substack{m\le t(H)/e^{l}\cr p\mid m\Rightarrow p\equiv1\bmod q\ \text{and}\ p>\log{H}}}1$$
$$\ge\left(1+O\left(\frac{\log{}\log{}\log{H}}{\log{}\log{H}}\right)\right)\frac{c(q)}{\Gamma(1/\phi(q))}\cdot\frac{H(\log{t(H)})^{\frac{1}{\phi(q)}}}{\log{H}}\prod_{\substack{p\le\log{H}\cr p\equiv1\bmod q}}\left(1-\frac{1}{p}\right)$$
```

VERDICT: DEFECTIVE (1 defect)

---

## 4. Recount against the report-R Section 4 baseline (V6)

| file | lines R / recount | objects R / recount | `$$` R / recount | UNSURE R / recount | notes R / recount | FLAGS R / recount |
| --- | --- | --- | --- | --- | --- | --- |
| maier85-shortintervals.md | 398 / 398 | 11 / 11 | 30 / 30 | 0 / 0 | 20 / 20 | 6 / 6 |
| freiberg10-strings1.md | 806 / 806 | 79 / 79 | 153 / 153 | 0 / 0 | 22 / 22 | 7 / 7 |
| freiberg11-strings2.md | 499 / 499 | 31 / 31 | 68 / 68 | 0 / 0 | 20 / 20 | 7 / 7 |

Every column agrees; no recount divergence entered the defect tables. The `$$`
column counts lines opening with the display delimiter, per the G1 Section 5
methodology, and the TRANSCRIPTION-UNSURE column counts unsure markers, the
single literal occurrence per file being the FLAGS line that reports the count.

The surplus-line count also agrees numerically at 3 / 1 / 1, but the baseline's
PROSE gloss for it is imprecise and is corrected here. The surplus lines are
the lines carrying the display delimiter somewhere other than at line start.
For `maier85-shortintervals.md` there are three: line 15, which is the Section
0 conventions note mentioning the delimiter inside a code span, and lines 86
and 151, which are the closers of the only two multi-line display blocks in the
file. For each Freiberg extract there is exactly one, and it is the same
Section 0 conventions note at line 15; neither file contains a multi-line
display block at all. So the true multi-line-closer counts are 2 / 0 / 0, and
the 3 / 1 / 1 figure counts the conventions note as well. The numbers the
dispatch asked to be recounted are unchanged; only the description of what they
count is corrected. No extract asserts the gloss, so no defect row follows from
it.

---

## 5. Summary verdicts

```
maier85-shortintervals.md      VERDICT: DEFECTIVE (1 defect)
freiberg10-strings1.md         VERDICT: DEFECTIVE (2 defects)
freiberg11-strings2.md         VERDICT: DEFECTIVE (1 defect)
```

Totals: 0 CLEAN, 3 DEFECTIVE, 4 defect rows, distributed by class as (a) 2,
(b) 1, (c) 1. Classes (d), (e), (f) and (g) are empty: no scope violation, no
untrue header field, no forbidden-language occurrence and no untrue FLAGS
statement was found in any of the three extracts. All fourteen sites Session R
repaired were re-checked as ordinary surface and every one is correct as
applied; none of the four defect rows above is at a repaired site.

END OF GRADE RECORD G2
