# item-0029 EXTRACT FIDELITY GRADE G1

## 0. Session identity, pin, method, V-G outcomes

Lane: EXECUTOR (local workstation, Claude Code). Executor model string:
claude-opus-5. Web OFF, cloud OFF for the entire session. Date of run:
2026-08-02. This session is a FRESH executor session: it is not the Session E
session, inherits no Session E context, notes, renders or text-layer dumps, and
did not read the withheld executor-local `shiu00-strings.md`.

Pin: this session pinned to the Section 0 pin of its ephemeral dispatch, which
equalled `git rev-parse HEAD` exactly; no rule-18 bookkeeping delta arose.

METHOD AFFIRMATION (dispatch Section 4.1, affirmed as executed).
`maier85-shortintervals.md` and `hildebrandmaier88-gaps.md` were graded against
this session's own renders only; for Hildebrand-Maier the text layer was used to
locate passages and never to verify one. `freiberg10-strings1.md` and
`freiberg11-strings2.md` were pre-compared against the text layer, and every
quotation and every display was then verified against the 200-dpi render of the
cited page before its row was closed. All 69 page rasters were produced inside
this session from the anchored bytes. Four page regions were re-rendered at
300-500 dpi to settle single-glyph decisions -- p.222 of Maier 1985 and pp.7, 10
and 17 of 1005.4703v2 -- and each is named in the defect row it settles.

This session repaired nothing, edited no extract, adjudicated nothing, and
consumed no extract content for item-0029 substance. The Shiu 2000 source and
the withheld Shiu extract were not opened, not read, not graded and not hashed.

V-G outcomes:

| row | class | outcome |
| --- | --- | --- |
| V1 | gate | HOLDS. Fresh executor session; no Session E artefact present or read; the session scratchpad was empty at start. |
| V2 | gate | FOUR MATCHES. sha256 of each of the four local source PDFs equals its Section 2.1 anchor line, verified before any source was opened. |
| V3 | gate | HOLD. P1: HEAD equalled the pin, no delta. P2: `status: ratified`. P3: ANN-20260801-92.yaml present, ledger validate passed. P4: the four extracts clean under `git status --short`, `shiu00-strings.md` untracked and gitignored. P5: no HASHES line carries any of the five identifiers. |
| V4 | gate | 69 PAGES ON DISK before grading started: 9 + 6 + 24 + 30, rendered in this session at 200 dpi from the anchored bytes. |
| V5 | record | REPRODUCED, all three as expected. Maier 1985: `pdffonts` lists no fonts and `pdftotext` over the whole document returns 6 bytes (one separator per page), i.e. no text layer; expected state, not a stop (rule 9). Hildebrand-Maier 1988: one embedded CID TrueType subset (LOUMNL+TimesNewRomanPSMT, Identity-H) carrying an OCR-derived layer corrupt throughout -- `R^k` as "Rfc", `N` as "TV", `p_{n+1}-p_n` as "Pn+i ~Pn", all three reproduced in this session's dump. 1005.4703v2 and 1110.6624v1: clean LaTeX-derived layers, usable. |
| V6 | record | 9 / 6 / 24 / 30 in Section 2.1 line order. Maier 1985's six PDF pages carry printed pages 221-225 on PDF pages 1-5; PDF page 6 is blank (0 pixels below intensity 200 out of 3866367). |
| V7 | record | Recount in Section 5 below. Lines, `$$`-block counts, TRANSCRIPTION-UNSURE counts and [extract note] counts all agree with the report-E inventory for all four files; no divergence arose from the recount. |

---

## 1. maier85-shortintervals.md

Source: Maier-Primes-in-short-intervals.pdf, printed pages 221-225 (PDF pages
1-5), PDF page 6 blank. Declared scope FULL.

Surface counts checked: 11 verbatim-quoted numbered or named objects (THEOREM;
LEMMA 1; LEMMA 2 (Gallagher); LEMMA 3 (Buchstab); LEMMA 4; displays (1.1),
(2.1), (2.2), (2.3), (2.4), (3.1)); 30 `$$` display blocks; 42 explicit page
references across 17 section headings, 6 uniformity-ledger items and 9
structural-map lines; 20 [extract note] lines; 6 header fields; 6 FLAGS bullets;
54 quotation-opening lines.

Scope sweep (S-f, FULL): PASSED. Every numbered or named object the source
prints appears in the extract -- the Theorem with all three of its assertions,
Lemmas 1-4, the numbered displays (1.1), (2.1)-(2.4) and (3.1), every unnumbered
display on pp.221-225, the good-modulus definition, the sieve-function
definitions, the ACKNOWLEDGMENT, references 1-10 and the address block. No
omission.

Header fields (S-e): all six true. The absolute source path resolves to the
anchored file on this workstation; the sha256 line equals the payloads/HASHES.txt
anchor line; the bibliographic identity matches the journal line printed on
p.221; the declared method and scope match ANN-20260801-92 as booked. No
grade-state, no unresolvable deixis.

Absence checks (S-h): PASSED. No axis, gate, verdict, NOT-FOUND or grade-state
language anywhere. "Uniformity ledger" is a section title using the common noun
and is not a reference to the project ledger.

Notes, map and uniformity ledger (S-d): all 6 uniformity-ledger items and all 9
structural-map lines are true of the source as printed and carry no
interpretation beyond labels and page-anchored facts. The p.222 print-slip note
(the vertical bar standing where a closing parenthesis is expected in
`L(s,chi)`) is true: this session re-rendered p.222 at 300 dpi and confirms both
the slip and the outer bars of the displayed zero-free condition.

Displays and quotations (S-a, S-b, S-c): all 30 display blocks and all quoted
prose verified character-exact against the renders of pp.221-225; all page
citations correct.

FLAGS (S-g): five of six statements true. The sixth is defective.

### Defect table

| # | file | extract line | source page | class |
| --- | --- | --- | --- | --- |
| M1 | maier85-shortintervals.md | 394-395 | 222 | (g) untrue FLAGS statement |

M1 is-state, verbatim:

```
  and cites Gallagher only in the reference list as [3]; the string
  "Gallagher" does not appear in the body of this paper.
```

M1 finding: p.222 prints the lemma heading `LEMMA 2 (Gallagher).` in the body of
the paper, immediately above the good-modulus prime-counting display. The string
"Gallagher" therefore does appear in the body. The claim is also contradicted by
the same FLAGS bullet two lines earlier ("Lemma 3 (Buchstab) and Lemma 2
(Gallagher)") and by the extract's own transcription at line 133. Confirmed on a
300-dpi re-render of the p.222 region. The first half of the clause is true: the
bracketed citation [3] appears only in the reference list on p.225 and nowhere in
the body of pp.221-225.

M1 should-state, verbatim:

```
  and cites Gallagher only in the reference list as [3]; the bracketed
  citation [3] does not appear in the body of this paper, though the name
  Gallagher is printed in the heading of LEMMA 2 (p.222).
```

VERDICT: DEFECTIVE (1 defect)

---

## 2. hildebrandmaier88-gaps.md

Source: S0002-9939-1988-0958032-5.pdf, printed pages 1-9 coinciding with the PDF
pages. Declared scope FULL.

Surface counts checked: 31 verbatim-quoted numbered or named objects (THEOREM;
COROLLARY; LEMMA 1; LEMMA 2; LEMMA 3; LEMMA 4; displays (1)-(21), (*), (**),
(6)' and (7)'); 59 `$$` display blocks; 25 display page labels plus 71 explicit
page references across 22 section headings, 6 uniformity-ledger items and 10
structural-map lines; 20 [extract note] lines; 6 header fields; 8 FLAGS bullets;
95 quotation-opening lines.

Scope sweep (S-f, FULL): PASSED. Every numbered or named object the source
prints appears in the extract: the Theorem, the Corollary, Lemmas 1-4, the full
printed proof of Lemma 4, the single display sequence (1)-(21) complete, the
named displays (*), (**), (6)' and (7)', every unnumbered display on pp.1-8, the
front matter and copyright line, references 1-9 and both address lines. No
omission.

Header fields (S-e): all six true, including the bibliographic identity
"Proc. Amer. Math. Soc. 104 (1988), no. 1, 1-9" against the masthead on p.1 and
the printed pagination. No grade-state, no unresolvable deixis.

Absence checks (S-h): PASSED. The 11 occurrences of "Erdos" are SOURCE text --
the mathematician named in the abstract, the introduction and reference entries
[1] and [2] -- and not project-object language.

Notes, map and uniformity ledger (S-d): all 6 uniformity-ledger items and all 10
structural-map lines true and page-anchored. The four conventions notes are true:
the cardinality glyph the source uses is the doubled-stroke hash, the declared
`\lvert ... \rvert` substitution is applied consistently, and the text-layer
corruption note is reproduced exactly by this session's own dump.

The dispatch's S-d attention example is CONFIRMED against both pages: p.2 prints
"Erdos and Ricci [8]" and entry [8] on p.9 is "G. Ricci" alone, with Erdos
appearing as entries [1] and [2]. The extract's FLAGS statement of this
discrepancy is true as written.

The cross-source FLAGS statement about the good-modulus definition is true in
both directions: p.2 of this source restricts the zero-free condition to
NONPRINCIPAL characters, and p.222 of Maier 1985 says "all characters".

Displays and quotations (S-a, S-b, S-c): all 59 display blocks and all quoted
prose verified character-exact against the renders of pp.1-9; all 25 display page
labels and all section-heading page spans correct.

FLAGS (S-g): all 8 statements true, including the sha256 claim, the
TRANSCRIPTION-UNSURE count of 0, both V-finding echoes and the non-strict
primorial claim.

zero defects

VERDICT: CLEAN

---

## 3. freiberg10-strings1.md

Source: 1005.4703v2.pdf, printed pages 1-24 coinciding with the PDF pages.
Declared scope FULL.

Surface counts checked: 79 verbatim-quoted numbered or named objects (Theorem
1.1; Lemma 2.1; Propositions 2.2 and 2.3; Lemmas 4.1 and 4.2; Lemmas 5.1-5.5;
displays (2.1)-(2.12), (3.1)-(3.2), (4.1)-(4.14), (5.1)-(5.32), (6.1)-(6.8));
153 `$$` display blocks; 65 display page labels plus 114 explicit page references
across 13 section headings, 7 uniformity-ledger items and 9 structural-map lines;
22 [extract note] lines; 6 header fields; 7 FLAGS bullets; 193 quotation-opening
lines.

Scope sweep (S-f, FULL): PASSED. Every numbered or named object the source
prints appears in the extract, including the eighteen displays (5.1)-(5.18) and
the nine displays (5.24)-(5.32) that the dispatch attention list did not name.
Sections 1-8 and both reference pages are covered. No omission.

Header fields (S-e): all six true.

Absence checks (S-h): the extract carries no axis, gate, verdict, NOT-FOUND or
grade-state language. It does carry one reference to a project ledger entry; that
is recorded as defect F1 below under class (c), where the same sentence's
substantive failure lies.

Displays and quotations (S-a, S-b, S-c): 150 of the 153 display blocks and all
quoted prose verified character-exact against the renders of pp.1-24. Three
display blocks deviate (F2, F3, F4). Four of the source's own print slips are
transcribed as printed and correctly flagged; two further print slips are
silently normalised (F3, F4).

Notes, map and uniformity ledger (S-d): all 7 uniformity-ledger items are true
and page-anchored. Six of the nine structural-map lines are true; four page
references inside three of them are wrong (F6, F7, F8, F9). One conventions note
carries a claim that is not a fact about the source (F1). One section heading
gives a page span that excludes a page it covers (F5).

FLAGS (S-g): all 7 statements true as written.

### Defect table

| # | file | extract line | source page | class |
| --- | --- | --- | --- | --- |
| F1 | freiberg10-strings1.md | 26-28 | n/a (not a source claim) | (c) untrue or interpretive note claim |
| F2 | freiberg10-strings1.md | 258 | 7 | (a) transcription deviation |
| F3 | freiberg10-strings1.md | 333 | 10 | (a) transcription deviation |
| F4 | freiberg10-strings1.md | 534 | 17 | (a) transcription deviation |
| F5 | freiberg10-strings1.md | 73 | 4 | (b) page-reference error |
| F6 | freiberg10-strings1.md | 750 | 8 | (b) page-reference error |
| F7 | freiberg10-strings1.md | 751 | 17 | (b) page-reference error |
| F8 | freiberg10-strings1.md | 755 | 8 | (b) page-reference error |
| F9 | freiberg10-strings1.md | 758 | 17 | (b) page-reference error |

F1 is-state, verbatim:

```
[extract note] The source prints no journal reference on the paper; it is an arXiv
preprint throughout. The paper was later published as J. London Math. Soc. 84 (2011)
344-364, which is recorded in ANN-20260801-91 but is not printed on these bytes.
```

F1 finding: the first sentence is true and page-anchored -- pp.1-24 carry only
the arXiv stamp and no journal line. The second sentence is neither true of the
source as printed nor a page-anchored fact: it imports an external bibliographic
statement whose stated authority is a project ledger entry, and it names that
entry inside the extract. An extract is a source surrogate; a ledger identifier
inside a hashed extract also goes stale the moment the ledger moves, which is the
state rule 27 exists to prevent one section higher up.

F1 should-state, verbatim:

```
[extract note] The source prints no journal reference on the paper; it is an arXiv
preprint throughout.
```

F2 is-state, verbatim:

```
$$\sum_{p\nmid Q}\left(-\frac{k}{p}-\frac{k^{2}}{2p^{2}}-\cdots-k\left(-\frac{1}{p}-\frac{1}{2p^{2}}-\cdots\right)\right)\ll k^{2}\sum_{p>\log{H}}\frac{1}{p^{2}}\ll\frac{k^{2}}{\log{H}\log{}\log{H}}.$$
```

F2 finding: p.7 prints the summand inside a BRACE pair enclosing two
separately parenthesised groups -- brace, open paren, the k-series, close paren,
minus k, open paren, the 1-series, close paren, close brace. The extract
transcribes a single parenthesis pair and drops the inner pair around the
k-series, so the printed delimiter structure is not reproduced. Confirmed on a
300-dpi re-render of the p.7 display. AGENTS.md prescribes `\lbrace` and
`\rbrace` for visible braces, and the same extract uses them correctly at line
179, so this is a slip rather than a declared convention.

F2 should-state, verbatim:

```
$$\sum_{p\nmid Q}\left\lbrace\left(-\frac{k}{p}-\frac{k^{2}}{2p^{2}}-\cdots\right)-k\left(-\frac{1}{p}-\frac{1}{2p^{2}}-\cdots\right)\right\rbrace\ll k^{2}\sum_{p>\log{H}}\frac{1}{p^{2}}\ll\frac{k^{2}}{\log{H}\log{}\log{H}}.$$
```

F3 is-state, verbatim:

```
$$\sum_{D\le R^{2}}\frac{\mu^{2}(D)\kappa^{\omega(D)}}{D}=\sum_{d_1\cdots d_{\kappa}\le R^{2}}\frac{\mu^{2}(d_1)\cdots\mu^{2}(d_{\kappa})}{d_1\cdots d_{\kappa}}\ll(\log{R^{2}})^{\kappa}\ll(\log{N})^{\kappa},$$
```

F3 finding: on p.10 the second summation condition is printed with the first
factor carrying NO subscript -- d, then the ellipsis, then d-sub-kappa -- while
the numerator and denominator of the same display both print the subscripted
form. Confirmed on a 300-dpi re-render of the p.10 display. The extract supplies
the missing subscript, which repairs a source print slip silently. This extract's
own standard, applied four times elsewhere, is to transcribe print slips as
printed and record them in FLAGS.

F3 should-state, verbatim:

```
$$\sum_{D\le R^{2}}\frac{\mu^{2}(D)\kappa^{\omega(D)}}{D}=\sum_{d\cdots d_{\kappa}\le R^{2}}\frac{\mu^{2}(d_1)\cdots\mu^{2}(d_{\kappa})}{d_1\cdots d_{\kappa}}\ll(\log{R^{2}})^{\kappa}\ll(\log{N})^{\kappa},$$
```

with the slip added to the FLAGS print-slip list as a fifth item, naming p.10.

F4 is-state, verbatim:

```
$$\sum_{1\le l\le\log{}\log{H}}\ \sum_{\substack{p\in I_l\cr p\not\equiv1\bmod q}}\ \sum_{\substack{p'\in J_l\cr p'\equiv1\bmod q}}1\ll\sum_{1\le l\le\log{}\log{H}}\frac{e^{l}H}{(\log{H})^{3}}\frac{(\log{H})^{2}}{e^{l}\log{}\log{H}}\ll\frac{H}{\log{H}}.$$
```

F4 finding: on p.17 the third summation's second condition is printed with the
UNPRIMED variable -- p congruent to 1 mod q -- under the sum over p-prime in
J-sub-l. Confirmed on a 500-dpi re-render of the p.17 condition line, where the
two conditions read "p not-congruent 1 mod q" and "p congruent 1 mod q" with no
prime on either. The extract supplies the prime on the second, repairing a source
print slip silently.

F4 should-state, verbatim:

```
$$\sum_{1\le l\le\log{}\log{H}}\ \sum_{\substack{p\in I_l\cr p\not\equiv1\bmod q}}\ \sum_{\substack{p'\in J_l\cr p\equiv1\bmod q}}1\ll\sum_{1\le l\le\log{}\log{H}}\frac{e^{l}H}{(\log{H})^{3}}\frac{(\log{H})^{2}}{e^{l}\log{}\log{H}}\ll\frac{H}{\log{H}}.$$
```

with the slip added to the FLAGS print-slip list as a sixth item, naming p.17.

F5 is-state, verbatim:

```
## 3. Section 2, Preliminaries (pp.2-3)
```

F5 finding: Section 2 of the source begins on p.2 and ends on p.4, where display
(2.12) and the closing sentence "The implied constant in (2.11) depends at most
on q." are printed above the Section 3 heading. The extract's own inner label at
line 139 reads "display (2.12), p.4", so the heading contradicts the body it
covers.

F5 should-state, verbatim:

```
## 3. Section 2, Preliminaries (pp.2-4)
```

F6 and F7 is-state, verbatim (one note, two wrong page numbers):

```
[extract note] 2. Lemma 2.1 (p.2) is quoted from [2, Chapter 14] and is used to define
$`q_0`$, $`p_0`$ and (2.1); (2.1) is then invoked in Section 4 twice, at
$`G(0,0;\Omega)`$ and $`G(0,0;\Omega^{+})`$ (pp.9, 11), and in the proof of Proposition
2.3 (p.16).
```

F6 finding: the first invocation of (2.1) in Section 4 is at the evaluation of
G(0,0;Omega), which with its sentence "The last product is ~ 1 by (2.1)." is
printed on p.8, not p.9. Page 9 carries (4.9)-(4.12) and no occurrence of
G(0,0;Omega). The second page number, 11, is correct.

F7 finding: the proof of Proposition 2.3 begins on p.17, headed "Proof of
Proposition 2.3." immediately below the Lemma 5.5 statement that closes p.16, and
the invocation "If p_0 != 1 then by (2.1)" is printed on p.17. Page 16 carries
(5.19)-(5.23) and the statement of Lemma 5.5 only.

F6 and F7 should-state, verbatim:

```
[extract note] 2. Lemma 2.1 (p.2) is quoted from [2, Chapter 14] and is used to define
$`q_0`$, $`p_0`$ and (2.1); (2.1) is then invoked in Section 4 twice, at
$`G(0,0;\Omega)`$ and $`G(0,0;\Omega^{+})`$ (pp.8, 11), and in the proof of Proposition
2.3 (p.17).
```

F8 is-state, verbatim:

```
[extract note] 4. Lemma 4.1 (p.6) is proved on pp.6-7 from (2.2), (2.3), (4.5), (4.6)
and the prime number theorem. Lemma 4.2 (p.8) is quoted as Lemma 2 of [5]; no argument
is printed.
```

F8 finding: the proof of Lemma 4.1 begins on p.6 and ends on p.8, whose first
sentence "by the prime number theorem, because Delta <= H^binom(k,2).
Exponentiating and letting H tend to infinity yields (4.5)." carries the closing
box. The stated range pp.6-7 excludes that page. The second sentence of the note
is true.

F8 should-state, verbatim:

```
[extract note] 4. Lemma 4.1 (p.6) is proved on pp.6-8 from (2.2), (2.3), (4.5), (4.6)
and the prime number theorem. Lemma 4.2 (p.8) is quoted as Lemma 2 of [5]; no argument
is printed.
```

F9 is-state, verbatim:

```
[extract note] 5. Proposition 2.3 (p.3) is proved on p.16 from Lemma 5.5 and Lemma 5.1,
together with (5.21) and (5.23).
```

F9 finding: as at F7, the printed proof of Proposition 2.3 occupies p.17, not
p.16. The rest of the note is true.

F9 should-state, verbatim:

```
[extract note] 5. Proposition 2.3 (p.3) is proved on p.17 from Lemma 5.5 and Lemma 5.1,
together with (5.21) and (5.23).
```

VERDICT: DEFECTIVE (9 defects)

---

## 4. freiberg11-strings2.md

Source: 1110.6624v1.pdf, printed pages 1-30 coinciding with the PDF pages.
Declared scope PARTIAL: Sections 1-3 in full; Section 4's Selberg-Delange proof
by named reference only, not transcribed.

Surface counts checked: 31 verbatim-quoted numbered or named objects (Theorem
1.1; Theorem 3.1 (Siegel-Walfisz); Lemmas 3.2, 3.3 and 3.4; displays (1.1)-(1.2)
and (3.1)-(3.24)); 68 `$$` display blocks; 26 display page labels plus 62
explicit page references across 11 section headings, 7 uniformity-ledger items
and 6 structural-map lines; 19 [extract note] lines; 6 header fields; 7 FLAGS
bullets; 89 quotation-opening lines.

Scope boundary (S-f, PARTIAL): PASSED, and the boundary is exactly honoured.
Sections 1-3 are complete: the abstract, the whole of Sections 1 and 2 including
all three footnotes, the statements of Theorem 3.1 and Lemmas 3.2-3.4, the
construction (3.1)-(3.6), the proof of Theorem 1.1 and the full printed proof of
Lemma 3.4 in both parts, ending with the closing box at the foot of p.13. Nothing
is transcribed from Section 4 beyond its printed heading, which the
scope-boundary section quotes as a named reference. The scope-boundary section's
four factual claims are all verified true against the renders: Section 4 headed
"4. Proof of Lemmas 3.2 and 3.3" begins on p.13 and ends on p.29; Section 5
headed "5. Acknowledgements" is on p.29; the reference list occupies pp.29-30;
the address block "Institutionen for matematik, KTH, 100 44 Stockholm, Sweden"
with an e-mail address closes p.30.

Header fields (S-e): all six true, including the declared PARTIAL scope string,
which matches ANN-20260801-92 as booked and matches what the extract does.

Absence checks (S-h): PASSED. No axis, gate, verdict, NOT-FOUND, grade-state or
project-object language anywhere.

Notes, map and uniformity ledger (S-d): all 7 uniformity-ledger items and all 6
structural-map lines are true and page-anchored, including the two-page ranges
for parts (a) and (b) of the proof of Lemma 3.4 and the p.13 location of the
closing numerical step. The footnote note is true: the three footnotes of
Section 2 are printed at the foot of pp.2-3.

FLAGS (S-g): all 7 statements true, including the V8 and V9 echoes, the three
divergence statements and the section-sign statement.

Page references (S-c): all 26 display page labels and all 11 section-heading page
spans correct.

Displays and quotations (S-a, S-b): 65 of the 68 display blocks and all quoted
prose verified character-exact against the renders of pp.1-13. Three sites
deviate.

### Defect table

| # | file | extract line | source page | class |
| --- | --- | --- | --- | --- |
| G1 | freiberg11-strings2.md | 372 | 11 | (a) transcription deviation |
| G2 | freiberg11-strings2.md | 375 | 11 | (a) transcription deviation |
| G3 | freiberg11-strings2.md | 379 | 11 | (a) transcription deviation |

G1 is-state, verbatim:

```
$`\log{H}=\log{(t(H)/e^{l})}^{1+o(1)}`$, where $`o(1)`$ is shorthand for
```

G1 finding: p.11 prints the right-hand side as the WHOLE logarithm enclosed in a
parenthesis pair and that pair raised to the exponent. The extract's form
attaches the exponent to the logarithm's argument instead, which is a different
quantity; the printed outer pair is not reproduced. The same extract writes the
correctly parenthesised form at line 379's denominator, so this is a slip rather
than a declared convention.

G1 should-state, verbatim:

```
$`\log{H}=\left(\log{(t(H)/e^{l})}\right)^{1+o(1)}`$, where $`o(1)`$ is shorthand for
```

G2 is-state, verbatim:

```
$$3\le q\le(\log{H})^{\alpha}\le\left(\log{t(H)/e^{l}}\right)^{\beta},\qquad\beta:=\tfrac{1}{2}(\alpha+\tfrac{1}{2})\in(0,\tfrac{1}{2}).$$
```

G2 finding: p.11 prints two nested parenthesis pairs -- one around the quotient
that is the logarithm's argument, one around the whole logarithm carrying the
exponent beta. The extract reproduces only the outer pair, so the rendered form
reads as the logarithm of t(H) divided by e-to-the-l, a different quantity.

G2 should-state, verbatim:

```
$$3\le q\le(\log{H})^{\alpha}\le\left(\log{(t(H)/e^{l})}\right)^{\beta},\qquad\beta:=\tfrac{1}{2}(\alpha+\tfrac{1}{2})\in(0,\tfrac{1}{2}).$$
```

G3 is-state, verbatim (the deviation is the numerator of the second fraction):

```
$$\sum_{\substack{m\le t(H)/e^{l}\cr p\mid m\Rightarrow p\equiv1\bmod q\ \text{and}\ p>\log{H}}}1=\left(1+O\left(\frac{(\log{}\log{t(H)})^{c}}{(\log{t(H)})^{1-2\beta}}\right)\right)\frac{c(q)}{\Gamma(1/\phi(q))}\times\frac{t(H)}{e^{l}}\cdot\frac{\left(\log{t(H)/e^{l}}\right)^{\frac{1}{\phi(q)}}}{\log{(t(H)/e^{l})}}\prod_{\substack{p\le\log{H}\cr p\equiv1\bmod q}}\left(1-\frac{1}{p}\right)$$
```

G3 finding: the first line of display (3.22) on p.11 prints both the numerator
and the denominator of that fraction with the logarithm's argument parenthesised.
The extract parenthesises the denominator and not the numerator, so one display
block carries both forms of the same object.

G3 should-state, verbatim:

```
$$\sum_{\substack{m\le t(H)/e^{l}\cr p\mid m\Rightarrow p\equiv1\bmod q\ \text{and}\ p>\log{H}}}1=\left(1+O\left(\frac{(\log{}\log{t(H)})^{c}}{(\log{t(H)})^{1-2\beta}}\right)\right)\frac{c(q)}{\Gamma(1/\phi(q))}\times\frac{t(H)}{e^{l}}\cdot\frac{\left(\log{(t(H)/e^{l})}\right)^{\frac{1}{\phi(q)}}}{\log{(t(H)/e^{l})}}\prod_{\substack{p\le\log{H}\cr p\equiv1\bmod q}}\left(1-\frac{1}{p}\right)$$
```

VERDICT: DEFECTIVE (3 defects)

---

## 5. Recount against the report-E inventory (V7)

| file | lines E / recount | objects E / recount | `$$` E / recount | UNSURE E / recount | notes E / recount |
| --- | --- | --- | --- | --- | --- |
| maier85-shortintervals.md | 397 / 397 | 11 / 11 | 30 / 30 | 0 / 0 | 20 / 20 |
| hildebrandmaier88-gaps.md | 492 / 492 | 31 / 31 | 59 / 59 | 0 / 0 | 20 / 20 |
| freiberg10-strings1.md | 804 / 804 | 79 / 79 | 153 / 153 | 0 / 0 | 22 / 22 |
| freiberg11-strings2.md | 497 / 497 | 31 / 31 | 68 / 68 | 0 / 0 | 19 / 19 |

Every column agrees. The `$$` column counts display blocks, not delimiter
occurrences: each count is the number of lines opening with the display
delimiter, and the surplus lines carrying the delimiter elsewhere are the closers
of multi-line blocks (3, 1, 1 and 1 respectively). The TRANSCRIPTION-UNSURE
column is the count of unsure markers, which is zero in all four; the single
literal occurrence of the token in each file is the FLAGS line reporting the
count. No recount divergence arose, so no recount finding enters the defect
tables above.

---

## 6. Summary verdicts

```
maier85-shortintervals.md      VERDICT: DEFECTIVE (1 defect)
hildebrandmaier88-gaps.md      VERDICT: CLEAN
freiberg10-strings1.md         VERDICT: DEFECTIVE (9 defects)
freiberg11-strings2.md         VERDICT: DEFECTIVE (3 defects)
```

Totals: 1 CLEAN, 3 DEFECTIVE, 13 defect rows, distributed by class as (a) 6,
(b) 5, (c) 1, (g) 1. Classes (d), (e) and (f) are empty: no scope violation, no
untrue header field, and no forbidden-language occurrence was found in any of the
four extracts.

END OF GRADE RECORD G1
