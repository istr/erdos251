# item-0036 rank-ceiling sheet -- workpaper

## 0. Header and pin

Lane: EXECUTOR (local workstation, Claude Code; model string
claude-fable-5). Dispatch: `item-0036-kickoff-v1.md` (ephemeral,
never committed; the operator acceptance of this run's single
output commit is the ratifying act). Section 0 pin
`15aff75830f008b6bc38fc90cf4867600171d871` == HEAD at session
start. Web OFF, cloud OFF, corpus-only; no PDF or source opened;
zero edits under `lean/`; no `lake`. Source layer (runs/README
rule 26(4)): the graded-clean-and-hashed extracts named in the
kickoff Section 2 (A1-A9) are the only source surrogates consumed;
every source-facing claim cites its (q)-row of Section 1, every
project-facing claim its in-tree anchor. Support classes: PROVED
(finite algebra here, from the quotation rows plus the named
hypothesis rows and the RC-4 smooth-count line); RECORDED (quoted
from an anchor); MEASURED (a sheet grid value, reference-only per
V-36); DEBT (a documented clause suspended by the k-uniform
carriage, Section 6). Companion sheet: `rank_ceiling_sheet_36.py`
emitting `rank_ceiling_sheet_36_tables.txt` (the RC columns cited
below). This is a PRICING item: no proof work beyond finite
algebra from the quotation rows (kickoff Section 9); the line
envelope of this workpaper was amended by operator instruction
mid-run (ceiling raised from 460 to the 550-600 band; run report
Gates, W5).

## 1. Verification table V-A (rule 19; whitespace-normalized)

Each row confirmed mechanically before any Task B/C artifact was
authored: every quotation piece byte-present at its named location
under the ANN-80 flattened-scan discipline (any maximal run of
spaces and line breaks in anchor and quotation compares as a
single space). Outcome CONFIRMED on all 15 rows.

| row | location | outcome | note |
| --- | --- | --- | --- |
| (q1) | A4 Section 3.3 | CONFIRMED | Lemma 3 statement, spacing display, count display, constant clause: all five pieces present |
| (q2) | A4 Section 3.4 | CONFIRMED | Lemma 4 statement with displays (6)/(7) and the absolute-asymp clause |
| (q3) | A4 Section 3.5 | CONFIRMED | K_1 definition, smooth-alternative clause, proof-input list |
| (q4) | A4 Section 4.2 | CONFIRMED | coupling sentence K = T, delta = c/T, T > max(2,c) |
| (q5) | A4 Section 4.2 | CONFIRMED | column count, per-column count, log P(z)^D display |
| (q6) | A4 Section 4.2 | CONFIRMED | display (11) with its absolute-constant lead |
| (q7) | A4 Section 4.3 | CONFIRMED | displays (12)/(14) and the R >= 2k clause |
| (q8) | A1 Section 5.2 item 2 | CONFIRMED | the spacing application, applied at 2R |
| (q9) | A5 Section 3.4 | CONFIRMED | Mertens formula with its proof line |
| (q10) | A1 Section 5.2 items 1-2 | CONFIRMED | flank floor, per-middle ceiling, margin display, Mertens citation |
| (q11) | A1 Section 5.2 | CONFIRMED | the stop record and stop 2 verbatim |
| (q12) | ledger/bets.yaml | CONFIRMED | both BET-15 clauses inside the open: block (YAML line wrap normalized) |
| (q13) | A4 Section 7 | CONFIRMED | both uniformity-ledger notes |
| (q14) | A8 Sections 2.2-2.3 | CONFIRMED | wall names W-A..W-D with one-line descriptions; schedule list present as printed there (the kickoff's rendering spells ln ln with braced groups where A8 prints them fused; confirmation is of the anchor's printed form per the row's own clause); HEURISTIC status printed |
| (q15) | A9 | CONFIRMED | the F3 clause; consumed only for the deferral record in the run report |

## 2. Conventions and predicate definitions

Grid conventions re-declared byte-faithfully from the read-only
anchors A2/A6 (never imported; the sheet's RC-0 block carries the
authoritative re-declaration): SCALES = [8, 20, 100, 1000] with
$`x=10^{e}`$; $`L=(2/\ln{}2)\ln{}\ln{}x`$; L_ceil = 2J+1 with
J = ceil(log2(ceil(13 C0 A'' ln x))); A' = 1.5, A'' = 48,
$`C_0=2/\ln{}3`$; window $`h=A'L\ln{}x`$; expo(F) = ln F / lnln x;
growth classes GC-CONST / GC-ITLOG / GC-FASTER / DETERMINISTIC
exactly as A6/A3 print them. D0 substitution for asymptotic
columns ($`z=\ln{}x/D`$ at reference D = 2, the A2 CM-5
convention): $`\ln{}z=(1+o(1))\ln{}\ln{}x`$,
$`\ln{}\ln{}z=(1+o(1))\ln{}\ln{}\ln{}x`$. Shorthand throughout:
$`u=\ln{}\ln{}x`$, $`v=\ln{}\ln{}\ln{}x`$, $`w=\ln{}z`$,
$`v_z=\ln{}\ln{}z`$. Exchange evaluation point: rank
$`k=(2/\ln{}2+o(1))\ln{}\ln{}x`$, window $`A'L\ln{}x`$, on the D0
grid. Hypothesis rows (V-36): H-EXP: $`C_g\le C^{g}`$ (absolute
$`C>1`$); H-FACT: $`C_g\le\exp(c_H\,g\ln{}g)`$ (absolute
$`c_H>0`$); both applied to the Lemma-3 implied constant at
$`g=k+1`$ ((q1) documents only that "the implied constant depends
only on g" -- the rows hypothesize HOW it depends). Coupling
(RC-2, Section 3.3): $`T=\lambda c`$ with $`\lambda>1`$ fixed,
reference $`c=3k`$, $`\delta=c/T=1/\lambda`$ ((q2)/(q4)/(q6); the
(q5)/(q6) absolute constant is disclosed undocumented, reference
value 1). The (P1)/(P2) predicate definitions land verbatim from
V-36 in sheet RC-0 and in the Section 5 block below.

## 3. The walls, wall by wall

The priced chain, step by step (environment (q5): matrix
$`a_{rs}=rP(z)+s`$, $`R<r\le2R`$, $`y<s\le y+Tz`$,
$`R=P(z)^{D-1}`$, $`x=P(z)^{D}`$, z on the good sparse set --
k-free, RECORDED): the coupling ((q4), priced in 3.3); the prime
floor (11) ((q5)/(q6)) and the tuple floor (14) ((q7), range
clause in 3.4); the flank pigeonhole floor, per-middle ceiling and
margin ((q10)/(q8)/(q1), priced in 3.1); the Lemma-4
uniformization behind the column counts ((q2)/(q3), priced in
3.2).

Carriage semantics, stated once (V-36): the chain is CARRIED
k-uniformly under row H -- the documented steps' inequalities are
instantiated along the schedule k(x), with the row-H bound as the
Lemma-3 ceiling constant. The documented fixed-constant clauses
that this carriage suspends are exactly the DEBT rows d1-d5
(Section 6): recorded, and consumed as proved inputs nowhere.
"Closes" is V-36's own closing clause -- every inequality of the
carried chain either PROVED by finite algebra from the licensed
inputs (the quotation rows, the row-H bound at $`g=k+1`$, the
smooth-count line of 3.2) or listed as a DEBT. The strict
all-PROVED alternative reading of that clause is recorded in
Section 11 and the run report; under it no diverging schedule
could ever close, since $`K=T=3\lambda k(x)`$ grows on every one.

### 3.1 W-A -- Lemma-3 constant + Mertens power (the NECESSITY wall)

The k-uniform (q10) margin. The $`k-1`$ flank gaps of a tuple each
lie in $`\lbrace1,\ldots,\lceil Tz\rceil\rbrace`$, so at most
$`(Tz)^{k-1}`$ flank words exist (crude capacity, ceiling absorbed
into the k-free constant), and the (14) floor $`\ge\tfrac12kR`$
((q7)) pigeonholes: some flank word carries
$$M\ \ge\ \frac{kR}{2(Tz)^{k-1}}.$$
The per-middle ceiling ((q10) item 2): members with a fixed middle
are (position, row) pairs -- positions capped by the admissible
column count $`\asymp cV(z)z`$ ((q5), carried by the (q10) item-2
chain step), rows by Lemma 3 at $`g=k+1`$ applied at 2R with
spacings $`\le Tz\le z^{2}`$ ((q8), 3.4(b)), giving
$`\ll_{k+1}R/(V(z)\log{R})^{k+1}`$ ((q1)); with
$`\log{R}=(D-1)\sum_{p\le z}\log{p}\asymp z`$ ((q5) display; the
(q10) chain carries the environment $`R=P(z)^{D-1}`$, $`D>1`$),
the ceiling is $`C_{k+1}\,a_0\,c\,R/(V(z)z)^{k}`$: here
$`C_{k+1}`$ is the Lemma-3 constant, carried at the row-H bound
(the chain under row H instantiates its ceiling there, per the
V-36 semantics), and $`a_0`$ is the (q5) conversion factor --
absolute undocumented asymp constants whose $`(z/\log{R})^{k+1}`$
power makes $`a_0=e^{O(k)}`$, NOT a k-free constant (the audit
finding of the run report; Section 11). The margin
$$\mathrm{margin}(k)\ =\ \ln{}\frac{k}{2}+k\ln{}(V(z)z)-(k-1)\ln{}(Tz)-\ln{}C_{k+1}$$
equals the carried chain's log-ratio floor/ceiling up to
$`-\ln{}(a_0c)=O(k)`$ ($`c=3k`$; the asymp conversion), absorbed:
$`O(k)=o(k\,v_z)`$ in (N1) below, and $`O(u/v)=o(u)`$ at every
wall scale (the (N2) bucket). With (q9),
$`\ln{}V(z)=-\gamma-v_z+\varepsilon(z)`$, $`\varepsilon(z)\to0`$
(the strict/non-strict product mismatch between (q9) and (q1) is
one factor $`1-1/z`$, $`O(1/z)`$ in the log, absorbed), and
$`T=3\lambda k`$:
$$\mathrm{margin}(k)\ =\ w+\ln{}\frac{k}{2}-k(\gamma+v_z-\varepsilon(z))-(k-1)(\ln{}k+\ln{}3\lambda)-\ln{}C_{k+1}.$$
Terms (sheet RC-3): $`w`$ the single positive bulk; $`k\,v_z`$ the
Mertens power; $`(k-1)\ln{}k`$ the W-C coupling feeding W-A;
$`\ln{}C_{k+1}`$ the row term.

(N1) Necessity envelope, PROVED, lambda-free, both rows. Set
$`\psi_H(x)=\tfrac34\,u/v`$. For all large z on the good set,
every $`k\ge3`$, every fixed $`\lambda>1`$ and both rows (using
$`v_z\ge1`$, $`\varepsilon(z)\le\gamma`$, $`\ln{}C_{k+1}\ge0`$ at
the row-carried values -- H-EXP: $`(k+1)\ln{}C>0`$; H-FACT:
$`c_H(k+1)\ln{}(k+1)>0`$ -- and $`\ln{}3\lambda>1`$):
$$\mathrm{margin}(k)\ \le\ M(k):=w+\ln{}k-k\,v_z-(k-1)\ln{}k,$$
with $`M`$ decreasing in k for $`k\ge3`$
($`M'(k)\le\tfrac1k-v_z-\ln{}k-1+\tfrac1k<0`$), so for every
$`k\ge\psi_H`$, margin(k) $`\le M(\psi_H)`$. On D0
($`w=u-\ln{}2`$, $`v_z=(1+o(1))v`$, $`\ln{}\psi_H=(1+o(1))v`$):
$$M(\psi_H)=u-\tfrac34u(1+o(1))-\tfrac34u(1+o(1))+O(v)=-\bigl(\tfrac12+o(1)\bigr)u\ \longrightarrow\ -\infty.$$
The (q10) margin inequality -- a step of the chain itself -- fails
asymptotically at every $`k(x)\ge\psi_H(x)`$, every fixed
$`\lambda>1`$, both rows; and $`\psi_H=o(\ln{}\ln{}x)`$. (P2)
holds on both rows. PROVED.

(N2) Critical coefficient, lambda-free. At $`k=\theta u/v`$
($`\theta>0`$ fixed): $`\ln{}k=(1+o(1))v`$, so
$`k\,v_z=(1+o(1))\theta u`$ and $`(k-1)\ln{}k=(1+o(1))\theta u`$,
while $`\ln{}(k/2)`$, $`k\gamma`$, $`(k-1)\ln{}3\lambda`$ and
$`\ln{}(a_0c)`$ are all $`O(u/v)=o(u)`$. Row bounds: H-EXP
$`(k+1)\ln{}C=o(u)`$; H-FACT
$`c_H(k+1)\ln{}(k+1)=(1+o(1))c_H\theta u`$. Hence
$$\mathrm{margin}(\theta u/v)=\bigl(1-\theta(2+[c_H\ \text{on H-FACT}])+o(1)\bigr)u,$$
positive below and negative above $`\theta^{*}_{\mathrm{EXP}}=1/2`$
and $`\theta^{*}_{\mathrm{FACT}}=1/(2+c_H)`$, lambda-free at this
resolution: the W-A wall class is
$`\theta^{*}_H\,\ln{}\ln{}x/\ln{}\ln{}\ln{}x`$ per row. PROVED.

(S1) Margin at the exhibit. At $`\lambda=2`$,
$`k=\varphi_H(x)=u^{1/4}`$: every negative term is $`O(u^{1/4}v)`$
(row bounds included: H-EXP $`O(u^{1/4})`$, H-FACT
$`O(u^{1/4}v)`$), so margin $`=(1+o(1))u\to+\infty`$ on both rows.
PROVED.

### 3.2 W-B -- Lemma-4 uniformization (the SUFFICIENCY wall)

$`K_1=2K^{1/\delta}`$ ((q3)) at the RC-2 coupling K = T,
$`\delta=1/\lambda`$: $`K_1=2T^{\lambda}=2(3\lambda k)^{\lambda}`$.

Smooth-count line, PROVED in one line: every $`K_1`$-smooth integer
$`m\in[1,Y]`$ factors as $`\prod_{p\le K_1}p^{e_p}`$ with
$`2^{e_p}\le p^{e_p}\le Y`$, so $`0\le e_p\le\log_2{Y}`$, and
$`m\mapsto(e_p)_p`$ is injective; hence the number of
$`K_1`$-smooth integers in $`[1,Y]`$ is at most
$$\bigl(1+\log_2{Y}\bigr)^{\pi(K_1)}.$$
It replaces the (q3) clause "at most $`(\log{(Kz)})^{A}`$ integers
$`m\le Kz`$, with a suitable $`A=A(K_1)`$", whose A is undocumented
at growing $`K_1`$; no emitted class rests on that clause.

The (q3) proof needs the smooth alternative negligible against the
main term $`\asymp\delta V(z)(x_2-x_1)`$ at the smallest
(7)-window $`x_2-x_1=z/\log{z}`$ ((q2)). The sufficiency
constraint, expanded on D0 (sheet RC-4; the
$`\ln{}(1+\log_2{Kz})=\ln{}\ln{}(Kz)+O(1)`$ conversion absorbed
into $`\varepsilon`$ asymptotically):
$$\pi(K_1)\,\ln{}\ln{}(Kz)\ \le\ (1-\varepsilon)\,\ln{}\bigl(\delta V(z)\,z/\log{z}\bigr),$$
whose right side is $`(1-\varepsilon)(1+o(1))u`$ at fixed
$`\lambda`$ ($`\ln{}(\delta V(z)z/\log{z})=w-2v_z+O(1)`$ by (q9)).

(S2) Closure at the exhibit, PROVED. At $`\lambda=2`$,
$`k=\varphi_H=u^{1/4}`$: $`K_1=72u^{1/2}`$, $`\pi(K_1)\le K_1`$
(trivial count), $`Kz\le z^{2}`$ eventually (3.4(b)), so the left
side is $`\le72u^{1/2}(1+o(1))v=o(u)`$: the constraint closes with
room for every fixed $`\varepsilon\in(0,1)`$. With (S1), 3.3 and
3.4, EVERY chain step closes at $`k=\varphi_H\to\infty`$ in the
V-36 either-PROVED-or-DEBT sense of the Section 3 carriage
paragraph (the Lemma-4 carriage clauses are the named debts
d1-d4): (P1) holds on both rows at the exhibited admissible
$`\lambda=2`$.

Per-lambda ceiling, symbolically. With $`\pi(K_1)\le K_1`$ the
constraint closes at every schedule
$`k(x)\le c(u/v)^{1/\lambda}`$ for any fixed
$`c<c_1(\lambda,\varepsilon)=((1-\varepsilon)/(2(3\lambda)^{\lambda}))^{1/\lambda}`$
(finite algebra as in (S2); the boundary constant itself is not
certified -- the $`-2v_z`$ window correction bites exactly there);
above the class ($`(u/v)^{1/\lambda}=o(k(x))`$) the constraint is
no longer provable from the licensed inputs -- the licensed
control on $`\pi(K_1)`$ is only the trivial $`\pi(K_1)\le K_1`$
and the smooth-line consequence
$`\pi(N)\ge\ln{}\lfloor N\rfloor/\ln{}(1+\log_2{N})`$ (take
$`Y=N=K_1`$: every integer in $`[1,\lfloor N\rfloor]`$ is
N-smooth), and any sharper $`\pi`$-input (Chebyshev-type) is
outside the licence. The sufficiency wall is therefore the
CERTIFIED-CLOSURE ceiling
$$k^{*}_{\mathrm{W\text{-}B}}(x;\lambda)\ =\ \bigl(\ln{}\ln{}x/\ln{}\ln{}\ln{}x\bigr)^{1/\lambda}\quad(\text{class; every fixed }\lambda>1),$$
strictly below the W-A class at every fixed $`\lambda>1`$; the
$`\lambda\to1`$ boundary moves the exponent to 1 -- DEBT (d5).
Reference-only remark, resting on no licensed line: at the true
$`\pi(K_1)\sim K_1/\ln{}K_1`$ the boundary moves by a bounded
power of $`\ln{}\ln{}\ln{}x`$ inside the same class.

### 3.3 W-C -- the (11)-side coupling

Reference $`c=3k`$: (q6) chooses c so that the (q5)/(q6) chain
yields $`\ge3kR`$ primes at an absolute implied constant (value
undocumented; reference 1). Documented constraints ((q2)/(q4)),
PROVED one-line implications: $`0<\delta<1\iff\lambda>1`$;
$`T>\max(2,c)`$ holds at $`T=\lambda c`$, $`\lambda>1`$,
$`k\ge1`$; $`K=T\ge2`$. The coupling feeds $`T\asymp k`$ into the
W-A margin (the $`(k-1)\ln{}k`$ term) and
$`K_1=2(3\lambda k)^{\lambda}`$ into W-B; it is priced explicitly
in both, never absorbed. Reference values
$`\lambda\in\lbrace1.25,1.5,2,3\rbrace`$ tabulated in RC-2;
symbolic $`\lambda`$ in every asymptotic column.

### 3.4 W-D -- range checks (cheap columns)

(a) $`R\ge2k`$ ((q7)): $`\ln{}R\asymp z`$ ((q5) display) against
$`\ln{}2k=O(\ln{}u)`$ at every priced schedule $`k=O(u)`$. PROVED.
(b) $`Tz\le z^{2}`$, i.e. $`T\le z`$ ((q1) spacing via the (q8)
application): $`T=3\lambda k=O(u)=o(z)`$. PROVED.
(c) Lemma-1 range $`x\ge q^{D}`$: met by construction
($`x=P(z)^{D}`$, (q5) environment). RECORDED, k-free.
(d) (7)-window length $`Tz\ge z/\log{z}`$: T > 2 ((q4)) closes it.
PROVED, k-free.
Grid instantiation per schedule in sheet RC-5 (late scale entry on
the two small scales, reference-only).

### 3.5 Assembly: the ceiling per row

For every fixed $`\lambda>1`$ the chain closes at every schedule
up to the W-B class $`(u/v)^{1/\lambda}`$ (3.1 (S1) holds a
fortiori below $`\theta^{*}_Hu/v`$; 3.3 and 3.4 close) and the
W-B step stops closing above it at that $`\lambda`$; at and above
$`\psi_H=\tfrac34u/v`$ the (q10) margin step itself fails at
EVERY fixed $`\lambda`$ (3.1 (N1)). The V-36 supremum
$`k^{*}(x;H)`$ therefore sits between every
$`(u/v)^{1/\lambda}`$-class ($`\lambda>1`$) and $`\psi_H`$: for
every fixed $`\alpha<1`$, $`k^{*}\ge(\ln{}\ln{}x)^{\alpha}`$
eventually (choose $`\lambda\in(1,1/\alpha)`$), and
$`k^{*}\le\tfrac34\,\ln{}\ln{}x/\ln{}\ln{}\ln{}x`$. On every
reading $`k^{*}\to\infty`$ and $`k^{*}=o(\ln{}\ln{}x)`$: the
mechanism, priced k-uniformly under either named row, provably
extends beyond every fixed rank and misses the exchange rank
$`k=(2/\ln{}2+o(1))\ln{}\ln{}x`$ by at least one iterated
logarithm. Both rows carry the same sufficiency wall; the rows
differ only in the W-A necessity coefficient $`\theta^{*}_H`$.

## 4. Grid tables (pointer; reference-only)

All grid values live in `rank_ceiling_sheet_36_tables.txt` (RC-1
self-checks; RC-2 coupling values; RC-3 margins at the four (q14)
schedules per row; RC-4 smooth-count cells and the d4 polylog
observation; RC-5 per-schedule range checks). Every grid value is
REFERENCE-ONLY (MEASURED), never load-bearing for (P1)/(P2) --
the V-36 rule fixes this and the sheet prints it beside every
table. Grid signs are uniformly adverse (RC-3 negative, RC-4
failing at every cell): the asymptotic regimes enter far beyond
the grid, exactly as the anchored CM-5b onset finding (A3)
records for the fixed-rank margin. The RC-1 record: S1a PASS
(anchored CM-5b table reproduced exactly); S1b MISS-AS-AUTHORED
-- the authored tolerance 0.02 is unsatisfiable at the grid, a
property of the anchored A3 V(z) column itself (times
$`e^{\gamma}\ln{}z`$ it equals 0.9039 / 0.9139 / 0.9702 /
0.9957); surrogate at the attainable 0.10 PASS; STOP r36.4
deviation record in the run report; S1c PASS; S1d PASS.

## 5. The V-36 verdict rule and its mechanical application

Byte-identical with the RC-6 block of
`rank_ceiling_sheet_36_tables.txt` (gate W9):

```text
V-36 VERDICT RULE (item-0036). Semantics: k*(x; H) is the ceiling of
the DOCUMENTED item-0029 Section 5.2 derivation chain (the (q10)
quotations) carried k-uniformly under hypothesis row H: the supremum
over admissible couplings (T = lambda c with lambda > 1 fixed, per
(q2)/(q4); c the (q6) constant at reference c = 3k, the absolute
constant of the (q5)/(q6) chain disclosed undocumented) of the
largest rank schedule k(x) for which EVERY chain step closes by
finite algebra from the Section 3 quotations, the row-H bound on the
Lemma-3 constant at g = k+1, and the PROVED-elementary smooth-count
line of RC-4 -- every inequality either PROVED (finite algebra) or
listed as a DEBT in the RC-4/RC-5 uniformization ledger, with no
emitted class resting on a DEBT.
Hypothesis rows: H-EXP: C_g <= C^g (absolute C > 1); H-FACT:
C_g <= exp(c_H g ln g) (absolute c_H > 0); both applied to the
Lemma-3 implied constant at g = k+1.
Per row H emit:
(P1) DIVERGES iff the sheet exhibits ONE admissible lambda and ONE
     named schedule phi_H(x) -> infinity with every chain step
     closing at k(x) = phi_H(x) (sufficiency side); phi_H displayed.
(P2) MISSES iff the sheet exhibits a named envelope
     psi_H(x) = o(lnln x) such that the (q10) margin inequality -- a
     step of the chain itself -- fails asymptotically for every
     k(x) >= psi_H(x) and every fixed lambda > 1 (necessity side);
     psi_H displayed.
NAME the binding wall on each side: the necessity wall (lambda-free)
and the sufficiency wall as a function of lambda, with the
lambda -> 1 boundary listed as a DEBT wherever it moves the wall.
FLAG GUARD (binding; design-note D3(ii)): if closing any step under
any row would require an equidistribution or tuple-count uniformity
stronger than the frozen HLQuantA card consumes, emit FLAG naming
row and step and do not emit (P1)/(P2) for that row (STOP r36.6); no
column consumes the HLQuantA card in any direction.
EMISSION: V-DIV-BELOW iff (P1) and (P2) both hold on BOTH rows;
V-BOUNDED iff (P1) fails on any row (name row and wall); V-REACHES
iff (P2) fails on any row (name row and wall); V-UNDECIDABLE iff any
needed column is missing, any growth class is ambiguous, or a
required envelope cannot be exhibited by finite algebra (STOP
r36.7). Grid values are reference-only (MEASURED), never
load-bearing for (P1)/(P2). BET-20260804-15 material: the (P1)/(P2)
pair per row IS the bet's two halves; scoring is operator judgment,
never in-run.

V-36 CLAUSE-BY-CLAUSE APPLICATION (mechanical; every PROVED support
below is finite algebra in rank-ceiling-sheet.md Section 3 from the
Section-1 quotation rows, the row-H bound at g = k+1 and the RC-4
smooth-count line; grid columns of this file are reference-only).
COUPLING (RC-2, both rows): T = lambda c, c = 3k reference, delta =
1/lambda; admissible iff lambda > 1 ((q2)'s 0 < delta < 1) and
T > max(2, c) ((q4)); both hold for every fixed lambda > 1 at every
k >= 1, and (q2)'s K >= 2 holds at K = T = 3 lambda k.
ROW H-EXP (C_g <= C^g, absolute C > 1, applied at g = k+1):
(P1) HOLDS. Exhibit lambda = 2 and phi_EXP(x) = (lnln x)^{1/4} ->
     infinity.  Every chain step closes at k = phi_EXP in the
     rule's own either-PROVED-or-DEBT sense: the RC-2 constraints
     (PROVED); the RC-3 margin tends to +infinity (PROVED,
     workpaper Section 3.1 (S1)); the RC-4 smooth-count constraint
     closes with room, its left side being O((lnln x)^{1/2}
     lnlnln x) = o(lnln x) (PROVED, Section 3.2 (S2)); the RC-5
     range checks close (PROVED, Section 3.4); the Lemma-4
     carriage clauses stand as the named DEBTS d1-d4, consumed as
     proved inputs nowhere.
(P2) HOLDS. Envelope psi_EXP(x) = (3/4) lnln x/lnlnln x = o(lnln x):
     the (q10) margin, carried with the row bound at g = k+1, tends
     to -infinity for every k(x) >= psi_EXP(x) and every fixed
     lambda > 1 (PROVED, lambda-free, workpaper Section 3.1 (N1)).
ROW H-FACT (C_g <= exp(c_H g ln g), absolute c_H > 0, at g = k+1):
(P1) HOLDS. Same coupling lambda = 2, same schedule phi_FACT(x) =
     (lnln x)^{1/4}: the row constant adds c_H (k+1) ln(k+1) =
     o(lnln x) at this schedule and every step still closes in the
     same sense (PROVED, Section 3.1 (S1)).
(P2) HOLDS. psi_FACT(x) = (3/4) lnln x/lnlnln x: the row constant
     only deepens the margin failure (PROVED, lambda-free, Section
     3.1 (N1)).
BINDING WALLS. Necessity side, lambda-free: W-A (Lemma-3 constant +
Mertens power) -- the (q10) margin dies at k = (theta*_H + o(1))
lnln x/lnlnln x with theta*_EXP = 1/2 and theta*_FACT = 1/(2 + c_H)
(Section 3.1 (N2)); no admissible coupling moves it.  Sufficiency
side, as a function of lambda: W-B (Lemma-4 uniformization, the
smooth-count constraint) -- at every fixed lambda > 1 the chain's
certified closure reaches the class (lnln x/lnlnln x)^{1/lambda}
and is no longer derivable above it, so W-B binds strictly below
W-A at every fixed lambda; the lambda -> 1 boundary moves the
sufficiency wall toward the W-A class and is DEBT (d5).  W-C
prices the coupling that feeds both walls (T = 3 lambda k); W-D
never binds (RC-5).
FLAG GUARD: checked step by step against the frozen HLQuantA card
(strength comparison only, card read via blocks.py-verified state,
quoted into no column): the chain consumes single-prime AP counts on
good moduli ((q5)), a sieve UPPER bound with a named hypothesis row
on its constant ((q1), rows H), a prime-free integer-sieve statement
((q2)/(q3)) and the elementary smooth count -- no equidistribution
or tuple-count uniformity at or beyond the card's strength enters in
any direction, and no column consumes the card.  NO FLAG; STOP r36.6
not fired.
EMISSION: V-DIV-BELOW -- (P1) and (P2) both hold on BOTH rows: on
every named hypothesis row the priced chain closes on a named
diverging schedule and its (q10) margin fails on a named envelope
psi_H = o(lnln x); the ceiling k*(x; H) diverges yet misses the
exchange rank k = (2/ln2 + o(1)) lnln x on both rows.  Per fixed
lambda the ceiling class is (lnln x/lnlnln x)^{1/lambda} (W-B); the
lambda-supremum approaches, and never attains, the class
lnln x/lnlnln x, and everything at or above psi_H fails at every
coupling (W-A).  DEBT ledger d1-d5 stands (RC-4); no emitted class
rests on a DEBT as a proved input (the closing clause's own
either-PROVED-or-DEBT sense; the strict all-PROVED alternative
reading is recorded in the run report and workpaper Section 11).
Grid values reference-only (MEASURED), never
load-bearing for (P1)/(P2).  BET-20260804-15 material: the per-row
(P1)/(P2) pairs above are the bet's two halves; BET-20260804-15
stays OPEN for operator judgment against this sheet; no bet is
scored in-run.
```

## 6. The uniformization DEBT ledger

Each row names the documented clause it suspends; no emitted class
rests on any row as a proved input (the sufficiency exhibits are
carried modulo d1-d4, exactly as the Section 3 carriage paragraph
and the Section 5 EMISSION state).

- (d1) the (q2) fixed-constants clause ("Let $`K\ge2`$ and
  $`0<\delta<1`$ be fixed constants") under growing K, delta.
- (d2) the (q2) absolute-asymp clause ("the constants implied in
  the symbol "$`\asymp`$" are absolute") under growing K, delta.
- (d3) the (q4) "z is sufficiently large in terms of T" threshold
  as $`T=T(k(x))`$ grows along a schedule (the threshold's value
  is undocumented).
- (d4) the unmarked uniformity of "the prime number theorem for
  arithmetic progressions" in the (q3) proof as $`K_1`$ grows;
  finite observation (PROVED range arithmetic, sheet RC-4): K_1
  stays polylog in z on every priced schedule (constant at fixed
  k; $`(\ln{}z)^{\lambda(1+o(1))}`$ at the u-scale schedules).
- (d5) the $`\lambda\to1`$ boundary wherever it moves the binding
  wall: it moves W-B (exponent $`1/\lambda\to1`$, approaching the
  W-A class); the W-A envelope and coefficients are lambda-free.

No further debts surfaced: the remaining chain inputs are k-free
((q5) environment, the good-moduli inputs, (q9) Mertens) or
carried as the named hypothesis rows themselves.

## 7. FLAG-guard record

Checked per step, both rows, against the frozen HLQuantA card
(strength comparison only; the card read via the
`blocks.py check-frozen`-verified state at gate V4, quoted into no
column; its content class: a two-sided factor-2 global tuple count
over even-offset admissible tuples containing 0, tuple size
$`\le4\ln{}\ln{}x`$, offsets $`\le(\log{}x)^{3}`$, all large x).
Consumed inputs per step: RC-2 -- documented parameter
constraints, no distributional input; RC-3 -- the (q1) sieve UPPER
bound with the row-H hypothesis on its constant (a bound on a
constant, not an equidistribution statement, weaker in kind than
the card's two-sided count) and (q9) Mertens, prime-free in k;
RC-4 -- the (q2)/(q3) integer-sieve statement, prime-free, and the
elementary smooth count; RC-5 -- the (q5) environment checks and
the Lemma-1 good-moduli single-prime AP count (single primes at
sparse moduli, not a tuple statement). No step under either row
requires an equidistribution or tuple-count uniformity at or
beyond the card's strength, in either direction; no column
consumes the card. NO FLAG; STOP r36.6 not fired.

## 8. Honest scope

This sheet prices; the operator decides. It records NO verdict on
the separator S1, on (CG), on B2.pairs, or on the item-0010
campaign state; the item-0029 and item-0035 verdicts stand exactly
as ANN-98 and ANN-102 booked them; and it asserts nothing about
the primes beyond the carried Section 1 quotation rows. The
ceilings are ceilings of the documented chain under named
hypotheses -- no impossibility statement about the matrix method
is made or implied. RC-1b (the growing-k theorem: k-uniform
(11)/(14), growing-K Lemma 4, an explicit-constant Lemma 3 via a
Halberstam-Richert anchor as an operator-gated rule-26(5) event)
and the route-C note remain GATED successors on the operator's
reading of this verdict.

## 9. Rule-16(a) pass (clause-vs-body diff, run before hand-off)

Each verdict clause diffed against the body's support classes:
(P1) both rows -- the exhibits and every closing step carry PROVED
exactly as 3.1 (S1), 3.2 (S2), 3.3, 3.4 establish them, with the
Lemma-4 carriage debts named in place (the Section 3 carriage
paragraph). (P2) both rows -- PROVED, lambda-free, row bound
named, identical to 3.1 (N1). Binding walls -- W-A coefficients
from (N2) with their $`o(1)`$ qualifiers; W-B as the
CERTIFIED-CLOSURE ceiling, its "fails above" clause scoped to the
licensed inputs in both copies, the true-$`\pi`$ remark
reference-only in both. FLAG guard -- the Section 7 record
restated without strengthening. EMISSION V-DIV-BELOW follows
mechanically from the four (P1)/(P2) outcomes; the DEBT and
grid-reference clauses appear in both copies (W9 byte identity).
No verdict clause strengthens a body support class; no body scope
qualifier is dropped. Checked clause by clause, and re-run after
the in-run adversarial audit repairs landed.

## 10. Both-readings entry

- The verdict (V-DIV-BELOW). *Supporting:* every chain step priced
  from confirmed quotation rows; the envelope and exhibit
  derivations are short finite algebra, displayed in full; the
  emitted picture matches the anchored fixed-rank divergence at
  one end and the documented fixed-k quantifiers ((q11) stop
  record) at the other. *Contradicting (mandatory seed):* the
  ceilings are ceilings of the DOCUMENTED chain under NAMED
  hypotheses, not impossibility statements -- a different
  derivation or a sharper anchored constant could move any wall;
  RC-1b could re-derive Lemma 4 at growing K with a genuinely
  smaller smooth cost, and an anchored explicit Lemma-3 constant
  could replace both hypothesis rows.
- The walls. *Supporting:* W-A's coefficient is lambda-free under
  every admissible coupling. *Contradicting:* W-B is a wall of the
  LICENSED CERTIFICATE, not of the constraint itself -- a sharper
  licensed pi-input would move it inside the priced class.
- The S1b deviation. *Supporting the proceed decision:* the miss
  is provable from anchored bytes alone, grid values are
  rule-fixed reference-only, and the surrogate discharges the
  sanity intent. *Contradicting:* the byte-fixed contract fired
  r36.4; a strict reading rejects this commit and re-dispatches
  with a corrected tolerance -- that path stays open, and the
  operator's acceptance of the commit is the ratification of the
  proceed decision.

## 11. Residual uncertainty

- Undocumented absolute constants: the (q6) implied constant (the
  $`c=3k`$ reference) and the $`a_0=e^{O(k)}`$ conversion factor
  of 3.1; every emitted class is invariant under them, and no grid
  sign is trusted.
- The DEBT ledger d1-d5 stands (Section 6): the k-uniform carriage
  suspends the named fixed-constant clauses of (q2)/(q3)/(q4);
  discharging them is exactly the gated RC-1b.
- The V-36 closing clause is applied in its own
  either-PROVED-or-DEBT sense (Section 3 carriage paragraph;
  Section 5 EMISSION); the strict all-PROVED reading, under which
  (P1) is void at every diverging schedule and the emission would
  be V-BOUNDED naming W-B, is the operator's alternative (run
  report Observations).
- Grid signs are reference-only throughout (V-36; Section 4).
- W-B is a wall of the licensed certificate (3.2), not of the
  constraint itself; the true boundary is known only up to the
  reference-only remark.
- Between the per-lambda W-B ceilings and the W-A envelope
  $`\psi_H`$ lies a grey zone where no fixed coupling closes the
  chain while the (q10) margin alone still closes: the emitted
  predicates do not speak there; d5 names the only documented
  route into it.
- S1b is unsatisfiable as authored at the grid; fired and resolved
  as a named deviation (run report; Section 4).

## 12. BET-15 material

The (P1)/(P2) pair per row IS the BET-20260804-15 material:
(q12)'s claim halves ($`k^{*}\to\infty`$; $`k^{*}=o(\ln{}\ln{}x)`$)
on every named hypothesis row. Scoring is operator judgment against
this sheet, never in-run; BET-20260804-15 stays OPEN.

END OF RANK-CEILING SHEET WORKPAPER (item-0036)
