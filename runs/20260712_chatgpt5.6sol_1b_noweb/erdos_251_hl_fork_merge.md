# Erdős Problem #251: konditionale HL→Fork-Merge→Irrationalitäts-Kette

## Integritätsangaben zur Eingabedatei

- Eingabedatei: `1b_briefed.md`
- Dateigröße: **7.901 Bytes**
- SHA-256: **`5f6abc6f77e401ae040a60945d6b2b7060fd18913e8181edeea2b4a21394b4e4`**
- Webrecherche: **nicht verwendet**
- Literaturangaben aus dem Briefing: **UNVERIFIED**; keine davon wird als Beweisprämisse benutzt.

---

## 1. Ergebnis in einem Satz

Es wird eine vollständig quantifizierte, bewusst sehr starke Hardy–Littlewood-artige Hypothese `HL_quant` formuliert. Aus ihr folgt rigoros eine Fork-Merge-Folge `(FM)`; aus `(FM)` folgt rigoros die Irrationalität

\[
S=\sum_{n\ge 1}\frac{p_n}{2^n}.
\]

Damit ist die **konditionale** Kette

\[
\boxed{\mathrm{HL\_quant}\Longrightarrow (FM)\Longrightarrow S\notin\mathbb Q}
\]

vollständig. Nicht bewiesen ist `HL_quant` selbst. Der präzise offene Punkt ist insbesondere eine uniforme **bedingte erste Momentabschätzung für die binären Gap-Tails** auf exakten Primzahllücken-Zylindern der Länge `O(log log x)`.

---

## 2. Notation und elementare Identitäten

Es sei `p_n` die `n`-te Primzahl, mit `p_1=2`, und

\[
g_n:=p_{n+1}-p_n\qquad(n\ge 1).
\]

Weiter sei

\[
S:=\sum_{n\ge1}\frac{p_n}{2^n},
\qquad
\delta_n:=\sum_{j\ge1}\frac{g_{n+j}}{2^j}.
\]

Die Konvergenz folgt beispielsweise aus der elementaren Chebyshev-Abschätzung `p_n=O(n\log(n+1))`; für die eigentliche Fork-Merge-Argumentation genügt die Summierbarkeit der angezeigten Reihen.

### Claim C01 — Tail-Identitäten

Für alle `n\ge1` gilt

\[
\delta_{n+1}=2\delta_n-g_{n+1}.
\tag{2.1}
\]

Für `J\ge0` gilt daher

\[
\delta_{n+J}
 =2^J\delta_n-
 \sum_{i=1}^{J}2^{J-i}g_{n+i}.
\tag{2.2}
\]

Außerdem

\[
\sum_{n\ge1}\frac{g_n}{2^n}=S-2.
\tag{2.3}
\]

**Beweis.** Alle Aussagen folgen durch Indexverschiebung in absolut konvergenten Reihen. Für (2.1):

\[
2\delta_n
 =g_{n+1}+\sum_{j\ge1}\frac{g_{n+1+j}}{2^j}
 =g_{n+1}+\delta_{n+1}.
\]

Formel (2.2) folgt durch Iteration. Für (2.3) wird `g_n=p_{n+1}-p_n` eingesetzt und teleskopiert. ∎

Status: **proved**.

---

## 3. Rationalität erzwingt ein gerades Gitter

### Claim C02 — Eventuelle Ganzzahligkeit

Angenommen

\[
S=\frac{a}{2^s b},
\qquad a\in\mathbb Z,
\quad s\in\mathbb N,
\quad b\in\mathbb N_{>0}\text{ ungerade}.
\tag{3.1}
\]

Dann ist

\[
b\delta_n\in\mathbb Z
\qquad(n\ge s).
\tag{3.2}
\]

**Beweis.** Setze

\[
u_n:=\sum_{k\ge1}\frac{p_{n+k}}{2^k}.
\]

Dann ist

\[
2^nS
 =\sum_{r=1}^{n}p_r2^{n-r}+u_n,
\]

also `u_n=2^nS-A_n` mit einem `A_n\in\mathbb Z`. Da
`\delta_n=u_n-p_{n+1}`, folgt für `n\ge s`

\[
b\delta_n
 =a2^{n-s}-b(A_n+p_{n+1})\in\mathbb Z.
\]

∎

Status: **proved**.

### Claim C03 — Gerades Gitter

Unter (3.1) gilt sogar

\[
b\delta_n\in2\mathbb Z
\qquad(n\ge \max(s+1,2)).
\tag{3.3}
\]

**Beweis.** Aus (2.1) folgt

\[
b\delta_n=2b\delta_{n-1}-bg_n.
\]

Für `n\ge s+1` ist `b\delta_{n-1}` ganzzahlig. Für `n\ge2` ist `g_n` gerade, da beide beteiligten Primzahlen ungerade sind. Beide Terme auf der rechten Seite sind daher gerade. ∎

**[BRIEFING FACT USED: PARITY]** Dies ist genau die im Briefing genannte Paritätsverschärfung. Sie verdoppelt das Quantisierungsgitter von `2^J` auf `2^{J+1}`.

Status: **proved**.

---

## 4. Wiederholte Blöcke quantisieren den Tail-Unterschied

Ein Gap-Block der Länge `J` an der Stelle `n` ist

\[
(g_{n+1},\ldots,g_{n+J}).
\]

### Claim C04 — Repeated-block quantization

Seien `n,m\ge N`, wobei `b\delta_t\in2\mathbb Z` für alle `t\ge N`. Falls

\[
g_{n+i}=g_{m+i}\qquad(1\le i\le J),
\tag{4.1}
\]

dann gilt

\[
b(\delta_{n+J}-\delta_{m+J})\in2^{J+1}\mathbb Z.
\tag{4.2}
\]

Insbesondere erzwingt

\[
|\delta_{n+J}-\delta_{m+J}|<\frac{2^{J+1}}b
\tag{4.3}
\]

die exakte Gleichheit

\[
\delta_{n+J}=\delta_{m+J}.
\tag{4.4}
\]

**Beweis.** Setze `D_i:=\delta_{n+i}-\delta_{m+i}`. Wegen (2.1) und (4.1) ist

\[
D_i=2D_{i-1}\qquad(1\le i\le J),
\]

also `D_J=2^JD_0`. Da `bD_0` die Differenz zweier gerader ganzer Zahlen ist, liegt `bD_0` in `2\mathbb Z`. Folglich liegt `bD_J` in `2^{J+1}\mathbb Z`. Ein von null verschiedenes Element dieses Gitters hat Betrag mindestens `2^{J+1}`; daraus folgt (4.4). ∎

Status: **proved**.

---

## 5. Präzise Fork-Merge-Hypothese

### Definition FM

`(FM)` bedeutet: Es gibt Folgen

\[
(n_r,m_r,J_r,K_r,H_r)_{r\ge1}
\]

mit `n_r<m_r`, positiven ganzen `J_r,K_r`, reellen `H_r>0` und Gap-Wörtern

\[
W_r=(w_{r,1},\ldots,w_{r,J_r}),
\qquad
V_r=(v_{r,1},\ldots,v_{r,K_r}),
\]

sowie zwei verschiedenen zentralen Gaps `a_r\ne a'_r`, sodass:

1. **gemeinsamer Präfix**
   \[
   g_{n_r+i}=g_{m_r+i}=w_{r,i}
   \quad(1\le i\le J_r);
   \tag{FM1}
   \]

2. **Fork**
   \[
   g_{n_r+J_r+1}=a_r,
   \qquad
   g_{m_r+J_r+1}=a'_r,
   \qquad a_r\ne a'_r;
   \tag{FM2}
   \]

3. **gemeinsamer Suffix nach dem Fork**
   \[
   g_{n_r+J_r+1+i}=g_{m_r+J_r+1+i}=v_{r,i}
   \quad(1\le i\le K_r);
   \tag{FM3}
   \]

4. **vier kleine Tails**
   \[
   \max\!\left\{
   \delta_{n_r+J_r},\delta_{m_r+J_r},
   \delta_{n_r+J_r+K_r+1},
   \delta_{m_r+J_r+K_r+1}
   \right\}\le H_r;
   \tag{FM4}
   \]

5. **asymptotische Kleinheit**
   \[
   \min(n_r,m_r)\to\infty,
   \qquad
   \frac{H_r}{2^{J_r}}\to0,
   \qquad
   \frac{H_r}{2^{K_r}}\to0.
   \tag{FM5}
   \]

Diese Form enthält keine Forderung nach einem strikt positiven Tail-Unterschied vor dem Fork.

**[BRIEFING FACT RESPECTED: EXACT-LOCKING COUNTERMODEL]** Der Equal-run-Squeeze kann durch exaktes Locking ausfallen. `(FM)` benutzt stattdessen den erzwungenen nichtverschwindenden zentralen Gap-Unterschied; deshalb ist keine Anti-Locking-Klausel nötig.

**[BRIEFING FACT RESPECTED: PRIMORIAL OBSTRUCTION]** `(FM)` fordert keine langen konstanten Gap-Runs und keine Wiederholung eines festen Wortes mit wachsender Wiederholungszahl. Die verwendeten Wörter dürfen mit `r` wachsen. Die Primorial-Obstruktion wird daher nicht verletzt und wird im Beweis nicht als positive Existenzinformation benutzt.

---

## 6. Fork-Merge impliziert Irrationalität

### Claim C05 — Fork-merge contradiction

Aus `(FM)` folgt `S\notin\mathbb Q`.

**Beweis.** Angenommen `S\in\mathbb Q`. Schreibe `S=a/(2^sb)` wie in (3.1). Nach Claim C03 gibt es `N`, sodass `b\delta_t\in2\mathbb Z` für alle `t\ge N`.

Wegen `(FM5)` kann `r` so groß gewählt werden, dass

\[
n_r,m_r\ge N,
\qquad
H_r<\frac{2^{J_r+1}}b,
\qquad
H_r<2^{K_r+1}.
\tag{6.1}
\]

Aus `(FM1)`, Claim C04 und `(FM4)` folgt

\[
|\delta_{n_r+J_r}-\delta_{m_r+J_r}|
\le H_r
<\frac{2^{J_r+1}}b.
\]

Daher

\[
\delta_{n_r+J_r}=\delta_{m_r+J_r}.
\tag{6.2}
\]

Ein Schritt über den Fork liefert mit (2.1)

\[
\begin{aligned}
\delta_{n_r+J_r+1}-\delta_{m_r+J_r+1}
&=(2\delta_{n_r+J_r}-a_r)
 -(2\delta_{m_r+J_r}-a'_r)\\
&=a'_r-a_r.
\end{aligned}
\tag{6.3}
\]

Über den gemeinsamen Suffix verdoppelt sich der Unterschied in jedem Schritt. Somit

\[
\delta_{n_r+J_r+K_r+1}
-\delta_{m_r+J_r+K_r+1}
=2^{K_r}(a'_r-a_r).
\tag{6.4}
\]

Für hinreichend großes `r` liegen beide zentralen Gaps hinter `p_2`; sie sind daher gerade. Aus `a_r\ne a'_r` folgt

\[
|a'_r-a_r|\ge2.
\]

Also ist der Betrag der linken Seite von (6.4) mindestens `2^{K_r+1}`. Andererseits sind beide Tails positiv und nach `(FM4)` höchstens `H_r`; damit ist ihr Abstand höchstens `H_r`. Wegen (6.1) ist das unmöglich. Folglich ist `S` irrational. ∎

Status: **proved**.

---

## 7. Vollständig quantifizierte Hypothese `HL_quant`

Die folgende Hypothese ist absichtlich stärker als eine gewöhnliche Hardy–Littlewood-Primtupelvermutung. Sie enthält neben uniformen exakten Gap-Zählungen eine bedingte erste Momentabschätzung für `\delta`. Gerade diese Momentklausel ist der entscheidende, gegenwärtig unbewiesene Input.

Alle Logarithmen in diesem Abschnitt sind natürliche Logarithmen.

### 7.1 Exakte Gap-Zylinder

Für ein Wort positiver gerader Zahlen

\[
w=(d_1,\ldots,d_\ell)
\]

setze

\[
h_0=0,
\qquad
h_i=d_1+\cdots+d_i,
\qquad
\mathcal H(w)=\{h_0,\ldots,h_\ell\}.
\]

Sei

\[
\mathcal I(w)=\{1,\ldots,h_\ell-1\}\setminus\mathcal H(w).
\]

Ein Auftreten von `w` bei `n` bedeutet

\[
g_{n+i}=d_i\qquad(1\le i\le\ell).
\]

Äquivalent sind `p_n+h_i` für alle `h_i\in\mathcal H(w)` prim und alle dazwischenliegenden `p_n+t`, `t\in\mathcal I(w)`, nicht prim.

Definiere

\[
\operatorname{Occ}_X(w)
:=\{n:X\le p_n<2X,\ g_{n+i}=d_i\ (1\le i\le\ell)\}
\]

und

\[
N_X(w):=|\operatorname{Occ}_X(w)|.
\]

### 7.2 Hardy–Littlewood-Modellmasse

Für eine endliche Menge `A\subset\mathbb Z` sei

\[
\mathfrak S(A)
:=\prod_q
\left(1-\frac{\nu_A(q)}q\right)
\left(1-\frac1q\right)^{-|A|},
\]

wobei `\nu_A(q)` die Anzahl der von `A` modulo `q` belegten Restklassen ist. Ist `A` nicht zulässig, wird `\mathfrak S(A)=0` gesetzt.

Die formale exakte-Gap-Modellmasse ist die vollständige Inclusion-Exclusion

\[
\mathcal M_X(w)
:=\sum_{A\subseteq\mathcal I(w)}(-1)^{|A|}
\mathfrak S(\mathcal H(w)\cup A)
\int_X^{2X}
\prod_{h\in\mathcal H(w)\cup A}
\frac{dt}{\log(t+h)}.
\tag{7.1}
\]

Diese Formel dient nur zur Festlegung des vorhergesagten Hauptterms. Die Hypothese behauptet die Uniformität direkt für **exakte Gap-Zylinder**; sie wird nicht aus einer nur für beschränkte Primtupelgröße bekannten Formel abgeleitet.

### 7.3 Uniformitätsbereich

Fixiere die Konstanten

\[
\kappa=2,
\qquad C_{\rm win}=6,
\qquad A_{\rm err}=20.
\]

Für `X>e^e` sei `\mathcal W_X` die Menge aller Wörter `w=(d_1,\ldots,d_\ell)` mit

\[
1\le\ell\le C_{\rm win}\log\log X,
\tag{7.2}
\]

\[
d_i\in2\mathbb N_{>0},
\qquad
\max_i d_i\le(\log X)^3,
\qquad
\sum_i d_i\le(\log X)^3.
\tag{7.3}
\]

Damit sind sowohl die Zahl der aufeinanderfolgenden Gaps als auch alle räumlichen Shifts vollständig spezifiziert:

- Gap-Fenster: höchstens `6 log log X` Gaps;
- räumliche Verschiebungen: höchstens `(log X)^3`;
- relativer Fehlergewinn: `(log X)^{-20}`.

### 7.4 Die vier Klauseln von `HL_quant`

Es existieren absolute Konstanten `X_0>e^e` und `B\ge1`, sodass für jedes `X\ge X_0` Folgendes gilt.

#### HLQ1 — Uniforme exakte Gap-Zählung

Für jedes `w\in\mathcal W_X` mit `\mathcal M_X(w)>0` gilt

\[
|N_X(w)-\mathcal M_X(w)|
\le
\frac{\mathcal M_X(w)}{(\log X)^{20}}.
\tag{HLQ1}
\]

#### HLQ2 — Uniformes bedingtes erstes Tail-Moment

Für jedes `w\in\mathcal W_X`, jedes `0\le t\le |w|` und `\mathcal M_X(w)>0` gilt

\[
\sum_{n\in\operatorname{Occ}_X(w)}\delta_{n+t}
\le
B\log X\;\mathcal M_X(w)
\left(1+\frac1{(\log X)^{20}}\right).
\tag{HLQ2}
\]

Dies ist eine statistische Mischungs-/Momentklausel. Sie sagt, dass das Konditionieren auf ein exaktes Gap-Wort der Länge `O(log log X)` den mittleren geometrisch gewichteten Zukunftstail nicht über die natürliche Größenordnung `O(log X)` aufbläht.

#### HLQ3 — Fork-reiche Modellfamilie

Setze

\[
r(X):=\lfloor2\log\log X\rfloor.
\tag{7.4}
\]

Dann existieren Wörter `W_X,V_X` der Länge `r(X)` und verschiedene positive gerade Zahlen `a_X\ne a'_X`, sodass

\[
w_X:=W_X\,a_X\,V_X,
\qquad
w'_X:=W_X\,a'_X\,V_X
\tag{7.5}
\]

beide in `\mathcal W_X` liegen und

\[
\mathcal M_X(w_X),\ \mathcal M_X(w'_X)
\ge
X\exp\!\bigl(-20(\log\log X)^2\bigr).
\tag{HLQ3}
\]

Die rechte Seite geht gegen unendlich. Diese Klausel ist eine exakt formulierte Zulässigkeits-/Nichtdegenerationsforderung für zwei Modellzylinder mit demselben Präfix und Suffix, aber verschiedenen zentralen Gaps.

#### HLQ4 — Uniformität der Konstanten

Dieselben Konstanten `X_0,B,6,20` gelten gleichzeitig für sämtliche Wörter und Offsets in (7.2)–(7.5).

### 7.5 Wo jede Uniformität ausgegeben wird

- `C_win=6` wird benutzt, weil `|W_Xa_XV_X|=2r(X)+1\le 5\log\log X` für großes `X`.
- Die Shift-Schranke `(log X)^3` wird benutzt, damit beide Fork-Wörter im erlaubten räumlichen Fenster liegen.
- Der relative Fehler `(log X)^{-20}` in `HLQ1` wird nur benutzt, um `N_X(w)\ge\tfrac12\mathcal M_X(w)>0` zu erhalten.
- Derselbe Fehler in `HLQ2` wird beim Übergang vom Modellhauptterm zum bedingten Durchschnitt benutzt.
- Die Untergrenze in `HLQ3` zeigt, dass die Zylinder nicht nur formal positiv sind, sondern sehr viele erwartete Auftreten besitzen. Für die reine Existenz aus dem relativen Fehler wäre Positivität bereits ausreichend.
- Die Wahl `\kappa=2` wird genau in
  \[
  2^{r(X)}\asymp(\log X)^{2\log2}
  \]
  ausgegeben; da `2\log2>1`, dominiert diese Größe den Tail-Bound `O(log X)`.

---

## 8. Beweis `HL_quant ⇒ FM`

### Claim C06 — `HL_quant` erzeugt Fork-Merge-Konfigurationen

Unter `HL_quant` gilt `(FM)`.

**Beweis.** Sei `X\ge X_0` groß genug, dass

\[
\varepsilon_X:=(\log X)^{-20}\le\frac12.
\]

Wähle nach `HLQ3` die beiden Wörter

\[
w=W\,a\,V,
\qquad
w'=W\,a'\,V,
\qquad a\ne a',
\]

mit `|W|=|V|=r=\lfloor2\log\log X\rfloor`.

Nach `HLQ1` gilt für `q\in\{w,w'\}`

\[
N_X(q)\ge(1-\varepsilon_X)\mathcal M_X(q)>0.
\tag{8.1}
\]

Für `q=w` wende `HLQ2` bei den beiden Indexoffsets `t=r` und `t=2r+1` an. Dann

\[
\sum_{n\in\operatorname{Occ}_X(w)}
\bigl(\delta_{n+r}+\delta_{n+2r+1}\bigr)
\le
2B\log X\,\mathcal M_X(w)(1+\varepsilon_X).
\tag{8.2}
\]

Division durch (8.1) zeigt, dass der Durchschnitt über `\operatorname{Occ}_X(w)` höchstens

\[
2B\log X\frac{1+\varepsilon_X}{1-\varepsilon_X}
\le6B\log X
\tag{8.3}
\]

ist. Also gibt es ein Auftreten bei einem Index `n=n(X)` mit

\[
\delta_{n+r}+\delta_{n+2r+1}\le6B\log X.
\tag{8.4}
\]

Insbesondere sind beide Tails einzeln höchstens `6B\log X`.

Dasselbe Argument für `w'` liefert einen Index `m=m(X)` mit

\[
\delta_{m+r},\delta_{m+2r+1}\le6B\log X.
\tag{8.5}
\]

Die Indizes `n` und `m` sind verschieden, denn am selben Index kann der zentrale Gap nicht zugleich `a` und `a'` sein. Vertausche sie nötigenfalls, sodass `n<m`.

Setze

\[
J_X=K_X=r(X),
\qquad
H_X=6B\log X.
\tag{8.6}
\]

Die Wortdefinition liefert `(FM1)`–`(FM3)`, und (8.4)–(8.6) liefern `(FM4)`. Da `p_n,p_m\ge X`, gehen `n,m` mit `X` gegen unendlich.

Schließlich ist

\[
2^{r(X)}
\ge\frac12\exp(2\log2\,\log\log X)
=\frac12(\log X)^{2\log2}.
\tag{8.7}
\]

Daher

\[
\frac{H_X}{2^{J_X}}
=\frac{H_X}{2^{K_X}}
\le
12B(\log X)^{1-2\log2}
\longrightarrow0,
\tag{8.8}
\]

weil `1-2\log2<0`. Entlang beispielsweise `X_j=\lceil\exp(\exp j)\rceil` erhält man die in `(FM)` verlangte Folge. ∎

Status: **proved, conditional on HL_quant**.

### Korollar C07 — Primäres Ziel

\[
\boxed{\mathrm{HL\_quant}\Longrightarrow (FM)\Longrightarrow S\notin\mathbb Q.}
\]

Status: **proved, conditional on HL_quant**.

**[BRIEFING FACT NOT USED: EMPIRICS]** Die numerischen Befunde unter `3\cdot10^7` werden in keinem Beweisschritt verwendet.

**[BRIEFING FACT NOT USED: STATISTICS NO-GO]** Bloße PNT-artige Globalstatistik wird nicht verwendet. Die entscheidende Klausel `HLQ2` ist ausdrücklich auf primspezifische exakte Gap-Zylinder konditioniert.

---

## 9. Lean-4-orientierte Formulierung

Der folgende Code ist als formal präzises Implementierungsskelett gedacht. Er ist **nicht gegen eine konkrete Mathlib-Version kompiliert**; insbesondere können Namen für `Nat.nth`, Primzahl-Monotonie, `Irrational`, Summierbarkeit und `Tendsto` geringfügig angepasst werden müssen.

### 9.1 Nullbasierte Definitionen

```lean
noncomputable section

open scoped BigOperators Topology
open Filter

-- q 0 = 2, q 1 = 3, ...
def q (n : ℕ) : ℕ := Nat.nth Nat.Prime n

def gap (n : ℕ) : ℕ := q (n + 1) - q n

-- Entspricht dem einbasierten δ_n bei q n = p_{n+1}.
def delta (n : ℕ) : ℝ :=
  ∑' j : ℕ, (gap (n + j) : ℝ) / (2 : ℝ) ^ (j + 1)

def erdosSeries : ℝ :=
  ∑' n : ℕ, (q n : ℝ) / (2 : ℝ) ^ n

-- Das S der Aufgabenstellung ist erdosSeries / 2.
def S : ℝ := erdosSeries / 2

def SameBlock (n m J : ℕ) : Prop :=
  ∀ i, i < J → gap (n + i) = gap (m + i)

def BlockCode (n J : ℕ) : ℕ :=
  ∑ i in Finset.range J, 2 ^ (J - 1 - i) * gap (n + i)
```

### 9.2 `delta_block`

```lean
theorem delta_block (n J : ℕ) :
    delta (n + J)
      = (2 : ℝ) ^ J * delta n
        - ∑ i in Finset.range J,
            (2 : ℝ) ^ (J - 1 - i) * (gap (n + i) : ℝ) := by
  induction J with
  | zero => simp
  | succ J ih =>
      -- Benötigt zuerst delta (n+1) = 2*delta n - gap n.
      -- Danach ih, Indexarithmetik und ring.
      sorry
```

### 9.3 `rational_delta_eventually_lattice`

Es ist formal bequemer, die Paritätsverschärfung direkt in die Aussage aufzunehmen.

```lean
def IsRationalReal (x : ℝ) : Prop :=
  ∃ r : ℚ, (r : ℝ) = x

theorem rational_delta_eventually_lattice
    (hS : IsRationalReal S) :
    ∃ b : ℕ, 0 < b ∧ Odd b ∧
      ∃ N : ℕ, ∀ n ≥ N,
        ∃ z : ℤ, (b : ℝ) * delta n = (2 : ℝ) * z := by
  -- 1. Schreibe S = a / (2^s*b), b ungerade.
  -- 2. Benutze 2^n*S = ganzzahliger Präfix + u_n.
  -- 3. Erhalte b*delta n ∈ ℤ ab n≥s.
  -- 4. Nutze gap n gerade ab n≥1 und die Rekursion,
  --    um b*delta n ∈ 2ℤ ab n≥s+1 zu erhalten.
  sorry
```

### 9.4 `repeated_block_quantization`

```lean
theorem repeated_block_quantization
    {b n m J : ℕ}
    (hb : 0 < b)
    (hn : ∃ zn : ℤ, (b : ℝ) * delta n = (2 : ℝ) * zn)
    (hm : ∃ zm : ℤ, (b : ℝ) * delta m = (2 : ℝ) * zm)
    (hblock : SameBlock n m J) :
    ∃ z : ℤ,
      (b : ℝ) * (delta (n + J) - delta (m + J))
        = (2 : ℝ) ^ (J + 1) * z := by
  -- Subtrahiere zweimal delta_block.
  -- Wegen hblock heben sich die BlockCodes auf.
  -- Die Startdifferenz liegt in 2ℤ.
  sorry
```

### 9.5 Fork-Merge-Struktur

```lean
structure ForkMergeAt
    (n m J K : ℕ) (H : ℝ) : Prop where
  n_lt_m : n < m
  prefix : SameBlock n m J
  fork_ne : gap (n + J) ≠ gap (m + J)
  suffix : SameBlock (n + J + 1) (m + J + 1) K
  H_pos : 0 < H
  tail_n_fork : delta (n + J) ≤ H
  tail_m_fork : delta (m + J) ≤ H
  tail_n_end : delta (n + J + 1 + K) ≤ H
  tail_m_end : delta (m + J + 1 + K) ≤ H

def SmallTailForkMerge : Prop :=
  ∃ n m J K : ℕ → ℕ, ∃ H : ℕ → ℝ,
    (∀ r, ForkMergeAt (n r) (m r) (J r) (K r) (H r)) ∧
    Tendsto n atTop atTop ∧
    Tendsto m atTop atTop ∧
    Tendsto (fun r => H r / (2 : ℝ) ^ (J r)) atTop (𝓝 0) ∧
    Tendsto (fun r => H r / (2 : ℝ) ^ (K r)) atTop (𝓝 0)
```

### 9.6 `fork_merge_contradiction`

```lean
theorem fork_merge_contradiction
    {b n m J K : ℕ} {H : ℝ}
    (hb : 0 < b)
    (hlat_n : ∃ zn : ℤ, (b : ℝ) * delta n = (2 : ℝ) * zn)
    (hlat_m : ∃ zm : ℤ, (b : ℝ) * delta m = (2 : ℝ) * zm)
    (hfm : ForkMergeAt n m J K H)
    (hprefix_small : H < (2 : ℝ) ^ (J + 1) / b)
    (hsuffix_small : H < (2 : ℝ) ^ (K + 1))
    (hn_large : 1 ≤ n)
    (hm_large : 1 ≤ m) : False := by
  -- A. repeated_block_quantization + |fork tail difference|≤H
  --    liefert delta(n+J)=delta(m+J).
  -- B. Ein Rekursionsschritt liefert Unterschied der zentralen Gaps.
  -- C. hfm.suffix multipliziert diesen Unterschied mit 2^K.
  -- D. Prim-Gaps ab Index 1 sind gerade; fork_ne gibt Betrag ≥2.
  -- E. Endtails sind positiv und ≤H, also Abstand ≤H; Widerspruch.
  sorry
```

### 9.7 `erdos_251_of_small_tail_fork_merge`

```lean
theorem erdos_251_of_small_tail_fork_merge
    (hFM : SmallTailForkMerge) : Irrational erdosSeries := by
  intro hrat
  have hSrat : IsRationalReal S := by
    -- S = erdosSeries / 2; Rationalität ist unter Division durch 2 stabil.
    sorry
  obtain ⟨b, hb, hbod, N, hlattice⟩ :=
    rational_delta_eventually_lattice hSrat
  obtain ⟨n, m, J, K, H, hcfg, hnTop, hmTop, hJsmall, hKsmall⟩ := hFM
  -- Wähle r groß mit n r,m r≥N und beiden Kleinheitsungleichungen.
  -- Wende fork_merge_contradiction an.
  sorry
```

Damit ist das vom Briefing verlangte Endziel:

```lean
theorem erdos_251
    (hHL : HLQuant) :
    Irrational
      (∑' n : ℕ, (Nat.nth Nat.Prime n : ℝ) / (2 : ℝ) ^ n) := by
  exact erdos_251_of_small_tail_fork_merge
    (hl_quant_implies_small_tail_fork_merge hHL)
```

### 9.8 Lean-seitige Repräsentation von `HL_quant`

Für die Formalisierung wird die explizite analytische Definition der Modellmasse (7.1) zweckmäßig von den vier logisch benutzten Feldern getrennt. Das folgende Schema bildet den **vollen Quantorenbereich** ab; `modelMass` ist dabei anschließend durch die formalisierte Inclusion-Exclusion (7.1) zu instanziieren.

```lean
structure GapWord where
  entries : List ℕ

def GapWord.len (w : GapWord) : ℕ := w.entries.length

def GapWord.span (w : GapWord) : ℕ := w.entries.sum

def GapWord.InWindow (X : ℕ) (w : GapWord) : Prop :=
  0 < w.len ∧
  (w.len : ℝ) ≤ 6 * Real.log (Real.log X) ∧
  (∀ d ∈ w.entries, 0 < d ∧ Even d ∧
      (d : ℝ) ≤ (Real.log X) ^ 3) ∧
  (w.span : ℝ) ≤ (Real.log X) ^ 3

def OccursAt (w : GapWord) (n : ℕ) : Prop :=
  ∀ i, i < w.len → gap (n + i) = w.entries.get ⟨i, by assumption⟩

def OccSet (X : ℕ) (w : GapWord) : Finset ℕ :=
  -- Indizes n mit X ≤ q n < 2X und OccursAt w n.
  sorry

def occCount (X : ℕ) (w : GapWord) : ℕ := (OccSet X w).card

-- Durch die vollständige Inclusion-Exclusion (7.1) zu definieren.
def modelMass (X : ℕ) (w : GapWord) : ℝ := sorry

def tailMoment (X t : ℕ) (w : GapWord) : ℝ :=
  ∑ n in OccSet X w, delta (n + t)

structure HLQuantFull : Prop where
  X0 : ℕ
  B : ℝ
  B_pos : 0 < B

  count_uniform :
    ∀ X ≥ X0, ∀ w,
      w.InWindow X → 0 < modelMass X w →
      |(occCount X w : ℝ) - modelMass X w|
        ≤ modelMass X w / (Real.log X) ^ 20

  tail_first_moment :
    ∀ X ≥ X0, ∀ w t,
      w.InWindow X → t ≤ w.len → 0 < modelMass X w →
      tailMoment X t w
        ≤ B * Real.log X * modelMass X w
          * (1 + 1 / (Real.log X) ^ 20)

  fork_rich :
    ∀ X ≥ X0,
      ∃ W V : GapWord, ∃ a a' : ℕ,
        W.len = ⌊2 * Real.log (Real.log X)⌋₊ ∧
        V.len = ⌊2 * Real.log (Real.log X)⌋₊ ∧
        0 < a ∧ Even a ∧ 0 < a' ∧ Even a' ∧ a ≠ a' ∧
        let w  := ⟨W.entries ++ [a]  ++ V.entries⟩
        let w' := ⟨W.entries ++ [a'] ++ V.entries⟩
        w.InWindow X ∧ w'.InWindow X ∧
        (X : ℝ) * Real.exp (-20 * (Real.log (Real.log X)) ^ 2)
          ≤ modelMass X w ∧
        (X : ℝ) * Real.exp (-20 * (Real.log (Real.log X)) ^ 2)
          ≤ modelMass X w'
```

Die rein operationale Konsequenz kann zusätzlich als kleinere Schnittstelle gespeichert werden:

```lean
structure HLQuantOperational : Prop where
  B : ℝ
  B_pos : 0 < B
  X0 : ℕ
  fork_words :
    ∀ X ≥ X0,
      ∃ r n m : ℕ, ∃ H : ℝ,
        r = ⌊2 * Real.log (Real.log X)⌋₊ ∧
        ForkMergeAt n m r r H ∧
        H ≤ 6 * B * Real.log X
```

Dann ist

```lean
theorem hl_quant_implies_operational
    (hHL : HLQuantFull) : HLQuantOperational := by
  -- HLQ1 liefert nichtleere OccSet-Mengen.
  -- HLQ2 bei t=r und t=2r+1 liefert je ein gutes Auftreten.
  -- HLQ3 liefert gemeinsamen Präfix/Suffix und verschiedene Zentralgaps.
  sorry

theorem hl_quant_implies_small_tail_fork_merge
    (hHL : HLQuantFull) : SmallTailForkMerge := by
  have hop := hl_quant_implies_operational hHL
  -- Setze X_j = ceil(exp(exp j)) und benutze 2^(floor(2 loglog X))
  -- ≥ (1/2)*(log X)^(2 log 2).
  sorry
```

Der mathematische Beweis dieses Übergangs ist vollständig in Abschnitt 8 angegeben. Die `sorry`-Stellen betreffen die noch auszuführende Mathlib-Codierung, nicht eine logische Lücke in der konditionalen Papierargumentation.

---

## 10. Sekundärroute: `v₂`-Blöcke

Für

\[
C_{n,J}:=\sum_{i=1}^{J}2^{J-i}g_{n+i}
\]

gilt nach Claim C01

\[
\delta_{n+J}=2^J\delta_n-C_{n,J}.
\tag{10.1}
\]

### Claim C08 — `v₂`-Block-Untergrenze

Angenommen `S=a/(2^sb)` mit ungeradem `b` und `n\ge s`. Dann

\[
b\delta_{n+J}\ge 2^{\min(J,v_2(C_{n,J}))}.
\tag{10.2}
\]

**Beweis.** Aus (10.1) folgt

\[
b\delta_{n+J}\equiv-bC_{n,J}\pmod{2^J}.
\]

Da `b` ungerade ist, hat `bC_{n,J}` dieselbe `2`-adische Bewertung wie `C_{n,J}`. Ist `v_2(C_{n,J})<J`, ist die linke Seite durch `2^{v_2(C_{n,J})}` teilbar. Ist `v_2(C_{n,J})\ge J`, ist sie durch `2^J` teilbar. Da `b\delta_{n+J}` eine positive ganze Zahl ist, folgt (10.2). ∎

Daher genügt die Existenz einer Folge `(n_r,J_r)` mit

\[
\min(J_r,v_2(C_{n_r,J_r}))
-\log_2\delta_{n_r+J_r}\longrightarrow+\infty
\]

zur Irrationalität. Eine Ableitung dieser Existenz aus `HL_quant` wird hier nicht behauptet; sie wäre eine zusätzliche, derzeit unbewiesene arithmetische Divisibilitätsaussage.

Status: **proved implication; existence hypothesis unproved**.

---

## 11. CLAIMS-Ledger

| ID | Exakte Aussage | Status | Abhängigkeiten | Konfidenz |
|---|---|---|---|---:|
| C01 | Rekursion (2.1), Blockformel (2.2), Gap-Summenidentität (2.3) | proved | absolute Konvergenz | 0.99 |
| C02 | `S=a/(2^sb) ⇒ bδ_n∈ℤ` für `n≥s` | proved | C01/Tailzerlegung | 0.99 |
| C03 | Eventuell `bδ_n∈2ℤ` | proved | C02, gerade Prim-Gaps | 0.99 |
| C04 | Gleicher Präfix der Länge `J` ⇒ `b(δ_{n+J}-δ_{m+J})∈2^{J+1}ℤ` | proved | C01, C03 | 0.99 |
| C05 | `(FM) ⇒ S` irrational | proved | C01, C03, C04 | 0.99 |
| C06 | `HL_quant ⇒ (FM)` | proved | HLQ1–HLQ4 als Hypothese | 0.98 |
| C07 | `HL_quant ⇒ S` irrational | proved | C05, C06 | 0.98 |
| C08 | `v₂`-Block-Untergrenze (10.2) | proved | C01, C02 | 0.98 |
| C09 | Wahrheit von `HLQ1` im Fenster `≤6 log log X` mit relativem Fehler `(log X)^-20` | heuristic | quantitative exakte-Gap-HL-Theorie | 0.10 |
| C10 | Wahrheit von `HLQ2`, bedingtes Tail-Moment `O(log X)` auf jedem exakten Gap-Zylinder | heuristic | starke uniforme Primprozess-Mischung | 0.05 |
| C11 | Wahrheit von `HLQ3`, fork-reiche Modellwortpaare mit Masse `≥X exp(-20(loglog X)^2)` | heuristic | Zulässigkeits-/Singularserienkontrolle | 0.15 |
| C12 | Die im Briefing referierten Tao-/Schlage-Puchta-Beschreibungen sind korrekt | heuristic | UNVERIFIED; keine Webrecherche; nur Briefing | 0.20 |
| C13 | Primorial-Obstruktion, Exact-locking-Gegenmodell und Empirik aus dem Briefing | sketch | im vorliegenden Text nicht neu bewiesen | 0.70 |
| C14 | Das Lean-Skelett kompiliert ohne Anpassungen gegen eine konkrete Mathlib-Version | sketch | konkrete Mathlib-API | 0.35 |
| C15 | Lange konstante Gap-Runs als primärer Irrationalitätsmechanismus | false-start | Primorial-Obstruktion und Exact-locking laut Briefing | 0.95 |

---

## 12. Wo ich feststecke

Die konditionale Implikationskette ist geschlossen. Der offene mathematische Input liegt **vor** ihr:

1. **Hauptlücke:** Beweis von `HLQ2`. Benötigt wird eine uniforme Abschätzung
   \[
   \mathbb E(\delta_{n+t}\mid \text{exaktes Gap-Wort }w)=O(\log X)
   \]
   gleichzeitig für alle Wörter von Länge `O(log log X)` und räumlichem Durchmesser höchstens `(log X)^3`, mit relativem polylogarithmischem Fehler. Eine gewöhnliche Hardy–Littlewood-Aussage über endlich viele vorgeschriebene Primstellen liefert diese bedingte unendliche Tail-Kontrolle nicht unmittelbar.

2. **Zweite Lücke:** Beweis von `HLQ3` aus einer natürlicheren, standardisierten Primtupelvermutung. Man muss fork-kompatible exakte Gap-Wörter `WaV` und `Wa'V` mit kontrollierter positiver Modellmasse konstruieren und die Inclusion-Exclusion gegen zusätzliche Primzahlen uniform beherrschen.

3. **Formalisierungslücke:** Die Lean-Statements sind index- und typpräzise strukturiert, aber nicht kompiliert. Insbesondere müssen Summierbarkeit, Primzahlmonotonie, die genaue Mathlib-Definition von `Irrational` und einige Coercions implementiert werden.

Damit ist der exakte Status:

\[
\boxed{
\text{vollständiger konditionaler Beweis, aber kein Beweis von }\mathrm{HL\_quant}.
}
\]

---

## 13. Audit der Briefing-Fakten

- **Primorial obstruction:** ausdrücklich berücksichtigt; nicht als Beweisinput benutzt.
- **Parity:** ausdrücklich in Claim C03 und C04 benutzt.
- **Exact-locking countermodel:** ausdrücklich bei der Wahl von Fork-Merge statt Equal-run berücksichtigt; nicht als formale Prämisse benutzt.
- **Empirics:** ausdrücklich nicht benutzt.
- **Literatur:** wegen abgeschalteter Recherche als **UNVERIFIED** markiert und nicht beweistragend verwendet.
