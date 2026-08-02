# item-0029 SESSION E (extraction) -- run report

Lane: EXECUTOR (local workstation, Claude Code). Web OFF, cloud OFF for the
entire session. Executor model: claude-opus-5. Date of run: 2026-08-02.

## 0. Pin and rule-18 delta

Section 0 pin of the dispatch: `1e5a4cc98d0619608e6ce28c889566b745e576a6`.

P1 outcome, verbatim from the session-start check:

```
$ git rev-parse HEAD
1e5a4cc98d0619608e6ce28c889566b745e576a6
$ git status --porcelain
?? item-0029-kickoff-E-v1.md
$ git diff 1e5a4cc98d0619608e6ce28c889566b745e576a6..HEAD --name-only
(no output)
```

HEAD equals the Section 0 pin exactly, so the first branch of P1 holds and no
rule-18 delta arises. The only untracked path at session start was the ephemeral
kickoff itself, which is never committed.

P2: `roadmap/item-0029.md` frontmatter reads `status: ratified`. Holds.

P3: `ledger/annotations/ANN-20260801-91.yaml` exists (7832 bytes) and
`python3 scripts/ledger_check.py validate` passed. Holds.

## 1. Gates at start and close

Every Section 8 gate was run twice, once before any extract file was created and
once after all outputs existed. Outputs were identical at both runs except where
noted. Verbatim close-run outputs:

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
  5 post-pin entr(ies), out of scope here, covered by append-only
RELOCATION CHECK PASSED -- concatenation is byte-identical to the old body.

$ python3 scripts/ledger_check.py validate
  91 entries, sequence numbers up to 91, 13 bets
  4 grandfathered malformed refs (allowlist size 4)
VALIDATE: passed.

$ python3 scripts/ledger_check.py append-only --base 1e5a4cc98d0619608e6ce28c889566b745e576a6
APPEND-ONLY: 0 change(s) under ledger/annotations over
1e5a4cc98d0619608e6ce28c889566b745e576a6..HEAD, additions only.

$ python3 scripts/writeup_mapper.py check --manifest writeup/sources.yml
PASS

$ python3 scripts/mathjax_lint.py
MATHJAX LINT: 149 file(s) checked, 0 problem(s)

$ python3 .agents/skills/roadmap-items/scripts/roadmap.py show item-0029
status: ratified

ASCII check: 0 non-ASCII bytes in each of the six new Markdown files produced
by this session and in the new ledger entry.
```

Start-run differences, both expected and both mechanical: `mathjax_lint` reported
143 files at start against 149 at close (the five extracts plus this report; the
lint walks the tree and does not consult .gitignore, so it still sees the withheld
Shiu extract of D8), and
`append-only` is a close-only gate and was not run at start. `roadmap.py show
item-0029` reported `status: ratified` at both runs. The roadmap tool was invoked
at `.agents/skills/roadmap-items/scripts/roadmap.py`, per the ANN-88 environment
finding. No `lake` invocation was made.

`payloads/HASHES.txt` is byte-unchanged by this session: `git diff --stat
payloads/HASHES.txt` is empty at close.

## 2. Verification table V-E

| row | class | outcome |
| --- | --- | --- |
| V1 | gate | PASS. All five anchor lines are byte-present in payloads/HASHES.txt, and at exactly the stated line numbers 28, 29, 105, 106, 107. No line moved. |
| V2 | gate | PASS. sha256 of each of the five local PDFs equals its anchor line. Re-verified a second time mid-session (see Section 5, D1) with identical results. |
| V3 | gate | PASS. P1, P2, P3 all hold; see Section 0. |
| V4 | gate | PASS. `dossier/item-0029-workpapers/` did not exist at session start. |
| V5 | record | Steering expectation CONFIRMED against the anchored bytes. `pdffonts` on Maier-Primes-in-short-intervals.pdf lists no fonts at all, and `pdftotext -f 1 -l 1` returns 1 byte (a newline). There is no text layer. This is the expected state, not a stop (rule 9). Extraction for this source is render-only. |
| V6 | record | Steering expectation CONFIRMED. S0002-9939-1988-0958032-5.pdf carries one embedded CID TrueType subset font (LOUMNL+TimesNewRomanPSMT, Identity-H, uni=yes) and a text layer that is OCR-derived and corrupt throughout: it renders R^k as "Rfc", N as "TV", delta as "6", and p_{n+1}-p_n as "Pn+i ~Pn". Renders are the evidence base; the layer was used for navigation only. |
| V7 | record | DETERMINED and declared in the header. The Shiu publisher PDF carries a text layer, but every font is a Type 1 CUP subset with a Custom encoding and no ToUnicode map (uni=no on all of them). Extracted characters are therefore systematically mis-mapped: "=" comes out as "l", the congruence sign is dropped, and most subscripts land on separate lines. The declared extraction method for this source is render-based. |
| V8 | record | Page counts in the Section 2.1 line order: 9 / 6 / 15 / 24 / 30. Steering expectation was 9 / 6 / 15 (journal pp. 359-373) / ~23-24 / ~29-30. All five within expectation; see Section 5, D2 for the one detail worth recording. |
| V9 | record | CONFIRMED. In 1110.6624v1 the first page of "4. Proof of Lemmas 3.2 and 3.3" is p.13, matching steering's read of the non-canonical copy. |

## 3. Per-source method record

- Maier 1985 (Michigan Math. J. 32 (1985) 221-225). Method: render-based,
  200-dpi page rasters of all 6 pages, plus two 400-dpi crops of p.222 to settle
  bracket glyphs in the good-modulus definition. No text layer exists (V5).
  Printed pages 221-225 occupy PDF pages 1-5; PDF page 6 is blank.
- Hildebrand-Maier 1988 (Proc. Amer. Math. Soc. 104 (1988) 1-9). Method:
  render-based, 200-dpi rasters of all 9 pages. Text layer present but OCR-corrupt
  (V6) and used only to locate material. Printed pagination 1-9 coincides with the
  PDF pages.
- Shiu 2000 (J. London Math. Soc. (2) 61 (2000) 359-373). Method: render-based,
  200-dpi rasters of all 15 pages, plus 400-dpi crops of pp.367 and 368 to settle
  the set glyph of the constructed prime set and one variable. Text layer present
  but character-mapping-corrupt (V7). Printed journal pages 359-373 map to PDF
  pages 1-15.
- Freiberg 1005.4703v2. Method: text-layer with render verification. The text
  layer is clean LaTeX-derived output; each quoted passage was checked against a
  200-dpi raster of the page it is cited from. Printed pagination 1-24 coincides
  with the PDF pages.
- Freiberg 1110.6624v1. Method: text-layer with render verification, same
  protocol. Printed pagination 1-30 coincides with the PDF pages. The declared
  scope covers pp.1-13 through the end of Section 3; the V9 boundary (Section 4
  beginning on p.13) is stated in the extract's own scope-boundary section.

## 4. Per-extract inventory

| file | lines | verbatim-quoted numbered/named objects | `$$`-display blocks | TRANSCRIPTION-UNSURE | [extract note] lines |
| --- | --- | --- | --- | --- | --- |
| maier85-shortintervals.md | 397 | 11 (Theorem, Lemmas 1-4; displays (1.1), (2.1)-(2.4), (3.1)) | 30 | 0 | 20 |
| hildebrandmaier88-gaps.md | 492 | 31 (Theorem, Corollary, Lemmas 1-4; displays (1)-(21), (*), (**), (6)', (7)') | 59 | 0 | 20 |
| shiu00-strings.md | 650 | 10 (Theorems 1-2, Lemmas 1-5; displays (1)-(3)) | 113 | 0 | 16 |
| freiberg10-strings1.md | 804 | 79 (Theorem 1.1, Lemma 2.1, Propositions 2.2-2.3, Lemmas 4.1-4.2, Lemmas 5.1-5.5; displays (2.1)-(2.12), (3.1)-(3.2), (4.1)-(4.14), (5.1)-(5.32), (6.1)-(6.8)) | 153 | 0 | 22 |
| freiberg11-strings2.md | 497 | 31 (Theorem 1.1, Theorem 3.1, Lemmas 3.2-3.4; displays (1.1)-(1.2), (3.1)-(3.24)) | 68 | 0 | 19 |

Envelopes (Section 5 of the dispatch): 100-400, 140-500, 180-650, 280-900,
180-650 respectively. All five files are inside their envelope. This report is
inside 150-450. No file was padded or content-trimmed to fit; where a first draft
came in long, the fix was presentational density (line wrapping, dropped
decorative subheadings, merged ledger and map items) with the transcribed object
set unchanged.

The row for shiu00-strings.md is an inventory of a file that was produced in
full but is NOT part of this apply; see D8 below.

## 5. Deviations and surprises

D1. SCRATCHPAD LOSS AND FULL RE-VERIFICATION. Partway through the session the
operator interrupted, and the session scratchpad -- holding the page renders and
the text-layer dumps -- was cleared during the break. The renders behind the
already-drafted Maier 1985 and Hildebrand-Maier 1988 transcriptions were
therefore no longer on disk. Rather than proceed on unverifiable state, the
session re-verified the five sha256 anchors against the local PDFs a second time,
re-rendered all 84 source pages from the anchored bytes, re-ran every V5-V8 probe,
and re-read the Maier 1985 pages page by page against the fresh renders before
continuing. The two already-drafted extracts were confirmed against the fresh
renders with no correction required. Every quotation in all five extracts rests on
a render or text layer produced from the anchored bytes and read in this session.

D2. Maier 1985 page count. The PDF has 6 pages against a steering expectation of
"6 pp.", and the printed article occupies pages 221-225, i.e. five printed pages;
PDF page 6 is blank. Recorded rather than resolved.

D3. Numbered-display counts diverge from the dispatch's per-source attention lists
in four places, each recorded in the FLAGS of the extract concerned and none
resolved silently:
  (a) Hildebrand-Maier: the dispatch named "displays (1)-(5)"; the source runs one
      sequence (1)-(21) plus the named displays (*), (**), (6)' and (7)'.
  (b) Shiu: the dispatch named "every numbered display in between"; the source
      numbers exactly three displays, (1), (2) and (3), all inside the proof of
      Lemma 3 on p.366. Every other display in the paper is unnumbered. All are
      transcribed regardless.
  (c) Freiberg 1005.4703v2: the dispatch named (5.19)-(5.23); the source also
      numbers (5.1)-(5.18) and (5.24)-(5.32).
  (d) Freiberg 1110.6624v1: the dispatch named the construction (3.1)-(3.6); the
      source also numbers (3.7)-(3.24) inside the declared scope.

D4. Shiu naming divergences, two, both recorded in that extract's FLAGS. The
constructed prime set is printed as a script P with subscript a and defined on
p.367; P'(y) on p.362 is a different object inside the proof of Lemma 1, and the
"P'(H)" form the dispatch mentioned is not this source's notation. The
composed-integers counting lemma the construction rests on is this source's
LEMMA 3 (p.363), not its Lemma 2; Lemma 2 (p.363) is the two-sided pi(x; q', a')
estimate, Brun-Titchmarsh above and Gallagher below.

D5. Source print slips, recorded alongside the transcriptions and not repaired.
Maier 1985 p.222 prints a vertical bar where a closing parenthesis is expected in
`L(s,chi)`. Hildebrand-Maier p.2 writes "Erdos and Ricci [8]" while entry [8] is
G. Ricci alone. Shiu p.368 prints the interval as (0, yx] in the |S| line against
(0, yz] in the companion |T| line, prints |P| for |P_1| in the section's first
sentence, and carries an innermost sum with no summand in the |T| display; p.369
prints the Q/phi(Q) product over a bare script P; p.363 prints P'(p_n) on both
sides of one inequality. Freiberg 1005.4703v2 prints mu(d_1)mu(d_1) in
F(s_1,s_2;Omega) (p.8) and 1/p^{s_1} + 1/p^{s_1} in G(s_1,s_2;Omega^+) (p.11),
drops the subscript R from Lambda in (6.2)-(6.3), and prints "Cauchy-Schwartz" at
(6.7).

D6. Definitional divergence between the two Maier-lineage sources, recorded in the
Hildebrand-Maier FLAGS: the 1988 good-modulus definition restricts the zero-free
condition to NONPRINCIPAL characters, where the 1985 definition says "all
characters"; and the 1988 primorial is over p <= z where the 1985 one is over
p < z.

D7. The Shiu PDF carries a Wiley Online Library delivery stamp in the right margin
of every page, naming the downloading account and the download date. It is an
artifact of the delivery of this PDF rather than part of the article; it is
recorded in that extract's conventions and FLAGS and is not transcribed.

D8. THE SHIU EXTRACT IS WITHHELD FROM THE APPLY ON OPERATOR INSTRUCTION. At apply
time, with all six output files written and every gate green, the operator
directed on publisher-copyright grounds that shiu00-strings.md not be committed,
that .gitignore name it, and that the remainder be committed. That instruction was
followed. The file was produced in full to the same specification as the other
four, is inside its 180-650 envelope at 650 lines, and remains on the executor
workstation; it is inventoried in Section 4 above and is not in the commit.

The consequence is stated here rather than absorbed. Rule 21 names the anchored
extract as "the one permitted substitute" for a source that cannot be committed,
and rule 26 makes the extract "the only in-tree representation of its source".
With the extract withheld, the Shiu 2000 source has no in-tree representation at
all: it is anchored in payloads/HASHES.txt at line 105 and readable by nobody
working from the tree. That is precisely the operator-held-object state rules 21
and 26 exist to prevent. Session G cannot grade the Shiu extract and Session M
cannot consume it under rule 26(4), so any item-0029 conclusion that would rest on
Shiu 2000 must either be carried by the two Freiberg extracts, which quote and
cite Shiu's construction at second hand, or be reopened by the operator as a
separate rule-26(5) event. This report records the exclusion and its consequence;
resolving the standing question it creates is the operator's, not this session's.

This is a change to the run's file list made after the outputs existed. It is not
an addendum to a finished run in the rule-24 sense -- no report had been applied
and no ratifying commit had landed -- but it is a scope decision taken outside the
dispatch, so it is booked by name here and in ANN-92 rather than folded silently
into the deliverables.

No fidelity doubt about any EXISTING graded extract surfaced during this session
(r29E.6 not triggered).

## 6. STOP conditions

All ten reported, none fired.

- r29E.1 validity failure (P1 content-path delta, P2, P3, V4): NOT FIRED. HEAD
  equalled the pin, item-0029 was ratified, ANN-91 existed and validated, and the
  workpaper directory was absent.
- r29E.2 source-hash mismatch on any of the five (V2): NOT FIRED. All five matched,
  twice.
- r29E.3 unreadable source: NOT FIRED. All 84 pages rasterised at 200 dpi. Two
  regions were re-rendered at 400 dpi for glyph decisions (Maier 1985 p.222; Shiu
  pp.367-368); no page was illegible at either resolution.
- r29E.4 scope pressure: NOT FIRED. No network access was attempted or required;
  no sixth source was opened; no existing extract, workpaper, Lean file or
  payloads/HASHES.txt line was touched. The operator's apply-time exclusion of the
  Shiu extract (D8) narrowed the apply rather than widening the scope, and was an
  operator decision rather than a step the work required.
- r29E.5 envelope breach: NOT FIRED. All six files are inside their envelopes; see
  Section 4.
- r29E.6 fidelity doubt about an existing graded extract: NOT FIRED. None arose.
- r29E.7 verdict drift: NOT FIRED. No sentence adjudicating an item-0029 axis, the
  positive-proportion gate or either named finding was written into any extract or
  into this report. No extract contains an axis verdict, gate language, a
  NOT-FOUND probe, or a comparison to a project object.
- r29E.8 ANN sequence collision: NOT FIRED. `ledger/annotations/ANN-20260801-92.yaml`
  did not exist at session start; the computed next number is 92.
- r29E.9 close-gate failure: NOT FIRED. All Section 8 gates are green at close;
  see Section 1.
- r29E.10 instruction unsatisfiable or internally divergent: NOT FIRED. No
  divergence between Section 4 of the dispatch and ANN-20260801-91 was found. The
  four attention-list divergences of D3 and the two naming divergences of D4 are
  divergences between a dispatch attention list and the canonical bytes, which the
  dispatch's own object-coverage rule directs to FLAGS rather than to a stop; the
  lists are floors, and the canonical bytes governed in every case.

## 7. Budget reconciliation

| task | dispatch estimate | actual |
| --- | --- | --- |
| V-E table + gates at start | mechanical, < 30 min equiv. | as estimated; one pass, no re-runs needed |
| renders | ~83 source pages once at 200 dpi; 300 dpi only on legibility need | 84 pages at 200 dpi, rendered twice (see D1); two 400-dpi region re-renders for glyph decisions rather than 300-dpi page re-renders, both for typography rather than legibility |
| maier85 + hm88 extracts | the render-transcription bulk | as estimated; the heavier of the two costs was reading all 15 Shiu pages, which the dispatch grouped with the text-layer sources but which V7 moved to the render-based protocol |
| shiu00 + freiberg10 + freiberg11 | text-layer-assisted (subject to V7), render-verified | shiu00 moved to render-based by the V7 finding; the two Freiberg extracts were text-layer with render verification as planned. freiberg10 is the largest output at 804 lines, consistent with its 68 numbered displays |
| report + ANN + HANDOVER + close gates | mechanical | as estimated, plus one unbudgeted correction pass over the report, ANN-92 and HANDOVER after the operator's apply-time exclusion of the Shiu extract (D8) changed the apply's file list |

The page count is 84 rather than the estimated ~83 (9 + 6 + 15 + 24 + 30). No
proof work, no computation beyond hashing, rendering and linting, no Lean, no
network. All five extracts were completed. The only shortfall to name is not a
shortfall of the work: four of the five reach the tree, and the fifth is withheld
by operator instruction (D8).
