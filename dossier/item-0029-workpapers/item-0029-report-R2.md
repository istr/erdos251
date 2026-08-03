# item-0029 SESSION R2 (repair, second cycle) -- run report

Lane: EXECUTOR (local workstation, Claude Code). Web OFF, cloud OFF for the
entire session. Executor model: claude-fable-5. Date of run: 2026-08-03; the
operator decision opening this second cycle was taken 2026-08-02 at dispatch
of the ephemeral kickoff item-0029-kickoff-R2-v1.md.

This session is FRESH in the rule-26(3) sense: it is none of the Sessions E,
G, R or G2, inherits no context, notes, renders or text-layer dumps from any
of them, and did not read the withheld executor-local `shiu00-strings.md`.
Everything it verified against was produced inside this session from the
anchored bytes. This session edited with sources open and graded nothing,
hashed nothing, verdicted nothing (rule 26(1) and 26(3)); the terminal
re-grade is Session G3, a further fresh session.

## 0. Pin and rule-18 delta

P1 outcome, verbatim from the session-start check:

```
$ git rev-parse HEAD
d90794b1281f7114cd209ca810534a44b79b88a8
$ git diff d90794b1281f7114cd209ca810534a44b79b88a8..HEAD --name-only
(no output)
$ git status --short
?? item-0029-kickoff-R2-v1.md
```

HEAD equals the Section 0 pin exactly, so the first branch of P1 holds and NO
RULE-18 DELTA ARISES. The only untracked path at session start was the
ephemeral kickoff, which is never committed.

P2: `roadmap/item-0029.md` frontmatter reads `status: ratified`. Holds.

P3: `ledger/annotations/ANN-20260802-95.yaml` exists and
`python3 scripts/ledger_check.py validate` passed at 95 entries. Holds.

P4: the three repair targets exist under `dossier/item-0029-workpapers/extract/`
exactly as committed at the pin -- `git status --short` reports nothing under
that path -- and the three hashed grade-chain artifacts verified against their
payloads/HASHES.txt lines before any source was opened:
`hildebrandmaier88-gaps.md` at `9d0d8bc0...6dfffa`, `extract-grades-G1.md` at
`0739f84c...71c5c7`, `extract-grades-G2.md` at `f4c564b6...63aab1`. Holds.

P5: `dossier/item-0029-workpapers/item-0029-report-R2.md` did not exist
("Datei oder Verzeichnis nicht gefunden"). Holds. The ANN collision check ran
with it: `ledger/annotations/ANN-20260802-96.yaml` did not exist either.

## 1. Gates at start and close

Every Section 8 gate ran twice, once before any render or edit was made and
once after all outputs existed. Verbatim close-run outputs; the two gates
whose output depends on whether the commit exists are recorded in their
post-commit form, which is the state a later session can reproduce:

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
  10 post-pin entr(ies), out of scope here, covered by append-only
RELOCATION CHECK PASSED -- concatenation is byte-identical to the old body.

$ python3 scripts/ledger_check.py validate
  96 entries, sequence numbers up to 96, 13 bets
  4 grandfathered malformed refs (allowlist size 4)
VALIDATE: passed.

$ python3 scripts/ledger_check.py append-only --base <the Section 0 pin>
APPEND-ONLY: 1 change(s) under ledger/annotations over d90794b1281f7114cd209ca810534a44b79b88a8..HEAD, additions only.

$ python3 scripts/writeup_mapper.py check --manifest writeup/sources.yml
PASS

$ python3 scripts/mathjax_lint.py
MATHJAX LINT: 155 file(s) checked, 0 problem(s)

$ python3 .agents/skills/roadmap-items/scripts/roadmap.py show item-0029
status: ratified

ASCII check: 0 non-ASCII bytes in each new or edited file of this apply
(the three repaired extracts, this report, ANN-20260802-96.yaml, HANDOVER.md).

sha256 recheck of the three hashed grade-chain artifacts against
payloads/HASHES.txt (byte-untouched proof):
dossier/item-0029-workpapers/extract/hildebrandmaier88-gaps.md: OK
dossier/item-0029-workpapers/extract-grades-G1.md: OK
dossier/item-0029-workpapers/extract-grades-G2.md: OK

$ git diff --name-only <the Section 0 pin>..HEAD
HANDOVER.md
dossier/item-0029-workpapers/extract/freiberg10-strings1.md
dossier/item-0029-workpapers/extract/freiberg11-strings2.md
dossier/item-0029-workpapers/extract/maier85-shortintervals.md
dossier/item-0029-workpapers/item-0029-report-R2.md
ledger/annotations/ANN-20260802-96.yaml
```

The apply is exactly the six files of Section 9 of the kickoff. Start-run
differences, all expected and all mechanical: `mathjax_lint` reported 154
files at start against 155 at close (this report); `ledger_check.py
relocation-check` reported 9 post-pin entries at start against 10 at close
(ANN-96); `validate` reported 95 entries at start against 96 at close;
`append-only` read 0 changes at start and is quoted post-commit above, as is
`git diff --name-only`, which is empty before the commit. `roadmap.py show
item-0029` reported `status: ratified` at both runs, invoked at
`.agents/skills/roadmap-items/scripts/roadmap.py`. No `lake` invocation was
made. payloads/HASHES.txt appears in no diff of this apply.

## 2. Verification table V-R2

| row | class | outcome |
| --- | --- | --- |
| V1 | gate | HOLDS. Fresh executor session; not Session E, G, R or G2; no artefact, render, dump or note of any of them was present or read; the session scratchpad was empty at start (0 files). The withheld `shiu00-strings.md` was never opened, and neither was the Shiu source. Operator freshness confirmed at dispatch. |
| V2 | gate | THREE MATCHES. `sha256sum` over the three needed local PDFs returned exactly the Section 2.1 anchor lines: `df9614f4...26efc` for Maier-Primes-in-short-intervals.pdf, `c08c6582...fdca49` for 1005.4703v2.pdf, `407336f4...5e997` for 1110.6624v1.pdf. Verified before any source was opened. The Hildebrand-Maier source was not needed and not opened; anchor line 105 (Shiu) stayed out of scope. |
| V3 | gate | HOLD. P1 through P5 all hold; see Section 0. |
| V4 | gate | ALL NAMED PAGES ON DISK BEFORE EDITING, via the cheap safe superset: all 60 pages of the three sources (6 + 24 + 30) rasterised in this session at 200 dpi from the anchored bytes with `pdftoppm`, one invocation per source. Eight full pages re-rendered at high dpi for the glyph, delimiter and subscript decisions: Maier 1985 printed pp.222, 223, 224 at 400 dpi; 1005.4703v2 pp.10, 12, 21 at 500 dpi; 1110.6624v1 pp.10, 12 at 500 dpi; with sub-crops of the (6.4) region of p.21, the (3.23) region of p.12 and the Lemma 5.2 region of 1005.4703v2 p.12 read at full resolution. |
| V5 | gate | FOUR UNIQUE MATCHES. Each is-state was extracted byte-for-byte from the fenced blocks of the hashed G2 record (no retyping) and found byte-exact EXACTLY ONCE in its file, at exactly the recorded line: M2 at maier85 line 345, F10 at freiberg10 line 632, F11 at freiberg10 line 20, G4 at freiberg11 line 390. No should-state was present anywhere before the edits. |

## 3. The four record positions

Applied in file order and ascending extract line within each file
(M2; then F11 before F10, since F11 sits at line 20 and F10 at line 632;
then G4), each verified against this session's renders before the next
position started. Each replacement was performed programmatically with the
is-state and should-state taken byte-for-byte from the G2 record's own
fenced blocks, refusing unless the is-state occurred exactly once.

| position | file | edit applied | render verification | resulting line(s) |
| --- | --- | --- | --- | --- |
| M2 | maier85-shortintervals.md | yes | The repaired locator reads "(pp.223-224)". On this session's renders, p.223 ends mid-sentence with "In the sequel we assume that z -> infinity through a set" and p.224 opens with "of z for which P(z) is a good modulus in the sense of Lemma 1 and that z >= e^{cD}, where c is the constant in Lemma 2" -- the cited assumption straddles the break exactly as the G2 finding describes; both distinguishing components sit on p.224. Confirmed on 400-dpi renders of both pages. | 345-348 |
| F11 | freiberg10-strings1.md | yes | The repaired note attributes the calligraphic S to Section 5 and the calligraphic T and E to Section 4. Confirmed: the calligraphic S is first printed at Lemma 5.2 on p.12 ("Let S(x) denote the set of positive integers..."), inside Section 5 (500-dpi crop); the calligraphic T and E are printed as the starred T and E of (4.12) on pp.9-11, inside Section 4; and a page-by-page sweep of pp.6-11 (all of Section 4, which ends on p.11 above the Section 5 heading) found no calligraphic S anywhere. | 20-26 |
| F10 | freiberg10-strings1.md | yes | The repaired third sum of (6.4) now carries both printed subscript rows. Confirmed on the 500-dpi crop of the p.21 region: the index row "d_1,...,d_4" is printed above the condition row "[d_1,...,d_4]=D", and the should-state's `\substack` reproduces exactly those two rows. | 633 |
| G4 | freiberg11-strings2.md | yes | The repaired (3.23) chain carries the printed triple-sum member. Confirmed on the 500-dpi crop of the head of p.12: all three summation signs with their subscript rows -- outer "1 <= l <= (1/2) log t(H)" (the restricted range, distinct from (3.20)'s "log t(H)" on p.10), middle "p in I_l" over "p == a mod q", inner "m <= t(H)/e^l" over "p | m => p == 1 mod q" over "and p > log H" -- of the summand 1, followed by the printed main-term line and the unchanged trailing-factor line. The inner sum's three printed subscript rows are wrapped into two `\substack` rows exactly as the fixed reading (b) of report-G2 Section 5 D1 prescribes for this very sum; nothing printed is absent. One display block became two by design; the following line (now 392) is byte-unchanged. | 390-391 |

No position was blocked, none was approximated, and no fifth edit was made:
the diff of this apply over the three extracts is exactly the four positions.

## 4. Post-repair inventory (the Session G3 baseline)

| file | lines | objects | `$$` blocks | UNSURE | notes |
| --- | --- | --- | --- | --- | --- |
| maier85-shortintervals.md | 398 | 11 | 30 | 0 | 20 |
| freiberg10-strings1.md | 807 | 79 | 153 | 0 | 22 |
| freiberg11-strings2.md | 500 | 31 | 69 | 0 | 20 |

Line deltas against the G2 recount (398 / 806 / 499): F11 adds one line to
freiberg10 (the six-line note became seven); G4 adds one line to freiberg11
(one display became two). M2 and F10 are line-count-neutral. The `$$` column
counts lines opening with the display delimiter, per the G1 Section 5
methodology: G4 raises the freiberg11 count from 68 to 69 BY DESIGN; the
other two files are unchanged at 30 and 153. No verbatim-quoted numbered or
named object was added or removed -- no edit touched an object boundary --
so the object column carries the G2 recount unchanged. TRANSCRIPTION-UNSURE
markers: 0 in each file; the single literal occurrence per file is the FLAGS
line that reports the count. [extract note] lines: unchanged at 20 / 22 / 20
(M2 and F11 edit inside existing notes; neither adds one). Multi-line-display
closers, counted by the corrected report-G2 D3 reading and NOT by the
superseded report-R gloss: 2 / 0 / 0 (maier85 lines 86 and 151; neither
Freiberg file contains a multi-line display block -- both G4 lines open and
close their own delimiters). Surplus delimiter lines (delimiter not at line
start): 3 / 1 / 1, the Section 0 conventions note at line 15 in each file
plus the two maier85 closers. All three files are inside their symmetric
rule-23 envelopes: 398 in 394-402, 807 in 802-812, 500 in 495-505.

## 5. Observations NOT acted on

None. No new slip, misprint, divergence or doubt was noticed in any of the
three files or on any rendered page beyond the four repaired positions;
nothing tempted a fifth edit, so r29R2.7 had nothing to route here. No
fidelity doubt about any hashed file arose (r29R2.6); the three hashed
grade-chain artifacts were consumed read-only and verify at close.

## 6. STOP conditions

All ten reported by name, none fired.

- r29R2.1 validity failure: NOT FIRED. P1 held on its first branch (HEAD
  equalled the pin, empty diff); P2 ratified; P3 present and validating;
  P4 clean targets and three hash matches; P5 no prior report, no ANN-96.
- r29R2.2 source-hash mismatch: NOT FIRED. Three matches, checked before
  any source was opened.
- r29R2.3 untouchable touched: NOT FIRED. hildebrandmaier88-gaps.md,
  extract-grades-G1.md, extract-grades-G2.md and payloads/HASHES.txt appear
  in no diff of this apply; all verify against their hash lines at close.
- r29R2.4 spec ambiguity: NOT FIRED. All four is-states matched byte-exact,
  exactly once, at the recorded lines, and no should-state conflicted with
  this session's renders under the governing readings.
- r29R2.5 envelope breach: NOT FIRED. 398 / 807 / 500 against 394-402 /
  802-812 / 495-505, and this report is inside 100-300.
- r29R2.6 fidelity doubt about a hashed file: NOT FIRED. None arose.
- r29R2.7 scope pressure: NOT FIRED. No edit beyond the four positions
  appeared necessary or tempting; Section 5 is empty.
- r29R2.8 ANN sequence collision: NOT FIRED. ANN-20260802-96.yaml did not
  exist at session start.
- r29R2.9 close-gate failure: NOT FIRED. All Section 8 gates green at
  close; see Section 1.
- r29R2.10 instruction unsatisfiable or internally divergent: NOT FIRED.
  No divergence between the kickoff and the G2 record was found; the record
  was treated as governing throughout and every edit was taken from its
  fenced blocks. The one reading this session had to apply -- the G4
  should-state's two-row `\substack` for the inner sum's three printed
  subscript rows -- is the fixed reading (b) of report-G2 Section 5 D1,
  which names this exact sum as its example; applying it is not a
  divergence.

## 7. Budget reconciliation

| task | dispatch estimate | actual |
| --- | --- | --- |
| V-R2 table, gates at start, render pass | mechanical | as estimated; one `pdftoppm` invocation per source for the 60-page 200-dpi pass, eight high-dpi page re-renders, three sub-crops. |
| the four edits with per-position render verification | the bulk; F10 and G4 display surgery against 400-500 dpi crops, M2 a two-character locator widening, F11 a one-clause reattribution | as estimated. The byte-exact extraction of is/should-states from the record's own fenced blocks made each edit mechanical; the session's time went into the render verifications, including the six-page Section 4 sweep for F11's negative claim. |
| report, ANN, HANDOVER, close gates | mechanical | as estimated. |

All four positions were applied and verified; the STOP outcome was not
needed. No proof work, no computation beyond hashing, rendering and linting;
no Lean, no network, no roadmap edit, no extract content consumed for
item-0029 substance. The three repaired extracts REMAIN UNGRADED and carry
no standing until Session G3, the terminal re-grade of the operator-opened
second cycle, whose kickoff is authored ephemerally and which fixes the six
disclosed readings as governing. A repair shortfall discovered there cannot
loop again without a further operator decision.
