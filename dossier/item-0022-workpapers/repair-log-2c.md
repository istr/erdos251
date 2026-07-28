# item-0022 extract repair log -- Phase 2c, repaired against the anchored PDFs

Phase 2c of the item-0033 disposition chain. Executed by the local
executor under an ephemeral dispatch pinned to `f1bd97a`, never
committed; the operator apply is the ratifying commit.

**This pass opened the seven PDFs and edited the seven extracts.** It
hashes nothing. The grade that confers corpus standing is a separate
pass -- the Phase 2b protocol re-run against the repaired extracts by a
fresh session -- and that pass hashes the CLEAN. A session does not
grade the artifact it just produced.

**Specification.** `extract-grades-r1.md` (ANN-78) at `f1bd97a`. Its
per-extract fail tables and I1/I2 dispositions are the worklist. Nothing
was repaired that the grade does not name, except the universal header
and one ASCII-gate violation recorded under S7 below.

**Fidelity authority.** Every repair below was decided by opening the
anchored PDF at the location and comparing. The extract's own text was
never treated as evidence about itself. No dropped report, no kickoff
dispatch, and no operator-held PDF was opened, at any point, for any
purpose.

**Tooling.** `pdftotext -layout` and `pdftotext` (raw) for the text
layer, `pdfinfo` for metadata, `sha256sum` for anchor identity, and
`pdftoppm -r 200 -png` for rendered page images. Renders were used where
a judgement turns on a glyph the text layer cannot settle: pages 7 and 8
of `1004.1072v1.pdf`.

---

## Section 0 -- preflight, all six predicates

| predicate | result |
| --- | --- |
| P1 -- `git diff --stat f1bd97a..HEAD` empty or `roadmap/` only | PASS (empty; HEAD equals the pin) |
| P2 -- last ledger annotation is `ANN-20260728-78` | PASS |
| P3 -- `item-0033` ratified at position 1 of `_order.md` | PASS |
| P4 -- `extract-grades-r1.md` unmodified since `f1bd97a` | PASS |
| P5 -- seven PDFs, sha256 equals header value and booked line | PASS, 7 of 7 |
| P6 -- the two HANDOVER anchors each occur exactly once | PASS, 1 and 1 |

No rule-18 delta: HEAD equals the Section 0 pin.

### P5 detail -- anchor identity, checked before any edit

Each file's sha256 equals both the value printed in the extract header
and the line booked in `payloads/HASHES.txt`.

| extract | anchor | sha256 (prefix) | HASHES.txt line |
| --- | --- | --- | --- |
| bloomkuperberg23-oddmoments.md | 2312.09021v2.pdf | 46b80c9b | 85 |
| kowalski-singser-dist.md | singular-series-distribution.pdf | 378433db | 83 |
| kuperberg21-oddmoments.md | 2109.03767v3.pdf | e1bbabbd | 84 |
| kuperberg23-apsmooth.md | 2301.06095v1.pdf | c67fdd9c | 86 |
| pintz10-patterns.md | 1004.1072v1.pdf | 74824028 | 82 |
| precedent-p1-2605.22763.md | 2605.22763v2.pdf | d71b78f1 | 87 |
| precedent-p3-2601.07421.md | 2601.07421v5.pdf | fb1bccdb | 88 |

---

## Section 1 -- the universal header repair, applied to all seven

Removed from every extract: the assurance
`(operator-verified; re-verified this session)` and the ephemeral
identification `CONFIRMED against the dispatch`. Both claimed a fidelity
the lane that wrote them could not have had, because that lane could not
open the source.

Replaced in every extract with a provenance line that states only what
is true at this pin: transcribed from the anchored PDF named in the
header; fidelity repair applied per the ANN-78 grade; re-grade pending.
The header now states no fidelity grade the repair has not earned.

The `Front-matter identification` sentence was re-pointed from the
dispatch to p.1 of the anchor in all seven.

---

## Section 2 -- bloomkuperberg23-oddmoments.md

Anchor: `2312.09021v2.pdf`, 38 pages.

| # | repair | checked against |
| --- | --- | --- |
| B10 | The bibliography entry "V. Kuperberg, Odd moments in the distribution of primes, arXiv:2109.03767, 2021" was attributed to "anchor 3", an index into a numbering that no longer exists. Re-attributed by identifier to `2301.06095v1` reference 4. The header now also records what this anchor's own corresponding entry prints. | `2301.06095v1.pdf` p.19, reference 4 (printed `4.`, not `[4]`); `2312.09021v2.pdf` p.37, reference [17] |
| B10a | The reading "original submission 2023" was sourced to that mis-attributed quotation. Re-sourced to the arXiv identifier 2312, printed on p.1. | p.1 arXiv stamp |
| B11 | NOT-FOUND probe said no claim about even-order moments of the refined singular series is present. Narrowed to "not proved here": the even-k asymptotic is printed on p.4 and attributed there to Montgomery-Soundararajan [19]. | p.4 |
| B12 | Scope sentence said the paper's scope "is the odd-order moments of $`R_k(h)`$ only". Replaced with the three objects the paper actually carries, and the probes scoped to the singular-series object. | p.1-p.2 (Theorem 1), p.4 (Theorem 2, Theorem 3) |
| I1 L42 | `## 2. Statement cited by item-0022's reports` retitled `## 2. Statement extracted from the anchor` | -- |
| I1 L44 | Section 2.1 heading re-anchored to `(Theorem 2, p.4)` | p.4 |
| I1 L55 | Framing clause `This confirms report 1's claim:` deleted; the sentence now states what Theorem 2 proves, with no addressee | -- |
| I2 L9 | `item-0022 kickoff dispatch` reference removed | identification printed on p.1 |
| I2 L15 | `against the dispatch` removed | identification printed on p.1 |
| I3 L18, L75-L78 | The assertion that report 1's bibliography carries no URL for this paper is an assertion about a dropped object. Dropped. The disclaimer half of the FLAGS sentence survives, restated without the addressee. | -- |

The probe clause that carries item-0026 reasoning -- no uncentered
second moment $`\sum\mathfrak{S}(H)^2`$ (grade check B13) -- is
preserved verbatim. The Theorem 2 display and the front-matter
quotation were not touched.

---

## Section 3 -- kowalski-singser-dist.md

Anchor: `singular-series-distribution.pdf`, 30 pages. Printed page N
equals PDF page N throughout, re-confirmed.

| # | repair | checked against |
| --- | --- | --- |
| W7 | Singular-series definition cited to p.1; corrected to p.2, eq. (1.1). | p.2 |
| W9 | Theorem 1.1 cited to p.5; corrected to p.3. | p.3 |
| W11 | Gallagher eq. (1.5) cited to p.5; corrected to p.3. | p.3 |
| W17 | Inside the block introduced `p.15, Example 3.5:`, the source's cross-reference "(see Example 4.3 for a more precise estimate)" had been deleted with no ellipsis and the following independent sentence folded into the parenthesis that replaced it. Both restored as printed. | p.15 |
| W26 | Probe said [MS] "is cited only in this paper's own bibliography". It is cited in the body on p.3. Narrowed, with the body sentence quoted; the substantive half -- no $`R_k(h)`$ theorem stated or proved here -- is preserved. | p.3 |
| I1 L52 | `## 2. Statements cited by item-0022's reports` retitled `## 2. Statements extracted from the anchor` | -- |
| I2 L16 | `against the dispatch` removed; the source URL is now pointed at its in-tree record. | p.1; `payloads/HASHES.txt` line 83 |
| I3 L172-L187 | The attribution of the ratio $`1.1504807723\ldots`$ and its two derived quantities to report 1 cannot be checked at any pin. The derivation is restated as this project's own, from the anchored ingredients. The arithmetic itself is unchanged and still points at `kowalski-mu-recheck.py` / `.txt`. | p.15 (the $`\mu_k(2)`$ Euler product, its numerical values, the parity-vanishing probability) |

PDF page 5 was read to confirm W9 and W11: it carries the close of
Section 1 and the opening of Section 2, and names Theorem 1.1 only in a
forward reference. Every transcribed formula and every numerical value
was left byte-for-byte as it was.

---

## Section 4 -- kuperberg21-oddmoments.md

Anchor: `2109.03767v3.pdf`, 51 pages.

| # | repair | checked against |
| --- | --- | --- |
| K13 | Same defect as B10, attributed here to "anchor 4". Re-attributed by identifier to `2301.06095v1` reference 4. Confirmed that the quoted string is not printed in this anchor, whose bibliography carries no entry for this paper at all. | `2301.06095v1.pdf` p.19; whole of `2109.03767v3.pdf` |
| K14 | The "byte-for-byte the same formula report 1 attributes ..." comparison has one term that is gone and is unverifiable at any pin. Severed. The anchored half is kept: this anchor restates the Montgomery-Soundararajan estimate in its own introduction as the result it builds on. | p.3, eq. (4) |
| K16 | Uniformity ledger cited p.4 for a statement p.4 does not carry, and stated it more strongly than the source does. Re-cited to p.3, with the printed sentence quoted, and the "only an upper bound" reading marked as inference from Theorem 1.2 and Conjecture 1.1. | p.3; p.4 carries Theorems 1.3 and 1.4, on the function-field moments $`m_k(Q;h)`$ |
| K18 | Probe asserted the paper "works throughout with the centered/refined singular series $`\mathfrak{S}_0`$ and its sums $`R_k(h)`$". Contradicted three ways; the generalization is dropped and K17's clause kept. | p.1 (uncentered $`\mathfrak{S}(\mathcal{D})`$, eq. (1)); p.2 (Gallagher's uncentered average, the inversion); p.4 (Theorems 1.3, 1.4) |
| I1 L40 | `## 2. Statements cited by item-0022's reports` retitled `## 2. Statements extracted from the anchor` | -- |
| I1 L59 | Section 2.2 heading re-anchored to `(Conjecture 1.1 and Theorem 1.2, p.3)` | p.3 |
| I1 L88 + verbatim prose | The framing clause `matching report 1's own characterization` **and the German-language quotation of report 1 it introduced** were removed together, as one operation. The probe's surviving sentence stands on grade check K17 alone. | -- |
| I2 L8 | `item-0022 kickoff dispatch` removed; the 2021 submission is carried by the arXiv identifier on p.1. | p.1 |
| I2 L15 | `against the dispatch` removed | p.1 |

All three transcribed displays -- eq. (4), Conjecture 1.1, Theorem 1.2
-- are byte-for-byte unchanged.

---

## Section 5 -- kuperberg23-apsmooth.md

Anchor: `2301.06095v1.pdf`, 19 pages.

| # | repair | checked against |
| --- | --- | --- |
| A12 | The quoted passage was attributed to "Theorem 1.2's remark". The paragraph the paper labels `Remark.` is a different one and says something else. Re-cited to Theorem 1.2's "In particular" clause. | p.4 |
| A13 | Inside the same quotation the source's "..., then" had been replaced by an ellipsis followed by the extract's own connective "the theorem implies", unmarked. The source's "then" is restored and the quotation now opens where the source opens it. | p.4 |
| A15 | "Theorems 1.1-1.5" implies a Theorem 1.4 the paper does not have. Replaced by the four the paper states, with the absence recorded. | whole PDF: Theorem 1.1 p.3, 1.2 p.4, 1.3 p.5, 1.5 p.5; zero occurrences of "Theorem 1.4" |
| I1 L39 | `## 2. Statement cited by item-0022's reports` retitled `## 2. Statement extracted from the anchor` | -- |
| I1 L41 | Section 2.1 heading re-anchored to `(Theorems 1.1 and 1.2, pp.3-4)` | pp.3-4 |
| I1 L60 | Framing clause `This confirms report 1's characterization:` deleted | -- |
| I1 L84 | The closing sentence `This matches report 1's own characterization of the gap ...` deleted whole | -- |
| I2 L12 | `against the dispatch` removed | p.1 |
| header | The attribution of `2210.09775v2` to "report 1's footnote 6", and the checklist-row pointer, deleted. The verifiable half -- that this is a different paper -- is kept. | p.1 |

The Theorem 1.1 display, including the error term, is byte-for-byte
unchanged.

---

## Section 6 -- pintz10-patterns.md

Anchor: `1004.1072v1.pdf`, 9 pages. The stress case, and the only
extract carrying a mathematical fail.

### 6.1 The one display repair (P27)

Inside the block introduced with the word "verbatim", the extract
printed the (2.16) middle numerator as
$`1-\frac{r(\nu_p+1)}{p}+O(p^{-2})`$. The source prints
$`\frac{\nu_p}{p}+1-\frac{\nu_p}{p}-\frac{r(\nu_p+1)}{p}+O(1/p^2)`$ --
the two $`\nu_p/p`$ terms **unperformed**. The extract had performed the
cancellation silently inside a quotation.

Repaired: the numerator is now transcribed as the source prints it, and
the cancellation is recorded one line below as the extract's own step,
so a reader sees the source's state and the extract's algebra
separately.

Confirmed three ways, because the grade turns on it: the `-layout` text
layer, the raw text layer, and a 200-dpi render of p.7 read as an image.
All three print the uncancelled numerator.

**The first fraction was not touched.** It carries the exponent r at
both factors, it is the feature the extract relies on, and it passed
(grade check P26). Verified byte-for-byte unchanged.

### 6.2 The remaining repairs

| # | repair | checked against |
| --- | --- | --- |
| P8 | The Lemma 2 lead-in was quoted as "For fixed nu, r"; the source prints "For fixed nu r", with no comma. Transcribed as printed, with the slip noted below the quotation. | p.6 |
| P13 | The proof close was quoted as "P = O(H)"; the source prints a digit zero, "P = 0(H)". Transcribed as printed, with the slip noted. | p.8, text layer and 200-dpi render |
| P20 | The proof opening was quoted as "<< or O symbols"; the source prints a digit zero, "<< or 0 symbols". Transcribed as printed, with the slip noted. | p.7, text layer and 200-dpi render |
| P21 | The (2.12) definition of $`\Delta`$ had been rendered $`\Delta:=\prod_i(h-d_i)`$, dropping both product limits. Restored to $`\Delta:=\prod_{i=1}^{\nu}(h-d_i)`$, which is the part of the display that shows the product runs over $`\mathcal{D}`$ and not over $`\mathcal{D}^{+}`$. | p.7, text layer and 200-dpi render |
| P28 | The block was introduced as "p.7"; the last two equalities of (2.16) are printed at the top of p.8. Corrected to "pp.7-8". | p.7 into p.8 |
| I1 L35 | `## 2. Statements cited by item-0022's reports` retitled `## 2. Statements extracted from the anchor` | -- |
| I1 L37 | Section 2.1 heading re-anchored to `### 2.1 Lemma 2 and its r=1 remark (p.6)` | p.6 |
| I1 L240 + verbatim prose + row pointer | The paragraph `**Report 1's claim, reassessed.**` was deleted whole, **together with the German-language quotation of report 1 it carried and the checklist-row pointer that closed it**. One operation, not three: a severance that kept the quotation would leave unattributable prose in the corpus, and one that kept the pointer would leave a pointer into a withdrawn register. | -- |
| I2 L15 | `against the dispatch` removed | p.1 |
| I2 L90, L149, L254, L255, L256, L260 | Six class-(a) disclaimers of operator-held documents deleted, including the FLAGS bullet that named the two documents. Nothing in the extract rested on them; the Section 2.3 revision is restated as resting on pp.6-8 of the anchor, which is where it was in fact tested. | pp.6-8 |

### 6.3 Two overstated verification assurances, removed

The grade's Section 6.5 found the extract's assurance that the (2.16)
block was "independently re-verified via pdftotext this session"
falsified for the line P27 names, since `pdftotext` returns the
uncancelled numerator. That assurance and its twin in Section 6 were
removed and replaced by statements of what was actually checked and
where. This is the same class of defect as the header assurance repaired
in Section 1 of this log.

### 6.4 What was preserved

The load-bearing transcription of (2.10) -- exponent 2, no cardinality
restriction -- is **unchanged**, as are (2.8), (2.9), (2.11),
(2.13)-(2.15), the reconstructed Lemma 2 display, and the extract's own
induction. All verified byte-for-byte. The extract's Section 6 reading
of the anchor stands where it stood.

---

## Section 7 -- precedent-p1-2605.22763.md

Anchor: `2605.22763v2.pdf`, 60 pages.

| # | repair | checked against |
| --- | --- | --- |
| C9, C10, C11 | One block introduced `p.9, Section 5:` joined two sentences with an ellipsis. They are printed six pages apart: the first opens Section 5 on p.8, the second is in the Introduction on p.2. Section 5 begins on p.8, not p.9. Split into two separately cited quotations, and the ellipsis that asserted contiguity is gone. | p.8 (Section 5, "Impact of Agent Architecture and Model"); p.2 (Section 1, Introduction) |
| C15, C16 | The availability sentence was cited to p.1 and printed without the `www.` component. Both corrected. | p.2 |
| C18 | "Even most Erdos problems remain out of reach" was cited to p.10; it is printed on p.11. Corrected. | p.11 (Section 6 "Discussion" begins on p.10) |
| I1 L52 | `## 2. Statements cited by item-0022's reports` retitled `## 2. Statements extracted from the anchor` | -- |
| I1 L54 | Section 2.1 heading re-anchored to `(Introduction, pp.1-2)` | pp.1-2 |
| I1 L62 | Section 2.2 heading re-anchored to `(Introduction p.2; Section 5, p.8)` | p.2, p.8 |
| I1 L73 | Section 2.3 heading re-anchored to `(Section 2, p.2; p.4)` | p.2, p.4 |
| I1 L81 | Section 2.4 heading re-anchored to `(Introduction, p.2)` | p.2 |
| I2 L18 | **Class (c).** The self-label "precedent P1 (Appendix C.1)" is carried by nothing at any anchor. Per the grade it is deleted, not re-anchored. Deleted. | -- |
| I2 L21 | `kickoff dispatch` removed | p.1 |

The severed forms for the 2.2, 2.3 and 2.4 headings fold in the page
repairs, exactly as the grade specifies; heading and page repair were
one operation for those three.

---

## Section 8 -- precedent-p3-2601.07421.md

Anchor: `2601.07421v5.pdf`, 20 pages.

| # | repair | checked against |
| --- | --- | --- |
| T7 | The Lean-correspondence quotation was cited to p.2; it opens Section 6 on p.10. Corrected to "p.10, Section 6 (Correspondence with the Lean development)". | p.10 |
| T11 | The FLAGS description of the bounded read said "title page through the start of Section 4". Corrected to "title page through the opening of Section 6", and the description of what was not read corrected with it. | Section layout read from the PDF: Section 2 p.3, Section 3 p.4, Section 4 p.6, Sections 5 and 6 both p.10 |
| I1 L37 | `## 2. Statement cited by item-0022's reports` retitled `## 2. Statement extracted from the anchor` | -- |
| I1 L39 | Section 2.1 heading re-anchored to `(abstract, p.1; Section 6, p.10)` | p.1, p.10 |
| I2 L12 | **Class (c).** The self-label "precedent P3 (Appendix C.1)" is deleted, not re-anchored. | -- |
| I2 L15 | `kickoff dispatch` removed | p.1 |

---

## Section 9 -- the inventory, re-run at close

The inventory is the evidence that the severance happened. It is
**expected** to move, and this is the one gate whose change is the
intended outcome. The inventory file itself was not edited; only its
regenerated counts are quoted.

| extract | I1 | I2 | I3 | I4 | lines | fenced |
| --- | --- | --- | --- | --- | --- | --- |
| bloomkuperberg23-oddmoments.md | 3 -> 0 | 2 -> 0 | 4 -> 0 | 3 -> 1 | 78 -> 87 | 1 -> 1 |
| kowalski-singser-dist.md | 1 -> 0 | 1 -> 0 | 5 -> 0 | 2 -> 3 | 200 -> 210 | 9 -> 9 |
| kuperberg21-oddmoments.md | 3 -> 0 | 2 -> 0 | 1 -> 0 | 2 -> 1 | 94 -> 95 | 3 -> 3 |
| kuperberg23-apsmooth.md | 4 -> 0 | 1 -> 0 | 0 -> 0 | 2 -> 1 | 90 -> 89 | 1 -> 1 |
| pintz10-patterns.md | 3 -> 0 | 7 -> 0 | 1 -> 0 | 3 -> 2 | 275 -> 279 | 11 -> 11 |
| precedent-p1-2605.22763.md | 5 -> 0 | 2 -> 0 | 0 -> 0 | 1 -> 1 | 114 -> 118 | 0 -> 0 |
| precedent-p3-2601.07421.md | 2 -> 0 | 2 -> 0 | 0 -> 0 | 2 -> 2 | 70 -> 71 | 0 -> 0 |
| **total** | **21 -> 0** | **17 -> 0** | **11 -> 0** | **15 -> 11** | **921 -> 949** | **25 -> 25** |

Extracts carrying at least one I1 match: 7 of 7 -> 0 of 7.
Extracts carrying at least one I2 match: 7 of 7 -> 0 of 7.
Extracts carrying at least one I3 match: 4 of 7 -> 0 of 7.
Extracts carrying none of I1, I2, I3: 0 of 7 -> **7 of 7**.

**The fenced/display line count is unchanged at 25.** That is the
mechanical check that no display was added or removed. It was
supplemented by a byte-comparison of every display block against the
pin: six of the seven extracts have all displays byte-identical, and
pintz10 has exactly one changed line, the (2.16) middle numerator that
P27 names. Zero displays or numbered objects marked PASS were changed.

The I4 movement (15 -> 11) is the in-tree cross-reference axis. It falls
because checklist-row pointers were removed inside paragraphs the grade
ordered deleted (kuperberg21 R1-007, kuperberg23 R1-013, pintz10
R1-015), and rises by one in kowalski where the in-tree
`payloads/HASHES.txt` record replaced a dispatch reference.

---

## Section 10 -- STOP-AND-REPORT, all seven reported

| stop | fired | detail |
| --- | --- | --- |
| S1 | NO | HEAD equals the pin; no rule-18 delta. |
| S2 | NO | Both Appendix B anchors matched exactly once. |
| S3 | NO | Last annotation `ANN-20260728-78`; item-0033 ratified at position 1; grade file unmodified. |
| S4 | NO | No repair required a dropped, ephemeral or operator-held object. No repair would have changed a display or numbered object marked PASS. |
| S5 | NO | Every gate other than the inventory diff produces its start-of-pass output at close. See Section 11. |
| S6 | NO | No hash line added. No write to `roadmap/`, `lean/`, `runs/`, `writeup/`, the checklist, the inventory file, the grade file, or `payloads/HASHES.txt`. |
| S7 | **YES -- three findings** | See Section 10.1. Not a stop for the pass; logged for the re-grade and reported prominently. |

### 10.1 -- S7: three defects ANN-78 did not record

**These mean the first grade was not complete. The re-grade must be told
where to look.** None was repaired in this pass, except where a
mandatory close gate compelled it (S7-1); the repair pass discharges a
known spec and does not re-open grading.

**S7-1. A non-ASCII line inside a quotation, in an extract declaring
"ASCII-folded per AGENTS.md".** `pintz10-patterns.md` line 99 carried
`U+03A0 GREEK CAPITAL LETTER PI` followed by `U+2081 SUBSCRIPT ONE` in
the (2.16) lead-in quotation. The ANN-78 grade marked that line PASS
(check P25) and recorded nothing. The dispatch's own close gate requires
every extract file to be ASCII-only, so this one **was** repaired -- to
the inline form $`\Pi_1(h)`$, matching the notation the display directly
below it already used -- and it is disclosed here rather than fixed
silently. The
ASCII gate consequently returns 0 at close where it returned 1 at start,
for this file only; every other extract was 0 at both.

**S7-2. An uncounted report reference that survives all three inventory
axes.** `kuperberg23-apsmooth.md` carries `(report 1's "Input (i)")` in
its NOT-FOUND probe, split across a line break as `report` / `1's`. The
inventory's I1/I2/I3 patterns match on a single line and therefore never
saw it, so the grade never dispositioned it. It is still in the file.
The extract now reports 0 on all three axes while still containing a
reference to a dropped report. **The inventory's zero is not proof of
severance.** The re-grade should treat the axes as a lower bound and
sweep line-break-tolerantly.

**S7-3. A second uncounted ephemeral reference.**
`precedent-p1-2605.22763.md`, in its NOT-FOUND probe, reads "Consistent
with Appendix C.1's ANCHORED-BY-COMMIT class for P2, this item's row is
WEB-DEFERRED per STOP 7.8". Appendix C.1 is the same object whose
`precedent P1` label the grade classified as (c) load-bearing and
unreplaceable and ordered deleted at L18. This second reference to it
was not counted on any axis and not dispositioned. It is still in the
file. It is very likely a third class-(c) reference, and the re-grade
should decide it on the same footing as the two the grade did find.

### 10.2 -- two errors in the ANN-78 grade's own prose

Neither changes a repair; both are recorded so the re-grade does not
inherit them.

- Grade Section 2.2, check B10 detail states that `2312.09021v2.pdf`
  "p.38 prints its corresponding entry as [17]". Reference [17] is
  printed on **p.37**; p.38 carries references [21] and [22]. The
  repair uses p.37.
- Grade Section 8.2, check T11 detail states that in
  `2601.07421v5.pdf` "Section 5 [begins] on p.9". Section 5
  ("Completion of the proof") begins on **p.10**, as does Section 6.
  The repair text the grade prescribes -- "title page through the
  opening of Section 6" -- is unaffected and was used as written.

### 10.3 -- a defect in the dispatch's own gate line

The Section 4 gate line

```
python3 dossier/item-0022-workpapers/extract-inventory.py && diff -q <output> dossier/item-0022-workpapers/extract-inventory-r1.md
```

assumes `extract-inventory.py` emits to stdout. It does not: it
**writes `dossier/item-0022-workpapers/extract-inventory-r1.md` in
place**. Running it as written therefore overwrites the very file it is
meant to diff against, and would have edited the inventory file, which
S6 forbids.

Running the script overwrote the inventory file once. It was restored
immediately with `git checkout --`, and `git status --porcelain` for
that path is empty at close: the file is byte-identical to the pin. The
regenerated output was kept outside the repository and its counts are
quoted in Section 9. **The inventory file is unmodified by this apply.**

---

## Section 11 -- gates

Run at start and at close.

| gate | start | close |
| --- | --- | --- |
| `blocks.py check-frozen` | all byte-identical | all byte-identical |
| `blocks.py relocation-check` | PASSED | PASSED |
| `grep -rnE '^\s*sorry\s*$' lean/Erdos251/` | 1 (`Statement.lean:21`) | 1 (`Statement.lean:21`) |
| `grep -c a6276f4c... lean/lake-manifest.json` | 1 | 1 |
| `tail -c 1 lean/lean-toolchain \| od -c` | `\n` | `\n` |
| `roadmap.py show item-0033` | ratified, rank 0100 | ratified, rank 0100 |
| `writeup_mapper.py check` | PASS | PASS |
| `mathjax_lint.py` | 138 files, 0 problems | 138 files, 0 problems |
| ASCII, seven extracts | 0 except pintz10 = 1 | 0, all seven |
| ASCII, `HANDOVER.md` | 0 | 0 |
| ASCII, this repair log | n/a | 0 |
| inventory | 21 / 17 / 11 | 0 / 0 / 0 -- **expected to move** |

The ASCII row is the only gate other than the inventory whose output
differs between start and close, and the difference is the S7-1 repair
that the gate itself compels. It is reported rather than absorbed.

---

## Section 12 -- what this pass did not do

- It hashed nothing. Not an extract, not this log. Standing is the
  re-grade's to confer.
- It did not open a dropped report, the kickoff dispatch, or an
  operator-held PDF.
- It did not change a display or numbered object the grade marked PASS.
  Verified mechanically, per Section 9.
- It did not edit the grade file, the inventory file, the checklist, or
  `payloads/HASHES.txt`.
- It did not re-verdict any claim row.
- It did not close item-0033.
- It did not repair the three S7 findings, except where a mandatory
  close gate compelled it and the exception is disclosed.

## Section 13 -- the re-grade this pass hands off to

Before the analysis lane may consume any of these seven, and before
item-0033 can close, the Phase 2b dispatch is re-run against the
repaired extracts by a **fresh executor session that did not perform
this repair**, cross-family preferred, with the pin bumped to this
pass's commit. It grades on the full ANN-78 fidelity surface, fresh, not
as a diff against this log; it exhibits `pdftotext` output alongside
every quotation it grades CLEAN; and on CLEAN it hashes the extract and
the re-grade record. An extract that does not re-grade CLEAN returns
here.

It should additionally read Section 10.1 before starting: three defects
this pass found are undischarged, and one of them means the inventory's
zero counts cannot be taken as proof of severance.
