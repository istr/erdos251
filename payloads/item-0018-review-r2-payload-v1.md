# Review payload R2 -- adversarial scope audit (blind, cross-family)
# item-0018 M1: relative extension statement layer

You are a reviewer from a different model family than the object's
author. You receive EXACTLY twelve files: this payload, the review
object, and a ten-file read-only reference pack. Do not use the web.
Do not attempt to identify, locate, or fetch the project the files
come from; file paths inside the pack are internal cross-reference
labels only. Treat the supplied bytes as canonical (hash
verification is operator-side; the manifest below is for the
operator's dispatch check).

OBJECT: item-0018-review-object-v1.md
  sha256 86ddc3c0968af1663ba9e06a020d4858bc4a39d93f1053c81f3ef2f6918c3efd
  A mathematics statement-layer document: exactly quantified
  CANDIDATE theorems (none of the OPEN ones is claimed proved)
  about prime-gap "exchange configurations" for a binary-digit
  irrationality program, with budget sheets, no-go audit verdicts,
  a consumer implication design, and a selection verdict. Four
  marked redactions (r1-r4, manifest in the object header): an
  in-run audit record is withheld so your review is independent.

REFERENCE PACK (read-only; the corpus you may check claims against;
nothing outside it is admissible support):
  lean/Erdos251/Exchange.lean
    693c77f449f061fe11064e82d088015375006e6fead46539acf866bef868f4bf
    The consumer: ExchangeAt fields, ExchangeSupply1, the b = 1
    gate. Target of check S5.
  lean/Erdos251/Hypotheses.lean
    16d65550a51b54417bb4c4c37909acd57de7bad3eeb8b5bae7def043ce7e3d1a
    The frozen HLQuantA and CramerGranville texts plus the
    singularSeries / tupleCount / modelMass vocabulary. Target of
    check S4.
  lean/Erdos251/Counting/Words.lean
    bd2f1c49627ef2336ad153cf8925088ccd65f0fa18248296dfc87bcdc1e75982
  lean/Erdos251/Counting/Lemmata.lean
    f131eb91105fe59bca95a347c411c634a646869f29f1f04acd0009affd1c3bfe
  lean/Erdos251/Counting/ConsecTransfer.lean
    e3824192f724411a9142dad0faef480d6157d9705fb801b41fd201bfcd2743e9
  lean/Erdos251/Counting/OneExtension.lean
    2a00e8407fc167e723cb434ef80dfa378142bff19a7faf59259ac02e5dbadada
    The machine-checked Counting layer the object's Section 6 reuse
    audit cites by decl name.
  dossier/e2prime-supply.md
    6dab09983b498a254bfb0fd04d8a18f9a0f323ee186fe55c7b7bddc3f771dadc
    The predecessor dossier (v2). The object cites its Sections 1,
    2, 3.2-3.3, 4.3-4.5, 6, 7.1-7.2, 8, 9 (P3.n, D1.n, F17.n,
    U17.n labels resolve here).
  payloads/item-0005-adjudication-v1.md
    7feef76cdf4e0be574755b6ebcae13d8f744a53cc1a76c5329d52cce9ab8f986
  payloads/item-0017-adjudication-v1.md
    305096e507885add096b9d2d1c5e3445c1cf169d9f93ee09547a6516372959b8
    Provenance sources for the anti-rigidity form and the FATAL-2 /
    F17.9 calculus the object leans on.
  runs/README.md
    fb4dbdc804d351c749468a9d51a3a5071fbe8a892d22603054e43c5757857c3d
    Process rules; rule 15 (asymptotic budget sheet) defines what
    check S6 audits against.

ROLE (scope audit, adversarial): attempt to convict the object of
OVERCLAIMING -- claims whose stated strength exceeds what the body
proves, measures, cites, or is entitled to assert -- and of
UNDER-SPECIFICATION -- candidate statements whose quantifiers,
constants, or normalizations are not pinned. The OPEN candidates
are targets for statement-precision defects, not for being open:
do not report "this is unproved" where the object already says
OPEN. Computation is welcome (re-derive small arithmetic; show it);
your primary duty is logical scope. Mandatory checks:

S1. Verdict vs body: for every claim row of Section 9 (the D3
    verdict table plus its notes), every claim of Section 8 (D5),
    and every scope sentence of Section 10 (F18.1-F18.5), locate
    the body text it rests on and classify the support as PROVED /
    MEASURED / HEURISTIC / MODEL / OPEN / CITED; flag every
    wording stronger than its support class and every missing
    inline qualifier. The object's candidate set carries exactly
    TWO "proved" tags (A2; C2 base form): check each against its
    displayed derivation and cited predecessors with particular
    care -- these two carry the pigeonhole's population floor.
S2. Quantifier hygiene per candidate (Section 4, all of A1, A1typ,
    A2, A3, B1, B1', B2 plain and reduced, B3, C1, C2): is the
    quantifier order unambiguous; is every constant's dependence
    declared (on eps, s, x, the family, the D0 pins); is the
    normalization (even-conditioned vs unconditioned) stated where
    a singular-series quantity appears; is any uniformity claimed
    that the displayed prefix does not deliver? Quote any
    undeclared dependence you find.
S3. Necessity vs sufficiency: the object repeatedly prices
    NECESSITY budgets (the c* window; the C1 closure inputs
    (n1)/(n2); the F18.4 route-vs-statement split). Hunt for any
    sentence where a necessity budget, a route wall, or a named
    open input is read as sufficiency, as statement-level
    impossibility, or as discharged; quote each.
S4. Open-strength check: compare each candidate AS STATED against
    the frozen HLQuantA text in the pack. Convict any statement at
    least as strong as HLQuantA, or a known-open strengthening of
    it, that is not flagged as such; audit the object's own B1(ii)
    FLAG for whether its scoping ("does NOT formally imply
    HLQuantA") is argued or asserted.
S5. Consumer fidelity: (a) the three Prop displays of Section 7.1,
    including the bracketed provenance claims and the pin
    arithmetic behind TailIntersection's 1/4; (b) the Section 7.2
    pigeonhole as a finite chain -- for every step, name what
    licenses it, and check the quantifier coupling (eps = delta/4)
    against the Prop prefixes; (c) the Section 7.3 field-by-field
    instantiation against the supplied Exchange.lean (every
    ExchangeAt field, the b = 1 gate, the threshold threading).
    Any gap between 7.1/7.2/7.3 and the Lean text is reportable at
    full severity.
S6. Budget coverage (rule 15 in the supplied runs/README): does
    every constant and factor of every candidate appear in a
    budget-table row at the exchange scaling; is any constant
    introduced in Section 4 or 7 absent from Section 5's sheets?
    Name each absentee.
S7. Declared-amendment sites: the object marks in-place repairs
    ("audit repair" / "audit-corrected"). Check each marked site
    for internal coherence with its surroundings and the registers
    (F18/U18); re-derive independently rather than deferring to
    the mark. Do not attempt to reconstruct the withheld record.
S8. Corpus fidelity: spot-verify the object's citations INTO the
    pack (dossier section numbers, decl names and their actual
    statements, adjudication content); convict any load-bearing
    dependence on material outside the pack, and any decl cited
    for more than its statement delivers.
S9. Unstated load-bearing steps: any claim that rests on a step
    the object neither displays, prices, nor names as an open
    input -- name the step.

FORMAT: findings listed by severity FATAL / MAJOR / MINOR / NOTE,
each with exact location (section number + quoted sentence), the
support class you assign, and the narrower wording you would
require (or the counterexample; arithmetic shown). Findings must
quote the object verbatim; paraphrase convictions are inadmissible.
Severity calibration for this scope audit: FATAL = a load-bearing
claim (one the Section 8 verdict or the Section 7 design rests on)
false or mis-scoped as stated; MAJOR = a support-class promotion or
quantifier defect that does not topple the selection; MINOR = local
wording or scope slips; NOTE = observations. Then an overall
verdict (SOUND / SOUND WITH REPAIRABLE ISSUES / UNSOUND) with a
confidence in [0,1]. Deliver as ONE markdown file named
item-0018-review-r2-v1.md.
