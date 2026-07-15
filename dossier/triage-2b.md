# Triage 2b -- blind re-review R2b (Fable arm) and cross-arm comparison

Round R2 ran TWO arms on the identical anchor-stripped object
(be11a262...0e95ff) with the identical payload review_2a: R2a = ChatGPT
temp chat (triage-2a) and R2b = Fable, two turns per rule 7 (phase
discipline attested for turn 1; only the reviewer's own output fed
back). R2b report: review_report_turn2.md, self-declared sha
e2b8d0ab...faa9c4 (above-hash-line convention; operator hash of the
archived file canonical). Same-family arm on a fable-lineage object is
DELIBERATE: it tests the ANN-10 thesis (blindness is role-induced, not
family-induced) on the review side.

## Verdict

SOUND with repairable issues, 0.88 (elementary rail 0.98, counting
rail 0.85 conditional on sketch repair, assembly 0.92), ZERO fatal.
Computation volume exceeds R2a: exact Fraction arithmetic throughout,
sieve to 7e7, 200 randomized synthetic FM instances for the step-2
identity, rational SURROGATES certifying the 2.3/2.4 threshold
sharpness (b delta odd AT s, even from s+1; WLOG s >= 1 necessary),
and a full independent re-execution of the section 8.4 empirical
records.

## Adjudication of R2b findings

R2b-1 (A18/P3e; = R2a-1, convergent). The 4.2 sketch's kappa-uniform
"<= 3k" fails; INDEPENDENT sharper witness H = {0, 444}, t = 70,
colliding {5, 7, 11, 17}, kappa_min = 404.15 (steering-re-executed
exactly; R2a needed kappa ~ 9115). Statement intact; repair identical
in shape to R2a's. Already EXECUTED in v1.2; witness added to the
lemma note in v1.3.

R2b-2 (P3d; = R2a-adjacent, convergent). Span-hypothesis necessity via
the independent linear family {0, 2, 6, D}: sum ~ 0.98 D. Matches
steering's {0, D} check (0.99 D) and the v1.1/F2 record. No action.

R2b-3 (A25/P5; repairable, NEW). Budget ineffectivity should be
declared: L + 2 <= 4 lnln x first holds near lnln x ~ 31.3 (C_g = 1),
max over x of (L+2) - 3 lnln x ~ 31.7, and at x = e^100 the
construction is out of budget (41 > 18.42). Valid -- the theorem is
honestly asymptotic but said so only implicitly. EXECUTED in v1.3
(section 7 declaration). R2a had observed the same threshold class
(~34.5 at C_g = 10) without requiring the declaration.

R2b-4 (A10; cosmetic, NEW). gamma's evenness is not load-bearing in
Theorem 3.2 (steering-verified: no parity use in steps 1-5); it is
automatic in section 5. Noted in v1.3 (Definition 3.1 bracket); the
frozen Lean ForkMergeAt keeps its even_gamma field -- a harmless extra
hypothesis the construction satisfies.

R2b-5 (A11; cosmetic, parked). The -2 slack in step 1 is unnecessary
(gamma 2^K >= 2^{K+1} > 2^K suffices); it comes free from delta >= 2.
No action.

R2b-6 (A29/A30; certification, NEW). Section 8.4's empirical records
independently re-executed: the (s, b) exclusion CONFIRMED with the
n* = pi(3e7) - 400 margin discrepancy resolved and zero candidates at
certified distance 2^{-18.2}; the denominator bound re-derived and
STRENGTHENED to > 10^1050 (exact interval of width 2^{-6977},
Stern-Brocot simplest fraction). Steering spot-check: pi(3e7) =
1,857,859 exact by sieve. Recorded in v1.3 (section 8.4 bracket).

R2b-7 (A16/R1; = R2a-6, accepted). 4.1/4.2 remain sketches; closure is
the Lean counting layer. Already declared in the v1.2 changelog.

R2b-8 (A20, cosmetic, parked). 4.3's uniformity over w could be one
sentence more explicit. Parked.

## The orientation non-conflict (cross-arm resolution)

R2a flagged claim (i): natural order (w, w') gives (-gamma, +gamma).
R2b computed and labeled (w' - w) = (+gamma, -gamma) -- the SAME
mathematics in the opposite difference direction, read as compatible
with the object's "(+gamma, -gamma)". Two competent reviewers reading
one line two ways is the definition of ambiguity; the v1.2 fix (natural
order stated, section-6 swap referenced) stands vindicated. No
mathematical disagreement exists between the arms.

## Cross-arm matrix

Convergent (independent witnesses/methods): 4.2 sketch defect;
span-hypothesis necessity; zero fatal; the elementary and assembly
rails fully confirmed; FM-1's exact 2^K target; exact-hit immunity;
hypothesis non-circularity with the same "materially stronger than
fixed-H HL, honestly declared" characterization. Arm-unique valid
finds: R2a -- orientation ambiguity, 0-based normalization handoff;
R2b -- ineffectivity declaration, evenness cosmetic, section 8.4
certification + strengthening, threshold-sharpness surrogates.
Disagreement set after adjudication: EMPTY.

## Calibration, second measurement

Zero gap-class claims against the machine-checked sections in either
arm; R2b additionally re-executed the Theorem 3.2 arithmetic on 200
synthetic instances with exact arithmetic and found no deviation.
Both arms' false-positive rate on Lean ground truth: 0. The
same-family arm was NOT blind on the fable-lineage object -- second
data point for role-not-family (ANN-10), now on the review side with
an anchor-stripped object.

## Position

chain-v1 v1.3 carries zero open repairables from THREE independent
blind reviews (round-1 cross-family, R2a cross-family, R2b
same-family) plus one formalization pass plus steering re-execution.
Two review arms independently certify the empirical layer. BET-04
sign-off targets v1.3; the item-0014 skeleton transcribes v1.3
sections 4-5.
