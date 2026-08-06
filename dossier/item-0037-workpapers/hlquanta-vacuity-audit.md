# item-0037 HLQuantA vacuity audit -- workpaper

## 0. Header and pin

Lane: EXECUTOR (local workstation, Claude Code; model string
claude-opus-5[1m]). Dispatch: `item-0037-kickoff-v1.md` (ephemeral, never
committed; the operator acceptance of this run's single output commit is the
ratifying act). Section 0 pin `4dd53babefa7579954cca7a1aa5c9687e663f8d3` ==
HEAD at session start, so the rule-18 delta is empty. Web OFF, cloud OFF,
corpus-only; no PDF and no source opened; zero edits under `lean/`; no `lake`;
no computation, no census, no `.py` artifact. Source layer (runs/README rule
26(4)): the two graded-clean-and-hashed extracts

- A1 `dossier/item-0029-workpapers/extract/maier85-shortintervals.md`
  (`payloads/HASHES.txt` line 111; CLEAN, ANN-20260803-97),
- A2 `dossier/item-0029-workpapers/extract/hildebrandmaier88-gaps.md`
  (`payloads/HASHES.txt` line 108; CLEAN, ANN-20260802-93),

are the ONLY source surrogates consumed; every source-facing sentence cites its
(q)-row of Section 1, every project-facing sentence its in-tree anchor. Support
classes: PROVED (elementary finite algebra here, from the quotation rows and
the card's own definitions), RECORDED (read from an anchor), PROVED-LEAN
(machine-checked in this tree), OPEN. Logarithms are natural (`Real.log`),
matching the card. No verdict of item-0029, item-0035 or item-0036 is
re-opened, and none is consumed as an input. The line envelope of this
workpaper was AMENDED BY OPERATOR INSTRUCTION mid-run: the dispatch's
[340, 520] became [340, 650] ("I approve a 650 line limit"), issued after the
run reported envelope pressure; gate W4 is checked against the amended band and
the run report records the amendment, its second-recurrence reading and the
process step the operator ordered with it (run report Gates W4, Observations
O2, Follow-up).

## 1. Verification table V-A (rule 19; whitespace-normalized)

Every quotation piece below was confirmed byte-present at its named anchor
BEFORE any Task A or Task B text was authored, under the ANN-80 flattened-scan
discipline (any maximal run of spaces and line breaks in anchor and quotation
compares as a single space). Outcome CONFIRMED on all 31 rows, 56 pieces, 0
misses; rows (q30) and (q31) were added at the end of the refuter pass, with
the same check, when the instance set grew by OSC-0 and BG-1 (Section 12, F7).

| row | anchor | outcome | content |
| --- | --- | --- | --- |
| (q1) | A1 Section 2.1 | CONFIRMED | THEOREM lead sentence and both oscillation displays |
| (q2) | A1 Section 2.1 | CONFIRMED | the sharpened range clause and its display |
| (q3) | A1 Section 3.1 | CONFIRMED | good-modulus definition ("all characters"); `P(z)` strict |
| (q4) | A1 Section 3.2 | CONFIRMED | LEMMA 1, arbitrarily large good z |
| (q5) | A1 Section 3.3 | CONFIRMED | LEMMA 2 (Gallagher) with its full proviso |
| (q6) | A1 Section 3.3 | CONFIRMED | the PNT display inside Lemma 2's proof line |
| (q7) | A1 Section 4.1 | CONFIRMED | the scale restriction (good z, `z >= e^{cD}`, `U <= P(z)`) |
| (q8) | A1 Section 4.1 | CONFIRMED | the matrix display |
| (q9) | A1 Section 4.1 | CONFIRMED | rows are U consecutive integers; columns are APs mod `P(z)` |
| (q10) | A1 Section 4.2 | CONFIRMED | `U=[z^{lambda_1}]`; the `l_0`/`K_0` subdivision |
| (q11) | A1 Section 6 | CONFIRMED | uniformity ledger: z is not free |
| (q12) | A1 FLAGS | CONFIRMED | strict modulus `prod_{p<z} p` |
| (q13) | A1 Section 3.4 | CONFIRMED | LEMMA 3 (Buchstab) and the sieve function `Phi(x,y)` |
| (q14) | A2 Section 2.2 | CONFIRMED | the method paragraph (governing sentence of M-ROW) |
| (q15) | A2 Section 3.2 | CONFIRMED | LEMMA 1 with its display and the `D > 1` clause |
| (q16) | A2 Section 3.2 | CONFIRMED | LEMMA 2, arbitrarily large good z |
| (q17) | A2 Section 3.3 | CONFIRMED | LEMMA 3: spacing hypothesis, count display, constant clause |
| (q18) | A2 Section 3.4 | CONFIRMED | LEMMA 4 with displays (6) and (7) |
| (q19) | A2 Section 4.2 | CONFIRMED | the matrix, `R=P(z)^{D-1}`, `x=P(z)^{D}=RP(z)` |
| (q20) | A2 Sections 4.2, 4.4 | CONFIRMED | `log P(z)^D asymp z`; `log x = D log P(z) >= z` |
| (q21) | A2 Sections 4.2, 4.3 | CONFIRMED | (11), the row count `<= R+1`, and (14) |
| (q22) | A2 Section 4.5 | CONFIRMED | the per-box upper bound (19) |
| (q23) | A2 Section 2.1 | CONFIRMED | THEOREM and its measure display |
| (q24) | A2 Section 5 | CONFIRMED | the nonconstructive clause |
| (q25) | A2 Section 7 | CONFIRMED | uniformity ledger: the z are drawn from Lemma 2's set |
| (q26) | A2 FLAGS | CONFIRMED | nonprincipal-vs-all characters; non-strict modulus |
| (q27) | A2 Section 3.1 | CONFIRMED | good-modulus definition (nonprincipal characters) |
| (q28) | A2 Section 4.2 | CONFIRMED | `y <= 2P(z)` |
| (q29) | A2 Section 3.1 | CONFIRMED | the good-modulus constant C is given, not derived |
| (q30) | A1 Section 2 | CONFIRMED | the cited [9] failure of (1.1) and its `Phi` display |
| (q31) | A2 Section 2 | CONFIRMED | displays (1), (3), (4) and the `c = 0.248...` record clause |

## 2. The audit target

### 2.1 The frozen card, verbatim

Addressed by DECLARATION NAME (item-0016). `python3 lean/scripts/blocks.py
extract HLQuantA` prints sha256
`5d1a63a88356f054cd1ad4600b6cd03686702e36b94a7eb4571710cdb287a762`, equal to
the `lean/frozen-blocks.yaml` manifest value, and `check-frozen` reports
`OK HLQuantA` with all three frozen blocks byte-identical (gate V2). That
extract output is the statement this audit reasons about:

```lean
/-- HYPOTHESIS A (chain-v1 section 1): uniform two-sided tuple counts.
Window: `|H| <= 4 lnln x`, span `<= (log x)^3`, even offsets containing 0,
factor 2 on both sides. -/
def HLQuantA : Prop :=
  exists x0 : N, forall x : N, x0 <= x ->
    forall H : Finset N, 0 in H -> (forall h in H, Even h) -> IsAdmissible H ->
      (H.card : R) <= 4 * Real.log (Real.log x) ->
      (forall h in H, (h : R) <= Real.log x ^ 3) ->
      modelMass H x / 2 <= (tupleCount H x : R) and
        (tupleCount H x : R) <= 2 * modelMass H x
```

[audit note] The block is the frozen block with its Lean unicode
transliterated for this ASCII-only artifact (`forall`, `exists`, `in`, `and`,
`N`, `R`, `<=`, `->`); the byte-exact block is the `blocks.py` output at the
pin and nothing below turns on the rendering. The supporting definitions in the
same file, read at the pin as the operative meaning of the four symbols (they
are NOT themselves frozen): `nuMod H p` is the number of residue classes mod p
occupied by H; `IsAdmissible H` is `nuMod H p < p` for every prime p;
`singularSeries H` is the tprod of `(1 - nuMod H p / p) / (1 - 1/p)^{|H|}` over
the primes; `tupleCount H x` counts `{a in [0,x] : a + h prime for all h in H}`;
`modelMass H x` is `singularSeries H * x / (log x)^{|H|}`. Two authoring notes
carried from the card's module docstring, RECORDED and not re-litigated: the
factor-2 band was chosen after the gpt-iso 9.8 `HLQuantFull` template (relative
accuracy on exact gap cylinders) was found provably false as stated and
deliberately NOT ported; and the card counts NONCONSECUTIVE admissible tuples,
consecutiveness being DERIVED downstream (chain-v1 Lemma 4.3), never assumed.
The audit is therefore against the factor-2 band as frozen, never against a
stronger relative-accuracy statement.

### 2.2 The four comparison axes

Read off the verbatim statement, with `k = |H|` and `M_H(x) = modelMass H x`:

- Q-DOMAIN. `tupleCount H x` counts admissible starts in the CUMULATIVE range
  $`a\in[0,x]`$, never in a short window $`(x,x+\Phi(x)]`$ and never inside a
  residue class.
- Q-TUPLE. The counted object is a k-fold prime constellation
  $`\lbrace a+h:h\in H\rbrace`$ with $`0\in H`$, every offset EVEN, `H`
  admissible. At $`k=1`$ (`H = {0}`) and only there it degenerates to a
  single-prime count.
- Q-BAND. The tolerance is the TWO-SIDED FACTOR 2,
  $`M_H(x)/2\le\mathrm{tupleCount}(H,x)\le2M_H(x)`$: not an asymptotic
  $`(1+o(1))`$ and not a bound with an unquantified implied constant.
- Q-UNIF. The band is asserted UNIFORMLY over admissible even-offset `H` with
  $`k\le4\log{}\log{x}`$ and $`h\le(\log{x})^{3}`$ for every $`h\in H`$,
  eventually in x (one $`x_0`$ for all larger x).

A documented instance is DISJOINT exactly when at least one axis separates it
from these ranges, and INTERSECTS only when it lands inside all four AND
contradicts the Q-BAND inequality.

## 3. Three elementary lemmas

Finite algebra from the card's own definitions and the Section 1 quotation
rows; no campaign target is touched.

(L1) CAPACITY. For every `H`, every X and every set `S` of integers, altering
the primality pattern only inside `S` changes `tupleCount(H,X)` by at most
$`\lvert S\cap[0,X]\rvert`$, each removed or added start being one element of
`S`. So a mechanism whose ENTIRE carrier `S` satisfies
$`\lvert S\cap[0,X]\rvert<M_H(X)/2`$ cannot force either half of the Q-BAND
inequality to fail at `(H,X)`, whatever it asserts about the primes inside
`S`. PROVED (elementary).

(L2) MASS FLOOR, uniform over the whole Q-UNIF range. For every admissible `H`
in the card's range,
$$
M_H(x)\ \ge\ x\exp\bigl(-(4+o(1))(\log{}\log{x})^{2}\bigr)\ =\ x^{1-o(1)}.
$$
Proof. (i) $`(\log{x})^{k}=\exp(k\log{}\log{x})\le\exp(4(\log{}\log{x})^{2})`$
by Q-UNIF. (ii) $`\mathrm{S}(H)\ge e^{-Ck}`$ for an absolute C: in
$`\log{}\mathrm{S}(H)=\sum_p[\log{}(1-\nu_H(p)/p)-k\log{}(1-1/p)]`$, for
$`p\le2k`$ admissibility gives $`1-\nu_H(p)/p\ge1/p`$ while the second term is
non-negative, so the summand is $`\ge-\log{p}`$ and
$`\sum_{p\le2k}\log{p}\le2k\log{4}`$ (`Erdos251.sum_log_primesUpto_le`,
PROVED-LEAN in `lean/Erdos251/Mertens.lean`; the same order is RECORDED at
(q20)); for $`p>2k`$ one has $`\nu_H(p)\le k<p/2`$, hence
$`\log{}(1-\nu_H(p)/p)\ge-k/p-k^{2}/p^{2}`$ and $`-k\log{}(1-1/p)\ge k/p`$, so
the summand is $`\ge-k^{2}/p^{2}`$ and $`\sum_{p>2k}k^{2}/p^{2}\le k/2`$. Thus
$`\log{}\mathrm{S}(H)\ge-(2\log{4}+1/2)k`$, and with $`k\le4\log{}\log{x}`$,
$`\mathrm{S}(H)\ge(\log{x})^{-4(2\log{4}+1/2)}=x^{-o(1)}`$. PROVED. The same
floor is RECORDED independently in the card's module docstring ("in-budget
model masses are `x^{1-o(1)}`", chain-v1 Lemma 4.1); the audit does not rest on
that citation, having proved what it needs.

(L3) CARRIER DENSITY. Both documented constructions are matrices over the
primorial modulus, with carrier cardinality $`x^{1-1/D+o(1)}`$ at their own
scale `x`, for the fixed constant `D` each source names.

- A2 (q19): $`a_{rs}=rP(z)+s`$, $`R<r\le2R`$, $`y<s\le y+Tz`$,
  $`R=P(z)^{D-1}`$, $`x=P(z)^{D}=RP(z)`$; the row count is $`\le R+1`$ (q21)
  and each row is an interval of at most $`Tz+1`$ integers, so
  $`\lvert A\rvert\le(R+1)(Tz+1)=x^{1-1/D}(Tz+1)(1+o(1))`$. With `D > 1`
  RECORDED at (q15), `T` fixed with `k`, and $`z\asymp\log{x}`$ by (q20), this
  is $`x^{1-1/D+o(1)}`$.
- A1 (q8): $`a_{rs}=s+rP(z)`$, $`1\le s\le U`$,
  $`P(z)^{D-1}<r\le2P(z)^{D-1}`$, with $`U=[z^{\lambda_1}]`$ (q10) and
  $`x=a_l\asymp P(z)^{D}`$, so
  $`\lvert\mathfrak{M}\rvert\le P(z)^{D-1}U=x^{1-1/D}(\log{x})^{O(1)}`$ for
  every integer $`D\ge1`$ (at `D = 1` the matrix is a single row of
  polylogarithmic length).

PROVED from the documented parameters. The deficit is ARCHITECTURAL: the
carrier density is (row length)/`P(z)`, the row length is polynomial in z by
the sources' own choices ((q10); (q18)'s window `Kz`) while the modulus is the
primorial with $`\log{}P(z)\asymp z`$ (q20), so the density is
$`e^{-(1+o(1))z}=x^{-1/D+o(1)}`$ at every admissible parameter choice. Hence,
for every `H` in the card's range and every X at or above a carrier's scale,
$`\lvert\text{carrier}\cap[0,X]\rvert\le x^{1-1/D+o(1)}=o(M_H(X))`$, because
$`1/D`$ is a fixed positive constant while the mass floor loses only
$`x^{o(1)}`$. PROVED.

## 4. Task A -- the mechanisms, with their exact scope

### 4.1 M-OSC, the short-interval oscillation (A1)

Governing statement, verbatim (q1), A1 Section 2.1: "THEOREM. Let
$`\Phi(x)=(\log{x})^{\lambda_0}`$, $`\lambda_0>1`$. Then" followed by
$$
\limsup_{x\to\infty}\frac{\pi(x+\Phi(x))-\pi(x)}{\Phi(x)/\log{x}}>1
\quad\text{and}\quad
\liminf_{x\to\infty}\frac{\pi(x+\Phi(x))-\pi(x)}{\Phi(x)/\log{x}}<1,
$$
and (q2), the sharpened clause "For the range $`1<\lambda_0<e^{\gamma}`$ we
have even" with $`\limsup\ge e^{\gamma}/\lambda_0`$.

Scope, RECORDED with every qualifier carried. The object is the SHORT interval
$`(x,x+\Phi(x)]`$ of length $`(\log{x})^{\lambda_0}`$, $`\lambda_0>1`$ FIXED;
it counts SINGLE primes ($`\pi`$); the assertion is a limsup/liminf along
$`x\to\infty`$, i.e. existence of scales, not a statement at every scale; the
realizing construction (q7)-(q10) runs with `z` restricted to the sparse
good-modulus set of Lemma 1 and $`z\ge e^{cD}`$, `D` fixed depending at most on
$`\epsilon`$, and the extract's uniformity ledger states the restriction (q11):
"The variable z is not free". The third assertion holds only on
$`1<\lambda_0<e^{\gamma}`$. The sieve inputs (q13) -- Lemma 3 (Buchstab), for
FIXED $`\lambda>1`$ as a limit in z, and the sign-change Lemma 4 -- speak about
$`\Phi(x,y)=\lvert\lbrace n\le x:(n,P(y))=1\rbrace\rvert`$ and about
$`\omega(u)`$: counts of integers coprime to a primorial, prime-free. The
Theorem is proved in its source; this audit neither re-proves nor weakens it.

Axis reading: Q-DOMAIN short window; Q-TUPLE single primes; Q-BAND a
limsup/liminf separation from 1, with NO upper bound on the oscillation
amplitude anywhere in the extract; Q-UNIF fixed $`\lambda_0`$, fixed `D`, `z`
sparse.

### 4.2 M-ROW, the exceptionally prime-poor matrix rows (A2)

Governing statement, verbatim (q14), A2 Section 2.2: "The key idea is to
construct a matrix, whose rows are intervals of consecutive integers, and which
contains exceptionally few primes. The gaps between consecutive primes in the
rows of this matrix are therefore larger than normal."

Scope, RECORDED. The matrix is (q19); each row is an interval of $`Tz`$
consecutive integers at magnitude $`x=P(z)^{D}`$; the deficiency is engineered
by (q18) Lemma 4, which supplies ONE `y` with a factor-$`\delta`$ deficiency of
integers coprime to `P(z)` in every subwindow of $`(y,y+Kz]`$ of length at
least $`z/\log{z}`$ -- an INTEGER-SIEVE statement, prime-free, with `K` and
$`\delta`$ FIXED constants and the implied $`\asymp`$ constants absolute. The
prime floors are (q21): $`\ge3kR`$ primes in `A`, at most $`R+1`$ rows,
$`\ge\tfrac12kR`$ tuples (13) of CONSECUTIVE primes in good rows; the per-box
upper bound is (q22) via Lemma 3. The conclusion (q23) is a Lebesgue-measure
lower bound on the set of limit points of normalized consecutive-gap tuples,
with `k` a FIXED positive integer, `c(k)` depending only on k, T sufficiently
large, the Section-3 constants depending on k but not T; the source records
(q24) that "Our method is, like earlier methods, nonconstructive and yields
only the existence of (sufficiently many) limit points." The z are drawn from
Lemma 2's sparse set and the limit-point passage takes a subsequence (q25).

Axis reading: Q-DOMAIN a matrix of relative density $`x^{-1/D+o(1)}`$ inside
$`(x,3x]`$ (L3); Q-TUPLE consecutive-prime tuples and gap ratios at FIXED rank,
plus prime-free coprime counts; Q-BAND $`\gg`$, $`\ll`$, $`\asymp`$ with
implied constants absolute or depending on `k`, never a specific two-sided
factor; Q-UNIF fixed `k`, fixed `T`, `z` sparse and large in terms of T.

### 4.3 M-AP, the good-moduli arithmetic-progression inputs (A1 and A2)

Governing statements, verbatim. (q4) A1 Lemma 1: "LEMMA 1. There is a constant
$`C>0`$ such that, in terms of C, there exist arbitrarily large values of z for
which the modulus $`P(z)`$ is good." (q5) A1 Lemma 2 (Gallagher), the
good-modulus AP asymptotic, valid only "provided $`(a,q)=1`$, $`x\ge q^{D}`$,
and $`x/2\le h\le x`$, where $`\log{q}\ge D\ge D_0`$". (q15) A2 Lemma 1, the
good-modulus AP lower bound
$`\pi(2x,q,a)-\pi(x,q,a)\gg x/(\varphi(q)\log{x})`$ "uniformly for
$`x\ge q^{D}`$ and $`(a,q)=1`$", with "D is a constant $`>1`$ that depends only
on the constant C". (q16) A2 Lemma 2, existence of arbitrarily large good `z`.
(q17) A2 Lemma 3, the prime g-tuple AP upper bound
$`\ll_g R/(V(z)\log{R})^{g}`$ under the spacing hypothesis
$`0<\lvert s_i-s_j\rvert\le z^{2}`$, `g` a FIXED positive integer and "the
implied constant depends only on g".

Scope, RECORDED. Every AP input is stated for the SPECIFIC modulus `q = P(z)`
on the SPARSE good scales; the good-modulus definitions differ between the
sources (Section 11) and are carried, not smoothed; A1 Lemma 2 is an
equidistribution ASYMPTOTIC restricted to long ranges $`x/2\le h\le x`$ inside
one residue class; A2 Lemma 1 is a LOWER bound on single primes in one residue
class; A2 Lemma 3 is the corpus's ONLY tuple-counting statement and is an UPPER
bound with an existentially quantified, undocumented constant. The extract also
carries, inside A1 Lemma 2's proof line, the corpus's only cumulative-domain
prime statement, (q6): "the prime number theorem in the form
$`\pi(x)=\mathrm{li}\,x(1+O(e^{-\sqrt{\log{x}}}))`$."

## 5. Task B -- instance-by-instance mapping

Reading decision, disclosed: the instance set is the set of DOCUMENTED
FALSIFICATION INSTANCES of the three named mechanisms, which is what the
dispatch's Section 1 question and the V-37 rule quantify over. Positive
baseline statements consumed as inputs -- the PNT display (q6), A1's account of
Selberg's conditional almost-all result -- are NOT labeled: they are not
instances of a falsification mechanism, and the three labels are about
separation and contradiction. One consistency observation is recorded instead,
and it concerns the only documented statement that lands inside the card's
Q-DOMAIN at all: (q6) gives $`\pi(x)=\mathrm{li}\,x(1+o(1))`$, and since
$`\mathrm{li}\,x\sim x/\log{x}=M_{\lbrace0\rbrace}(x)`$ (the singular series of
$`H=\lbrace0\rbrace`$ is 1), the card's inequality at `k = 1` is IMPLIED by the
documented PNT for all large x. Where the corpus speaks cumulatively at all, it
agrees with the card.

### 5.1 The label table

| instance | documented object | carrier / domain | label | primary separator |
| --- | --- | --- | --- | --- |
| OSC-0 (q30) | the cited [9] failure of (1.1) at `Phi(x) = log x (lnln x ln_4 x/(ln_3 x)^2)` | one short window per scale | DISJOINT | Q-DOMAIN |
| OSC-1 (q1) | limsup of the short-window `pi`-ratio `> 1` | one short window per scale | DISJOINT | Q-DOMAIN |
| OSC-2 (q1) | liminf of the same ratio `< 1` | one short window per scale | DISJOINT | Q-DOMAIN |
| OSC-3 (q2) | limsup `>= e^gamma/lambda_0` on `1 < lambda_0 < e^gamma` | one short window per scale | DISJOINT | Q-DOMAIN |
| OSC-4 (q7)-(q10) | the realizing matrix, (3.1), the extracted row and subinterval | matrix, density `x^{-1/D+o(1)}` | DISJOINT | Q-DOMAIN |
| OSC-5 (q13) | Buchstab limit; the `omega - e^{-gamma}` sign change | integers coprime to `P(y)` | DISJOINT | Q-TUPLE |
| ROW-1 (q14) | rows with exceptionally few primes, larger-than-normal gaps | matrix, density `x^{-1/D+o(1)}` | DISJOINT | Q-DOMAIN |
| ROW-2 (q18) | Lemma 4: factor-`delta` coprime deficiency on `(y, y+Kz]` | window of length `Kz asymp T log x` | DISJOINT | Q-TUPLE |
| ROW-3 (q21) | the (11)/(12)/(14) prime and consecutive-tuple floors | inside the matrix | DISJOINT | Q-DOMAIN |
| ROW-4 (q22) | the per-box tuple upper bound (19) | one box, inside the matrix | DISJOINT | Q-DOMAIN |
| ROW-5 (q23) | positive Lebesgue measure of `S^{(k)}` in `[0,T]^k` | limit-point set in ratio space | DISJOINT | Q-TUPLE |
| BG-1 (q31) | cited limsup/liminf statements on `d_n/log n`, record `c = 0.248...` | consecutive-gap ratios | DISJOINT | Q-TUPLE |
| AP-1 (q4) | existence of arbitrarily large good moduli `P(z)` | no prime count at all | DISJOINT | Q-TUPLE |
| AP-2 (q5) | Gallagher AP asymptotic, `x/2 <= h <= x` | one residue class mod `P(z)` | DISJOINT | Q-DOMAIN |
| AP-3 (q15) | AP lower bound `>> x/(phi(q) log x)` | one residue class mod `P(z)` | DISJOINT | Q-DOMAIN |
| AP-4 (q16) | existence of arbitrarily large good moduli `P(z)` | no prime count at all | DISJOINT | Q-TUPLE |
| AP-5 (q17) | prime g-tuple AP upper bound, constant depending only on g | residue class, `R` rows, spacings `<= z^2` | DISJOINT | Q-BAND |

Seventeen instances, seventeen DISJOINT, no INTERSECTS, no UNDECIDED-IN-CORPUS.

### 5.2 The separations, written out

M-OSC (OSC-0 to OSC-4). PRIMARY SEPARATOR Q-DOMAIN, separating quantitatively
rather than by kind. The documented carrier at one scale is a single window of
length $`\Phi(x)=(\log{x})^{\lambda_0}`$ -- or, taking the whole realizing
device instead of the extracted window, the matrix $`\mathfrak{M}`$ of (L3)
with $`\lvert\mathfrak{M}\rvert=x^{1-1/D+o(1)}`$. By (L1) and (L2) neither can
move `tupleCount(H,x)` by as much as $`M_H(x)/2=x^{1-o(1)}/2`$, in either
direction, for any `H` in the card's range. SECONDARY SEPARATOR Q-TUPLE for
every `k >= 2`: the documented object is $`\pi`$, a single-prime count.
Q-TUPLE does NOT separate at `k = 1`, which is why Q-DOMAIN is named primary;
at `k = 1` the card's inequality is in addition implied by the documented PNT
(Section 5), so no true statement can contradict it there. PROVED, uniformly
in `H`.

OSC-5 and BG-1, the prime-free and gap-ratio rows. OSC-5 (q13) speaks about
$`\Phi(x,y)=\lvert\lbrace n\le x:(n,P(y))=1\rbrace\rvert`$, a count of integers
coprime to a primorial, and about $`\omega(u)`$, the Buchstab function: neither
mentions primes, so Q-TUPLE separates outright. BG-1 (q31) records the cited
limsup and liminf statements about the normalized consecutive gap
$`d_n/\log{n}`$, the record $`c=0.248\ldots`$ included; these constrain the
SPACING of consecutive primes, not the number of admissible starts $`a\le x`$
whose fixed even offset set is entirely prime, and the card never mentions
consecutiveness at all (it is derived downstream, Section 2.1). Q-TUPLE
separates, and nothing in those displays bounds any cumulative count in either
direction. PROVED.

M-ROW (ROW-1, ROW-3, ROW-4). PRIMARY SEPARATOR Q-DOMAIN by the same capacity
comparison: the entire matrix `A`, taken at its worst -- every cell void of
tuples, or every cell carrying one -- moves the cumulative count by at most
$`\lvert A\rvert=x^{1-1/D+o(1)}=o(M_H(x))`$. That is the strongest reading of
"exceptionally few primes" and it still does not reach. ROW-2 separates on
Q-TUPLE first: Lemma 4 counts integers coprime to `P(z)`, a prime-free
statement, and only on a window of length `Kz` (Q-DOMAIN second). ROW-5
separates on Q-TUPLE: a lower bound on the Lebesgue measure of a limit-point
set in gap-ratio space asserts nothing about `tupleCount(H,x)` for any fixed
`H` at any x, and (q24) records the method's nonconstructive character in the
source's own words. PROVED, uniformly in `H`.

M-AP (AP-1 to AP-5). AP-1 and AP-4 assert the existence of moduli with a
zero-free property; they constrain no prime count, so every axis separates and
Q-TUPLE is named primary. AP-2 and AP-3 constrain single primes inside ONE
residue class mod `P(z)`, of relative density $`1/P(z)=x^{-1/D}`$ in the card's
domain: Q-DOMAIN separates by (L1) and (L2), and summing AP-2 over the
$`\varphi(P(z))`$ classes recovers a PNT-type statement for a long range, again
agreeing with the card at `k = 1` rather than contradicting it. AP-5 is the
only instance whose object is a tuple count, and it separates on Q-BAND: its
tolerance is an implied constant "depend[ing] only on g" whose value the
extract does not document, and an upper bound with an existentially quantified,
unnamed constant is compatible with every specific two-sided factor -- it
cannot contradict the card's factor 2 in either direction. Q-DOMAIN separates
it a second time (one residue class, `R` rows). PROVED (from the documented
statement's own quantifier structure).

## 6. The mandatory Q-UNIF-edge pass

The verdict may not rest on the Q-DOMAIN separation read as a difference of
kind. The honest question: at the card's edge -- offset span up to
$`(\log{x})^{3}`$, tuple size up to $`4\log{}\log{x}`$ -- can a documented
short-window or sparse-row deficiency be SUMMED or TRANSPORTED onto the
cumulative even-offset tuple count?

(E1) The separation is uniform at the edge, and that is the whole answer.
(L2)'s floor is proved UNIFORMLY over the card's entire Q-UNIF range: the span
budget $`(\log{x})^{3}`$ does not enter it at all, and the rank budget
$`4\log{}\log{x}`$ enters only through $`(\log{x})^{-k}`$ and $`e^{-Ck}`$, both
$`x^{-o(1)}`$. The carriers of (L3) are smaller by a fixed power
$`x^{-1/D}`$. An $`x^{o(1)}`$ edge penalty cannot close an $`x^{1/D}`$ gap.
PROVED. The Q-UNIF edge is therefore not a soft face of the card: it is the
face on which the documented mechanisms are FURTHEST from reaching, since they
do not vary with `H` at all.

(E2) Summation does not help, and this is where a naive audit would go wrong.
Three summations were priced. (a) Over the subwindows of one row: the row is
the carrier already counted in (L3). (b) Over dyadic scales below x: the
carrier at scale $`x/2^{j}`$ has cardinality $`(x/2^{j})^{1-1/D+o(1)}`$ and
$`\sum_{j\ge0}(x/2^{j})^{1-1/D}=O(x^{1-1/D})`$ for `D > 1`, while at the
`D = 1` corner of A1 each scale contributes only a polylogarithmic carrier over
$`O(\log{x})`$ scales. (c) Over the admissible moduli at one scale:
$`P(z)\le x`$ forces $`z=O(\log{x})`$ by (q20), so at most $`O(\log{x})`$
values of z are available and the union of their matrices is still
$`x^{1-1/D+o(1)}`$. In all three the summed carrier stays $`o(M_H(x))`$.
PROVED.

(E3) The corpus's only tuple-counting statement cannot be applied at the span
edge at all. AP-5 (q17) requires $`0<\lvert s_i-s_j\rvert\le z^{2}`$. To use it
against the cumulative count one must partition $`[0,x]`$ into residue classes
mod `P(z)` with `R = x/P(z) >= 2`, hence $`P(z)\le x/2`$; by (q20)
$`\log{}P(z)\asymp z`$, so $`z=O(\log{x})`$ and the spacing budget is
$`z^{2}=O((\log{x})^{2})`$, while the card's span budget is $`(\log{x})^{3}`$,
which exceeds it for all large x. No `H` at the card's span edge is even
eligible for the only documented tuple bound. PROVED. This cuts toward
DISJOINT, not toward UNDECIDED: what fails is the documented mechanism's own
hypothesis, not the audit's ability to decide the instance.

(E4) The rank edge lies outside every documented quantifier. AP-5 fixes `g`,
A2's Theorem fixes `k`, A1's Theorem fixes $`\lambda_0`$ and `D`: no documented
instance quantifies over a rank growing with x, so none speaks at
$`k\to\infty`$, let alone at $`k\le4\log{}\log{x}`$. RECORDED. (What a
k-uniform carriage of the A2 chain would cost was priced by item-0036 under
named hypothesis rows; that verdict is neither re-opened nor used here.)

(E5) What a transport would have to look like, stated so the absence is
falsifiable. To threaten the card a mechanism must act on at least
$`M_H(x)/2=x^{1-o(1)}`$ starts $`a\le x`$ -- a set of relative density
$`x^{-o(1)}`$, not $`x^{-1/D}`$. Neither extract documents any statement about
a set of that size other than the PNT display (q6), which agrees with the card.
The obstruction is architectural (L3): the method's modulus is a primorial,
exponentially large in the window parameter, so its carriers are polynomially
thin by construction. Anything acting on a positive-density set would be a
different mechanism, not a scaled-up version of these.

(E6) NOT used as a separator, deliberately: the sparseness of the good-modulus
scale set. The card is universal in x above $`x_0`$, so a violation at a single
admissible scale, arbitrarily large, would falsify it, and scale sparsity
therefore separates nothing. The separation above is by MAGNITUDE at each
scale and holds at every scale the mechanisms occupy. This is a repair the
in-run refuter pass forced (Section 12, F2).

OUTCOME, in the dispatch's own third branch: the documented scopes demonstrably
cannot reach the cumulative even-offset tuple count within the card's ranges;
the "cannot reach" argument is (L1)+(L2)+(L3) with the summations of (E2),
support class PROVED from the documented parameters and the card's own
definitions, with one RECORDED input (q20) and one PROVED-LEAN input
(`sum_log_primesUpto_le`). No heuristic step enters.

## 7. The V-37 verdict rule and its mechanical application

Byte-fixed at the pin (dispatch Section 5), reproduced verbatim:

```text
V-37.
  (a) The verdict is CLEAR if and only if every documented instance is
      DISJOINT.
  (b) The verdict is INTERSECTS if at least one documented instance is written
      out as INTERSECTS.
  (c) Otherwise -- no instance INTERSECTS and at least one is
      UNDECIDED-IN-CORPUS -- the verdict is INCONCLUSIVE, and the verdict line
      NAMES the missing anchor(s).

Precedence is explicit: INTERSECTS (b) dominates INCONCLUSIVE (c); a
written-out intersection is a decided NO regardless of any undecided residue.
CLEAR (a) requires the full instance set DISJOINT with no undecided residue.
```

APPLICATION, clause by clause. The Task B label set is seventeen instances, all
DISJOINT (Section 5.1), zero INTERSECTS, zero UNDECIDED-IN-CORPUS. Clause (b)
does not apply: no instance lands inside all four axes, so no Q-BAND
contradiction is available to write out. Clause (c) does not apply: no instance
was left undecided by the corpus, so there is no missing anchor to name in the
verdict line. Clause (a) applies exactly.

EMISSION: V-37 = CLEAR. No falsification instance documented in the CLEAN A1
and A2 extracts contradicts any instance of the frozen `HLQuantA` statement
inside the card's own quantifier ranges. Support classes carried into the
emission verbatim from the body: the per-instance separations are PROVED
(Section 5.2) from the documented scopes ((q1)-(q29), RECORDED) plus the three
elementary lemmas of Section 3, of which (L2) additionally consumes one
PROVED-LEAN in-tree input; the Q-UNIF-edge pass returns the third branch with
support class PROVED (Section 6). No separator is heuristic. The emission is
about the DOCUMENTED zones only and does not assert that `HLQuantA` is true
(Section 10).

## 8. BET-16 material

`BET-20260804-16` (`ledger/bets.yaml`, `open:` block, resolve_by 2026-10-31)
registers: CLEAR resolves YES, INTERSECTS resolves NO, INCONCLUSIVE with a
named missing anchor voids the bet. The emitted verdict is CLEAR, so the bet's
material is a YES; the bet's claim ("no falsification instance documented in
the CLEAN maier85 and hm88 extracts contradicts any instance of the frozen
HLQuantA statement inside the card's own quantifier ranges") is the emission
line of Section 7 nearly word for word. Scoring is operator judgment against
this workpaper, NEVER in-run (rule 28(iii)): BET-20260804-16 STAYS OPEN for
operator judgment.

## 9. Rule-16(a) pass (verdict-vs-body clause diff, run before hand-off)

Each verdict clause diffed against the body's support classes. "Every
documented instance is DISJOINT" -- the seventeen rows of 5.1 with their
primary separators, each written out in 5.2, none promoted: the AP rows with
Q-TUPLE primary keep "constrains no prime count", the AP-5 row keeps
"unquantified implied constant" rather than any assumption about its value, and
the M-OSC rows keep Q-DOMAIN (not Q-TUPLE) as primary because Q-TUPLE fails to
separate at `k = 1`. "No instance is UNDECIDED" -- supported by 5.2 and (E3),
where the span-edge failure is of the mechanism's own hypothesis; the residual
extraction candidates of Section 13 are NOT missing anchors for any instance
and do not enter the verdict line. "Uniformly at the Q-UNIF edge" -- (L2) is
proved uniformly over the card's whole range and (E1) states the quantifier; no
clause claims uniformity the body does not prove. Scope qualifiers surviving
verbatim into the verdict: "documented", "inside the card's own quantifier
ranges", "the CLEAN A1 and A2 extracts". No verdict clause strengthens a body
support class; no body qualifier is dropped; nothing labeled RECORDED is cited
as PROVED. PASS.

## 10. Honest scope

This audit prices a risk against a corpus. It proves nothing about the primes
beyond the Section 3 lemmas and it does NOT establish that `HLQuantA` is true:
the card remains a hypothesis, OPEN, exactly as the round-1 conditional theorem
consumes it. The verdict is relative to two extracts -- CLEAR means no
DOCUMENTED instance in A1 and A2 reaches the card, not that no falsification
exists in the Maier genre at large. No verdict is recorded here on the
separator S1, on (CG), on B2.pairs or on the item-0010 campaign state; the
item-0029, item-0035 and item-0036 verdicts stand exactly as ANN-98, ANN-102
and ANN-103 booked them, and none was consumed as an input. No extract, extract
header, grade record, Lean file or frozen block was edited and no source was
opened. Any escalation beyond A1 and A2 is an operator-gated rule-26(5) event
and is not this item (Section 13).

## 11. The two documented extract differences, carried

Both are FLAGS the extracts themselves record; both are carried into the
mapping rather than smoothed.

- Characters. A1 (q3) defines a good modulus by "$`L(s,\chi\rvert\ne0`$ for all
  characters $`\chi`$ mod q"; A2 (q27) requires it only "for all nonprincipal
  characters $`\chi`$ mod q", and A2's FLAGS (q26) name the divergence: "a
  qualifier absent from the corresponding definition in Maier 1985, which says
  "all characters"". The two AP input families are therefore NOT
  interchangeable and no step of this audit maps one onto the other: AP-1/AP-2
  are read only against A1's definition, AP-3/AP-4/AP-5 only against A2's. No
  separator depends on either definition; what the separations use is the
  sparseness and the size of `P(z)`, which both definitions share.
- Modulus. A1 (q3), (q12): $`P(z)=\prod_{p<z}p`$, STRICT. A2 (q26), Section
  3.2: $`P(z)=\prod_{p\le z}p`$, NON-STRICT. The difference is one factor of at
  most `z`, i.e. at most $`\log{z}`$ in $`\log{}P(z)`$, and (L3) uses only
  $`\log{}P(z)\asymp z`$, which both satisfy; the carrier-density exponent
  $`1/D`$ is untouched. Priced here once, and used nowhere as an equivalence.

## 12. In-run adversarial refuter record (dispatch Section 6)

Before hand-off the run attacked its own draft with independent lenses --
separator validity, the Q-UNIF-edge transport, the UNDECIDED question, the
verdict emission. Findings SUSTAINED and the repairs they forced, disclosed
rather than absorbed:

- F1. The draft's first Q-DOMAIN argument was qualitative ("a short window is
  not a cumulative range") and would have been an unstated strengthening: with
  no lower bound on `M_H(x)` it does not exclude a window from swallowing the
  band. REPAIRED by proving (L2) and routing every separation through the
  capacity comparison (L1).
- F2. The draft used the sparseness of the good-modulus scale set as a
  separator. INVALID: the card is universal in x, so one admissible scale
  suffices to falsify it. REPAIRED; the sparse-scale clause is now RECORDED as
  scope and explicitly excluded from every separator ((E6)).
- F3. Q-TUPLE was named primary separator for M-OSC. INVALID at `k = 1`, where
  `H = {0}` makes the card a single-prime statement. REPAIRED: Q-DOMAIN primary
  throughout, Q-TUPLE secondary for `k >= 2`.
- F4. A comfort reading was drafted and REJECTED: that the documented
  oscillation amplitude $`e^{\gamma}/\lambda_0<e^{\gamma}<2`$ sits inside the
  card's factor 2. This misreads (q2), which lower-bounds a limsup and does not
  bound the oscillation from above; NOTHING in either extract bounds the
  amplitude. The audit rests on no such reading.
- F5. The AP-5 label was drafted UNDECIDED-IN-CORPUS on the ground that the
  implied constant is undocumented. Overturned against the anchor: the
  documented statement quantifies that constant existentially, so it carries no
  strength that could contradict a specific factor, and the instance is DECIDED
  (DISJOINT on Q-BAND). The undocumented constant is recorded as a residual
  (Section 13) instead, where it belongs -- it bounds what a SHARPER anchor
  could do, not what this one does.
- F6. The `D = 1` corner of A1's matrix (the exponent $`x^{1-1/D}`$
  degenerating to $`x^{0}`$) was checked rather than assumed away: at `D = 1`
  the matrix is a single row of length $`[z^{\lambda_1}]`$, so the carrier is
  polylogarithmic and the separation is stronger, not weaker.
- F7. Completeness of the instance set was attacked: the intro-level cited
  statements of both extracts were swept and two rows added (OSC-0, BG-1)
  rather than left implicit.

No sustained finding touched the emission. The rule-16(a) pass (Section 9) was
re-run after these repairs landed.

## 13. Residual uncertainty, and the both-readings entry

- The verdict is CORPUS-RELATIVE. Two escalations would test faces this corpus
  cannot: an explicit-constant sieve upper bound at growing `g` -- A2 (q17)
  names "[4, Theorem 2.3]" (Halberstam-Richert, Sieve methods) as a source for
  Lemma 3 but transcribes no constant -- and the Friedlander-Granville
  AP-uniformity zone named in `dossier/post-0029-design-notes.md` Section 3.2.
  NEITHER is a missing anchor for any instance (no instance was left undecided,
  so neither enters the V-37 verdict line under clause (c)); each is an
  operator-gated rule-26(5) extraction event, out of scope for this item, and
  named here so the residual is falsifiable rather than implicit.
- The card's own truth is untouched: `HLQuantA` is a hypothesis. This audit
  removes one named vacuity risk and supplies no evidence FOR the card.
- (L2)'s constant is crude on purpose ($`2\log{4}+1/2`$); every emitted
  statement is invariant under it, since it enters only an $`x^{o(1)}`$ factor.
- Both readings. *Supporting CLEAR:* every separation is quantitative and
  uniform in `H`; the capacity comparison holds at the extreme reading of each
  mechanism (every documented cell adverse); and the one axis where the corpus
  speaks cumulatively -- the PNT display -- agrees with the card.
  *Contradicting (mandatory seed):* the capacity argument is a statement about
  CARRIER SIZE, so it is silent about any mechanism acting on a positive-density
  set; if a future anchored statement produced Maier-type oscillation for a
  CUMULATIVE tuple count, or an explicit sieve constant below the model
  prediction at the card's rank, this verdict would not protect the card, and
  neither possibility is excluded by anything proved here. The audit's CLEAR
  prices the documented zone exactly, and no more.

END OF item-0037 VACUITY AUDIT WORKPAPER
