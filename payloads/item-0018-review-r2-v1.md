# Adversarial Scope Audit — item-0018 M1 Statement Layer

**Review object:** `item-0018-review-object-v1.md`  
**Review payload:** `item-0018-review-r2-payload-v1.md`  
**Required review role:** blind cross-family adversarial scope audit  
**Web use:** none  
**Authorized corpus:** the review object, the payload, and the ten-file reference pack only  
**Operator hash override:** the operator confirmed that `fb4dbdc804d351c749468a9d51a3a5071fbe8a892d22603054e43c5757857c3d` is the canonical hash of the supplied `runs/README.md`; the older hash in the payload manifest is superseded.

## Overall verdict

**SOUND WITH REPAIRABLE ISSUES**  
**Confidence:** `0.94`

The central conditional consumer design is sound: the Section 7.2 finite pigeonhole is valid, its quantifier coupling is valid in the final epsilon-form of `RelExtensionUpper`, the `A' = 3/2`, `A'' = 48` population arithmetic supplies the stated `N/4` floor for each fixed threshold, and Section 7.3 matches every field of the supplied `ExchangeAt` structure and the threshold quantifier of `ExchangeSupply1`.

No FATAL finding was found.

The object nevertheless does not yet meet its own claim that every candidate is an exactly quantified statement. The selected B-layer candidate is written in two non-equivalent syntactic forms, with an unquantified rate function in Section 4 and a correct epsilon-form only later in Section 7. Several C-layer family dependencies are not pinned; route-specific obstructions are promoted to unconditional closure language; one heuristic wall is repeated in the findings register without its heuristic qualifier; and the redacted-site Model-M claim says “derivable” although the supplied dossier proves only a weaker result in a different filter regime. The numerical budget tables and several claimed finite computations are also outside the authorized twelve-file corpus, so their exact coverage cannot be audited.

---

# Findings

## FATAL

None.

---

## MAJOR

### MAJOR-1 — The selected B2 statement is not closed as written; `C_F` is unquantified and the epsilon-prefix does not bind the displayed bound

**Location:** Section 4.B, Candidate B2; Section 9 D3 row for B2.

> “Selection form (B2.plain): for every eps > 0 there is x_4(eps) with: for all x >= x_4, all s >= 0, and EVERY selection function P |-> d_P …  
> `sum over P of N_{P, d_P} <= (C_F(x)/ln x) * sum over P of N_P,`  
> `gate: C_F(x) = o(ln x) [equivalently, RHS = eps * sum N_P eventually, for every eps > 0].`”

> “The pure-concentration isolate is the REDUCED form (B2.reduced), the selected candidate:  
> `sum over P of ( N_{P, d_P} - 1 )_+ <= (C_F(x)/ln x) * sum over P of N_P, same quantifiers, same gate.`”

> “B2 … pass … CONDITIONAL (OI-B2 = item-0020 target); reduced form selected.”

**Support class assigned:** OPEN target, but **UNDER-SPECIFIED** as a proposition.

The prefix quantifies `eps`, but `eps` does not occur in the displayed inequality. Conversely, `C_F` occurs in the inequality but is never introduced by `exists`, `forall`, or a fixed-parameter declaration. “`C_F(x)` explicit” is not a quantifier. The rate form and epsilon form are mathematically equivalent only after one of them has first been stated as a closed proposition with uniformity in `s` and the selection.

Section 7.1 later gives a correct closed epsilon-form:

> “forall eps > 0, exists x_4(eps), forall x >= x_4, forall s, forall selections (d_P):  
> `sum over P of (N_{P,d_P} - 1)_+ <= eps * sum over P of N_P.`”

That later repair makes the consumer implication usable, but it does not retroactively make Candidate B2 in Section 4 exactly quantified. The D3 “pass” row is therefore stronger than the candidate body supports.

**Required wording:** adopt the Section 7.1 epsilon-form verbatim in Section 4 and remove `C_F` from the formal candidate; or state a rate form such as:

> There exists a fixed nonnegative function `C_F` with `C_F(x)/ln x -> 0` and a threshold `x_4` such that, for all `x >= x_4`, all `s`, and all selections, the displayed rate inequality holds.

The epsilon-form is preferable because it is exactly what Section 7.2 consumes.

---

### MAJOR-2 — B3 has the same unquantified-rate defect, and the dependence of `C_q` on the exceptional-mass parameter is not pinned

**Location:** Section 4.B, Candidate B3; Section 9 D3 row for B3.

> “For every eps > 0 there is x_5(eps): for all x >= x_5, s >= 0, there is an exceptional sub-family E … such that …  
> `N_{P,d}(x) <= (C_q(x)/ln x) * N_P(x) + 1,`  
> `gate C_q(x) = o(ln x).`”

> “B3 … pass … CONDITIONAL(OI-B2 fallback).”

**Support class assigned:** OPEN target, but **UNDER-SPECIFIED**.

`C_q` is not quantified. It is also unclear whether one fixed rate function works for every `eps`, whether a separate `C_{q,eps}` is allowed, or whether `C_q` may depend on the family rule. Those choices are materially different when Section 7.4 couples the exceptional mass to `delta/4`.

The claim that B3 is derivable from B2.reduced is plausible after a rate has been extracted from the epsilon-form and a weighted Markov argument is written, but that does not repair B3’s own prefix.

**Required wording:** for example,

> There exists a fixed nonnegative function `C_q` with `C_q(x)/ln x -> 0` such that, for every `eps > 0`, there exists `x_5(eps)` for which the exceptional-family and per-class conclusions hold for all `x >= x_5(eps)` and all `s`.

Any dependence of `C_q` on `eps`, the D0 pins, or the family rule must instead be declared explicitly.

---

### MAJOR-3 — A1-typ is described as both “the same display” and “thinning-corrected,” but no exact candidate inequality or full prefix is given

**Location:** Section 4.A, A1-typ; Section 8 A-layer verdict; Section 9 D3 row for A1typ.

> “A1-typ (exchange-typical-span variant; named open input OI-A1). The same display with (h2) replaced by the D0 window budget span <= A' L ln x is NOT derivable from the landed machinery … and its honest heuristic form carries the Cramer thinning factor `(ln x)^{-tau(A')}` … Kept as a statement target only.”

> “A-layer: … A1-typ (open; thinning-corrected; statement target only).”

**Support class assigned:** OPEN target with HEURISTIC motivation, but **not an exact statement**.

“The same display” would retain A1’s unthinned lower bound. “Thinning-corrected” requires a different lower bound. The object never says whether the candidate conclusion is

- the unthinned A1 conclusion at larger span;
- a lower bound multiplied by `(ln x)^{-tau(A')}`;
- a bound with an additional `o(1)` in the exponent;
- or a two-sided consecutive-count law.

It also does not restate whether `HLQuantA` remains an assumption, how the thinning error is uniform in `(P,d)`, or what the threshold depends on. Consequently, the D3 row cannot legitimately record that this candidate has passed quantifier and open-strength hygiene.

**Required wording:** write one complete inequality with its entire prefix, including the `HLQuantA` assumption if retained, the exact exponent/error convention, uniformity over `(P,d)`, and all threshold dependencies. If only a heuristic formula is intended, label it as a heuristic template rather than a candidate theorem.

---

### MAJOR-4 — C1’s family is not pinned independently of `s` or the cap outcome; as written it permits circular post-cap family selection

**Location:** Section 4.C, Candidate C1.

> “For a specified family FF(x) subset Fam of side pairs: there is eps_C < 1/2 and x_6 with: for all x >= x_6, s >= 0:  
> `sum over P in FF(x) of N_P(S'^{(s)}_x) >= (1 - eps_C) * sum over P in FF(x) of N^w_P(x).`”

> “DEFINITION (eta): the family site-density is eta(x) := `(sum over P in FF(x) of N^w_P(x)) / N`.”

**Support class assigned:** OPEN target, but **UNDER-SPECIFIED** and potentially circular.

By RS.1, omitted `Fam` arguments default to the capped set `S'^{(s)}_x`, which depends on both `s` and `x`. C1 instead writes `FF(x)`, then quantifies over every `s`. It is therefore unclear whether:

1. `FF` is a family rule `FF_{s,x}`;
2. it is fixed independently of `s`;
3. it is selected from the window-only family;
4. or it may be selected after seeing which classes survive the caps.

The fourth interpretation is circular for a cap-retention theorem: classes whose entire window mass is destroyed by the caps can be omitted by defining `FF` from the capped realized family. The empty family also satisfies the display trivially. The dependence of `eps_C` and `x_6` on the family rule is not declared.

This ambiguity propagates into the item-0021 transfer target and the D3 “pass” row for C1.

**Required wording:** quantify an **ex ante family rule**, for example `FF_{s,x}` defined from window-only side data or otherwise declared independent of the two delta-cap outcomes. State whether the theorem is for every such family or for one named family, and state the dependencies of `eps_C` and `x_6`. Use `N^{w,(s)}_P` notation or an equivalent explicit definition so that the threshold dependence is visible on both sides.

---

### MAJOR-5 — The C-layer obstruction is repeatedly promoted from “this recorded route fails” to unconditional closure language

**Location:** Section 4.A A1 consumer-fit note; Section 6 consequence; Section 10 F18.2.

> “The class is HL-thin … and the C-layer window for thin classes is CLOSED unconditionally (F18.2, budget T6(b)).”

> “the small-span route re-concentrates the entire unconditional burden onto the C-layer at thin density, where F18.2 closes the window.”

> “The A-side thinning tau(A') = 2A'/ln 2 >= 2.885 exceeds c* for every admissible A', so no single thinned class ever fits: C-layer viability is a family property.”

**Support class assigned:** ROUTE-RELATIVE necessity analysis; part HEURISTIC through U18.1.

C1 itself correctly says:

> “a NECESSITY budget. It is NOT sufficient”

and later limits the per-class statement to what is

> “unreachable by this route.”

The quoted “CLOSED unconditionally” and “no single … ever fits” language is broader. The supplied analysis excludes the recorded truncated-tail/HLQuantA-numerator route at the stated density; it does not prove that every possible tail-intersection theorem for a thin class is impossible. Moreover, the `tau(A')` thinning law is explicitly U18.1 heuristic, so it cannot support an unqualified “ever.”

The overstatement affects the Section 8 ranking of A1, but it does not invalidate the selected A3+B2+C2 implication.

**Required wording:** replace the absolute clauses by:

> The recorded truncated-tail transfer, within the frozen `HLQuantA` card budget, does not cover a family of this density. Under the U18.1 thinning heuristic, a single typical-span class also lies outside that route’s `c*` window.

Do not use “closed unconditionally” without “for this route.”

---

### MAJOR-6 — F18.1 repeats the heuristic half of wall w2 as an established finding without its inline qualifier

**Location:** Section 6 wall w2; Section 10 F18.1.

Section 6 correctly discloses:

> “[Scope tag, audit-added: the LOWER-bound half of ‘true size’ -- that the ratio sum really is Theta(W/ln x) -- is the growing-k mean-2 heuristic, U18.2-class; w1 is the PROVED half of the wall.]”

But F18.1 states:

> “at exchange-typical span the transfer is blocked by walls w1 (necessary span hypothesis of oneExtension_sum_le) and w2 (the Theta(L)-oversized extension term against the ln x/8 reserve, sieve-constant-independent) -- both quantified in budget T5(b).”

**Support class assigned:** w1 = PROVED/CITED; the lower-bound half of w2 = HEURISTIC.

The findings register is explicitly one of the payload’s mandatory support-class audit surfaces. The heuristic qualifier does not travel with the repeated w2 claim. “Both quantified” is not a substitute for “one side is heuristic.” The current wording promotes U18.2-class support to a finding.

This does not destroy the reuse-audit conclusion that the landed `oneExtension_sum_le` theorem cannot be applied at exchange span: w1 alone establishes that statement about the landed route.

**Required wording:** state:

> w1 is a proved regime boundary of the landed declaration. Under the U18.2 growing-k mean heuristic, w2 predicts an additional `Theta(L)` size obstruction.

---

### MAJOR-7 — U18.6 says the Model-M A3 analogue is “derivable,” but the supplied dossier proves a weaker fraction in a different filter regime

**Location:** Section 4.A A3 support; Section 11 U18.6; declared redaction site r3.

> “the Model M analogue at delta = 1 - o(1) is DERIVABLE FROM the Theorem M1 toolkit … but is NOT STATED in M1”

> “U18.6 The Model-M analogue of A3 at delta = 1 - o(1): derivable from the Theorem M1 toolkit … Write-out debt … until discharged, A3 carries no PROVED model tag.”

**Support class assigned:** MODEL-motivated OPEN derivation, not DERIVED in the supplied corpus.

The supplied predecessor dossier’s Theorem M1 proves an explicit disjoint-pair floor corresponding only to a `(ln x)^{-2+o(1)}` twinned-site fraction. It is formulated with `Par(1,x)` and the per-position filter `S^M_x(A,D)`. Candidate A3 is formulated on the aggregate-filter set `S'_x` with the distinct `Par'(1,x)` pins.

A `delta = 1-o(1)` site-mass conclusion may well be obtainable, but it needs at least:

1. a **uniform lower** bound on the match probability for every aggregate-window-admissible side word, not merely the upper-degree estimate used in M1(e);
2. a lower-tail argument after residue-class dilution;
3. adaptation of the cap-conditioning and site-concentration layer from `Par` to `Par'`;
4. a conversion from positive degree to mass in `Fam_2`.

None is written in the authorized corpus. Calling the result “derivable” is therefore a support-class promotion, even though the object commendably withholds a PROVED tag.

**Required wording:** replace “derivable” by:

> plausibly derivable after an additional uniform lower-tail argument and an adaptation from `Par` to `Par'`; no such derivation is supplied here.

Alternatively, add the complete derivation to the authorized corpus.

---

### MAJOR-8 — The universal per-class C1'' obstruction uses an unstated class-density upper bound

**Location:** Section 4.C, C1''.

> “at exchange rank a single class has density at most ~ `(ln x)^{-(k-1)}`, driving the needed tail rank to ~ `(k-1) lnln x/ln2` >> the headroom: per-class C1'' is unreachable by this route for ANY family at exchange rank”

**Support class assigned:** ASSERTED route calculation with an UNSTATED load-bearing step.

No displayed argument in the object proves the quoted upper bound for a **side class**, which is a sum over all allowed middles. `HLQuantA` concerns nonconsecutive full tuples; A1 supplies a consecutive lower bound at small span. To obtain the asserted side-class upper density one must state and price, at minimum:

- a full-word upper bound with its growing-`k` constant and singular-series dependence;
- the number of allowed middle values;
- the summation over those middles;
- and the normalization by `N = pi(x)`.

The conclusion may survive such a calculation at the coarse `exp(-Theta((lnln x)^2))` scale, but the object neither displays it nor cites a declaration that delivers it. It is load-bearing for the phrase “ANY family.”

**Required wording:** either provide the side-class upper-bound derivation and its budget row, or narrow the claim to:

> for a class known independently to have density `exp(-Theta((lnln x)^2))`, this recorded C1 route exceeds the frozen card headroom.

---

### MAJOR-9 — Exact budget coverage and several finite numerical witnesses rely on workpapers outside the authorized corpus

**Location:** Sections 0, 3, 4, 5, and 6.

> “Companion workpapers: dossier/item-0018-workpapers/budget_sheet.py and its companion output budget_sheet_tables.txt”

> “Per-candidate pointers (every k- or x-dependent constant class of Section 4 appears in at least one row …)”

> “budget T4 witnesses”

> “ratio rows 101 -> 268 across the grid”

**Support class assigned:** COMPUTED / OUT-OF-CORPUS / UNVERIFIED.

The payload authorizes exactly twelve files. Neither `budget_sheet.py` nor `budget_sheet_tables.txt` is in that pack. Therefore S6 cannot verify the claim that every candidate factor appears in an actual table row, and S8 cannot accept exact finite witnesses whose only stated provenance is those absent files.

Several important symbolic calculations can be re-derived from the supplied text—the `1/4` population floor, `c*`, the depth-inflation formulas, and the local `rho` formula—but the following remain uncheckable as exact reported computations: the T4 finite `rho` values, the T5 finite vacuity thresholds and ratios, the T7 reserve table, and the “exactly one admissible in-budget middle” computation.

Even the Section 5 pointer index does not visibly book every introduced variant parameter. At least the following are not named in a concrete row description:

- the multiplicity function `m(x)` in A3(m);
- the per-class mass floor `mu(x)` in C1'';
- the fixed profile margin `eps` in C1(n1).

**Required wording or corpus repair:** either place the two workpapers in an operator-authorized review pack, or reproduce the decisive rows and formulas inside the object. Until then, label exact finite outputs “reported by an unavailable companion computation” and do not claim S6 completeness.

---

## MINOR

### MINOR-1 — F18.5’s unconditional singleton counterexample ignores B1’s `rho`-cap domain

**Location:** Section 4.B B1; Section 10 F18.5.

> “WITHOUT the floor (b1-floor) the pointwise form is FALSE at any scale where small classes exist”

> “the pointwise relative extension bound WITHOUT a multiplicity floor is false wherever singleton/small classes exist”

**Support class assigned:** LOGICAL, but only under an additional domain condition.

For a singleton class with realized middle `d`, the contradiction is valid when the candidate actually quantifies that cell and its coefficient is `o(1)`, for example when `rho(P,d) <= R(x) = o(ln x)`. B1 does not quantify realized middles outside the `rho` cap. The mere existence of a singleton class therefore does not by itself refute the capped no-floor statement.

**Required wording:**

> Without the multiplicity floor, the capped pointwise form is false whenever a small class has a realized middle inside the `rho <= R(x)` domain; the uncapped constant-`o(ln x)` form is false for every sufficiently small realized class.

---

### MINOR-2 — “B1 is logically the strongest” is false; the B candidates are incomparable across their domains

**Location:** Section 8 opening gloss.

> “B1 is logically the strongest B-layer statement and is ranked last”

**Support class assigned:** ASSERTED comparison.

B1 gives a sharp pointwise result only for high-multiplicity, `rho`-capped classes. B2.reduced covers all realized classes in aggregate and includes the small and high-`rho` populations excluded from B1. Neither proposition, as stated, implies the other.

**Required wording:**

> B1 gives the strongest pointwise conclusion on its restricted domain, but it is not logically comparable with the global averaged forms.

---

### MINOR-3 — The threshold dictionary uses two different paper-to-Lean conventions

**Location:** Section 1 D0 table; Section 7.3.

> “paper; Lean t = s+2 (FW-3)”

> “thresholds: n, m >= s+1 >= t for the Lean threshold t with s := t”

**Support class assigned:** PROVED-compatible, but not a single fixed dictionary.

Both choices can establish `ExchangeSupply1`: setting the paper threshold to `t` is stronger than needed, and the downstream theorem later calls `ExchangeSupply1` at `t = s+2`. The mathematics is sound, but the object claims the dictionary is fixed and then uses two conventions.

**Required wording:** choose one convention. The cleanest is:

> To prove `ExchangeSupply1` at Lean threshold `t`, apply the paper propositions with paper threshold `s=t`; the downstream dyadic theorem itself later supplies `t=s_dyadic+2`.

---

### MINOR-4 — RS.3 states quotient factor algebra without restricting to positive denominator singular series

**Location:** Section 3, Definition RS.3.

> “For P = (a,c) and even d: `rho(P,d) := S(H(a,d,c)) / ( S(H_pre(a)) * S(H_suf(c)) )`”

> “EXACT LOCAL FORM … per odd prime the factor of rho is …”

**Support class assigned:** PROSE algebra valid on the admissible/positive-denominator domain.

For arbitrary even side pairs, `H_pre` or `H_suf` can be inadmissible, making the denominator singular series zero. Real-number division may still have a formal convention, but the Euler-factor quotient and insert-log argument require positive denominator factors. Realized large-anchor words are expected to be admissible, and B1’s multiplicity floor removes many exceptional patterns, but the definition itself does not state a domain.

**Required wording:** restrict RS.3’s factorized quotient claims to side blocks with positive singular series, or explicitly define a convention for zero denominators and exclude that case from B1 and m3.

---

### MINOR-5 — B1′ does not quantify its “absolute” constant or add it to the threshold dependence

**Location:** Section 4.B, B1′.

> “B1' … with `(rho + eps)` replaced by `C_rel * rho` for an absolute `C_rel >= 1`”

**Support class assigned:** OPEN target, locally under-specified.

It is unclear whether the statement asserts the existence of one absolute `C_rel`, holds for every such constant, or treats it as a fixed external parameter. The threshold notation still reads `x_3(eps; eps_0,R)` even though the precision parameter `eps` has disappeared.

**Required wording:** state either `there exists an absolute C_rel >= 1` and include it in the threshold data, or declare it as a fixed candidate parameter before the prefix.

---

## NOTE

### NOTE-1 — The two “proved” tags are sustained

**A2:** The equality is the RS.1 partition identity. The lower bound is exactly the thresholded form of dossier P3.3′(ii): remove at most `s` initial sites from the aggregate-filter population. The generalized repaired A′′ clause in the dossier supports the D0 pin `A''=48`.

**C2 base form:** It is the same P3.3′(ii) site-abundance statement read as a filters-first population theorem. Both delta caps are inside `S'_x` by definition. This tag is properly “proved at dossier level,” not a Lean theorem.

No support-class promotion was found in these two tags.

---

### NOTE-2 — The Section 7.2 pigeonhole is valid

Fix `s` and take `x` beyond the three thresholds. Under middle rigidity, every class has a selected realized middle and

\[
\sum_P (N_{P,d_P}-1)_+
 = \sum_P (N_P-1)
 \ge \frac12\sum_{P\in\mathrm{Fam}_2}N_P
 \ge \frac{\delta}{2}|S'^{(s)}_x|
 = \frac{\delta}{2}\sum_P N_P.
\]

The epsilon-form of `RelExtensionUpper` at `eps=delta/4` gives the contradictory upper bound. `TailIntersection` supplies strict positivity. The selection is admissible because every realized middle is even and is at most the positive aggregate window sum `A' L ln x`.

---

### NOTE-3 — The `N/4` arithmetic is correct

At the pinned constants,

\[
1-\frac1{A'}-\frac2{A''}
=1-\frac23-\frac1{24}
=\frac7{24}
=\frac14+\frac1{24}.
\]

For each fixed `s`, the `-s-o(N)` loss is absorbed by choosing `x_7(s)` sufficiently large. Thus Section 7.1’s `N/4` floor is supported; it would not follow from the predecessor dossier’s old example `A''=12`.

---

### NOTE-4 — Section 7.3 is faithful to `Exchange.lean`

The supplied Lean structure requires:

- `1 <= J`, `1 <= K`;
- `SameBlock n m J`;
- `gap (n+J) != gap (m+J)`;
- `SameBlock (n+J+1) (m+J+1) K`;
- near caps at `delta(n+J)` and `delta(m+J)`;
- far caps at `delta(n+J+1+K)` and `delta(m+J+1+K)`;
- and the separate real gate `(D:ℝ)-2 < 2^(J+1)`.

The object supplies each field with the correct ANN-50 shift. Since `L=J+1+K`, the paper far index `n+L` matches the Lean far index. From `D <= 2^J`, the gate follows immediately:

\[
D-2 < D \le 2^J < 2^{J+1}.
\]

For every Lean threshold `t`, choosing one sufficiently large `x` and the resulting pair gives the existential required by `ExchangeSupply1`.

---

### NOTE-5 — The principal declaration citations are faithful

Spot checks against the supplied Lean files sustain the Section 6 reuse table:

- `consCount` counts consecutive realizations with anchor prime in `(sqrt x,x]`;
- `consCount_lower_bound` is uniform under `HLQuantA`, the card budget, and the small-span hypothesis, with conclusions `modelMass/4 <= consCount` and `1 <= consCount`;
- `oneExtension_sum_le` explicitly requires the small-span hypothesis and its docstring states that the unrestricted form is false;
- `nuMod_insert` gives the `0`/`+1` dichotomy;
- `log_singularFactor_insert_sub_le` gives the collision/new-class one-insert log bound;
- `ExchangeAt` and `ExchangeSupply1` are represented accurately in Section 7.

The object is also correct that the supplied Lean declarations do **not** machine-check the `(K+1)`-fold two-block `rho` composition or C1’s family transfer.

---

### NOTE-6 — The `c*` necessity arithmetic is correct, within its stated route

The frozen `HLQuantA` card budget is `4 lnln x`. The base exchange rank is `(2/ln 2) lnln x`. For family density `eta=(ln x)^{-c}`, the additional truncation rank is

\[
\log_2(1/\eta)=\frac{c}{\ln2}\ln\ln x.
\]

The card headroom condition is therefore

\[
\frac2{\ln2}+\frac c{\ln2}<4
\quad\Longleftrightarrow\quad
c<4\ln2-2=0.772588\ldots.
\]

This verifies the necessity budget, not sufficiency and not a universal no-go.

---

### NOTE-7 — The repaired local formula for `rho` is algebraically correct on the admissible domain

For odd `p`, the `(1-1/p)` powers cancel because the full tuple cardinality is the sum of the two block cardinalities. The local quotient is

\[
\frac{1-\nu_H/p}
 {(1-\nu_{\rm pre}/p)(1-\nu_{\rm suf}/p)}.
\]

Since `nu_H >= max(nu_pre,nu_suf)`, it is bounded by

\[
(1-\min(\nu_{\rm pre},\nu_{\rm suf})/p)^{-1}.
\]

When both blocks occupy the same `p-1` residue classes, the factor is `p`, not merely `1+1/(p-1)`. Thus the object correctly retracts the one-insert cap as a two-block quotient bound. The exact finite T4 values remain outside the authorized corpus, as recorded in MAJOR-9.

---

# Mandatory-check disposition

| Check | Disposition |
|---|---|
| **S1 Verdict vs body** | A2 and C2 proved tags sustained. Promotions found in F18.1, F18.2/A1 consumer language, U18.6, and D3 pass rows for under-specified B2/B3/C1/A1-typ. |
| **S2 Quantifier hygiene** | A1, A2, A3, B1, and C2 are substantially pinned. A1-typ, B1′, B2, B3, C1/C1′/C1′′ require repairs. |
| **S3 Necessity vs sufficiency** | The `c*` calculation is correctly called necessary in C1, but later “closed unconditionally” / “ever fits” language exceeds the route-relative result. |
| **S4 Open-strength check** | No unflagged candidate was shown to imply frozen `HLQuantA`. B1’s non-implication is defensible because it has no absolute mass lower bound and has floor/cap escape domains, but the object only sketches this. A1-typ is openly HL-adjacent but lacks an exact statement. |
| **S5 Consumer fidelity** | PASS, subject only to the threshold-notation cleanup in MINOR-3. |
| **S6 Budget coverage** | NOT AUDITABLE from the authorized corpus; exact workpapers absent. Visible pointer omissions recorded in MAJOR-9. |
| **S7 Amendment sites** | A′′ pin, two-block `rho` correction, B3 nonempty-exception correction, and C1 n1/n2 necessity repair are coherent. The r3/U18.6 categorical “derivable” wording is not sustained. Several finite “steering-re-executed” computations are unavailable. |
| **S8 Corpus fidelity** | Lean and predecessor citations spot-checked and mostly faithful. Load-bearing exact budget computations depend on files outside the pack. |
| **S9 Unstated load-bearing steps** | The side-class density bound behind universal C1′′ obstruction is unstated; U18.6 requires an unwritten filter-regime adaptation and lower-tail proof. |

---

# Required repair set

1. Replace Section 4 B2.reduced by the exact Section 7.1 epsilon-form.
2. Quantify one fixed `C_q` in B3, or replace B3 by a fully epsilon/rate-stated alternative.
3. Write A1-typ as one complete theorem statement rather than “the same display” plus a heuristic correction.
4. Redefine C1 using an ex ante family rule with explicit `(s,x)` dependence and cap independence; declare all dependencies.
5. Add “for this recorded route” and U18.1/U18.2 qualifiers wherever the thin-class and w2 obstructions are repeated.
6. Downgrade U18.6 from “derivable” to a proposed model lemma unless the missing proof and `Par -> Par'` adaptation are supplied.
7. Display or authorize the budget workpapers before claiming full rule-15 coverage and exact finite numerical verification.
8. State and price the side-class density upper bound used by C1′′.
9. Qualify F18.5 by the `rho`-capped domain and replace “B1 is logically strongest” by a restricted-domain comparison.

After those repairs, the object’s central deliverable—a precise conditional statement layer whose selected triple implies `ExchangeSupply1`—would be support-class coherent.
