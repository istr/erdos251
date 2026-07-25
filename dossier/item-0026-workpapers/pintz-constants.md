# item-0026 workpaper: effectivizing the Pintz (1.8) span constants

Lane: EXECUTOR (local). Dispatch: `dispatch-pintz-constants-v1.md` v1
(ephemeral, uncommitted). This workpaper is a **computation and
effectivization** record: it closes extract FLAGS 3 and 6 of
`pintz10-singser.md`, prices the result on the anchored grid, and — where
a constant cannot be pinned from the printed proof — names the exact step
and carries the constant symbolically, per dispatch Section 9 and
STOP-AND-REPORT conditions 5/6.

Support classes used on every claim: `PROVED` (finite algebra / logic
carried out here), `MEASURED` (a value emitted by the Section 8 sheet),
`RECORDED` (verbatim from a byte-verified source), `OPEN` (could not be
pinned from the text).

---

## Section 0 — pin and rule-18 delta

Section 0 pin (dispatch): `97bf6d6195b99984d9a0cb87577c831662cbc26b`.

`HEAD` at session start and close equals the pin. Rule-18 check
(`git diff --name-only <pin>..HEAD`): **empty** — no bookkeeping delta and
no content-path delta. `RECORDED`.

`git status --short` at close carries only untracked paths: the two new
Section 8 files of this session, plus the pre-existing (not
session-authored) `dispatch-pintz-constants-v1.md` (ephemeral, never
committed) and `0001-writeup-mapper-repair.mbox` (unrelated, IDE-opened).
No tracked path is modified. `RECORDED`.

---

## Section 1 — gates (verbatim, session start == close)

`python3 lean/scripts/blocks.py check-frozen`:

```
  OK   erdos_251_irrational               lean/Erdos251/Statement.lean:18
  OK   HLQuantA                           lean/Erdos251/Hypotheses.lean:199
  OK   CramerGranville                    lean/Erdos251/Hypotheses.lean:210

FROZEN BLOCKS: all byte-identical.
```

`python3 lean/scripts/blocks.py relocation-check`:

```
RELOCATION CHECK PASSED -- concatenation is byte-identical to the old body.
```

Sorry census (`grep -rn '\bsorry\b' lean/ --include=*.lean`, proof terms):
exactly one, `lean/Erdos251/Statement.lean:21:  sorry`. `RECORDED`.

Mathlib pin: `lean/lake-manifest.json:8: "rev":
"a6276f4c6097675b1cf5ebd49b1146b735f38c02"` — intact. `RECORDED`.

`lean-toolchain` (`cat -A`): `leanprover/lean4:v4.16.0$` — single trailing
newline. `RECORDED`.

`roadmap/item-0026.md`: `status: ratified`. `RECORDED`.

Anchored sheets byte-identity at close: `git diff --stat` on
`dossier/item-0010-workpapers/budget_sheet_20_ext.py` and
`dossier/item-0020-workpapers/budget_sheet_20.py` is empty — both
unchanged. The new sheet neither imports nor overwrites either. `RECORDED`.

---

## Section 2 — evidence base sha256 (verified byte-identical before use)

| path | sha256 | booked-as (`payloads/HASHES.txt`) |
|---|---|---|
| `dossier/1004.1084v1.pdf` | `f730b045…39e5e5` | `https://arxiv.org/pdf/1004.1084v1` ✓ |
| `dossier/2210.09775v2.pdf` | `653dcd73…48939` | `https://arxiv.org/pdf/2210.09775v2` ✓ |

Full hashes verified equal:
`f730b045f1163bd539120e3e47237e92720e222d4663db1f86931d620739e5e5`
(1004.1084v1) and
`653dcd731f11c6bab47fa61989b31f50dc3318464fc4d300276698045ba48939`
(2210.09775v2). `RECORDED`. Governing displays below are quoted from the
byte-verified PDFs via their faithful transcriptions in
`pintz10-singser.md` and `kuperberg22-singseries.md` (rule 19).

---

## Section 3 — the governing chain (quoted, rule 19)

The object is the $`h`$-averaged relative one-position extension quotient
$`S_{\mathcal H}(H)`$. Pintz's setup (2.1), factorization (2.2), and the
three factor estimates, verbatim:

> "(2.1)  nu'_p := nu_p(calH'),  y := 5 log H / 6,
>        P := \prod_{p <= y} p,  Delta := \prod_{i=1}^{k} (h - h_i)."

> "(2.2)  S(calH')/S(calH) = \prod_p ( 1 - nu'_p/p ) / ( (1 - nu_p/p)(1 -
> 1/p) ) := \Pi_1 . \Pi_2 . \Pi_3  [with \Pi_1 over p <= y; \Pi_2 over
> p > y, p | Delta; \Pi_3 over p > y, p !| Delta …]."

> "For p !| Delta we have nu'_p = nu_p + 1, otherwise nu'_p = nu_p, hence
> (2.3)  \Pi_3 = \prod_{p>y} ( 1 + O(k/p^2) ) = 1 + O( k/(y log y) ),"

> "(2.4)  \Pi_2 = \prod_{p>y, p|Delta} (1 - 1/p)^{-1} = exp( O(
> \sum_{p>y, p|Delta} 1/p ) )."

> "Since by the Prime Number Theorem \sum_{p|Delta} log p <= log Delta <=
> 2ky, … (2.5)  \sum_{p|Delta, p>y} 1/p <= \sum_{y<p<4ky} 1/p <= log(
> log(5ky) / log y ) <= 2 eps."

> "(2.6)  \Pi_2 \Pi_3 (h) = 1 + O(eps)."

> "(2.7)  (1/P) \sum_{h=1}^{P} \Pi_1(h) = … = 1."

> "To prove Theorem 1' we can replace (2.4)-(2.5) with the trivial relation
> Pi_2 >= 1, thereby obtaining
> (2.8)  Pi_2 Pi_3 (h) >= { 1 + O(eps)  if k/(log H log_2 H) = O(eps),
>                         { c_1         if k/(log H log_2 H) <= c_3.
> This, together with (2.7) proves Theorem 1'."

The results themselves (RECORDED):

> "(1.7)  S_calH(H) >= 1 + O(eps)   if H >= exp( (1/eps) k/log k )
> and with some absolute constants c_1, c_2
> (1.8)  S_calH(H) >= c_1   if H >= exp( c_2 k/log k )."

### 3.0 One exact identity used throughout (PROVED)

For $`p\nmid\Delta`$ (so $`\nu'_p=\nu_p+1`$), write $`a=\nu_p/p`$,
$`b=1/p`$. The $`\Pi_3`$ factor is

$$\frac{1-(\nu_p+1)/p}{(1-\nu_p/p)(1-1/p)}=\frac{1-a-b}{(1-a)(1-b)}
=1-\frac{ab}{(1-a)(1-b)}=1-\frac{\nu_p}{(p-\nu_p)(p-1)}.$$

So, exactly,

$$1-(\Pi_3\text{ factor at }p)=\frac{\nu_p}{(p-\nu_p)(p-1)}.\qquad(\star)$$

`PROVED`. Everything in Q2–Q4 rests on when $`(\star)`$ is $`O(k/p^2)`$
(the printed (2.3) claim) and when it is not.

---

## Q1 — is `log_2 H` iterated or base-2? (extract FLAG 3)

**Resolution: iterated, $`\log_2 H=\log{}\log{}H`$. `PROVED`, and
self-consistent with (1.8).**

The denominator of (2.8) is fixed by the error term of (2.3), which is
$`k/(y\log{}y)`$ with $`y=5\log{}H/6`$ (2.1). Compute $`y\log{}y`$ with
$`u:=\log{}H`$:

$$y\log{}y=\frac{5u}{6}\log{}\!\Big(\frac{5u}{6}\Big)
=\frac{5u}{6}\big(\log{}u+\log{}(5/6)\big)
=\frac{5}{6}\,(\log{}H)(\log{}\log{}H)\Big(1+\frac{\log{}(5/6)}{\log{}\log{}H}\Big).$$

Thus $`y\log{}y=\tfrac56(\log{}H)(\log{}\log{}H)\,(1+o(1))`$, an object of
order $`(\log{}H)(\log{}\log{}H)`$. The paper's threshold ratio
$`k/(\log{}H\,\log_2{}H)`$ in (2.8) equals $`k/(y\log{}y)`$ up to the
constant $`\tfrac56`$ and the $`1+o(1)`$ **iff** $`\log_2{}H=\log{}\log{}H`$.
`PROVED`.

- **Iterated reading** ($`\log_2{}H=\log{}\log{}H`$): admissible rank in
  (2.8) is of order $`(\log{}H)(\log{}\log{}H)`$. `PROVED`.
- **Base-2 reading** ($`\log_2{}H=\log{}H/\log{}2`$): the denominator would
  be $`(\log{}H)^2/\log{}2`$, order $`(\log{}H)^2`$, which does **not**
  match $`y\log{}y\sim(\log{}H)(\log{}\log{}H)`$. `PROVED`.

**Self-consistency with (1.8).** Set $`H=\exp(c_2 k/\log{}k)`$, the (1.8)
threshold, so $`u=\log{}H=c_2 k/\log{}k`$ and
$`\log{}\log{}H=\log{}(c_2 k/\log{}k)=\log{}k\,(1+o(1))`$. Under the
iterated reading,

$$(\log{}H)(\log{}\log{}H)=\frac{c_2 k}{\log{}k}\cdot\log{}k\,(1+o(1))
=c_2 k\,(1+o(1)),$$

so the floor condition $`k\le c_3(\log{}H)(\log{}\log{}H)`$ becomes
$`k\le c_3 c_2 k\,(1+o(1))`$, i.e.

$$\boxed{c_2\,c_3=1+o(1).}\qquad\text{(iterated reading — consistent)}$$

Under the base-2 reading the same substitution gives
$`(\log{}H)^2/\log{}2=(c_2 k/\log{}k)^2/\log{}2`$, so the floor condition
would read $`H\ge\exp\!\big(c'\sqrt{k}\big)`$ — a $`\sqrt{k}`$ threshold,
irreconcilable with (1.8)'s $`k/\log{}k`$. `PROVED`.

**STOP condition 3 does not fire.** The two readings disagree with each
other (that is the ambiguity), but the proof (via $`y\log{}y`$) and (1.8)
**both** select the iterated reading; the (2.8) threshold *is* reconciled
with (1.8), under that reading, with $`c_2 c_3=1+o(1)`$. This confirms
extract FLAG 3's resolution-by-context and upgrades it to `PROVED`.

---

## Q2 — the threshold constant `c_3` (and `c_2`)

**Relation: `PROVED` — $`c_2=1/c_3+o(1)`$ (Q1). Absolute value: not
recoverable from the printed proof in the operative regime; STOP condition
6 finding, exact step named below.**

### 2a. What the printed chain gives when it is valid (PROVED)

For Theorem 1' the only change from Theorem 1 is $`\Pi_2\ge1`$; the floor
is carried entirely by $`\Pi_3`$ via (2.3). Using $`(\star)`$ and
$`\Pi_2\ge1`$,

$$\Pi_2\Pi_3(h)\ge\Pi_3(h)=\prod_{\substack{p>y\cr p\nmid\Delta}}
\Big(1-\frac{\nu_p}{(p-\nu_p)(p-1)}\Big).$$

*If every $`p>y`$ has $`\nu_p/p`$ bounded away from $`1`$* — concretely if
$`y\ge k`$, so that $`\nu_p\le k\le y<p`$ and hence $`p-\nu_p\ge p-k\ge
p(1-k/y)`$ — then, by $`(\star)`$,

$$0\le 1-(\Pi_3\text{ factor})=\frac{\nu_p}{(p-\nu_p)(p-1)}
\le\frac{k}{(1-k/y)\,p(p-1)}\le\frac{C_0}{1-k/y}\cdot\frac{k}{p^2},$$

with $`C_0=\big(1-1/p\big)^{-1}\le 2`$ for $`p\ge2`$ (here $`p>y`$ is
large, so $`C_0\to1`$). Summing and using
$`\sum_{p>y}p^{-2}=\tfrac{1}{y\log{}y}(1+o(1))`$ (partial summation on
$`\pi(t)`$; Rosser–Schoenfeld bounds $`\pi(t)`$ explicitly, giving the
constant), this is the effectivized form of (2.3):

$$-\log{}\Pi_3(h)\le\frac{C_0}{1-k/y}\cdot\frac{k}{y\log{}y}\,(1+o(1)).
\qquad(2.3')$$

Then the two regimes of (2.8) come out with explicit constants:

- **Asymptotic-1** ($`\ge1+O(\varepsilon)`$): holds once
  $`\tfrac{C_0}{1-k/y}\cdot\tfrac{k}{y\log{}y}\le C'\varepsilon`$.
- **Floor** ($`\ge c_1`$): holds once
  $`\tfrac{C_0}{1-k/y}\cdot\tfrac{k}{y\log{}y}\le\log{}(1/c_1)`$, i.e.
  using $`y\log{}y=\tfrac56(\log{}H)(\log{}\log{}H)(1+o(1))`$ and
  $`R:=k/(\log{}H\,\log{}\log{}H)`$,

$$R\le\frac{5}{6}\cdot\frac{(1-k/y)\log{}(1/c_1)}{C_0}\,(1+o(1))=:c_3,
\qquad c_2=\frac{1}{c_3}(1+o(1)).\qquad(2.3'')$$

So **the relation is `PROVED`**: $`c_2=1/c_3`$, and
$`c_3=\tfrac56(1-k/y)\log{}(1/c_1)/C_0`$ up to $`1+o(1)`$ — a clean
trade-off (Q3) *provided $`(2.3')`$ is legitimate*, which needs
$`k\le y`$ (in fact $`k`$ bounded away from $`y`$ for $`C_0/(1-k/y)`$ to be
absolute).

### 2b. Why the printed chain is not valid in the operative regime (finding)

The floor (1.8) and its proof-internal condition (2.8) live in the regime
$`k>y`$, not $`k\le y`$. At the (1.8) threshold $`H=\exp(c_2 k/\log{}k)`$,
$`y=\tfrac56\log{}H=\tfrac56 c_2 k/\log{}k`$, so

$$\frac{k}{y}=\frac{6\log{}k}{5\,c_2}\xrightarrow[k\to\infty]{}\infty.
\qquad(\dagger)$$

`PROVED`. For **any** fixed absolute $`c_2>0`$ and all large $`k`$,
$`k\gg y`$. Hence the interval $`(y,k]`$ is non-empty and, in fact,
contains almost all primes up to $`k`$ (since $`y\sim k/\log{}k`$). For a
prime $`p\in(y,k]`$ the bound $`(\star)=O(k/p^2)`$ **fails**: with
$`\nu_p`$ allowed up to $`p-2`$ (the largest value compatible with an
admissible extension via a free class, $`\nu'_p=\nu_p+1\le p-1<p`$),

$$1-(\Pi_3\text{ factor at }p)=\frac{\nu_p}{(p-\nu_p)(p-1)}
\ \xrightarrow{\nu_p=p-2}\ \frac{p-2}{2(p-1)}\to\frac12,$$

a per-factor deviation of order $`1`$, not $`O(k/p^2)=O(1/p)`$. Numerical
witness (star identity, $`p=11,\ \nu_p=9`$): factor
$`=1-\tfrac{9}{2\cdot10}=0.55`$, whereas $`O(k/p^2)`$ with $`k\approx p`$
predicts $`\approx0.09`$. `PROVED`.

**Existence of a tuple + admissible extension realizing the failure.**
By CRT one may prescribe, for each prime $`p`$ in a band around
$`k/\log{}k`$, that $`\mathcal H`$ occupy exactly $`p-2`$ residue classes
(avoid two) and that the extension $`h`$ lie in one of the two free
classes (so $`p\nmid\Delta`$, and $`\nu'_p=p-1<p`$: the extension is
admissible). For such an $`(\mathcal H,h)`$,

$$\Pi_3(h)\le\prod_{\substack{p\in(y,k]\cr\nu_p=p-2,\ h\text{ free}}}
\!\!\Big(\tfrac12+o(1)\Big)
=2^{-\,\Theta(k/(\log{}k)^2)}\longrightarrow0,$$

so $`\Pi_2\Pi_3(h)\ge c_1`$ with an absolute $`c_1>0`$ **fails pointwise**.
`PROVED`. The exact offending step is the passage

> "(2.3)  \Pi_3 = \prod_{p>y} ( 1 + O(k/p^2) ) = 1 + O( k/(y log y) ),"

used **pointwise for all $`h`$** to assert the floor line of (2.8). Its
per-factor bound tacitly assumes $`\nu_p/p`$ bounded from $`1`$, i.e.
$`p\gg k`$; that holds in Theorem 1's regime
($`H\ge\exp(k^{1/\varepsilon})`$ forces $`k\le u^{\varepsilon}\ll y`$) but
is contradicted by $`(\dagger)`$ in Theorem 1''s floor regime.

### 2c. Is the theorem wrong? No — but the fix is not in the text

The pointwise failure is on a set of $`h`$ of density $`o(1)`$ (the bad
$`h`$ must avoid $`\mathcal H`$ modulo each near-complete prime, a
$`\prod(2/p)\to0`$ event). Since those $`h`$ contribute
$`\ge0`$ to the average and $`\Pi_1`$ (small primes $`p\le y`$) is
CRT-independent of the large-prime event defining "bad", one expects

$$S_{\mathcal H}(H)=\tfrac1H\!\sum_h\Pi_1\Pi_2\Pi_3(h)
\ge c_1\cdot\tfrac1H\!\!\sum_{h\ \mathrm{good}}\!\!\Pi_1
=c_1\big(1-o(1)\big),$$

so **Theorem 1' is plausibly true as stated**. But this rescue replaces
Pintz's printed step "(2.8) pointwise $`\times`$ (2.7)" with an averaged
argument (good-$`h`$ density $`+`$ CRT independence of $`\Pi_1`$) that the
four-page note does not carry. Pinning $`c_1,c_2,c_3`$ as absolute
constants therefore requires redoing the $`\Pi_3`$ analysis across the band
$`y<p\le k`$ — a step absent from the text.

**Verdict (Q2).** `PROVED`: $`c_2=1/c_3`$, and in the *restricted* regime
$`k\le y`$ (equivalently $`H\ge\exp(\tfrac{6}{5}k)`$) the constant chain
$`(2.3')`$–$`(2.3'')`$ is explicit via Rosser–Schoenfeld. `OPEN`: the
absolute values of $`c_1,c_2,c_3`$ for the *stated* floor threshold
$`\exp(c_2 k/\log{}k)`$ are **not recoverable from the printed proof**,
because $`(\dagger)`$ forces the operative regime into $`k>y`$ where (2.3)
is invalid pointwise. This is the STOP condition 6 case: the printed
bookkeeping, taken literally, forces a dependence on the tuple structure
$`\mathcal H`$ (via the $`\nu_p`$ pattern on $`(y,k]`$) that the absolute
claim cannot absorb; the exact governing display is (2.3), quoted above.
The finding is reported, not folded into a table; no fabricated $`c_3`$ is
emitted.

---

## Q3 — the floor constant `c_1` as a function of `c_3`

**Trade-off (`PROVED`, valid where (2.3) is valid, i.e. $`k\le y`$):** from
$`(2.3'')`$, with $`C_0\to1`$ and $`k/y\to0`$ in the clean regime,

$$\log{}\frac{1}{c_1}=\frac{6}{5}\,C_0\,c_3\,(1+o(1)),
\qquad\Longleftrightarrow\qquad
c_1=\exp\!\Big(-\tfrac65 C_0\,c_3\Big)(1+o(1)).$$

Equivalently, in terms of the operative ratio,
$`c_1=\exp\!\big(-C_0\cdot\tfrac{k}{y\log{}y}\big)(1+o(1))`$. A larger
admissible rank (larger $`c_3`$) buys a smaller floor $`c_1`$, monotone and
smooth — the expected trade-off curve; the project may consume any point
of it **within the clean regime**. `PROVED`.

**But the curve does not reach the operative point.** The whole content of
Theorem 1' — the $`/\log{}k`$ improvement in the exponent over the trivial
$`\exp(\Theta(k))`$ threshold — lives in $`k>y`$ (see $`(\dagger)`$), where
the curve above is not certified. Delivering "the point the project
consumes" would require the Q2 rescue argument, which is `OPEN`. So the
trade-off is delivered **symbolically and regime-restricted**, not as a
single certified operative pair. `PROVED` (curve) + `OPEN` (its operative
endpoint).

---

## Q4 — the `O`-term in (1.7) (extract FLAG 6)

**Reading `≥ 1 − Cε`: textually forced. Constant `C`: `OPEN`, same
obstruction as Q2.**

(1.7) reads "$`S_{\mathcal H}(H)\ge1+O(\varepsilon)`$"; (2.6) reads
"$`\Pi_2\Pi_3(h)=1+O(\varepsilon)`$". The `O` in (2.6) is a two-sided
big-$`O`$, so "$`\ge1+O(\varepsilon)`$" **means** "$`\ge1-C\varepsilon`$
for some absolute $`C`$ and all small $`\varepsilon`$": the extract's
reading (FLAG 6) is the forced reading of the notation, not an
over-strengthening. `PROVED` (that the reading is textually forced).

Making $`C`$ explicit, however, inherits the Q2 obstruction. The (1.7)
regime is $`H\ge\exp((1/\varepsilon)k/\log{}k)`$, giving
$`k\le\varepsilon\,u\log{}k`$ and hence, for fixed $`\varepsilon`$,

$$\frac{k}{y}=\frac{6\varepsilon\log{}k}{5}\xrightarrow[k\to\infty]{}\infty,$$

so (1.7) is **also** in the $`k>y`$ regime and the constant in (2.3)/(2.6)
that feeds $`C`$ is not pinnable from the printed per-factor bound. The
$`\Pi_2`$ contribution via (2.4)–(2.5) *is* explicit — (2.5) reads
"$`\le\log{}(\log{}(5ky)/\log{}y)\le2\varepsilon`$", giving
$`\Pi_2=\exp(O(2\varepsilon))`$ with an absorbable constant — but the
$`\Pi_3`$ contribution is the same un-pinnable $`(2.3)`$ term. Hence
**$`C`$ cannot be pinned from the text**: `OPEN`, with the obstruction the
same governing display (2.3).

---

## Section 3 (dispatch) — pricing against the target (rule 15)

Conventions taken verbatim from `budget_sheet_20_ext.py` (re-declared, not
imported): scales $`x\in\lbrace10^{8},10^{20},10^{100},10^{1000}\rbrace`$;
grid rank $`k=L=(2/\ln{}2)\ln\ln{}x`$ and the D0-exact
$`L_{\mathrm{ceil}}=2J+1`$, $`J=\lceil\log_2{}\lceil13C_0A''\ln{}x\rceil\rceil`$;
window $`h=A'L\ln{}x`$, $`A'=1.5`$, $`A''=48`$, $`C_0=2/\ln{}3`$.

**Self-check (`MEASURED`).** The Section 8 sheet first reproduces the
anchored F17.9 column $`L\ln{}L/\ln\ln{}x`$:

| $`x`$ | F17.9 sheet | F17.9 anchored |
|---|---|---|
| $`10^{8}`$ | 6.1430 | 6.143 |
| $`10^{20}`$ | 6.9320 | 6.932 |
| $`10^{100}`$ | 7.9443 | 7.944 |
| $`10^{1000}`$ | 8.9629 | 8.963 |

Match to 3 dp; the sheet's conventions are anchor-faithful. `MEASURED`.

**Effectivization ceiling vs demand (`MEASURED`).** Because the printed
floor is certified only for $`k\le y=5\ln{}h/6`$ (Q2), the effectivization
ceiling is $`k_{\mathrm{adm}}=y`$. The grid demand $`k_{\mathrm{req}}`$ is
$`L`$ (grid) and $`L_{\mathrm{ceil}}`$ (D0-exact):

| $`x`$ | $`k_{\mathrm{req}}=L`$ | $`y=5\ln{}h/6`$ | headroom $`y/L`$ | $`k/y`$ | verdict |
|---|---|---|---|---|---|
| $`10^{8}`$ | 8.4065 | 4.5400 | 0.5401 | 1.8517 | **UNAVAILABLE** |
| $`10^{20}`$ | 11.0504 | 5.5314 | 0.5006 | 1.9977 | **UNAVAILABLE** |
| $`10^{100}`$ | 15.6942 | 7.1650 | 0.4565 | 2.1904 | **UNAVAILABLE** |
| $`10^{1000}`$ | 22.3381 | 9.3780 | 0.4198 | 2.3820 | **UNAVAILABLE** |

| $`x`$ | $`k_{\mathrm{req}}=L_{\mathrm{ceil}}`$ | $`y`$ | headroom $`y/L_{\mathrm{ceil}}`$ | $`L_{\mathrm{ceil}}/y`$ | verdict |
|---|---|---|---|---|---|
| $`10^{8}`$ | 31 | 4.5400 | 0.1465 | 6.8283 | **UNAVAILABLE** |
| $`10^{20}`$ | 33 | 5.5314 | 0.1676 | 5.9659 | **UNAVAILABLE** |
| $`10^{100}`$ | 37 | 7.1650 | 0.1936 | 5.1640 | **UNAVAILABLE** |
| $`10^{1000}`$ | 45 | 9.3780 | 0.2084 | 4.7985 | **UNAVAILABLE** |

**Classification: UNAVAILABLE in the tabulated range — grid-uniformly, and
worsening with scale.** `MEASURED`. The grid rank exceeds the split point
$`y`$ at every scale, $`k/y=1.85\to2.38`$ (grid) and $`4.8\to6.8`$
(D0-exact), rising. The window $`h=A'L\ln{}x`$ grows too slowly relative to
$`L`$ for growth alone ever to reach $`k\le y`$; the project sits squarely
in the regime where the printed floor is not effectivizable.

**Steering's authoring-time sensitivity is SUPERSEDED.** Steering reported
headroom $`1.10/1.14/1.18/1.22`$ growing like $`\ln\ln\ln{}h`$, from
$`k_{\mathrm{adm}}=c_3\ln{}h\,\ln\ln{}h`$ with $`c_3=1`$ **assumed** a valid
absolute constant. (The 1.10 is reproduced exactly:
$`\ln{}h\cdot\ln\ln{}h/L=5.448\cdot1.696/8.407=1.099`$ at $`10^{8}`$.) Q2
shows $`c_3`$ is not recoverable as an absolute constant from the printed
proof in this regime, so $`k_{\mathrm{adm}}=c_3\ln{}h\,\ln\ln{}h`$ has no
standing; the printed-proof ceiling is the regime boundary
$`k_{\mathrm{adm}}=y`$, which sits **below** demand. The corrected picture
inverts steering's conclusion: not growing headroom but a widening deficit.
`MEASURED`.

**Rule-12 landing (settled numerically).** The effectivized constant does
**not** land in the operative regime: neither an additive threshold shift
nor a leading-coefficient coupling, because the obstruction is a *regime
boundary* $`k>y`$, not an error term inside a convergent chain. Numerically
$`k/y`$ never approaches $`1`$ from above in or beyond the grid (it rises),
so there is no additive onset scale at which the floor becomes available.
`MEASURED`.

---

## Section 4 (dispatch) — Kuperberg's `(3 log k)^k` constant (secondary)

Delivered. The proof (Lemma 2.1 / (20)–(21), extract Section 8) does permit
making the constant explicit; the printed "3" drops a Mertens factor.

Governing displays (RECORDED):

> "(20)  S(H) << prod_{p<=k^3} 1/(1-1/p)^k prod_{p>k^3} (1-k/p)/(1-1/p)^k
> (k choose 2)^{-1} sum … exp( 2 (k choose 2) sum_{p|(h_i-h_j), p>k^3}
> 1/p )."

> "T_k(h) << h^k prod_{p<=k^3} 1/(1-1/p)^k << h^k (3 log k)^k, as desired."

The displayed step is $`\prod_{p\le k^3}(1-1/p)^{-1}\le 3\log{}k`$. By
Mertens' third theorem in explicit (Rosser–Schoenfeld) form,
$`\prod_{p\le z}(1-1/p)^{-1}=e^{\gamma}\log{}z\,(1+o(1))`$; at $`z=k^3`$,
$`\log{}z=3\log{}k`$, so

$$\prod_{p\le k^3}\Big(1-\tfrac1p\Big)^{-1}=e^{\gamma}\cdot3\log{}k\,(1+o(1))
=3e^{\gamma}\log{}k\,(1+o(1)),\qquad e^{\gamma}=1.781072\ldots$$

The honest displayed factor is $`3e^{\gamma}\log{}k\approx5.34\log{}k`$, not
$`3\log{}k`$; the printed $`(3\log{}k)^k`$ drops $`e^{\gamma}`$ per prime,
an $`e^{\gamma k}`$ loss overall. This is not absorbable into the absolute
$`\ll`$-constant (it is $`k`$-exponential). `PROVED` (algebra) + `MEASURED`
(exact finite product):

| $`x`$ | $`k=L`$ | exact $`\prod_{p\le k^3}(1-1/p)^{-1}`$ | $`3\ln{}k`$ | $`3e^{\gamma}\ln{}k`$ | $`\mathrm{exact}/(3\ln{}k)`$ |
|---|---|---|---|---|---|
| $`10^{8}`$ | 8.407 | 11.4270 | 6.3870 | 11.3757 | 1.7891 |
| $`10^{20}`$ | 11.050 | 12.8842 | 7.2074 | 12.8369 | 1.7876 |
| $`10^{100}`$ | 15.694 | 14.7423 | 8.2599 | 14.7114 | 1.7848 |
| $`10^{1000}`$ | 22.338 | 16.6124 | 9.3189 | 16.5976 | 1.7827 |

$`\mathrm{exact}/(3\ln{}k)\to e^{\gamma}`$: the exact product is
$`3e^{\gamma}\ln{}k`$.
`MEASURED`.

**Grid pricing, exponent $`\mathrm{expo}=\ln(\mathrm{cost})/\ln\ln{}x`$
(`MEASURED`), against the anchored F17.9 column:**

| $`x`$ | $`(3\ln{}k)^k`$ | $`(3e^{\gamma}\ln{}k)^k`$ | $`\mathrm{exact}^k`$ | F17.9 |
|---|---|---|---|---|
| $`10^{8}`$ | 5.3503 | 7.0158 | 7.0287 | 6.1430 |
| $`10^{20}`$ | 5.6990 | 7.3644 | 7.3751 | 6.9320 |
| $`10^{100}`$ | 6.0922 | 7.7577 | 7.7638 | 7.9443 |
| $`10^{1000}`$ | 6.4403 | 8.1058 | 8.1084 | 8.9629 |

The $`(3\ln{}k)^k`$ column reproduces steering's displayed-factor figures
$`5.350/5.699/6.092/6.440`$ exactly (steering **reproduced**, not
corrected — the arithmetic of $`(3\ln{}k)^k`$ is right; only the *constant*
$`3`$ is Mertens-loose). The Mertens-honest column is larger by
$`2\gamma/\ln{}2=1.6655`$ in expo (the dropped $`e^{\gamma k}`$), and both
grow like $`(2/\ln{}2)\ln(3e^{\gamma}\ln{}k)\sim\ln\ln\ln{}x`$:
Theorem 1.2's average-side upper bound is superpolylog at exchange depth
under **either** constant. `MEASURED`.

---

## Section 5 (dispatch) — what this settles and does not settle

Stated in the workpaper's own voice so it cannot be over-read downstream:

- **Direction.** Pintz's object is a **lower** bound on an *averaged*
  relative one-position extension quotient $`S_{\mathcal H}(H)`$. The
  direction of what is proved is recorded; whether the project's consuming
  route needs a lower or an upper bound here is an **open steering
  question**, not answered in this session. `RECORDED`.
- **Rank axis (A1), singular-series side.** A *favourable* effectivization
  would remove the rank axis as a blocker on the singular-series side only.
  This session does **not** deliver a favourable effectivization at the
  grid: Section 3 is **UNAVAILABLE grid-uniformly** (Q2/Q3 obstruction).
  Even the mathematically corrected Theorem 1' would say nothing about
  prime realizations. `RECORDED`.
- **The located absence (A3, the grain) is untouched.** The transfer from
  singular-series averages to consecutive-gap-word class masses
  $`N_{P,d}`$ is an A3 absence untouched by any value of $`c_1,c_2,c_3`$.
  Nothing here bears on it. `RECORDED`.
- **No verdict** on S1, on `CG`, or on the item-0010 campaign state is
  recorded in this session. `RECORDED`.

---

## Flags

- **F1 (Q1, resolves extract FLAG 3).** `log_2 H` in (2.8) is the iterated
  logarithm $`\log{}\log{}H`$; `PROVED` from $`y\log{}y`$ and cross-checked
  against (1.8) as $`c_2 c_3=1+o(1)`$. Extract FLAG 3 upgraded from
  resolved-by-context to `PROVED`.
- **F2 (Q2/Q3, STOP condition 6).** The printed step (2.3),
  "$`\Pi_3=\prod_{p>y}(1+O(k/p^2))=1+O(k/(y\log{}y))`$", used **pointwise**
  for the floor line of (2.8), is not valid in the operative regime: the
  floor threshold forces $`k/y=6\log{}k/(5c_2)\to\infty`$ $`(\dagger)`$, so
  primes $`p\in(y,k]`$ enter $`\Pi_3`$ with per-factor deviation $`O(1)`$
  (identity $`(\star)`$; witness $`p=11,\nu_p=9\Rightarrow0.55`$), and a
  CRT-constructible admissible $`(\mathcal H,h)`$ sends
  $`\Pi_2\Pi_3(h)\to0`$. Consequence: $`c_1,c_2,c_3`$ are **not
  recoverable as absolute constants from the printed proof**; the relation
  $`c_2=1/c_3`$ and the trade-off $`c_1=\exp(-\tfrac65C_0c_3)`$ hold only
  in the restricted regime $`k\le y`$ ($`H\ge\exp(\tfrac65 k)`$), a
  $`\exp(\Theta(k))`$ threshold, not the claimed $`\exp(c_2 k/\log{}k)`$.
  The theorem is plausibly still true via a good-$`h`$/CRT averaging
  rescue **absent from the four-page note**. Reported carefully with
  displays quoted; no fabricated constant emitted. `OPEN`.
- **F3 (Q4, extract FLAG 6).** The reading
  "$`\ge1+O(\varepsilon)`$" $`\Rightarrow`$ "$`\ge1-C\varepsilon`$" is the
  textually forced meaning of the two-sided $`O`$ in (2.6); `PROVED`. The
  value of $`C`$ is `OPEN`, inheriting the F2 obstruction ((1.7) is also in
  $`k>y`$).
- **F4 (Section 3).** Grid pricing **UNAVAILABLE grid-uniformly** and
  worsening; steering's $`1.10/1.14/1.18/1.22`$ growing-headroom
  sensitivity is **SUPERSEDED** (it assumed $`c_3=1`$ absolute). Rule-12
  landing: the constant does not land (regime boundary, not additive/
  coefficient). `MEASURED`.
- **F5 (Section 4).** Kuperberg's displayed $`3\log{}k`$ is Mertens-loose;
  the honest factor is $`3e^{\gamma}\log{}k\approx5.34\log{}k`$ (exact
  product $`/(3\ln{}k)\to e^{\gamma}`$). $`(3\ln{}k)^k`$ arithmetic
  reproduces steering's $`5.350/5.699/6.092/6.440`$; the honest column is
  $`+2\gamma/\ln{}2=1.666`$ in expo. Both superpolylog at exchange depth.
  `MEASURED`. This is a looseness in a displayed constant, **not** a proof
  gap: Theorem 1.2's $`\ll`$ already tolerates $`e^{O(k\log{}\log{}k)}`$
  (paper p. 2), which absorbs $`e^{\gamma k}`$.

---

## Section 8 (dispatch) — outputs and hashes

- `dossier/item-0026-workpapers/pintz-constants.md` (this file).
- `dossier/item-0026-workpapers/pintz_constants_sheet.py`
  sha256 `8980bc595ff30cbb251d8bb19b8787f1b4fba3126226d483dc7d2e2d19b5935f`;
  deterministic, re-run stable (two runs → identical table hash).
- `dossier/item-0026-workpapers/pintz_constants_sheet_tables.txt`
  sha256 `6f37598d3fa3fcdac4063a357de940a640af33052101cc0ebd8a1f026d3e2e57`.

The executor commits and pushes nothing; steering authors the ledger entry
post-run. Per STOP conditions 5/6 (F2), the constant-bearing questions
Q2–Q4 are reported with the exact obstructing step named and the constants
carried symbolically, rather than pinned to invented values.
