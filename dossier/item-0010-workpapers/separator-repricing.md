# Separator re-pricing audit (item-0010)

Date: 2026-07-24. Author: item-0010 executor (EXECUTOR lane, Claude
Code, local machine; model string `claude-opus-4-8[1m]`). Against the
item-0010 kickoff v2 (operator-supplied, ephemeral, never committed).
Web OFF and cloud OFF for the entire session (corpus-only; evidence
firewall honored -- no external literature, no steering triage document,
no answer key entered). Local computation only. Zero edits under
`lean/`; no `lake` invocation; no roadmap edit; no new measurement run.

## Evidence labels (load-bearing; repository meanings)

`FORMAL` -- proved in the checked Lean tree. `PROVED-DOSSIER` -- a
complete repository proof at dossier grain, no Lean supplier theorem.
`PROVED` -- finite algebra proved in this workpaper. `MEASURED` --
computed on the frozen census/registry. `HEURISTIC`, `MODEL-ONLY`,
`OPEN`, `UNMEASURED` retain their usual repository meanings. Every
verdict clause of W6 carries its class inline.

## Obstruction-language discipline (binding, B1)

Every negative below is a **located obstruction relative to a named
inventory**, never an impossibility theorem, and never a claim that any
endpoint is unprovable. Scope qualifiers, quantifier order, constants,
and dependency declarations are preserved verbatim from their anchors;
no mathematical statement is strengthened during exposition.

---

## W0. Gates and continuity (verbatim)

- `git rev-parse HEAD` = `60ba5f1b2eaef19108e7e40d1b164fc0d3b78cb8`
  == the Section 0 pin EXACTLY. `git diff <pin>..HEAD` is empty: there
  is no rule-18 delta at all (HEAD is the pin). The expected
  bookkeeping movement -- removal of `item-0021` from
  `roadmap/_order.md` -- is already folded into the pin commit
  (`60ba5f1 chore: park roadmap item-0021`); nothing content-path
  differs. No STOP-AND-REPORT condition 1 fires.
- Section 2 anchors: all ten sha256 verified byte-identical at session
  start (`relext-upper.md`, `relext-statements.md`, item-0020
  `proofs.md` / `mechanism-inventory.md` / `item-0020-final-report.md`
  / `budget_sheet_20.py`, item-0010 `collision-gap-audit.md` /
  `m5-lite-audit.md` / `flank-collision-singleton-frontier-audit.md`,
  `literature.md`). No condition 2.
- `python3 lean/scripts/blocks.py check-frozen` -> "FROZEN BLOCKS: all
  byte-identical." (`erdos_251_irrational`, `HLQuantA`,
  `CramerGranville`). PASS.
- `python3 lean/scripts/blocks.py relocation-check` -> "RELOCATION
  CHECK PASSED -- concatenation is byte-identical to the old body."
  PASS.
- Sorry census: exactly one proof-term `sorry`, at
  `lean/Erdos251/Statement.lean:21`; every other occurrence of the
  token in `lean/` is prose inside a docstring (`Statement.lean:8`,
  `Counting.lean:13`, `Counting.lean:90`). Every other file zero. PASS.
- mathlib pin `a6276f4c6097675b1cf5ebd49b1146b735f38c02` (`inputRev`
  `v4.16.0`) intact in `lean/lake-manifest.json`. PASS.
- `lean-toolchain` ends `"leanprover/lean4:v4.16.0\n"` (single trailing
  newline). PASS.
- `roadmap/item-0010.md`: `status: ratified`. PASS.

No condition 3. Working tree clean except the untracked ephemeral
kickoff file (operator input, never committed).

---

## W1. Public status page update (mechanical; record only)

Executed immediately after W0, before reading any Section 2 anchor
content, per the kickoff's placement. Two byte-exact replacements in
`writeup/status.md`, taken verbatim from the fenced kickoff text; no
paraphrase, no extension, nothing derived from this session's own work.
Replacement 1 (the $`1/64`$-relativization paragraph, inserted after
"...`B2.pairs` itself remains open.") and Replacement 2 (the Section 6
measurement paragraph) each matched their anchor string exactly once.

W1 gates after replacement: zero bare inline `$...$`; zero raw `\log`
outside `\log{}`/`\log_`; no trailing whitespace; non-ASCII exactly the
four pre-existing characters (e-acute, o-double-acute, and the
two curly quotation marks); `git diff --stat`
shows `writeup/status.md` and nothing else (12 insertions, 1 deletion).
No condition 4. Post-W1 sha256 of `writeup/status.md`:
`335eb6ea026ab2a41ac6e48f31e034da2f72d5597e0e62415fc71fa1b8120c6d`.

STOP condition 7 note: the W1 text is fixed and sourced entirely from
pre-pin ledger entries (ANN-20260722-58, -59, -61, ANN-20260724-62,
-63). Nothing in W2--W6 below was allowed to influence it. Where this
session's own work bears on the W1 text, it is recorded in W6, not
edited into `status.md`.

---

## W2. Endpoint demand ledger

Three endpoints, each restated byte-exactly from its anchor, then
reduced to its **minimal quantitative demand**: the weakest
`(strength, uniformity, scale-density)` triple that suffices for the
downstream `ExchangeSupply1`. The rule-15 arithmetic is in
`budget_sheet_20_ext.py` table T8. Throughout,
$`N=N(x,s)=\lvert S_x^{\prime(s)}\rvert`$,
$`F=F(x,s)=\lvert\mathrm{Fam}(S_x^{\prime(s)})\rvert`$, and
$`Q=Q(x,s)`$ is the class-normalized collision statistic.

### W2.1 `B2.pairs` (baseline, for comparison only)

Anchor (`relext-upper.md` Section 2; `mechanism-inventory.md` M1.c;
`proofs.md` C3). For every $`\varepsilon>0`$ there is
$`x_8(\varepsilon)`$ such that for all $`x\ge x_8`$ and all
$`s\ge0`$:

$$
Q(x,s)=\sum_{P\in\mathrm{Fam}(S_x^{\prime(s)})}\frac1{N_P}
\sum_{\substack{d\ge2 \cr 2\mid d}}N_{P,d}(N_{P,d}-1)
\ \le\ \varepsilon\,\lvert S_x^{\prime(s)}\rvert .
$$

Minimal demand triple. **Strength:** $`Q/N\to0`$ (every fixed
$`\varepsilon>0`$ eventually). The minimal strength that feeds the
current pigeonhole is weaker than the stated $`\varepsilon\to0`$: the
exchange needs $`\varepsilon_{\mathrm{REU}}<\delta/2`$, hence a fixed
pair coefficient $`c<(\delta/2)^2`$, which at the proved
$`\delta=1/2`$ is $`c<1/16`$ (the recorded $`1/64=(\delta/4)^2`$
is convenient slack, `PROVED-DOSSIER` through C3). **Uniformity:** one
threshold $`x_8`$ uniform in $`s`$ ($`s`$ inside $`x`$).
**Scale-density:** all large $`x`$ (eventual). Consumes: an
$`s`$-uniform constant and an eventual-in-$`x`$ statement.

### W2.2 `CG` = `CollisionGapAlongScales` (the weakest endpoint)

Anchor (`collision-gap-audit.md` A / C.4; ANN-20260722-58):

$$
\tag{CG}
\forall s\ \exists\eta_s\in(0,1]\ \forall X\ \exists x\ge X:\quad
0<N(x,s),\qquad Q(x,s)\le(1-\eta_s)N(x,s),
$$

equivalently $`\liminf_{x\to\infty}Q(x,s)/N(x,s)<1`$ for each fixed
$`s`$ after eventual positivity. Minimal demand triple.
**Strength:** constant-order -- any fixed $`0\le c_s<1`$
($`\eta_s=1-c_s>0`$); **not** $`c\to0`$. **Uniformity:** none in
$`s`$ ($`\eta_s`$ may depend on $`s`$). **Scale-density:**
sparse -- one favorable scale per threshold $`X`$ on an unbounded
integer sequence, per fixed $`s`$ (a $`\liminf`$, not a limit).

What `CG` does **not** consume (recorded explicitly, kickoff W2): no
$`s`$-uniform constant; no statement valid at all large $`x`$; no
global $`x`$-threshold; no $`\varepsilon\to0`$; and at integration
time neither `MatchedFlankLower` nor `RelExtensionUpper`. The exact
finite criterion behind (CG) is $`Q<N-F`$ (PROVED, `collision-gap-audit`
B.3: $`N-F-Q=\sum_P(2/N_P)\sum_{d<e}N_{P,d}N_{P,e}\ge0`$), and
$`F/N\to0`$ for each fixed $`s`$ (`PROVED-DOSSIER`, the sparse-flank
family (SF)) closes the margin.

Rule-12 pre-clearance, recorded and not lost downstream: **every**
route through `CG` consumes item-0020's $`F(x,s)/N(x,s)\to0`$. Per
ANN-20260724-63 that ingredient has no effective onset in any reachable
range -- the proved capacity/population comparator
$`\mathrm{cap}_{J+K}(x)`$ vs $`P_0(x)=x\ln3/(16\ln{}x)`$ does not
turn permanently favorable until roughly $`1.20\times10^{105}`$
(proved binomial cap $`\binom{M}{r}`$) or $`3.53\times10^{106}`$
(displayed cap). Both crossovers are reproduced in `budget_sheet_20_ext.py`
T10 (proved binomial at $`x\sim10^{105.1}`$, displayed at
$`x\sim10^{106.5}`$; `MEASURED` from the extension sheet, matching the
anchored audit values). This does not invalidate (CG); it means every
`CG`-route is `Eventually`/`Tendsto`-extraction only, with no concrete
materialization -- a numerical fact about the route, `PROVED-DOSSIER`.

### W2.3 `ExAnteWeightedMiddleContractionAlongScales` (implies `CG`)

Anchor (ANN-20260723-59; `m5-lite-audit.md`). One predeclared selector
and saving profile $`\kappa_P`$, fixed **before inspecting the middle
histogram** (ex-ante, cap-blind), gives classwise bounds

$$
N_{P,d}\le(1-\kappa_P)N_P+1\qquad\text{and}\qquad
\sum_{P\in G}\kappa_P N_P\ \ge\ \eta_s N
$$

on unbounded scales for each fixed $`s`$, with the site-weighted
saving positive on the favorable family $`G`$. This implies
`CollisionGapAlongScales` with the same $`\eta_s`$ (ANN-59; PROVED
finite envelope: if $`N_{P,d}\le\lambda N_P+1`$ on every repeated
realized middle with $`0\le\lambda<1`$ then $`Q_P\le\lambda N_P`$).

Minimal demand triple. **Strength:** a per-class contraction plus a
fixed positive site-weighted saving $`\eta_s`$ on $`G`$; not
$`c\to0`$. **Uniformity:** none in $`s`$. **Scale-density:**
sparse (unbounded scales per $`s`$), plus the ex-ante discipline on
$`\kappa_P`$. What it does **not** consume, additionally: the
$`\rho`$-cap $`R=o(\log{}x)`$ -- ANN-59 records this as an old proof
device, not a logical requirement of the new endpoint.

### W2.4 Demand order

$$
\text{CG}\ \prec\ \text{Contraction}\ \prec\ \text{B2.pairs},
$$

with `CG` the weakest currently known sufficient endpoint for
$`S\notin\mathbb Z[1/2]`$. The re-pricing question of W4 is whether
descending this order rescues any separator that was fatal for
`B2.pairs`.

---

## W3. Model-refutation criterion

### W3.1 The criterion (PROVED-DOSSIER)

Let $`T`$ be the named unconditional tool list of `proofs.md` C4
(RS.1/D0.3 identities, capacity bounds, the Chebyshev/PNT/Markov
aggregates, retention/`TailIntersection`, gap parity and the
parameter-map arithmetic). The even-Cramer-smooth deterministic gap
system

$$
q_1=2,\ q_2=3,\ q_3=5,\ q_4=7,\qquad
q_{n+1}=q_n+2\left\lceil\tfrac{\ln{}q_n}{2}\right\rceil\ (n\ge4)
$$

satisfies **every** member of $`T`$ verbatim, with the same constants
(`proofs.md` C4 CONSTRUCTION AND VERIFICATION; support: `PROVED`,
elementary model construction plus fact checks, with the
$`q_n=(1+o(1))n\ln{}n`$ step at standard-comparison grade, U20.5
write-out debt).
Consequently:

> **Criterion.** If an endpoint $`E`$ is false in this model, then no
> conjunction of members of $`T`$ implies $`E`$; any proof of
> $`E`$ must consume at least one input **outside $`T`$ that fails
> in the model**.

This is the located-obstruction form of F20.7, relative to the named
list $`T`$; it is not an impossibility claim (`collision-gap-audit`
I; `relext-upper.md` F20.7).

### W3.2 Each endpoint checked against the model, individually

- **`B2.pairs`**: FALSE. $`Q(x,0)\ge(1-o(1))N(x,0)`$ (`proofs.md` C4),
  so $`Q/N\to1`$ refutes $`Q=o(N)`$. `PROVED-DOSSIER`.
- **`CG`**: FALSE. $`Q/N\to1`$ (a limit) refutes
  $`\liminf Q/N<1`$. Two verifications the kickoff mandates before
  W4:
  - **(a) PROVED vs MODEL-ONLY.** $`Q/N\to1`$ in this model is
    `PROVED-DOSSIER` (`m5-lite-audit.md` F20.7 row: "`PROVED-DOSSIER`,
    with U20.5 write-out debt"; `collision-gap-audit` I derives it from
    C4's $`Q(x,0)\ge(1-o(1))N`$ and the universal $`Q\le N-F\le N`$).
    The barrier argument needs it `PROVED`; it is. The model is a
    deterministic **proof object**, not a probabilistic heuristic, so
    the `MODEL-ONLY` support class does not enter, and STOP condition 5
    does not fire on this ground.
  - **(b) Full limit vs subsequence, and the $`D0`$ depth-jump
    interaction.** `CG` is a $`\liminf`$ statement; it is barred only
    if the model's $`Q/N\to1`$ is a **genuine limit over all integer
    $`x`$**, not merely along a subsequence. Verified: the non-rigid
    classes number $`\sim\ln{}x/2`$ (one size-2 class per realized
    gap-value step; `proofs.md` C4 step (4), audit-verified
    computationally at $`10^6/5\times10^6/10^8`$), carrying
    $`O(\ln{}x)`$ non-rigid sites; they sit inside a transitional
    (boundary-straddling) subfamily of total site mass $`O(L\ln{}x)`$,
    itself mostly **rigid** singletons. Both the non-rigid mass and the
    enclosing transitional mass are $`o(N)`$ at **every** large $`x`$.
    Since
    $`L=(2+o(1))\log_2{}\ln{}x`$ and $`N=x^{1-o(1)}`$, the
    transitional share $`O(L\ln{}x)/N=x^{-1+o(1)}\to0`$ at every
    scale, **including the $`D0`$ depth-jump scales**: a jump raises
    $`J,K`$ by one but leaves the count of realized gap values
    ($`\sim\ln{}x/2`$) and hence the transitional-class count
    $`O(\ln{}x)`$ unchanged in order, so $`L\ln{}x=x^{o(1)}=o(N)`$
    is preserved across jumps. Therefore $`Q(x,0)/N\ge1-o(1)`$ for
    every large $`x`$; no subsequence has $`\liminf<1`$. The
    sparse-scale freedom in `CG` does **not** escape the model.
    `PROVED-DOSSIER`. STOP condition 5 does not fire.
- **`ExAnteWeightedMiddleContractionAlongScales`**: FALSE, a fortiori
  (it implies `CG`). Directly (ANN-59): "In the even-Cramer-smooth
  model $`Q/N\to1`$. On model scales where the classwise bounds hold,
  the normalized weighted saving tends to 0; otherwise the classwise
  bound itself fails." So the contraction and the positive saving
  cannot both hold. `PROVED-DOSSIER`.

All three endpoints fail in the model. The barrier of W3.1 therefore
applies to each, confirming the load-bearing sentence of the W1 text
("the barrier described in Section 5 applies to both", now to all
three). W4 changes character only if some **separator** outside $`T`$
becomes affordable under the weaker endpoints.

---

## W4. Separator re-pricing

`proofs.md` C4 SCOPE names three separator families -- inputs outside
$`T`$ that fail in the model. Each is re-priced against `CG` and
against the contraction endpoint at rank
$`k=(2/\ln2+o(1))\,\ln\ln{}x`$ in `budget_sheet_20_ext.py` (tables
T9--T11), against $`\ln{}x`$ (G1), $`x^{\varepsilon}`$ (G2), and the
pigeonhole reserve (G3). The organizing principle, PROVED-DOSSIER: a
cost that depends on the tuple **rank** $`m`$ -- fixed by the $`D0`$
exchange geometry, which `CG` inherits unchanged (same
$`S_x^{\prime(s)}`$, same parameter map) -- is **invariant** under the
`B2.pairs`->`CG` relaxation; only a cost that depends on strength,
$`s`$-uniformity, or scale-density can drop.

### W4.S3 Bounded / small-gap input (Maynard, anchored `1311.4600`) -- the highest-EV row

It fails in the model (all model gaps $`\to\infty`$), so it is a
genuine separator. It was rejected for `B2.pairs` because its
quantitative cost at growing rank is superpolylog, priced at sheet row
`T6 M3(c)`. Re-price for a fixed $`\eta_s>0`$ on an unbounded scale
sequence per fixed $`s`$.

Producing non-rigidity means exhibiting, within $`S_x^{\prime(s)}`$,
two sites $`n\ne m`$ in one class $`P`$ -- i.e. realizing a
**prescribed even flank word of length $`J+K=L-1`$** twice, with
distinct middles. The flank length grows:
$`J=K=\lceil\log_2 D\rceil=(1+o(1))\log_2\ln{}x\to\infty`$. The
density of primes
realizing a prescribed length-$`m`$ gap word twice is governed by a
rank-$`m`$ sieve/singular-series whose uniform control costs
$`\exp((1+o(1))m\ln{}m)`$ at cluster size $`m\sim L`$ (the F17.9 /
`T1` class; T6 M3(c)). `budget_sheet_20_ext.py` T9.S3 tabulates the
exponent $`\mathrm{expo}=(L\ln{}L)/\ln\ln{}x`$ at the grid
($`6.14\to8.96`$ across $`x=10^8`$ to $`10^{1000}`$) -- the same
superpolylog class as the anchor `T1` $`\exp(k\ln{}k)`$ row.

Answer, explicit as the kickoff demands. The `B2.pairs`->`CG` relaxation
removes (i) $`\varepsilon\to0`$, (ii) $`s`$-uniformity, (iii)
all-large-$`x`$. **None of (i)--(iii) is the binding cost**: the
binding cost is the rank $`m\sim L`$, which is $`D0`$-forced and
identical for `CG`. A bounded-rank Maynard input (fixed $`m`$) is
affordable but has only $`m`$ primes and cannot realize a
growing-length flank word, so it never populates a $`D0`$-depth class
with a twin and contributes nothing to $`Q,N`$ at $`D0`$ depth.
Aggregating to a positive proportion $`\eta_s`$ of non-rigid mass only
multiplies the per-word rank-$`L`$ cost. Therefore:

> **The superpolylog rank cost is still binding under `CG` and under
> the contraction endpoint.** `PROVED-DOSSIER` (rank $`D0`$-forced,
> `relext-statements` D0; cost the `T1`/F17.9 class, sheet T9.S3; the
> relaxation touches strength/uniformity/density, not rank). S3 does
> not survive re-pricing.

### W4.S2 Second-moment gap statistic (Montgomery--Soundararajan)

Recorded present in `dossier/literature.md` only, not an unconditional
corpus tool at word grain, itself Cramer-defying (variance
$`\sim H\log{}(N/H)`$, not $`H`$). At constant-order demand, does the
word-grain gap close, or is the corpus-status gap binding?

Both a **regime** gap and a **corpus-status** gap bind, and neither is a
strength gap that `CG` could relax. Regime: Montgomery--Soundararajan
is an interval statement in the range
$`N^{\delta}\le H\le N^{1-\delta}`$ ($`H`$ polynomially large); the
exchange middle sits in
a window of size $`A'L\ln{}x\sim(\log{}x)(\log{}\log{}x)`$ -- far below
$`N^{\delta}`$. The nearest corpus tool in this line, Kuperberg
`2210.09775` (anchored; `D1.b`), admits rank $`k\lesssim(\log{}h)^{1/2}`$
at window $`h`$, while the exchange needs
$`k=(2/\ln2)\ln\ln{}x`$ at $`h=A'L\ln{}x`$;
`budget_sheet_20_ext.py` T9.S2 tabulates the ratio
$`k_{\mathrm{req}}/k_{\mathrm{adm}}\sim(\ln\ln{}x)^{1/2}\to\infty`$
($`3.60\to6.66`$ across the grid) -- a regime square-out independent
of endpoint strength. Corpus-status: it is a literature citation, not a
word-grain corpus tool (the group structure the large sieve / BV need is
absent on side-pair classes). `PROVED-DOSSIER`: S2 is regime-blocked
under `CG`; the constant-order demand does not close the word-grain gap.
S2 does not survive re-pricing.

### W4.S1 Middle-slot equidistribution / upper-uniformity (`NI-M2`, `NI-M4` shapes)

Recorded absent from the corpus. Does the constant-order demand of `CG`
admit a **weaker** member of this family than `NI-M2` in full?

Yes, in strength -- but the carrier is still absent. `NI-M2` (class
equidistribution at rank $`k`$) and `NI-M4` (word-grain upper mean
value at rank $`k`$) are the salient middle-slot inputs; their
**local** cost is dimension-1, $`O(1)`$ $`\rho`$-algebra factors
(M7), so they clear every budget -- `budget_sheet_20_ext.py` T9.S1 marks
their exponent $`0`$ at every scale. The block is **absence**, not
cost (F20.4/F20.5, recorded obstructions). `CG` genuinely weakens the
**demanded strength**: from full equidistribution (error $`o(1)`$,
driving $`Q/N\to0`$) to constant-order middle non-concentration on
sparse scales per $`s`$ ($`Q/N\le1-\eta_s`$ on a $`\liminf`$
sequence). That target is strictly weaker; whether it is provable is
**not decidable from the corpus** -- no averaged middle-slot
non-concentration statement at rank $`k\sim2.885\,\ln\ln{}x`$ exists
in the shelf, and weakening the endpoint does not manufacture one
(`collision-gap-audit` E). S1 is the H-SEP-shaped separator: a
middle-slot distributional input at the `HLQuantA` **rank**
$`k\sim2.885\,\ln\ln{}x`$ (inside the $`\le4\ln\ln{}x`$ card), carrying
the **upper / equidistribution** content that the frozen lower-bound
`HLQuantA` lacks -- `NI-M2`/`NI-M4` are strictly beyond-`HLQuantA` upper
content (`mechanism-inventory` M4; `relext-statements` D3(ii)) -- and is
present here only as an absent target. [audit repair: "of HLQuantA
shape" was an over-identification; the corpus reserves the `HLQuantA`
name for the absolute lower bound, so the separator is stated at the
`HLQuantA` rank but beyond its content.]

> S1: **undecidable at corpus grain** under `CG`. Deciding fact
> (named): an unconditional averaged middle-slot non-concentration /
> upper-uniformity statement at rank $`k=(2/\ln2+o(1))\ln\ln{}x`$,
> window $`A'L\ln{}x`$, of strength enough to keep a fixed proportion
> of $`D0`$-depth site mass off its modal middle on some unbounded
> scale sequence per $`s`$ -- a statement that fails in the
> even-Cramer-smooth model.

### W4.U20.4 Re-open sweep of the anchored corpus

Execute the `U20.4` re-open clause: sweep the anchored corpus for any
unconditional fact **outside $`T`$** that **fails in the model** and
has **not yet entered the inventory** $`\lbrace S1,S2,S3\rbrace`$. Anything found
re-opens the inventory, not Theorem 4. Named enumeration of what was
swept (the anchored PDF shelf of `payloads/HASHES.txt` plus
`literature.md`), model-behaviour recorded for each (model gaps are
$`g_n\sim\ln{}q_n`$, smooth, monotone, all $`\to\infty`$):

| corpus fact | fails in model? | disposition |
| --- | --- | --- |
| Maynard, *Small gaps between primes* (`1311.4600`) | yes (gaps $`\to\infty`$) | = S3 |
| Maynard, *Dense clusters* (`1405.2593`) | yes | S3 family |
| Banks--Freiberg--Turnage-Butterbaugh (`1311.7003`) | yes (consecutive primes in constant patterns) | S3 family |
| Goldston--Pintz--Yildirim small-gaps (`0409258`) | yes | S3 family |
| Kuperberg (`2210.09775`) | yes (singular-series sums, MS line) | = S2 |
| Montgomery--Soundararajan (`literature.md`) | yes | = S2 |
| Maier, *Primes in short intervals* | yes (model is smooth; Maier shows short-interval oscillation) | S1/S2 family; short-interval, regime-blocked |
| Ford--Green--Konyagin--Maynard--Tao, *Long gaps* (`1412.5029`) | **yes** (model max gap $`\sim\ln{}x`$; theorem forces $`\gg\ln{}x`$) | **NEW hit** -- see below |
| Pratt (`2409.15185`), Tao--Teravainen (`2512.01739`) | n/a (bounded $`\omega(n)`$, different series) | not a matched-flank input; corroborating meta-fact below |
| Cramer 1936 / Granville 1995 | -- (the model being defied) | not a separator |

The sweep is **not empty**: the long-gaps theorem of Ford--Green--
Konyagin--Maynard--Tao is a $`T`$-external, model-failing corpus fact
outside $`\lbrace S1,S2,S3\rbrace`$ (the model's maximal gap up to $`x`$ is
$`\sim\ln{}x`$, asymptotically below the theorem's
$`\gg(\log{}x)(\log{}\log{}x)(\log{}\log{}\log{}\log{}x)/(\log{}\log{}\log{}x)`$).
It **re-opens the `U20.4` inventory** (the claim "T exhausts the
program's unconditional inputs" is not complete of model-failing facts).
It is **not a viable separator**, however -- but **not** for a
window-cap reason. [audit repair: the draft claimed a single large gap
violates the $`D0.2'`$ window cap and is filtered out of
$`S_x^{\prime(s)}`$; that is quantitatively false. The FGKMT maximal gap
is $`\sim(\log{}x)(\log{}\log{}x)\cdot o(1)=o(A'L\ln{}x)`$, a vanishing
fraction of the window budget, and `relext-statements` line 664
confirms the window admits middles up to $`A'L\ln{}x>2D`$; a lone large
gap does not exceed the cap.] The correct reason is structural: FGKMT is
a **single-event existence** statement about one **maximal gap** (gap
*size*), not about matched flanks. It produces no pair of sites sharing
one flank word with distinct middles, and it contributes $`O(1)`$ sites,
not the positive proportion $`\eta_s N`$ of non-rigid mass that (CG)
requires -- the rigidity defect
$`N-F-Q=\sum_P(2/N_P)\sum_{d<e}N_{P,d}N_{P,e}`$ needs a
positive-proportion family of classes with $`\ge2`$ distinct realized
middles, which a size-existence bound on one gap cannot supply. So it
cannot feed $`Q<N-F`$. Recorded as a hit that
re-opens the inventory but changes no verdict. `PROVED-DOSSIER`.

Corroborating meta-fact, both-readings: Tao--Teravainen (`2512.01739`,
anchored) settle $`\sum\omega(n)/2^n`$ unconditionally with
Maynard-type sieves but state explicitly that growing numerators (like
$`p_n`$) have "no known techniques to unconditionally obtain
asymptotics" (`literature.md` Item 8b). Supporting reading: the
bounded-gap machinery exists and defies the model. Contradicting
reading: its authors place the growing-rank transfer -- exactly the
$`p_n`$ regime of this problem -- outside current technique, matching
the S3 superpolylog-rank verdict. Both recorded.

---

## W5. Error landing (rule-12)

For every candidate surviving W4, the rule-12 error-landing check must
run before any further investment. **No separator survives W4** as a
live sheet-clean candidate against `CG` (S3: superpolylog rank, still
binding; S2: regime-blocked; S1: right shape, absent, undecidable at
corpus grain; the `U20.4` hit non-viable). So there is no surviving
candidate to error-land, and STOP condition 6 does not fire.

The rule-12 landing is recorded for the ingredient every `CG`-route
does consume, $`F/N\to0`$ (SF): the $`o(1)`$ in
$`F/N=x^{-1+o(1)}`$ lands as an **additive threshold shift** -- the
$`\sim1.20\times10^{105}`$ (binomial) / $`3.53\times10^{106}`$
(displayed) onset -- **not** as a leading-coefficient coupling
(`budget_sheet_20_ext.py` T10; anchor `T3` landing row: "no leading-
coefficient coupling anywhere"). Settled numerically in advance: the
extension sheet reproduces both crossovers ($`10^{105.1}`$,
$`10^{106.5}`$). Consequence: every `CG`-route is
`Eventually`/`Tendsto`-extraction only, with no concrete
materialization in any reachable range; the hypothetical S1 CG-proof, if
its carrier existed, would consume the C3 reduction shape (no $`k`$-
or $`x`$-dependent constant, anchor `T5` row (a) NONE) and leave full
pigeonhole reserve (T11) -- so the reserve is never S1's binding
constraint; its absence is.

---

## W6. Verdict

Support class on every clause; rule-16(a) clause-vs-body diff run below.

**Primary hypothesis H-SEP: CONFIRMED (obstruction upgrade).**
[`PROVED-DOSSIER` for the S2/S3 negatives and the barrier; the S1
component is `OPEN`/undecidable-at-corpus-grain, named.]

1. Against the weakest currently known sufficient endpoint `CG` (and its
   strengthening, the contraction endpoint), and after adjoining the
   named separator inventory $`\lbrace S1,S2,S3\rbrace`$ plus the `U20.4` sweep
   to the tool list, **no separator in the anchored corpus survives
   re-pricing** as a live candidate with a sheet-clean rule-15 ledger:
   - S3 (Maynard bounded gaps) fails on a **rank** cost
     $`\exp((1+o(1))m\ln{}m)`$, $`m\sim L`$, which is invariant
     under the `B2.pairs`->`CG` relaxation because the relaxation touches
     strength / $`s`$-uniformity / scale-density, never the
     $`D0`$-forced rank [`PROVED-DOSSIER`; sheet T9.S3].
   - S2 (Montgomery--Soundararajan / Kuperberg line) fails on a
     **regime** square-out
     $`k_{\mathrm{req}}/k_{\mathrm{adm}}\sim(\ln\ln{}x)^{1/2}`$ and on
     corpus status, neither a strength gap `CG` could close
     [`PROVED-DOSSIER`; sheet T9.S2].
   - S1 (middle-slot equidistribution / upper-uniformity, `NI-M2`/`NI-M4`)
     is the **right shape** -- a middle-slot distributional input at the
     `HLQuantA` rank $`k\sim2.885\,\ln\ln{}x`$, carrying the upper /
     equidistribution content the frozen lower-bound `HLQuantA` lacks --
     and is **absent** from the corpus; `CG` weakens the demanded
     strength (constant-order non-concentration on sparse scales) but
     does not manufacture the carrier, so the re-pricing is
     **undecidable at corpus grain** [`OPEN`; deciding fact named in
     W4.S1].
2. Therefore the located obstruction **upgrades**: from "relative to
   $`T`$, for `B2.pairs`" to **"relative to $`T`$ together with the
   named separator inventory, for `CG`, the weakest currently known
   sufficient endpoint."** Any proof of `CG` must consume an input
   **outside $`T`$ that fails in the model** (the barrier's own
   characterization; `proofs.md` C4 SCOPE: "the characterization is
   failure-in-model, not middle-slot-ness"). The **salient**, and only
   currently identified, such family at the exchange rank is the
   middle-slot distributional statements at rank
   $`k\sim2.885\,\ln\ln{}x`$ -- the upper / equidistribution companion,
   at the `HLQuantA` rank but beyond its lower-bound content, of the
   uniform-tuple input the conditional full-irrationality route assumes.
   This is a materially stronger `(S-)` statement than the item-0020
   register and directly informs BET-20260718-08 [`assessment`; the
   sub-clauses carry the classes above. audit repair: "requires
   precisely a middle-slot input" / "HLQuantA-shape" over-strengthened
   the barrier; softened to salient-family + failure-in-model].
3. The `U20.4` sweep is not empty: Ford--Green--Konyagin--Maynard--Tao
   long gaps is a $`T`$-external model-failing corpus fact that
   re-opens the inventory but is **non-viable** as a separator -- a
   single-event maximal-gap existence about gap *size*, not
   matched-flank non-rigidity; it contributes $`O(1)`$ sites, not the
   positive proportion (CG) needs [`PROVED-DOSSIER`; audit repair: the
   draft's window-cap filtering reason was quantitatively wrong -- a
   lone FGKMT gap is $`o(A'L\ln{}x)`$, inside the cap]. No new viable
   separator emerges.
4. STOP conditions: none fired. #5 does not fire -- the model's
   $`Q/N\to1`$ is a **genuine limit** over all integer $`x`$
   (transitional mass $`o(N)`$ at every scale, including $`D0`$
   depth jumps) and is `PROVED-DOSSIER`, not `MODEL-ONLY` (W3.2b). #6
   does not fire -- no separator survives W4 sheet-clean. #8 does not
   fire -- every fact used (Maynard `1311.4600`, Montgomery--
   Soundararajan via `literature.md`, Kuperberg `2210.09775`, FGKMT
   `1412.5029`, Maier) is in the anchored corpus / PDF shelf. #7 does
   not fire -- W1 was fixed pre-pin and untouched by W2--W6.
5. Obstruction-language discipline (binding): the above is a **located
   obstruction relative to a named inventory**, not an impossibility
   theorem; no endpoint is claimed unprovable. `CG` remains the
   recommended proof-campaign target; the re-pricing shows only that its
   proof must still consume an input that fails in the
   even-Cramer-smooth model and is absent from the corpus -- the salient
   such family being the middle-slot distributional inputs at the
   exchange rank.

### rule-16(a) clause-vs-body diff

Every scope qualifier of the body survives into the verdict verbatim:
- "weakest currently known sufficient endpoint" -- body W2.4, verdict 1/2.
- "invariant under the relaxation ... never the $`D0`$-forced rank" --
  body W4.S3, verdict 1.
- "regime square-out ... neither a strength gap `CG` could close" --
  body W4.S2, verdict 1.
- "right shape, absent, undecidable at corpus grain" -- body W4.S1,
  verdict 1; the deciding fact named identically in both. The
  "at-the-`HLQuantA`-rank, beyond its content" qualifier (not "of
  `HLQuantA` shape") is carried identically in body W4.S1 and verdict
  1/2.
- "failure-in-model is the characterization, middle-slot the salient
  family" -- body W4.S1 / W3.1, verdict 2/5 (not "requires precisely
  middle-slot").
- "genuine limit over all integer $`x`$ ... including $`D0`$ depth
  jumps ... `PROVED-DOSSIER`, not `MODEL-ONLY`" -- body W3.2b, verdict 4.
- "re-opens the inventory but non-viable (single-event maximal-gap,
  gap-size not matched-flank; not a window-cap reason)" -- body
  W4.U20.4, verdict 3.
- No verdict clause strengthens a body support class; the S1 `OPEN`
  label and the S2/S3 `PROVED-DOSSIER` negatives are carried without
  promotion.

---

## Both-readings appendix (empirical and literature citations)

- **Singleton frontier** (`flank-collision-singleton-frontier-audit.md`;
  ANN-20260724-62; MEASURED-PRODUCTION). 35 rows = 7 scales
  ($`10^6`$--$`10^9`$) $`\times`$ 5 thresholds; every row
  $`N=F`$, $`Q=0`$, $`N-F-Q=0`$; largest $`(10^9,0)`$:
  $`N=F=50{,}827{,}008`$; $`C_{\mathrm{flank}}=0`$ everywhere.
  *Supporting reading:* the statistic vanishes identically -- consistent
  with model rigidity; no non-rigidity observed. *Contradicting
  reading:* the measured range ($`\le10^9`$) is astronomically below
  the heuristic order-one collision region $`10^{27}`$--$`10^{30}`$
  ($`\gamma`$ stress envelope $`[1.57,1.98]`$, HEURISTIC) and the
  proved $`F/N`$ onset $`\sim10^{105}`$, so it supplies **no**
  evidence for or against the asymptotic statement (ANN-61: "finite
  adverse evidence and no asymptotic M5-lite claim"). Both recorded.
- **Reading cautions** (ANN-20260724-63, binding).
  $`\eta_{\mathrm{cert}}=(1-\lambda_{\max})\alpha`$ in
  `m5-lite-phase3b/production/per-rule-certificates.json` reaches
  $`1.0`$ in 224 of 805 rows **purely because
  $`\lambda_{\max}=0`$ under singleton inertia**; the collision-gap
  margins are $`\eta_{\mathrm{escape}}`$ and $`\eta_{\mathrm{Gini}}`$,
  which are $`0`$ in all 805 rows. $`\eta_{\mathrm{cert}}`$ is **not**
  a measured collision-gap margin and is nowhere cited as one in this
  audit. The 35 frozen rows are 7 independent scales ($`N`$ falls by
  exactly $`s`$ at every scale; the $`s`$-panel is deterministic
  prefix deletion). Honored throughout.
- **Maynard / Tao--Teravainen literature** -- both-readings recorded in
  W4.U20.4.

---

## In-run adversarial audit (refuter panel; EXECUTED)

A local, corpus-only, web-OFF refuter panel (15 agents = 3 diverse
lenses -- arithmetic/correctness, adversarial, corpus-fidelity/verdict-
promotion -- on each of 5 load-bearing claims) was run against the draft
before this version was fixed, mirroring the project's in-run refuter
discipline (item-0018 Section 9a; item-0020 audit fan-out). Sustained =
$`\ge2`$ of 3 lenses refute.

SURVIVED clean (0/3): the S3 rank-invariance verdict (the highest-EV
row); the W3.2b $`Q/N\to1`$ genuine-limit / STOP-5 verification; the S2
regime-block verdict.

SUSTAINED and repaired in place (marked "[audit repair]" inline):

- **(2/3) H-SEP wording over-strengthened the barrier.** The draft's
  "requires precisely a middle-slot distributional input of `HLQuantA`
  shape" made a shape-necessity claim the barrier disclaims (`proofs.md`
  C4 SCOPE: "the characterization is failure-in-model, not
  middle-slot-ness") and re-used the reserved `HLQuantA` name for the
  class-relative `NI-M2`/`NI-M4` carrier, which the corpus records as
  strictly beyond-`HLQuantA` upper content. Repaired: W4.S1, verdict 1,
  verdict 2, verdict 5, and the rule-16(a) diff now state
  failure-in-model as the characterization, middle-slot as the salient
  family, and the separator as at the `HLQuantA` **rank** but **beyond**
  its lower-bound content. The H-SEP verdict (CONFIRMED / obstruction
  upgrade) is unchanged in substance; the over-strengthening -- exactly
  the verdict-promotion pattern this project has caught three times -- is
  removed.
- **(2/3) FGKMT non-viability reason was quantitatively wrong.** The
  draft claimed a single Ford--Green--Konyagin--Maynard--Tao large gap
  violates the $`D0.2'`$ window cap and is filtered out of
  $`S_x^{\prime(s)}`$; but the FGKMT gap is $`o(A'L\ln{}x)`$ (a vanishing
  fraction of the budget; `relext-statements` line 664 admits middles up
  to $`A'L\ln{}x`$). Repaired: W4.U20.4 and verdict 3 now give the
  correct structural reason (single-event maximal-gap existence about
  gap *size*, not matched-flank non-rigidity; $`O(1)`$ sites, not the
  positive proportion (CG) needs). The non-viability *conclusion* and
  the "re-opens the inventory" hit are unchanged.

Non-material notes folded: the W3.2b non-rigid-vs-transitional mass
phrasing was sharpened (both are $`o(N)`$); the $`Q/N\to1`$ support
carries its "with U20.5 write-out debt" and "relative to $`T`$"
qualifiers (W3.1/W3.2a). No STOP condition changed; no verdict was
demoted.

---

## GATES

- W0 gates: recorded verbatim above (pin == HEAD, no rule-18 delta; ten
  Section 2 anchors byte-identical; frozen-blocks / relocation /
  sorry-census / mathlib-pin / toolchain-newline / roadmap-status all
  PASS). No STOP condition fired.
- W1: post-replacement `writeup/status.md` sha256
  `335eb6ea026ab2a41ac6e48f31e034da2f72d5597e0e62415fc71fa1b8120c6d`;
  `git diff --stat` = `writeup/status.md` only; W1 gate checks PASS.
- Budget-sheet extension `budget_sheet_20_ext.py` (deterministic;
  re-run sha256-stable) sha256:
  `9c0d51f30b458ee0991d8980237a9a4a2d404f0f2659e28d89b27e26024e1899`.
- Emitted table `budget_sheet_20_ext_tables.txt` sha256:
  `135815b3b3253003650352914c6a9d88986d2fc1cc6de2a4f1db878b1c47bd71`.
- The anchored `dossier/item-0020-workpapers/budget_sheet_20.py` is
  untouched (byte-identical to the Section 2 anchor
  `bbce2f58...b0d`); the extension neither imports nor overwrites it.
- This report's own sha256 is computed over the finalized bytes at
  close and booked in the run log (a file cannot contain its own hash);
  its value is reported by the executor at hand-off.
- MathJax conventions per `AGENTS.md`: inline math dollar-backtick;
  `\mathrm`, `\lvert`/`\rvert`, `\lbrace`/`\rbrace`, `\substack`+`\cr`,
  `\log{}`; display in `$$` blocks.

## Outputs (kickoff Section 8)

- `dossier/item-0010-workpapers/separator-repricing.md` (this report);
- `dossier/item-0010-workpapers/budget_sheet_20_ext.py` and its emitted
  `budget_sheet_20_ext_tables.txt`;
- the two W1 replacements in `writeup/status.md`;
- nothing else. The executor commits nothing and pushes nothing; the
  ledger entry is authored by steering post-run.
