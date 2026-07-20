# Notation

The table keeps established project notation unchanged. “Pinned” below means the parameter map fixed in the relative-extension statement layer, not a claim about every possible parameter choice.

| Symbol or name | Meaning | Source | Scope qualification |
| --- | --- | --- | --- |
| $p_n$ | The $n$-th prime, with $p_1=2$. | `dossier/chain-v1.md`, §1 | One-indexed in the prose sources. |
| $g_n$ | The consecutive prime gap $p_{n+1}-p_n$. | `dossier/chain-v1.md`, §1 | The Lean gap index is shifted as documented in the statement layer. |
| $S$ | $\sum_{n\ge1}p_n/2^n$. | `dossier/chain-v1.md`, §1 | The original irrationality question remains open. |
| $x$ | The asymptotic prime-size parameter. | `dossier/relext-statements.md`, §1 | All proved matched-flank claims are for sufficiently large $x$. |
| $s$ | A fixed lower threshold on site indices. | `dossier/relext-statements.md`, §1 | In the proved lower bound, the eventual $x$-threshold may depend on $s$. |
| $J,K,L$ | Prefix depth, suffix depth, and full word length, with $L=J+1+K$. | `dossier/relext-statements.md`, §1 | At the pinned map, $J=K=\lceil\log_2 D\rceil$. |
| $S_x^{\prime(s)}$ | Filtered sites at scale $x$, beyond threshold $s$, satisfying the window and two tail caps. | `dossier/relext-statements.md`, §§1, 3 | Filters-first: caps are inside the counted set. |
| $P=(a,c)$ | A matched pair of prefix and suffix gap words, called a side pair or flank pair. | `dossier/relext-statements.md`, §3 | Entries are positive even gaps on realized prime sites. |
| $\mathrm{Fam}(S_x^{\prime(s)})$ | The realized family of side pairs with $N_P\ge1$. | `dossier/relext-statements.md`, §3 | Depends on the filtered site set. |
| $\mathrm{Fam}_2(S_x^{\prime(s)})$ | The realized side pairs with $N_P\ge2$. | `dossier/relext-statements.md`, §3 | Counts multi-member classes, not classes with two distinct middles. |
| $N_P$ | The number of filtered sites in side-pair class $P$. | `dossier/relext-statements.md`, §3 | $N_P\ge1$ on the realized family. |
| $N_{P,d}$ | The number of members of class $P$ whose middle gap is $d$. | `dossier/relext-statements.md`, §3 | Realized middle gaps are even and at least $2$. |
| $Q(x,s)$ | The class-normalized ordered within-middle pair sum used in `B2.pairs`. | `dossier/item-0020-workpapers/proofs.md`, Claim C3 | Singleton classes contribute zero. |
| `MatchedFlankLower` | A positive-proportion lower bound for the mass of multi-member side-pair classes. | `dossier/relext-statements.md`, §7.1 | Proved asymptotically at the pinned map with $\delta=1/2$. |
| `RelExtensionUpper` | An adversarial-selection upper bound on repeated middle mass inside realized side classes. | `dossier/relext-statements.md`, §7.1 | Open. |
| `TailIntersection` | A positive-density lower bound for filtered sites beyond each threshold. | `dossier/relext-statements.md`, §7.1 | Proved at the pinned map. |
| `B2.pairs` | The class-normalized pair estimate sufficient for `RelExtensionUpper`. | `dossier/relext-upper.md`, §2 | Open; the implication to `RelExtensionUpper` is proved. |
