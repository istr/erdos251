# Re-grade r2 -- the five item-0022 survivors against their anchored PDFs

Phase 2d of item-0033. Executed by the local executor (Claude Opus 5,
`claude-opus-5[1m]`) on 2026-07-28 against pin
`87727aa598f74a38d9a8d4b6e788f57975bf920f`, under an ephemeral dispatch
that was never committed. This session did not produce, repair or
previously grade any of these extracts.

This is a FRESH grade on the full ANN-78 surface, plus the two axes 2b
did not cover (the robust dropped-object scan and in-tree
path-liveness). It is not a diff against the ANN-78 grade
(`extract-grades-r1.md`) or against `repair-log-2c.md` /
`repair-log-2c-residual.md`. Those records were consulted only for where
to look; no PASS below rests on them. Every PASS was earned by reading
the anchored PDF at the location.

**Verdict: THREE CLEAN, TWO BOUNCED. The pass is not terminal.**

---

## Section 0 -- preflight, all seven checks

| check | required | observed | result |
| --- | --- | --- | --- |
| P1 | `git diff --stat <pin>..HEAD` empty or `roadmap/` only | HEAD equals the pin; diff empty | PASS |
| P2 | last annotation id is `ANN-20260728-80` | last id in `ledger.yaml` is `ANN-20260728-80` | PASS |
| P3 | `item-0033` ratified at position 1 | `status: ratified`; `roadmap.py order` reports it at position 1; `roadmap.py next` reports `item-0033` | PASS |
| P4 | `extract/` holds exactly the five survivors, neither precedent | exactly the five named files | PASS |
| P5 | each PDF's sha256 matches its header and its booked line | five for five, both ways | PASS |
| P6 | no `payloads/HASHES.txt` line names anything under `dossier/item-0022-workpapers/` | none | PASS |
| P7 | the three Appendix B anchors each occur exactly once | 1, 1, 1 | PASS |

P5 in full -- computed sha256, extract header, and `payloads/HASHES.txt`
line, all three identical for each anchor:

```
74824028eb50c322f43da700fcb31fe10ce91272fe8e73695e9a4f82df22053b  dossier/1004.1072v1.pdf                 HASHES.txt:82
378433db556a2e83236f83a946d15178fe431e08f81511764325cce361b27920  dossier/singular-series-distribution.pdf HASHES.txt:83
e1bbabbd259d43bf80614756bc96ddb13612e82bdd8887d536612bd7d5441f94  dossier/2109.03767v3.pdf                 HASHES.txt:84
46b80c9b72e4eea34b74eb263b25a6eb6ee21647352b840438d35407f707ec5f  dossier/2312.09021v2.pdf                 HASHES.txt:85
c67fdd9c9a822581371409e3fae54c9fcf97e0bd1a0b534fb22ea7a4b61f9617  dossier/2301.06095v1.pdf                 HASHES.txt:86
```

**Rule-18 delta, recorded verbatim.** HEAD equals the Section 0 pin, so
rule 18 does not fire. The working tree carries four untracked files at
pin time, none of them written by this pass:

```
?? dossier/item-0022-workpapers/pintz10-2-16-recheck.py
?? dossier/item-0022-workpapers/pintz10-2-16-recheck.txt
?? dossier/item-0022-workpapers/pintz10-source-defects.md
?? item-0033-phase2d-dispatch-v1.md
```

The first three are a steering workpaper of 2026-07-26 on the pintz10
anchor and its reproduction script; the fourth is this pass's own
ephemeral dispatch. This pass neither edits, hashes, commits nor relies
on any of them. `pintz10-source-defects.md` was read after the pintz10
grade below was formed, and changed nothing in it.

---

## Section 1 -- rendering convention for the exhibitions

Every exhibition below is the `pdftotext` rendering of the anchored PDF
at the cited page, ASCII-folded, because the gate requires this record to
be ASCII-only and because ANN-78's own failure included two non-ASCII
characters passed inside a quotation. Folding used, and nothing else:

```
nu mu sigma phi eps gamma delta lambda rho psi pi theta Delta Omega
<=  >=  <<  ~ (for the tilde-sim)  =~ (for asymp)  !=  ->  infinity
in  subset  union  empty  prod  sum  |  ndiv (for "does not divide")
Fraktur S -> S     en/em dash -> hyphen     curly quotes -> straight
```

Where a rendering artifact of the anchor's own font encoding matters,
it is named at the point of use rather than folded silently.

Exhibitions are minimal-span: the quoted span and a few words of
context, no more of the source than the bounded extract already quotes.

---

## Section 2 -- gates at start of pass

All ran clean, from the repo root:

```
blocks.py check-frozen ......... FROZEN BLOCKS: all byte-identical (3 blocks)
blocks.py relocation-check ..... PASSED, concatenation byte-identical to old body
sorry scan ..................... lean/Erdos251/Statement.lean:21 (the baseline
                                 top-level statement sorry; unchanged, tracked)
lake-manifest rev count ........ 1
lean-toolchain last byte ....... \n
roadmap.py show item-0033 ...... status: ratified
writeup_mapper.py check ........ PASS
mathjax_lint.py ................ 138 file(s) checked, 0 problem(s)
extract/ non-ASCII counts ...... 0 0 0 0 0
HANDOVER.md non-ASCII .......... 0
git status --porcelain ......... the four untracked files of Section 0
```

---

## Section 3 -- axis 3.2, the robust dropped-object scan

Run from the repo root with line breaks flattened, so a reference split
across a line break cannot hide:

```
== dossier/item-0022-workpapers/extract/bloomkuperberg23-oddmoments.md
  (none)
== dossier/item-0022-workpapers/extract/kowalski-singser-dist.md
this session
== dossier/item-0022-workpapers/extract/kuperberg21-oddmoments.md
  (none)
== dossier/item-0022-workpapers/extract/kuperberg23-apsmooth.md
  (none)
== dossier/item-0022-workpapers/extract/pintz10-patterns.md
  (none)
```

**Outcome: the survivors are re-established clean of dropped objects.**
No `report N`, no `appendix c.N`, none of the header residues
(`kickoff`, `operator-held`, `operator-verified`, `re-verified this
session`, `against the dispatch`) on any of the five. The single hit is
kowalski's `this session`, which is item 3.4(a) and is adjudicated in
Section 9. This does not rest on the residual apply's word; it is an
independent re-establishment.

---

## Section 4 -- axis 3.3, in-tree path-liveness

Every in-tree cross-reference the five extracts make, checked to resolve
at HEAD. ANN-78 passed I4 without this check.

| extract | reference | resolves at HEAD |
| --- | --- | --- |
| all five | `dossier/item-0022-workpapers/extract-grades-r1.md` | YES, file present |
| bloomkuperberg | `/home/istr/pro/erdos251/dossier/2312.09021v2.pdf` | YES, sha256 matches |
| bloomkuperberg | `2301.06095v1` reference 4, p.19 | YES, `dossier/2301.06095v1.pdf` present; ref 4 read at p.19 |
| kowalski | `/home/istr/pro/erdos251/dossier/singular-series-distribution.pdf` | YES, sha256 matches |
| kowalski | `payloads/HASHES.txt` line 83 | YES, line 83 is exactly the ETH Zurich URL for this anchor |
| kowalski | `kowalski-mu-recheck.py` / `.txt` | YES, both present in this directory |
| kuperberg21 | `/home/istr/pro/erdos251/dossier/2109.03767v3.pdf` | YES, sha256 matches |
| kuperberg21 | `2301.06095v1` reference 4, p.19 | YES, as above |
| kuperberg23 | `/home/istr/pro/erdos251/dossier/2301.06095v1.pdf` | YES, sha256 matches |
| kuperberg23 | "the anchored arXiv:2210.09775v2" | YES, `dossier/2210.09775v2.pdf` present and booked at `payloads/HASHES.txt` line 21 |
| pintz10 | `/home/istr/pro/erdos251/dossier/1004.1072v1.pdf` | YES, sha256 matches |
| pintz10 | `AGENTS.md` | YES, file present |

**Outcome: no dangling in-tree reference on any of the five.** The
stale `roadmap/item-0022.md` reference the dispatch names is absent
from the tree as it stands; no successor to it was found. This axis
bounces nothing.

---

## Section 5 -- `bloomkuperberg23-oddmoments.md` -- CLEAN

Anchor `dossier/2312.09021v2.pdf`, sha256 `46b80c...7ec5f`, 38 pages.
Metadata checked against `pdfinfo`: Creator `arXiv GenPDF
(tex2pdf:a6404ea)`, Producer `pikepdf 8.15.1`, Author field `Thomas F.
Bloom; Vivian Kuperberg`, no journal reference printed. All as the
extract records.

**H1 -- the reference [17] entry, p.37.** The extract quotes it as the
anchor's own corresponding entry for the companion work.

```
p.37, References:
  [17] V. Kuperberg. Odd moments in the distribution of primes, Algebra Number
      Theory 19 (2025), no. 4, 617-666.
```

PASS. The page is p.37, not p.38; p.38 carries only [21] and [22]. This
corrects the ANN-78 grade prose and is booked in Section 10.

**H2 -- the string not printed in this anchor.** The extract says the
`arXiv:2109.03767, 2021` form is not printed here. A whole-document
search of the text layer for `2109.03767` returns nothing. PASS.

**H3 -- the companion string at `2301.06095v1`, p.19.**

```
2301.06095v1, p.19, References:
  4. V. Kuperberg, Odd moments in the distribution of primes, arXiv:2109.03767,
     2021.
```

PASS, character for character.

**Q1 -- front matter, p.1.**

```
p.1:
  ODD MOMENTS AND ADDING FRACTIONS
  THOMAS F. BLOOM AND VIVIAN KUPERBERG
  Abstract. We prove near-optimal upper bounds for the odd moments
  of the distribution of coprime residues in short intervals, confirming a
  conjecture of Montgomery and Vaughan. As an application, we prove
  near-optimal upper bounds for the average of the refined singular series
  in the Hardy-Littlewood conjectures concerning the number of prime
  k-tuples for k odd. The main new ingredient is a near-optimal upper
  bound for the number of solutions to sum_{1<=i<=k} a_i/q_i in Z when k is odd,
  with gcd(a_i, q_i) = 1 and restrictions on the size of the numerators and
  denominators, which is of independent interest.
```

PASS. The extract's transcription is word-for-word, with the display
inside the abstract set as inline math and the em-dash-free text
unchanged.

**Q2 and D1 -- Theorem 2 and its display, p.4.**

```
p.4:
  Theorem 2. If k >= 3 is an odd integer and h >= 2 then
                     R_k(h) << (log h)^{O(1)} h^{(k-1)/2}.
     As with Theorem 1, and in keeping with the previous conjecture for the
  growth of R_k(h), we believe (but cannot prove) that this upper bound is
  essentially the best possible, up to the exponent of log h.
```

PASS. The quotation is exact, the display matches, the theorem number
and the page are right, and the two sentences are contiguous in the
source as the extract presents them.

**Q3 -- the implied-constant footnote, p.1.**

```
p.1, footnote 1:
  ... All implied constants depend (only, yet substantially) on k.
```

PASS. The extract quotes the clause exactly and uses it, correctly, as
the paper's own scope declaration for Theorem 2's implied constant.

**Q4 and D2 -- the even-k asymptotic attributed to [19], p.4.**

```
p.4:
  When k is even Montgomery and Soundararajan [19] proved an asymptotic
  for R_k(h) of the shape
                          R_k(h) ~ mu_k(-h log h)^{k/2}
```

PASS. The display matches, the attribution to [19] matches, and the
extract's NOT-FOUND probe is correspondingly narrowed to "it is not this
paper's own result" rather than "not present" -- which is the correct
narrowing.

**N1 -- "NOT proved in this paper: any even-order result of its own for
the refined singular series."** Checked, not inherited. The only even-k
statements about $`R_k(h)`$ in the document are the attribution to
[19] on p.4; the Section 3.3 formulae on p.30, which the paper itself
frames as expectations ("We expect ...", "(conjecturally) independent of
q") and which explicitly say "For k even, an asymptotic for R_k(h) has
already been given in [19]"; and Section 4.2 on p.35, which is an open
problem ("Surprisingly, the methods of this paper do not appear to help
with the lower order terms for even moments"). No even-order result of
its own. PASS, and the negative is no broader than the anchor supports.

**N2 -- "NOT present in this paper: any uncentered second moment
$`\sum\mathfrak{S}(H)^2`$."** The paper's objects are $`M_k(q,h)`$
(central moments of coprime residues) and $`R_k(h)`$, which is built
from the refined $`\mathfrak{S}_0(D;q)`$ at (17)/(18) on p.26. A
whole-document search finds no sum of a squared singular series and no
occurrence of "second moment" or "uncentered". PASS.

**S1 -- the scope statement.** Theorem 1 at p.2, Theorem 2 at p.4,
Theorem 3 at p.4, all confirmed at those pages. Theorem 1 is about
$`M_k(q,h)`$; Theorem 3 is the rational-linear-equation counting
bound. The extract's "three objects, not one" is right and its two
probes are correctly scoped to the singular-series object. PASS.

**Grade: CLEAN.** Every display, every theorem number, every page
citation, every quotation and both negatives check out against the
anchor. Two non-blocking observations are recorded in Section 12.

---

## Section 6 -- `kowalski-singser-dist.md` -- CLEAN

Anchor `dossier/singular-series-distribution.pdf`, sha256
`378433...7920`, 30 pages. Metadata checked: Creator `TeX`, Producer
`pdfTeX-1.40.19`, CreationDate `Sun Jun 16 16:09:41 2019 CEST`. No arXiv
identifier, no journal reference, no printed date in the text -- p.1
carries only the MSC line and the keywords. All as the extract records.

**H1 -- the page-numbering claim.** The extract states that PDF page
numbering matches the paper's printed page numbers 1-30 exactly, and
says it verified pages 1, 20 and 21. This pass checked **all thirty**:
PDF page N carries printed page number N for every N from 1 to 30, the
running heads alternating title and author as expected. PASS, and
stronger than the extract's own claim.

**H2 -- `payloads/HASHES.txt` line 83.** Line 83 is exactly
`378433db...b27920  https://people.math.ethz.ch/~kowalski/singular-series-distribution.pdf`.
PASS.

**Q1 -- front matter, p.1.**

```
p.1:
  AVERAGES OF EULER PRODUCTS, DISTRIBUTION OF
  SINGULAR SERIES AND THE UBIQUITY OF POISSON
  DISTRIBUTION
  EMMANUEL KOWALSKI
  Abstract. We discuss in some detail the general problem of computing aver-
  ages of convergent Euler products, and apply this to examples arising from sin-
  gular series for the k-tuple conjecture and more general problems of polynomial
  representation of primes. We show that the "singular series" for the k-tuple
  conjecture have a limiting distribution when taken over k-tuples with (distinct)
  entries of growing size. We also give conditional arguments that would imply
  that the number of twin primes (or more general polynomial prime patterns)
  in suitable short intervals are asymptotically Poisson distributed.
```

PASS, word for word.

**Q2 -- affiliation, last page (p.30).**

```
p.30:
  ETH Zurich - D-MATH, Ramistrasse 101, 8092 Zurich, Switzerland
  Email address: kowalski@math.ethz.ch
```

PASS. The source line is set in small capitals, which the extract
renders as capitals; the umlauts are ASCII-folded per the extract's own
stated convention. Nothing else differs.

**Q3 and D1 -- the singular series (1.1), p.2.**

```
p.2:
     The singular series associated with h is defined as the Euler product
  (1.1)  S(h) = prod_p (1 - nu_p(h)/p)(1 - 1/p)^{-k}
              = prod_p (1 - (nu_p(h) - 1)/(p-1))(1 - 1/p)^{1-k}
  which is absolutely convergent (as will be checked again later; here and
  throughout the paper, as usual, p is restricted to prime numbers).
```

PASS. Both halves of the display match term for term, the equation
number and page are right, and the quoted words are contiguous and
verbatim. The extract closes the quotation at "which is absolutely
convergent." with a terminal period where the source continues into a
parenthetical -- ordinary truncation of a bounded quotation, no word
altered, no meaning changed. Recorded in Section 12, not a blocker.

**Q4 and D2 -- Theorem 1.1 and the sentence that follows it, p.3.**

```
p.3:
  Theorem 1.1. Let k >= 1 be fixed. For any complex number m in C with Re(m) >= 0,
  there exists a complex number mu_k(m) such that
                     lim_{h->+infinity} (1/h^k) sum*_{|h|<=h} S(h)^m = mu_k(m).
    Moreover, for m, k >= 1 both integers, we have the symmetry property
  (1.6)              mu_k(m) = mu_m(k) ;
  in addition, we have mu_1(m) = 1 for all integers m >= 1, and hence mu_k(1) = 1 for
  all k >= 1.
     The last statement (mu_k(1) = 1) is of course Gallagher's theorem (1.5); our proof
  is not intrinsically different, but maybe more enlightening.
```

PASS. Both displays match, and the closing paragraph is genuinely
contiguous with the theorem in the source, as the extract presents it.

**Q5 and D3 -- Gallagher (1.5), p.3.**

```
p.3:
     A result of Gallagher [Ga] states that
  (1.5)              lim_{h->+infinity} (1/h^k) sum*_{|h|<=h} S(h) = 1,
  for any fixed k, as h -> +infinity, where |h| = max h_i and sum* restricts to
  k-tuples with distinct components.
```

PASS.

**Q6 and D4 -- Example 3.5, p.15.**

```
p.15:
  Example 3.5. Let m = 2. We find (using the symmetry property) that the mean-
  square of S(h) is given by
                     lim_{h->+infinity} (1/h^k) sum*_{|h|<=h} S(h)^2 = mu_k(2),
  where
    mu_k(2) = prod_p ((1 - 1/p)(1 - 2/p)^k + (1/p)(1 - 1/p)^k)(1 - 1/p)^{-2k}.
    In particular, we find (using Pari/GP for instance):
                     mu_2(2) = 2.300...      mu_3(2) = 6.03294...
                     mu_4(2) = 17.562...     mu_5(2) = 55.255...
                                 mu_6(2) = 184.18...
     Note that the second (and higher) moments increase quickly with k (as proved
  in Proposition 4.1 in the next section). This is explained intuitively by the fact
  that S(h) is often zero: for instance, the 2-factor of S(h) is zero unless all h_i are
  of the same parity, which happens with probability 2^{1-k} only (see Example 4.3 for
  a more precise estimate). For those, of course, the 2-factor is very large (equal to
  2^{k-1}).
```

PASS. The Euler product matches factor for factor -- including that the
$`(1-1/p)^{-2k}`$ sits outside the bracket -- and all five numerical
values match digit for digit.

**Q7 -- Proposition 4.1, p.15.**

```
p.15:
  Proposition 4.1. For any fixed k >= 1, we have
              log mu_k(m) = km log log 3m + O(m),   for m >= 1,
  where the implied constant depends on k.
```

PASS. The extract sets the quantifier as `m >= 1` inside the display
where the source prints `for m >= 1`; the constraint and its scope are
unchanged.

**Q8 -- Example 4.3, p.18.**

```
p.18:
  Example 4.3. As a corollary of Proposition 4.1 and symmetry, we have
                     log mu_k(2) = 2k log log 3k + O(k)
  for k >= 1.
```

PASS.

**Q9 -- the [MS] citation, p.3.**

```
p.3:
  This property was used by Gallagher himself to understand
  the behavior of primes in short intervals (see also the recent work by Montgomery
  and Soundararajan [MS]),
```

PASS. A whole-document search for `[MS]` returns exactly two hits: this
one in the body at p.3, and the bibliography entry at p.30. The
extract's negative -- "the theorem itself is neither stated nor proved
here" -- is therefore exactly as broad as the anchor supports.

**M1 -- method anatomy.** Each structural claim checked at its page:
Proposition 2.1 and the $`\prod_p(1+X_p)`$ versus independent-model
$`\prod_p(1+Y_p)`$ framework are on p.6; $`X_p(h)=a(p,\nu_p(h))`$
and $`Y_p=a(p,\rho_p)`$ on $`\Omega_2`$ are set at pp.10-12; (3.10)
is the closed form
$`\mu_k(m)=\prod_p(1-1/p)^{-km}\mathbf{E}_2((1-\rho_p/p)^m)`$, quoted
back in that form by the paper itself at p.15; Section 4 splits the
product at $`p<km`$ and $`p\ge km`$ on pp.16-17; Theorem 1.3
(p.4-5, proved in Section 5) is explicitly conditional -- "Assume that
the Bateman-Horn conjecture holds uniformly for all primitive families
with non-zero singular series" -- and Proposition 2.1 is invoked in its
proof at p.19. PASS on every point.

**N1 -- the growing-k negative.** Example 4.3 gives
$`\log{}\mu_k(2)=2k\log{}\log{}3k+O(k)`$, so $`\mu_k(2)`$ grows like
$`\exp(2k\log{}\log{}3k)`$, faster than any fixed exponential in k.
The extract's "Proposition 4.1 and Example 4.3 show the opposite" is
correct. PASS.

**N2 -- the 1.1504807723 ratio, correctly disclaimed.** The extract says
this value is NOT printed in the anchor and is the project's own
derivation from $`\mu_2(1)=1`$ and $`\mu_2(2)`$. Confirmed: no such
figure appears anywhere in the anchor. The disclaimed derivation is
arithmetically sound -- conditioning on the non-vanishing event of
probability $`q=2^{1-k}=1/2`$ at k=2 multiplies both moments by 2, so
the ratio is $`2\mu_2(2)/2^2=\mu_2(2)/2`$, and
$`\mu_2(2)=2.3009615447\ldots`$ gives $`1.1504807723\ldots`$. The
in-tree reproduction `kowalski-mu-recheck.txt` reports
`1.15048077235661` and reproduces all five of Example 3.5's printed
values. PASS: the extract asserts no fidelity it does not exhibit, and
the attribution to the project rather than to Kowalski is correct.

**A1 -- the `this session` deictic.** Adjudicated in Section 9. Not a
blocker.

**Grade: CLEAN.**

---

## Section 7 -- `kuperberg21-oddmoments.md` -- CLEAN

Anchor `dossier/2109.03767v3.pdf`, sha256 `e1bbab...41f94`, 51 pages.
Metadata checked: Creator `LaTeX with hyperref`, Producer
`pdfTeX-1.40.25`, CreationDate `Wed Jul 31 02:11:45 2024 CEST`. No
journal reference printed. All as the extract records.

**Encoding note, named rather than folded silently.** This anchor's text
layer uses a Type 1 encoding under which `pdftotext` renders several math
glyphs as letters and accents: `(` and `)` come out as `p` and `q`, `=`
as a left double quote, `+` as a grave accent, minus as an acute accent,
the summation and product signs as accented Latin letters, and the
relations "less-or-equal", "greater-or-equal", "much-less-than" and
"asymptotic-to" as an accented `d`, an accented `e`, an exclamation mark
and an em dash respectively. Every exhibition below is given decoded, and
the decoding was checked against the rendered display rather than
assumed.

**H1 -- the sidebar identification, p.1.** `arXiv:2109.03767v3
[math.NT] 29 Jul 2024`, exactly as the extract records. 51 pages
confirmed. PASS.

**H2 -- the companion string at `2301.06095v1`, p.19.** Same reference 4
exhibited in Section 5 (H3). PASS.

**H3 -- "whose own bibliography carries no entry for it."** The
bibliography runs pp.50-51, entries 1 through 15. No self-entry, and no
entry for "Odd moments in the distribution of primes". PASS.

**Q1 -- front matter, p.1.**

```
p.1 (decoded):
  ODD MOMENTS IN THE DISTRIBUTION OF PRIMES
  VIVIAN KUPERBERG
  Abstract. Montgomery and Soundararajan showed that the distribution of psi(x + H) -
  psi(x), for 0 <= x <= N, is approximately normal with mean ~ H and variance ~ H log(N/H),
  when N^delta <= H <= N^{1-delta}. Their work depends on showing that sums R_k(h) of k-term
  singular series are mu_k(-h log h + Ah)^{k/2} + O_k(h^{k/2-1/(7k)+eps}), where A is a
  constant and mu_k are the Gaussian moment constants. We study lower-order terms in the
  size of these moments. We conjecture that when k is odd, R_k(h) =~ h^{(k-1)/2}(log h)^{(k+1)/2}.
  We prove an upper bound with the correct power of h when k = 3, and prove analogous upper
  bounds in the function field setting when k = 3 and k = 5. We provide further evidence for
  this conjecture in the form of numerical computations.
```

PASS, word for word against the extract's transcription.

**Q2 and D1 -- equation (4) and its lead-in, p.3.**

```
p.3 (decoded):
  showing that for any nonnegative integer k, for any h > 1, and for any eps > 0,
  (4)        R_k(h) = mu_k(-h log h + Ah)^{k/2} + O_k(h^{k/2-1/(7k)+eps}),
  where A = 2 - gamma - log 2pi. Their estimate on R_k(h) implies their bound on the moments.
```

PASS. The extract's framing -- that the anchor restates the
Montgomery-Soundararajan estimate in its own introduction as the result
it builds on -- matches the role (4) actually plays on p.3, where it is
introduced by "Montgomery and Soundararajan considered the sum (3)".

**Q3 and D2 -- Conjecture 1.1, p.3.**

```
p.3 (decoded):
  Conjecture 1.1. Let k >= 3 be an odd integer, and let h > 1. With R_k(h) defined as above,
                     R_k(h) =~ h^{(k-1)/2}(log h)^{(k+1)/2}.
    The conjectured power of log h here comes from numerical evidence, which we present in
  Section 5.
```

PASS. The two sentences are contiguous in the source as presented.

**Q4 and D3 -- Theorem 1.2, p.3.**

```
p.3 (decoded):
  Theorem 1.2. For h >= 4 and R_3 defined in (3),
                     R_3(h) << h(log h)^5.
```

PASS.

**Q5 -- the "we do not know" sentence, p.3.**

```
p.3 (decoded):
  For k odd, we do not know, even heuristically, which terms contribute to the main
  term in R_k(h); for this reason, we do not know what the constant should be in front of the
  asymptotic in Conjecture 1.1.
```

PASS, and it sits at p.3 as cited.

**U1 -- the uniformity ledger.** Correct, and correctly labelled. The
extract states plainly that "no asymptotic for $`R_k(h)`$ at odd k is
proved here -- only an upper bound, and only the conjectured power of h
(not of log h) at k=3 -- is an inference from Theorem 1.2 and Conjecture
1.1 as printed, not a statement the paper makes in those words." That
is the right classification: Conjecture 1.1 asks for
$`h(\log{}h)^{2}`$ at k=3 while Theorem 1.2 delivers
$`h(\log{}h)^{5}`$, so the power of h matches and the power of
$`\log{}h`$ does not. Nothing is strengthened. PASS.

**N1 -- the NOT-FOUND probe.** "flanked", "aggregated simplex",
"uncentered" and "second moment" return nothing in a whole-document
search; the paper's objects are $`M_K(N;H)`$ and
$`R_k(h)=\sum\mathfrak{S}_0(D)`$, the centered form defined at (2) on
p.2, never an uncentered $`\sum\mathfrak{S}(H)^2`$. PASS.

**Grade: CLEAN.**

---

## Section 8 -- `kuperberg23-apsmooth.md` -- BOUNCED

Anchor `dossier/2301.06095v1.pdf`, sha256 `c67fdd...f9617`, 19 pages.
Metadata and front matter check out; the abstract on p.1, Theorem 1.1
and its display on p.3, the definition of $`\mathcal{B}_k`$ at (8) on
p.3, the "In particular" clause of Theorem 1.2 on p.4, the uniformity
ledger and the whole of the NOT-FOUND probe all PASS -- see the
exhibitions below. The extract bounces on one sentence.

**Q1 and D1 -- Theorem 1.1, p.3.** PASS.

```
p.3:
  Theorem 1.1. Fix a modulus r >= 1, an integer k >= 1, and k congruence classes c_1, ..., c_k
  modulo r. Define B_k as in (8). Let q >= 1 be a squarefree integer with (r, q) = 1, and define
  V_k(q, h; r, c_1, ..., c_k) as in (6). For h >= 3,
     V_k(q,h;r,c_1,...,c_k) = sum_{sigma in B_k} prod_{(i,j) in sigma} V_2(q,h;r,c_i,c_j)
                              + O_{r,k}( h^{k/2-1/(7k)} (q/phi(q))^{2^k + k/2} ).
```

**Q2 -- the definition of $`\mathcal{B}_k`$, p.3.** PASS.

```
p.3:
  Let B_k denote the set of perfect matchings of [1, k], so that ...
```

**Q3 and D2 -- Theorem 1.2's "In particular" clause, p.4.** PASS.

```
p.4:
    In particular, if #B~(c_1, ..., c_k) is the number of ways to pair the c_i's such that every pair
  has equal values, then
     R_k(h; r, c_1, ..., c_k) = #B~(c_1,...,c_k) ( -h (phi(r)/r) log h + C_0(r)h )^{k/2}
                                + O_{r,k}( h^{k/2}(log h)^{k/2-1} ).
```

**N1 -- the NOT-FOUND probe and the theorem list.** PASS. Theorem 1.1 is
at p.3, Theorem 1.2 at p.4, Theorem 1.3 at p.5 and Theorem 1.5 at p.5,
all confirmed at those pages; the paper states no Theorem 1.4 (see
Section 9(b)); and all four are asymptotic formulae for sums of the
singular-series constant or its restricted and weighted variants, never
a lower bound for a prime-tuple counting function. The only further
numbered statements in the paper are Theorem 2.1, Lemmas 3.1, 3.2, 1.4
and 5.1-5.3, all internal machinery of the same kind.

**FINDING F1 -- the description of display (9) is wrong. CLEAN-BLOCKER.**

The extract, at lines 55-58, describes Theorem 1.2 as follows:

> p.4, Theorem 1.2 (the corresponding asymptotic for
> $`R_k(h;r,c_1,\ldots,c_k)`$) sums over partitions of $`[1,k]`$
> into doubleton and singleton blocks, with **the doubleton part** again
> organized by perfect matchings
> $`\sigma \in \mathcal{B}(j+1,\ldots,k-j)`$ of the remaining indices
> (eq. (9)).

The source at p.4:

```
p.4, display (9), summation conditions:
  0 <= j <= k/2
  P refines {C_l}, P = {S_1, ..., S_{k-j}}
      |S_m| = 2  for all 1 <= m <= j
      |S_m| = 1  for all j < m <= k-j
  ... ( (h/r) sum_{d|Q, d>1} mu(d)^2/phi(d) )^j
  ... sum_{sigma in B(j+1,...,k-j)} prod_{(i1,i2) in sigma} V_2(Q,h;r,c(S_{i1}), c(S_{i2}))
```

The partition has j doubleton blocks, indexed 1 through j, and k-2j
singleton blocks, indexed j+1 through k-j. The matching
$`\sigma\in\mathcal{B}(j+1,\ldots,k-j)`$ ranges over the index set
$`\lbrace j+1,\ldots,k-j\rbrace`$ -- that is, it pairs the SINGLETON
blocks, not the doubleton blocks. The doubleton blocks are accounted for
by the separate $`j`$-th power factor. The extract binds "the
doubleton part" to what $`\sigma`$ organizes, and $`\sigma`$
organizes singletons.

The anchor confirms this independently at its own smooth-weight analogue
(16), p.6, whose closing clause reads:

```
p.6, after display (16):
  where the sum is taken over partitions of [1, k] where each part has either 1 or 2
  elements, and for |S_m| = 1, f_{S_m} denotes f_j where j in S_m.
```

The pairing argument $`f_{S_{i_1}}`$ is defined only for singleton
blocks. The reading is not ambiguous.

This is a false statement about the structure of a display block, on the
ANN-78 surface ("every display block ... checked against the PDF at the
location"). It bounces.

**Grade: BOUNCED.** Repair spec in Section 11.

---

## Section 9 -- `pintz10-patterns.md` -- BOUNCED

Anchor `dossier/1004.1072v1.pdf`, sha256 `748240...22053b`, 9 pages.
Metadata and front matter check out. Most of the extract PASSES,
including the parts the project actually leans on; it bounces on its
Method anatomy section, with two further defects recorded.

**Q1 and D1 -- Lemma 2, its display (2.10), and the two Remarks, p.6.**
PASS on content.

```
p.6:
  Lemma 2. For fixed nu r and H > H_0(nu, r) we have
  (2.10)   S(nu, r) = sum_{D subset [1,H]} S^2(D^+) <= c_8(nu, r) H^nu.
  Remark. The condition H > H_0(nu, r) and H > H_0(nu) is naturally not
  necessary if we do not care about the values of the constants c_7(nu) and
  c_8(nu, r).
  Remark. In case of r = 1 we will additionally show, similarly to (2.9),
  S(nu, r) ~ H^nu as H -> infinity. This slightly modified form implies easily the
  original Gallagher's theorem too, by dividing all possible nu + 1-tuples ac-
  cording to the smallest element of it and using that S(H) is invariant under
  translation.
```

The missing comma in "For fixed nu r" is in the source, exactly as the
extract's own print-slip note says. The display carries exponent 2 and
no cardinality condition under the summation sign, both confirmed. The
three quoted blocks are contiguous in the source, as presented.

**Q2 -- the proof close, p.8.** PASS.

```
p.8:
     (2.14)-(2.16) together prove the lemma, while for r = 1, in order to
  obtain ~ instead of <<, it is enough to observe that the numerator after the
  product sign equals exactly 1 for each prime p, and the contribution of the
  incomplete period, the interval [RP + 1, RP + r], is <= P = 0(H) by the
  prime number theorem, since y = log H/2.
```

The digit-zero claim is CONFIRMED, and by a stronger instrument than the
extract's 200-dpi render: `pdftotext` reads the character stream from the
font encoding, and it renders this glyph as the digit `0` while
rendering the neighbouring `= O(1)` at the top of the same page as the
letter `O`. The same holds at p.7 for "<< or 0 symbols" against
"1 + O(1/p^2)" in (2.14). Both PASS.

**Q3 and D2 -- Lemma 1 and (2.8), p.6.** Content PASSES; see F3 for the
elision.

```
p.6:
  Lemma 1. For fixed nu and any H > H_0(nu) we have
  (2.8)   sum_{D subset [1,H], |D|=nu} S^2(D^+) <= c_7(nu)H^nu.
  Remark. The parameter H can be arbitrary here, not just that given in
  (2.2).
  Remark. The above lemma is somewhat analogous to Gallagher's theorem
  (2.9)   sum_{D subset [1,H], |D|=nu} S(D) ~ H^nu,
  the difference being the non-essential appearance of D^+ = D union {0} in place
  of D and the more essential change in the exponent: two instead of one.
```

(2.8) carries `|D|=nu` on its own second summation line, and (2.10) does
not -- the asymmetry the extract's Section 6 turns on. Both confirmed.

**Q4 and D3 -- (2.11) and its surrounding prose, pp.6-7.** PASS.

```
p.6 (last paragraph) into p.7:
  Proof of Lemma 2. We will prove in fact a little bit more. Namely, the fact
  that extending every concrete admissible D union {0} of size t + 1 >= 1 with
  just one element running over [1, H] the square of the singular series will be
  larger at most by a factor depending on t. In such a way, (2.10) follows by
  induction from
  (2.11)  S*(t, r, D) := sum_{1<=h<=H, h not in D} ( S(D^+ union {h}) / S(D^+) )^r << H
  where D^+ is any admissible set of size t + 1 and, as in the following, we will
  not mark the dependence of the constants implied by << or 0 symbols on t
  and r.
```

The extract's page citation "p.6-7" is correct here: the passage does
straddle the break.

**Q5 and D4 -- (2.12) through (2.16), pp.7-8.** PASS.

```
p.7:
  (2.12)  nu_p' = nu_p(D^+ union {h}), nu_p = nu_p(D^+), y = log H / 2,
          P = prod_{p<=y} p, Delta := prod_{i=1}^{nu} (h - d_i).
  (2.13)  S(D^+ union {h}) / S(D^+) = prod_1 . prod_2 . prod_3   [over p<=y; p>y,p|Delta; p>y,p ndiv Delta]
  (2.14)  prod_3 = prod_{p>y} (1 + O(1/p^2)) = 1 + O(1/y)
  (2.15)  log prod_2 << ... << 1/log y
     If H = RP + r, 0 <= r < P then prod_1(h) is periodic with period P. ...
     Consequently
  (2.16)  (1/P) sum_{h=1}^{P} prod_1(h)
            = prod_{p|P} { nu_p/p (1 - nu_p/p)^r + (1 - nu_p/p)(1 - (nu_p+1)/p)^r }
                         / ( (1 - nu_p/p)^r (1 - 1/p)^r )
            = prod_{p|P} ( nu_p/p + 1 - nu_p/p - r(nu_p+1)/p + O(1/p^2) )
                         / ( 1 - r(nu_p+1)/p + O(1/p^2) )
p.8 (top):
            = prod_{p|P} (1 + O(1/p^2)) = O(1).
```

Every claim the extract makes about this passage checks out: the
exponent r stands on both $`(1-\nu_p/p)`$ and
$`(1-(\nu_p+1)/p)`$ at every $`p\mid P`$; the middle numerator does
leave $`\nu_p/p`$ and $`-\nu_p/p`$ uncancelled in the source, and
the extract correctly labels the cancellation as its own step and not
the source's; and the last two equalities of (2.16) are indeed printed
at the top of p.8. The prose ellipsis the extract marks with `...` is a
real elision, correctly marked.

**M1 -- the Section 2 reduction.** PASS. Section 2 does reduce via
Selberg's sieve at (2.1), Cauchy's inequality at (2.7), and Lemma 1 /
Lemma 2's bound on $`\sum\mathfrak{S}^2(D^+)`$, exactly as described.

**U1 -- the uniformity ledger and N1 -- the NOT-FOUND probe.** PASS.
$`c_7(\nu)`$ depends on $`\nu`$ alone, $`c_8(\nu,r)`$ on both, the
thresholds are as printed, the paper's own Remark says the thresholds
are an artifact of not tracking constants, and nothing in the nine pages
gives a bound uniform in $`\nu`$. The revised probe entry, which
records that a general-r moment bound IS established by the proof and
that this was wrongly recorded as NOT-FOUND earlier, is correctly
sourced to Section 2.3's induction and Section 6, and is labelled as
such.

**C1 -- Section 6 COMMENTARY.** PASS as commentary. It is explicitly
labelled "assessment, not extraction", it re-confirms the literal
transcription of (2.10) as accurate, and it separates the printed
display from the reading it argues for. Nothing in it is presented as
the source's own words.

**FINDING F2 -- the paper's main theorem is misidentified. CLEAN-BLOCKER.**

The extract's Section 3 (Method anatomy) opens:

> Section 1 states **the main theorem**: under a distribution-level
> hypothesis $`\vartheta>1/2`$ on the primes, there is a bounded even
> $`d\le C_1(\vartheta)`$ such that the set of primes p with
> $`p,p+d`$ both prime contains arbitrarily long arithmetic
> progressions (building on Green-Tao and Goldston-Pintz-Yildirim).
> Section 2 proves **a quantitative strengthening**: ...

The content described is real and is stated in Section 1 -- but the
anchor attributes it to a different preprint of the same author, and it
is not this note's theorem:

```
p.2:
     The author showed recently that a combination of the two above results
  is possible, showing thereby new patterns of primes.
  Theorem [Pin]. If the primes have a distribution level theta > 1/2 then there
  exists a positive even d <= C_1(theta) such that the set P(d) of primes p satisfying
  (1.3) contains arbitrarily long arithmetic progressions.
```

```
p.9, References:
  [Pin] J. Pintz, Are there arbitrarily long arithmetic progressions in the se-
       quence of twin primes? preprint, arxiv math.NT
```

This note's own main theorem is stated later in Section 1, at p.4, and
is unconditional:

```
p.4:
     The aim of this note is to show that the method of the mentioned work
  [GPY3] can be modified to yield for any fixed eta > 0 for N -> infinity many
  nu + 1-dimensional patterns of type (d_1, ..., d_nu) ...
     The exact formulation of our result to be proved is as follows.
  Theorem. Let eta > 0 be any positive constant, nu and m natural numbers.
  Then we have a positive constant c(eta, nu) depending on eta and nu such that
  for any N > N_0(eta, nu, m) we have a set D_{N nu} of nu-tuples (d_1, ..., d_nu) with
  0 < d_1 < ... < d_nu such that
  (1.17)  |D_{N nu}| >= c(eta, nu) log^nu N
  and every element of D_{N nu} satisfies (1.15) and (1.16).
```

```
p.5, section heading:
  2   Proof of the Theorem
```

So the extract calls a cited prior result of a companion preprint "the
main theorem" of this anchor, and calls the anchor's actual main theorem
"a quantitative strengthening" of it. The consequence is not cosmetic: a
reader of the extract takes away that 1004.1072v1's own result is
conditional on a distribution level $`\vartheta>1/2`$, when the
theorem it states and proves is unconditional and is about the density
of realizable difference tuples. This misstates the anchor's structure
and misclassifies the provenance and the conditionality of a result --
the classification discipline AGENTS.md requires an extract to preserve.
It bounces.

The second half of the sentence is separately checked and is accurate on
its own terms: Section 2 does prove that for any $`\eta>0`$ and
natural $`\nu,m`$ there is a set of $`\nu`$-tuples of size
$`\gg\log^\nu N`$ (1.17) each realizing $`\gg N^2/\log^m N`$
length-m arithmetic progressions (the Corollary, p.4).

**FINDING F3 -- an unmarked elision inside a quotation. Recorded in the
bounce spec.**

The extract's Section 2.2 presents Lemma 1 and the "somewhat analogous
to Gallagher's theorem" Remark as one continuous quotation. In the
source, exhibited at Q3 above, the Remark "The parameter H can be
arbitrary here, not just that given in (2.2)." stands between them. The
extract drops it silently, with no ellipsis -- in an extract that marks a
real elision with `...` two sections later, at (2.16). Every quoted word
is verbatim; what is not faithful is the presented adjacency.

**FINDING F4 -- an over-broad page citation. Recorded in the bounce spec.**

Section 2.1's lead-in reads "This is Lemma 2 and its r=1 remark, p.6-7".
The quoted block -- Lemma 2, its display, and both Remarks -- is
entirely on p.6. The section heading itself says "(p.6)" and is right.

**Grade: BOUNCED.** Repair spec in Section 11.

---

## Section 10 -- the two logged adjudications

### (a) kowalski `this session` -- DECIDED: it does NOT block CLEAN

The line, at `kowalski-singser-dist.md` L203-210, is in the FLAGS block:

> An earlier draft of this extract wrongly asserted that this PDF
> contained two concatenated documents (a ChatGPT-style transcript
> followed by the Kowalski paper). That was a mistake made while tracking
> page ranges across a large multi-document tool result in **this
> session**, not a property of the file. Corrected after directly
> re-reading PDF page 1, page 20, and page 21 in isolation: this file is
> Kowalski's own 30-page paper throughout, with PDF page numbers matching
> its printed page numbers 1-30 exactly.

**Decision: pass it, on the record, for three reasons.**

1. **The deixis is not load-bearing.** What the note has to deliver is
   the correction, and the correction is checkable without resolving
   "this session": this pass verified all thirty pages independently and
   confirms the file is Kowalski's 30-page paper throughout with printed
   numbers 1-30. The unresolvable phrase names only where the retracted
   error came from -- an item of the extraction's own dated history,
   which is exactly what a FLAGS log is for. Read as the extraction's
   own annotation of itself, "this session" resolves to the annotation's
   own authorship, and a FLAGS block is the one place in an extract where
   that reading is available.

2. **The same class of deixis stands, unremarked, in all five
   survivors.** Every one of the five carries the header line "fidelity
   repair applied per the ANN-78 grade (`extract-grades-r1.md`) **at this
   pin**; re-grade pending." "At this pin" names no commit and no later
   reader can resolve it either. A rule that bounces kowalski for an
   unresolvable deictic bounces all five, including the two this pass
   grades CLEAN on every other axis -- and it bounces them on a line
   ANN-78, the 2c repair and the 2c-residual apply all passed. This pass
   is not the place to introduce a corpus-wide rule by applying it to one
   file.

3. **It is not a dropped-object residual and the surrounding claim is
   true.** It attributes nothing to a dropped report, kickoff dispatch or
   operator-held object, and the sentence it sits in is accurate.

**Consequence booked, not acted on.** The deixis is real and worth
retiring. The right place is a repair apply that also has to touch the
same header line for a second reason -- see Section 12, O1: after this
apply lands, "re-grade pending" is stale on every survivor that has been
re-graded. Retiring both at once, in one repair pass, is cheaper and
safer than either alone, and neither is this pass's to perform.

### (b) the `Theorem 1.4` phrasing -- CONFIRMED, not a defect

`kuperberg23-apsmooth.md` states, inside its NOT-FOUND probe, "the paper
states no Theorem 1.4". This is literally true and is confirmed here so
that a later re-grader who greps `1.4` and finds a Lemma does not
misread the extract as wrong.

```
p.5:
  Lemma 1.4. Fix h >= 1 and let f_1, f_2 : R_{>=0} -> C be smooth functions with compact sup-
  ports supp(f_i) subset (0, infinity) such that |f^_i(xi)| << O(|xi|^{-2}). Define Q := prod_{p<=h^2} p, and define
  V_2(q, h; f_1, f_2) via (11). Then
  (14)  V_2(Q, h; f_1, f_2) = (-f^_1(0) f^_2(0) + {Mf}(2))h^2 - ({Mf}'(1)/2) h log h + O_{f_1,f_2}(h),
```

The numbering slot 1.4 in `2301.06095v1` is occupied by a **Lemma**, at
p.5, between Theorem 1.3 (p.5) and Theorem 1.5 (p.5). A whole-document
search of the text layer for the string `Theorem 1.4` returns zero hits;
the numbered statements in Section 1 are Theorems 1.1, 1.2, 1.3, 1.5 and
Lemma 1.4, and every later reference to the 1.4 object in the body
("In Section 5.2, we prove Lemma 1.4", "5.2. Proof of Lemma 1.4", "We
are now ready to prove Lemma 1.4") calls it a Lemma. **Not a defect; a
note that prevents a false one.** It is independent of the reason
kuperberg23 bounces.

---

## Section 11 -- verdicts, hashes and bounce specs

| extract | grade | one-clause reason |
| --- | --- | --- |
| `bloomkuperberg23-oddmoments.md` | **CLEAN** | every display, number, page citation, quotation and both negatives verified against `2312.09021v2` |
| `kowalski-singser-dist.md` | **CLEAN** | all nine quotations and four displays verified against `singular-series-distribution.pdf`; the `this session` deictic adjudicated as non-blocking |
| `kuperberg21-oddmoments.md` | **CLEAN** | all five quotations and three displays verified against `2109.03767v3` through its Type 1 encoding |
| `kuperberg23-apsmooth.md` | **BOUNCED** | the description of display (9) assigns the perfect matchings to the doubleton blocks; the anchor pairs the singleton blocks |
| `pintz10-patterns.md` | **BOUNCED** | Method anatomy presents the cited [Pin] conditional theorem as this anchor's main theorem, which is instead the unconditional p.4 Theorem |

**Hash lines added by this apply, to `payloads/HASHES.txt`:**

```
9125824e3517864026dbb98b453b498d9941cd86038bddf2d42722431ccd4d2c  dossier/item-0022-workpapers/extract/bloomkuperberg23-oddmoments.md
2177b8054b3c271ea682eb8c610d2e44c536abb9aa631c9e6d22f32a4e65f451  dossier/item-0022-workpapers/extract/kowalski-singser-dist.md
50beadb89264ea18a5faabe6f070c5f8950517304f36d0b812192ee0c1032c00  dossier/item-0022-workpapers/extract/kuperberg21-oddmoments.md
```

**No hash is added for either bounced extract, and NO HASH IS ADDED FOR
THIS RECORD.** The pass is not terminal, so a partial determination is
not frozen. The record's own hash, and the ANN-78 grade file's still
withheld hash, wait for the terminal re-grade.

### Repair spec -- `kuperberg23-apsmooth.md`

One-line spec: in the Theorem 1.2 sentence (lines 55-58), replace "with
the doubleton part again organized by perfect matchings" with the
singleton part -- $`\sigma\in\mathcal{B}(j+1,\ldots,k-j)`$ pairs the
$`k-2j`$ SINGLETON blocks $`S_{j+1},\ldots,S_{k-j}`$, while the
$`j`$ doubleton blocks are carried by the separate
$`\left(\frac{h}{r}\sum_{d\mid Q,\,d>1}\frac{\mu(d)^2}{\phi(d)}\right)^j`$
factor. Verify against p.4 display (9) and against the closing clause of
(16) on p.6. Nothing else in this extract needs to move.

### Repair spec -- `pintz10-patterns.md`

Three items, all in prose, none touching a display or a transcription:

1. Section 3, first sentence: the theorem quoted there is `Theorem
   [Pin]` at p.2, a cited prior preprint of the same author, not this
   note's main theorem. Re-point it -- this anchor's own Theorem is the
   unconditional one at p.4 proved in Section 2 ("2 Proof of the
   Theorem"), whose content the sentence's second half already states
   correctly. Do not carry the "quantitative strengthening" framing over
   unchanged; the p.4 Theorem is not a strengthening of [Pin]'s
   statement.
2. Section 2.2: mark the elision. The Remark "The parameter H can be
   arbitrary here, not just that given in (2.2)." stands between Lemma 1's
   display and the "somewhat analogous" Remark in the source; insert an
   ellipsis, or quote it, as Section 2.3 already does at (2.16).
3. Section 2.1, line 41: "p.6-7" for the Lemma 2 block should be "p.6".
   The section heading is already right.

After repair, both bounced extracts need a terminal re-grade before any
hash. This record's Sections 8 and 9 exhibit everything else in both
files as verified, so the terminal re-grade can be scoped to the repaired
spans plus a fresh robust scan and path-liveness check.

---

## Section 12 -- observations, none of them blockers

Recorded so a later pass does not have to rediscover them, and so that
the reasoning that kept them out of the bounce list is on the record.

- **O1 -- "re-grade pending" goes stale when this apply lands.** All five
  survivors carry the header line "fidelity repair applied per the ANN-78
  grade (`extract-grades-r1.md`) at this pin; re-grade pending." At HEAD
  that line is true. Once this apply lands it is false for the three that
  graded CLEAN and were hashed. This pass cannot fix it -- editing a
  survivor is an S7 -- so it is booked for the repair apply, together with
  the "at this pin" deixis of Section 10(a). Both live on the same line.
- **O2 -- bloomkuperberg's FLAGS over-reaches by one clause.** It ends
  "Everything recorded above is established against this anchor
  directly." One header sentence is not: the `2301.06095v1` reference 4
  string is established against a different anchor. Not a blocker,
  because that sentence names its own evidence base explicitly and
  correctly on the same page, so no reader is misled about provenance;
  kuperberg21 carries the same header sentence and its FLAGS makes no
  such claim. Worth tightening in any future repair.
- **O3 -- bloomkuperberg does not record the anchor's printed date.** The
  p.1 sidebar reads `arXiv:2312.09021v2 [math.NT] 12 May 2026`; the
  extract records only the identifier-derived December 2023 submission
  date. Nothing false is asserted, but the other four extracts do print
  the anchor's own date line.
- **O4 -- a truncated quotation in kowalski 2.1.** The (1.1) quotation
  ends "which is absolutely convergent." where the source continues into
  a parenthetical. Ordinary bounded-quotation truncation, no word
  altered.
- **O5 -- the source's own reuse of `r` in pintz10.** 1004.1072v1 uses
  `r` for the moment order in (2.11)/(2.16) and, in the same proof, for
  the division remainder in "H = RP + r, 0 <= r < P" and "[RP + 1, RP +
  r]". The extract quotes both correctly and does not flag the
  collision. Its reading -- that (2.16)'s exponent is (2.11)'s moment
  order -- is the right one, since the remainder enters only through the
  period decomposition, but a note would help a later reader. The
  untracked steering workpaper `pintz10-source-defects.md` records the
  same observation at its Section 8(4), independently.
- **O6 -- house MathJax conventions in the extracts.** Several extracts
  use a double backslash inside `\substack`, bare pipes for cardinality,
  `\log` without braces, and `\#` for a count. `mathjax_lint.py` passes
  on all of them, these are not on the graded surface, and correcting
  them would mean editing a survivor, which S7 forbids. Recorded only.
- **O7 -- kowalski's parity claim is the extract's, not the anchor's.**
  The uniformity ledger says the $`2^{1-k}`$ parity-vanishing
  probability "is exact for every fixed k ... not an asymptotic
  statement". The anchor prints only "which happens with probability
  2^{1-k} only". The claim is true in the paper's own
  $`\Omega_2`$ model and the extract gives its rationale in the same
  breath, so it is not an unexhibited assertion; but it is the extract's
  reading, not a scope qualifier the anchor states.

---

## Section 13 -- corrections to the ANN-78 grade prose, not inherited

Per the dispatch and the operator's standing choice, `extract-grades-r1.md`
is left as a timestamped record and is NOT edited. The two page errors in
its prose are corrected here instead, and this pass used the correct
pages throughout:

- Reference [17] of `2312.09021v2` is on **p.37**, not p.38. Exhibited in
  Section 5 (H1); p.38 carries only entries [21] and [22].
- Section 5 of `2601.07421` begins on **p.10**, not p.9. This anchor
  belongs to `precedent-p3-2601.07421.md`, one of the two extracts
  dropped by ANN-80, so no extract graded here cites it. The correction
  is recorded for the record's completeness and was not otherwise used.

**The ANN-78 grade was incomplete, booked plainly.** It has now been
shown incomplete four times: it passed two non-ASCII characters in a
quotation, missed a `report 1` reference split across a line break,
passed an I4 cross-reference without checking that the path still
resolved, and -- as this pass adds -- passed two extracts carrying false
statements about their anchors' own structure. That is why a single
grade of these extracts is not trustworthy and why this pass re-graded
everything fresh rather than diffing.

---

## Section 14 -- STOP-AND-REPORT, all seven reported

- **S1 -- NOT FIRED.** HEAD equals the Section 0 pin; the diff is empty;
  no commit has landed past the pin. The four untracked files of Section
  0 are neither commits nor writes of this apply.
- **S2 -- NOT FIRED.** Each of the three Appendix B anchors matches
  exactly once.
- **S3 -- NOT FIRED.** Last annotation is `ANN-20260728-80`; item-0033 is
  `status: ratified` at position 1 of the execution order; `extract/`
  holds exactly the five survivors; no item-0022-workpaper hash was
  present at start.
- **S4 -- NOT FIRED.** Every cited PDF location exists and is legible. No
  fidelity check was abandoned for want of a readable location. Two
  anchors needed care -- `2109.03767v3`'s Type 1 encoding (Section 7) and
  `1004.1072v1`'s digit-zero glyphs (Section 9) -- and both were resolved
  from the font encoding rather than guessed.
- **S5 -- NOT FIRED.** Every gate in Section 4 of the dispatch passed at
  start and at close; see Section 2 above and Section 15 below.
- **S6 -- NOT FIRED.** All five PDF sha256 values match their booked
  lines, so grading began. The three hash lines this apply adds were each
  recomputed from the file in the tree after the write and match. No hash
  was added for a bounced extract, and none for this record, which is
  correct because the pass is not terminal. Nothing under `roadmap/`,
  `lean/`, `runs/`, `writeup/`, the checklist, `extract-grades-r1.md`,
  `extract-inventory.py`, `extract-inventory-r1.md` or any extract file
  was touched.
- **S7 -- NOT FIRED, and deliberately so.** Two extracts could not be
  made to pass without editing them. Neither was edited: both were
  bounced with a repair spec, which is what S7 requires. No claim in this
  record asserts a fidelity it did not exhibit; every PASS above carries
  its source span.

---

## Section 15 -- gates at close

Re-run after the writes. The five extracts were graded and not edited, so
their ASCII counts and every gate except the ledger, HANDOVER and HASHES
writes reproduce start-of-pass output exactly.

```
blocks.py check-frozen ......... FROZEN BLOCKS: all byte-identical
blocks.py relocation-check ..... PASSED
sorry scan ..................... lean/Erdos251/Statement.lean:21 (baseline, unchanged)
lake-manifest rev count ........ 1
lean-toolchain last byte ....... \n
roadmap.py show item-0033 ...... status: ratified
writeup_mapper.py check ........ PASS
mathjax_lint.py ................ 0 problem(s), now including this record
extract/ non-ASCII counts ...... 0 0 0 0 0
HANDOVER.md non-ASCII .......... 0
extract-grades-r2.md non-ASCII . 0
```

**Hash-integrity gate.** Each of the three lines added to
`payloads/HASHES.txt` was checked by recomputing the sha256 of the named
file in the tree after the write. All three match. Nothing else in that
file was altered; the write is append-only.

---

## Section 16 -- what this sets up

item-0033's acceptance is **not** met by this pass. Three of the five
survivors are CLEAN and hashed; two are bounced. The item stays open and
stays ratified at position 1.

The path forward, in order:

1. A **repair apply** on `kuperberg23-apsmooth.md` and
   `pintz10-patterns.md`, to the specs in Section 11. It should fold in
   the header-line work of Section 10(a) and O1 across all five, since it
   is the same line and this pass could not touch it.
2. A **terminal re-grade** by a session that did not perform that repair,
   over the two repaired extracts, which then hashes them and hashes the
   re-grade record.
3. The **close**, a separate roadmap apply, the operator's: set
   `item-0033` to its terminal status, move it to `roadmap/completed/`,
   and write the close summary recording the full disposition -- register
   withdrawn, five extracts graded CLEAN and hashed, two precedents
   dropped, seventh verdict-promotion recurrence booked, surrogate rule
   routed to item-0034.

This pass recommends none of the close and performs none of it. It
recommends step 1.
