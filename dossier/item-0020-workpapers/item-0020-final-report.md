# item-0020 final report -- averaged relative one-position extension
# sieve with o(log x) constant (the B2.reduced proof campaign)

Run: single-session execution of the kickoff v1 package order W0-W5
(the session cut is the executor's per kickoff Section 6; item-0018
precedent). EXECUTOR lane, local machine, Claude Code; model string
claude-fable-5 (Fable 5), reasoning high. Web OFF throughout
(corpus-only; kickoff Section 2 evidence firewall honored: the two
2026-07-18 operator reports are cited nowhere; no external
literature entered). Local code execution only (runs rule 6). Zero
edits under lean/; no lake invocation; no git commits by the run.

Kickoff disk sha256 (operator-side booking canonical):

    a2c21d490e1f7b3a7b92e6752508f4827eb890e38ff05332b763f63fe3229f63
      item-0020-kickoff-v1.md

## Session A (single session; sections by work package)

### Gates verbatim (session start)

    git rev-parse HEAD
      17deadb3bb5c4207e63d93744ea0e1b043a710ed  == Section 0 pin
      EXACTLY; no rule-18 delta; PARALLEL-0022 clause not exercised
    Section 2 anchors: all nine sha256 byte-identical      PASS
    python3 lean/scripts/blocks.py check-frozen
      -> "FROZEN BLOCKS: all byte-identical."              PASS
    python3 lean/scripts/blocks.py relocation-check
      -> "RELOCATION CHECK PASSED -- concatenation is
          byte-identical to the old body."                 PASS
    sorry census: exactly lean/Erdos251/Statement.lean:1,
      every other file 0                                   PASS
    mathlib pin a6276f4c6097675b1cf5ebd49b1146b735f38c02
      intact in lean/lake-manifest.json                    PASS
    lean-toolchain ends "v4.16.0\n" (trailing newline)     PASS
    roadmap/item-0020.md: status: ratified                 PASS

### W0 -- setup and continuity

dossier/item-0020-workpapers/ created; working-notes.md records the
four binding surfaces by direct quotation (the 7.1
RelExtensionUpper text; the FIXED-DELTA gate sentence; the
D3(i)-(vi) list; the 7.4 slack ledger) and the W2/V2/cap
vocabulary dictionary against e2prime D0.3. Anchor reading for this
run additionally consumed (read-only, in-corpus): e2prime-supply
P1/P2/P3/P3.3'/M2.3/D1.a/D1.b/F17.5/D5.c and runs/README rules
9/12/15/16/17/18.

### W1 -- mechanism inventory (mechanism-inventory.md)

One statement-grain page per mechanism M1-M7, written before any
proof step; F18.3 singleton-inertness enforced on every B-input;
the M1 trap line carried verbatim. Two mechanism mutations,
recorded not silent: M6's class-level variant merges into M3, its
extension-position variant into M2(ii); M7 is subsumed as the M1
lane's room calculus. One NEW candidate statement produced at
statement grain: B2.pairs (the class-normalized relative pair
statement; final form in relext-upper.md Section 2), plus one NEW
A-side statement A3.card (the cardinality form of
MatchedFlankLower).

### W2 -- budget sheets and no-go audit (budget_sheet_20.py,
### budget_sheet_20_tables.txt; deterministic, sha256-stable
### across reruns)

Mandatory rows delivered: (a) per-route constants vs ln x / x^eps /
the reserve (T1, T5, T6); (b) the rank-2k trap row, tabulated
(T1: exponents 18.9 -> 23.2 on the grid; ratio-to-room rows
15.3 -> 21.3); (c) the rule-12 landing row (T3: all additive terms
in this run's chains land additively; no dyadic-coefficient
coupling anywhere); (d) D3(i)-(vi) one-liners in verbatim question
order (T7). New quantitative rows: the capacity/crossover ledger
(T2, both conventions labeled: scale markers x ~ 1e25 (A3.card) /
1e28 (M1.a-falsity); PROOF-condition crossings at the ceil-honest
D0 depths x ~ 1e100-1e110 with C_0 in {1,2} -- finite-scale
honesty per D3(vi)); the M1.b insufficiency
counterexample settled in exact integers (T4); the B2.pairs
consumption arithmetic (T5: pair-eps = 1/64 closes the pigeonhole
at delta = 1/2; anti-vacuity floor C_F >= share/(A'L)).

PRIORITY ORDER (the W2 deliverable), with justifications:

1. M3 engine (GO). Every constant in its chains is capacity-grade
   (sheet-empty of forbidden classes); its four targets (A3.card,
   the V2 floor, the M1.a falsity, the barrier) were each one
   Cauchy-Schwarz or one counting step from anchored proved facts,
   so the cost/benefit is the best on the board -- and two of the
   four (A3.card, barrier) materially reshape the program (ledger
   delta = 1/2; all-T-routes dead a priori).
2. M1.c reduction (GO). The reduction B2.pairs => RelExtensionUpper
   is constant-free (T5 row (a): NONE) and converts the D5-frozen
   adversarial-selection target into a selection-free second-moment
   statement -- the exact "structurally different exclusion device"
   shape 7.5 mandates (no per-word constant can even appear).
   Priced risk: the sqrt(eps) loss, shown inherent (proofs.md
   C3(c)), is harmless against the 7.4 ledger (1/64 consumption
   point).
3. M1.c closure attempts (GO as obstruction-registering). The two
   available closure lanes (union sieve; identity layer) were run
   to their quantified deaths (F20.3, F20.7) so the successor item
   inherits named walls, not vibes.
4. M5 (CONDITIONAL, deferred). Statement shape + named inputs
   NI-M5a/b recorded; no in-corpus proof surface exists, so proof
   investment would violate rule 15's cost discipline.
   M2/M4/M6: NO-GO registered with exact gaps (F20.4-F20.6); no
   investment beyond their sheet rows.

### W3 -- proof investment (proofs.md; evaluator-first honored:
### every constant went through the sheet, T2-T5 rows added
### in-run)

Executed down the priority order. Four claims proved (support
classes in relext-upper.md Section 1): C1 A3.card; C2 M1.a falsity
+ V2 floor; C3 the B2.pairs reduction (unrestricted selections;
FL-1 declaration made); C4 the identity-layer barrier (even
Cramer-smooth model + finite-scale gluing). No route needed the
coupled gate (FL-2 never triggered); no heuristic carries any
proved sentence; model-M content appears nowhere in the proofs
(the C4 model is a proof OBJECT -- an explicit deterministic
sequence -- not a probabilistic model heuristic). B2.pairs itself:
OPEN, registered U20.1 with both-readings empirical contact.

### In-run adversarial audit (workflow fan-out; the project's
### refuter discipline)

Two passes; full disposition in audit-record.md. PASS 1 (against
the pre-repair drafts): 14 finders -- three refuters per claim
C1-C4 (arithmetic, corpus-fidelity, counterexample lenses), an
independent budget-sheet re-execution from fresh code, and a
completeness critic -- then two adversarial confirmers per raised
FATAL/MAJOR. Raised: 0 FATAL, 5 MAJOR, ~40 MINOR/NOTE. Sustained
(2/2): 4 MAJOR. Headline: a 3-refuter independent convergence
(the project's strongest signal class, third recurrence after
item-0017 B3 / item-0018 O3) on the C4 barrier STATEMENT
overclaiming universal rigidity -- the model's gap-step boundaries
carry ~ln x/2 non-rigid size-2 classes (refuter-verified
computationally at 1e6-1e8); the statement was weakened to the
hedged form its own verification proves (transitional mass
O(L ln x) = o(|S'|); argmax selection), conclusions unchanged and
refuter-measured at 0.998-0.99996 |S'|. The other sustained
repairs: the full six-line D3 matrix per mechanism (T7), the
single-eps_C-convention 1/64 gate arithmetic, and the
failure-in-model characterization of the barrier's consequence
clause. The sheet re-execution reproduced every numeric table
value to 3 significant figures and exposed the crossover-
convention mislabels (repaired: both conventions now printed with
a real sign-change scan). The five-refuter convergent m1 finding
(the vacuous n = 1 odd-word exception) and the remaining minors
were all repaired in place; one raised MAJOR was overruled on a
split confirmation vote with its substance folded via the minor
cluster (audit-record Section 3). PASS 2 (against the repaired
package): the rule-16(a) clause diff over relext-upper.md Section
1, a dedicated re-refutation of the repaired C4, and a cross-file
consistency sweep; disposition in audit-record.md Section 7.

### W4 -- verdict object

dossier/relext-upper.md v1 written to the Section 5 structure;
Section 1 is the one-page support-classed verdict; the rule-16(a)
clause diff over it is recorded in audit-record.md. Verdict: (S-)
in full, with REDUCED(B2.pairs) and four proved partials; the gate
sentence answered NOT CLEARED; at dossier grade the supply triple
now hangs on RelExtensionUpper alone.

### Observations (O-n)

O1 (the missed trivial half). The A-side of the supply design
   (MatchedFlankLower) was carried as OPEN through two items while
   being a two-step consequence of anchored facts (P3.3'(iv)
   capacity + P3.3'(ii)/TailIntersection retention + RS.1). The
   miss survived item-0018's nine-agent audit and R2 because every
   eye was on the B-side wall calculus; the cardinality regime
   also only opens at x ~ 1e25+ (marker; 1e100+ at the proof
   condition), far beyond every measurement, so
   no empirical signal ever pointed at it. Process lesson: when a
   layer's statements are ranked by consumer fit, run one explicit
   "is any of these trivially true/false at the pinned parameter
   map" pass per layer -- the same pass that caught M1.a's falsity
   here (O2) caught A3's triviality.
O2 (the anchored lane's display was unsatisfiable). The kickoff's
   M1 sufficient condition W2 = o(|S'|) is provably false at the
   D0 depths (F20.1): the (N-1)_+ <= N(N-1) majorization is
   x^{1-o(1)} lossy at astronomical class multiplicities. The
   lane's own relative hope survives exactly as the kickoff
   phrased it, but the load-bearing normalization (per-class
   1/N_P) is forced (T4 counterexample) -- statement-grain work
   the inventory did BEFORE proof investment, as rule 15 intends.
O3 (where the whole program's hardness now sits). After this run
   the unconditional corridor is exactly: prove B2.pairs. The
   barrier (F20.7) proves every route must consume an input that
   fails in the barrier model (salient family: middle-slot
   distributional inputs); the sheet proves the two generic
   carriers (per-word sieves, pair sieves) are
   superpolylog-dead; the named viable input shapes are NI-M2
   (class equidistribution) and NI-M4 (word-grain upper mean
   value) -- both genuinely new mathematics relative to the
   corpus. This is the exact quantitative successor surface.
O4 (finite-scale honesty). Every new asymptotic result of this run
   is vacuous below the T2/T3 crossovers (x ~ 1e25-1e28 marker
   convention; x ~ 1e100-1e110 at the proof condition); the measured
   1e6-1e10 world (m1: 99.75%+ singletons) is the OPPOSITE regime
   (word space exceeds site count). Both readings are printed
   wherever a measured number appears; no finite-scale closure is
   claimed anywhere (E3 duty).
O5 (statement-layer standing after this run). A3's "OPEN" status
   line and D5's A-layer ordering are superseded in content (not
   in shape) by Theorem 1; the B-layer selection (B2.reduced
   primary, B3 fallback) is unchanged; the C-layer is unchanged.
   FU5 stages the erratum as operator bookkeeping; U18.5 was not
   engaged (no shape change).

### Follow-up candidates

See relext-upper.md Section 7 (FU1-FU5), all with rule-15 remarks;
none executed.

### W5 -- close gates (kickoff Section 7, run verbatim at close)

    python3 lean/scripts/blocks.py check-frozen
      -> "FROZEN BLOCKS: all byte-identical."          PASS
    python3 lean/scripts/blocks.py relocation-check
      -> "RELOCATION CHECK PASSED -- concatenation is
          byte-identical to the old body."             PASS
    sorry census: exactly lean/Erdos251/Statement.lean:1,
      every other file 0                               PASS
    mathlib pin a6276f4c6097675b1cf5ebd49b1146b735f38c02
      intact in lean/lake-manifest.json                PASS
    lean-toolchain trailing newline intact
      (file ends "...6.0\n")                           PASS
    git rev-parse HEAD == the Section 0 pin
      (17deadb3...; no commits made by the run; the
      rule-18 / parallel-0022 clauses were never
      exercised -- HEAD == pin throughout)             PASS
    git status --porcelain == exactly the Section 5
      writes-scope:
        ?? dossier/item-0020-workpapers/
        ?? dossier/relext-upper.md
        ?? item-0020-kickoff-v1.md
      (the kickoff line is the operator's own ephemeral
      input file, pre-existing, never committed, not a
      run write, per kickoff Section 5)                PASS
    Section 2 anchors: all nine sha256 re-verified
      byte-identical at close                          PASS
    rule-16(a) clause diff over relext-upper.md
      Section 1: EXECUTED (independent agent, PASS 2 of
      the in-run audit; 1 MAJOR + 5 MINOR + 4 NOTE
      findings, all folded -- audit-record.md
      Sections 6-7)                                    DONE

Committed data volume: workpapers ~112 KB across 7 files (max
file 22 KB) + relext-upper.md ~18 KB -- inside the ~200 KB
per-file and ~2 MB total caps; no raw dumps.

Deliverable hashes (runner-computed; operator-side sha256
canonical; this report's own hash is operator-computed at
booking):

    9a53a868e32a970502f5050634ceb819404c50ee6b3e703f7d730504f3a8187d
      dossier/relext-upper.md
    c0be34329fc1fc21317264091a22f52ba178a3d6b8d58593643f2faf344298e1
      item-0020-workpapers/working-notes.md
    fe2ad5a3f95f2fb8589b71432d0c2ca2a53cd0e0a6dcdafd3044b45be82afacf
      item-0020-workpapers/mechanism-inventory.md
    bbce2f583f0a1f158b7fc5f13ca120b5388be642c585bbbdac5e6be5c5558b0d
      item-0020-workpapers/budget_sheet_20.py
    6ec75efbc0c1778df57276dc9ac060cd77c47fdc57496e99e0399f0c038b0137
      item-0020-workpapers/budget_sheet_20_tables.txt
      (deterministic: byte-identical across re-runs, incl. a
      post-repair regeneration check)
    58e16a603705ac85d519a510c4049d47e9e7a9ba4290f7b7905abef7da865e64
      item-0020-workpapers/proofs.md
    776920d763e6e3c5d202288a3d93068c1749a7f8c57604b0bdf73a26ac8f6866
      item-0020-workpapers/audit-record.md

Committed data volume: workpapers + verdict object, ASCII, all
files well under the ~200 KB per-file cap; no raw dumps.

Review gate (staged per kickoff Section 8, operator decision):
(S-) outcome pattern: R1-light steering re-execution of
budget_sheet_20.py (deterministic; sha256-stable) and of the T4
exact-integer counterexample; rule-16(a) pass over relext-upper.md
Section 1 (in-run pass already executed and folded, audit-record);
blind R2 optional at operator discretion. BET-08 keeps running to
resolve_by. Bookkeeping (ledger ANN, HASHES, roadmap done-move,
HANDOVER) is steering/operator post-run; nothing of it is this
run's writes-scope.
