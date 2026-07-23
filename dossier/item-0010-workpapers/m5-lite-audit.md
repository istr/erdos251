# M5-lite statement and budget audit for item-0010

Date: 2026-07-23. Pin:
`9b993ced7627f803493e9df0564785a5e99af19a` (verified exactly before
the audit). Scope: statement minimization and budget arithmetic only.
Web OFF. No empirical campaign, literature search, Lean edit, or
roadmap edit was made.

Evidence labels are load-bearing. `FORMAL` means proved in the checked
Lean tree. `PROVED-DOSSIER` means proved in the repository at dossier
grain. `PROVED` means finite algebra proved in this workpaper. `OPEN`,
`MEASURED`, `HEURISTIC`, and `RECORDED` retain the repository meanings.

Repository inputs audited in full:
`dossier/item-0010-workpapers/collision-gap-audit.md`,
`dossier/relext-upper.md`, `dossier/relext-statements.md`,
`dossier/item-0020-workpapers/mechanism-inventory.md`,
`lean/Erdos251/Supply.lean`, `lean/Erdos251/Exchange.lean`, and
`ledger.yaml`, especially `ANN-20260722-58`.

## A. Executive verdict

The proposed M5-lite implication is correct [PROVED]. For a realized
side class $`P`$, if

$$
 N_{P,d}\le \lambda N_P+1,\qquad 0\le\lambda<1,
$$

for every repeated realized middle, then

$$
 Q_P=\frac1{N_P}\sum_dN_{P,d}(N_{P,d}-1)
 \le\lambda N_P.
$$

For an ex ante favorable family $`\mathcal G`$, the clean linear
global budget is

$$
 Q\le N-(1-\lambda)N_{\mathcal G}-F_{\mathrm{exc}},
 \qquad
 \alpha>0,\quad N_{\mathcal G}\ge\alpha N
 \Longrightarrow
 \boxed{\eta=(1-\lambda)\alpha}.
$$

It retains the sharp universal complement slack; B.2 records the
still sharper integer-packing envelope on favorable classes.

The weakest useful M5-shaped form found is not the two-constant form
but an ex ante site-weighted contraction budget. A predeclared
selector and coefficient profile assign a classwise saving
$`\kappa_P\in[0,1]`$ without inspecting the realized middle histogram.
It is enough, on unbounded scales for each fixed $`s`$, that

$$
 N_{P,d}\le(1-\kappa_P)N_P+1
 \quad\text{and}\quad
 \sum_{P\in\mathcal G}\kappa_PN_P\ge\eta_sN.
$$

This named statement implies `CollisionGapAlongScales` with the same
$`\eta_s`$. Its uniform $`(\alpha,\lambda)`$ specialization is
cleaner but quantitatively stronger; thresholding a predeclared
weighted profile recovers a uniform positive-mass subfamily with a
constant loss. Direct Gini defect is mathematically weaker but nearly
restates the consumer. Singleton-inert majority escape is therefore
kept as the principal measurement companion, not the selected proof
surface.

NI-M5a and NI-M5b are substantially stronger. They give
$`\alpha=7/8`$, $`c(x)=C_q(x)/\log{} x\to0`$, and

$$
 \frac QN\le\frac18+\frac78c(x)
 =\frac18+o(1).
$$

After the threshold where $`c(x)\le1/2`$, they give
$`\eta=7/16`$, and eventually every fixed
$`0<\eta<7/8`$. M5-lite needs only a positive weighted margin,
permits $`s`$-dependent constants, and needs only unbounded favorable
scales.

The rho cap $`R=o(\log{} x)`$ is not logically required. It is one
old proof device for forcing $`\lambda(x)\to0`$. A larger rho regime
could be admissible if another argument still proves a fixed
contraction below one; no such argument is proved here.

Next measurement should map, for predeclared selectors, the joint
frontier of declared-profile validity, favorable site mass, majority
escape, and Gini defect while retaining the prior full diagnostics.
Next proof work should target the weighted statement, or its uniform
specialization, using an input outside the recorded model-blind list
that fails in the even-Cramer-smooth barrier model.

## B. Exact finite lemmas

### B.1 Setup and arithmetic domain

Fix a finite filtered site set $`T`$. Let

$$
 N=\lvert T\rvert,\qquad
 F=\lvert\mathrm{Fam}(T)\rvert.
$$

For a realized side class $`P`$, put

$$
 n=N_P\ge1,\qquad a_d=N_{P,d},\qquad
 \sum_da_d=n,
$$

and

$$
 Q_P=\frac1n\sum_da_d(a_d-1),\qquad Q=\sum_PQ_P.
$$

In the Lean-facing reading, $`a_d-1`$ is Nat subtraction before the
cast. This creates no discrepancy:

- if $`a_d=0`$, the summand is zero;
- if $`a_d=1`$, the summand is zero;
- if $`a_d\ge2`$, Nat subtraction agrees with integer and real
  subtraction.

Therefore the logically weakest domain for a classwise contraction
hypothesis is the set of repeated realized middles
$`d`$ with $`N_{P,d}\ge2`$. Quantifying over all realized middles is
cleaner and equivalent for the estimate. Provided every realized
middle lies in the prospective D0 window, quantifying over that whole
window is also logically equivalent for the bare inequality: zero and
singleton cells satisfy it automatically when $`\lambda\ge0`$. It is
a broader proof-interface domain, not a stronger finite numerical
hypothesis, and the consumer does not need it.

### B.2 Classwise M5-lite inequality

Assume $`0\le\lambda<1`$ and

$$
 a_d\le\lambda n+1
$$

for every repeated realized $`d`$. Then

$$
 a_d-1\le\lambda n
$$

on every nonzero summand. Multiplication by $`a_d\ge0`$ gives

$$
 a_d(a_d-1)\le\lambda n a_d.
$$

Summing and using $`\sum_da_d=n`$ proves [PROVED]

$$
 \boxed{Q_P\le\lambda n.}
$$

The additive $`+1`$ is exactly aligned with the reduced factorial
moment: it is removed by $`a_d-1`$. It is also the largest
scale-independent real additive slack that guarantees this same
bound for every real $`\lambda\in[0,1)`$ and integer class data. Any
larger fixed slack admits choices where an integer cell crosses the
$`\lambda n+1`$ boundary and the displayed conclusion fails.
Explicitly, for a proposed slack $`c>1`$, choose
$`t\in(1,c]`$, an integer $`n>t`$, and
$`\lambda=1-t/n`$. A single rigid cell $`a=n`$ obeys
$`a=\lambda n+t\le\lambda n+c`$, while
$`Q_P=n-1>\lambda n=n-t`$.

Singleton classes cause no exception. For $`n=1`$, the unique
realized cell has size one, so $`Q_P=0\le\lambda`$.

There is harmless integer slack. Since
$`a_d-1\le\lfloor\lambda n\rfloor`$ on every contributing cell,

$$
 Q_P\le\lfloor\lambda n\rfloor\le\lambda n.
$$

The sharp finite envelope from this hypothesis alone is stronger.
Put

$$
 1\le b=\min\left(n,\lfloor\lambda n+1\rfloor\right)\le n,
 \qquad n=qb+r,\qquad 0\le r<b.
$$

The cell cap is $`b`$, and convexity packs $`q`$ cells of size $`b`$
and, when nonzero, one cell of size $`r`$. Hence [PROVED]

$$
 \boxed{
 Q_P\le
 \frac{qb(b-1)+r(r-1)}n
 =
 b-1-\frac{r(b-r)}n.
 }
$$

This is attained by the displayed packing, so it is sharp without
additional information about the middle domain. The report uses
$`Q_P\le\lambda n`$ in the main ledger because that real linear bound
composes cleanly across classes.

### B.3 Sharp universal complement bound

For every cell, $`a_d\le n`$, hence

$$
 a_d(a_d-1)\le(n-1)a_d.
$$

After summation [PROVED],

$$
 \boxed{Q_P\le n-1<n.}
$$

The first inequality is sharp: equality holds exactly when the class
is middle-rigid. Thus, if

$$
 N_{\mathrm{exc}}=\sum_{P\notin\mathcal G}N_P
 \quad\text{and}\quad
 F_{\mathrm{exc}}=
 \lvert\mathrm{Fam}(T)\setminus\mathcal G\rvert,
$$

then

$$
 \boxed{Q_{\mathrm{exc}}\le N_{\mathrm{exc}}-F_{\mathrm{exc}}.}
$$

The extra $`F_{\mathrm{exc}}`$ is useful finite slack. It supplies a
fixed normalized gap only if $`F_{\mathrm{exc}}/N`$ itself stays
bounded below. In the present D0 regime the proved sparse-family
ratio has $`F/N\to0`$ for each fixed $`s`$, so this slack cannot be
the asymptotic source of the desired collision gap. The clean
consumer may therefore charge the complement only by
$`Q_{\mathrm{exc}}\le N_{\mathrm{exc}}`$, while retaining the sharper
formula in the ledger.

### B.4 Global uniform inequality

Under the uniform classwise contraction on $`\mathcal G`$,

$$
\begin{aligned}
 Q
 &\le\lambda N_{\mathcal G}
   +N_{\mathrm{exc}}-F_{\mathrm{exc}}\\
 &=N-(1-\lambda)N_{\mathcal G}-F_{\mathrm{exc}}\\
 &\le N-(1-\lambda)N_{\mathcal G}.
\end{aligned}
$$

If $`N>0`$ and $`N_{\mathcal G}\ge\alpha N`$, then

$$
 \boxed{
 \frac QN
 \le1-(1-\lambda)\alpha-\frac{F_{\mathrm{exc}}}{N}
 \le1-(1-\lambda)\alpha.
 }
$$

The hypotheses $`\alpha>0`$ and $`\lambda<1`$ are exactly what
guarantee a positive gap from the FM and MC terms alone. Equality in
FM or MC is harmless. A positive normalized
$`F_{\mathrm{exc}}`$ or integer-rounding term could create extra
finite slack, but the preferred asymptotic statement does not rely
on it.

### B.5 Scale-dependent constants

Let

$$
 \gamma_{s,x}=(1-\lambda_{s,x})\alpha_{s,x}.
$$

Positivity of $`\gamma_{s,x}`$ at every finite scale is not enough:
the values may tend to zero. The exact fixed-gap quantifier is

$$
\boxed{
 \forall s\ \exists\eta_s>0\ \forall X\ \exists x\ge X:
 \quad N(x,s)>0,\qquad
 \gamma_{s,x}\ge\eta_s,
}
$$

with a valid ex ante certificate at the chosen $`x`$.

If $`\mathcal U_s`$ is a pre-existing unbounded set of candidate
scales, this is equivalent to

$$
 \limsup_{\substack{x\to\infty\cr x\in\mathcal U_s}}
 \gamma_{s,x}>0.
$$

Equivalently,

$$
 \liminf_{\substack{x\to\infty\cr x\in\mathcal U_s}}
 \left(1-\gamma_{s,x}\right)<1.
$$

The kickoff's proposed condition

$$
 \limsup_{\substack{x\to\infty\cr x\in\mathcal U_s}}
 \left(1-\gamma_{s,x}\right)<1
$$

is sufficient but stronger: it says
$`\liminf\gamma_{s,x}>0`$ on the whole candidate set. It becomes
equivalent after existentially passing to a favorable subsequence.

### B.6 Class-dependent weighted contraction

Let a predeclared profile assign $`\lambda_P\in[0,1]`$ to favorable
classes, and assume

$$
 N_{P,d}\le\lambda_PN_P+1
$$

for every repeated realized middle. The value $`\lambda_P=1`$ is
allowed and records no saving. Applying B.2 class by class and B.3
on the complement gives [PROVED]

$$
 \boxed{
 Q\le
 N-\sum_{P\in\mathcal G}(1-\lambda_P)N_P-F_{\mathrm{exc}}.
 }
$$

Thus the exact averaged sufficient condition is

$$
 \boxed{
 \frac1N\sum_{P\in\mathcal G}(1-\lambda_P)N_P
 \ge\eta_s>0.
 }
$$

This is weaker in constants than committing in advance to one
$`\alpha_s`$ and one $`\lambda_s`$. At the qualitative
positive-margin level the two forms are equivalent after thresholding
an ex ante profile. Indeed, if the weighted margin is at least
$`\eta N`$, then the classes satisfying

$$
 1-\lambda_P\ge\frac\eta2
$$

carry site mass at least $`\eta N/2`$. On that subfamily one may take

$$
 \alpha=\frac\eta2,\qquad
 \lambda=1-\frac\eta2,
$$

which certifies a uniform product margin $`\eta^2/4`$.

This thresholding is analytically legitimate only when the coefficient
profile was predeclared from permitted ex ante data. Fitting
$`\lambda_P`$ after inspecting the middle histogram turns the statement
into the modal certificate of B.7 and removes most of its value as a
proof target.

### B.7 Reduced maximum and majority escape

Let

$$
 M_P=\max_{\substack{d\cr N_{P,d}>0}}N_{P,d}.
$$

Since $`N_{P,d}-1\le M_P-1`$ on every contributing cell,

$$
 \boxed{Q_P\le M_P-1.}
$$

This is sharp as a uniform simple bound; for example, equal nonzero
cells of size $`M_P`$ attain equality. A sharper envelope using only
$`N_P`$ and $`M_P`$ is available. If

$$
 N_P=q_PM_P+r_P,\qquad 0\le r_P<M_P,
$$

convexity gives

$$
 Q_P\le
 \frac{q_PM_P(M_P-1)+r_P(r_P-1)}{N_P}
 =
 M_P-1-\frac{r_P(M_P-r_P)}{N_P}.
$$

For an ex ante family $`\mathcal G`$, using the sharp universal bound
on every class gives

$$
 \boxed{
 Q\le
 N-F-\sum_{P\in\mathcal G}(N_P-M_P).
 }
$$

Therefore the singleton-inert majority-escape condition

$$
 \sum_{P\in\mathcal G}(N_P-M_P)\ge\eta_sN
$$

implies `CollisionGapAlongScales` with the same $`\eta_s`$, and in
fact gives the stronger finite estimate

$$
 Q\le(1-\eta_s)N-F.
$$

It is sufficient, not identical, at the same constant. The minimal
modal saving relative to the coarse complement charge
$`Q_P\le N_P`$ is

$$
 \sum_{P\in\mathcal G}(N_P-M_P+1).
$$

The added one per class is the self-pair or singleton slack. It makes
the modal statement closer to CG and can dominate singleton-heavy
finite rows. Majority escape deliberately deletes that artifact.

### B.8 Gini impurity and exact collision defect

Put

$$
 p_{P,d}=\frac{N_{P,d}}{N_P}
$$

and define the class defect

$$
\begin{aligned}
 D_P
 &=(N_P-1)-Q_P\\
 &=N_P\left(1-\sum_dp_{P,d}^2\right)\\
 &=\frac2{N_P}\sum_{d<e}N_{P,d}N_{P,e}.
\end{aligned}
$$

The middle expression is site mass times the Gini impurity of the
middle distribution. The collision-gap audit proved

$$
 N-F-Q=\sum_PD_P.
$$

Let $`E_P=N_P-M_P`$. The maximum bound in B.7 gives
$`D_P\ge E_P`$. Conversely,

$$
 \sum_dN_{P,d}^2\ge M_P^2,
$$

so

$$
 D_P\le
 \frac{N_P^2-M_P^2}{N_P}
 =E_P\left(1+\frac{M_P}{N_P}\right)
 \le2E_P.
$$

Hence [PROVED]

$$
 \boxed{E_P\le D_P\le2E_P.}
$$

A positive site-mass-weighted majority escape and a positive
site-mass-weighted Gini defect are therefore equivalent up to a
factor two. Direct Gini defect is mathematically closest to the
consumer and the weakest exact non-rigidity metric. It is also close
to a restatement of $`N-F-Q`$, so it does not by itself identify a
new proof mechanism.

## C. Quantifier comparison

### C.1 Recorded old M5 architecture

The following is the useful quantifier expansion of the recorded
NI-M5 lane. Both inputs remain `OPEN`.

`NI-M5a` [OPEN]: there are a predeclared rho-capped selector, a
function $`R`$ with $`R(x)=o(\log{} x)`$, and a threshold
$`X_a`$ such that

$$
 \forall x\ge X_a\ \forall s\ge0:
 \qquad
 N_{\mathrm{exc}}(x,s)\le\frac18N(x,s).
$$

Thus

$$
 N_{\mathcal G}(x,s)\ge\frac78N(x,s).
$$

`NI-M5b` [OPEN]: there are one function $`C_q`$, independent of the
class and the selection, and a threshold $`X_b`$, with

$$
 \frac{C_q(x)}{\log{} x}\longrightarrow0,
$$

such that

$$
 \forall x\ge X_b\ \forall s\ge0\
 \forall P\in\mathcal G_{s,x}\ \forall d\in\mathcal D_{s,x}(P):
 \qquad
 N_{P,d}\le
 \frac{C_q(x)}{\log{} x}N_P+1.
$$

Here $`\mathcal D_{s,x}(P)`$ is the recorded prospective even
D0-window middle domain.

The all-prospective-middle domain, the rho cap, the all-large-scale
form, and the strong $`s`$ uniformity are features of this proof
architecture. They are not consumed by the finite collision budget.

### C.2 Preferred M5-lite statement

Fix one named admissible rule which, before any middle histogram is
opened, assigns:

1. a selector
   $`\mathrm{Sel}(s,x,P)\in\lbrace0,1\rbrace`$; and
2. a contraction saving
   $`\kappa(s,x,P)\in[0,1]`$.

Let

$$
 \mathcal G_{s,x}
 =
 \lbrace P\in\mathrm{Fam}(T_{s,x}):
 \mathrm{Sel}(s,x,P)=1\rbrace.
$$

`ExAnteWeightedMiddleContractionAlongScales` [OPEN] is:

$$
\boxed{
\begin{gathered}
 \forall s\ \exists\eta_s>0\ \forall X\ \exists x\ge X:
 \quad N(x,s)>0,\\
 \forall P\in\mathcal G_{s,x}\ \forall d\
 \bigl(N_{P,d}\ge2\Longrightarrow
 N_{P,d}\le(1-\kappa(s,x,P))N_P+1\bigr),\\
 \sum_{P\in\mathcal G_{s,x}}
 \kappa(s,x,P)N_P\ge\eta_sN(x,s).
\end{gathered}
}
$$

By B.6 it implies `CollisionGapAlongScales` with the same
$`\eta_s`$.

The uniform favorable-mass specialization takes

$$
 \kappa(s,x,P)=1-\lambda_s
$$

on a family of mass at least $`\alpha_sN`$. Its gap is

$$
 \eta_s=(1-\lambda_s)\alpha_s.
$$

### C.3 Consumer chain

The exact chain is

$$
\begin{aligned}
 &\texttt{ExAnteWeightedMiddleContractionAlongScales}\\
 &\qquad\Longrightarrow
 \texttt{CollisionGapAlongScales}\\
 &\qquad+\ \texttt{SparseFlankFamily}
 \Longrightarrow
 \texttt{CollisionDeficitSupply}\\
 &\qquad\Longrightarrow
 \texttt{ExchangeSupply1}.
\end{aligned}
$$

The first implication is `PROVED` here. `SparseFlankFamily`, namely
$`F(x,s)/N(x,s)\to0`$ for each fixed $`s`$, is
`PROVED-DOSSIER`. The last implication reuses the `FORMAL`
`supply_of_triple` clause table after the finite non-rigid class is
extracted; the standalone collision-deficit wrapper is not yet Lean
formalized.

For a requested threshold $`t`$, take $`s=t`$. If CG supplies
$`\eta_t`$, first pass the sparse-family threshold

$$
 F(x,t)<\frac{\eta_t}{2}N(x,t),
$$

then choose one favorable CG scale beyond it. At that scale,

$$
 Q\le(1-\eta_t)N<N-F.
$$

The strict inequality follows with room at least
$`\eta_tN/2`$. One scale per threshold is exactly what
`ExchangeSupply1` consumes.

### C.4 Side-by-side quantifiers

| Statement | Useful quantifier shape | Constant or size | Uniformity |
| --- | --- | --- | --- |
| NI-M5a [OPEN] | One predeclared capped rule; all sufficiently large $`x`$ in the old interface | $`N_{\mathrm{exc}}\le N/8`$, hence $`\alpha=7/8`$ | Strong old $`s`$ uniformity |
| NI-M5b [OPEN] | All sufficiently large $`x`$; every favorable $`P`$ and every prospective relevant $`d`$ | $`\lambda(x)=C_q(x)/\log{} x\to0`$ | One rate, classwise and selection-uniform |
| Preferred M5-lite [OPEN] | $`\forall s\ \exists\eta_s>0\ \forall X\ \exists x\ge X`$ | Weighted ex ante saving at least $`\eta_sN`$ | Constants and scales may depend on $`s`$ |
| `CollisionGapAlongScales` [OPEN] | $`\forall s\ \exists\eta_s>0\ \forall X\ \exists x\ge X`$ | $`N>0`$ and $`Q\le(1-\eta_s)N`$ | No common subsequence or global threshold |
| `CollisionDeficitSupply` [PROPOSED CORE] | $`\forall t\ \exists x`$ beyond the D0 gates | $`Q(x,t)<N(x,t)-F(x,t)`$ | One scale per threshold |
| `ExchangeSupply1` [NAMED PROP] | $`\forall t\ \exists n,m,J,K,D`$ | One `ExchangeAt` witness and the gate | No scale remains in the conclusion |

Neither MFL nor REU is consumed by the direct collision route at
integration time.

## D. Constant and budget ledger

### D.1 Old-to-new implication

Set

$$
 c(x)=\frac{C_q(x)}{\log{} x}.
$$

NI-M5a gives $`\alpha=7/8`$ and NI-M5b gives $`c(x)\to0`$. On the
sufficiently large scales where $`0\le c(x)\le1`$, the clean linear
split, retaining the sharp complement term, is

$$
\begin{aligned}
 \frac QN
 &\le
 c(x)\frac{N_{\mathcal G}}N
 +\frac{N_{\mathrm{exc}}}N
 -\frac{F_{\mathrm{exc}}}N\\
 &\le
 \frac18+\frac78c(x)
 -\frac{F_{\mathrm{exc}}}N.
\end{aligned}
$$

Therefore

$$
 \frac QN\le\frac18+o(1).
$$

For any fixed $`\lambda_0\in(0,1)`$, choose
$`X_{\lambda_0}`$ so that

$$
 C_q(x)\le\lambda_0\log{} x
 \qquad(x\ge X_{\lambda_0}).
$$

Then M5-lite holds with

$$
 \boxed{
 \alpha=\frac78,\qquad
 \lambda=\lambda_0,\qquad
 \eta=\frac78(1-\lambda_0).
 }
$$

At $`\lambda_0=1/2`$ this gives $`\eta=7/16`$. More generally, the
old inputs eventually supply every fixed $`0<\eta<7/8`$.

### D.2 Budget sheet

| Quantity | Old M5 requirement | New uniform M5-lite | Preferred weighted form | Logical reason |
| --- | --- | --- | --- | --- |
| Favorable site mass | $`\ge7N/8`$ | $`\ge\alpha_sN`$, some $`\alpha_s>0`$ | No separate lower bound; weighted saving is $`\ge\eta_sN`$ | Only positive normalized saving is consumed |
| Exceptional site mass | $`\le N/8`$ | May be $`(1-\alpha_s)N`$ with any $`\alpha_s>0`$ | No separately assumed bound; the margin forces $`N_{\mathrm{exc}}\le(1-\eta_s)N`$ | Since $`\kappa_P\le1`$, favorable site mass is at least $`\eta_sN`$ |
| Middle coefficient | $`C_q(x)/\log{} x=o(1)`$ | Any $`\lambda_s<1`$ | Classwise $`1-\kappa_P`$ with positive weighted $`\kappa_P`$ margin | Fixed contraction suffices |
| Collision conclusion | $`Q/N\le1/8+o(1)`$ | $`Q/N\le1-(1-\lambda_s)\alpha_s`$ | $`Q/N\le1-\eta_s`$ | Direct classwise summation |
| Gap | Tends to at least $`7/8`$ in this split | $`\eta_s=(1-\lambda_s)\alpha_s>0`$ | Any fixed $`\eta_s>0`$ per $`s`$ | Exactly what CG consumes |
| Complement class slack | $`-F_{\mathrm{exc}}/N`$ available | Same | Same | Sharp $`Q_P\le N_P-1`$ |
| Uniformity in $`s`$ | Strong old interface | Not needed | Not needed | One threshold is handled at a time |
| Scales | All sufficiently large | Unbounded favorable scales | Unbounded favorable scales | One witness scale is consumed |
| Rho cap | $`R=o(\log{} x)`$ | Not in the statement | Not in the statement | It is an old proof device |
| Middle domain | Prospective even D0-window interface | Realized middles suffice | Repeated realized middles are the minimal nonredundant domain | The domains are equivalent for the bare bound because zero and singleton cells satisfy it automatically |
| Multiplicity floor | None in the stated $`+1`$ form; the sharper B1 precision form used one | Not needed | Not needed | The $`+1`$ handles integer granularity |
| D0 window | Built into $`T_{s,x}`$ | Unchanged filters-first set | Unchanged filters-first set | The consumer needs the existing clause table |
| Selector | Ex ante rho-capped family | Ex ante family | Ex ante selector and coefficient profile | Prevents outcome-conditioned circularity |

All strictness is now visible:

- $`N>0`$ is required before normalizing;
- $`\alpha_s>0`$ and $`\lambda_s<1`$ give a positive uniform gap;
- in the weighted form, $`\eta_s>0`$ is the load-bearing strict
  margin;
- an estimate with $`\eta_s=0`$ or a product margin tending to zero
  does not imply CG;
- the later sparse-family comparison must be strict,
  $`F<\eta_sN`$, and is obtained by going sufficiently far out.

## E. Barrier table

The verdicts below retain the scope and evidence classes of
F20.1--F20.7. A weaker endpoint is not promoted to a new proof route
without a new carrier.

| Barrier | M5-lite verdict | Consequence |
| --- | --- | --- |
| F20.1 pair-versus-site mismatch | The raw obstruction and the $`Q`$ normalization are `PROVED-DOSSIER`; clearance by the new site-weighted inequality is `PROVED` here. | Raw $`W_2=o(N)`$ remains false and cannot replace $`Q`$. |
| F20.2 class-size skew | Cannot break the proved implication. It does break class-count or unweighted averages [PROVED]. | The $`N_P`$ weights are load-bearing. |
| F20.3 rank-$`2k`$ union sieve | Not cleared for the recorded route [PROVED-DOSSIER route arithmetic]. Fixed contraction replaces a vanishing coefficient by a coefficient below one, but the union-sieve cost remains superpolylogarithmic. | The target gains at most one full $`\log{} x`$ of coefficient room; the cost $`(\log{} x)^{5.77\log{}(\log{}(\log{} x))+O(1)}`$ still exceeds it. |
| F20.4 missing class carrier | Not cleared [RECORDED]. Relative Selberg still needs NI-M2 in the recorded architecture. | A weaker one-sided or positive-mass carrier is possible in principle but absent from the corpus. |
| F20.5 word-grain mean value | Not cleared [RECORDED]. The recorded dispersion route still needs NI-M4. | A lower-moment or positive-proportion substitute is only an open possibility. |
| F20.6 signed weights | Unchanged [PROVED-DOSSIER costs; RECORDED merges]. Word-rank routes hit F17.9, class-only routes are middle-blind, and extension-only routes inherit NI-M2. | Weakening the endpoint supplies no new signed-weight carrier. |
| F20.7 smooth-model barrier | The model has $`Q/N\to1`$ [`PROVED-DOSSIER`, with U20.5 write-out debt], so the M5-lite package fails [`PROVED` here]. | Exhaustion of the current named list T is the U20.4 inventory claim, not a theorem: a new route needs an input outside T that fails in the model. |

For F20.2, site mass cannot be replaced by a favorable fraction of
classes. Take $`u`$ favorable singleton classes and one exceptional
middle-rigid class of size $`u^2`$. The favorable fraction of classes
tends to one, but

$$
 \frac{N_{\mathcal G}}N=\frac1{u+1}\longrightarrow0
$$

and

$$
 \frac QN
 =\frac{u^2-1}{u^2+u}
 =1-\frac1u
 \longrightarrow1.
$$

The present site-weighted hypotheses exclude this counterexample
exactly.

For F20.3, the concrete room gained is real but insufficient. A local
law of shape

$$
 N_{P,d}\le
 \frac{C_{\mathrm{rel}}R(x)}{\log{} x}N_P+1
$$

now needs only

$$
 \frac{C_{\mathrm{rel}}R(x)}{\log{} x}\le\lambda_s<1
$$

on the favorable scales. Conditional on a fixed
$`C_{\mathrm{rel}}`$, this arithmetic would permit
$`R(x)\sim c\log{} x`$ when $`C_{\mathrm{rel}}c<1`$. It does not
prove such a law or a positive favorable mass at that larger cap.

For F20.7, the smooth model has

$$
 \frac{Q(x,0)}{N(x,0)}\longrightarrow1.
$$

For a proposed profile, put

$$
 S=\sum_{P\in\mathcal G}\kappa_PN_P.
$$

On every model scale where its classwise contraction bounds hold,
B.6 forces

$$
 0\le\frac SN
 \le1-\frac QN-\frac{F_{\mathrm{exc}}}N
 \le1-\frac QN\longrightarrow0.
$$

Thus a sufficient weighted package fails either through its
classwise bounds or through loss of its positive margin. In the
uniform form, either the classwise bound fails or
$`(1-\lambda)N_{\mathcal G}/N\to0`$. Majority escape and Gini defect
have normalized sums tending to zero unconditionally. The proved
route-design consequence is only T-relative: an input outside the
named model-blind list T must fail in the model.
`Middle-slot distribution` is the salient target family, not a proved
logically necessary category.

## F. Preferred successor statement

### F.1 Permitted selector and profile data

The selector and coefficient profile must be named before inspecting
middle collisions. They may use:

- $`s`$, $`x`$, and the D0 values $`J`$, $`K`$, $`D`$, and the
  aggregate window;
- the side pair $`P=(a,c)`$, side spans, and other side-only data;
- predeclared small-prime CRT profiles;
- prospective singular-series, rho, or admissibility data computed
  over the full residual D0 middle domain

  $$
   \left\lbrace d\in\mathbb N:
   \substack{d\text{ even},\ d\ge2,\cr
   A_J+d+C_K\le W(x)}
   \right\rbrace,
  $$

  not over the realized support;
- predeclared class-size bins based on $`N_P`$.

Using $`N_P`$ is not logically circular. It is the side-class
marginal $`\sum_dN_{P,d}`$ and the denominator of the target
inequality, not the middle allocation. A size rule and every threshold
must nevertheless be frozen before the middle histogram is opened.
Size-based rules should be reported separately from purely
side-geometric rules because their analytic selection costs differ.

Forbidden selector or profile inputs include:

- whether a class realizes at least two middles;
- $`M_P`$, $`Q_P`$, Gini defect, or observed reduced concentration;
- all-distinct or low-collision predicates;
- a rho cap computed only on realized middles;
- caps, bins, or coefficient profiles tuned after inspecting
  $`Q`$, $`\eta_{\mathrm{cert}}`$, or the collision frontier.

A post hoc value

$$
 \lambda_P=\frac{M_P-1}{N_P}
$$

is a valid finite certificate, but it is not an ex ante analytic
predictor and may not define the preferred family or profile.

### F.2 Candidate comparison

| Candidate | Exact margin | Relation to CG | Analytic value | Measurement value |
| --- | --- | --- | --- | --- |
| H1 uniform mass and contraction | $`N_{\mathcal G}\ge\alpha_sN`$, $`N_{P,d}\le\lambda_sN_P+1`$ | Same-scale gap $`(1-\lambda_s)\alpha_s`$ | Cleanest pointwise proof target; stronger constants | Uniform maximum can be brittle |
| H2 ex ante weighted contraction | Classwise $`1-\kappa_P`$ bounds and $`\sum_{P\in\mathcal G}\kappa_PN_P\ge\eta_sN`$ with predeclared $`\kappa_P`$ | Same-scale gap $`\eta_s`$ | Best M5-shaped averaged target; tolerates controlled bad classes | Exact weighted frontier |
| H3 majority escape | $`\sum_{P\in\mathcal G}(N_P-M_P)\ge\eta_sN`$ | Gives $`Q\le(1-\eta_s)N-F`$ | Singleton-inert and concrete, but close to non-rigidity | Strong robust diagnostic |
| H4 direct Gini defect | $`\sum_{P\in\mathcal G}D_P\ge\eta_sN`$ | Exact contribution to $`N-F-Q`$ | Mathematically weakest exact defect form, but near-tautological | Exact diagnostic and integrity check |

The exact outer quantifiers are as follows. Every family is fixed by
an ex ante selector. H1 is

$$
\begin{gathered}
 \forall s\ \exists\alpha_s\in(0,1]\ \exists\lambda_s\in[0,1)\quad
 \forall X\ \exists x\ge X:\quad N(x,s)>0,\\
 N_{\mathcal G}\ge\alpha_sN,\qquad
 \forall P\in\mathcal G\ \forall d\
 \bigl(N_{P,d}\ge2\Longrightarrow
 N_{P,d}\le\lambda_sN_P+1\bigr).
\end{gathered}
$$

H2 has the outer quantifiers and classwise clauses in C.2. H3 and H4
each use

$$
 \forall s\ \exists\eta_s>0\ \forall X\ \exists x\ge X:
 \quad N(x,s)>0
$$

followed, respectively, by

$$
 \sum_{P\in\mathcal G}(N_P-M_P)\ge\eta_sN
 \qquad\text{or}\qquad
 \sum_{P\in\mathcal G}D_P\ge\eta_sN.
$$

The outcome quantities in H3 and H4 certify the selected family's
margin; they may not define that family.

For the exact relation to the old inputs, put
$`c(x)=C_q(x)/\log{} x`$. At every sufficiently large scale,
NI-M5a and NI-M5b give the H1 row with $`\alpha=7/8`$ and
$`\lambda=c(x)`$; choosing any fixed $`\lambda_0\in(0,1)`$ after
$`c(x)\le\lambda_0`$ gives H1's along-scales form. They give H2 with
$`\kappa_P=1-c(x)`$ and

$$
 \sum_{P\in\mathcal G}\kappa_PN_P
 \ge\frac78(1-c(x))N.
$$

They also give

$$
 \sum_{P\in\mathcal G}(N_P-M_P)
 \ge(1-c(x))N_{\mathcal G}-F_{\mathcal G},
 \qquad
 \sum_{P\in\mathcal G}D_P
 \ge(1-c(x))N_{\mathcal G}-F_{\mathcal G}.
$$

Thus H3 and H4 follow with a fixed positive margin after also using
the separate `SparseFlankFamily` input
$`F_{\mathcal G}/N\le F/N\to0`$. This extra sparse-family use is not
silently attributed to NI-M5a or NI-M5b.

By mathematical statement weakness, direct defect is closest to the
minimum, while H2 gives the weakest useful M5-style proof surface.
H3 and H4 are equivalent up to a factor two. H1 and H2 are
qualitatively equivalent after thresholding an ex ante profile, but H2
retains the sharper weighted budget.

As a `HEURISTIC` route-design ranking, proof usefulness is H2, H1,
H3, H4, while direct measurability and robustness is H3/H4, H2, H1.
Compatibility with the recorded M5 vocabulary is H1, H2, H3, H4.

The selected successor is therefore:

$$
 \boxed{\texttt{ExAnteWeightedMiddleContractionAlongScales}.}
$$

Its exact quantifiers and dependencies are those of C.2. The
selector and coefficient profile are part of the named statement
data, not existential objects selected after the scale's collision
outcome is inspected. Analytic content remains `OPEN`.

`PositiveMassMiddleEscapeAlongScales` is the preferred
measurement-facing companion:

$$
 \forall s\ \exists\eta_s>0\ \forall X\ \exists x\ge X:
 \quad N(x,s)>0,\qquad
 \sum_{P\in\mathcal G_{s,x}}(N_P-M_P)\ge\eta_sN(x,s).
$$

It is deliberately stronger than the minimal self-pair-sensitive
modal certificate and guards against singleton-dominated finite
rows.

## G. Revised measurement specification

No measurement is executed by this audit. A later campaign requires a
separately ratified dispatch.

### G.1 Predeclared frontier registry

Before computing any middle histogram, version a finite registry of
selector/profile rules. The primary rows must use the exact
D0-coupled parameter map. Fixed sub-frontier rows are continuity
diagnostics only.

The six numbered requirements in
`dossier/item-0010-workpapers/collision-gap-audit.md`, section J, are
incorporated without weakening. The new profile fields below are
additions, not replacements. In particular, retain:

1. exact full-family $`Q/N`$, $`F/N`$, and $`(N-F-Q)/N`$;
2. every predeclared dyadic class-size row
   $`N_M/N`$, $`W_{2,M}`$, $`V_{2,M}`$, $`Q_M/N`$, rigid and
   non-rigid site mass, with the earlier G.3 integrity checks;
3. residual-boundary $`A_P`$ with directed high-precision comparison,
   only the necessary primes $`p\le k`$, isolated base-prime and
   initial exceptions, the late-anchor site-mass distribution of
   $`A_P`$, contaminated site mass, and
   $`\sum_PN_P/(N\widetilde A_P)`$;
4. full-family rho energy
   $`N^{-1}\sum_{P,d}N_{P,d}\rho(P,d)`$ with the same exact local
   factors, certified tails, and separate off-domain or
   inadmissibility-exception contribution;
5. weighted and unweighted correlations using the actual cell
   contribution $`N_{P,d}(N_{P,d}-1)/N_P`$ against $`N_P`$, the
   dyadic stratum, $`A_P`$, and $`\rho(P,d)`$; and
6. predeclared CRT-profile site mass, rho energy, and $`Q`$
   contribution for
   $`(\nu_H,\nu_{\mathrm{pre}},\nu_{\mathrm{suf}})`$.

The registry should cross, where computationally feasible:

- prospective rho caps, including several fractions of
  $`\log{} x`$ rather than only $`o(\log{} x)`$-motivated caps;
- predeclared small-prime CRT profiles, at least
  $`p=3,5,7,11,13`$;
- side-span and residual-middle-domain strata;
- predeclared $`N_P`$ bins;
- combinations fixed before opening the collision data.

Every registry entry must store both the selector formula and the
declared saving formula
$`\kappa^{\mathrm{decl}}(s,x,P)\in[0,1]`$, including all thresholds
and empty-set conventions. The family rule and saving profile must
never be redefined from observed collision performance.

### G.2 Exact finite certificate metrics

For every $`(s,x,\mathrm{rule})`$ row, report in exact rational
arithmetic

$$
 \alpha=\frac{N_{\mathcal G}}N.
$$

Define

$$
 r_P=
 \max_d\frac{(N_{P,d}-1)_+}{N_P},
$$

with $`r_P=0`$ for a singleton. Write
$`\kappa_P=\kappa^{\mathrm{decl}}(s,x,P)`$. The declared classwise
bound holds exactly when

$$
 r_P\le1-\kappa_P.
$$

Therefore report

$$
 \delta_P=(1-\kappa_P)-r_P,\qquad
 \mathcal V=\lbrace P\in\mathcal G:\delta_P<0\rbrace,
$$

$$
 \eta_{\mathrm{profile}}
 =\frac1N\sum_{P\in\mathcal G}\kappa_PN_P,\qquad
 \beta_{\mathrm{viol}}
 =\frac1N\sum_{P\in\mathcal V}N_P,
$$

as well as $`\min_{P\in\mathcal G}\delta_P`$ and
$`\max_{P\in\mathcal G}(-\delta_P)_+`$. If
$`\mathcal G`$ is empty, report it explicitly,
set $`\eta_{\mathrm{profile}}=\beta_{\mathrm{viol}}=0`$, and leave
the two extrema undefined rather than inventing favorable values.

The declared profile passes its classwise test exactly when
$`\mathcal V`$ is empty. If it passes, then [PROVED]

$$
 \boxed{
 \frac QN
 \le1-\eta_{\mathrm{profile}}
 -\frac{F_{\mathrm{exc}}}N.
 }
$$

It is a positive-margin finite H2 certificate only when also
$`\eta_{\mathrm{profile}}>0`$. A failed row must remain failed; no
post hoc reduction of $`\kappa_P`$ may be reported as validation of
the declared rule.

For comparison, report the post hoc uniform optimum

$$
 \lambda_{\max}
 =
 \max_{\substack{P\in\mathcal G\cr N_P\ge2}}r_P.
$$

If the indexed set is empty, report that fact and use the declared
empty-set convention $`\lambda_{\max}=0`$. The uniform finite
certificate is

$$
 \eta_{\mathrm{cert}}
 =(1-\lambda_{\max})\alpha.
$$

Also report the post hoc optimal weighted envelope and the
singleton-inert exact quantities

$$
 \eta_{\mathrm{weight}}
 =
 \frac1N\sum_{P\in\mathcal G}(1-r_P)N_P
 =
 \frac1N\sum_{P\in\mathcal G}(N_P-M_P+1),
$$

$$
 \eta_{\mathrm{escape}}
 =
 \frac1N\sum_{P\in\mathcal G}(N_P-M_P),
$$

and

$$
 \eta_{\mathrm{Gini}}
 =
 \frac1N\sum_{P\in\mathcal G}
 N_P\left(1-\sum_dp_{P,d}^2\right).
$$

The table integrity checks are

$$
 \eta_{\mathrm{cert}}\le\eta_{\mathrm{weight}},
 \qquad
 \eta_{\mathrm{weight}}
 =\eta_{\mathrm{escape}}+\frac{F_{\mathcal G}}N,
$$

and

$$
 \eta_{\mathrm{escape}}
 \le\eta_{\mathrm{Gini}}
 \le2\eta_{\mathrm{escape}}.
$$

On every declared-profile passing row, also verify

$$
 \eta_{\mathrm{profile}}\le\eta_{\mathrm{weight}}
$$

and the boxed global inequality against the directly computed
$`Q/N`$. These are rigorous certificates for that finite row only.
The $`r_P`$-optimized quantities are post hoc finite envelopes, not
validation that a declared profile persists asymptotically.

### G.3 Mandatory global diagnostics

Every scale must still report

$$
 \frac QN,\qquad
 \frac FN,\qquad
 \frac{N-F-Q}{N}.
$$

The last quantity must agree with the all-class Gini defect.

The following warning is binding:

> A small $`Q/N`$ with $`F/N\approx1`$ provides no non-rigidity
> margin. Singleton-dominated finite regimes make $`Q/N`$,
> $`\lambda_{\max}<1`$, and $`\eta_{\mathrm{weight}}`$ look
> favorable for self-pair reasons alone.

Indeed, every finite realized class has $`r_P<1`$. Thus every nonempty
finite predeclared family has $`\lambda_{\max}<1`$ and a formally
positive rowwise $`\eta_{\mathrm{cert}}`$. The campaign question is
whether a declared profile has
$`\beta_{\mathrm{viol}}=0`$ and
$`\eta_{\mathrm{profile}}`$ bounded below, or whether a
singleton-inert margin stays bounded below, on an unbounded
D0-coupled sequence. Positivity at one finite row is not enough.

### G.4 Robust summaries and evidence classes

Uniform maxima may be dominated by negligible classes. Also report:

- site-mass-weighted distributions and quantiles of $`r_P`$;
- trimmed and untrimmed site-weighted means;
- Pareto frontiers of $`\alpha`$, $`\lambda_{\max}`$, and
  $`\eta_{\mathrm{cert}}`$ across the predeclared registry;
- the exact contributions to $`\eta_{\mathrm{escape}}`$ and
  $`\eta_{\mathrm{Gini}}`$ by class-size, rho, and CRT strata;
- scale trends separately for each fixed $`s`$.

A weighted quantile can yield a finite inequality only after the
entire omitted tail is charged explicitly by the universal zero-saving
bound. Such a calculation is still outcome calibration and may not be
used to redefine the favorable family.

Classifications:

- **rigorous finite certificates:** the exact partition identities,
  the declared-profile violation test and passing-row bound,
  $`\lambda_{\max}`$ plus $`\eta_{\mathrm{cert}}`$, the post hoc
  weighted envelope, majority escape, Gini defect, and explicit
  universal tail charges;
- **measured, non-certifying diagnostics:** exact weighted quantiles,
  trimmed summaries, and frontier rows are `MEASURED` once executed;
  their persistence or asymptotic interpretation remains
  `HEURISTIC`;
- **post hoc explanatory correlations:** top contributors and
  correlations against $`N_P`$, admissible-middle multiplicity, rho,
  span, and CRT profile are `MEASURED` outputs, while any proposed
  mechanism inferred from them is `HEURISTIC`.

No post hoc explanatory category may feed back into the selector
registry in the same campaign.

## H. Proof-route consequences

### H.1 Statement requirements versus proof devices

`CollisionGapAlongScales` consumes only:

1. one fixed $`s`$ at a time;
2. a positive $`s`$-dependent margin;
3. unbounded favorable scales;
4. the existing filters-first definitions of $`N`$ and $`Q`$.

The following are not statement-level dependencies:

- a rho cap;
- CRT-alignment selection;
- singular-series control;
- a local quotient law;
- relative sieve;
- dispersion;
- a specific middle-slot distribution theorem.

They are possible proof devices for producing the contraction margin.
Within the recorded inventory, success requires an input outside the
named model-blind list T that fails in the smooth barrier model.
Prime-specific middle-slot control is a salient candidate, not a
proved necessary category.

### H.2 What is genuinely relaxed

The old M5 lane sought almost all favorable mass and a coefficient
tending to zero. The new ledger permits:

- any positive favorable site share;
- any coefficient bounded strictly below one;
- a class-dependent weighted saving;
- constants depending on $`s`$;
- only unbounded favorable scales.

This is a genuine statement and constant relaxation. In particular,
$`R=o(\log{} x)`$ is not logically required. A rho-based proof may use
a substantially larger cap if it can still prove a strict contraction
and a positive site-weighted margin.

### H.3 What remains blocked

The recorded rank-$`2k`$ union-sieve route remains beyond budget. The
fixed-contraction endpoint does not absorb its superpolylogarithmic
constant.

The recorded relative/class-level route still lacks NI-M2. A weaker
one-sided carrier targeted only at positive mass could suffice, but no
such carrier is proved or present in the corpus.

The recorded dispersion route still lacks NI-M4 at word grain. A
lower-moment or positive-proportion theorem might be enough for
M5-lite, but this is a speculative route-design observation, not a
deduction.

Signed-weight routes remain in the recorded F20.6 merge classes.

Therefore M5-lite is not yet a proof of item-0010 and not yet a
genuinely new mechanism. It is a strictly cheaper endpoint. Within the
recorded program, a future route is new only when it supplies the
missing carrier, including an input outside list T that fails in the
smooth model. This conclusion retains the U20.4 inventory and U20.5
write-out qualifications.

## I. Optional Lean-facing note

No Lean is implemented here.

A statement-layer design may parameterize the analytic Prop by a named
selector and contraction profile:

```text
def ExAnteWeightedMiddleContractionAlongScales
    (P : SupplyParams) (sel : Selector) (save : SavingProfile) : Prop :=
  forall s, exists eta : Rat, 0 < eta and
    forall X, exists x, X <= x and
      0 < (filteredSites P s x).card and
      classwise_middle_bounds P sel save s x and
      eta * (filteredSites P s x).card <=
        weighted_saving P sel save s x
```

This is Lean-shaped pseudocode, not accepted syntax. The selector and
profile admissibility conditions should be documentation and
statement-layer parameters; the analytic content remains a named Prop.

The finite layer needs:

1. a realized-middle fiber partition proving
   $`\sum_dN_{P,d}=N_P`$;
2. positivity of realized-class denominators, already available as
   `classSites_nonempty`;
3. the classwise contraction sum of B.2;
4. the weighted global sum of B.6;
5. the previously proposed finite
   `collision_deficit_supply` extraction.

The intended theorem chain is:

```text
ExAnteWeightedMiddleContractionAlongScales
  -> CollisionGapAlongScales

(FamilySparse and CollisionGapAlongScales)
  -> CollisionDeficitSupply

CollisionDeficitSupply
  -> ExchangeSupply1
```

The new algebraic implication is simple enough to formalize
independently of any analytic supplier. The final theorem should reuse
the existing `supply_of_triple` clause-table pattern rather than
duplicate it. No change to the analytic evidence classification or to
the existing classical-three axiom expectation is suggested.
