# item-0020 in-run adversarial audit record (workflow fan-out;
# refuter discipline, default-refute; project 3.5-pass pattern)

Design: 14 finder agents -- 3 independent refuters per claim C1-C4
(lenses: arithmetic/quantifiers, corpus fidelity, counterexample
hunt), one independent budget-sheet re-execution (fresh code, no
copying), one completeness critic over the W0-W3 package -- then 2
independent adversarial confirmers per raised FATAL/MAJOR finding
(sustained = 2/2 confirm). All agents corpus-only, local python3
permitted. Executed against the PRE-repair drafts; every sustained
finding repaired in place -- with [audit repair] marks in the
workpapers, and worded inline ("audit-weakened"/"audit-verified")
in the verdict object; the repaired files are the committed
versions.

## 1. Verdict summary

  agent          verdict              findings
  C1:arith       SOUND_WITH_ISSUES    5 (0 MAJOR)
  C1:corpus      SOUND_WITH_ISSUES    6 (0 MAJOR)
  C1:cex         SOUND_WITH_ISSUES    5 (0 MAJOR)
  C2:arith       SOUND_WITH_ISSUES    3 (0 MAJOR)
  C2:corpus      SOUND_WITH_ISSUES    3 (0 MAJOR)
  C2:cex         SOUND                4 (0 MAJOR)
  C3:arith       SOUND_WITH_ISSUES    3 (0 MAJOR)
  C3:corpus      SOUND_WITH_ISSUES    5 (0 MAJOR)
  C3:cex         SOUND                4 (0 MAJOR)
  C4:arith       SOUND_WITH_ISSUES    6 (1 MAJOR)
  C4:corpus      SOUND_WITH_ISSUES    7 (1 MAJOR)
  C4:cex         SOUND_WITH_ISSUES    5 (1 MAJOR)
  sheet-reexec   SOUND_WITH_ISSUES   10 (1 MAJOR)
  completeness   SOUND_WITH_ISSUES   10 (1 MAJOR)

Raised FATAL: 0. Raised MAJOR: 5. Sustained (2/2 confirmed): 4.
Overruled (split vote): 1. No claim's CONCLUSION was overturned;
one claim's STATEMENT was weakened to what its own verification
proves.

## 2. Sustained findings and executed repairs

S1 [MAJOR, 3-agent convergence: C4:arith + C4:corpus + C4:cex; both
   confirmers each]. The C4 barrier STATEMENT's universal clause
   "every realized class of size >= 2 is middle-rigid" is FALSE in
   the constructed model: every gap-step boundary g -> g+2
   realizes the side pair (g^J, (g+2)^K) at two consecutive sites
   with middles g and g+2 -- a non-rigid size-2 class; ~ln x/2
   such classes at every scale (computationally verified by the
   refuters at 1e6/5e6/1e8 with the pin depths; e.g. 7 such
   classes at 1e8). The claim's CONCLUSIONS survive: the
   verification step (4) had proved only the hedged form, and the
   refuters measured the displayed ratios at 0.9981-0.99996 |S'|.
   REPAIR (executed, proofs.md C4): statement weakened to
   "middle-rigid outside a transitional subfamily of mass
   O(L ln x) = o(|S'|)", selection defined as argmax, s = 0
   sufficiency noted, the non-rigid boundary population named
   exactly, and the audit's alternative construction (single-site
   intermediate runs) recorded as an unexecuted option.
   Independent same-object convergence (3x) is the strongest
   signal class of the project's process history (item-0017 B3,
   item-0018 O3); it recurred here.

S2 [MAJOR, C4:arith/corpus (overlapping with S1's confirmations)].
   The consequence clause overstated the characterization: what is
   proved is "every proof must consume an input that FAILS in the
   model", not "...that distinguishes the middle slot" (the
   Maynard example in SCOPE is itself a non-middle-slot qualifying
   input). REPAIR (executed): characterization corrected in
   proofs.md C4 and relext-upper.md items 7/F20.7; middle-slot
   inputs demoted to "the salient family".

S3 [MAJOR, completeness]. Kickoff W2(d) mandates six D3 answer
   lines per mechanism; the draft T7 gave first-failure lines only
   for the mechanism routes. REPAIR (executed): budget_sheet_20 T7
   now carries the full six-line matrix for M1.a/M1.b/M2/M3/M4/
   M5/M6/M7 (full answers for the live M5 and open M1.b; explicit
   "moot" entries after a route's first FAIL).

S4 [MAJOR, sheet-reexec; vote split 1-1 on a SEPARATE raising of
   the same substance by sheet-reexec -- see O1 -- but sustained
   as part of the eps_C cluster via C3:arith + C3:corpus + C3:cex
   + completeness MINOR convergence]. The T5/C3(d) gate arithmetic
   mixed two eps_C conventions (measured eps_C = 0 giving 1/16 vs
   consumed eps_C < 1/2 giving 1/64) without reconciliation.
   REPAIR (executed, T5 + proofs.md C3(d)): single convention --
   eps_C is ABSENT from this run's chain (7.4(s2) applies only to
   window-only detours; the C1/C3 chains have none); the one
   consumption point is pair-eps = (delta/4)^2 = 1/64; the m4
   measurement stays direction-only (D3(vi)); the measured-analogue
   comparison now cites both grains (W2-grain ~0.47, Q-grain ~0.24
   at 1e9) against 1/64.

## 3. Overruled finding

O1 [MAJOR raised by sheet-reexec; confirmers split 1-1, not
   sustained as raised]. As raised, it asserted the sheet's
   declared consumption made the printed 1/16 threshold invalid;
   the refuting confirmer read the (1-eps_C) factor differently.
   The SUBSTANCE (two conventions mixed in one display) was
   independently raised as MINOR by three C3 refuters and the
   completeness critic and is repaired per S4; nothing of the
   raised content is silently dropped.

## 4. Minor/note disposition (grouped; all repaired unless noted)

m1 [5-agent convergence: C1:arith/corpus/cex, C2:arith/corpus/cex].
   The draft's "n = 1 odd-entry word" exception is VACUOUS under
   the RS.1/T6 indexing (site words use gap indices >= n+1 >= 2,
   all even); the +1 slack was unnecessary. REPAIRED: I5 rewritten,
   +1 dropped from C1/C2 and downstream displays (F20.1).
m2 [C1:arith/corpus/cex]. Depth form written as coefficient-O(1);
   the corpus form is additive. REPAIRED (C1 step (2)).
m3 [C1:arith/cex + C1:corpus + C2:cex + sheet-reexec, convergent].
   Crossover-convention mismatches: the sheet bisected a
   neighboring condition (8 cap <= x/ln x, continuous depth proxy
   mislabeled "D0-honest") and rounded decades upward; the T2/T3
   commentary contradicted its own rows ("from 1e20 on";
   "1e40-1e260", a stale range matching nothing); "monotone
   verified" was asserted but not performed. REPAIRED: T2 now
   prints BOTH labeled conventions -- scale marker and the exact
   proof condition 8 cap <= x/(2 C_0 ln x) at ceil-honest depths
   (crossings 1e100-1e110) -- with an actual single-sign-change
   scan; rounding to nearest decade; commentary rewritten; proofs
   C1(4)/C2 and relext-upper item 2/F20.1 re-cited accordingly;
   x_0(C_0) folded into x_2(s).
m4 [C1/C2/C4 corpus lenses]. Provenance labels: I4's inversion and
   I3's general-r form are this-run derivations from anchored
   facts, not displayed corpus lemmas. REPAIRED (consumed-inputs
   block relabeled).
m5 [C3:arith/corpus/cex]. Sharpness remark's Q dropped the 1/m
   normalization and understated the sharpness domain; the
   configuration was mislabeled a C(t) variant. REPAIRED (C3(c):
   exact arithmetic, ratio sqrt(1-1/r) for every 2 <= r <= m).
m6 [C3 lenses]. B2.pairs hypothesis display: d-range aligned to
   the anchored "even d >= 2" form with the parity note that makes
   step (2) airtight. REPAIRED.
m7 [C4 lenses]. C_0 numeral (2/ln 3 = 1.8205, attained at the
   shared q_1 = p_1 = 2 datum); delta >= 2 one-line argument
   replacing the "glued initial values" appeal; s-quantifier made
   explicit (s = 0); Montgomery-Soundararajan corpus-status
   wording; dangling "M3(c)" reference -- the row now exists (T6
   M3(c)). ALL REPAIRED; the inventory M3.3 constant-gap sketch
   correction is recorded as a non-silent mutation note.
m8 [completeness]. M6 singleton-inertness statement and M4
   quantifier prefix / "where o(ln x) comes from" lines added to
   the inventory; T1 trap-row ratio annotation (2.4-2.6x at
   tabulated scales); working-notes digest fragments replaced by
   full 64-hex digests (all nine re-verified against the kickoff
   list); cross-reference fixes (T2 -> T1; "row M1(c)" -> T4).
   ALL REPAIRED. The W2 priority-order justification paragraphs
   live in the final report Section W2 (written after the critic
   ran); the F20/U20 numbers cited in the workpapers are assigned
   exactly as anticipated in relext-upper.md Sections 5/6.

## 5. Positive verification records (recorded, not findings)

- sheet-reexec reproduced EVERY numeric value of the committed
  tables to 3 significant figures from independently written code
  (T0/T1 incl. the trap row, T2 exponents and all crossings, T3
  ratios, T4 exact counterexample arithmetic incl. the B2.pairs
  refusal check, T5 floors and gate coefficient, T6 span ratios).
- C1: the capacity identity and C(M,r) <= (eM/r)^r brute-force
  verified; all-singleton/empty-Fam_2 edge cases checked; every
  consumed input verified at claimed strength against the anchors
  (I1 RS.1 verbatim; I2 quantifier order verbatim incl. PROVED
  status provenance).
- C2: the adversary's optimal spread configuration checked; the
  T3 ratios reproduced to the digit.
- C3: selection/threshold order verified load-bearing and correct
  (x_4(eps) := x_8(eps^2) s-free); the restricted-form a-fortiori
  step and the FL-1 declaration verified against Supply.lean's
  hrestr encoding.
- C4: the model's T-fact checks re-executed numerically by the
  refuters out to q ~ e^10000 (Chebyshev sup 2/ln 3 at n = 1,
  interior max 1.3337 at n = 148, decaying; PNT ratio -> 1; P3.2
  ratio ~1.2 vs bound 26; two_le_delta zero violations; all sites
  pass all three D0.2' filters at 1e6); the displayed
  (1 - o(1))-ratios measured at 0.9981 (1e6), 0.9995 (5e6),
  0.99996 (1e8).

## 6. Post-repair passes

- The repaired budget sheet re-runs deterministically (sha256-
  stable across consecutive runs).
- A post-repair verification workflow (rule-16(a) clause diff over
  relext-upper.md Section 1 against the body/workpaper support
  classes, plus a dedicated re-refutation of the REPAIRED C4
  statement) ran after the repairs; its disposition is Section 7.

## 7. Post-repair verification disposition (PASS 2; three agents:
## rule-16(a) clause diff, C4 re-refutation, consistency sweep)

Verdicts: clause-diff PASS_WITH_ISSUES (1 MAJOR, 4 MINOR, 4 NOTE);
C4 re-refutation PASS_WITH_ISSUES (2 MAJOR residue findings, 2
MINOR, 2 NOTE) -- the REPAIRED C4 statement itself survived
re-refutation; consistency sweep FAIL-as-run (4 MAJOR, all stale
pre-repair residues or the then-unfilled Section 7 slot). Every
finding was folded in a second repair round; disposition:

P1 [MAJOR, clause-diff]. Verdict item 4 re-attached eps_C < 1/2 to
   the pigeonhole consumption point (the S4 defect resurfacing in
   the verdict object; a literal consumer would misbudget by a
   factor 2-4). REPAIRED: item 4 now states the T5 single
   convention (eps_C absent from the chain; 1/8 eps_C-free; the
   eps_C < 1/2 reading attaches to the gate-sentence display
   only).
P2 [MAJOR x2, C4-rerefute + consistency]. Unrepaired S1/S2
   residues in mechanism-inventory M3.3 (universal rigidity +
   exact LHS = |S'| - |Fam| + middle-slot characterization) and
   final-report O3 (middle-slot characterization). REPAIRED: both
   re-worded to the hedged/failure-in-model forms with [audit
   repair] marks; M6's "see the middle slot" clause corrected to
   "carry content outside T".
P3 [MAJOR, consistency]. Final-report W2/O1/O4 carried the
   pre-repair crossover values and the "D0-honest" mislabel.
   REPAIRED to the two-convention T2 values (markers 1e25/1e28;
   proof-condition ceil-honest 1e100-1e110).
P4 [MINOR, C4-rerefute; accepted with its supplied fix]. The
   confinement of non-rigid classes to straddling sites was used
   but not argued. REPAIRED: the one-line SEPARATION lemma added
   to C4 step (4) (g nondecreasing squeezes the middle of any
   (g^J, g^K)-class to g, so classes with run-interior members
   are rigid), plus the #classes = O(L ln x) count, the
   "adjacent runs exceed the depths" boundary quantifier, and
   the gluing example moved above the measured window data
   (x_0 = 2e10).
P5 [MINOR cluster, clause-diff]. Verdict-object precision: item 7
   "o(1) site mass" -> o(1) SHARE with absolute mass O(L ln x);
   the completeness-of-T reading tagged as the U20.4 inventory
   claim; item 8 now cites both measured grains (W2 ~0.47,
   Q ~0.24) at 1.2-1.5 orders above 1/64 and carries the
   alignment-honesty qualifier verbatim; item 1 records M7's
   SUBSUMED-by-merge status; F20.7 "fails maximally" -> "fails at
   the maximal order (1-o(1))|S'|"; support-class taxonomy note
   added to the Section 1 preamble; the M7 chapter's T4 citation
   disambiguated to the anchored item-0018 budget T4; the M2
   inventory span-factor citation repointed to T6 M2(a)
   (5.9 -> 541); the report's "eps_C/1-64" numeral fixed.
P6 [NOTEs, recorded without action]: the (5,5,34) decline
   endpoints added to verdict item 8 for the plural "live rows";
   the four-class support taxonomy extension is declared, not
   silent; audit-record marking language scoped (Section 0).

After the second repair round the package is internally
consistent; the C4 re-refuter's independent census (4/5/7
non-rigid boundary classes at 1e6/5e6/1e8; exact recount
LHS = |S'| - |Fam| - 7 at 1e8) is the quantitative record behind
the hedged barrier statement. No third pass was run: every PASS-2
finding was either a residue of a PASS-1 repair (now folded), a
precision upgrade, or carried its own verified fix; none touched
a theorem's conclusion.
