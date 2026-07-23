# item-0010 M5-lite Phase 3b optimization and full-campaign report

Date: 2026-07-23. Redispatch pin:
`3d3abb3fdc80c34a690fccab3ae1ff8bdb20a47a` (verified exactly).
Registry SHA-256:
`047bfe6e64146d78e851e2964033b6381ef78f1aa9802f02401276130f4e547b`
(verified unchanged).

Evidence labels are load-bearing. `MEASURED` denotes an exact finite count or
a recorded finite numerical computation. `HEURISTIC` denotes an
interpretation or extrapolation. `OPEN` denotes an unresolved mathematical
claim. This report makes no asymptotic claim.

## A. Executive verdict

Phase 3b and the full frozen Phase 4 campaign completed [MEASURED].

The reference bottleneck was repeated Python set construction and exact
large-integer product work for every class-middle-prime triple. The optimized
implementation replaces that inner loop by a C11 residue-overlap kernel. For
each side class and small prime, it constructs the prefix and suffix residue
sets once and uses a lookup indexed by $`d\bmod p`$ for every prospective and
realized middle. The same table supplies $`A_P`$, prospective rho, realized
rho, off-domain flags, and CRT profiles.

At the frozen smoke row, the compiled prospective-plus-realized kernel took
1.537 seconds on 24 workers. The two corresponding reference phases took
162.344 and 127.954 seconds, for a combined 290.297 seconds. The measured
kernel speedup is therefore about 189 times. The complete bounded-memory
largest scale, including prime/gap/delta loading, class construction, all five
fixed-$`s`$ reductions, rho, CRT, certificates, and compact checkpoints, took
3,762.2 seconds (62.7 minutes) and peaked at 3,491,920 KiB RSS.

The full seven-scale, five-$`s`$ ladder contains 35 completed rows. The
recorded scale-result wall times sum to 5,865.5 seconds; the smallest row was
resumed from its summaries, so the end-to-end production work was about 98
minutes rather than exactly that sum. Cloud compute was not used. Paid-cloud
cost was zero.

The implementation is parallelizable, but local execution was sufficient.
The repository instruction forbidding delegation of repository computation
to Codex Cloud was respected.

The full finite result remains singleton-inert [MEASURED]. At every one of the
35 rows,

$$
N=F,\qquad Q=0,\qquad N-F-Q=0.
$$

Thus every declared certificate rule passes its classwise finite test, but no
rule has positive majority-escape or Gini margin. This is complete finite
evidence on the frozen ladder, not evidence for an asymptotic M5-lite
statement.

## B. Mathematical equivalence

The frozen smoke row $`(x,s)=(10^6,0)`$ was checked against the immutable raw
reference arrays.

- The D0 parameters, class partition, $`N_P`$, realized cells, $`A_P`$,
  residual-domain sizes, prospective off-domain counts, realized off-domain
  flags, finite-anchor correction, and every CRT profile agree exactly.
- All 78,261 prospective reference rho values and all 78,261 realized
  reference rho values lie inside the compiled kernel's certified
  long-double enclosures.
- 76,598 prospective binary64 values are bit-identical to the reference; the
  maximum difference is two ulps and
  $`7.11\times10^{-15}`$ in absolute value.
- 76,439 realized binary64 values are bit-identical; the maximum difference is
  one ulp and $`9.09\times10^{-13}`$ in absolute value.
- Every R2 selector membership agrees for caps
  $`1/8,1/4,1/2,3/4,1`$ times $`\log{}x`$, with zero interval-boundary
  ambiguities.
- The compact streaming reducer independently reproduces the smoke global,
  class-size, $`A_P`$, rho-energy, all 23 rule, and all 200 CRT rows.

The independent cross-check routes were:

1. the old Python `set`/`Fraction` oracle versus the compiled overlap kernel
   on the complete smoke row;
2. a direct set-based residue implementation versus the overlap lookup on
   deterministic synthetic cases (seed 251003);
3. the monolithic smoke reducer versus the bucket-summary reducer.

The targeted suite covers side-block and full-tuple inadmissibility, empty and
small residual domains, multiple admissible middles, changes with
$`d\bmod p`$, large local products, and the six finite-anchor exceptions.

## C. Optimization details

For a fixed side class and odd prime $`p`$, let $`A`$ and $`B`$ be the distinct
prefix and suffix residue sets. The implementation precomputes

$$
\mathrm{overlap}_p(r)
=
\lvert A\cap(a_J+r+B)\rvert,
$$

then evaluates

$$
\nu_H(d)
=
\nu_{\mathrm{pre}}+\nu_{\mathrm{suf}}
-\mathrm{overlap}_p(d\bmod p).
$$

This removes repeated tuple construction and residue-set allocation from the
middle loop. The factors above the residual span are invariant and are
computed once per parameter row. Prospective and realized calculations share
the side residue tables.

All admissibility and CRT data remain integer-exact. Rho is accumulated with a
64-bit-mantissa `long double`. A conservative rounding enclosure includes a
200,000-operation allowance, exceeding the operations used for every prime
through the frozen cutoff $`Q=10^6`$. Selector membership is accepted only
when the enclosure lies on one side of its threshold; an overlap would stop
the run. No overlap occurred in any production row.

The class pipeline uses the existing deterministic side-word hash. Equal
sides always enter the same one of 64 buckets. Each bucket is sorted and
reduced independently, so the scale-wide side matrix is never materialized.
The bucket arrays live in memory only until their compact exact summary is
atomically written. The fixed-$`s`$ views reuse the $`s=0`$ prospective and
realized rho values; removing the at most 1,000 early sites updates their
class/cell counts exactly.

The singleton fast path is conditional. Every bucket first verifies
$`N_P=N_{P,d}=1`$ for all its records. If that check fails, the general exact
collision reducer is used. All production buckets satisfied the singleton
check.

## D. Parallelization and scaling

The independent axes and deterministic merges are recorded in
`m5-lite-phase3b/parallelization.json`.

- Scale shards use the frozen integer $`x`$ as key and merge in ladder order.
- Class shards use the fixed side-word hash bucket and merge in bucket-index
  order.
- Compiled kernel shards use bucket-local contiguous class intervals and
  write disjoint result slices.
- Fixed-$`s`$ rows are exact reductions of one shared $`s=0`$ class/rho
  object.

Integer and rational reducers are associative and commutative. Floating rho
energy is merged deterministically in bucket order and retains its certified
source enclosures. Each compact bucket summary is written atomically. A retry
recomputes only a missing or invalid summary; duplicate and missing bucket
keys are detected before scale merge.

On an 8,192-class smoke sample, 24 workers achieved 17.97 times the
one-worker rate and 5.48 million prospective candidates per second. At
$`x=3\times10^6`$, the corresponding speedup was 18.52 times and the rate was
5.61 million candidates per second. The smoke sample processed about 42,945
classes and realized cells per second on 24 workers. The complete largest
scale processed about 13,510 classes per second including all non-kernel
phases.

The measured bottleneck after kernel scaling is deterministic bucket class
construction and exact summary reduction, not rho residue evaluation.

No cloud resource was used, so compute-hours and monetary cost for cloud are
both zero. Local wall time and peak RSS are recorded for each scale in the
production manifest.

## E. Reproduction

Primary sources:

- `dossier/item-0010-workpapers/m5_lite_phase3b.py`;
- `dossier/item-0010-workpapers/m5_lite_phase3b_kernel.c`.

The recorded environment is Python 3.13.5, NumPy 2.2.4, and GCC 14.2.0.
The compiled shared object requires a `long double` mantissa of at least 64
bits; the production machine reports exactly 64.

Core commands:

```text
python3 -B dossier/item-0010-workpapers/m5_lite_phase3b.py self-test
python3 -B dossier/item-0010-workpapers/m5_lite_phase3b.py equivalence 24
python3 -B dossier/item-0010-workpapers/m5_lite_phase3b.py benchmark 1000000 8192
python3 -B dossier/item-0010-workpapers/m5_lite_phase3b.py benchmark 3000000 8192
python3 -B dossier/item-0010-workpapers/m5_lite_phase3b.py produce-scale-memory X 24
python3 -B dossier/item-0010-workpapers/m5_lite_phase3b.py finalize-campaign
```

The production manifest records source, driver, executable, scale-result, and
artifact hashes. Compact summary files are keyed by scale and bucket. The
abandoned 9.4 GiB raw-checkpoint experiment was removed after the compact
campaign completed; no `/tmp` checkpoint is authoritative production
evidence.

## F. Full measurement result

The complete global table is in
`m5-lite-phase3b/production/global-per-scale.json`. The $`s=0`$ rows are:

| $`x`$ | $`N`$ | $`F`$ | $`Q`$ | $`(N-F-Q)/N`$ | realized rho energy / $`N`$ |
| ---: | ---: | ---: | ---: | ---: | ---: |
| $`10^6`$ | 78,261 | 78,261 | 0 | 0 | 457.824172 |
| $`3\times10^6`$ | 216,578 | 216,578 | 0 | 0 | 659.137214 |
| $`10^7`$ | 664,306 | 664,306 | 0 | 0 | 659.523503 |
| $`3\times10^7`$ | 1,857,274 | 1,857,274 | 0 | 0 | 665.480557 |
| $`10^8`$ | 5,759,779 | 5,759,779 | 0 | 0 | 671.438082 |
| $`3\times10^8`$ | 16,247,074 | 16,247,074 | 0 | 0 | 675.624907 |
| $`10^9`$ | 50,827,008 | 50,827,008 | 0 | 0 | 679.696214 |

The same singleton identities hold for
$`s\in\lbrace1,10,100,1000\rbrace`$ at every scale.

At the largest row, the exact $`A_P`$ class distribution is:

| $`A_P`$ | Classes/site mass |
| ---: | ---: |
| 0 | 6 |
| 1 | 32,263,625 |
| 2 | 14,709,040 |
| 3--4 | 3,638,540 |
| 5--8 | 213,312 |
| 9--16 | 2,475 |
| 17 or more | 10 |

The residual-domain size ranges from 1 to 417. Six finite-anchor classes are
corrected, and no $`\widetilde A_P`$ is zero. The exact inverse mean is

$$
\frac1N\sum_P\frac{N_P}{\widetilde A_P}
=
\frac{71439963679889}{88963528642560}.
$$

The largest-row realized rho energy per site is 679.696214. Four realized
cells are off-domain, and the full prospective census contains 586
off-domain candidates.

For illustration, the largest-row R2 cap $`(1/8)\log{}x`$ selects 20,525,281
classes, while the cap $`\log{}x`$ selects 49,877,781. Both selections have
zero collision violation mass because every selected class is a singleton.
This is a finite implementation result, not evidence of contraction. The
complete 805 certificate rows and 9,028 CRT rows are retained in the
machine-readable production artifacts.

`MEASURED`:

- full completion of the 35 frozen rows;
- all exact collision, class-size, $`A_P`$, selector, and CRT counts;
- all zero-ambiguity enclosure decisions;
- rho energies and certified tail widths;
- local runtimes, throughput, hashes, and peak RSS.

`HEURISTIC`:

- any extrapolation beyond $`10^9`$;
- any claim that singleton dominance, the $`A_P`$ distribution, rho energy,
  or selector mass persists.

`OPEN`:

- every asymptotic M5-lite profile;
- any positive singleton-inert escape or Gini margin;
- which prime-specific structure can force the required non-rigid collision
  mass.

The historical Phase-3 STOP report is preserved unchanged. This report
supersedes only its implementation-feasibility verdict: the frozen campaign
is now computationally complete, while its mathematical interpretation
remains finite and adverse.
