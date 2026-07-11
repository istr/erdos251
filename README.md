# erdos251

Attempt on Erdős Problem #251: is S = sum_{n>=1} p_n / 2^n irrational?
(p_n = n-th prime; decimal expansion OEIS A098990; statement formalized in
google-deepmind/formal-conjectures.)

This repo is the single source of truth for a human-plus-frontier-model
research pilot. Conversations are ephemeral scratch; durable state lives here.

## Layout

- `HANDOVER.md`        cold-start entry point. Read this first.
- `dossier/`           canonical research notes (runde0 = pre-dissection, frozen).
- `payloads/`          exact, hashed model inputs per stage (contamination classes).
- `runs/`              one directory per model run: config, transcript, output.
- `lean/`              Lake project; vendored target statement; CI = lake build.
- `ledger.yaml`        pre-registered bets and Brier scoring.
- `roadmap/`           work items (roadmap-items store; one file per item).

## Ground rules

1. Firewall: payload classes A/B/C control exactly what each run may see.
   See HANDOVER.md section 4. Stage 1a runs must never see class-C material.
2. Stateless prover runs: payload in, artifact out. Repair loops carry only
   the Lean compiler error, never accumulated chat.
3. Reviews are blind: reviewers get claims plus minimal dependencies, not the
   producer's reasoning. Rebuttal happens after the independent verdict.
4. Every quantitative expectation is registered in `ledger.yaml` before the
   evidence arrives, and scored after.
5. Working language of canonical artifacts: English (cross-model interop).
   Steering conversations may be German.
6. Citation etiquette: cite Erdős's original sources for the problem; cite the
   site as: T. F. Bloom, Erdős Problem #251, https://www.erdosproblems.com/251
   (with access date). ScPu11 = J.-C. Schlage-Puchta, Acta Arith. 126 (2007),
   295-303, arXiv:1105.1451.

## Status

Skeleton materialized 2026-07-11. Lean project is UNVERIFIED (no toolchain in
the authoring sandbox); first CI run validates. Roadmap items are `proposed`;
the initial commit by the operator is the ratifying act for the skeleton, item
statuses are advanced separately via the roadmap script.
