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
