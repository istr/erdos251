# Item-0026 literature consolidation

Steering-authored 2026-07-25, operator-approved, landed at pin
`57e704643bd24fa982c6015d6a40477ef0cb739e`. Web OFF: every candidate
claim is read from a primary anchor booked in `payloads/HASHES.txt`, via
the seven extracts delivered at `97bf6d6` and the constants workpaper at
`2cea537`.

This supersedes an unlanded steering draft of 2026-07-24 in six places,
recorded as E1--E6 in Section 0. That draft was authored before the
extraction and carried two claims taken from review-run outputs and one
assumed constant; all three were wrong, in the same direction, and the
draft therefore over-priced how close the literature sits to S1. Section
0 is the operative part of this document. The draft itself is not in the
tree and is not an anchor; it circulated in steering and is cited here
only as the thing being corrected.

The draft carried a further section specifying `HANDOVER.md` deltas.
Those deltas were executed at commit `006a2c7` and booked as
ANN-20260725-67; the section is dropped here rather than kept as an
apparently open task list.

## Obstruction-language discipline (binding)

Every negative below is a located absence relative to a named inventory
of seven primary anchors, never an impossibility theorem. The Pintz
finding (Section 4) names a gap in a printed argument at its exact step
and does not assert that the theorem is false.

---

## 0. Errata against the 2026-07-24 draft

**E1 — the draft's axis A4 was ill-defined.** It read "A4 direction (upper /
non-concentration)". For the collision quantity these coincide, since
$`Q+(N-F-Q)=N-F`$ makes an upper bound on $`Q`$ the same statement as a
lower bound on cross mass. For moments of a counting function they do
not: a moment lower bound is a lower bound on spread, not an upper bound
on concentration at the modal middle. The extraction lane had to
interpret the axis and chose anti-concentration, correctly and
consistently. **A4 is object-bound from here on**, and the draft's
matrix is not load-bearing in that column.

**E2 — the draft mis-signed the Matomäki--Teräväinen window claim.** It argued
that the target window $`(\ln{}x)(\ln\ln{}x)`$ "lies strictly inside
$`(\log{}x)^{2.1}`$" and counted `2207.05038` as the strongest A2 hit.
That is backwards. An almost-all-intervals statement at a *longer*
window is a *weaker* statement and implies nothing at a shorter one. The
extraction verdict is `A2 FAILS` for `2207.05038`. The genuine
unconditional A2 hits are Teräväinen `1510.06005` and Matomäki
`2012.11565`, whose windows approach $`\log{}x`$ from above — the
opposite end of the same family from where the draft pointed.

**E3 — the draft's Pintz rank pricing is withdrawn.** It read Theorem 1' (1.8)
as admitting rank $`k\lesssim c_3(\log{}H)(\log{}\log{}H)`$ and tabulated
headroom 1.10 / 1.14 / 1.18 / 1.22 growing like $`\ln\ln\ln{}h`$. That
computation assumed $`c_3=1`$ to be a valid absolute constant. It is not
available (Section 4). The printed-proof ceiling is the regime boundary
$`k\le y=\tfrac56\log{}H`$, **linear in $`\log{}H`$**, and the demand
exceeds it at every tabulated scale.

**E4 — the draft's Kuperberg 1.2 pricing is withdrawn in part.** The displayed
$`(3\log{}k)^k`$ drops $`e^{\gamma}`$ per factor; the honest factor is
$`3e^{\gamma}\log{}k=5.343\log{}k`$, an added
$`2\gamma/\ln2=1.6655`$ in the exponent. Corrected against the anchored
F17.9 wall:

| $`x`$ | K1.2 as displayed | K1.2 honest | F17.9 wall | which is cheaper |
| --- | --- | --- | --- | --- |
| $`10^{8}`$ | 5.350 | 7.016 | 6.143 | **the wall** |
| $`10^{20}`$ | 5.699 | 7.364 | 6.932 | **the wall** |
| $`10^{100}`$ | 6.092 | 7.758 | 7.944 | K1.2 |
| $`10^{1000}`$ | 6.440 | 8.106 | 8.963 | K1.2 |

The draft claimed K1.2 is milder "by the factor 1.15--1.46 across the grid". It
is in fact **more expensive than the wall below about $`10^{100}`$**.
The qualitative reading survives — on the singular-series side S1 is a
priced cost, not an absence — but the quantification that made it
interesting does not.

**E5 — the draft over-claimed novelty for two shelf items.** It presented
Kuperberg Theorem 1.2 and Pintz Theorem 1' as material both review runs
had missed. Both were already extracted at `item-0017-workpapers/extract/`,
Theorem 1.2 with its own focus section. The real finding is narrower and
more useful: extracted material never reached the S1 axis pricing. That
is a routing defect in the project, not a gap in the shelf.

**E6 — the draft's H1 argument is withdrawn; H1 itself is downgraded.** See
Section 5.

---

## 1. The demand, and the six axes

`separator-repricing.md` W4.S1 deciding fact, verbatim, unchanged:

````text
> an unconditional averaged middle-slot non-concentration /
> upper-uniformity statement at rank $`k=(2/\ln2+o(1))\ln\ln{}x`$,
> window $`A'L\ln{}x`$, of strength enough to keep a fixed proportion
> of $`D0`$-depth site mass off its modal middle on some unbounded
> scale sequence per $`s`$ -- a statement that fails in the
> even-Cramer-smooth model.
````

| axis | demand | relaxed by `CG`? |
| --- | --- | --- |
| A1 rank | $`k\approx2.885\ln\ln{}x`$ | no ($`D0`$-forced) |
| A2 window | $`h\asymp(\ln{}x)(\ln\ln{}x)`$, **at** that length, not above | no |
| A3 grain | class masses $`N_{P,d}`$ of consecutive-gap words | no |
| A4 direction | for $`Q`$: upper $`\equiv`$ anti-concentration; for counting moments the two separate, and the demand is the **upper/anti-concentration on class mass** (E1) | no |
| A5 strength | constant order | yes |
| A6 density | sparse scales, no $`s`$-uniformity | yes |

## 2. Verdict

**NOT-FOUND at literature grain** for an exact unconditional S1 carrier;
no candidate clears all six axes, so no carrier is located and the
item-0010 campaign state is unchanged.

The informative form, and the one to use downstream:

> **A3 fails for all seven anchors.** The located absence is the
> *transfer* from singular-series averages and interval counts to
> consecutive-gap-word class masses — not a blanket corpus absence, and
> not an absence on the rank or window axes taken separately.

Sub-findings that survive from the draft: Kuperberg is the strongest direct
near miss; every conditional sighting at the right scale rests on a
uniform Hardy--Littlewood hypothesis; Maier is a regime filter, not a
killer.

## 3. Candidate matrix

Single source: the per-axis verdict table for all seven anchors lives in
`dossier/item-0026-workpapers/extraction-report.md`, section 5
("Consolidated per-axis verdict"). It is not reproduced here; a second
copy would drift.

What that table shows, and what is not stated alongside it there:

- **The distance to S1 is now measured, not estimated.** Jha clears rank
  and window *jointly*. What separates his conditional theorem from S1
  is a Hardy--Littlewood variant plus A3 — two named things, not an
  open-ended gap.
- **The unconditional frontier is further away than the draft
  suggested.** No unconditional anchor clears A1. The two that clear A2 do so by
  approaching $`\log{}x`$ on almost-prime objects, which is the wrong
  object at the right length.

## 4. The Pintz finding, and what it closes

The effectivization dispatch booked at ANN-20260725-66 asked for the
absolute constant $`c_2`$ in Pintz (1.8). The answer is that it is not recoverable from the printed proof in the
regime the theorem itself operates in. Governing display, verbatim from
`item-0017-workpapers/extract/pintz10-singser.md`:

````text
(2.3)  \Pi_3 = \prod_{p>y} ( 1 + O(k/p^2) ) = 1 + O( k/(y log y) ),
````

With $`y:=5\log{}H/6`$ the exact per-factor value is
$`\nu_p/((p-\nu_p)(p-1))`$, which is $`O(k/p^2)`$ only where
$`\nu_p/p`$ is bounded away from $`1`$, i.e. $`p\gg k`$. Theorem 1 lives
there. Theorem 1' does not: at its own threshold
$`H=\exp(c_2k/\log{}k)`$ one gets $`k/y=6\log{}k/(5c_2)\to\infty`$ for
every fixed absolute $`c_2`$, so the band $`y<p\le k`$ is non-empty and
carries per-factor deviations of order $`1`$. `PROVED`; steering
re-derived the identity and the ratio independently.

**Pricing.** On the $`D0`$ grid, $`k/y=1.85`$ / $`2.00`$ / $`2.19`$ /
$`2.38`$ at $`10^{8}`$ / $`10^{20}`$ / $`10^{100}`$ / $`10^{1000}`$ and
larger on the exact rank. The limit is
$`k/y\to(2/\ln2)/(5/6)=3.4625`$: the ratio converges from below to a
constant above $`1`$, so the clean regime $`k\le y`$ is **never entered
at any scale**. This is a regime boundary, not an additive threshold
shift, and growth alone does not cross it.

**What this is not.** Theorem 1' is plausibly true as stated: the
pointwise failure sits on a density-$`o(1)`$ set of extension positions,
and an averaging argument over good $`h`$ with CRT independence of the
small-prime factor plausibly rescues it. What the four-page note does
not carry is that argument. The weakest link in the finding is the CRT
construction exhibiting a tuple that realizes the failure — sketched,
not carried out. The gap itself does not depend on it; the
strengthening from "the proof does not show it" to "pointwise it is
false" does.

## 5. Hypotheses, re-ranked

### H1 — cross-mass reorientation: `DOWNGRADED`

The draft argued that the lower-bound direction is the one the literature
supplies at target rank. Both supports are gone. Pintz's floor is not
available at target rank (Section 4). And `dlbf20-moments.md` records
that the sparse-scale mechanism in de la Bretèche--Fiorilli is a
Kaczorowski--Pintz style RH dichotomy — direction-neutral, ineffective,
with the moment lower bound a downstream Hölder consequence of an
$`\Omega`$-result. There is no direction asymmetry in the literature to
exploit.

What remains is correct but thin: $`Q\le(1-\eta)N`$ and the cross-mass
lower bound are the *same statement*, so H1 is not a logical weakening.
It is a change of proof technique — second-moment/positivity methods
instead of sieve upper bounds — with no located instrument behind it.
Recommend it stay registered and unscheduled.

### H2 — Maier matrix at word grain on sparse scales: `UNCHANGED, now first`

Untouched by everything above, and it is the only hypothesis whose
target axis is A3, which the extraction identified as *the* located
absence. The case: the matrix method fixes residues modulo a primorial
and varies the row index, so a row family is structurally a flank class
with many members; and its characteristic defect — anomaly only along a
sparse sequence of $`x`$ — is exactly what A6 relaxation removes.

The decisive objection is unchanged and must be tested against the
method rather than against the located theorems: whether the row-average
anomaly converts into a positive proportion of classes with two distinct
realized middles, or only into an $`O(1)`$ existence statement.

### H3 — class-restricted Kuperberg cost: `WEAKENED but still cheap`

E4 removes most of the headroom H3 was reaching for: with the honest
constant, Theorem 1.2 is more expensive than the F17.9 wall below about
$`10^{100}`$, so a class-restricted analogue must recover more than the draft
assumed to reach (G1). It remains a budget-sheet-only question,
answerable at negligible cost, with either outcome a deliverable.
Recommend it run before H2 purely on cost grounds.

## 6. Recommendation

1. **H2 is the next substantive item.** It is the only registered
   hypothesis aimed at A3, and A3 is now the named absence. Propose it
   as a roadmap item with the positive-proportion question as its sole
   gate.
2. **H3 as a cheap precursor**, one sheet, closed either way.
3. **H1 stays registered, unscheduled**, with its literature leg struck.
4. **Consider whether Jha's hypothesis is the right target to study
   directly.** He is the only anchor clearing A1 and A2 jointly; the
   distance from his Hardy--Littlewood variant to what the project can
   assume is a measurable quantity and nobody has measured it.
5. **No re-scoping of item-0023** on H1's account; the Dispersion Arm
   should not inherit an argument that has been withdrawn.

## Both-readings appendix

- **The extraction result.** *Supporting:* seven primary anchors, 14
  independent verification agents, 0 errors, every mandatory statement
  quotable — this is the best-evidenced absence the project has
  produced. *Contradicting:* the absence is scoped to seven anchors
  chosen by two review runs that between them missed six shelf-resident
  items, so the inventory's completeness rests on the same search whose
  blind spots E5 documents.
- **The Pintz finding.** *Supporting:* the identity is exact, the regime
  computation is finite algebra, and both were re-derived independently.
  *Contradicting:* it is a gap in a printed argument, not a defect in a
  theorem; the rescue is plausible and standard; and the finding's
  strengthening step rests on an unexecuted construction.
- **Jha clearing A1 and A2.** *Supporting:* it converts an open-ended
  distance into two named obstacles. *Contradicting:* the hypothesis he
  assumes may be far stronger than anything the project could hope to
  assume, and nobody has measured how much stronger.
- **This document against the unlanded draft.** *Supporting:* every correction moves in the same
  direction — away from over-optimism — which is the direction errors
  of this kind usually need to move. *Contradicting:* six corrections in
  one revision is evidence that the draft's method (authoring from run outputs
  and sensitivity calculations before extraction) was not sound, and the
  same method has not been used since; that is a process reading, not a
  mathematical one.

## Residual uncertainty

- Pintz's $`c_1,c_2,c_3`$ remain `OPEN`, and the rescue argument is
  unverified in either direction.
- Kuperberg 1.2's implied constant in $`\ll`$ is still unexamined; the
  corrected columns price the displayed factor with the honest Mertens
  constant only.
- Every `even-Cramér` cell is `untested`. Whether any of the seven fails
  in the deterministic model — the separator property S1 also demands —
  is unknown, and no anchor speaks to it.
- H2's central claim (matrix rows are flank classes) is a structural
  reading of a method, `HEURISTIC`, contradicted by the located
  literature. It is proposed for adjudication because the two readings
  disagree.
- No search was performed beyond the anchored shelf in this revision.
