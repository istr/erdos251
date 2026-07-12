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

---

## Addendum (2026-07-12, late): fable-5 1b arm -- third chain, kernel factorization

Registry: run 20260712_fable5_1b (incognito, web off, >= 2 turns; turn-1 file
write aborted by a filesystem reset; turn 2 = deterministic 3-step abort-safe
serialization of the turn-1 reasoning plus closure of CL3). Provenance is
producer-side complete for the first time: payload self-hash correct,
turn-1 transcript self-hashed (1c5a5ecb...f1d2a75), report self-hashed and
VERIFIED by steering (e5f818af...c7a6560). Output sha256 = the self-hash.
Language: English. Turn-1 trace to the trace repo when available.

Verdict (steering, line-by-line): chain complete and correct.
- CL6 five-step contradiction verified; strictness comes free from
  delta >= 2 (end-tails in [2, H] give |diff| < H <= 2^K); only TWO tail
  bounds; b-free statement; J at triple-log scale suffices since
  gamma <= span <= C1 L ln L.
- CL12 deletion construction verified: both sub-tuples of one super-tuple of
  the first L+2 primes above L+3; antisymmetric middle (+gamma, -gamma);
  admissibility automatic; span <= C1 L ln L; budget L+2+1 <= 4 lnln x
  (explains clause A's constant).
- CL9/CL10 verified in outline: r_p < 1 for non-colliding p, collision
  primes <= 3k, extension sum <= C2 k (ln k)^2; Bonferroni r = 1 is an exact
  union bound; N_cons >= (1/4) S(H) x / l^{L+1} >= 1. THIS CLOSES the
  "nonconsecutive -> consecutive" transition both GPT arms had left open.
  Top reviewer target (self-rated 0.88).
- CL11 tail bound from Cramer-Granville verified. CL13 (independence of
  clause B from clause A at polylog savings) is an exponent-level sketch,
  self-rated 0.70 -- second reviewer target.
- Discipline: [CLASSICAL] tags with inline sketches; briefing-usage register
  complete; FS1-FS5 false-start map with the quantitative family-tax
  computation (fails at the triple-log margin) -- the sharpest wall
  cartography of the experiment so far. Lean skeleton uses the requested
  names; NOTE the HLQuantA stub is literally `True` (flagged by the model
  itself) -- it must not be mistaken for a formalized hypothesis.

Architecture comparison, now three chains:

| | gpt-web | gpt-iso | fable |
|---|---|---|---|
| counting clause | relative error, 20 loglog | relative error, 6 loglog | two-sided factor 2, 4 lnln |
| second clause | Q2 model entropy (bespoke, weak, plausibly provable) | HLQ2 cylinder moments (heavy, 0.05) + HLQ3 | B = Cramer-Granville (NAMED standard conjecture) |
| tail control | proved unconditionally (Markov) | hypothesized per cylinder | pointwise from B |
| fork existence | pigeonhole over all contexts | pointwise pair mass | CONSTRUCTED (deletion pair) |
| transfer noncons->cons | open (transition 1) | open | PROVED (CL9/CL10) |
| FM shape | 1-gap middle, four tails | 1-gap middle, four tails | 2-entry +-gamma middle, two tails, b-free |

KERNEL FACTORIZATION (the experiment's central structural finding): all
three chains share the proved elementary lattice layer and now a proved
transfer layer (fable CL9/CL10, transplantable); what remains is ONE
statistical kernel in four formulations, ordered by strength:
  B (pointwise Cramer gaps)  >  HLQ2 (per-cylinder moments)  >
  two-word variance (fable section 11: second moment of delta over the
  occurrences of one fixed word)  ;  Q2 (model-side entropy) orthogonal,
  plausibly provable for the standard singular-series model.
Sharpest open sub-target on record: the two-word variance estimate.

Review matrix (BET-04): payload R1 is generic and reusable. Object 1 =
gpt-web document, reviewers fresh fable-5 incognito + gemini-3.1-pro.
Object 2 = fable document, reviewers gpt-5.6-sol + gemini-3.1-pro
(cross-family: no model family reviews its own chain). BET-04 resolves if
ANY one chain survives blind review plus operator sign-off.

### Amendment (2026-07-12): review matrix minimized; Gemini demoted

Decision (pre-registered BEFORE any review verdict exists, to preclude
post-hoc reviewer shopping): Gemini leaves the production track (its 1b arm
becomes optional, API/Colab route documented) and the load-bearing review
track. The BET-04 criterion requires ONE second-model blind review plus
operator; the minimal compliant matrix is: object 1 (gpt-web chain) <-
fresh fable-5 incognito; object 2 (fable chain) <- gpt-5.6-sol; no family
reviews its own chain. Gemini remains welcome as an optional third opinion
(informative, not load-bearing) and stays fully in the measurement track
(integrity and phenomenology probes). Rationale on record: two provably
empty 1a hypotheses, no self-hash capability in the isolated surface, one
fabricated checksum, and confabulated cross-vendor capability claims
(runs/README rule 10).

### Review 1 verdict and steering adjudication (2026-07-12)

Object 2 (fable chain) reviewed by gpt-5.6-sol, web off, temporary chat,
8m19s. Provenance fully closed: reviewer self-computed BOTH attachment
hashes correctly (R1 f4a15ffa..., object e5f818...); review file sha
4a2e2eab...6329d209, self-reported and operator-verified. Language: German
under the German wrapper. Phase discipline attested (A written before B).

VERDICT: "SOUND with repairable issues", confidence 0.94. Zero fatal. The
entire load-bearing structure was independently confirmed step by step
(CL3/CL4, the five-step CL6, the CL9/CL10 counting layer including r_p < 1
and Bonferroni, the deletion construction with the interior check i0 = J+2,
CL11, the two-site selection). P7 affirms the exact-hit immunity as real;
P1 concludes the hypothesis is NOT circular but, through clause B, is
materially stronger than a pure HL tuple hypothesis -- matching the
steering kernel ordering exactly.

Steering adjudication of the seven repairs: ALL ACCEPTED.
1. Convergence via p_n <= 2^n is a REAL error (true statement, invalid
   proof, self-confidence 1.00) -- fix p_n = O(n log n). MISSED BY STEERING.
2. Parity threshold fails at s = 0 (g_1 = 1 odd makes b*delta_1 odd) --
   REAL; elegant fix "wlog s >= 1" (representation need not be reduced,
   reviewer A08/A17). MISSED BY STEERING: the mechanism was verified
   generically, the boundary instantiation never tested. Both misses are
   recorded as steering-verification blind spots; the blind review layer
   caught what the architect-adjacent reader did not. Process working.
3. Mertens/Euler-product package (A35, the single gap-severity item):
   accepted; resolution by post-blind citation or full proofs in the
   consolidated chain (item-0004/0007), where blind constraints no longer
   apply.
4. CL13 weakened to "the presented inclusion-exclusion route does not
   suffice" -- accepted, matches the 0.70 triage rating.
5. Budget off-by-one (L+2+1) -- cosmetic, accepted; factor 3 suffices.
6. Lean thresholds and a REAL HLQuantA definition -- accepted, item-0002.
7. Overclaim language ("every implication proved", "Mathlib-ready") to be
   qualified -- accepted; also logged as a Q5 datum (producer confidence
   language vs. audited status).

Probe-design lesson: P2/P3/P5/P6 were shaped around the web-arm
architecture; the reviewer adapted them correctly (e.g. establishing that
H/2^J -> 0 is neither claimed nor needed in the fable architecture, and
that no (1+eps)/(1-eps) division occurs). Future R-payloads: object-neutral
probes or per-object probe sets.

BET-04 position after review 1: the fable chain has survived one blind
cross-review with zero fatal findings. Resolution still requires (i) the
seven repairs executed in the consolidated chain document and re-verified,
(ii) operator sign-off; review of object 1 (gpt-web chain, reviewer fresh
fable-5) proceeds independently.

### Review 2 verdict and steering adjudication (2026-07-12)

Object 1 (gpt-web chain) reviewed by fresh fable-5 incognito, web off,
multi-turn (turn-1 transcript self-hashed 74750bee...d7aa4f, continuation
not restart, all three attachment/self hashes computed correctly). Review
file sha 50efe768...236e64. Language: German.

VERDICT: UNSOUND (fatal gap), confidence 0.90. Finding A9, RE-DERIVED AND
CONFIRMED BY STEERING: clause (Q1) is unconditionally unsatisfiable for
large x. For the length-1 word d = (d1), d1 = largest even <= (log x)^3,
the pair {0, d1} is admissible (nu_2 = 1; nu_q <= 2 < q), so M_x(d) > 0;
the exponential span factor of model (6.1) gives M_x(d) =
e^{-(1+o(1))(log x)^2} < 1/(1+eps); the purely RELATIVE error form then
demands an integer N_x(d) inside (0,1), which does not exist. The M ~ 1
threshold sits near d1 = (log x)^2, so THOUSANDS of family words lie in the
lethal band -- not a corner case. Consequence: HL_quant (web form) is
provably false as stated; the conditional theorem is vacuously true; the
document's own section 14 misdiagnosed its gap (A26). Failure CLASS:
provably-empty antecedent -- identical to the two Gemini 1a hypotheses,
which steering diagnosed there and MISSED here (third steering blind spot,
the largest; the triage sentence "chain complete and correct" for the web
arm is hereby retracted in its hypothesis half; the deductive half stands,
confirmed by the reviewer: C1-C5 watertight, HL=>FM correct modulo the P2
one-line lemma, constants exact with the sharp threshold
eps <= eta/(4-3eta) = 1/77, no circularity, exact-hit immunity real).

REPAIR (reviewer-provided, adopted as canonical for item-0007): mixed error
form |N - M| <= eps0 * M + x^theta, theta < 1 fixed, eps0 <= 1/77; the word
family has x^{o(1)} members, so additive terms cost x^{theta+o(1)} = o(T_x)
and the chain survives with eta/2 -> eta/3 slack. Additionally A_err = 10
is abandoned: even post-repair, (log x)^{-10} relative precision against
the closed-form model (6.1) is presumably false (secondary corrections of
relative order 1/log x, Montgomery-Soundararajan flavor -- UNVERIFIED,
item-0004). The P2 lemma (T_x = (1-o(1))|I_x|) must be stated explicitly.

ARCHITECTURE IMPACT: gpt-iso's HLQ1 carries the SAME defect (relative
(log X)^{-20} on exact gap cylinders; single-entry huge-gap words in
family). The fable chain is STRUCTURALLY IMMUNE: its clause A counts
nonconsecutive tuples, whose in-budget masses are x^{1-o(1)}
(singular series >= e^{-Ck}, k <= 4 lnln x), and consecutiveness is DERIVED
via the Bonferroni layer CL9/CL10. Canonical design going forward: fable
spine (nonconsecutive counting + Bonferroni transfer) with the mixed error
form; consecutive-level clauses, where unavoidable, mixed-form mandatory.

STEERING METHODOLOGY REGISTER (blind spots now three: invalid convergence
justification; s = 0 parity threshold; Q1 integrality -- plus the habit of
verifying-and-silently-supplying unstated steps like P2 instead of flagging
them). New checklist rules: (i) every family-quantified hypothesis clause
is evaluated at extreme family members; (ii) integrality, positivity, and
sub-1-mass corners are checked explicitly; (iii) unstated load-bearing
steps are flagged as gaps even when true. Role-blindness datum: a fresh
same-family instance caught what the architect-adjacent instance missed --
the blindness is role-induced, not family-induced.

Misc: reviewer flagged the briefing citation "Acta Arith. 126 (2007)"
alongside arXiv:1105.1451 as anachronism-suspicious (plausible
retro-posting; verify in item-0004).

BET-04 position after both reviews: the path runs exclusively through the
FABLE chain (review 1: sound with repairables, zero fatal). The gpt-web
chain is locally repairable but would need re-review post-repair; not
required for the bet. Next artifact: the consolidated chain document
(item-0007 deliverable) -- fable spine, mixed-error clause A, all seven
review-1 repairs executed, both reviews ingested -- then operator sign-off.
