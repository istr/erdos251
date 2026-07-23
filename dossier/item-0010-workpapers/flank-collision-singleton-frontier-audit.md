# Flank-collision singleton-frontier audit for item-0010

Date: 2026-07-23. Execution pin:
`67661c6f83516b07df1f402c8a375d9b3600d6c6` (verified exactly before
the audit). Web OFF. Local computation only. No Lean file, frozen M5-lite
registry, historical production artifact, roadmap item, run, or payload was
changed.

Evidence labels are load-bearing:

- `FORMAL` means proved in the checked Lean tree.
- `PROVED-DOSSIER` means proved at repository dossier grain but not supplied
  by a Lean theorem.
- `PROVED` means an exact finite or elementary derivation recorded here.
- `MEASURED-PRODUCTION` means an exact count in the frozen Phase-3b
  production artifacts.
- `MEASURED-AUDIT` means a new exact finite calculation in this audit over
  the existing regenerable local prime-gap cache.
- `MEASURED-CONTEXT` means an exact item-0019 count from a different,
  explicitly labeled parameter or filter world.
- `HEURISTIC` means a model, extrapolation, or resource projection.
- `OPEN` means unresolved.

No finite observation below is promoted to an asymptotic statement.

Primary repository sources are
`m5-lite-phase3b-optimization-report.md`,
`m5-lite-measurement-report.md`,
`m5-lite-phase3b/production/global-per-scale.json`,
`m5-lite-measurement-registry.yaml`, `m5-lite-audit.md`,
`collision-gap-audit.md`, `dossier/relext-upper.md`,
`dossier/relext-statements.md`,
`dossier/item-0020-workpapers/proofs.md`,
`dossier/item-0020-workpapers/mechanism-inventory.md`, and
`dossier/item-0019-workpapers/item-0019-final-report.md`. Relevant ledger
entries through ANN-61 and the complete compact Phase-3b artifact set were
also audited.

## A. Executive verdict

The frozen seven-scale, five-threshold campaign is completely singleton
[MEASURED-PRODUCTION]. At all 35 rows,

$$
N=F,\qquad Q=0,\qquad N-F-Q=0.
$$

The largest row is $`(x,s)=(10^9,0)`$ with
$`N=F=50{,}827{,}008`$. Thus H1, H2, and H3 all failed to occur, and

$$
C_{\mathrm{flank}}=\sum_P\binom{N_P}{2}=0
$$

at every row.

The committed compact artifacts do not retain exact side words. This audit
therefore required an exact equality-refinement pass over the existing
regenerable cache. It reproduced the committed site counts and found each
complete prefix and complete suffix individually unique on all seven
$`s=0`$ rows [MEASURED-AUDIT]; deletion then proves the same for all 35
rows. At $`10^9`$, the canonical joint key has 47 pair collisions at
$`6+6`$ and zero at $`7+7`$; all four first/last sensitivity paths are
zero by $`8+8`$. The exact all-row dense mesh has no sustained asymmetric
ridge and no zero/nonzero status change under $`s\le1000`$. Joint
uniqueness is therefore already explained at one-sided grain, although
combining shorter sides accelerates it. The off-diagonal product model
matches positive canonical joint counts within about 4 percent through
$`6+6`$, a calibrated finite fact rather than an independence claim.

The observed singleton regime is unsurprising under the calibrated stress
models considered here [HEURISTIC]. Transporting the measured per-coordinate
collision retention across unmeasured coordinates and D0 jumps gives an
order-one birthday region only around $`10^{27}`$ to $`10^{30}`$.
This is a sensitivity envelope, not a confidence interval; sparse zeros,
unmeasured coordinates, and future key changes leave the exact crossover
`OPEN`.

D0 dimension growth can reset collision buildup. The present
$`J=K=15`$ interval ends at
$`x=3{,}368{,}925{,}490{,}843`$; $`J=K=16`$ begins at the next integer.
Within a constant-depth interval $`C_{\mathrm{flank}}`$ is nondecreasing
[PROVED]. Across a jump, the key is neither a refinement nor a coarsening;
global monotonicity must not be assumed.

The existing sparse-family proof is fully compatible with the finite
singletons. At $`10^9`$, its displayed analytic capacity upper bound is
about $`3.13\times10^{41}`$ times actual $`N`$. Including D0 jumps, that
displayed bound does not permanently beat the population comparator until
about $`3.53\times10^{106}`$ [numerical evaluation of
`PROVED-DOSSIER` bounds]. The tighter proved binomial cap moves this only to
about $`1.20\times10^{105}`$; neither is a prediction.

Recommended next action: land the reproducible flank-only diagnostic, then,
under separate dispatch, use $`3\times10^9`$ and $`10^{10}`$ as
constant-depth validation probes. Do not start a blind search toward the
heuristic H1 region or introduce a redundant analytic Prop.

For finite search, the primary event is

$$
\boxed{F<N,\ \text{not }Q>0.}
$$

If the first such row has $`Q=0`$, every repeated member in every repeated
flank has a different middle. A direct non-rigid matched-flank witness is
then guaranteed, not merely likely.

## B. Exact finite milestone algebra

### B.1 Full-flank collision count

Fix a finite filters-first site set $`T=T_{s,x}`$. Write

$$
N=\lvert T\rvert,\qquad
F=\lvert\mathrm{Fam}(T)\rvert,
$$

and let $`N_P`$ be the size of a realized exact flank class. The realized
classes partition $`T`$, so

$$
\sum_P N_P=N.
$$

Because every realized class is nonempty,

$$
N-F=\sum_P(N_P-1).
$$

Define

$$
C_{\mathrm{flank}}
=\sum_P\binom{N_P}{2}.
$$

Then [PROVED]

$$
2C_{\mathrm{flank}}
=\sum_PN_P(N_P-1).
$$

Every summand in both expressions is nonnegative. For $`N>0`$,

$$
\boxed{
F=N
\iff
\forall P,\ N_P=1
\iff
\max_PN_P=1
\iff
C_{\mathrm{flank}}=0.
}
$$

For $`N=0`$, the first, second, and fourth conditions remain equivalent;
the maximum needs an explicit empty-family convention, such as zero.

The cleanest computational form is to exact-sort the full flank keys, take
their run lengths $`m`$, and accumulate

$$
F\mathrel{+}=1,\qquad
C_{\mathrm{flank}}\mathrel{+}=\frac{m(m-1)}2,\qquad
N-F\mathrel{+}=m-1.
$$

This requires no middle census. A hash may partition work, but exact word
comparison must resolve every equal-hash run.

### B.2 H1, H2, and H3 are different

For a middle value $`d`$ inside class $`P`$, let $`N_{P,d}`$ be its
multiplicity. The exact item-0010 statistic is

$$
Q
=\sum_P\frac1{N_P}
  \sum_dN_{P,d}(N_{P,d}-1).
$$

The three milestones are:

| Milestone | Exact criterion | Finite meaning |
| --- | --- | --- |
| H1 | $`F<N`$, equivalently $`C_{\mathrm{flank}}>0`$ | Some full flank repeats. |
| H2 | $`N-F-Q>0`$ | Some full flank realizes at least two different middles. |
| H3 | $`Q>0`$ | Some middle occurs at least twice inside one full flank. |

The classwise identity from `collision-gap-audit.md` is [PROVED]

$$
\begin{aligned}
N-F-Q
&=
\sum_P
\left(
N_P-1-\frac1{N_P}\sum_dN_{P,d}(N_{P,d}-1)
\right)\\
&=
\sum_P\frac2{N_P}
\sum_{d<e}N_{P,d}N_{P,e}.
\end{aligned}
$$

It follows exactly that:

1. H2 implies H1.
2. H3 implies H1.
3. H2 does not imply H3: one class with middle counts $`(1,1)`$ has
   positive defect and $`Q_P=0`$.
4. H3 does not imply H2: one rigid class with middle count $`(2)`$ has
   $`Q_P>0`$ and zero defect.
5. H2 and H3 can occur together, for example with middle counts
   $`(2,1)`$.

Since the summands defining $`Q`$ are nonnegative,

$$
Q=0
\iff
\forall P,d,\quad N_{P,d}\le1.
$$

Therefore

$$
\boxed{
F<N,\ Q=0
\Longrightarrow
N-F-Q=N-F>0.
}
$$

This is the best possible first finite outcome for the direct exchange route:
every repeated flank is automatically non-rigid.

### B.3 Extraction into the formal exchange interface

Suppose a row with filter parameter $`s=t`$ has $`F<N`$ and $`Q=0`$.
Choose a repeated realized side pair $`w=(a,c)`$ and two of its sites.
Their full flanks agree and their middles differ. The clause-table tail of
`supply_of_triple` in `lean/Erdos251/Supply.lean` then supplies:

- the depths from `length_of_mem_realizedFamily`;
- filtered membership and the matching prefix/suffix clauses from
  `mem_classSites`;
- the threshold and near/far delta caps from `site_clauses`;
- positive depths from `one_le_J` and `one_le_K`;
- the real gate from `D_le_two_pow_J`.

The filtered-site clause gives $`t+1\le n,m`$, which is stronger than the
$`t\le n,m`$ conjuncts required by `ExchangeSupply1`. This part of the
clause construction is `FORMAL`; the finite selection algebra above is
`PROVED` but is not a named Lean theorem.

One such row supplies the witness for one requested threshold $`t`$. It
does not by itself prove the full universally quantified `ExchangeSupply1`;
one suitable row must be chosen for every $`t`$. Once that supply exists,
`dyadic_of_exchange_supply` in `lean/Erdos251/Exchange.lean` formally yields
the item-0010 non-dyadic conclusion.

## C. Prefix, suffix, and joint collision decomposition

### C.1 Exact objects

For a site, let $`a`$ be its exact $`J`$-gap prefix word and $`c`$ its
exact $`K`$-gap suffix word. Define

$$
N_a^{\mathrm{pre}},\qquad
N_c^{\mathrm{suf}},\qquad
N_{a,c},
$$

and

$$
\begin{aligned}
C_{\mathrm{pre}}
&=\sum_a\binom{N_a^{\mathrm{pre}}}{2},\\
C_{\mathrm{suf}}
&=\sum_c\binom{N_c^{\mathrm{suf}}}{2},\\
C_{\mathrm{flank}}
&=\sum_{a,c}\binom{N_{a,c}}2.
\end{aligned}
$$

These use the unchanged D0 side words and the exact filters-first site set.
No side word was redefined.

### C.2 Artifact limitation and audit reconstruction

All 448 committed Phase-3b stream-bucket JSON files were inspected. They
retain exact aggregate class, middle, certificate, rho, and CRT summaries,
but no exact `sides`, `mid`, `first_site`, or reconstructible per-class key.
The transient in-memory record has side words, but the compact production
path discards them. The older raw NPZ path also omitted side words. The
optimization report explicitly records that the abandoned raw checkpoints
were removed and that no temporary checkpoint is authoritative.

The one-sided and truncated statistics therefore cannot be recovered from
committed output. The audit used the existing regenerable local arrays
$`p`$, $`g`$, and $`\delta`$ to reconstruct the site sets at each frozen
scale [MEASURED-AUDIT]. It checked:

- `int64`, `int16`, and `float64` dtypes for $`p`$, $`g`$, and
  $`\delta`$;
- compatible lengths and $`g_i=p_{i+1}-p_i`$ over every cached row;
- positive gaps, with measured maximum 282, below the exact packing base
  32,768;
- exact reproduction of all 35 committed values of $`N`$ before computing
  collisions.

Equality classes were refined recursively by the next exact gap coordinate.
No probabilistic hash certified equality. Singleton classes were pruned
because no later coordinate can merge them. For a current $`s=0`$ class of
size $`m`$, if the threshold removes $`r_s`$ of its actual sites, its exact
positive-threshold contribution is

$$
\binom{m-r_s}{2}.
$$

This deletion update computed every truncated count for
$`s=1,10,100,1000`$ without re-sorting the retained bulk. At $`x=10^6`$,
all eight paths at all four positive thresholds were independently checked
against separate full refinements.

The cache is uncommitted and is not a production artifact. To identify this
audit run, the SHA-256 of the raw concatenation in scale order, with
`p`, `g`, and `delta` at each scale, is
`7a67845d8be67c109890aab3b228e6ba6f52e7613af762dd1a45a5768cfc3c91`.
The final all-threshold panel and parity-mesh drivers have SHA-256 values
`71ec763e5fd0d3cac7c5516ce7396c723edf1b135d372016d18d21e95ca7f9bf`
and
`d7aff3f8ed962e8a2439c2cef610dcfc0c299191daa98d3a6aadee419417f9cd`.
The raw concatenations of their seven JSON results in scale order have
SHA-256 values
`700d743b06c8a9ce2043de6653daa22fac1217de029aa6e1010ba499709fc564`
and
`db8ffa41471d3a79a38e7724dc8c25e2d133536bf3bc421ce7e2bed14593ace8`,
respectively. These hashes identify the new measurement inputs and run; they
do not turn temporary cache files into frozen production evidence.

The final pass computed four complete one-sided coordinate orders, four
corner-to-corner paired-coordinate paths, and the canonical efficient dense
subset defined in Section D, for every one of the 35 measured rows. Every
$`s=0`$ path agrees exactly with the independent pilot pass. All
depth/threshold monotonicities, overlapping mesh cells, and
joint-to-marginal inequalities passed. The unmeasured odd off-diagonal cells
of the complete two-dimensional surface are not silently inferred.

### C.3 Complete-side result

The frozen production singleton rows are [MEASURED-PRODUCTION]:

| $`x`$ | $`(D,J,K)`$ | $`N=F`$ for $`s=0,1,10,100,1000`$ |
| ---: | ---: | --- |
| $`10^6`$ | $`(15695,14,14)`$ | 78,261; 78,260; 78,251; 78,161; 77,261 |
| $`3\times10^6`$ | $`(16943,15,15)`$ | 216,578; 216,577; 216,568; 216,478; 215,578 |
| $`10^7`$ | $`(18310,15,15)`$ | 664,306; 664,305; 664,296; 664,206; 663,306 |
| $`3\times10^7`$ | $`(19558,15,15)`$ | 1,857,274; 1,857,273; 1,857,264; 1,857,174; 1,856,274 |
| $`10^8`$ | $`(20926,15,15)`$ | 5,759,779; 5,759,778; 5,759,769; 5,759,679; 5,758,779 |
| $`3\times10^8`$ | $`(22174,15,15)`$ | 16,247,074; 16,247,073; 16,247,064; 16,246,974; 16,246,074 |
| $`10^9`$ | $`(23542,15,15)`$ | 50,827,008; 50,827,007; 50,826,998; 50,826,908; 50,826,008 |

The corresponding exact side/truncation summary for $`s=0`$ is
[MEASURED-AUDIT]:

| $`x`$ | $`N`$ | $`J=K`$ | Last positive one-sided depth and count | First zero one-sided depth | Canonical $`C_{6,6}`$ | Canonical $`C_{7,7}`$ | All four tested joint paths zero by |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| $`10^6`$ | 78,261 | 14 | depth 13: 1 | 14 | 0 | 0 | $`7+7`$ |
| $`3\times10^6`$ | 216,578 | 15 | depth 13: 1 | 14 | 0 | 0 | $`7+7`$ |
| $`10^7`$ | 664,306 | 15 | depth 13: 1 | 14 | 0 | 0 | $`7+7`$ |
| $`3\times10^7`$ | 1,857,274 | 15 | depth 13: 1 | 14 | 2 | 0 | $`7+7`$ |
| $`10^8`$ | 5,759,779 | 15 | depth 13: 2 | 14 | 3 | 0 | $`7+7`$ |
| $`3\times10^8`$ | 16,247,074 | 15 | depth 14: 1 | 15 | 9 | 0 | $`7+7`$ |
| $`10^9`$ | 50,827,008 | 15 | depth 14: 7 | 15 | 47 | 0 | $`8+8`$ |

At every reconstructed $`s=0`$ row, both the complete prefix and complete
suffix have multiplicity histogram

$$
\lbrace 1:N\rbrace.
$$

Thus [MEASURED-AUDIT]

$$
C_{\mathrm{pre}}=C_{\mathrm{suf}}=0,\qquad
\max_aN_a^{\mathrm{pre}}
=\max_cN_c^{\mathrm{suf}}=1.
$$

For fixed $`x`$, every positive-$`s`$ site set is a subset of the
$`s=0`$ set and uses the same side keys. Deleting sites cannot create a
collision. Hence complete prefix and complete suffix uniqueness extends to
all 35 production rows [PROVED], using the measured $`s=0`$ uniqueness.
The number of sites whose complete prefix and complete suffix both repeat
is zero on every
production row. In particular, there are no sites whose complete sides each
repeat with different partners. The full joint uniqueness through $`10^9`$
is already explained at one-sided grain.

This does not mean the one-sided frontier is remote. From $`10^8`$ to
$`3\times10^8`$, the last one-sided collision moved from depth 13 to depth
14. At $`10^9`$, seven pairs still collide at depth 14 and the fifteenth
coordinate resolves all of them. An imminent complete-side collision is not
the same event as a full-flank collision: the canonical paired word is
already unique at $`7+7`$.

### C.4 Item-0019 continuity context

Item-0019 measured collisions at smaller fixed depths. These are
`MEASURED-CONTEXT`, not rows of the coupled D0 M5-lite campaign.
At $`x=10^9`$ in its fixed `D0.2'` world:

| $`(J,K,D)`$ | $`C_{\mathrm{flank}}`$ | Non-rigid repeated classes |
| ---: | ---: | ---: |
| $`(4,5,30)`$ | 47,994 | 25,155 |
| $`(5,5,34)`$ | 4,955 | 2,334 |
| $`(6,6,64)`$ | 88 | 29 |
| $`(7,6,44)`$ | 10 | 3 |
| $`(7,7,67)`$ | 0 | 0 |
| $`(8,8,67)`$ | 0 | 0 |

Its separate fixed `D0.2` (without the prime) $`(7,7)`$ stretch found 5
repeated flank classes, 2 non-rigid, at $`5\times10^9`$, and 10 repeated
classes, 3 non-rigid, at $`10^{10}`$. These rows use different depths, cap
values, and filter worlds.
They cannot be spliced into the D0 collision curve or used as a D0
probability estimate. They do show that an initial collision batch need not
be entirely rigid or entirely non-rigid; after H1, the exact defect must be
computed. The special case $`Q=0`$ remains a logical guarantee of
non-rigidity.

## D. Truncated collision curves

### D.1 Definitions and checks

For $`1\le j\le J`$ and $`1\le k\le K`$, define the canonical
truncations by the first $`j`$ prefix gaps and first $`k`$ suffix gaps.
Let

$$
C_{\mathrm{pre}}(j),\qquad
C_{\mathrm{suf}}(k),\qquad
C_{\mathrm{joint}}(j,k)
$$

be their exact pair-collision counts. At depth zero,

$$
C_{\mathrm{pre}}(0)
=C_{\mathrm{suf}}(0)
=C_{\mathrm{joint}}(0,0)
=\binom N2.
$$

The efficient dense subset was declared before its computation. Put

$$
E_r
=
\lbrace1,r\rbrace
\cup
\lbrace2u:1\le2u\le r\rbrace
$$

and

$$
\mathcal G_{J,K}
=
(E_J\times E_K)
\cup
\lbrace(d,d):1\le d\le\min(J,K)\rbrace.
$$

Every full-grid point is within one step in each coordinate of
$`\mathcal G_{J,K}`$. It contains both endpoint depths, the full point,
every balanced depth, and unequal-depth probes. The audit computed all
canonical one-sided depths, $`C_{\mathrm{joint}}`$ on this mesh, and four
first/last-oriented diagonals for all 35 rows. This is 70 canonical cells
when $`J=K=14`$ and 87 when $`J=K=15`$, instead of 196 and 225.

Exact refinement gives the integrity relations

$$
C_{\mathrm{joint}}(j,k)
\le
\min\left(
C_{\mathrm{pre}}(j),C_{\mathrm{suf}}(k)
\right),
$$

nonincreasing in each coordinate, and

$$
C_{\mathrm{joint}}(J,K)=C_{\mathrm{flank}}.
$$

All computed rows satisfy these checks.

### D.2 Largest-row canonical curve

At $`(x,s)=(10^9,0)`$, the exact canonical curves are
[MEASURED-AUDIT]:

| Depth | $`C_{\mathrm{pre}}(j)`$ | $`C_{\mathrm{suf}}(j)`$ | $`C_{\mathrm{joint}}(j,j)`$ |
| ---: | ---: | ---: | ---: |
| 1 | 72,359,250,499,989 | 72,357,516,689,370 | 4,055,151,700,425 |
| 2 | 4,756,979,696,674 | 4,756,827,409,549 | 17,563,494,520 |
| 3 | 362,106,893,755 | 362,095,634,402 | 102,351,305 |
| 4 | 30,172,202,198 | 30,171,381,075 | 718,544 |
| 5 | 2,673,529,685 | 2,673,468,038 | 5,746 |
| 6 | 249,611,576 | 249,606,202 | 47 |
| 7 | 24,407,892 | 24,407,406 | 0 |
| 8 | 2,490,175 | 2,490,131 | 0 |
| 9 | 263,747 | 263,743 | 0 |
| 10 | 28,790 | 28,790 | 0 |
| 11 | 3,285 | 3,286 | 0 |
| 12 | 413 | 413 | 0 |
| 13 | 59 | 59 | 0 |
| 14 | 7 | 7 | 0 |
| 15 | 0 | 0 | 0 |

The pair count falls by roughly one to two orders of magnitude with each
early coordinate. The one-sided sparse tail persists much longer than the
joint tail.

### D.3 Exact all-threshold panel

In this table, each five-entry vector is ordered by
$`s=0,1,10,100,1000`$. The final scalar in each row is common to all four
one-sided coordinate orders and all five thresholds:

| $`x`$ | $`C_{\mathrm{joint}}(6,6)`$ | $`C_{\mathrm{joint}}(7,7)`$ | Last positive depth/count on each one-sided path, all five $`s`$ |
| ---: | --- | --- | ---: |
| $`10^6`$ | 0; 0; 0; 0; 0 | 0; 0; 0; 0; 0 | 13: 1 |
| $`3\times10^6`$ | 0; 0; 0; 0; 0 | 0; 0; 0; 0; 0 | 13: 1 |
| $`10^7`$ | 0; 0; 0; 0; 0 | 0; 0; 0; 0; 0 | 13: 1 |
| $`3\times10^7`$ | 2; 2; 2; 2; 2 | 0; 0; 0; 0; 0 | 13: 1 |
| $`10^8`$ | 3; 3; 3; 3; 3 | 0; 0; 0; 0; 0 | 13: 2 |
| $`3\times10^8`$ | 9; 9; 9; 9; 9 | 0; 0; 0; 0; 0 | 14: 1 |
| $`10^9`$ | 47; 47; 47; 47; 47 | 0; 0; 0; 0; 0 | 14: 7 |

These are exact positive-threshold measurements, not deletion-lemma
inferences. The early-site deletions do change dense truncated counts. The
largest absolute change in the eight-path panel is
$`3{,}933{,}603{,}528`$ at $`(x,s)=(10^9,1000)`$, where
$`C_{\mathrm{pre}}(1)`$ falls from 72,359,250,499,989 to
72,355,316,896,461, only 0.005436 percent. The largest relative change at
a sparse positive cell is 50 percent, from 2 to 1; among cells initially at
least 100, it is 12 percent, from 175 to 154. No mesh cell changes
zero/nonzero status for $`s\le1000`$.

### D.4 Canonical off-diagonal mesh

The parity mesh tests whether the diagonal hides an asymmetric ridge.
The $`s=0`$ summary is:

| $`x`$ | Unordered transpose pairs with a zero/nonzero mismatch | Largest $`j+k`$ with a positive mesh count | Maximum transpose ratio when both counts are at least 100 |
| ---: | ---: | ---: | ---: |
| $`10^6`$ | 3 | 13 | 1.01743 |
| $`3\times10^6`$ | 1 | 12 | 1.02200 |
| $`10^7`$ | 1 | 12 | 1.03565 |
| $`3\times10^7`$ | 2 | 12 | 1.01687 |
| $`10^8`$ | 0 | 13 | 1.09412 |
| $`3\times10^8`$ | 0 | 14 | 1.08175 |
| $`10^9`$ | 2 | 14 | 1.05449 |

Here the transpose ratio is
$`\max(C_{j,k}/C_{k,j},C_{k,j}/C_{j,k})`$. The mismatch count and deepest
positive depth are unchanged across all five thresholds. At $`10^9`$, the
deepest positive cells are

$$
C_{4,10}=2,\qquad C_{6,8}=1,\qquad
C_{10,4}=2,\qquad C_{12,2}=1,
$$

while $`C_{8,6}=C_{2,12}=0`$. Thus the only transpose mismatches at that
scale sit at the one-pair floor. No sustained prefix-heavy or suffix-heavy
ridge appears on the dense mesh [MEASURED-AUDIT]. A very narrow feature
confined to unsampled odd off-diagonal cells is not ruled out; the scalable
campaign specification therefore retains the full-grid output.

### D.5 Coordinate-position sensitivity

The audit also added coordinates from each end of each side. At $`10^9`$:

| Diagonal path | Count at six coordinate pairs | Count at seven coordinate pairs | Count at eight coordinate pairs |
| --- | ---: | ---: | ---: |
| first prefix, first suffix | 47 | 0 | 0 |
| last prefix, first suffix | 88 | 0 | 0 |
| first prefix, last suffix | 50 | 1 | 0 |
| last prefix, last suffix | 47 | 0 | 0 |

The four paths differ by at most a factor of two at the sparse six-pair
level. Prefix and suffix one-sided counts likewise agree closely throughout
the curve. This finite symmetry gives no evidence that one early or late
coordinate block uniquely dominates. It also gives no theorem of
stationarity: the collision-retention rate changes materially with depth.

The four paths and the canonical parity mesh answer different questions:
the paths stress coordinate position, while the mesh stresses unequal
prefix/suffix depth. Together they form the predeclared efficient dense
subset; they are not described as the complete 225-cell surface.

## E. Collision entropy and unseen-support audit

### E.1 Exact empirical quantities

For $`N>0`$ and exact multiplicities $`N_z`$, put $`p_z=N_z/N`$ and

$$
C=\sum_z\binom{N_z}{2}.
$$

Entropy values use the natural logarithm.

Then [PROVED]

$$
\sum_zp_z^2
=\frac1{N^2}\sum_zN_z^2
=\frac{N+2C}{N^2},
$$

$$
\sum_zN_z(N_z-1)=2C,
$$

and the empirical Renyi-2 quantities are

$$
H_2^{\mathrm{Renyi}}
=2\log{}N-\log{}(N+2C),
\qquad
S_2
=\frac{N^2}{N+2C}.
$$

These are exact properties of the observed empirical distribution. They are
not estimates of an unseen word law. The transformation was applied to every
one-sided path and threshold count; the tables below show representative
largest-row values rather than reproducing all 35 derived entropy arrays.

At $`10^9`$, the canonical $`6+6`$ key has $`C=47`$ and

$$
S_2=50{,}826{,}914.00017\ldots,
$$

almost $`N=50{,}827{,}008`$. Yet its off-diagonal pair-collision support,
defined diagnostically as

$$
S_{\mathrm{pair}}
=\frac{\binom N2}{C},
$$

is about $`2.75\times10^{13}`$. The diagonal self mass makes the plug-in
$`S_2`$ about $`5.4\times10^5`$ times smaller than this sparse
off-diagonal quantity. At depth $`7+7`$, $`C=0`$ and the plug-in calculation gives
$`S_2=N`$ only because every observed atom is a singleton.

Therefore

$$
\boxed{
C=0\Longrightarrow S_2=N
\quad\text{does not estimate latent support or the next collision rate.}
}
$$

### E.2 Product-of-marginals calibration

Let $`B_N=\binom N2`$. Using off-diagonal pair rates, the independent
product-of-marginals prediction is

$$
C_{\mathrm{joint}}^{\mathrm{prod}}(j,k)
=
\frac{
C_{\mathrm{pre}}(j)C_{\mathrm{suf}}(k)
}{B_N}.
$$

At $`10^9`$ on the canonical diagonal:

| Depth | Actual joint count | Product prediction | Actual / prediction |
| ---: | ---: | ---: | ---: |
| 1 | 4,055,151,700,425 | $`4.05339\times10^{12}`$ | 1.00043 |
| 2 | 17,563,494,520 | $`1.75182\times10^{10}`$ | 1.00259 |
| 3 | 102,351,305 | $`1.01508\times10^8`$ | 1.00831 |
| 4 | 718,544 | 704,763 | 1.01955 |
| 5 | 5,746 | 5,533.51 | 1.03840 |
| 6 | 47 | 48.23 | 0.97440 |
| 7 | 0 | 0.461 | censored zero |

This is unusually good finite calibration through the positive-count range.
It answers the dependence audit on the canonical diagonal: the product
count has at most a few percent error before the sparse floor. It does not
justify probabilistic independence, and it has no full-word content once
both empirical one-sided counts are zero.

The off-diagonal mesh gives a broader check:

| $`(j,k)`$ | Actual joint count | Product prediction | Actual / prediction |
| ---: | ---: | ---: | ---: |
| $`(1,10)`$ | 1,703 | 1,612.786 | 1.05594 |
| $`(10,1)`$ | 1,615 | 1,612.747 | 1.00140 |
| $`(2,10)`$ | 119 | 106.026 | 1.12236 |
| $`(10,2)`$ | 117 | 106.023 | 1.10353 |
| $`(4,8)`$ | 57 | 58.1661 | 0.97995 |
| $`(8,4)`$ | 63 | 58.1656 | 1.08312 |

Once counts fall to one or two, ratios can fluctuate by factors near three
and zeros are censored. The table therefore calibrates dependence only
where collisions remain adequately populated.

Write $`N_a=N_a^{\mathrm{pre}}`$ in this paragraph. When
$`C_{\mathrm{pre}}(j)>0`$, the exact conditional decomposition for distinct
unordered site pairs is

$$
\frac{C_{\mathrm{joint}}}{B_N}
=
\frac{C_{\mathrm{pre}}}{B_N}
\sum_{a:\,N_a\ge2}
\frac{\binom{N_a}{2}}{C_{\mathrm{pre}}}
\frac{\sum_c\binom{N_{a,c}}2}{\binom{N_a}{2}}.
$$

The sum is the weighted same-suffix rate among pairs already known to share
a prefix. When also $`C_{\mathrm{suf}}(k)>0`$, replacing that conditional
rate by the marginal distinct-pair rate $`C_{\mathrm{suf}}/B_N`$ gives
exactly the product column above. Thus actual/prediction is exactly the
off-diagonal conditional dependence factor

$$
\kappa(j,k)
=
\frac{C_{\mathrm{joint}}(j,k)B_N}
{C_{\mathrm{pre}}(j)C_{\mathrm{suf}}(k)}.
$$

It ranges from 0.974 to 1.038 through the positive depths in the canonical
diagonal table. F4 does not materially move the finite depth-six crossover
relative to F1. It supplies no full-word correction after the conditional
cells themselves reach the singleton floor.

### E.3 Executed block increments and censored direct fit

For the canonical $`(10^9,0)`$ paths, the exact empirical entropy increments
$`\Delta H_2(d)=H_2(d)-H_2(d-1)`$ are [MEASURED-AUDIT]:

| Added depth $`d`$ | Prefix $`\Delta H_2`$ | Suffix $`\Delta H_2`$ | Joint-diagonal $`\Delta H_2`$ |
| ---: | ---: | ---: | ---: |
| 1 | 2.882 | 2.882 | 5.764 |
| 2 | 2.722 | 2.722 | 5.440 |
| 3 | 2.575 | 2.575 | 4.925 |
| 4 | 2.484 | 2.484 | 1.587 |
| 5 | 2.415 | 2.415 | 0.02766 |
| 6 | 2.284 | 2.284 | 0.0002242 |

The one-sided increments decline steadily, so an i.i.d. per-gap collision
entropy is not supported. The abrupt joint flattening is mostly the empirical
self-mass ceiling $`H_2\le\log{}N`$, not evidence that latent word
complexity stops growing.

For F5, ordinary least squares on the six positive values
$`\log{}C_{\mathrm{joint}}(d,d)`$, $`1\le d\le6`$, gives slope
$`-5.019`$ per added coordinate pair and $`R^2=0.99944`$
[MEASURED-AUDIT]. This calculation has consecutive slopes drifting from
about $`-5.44`$ to $`-4.81`$, exposing finite-depth structure despite the
high $`R^2`$.
The zero at depth seven is treated as censored at the zero-count floor; it
was not entered as $`\log{}0`$. This fit diagnoses the observed curve but
is not a confidence-bearing extrapolation to the full word.

### E.4 Model-route ranking

The routes F1--F5 rank as follows for the present data:

1. **F5, direct same-world truncation fit.** This uses the closest observed
   object. Positive counts must be fit with zeros treated as censoring, not
   by taking $`\log{}0`$.
2. **F4, conditional suffix given prefix.** This is exact empirically and
   can detect dependence missed by a marginal product, but it becomes sparse
   quickly.
3. **F2, block collision-entropy increments.** Use adjacent-coordinate
   blocks and position terms. The changing retention rate rules out an
   i.i.d. gap-symbol fit.
4. **F1, product of marginals.** It is well calibrated through depth
   $`6+6`$, but extrapolation beyond the one-sided zero floor is unsupported.
5. **F3, birthday conversion.** This converts a separately justified latent
   support into an expected collision count; it is not itself a support
   estimator.

### E.5 Crossover stress test

For a deliberately simple sensitivity model, write the per-coordinate
collision retention as

$$
q(x)\approx\frac{\gamma}{\log{}x}
$$

and use

$$
\mathbb E C_{\mathrm{flank}}
\approx
\binom{N(x,0)}2q(x)^{2J(x)}.
$$

The $`10^9`$ joint depth-six count gives
$`\gamma\approx1.57`$. The one-sided depth-14 count gives
$`\gamma\approx1.98`$. The increase with depth is itself evidence against
stationary coordinates, so these values define a stress envelope rather
than fitted constants.

Using $`N\approx1.05x/\log{}x`$ and the exact stepwise D0 depth gives
[HEURISTIC]:

- at $`10^9`$, expected full-flank collisions of roughly
  $`3\times10^{-19}`$ to $`3\times10^{-16}`$;
- throughout the current $`J=15`$ interval, expected collisions still well
  below one;
- immediately before the $`J=16`$ to $`J=17`$ jump, a range from roughly
  $`2\times10^{-4}`$ to $`3\times10^{-1}`$;
- an order-one region in the $`J=17`$ interval around
  $`10^{27}`$ to $`10^{30}`$.

The uncertainty is much larger than that displayed range suggests.
Unmeasured tail-coordinate dependence, the changing filters, and D0 key
shifts can move it by many orders of magnitude. The correct conclusion is:
the observed zero count is compatible with calibrated finite models, while
the actual crossover scale is `OPEN`.

## F. D0 dimension growth and singleton-frontier definitions

### F.1 Exact depth map and jump points

The frozen D0 map is

$$
C_0=\frac2{\log{}3},\qquad
D(x)=\left\lceil\frac{1248}{\log{}3}\log{}x\right\rceil,
$$

$$
J(x)=K(x)=\left\lceil\log_2{}D(x)\right\rceil,
\qquad
L(x)=2J(x)+1.
$$

Because $`1248=2^5\cdot39`$, the real interval for $`J=m`$ is

$$
3^{\,2^{m-6}/39}
<
x
\le
3^{\,2^{m-5}/39}.
$$

Relevant integer starts are:

| New depth | First integer $`x`$ |
| ---: | ---: |
| $`J=15`$ | 1,835,464 |
| $`J=16`$ | 3,368,925,490,844 |
| $`J=17`$ | 11,349,658,962,853,566,790,172,100 |
| $`J=18`$ | approximately $`1.288\times10^{50}`$ |
| $`J=19`$ | approximately $`1.659\times10^{100}`$ |

Only the $`14\to15`$ jump occurs inside the measured ladder.

### F.2 What is monotone

Fix $`s`$ and an interval on which $`J,K`$ are constant. As $`x`$
increases:

- the prime-anchor cutoff includes more sites;
- $`D(x)`$ and $`W(x)`$ do not decrease;
- the far cap $`2^K`$ is fixed;
- the exact flank equivalence relation is fixed.

Thus old qualifying sites remain and old equal flank keys remain equal.
Every class multiplicity, $`N-F`$, and $`C_{\mathrm{flank}}`$ is
nondecreasing [PROVED] directly from the dossier definitions. Once H1
occurs in such an interval, it persists to the interval's end.

At a simultaneous $`J,K`$ jump, the situation is different. For old depth
$`r`$:

- the old middle becomes the new last prefix coordinate;
- the old first suffix coordinate becomes the new middle;
- the new suffix drops that old coordinate and appends two farther gaps;
- the filter indices and window length also change.

The new key is neither a refinement nor a coarsening, and the site sets need
not be nested. A collision can appear or disappear. The observed resolution
of depth-14 one-sided collisions by coordinate 15 illustrates that an added
coordinate can separate a pair, but it is not an observed cross-jump reset.

### F.3 Recommended frontier terminology

The finite diagnostic

$$
\mathrm{SingletonFlanks}(x,s)
:\iff
F(x,s)=N(x,s)
$$

is useful dossier terminology. It is not a needed analytic Prop.

A global minimum

$$
X_{\mathrm{first}}(s)
=
\min\left\lbrace x:F(x,s)<N(x,s)\right\rbrace
$$

is mathematically well-defined if the set is nonempty, but it is not a
persistence threshold across D0 jumps. Reports should distinguish:

1. the first collision on a declared finite ladder;
2. the first collision inside one constant-$`(J,K)`$ interval;
3. paired values immediately before and after a D0 jump;
4. eventual collision existence supplied by `SparseFlankFamily`.

The model-dependent balance quantity

$$
B_{\mathrm{model}}(x)
=2\log{}N(x,s)-H_{\mathrm{pred}}(x)
$$

has the birthday interpretation

$$
\mathbb E C_{\mathrm{flank}}
\approx\frac12e^{B_{\mathrm{model}}}.
$$

At $`10^9`$, the stress envelope gives roughly
$`-42\le B_{\mathrm{model}}\le-35`$. A D0 depth increment multiplies
the modeled collision count by approximately $`q(x)^2`$, producing a
sawtooth. This paragraph is `HEURISTIC`; the fixed-interval monotonicity
above is `PROVED`.

For reference, applying the same $`\gamma\in[1.57,1.98]`$ stress envelope
to the measured $`s=0`$ populations gives:

| $`x`$ | $`J`$ | Stress range for $`B_{\mathrm{model}}`$ |
| ---: | ---: | ---: |
| $`10^6`$ | 14 | -38.36 to -31.86 |
| $`3\times10^6`$ | 15 | -42.97 to -36.01 |
| $`10^7`$ | 15 | -43.05 to -36.09 |
| $`3\times10^7`$ | 15 | -42.98 to -36.01 |
| $`10^8`$ | 15 | -42.74 to -35.78 |
| $`3\times10^8`$ | 15 | -42.40 to -35.44 |
| $`10^9`$ | 15 | -41.92 to -34.96 |

The drop between the first two rows is the modeled $`14\to15`$ reset. This
table is a transport of the largest-row calibration, not a separate fit at
each scale.

## G. Quantitative sparse-family threshold audit

### G.1 Numerical bounds on measured rows

Put

$$
r=J+K,\qquad
M=\left\lfloor\frac34L\log{}x\right\rfloor.
$$

The positive-even composition count used in the item-0020 proof gives

$$
F\le
B_{\mathrm{cap}}(x)
:=\binom Mr.
$$

and the displayed simplification is

$$
B_{\mathrm{cap}}(x)
\le
U_{\mathrm{cap}}(x)
:=
\left(
\frac{3e}{4}\frac Lr\log{}x
\right)^r.
$$

The eventual population expression is

$$
P_0(x)
:=
\frac{x}{8C_0\log{}x}
=
\frac{x\log{}3}{16\log{}x}.
$$

The proof supplies $`N(x,s)\ge P_0(x)`$ only after its fixed-$`s`$
analytic gates. Numerically, actual measured $`N`$ exceeds $`P_0`$ at
every frozen row.

| $`x`$ | $`(r,M)`$ | Actual $`N`$ range over the five $`s`$ values | $`B_{\mathrm{cap}}`$ | $`U_{\mathrm{cap}}`$ | $`P_0`$ | $`B_{\mathrm{cap}}/N`$ range | $`U_{\mathrm{cap}}/N`$ range | $`B_{\mathrm{cap}}/P_0`$ |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| $`10^6`$ | $`(28,300)`$ | 77,261--78,261 | $`2.04415\times10^{39}`$ | $`1.04461\times10^{41}`$ | 4,970.013 | $`2.612\times10^{34}`$--$`2.646\times10^{34}`$ | $`1.335\times10^{36}`$--$`1.352\times10^{36}`$ | $`4.113\times10^{35}`$ |
| $`3\times10^6`$ | $`(30,346)`$ | 215,578--216,578 | $`1.53604\times10^{43}`$ | $`8.23791\times10^{44}`$ | 13,811.728 | $`7.092\times10^{37}`$--$`7.125\times10^{37}`$ | $`3.804\times10^{39}`$--$`3.821\times10^{39}`$ | $`1.112\times10^{39}`$ |
| $`10^7`$ | $`(30,374)`$ | 663,306--664,306 | $`1.75198\times10^{44}`$ | $`8.45858\times10^{45}`$ | 42,600.112 | $`2.637\times10^{38}`$--$`2.641\times10^{38}`$ | $`1.273\times10^{40}`$--$`1.275\times10^{40}`$ | $`4.113\times10^{39}`$ |
| $`3\times10^7`$ | $`(30,400)`$ | 1,856,274--1,857,274 | $`1.42490\times10^{45}`$ | $`6.11489\times10^{46}`$ | 119,645.292 | $`7.672\times10^{38}`$--$`7.676\times10^{38}`$ | $`3.292\times10^{40}`$--$`3.294\times10^{40}`$ | $`1.191\times10^{40}`$ |
| $`10^8`$ | $`(30,428)`$ | 5,758,779--5,759,779 | $`1.16883\times10^{46}`$ | $`4.64575\times10^{47}`$ | 372,750.980 | $`2.029\times10^{39}`$--$`2.030\times10^{39}`$ | $`8.066\times10^{40}`$--$`8.067\times10^{40}`$ | $`3.136\times10^{40}`$ |
| $`3\times10^8`$ | $`(30,453)`$ | 16,246,074--16,247,074 | $`6.80595\times10^{46}`$ | $`2.64124\times10^{48}`$ | 1,055,313.857 | $`4.189\times10^{39}`$--$`4.1893\times10^{39}`$ | $`1.6257\times10^{41}`$--$`1.6258\times10^{41}`$ | $`6.449\times10^{40}`$ |
| $`10^9`$ | $`(30,481)`$ | 50,826,008--50,827,008 | $`4.36160\times10^{47}`$ | $`1.59086\times10^{49}`$ | 3,313,342.047 | $`8.5813\times10^{39}`$--$`8.5814\times10^{39}`$ | $`3.12995\times10^{41}`$--$`3.13001\times10^{41}`$ | $`1.316\times10^{41}`$ |

Actual $`F=N`$ is many orders below both capacity bounds. There is no
conflict: an upper bound can be extremely larger than the realized family.

### G.2 Capacity/population comparator crossovers

The following high-precision roots include the stepwise D0 depth changes.
They compare the capacity bounds to $`\alpha P_0`$ and therefore estimate
the capacity/population part of the proof. The repository proof does not
record an explicit numerical onset for every fixed-$`s`$ TailIntersection
gate, so these are not certified exact values of the final
$`X(s,\alpha)`$.

| Bound | First temporary $`\mathrm{cap}<P_0`$ window begins | Reset | Permanent $`\mathrm{cap}<P_0`$ crossover | Permanent $`\mathrm{cap}<P_0/2`$ crossover | Permanent $`\mathrm{cap}<P_0/10`$ crossover |
| --- | ---: | ---: | ---: | ---: | ---: |
| Displayed $`U_{\mathrm{cap}}`$ | $`1.43\times10^{100}`$ | $`J=19`$ jump near $`1.66\times10^{100}`$ | $`3.53\times10^{106}`$ | $`8.05\times10^{106}`$ | $`5.44\times10^{107}`$ |
| Proved binomial $`B_{\mathrm{cap}}`$ | $`4.98\times10^{98}`$ | same jump | $`1.20\times10^{105}`$ | $`2.74\times10^{105}`$ | $`1.86\times10^{106}`$ |

At the $`J=19`$ jump, the displayed ratio
$`U_{\mathrm{cap}}/P_0`$ rises from about 0.883 to about
$`1.96\times10^5`$. Conditional on the eventual population gate already
being available, the displayed comparison would temporarily imply a
collision and then lose that implication, even though `SparseFlankFamily`
eventually proves permanent dominance.

For fixed depth and $`t=\log{}x`$,

$$
\frac{d}{dt}
\log{}\left(\frac{U_{\mathrm{cap}}}{P_0}\right)
=
\frac{r+1}{t}-1.
$$

The displayed proof ratio therefore worsens throughout the current
$`J=15`$ interval, whose upper endpoint has $`t<31`$. This is behavior
of the crude bound, not behavior of actual collisions.

The dominant delay is the high-dimensional composition term together with
D0 depth growth. Freezing $`J=15`$ would make the displayed comparator cross
near $`10^{81.3}`$; D0 growth postpones its permanent crossover by about 25
decades.
As a coefficient-sensitivity substitution [HEURISTIC], replacing the
Chebyshev coefficient by the measured finite population scale shifts only
about 1.4 decades. Replacing the displayed power by the proved binomial
shifts about 1.5 decades by deterministic bound arithmetic. Constants in the
population lower bound are not the main obstruction.

The displayed roots were obtained by bisection in $`t=\log{}x`$ separately
inside each exact D0 interval. For the binomial roots, the computation
enumerated the integer values of $`M`$, intersected each constant-$`M`$
interval with the D0 interval, and bisected the logarithmic comparison
using the exact binomial logarithm. This preserves both the D0 and
$`\lfloor W/2\rfloor`$ step changes.

## H. M5-lite relevance before H1

### H.1 Classification

| Classification | Quantities | Verdict before a repeated flank |
| --- | --- | --- |
| Singleton-trivial | $`Q/N=0`$; $`N-F-Q=0`$; zero violation mass; classwise profile pass; $`\lambda_{\max}=0`$; majority escape and Gini margins | These contain no middle-contraction evidence because every class has size one. Positive declared or post hoc profile values can be self-pair artifacts. |
| Informative upstream | Exact $`N,F`$; D0 parameters; side spans; residual-domain sizes; one-sided and truncated collisions; prospective $`A_P`$; existing finite rho and CRT summaries as contextual structural descriptors | These describe the site and word geometry. Persistence beyond the measured ladder remains `HEURISTIC` or `OPEN`. |
| Premature for the H1 search | Recomputing full realized-rho energy or prospective rho for every frontier row; recomputing CRT contribution decompositions for $`Q`$; collision correlations | These are downstream of a collision. A flank-only pass should omit them until H1, then compute them only if separately justified. |

This is not retroactive criticism of M5-lite. The campaign established the
complete singleton frontier, independently validated the optimized exact
kernel, and preserved useful infrastructure. It changes the next campaign's
objective from middle contraction to locating H1.

### H.2 What $`A_P`$ means

At $`(x,s)=(10^9,0)`$, the exact prospective admissible-middle counts are
[MEASURED-PRODUCTION]:

| $`A_P`$ | Site/class mass |
| ---: | ---: |
| 0 | 6 |
| 1 | 32,263,625 |
| 2 | 14,709,040 |
| 3--4 | 3,638,540 |
| 5--8 | 213,312 |
| 9--16 | 2,475 |
| 17 or more | 10 |

Thus 63.477 percent of the site/class mass has $`A_P=1`$, 92.417 percent
has $`A_P\le2`$, and 99.575 percent has $`A_P\le4`$. The exact inverse
corrected-support mean is

$$
\frac{71439963679889}{88963528642560}
=0.8030252933\ldots.
$$

$`A_P`$ excludes finite-anchor inadmissibility exceptions. For an exact
finite identity, define

$$
\widetilde A_P
=
A_P+
\left\lvert
\left\lbrace
\text{distinct exceptional realized middles in }P
\right\rbrace
\right\rvert.
$$

The six measured $`A_P=0`$ classes are precisely contaminated by this
finite-anchor issue; their corrected supports are nonzero. The displayed
inverse mean uses $`\widetilde A_P`$, not raw $`A_P`$.

$`A_P`$ counts prospective admissible middles conditional on a realized
flank. It is not $`N_P`$, a flank support size, or a flank-collision
probability. A flank can have several prospective middles and still occur
once, as every measured class does.

The small $`A_P`$ distribution is adverse finite context for the stronger
`B2.pairs` target: if a repeated class has corrected support one, it must be
middle-rigid. The exact Cauchy lower audit is

$$
\frac QN
\ge
\frac1N\sum_P\frac{N_P}{\widetilde A_P}
-\frac FN.
$$

At the singleton rows $`F/N=1`$, so this lower bound is inert. Any claim
that the measured inverse-support mass persists while $`F/N\to0`$ would be
an unproved asymptotic extrapolation.

### H.3 Statement-layer consequence

A new `RepeatedFlankAlongScales` Prop is mathematically redundant.
`SparseFlankFamily` already gives [PROVED-DOSSIER], for every fixed
$`s`$ and $`\alpha>0`$,

$$
\exists X(s,\alpha)\ \forall x\ge X(s,\alpha):
\qquad
N(x,s)>0,\quad F(x,s)<\alpha N(x,s).
$$

Taking any $`\alpha<1`$ gives eventual H1, stronger than arbitrarily large
collision rows. `SingletonFlanks` should remain diagnostic terminology.
A genuinely new interface would need an effective finite threshold or a
quantitative collision law, neither of which is proved here.

## I. Flank-only frontier campaign specification

### I.1 Required row output

For every exact D0 filters-first row, emit:

$$
x,\ s,\ J,\ K,\ N,\ F,\ N-F,\ \max_PN_P,
$$

$$
C_{\mathrm{flank}},\quad
C_{\mathrm{pre}},\quad
C_{\mathrm{suf}},
$$

and the full exact arrays

$$
\left(C_{\mathrm{pre}}(j)\right)_{1\le j\le J},
\quad
\left(C_{\mathrm{suf}}(k)\right)_{1\le k\le K},
\quad
\left(C_{\mathrm{joint}}(j,k)\right)_{
1\le j\le J,\ 1\le k\le K}.
$$

Also emit repeated-site mass, repeated-class count, maximum multiplicity,
and multiplicity histograms for every one-sided depth and a declared dense
joint summary.

Enforce:

$$
F=N
\iff
\forall P,\ N_P=1
\iff
C_{\mathrm{flank}}=0,
$$

and, when $`N>0`$,

$$
F=N\iff\max_PN_P=1.
$$

$$
2C_{\mathrm{flank}}
=\sum_PN_P(N_P-1),
$$

the depth monotonicities, the joint-to-marginal inequality, and
$`C_{\mathrm{joint}}(J,K)=C_{\mathrm{flank}}`$.

### I.2 Immediate H1 spill

If $`F<N`$, atomically retain every repeated exact full flank with:

- its exact side word, plus a stable hash used only as an index;
- $`N_P`$;
- exact site indices and anchor primes;
- realized middle values and all $`N_{P,d}`$;
- the threshold, window, near-cap, and far-cap checks for every site;
- $`Q_P`$, rigidity defect, and a direct-Exchange-witness flag.

If $`Q=0`$, stop the downstream diagnostic expansion and record that the
non-rigid witness is algebraically guaranteed. Rho is not needed for this
conclusion.

### I.3 Exact scalable implementation

1. Regenerate or load $`p,g,\delta`$ with source and data hashes. Check
   dtypes, lengths, $`g_i=p_{i+1}-p_i`$, gap bounds, and D0 boundary
   stability.
2. Stream the $`s=0`$ filters-first sites in bounded chunks.
3. For full flanks, use a deterministic fixed hash only to shard records.
   Exact-sort and compare the complete gap tuples inside every shard.
4. Spill only repeated full groups. Near the current frontier this output is
   tiny.
5. Build exact recursive prefix and suffix IDs from
   `(parent_id, next_gap)`. Count each pair
   `(prefix_id_j, suffix_id_k)` exactly for the $`C_{j,k}`$ grid.
   Existing full-side hash buckets cannot count prefix collisions because
   equal prefixes may lie in different full-side buckets.
6. Derive the positive-$`s`$ panel by decrementing the actual early-site
   memberships, following Phase-3b. Do not assume blindly that
   $`N_s=N_0-s`$ on future rows.
7. Merge shards in fixed order and retain a manifest of source, input,
   parameter, output, and worker-independent merge hashes.

At $`10^9`$, materializing all 30 int16 side coordinates would use about
3.05 GB before sorting overhead. Retaining a uint32 exact ID at every side
depth would use about 6.10 GB. Sequential memory mapping, radix grouping,
and external sorting are preferable to holding all depth matrices at once.

### I.4 Scale strategy

The three candidate strategies have different roles:

- **K1, geometric ladder:** use factors of 3 and 10 for broad validation.
  It is simple but can hide a D0 reset.
- **K2, constant-depth probing:** prioritize this inside the enormous
  current $`J=K=15`$ interval. Collision counts are monotone there.
- **K3, near-jump pairs:** for the real jump boundary
  $`b_m=3^{2^{m-5}/39}`$, measure
  $`\lfloor b_m\rfloor`$ and $`\lfloor b_m\rfloor+1`$ with one reusable
  stream. This directly measures reset behavior.

Recommended hybrid:

1. turn the audit's exact all-row parity-mesh logic into the reusable
   memory-bounded full-grid diagnostic and replay it through $`10^9`$;
2. if separately dispatched, run $`3\times10^9`$ and $`10^{10}`$ as
   constant-$`J=15`$ validation probes;
3. add $`3\times10^{10}`$ only if the model or curve shape changes
   materially;
4. require a segmented sieve and external grouping before larger rows;
5. reserve the next-jump pair near $`3.369\times10^{12}`$ for that
   segmented implementation.

This schedule is for calibration, not a claim that H1 is likely at
$`10^{10}`$.

### I.5 Runtime and storage audit

The full Phase-3b $`10^9`$ row took 3,762.2 seconds and peaked at
3,491,920 KiB [MEASURED-PRODUCTION]. From the existing cache and without
rho, the final exact all-threshold eight-path process took 770.9 seconds and
4,303,216 KiB; the 87-cell parity-mesh process took 317.8 seconds and
4,224,072 KiB
[MEASURED-AUDIT]. They overlapped in time, so these are process-local figures,
not an aggregate benchmark. The sum of their peak resident sets is a
conservative overlap envelope of 8,527,288 KiB, or 8.132 GiB; aggregate RSS
was not instrumented. Both drivers favored audit clarity over minimum
memory.

The cache-to-eight-path pass was materially shorter than the recorded full
Phase-3b row; this is not an end-to-end comparison. The production report
identifies deterministic class construction and exact reduction as the
post-kernel bottleneck. A production mesh should share refinement states in
one memory-bounded pipeline instead of overlapping two independent large
processes.

Conservative unchanged-pipeline projections are [HEURISTIC]:

| $`x`$ | Projected wall time | Projected peak memory |
| ---: | ---: | ---: |
| $`3\times10^9`$ | about 3.0 hours | about 9.5 GiB |
| $`10^{10}`$ | about 9.4 hours | about 30 GiB |
| $`3\times10^{10}`$ | about 27 hours | about 86 GiB |
| $`10^{11}`$ | about 85 hours | about 272 GiB |

A flank-only external-sort pipeline should improve these numbers, but it
must be benchmarked before promising a factor. The current dense cache uses
roughly $`18\pi(x)`$ bytes for $`p,g,\delta`$ plus a dense sieve of order
$`x`$ bytes; it is not the architecture for the next D0 jump.

All repository computation must remain on the local workstation or on
separately operator-managed infrastructure. It must not be delegated to
Codex Cloud.

## J. Route recommendation

1. **Is $`F=N`$ through $`10^9`$ surprising?** No, not under any
   calibrated stress fit used here [HEURISTIC]. The exact finite result is
   nevertheless valuable because the full-word unseen support was not known
   in advance.

2. **Which part of the exact flank causes uniqueness?** Both complete
   one-sided words are individually unique at every measured $`s=0`$ row
   [MEASURED-AUDIT]. The canonical joint key becomes unique by $`7+7`$ at
   $`10^9`$, while each side needs all 15 coordinates. Joint combination is
   strong, but it acts on sides which are already individually complex.

3. **Where is the first full-flank collision plausibly expected?** The
   calibrated stationary-coordinate stress envelope reaches order one only
   around $`10^{27}`$ to $`10^{30}`$ [HEURISTIC]. This is not a confidence
   interval, and the actual frontier is `OPEN`.

4. **How uncertain is that estimate?** Extremely. Current measurements
   calibrate at most 14 coordinates per side, zeros are censored, and D0
   jumps change both the key and filters. Shifts of many orders of magnitude
   are plausible.

5. **Does D0 growth push the frontier outward?** Structurally, it can reset
   collisions because the key is nonnested. In the stress model, each
   simultaneous depth increment multiplies expected collisions by roughly
   $`q(x)^2`$, producing a large sawtooth drop [HEURISTIC].

6. **How late is the collision forced by the sparse-family proof?** The
   displayed capacity/population comparison becomes permanent near
   $`3.53\times10^{106}`$; the tighter proved binomial comparison gives
   about $`1.20\times10^{105}`$. These are numerical proof-bound
   crossovers, subject to the proof's non-explicit fixed-$`s`$ population
   onset, not actual frontier predictions.

7. **What should the next computation do?** The required exact all-row dense
   subset and conditional audit are complete. First land their
   memory-bounded full-grid implementation; then use $`3\times10^9`$ and
   $`10^{10}`$ only as model-validation probes under a separate dispatch.
   Do not spend a blind campaign trying to reach the current heuristic H1
   scale, and do not return to realized rho before H1.

8. **If H1 occurs with $`Q=0`$, does an Exchange witness appear?** Yes,
   exactly. Every repeated cell is then a singleton, so any repeated full
   flank has different middles and the existing formal clause table extracts
   an `ExchangeAt` witness satisfying the threshold conjuncts of
   `ExchangeSupply1`. If $`Q>0`$, H1 alone does not guarantee non-rigidity;
   the defect must be checked immediately.

The prioritized next action is therefore:

$$
\boxed{
\text{land the reusable exact full-grid diagnostic, then validate it at
two larger constant-depth rows.}
}
$$

No new analytic statement, Lean change, roadmap state change, or
beyond-$`10^9`$ campaign is warranted by this audit alone.
No kickoff stop condition fired.
