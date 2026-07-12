# Erdős-Problem 251: rigorose Reduktionen und bedingte Kriterien

## Datei-Integrität

- Eingabedatei: `1a_blind.md`
- SHA-256: `482f56ab95bbd912a68b3ade54d4de87cffb721ffda5f6016efdf18023a78fce`
- Berechnung: SHA-256 über die unveränderte Bytefolge der angehängten Datei.

## Ergebnis in einem Satz

Die Irrationalität von

\[
S=\sum_{n\ge 1}\frac{p_n}{2^n}
\]

wird hier **nicht unbedingt entschieden**. Bewiesen werden jedoch zwei exakte, voneinander verschiedene Obstruktionen gegen Rationalität:

1. ein **2-adisches Rückwärtsblock-Kriterium** für binär gewichtete Primlücken;
2. ein **Periodenblock-Kriterium**, das lange Wiederholungen nichtkonstanter Lückenwörter über den wachsenden Nenner ihres periodischen Fixpunkts ausnutzt.

Außerdem wird rigoros gezeigt, dass selbst Monotonie, Parität und eine termweise Abweichung von höchstens `2` von einem beliebigen glatten Wachstumsprofil die Rationalität der Binärsumme nicht verhindern können.

---

# CLAIMS ledger

| ID | Exakte Aussage | Status | Abhängigkeiten | Konfidenz |
|---|---|---|---|---:|
| C1 | Die SHA-256-Summe der Eingabedatei ist `482f56ab95bbd912a68b3ade54d4de87cffb721ffda5f6016efdf18023a78fce`. | proved | Bytefolge der Eingabedatei | 1.00 |
| C2 | Für jedes `n≥0` unterscheidet sich `δ_n` von `2^n S` um eine ganze Zahl. Daher gilt: Ist `S=a/(2^s b)` mit ungeradem `b`, so ist `bδ_n∈ℤ` für alle `n≥s`; umgekehrt impliziert bereits `bδ_n∈ℤ` für ein einziges `n` und ein `b≥1`, dass `S∈ℚ`. | proved | Definitionen von `u_n,δ_n`; Konvergenz der Reihen | 0.99 |
| C3 | Für `C_{n,J}:=Σ_{i=1}^J 2^{J-i}g_{n+i}` gilt exakt `2^Jδ_n=C_{n,J}+δ_{n+J}`. | proved | Definition von `δ_n` oder Rekursion `δ_{n+1}=2δ_n-g_{n+1}` | 1.00 |
| C4 | Unter `S=a/(2^s b)`, `b` ungerade, gilt für `n≥s`, `J≥1` und `t=min(J,v₂(C_{n,J}))`: `bδ_{n+J}≥2^t`. | proved | C2, C3, Positivität von `δ` | 0.99 |
| C5 | Falls es Folgen `(n_k,J_k)` mit `n_k→∞` und `2^{min(J_k,v₂(C_{n_k,J_k}))}/δ_{n_k+J_k}→∞` gibt, dann ist `S` irrational. | proved | C4 | 0.99 |
| C6 | Wiederholt sich ein Wort `w=(c_1,…,c_r)` genau `K`-mal ab `g_{n+1}`, und ist `B_w=Σ_{i=1}^r2^{r-i}c_i`, `α_w=B_w/(2^r-1)`, so gilt `δ_n-α_w=2^{-Kr}(δ_{n+Kr}-α_w)`. | proved | C3 / Iteration einer affinen Kontraktion | 1.00 |
| C7 | Sei `q_w` der Nenner von `α_w` in vollständig gekürzter Form. Unter Rationalität von `S` mit ungeradem Nennerteil `b` gilt: Ist `q_w∤b`, dann `|δ_{n+Kr}-α_w|≥2^{Kr}/(bq_w)`. Ist `q_w|b`, dann gilt entweder `δ_{n+Kr}=α_w` oder `|δ_{n+Kr}-α_w|≥2^{Kr}/b`. | proved | C2, C6; elementare Gitterdistanz | 0.99 |
| C8 | Existieren wiederholte Wörter `w_k` mit Startindizes `n_k→∞`, reduzierten Nennern `q_k→∞` und `q_k|δ_{n_k+K_kr_k}-α_k|/2^{K_kr_k}→0`, dann ist `S` irrational. | proved | C7 | 0.99 |
| C9 | Für jede konvergente Binärsumme `A=Σa_n/2^n`, jedes `N` und jedes `c>0` kann man Koeffizienten `ε_n∈{0,1}` für `n>N` so wählen, dass `Σ(a_n+cε_n)/2^n` rational ist. | proved | Vollständigkeit der Binärdarstellung; Dichtheit von `ℚ` | 0.99 |
| C10 | Insbesondere können Parität, strikte Monotonie und eine termweise Störung von höchstens `2` eines vorgegebenen hinreichend separierten ganzzahligen Wachstumsprofils erhalten bleiben, während die Binärsumme rational gemacht wird. Diese Eigenschaften allein können daher die Primzahlarithmetik nicht ersetzen. | proved | C9 | 0.98 |
| C11 | Eine bloße Wiederholung eines festen konstanten Lückenworts liefert nur den Nenner `q_w=1`; damit bleibt der unbekannte ungerade Nennerteil `b` unangegriffen und man benötigt zusätzlich den Nichtgleichheits-/Squeeze-Schritt. | proved | C6, C7 | 1.00 |
| C12 | Die im Dossier genannten historischen, numerischen und literaturbezogenen Aussagen werden hier nicht extern geprüft und nicht als Beweisschritte benutzt. | proved | Methodische Festlegung | 1.00 |

---

# Hauptausarbeitung

## 1. Notation und Gitterstruktur der Tails

Es sei

\[
g_n=p_{n+1}-p_n
\]

und für `n≥0`

\[
u_n:=\sum_{k\ge1}\frac{p_{n+k}}{2^k},
\qquad
\delta_n:=u_n-p_{n+1}.
\]

Dann ist

\[
\delta_n=\sum_{j\ge1}\frac{g_{n+j}}{2^j}.
\]

Für

\[
A_n:=\sum_{m=1}^{n}2^{n-m}p_m\in\mathbb Z
\]

folgt direkt aus der Zerlegung von `S` in Anfangsstück und Rest:

\[
u_n=2^nS-A_n.
\]

Also

\[
\delta_n=2^nS-(A_n+p_{n+1}). \tag{1}
\]

Damit ist `δ_n` modulo ganzen Zahlen genau die Verdopplungsbahn von `S`.

Ist

\[
S=\frac{a}{2^s b},\qquad b\ge1\text{ ungerade},
\]

so ergibt (1) für jedes `n≥s`

\[
b\delta_n\in\mathbb Z. \tag{2}
\]

Umgekehrt genügt ein einziges rationales `δ_n`: Aus (1) folgt dann

\[
S=2^{-n}\bigl(\delta_n+A_n+p_{n+1}\bigr)\in\mathbb Q.
\]

Das beweist C2. Es erklärt zugleich, warum die Integrabilität entlang der Rekursion allein keine neue Kongruenzinformation liefert: Hat man einen Gitterpunkt erreicht, propagiert die ganzzahlige affine Rekursion ihn automatisch weiter.

## 2. Allgemeine endliche Blockidentität

Für `J≥1` definiere den rückwärts binär gewichteten Lückencode

\[
C_{n,J}:=\sum_{i=1}^{J}2^{J-i}g_{n+i}.
\]

Aus der Taildarstellung folgt

\[
\begin{aligned}
\delta_n
&=\sum_{i=1}^{J}\frac{g_{n+i}}{2^i}
 +\frac1{2^J}\sum_{j\ge1}\frac{g_{n+J+j}}{2^j}\\
&=2^{-J}\bigl(C_{n,J}+\delta_{n+J}\bigr).
\end{aligned}
\]

Somit

\[
2^J\delta_n=C_{n,J}+\delta_{n+J}. \tag{3}
\]

Dies ist C3.

---

## 3. Neue Reduktion I: 2-adische Rückwärtsblock-Obstruktion

Nehmen wir vorübergehend an,

\[
S=\frac{a}{2^s b}
\]

mit ungeradem `b`. Setze für `m≥s`

\[
d_m:=b\delta_m\in\mathbb Z.
\]

Da alle Primlücken positiv sind, ist `δ_m>0`, also `d_m>0`.

Multiplikation von (3) mit `b` ergibt

\[
d_{n+J}=2^Jd_n-bC_{n,J}. \tag{4}
\]

Daher

\[
d_{n+J}\equiv-bC_{n,J}\pmod {2^J}. \tag{5}
\]

Sei `v₂(x)` die 2-adische Bewertung eines positiven ganzzahligen `x` und

\[
t:=\min\{J,v_2(C_{n,J})\}.
\]

Weil `b` ungerade ist, verändert die Multiplikation mit `b` die 2-adische Bewertung nicht.

- Falls `v₂(C_{n,J})<J`, hat jede ganze Zahl in der Restklasse aus (5) exakt mindestens den Faktor `2^t`; eine positive solche Zahl ist daher mindestens `2^t`.
- Falls `2^J\mid C_{n,J}`, ist `d_{n+J}` nach (5) ein positives Vielfaches von `2^J` und daher mindestens `2^J`.

In beiden Fällen gilt exakt

\[
\boxed{\;b\delta_{n+J}\ge
2^{\min(J,v_2(C_{n,J}))}.\;} \tag{6}
\]

Das beweist C4.

### Unmittelbares Irrationalitätskriterium

Aus (6) folgt C5:

> Falls es Blöcke gibt, für die die 2-adische Teilbarkeit des rückwärts gewichteten Lückencodes die Größe des anschließenden Tails beliebig stark übertrifft, ist `S` irrational.

Formal genügt

\[
\lim_{k\to\infty}
\frac{2^{\min(J_k,v_2(C_{n_k,J_k}))}}
     {\delta_{n_k+J_k}}
=\infty,
\qquad n_k\to\infty. \tag{7}
\]

Denn bei rationalem `S` wäre der Quotient in (7) nach (6) für alle hinreichend großen `k` höchstens das feste `b`.

### Bedeutung des Kriteriums

Dieses Kriterium benutzt keine gleichen Lücken. Es sucht stattdessen endliche Lückenblöcke, deren letzte Stellen beim Lesen als binär gewichtetes Wort eine ungewöhnlich hohe Zweierpotenz auslöschen.

Für festes `T≤J` hängt

\[
C_{n,J}\pmod {2^T}
\]

nur von den letzten `T` Lücken des Blocks ab. Die fehlende Aussage ist daher eine konkrete endliche Kongruenz- plus Größenfrage über Primlücken, nicht eine Behauptung über einen unendlichen Tail.

---

## 4. Neue Reduktion II: lange Potenzen eines Lückenworts

Sei

\[
w=(c_1,\ldots,c_r)
\]

und nehme an, dass dieses Wort ab Index `n+1` genau `K`-mal hintereinander in der Lückenfolge auftritt:

\[
g_{n+\ell r+i}=c_i
\quad
(0\le\ell<K,\ 1\le i\le r). \tag{8}
\]

Definiere

\[
B_w:=\sum_{i=1}^{r}2^{r-i}c_i,
\qquad
\alpha_w:=\frac{B_w}{2^r-1}. \tag{9}
\]

Für einen einzelnen Wortblock lautet (3)

\[
\delta_n=\frac{B_w}{2^r}+2^{-r}\delta_{n+r}. \tag{10}
\]

Die Zahl `α_w` ist der eindeutige Fixpunkt der affinen Abbildung auf der rechten Seite, denn

\[
\alpha_w=\frac{B_w}{2^r}+2^{-r}\alpha_w.
\]

Nach `K` Iterationen von (10) folgt

\[
\boxed{\;
\delta_n-\alpha_w
=2^{-Kr}\bigl(\delta_{n+Kr}-\alpha_w\bigr).
\;} \tag{11}
\]

Das ist C6.

### Der neue Nennermechanismus

Schreibe `α_w=m_w/q_w` vollständig gekürzt, also

\[
q_w=\frac{2^r-1}{\gcd(B_w,2^r-1)}. \tag{12}
\]

Unter der Rationalitätsannahme liegt `δ_n` für `n≥s` im Gitter `(1/b)ℤ`.

#### Fall 1: `q_w∤b`

Dann liegt `α_w` nicht in `(1/b)ℤ`. Für jedes `z∈ℤ` gilt

\[
\left|\frac{z}{b}-\frac{m_w}{q_w}\right|
=\frac{|q_wz-bm_w|}{bq_w}
\ge\frac1{bq_w},
\]

weil der Zähler eine von null verschiedene ganze Zahl ist. Mit (11) folgt

\[
\boxed{\;
|\delta_{n+Kr}-\alpha_w|
\ge \frac{2^{Kr}}{bq_w}.
\;} \tag{13}
\]

#### Fall 2: `q_w|b`

Dann liegt auch `α_w` im Gitter `(1/b)ℤ`. Folglich ist entweder

\[
\delta_n=\alpha_w,
\]

was nach (11) äquivalent zu `δ_{n+Kr}=α_w` ist, oder

\[
|\delta_n-\alpha_w|\ge\frac1b.
\]

Im zweiten Unterfall liefert (11)

\[
\boxed{\;
|\delta_{n+Kr}-\alpha_w|
\ge\frac{2^{Kr}}b.
\;} \tag{14}
\]

Damit ist C7 bewiesen.

### Präziser bedingter Irrationalitätssatz

Für eine Folge tatsächlicher Primlückenwörter `w_k` seien

- `r_k` ihre Längen,
- `K_k` ihre Wiederholungszahlen,
- `n_k` ihre Startindizes,
- `α_k` die Fixpunkte aus (9),
- `q_k` deren vollständig gekürzte Nenner.

Dann gilt:

> **Theorem (bedingte Irrationalität durch Wortpotenzen).**  
> Angenommen,
> \[
> n_k\to\infty,\qquad q_k\to\infty,
> \]
> und
> \[
> \frac{q_k\,|\delta_{n_k+K_kr_k}-\alpha_k|}
> {2^{K_kr_k}}
> \longrightarrow0. \tag{15}
> \]
> Dann ist `S` irrational.

**Beweis.** Wäre `S=a/(2^sb)` rational, so wäre für große `k` sowohl `n_k≥s` als auch `q_k>b`. Damit kann `q_k` kein Teiler von `b` sein. Nach (13) wäre dann

\[
\frac{q_k|\delta_{n_k+K_kr_k}-\alpha_k|}
     {2^{K_kr_k}}
\ge\frac1b,
\]

im Widerspruch zu (15). ∎

Dies beweist C8.

### Vollständig explizite stärkere Hypothese

Eine leichter prüfbare, aber stärkere Version ersetzt den exakten Ausdruck in (15) durch Schranken. Gilt zusätzlich

\[
\delta_{n_k+K_kr_k}\le M_k,
\qquad
\max_i c_{k,i}\le H_k,
\]

so liegt `α_k` als positiv gewichteter periodischer Mittelwert zwischen den Wortwerten, insbesondere `0<α_k≤H_k`. Daher

\[
|\delta_{n_k+K_kr_k}-\alpha_k|\le M_k+H_k.
\]

Es reicht also die rein quantitative Bedingung

\[
q_k\to\infty,
\qquad
\frac{q_k(M_k+H_k)}{2^{K_kr_k}}\to0. \tag{16}
\]

### Beziehung zum Gleichlücken-Squeeze

Für ein konstantes Wort der Länge `r=1`, also `w=(c)`, ist

\[
\alpha_w=c,
\qquad q_w=1.
\]

Damit teilt `q_w` jeden möglichen Nenner `b`; Fall 1 ist nie verfügbar. Übrig bleibt Fall 2: entweder exakte Gleichheit oder die bekannte Squeeze-Untergrenze. Dies beweist C11 und zeigt den Vorteil nichtkonstanter Wörter mit wachsenden reduzierten Nennern.

---

## 5. Rigorose Widerlegung einer natürlichen Wachstumsstrategie

Die folgende elementare Kodierungslemma zeigt, dass selbst extrem genaue Wachstumsinformation die Irrationalität nicht erzwingen kann.

### Binäre Rationalisierung durch beschränkte Tail-Störungen

Sei

\[
A=\sum_{n\ge1}\frac{a_n}{2^n}
\]

eine konvergente reelle Reihe. Fixiere `N≥0` und `c>0`. Die durch Störungen

\[
a_n\longmapsto a_n+c\varepsilon_n,
\qquad
\varepsilon_n\in\{0,1\},\quad n>N,
\]

erreichbare Änderung ist jedes Element des Intervalls

\[
\left[0,\frac{c}{2^N}\right]. \tag{17}
\]

Denn für jedes `x` in diesem Intervall liegt

\[
y:=\frac{2^Nx}{c}
\]

in `[0,1]` und besitzt eine Binärdarstellung

\[
y=\sum_{j\ge1}\frac{\varepsilon_{N+j}}{2^j}.
\]

Nach Rückskalierung folgt

\[
x=\sum_{n>N}\frac{c\varepsilon_n}{2^n}.
\]

Da die rationalen Zahlen dicht sind, enthält das nichttriviale Intervall

\[
\left[A,A+\frac c{2^N}\right]
\]

eine rationale Zahl `R`. Wähle `x=R-A` und die zugehörigen Binärziffern. Dann ist

\[
\sum_{n\ge1}\frac{a_n+c\varepsilon_n}{2^n}=R\in\mathbb Q.
\]

Das beweist C9.

### Erhaltung von Parität und Monotonie

Setzt man `c=2` und sind die `a_n` ganzzahlig, bleibt die Parität jedes Terms erhalten. Sind außerdem die Tail-Abstände

\[
a_{n+1}-a_n\ge3\qquad(n>N),
\]

so gilt für die gestörte Folge

\[
(a_{n+1}+2\varepsilon_{n+1})-(a_n+2\varepsilon_n)
\ge 3-2=1.
\]

Die Folge bleibt also strikt wachsend und jeder Term ändert sich um höchstens `2`.

Folglich gibt es zu jedem hinreichend separierten ganzzahligen Wachstumsprofil eine Folge mit

- derselben Parität,
- strikter Monotonie,
- termweiser Abweichung höchstens `2`,
- aber rationaler Binärsumme.

Das beweist C10. Eine erfolgreiche Lösung muss daher eine Eigenschaft verwenden, die durch solche unabhängigen kleinen Tail-Störungen zerstört wird — konkret die arithmetische Struktur der Primlücken oder eine gleich starke globale Abhängigkeit.

---

# Lean-nahe Lemmaformulierungen

Die folgenden Signaturen sind bewusst auf abstrakte Folgen formuliert. Sie vermeiden zunächst Bibliotheksdetails zu `Nat.nth Nat.Prime`, Konvergenz und `padicValNat`. Die mathematischen Aussagen sind exakt; einzelne Bezeichner können in Mathlib anders heißen.

## A. Rekursion und endlicher Blockcode

```lean
-- G n corresponds to the gap after the 0-indexed prime q n.

def blockCode (G : Nat → Nat) (n : Nat) : Nat → Nat
  | 0     => 0
  | J + 1 => 2 * blockCode G n J + G (n + J)

-- Abstract recurrence satisfied by delta.
def GapRecurrence (δ : Nat → Real) (G : Nat → Nat) : Prop :=
  ∀ n, δ (n + 1) = 2 * δ n - G n

theorem delta_block_identity
    (δ : Nat → Real) (G : Nat → Nat)
    (hrec : GapRecurrence δ G) (n J : Nat) :
    (2 : Real)^J * δ n = blockCode G n J + δ (n + J) := by
  -- induction on J using hrec
  sorry
```

`blockCode G n J` ist exakt

\[
\sum_{i=0}^{J-1}2^{J-1-i}G(n+i).
\]

## B. Gitterannahme aus Rationalität

```lean
def EventuallyOddLattice
    (δ : Nat → Real) (b s : Nat) : Prop :=
  Odd b ∧ 0 < b ∧
  ∀ n, s ≤ n → ∃ d : Nat, (d : Real) = b * δ n
```

Für die konkrete Primfolge ist aus C2 zu beweisen:

```lean
-- S here is the 1-indexed real series from the statement.
theorem rational_implies_eventually_odd_lattice
    (hS : S = a / ((2 : Real)^s * b))
    (hb : Odd b) (hbpos : 0 < b) :
    EventuallyOddLattice δ b s := by
  -- use δ n = 2^n S - an integer
  sorry
```

## C. 2-adische Blockuntergrenze

Mathematisch exakte Form:

```lean
/-- Here truncV2 x J = min J (v₂ x), with truncV2 0 J = J. -/
theorem lattice_block_v2_lower_bound
    (δ : Nat → Real) (G : Nat → Nat)
    (hrec : GapRecurrence δ G)
    (hpos : ∀ n, 0 < δ n)
    (b s n J : Nat)
    (hlat : EventuallyOddLattice δ b s)
    (hns : s ≤ n) :
    (2 : Real)^(truncV2 (blockCode G n J) J)
      ≤ b * δ (n + J) := by
  -- obtain natural d_n and d_{n+J}; use
  -- d_{n+J} ≡ -b * blockCode G n J [ZMOD 2^J]
  -- and oddness of b
  sorry
```

Daraus folgt direkt die Lean-Zielstruktur des bedingten Kriteriums C5:

```lean
theorem irrational_of_unbounded_v2_blocks
    (hblocks :
      ∀ B : Nat, ∀ s : Nat, ∃ n J : Nat,
        s ≤ n ∧
        B * δ (n + J)
          < (2 : Real)^(truncV2 (blockCode G n J) J)) :
    Irrational S := by
  intro hrat
  -- extract odd denominator b and contradict hblocks with B = b
  sorry
```

Diese quantifizierte Form vermeidet Grenzwertbibliothek und ist logisch äquivalent zur für C5 benötigten Unbeschränktheit.

## D. Wiederholtes Wort und Fixpunkt

```lean
def wordValue {r : Nat} (w : Fin r → Nat) : Nat :=
  ∑ i, 2^(r - 1 - i.1) * w i

def wordFixedPoint {r : Nat} (w : Fin r → Nat) : Real :=
  wordValue w / ((2 : Real)^r - 1)

def RepeatsWord
    (G : Nat → Nat) (n K : Nat) {r : Nat} (w : Fin r → Nat) : Prop :=
  ∀ ℓ, ℓ < K → ∀ i : Fin r, G (n + ℓ*r + i.1) = w i

theorem repeated_word_contraction
    (hrec : GapRecurrence δ G)
    (hw : RepeatsWord G n K w) :
    δ n - wordFixedPoint w =
      (2 : Real)^(-(K*r : Int)) *
        (δ (n + K*r) - wordFixedPoint w) := by
  -- preferably state with division by 2^(K*r), avoiding Int powers
  sorry
```

Eine Lean-freundlichere Zielgleichung ohne negative Exponenten ist

```lean
(2 : Real)^(K*r) * (δ n - wordFixedPoint w)
  = δ (n + K*r) - wordFixedPoint w
```

## E. Nennerobstruktion

Sei `α=m/q` gekürzt. Die zentrale Gitterlemma ist unabhängig von Primzahlen:

```lean
theorem dist_rational_from_lattice
    (m q b z : Int)
    (hq : 0 < q) (hb : 0 < b)
    (hcop : IsCoprime m q)
    (hnot : ¬ q ∣ b) :
    |(z : Real) / b - (m : Real) / q| ≥ 1 / ((b*q : Int) : Real) := by
  -- numerator |q*z - b*m| is a nonzero integer
  sorry
```

Zusammen mit `repeated_word_contraction` ergibt dies C7 und C8.

---

# Wo die Bedingungen ihre quantitative Stärke verbrauchen

## Beim 2-adischen Kriterium C5

Benötigt wird eine Folge tatsächlicher Primlückenblöcke, für die

\[
\min(J,v_2(C_{n,J}))-\log_2\delta_{n+J}\to+\infty.
\]

Die gesamte Stärke wird an genau zwei Stellen verbraucht:

1. hohe Zweierpotenzteilbarkeit des endlichen Rückwärtscodes `C_{n,J}`;
2. eine im Vergleich dazu kleine Größe des nachfolgenden geometrischen Tails.

Es ist keine Häufigkeitsaussage nötig; eine geeignete Folge einzelner Blöcke genügt.

## Beim Periodenblock-Kriterium C8

Benötigt werden Wortpotenzen mit

1. `q_k→∞`, damit der reduzierte Fixpunktnenner schließlich nicht mehr den unbekannten festen Nenner `b` teilen kann;
2. exponentieller Kontraktion `2^{-K_kr_k}`, die den Nachlauf stärker schlägt als der Faktor `q_k`.

In der expliziten Version (16) wird die gesamte Uniformität in

\[
q_k(M_k+H_k)=o(2^{K_kr_k})
\]

verbraucht. Die bloße Existenz jedes festen Musters, selbst unendlich oft, reicht nicht.

---

# Where I am stuck

Der exakt fehlende Bestandteil ist eine **unbedingte Primlückenaussage**, die mindestens eines der folgenden beiden Kriterien für die tatsächliche Primfolge erzwingt:

1. **2-adische Blockauslöschung:** Es existieren Blöcke mit
   \[
   \frac{2^{\min(J,v_2(C_{n,J}))}}{\delta_{n+J}}
   \to\infty.
   \]

2. **Nichtkonstante lange Wortpotenzen mit wachsendem Fixpunktnenner:** Es existieren wiederholte Lückenwörter mit
   \[
   q_k\to\infty,
   \qquad
   \frac{q_k|\delta_{n_k+K_kr_k}-\alpha_k|}
        {2^{K_kr_k}}
   \to0.
   \]

Die im Ausgangsdokument eingefrorenen Informationen liefern weder die benötigte 2-adische Auslöschung noch die erforderlichen quantitativ frühen und langen Wortwiederholungen. Für konstante Wörter bleibt zusätzlich der Ausnahmefall `δ=α` beziehungsweise der unbekannte ungerade Nennerteil bestehen.

Daher liegt hier rigoroser partieller Fortschritt in Form neuer notwendiger Bedingungen und exakter bedingter Irrationalitätssätze vor, aber kein unbedingter Beweis von Erdős Problem 251.

---

# Nicht verwendete oder nicht extern verifizierte Angaben

Die folgenden im Ausgangsdokument enthaltenen Arten von Aussagen werden in keinem Beweis oben benötigt und bleiben gemäß Aufgabenregel **UNVERIFIED**:

- historische Zuschreibungen und Jahreszahlen;
- Aussagen zum gegenwärtigen Literaturstand bestimmter Primlückenmuster;
- numerische Dezimal- und Kettenbruchdaten;
- probabilistische Cramér-Modell-Heuristiken;
- asymptotische Durchschnittsaussagen wie `δ_n ~ log n`, sofern sie nicht als zusätzliche Hypothese eingesetzt werden.

Alle als `proved` markierten Resultate wurden oben elementar aus den Definitionen, der gegebenen Konvergenz und endlicher Arithmetik hergeleitet.
