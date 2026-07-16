# Literature verification report (item-0004)

Provenance: item-0004 executed as a steering session with web research
mode ON (ledger ANN-27, decision 3), operator istr, 2026-07-16.
Original artifact (UTF-8) held by the operator, sha256
8c095e5cd2c89149ee1e122975a72a3d27f4d25b786274dcdf621d72f9852fb4.
This copy is an ASCII transliteration (diacritics folded: Erdos,
Cramer, Teravainen, Turan, Hoelder, "series a valeur"; math symbols
spelled out); content otherwise verbatim, including the report's own
verdict vocabulary. Steering disposition: ledger ANN-28. Addendum
(forum verbatims, below the report): ledger ANN-29.

---

Verifikationsbericht -- Roadmap-Item-0004 (erdos251): CPAP- und Nachbarschafts-Literaturstatus

Stand: 2026-07-16. Alle Web-Quellen an diesem Datum abgerufen. Verdikt-Legende: BESTAETIGT (= Projekt-Zitat korrekt), KORRIGIERT (= Projekt-Zitat falsch, korrekte Daten angegeben), WIDERLEGT (= Sachbehauptung falsch), STILL-OPEN (= Statusfrage bestaetigt offen), NOT-FOUND/UNVERIFIZIERT.

## TL;DR
- **BET-06 wird als NEIN aufgeloest.** Kein Prior-Art fuer die Zielimplikation gefunden -- weder eine bedingte Herleitung (uniforme Hardy-Littlewood-Tupel + Cramer-Typ-Luecken ==> Irrationalitaet von sum p_n/2^n) noch ein staerkeres unbedingtes Resultat existiert in der Literatur; Erdos #251 ist per 2026-07-16 weiterhin OFFEN, und die Projekt-Nische ("Ausfuehrung von Taos Idee neun Monate spaeter") ist unbesetzt.
- **Die ScPu11-Anachronismus-Vermutung ist WIDERLEGT.** arXiv:1105.1451 und Acta Arith. 126 (2007) 295-303 sind dasselbe Paper (nachtraeglicher arXiv-Upload 2011 der 2007er Publikation, DOI 10.4064/aa126-4-1); die Zitat-Paarung im Projekt ist korrekt.
- **CPAP-3 ist weiterhin OFFEN.** Die Unendlichkeit dreier aufeinanderfolgender Primzahlen in AP mit gleichen Luecken ist per Juli 2026 nicht bewiesen; Shiu und Banks-Freiberg-Turnage-Butterbaugh liefern nur konstante Restklassen-Muster (kongruent mod q), nicht gleiche Luecken.

## Key Findings (Verdikt pro Item)
1. ScPu11-Identifikatoren -- Anachronismus-Vermutung WIDERLEGT / Zitat BESTAETIGT.
2. ScPu11-Inhaltsansprueche -- BESTAETIGT (aus PDF verifiziert); Attributions-Diskrepanz auf der Problemseite BESTAETIGT.
3. Kuperberg 2210.09775 + Gallagher 1976 -- BESTAETIGT (Kuperberg-Journalstatus geklaert).
4. Standardzitate -- Rosser-Schoenfeld BESTAETIGT; Mertens KORRIGIERT; Hardy-Wright-Theoremnummer UNVERIFIZIERT; Bertrand BESTAETIGT.
5. Cramer-Granville -- BESTAETIGT; Hypothese B getreue Wiedergabe.
6. Erdos #251 Mapping + Seitenstatus -- BESTAETIGT (offen); Forum-Kommentare UNVERIFIZIERT (Bot-Sperre).
7. CPAP-3-Status -- STILL-OPEN.
8. Pratt- und Tao-Teravainen-Nutzung -- BESTAETIGT.
9. BET-06 Prior-Art-Sweep -- NOT-FOUND ==> Aufloesung NEIN.
10. Mathlib-Namen -- GESCHLOSSEN (keine Web-Verifikation).

## Details

### Item 1 -- ScPu11-Identifikatoren (Anachronismus-Verdacht)
Abgerufen: arxiv.org/abs/1105.1451; biblio.ugent.be/publication/597120; arxiv.org/list/math/2011-05 (alle 2026-07-16).
arXiv:1105.1451, "The irrationality of some number theoretical series", J.-C. Schlage-Puchta, eingereicht 7. Mai 2011 (nur v1). Die arXiv-Seite traegt die Journal-Referenz "Acta Arith. 126 (2007), no. 4, 295--303" und die Related-DOI 10.4064/aa126-4-1. Es handelt sich um **ein und dasselbe Paper**: ein 2011 nachtraeglich hochgeladenes Preprint der bereits 2007 in Acta Arithmetica erschienenen Arbeit. Die 2011er arXiv-ID neben der 2007er Journal-Publikation ist **kein Anachronismus**, sondern Standardpraxis (Schlage-Puchta lud im Mai 2011 mehrere aeltere Arbeiten hoch, z.B. 1105.1452 = Ramanujan J. 12 (2006) 455-460). Verdikt: die Paarung im Projekt ist korrekt; die Anachronismus-Vermutung ist WIDERLEGT. Exakte Bibliographie: **J.-C. Schlage-Puchta, "The irrationality of some number theoretical series", Acta Arithmetica 126 (2007), no. 4, 295-303, DOI 10.4064/aa126-4-1, arXiv:1105.1451, MSC 11J72.**

### Item 2 -- ScPu11-Inhaltsansprueche
Abgerufen: Volltext-PDF arxiv.org/pdf/1105.1451 (2026-07-16). Alle im Dossier (dissektion.md sec.3.4) behaupteten Strukturelemente woertlich verifiziert:
- **Theorem 1**: fuer S_lambda = sum_{n>=0} [n^lambda]/n! ist {1,e} union {S_lambda : lambda in (0,infinity)\Z} Q-linear unabhaengig. Proposition 1 (Injektivitaet, Monotonie, Rechtsstetigkeit, Bild von Kontinuumsmaechtigkeit, Hausdorff-Dimension 0, total unzusammenhaengend) -- BESTAETIGT.
- **Theorem 2**: Ziffern-Konkatenation zur Basis b (b keine echte Potenz), alpha = 0.f(1)f(2)f(3)..., f nichtfallend, f(n+1)/f(n) ~ g(n), g nichtfallend mit g(n+1)/g(n) -> 1; Rationalitaet erzwingt g -> c, c Potenz von b, f(n+1) = c*f(n) + O(1). Mahler/Bundschuh-Linie explizit ([7] Mahler, J. Number Theory 13 (1981) 268-269; [1] Bundschuh, J. Number Theory 19 (1984) 248-253) -- BESTAETIGT.
- **Theorem 3**: 1, S_0, S_1, S_2, ... Q-linear unabhaengig, S_k = sum p_n^k/n!, UNBEDINGT (kein HL/Schinzel noetig) -- BESTAETIGT.
- **Beweismaschinerie**: Lemma 3 (Selberg-Sieb-Obergrenze via Halberstam-Richert [4, Thm 5.1]); Lemma 4 (kein nichttriviales Polynom in aufeinanderfolgenden Luecken verschwindet fuer positiven Anteil von n); Lemma 5 (Polynomalgebra, haelt Residuum nichttrivial); Lemma 6 (van-der-Corput + PNT, Diskrepanzschranke); zusaetzlich Lemma 1 (Weyl-van der Corput), Lemma 2 (Erdos-Turan). Rekursive Kreuz-Elimination ueber aufeinanderfolgende n mit Polynomkoeffizienten in den Luecken -- BESTAETIGT.
- **Historischer Anspruch**: Das Paper sagt woertlich: "P. Erdos[2] stated that S_k is irrational and gave a proof for k = 1. However, it appears that, for k > 1, no proof has appeared in print." Erdos-Ref [2] = **P. Erdos, "Sur certaines series a valeur irrationnelle", Enseignement Math. (2) 4 (1958), 93-100.** Verdikt: "per ScPu11 hat Erdos nur k=1 gedruckt bewiesen" -- BESTAETIGT.
- **ATTRIBUTIONS-DISKREPANZ (flag)**: Die erdosproblems.com/251-Seite schreibt "Erdos [Er58b] proved that sum p_n^k/n! is irrational for every k>=1". [Er58b] ist genau die 1958er Enseign.-Math.-Arbeit. Diese "fuer jedes k>=1"-Zuschreibung an Erdos widerspricht ScPu11, wonach Erdos nur k=1 druckte; die Allgemein-k-Aussage stammt (unbedingt) aus Schlage-Puchtas Theorem 3. Die Projekt-Vermutung, die Seite schreibe alle k faelschlich [Er58b] zu, ist BESTAETIGT.

### Item 3 -- Kuperberg + Gallagher
Abgerufen: arxiv.org/abs/2210.09775 + PDF; cambridge.org/Wiley Mathematika-Landingpages; academic.oup.com/qjmath (alle 2026-07-16).
- **Vivian Kuperberg, "Sums of singular series with large sets and the tail of the distribution of primes"**, arXiv:2210.09775 (v1 18. Okt. 2022, v2 15. Juni 2023, 20 S., math.NT). Titel und Autor exakt wie im Sekundaerdatensatz. **Journalstatus geklaert**: publiziert in **The Quarterly Journal of Mathematics 74 (2023), no. 4, 1457-1479, DOI 10.1093/qmath/haad030** (Oxford Academic; auf Kuperbergs Publikationsliste als Journal-Artikel 2023 gefuehrt). Inhalt passt zur Projektnutzung: Averaging/Summierung singulaerer Reihen in der Gallagher/Montgomery-Soundararajan-Linie, mit k gross relativ zu h; Anwendung auf den Tail (Anzahl Intervalle [n, n+lambda log x] mit >= k Primzahlen << x*exp(-k/(lambdae))). Relevant fuer die Luecke zwischen HL-Inputs fester Dimension und Fenstern der Groesse log log x.
- **P. X. Gallagher, "On the distribution of primes in short intervals", Mathematika 23 (1976), no. 1, 4-9, DOI 10.1112/S0025579300016442.** Seiten exakt bestaetigt. Standardcharakterisierung bestaetigt: Gallagher leitet aus einer uniformen Hardy-Littlewood-Prime-k-Tupel-Vermutung bei fester/beschraenkter Dimension eine Poisson-Verteilung der Primzahlen in log-grossen Intervallen ab (Kuperberg-Abstract: "In 1976, Gallagher showed that the Hardy-Littlewood conjectures on prime k-tuples imply that the distribution of primes in log-size intervals is Poissonian ... For both of these analyses, k is fixed throughout").

### Item 4 -- Standardzitate der Kette
(a) **Mertens -- KORRIGIERT.** Die Mertensschen Saetze (drei asymptotische Gesetze, inkl. prod_{p<=x}(1-1/p)^{-1} ~ e^gamma*log x, Basis fuer Schranken der Form prod(1-1/p)^{-1} <= C*ln(k+2)) stehen in **F. Mertens, "Ueber einige asymptotische Gesetze der Zahlentheorie", J. reine angew. Math. 77 (1874), 289-338** (EuDML doc/148241). Das oft verwechselte gleichjaehrige Paper "Ein Beitrag zur analytischen Zahlentheorie", J. reine angew. Math. **78** (1874), 46-62 (DOI 10.1515/crll.1874.78.46) ist eine andere Arbeit. Empfehlung: fuer Mertens-Typ-Produktschranken **Band 77, S. 289-338** zitieren.
(b) **Rosser-Schoenfeld -- BESTAETIGT.** J. B. Rosser, L. Schoenfeld, "Approximate formulas for some functions of prime numbers", Illinois J. Math. 6 (1962), no. 1, 64-94, DOI 10.1215/ijm/1255631807. Enthaelt explizite Mertens-/Chebyshev-Typ-Schranken (Standardquelle fuer explizite Konstanten).
(c) **Hardy-Wright -- teils UNVERIFIZIERT.** Verlagsdaten der 6. Auflage bestaetigt: G. H. Hardy, E. M. Wright, rev. D. R. Heath-Brown, J. Silverman, "An Introduction to the Theory of Numbers", 6. Aufl., Oxford University Press, 2008, ISBN 978-0-19-921986-5. Die exakte Theoremnummer fuer p_n ~ n*log n bzw. p_n = O(n*log n) konnte nicht aus einer abgerufenen Primaerquelle verifiziert werden -- die Chain-v1-Angabe "Thm 8 area" bleibt bis zur Sichtpruefung am Band offen (die scharfe Asymptotik steht im Kapitel ueber Groessenordnungen arithmetischer Funktionen, nicht im Anfangskapitel "The Series of Primes").
(d) **Bertrand-Postulat -- BESTAETIGT (Standardzuschreibung).** Bertrand-Vermutung 1845, Beweis Chebyshev 1852; stuetzt p_{nu+j} < 2^j*p_nu.

### Item 5 -- Cramer-Granville
Abgerufen: EuDML doc/205441; Wikipedia "Cramer's conjecture"; arXiv:1506.03359, 2605.23014; arXiv 2301.06095-Referenzliste; Springer/CMP (alle 2026-07-16).
(a) **H. Cramer, "On the order of magnitude of the difference between consecutive prime numbers", Acta Arithmetica 2 (1936), 23-46, DOI 10.4064/aa-2-1-23-46.** Explizit konjektuiert Cramer g_n = O((log p_n)^2); sein probabilistisches Modell stuetzt die staerkere Form limsup g_n/(log p_n)^2 = 1 (mit Wahrscheinlichkeit 1 im Modell). BESTAETIGT.
(b) **A. Granville, "Harald Cramer and the distribution of prime numbers", Scandinavian Actuarial Journal 1995, no. 1, 12-28.** Maiers Satz zeigt, dass das Cramer-Modell kurze Intervalle inadaequat beschreibt; Granvilles verfeinertes Modell (Beruecksichtigung Teilbarkeit durch kleine Primzahlen) legt limsup g_n/(log p_n)^2 >= 2*e^{-gamma} ~= 1.1229 nahe. BESTAETIGT.
(c) **"Cramer-Granville-Vermutung"** ist der etablierte Name fuer g_n = O((log p_n)^2) bzw. g_n <= c*(log p_n)^2 mit unspezifizierter Konstante c >= 1 (LeClair, arXiv:1506.03359: "The Cramer-Granville conjecture is an upper bound on prime gaps, g_n = p_{n+1}-p_n < c*log^2 p_n for some constant c >= 1"). Die Projekt-Hypothese B (es existieren C_g >= 1 und nu_B mit g_nu <= C_g*(ln p_nu)^2 fuer alle nu >= nu_B) ist eine getreue punktweise Wiedergabe. BESTAETIGT.
Montgomery-Soundararajan (aus Reviewer-Erinnerung) -- verifiziert per Springer/CMP: **H. L. Montgomery, K. Soundararajan, "Primes in Short Intervals", Commun. Math. Phys. 252 (2004), no. 1-3, 589-617, DOI 10.1007/s00220-004-1222-4.** Abstract verbatim: "Contrary to what would be predicted on the basis of Cramer's model ... the distribution of psi(x+H)-psi(x), for 0<=x<=N, is approximately normal with mean ~H and variance ~H*log(N/H), when N^delta <= H <= N^{1-delta}." (Momente/Sekundaerterme der singulaeren Reihe.) BESTAETIGT.

### Item 6 -- Erdos #251 Mapping + Seitenstatus
Abgerufen: erdosproblems.com/251 (via Suchindex, Live-Fetch bot-gesperrt); dedizierter Subagent (alle 2026-07-16).
- Problem #251 lautet exakt "Is [ sum_{n>=1} p_n/2^n ] irrational? (Here p_n is the nth prime.)". Referenzen: **[Er58b][ErGr80, p.62][Er88c, p.103]**. OEIS A098990. Problemseite zuletzt bearbeitet 28. Sept. 2025.
- [Er58b] = P. Erdos, "Sur certaines series a valeur irrationnelle", Enseign. Math. (2) 4 (1958), 93-100 (identisch mit ScPu11-Ref [2]). [Er88c] = Erdos 1988 (konjekturiert sum p_n^k/2^n irrational fuer alle k sowie sum p_n/(g_1***g_n) irrational unter Wachstumsbedingung g_n>=2, g_n=o(p_n)).
- **STATUS: OFFEN.** Die Seite fuehrt keine Loesung (weder partiell noch vollstaendig) und keine noch nicht eingearbeitete Kommentaraktivitaet.
- Forum-Thread /forum/thread/251: enthaelt 4 Beitraege, letzter von "Nat Sothanaphan". Die im Item beschriebenen Kommentare -- **Terence Tao** (~2025-10-07: Partielle Summation reduziert auf die Luecken-Reihe; eine hinreichend quantitative/uniforme Prime-k-Tupel-Vermutung ueber ~log log n aufeinanderfolgende Luecken gibt statistische Kontrolle; Shannon-Entropie als moegliches Werkzeug) und **"Alfaiz"** (~2026-04-15: Verweis auf Schlage-Puchta mit "Theorem 2 seems related") -- konnten wegen der Bot-Sperre NICHT woertlich verifiziert werden. UNVERIFIZIERT, aber plausibel (Tao ist auf Nachbar-Threads als Kommentator belegt; Alfaiz ist ein aktiver Literatur-Hinweisgeber auf der Plattform). Die beschriebene Reduktion ist konsistent mit Taos Methodik in verwandten Arbeiten (Abel-Summation -> Prime-Luecken -> uniforme HL-Tupel + Entropie).
- **KEINE neueren Entwicklungen**: keine Posts mit Loesungsanspruch, keine Statusaenderung, keine verlinkten Preprints nach 2026-04-15 bis 2026-07-16. #251 bleibt offen.

### Item 7 -- CPAP-3-Status
Abgerufen: arXiv:1311.7003 (BFTB); arXiv 1409.8361, 1410.8400; Wikipedia "Primes in arithmetic progression"; arXiv:1510.00743, 1408.6002 (CPAP-Liste offener Probleme); ams.org/mathnet.ru (FGKMT) (alle 2026-07-16).
- **D. K. L. Shiu, "Strings of congruent primes", J. London Math. Soc. (2) 61 (2000), no. 2, 359-373**: beweist beliebig lange Ketten aufeinanderfolgender Primzahlen, die alle kongruent a mod q sind -- NICHT gleiche Luecken.
- **W. D. Banks, T. Freiberg, C. L. Turnage-Butterbaugh, "Consecutive primes in tuples", Acta Arith. 167 (2015), no. 3, 261-266 (arXiv:1311.7003)**: leitet via Maynard-Tao die Unendlichkeit aufeinanderfolgender Primzahlen in konstanten Mustern (kongruent mod q) her. Die Methode ist in der Nachfolgeliteratur explizit als "restricted to constant patterns" charakterisiert; sie liefert KEINE unendlich vielen CPAP-3 (gleiche Luecken), sondern nur verwandte Restklassen-Aussagen.
- **J. Maynard, "Dense clusters of primes in subsets", Compositio Math. 152 (2016), no. 7, 1517-1554**: liefert dichte Cluster, aber kein CPAP-3.
- Kein 2016-2026-Resultat, das die CPAP-3-Unendlichkeit unbedingt entscheidet, gefunden. Die "CPAP-Vermutung" (fuer jedes k>2 unendlich viele k aufeinanderfolgende Primzahlen in AP) wird in der Literatur weiterhin als offenes Problem gefuehrt (arXiv:1510.00743: "CPAP conjecture - For every k > 2, there exist infinitely many sets of k consecutive primes in arithmetic progression").
- **VERDIKT: CPAP-3-Unendlichkeit ist per Juli 2026 OFFEN.** Die Projektannahme "still assumed open" ist bestaetigt.
- **Grosse-Luecken-Referenz**: K. Ford, B. Green, S. Konyagin, J. Maynard, T. Tao, "Long gaps between primes", **J. Amer. Math. Soc. 31 (2018), no. 1, 65-105, DOI 10.1090/jams/876** (arXiv:1412.5029). Schranke: max_{p_{n+1}<=X}(p_{n+1}-p_n) >> (log X)(log log X)(log log log log X)/(log log log X) fuer hinreichend grosse X. BESTAETIGT.

### Item 8 -- Pratt-Uniformitaet und Tao-Teravainen
Abgerufen: arxiv.org/abs/2409.15185 + HTML-Volltext; sciencedirect.com (JNT); erdosproblems.com/69; arxiv.org/html/2512.01739; terrytao.wordpress.com (alle 2026-07-16).
(a) **Kyle Pratt, "The irrationality of a prime factor series under a prime tuples conjecture", arXiv:2409.15185**, eingereicht 23. Sept. 2024; publiziert in **Journal of Number Theory 276 (2025), 270-285, DOI 10.1016/j.jnt.2025.02.010**. Resultat: unter einer "suitably uniform version of the prime k-tuples conjecture" ist sum_{n>=1} omega(n)/2^n irrational (settling conditionally a question of Erdos). omega(n) = Anzahl verschiedener Primteiler; die Reihe ist aequivalent zu sum_p 1/(2^p-1). **Uniformitaetsnutzung (praezisiert)**: Pratts Conjecture 1.2 ist eine quantitative HL-Tupel-Vermutung mit allgemeinen Linearformen L_k(n) = a_k*n + b_k, in der ausdruecklich Uniformitaet zugelassen wird (Zahl K der Formen und Koeffizientengroessen duerfen mit x wachsen). Pratt merkt an: "The statement of Conjecture 1.2 suffices for our present work, but could be refined further. There are various statements of a uniform prime tuples conjecture in the literature (e.g. [10, Conjecture 1.3]), but usually only in the case in which L_k(n) = n + b_k for each" -- d.h. Pratt laesst allgemeine Linearformen zu, waehrend die Literatur-Uniformitaet meist auf Verschiebungsformen n+b_k beschraenkt bleibt. Fuer die exakte numerische Fensterbreite empfiehlt sich eine Sichtpruefung des Conjecture-1.2-Wortlauts am Volltext.
(b) **Tao-Teravainen [TaTe25]: T. Tao, J. Teravainen, "Quantitative correlations and some problems on prime factors of consecutive integers", arXiv:2512.01739** (Dez. 2025). Beweist u.a. UNBEDINGT, dass sum_{n=1}^infinity omega(n)/2^n irrational ist ("Recently, Theorem 1.3 was shown conditionally on a form of the prime tuples conjecture in [46]; our result makes the irrationality unconditional"). Methode: probabilistische Methode + hochdimensionales Maynard-Typ-Sieb (fuer die Irrationalitaet); quantitative Zweipunkt-Korrelationen multiplikativer Funktionen unter Nutzung von Pilattes Arbeit (fuer die uebrigen Resultate). **Beschraenkung auf beschraenkte Numeratoren**: Die Maschinerie ist auf beschraenkte arithmetische Funktionen (omega(n)) zugeschnitten; die Autoren merken an, dass fuer schwierigere Faelle "there are no known techniques to unconditionally obtain asymptotics" und dass eine Abschwaechung der Hypothese "unlikely ... at our current level of understanding of analytic number theory" sei. Kein Transfer auf wachsende Numeratoren wie p_n -- hoch relevant fuer Item-0005.
(c) Die Reihe 1/(2^p-1) = sum omega(n)/2^n gehoert zu **Erdos-Problem #69** (Tao merkt an, es sei ein Spezialfall von #257). Status auf der Seite: bewiesen -- bedingt von Pratt [Pr24], unbedingt von Tao-Teravainen [TaTe25]. BESTAETIGT.

### Item 9 -- BET-06 Prior-Art-Sweep (der entscheidende Punkt)
Durchsuchte Basis (alle 2026-07-16): arXiv math.NT-Listen und Volltextsuche (irrationality, p_n/2^n, prime tuples irrationality, Erdos problem 251, prime binary digits); Google-/Websuche; Terry Taos Blog (terrytao.wordpress.com); Teravainen-Profil; zitierende Arbeiten von Pratt und Tao-Teravainen; erdosproblems.com/251 und Forum-Thread 251; Kuperberg-, Gallagher-, Cramer-Granville-Literatur.
(a) **Zielimplikation** (uniforme HL-Tupel + evtl. Cramer-Typ-Luecken ==> Irrationalitaet von sum p_n/2^n): **NOT-FOUND.** Kein Journalpaper, kein arXiv-Preprint, kein Blog/Forum-Beitrag, keine Seminarfolien mit dieser Implikation oder etwas materiell Aequivalentem.
(b) **Staerkeres** (unbedingter Beweis von sum p_n/2^n irrational ==> Loesung #251; oder dieselbe Implikation unter schwaecheren Hypothesen): **NOT-FOUND.** #251 offen; Problemseite fuehrt keine Loesung.
(c) **Nahe Varianten**: Pratt (2024/2025) und Tao-Teravainen (2025) behandeln omega(n) (beschraenkt), nicht p_n. Kaneko-Suzuki-Tachiya (arXiv:2601.20743) behandeln sparse Reihen d(n)^k/t^{sigma(n)} etc., nicht p_n/2^n. arXiv:2505.06242 ("Hoelder continuity of an alternating Erdos series on prime k-tuples") betrifft die alternierende Reihe n/p_n, nicht #251. Keine Variante deckt wachsendes arithmetisches f = p_n / sum p_n/b^n fuer andere Basen ab.
Zeitfenster **Okt. 2025 (Taos Forum-Kommentar) bis 2026-07-16**: Niemand hat Taos Idee oeffentlich ausgefuehrt; kein Preprint, kein Loesungsanspruch.
**VERDIKT BET-06 = NEIN** (die Implikation existiert NICHT in der Literatur). Evidenzinventar: (i) #251 dokumentiert offen mit 4 Forum-Posts, kein Loesungsanspruch; (ii) arXiv-Voll-/Listensuche ohne Treffer fuer die Implikation; (iii) die einzigen thematisch nahen Resultate (Pratt, Tao-Teravainen) betreffen beschraenkte omega(n) und aeussern explizit, dass wachsende Numeratoren ausserhalb der aktuellen Technik liegen; (iv) Taos Forum-Kommentar (falls, wie angenommen, vorhanden) ist eine Skizze, kein Beweis.

### Item 10 -- Geschlossenes Item (nur Erwaehnung)
Mathlib-Namen Nat.nth, Nat.count, Mathlib.Data.Real.Irrational sind vom Projekt empirisch in-tree bestaetigt; keine Web-Verifikation erforderlich. GESCHLOSSEN.

## Recommendations
1. **BET-06 als NEIN aufloesen (Ledger-Eintrag).** Die Zielimplikation existiert nicht in der Literatur; die oeffentliche Nische ist offen. Schwellenwert fuer Umkehr: Auftauchen eines arXiv-Preprints oder Forum-/Blog-Beitrags, der (uniforme HL) + (Cramer-Typ) ==> Irrationalitaet von sum p_n/2^n aussagt, oder ein unbedingter #251-Beweis. Konkret: automatisierten Alert auf arXiv math.NT (Stichworte irrationality + prime + 2^n) und auf erdosproblems.com/251 einrichten.
2. **Zitat-Korrekturen in dossier/chain-v1.md und dissektion.md**: (a) ScPu11 als ein Paper fuehren (Acta Arith. 126 (2007) 295-303 = arXiv:1105.1451, DOI 10.4064/aa126-4-1); Anachronismus-Flag entfernen. (b) Mertens-Zitat auf J. reine angew. Math. **77** (1874) 289-338 umstellen (nicht 78, 46-62). (c) Kuperberg-Zitat mit Journalpublikation vervollstaendigen (Quart. J. Math. 74 (2023) 1457-1479, DOI 10.1093/qmath/haad030). (d) Hardy-Wright-Theoremnummer am physischen Band (6. Aufl., 2008) verifizieren, bevor "Thm 8" als endgueltig markiert wird.
3. **Flag-Uebergaenge**: Alle in diesem Bericht als BESTAETIGT markierten Zitate koennen von UNVERIFIED auf VERIFIED gesetzt werden. Als UNVERIFIED zu belassen: (i) exakter Wortlaut der Tao-/Alfaiz-Forum-Kommentare zu #251; (ii) exakte Hardy-Wright-Theoremnummer; (iii) praezise numerische Uniformitaets-/Fensterschranke aus Pratts Conjecture 1.2.
4. **Fuer Item-0005** (Transfer auf wachsende Numeratoren) die explizite Limitierungsbemerkung von Tao-Teravainen (arXiv:2512.01739) als Motivation zitieren: aktuelle Technik erreicht wachsende Numeratoren nicht unbedingt.

## Projekt-relevante Warnflaggen (prominent)
- (i) **CPAP-3-Unendlichkeit ist NICHT bewiesen** -- bleibt offen; keine Aenderung an Projektannahmen noetig.
- (ii) **ScPu11-Identifikatoren erfordern KEINE Korrektur der Substanz** (Zitat war korrekt), aber der Anachronismus-Flag ist zu entfernen; ScPu11 ist ein einziges Paper (2007 = arXiv 2011).
- (iii) **Kein Prior-Art fuer die Zielimplikation** -- die zentrale Voraussetzung fuer einen oeffentlichen Anspruch (BET-06) ist erfuellt (Nische frei).
- (iv) **Keine Statusaenderung an Erdos #251** -- weiterhin OFFEN per 2026-07-16.

## Caveats
- Die erdosproblems.com-Seiten (Problem 251 und Forum-Thread 251) sind bot-gesperrt; Problemwortlaut, Referenzen und Offen-Status wurden ueber Suchindex und einen dedizierten Subagenten bestaetigt, aber die zwei spezifischen Forum-Kommentare (Tao 2025-10-07, Alfaiz 2026-04-15) konnten nicht woertlich abgerufen werden. Sie bleiben UNVERIFIZIERT (plausibel). Eine manuelle, im Browser durchgefuehrte Sichtpruefung der Thread-Seite wird empfohlen, um diese beiden Kommentare zu zitieren.
- MathSciNet/zbMATH waren nicht direkt zugaenglich; Bibliographie wurde ueber Verlags-/EuDML-/Project-Euclid-/arXiv-/Oxford-Academic-Primaerseiten verifiziert.
- Bertrand-Postulat und die Hardy-Wright-Groessenordnung wurden nicht aus abgerufenen Primaerbaenden, sondern aus Standard-Sekundaerquellen bewertet; die exakte Hardy-Wright-Theoremnummer bleibt offen.

---

## Addendum: forum thread 251 verbatims (operator browser check, 2026-07-16)

Provenance: the report's caveat "bot-gesperrt / UNVERIFIZIERT" for the
two forum comments is RESOLVED by an operator manual browser read of
https://www.erdosproblems.com/forum/thread/251 on 2026-07-16
(screenshot operator-held, sha256
7150f5b265f77a2438efce9c9a96f76fef7c23d4f1d3432f9176c4571ab06d35).
Mathematics transcribed in LaTeX tokens; bracketed [phrases] were
hyperlinks whose targets the screenshot does not capture.

Page state: "0 claimed proofs for this problem". Likes: ebarschkis,
Prasannam, qrdl, jizert. Interested in collaborating / currently
working / looks difficult / looks tractable / could be formalisable /
working on formalising: all None. Recommended citation format shown on
page: "T. F. Bloom, Erdos Problem #251,
https://www.erdosproblems.com/251, accessed 2026-07-16". Footer:
comments are user responsibility, not verified for correctness.

All four posts, oldest first:

1. TerenceTao -- 17:17 on 07 Oct 2025 (VERIFIED verbatim; report item 6
   assumed content confirmed exactly):
   "By summation by parts, this is equivalent to the irrationality of
   \sum_n \frac{p_{n+1}-p_n}{2^n}. It is possible that a sufficiently
   quantitative and uniform version of the prime tuples conjecture can
   resolve this problem, if it gives sufficient statistical control on
   the binary expansion of about \log\log n consecutive prime gaps
   p_{n+1}-p_n (which is usually of size \asymp \log n) to show that
   the binary expansion of \sum_n \frac{p_{n+1}-p_n}{2^n} cannot be
   periodic. The theory of Shannon entropy may be helpful in this
   regard."

2. Alfaiz -- 03:28 on 15 Apr 2026 (VERIFIED verbatim):
   "[ScPu11] by D. C. Schlage Puchta seems related to this problem.
   (See Theorem 2)."
   Note: the forum initials "D. C." are wrong; the paper's author is
   J.-C. (Jan-Christoph) Schlage-Puchta. The [ScPu11] pairing with
   arXiv:1105.1451 = Acta Arith. 126 (2007) 295-303 stands (report
   item 1).

3. Vjeko_Kovac -- 11:13 on 15 Apr 2026 (the BET-01 variant solution,
   now verbatim; red-bordered as recent):
   "The last conjecture below the main problem statement has an
   (overly simple) negative answer. The idea is elementary, just make
   the series telescope by choosing positive integers (c_n) such that
   \frac{p_n}{g_1 \cdots g_n} = \frac{c_n}{g_1 \cdots g_{n-1}} -
   \frac{c_{n+1}}{g_1 \cdots g_n}, i.e. c_{n+1} = c_n g_n - p_n.
   Thus, one can define (c_n) recursively, by only making sure that
   c_{n+1} \equiv -p_n \pmod{c_n} and that it is bounded from below
   by something that grows slowly but steadily. Afterwards one just
   sets g_n := \frac{c_{n+1} + p_n}{c_n}. I got ChatGPT 5.4 Pro
   [figure out the proof] and [write up the details] with only minimal
   orchestration from my side. It is possible that Erdos also wanted
   (g_n) to be increasing, but then it would be weird to emphasize
   g_n \geq 2 and switch the notation from a_n to g_n for this
   particular problem in [Er88c]."

4. Nat Sothanaphan -- 17:06 on 15 Apr 2026 (reply to 3; red-bordered):
   "Thanks! I ran standard [check] which found no issues. It seems
   this proof is a bit stronger than g_n = o(p_n). It may be of
   interest to see what the best provable statement is."

Steering verification note: the telescoping identity and a numeric
instance were re-executed (c = 2, 4, 5, 10, 13 gives g = 3, 2, 3, 2,
all >= 2, and the partial sum \sum_{n<=4} p_n/(g_1...g_n) = 59/36 =
c_1 - c_5/(g_1 g_2 g_3 g_4) exactly); with c_n -> infinity slowly the
series equals c_1 and g_n ~ p_n/c_n = o(p_n), so the [Er88c]
generalized-denominator conjecture fails as stated -- consistent with
the ledger's BET-01 outcome H2 (adversarial telescoping) and the
project dissection. New meta-fact on record: the write-up of this
negative answer was produced by an LLM (ChatGPT 5.4 Pro) under
"minimal orchestration" -- AI-assisted mathematics is already on this
thread.
