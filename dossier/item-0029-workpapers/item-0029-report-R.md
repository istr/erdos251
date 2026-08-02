# item-0029 SESSION R (repair) -- run report

Lane: EXECUTOR (local workstation, Claude Code). Web OFF, cloud OFF for the
entire session. Executor model: claude-opus-5. Date of run: 2026-08-02.

This session is FRESH in the rule-26(3) sense: it is neither the Session E nor
the Session G session, inherits no context, notes, renders or text-layer dumps
from either, and did not read the withheld executor-local `shiu00-strings.md`.
Everything verified against the sources below was produced inside this session
from the anchored bytes. This session graded nothing, hashed nothing and
verdicted nothing, its own work included.

## 0. Pin and rule-18 delta

P1 outcome, verbatim from the session-start check:

```
$ git rev-parse HEAD
3f4cf39a796776eafea2fb9a314eaf575597c46f
$ git status --short
?? item-0029-kickoff-R-v1.md
$ git diff 3f4cf39a796776eafea2fb9a314eaf575597c46f..HEAD --name-only
(no output)
```

HEAD equals the Section 0 pin exactly, so the first branch of P1 holds and NO
RULE-18 DELTA ARISES. The only untracked path at session start was the ephemeral
kickoff itself, which is never committed.

P2: `roadmap/item-0029.md` frontmatter reads `status: ratified`. Holds.

P3: `ledger/annotations/ANN-20260802-93.yaml` exists (10670 bytes) and
`python3 scripts/ledger_check.py validate` passed. Holds.

P4: the three repair targets exist under `dossier/item-0029-workpapers/extract/`
exactly as committed at the pin -- `git status --short` reports nothing under
that path -- and both hashed session-G artifacts verified against their
`payloads/HASHES.txt` lines (108 and 109) before any edit was made. Holds.

P5: `dossier/item-0029-workpapers/item-0029-report-R.md` did not exist at
session start; `ls` returned "Datei oder Verzeichnis nicht gefunden". No prior
partial repair state. Holds.

## 1. Gates at start and close

Every Section 8 gate was run twice, once before any edit or output file was made
and once after all outputs existed. Verbatim close-run outputs:

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
  8 post-pin entr(ies), out of scope here, covered by append-only
RELOCATION CHECK PASSED -- concatenation is byte-identical to the old body.

$ python3 scripts/ledger_check.py validate
  94 entries, sequence numbers up to 94, 13 bets
  4 grandfathered malformed refs (allowlist size 4)
VALIDATE: passed.

$ python3 scripts/ledger_check.py append-only --base <the Section 0 pin>
APPEND-ONLY: 1 change(s) under ledger/annotations over 3f4cf39a796776eafea2fb9a314eaf575597c46f..HEAD, additions only.

$ python3 scripts/writeup_mapper.py check --manifest writeup/sources.yml
PASS

$ python3 scripts/mathjax_lint.py
MATHJAX LINT: 152 file(s) checked, 0 problem(s)

$ python3 .agents/skills/roadmap-items/scripts/roadmap.py show item-0029
status: ratified

ASCII check: 0 non-ASCII bytes in each of the three edited extracts, in the new
report and ANN-20260802-94.yaml, and in the edited HANDOVER.md.

sha256 recheck of the two hashed session-G artifacts against payloads/HASHES.txt:
dossier/item-0029-workpapers/extract/hildebrandmaier88-gaps.md: OK
dossier/item-0029-workpapers/extract-grades-G1.md: OK

$ git diff --name-only <the Section 0 pin>..HEAD
HANDOVER.md
dossier/item-0029-workpapers/extract/freiberg10-strings1.md
dossier/item-0029-workpapers/extract/freiberg11-strings2.md
dossier/item-0029-workpapers/extract/maier85-shortintervals.md
dossier/item-0029-workpapers/item-0029-report-R.md
ledger/annotations/ANN-20260802-94.yaml

$ git status --porcelain
?? item-0029-kickoff-R-v1.md
```

The apply is exactly the six files of Section 9. The one path left untracked is
the ephemeral kickoff itself, which is never committed. The two gates whose
output depends on whether the commit exists are recorded above in their
post-commit form, which is the state a later session can reproduce:
`append-only` reads 1 change over the pin..HEAD range, additions only (it reads
0 while the outputs are still uncommitted), and `git diff --name-only` is empty
before the commit.

Start-run differences, all expected and all mechanical: `mathjax_lint` reported
151 files at start against 152 at close (this report); `ledger_check.py
relocation-check` reported 7 post-pin entries at start against 8 at close
(ANN-94); `ledger_check.py validate` reported 93 entries at start against 94 at
close; and `append-only` is a close-only gate and was not run at start.
`roadmap.py show item-0029` reported `status: ratified` at both runs. The
roadmap tool was invoked at `.agents/skills/roadmap-items/scripts/roadmap.py`.
No `lake` invocation was made. `payloads/HASHES.txt` is byte-unchanged and was
not opened for writing at any point.

## 2. Verification table V-R

| row | class | outcome |
| --- | --- | --- |
| V1 | gate | HOLDS. Fresh executor session; not Session E, not Session G; no artefact, render, dump or note of either was present or read; the session scratchpad was empty at start. The withheld `shiu00-strings.md` was never opened, and neither was the Shiu source. |
| V2 | gate | THREE MATCHES. `sha256sum` over the three needed local PDFs returned exactly the Section 2.1 anchor lines: `df9614f4...26efc` for Maier-Primes-in-short-intervals.pdf, `c08c6582...dca49` for 1005.4703v2.pdf, `407336f4...5e997` for 1110.6624v1.pdf. Verified before any source was opened. The Hildebrand-Maier source was not needed and not opened; anchor line 105 (Shiu) stayed out of scope. |
| V3 | gate | HOLD. P1 through P5 all hold; see Section 0. |
| V4 | gate | ALL NAMED PAGES ON DISK BEFORE EDITING, as a superset: 60 pages (6 + 24 + 30) rasterised in this session at 200 dpi from the anchored bytes with `pdftoppm`, which covers every page named in the thirteen defect rows or their findings. Six page regions were re-rendered at 300-500 dpi to settle single-glyph and delimiter decisions -- Maier p.222 at 400 dpi, 1005.4703v2 p.7 at 300 dpi, p.10 and p.17 at 500 dpi, 1110.6624v1 p.11 at 400 dpi (two regions) -- each named in the position it settles. |
| V5 | gate | THIRTEEN UNIQUE MATCHES. Each recorded is-state was found byte-exact, exactly once, in its file: M1 at 394; F1 at 26; F5 at 73; F2 at 258; F3 at 333; F4 at 534; F6 and F7 in the single four-line note opening at 748 and spanning the recorded lines 750-751; F8 at 755; F9 at 758; G1 at 372; G2 at 375; G3 at 379. No miss, no multiple match, nothing guessed. |
| V6 | gate | PRESENT AS DESCRIBED. `freiberg11-strings2.md` declared its section-sign folding in its FLAGS section (the last bullet) and its Section 0 carried four conventions notes, none of them that declaration. `freiberg10-strings1.md` carries the pointer-back-to-Section-0 style in its own FLAGS, which R-A follows. |

## 3. The fourteen positions

Each row was edited byte-for-byte to the should-state printed in the grade
record, and then verified against this session's own renders of the source pages
named in that row's finding before the next position was started.

| position | file | applied | render verification | line after repair |
| --- | --- | --- | --- | --- |
| M1 | maier85-shortintervals.md | yes | p.222 at 400 dpi prints `LEMMA 2 (Gallagher).` in the body; pp.221, 222, 223, 224 and the p.225 body carry no bracketed [3], which appears only as reference-list entry 3 on p.225. Repaired sentence states exactly that. | 394-396 |
| F1 | freiberg10-strings1.md | yes | p.1 carries only the arXiv stamp `arXiv:1005.4703v2 [math.NT] 26 Aug 2010` and no journal line; the arXiv-only first sentence stands and the imported-bibliography sentence with its ledger identifier is gone. | 26-27 |
| F5 | freiberg10-strings1.md | yes | p.2 carries the `2. PRELIMINARIES` heading and p.4 carries (2.12) with the closing sentence above the `3. PROOF OF THEOREM 1.1` heading, so the section runs pp.2-4. | 72 |
| F2 | freiberg10-strings1.md | yes | p.7 at 300 dpi prints brace, open paren, the k-series, close paren, minus k, open paren, the 1-series, close paren, close brace. Repaired display reproduces that delimiter structure with `\lbrace` and `\rbrace`. | 257 |
| F3 | freiberg10-strings1.md | yes | p.10 at 500 dpi prints the second summation condition as d, ellipsis, d-sub-kappa with the first factor unsubscripted, against the subscripted numerator and denominator. Repaired display transcribes the slip as printed. | 332 |
| F3 (FLAGS) | freiberg10-strings1.md | yes | same render; the slip is added as the fifth item of the FLAGS print-slip list, naming p.10, in that list's existing style. | 800-801 |
| F4 | freiberg10-strings1.md | yes | p.17 at 500 dpi prints the two conditions as p not-congruent 1 mod q and p congruent 1 mod q, with no prime on either. Repaired display carries the unprimed variable in the second. | 533 |
| F4 (FLAGS) | freiberg10-strings1.md | yes | same render; the slip is added as the sixth item of the FLAGS print-slip list, naming p.17, in that list's existing style. | 802-803 |
| F6 | freiberg10-strings1.md | yes | p.8 prints the evaluation of G(0,0;Omega) with "The last product is ~ 1 by (2.1)."; p.9 carries (4.9)-(4.12) and no occurrence of G(0,0;Omega); p.11 prints the second invocation. Page numbers now pp.8, 11. | 749 |
| F7 | freiberg10-strings1.md | yes | p.17 opens with "Proof of Proposition 2.3." and the invocation "If p_0 != 1 then by (2.1)"; p.16 carries (5.19)-(5.23) and the Lemma 5.5 statement only. Page number now p.17. | 750 |
| F8 | freiberg10-strings1.md | yes | p.6 prints the Lemma 4.1 statement and the opening of its proof; p.8 opens with "by the prime number theorem, because Delta <= H^binom(k,2). Exponentiating and letting H tend to infinity yields (4.5)." carrying the closing box. Range now pp.6-8. | 754 |
| F9 | freiberg10-strings1.md | yes | same p.16 and p.17 renders as F7: the printed proof of Proposition 2.3 occupies p.17. Page number now p.17. | 757 |
| G1 | freiberg11-strings2.md | yes | p.11 at 400 dpi prints the whole logarithm inside a parenthesis pair carrying the exponent 1+o(1). Repaired inline form reproduces the outer pair. | 376 |
| G2 | freiberg11-strings2.md | yes | p.11 at 400 dpi prints two nested pairs, one around the quotient argument and one around the whole logarithm carrying beta. Repaired display carries both. | 379 |
| G3 | freiberg11-strings2.md | yes | p.11 at 400 dpi prints both the numerator and the denominator of that fraction with the logarithm's argument parenthesised. Repaired display carries both forms alike. | 383 |
| R-A | freiberg11-strings2.md | yes | the declaration sentence moved verbatim into the Section 0 conventions list, with only the deixis "above" fitted to "below" for its new position and the FLAGS bullet label dropped; the declared convention's content is unchanged. FLAGS retains a pointer back to Section 0 in the `freiberg10-strings1.md` style. The declaration itself is true of the source: p.3 at 400 dpi prints the section sign in "[2, 6.2]", "[2, 4, 7]", "[2, 7]" and "[2, 5]". | Section 0 at 22-25; FLAGS pointer at 498-499 |

All fourteen positions were applied and verified. No position was blocked, no
position was approximated, and no fifteenth edit was made.

## 4. Post-repair inventory (V7 baseline for the terminal re-grade)

| file | lines | quoted objects | `$$` blocks | TRANSCRIPTION-UNSURE | [extract note] lines |
| --- | --- | --- | --- | --- | --- |
| maier85-shortintervals.md | 398 (was 397) | 11 (unchanged) | 30 (unchanged) | 0 | 20 (unchanged) |
| freiberg10-strings1.md | 806 (was 804) | 79 (unchanged) | 153 (unchanged) | 0 | 22 (unchanged) |
| freiberg11-strings2.md | 499 (was 497) | 31 (unchanged) | 68 (unchanged) | 0 | 20 (was 19) |

The `$$` column counts lines opening with the display delimiter, as the grade
record's V7 recount does; the surplus lines carrying the delimiter elsewhere are
the closers of multi-line blocks and remain 3, 1 and 1. The TRANSCRIPTION-UNSURE
column is the count of unsure markers, zero in all three; the single literal
occurrence of the token in each file is the FLAGS line reporting the count.

Line deltas, each accounted for: maier85 +1, the M1 should-state being three
lines against a two-line is-state. freiberg10 +2, that is -1 for the F1 sentence
removal and +3 for the two FLAGS print-slip items. freiberg11 +2, that is +4 for
the moved declaration in Section 0 and -2 for the shorter FLAGS pointer.

The one inventory column that moves is `freiberg11-strings2.md`'s
[extract note] count, 19 to 20: position R-A converts a FLAGS bullet into a
Section 0 conventions note, and Section 0 notes carry the [extract note] marker
while FLAGS bullets do not. FLAGS bullet counts are unchanged at 6 / 7 / 7. No
numbered or named object was added, removed or renamed by any of the fourteen
positions, so the quoted-object counts stand at 11 / 79 / 31.

Envelope check (rule 23, symmetric): 398 in 392-404; 806 in 797-812; 499 in
491-505; this report inside 100-300. None was padded or trimmed to fit.

## 5. Observations not acted on

O1. `freiberg10-strings1.md` line 749 now reads "(pp.8, 11)". The two pages are
the two Section 4 invocations of (2.1) and are correct as repaired, but the
extract's own structural-map item 3 gives Section 4 as pp.6-11 while item 6
gives Lemma 5.5 as proved on pp.17-20; those ranges were not in any defect row
and were not re-verified by this session. Stated only so the re-grade knows
which map lines this session did and did not check.

O2. The FLAGS print-slip list of `freiberg10-strings1.md` is now ordered p.8,
p.11, pp.20-21, p.22, p.10, p.17: ascending by page for the first four items and
then the two appended ones. The record prescribes "fifth item" and "sixth item"
explicitly, so they were appended in that order rather than merged into page
order. No re-ordering was attempted.

O3. The moved declaration of position R-A contains one word this session
changed: "above" became "below", because the sentence's deixis pointed at the
transcription that follows Section 0 rather than precedes FLAGS. This is the
"minimal syntactic fitting" the kickoff licenses; it is recorded here because it
is the only wording change inside an otherwise verbatim move.

O4. No fidelity doubt about any hashed extract arose. `hildebrandmaier88-gaps.md`
and the five item-0022 extracts were not opened; r29R.6 did not trigger.

Nothing else was noticed that would have called for an edit. No extract content
was consumed for item-0029 substance at any point: no axis, no
positive-proportion gate, no named finding and no comparison to a project object
appears in this report or in any edit.

## 6. STOP conditions

All ten reported by name, none fired.

- r29R.1 validity failure (P1 content-path delta, P2, P3, P4, P5): NOT FIRED.
  HEAD equalled the pin with no delta at all, item-0029 was ratified, ANN-93
  existed and validated, the three targets were clean and both hashed artifacts
  verified, and no prior report-R existed.
- r29R.2 source-hash mismatch on any needed source (V2): NOT FIRED. All three
  matched, checked before any source was opened.
- r29R.3 untouchable touched or about to be: NOT FIRED.
  `hildebrandmaier88-gaps.md` and `extract-grades-G1.md` were opened read-only
  and still verify against their hash lines at close; `payloads/HASHES.txt` is
  byte-unchanged and appears in no diff of this apply.
- r29R.4 spec ambiguity: NOT FIRED. All thirteen is-states were found byte-exact
  and unique, every should-state was confirmed by this session's renders rather
  than contradicted, and the R-A source sentence was exactly as described.
- r29R.5 envelope breach, either direction: NOT FIRED. See Section 4.
- r29R.6 fidelity doubt about a hashed extract: NOT FIRED. None arose; see O4.
- r29R.7 scope pressure: NOT FIRED. No edit beyond the fourteen positions was
  made. The observations of Section 5 are recorded there and nowhere else, and
  no fifteenth edit exists in the diff, which is exactly the fourteen positions.
- r29R.8 ANN sequence collision: NOT FIRED.
  `ledger/annotations/ANN-20260802-94.yaml` did not exist at session start; the
  computed next number is 94.
- r29R.9 close-gate failure: NOT FIRED. All Section 8 gates are green at close;
  see Section 1.
- r29R.10 instruction unsatisfiable or internally divergent: NOT FIRED. No
  divergence between this kickoff and the grade record arose. One under-statement
  in the kickoff was resolved without a stop and is recorded here: the V4
  parenthetical named 1005.4703v2 pages 1, 4, 7, 8, 10, 11 and 17, while the
  findings of F5, F6, F7, F8 and F9 also name pp.2, 6, 9 and 16. The governing
  clause of the same row is "every source page named in any of the thirteen
  defect rows or their findings", so this session rendered all 24 pages of that
  source and all 30 of 1110.6624v1, a superset of both readings. A superset
  satisfies the gate under either reading, so no clause had to be chosen against
  the other and no interpretation was needed.

## 7. Budget reconciliation

| task | dispatch estimate | actual |
| --- | --- | --- |
| V-R table, gates at start, render pass over the named pages | mechanical | as estimated. One `pdftoppm` invocation per source produced all 60 pages; the six high-dpi region re-renders were cropped directly from the anchored bytes rather than upscaled. |
| the fourteen edits with per-position render verification | the bulk; F2-F4 and G1-G3 single-display surgery, F5-F9 single numbers, M1/F1 single sentences, R-A one sentence move | as estimated in shape. The verification, not the editing, was the cost: five of the six page-reference rows needed two page lookups each, one to confirm the page the material is on and one to confirm the page it is not on. F3 and F4 needed the 500-dpi crops the record itself had used. |
| report, ANN, HANDOVER, close gates | mechanical | as estimated. |

Nothing was graded, hashed or verdicted, this session's own work included. The
three repaired extracts REMAIN UNGRADED and carry no standing: an ungraded or
defective extract directs attention at most (rule 26(1)). Standing over them is
the terminal re-grade session's to confer or withhold, and that session is the
last permitted pass of the ANN-20260801-91 cycle. No proof work, no computation
beyond hashing, rendering and linting; no Lean, no network, no roadmap edit.
