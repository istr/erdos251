# Collision-gap audit for item-0010

Date: 2026-07-22.  Pin:
`8ae6aebb72c52c505468b3abb0917c681a47d239` (verified exactly before
the audit).  Scope: target minimization and implication audit only.
Web OFF.  No existing Lean file, frozen statement, historical run,
payload, or roadmap item was changed.

Evidence labels used below are load-bearing.  `FORMAL` means proved in
the checked Lean tree.  `PROVED-DOSSIER` means a complete repository
proof at dossier grain, but no Lean supplier theorem.  `PROVED` means
finite algebra proved in this workpaper.  `MEASURED`, `HEURISTIC`,
`OPEN`, and `UNMEASURED` retain their usual repository meanings.

## A. Executive verdict

Full `B2.pairs` is substantially stronger than item-0010 needs.
For a filtered site set $`T=S'^{(s)}_x`$, write

$$
 N=\lvert T\rvert,\qquad F=\lvert\mathrm{Fam}(T)\rvert,
$$

and let $`Q=Q(x,s)`$ be the class-normalized collision statistic of
item-0020.  The exact finite criterion is

$$
 \boxed{Q<N-F.}
$$

It holds if and only if at least one realized flank class contains two
filtered sites with different middles.  Such a pair feeds the existing
`Supply.lean` clause table directly and gives an `ExchangeAt` witness.
Thus the logically weakest finite input is one scale satisfying this
strict inequality for each exchange threshold.  This criterion is so
close to the desired non-rigidity conclusion that it is not the most
useful next analytic target.

The weakest clean, non-tautological successor target found is the
following fixed collision gap on unbounded, threshold-dependent scales:

$$
 \tag{CG}
 \forall s\ \exists\eta_s\in(0,1]\ \forall X\ \exists x\ge X:
 \quad 0<N(x,s),\qquad Q(x,s)\le(1-\eta_s)N(x,s).
$$

Item-0020 already proves, for every fixed $`s`$,

$$
 \frac{F(x,s)}{N(x,s)}\longrightarrow0.
$$

Choose a favorable scale from (CG) after
$`F<\eta_sN/2`$.  Then

$$
 Q\le(1-\eta_s)N<N-F,
$$

with a positive margin at least $`\eta_sN/2`$.  Consequently one
suitable scale per threshold suffices.  Neither all sufficiently large
scales, a common subsequence, a constant uniform in $`s`$, nor one
global threshold in $`x`$ is consumed.  Once $`N(x,s)>0`$ eventually,
(CG) is equivalent to

$$
 \forall s,\qquad \liminf_{x\to\infty}\frac{Q(x,s)}{N(x,s)}<1
$$

over integer $`x`$.

The recorded $`1/64`$ pair-collision point is a convenient consequence
of the present generic `RelExtensionUpper` interface, not a logical
threshold for item-0010.  The old route needs
$`\varepsilon_{\mathrm{REU}}<\delta/2`$, hence through the square-root
reduction it needs
$`\varepsilon_{\mathrm{pair}}<(\delta/2)^2`$.  At the recorded
$`\delta=1/2`$, the resulting sufficient pair range is $`<1/16`$, while
the code/prose choice $`1/64`$ comes from the extra slack
$`\varepsilon_{\mathrm{REU}}=\delta/4=1/8`$.  Since item-0020 proves every
fixed $`\delta<1`$, a modified old interface could consume every fixed
nonnegative pair coefficient $`<1/4`$.  The direct route consumes any
fixed coefficient in $`[0,1)`$ on a suitable unbounded per-$`s`$
subsequence.

Recommendation: the next proof campaign should not target full
`B2.pairs` by default.  It should target (CG), or an explicitly modular
`RHO-ENERGY` package that implies (CG).  Before that campaign, the full
$`Q/N`$, the D0-exact admissible-middle multiplicity, and the
site-weighted rho energy should be measured.  These measurements are
diagnostics only.

## B. Exact finite lemmas

### B.1 Partition identities

Fix a finite filters-first set $`T`$.  For every realized side pair
$`P`$, let $`F_P(T)`$ be its class, $`N_P=\lvert F_P(T)\rvert`$, and let
$`N_{P,d}`$ count members with middle $`d`$.  RS.1 gives exactly

$$
 \sum_d N_{P,d}=N_P,
 \qquad
 \sum_{P\in\mathrm{Fam}(T)}N_P=N.
$$

The second identity is `card_filteredSites_eq_sum` in Lean.  The first
is definitional at dossier level but does not yet have a named Lean
theorem; a formalization should prove it by a finite fiber partition of
the realized middle image.

All denominators below are safe because a realized class is nonempty.
In Lean this is `classSites_nonempty`.

### B.2 Conditional-collision identity

Assume $`N>0`$ for the normalized and probabilistic statements below,
and put $`p_{P,d}=N_{P,d}/N_P`$.  (The unnormalized identity remains
valid for the empty set.)  For one class,

$$
\begin{aligned}
 Q_P
 &=\frac1{N_P}\sum_dN_{P,d}(N_{P,d}-1)\\
 &=\frac1{N_P}\left(\sum_dN_{P,d}^2-N_P\right)\\
 &=N_P\sum_dp_{P,d}^2-1.
\end{aligned}
$$

Therefore [PROVED]

$$
 \boxed{
 Q=\sum_PN_P\sum_dp_{P,d}^2-F
 }
$$

and

$$
 \frac QN
 =\sum_P\frac{N_P}{N}\sum_dp_{P,d}^2-\frac FN.
$$

Probabilistic interpretation: choose $`U`$ uniformly from $`T`$, then,
conditional on its side class $`P`$, choose $`V`$ uniformly and
independently from $`F_P(T)`$.  The first term is the probability that
$`U`$ and $`V`$ have the same middle.  The term $`F/N`$ is exactly the
probability that $`U=V`$.  Hence

$$
 \frac QN
 =\Pr\lbrace U\ne V\text{ and the two middles agree}\rbrace.
$$

### B.3 Exact rigidity defect

For each class,

$$
\begin{aligned}
 (N_P-1)-Q_P
 &=N_P-\frac1{N_P}\sum_dN_{P,d}^2\\
 &=\frac{N_P^2-\sum_dN_{P,d}^2}{N_P}\\
 &=\frac2{N_P}\sum_{d<e}N_{P,d}N_{P,e}.
\end{aligned}
$$

Thus [PROVED]

$$
 \boxed{
 N-F-Q
 =\sum_P\frac2{N_P}\sum_{d<e}N_{P,d}N_{P,e}\ge0.
 }
$$

The summand vanishes exactly when the class realizes one middle.
Consequently:

1. $`Q\le N-F`$ always.
2. If every realized class is middle-rigid, then exactly
   $`Q=N-F`$; no inequality loss occurs.
3. $`Q<N-F`$ if and only if some realized class contains two
   different realized middles.

This independently verifies the kickoff observation.

### B.4 Extraction of `ExchangeAt`

Suppose $`Q<N-F`$.  By B.3 choose a realized side pair $`w=(a,c)`$, two
middles $`d\ne e`$, and sites $`n,m\in F_w(T)`$ realizing them.
Then $`n\ne m`$, their prefix and suffix words agree, and their middle
gaps differ.  Because $`T`$ is the existing filters-first
`filteredSites` set, both sites already carry the near and far delta
caps and the threshold clause.

For the ambient `Par : SupplyParams` at scale $`x`$, set
$`J=Par.J(x)`$, $`K=Par.K(x)`$, and $`D=Par.D(x)`$.
The tail of `supply_of_triple` then applies verbatim:

- `length_of_mem_realizedFamily` identifies the two flank lengths;
- `mem_classSites` supplies filtered membership and `sideMatchAt`;
- `site_clauses` supplies the threshold and both cap clauses;
- `Par.one_le_J`, `Par.one_le_K` supply positive depths;
- `Par.D_le_two_pow_J` gives
  $`(D:\mathbb R)-2<2^{J+1}`$.

With the filter parameter set to the requested threshold $`s=t`$, the
site clause actually gives $`t+1\le n,m`$, stronger than the
$`t\le n,m`$ required by `ExchangeSupply1`.  The scale $`x`$ disappears
after the witness is extracted.  This proves that exactly one suitable
scale per $`t`$ is enough.  No `RelExtensionUpper` re-enters the
argument.

Evidence status: the clause-table construction is machine-checked
inside `supply_of_triple`, but no standalone non-rigid-class theorem is
exported.  Reuse requires factoring that formal proof pattern.  The
$`Q`$-to-non-rigidity algebra is `PROVED` here but not yet encoded in Lean.

## C. How much asymptotic input is needed?

### C.1 The proved sparse-family ratio

Let $`T_{s,x}=S'^{(s)}_x`$, $`N_{s,x}=\lvert T_{s,x}\rvert`$, and
$`F_{s,x}=\lvert\mathrm{Fam}(T_{s,x})\rvert`$.  Claim C1 of the item-0020
proofs gives the following ingredients at the D0 pin.

Every realized side pair is a $`(J+K)`$-tuple of positive even integers
whose side sum is inside the aggregate window.  Hence

$$
 F_{s,x}\le \mathrm{cap}_{J+K}(x)
 \le
 \left(\frac{eA'}2\frac{L}{J+K}\log{} x\right)^{J+K}
 =x^{o(1)}.
$$

This upper bound is uniform in $`s`$.  TailIntersection and the
Chebyshev inversion give, for each fixed $`s`$,

$$
 N_{s,x}\ge\frac{\pi(x)}4
 \ge\frac{x}{8C_0\log{} x}
 =x^{1-o(1)}
$$

for all sufficiently large $`x`$.  Therefore [PROVED-DOSSIER]

$$
 \tag{SF}
 \forall s\ \forall\alpha>0\ \exists X(s,\alpha)\ \forall x\ge X:
 \quad N_{s,x}>0,\qquad F_{s,x}<\alpha N_{s,x}.
$$

Only the population/TailIntersection part of $`X(s,\alpha)`$ depends
on $`s`$; the capacity-comparison threshold is $`s`$-free.  There
cannot be a useful all-$`s`$-at-one-$`x`$ statement because sufficiently
large $`s`$ empties a fixed finite scale.

`SupplyParams` is abstract in Lean and has no concrete D0 constructor.
Thus (SF), the D0 growth laws, and their analytic population inputs are
not currently formal theorems.

### C.2 W1

An all-sufficiently-large version of

$$
 Q(x,s)\le(1-\eta_s)N_{s,x}
$$

is sufficient but stronger than necessary.  The same fixed gap on
arbitrarily large scales is sufficient: choose one such scale beyond
$`X(s,\eta_s/2)`$ in (SF).

A bare assertion that there is one $`x\ge X_s`$, where $`X_s`$ is only
an unrelated existential number, is not by itself composable with the
later capacity threshold.  One isolated scale is sufficient only if
the statement explicitly places that scale beyond all population,
capacity, parameter, and threshold gates.  The unbounded formulation
(CG) is the clean way to guarantee this without baking a proof-produced
threshold into the target.

### C.3 W2 and W3

For fixed $`s`$, (SF) makes $`N_{s,x}>0`$ eventually, so the integer
sequence $`Q(x,s)/N_{s,x}`$ is eventually defined.

If its liminf is $`\ell_s<1`$, choose
$`0<\eta_s<1-\ell_s`$.  There are arbitrarily large integer scales
with $`Q/N\le1-\eta_s`$.  One can choose one after every finite
auxiliary threshold.  Thus W2 suffices.

Conversely, W3 gives a fixed $`\eta_s>0`$ on an unbounded sequence, so
the liminf is at most $`1-\eta_s<1`$.  Therefore W2 and W3 are
equivalent after eventual positivity.  Both are strictly weaker than an
all-large-$`x`$ W1 statement.

The simultaneous gates mentioned in the kickoff cause no extra
uniformity:

- the family-capacity ratio and positivity hold eventually for the
  fixed $`s`$;
- the filters and threshold $`n,m\ge t`$ are built into
  $`T_{t,x}`$;
- $`D\le2^J`$ is a `SupplyParams` property at the chosen scale;
- `ExchangeSupply1` asks for one witness, not a persistent family of
  witnesses.

### C.4 Preferred target and the exact minimum

The preferred proof-campaign statement is the finite-quantifier form
(CG), named provisionally:

`CollisionGapAlongScales` [OPEN]:

$$
 \forall s\in\mathbb N\ \exists\eta_s\in\mathbb R:
 0<\eta_s\le1\ \wedge\
 \forall X\in\mathbb N\ \exists x\in\mathbb N:
 X\le x,\ 0<N_{s,x},\
 Q(x,s)\le(1-\eta_s)N_{s,x}.
$$

Its constants may depend on $`s`$; its favorable scales may depend on
both $`s`$ and $`X`$.  It is entirely in the existing RS.1/D0
vocabulary and, together with the already proved (SF), implies
`ExchangeSupply1` directly.

The logically weaker exact interface is

`CollisionDeficitSupply`:

$$
 \forall t\ \exists x:\qquad
 Q(x,t)<N_{t,x}-F_{t,x}.
$$

This is equivalent to supplying one non-rigid filtered class per
threshold.  It is the right minimal Lean core, but nearly restates the
combinatorial conclusion and is therefore not the recommended analytic
campaign target.

## D. Direct route versus `supply_of_triple`

The present route is

$$
 \texttt{MatchedFlankLower}+\texttt{RelExtensionUpper}
 +\texttt{TailIntersection}
 \Longrightarrow\texttt{ExchangeSupply1}.
$$

The proposed route is

$$
 \texttt{SparseFlankFamily}+\texttt{CollisionGapAlongScales}
 \Longrightarrow\texttt{CollisionDeficitSupply}
 \Longrightarrow\texttt{ExchangeSupply1}.
$$

The hypotheses actually consumed are different:

| Question | Existing triple | Direct collision route |
| --- | --- | --- |
| MatchedFlankLower needed? | Yes, by the old pigeonhole | No |
| RelExtensionUpper needed? | Yes | No |
| TailIntersection needed? | Supplies positivity and old population | Only upstream in the proved derivation of (SF) |
| Population input at integration time | $`N\ge1`$ | The strict sparse-family inequality, which already forces $`N>0`$ |
| Uniform constant in $`s`$? | The Prop carries one $`\delta`$ | No; $`\eta_s`$ may depend on $`s`$ |
| All large scales? | Props are stated that way | No; one unbounded favorable subsequence per $`s`$ |
| Scales consumed per threshold | One | One |

Eventual nonemptiness alone does not imply $`F/N\to0`$.  The load-bearing
replacement for full TailIntersection is the population lower bound
dominating the $`x^{o(1)}`$ family capacity, packaged as (SF).  Once
(SF) is available, neither the full TailIntersection Prop nor
MatchedFlankLower appears in the direct integrator.

## E. Quantifier table

| Statement | Exact useful quantifiers | Size demanded | Uniformity retained/dropped |
| --- | --- | --- | --- |
| Current `B2.pairs` | $`\forall\varepsilon>0\ \exists X(\varepsilon)\ \forall x\ge X\ \forall s`$ | $`Q\le\varepsilon N`$ | threshold uniform in $`s`$; all large $`x`$; ratio tends to zero |
| Current `RelExtensionUpper` | $`\forall\varepsilon>0\ \exists X(\varepsilon)\ \forall x\ge X\ \forall s\ \forall d_P`$ satisfying the realized-family even, $`\ge2`$, and window restrictions | selected reduced mass $`\le\varepsilon N`$ | adversarial restricted selections; same strong $`s,x`$ uniformity |
| Preferred (CG) | $`\forall s\ \exists\eta_s>0\ \forall X\ \exists x\ge X`$ | $`Q\le(1-\eta_s)N`$ | no $`s`$-uniform gap; only unbounded scales; no selection |
| Exact finite deficit | $`\forall t\ \exists x`$ after the D0 gates | $`Q<N-F`$ | no asymptotic uniformity at all |
| `ExchangeSupply1` | $`\forall t\ \exists n,m,J,K,D`$ | one non-rigid filtered class | no scale appears in the conclusion |

The proposed target neither states nor implies `HLQuantA`, and it drops
rather than adds tuple-wise uniformity.  A proof may still need a new
prime-distribution carrier; weakening the endpoint does not manufacture
one.

## F. Constant ledger

### F.1 Old route

Under complete rigidity the `supply_of_triple` lower chain is

$$
 \sum_P(N_P-1)
 \ge\sum_{P\in\mathrm{Fam}_2}(N_P-1)
 \ge\frac12\sum_{P\in\mathrm{Fam}_2}N_P
 \ge\frac\delta2N.
$$

The factor $`1/2`$ is sharp for an interface that knows only the
multi-class site mass: size-two classes attain it.  Therefore the sharp
strict comparison is

$$
 \boxed{\varepsilon_{\mathrm{REU}}<\delta/2.}
$$

Equality gives no contradiction.  The present Lean proof asks
`RelExtensionUpper` for $`\delta/4`$, a convenient interior point.

Claim C3 of item-0020 gives

$$
 \sum_P(N_{P,d_P}-1)_+\le\sqrt{NQ}.
$$

Thus a fixed pair coefficient $`c\ge0`$, with $`Q\le cN`$, closes this old
interface whenever

$$
 \boxed{c<(\delta/2)^2.}
$$

The repository classifications are:

| Quantity | Value/range | Status |
| --- | --- | --- |
| Recorded MFL constant | $`\delta=1/2`$ | PROVED-DOSSIER |
| Stronger MFL family | every fixed $`0<\delta<1`$ eventually | PROVED-DOSSIER; not exposed by a Lean supplier |
| Current REU consumption | $`1/8=\delta/4`$ | convenient slack in the formal integrator |
| Current pair point | $`1/64=(1/8)^2`$ | proved consumption arithmetic through C3; `B2.pairs` itself remains OPEN |
| Strict old-route sufficient range at $`\delta=1/2`$ | $`\varepsilon_{\mathrm{REU}}<1/4`$, $`0\le c<1/16`$ | conditional PROVED implication through C3; not the current Prop shape for a lone fixed $`c`$ |
| Range using all fixed $`\delta<1`$ | every fixed $`0\le c<1/4`$ | conditional PROVED implication using dossier-proved MFL after choosing $`2\sqrt c<\delta<1`$; interface change required |

The stronger MFL quantifier used in the final row is exact: for every
rational $`0<\delta<1`$ and every $`s`$, there is $`X(\delta,s)`$ such that
for all $`x\ge X(\delta,s)`$ the multi-class site mass is at least
$`\delta N`$.  One may take
$`X=\max\lbrace x_7(s),x_0(C_0),x_{\mathrm{cap}}(\delta)\rbrace`$, with
$`x_{\mathrm{cap}}(\delta)`$ independent of $`s`$.  Claim C3's threshold map
is $`x_4(\varepsilon)=x_8(\varepsilon^2)`$.  It is uniform in $`s`$ for
all $`x\ge x_4`$, and the dossier reduction handles unrestricted
selections (hence the formally restricted ones).  The current
`RelExtensionUpper` Prop requires all positive epsilons, and
`supply_of_triple` asks for $`\delta/4`$.  A lone fixed-$`c`$ theorem does
not inhabit that interface without changing or adding a theorem.

### F.2 Direct route

At a finite scale the sharp normalized threshold is

$$
 \frac QN<1-\frac FN.
$$

Since $`F/N\to0`$ for each fixed $`s`$, every fixed coefficient
$`0\le c_s<1`$ on unbounded scales is sufficient.  Equivalently, any
$`\eta_s=1-c_s>0`$ in (CG) works.  No constant uniform in $`s`$ is
needed.

## G. Successor targets

### G.1 Preferred weak collision target

Adopt `CollisionGapAlongScales` in the exact form (CG) of C.4.  Its
direct implication is:

$$
 \texttt{SparseFlankFamily}\wedge\texttt{CollisionGapAlongScales}
 \Longrightarrow\texttt{ExchangeSupply1}.
$$

Proof: for a requested $`t`$, take the $`\eta_t`$ supplied by (CG),
take the (SF) threshold for $`\alpha=\eta_t/2`$, choose a favorable
scale beyond it, apply B.3, and reuse B.4.  Every dependency and
quantifier has now been displayed.

This target is weaker than `B2.pairs` in all of the relevant ways:
the normalized collision need only stay below one, the constant may
depend on $`s`$, and the estimate is needed only along unbounded scales.

### G.2 `RHO-ENERGY` intermediate

Define the site-mass-weighted rho energy, over realized middles, by

$$
 R_\rho(x,s)=\sum_{P,d}N_{P,d}\rho(P,d).
$$

The weakest exact form of this modular architecture that implies (CG)
uses the following two open statements.

`RhoPairTransfer` [OPEN prime-distribution input].  For every fixed
$`s`$, there are a finite $`C_s>0`$ and a nonnegative error profile
$`e_s(x)`$ such that, for all sufficiently large $`x`$,

$$
 \tag{RE1}
 \frac{Q(x,s)}{N(x,s)}\le
 C_s\frac{R_\rho(x,s)}{N(x,s)\log{} x}+e_s(x)
$$

`RhoCombinedGap` [OPEN combined strict-margin input].  For every fixed $`s`$,

$$
 \tag{RE2}
 \liminf_{x\to\infty}\left(
 C_s\frac{R_\rho(x,s)}{N(x,s)\log{} x}+e_s(x)
 \right)<1.
$$

The strict combined inequality supplies a fixed margin on an unbounded
subsequence, so (RE1)-(RE2) imply (CG).  A cleaner, stronger, and more
usefully separable campaign target is `RhoPairTransfer0`, requiring
$`e_s(x)\to0`$, together with `RhoMassGap`, requiring
$`\liminf R_\rho/(N\log{} x)<1/C_s`$.  Taking one D0-only constant
$`C_s=C`$ is cleaner still, but is not consumed by item-0010.  Likewise,
$`R_\rho/N=o_s(\log{} x)`$ would recover a vanishing collision ratio and
is more than item-0010 needs.

The two proof inputs are genuinely separate:

- (RE1) is an averaged relative factorial-moment, pair-to-rho upper
  bound.  It is new.  A direct union-sieve proof counts a rank-$`2k`$
  union and hits F20.3; a class-relative proof needs an NI-M2-type
  carrier; a dispersion proof needs NI-M4.
- `RhoMassGap` controls how much realized site mass lies on CRT-aligned,
  high-rho configurations.  Item-0019 measured strong alignment
  selection at fixed rows but did not measure this D0-coupled
  asymptotic quantity.

This package is not merely NI-M5a/NI-M5b as a statement.  If one proves
it by splitting at an ex-ante rho cap and applying the pointwise bound

$$
 N_{P,d}\le\frac{C\rho(P,d)}{\log{} x}N_P+1,
$$

then multiplication by $`N_{P,d}/N_P`$ and summation gives (RE1) on the
capped family, while exceptional site mass bounds its contribution to
$`e_s`$.  This is the NI-M5a plus NI-M5b proof route.  Current NI-M5a
only gives exceptional mass $`\le1/8`$, hence $`e_s\le1/8+o(1)`$ rather
than $`e_s\to0`$.  Nevertheless, current NI-M5a plus NI-M5b already
imply (CG) directly: on the favorable capped family,
$`Q_{\mathrm{fav}}=o(N)`$, while the universal bound $`Q_P\le N_P`$ gives
$`Q_{\mathrm{exc}}\le N_{\mathrm{exc}}\le N/8`$ on the exceptional family, so
$`Q/N\le1/8+o(1)`$.  An extra rho-energy margin is needed only to embed
this cap-split proof into the full-global-energy (RE1)--(RE2) package;
the cleaner separated vanishing-error package needs a strengthened
NI-M5a.  Conversely, averaged (RE1) does not imply pointwise NI-M5b,
and the energy condition is not itself a preselected
exceptional-family bound.

### G.3 Class-size stratification

For dyadic $`M\ge1`$, put

$$
 \mathcal F_M=\lbrace P:M\le N_P<2M\rbrace,\qquad
 N_M=\sum_{P\in\mathcal F_M}N_P,
$$

$$
 W_{2,M}=\sum_{P\in\mathcal F_M}\sum_dN_{P,d}(N_{P,d}-1),
\qquad
 V_{2,M}=\sum_{P\in\mathcal F_M}N_P(N_P-1),
$$

and

$$
 Q_M=\sum_{P\in\mathcal F_M}
 \frac1{N_P}\sum_dN_{P,d}(N_{P,d}-1).
$$

Since $`M\le N_P\le2M-1`$, [PROVED]

$$
 \frac{W_{2,M}}{2M-1}\le Q_M\le\frac{W_{2,M}}M
$$

and

$$
 (M-1)N_M\le V_{2,M}\le(2M-2)N_M.
$$

Hence a uniform stratum estimate

$$
 W_{2,M}\le\theta V_{2,M},\qquad \theta<1/2,
$$

would give

$$
 Q_M\le\theta(2-2/M)N_M,
 \qquad Q\le2\theta N,
$$

and therefore (CG) with a fixed gap.  More generally it is enough that

$$
 \sum_M\theta_M(2-2/M)N_M\le(1-\eta)N
$$

on the favorable scales.

Stratification does expose the F20.2 counterexample: rigid size-two
classes can no longer hide behind one much larger spread class in a
different stratum.  Within the size-two stratum their pair ratio is one
and the proposed estimate visibly fails.  But this does not create a
new proof device.  The quantity $`\sum_M W_{2,M}/M`$ is already $`Q`$
within a factor two, and the obvious sieve estimate for $`W_{2,M}`$
still counts rank-$`2k`$ unions and hits F20.3.

Verdict: **useful only as an empirical diagnostic**; redundant as a
standalone proof mechanism.  No stratified target is recommended beside
(CG) and (RE1)-(RE2).

## H. Admissible-middle multiplicity

### H.1 Exact D0 definition

For $`P=(a,c)`$, write

$$
 A_J=\sum_{i=1}^J a_i,\qquad C_K=\sum_{i=1}^K c_i,
 \qquad W(x)=A'L(x)\log{} x.
$$

The D0-exact prospective middle multiplicity is

$$
 A_P(x)=
 \left\lvert
 \left\lbrace d\in\mathbb N:
 \substack{d\text{ is even},\ d\ge2 \cr
 A_J+d+C_K\le W(x) \cr
 H(a,d,c)\text{ is admissible}}
 \right\rbrace
 \right\rvert.
$$

The residual allowance
$`d\le W(x)-A_J-C_K`$ is load-bearing.  The crude global bound
$`d\le W(x)`$, although sufficient for the existing REU selection
restriction, defines a different object.  The two delta caps should not
be folded into $`A_P`$: they are filters-first site conditions and are
not determined by the finite side pair and prospective middle alone.

U18.7 used the different small-span budget
$`\kappa(k-1)\log{}(k+1)`$.  Its balanced $`k=24`$ example with one
admissible middle is an exact finite audit datum recorded inside the
U18.7 `UNVERIFIED` register.  It is audit-computed/recorded, not an
asymptotic theorem and not a measurement of the D0 quantity above.
Balanced growing-rank multiplicity remains `OPEN`.

### H.2 Finite-anchor qualification

The requested sentence "every realized middle is admissible" is not
literally true at the first few prime anchors.  If a $`k`$-point tuple
$`H`$ is inadmissible, some prime $`p\le k`$ is covered in every residue
class.  A translate on which every point is prime must then contain the
prime $`p`$ itself.  In particular an inadmissible tuple cannot be
prime-realized once its base prime exceeds $`k`$.

Thus at most $`O(\pi(k))`$ initial sites are exceptional.  On the
late-anchor set every realized middle belongs to the admissible set in
H.1.  For an exact finite statement one may either remove and record
those sites or define

$$
 \widetilde A_P=A_P+
 \left\lvert\left\lbrace\text{distinct exceptional realized middles in }P\right\rbrace\right\rvert.
$$

This qualification is asymptotically harmless but must not be hidden in
an exact identity.  Removing one site changes only one class
contribution to $`Q`$; the class formula gives an absolute change at most
two.  Removing all $`O(\pi(k))`$ early sites therefore changes $`Q`$ by
$`O(\pi(k))`$, while changing $`N`$ and $`F`$ by at most the same order.
At the D0 depths, for each fixed $`s`$,
$`O(\pi(k(x)))/N(x,s)\to0`$.

### H.3 Consequences

Away from the finite exceptions, if $`r_P`$ is the realized middle
support size, then

$$
 r_P\le A_P,
 \qquad
 \sum_dp_{P,d}^2\ge\frac1{r_P}\ge\frac1{A_P}
$$

by Cauchy-Schwarz.  With $`\widetilde A_P`$, the same statement is exact
on the full finite set.  Therefore

$$
 \frac QN+\frac FN
 =\sum_P\frac{N_P}{N}\sum_dp_{P,d}^2
 \ge
 \sum_P\frac{N_P}{N\widetilde A_P}.
$$

This is a necessary-condition audit, not an upper bound.  On the full
finite set, `B2.pairs` together with $`F/N\to0`$ would force the
site-mass-weighted inverse $`\widetilde A_P`$ to tend to zero.  After
deleting the $`o(N)`$ early sites, the same conclusion applies to the
late-anchor $`A_P`$ distribution.  Thus bounded-$`A_P`$ late mass, and
especially late $`A_P=1`$ mass, would have to vanish.  The weaker
collision gap only requires a positive amount of non-rigid behavior;
it does not require admissible support to grow without bound on almost
all site mass.

The D0 distribution of $`A_P`$ is `UNMEASURED`.  Measuring it is
mandatory before another broad proof campaign, because it can refute
the plausibility of full `B2.pairs` at the statement level or identify
the exact mass on which a weaker gap could live.

## I. Barrier audit

For F20.2, the repository's recorded configuration `C(t)` refutes the
REU inference but has $`Q/N=1/3`$, so it does not itself refute (CG).
The analogous implication to (CG) is nevertheless false.  For
$`u\to\infty`$, take $`u^4`$ rigid classes, each of size $`u^4`$, and one
all-distinct class of size $`u^7`$.  Then [PROVED]
$`W_2/V_2\to0`$ while
$`Q/N=(u^8-u^4)/(u^8+u^7)\to1`$.  Thus an unnormalized global pair
ratio still cannot supply (CG); class normalization or equivalent
stratum control remains load-bearing.

| Barrier | Effect on the proposed target | Evidence status |
| --- | --- | --- |
| F20.1 pair-versus-site mismatch | Raw $`W_2=o(N)`$ remains false.  Class normalization in $`Q`$ avoids that mismatch. | PROVED-DOSSIER |
| F20.2 class-size skew | The recorded `C(t)` refutes REU; the displayed $`u`$-family separately proves that unnormalized $`W_2/V_2`$ does not imply (CG). | `C(t)`: PROVED-DOSSIER; displayed $`u`$-family: PROVED |
| F20.3 rank-$`2k`$ union sieve | Weakening the endpoint does not repair this route: a direct union-sieve proof of $`Q`$, $`W_{2,M}`$, or (RE1) still pays the superpolylogarithmic rank-$`2k`$ cost. | PROVED-DOSSIER route arithmetic; route-specific |
| F20.4 missing class carrier | Relative Selberg still needs NI-M2.  A weaker genuinely averaged carrier is not ruled out, but none is in the corpus. | Recorded obstruction |
| F20.5 word-grain mean value | The recorded dispersion architecture still needs NI-M4. | Recorded obstruction |
| F20.6 signed weights | Word-rank systems hit F17.9; class-only systems are middle-blind; one-extension systems merge into NI-M2. | PROVED-DOSSIER cost for the recorded routes; merge taxonomy RECORDED |
| F20.7 smooth-model barrier | (CG) is false in the model, so every proof needs an input outside the named tool list (T) that fails there. | PROVED-DOSSIER relative to (T); U20.4 inventory and U20.5 write-out qualifications retained |

For F20.7, Claim C4 gives in the even-Cramer-smooth gap system

$$
 Q(x,0)\ge(1-o(1))N(x,0).
$$

The universal bound from B.3 gives $`Q\le N-F\le N`$, so

$$
 \frac{Q(x,0)}{N(x,0)}\longrightarrow1.
$$

Thus W1 with a fixed gap, W2, W3, and (CG) all fail already at
$`s=0`$.  The target is weaker than `B2.pairs`, but it is not an
identity-layer consequence.  At least one member of any sufficient
`RHO-ENERGY` package must fail in this model; (RE1)'s middle-sensitive
prime-distribution comparison is the intended model-failing input.

This is a located obstruction relative to the named list (T), not an
impossibility theorem.  The assertion that (T) exhausts the current
program's unconditional inputs remains the U20.4 inventory claim.

## J. Executor follow-up measurement specification

Do not execute this campaign without a later ratified dispatch.  Its
purpose is finite-scale calibration only; no row may be promoted to an
asymptotic constant or proof.

Use the exact D0-coupled parameter map as the primary ladder.  Fixed
sub-frontier rows may be retained only as separately labeled continuity
diagnostics.  For every scale report:

1. **Full collision statistic.**  Compute in exact rational arithmetic
   $`Q/N`$, $`F/N`$, and the rigidity margin $`(N-F-Q)/N`$.  This must use
   every class and the full pair statistic, not only item-0019's
   all-`Fam_2` reduced-max statistic, which was size-two dominated.
2. **Class-size strata.**  For each predeclared dyadic $`M`$, report
   $`N_M/N`$, $`W_{2,M}`$, $`V_{2,M}`$, $`Q_M/N`$, and the rigid versus
   non-rigid site mass.  Verify the inequalities of G.3 exactly as a
   table integrity check.
3. **Admissible-middle multiplicity.**  Compute $`A_P(x)`$ using the
   residual allowance $`A_J+d+C_K\le W(x)`$, not a global $`d`$ cap.
   Use directed/high-precision comparison at the real boundary.  Test
   admissibility only for the necessary primes $`p\le k`$, and isolate
   base-prime-$`\le k`$ exceptions rather than silently classifying them.
   Report the late-anchor site-mass distribution of $`A_P`$, the site
   mass of classes contaminated by an initial exception, and
   $`\sum_PN_P/(N\widetilde A_P)`$ on the full set.
4. **Full rho energy.**  Extend item-0019 m3 beyond `Fam_2` and compute
   $`N^{-1}\sum_{P,d}N_{P,d}\rho(P,d)`$, with the same exact local
   factors and certified tail intervals.  Report how much energy comes
   from inadmissibility exceptions/off-domain cells separately.
5. **Contribution correlations.**  For each cell use its actual
   contribution
   $`N_{P,d}(N_{P,d}-1)/N_P`$.  Correlate class/cell contributions to
   $`Q`$ with $`N_P`$, the dyadic stratum, $`A_P`$, and $`\rho(P,d)`$.
   Report both site-mass-weighted and unweighted summaries.
6. **CRT-alignment strata.**  Predeclare small-prime profiles at least
   for $`p=3,5,7,11,13`$, recording
   $`(\nu_H,\nu_{\mathrm{pre}},\nu_{\mathrm{suf}})`$, their site mass, rho energy,
   and contribution to $`Q`$.  Do not define a favorable family after
   inspecting the collision outcome.

Item-0019 presently supplies only finite-scale direction: max
$`N_P=4`$, an $`N_P=2`$-dominated collision analogue around $`0.24`$ on
the live $`10^9`$ rows, and rho censuses on `Fam_2` showing alignment
selection.  Those `MEASURED` facts neither establish nor refute (CG) on
the D0-coupled asymptotic map.

## K. Optional Lean-shape sketch (no implementation)

No existing Lean file should be edited until the statement layer is
separately dispatched.  A minimal sketch is:

```text
def realizedMiddles (P : SupplyParams) (w : SidePair) (s x : Nat) :
    Finset Nat :=
  (classSites P w.1 w.2 s x).image
    (fun n => gap (n + w.1.length))

def collisionMass (P : SupplyParams) (s x : Nat) : Rat :=
  sum over w in realizedFamily P s x of
    (sum over d in realizedMiddles P w s x of
      ((Nwd * (Nwd - 1 : Nat) : Nat) : Rat)) / (Nw : Rat)

def CollisionDeficitSupply (P : SupplyParams) : Prop :=
  forall t, exists x,
    collisionMass P t x <
      ((filteredSites P t x).card : Rat) -
        ((realizedFamily P t x).card : Rat)

theorem collision_deficit_supply
    (P : SupplyParams) (h : CollisionDeficitSupply P) :
    ExchangeSupply1 := by
  -- finite collision identity -> a non-rigid realized class
  -- reuse the existing supply_of_triple clause table
```

This is Lean-shaped pseudocode, not accepted syntax.  Here `Rat` stands
for Lean's rational type; `Nw` and `Nwd` abbreviate `classCount` and
`classCountMid`; and `Nwd - 1` is Nat subtraction before the cast.  A
real implementation must spell out the finite sums and casts.  A
site-expanded equivalent

$$
 \sum_P\frac1{N_P}\sum_{n\in F_P}
   (N_{P,\mathrm{mid}(n)}-1)
$$

may be easier to formalize because it avoids first proving a separate
finite support enumeration.

New finite combinatorial lemmas required:

1. the realized-middle fibers partition `classSites`, hence
   $`\sum_d N_{P,d}=N_P`$;
2. realized-class denominators are positive;
3. the class defect identity of B.3;
4. positive total defect yields $`w,n,m`$ in one class with distinct
   middle gaps.

All analytic content may remain in named Props.  A W3 wrapper would add

```lean
FamilySparse P
CollisionGapAlongScales P
```

and prove that their conjunction implies `CollisionDeficitSupply P`.
The exact core theorem itself needs neither `MatchedFlankLower`,
`RelExtensionUpper`, nor `TailIntersection`.

The clause-table half should be factored from the existing
`supply_of_triple` proof rather than duplicated: it already uses
`length_of_mem_realizedFamily`, `mem_classSites`, `site_clauses`, and
the three `SupplyParams` laws in precisely the needed shapes.  Expected
axiom footprint: unchanged classical three.  No analytic assertion
needs to become a theorem in this module; it may remain a named Prop
supplier, following the current statement-layer pattern.

## L. Final target decision

The audit supports the following execution order for the mathematical
frontier:

1. Measure the full statistic, $`A_P`$, rho energy, and alignment strata
   under a separately ratified finite campaign.
2. Target `CollisionGapAlongScales`, not full `B2.pairs`, unless the
   measurement and a new proof carrier specifically support the
   stronger statement.
3. Prefer a modular `RHO-ENERGY` proof only if both the averaged
   pair-to-rho comparison and the separate CRT-alignment mass estimate
   have credible proof surfaces.
4. Treat class-size stratification as a diagnostic, not a new proof
   mechanism.

No stop condition of the kickoff fired: the rigidity identity is exact;
the sparse-family ratio has the required per-threshold strength; one
scale per threshold is exactly what `ExchangeSupply1` consumes; and the
direct implication does not use `RelExtensionUpper`.  The only requested
elementary assertion requiring correction is the finite-anchor version
of "every realized middle is admissible"; H.2 records the exact
qualification rather than silently strengthening it.
