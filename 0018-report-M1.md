# item-0018 M1 completion report -- relative extension statement layer

Date: 2026-07-19. Runner: steering lineage, fresh instance; model
string claude-fable-5 (Claude Fable 5), ultracode + workflows,
reasoning high (execution_profile per roadmap/item-0018.md). Kickoff:
item-0018-kickoff-v1.md, disk sha256
44c07d99a1f00730d58a643469042b2f155a798990b61a987388c684b960f818
(operator-side sha256 canonical; see the pin/hash record below).
Web OFF honored: no network/literature tool was invoked at any point
(corpus-only); local code execution used throughout (python3, sympy,
mpmath) per runs/README rule 6; the in-run adversarial audit used
nine local subagents (workflow fan-out), each itself corpus-only.
Out-of-corpus firewall honored: the two 2026-07-18 operator reports
are cited nowhere; the k = 2 inflation constant enters only through
the in-repo F17.5 Euler product, independently recomputed (budget
T3).

## 1. Gates (Section 7 of the kickoff; outputs verbatim)

- git rev-parse HEAD
    32b91ea92d73cfb667a5e85c4f6f4db27ba0474a
- python3 lean/scripts/blocks.py check-frozen
    OK erdos_251_irrational / HLQuantA / CramerGranville;
    "FROZEN BLOCKS: all byte-identical."
- python3 lean/scripts/blocks.py relocation-check
    "RELOCATION CHECK PASSED -- concatenation is byte-identical to
    the old body."
- grep -rcE '^\s*sorry\s*$' lean/Erdos251 --include='*.lean'
    lean/Erdos251/Statement.lean:1; every other file 0.
- roadmap/item-0018.md: status: ratified.

PIN / HASH RECORD (deviation, not silently absorbed). The kickoff's
Section 7 first predicate reads HEAD == 8cb5086... while its own
Section 0 pins main = 32b91ea... (the actual HEAD). Resolution
executed: the kickoff on disk is a post-bookkeeping revision of the
version ANN-51 records (steering sha256 57655d5a..., authored at pin
8cb5086); git diff 8cb5086..32b91ea touches ONLY bookkeeping (report
shards, HANDOVER, ledger, HASHES, roadmap, runs/README) -- every
Section 2 read-only anchor is byte-identical across both states, and
runs/README rule 15, which this kickoff binds to, exists only at
32b91ea. Per the item-0017 precedent ("kickoff read-only anchors
unchanged ... session A pins to" the new HEAD) the session pinned to
32b91ea; the stale Section 7 line and the superseded ANN-51 steering
hash are recorded here for the operator to reconcile (the operator-
side sha256 of the REVISED kickoff, 44c07d99..., should enter the
bookkeeping at close; steering cannot self-certify it).

## 2. Writes-scope diff (worktree at close; exhaustive)

git status --porcelain:
    ?? dossier/item-0018-workpapers/     (budget_sheet.py +
                                          budget_sheet_tables.txt)
    ?? dossier/relext-statements.md      (v1, the M1 deliverable)
    ?? item-0018-kickoff-v1.md           (operator's own ephemeral
                                          file; pre-existing, not a
                                          run write, never committed)
    plus this report, 0018-report-M1.md.
Exactly the Section 6 writes and NOTHING else: zero edits under
lean/, ledger.yaml, roadmap/, payloads/, runs/, HANDOVER.md.
Deliverable hashes (steering-computed; operator sha256 canonical):
    relext-statements.md
      be3b9e625d7c9b39417e626504d471407ade0596682e80803e20c9abd28e09c8
    budget_sheet.py
      129b39fbd2926e7e8ab56a26ac85d84bfc148dde97779ad04ef2809ba946530d
    budget_sheet_tables.txt
      e4e070d721f564dd728ffb4a633a00ef476bca08e739dd37ad9aa8fbc4cfd302

## 3. Run structure (kickoff Section 9 split, honored in one run)

Session A equivalent: D0 regime lock + T6 dictionary smoke test
(executed BEFORE D1; the (7,6,44,3) certificate re-derived from the
printed primes, primality/consecutiveness re-checked, ANN-50
dictionary fixed, both (E5) gates verified) + D1 candidate drafting.
Session B equivalent: per-candidate rule-15 budget sheets (committed
script + tables) BEFORE the no-go audit; then a NINE-AGENT
adversarial audit pass against the drafted document (five
per-candidate refuters, an independent budget re-execution in the
3.5-pass discipline, a quantifier/arithmetic pass, a corpus-fidelity
pass, a completeness critic), adjudicated with every FATAL/MAJOR
steering-re-executed before disposition (checklist rule iv).
Session C equivalent: D4 consumer design + D5 selection verdict +
repairs folded in + this report. Binding order D0 -> D1 -> (D2 then
D3 per candidate) -> D4 -> D5 was honored; the in-run audit is the
M1-internal quality pass, NOT the operator-side M1 review gate
(Section 6 below).

## 4. Observations

O1 (mandate outcome). The M1 statement layer is DELIVERED: eight
   primary candidates with sub-variants (A1/A2/A3; B1/B2/B3 with
   B2.reduced; C1/C2), each with full quantifier prefix, uniformity
   range, constant dependence, normalization, rule-15 budget sheet,
   and a written six-question no-go audit; a reuse audit over all
   eleven named Counting decls; the D4 derivation Selected-A +
   Selected-B + Selected-C => ExchangeSupply1 with the pigeonhole
   displayed (trap T3), the t-threading spelled, the b = 1 gate
   production from Par', and the T5 slack ledger; the D5 selection
   verdict fixing item-0019 measurements (m1-m5), the item-0020
   proof target (B2.reduced at C_F = o(ln x) -- matching the
   BET-08 registration's deferential shape clause), the item-0021
   transfer target (C1 aggregate, c* necessity budget + named
   closure inputs), and the M2 prerequisites (three Props named
   MatchedFlankLower / RelExtensionUpper / TailIntersection, with
   Lean statement patterns and a hazards register; no Lean
   written). Both target shapes (exclusion form; anti-rigidity
   counting form) were kept alive to D5 and mapped onto each other
   (Section 7.5 of the deliverable).
O2 (headline mathematical findings, F18.1-F18.5). (1) The
   kickoff's reuse-audit question has a SPLIT answer:
   consCount_lower_bound consumes the A-layer VERBATIM at small
   span; at exchange-typical span the transfer is blocked by two
   quantified walls (the decl's own NECESSARY span hypothesis; a
   Theta(L)-oversized extension term against the ln x/8 reserve,
   sieve-constant-independent). (2) A new quantitative window:
   within the frozen HLQuantA card budget the truncated-tail
   C-layer transfer REQUIRES family density (ln x)^{-c} with
   c < c* = 4 ln 2 - 2 = 0.7726 (necessity; closure needs two
   further named inputs), and the A-side thinning tau(A') >= 2.885
   exceeds c*: C-layer viability is a family property. (3) The
   family-averaged B-form must be stated in the reduced
   (N_{P,d_P} - 1)_+ form: the plain form smuggles abundance.
   (4) F17.9's locus is sharpened: the o(ln x) statement gate is
   passable by selection-gated forms; the superpolylog wall is a
   property of per-word-sieve proof routes. (5) The pointwise
   B-form is FALSE without a multiplicity floor and (post-audit) a
   quotient cap; its truth window is expected-unmeasurable at
   reachable scales, pending m1. NO B-layer candidate fails D3(i)
   at statement level: the kickoff's obstruction-record contingency
   branch was NOT triggered; the averaged forms were checked first
   as instructed and are where the layer concentrates.
O3 (in-run audit disposition; the strongest process datum of the
   run). The nine-agent pass returned 3 FATAL / 17 MAJOR / 44
   MINOR / 27 NOTE findings; after steering re-execution the
   sustained core was: [FATAL, 5-agent convergence] the draft's
   worst-case bound on the two-block quotient rho was FALSE (the
   machine-checked insert telescope bounds S(H_d)/S(H_pre) only;
   dividing by S(H_suf) lets CRT-aligned classes reach rho =
   (ln x)^{1-o(1)}, exceeding ln x at finite scales -- witnesses
   rho = 82.24/221.66/1060.3 at the grid depths, all
   steering-re-executed); [FATAL] the draft had promoted the c*
   NECESSITY budget to sufficiency ("closes exactly"); [MAJOR
   convergences] an A3 model-support provenance promotion, the
   TailIntersection constant failing under the draft parameter
   lock, a class-COUNT-vs-class-SIZE corpus misread, a false
   middle-flexibility abundance claim (exactly ONE admissible
   in-budget middle at k = 24 for the exhibited construction), and
   a false quantifier-necessity claim. ALL repaired in place with
   marked amendments (deliverable Section 9a); the D5 selection,
   the 7.2 pigeonhole, the 7.3 instantiation table, and the M2
   design survived every finding. Process echo of item-0017 B3:
   independent same-object convergence (5x on the rho defect, 4x
   on the A3 provenance, 3x on TailIntersection and the
   count-vs-size misread) is again the strongest signal; and the
   rho defect is EXACTLY the rule-15 target class (a fixed-k
   per-insert constant silently promoted to a growing-k two-block
   setting) -- caught this time at statement stage, pre-proof, by
   the adversarial layer the rule prescribes.
O4 (finite-scale honesty rows). The in-repo Lemma 4.1 constant
   C = 12 makes the HLQuantA-conditional class floor vacuous below
   x ~ 1e371 (C = 1: ~1e45), and the small-span Bonferroni closure
   at C2 = 1 opens only near 1e1000: the conditional A-layer is an
   asymptotic statement layer, not a computational one, at every
   reachable scale. Recorded per D3(vi) so no item-0019 measurement
   is mistaken for these constants.
O5 (kickoff textual defects found, for the operator's kickoff-v2
   hygiene): the stale Section 7 HEAD predicate (Section 1 above);
   the Section 2 attribution of the anti-rigidity counting form to
   "item-0005 adjudication F2" (the content is item-0005 P4 +
   item-0017 FATAL-2; the item-0005 Section-6 F2 is the Lean-module
   follow-up) -- handled as a provenance note in the deliverable's
   Section 0, no content ambiguity.

## 5. Follow-up candidates (described only; never silently executed)

FU1 U18.6 write-out: the Model-M A3 analogue at delta = 1 - o(1)
    (per-site lower-tail Chernoff + M1(e) dilution); one short
    model session, would upgrade A3's support tag.
FU2 U18.7 engineering: side pairs with >= 2 admissible in-budget
    middles at every rank (blocks leaving >= 2 uncovered shift
    classes mod every small prime); gates A1's two-word route.
FU3 U18.3 model check: the B1 multiplicity-floor necessity/
    sufficiency in Model M (cheap Session-B-style check).
FU4 T4 extremal refinement: the exact sup of rho over in-window
    admissible (P,d) at the grid depths (small search space at
    1e8; would replace the witness lower bounds by the true sup).
FU5 Kickoff v2 (M2): prerequisites fully staged in the
    deliverable's Sections 7.1/7.6/8; M2 waits on the M1 review
    gate and operator kickoff, per the kickoff's own Section 0.

## 6. M1 review-gate preparation (B2 architecture; execution is an
## operator decision, not this run)

Rule 16(a) status: the verdict tables (deliverable Section 9) were
diffed against the body's support classes in-run, AFTER the audit
repairs (deliverable Section 9a). Strip-relevant anchors for the
review object build (the object is dossier/relext-statements.md;
the strip should retain statement text and verdicts, withhold the
9a adjudication narrative if a blind R2 is wanted):
- R1 (light budget-sheet re-execution): budget_sheet.py +
  budget_sheet_tables.txt; the T4 witness configurations (exact
  block data are printed in the script); the T6 smoke-test data
  (certificate primes are in dossier Section 7.2, in-corpus);
  re-execution targets: T0-T7 rows, the c* algebra, the vacuity
  crossings 1e371/1e45, the witness rho values.
- R2 (load-bearing cross-family scope audit): Section 4 quantifier
  prefixes and uniformity claims; Section 9 verdicts vs body
  support classes; the F18.n scope sentences (esp. F18.2's
  necessity-vs-sufficiency line and F18.4's domain scoping);
  Section 7.1 Prop shapes vs their claimed provenance (A3/
  B2.reduced/C2-at-pin); the deliverable's own audit-repair marks
  as declared-amendment sites.
- Dependencies the reviewer needs read-only: lean/Erdos251/
  Exchange.lean, Hypotheses.lean, Counting/{Words, Lemmata,
  ConsecTransfer, OneExtension}.lean (decl statements);
  dossier/e2prime-supply.md Sections 1, 2, 3.2-3.3, 4.3-4.5, 6,
  7.1-7.2, 8, 9; both adjudication payloads; runs/README rules
  15-16.
