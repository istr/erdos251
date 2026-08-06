# item-0037 run report (HLQuantA vacuity audit)

Lane: EXECUTOR (local workstation, Claude Code; model string
claude-opus-5[1m], rule 26(3) session identity -- the dispatch asserted no
model string for the executor and this run records its own). Dispatch:
`item-0037-kickoff-v1.md` (ephemeral, never committed; operator-side sha256
canonical; the operator acceptance of this run's single output commit is the
ratifying act). Section 0 pin `4dd53babefa7579954cca7a1aa5c9687e663f8d3` ==
HEAD at session start; session ran and landed 2026-08-06. Environment: web OFF,
cloud OFF, corpus-only; no PDF and no source opened; zero edits under `lean/`;
no `lake`; no computation, no census, no `.py` artifact. Landing form: rule
28(a) IN-RUN BOOKING -- the two artifacts land with their booking (HASHES lines
127-128, ANN-20260806-105, three HANDOVER deltas, tool-executed roadmap
done-move) as ONE commit; nothing is pushed. BET-20260804-16 stays OPEN for
operator judgment against this audit; no bet is scored in-run (rule 28(iii)).

## 1. Verdict (V-37, clause by clause)

EMISSION: V-37 = CLEAR. No falsification instance documented in the CLEAN
`maier85-shortintervals.md` and `hildebrandmaier88-gaps.md` extracts
contradicts any instance of the frozen `HLQuantA` statement inside the card's
own quantifier ranges. The byte-fixed rule and its mechanical application are in
`hlquanta-vacuity-audit.md` Section 7; the rule block is reproduced there
verbatim from the dispatch Section 5.

- Label set: SEVENTEEN documented instances, all DISJOINT. Zero INTERSECTS
  (clause (b) does not apply: no instance lands inside all four axes, so no
  Q-BAND contradiction is available to write out). Zero UNDECIDED-IN-CORPUS
  (clause (c) does not apply: no missing anchor enters the verdict line).
  Clause (a) applies exactly.
- M-OSC (OSC-0..OSC-5): DISJOINT, primary separator Q-DOMAIN on the five
  short-window/matrix rows, Q-TUPLE on the prime-free sieve-function row.
- M-ROW (ROW-1..ROW-5) and BG-1: DISJOINT, primary separator Q-DOMAIN on the
  three matrix-carried rows, Q-TUPLE on the coprime-count, limit-point-measure
  and gap-ratio rows.
- M-AP (AP-1..AP-5): DISJOINT, primary separator Q-TUPLE on the two
  good-modulus existence rows, Q-DOMAIN on the two single-prime AP rows, and
  Q-BAND on AP-5 (hm88 Lemma 3), the corpus's only tuple-counting statement,
  whose implied constant is existentially quantified and undocumented.
- Q-UNIF-EDGE PASS (mandatory, workpaper Section 6): outcome is the dispatch's
  THIRD branch -- the documented scopes demonstrably CANNOT REACH the
  cumulative even-offset tuple count within the card's ranges. The argument is
  (L1) capacity + (L2) a mass floor `M_H(x) >= x exp(-(4+o(1))(lnln x)^2)`
  proved UNIFORMLY over the card's whole range + (L3) carrier cardinality
  `x^{1-1/D+o(1)}` for both documented matrices, plus three priced summations
  (subwindows, dyadic scales, admissible moduli). Support class PROVED
  throughout, with one RECORDED input ((q20), `log P(z)^D = D sum_{p<=z} log p
  asymp z`) and one PROVED-LEAN input (`Erdos251.sum_log_primesUpto_le`). No
  heuristic step enters any separator.
- Two sharpenings the pass produced, both new to the project record: the
  Q-UNIF edge is the face on which the documented mechanisms are FURTHEST from
  reaching (they do not vary with `H` at all, while the mass floor loses only
  `x^{o(1)}` there); and hm88 Lemma 3 is INELIGIBLE at the card's span edge --
  its own spacing hypothesis `|s_i - s_j| <= z^2` is incompatible with span
  `(log x)^3` for every modulus `P(z) <= x/2`, since (q20) forces
  `z = O(log x)`.
- BET-20260804-16 material: CLEAR is the bet's YES material; scoring is
  operator judgment, never in-run.

## 2. Gates

At start (all green; commands and outcomes):

- V1: `git rev-parse HEAD` = 4dd53babefa7579954cca7a1aa5c9687e663f8d3 = the
  Section 0 pin exactly; `git diff <pin>..HEAD` empty, so the rule-18 delta is
  EMPTY and both P0-a and P0-b hold trivially. PASS.
- V2: `python3 lean/scripts/blocks.py check-frozen` -- all three blocks
  byte-identical (`erdos_251_irrational`, `HLQuantA`, `CramerGranville`);
  `blocks.py extract HLQuantA` prints sha256 `5d1a63a8...b287a762`, equal to the
  `lean/frozen-blocks.yaml` manifest value. PASS.
- V3: `blocks.py relocation-check` PASSED (concatenation byte-identical to the
  old body); `scripts/ledger_check.py relocation-check` PASSED. PASS.
- V4: `ledger_check.py validate` passed (104 entries, 17 bets, 4 grandfathered
  refs); `ledger_check.py append-only --base <pin>` -- 0 changes, additions
  only. PASS.
- V5: `grep -rnE '^\s*sorry\s*$' lean/` -- exactly
  `lean/Erdos251/Statement.lean:21`. PASS.
- V6: mathlib pin `a6276f4c` present exactly once in `lean/lake-manifest.json`;
  `lean/lean-toolchain` ends in newline (0x0a); NO `lake` invocation made. PASS.
- V7: `sha256sum` on both extracts equals `payloads/HASHES.txt` lines 111 and
  108 (`901ec906...c65c09`, `9d0d8bc0...6dfffa`); `python3
  scripts/writeup_mapper.py check --manifest writeup/sources.yml` PASS;
  `python3 scripts/mathjax_lint.py` 0 problems over 169 files. PASS.
- V8: `roadmap.py show item-0037` status ratified; item-0037 the first line of
  `roadmap/_order.md`. PASS.

At close (all green; the one amended gate stated in place):

- W1: `git status --porcelain` shows exactly the Section 9 writes plus the
  untracked ephemeral kickoff file -- the item-0010/0035/0036 precedent, named
  here as the expected deviation. PASS.
- W2: `python3 scripts/mathjax_lint.py` over the tracked markdown tree
  including the two new files -- 0 problems. PASS.
- W3: ASCII scan over both new files -- 0 non-ASCII bytes. PASS.
- W4: workpaper 628 lines. The dispatch envelope [340, 520] was AMENDED BY
  OPERATOR INSTRUCTION mid-run to [340, 650] ("I approve a 650 line limit"),
  issued after the run reported envelope pressure; 628 lies in the amended
  band. PASS under the amended envelope, which is itself part of this report's
  record (Observations O2, Follow-up F-ENV).
- W5: `check-frozen` re-run at close -- all three blocks still byte-identical;
  `blocks.py relocation-check` PASSED; both extract sha256 re-verified against
  `payloads/HASHES.txt` at close, unchanged. PASS.
- W6: after staging: `ledger_check.py relocation-check` PASSED, `validate`
  passed (105 entries), `append-only --base <pin>` additions only. PASS.
- W7: `payloads/HASHES.txt` gains exactly TWO lines (127 workpaper, 128
  report), nothing above them touched; both re-verified against the files on
  disk after the append; the one-line-per-file invariant re-checked over the
  whole file. PASS.
- W8: roadmap done-move TOOL-EXECUTED (`roadmap.py done item-0037 --summary
  ...`); `roadmap.py show item-0037` status completed at
  `roadmap/completed/item-0037.md`; `roadmap/_order.md` lost its first line and
  now begins with item-0027. PASS.
- W9: rule-16(a) verdict-vs-body pass present as workpaper Section 9, re-run
  after the refuter repairs landed; `writeup_mapper.py check` PASS at close (no
  writeup file edited, no-regression confirmation). PASS.

STOP-AND-REPORT conditions, all ten reported by name:

- r37.1 (pin/anchor delta): NOT FIRED -- HEAD == pin, empty diff.
- r37.2 (frozen/extract drift): NOT FIRED -- `check-frozen` OK, `HLQuantA` at
  its frozen sha256, both extract hashes match HASHES lines 111 and 108.
- r37.3 (extraction demanded): NOT FIRED. No instance required a source beyond
  the two CLEAN extracts; all seventeen were decided in-corpus. Two escalation
  CANDIDATES are named in workpaper Section 13 as future operator-gated
  rule-26(5) events (an explicit-constant sieve upper bound at growing g --
  hm88 names "[4, Theorem 2.3]", Halberstam-Richert, without transcribing a
  constant -- and the Friedlander-Granville AP-uniformity zone); NEITHER is a
  missing anchor for any instance and neither enters the verdict line. The
  near-miss is disclosed here so the distinction is auditable.
- r37.4 (intersection found): NOT FIRED -- no instance lands inside all four
  axes.
- r37.5 (strengthening / analysis-lane fidelity): NOT FIRED. One drafted
  comfort reading was caught and REJECTED before it reached any clause (O1,
  F4); no fidelity question about either extract arose, so none was answered
  in-lane.
- r37.6 (envelope breach, symmetric): NOT FIRED under the operator-amended
  envelope (W4). It WOULD have fired against the dispatch envelope as
  authored; see O2.
- r37.7 (scope violation): NOT FIRED -- no item-0029/0035/0036 verdict
  re-opened or consumed, no verdict on S1, (CG) or B2.pairs, no proof work
  beyond the three elementary lemmas of workpaper Section 3, no Lean edit, no
  `lake`, no read-only anchor edited, no in-run bet scoring.
- r37.8 (booking-path breach): NOT FIRED -- the booking touches only
  `payloads/HASHES.txt`, `ledger/annotations/ANN-20260806-105.yaml`,
  `HANDOVER.md` and the tool-executed roadmap move. In particular
  `runs/README.md` was NOT edited (see F-ENV: the rule candidate is routed to
  the operator by name instead) and `ledger/bets.yaml` is byte-untouched.
- r37.9 (gate red): NOT FIRED -- every Section 8 gate green at start and at
  close.
- r37.10 (non-ASCII / MathJax): NOT FIRED -- 0 non-ASCII bytes and 0 mathjax
  problems on both committed files.

## 3. Observations

O1. IN-RUN ADVERSARIAL REFUTER PASS, DISCLOSED (item-0035/0036 precedent). The
run attacked its own draft with independent lenses -- separator validity, the
Q-UNIF-edge transport, the UNDECIDED question, the verdict emission -- and the
full record with the repairs it forced is workpaper Section 12 (F1-F7). The
three findings that changed the artifact rather than polishing it:

- F1. The first Q-DOMAIN separator was QUALITATIVE ("a short window is not a
  cumulative range"). With no lower bound on `M_H(x)` that does not exclude a
  window from swallowing the band -- an unstated strengthening. Repaired by
  proving the mass floor (L2) and routing every separation through the capacity
  comparison (L1). Without this repair the CLEAR would have rested on an
  unproved size comparison.
- F2. The draft used the SPARSENESS of the good-modulus scale set as a
  separator. INVALID: the card is universal in x above `x0`, so a violation at
  a single admissible scale, arbitrarily large, falsifies it. Repaired; scale
  sparsity is now RECORDED as scope and explicitly excluded from every
  separator (workpaper (E6)). This is the finding a naive audit of this item
  would most likely have shipped.
- F5. AP-5 was drafted UNDECIDED-IN-CORPUS on the ground that hm88 Lemma 3's
  implied constant is undocumented -- which would have made the verdict
  INCONCLUSIVE and VOIDED BET-16. Overturned against the anchor: the documented
  statement quantifies that constant EXISTENTIALLY, so it carries no strength
  that could contradict a specific two-sided factor, and the instance is
  decided DISJOINT on Q-BAND. The undocumented constant is recorded as a
  residual instead (workpaper Section 13), where it bounds what a SHARPER
  anchor could do, not what this one does. The verdict therefore turned on this
  finding, and it is stated here rather than absorbed.

Also sustained and repaired: F3 (Q-TUPLE is not a separator at `k = 1`, where
`H = {0}` makes the card a single-prime statement, so Q-DOMAIN is primary
throughout), F4 (a REJECTED comfort reading: the documented amplitude
`e^gamma/lambda_0 < 2` does NOT bound the oscillation, since (q2) lower-bounds
a limsup; nothing in either extract bounds the amplitude from above), F6 (the
`D = 1` corner of the maier85 matrix checked, not assumed away), F7 (instance
set swept for completeness; OSC-0 and BG-1 added, with V-A rows (q30)/(q31)
added under the same check). No sustained finding touched the emission.

O2. THE DISPATCH LINE ENVELOPE WAS TOO SMALL, AND THAT IS THE SECOND
RECURRENCE. The audit as delivered is 628 lines against a dispatch ceiling of
520. The operator amended the envelope to [340, 650] on being told, and gate W4
is checked against the amended band. THE OPERATOR RECORDS THIS AS THE SECOND
TIME THE STEERING LANE SET A BUDGET TOO SMALL FOR THE ARTIFACT IT ORDERED: the
first was item-0036, whose workpaper envelope [140, 460] was amended mid-run to
[550, 600] and landed at 566 (ANN-103, item-0036 report W5). Both amendments
were operator-issued after the executor reported pressure; neither was a
content defect. What is NEW and is disclosed here as an executor-side process
defect: on hitting the ceiling this run FIRST COMPRESSED the draft (V-A table
merged from 29 rows to 11, two scope paragraphs fused, the axis readings
inlined) and only then reported, so a silent quality loss preceded the report.
The compression was fully reverted after the amendment; the delivered artifact
is the uncompressed one, and rows (q30)/(q31) plus the OSC-5/BG-1 separation
paragraph were added afterwards on top of it. Compression under an
unnegotiated ceiling is exactly the rule-23 concern with the sign reversed --
rule 23 stops an artifact that comes in far UNDER its envelope by a mid-run
scope decision, and it does not reach an artifact silently thinned to fit a
ceiling.

O3. BUDGETS. Workpaper 628 lines (operator-amended envelope), report 281
lines, no `.py` artifact by design. One large/high session; network none, PDF
none, Lean build none. The rule-19 quotation check (31 rows, 56 pieces, 0
misses) ran from the session scratchpad and is NOT committed, per the
dispatch's no-`.py`-artifact clause; it is reproducible from the workpaper's
own quotation rows against the two hashed extracts.

O4. A REPOSITORY-INTEGRITY DEFECT OBSERVED AND DELIBERATELY NOT REPAIRED:
`ledger/bets.yaml` does not parse as YAML at this pin. `python3 -c "import
yaml; yaml.safe_load(open('ledger/bets.yaml'))"` raises
`ScannerError: mapping values are not allowed here, line 367`. The break was
introduced by the ANN-104 apply c1fc8c3 (the BET-15 scoring): the BET-15 block
carries `note: >-` BEFORE `outcome:`/`brier:`, and the scoring text was
appended after `brier: 0.0625` at note indent, so it is no longer a valid
mapping value. `git show 8a87149:ledger/bets.yaml` still parses; c1fc8c3,
164af1a and HEAD do not. NOT REPAIRED HERE: `ledger/bets.yaml` is outside this
run's granted booking paths (dispatch Section 9.2 requires it byte-untouched)
and touching it would trip r37.8. Consequences for a cold start: the file is
still readable by eye and `ledger_check.py validate` does not parse it as YAML,
so CI is green and nothing alerts; any consumer that YAML-loads bets.yaml fails
today. Routed to the operator as its own bookkeeping repair.

O5. The audit consumed no item-0029/0035/0036 result. That is a scope fact, not
an oversight: the dispatch's question is about the two extracts and the frozen
card only, and importing a project verdict would have made the corpus-relative
CLEAR harder to read, not easier.

## 4. Follow-up candidates (non-binding)

- F-ENV, the process step the operator ordered with the amendment: ADD A
  STOP-AND-ASK BEFORE COMPRESSING. When an artifact cannot be delivered inside
  its declared envelope (or any declared budget) without dropping content, the
  run STOPS and asks the operator for an envelope or budget decision BEFORE
  compressing; it does not compress first and report after. Rationale, from
  this run: compression to fit a ceiling is a silent scope decision taken by
  the executor, invisible in the delivered artifact, and it is the mirror image
  of the rule-23 undershoot the envelope stop already covers. Recommended
  landing: a new clause in `runs/README.md` (rule-23 family, or a rule 29) plus
  one line in the kickoff template beside the DECLARED LINE ENVELOPE. NOT
  applied by this run: `runs/README.md` is outside the granted booking paths
  (r37.8), so the candidate is routed by name.
- F-BETS: repair `ledger/bets.yaml` so it parses (O4), and consider adding a
  YAML-load assertion for it to `scripts/ledger_check.py validate` so the class
  of defect is mechanically caught -- the item-0032 lesson applied to the one
  ledger object the split left mutable.
- F-ANCHOR: if the operator ever wants the vacuity question closed beyond the
  documented zone, the two rule-26(5) extraction candidates are named in
  workpaper Section 13 (Halberstam-Richert Theorem 2.3 for an explicit sieve
  constant at growing g; the Friedlander-Granville AP-uniformity zone). Each is
  an operator-gated event with named anchor line, purpose and scope; neither is
  needed for this item's verdict.
- F-0027: this audit is the insurance the design note (Section 3.3, Section 7)
  wanted before item-0027 builds a Lean integrator around `HLQuantA`. The
  insurance now reads: no documented Maier-genre instance in corpus reaches the
  card, with the capacity argument stated so a future anchored mechanism acting
  on a positive-density set would visibly break it.

## 5. Artifact hashes (final bytes)

- hlquanta-vacuity-audit.md
  704b5e25214fe36b819da60c20425e7a09b3e631434fbbc56b5a1f03e93704b7
- item-0037-report.md: this file's own sha256 is stated in the hand-off message
  (operator-side hashing canonical) and booked as HASHES line 128.

Rule-28(a) form restated: artifacts and booking land as one commit; the commit
author string names the executor model; the run pushes nothing.
BET-20260804-16 stays OPEN for operator judgment against this audit; no bet is
scored by this apply.

END OF item-0037 RUN REPORT
