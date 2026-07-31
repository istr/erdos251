# Source-level observations on arXiv:1004.1072v1, read against arXiv:1004.1084v1

Workpaper. Authored by steering (Claude Opus 5) on operator instruction,
2026-07-26. NOT COMMITTED. Verification status: awaiting executor
confirmation under the item-0022 repair dispatch r1, Task D; awaiting
operator ratification thereafter.

This paper records three observations about a primary source and one
relation between two primary sources. It is deliberately not called an
erratum: an erratum is issued by an author. Two of the three observations
are print-level defects in a preprint; the third is a result of this
project and not a defect at all. They are independent and are not to be
aggregated into a judgement about the source as a whole.

---

## Section 0 -- Objects and anchors

| object | anchor | sha256 |
| --- | --- | --- |
| J. Pintz, "Patterns of primes", 9 pp., 7 Apr 2010 | https://arxiv.org/pdf/1004.1072v1 | 74824028eb50c322f43da700fcb31fe10ce91272fe8e73695e9a4f82df22053b |
| J. Pintz, "On the singular series in the prime k-tuple conjecture", 4 pp., 7 Apr 2010 | https://arxiv.org/pdf/1004.1084v1 | f730b045f1163bd539120e3e47237e92720e222d4663db1f86931d620739e5e5 |

In-tree extract of the second, in corpus since item-0017:
`dossier/item-0017-workpapers/extract/pintz10-singser.md`. Its Theorem 1
and Theorem 1' blocks are quoted verbatim there and are the source of the
threshold statements in Section 5 below.

Notation follows the in-tree extract convention: the Fraktur singular-series
symbol is written $`S`$, the anchored tuple is $`\mathcal D^{+} = \mathcal D \cup \lbrace 0 \rbrace`$,
$`\nu_p`$ is the number of residue classes occupied modulo $`p`$, and
$`r`$ is the moment order.

---

## Section 1 -- Instruments and their standing

No observation below rests on a single instrument. This section exists so
that a later reader can see which instrument carries which fact, and where
an instrument is weaker than it looks.

| # | instrument | what it settles | standing |
| --- | --- | --- | --- |
| I1 | two blind image readings, cross-family (Fable 5 Max, ChatGPT-5.6 Sol Pro), identical operator prompt, PDF text tooling explicitly forbidden, separate anonymous sessions | the printed exponent in (2.10) and the absence of the cardinality condition | two samples of ONE instrument class. Both are language models reading rasterized mathematics; that is a shared failure mode, and cross-family diversity does not remove it |
| I2 | the arXiv text layer for the same identifier | the same two facts, from the character stream rather than from a rendering | a genuinely different instrument. But the read was a live fetch of the identifier, NOT of the anchored bytes. This is the gap that r1 Task D closes |
| I3 | self-consistency of the printed statement | that the printed form cannot be what is meant | needs no glyph at all; see Section 2 |
| I4 | symbolic computation, `pintz10-2-16-recheck.py` | the order of the local average in (2.16) | reproducible; support class MEASURED |
| I5 | the convention of the companion note | the reading of (2.12) | the strongest instrument available here: the author's own hand, same day |

---

## Section 2 -- D1: the exponent and the cardinality condition in (2.10)

**What is printed.** As carried by I1 and I2, Lemma 2 reads

```
Lemma 2. For fixed nu r and H > H0(nu, r) we have
(2.10)   S(nu, r) = SUM            S^2(D^+)  <=  c8(nu, r) H^nu
                    D subset [1,H]
```

That is: the exponent on the singular series is the digit 2, the same glyph
as in (2.8) of Lemma 1, and the condition $`\lvert \mathcal D \rvert = \nu`$
is absent under the summation sign, although it is present in both (2.8)
and (2.9).

**What the proof supports.** The $`r`$-th moment under
$`\lvert \mathcal D \rvert = \nu`$:

$$\sum_{\substack{\mathcal D \subset [1,H] \cr \lvert \mathcal D \rvert = \nu}} S^{r}(\mathcal D^{+}) \;\le\; c_8(\nu,r)\,H^{\nu}.$$

**Four internal signals, each independently sufficient to exclude the
printed form.**

1. Notation. The left-hand side is written $`S(\nu,r)`$. In this display
   $`\nu`$ can enter only through the cardinality condition and $`r`$
   only through the exponent. The printed form makes both parameters of the
   left-hand side vacuous at once, and leaves $`c_8(\nu,r)`$ and
   $`H_0(\nu,r)`$ without an argument to depend on.
2. Falsity as printed. An unrestricted sum over all subsets of $`[1,H]`$
   has on the order of $`2^{H}`$ terms and cannot be bounded by
   $`c_8(\nu,r)H^{\nu}`$. The subsets of cardinality $`\nu+1`$ alone
   already contribute on the order of $`H^{\nu+1}`$.
3. The proof. Display (2.11) raises the one-position ratio to the power
   $`r`$, and its induction adds one element per step from the seed
   $`\mathcal D^{+} = \lbrace 0 \rbrace`$; each step contributes exactly one
   factor $`H`$, which is what produces $`H^{\nu}`$ on the right.
   Nothing in the proof addresses a statement whose exponent is fixed at 2
   for all $`r`$.
4. The remark on $`r = 1`$. The source states an asymptotic in that case.
   With a fixed exponent 2 there is no case $`r = 1`$ to state, and the
   second moment does not satisfy it.

**Support class.** The print state is MEASURED (I1 twice, I2 once; pending
confirmation against the anchored bytes). The intended reading is a
RECONSTRUCTION by this project, not a statement by the author.

**Consequence.** None for the item-0022 verdict on report 1. Report 1 cites
Lemma 2 for the general-moment claim, and Lemma 2 is the general-moment
lemma. The verdict is CONFIRMED and stays CONFIRMED.

---

## Section 3 -- D2: the product in (2.12) omits the anchor component

**What is printed.** In (2.12) the auxiliary product is
$`\Delta := \prod_{i=1}^{\nu}(h - d_i)`$, running over the $`\nu`$
elements of $`\mathcal D`$ only, although $`\mathcal D^{+}`$ has
$`\nu+1`$ elements and contains 0.

**What the companion does.** In (2.1) of 1004.1084v1 the corresponding
product runs over all $`k`$ elements of the set under consideration. The
same author, the same day, the same construction, with the element that
1004.1072v1 drops.

**Consequence, checked rather than asserted.** The product feeds the case
distinction that follows: $`p \mid \Delta`$ is used as the test for
whether the adjoined $`h`$ lands in a residue class already occupied. If
$`p \mid h`$ while $`p \nmid \prod_i (h - d_i)`$, then $`h`$ occupies
the class of the anchor element 0, so $`\nu_p' = \nu_p`$, whereas the
printed test assigns $`\nu_p' = \nu_p + 1`$. The mis-assignment affects
only the bookkeeping between the second and third products, for primes
dividing $`h`$, and is harmless for the estimates.

**Support class.** MEASURED (I2, I5). Reading of the intent: RECONSTRUCTION.

---

## Section 4 -- S1: the local average in (2.16) is one order sharper than printed

This is a result of this project. It is NOT a defect in the source, and it
must not be reported as one: the printed bound is correct, merely not
sharp.

**Printed.** Display (2.16) evaluates the per-prime factor of the period
average and states it as $`1 + O(p^{-2})`$, which suffices for the
convergence the source needs.

**Reproduced.** Expanding the printed factor as a formal series in
$`1/p`$, the linear terms cancel identically between numerator and
denominator, and so do the quadratic ones:

$$\frac{\frac{\nu_p}{p}\lparen 1-\frac{\nu_p}{p}\rparen^{r} + \lparen 1-\frac{\nu_p}{p}\rparen \lparen 1-\frac{\nu_p+1}{p}\rparen^{r}}{\lparen 1-\frac{\nu_p}{p}\rparen^{r}\lparen 1-\frac{1}{p}\rparen^{r}} \;=\; 1 \;+\; \frac{r\,\nu_p\,(r-1)}{2}\cdot\frac{1}{p^{3}} \;+\; O\lparen p^{-4}\rparen .$$

**The $`r = 1`$ collapse is exact, not asymptotic.** At $`r = 1`$ the
numerator equals the denominator identically, so the local factor is
exactly 1. This reproduces, from a different display in a different paper,
the statement (2.7) of 1004.1084v1, where the same average is asserted to
be exactly 1. Two independent routes to the same exact value.

**Why this project noticed.** Not sharpness for its own sake. The project
needs the dependence of $`c_8(\nu,r)`$ on the rank and on the moment
order; a third-order coefficient that is explicit in $`\nu_p`$ and
$`r`$ is a handle, and an $`O(p^{-2})`$ is not.

**Support class.** MEASURED. Series identity to the printed order plus
numerical spot checks at $`p = 101`$ and $`p = 10007`$ for several
$`(\nu_p, r)`$, including a non-integer $`r`$. It is not PROVED: no
remainder is controlled uniformly in $`p`$, $`\nu_p`$ and $`r`$ here.

**Reproduction.** `pintz10-2-16-recheck.py` in this directory, output in
`pintz10-2-16-recheck.txt`. Deterministic, no network, no input files.
The script records one reproducibility hazard: calling `simplify` on the
quotient with a symbolic exponent returns the literal 1, which is false;
numerator and denominator must be expanded separately.

---

## Section 5 -- The pairing, and the direction asymmetry

The two notes of 7 April 2010 treat the same one-position ratio
$`S(\mathcal H \cup \lbrace h \rbrace)/S(\mathcal H)`$ and split the work
between them.

| source | object | rank dependence |
| --- | --- | --- |
| 1004.1084v1, Theorem 1 | the average of the ratio, i.e. $`r = 1`$, two-sided | tracked: $`H \ge \exp{\lparen k^{1/\varepsilon}\rparen}`$ |
| 1004.1084v1, Theorem 1' | the same, lower bound only | cheaper: $`H \ge \exp{\lparen c_2 k/\log{k}\rparen}`$ |
| 1004.1072v1, Lemma 2 | the general $`r`$-th moment | not marked, expressly |

The thresholds are quoted verbatim in the in-tree extract named in Section 0
and are not restated from memory here.

**The asymmetry.** The two-sided statement at $`r = 1`$ costs a threshold
exponential in a power of the rank. The cheap threshold buys only a lower
bound. The general moment order comes with constants the source declines to
track.

**The author names the reason.** A remark in 1004.1084v1 observes that in
most applications one needs just lower estimates for the singular series.

**What this is, and what it is not.** It is a gap in the literature, named
by the author of the sharpest available treatment. It is NOT a corpus gap:
both sources are anchored, and 1004.1084v1 has been extracted since
item-0017. The project's target quantity is an averaged relative
one-position extension bound in the upper direction, uniform in the rank --
that is, the direction and the uniformity that this pair of notes does not
jointly supply.

**Routing.** This section is material for item-0028 and must be on its desk
before its sheet is authored. It changes no verdict in item-0022.

---

## Section 6 -- What does not follow

Stated explicitly, because each of these is a step somebody will otherwise
take.

- No verdict in the item-0022 checklist changes on account of D1. Report 1
  cited Lemma 2 correctly.
- Nothing here touches report 3 or any route. Route material is item-0031's,
  and item-0031 is proposed and unscheduled.
- The three observations do not aggregate. Two print-level slips and one
  understated error term in a nine-page note are not a judgement about the
  source's reliability, and no artifact of this project may phrase them as
  one.
- S1 is not a correction of the author. The printed bound is true.
- No claim is made that no refereed version exists. Two independent searches
  surfaced none and no later arXiv version surfaced, but the submission
  history was not read. The correct statement is: none found.

---

## Section 7 -- Corpus-hygiene rule arising from this paper

Proposed to the operator, for booking in the ledger:

> Any project use of Lemma 2 of 1004.1072v1 carries the support annotation
> `unrefereed-preprint; printed statement differs from the statement the
> proof establishes; reading reconstructed and verified in-project`.

The point is operational, not pedantic. It is the difference between a
bound that may be cited and a bound that this project must re-derive before
anything load-bearing rests on it. `RelExtensionUpper` is load-bearing.

---

## Section 8 -- Open items

1. Confirm the printed strings of (2.10) and (2.12) against the anchored
   bytes rather than against a live fetch. This is r1 Task D and is the one
   step that closes I2.
2. 1004.1084v1 cites a preprint of the same author, "A note on small gaps
   between primes", with no identifier, and its (1.4) -- the inequality the
   note starts from -- rests on it. This is a gesture reference of the same
   class the item-0022 checklist registers for report 3, and it belongs in
   the same register.
3. Whether a refereed version of either note exists. Open; see Section 6.
4. Minor, recorded and not pursued: on p. 8 of 1004.1072v1 the letter
   $`r`$ is reused as the division remainder alongside the moment order
   of the same proof.

---

## Section 9 -- Provenance

Instruments I1 through I5 as tabulated in Section 1. The two blind image
readings were commissioned by the operator under an identical prompt, in
separate anonymous sessions, with PDF text tooling explicitly forbidden;
the reports and the prompt are anchored separately and are objects of
verification, never evidence. The symbolic computation was authored and run
by steering and is reproducible from the script in this directory. The
in-tree extract of 1004.1084v1 predates this paper and was not modified.

This paper contains no byte-exact instruction content and no pin. It is a
findings record, and its claims are classified in place.
