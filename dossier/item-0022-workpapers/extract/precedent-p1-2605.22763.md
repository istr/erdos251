# EXTRACTION: George Tsoukalas et al., "Advancing Mathematics Research with AI-Driven Formal Proof Search"

Source (only evidence base): /home/istr/pro/erdos251/dossier/2605.22763v2.pdf
sha256 d71b78f1ea764ea0489b7fdec3c53d394cf99cd2ac2a22c1d61e744618e9573d
Transcribed from the anchored PDF named above; fidelity repair applied
per the ANN-78 grade (`extract-grades-r1.md`) at this pin; re-grade
pending.
arXiv:2605.22763v2 [cs.AI] [arXiv preprint] 8 Jun 2026 (printed dateline
"2026-6-9" on the paper's own header). Author(s): George Tsoukalas,
Anton Kovsharov, Sergey Shirobokov, Anja Surina, Moritz Firsching,
Gergely Berczi, Francisco J. R. Ruiz, Arun Suggala, Adam Zsolt Wagner,
Eric Wieser, Lei Yu, Aja Huang, Miklos Z. Horvath, Andrew Ferraiuolo,
Henryk Michalewski, Edward Lockhart, Codrut Grosu, Thomas Hubert, Matej
Balog, Pushmeet Kohli, Swarat Chaudhuri (Google DeepMind / Aarhus
University / Google, per the printed affiliations). 60 pages. PDF
metadata: Creator "arXiv GenPDF (tex2pdf:a6404ea)", Producer "pikepdf
8.15.1". No journal reference is printed (Google DeepMind technical
report / arXiv preprint).

Front-matter identification, read from p.1 of the anchor: title, author
list and arXiv identifier are as printed there. No deviation.

---

## Transcription conventions

ASCII-folded (Erdos rendered without diacritics). No TRANSCRIPTION-UNSURE
passages encountered.

## 1. Front matter (verbatim)

"Advancing Mathematics Research with AI-Driven Formal Proof Search /
George Tsoukalas, Anton Kovsharov, Sergey Shirobokov, Anja Surina,
Moritz Firsching, Gergely Berczi, Francisco J. R. Ruiz, Arun Suggala,
Adam Zsolt Wagner, Eric Wieser, Lei Yu, Aja Huang, Miklos Z. Horvath,
Andrew Ferraiuolo, Henryk Michalewski, Edward Lockhart, Codrut Grosu,
Thomas Hubert, Matej Balog, Pushmeet Kohli and Swarat Chaudhuri /
Large language models (LLMs) increasingly excel at mathematical
reasoning, but their unreliability limits their utility in mathematics
research. A mitigation is using LLMs to generate formal proofs in
languages like Lean. We perform the first large-scale evaluation of
this method's ability to solve open problems. Our most capable agent
autonomously resolved 9 of 353 open Erdos problems at the per-problem
cost of a few hundred dollars, proved 44/492 OEIS conjectures, and is
being deployed in combinatorics, optimization, graph theory, algebraic
geometry, and quantum optics research. A basic agent alternating
LLM-based generation with Lean-based verification replicated the Erdos
successes but proved costlier on the hardest problems. These findings
demonstrate the power of AI-aided formal proof search and shed light on
the agent designs that enable it."

## 2. Statements extracted from the anchor (verbatim)

### 2.1 The headline solve counts (Introduction, pp.1-2)

p.1-2, Introduction: "Our full-featured agent autonomously solved 9
Erdos problems out of 353 attempted, including two questions that had
been open for 56 years [54, 7, 17], at the inference cost of a few
hundred dollars per problem. It also proved 44/492 open conjectures
from the Online Encyclopedia of Integer Sequences (OEIS)..."

### 2.2 The basic agent replicating the Erdos successes (Introduction p.2; Section 5, p.8)

Two passages, printed six pages apart and quoted separately.

p.8, Section 5 ("Impact of Agent Architecture and Model"): "We compared
the agents by analyzing the solve rate against the cost (in US dollars)
per successfully proven problem."

p.2, Section 1 (Introduction): "To understand the impact of the agent
design on these results, we did a post-hoc analysis of the performance
of the full-featured and basic agents, as well as two agents with
intermediate capabilities, on the 9 Erdos problems solved by the
full-featured agent. Remarkably, the basic agent solved all 9 problems,
though at a higher cost on the harder problems."

### 2.3 Lean mechanical verification (Section 2, p.2; p.4)

p.2, Section 2 ("Lean."): "Lean [43] is a proof assistant in which
definitions, theorems, and proofs are all mechanically verified code...
A proof is correct if it leads the compiler to a state with no pending
goals."; and p.4: "after each solve, experts on our team validated that
the Lean statement faithfully captured the original conjecture."

### 2.4 Public availability of results (Introduction, p.2)

p.2 (Introduction, final sentence): "All Lean proofs and select
natural-language proofs are available in
https://www.github.com/google-deepmind/alphaproof-nexus-results."

## 3. Uniformity ledger

Not applicable in the Appendix B sense (this is an empirical/systems
paper, not an asymptotic theorem); the counts above (9/353, 44/492) are
the paper's own reported totals for its full-featured agent (D) as
described in Section 2 and Table 1, not a claim of completeness over
all Erdos problems (p.11 states "Even most Erdos problems remain out of
reach").

## 4. NOT-FOUND probe

Checked and NOT present in this paper: a specific commit SHA for the
alphaproof-nexus-results repository (the URL is given, but no commit
hash is printed anywhere in the paper). Consistent with Appendix C.1's
ANCHORED-BY-COMMIT class for P2, this item's row is WEB-DEFERRED per
STOP 7.8 pending a commit SHA; this session does not fetch one.

## FLAGS

No sha256 mismatch, no TRANSCRIPTION-UNSURE passages. This extract was
read to PDF page 15 of 60 (abstract, introduction, Sections 2-4 covering
the agent architecture, Erdos-problem and OEIS results, and the deployed
research applications); the remaining ~45 pages (further deployment
case studies, supplementary material, references) were not read, since
no further item-0022 claim requires them. This is consistent with a
bounded citation extract per Appendix B (T1 tier for the specific
counts and mechanisms quoted above; no method-anatomy section is
carried).
