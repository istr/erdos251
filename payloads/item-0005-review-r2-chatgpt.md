# Adversariale Prüfung des Verdikts zum TaTe-Transfer

## Ergebnis

**Das starke Verdikt ist nicht haltbar.** Haltbar ist lediglich die engere Aussage:

> Die TaTe-Beweisführung lässt sich nicht durch schlichtes Ersetzen von \(\omega(n)\) durch \(p_n\) oder \(g_n\) übertragen.

Nicht bewiesen sind dagegen die wesentlich stärkeren Aussagen „no repair exists“, „an exact bridge is impossible“ und „E2 is the exact remaining wall“. Zwei davon sind in der angegebenen Form sogar wörtlich falsch.

## 1. O1 ist lokal richtig, die globale Schlussfolgerung aber zu stark

TaTe gewinnen (5.2) tatsächlich aus der exakten Identität

\[
\omega(pm)=\omega(m)+1-\mathbf 1_{p\mid m}.
\]

Dadurch wird aus dem Translationsparameter in (5.1) ein Dilationsparameter \(p\). Genau diese Dilatation erzeugt anschließend

\[
r_{\varepsilon,h}
=p_0h+\sum_k(h-k)\varepsilon_kv_k,
\]

sodass der \(h=k\)-Term von \(\varepsilon_k\) unabhängig wird und im alternierenden Würfel verschwindet. Das Paper bestätigt diese Abfolge ausdrücklich; siehe TaTe, §5.1–5.2, Gleichungen (5.1)–(5.8), S. 45–46.

Daraus folgt:

\[
\text{„Der vorhandene Beweis überträgt sich nicht wörtlich.“}
\]

Nicht daraus folgt:

\[
\text{„Keine Modifikation der Methode kann funktionieren.“}
\]

Das wäre ein No-go-Theorem über **alle möglichen Reduktionen**, nicht nur über lineare Nachbildungen von (5.2). Ein solches Theorem steht weder in TaTe noch wird es im Verdikt präzise formuliert.

Die Autoren selbst beschreiben ihre Methode nicht als derart starr: Sie halten Anwendungen auf andere, den Primzahlen hinreichend ähnliche Mengen für plausibel und weisen außerdem auf Modifikationen für andere Basen und für \(\Omega\) hin; siehe TaTe, §1.3, S. 4. Das schließt \(S\) keineswegs ein, warnt aber gegen eine behauptete vollständige Klassifikation der Reichweite.

## 2. O3 enthält eine wörtlich falsche Behauptung: Exakte Count–Value-Brücken existieren

Setze \(g_j=p_{j+1}-p_j\). Dann gelten die exakten Identitäten

\[
\boxed{
S=2+\sum_{j\ge1}\frac{g_j}{2^j}
}
\]

und

\[
\boxed{
S=1+\sum_{m\ge1}2^{-\pi(m)}.
}
\]

Die erste folgt aus

\[
p_n=2+\sum_{j<n}g_j,
\qquad
\sum_{n>j}2^{-n}=2^{-j}.
\]

Für die zweite schreibt man

\[
p_n=1+\sum_{m\ge1}\mathbf 1_{m<p_n}.
\]

Da \(m<p_n\) genau dann gilt, wenn \(\pi(m)<n\), erhält man durch Vertauschen der nichtnegativen Summen

\[
\sum_{n\ge1}\frac{p_n}{2^n}
=1+\sum_{m\ge1}\sum_{n>\pi(m)}2^{-n}
=1+\sum_{m\ge1}2^{-\pi(m)}.
\]

Das ist eine **exakte Reindexierung von der Primzahl-Indexposition zur Wertvariablen \(m\)**. Sie ist möglicherweise analytisch nicht stark genug, aber sie widerlegt die wörtliche Aussage, eine exakte Count–Value-Brücke sei „impossible outright“.

Auch

\[
T:=\sum_p2^{-p}
=\sum_{n\ge1}2^{-p_n}
=\sum_{n\ge1}
  2^{-\,2-\sum_{j<n}g_j}
\]

ist eine exakte, allerdings nichtlineare Funktion derselben Gap-Folge.

Der Produktformel-Schritt in O3 ist deshalb ungültig. Die Ungleichung

\[
|z|_\infty |z|_2\ge1,\qquad
0\ne z\in\mathbb Z[1/2],
\]

kann erst benutzt werden, nachdem ein bestimmter Ausdruck als **nichtnuller dyadischer Rationaler** identifiziert wurde. Weder \(T\) noch die Differenz zweier allgemeiner unendlicher Gap-Funktionale ist automatisch ein Element von \(\mathbb Z[1/2]\).

Aus „\(S\) ist rational“ folgt über die obigen exakten Brücken keineswegs „\(T\) ist rational“. Dafür müsste die Brücke eine rationale Funktion **allein des Wertes \(S\)** sein. Diese zusätzliche Annahme ist im Verdikt weder formuliert noch bewiesen. Die Formulierung

> Any exact bridge would already force rationality of \(T\).

ist daher falsch. Richtig wäre höchstens:

> Eine rationalitätsübertragende Brücke von einer bestimmten, eng definierten Art würde bereits das Problem lösen.

Das ist aber lediglich eine Umformulierung der Schwierigkeit, kein strukturelles Unmöglichkeitsresultat.

## 3. O2 schließt nur lineare Funktionale, nicht die deduktive Closure

Angenommen, Rationalität liefert

\[
b\delta_n\in\mathbb Z
\qquad(n\ge s).
\]

Dann liefert sie sofort für beliebig viele unabhängig gewählte Indizes

\[
b^r\delta_{n_1}\cdots\delta_{n_r}\in\mathbb Z.
\]

Insbesondere ist

\[
\boxed{
b^2(\delta_{n+u}-\delta_n)
   (\delta_{n+v}-\delta_n)\in\mathbb Z
}
\]

eine exakte Drei-Parameter-Familie.

Damit entsteht für O2 ein unausweichliches Dilemma:

1. Umfasst „deductive closure“ solche polynomialen Konsequenzen, ist die Behauptung falsch, es gebe nur die eine echte Zwei-Parameter-Familie der Tail-Periodizität.
2. Umfasst sie nur lineare Funktionale, kann eine lineare Rigidity-Aussage nicht begründen, warum **keine nichtlineare Reparatur** existiert.

Das ist besonders relevant, weil TaTe selbst nach der linearen Kongruenz sofort die nichtlineare Abbildung \(t\mapsto e(t)\), Erwartungswerte, Momente und Varianzen benutzen; siehe TaTe, Gleichungen (5.8)–(5.21), S. 46–49. Eine No-go-Aussage, die nur lineare Gap-Funktionale klassifiziert, deckt daher nicht einmal die Art nichtlinearer Verarbeitung ab, die im Originalbeweis zentral ist.

Hinzu kommt ein formaler Mangel: „closed \(\mathbb Z\)-span“ hat ohne Angabe von

- dem Raum der Funktionale,
- der zugelassenen Koeffizienten,
- der Konvergenzbedingungen und
- der verwendeten Topologie

keinen eindeutigen mathematischen Inhalt. Koeffizientenweise, in einer gewichteten \(\ell^1\)-Norm oder in einer Operatornorm ergeben sich verschiedene Abschlüsse. Eine nicht spezifizierte „Rigidity theorem“ kann keine beweiskräftige universelle Schlussfolgerung tragen.

## 4. O3 verwechselt den Zähler der Reihe mit dem Interface von Theorem 3.1

Theorem 3.1 handelt tatsächlich von zwei 1-beschränkten multiplikativen Funktionen; siehe TaTe, Theorem 3.1, S. 24–25. Aber das TaTe-Verfahren wendet dieses Theorem **nicht direkt auf den Reihenzähler \(\omega(n)\)** an. \(\omega\) ist weder 1-beschränkt noch multiplikativ.

Stattdessen werden erst sehr spät die vollständig multiplikativen Hilfsfunktionen

\[
g_\ell(p)=\mathbf 1_{p\notin J_\ell}
\]

eingeführt. Sie kodieren das Ereignis, dass eine Zahl keinen Primfaktor in einem bestimmten Intervall besitzt. Theorem 3.1 wird ausschließlich auf Korrelationen dieser Hilfsfunktionen angewandt, um den Very-Large-Prime-Fehler zu kontrollieren; siehe TaTe, Gleichungen (5.43)–(5.45), S. 54–56.

Daher ist die Behauptung

> Every series the engine can digest has numerator covariant under argument division by primes.

keine Konsequenz von Theorem 3.1. Das tatsächliche Interface lautet nur:

> Nach allen algebraischen und probabilistischen Reduktionen muss ein verbleibender Fehler durch eine Zweipunktkorrelation geeigneter multiplikativer Hilfsfunktionen kontrollierbar sein.

Es ist nicht ausgeschlossen, dass eine andere Reduktion von \(S\) ebenfalls bei solchen Hilfsfunktionen endet, obwohl \(p_n\) und \(g_n\) selbst nicht multiplikativ sind.

Auch der Verweis auf die Bemerkung über Dreipunktkorrelationen beweist die behauptete Barriere nicht. TaTe sagen dort, dass die spezielle Gleichung

\[
\omega(n)=\omega(n+1)=\omega(n+2)
\]

eine Triple-Correlation-Version verlangen würde; siehe TaTe, Ende von §4, S. 44. Das impliziert nicht, dass jedes Funktional von \(\asymp\log\log x\) Gaps analytische \(\log\log x\)-Punkt-Korrelationen benötigt. Im Irrationalitätsbeweis steht zunächst sogar eine Summe über \(2^K\) Verschiebungen; durch die algebraische Würfelstruktur reduziert sich der analytische Einsatz trotzdem auf Zweipunktkorrelationen. Die Anzahl formaler Terme ist also nicht identisch mit der benötigten Korrelationsordnung.

## 5. EXCH zeigt nicht, dass E2 „der einzige verbleibende Wall“ ist

EXCH ist eine hinreichende Bedingung. Um daraus den behaupteten „exact unconditional residue“ zu machen, wäre eine **Notwendigkeitserklärung** erforderlich:

> Jede mögliche TaTe-artige Widerlegung der Rationalität muss eine Konfiguration E1–E5 oder insbesondere E2 erzeugen.

Eine solche Erklärung fehlt.

Tatsächlich zeigt schon dieselbe Tail-Algebra eine größere Klasse möglicher Konfigurationen. Für beliebige Indizes \(t,u\) und jede Blocklänge \(L\) gilt

\[
\delta_t-\delta_u
=
\sum_{i=1}^{L}
 \frac{g_{t+i}-g_{u+i}}{2^i}
+
\frac{\delta_{t+L}-\delta_{u+L}}{2^L}.
\]

Nachdem ein Prefix-Argument \(\delta_t=\delta_u\) erzwungen hat, reicht daher jede Konfiguration mit

\[
\left|
\sum_{i=1}^{L}
 \frac{g_{t+i}-g_{u+i}}{2^i}
\right|
>
2^{-L}\left|\delta_{t+L}-\delta_{u+L}\right|
\]

für einen Widerspruch. Es ist **nicht notwendig**, dass genau eine Lücke verschieden und alle übrigen identisch sind. Mehrere verschiedene Lücken dürfen auftreten, solange ihre dyadisch gewichtete Differenz nicht durch den Endtail kompensiert wird.

E2 ist somit eine besonders saubere Hamming-Distanz-\(1\)-Bedingung, aber nicht die logisch einzige mögliche Austauschbedingung. Durchschnittliche Separation, mehrere kontrollierte Unterschiede oder eine charakteristische-Funktions-Variante könnten E2 umgehen.

Der zitierte Maynard-Text behandelt wohlverteilte Teilmengen der Primzahlen und garantiert darin nahe Primcluster. Seine künstlichen Gegenbeispiele zeigen, dass bloße Wohlverteilung bestimmte vorgeschriebene Muster nicht erzwingt. Sie sind aber kein Unmöglichkeitssatz für die tatsächliche Primfolge unter zusätzlicher arithmetischer Information.

Eine kleine interne Ungenauigkeit steckt zudem in der skizzierten EXCH-Rechnung: Aus

\[
0=\frac{d_1}{2}+2^{-(K+1)}\Delta_{\rm end},
\qquad
0\le\delta_{\rm end}^{(1)},\delta_{\rm end}^{(2)}\le2^K,
\]

folgt

\[
|d_1|=2^{-K}|\Delta_{\rm end}|\le1,
\]

nicht zwingend \(<1\). Der Widerspruch bleibt bestehen, weil eine nichtnullige Differenz hinreichend später Primlücken gerade und daher mindestens \(2\) im Betrag ist. Es ist kein tödlicher Fehler, aber die als „proof-level“ bezeichnete Darstellung ist an dieser Stelle nicht exakt.

## Revidiertes Verdikt

Die durch das Material gedeckte Aussage lautet:

> **NO VERBATIM TRANSFER IS PRESENTLY EXHIBITED.**  
> TaTes konkrete Beweiskette benutzt bei (5.2) wesentlich die exakte Additivität von \(\omega\), und für \(p_n\) beziehungsweise \(g_n\) ist kein vergleichbares lineares Dilationsgesetz angegeben. Das angehängte Paper liefert deshalb keinen unmittelbaren unbedingten Beweis für die Irrationalität von \(S\).

Nicht gedeckt ist dagegen:

> **THE METHOD DOES NOT EXTEND, AND NO REPAIR EXISTS.**

O2 klassifiziert höchstens eine lineare formale Schicht, O3s universelle Bridge-Behauptung wird durch die exakten Identitäten mit \(\pi(m)\) und \(g_n\) widerlegt, Theorem 3.1 klassifiziert nicht die zulässigen Reihenzähler, und EXCH/E2 ist nur ein hinreichender Weg unter mehreren möglichen Tail-Separationsmechanismen.

Das Verdikt beweist daher keine strukturelle Unmöglichkeit; es dokumentiert lediglich das Scheitern einer bestimmten, überwiegend linearen Transferarchitektur.

## Quelle

Terence Tao und Joni Teräväinen, *Quantitative Correlations and Some Problems on Prime Factors of Consecutive Integers*, arXiv:2512.01739v2, insbesondere §1.3, Theorem 3.1 sowie §5.
