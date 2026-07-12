# Erdős-Problem #251: SHA-256 und konditionale Fork-Merge-Reduktion

## 0. Eingabedatei und SHA-256

- Eingabedatei: `1b_briefed(2).md`
- Dateigröße: `7901` Byte
- SHA-256:

```text
5f6abc6f77e401ae040a60945d6b2b7060fd18913e8181edeea2b4a21394b4e4
```

Die Summe wurde bytegenau mit `sha256sum` über `/mnt/data/1b_briefed(2).md` berechnet.

---

## 1. Ergebnis in einem Satz

Es gibt eine vollständige und präzise Beweiskette

\[
\mathrm{HL}_{\mathrm{quant}}\Longrightarrow \mathrm{FM}
\Longrightarrow \sum_{n\ge 1}\frac{p_n}{2^n}\notin\mathbb Q,
\]

**sofern** `HL_quant` nicht nur eine uniforme Hardy–Littlewood-Asymptotik für einzelne Primzahllückenwörter bis zur Länge \(O(\log\log x)\), sondern zusätzlich eine quantitative, gemittelte **Fork-Antikonzentration nach Fixierung von Präfix und Suffix** enthält. Der zweite Pfeil ist elementar und vollständig bewiesen. Der erste Pfeil ist ebenfalls vollständig aus dem unten exakt formulierten Paket bewiesen. Das derzeit ungelöste mathematische Problem ist, diese Fork-Antikonzentration aus einer natürlicheren oder etablierten Version der uniformen Primzahl-\(k\)-Tupel-Vermutung herzuleiten.

Das unbedingte Erdős-Problem bleibt offen; die Problemseite führt es weiterhin als offen. Terence Tao weist dort auf genau die Notwendigkeit statistischer Kontrolle über ungefähr \(\log\log n\) aufeinanderfolgende Primzahllücken hin. [Erdős Problems #251](https://www.erdosproblems.com/251), [Diskussion zu #251](https://www.erdosproblems.com/forum/thread/251).

---

## 2. Notation

Es sei

\[
p_1=2<p_2<p_3<\cdots,
\qquad g_n:=p_{n+1}-p_n.
\]

Setze

\[
S:=\sum_{n\ge1}\frac{p_n}{2^n},
\qquad
u_n:=\sum_{k\ge1}\frac{p_{n+k}}{2^k},
\]

und

\[
\delta_n:=\nu_n-p_{n+1}
       =\sum_{j\ge1}\frac{g_{n+j}}{2^j}.
\]

Dann gilt

\[
\delta_{n+1}=2\delta_n-g_{n+1}.
\tag{2.1}
\]

Für \(J\ge0\) definiere den rückwärts gewichteten Blockcode

\[
C_{n,J}:=\sum_{i=1}^{J}2^{J-i}g_{n+i}.
\]

Iteration von (2.1) liefert

\[
\delta_{n+J}=2^J\delta_n-C_{n,J}.
\tag{2.2}
\]

**Markierung Briefing-Fakt:** Die Identitäten für \(\delta_n\), die Rekursion und der Blockcode stammen aus dem bereitgestellten Briefing; sie werden hier vollständig inline bewiesen bzw. durch endliche Iteration verifiziert.

---

## 3. CLAIMS-Ledger

| ID | Exakte Aussage | Status | Abhängigkeiten | Konfidenz |
|---|---|---:|---|---:|
| `HASH` | SHA-256 der Eingabedatei ist `5f6abc...b4e4`. | proved | bytegenaue Berechnung | 1.00 |
| `C1` | Die Reihen für \(S,\nu_n,\delta_n\) konvergieren absolut; (2.1) und (2.2) gelten. | proved | elementare Primzahlwachstumsabschätzung | 1.00 |
| `C2` | Ist \(S=A/(2^s b)\) mit \(b\) ungerade, dann ist \(b\delta_n\in\mathbb Z\) für \(n\ge s\), und \(b\delta_n\in2\mathbb Z\) für alle hinreichend großen \(n\). | proved | `C1`; Parität der Primzahllücken | 1.00 |
| `C3` | Gleiche Lückenpräfixe der Länge \(J\) quantisieren die Differenz: \(b(\delta_{n+J}-\delta_{m+J})\in2^{J+1}\mathbb Z\), sobald die beiden Ausgangstails im geraden Gitter liegen. | proved | `C2`, (2.2) | 1.00 |
| `C4` | Eine Fork-Merge-Konfiguration mit ausreichend kleinen vier Tails widerspricht Rationalität. | proved | `C2`, `C3`, gerade Primzahllücken | 1.00 |
| `C5` | Die asymptotische Fork-Merge-Hypothese `(FM)` impliziert die Irrationalität von \(S\). | proved | `C4` | 1.00 |
| `C6` | Im Mittel über Primindizes mit \(x\le p_n<2x\) ist \(\delta_{n+r}=O(\log x)\), gleichmäßig für \(r=O(\log\log x)\). | proved | PNT-grobe Schranken für \(p_n\), Teleskopieren | 0.99 |
| `C7` | Für \(H_x=(\log x)^4\) ist der Anteil der Indizes, bei denen einer von vier benötigten Tails \(>H_x\) ist, \(O((\log x)^{-3})\). | proved | `C6`, Markov | 1.00 |
| `C8` | Der Anteil der Startstellen, deren lokaler Block der Länge \(O(\log\log x)\) Spannweite \(>(\log x)^3\) hat, ist \(o(1)\). | proved | Teleskopieren, Markov | 1.00 |
| `HLQ` | Das unten formulierte uniforme, konsekutive Hardy–Littlewood-Paket mit Fork-Antikonzentration gilt. | heuristic / hypothesis | unbewiesene Primzahlstatistik | 0.55 als plausible Hypothese; 0 als bekanntes Theorem |
| `C9` | `HLQ` impliziert eine tatsächliche Fork-Antikonzentration für Primzahllückenwörter. | proved conditionally | `HLQ.Q1`, `HLQ.Q2` | 1.00 |
| `C10` | `HLQ` impliziert `(FM)`. | proved conditionally | `C7`, `C8`, `C9` | 1.00 |
| `C11` | `HLQ` impliziert Irrationalität von \(S\). | proved conditionally | `C5`, `C10` | 1.00 |
| `SC1` | Schlage-Puchtas Paper beweist Irrationalitätsergebnisse für Fakultätsreihen mit Selberg-Sieb, Polynomelimination und Diskrepanz. | proved as literature report | [ScPu11] | 0.99 |
| `SC2` | [ScPu11] liefert nicht die hier benötigte uniforme Existenz-/Antikonzentrationsaussage für Fensterlänge \(\asymp\log\log x\) in Basis 2. | proved as comparison of hypotheses | `SC1`, Form von `HLQ` | 0.98 |
| `V2` | Die im Briefing genannte \(v_2\)-Block-Hypothese impliziert Irrationalität. | proved | `C2`, (2.2) | 1.00 |
| `WP` | Die im Briefing genannte Wortpotenz-Hypothese impliziert Irrationalität. | proved | `C2`, affine Blockiteration | 0.99 |
| `FS1` | Eine bloße punktweise HL-Asymptotik ohne summierbare Familienuniformität oder Fork-Antikonzentration schließt die Möglichkeit „Fork ist Funktion von Präfix/Suffix auf fast allen tail-guten Stellen“ nicht aus. | proved as logical limitation of that input | Zählargument | 1.00 |
| `EMP` | Die numerischen Angaben des Briefings wurden in diesem Lauf nicht reproduziert. | heuristic / externally supplied | Briefing-Empirie | 0.50 |

---

## 4. Elementare Algebra

### Claim `C1`: Tail-Rekursion und Blockformel

Aus der Definition folgt

\[
\begin{aligned}
2\delta_n
 &=\sum_{j\ge1}\frac{g_{n+j}}{2^{j-1}}\\
 &=g_{n+1}+\sum_{j\ge2}\frac{g_{n+j}}{2^{j-1}}\\
 &=g_{n+1}+\delta_{n+1}.
\end{aligned}
\]

Damit gilt (2.1). Wiederholte Anwendung ergibt

\[
\begin{aligned}
\delta_{n+J}
 &=2^J\delta_n-
   \bigl(2^{J-1}g_{n+1}+2^{J-2}g_{n+2}+\cdots+g_{n+J}\bigr)\\
 &=2^J\delta_n-C_{n,J}.
\end{aligned}
\]

Die absolute Konvergenz folgt beispielsweise aus \(p_n=O(n\log(n+2))\), denn geometrische Gewichte dominieren jedes polynomisch-logarithmische Wachstum.

### Claim `C2`: Rationalität erzeugt ein gerades Tail-Gitter

Angenommen

\[
S=\frac{A}{2^s b},\qquad A\in\mathbb Z,
\quad s\ge0,
\quad b\ge1\text{ ungerade}.
\]

Für \(n\ge s\) gilt

\[
2^nS=
\sum_{r=1}^{n}p_r2^{n-r}+\nu_n.
\]

Daher

\[
b\nu_n=A2^{n-s}-b\sum_{r=1}^{n}p_r2^{n-r}\in\mathbb Z,
\]

und somit

\[
b\delta_n=b\nu_n-bp_{n+1}\in\mathbb Z.
\]

Für \(n\ge\max(s+1,2)\) ist \(A2^{n-s}\) gerade. In der endlichen Summe

\[
\sum_{r=1}^{n}p_r2^{n-r}
\]

trägt modulo \(2\) nur der letzte Summand \(p_n\) bei; dieser ist für \(n\ge2\) ungerade. Weil auch \(b\) ungerade ist, ist \(b\nu_n\) ungerade. Ebenso ist \(bp_{n+1}\) ungerade. Also

\[
b\delta_n\in2\mathbb Z.
\tag{4.1}
\]

**Markierung Briefing-Fakt PARITY:** Hier wird die im Briefing hervorgehobene Paritätsverschärfung verwendet; der Beweis ist vollständig inline gegeben.

### Claim `C3`: Quantisierung nach einem gemeinsamen Präfix

Seien

\[
g_{n+i}=g_{m+i}\qquad(1\le i\le J).
\]

Dann ist \(C_{n,J}=C_{m,J}\), und (2.2) liefert

\[
\delta_{n+J}-\delta_{m+J}
=2^J(\delta_n-\delta_m).
\]

Liegen \(b\delta_n\) und \(b\delta_m\) im geraden Gitter, so gilt

\[
b(\delta_{n+J}-\delta_{m+J})\in2^{J+1}\mathbb Z.
\tag{4.2}
\]

Insbesondere folgt aus

\[
\left|\delta_{n+J}-\delta_{m+J}\right|
 <\frac{2^{J+1}}b
\]

bereits die exakte Gleichheit

\[
\delta_{n+J}=\delta_{m+J}.
\tag{4.3}
\]

---

## 5. Fork-Merge-Hypothese `(FM)`

### 5.1 Asymptotische Form

`(FM)` bedeutet: Es gibt Folgen

\[
n_r<m_r,\quad J_r,K_r\ge1,\quad H_r>0,
\]

mit \(\min(n_r,m_r)\to\infty\), so dass für jedes \(r\):

1. gemeinsames Präfix:
   \[
   g_{n_r+i}=g_{m_r+i}\qquad(1\le i\le J_r);
   \]
2. echter Fork:
   \[
   a_r:=g_{n_r+J_r+1}
e
   a'_r:=g_{m_r+J_r+1};
   \]
3. gemeinsamer Merge-Suffix:
   \[
   g_{n_r+J_r+1+i}
   =g_{m_r+J_r+1+i}
   \qquad(1\le i\le K_r);
   \]
4. vier kleine Tails:
   \[
   \max\left\{
   \delta_{n_r+J_r},\delta_{m_r+J_r},
   \delta_{n_r+J_r+K_r+1},
   \delta_{m_r+J_r+K_r+1}
   \right\}\le H_r;
   \]
5. Größenbedingungen:
   \[
   \frac{H_r}{2^{J_r}}\longrightarrow0,
   \qquad
   \frac{H_r}{2^{K_r}}\longrightarrow0.
   \]

### 5.2 Claim `C4`: Fork-Merge-Widerspruch

Angenommen, \(S=A/(2^sb)\) mit ungeradem \(b\). Wähle \(r\) so groß, dass alle relevanten Indizes im geraden Tail-Gitter liegen und

\[
H_r<\frac{2^{J_r}}b,
\qquad
H_r<2^{K_r}.
\tag{5.1}
\]

Aus den beiden ersten Tail-Schranken folgt

\[
|\delta_{n_r+J_r}-\delta_{m_r+J_r}|
\le 2H_r<\frac{2^{J_r+1}}b.
\]

Mit (4.2) folgt die exakte Gleichheit

\[
\delta_{n_r+J_r}=\delta_{m_r+J_r}.
\]

Nach dem unterschiedlichen nächsten Gap ist daher

\[
\begin{aligned}
D_1
&:=\delta_{n_r+J_r+1}-\delta_{m_r+J_r+1}\\
&=2\bigl(\delta_{n_r+J_r}-\delta_{m_r+J_r}\bigr)
 -(a_r-a'_r)\\
&=a'_r-a_r.
\end{aligned}
\]

Auf dem gemeinsamen Suffix verdoppelt sich diese Differenz in jedem Schritt, also

\[
D_{K_r+1}
=2^{K_r}(a'_r-a_r).
\tag{5.2}
\]

Für hinreichend große Indizes sind alle Primzahllücken gerade. Weil \(a_r\ne a'_r\), gilt daher

\[
|a'_r-a_r|\ge2,
\]

und aus (5.2)

\[
|D_{K_r+1}|\ge2^{K_r+1}.
\tag{5.3}
\]

Andererseits geben die beiden Endtail-Schranken

\[
|D_{K_r+1}|
\le2H_r<2^{K_r+1},
\]

im Widerspruch zu (5.3).

Damit ist `C4` bewiesen.

### 5.3 Claim `C5`: `(FM)` impliziert Irrationalität

Jede rationale Zahl besitzt eine Darstellung \(A/(2^sb)\) mit ungeradem \(b\). Claim `C4` schließt jede solche Darstellung aus. Folglich ist \(S\) irrational.

**Markierung Briefing-Fakt EXACT-LOCKING:** Der Exact-Locking-Gegenmodellhinweis wird hier nur konzeptionell benutzt: Der Fork-Merge-Beweis benötigt keine Bedingung \(\delta\ne c\) und ist deshalb gegen exaktes Locking immun.

**Markierung Briefing-Fakt PRIMORIAL:** Die Primorial-Obstruktion wird im Fork-Merge-Beweis nicht benötigt. Insbesondere verlangt `(FM)` weder lange konstante Lückenfolgen noch einen festen wiederholten Gap-Wert.

---

## 6. Das exakt verwendete Paket `HL_quant`

### 6.1 Warum eine Zusatzklausel nötig ist

Eine uniforme asymptotische Formel für jedes einzelne Lückenwort liefert noch nicht automatisch, dass nach Fixierung eines langen Präfixes und Suffixes das mittlere Gap mehrere Werte mit nennenswerter Gesamtmasse annimmt. Genau diese bedingte Nichtdeterministik ist der Informationsgehalt, den der Fork-Merge-Schritt benötigt.

Tao formulierte auf der Diskussionsseite die Erwartung, dass eine genügend quantitative und uniforme Primzahl-\(k\)-Tupel-Vermutung statistische Kontrolle über ungefähr \(\log\log n\) aufeinanderfolgende Lücken geben könnte; Shannon-Entropie wurde als mögliches Werkzeug genannt. Das folgende Paket macht den hierfür tatsächlich benötigten Entropieschritt explizit.

### 6.2 Wörter, Zählfunktion und lokales Modell

Für ein Wort

\[
d=(d_1,\ldots,d_\ell)\in(2\mathbb N_{>0})^\ell
\]

setze

\[
h_0=0,\qquad h_i=d_1+\cdots+d_i,
\qquad \operatorname{span}(d)=h_\ell,
\]

und

\[
\mathcal H(d)=\{h_0,h_1,\ldots,h_\ell\}.
\]

Die Singularreihe ist

\[
\mathfrak S(\mathcal H)
:=\prod_q
\frac{1-\nu_q(\mathcal H)/q}{(1-1/q)^{|\mathcal H|}},
\]

wobei \(\nu_q(\mathcal H)\) die Anzahl der von \(\mathcal H\) modulo \(q\) belegten Restklassen bezeichnet. Für nicht-admissible \(\mathcal H\) setzen wir die Singularreihe gleich null.

Die tatsächliche Zahl konsekutiver Vorkommen ist

\[
N_x(d):=
\#\{n:x\le p_n<2x,\ g_{n+i}=d_i\ (1\le i\le\ell)\}.
\]

Als explizites konsekutives Hardy–Littlewood/Poisson-Lokalmodell verwenden wir

\[
M_x(d):=
\mathbf 1_{\mathcal H(d)\text{ admissibel}}
\int_x^{2x}
\frac{\mathfrak S(\mathcal H(d))}{(\log t)^{\ell+1}}
\exp\!\left(-\frac{\operatorname{span}(d)}{\log t}\right)dt.
\tag{6.1}
\]

Der Exponentialfaktor modelliert, dass zwischen den vorgeschriebenen Primzahlen keine weiteren Primzahlen liegen. Dies ist eine **Hypothesenformulierung**, kein derzeit bewiesenes Theorem. Gallagher zeigte für feste Dimension, dass geeignete uniforme Hardy–Littlewood-Annahmen zu Poisson-Statistik in logarithmisch kurzen Intervallen führen; das hier benötigte Fenster wächst dagegen wie \(\log\log x\). Siehe P. X. Gallagher, *On the distribution of primes in short intervals*, Mathematika 23 (1976), sowie die moderne Diskussion in V. Kuperberg, [arXiv:2210.09775](https://arxiv.org/abs/2210.09775).

### 6.3 Vollständige Definition von `HL_quant`

Fixiere die numerischen Konstanten

\[
C_{\rm win}=20,
\qquad A_{\rm err}=10,
\qquad A_{\rm block}=8,
\qquad \eta=\frac1{20}.
\]

`HL_quant` ist die Konjunktion der folgenden Aussagen für alle hinreichend großen \(x\).

#### `HLQ.Q1` — uniforme konsekutive Wortzählung

Für jedes

\[
1\le\ell\le C_{\rm win}\log\log x
\]

und jedes gerade positive Wort \(d\) der Länge \(\ell\) mit

\[
\operatorname{span}(d)\le(\log x)^3
\]

gilt gleichmäßig

\[
|N_x(d)-M_x(d)|
\le (\log x)^{-A_{\rm err}}M_x(d).
\tag{Q1}
\]

Ist \(M_x(d)=0\), verlangt `(Q1)` also \(N_x(d)=0\).

Die relative Form ist wesentlich: Sie lässt sich ohne Verlust über beliebige Familien solcher Wörter summieren.

#### `HLQ.Q2` — gemittelte Fork-Antikonzentration des Modells

Setze

\[
J_x=K_x=\left\lceil A_{\rm block}\log\log x\right\rceil,
\qquad L_x=J_x+K_x+1.
\]

Ein Wort der Länge \(L_x\) schreiben wir als

\[
d=(W,a,V),
\]

wobei \(|W|=J_x\), \(|V|=K_x\), und \(a\) das Fork-Gap ist. Alle folgenden Summen laufen über positive gerade Wörter mit Gesamtspannweite höchstens \((\log x)^3\). Dann gilt

\[
\sum_{W,V}\max_a M_x(W,a,V)
\le(1-\eta)
\sum_{W,a,V}M_x(W,a,V).
\tag{Q2}
\]

Dies ist die präzise quantitative Form der benötigten bedingten Entropie: Selbst nach Kenntnis von Präfix und Suffix kann ein einzelner Fork-Wert höchstens den Anteil \(1-\eta\) der Modellmasse tragen, im Mittel über die Kontexte \((W,V)\).

#### `HLQ.Q3` — Parameterkompatibilität

Für große \(x\) gilt

\[
L_x\le C_{\rm win}\log\log x.
\tag{Q3}
\]

Mit den gewählten Konstanten ist dies elementar, weil

\[
L_x\le16\log\log x+3<20\log\log x.
\]

### 6.4 Wo jede Uniformität ausgegeben wird

| Bestandteil | Verwendung |
|---|---|
| Fenster \(\ell\le20\log\log x\) | erlaubt die vollständigen Wörter \((W,a,V)\) mit \(J=K=\lceil8\log\log x\rceil\) |
| Shift-/Span-Grenze \((\log x)^3\) | umfasst alle lokal typischen Blöcke; `C8` zeigt, dass die übrigen Startstellen Dichte \(o(1)\) haben |
| relativer Fehler \((\log x)^{-10}\) | überträgt `(Q2)` mit festem positivem Verlust von Modellzählungen auf tatsächliche Primzahlzählungen |
| feste Entropielücke \(\eta=1/20\) | überlebt das Entfernen der tail-schlechten und span-schlechten Startstellen |
| Blockkonstante \(8\) | macht \(2^J,2^K\) größer als \((\log x)^4\), denn \(8\log 2>4\) |

---

## 7. Unbedingte Tail- und Span-Abschätzungen

Sei

\[
I_x:=\{n:x\le p_n<2x\}.
\]

Dann ist \(|I_x|\asymp x/\log x\).

### Claim `C6`: mittlerer Tail ist \(O(\log x)\)

Für ein festes \(r=O(\log\log x)\) gilt

\[
\sum_{n\in I_x}\delta_{n+r}
=\sum_{j\ge1}2^{-j}
  \sum_{n\in I_x}g_{n+r+j}.
\]

Da \(I_x\) ein zusammenhängendes Primindexintervall ist, teleskopiert die innere Summe. Mit der groben Standardabschätzung

\[
p_m\ll m\log(m+2)
\]

folgt

\[
\sum_{n\in I_x}g_{n+r+j}
\ll x+j\log(x+j+2).
\]

Die geometrische Summation über \(j\) ergibt

\[
\sum_{n\in I_x}\delta_{n+r}\ll x.
\]

Division durch \(|I_x|\gg x/\log x\) liefert

\[
\frac1{|I_x|}\sum_{n\in I_x}\delta_{n+r}
\ll\log x,
\tag{7.1}
\]

gleichmäßig für \(r=O(\log\log x)\).

### Claim `C7`: vier tail-schlechte Mengen sind vernachlässigbar

Setze

\[
H_x:=(\log x)^4.
\]

Für jede der vier Verschiebungen

\[
r\in\{J_x,
       J_x+K_x+1\}
\]

und für beide später zu wählenden Startstellen liefert Markovs Ungleichung aus (7.1)

\[
\#\{n\in I_x:\delta_{n+r}>H_x\}
\ll |I_x|(\log x)^{-3}.
\tag{7.2}
\]

Die Vereinigung der benötigten schlechten Mengen hat daher weiterhin Anteil \(O((\log x)^{-3})\).

### Claim `C8`: span-schlechte Blöcke sind vernachlässigbar

Für \(L=L_x\) gilt

\[
\operatorname{span}(g_{n+1},\ldots,g_{n+L})
=p_{n+L+1}-p_{n+1}.
\]

Die Summe dieser Spannweiten über \(n\in I_x\) ist durch \(O(Lx)\) beschränkt, da jede der \(L\) verschobenen Gap-Summen teleskopiert. Markov liefert

\[
\#\{n\in I_x:\operatorname{span}>(\log x)^3\}
\ll |I_x|\frac{L\log x}{(\log x)^3}
=|I_x|\,O\!\left(\frac{\log\log x}{(\log x)^2}\right).
\tag{7.3}
\]

---

## 8. Beweis `HL_quant ⇒ (FM)`

### 8.1 Tatsächliche Fork-Antikonzentration

Definiere

\[
T_x:=\sum_{W,a,V}N_x(W,a,V)
\]

und

\[
D_x:=\sum_{W,V}\max_a N_x(W,a,V),
\]

wobei nur Wörter der Länge \(L_x\) mit Spannweite \(\le(\log x)^3\) summiert werden.

Aus `(Q1)` folgt termweise

\[
N_x(W,a,V)
\le(1+\varepsilon_x)M_x(W,a,V),
\qquad
\varepsilon_x=(\log x)^{-10},
\]

und ebenso

\[
T_x\ge(1-\varepsilon_x)
\sum_{W,a,V}M_x(W,a,V).
\]

Daher ergibt `(Q2)`

\[
\begin{aligned}
D_x
&\le(1+\varepsilon_x)
   \sum_{W,V}\max_a M_x(W,a,V)\\
&\le(1+\varepsilon_x)(1-\eta)
   \sum_{W,a,V}M_x(W,a,V)\\
&\le\frac{1+\varepsilon_x}{1-\varepsilon_x}
   (1-\eta)T_x.
\end{aligned}
\]

Für große \(x\) ist somit

\[
D_x\le(1-\eta/2)T_x.
\tag{8.1}
\]

**Verwendung `HL_quant`:** `(Q1)` wird genau zur Übertragung vom Modell auf reale Zählungen verwendet; `(Q2)` liefert die feste Entropielücke; `(Q3)` legitimiert die Fensterlänge.

### 8.2 Entfernen schlechter Tails

Nach `C7` und `C8` ist die Zahl der Startstellen in \(T_x\), für die

- eine der benötigten Tailgrößen \(\delta_{n+J_x}\), \(\delta_{n+J_x+K_x+1}\) größer als \(H_x\) ist, oder
- die lokale Spannweite größer als \((\log x)^3\) ist,

von der Form \(o(T_x)\). Insbesondere ist sie für große \(x\) kleiner als \((\eta/4)T_x\).

Nenne die übrigen Startstellen `gut`.

### 8.3 Pigeonhole mit Antikonzentration

Angenommen, für jeden Kontext \((W,V)\) gäbe es unter den guten Startstellen höchstens einen Fork-Wert \(a\). Dann wäre die Gesamtzahl guter Startstellen höchstens

\[
\sum_{W,V}\max_a N_x(W,a,V)=D_x.
\]

Andererseits ist die Zahl guter Startstellen mindestens

\[
(1-\eta/4)T_x,
\]

während (8.1)

\[
D_x\le(1-\eta/2)T_x
\]

gibt. Das ist unmöglich.

Also existieren zwei verschiedene Startstellen \(n_x,m_x\) mit demselben \(W\), demselben \(V\), aber unterschiedlichen Fork-Gaps \(a\ne a'\), und alle vier benötigten Tails sind höchstens

\[
H_x=(\log x)^4.
\]

### 8.4 Größenverhältnisse

Mit

\[
J_x=K_x=\lceil8\log\log x\rceil
\]

gilt

\[
2^{J_x},2^{K_x}
\ge(\log x)^{8\log2}.
\]

Da

\[
8\log2\approx5.545>4,
\]

folgt

\[
\frac{H_x}{2^{J_x}}\to0,
\qquad
\frac{H_x}{2^{K_x}}\to0.
\]

Außerdem gehen \(n_x,m_x\to\infty\), weil \(p_{n_x},p_{m_x}\in[x,2x]\) und \(x\to\infty\).

Damit ist `(FM)` bewiesen. Dies ist Claim `C10`.

### 8.5 Hauptsatz

Aus `C10` und `C5` folgt:

> **Konditionaler Hauptsatz.** Gilt `HL_quant` in der exakten Form `(Q1)`–`(Q3)`, so ist
> \[
> \sum_{n\ge1}\frac{p_n}{2^n}
> \]
> irrational.

---

## 9. Warum eine gewöhnliche punktweise HL-Form nicht genügt

Der Beweis benötigt nach dem Entfernen einer kleinen, nur über Tail-Mittelwerte kontrollierten Ausnahmemenge noch zwei Vorkommen mit gleichem Kontext \((W,V)\) und verschiedenem Fork-Gap.

Eine Formel

\[
N_x(d)\sim M_x(d)
\]

für jedes einzelne Wort \(d\), ohne eine über große Wortfamilien summierbare relative Uniformität, erlaubt nicht, Fehler über die etwa

\[
\exp\bigl(\Theta((\log\log x)^2)\bigr)
\]

möglichen Wörter zu summieren. Selbst uniforme Existenz jedes einzelnen Wortes kontrolliert außerdem nicht, ob die tail-guten Vorkommen nach Entfernen einer kleinen globalen Ausnahmemenge in jedem Kontext auf genau einen Fork-Wert kollabieren.

Die Klausel `(Q2)` ist daher kein kosmetischer Zusatz. Sie ist der exakt benötigte Shannon-/Min-Entropieinhalt.

---

## 10. Beziehung zu Schlage-Puchta `[ScPu11]`

Das Paper ist abrufbar:

- J.-C. Schlage-Puchta, *The irrationality of some number theoretical series*, Acta Arith. 126 (2007), 295–303, [arXiv:1105.1451](https://arxiv.org/abs/1105.1451).

Das Paper beweist unter anderem lineare Unabhängigkeit bestimmter Fakultätsreihen. Im Beweis des dortigen Theorems 3 werden:

1. aus angenommener Rationalität sehr kleine Abstände zu ganzen Zahlen gewonnen;
2. Laurent-Entwicklungen und rekursive Elimination verwendet, um nichtverschwindende Polynome in aufeinanderfolgenden Primzahllücken zu isolieren;
3. mit einem Selberg-Sieb gezeigt, dass ein nichttriviales Lückenpolynom nur auf einer dünnen Menge verschwindet;
4. mittels Weyl–van der Corput/Erdős–Turán eine Diskrepanzabschätzung erzeugt, die der angenommenen Near-Integrality widerspricht.

Dies ist ein echter und relevanter Vorläufer. Für die Basis-2-Reihe fehlt jedoch genau die Uniformisierung auf eine wachsende Zahl \(k\asymp\log\log x\) von Lücken sowie eine Existenz-/Antikonzentrationsaussage. Das Selberg-Sieb in `[ScPu11]` liefert vor allem obere Schranken für Ausnahmemengen bei festem Fenster; es ersetzt nicht `(Q2)`.

---

## 11. Sekundärroute: \(v_2\)-Blöcke

Aus (2.2) folgt unter Rationalität und für große \(n\)

\[
b\delta_{n+J}=2^J(b\delta_n)-bC_{n,J}.
\]

Da \(b\delta_n\in2\mathbb Z\), ist der erste Term durch \(2^{J+1}\) teilbar. Weil \(b\) ungerade ist,

\[
v_2(bC_{n,J})=v_2(C_{n,J}).
\]

Daher gilt konservativ

\[
v_2(b\delta_{n+J})
\ge\min\{J,v_2(C_{n,J})\}.
\]

Da \(b\delta_{n+J}\) eine positive ganze Zahl ist,

\[
b\delta_{n+J}
\ge2^{\min\{J,v_2(C_{n,J})\}}.
\]

Somit impliziert die Existenz einer Folge von Blöcken mit

\[
\min\{J,v_2(C_{n,J})\}
-\log_2\delta_{n+J}\to+\infty
\]

die Irrationalität. Denn die Gitterabschätzung ist äquivalent zu

\[
b\ge
\frac{2^{\min\{J,v_2(C_{n,J})\}}}{\delta_{n+J}},
\]

während die rechte Seite unter der Hypothese gegen unendlich geht; dies ist für den festen Nennerteil \(b\) unmöglich.

**Markierung Briefing-Fakt PARITY:** Die gerade Gitterstruktur verbessert die Potenzschwelle um einen Faktor 2; die konservative Form oben genügt bereits.

Eine Ableitung dieser \(v_2\)-Existenzhypothese aus dem oben formulierten `HL_quant` ist nicht enthalten. Sie würde eine andere, 2-adische Antikonzentrationsklausel für den Blockcode benötigen.

---

## 12. Sekundärroute: Wortpotenzen

Sei \(w=(c_1,\ldots,c_r)\) und

\[
B_w:=\sum_{i=1}^{r}2^{r-i}c_i,
\qquad
\alpha_w:=\frac{B_w}{2^r-1}=\frac{m_w}{q_w}
\]

in gekürzter Form. Für \(K\) direkte Wiederholungen des Wortes gilt durch affine Iteration

\[
\delta_n-\alpha_w
=2^{-Kr}\bigl(\delta_{n+Kr}-\alpha_w\bigr).
\tag{12.1}
\]

Unter Rationalität liegt \(b\delta_n\) im Ganzzahlgitter. Falls \(q_w\nmid b\), kann \(\delta_n\ne\alpha_w\) nicht näher als \(1/(bq_w)\) an \(\alpha_w\) liegen. Aus (12.1) folgt daher

\[
|\delta_{n+Kr}-\alpha_w|
\ge\frac{2^{Kr}}{bq_w}.
\]

Folglich impliziert jede Folge von Wortpotenzen mit \(q_w\to\infty\), \(q_w\nmid b\) schließlich, und

\[
\frac{q_w|\delta_{n+Kr}-\alpha_w|}{2^{Kr}}\to0
\]

die Irrationalität. Konstante Wörter haben \(q_w=1\) und sind die degenerierte Equal-Run-Situation.

**Markierung Briefing-Fakt PRIMORIAL:** Lange Wiederholungen eines festen Wortes können primorialartige lokale Obstruktionen besitzen. Die Wortpotenzroute muss deshalb wachsende Wörter oder kleine Wiederholungszahlen zulassen.

---

## 13. Lean-4-orientierte Zerlegung

Die folgenden Signaturen sind ein formalisierungsnaher Blueprint; sie sind nicht in diesem Lauf gegen eine konkrete Mathlib-Version kompiliert worden. Mathlib enthält die relevanten Module `Mathlib.Data.Nat.Prime.Nth` und `Mathlib.NumberTheory.Real.Irrational`.

### 13.1 0-indizierte Definitionen

```lean
import Mathlib.Data.Nat.Prime.Nth
import Mathlib.NumberTheory.Real.Irrational
import Mathlib.Topology.Algebra.InfiniteSum.Real

open scoped BigOperators

noncomputable def P (n : ℕ) : ℕ := Nat.nth Nat.Prime n

def G (n : ℕ) : ℕ := P (n + 1) - P n

noncomputable def delta (n : ℕ) : ℝ :=
  ∑' j : ℕ, (G (n + j) : ℝ) / (2 : ℝ) ^ (j + 1)

noncomputable def erdos251Sum : ℝ :=
  ∑' n : ℕ, (P n : ℝ) / (2 : ℝ) ^ n
```

Hier ist `erdos251Sum = 2*S` in der 1-indizierten mathematischen Notation.

### 13.2 `delta_block`

```lean
def blockCode (n J : ℕ) : ℕ :=
  ∑ i in Finset.range J, 2 ^ (J - 1 - i) * G (n + i)

theorem delta_step (n : ℕ) :
    delta (n + 1) = 2 * delta n - G n := by
  -- tsum shift, absolute summability
  sorry

theorem delta_block (n J : ℕ) :
    delta (n + J) = (2 : ℝ) ^ J * delta n - blockCode n J := by
  induction J with
  | zero => simp [blockCode]
  | succ J ih =>
      rw [Nat.add_succ, delta_step, ih]
      -- algebra and Finset.sum_range_succ
      ring_nf
      sorry
```

Für die Formalisierung ist es wahrscheinlich bequemer, `blockCode` direkt als reelle endliche Summe zu definieren, damit Cast-Lemmata minimiert werden.

### 13.3 `rational_delta_eventually_lattice`

```lean
def RationalReal (x : ℝ) : Prop := ∃ q : ℚ, (q : ℝ) = x

theorem rational_delta_eventually_lattice
    (hRat : RationalReal erdos251Sum) :
    ∃ s b : ℕ, 0 < b ∧ Odd b ∧
      ∀ n ≥ s, ∃ z : ℤ, (b : ℝ) * delta n = z := by
  sorry

theorem rational_delta_eventually_even_lattice
    (hRat : RationalReal erdos251Sum) :
    ∃ s b : ℕ, 0 < b ∧ Odd b ∧
      ∀ n ≥ s, ∃ z : ℤ, (b : ℝ) * delta n = 2 * z := by
  sorry
```

Es ist sinnvoll, die rationale Darstellung zunächst als

```lean
∃ A : ℤ, ∃ s b : ℕ, 0 < b ∧ Odd b ∧
  erdos251Sum = A / ((2 : ℝ)^s * b)
```

zu normalisieren.

### 13.4 `repeated_block_quantization`

```lean
def SamePrefix (n m J : ℕ) : Prop :=
  ∀ i < J, G (n + i) = G (m + i)

theorem repeated_block_quantization
    {b n m J : ℕ}
    (hb : 0 < b)
    (hn : ∃ z : ℤ, (b : ℝ) * delta n = 2 * z)
    (hm : ∃ z : ℤ, (b : ℝ) * delta m = 2 * z)
    (hprefix : SamePrefix n m J) :
    ∃ z : ℤ,
      (b : ℝ) * (delta (n + J) - delta (m + J))
        = (2 : ℝ) ^ (J + 1) * z := by
  rw [delta_block, delta_block]
  have hcode : blockCode n J = blockCode m J := by
    -- extensional equality of finite sums from hprefix
    sorry
  rw [hcode]
  obtain ⟨zn, hzn⟩ := hn
  obtain ⟨zm, hzm⟩ := hm
  refine ⟨zn - zm, ?_⟩
  -- linear arithmetic/ring
  sorry
```

### 13.5 `fork_merge_contradiction`

```lean
def SameSuffix (n m J K : ℕ) : Prop :=
  ∀ i < K, G (n + J + 1 + i) = G (m + J + 1 + i)

def FourTailBound (n m J K : ℕ) (H : ℝ) : Prop :=
  delta (n + J) ≤ H ∧
  delta (m + J) ≤ H ∧
  delta (n + J + K + 1) ≤ H ∧
  delta (m + J + K + 1) ≤ H

theorem fork_merge_contradiction
    {b n m J K : ℕ} {H : ℝ}
    (hb : 0 < b)
    (hodd : Odd b)
    (hlattice :
      (∃ zn : ℤ, (b : ℝ) * delta n = 2 * zn) ∧
      (∃ zm : ℤ, (b : ℝ) * delta m = 2 * zm))
    (hprefix : SamePrefix n m J)
    (hfork : G (n + J) ≠ G (m + J))
    (hsuffix : SameSuffix n m J K)
    (hevenGaps : Even (G (n + J)) ∧ Even (G (m + J)))
    (htails : FourTailBound n m J K H)
    (hsmallJ : H < (2 : ℝ)^J / b)
    (hsmallK : H < (2 : ℝ)^K) : False := by
  -- 1. repeated_block_quantization
  -- 2. |difference at fork entrance| < 2^(J+1)/b => equality
  -- 3. one fork step gives difference of distinct even gaps
  -- 4. K equal suffix steps double the difference
  -- 5. lower bound 2^(K+1), upper bound 2H
  sorry
```

### 13.6 Nennerfreie Form von `(FM)`

Für Lean ist eine \(\forall B\forall N\exists\)-Form praktischer als Grenzwerte:

```lean
def ForkMergeHyp : Prop :=
  ∀ B N : ℕ, 0 < B →
    ∃ n m J K : ℕ, ∃ H : ℝ,
      N ≤ n ∧ n < m ∧
      SamePrefix n m J ∧
      G (n + J) ≠ G (m + J) ∧
      SameSuffix n m J K ∧
      FourTailBound n m J K H ∧
      H < (2 : ℝ)^J / B ∧
      H < (2 : ℝ)^K
```

Dann:

```lean
theorem erdos_251_of_small_tail_fork_merge
    (hFM : ForkMergeHyp) : Irrational erdos251Sum := by
  intro hnot
  have hRat : RationalReal erdos251Sum := by
    -- unfold Irrational / classical rational-or-irrational interface
    sorry
  obtain ⟨s, b, hb, hodd, hlattice⟩ :=
    rational_delta_eventually_even_lattice hRat
  obtain ⟨n, m, J, K, H, hn, hnm, hp, hf, hs, ht, hJ, hK⟩ :=
    hFM b s hb
  exact fork_merge_contradiction
    hb hodd ⟨hlattice n hn, hlattice m (le_trans hn hnm.le)⟩
    hp hf hs (by exact eventually_even_prime_gaps ...) ht hJ hK
```

### 13.7 `HLQuant`-Struktur

```lean
abbrev GapWord (ℓ : ℕ) := Fin ℓ → ℕ

structure HLQuant where
  x0 : ℝ
  uniform_count :
    ∀ x ≥ x0, ∀ ℓ : ℕ,
      ℓ ≤ Nat.ceil (20 * Real.log (Real.log x)) →
      ∀ d : GapWord ℓ,
        WordEvenPositive d →
        wordSpan d ≤ (Real.log x)^3 →
        |patternCount x d - hlModel x d|
          ≤ (Real.log x)^(-10) * hlModel x d
  model_fork_entropy :
    ∀ x ≥ x0,
      modelDeterministicMass x
        (Nat.ceil (8 * Real.log (Real.log x)))
        (Nat.ceil (8 * Real.log (Real.log x)))
      ≤ (1 - (1 / 20 : ℝ)) * modelTotalMass x
```

Die eigentliche Formalisierung sollte Zählwerte als `ℕ`, danach als `ℝ` gecastet, und die endlichen Wortmengen über eine explizite Span-Schranke als `Finset` darstellen.

Schließlich:

```lean
theorem fork_merge_of_HLQuant (hHL : HLQuant) : ForkMergeHyp := by
  -- C6-C8, Q1->reale Entropielücke, Pigeonhole
  sorry

theorem erdos_251 (hHL : HLQuant) :
    Irrational (∑' n : ℕ,
      (Nat.nth Nat.Prime n : ℝ) / (2 : ℝ)^n) := by
  exact erdos_251_of_small_tail_fork_merge (fork_merge_of_HLQuant hHL)
```

Wichtig: Der vom Nutzer genannte unbedingte Zielname

```lean
theorem erdos_251 : Irrational (...)
```

kann gegenwärtig nicht ohne eine unbewiesene Hypothese abgeschlossen werden, weil das zugrunde liegende Erdős-Problem offen ist. Der ehrliche formale Hauptsatz ist daher zunächst `erdos_251 (hHL : HLQuant)`.

---

## 14. Where I am stuck

Der exakte fehlende Baustein ist:

> **Beweise `(Q2)` — eine feste, gemittelte bedingte Entropielücke für das zentrale Primzahllückengap nach Fixierung von \(J,K\asymp\log\log x\) exakten Nachbarlücken — aus einer akzeptablen, möglichst standardnahen uniformen Hardy–Littlewood-Primzahl-\(k\)-Tupel-Vermutung mit Verschiebungen bis \((\log x)^3\).**

Genauer fehlen zwei Übergänge:

1. von uniformen Zählungen nicht notwendig konsekutiver Primzahl-\(k\)-Tupel zu konsekutiven Gap-Wörtern mit kontrollierter relativer Fehlersumme;
2. eine uniforme gemittelte Schranke
   \[
   \sum_{W,V}\max_a M_x(W,a,V)
   \le(1-\eta)\sum_{W,a,V}M_x(W,a,V)
   \]
   mit einem von \(x\) unabhängigen \(\eta>0\).

Ohne diesen Entropie-/Antikonzentrationsschritt ist `HL_quant ⇒ FM` nicht gerechtfertigt. Mit ihm ist die gesamte restliche Kette vollständig.

---

## 15. Literatur- und Quellenprüfung

1. **Status des Problems:** Erdős Problems #251 wird als offen geführt und stellt die Irrationalitätsfrage für \(\sum p_n/2^n\).  
   [https://www.erdosproblems.com/251](https://www.erdosproblems.com/251)

2. **Tao-Kommentar:** Partielle Summation reduziert auf die Lückenreihe; eine quantitative uniforme Primzahl-Tupel-Vermutung über ungefähr \(\log\log n\) Lücken und Shannon-Entropie werden als möglicher Ansatz genannt.  
   [https://www.erdosproblems.com/forum/thread/251](https://www.erdosproblems.com/forum/thread/251)

3. **Schlage-Puchta:** J.-C. Schlage-Puchta, *The irrationality of some number theoretical series*, Acta Arith. 126 (2007), 295–303.  
   [https://arxiv.org/abs/1105.1451](https://arxiv.org/abs/1105.1451)

4. **Gallagher-Kontext:** P. X. Gallagher, *On the distribution of primes in short intervals*, Mathematika 23 (1976), 4–9. Gallagher verbindet uniforme Hardy–Littlewood-Annahmen bei fester Dimension mit Poisson-Statistik.

5. **Singularserien/Poisson-Kontext:** V. Kuperberg, *Sums of singular series with large sets and the tail of the distribution of primes*, arXiv:2210.09775.  
   [https://arxiv.org/abs/2210.09775](https://arxiv.org/abs/2210.09775)

6. **Lean-Module:** Mathlib-Dokumentation enthält `Mathlib.Data.Nat.Prime.Nth` und `Mathlib.NumberTheory.Real.Irrational`.  
   [https://leanprover-community.github.io/mathlib4_docs/Mathlib](https://leanprover-community.github.io/mathlib4_docs/Mathlib)

---

## 16. Explizite Kennzeichnung der Briefing-Fakten

- **Primorial obstruction:** respektiert; nicht im Primärbeweis verwendet; verhindert insbesondere keine Fork-Merge-Wörter mit variierenden Gaps.
- **Parity:** vollständig bewiesen und in `C2`, `C3`, `C4` verwendet; liefert den Faktor 2 in der Gitterweite und den Mindestabstand verschiedener Fork-Gaps.
- **Exact-locking countermodel:** nicht als Beweisprämisse verwendet; erklärt, warum Fork-Merge gegenüber Equal-Run-Squeeze vorzuziehen ist.
- **Empirics:** nicht reproduziert und nicht im Beweis verwendet. Die Angaben zu Wiederholungen, minimalen Tail-Differenzen und endlichen Nennerausschlüssen bleiben in diesem Lauf extern gelieferte Daten.

