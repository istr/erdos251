# References and source guide

## External literature

<!-- sources: literature-problem, literature-schlage -->

- T. F. Bloom, “Erdős Problem #251,” <https://www.erdosproblems.com/251>, accessed 2026-07-16. This is the repository’s established citation form for the problem page.
- P. Erdős, “Sur certaines séries à valeur irrationnelle,” *L’Enseignement Mathématique* (2) 4 (1958), 93–100. This is the original source identified for the problem.
- J.-C. Schlage-Puchta, “The irrationality of some number theoretical series,” *Acta Arithmetica* 126 (2007), no. 4, 295–303, DOI 10.4064/aa126-4-1; arXiv:1105.1451. The later arXiv posting and the 2007 journal article are the same work.

## Internal project sources

<!-- sources: chain-main, frontier-verdict, item0020-verdict, claim-c1, claim-c3, claim-c4, final-observations, relext-definitions, relext-props -->

- `dossier/chain-v1.md`, especially §§1–7: the reviewed conditional irrationality theorem and its deterministic mechanism.
- `dossier/relext-statements.md`, especially §§1, 3, and 7: the filtered-site notation and the exact statement layer for `MatchedFlankLower`, `RelExtensionUpper`, and `TailIntersection`.
- `dossier/relext-upper.md`, especially §§1–2: the current verdict and the exact `B2.pairs` target.
- `dossier/item-0020-workpapers/proofs.md`, Claims C1, C3, and C4: the proved matched-flank lower bound, the square-root reduction, and the scoped barrier.
- `dossier/item-0020-workpapers/item-0020-final-report.md`: the verdict, limitations, and follow-up surface for the relative-extension campaign.

## Machine-checked sources

<!-- sources: chain-mechanism, lean-layout -->

- `lean/Erdos251/Basic.lean`, `ForkMerge.lean`, the `Counting/` modules, and `Conditional.lean`: the deterministic implication layer under the named analytic hypotheses.
- `lean/Erdos251/Supply.lean`: the checked integration of the named supply propositions into the exchange supply statement.
- `lean/README.md`: the verification layout and the boundary between the checked conditional implication and the intentionally open unconditional target.
