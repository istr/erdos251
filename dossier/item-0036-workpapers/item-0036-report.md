# item-0036 run report (rank-ceiling sheet)

Lane: EXECUTOR (local workstation, Claude Code; model string
claude-fable-5). Dispatch: `item-0036-kickoff-v1.md` (ephemeral,
never committed; operator-side sha256 canonical; the operator
acceptance of this run's single output commit is the ratifying
act). Section 0 pin `15aff75830f008b6bc38fc90cf4867600171d871` ==
HEAD at session start; session started 2026-08-05, landed
2026-08-06 (the ANN id carries the landing date). Environment: web
OFF, cloud OFF, corpus-only; no PDF opened, no source opened, zero
edits under `lean/`, no `lake`. Landing form: rule 28(a) IN-RUN
BOOKING -- the four artifacts plus this report land with their
booking (HASHES lines 123-126, ANN-20260806-103, three HANDOVER
deltas, tool-executed roadmap done-move) as ONE commit; nothing is
pushed. BET-20260804-15 stays OPEN for operator judgment against
this sheet; no bet is scored in-run (rule 28(iii)).

## 1. Verdict (V-36, clause by clause)

EMISSION: V-DIV-BELOW -- (P1) and (P2) both hold on BOTH named
hypothesis rows. The full byte-fixed rule and its mechanical
application are in `rank-ceiling-sheet.md` Section 5, byte-identical
with the RC-6 block of `rank_ceiling_sheet_36_tables.txt` (gate W9)
and, for the rule block itself, with the kickoff Section 1 bytes.

- Semantics: k*(x; H) is the ceiling of the documented item-0029
  Section 5.2 chain carried k-uniformly under row H, supremum over
  admissible couplings T = lambda c, c = 3k reference.
- Row H-EXP (C_g <= C^g, absolute C > 1): (P1) HOLDS -- lambda = 2,
  displayed schedule phi_EXP(x) = (lnln x)^{1/4} -> infinity, every
  chain step closing in the rule's either-PROVED-or-DEBT sense;
  (P2) HOLDS -- displayed envelope psi_EXP(x) = (3/4) lnln x /
  lnlnln x = o(lnln x), the (q10) margin failing asymptotically for
  every k >= psi_EXP and every fixed lambda > 1 (lambda-free).
- Row H-FACT (C_g <= exp(c_H g ln g), absolute c_H > 0): (P1)
  HOLDS (same coupling and schedule); (P2) HOLDS (same envelope;
  the row constant only deepens the failure).
- Binding walls, both sides named: NECESSITY W-A (Lemma-3 constant
  + Mertens power), lambda-free, margin dying at k = (theta*_H +
  o(1)) lnln x/lnlnln x, theta*_EXP = 1/2, theta*_FACT =
  1/(2+c_H); SUFFICIENCY W-B (Lemma-4 uniformization, the
  smooth-count constraint), per fixed lambda the CERTIFIED-CLOSURE
  ceiling class (lnln x/lnlnln x)^{1/lambda}, the lambda -> 1
  boundary DEBT (d5).
- FLAG guard: NO FLAG on any row or step (workpaper Section 7);
  STOP r36.6 not fired; no column consumes the HLQuantA card in
  any direction.
- DEBT ledger d1-d5 stands; no emitted class rests on a debt as a
  proved input. Grid values are reference-only (MEASURED), never
  load-bearing for (P1)/(P2).
- BET-20260804-15 material: the per-row (P1)/(P2) pairs are the
  bet's two halves; scoring is operator judgment, never in-run.

## 2. Gates

At start (all green; commands and outcomes):

- V1: `git rev-parse HEAD` = 15aff75830f008b6bc38fc90cf4867600171d871
  = the Section 0 pin exactly (no bookkeeping delta; P1 met on its
  first branch). PASS.
- V2: `sha256sum` over A1-A9 matched the kickoff Section 2 table on
  all nine lines. PASS.
- V3 (P2): `roadmap/item-0036.md` status: ratified; item-0036 the
  first item line of `roadmap/_order.md`. PASS.
- P3: last ledger annotation ANN-20260805-102;
  `payloads/HASHES.txt` exactly 122 lines. PASS (no r36.9).
- V4: `python3 lean/scripts/blocks.py check-frozen` -- all three
  blocks byte-identical (erdos_251_irrational, HLQuantA,
  CramerGranville). PASS.
- V5: `blocks.py relocation-check` PASSED; `scripts/ledger_check.py
  relocation-check` PASSED; `ledger_check.py validate` passed (102
  entries at start). PASS.
- V6: `grep -rnE '^\s*sorry\s*$' lean/` -- exactly
  `lean/Erdos251/Statement.lean:21`. PASS.
- V7: mathlib pin a6276f4c present once in `lean/lake-manifest.json`;
  `lean/lean-toolchain` ends in newline (0x0a). PASS.
- V8: both (q12) quotations byte-present inside the `open:` block of
  `ledger/bets.yaml` under whitespace normalization (the YAML line
  wrap). PASS.

At close (all green; the one amended gate and one named deviation
stated in place):

- W1: `git status --porcelain` shows exactly the Section 5 writes
  plus the untracked ephemeral kickoff file -- the item-0010/0035
  precedent, named here as the expected deviation. PASS.
- W2: `python3 scripts/mathjax_lint.py` over the two new .md files
  (workpaper, this report) -- 0 problems. PASS.
- W3: ASCII check over all five new files -- 0 non-ASCII bytes.
  PASS.
- W4: `sha256sum` over A1-A9 re-run at close -- unchanged on all
  nine. PASS.
- W5: workpaper 566 lines. The kickoff envelope [140, 460] was
  AMENDED BY OPERATOR INSTRUCTION mid-run ("I authorize an
  override to 550 to 600 lines", issued in the interactive session
  after the executor reported envelope pressure); 566 lies in the
  amended band. PASS under the amended envelope; the amendment is
  itself part of this report's record.
- W6: two invocations of `rank_ceiling_sheet_36.py` -- tables files
  byte-identical (also re-verified after the audit repairs). PASS.
- W7: rule-16(a) pass present as workpaper Section 9; re-run after
  the audit repairs; no verdict clause strengthens a body support
  class, no qualifier dropped. PASS.
- W8: after staging: `ledger_check.py relocation-check` PASSED,
  `validate` passed (103 entries), `append-only --base 15aff758...`
  PASSED. PASS.
- W9: the V-36 block byte-identical (cmp) between
  `rank_ceiling_sheet_36_tables.txt` and workpaper Section 5 (the
  full rule-plus-application region); the rule block additionally
  cmp-identical to the kickoff Section 1 bytes. PASS.

STOP-AND-REPORT conditions, all ten:

- r36.1 (Section 0 predicate / start gate): NOT FIRED.
- r36.2 (anchor hash mismatch): NOT FIRED.
- r36.3 (quotation not byte-present): NOT FIRED (V-A 15/15; the
  (q14) note in workpaper Section 1 records a kickoff-side
  rendering variance, resolved by the row's own "present as
  printed there" clause).
- r36.4 (RC-1 self-check miss): FIRED, by S1b as authored, and
  resolved as a named deviation -- see Observations O1.
- r36.5 (writes-scope pressure): NOT FIRED.
- r36.6 (FLAG guard): NOT FIRED.
- r36.7 (V-UNDECIDABLE): NOT FIRED.
- r36.8 (close gate failure): NOT FIRED (W5 under the operator
  amendment).
- r36.9 (sequence collision): NOT FIRED.
- r36.10 (proof-work pressure): NOT FIRED -- no wall required
  re-deriving (11)/(14)/Lemma 4 beyond the quotations plus the
  RC-4 smooth-count line; the fixed-constant clauses the carriage
  suspends are the DEBT ledger, which is the kickoff's own RC-4
  design, not a re-derivation.

## 3. Observations

O1. S1b IS UNSATISFIABLE AS AUTHORED; r36.4 FIRED AND THE RUN
PROCEEDED UNDER A NAMED DEVIATION SUBMITTED FOR OPERATOR
RATIFICATION. The authored check |V(z) e^gamma ln z - 1| <= 0.02
at z = ln x/2 cannot be met at scales 1e8/1e20/1e100 by ANY
implementation: the anchored A3 CM-5b V(z) column (reproduced
exactly by S1a) times e^gamma ln z equals 0.9039 / 0.9139 /
0.9702 / 0.9957 -- the Mertens (q9) error term at z = 9.21..115.13
is 3..10 percent, a mathematical fact computable from anchored
bytes alone. This is the rule-17 "unsatisfiable as authored"
class (the item-0018 M1 precedent, ANN-53, resolved in-run as a
deviation). Grounds for proceeding: (i) the defect is provable
from anchored bytes, independent of this session's work; (ii)
V-36 makes every grid value reference-only, so no emitted class
rests on the check; (iii) the check's sanity function (catch
gross errors: wrong log base, wrong gamma, off-by-e) is
discharged by the attainable surrogate tolerance 0.10, which
PASSES and is labeled as the executor's surrogate, not the
authored check; (iv) the operator acceptance of this single
commit is the ratifying act -- accepting it ratifies the proceed
decision, rejecting it restores the strict-stop path at the cost
of one re-dispatch with a corrected tolerance. S1a, S1c, S1d all
PASS as authored.

O2. IN-RUN ADVERSARIAL AUDIT, DISCLOSED (item-0035 precedent).
Before hand-off, a local, corpus-only, web-OFF refuter fan-out ran
against the draft artifacts: six independent single-lens refuters
(margin/envelope algebra; critical coefficients and exhibits; the
W-B wall; chain-vs-extracts; verdict logic; contract compliance),
25 findings returned. Sustained and REPAIRED in place:
- The 3.1 conversion factor a_0 is e^{O(k)} under the (q5) asymp
  licence, not k-free, and the margin-bridge slack is O(k), not
  O(ln k) (three refuters converged). Verdict-preserving -- O(k)
  = o(k lnlnln z) in (N1) and O(u/v) = o(u) at every wall scale
  -- but the printed support sentence was wrong; repaired in
  workpaper 3.1, the sheet comment, and Section 11.
- The tables RC-4 line claimed the W-B wall "PROVED both
  directions ... fails strictly above it", strengthening the
  workpaper's certified-closure scoping (the failure direction is
  not provable from the licensed inputs) -- exactly the
  rule-16(a)/W7 defect class; repaired to the certified-closure
  wording in the tables and the application copies.
- The per-lambda closure constant: closure is certified for any
  fixed c < c_1, not at the boundary constant c_1 itself (the
  -2 lnln z window correction); repaired in 3.2.
- The (N1) inequality ln C_{k+1} >= 0 needs the row-carried
  constant semantics, which the workpaper now states once
  (Section 3 carriage paragraph; 3.1); the rows alone are upper
  bounds and license no lower bound on the true constant.
- The licensed pi lower bound needed a floor for non-integer
  arguments (ln floor(N) / ln(1+log2 N)); repaired.
- The d4 growth display holds at the u-scale schedules only (K_1
  is constant at fixed k); the quantifier is repaired.
- The FLAG-record card description omitted the frozen card's
  domain restrictions (even offsets, 0 in H, admissibility);
  repaired, comparison outcome unchanged.
- The tables lacked the RC-0 label the workpaper cross-references;
  repaired (header line emitted).
SUSTAINED AS A READING QUESTION, NOT REPAIRED AWAY: two refuters
pressed that (P1)'s closure at any diverging schedule engages the
Lemma-4 carriage debts d1-d4, and that under a STRICT all-PROVED
reading of the V-36 closing clause (P1) would fail on every
diverging schedule and the emission would be V-BOUNDED naming
W-B. The run emits under the rule's own either-PROVED-or-DEBT
closing clause -- the reading under which the kickoff's mandated
DEBT-ledger design, its Section 8 expected picture and BET-15's
registered p = 0.75 are all coherent, and which the artifacts now
state explicitly (workpaper Section 3 carriage paragraph, Section
11; the EMISSION text itself). The strict alternative is recorded
here and in workpaper Section 11 as the operator's to adopt; under
it the verdict becomes V-BOUNDED (row: both; wall: W-B) with (P2)
unchanged. Rejected refuter claims (with grounds) and the full
finding list are reproducible from the session transcript; no
finding touched (P2), the walls' classes, or the V-A pass.

O3. BUDGETS. The sheet is 597 .py lines against the kickoff
estimate 380-560 -- a reported overrun (estimate, not a gate),
driven by the audit repairs and the RC-4 grid machinery. The
workpaper is 566 lines under the operator-amended envelope (W5).
The tables file is 381 lines. One large/high session; network
none, PDF none, Lean none.

O4. The (q14) V-A note: the kickoff renders the candidate schedule
list with braced ln-groups where A8 prints them fused; the row's
own "present as printed there" clause directs the confirmation at
the anchor's printed form, which is confirmed. Recorded in the
workpaper V-A table, not a stop.

O5. The session spanned local midnight (started 2026-08-05, landed
2026-08-06); the ANN sequence-103 file carries the landing date in
its id per the kickoff's run-date clause, and P3's
last-annotation check was made against ANN-20260805-102 at
session start.

## 4. Follow-up candidates (non-binding)

- F3 DEFERRAL, ROUTED TO THE OPERATOR'S DESK (kickoff Section 9;
  (q15)): the ANN-102 F3 candidate -- the explicit stretch-length
  lower bound of L5(e) for a model-side growth row -- is outside
  the ratified acceptance_intent and would have opened an
  item-0035 artifact this run does not consume. Deferred by name.
- The RC-1b gate decision (A8 Section 5): this sheet's verdict is
  the input the operator wanted before deciding RC-1b and the
  route-C note; the priced picture (sufficiency wall W-B at
  (lnln x/lnlnln x)^{1/lambda}, necessity wall W-A at theta*_H
  lnln x/lnlnln x, grey zone between, d1-d5 the debts RC-1b would
  discharge) is the decision surface.
- Kickoff-template lesson (rule-17 family): a byte-fixed numeric
  self-check tolerance should be verified satisfiable against the
  anchored values it cites at authoring time (S1b, O1); and a
  byte-fixed verdict rule that both mandates a DEBT ledger and
  bars classes "resting on" debts should fix the reading of
  "resting" (O2).
- If the operator prefers the strict r36.4 path: re-dispatch with
  a corrected S1b tolerance (0.10 grid-attainable, or the check
  restricted to 1e1000) -- all other run content is unaffected.

## 5. Artifact hashes (final bytes)

- rank-ceiling-sheet.md
  7a55c6ade846f1c67e62dec6953ed070d808f742876dd182c60e089a072f380e
- rank_ceiling_sheet_36.py
  606ad6ecc23f8cc92250bf5f992485a75197831c38f81a6cf0ec3969938a9bd8
- rank_ceiling_sheet_36_tables.txt
  2361c283900d9dac0049cabb02b1df19145961589cb6ce6ef5fbe9855af92e03
- item-0036-report.md: this file's own sha256 is stated in the
  hand-off message (operator-side hashing canonical) and booked as
  HASHES line 126.

Rule-28(a) form restated: artifacts and booking land as one
commit; the commit author string names the executor model (Claude
Fable 5); the run pushes nothing. BET-20260804-15 stays OPEN for
operator judgment against this sheet; no bet is scored by this
apply.

END OF item-0036 RUN REPORT
