# Adversarial Scope Audit — Item 0017 R2

## Review basis

This report executes the scope-audit payload against exactly these two files, with no web use:

- `item-0017-review-r2-payload-v1.md`  
  SHA-256: `f18f0bc02cc9808dbccb05ffbf014b2430d250bdce3be1c98da4a68805fdbdf6`
- `item-0017-review-object-v1.md`  
  SHA-256: `5a7a2647d11ec40d00b2d2ae2473bfdfd2a32a22ab731b7fe93dfe97b85fbb63`

Line numbers below refer to `item-0017-review-object-v1.md`.

## Overall verdict

**UNSOUND** — confidence **0.96**.

The dossier contains substantial useful work, including a largely disciplined statement layer, a real route-specific capacity calculation, informative finite computations, and a plausible certificate. The adverse verdict is about **scope and entitlement**, not about every local calculation. Three central conclusions are stronger than the supplied body permits:

1. the claim that the counting route is “exactly closed” converts finite measurements and a heuristic marginal collision constant into a primes-side conclusion, and then extrapolates a fixed-k second moment to growing word length without a tensorization theorem;
2. the claimed “single missing input” in V4 is contradicted by the dossier’s own growing-k sieve constant and by its separate tail-typicality blocker;
3. the model gate is presented as proved and independently checked although the concentration argument omits a load-bearing treatment of random indexing, overlapping/infinite tail dependence, and conditioning on the filters.

The global disclaimer in lines 33–38 does not cure locally unconditional phrases such as “exactly closed,” “only,” “all roads,” “confirmed EXHAUSTIVE,” and “the entire unconditional content.” The payload expressly requires inline scope qualifiers.

---

## S1 — Verdict-to-body support audit

| Verdict clause | Body relied on | Support class assigned | Scope judgment |
|---|---|---|---|
| **V1:** Model-M supply, ordered/disjoint pair counts | §3.2, Theorem M1, lines 528–600; checker note, lines 721–748 | **PROVED** as claimed, plus **CITED** checker assertion; proof incomplete | The asymptotic count is plausible, but the a.s. theorem lacks a valid supplied concentration/dependence argument. “Independently checked” is not auditable because derivations are withheld. |
| **V1:** model balance closes with room \((2\ln x)^M\) | §3.3, lines 609–634 | **PROVED** as claimed, conditional on the same omitted concentration machinery | The expectation algebra is supported; the almost-sure positivity claim inherits the M1 dependency gap. |
| **V1:** “The failure of unconditional supply is primes-specific, not architectural.” | Inference from §3 | **HEURISTIC** architectural inference | The model only shows that the obstruction is absent in Model M. It cannot establish that the actual failure is “primes-specific” as a fact about primes or rule out defects shared by other models/routes. |
| **V2:** P1 fixes the battleground | §2.3, lines 225–250 | **PROVED** | Supported for the stated P1 statistic. |
| **V2:** per-position filter capacity failure | §3.3 M2.3(i), lines 640–652 | **PROVED** within the pinned D0.2/max-capacity floor route | Properly route-relative in the body, but V2’s heading broadens it. |
| **V2:** aggregate-filter threshold calculus | §3.3 M2.3(ii), lines 653–675; §4.0, lines 753–774 | **PROVED** algebraically within D0.2′ and the max-entropy floor, subject to site-abundance qualifications | The claim “A′ > 1” is not sufficient under the displayed A″ = 16 lower bound; see MAJOR-2. |
| **V2:** primes-side closure through \(\gamma_2\to1.150481\) | §4.3, lines 867–906; §7 measurements | **MEASURED + HEURISTIC** | The dossier itself labels the asymptote “heuristic + empirical.” The verdict removes that qualifier and states a primes-side closure. The needed growing-window collision law is not proved by the marginal constant. |
| **V2:** S-weighted repair has the same constant and funnels to blocker 2 | §4.4, lines 920–960 | **HEURISTIC** extrapolation from a fixed two-point computation | The fixed-k value does not prove a growing-k simplex second moment or tensorization. The route is not closed by the supplied argument. |
| **V3:** depth floor for every M | §6.1(a), lines 1123–1128 | **PROVED** only for tail-typical routes with \(D\gtrsim\ln x\) | V3 omits the tail-typical/positive-density qualifier. E4/E5 alone do not force typical \(D\) at arbitrary constructed sites. |
| **V3:** blocker 1 is worse for M ≥ 2 | §6.2, lines 1151–1165 | **PROVED** for bare P1 positivity; model estimate is **HEURISTIC/PROVED-in-model** | The example proves that bare side-collision positivity is insufficient. “Pigeonhole-optimal” is only justified relative to that statistic, not every E-sensitive counting argument. |
| **V3:** blocker 2 is M-invariant | §6.3 and cited tool anatomies | **CITED + route analysis** | The dossier does not prove an impossibility theorem for every prescriptive construction. It maps the cited tool class. |
| **V3:** blocker 3 killing inequality | §6.1(b), lines 1129–1146 | **PROVED** algebra conditional on the cited [AUTH-S]/[AUTH-O] density form | Supported for that string-prescription mechanism and tail-selection method, not all construction routes. |
| **V3:** every corpus TT failure has the same mechanism | §5, especially lines 998–1112 | **CITED + cartographic assertion** | The rows support the listed examples, but no exhaustive mapping/composition theorem is supplied. |
| **V4:** one missing class lower bound; every other step available | §5 T1, lines 998–1016; §4.1 D1-L; finding F17.7 | **CITED**, with a contradicted quantitative inference | The body does not establish the claimed exclusion budget. Its own \(C^*(k)\) makes the extension upper bound too large at \(k\asymp\ln\ln x\). T1 also lists tail typicality separately. |
| **V5:** only normal form feeds the landed interface | §2.6, lines 387–440 | **PROVED** from the quoted interface, whose fidelity is **CITED** | This is the best-scoped verdict clause. It remains conditional on the omitted external module quotation being accurate. |
| **V6:** grid counts and collision constants | §7.1, lines 1218–1255 | **MEASURED** | Supported as script outputs at the listed scales, not as independent reproduction of an unseen committed record. |
| **V6:** Euler product/asymptote | §4.3, lines 869–878 | **HEURISTIC**, with a finite numerical check **MEASURED** | The finite direct sum is close to, not equal to, the infinite product; neither proves the prime-gap asymptote. |
| **V6:** b > 1 certificate and class counts | §7.2, lines 1257–1294 | **MEASURED**, partly hand-checkable, plus **CITED** project-history assertions | The printed primes verify the finite word and middle difference. The tail values, full scan counts, and “first of the project” claim are not hand-verifiable from the two supplied files. |

---

# Findings

## FATAL

### FATAL-1 — The “exactly closed” counting verdict is not established

**Location and verbatim claims**

- §1 V2, line 48: **“V2 (the counting route, exactly closed).”**
- §1 V2, lines 54–62: **“the primes close the route through the exactly-computed two-point HL mass: gamma_2 -> E_even[S_2^2]/4 = 1.150481 > gamma_2^crit = 2 sqrt(2)/e = 1.040520 (F17.5) -- a sieve-constant-independent closure with a strikingly thin margin (ratio 1.106), invisible in the model (gamma_2 = 1/2), measured above threshold at every reachable x. The S-weighted repair's own tool constant at k = 2 IS the same 1.1505 (D1.c): the counting route funnels into HL lower bounds at matched flanks -- blocker 2 -- with no constant to spare.”**
- §4.3, lines 894–900: **“(b) TRUTH face (heuristic + empirical, model-language discipline): the target inequality floor > C_words is FALSE for the primes at every A' > 1 if gamma_2 > 1.0405, as all measurements and the HL asymptote indicate”**.
- §4.3, lines 907–915: **“The three surviving routes, each meeting a named blocker, are pre-shaped for [PHASE-3]: (1) S-weighted floors -- need HL LOWER bounds at matched sides (parity-blocked prescription, O4 blocker 2) plus S-second moments at growing k (D1.c register target); (2) typical-set capacity restriction -- needs upper-sieve control of rare side words at entropy precision (D1.a constant territory, F17.4); (3) middle-width amplification (M > 1) -- room (2 ln x)^M grows only linearly in the exponent while the closure deficit is per-position multiplicative: no fixed M escapes.”**
- §4.4, lines 946–953: **“k = 2 ground truth: THE SECOND MOMENT IS LARGE, NOT 1+o(1). The F17.5 Euler product IS the k = 2 instance: the per-position (even-normalized) second moment E_even[S_2^2]/E_even[S_2]^2 = 4.601923/4 = 1.1505 > 1. Any k-fold product structure compounds this per position; hence the needed (1+o(1))^k quality is FALSE as stated, and the honest form of (ii) must carry the exact constant (1.1505...)^k -- which then re-enters the floor calculus as gamma_2 and reproduces the F17.5 closure.”**

**Support class:** **MEASURED + HEURISTIC**, with some **PROVED** route algebra.

**Why this is fatal**

The route algebra says what would happen **if** an effective consecutive-window collision constant behaved multiplicatively at length \(J+K\). The dossier supplies:

- two marginal measurements, at \(2\cdot10^6\) and \(2\cdot10^7\);
- three vector-level measurements at selected depths/scales;
- a heuristic marginal asymptote from an HL-frame gap law;
- no theorem that the collision probability of a \((J+K)\)-long consecutive gap vector is bounded below by \((1.150481/\ln x)^{J+K}\), or even that its geometric-mean constant remains above the critical value as \(J+K\to\infty\).

A one-coordinate collision constant does not tensorize automatically for dependent consecutive gaps. Finite vector measurements do not provide an asymptotic lower bound. Likewise, a fixed-k singular-series second moment greater than one does not prove that the growing-k simplex second moment carries \((1.1505-o(1))^k\). That is an unstated load-bearing tensorization/lower-bound step.

The claim is also internally inconsistent: §4.3 explicitly lists “typical-set capacity restriction” as a surviving counting-style route, while V2 says the counting route is exactly closed and §4.4 calls the S-weighted floor “the only repair.”

**Required narrower wording**

> Within the unweighted max-entropy floor using D0.2′, the reported prime data lie above the critical collision threshold, and the HL-frame marginal heuristic predicts that this obstruction persists. No unconditional asymptotic closure is proved. The growing-window collision law, the S-weighted route, and typical-set capacity refinements remain open.

**Unstated load-bearing steps**

1. A uniform growing-window collision lower bound or tensorization principle for consecutive prime gaps.
2. A growing-k lower bound for the singular-series second moment on the relevant simplex.
3. An argument excluding non-max-entropy/typical-set counting floors.

---

### FATAL-2 — V4’s “single missing input” is contradicted by the dossier’s own sieve constant and TT analysis

**Location and verbatim claims**

- §1 V4, lines 81–92: **“F17.7: [AUTH-A]'s Thm 5 exclusion pattern, transplanted to one matched-flank word class, derives (E2)-supply from a SINGLE missing input -- an HL-type lower bound for the class count of one matched-flank family at k ~ L = (2+o(1)) log2 ln x. The summed-[SIEVE-1] exclusion side is quantitatively AVAILABLE at our depths: D1-L (Section 4.1) is k-uniform precisely in-regime, so excluding a rigid middle over all <= A' L ln x/2 candidate values costs a factor the exclusion budget absorbs; only the class-count lower bound is missing. Equivalently (P1): the anti-rigidity counting statement of adjudication-F2 form. All roads of this dossier terminate at this one input.”**
- §5 T1, lines 1007–1016: **“Missing EXACTLY: (a) class-count LOWER bounds for word-level flank classes (replacing (6.6)) -- a prescribed-tuple lower bound at k ~ L, the parity-blocked class; (b) (E4) at log-power-sparse sites: [PROB-5] cost log^k x inflates D by log^k x, hence J by ~ k log2 log x -- self-defeat by factor k. TRANSPLANT SHAPE (recorded as the sharpest positive lead of the corpus): T1's exclusion argument applied to a flank class would derive (E2)-supply from HL-type lower bounds for ONE matched-flank family -- the wall is exactly the lower bound, nothing else in the pattern breaks.”**
- §4.1, lines 788–815: **“C*(k) = 2e (4 e^{-gamma} k)^k e^{1.45 sqrt k} <= (6.11)^k k! e^{1.45 sqrt k}.”** Also: **“C*(L+1) / (ln x)^{theta} = exp( (1+o(1)) L ln L )”**.

**Support class:** the class-lower-bound reduction is **CITED/ASSERTED**; the quantitative availability claim is contradicted by the dossier’s own **PROVED** asymptotic estimate.

**Why this is fatal**

Even granting an HL-scale lower bound for a matched-flank class of order

\[
\frac{x}{(\ln x)^k},
\]

an upper sieve for one rigid extra middle value has the scale

\[
C^*(k+1)\frac{x}{(\ln x)^{k+1}}.
\]

The upper/lower ratio, before any adverse singular-series ratio, is

\[
\frac{C^*(k+1)}{\ln x}.
\]

At the dossier’s depth \(k\asymp L\asymp (2/\ln2)\ln\ln x\), its own bound gives

\[
\log C^*(k+1)=(1+o(1))k\log k
  \asymp \ln\ln x\,\ln\ln\ln x,
\]

which dominates \(\log\ln x=\ln\ln x\). Therefore

\[
C^*(k+1)/\ln x\to\infty.
\]

The supplied D1-L bound is applicable in range, but it is **not quantitatively small enough to exclude rigidity**. “In regime” is not the same as “strong enough.” The claimed absorbing exclusion budget is neither displayed nor compatible with the stated constant.

Independently, the T1 anatomy itself names tail typicality/E4 at the sparse class as a second missing ingredient. An ordinary class-count lower bound does not automatically give an intersection with the D0 tail filters in the required quantifier order.

**Required narrower wording**

> A matched-flank class lower bound is one necessary input for a T1-style transplant. In addition, the argument needs an extension upper bound with a constant small enough at \(k\asymp\ln\ln x\), and a tail-typicality statement on the matched-flank class. D1-L as stated does not supply the required quantitative exclusion.

**Unstated load-bearing steps**

1. A comparison showing the extension upper bound is \(o\) of the flank-class lower bound at growing \(k\).
2. Uniform control of singular-series ratios for all candidate middles.
3. A lower bound after intersecting the matched-flank class with the near/far tail caps, or an equivalent conditional tail theorem.

---

## MAJOR

### MAJOR-1 — The Model-M almost-sure theorem omits its dependency/concentration proof

**Location and verbatim claims**

- §3.2 M1(a), lines 552–556: **“Hence a.s. eventually N_S >= x/(8 ln x) =: N_1 at every dyadic scale ([PROB-2] + [PROB-1]; filter events are functions of disjoint gap blocks, so the filtered count is a Lipschitz function of independent blocks and [PROB-3] applies; crude bounds suffice at the stated density).”**
- §3.2 M1(c), lines 565–568: **“the four cap events change all displayed probabilities by 1+o(1) factors (their failure probabilities are o(1) even conditionally on any window values under the cap, since tails are dominated by the geometric mass beyond the window).”**
- §3.5, lines 723–725: **“Two independent checker agents re-derived the section's computations from the setup + claimed answers only (derivations withheld).”**

**Support class:** **PROVED** as claimed, but the proof has an unstated load-bearing step; the checker statement is **CITED/ASSERTED**.

**Conviction**

The filters contain \(\delta_i^M\), which are infinite weighted tails, so they are not literally functions of disjoint finite gap blocks. More importantly, sites and words are indexed by the random ordered model-prime sequence. Flipping one underlying Bernoulli variable can shift all later prime indices, so a direct bounded-Lipschitz claim for the filtered indexed count is not supplied. The proof also conditions collision probabilities on filters that depend on overlapping gaps and tails without a quantitative uniform conditional estimate.

The expectation calculations may be salvageable, but the stated a.s. theorem and the M2 concentration conclusion require a truncation/coupling or dependency-graph argument that is absent. “Derivations withheld” cannot serve as reviewable support.

**Required narrower wording**

> The Model-M expectation and variance calculations predict the stated counts. A rigorous almost-sure theorem requires an explicit truncation of the delta tails and a dependency/concentration argument compatible with random prime indexing and filter conditioning.

---

### MAJOR-2 — “A′ > 1” does not imply the displayed positive site proportion when A″ = 16

**Location and verbatim claim**

- §2.7 P3.3′, lines 470–477: **“Fix A' in (1, 4 sqrt(2)/e), A'' = 16.”** And: **“Site abundance: |S'_x| >= N (1 - (1+o(1))/A' - 2/A'') - o(N), a positive proportion of pi(x) for A' > 1 strict (P3.1' + P3.2 twice).”**
- §4.0, lines 772–774: **“at the minimal admissible A' -> 1+”**.

**Support class:** **PROVED** algebra, which contradicts the prose conclusion.

**Conviction**

With \(A''=16\), the displayed coefficient tends to

\[
1-\frac1{A'}-\frac18.
\]

This is positive only when \(A'>8/7\), not for every \(A'>1\). Thus the stated primes-side Markov/PNT site-abundance argument does not justify taking the “minimal admissible” cap to \(1+\) under the fixed parameter map.

This can be repaired by choosing \(A''\) sufficiently large depending on a fixed \(A'-1\), or by restricting the proved interval to \(A'>8/7\). Neither repair appears in the statement.

**Required narrower wording**

> With A″ = 16, the displayed lower bound is positive for A′ > 8/7. For any fixed A′ > 1, one may instead choose A″ sufficiently large and then rerun the constant bookkeeping.

---

### MAJOR-3 — The depth floor is not forced by E4/E5 alone for every route

**Location and verbatim claims**

- §1 V3, lines 64–66: **“The depth floor J + K >= (2+o(1)) log2 ln x is (E4)/(E5)-forced for every middle width M”**.
- §6.1(a), lines 1123–1128: **“(E4) tail caps at tail-typical sites need D >= typical delta ~ ln x, and 2^K >= D; (E5) needs J >= log2(b D). Hence J, K >= (1+o(1)) log2 ln x REGARDLESS of the middle width M or the difference pattern.”**
- §6.3, lines 1170–1173: **“any prescriptive route must pin >= J + K = (2+o(1)) log2 ln x”**.

**Support class:** **PROVED** only under a tail-typical/positive-density premise.

**Conviction**

The body’s derivation explicitly assumes “tail-typical sites” and \(D\gtrsim\ln x\). E4 merely requires the selected sites to satisfy caps; it does not by itself preclude a construction concentrated on atypically small tails with smaller \(D\). Such a construction may face a sparsity penalty, but that is an additional argument, not the E4/E5 floor itself.

The V3 wording drops the premise and changes a route-relative statement into a universal one.

**Required narrower wording**

> For positive-density or otherwise tail-typical routes controlled through the D0/Markov selection layer, E4/E5 force J + K ≥ (2+o(1)) log2 ln x. A route using atypically small-tail sites would need a separate density-versus-depth analysis.

---

### MAJOR-4 — The three-blocker “confirmed EXHAUSTIVE” claim is not justified by the table

**Location and verbatim claims**

- §5, lines 1106–1112: **“No mechanism or composition in the corpus supplies all clauses simultaneously; each composition meets at least one of: class lower bounds (parity-blocked), sparse-site [PROB-5] cost ([AUTH-S]-circularity shape), pigeonhole variability-blindness. The three O4 blockers are confirmed EXHAUSTIVE for this corpus, with the sparse-site [PROB-5] cost now quantified as the uniform mechanism behind every TT failure.”**
- §1 V3, lines 72–74: **“Uniformly behind every tail-typicality failure in the corpus: the sparse-site [PROB-5] cost.”**

**Support class:** **CITED** tool cartography plus an unsupported exhaustiveness inference.

**Conviction**

The table presents T1–T6 and one matrix mechanism, sometimes grouping several of the claimed 14 texts. It does not provide:

- a one-to-one coverage ledger showing that every anchored text contributes no other mechanism;
- a formal definition of allowable “composition”;
- a closure argument proving that combining mechanisms cannot remove their individual blockers;
- an exhaustive list of TT failures with a demonstrated common reduction.

The rows support the more modest claim that **the mapped mechanisms, considered in the displayed ways**, meet one or more of the blockers. They do not prove exhaustiveness over all compositions in the corpus.

**Required narrower wording**

> Every individually mapped mechanism in T1–T6 and the [AUTH-K] matrix meets at least one of the three blockers in the displayed implementation. No mapped composition examined here supplies all clauses. Exhaustiveness over all possible compositions is not established.

---

### MAJOR-5 — Broad impossibility language escapes the stated corpus/route qualifiers

**Location and verbatim claims**

- §1 V3, lines 77–79: **“the entire unconditional content of supply-by-construction is the sparse-site tail clause.”**
- §4.3, lines 889–893: **“the floor's capacity term is the max-entropy simplex count; tightening it to the primes' true side-support requires exactly a two-point HL-type input (the collision constant), unavailable unconditionally -- the route cannot be completed by counting alone.”**
- §4.4, lines 920–921: **“The S-weighted floor (the only repair of F17.5's closure that stays on the counting route)”**.
- §4.4, lines 954–960: **“What remains open is only whether HL LOWER bounds at matched flanks (input (i), parity-blocked) could beat the second-moment denominator by the [INEQ-1] slack -- i.e., the counting route funnels back into blocker 2 with no constant to spare.”**
- §6.2, lines 1162–1164: **“the general (E2') clause makes pigeonhole-blindness strictly worse, never better”**.

**Support class:** mixed **PROVED** route calculations, **HEURISTIC**, and **CITED** tool limitations; no all-routes theorem.

**Conviction**

These sentences read as impossibility statements over broad method classes. The body only analyzes particular floor choices, filters, statistics, and cited constructions. It does not rule out entropy-sensitive side supports, asymmetric/adaptive filters, E-graded statistics, other weighted inequalities, or constructions that prove tail caps jointly rather than by post-selection.

The global sentence “all obstruction claims are … corpus-relative” is not an inline qualifier and does not resolve the literal breadth of “only,” “exactly,” “cannot,” and “entire.”

**Required narrower wording**

> For the D0.2/D0.2′ max-entropy floors and the mapped constructions in this corpus, the identified unresolved inputs are [named inputs]. No impossibility claim is made for other counting statistics, filter shapes, or construction methods.

---

### MAJOR-6 — P3.2’s constant 13 is not proved under its stated range

**Location and verbatim claim**

- §2.5 P3.2, lines 317–333: **“For 0 <= r <= L and N >= L + 16: sum_{n<=N} delta_{n+r} <= 13 C_0 N ln N”**; the proof concludes **“Total < 12 C_0 (N'+2) ln(N'+4) <= 13 C_0 N ln N for N >= L+16.”**

**Support class:** **PROVED** claim with an invalid final inequality under the stated hypotheses.

**Conviction**

Here \(N'=N+L\). The condition \(N\ge L+16\) permits \(L\) to be almost \(N\), in which case \(N'+2\) is almost \(2N\), and

\[
12(N'+2)\ln(N'+4)
\]

can be roughly \(24N\ln(2N)\), not at most \(13N\ln N\). The application has \(L=o(N)\), so a repaired asymptotic statement is likely available, but that condition is not in the lemma.

This lemma feeds both tail-filter losses and the D0.2′ site-abundance estimate, so the missing range condition is load-bearing.

**Required narrower wording**

> For the application regime L = o(N), and after increasing the threshold so that (N+L+2) ln(N+L+4) ≤ (13/12)N ln N, the stated 13C₀ bound holds. Alternatively, retain N ≥ L+16 and replace 13 by a sufficiently large absolute constant.

---

### MAJOR-7 — Certificate verification, reproduction, and “first of the project” are over-scoped

**Location and verbatim claims**

- §7, lines 1195–1197: **“exchange-class counts REPRODUCE the committed record”**.
- §7.1, lines 1237–1240: **“Class counts REPRODUCE the committed record 12/178/1287, 2/21/143, first (6,6,64) at 1e8.”**
- §7.2, lines 1268–1269: **“FIRST b > 1 CERTIFICATES OF THE PROJECT (E5 honored; verified by hand this session, gap-by-gap from the printed primes)”**.

**Support class:** **MEASURED** script output, partly **PROVED** by finite arithmetic, and **CITED** project-record/history claims.

**Conviction**

From the printed primes one can check the finite word data:

- both first seven gaps are `[4,2,16,2,10,12,18]`;
- the middle gaps are `6` and `30`, so \(d_1=-24\);
- the next six gaps agree as `[20,12,4,14,6,4]`;
- the gates \(3(44-2)=126<256\) and \(5(27-2)=125<256\) hold.

But the far-tail quantities \(\delta_{t+L}\) require primes beyond the 16 printed primes. The decimal tail values and the full scan counts therefore rely on the script/data, not “gap-by-gap from the printed primes.” Likewise, the supplied pair of files does not contain the prior committed record or a complete project-history audit, so “reproduce” and “FIRST … OF THE PROJECT” are not independently established here.

**Required narrower wording**

> The printed primes hand-verify the matched prefix/suffix, differing middle, and E5 gates. The delta caps and scan totals were computed by `d5b_deep.py`. Those totals match the prior figures quoted in this dossier. These are the first b > 1 certificates found in the searched project record as described by the executor.

---

## MINOR

### MINOR-1 — “Every reachable x” exceeds the measurements actually listed

**Location and verbatim claims**

- §1 V2, lines 58–59: **“measured above threshold at every reachable x.”**
- §7, lines 1209–1211: **“lambda_w means are >> 1 at all reachable x (sub-1-mass corner: realized words have N_w >= 1 while HL mass << 1) -- the D1.a-relevant regime is not directly observable at x <= 1e8.”**

**Support class:** **MEASURED**.

**Conviction**

The listed marginal \(\gamma_2\) measurements are at two scales; the listed vector measurements are at three scales and selected \((J,K)\). These data support “at every reported scale/configuration,” not every computationally reachable \(x\) or every \(x\le10^8\).

**Required narrower wording**

> The statistic is above threshold at each reported measurement scale and grid point.

---

### MINOR-2 — The explicit M1 matching floor differs by a factor of two between theorem and proof

**Location and verbatim claims**

- §3.2 Theorem M1, lines 534–536: **“the explicit disjoint floor is N_S/(8 (2-p)^{J+K})”**.
- §3.2 proof, lines 597–600: **“the matching size is >= T/(4 max_deg) >= (N_S^2 q_2^{J+K}/2)/(8 N_S p^{J+K}) = (N_S/16)(2-p)^{-(J+K)} = N_S (ln x)^{-2+o(1)} = x^{1-o(1)}.”**
- §3.5, lines 726–730: the checker says the matching floor is confirmed **“at the /16 level.”**

**Support class:** **PROVED**.

**Conviction**

The theorem states \(1/8\); the displayed greedy argument and checker support \(1/16\). The asymptotic \(x^{1-o(1)}\) conclusion is unaffected, but “all constants confirmed” is false as written.

**Required narrower wording**

> Replace the theorem’s explicit floor by N_S/(16(2-p)^{J+K}), or strengthen the matching calculation to justify 1/8.

---

### MINOR-3 — “Euler product = direct sum” states equality where only numerical agreement is shown

**Location and verbatim claims**

- §1 V6, lines 102–104: **“Euler product = direct sum.”**
- §4.3, lines 876–878: infinite-product value `4.601923...` and finite direct sum `4.601842 at D = 2e6`.

**Support class:** product evaluation **HEURISTIC/CITED** in its application; finite summation **MEASURED**.

**Conviction**

The displayed numbers are close but unequal. The finite truncation is a numerical consistency check, not identity.

**Required narrower wording**

> The D = 2e6 direct sum agrees with the Euler-product value to about 8×10⁻⁵.

---

### MINOR-4 — “Primes-specific” is stronger than the model gate can establish

**Location and verbatim claim**

- §1 V1, lines 45–46: **“The failure of unconditional supply is primes-specific, not architectural.”**

**Support class:** **HEURISTIC** architectural inference.

**Conviction**

A successful toy model establishes that the tested obstruction is not universal across that model class. It does not show that the actual failure is specifically caused by prime arithmetic, nor that every architectural issue has been excluded.

**Required narrower wording**

> The tested obstruction is absent in Model M, so the model gate finds no architectural contradiction at this level.

---

## NOTE

### NOTE-1 — The finite certificate core is internally consistent, conditional on the printed delta values

**Location:** §7.2, lines 1270–1286.

**Support class:** **PROVED** finite arithmetic plus **MEASURED** tail inputs.

The two printed prime lists give gap words

- `[4,2,16,2,10,12,18,6,20,12,4,14,6,4,12]`,
- `[4,2,16,2,10,12,18,30,20,12,4,14,6,4,6]`.

Thus the \((J,K)=(7,6)\) prefix/suffix match and \(d_1=-24\) check. Using the printed far-tail decimals, the E2′ comparison has

\[
|d_1|2^{-8}=0.09375,
\qquad
2^{-14}|14.562-21.089|\approx0.00039838,
\]

a factor of about 235 in the required direction. This strongly supports the certificate once the script-computed delta values are accepted. It does not validate the “from printed primes” wording for the tails.

### NOTE-2 — V5 is materially better scoped than V1–V4 and V6

**Location:** §1 V5 and §2.6.

**Support class:** internal implication **PROVED**, external interface quotation **CITED**.

The distinction between `SUP_1^norm`, `SUP'_1`, and the landed normal-form consumer is clearly recorded, including the missing normal-form post-processing step. The only recommended repair is to clarify that the `>` symbol denotes consumer priority/fit rather than ordinary logical strength, because “SUP′_b all odd b” is stronger as a family of hypotheses than the b = 1 instance.

---

# S2 — Impossibility-language sweep

The following sentences read more broadly than the body proves. Some are already addressed in the findings above; they are collected here to make the payload’s S2 check explicit.

| Exact sentence | Why it reads as all-routes impossibility | Required scope |
|---|---|---|
| **“V2 (the counting route, exactly closed).”** (§1, line 48) | Encompasses counting routes not analyzed and conflicts with the “typical-set capacity” survivor. | “The unweighted max-entropy floor under D0.2/D0.2′ is closed conditionally/heuristically as specified.” |
| **“NO admissible aggregate cap A' > 1 opens the unweighted floor route.”** (§4.3, lines 886–888) | Unqualified primes truth claim derived from heuristic/marginal data. | “Under the HL-frame collision asymptote, no fixed A′ > 1 opens this D0.2′ max-entropy floor.” |
| **“the route cannot be completed by counting alone.”** (§4.3, lines 891–893) | Rules out other capacity/entropy estimates without proof. | “This max-entropy implementation cannot be completed with the supplied unconditional counting inputs.” |
| **“The S-weighted floor (the only repair of F17.5's closure that stays on the counting route)”** (§4.4, lines 920–921) | Contradicted by the typical-set route listed in §4.3. | “One repair considered here is the S-weighted floor.” |
| **“What remains open is only whether HL LOWER bounds at matched flanks (input (i), parity-blocked) could beat the second-moment denominator by the [INEQ-1] slack”** (§4.4, lines 957–960) | Suppresses the unproved growing-k second moment and other repairs. | List both lower-bound and growing-k moment requirements; do not say “only.” |
| **“All roads of this dossier terminate at this one input.”** (§1, lines 91–92) | Unsupported because the dossier itself lists another TT input and the sieve exclusion fails quantitatively. | “The T1 transplant highlights this candidate input, among additional uniformity and tail requirements.” |
| **“No mechanism or composition in the corpus supplies all clauses simultaneously.”** (§5, lines 1106–1109) | No exhaustive composition argument is supplied. | “No displayed mechanism or examined composition supplies all clauses.” |
| **“the entire unconditional content of supply-by-construction is the sparse-site tail clause.”** (§1, lines 77–79; similarly F17.8) | Reads beyond T3 and beyond the mapped corpus. | “For the mapped T3 trap implementation, the remaining unconditional gap is the sparse-site tail clause.” |
| **“the general (E2') clause makes pigeonhole-blindness strictly worse, never better”** (§6.2, lines 1162–1164) | The example defeats bare P1 positivity, not every E-sensitive pigeonhole statistic. | “For the ungraded P1 side-collision statistic, M ≥ 2 adds an E = 0 degeneracy.” |

---

# S3 — Model/primes and heuristic-discipline result

**Result: failed at the verdict and findings-register layers.**

The body often labels Model M correctly, and §4.3 explicitly labels its “TRUTH face” as heuristic and empirical. The leakage occurs when those conclusions are promoted without the labels:

- V1: **“The failure of unconditional supply is primes-specific, not architectural.”**
- V2: **“the primes close the route through the exactly-computed two-point HL mass.”**
- F17.5 register, lines 1418–1422: **“The route is closed for the primes at every admissible A' > 1, independently of the sieve constant, and invisibly to Model M (gamma_2 = 1/2). HL clumping both supplies the exchange configurations and defeats the max-entropy capacity floor.”**

The “PROVABILITY face” is also too strong when it says true-support tightening **“requires exactly a two-point HL-type input.”** The body has not proved that every unconditional entropy/capacity refinement is equivalent to such an input.

Required discipline: retain “under the HL-frame heuristic,” “at the reported finite scales,” and “for this max-entropy floor” every time the conclusion is carried into §1 or the findings register.

---

# S4 — Quantifier-order result

**Result: failed in four places.**

1. **A′ range:** fixed A″ = 16 only proves positive density for A′ > 8/7, not all A′ > 1.
2. **Filter quantifier:** the threshold calculus covers D0.2′’s single window-sum simplex and a max-entropy capacity bound. It does not quantify over different filter shapes or typical-set supports.
3. **Measurement quantifier:** “every reachable x” should be “every reported measurement.”
4. **Depth quantifier:** the \((2+o(1))\log_2\ln x\) floor is derived after imposing tail typicality; it is not E4/E5 alone over all site-selection routes.

---

# S5 — Three-blocker exhaustiveness result

**Result: not established.**

The table is a useful taxonomy, but “confirmed EXHAUSTIVE” requires a coverage and composition argument that is absent. The safe conclusion is limited to the mechanisms and combinations explicitly displayed.

---

# S6 — Certificate-claim result

**Result: partially supported, over-scoped in wording.**

The finite word, gates, and weighted-middle inequality are checkable and consistent. Delta tails and class counts are script outputs. “Reproduces the committed record” and “first of the project” are external-history claims not established by the two-file blind package.

---

# S7 — Unstated load-bearing steps identified

1. **Growing-window collision tensorization:** marginal \(\gamma_2\) must control \((J+K)\)-coordinate consecutive gap collisions uniformly as \(J+K\to\infty\).
2. **Growing-k singular-series moment lower bound:** the fixed-k value 1.1505 must be shown to compound on the relevant simplex; k = 2 does not prove this.
3. **T1 extension exclusion:** D1-L’s growing-k constant must be \(o(\ln x)\) relative to a flank-class lower bound; the supplied constant is instead much larger.
4. **Tail intersection for V4:** the matched-flank lower bound must survive the near/far tail filters in the correct selection order.
5. **Model concentration:** truncate infinite delta tails and establish a dependency/Lipschitz argument compatible with random prime indexing and overlapping windows.
6. **P3.2 range repair:** add \(L=o(N)\) or enlarge the constant before using the tail-density bound.
7. **Exhaustive composition closure:** define the composition class and prove each possible composition inherits a listed blocker.
8. **Certificate tail audit:** identify the data/script computation used for delta values beyond the printed prime windows.

---

## Final disposition

The dossier should not be accepted with its current Section 1 verdict. A repair would need, at minimum:

- downgrade V2 from unconditional/exact closure to a route-specific heuristic-and-measurement obstruction;
- withdraw V4’s “single missing input” statement unless a new quantitative exclusion and tail-intersection proof is supplied;
- downgrade M1/M2 from proved a.s. statements or add the missing dependency argument;
- replace the exhaustiveness and all-routes language with explicit corpus-and-implementation qualifiers;
- split hand-verified certificate facts from script-computed tails/counts and project-history assertions.

Because V2 and V4 are not merely imprecise summaries but central conclusions contradicted by the supplied body, the appropriate current verdict is **UNSOUND**, not “sound with repairable wording issues.”
