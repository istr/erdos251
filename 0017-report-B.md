# item-0017 Session B completion report

Date: 2026-07-18. Executor: steering lineage (Claude Fable 5,
claude-fable-5), continuing the Session A run (compression at
steering discretion; gate order honored). Dossier:
dossier/e2prime-supply.md on branch item-0017.

## 1. Gates

- Section 6 predicates: unchanged from Session A (pin 66adc54
  ratified; hashes verified; prohibitions observed).
- D2 GATE: M1 + M2 COMPLETE and independently checked. DECISION:
  PASS WITH AMENDMENTS (dossier Section 3.4) -- the model balance
  closes a.s. along dyadic scales, so D1 is not architecturally
  dead; binding amendments F17.2 (room is (2 ln x)^M per middle
  position, NOT the kickoff's "(log x)^{2-o(1)}") and F17.3 (D1
  must run on the new aggregate filter D0.2'; the pinned
  per-position filter kills the floor route even in the model).
- Gate order: D2 completed before any D1 execution; D5.c empirical
  landing preceded D1-route trust (kickoff rule honored).

## 2. Observations

### D2 (COMPLETE)

- Theorem M1: model supply a.s. along dyadic scales -- x^{2-o(1)}
  ordered (E2')-pairs, x^{1-o(1)} disjoint pairs (explicit floor
  N_S (ln x)^{-2+o(1)}); full proof with covariance table and
  greedy-matching floor (U17.6 discharged).
- M2: expectation balance closes with relative room (2 ln x)^M;
  concentration; route audit produced the capacity-slack finding.
- Independent re-derivation pass: M1 checker CONFIRMED all
  constants (one proof refinement absorbed: residue-class dilution
  in the degree Chernoff); M2 checker PARTIAL on decimal places
  only (2.08104, theta(2) = 0.1146, theta(1.5) = 0.9447 -- all
  absorbed); no conclusion affected.

### New findings (F17.2-F17.8; dossier Sections 3-6)

- F17.2 room correction; F17.3 capacity-slack obstruction + the
  aggregate-filter repair D0.2' with threshold A' < 4 sqrt(2)/e =
  2.08104 and room exponent theta(A') = 1 - (2/ln 2) ln(e A'/4);
  P3.3' restores the kickoff's L = 2 log2 log x + O_b(1) form.
- F17.4 post-fix D1.a budget: room 2^{theta L/2} vs C_sel ~ 2^L L!.
- F17.5 (the session's sharpest new datum): collision-constant
  closure of the unweighted floor route. General threshold
  A'_crit = 2 sqrt(2)/(e gamma_2); the primes' gamma_2 exceeds the
  critical 1.0405 in every measurement (marginal 1.20/1.18 at
  2e6/2e7; vector-level 1.68/1.58/1.55 at 2e6/2e7/1e8) and at the
  heuristic asymptote E_even[S_2^2]/4 = 1.150481 (Euler product
  4.601923, CONFIRMED by direct summation 4.601842 at D = 2e6).
  The route is closed for the primes at every admissible A' > 1,
  independently of the sieve constant, invisibly to the model
  (gamma_2 = 1/2) -- HL clumping both supplies exchange
  configurations and defeats the max-entropy capacity floor. The
  margin is strikingly thin: 1.1505 vs 1.0405 (ratio 1.106).
- D1.b COMPLETE: Kuperberg Thm 1.1 regime gap is a full square
  (k linear in log h vs required k << (log h)^{1/2}); Thm 1.2's
  growth-free box average (3 log k)^k exceeds every polylog room;
  Pintz Lemma 4 upper direction fails at our depths while the
  lower direction holds (direction split recorded). The missing
  estimate "S second moment at growing k" confirmed absent from
  MoSo (fixed k) and Kuperberg (k << (log h)^{1/2}).
- D3 table drafted (pulled forward): per-mechanism reach rows
  T1-T6 + Maier matrix; blockers confirmed exhaustive for the
  corpus; the sparse-site Markov cost (F17.8) identified as the
  uniform mechanism behind every tail-typicality failure. F17.6:
  T5 transport dies at exactness + tail typicality, NOT at the
  (E5) b-D coupling the kickoff expected. F17.7: Pintz-Thm-5
  transplant reduces (E2)-supply to ONE missing input (HL-type
  class-count lower bound for a single matched-flank family) --
  the sharpest positive lead.
- D4 addenda drafted: Shiu circularity at the weighted clause
  killed by the M-invariant depth floor J+K >= (2+o(1)) log2 ln x
  (exact inequality recorded); pigeonhole blindness strictly
  finer at M >= 2 (E = 0 degeneracy); prescription burden
  M-invariant; Maier matrix joins the register (variability-blind
  + x^{1/D}-sparse columns).

### D5

- D5.c grid complete at 2e6/2e7/1e8 (dossier Section 7.1):
  reproduces the committed class counts (12/178/1287, 2/21/143,
  first (6,6,64) at 1e8); vector gamma_2 trend 1.68/1.58/1.55;
  S-site moments stable [1.32, 1.51]; scripts committed
  (balance_stats.py, d1c_gamma2.py).
- D5.b launched at 1e9 in-core (container probe: 88 GB free;
  ~6 GB peak): deeper firsts (7,7)/(8,8), b in {3,5} certificates
  honoring (E5), (6,6) continuity. Results land next commit.

### In flight

- D1.a: the self-proved k-uniform Selberg constant (workpaper
  d1a-selberg.md) by a max-effort agent; lands with the D1.a
  balance run in the next commit.

## 3. Follow-up candidates (none executed)

- Session C: finalize D1.a (verify the agent's derivation
  steering-side), D1.c (name the S-second-moment estimate
  precisely, assess MoSo machinery), D1.d (Chen-substitution
  reach statement); harvest D5.b; at least one new inline
  certificate into the dossier (acceptance clause).
- Session D: verdict Section 1, obstruction statement assembly
  (the acceptance-intent "named obstruction per blocker with exact
  quantitative gap" is now substantially pre-written by
  F17.3/F17.5/F17.7/F17.8 + D4), review payload build (strip
  script), R1/R2 blind reviews, adjudication, closure.
- For the operator (bookkeeping): U17.5 (pc_wordcount.py absent
  from tree); U17.7 (first project use of PNT, in P3.1' only).
