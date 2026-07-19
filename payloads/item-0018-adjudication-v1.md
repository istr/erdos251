# item-0018 M1 R2 adjudication (v1)

Date: 2026-07-19. Adjudicator: steering lineage (Claude Fable 5,
claude-fable-5). Every MAJOR disposition below was re-executed by
steering against the deliverable and the corpus before repair;
finite computations were re-run locally (sympy exact arithmetic).

## 0. Artifact identification (steering sha256; operator canonical)

- Review object: payloads/item-0018-review-object-v1.md,
  86ddc3c0968af1663ba9e06a020d4858bc4a39d93f1053c81f3ef2f6918c3efd
  -- committed byte-identical to the steering-delivered file.
- Review payload: payloads/item-0018-review-r2-payload-v1.md,
  54a2e789d2360c087a428a0b4617d20c73613c2b973a2c37997a880a5a7a843c
  -- OPERATOR REVISION of the steering-delivered file (c60941c8...
  f12690), verified single-line diff: the runs/README.md manifest
  hash updated bff65222... -> fb4dbdc8..., which steering verified
  equals runs/README.md at the branch state c1b262b (rule 17
  present). The in-session operator hash override recorded in the
  review header matches. Supersession per rule-17 discipline; the
  pack was taken at c1b262b while the steering manifest was
  computed at d0cde9b -- gate-hygiene lesson (Section 5).
- Review: payloads/item-0018-review-r2-v1.md, 505 lines,
  c1d846ccc4cf42ad6f8e4fc9db3ff27541d3fe4a0364eba9985711dfd46778f0.

## 1. Verdict acceptance

Reviewer verdict SOUND WITH REPAIRABLE ISSUES, confidence 0.94,
ZERO FATAL, 9 MAJOR / 5 MINOR / 7 NOTE. ACCEPTED. The review is of
high quality: every conviction quotes the object verbatim, the
positive NOTE layer independently re-derives the load-bearing
arithmetic (pigeonhole, N/4, c*, the rho local form, the 7.3 field
map), and the convictions are precision defects, not mathematical
errors in the selected design.

## 2. Dispositions (all repairs land in relext-statements.md v1.1,
## marked "[R2 repair, <finding>]"; Section 9b is the in-document
## record)

MAJOR-1 (B2 rate display not closed) -- SUSTAINED. Re-execution:
  the Section 4 display quantified eps without using it and used
  C_F without a quantifier; the 7.1 form was already closed.
  Repair: B2.plain and B2.reduced restated in the closed eps-form
  (identical to 7.1); C_F demoted to derived rate notation; the
  F18.3 entanglement derivation rewritten in eps-form (|Fam| <=
  eps sum N_P for every eps => mean multiplicity -> infinity).
  Locus precision: the defect sits against the kickoff-D1
  "full quantifier prefix" mandate (Section 4 display); the D3
  table's six questions do not include closedness, so the row
  itself was not false -- the repair makes the point moot.
MAJOR-2 (B3 C_q unquantified) -- SUSTAINED. Repair: one fixed
  nonnegative C_q with C_q/ln x -> 0, declared independent of eps,
  s and the selection, D0-pin dependence only; display unchanged.
MAJOR-3 (A1-typ not an exact statement) -- SUSTAINED. Repair:
  A1-typ written as ONE complete candidate: HLQuantA assumed by
  name, conclusion N^o >= (1/4)(ln x)^{-tau(A')(1+eps)} modelMass,
  tau(A') = 2A'/ln 2 fixed, uniformity and threshold dependence
  declared; heuristic MOTIVATION (U18.1) separated from statement
  exactness in the STATUS line.
MAJOR-4 (C1 family not ex ante; circularity) -- SUSTAINED.
  Re-execution: RS.1's default makes the draft's FF(x) subset Fam
  implicitly s-dependent while the display quantified over all s;
  the post-cap reading is circular and the empty family satisfies
  the display trivially. Repair: named EX ANTE family rule
  FF_{s,x}, declared CAP-BLIND (window-only and word data),
  nonempty window mass required, N^{w,(s)} threshold-explicit on
  both sides, eps_C/x_6 dependence declared; propagated to eta_s,
  C1'', and the D5 item-0021 target.
MAJOR-5 (route-relative promoted to unconditional closure) --
  SUSTAINED AS WORDING (the item-0017 FATAL-1 class). Re-execution:
  the c* window is a NECESSITY analysis of the recorded
  truncated-tail route, and the tau(A') thinning is U18.1
  heuristic; "CLOSED unconditionally" / "never fits" exceeded
  both. Repair at three sites (A1 consumer-fit; Section 6
  consequence; F18.2 body and register): "for this recorded
  route" plus the U18.1 qualifier; the mathematics is unchanged.
MAJOR-6 (F18.1 repeats w2 without its heuristic qualifier) --
  SUSTAINED. Repair in F18.1 and the Section 6 consequence: w1 =
  proved regime boundary; w2 = U18.2-predicted; "both quantified"
  -> "both tabulated".
MAJOR-7 (U18.6 "derivable" overclaims) -- SUSTAINED. Re-execution:
  dossier Theorem M1 is stated in Par(1,x) on the per-position
  filter S^M_x(A,D); its recorded clauses certify the
  (ln x)^{-2+o(1)} twinned fraction only; M1(e) is an
  upper/dilution device, and no uniform lower match-probability
  bound, post-dilution lower-tail argument, Par -> Par' adaptation
  or degree-to-mass conversion is written anywhere in the corpus.
  Repair: "PLAUSIBLY derivable after four named steps, none
  written; no derivation supplied" in the A3 support sentence and
  U18.6. FU1's one-session estimate is superseded by this
  four-step scope.
MAJOR-8 (C1'' side-class density bound unstated) -- SUSTAINED.
  Re-execution: no displayed upper bound for a side class exists
  in the object or the corpus, and a proved one would itself carry
  a growing-k sieve constant (F17.9-adjacent) -- the blanket "ANY
  family" claim rested on it. Repair: density figure marked
  HL-PREDICTED (model-level); obstruction scoped to classes with
  INDEPENDENTLY known density exp(-Theta((lnln x)^2)).
MAJOR-9 (workpapers outside the pack; pointer over-breadth;
  uncommitted k = 24 computation) -- PARTIALLY SUSTAINED.
  (a) Pack scoping: correct observation, but a payload-design
  consequence, not an object defect -- the R1 lane (budget-sheet
  re-execution) was discharged by steering with BYTE-IDENTICAL
  table reproduction and booked in ANN-53 before the R2 dispatch;
  the blind reviewer could not know this. Process repair: future
  review packs include the workpapers (they are not answer keys),
  and pack manifests pin a commit explicitly (Section 5).
  (b) Pointer over-breadth: SUSTAINED; the Section 5 sentence is
  narrowed and m(x)/mu(x)/(n1)-margin are declared explicitly.
  (c) Self-containedness: new Section 5a embeds the decisive rows
  verbatim (T4 witnesses, T5(a) vacuity, T5(b) w2 ratios, T6(b)
  c*, T7 reserve).
  (d) The k = 24 computation: STEERING RE-EXECUTED AT ADJUDICATION
  with displayed data, now embedded in A1: primes 29..137,
  balanced split J = K = 11, block spans 102, d = 6, budget
  148.07, candidates d' even in [2,46], EXACTLY d' = 6 admissible
  -- the object's claim confirmed. Scan over all splits J = 1..21:
  balanced and near-balanced give exactly 1; near-degenerate
  splits J in {1, 19, 20, 21} give 2-4. NEW OBSERVATION: doubly-
  extendable in-budget side pairs EXIST at k = 24 at degenerate
  aspect (a suffix block of 2-3 points is weakly
  shift-constrained); U18.7 remains OPEN as stated (uniform,
  balanced, growing rank) with its evidence updated and a concrete
  FU2 lead recorded.
MINOR-1 (F18.5 ignores the rho-cap domain) -- SUSTAINED; F18.5 and
  the B1 statement-precision paragraph domain-qualified.
MINOR-2 ("B1 logically strongest" false) -- SUSTAINED; D5 gloss
  replaced by the restricted-domain comparison.
MINOR-3 (two threshold conventions) -- SUSTAINED; single
  dictionary s := t (7.3), with the downstream dyadic consumer's
  own t = s+2 call noted; D0 row repaired.
MINOR-4 (RS.3 zero-denominator domain) -- SUSTAINED; positivity
  domain added, with the observation that any block realized by
  primes exceeding p omits residue 0 mod p, so realized side pairs
  are admissible with positive block singular series; rho := 0 off
  domain (unused).
MINOR-5 (B1' constant unquantified; stale threshold) -- SUSTAINED;
  existential absolute C_rel and threshold x_3'(eps_0, R).

NOTE-1..7 -- ACKNOWLEDGED, no action: both PROVED tags sustained;
pigeonhole, N/4 arithmetic, 7.3 fidelity, decl citations, c*
necessity arithmetic, and the repaired rho local form all
independently re-derived by the reviewer (NOTE-7 makes the 9a rho
retraction three-way verified: in-run audit, steering, R2).

## 3. What did NOT change

The D5 selection (A3 + B2.reduced + C2), the 7.1 Prop shapes, the
7.2 pigeonhole, the 7.3 instantiation, the slack ledger 7.4, and
the m1-m5 measurement spec are unchanged under all 14 sustained
findings (reviewer-confirmed for 7.1-7.3). The M2 surface is
STABLE; the item-0020 target statement (B2.reduced) is now also
CLOSED as a proposition, which is what BET-20260718-08's
deferential shape clause binds to.

## 4. Process observation B6 (for the ledger at close)

Third recurrence of the verdict-promotion pattern: item-0005 P1,
item-0017 FATAL-1, here MAJOR-5/6. Both same-family rule-16(a)
passes (the in-run post-repair diff AND the steering pre-gate
pass) missed "CLOSED unconditionally" / "both quantified"; the
cross-family audit caught them. Follow-up candidate (operator
decision, not codified here): strengthen rule 16(a) with a
promotion-hunting keyword sweep ("unconditional", "ever", "any
family", "never", "closes", "both proved/quantified") and/or place
the dedicated pass cross-family.

## 5. Gate-hygiene lessons (for kickoff/pack v2 templates)

(g1) Review packs include the item's committed workpapers.
(g2) Pack manifests pin the commit they were hashed at, stated in
the payload; operator re-pin follows rule-17 supersession (as
correctly happened here: bff65222 @ d0cde9b -> fb4dbdc8 @ c1b262b,
operator-overridden in-session and re-verified by steering).

## 6. Recommendation

M1 verdict layer v1.1 is support-class coherent under the review's
own repair set (all nine required repairs executed, 1:1 traceable
to [R2 repair] marks). Recommendation: operator ratifies v1.1, NO
second R2 round (item-0017 precedent: wording-class sustained
findings close at adjudication), ff-merge of branch item-0018 to
main, then close bookkeeping (ANN-54, HASHES for the four review
artifacts) and kickoff v2 for M2 against the post-merge pin.
