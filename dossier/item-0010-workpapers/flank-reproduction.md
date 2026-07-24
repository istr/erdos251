# Reproduction note for the item-0010 flank-collision frontier audit

Date: 2026-07-24. Author: steering lane, independent of the audit
executor. Scope: reproduction instructions and an independently
recomputed verification row for
`flank-collision-singleton-frontier-audit.md` (ANN-20260724-62).

This note adds no new mathematical claim. It exists because the audit's
`MEASURED-AUDIT` quantities are computed over a regenerable local cache
that is deliberately not committed, and because the audit's own output
JSON files are not committed either. Without a recorded reproduction
path those numbers could not be re-derived from repository bytes alone.

## A. Why the compact production artifacts are not sufficient

`m5-lite-phase3b/production/` retains compact exact summaries only. It
does not retain exact side words, so no equality-refinement curve,
off-diagonal mesh cell, or oriented-path count can be recovered from it.
The audit therefore recomputed those quantities directly from the
prime/gap/delta cache. The three drivers landed at commit
`89418e95` expose that computation.

## B. Cache regeneration

The cache is regenerable and deterministic. It is rebuilt by the
item-0019 helper that `m5_lite_measure.py` already imports:

```text
ITEM0019_CACHE=/tmp/item0010-m5-lite-cache \
python3 -c "import sys; sys.path.insert(0,'dossier/item-0019-workpapers'); \
import common; common.build(1000000)"
```

This writes `p_<x>.npy`, `g_<x>.npy`, and `delta_<x>.npy` below
`$ITEM0019_CACHE`. At `x = 10^6` the rebuild takes well under one
second. The drivers default to `/tmp/item0010-m5-lite-cache`.

## C. Driver invocation

Run from `dossier/item-0010-workpapers/`:

```text
python3 flank_frontier.py <x> [--s S] [--output PATH]
python3 flank_panel.py    <x> [--output-dir DIR]
python3 flank_mesh.py     <x> [--output-dir DIR]
```

`flank_panel.py` writes `flank-panel-<x>.json` and `flank_mesh.py`
writes `flank-mesh-<x>.json`. Note that `flank_frontier.py` takes
`--output` (a file), not `--output-dir`.

Per the ANN-20260724-62 post-landing exposure clause, the committed
`flank_frontier.py` and `flank_panel.py` bytes differ from their
original run bytes only in the `REPO` path line; `flank_mesh.py` is
byte-identical to its run copy.

## D. Canonical mesh cell accounting

The audit reports 70 canonical cells at `J = K = 14` and 87 at
`J = K = 15`. Those totals are the union of two driver outputs, not of
one file:

$$
\mathcal G_{J,K}
=
(E_J\times E_K)
\cup
\lbrace(d,d):1\le d\le\min(J,K)\rbrace .
$$

At `J = K = 14`, `E_J = {1,2,4,6,8,10,12,14}` has eight members, so
`flank_mesh.py` emits the 64 product cells. The six remaining canonical
cells are the odd diagonal depths `(3,3), (5,5), (7,7), (9,9),
(11,11), (13,13)`; these come from the diagonal paths of
`flank_panel.py`. 64 + 6 = 70. At `J = K = 15` the product block has
81 cells and the odd diagonal contributes 6 more, giving 87.

A reproduction that reads only `flank-mesh-<x>.json` will therefore see
64 (resp. 81) cells and must join the panel diagonal to obtain the
canonical set.

## E. Independent verification row

Steering rebuilt the cache from scratch and ran both drivers at
`x = 10^6` on the committed script bytes. All values below were
recomputed, not copied, and agree with the audit exactly
[MEASURED-AUDIT, independent recomputation].

Population and depth parameters:

| Quantity | Value |
| --- | ---: |
| `D` | 15,695 |
| `J = K` | 14 |
| `L` | 29 |
| `N` at `s = 0,1,10,100,1000` | 78,261; 78,260; 78,251; 78,161; 77,261 |

Audit Section D.3 row for `x = 10^6`:

| Quantity | Audit | Recomputed |
| --- | ---: | ---: |
| $`C_{\mathrm{joint}}(6,6)`$, all five $`s`$ | 0 | 0 |
| $`C_{\mathrm{joint}}(7,7)`$, all five $`s`$ | 0 | 0 |
| Last positive depth/count, every one-sided path, all five $`s`$ | 13: 1 | 13: 1 |

All four one-sided paths (`pre_first`, `pre_last`, `suf_first`,
`suf_last`) reach their last positive count at depth 13 with count 1 and
are zero at depth 14, so complete prefixes and complete suffixes are
individually unique on this row.

Audit Section D.4 row for `x = 10^6`:

| Quantity | Audit | Recomputed |
| --- | ---: | ---: |
| Unordered transpose pairs with a zero/nonzero mismatch | 3 | 3 |
| Largest $`j+k`$ with a positive mesh count | 13 | 13 |
| Maximum transpose ratio when both counts are at least 100 | 1.01743 | 1.01743 |

The maximizing cell is $`(j,k) = (2,4)`$ with counts 4,378 and 4,303.

## F. Remaining reproduction gap

`OPEN`: the audit's rows for `x = 3\times10^6` through `x = 10^9` have
not been independently recomputed here, and no driver output JSON is
committed at any scale. Any future dispatch that cites Section D or E
numbers beyond the `x = 10^6` row above should either commit the driver
outputs with hashes booked in `payloads/HASHES.txt`, or repeat this
verification at the cited scale.
