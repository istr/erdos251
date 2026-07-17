# HANDOVER -- erdos251 (round 2 in motion, 2026-07-17; round 1 closed and scored 2026-07-15)

Mission: public experiment attacking Erdos #251 (irrationality of
S = sum p_n/2^n) with frontier LLMs; goal is insight, not priority.
Operator: istr. Steering: Claude Fable 5 (fresh instance reads THIS first).

## Read order for a cold start
1. This file. 2. ledger.yaml (append-only; ANN-01..49; bets: 6 scored,
1 open -- BET-07 to 2026-08-08). 3. dossier/chain-v1.md (v1.4, SIGNED
OFF -- the round-1 result), then dossier/tate-transfer.md (v2 -- the
round-2 unconditional-front verdict; adjudication at
payloads/item-0005-adjudication-v1.md). 4. dossier/triage-2a.md and triage-2b.md (R2 adjudications),
then triage-1b.md end (methodology register: blind spots 1-5, checklist
rules i-iv) and triage-1a.md. 5. runs/README.md rules 1-11.
6. roadmap: python3 /mnt/skills/user/roadmap-items/scripts/roadmap.py
list --arc research. 7. lean/README.md (layout map; inventory 1 --
its later sections carry a STALE banner, HANDOVER is the record).

## Round-1 record (closed, scored)
- Result: chain-v1 v1.3 -- conditional theorem "Hypothesis A (uniform
  HL-type tuple counts) + Hypothesis B (Cramer-Granville) => S
  irrational". THREE blind reviews, zero fatal (review-1 0.94, R2a
  ChatGPT 0.90, R2b Fable 0.88); all found gaps repairable-class and
  EXECUTED (v1.1: F1 i_0 off-by-one + F2 Lemma-4.2 span necessity;
  v1.2: R2a repairs incl. kappa-honest 4.2 sketch; v1.3: R2b repairs
  incl. effectivity declaration). Cross-arm disagreement set: EMPTY.
  Empirical layer independently re-executed and STRENGTHENED
  (denominator > 10^1050).
- Bets: BET-04 YES brier 0.1225; BET-05 NO brier 0.2025; mean brier of
  the four scored binary bets 0.183 (coin-flip baseline 0.25). The
  YES declaration = the formal v1.3 sign-off (ANN-25). Open: BET-06
  (implication already in literature, p 0.10 -- GATES ANY PUBLIC
  CLAIM, resolves via item-0004) and BET-07 (unconditional progress,
  p 0.03, to 2026-08-08).
- Lean: deterministic half (chain-v1 sections 2-3) MACHINE-CHECKED --
  Basic, ForkMerge, Chebyshev sorry-free; #print axioms on
  erdos_251_of_small_tail_fork_merge = the classical three; CI
  enforces this on every push (required axiom gate, confirmed green).
  Items 0001/0002/0012/0013 done.
- Methodology dividends, all ledgered: statement-formalization plus
  mandatory computation caught what prose review missed twice
  (F1/F2); computation-mandatory payloads produced both R2 findings;
  anchor-stripped review objects held blind; role-not-family (ANN-10)
  confirmed a second time on the review side; five blind-spot
  register entries with checklist rules (i)-(iv).

## Current state (round-2 opening position)
- item-0014 statement skeleton LANDED (main 5144918): Counting.lean
  with real definitions (deletion construction, 0-based handoff via
  prefix sums, kappa-parametrized interfaces) and 12 intentional
  sorried statements; four proved smoke tests reproduce the
  review-verified word tables; fourth independent F1 confirmation
  (121/121 over (J,K) in [1,11]^2). Steering transcription-fidelity
  review: PASS with documented deviations (ANN-26). item-0014 stays
  OPEN on its ratified acceptance letter: blind cross-review of the
  statement set BEFORE any proof investment.
- item-0003 stays ratified integrator; its floor (ANN-14, ii-a) is
  met except fork_merge_of_hypotheses -- the analytic heart, chain-v1
  sections 4-6, now with its full interface skeleton beneath it.
- item-0011 (Hypotheses faithfulness pair) contingent, unscheduled.
- Inventory on main: 16 sorries = 3 pre-existing residuals
  (Conditional 1, Hypotheses 2) + Statement 1 + Counting 12.
- Round-2 decisions ratified 2026-07-16 (ANN-27, followup27): fidelity
  arm instrument STAGED in runs/_staging_review3fid (payload
  review_3_fidelity, deterministic strip script, object Parts I-III,
  wrapper verbatim, config; steering hashes staged, operator sha256
  canonical); item-0015 (heart proof item) proposed and ordered after
  item-0004, double-gated; statement-unfreeze batch LANDED (unused hb
  dropped from repeated_block_quantization, ANN-18 deferral resolved,
  inventory unchanged); R2 archive gap CLOSED (a70390f transcript,
  b32759d strip-script restore).
- item-0004 DONE 2026-07-16 (ANN-28): literature verification via
  research-mode steering session; report at dossier/literature.md;
  BET-06 scored NO (brier 0.01) -- no prior art, niche unoccupied;
  item-0015 gate (b) cleared.
- item-0014 CLOSED 2026-07-16 (ANN-30): blind fidelity arm
  (claude-sonnet-5, runs/20260716_sonnet5_review3fid) FAITHFUL with
  documented deviations, 0.85, zero unfaithful; two new findings
  adjudicated (4.3 conclusion deviation-weaker flagged; 4.4 missing
  1<=Cg proved inert, C>=1 question routed to item-0011). Instrument
  lesson booked: deliver Phase B in turn 2 on future two-phase arms.
- chain-v1 at v1.4 (ANN-31, citation hygiene only; sha
  6bcb1425...78ec0b); the ANN-28 queue item is discharged.
  Sorry inventory unchanged: 16.
- item-0015 session 1 COMPLETE on branch item-0015-counting-proofs
  (f4cc82b, ANN-33): T1-T5 proved, Counting 12 -> 7, statements
  steering-verified byte-identical; canary positive (both Hypotheses
  sorries reduce to one summability obligation; one bridge lemma
  verified at pin, one unverified-at-pin). Inventory after merge: 11.
- s2 Chebyshev risk resolved in-tree: Chebyshev.lean has
  centralBinom_le (hard half); s2 extracts pi(x) >= c x/log x.
- item-0015 session 3 COMPLETE on branch item-0015-s3 (2dc3f65,
  ANN-39): T1 (C = 12) + Mertens pack M1-M3 sharp + T2 step (a) +
  k = 0 edge; Counting 4 -> 3; inventory after merge: 5.
- ANN-39 follow-ups (1)+(3) DONE (c5103a9 on main, ANN-40;
  steering-verified ANN-41): MP relocated verbatim to Mertens.lean
  (mathlib-only; upstream port = drop the namespace line + rename),
  primesUpto canonical with bridge primesLe_image / sum_primesLe_eq,
  prod_primesLe deleted (orphan); Counting -478; inventory 5
  unchanged; MP stays visible unqualified in Counting.lean via the
  import.
- runs/ report-archival convention RATIFIED (operator applied
  3855c9e).

## Pending decisions and gates (operator), round 2
1. DISCHARGED: the s3 chain is on main (operator rebase; lean tree
   preserved byte-wise, steering-verified ANN-41) and the ANN-39
   follow-up refactor landed at c5103a9 (CI green on main,
   operator-attested). Main is the pin lineage; no branch merge
   pending. Inventory on main was 5 = Counting 3 (exactly 4.2, 4.3,
   constr_consCount_pos) + Conditional 1 + Statement 1; session 4
   took it to 4 by closing 4.2 (see 2b), and session 5 took it to 2
   by closing 4.3 + constr_consCount_pos (see 2c).
2. Session 3 CLOSED: ACCEPTED (ANN-39) at 2dc3f65. Kickoffs v3
   (sha256 385c1e91...d463d) and v3.1 delta (sha256
   f2976d93...d2d67) both ephemeral, never committed. Landed: T1
   (C = 12, k = 0 exact via singularSeries_singleton_zero); Mertens
   pack M1-M3 sorry-free sharp (M1 c1 = log 4 via
   padicValNat_factorial + primorial_le_4_pow, N >= 1; M2
   coefficient EXACTLY 1, c2 = 1 + b/log 2 - lnln 2; M3 exponent
   EXACTLY 1, c3 = exp(c2 + 1); AbelSummation unused); T2 step (a)
   (nuMod_insert, log_singularFactor_insert_sub_le) and the k = 0
   edge discharged in Lean. Steering re-verified: lean/ diff
   anchor..tip = Counting.lean only, +531/-0; vs main +852/-1 (the
   one deletion = T1's sorry); strict inventory 5. NEXT GATE:
   kickoff v4 -- gates (a) merge and (b) refactor are DONE (c5103a9,
   ANN-40/41). DISPATCH DECISION (ANN-41): v4 is written in a FRESH
   steering session from this HANDOVER, anchored at the
   operator-side HEAD after the ANN-41 apply. Scope:
   T2 (b) collision primes < span, (c) split at
   k+2 (SMALL trivial via M3; LARGE = sieve-theoretic
   squarefree-divisor expansion with omega(d) counting, the
   substantial piece), (d) assembly; T3 five-term Bonferroni
   ledger; fork_merge stays s4/s5. Unfreeze candidates (4.1
   clause-2 budget x2, evenness x2 -- evenness is a genuine
   HLQuantA hypothesis, asymmetric drop) booked to the BET-04
   basket; no mid-arc unfreeze. Report archival convention
   RATIFIED (3855c9e; report sha256 3fc8e757...8bfe3).
2b. SESSION 4 (executor, this HEAD): LEMMA 4.2 CLOSED, T3 OPEN.
   Two commits, ANN-42 (T2) and ANN-43 (T3 core). Inventory 5 -> 4 =
   Counting 2 (4.3, constr_consCount_pos) + Conditional 1 +
   Statement 1. All three frozen statements re-diffed BYTE-IDENTICAL
   against the original pin c6c0b98 after both commits; axiom gate on
   erdos_251_of_small_tail_fork_merge unchanged (classical three).
   Rule 12 ran FIRST and cleared the route on the ACTUAL span formula
   at kappa in {1,10,48} (48 = the C_1 constr_consCount_pos feeds in,
   which the kickoff appendix never tested): zero violations, LARGE
   log-sum shrinks in k, error lands additive as booked.
   LANDED: 4.2 whole (b/c/d as designed, no route deviation);
   C_2(kappa) = 2 kappa mertensC3 exp((2 + log kappa/log 4)/2), let
   to fall out. Two kickoff steps proved UNNEEDED: (b) does not need
   p prime, and (d) does not need the evens-counting
   #oneExtensions <= D/2 -- the crude <= D closes. T1's
   "naive constant fails" precedent did NOT recur.
   ALSO LANDED (proof-layer, NOT a closure): T3 step 1's structural
   core -- isConsecRealization_of_primes, the next-prime
   characterization q_succ_eq_of_no_prime_between, the wordPointSet
   prefix-sum structure, and mem_oneExtensions_of_prime_shift with
   its parity/admissibility inputs. Both of the kickoff's flagged
   step-1 sub-claims are now machine-checked rather than asserted
   (odd offsets need no case; the inadmissible-t x_0 is cheap --
   a > |H|+1, i.e. sqrt x > L+2, suffices).
   T3 RESIDUAL, itemized for kickoff v5 (the five-term cut is
   CONFIRMED SOUND -- no defect; it is simply not a one-session item
   alongside T2, which is a capacity finding, not a route error):
     (1) step 1's Finset card inequality: consCount >= tupleCount H x
         - tupleCount H (sqrt x) - sum_t tupleCount (insert t H) x.
         The anchor map a |-> Nat.count Nat.Prime a is injective on
         the good set; the structural core above supplies the rest.
     (2) steps 2-3: HLQuantA both directions + this session's 4.2 +
         the modelMass (insert t H) x -> modelMass H x algebra (ratio
         of singularSeries, one power of log x shifted). Note 4.2's
         span/conclusion shapes line up with 4.3's hypotheses
         VERBATIM under k = L -- no bridging needed, confirmed.
     (3) step 4: tupleCount H (sqrt x) <= sqrt x + 1. No content.
     (4) step 5: the x_0 assembly. Needs TWO growth-rate limits --
         (lnln x)(lnlnln x)^2 / log x -> 0 and
         x exp(-c (lnln x)^2) >> sqrt x. Neither is hard mathematics;
         both are real Lean work. No hidden-coefficient risk (|H| is
         O(lnln x) here, not coupled to the summation the way MP-M2's
         dyadic blocks were).
   constr_consCount_pos: still booked near-free downstream of T3, but
   that remains the kickoff's ESTIMATE -- it sits behind a sorry and
   was not exercised. RECOMMEND: kickoff v5 scopes T3 alone.
   fork_merge_of_hypotheses untouched, as scoped OUT.
2c. SESSION 5 (executor, this HEAD): LEMMA 4.3 CLOSED (gate) AND
   constr_consCount_pos CLOSED (stretch). COUNTING.LEAN IS SORRY-FREE.
   Two commits, ANN-44 (T3 gate, 0ed44b4) and ANN-45 (stretch,
   6055300); ANN-46 records one structural flag. Inventory 4 -> 2 =
   Conditional 1 (fork_merge_of_hypotheses, s6) + Statement 1.
   Executor model: Claude Opus 4.8 (claude-opus-4-8[1m]).
   Gates: G1 lean/ diff pin..HEAD = Counting.lean ONLY (+439/-7, no
   import change); G2 all three frozen blocks byte-identical vs the
   ORIGINAL pin c6c0b98 (2a/2b minus their deleted sorries, which are
   the deliverable; 2c bystander untouched whole); G3 strict inventory
   2; G4 classical three on every new declaration AND on
   erdos_251_of_small_tail_fork_merge, no sorryAx in either target, no
   native_decide; G5 lake build green locally.
   Kickoff v5's route was built AS DESIGNED -- no deviation, so the
   pre-cleared rule-12 landing was not re-run, and no numeric smoke
   test of the balance was attempted (section 3 forbids it; x_0 is
   astronomical and nothing materializes it).
   ROUND'S FINDING (a simplification, not a repair): bounding
   ln(L+2) <= L+1 <= 4t ONCE collapses every ln(4t+2) factor the
   kickoff carried into a pure power of t = lnln x. The booked TWO
   limits + the y ln(y+2) monotonicity helper collapse into ONE
   limit, tendsto_pow_loglog_div_log ((ln s)^n = o(s), from
   Real.isLittleO_pow_log_id_atTop), used at n = 3 (ext fraction) and
   n = 2 (mass margin). No cfm2-style plumbing needed; L = 0 needed no
   case split, as booked. Step 4 needed no lemma (it lives in step 1).
   STRETCH RESOLVES ANN-43'S OPEN QUESTION: "near-free" was correct
   and understated -- 12 lines, no helpers, first try. cspan_le(3,4),
   cbudget(5) and cword_admissible plug into 4.3 VERBATIM. Retrospective
   vindication of v1.1/F2: the narrowed span is exactly what makes
   5(iii) plug in without adaptation.
   TWO ITEMS FOR STEERING (flagged, not repaired -- both unfreeze
   candidates for the BET-04 basket):
     (i) `oneExtension_sum_le` exports C_2 with NO SIGN (bare
         exists C_2). The assembly must clamp to max C_2 1 before any
         monotonicity step. Costless, but 4.2's proof builds
         C_2 > 0 and could export it; that is the cleaner statement.
     (ii) `q_eq_of_count` was RELOCATED upward (statement/docstring/
         proof byte-unchanged, pointer note left at the old site per
         the ANN-38/39/40 convention) because consCount_bonferroni is
         its first consumer and Lean needs it declared earlier. A
         second inline Nat.nth_count bridge was the one-line
         alternative and was REJECTED: the module docstring asserts
         "Glue proofs (flagged): q_eq_of_count only", and duplicating
         would have silently falsified a traceability claim. Residual
         nit: that docstring's "used only by the smoke tests below" is
         now stale in its "only" (the "below" still holds).
   COST NOTE: consCount_lower_bound needs set_option maxHeartbeats
   400000 -- the tree's first. Heartbeats are cumulative per
   declaration and this is one large assembly; the set_option precedes
   the frozen docstring per the ANN-26 `... in` convention, so the
   frozen block is untouched. Two isDefEq sinks were removed rather
   than papered over first (nlinarith on 3-way products -> explicit
   calc; let-bound H -> clear_value, since linarith atom comparison
   was unfolding wordPointSet into a Finset.image).
   NEXT: fork_merge_of_hypotheses (s6) is now the ONLY counting-layer
   consumer left -- the whole section 4-5 interface beneath it is
   machine-checked. item-0003's floor (ANN-14, ii-a) is met except
   exactly this one theorem.
2d. SESSION 6 (executor, this HEAD): FORK_MERGE_OF_HYPOTHESES CLOSED.
   THE ITEM-0003 FLOOR (ANN-14, ii-a) IS MET. Conditional.lean is
   sorry-free; chain-v1 sections 2-6 are machine-checked end to end.
   One commit, ANN-47 (0b831d7). Inventory 2 -> 1 = Statement 1
   (erdos_251_irrational, open by design -- the unconditional target).
   Executor model: Claude Opus 4.8 (claude-opus-4-8[1m]).
   THE MILESTONE PRINT:
     'Erdos251.erdos_251_conditional' depends on axioms:
       [propext, Classical.choice, Quot.sound]
   Hypotheses A + B => Irrational (sum_n p_n/2^n), no sorryAx.
   Gates: G1 lean/ diff pin..HEAD = Conditional.lean ONLY (+223/-1,
   the one deletion = the deliverable sorry; sole import change
   +import Erdos251.Counting, no cycle); G2 BOTH frozen section-2
   blocks byte-identical (sha256-compared) vs BOTH the pin 93efb35 and
   the ORIGINAL c6c0b98 -- an `open Filter in` line precedes 2a's
   docstring per the ANN-26 `... in` convention, so the block itself is
   untouched; G3 strict inventory 1; G4 classical three on
   fork_merge_of_hypotheses, erdos_251_conditional AND (unchanged)
   erdos_251_of_small_tail_fork_merge, no sorryAx, zero native_decide
   (the only two tree hits are prose saying "no native_decide");
   G5 lake build green locally.
   Kickoff v6's route was built AS DESIGNED -- zero deviations. The
   pre-cleared rule-12 landing (FM-1) was therefore not re-run, and no
   numeric smoke test of any x_0 was attempted (section 3 forbids it).
   FM-1 landed exactly as pre-cleared: 3*(23/20)^2 = 3.9675 < 4, i.e.
   the margin Lemma 4.4's factor 3 (vs 4) was designed to buy is real
   and is consumed here, with the one extra eventual threshold
   20 lnln x <= ln x (via the s5 dividend tendsto_pow_loglog_div_log
   at n = 1 -- that ONE limit now serves 4.2, 4.3 AND section 6).
   All three predicted ~10-line helpers were needed and sufficient.
   Two more were extracted for reuse rather than inlined:
   `count_sqrt_le_of_anchor` (the anchor/count bridge: sqrt x < q idx
   forces count(sqrt x + 1) <= idx; consumed 4x -- both tails, both
   FM-3 arms) and `ctail_le` (the FM-1 chain itself; consumed by
   tail_n and tail_m). Counting.lean untouched, so its .olean stayed
   cached and every probe built in ~5s: the s5 5-minute cycle did not
   apply, as the kickoff designed.
   THE NAME SWAP (kickoff trap 1, BET-04-flagged) COST ZERO: binding
   n_FM := b (the w'-anchor), m_FM := a (the w-anchor) as instructed
   made cword_fork's two clauses land as `.symm` on both fork goals,
   first try. Being told the orientation is what made it free; the
   trap register earned its keep.
   THE TRAP THE KICKOFF DID NOT PREDICT (candidate for runs/README,
   alongside the rule-13 scratch-file convention): after `refine` with
   five lambdas, the per-r goal keeps un-beta-reduced
   `(fun r => cJ Cg (X + r)) r`, so `set J := cJ Cg (X + r)` silently
   fails to fold it -- omega then sees TWO distinct atoms for J and
   four word-position side-goals fail with ~20-atom counterexamples
   that name nothing. One `show ForkMergeAt ...` to beta-reduce fixes
   all four. Opaque until seen, one line after. Same family as s5's
   isDefEq sinks: the cost is always in what the tactic silently does
   NOT match.
   NOTHING IS FLAGGED FOR UNFREEZE this session -- no statement,
   docstring or Counting.lean line was touched, and no ANN-46-style
   structural move was needed.
   NEXT (steering/operator, post-verification): re-execute G1-G4 on
   the diff; verify the milestone print; item-0015 done-move and the
   item-0003 floor-closure bookkeeping (item-0003's remaining
   acceptance clause -- blind cross-review -- was met by chain-v1's
   three reviews, so the done-move is an operator call, not new work);
   runs/README rule-13 candidate rides the same batch. The ONLY
   remaining sorry in the tree is the unconditional target itself.
2e. POST-s6 BOOKKEEPING (steering batch, followup28 + roadmap mbox;
   operator apply = ratification): steering re-executed G1-G4 on the
   diff -- lean/ = Conditional.lean only, both frozen blocks
   sha256-identical across pin/c6c0b98/HEAD (4805b8c3... /
   ab0d99ec...), inventory 1 at Statement.lean:21, zero native_decide
   in lean/ additions -- and verified the milestone print wording in
   ANN-47. item-0015 DONE and item-0003 DONE via the roadmap mbox
   (item-0003's blind-cross-review clause met by chain-v1 v1.3's three
   reviews, ANN-25). runs/README gains rule 13 (scratch-file probing
   against the built olean) and rule 14 (post-refine beta-reduction
   trap), both from s5/s6 executor practice. Open on main: exactly
   Statement.lean's erdos_251_irrational. Next research fronts per
   _order: item-0007 (refined A2 at loglog windows), item-0005 (TaTe
   transfer to growing numerators); item-0016 (Counting split) sits in
   its post-heart slot alongside the pin-bump and the MP
   upstream-port preparation.
2f. ITEM-0016 LANDED (steering-emitted mbox, dispatch (a); operator apply
   = ratification). Counting.lean is now a thin umbrella (module docstring
   and traceability table byte-identical) over seven themed modules in
   lean/Erdos251/Counting/: Words, SingularSeries, OneExtension, Lemmata,
   ConsecTransfer, GapTail, Construction. PURE relocation, cut A
   (order-preserving, zero moves): the seven bodies concatenated in the
   umbrella's import order reproduce the pre-split body byte-for-byte
   (f14032eb...507c86 at the split commit; af4615e1...5ea4388 once the one
   declared docstring amendment is applied). Re-checkable any time:
   `python3 lean/scripts/blocks.py relocation-check`.
   NEW STANDING RULE, replacing the kickoffs' path+line frozen checks:
   frozen blocks are addressed BY DECLARATION NAME via
   lean/scripts/blocks.py check-frozen against lean/frozen-blocks.yaml
   (erdos_251_irrational, HLQuantA, CramerGranville). `open ... in` /
   `set_option ... in` lines sit outside the block (ANN-26). Kickoff
   templates: cite the decl name, never Counting.lean:NNN.
   The G2 gate shape for future relocations is the concatenation check, not
   a path diff.
2g. ITEM-0005 COMPLEX CLOSED (2026-07-17; full record ANN-49). Paper
   payload layer first (bf5de42): eight arXiv full texts sha256-anchored
   by URL in payloads/HASHES.txt, local PDFs gitignored under dossier/.
   Verdict dossier/tate-transfer.md: v1 3185181 -> two blind adversarial
   reviews (R1 Fable fresh-role: zero defects, sharpenings contributed;
   R2 ChatGPT cross-family: four scope overclaims sustained, the EXCH'
   generalization contributed) -> adjudication
   payloads/item-0005-adjudication-v1.md -> v2 8517b8b -> fixup 7293d75
   -> item-0005 done 25859d1. Result: NO unconditional TaTe transfer in
   the eight-text evidence base, failure structural; O1-O4 with scope
   qualifiers; one-generator rigidity; unconditional residue localized
   to (E2') (EXCH' sufficient, necessity lattice-layer-relative;
   EXCH_1 => item-0010); blocker register pigeonhole/parity/Shiu;
   certificates (5,5,34) and (6,6,64). Roadmap consolidation d97d40a:
   item-0007 (bd1480f), item-0008, item-0009 retired as subsumed
   (summaries carry the evidence); item-0017 created ratified ((E2')
   supply, successor of item-0008 / adjudication-F1); order
   item-0017 -> item-0010 -> item-0006. NOTE the two F-numberings:
   verdict Section 8 F1-F6 (follow-up basket; F3 = item-0010 re-scope,
   F2 = anti-rigidity counting target inside item-0017's frame, F5 =
   lemma bank, settled) vs adjudication F1-F3 (F1 -> item-0017).
   Steering blind-spot register grew by B1 (kickoff language-discipline
   deferral) and B2 (review-role complementarity) -- adjudication
   Section 5. Workpapers COMMITTED under dossier/item-0005-workpapers/;
   literature.md item (b) superseded, ERRATUM-4.
3. Pin policy (ANN-36): mathlib pin STAYS at a6276f4c -- master also
   lacks Mertens (verified 2026-07-16); MP is built in-session;
   post-heart pin-bump item proposed on operator word; MP is an
   upstream-contribution candidate after close.
4. Infrastructure (suggested, from the s2 incident): pre-seed agent
   worktrees with .lake/packages -> shared read-only +
   private .lake/build; consider write-protecting
   /opt/erdos251-lake/packages.
2. BET-07 resolution by 2026-08-08 (operator judgment); evidence base
   COMPLETE: tate-transfer.md Section 1 BET-07 paragraph, both blind
   reviews concur AGAINST (understanding progress, not theorem
   progress).
2b. item-0010 re-scope to EXCH_1 (verdict Section 8, F3): strictly
   easier target, certificate-backed at small depth -- operator word
   pending; steering emits the roadmap update on ratification.
3. OPTIONAL (operator): public thread post now unblocked (BET-06 NO;
   do NOT inherit the problem page's [Er58b] all-k attribution; the
   thread already carries AI-assisted mathematics, ANN-29) and/or set
   the could-be-formalisable / working-on-formalising flags on the
   problem page (both currently None -- minimal-footprint public
   claim); alerts per report recommendation 1 (arXiv math.NT
   irrationality+prime+2^n; erdosproblems.com/251 watch) PLUS the
   LLM-hunter repo (ANN-32): poll
   github.com/mehmetmars7/Erdosproblems-llm-hunter for commits
   touching attacks/erdos/ or docs/data/erdos_data.js on id 251 --
   the rendered page is a JS shell, blind to fetchers. Contamination
   note: that venue is public LLM-generated #251 material; web-ON
   runs must treat it as such.

## item-0004 RESOLVED (2026-07-16)
Full report: dossier/literature.md (ANN-28; original artifact
operator-held). All ten list items verdicted; BET-06 scored NO
(brier 0.01, binary mean 0.183 -> 0.149). Forum verbatims RESOLVED by
operator browser check (ANN-29; addendum in literature.md): Tao and
Alfaiz confirmed, Vjeko_Kovac telescoping post + reply now verbatim,
steering re-executed the algebra. Still UNVERIFIED: Hardy-Wright
theorem number (physical volume), Pratt Conjecture 1.2 numeric window
(full-text check). CPAP-3 and Erdos #251 confirmed OPEN; no prior art
for the target implication; 0 claimed proofs on the page.

## Steering sandbox notes (empirical)
- Background processes do NOT survive tool-call boundaries; container
  can be DOWN whole turns (rule 9 register, incident 2026-07-13/14):
  probe once, stage textually, ship on recovery.
- Egress blocks and the toolchain workaround recipe: lean/README.md.
  These are SANDBOX-specific; the executor machine builds locally
  (elan + cache work there), so local lake build is a real gate.
- lake update strips the trailing newline of lean-toolchain; restore
  before committing. Sorry inventory: grep -cE '^\s*sorry\s*$'.
- Lean elaboration traps, cumulative: dot-notation s.image f
  elaborates f before s (use explicitly typed functions);
  summable_nat_add_iff .mpr needs (f := ...); nlinarith heartbeats
  are cumulative in assembled proofs; congr 1 auto-reduces
  Nat-subtraction exponents (prefer omega rewrites); `open scoped
  Classical in` must PRECEDE the docstring (ANN-26).

## Protocol essentials (learned the hard way)
- Operator-side sha256 is the ONLY canonical integrity layer; model
  self-hashes reliable only WITH tools; never demand tool-dependent
  outputs in tool-less environments.
- claude.ai normal chats are never class-clean for this operator
  (memory); incognito or API for stage runs; ChatGPT temp chats for
  cross-family reviews; Gemini demoted (ANN-08). Displayed reasoning
  threads are DERIVED renderings -- trace_artifact_layer register,
  runs/README rule 11.
- Reviews: computation-MANDATORY payloads (review_2a pattern);
  anchor-stripped objects with deterministic, committed strip
  scripts; reviewer gets EXACTLY payload + object; web OFF; wrappers
  verbatim in configs (German wrapper flips outputs, Q5).
- Patches: git am -3, mboxes erdos251-followup2..26 in order; roadmap
  changes via the skill's emit-patch against a baseline snapshot
  taken BEFORE the move; steering author string
  "Claude Fable 5 (steering) <fable5-steering@localhost>".
- Kickoffs: ephemeral, byte-exact against a pin, path-scoped validity
  predicates (bookkeeping must not false-alarm the executor); M2
  completion-report shape (Gates verbatim / Observations / Follow-up
  candidates) is standing; closure ANNs carry the executor model.
- Checklist (triage-1b register, rules i-iv): extreme family members;
  integrality/positivity/sub-1-mass corners; flag unstated
  load-bearing steps; RE-EXECUTE every claimed direct computation --
  including amendment-adjacent lines; reading is not verification.

## Experiment questions snapshot
Q2 kernel ordering unchanged (chain-v1 8.1). Q3: route diversity is
sample-level; the two R2 arms found the same defect via different
witnesses. Q4: formalization pressure is itself a review instrument
(F1/F2, the 4.2-sketch constants); briefing = route lock. Q5:
language sampling-level (wrapper effects, steering-thread diglossia
datum, layer undetermined); anchor propagation is real and
anchor-stripping works; confabulated checksums vs honest declines;
calibration now has NUMBERS (review confidences 0.94/0.90/0.88 vs
finding counts; operator brier 0.183). Traces live in the private
trace repo; sha commitments in run configs; artifact layers per
rule 11.
