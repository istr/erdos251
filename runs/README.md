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
    (HANDOVER.md, ledger.yaml and -- since the item-0032 split --
    ledger/bets.yaml and ledger/annotations/, payloads/HASHES.txt,
    runs/README.md, roadmap/). A ledger append is now a NEW FILE
    under ledger/annotations/, so the list has to reach that
    directory or the next append trips this rule's content-path
    STOP. At session start the runner
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

20. Report standing -- anchoring is not absorption (2026-07-27;
    item-0034). Material produced outside the project's model-run
    protocol -- a stateless run, one hash-verified payload, an
    anchor-stripped object, a committed strip script, web off, the
    wrapper verbatim in the config -- has no standing as a unit of
    verification. A model-generated report that no primary anchor
    backs enters the corpus only as a list of pointers: the
    identifiers are booked, the sources are extracted and anchored,
    and the report's own prose is never the object of a per-claim
    verdict register. A verification ritual applied to an object no
    session can read manufactures standing rather than testing it.
    Provenance: item-0022 incident (dossier/item-0022-incident-r1.md),
    a per-claim register over the prose of three operator-held reports
    reading CONFIRMED with not one row checkable in the tree; ANN-74
    wrote the principle down one apply earlier and no rule enforced it.
21. No unreadable object (2026-07-27; item-0034). An object no session
    reading only the tree can read cannot be the object of a ratified
    item: every finding about it is unfalsifiable in the tree and only
    the holder can audit it, the exact inverse of the
    single-source-of-truth charter. Held outside the tree is the worst
    of the two available states -- enough standing to drive a ratified
    item, not enough to be checked. When a source genuinely cannot be
    committed (copyright, provenance hygiene), the one permitted
    substitute is its anchored extract under rules 26 and 27: an
    in-tree, URL-and-sha256-anchored, executor-graded-clean
    transcription that is itself readable and checkable. The
    substitute is named here, not improvised per item. Provenance:
    item-0022 incident 2.4 and D2, the operator-held-object
    load-bearing defect.
22. Promotion gate, post-gate passes (2026-07-27; item-0034; closes
    B6). Rule 16(a) diffs a verdict against its body's support classes
    before the review gate; it does not reach a pass that runs after
    the gate. A verdict that moves toward a stronger support class
    (model-only -> heuristic -> measured -> proved, or a
    cannot-verify STOP -> confirmed) inside a repair, amendment or
    addendum pass requires its own pass with the primary anchor open,
    and appears as a promotion in that pass's own header. Widening an
    anchor gate mid-pass, or reading an in-tree transcription in place
    of the anchored source, is exactly the move this rule forbids.
    This settles the rule-16 strengthening carried open as B6 since
    the third verdict-promotion recurrence: B6 is CLOSED by this rule.
    Provenance: seven recurrences through the item-0022 repair (ANN-76,
    D3); B6 carried open again by ANN-64 in favour of rule 19.
23. Symmetric scope envelope (2026-07-27; item-0034). The
    scope-envelope stop fires on undershoot as well as overshoot. A
    register or artifact that comes in far under its declared envelope
    -- by a scope decision taken mid-run, or by verdicting decisive
    sections against nothing -- trips the stop exactly as an overshoot
    does; a declared scope decision does not exempt it. Provenance:
    item-0022 incident D5, a register at 33 claims against a 60-140
    envelope, 45 per cent under the low end, passed by the
    overshoot-only stop and then called complete by the completion
    policy.
24. No mid-run task change (2026-07-27; item-0034). An instruction
    that changes a run's task after its final report is issued opens a
    new run against a new pin, never an addendum to the finished run.
    An addendum has no review in its path by construction, so a
    task-changing addendum rides unreviewed into a ratifying apply.
    New task, new run, new pin, new review. Provenance: item-0022
    incident D4, a verdict that oscillated three times in one day and
    landed via an unreviewed mid-session addendum; the content was
    right, the path had no review in it.
25. One apply -- artifact and its ledger entry travel together
    (2026-07-27; item-0034). An artifact drop and the ledger entry
    that books it land in one apply. A content commit whose ledger
    entry, hash lines and handover refresh are deferred to a follow-up
    produces the bookkeeping void this rule exists to prevent: the
    follow-up may not happen, and a cold start is then pointed at
    unbooked state. This binds even the sessions repairing the record;
    the strongest evidence for it is that the defect recurred inside
    the response to its own first booking (ANN-77). Provenance:
    item-0022 incident D1, a 3308-line artifact drop that deferred its
    ledger entry, hash lines and handover to a follow-up that did not
    happen, leaving four commits unbooked.
26. Source-extract surrogate standing (2026-07-30; item-0034
    amendment). The repository does not re-publish primary-source PDFs
    (copyright, provenance hygiene); sources are held by the operator
    and the executor lane only, anchored by URL and sha256, never
    duplicated into the tree. The extract is therefore the only
    in-tree representation of its source, consumed by both lanes -- the
    analysis lane because it has no source it can open, the executor
    lane for efficiency -- so extract correctness is mandatory, not
    optional cleanup: a defective extract is a silently wrong corpus.
    The lanes are structurally non-interchangeable on fidelity; no
    convention gives the analysis lane a source to check against.
    (1) An extract is created or edited only with its anchored source
    open, and carries corpus standing only after an executor fidelity
    grade against that source over the full surface -- every display,
    numbered object, citation, quotation and negative claim, and every
    prose claim the extract makes about its source. A
    display-and-quotation grade does not reach the prose glosses; those
    are where the item-0022 2d bounces were. An extract is re-graded
    after any change, and an ungraded or defective extract directs
    attention at most.
    (2) Extract fidelity is exclusively the executor lane's to
    establish. An analysis-lane fidelity assurance is void; a fidelity
    question that arises analysis-side is recorded as open and routed,
    never answered there.
    (3) A session never grades or hashes an artifact it produced or
    repaired -- the produce/grade/repair/re-grade separation, kept
    because standing is conferred by the grade, not by the work.
    (4) Both lanes consume only graded-clean-and-hashed extracts as
    source surrogates. No ad-hoc extraction, quotation or paraphrase
    from a source bypasses the extract layer, and for the analysis
    lane the graded extract is the primary anchor in the rule-19 sense.
    (5) New or additional extraction is an operator-gated event --
    named anchor line, purpose, scope -- whose result is graded and
    newly anchored before use. A superseding extract re-books its hash
    with the superseded line kept as history, per the rule-17 pattern.
    Provenance: item-0022 disposition, ANN-77 through ANN-83; the
    ANN-79 reframing (a defective extract is a silently wrong corpus);
    the ANN-82 prose-claims surface and the separation of duties; the
    operator rule proposal of 2026-07-28 folded with the chain's later
    sharpenings (ANN-84).
27. Extract provenance header design (2026-07-30; item-0034
    amendment; ANN-82). An extract's provenance header carries source
    identity and hash only -- URL with version, source sha256,
    declared extraction method and scope -- and never grade-state, and
    never a deixis a later reader cannot resolve ("re-grade pending",
    "this session", "at this pin"). Grade-state lives in the ledger and
    the grade record, which carry it authoritatively; a header
    asserting a fidelity it has not earned lets a consumer skip the
    check, and a header carrying process-state goes stale the moment
    the process moves while the hash forbids the edit. The rule is
    prospective: the five hashed CLEAN item-0022 extracts keep their
    stale "re-grade pending" clause, superseded by the ledger, because
    editing them would break the payloads/HASHES.txt one-line-per-file
    invariant. Provenance: ANN-82 header disposition, routed here.
