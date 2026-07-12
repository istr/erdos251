# Adversariales Review: `erdos251_stage1b_turn2.md`

## Prüfgrundlage und Integrität

Es wurden ausschließlich die beiden angehängten Dateien verwendet. Es erfolgte kein Webzugriff und es wurden keine fremden Quellen herangezogen.

- `sha256(review_1b.md)` = `f4a15ffa0d32acf7734000d120826fa6425cecb96ab3412a6b5250f86450f977`
- `sha256(erdos251_stage1b_turn2.md)` = `e5f818afe48e039327ecc4ac2f6003051c833cbda7fa1a6fa03874450c7a6560`

Die im Prüfdokument selbst genannte Prüfsumme `5f6abc...` ist ausdrücklich einer anders bezeichneten Datei `1b_briefed.md` zugeordnet und stimmt nicht mit der tatsächlich geprüften Anlage überein. Sie authentifiziert daher die vorliegende Anlage nicht.

## Phasenprotokoll

**Phase A wurde inhaltlich unabhängig erstellt und vollständig niedergeschrieben, bevor die Phase-B-Probes zur Auswertung herangezogen wurden.** Das Instruktionsdokument war technisch als Ganzes verfügbar; die Phase-A-Bewertungen wurden jedoch ohne Verwendung der Probe-Fragestellungen festgelegt.

# Phase A — unabhängige Verifikation

## Verdict ledger

| id | location | verdict | one-sentence justification | confidence |
|---|---|---|---|---:|
| A01 | Z. 5–9, Provenienz | cosmetic | Die interne SHA-256-Angabe betrifft eine anders benannte Datei und stimmt nicht mit der geprüften Anlage überein; die Vollständigkeitsbehauptung ist zudem nur eine Selbsteinschätzung. | 1.00 |
| A02 | Z. 7, Webstatus | correct | Das Dokument kennzeichnet Literaturbehauptungen als unverifiziert und behauptet keine tatsächlich ausgeführten Webabfragen. | 0.99 |
| A03 | Z. 17, Definitionen von \(p_n,g_n,\ell\) | correct | Die 1-basierte Primzahl- und Gap-Notation ist intern konsistent. | 1.00 |
| A04 | Z. 18 und 104, Konvergenz aus \(p_n\le 2^n\) | repairable | Aus \(p_n/2^n\le1\) folgt keine Konvergenz; die später skizzierte Schranke \(p_n=O(n\log n)\) würde die Lücke lokal schließen. | 1.00 |
| A05 | Z. 18, Lean-Ziel gleich \(2S\) | correct | Mit 0-basierter Primzahlfolge gilt \(\sum_{n\ge0}P_n/2^n=2\sum_{m\ge1}p_m/2^m=2S\). | 1.00 |
| A06 | Z. 19, Identität für \(u_n\) | correct | Multiplikation des abgeschnittenen Restes von \(S\) mit \(2^n\) ergibt genau \(u_n\). | 0.99 |
| A07 | Z. 19 und 104–106, Darstellung von \(\delta_n\) | correct | Nach gesicherter absoluter Konvergenz ist die nichtnegative Doppelsummen-Umsortierung korrekt und liefert \(\delta_n=\sum_{j\ge1}g_{n+j}2^{-j}\). | 0.98 |
| A08 | Z. 20, rationale Normalform | correct | Jede rationale Zahl lässt sich mit Nenner \(2^s b\), \(b\) ungerade, darstellen; Reduziertheit ist nicht erforderlich. | 1.00 |
| A09 | Z. 21, konsekutive Realisierung | correct | Die Definition trifft genau das Auftreten des Gap-Wortes ohne zusätzliche Primzahl im Spannintervall. | 0.99 |
| A10 | Z. 22, Admissibilität und Singularreihe | correct | Die Definitionen sind die üblichen endlichen Tupeldefinitionen und werden später konsistent eingesetzt. | 0.98 |
| A11 | Z. 104, Bertrand-Induktion \(p_n\le2^n\) | correct | Diese Schranke selbst folgt per Induktion aus Bertrand, ist aber zu schwach für den daraus gezogenen Konvergenzschluss. | 0.99 |
| A12 | Z. 105, Tausch der Summationsreihenfolge | repairable | Der Tausch ist wegen Nichtnegativität beziehungsweise absoluter Konvergenz zulässig, doch die benötigte Konvergenz wurde an dieser Stelle noch nicht korrekt begründet. | 0.98 |
| A13 | Z. 106, Rekurrenz \(\delta_{n+1}=2\delta_n-g_{n+1}\) | correct | Direktes Verschieben der Gap-Reihe ergibt die Rekurrenz ohne Zusatzannahme. | 1.00 |
| A14 | Z. 106, \(\delta_n\ge2\) für \(n\ge1\) | correct | Ab \(g_2\) sind alle Primzahldifferenzen gerade und mindestens 2, und die dyadischen Gewichte summieren sich zu 1. | 1.00 |
| A15 | Z. 108, Blockzerlegung CL1 | correct | Abtrennen der ersten \(T\) Terme und Reindizierung des Restes ergibt den Faktor \(2^{-T}\). | 1.00 |
| A16 | Z. 110, Integralgitterteil von CL2 | correct | Für \(n\ge s\) sind sowohl \(2^n bS\) als auch der skalierte endliche Präfix ganzzahlig. | 0.99 |
| A17 | Z. 110, Paritätsschwelle in CL2 | repairable | Für \(s=0,n=0\) ist \(g_1=1\) nicht gerade, sodass die Behauptung ab \(m=s+1=1\) falsch sein kann; man muss etwa \(s\ge1\) wählen oder die Schwelle auf \(m\ge\max(s+1,2)\) setzen. | 1.00 |
| A18 | Z. 112–115, CL3 | correct | Bei identischem Präfix löschen sich die endlichen Summen, und die gerade Gitterdifferenz wird mit \(2^J\) auf \(2^{J+1}\mathbb Z\) skaliert. | 0.99 |
| A19 | Z. 117, CL4 | correct | Ein Vielfaches von \(2^{J+1}\) mit strikt kleinerem Betrag muss null sein. | 1.00 |
| A20 | Z. 85–96, FM-Quantoren | correct | Die Sequenzquantoren, Blocklängen und asymptotischen Bedingungen sind hinreichend und enthalten keinen Nennerparameter \(b\). | 0.99 |
| A21 | Z. 87–91, FM-P/F/S/1 | correct | Die Präfix-, Zweifork-, Suffix- und Endtail-Bedingungen passen exakt zur späteren Blockzerlegung. | 0.99 |
| A22 | Z. 95–98, b-freie Margin | correct | Für jedes feste \(b\) folgt aus \((\gamma_r+4)/2^{J_r}\to0\) schließlich die benötigte Gittermargin. | 0.99 |
| A23 | Z. 98, Immunität gegen Exact Hits | correct | FM fordert keine Nichtintegralität oder Anti-Konzentration der Tails; exakte Gleichheit wird im Beweis sogar als Verriegelung genutzt. | 0.98 |
| A24 | Z. 121, gemeinsame Wahl von \(r\) | correct | Zwei eventuale Bedingungen können gleichzeitig erfüllt werden, da beide entlang derselben Folge gelten. | 1.00 |
| A25 | Z. 123, Endtail-Differenz | correct | Aus \(2\le\delta_{n+L},\delta_{m+L}\le H\) folgt \(|\Delta|\le H-2<H\le2^K\). | 1.00 |
| A26 | Z. 124–125, Forkzerlegung | correct | Die zwei Differenzen \(+\gamma,-\gamma\) tragen \(\gamma/2-\gamma/4=\gamma/4\) bei, der gemeinsame Suffix verschwindet. | 1.00 |
| A27 | Z. 126, Forknähe | correct | Die gedämpfte Endtail-Differenz ist strikt kleiner als \(1/4\), also ist der Gesamtbetrag kleiner als \((\gamma+1)/4\). | 1.00 |
| A28 | Z. 127, Gitter-Lock | correct | Die gewählte Margin macht das in \(2^{J+1}\mathbb Z\) liegende Produkt betragsmäßig zu klein und erzwingt Null. | 1.00 |
| A29 | Z. 128, Schlusswiderspruch | correct | Null am Fork impliziert \(|\delta_{n+L}-\delta_{m+L}|=\gamma2^K\), unvereinbar mit \(<2^K\) und \(\gamma\ge2\). | 1.00 |
| A30 | Z. 130 und 185, Übergang zu Irrationalität | correct | Nach Ausschluss jeder rationalen Normalform ist \(S\) irrational, und Multiplikation mit der von null verschiedenen rationalen Zahl 2 erhält Irrationalität. | 0.99 |
| A31 | Z. 134(i), Primorialschranke | repairable | Die angegebene Binomial-Induktionsidee ist plausibel, aber als „Beweis“ zu knapp, weil Induktionsintervalle und Basisfälle nicht vollständig ausgeschrieben sind. | 0.90 |
| A32 | Z. 134(ii), untere Chebyshev-Schranke | correct | Die Zentralbinomialkoeffizienten-Abschätzung ergibt für große Argumente eine Schranke der Form \(\pi(x)\ge x/(2\log x)\). | 0.94 |
| A33 | Z. 134(iii), obere Chebyshev-Schranke | correct | Aufteilung bei \(\sqrt x\) und die \(\theta\)-Schranke liefern die behauptete grobe obere Schranke für große \(x\). | 0.94 |
| A34 | Z. 134(iv), \(p_k\le C_Pk\log(k+2)\) | repairable | Die Bootstrap-Idee ist richtig, benötigt aber eine explizite Herleitung von \(p_k\le k^2\) für große \(k\) und die Behandlung kleiner Indizes. | 0.93 |
| A35 | Z. 134(v), Mertens-Paket | gap | Die exakten Mertens-Aussagen werden nur behauptet, und „partielle Summation aus Chebyshev“ allein beweist weder die Konstante noch den angegebenen Eulerprodukt-Bound; diese Lemmata sind im selbständigen Dokument nicht bewiesen. | 0.98 |
| A36 | Z. 140, CL8 für kleine Primzahlen | correct | Admissibilität liefert \(\nu_H(p)\le p-1\), daher ist jeder lokale Faktor mindestens \(1/p\). | 0.96 |
| A37 | Z. 140, CL8 für \(k+2<p\le2(k+1)\) | correct | Die grobe Untergrenze \(1/p\) und eine Chebyshev-Zählung ergeben insgesamt nur einen Faktor \(e^{-O(k)}\). | 0.95 |
| A38 | Z. 140, CL8 für \(2(k+1)<p\le D\) | correct | Da \((k+1)/p<1/2\), sind die Exponentialabschätzungen gültig, und bei \(D=O(k\log k)\) ist die reziproke Primzahlsumme über dieses kurze Verhältnis \(o(1)\). | 0.94 |
| A39 | Z. 140, CL8 für \(p>D\) | correct | Alle Offsets sind modulo \(p\) verschieden, und die logarithmische Faktorabweichung ist \(O(k^2/p^2)\), summiert also zu \(o(k)\). | 0.92 |
| A40 | Z. 140, Schluss \(\mathfrak S(H)\ge e^{-Ck}\) | repairable | Der Schluss folgt aus den Teilbereichen, sobald die in A35 fehlenden Primzahlprodukt-/Reziproksummen-Lemmata sauber bereitgestellt sind. | 0.94 |
| A41 | Z. 142–143, Singularreihenquotient CL9 | correct | Der Quotient der lokalen Faktoren ist korrekt, und bei Nichtkollision ist er wegen \(\nu_H\ge1\) strikt kleiner als 1. | 0.98 |
| A42 | Z. 143–144, Kollisionsprimzahlen | correct | Jede große Kollisionsprimzahl teilt \(\Delta_t\), und deren Anzahl wird durch \(\log\Delta_t/\log(2k+2)\) kontrolliert. | 0.97 |
| A43 | Z. 144–145, Summe der Quotienten | repairable | \(R_t=O(\log k)\) und höchstens \(O(k\log k)\) Werte von \(t\) geben die Behauptung, wiederum unter Verwendung des unbewiesenen Mertens-Produktbounds. | 0.96 |
| A44 | Z. 147, Charakterisierung konsekutiver Wörter | correct | Für ungerades Basisp \(p>D\) sind zusätzliche Primzahlen nur an geraden Offsets möglich; deren vollständiges Fehlen ist äquivalent zur Konsekutivität. | 0.99 |
| A45 | Z. 148, erste Bonferroni-Stufe | correct | Das Abziehen der Vereinigung durch die Summe der Einzelereignisse ist eine gültige untere Union-Bound-Abschätzung. | 1.00 |
| A46 | Z. 149, inadmissible Erweiterungen haben Anzahl 0 | correct | Eine überdeckende Primzahl \(q\le L+2\) teilt stets einen Wert \(p+h>q\), sodass nicht alle Werte prim sein können. | 0.99 |
| A47 | Z. 149, Anwendung von HL-A auf Erweiterungen | correct | Die Erweiterung hat \(L+2\) Punkte, gerade Offsets und denselben Span und liegt für große \(x\) innerhalb der angegebenen Budgets. | 0.98 |
| A48 | Z. 150, relative Entfernung durch Zusatzprimes | correct | Das Verhältnis ist \(O(L(\log L)^2/\ell)=o(1)\), da \(L\asymp\log\ell\). | 0.99 |
| A49 | Z. 151, Entfernung des Bereichs bis \(\sqrt x\) | correct | Der Hauptterm ist \(x\exp[-O((\log\ell)^2)]=x^{1-o(1)}\), also wesentlich größer als \(\sqrt x\). | 0.99 |
| A50 | Z. 152, positiver konsekutiver Count | correct | Nach Wahl eines ausreichend großen Schwellwerts bleiben mindestens ein Viertel des Hauptterms und damit mindestens eine Realisierung. | 0.98 |
| A51 | Z. 157–160, Parameter \(H,K,J,L\) | correct | \(2^K\ge H\), \(K=(2/\log2)\log\log x+O(1)\), und \(2^J\ge(K+20)^4\) sind korrekt. | 1.00 |
| A52 | Z. 162–164, Löschkonstruktion und Interior-Bedingung | correct | Mit \(i_0=J+2\) und \(L=J+2+K\) liegen beide gelöschten Punkte für \(K\ge1\) strikt im Inneren. | 0.99 |
| A53 | Z. 166, Wortstruktur | correct | Direktes Ausrechnen der Lücken nach den beiden benachbarten Löschungen liefert Präfixgleichheit, \(+\gamma,-\gamma\) und einen gemeinsamen Suffix der Länge \(K\). | 1.00 |
| A54 | Z. 167, Admissibilität | correct | Vor Translation fehlt für \(p\le L+2\) die Klasse 0, nach Translation eine verschobene Klasse; für größere \(p\) reichen \(L+1<p\) Punkte nicht zur Vollbelegung. | 0.99 |
| A55 | Z. 168, Spanbound | correct | Der Index von \(q_{L+2}\) ist höchstens \(2L+4\), und die zuvor behauptete Primzahlschranke liefert \(D=O(L\log L)\). | 0.96 |
| A56 | Z. 169 und U1/U2, Budgetzählung | cosmetic | Die tatsächlichen Kardinalitäten sind \(L+1\) beziehungsweise \(L+2\); die Formulierung „\(L+2+1\)“ ist off-by-one, und asymptotisch würde bereits der Faktor 3 statt 4 genügen. | 0.99 |
| A57 | Z. 173–174, Tailbound CL11 | correct | Iteriertes Bertrand, \(\log p_{\nu+j}\le\log p_\nu+j\), \(\sum j^22^{-j}=6\) und \((\log p_\nu)^2\ge12\) liefern den Faktor 3. | 0.99 |
| A58 | Z. 176, getrennte Wahl der beiden Wortvorkommen | correct | CL10 liefert für jedes der zwei festen Wörter mindestens eine Realisierung am selben Skalenparameter; Gleichheit der Sites ist wegen verschiedener Wörter ausgeschlossen. | 0.98 |
| A59 | Z. 178, Tailindex und \(p_{n+L}\le2x\) | correct | Der Wortspan endet bei \(p_{n+L+1}\), also liegt insbesondere \(p_{n+L}\le p_{n+1}+D\le2x\) für große \(x\). | 0.99 |
| A60 | Z. 179, FM-2-Konstanten | correct | Aus \(\gamma\le C_1L\log L\), \(2^J\ge(K+20)^4\), \(L\le2(K+20)\) und \(\log L\le K+20\) folgt eine \(O(K^{-2})\)-Schranke. | 0.98 |
| A61 | Z. 180–181, Entkommen der Sites | correct | Aus \(p_{n+1}>\sqrt x\) folgt \(n\ge\pi(\sqrt x)\), sodass jede Folge \(x_r\to\infty\) die FM-3-Bedingung erfüllt. | 0.99 |
| A62 | Z. 55–64, Quantoren von HL-A | correct | Die Hypothese ist klar und stark genug formuliert; wegen \(C_A\ell^{-A_0}\to0\) stehen eventuale Faktoren zwischen \(1/2\) und 2 zur Verfügung. | 0.98 |
| A63 | Z. 66–67, HL-B | correct | Die globale punktweise Gap-Schranke ist eindeutig formuliert und genau die in CL11 verwendete Annahme. | 1.00 |
| A64 | Z. 69 und 321–323, Zirkularität und Einordnung | repairable | Keine Klausel erwähnt \(S\) oder seine Irrationalität, also keine Zirkularität; das Paket ist wegen HL-B aber materiell stärker als eine reine Hardy–Littlewood-Tupelhypothese und sollte nicht ohne Zusatzqualifikation „HL“ genannt werden. | 0.99 |
| A65 | Z. 43, 69 und 302, „CL13 beweist Unabhängigkeit“ | gap | Die Analyse eines bestimmten Inclusion–Exclusion-Wegs beweist keine logische Nichtableitbarkeit von B aus A; höchstens wird gezeigt, dass dieser naive Weg mit polylogarithmischem Fehler nicht reicht. | 0.99 |
| A66 | Z. 212–217, Lean-Indexierung von `P`, `G`, `delta` | correct | `G n` entspricht mathematisch \(g_{n+1}\), und `delta n` entspricht der im Text verwendeten \(\delta_n\). | 0.98 |
| A67 | Z. 220–222, Lean-`delta_block` | correct | Die 0-basierte Summe über `range T` bildet genau die ersten \(T\) Gap-Terme ab. | 0.97 |
| A68 | Z. 224–240, Lean-Gitterlemma für das Ziel \(2S\) | repairable | Die Prosa beweist das Gitter für \(S\), während `hS` die Rationalität von \(2S\) parametrisiert; dadurch verschiebt sich die sichere Integralschwelle mindestens um eins, zusätzlich zur Paritätsrandfrage aus A17. | 1.00 |
| A69 | Z. 243–253, Lean-`FMConfig` | repairable | Die mathematische Struktur ist korrekt, aber Coercions wie `-γ` auf einer erwarteten Ganzzahl und weitere Details sind nicht als kompilierend belegt. | 0.90 |
| A70 | Z. 274–290, `HLQuantA`-Stub | gap | `Admissible` ist undefiniert, die Proposition endet in `True`, und der gezeigte Code formalisiert die analytische Hypothese nicht; `hl_quant_implies_fm` folgt aus diesem Stub nicht mathematisch. | 1.00 |
| A71 | Z. 298, „Mathlib-ready/routine bookkeeping“ | gap | Ohne Definition der Singularreihe, Zählfunktionen, Konvergenz- und Uniformitätslemmata ist der analytische Teil kein bloßes syntaktisches Ausfüllen und der Code nicht lauffähig. | 0.99 |
| A72 | Z. 302–317, False starts und Sekundärhinweise | cosmetic | Diese Aussagen sind nicht lasttragend und teils ausdrücklich nur Skizzen oder unverifiziert; sie sollten nicht als bewiesene Nebenresultate gelesen werden. | 0.95 |
| A73 | Z. 321, „Nothing is missing inside the conditional chain“ | gap | Konvergenzbegründung, Mertens-Lemmata, Paritätsrandfall und formale Schnittstelle sind tatsächlich nicht vollständig geschlossen. | 1.00 |

## Phase-A-Gesamturteil

**gaps found:**

1. Ungültiger Konvergenzschluss aus \(p_n\le2^n\); reparierbar durch die später skizzierte polynomiale Primzahlschranke.
2. Randfehler in der Paritätsaussage für \(s=0\); reparierbar durch Wahl \(s\ge1\) oder spätere Schwelle.
3. Das benötigte Mertens-/Eulerprodukt-Paket ist nicht aus dem Dokument heraus bewiesen; als klassische Lemmaeinfügung reparierbar.
4. CL13 belegt keine logische Unabhängigkeit von HL-B gegenüber HL-A.
5. Die Lean-Version parametrisiert die Rationalität von \(2S\), verwendet aber Schwellen aus dem Beweis für \(S\); zudem ist `HLQuantA` nur ein nicht tragfähiger Stub.
6. Mehrere Vollständigkeits- und „Mathlib-ready“-Aussagen sind dadurch zu stark.

Die zentrale mathematische Kette

\[
\text{HL-A + HL-B}\Longrightarrow\text{konkrete FM-Konfigurationen}\Longrightarrow S\text{ irrational}
\]

ist nach Korrektur dieser Punkte schlüssig. Insbesondere wurde kein fataler Fehler in der Fork–Merge-Widerspruchsrechnung oder in der Lösch-/Bonferroni-Konstruktion gefunden.

**Overall Phase-A verdict:** `gaps found (A04/A12, A17, A35/A40/A43, A65, A68–A71, A73)`  
**Overall confidence:** `0.95`

# Phase B — gezielte Probes P1–P7

## P1. Model-entropy clause

**Im geprüften Dokument gibt es keine „model-entropy clause“ und keine gemittelte Fork-Anti-Konzentrationsannahme mit fester Konstante.** Daher kann diese Klausel weder als rein lokales Modellstatement noch als plausibel beweisbare Eigenschaft des Singularreihenmodells verifiziert werden.

**Argument in positiver Richtung:** Der tatsächlich vorhandene Zählteil ist lokal: HL-A weist jedem expliziten endlichen Offset-Tupel \(H\) den Singularreihen-Hauptterm \(\mathfrak S(H)x/\ell^{|H|}\) zu. Die Konstruktion benötigt nur zwei explizit gebaute Wörter und die Einpunkt-Erweiterungen, also keine globale Statistik über \(\delta\)-Tails.

**Argument in negativer Richtung:** HL-B ist keine Aussage über das lokale Singularreihenmodell, sondern eine globale punktweise Schranke für alle hinreichend späten Primzahllücken. Außerdem wird weder ein Entropiefunktional definiert noch eine gemittelte Anti-Konzentrationskonstante hergeleitet. Aus dem Dokument folgt daher keine Antwort auf die Frage, ob eine solche Modellklausel für das Standardmodell beweisbar wäre.

**Conclusion:** `not present / not applicable`. Die Beweiskette braucht diese Klausel nicht; ihre Rolle wird vollständig durch die punktweise HL-B-Tailkontrolle ersetzt.

## P2. Gesamtzahl der Muster \(T_x\)

Ein Objekt \(T_x\) wird nicht definiert oder verwendet. Die behauptete Beziehung

\[
T_x=(1-o(1))|I_x|
\]

ist daher im Dokument weder beweisbar noch nötig. Der Beweis zählt nicht alle an Startindizes auftretenden Wörter und führt keinen Spanfilter über eine Musterpopulation aus. Stattdessen werden pro Skala genau zwei deterministisch konstruierte Wörter \(w,w'\) gewählt und für jedes Wort separat mittels CL10 mindestens eine konsekutive Realisierung nachgewiesen.

**Conclusion:** Der Schritt ist für den vorliegenden Beweis unnötig.

## P3. Vier-Tails-Buchhaltung

Es gibt keine „good site“-Definition und keine vier Tailgrößen. Der eigentliche Beweis benötigt nur

\[
\delta_{n+L}\quad\text{und}\quad\delta_{m+L}.
\]

CL11 kontrolliert jede dieser Größen punktweise, weil HL-B für jeden hinreichend großen Index gilt. Die Tailwerte am Fork \(n+J,m+J\) werden nicht separat vorausgesetzt oder abgeschätzt, sondern aus Middle Block, gemeinsamem Suffix und den zwei Endtails exakt ausgerechnet.

Damit liefern zwei Sites genau die zwei benötigten Bounds. Eine Behauptung, dass pro Site zwei Tailoffsets und insgesamt vier Bounds nötig seien, trifft auf diese Fassung nicht zu.

**Conclusion:** Die tatsächlich verwendete Zwei-Tails-Buchhaltung ist korrekt; die Vier-Tails-Prämisse ist hier nicht anwendbar.

## P4. Klausel \(M_x(d)=0\) und inadmissible Wörter

Eine Zählaxiomnotation \(M_x(d)\) oder \(N_x(d)\) kommt nicht vor. Die analoge Aussage in CL10 ist jedoch tatsächlich **unbedingt**:

Ist \(H(w)\cup\{t\}\) inadmissibel und hat \(L+2\) Punkte, so gibt es eine Primzahl \(q\le L+2\), deren Restklassen vollständig getroffen werden. Für jedes Basisp \(p>\sqrt x>q\) existiert dann ein Offset \(h\) mit \(q\mid p+h\). Da \(p+h>q\), ist dieser Wert zusammengesetzt; folglich kann kein Basisp alle Tupelwerte prim machen. Der Count ist exakt 0.

Diese Nullfeststellung ist in CL10 nützlich, weil HL-A nur auf admissible Erweiterungen angewandt werden darf. Sie muss aber nicht als zusätzliche Axiomklausel formuliert werden.

**Conclusion:** `N=0` für die dort betrachteten inadmissiblen Erweiterungen ist unconditional und korrekt; eine separate Zählaxiomklausel ist nicht erforderlich.

## P5. Konstantentabelle neu berechnet

Setze \(\ell=\log x\). Aus

\[
H(x)=3C_g(\log 2x)^2,
\qquad
K=\lceil\log_2H(x)\rceil
\]

folgt

\[
K=\frac{2}{\log2}\log\ell+O(1)
  \approx2.88539\,\log\ell.
\]

Weiter ist

\[
J=\lceil4\log_2(K+20)\rceil=O(\log\log\ell),
\qquad
L=K+J+2.
\]

### Fensterlänge versus Blocklänge

- Basis-Tupel: \(|H(w)|=L+1\).
- Einpunkt-Erweiterung: \(|H(w)\cup\{t\}|=L+2\).
- Asymptotisch:
  \[
  \frac{L+2}{\log\ell}\to\frac2{\log2}\approx2.88539<3.
  \]

Daher liegen Basis und Erweiterung für hinreichend großes \(x\) sogar unter \(3\log\log x\); das HL-A-Budget \(4\log\log x\) ist großzügig. Die Formulierung in Z. 169 mit „\(L+2+1\)“ ist ein off-by-one-Schreibfehler, nicht eine verbrauchte zusätzliche Stelle.

### Relativfehler versus Entfernungen

Mit \(M_H=\mathfrak S(H)x/\ell^{L+1}\) gilt:

- HL-Relativfehler:
  \[
  \varepsilon_H\le C_A\ell^{-A_0}=o(1)
  \quad(A_0\ge1).
  \]
- Bonferroni-Entfernung relativ zum Hauptterm:
  \[
  O\!\left(\frac{L(\log L)^2}{\ell}\right)
  =O\!\left(\frac{\log\ell\,(\log\log\ell)^2}{\ell}\right)
  =o(1).
  \]
- Entfernung \(p\le\sqrt x\): Aus
  \[
  M_H\ge x\exp[-O((\log\ell)^2)]=x^{1-o(1)}
  \]
  folgt
  \[
  \frac{\sqrt x}{M_H}
  \le \exp[-\ell/2+O((\log\ell)^2)]
  =o(1).
  \]

Keiner der Entfernungsterme muss vom HL-Fehler dominiert werden; es genügt, dass alle drei relativ zum Hauptterm gegen 0 gehen.

### FM-2-Ungleichung

Da \(2^J\ge(K+20)^4\), \(\gamma\le C_1L\log L\), \(L\le2(K+20)\) und \(\log L\le K+20\), gilt schließlich

\[
\frac{\gamma+4}{2^J}
\le
\frac{C_1L\log L+4}{(K+20)^4}
\le
\frac{3C_1}{(K+20)^2}
\longrightarrow0.
\]

Die letzte `3` ist für große \(K\) gültig, sobald \(4\le C_1(K+20)^2\).

### Prüfpunktspezifisch: \(H/2^J\)

Die Aussage \(H/2^J\to0\) wäre **falsch**:

\[
H\asymp\ell^2,
\qquad
2^J\asymp K^4\asymp(\log\ell)^4,
\qquad
\frac{H}{2^J}\to\infty.
\]

Der Beweis benötigt diese Aussage nicht. Er benötigt stattdessen die zwei getrennten Relationen

\[
H\le2^K
\quad\Longrightarrow\quad
2^{-(K+2)}H\le\frac14,
\]

und

\[
\frac{\gamma+4}{2^J}\to0.
\]

**Conclusion:** Die tatsächlich benötigte Konstantenrechnung stimmt; eine behauptete Grenze \(H/2^J\to0\) wäre ein Fehler, kommt aber in der Beweisführung nicht vor.

## P6. Epsilon-Buchhaltung

HL-A liefert

\[
\pi_H(x)=M_H(1+E_H),\qquad |E_H|\le\varepsilon(x),
\quad \varepsilon(x)=C_A\ell^{-A_0}\to0.
\]

Für hinreichend großes \(x\) kann \(\varepsilon\le1/2\) gewählt werden; dann

\[
\frac12M_H\le\pi_H(x)\le\frac32M_H\le2M_H.
\]

CL10 verwendet nur diese einseitigen Faktoren. Es gibt keinen Schritt, der unkontrolliert durch \(1-E_H\) dividiert oder einen Quotienten \((1+\varepsilon)/(1-\varepsilon)\) benötigt. Für die Schlusskonstante \(1/4\) kann man die beiden Entfernungsterme jeweils auf höchstens \(M_H/8\) beschränken:

\[
N_{\rm cons}\ge\frac12M_H-\frac18M_H-\frac18M_H=\frac14M_H.
\]

Weitere numerische Checks:

- Aus \((\gamma+4)/2^J<8/b\) folgt exakt
  \[
  b(\gamma+4)/4<2^{J+1}.
  \]
- Aus \(|\Delta_{\rm end}|<2^K\) folgt
  \[
  2^{-(K+2)}|\Delta_{\rm end}|<1/4.
  \]
- Damit ist
  \[
  |\Delta_{\rm fork}|<(\gamma+1)/4<(\gamma+4)/4.
  \]

**Conclusion:** Die Epsilon- und Faktor-Buchhaltung ist korrekt; die Schwellenwerte sollten im Text nur expliziter zusammengefasst werden.

## P7. Robustheit gegenüber Exact Hits

Der Beweis benötigt keine Bedingung der Form „der Tail unterscheidet sich von einer ganzen Zahl“. Unter der Rationalitätsannahme wird gerade ausgenutzt, dass die Fork-Differenz nach Skalierung auf einem diskreten Gitter liegt. Sobald ihr Betrag kleiner als die Gitterweite ist, folgt die exakte Gleichheit

\[
\delta_{n+J}=
\delta_{m+J}.
\]

Diese exakte Gleichheit wird anschließend mit der nichtverschwindenden strukturellen Forkmasse \(\gamma/4\) kombiniert und erzwingt die große Endtail-Differenz \(\gamma2^K\). Selbst wenn einer oder beide Endtails exakt ganzzahlig, exakt gleich oder anderweitig „locked“ wären, bliebe der Widerspruch bestehen. Die einzige Striktheit stammt aus der Größenabschätzung \(|\delta_{n+L}-\delta_{m+L}|<2^K\), nicht aus einer Anti-Hit-Annahme.

**Conclusion:** Die behauptete Immunität gegen Exact Hits ist im tatsächlich geschriebenen Fork–Merge-Beweis real.

# Final verdict

**`SOUND with repairable issues`**

Reparaturliste:

1. Konvergenz mit \(p_n=O(n\log n)\) statt mit \(p_n\le2^n\) begründen.
2. Paritätsschwelle für den Fall \(s=0\) korrigieren oder die rationale Darstellung mit \(s\ge1\) wählen.
3. Das verwendete Mertens-/Eulerprodukt-Paket als klare Lemmas mit Beweis einfügen.
4. CL13 von „logischer Unabhängigkeit“ auf „der dargestellte Inclusion–Exclusion-Weg reicht nicht“ abschwächen.
5. Die Off-by-one-Budgetformulierung bereinigen.
6. Die Lean-Schwellen an die Rationalität des Ziels \(2S\) anpassen und `HLQuantA` wirklich definieren; der vorhandene Stub darf nicht als formaler Beweis gelten.
7. Aussagen wie „every implication proved“, „nothing missing“ und „Mathlib-ready“ entsprechend einschränken.

Keiner dieser Punkte erfordert eine Änderung des Fork–Merge-Mechanismus, der expliziten Löschkonstruktion oder der beiden Hypothesen HL-A/HL-B. Die Hypothese ist **nicht zirkulär**, aber wegen der globalen Cramér–Granville-Klausel HL-B materiell stärker als eine reine Hardy–Littlewood-Tupelhypothese.

**Overall confidence:** `0.94`

# What I could not check

- Gemäß Benutzerverbot wurden Literaturstatus, benannte Threads, ScPu11, aktuelle Lean-/Mathlib-Namen und sonstige externe Aussagen nicht im Web verifiziert.
- Im lokalen Ausführungsumfeld war kein Lean-/Lake-Compiler verfügbar; der Code wurde daher statisch geprüft, nicht kompiliert.
- Die im Dokument genannten Dateien `1b_briefed.md` und `transcript-turn-1.md` lagen nicht als separate Anlagen vor; ihre Prüfsummen und Provenienz konnten nicht verifiziert werden.
- Die behaupteten klassischen Mertens-Lemmata wurden im Dokument nicht vollständig bewiesen. Ich konnte ihre konkrete Verwendung und die benötigte Form prüfen, aber unter dem Verbot fremder Quellen keinen externen Beleg nachziehen.
