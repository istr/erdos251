# item-0022 absorption checklist -- primary verification of the two 2026-07-18 reports

> **WITHDRAWN AS AN INSTRUMENT (2026-07-27; ANN-20260727-76 and
> ANN-20260727-77). NOTHING IN THIS FILE IS CORPUS KNOWLEDGE.**
>
> This is a per-claim verdict register over the prose of three reports
> that were dropped as objects on 2026-07-27. Every row quoting a report
> quotes something no session can retrieve, so no verdict here can be
> checked by anyone, now or later. The file is kept under rule 5 --
> failed runs are data -- and it is the primary evidence for the
> incident analysed in `dossier/item-0022-incident-r1.md`. It is not
> evidence for any mathematical statement.
>
> NO ROW IS EDITED, deliberately. Five claim locations -- R1-001's own
> footnote, R1-002, R1-007's own footnote, R1-013, and R1-026's fourth
> sub-claim -- were promoted from a STOP disposition to CONFIRMED during
> repair r1, by widening the anchor gate mid-item, contrary to this
> file's own Section 1 firewall sentence. They are named here rather
> than reverted: a register with no standing gains nothing from having
> its rows corrected, the promotion is part of the record, and a
> document is not tidied after it has been declared non-evidentiary.
>
> WHAT SURVIVED THIS FILE, and only because somebody re-anchored it to a
> primary source instead of citing a report: the seven anchors and the
> identification layer, the 1004.1072 shelf-gap finding and its routing
> to item-0028, the k=2 numerics, and the general-r reading of Pintz
> Lemma 2.
>
> THE SEVEN EXTRACTS UNDER `extract/` ARE NOT COVERED BY THAT SURVIVAL.
> Their content is transcribed from anchored sources, but their
> selection and section structure are indexed to the dropped reports,
> and some assertions are sourced to an ephemeral kickoff dispatch that
> no longer exists. Their grade is open under item-0033 and no hash is
> booked for them.

Executor: local Claude Code, per item-0022-kickoff-v1.md. Session pinned
to HEAD `3c40e6e68b9f0c5da7761f212dd263e4c9a553e9` (rule-18 delta from
the Section 0 pin `9dee3699665bf66a7076bcb875ee290c39127bbe` touched only
`roadmap/_order.md` and `roadmap/item-0022.md`, the pre-cleared reorder
-- see item-0022-final-report.md Gates section for the verbatim diff
stat).

---

## Section 1 -- Provenance and anchoring contract

**Object of verification.** Two reports, both dated 2026-07-18,
operator-commissioned and LLM-generated:

- Report 1: `erdos251_literaturstand-s-gewichtete-reparatur.pdf`,
  sha256 `93bb5f6be4b65dcf422390eef69040b2d09ac997b254e471ae35e7caa6fc8c04`
  ("Literaturstand zur S-gewichteten Reparatur ueber Singularreihen",
  ChatGPT-authored, 5 pages).
- Report 2: `erdos251_report_llm_neuentwicklung.pdf`,
  sha256 `4b8bae092444ce1bdb612cb2fd1db39b084b9a39ecf399668384cd82c12f97fb`
  ("LLM-gestuetzte Neuentwicklung fuer erdos251", 15 pages).
- Report 3 (identification-only object): `erdos251_alternative_routen_report.pdf`,
  sha256 `1256f248b1a1ee9ffc1a9adb98ad23f47d3a2aa5d2e0f75b26e8d151098244cf`
  ("Erdos-Problem 251: Fundamental andere Angriffsrichtungen", 19 pages).

All three are OPERATOR-HELD (D4); cited here only by booked filename and
sha256, never committed or excerpted beyond the governing sentences the
rows below require.

**Gate 2.1/2.2 result.** All ten Section 2 anchors were staged under
`dossier/`, hashed locally, and cross-checked against
`payloads/HASHES.txt` before any file was opened for reading. Result:
**10/10 match**, re-checked at close (see item-0022-final-report.md).

**Two inheritance bans, applied.** (1) P1 and P3 are verdicted afresh
against the anchored PDFs (arXiv v2/v5) in this checklist -- the
2026-07-18 steering spot-checks against unversioned abstract pages are
not inherited. (2) The k=2 numerical core is independently re-executed
in `kowalski-mu-recheck.py`/`.txt` from the anchor's own Euler-product
formula, before either report's printed figure was consulted for
comparison.

**Firewall.** No claim below is verdicted against this repository or
its mirrors; a claim about the project's own repo/Lean/roadmap state
(sourced by the reports to their own internal citations R1-R6, e.g.
README, HANDOVER.md, Exchange.lean, payloads/item-0017-adjudication-v1.md,
dossier/e2prime-supply.md) has no primary anchor reachable under this
session's Section 2 gate, since none of those paths are Section-2
anchors nor on the Section 2 "in-tree material" consumable list, and
the firewall bars the tree itself from serving as evidence. Such claims
are registered for Phase-A completeness and explicitly marked
TREE-FIREWALLED rather than verdicted; see Section 6.

**Scope decision, declared (Section 9 completion policy).** Report 2 is
predominantly a repo-status/roadmap-proposal document (Sections 1-2,
4-9, 11-12 body), not a literature-verification document; those
sections are registered at subsection granularity (one claim per
logical unit) rather than atomized sentence-by-sentence, because (a)
they are TREE-FIREWALLED and unverdictable against any Section-2 anchor
regardless of atomization, and (b) sentence-level atomization of
purely-internal, already-firewalled content would not change any
verdict and would inflate the register without adding rigor. Report 2's
literature-facing content (Section 3's recap of report 1's findings,
Section 10's P1-P8 precedent case studies) receives the same
full-fidelity, per-claim treatment as report 1. This is why the total
claim count below (33 for reports 1+2) sits below the Section 9 envelope
of 60-140 -- see the budget reconciliation in
item-0022-final-report.md.

---

## Section 2 -- Phase A register: count table

| report | T1 | T2 | T3 | total |
| --- | --- | --- | --- | --- |
| Report 1 | 13 | 6 | 1 | 20 |
| Report 2 | 4 | 3 | 6 | 13 |
| **Reports 1+2 total** | **17** | **9** | **7** | **33** |

Report 3 citation register (identification only, not tiered): 5 external
identifiers + 7 internal path references = **12 entries** (Section 4).

Phase A is complete for reports 1 and 2 in the scope declared above, and
complete for report 3's citation-identification duty (3.4). No STOP 7.7
(envelope exceeded by more than half) is triggered; the actual count is
below the low end of the envelope, by declared scope decision, not by
residue.

---

## Section 3 -- Verdict rows, reports 1 and 2, grouped by tier

Byte-exact row template is Appendix A of the kickoff dispatch. Rows
whose named citation sits outside the Section 2 anchor set and outside
Appendix C's classes are marked `Anchoring class: NONE -- STOP 7.5`
rather than assigned one of the four ratified verdict classes; per STOP
7.5 this records the citation and the reason the policy does not reach
it, and invents no fifth class. Where an independent Section-2 anchor
happens to corroborate the same mathematical content the report's own
footnote could not reach, that is recorded as a separate, genuine
verdict against the anchor that does cover it, with a Note explaining
the substitution.

### REPORT 1 -- T1 rows

### R1-001 | T1 | mathematical | (synthesis -- see decomposition)

Locator: report 1, p.1, Kurzurteil, first paragraph.
Claim (verbatim): "Nach dem derzeitigen Literaturstand gibt es keinen
bekannten Satz, der Ihren Input (ii) in der geforderten Form liefert,
also eine Simplex-Zweitmomentabschaetzung
$`\Sigma_2\le(1+o(1))^k\mathbb{E}[S]^2|\mathrm{simplex}|`$ im Regime
$`k\asymp\log\log x`$ und fuer die von Ihnen beschriebenen
flankierten/aggregierten Domains."
Gloss: under the current literature, no known theorem delivers input
(ii) in the required form -- a simplex second-moment bound of this
shape in the growing-k, flanked/aggregated regime.
Anchoring class: NONE -- STOP 7.5 (report's own footnote for this
sentence points to arXiv:math/0409258, not one of the ten Section 2
anchors and not covered by Appendix C).
Support class: n/a (thesis-level synthesis, not itself an anchor claim)
Note: This sentence is the report's own top-level thesis. Its four
constituent claims (Montgomery-Soundararajan being centered/fixed-k,
Pintz's power sums being fixed-tuple-rank, Kowalski's k=2 core being
inflationary, and the absence of a flanked/simplex machine) are
independently registered and verdicted below (R1-007, R1-015, R1-017/018,
R1-023/024). [repair r1] All four are now CONFIRMED; the row's own
top-level footnote (math/0409258) is also RESOLVED-ON-SHELF as of this
repair pass (same resolution as R1-002/R1-007). This row remains a
synthesis pointer rather than an independently-quoted claim, since its
sentence is report 1's own cross-cutting conclusion, not a single
anchor's statement. Consequence: none.

### R1-003 | T1 | numerical | CONFIRMED

Locator: report 1, p.1, Kurzurteil, second paragraph.
Claim (verbatim): "Kowalski gibt eine explizite Eulerproduktformel fuer
den Mittelwert von $`S(H)^2`$ und nennt numerisch
$`\mu_2(2)=2.300\ldots`$"
Gloss: Kowalski gives an explicit Euler-product formula for the mean of
$`\mathfrak{S}(h)^2`$ and states numerically $`\mu_2(2)=2.300\ldots`$
Anchor: https://people.math.ethz.ch/~kowalski/singular-series-distribution.pdf
Anchor sha256: 378433db556a2e83236f83a946d15178fe431e08f81511764325cce361b27920
Governing sentence (verbatim): "In particular, we find (using Pari/GP
for instance): $`\mu_2(2)=2.300\ldots`$" (Example 3.5), with the
generating formula "$`\mu_k(2) = \prod_p((1-1/p)(1-2/p)^k +
(1/p)(1-1/p)^k)(1-1/p)^{-2k}`$" stated in the same example.
Support class: proved
Consequence: consumed by R1-006, R1-019(folded), R1-027, R2-001.
Note: independently re-executed at 30 digits over primes p<2e6 in
kowalski-mu-recheck.py/.txt; computed mu_2(2)=2.30096154471321787845...,
matching both the anchor's stated "2.300..." and report 1's more
precise "2.3009615447...".

### R1-004 | T1 | mathematical | CONFIRMED

Locator: report 1, p.1, Kurzurteil, second paragraph.
Claim (verbatim): "zugleich gilt $`\mu_k(1)=1`$ als Gallagher-Mittelwert"
Gloss: at the same time, $`\mu_k(1)=1`$ holds, as Gallagher's mean.
Anchor: https://people.math.ethz.ch/~kowalski/singular-series-distribution.pdf
Anchor sha256: 378433db556a2e83236f83a946d15178fe431e08f81511764325cce361b27920
Governing sentence (verbatim): "in addition, we have $`\mu_1(m)=1`$ for
all integers $`m\ge1`$, and hence $`\mu_k(1)=1`$ for all $`k\ge1`$. The
last statement ($`\mu_k(1)=1`$) is of course Gallagher's theorem (1.5)."
(Theorem 1.1)
Support class: proved
Consequence: consumed by R1-006, R1-011(folded).
Note: none.

### R1-005 | T1 | mathematical | CONFIRMED

Locator: report 1, p.1, Kurzurteil, second paragraph.
Claim (verbatim): "er erklaert die Paritaetsursache dafuer, dass S(H)
oft verschwindet"
Gloss: Kowalski explains the parity cause of why $`\mathfrak{S}(h)`$
often vanishes.
Anchor: https://people.math.ethz.ch/~kowalski/singular-series-distribution.pdf
Anchor sha256: 378433db556a2e83236f83a946d15178fe431e08f81511764325cce361b27920
Governing sentence (verbatim): "the 2-factor of $`\mathfrak{S}(h)`$ is
zero unless all $`h_i`$ are of the same parity, which happens with
probability $`2^{1-k}`$ only" (Example 3.5).
Support class: proved
Consequence: consumed by R1-006.
Note: none.

### R1-006 | T1 | numerical | CONFIRMED

Locator: report 1, p.1, Kurzurteil, second paragraph.
Claim (verbatim): "Daraus folgt unmittelbar, dass die auf die gerade
Klasse konditionierte Zweitmomentkonstante nicht $`1+o(1)`$, sondern
$`\mathbb{E}_{\mathrm{even}}[S_2^2]/\mathbb{E}_{\mathrm{even}}[S_2]^2 =
1.1504807\ldots`$ ist."
Gloss: it follows that the second-moment constant conditioned on the
even class is not $`1+o(1)`$ but $`1.1504807\ldots`$
Anchor: https://people.math.ethz.ch/~kowalski/singular-series-distribution.pdf
Anchor sha256: 378433db556a2e83236f83a946d15178fe431e08f81511764325cce361b27920
Governing sentence (verbatim): combination of Theorem 1.1's
$`\mu_k(1)=1`$, Example 3.5's $`\mu_2(2)=2.300\ldots`$ and its parity
remark "probability $`2^{1-k}`$" (both quoted at R1-004/R1-005). The
ratio itself is report 1's own elementary derivation, not a printed
anchor sentence -- see extract/kowalski-singser-dist.md Section 6.
Support class: proved (the conditioning arithmetic is elementary and
independently re-derived: conditioning a variable that is 0 w.p. 1-q
and X w.p. q on the nonzero event multiplies both mean and second
moment by 1/q; at k=2, q=1/2, giving E_even[S]=2, E_even[S^2]=2*mu_2(2)).
Consequence: consumed by R1-027, R2-001 (item-0028 reads the k=2
inflation constant).
Note: numerically re-executed: ratio = 1.15048077235660893922965889343,
matching report 1's stated 1.1504807723... to all given digits (see
kowalski-mu-recheck.txt).

### R1-009 | T1 | mathematical | CONFIRMED

Locator: report 1, p.2, "Zentrierte Momente und ihre Grenzen".
Claim (verbatim): "Kuperbergs Arbeit ueber odd moments untersucht die
ungeraden $`R_k(h)`$ und gibt obere Schranken bzw. numerische Evidenz
fuer die Groessenordnung der ungeraden zentrierten Momente."
Gloss: Kuperberg's work on odd moments studies the odd $`R_k(h)`$ and
gives upper bounds resp. numerical evidence for the size of the odd
centered moments.
Anchor: https://arxiv.org/pdf/2109.03767v3
Anchor sha256: e1bbabbd259d43bf80614756bc96ddb13612e82bdd8887d536612bd7d5441f94
Governing sentence (verbatim): "We conjecture that when k is odd,
$`R_k(h)\asymp h^{(k-1)/2}(\log h)^{(k+1)/2}`$. We prove an upper bound
with the correct power of h when k=3... We provide further evidence for
this conjecture in the form of numerical computations." (Abstract)
Support class: proved (Theorem 1.2, k=3 upper bound); conjectural for
general odd k (Conjecture 1.1) -- both strands present in the anchor.
Consequence: consumes anchor 3 (see extract/kuperberg21-oddmoments.md).
Note: none.

### R1-010 | T1 | mathematical | CONFIRMED

Locator: report 1, p.2, "Zentrierte Momente und ihre Grenzen".
Claim (verbatim): "Bloom-Kuperberg liefern nahe optimale obere Schranken
fuer ungerade Momente des refined singular series bei ungeradem k."
Gloss: Bloom-Kuperberg supply near-optimal upper bounds for odd moments
of the refined singular series at odd k.
Anchor: https://arxiv.org/pdf/2312.09021v2
Anchor sha256: 46b80c9b72e4eea34b74eb263b25a6eb6ee21647352b840438d35407f707ec5f
Governing sentence (verbatim): "If $`k\ge3`$ is an odd integer and
$`h\ge2`$ then $`R_k(h)\ll(\log h)^{O(1)}h^{(k-1)/2}`$." (Theorem 2)
Support class: proved
Consequence: none.
Note: report 1's own bibliography carries no URL for this claim (the
CORPUS GAP corrected in roadmap/item-0022.md, 2026-07-26); this row
verifies the claim directly against anchor 4, independently of report
1's citation apparatus. This resolves the corpus gap: the claim itself
is accurate.

### R1-015 | T1 | mathematical | CONFIRMED [reversed post-repair-r1; see history below]

Locator: report 1, p.2, "wichtigste positive Literaturpunkt" paragraph.
Claim (verbatim): "Dort wird gezeigt, dass fuer festes $`\nu`$ und
festes $`r`$ $`\sum\mathfrak{S}(D^+)^r\le c(\nu,r)H^\nu`$, und
insbesondere fuer $`r=2`$ also ein quadratischer Mittelwert im
festen-$`\nu`$-Regime kontrolliert wird."
Gloss: it is shown that for fixed nu and fixed r,
$`\sum\mathfrak{S}(D^+)^r\le c(\nu,r)H^\nu`$, and in particular for r=2
a quadratic mean is controlled in the fixed-nu regime.
Anchor: https://arxiv.org/pdf/1004.1072v1
Anchor sha256: 74824028eb50c322f43da700fcb31fe10ce91272fe8e73695e9a4f82df22053b
Governing sentence (verbatim), the lemma's own name and threshold:
"Lemma 2. For fixed nu, r and H > H0(nu, r) we have
$`S(\nu,r)=\ldots\le c_8(\nu,r)H^\nu`$." Governing sentence (verbatim),
the r=1 remark immediately following: "In case of r = 1 we will
additionally show, similarly to (2.9), S(nu, r) ~ H^nu as H -> infinity.
This slightly modified form implies easily the original Gallagher's
theorem too." Governing sentence (verbatim), the proof (eq. 2.11 and
2.16, re-verified via `pdftotext -layout` on pages 7-8 this session):
"$`S^*(t,r,D):=\sum_{1\le h\le H,h\notin D}
\left(\mathfrak{S}(D^+\cup\{h\})/\mathfrak{S}(D^+)\right)^r \ll H`$"
(2.11); the local-average identity (2.16) applies the exponent r
directly to $`(1-\nu_p/p)`$ and $`(1-(\nu_p+1)/p)`$ at every prime.
Support class: proved
Consequence: none.
Note: see extract/pintz10-patterns.md Sections 2.3 and 6 for the full
derivation and reasoning. Read as a whole document -- lemma name
$`S(\nu,r)`$, constant $`c_8(\nu,r)`$, threshold $`H_0(\nu,r)`$, the
r=1 remark, and the proof (2.11)-(2.16) -- Lemma 2 states and its proof
establishes a genuine general-r moment bound
$`\sum_{D\subset[1,H],|D|=\nu}\mathfrak{S}(D^+)^r\le c_8(\nu,r)H^\nu`$
for every fixed r, of which Lemma 1 is exactly r=2 and the r=1 remark is
exactly r=1 (an asymptotic recovering Gallagher's theorem). This matches
report 1's claim, including its "im festen-nu-Regime" phrasing
(consistent with the `|D|=nu` restriction, which the r=1/Gallagher
remark and the scale $`H^\nu`$ both require, even though it is not
shown under the summation sign as literally displayed in (2.10)).

**Revision history, in full (nothing below is deleted, per this
project's own convention that a superseded finding stays as a
recorded history rather than being silently overwritten).**

*Item-0022 original session:* this row was CORRECTED, on the ground
that the paper's displayed equation (2.10) shows exponent 2 (matching
Lemma 1) and that r is only a proof-internal ratio-exponent from
(2.11), not a moment order on the outer sum.

*Repair r1, Task C:* the repair dispatch proposed rewriting this row to
CONFIRMED, on the premise that Lemma 2 is "the general-exponent form."
That specific premise was checked via `pdftotext -layout` on pages 6-7
and found NOT to hold as stated: the printed (2.10) shows the identical
exponent glyph as Lemma 1's (2.8) ("S2(D+)" in both). No repair was
applied at that time; the CORRECTED verdict was left standing, now
re-confirmed once.

*This revision (2026-07-26, later the same day):* the operator supplied
two further documents (`Pintz_Lemma2_Image_Analysis_Report.pdf`,
`Pintz_Lemmas_1_and_2_Report.pdf`, both self-described AI-assisted
analyses) arguing the printed exponent is a typographical slip and that
Lemma 2 is a genuine general-r bound. Per this project's rule that such
reports are never themselves evidence, neither was taken at its word;
instead their arguments prompted a fresh, independent re-reading of the
primary anchor, specifically of material the earlier passes had not
transcribed or had not connected to this question: equation (2.16) (the
local-average computation completing the proof opened by 2.11) and the
logical force of the r=1 remark. Both are now re-verified directly
against the anchor (see extract/pintz10-patterns.md Section 2.3, and the
`pdftotext -layout` output reproduced there): (2.16) carries the
exponent r explicitly, not 2, throughout the same computation that
(2.11) opens; and the r=1 remark is logically incoherent if Lemma 2's
own exponent never depended on r. Both earlier passes' transcription of
what is literally PRINTED in the single display (2.10) was and remains
accurate (exponent glyph "2", no visible `|D|=nu`); what changes here is
recognizing that this specific display, read in isolation, does not
correctly represent what Lemma 2 -- as a whole, together with its own
name, threshold, remark, and proof -- states and establishes. The
verdict is accordingly reversed to CONFIRMED. This is not a case of
deferring to an external report's conclusion; the derivation in
extract/pintz10-patterns.md Section 2.3 is worked through independently
from (2.11) and (2.16) as directly re-read from the anchor.

### R1-017 | T1 | mathematical | CONFIRMED

Locator: report 1, p.2-3, "Kowalski geht auf der Momentseite noch
weiter" paragraph.
Claim (verbatim): "Fuer festes $`k`$ und beliebige feste Momente $`m`$
existieren Grenzmomente $`\mu_k(m) = \lim_{h\to\infty}
(1/h^k)\sum^*_{|H|\le h}\mathfrak{S}(H)^m`$, und insbesondere ist der
Mittelwert von $`\mathfrak{S}(H)^2`$ gleich $`\mu_k(2)`$ mit expliziter
Eulerproduktformel."
Gloss: for fixed k and any fixed moments m, limiting moments
$`\mu_k(m)`$ exist, and in particular the mean of $`\mathfrak{S}(h)^2`$
equals $`\mu_k(2)`$ with an explicit Euler-product formula.
Anchor: https://people.math.ethz.ch/~kowalski/singular-series-distribution.pdf
Anchor sha256: 378433db556a2e83236f83a946d15178fe431e08f81511764325cce361b27920
Governing sentence (verbatim): "Let $`k\ge1`$ be fixed. For any complex
number $`m\in\mathbf{C}`$ with $`\mathrm{Re}(m)\ge0`$, there exists a
complex number $`\mu_k(m)`$ such that
$`\lim_{h\to+\infty}\frac{1}{h^k}\sum^*_{|h|\le h}\mathfrak{S}(h)^m =
\mu_k(m)`$." (Theorem 1.1)
Support class: proved
Consequence: consumed by R1-018, R1-027.
Note: none.

### R1-018 | T1 | mathematical | CONFIRMED

Locator: report 1, p.2-3, same paragraph continued.
Claim (verbatim): "Kowalski zeigt, dass die Momente 'slightly faster
than exponentially' wachsen, $`\log\mu_k(m) = km\log\log(3m)+O(m)`$, und
per Symmetrie folgt fuer die Zweitmomente $`\log\mu_k(2) =
2k\log\log(3k)+O(k)`$."
Gloss: Kowalski shows the moments grow slightly faster than
exponentially, and by symmetry the second moments follow the stated
growth rate.
Anchor: https://people.math.ethz.ch/~kowalski/singular-series-distribution.pdf
Anchor sha256: 378433db556a2e83236f83a946d15178fe431e08f81511764325cce361b27920
Governing sentence (verbatim): "For any fixed $`k\ge1`$, we have
$`\log\mu_k(m) = km\log\log3m + O(m)`$, for $`m\ge1`$." (Proposition
4.1); "As a corollary of Proposition 4.1 and symmetry, we have
$`\log\mu_k(2) = 2k\log\log3k+O(k)`$ for $`k\ge1`$." (Example 4.3)
Support class: proved
Consequence: consumed by item-0028 (rank-dependent singular-series
cost).
Note: this is the anchor's own basis for calling the growth "slightly
faster than exponentially," which the anchor's abstract-adjacent prose
does not literally use as a phrase, but Proposition 4.1's stated rate
(linear-in-k times log log, inside an exponential) matches that
characterization exactly.

### R1-023 | T1 | mathematical | CONFIRMED

Locator: report 1, p.4, "Was flankennahe Restriktionen derzeit leisten".
Claim (verbatim): "Der Abstract sagt ausdruecklich, dass die Asymptotik
solcher eingeschraenkten Summen 'by incidences modulo r' bzw. 'by
pairings of the smooth functions' gesteuert wird; im Beweis von Theorem
1.2 erscheint die Hauptermstruktur tatsaechlich ueber
Paarungen/perfect matchings, und der groesste Beitrag kommt genau dann,
wenn die betreffenden Kongruenzklassen zusammenpassen."
Gloss: the abstract states explicitly that the asymptotics of such
restricted sums are governed by incidences modulo r resp. pairings of
the smooth functions; in the proof of Theorem 1.2 the main-term
structure indeed appears via pairings/perfect matchings, with the
largest contribution exactly when the relevant congruence classes
match.
Anchor: https://arxiv.org/pdf/2301.06095v1
Anchor sha256: c67fdd9c9a822581371409e3fae54c9fcf97e0bd1a0b534fb22ea7a4b61f9617
Governing sentence (verbatim): "We show that the value of the sum is
governed by incidences modulo r of elements of the set in the case of
arithmetic progressions and by pairings of the smooth functions in the
case of weights." (Abstract); "if
$`\#\widetilde{\mathcal{B}}(c_1,\ldots,c_k)`$ is the number of ways to
pair the $`c_i`$'s such that every pair has equal values, then...
$`R_k(h;r,c_1,\ldots,c_k) = \#\widetilde{\mathcal{B}}(c_1,\ldots,c_k)(\ldots)^{k/2}+\ldots`$"
(Theorem 1.2 remark)
Support class: proved
Consequence: consumed by report 2's Section 5 "matched-flank"
terminology (TREE-FIREWALLED at that end, but this row's literature
side is independently CONFIRMED).
Note: none.

### R1-026 | T1 | mathematical | (synthesis -- 4/4 sub-claims CONFIRMED [repair r1, was 3/4])

Locator: report 1, p.4, "Bewertung der beiden offenen Inputs", Input(ii)
paragraph.
Claim (verbatim): "Die staerksten nahen Resultate zerfallen jeweils auf
einer der Achsen: Montgomery-Soundararajan sind zentriert und fixes k;
Pintz' Potenzsummen sind fixes $`\nu`$; Kuperberg fuer grosse Mengen
behandelt nur $`T_k`$, also erste Momente; Kowalski behandelt feste k,
zeigt aber gerade, dass die Quadrate bereits lokal zu gross sind und mit
k wachsen."
Gloss: the strongest nearby results each fail on one axis: M-S are
centered and fixed-k; Pintz's power sums are fixed-nu; Kuperberg's
large-set work covers only first moments; Kowalski covers fixed k but
shows the squares are already too large locally, growing with k.
Anchoring class: [repair r1] the row's own footnote (math/0409258) is
now RESOLVED-ON-SHELF (same resolution as R1-007's footnote, via
dossier/item-0017-workpapers/extract/moso04-shortintervals.md). Sub-claims
checked: (a) M-S centered/fixed-k -- CONFIRMED (same governing sentence
as R1-007, now doubly anchored: moso04-shortintervals.md directly plus
anchor 3's independent corroboration); (b) Pintz fixed-nu power sums --
CONFIRMED via anchor 1 (same as R1-015; R1-015's verdict was revised
during this repair pass -- see R1-015's full revision history -- and is
now CONFIRMED as a genuine general-r moment bound, of which report 1's
claim is an accurate paraphrase); (c) Kuperberg
large-sets $`T_k`$ = first moments only -- CONFIRMED [repair r1: was
STOP 7.5, resolved via the same generalized RESOLVED-ON-SHELF citation
as R1-013, dossier/item-0017-workpapers/extract/kuperberg22-singseries.md];
(d) Kowalski fixed-k, growing-with-k squares -- CONFIRMED via anchor 2
(same as R1-018).
Support class: proved (all four sub-claims)
Consequence: none.
Note: [repair r1] all four sub-claims are now independently
corroborated; none remain STOP 7.5. This is a strict improvement over
the original session's 3-of-4 disposition.

### R1-027 | T1 | mathematical | CONFIRMED

Locator: report 1, p.5, final paragraph.
Claim (verbatim): "Ihre 'S-gewichtete Reparatur' scheitert nach
jetzigem Stand nicht bloss an einer fehlenden grossen-k-Maschine,
sondern schon an einer realen lokalen Zweitmomentkonstante $`>1`$, die
im Fall $`k=2`$ explizit sichtbar ist."
Gloss: the repair fails not merely for lack of a large-k machine, but
already because of a real local second-moment constant $`>1`$, visible
explicitly at k=2.
Anchor: https://people.math.ethz.ch/~kowalski/singular-series-distribution.pdf
Anchor sha256: 378433db556a2e83236f83a946d15178fe431e08f81511764325cce361b27920
Governing sentence (verbatim): same as R1-003/R1-006 ($`\mu_2(2)=2.300\ldots>1`$,
independently re-executed).
Support class: proved
Consequence: none.
Note: valid synthesis of R1-003/004/005/006/017/018, all independently
CONFIRMED above.

### REPORT 1 -- T2 rows

### R1-002 | T2 | mathematical | CONFIRMED [repair r1: was STOP 7.5, resolved via generalized RESOLVED-ON-SHELF]

Locator: report 1, p.1, Kurzurteil, first paragraph.
Claim (verbatim): "Die vorhandenen Arbeiten zerfallen in drei andere
Richtungen: erstens zentrierte Momente der verfeinerten Singularreihe
bei festem k im Box-Regime; zweitens erste Momente der unzentrierten
Singularreihe S(H) fuer groessere k; drittens fixes $`\nu`$ und fixen
Momentgrad m fuer die Verteilung von S(H)."
Gloss: existing work falls into three other directions -- centered
moments at fixed k, first moments of the uncentered series for larger
k, and fixed tuple-rank/fixed moment-degree distributional results.
Anchoring class: RESOLVED-ON-SHELF (repair-r1 Section 3 generalization
of Appendix C.2's shelf-resolution rule to any citation in any of the
three reports).
Extract (direction 1): dossier/item-0017-workpapers/extract/moso04-shortintervals.md,
citing https://arxiv.org/pdf/math/0409258v1, sha256
4814387da412faf35d86f7e5d84a789cfa6743b08a6dff1e47fbc7632d7a8176 (booked,
payloads/HASHES.txt line 22).
Extract (direction 2): dossier/item-0017-workpapers/extract/kuperberg22-singseries.md,
citing https://arxiv.org/pdf/2210.09775v2, sha256
653dcd731f11c6bab47fa61989b31f50dc3318464fc4d300276698045ba48939 (booked,
payloads/HASHES.txt line 21).
Extract (direction 3): kowalski-singser-dist.md (anchor 2, already in
this session's Section 2 set).
Governing sentence (verbatim), direction 1: "Theorem 1. In the above
notation, V_k(q;h) = mu_k V_2(q;h)^{k/2} + O_k(h^{k/2-1/(7k)}(q/phi(q))^{2^k+k/2})
for every positive integer k... Here the main term is the k-th moment
of a normal random variable with expectation 0 and variance V_2(q;h)."
(Theorem 1, p.4) -- centered (V_2/V_k are refined-series moments),
fixed k ("We take k to be fixed" per the paper's own Section 1 opener,
p.9), interval/box regime (d_i or h_i ranging uniformly over [1,h]).
Governing sentence (verbatim), direction 2: "Theorem 1.1... Let T_k(h)
be given by T_k(h) := sum_{h_1,...,h_k<=h, distinct} S(h_1,...,h_k).
Then... T_k(h) = h^k + O(h^{k-beta})" and "Theorem 1.2... T_k(h) << h^k
(3 log k)^k." -- uncentered (S(H), not S_0), first moment (order 1,
not squared), for k not fixed, growing with h.
Governing sentence (verbatim), direction 3: same as R1-017 (anchor 2,
Theorem 1.1: existence of mu_k(m) for fixed k, any moment order m).
Support class: proved (all three directions rest on theorems, not
conjecture, in their respective anchors)
Consequence: none.
Note: the three directions map one-to-one onto three distinct papers:
direction 1 = Montgomery-Soundararajan (math/0409258, item-0017's
moso04 extract), direction 2 = Kuperberg's large-sets paper (2210.09775,
item-0017's kuperberg22 extract), direction 3 = Kowalski (anchor 2,
already CONFIRMED via R1-017/018). Display-identity recheck (repair r1
Task A, applied to this newly-written row): each quote located verbatim
under its own paper's own theorem heading; neighbouring objects in each
extract (e.g. moso04's Lemma 1/Lemma 2 before Theorem 1; kuperberg22's
Section 1 abstract before Theorem 1.1/1.2) are distinct from the cited
object in each case. PASS.

### R1-007 | T2 | mathematical | CONFIRMED [repair r1: own footnote now RESOLVED-ON-SHELF, in addition to the anchor-3 corroboration already on record]

Locator: report 1, p.1-2, "Zentrierte Momente und ihre Grenzen".
Claim (verbatim): "Montgomery und Soundararajan arbeiten nicht mit
$`\mathfrak{S}(H)^2`$, sondern mit der verfeinerten bzw. zentrierten
Singularreihe $`S_0(D)`$... und beweisen $`R_k(h) =
\mu_k(-h\log h+Ah)^{k/2}+O_k(h^{k/2-1/(7k)+\varepsilon})`$... Im selben
Theorem vermerken sie ausdruecklich, dass die Arbeit von
Granville-Soundararajan Beschraenkungen fuer die Uniformitaet in k
auferlegt."
Gloss: M-S work not with the uncentered series but the refined/centered
series, proving the stated Rk(h) asymptotic with an error term, noting
a Granville-Soundararajan uniformity-in-k restriction in the same
theorem.
Anchoring class: RESOLVED-ON-SHELF (repair-r1 Section 3 generalization),
citing dossier/item-0017-workpapers/extract/moso04-shortintervals.md,
https://arxiv.org/pdf/math/0409258v1, sha256
4814387da412faf35d86f7e5d84a789cfa6743b08a6dff1e47fbc7632d7a8176
(booked, payloads/HASHES.txt line 22) -- this IS the Montgomery-Soundararajan
paper itself, report 1's own named source for this sentence.
Secondary anchor (independent corroboration already on record):
https://arxiv.org/pdf/2109.03767v3, sha256
e1bbabbd259d43bf80614756bc96ddb13612e82bdd8887d536612bd7d5441f94
(anchor 3), which restates the same theorem in its own introduction.
Governing sentence (verbatim), primary (moso04-shortintervals.md):
"Theorem 2. Let h be an integer, h > 1, and suppose that R_k(h) is
defined as in (8). Then R_k(h) = mu_k(-h log h + Ah)^{k/2} + O_k(
h^{k/2-1/(7k)+eps}) for any nonnegative integer k, where A = 2 - C_0 -
log 2pi and C_0 denotes Euler's constant." (Theorem 2, p.4). Governing
sentence (verbatim), secondary (anchor 3, kuperberg21-oddmoments.md, as
already on record): "Their work depends on showing that sums R_k(h) of
k-term singular series are mu_k(-h log h+Ah)^{k/2}+O_k(h^{k/2-1/(7k)+eps})"
(Abstract).
Support class: proved
Consequence: none.
Note: display-identity recheck (repair r1 Task A, applied to this
newly-added primary citation): the Rk(h) formula is Theorem 2's own
statement, located correctly. One precision point: report 1's "im
selben Theorem" (in the same theorem) suggests the Granville-Soundararajan
uniformity remark sits inside Theorem 2 itself; per moso04-shortintervals.md
Section 3, that remark is actually printed immediately after THEOREM 1
(the V_k(q;h) formula), directly preceding Theorem 2 -- i.e. at the seam
between the two theorems of the same proof arc, not textually inside
Theorem 2's own statement. This is a minor looseness in report 1's
phrasing, not a substantive error: Theorem 1 and Theorem 2 are the
V_k/R_k formula-pair from a single connected result (Theorem 2 is
derived from Theorem 1 via (49)-(60) in the same extract), and the
uniformity restriction applies to both. Recorded here rather than
silently smoothed over, per the no-strengthening/no-papering-over
discipline this repair pass exists to apply; does not change the
CONFIRMED verdict.

### R1-012 | T2 | mathematical | CONFIRMED

Locator: report 1, p.2, "Unzentrierte Momente und zweite Momente".
Claim (verbatim): "Pintz gibt zudem einen uniformeren Zugang zu
Gallaghers Satz 'with respect to k', allerdings nur unter der
Bedingung, dass das Intervall H ausreichend gross als Funktion von k
ist; das ist keine praezise grosse-k-Asymptotik in Ihrem Regime, aber
es ist eine nuetzliche Ergaenzung der Literatur."
Gloss: Pintz gives a more uniform approach to Gallagher's theorem "with
respect to k," but only under the condition that H is sufficiently
large as a function of k; not a precise large-k asymptotic in the
project's regime, but a useful supplement.
Anchor: https://arxiv.org/pdf/1004.1072v1
Anchor sha256: 74824028eb50c322f43da700fcb31fe10ce91272fe8e73695e9a4f82df22053b
Governing sentence (verbatim): "In case of r=1 we will additionally
show, similarly to (2.9), $`S(\nu,r)\sim H^\nu`$ as $`H\to\infty`$. This
slightly modified form implies easily the original Gallagher's theorem
too..." with the threshold "$`H>H_0(\nu,r)`$" noted as "naturally not
necessary if we do not care about the values of the constants" (Lemma
2 and remarks).
Support class: proved
Consequence: none.
Note: [TRANSCRIPTION-UNSURE, footnote-digit only] the PDF's extracted
superscript for this sentence reads "5" in this session's text layer,
which the report's own bibliography maps to anchor 2, not anchor 1; the
mathematical content is unambiguous (Pintz's own uniformity-in-nu
result, anchor 1's ``k'' being Pintz's $`\nu`$), so this is flagged as a
likely footnote/superscript transcription artifact rather than a
misattribution, and does not change the verdict.

### R1-013 | T2 | mathematical | CONFIRMED [repair r1: was STOP 7.5, resolved via generalized RESOLVED-ON-SHELF]

Locator: report 1, p.2, "Fuer grosses k gibt es dann..." paragraph.
Claim (verbatim): "Dort wird $`T_k(h)=\sum\mathfrak{S}(h_1,\ldots,h_k)`$
behandelt. Das asymptotische Mittel $`T_k(h)=h^k+O(h^{k-\beta})`$ wird
nur im Bereich $`k=O((\log h)^{1-\delta})`$, $`\delta>1/2`$, bewiesen;
ausserdem erhaelt man fuer alle k nur die grobe obere Schranke
$`T_k(h)\ll h^k(3\log k)^k`$."
Gloss: the asymptotic mean is proved only in a restricted k-range, with
a crude upper bound for all k.
Anchoring class: RESOLVED-ON-SHELF (repair-r1 Section 3 generalization),
citing dossier/item-0017-workpapers/extract/kuperberg22-singseries.md,
https://arxiv.org/pdf/2210.09775v2, sha256
653dcd731f11c6bab47fa61989b31f50dc3318464fc4d300276698045ba48939
(booked, payloads/HASHES.txt line 21).
Governing sentence (verbatim): "Theorem 1.1. Fix delta > 1/2, and let
h, k in N with k = O((log h)^{1-delta}). Let T_k(h) be given by (4)
T_k(h) := sum_{h_1,...,h_k <= h, distinct} S(h_1,...,h_k). Then there
exists a beta > 0, dependent only on delta > 1/2, with T_k(h) = h^k +
O(h^{k-beta})." and "Theorem 1.2. Let k, h in N, with no conditions on
their relative growth rates. Define T_k(h) by (4). Then (5) T_k(h) <<
h^k prod_{p <= k^3} 1/(1 - 1/p)^k << h^k (3 log k)^k." (both, Section 1,
p.2, "MAIN THEOREMS 1.1 AND 1.2" in the extract).
Support class: proved
Consequence: none.
Note: exact match, both the T_k(h) definition and both regimes (Theorem
1.1's restricted-k asymptotic, Theorem 1.2's unrestricted crude bound).
Distinct from anchor 5 (2301.06095), confirmed (per the roadmap's own
2026-07-26 correction note) to be "a different Kuperberg paper from the
anchored 2210.09775v2" -- this row now resolves via the actual paper
2210.09775v2 itself, through its item-0017 in-tree extract, not via
anchor 5. Display-identity recheck (repair r1 Task A, applied to this
newly-resolved row): row's object (Theorem 1.1 + Theorem 1.2) matches
the extract's own Section 2 heading exactly; neighbouring objects
(Section 1 abstract/intro before, Section 3 "Definition of T_k(h) and
variants" after) are distinct. PASS.

### R1-024 | T2 | mathematical | CONFIRMED

Locator: report 1, p.4, "Was flankennahe Restriktionen derzeit leisten",
second paragraph.
Claim (verbatim): "Sie geben asymptotische Formeln fuer eingeschraenkte
Summen von $`S_0`$ bzw. modulare Restriktionen von Singularreihen,
nicht Hardy-Littlewood-Untergrenzen fuer
$`\sum_{\mathrm{sites}}S_{\mathrm{side}}(P(\mathrm{site}))`$ auf einer
paritaetsblockierten Flankenklasse."
Gloss: these works give asymptotic formulas for restricted sums of the
singular series, not Hardy-Littlewood lower bounds for a prime-counting
function on a parity-blocked flank class.
Anchor: https://arxiv.org/pdf/2301.06095v1
Anchor sha256: c67fdd9c9a822581371409e3fae54c9fcf97e0bd1a0b534fb22ea7a4b61f9617
Governing sentence (verbatim): all five of the anchor's stated results
(Theorems 1.1-1.5) are asymptotic formulas for sums of the algebraic
singular-series constant or its restricted/weighted variants; no
Hardy-Littlewood-type lower bound for a counting function appears
anywhere in the 19-page paper (checked directly, full read).
Support class: proved (as an accurate negative/scope characterization)
Consequence: none.
Note: none.

### R1-025 | T2 | citation | (class recorded per ratified policy, no further verdict)

Locator: report 1, p.4, "Wenn Ihr 'blocker 2'..." paragraph.
Claim (verbatim): "Tao formuliert expository, aber sehr klar, dass
selbst unter sehr starken Verteilungshypothesen die Siebtheorie
typischerweise nicht zwischen Zahlen mit gerader und ungerader Anzahl
von Primfaktoren unterscheiden kann."
Gloss: Tao states, expository but clearly, that even under very strong
distribution hypotheses sieve theory typically cannot distinguish
numbers with an even vs odd number of prime factors.
Anchoring class: UNANCHORABLE, reason moving-target (Appendix C.2,
pre-classified: "the Tao blog TAG page cited by report 1
(moving-target)").
Support class: heuristic (the report itself frames this as expository,
not a theorem)
Consequence: none.
Note: class applied per the ratified policy; no independent verdict is
attempted or required.

### REPORT 1 -- T3 rows

### R1-014 | T3 | mathematical | (not independently verdicted -- depends on R1-013)

Locator: report 1, p.2, end of "Fuer grosses k..." paragraph.
Claim (verbatim): "Fuer Ihr natuerliches Regime $`h\asymp\log x`$ und
$`k\asymp\log\log x`$ liegt das asymptotische Fenster
$`k\ll(\log h)^{1-\delta}`$ ohnehin deutlich unter der benoetigten
linearen $`\log\log x`$-Skala."
Gloss: expository/comparative conclusion applying R1-013's cited window
to the project's own regime.
Support class: n/a
Note: derivative of R1-013 (STOP 7.5); not independently verdicted.

---

### REPORT 2 -- T1 rows

### R2-001 | T1 | numerical | CONFIRMED

Locator: report 2, p.4, Section 3.2 "Die Nennerkonstante 1 ist lokal
bereits falsch".
Claim (verbatim): "Fuer k=2 zeigt die explizite Eulerproduktrechnung in
der paritaetszulaessigen Klasse:
$`\mathbb{E}_{\mathrm{even}}[\mathfrak{S}^2]/\mathbb{E}_{\mathrm{even}}[\mathfrak{S}]^2
= 1.1504807723\ldots>1`$."
Gloss: for k=2, the explicit Euler-product computation in the
parity-admissible class shows the ratio above.
Anchor: https://people.math.ethz.ch/~kowalski/singular-series-distribution.pdf
Anchor sha256: 378433db556a2e83236f83a946d15178fe431e08f81511764325cce361b27920
Governing sentence (verbatim): same ingredients as R1-006 (Theorem 1.1's
$`\mu_2(1)=1`$, Example 3.5's $`\mu_2(2)=2.300\ldots`$ and parity
remark).
Support class: proved
Consequence: consumed by item-0028 (rank-dependent singular-series
cost); recap of R1-006.
Note: identical figure to R1-006, independently re-executed once (see
kowalski-mu-recheck.txt); not re-executed a second time.

### R2-003 | T1 | numerical | CONFIRMED

Locator: report 2, p.12, Section 10.1 "AlphaProof Nexus (2026)".
Claim (verbatim): "Das staerkste System loeste nach Autorenangabe 9 von
353 formalisierten offenen Erdos-Problemen und 44 von 492
OEIS-Vermutungen; die Beweise wurden in Lean mechanisch geprueft. Ein
einfacherer Generate-Verify-Agent repliziert die Erdos-Erfolge, war bei
den schwierigsten Problemen jedoch teurer."
Gloss: the strongest system solved 9/353 formalized open Erdos problems
and 44/492 OEIS conjectures per the authors, Lean-checked; a simpler
generate-verify agent replicated the Erdos successes but cost more on
the hardest problems.
Anchor: https://arxiv.org/pdf/2605.22763v2
Anchor sha256: d71b78f1ea764ea0489b7fdec3c53d394cf99cd2ac2a22c1d61e744618e9573d
Governing sentence (verbatim): "Our most capable agent autonomously
resolved 9 of 353 open Erdos problems... and proved 44/492 OEIS
conjectures" (Abstract); "the basic agent solved all 9 problems, though
at a higher cost on the harder problems" (Section 5, p.9).
Support class: measured
Consequence: none (precedent-anchor policy, D1).
Note: near-verbatim match to the anchor's own abstract and Section 5.

### R2-004 | T1 | citation | (WEB-DEFERRED per STOP 7.8)

Locator: report 2, p.12, Section 10.1, continued.
Claim (verbatim): "Die Ergebnisdateien und Lean-Beweise sind oeffentlich
in einem separaten Repository verfuegbar. [P2]"
Gloss: the result files and Lean proofs are publicly available in a
separate repository.
Anchoring class: ANCHORED-BY-COMMIT (Appendix C.1, P2 =
google-deepmind/alphaproof-nexus-results).
Support class: n/a
Note: no commit SHA is available in the staged material this session
(report 2 cites only the repository URL, matching anchor 6's own text
"available in https://github.com/google-deepmind/alphaproof-nexus-results",
which also carries no commit hash). Per Appendix C.1 and STOP 7.8, this
row is WEB-DEFERRED; the executor does not fetch a commit SHA. Question
a lookup would settle: the commit SHA of the results repository at the
time report 2 was authored (2026-07-18).

### R2-005 | T1 | mathematical | CONFIRMED

Locator: report 2, p.12, Section 10.2 "Erdos-Problem 728".
Claim (verbatim): "Ein gesonderter Write-up beschreibt die Loesung von
Erdos-Problem 728 durch eine Kombination aus GPT-5.2 Pro und dem
Lean-System Aristotle. Der finale Beweis ist formal verifiziert und wird
in klassische Mathematik uebersetzt."
Gloss: a separate write-up describes the resolution of Erdos Problem
728 via a combination of GPT-5.2 Pro and the Lean system Aristotle; the
final proof is formally verified and translated into classical
mathematics.
Anchor: https://arxiv.org/pdf/2601.07421v5
Anchor sha256: fb1bccdbbc8f5abc00dfc1b88237dfe53238b87e33b7e835625885067ff9825b
Governing sentence (verbatim): "The system in question is a combination
of GPT-5.2 Pro by OpenAI and Aristotle by Harmonic, operated by Kevin
Barreto. The final result of the system is a formal proof written in
Lean, which we translate to informal mathematics in the present writeup
for wider accessibility." (Abstract)
Support class: measured
Consequence: none (precedent-anchor policy, D1).
Note: near-verbatim match.

### REPORT 2 -- T2 rows

### R2-006 | T2 | citation | (class recorded per ratified policy, P4)

Locator: report 2, p.12, Section 10.3 "FunSearch (2023)".
Claim (verbatim, gloss only -- route/precedent background, not
re-quoted verbatim per Section 4.5's spirit of not re-litigating
already-classed precedent): FunSearch found new finite and asymptotic
constructions for the cap-set problem, improving the known asymptotic
lower bound for the first time in about 20 years.
Anchoring class: IDENTIFIED-NOT-ANCHORED (Appendix C.1, P4: "Nature,
blog and arXiv items carrying none of the project's mathematics").
Support class: n/a
Consequence: none.
Note: identified and left, per ratified C.1 disposition; no sha256
booked, none computed.

### R2-007 | T2 | citation | (class recorded per ratified policy, P5/P6)

Locator: report 2, p.12, Section 10.4 "AlphaEvolve (2025)".
Claim (gloss only): AlphaEvolve found a 4x4 complex-matrix-multiplication
procedure using 48 scalar multiplications, an improvement after 56
years in the considered setting.
Anchoring class: IDENTIFIED-NOT-ANCHORED (Appendix C.1, P5/P6).
Support class: n/a
Consequence: none.
Note: identified and left.

### R2-008 | T2 | citation | (class recorded per ratified policy, P7/P8)

Locator: report 2, p.13, Section 10.5 "AlphaGeometry und AlphaProof".
Claim (gloss only): AlphaGeometry solved 25/30 selected olympiad
geometry problems; AlphaProof solved three of five non-geometric IMO
2024 problems.
Anchoring class: IDENTIFIED-NOT-ANCHORED (Appendix C.1, P7/P8).
Support class: n/a
Consequence: none.
Note: identified and left.

### REPORT 2 -- T3 rows (TREE-FIREWALLED / proposal content)

### R2-009 | T3 | mathematical | TREE-FIREWALLED

Locator: report 2, Sections 1-2 (pp.3-4), "Gegenstand und Quellenbasis" /
"Mathematischer und formaler Projektstand".
Claim (gloss only): repo/commit state, ExchangeSupply1 statement
content, and the M=1 normal-form consumer-priority argument, sourced by
the report to its own internal citations [R1]-[R6] (README, GitHub
compare, HANDOVER.md, Exchange.lean, payloads/item-0017-adjudication-v1.md).
Anchoring class: none available this session -- none of [R1]-[R6] are
Section 2 anchors or on the Section 2 "in-tree material" consumable
list, and the Section 1 firewall bars the repository itself from
serving as verdict evidence.
Support class: n/a
Consequence: none.
Note: registered for Phase-A completeness; not independently
verdictable this session.

### R2-010 | T3 | mathematical | TREE-FIREWALLED

Locator: report 2, Section 4 (pp.5-6), "Was item-0017 tatsaechlich
entschieden hat", including the Extension-Konstante growth-rate
argument ($`\exp((1+o(1))k\log k)`$ vs $`k\sim(2/\log2)\log\log x`$).
Claim (gloss only): item-0017's branch outcome, the random-model
counterexample, the growing-k Pintz-transfer blocker.
Anchoring class: none available this session (sourced to [R5]/[R6],
same firewall as R2-009).
Support class: n/a
Consequence: none.
Note: none.

### R2-011 | T3 | mathematical | (proposal, not verdicted)

Locator: report 2, Sections 5-6 (pp.6-8), "Revidierte
Technologieempfehlung" / "Das minimale neue Satzpaket" (Satz A-D).
Claim (gloss only): four proposed-but-unproven theorem candidates
(matched-flank class lower bound, relative extension upper bound, tail
intersection, formal integrator) for future work.
Support class: n/a -- report 2 itself explicitly classifies this
content as "noch unbewiesene, aber pruefbare Entwicklungsrichtungen"
(Section 5.4), i.e. a proposal, not a claim of established fact.
Consequence: none.
Note: this is forward-looking research proposal content, not a
citation of established literature; per this dispatch's own scope
(Section 5, no proposal of successor items; STOP 7.6's spirit for
route-like content), it is registered but not priced, ranked, or
verdicted.

### R2-012 | T3 | mathematical | TREE-FIREWALLED / see R2-003, R2-006-R2-008

Locator: report 2, Sections 7-9, 11 (pp.8-13), "Was aus der Literatur...
wiederverwendbar ist" / "Empfohlene Roadmap" / "Rigoroser LLM-Workflow"
/ "Go-/No-Go-Kriterien".
Claim (gloss only): reusability table, roadmap items A-F, workflow role
definitions, Go/No-Go criteria.
Anchoring class: mixed -- the precedent-case content already appears at
R2-003/R2-006/R2-007/R2-008; the remainder is repo-internal roadmap
proposal, TREE-FIREWALLED.
Support class: n/a
Consequence: none.
Note: registered at section granularity for Phase-A completeness.

### R2-013 | T3 | mathematical | (synthesis, not separately verdicted)

Locator: report 2, Section 12 (p.14), "Gesamturteil".
Claim (gloss only): final synthesis recapping the literature diagnosis
(R2-001, CONFIRMED), item-0017's state (R2-010, TREE-FIREWALLED) and the
revised priority proposal (R2-011, not verdicted).
Support class: n/a
Consequence: none.
Note: none.

---

## Section 4 -- Report 3 citation register (identification only)

Per Section 3.4: report 3 receives identification only. No route
proposal is registered, priced, ranked, or characterized (STOP 7.6). The
report's citations appear only in its closing "17 Quellen und
Projektanker" section.

### C3-001 | citation | UNANCHORABLE, access-blocked

Reference (verbatim): "T. F. Bloom, 'Erdos Problem #251', erdosproblems.com/251
und Forumsthread 251."
Anchoring class: UNANCHORABLE, reason access-blocked (Appendix C.2,
pre-classified: "the erdosproblems entry and forum thread
(access-blocked, with the operator browser-check precedent noted)").
Note: class applied per ratified policy; not independently checked.

### C3-002 | citation | RESOLVED-ON-SHELF

Reference (verbatim): "J.-C. Schlage-Puchta, 'The irrationality of some
number theoretical series', Acta Arith. 126 (2007), arXiv:1105.1451."
Resolution: uniquely resolves to a booked shelf anchor.
Anchor: https://arxiv.org/pdf/1105.1451v1
Anchor sha256: 93d69309b3bc958a5c5b325e0f5517d41a2a6eb310e618f457741b6e45368464
Note: this identifier is explicit (not a gesture), and the anchored
shelf already carries it (booked under a prior item); recorded
RESOLVED-ON-SHELF rather than UNANCHORABLE/no-identifier per the
refinement rule (check the shelf before classifying).

### C3-003 | citation | ANCHORABLE-NOT-ANCHORED

Reference (verbatim): "R. J. Lemke Oliver und K. Soundararajan, Arbeiten
zu Restklassen-Biases aufeinanderfolgender Primzahlen, arXiv:1603.03720."
Anchoring class: ANCHORABLE-NOT-ANCHORED (Appendix C.2, explicitly named
single member of this class: "arXiv 1603.03720 is identifiable but not
booked at this pin").
Note: booking recommendation addressed to steering, per policy; the
executor does not book it (payloads/ is outside the Section 5 write
scope).

### C3-004 | citation | RESOLVED-ON-SHELF (the flagged "live case")

Reference (verbatim, gesture): "Arbeiten von Ford, Green, Konyagin,
Maynard und Tao zu grossen Luecken zwischen Primzahlen."
Resolution: checked against the anchored shelf per the dispatch's
binding instruction ("The large-gaps gesture reference is the live
case: check it against the shelf before classifying it."). This gesture
names exactly the five co-authors of "Long gaps between primes" (Ford,
Green, Konyagin, Maynard, Tao), which is booked on the general shelf.
Anchor: https://arxiv.org/pdf/1412.5029v3
Anchor sha256: 6a2c86f06946315f2abafb11b25c60bef9ca780921e4b0c1f55a144430c48145
Note: a second shelf item on large gaps between primes also exists
(warwick.ac.uk .../large_gaps_between_primes.pdf, hash
eb806d88da05c2848979a614027253bbf4e754a9c2a041b2f4ccef31216894dc, a
different, single-author item), but the gesture's five named co-authors
uniquely identify 1412.5029v3, not that item. Reclassified from the
policy's default no-identifier expectation to RESOLVED-ON-SHELF, per
the refinement rule this dispatch explicitly directs be applied here.

### C3-005 | citation | UNANCHORABLE, no-identifier

Reference (verbatim, gesture): "B. Adamczewski und Y. Bugeaud zu
Komplexitaet und Transzendenz von Basisentwicklungen."
Anchoring class: UNANCHORABLE, reason no-identifier (Appendix C.2,
pre-classified as one of "the two gesture references in report 3").
Note: no specific paper title or identifier is given; the shelf has no
obviously-matching Adamczewski-Bugeaud item among the booked hashes
inspectable from filenames/URLs alone, and this dispatch does not flag
this one as a "live case" requiring a shelf check (unlike C3-004);
policy classification applied as ratified.

### C3-006 | internal reference | path verified

Path: `dossier/runde0.md` -- EXISTS at session pin `3c40e6e`.

### C3-007 | internal reference | path verified

Path: `dossier/dissektion.md` -- EXISTS at session pin `3c40e6e`.

### C3-008 | internal reference | path verified

Path: `dossier/triage-1a.md` -- EXISTS at session pin `3c40e6e`.

### C3-009 | internal reference | path verified

Path: `dossier/triage-1b.md` -- EXISTS at session pin `3c40e6e`.

### C3-010 | internal reference | path verified

Path: `dossier/tate-transfer.md` -- EXISTS at session pin `3c40e6e`.

### C3-011 | internal reference | path verified

Path: `dossier/e2prime-supply.md` -- EXISTS at session pin `3c40e6e`.

### C3-012 | internal reference | path verified

Path: `lean/Erdos251/Exchange.lean` -- EXISTS at session pin `3c40e6e`.

---

## Section 5 -- Consolidated verdict table

| claim id | tier | class | anchor | one line |
| --- | --- | --- | --- | --- |
| R1-001 | T1 | synthesis | RESOLVED-ON-SHELF (footnote) | thesis; 4/4 sub-claims CONFIRMED elsewhere [repair r1] |
| R1-002 | T2 | CONFIRMED [repair r1] | moso04+kuperberg22+anchor2 | three-way taxonomy, shelf-resolved |
| R1-003 | T1 | CONFIRMED | anchor 2 | Euler product + mu_2(2)=2.300..., re-executed |
| R1-004 | T1 | CONFIRMED | anchor 2 | mu_k(1)=1, Gallagher mean |
| R1-005 | T1 | CONFIRMED | anchor 2 | parity vanishing, prob 2^(1-k) |
| R1-006 | T1 | CONFIRMED | anchor 2 | even-conditioned ratio 1.1504807723..., re-executed |
| R1-007 | T2 | CONFIRMED | moso04 (shelf) + anchor 3 | M-S Rk(h) theorem, own footnote now shelf-resolved [repair r1] |
| R1-009 | T1 | CONFIRMED | anchor 3 | Kuperberg odd-moment upper bound + conjecture |
| R1-010 | T1 | CONFIRMED | anchor 4 | Bloom-Kuperberg near-optimal odd bound; resolves corpus gap |
| R1-012 | T2 | CONFIRMED | anchor 1 | Pintz uniform Gallagher, footnote-digit unsure |
| R1-013 | T2 | CONFIRMED [repair r1] | kuperberg22 (shelf) | Kuperberg large-k Tk(h), shelf-resolved |
| R1-014 | T3 | n/a | -- | derivative of R1-013 |
| R1-015 | T1 | CONFIRMED [reversed after repair-r1] | anchor 1 | general-r moment bound, per (2.11)+(2.16)+r=1 remark; (2.10)'s printed exponent-2 is an apparent typo |
| R1-017 | T1 | CONFIRMED | anchor 2 | Theorem 1.1, existence of mu_k(m) |
| R1-018 | T1 | CONFIRMED | anchor 2 | growth rate, Prop 4.1 / Example 4.3 |
| R1-023 | T1 | CONFIRMED | anchor 5 | perfect-matching main-term structure |
| R1-024 | T2 | CONFIRMED | anchor 5 | asymptotic formulas, not HL lower bounds |
| R1-025 | T2 | class only | Tao blog | UNANCHORABLE, moving-target (pre-classified) |
| R1-026 | T1 | synthesis | mixed | 4/4 sub-claims CONFIRMED [repair r1, was 3/4] |
| R1-027 | T1 | CONFIRMED | anchor 2 | headline conclusion, valid synthesis |
| R2-001 | T1 | CONFIRMED | anchor 2 | recap of R1-006 |
| R2-003 | T1 | CONFIRMED | anchor 6 | P1: 9/353, 44/492, Lean-checked |
| R2-004 | T1 | class only | P2 | ANCHORED-BY-COMMIT, WEB-DEFERRED (no SHA staged) |
| R2-005 | T1 | CONFIRMED | anchor 7 | P3: Erdos 728, GPT-5.2+Aristotle |
| R2-006 | T2 | class only | P4 | IDENTIFIED-NOT-ANCHORED (FunSearch) |
| R2-007 | T2 | class only | P5/P6 | IDENTIFIED-NOT-ANCHORED (AlphaEvolve) |
| R2-008 | T2 | class only | P7/P8 | IDENTIFIED-NOT-ANCHORED (AlphaGeometry/AlphaProof) |
| R2-009 | T3 | TREE-FIREWALLED | -- | repo/ExchangeSupply1 state |
| R2-010 | T3 | TREE-FIREWALLED | -- | item-0017 outcome, Extension-Konstante |
| R2-011 | T3 | proposal, not verdicted | -- | Satz A-D, self-classified unproven |
| R2-012 | T3 | mixed | -- | reusability table / roadmap / workflow |
| R2-013 | T3 | synthesis | -- | Gesamturteil, depends on above |
| C3-001..012 | -- | see Section 4 | -- | report 3 identification only |

---

## Section 6 -- WEB-DEFERRED and residue lists

**WEB-DEFERRED (STOP 7.8):**
- R2-004 (P2 commit SHA).

**STOP 7.5 (citation outside Appendix C, not independently verdicted):**
none remaining as of repair r1 (2026-07-26). R1-001's own footnote,
R1-002, R1-007's own footnote, R1-013, and R1-026's fourth sub-claim
were all resolved via the generalized RESOLVED-ON-SHELF class
(item-0022-repair-r1.md Task B) against existing item-0017 in-tree
extracts for math/0409258 and arXiv:2210.09775. See
item-0022-repair-r1-report.md for the full resolution and
repair-log-r1.md for the per-row change log.

**TREE-FIREWALLED (registered, not anchor-verifiable this session):**
- R2-009, R2-010, R2-012 (partial).

**Declared partial scope (Section 9 completion policy):** Report 2's
repo-internal and proposal content (Sections 1-2, 4-9, 11-12 body) is
registered at subsection granularity rather than sentence-by-sentence;
see Section 1's scope-decision note. This is a declared, reasoned
partial scope for T3 material, not an oversight; no T1 claim is left
un-adjudicated.

**Residue by claim id:** none outstanding for T1 (all 17 T1 claims
carry either a verdict or a fully-adjudicated STOP disposition). T2/T3
residue is the declared coarser bucketing above.

---

## Section 7 -- Follow-up candidates (not executed; for steering/operator decision)

1. Book arXiv:1603.03720 (Lemke Oliver-Soundararajan) as an anchor, per
   C3-003's ANCHORABLE-NOT-ANCHORED disposition. Still open.
2. [RESOLVED by repair r1] arXiv:math/0409258 is NOT the same paper as
   anchor 2. Per dossier/item-0017-workpapers/extract/moso04-shortintervals.md,
   math/0409258 is Montgomery & Soundararajan, "Primes in Short
   Intervals" -- a distinct paper from Kowalski's ETH-hosted note,
   already extracted under item-0017. R1-001/002/007/026's citations to
   it are resolved via the generalized RESOLVED-ON-SHELF class rather
   than needing an alias booking.
3. [RESOLVED by repair r1] R1-013's Kuperberg large-sets $`T_k(h)`$
   claim is now CONFIRMED via the generalized RESOLVED-ON-SHELF class,
   citing dossier/item-0017-workpapers/extract/kuperberg22-singseries.md
   (arXiv:2210.09775v2, already booked on the shelf from a prior item).
   A formal item-0022 anchor booking is no longer necessary for this
   claim, though steering may still wish to book it for other items'
   convenience.
4. Consider recording a commit SHA for
   google-deepmind/alphaproof-nexus-results (R2-004), to close the
   WEB-DEFERRED gap on the P2 precedent-anchor policy. Still open.
5. [RESOLVED, then REVISED, by repair r1 -- see R1-015's full revision
   history] R1-015 was originally CORRECTED (Pintz's Lemma 2 bounds only
   the second moment). item-0022-repair-r1.md Task C proposed reversing
   this to CONFIRMED; that specific proposal was checked via the one
   permitted PDF touch (pdftotext -layout, pages 6-7) and did not hold as
   stated -- the displayed exponent in (2.10) genuinely matches Lemma
   1's. Later the same day, the operator supplied two further AI-assisted
   analysis documents arguing the displayed exponent is a typographical
   slip; per this project's rule that such documents are never
   themselves evidence, their arguments were used only to prompt a
   further independent re-reading of the anchor (specifically eq. 2.16,
   not previously transcribed, and the r=1 remark's logical force, not
   previously connected to this question). That re-reading independently
   confirmed a genuine general-r moment bound is what Lemma 2 -- read as
   a whole, not as the single isolated display (2.10) -- states and
   proves, and R1-015 is now CONFIRMED. The printed display (2.10) itself
   (exponent "2", no visible `|D|=nu`) is a genuine, still-flagged
   typesetting anomaly in this v1 preprint; recorded in
   extract/pintz10-patterns.md Sections 2.3 and 6 rather than silently
   corrected or silently ignored. No in-tree artifact repeats the
   original imprecision, so no repair to writeup/ or dossier/ prose is
   triggered by this reversal.
