# item-0035 completion report

Lane: EXECUTOR (local workstation, Claude Code; model string
claude-fable-5). Date: 2026-08-05. Dispatch:
`item-0035-kickoff-v1.md` v1 (ephemeral, never committed; the
operator-side sha256 of the dispatched file is canonical; the
operator apply of this run's outputs is the ratifying commit).
Section 0 pin `f164ea3a7d8905993d14afecbc74fa96e54b56d4` == HEAD at
session start, empty delta (Gates V1). Environment: web OFF, cloud
OFF, corpus-only; no PDF opened; no source opened (A7 unopened);
zero edits under `lean/`; no `lake`; no roadmap, ledger, HASHES,
writeup or HANDOVER edit; tree writes confined to
`dossier/item-0035-workpapers/` (session scratch under the
sandboxed `/tmp` scratchpad). Enabled tools: local shell (git,
sha256sum, grep, wc), python3 stdlib, file read/write; local
subagent fan-out for the in-run adversarial audit (corpus-only, web
OFF; disclosed in Observations). Execution profile honoured:
`{ class: large, reasoning: high }`.

## Verdict (kickoff Section 4.5, V-35 rule)

**V-CERT (separator instance certified).** Clause by clause:

- (a) HOLDS. (M-BOUND) is PROVED at dossier grade in
  `separator-instance-certificate.md` Section 5, by
  elementary/finite argument from the Section 3/4 definitions and
  the (q1) recursion alone, for every $`(J,K)`$ with $`J,K\ge1`$;
  the initial segment ($`g_1=1`$, pre-recursion gaps) and every
  stretch-length case consumed are treated in certificate Section 4
  (L1, L1', L5: small stretches by enumeration, every $`m\ge2`$ by
  the crossing argument).
- (b) HOLDS. The statement-level pairing is certificate Section 2
  ((q3) quoted verbatim with qualifiers intact; quantifier mapping
  displayed) and Section 6 ((M-FALS) derived from (M-BOUND) by
  displayed logic, reading scope explicit).
- (c) HOLDS. The non-transfer paragraph is certificate Section 8,
  with exactly the three clauses: fixed rank only; no claim at the
  growing D0 depth; no verdict on S1, (CG) or B2.pairs.
- (d) HOLDS. Both-readings entry: certificate Section 12, with the
  mandated contradicting seed (one deterministic system -- an
  instance, not a theory of smooth models).
- (e) HOLDS. The rule-16(a) clause-vs-body diff is certificate
  Section 11; no verdict clause strengthens a body support class,
  no body qualifier dropped.

V-COUNTER not engaged: no model class with three or more distinct
realized middles exists (proved, Section 5) and none was found by
the census (kill criterion (q7) never triggered). No V-INCOMPLETE
element remains.

## Gates (outcomes verbatim)

- V1: `git rev-parse HEAD` ->
  `f164ea3a7d8905993d14afecbc74fa96e54b56d4` == the Section 0 pin;
  `git diff --name-only <pin>..HEAD` -> empty (no rule-18 delta at
  all); `git status --porcelain` at start ->
  `?? item-0035-kickoff-v1.md` only. HOLD.
- V2: `sha256sum` over A1-A7 -> all seven byte-identical to the
  dispatch Section 2 table (A1 `3b285592...2cf8`, A2
  `644c512b...e63d`, A3 `55c915f0...f79b`, A4 `58e16a60...5e64`,
  A5 `4e168441...3582`, A6 `9d195378...9d06`, A7
  `9d0d8bc0...dffa`). HOLD.
- V3: `grep -n "^status:" roadmap/item-0035.md` ->
  `3:status: ratified`. HOLD.
- V4: `python3 lean/scripts/blocks.py check-frozen` -> "FROZEN
  BLOCKS: all byte-identical." (erdos_251_irrational, HLQuantA,
  CramerGranville all OK). HOLD.
- V5: `blocks.py relocation-check` -> "RELOCATION CHECK PASSED --
  concatenation is byte-identical to the old body.";
  `ledger_check.py relocation-check` -> same PASS;
  `ledger_check.py validate` -> "VALIDATE: passed." (100 entries,
  17 bets, 4 grandfathered malformed refs, allowlist size 4). HOLD.
- V6: `grep -rnE '^\s*sorry\s*$' lean/` -> exactly one hit,
  `lean/Erdos251/Statement.lean:21`. HOLD.
- V7: `grep -n "a6276f4c" lean/lake-manifest.json` -> line 8, rev
  `a6276f4c6097675b1cf5ebd49b1146b735f38c02`; `tail -c 1
  lean/lean-toolchain | od -An -tx1` -> `0a`. HOLD.
- V8: `grep -n "BET-20260804-14" ledger/bets.yaml` -> line 330,
  inside the `open:` block; claim and resolution byte-match the
  dispatch (q6) quotation. HOLD.
- W1: `git status --porcelain` at close ->
  `?? dossier/item-0035-workpapers/` and
  `?? item-0035-kickoff-v1.md`. The first is the run's output
  directory (expected). The second is the ephemeral dispatch
  document itself, present before session start (V1 record), never
  committed per its own header; the item-0010 precedent (A2 W0:
  "Working tree clean except the untracked ephemeral kickoff file")
  applies. No run write outside `dossier/item-0035-workpapers/`.
  HOLD, with the deviation named.
- W2: `python3 scripts/mathjax_lint.py
  dossier/item-0035-workpapers/*.md` -> 0 problems (certificate and
  this report). HOLD.
- W3: `LC_ALL=C grep -nP '[^\x00-\x7F]'
  dossier/item-0035-workpapers/*` -> no output (ASCII only). HOLD.
- W4: `sha256sum` over A1-A7 re-run at close -> unchanged vs the
  dispatch Section 2 table. HOLD.
- W5: `wc -l separator-instance-certificate.md` -> 450, inside the
  [120, 450] envelope (at the ceiling; zero headroom -- see
  Observations). HOLD.
- W6: two invocations of `model_word_census_35.py`; emitted
  `model_word_census_35_tables.txt` sha256
  `1b87c64a9c8235570b4c7a0718eb2d40bc78e8204bf1c3c0f5bfb9582c21ef10`
  both times (byte-identical; deterministic). The post-audit script
  edit (Observations item 2) was followed by two fresh runs; the
  emitted tables remained byte-identical to the pre-edit bytes.
  HOLD.
- W7: rule-16(a) clause-vs-body diff present as certificate Section
  11; no verdict clause strengthens a body support class. HOLD.

## Observations

1. In-run adversarial audit (disclosed; local, corpus-only, web
   OFF). A six-agent refuter/auditor fan-out ran against the draft
   certificate (three proof lenses: case analysis, lemmas,
   sharpness/readings; plus compliance, quotation-fidelity, and
   script audits), followed by a focused re-check of the repaired
   text. Zero FATAL findings; (M-BOUND) survived every refutation
   attempt. Sustained findings, all repaired in place before
   hand-off:
   - (MAJOR, readings) The draft claimed the falsification covers
     "every 'along a scale sequence' reading" unscoped. Refuted by
     a pooled reading -- the union of middles accumulated across
     DIFFERENT per-scale classes -- which is TRUE in the model (by
     the certificate's own Section 7 boundary classes) exactly as
     for the primes, so that reading separates nothing. Repaired:
     the falsified scope is now explicitly the per-class count
     (certificate Sections 2, 3, 6, 11), and the pooled quantity is
     openly recorded as outside the falsified scope (Section 6).
     This deliberately narrows the coverage clause of the dispatch
     Section 4 mandated remark, whose literal form carries the
     over-broad claim; the inheritance content of the remark is
     intact and the dispatch's (M-FALS) target is delivered in
     full. Whether the dispatch owes itself a rule-17 v2 marker for
     that sentence is the operator's call.
   - (MINOR, L5(c)) "so g_17 = 6" over-claimed what (n4) alone
     yields; weakened to "so 17 notin S_4", which is all L5(c)
     consumes.
   - (MINOR, primes restatement) The Section 2 restatement now
     carries the anchor's "on all large good z" threshold
     qualifier.
   - (MINOR, script) The self-check now prints every mismatch row
     (previously capped at 50, contradicting the header's "printed
     in full"); the output path is now anchored to the script's own
     directory (STOP-9 hygiene). Emitted tables byte-identical
     before and after.
2. Independent reproduction (MEASURED corroboration; no gate rests
   on it). Two auditor-written re-implementations -- one
   pure-integer, decimal-threshold at precision 80, no float log --
   reproduced the census output exactly at both $`10^{5}`$ and
   $`10^{7}`$: all ten per-$`(J,K)`$ summary rows, every stretch
   run, and every two-middle class listing. All 77 two-middle
   classes in range have the proved boundary form. The minimum
   distance of $`\ln{}(q_n)/2`$ to an integer over the full range
   is 8.56e-8, above the 1e-9 decimal-fallback trigger, consistent
   with the reported 0 fallbacks; gates (i)/(ii) were additionally
   proven live by mutation tests (both fire and exit nonzero).
3. The certificate sits at exactly 450 lines -- the envelope
   ceiling. Any future amendment pass that adds a net line breaches
   STOP 7; an operator-side note for any repair dispatch.
4. The pooled-quantity record (certificate Section 6) states a
   primes-side consequence (pooled union infinite) that is an
   immediate consequence of the carried A1 Section 5.2 sentence; it
   subtracts from the separation claim rather than strengthening
   anything; recorded here because the discipline register reads
   "nothing about the primes beyond the verbatim (q3) quotation"
   strictly.
5. The (q1) display was verified byte-identical against A2 W3.1 by
   `cmp` before and after the envelope trims ((q2) located verbatim
   in A1 Section 8; STOP 4 never fired). No STOP condition fired at
   any point in the run.
6. D2 pricing: the default range $`q_n\le10^{7}`$ (630405 terms)
   was kept; runtime approximately 8 seconds per invocation,
   single-threaded. No larger bound was needed -- the census is
   corroboration, not evidence.

## Follow-up candidates (non-binding)

- F1 (operator, cheap): if the dispatch text is ever re-issued, a
  rule-17 v2 could align the Section 4 remark's coverage clause
  with the per-class scoping the certificate carries (Observations
  1); alternatively the deviation record here suffices.
- F2 (item-0038 synergy): the pooled middle-diversity statistic
  (union of middles across the Section 7 boundary classes) is a
  cheap, well-defined model statistic and a natural calibration row
  for the fixed-rank census companion of item-0038, if wanted.
- F3 (item-0036 synergy): the explicit stretch-length lower bound
  $`(3\cdot7^{m-1}-m+1)/m`$ of certificate L5(e) is available if a
  model-side growth row is ever priced there.
- F4 (operator): BET-20260804-14 resolution material is complete
  and named in certificate Section 13; scoring is operator
  judgment, never in-run.

## Artifact hashes (final bytes)

- `separator-instance-certificate.md` sha256
  `17b7ae436f85f6732aebf5de84aea9a7884fc1a3df964e48fa81e5177194aebd`
- `model_word_census_35.py` sha256
  `3631edc056acbd49ff8d95e7bb49116c95fcde7726d9620b5ccb1dbb31ef4014`
- `model_word_census_35_tables.txt` sha256
  `1b87c64a9c8235570b4c7a0718eb2d40bc78e8204bf1c3c0f5bfb9582c21ef10`

This report's own sha256 is computed over its finalized bytes at
close and stated in the hand-off message (a file cannot contain its
own hash); operator-side hashing remains the only canonical
integrity layer. The executor commits nothing and pushes nothing;
ledger entry, HASHES lines, HANDOVER refresh and the roadmap
done-move are steering's, riding the operator's single ratifying
apply (rule 25).

END OF item-0035 COMPLETION REPORT
