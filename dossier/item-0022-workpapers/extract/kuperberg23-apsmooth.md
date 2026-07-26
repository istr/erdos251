# EXTRACTION: Vivian Kuperberg, "Sums of singular series along arithmetic progressions and with smooth weights"

Source (only evidence base): /home/istr/pro/erdos251/dossier/2301.06095v1.pdf
sha256 c67fdd9c9a822581371409e3fae54c9fcf97e0bd1a0b534fb22ea7a4b61f9617
(operator-verified; re-verified this session).
arXiv:2301.06095v1 [math.NT] [arXiv preprint] 15 Jan 2023. Author(s):
Vivian Kuperberg. 19 pages. PDF metadata: Creator "LaTeX with hyperref",
Producer "dvips + GPL Ghostscript GIT PRERELEASE 9.22", CreationDate
"Wed Jan 18 02:56:39 2023 CET". No journal reference is printed on the
paper.

Front-matter identification CONFIRMED against the dispatch: author
"Vivian Kuperberg", title "Sums of singular series along arithmetic
progressions and with smooth weights", arXiv:2301.06095v1. No
deviation. This is confirmed to be a different paper from the anchored
arXiv:2210.09775v2 (a separate, non-item-0022 shelf item cited by report
1's footnote 6 for a different Kuperberg result on sums over large sets
$`T_k(h)`$; see checklist row R1-013).

---

## Transcription conventions

ASCII-folded. No TRANSCRIPTION-UNSURE passages encountered.

## 1. Front matter (verbatim)

"SUMS OF SINGULAR SERIES ALONG ARITHMETIC PROGRESSIONS AND WITH SMOOTH
WEIGHTS / VIVIAN KUPERBERG / Abstract. Sums of the singular series
constants that appear in the Hardy-Littlewood k-tuples conjectures have
long been studied in connection to the distribution of primes. We study
constrained sums of singular series, where the sum is taken over sets
whose elements are specified modulo r or weighted by smooth functions.
We show that the value of the sum is governed by incidences modulo r of
elements of the set in the case of arithmetic progressions and by
pairings of the smooth functions in the case of weights. These sums shed
light on sums of singular series in other formats."

## 2. Statement cited by item-0022's reports (verbatim)

### 2.1 The perfect-matching / pairing main-term structure (report 1's "matched-flank" analogy)

p.3, Theorem 1.1 (restricted sums along arithmetic progressions): "Fix a
modulus $`r\ge1`$, an integer $`k\ge1`$, and k congruence classes
$`c_1,\ldots,c_k`$ modulo r. Define $`\mathcal{B}_k`$ as in (8). Let
$`q\ge1`$ be a squarefree integer with $`(r,q)=1`$, and define
$`V_k(q,h;r,c_1,\ldots,c_k)`$ as in (6). For $`h\ge3`$,

$$V_k(q,h;r,c_1,\ldots,c_k) = \sum_{\sigma\in\mathcal{B}_k}\prod_{(i,j)\in\sigma}V_2(q,h;r,c_i,c_j) + O_{r,k}\left(h^{k/2-1/(7k)}\left(\frac{q}{\phi(q)}\right)^{2^k+k/2}\right).$$"

where (p.3) $`\mathcal{B}_k`$ is defined as "the set of perfect matchings
of $`[1,k]`$" (a perfect matching being a set of unordered pairs $`(i,j)`$
partitioning $`[1,k]`$).

p.4, Theorem 1.2 (the corresponding asymptotic for $`R_k(h;r,c_1,\ldots,c_k)`$)
sums over partitions of $`[1,k]`$ into doubleton and singleton blocks,
with the doubleton part again organized by perfect matchings $`\sigma \in
\mathcal{B}(j+1,\ldots,k-j)`$ of the remaining indices (eq. (9)).

This confirms report 1's characterization: the main-term structure of
these restricted sums is governed by perfect matchings/pairings of the
index set, with the dominant contribution occurring when the paired
congruence classes coincide (Theorem 1.2's remark, p.4: "if
$`\#\widetilde{\mathcal{B}}(c_1,\ldots,c_k)`$ is the number of ways to
pair the $`c_i`$'s such that every pair has equal values... the theorem
implies $`R_k(h;r,c_1,\ldots,c_k) =
\#\widetilde{\mathcal{B}}(c_1,\ldots,c_k)\left(-h\frac{\phi(r)}{r}\log
h+C_0(r)h\right)^{k/2}+O_{r,k}(h^{k/2}(\log h)^{k/2-1})`$").

## 3. Uniformity ledger

Theorem 1.1 and 1.2 hold for fixed $`r,k`$ as $`h\to\infty`$, with
implied constants depending on $`r`$ and $`k`$; the paper gives no claim
uniform in growing $`k`$.

## 4. NOT-FOUND probe

Checked and NOT present in this paper: any Hardy-Littlewood-type lower
bound for a prime-counting function $`\sum_{\text{sites}}
S_{\text{side}}(P(\text{site}))`$ on a parity-blocked flank class (report
1's "Input (i)"). This paper's results (Theorems 1.1-1.5) are all
asymptotic formulas for sums of the algebraic singular-series constant
itself (or its restricted/weighted variants), never lower bounds for a
prime-tuple counting function. This matches report 1's own
characterization of the gap between what this anchor supplies and what
its "Input (i)" would require.

## FLAGS

No sha256 mismatch, no TRANSCRIPTION-UNSURE passages.
