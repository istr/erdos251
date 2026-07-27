# item-0022 extract grades r1 -- graded against the anchored PDFs

Phase 2b of the item-0033 disposition chain. Executed by the local executor
under an ephemeral dispatch pinned to `91dec12`, never committed; the
operator apply is the ratifying commit.

**This is the pass that opened the PDFs.** Every prior item-0022 apply was
forbidden from opening a primary source. Every fidelity judgement below was
made by reading the anchored PDF at the cited location and comparing it with
the extract. No judgement rests on an extract's own account of itself.

**Scope.** Exactly the seven extracts inventoried in
`extract-inventory-r1.md` at `91dec12`: 921 lines, 21 I1 findings, 17 I2, 11
I3, 15 I4, 25 display-fenced lines. No scope was added. No extract file was
edited. No checklist row was touched. No claim row was re-verdicted. The
inventory was re-run and reproduces byte-for-byte; it was not modified.

**What was NOT opened.** The three dropped reports, the item-0022 kickoff
dispatch, and the two operator-held Pintz documents. Not once, not to check
a reference, not to resolve an attribution. Where an extract asserts
something about one of those objects, that assertion is graded as a
provenance defect in the extract, by reading the extract and the anchor
only. No content of any dropped report is restated here; where an extract
carries report prose, this file names the location and the character of the
quotation and does not reproduce it.

---

## Section 0 -- the standard applied

Three grades, per the dispatch rubric. Because no extract was severed in
this apply, no extract could reach CLEAN even on a perfect fidelity record;
the live question for each was CLEAN-PENDING versus DEFECTIVE.

The fidelity surface graded is the one the rubric names -- every transcribed
formula, every theorem / lemma / equation number, every page citation, every
quoted phrase -- plus every other claim the extract makes **about the
anchor** (NOT-FOUND probes, uniformity-ledger entries, header facts),
because those are assertions the PDF can adjudicate and a later reader will
rely on. A FAIL is a claim the PDF contradicts. The rubric's DEFECTIVE
threshold is one unfaithful transcription, so any FAIL carries the extract
to DEFECTIVE.

Three classes of deviation are recorded as FAIL and should be read with
their weight, not flattened:

- **Fabricated location.** The extract cites a page, section or labelled
  block that does not carry the quoted object. The object is printed
  elsewhere in the same PDF.
- **Altered quotation.** Text inside quotation marks differs from what the
  source prints -- an inserted connective, a silent deletion, a performed
  cancellation, a repaired typo, a dropped limit.
- **Contradicted assertion.** A NOT-FOUND probe or a scope statement that
  the PDF refutes.

Deviations that the extract's own declared conventions license -- ASCII
folding of diacritics and of mathematical glyphs, truncation of a quotation
at a sentence boundary, omission of an intervening remark -- are recorded as
notes, not fails.

## Section 0a -- tooling, disclosed

`pdftotext -layout` and `pdftotext` (raw) for the text layer, `pdfinfo` for
metadata and page counts, `sha256sum` for the anchor identity check, and
`pdftoppm -r 200 -png` for rendered page images. The rendered images matter
in one place and are named there: two of the Pintz findings turn on whether
a printed glyph is a capital O or a digit zero, and the text layer alone
cannot settle that. Pages 6, 7 and 8 of `1004.1072v1.pdf` were rendered and
read as images to settle it.

## Section 0b -- anchor identity, checked before any grading

All seven anchors: file sha256 equals both the value printed in the extract
header and the line booked in `payloads/HASHES.txt`. 7 of 7. Declared page
counts equal `pdfinfo` page counts. 7 of 7. Declared PDF metadata (Creator,
Producer, CreationDate, Author where claimed) matches `pdfinfo`. 7 of 7.

| extract | anchor | sha256 (prefix) | pages declared / actual |
| --- | --- | --- | --- |
| bloomkuperberg23-oddmoments.md | 2312.09021v2.pdf | 46b80c9b | 38 / 38 |
| kowalski-singser-dist.md | singular-series-distribution.pdf | 378433db | 30 / 30 |
| kuperberg21-oddmoments.md | 2109.03767v3.pdf | e1bbabbd | 51 / 51 |
| kuperberg23-apsmooth.md | 2301.06095v1.pdf | c67fdd9c | 19 / 19 |
| pintz10-patterns.md | 1004.1072v1.pdf | 74824028 | 9 / 9 |
| precedent-p1-2605.22763.md | 2605.22763v2.pdf | d71b78f1 | 60 / 60 |
| precedent-p3-2601.07421.md | 2601.07421v5.pdf | fb1bccdb | 20 / 20 |

---

## Section 1 -- the grades

| extract | grade | reason, one line |
| --- | --- | --- |
| bloomkuperberg23-oddmoments.md | DEFECTIVE | NOT-FOUND probe contradicted on p.4; header quotes a bibliography entry this anchor does not print |
| kowalski-singser-dist.md | DEFECTIVE | three page citations name pages that do not carry the quoted objects; one verbatim block silently deletes and rewrites source text |
| kuperberg21-oddmoments.md | DEFECTIVE | uniformity-ledger page citation wrong; NOT-FOUND scope statement contradicted; one comparison rests entirely on a dropped object |
| kuperberg23-apsmooth.md | DEFECTIVE | quoted passage attributed to a "Remark" that is a different paragraph; unmarked insertion inside the quotation; names a Theorem 1.4 the paper does not have |
| pintz10-patterns.md | DEFECTIVE | the (2.16) block introduced as verbatim performs a cancellation the source leaves unperformed; four further altered quotations |
| precedent-p1-2605.22763.md | DEFECTIVE | one quotation splices passages six pages apart under a single wrong section citation; two further wrong pages; quoted URL drops a printed component |
| precedent-p3-2601.07421.md | DEFECTIVE | the Lean-correspondence quotation is cited to p.2 and is printed on p.10, in a different section |

**0 CLEAN. 0 CLEAN-PENDING. 7 DEFECTIVE.**

**The headline, stated plainly.** The mathematics these extracts transcribe
is, with one exception, faithful. Every displayed formula that transcribes a
source display was checked against the PDF and reproduces it correctly,
except the second fraction of Pintz (2.16). Theorem, lemma and equation
numbers are correct throughout, in all seven. What fails is the citation
apparatus around the mathematics: page references that name the wrong page,
quotations that have been tidied, spliced, or silently extended, and
negative claims stated more broadly than the source supports. That is a
consistent signature, and it is what a pass that never opened the sources
would produce.

**Nothing was hashed.** No extract graded CLEAN, so by the dispatch's Lane B
rule -- "nothing if nothing is clean" -- no hash line was added for any
extract, and none for this grade file either.

---

## Section 2 -- bloomkuperberg23-oddmoments.md

**Grade: DEFECTIVE.** Its one transcribed display and its one long quotation
are exact, but its NOT-FOUND probe is contradicted by p.4 of its own anchor
and its header attributes to this anchor a bibliography entry that a
different anchor prints.

### 2.1 Fidelity checks

| # | extract location | what was checked | PDF location | verdict |
| --- | --- | --- | --- | --- |
| B1 | L3-L4 | source path, sha256 | file | PASS |
| B2 | L10-L13 | 38 pages, Creator, Producer, Author field | `pdfinfo` | PASS |
| B3 | L13 | "No journal reference is printed" | whole PDF | PASS |
| B4 | L16-L17 | authors and title, as identification | p.1 title block | PASS |
| B5 | L30-L40 | front-matter quotation (title, authors, whole abstract) | p.1 | PASS |
| B6 | L46 | "p.4, Theorem 2" | p.4 | PASS |
| B7 | L48 | the Theorem 2 display | p.4 | PASS |
| B8 | L50-L53 | the paragraph following Theorem 2, quoted | p.4 | PASS |
| B9 | L61-L63 | implied-constant footnote, quoted | p.1 footnote 1 | PASS |
| B10 | L7-L10 | quoted bibliography entry for Kuperberg 2021 | p.38 ref [17] | **FAIL** |
| B11 | L67-L68 | NOT-FOUND: no claim about even-order moments of the refined singular series | p.4 | **FAIL** |
| B12 | L69-L70 | NOT-FOUND: "the paper's scope ... is the odd-order moments of $`R_k(h)`$ only" | p.1, p.4, p.5 | **FAIL** |
| B13 | L68-L69 | NOT-FOUND: no uncentered second moment $`\sum \mathfrak{S}(H)^2`$ | whole PDF | PASS |

Display-fenced lines in this extract: 1 (B7). Checked.

### 2.2 The fails, in detail

**B10.** L7-L10 sources the "original submission 2023" reading to "anchor
3's bibliography" and quotes it as

```
V. Kuperberg, Odd moments in the distribution of primes, arXiv:2109.03767, 2021
```

That string is not printed in this anchor. `2312.09021v2.pdf` p.38 prints
its corresponding entry as

```
[17] V. Kuperberg. Odd moments in the distribution of primes, Algebra Number Theory
     19 (2025), no. 4, 617-666.
```

-- a journal reference, no arXiv identifier, no year 2021. The quoted string
**is** printed, verbatim, in a different member of the anchor set:
`2301.06095v1.pdf` p.19, reference [4]. The defect is therefore not that the
string is invented but that it is attributed by an index ("anchor 3") into a
numbering that no longer exists in the tree, and the attribution lands on the
wrong anchor. Repair: cite the anchor by identifier -- `2301.06095v1` ref [4]
-- not by ephemeral index. The same string, with the same defect, recurs in
`kuperberg21-oddmoments.md` (check K13 below), where it is attributed to
"anchor 4".

**B11.** L67-L68 asserts that NOT present in this paper is "any claim about
the *even*-order moments of the refined singular series". p.4 prints:

> When k is even Montgomery and Soundararajan [19] proved an asymptotic for
> $`R_k(h)`$ of the shape $`R_k(h) \sim \mu_k(-h\log{h})^{k/2}`$ for some
> explicit constant $`\mu_k > 0`$, which implies Gallagher's estimate for
> the average of $`\mathfrak{S}`$.

That is a claim about the even-order moments of the refined singular series,
present in this paper, attributed to [19]. Repair: restrict the probe to the
paper's own results -- "no even-order result is proved here; the even-k
asymptotic on p.4 is quoted from Montgomery-Soundararajan [19]".

**B12.** The same sentence asserts "the paper's scope (per its own abstract
and Theorem 2) is the odd-order moments of $`R_k(h)`$ only". The abstract
itself names two further objects: the odd moments of $`M_k(q,h)`$, the
distribution of coprime residues in short intervals (Theorem 1, p.2), and
the counting bound for solutions of a rational linear equation (Theorem 3,
p.4). $`R_k(h)`$ is one of three objects, not the only one. Repair: name the
three and scope the probe to the singular-series half.

**B13 passes and is worth recording as a pass.** The uncentered second
moment $`\sum \mathfrak{S}(H)^2`$ appears nowhere in the 38 pages. The half
of the probe that carries item-0026's A3 reasoning is sound.

### 2.3 I1 disposition (3 headings)

| line | verbatim heading or annotation | severed, source-anchored form |
| --- | --- | --- |
| L42 | `## 2. Statement cited by item-0022's reports (verbatim)` | `## 2. Statement extracted from the anchor (verbatim)` |
| L44 | `### 2.1 The near-optimal odd-moment bound for the refined singular series (report 1's "nahe optimale obere Schranken" claim)` | `### 2.1 The near-optimal odd-moment bound for the refined singular series (Theorem 2, p.4)` |
| L55 | `confirms report 1` (in "This confirms report 1's claim: the paper does prove a near-optimal ...") | delete the framing clause; the surviving sentence states what Theorem 2 proves, with no addressee |

None of the three touches the transcribed content beneath it. Severance is
recorded, not applied.

### 2.4 I2 disposition (2 references)

| line | matched text | kind | anchor location that replaces it, or reason |
| --- | --- | --- | --- |
| L9 | `item-0022 kickoff dispatch` | (b) removable duplicate | the identification of 2312.09021 as the Bloom-Kuperberg paper is printed on p.1 (title block, author line, arXiv stamp) and in the PDF Author metadata |
| L15 | `against the dispatch` | (b) removable duplicate | every identification fact named -- authors, title, identifier -- is printed on p.1 |

No (c). The extract's DEFECTIVE grade rests on fidelity, not on I2.

### 2.5 I3 note (4 bare mentions)

L18, L75, L76, L78. **Two of the four carry evidentiary weight and are
flagged.** L18 and the L75-L78 cluster both assert that report 1's own
bibliography carries no URL for this paper. That is an assertion about a
dropped object; it cannot be checked at any pin. It is not, however,
unreplaceable: the same fact is recorded in-tree at `HANDOVER.md` (the
ANN-74 bullet) and in `roadmap/completed/item-0022.md`. Repair: cite the
in-tree record, or drop the sentence. The remainder of the L75-L78 sentence
-- that the claim is confirmed against this anchor without reference to what
report 1 says -- is a disclaimer and survives severance unchanged.

---

## Section 3 -- kowalski-singser-dist.md

**Grade: DEFECTIVE.** Every formula it transcribes is exact and every
numerical value reproduces to the printed digit, but three of its six page
citations name a page that does not carry the object, one verbatim block
deletes a source cross-reference and rewrites a sentence, and one NOT-FOUND
clause is contradicted on p.3.

### 3.1 Fidelity checks

| # | extract location | what was checked | PDF location | verdict |
| --- | --- | --- | --- | --- |
| W1 | L3-L4 | source path, sha256 | file | PASS |
| W2 | L11-L14 | 30 pages, Creator, Producer, CreationDate | `pdfinfo` | PASS |
| W3 | L17-L19 | title as printed on page 1 | p.1 | PASS |
| W4 | L21-L23 | "PDF page numbering matches the paper's own printed page numbers 1-30 exactly" | pp.1-30 headers | PASS |
| W5 | L36-L46 | front-matter quotation (title, author, whole abstract) | p.1 | PASS |
| W6 | L48-L50 | affiliation line, "last page of the paper" | p.30 | PASS |
| W7 | L56 | page citation "p.1" for the singular-series definition | printed on **p.2**, eq. (1.1) | **FAIL** |
| W8 | L59 | the (1.1) display, both Euler-product forms | p.2 | PASS |
| W9 | L65 | page citation "p.5" for Theorem 1.1 | printed on **p.3** | **FAIL** |
| W10 | L65-L80 | the Theorem 1.1 statement and the sentence following it | p.3 | PASS |
| W11 | L84 | page citation "p.5, eq. (1.5)" for Gallagher | printed on **p.3** | **FAIL** |
| W12 | L86-L89 | the (1.5) display and its qualifying clause | p.3 | PASS |
| W13 | L93 | "p.15, Example 3.5" | p.15 | PASS |
| W14 | L96 | the mean-square limit display | p.15 | PASS |
| W15 | L100 | the $`\mu_k(2)`$ Euler-product display | p.15 | PASS |
| W16 | L104 | the five numerical values $`\mu_2(2)`$ through $`\mu_6(2)`$ | p.15 | PASS |
| W17 | L106-L112 | the parity-vanishing paragraph, quoted | p.15 | **FAIL** |
| W18 | L116 | "p.15, Proposition 4.1" | p.15 | PASS |
| W19 | L118 | the Proposition 4.1 display | p.15 | PASS |
| W20 | L122 | "p.18, Example 4.3" | p.18 | PASS |
| W21 | L125 | the Example 4.3 display | p.18 | PASS |
| W22 | L131-L138 | method anatomy: Proposition 2.1, the $`X_p`$ / $`Y_p`$ model, $`\Omega_2`$, the (3.10) closed form | p.8 (Prop 2.1), p.11-p.12, p.15 | PASS |
| W23 | L139-L141 | "splitting the product at $`p<km`$ and $`p\ge km`$" | p.17 | PASS |
| W24 | L142-L144 | Section 5 proves Theorem 1.3, conditional on a uniform Bateman-Horn hypothesis | p.5, Section 5 | PASS |
| W25 | L148-L158 | uniformity ledger: fixed k, integer symmetry, m-asymptotic, exact $`2^{1-k}`$ | p.3, p.15, p.15 | PASS |
| W26 | L169-L170 | NOT-FOUND: [MS] "cited only in this paper's own bibliography" | **p.3, in the body** | **FAIL** |
| W27 | L170 | NOT-FOUND: no Montgomery-Soundararajan $`R_k(h)`$ theorem restated or proved here | whole PDF | PASS |
| W28 | L162-L167 | NOT-FOUND: no per-position $`(1+o(1))^k`$ constant in a growing-k regime | p.15, p.18 | PASS |
| W29 | L169 | NOT-FOUND: no "flanked" or "aggregated simplex" domain | whole PDF | PASS |
| W30 | L170-L173 | the ratio $`1.1504807723\ldots`$ is not printed in this paper | whole PDF | PASS |

Display-fenced lines in this extract: 9 (W8, W12, W14, W15, W16, W19, W21,
and the two-line displays inside W10). Checked.

### 3.2 The fails, in detail

**W7, W9, W11 -- three fabricated locations.** The extract's own header
establishes that PDF page N is printed page N, and that is true. Against
that grid:

| extract cites | object | actually printed on |
| --- | --- | --- |
| p.1 | the singular-series definition, eq. (1.1) | p.2 |
| p.5 | Theorem 1.1 | p.3 |
| p.5 | eq. (1.5), Gallagher's theorem | p.3 |

PDF page 1 carries the abstract, the opening of Section 1, the definition of
$`\pi(N;\mathbf{h})`$ and of $`\nu_p(\mathbf{h})`$ -- and stops before (1.1).
PDF page 5 carries the close of Section 1 (the notation paragraph) and the
opening of Section 2; it names "Theorem 1.1" once, in the sentence "we use
it to prove Theorem 1.1 and Theorem 1.2 in Sections 3 and 4", which is a
forward reference, not the statement. The transcribed content in all three
cases is exact; only the addresses are wrong. Repair: p.1 -> p.2, p.5 -> p.3
(twice).

**W17 -- altered quotation.** L106-L112 is inside the block introduced as
`p.15, Example 3.5:` and opened with a quotation mark. The source prints:

> Note that the second (and higher) moments increase quickly with k (as
> proved in Proposition 4.1 in the next section). This is explained
> intuitively by the fact that $`\mathfrak{S}(\mathbf{h})`$ is often zero:
> for instance, the 2-factor of $`\mathfrak{S}(\mathbf{h})`$ is zero unless
> all $`h_i`$ are of the same parity, which happens with probability
> $`2^{1-k}`$ only (see Example 4.3 for a more precise estimate). For those,
> of course, the 2-factor is very large (equal to $`2^{k-1}`$).

The extract prints "... which happens with probability $`2^{1-k}`$ only (for
those, of course, the 2-factor is very large, equal to $`2^{k-1}`$)." Two
changes, both unmarked: the source's cross-reference "(see Example 4.3 for a
more precise estimate)" is deleted with no ellipsis, and the source's
following independent sentence is folded into the parenthesis that replaced
it. The deletion is the more consequential of the two -- it removes the
source's own signal that $`2^{1-k}`$ is not its last word on the question,
which is exactly the kind of qualifier the evidence discipline exists to
preserve. Repair: restore both, or mark the elision.

**W26 -- contradicted assertion.** L169-L170 says the Montgomery-
Soundararajan result "is cited only in this paper's own bibliography, entry
[MS]". p.3 cites it in the body: "This property was used by Gallagher
himself to understand the behavior of primes in short intervals (see also
the recent work by Montgomery and Soundararajan [MS])". The substantive half
of the probe -- that no $`R_k(h)`$ theorem is restated or proved in this
paper -- is correct and survives (W27). Repair: "[MS] is cited in the body
at p.3 and in the bibliography; the theorem itself is neither stated nor
proved here."

### 3.3 I1 disposition (1 heading)

| line | verbatim heading | severed, source-anchored form |
| --- | --- | --- |
| L52 | `## 2. Statements cited by item-0022's reports (verbatim, in reading order)` | `## 2. Statements extracted from the anchor (verbatim, in reading order)` |

### 3.4 I2 disposition (1 reference)

| line | matched text | kind | anchor location that replaces it, or reason |
| --- | --- | --- | --- |
| L16 | `against the dispatch` | (b) removable duplicate | author and title as printed on p.1; the URL is carried in-tree by `payloads/HASHES.txt` line 83 |

No (c).

### 3.5 I3 note (5 bare mentions)

L172, L173, L179, L182, L187. **All five sit in one connected argument and
the cluster carries evidentiary weight; it is flagged.** L170-L175 (the
NOT-FOUND tail) and L179-L188 (Section 6) together attribute to report 1 a
numerical value and two derived quantities, and then assess that derivation
as correct. The attribution cannot be checked at any pin.

It is, however, replaceable rather than load-bearing, and that distinction
is what keeps this out of STOP S7. Everything the argument needs from the
anchor is confirmed against the anchor: the $`\mu_k(2)`$ Euler product and
its numerical values (W15, W16) and the exact parity-vanishing probability
(W25). The arithmetic itself is reproduced in-tree in
`kowalski-mu-recheck.py` / `.txt`, which the inventory counts as I4. Repair:
state the derivation as this project's, from the anchored ingredients, and
drop the attribution.

---

## Section 4 -- kuperberg21-oddmoments.md

**Grade: DEFECTIVE.** Its three transcribed displays and its abstract are
exact and correctly numbered and paged, but one uniformity-ledger citation
names the wrong page for a statement it also strengthens, its NOT-FOUND
scope sentence is contradicted by the paper's own definitions and theorems,
and its central corroboration sentence is a comparison whose second term is
a dropped object.

### 4.1 Fidelity checks

| # | extract location | what was checked | PDF location | verdict |
| --- | --- | --- | --- | --- |
| K1 | L3-L4 | source path, sha256 | file | PASS |
| K2 | L6 | "arXiv:2109.03767v3 [math.NT] 29 Jul 2024" | p.1 arXiv stamp | PASS |
| K3 | L10-L13 | 51 pages, Creator, Producer, CreationDate | `pdfinfo` | PASS |
| K4 | L13 | "No journal reference is printed on the paper" | whole PDF | PASS |
| K5 | L16-L17 | author, title, identifier as identification | p.1 | PASS |
| K6 | L27-L38 | front-matter quotation (title, author, whole abstract) | p.1 | PASS |
| K7 | L44 | "p.3 (Section 1, eq. (4))" | p.3 | PASS |
| K8 | L47 | the eq. (4) display | p.3 | PASS |
| K9 | L49-L50 | the clause naming $`A = 2 - \gamma - \log{2\pi}`$ and the sentence after it | p.3 | PASS |
| K10 | L61 | "p.3, Conjecture 1.1" | p.3 | PASS |
| K11 | L61-L67 | Conjecture 1.1 statement, display, and the sentence on numerical evidence | p.3 | PASS |
| K12 | L69-L71 | "p.3, Theorem 1.2" and its display | p.3 | PASS |
| K13 | L8-L10 | quoted bibliography entry for this paper | not printed in this anchor | **FAIL** |
| K14 | L52-L57 | "byte-for-byte the same formula report 1 attributes ..." | not checkable against any anchored source | **FAIL** |
| K15 | L75-L77 | uniformity ledger: eq. (4) holds for any nonnegative k, any h>1, any eps>0 | p.3 | PASS |
| K16 | L78-L80 | "the paper states (p.4) it does not prove an asymptotic for $`R_k(h)`$ when k is odd" | nearest printed statement is on **p.3**, and is weaker | **FAIL** |
| K17 | L84-L86 | NOT-FOUND: no "flanked" / "aggregated simplex" domain, no uncentered $`\sum \mathfrak{S}(H)^2`$ | whole PDF | PASS |
| K18 | L86-L88 | NOT-FOUND: "the paper works throughout with the centered/refined singular series $`\mathfrak{S}_0`$ and its sums $`R_k(h)`$" | p.1, p.2, p.4 | **FAIL** |

Display-fenced lines in this extract: 3 (K8, K11, K12). Checked. All three
are exact.

### 4.2 The fails, in detail

**K13.** Identical in kind to check B10 in Section 2 above: the quoted
bibliography entry is printed in `2301.06095v1.pdf` p.19 reference [4], not
in this anchor and not in `2312.09021v2.pdf`. Here the attribution is
"anchor 4"; in the Bloom-Kuperberg extract the same string is attributed to
"anchor 3". At most one of the two indices can be right, and neither is
resolvable now, because the numbering lived in the kickoff dispatch. Repair,
in both places: cite `2301.06095v1` ref [4] by identifier.

**K14.** L52-L57 states that the transcribed eq. (4) is "byte-for-byte the
same formula report 1 attributes (via its own footnote 3, pointed at
arXiv:math/0409258 ...) to Montgomery-Soundararajan". The comparison has two
terms and one of them is gone. It cannot be checked now and could not be
checked by any later session. It is graded from the extract and the anchor
alone -- no dropped report was opened to grade it -- and the grade is that
the sentence is unverifiable and must be severed, not repaired.

The **substantive** half of the same sentence -- "this anchor restates the
identical theorem in its own introduction as the result it builds on" -- is
confirmed: eq. (4) is printed on p.3 as the Montgomery-Soundararajan
estimate this paper builds on (K7, K8, K9). Repair: keep the anchored half,
delete the comparison.

**K16.** The extract's uniformity ledger says "the paper states (p.4) it
does not prove an asymptotic for $`R_k(h)`$ when k is odd for any k, only an
upper bound". Two problems. The page: p.4 carries Theorems 1.3 and 1.4, both
about the function-field moments $`m_k(Q;h)`$ of reduced residues, and no
such statement. The strength: the nearest printed statement is on p.3 --
"For k odd, we do not know, even heuristically, which terms contribute to
the main term in $`R_k(h)`$; for this reason, we do not know what the
constant should be in front of the asymptotic in Conjecture 1.1" -- which
says the constant is unknown, not that no asymptotic is proved. The
extract's conclusion happens to be true (only Theorem 1.2's upper bound is
proved) but it is presented as the paper's own statement at a page that does
not carry it. Repair: cite p.3, quote what is printed, and mark the "only an
upper bound" reading as inference from Theorem 1.2.

**K18.** "The paper works throughout with the centered/refined singular
series $`\mathfrak{S}_0`$ and its sums $`R_k(h)`$" is contradicted three
ways by the anchor. p.1 defines the uncentered $`\mathfrak{S}(\mathcal{D})`$
and eq. (1) gives its exponential-sum form. p.2 states Gallagher's
uncentered average $`\sum_{\mathcal{D}\subset[1,h]}
\mathfrak{S}(\mathcal{D}) \sim \sum_{\mathcal{D}\subset[1,h]} 1`$ and the
inversion $`\mathfrak{S}(\mathcal{D}) = \sum_{\mathcal{J}\subseteq
\mathcal{D}} \mathfrak{S}_0(\mathcal{J})`$. p.4 states Theorems 1.3 and 1.4,
which are about $`m_k(Q;h)`$ in the function-field setting and involve
neither $`\mathfrak{S}_0`$ nor $`R_k(h)`$. The clause that actually carries
the item-0026 reasoning -- that no uncentered second moment
$`\sum \mathfrak{S}(H)^2`$ over a flanked simplex appears -- is separate,
and it passes (K17). Repair: keep K17's clause, drop the "works throughout"
generalization.

### 4.3 I1 disposition (3 headings)

| line | verbatim heading or annotation | severed, source-anchored form |
| --- | --- | --- |
| L40 | `## 2. Statements cited by item-0022's reports (verbatim)` | `## 2. Statements extracted from the anchor (verbatim)` |
| L59 | `### 2.2 The odd-moment conjecture and upper bound (report 1's "obere Schranken bzw. numerische Evidenz" claim)` | `### 2.2 The odd-moment conjecture and upper bound (Conjecture 1.1 and Theorem 1.2, p.3)` |
| L88 | `matching report 1` (in the NOT-FOUND probe at L88-L90) | delete the clause **and the German-language quotation of report 1 that it introduces**; the probe's surviving sentence stands on K17 alone |

**L88 is the heaviest of the twenty-one.** The annotation does not merely
frame extracted content -- it introduces a verbatim quotation of report 1's
prose, carried in the extract at L88-L90. Severing the annotation without
removing the quotation would leave dropped-report prose in the corpus with
its provenance marker stripped, which is worse than leaving it marked. The
quotation is not reproduced in this file; its location and character are
named and that is the whole of the finding.

### 4.4 I2 disposition (2 references)

| line | matched text | kind | anchor location that replaces it, or reason |
| --- | --- | --- | --- |
| L8 | `item-0022 kickoff dispatch` | (b) removable duplicate | the 2021 submission is carried by the arXiv identifier 2109 printed on p.1, and the bibliography entry named in K13 is printed in `2301.06095v1` p.19 ref [4] |
| L15 | `against the dispatch` | (b) removable duplicate | author, title and identifier all printed on p.1 |

No (c).

### 4.5 I3 note (1 bare mention)

L52. **It carries evidentiary weight and is flagged**; it is the same site
as check K14 and is disposed of there.

---

## Section 5 -- kuperberg23-apsmooth.md

**Grade: DEFECTIVE.** This is the nearest of the seven to repairable: its
page citations are all correct, its Theorem 1.1 display -- the longest
transcribed formula in the set outside Pintz -- is exact down to the error
term's exponent, and it has no formula deviations at all. It fails on three
citation-apparatus defects.

### 5.1 Fidelity checks

| # | extract location | what was checked | PDF location | verdict |
| --- | --- | --- | --- | --- |
| A1 | L3-L4 | source path, sha256 | file | PASS |
| A2 | L6 | "arXiv:2301.06095v1 [math.NT] 15 Jan 2023" | p.1 arXiv stamp | PASS |
| A3 | L6-L9 | 19 pages, Creator, Producer, CreationDate | `pdfinfo` | PASS |
| A4 | L9-L10 | "No journal reference is printed on the paper" | whole PDF | PASS |
| A5 | L15-L18 | "a different paper from the anchored arXiv:2210.09775v2" | p.1 identifier and title | PASS |
| A6 | L28-L37 | front-matter quotation (title, author, whole abstract) | p.1 | PASS |
| A7 | L43 | "p.3, Theorem 1.1" | p.3 | PASS |
| A8 | L43-L49 | the Theorem 1.1 statement and its display, including the error term $`O_{r,k}(h^{k/2-1/(7k)}(q/\phi(q))^{2^k+k/2})`$ | p.3 | PASS |
| A9 | L51-L53 | "(p.3) $`\mathcal{B}_k`$ ... the set of perfect matchings of $`[1,k]`$" | p.3, eq. (8) | PASS |
| A10 | L55-L58 | "p.4, Theorem 1.2 ... perfect matchings $`\sigma \in \mathcal{B}(j+1,\ldots,k-j)`$ ... (eq. (9))" | p.4 | PASS |
| A11 | L63-L68 | the $`\#\widetilde{\mathcal{B}}`$ formula, as content | p.4 | PASS |
| A12 | L63 | attribution of that passage to "Theorem 1.2's remark" | p.4: it is the "In particular" continuation of the theorem; the paragraph labelled `Remark.` is a different one | **FAIL** |
| A13 | L65-L66 | the ellipsis and the words "the theorem implies" inside the quotation | p.4 | **FAIL** |
| A14 | L72-L74 | uniformity ledger: fixed $`r,k`$, constants depending on $`r`$ and $`k`$, no growing-k claim | p.3, p.4 | PASS |
| A15 | L81-L83 | NOT-FOUND: "This paper's results (Theorems 1.1-1.5)" | there is no Theorem 1.4 in this paper | **FAIL** |
| A16 | L78-L86 | NOT-FOUND: no Hardy-Littlewood-type lower bound for a prime-counting function; the results are asymptotic formulas for sums of the singular-series constant | whole PDF | PASS |

Display-fenced lines in this extract: 1 (A8). Checked, and exact.

### 5.2 The fails, in detail

**A12.** The quoted passage begins "In particular, if
$`\#\widetilde{\mathcal{B}}(c_1,\ldots,c_k)`$ is the number of ways to pair
the $`c_i`$'s such that every pair has equal values, then ...". On p.4 that
sentence is inside the Theorem 1.2 block, immediately after eq. (9). The
paragraph that the paper actually labels `Remark.` follows it and says
something else -- that when all the $`c_i`$ are congruent mod r,
$`\#\widetilde{\mathcal{B}} = \mu_k`$ and the theorem implies Theorem 2 of
[7]. Naming a labelled block that exists and does not contain the quoted
text is a fabricated location even though the page is right. Repair:
"Theorem 1.2's 'In particular' clause, p.4".

**A13.** In the same quotation the source's "..., then" is replaced by an
ellipsis followed by "the theorem implies", and that phrase sits inside the
quotation marks with no marker. It is the extract's own connective presented
as the source's words. Repair: bracket it, or restore "then".

**A15.** "This paper's results (Theorems 1.1-1.5)" names a range. The paper
states Theorem 1.1 (p.3), Theorem 1.2 (p.4), Theorem 1.3 (p.5) and Theorem
1.5 (p.5). There is no Theorem 1.4 anywhere in the 19 pages. This is the
mildest fail in this file and is recorded as such, but a range citation that
implies a numbered object the source does not have is still a citation the
PDF refutes. Repair: enumerate the four.

### 5.3 I1 disposition (4 headings)

| line | verbatim heading or annotation | severed, source-anchored form |
| --- | --- | --- |
| L39 | `## 2. Statement cited by item-0022's reports (verbatim)` | `## 2. Statement extracted from the anchor (verbatim)` |
| L41 | `### 2.1 The perfect-matching / pairing main-term structure (report 1's "matched-flank" analogy)` | `### 2.1 The perfect-matching / pairing main-term structure (Theorems 1.1 and 1.2, pp.3-4)` |
| L60 | `confirms report 1` (in "This confirms report 1's characterization: the main-term structure ...") | delete the framing clause; the surviving sentence states the main-term structure with no addressee |
| L84 | `matches report 1` (in "This matches report 1's own characterization of the gap ...") | delete the whole sentence; it adds nothing to the probe above it, which stands on A16 |

### 5.4 I2 disposition (1 reference)

| line | matched text | kind | anchor location that replaces it, or reason |
| --- | --- | --- | --- |
| L12 | `against the dispatch` | (b) removable duplicate | author, title and identifier all printed on p.1 |

No (c).

### 5.5 I3 note

The inventory records 0 I3 matches for this extract, and that is confirmed.
Note separately that the header at L15-L18 attributes a citation to "report
1's footnote 6", which is an assertion about a dropped object; the inventory
does not count it on any axis because the phrase carries no `report N`
token in the counted form. **This is a scope observation, not new scope:**
it is reported here, as the dispatch requires, and no worklist was widened
on account of it. Repair: delete the footnote attribution; the verifiable
half -- that this is a different paper from `2210.09775v2` -- passes as A5.

---

## Section 6 -- pintz10-patterns.md

**Grade: DEFECTIVE.** The stress case, and it earns the label. Its
load-bearing transcription -- the printed form of (2.10), exponent 2 and no
cardinality restriction -- is exactly right, and so is every other display
it takes from the source, except one. That one is inside a block introduced
with the word "verbatim", and the extract's own assurance that the block was
"independently re-verified via pdftotext this session" does not hold for it.

### 6.1 Fidelity checks

| # | extract location | what was checked | PDF location | verdict |
| --- | --- | --- | --- | --- |
| P1 | L3-L4 | source path, sha256 | file | PASS |
| P2 | L6 | "arXiv:1004.1072v1 [math.NT] ... 7 Apr 2010" | p.1 arXiv stamp | PASS |
| P3 | L6-L8 | author and Renyi Institute affiliation | p.9 signature block | PASS |
| P4 | L8-L12 | 9 pages, Creator, Producer, CreationDate | `pdfinfo` | PASS |
| P5 | L11-L13 | "No journal reference is printed on the paper" | whole PDF | PASS |
| P6 | L31-L33 | front-matter quotation, including the OTKA / ERC footnote | p.1 | PASS |
| P7 | L39 | "This is Lemma 2 and its r=1 remark, p.6-7" | both printed on p.6 | PASS (range contains) |
| P8 | L41 | the Lemma 2 lead-in, quoted | p.6 | **FAIL** |
| P9 | L43 | the (2.10) display: exponent 2, sum over $`\mathcal{D}\subset[1,H]`$ with no cardinality condition | p.6 | PASS |
| P10 | L45-L47 | the Remark on $`H_0(\nu,r)`$, $`c_7(\nu)`$, $`c_8(\nu,r)`$ | p.6 | PASS |
| P11 | L49-L53 | the r=1 Remark | p.6 | PASS |
| P12 | L55 | "Proof close, p.8" | p.8 | PASS |
| P13 | L55-L59 | the proof-close quotation | p.8 | **FAIL** |
| P14 | L63 | "p.6" for Lemma 1 | p.6 | PASS |
| P15 | L65 | the (2.8) display, with $`\lvert \mathcal{D}\rvert=\nu`$ on its own line | p.6 | PASS |
| P16 | L66-L71 | the Gallagher Remark and the (2.9) display | p.6 | PASS |
| P17 | L75 | "p.6-7, opening the proof of Lemma 2" | p.6 into p.7 | PASS |
| P18 | L75-L80 | the proof-opening quotation | p.6 | PASS |
| P19 | L81 | the (2.11) display | p.7 | PASS |
| P20 | L83-L85 | "constants implied by $`\ll`$ or O symbols on t and r" | p.7 | **FAIL** |
| P21 | L92-L93 | the (2.12) inline transcription | p.7 | **FAIL** |
| P22 | L93-L96 | the (2.13) three-way split over $`p\le y`$, $`p>y,p\mid\Delta`$, $`p>y,p\nmid\Delta`$ | p.7 | PASS |
| P23 | L96 | (2.14) $`\prod_3 = 1+O(1/y)`$ | p.7 | PASS |
| P24 | L96-L97 | (2.15) $`\log{\prod_2}\ll 1/\log{y}`$ | p.7 | PASS |
| P25 | L99-L101 | the (2.16) lead-in, quoted | p.7 | PASS |
| P26 | L103-L106 | the (2.16) first fraction | p.7 | PASS |
| P27 | L107 | the (2.16) second fraction, numerator | p.7 | **FAIL** |
| P28 | L108 | the (2.16) tail, $`= \prod_{p\mid P}(1+O(p^{-2})) = O(1)`$ | printed on **p.8**, block introduced as p.7 | **FAIL** (minor) |
| P29 | L110-L116 | the claim that (2.16) carries the exponent r at every $`p\mid P`$ | p.7 | PASS |
| P30 | L153-L165 | method anatomy: Selberg's sieve (2.1), Cauchy (2.7), the Theorem and its Corollary | p.5, p.5, p.4 | PASS |
| P31 | L169-L174 | uniformity ledger on $`c_7(\nu)`$, $`c_8(\nu,r)`$, $`H_0`$ | p.6 | PASS |
| P32 | L181-L182 | "No claim in this paper gives a bound uniform in $`\nu`$" | whole PDF | PASS |
| P33 | L186-L189 | NOT-FOUND: no growing-rank asymptotic, no $`(1+o(1))^k`$, no claim uniform in r | whole PDF | PASS |
| P34 | L199-L209 | Section 6's claim that (2.10) prints exponent 2 and no $`\lvert \mathcal{D}\rvert=\nu`$, unlike (2.8) | p.6 | PASS |

Display-fenced lines in this extract: 11. Seven transcribe source displays
(P9, P15, P16, P19, P26/P27, and the two inline displays in P21/P22); four
are the extract's **own** derivation -- the induction at L135-L145 and the
reconstructed Lemma 2 at L231 -- and are labelled as such in the extract.
Those four are not graded as transcriptions, because they do not claim to
be; they are the extract's reconstruction, and the extract says so.

### 6.2 The fails, in detail

**P27 -- the material one.** L97 introduces the block with "then,
verbatim:". The source prints, on p.7:

$$\frac{1}{P}\sum_{h=1}^{P}\prod\nolimits_1(h) \;=\; \prod_{p\mid P}\frac{\lbrace \frac{\nu_p}{p}\left(1-\frac{\nu_p}{p}\right)^{r} + \left(1-\frac{\nu_p}{p}\right)\left(1-\frac{\nu_p+1}{p}\right)^{r}\rbrace}{\left(1-\frac{\nu_p}{p}\right)^{r}\left(1-\frac{1}{p}\right)^{r}} \;=\; \prod_{p\mid P}\frac{\frac{\nu_p}{p}+1-\frac{\nu_p}{p}-\frac{r(\nu_p+1)}{p}+O\left(\frac{1}{p^{2}}\right)}{1-\frac{r(\nu_p+1)}{p}+O\left(\frac{1}{p^{2}}\right)}$$

The extract prints the second fraction's numerator as
$`1-\frac{r(\nu_p+1)}{p}+O(p^{-2})`$. The two are equal -- the source's
$`\frac{\nu_p}{p}`$ and $`-\frac{\nu_p}{p}`$ cancel -- but the source leaves
the cancellation unperformed and the extract performs it silently, inside a
block labelled verbatim. The first fraction (P26) is reproduced exactly,
including the exponent r at both factors, which is the feature the extract
relies on; the deviation is confined to the middle expression.

This was confirmed three ways, because the grade turns on it: the
`-layout` text layer, the raw text layer, and a 200-dpi render of p.7 read
as an image. All three print
$`\frac{\nu_p}{p}+1-\frac{\nu_p}{p}-\frac{r(\nu_p+1)}{p}`$. Repair:
transcribe the numerator as printed and record the cancellation as the
extract's own step, one line below.

**P8, P13, P20 -- three repaired source typos inside quotations.** The
source carries print-level slips and the extract silently fixes them:

Both columns below are ASCII-folded on the same convention the inventory
uses, so the only differences shown between them are the ones being flagged.

| extract prints | source prints | the difference | location |
| --- | --- | --- | --- |
| `For fixed nu, r and H > H0(nu, r)` | `For fixed nu r and H > H0(nu, r)` | no comma after nu in the source | p.6, Lemma 2 |
| `implied by << or O symbols` | `implied by << or 0 symbols` | digit zero in the source, not capital O | p.7, after (2.11) |
| `is <= P = O(H)` | `is <= P = 0(H)` | digit zero in the source, not capital O | p.8, proof close |

The two digit-zero findings are the reason p.7 and p.8 were rendered as
images. On the rendered page the glyph in "$`\ll`$ or 0 symbols" and in
"$`P = 0(H)`$" is narrow and upright, and is visibly a different character
from the wide italic O in "$`1 + O(1/p^2)`$" and "$`= O(1)`$" on the same
pages. They are digit zeros in the source, not a text-layer artifact.

Each of the three is mathematically inert, and none is invented content.
They are recorded as fails because the extract presents these passages as
verbatim, and because silently normalizing a source's print state is
precisely the operation that makes a later reader unable to tell the
source's state from the extract's reading of it. Repair: transcribe as
printed and note the slip alongside.

**P21 -- dropped product limits.** The extract renders the (2.12) definition
of $`\Delta`$ as $`\Delta:=\prod_i(h-d_i)`$. The source prints
$`\Delta := \prod_{i=1}^{\nu}(h-d_i)`$, with both limits. The lower limit
$`i=1`$ and the upper limit $`\nu`$ are exactly the feature that shows the
product runs over $`\mathcal{D}`$ and not over $`\mathcal{D}^{+} =
\mathcal{D}\cup\lbrace 0\rbrace`$, which has $`\nu+1`$ elements. Erasing the
limits erases the only part of the display that carries that information.
Repair: restore both limits.

**P28 -- minor page attribution.** L87-L88 introduces the block as "p.7
(continued, the local averaging computation, eq. (2.12)-(2.16))". The last
two equalities of (2.16) are printed at the top of p.8. Repair: "pp.7-8".

### 6.3 The (2.10) / (2.16) exponent question, settled against the PDF

The dispatch asks for this finding explicitly. Stated against the anchor,
with nothing carried over from the extract's own reading:

1. **(2.10) as printed** carries the exponent **2** on
   $`\mathfrak{S}(\mathcal{D}^{+})`$ and **no** $`\lvert \mathcal{D}\rvert =
   \nu`$ condition under the summation sign. Both features confirmed on p.6,
   in the text layer and on the rendered page. The extract's transcription
   of this display is correct and its Section 6 description of it is
   correct.
2. **(2.8), Lemma 1**, on the same page, carries the same exponent 2 **and**
   the condition $`\lvert \mathcal{D}\rvert = \nu`$ on its own second
   summation line. Confirmed.
3. **(2.11) and (2.16) both carry a general exponent r.** (2.11) raises the
   one-position ratio to the power r; (2.16) applies r to
   $`\left(1-\frac{\nu_p}{p}\right)`$ and
   $`\left(1-\frac{\nu_p+1}{p}\right)`$ at every $`p\mid P`$, and to both
   denominator factors. Confirmed on the rendered p.7.
4. **The r=1 remark is printed**, immediately after (2.10), and asserts an
   asymptotic $`S(\nu,r)\sim H^{\nu}`$ in that case. Confirmed on p.6.
5. **The lemma name and constants are r-dependent**: the left-hand side is
   $`S(\nu,r)`$, the constant is $`c_8(\nu,r)`$, the threshold is
   $`H_0(\nu,r)`$. Confirmed on p.6.
6. **The Lemma 2 lead-in itself carries a print slip** -- "For fixed
   $`\nu`$ r", with no comma -- which is independent evidence that this
   display was not proofread with care.

The coherent reading of the anchor is therefore a general-r bound under the
cardinality restriction, and the printed exponent 2 together with the
missing size restriction is a v1 typesetting defect. That is what the PDF
supports.

**This is recorded as a fidelity finding about the extract, not as a
re-verdict of any claim row.** No claim row is touched by this file. The
observation that the extract's Section 6 reaches the same reading is
recorded as a pass on P34, and nothing follows from it here.

### 6.4 I1 disposition (3 headings)

| line | verbatim heading or annotation | severed, source-anchored form |
| --- | --- | --- |
| L35 | `## 2. Statements cited by item-0022's reports (verbatim, in reading order)` | `## 2. Statements extracted from the anchor (verbatim, in reading order)` |
| L37 | `### 2.1 The Theorem actually invoked (report 1's "uniform Gallagher w.r.t. k" claim)` | `### 2.1 Lemma 2 and its r=1 remark (p.6)` |
| L240 | `Report 1's claim` (heading the paragraph `**Report 1's claim, reassessed.**` at L240) | delete the paragraph whole, **including the German-language quotation of report 1 it carries at L241-L245 and the checklist-row pointer at L246-L248** |

**L240 is the second of the two heavy ones.** Like kuperberg21's L88, the
annotation introduces verbatim report prose; unlike it, the paragraph also
ends by pointing at a checklist row's verdict. Both must go together: a
severance that removed the frame and kept the quotation would leave
unattributable prose in the corpus, and one that kept the row pointer would
leave a pointer into a withdrawn register. The quotation is not reproduced
in this file.

Note that severing L240-L248 removes nothing the extract needs. Its Section
6 reading of the anchor stands on P34, P9, P11 and P29, all of which are
confirmed against the PDF.

### 6.5 I2 disposition (7 references)

| line | matched text | kind | anchor location that replaces it, or reason |
| --- | --- | --- | --- |
| L15 | `against the dispatch` | (b) removable duplicate | author, title and identifier all printed on p.1 |
| L90 | `operator-supplied` | (a) disclaimer | states the tool re-run was made independently of operator-supplied material |
| L149 | `operator-supplied` | (a) disclaimer | states the derivation is not sourced from operator-supplied material |
| L254 | `operator supplied two documents` | (a) disclaimer | opens the FLAGS provenance note that records the two documents were not cited as sources |
| L255 | `Pintz_Lemma2_Image_Analysis_Report.pdf` | (a) disclaimer | names an object of the same disclaimer; the extract cites no content from it |
| L256 | `Pintz_Lemmas_1_and_2_Report.pdf` | (a) disclaimer | as above |
| L260 | `operator-commissioned` | (a) disclaimer | states the standing rule that such reports are never themselves evidence |

No (c). All seven are the disclaiming direction, which the inventory
predicted and this grading confirms: not one of the seven sources an
assertion **to** an ephemeral object.

**The disclaimers were tested, not accepted.** The extract asserts that its
revision rests on an independent re-reading of the anchor, reproduced in its
Section 2.3, rather than on the two operator-held documents. That assertion
is testable against the PDF without opening either document, and it was
tested: the substance holds -- (2.11) and (2.16) do carry the exponent r,
and the r=1 remark is printed as quoted -- but the accompanying assurance
that the (2.16) block was "independently re-verified via pdftotext this
session" is falsified for the one line P27 names, since `pdftotext` returns
the uncancelled numerator. The disclaimers are honest about provenance and
overstated about verification.

### 6.6 I3 note (1 bare mention)

L240. **It carries evidentiary weight and is flagged**; it is the same site
as the I1 annotation above and is disposed of there.

---

## Section 7 -- precedent-p1-2605.22763.md

**Grade: DEFECTIVE.** Its abstract and two of its four extracted passages
are exact and correctly located. The other two are not: one is a splice of
two passages printed six pages apart, presented under a single section
citation that fits neither, and one is quoted from the wrong page with a
component of a URL dropped.

### 7.1 Fidelity checks

| # | extract location | what was checked | PDF location | verdict |
| --- | --- | --- | --- | --- |
| C1 | L3-L4 | source path, sha256 | file | PASS |
| C2 | L6 | "arXiv:2605.22763v2 [cs.AI] 8 Jun 2026", printed dateline "2026-6-9" | p.1 | PASS |
| C3 | L8-L13 | all 21 author names, in order | p.1 | PASS |
| C4 | L12-L13 | affiliations Google DeepMind / Aarhus University / Google | p.1 | PASS |
| C5 | L13-L16 | 60 pages, Creator, Producer, Title, Author metadata | `pdfinfo` | PASS |
| C6 | L32-L50 | front-matter quotation (title, author list, whole abstract) | p.1 | PASS |
| C7 | L56 | "p.1-2, Introduction" | pp.1-2 | PASS |
| C8 | L56-L60 | the solve-count quotation, which straddles the page break | p.1 into p.2 | PASS |
| C9 | L64 | "p.9, Section 5" | Section 5 begins on **p.8** | **FAIL** |
| C10 | L64-L66 | "We compared the agents by analyzing the solve rate against the cost (in US dollars) per successfully proven problem" | **p.8** | **FAIL** |
| C11 | L66-L71 | "To understand the impact of the agent design ... Remarkably, the basic agent solved all 9 problems ..." | **p.2, Introduction** | **FAIL** |
| C12 | L75 | "p.2, Section 2 ('Lean.')" | p.2 | PASS |
| C13 | L75-L78 | the two Lean-verification fragments | p.2 | PASS |
| C14 | L78-L79 | "p.4: 'after each solve, experts on our team validated ...'" | p.4 | PASS |
| C15 | L83 | "p.1 (Introduction, final sentence)" | **p.2** | **FAIL** |
| C16 | L83-L85 | the availability sentence and its URL | p.2 | **FAIL** |
| C17 | L89-L94 | uniformity ledger: 9/353 and 44/492 are the full-featured agent (D)'s totals | p.1, p.2; agent (D) named full-featured at p.34 | PASS |
| C18 | L92-L94 | "(p.10 states 'Even most Erdos problems remain out of reach')" | **p.11** | **FAIL** |
| C19 | L98-L100 | NOT-FOUND: no commit SHA for the results repository anywhere in the paper | whole PDF, 60 pages | PASS |
| C20 | L106-L114 | FLAGS: read bounded to p.15 of 60 | consistent with C7-C14 | PASS |

Display-fenced lines in this extract: 0.

### 7.2 The fails, in detail

**C9, C10, C11 -- one quotation, two sources, six pages apart.** The extract
presents a single block introduced `p.9, Section 5:` containing two
sentences joined by an ellipsis. They are printed in different places:

| fragment | printed on | in |
| --- | --- | --- |
| "We compared the agents by analyzing the solve rate against the cost (in US dollars) per successfully proven problem" | p.8 | Section 5, "Impact of Agent Architecture and Model" |
| "To understand the impact of the agent design on these results, we did a post-hoc analysis ... Remarkably, the basic agent solved all 9 problems, though at a higher cost on the harder problems." | p.2 | Section 1, Introduction |

Section 5 begins on p.8, not p.9. The second fragment is not in Section 5 at
all; it is in the Introduction, six pages earlier. The ellipsis conceals the
jump. Both fragments are individually exact, and the claim they jointly
support -- that the basic agent solved all 9 -- is true and is printed in
the paper. But an ellipsis inside a quotation asserts contiguity, and here
there is none. Repair: split into two quotations, cite p.8 and p.2
separately.

**C15, C16 -- wrong page and an altered URL.** The availability sentence is
the Introduction's last sentence, but the Introduction runs onto p.2 and the
sentence is printed there, not on p.1. And the source prints:

```
All Lean proofs and select natural-language proofs are available in
https://www.github.com/google-deepmind/alphaproof-nexus-results.
```

The extract prints the URL without the `www.` component. It resolves to the
same place; it is not what the paper prints. This one deserves a sentence of
its own: a URL inside a quotation is the single most-copied kind of string
in a corpus, and an extract whose stated purpose is to be the checkable
record of what a source says must reproduce it character for character.
Repair: `p.2`, and restore `www.`.

**C18 -- wrong page.** "Even most Erdos problems remain out of reach" is
printed on p.11. Section 6, "Discussion", begins on p.10; the sentence is on
the following page. The quotation itself is exact. Repair: p.11.

**C19 passes and the pass is worth its line.** The claim is that no commit
SHA appears anywhere in the paper. That was checked against all 60 pages,
not against the extract's declared 15-page bounded read: the appendix
repository links use `blob/main`, a branch reference, and no
forty-hexadecimal string occurs in the document. The negative claim is
sound over its full stated scope.

### 7.3 I1 disposition (5 headings)

| line | verbatim heading | severed, source-anchored form |
| --- | --- | --- |
| L52 | `## 2. Statements cited by item-0022's reports (verbatim)` | `## 2. Statements extracted from the anchor (verbatim)` |
| L54 | `### 2.1 The headline solve counts (report 2 Section 10.1)` | `### 2.1 The headline solve counts (Introduction, pp.1-2)` |
| L62 | `### 2.2 The basic Generate-Verify agent replicating the Erdos successes (report 2's "einfacherer Generate-Verify-Agent" claim)` | `### 2.2 The basic agent replicating the Erdos successes (Introduction p.2; Section 5, p.8)` |
| L73 | `### 2.3 Lean mechanical verification (report 2's "die Beweise wurden in Lean mechanisch gepruft" claim)` | `### 2.3 Lean mechanical verification (Section 2, p.2; p.4)` |
| L81 | `### 2.4 Public availability of results (report 2's [P2] citation)` | `### 2.4 Public availability of results (Introduction, p.2)` |

The severed forms for L62, L73 and L81 fold in the page repairs from C9-C16;
this is written, not applied, and the repair and the severance are one
operation for these three headings.

### 7.4 I2 disposition (2 references)

| line | matched text | kind | anchor location that replaces it, or reason |
| --- | --- | --- | --- |
| L18 | `against the dispatch` | **(c) load-bearing and unreplaceable** | the sentence's content is "this is precedent P1 (Appendix C.1)". No anchored source carries the label P1 or the Appendix C.1 classification; both existed only in the kickoff dispatch and the withdrawn register. Nothing in the PDF can replace it |
| L21 | `kickoff dispatch` | (b) removable duplicate | title, author and identifier are printed on p.1; the roadmap half of the reference is in-tree |

**One (c).** Under the rubric a (c) forces DEFECTIVE on its own. This
extract is already DEFECTIVE on fidelity, so the classification does not
move the grade -- but it changes the repair. A (c) cannot be rewritten to
point at the anchor, because there is nothing at the anchor to point at. The
`precedent P1 (Appendix C.1)` label must be **deleted**, not re-anchored,
and whatever corpus role this extract is to have must be assigned afresh by
the decision that Section 9 leaves open. Recorded, so that a later repair
pass does not try to salvage the label.

### 7.5 I3 note

The inventory records 0 I3 matches, and that is confirmed.

---

## Section 8 -- precedent-p3-2601.07421.md

**Grade: DEFECTIVE.** The shortest extract in the set and the one with the
fewest checks, and it fails one of them squarely: the Lean-correspondence
quotation is cited to p.2 and is printed on p.10, in a different section,
and the extract's own description of what it read is inconsistent with the
paper's section layout.

### 8.1 Fidelity checks

| # | extract location | what was checked | PDF location | verdict |
| --- | --- | --- | --- | --- |
| T1 | L3-L4 | source path, sha256 | file | PASS |
| T2 | L6-L8 | "arXiv:2601.07421v5 [math.NT] 26 Jan 2026"; printed dateline "Jan 27, 2026" | p.1 | PASS |
| T3 | L8 | author and email | p.1 and its footnote | PASS |
| T4 | L8-L10 | 20 pages, Creator, Producer, Title, Author metadata | `pdfinfo` | PASS |
| T5 | L26-L35 | front-matter quotation (title, author, dateline, abstract first paragraph) | p.1 | PASS |
| T6 | L41-L45 | the two R2-005 fragments on the system and the formal-to-informal translation | p.1 abstract | PASS |
| T7 | L47 | "p.2, further detail on the Lean/informal relationship" | printed on **p.10**, in Section 6 | **FAIL** |
| T8 | L48-L49 | the quoted sentences themselves | p.10 | PASS |
| T9 | L58-L62 | NOT-FOUND: no claim that the result is in its best possible form; Remark 1 on p.2 | p.2 | PASS |
| T10 | L60-L62 | the Remark 1 quotation | p.2 | PASS |
| T11 | L66-L70 | FLAGS: "read to PDF page 10 of 20 (title page through the start of Section 4)" | Section 4 begins on p.6; p.10 is inside Section 6 | **FAIL** |

Display-fenced lines in this extract: 0.

### 8.2 The fails, in detail

**T7.** The quoted sentences are

> The accompanying Lean file Erdos728b.lean [1] contains a fully formal
> proof of the main theorem. We map our lemmas to the Lean file as follows.

They open Section 6, "Correspondence with the Lean development", on p.10.
p.2 carries the close of the Introduction, Theorem 1, Remark 1 and the
acknowledgements, and contains neither sentence. The quotation is exact; the
address is off by eight pages and one section. Repair: "p.10, Section 6".

**T11.** The FLAGS section describes the bounded read as "PDF page 10 of 20
(title page through the start of Section 4)". Against the paper's own
layout, Section 2 begins on p.3, Section 3 on p.4, Section 4 on p.6, Section
5 on p.9 and Section 6 on p.10. A read to p.10 therefore covers Sections 1
through 5 entire and reaches into Section 6 -- which it must, since the
sentences quoted at T8 are printed there. The page bound is coherent with
what the extract quotes; the parenthetical describing it is not, and it
understates the read by two whole sections. Repair: "title page through the
opening of Section 6".

The two fails compound: T7's wrong page and T11's wrong section description
are the same error seen from two sides, and a reader trusting either would
conclude the Lean-correspondence material sits in the front matter.

**Note, not a fail.** Section 1 is headed "Front matter (verbatim)" and
reproduces the first of the abstract's two paragraphs. The second paragraph,
which states the proved result and sketches the argument, is omitted with no
ellipsis. Every other extract in the set reproduces the abstract whole. This
is recorded as a selection note rather than a fail, because the extract's
declared bounded-read convention licenses selection -- but the omission is
silent, and marking it would cost one character.

### 8.3 I1 disposition (2 headings)

| line | verbatim heading | severed, source-anchored form |
| --- | --- | --- |
| L37 | `## 2. Statement cited by item-0022's reports (verbatim)` | `## 2. Statement extracted from the anchor (verbatim)` |
| L39 | `### 2.1 The system, mechanism, and formal-to-informal translation (report 2 Section 10.2)` | `### 2.1 The system, mechanism, and formal-to-informal translation (abstract, p.1; Section 6, p.10)` |

L39's severed form folds in the T7 repair, as with the precedent-p1
headings.

### 8.4 I2 disposition (2 references)

| line | matched text | kind | anchor location that replaces it, or reason |
| --- | --- | --- | --- |
| L12 | `against the dispatch` | **(c) load-bearing and unreplaceable** | the sentence's content is "this is precedent P3 (Appendix C.1)". As with precedent-p1 L18, no anchored source carries the label or the classification |
| L15 | `kickoff dispatch` | (b) removable duplicate | title, author and identifier are printed on p.1; the roadmap half of the reference is in-tree |

**One (c)**, of the same shape as precedent-p1's, with the same consequence:
the label is deleted, not re-anchored.

### 8.5 I3 note

The inventory records 0 I3 matches, and that is confirmed.

---

## Section 9 -- what this grading found, across the seven

**One.** The mathematics is sound and the citation apparatus is not. Across
all seven extracts, 25 display-fenced lines and every theorem, lemma and
equation number were checked. Exactly one display deviates from its source
(Pintz (2.16)'s middle numerator, P27) and every numbered object -- Lemma 1,
Lemma 2, (2.8) through (2.16), Theorem 1.1, (1.5), Example 3.5, Proposition
4.1, Example 4.3, eq. (4), Conjecture 1.1, Theorem 1.2, Theorem 2, (6), (8),
(9), Remark 1 -- is correctly identified. Against that, eleven page or
section citations name a location that does not carry the object they cite,
spread across five of the seven extracts. An extract set produced without
opening its sources is exactly what that pattern looks like.

**Two.** Every quotation that was altered was altered in the direction of
tidiness: a comma inserted where the source omitted one, a typo repaired, a
cancellation performed, a cross-reference dropped, a connective supplied, a
`www.` removed. None of the alterations inserts content the source does not
support. That is worth stating plainly, because it bounds what the defect
is: these are not fabrications, they are an editorial hand operating inside
quotation marks. The reason it still fails is that the extracts exist to be
the checkable record of what the sources print, and an edited quotation
cannot serve that.

**Three.** The NOT-FOUND probes are the least reliable sections. Four of the
seven carry a probe or scope sentence the anchor contradicts (B11, B12, W26,
K18, A15), and in every case the contradiction is an over-broad negative
rather than a wrong one: the probe says "not present in this paper" where
the truth is "not proved in this paper" or "not this paper's own result".
Every probe clause that carries item-0026 reasoning survived -- no uncentered
$`\sum \mathfrak{S}(H)^2`$, no flanked or aggregated-simplex domain, no
per-position $`(1+o(1))^k`$, no growing-rank asymptotic, no commit SHA. The
defect is in how the negatives are stated, not in what they found.

**Four.** The inventory's I3 axis should not be assumed inert. The dispatch
asked for the eleven bare mentions to be confirmed as carrying no
evidentiary weight, or flagged. **Four sites are flagged**: bloomkuperberg
L18 and its L75-L78 cluster, kowalski L172-L187, kuperberg21 L52, pintz10
L240. Each asserts something about a dropped report that no session can
check. Three of the four are replaceable -- the fact is separately recorded
in-tree, or the mathematics is separately anchored -- and one, pintz10 L240,
is a verbatim quotation that must be deleted rather than re-sourced.

**Five.** Two extracts carry verbatim report prose (kuperberg21 L88-L90,
pintz10 L241-L245), in both cases underneath an I1 framing annotation. Their
severance and the removal of the quotation are one operation, not two, and a
repair pass that severs the frame while keeping the text would make the
corpus worse rather than better.

**Six.** Two I2 references are class (c), and they are the same reference:
the precedent extracts' self-identification as "precedent P1 / P3 (Appendix
C.1)". Nothing at any anchor carries that label. It is the only place in the
seven where an extract states a fact that exists solely because a now-gone
object asserted it, and it is a role label rather than a mathematical claim,
which is why it costs the corpus nothing to delete.

**Seven, and this is the one to carry forward.** All seven extracts need
**two** distinct repairs, not one. The severance of I1 and I2 provenance
defects, which Phase 2a scoped, is necessary and not sufficient: a fully
severed extract set would still carry eleven fabricated locations, six
altered quotations and five contradicted negatives. Every repair recorded
above is small, local and mechanically checkable against a PDF that is in
the tree and hash-booked. None requires a dropped object. But they must
actually be done, and done with the PDFs open, before a hash is booked over
any of these files.

---

## Section 10 -- what was hashed

**Nothing.**

No extract graded CLEAN. The dispatch's Lane B rule is "only CLEAN extracts,
and the grade file itself, are hashed ... nothing if nothing is clean", and
its budget line reads "one per CLEAN extract, plus one for the grade file; 0
if nothing is CLEAN". Zero applies. `payloads/HASHES.txt` is unmodified by
this apply and this grade file is not hashed either.

That is the intended outcome of the rule and not a shortfall. Anchoring
freezes what it books; ERRATUM-5 is the standing demonstration of what a
hash over a defect costs; and every one of these seven files has a defect
that a hash would freeze.

## Section 11 -- what this pass did not do

- It did not open a dropped report, the kickoff dispatch, or an
  operator-held PDF. Not once.
- It did not edit any extract. Not one character.
- It did not edit a checklist row or the inventory.
- It did not re-verdict any claim row. The (2.10) / (2.16) finding in
  Section 6.3 is a fidelity finding about the extract and about what the
  anchor prints; it touches no row and no verdict.
- It did not hash anything.
- It did not decide whether the two precedent extracts stay in the corpus.
  Their fidelity is graded on the same footing as the other five and their
  membership stays an open operator question. Note that both carry the only
  two class-(c) I2 references in the set, which is information for that
  decision and not a resolution of it.
- It did not perform any severance or any repair. Every one is written down
  above and none is applied.
