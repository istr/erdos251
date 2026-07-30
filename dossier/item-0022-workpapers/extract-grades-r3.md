# Re-grade r3 -- the two repaired item-0022 extracts, terminal

Phase 2d-residual of item-0033, the TERMINAL re-grade. Executed by the
local executor (Claude Opus 5, `claude-opus-5[1m]`) on 2026-07-30
against pin `08164ba2d76212a8daf368efe73cd73109d606eb`, under an
ephemeral dispatch that was never committed. This session did not
produce, repair or previously grade either of these extracts; it is the
fresh session the ANN-82 entry and `extract-grades-r2.md` Section 16
require, because an executor must not grade its own repair.

Scope: the DELTA since the r2 grade, in full. The repair changed only
`kuperberg23-apsmooth.md` and `pintz10-patterns.md`, and only inside the
bounce spans, so the diff
`2229c55..HEAD -- extract/kuperberg23-apsmooth.md extract/pintz10-patterns.md`
is the exact grading surface. Every added or changed line in it is
graded here -- new quotations, new citations, new paraphrase claims
about the source, changed page references -- not merely the three
in-span additions ANN-82 disclosed. The r2 record verified everything
the repair did not touch; the diff confirms nothing outside the bounce
spans drifted, and the unchanged remainder is not re-graded.

Fidelity was decided against the PDF at every point. `repair-log-2d-bounce.md`
exhibited the repair's own additions; that exhibition was treated as a
claim to be tested, not as evidence, and no PASS below rests on it.

**Verdict: BOTH CLEAN. The pass is terminal.**

---

## Section 0 -- preflight, all eight checks

| check | required | observed | result |
| --- | --- | --- | --- |
| P1 | `git diff --stat <pin>..HEAD` empty or `roadmap/` only | HEAD equals the pin; diff empty | PASS |
| P2 | last annotation id is `ANN-20260728-82` | last id in `ledger.yaml` is `ANN-20260728-82` | PASS |
| P3 | `item-0033` ratified at position 1 | `status: ratified`; `roadmap.py order` reports it at position 1; `roadmap.py next` reports `item-0033` | PASS |
| P4 | `extract-grades-r2.md` and `repair-log-2d-bounce.md` exist and are unmodified since the pin | both present; empty diff against the pin and clean in `git status` | PASS |
| P5 | the three PDF sha256 match both the header and the booked line | three for three, both ways | PASS |
| P6 | the three CLEAN extracts' ANN-81 hashes still match their files | three for three | PASS |
| P7 | neither repaired extract appears in `payloads/HASHES.txt` | neither does | PASS |
| P8 | the two Appendix B anchors each occur exactly once | 1, 1 | PASS |

P5 in full -- computed sha256, the extract header (for the two own
anchors) and the `payloads/HASHES.txt` line, all identical:

```
c67fdd9c9a822581371409e3fae54c9fcf97e0bd1a0b534fb22ea7a4b61f9617  dossier/2301.06095v1.pdf   HASHES.txt:86
653dcd731f11c6bab47fa61989b31f50dc3318464fc4d300276698045ba48939  dossier/2210.09775v2.pdf   HASHES.txt:21
74824028eb50c322f43da700fcb31fe10ce91272fe8e73695e9a4f82df22053b  dossier/1004.1072v1.pdf    HASHES.txt:82
```

`2210.09775v2` carries no extract header hash: it is the anchor
`kuperberg23-apsmooth.md` cross-references at its front-matter
identification ("This is a different paper from the anchored
arXiv:2210.09775v2"), and it is checked here against its booked line
alone, which is what that reference asserts.

P6 in full -- recomputed from the files in the tree at start of pass:

```
9125824e3517864026dbb98b453b498d9941cd86038bddf2d42722431ccd4d2c  extract/bloomkuperberg23-oddmoments.md  = HASHES.txt:92
2177b8054b3c271ea682eb8c610d2e44c536abb9aa631c9e6d22f32a4e65f451  extract/kowalski-singser-dist.md        = HASHES.txt:93
50beadb89264ea18a5faabe6f070c5f8950517304f36d0b812192ee0c1032c00  extract/kuperberg21-oddmoments.md       = HASHES.txt:94
```

**Rule-18 delta, recorded verbatim.** HEAD equals the Section 0 pin, so
rule 18 does not fire. The working tree carries four untracked files at
pin time, none of them written by this pass:

```
?? dossier/item-0022-workpapers/pintz10-2-16-recheck.py
?? dossier/item-0022-workpapers/pintz10-2-16-recheck.txt
?? dossier/item-0022-workpapers/pintz10-source-defects.md
?? item-0033-terminal-regrade-dispatch-v1.md
```

The first three are the same steering workpaper of 2026-07-26 the r2
record names in its own Section 0; the fourth is this pass's ephemeral
dispatch. This pass neither edits, hashes, commits nor relies on any of
them.

---

## Section 1 -- rendering convention for the exhibitions

Every exhibition below is the `pdftotext` rendering of the anchored PDF
at the cited page, ASCII-folded, because the gate requires this record
to be ASCII-only. Folding used, and nothing else:

```
nu mu sigma phi eps gamma eta theta vartheta Delta  ell -> l
<=  >=  <<  ~ (for the tilde-sim)  !=  ->  infinity  |  ndiv
in  subset  union  empty  prod  sum  refines (for the curly precedes)
Fraktur S -> S   en/em dash -> hyphen   curly quotes -> straight
```

Where a rendering artifact of the anchor's own font encoding matters it
is named at the point of use rather than folded silently. Two of the
four exhibitions below were additionally read on a 200-dpi render of
the page, because a `pdftotext` layout dump cannot settle the internal
structure of a multi-line display; those two are marked.

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
mathjax_lint.py ................ 140 file(s) checked, 0 problem(s)
extract/ non-ASCII counts ...... 0 0 0 0 0
HANDOVER.md non-ASCII .......... 0
git status --porcelain ......... the four untracked files of Section 0
```

---

## Section 3 -- the grading surface, established from the diff

`git diff 2229c55..HEAD` over the two files returns exactly four hunks.
One is in `kuperberg23-apsmooth.md`, at the Theorem 1.2 sentence: 3
lines removed, 10 added. Three are in `pintz10-patterns.md` -- Section
2.1's lead-in, Section 2.2 under Lemma 1's display, and Section 3 --
14 lines removed and 26 added between them. No other file, and no other
span of these two files, appears in the diff. Line counts move 89 to 96
and 279 to 291, as ANN-82 records.

That is the whole surface, and all of it is graded below. In
particular the Section 3 rewrite in `pintz10-patterns.md` is graded as
paraphrase carrying citations: its section heading reads "(paraphrase
except quotes)", but a citation to the wrong page or a claim the source
does not make is a fidelity defect whether or not it sits inside
quotation marks. That is the lesson the 2d bounce taught, applied
exactly where the 2d bounce was.

---

## Section 4 -- axis 3.2, the robust dropped-object scan, fresh

Run from the repo root with line breaks flattened, so a reference split
across a line break cannot hide, over the alternation the r2 record
used (`report N`, `appendix c.N`, `kickoff`, `operator-held`,
`operator-verified`, `re-verified this session`, `against the
dispatch`, `this session`), widened here by `verdict register`,
`absorption-checklist` and `precedent-pN`:

```
== dossier/item-0022-workpapers/extract/kuperberg23-apsmooth.md
  (none)
== dossier/item-0022-workpapers/extract/pintz10-patterns.md
  (none)
```

**Outcome: the repair introduced no reference to a dropped object, and
removed none that was there.** Both files were already clean of these
at the r2 grade and remain so. The `this session` hit the r2 record
found is on `kowalski-singser-dist.md`, which this pass does not touch
and does not re-grade.

---

## Section 5 -- axis 3.3, in-tree path-liveness, fresh

Every in-tree cross-reference the two extracts make, re-checked to
resolve at HEAD.

| extract | reference | resolves at HEAD |
| --- | --- | --- |
| both | `dossier/item-0022-workpapers/extract-grades-r1.md` | YES, file present |
| kuperberg23 | `/home/istr/pro/erdos251/dossier/2301.06095v1.pdf` | YES, sha256 matches header and booked line |
| kuperberg23 | "the anchored arXiv:2210.09775v2" | YES, `dossier/2210.09775v2.pdf` present, sha256 matches `payloads/HASHES.txt` line 21 |
| pintz10 | `/home/istr/pro/erdos251/dossier/1004.1072v1.pdf` | YES, sha256 matches header and booked line |
| pintz10 | `AGENTS.md` | YES, file present |

**Outcome: no dangling in-tree reference on either extract.** The
repair added no in-tree reference; the five above are the same set the
r2 record cleared, re-established here rather than inherited. This axis
bounces nothing.

---

## Section 6 -- `kuperberg23-apsmooth.md` -- CLEAN

Anchor `dossier/2301.06095v1.pdf`, sha256 `c67fdd...f9617`, 19 pages.
The delta is one sentence, the Theorem 1.2 description at lines 55-65,
rewritten from three lines to ten. Four distinct claims, each checked
at its cited location.

**K1 -- display (9)'s summation conditions, p.4.** Read on a 200-dpi
render of p.4 as well as the layout dump, because the `pdftotext`
column layout cannot settle which conditions sit under which summation
sign.

```
p.4, display (9), the two summation signs and the factor between them:
  sum_{0 <= j <= k/2}  (-1)^j
    sum_{ P refines {C_l}_{l in [1,k]}
          P = {S_1, ..., S_{k-j}}
          |S_m| = 2  for all 1 <= m <= j
          |S_m| = 1  for all j < m <= k-j }
      ( (h/r) sum_{d | Q, d > 1} mu(d)^2 / phi(d) )^j
        sum_{sigma in B(j+1,...,k-j)} prod_{(i_1,i_2) in sigma}
          V_2(Q, h; r, c(S_{i_1}), c(S_{i_2})), + O_{r,k}( h^{k/2-1/(7k)+eps} ).
```

PASS on all four counts the extract asserts.

- **The range.** The extract's "for each $`0\le j\le k/2`$" is the
  outer summation index as printed.
- **The block structure.** The extract's "$`j`$ doubleton blocks
  $`S_1,\ldots,S_j`$ and $`k-2j`$ singleton blocks
  $`S_{j+1},\ldots,S_{k-j}`$" is exactly
  $`\lvert S_m\rvert=2`$ for $`1\le m\le j`$ and
  $`\lvert S_m\rvert=1`$ for $`j<m\le k-j`$. The singleton count
  $`(k-j)-j=k-2j`$ is arithmetic on the printed index ranges, and
  $`2j+(k-2j)=k`$ is consistent with $`P`$ being a partition of
  $`[1,k]`$.
- **The matching pairs the singletons -- the correction.** The source
  ranges $`\sigma`$ over $`\mathcal{B}(j+1,\ldots,k-j)`$, whose index
  set $`\lbrace j+1,\ldots,k-j\rbrace`$ is precisely the singleton
  block indices, and the summand's arguments are
  $`c(S_{i_1}),c(S_{i_2})`$ for $`(i_1,i_2)\in\sigma`$. The extract
  now says the matchings "pair the singleton blocks
  $`S_{j+1},\ldots,S_{k-j}`$", which is what the display does. This is
  the r2 CLEAN-blocker, repaired correctly.
- **The doubleton factor.** The extract's
  $`\left(\frac{h}{r}\sum_{d\mid Q,\,d>1}\frac{\mu(d)^2}{\phi(d)}\right)^j`$
  matches the printed factor term for term, including that the
  fraction is $`h`$ over $`r`$ and that the whole bracket carries the
  exponent $`j`$. Confirmed on the render, where the fraction bar and
  the outer exponent are unambiguous. The extract's reading -- that
  this factor is what carries the $`j`$ doubleton blocks -- follows
  from the display: the doubleton blocks appear nowhere else in the
  summand.

**K2 -- the independent confirmation at (16), p.6.** The anchor's
smooth-weight analogue of (9) carries a closing clause that fixes the
same reading from the other side.

```
p.6, immediately after display (16):
  where the sum is taken over partitions of [1, k] where each part has either 1 or 2
  elements, and for |S_m| = 1, f_{S_m} denotes f_j where j in S_m.
```

PASS. The paired argument $`f_{S_m}`$ is defined only for a singleton
block, so the matching in the analogous display can only be pairing
singletons. The reading is not ambiguous, and it is now the extract's.

**K3 -- the refinement condition, and that it is not an over-statement.**
The extract's added clause is that the partitions "refine the
congruence-class sets $`C_\ell`$ of p.3". Both halves check.

```
p.3, last line:
  In order to state our main result on the asymptotics of R_k(h; r, c_1, ..., c_k), we define some
  further notation. For 1 <= l <= r, define
                             C_l := {i : c_i = l mod r} .
```

```
p.4, first paragraph:
  Note that some of the sets C_l may be empty, and that union_{l=1}^{r} C_l = [1, k]. We will say
  that a partition P = {S_1, ..., S_M} of [1, k] refines {C_l}_{l in [1,k]} if for each S_m in P,
  there exists some l with S_m subset C_l; note that l is then unique. For such a partition,
  write P refines {C_l}_{l in [1,k]} and define c(S_m) to be the value l with S_m subset C_l.
```

PASS, and PASS on the over-statement question specifically. The
refinement relation is the source's own summation condition on the
inner sum of (9) -- the source writes it with the curly-precedes
symbol, defined in the paragraph above as exactly "refines" -- so
stating it is reproducing a printed condition, not adding one. The
extract attributes $`C_\ell`$ to p.3, which is where it is defined;
the refinement relation itself is defined at the top of p.4, and the
extract does not claim otherwise. The extract quantifies the
$`C_\ell`$ with no index range, which sidesteps a discrepancy internal
to the anchor (the definition reads $`1\le\ell\le r`$ while the
refinement notation writes $`\lbrace C_\ell\rbrace_{\ell\in[1,k]}`$);
nothing is asserted that the source does not bear.

**K4 -- the $`\mathcal{B}(\cdot)`$ notation, p.3.** The extract calls
the elements of $`\mathcal{B}(j+1,\ldots,k-j)`$ "perfect matchings".

```
p.3:
  Let B_k denote the set of perfect matchings of [1, k], so that ... (8) ...
  Note that when k is odd, B_k = empty. Moreover, for a set of integers {a_1, ..., a_k}, we will
  denote by B(a_1, ..., a_k) the set of matchings of {a_1, ..., a_k} into pairs, so that
  B_k = B([1, k]).
```

PASS. $`\mathcal{B}(\cdot)`$ is the source's own generalization of
$`\mathcal{B}_k`$, the set of perfect matchings, to an arbitrary index
set, so "perfect matchings $`\sigma\in\mathcal{B}(j+1,\ldots,k-j)`$"
is the anchor's own vocabulary.

**Nothing outside the delta was re-graded**, and the diff confirms
nothing outside it moved. The r2 record's Q1, Q2, Q3, N1 and the
Theorem 1.4 adjudication stand as that record's, unchanged and
untouched by the repair.

**Grade: CLEAN.**

---

## Section 7 -- `pintz10-patterns.md` -- CLEAN

Anchor `dossier/1004.1072v1.pdf`, sha256 `748240...22053b`, 9 pages.
Three repair points, of which the Section 3 rewrite is the substantial
one. Every cited page in the delta exists and is legible.

**P1 -- Section 2.1's page correction, `p.6-7` to `p.6`.**

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
  Proof of Lemma 2. We will prove in fact a little bit more. ...
```

PASS. The quoted block -- Lemma 2, its display, and both Remarks -- is
entirely on p.6; the page break falls three lines later, inside the
proof lead-in. The lead-in and the section heading now agree, both
reading p.6.

**P2 -- the Section 2.3 `p.6-7` left unchanged is correct.** The
passage that lead-in cites genuinely straddles the break: "We will
prove in fact a little bit more ... the square of the singular series
will be" are the last lines of p.6, and "larger at most by a factor
depending on t. In such a way, (2.10) follows by induction from
(2.11) ... on t and r." are the first lines of p.7. PASS -- the repair
was right to leave it.

**P3 -- Section 2.2's added Remark quotation, p.6.** The elision the r2
record found was closed by quoting the intervening Remark rather than
by an ellipsis.

```
p.6, between Lemma 1's display (2.8) and the "somewhat analogous" Remark:
  (2.8)   sum_{D subset [1,H], |D|=nu} S^2(D^+) <= c_7(nu)H^nu.
  Remark. The parameter H can be arbitrary here, not just that given in
  (2.2).
  Remark. The above lemma is somewhat analogous to Gallagher's theorem
```

PASS, byte-faithful. The extract's

> **Remark.** The parameter H can be arbitrary here, not just that given in
> (2.2).

is the source string character for character, including the line break
falling after "given in", with only the extract's own house bolding of
the word "Remark." added -- the same bolding it applies to Lemma 1,
Lemma 2 and every other Remark it quotes. The placement is the
source's: between (2.8) and the "somewhat analogous" Remark, exactly
where the source prints it. The presented adjacency in Section 2.2 is
now the source's own adjacency, which is what the r2 finding asked for.

**P4 -- Section 3, the rewrite. Every claim at its cited page.**

*(a) The survey sentence -- Green-Tao and [GPY2] at p.1.*

```
p.1:
  A few years ago Green and Tao [GT] proved their striking result about
  patterns in primes.
  Theorem (Green-Tao). The primes contain arbitrarily long arithmetic pro-
  gressions.
  ...
      Another, albeit conditional result of Goldston, Yildirim and the author
  [GPY2] yielded the existence of other patterns.
  Theorem ([GPY2]). If the primes have a distribution level theta > 1/2, that
  is, if for any positive eps and A we have ... (1.2) ...
  then there exists a positive even d <= C_1(theta) and infinitely many pairs of
  primes
  (1.3)                        p, p + d in P.
```

PASS. Both are on p.1, as the extract says. The extract's
"conditional" is the anchor's own word for [GPY2] ("Another, albeit
conditional result"), and "bounded-gap theorem" is what the statement
is: a positive even $`d\le C_1(\vartheta)`$ with infinitely many
prime pairs $`p,p+d`$. The label `[GPY2]` is the one the anchor prints
at this location. The attribution "Goldston-Pintz-Yildirim" resolves
the anchor's "Goldston, Yildirim and the author" correctly, the author
being Pintz.

*(b) "Theorem [Pin]" at p.2, and that it is a cited prior preprint.*

```
p.2:
      The author showed recently that a combination of the two above results
  is possible, showing thereby new patterns of primes.
  Theorem [Pin]. If the primes have a distribution level theta > 1/2 then there
  exists a positive even d <= C_1(theta) such that the set P(d) of primes p satisfying
  (1.3) contains arbitrarily long arithmetic progressions.
```

PASS. It is at p.2; it is introduced as the author's own recent work
elsewhere; and it is keyed to a bibliography entry, so it is a cited
prior preprint and not a theorem this note proves. The extract's gloss
of its content -- distribution level $`\vartheta>1/2`$, an even
$`d\le C_1(\vartheta)`$, the set of primes $`p`$ with $`p,p+d`$ both
prime containing arbitrarily long arithmetic progressions -- resolves
the anchor's `P(d)` through (1.3) on p.1, correctly.

*(c) The p.9 bibliography entry, byte-faithful.*

```
p.9, References:
  [Pin] J. Pintz, Are there arbitrarily long arithmetic progressions in the se-
       quence of twin primes? preprint, arxiv math.NT
```

PASS, character for character against the extract's quotation, with
the source's own hyphenation across the line break ("se-/quence")
closed up, and with no terminal period, which the source does not
print either. Checked programmatically against the p.9 text layer with
whitespace normalized, not by eye.

*(d) "Theorem [GPY3]" at p.3.*

```
p.3:
  Theorem [GPY3]. Unconditionally we have Delta*_1 = 0; further the Elliott-
  Halberstam conjecture [EH] implies Delta*_2 = 0.
```

PASS. It is at p.3, and it is a result this note builds on -- p.4
opens "The aim of this note is to show that the method of the
mentioned work [GPY3] can be modified to yield ...".

*(e) This note's own Theorem: unconditional, p.4, proved in Section 2,
with (1.17) and the Corollary.* Read on a 200-dpi render of p.4 as
well as the layout dump, because `pdftotext` drops the cardinality bars
around $`\mathcal{D}_N^\nu`$ in (1.17).

```
p.4:
      The exact formulation of our result to be proved is as follows.
  Theorem. Let eta > 0 be any positive constant, nu and m natural numbers.
  Then we have a positive constant c(eta, nu) depending on eta and nu such that
  for any N > N_0(eta, nu, m) we have a set D_N^nu of nu-tuples (d_1, ..., d_nu) with
  0 < d_1 < ... < d_nu such that
  (1.17)                  |D_N^nu| >= c(eta, nu) log^nu N
  and every element of D_N^nu satisfies (1.15) and (1.16).
  Corollary Under the above conditions, if (d_i)_{i=1}^{nu} in D_N^nu then the set
  P(d_1, ..., d_nu) of primes contains at least c'(eta, nu, m) N^2/log^m N arithmetic pro-
  gressions of length m.
```

```
p.5, section heading:
  2   Proof of the Theorem
```

PASS on every component.

- **At p.4** -- the Theorem is printed there, as is the Corollary.
- **Unconditional** -- the statement carries no distribution-level
  hypothesis and no other conditional premise; it is quantified over
  $`\eta>0`$, natural $`\nu,m`$ and $`N>N_0(\eta,\nu,m)`$ only. The
  contrast the extract draws with the conditional [Pin] is the
  anchor's own.
- **Proved in Section 2, heading "2 Proof of the Theorem", p.5** --
  the heading is at p.5, byte-faithful.
- **The tuple-count size at (1.17)** -- the extract's "a set of
  $`\nu`$-tuples of admissible differences of size
  $`\gg\log^\nu N`$ (1.17)" is
  $`\lvert\mathcal{D}_N^\nu\rvert\ge c(\eta,\nu)\log^\nu{}N`$ as
  printed, with the constant absorbed into $`\gg`$.
- **The AP-count Corollary at p.4** -- the extract's "each realizing
  $`\gg N^2/\log^m N`$ length-$`m`$ arithmetic progressions of
  $`(\nu{+}1)`$-tuples of primes" is the Corollary's
  $`c'(\eta,\nu,m)N^2/\log^m{}N`$ progressions of length $`m`$ inside
  $`\mathcal{P}(d_1,\ldots,d_\nu)`$, which (1.15) on the same page
  defines as the set of primes $`p\in[N,2N)`$ with $`p+d_i`$ prime for
  every $`i`$ -- so each member of such a progression is the base of a
  $`(\nu{+}1)`$-tuple of primes. The anchor's own Remark immediately
  below the Corollary says the same in its own words ("we actually
  obtain a large number of nu + 1-dimensional arithmetic progressions
  ... as a configuration of primes p^(j) + d_i in P, p^(j) in P where
  {p^(j)}_{j=1}^{m} forms an m-term arithmetic progressions").

*(f) The "quantitative strengthening" framing is gone.* A search of
`extract/` for the string returns zero hits. PASS. The claim it
carried -- that this note's Theorem strengthens [Pin]'s -- is not made
anywhere in the rewritten section, which is right: the two theorems
have different hypotheses and different conclusions, and neither
implies the other as printed.

*(g) The unchanged tail of the paragraph.* The rewrite's closing
sentence -- the reduction via Selberg's sieve, Cauchy-Schwarz and
Lemma 1 / Lemma 2's bound on $`\sum\mathfrak{S}^2(D^+)`$ to a sum over
$`\nu`$-subsets of $`[1,H]`$ -- is carried over from the pre-repair
text but sits inside the rewritten hunk, so it is graded here rather
than inherited. PASS: (2.1) on p.5 is the Selberg's sieve step ("can
be estimated from above by Selberg's sieve (cf. Theorem 5.1 of [HR]
...)"), (2.7) on p.5 is the Cauchy step ("Now, using Cauchy's
inequality, (2.5) implies"), and p.6 opens "Hence, in order to show
(2.6), thereby our Theorem, it is sufficient to show the following
Lemma 1", whose display (2.8) sums over $`D\subset[1,H]`$ with
$`\lvert D\rvert=\nu`$.

**Grade: CLEAN.**

---

## Section 8 -- verdicts, hashes and the terminal determination

| extract | grade | one-clause reason |
| --- | --- | --- |
| `kuperberg23-apsmooth.md` | **CLEAN** | display (9)'s summation conditions, the singleton pairing, the refinement condition and the doubleton factor all verified at `2301.06095v1` pp.3-4 and confirmed at (16) on p.6 |
| `pintz10-patterns.md` | **CLEAN** | the page correction, the added Remark quotation and every citation of the Section 3 rewrite verified at `1004.1072v1` pp.1-6 and p.9 |

**Hash lines added by this apply, to `payloads/HASHES.txt`:**

```
10e32aec27ae95ce5d707d79d37e3e22707951b6a5f61f0e1e3d08162bdfb3c4  dossier/item-0022-workpapers/extract/kuperberg23-apsmooth.md
283b57b91110e707378a1d2e6e932282066a31b5d7147f3c9cf3a94bd41d3e09  dossier/item-0022-workpapers/extract/pintz10-patterns.md
```

Neither path was booked before this apply, so both are new lines and
the one-line-per-file invariant holds.

**This record is hashed too, as the terminal determination**, and its
line is appended third. Its sha256 is deliberately NOT printed inside
this file: a file cannot state its own hash without changing it. The
value is computed from the finalized record and checked by the
hash-integrity gate at close, and it is readable at
`payloads/HASHES.txt` for
`dossier/item-0022-workpapers/extract-grades-r3.md`.

**What is still NOT hashed, and why.** `extract-grades-r1.md` (the
ANN-78 grade) and `extract-grades-r2.md` remain unhashed. The ANN-78
grade has now been shown incomplete four times and is kept as a
timestamped record of that incompleteness, not as a standing
determination; the r2 record is explicitly non-terminal by its own
Section 11. Neither is this pass's to book.

---

## Section 9 -- observations, none of them blockers

Recorded so a later pass does not have to rediscover them, and so that
the reasoning that kept them off the bounce list is on the record.

- **O1 -- "bounded even" for the anchor's "positive even", in the
  [Pin] gloss.** The extract's Section 3 renders Theorem [Pin]'s
  $`d`$ as "a bounded even $`d\le C_1(\vartheta)`$" where p.2 prints
  "a positive even $`d\le C_1(\vartheta)`$". The inequality, the
  parity and the constant are all preserved; what is dropped is
  positivity. Not a blocker: nothing is strengthened -- the extract's
  form is implied by the anchor's, not the reverse -- the quantifier
  order and the dependency $`C_1(\vartheta)`$ are intact, and the
  clause is paraphrase, not quotation. It is worth naming because
  positivity is what stops the statement from being satisfiable at
  $`d=0`$, so the paraphrase is looser than the source at one word.
  The wording predates the repair, which carried it over from the
  pre-repair paragraph unchanged; it was not introduced here and was
  not the r2 bounce.
- **O2 -- "admissible differences" is the extract's word.** The
  anchor's Theorem says only "a set $`\mathcal{D}_N^\nu`$ of
  $`\nu`$-tuples $`(d_1,\ldots,d_\nu)`$ with
  $`0<d_1<\cdots<d_\nu`$"; admissibility is not printed there. It is
  entailed, since every element of $`\mathcal{D}_N^\nu`$ satisfies
  (1.15), which forces $`\lvert\mathcal{P}(d_1,\ldots,d_\nu)\rvert>0`$
  and hence a realizing prime tuple. Not a blocker, and also
  pre-repair wording.
- **O3 -- the anchor's index-range discrepancy at
  $`\lbrace C_\ell\rbrace`$.** `2301.06095v1` defines $`C_\ell`$ for
  $`1\le\ell\le r`$ on p.3 and then writes
  $`\lbrace C_\ell\rbrace_{\ell\in[1,k]}`$ on p.4 and in (9). This is
  the source's own slip. The extract does not reproduce either index
  range, so it inherits nothing from it; recorded only so a later
  reader does not read the extract's silence as an omission.
- **O4 -- the r2 record's Section 12 observations O1-O7 are
  untouched.** None of them concerns the delta, and O1 (the stale
  "re-grade pending" header clause) is superseded by the disposition
  in Section 10 below rather than discharged.

---

## Section 10 -- the header disposition, carried forward

**No header was edited by this apply**, as by ANN-82. All five
survivors keep the clause "fidelity repair applied per the ANN-78
grade (`extract-grades-r1.md`) at this pin; re-grade pending."

That clause is now stale on all five: three were re-graded at ANN-81
and the remaining two are re-graded here. It is left in place
deliberately, as a 2c-era annotation SUPERSEDED BY THE LEDGER AND BY
THIS RECORD rather than edited, for the reason ANN-82 gives and this
apply inherits: the three CLEAN extracts are hashed at ANN-81 and the
two graded here are hashed by this apply, so editing any of them would
either break `payloads/HASHES.txt`'s append-only rule or add a second
line for a path that has appeared once, breaking a one-line-per-file
invariant that file has held over its whole history. A cosmetic
process-note is not worth either. The "at this pin" deixis in the same
clause was adjudicated non-blocking at ANN-81 and that adjudication
stands.

Grade-state does not belong in an extract header; it belongs in the
ledger and in the grade record, which now carry it authoritatively for
all five. The header-design rule -- a provenance header carries source
and hash only, never grade-state and never an unresolvable deixis -- is
routed to item-0034 and requires no edit to these five going forward.

**The close summary should carry this disposition**, together with the
two page corrections to the ANN-78 grade prose, which stay in
`extract-grades-r2.md` Section 13 and are restated here so that a
reader of the terminal record has them: reference [17] of
`2312.09021v2` is at **p.37**, not p.38; and Section 5 of
`2601.07421` begins at **p.10**, not p.9 (that anchor belongs to one of
the two extracts ANN-80 dropped, so no surviving extract cites it).

---

## Section 11 -- STOP-AND-REPORT, all seven reported

- **S1 -- NOT FIRED.** HEAD equals the Section 0 pin; the diff is
  empty; no commit has landed past the pin. The four untracked files of
  Section 0 are neither commits nor writes of this apply.
- **S2 -- NOT FIRED.** Each of the two Appendix B anchors matches
  exactly once.
- **S3 -- NOT FIRED.** Last annotation at start is `ANN-20260728-82`;
  item-0033 is `status: ratified` at position 1 of the execution order;
  `extract-grades-r2.md` and `repair-log-2d-bounce.md` are unmodified
  since the pin; all three ANN-81 CLEAN hashes matched at start; neither
  repaired extract was already booked in `payloads/HASHES.txt`.
- **S4 -- NOT FIRED.** Every cited PDF location in the delta exists and
  is legible: `2301.06095v1` pp.3, 4, 6 and `1004.1072v1` pp.1, 2, 3, 4,
  5, 6, 9. No fidelity check was abandoned for want of a readable
  location. Two displays needed a 200-dpi render rather than the layout
  dump -- `2301.06095v1` display (9) and `1004.1072v1` (1.17) -- and
  both were resolved from the render, not guessed.
- **S5 -- NOT FIRED.** Every gate in the dispatch's Section 4 passed at
  start and at close, including the frozen-CLEAN and hash-integrity
  gates; see Section 2 above and Section 12 below.
- **S6 -- NOT FIRED.** All three PDF sha256 values match their booked
  lines, so grading began. Every hash line this apply adds was
  recomputed from the file in the tree after the write and matches. No
  hash was added for a bounced extract, because neither bounced; the
  record's own hash is added because the pass is terminal. Nothing under
  `roadmap/`, `lean/`, `runs/`, `writeup/`, the checklist, the
  inventory, `extract-grades-r1.md`, `extract-grades-r2.md`,
  `repair-log-2d-bounce.md`, any extract file or any extract header was
  touched.
- **S7 -- NOT FIRED.** No extract needed an edit to pass. Neither
  extract was edited by this pass at all: both were graded as they stand
  at the pin and both earned CLEAN on the delta. No defect was found on
  any of the three frozen CLEAN extracts, which were not opened for
  grading -- they are frozen at ANN-81, and a finding on one would be
  logged and reported here, never repaired. Every PASS above carries its
  source span.

---

## Section 12 -- gates at close

Re-run after the writes. Both extracts were graded and not edited, so
their ASCII counts and every gate except the ledger, HANDOVER and
HASHES writes reproduce start-of-pass output exactly.

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
extract-grades-r3.md non-ASCII . 0
```

The only gate movement is `mathjax_lint.py`'s file count, which rises
by this record.

**Frozen-CLEAN gate.** The three ANN-81 CLEAN extracts were re-hashed
from the files in the tree after the writes; each still equals its
booked line, `payloads/HASHES.txt` lines 92-94:

```
9125824e...cd4d2c  extract/bloomkuperberg23-oddmoments.md   MATCH
2177b805...65f451  extract/kowalski-singser-dist.md         MATCH
50beadb8...032c00  extract/kuperberg21-oddmoments.md        MATCH
```

**Hash-integrity gate.** Each of the three lines added to
`payloads/HASHES.txt` was checked by recomputing the sha256 of the
named file in the tree after the write. All three match. Nothing else
in that file was altered; the write is append-only.

---

## Section 13 -- what this earns

**item-0033's acceptance is met in full.** With both extracts CLEAN and
hashed:

- the register was withdrawn as an instrument (ANN-77);
- the extracts were graded against their anchors and repaired (ANN-78,
  ANN-79);
- the two entangled precedent extracts were dropped and the severance
  residuals closed (ANN-80);
- **five extracts are graded CLEAN and hashed** -- three at ANN-81, two
  at this terminal entry -- and **two precedents are dropped**, which is
  the five-not-seven acceptance ANN-80 set;
- the seventh verdict-promotion recurrence was booked and routed to
  item-0034 (ANN-76), along with the surrogate-standing rule and the
  header-design lesson.

**The close is not this pass's to perform.** It is the operator's
separate roadmap apply, mirroring item-0022 and item-0031: set
`item-0033` to its terminal status, move it to `roadmap/completed/`,
and write the close summary. The close summary should record the full
disposition, including the five-not-seven acceptance, the header
disposition of Section 10 above, and the two page corrections to the
ANN-78 grade prose restated there.

This pass recommends the close and performs none of it.
