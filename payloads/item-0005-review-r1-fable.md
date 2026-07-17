# Adversarialer Prüfbericht

**Gegenstand:** Verdikt „The method does not extend" — Nicht-Übertragbarkeit des unbedingten Tao–Teräväinen-Beweises (arXiv:2512.01739v2, Theorem 1.3, Erdős #69) auf $S = \sum_n p_n/2^n$

**Datum:** 17. Juli 2026
**Rolle:** Adversarialer Prüfer (Falsifikationsversuch Nr. 7)

---

## Prüfergebnis vorab

Die Widerlegung ist mir nicht gelungen. Ich habe sieben unabhängige Angriffslinien gegen das Verdikt gefahren; alle scheitern an identifizierbaren strukturellen Gründen, die exakt den Schichten O1–O4 entsprechen. Darüber hinaus habe ich die beiden tragenden mathematischen Bausteine des Verdikts — das EXCH-Lemma (O4) und den Rigiditätskern (O2) — unabhängig nachgerechnet; beide halten, und O2 lässt sich sogar *verschärfen*. Im Einzelnen:

## 1. Nachbau der Gitterschicht (Prüfung der O1-Prämisse)

Sei $S = a/(2^s b)$ mit $b$ ungerade. Für $n \ge s$ ist $b\,2^nS \in \mathbb{Z}$, also mit $T_n := \sum_{h\ge1} p_{n+h}2^{-h}$ auch $bT_n \in \mathbb{Z}$. Mit $g_i := p_{i+1}-p_i$ und $\delta_n := T_n - p_{n+1} = \sum_{i\ge1} g_{n+i}2^{-i}$ folgt $b\delta_n \in \mathbb{Z}$ für $n \ge s$, dazu unbedingt die Rekursion $2\delta_{n-1} = g_n + \delta_n$ sowie $\delta_n \ge 2$. Das ist verbatim die behauptete (5.1)-Entsprechung. Der Schritt (5.1)→(5.2) benötigt bei Tao–Teräväinen die exakte Identität $\omega(pn)=\omega(n)+1-\mathbb{1}_{p\mid n}$, die eine Dilation der Ziffernposition ($h\mapsto ph$) in eine Division des Arguments ($n\mapsto n/p$) verwandelt. Für $p_n$ existiert keine exakte Funktionalgleichung unter irgendeiner Indexabbildung: $p_{2n}-2p_n \sim 2n\log 2 \to \infty$ mit Fluktuationen weit oberhalb jeder mod-1-Toleranz; Bertrand u. ä. sind Ungleichungen; $p_{\pi(m)}$-Konstruktionen sind nur bis auf die (unbekannte) Lückenstruktur bestimmt. O1 hält.

## 2. Angriffslinien und ihr Scheitern

1. **Translationswürfel statt Dilationswürfel.** Die einzige verfügbare Zweiparameterfamilie ist die Translation. Der alternierende Würfel über $n+\sum_k \epsilon_k l_k$ liefert $\sum_{h\ge1} 2^{-h}\,(\Delta_{l_1}\cdots\Delta_{l_K}g)(n+h)$ — einen $K$-fachen Differenzenoperator auf der Lückenfolge, ohne jede automatische Auslöschung der ersten $K$ Terme, weil der Ziffernkoeffizient jedes $\epsilon_k$ identisch 1 ist (statt TaTes $h$-abhängigem Faktor $(h-k)$ in (5.7)). Erzwingt man die Auslöschung von Hand, ist das eine Wortkoinzidenz — Beschaffung vom Typ (E1) —, und ein Widerspruch verlangt anschließend eine Nichtkoinzidenz — Typ (E2). Alle Würfelrouten münden also nachweislich in EXCH-förmige Anforderungen; das *reproduziert* die Lokalisierung des Verdikts, statt sie zu widerlegen.

2. **Billige Tail-Argumente im Stil von Remark 1.4.** Dort wird der Rest nach Multiplikation klein; hier wächst er: $bT_n \ge b\,p_{n+1}/2 \to \infty$. Der klassische „Rest in $(0,1)$"-Trick ist unanwendbar.

3. **Zähl↔Wert-Brücken.** Zwei kleine Identitäten machen O3s Dichotomie scharf: Summenvertauschung gibt $S = \sum_{j\ge0} 2^{-\pi(j)}$ (Zählfunktion im *Exponenten*), während $\sum_m \pi(m)2^{-m} = 2\sum_p 2^{-p} = 2T$ (Zählfunktion im *Zähler*) trivial irrational ist — die Ziffern von $T$ sind der aperiodische Primindikator (unendlich viele Einsen, Dichte 0). Die Reindizierung $m=p_n$ multipliziert Tails mit $2^{m-\pi(m)}$, unbeschränkt: kein gemeinsamer Nenner. Eine Mahler-Methode bräuchte eine Funktionalgleichung von $\sum_n p_n z^n$ — nicht vorhanden.

4. **Direkte Fütterung des analytischen Motors.** Theorem 3.1 verlangt 1-beschränkte *multiplikative* Funktionen, zwei Shifts, und wird in §5 nur bei (5.42)–(5.45) konsumiert (verifiziert). Lückenfunktionale sind Primindikator-Korrelationen, nicht multiplikativ, und bräuchten für (E2) Kontrolle über $\sim\log\log x$ Punkte; das Paper selbst erklärt schon Dreipunkt-Korrelationen für außerhalb der aktuellen Technologie (Remark 4.2, dritter Punkt — Zitat korrekt).

5. **(E2) via Siebmethoden.** Maynard–Tao/Zhang liefern „mindestens $m$ der Positionen prim", nie exakte Muster (Paritätsproblem), und schon gar nicht *zwei* Fenster mit identischen Flanken und differierender Mitte — zumal bei wachsenden Tiefen $J,K \asymp \log\log x$ plus (E4)-Typikalität.

6. **(E2) via Kombinatorik/symbolischer Dynamik.** Ich habe versucht, „Sandwich-Rigidität" (Mitte als Funktion der Flanken an typischen Stellen) über Morse–Hedlund-artige Komplexitätsargumente zu widerlegen: scheitert dreifach — (i) das Lückenalphabet ist unbeschränkt (Westzynthius/FGKMT), (ii) die Typikalitätsrestriktion (Ausnahmedichte $\sim 1/A$) zerstört jede Propagation der Determinismus-Relation, (iii) die Fenster wachsen mit $x$. Zählen ist bestätigt blind: Es gibt nur $\exp(O((\log_2 x)^2))$ typische Wörter der Länge $J{+}K{+}1$ gegenüber $\sim x/\log x$ Stellen — massive Wiederholung ist erzwungen und mit Rigidität *verträglich*. Lückenmomente sind rigiditätsinvariant.

7. **Shiu-Strings mit $q=2^t$.** Erzwingen Lücken $\equiv 0 \pmod{2^t}$, aber die Quantisierung $b\delta_n \in 2\mathbb{Z}$ propagiert widerspruchsfrei durch jede solche Konfiguration. Quantitativ zirkulär wie behauptet: Stringlängen $\gtrsim \log\log x$ haben doppelt-exponentiell kleine Dichte, unvereinbar mit den Markov-Typikalitätsanforderungen von (E4).

Literaturabgleich: Nach meinem Kenntnisstand ist die Irrationalität von $S$ offen; die im Paper angebotene Verallgemeinerung („sets $A$ sufficiently similar to the primes") betrifft $\sum_{n\in A}1/(2^n-1)$ — Wert-Position — und deckt $S$ nicht.

## 3. Unabhängige Verifikationen (positive Befunde)

**EXCH ist korrekt**, einschließlich des einzigen heiklen Details, der $2^{J+1}$-Teilbarkeit: Für $n\ge s{+}1$ ist $b\delta_n = 2b\delta_{n-1}-bg_n$ *gerade* ($b$ ungerade, Lücken gerade). (E1) gibt $b(\delta_n-\delta_m) = 2^{-J}\,b(\delta_{n+J}-\delta_{m+J}) \in 2\mathbb{Z}$, also $2^{J+1}\mid b(\delta_{n+J}-\delta_{m+J})$; mit $\delta \in [2,D]$ und (E5) folgt $\delta_{n+J}=\delta_{m+J}$. Reihensubtraktion mit (E2),(E3) liefert $0 = d_1/2 + 2^{-(K+1)}\Delta_{\mathrm{end}}$, $|\Delta_{\mathrm{end}}|\le 2^K-2$, also $|d_1|<1$ — Widerspruch zu $|d_1|\ge2$. Auch der Parameterhaushalt ist konsistent ($2^{J+1} > bD$ mit $D=O_A(\log x)$ und $2^K \gtrsim \log x$ erzwingen $J,K\gtrsim \log_2\log x$; Wortkapazitäten liegen weit darüber).

**Verschärfung von O2 (Ein-Generator-Beobachtung).** Wegen $\delta_n = 2\delta_{n-1}-g_n$ propagiert $b\delta_s\in\mathbb{Z}$ *vorwärts automatisch*: Die gesamte Kongruenzfamilie $\{b\delta_n\in\mathbb{Z}\}_{n\ge s}$ ist deduktiv äquivalent zur einen Kongruenz $b\delta_s\in\mathbb{Z}$. Rationalität liefert auf der formalen Ebene also exakt *ein* Gitter-Bit; alles Weitere ist Translation. Daraus folgt der C3/C6-Kern direkt: Über allen Integer-Gap-Modellen zertifizierte Funktionale liegen in $\mathbb{Z}\delta_s$ plus endlichen ganzzahligen Lückenkombinationen; Funktionale mit unendlich vielen Nullkoeffizienten kollabieren (Koeffizient von $g_m$ ist $2^{-m}P_m$ mit $P_m=\sum_{j<m}c_j2^j$; unendlich viele Nullen erzwingen Blockstruktur, d. h. triviale Teleskopidentitäten wie $2\delta_j-\delta_{j+1}=g_{j+1}$). Die Tail-Periodizität ist verifiziert: $b\delta_n \equiv 2^{n-s}\,b\delta_s \pmod b$. TaTes Gewinn stammt demgegenüber vollständig aus (5.2) — echter neuer arithmetischer Input via der Funktionalgleichung von $\omega$, der im abstrakten Gap-Modell nicht existiert.

**Bemerkenswerte Kontraposition:** EXCH besagt umgekehrt, dass Rationalität selbst die Sandwich-Rigidität der Lücken an typischen matched-flank-Paaren *erzwingt*. Der Engpass (E2) ist also nicht das Ergebnis mangelnder Suche, sondern innerhalb der Gitterschicht strukturell erzwungen: Der einzige Widerspruchshebel ist eine rohe Lückendifferenz bei identischem Kontext, und genau diese liefert kein unbedingtes Werkzeug.

Zitatprüfung im Paper: (1.1), (5.1)–(5.3), die $(h{-}k)$-Struktur von (5.7), Lemma 5.2 via Gowers-Monotonie [53, (11.7)], die Verpackung (5.18)/(5.20) vs. (5.21) als Theorem 5.1, die alleinige Thm-3.1-Verwendung bei (5.42)–(5.45), die Mertens-Massen-Untergrenze $\asymp (\log_3 x)^2$ via $2^K$ — alles korrekt wiedergegeben.

## 4. Nicht prüfbare Restpunkte

Vier Punkte konnte ich mangels Zugriff auf die acht Projekttexte nicht im Wortlaut auditieren: die exakte Formulierung der C3/C6-Rigidität (meine Herleitung deckt die natürliche Lesart und ersetzt sie funktional), die genaue „$O(\sqrt{\log x})$"-Kapazitätsrechnung (untergeordnet — die schwächere, elementare Schranke $\log x/\log\log x$ genügt), die exakte Fundstelle des Maynard-Vorbehalts (die mathematische Aussage, Paritätsblockade exakter Muster, ist unstrittig) und die Formalisierung des Produktformel-Brückenlemmas (das Zielobjekt $T$ ist trivial irrational; meine eigene Prüfung fand keinen Weg um die Unbeschränktheit von $2^{m-\pi(m)}$ herum). Keiner dieser Punkte ist tragend für mein Ergebnis, da ich die lasttragenden Teile unabhängig hergeleitet habe.

## Schlussurteil

Das Verdikt hält der adversarialen Prüfung stand. Dieser siebte Falsifikationsversuch scheitert wie die sechs vorherigen — und schließt, wie vier davon, mit einer Rigiditätsaussage, hier sogar in verschärfter Form: Die gesamte unbedingte Ausbeute der Rationalitätsannahme ist ein einziges, translationspropagiertes Gitter-Bit, dilationsfrei und amplifikationsinert. Der exakte unbedingte Rest ist Klausel (E2), eine Zwei-Stellen-Wortkorrelations-Untergrenze, für die weder das vorgelegte Paper noch mir bekannte unbedingte Technik ein Werkzeug bereitstellt.
