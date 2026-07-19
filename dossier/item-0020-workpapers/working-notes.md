# item-0020 W0 working notes -- continuity record and the four
# binding surfaces (kickoff v1 Section 3, W0)

Run: item-0020 (RelExtensionUpper / B2.reduced proof campaign),
executor lane, Claude Code on the operator machine; model string
claude-fable-5 (Fable 5), reasoning high. ASCII only; English only.
Web OFF (corpus-only per the kickoff Section 2 evidence firewall);
local code execution permitted (runs/README rule 6).

## 0. Pin and anchor record (rule 17/18; kickoff Section 0)

git rev-parse HEAD at session start =
17deadb3bb5c4207e63d93744ea0e1b043a710ed = the Section 0 pin of
kickoff v1 EXACTLY. No bookkeeping delta; the rule-18 clause and the
PARALLEL-0022 clause were NOT exercised (HEAD == pin, zero commits
ahead). Worktree pristine except the ephemeral operator kickoff file
(item-0020-kickoff-v1.md, repo root; never committed, not a run
write, per its own header and kickoff Section 5).

All nine Section 2 anchors verified byte-identical (sha256, session
start; full digests [audit repair: the draft's abbreviated
fragments were partly mistranscribed -- the PASS verdicts were and
are correct against the full digests below]):

  3577b92dbdb3e5b832aa3c89654056276b0cd22a0270f077ec06a16eb60cfdbe
    dossier/relext-statements.md                              PASS
  d233d2331fde561200cc83b6281209db7bbf8d632a6ddf33c9167ffca33d78fd
    dossier/item-0019-workpapers/item-0019-final-report.md    PASS
  229e43e2f9f63f0846b2ca1bcf57aa38a49a8a624860c9a1dc4005a66ca9a2cb
    dossier/item-0018-workpapers/item-0018-final-report.md    PASS
  129b39fbd2926e7e8ab56a26ac85d84bfc148dde97779ad04ef2809ba946530d
    dossier/item-0018-workpapers/budget_sheet.py              PASS
  e4e070d721f564dd728ffb4a633a00ef476bca08e739dd37ad9aa8fbc4cfd302
    dossier/item-0018-workpapers/budget_sheet_tables.txt      PASS
  27ac8e4f88c7016d4c3e67cd9590ad252faefbc0332b7fad42dea67bc349b8a1
    dossier/item-0019-workpapers/tables/m1_class_sizes.txt    PASS
  a688bf886ba54eacf280a43e4ce0df3a32776af210a95d734e61933bdd0ccb53
    dossier/item-0019-workpapers/tables/m2_concentration.txt  PASS
  22f6dc689d04abde0751e254cde7988a4409d7ec49f44b8cddcf98543bb17237
    dossier/item-0019-workpapers/tables/m3_rho_census.txt     PASS
  a8fd55c127e68adce100acb2c7ec301145c9bc698653f311374f868ed42092f9
    lean/Erdos251/Supply.lean                                 PASS

Kickoff disk hash (operator-side booking canonical; recorded for the
apply):

    sha256(item-0020-kickoff-v1.md) =
      a2c21d490e1f7b3a7b92e6752508f4827eb890e38ff05332b763f63fe3229f63

Session-start validity predicates (all PASS; re-run at close):
    blocks.py check-frozen    -> "FROZEN BLOCKS: all byte-identical."
    blocks.py relocation-check-> "RELOCATION CHECK PASSED"
    sorry census              -> exactly Statement.lean:1, rest 0
    mathlib pin a6276f4c...   -> intact in lean/lake-manifest.json
    lean-toolchain            -> ends "v4.16.0\n" (trailing newline
                                 intact)

## 1. Binding surface 1 -- the target (verbatim,
## dossier/relext-statements.md Section 7.1)

    RelExtensionUpper  (= B2.reduced):
      forall eps > 0, exists x_4(eps), forall x >= x_4, forall s,
      forall selections (d_P):
        sum over P of (N_{P,d_P} - 1)_+ <= eps * sum over P of N_P.
      [The o(ln x)/ln x gate is stated as the clean relative-eps form;
      C_F(x) = eps ln x recovers the kickoff display.]

All counts on T = S'^{(s)}_x per RS.1 (filters-first, caps inside).
The adversarial selection quantifier is load-bearing. FL-1 (item-0018
M2 report F1): the PRIMARY proof burden is the RESTRICTED selection
form -- selections range over d with Even d, 2 <= d,
(d : R) <= wbound x -- exactly the hypothesis supply_of_triple
consumes (lean/Erdos251/Supply.lean, RelExtensionUpper's hrestr
clause). An unrestricted proof is declared if obtained.

## 2. Binding surface 2 -- the gate (verbatim, item-0019 final
## report Section 6, the FIXED-DELTA verdict)

    "On these data A3 is plausible AT FIXED delta, and the gate
    item-0020 must clear is the FIXED-DELTA gate:

        RelExtensionUpper with C_F(x) = o(ln x), quantitatively
        C_F(x) <= (1 - eps) (delta/2)(1 - eps_C) ln x,

    with eps_C measured ~0 (Section 5.4).  The coupled gate C_F(x) =
    o(delta(x) ln x) is NOT forced by any measured decay."

Honesty caveat carried verbatim (E3 of the kickoff): "at 1e9 the
measured C_F/ln x (~0.24) exceeds the measured
(delta_emp/2)(1 - eps_C) (~1.2e-3) by two orders -- the exclusion
inequality is far from closing at reachable x; what the campaign
certifies is the DIRECTION of both terms (delta rising, C_F/ln x
falling), not a finite-scale closure."

## 3. Binding surface 3 -- the D3(i)-(vi) question list (verbatim,
## dossier/relext-statements.md Section 9)

    (i)   k!/2^k/exp(k log k) growth;
    (ii)  secretly at least as strong as an open HL uniformity
          (compared against frozen HLQuantA verbatim);
    (iii) caps inside the count from the start;
    (iv)  unproved tensorization (U17.11(a)) or growing-k
          compounding (U17.11(b)) presupposed;
    (v)   marginal statistics used as window statistics;
    (vi)  finite measurement treated as an asymptotic constant.

## 4. Binding surface 4 -- the 7.4 slack ledger (verbatim,
## dossier/relext-statements.md Section 7.4)

    "In C_F-form the contradiction of 7.2 reads: rigidity would force
        C_F(x) >= (delta/2) ln x.
    So the o(ln x) gate is consumed, in order:
      (s1) the A-side proportionality delta/2 (MatchedFlankLower's
           constant; a fixed positive factor);
      (s2) the C-side retention: if the A- or B-side proofs detour
           through window-only counts, C1's (1 - eps_C) multiplies
           delta (eps_C < 1/2 suffices: the design never needs o(1)
           retention);
      (s3) the B3 exceptional mass, if B3 replaces B2.reduced: needs
           eps_B3 <= delta/4 (coupled gate);
      (s4) the threshold truncation: absorbed in x_2(s) (A2's -s
           term), never in the constants.
    ITEM-0020's REAL TARGET CONSTANT (the answer the kickoff
    demands): prove RelExtensionUpper with ANY C_F(x) = o(ln x);
    quantitatively, C_F(x) <= (1 - eps) (delta/2) (1 - eps_C) ln x
    for some eps > 0 already closes with A3's delta."

## 5. Vocabulary dictionary fixed for this run (RS.1 / D0.3 / ANN-50)

All counts are RS.1 on T = S'^{(s)}_x unless labeled otherwise.
Pair-count dictionary against e2prime-supply D0.3 (both worlds
ordered, D0.3 includes the diagonal; RS.1-derived sums are
off-diagonal):

    W2(x)  := sum_P sum_d N_{P,d}(N_{P,d} - 1)   =  C_words,off
              (ordered site pairs n != m, equal FULL word)
    V2(x)  := sum_P N_P (N_P - 1)                =  C_sides,off
              (ordered site pairs n != m, equal SIDES)
    cap_r  := the P3.3'(iv)-pattern simplex capacity at r even
              positions inside the window budget:
              #tuples <= C(floor(A' L ln x / 2), r)
                      <= ((e A'/2)(L/r) ln x)^r;
              cap_{J+K} = ((e A'/2 + o(1)) ln x)^{J+K} = x^{o(1)}
              (side capacity), cap-analog at r = L for full words:
              |W_L| <= ((e A'/2 + o(1)) ln x)^L = x^{o(1)}.

Index dictionary: ANN-50 / T6 as fixed in relext-statements Section 2
and Supply.lean's module header (Lean gap k = paper g_{k+1}; the
middle is gap (n+J); delta carries no shift). No code in this run
touches gap arrays (no measurement campaign; the budget sheet is
symbolic), so the dictionary is consumed for statement fidelity only.

## 6. Session plan note

Single-session execution of the kickoff's package order W0-W5 (the
cut is the executor's per Section 6; item-0018 precedent "Section 9
split honored in one run"). W1+W2 close with the priority order
BEFORE any proof investment; W3 invests only in GO/REDUCED lanes;
adversarial verification (workflow fan-out, refuter discipline, the
project's 3.5-pass pattern) runs over every new proved claim before
it enters dossier/relext-upper.md.
