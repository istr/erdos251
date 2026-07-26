# EXTRACTION: Vivian Kuperberg, "Odd moments in the distribution of primes"

Source (only evidence base): /home/istr/pro/erdos251/dossier/2109.03767v3.pdf
sha256 e1bbabbd259d43bf80614756bc96ddb13612e82bdd8887d536612bd7d5441f94
(operator-verified; re-verified this session).
arXiv:2109.03767v3 [math.NT] [arXiv preprint] 29 Jul 2024 (v3; original
submission 2021, per the paper's own reference to a 2021 arXiv posting
in the item-0022 kickoff dispatch and anchor 4's bibliography entry "V.
Kuperberg, Odd moments in the distribution of primes, arXiv:2109.03767,
2021"). Author(s): Vivian Kuperberg. 51 pages. PDF metadata: Creator
"LaTeX with hyperref", Producer "pdfTeX-1.40.25", CreationDate "Wed Jul
31 02:11:45 2024 CEST" (a re-render timestamp for this v3 upload). No
journal reference is printed on the paper.

Front-matter identification CONFIRMED against the dispatch: author
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

## 2. Statements cited by item-0022's reports (verbatim)

### 2.1 The Montgomery-Soundararajan Rk(h) theorem, as independently restated by this anchor

p.3 (Section 1, eq. (4)): "showing that for any nonnegative integer k,
for any h > 1, and for any eps > 0,

$$R_k(h) = \mu_k(-h\log h + Ah)^{k/2} + O_k(h^{k/2-1/(7k)+\varepsilon}),$$

where $`A = 2 - \gamma - \log 2\pi`$. Their estimate on $`R_k(h)`$
implies their bound on the moments."

This is byte-for-byte the same formula report 1 attributes (via its own
footnote 3, pointed at arXiv:math/0409258, which is outside this
session's Section 2 anchor set -- see checklist row R1-007) to
Montgomery-Soundararajan; it is independently confirmed here because
this anchor (one of the ten Section 2 anchors) restates the identical
theorem in its own introduction as the result it builds on.

### 2.2 The odd-moment conjecture and upper bound (report 1's "obere Schranken bzw. numerische Evidenz" claim)

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
- Theorem 1.2's upper bound is specific to k=3 only; the paper states
  (p.4) it does not prove an asymptotic for Rk(h) when k is odd for any
  k, only an upper bound, and only proves the conjectured power of h
  (not of log h) at k=3.

## 4. NOT-FOUND probe

Checked and NOT present in this paper: any claim about a "flanked" or
"aggregated simplex" domain, or about unzentrierte (uncentered)
Zweitmomente $`\sum\mathfrak{S}(H)^2`$; the paper works throughout with
the centered/refined singular series $`\mathfrak{S}_0`$ and its sums
$`R_k(h)`$, matching report 1's own characterization that this line "ist
weiterhin eine Theorie von Rk(h) bzw. S0, nicht von sum S(H)^2 ueber
flankierte Simplexe."

## FLAGS

No sha256 mismatch, no TRANSCRIPTION-UNSURE passages.
