# EXTRACTION: Vivian Kuperberg, "Odd moments in the distribution of primes"

Source (only evidence base): /home/istr/pro/erdos251/dossier/2109.03767v3.pdf
sha256 e1bbabbd259d43bf80614756bc96ddb13612e82bdd8887d536612bd7d5441f94
Transcribed from the anchored PDF named above; fidelity repair applied
per the ANN-78 grade (`extract-grades-r1.md`) at this pin; re-grade
pending.
arXiv:2109.03767v3 [math.NT] [arXiv preprint] 29 Jul 2024 (v3; the arXiv
identifier 2109 dates the original submission to September 2021). This
paper is listed as "V. Kuperberg, Odd moments in the distribution of
primes, arXiv:2109.03767, 2021" at `2301.06095v1` reference 4, p.19;
that string is not printed in this anchor, whose own bibliography
carries no entry for it. Author(s): Vivian Kuperberg. 51 pages. PDF
metadata: Creator "LaTeX with hyperref", Producer "pdfTeX-1.40.25",
CreationDate "Wed Jul 31 02:11:45 2024 CEST" (a re-render timestamp for
this v3 upload). No journal reference is printed on the paper.

Front-matter identification, read from p.1 of the anchor: author
"Vivian Kuperberg", title "Odd moments in the distribution of primes",
arXiv:2109.03767v3. No deviation.

---

## Transcription conventions

ASCII-folded. No TRANSCRIPTION-UNSURE passages encountered.

## 1. Front matter (verbatim)

"ODD MOMENTS IN THE DISTRIBUTION OF PRIMES / VIVIAN KUPERBERG /
Abstract. Montgomery and Soundararajan showed that the distribution of
psi(x+H) - psi(x), for 0 <= x <= N, is approximately normal with mean ~
H and variance ~ H log(N/H), when N^delta <= H <= N^{1-delta}. Their
work depends on showing that sums Rk(h) of k-term singular series are
mu_k(-h log h + Ah)^{k/2} + O_k(h^{k/2-1/(7k)+eps}), where A is a
constant and mu_k are the Gaussian moment constants. We study
lower-order terms in the size of these moments. We conjecture that when
k is odd, Rk(h) =~ h^{(k-1)/2}(log h)^{(k+1)/2}. We prove an upper bound
with the correct power of h when k = 3, and prove analogous upper bounds
in the function field setting when k = 3 and k = 5. We provide further
evidence for this conjecture in the form of numerical computations."

## 2. Statements extracted from the anchor (verbatim)

### 2.1 The Montgomery-Soundararajan Rk(h) theorem, as independently restated by this anchor

p.3 (Section 1, eq. (4)): "showing that for any nonnegative integer k,
for any h > 1, and for any eps > 0,

$$R_k(h) = \mu_k(-h\log h + Ah)^{k/2} + O_k(h^{k/2-1/(7k)+\varepsilon}),$$

where $`A = 2 - \gamma - \log 2\pi`$. Their estimate on $`R_k(h)`$
implies their bound on the moments."

This anchor restates the Montgomery-Soundararajan estimate in its own
introduction, as the result it builds on: eq. (4) is printed on p.3 in
exactly that role.

### 2.2 The odd-moment conjecture and upper bound (Conjecture 1.1 and Theorem 1.2, p.3)

p.3, Conjecture 1.1: "Let k >= 3 be an odd integer, and let h > 1. With
Rk(h) defined as above,

$$R_k(h) \asymp h^{(k-1)/2}(\log h)^{(k+1)/2}.$$

The conjectured power of log h here comes from numerical evidence, which
we present in Section 5."

p.3, Theorem 1.2: "For h >= 4 and R3 defined in (3),

$$R_3(h) \ll h(\log h)^5.$$"

## 3. Uniformity ledger

- Theorem/eq.(4)'s bound holds for any nonnegative integer k, any h>1,
  any eps>0, with an implied constant depending on k and eps.
- Theorem 1.2's upper bound is specific to k=3 only. What the paper
  states, on p.3, is: "For k odd, we do not know, even heuristically,
  which terms contribute to the main term in $`R_k(h)`$; for this
  reason, we do not know what the constant should be in front of the
  asymptotic in Conjecture 1.1." That no asymptotic for $`R_k(h)`$ at
  odd k is proved here -- only an upper bound, and only the conjectured
  power of h (not of log h) at k=3 -- is an inference from Theorem 1.2
  and Conjecture 1.1 as printed, not a statement the paper makes in
  those words.

## 4. NOT-FOUND probe

Checked and NOT present in this paper: any claim about a "flanked" or
"aggregated simplex" domain, or about uncentered second moments
$`\sum\mathfrak{S}(H)^2`$.

## FLAGS

No sha256 mismatch, no TRANSCRIPTION-UNSURE passages.
