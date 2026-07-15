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
