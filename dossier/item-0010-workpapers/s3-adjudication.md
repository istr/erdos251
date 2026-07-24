# S3 non-survival grade -- adjudication (Dispatch C)

Date: 2026-07-24. Executor: fresh adjudicator (not the audit author, not
either cross-family reviewer), EXECUTOR lane, Claude Code, local machine;
model string `claude-opus-4-8[1m]`. Against `dispatch-C-s3-adjudication-v2.md`
(operator-supplied). Web OFF and cloud OFF for the entire session
(corpus-only; no external literature, no steering triage, no answer key).
Local computation only. This is an adjudication note, **not** a repair of the
artifact: nothing under `writeup/`, `lean/`, or the artifact
`separator-repricing.md` is edited; the only file writes this session are the
`L_ceil` addition to `budget_sheet_20_ext.py` and its regenerated table
(Dispatch C Section 5), plus this note.

Evidence labels carry their repository meanings (`separator-repricing.md`
"Evidence labels"): `FORMAL`, `PROVED-DOSSIER`, `PROVED`, `MEASURED`,
`HEURISTIC`, `MODEL-ONLY`, `OPEN`, `RECORDED`, `UNMEASURED`.

---

## 1. Gate line

Pin: `80c904eee5838e20b24b0e76cbcc6e3f1e5372f7` == `git rev-parse HEAD`
EXACTLY. Web OFF, cloud OFF. All ten Section-2 material hashes verified
byte-identical at session start:

Under review (writable only as Section 5 permits):

    644c512b7e1a4106eea14454e0ebbdade22bdcdaf753ed1b38bf64d155fee63d
      dossier/item-0010-workpapers/separator-repricing.md
    9a0cd704314d74c09f1e1ec19420531db7a0ce28f3e7979931a726f0181d19ea
      dossier/item-0010-workpapers/budget_sheet_20_ext.py       (pre-C1)
    49907f0cb1af2e09579aa346568a98610a2b0411b11cf3e743929e4897c79036
      dossier/item-0010-workpapers/budget_sheet_20_ext_tables.txt (pre-C1)

Evidence base (read-only; each verified before reading):

    bbce2f583f0a1f158b7fc5f13ca120b5388be642c585bbbdac5e6be5c5558b0d
      dossier/item-0020-workpapers/budget_sheet_20.py
    55c915f0ae0ffcabd66cb07b3467881f9a035e9ecd63657c0b1486b173e1f79b
      dossier/item-0010-workpapers/collision-gap-audit.md
    1a34255829ef47c4cc311833f839ffd1ee5ab4b243164dc63c407b5f0c5adcb4
      dossier/relext-statements.md
    58e16a603705ac85d519a510c4049d47e9e7a9ba4290f7b7905abef7da865e64
      dossier/item-0020-workpapers/proofs.md
    fe2ad5a3f95f2fb8589b71432d0c2ca2a53cd0e0a6dcdafd3044b45be82afacf
      dossier/item-0020-workpapers/mechanism-inventory.md
    17a3d8c5c2e205fba4417f96739896f3bc7c486b7bf5c36db772e1a5f474a7bc
      dossier/literature.md
    3663dc9e8ec534e0959449bcb694b8a3ae29f1bfb4f13bfd954eec2b7efd0e51
      writeup/status.md   (frozen; untouched, re-verified at close)

`writeup/status.md` and `budget_sheet_20.py` remain byte-identical at close.
No STOP-AND-REPORT condition 1 fires.

The contested clause, quoted (rule 19), `separator-repricing.md` verdict
clause 1 (l.652-656):

````text
   - S3 (Maynard bounded gaps) fails on a **rank** cost
     $`\exp((1+o(1))m\ln{}m)`$, $`m\sim L`$, which is invariant
     under the `B2.pairs`->`CG` relaxation because the relaxation touches
     strength / $`s`$-uniformity / scale-density, never the
     $`D0`$-forced rank [`PROVED-DOSSIER`; sheet T9.S3].
````

---

## 2. C1 -- the `L_ceil` re-run (both columns)

`budget_sheet_20_ext.py` prices T9.S3 on the **grid** surrogate
$`L=(2/\ln2)\,\ln\ln{}x`$ (anchor tag (m); disclosed in the B-pass, not
switched). The $`D0`$-exact depth is $`L=2J+1`$,
$`J=\lceil\log_2\lceil13C_0A''\ln{}x\rceil\rceil`$, shipped as `L_ceil()` in
the anchored `budget_sheet_20.py` (l.156-161). Per Section 5, I added
**only** a `T9.S3.Lceil` block that re-prices the **same** cost
$`m\ln{}m`$ at $`m=L_{\mathrm{ceil}}`$, alongside the grid columns, leaving
every existing numeric column byte-identical.

Both columns, exponent $`=\mathrm{expo}[\exp(m\ln{}m)]=(m\ln{}m)/\ln\ln{}x`$
(so cost $`=(\ln{}x)^{\mathrm{expo}}`$):

| $`x`$ | grid $`m=L`$ | grid expo | exact $`m=L_{\mathrm{ceil}}=2J+1`$ | exact expo |
| --- | --- | --- | --- | --- |
| $`10^{8}`$    |  8.407 | 6.143 | 31 | 36.538 |
| $`10^{20}`$   | 11.050 | 6.932 | 33 | 30.128 |
| $`10^{100}`$  | 15.694 | 7.944 | 37 | 24.563 |
| $`10^{1000}`$ | 22.338 | 8.963 | 45 | 22.127 |

Direction, as the dispatch predicted: the exact rank exceeds the grid rank
(additively by $`\sim(2/\ln2)\ln(13C_0A'')\approx20`$ at these scales, ratio
$`\sim3.7\times`$ at $`10^8`$ falling to $`\sim2.0\times`$ at $`10^{1000}`$),
so $`\exp(m\ln{}m)`$ is **larger** and the (G1) $`o(\ln{}x)`$ failure is only
**deeper** (exact expo $`22`$--$`37`$ versus grid $`6`$--$`9`$). (G2) still
passes: $`m\ln{}m=o(\ln{}x)`$ at exact $`m`$ too, since
$`m=(2/\ln2+o(1))\ln\ln{}x=O(\ln\ln{}x)`$. The instrument can only help the
artifact's own position, and it does. `MEASURED` (deterministic sheet;
re-run-stable).

**Scope (as the dispatch mandates): C1 bears on the _magnitude_ of the
per-word / EX (union-sieve) route only. It does not answer C2 or C3.** It
does not stand in for them and is not allowed to.

Script diff (pure insertion; the regenerated table diff is
`83a84,105`, a pure insertion; no pre-existing byte changed -- verified by
`difflib` opcodes = `{'insert'}` only, so STOP condition 2 does **not**
fire):

````diff
159a160,192
> # -- T9.S3.Lceil (Dispatch C, C1): the SAME cost m ln m re-priced at the
> #    D0-EXACT rank m = L_ceil = 2J+1 (anchored budget_sheet_20.py L_ceil()
> #    form; C_0 = 2/ln 3), reported ALONGSIDE the grid-L columns above.
> #    Section 5 permits ONLY this addition; every grid column above is
> #    left byte-identical.  This block adds NO new column to any other
> #    table and changes no existing value.
> emit("-- T9.S3.Lceil  Dispatch-C C1 re-run: cost m ln m at the D0-EXACT")
> emit("   rank m = L_ceil = 2J+1, J = ceil(log2(ceil(13 C_0 A'' ln x))),")
> emit("   ALONGSIDE the grid-L T9.S3 columns above (which are unchanged).")
> emit("x        m=L_ceil   expo[exp(m ln m)]   vs (G1)/(G2)")
> for e in SCALES:
>     lnx, llx, L, k = regime(e)
>     lnx_f = float(lnx_of(e))
>     Dex = math.ceil(13 * float(C0) * APP * lnx_f)
>     Jex = math.ceil(math.log2(Dex))
>     Lex = 2 * Jex + 1
>     cost_ceil = Lex * log(Lex)
>     emit("1e%-5d %10d %14.3f        SUPERPOLYLOG: FAILS (G1) HARDER; PASSES (G2)"
>          % (e, Lex, float(expo(cost_ceil, llx))))
> emit("  -> exact m = 2J+1 exceeds grid m = (2/ln2)lnln x by ~3.7x (1e8) ..")
> [ ... 12 further prose emit() lines; the scope note reproduced above ... ]
> emit("")
````

The grid T9.S3 / T9.S2 / T10 / T11 columns and the disclosure block are
byte-identical to the anchor (`diff` confirmed). No conclusion elsewhere in
the sheet changes.

---

## 3. C2 -- necessity

**Question (dispatch).** Is the failing gate necessary for `CG`, or was it
calibrated for the route `CG` bypasses?

**Step 1 -- the bypass is real (Section D).** The direct route is
`SparseFlankFamily` $`\wedge`$ `CollisionGapAlongScales`
$`\Longrightarrow`$ `CollisionDeficitSupply` $`\Longrightarrow`$
`ExchangeSupply1` (`collision-gap-audit.md` l.356-362). Its consumed-hypothesis
table (l.366-380) records: `MatchedFlankLower` **not** needed;
`RelExtensionUpper` **not** needed; `TailIntersection` only **upstream in the
proved derivation of (SF)**. So Position 2(a)'s premise is factually correct:
`CG` drops exactly the two integration requirements around which the old
$`1/64`$ interface was calibrated. `PROVED-DOSSIER` (Section D table).

**Step 2 -- what `F17.9` at l.471 does and does not cover.** The wall the S3
cost fails is `F17.9`, the $`o(\ln{}x)`$ gate at exchange rank. Its scope,
`relext-statements.md` l.467-473 (governing sentence, rule 19):

> "every displayed sieve constant ... is $`\exp((1+o(1))k\ln{}k)`$ =
> superpolylog (budget T1) and fails the $`o(\ln{}x)`$ gate at exchange rank.
> **`F17.9` is proved only against `k`-uniform per-word constants: (abs) is
> the shape it kills.**"

So `F17.9` is a **shape-specific** obstruction: it kills the absolute-normalized
**per-word** sieve constant (the (abs)/EX shape). It does **not**, by itself,
reach the averaged/relative (rel) shape -- the corpus names that as the
"`F17.9`-evading lane" (l.476-479; `7.5` l.1048-1052). This is the scope the
dispatch flags as "precisely the question": read at face value, `F17.9` alone
does not show the gate survives the drop to `CG`'s averaged shape.

**Step 3 -- necessity is nonetheless established for the Maynard input,
because the rank cost is priced on `CG`'s aggregate object directly.** The
gap in Step 2 is filled without appeal to `RelExtensionUpper`. Any **sieve**
upper bound on `CG`'s own aggregate collision object -- the `B2.pairs`
numerator / $`W_2`$ / the rho-energy transfer (RE1) -- pays a rank cost one
floor up:

- `mechanism-inventory.md` l.76-79 (governing sentence): "any upper bound on
  $`W_2`$ (or on `B2.pairs`' numerator) that **sieves the UNION of the two
  translated point sets** pays a sieve constant at rank up to $`2k`$:
  $`\exp((1+o(1))2k\ln2k)`$, superpolylog -- the `F17.9` wall one floor up."
- `collision-gap-audit.md` l.748 (barrier row F20.3): "a direct union-sieve
  proof of $`Q`$, $`W_{2,M}`$, or (RE1) still pays the superpolylogarithmic
  rank-$`2k`$ cost. `PROVED-DOSSIER` route arithmetic; route-specific."

This rank-$`2k`$ pricing is intrinsic to sieving a matched-flank pair
correlation at $`D0`$ depth; it does **not** consume `MatchedFlankLower` or
`RelExtensionUpper`. The rank itself ($`m\sim L`$ per-word, $`2k`$ for the
union) is $`D0`$-forced -- the flank length $`J+K=L-1`$ is the class
geometry, on the **same** site set $`S_x^{\prime(s)}`$ and the **same**
parameter map, which `CG` inherits unchanged (`relext-statements.md` E-table
l.392: the proposed target "neither states nor implies `HLQuantA`, and it
drops rather than adds tuple-wise uniformity"; `separator-repricing.md`
W4.0 l.360-364).

**Answer to C2.** The gate is necessary for **every route that consumes the
Maynard input**: the per-word/EX route at rank $`m\sim L`$ (`F17.9`/(abs),
l.471-473; T9.S3), and the aggregate/union-sieve route at rank $`2k`$
(F20.3; M1 l.76-79). It was **not** merely calibrated for the bypassed
`RelExtensionUpper` route -- the rank-$`2k`$ pricing lands on `CG`'s aggregate
object independently of that route. The one route `F17.9` does not reach --
the direct (rel)/AR averaged lane -- is not a Maynard route at all (C3);
its obstruction is a different, absent input (S1). Support: `PROVED-DOSSIER`
(F20.3 route arithmetic; Section D; M1 mandatory line), inherited, not
upgraded here.

---

## 4. C3 -- aggregation

**Question (dispatch).** Does a per-word cost failure block an aggregate
proportion statement? Construct the aggregation, or show why it cannot close.

**The aggregate object.** `CG` asks for $`Q(x,s)\le(1-\eta_s)N`$ on an
unbounded per-$`s`$ scale sequence. Via (SF) ($`F/N\to0`$,
`collision-gap-audit.md` C.1) and the exact identity B.3
(l.170-177),

$$
 N-F-Q=\sum_P\frac{2}{N_P}\sum_{d<e}N_{P,d}N_{P,e}\ge0,
$$

`CG` is equivalent to a **positive-proportion, class-normalized** middle-split
deficit: $`N-F-Q\ge(\eta_s-o(1))N`$. Two facts fix what "aggregation" can and
cannot buy.

**(i) Class normalization is load-bearing; the raw global pair ratio is
provably insufficient.** The unnormalized side/word collision counts
$`V_2=\sum_PN_P(N_P-1)`$ and $`W_2=\sum_{P,d}N_{P,d}(N_{P,d}-1)`$ are **both**
proved $`\to\infty\cdot N`$ (`proofs.md` C2 and remark (c), l.130-147: pair-vs-
site mass mismatch at astronomical class multiplicities). But their ratio is
not enough: `collision-gap-audit.md` I l.736-742 exhibits a $`u`$-family with
$`W_2/V_2\to0`$ while $`Q/N\to1`$, so "an unnormalized global pair ratio still
cannot supply (CG); **class normalization or equivalent stratum control
remains load-bearing**" (F20.2 row, l.741). So "summing over side words" must
be done class-normalized (the $`Q`$ statistic) or stratified
($`W_{2,M}\le\theta V_{2,M}`$, G.3 l.598-617).

**(ii) The worked bound: aggregating the _Maynard input_ pays a rank cost in
both realizations -- it multiplies, not cancels.** To lower-bound the deficit
one must upper-bound the same-middle mass $`\sum_P(1/N_P)\sum_dN_{P,d}^2=Q+F`$.
Maynard is a **sieve**; its two sieve realizations of this upper bound are:

- *Per-word / full-word (EX).* Bound $`N_{P,d}`$ (the count realizing a full
  length-$`L`$ word) by a rank-$`L`$ sieve. Cost
  $`\exp((1+o(1))L\ln{}L)`$ per word (T9.S3; C1's $`L_{\mathrm{ceil}}`$ column,
  expo $`22`$--$`37`$). Summing over a positive proportion of the
  $`F=x^{o(1)}`$ classes only adds a further $`x^{o(1)}`$ factor: strictly
  larger, still (G1)-failing.
- *Aggregate / union (the very "summing over side words" the attack names).*
  Bound the matched-flank **pair** count by sieving the union of the two
  translated point sets. Cost $`\exp((1+o(1))2k\ln2k)`$, rank $`2k`$
  (M1 l.76-79; F20.3 l.748; G.3 l.623-625: "the obvious sieve estimate for
  $`W_{2,M}`$ still counts rank-$`2k`$ unions and hits F20.3").

Worked comparison: rank-$`2k\;=\;2(L+1)`$ **exceeds** rank-$`L`$, and
$`\exp(2k\ln2k)/\exp(L\ln{}L)\to\infty`$. So aggregating the Maynard input
**multiplies** the per-word cost -- exactly the artifact's one-line answer
(`separator-repricing.md` W4.S3 l.396-397, "Aggregating ... only multiplies
the per-word rank-$`L`$ cost"), here supplied as a corpus-grounded derivation
rather than an assertion. `PROVED-DOSSIER` (F20.3; M1 mandatory line; G.3).

**(iii) The one aggregate route that _does_ evade the rank cost is not a
Maynard route.** The corpus records a genuine wall-evading lane
(`relext-statements.md` 7.5 l.1048-1052, governing sentence): "the GLOBAL
PAIR-COUNTING lane ... bound $`\sum_P(N_{P,d_P}-1)_+`$ by word-collision pair
counts against side-collision pair counts, **so that no per-word sieve
constant (hence no `F17.9` wall) ever appears**." Its enabling input is an
**upper equidistribution / word-grain mean-value** carrier:
`collision-gap-audit.md` G.2 l.533-536 -- "a class-relative proof needs an
`NI-M2`-type carrier; a dispersion proof needs `NI-M4`" -- both `Recorded
obstruction`, `OPEN` ("a weaker genuinely averaged carrier is **not ruled
out**, but none is in the corpus", F20.4/F20.5 l.749-750;
`mechanism-inventory.md` M2/M4 l.126-137, l.233-238). This carrier is
`separator-repricing.md`'s **S1** (W4.S1 l.474-478, l.491-500), an
upper/equidistribution input "strictly beyond-`HLQuantA` content." Maynard is
a **lower-bound clustering / existence** input (`proofs.md` C4 SCOPE
l.342-346, listed as a *distinct*, non-middle-slot failure-in-model family;
`literature.md` l.80-81: the Maynard--Tao circle yields dense clusters and
constant-pattern-mod-$`q`$ consecutive primes, "keine gleiche Luecken" -- no
same-gap matched flanks). A lower-bound existence tool cannot supply an upper
mean-value carrier. So the wall-evading aggregate route **does not consume
S3**; it consumes S1.

**Answer to C3.** A per-word cost failure does **not** in general block an
aggregate proportion statement -- and here it does not, in the abstract: `CG`'s
averaged shape has a wall-evading route. But that route consumes **S1**, not
Maynard. For the **Maynard input specifically**, both aggregation realizations
(per-word rank-$`L`$, union rank-$`2k`$) are superpolylog and (G1)-failing, so
aggregating S3 does not recover an affordable deficit -- it multiplies the
cost. The residual open aggregate route is S1's absent carrier, which Maynard
cannot feed.

---

## 5. C4 -- the grade

The dispute is **not** mis-stated (STOP condition 4 does not fire): Positions
1 and 2 are the real disagreement. It is decided as follows.

**Grade: `PROVED-DOSSIER`**, upheld, read as a **route-exhaustive,
member-specific negative on the Maynard input** -- Dispatch C's admissible
outcome "Position 1 upheld." The disputed clause 1 stands. What the artifact
lacked, and this note supplies, is the derivation answering (a) and (b), not
the grade.

Support classification, clause by clause:

- *S3 fails on a rank cost $`\exp((1+o(1))m\ln{}m)`$, $`m\sim L`$, per-word
  (EX) route.* `PROVED-DOSSIER`. (`proofs.md` C4 SCOPE l.342-346;
  `relext-statements.md` l.467-473; T9.S3; magnitude confirmed and
  strengthened by C1's $`L_{\mathrm{ceil}}`$ column, C1 above.)
- *The rank is $`D0`$-forced and invariant under `B2.pairs`->`CG`; the
  relaxation touches strength / $`s`$-uniformity / scale-density, never the
  rank.* `PROVED-DOSSIER`. (Same site set / parameter map inherited by `CG`,
  `relext-statements.md` E-table l.392; `separator-repricing.md` W4.0
  l.360-364. Uncontested by Position 2 and confirmed here.)
- *Every route that consumes Maynard pays the rank cost -- per-word at rank
  $`m\sim L`$, aggregate-by-union-sieve at rank $`2k`$.* `PROVED-DOSSIER`
  (C2, C3; F20.3 l.748 "route arithmetic"; M1 l.76-79). **This is the clause
  the artifact asserts but does not derive; it is derived here.** It is what
  earns the grade: adjoining Maynard to the tool list yields no affordable
  `CG` proof by any Maynard route.

**Retained conditional (obstruction discipline, binding).** "S3 does not
survive" is a **located obstruction relative to the named inventory $`T`$**
(`collision-gap-audit.md` l.772-773), a statement about recorded routes that
consume Maynard -- never that `CG`, or the input `1311.4600`, is unprovable,
impossible, or absolute. The per-word-wall-evading aggregate/AR global-
pair-counting route to `CG` remains genuinely **`OPEN`**; its carrier is the
absent averaged middle-slot input `NI-M2`/`NI-M4` -- right regime (rank
$`\sim k`$, window $`A'L\ln{}x`$), right shape, absent from the corpus -- i.e.
**S1**, which the artifact already grades `OPEN`/undecidable-at-corpus-grain
(`separator-repricing.md` W4.S1 verdict l.666-677) and which Maynard does not
and cannot feed. So the componentization S3 `PROVED-DOSSIER` / S1 `OPEN` is
internally consistent, and clause 1 is entitled to its grade.

**On the two Position-2 grounds, explicitly.**

- *(a) Necessity -- fails as an attack, but names a real derivation gap.* The
  gate is necessary for every Maynard route (C2), priced on `CG`'s aggregate
  object directly, so it was not merely calibrated for the bypassed route. The
  attack correctly observes the artifact does not derive this -- it asserts
  invariance ("touches strength/uniformity/density, never rank") without
  addressing the `MatchedFlankLower`/`RelExtensionUpper` drop or the aggregate
  pricing. The gap is fillable and here filled.
- *(b) Aggregation -- fails as an attack, but names a real derivation gap.*
  Summing over side words does not recover a cheap deficit **for Maynard**:
  the sieve aggregation pays rank-$`2k`$, worse (C3). The attack correctly
  observes the artifact's one-line answer is asserted, not worked; the worked
  bound is supplied here, and it corroborates the artifact.

**Both-readings on `1311.4600` (binding).** *What it gives:* the bounded-gap /
dense-cluster machinery exists and **fails in the model** (all model gaps
$`\to\infty`$), so Maynard is a genuine model-failing input; via Gallagher its
fixed-$`k`$ averaged face is Poissonian -- the right *shape* for an averaged
carrier (`literature.md` l.54). *What it does not give at growing rank:* the
Gallagher/Maynard analysis holds "$`k`$ fixed throughout" (l.54); at growing
rank $`m\sim L`$ the uniform sieve control is superpolylog (T6 M3(c); T9.S3);
the consecutive-prime results are **constant-pattern-mod-$`q`$**, not the
same-gap matched-flank coincidences the exchange needs (Banks--Freiberg--
Turnage-Butterbaugh, l.80); and the growing-rank transfer has "no known
techniques to unconditionally obtain asymptotics" (Tao--Teravainen, l.89). So
at growing rank Maynard supplies **neither** an affordable per-word/union-sieve
upper bound **nor** the averaged `NI-M2`/`NI-M4` carrier (the latter being
S1's, of the opposite -- upper/equidistribution -- flavor). Both readings
recorded.

**Method note (adversarial verification).** The verdict here reverses the
direction this executor first leaned. An initial reading treated the aggregate
route as "S3's open aggregate sub-route" and inclined toward "S3-vs-`CG` OPEN."
A four-lens corpus-only refuter panel (Position-1 defender; corpus-fidelity;
S1-vs-S2 landing; Maynard growing-rank) plus a synthesis judge -- run against
the anchored files -- showed that inclination to be an overreach that
double-counts S1's openness under the S3 label: the wall-evading aggregate
route consumes S1's carrier, not Maynard, and every actual Maynard route pays
the rank cost. The load-bearing correction is the rank-$`2k`$ pricing of the
aggregate object (M1 l.76-79; F20.3 l.748), which the initial reading had
under-weighted. The corrected verdict is the one above.

---

## 6. What could not be decided, and the deciding fact

Everything the dispatch asked about **S3** is decided: clause 1 is
`PROVED-DOSSIER` as a member-specific negative on the Maynard input.

The one thing this dispatch does **not** decide -- and is explicitly barred
from re-opening (Section 5: do not re-open S1) -- is whether the wall-evading
aggregate/AR route to `CG` can be **proved**. That is **S1's** open question,
not S3's, and it turns on a single deciding fact, named identically in the
artifact (`separator-repricing.md` W4.S1 verdict l.502-508):

> an unconditional **averaged middle-slot non-concentration / upper-uniformity
> (word-grain mean-value)** statement at rank
> $`k=(2/\ln2+o(1))\ln\ln{}x`$, window $`A'L\ln{}x`$, of strength enough to
> keep a fixed proportion of $`D0`$-depth site mass off its modal middle on
> some unbounded scale sequence per $`s`$ -- a statement that **fails in the
> even-Cramer-smooth model** (i.e. `NI-M2`/`NI-M4`).

Its presence or absence in the mathematical literature is not resolvable at
corpus grain (web OFF; the anchored shelf records it as absent, F20.4/F20.5).
That fact decides S1, not S3, and is the searchable/provable object. Its
resolution would **not** rehabilitate Maynard: even were the carrier found, it
would be an S1 input, and the S3 rank-cost negative on the Maynard input would
stand unchanged.

No literature fact outside the anchored corpus was required to decide S3
(STOP condition 1 did not fire on that ground). Deciding C2/C3 did **not**
require re-opening the barrier, the endpoint, or any other separator (STOP
condition 3 does not fire): the argument stays inside the S3 row and the
already-recorded F20.2/F20.3/F20.4/F20.5 barrier taxonomy.

---

## 7. Hashes

New hashes of the two changed files (post-C1):

    eedef5e23e00d7c2690b9580c0ea3ff22dde34a0cc4c1eb24c63947202d899b0
      dossier/item-0010-workpapers/budget_sheet_20_ext.py
    11660525a92bc49dfb0818f8f61bbc31894b78e04783a5abe04728059a5ec476
      dossier/item-0010-workpapers/budget_sheet_20_ext_tables.txt

Regenerated from the script (deterministic; identical on re-run). The anchored
`dossier/item-0020-workpapers/budget_sheet_20.py`
(`bbce2f58...b0d`) and `writeup/status.md` (`3663dc9e...3e51`) are byte-identical
at close.

This note's own sha256 is computed over its finalized bytes at close and
reported by the executor at hand-off (a file cannot contain its own hash).

Outputs (Dispatch C Section 8): this note; the `L_ceil` addition to
`budget_sheet_20_ext.py` and its regenerated `budget_sheet_20_ext_tables.txt`;
nothing else. The executor commits nothing and pushes nothing.
