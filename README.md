# erdos251

## The problem

Let $`p_n`$ denote the $`n`$-th prime. Erdős Problem 251 asks whether

$$
S=\sum_{n\ge 1}\frac{p_n}{2^n}
$$

is irrational. The series converges absolutely, but that elementary fact does not decide its arithmetic nature. The original problem remains open.

**Nothing in this project is an unconditional proof of the irrationality of** $`S`$.

Please read the [status page](writeup/status.md) for a human-readable description of the mathematical findings and progress of this project.

The project studies the problem through consecutive prime gaps. Write $`g_n=p_{n+1}-p_n`$. Summation and tail identities turn a hypothetical rational representation of $`S`$ into strong lattice restrictions on weighted tails of the gap sequence. The main strategy is then to find two long prime-gap words with matching flanks but different middle behavior. Such a configuration conflicts with those lattice restrictions once its end tails are sufficiently small.

The decimal expansion of $`S`$ is OEIS A098990.
The statement is formalized in google-deepmind/formal-conjectures.

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
- `writeup/`           curated human-readable status and technical note.

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

The original problem remains open. The repository contains a reviewed
conditional irrationality theorem, a machine-checked deterministic implication
layer, and unconditional partial progress reducing the current analytic
bottleneck to `B2.pairs`. See [`writeup/status.md`](writeup/status.md) for the
curated account and [`HANDOVER.md`](HANDOVER.md) for the operational state.
