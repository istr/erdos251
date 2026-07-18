# item-0017 Session C completion report

Date: 2026-07-18. Executor: steering lineage (Claude Fable 5,
claude-fable-5), same run as Sessions A-B (compression at steering
discretion). Dossier: dossier/e2prime-supply.md, branch item-0017.

## 1. Gates

- Section 6 predicates: unchanged (pin 66adc54 ratified; hashes
  verified; prohibitions observed; kickoff sha256 re-verified
  against ledger ANN-50's canonical value -- match).
- D2 gate: PASS (recorded Session B); order honored throughout.

## 2. Observations

### D1.a (COMPLETE; the heaviest deliverable of the item)

Workpaper item-0017-workpapers/d1a-selberg.md (618 lines,
self-contained): k-uniform Selberg upper bound
  N(X;H) <= C(k)(1+err) S(H) X/(ln X)^k,
  C(k) = 2((8k+2) e^{-gamma})^k,  err <= 20 k^2 lnln X/ln X,
valid for k <= (lnln X)^2, span <= (ln X)^2, X >= exp(exp(30));
optimized C*(k) <= (6.11)^k k! e^{1.45 sqrt k} for k >= 5. External
inputs: four Rosser-Schoenfeld inequalities only (numbering
memory-cited: U17.10); no Halberstam-Richert, no PNT. Honesty
layer: the self-contained constant exceeds the classical 2^k k! by
~(3.06)^k (inherent to the Rankin-truncation route; workpaper
Section 13 traces every factor). STEERING-VERIFIED by re-execution
of the core steps (Rankin tail, Delta >= 0.7543, Mertens assembly,
constant-gap ratios).
BALANCE RUN: in-regime (k = L+1, span fine), the max-S balance
fails by exp((1+o(1)) L ln L) already at S-term = 1 -- the
kickoff's predicted "2^L L!"-type failure, self-proved, and
robust (the classical constant fails identically). DOUBLE KILL
with F17.5 (which binds even at C_per = 1).

### D1.c / D1.d (COMPLETE)

- D1.c: "S second moment at growing k" named precisely (dossier
  4.4); its k = 2 ground truth IS the F17.5 constant 1.1505 -- the
  S-weighted repair funnels into HL lower bounds at matched flanks
  (blocker 2) with no constant to spare. MoSo confirmed fixed-k
  (centered moments, box domain); Kuperberg k << (log h)^{1/2};
  the tool gap is genuine AND its two-point value is exactly the
  closing constant.
- D1.d: Chen substitution mapped (dossier 4.5): a 0.25% pairwise
  gain, category-mismatched to both critical spots (true-mass
  closure not a sieve constant; per-word deficit super-exponential).
  Best current pairwise value 3.99 recorded. A located non-lever.

### D5.b (COMPLETE; x = 1e9 in-core, pi(1e9) = 50,847,534)

- FIRST b > 1 CERTIFICATES of the project: inline (7,6,44,3), gate
  126 < 256, d_1 = -24, residual -1.78e-15, HAND-VERIFIED gap by
  gap; (7,6,27,5) on the same sites (gate 125 < 256); 3 classes
  each. One constellation kills b in {1,3,5} (its 1-shift is a
  (6,6,64) b = 1 pair).
- Frontier: (7,7)/(8,8) have ZERO side collisions at 1e9 --
  consistent with the collision calculus (expected ~0.5); first
  (7,7) pairs predicted near 5e9-1e10 (executor-slot candidate).
- (6,6,64): 1 -> 29 classes from 1e8 to 1e9; widest pair spans
  anchors 267,737 vs 979,591,577.
- Acceptance clause's certificate sentence: DISCHARGED.

### Verdict

Section 1 v1 complete, all pending slots closed: obstruction
branch delivered with named obstruction per blocker and exact
quantitative gaps (V2/V3), architecture model-consistent (V1),
single sharpest residual isolated (V4: one HL-type class-count
lower bound at matched flanks; exclusion side available via D1-L),
interface order (V5), certificates (V6).

## 3. Follow-up candidates (none executed)

- Session D (next): payload build via strip_payload.py (drop-table
  refinement), R1 same-family fresh-role blind review (web OFF,
  payload + object only); then STOP-AND-REPORT to the operator:
  R2 cross-family review is operator-side by B2 architecture, and
  closure (emit-patch, ledger ANN, BET-07 note) waits on operator
  ratification of the verdict.
- Successor item candidate (from V4/F17.7): "matched-flank
  class-count lower bound" as its own research item (the
  adjudication-F2 anti-rigidity statement, now with the exclusion
  side pre-built and the exact budget known).
- Executor-slot candidate: (7,7) first-pair hunt at 5e9-1e10
  (segmented sieve).
