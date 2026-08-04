# item-0029 Session M run report -- the word-grain adjudication

Lane: EXECUTOR (local workstation, Claude Code; model string
claude-fable-5). Executed 2026-08-04 against the ephemeral kickoff
`item-0029-kickoff-M-v1.md` v1 (never committed; the operator apply is
the ratifying commit). Session M is the terminal, substantive session
of item-0029 under the ANN-20260801-91 frame, on the full four-extract
surrogate set ANN-20260803-97 licensed. Web OFF and cloud OFF for the
whole session; no PDF opened; `shiu00-strings.md` never opened.

Deliverables of this apply: `word-grain-adjudication.md` (699 lines),
`maier_matrix_sheet_29.py` (526), `maier_matrix_sheet_29_tables.txt`
(334), this report, plus the Section 7 bookkeeping (HASHES append,
ANN-20260804-98, HANDOVER deltas, roadmap done-move) in ONE apply
(rule 25).

**Headline: VERDICT V-NEG (bounded existence or weaker, at corpus
grain), by mechanical application of the S6 rule; all four clauses
fail. The two named findings F-CONS and F-MODEL are recorded in the
adjudication workpaper Sections 7-8.**

---

## 0. Section 0 pin and rule-18 delta (verbatim)

```
$ git rev-parse HEAD
7bed96ac7bd688025342d76dddf507a70682b09b
$ git diff --name-only 7bed96ac7bd688025342d76dddf507a70682b09b..HEAD
(empty)
```

HEAD equalled the Section 0 pin exactly; no rule-18 delta arose. The
working tree carried only the untracked ephemeral kickoff. P1 holds.

---

## 1. Gates at start and close

At start (all green, run before any output file existed):

```
python3 lean/scripts/blocks.py check-frozen        3x OK, byte-identical
python3 lean/scripts/blocks.py relocation-check    PASSED
grep -rnE '^\s*sorry\s*$' lean/Erdos251/           exactly Statement.lean:21
grep -c a6276f4c... lean/lake-manifest.json        1
tail -c 1 lean/lean-toolchain | od -c              \n
python3 scripts/ledger_check.py relocation-check   PASSED
python3 scripts/ledger_check.py validate           passed (97 entries)
python3 scripts/ledger_check.py append-only --base <pin>  0 changes, additions only
python3 scripts/writeup_mapper.py check ...        PASS
python3 scripts/mathjax_lint.py                    157 files, 0 problems
roadmap.py show item-0029                          status: ratified
scratchpad                                         empty at start
```

At close, wave 1 (run after the three substantive deliverables were
frozen and before this report was hashed; all green):

```
check-frozen                                       3x OK, byte-identical
relocation-check (blocks)                          PASSED
sorry inventory                                    exactly Statement.lean:21
manifest rev count                                 1
toolchain trailing byte                            \n
ledger relocation-check                            PASSED
ledger validate                                    passed (97 at wave 1)
ledger append-only --base <pin>                    0 changes, additions only
writeup_mapper check                               PASS
mathjax_lint                                       158 files, 0 problems
  (word-grain-adjudication.md included; this report brings the close
  count to 159 = 157 + the two new .md, verified at wave 2)
roadmap show item-0029                             ratified (pre-done-move)
sha256 recheck, twelve consumed hashed inputs      12/12 OK
ASCII check, three frozen deliverables             0 non-ASCII bytes each
sheet re-run stability (V7 S1c)                    two runs byte-identical
S6 block byte-identity (workpaper vs tables)       BYTE-IDENTICAL
```

At close, wave 2 (run after this report was frozen and the Section 7
bookkeeping landed; outcomes recorded here as the expected state and
restated with the invariant recheck in ANN-20260804-98, per the D2
disclosure in Section 4):

```
mathjax_lint                                       159 files, 0 problems
ledger validate                                    passed (98 entries)
ledger append-only --base <pin>                    additions only
roadmap show item-0029                             done, at completed/
sha256 recheck, four appended HASHES lines         4/4 OK against disk
duplicate-identifier check, payloads/HASHES.txt    118 identifiers, 118 distinct
ASCII check, every new/edited file of the apply    0 non-ASCII bytes
git diff --name-only <pin>..HEAD                   exactly the Section 9 list
```

No `lake` invocation was made at any point (kickoff 4.7).

---

## 2. The V-M table (one line per row)

- V1 freshness: HOLDS -- none of Sessions E/G/R/G2/R2/G3; scratchpad
  empty at start; `shiu00-strings.md` never opened; no PDF opened
  (one metadata disclosure, Section 4 D1).
- V2: HOLDS -- all twelve hashed inputs (lines 108-114, 78, 81,
  102-104) verified byte-identical before first consumption, and
  again at close.
- V3: HOLDS -- P1-P5 all hold at session start (P1 pin exact; P2
  ratified at order position 1; P3 ANN-97 present, validate passed at
  97; P4 the twelve verifications; P5 no output path, no HASHES line
  for one, no sequence-98 annotation).
- V4: CONFIRMED on all four ANN-91-booked purposes, with two
  precisions recorded in the workpaper Section 1 (freiberg11's
  Selberg-Delange attribution lives in the scope declaration; maier85
  cites Gallagher by name in a lemma heading, [3] absent from the
  body). No correction was needed; nothing was absorbed.
- V5: CONFIRMED -- the freiberg11 PARTIAL scope is declared in header
  and scope-boundary section and honoured; no adjudication clause
  rests on Section-4-only content beyond its named reference.
- V6: CONFIRMED -- the category-grain prior reads exactly as quoted
  (W4.U20.4; literature-consolidation Section 2 A3 line); held as
  prior only.
- V7: HOLDS -- S1a reproduces the anchored F17.9 column
  (6.143/6.932/7.944/8.963); S1b reproduces the named method-side
  printed numeric (1/2)(1-1/e)e^(gamma/2) = 0.42... > 2/5
  (freiberg11-strings2.md p.13); S1c two full runs of the sheet
  emitted byte-identical tables files (sha256-compared).

---

## 3. Task summary (pointers only)

- Task A (schema reconstruction): workpaper Section 3, elements
  A-1..A-8, each with extract citation, support class as documented,
  and quoted statement.
- Q-CORR: workpaper Section 4 -- CORR-NOT-ESTABLISHED, three missing
  elements named (m1 matching flanks uncontrolled; m2 the family
  index fixes admissible offsets, not the flank word; m3
  consecutiveness not forced at growing flank length).
- Q-SHAPE: workpaper Section 5 -- not SHAPE-POSITIVE-PROPORTION
  anywhere; a PROVED fixed-rank existence statement with growing
  count of two-distinct-middle flank classes (Section 5.2, the
  per-middle-ceiling derivation); SHAPE-NOT-DERIVABLE at the growing
  D0 depth; both bucket readings stated, same clause outcome.
- Task B (rule-15 sheet): `maier_matrix_sheet_29.py` /
  `_tables.txt` -- columns CM-1..CM-6 with support classes and
  citations; self-checks S1a/S1b in-script, S1c recorded here.
- S6 verdict: applied mechanically; V-NEG with per-clause failing
  elements and STRUCTURAL/EVIDENTIAL classes; rule text and verdict
  block byte-identical between workpaper Section 6 and the tables
  file; strongest supported shapes recorded per the rule's final
  clause (value axis, row-count axis, family axis).
- Findings: F-CONS (workpaper Section 7) and F-MODEL (Section 8, six
  input adjudications: three FAIL PROVED, one upper bound FAILS
  PROVED, one holds, two families OPEN/untested), each with support
  per clause and a both-readings entry (Section 10).
- Rule-16(a) pass: workpaper Section 9; no promotion, no dropped
  qualifier.

---

## 4. Deviations and judgment calls (each disclosed with reasoning)

- D1 (metadata touch of the withheld extract). An early `wc -l` glob
  over `extract/*.md` included the gitignored `shiu00-strings.md` in
  its line-count listing (650). Content was never read; the file was
  never opened; every subsequent command named files explicitly. A
  line count is metadata, not content, so V1/r29M.3 are read as
  holding; disclosed so a later session can overrule that reading.
- D2 (close-gate recording order). The kickoff asks both gate runs to
  be recorded verbatim in this report, but several close gates can
  only run after this report is frozen and hashed (its own HASHES
  line, the 118-identifier recheck, ledger validate at 98, the
  done-move state, the final diff list). Resolution, following the
  item-0028 precedent: wave 1 is recorded verbatim above; wave 2 is
  recorded as the attested expected state here and restated with the
  invariant recheck in ANN-20260804-98, which travels in the same
  apply. Any wave-2 failure is a STOP (r29M.9) and would void the
  apply before commit.
- D3 (in-session adversarial verification). Before freezing, the
  session ran local multi-agent verification passes (local
  workstation only, web OFF, no PDF; agents read only in-tree
  md/py/txt files, the withheld extract excluded by instruction) over
  the drafted deliverables: six lenses (quote fidelity, finite
  algebra, promotion discipline, sheet arithmetic, contract
  compliance, adversarial re-derivation), then a focused re-check of
  the repaired material. The passes found and the session repaired:
  (i) the draft's Q-SHAPE under-claim -- the adversarial
  re-derivation located the per-middle-ceiling route (Lemma 3 with
  the hm88 Section 4.2 column count) that PROVES distinct middles at
  fixed rank, which the draft had recorded as absent; adopted into
  Section 5.2/CM-5b after independent confirmation, and the S6
  clause-(a) text, F-CONS(ii), and the strongest-shape record were
  rewritten accordingly (the V-NEG letter is unchanged); (ii) a
  margin-formula/conclusion pairing defect in the draft CM-5a (flank
  vs complete-word capacity), repaired by pricing both margins;
  (iii) a growth-class label (CM-3a GC-ITLOG, not GC-FASTER); (iv)
  the model-translate constant R/(2m) and the Lemma-3-at-2R range
  note in F-MODEL item 4; (v) citation and vocabulary precision items
  (support-class names unified to the kickoff vocabulary; the
  freiberg11 Lemma 3.2/3.3 proof-line split; the hm88
  abstract-vs-Theorem quote locator; the f11 share-discount minus
  one; A-3/A-5 quote and class completions; F-CONS both-readings
  entry added). This use of local agents is a verification
  instrument, not a consumption channel: every adopted statement was
  re-derived against the extracts and carries its own citation.
- D4 (reference constants in sheet columns). CM-1/CM-2/CM-4/CM-5
  price documented shapes at named reference parameters (D=2, T=5,
  k=5, c=1, C'_k=1), each marked reference-only where the source's
  constant is undocumented; only asymptotic statements are labelled
  PROVED. Accepted nits from the focused re-check, disclosed rather
  than repaired: the k>=2 qualifier on the class-count divergence is
  stated in Section 5.2 but elided in the summary lines (degenerate:
  word-grain families need k>=3); two implied constants are written
  >>_k where >>_{k,T} would be strict; T=5 at k=5 is not
  source-certified as satisfying hm88's T > max(2,c) (covered by the
  reference-only flag).
- D5 (S6 byte-identity mechanics). The workpaper carries the S6 block
  inside a fenced code block whose content was injected
  programmatically from the emitted tables file and diff-verified
  byte-identical, so the two copies cannot drift.
- D6 (V-M placement). The one-line V-M table lives here (Section 2)
  per the kickoff's Section 3; the workpaper Section 1 carries the
  record rows' confirm-or-correct detail.

---

## 5. STOP-AND-REPORT conditions (all ten by name)

- r29M.1 validity failure: DID NOT FIRE (P1-P5 held; pin == HEAD).
- r29M.2 input-hash mismatch: DID NOT FIRE (12/12 at start and close).
- r29M.3 freshness breach: DID NOT FIRE (see D1 disclosure; no
  content of the withheld extract or any PDF was opened; web and
  cloud untouched).
- r29M.4 scope pressure: DID NOT FIRE (no step required a PDF, web,
  new extraction, edit to hashed files, re-grade, Lean edit, writeup
  edit, bet edit, or measurement run).
- r29M.5 Shiu dependence: DID NOT FIRE as a stop -- no load-bearing
  element was reachable only through Shiu-2000-only content; the
  OUT-OF-REACH marker is recorded (workpaper A-6(3), Section 7) and
  every S6 clause was determined without it. The operator's standing
  rule-26(5) question is untouched.
- r29M.6 envelope breach: DID NOT FIRE (699 / 526 / 334 / this
  report, all inside their envelopes).
- r29M.7 fidelity doubt: DID NOT FIRE (no suspected defect in any
  graded extract surfaced during consumption).
- r29M.8 verdict undecidable: DID NOT FIRE -- the one bucket-fit
  question (fixed-k existence vs proportion-not-derivable) gives the
  same clause (a) outcome under both readings, both stated
  (workpaper Section 5.2 Determination); no clause outcome differed
  between readings, so the rule's choose-neither trigger never arose.
- r29M.9 close-gate failure: DID NOT FIRE (wave 1 verbatim above;
  wave 2 attested and restated in ANN-98).
- r29M.10 sequence collision / unsatisfiable instruction: DID NOT
  FIRE (no annotation with sequence 98 existed; no contradictory
  clauses surfaced).

---

## 6. Budget reconciliation

| task | estimate (kickoff Section 11) | actual |
| --- | --- | --- |
| V-M, start gates, twelve verifications | mechanical | mechanical, as estimated |
| Task A read | the bulk; 398+807+500+492 lines plus anchors | all four extracts and every Section 2.2 anchor read in full |
| Q-CORR / Q-SHAPE | the substantive core | as estimated, plus one repair round after the in-session verification located the stronger fixed-rank derivation |
| Task B sheet | comparable to the 525-line item-0028 sheet | 526 lines, sieve-light (theta and V(z) by sieve over z <= 1152) |
| Findings | prose over Task A plus quoted priors; elementary model checks | as estimated; four PROVED model failures, one hold, two OPEN |
| Write-up, rule-16(a), both-readings, residuals | one careful pass | one pass plus the envelope-driven compression pass |
| Bookkeeping | mechanical | mechanical, one apply |

No budget overrun; the session finished inside one continuous run.

---

## 7. Terminality

The roadmap done-move is recorded: item-0029 is CLOSED AS DONE by
this apply, moved to `roadmap/completed/item-0029.md` with a Final
summary, and dropped from `roadmap/_order.md` (tool-executed; effects
verified via `order` and `show`). BET-20260725-12 STILL BINDS AND
STAYS OPEN for operator judgment against the item-0029 finding,
resolve_by 2026-09-30; no bet was scored, re-priced or amended and
`ledger/bets.yaml` is byte-untouched. The Shiu 2000 standing question
(ANN-92) is carried forward unchanged and remains the operator's
alone: the source stays anchored with no in-tree surrogate, and
nothing in this session consumed it in any direction. This session
took no step beyond the item's single gate and its two named
findings: no verdict on S1, (CG), B2.pairs, or the item-0010 campaign
state is recorded anywhere in this apply, and no proof work toward
any of them was attempted.

END OF ITEM-0029 SESSION M RUN REPORT
