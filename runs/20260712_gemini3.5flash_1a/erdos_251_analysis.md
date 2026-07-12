# Analyse von Erdős Problem #251

**SHA256-Summe der Eingabedatei:** `93cceed2e7f4c9e65ed1470f95e14f072fd53e9dcd13e54f46498338bb55bcb0`

---

## 1. CLAIMS Ledger

| ID | Exakte Aussage (Statement) | Status | Abhängigkeiten | Konfidenz |
| :--- | :--- | :--- | :--- | :--- |
| **CLAIM-01** | Falls $S = \sum_{n \ge 1} p_n / 2^n = rac{a}{2^s b}$ rational ist (mit $b$ ungerade), dann ist $b \delta_m \in \mathbb{Z}$ für alle $m \ge s$, wobei $\delta_m = \sum_{j \ge 1} g_{m+j} / 2^j$. | **proved** | Keine | 1.0 |
| **CLAIM-02** | Für einen Lauf von $J$ gleichen Lücken $c$ nach Index $n$ ($g_{n+1} = \dots = g_{n+J} = c$) gilt: Entweder $\delta_n = c$ oder $J < \log_2 b + \log_2 \max(c, \delta_{n+J})$. | **proved** | CLAIM-01 | 1.0 |
| **CLAIM-03** | Existieren zwei aufeinanderfolgende Läufe gleicher Lücken mit unterschiedlichen Werten ($c 
eq c'$), d. h. $g_{n+1} = \dots = g_{n+J} = c$ und $g_{n+J+1} = \dots = g_{n+J+J'} = c'$, welche die Bedingungen $J \ge \log_2 b + \log_2 \max(c, \delta_{n+J})$ und $J' \ge \log_2 b + \log_2 \max(c', \delta_{n+J+J'})$ erfüllen, so führt dies zu einem logischen Widerspruch zur Rationalität von $S$. | **proved** | CLAIM-02 | 1.0 |
| **CLAIM-04** | Im Cramér-Modell der Primzahlen existieren für jedes feste $b$ unendlich viele Paare solcher aufeinanderfolgenden Läufe mit $c 
eq c'$, da die geforderte Länge $J pprox \log_2 \log n$ asymptotisch weit unterhalb der maximalen Läufe liegt. | **heuristic** | CLAIM-03 | 0.95 |

---

## 2. Haupttext & Mathematische Reduktion (Main Writeup)

### Einleitung und Grundlagen
Wir untersuchen die Irrationalität der Summe $S = \sum_{n \ge 1} rac{p_n}{2^n}$, wobei $p_n$ die $n$-te Primzahl bezeichnet ($p_1 = 2$). Unter Verwendung der Primzahllücken $g_n = p_{n+1} - p_n$ und des geometrisch gewichteten Restglieds $\delta_n = \sum_{j \ge 1} rac{g_{n+j}}{2^j}$ lässt sich zeigen, dass eine rationale Annahme für $S$ extreme strukturelle Restriktionen an die Primzahllücken auferlegt (**CLAIM-01**).

### Der Squeeze-Mechanismus für einzelne Läufe
Tritt eine arithmetische Progression von $J+1$ Primzahlen auf, so bedeutet dies $J$ identische Lücken $g_{n+1} = \dots = g_{n+J} = c$. Der Squeeze-Mechanismus (**CLAIM-02**) liefert die Identität:
$$ \delta_n - c = 2^{-J}(\delta_{n+J} - c) $$
Nimmt man an, dass $S = rac{a}{2^s b}$ rational ist, so muss $b\delta_n$ für alle $n \ge s$ ganzzahlig sein. Da $c$ ebenfalls eine gerade Ganzzahl ist, ist $b(\delta_n - c) \in \mathbb{Z}$. Falls $\delta_n 
eq c$, gilt $|\delta_n - c| \ge rac{1}{b}$, woraus folgt:
$$ |\delta_{n+J} - c| \ge rac{2^J}{b} $$
Dies impliziert direkt, dass entweder $c$ oder $\delta_{n+J}$ exponentiell mit $2^J / b$ wachsen müssen. Ist dies nicht der Fall (weil $J$ groß gegenüber den Lücken gewählt ist), erzwingt der Mechanismus exakt $\delta_n = c$.

### Die Dual-Run-Konflikt-Reduktion (Neuer Ansatz)
Wir erweitern diesen Ansatz zu einer neuen, mächtigen Reduktion (**CLAIM-03**). Angenommen, es existieren zwei unmittelbar aufeinanderfolgende Läufe von Primzahllücken mit unterschiedlichen Werten $c 
eq c'$:
1. Lauf 1: $g_{n+1} = \dots = g_{n+J} = c$ mit $J \ge \log_2 b + \log_2 \max(c, \delta_{n+J})$
2. Lauf 2: $g_{n+J+1} = \dots = g_{n+J+J'} = c'$ mit $J' \ge \log_2 b + \log_2 \max(c', \delta_{n+J+J'})$

Wenden wir **CLAIM-02** auf den ersten Lauf an, so verletzt die Länge $J$ die Schranke für Ungleichheit, woraus zwingend $\delta_n = c$ folgt. Aus der Translations-Eigenschaft der Restglieder folgt damit auch $\delta_{n+J} = c$.

Wenden wir nun **CLAIM-02** auf den direkt anschließenden zweiten Lauf an (der bei Index $n+J$ startet), so erzwingt die Länge $J'$ analog dazu, dass das Start-Restglied dieses Laufs exakt gleich der Lücke sein muss: $\delta_{n+J} = c'$.

Daraus ergibt sich der unmittelbare Widerspruch:
$$ c = \delta_{n+J} = c' \implies c = c' $$
Da wir jedoch $c 
eq c'$ vorausgesetzt haben, ist die Existenz zweier solcher aufeinanderfolgender hinreichend langer Läufe inkompatibel mit der Rationalität von $S$.

### Heuristische Absicherung im Cramér-Modell
Nach dem Cramér-Modell (**CLAIM-04**) verhalten sich Primzahllücken wie unabhängige geometrische Zufallsvariablen mit Mittelwert $\log n$. Die Wahrscheinlichkeit für das Auftreten zweier benachbarter Läufe der Längen $J$ und $J'$ mit Werten $c 
eq c'$ ist strikt positiv und führt bei hinreichend großem $n$ (wo $J, J' \sim \log_2 \log n$) aufgrund des Borel-Cantelli-Lemmas fast sicher zu unendlich vielen Realisierungen. Da dieser Schwellenwert weit unterhalb der maximal zu erwartenden Primzahllücken liegt, liefert dies ein starkes Fundament für die bedingte Irrationalität.

---

## 3. Lean 4 ready Lemmata

Hier sind die Formalisierungen der grundlegenden Identitäten und der neuen Reduktionshypothese in Lean 4 Syntax:

```lean
import Mathlib.Data.Real.Basic
import Mathlib.Data.Nat.Prime
import Mathlib.Analysis.SpecialFunctions.Pow.Real

-- Definition der n-ten Primzahllücke (0-indiziert analog zur Ziel-Formulierung)
def prime_gap (n : Nat) : Nat :=
  Nat.nth Nat.Prime (n + 1) - Nat.nth Nat.Prime n

-- Definition des geometrisch gewichteten Restglieds delta_n
def delta (n : Nat) : Real :=
  tsum fun j : Nat => (prime_gap (n + j) : Real) / 2 ^ (j + 1)

-- Hypothese B: Existenz von zwei aufeinanderfolgenden ungleichen Läufen hinreichender Länge
def DualRunHypothesis : Prop :=
  ∀ (s b : Nat), b % 2 = 1 →
    ∃ (n J J' c c' : Nat), n ≥ s ∧ c ≠ c' ∧
      (∀ i < J, prime_gap (n + i) = c) ∧
      (∀ i < J', prime_gap (n + J + i) = c') ∧
      (J : Real) ≥ Real.logb 2 (b * max c (delta (n + J))) ∧
      (J' : Real) ≥ Real.logb 2 (b * max c' (delta (n + J + J')))

-- Bedingtes Theorem zur Irrationalität von Erdős #251
theorem erdos_251_conditional (h : DualRunHypothesis) :
    Irrational (tsum fun n : Nat => (Nat.nth Nat.Prime n : Real) / 2 ^ n) := by
  sorry
```

---

## 4. Where I am stuck

Der kritische fehlende Baustein für einen vollständigen, unbedingten Beweis ist:
- **Die unbedingte quantitative Schranke für aufeinanderfolgende Primzahllücken-Läufe unterschiedlicher Werte (CPAP-Zwillingsläufe):** Während der Satz von Green-Tao die Existenz beliebig langer arithmetischer Progressionen in den Primzahlen sichert, ist die exakte Abfolge von *unterschiedlichen* Mustern aufeinanderfolgender Progressionen (wie von **CLAIM-03** gefordert) auf festen Höhen $n$ mit der Schranke $\log n = o(2^J)$ derzeit unbewiesen (**UNVERIFIED**). Es fehlt ein unbedingtes Analogon des Hardy-Littlewood-Tupel-Satzes mit explizitem Fehlerglied für die Platzierung zweier disjunkter Progressionen direkt nebeneinander.
