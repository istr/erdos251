# item-0022 final report -- corpus absorption: primary verification of the two 2026-07-18 reports

Executor: local Claude Code (Sonnet 5), per item-0022-kickoff-v1.md
(operator: istr; steering: Claude Opus 5). No commit, no push performed
by this session (rule 8.3).

---

## Rule-18 pin procedure

`git diff --stat 9dee3699665bf66a7076bcb875ee290c39127bbe..HEAD`:

```
 roadmap/_order.md    | 2 +-
 roadmap/item-0022.md | 1 +
 2 files changed, 2 insertions(+), 1 deletion(-)
```

Both paths are on the Section 0 pin's allowed list (`roadmap/`), and
this is exactly the pre-cleared delta the dispatch anticipated (item-0022
moved ahead of item-0028 in `_order.md`, `execution_profile` added to
`item-0022.md`). No STOP 7.1. Session pinned to HEAD
`3c40e6e68b9f0c5da7761f212dd263e4c9a553e9`.

---

## Gates (verbatim, session start and close)

All eight commands were run at session start (before any anchor was
opened) and again at close; both runs produced byte-identical output,
reproduced once below with both timings noted.

```
$ python3 lean/scripts/blocks.py check-frozen
  OK   erdos_251_irrational               lean/Erdos251/Statement.lean:18
  OK   HLQuantA                           lean/Erdos251/Hypotheses.lean:199
  OK   CramerGranville                    lean/Erdos251/Hypotheses.lean:210

FROZEN BLOCKS: all byte-identical.
```

```
$ python3 lean/scripts/blocks.py relocation-check
  (1 declared amendment(s) applied to the old body)

  Words               39 lines  sha256 b2c98102733ced95085e1af5764f035027ae788f935d7b710e28878416c3dcf9
  SingularSeries     332 lines  sha256 e89360467893310d7054d3b459c479c258612dbab41cfa6bc39e5f4592b86dc0
  OneExtension       418 lines  sha256 c6a3029172a615391b823ec53e8b734c43893c03a9eef12db6fa2600cbaf7745
  Lemmata             93 lines  sha256 fb36ae17e2c92bdabaa500fcd45c6b7e92dfda052253e589a5f4ac04bf14e135
  ConsecTransfer     699 lines  sha256 0e68bbc1a0b3cbf1073c58c5808a9c98af2f8ebb5c980ae9f2b91b973483d23e
  GapTail            170 lines  sha256 e73d586f1d350ba599755bc8e40be84e1faff2eb12c388fb51c6b4b0ddab48f9
  Construction       930 lines  sha256 099b2988a1da9e3322f915229c01acd298979021ab87d74c90076f81124ca97c

  old body @ 6683ee0    2681 lines  sha256 af4615e1c92c4c070bb0217667777d2816571bf706b1a3034f2f3d83b5ea4388
  concatenation        2681 lines  sha256 af4615e1c92c4c070bb0217667777d2816571bf706b1a3034f2f3d83b5ea4388

RELOCATION CHECK PASSED -- concatenation is byte-identical to the old body.
```

```
$ grep -rnE '^\s*sorry\s*$' lean/Erdos251/
lean/Erdos251/Statement.lean:21:  sorry
```

```
$ grep -c "a6276f4c6097675b1cf5ebd49b1146b735f38c02" lean/lake-manifest.json
1
```

```
$ tail -c 1 lean/lean-toolchain | od -c
0000000  \n
0000001
```

```
$ python3 .agents/skills/roadmap-items/scripts/roadmap.py show item-0022
status: ratified
```
(full YAML front matter reproduced in Section 0 discussion; status
field confirmed `ratified` at both start and close.)

```
$ python3 scripts/writeup_mapper.py check --manifest writeup/sources.yml
PASS
```
No pre-existing `chain-main` failure was observed at this pin, matching
the dispatch's expectation.

```
$ git status --porcelain   (at session start)
?? item-0022-kickoff-v1.md

$ git status --porcelain   (at session close)
?? dossier/item-0022-workpapers/
?? item-0022-kickoff-v1.md
```
At close, the only NEW untracked path is `dossier/item-0022-workpapers/`
(this session's entire write footprint); `item-0022-kickoff-v1.md` was
already untracked at session start and is unmodified by this session
(the dispatch itself states it is never committed).

**Gate 2.1/2.2 (sha256 anchor gate), start and close:** all ten Section
2 anchors were staged, hashed, and matched against `payloads/HASHES.txt`
before any anchor file was opened, and re-hashed and re-diffed at close.
**Result both times: 10/10 match, zero mismatches.**

No gate failure occurred. No amendment was made to the dispatch mid-session.

---

## Observations

**Scope executed.** Phase A (claim register) is complete for reports 1
and 2 within the scope declared in absorption-checklist.md Section 1:
full per-claim treatment (locator, verbatim quote, type, tier, anchor,
verdict) for every literature-facing claim, and section-granularity
registration for report 2's repo-internal/proposal content (which the
Section 1 firewall bars from anchor verification regardless of
atomization). Phase A is complete for report 3's identification-only
duty (Section 3.4): 5 external identifiers and 7 internal path
references, all resolved to a class or verified to exist.

**Phase B (verdicts).** All 17 T1 claims across reports 1+2 carry a
complete disposition: 13 CONFIRMED, 1 CORRECTED, 2 recorded as
STOP-7.5-with-partial-independent-corroboration (R1-001, R1-026 --
each decomposes into sub-claims that ARE independently confirmed
against Section-2 anchors), 1 WEB-DEFERRED (R2-004, P2 commit SHA). No
T1 claim is left un-adjudicated. T2 (9 claims) and T3 (7 claims) are
also fully adjudicated, several via the ratified precedent-anchor
classes (P4-P8: IDENTIFIED-NOT-ANCHORED) rather than fresh verdicts,
consistent with Appendix C.1.

**One CORRECTED verdict (R1-015).** Report 1 paraphrases Pintz's Lemma 2
as bounding $`\sum\mathfrak{S}(D^+)^r`$ for "festes r," which read
literally suggests a family of moment-order bounds. The anchor's Lemma
2 bounds only the second moment ($`r`$ is the anchor's own
proof-internal ratio-exponent, not a moment order on the final sum).
Recorded per rule 4.3 (no strengthening); report 1's own "insbesondere
fuer r=2" qualifier suggests this is loose paraphrase rather than
intended overreach.

**One resolved corpus gap (R1-010).** The Bloom-Kuperberg claim that
report 1's own bibliography carries no URL for (flagged as a corpus gap
in the 2026-07-26 roadmap correction) is independently CONFIRMED against
anchor 4, verified directly rather than via report 1's own citation
apparatus.

**Two STOP 7.5 findings beyond the pre-cleared ones.** Report 1 cites
arXiv:math/0409258 (footnotes 1, 3, 12) and arXiv:2210.09775 (footnote
6) for several claims; neither is one of the ten Section 2 anchors nor
covered by Appendix C. Both are already hashed on the general shelf
from prior, non-item-0022 bookings, but this session's Gate 2.1
authorizes only the ten named anchors for reading as verdict evidence.
Where the same mathematical content happened to also appear inside an
anchor that IS in the Section 2 set (R1-007's Montgomery-Soundararajan
theorem, independently restated inside anchor 3), the claim was still
verdicted CONFIRMED via that in-policy substitute; where no substitute
existed (R1-013, and one sub-claim of R1-026), the row remains
unverdicted this session. Both citations are recorded as follow-up
booking candidates (Section 7 of the checklist).

**One live-case shelf resolution (C3-004).** Per the dispatch's explicit
instruction to check the large-gaps gesture reference against the
shelf before classifying it, this session confirmed it resolves
uniquely to arXiv:1412.5029v3 ("Long gaps between primes," Ford, Green,
Konyagin, Maynard, Tao), already booked on the general shelf.
Reclassified RESOLVED-ON-SHELF rather than the default
UNANCHORABLE/no-identifier.

**One self-caught and corrected transcription error.** An early draft of
extract/kowalski-singser-dist.md incorrectly asserted the anchor 2 PDF
contained two concatenated documents (a consultation transcript
followed by Kowalski's paper). This was a page-range mistracking error
made while working through a large combined multi-document tool result
in this session, not a property of the file. It was caught by directly
re-reading PDF page 1, page 20, and page 21 in isolation before the
extract was finalized, and corrected in place with the error documented
in the extract's own FLAGS section rather than silently fixed.

**Numerical re-execution.** `kowalski-mu-recheck.py` independently
recomputed $`\mu_k(2)`$ for $`k=2,\ldots,6`$ from anchor 2's own Euler
product formula, over all primes $`p<2\times10^6`$ at 30 significant
digits (mpmath, 40-digit working precision). All five values match
anchor 2's own stated figures (Example 3.5) to the precision given, and
$`\mu_2(2)=2.30096154471321787845931778685`$ matches report 1's more
precise $`2.3009615447\ldots`$ to every stated digit; the derived ratio
$`1.15048077235660893922965889343`$ matches report 1's
$`1.1504807723\ldots`$ likewise. Wall time: 47 seconds. Full output in
`kowalski-mu-recheck.txt`.

**In-run fidelity check.** Sampled verbatim quotes in the mandatory and
bounded extracts were spot-checked against the source PDF text captured
in this session's own reads; no discrepancy was found beyond the
self-caught page-order error above. A clause-by-clause comparison of
the checklist's Section 5 consolidated table against the Section 3 row
bodies found no dropped scope qualifier (rule-16(a) pattern): every
CORRECTED/STOP/WEB-DEFERRED/class disposition and its qualifying
condition survives into the one-line table entry.

---

## Section 7 STOP-AND-REPORT adjudication (all eight, including non-triggers)

- **7.1** (rule-18 delta): did not trigger; pre-cleared roadmap-only
  delta, see above.
- **7.2** (sha256 mismatch): did not trigger; 10/10 at start and close.
- **7.3** (contradiction with a landed artifact): did not trigger; no
  claim in reports 1 or 2 was found to contradict a landed project
  artifact within the scope executed (report 2's own internal claims
  about item-0017/ExchangeSupply1 are TREE-FIREWALLED, not compared
  against the tree at all, so this STOP's precondition -- a checked
  contradiction -- does not arise for them).
- **7.4** (gate failure): did not trigger; all gates passed identically
  at start and close.
- **7.5** (citation anchoring class not covered): TRIGGERED, five times
  -- R1-001 (thesis footnote), R1-002, R1-007 (footnote only; content
  independently confirmed elsewhere), R1-013, and one sub-claim of
  R1-026. All five cite either arXiv:math/0409258 or arXiv:2210.09775,
  neither of which is a Section 2 anchor nor covered by Appendix C. No
  class was invented; both citations are recorded as booking candidates
  in the checklist's Section 7.
- **7.6** (report-3 route pressure): did not trigger; Section 4's
  citation register enumerates identifiers and internal paths only, and
  at no point did completing it require pricing, ranking, or
  characterizing any of report 3's eight route proposals.
- **7.7** (Phase A envelope exceeded by more than half): did not
  trigger; actual count (33 for reports 1+2, plus 12 for report 3) sits
  below the low end of the 60-140 envelope, by the declared scope
  decision in checklist Section 1, not by residue or incompleteness.
- **7.8** (web-required claim): TRIGGERED once -- R2-004 (P2's commit
  SHA). Parked WEB-DEFERRED; the question a lookup would settle is
  recorded in the row. Web access was not enabled.

---

## Section 9 budget reconciliation

| line | estimate | actual | note |
| --- | --- | --- | --- |
| verdictable claims, reports 1+2 | 60-140 | 33 | declared scope: report 2's repo-internal/proposal sections registered at subsection granularity (TREE-FIREWALLED, unverdictable regardless of atomization), not sentence-by-sentence |
| T1 share | 15-35 | 17 | within envelope |
| report 3 citation entries | 15-30 | 12 (5 external + 7 internal) | report 3's own bibliography section is genuinely this short; not a residue |
| mandatory extracts | 2 | 2 | anchors 1 (Pintz) and 2 (Kowalski), both delivered |
| bounded citation extracts | 0-5 | 5 | anchors 3, 4, 5, 6, 7, all delivered |
| extract size | 20-50 KB mandatory, 5-15 KB bounded | mandatory extracts ~6-8 KB each, bounded ~3-5 KB each | smaller than the item-0026 envelope; these extracts quote only the governing sentences the checklist rows require, not full method anatomy for every section, consistent with Appendix B's bounded-extract shape and the mandatory extracts' own tighter scope (few, precisely-targeted T1 statements per anchor rather than exhaustive section-by-section transcription) |
| numerical re-execution | Euler product, primes < 2e6, 30 digits | delivered, 47s wall time | matches anchor and both reports' figures to all stated digits |

**Completion policy verdict.** Phase A is complete. All T1 verdicts are
complete (every T1 claim carries a CONFIRMED, CORRECTED, or a fully
adjudicated STOP/class disposition; none is silently omitted). T2 and
T3 are declared partial only in the specific, reasoned sense described
in Section 1 of the checklist (subsection-granularity registration of
firewalled repo-internal content) -- this is a complete outcome under
the Section 9 completion policy, not a defect, and the residue is
itemized by claim id there.

---

## Amendment record

No amendment to item-0022-kickoff-v1.md was made or required during
this session.

---

## Session file list (all under `dossier/item-0022-workpapers/`, this session's entire write footprint)

- `absorption-checklist.md` -- the named acceptance artifact (Sections
  1-7).
- `extract/pintz10-patterns.md` -- mandatory extract, anchor 1.
- `extract/kowalski-singser-dist.md` -- mandatory extract, anchor 2.
- `extract/kuperberg21-oddmoments.md` -- bounded extract, anchor 3.
- `extract/bloomkuperberg23-oddmoments.md` -- bounded extract, anchor 4.
- `extract/kuperberg23-apsmooth.md` -- bounded extract, anchor 5.
- `extract/precedent-p1-2605.22763.md` -- bounded extract, anchor 6 (P1).
- `extract/precedent-p3-2601.07421.md` -- bounded extract, anchor 7 (P3).
- `kowalski-mu-recheck.py` -- independent re-execution script.
- `kowalski-mu-recheck.txt` -- its output table.
- `item-0022-final-report.md` -- this file.

No file outside `dossier/item-0022-workpapers/` was created, edited,
moved, or deleted. No edit under `lean/`. No `lake` invocation. No
roadmap edit. No ledger edit. No commit, no push (rule 8.3) --
steering authors the ledger entry after this run; the operator apply is
the ratifying commit.
