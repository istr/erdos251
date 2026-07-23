# item-0010 M5-lite measurement report

Date: 2026-07-23. Dispatch pin:
`8d82901785b36ab87dc413dc7f0cc1e992808748` (verified exactly).
Web OFF. Local computation only. No Lean, frozen statement, roadmap,
run-history, or payload file was changed.

Evidence labels are load-bearing. `MEASURED` means an exact finite
count or a recorded finite numerical computation. `HEURISTIC` means an
interpretation or persistence claim not proved by the finite data.
`OPEN` means not resolved. This campaign made no asymptotic claim.

## A. Executive result

The registry was frozen before every new production collision output.
Its SHA-256 is
`047bfe6e64146d78e851e2964033b6381ef78f1aa9802f02401276130f4e547b`.

Phase 1 synthetic tests passed. Phase 2 reproduced the overlapping
item-0019 row `(J,K,D,x)=(4,5,30,2000000)` exactly. Phase 3 completed
the smallest primary coupled row, $`(x,s)=(10^6,0)`$, including the
full prospective residual middle domain, exact local rho factors
through $`Q=10^6`$, certified rho tails, all registry rules, $`A_P`$,
realized rho energy, CRT strata, and exact collision identities.

The finite row is a complete singleton artifact [MEASURED]:

$$
N=F=78261,\qquad Q=0,\qquad
\frac{N-F-Q}{N}=0.
$$

All 23 certificate candidates in R0--R3 pass their classwise test and
have zero violation mass, but none has a positive singleton-inert
escape or Gini margin. Their apparent success is therefore not
evidence for M5-lite. In particular, the all-class rules have
$`\lambda_{\max}=0`$ and positive post hoc or declared profile
quantities only because every class is a singleton.

No rule was tested on a largest ladder row. No rule passed a largest
row, no favorable-mass persistence was measured, and no statement
about collapse or persistence is made.

The mandatory prospective-rho object is the dominant cost. On 24
local workers, the smallest row required 162.34 seconds for
prospective rho and $`A_P`$, plus 127.95 seconds for full realized
rho. Scaling only by the exact prime populations of the frozen ladder
projects 77.98 wall-hours for those two phases, including 52.39 hours
at $`10^9`$, before larger residual domains, cache generation,
class sorting, five $`s`$ views, correlations, and rendering. This is
a conservative lower projection, not a runtime guarantee.

The campaign therefore fired the kickoff's computational-feasibility
STOP in Phase 3. The full primary ladder was not run. No rule, cap,
threshold, coefficient, ladder point, or mathematical object was
changed; prospective rho was not replaced by realized-only rho and no
sampling was used.

Successor recommendation: retain the frozen mathematical registry.
Before re-dispatching production, implement and independently validate
a substantially faster exact prospective-rho kernel and a bucketed
class pipeline. The present finite row does not select a proof target.

## B. Registry provenance

The registry is:

- `dossier/item-0010-workpapers/m5-lite-measurement-registry.yaml`;
- copied byte-for-byte to
  `m5-lite-measurements/frozen-registry.yaml`;
- SHA-256 anchored in `m5-lite-measurements/registry.sha256`.

The registry predates all new production output. It fixes:

- $`A'=3/2`$, $`A''=48`$, and the explicit repository Chebyshev
  choice $`C_0=2/\log{}(3)`$;
- the exact D0 map
  $`D=\lceil13C_0A''\log{}x\rceil`$ and
  $`J=K=\lceil\log_2{}D\rceil`$;
- the seven-point $`x`$ ladder and
  $`s\in\lbrace0,1,10,100,1000\rbrace`$;
- all R1 constant profiles;
- all R2 cap/profile crosses;
- the four R3 weighted profiles;
- all size, $`A_P`$, residual-domain, span, and CRT strata;
- the prospective rho upper-endpoint convention through $`10^6`$,
  including zeros and empty domains.

The registry file was not edited after its hash was recorded.

## C. Global D0 smoke table

The exact coupled parameters at $`x=10^6`$ are:

| $`s`$ | $`D`$ | $`J`$ | $`K`$ | $`L`$ | $`\lfloor W\rfloor`$ |
| ---: | ---: | ---: | ---: | ---: | ---: |
| 0 | 15695 | 14 | 14 | 29 | 600 |

The global collision table is:

| $`x`$ | $`s`$ | $`N`$ | $`F`$ | $`Q`$ | $`Q/N`$ | $`F/N`$ | $`(N-F-Q)/N`$ |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| $`10^6`$ | 0 | 78261 | 78261 | 0 | 0 | 1 | 0 |

The direct collision calculation, rigidity identity, all-class Gini
identity, $`Q\le N-F`$, and majority-escape/Gini inequalities all
passed exactly.

## D. Declared-profile smoke table

Every row below has $`\beta_{\mathrm{viol}}=0`$ and passes only at
this finite singleton row.

| Rule | $`\alpha`$ | $`\eta_{\mathrm{profile}}`$ | $`\lambda_{\max}`$ | $`\eta_{\mathrm{escape}}`$ | $`\eta_{\mathrm{Gini}}`$ |
| --- | ---: | ---: | ---: | ---: | ---: |
| R1 all, $`\kappa=1/8`$ | 1 | $`1/8`$ | 0 | 0 | 0 |
| R1 all, $`\kappa=1/4`$ | 1 | $`1/4`$ | 0 | 0 | 0 |
| R1 all, $`\kappa=1/2`$ | 1 | $`1/2`$ | 0 | 0 | 0 |
| R2 cap $`(\log{}x)/8`$, $`\kappa=1/2`$ | $`6774/26087`$ | $`3387/26087`$ | 0 | 0 | 0 |
| R2 cap $`\log{}x`$, $`\kappa=1/2`$ | $`24819/26087`$ | $`24819/52174`$ | 0 | 0 | 0 |
| R3, $`C=1/2`$ | $`26085/26087`$ | 0.8343905509 | 0 | 0 | 0 |
| R3, $`C=1`$ | $`26085/26087`$ | 0.6898153027 | 0 | 0 | 0 |
| R3, $`C=2`$ | $`26085/26087`$ | 0.4791588237 | 0 | 0 | 0 |
| R3, $`C=4`$ | $`26085/26087`$ | 0.2567196982 | 0 | 0 | 0 |

The full 23-row table, including exact favorable masses,
$`F_{\mathrm{exc}}/N`$, extrema, post hoc envelopes, weighted
quantiles, and every integrity check, is in
`m5-lite-measurements/per-rule-certificates.json`.

The rho cap enlarges favorable mass monotonically on this finite row:

| Cap scale $`c`$ in $`c\log{}x`$ | Favorable site mass | $`\alpha`$ |
| ---: | ---: | ---: |
| $`1/8`$ | 20322 | $`6774/26087`$ |
| $`1/4`$ | 42782 | $`42782/78261`$ |
| $`1/2`$ | 63435 | $`21145/26087`$ |
| $`3/4`$ | 71233 | $`71233/78261`$ |
| 1 | 74457 | $`24819/26087`$ |

This does not show that fractions-of-$`\log{}x`$ caps improve the
contraction frontier: contraction has no singleton-inert content on
this row.

## E. Singleton-inert and post hoc tables

For every registry rule on the smoke row,
$`\eta_{\mathrm{escape}}=\eta_{\mathrm{Gini}}=0`$. For the all-class
rules,

$$
\lambda_{\max}=0,\qquad
\eta_{\mathrm{cert}}=1,\qquad
\eta_{\mathrm{weight}}=1.
$$

The discrepancy is exactly the warned self-pair artifact:

$$
\eta_{\mathrm{weight}}
=
\eta_{\mathrm{escape}}+\frac{F_{\mathcal G}}N
=0+1.
$$

The class-size table has only the $`M=1`$ stratum:

| Stratum | Classes | Site mass | $`W_{2,M}`$ | $`V_{2,M}`$ | $`Q_M/N`$ | Rigid mass | Non-rigid mass |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| $`1\le N_P<2`$ | 78261 | 78261 | 0 | 0 | 0 | 78261 | 0 |

## F. Admissible-middle multiplicity

The residual-domain size ranges from 6 to 241. The exact $`A_P`$
site-mass distribution is:

| $`A_P`$ | Site mass | Site-mass share |
| --- | ---: | ---: |
| 0 | 6 | $`2/26087`$ |
| 1 | 59503 | $`59503/78261`$ |
| 2 | 16851 | $`5617/26087`$ |
| 3--4 | 1871 | $`1871/78261`$ |
| 5--8 | 30 | $`10/26087`$ |
| 9 or more | 0 | 0 |

Six classes, of total site mass six, contain a separated finite-anchor
inadmissibility exception. After the exact correction,
$`\widetilde A_P`$ is nonzero for every realized class and

$$
\frac1N\sum_P\frac{N_P}{\widetilde A_P}
=\frac{1370927}{1565220}.
$$

This is strong adverse finite evidence for the full `B2.pairs`
necessary-condition direction at this early row, but it is not an
asymptotic statement and does not decide the weaker collision gap.

## G. Rho, CRT, and contribution decomposition

The full realized rho upper-endpoint energy is [MEASURED]

$$
\frac1N\sum_{P,d}N_{P,d}\rho_Q(P,d)
=457.8241719931.
$$

The certified omitted-tail log width is $`0.000459`$. Three realized
cells, of site mass three, are off-domain under the finite-anchor
side-block convention and contribute rho zero.

There are 200 exact CRT profile rows across
$`p=3,5,7,11,13`$. Every $`Q`$, majority-escape, and Gini
contribution in every profile is zero because the full row is
singleton. Rho-energy and site-mass decompositions are retained in
`m5-lite-measurements/CRT-strata.json`. No CRT profile was promoted to
a favorable selector.

Collision correlations are degenerate on the smoke row because every
cell contributes zero to $`Q`$. No coefficient or selector was tuned
from that outcome.

## H. Evidence classification

`MEASURED`:

- the registry hash and exact pin;
- all synthetic and item-0019 continuity checks;
- the complete $`(10^6,0)`$ D0 row;
- every exact integer count and rational collision certificate;
- the $`A_P`$ and finite-anchor correction;
- rho upper-endpoint energy and certified tail width;
- CRT strata;
- the recorded 24-worker phase runtimes.

`HEURISTIC`:

- any extrapolation from the singleton row;
- any statement that singleton dominance, the $`A_P=1`$ mass, rho
  energy, or cap mass persists;
- the linear full-ladder runtime projection.

`OPEN`:

- every asymptotic M5-lite profile;
- every largest-row comparison;
- favorable-mass persistence or collapse;
- whether rho caps improve a non-singleton contraction frontier;
- which prime-specific proof carrier should be targeted.

## I. Phase-3 STOP and successor

The frozen ladder contains 75,679,066 primes in total. At the measured
smallest-row per-class/cell throughput, mandatory prospective and
realized rho alone project to 77.98 wall-hours on 24 workers. The
largest row contributes 52.39 projected hours. This excludes costs
which grow with scale.

Continuing unchanged with this implementation would not be a credible
finite campaign within the local execution envelope. Replacing the
prospective selector by realized-only rho, sampling it, truncating the
ladder, or relaxing the certified tail would change the dispatched
object and is forbidden. The run therefore stopped before Phase 4.

The next action is implementation work, not proof work and not a new
post-hoc registry:

1. build a bucketed class pipeline which never materializes the full
   high-scale side matrix;
2. implement the same exact prospective-rho object in a compiled,
   independently cross-checked kernel;
3. reproduce this smoke row byte-for-byte;
4. re-profile before authorizing the full frozen ladder.

The campaign success criterion was not achieved because the full
predeclared frontier was not mapped. Item-0010 remains ratified and
open.

## J. Reproducibility and artifact map

Primary script:
`dossier/item-0010-workpapers/m5_lite_measure.py`.

Commands and versions are recorded in
`m5-lite-measurements/run-manifest.json`. The machine-readable
directory contains:

- frozen registry and hash;
- run manifest and per-artifact hashes;
- global smoke table;
- class-size table;
- raw prospective class arrays;
- raw realized-rho/CRT arrays;
- per-rule certificate table;
- $`A_P`$ table;
- rho-energy table;
- CRT-strata table;
- integrity results;
- Phase-3 feasibility record.

All raw certificate counts are exact. Display floats retain their
source arrays and certified rho-tail width. No sampling or random seed
was used.
