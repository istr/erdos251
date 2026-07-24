# Run protocol

One directory per run: `runs/<YYYYMMDD>_<model>_<stage>/` containing
`config.yaml` (copy of `_template/config.yaml`, filled), `transcript.md`
(verbatim), `output.md` (the artifact), optional `output.lean`.

Rules:
1. Stateless: a run receives exactly one payload file (verify sha256 against
   payloads/HASHES.txt and record it in config.yaml) plus nothing else.
2. Stage 1a and 1a0 runs: web access OFF where the provider allows it; the
   payload states the no-external-literature rule either way.
3. Repair loops (Lean): only the compiler error message travels back into the
   next turn. No accumulated reasoning, no restated context.
4. Review runs: reviewer receives the claims ledger of the reviewed output plus
   minimal dependencies, NOT the producer's reasoning or transcript. Rebuttal
   only after the independent verdict is archived.
5. Nothing is deleted. Failed runs are data.

## Clarifications (2026-07-12, after run 20260712_fable5_1a_item0001)

6. "No external tools" in stage payloads means NETWORK/LITERATURE tools.
   Local code execution without network access is permitted and encouraged
   at every stage; record enabled tools in config.yaml.
7. Provider turn limits: continuing in the same chat is permitted. Feed back
   only the model's own prior trace/output (record its sha256 in the next
   turn's input); note the pattern in config notes ("consolidation turn").
   Contamination class discipline is unchanged by continuation.
8. Memory-bearing consumer surfaces (e.g. standard claude.ai chats) are NOT
   class-clean for this operator; use incognito mode or the API for stage
   runs.

9. Environment capability register (2026-07-12). Gemini anonymous
   ("temporary") chats have NO code execution: models there cannot compute
   hashes (root cause of the 1a self-hash failures) and cannot write file
   artifacts -- output arrives inline; the operator copies, archives, and
   hashes it (record "serialization: inline-copy"; beware UI/copy-level
   corruption, a different class from the 1a escape-eating writer bug).
   General rule: NEVER demand tool-dependent outputs (hashes, file writes,
   execution results) in environments lacking the tool -- an unsatisfiable
   instruction is a confabulation trap. Hash requests in wrappers include
   the fallback "if no code execution is available, say so instead of
   outputting a number". Operator-side hashing remains the only canonical
   integrity layer.
   Register entry (2026-07-15): claude.ai steering surface -- container
   tools (bash, file view/create) can be UNAVAILABLE across whole turns;
   observed over two consecutive steering turns 2026-07-13/14,
   provider-confirmed as a partial outage of container creation
   (status.claude.com incident 89rcltb8qg63, posted 2026-07-14 21:31
   UTC), recovered by 2026-07-15 18:44 UTC. Effect: steering patch
   production and repo verification blocked for the duration; executor
   and operator lanes unaffected. Discipline: probe once, then stop --
   repeated probing of a dead container is noise; stage content
   textually for operator pre-review and ship on recovery.
   Register entry (2026-07-19): claude.ai steering surface --
   container CAPACITY varies per session and is a per-session
   observation, never a surface property: 3 GB RAM / 1 core at the
   item-0019 close (ANN-56) vs 96 GB total / 88 GB free at the
   item-0017 probe (2026-07-13). Consequence: review-gate scopes
   that assume the large container (e.g. 1e9 in-core re-execution)
   must carry a declared-partial-scope fallback; exercised at the
   item-0019 close (steering R1-light at {2e6, 2e7, 1e8} full +
   independent stretch-certificate verification; residual
   re-execution program staged, optional, non-blocking).

10. Capability claims by models about environments -- their own or other
    vendors' -- are NOT evidence (observed 2026-07-12: gemini-3.1-pro
    asserting claude.ai has no code execution while this repo's fable runs
    hashed and sieved in exactly that environment). The capability register
    is empirical-only: per surface, per observation, with dates.

11. Trace-artifact layer register (2026-07-13). Displayed reasoning
    threads on consumer surfaces are DERIVED renderings (rendered or
    summarized), not raw traces; the raw layer is accessible to neither
    the model nor the operator (claude.ai steering surface, confirmed
    2026-07-13: transcript only, on both sides). Every archived trace or
    thread artifact records trace_artifact_layer: raw | rendered |
    summarized | undetermined, plus the derivation chain where known;
    prefer the least-derived available artifact. Consequences:
    artifact-to-artifact comparisons remain valid (the 15.6
    anchor-propagation finding stands); operator-side hashes certify
    WHICH rendering exists, never what produced it -- integrity is not
    provenance depth; model self-reports about the underlying
    computation remain non-evidence (rule 10 applies to introspection
    too).

12. Error-landing check for route proposals (2026-07-16). When a proposed
    route carries an O(1) error term through a divergent summation,
    determine WHERE the error lands BEFORE building: leading coefficient
    vs additive constant is the whole question. Coupling the error to a
    divergent index sum (dyadic blocks: once per block over j log r,
    summed harmonically) inflates the leading coefficient by C/log r for
    every fixed ratio r; coupling the SAME error to a bounded telescoping
    variation (discrete Abel: sum (w i - w (i+1)) = w 2 - w P <= 1/log 2)
    keeps it additive. The check is cheap to settle numerically in
    advance and is exactly what caught the item-0015 s3 dyadic MP-M2
    defect (coefficient 4 vs the required exactly-1; ANN-37) before any
    Lean investment.
13. Scratch-file probing against the built olean (2026-07-17). When
    iterating inside a heavy module, develop candidate proofs in an
    untracked scratch file that imports the module and states the
    target under a scratch name; transplant once when it compiles.
    A sorried original inside the imported .olean is only sorryAx and
    does not interfere. This turned item-0015 s5's five-minute rebuild
    cycles into seconds, and its corollary shaped s6: when a session
    can live one layer downstream (Conditional against the cached
    Counting olean), scope it there and the cycle never appears.
14. Post-refine beta-reduction trap (2026-07-17). After `refine` with
    lambda witnesses, per-index goals keep un-beta-reduced
    applications like `(fun r => f (X + r)) r`; `set` silently fails
    to fold them, omega then sees distinct atoms and fails with large
    counterexamples that name nothing. One `show <target type>`
    beta-reduces the goal and fixes all downstream matches. Same
    family as the s5 isDefEq sinks (ANN-44/47): the cost is in what
    the tactic silently does NOT match.
15. Asymptotic budget sheet for exchange-regime candidates
    (2026-07-18). Before any proof investment in a candidate theorem
    or route targeting the exchange regime, evaluate EVERY constant
    and factor mechanically at k = (2/ln 2 + o(1)) loglog x against
    log x, x^eps and the pigeonhole reserve; script the sheet where
    possible and commit it with the workpapers. Hidden k!, 2^k or
    exp((1+o(1)) k log k) factors are immediate no-gos: they exceed
    every power of log x at exchange depths. Provenance: item-0017 R2
    FATAL-2 / F17.9 -- a fixed-k exclusion constant silently promoted
    to growing k survived drafting, an in-run checker pass and R1,
    and would have been caught by this sheet at statement time.
    Rule 12 is the special case where the landing slot of one error
    term decides; this rule is the general per-candidate ledger.
16. Verdict-body clause diff and dependency audit (2026-07-18).
    (a) Before a dossier enters its review gate, its verdict section
    is diffed clause by clause against the body's support classes
    (proved / measured / heuristic / model-only) by a dedicated pass;
    scope qualifiers present in the body must survive promotion into
    the verdict verbatim. Recurrence pattern: item-0005 P1 and
    item-0017 FATAL-1 (process finding B4). (b) Computation-audit
    payloads carry an explicit dependency/conditioning checklist item
    beyond constant re-execution: same-run checkers verified every
    constant yet could not audit dependency structure (R2 MAJOR-1;
    process finding B5).
17. Single-source pin in kickoffs (2026-07-19). A kickoff states
    its pin literal exactly once (Section 0); every other
    reference, validity predicates included, points at "the
    Section 0 pin" symbolically. Any kickoff revision bumps the
    version marker, re-runs an internal consistency pass (all pin
    references; every predicate satisfiable at the new pin), and
    the superseding sha256 is re-booked in the ledger -- the
    recorded hash of a superseded version stays as history.
    Provenance: the item-0018 M1 dispatch. The v1 kickoff
    duplicated the pin literal into its predicate list AND was
    unsatisfiable as authored (the HEAD pin predated an object
    another predicate required); the operator revision fixed
    Section 0 but the stale literal survived, costing the run a
    deviation resolution (resolved correctly per the item-0017
    anchors-unchanged precedent; ANN-53).
18. Pin semantics under bookkeeping races (2026-07-19). A kickoff
    pin denotes the last pre-bookkeeping CONTENT state; HEAD may
    legitimately be ahead of it by bookkeeping-only commits
    (HANDOVER.md, ledger.yaml, payloads/HASHES.txt,
    runs/README.md, roadmap/). At session start the runner
    verifies (a) git diff pin..HEAD touches only those paths, and
    (b) every Section-2 read-only anchor is byte-identical across
    both states; then the session pins to HEAD and records the
    delta in the report. Any content-path delta remains a
    STOP-AND-REPORT. Provenance: the ANN-anchored kickoff-hash
    verification necessarily advances HEAD past any pre-authored
    pin (item-0018 M1: stale duplicated predicate, rule 17;
    item-0018 M2: Section-0 pin vs ANN-54 presence, report O3 --
    second recurrence, both resolved correctly by the runs).
19. Primary-anchor authoring (2026-07-24). Prose that will land in a
    committed artifact -- statement text, public exposition, or a
    byte-exact block inside a dispatch -- and any finding asserted
    about such an artifact, is authored against the primary anchor,
    with the governing sentence quoted verbatim in the authoring turn.
    A ledger entry, a review finding, a repair log, or a hand-off
    message may direct attention to a claim; it may never be the
    source of its wording or the evidence for its state. Summaries
    drop scope qualifiers, and a dropped qualifier is
    indistinguishable from a strengthened claim. The gate is
    mechanical: the authoring turn must contain the quote, so a
    reviewer can check the wording against its source without
    re-deriving it. Provenance: item-0010 R1/R2 chain, six steering
    errors -- two findings asserted from executor hand-off text that
    the artifacts contradicted, and four wordings authored from
    ledger notes or reviewer summaries, of which the public
    "weakest currently known sufficient endpoint" sentence dropped
    exactly the qualifier standing in collision-gap-audit.md:39.
    A finding that names more than one location is routed with its
    full location list quoted, and every named location receives
    either a repair in the dispatch or a deferral stated by name with
    a reason. A partial routing without a residue note is
    indistinguishable from a silent decision not to repair, and the
    executor cannot tell the difference either.
    Second pattern, same chain: a cross-family finding located at both
    writeup/status.md and separator-repricing.md was routed only to
    the public page; the report half survived a full repair pass and
    was caught by the executor, not by steering.
