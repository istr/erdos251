# item-0026 extraction and directory-update: executor session report

Lane: EXECUTOR (local, Claude Code). Dispatch: `dispatch-item-0026-extract-v1.md`
(ephemeral, uncommitted). Session date: 2026-07-25. Operator: istr.
No commit, no push (Section 8): steering authors the ledger entry post-run.

## 1. Section 0 pin and rule-18 delta

Section 0 pin: `e368159c04aebc3d6941717ba289bcc64da77f52`.

At session start `HEAD` equalled the pin exactly, so `git diff <pin>..HEAD`
is empty -- no delta at all, hence trivially no content-path delta
(rule 18 satisfied; session pins to HEAD = the Section 0 pin). Steering's
authoring-time claim was independently confirmed:

```
git diff --stat 2c59f4e4f1f2643c1049e8b0d15ab6d12a9a5cde..e368159c04aebc3d6941717ba289bcc64da77f52
 payloads/HASHES.txt | 7 +++++++
 1 file changed, 7 insertions(+)
```

So the pin differs from `2c59f4e` by exactly seven insertions in
`payloads/HASHES.txt` (the seven new anchors) and nothing else.

## 2. sha256 verification of the seven anchors (Section 2)

Each local PDF under `dossier/` was hashed and matched against the value
booked in `payloads/HASHES.txt` at the pin (keyed there by the
`https://arxiv.org/pdf/<id>` URL). All seven verified before any reading:

| # | anchor | sha256 (booked = computed) | verified |
| --- | --- | --- | --- |
| 1 | 2009.05760v1 | 0a3d4a99...c66977 | OK |
| 2 | 2207.05038v2 | 93aa865f...67380d | OK |
| 3 | 1510.06005v2 | 05cc130e...9a52ddb | OK |
| 4 | 2012.11565v3 | 676ac2ce...f007d (676ac2ceafc1550d...) | OK |
| 5 | 2605.23014v1 | ccf3f21a...b0c551 | OK |
| 6 | 2407.05380v2 | 019b27fd...06e890 | OK |
| 7 | 2401.04000v4 | bbc3bf47...a20c31 | OK |

Full values are recorded in `dossier/literature.md` Addendum 3 and were
re-cross-checked against `payloads/HASHES.txt` at close (7/7 match).

## 3. Gate lines (Section 6), verbatim

Run at session start and again at close; identical both times except where
noted.

```
check-frozen:
  OK   erdos_251_irrational               lean/Erdos251/Statement.lean:18
  OK   HLQuantA                           lean/Erdos251/Hypotheses.lean:199
  OK   CramerGranville                    lean/Erdos251/Hypotheses.lean:210
FROZEN BLOCKS: all byte-identical.

relocation-check:
RELOCATION CHECK PASSED -- concatenation is byte-identical to the old body.

sorry census (grep 'sorry' over lean/Erdos251/*.lean, comment lines removed):
  Statement.lean:8   prose in docstring ("answer(sorry)")
  Statement.lean:21  THE one proof-term sorry
  Counting.lean:13   prose in docstring ("intentional, named `sorry`s")
  Counting.lean:90   prose in docstring ("sorry inventory ... unchanged")
  => exactly one proof-term sorry, at lean/Erdos251/Statement.lean:21.

mathlib pin a6276f4c6097675b1cf5ebd49b1146b735f38c02 in lake-manifest.json: 1 occurrence (intact).
lean-toolchain ends with a single trailing newline: True.
roadmap/item-0026.md: status: ratified.
```

All gates pass unchanged. Zero edits were made under `lean/`; no `lake`
invocation; no roadmap edit; no ledger edit.

## 4. Per-paper delivery (all seven delivered; independent verify CONFIRMED)

Extraction ran as a local multi-agent workflow: one extraction agent per
PDF (web OFF; single verified PDF as the only evidence base), each followed
by an independent adversarial fidelity verifier (front matter, sampled
verbatim quotes vs the PDF, mandatory statements, NOT-FOUND probes,
no-strengthening, per-axis verdict). 14 agents, 0 errors.

| # | tier | anchor | extract file | KB | front matter | verify | quotes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 1 | 2009.05760v1 | dlbf20-moments.md | 38.9 | match | CONFIRMED | 15/15 |
| 2 | 1 | 2207.05038v2 | mt22-almostprimes2.md | 41.2 | match | CONFIRMED | 30/30 |
| 3 | 1 | 1510.06005v2 | tera15-almostprimes.md | 33.2 | match | CONFIRMED | 16/16 |
| 4 | 2 | 2012.11565v3 | matomaki20-veryshort.md | 32.9 | match | CONFIRMED | 18/18 |
| 5 | 2 | 2605.23014v1 | jha26-poissontail.md | 40.9 | match | CONFIRMED | 20/20 |
| 6 | 3 | 2407.05380v2 | leung24-pseudorandom.md | 34.4 | match | CONFIRMED | 25/25 |
| 7 | 3 | 2401.04000v4 | leung24-jointdist.md | 39.1 | match | CONFIRMED | 16/16 |

All three tiers delivered complete (not a scattered partial). All seven
front matters confirmed against the PDFs with no author or title deviation.
Row 7 author, left by steering to be read, is Sun-Kai Leung (Universite de
Montreal); the filename `leung24-jointdist.md` is therefore correct and was
kept.

## 5. Consolidated per-axis verdict (across all delivered papers)

Axes: A1 rank, A2 window, A3 grain (consecutive-gap-word class masses
$`N_{P,d}`$), A4 direction (upper/non-concentration), A5 strength
(constant order suffices), A6 density (sparse scales). A1-A4 not relaxed by
CG; A5, A6 relaxed.

| anchor | A1 | A2 | A3 | A4 | A5 | A6 | even-Cramer | clears all 6 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 2009.05760 | FAILS | FAILS | FAILS | CLEARS | CLEARS | CLEARS | untested | no |
| 2207.05038 | FAILS | FAILS | FAILS | CLEARS(form) | CLEARS | CLEARS | untested | no |
| 1510.06005 | FAILS | CLEARS | FAILS | CLEARS | CLEARS | CLEARS | untested | no |
| 2012.11565 | FAILS | CLEARS | FAILS | FAILS | CLEARS | CLEARS | untested | no |
| 2605.23014 | CLEARS | CLEARS | FAILS | CLEARS(caveat) | CLEARS | CLEARS | untested | no |
| 2407.05380 | FAILS | FAILS | FAILS | FAILS | CLEARS(vac) | CLEARS(vac) | untested | no |
| 2401.04000 | FAILS | FAILS | FAILS | CLEARS(form) | CLEARS | CLEARS | untested | no |

Structural fact for steering (stated as a located absence, not a verdict):
**A3 FAILS for all seven.** No delivered result carries the
consecutive-gap-word class-mass grain; the one paper reaching the target
rank-and-window jointly (2605.23014, conditionally) still fails A3, and the
unconditional papers fail A1 and/or A2 as well as A3. Every "even-Cramer"
cell is `untested` (each paper is silent on the deterministic gap system;
untested was accepted, guesses were not).

## 6. STOP-AND-REPORT adjudication (Section 7): none triggered

- 7.1 rule-18 content-path delta: no (empty delta).
- 7.2 sha256 mismatch: no (7/7 verified).
- 7.3 front-matter contradiction: no (all seven match; row-7 author read
  and consistent).
- 7.4 gate failure: no (all Section 6 gates pass; the mapper is not a
  Section 6 gate -- see Section 8 below).
- 7.5 unquotable mandatory statement: no (every mandatory display was
  transcribed; several from page images where pdftotext scrambled them).
- 7.6 references.md un-editable without a sources.yml change: no (see
  Section 8).
- 7.7 a candidate clears all six axes: **no** -- none clears all six, so no
  located carrier; the item-0010 campaign state is unchanged by this
  delivery.

## 7. Directory updates and rule-19 governing quotes

Every description asserted about a paper was authored from its extract (or,
for the two corrections, from the pre-existing extract named by the
dispatch), with the governing sentence quoted here.

### 7.1 writeup/references.md -- Section 2 additions (2009.05760, 2605.23014, 2407.05380, 2401.04000)

- 2009.05760 governing quote (dlbf20-moments.md, abstract p. 1): "We
  establish lower bounds for all weighted even moments of primes up to X in
  intervals which are in agreement with a conjecture of Montgomery and
  Soundararajan. Our bounds hold unconditionally for an unbounded set of
  values of X, and hold for all X under the Riemann Hypothesis. We also
  deduce new unconditional Omega-results for the classical prime counting
  function."
- 2605.23014 governing quote (jha26-poissontail.md, abstract p. 1): "For
  slowly growing lambda, and conditional on a strong variant of the
  Hardy-Littlewood conjectures, we establish asymptotics ... we identify a
  phase transition and explore the breakdown of these distributions for
  larger lambda, capturing the precise deviations when lambda grows slower
  than any fixed power of log x."
- 2407.05380 governing quote (leung24-pseudorandom.md, abstract p. 1):
  "Assuming a q-variant of the prime k-tuple conjecture uniformly, we
  compute mixed moments of the number of primes in disjoint short intervals
  and progressions ... we establish the convergence of both sequences of
  suitably normalized primes to a standard Poisson point process."
- 2401.04000 governing quote (leung24-jointdist.md, abstract p. 1):
  "Assuming the Riemann hypothesis (RH) and the linear independence
  conjecture (LI), we show that the weighted count of primes in multiple
  short intervals follows a multivariate Gaussian distribution with weak
  negative correlations. As an application ... a sharp phase transition:
  biased races ... once the number of intervals exceeds an explicit
  critical threshold."

### 7.2 writeup/references.md -- new Section 4 "Almost primes at logarithmic window scales" (1510.06005, 2012.11565, 2207.05038)

The new section was placed after Section 3 and before the old Section 4,
which was renumbered to 5 (and old Section 5 to 6). Each description names
the object (E_2, E_3, P_2) and the window, since the object is the axis
(A3) on which this line misses.

- 1510.06005 governing quote (tera15-almostprimes.md, abstract p. 1): "We
  show that almost all intervals [x, x + log^{1+eps} x] contain E3 numbers,
  and almost all intervals [x, x + log^{3.51} x] contain E2 numbers. ... We
  also consider general Ek numbers, and find them on intervals whose
  lengths approach log x as k -> infinity."
- 2012.11565 governing quote (matomaki20-veryshort.md, abstract p. 1): "We
  show that as soon as h -> infinity with X -> infinity, almost all
  intervals (x - h log X, x] with x in (X/2, X] contain a product of at
  most two primes. In the proof we use Richert's weighted sieve, with the
  arithmetic information eventually coming from results of Deshouillers and
  Iwaniec on averages of Kloosterman sums."
- 2207.05038 governing quote (mt22-almostprimes2.md, abstract p. 1): "We
  show that, for almost all x, the interval (x, x + (log x)2.1 ] contains
  products of exactly two primes. ... we prove a new type II estimate. One
  of the new innovations is to use Heath-Brown's mean value theorem for
  sparse Dirichlet polynomials."

### 7.3 writeup/references.md -- descriptive correction, Pintz 1004.1084

Authored from `dossier/item-0017-workpapers/extract/pintz10-singser.md`.
Governing displays (verbatim from that extract):

- Object, (1.4): "S_calH(H) := (1/H) sum_{h=1}^{H} S(calH cup {h})/S(calH)".
- Two-sided, Theorem 1 (1.6): "S_calH(H) = 1 + O(eps) if H >= exp(k^{1/eps})".
- Lower-bound-only, Theorem 1' (1.8): "S_calH(H) >= c_1 if H >= exp(c_2 k/log k)"
  (and (1.7): ">= 1 + O(eps) if H >= exp((1/eps) k/log k)").

The corrected sentence records the quantitative shape (the h-averaged
relative one-position extension quotient, a two-sided form and a
lower-bound-only form carrying different span thresholds in the tuple
dimension k), and keeps the induction-to-Gallagher clause.

### 7.4 writeup/references.md -- descriptive correction, Kuperberg 2210.09775

Authored from `dossier/item-0017-workpapers/extract/kuperberg22-singseries.md`
Section 8. Governing quotes (verbatim from that extract):

- Restricted-rank asymptotic, Theorem 1.1: "Fix delta > 1/2, and let h, k
  in N with k = O((log h)^{1-delta}). ... T_k(h) = h^k + O(h^{k-beta})."
- The added content, Theorem 1.2: "Let k, h in N, with no conditions on
  their relative growth rates. Define T_k(h) by (4). Then (5) T_k(h) << h^k
  prod_{p <= k^3} 1/(1 - 1/p)^k << h^k (3 log k)^k." Section 8 barrier
  paragraph frames it: "Theorem 1.2 provides a bound that is uniform in h on
  the average value of k-term singular series."

The correction adds (does not replace) the Theorem 1.2 bound that holds
with no condition on the relative growth of the rank and the window.

### 7.5 dossier/literature.md -- Addendum 3

Appended after a `---` rule, following the established addendum pattern;
the report body, TL;DR, Key Findings, and the two existing addenda are
untouched (diff: +76, -0). It registers the seven anchors (identifier,
author, title, venue = arXiv preprint, sha256 as booked, extract file),
states the item-0026 literature-grain verdict as the located A3 absence
(not a blanket "absent from corpus"), points to the two run outputs as the
search record (with the ChatGPT run flagged as a translation of an
unretained German report carrying no verbatim anchors -- a lead list, not a
citable object), and records no verdict on any candidate. Language boundary
noted at the head; ASCII-only throughout (verified). The seven sha256 were
re-cross-checked against `payloads/HASHES.txt`: 7/7 match.

## 8. Mapper check (Section 5.2) -- pre-existing failure, reported not repaired

`python3 scripts/writeup_mapper.py check --manifest writeup/sources.yml`,
run before and after the edits, returns identically:

```
FAIL: entry chain-main: target heading is missing
```

This is a **pre-existing** failure, unrelated to this session: entry
`chain-main` expects target heading `## The conditional result` in
`writeup/status.md`, which is absent at the pin. `writeup/status.md` is
outside this dispatch's scope and was not touched. Per Section 5.2 the
discrepancy is reported and NOT repaired (an unrelated repair inside a
directory-update change is exactly the coupling the dispatch forbids).

Two further mapper facts, reported not repaired:

1. **references.md needs no sources.yml change (Section 7.6 not
   triggered).** The mapper binds section-level `<!-- sources: ... -->`
   comment ids and per-entry source blobs; it does not tie individual
   reference bullets to sources. The edits add no new source comment and
   change no source id, so `references.md` was editable as-is. Separately,
   the `## External literature` comment names five ids
   (`literature-problem`, `literature-schlage`, `literature-prime-tuples`,
   `literature-prime-gaps`, `literature-standard-estimates`) while
   `sources.yml` defines only the first two; this 5-vs-2 discrepancy is
   pre-existing and is masked only because the run fails earlier at
   `chain-main`.
2. **literature.md source-blob drift (consequence of the instructed
   Addendum 3 append).** `sources.yml` pins `literature.md` at blob
   `8d00aaed4b0e1f96a80f8c8fa8a107bf6835afd5` for entries
   `literature-problem`/`literature-schlage`. Appending Addendum 3 (Section
   5.1) drifts it to `010a376453be0699438a8eda8cb32979150e735b`. Were the
   earlier `chain-main` failure resolved, this would surface as a
   `source drift` error for those two entries. It is a direct consequence
   of the dispatch-instructed edit; per Section 5.2 `sources.yml` is not
   modified here. Steering decides whether to re-pin the blob.

## 9. Budget (Section 9, rule 15): actuals vs estimate

| tier | anchor | est. pages | actual pages | est. size | actual KB |
| --- | --- | --- | --- | --- | --- |
| 1 | 2009.05760 | 17 | 15 | 25-50 | 38.9 |
| 1 | 2207.05038 | 25 | 26 | 25-50 | 41.2 |
| 1 | 1510.06005 | 20 | **40** | 25-50 | 33.2 |
| 2 | 2012.11565 | 25 | 31 | 25-50 | 32.9 |
| 2 | 2605.23014 | unknown | 29 | 25-50 | 40.9 |
| 3 | 2407.05380 | unknown | 13 | 20-40 | 34.4 |
| 3 | 2401.04000 | unknown | 43 | 20-40 | 39.1 |

Two page-count deviations from Section 9: `1510.06005` is 40 pages (est.
20) and `2401.04000` is 43 pages (est. unknown, now recorded). All extract
sizes landed inside the 20-50 KB envelope. All three tiers were delivered in
one session (parallel local extraction), so the "tier-1-only fallback" was
not needed.

## 10. Deviations and flags (consolidated)

- **2009.05760 date oddity** (dlbf20 flag 1, no bearing on identity): the
  arXiv side-stamp on p. 1 reads "12 Sep 2020" while the paper's own footer
  and the PDF CreationDate read "15 Sep 2020".
- **Image-layer transcription**: across papers, theorem/equation displays
  that `pdftotext` scrambled (stacked exponents, singular-series products,
  Corollary ranges) were transcribed from 200-dpi `pdftoppm` page renders
  and flagged `[TRANSCRIPTION-UNSURE, resolved-by-image]`; each extract's
  FLAGS records which layer each hard display came from (method note per
  `mangerel.md`).
- **Verifier minor notes**: each independent verifier returned CONFIRMED
  with an empty high-severity list; the only entries were LOW/editorial
  (e.g. a paraphrase gloss, a NOT-FOUND note's location wording). No
  strengthening was found in any extract.

## 11. Process findings (workflow lane hygiene; not evidence-integrity)

1. The `leung24-jointdist` extraction agent left two `pdftotext` scratch
   dumps (`scratch_layout.txt`, `scratch_raw.txt`, of `2401.04000v4.pdf`)
   at the repo root instead of a temp dir. They are re-derivable, not
   evidence; the executor removed them. Recommendation for future
   dispatches: instruct agents to scratch under the session scratch dir.
2. An extraction agent moved the pre-existing operator file
   `dossier/item-0026-workpapers/item-0026-literature-consolidation-v1.md`
   to the repo root (content unchanged: same size and mtime, i.e. `mv`, not
   a rewrite). The agents had been told not to touch it. The operator
   catered for the file; the executor did not delete it. Recommendation:
   constrain agent write/move scope to the single output path.

Neither finding affected any extract or directory-update content.

## 12. Session file list (Section 8 outputs)

New (untracked):
- dossier/item-0026-workpapers/extract/dlbf20-moments.md
- dossier/item-0026-workpapers/extract/mt22-almostprimes2.md
- dossier/item-0026-workpapers/extract/tera15-almostprimes.md
- dossier/item-0026-workpapers/extract/matomaki20-veryshort.md
- dossier/item-0026-workpapers/extract/jha26-poissontail.md
- dossier/item-0026-workpapers/extract/leung24-pseudorandom.md
- dossier/item-0026-workpapers/extract/leung24-jointdist.md
- dossier/item-0026-workpapers/extraction-report.md (this file)

Modified (tracked):
- dossier/literature.md (Addendum 3 append; +76, -0)
- writeup/references.md (Section 2 adds, new Section 4 + renumber, Pintz and
  Kuperberg corrections; +14, -4)

`git diff --stat` at close shows only the two tracked files above; the only
untracked path is `dossier/item-0026-workpapers/`. Nothing outside the lane.

## 13. Scope note

No verdict on the S1 carrier question is recorded anywhere in this delivery.
Pricing the seven candidates against the six axes and deciding S1 is a
separate steering task after delivery. The executor commits and pushes
nothing; steering authors the ledger entry post-run.
