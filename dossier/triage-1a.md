# Steering triage: stage 1a runs (CONTAMINATION CLASS C+)

QUARANTINE: this file synthesizes across 1a runs. It must NOT enter any
remaining stage-1a run (Gemini slot still OPEN) nor any blind review of a 1a
output. It feeds only the 1b briefing extension and steering.

Date: 2026-07-12. Author: steering (Claude Fable 5). Verification level:
every "verified" claim below was independently re-derived or spot-checked by
steering; middle sections of ab2 (fork-merge proof, countermodel mechanics)
were additionally read verbatim.

## 0. Run registry

| run_id | model | dur | turns | lang | output sha256 |
|---|---|---|---|---|---|
| 20260712_fable5_1a_item0001 | fable-5 (Anthropic, incognito) | ~79 min | 3 (2x turn limit, consolidation) | en | 5460a5bb...a6998 |
| 20260712_gpt56sol_1a_ab1 | gpt-5.6-sol (OpenAI, A/B var. 1) | 9m07s | 1 | de (Lean layer en) | 060dab2b...e56213 |
| 20260712_gpt56sol_1a_ab2 | gpt-5.6-sol (OpenAI, A/B var. 2) | 12m15s | 1 | en | 0536487183...5f073e |

Fable traces: turn-1-2 sha 801abb86...137a24 (referenced by the report
itself), turn-3 sha ea0eb57d...bacdd0. Payload byte-identity confirmed by
three independent sha256 computations (steering, fable5 in-run, gpt56sol
in-run): 482f56ab...a78fce.

Shared GPT wrapper (verbatim, German): "Bitte einmal die angehaengte Datei
lesen. Die sha256-Summe berechnen und ausgeben. Die Anweisungen exakt
ausfuehren. Recherche und Websuche sind ausgeschaltet. Das Ergebnis als
Markdown-Datei praesentieren. Das ist eine 0-Temperature, 1-Turn Aufgabe.
Keine Nachfragen." Sampling: temp 0 requested, NOT enforceable on the
consumer surface; record as such. Use the identical wrapper for the Gemini
run. Contamination audits: clean on all three (no class-C markers; all
"Tao" hits are theorem names, LIT-flagged).

## 1. Per-run verdicts (compact)

fable5: verified C13 primorial obstruction (steering re-derivation), C14
spot checks, C7 parity (b*delta in 2Z for n >= s+1), C5 doubling-map
dictionary, Theorems A/B/C logic, C20 dyadic route, C9/C10 delta lower
bounds (method plausible, computer-assisted), C11 J=1 refutation. Corrected
the dossier (ERRATUM-1/2). Unique: primorial, parity, two-window/H-sep,
dyadic delta<4, numerics layer (finite exclusions: denominator > 10^298;
S != a/(2^s b) for s <= 1,857,459, odd b <= 99,999 -- finite, correctly
labelled). Miss: none structural; trace propagated an unverified 15.6
estimate later corrected in the report (Q5 fidelity datum).

gpt56sol-ab1: verified C4/C5 v2-block lower bound (b odd preserves
valuation; positive integer in residue class => >= 2^t), C6/C7 word
fixpoint alpha_w = B_w/(2^r - 1) and lattice distance 1/(b q_w), C8
conditional theorem (q_k -> infty beats any fixed b), C9/C10 rationalization
no-go (independent second derivation of the statistics vacuity). Unique:
v2-block route, word-power route, the observation that constant words have
q_w = 1 (why equal runs are the degenerate anti-concentration case).
Miss: parity refinement (factor 2 available in (13)/(14)); no numerics;
word admissibility calculus implicit (steering note: K ~ 3 repeats of a
word of length r ~ log2 log p satisfy (16), and small K evades the
primorial coverage argument entirely -- runs were the r=1, K large extreme).

gpt56sol-ab2: verified C1-C7 including exact-locking (C7), fork-merge C4/C5
(proof read verbatim: C3 forces D0 = 0, the fork supplies D1 = a'-a != 0
combinatorially, the suffix doubles K times, (5.11) bH < 2^J and H < 2^K
closes; b enters ONLY the prefix condition), C6 gap-theoretic corollary
shape (tail estimate reconstructed), countermodel C8 (transition-gap
mechanics and sum = 7 re-derived; states x_n = current gap, transitions
g = 2 c_k - c_{k+1}). Unique: fork-merge, exact-locking theorem, the
countermodel (rational, gaps Theta(log n), arbitrarily long runs with
lcm(1..J+1)-divisible difference, squeeze mute). Miss: parity; no numerics;
C10 abundance heuristic honestly rated 0.35.

## 2. Route landscape after 1a (hypothesis demands on actual primes)

| route | demands | b enters via | exact-hit risk | source |
|---|---|---|---|---|
| A: (P)/L-star | equal run + 0 < \|delta-c\| < eps | threshold eps ~ 1/b | eliminated by 0< clause | fable5 |
| C: H-sep | pattern repeat + 0 < \|diff\| < 2^{J+1}/b | threshold | needs 0< | fable5 |
| E: v2-blocks | ONE pattern with v2(code) >= log2 log p + w(1) | b*delta >= 2^t vs delta size | none | ab1 |
| F: word-powers | ~3 adjacent repeats of growing word, q_w -> infty | q_k > b eventually | none | ab1 |
| G: fork-merge | twin occurrence W a V / W a' V, \|W\|,\|V\| >~ log2 log p | prefix only (2^J/b) | none | ab2 |

All five sit on the same loglog window budget. E, F, G are existence-only.
Current weakest-hypothesis favorite: G (no anti-concentration, no
denominator arithmetic beyond the prefix threshold, directly Lean-shaped in
ab2 section 8.4). Parity uplift (fable5 C7) sharpens the thresholds of
A, C, E, G by a factor 2 -- cross-pollination item for 1b.

## 3. Cross-run syntheses

1. ERRATUM-3 (see dossier/errata.md): runde0's Lemma L retracted -- ab2's
   countermodel shows exact locking is a real escape and refutes the
   maximal-run fix; fable5's (L*)/(P) had silently repaired it via the
   strict-positivity clause; G needs no such clause at all.
2. The statistics/growth no-go is now independently proved twice (fable5 C8
   steering construction with PNT-grade statistics; ab1 C9/C10 perturbation
   coding with parity and monotonicity preserved). First replicated theorem
   of the experiment.
3. fable5's empirical two-window census (262,687 repeating J=6 patterns
   below 3e7, minimal aftermath difference 1.7e-6) is direct empirical
   support for ab2's C10 abundance heuristic: fork-merge configurations are
   refinements of pattern repeats, birthday-scaling plentiful.
4. ab1's C11 and fable5's Hypothesis (P) are the same fact from two sides:
   constant words have fixpoint denominator 1, which is exactly why the
   equal-run route needs anti-concentration.

## 4. Q5 observations (trace/artifact phenomenology)

- Within-model A/B pair, identical German wrapper, identical payload:
  variant 1 answered in German, variant 2 in English. Language selection is
  sampling-level, not model-level.
- Code-switching inside ab1: Lean comments and the mandated section header
  "Where I am stuck" in English within a German document.
- fable5 stayed English throughout (wrapper language: confirm from
  transcript). fable5 trace shows anchor propagation: an unverified 15.6
  estimate travelled three turns as "verified" before the report's exact
  computation corrected it to 4.693 -- report != trace, artifact discipline
  caught it.
- Self-correction marker density (fable5): 62 in exploration turns vs 14 in
  the consolidation turn.
- Effort contrast: 79 min / 3 turns / full numerics (fable5) vs 9-12 min /
  1 turn / zero numerics (gpt56sol) -- yet disjoint novel mechanisms from
  each. Route diversity so far is BETWEEN samples, not only between models.

## 5. Implications for the 1b briefing (extend before dispatch)

Add to payloads/1b: routes E, F, G with exact statements; parity uplift;
ERRATUM-3 and the countermodel; the run-census empirics; instruction to
target the weakest route (G) for the conditional theorem and its Lean form
(ab2 8.4 skeleton). Do NOT dispatch 1b until the Gemini 1a slot is closed
and archived.
