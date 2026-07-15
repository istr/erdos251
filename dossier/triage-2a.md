# Triage 2a -- blind re-review R2 of chain-v1 (adjudication)

Object: anchor-stripped derivation of chain-v1 v1.1
(object_conditional_chain.md, steering sha be11a262...0e95ff; derivation
runs/_staging_review2a/strip_review_copy.py, deterministic). Reviewer:
ChatGPT temp chat, web OFF, payload review_2a (computation mandatory).
Report: blind_review_report.md, self-declared sha 861c734c...d2528a
(scope caveat in the report; operator hash of the archived file is
canonical). Phase discipline confirmed in-report; computations section
lists 11 re-executed calculations including two full deletion cases and
an exhaustive 267-set Lemma-4.2 small search.

## Verdict

SOUND with repairable issues, overall confidence 0.90 (Phase A 0.91),
ZERO fatal. Explicitly confirmed: FM-1 hits the exact 2^K target
(P5), the five contradiction steps (P6), exact-hit immunity (P7), the
elementary layer (P8), hypothesis non-circularity and role separation
(P1), and -- decisively for the v1.1/F1 repair -- claim (i) verified by
full computation in two (J, K) cases (P2).

## Adjudication of findings

R2-1 (A35/A36/A39; gap class, repairable). The Lemma 4.2 SKETCH's
kappa-uniform collision bounds ("<= 3k", "product <= e^2") are FALSE
for large fixed kappa. Counterexamples steering-re-executed exactly:
t = 10010 = 2*5*7*11*13 gives 4 > 3k = 3 colliding primes at k = 1
(kappa_min = 9115.1356...); prod_{5<=p<=10^6} p/(p-1) = 8.20246098 >
e^2 = 7.38905610. The STATEMENT survives (reviewer's exhaustive small
search: normalized sums 0.50/0.71/0.83 for k = 2/3/4 at kappa = 4, no
counterexample; reviewer supplies the correct O_kappa(k) / e^{O_kappa(1)}
repair with the (k+1) ln D / ln(2k+2) count and the 1/(p-1) reciprocal
sum). EXECUTED in v1.2 with the reviewer's argument. Provenance note:
the false constants predate v1.1; making kappa explicit in v1.1 exposed
them, and steering did not re-derive the sketch internals it was
editing around -- blind-spot register entry 5 (triage-1b addendum 2).

R2-2 (A56/P2; repairable). Claim (i)'s fork orientation: the natural
order (w, w') gives (-gamma, +gamma), not the stated (+gamma, -gamma);
section 6's name swap absorbs it, but (i) was literally wrong. Matches
steering's own F1 verification output (fork_vals = (-gamma, +gamma)),
which had checked |gamma| only -- the reviewer's exact-sign check is
sharper. EXECUTED in v1.2 (orientation corrected, swap referenced).

R2-3 (A55; repairable-cosmetic). The section-5 point sets must be
handed to Lemma 4.3 / Hypothesis A as 0-based translates A - q_0;
section 4's definition of "point set of w" makes this implicit and
5(ii) says "before translation", but the handoff was never spelled
out. EXECUTED in v1.2 (explicit normalization sentence).

R2-4 (A07/A52, A62; repairable, trivial). C_g positivity needed for
log2(4 C_g); C_1 >= 1 needed for kappa = C_1. EXECUTED in v1.2
(C_g >= 1 WLOG in Hypothesis B; C_1 >= 1 fixed in 5(iii)).

R2-5 (A60/P4.5; cosmetic). 5(iv) mixed base and extension
cardinalities. EXECUTED in v1.2 (L + 1 word points stated, with the
(2/ln 2) lnln x asymptotics and the 4 lnln x - 1 budget check).

R2-6 (A31; accepted, not executed). Lemmas 4.1/4.2 remain QED-sketch
rather than full write-ups. Deliberate: their honest closure is the
Lean counting layer (item-0014 path), which supersedes prose sketches;
recorded in the v1.2 changelog. The sketches must be CORRECT (now are,
per R2-1 repair), not complete.

R2-7 (A16; cosmetic, not executed). "s positive" vs the s = 0
discussion uses mixed conventions; the WLOG s >= 1 handles the
mathematics and the Lean layer is machine-checked. Parked.

R2-8 (A41 wording "p > D"; cosmetic, not executed). Linguistic only
per the reviewer's own adjudication. Parked.

Effectiveness observations (not gaps): the reviewer's rastering finds
the 4 lnln x - 1 budget first satisfied near lnln x = 34.5 for
C_g = 10 -- the theorem is honestly asymptotic; noted, no action.

## Calibration measurement (internal aid, config notes)

Sections 2-3 and the Theorem 3.2 arithmetic of the object are
machine-checked in lean/ (milestone, ANN-18). Reviewer verdicts there:
zero gap/repairable/fatal claims against machine-checked content
(A16/A41 are prose-convention cosmetics outside the Lean statements);
P6 confirms all five contradiction steps, P7 the immunity, P8 the
elementary spot checks. Measured false-positive rate on ground truth:
0. All four gap-class findings sit in the unformalized sections 4-5
prose -- exactly the live-signal region. The reviewer's confidence
(0.90, four repairables, zero fatal) is better calibrated than
review-1's 0.94/zero-findings-in-that-layer; the instrument delta
(computation mandatory, uniform-intensity probes) is measurably doing
work: both new findings were produced BY the mandated computations
(exhaustive search, counterexample construction), and the anchor
stripping held -- the report contains no reference to any prior review
or version history.

## Steering re-execution log

Per checklist rule (iv), re-executed before adjudication: A35
factorization and colliding-prime count; A36 collision product to
p <= 10^6 (both exact to the reviewer's digits, 2026-07-15 22:14 UTC
sandbox); A56 orientation cross-checked against the retained F1
verification output; P3's k = 2 row spot-checked analytically
({0,4,10}: single admissible extension t = 6, sum consistent).

## Position

All known repairs are executed; chain-v1 v1.2 carries zero open
repairables from two independent blind reviews plus one formalization
pass. BET-04 sign-off is now an operator decision with a clean table.
The item-0014 statement skeleton transcribes v1.2 sections 4-5.
