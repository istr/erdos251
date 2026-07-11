# Payloads and contamination classes

Class A = problem statement only            -> 1a0_control.md (optional arm)
Class B = A plus frozen runde0 dossier      -> 1a_blind.md
Class C = B plus dissection briefing        -> 1b_briefed.md

Stage 1a/1a0 runs must never receive class-C material. Hash every payload
(sha256sum, recorded in HASHES.txt) and copy the hash into the run config.
Payloads are self-contained single files by design (stateless dispatch).
For 1b, the operator MAY additionally attach the ScPu11 PDF (arXiv:1105.1451);
if attached, record that in the run config notes.
