# item-0035 separator instance certificate

## 1. Header

Lane: EXECUTOR (local workstation, Claude Code; model string
claude-fable-5). Dispatch: `item-0035-kickoff-v1.md` v1 (ephemeral,
never committed; the operator apply of this run's outputs is the
ratifying commit; the operator-side sha256 of the dispatched file
is canonical). Pin: "the Section 0 pin" of the dispatch, verified
equal to HEAD at session start with an empty delta; all seven
dispatch anchors sha256-verified at start and close (Gates V1/V2/W4
of `item-0035-report.md`). Source layer (rule 26(4)): NO source
opened, no PDF opened. The primes half is consumed as the in-tree
PROVED object quoted verbatim in Section 2 (anchor A1,
`dossier/item-0029-workpapers/word-grain-adjudication.md`); the
reference-only extract anchor A7
(`dossier/item-0029-workpapers/extract/hildebrandmaier88-gaps.md`)
was NOT opened -- no source-facing sentence is authored here;
source display ids inside the verbatim (q3) quotation are carried
as part of that quotation, not consumed. Support classes:
PROVED (elementary/finite argument in this workpaper, from the
Section 3 definitions and the Section 4 numeric bounds on e alone);
RECORDED (verbatim quotation from a named in-tree anchor, never
strengthened, requantified, or stripped of a qualifier); MEASURED
(Section 10 script tables; finite range only).

## 2. The statement pair

The statement under pairing, at fixed rank $`k\ge3`$ (the item-0029
PROVED matrix conclusion, per the ratified acceptance intent):

> S(k): some flank class at rank k carries unboundedly many
> distinct realized middles along a scale sequence.

PRIMES INSTANCE (part (a) of the pair; CARRIED, not re-derived).
Verbatim from A1 Section 6, the S6 verdict's FAMILY-axis clause
(initial segment, extent fixed by the dispatch; support as there):

```text
FAMILY axis -- at fixed rank on sparse scales: EXISTENCE of flank
classes with two distinct realized middles, derivably unbounded
per-scale count, all but o(1) of the tuple mass non-rigid, PROVED
(finite algebra from hildebrandmaier88-gaps.md (14), the Section 4.2
column count, Lemma 3 and Mertens; adjudication Section 5.2, sheet
CM-5b)
```

with A1 Section 5.2 item 2, verbatim: "On all large good z
the heavy flank class cannot concentrate on one middle: it carries
derivably $`\gg z/(\log{z})^{k}`$ DISTINCT realized middles." The
class vocabulary is (q4) of the dispatch, verbatim from A1 Section 2
(fixed against `collision-gap-audit.md` B.1): "a WORD-GRAIN FLANK
CLASS is a realized flank class $`P`$ (members share one left flank
word of $`J`$ and one right flank word of $`K`$ consecutive prime
gaps; $`N_{P,d}`$ counts members with middle gap $`d`$); "two
distinct realized middles" means $`d\ne e`$ with $`N_{P,d}\ge1`$ and
$`N_{P,e}\ge1`$." So, for the primes, S(k) holds at every fixed
rank $`k\ge3`$ exactly as carried: on all large good $`z`$ of the
sparse good-modulus set, per scale, the heavy class of that scale
carries a derivably unbounded number of distinct realized middles
-- existence, per scale, no proportion claim; every qualifier binds.

MODEL INSTANCE (part (b) of the pair; THE ITEM; proved in Sections
4-6): in the even-Cramer-smooth model of Section 3, at every fixed
rank $`k\ge3`$ and every $`(J,K)`$, every realized model flank
class carries at most two distinct realized middles ((M-BOUND),
Section 5), so S(k) is FALSE there ((M-FALS), Section 6).

Quantifier mapping ((q3)-carried primes side vs proved model side):

| axis | primes instance (q3) | model instance |
| --- | --- | --- |
| rank | fixed rank $`k`$ | every fixed $`k\ge3`$, every $`(J,K)`$, $`J,K\ge1`$ |
| class grain | word-grain flank class (q4): shared left/right flank words, one middle gap | model flank class (Section 3): identical $`(a,c)`$ grain on the model gap sequence |
| middles / count | per-class distinct realized middles ($`d\ne e`$, both realized); two, with derivably unbounded per-scale count | $`\lvert\mathrm{mid}(P)\rvert`$: at most two, always |
| scale structure | sparse good-modulus scales $`z`$; the class may vary with the scale | full unfiltered sequence AND every truncation/sub-family (Section 3 inheritance remark) |
| class quantifier | EXISTENCE (some class, per scale) | UNIVERSAL (every realized class) |

The model bound is universal over classes, decompositions, and
sub-families, so it falsifies S(k) under every reading in which the
count is what ONE class carries at a scale -- fixed or
per-scale-varying, the count the primes instance carries; Section 6
makes the scope explicit and records the pooled quantity outside
it. Nothing about the primes is asserted beyond the quotation.

## 3. Model definitions fixed

The model, transcribed byte-identically from
`dossier/item-0010-workpapers/separator-repricing.md` W3.1 ((q1) of
the dispatch):

$$
q_1=2,\ q_2=3,\ q_3=5,\ q_4=7,\qquad
q_{n+1}=q_n+2\left\lceil\tfrac{\ln{}q_n}{2}\right\rceil\ (n\ge4)
$$

Model gap sequence: $`g_n:=q_{n+1}-q_n`$ for $`n\ge1`$.

Fix integers $`J\ge1`$, $`K\ge1`$; the rank is $`k=J+K+1\ge3`$. A
SITE at rank $`(J,K)`$ is an index $`i\ge1`$; its word is
$`(g_i,\ldots,g_{i+k-1})`$, with left flank
$`a=(g_i,\ldots,g_{i+J-1})`$, middle $`d=g_{i+J}`$, and right flank
$`c=(g_{i+J+1},\ldots,g_{i+J+K})`$. The MODEL FLANK CLASS of a pair
$`(a,c)`$ is the set of all sites carrying these flanks; a class is
REALIZED if it is nonempty. The realized middles of a class $`P`$
are $`\mathrm{mid}(P)=\lbrace g_{i+J}:i\in P\rbrace`$, counted over
the FULL infinite sequence, unfiltered.

TARGET (M-BOUND): for every $`(J,K)`$ with $`J,K\ge1`$ and every
realized model flank class $`P`$: $`\lvert\mathrm{mid}(P)\rvert\le2`$.

Inheritance remark (binding for Section 6): the bound is inherited
by every sub-family of sites (any scale truncation to $`q_i\le x`$
and any filtered variant), since restricting sites can only shrink
$`\mathrm{mid}(P)`$; the Section 6 falsification therefore covers
every "along a scale sequence" reading of the per-class count.

## 4. Structure lemmas

Numeric input, used only through four consequences:
$`2.71<e<2.72`$, hence $`7.34<e^{2}<7.40`$, $`53.8<e^{4}<54.8`$;
(n1) $`7\le e^{2}`$; (n2) $`9>e^{2}`$; (n3) $`53\le e^{4}`$; (n4)
$`57>e^{4}`$.

L1 (initial segment; PROVED by direct evaluation). $`g_1=1`$,
$`g_2=2`$, $`g_3=2`$ from the listed values $`2,3,5,7`$. The
recursion starts at $`n=4`$: $`g_n=2\lceil\ln{}(q_n)/2\rceil`$ for
all $`n\ge4`$. By (n1), $`0<\ln{}(7)/2\le1`$, so $`g_4=2`$ and
$`q_5=9`$; by (n2) and (n1), $`1<\ln{}(9)/2\le2`$, so $`g_5=4`$.

L1' (stretch description; (q2) transcribed with source, then
re-proved in one line). Verbatim from A1 Section 8 (RECORDED; PROVED
there, one line): "for $`n\ge4`$ and $`q_n\in(e^{2m-2},e^{2m}]`$ the
increment is exactly $`2m`$, so the model sequence from $`q_4`$ on
is, within each such range, an AP segment of difference $`2m`$ ("a
stretch"), each stretch multiplicatively long". One-line proof, so
this certificate is self-contained: for $`n\ge4`$,
$`g_n=2\lceil\ln{}(q_n)/2\rceil`$, and
$`\lceil\ln{}(q)/2\rceil=m`$ iff $`m-1<\ln{}(q)/2\le m`$ iff
$`e^{2m-2}<q\le e^{2m}`$. The description covers every $`n\ge4`$
(each $`q_n\ge7>1=e^{0}`$ lies in exactly one such range); the
pre-recursion gaps are exactly the L1 list $`g_1=1`$, $`g_2=g_3=2`$.

L2 (monotonicity and exact step sizes; PROVED). The consecutive
steps are: $`g_2-g_1=+1`$ (the one exceptional step);
$`g_3-g_2=0`$, $`g_4-g_3=0`$ (L1); and for every $`n\ge4`$,
$`g_{n+1}-g_n\in\lbrace0,+2\rbrace`$. Hence $`(g_n)_{n\ge1}`$ is
non-decreasing, and every step from an index $`n\ge2`$ is $`0`$ or
$`+2`$. Proof of the $`n\ge4`$ clause: $`g_{n+1}-g_n=
2(\lceil\ln{}(q_{n+1})/2\rceil-\lceil\ln{}(q_n)/2\rceil)`$, and the
ceiling difference is $`\ge0`$ ($`q_{n+1}>q_n`$) and $`\le1`$,
since $`\ln{}(q_{n+1})/2-\ln{}(q_n)/2<1`$: indeed
$`q_{n+1}=q_n+2\lceil\ln{}(q_n)/2\rceil\le q_n+\ln{}(q_n)+2<2q_n<
e^{2}q_n`$, where $`\ln{}(q)+2<q`$ for $`q\ge7`$ (true at $`q=7`$
since $`\ln{}(7)+2<4<7`$, and $`q-\ln{}(q)-2`$ increases for
$`q>1`$).

L3 (parity, value set, stretches; PROVED). (a) $`g_1=1`$ is the
only odd gap and the only gap of value $`1`$: $`g_2=g_3=2`$ and
$`g_n=2\lceil\cdot\rceil`$ is even for $`n\ge4`$. (b)
$`g_n\to\infty`$: $`q_n`$ strictly increases, so
$`g_n=2\lceil\ln{}(q_n)/2\rceil\to\infty`$. (c) Each attained value
$`v`$ has index set $`S_v:=\lbrace n\ge1:g_n=v\rbrace`$ a nonempty
FINITE interval (monotonicity; (b)). (d) The attained values are
exactly $`1`$ and every even $`2m`$, $`m\ge1`$: from $`g_2=2`$ the
sequence is non-decreasing, unbounded, with steps $`0/+2`$ (L2), so
no even value is skipped. (e) The intervals
$`S_1=\lbrace1\rbrace,S_2,S_4,S_6,\ldots`$ tile
$`\lbrace1,2,3,\ldots\rbrace`$ in this order; in particular, with
$`t_{2m}:=\max S_{2m}`$, $`\min S_{2m+2}=t_{2m}+1`$.

L4 (boundary uniqueness and pinning; PROVED). (a) For each
$`m\ge1`$ the adjacent pair $`(g_n,g_{n+1})=(2m,2m+2)`$ occurs at
exactly one index, $`n=t_{2m}`$; the pair $`(1,2)`$ occurs exactly
at $`n=1`$; no other unequal adjacent pair occurs (L2/L3: steps
from $`n\ge2`$ are $`0/+2`$, values are never skipped, each $`S_v`$
is one interval). (b) Pinning: a word containing at a known offset
an adjacent unequal pair -- or the value $`1`$ (L3(a): only at
index $`1`$) -- determines the absolute index of that entry by (a),
hence the site index $`i`$: at most ONE site realizes such a word
pattern.

L5 (stretch lengths; PROVED). (a) $`\lvert S_1\rvert=1`$: the named
exception, the only length-1 stretch in the whole sequence. (b)
$`S_2=\lbrace2,3,4\rbrace`$, length 3 (L1). (c)
$`S_4=\lbrace5,\ldots,16\rbrace`$, length 12, by enumeration:
$`q_5,\ldots,q_{16}=9,13,17,21,25,29,33,37,41,45,49,53`$, each in
$`(e^{2},e^{4}]`$ by (n2)/(n3), so each gap is $`4`$ (L1'); and
$`q_{17}=57>e^{4}`$ by (n4), so $`17\notin S_4`$. (d) For EVERY
$`m\ge2`$: $`\lvert S_{2m}\rvert\ge2`$. Proof: let
$`n_0=\min S_{2m}`$; then $`n_0\ge5`$ (L1), so $`n_0-1\ge4`$, and
the entry step is $`+2`$ (L2, L3(d)): $`g_{n_0-1}=2m-2`$, hence by
L1' $`q_{n_0-1}\le e^{2m-2}`$ and
$`q_{n_0}=q_{n_0-1}+2(m-1)\le e^{2m-2}+2(m-1)`$. Then
$`q_{n_0+1}=q_{n_0}+2m\le e^{2m-2}+4m-2\le e^{2m}`$, because
$`e^{2m-2}(e^{2}-1)>7^{m-1}\cdot6\ge6m>4m-2`$ (using $`e^{2}>7.34`$
and $`7^{m-1}\ge m`$, induction); also
$`q_{n_0+1}>q_{n_0}>e^{2m-2}`$ (L1' at $`n_0`$). So
$`q_{n_0+1}\in(e^{2m-2},e^{2m}]`$, giving $`g_{n_0+1}=2m`$ (L1')
and $`n_0+1\in S_{2m}`$. (e) Divergence (used only by Section 7):
while $`q_{n_0}+2mj\le e^{2m}`$ the indices $`n_0,\ldots,n_0+j`$
all lie in $`S_{2m}`$ (induction on $`j`$ with L1'), so
$`\lvert S_{2m}\rvert\ge(e^{2m}-q_{n_0})/(2m)\ge
(e^{2m}-e^{2m-2}-2(m-1))/(2m)>(3\cdot7^{m-1}-m+1)/m\to\infty`$:
for every bound $`B`$ there is $`m_1(B)`$ with
$`\lvert S_{2m}\rvert\ge B`$ for all $`m\ge m_1(B)`$. Consequence
of (a)-(d): every even value has stretch length $`\ge2`$.

## 5. Main bound (M-BOUND)

Fix $`(J,K)`$, $`J,K\ge1`$, and a realized class $`P`$ with flank
pair $`(a,c)`$. Complete case analysis; every case names the
lemmas it consumes. The dispatch's four case families map as: rigid
= C0; adjacent values = C1 (value-1 shapes dispatched by S0); two
or more steps apart = C2; a flank containing a step = S1 (S0 its
initial-segment refinement).

S0 (some flank entry equals 1). By L4(b) the site index is
determined: $`P`$ is a singleton, $`\lvert\mathrm{mid}(P)\rvert=1`$.
[Consumes L3(a), L4.]

S1 (some flank non-constant, no entry 1). The flank contains an
adjacent unequal pair at a known offset; by L4(b), $`P`$ is a
singleton, $`\lvert\mathrm{mid}(P)\rvert=1`$. [Consumes L2-L4.]

Otherwise both flanks are constant with no entry $`1`$: left value
$`w`$, right value $`w'`$, both even $`\ge2`$ (L3(a)); $`w'-w`$ is
even, and monotonicity (L2) across
$`g_{i+J-1}=w\le g_{i+J}\le g_{i+J+1}=w'`$ forces $`w\le w'`$.

C0 ($`w'=w`$; rigid). Every member's middle is squeezed to
$`w`$, so $`\mathrm{mid}(P)=\lbrace w\rbrace`$,
$`\lvert\mathrm{mid}(P)\rvert=1`$, whatever the member count.
[Consumes L2.]

C1 ($`w'=w+2`$; boundary class). Every member's middle satisfies
$`w\le g_{i+J}\le w+2`$ and $`g_{i+J}`$ is even (its index
$`i+J\ge2`$, so the value is not $`1`$; L3(a)), hence
$`g_{i+J}\in\lbrace w,w+2\rbrace`$ and
$`\lvert\mathrm{mid}(P)\rvert\le2`$. Structure, consumed by Section
7 and the script gate (ii): the left flank lies in $`S_w`$, so
$`i+J-1\le t_w`$; the right flank lies in $`S_{w+2}`$, so
$`i+J+1\ge\min S_{w+2}=t_w+1`$ (L3(e)); hence
$`P\subseteq\lbrace t_w-J,\ t_w+1-J\rbrace`$: at most two members,
at consecutive sites, with middles $`g_{t_w}=w`$ and
$`g_{t_w+1}=w+2`$. [Consumes L2, L3, L4.]

C2 ($`w'\ge w+4`$; empty). Suppose a member $`i`$ exists. Its last
left-flank index satisfies $`i+J-1\ge2`$ (index $`1`$ would put
$`g_1=1`$ in the flank, excluded here), so both steps across the
middle are $`0`$ or $`+2`$ (L2): $`w'-w\le4`$, with equality only
if both steps are $`+2`$, i.e.
$`(g_{i+J-1},g_{i+J},g_{i+J+1})=(w,w+2,w+4)`$; then
$`S_{w+2}=\lbrace i+J\rbrace`$ would be a length-1 stretch of the
even value $`w+2\ge4`$, contradicting L5. So $`w'-w\le2`$:
contradiction; the case is empty. [Consumes L2, L3, L5.]

CONCLUSION (M-BOUND, PROVED): for every $`(J,K)`$ with $`J,K\ge1`$
and every realized model flank class $`P`$,
$`\lvert\mathrm{mid}(P)\rvert\le2`$. Moreover a two-middle class
occurs only in case C1, with exactly two members, at consecutive
sites $`t_w-J`$ and $`t_w+1-J`$, middles $`w`$ and $`w+2`$ -- the
boundary form the Section 10 script gate (ii) checks.

## 6. Falsification (M-FALS)

Derivation, displayed. Reading scope, explicit: "carries" is a
per-class count -- the distinct middles ONE class, possibly varying
with the scale, realizes at one truncation; the (q3) count.

1. By (M-BOUND), $`\lvert\mathrm{mid}(P)\rvert\le2`$ for every
   realized class $`P`$ of the full sequence, every $`(J,K)`$.
2. By the Section 3 inheritance remark, the same bound holds for
   the classes of every truncation $`q_i\le x`$ and every filtered
   sub-family of sites.
3. Under every reading in scope, S(k) requires some class of some
   truncation to carry at least three distinct realized middles --
   contradicting 1-2.

Therefore, at every fixed rank $`k\ge3`$ and every $`(J,K)`$: no
model flank class carries three or more distinct realized middles,
a fortiori none carries unboundedly many along any scale sequence,
whether the class is held fixed or varies with the scale. S(k) is
FALSE in the model. (M-FALS) PROVED.

Recorded openly, outside the falsified scope: the POOLED union of
middles across DIFFERENT per-scale classes along a sequence is
infinite in the model (Section 7's boundary classes, pooled over
$`m`$, realize every large even value), as trivially for the
primes; no single class carries that union -- it is not what S(k)
asserts or (q3) proves; the pair separates at the per-class count.

Statement-level separator instance, assembled: S(k) is TRUE for
the primes at every fixed rank $`k\ge3`$ exactly in the carried
(q3) form (existence, sparse good-modulus scales, derivably
unbounded per-scale count, no proportion), and FALSE in the one
even-Cramer-smooth system of Section 3. No claim about the primes
beyond the Section 2 quotation; none about any other smooth model.

## 7. Sharpness (non-gating; delivered, PROVED)

For every $`(J,K)`$ there is $`m_0(J,K)`$ such that for every
$`m\ge m_0`$ the boundary class with left flank $`(2m)^{J}`$ and
right flank $`(2m+2)^{K}`$ realizes exactly the two middles
$`\lbrace2m,2m+2\rbrace`$. Proof. Take
$`m_0(J,K):=m_1(\max(J,K)+1)`$ from L5(e), so that both
$`\lvert S_{2m}\rvert`$ and $`\lvert S_{2m+2}\rvert`$ are
$`\ge\max(J,K)+1`$ for all $`m\ge m_0`$. Write $`t=t_{2m}`$. Site
$`i_1=t-J`$: left flank occupies $`t-J,\ldots,t-1\subseteq S_{2m}`$
(needs $`\lvert S_{2m}\rvert\ge J+1`$), middle $`g_t=2m`$, right
flank $`t+1,\ldots,t+K\subseteq S_{2m+2}`$ (needs
$`\lvert S_{2m+2}\rvert\ge K`$; L3(e)). Site $`i_2=t+1-J`$: left
flank $`t+1-J,\ldots,t\subseteq S_{2m}`$ (needs
$`\lvert S_{2m}\rvert\ge J`$), middle $`g_{t+1}=2m+2`$, right flank
$`t+2,\ldots,t+K+1\subseteq S_{2m+2}`$ (needs
$`\lvert S_{2m+2}\rvert\ge K+1`$). Both sites are members, so both
middles are realized; by C1 no other middle is possible: exactly
two. QED.

This is the fixed-rank transport of the (q5) precedent, RECORDED
verbatim from `separator-repricing.md` W3.2(b): "the non-rigid
classes number $`\sim\ln{}x/2`$ (one size-2 class per realized
gap-value step; `proofs.md` C4 step (4), audit-verified
computationally at $`10^6/5\times10^6/10^8`$), carrying
$`O(\ln{}x)`$ non-rigid sites" -- with the load-bearing squeeze
confinement of `proofs.md` C4 step (4) as its cited mechanism; the
precedent lives at the growing D0 depth, and this section proves
only its fixed-rank analogue (one two-member boundary class per
qualifying value step), claiming nothing at the D0 depth itself.

## 8. Non-transfer paragraph

Fixed rank only: every statement proved here quantifies over fixed
$`(J,K)`$ with $`J,K\ge1`$, i.e. fixed rank $`k=J+K+1\ge3`$. No
claim at the growing D0 depth: nothing here addresses
$`J=K=(1+o(1))\log_2{}\ln{}x`$ or any $`k`$ growing with the
scale; the D0-depth record remains the (q5) precedent. No verdict
on S1, (CG) or B2.pairs: this certificate neither states nor
implies any verdict on the separator S1, on (CG), on B2.pairs, or
on the item-0010 campaign state.

## 9. Discipline lines

Rule 15: NOT ENGAGED. Verbatim from
`dossier/post-0029-design-notes.md` Section 1.3 ((q8)): "not
engaged -- the statement is fixed-rank and no exchange-regime
constant enters; the note records this non-engagement explicitly
rather than silently."
Rule 12: not engaged -- no divergent-summation error term arises;
fixed-rank finite combinatorics of one deterministic sequence. D3
ex-ante no-go audit: PASS on record at the same anchor's Section
1.4; cited, not re-run.

## 10. MEASURED appendix (D2 script results)

Script: `model_word_census_35.py`; emitted tables:
`model_word_census_35_tables.txt`. Deterministic (two invocations,
byte-identical output; Gates W6), stdlib-only, no network,
single-threaded; range $`q_n\le10^{7}`$ (630405 terms, 630404
gaps); edge-safe ceiling rule stated in the script header (0
decimal fallbacks triggered); threshold self-check PASS (boundaries
reconstructed independently from $`\lfloor e^{2m}\rfloor`$ floors).
Every table is MEASURED; finite range only; no asymptotic claim.

| $`k`$ | $`(J,K)`$ | sites | classes | singletons | two-middle | max middles |
| --- | --- | --- | --- | --- | --- | --- |
| 3 | (1,1) | 630402 | 18 | 2 | 8 | 2 |
| 4 | (1,2) | 630401 | 25 | 9 | 8 | 2 |
| 4 | (2,1) | 630401 | 25 | 9 | 8 | 2 |
| 5 | (1,3) | 630400 | 32 | 16 | 8 | 2 |
| 5 | (2,2) | 630400 | 32 | 16 | 8 | 2 |
| 5 | (3,1) | 630400 | 33 | 18 | 7 | 2 |
| 6 | (1,4) | 630399 | 39 | 23 | 8 | 2 |
| 6 | (2,3) | 630399 | 39 | 23 | 8 | 2 |
| 6 | (3,2) | 630399 | 40 | 25 | 7 | 2 |
| 6 | (4,1) | 630399 | 40 | 25 | 7 | 2 |

Consistency gates: (i) max distinct middles $`\le2`$ in every row
-- PASS, no V-COUNTER material; (ii) every two-middle class found
has the Section 5 boundary form (two members, consecutive sites,
constant flanks $`w`$ / $`w+2`$, middles $`\lbrace w,w+2\rbrace`$,
left member ending at $`t_w`$) -- PASS in every row; each is listed
in full (flank words, boundary value, witnessing sites) in the
tables file. A measured observation, explained by the PROVED
Section 7 membership conditions and promoted to nothing: at
$`J\ge3`$ the $`2\to4`$ boundary contributes no two-middle class,
matching $`\lvert S_2\rvert=3<J+1`$.

## 11. Rule-16(a) clause-vs-body diff

Verdict-bearing clauses, diffed against the body's support classes
before hand-off. (M-BOUND): PROVED, body Section 5 (elementary
case analysis from the Section 3 definitions, the Section 4 lemmas
and the stated numeric bounds on e); Sections 2 and 6 claim
nothing stronger, and Section 6 falsifies the per-class count only
-- its pooled record subtracts from the claim, never adds.
(M-FALS): PROVED, displayed logic from (M-BOUND) plus the
inheritance remark; the falsified statement is the existential
S(k), not more. Primes instance: RECORDED, exactly the (q3)
support and qualifiers (fixed rank, sparse good-modulus scales,
existence with derivably unbounded per-scale count, no proportion,
non-rigid mass clause) -- quoted, never restated stronger; the
pairing instantiates (q3) at fixed $`k\ge3`$ and adds nothing.
Sharpness: PROVED, non-gating. Section 10 numbers: MEASURED with
the finite-range label, none promoted. No verdict clause
strengthens a body support class; no body qualifier is dropped.
Checked clause by clause.

## 12. Both-readings entry

Supporting reading. The bound is proved by a complete, elementary,
finite case analysis over a deterministic sequence, consuming only
the (q1) recursion, the Section 4 lemmas, and two-digit rational
bounds on $`e`$; the initial segment and every small stretch are
enumerated; the census at $`q_n\le10^{7}`$ returns max distinct
middles $`=2`$ in all ten decompositions, every two-middle class in
the proved boundary form -- proof and enumeration agree both ways.

Contradicting reading (the seed the dispatch mandates). The model
is ONE deterministic system -- an instance, not a theory of smooth
models: the certificate shows the paired statement CAN fail in a
system satisfying the project's unconditional tool list, not that
it fails in every Cramer-smooth system, and nothing selects the
model as canonical beyond its standing corpus role (A2 W3.1). The
primes side is consumed as RECORDED: whatever weakness its
qualifiers carry (sparse scales, existence only) is inherited, and
the pair is only as sharp as (q3).

## 13. Residual uncertainty and the BET-14 material

Residual uncertainty, named. (i) The numeric bounds on $`e`$ are
classical, consumed only through (n1)-(n4); a slip would surface
in the L5 enumerations, cross-checked in range by the script's
independent threshold reconstruction. (ii) The script is a finite
check; nothing asymptotic rests on it, and the proof rests on
nothing measured. (iii) The grade rests on this workpaper's own
elementary proofs; no source consumed (A7 unopened), no
extract-fidelity risk.

BET-20260804-14 material, NAMED (the bet is scored by the
operator, never in-run): this certificate is the resolution
material -- (M-BOUND) delivered PROVED at dossier grade for every
fixed rank $`k\ge3`$ (Section 5), the falsification (M-FALS) of
the item-0029 PROVED matrix conclusion displayed (Section 6), the
non-transfer paragraph present (Section 8). No fixed-rank class
with three or more distinct middles exists (Section 5) and none
was found by the census (Section 10): the kill criterion ((q7))
was not triggered.

END OF item-0035 SEPARATOR INSTANCE CERTIFICATE
