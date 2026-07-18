# Review payload R2 -- adversarial scope audit (blind, cross-family)

You are a reviewer from a different model family than the object's
author. You receive EXACTLY two files: this payload and the review
object (an anchor-stripped mathematics dossier about prime-gap
"exchange configurations" for a binary-digit irrationality program).
Do not use the web. Bracketed tokens like [TEXT-A], [PIN-2] are
deliberate anonymizations; treat them as opaque names.

ROLE (scope audit, adversarial): attempt to convict the object of
OVERCLAIMING -- claims whose stated strength exceeds what the body
proves, measures, or is entitled to assert. Computation is welcome
but your primary duty is logical scope. Mandatory checks:

S1. Verdict vs body: for every clause of Section 1 (V1-V6), locate
    the body section it rests on and classify the support as
    PROVED / MEASURED / HEURISTIC / CITED; flag every clause whose
    verdict wording is stronger than its support class, and every
    missing inline scope qualifier.
S2. Obstruction language: the object claims "located obstruction,
    never impossibility". Hunt for sentences that read as
    impossibility claims over all routes (rather than
    corpus-relative or route-relative); quote each.
S3. Model-vs-primes discipline: every model-M statement must be
    marked as model-only; every heuristic constant must be labeled;
    check the "TRUTH face"/"PROVABILITY face" split (Section 4.3)
    for leakage of heuristic conclusions into provability claims.
S4. Quantifier order: the object makes claims of the form "route X
    fails for every admissible parameter" -- check whether the
    parameter ranges are the right ones (e.g. is A' > 1 really
    forced; could a different filter shape evade the threshold
    calculus; is the "every measurement" clause justified by the
    measurements actually listed).
S5. The three-blocker exhaustiveness claim (Section 5 table
    summary): is "confirmed EXHAUSTIVE for this corpus" justified
    by the rows shown, and is the corpus-relativity stated
    everywhere it is needed?
S6. The certificate claims (Section 7): are "verified by hand" and
    "reproduces the committed record" statements scoped to what was
    actually checked?
S7. Any claim you find that depends on an unstated load-bearing
    step (checklist-rule-iii style): name the step.

FORMAT: findings listed by severity FATAL / MAJOR / MINOR / NOTE,
each with exact location (section + quoted sentence), the support
class you assign, and the narrower wording you would require; then
an overall verdict (SOUND / SOUND WITH REPAIRABLE ISSUES / UNSOUND)
with a confidence in [0,1]. Findings must quote the object
verbatim; paraphrase convictions are inadmissible.
