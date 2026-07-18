# REVIEW R1 -- ADVERSARIAL COMPUTATION AUDIT (blind, fresh instance)

[Transcription note (steering): received from the blind reviewer
2026-07-18; em-dashes transliterated to ASCII "--" and HTML entity
escapes reversed; content otherwise verbatim.]

Object: item-0017 review object v1 (anchor-stripped dossier, 1459
lines). Payload: R1 computation-audit payload v1. Files read: exactly
these two. Web: not used. All numerics below were re-derived or
re-executed with my own Python scripts (own sieves, own prime
generation, own Miller-Rabin, own SPF factorization); scripts run
under /tmp scratch, nothing written into the repository.

## 1. FINDINGS BY SEVERITY

### FATAL

None.

### MAJOR

**M-1. Lemma P3.2 (Section 2.5) is false at its stated threshold
N >= L+16.**
Location: Section 2.5, P3.2 proof, final line: "Total < 12 C_0
(N'+2) ln(N'+4) <= 13 C_0 N ln N for N >= L+16."
My computation (N' = N+L): the claimed inequality
12(N+L+2)ln(N+L+4) <= 13 N ln N fails on a large part of the stated
domain:

```
  N=32,   L=16   (N=L+16): LHS=2371    RHS=1442    FALSE
  N=116,  L=100  (N=L+16): LHS=14110   RHS=7168    FALSE
  N=1000, L=100  (N=10L):  LHS=92657   RHS=89801   FALSE
  N=1016, L=1000 (N=L+16): LHS=184304  RHS=91447   FALSE
  N=2000, L=100  (N=20L):  LHS=193004  RHS=197623  true
```

The chain only closes for N larger than roughly 20L. Since the lemma
is derived from the Chebyshev-type hypothesis p_n <= C_0 n ln(n+2)
alone ("explicit functions of C_0 alone"), and near-extremal gap
configurations consistent with that hypothesis approach the
12 C_0 (N'+2) ln(N'+4) bound, the lemma as stated (not merely its
proof) is unsound at the printed threshold. Repair is one line and I
verified it: N >= 40(L+2) makes the step hold (checked exhaustively
for L = 1..1999), or keep N >= max(L+16, 32) and raise the constant
13 to 29 (12 * 2N * 1.2 ln N = 28.8 C_0 N ln N). Downstream damage:
none -- every consumer (P3.3(iii), P3.3'(ii)) applies P3.2 at
N = pi(x) with L = O(loglog x), astronomically inside the repaired
domain, and P3.4 lets x_1(b) absorb the threshold. The object's own
bracket "[Constants deliberately loose; only explicitness is
load-bearing]" is exactly the layer that is wrong here, which is why
I grade this MAJOR rather than MINOR.

### MINOR

**m-1. Theorem M1(ii) (Section 3.2): stated disjoint floor is 2x
what the proof delivers.**
Location: "the explicit disjoint floor is N_S/(8 (2-p)^{J+K})".
My re-derivation of proof step (e): T >= E[T]/2 = N_S^2
q_2^{J+K}/2; 4*max_deg = 8 N_S p^{J+K}; matching >= (N_S^2
q_2^{J+K}/2)/(8 N_S p^{J+K}) = (N_S/16)(2-p)^{-(J+K)}. The proof's
own display says "/16" and Section 3.5's checker confirms "matching
floor at the /16 level", but the theorem statement says /8.
Statement/proof mismatch by a factor 2; asymptotic conclusion
(x^{1-o(1)}) unaffected.

**m-2. F17.5(b) (Section 4.3): deficit exponent "0.35" is wrong for
the stated gamma_2.**
Location: "deficit factor ... = (ln x)^{(2/ln 2) ln(e A' gamma_2/2)
- 1 + o(1)}, e.g. (ln x)^{0.35+o(1)} at A' -> 1+, gamma_2 =
1.1505."
My computation: (2/ln 2) ln(e * 1.150481 / 2) - 1 = 2.885390 *
ln(1.563697) - 1 = 2.885390 * 0.447054 - 1 = **0.28986**, i.e.
(ln x)^{0.290+o(1)}. The printed 0.35 corresponds to the empirical
2e7 value gamma_2 = 1.1808 (which gives 0.36492) -- a
value-substitution slip. The closure direction (exponent strictly
positive) is unaffected.

**m-3. P3.3'(ii) (Section 2.7): "a positive proportion of pi(x) for
A' > 1 strict" is false for A' <= 8/7.**
My computation of the displayed bound N(1 - (1+o(1))/A' - 2/A'')
with A'' = 16: A'=1.01 -> -0.115; A'=1.1 -> -0.034; A'=8/7 ->
0.000; A'=1.2 -> +0.042. The bound is vacuous on (1, 8/7]. This
also touches the "at the minimal admissible A' -> 1+" locution in
Section 4.0 and F17.5: with A''=16 fixed, A' near 1 is not
certified site-abundant; the clean repair is A'' -> larger (cost
only +log2 A'' in J, K). No verdict clause changes: the primes-side
closure (F17.5) holds for every A' > 1 regardless of abundance, and
the model window (8/7, 2.081) remains nonempty.

**m-4. M2.2 (Section 3.3): the adjacent-word-run probability
"q_2^{L} per adjacent pair" understates the true probability by
(ln x)^{2+o(1)}/L.**
The event word(i)=word(i+1) forces h_{i+1}=...=h_{i+L+1}; true
probability = sum_t P(h=t)^{L+1} = p^{L+1}/(1-(1-p)^{L+1}) ~
p^L/(L+1) = q_2^L * (2-p)^L/(L+1). Numerical check (p=0.01, L=5):
true 1.71e-11 vs claimed q_2^5 = 3.2e-12, ratio 5.34 = (2-p)^5/6 as
predicted. The conclusion survives: overlapping block / main =
(2-p)^L/((L+1) N_S) = x^{-1+o(1)}, still o(main). Wrong
intermediate constant, right conclusion.

### NOTE

**n-1.** M1(d): "(ln x)^{0.831+o(1)}" -- exact exponent is
2 log2(4/3) = 0.830075 (Section 3.5 itself prints 0.83007; M1(d)
carries a stale 0.831).
**n-2.** M2.3(ii): "theta(1.9) = 0.2628" -- my value 1 - (2/ln 2)
ln(1.9e/4) = 0.262611, which rounds to 0.2626, not 0.2628.
(theta(2) = 0.114610 -> "0.1146" correct; theta(1.5) = 0.944685 ->
"0.9447" correct; theta(4/e) = 1 exact, confirmed.)
**n-3.** Section 4.1 honesty layer: "~ (3.06)^k" -- exact
2e^{1-gamma} = 3.05241 (payload's quoted 3.057 also inexact). The
Corollary bound "C*(k) <= (6.11)^k k! e^{1.45 sqrt k}" is a valid
inequality: 4e^{1-gamma} = 6.10482 < 6.11, and I checked via
Stirling that the poly factors are absorbed for k >= 5.
**n-4.** D5.c site counts: my independent pipeline reproduces every
collision-layer number exactly (see Section 3 below) but yields
site counts ~0.13% higher (143992 vs 143787 at (4,5,30), x=2e6;
same-size offset in all rows), while the internal differences match
exactly (|S|-|W| = 26 and |W|-|P| = 12 at 2e6; 211/178 at 2e7;
1326/1287 at 1e8, identical to the object's implied values). This
is a site-admission index-convention offset at the filter boundary,
with zero effect on any committed record.
**n-5.** D1-L's Delta >= 0.7543 display and the Rankin/R-S assembly
live in the workpaper (d1a-selberg.md), which is outside the two
files I am permitted to read; they are not independently checkable
in this review. All in-object consequences of D1-L that are
checkable (constant shapes, regime conditions, err term) verify.
This aligns with the object's own U17.10 flag.
**n-6.** The in-regime error k^2 lnln X/ln X at k = (2/ln 2) lnln x
is o(1) only asymptotically: 11.2 at x=1e8, 3.4 at 1e300, 2.1e-8 at
X = exp(exp(30)). The workpaper's floor X >= exp(exp(30)) makes err
genuinely small on the stated domain; no discrepancy, recorded for
scope-awareness.

## 2. MANDATED COMPUTATIONS -- MY VALUES VS THE OBJECT'S

### C1 (model constants, Section 3)

- q_2: brute sums sum_t (p(1-p)^{t-1})^2 at p = 0.1/0.01/0.001
  equal p/(2-p) to 10 digits (e.g. p=0.01: 0.005025125628 both).
  CONFIRMED.
- q_3: brute sums equal p^2/(3-3p+p^2) to 10 digits. CONFIRMED.
- q_3/q_2^2 = (2-p)^2/(3-3p+p^2) -> 4/3 with measured correction
  coefficient (r - 4/3)/p^2 -> -1/9 (O(p^2), matching the 3.5
  checker). CONFIRMED.
- (2 ln x)^{J+K} at J+K = 2 log2 ln x: exponent (J+K) ln(2 ln x) vs
  (2/ln 2)(lnln x)^2: 70.4/61.2 (ln x = 100), 578.4/550.7
  (ln x = 1e6); ratio exponent/ln x = 0.70, 0.026, 5.8e-4 -> 0:
  x^{o(1)}. CONFIRMED.
- Variance blocks: shared-site / E[T]^2 = 4 q_3^{J+K}/(N
  q_2^{2(J+K)}) = 4(4/3)^{J+K}(1+o(1))/N_S = x^{-1+o(1)} with
  (4/3)^{J+K} = (ln x)^{0.830075+o(1)}; overlap block / E[T]^2 =
  4(L+2)/(N_S q_2^{J+K}) = x^{-1+o(1)}. Algebra re-derived,
  CONFIRMED (see n-1 for the 0.831 rounding).
- Matching floor: re-derived -- proof gives /16, statement /8
  (finding m-1).
- Dyadic Borel-Cantelli: P(T < E[T]/2) <= 4 Var/E[T]^2 =
  x_r^{-1+o(1)}; sum_r 2^{-r(1-o(1))} < infinity. CONFIRMED.

### C2 (threshold algebra, Sections 3.3/4.0)

- Display identities verified to machine precision at test values:
  (2/(A ln x))^{J+K}(2 ln x)^{J+K+1} = (2 ln x)(4/A)^{J+K} (ratio
  1.000000000000); aggregate variant likewise.
- 4 sqrt(2)/e = 2.0810404 (object 2.08104 CONFIRMED). theta(A') =
  1 - (2/ln 2) ln(e A'/4): theta(2) = 0.1146, theta(1.5) = 0.9447,
  theta(4/e) = 1 exactly -- CONFIRMED; theta(1.9) = 0.2626 vs
  printed 0.2628 (n-2).
- Generalized form: floor/C_words,off = (ln x/gamma_2)(2/(e A'
  gamma_2))^{J+K} diverges iff A' < 2 sqrt(2)/(e gamma_2); at
  gamma_2 = 1/2 this is 4 sqrt(2)/e (consistent); at A' -> 1+ the
  openness criterion is gamma_2 < 2 sqrt(2)/e = 1.0405202. Algebra
  re-derived, CONFIRMED (with the m-3 site-abundance caveat at
  A' -> 1+).

### C3 (collision constant, Section 4.3)

Own prime sieve to 2e7; own SPF sieve to 2e6.
- C_2 = 0.66016182 (tail error < 3e-9).
- Euler product E = 4 C_2^2 prod_{p>2}(1 + ((p-1)^2/(p-2)^2 - 1)/p)
  = **4.6019231**. Object: 4.601923... EXACT MATCH. E/4 =
  1.1504808 (object 1.150481). CONFIRMED.
- Direct summation (2/D) sum_{even d <= D} S_2(d)^2 with S_2(d) =
  2 C_2 prod_{p|d, p>2}(p-1)/(p-2): D=1e5: 4.600773; D=1e6:
  4.601766; **D=2e6: 4.601842** -- matches the object's 4.601842 to
  all printed digits, and converges toward the Euler product.
  CONFIRMED.
- gamma_2^crit = 2 sqrt(2)/e = 1.0405202 (object 1.040520). Margin
  ratio 1.150481/1.040520 = 1.10568 (object 1.106). CONFIRMED.

### C4 (P1/P2/P3, Section 2)

- P1(a)-(d): re-derived algebraically (fiber decomposition of
  pi-matched ordered pairs; Cauchy-Schwarz on fibers). Sound.
  (Trivial typo "w(u')" for "w(n')" is self-annotated in the
  object.)
- P2: chain re-derived: |sum| = |E| 2^{-(J+M)}; far caps +
  two_le_delta give |delta_{t+L} - delta_{u+L}| <= 2^K - 2, and
  2^{-L}(2^K-2) = 2^{-(J+M)}(1 - 2^{1-K}) < 2^{-(J+M)} <=
  |E| 2^{-(J+M)}; evenness of middle gaps (indices >= 2) forces E
  even, |E| >= 2: factor-2 margin. CONFIRMED.
- E-invariant example: middles (2,8) vs (4,4), d = (-2,+4), E =
  2(-2) + 1(+4) = 0: weighted left side exactly 0. CONFIRMED.
- Majorant: sum_{j>=1}(j+1)^2 2^{-j} = 11.000000 (components
  sum j 2^{-j} = 2, sum j^2 2^{-j} = 6, sum 2^{-j} = 1). CONFIRMED.
  Sub-steps (N'+j+2) <= (N'+2)(j+1) (difference j(N'+1) >= 0),
  ln(N'+j+4) <= ln(N'+4)(1+ln(j+1)) (needs ln(N'+4) >= 1, always),
  1+ln(j+1) <= j+1: all verified. P3.1's chain (N+L+1 <= 2N,
  ln 2 <= 0.2 ln N iff N >= 32) verified. P3.2's FINAL step: FALSE
  at threshold -- finding M-1.
- P3.3 self-consistency: (i) b(D-2) < bD <= 2^J = 2^{J+1}/2 from
  J = ceil(log2(bD)); (ii) 2^K >= D; (iii) union-bound arithmetic
  (2.4/8 + 2/(8 C_0 L) <= 1/2); (iv) second-order term
  2 log2 log2 ln x genuinely unbounded (deviation note correct);
  (v) capacity exponent (J+K)(lnln x + ln(A/2)) ~ 2.885(lnln x)^2
  <= 5(lnln x)^2. All CONFIRMED.
- P3.3': stars-and-bars with even parts = C(floor(A'L ln x/2), J+K)
  <= (e m/r)^r verified; depth O_b(1) restoration verified; (ii)
  positive-proportion gloss FALSE on (1, 8/7] -- finding m-3.

### C5 (D1-L spot checks, Section 4.1)

- Constant-gap ratios: C(k)/(2^k k!) = ((4k+1)e^{-gamma})^k * 2/k!
  ~ 2e^{1/4}(4e^{1-gamma})^k/sqrt(2 pi k) with 4e^{1-gamma} =
  6.1048 ("6.11" as an upper bound: valid); C*(k)/(2^k k!) ~
  (2e^{1-gamma})^k/sqrt(2 pi k) with 2e^{1-gamma} = 3.0524 (object
  "~3.06": last digit off, n-3). Stirling check of C*(k) <=
  (6.11)^k k! e^{1.45 sqrt k} passes for k >= 5. CONFIRMED with
  rounding notes.
- In-regime error: k^2 lnln X/ln X at k = (2/ln 2) lnln x: o(1),
  values shown in n-6; regime conditions k <= (lnln X)^2 and
  span <= (ln X)^2 hold at the stated X-floor. CONFIRMED.
- Delta >= 0.7543: not checkable from the two permitted files
  (n-5).

### C6 (inline certificates, Sections 7.1-7.2)

All with my own code (deterministic Miller-Rabin base set {2..37};
segmented sieves; 80-term dyadic tails):
- Primality: all 32 printed numbers prime. Consecutiveness: my
  sieve's first 16 primes from each anchor equal the printed lists
  exactly (no primes omitted).
- Words: site n gaps [4,2,16,2,10,12,18 | 6 | 20,12,4,14,6,4],
  site m gaps [4,2,16,2,10,12,18 | 30 | 20,12,4,14,6,4]; flanks
  match entry by entry; middles 6 vs 30; d_1 = -24. All as printed.
- Deltas: my values delta_{t+J} = 10.426 / 22.477, delta_{t+L} =
  14.562 / 21.089 -- all four match the printed decimals. Caps:
  near <= 44 (b=3) and <= 27 (b=5) hold; far <= 2^6 = 64 hold.
- (E5) gates: 3*(44-2) = 126 < 256; 5*(27-2) = 125 < 256;
  1*(64-2) = 62 < 128. All hold.
- (E2'): LHS = 24/256 = 0.093750 > RHS = 2^{-14}|14.562-21.089| =
  3.98e-4. Holds with large margin (factor-2 margin clause
  satisfied: |E| = 24, even).
- Lemma 2.2 subtraction identity residual: my value -5.7e-16
  (object -1.78e-15); both machine-epsilon, difference is summation
  order. CONFIRMED at machine precision.
- 1-shifted (6,6,64) b=1 form: shifted flanks match, caps <= 64 all
  hold -- the one-constellation-kills-b-in-{1,3,5} claim CONFIRMED.
- Bonus checks: gap-index anchors verified by own sieve counts:
  pi(125063226) = 7113518 and pi(14824986) = 960168 (first printed
  prime = p_{t+1}, consistent with D0.1); the 1e9 first (6,6,64)
  class anchors 267737 / 979591577 verified: prefix
  [2,10,14,18,10,6] and suffix [8,18,4,24,6,14] match entrywise,
  middles 6 vs 36, all caps <= 64.
- Full 1e9 census re-executed (own odd-sieve to 1e9, sliding-window
  lexsort over ~5.08e7 sites): **(6,6,64): 29 classes** (claim 29);
  **(7,6,44) b=3: 3 classes** (claim 3); **(7,6,27) b=5: 3
  classes** (claim 3); **(7,7,67) and (8,8,67): zero side
  collisions** (claim zero). pi(1e9) = 50847534 by own segmented
  count (object: verified same). Expected (7,7) side collisions
  N^2(gamma^vec/ln x)^{14} = 0.44 at gamma = 1.55 (object "~0.5")
  -- consistent with the observed zero. ALL CONFIRMED.
- D5.c grid (beyond mandate, reproduced in full): all committed
  collision-layer numbers reproduce EXACTLY at x = 2e6/2e7/1e8:
  C_w-off/C_s-off/P1/cls = 52/76/24/12, 14/18/4/2, 2/2/0/0,
  0-saturated; 422/778/356/178, 66/108/42/21, 2/2/0/0;
  2654/5232/2578/1287, 352/638/286/143, 4/6/2/1. Class records
  12/178/1287, 2/21/143, first (6,6,64) at 1e8: CONFIRMED.
  Marginal gamma_2: my values 1.2005 (2e6) and 1.1808 (2e7) --
  exact to 4 decimals; my 1e8 value 1.1711 continues the claimed
  decline toward 1.1505. Naive baselines 1.418e-3/2.461e-2/
  1.982e-1 reproduce exactly with q_2 = 1/(2 ln x); vector
  constants 1.676/1.581/1.550 (object 1.68/1.58/1.55). Calibration
  ratio 0.1158/0.0345 = 3.36 (object "~3.4x"). pi(2e6/2e7/1e8) =
  148933/1270607/5761455 all confirmed. Site-count offset: n-4.

### C7 (internal consistency)

Every Section 1 V-clause traces to a body section that proves or
measures what it says: V1 -> 3.2/3.3/3.4 (gate PASS with
amendments, recorded, gate order documented); V2 -> 2.3, 3.3, 4.0,
4.3, 4.4 (all constants consistent, incl. ratio 1.106 and the
1.1505 = k=2 tool constant identification); V3 -> 6.1-6.3,
F17.6/F17.8 (killing inequality re-derived: exp(C * (2+o(1)) log2
ln x) = (ln x)^{(2C/ln 2)(1+o(1))} vs available J = (1+o(1)) log2
ln x -- correct); V4 -> 5.T1/F17.7 (candidate-value count <=
A'L ln x/2 consistent with even values under the window cap);
V5 -> 2.6 (FW-1..4 coherent; FW-4's parity remark consistent with
P2); V6 -> 7.1/7.2 (every number now independently reproduced).
Scope qualifiers present where the body is heuristic/empirical:
F17.5's truth face flagged heuristic+empirical with U17.9; the gap
law and vector constants flagged U17.8/U17.9; model discipline
maintained in Section 3; the acceptance-intent check's three
clauses match the body. The only statement/proof mismatches found
are m-1/M-1/m-3 above. Theorem D0.6's proof re-checked line by line
(Lemma 2.3 -> 2.4 -> 2.5 pin, then two Lemma 2.2 subtractions +
strict triangle inequality): sound.

## 3. VERDICT

**SOUND WITH REPAIRABLE ISSUES. Confidence: 0.89.**

Basis: the entire numeric spine -- collision constants, threshold
algebra, the Euler product and its direct-sum confirmation, both
inline certificates down to machine-precision residuals, and the
complete empirical census at 2e6/2e7/1e8/1e9 including the
29/3/3/0/0 frontier data -- reproduces exactly under independent
re-computation. The five substantive defects found (one
false-as-stated lemma threshold, one statement/proof factor 2, one
wrong illustrative exponent 0.35 -> 0.29, one vacuous
site-abundance gloss for A' <= 8/7, one understated run
probability) are all locally repairable with no verdict clause of
Section 1 changing under repair. Nothing rises to FATAL. Confidence
is capped below 0.95 because the D1-L workpaper internals (Delta >=
0.7543, the R-S citations flagged in U17.10) and the 14 anchored
anatomies are outside the two files this review may read, so the
sieve-constant layer is verified only at its in-object interface.
