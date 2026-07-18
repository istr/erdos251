# item-0017 Session D completion report + OPERATOR HANDOFF

Date: 2026-07-18. Executor: steering lineage (Claude Fable 5,
claude-fable-5), one continuous run for Sessions A-D (compression at
steering discretion; all binding gate orders honored). Branch:
item-0017 (five commits; main untouched). THIS REPORT IS A
STOP-AND-REPORT: everything below the "Operator package" line needs
operator action; nothing further is executed by this run.

## 1. Gates

- Section 6 predicates: held all session (pin 66adc54 operator-
  ratified at start; all 21 anchors; kickoff sha256 = ledger ANN-50
  canonical value; prohibitions observed -- no lean/ edits, no
  chain-v1/tate-transfer edits, kickoff uncommitted, roadmap
  untouched, ASCII-only artifacts).
- D2 gate: PASS with amendments (Session B), order honored.
- Review gate: R1 EXECUTED (blind, computation-mandatory);
  R2 operator-side, pending. Closure NOT executed (ratification-
  gated): no roadmap emit-patch, no ledger append.

## 2. Observations (Session D)

- Review object built with the committed deterministic strip script,
  leak-audited: payloads/item-0017-review-object-v1.md, sha256
  5a7a2647d11ec40d00b2d2ae2473bfdfd2a32a22ab731b7fe93dfe97b85fbb63.
- R1 (same-family fresh instance, web OFF, exactly payload+object):
  VERDICT "SOUND WITH REPAIRABLE ISSUES", confidence 0.89, ZERO
  FATAL. The full numeric spine reproduced independently (Euler
  product exact; both certificates to machine precision incl.
  primality/consecutiveness of all 32 printed primes; an
  INDEPENDENT full 1e9 census matching 29/3/3/0/0; every committed
  grid record). Review registered:
  payloads/item-0017-review-r1-v1.md.
- R1 findings: 1 MAJOR + 4 MINOR + 6 notes; every finding
  steering-RE-EXECUTED before absorption (checklist rule iv), all
  repaired in place with marked amendments (dossier Sections 2.5,
  2.7, 3.2, 3.3, 4.3): the one genuine lemma-level error was
  P3.2's threshold (N >= L+16 -> N >= 40(L+2)); the rest were a
  statement/proof factor 2, an exponent value-substitution, a
  vacuous abundance gloss near A' = 1, and an intermediate
  constant. NO verdict clause changed under repair (R1's
  assessment, re-confirmed clause-by-clause). R1's bonus
  measurement gamma_2(1e8) = 1.1711 adopted (decline toward the
  1.1505 asymptote continues).

## 3. Item state after Sessions A-D

The mandate's disjunction is discharged on the obstruction branch:
- Named obstruction per blocker with exact quantitative gaps
  (dossier Sections 4-6; F17.2-F17.8), the sharpest being the
  collision-constant closure F17.5 (E_even[S_2^2]/4 = 1.150481 vs
  critical 2 sqrt(2)/e = 1.040520; margin ratio 1.106) and the
  double-kill of D1.a (self-proved k-uniform Selberg constant,
  deficit exp((1+o(1)) L ln L)).
- Certificate layer extended: first b > 1 certificates (b = 3
  inline, hand- AND R1-verified; b = 5 same constellation; one
  constellation kills b in {1,3,5}); (7,7)/(8,8) frontier located
  at 1e9 with collision-calculus consistency; (6,6,64) 1 -> 29.
- The single residual (V4/F17.7): one HL-type matched-flank
  class-count lower bound at k ~ L; exclusion side pre-built by
  D1-L. Successor-item candidate.

## 4. Operator package (ACTION REQUIRED)

(a) R2 cross-family review (B2 architecture; cannot be run from
    this environment). Hand to a cross-family model EXACTLY these
    two files:
      payloads/item-0017-review-object-v1.md
        sha256 5a7a2647d11ec40d00b2d2ae2473bfdfd2a32a22ab731b7fe
        93dfe97b85fbb63
      payloads/item-0017-review-r2-payload-v1.md  (scope audit)
        sha256 f18f0bc02cc9808dbccb05ffbf014b2430d250bdce3be1c98
        da4a68805fdbdf6
    NOTE: the object is the SESSION-C state of the dossier (R1 and
    R2 review the same object; the post-R1 repairs are visible to
    the adjudication, not to R2 -- same-object blindness preserved).
    Optional per R1's confidence note: widen R2's file set with
    dossier/item-0017-workpapers/d1a-selberg.md (stripped) if you
    want the sieve-constant internals cross-audited.
(b) After R2 returns: adjudication (point-by-point disposition of
    R1+R2, v2 revision of the dossier if sustained findings
    require it) -- steering executes on request; then operator
    ratification of the verdict.
(c) Closure after ratification (NOT executed now): roadmap
    emit-patch (item-0017 done-move via the roadmap skill); ledger
    ANN append. Draft ANN body for your editing:
      "item-0017 Sessions A-D executed by steering lineage (Claude
      Fable 5, claude-fable-5, ultracode + workflows) in one run
      against kickoff v1 (sha 45591703..., operator-ratified;
      session-A STOP-AND-REPORT on the item-0010.md anchor delta
      ratified as re-pin to 66adc54). Branch item-0017: dossier
      e2prime-supply.md v1 (obstruction branch; D2 gate PASS;
      F17.1-F17.8; U17.1-U17.10), 14 anchored anatomies, committed
      workpapers (balance_stats, d1c_gamma2, d5b_deep,
      d1a-selberg 618-line self-contained k-uniform Selberg bound,
      strip_payload), D5 grid at 2e6..1e9 with the project's first
      b > 1 certificates, R1 blind computation audit (SOUND WITH
      REPAIRABLE ISSUES 0.89, zero fatal; all findings repaired,
      marked, registered). R2 cross-family + adjudication +
      ratification pending operator. K1 handshake honored (D0
      targets width 1 primarily; F17.1 converges with ANN-50 K1)."
(d) BET-07 relevance (resolve_by 2026-08-08, "unconditional
    progress", p = 0.03): this verdict is further evidence AGAINST
    unconditional progress (obstruction branch taken; the model
    gate PASS and the certificate layer are understanding progress,
    not unconditional theorem progress). Resolution is the
    operator's call, per the tate-transfer precedent.
(e) Bookkeeping flags for you: U17.5 (kickoff lists
    pc_wordcount.py, absent from the committed tree); U17.7 (first
    project use of PNT, P3.1' only); U17.10 (R-S equation numbers
    in d1a-selberg.md memory-cited; verify against the 1962 paper
    before any external circulation); payload hashes above not yet
    booked in payloads/HASHES.txt (operator-side sha256 canonical).
(f) Branch merge: item-0017 branch (5 commits) is ready for your
    review/merge at your discretion; main was never touched.

## 5. Follow-up candidates (none executed)

- Successor item: "matched-flank class-count lower bound" (the V4
  residual; adjudication-F2 anti-rigidity form; exclusion side and
  budgets pre-built).
- Executor slot: (7,7) first-pair hunt at 5e9-1e10 (segmented
  sieve).
- Lean extension layer (only if ever needed for consumption):
  weighted-(E2') generalization of ExchangeAt (per K1 and FW-1).
