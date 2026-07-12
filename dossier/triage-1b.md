# Steering triage: stage 1b pair (CONTAMINATION CLASS C+)

QUARANTINE: synthesizes across 1b runs and steering verification. Must not
accompany any blind review dispatch (see payloads/review_1b.md) and must not
enter future blind arms.

Date: 2026-07-12. Author: steering (Claude Fable 5). Both documents were read
in full; every "verified" item below was checked line by line by steering.

## 0. Run registry

| run_id | arm | model | dur | lang | self-hash | output sha256 |
|---|---|---|---|---|---|---|
| 20260712_gpt56sol_1b_web | web ON | gpt-5.6-sol (operator: confirm string) | 14m44s | de | correct | 32128bc2...ea6b10 |
| 20260712_gpt56sol_1b_iso | web OFF | gpt-5.6-sol (operator: confirm string) | 13m40s | de | correct | d60b460c...c8eefa |

Payload: 1b revision 2, sha 5f6abc6f...b4e4, self-verified correctly by BOTH
runs (OpenAI remains the only vendor with a clean self-hash record).
Wrapper v2 (web arm, verbatim): "... Recherche und Websuche sind
ausdruecklich erlaubt. Falls das relevante Paper ScPu11 nicht abrufbar ist,
kann ich es bereitstellen. ... Aber Nachfragen, Recherche, Fragen nach
zusaetzlichem Material und mehrere Turns sind ausdruecklich erlaubt. Es ist
NICHT ERLAUBT, auf Memory ausserhalb dieser Anweisung zurueckzugreifen."
Wrapper v3 (isolated arm, verbatim): "... Recherche und Websuche sind
abgeschaltet. ... Aber Nachfragen, inklusive Fragen nach zusaetzlichem
Material und mehrere Turns sind ausdruecklich erlaubt." (No memory clause;
operator to record surface type.) Note: the web arm ran because the intended
incognito isolation failed technically; the memory prohibition is a soft
mitigation only.

## 1. Verdicts (steering verification)

WEB ARM (erdos_251_hl_fork_merge_result.md): complete chain
HL_quant => FM => irrational. Verified: C1-C5 (identities, even lattice,
quantization, fork-merge, FM => irrational), C6 unconditional mean-tail
O(log x) by telescoping, C7/C8 Markov removals, 8.1-8.4 pigeonhole with the
two load-bearing subtleties explicitly checked: T_x = (1-o(1))|I_x| (every
site carries some word; only the span filter removes o(1)) and the four-tails
bookkeeping (goodness removes both shifts per site). Package: Q1 relative
counting error (log x)^{-10} over words of length <= 20 loglog x, span
<= (log x)^3; Q2 averaged model fork-entropy with fixed eta = 1/20 (a
statement about the explicit singular-series/Poisson model, plausibly
provable for it); Q3 window arithmetic. FS1 proved: pointwise HL without
family-summable relative errors cannot exclude fork-collapse on good sites
(the occurrences of one word, ~x exp(-Theta((loglog x)^2)), fit inside the
bad-tail set, ~x (log x)^{-3}). Minor flags: mathlib module names look
suspect (Mathlib.Data.Nat.Prime.Nth / Mathlib.NumberTheory.Real.Irrational;
expect Mathlib.Data.Nat.Nth / Mathlib.Data.Real.Irrational -- item-0002),
Kuperberg arXiv:2210.09775 to be spot-checked (item-0004), one \ne escape
mangled in 5.1 (cosmetic).

ISOLATED ARM (erdos_251_hl_fork_merge.md): complete chain with a DIFFERENT
package. Verified: C01-C05 (same core, parity marked), C06 in full: HLQ1
gives nonempty occurrence sets; HLQ2 (conditional first tail moment on exact
gap cylinders) at offsets t = r and t = 2r+1 plus Markov-within-cylinder
((1+eps)/(1-eps) <= 3) yields one good occurrence per word; n != m forced by
the differing central gap; 2^r >= (1/2)(log X)^{2 ln 2} beats H = 6B log X
since 2 ln 2 > 1. Model mass defined via full inclusion-exclusion (more
principled than the web arm's Poisson factor). Exemplary honesty: rates the
TRUTH of its own clauses HLQ1/HLQ2/HLQ3 at 0.10/0.05/0.15 and names HLQ2 as
the main gap; UNVERIFIED discipline applied to all briefing literature.
Minor flags: "Where I am stuck" delivered as German header (contract asked
the English literal; trivial); Lean compile confidence self-rated 0.35.

## 2. Architecture comparison (the substantive Q4 payload)

| aspect | web arm | isolated arm |
|---|---|---|
| tail control | PROVED unconditionally (telescoping + Markov, C6-C8) | HYPOTHESIZED conditionally per cylinder (HLQ2, self-rated 0.05) |
| model clause | averaged fork entropy, eta = 1/20 (weak, robust) | pointwise fork-pair mass lower bound (stronger) |
| model definition | Poisson-exponential factor (heuristic) | full inclusion-exclusion (principled) |
| constants | 20 loglog window, error (log x)^{-10}, H = (log x)^4 | 6 loglog window, error (log x)^{-20}, H = 6B log x |
| literature | ScPu11 verified (SC2), Tao thread, Gallagher, Kuperberg | none (web off), briefing UNVERIFIED |

Synthesis for item-0007: adopt the WEB package (unconditional tail layer plus
averaged Q2) with the ISOLATED model-mass definition (inclusion-exclusion).
The open mathematical work orders as: (i) prove Q2 for the standard
singular-series model (plausibly a lemma); (ii) the nonconsecutive ->
consecutive transfer inside Q1; both named identically by the two arms.

## 3. Q4 verdict (value of context) and other experiment entries

- 1a -> 1b: total route lock. Both briefed runs executed fork-merge as
  instructed and completed the chain; in blind stage only 1 of 5 runs found
  the mechanism. Context value = route selection plus full execution.
- web vs isolated: the mathematical core survived isolation; web bought
  literature grounding plus (observed, not attributable at n = 1) the leaner
  hypothesis architecture. Both arms ~14 min, both German, both self-hash
  correct.
- ANN-02 ADJUDICATED (middle position): fable5-C18 was right that pointwise
  HL cannot suffice (FS1, web arm section 9); steering was right that no
  prime-level anti-concentration axiom is needed -- the entropy content
  lives in the MODEL (Q2/eta), where it is plausibly provable. Both
  ingredients (family-summable relative errors AND a model entropy clause)
  are required; Tao's "Shannon entropy" pointer is thereby made precise.
- Methodology note: steering raised and then retracted a repo-leak alarm on
  the web arm; the grep hits were substrings (d-istr-ibution, the mathlib
  github.io link, the self-chosen Lean identifier erdos251Sum). Recorded as
  a false-positive class for future audits: anchor greps on word boundaries.

## 4. Bets status

- BET-04 (informal conditional proof): chain complete and steering-verified
  TWICE; resolution requires blind cross-review plus operator sign-off.
  Review object: the WEB-ARM document (fuller); isolated arm held as
  independent replication evidence. Reviewers: cross-vendor pair (fresh
  fable-5 incognito plus gemini-3.1-pro), payload payloads/review_1b.md,
  operator attaches the artifact separately, NO steering material.
- BET-05 (Lean-verified same round): unresolved; Lean bring-up (item-0002)
  has not started. Both arms delivered compatible skeletons (the isolated
  9.x set is the more index-careful one).
