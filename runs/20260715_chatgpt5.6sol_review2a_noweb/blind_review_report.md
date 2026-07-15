# Blindes adversariales Gutachten

Prüfobjekt: das mathematische Dokument zur konditionalen Irrationalität von S. fileciteturn0file0  Verfahrens- und Outputvertrag: Payload R2. fileciteturn0file1

[Vollständigen Report als Markdown herunterladen](sandbox:/mnt/data/blind_review_report.md)

Webzugriff wurde nicht benutzt. Alle Literatur-, Prioritäts-, Bibliotheks- und empirischen Abgleiche, die nicht allein aus den zwei Dateien oder endlicher lokaler Rechnung folgen, sind als **UNVERIFIED** markiert.

## 1. Phase A — unabhängige Zeilenprüfung

| id | location | verdict | one-sentence justification | confidence |
|---|---|---|---|---:|
| A01 | Z. 3–5 | cosmetic | Die konditionale Einordnung ist kohärent; die Aussagen „offen“, „standard-shaped“ und „Erdős problem #251“ sind mangels Web-/Literaturzugriff UNVERIFIED. | 0.900 |
| A02 | Z. 9–14 | correct | Die Definitionen von Primzahlen, Lücken, S, π_H, M_H und Zulässigkeit sind intern konsistent. | 0.990 |
| A03 | Z. 16–19 | correct | Hypothese A hat klare Quantoren und ist eine starke, aber widerspruchsfreie uniforme Primtupel-Annahme. | 0.980 |
| A04 | Z. 20–21 | correct | Aus Lemma 4.1 und k+1≤4 ln ln x folgt uniform log M_H=ln x-o(ln x), also M_H=x^{1-o(1)}≫1. | 0.970 |
| A05 | Z. 22–25 | correct | Eine zweiseitige relative Approximation einer positiven Modellmasse M<1 durch eine ganze konsekutive Anzahl ist unmöglich, weshalb die Designwarnung sachlich zutrifft. | 0.930 |
| A06 | Z. 26–27 | correct | Der alternative Fehler |π_H-M_H|≤M_H/3+x^t liefert wegen M_H=x^{1-o(1)} und t<1 schließlich dieselben groben Faktoren 1/2 und 2. | 0.960 |
| A07 | Z. 29–30 | repairable | Hypothese B ist kohärent, aber C_g>0 sollte explizit verlangt oder C_g nachträglich auf max(C_g,1) vergrößert werden, da später log₂(4C_g) benutzt wird. | 0.990 |
| A08 | Z. 32–33 | correct | Bei der üblichen 0-Indizierung p_{n+1}=Nat.nth Prime n ist die zweite Reihe exakt 2S; die konkrete Lean-Bibliotheksnotation ist UNVERIFIED. | 0.960 |
| A09 | Z. 35–38 | correct | Keine Hypothese erwähnt Rationalität oder S, und im Beweis übernehmen A und B getrennte Muster- bzw. Schwanzrollen; die Aussage „sharpest known“ ist hingegen UNVERIFIED. | 0.940 |
| A10 | Z. 42–44 | correct | Die verwendete obere Schranke p_n≤C_0 n ln(n+2) genügt, wobei Zitat und genaue Fundstelle UNVERIFIED bleiben. | 0.950 |
| A11 | Z. 44–45 | correct | Aus p_n=O(n ln n) folgt durch Vergleich mit ∑n ln(n+2)2^{-n} die absolute Konvergenz von S und allen verschobenen Schwänzen. | 0.990 |
| A12 | Z. 45–46 | correct | Aus u_n-p_{n+1}=∑_{k≥1}(p_{n+k}-p_{n+1})2^{-k} und absolut erlaubtem Summenwechsel folgt δ_n=∑_{j≥1}g_{n+j}2^{-j}. | 0.990 |
| A13 | Z. 47 | correct | Indexverschiebung ergibt δ_{n+1}=2δ_n-g_{n+1}, und für n≥1 sind alle g_{n+j} gerade und mindestens 2, also δ_n≥2. | 0.990 |
| A14 | Z. 48–49 | correct | Die bloße Schranke p_n≤2^n gäbe nur p_n2^{-n}≤1 und somit keinen konvergenten Majoranten. | 0.990 |
| A15 | Z. 51–52 | correct | Aufspaltung der δ_n-Reihe nach den ersten T Termen liefert die Blockidentität exakt. | 0.990 |
| A16 | Z. 54–57 | cosmetic | Die rationale Darstellung mit ungeradem b und s≥1 ist erreichbar, doch „s positive“ und die anschließende Diskussion s=0 verwenden uneinheitliche Konventionen für natürliche Zahlen. | 0.980 |
| A17 | Z. 58–59 | correct | Die Identität 2^nS=∑_{j≤n}p_j2^{n-j}+u_n zeigt für n≥s unmittelbar b u_n,bδ_n∈ℤ. | 0.990 |
| A18 | Z. 60–64 | correct | Für n≥s ist g_{n+1} eine Differenz ungerader Primzahlen, daher ist bδ_{n+1}=2bδ_n-bg_{n+1} gerade und die Schwelle s+1 ist richtig. | 0.990 |
| A19 | Z. 66–71 | correct | Nach Kürzung des gemeinsamen Präfixes gilt b(δ_{n+J}-δ_{m+J})=2^J b(δ_n-δ_m)∈2^{J+1}ℤ. | 0.990 |
| A20 | Z. 73–74 | correct | Die elementare Quantisierungsaussage über ein Vielfaches von 2^{J+1} ist exakt. | 1.000 |
| A21 | Z. 78–86 | correct | Die FM-Definition ist indexmäßig konsistent und L=J+2+K umfasst Präfix, zwei Gabelstellen und K Suffixlücken. | 0.990 |
| A22 | Z. 87–89 | correct | Die angekündigte Exact-hit-Robustheit entspricht dem späteren Beweis, der Gleichheit erzwingt und keine Nichtganzzahligkeitsannahme verwendet. | 0.980 |
| A23 | Z. 91–94 | correct | FM-2 und FM-3 erlauben gleichzeitig min(n,m)≥s+1 und (γ+4)/2^J<8/b; die umgeformte Gitterungleichung ist äquivalent. | 0.990 |
| A24 | Z. 95–96 | correct | Aus 2≤δ_{n+L},δ_{m+L}≤2^K folgt |Δ_end|≤2^K-2<2^K. | 0.990 |
| A25 | Z. 97–99 | correct | Die gewichteten Differenzen +γ an Stelle J+1 und −γ an Stelle J+2 ergeben γ/2−γ/4 plus 2^{-(K+2)}Δ_end. | 0.990 |
| A26 | Z. 100–101 | correct | Die Endschranke liefert einen strikt kleineren Rest als 1/4 und damit |δ_{n+J}-δ_{m+J}|<(γ+1)/4<(γ+4)/4. | 0.990 |
| A27 | Z. 102–104 | correct | Lemma 2.4 und die strikte Größenschranke zwingen das relevante Gittervielfache auf null. | 0.990 |
| A28 | Z. 105–106 | correct | Aus der erzwungenen Gleichheit folgt |Δ_end|=γ2^K≥2^{K+1}, im Widerspruch zu Schritt 1. | 0.990 |
| A29 | Z. 110–113 | correct | Die Definition einer konsekutiven Realisierung stimmt mit dem Lückenwort und seinem kumulativen Punktset überein. | 0.990 |
| A30 | Z. 115–117 | correct | Die behauptete untere Schranke der singulären Reihe ist plausibel und durch die angegebenen lokalen Abschätzungen tatsächlich herleitbar. | 0.940 |
| A31 | Z. 118–123 | repairable | Der Text gibt nur einen QED-sketch ohne vollständige Summenabschätzungen und ohne verifizierte Mertens-Konstanten, obwohl die Lücke mit Standardabschätzungen geschlossen werden kann. | 0.930 |
| A32 | Z. 116–117 | correct | Für k=O(ln ln x) sind k ln(k+2) und (k+1)ln ln x beide o(ln x), sodass die Massenfolgerung uniform gilt. | 0.980 |
| A33 | Z. 125–128 | correct | Lemma 4.2 quantifiziert für jedes feste κ über alle zulässigen geraden H mit D≤κk ln(k+2), wobei C_2 nur von κ abhängen darf. | 0.970 |
| A34 | Z. 129–130 | correct | Bei einer neuen Restklasse ist der lokale Quotient 1−ν/((p−ν)(p−1))≤1−1/(p−1)^2<1. | 0.990 |
| A35 | Z. 131 | repairable | Die Zwischenbehauptung, es gebe höchstens 3k kollidierende Primzahlen p>2(k+1), ist für beliebig großes festes κ falsch, wie H={0,10014}, t=10010, k=1 zeigt. | 0.999 |
| A36 | Z. 131–132 | repairable | Auch die κ-unabhängige Produktschranke e^2 ist bei k=1 und hinreichend riesigem festem κ falsch; korrekt ist eine Schranke e^{O_κ(1)}. | 0.998 |
| A37 | Z. 132 | correct | Für kleine Primzahlen ist das Produkt der möglichen Faktoren p/(p−1) durch O(ln(k+2)) beschränkt, vorbehaltlich UNVERIFIED Mertens-Zitat. | 0.960 |
| A38 | Z. 132–133 | correct | Die Anzahl gerader Kandidaten t ist höchstens D/2≤(κ/2)k ln(k+2). | 0.990 |
| A39 | Z. 125–133 | repairable | Die Lemmaaussage bleibt richtig, wenn man die falschen 3k/e^2-Sätze durch O_κ(k) beziehungsweise e^{O_κ(1)} ersetzt; der vorhandene Beweissketch ist daher nicht wörtlich gültig. | 0.970 |
| A40 | Z. 135–140 | correct | Die Hypothesen von Lemma 4.3 lassen genau einen zusätzlichen Punkt innerhalb des A-Fensters zu und die behauptete uniforme Untergrenze ist mit den Folgeschritten vereinbar. | 0.970 |
| A41 | Z. 141–143 | correct | Für einen ungeraden Anker p>√x kann eine zusätzliche Primzahl zwischen p und p+D nur an einem geraden inneren Offset liegen; die Formulierung „p>D“ ist nur sprachlich unsauber. | 0.980 |
| A42 | Z. 143–145 | correct | Eine unzulässige Erweiterung besitzt eine deckende Primzahl q≤L+2, die dann eines der Zahlen p+h>√x>q echt teilt, also keine Realisierung zulässt. | 0.990 |
| A43 | Z. 145–148 | correct | Aus L+1≤4 ln ln x−1 folgt für jede Erweiterung L+2≤4 ln ln x, und der Polylog-Span liegt schließlich unter (ln x)^3. | 0.980 |
| A44 | Z. 149 | correct | Die erste Bonferroni-/Union-Bound-Zeile zieht kleine Anker und jede mögliche zulässige Zusatzprimzahl ab und ist als Untergrenze exakt. | 0.990 |
| A45 | Z. 150 | correct | Hypothese A liefert den Faktor 1/2 für H und Faktor 2 für Erweiterungen, während π_H(√x)≤√x gilt. | 0.990 |
| A46 | Z. 151 | correct | Mit M_{H∪{t}}/M_H=(𝔖(H∪{t})/𝔖(H))/ln x ergibt Lemma 4.2 genau den angezeigten Fehlerterm. | 0.990 |
| A47 | Z. 152 | correct | Da k ln^2(k+2)/ln x→0 und √x/M_H→0 uniform, ist die Gesamtabzugsquote schließlich höchstens 1/4 und die Konstante 1/4 korrekt. | 0.980 |
| A48 | Z. 153–155 | correct | Die Konstantenverkettung k=L und κ aus der Spanhypothese ist richtig, sofern Lemma 4.2 in reparierter Form verwendet wird. | 0.970 |
| A49 | Z. 156–158 | correct | Jeder Startindex bestimmt genau ein Längen-L-Lückenwort; die Zusatzzeile ist tautologisch und im Beweis unbenutzt. | 0.990 |
| A50 | Z. 160–163 | correct | Für ν groß genug gilt B für alle ν+j, und iteriertes Bertrand ergibt p_{ν+j}<2^j p_ν; Literaturbezeichnung und Zitat sind UNVERIFIED. | 0.970 |
| A51 | Z. 164–167 | correct | Mit ∑2^{-j}=1 und ∑j^2 2^{-j}=6 folgt 2a^2+12≤3a^2 genau ab a^2≥12. | 0.990 |
| A52 | Z. 171–173 | repairable | K,J,L sind asymptotisch korrekt definiert, doch die Verwendung von log₂(4C_g) erfordert die in A07 fehlende explizite Positivität von C_g. | 0.990 |
| A53 | Z. 172–173 | correct | K=⌈log₂ H_x⌉ impliziert exakt 2^K≥H_x=4C_g(ln x)^2. | 0.990 |
| A54 | Z. 174–176 | correct | i_0=J+1 liegt mit i_0+1=J+2≤L im Inneren, und γ ist gerade, weil alle q_i ungerade Primzahlen sind. | 0.990 |
| A55 | Z. 177–180 | repairable | Für Lemma 4.3 müssen A und A′ ausdrücklich durch Subtraktion von q_0 auf Punktsets mit Start 0 normiert werden; Translation ändert weder Lücken noch Zulässigkeit. | 0.990 |
| A56 | Z. 181–183 | repairable | Die Wörter teilen genau J Präfix- und K Suffixstellen, aber bei der natürlichen Zuordnung A↦w,A′↦w′ gilt w−w′=(−γ,+γ), sodass die Orientierung erst durch Vertauschen stimmt. | 0.999 |
| A57 | Z. 184–186 | correct | Für p≤L+2 fehlt vor Translation die Restklasse 0 und für p>L+2 sind L+1 Punkte zu wenige, um alle Restklassen zu bedecken. | 0.990 |
| A58 | Z. 187–188 | correct | Mit r=π(L+3)≤L+2 ist q_{L+1}=p_{r+L+2}≤p_{2L+4}, woraus eine feste C_1-Schranke C_1L ln L folgt. | 0.970 |
| A59 | Z. 188–190 | correct | Aus 2^J≥(K+20)^4, L≤2(K+20) und ln L≤K+20 folgt für große x die angezeigte O((K+20)^{-2})-Schranke. | 0.980 |
| A60 | Z. 191–192 | cosmetic | Asymptotisch ist L+2=(2/ln2)ln ln x+O(ln ln ln x)<3 ln ln x, doch die Formulierung „L+2 Punkte plus ein Erweiterungspunkt“ vermischt Basis- und Erweiterungskardinalität. | 0.970 |
| A61 | Z. 192 | correct | C_1L ln L=O(ln ln x·ln ln ln x) liegt für hinreichend großes x weit unter (ln x)^3. | 0.990 |
| A62 | Z. 196–198 | repairable | Der Span erfüllt Lemma 4.3 mit κ=max(1,C_1), nicht zwingend wörtlich κ=C_1, falls C_1 nicht zuvor ≥1 gewählt wurde. | 0.980 |
| A63 | Z. 198–201 | correct | Lemma 4.3 liefert je eine Realisierung, und derselbe Start kann wegen der unterschiedlichen Stelle J+1 nicht beide Wörter realisieren. | 0.990 |
| A64 | Z. 202 | correct | Nach dem in A56 erwähnten Vertauschen liefern die Wortidentitäten exakt FM-P, FM-F und FM-S. | 0.990 |
| A65 | Z. 203–206 | correct | Für ν=n_x+L gilt p_ν≤p_{n_x+L+1}≤x+D=x e^{o(1)}, daher δ_ν≤3C_g(ln x+o(ln x))^2≤H_x≤2^K. | 0.980 |
| A66 | Z. 207 | correct | FM-2 folgt direkt aus A59. | 0.990 |
| A67 | Z. 207–208 | correct | p_{n_x+1},p_{m_x+1}>√x zwingt beide Indizes und damit ihr Minimum gegen unendlich. | 0.990 |
| A68 | Z. 209 | correct | Die Wahl irgendeiner Folge x_r→∞ erzeugt die in FM verlangten Folgen nach Verwerfung endlich vieler Anfangswerte. | 0.980 |
| A69 | Z. 210–211 | correct | Irrationalität bleibt unter Multiplikation mit der von null verschiedenen rationalen Zahl 2 erhalten. | 0.990 |
| A70 | Z. 215–219 | correct | Der Text behauptet zu Recht keine logische Unabhängigkeit von A und B; die weitergehende Aussage über unbekannte Ableitungen ist UNVERIFIED. | 0.950 |
| A71 | Z. 220–222 | correct | Das Nichtvorliegen einer Lean-Kompilationsbehauptung ist klar und hat keinen Einfluss auf den Papierbeweis. | 0.990 |
| A72 | Z. 223–225 | cosmetic | A ist der Form nach Hardy–Littlewood-artig, aber wegen wachsendem k und uniformem Faktor materiell stärker als die übliche fest-H-Version; Offenheits- und Namensangaben sind UNVERIFIED. | 0.940 |
| A73 | Z. 229–233 | cosmetic | Die behauptete Kernel-Ordnung und Plausibilitätsbewertung sind unbenutzte Forschungsmeinungen und ohne externe Unterlagen UNVERIFIED. | 0.860 |
| A74 | Z. 234–239 | cosmetic | Die Lean-Schnittstellennamen und das Fehlen von True-Platzhaltern sind ohne Quellcode UNVERIFIED und für den mathematischen Schluss irrelevant. | 0.900 |
| A75 | Z. 240–242 | cosmetic | Die Bezeichnung als „sharpest weakening target“ ist eine unbenutzte Prioritäts-/Literaturaussage und UNVERIFIED. | 0.820 |
| A76 | Z. 243–246 | cosmetic | Die empirische Konsistenz und die beiden endlichen Ausschlussrekorde sind ohne Datensatz oder Zertifikat UNVERIFIED und werden nirgends im Beweis benutzt. | 0.880 |

### Phase-A-Gesamturteil

**gaps found:**

1. **Lemma 4.2, Beweissketch:** Die Aussagen „höchstens 3k“ und „Produkt ≤e²“ sind für beliebig großes festes κ falsch; die Lemmaaussage ist aber durch κ-abhängige Schranken reparierbar.
2. **Analytische Ausführung:** Lemma 4.1 und Lemma 4.2 sind als „QED-sketch“ statt als vollständige Beweise niedergeschrieben; die fehlenden Abschätzungen sind standardnah und lokal ergänzbar, aber der Text ist damit nicht buchstäblich eine vollständig ausgeschriebene Beweiskette.
3. **Deletion-Konstruktion:** Die Punktmengen müssen für Lemma 4.3 um −q₀ auf 0 normiert werden, und bei der natürlichen Benennung ist die Vorzeichenorientierung zunächst (−γ,+γ), nicht (+γ,−γ); das in Abschnitt 6 erlaubte Vertauschen repariert dies.
4. **Kleine Quantoren-/Konstantenpflege:** C_g>0, C_1≥1 beziehungsweise κ=max(1,C_1) und die genaue Basis-/Erweiterungskardinalität sollten explizit formuliert werden.

Keiner dieser Punkte ist fatal für den konditionalen Hauptschluss. **Phase-A-Gesamtconfidence: 0.91.**

**Prozessbestätigung:** Phase A ist hier vollständig ausgeschrieben und abgeschlossen; erst ab der folgenden Überschrift wird Phase B geöffnet und nach P1–P8 strukturiert.

## 2. Phase B — gezielte Proben

### P1. Hypothesenstärke, Rollen und Zirkularität

**Argument dafür, A als Hardy–Littlewood-artig zu bezeichnen.** A zählt für jedes zulässige endliche Offsetset Übersetzungen, bei denen alle verschobenen Zahlen prim sind, und verwendet exakt die singuläre Reihe sowie die Haupttermform \(x/(\ln x)^{|H|}\). Sie enthält weder konsekutive Lücken noch \(\delta_n\), Rationalität oder die Zahl \(S\). In diesem strukturellen Sinn ist A eine uniforme Hardy–Littlewood-Tupelannahme.

**Argument dagegen, A als „gewöhnliche“ Hardy–Littlewood-Vermutung zu bezeichnen.** Die Uniformität gilt gleichzeitig für \(|H|\le 4\ln\ln x\), für alle Spannen bis \((\ln x)^3\), mit einem festen zweiseitigen Faktor. Das ist materiell stärker als eine fest-\(H\)-Asymptotik und sollte als **starke uniforme Hardy–Littlewood-artige Hypothese** bezeichnet werden, nicht als bloße Standardform ohne Zusatz.

**Rolle von B.** B wird nicht zur Erzeugung der zwei Wörter benutzt; dies tut A über Lemma 4.3. B wird ausschließlich benutzt, um die beiden Endschwänze punktweise durch \(2^K\) zu beschränken. Damit sind die Rollen im Beweis funktional getrennt.

**Argument für Unabhängigkeit in der Rolle.** Entfernt man A, fehlen die zwei benötigten konsekutiven Realisierungen; entfernt man B, liefert der Text keine uniforme FM-1-Schranke an den ausgewählten Stellen. Die beiden Eingaben bedienen somit verschiedene Beweisinterfaces.

**Argument gegen eine Behauptung logischer Unabhängigkeit.** Aus den zwei Dateien folgt nicht, dass A B weder impliziert noch widerlegt; der Text nimmt diese logische Unabhängigkeit ausdrücklich nicht in Anspruch. „Independent in role“ ist daher richtig, „logically independent“ wäre UNVERIFIED.

**Zirkularität in beide Richtungen.** Weder A noch B erwähnt \(S\), rationale Darstellungen, die Gitteraussage oder FM. Umgekehrt enthält die Irrationalität eines einzelnen gewichteten Primzahlwerts ersichtlich keine im Text hergeleitete Information, die uniforme Tupelzählungen oder eine punktweise \(O(\log^2 p)\)-Lückenschranke ergäbe. Es gibt daher keine verdeckte Annahme der Konklusion oder einer im Dokument nachgewiesenen Äquivalenz.

**P1-Fazit:** A ist eine starke uniforme Hardy–Littlewood-artige Tupelhypothese; B ist in der Beweisrolle separat, ohne dass logische Unabhängigkeit behauptet oder bewiesen wäre; keine Klausel ist zirkulär. Literatur- und Namensabgleich: **UNVERIFIED**.

### P2. Deletion-Konstruktion mit zwei vollständigen Beispielen

Für beide Beispiele bezeichnet \(w\) das Wort von \(A\) und \(w'\) das Wort von \(A'\), genau in der Reihenfolge der Definition. Die Rechnung zeigt deshalb zunächst \(w-w'=(-\gamma,+\gamma)\) an den Gabelstellen; nach Vertauschen der beiden Wörter erhält man die FM-Orientierung \((+\gamma,-\gamma)\).

#### Beispiel 1: \(J=3,\ K=4\)

\[
L=J+2+K=9,\qquad L+3=12,\qquad i_0=J+1=4.
\]

Die ersten \(L+2=11\) Primzahlen größer als 12 sind
\[
(q_0,\ldots,q_{10})=(13,17,19,23,29,31,37,41,43,47,53).
\]
Damit
\[
\gamma=q_5-q_4=31-29=2.
\]

Es werden \(q_{i_0+1}=q_5=31\) beziehungsweise \(q_{i_0}=q_4=29\) gelöscht:
\[
A=(13,17,19,23,29,37,41,43,47,53),
\]
\[
A'=(13,17,19,23,31,37,41,43,47,53).
\]

Die vollständigen Lückenwörter lauten
\[
w=(4,2,4,6,8,4,2,4,6),
\]
\[
w'=(4,2,4,8,6,4,2,4,6).
\]

Prüfung:
- gemeinsames Präfix der Länge \(J=3\): \((4,2,4)\);
- Gabelstellen \(J+1=4\) und \(J+2=5\): \(w-w'=(-2,+2)=(-\gamma,+\gamma)\);
- gemeinsames Suffix der Länge \(K=4\): \((4,2,4,6)\);
- Interieur: \(1\le i_0=4\) und \(i_0+1=5\le L=9\).

Nach Vertauschen \(w'\leftrightarrow w\) ist die Differenz an den Gabelstellen \((+\gamma,-\gamma)\), exakt wie FM-F.

Die auf 0 normierten Punktsets sind
\[
A-q_0=(0,4,6,10,16,24,28,30,34,40),
\]
\[
A'-q_0=(0,4,6,10,18,24,28,30,34,40).
\]

#### Beispiel 2: \(J=2,\ K=3\)

\[
L=7,\qquad L+3=10,\qquad i_0=3.
\]

Die ersten \(L+2=9\) Primzahlen größer als 10 sind
\[
(q_0,\ldots,q_8)=(11,13,17,19,23,29,31,37,41),
\]
und
\[
\gamma=q_4-q_3=23-19=4.
\]

Somit
\[
A=(11,13,17,19,29,31,37,41),
\]
\[
A'=(11,13,17,23,29,31,37,41),
\]
\[
w=(2,4,2,10,2,6,4),
\]
\[
w'=(2,4,6,6,2,6,4).
\]

Prüfung:
- gemeinsames Präfix der Länge 2: \((2,4)\);
- Gabelstellen 3 und 4: \(w-w'=(-4,+4)=(-\gamma,+\gamma)\);
- gemeinsames Suffix der Länge 3: \((2,6,4)\);
- \(i_0=3\) und \(i_0+1=4\le7\).

Auch hier liefert Vertauschen exakt \((+\gamma,-\gamma)\). Die normierten Punktsets sind
\[
(0,2,6,8,18,20,26,30),\qquad (0,2,6,12,18,20,26,30).
\]

**P2-Fazit:** Präfix-, Suffix- und Indexbehauptung sind richtig; die natürliche Beschriftung hat das umgekehrte Vorzeichenpaar und muss, wie Abschnitt 6 zulässt, vertauscht werden.

### P3. Quantoren-Stresstest für Lemma 4.2

Die präzise Familie ist:

Für jedes **fest gewählte** \(\kappa\ge1\) soll es eine Konstante \(C_2(\kappa)\) geben, sodass für jedes \(k\ge0\) und jedes zulässige Set
\[
H=\{0=h_0<h_1<\cdots<h_k\}
\]
aus geraden ganzen Zahlen mit
\[
D=h_k\le\kappa k\ln(k+2)
\]
gilt
\[
\sum_{\substack{0<t<D,\ t\ {\rm gerade},\ t\notin H\\H\cup\{t\}\ {\rm zulässig}}}
\frac{\mathfrak S(H\cup\{t\})}{\mathfrak S(H)}
\le C_2(\kappa)k\ln^2(k+2).
\]
Es gibt in diesem Lemma keinen \(x\)-Quantor und keine A-Budgetbedingung; \(C_2\) darf von \(\kappa\), aber nicht von \(k,H,t\), abhängen.

**Kleinste Randfälle.**
- \(k=0\): \(D=0\), die Summe ist leer und beide Seiten sind 0.
- \(k=1,\kappa=1\): Wegen des kleinsten positiven geraden Offsets 2 und \(2>\ln3\) gibt es kein nichttriviales \(H\), also ist der Fall vakuos.
- \(k=1,\kappa=4\): Zulässig sind am Rand unter anderem \(H=\{0,4\}\), doch der einzige innere gerade Kandidat \(t=2\) macht \(\{0,2,4\}\) modulo 3 unzulässig; die Summe ist 0.

**Exhaustive kleine Suche.** Für \(\kappa=4\), \(1\le k\le4\), alle geraden Sets bis zur abgerundeten Spangrenze und alle zulässigen inneren Erweiterungen wurden 267 zulässige \(H\) enumeriert. Die singulären Quotienten wurden als endliche Eulerprodukte bis \(p\le100000\) approximiert; die schärfsten gefundenen normalisierten Summen waren:

| k | schärfstes H | D | Summe der Quotienten (Cutoff \(10^5\)) | geteilt durch \(k\ln^2(k+2)\) |
|---:|---|---:|---:|---:|
| 1 | \(\{0,2\}\) oder \(\{0,4\}\) | 2/4 | 0 | 0 |
| 2 | \(\{0,4,10\}\) | 10 | 1.93647 | 0.50382 |
| 3 | \(\{0,2,8,18\}\) | 18 | 5.49160 | 0.70669 |
| 4 | \(\{0,2,6,24,26\}\) | 26 | 10.70414 | 0.83355 |

Beim letzten Set sind genau drei zulässige Erweiterungen vorhanden, jede mit approximativem Quotienten 3.56805. Die Werte stabilisierten sich beim Cutoffwechsel \(100,1000,5000,20000,100000\); dies ist ein numerischer Stresstest, kein Beweis des unendlichen Produkts.

**Endlicher Gegenbeleg gegen den Beweissatz „höchstens \(3k\)“.** Setze
\[
k=1,\quad H=\{0,10014\},\quad t=10010.
\]
Dann sind \(H\) und \(H\cup\{t\}\) zulässig; die Spanhypothese gilt für jedes feste
\[
\kappa\ge \frac{10014}{\ln3}=9115.1356\ldots.
\]
Die vier Primzahlen \(5,7,11,13>2(k+1)=4\) kollidieren, weil sie \(t\) teilen. Das sind 4 statt höchstens \(3k=3\).

**Endlicher Gegenbeleg gegen das κ-unabhängige Produkt \(e^2\).** Für
\[
t=2\prod_{5\le p\le10^6}p,\qquad H=\{0,t+6\},\qquad k=1
\]
ist die Erweiterung mit \(t\) zulässig, und das endliche Produkt der großen Kollisionsfaktoren ist
\[
\prod_{5\le p\le10^6}\frac p{p-1}\approx8.20246>e^2\approx7.38906.
\]
Die hierfür benötigte \(\kappa\) ist zwar astronomisch, aber das Lemma quantifiziert über jedes feste \(\kappa\).

**Reparatur.** Für einen festen Kandidaten \(t\) ist der lokale Quotient bei einer neuen Restklasse kleiner als 1; nur Kollisionsprimzahlen tragen \(p/(p-1)>1\) bei. Für \(p\le2(k+1)\) ist ihr Produkt \(O(\ln(k+2))\). Für \(p>2(k+1)\) teilt eine solche Primzahl mindestens eine der Zahlen \(t-h_i\), und
\[
\sum_{\substack{p\mid(t-h_i)\\p>2(k+1)}}\frac1{p-1}
\le
\frac{\log D}{\log(2(k+1))}\frac1{2k+1}.
\]
Nach Summation über \(i=0,\ldots,k\) ist dies \(O_\kappa(1)\), wobei endlich viele kleine \(k\) in die \(\kappa\)-abhängige Konstante eingehen. Also ist jeder Quotient
\[
O_\kappa(\ln(k+2)),
\]
und mit höchstens \(D/2=O_\kappa(k\ln(k+2))\) Kandidaten folgt die behauptete Summe.

**P3-Fazit:** Kein Gegenbeispiel zur Lemmaaussage wurde gefunden; zwei wörtliche Zwischenbehauptungen des Beweissketches sind jedoch falsch und müssen durch \(\kappa\)-abhängige Versionen ersetzt werden.

### P4. Transferkette und Konstanten

Sei \(H=H(w)\) mit \(k=L\).

1. Die Anzahl der konsekutiven Realisierungen mit Anker in \((\sqrt x,x]\) ist mindestens
   \[
   \pi_H(x)-\pi_H(\sqrt x)-\sum_t\pi_{H\cup\{t\}}(x).
   \]
   Mehrfach vorhandene Zusatzprimzahlen verursachen nur Mehrfachabzug und gefährden eine Untergrenze nicht.

2. Hypothese A gibt
   \[
   \pi_H(x)\ge\frac12M_H(x),\qquad
   \pi_{H\cup\{t\}}(x)\le2M_{H\cup\{t\}}(x).
   \]
   Außerdem \(\pi_H(\sqrt x)\le\pi(\sqrt x)\le\sqrt x\). Damit sind die Faktoren \(1/2\) und \(2\) korrekt.

3. Wegen
   \[
   M_{H\cup\{t\}}(x)
   =M_H(x)\frac{\mathfrak S(H\cup\{t\})/\mathfrak S(H)}{\ln x}
   \]
   liefert Lemma 4.2
   \[
   2\sum_tM_{H\cup\{t\}}(x)
   \le
   2C_2(\kappa)L\ln^2(L+2)\frac{M_H(x)}{\ln x}.
   \]

4. Uniform gilt bei \(L=O(\ln\ln x)\)
   \[
   \frac{2C_2L\ln^2(L+2)}{\ln x}\to0,\qquad
   \frac{\sqrt x}{M_H(x)}=x^{-1/2+o(1)}\to0.
   \]
   Für hinreichend großes \(x\) ist die Summe dieser beiden relativen Fehler höchstens \(1/4\), also
   \[
   N_{\rm cons}\ge\left(\frac12-\frac14\right)M_H=\frac14M_H.
   \]
   Die Konstante \(1/4\) ist somit korrekt.

5. **Kardinalitäten:** Das Wort hat \(L\) Lücken und \(L+1\) Punkte. Lemma 4.3 nimmt \(L+1\le4\ln\ln x-1\) an; jede Einpunkterweiterung hat \(L+2\le4\ln\ln x\) Punkte. In Abschnitt 5 ist
   \[
   L+2=K+J+4=\frac{2}{\ln2}\ln\ln x+O(\ln\ln\ln x),
   \]
   und \(2/\ln2\approx2.88539<4\), sodass die Bedingung schließlich erfüllt ist. Die Formulierung in 5(iv) ist unsauber, aber die tatsächliche Reserve reicht.

6. **Spanverkettung 4.3→4.2:** Lemma 4.3 verlangt \(D\le\kappa L\ln(L+2)\), und Lemma 4.2 wird mit \(k=L\) und genau demselben festen \(\kappa\) aufgerufen.

7. **Spanverkettung 5→6→4.3:** Abschnitt 5 liefert \(D\le C_1L\ln L\le C_1L\ln(L+2)\). Man darf \(C_1\) ohne Verlust auf mindestens 1 vergrößern und dann \(\kappa=C_1\) setzen; alternativ \(\kappa=\max(1,C_1)\). Außerdem ist dieser Span schließlich kleiner als \((\ln x)^3\), sodass A anwendbar ist.

**P4-Fazit:** Die Bonferroni-Konstanten, die echte \(L+1/L+2\)-Buchhaltung und die Konstantenverkettung sind korrekt, abgesehen von der reparierbaren sprachlichen Kardinalitätsverwechslung und der Konvention \(C_1\ge1\).

### P5. Abschnitt 5(iii)/(iv) und FM-Ledger

Aus
\[
K=\left\lceil\log_2(4C_g)+2\log_2\ln x\right\rceil
=\left\lceil\log_2\bigl(4C_g(\ln x)^2\bigr)\right\rceil
\]
folgt exakt
\[
2^K\ge4C_g(\ln x)^2=H_x.
\]

Ferner
\[
J=\lceil4\log_2(K+20)\rceil
\quad\Longrightarrow\quad
2^J\ge(K+20)^4.
\]
Mit \(\gamma\le C_1L\ln L\), \(L\le2(K+20)\) und \(\ln L\le K+20\) folgt
\[
\gamma+4\le2C_1(K+20)^2+4\le3C_1(K+20)^2
\]
für große \(x\) nach eventueller Vergrößerung von \(C_1\). Somit
\[
\frac{\gamma+4}{2^J}
\le\frac{3C_1}{(K+20)^2}\longrightarrow0.
\]

**FM-1 mit dem exakten Zweierpotenzziel.** Für \(\nu=n_x+L\) ist
\[
p_\nu\le p_{n_x+L+1}=p_{n_x+1}+D\le x+D=x(1+o(1)),
\]
und ebenso für \(m_x\). Lemma 4.4 gibt daher
\[
\delta_\nu\le3C_g(\ln p_\nu)^2
\le3C_g(\ln x+o(\ln x))^2
\le4C_g(\ln x)^2=H_x\le2^K.
\]
FM-1 verlangt genau \(2^{K_r}\), nicht \(2^{K_r+1}\) oder \(H_x\); die Kette erreicht genau diese geforderte Schranke.

**Lokale Zahlenkontrolle.** Für \(C_g=10\) ergaben die endlichen Rechnungen:

| \(\ln x\) | K | J | L | \(H_x\) | \(2^K/H_x\) | tatsächliches \((\gamma+4)/2^J\) der Konstruktion |
|---:|---:|---:|---:|---:|---:|---:|
| 10 | 12 | 20 | 34 | 4,000 | 1.0240 | \(1.3351\cdot10^{-5}\) |
| 100 | 19 | 22 | 43 | 400,000 | 1.31072 | \(1.9073\cdot10^{-6}\) |
| 1,000 | 26 | 23 | 51 | 40,000,000 | 1.67772 | \(7.1526\cdot10^{-7}\) |
| \(10^6\) | 46 | 25 | 73 | \(4\cdot10^{13}\) | 1.75922 | \(2.3842\cdot10^{-7}\) |

Diese Beispielwerte sollen nicht die asymptotische Budgetschwelle belegen; sie prüfen die Rundung und \(2^K\ge H_x\). Für \(C_g=10\) wurde numerisch die erste Rasterstelle \(\ln\ln x\approx34.50\) gefunden, an der \(L+2\le4\ln\ln x-1\) gilt; die Aussage ist ausdrücklich nur „für große \(x\)“.

**P5-Fazit:** Die Grenzwertrechnung und das exakte FM-1-Ziel \(2^K\) stimmen.

### P6. Theorem 3.2, Schritte 1–5

Setze
\[
\Delta_{\rm end}=\delta_{n+L}-\delta_{m+L}.
\]

1. **Endschwänze.** Beide Zahlen liegen im Intervall \([2,2^K]\), also
   \[
   |\Delta_{\rm end}|\le2^K-2<2^K.
   \]

2. **Gabelzerlegung.** Nach \(T=K+2\) Schritten ab \(n+J\) beziehungsweise \(m+J\) tragen die zwei unterschiedlichen Lücken
   \[
   \frac{\gamma}{2}+\frac{-\gamma}{4}=\frac\gamma4
   \]
   bei; die \(K\) Suffixlücken heben sich auf, und der Rest ist
   \[
   2^{-(K+2)}\Delta_{\rm end}.
   \]
   Somit
   \[
   \delta_{n+J}-\delta_{m+J}
   =\frac\gamma4+2^{-(K+2)}\Delta_{\rm end}.
   \]

3. **Nähe.**
   \[
   \left|2^{-(K+2)}\Delta_{\rm end}\right|<\frac14,
   \]
   also
   \[
   |\delta_{n+J}-\delta_{m+J}|
   <\frac{\gamma+1}{4}<\frac{\gamma+4}{4}.
   \]

4. **Gitterlock.** Aus dem gemeinsamen Präfix folgt
   \[
   b(\delta_{n+J}-\delta_{m+J})\in2^{J+1}\mathbb Z.
   \]
   Die Auswahl
   \[
   \frac{\gamma+4}{2^J}<\frac8b
   \]
   ist äquivalent zu
   \[
   \frac{b(\gamma+4)}4<2^{J+1}.
   \]
   Der Betrag des Gitterelements ist strikt kleiner als sein kleinstes positives Gittermaß, also ist er 0.

5. **Widerspruch.** Die Gleichheit der beiden \(\delta\)-Werte gibt
   \[
   \frac\gamma4=-2^{-(K+2)}\Delta_{\rm end},
   \]
   folglich
   \[
   |\Delta_{\rm end}|=\gamma2^K\ge2^{K+1},
   \]
   was Schritt 1 widerspricht.

**P6-Fazit:** Alle fünf arithmetischen Schritte sind exakt.

### P7. Exact-hit-Robustheit

Der Beweis braucht keine Aussage „\(\delta_n\) ist kein Integer“ oder „der Schwanz trifft kein Gitter“. Im Gegenteil zwingt Schritt 4 ausdrücklich den **exakten Treffer**
\[
\delta_{n+J}=\delta_{m+J}.
\]
Dieser Treffer wird in Schritt 5 eingesetzt und erzeugt wegen der Gabelgröße \(\gamma\ge2\) einen zu großen Endunterschied.

Die nötige Striktheit kommt an zwei Stellen aus vorhandenen deterministischen Schranken:
\[
|\Delta_{\rm end}|\le2^K-2<2^K,
\]
wobei die „−2“ aus \(\delta\ge2\) stammt, und daraus
\[
|2^{-(K+2)}\Delta_{\rm end}|<1/4.
\]
Damit bleibt die Gitterlock-Ungleichung strikt, selbst wenn ein Schwanz oder eine Differenz zufällig ganzzahlig ist.

**P7-Fazit:** Die behauptete Exact-hit-Immunität ist real und im Beweis korrekt umgesetzt.

### P8. Elementare Spotchecks

**Konvergenz.** \(p_n\le C_0n\ln(n+2)\) liefert einen summierbaren Majoranten. Dagegen würde \(p_n\le2^n\) nur
\[
p_n2^{-n}\le1
\]
liefern, und \(\sum1\) divergiert; die Warnung ist richtig.

**Parität am \(s\)-Rand.** Für \(n=s\ge1\) ist \(b\delta_s\) zunächst nur ganzzahlig. Die Rekursion ergibt
\[
b\delta_{s+1}=2b\delta_s-bg_{s+1}.
\]
Da \(s+1\ge2\), sind \(p_{s+1}\) und \(p_{s+2}\) beide ungerade, also \(g_{s+1}\) gerade; daher ist \(b\delta_{s+1}\) gerade. Dies beweist genau „gerade für alle Indizes \(\ge s+1\)“ und nicht unnötig schon bei \(s\). Die Umkodierung \(s=0\mapsto s=1\) vermeidet \(g_1=1\).

**Lemma 4.4.** Mit der erzeugenden Funktion
\[
\sum_{j\ge1}j^2z^j=\frac{z(1+z)}{(1-z)^3}
\]
folgt bei \(z=1/2\)
\[
\sum_{j\ge1}j^22^{-j}=6,
\qquad
\sum_{j\ge1}2^{-j}=1.
\]
Für \(a=\ln p_\nu\) ergibt
\[
\sum_{j\ge1}(a+j)^22^{-j}
\le2a^2+2\cdot6=2a^2+12\le3a^2
\]
genau unter der angegebenen Bedingung \(a^2\ge12\). Die numerische Konstante 3 und die Schwelle 12 stimmen.

**P8-Fazit:** Alle drei elementaren Spotchecks bestehen.

## 3. Endurteil

**SOUND with repairable issues.**

Die konditionale Kernkette
\[
A+B\Longrightarrow{\rm FM}\Longrightarrow S\notin\mathbb Q
\]
ist nach meiner Prüfung mathematisch tragfähig. Die folgenden Reparaturen sind erforderlich, bevor ich den Text als vollständig ausgeschriebenen Beweis akzeptieren würde:

1. In Lemma 4.2 die falschen κ-uniformen Behauptungen „≤3k“ und „Produkt ≤e²“ durch \(O_\kappa(k)\) und \(e^{O_\kappa(1)}\) ersetzen und die Summenabschätzung ausführen.
2. Die Beweisskizzen der Lemmas 4.1 und 4.2 zu vollständigen lokalen Eulerprodukt-/Mertens-Abschätzungen ausbauen.
3. In Abschnitt 5 die Punktsets als \(A-q_0,A'-q_0\) an Lemma 4.3 übergeben und die Wortorientierung explizit vertauschen.
4. \(C_g>0\), \(C_1\ge1\) oder \(\kappa=\max(1,C_1)\) sowie die \(L+1/L+2\)-Kardinalitäten sauber festhalten.

Keine gefundene Lücke zerstört den Hauptschluss; insbesondere sind FM-1, die Gitterquantisierung und der Exact-hit-Widerspruch korrekt.

**Overall confidence: 0.90.**

## 4. What I could not check

- **UNVERIFIED:** genaue Literaturstellen und Namenszuordnungen zu Hardy–Wright/Chebyshev, Bertrand, Mertens, Rosser–Schoenfeld und „Cramér–Granville“.
- **UNVERIFIED:** Erdős-Problemnummer 251, die Aussage „sharpest known weakening target“ und sonstige Prioritäts-/Offenheitsbehauptungen.
- **UNVERIFIED:** Lean-Bibliotheksname `Nat.nth Prime`, die genannten Skeleton-Namen und Kompilierbarkeit, da kein Lean-Projekt beigefügt ist.
- **UNVERIFIED:** die empirischen Angaben zu Primzahlen unter \(3\cdot10^7\), zur Schranke \(10^{298}\) und zu \(s\le1{,}857{,}459,\ b\le99{,}999\), da Datensatz, Code und Zertifikate fehlen.
- Die unendlichen singulären Reihen in P3 wurden nicht „numerisch bewiesen“; ich habe endliche Eulerprodukte bis zu angegebenen Cutoffs berechnet und die benötigte asymptotische Reparatur analytisch kontrolliert.
- Webzugriff wurde entsprechend der Vorgabe nicht verwendet.

## 5. Computations performed

1. **Datei- und Zeilenprüfung:** Beide lokalen Markdown-Dateien wurden direkt eingelesen; das Prüfobjekt hatte 12 622 Zeichen und die Payload 5 077 Zeichen.
2. **Deletion-Fall \(J=3,K=4\):** Primtabelle, beide Löschmengen, alle neun Lücken, Differenzvektor \((0,0,0,-2,2,0,0,0,0)\), normierte Punktsets und Zulässigkeit wurden per Python/SymPy neu berechnet.
3. **Deletion-Fall \(J=2,K=3\):** Primtabelle, beide Löschmengen, alle sieben Lücken, Differenzvektor \((0,0,-4,4,0,0,0)\), normierte Punktsets und Zulässigkeit wurden per Python/SymPy neu berechnet.
4. **Lemma-4.2-Kleinsuche:** Für \(\kappa=4\), \(1\le k\le4\), wurden 267 zulässige gerade Sets samt allen inneren zulässigen Erweiterungen exhaustiv enumeriert; Eulerprodukte wurden bei Cutoffs 100, 1 000, 5 000, 20 000 und 100 000 verglichen.
5. **Falscher 3k-Satz:** Für \(H=\{0,10014\},t=10010\) wurden Zulässigkeit, minimale \(\kappa=9115.135615\ldots\) und die vier großen Kollisionsprimzahlen \(5,7,11,13\) direkt berechnet.
6. **Falscher e²-Satz:** Das endliche Produkt \(\prod_{5\le p\le10^6}p/(p-1)\) wurde logarithmisch berechnet und ergab 8.20246098…, gegenüber \(e^2=7.38905610\ldots\).
7. **Geometrische Momente:** SymPy berechnete \(\sum_{j\ge1}2^{-j}=1\) und \(\sum_{j\ge1}j^22^{-j}=6\).
8. **Fork-Algebra:** Symbolische Vereinfachung von \(\gamma/2-\gamma/4+2^{-(K+2)}\Delta_{\rm end}\) ergab \(\gamma/4+\Delta_{\rm end}/(4\cdot2^K)\).
9. **K/J/H_x-Rundung:** Für \(C_g=10\) und \(\ln x\in\{10,100,1000,10^6\}\) wurden \(K,J,L,H_x,2^K/H_x\), die tatsächlichen Konstruktionsprimzahlen und \((\gamma+4)/2^J\) neu berechnet.
10. **Budget-Raster:** Für \(C_g=10\) wurde die asymptotische Kardinalitätsungleichung numerisch gerastert; \(L+2\le4\ln\ln x-1\) trat erstmals nahe \(\ln\ln x=34.50\) auf, während die stärkere Hilfsungleichung \(L+2\le3\ln\ln x\) erst nahe 448 auftrat.
11. **Allgemeine Indexarithmetik:** Die Positionen der gelöschten Punkte wurden algebraisch nachgerechnet; vor Vertauschung ist die Differenz stets \((-\gamma,+\gamma)\) an den Positionen \(J+1,J+2\), mit genau J gleichen Vorgängern und K gleichen Nachfolgern.

## 6. SHA-256

Wegen der unvermeidlichen Selbstreferenz bezieht sich der folgende Wert auf den vollständigen UTF-8-Report von der ersten Überschrift bis einschließlich dieses Satzes, jedoch ohne die nachfolgende Digest-Zeile.
SHA256: `861c734cdc913228ed81888a767c69689997e10b77b66e8860c2c452d4d2528a`
