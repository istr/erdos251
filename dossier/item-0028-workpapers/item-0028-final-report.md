# item-0028 final report -- class-restricted Kuperberg 1.2 cost: budget-sheet decision

Lane: EXECUTOR (local). Executed against `item-0028-kickoff-v1.md` v1
(ephemeral dispatch, never committed; the operator apply is the
ratifying commit). Section 0 pin
`9e1206a037342e0a99d53ac440ec86fee703663e`.

---

## 0. Pin and rule-18 delta

At session start `HEAD` equaled the Section 0 pin exactly:

```text
$ git diff --name-only 9e1206a037342e0a99d53ac440ec86fee703663e..HEAD
(empty)
$ git rev-parse HEAD
9e1206a037342e0a99d53ac440ec86fee703663e
```

No content-path delta, no bookkeeping delta: rule-18 check trivially
holds (empty diff). All Section 2 read-only anchors were verified
byte-identical against `payloads/HASHES.txt` (or the git blob at the
pin, for the two anchors not hashed) before any write; see Section 2
below.

---

## 1. Gates at start and close

Gates at session start (all green):

```text
python3 lean/scripts/blocks.py check-frozen        3x OK, byte-identical
python3 lean/scripts/blocks.py relocation-check    PASSED
grep -rnE '^\s*sorry\s*$' lean/Erdos251/           lean/Erdos251/Statement.lean:21 (exactly one)
grep -c a6276f4c6097675b1cf5ebd49b1146b735f38c02 lean/lake-manifest.json   1
tail -c 1 lean/lean-toolchain | od -c              \n
python3 scripts/ledger_check.py relocation-check   PASS
python3 scripts/ledger_check.py validate           PASS (87 entries, 13 bets, 4 grandfathered malformed refs)
python3 scripts/writeup_mapper.py check --manifest writeup/sources.yml  PASS
python3 scripts/mathjax_lint.py                    141 files, 0 problems
roadmap.py show item-0028                          status: ratified
```

Roadmap tool invocation note: the dispatch names
`.claude/skills/roadmap-items/scripts/roadmap.py` (Claude Code tree);
at this pin that path does not exist -- only
`.agents/skills/roadmap-items/scripts/roadmap.py` is present in the
tree, and `.claude/skills/roadmap-items/` holds only `SKILL.md`. This
is an environment mismatch against the dispatch's "both trees exist at
the Section 0 pin" assumption, not a validity-predicate failure: the
`.agents/` copy is the live roadmap tool this repository uses (per the
`roadmap-items` skill), and it was used throughout this session for
every roadmap read and the closing `done` call. Recorded here rather
than silently substituted.

Gates at close (all green; re-run after Sections 3-7 landed, incl. the
ledger triple and mathjax_lint over the new files):

```text
python3 lean/scripts/blocks.py check-frozen        3x OK, byte-identical
python3 lean/scripts/blocks.py relocation-check    PASSED
grep -rnE '^\s*sorry\s*$' lean/Erdos251/           lean/Erdos251/Statement.lean:21 (exactly one)
grep -c a6276f4c6097675b1cf5ebd49b1146b735f38c02 lean/lake-manifest.json   1
tail -c 1 lean/lean-toolchain | od -c              \n
python3 scripts/ledger_check.py relocation-check   PASS
python3 scripts/ledger_check.py validate           PASS
python3 scripts/ledger_check.py append-only --base 9e1206a037342e0a99d53ac440ec86fee703663e  PASS
python3 scripts/writeup_mapper.py check --manifest writeup/sources.yml  PASS
python3 scripts/mathjax_lint.py                    143 files, 0 problems (incl. new files)
ASCII check                                        0 non-ASCII bytes across all new dossier/item-0028-workpapers/ files and the ANN file
re-run stability                                   two runs of class_restricted_sheet_28.py produce byte-identical tables files (verified)
roadmap.py show item-0028                          done (this apply)
```

STOP conditions: all reported below (Section 8); none fired.

---

## 2. Section V-A and V-B

### Section V-A -- verification of `pintz10-source-defects.md` against the
graded extracts (completed BEFORE any Section 3-4 artifact was
authored)

| row | outcome | note |
| --- | --- | --- |
| A1 | CONFIRMED | both sha256 in the workpaper's Section 0 match `payloads/HASHES.txt` lines 27 and 82 exactly (`f730b045...` for 1004.1084v1, `74824028...` for 1004.1072v1); both URLs match |
| A2 | SUPPORTED-WITH-INFERENCE | `pintz10-patterns.md` Section 2.1 confirms the Lemma 2 lead-in ("For fixed nu r", no comma), exponent digit 2, and the absence of `\|D\|=nu` under the sum, verbatim. The "(2.8)" / "(2.9)" equation-number identification of the r=1 remark's "similarly to (2.9)" is an inference from the extract's own sequencing (Lemma 1's display, then the Gallagher-analogous remark, both preceding Lemma 2's (2.10)); the extract does not print explicit "(2.8)"/"(2.9)" tags on Lemma 1's own displays, matching the row's own expected outcome |
| A3 | CONFIRMED | the reconstructed general-r statement (`sum_{D subset [1,H], \|D\|=nu} S^r(D+) <= c_8(nu,r) H^nu`) matches `pintz10-patterns.md` Section 6's boxed display exactly. Signals 2 (falsity), 3 (the proof), 4 (the r=1 remark) are all present in Sections 2.1/2.3/6 of the extract; signal 1 (notation) is the workpaper's own argument, consistent with but not independently sourced from the extract's own notation (`S(nu,r)`, `c_8(nu,r)`, `H_0(nu,r)`, all present in 2.1) |
| A4 | STALE BY SUPERSESSION, as expected | the register row R1-015 the workpaper cites was withdrawn as an instrument (ANN-20260727-77); not checkable as written, not CONTRADICTED. The mathematical content (Lemma 2 cites the general-moment claim correctly) survives via the graded extract |
| A5 | CONFIRMED | `pintz10-patterns.md` 2.3's (2.12) restores the limits `i=1..nu` on Delta (product over the nu elements of D only); `pintz10-singser.md` Section 3's (2.1) has Delta over `i=1..k` (all k elements of calH). The nu'_p bookkeeping consequence is elementary algebra, independently re-derived: if p\|h and p does not divide the nu-restricted Delta, h occupies the anchor residue class 0 mod p (already counted), so nu_p' = nu_p, not nu_p+1 as the printed test would assign |
| A6 | CONFIRMED, pending 3.2 (below) | `pintz10-patterns.md` 2.3 carries (2.16) as transcribed with the "extract's own step" cancellation note; `pintz10-singser.md` Section 3's (2.7) evaluates to exactly 1, matching the claimed "two independent routes to the same exact value" |
| A7 | CONFIRMED | `pintz10-singser.md` Section 2 (Theorem 1 = (1.6), Theorem 1' = (1.7)/(1.8), both Remarks) matches the workpaper's threshold table exactly; `pintz10-patterns.md` 2.3's "we will not mark the dependence ... on t and r" is present verbatim |
| A8 | CONFIRMED | `pintz10-singser.md` Section 2's second Remark verbatim: "... in most other applications for problems involving small gaps between primes and almost primes we need just lower estimates for the singular series" |
| A9 | IMPRECISE, as expected | `pintz10-singser.md` Section 4 has the `[Pin]` reference line verbatim, no identifier beyond "preprint". But (1.4) is DEFINED within 1004.1084v1's own Section 1, not proved by resting on `[Pin]`; `[Pin]` is cited only as having shown (1.4) for a *particular* calH_k, while Theorems 1/1' (which go "beyond (1.4)") are proved independently in the note's own Section 2. "its (1.4) ... rests on it" overstates the dependency. File not edited (leave-and-document) |
| A10 | recorded, read | Sections 6 and 8 residual claims read for internal consistency; no anchor check required by the row's own terms |

No V-A row lands CONTRADICTED. r28.3 does not fire on the V-A pass.

### Section 3.2 -- recheck re-execution

`pintz10-2-16-recheck.py` re-executed from its landed directory
(`dossier/item-0028-workpapers/`). stdout identical to the landed
`pintz10-2-16-recheck.txt` except line 2, the tool-version line:
landed says `sympy 1.14.0, mpmath 1.3.0`; this session's environment
has `sympy 1.13.3, mpmath 1.3.0`. Every other line, including the
series-expansion coefficients, the r=1 exact-identity check, and the
numerical spot checks at p=101 and p=10007, is byte-identical. r28.3
does not fire (a version-line difference is the one permitted
exception, named in the dispatch).

### Section V-B -- verification of the sheet's governing displays

| row | outcome | note |
| --- | --- | --- |
| B1 | CONFIRMED | `kuperberg22-singseries.md` Section 1, eq. (2), verbatim match |
| B2 | CONFIRMED | Section 2, Theorem 1.2 and eq. (5), verbatim match |
| B3 | CONFIRMED | Section 8, the "as desired" conclusion line and Lemma 2.1's (20), verbatim match |
| B4 | CONFIRMED | `kowalski-singser-dist.md` Section 2.4 (Example 3.5), the parity-vanishing sentence, verbatim match |
| B5 | CONFIRMED | Section 2.4, the mu_k(2) Euler product and the five printed numerical values, verbatim match |
| B6 | CONFIRMED | Section 2.5, Proposition 4.1 and Example 4.3, verbatim match |
| B7 | CONFIRMED | `pintz10-patterns.md` Section 2.3, the (2.11) display and the "we will not mark the dependence" sentence, verbatim match |
| B8 | CONFIRMED | Section 2.3, the (2.12) conventions (y, P, Delta) and the (2.16) display with exponent r, verbatim match |
| B9 | CONFIRMED | Section 6, the reconstructed general-r boxed display, verbatim match |
| B10 | CONFIRMED | `pintz-constants.md` Section 3.0, the star identity `1-(Pi_3 factor at p) = nu_p/((p-nu_p)(p-1))`, PROVED status, verbatim match |
| B11 | CONFIRMED | `literature-consolidation.md` Sections 0 (E4 table, all four columns at all four scales) and 5 (H3, "WEAKENED but still cheap ... must recover more than the draft assumed"), verbatim match |
| B12 | CONFIRMED | `pintz-constants.md` Section 4 grid table (5.3503/5.6990/6.0922/6.4403 displayed, 7.0158/7.3644/7.7577/8.1058 honest, 7.0287/7.3751/7.7638/8.1084 exact) and Section 3 F17.9 self-check values (6.1430/6.9320/7.9443/8.9629 vs 6.143/6.932/7.944/8.963 anchored), verbatim match |

No V-B row fails to be byte-present in its named extract. r28.5 does
not fire.

---

## 3. The landing record

Destination: `dossier/item-0028-workpapers/`. The three files were
held untracked in the executor working tree under
`dossier/item-0022-workpapers/` since 2026-07-26 and moved byte-exact
(no content change; hashes below match the Section 3 steering-expected
values):

```text
223465daa26d14129c19b563919d73fe045e1351291ca2ec32725cd4ed7bc8ba  pintz10-source-defects.md
85c9db73c32af52c927f163d782802de2e4e07d7892567d2f6c295251cc81f88  pintz10-2-16-recheck.py
2524cc7cd1da822272dbe55a81fbd60547736f8a6fa787ff0fafab18eb999f2f  pintz10-2-16-recheck.txt
```

`pintz10-landing-note.md` was written byte-exact per the dispatch's
Section 3.3 template. Supersession list, restated in one line each
(full text in the landing note):

- header "NOT COMMITTED" / Task D verification-status sentence --
  discharged by this session's re-verification against the graded
  extracts (Section V-A above) instead of the named item-0022 repair
  dispatch r1 Task D path, which never ran.
- Section 1, instrument I2 row ("the gap that r1 Task D closes") --
  closed by the graded extract instead.
- Section 2 support-class clause ("pending confirmation against the
  anchored bytes") -- confirmed via the graded extract (ANN-83).
- Section 2 consequence / Section 6 first bullet -- the item-0022
  verdict register they address was withdrawn as an instrument
  (ANN-77); the general-r reading survives via the graded extract.
- Section 6 ("item-0031 is proposed and unscheduled") -- item-0031 was
  withdrawn (ANN-77).
- Section 8 item 1 -- discharged as above.

Label collision booked: the workpaper's own "S1" (its Section 4) is
cited throughout this session's artifacts as "the (2.16) sharpening",
never as bare S1, to avoid collision with the project-level separator
S1 of `separator-repricing.md` W4.S1.

---

## 4. Sheet results

Full tables in `class_restricted_sheet_28_tables.txt`; the headline
figures are reproduced here with support class in place.

### S1 self-checks (all PASS; no r28.4 fire)

- S1a: F17.9 reproduced to 3dp at all four scales (6.1430/6.9320/
  7.9443/8.9629 vs anchored 6.143/6.932/7.944/8.963).
- S1b: K1.2 displayed/Mertens-honest/exact triple reproduced to 4dp at
  all four scales, exact product recomputed from a sieve (not
  copied): 5.3503/5.6990/6.0922/6.4403 | 7.0158/7.3644/7.7577/8.1058 |
  7.0287/7.3751/7.7638/8.1084.
- S1c: Kowalski mu_k(2), k=2..6, Euler product over primes p < 2e6 at
  dps 40 (ANN-74 method), reproduced to every printed digit: mu_2(2) =
  2.30096154471322 (2.300...), mu_3(2) = 6.03294567320657
  (6.03294...), mu_4(2) = 17.5624600163967 (17.562...), mu_5(2) =
  55.2550578033345 (55.255...), mu_6(2) = 184.18159739066 (184.18...).
- S1d: the Section 3.2 recheck re-run, PASS (version line only
  difference).

### S3 -- unrestricted references (relative to 1)

| column | x=1e8 | x=1e20 | x=1e100 | x=1e1000 | class | support |
| --- | --- | --- | --- | --- | --- | --- |
| C3a (K1.2 Mertens-honest) | 7.0158 | 7.3644 | 7.7577 | 8.1058 | GC-ITLOG | MEASURED |
| C3b ((4/ln2) lnln(3L)) | 6.7619 | 7.2312 | 7.7823 | 8.2883 | GC-ITLOG | MEASURED |

C3a carries no Section 3.4 annotation (that annotation is scoped to
Pintz Lemma 2 of 1004.1072v1 only); Kuperberg 1.2 is "unrefereed-
preprint" venue class on its own account. C3b carries two caveats: the
O(k) additive term makes per-scale values indicative only (the
deliverable is the growth class), and the venue is an unrefereed
ETH-hosted note.

### S4 -- class-family forced profile

C4a (parity main term, PROVED, DETERMINISTIC -- fixes the loss
normalization, not itself loss): at t=L+1 the expo is exactly 2r at
every scale (identity); at t=L_ceil+1 it descends toward 2r as scale
grows:

| | x=1e8 | x=1e20 | x=1e100 | x=1e1000 |
| --- | --- | --- | --- | --- |
| t=L+1, r=1 | 2.0000 | 2.0000 | 2.0000 | 2.0000 |
| t=L+1, r=2 | 4.0000 | 4.0000 | 4.0000 | 4.0000 |
| t=Lc+1, r=1 | 7.3752 | 5.9727 | 4.7151 | 4.0290 |
| t=Lc+1, r=2 | 14.7505 | 11.9453 | 9.4302 | 8.0580 |

C4c (pointwise worst odd-prime profile, PROVED, finite computation):

| | x=1e8 | x=1e20 | x=1e100 | x=1e1000 |
| --- | --- | --- | --- | --- |
| expo | 4.6754 | 5.0215 | 5.4101 | 5.7547 |

Class GC-ITLOG (the sum over odd primes p <= k^3 grows like lnln
k^3). Conclusion: pointwise, restriction to the class family changes
the p=2 factor from rare-event to main term and changes nothing else
in the growth class.

### S5 -- the one located cardinality-restricted mechanism

C5a (split-point coverage, MEASURED-exact; y = ln(h)/2, the 1004.1072
convention):

| x | y | primes<=y | pi(y) | share of full Mertens mass |
| --- | --- | --- | --- | --- |
| 1e8 | 2.7240 | [2] | 1 | 0.2851 |
| 1e20 | 3.3188 | [2, 3] | 2 | 0.4304 |
| 1e100 | 4.2990 | [2, 3] | 2 | 0.4086 |
| 1e1000 | 5.6268 | [2, 3, 5] | 3 | 0.4705 |

The covered small-prime range grows from {2} to {2,3,5} across the
grid, never reaching 2 < p <= k^3 (k^3 is approximately 594/1349/3866/11147
at the four scales, per the C4c/S1b sieve bound).

C5b (band ratio, PROVED limit L/y -> 4/ln2 = 5.7708):

| x | L/y | Lc/y |
| --- | --- | --- |
| 1e8 | 3.0861 | 11.3804 |
| 1e20 | 3.3296 | 9.9432 |
| 1e100 | 3.6507 | 8.6067 |
| 1e1000 | 3.9700 | 7.9975 |

The band (y, t] is nonempty grid-uniformly (both ratios exceed 1 at
every scale). This bites any two-sided or lower-direction use (the
mirror of the pintz-constants F2 finding, via the star identity B10);
the upper direction is band-immune (C5c).

C5c (Pi_3 <= 1 for admissible extensions, PROVED, upper direction):
stated, not tabulated -- see Section 4 of the sheet output for the
one-line derivation from B10 + B1.

C5d (the (2.16)-sharpening averaged per-step cost):

(i) EXACT, MEASURED-exact, finite product over p<=y of the max-over-nu
local factor at t=L+1:

| x | prod r=1 | prod r=2 | expo r=1 | expo r=2 |
| --- | --- | --- | --- | --- |
| 1e8 | 1.000000 | 2.000000 | 0.0000 | 0.2379 |
| 1e20 | 1.000000 | 3.000000 | 0.0000 | 0.2869 |
| 1e100 | 1.000000 | 3.000000 | 0.0000 | 0.2020 |
| 1e1000 | 1.000000 | 3.750000 | 0.0000 | 0.1707 |

(the r=1 product is exactly 1 at every scale -- the local factor's
r=1 collapse (2.7) reproduced as the exact identity it is.)

(ii) LIMIT SHAPE, MEASURED, expo limit (2/ln2)*(r(r-1)/2)*C3, C3 =
sum_p (p-1)/p^3 = P(2)-P(3) = 0.277484780742... (prime-zeta values;
cross-checked by a direct sieve sum over primes p < 2e6, giving
0.277484748391..., agreeing to 7 significant digits -- the residual
is the un-summed tail beyond 2e6, consistent with the closed form).
At r=1 the limit is 0 (the r=1 collapse again); at r=2 it is 0.8007.
Class GC-CONST (the ratio L/lnln x = 2/ln2 does not grow with scale).
Support quotes the recheck script's own caveat: "no remainder is
controlled uniformly in p, nu_p and r here."

C5d is component-only: it covers only the C5a-located prime set p<=y,
not the full small-prime range 2 < p <= k^3 that C4c and C5e price.

C5e (the unmarked residue -- the printed pointwise bookkeeping, source
disclosure B7 quoted: "we will not mark the dependence of the
constants implied by << or 0 symbols on t and r"):

| x | expo r=1 | expo r=2 |
| --- | --- | --- |
| 1e8 | 24.2054 | 48.4109 |
| 1e20 | 26.5790 | 53.1580 |
| 1e100 | 31.0509 | 62.1018 |
| 1e1000 | 37.3098 | 74.6196 |

Class GC-FASTER. An h-averaged treatment of Pi_2 would plausibly be
per-step o(1), but that derivation and the joint average of
Pi_1^r Pi_2^r it requires is ABSENT from the nine-page note (same
shape as the pintz-constants F2 finding: plausibly rescuable, not
carried by the source). OPEN, out of scope (item body non-scope).

---

## 5. Verdict

**VERDICT (V-NEG), verbatim from the sheet's S6:**

NEGATIVE AT CORPUS GRAIN: no located mechanism prices a
class-restricted r-th-moment loss (r in {1,2}, relative to the C4a
main term) in growth class GC-CONST at support MEASURED or better
over the full small-prime range; the item's hypothesis closes. The
one GC-CONST mechanism located (C5d, the (2.16) sharpening) is
component-only: it covers p <= y (C5a), not the full range 2 < p <=
k^3 that C4c and C5e cover, where the cost is GC-ITLOG (C4c) and
GC-FASTER (C5e) respectively.

Mechanical determination, per the S6 rule: every candidate column
that is GC-CONST (C5d) is component-only, and every full-range column
(C3a, C3b, C4c, C5e) is GC-ITLOG or worse -- the exact condition under
which the sheet's S6 rule emits (V-NEG). No column is missing, no
normalization is mixed, no class is ambiguous, so r28.7 (undecidable)
does not fire.

Honest scope paragraph, mirroring `pintz-constants.md` Section 5: this
report records no verdict on the project-level separator S1, on (CG),
on B2.pairs, or on the item-0010 campaign state. The (2.16)-sharpening
label rule (Section 3, above) is binding: no artifact of this session
uses the bare label "S1" for the workpaper's own Section 4
observation. Every use of Lemma 2 of 1004.1072v1 in this report and
the sheet carries the Section 3.4 support annotation: "unrefereed-
preprint; printed statement differs from the statement the proof
establishes; reading reconstructed and verified in-project." (Section
3.4's annotation does NOT extend to Kuperberg Theorem 1.2, which
carries its own, separate "unrefereed-preprint" venue note on C3a
above, without the "printed statement differs" clause -- that clause
is specific to the Pintz Lemma 2 print defect D1, not to Kuperberg's
paper.)

BET-20260725-11 now binds (item ratified and run) and stays OPEN for
operator judgment against this sheet, resolve_by 2026-09-30; this
report does not score the bet, and `ledger/bets.yaml` is untouched.

---

## 6. Both-readings appendix

**The verdict.** *Supporting:* every full-range column located in the
literature (C3a, C3b, C4c, C5e) is GC-ITLOG or GC-FASTER, all four
independently derived from different anchors (Kuperberg Theorem 1.2,
Kowalski Example 4.3, the star identity B10, and Pintz's own
"unmarked dependence" disclosure); the one GC-CONST mechanism found
(C5d) is provably component-only by the C5a split-point computation,
not by assumption. *Contradicting:* the sheet searches only the seven
anchors on this session's desk; a mechanism outside them (e.g. an
h-averaged treatment of Pi_2, C5e's own named absence) could in
principle rescue a full-range GC-CONST column, and the item's own
non-scope explicitly excludes attempting that proof work here.

**The C3b reference column.** *Supporting:* the leading term
(4/ln2) lnln(3L) is a direct instantiation of Kowalski's proved
Proposition 4.1 / Example 4.3, an unconditional asymptotic with no
open step. *Contradicting:* the O(k) additive term is unpinned at the
grid's finite scales, so the printed per-scale numbers are indicative
of the growth class only, not a certified numeric bound; the venue is
an unrefereed note.

**The C5e residue.** *Supporting:* the pointwise bound is exactly what
the source states and discloses as unmarked; nothing here
over-interprets the source. *Contradicting:* the bound is very
plausibly loose -- an h-averaged treatment is the natural next step
and is explicitly flagged as absent rather than impossible; if it
exists, C5e's GC-FASTER classification would not survive, though it
would not by itself flip the verdict (C4c alone already keeps the
full range at GC-ITLOG or worse).

---

## 7. Residual uncertainty

- C3b's O(k) additive term is unpinned; only the growth class
  (GC-ITLOG) is certified, not a numeric constant.
- C5d(ii)'s remainder is not uniformly controlled in p, nu_p, r (the
  recheck script's own caveat, quoted above); the LIMIT SHAPE column
  is a series identity to the printed order, not a proof.
- C5e's averaged Pi_2 treatment is un-derived (Section 1 non-scope);
  its absence is the same shape as the pintz-constants F2 finding.
- Every even-Cramer cell remains untested (unchanged from item-0026;
  literature-consolidation.md Residual uncertainty).
- A9's IMPRECISE reading of "its (1.4) ... rests on it" is sustained
  in this session's own re-read; the source file is left unedited
  (leave-and-document).

---

## 8. STOP-AND-REPORT conditions

All ten conditions reported; none fired.

- r28.1 (Section 0 predicate failure): did not fire. All three
  validity predicates held at session start; the rule-18 delta was
  empty; all Section 2 anchors were byte-identical; all start gates
  were green.
- r28.2 (input-hash mismatch): did not fire. All three Section 3
  files matched the steering-expected sha256 exactly before landing.
- r28.3 (verification failure): did not fire. No V-A row landed
  CONTRADICTED; the recheck re-run differed only on the permitted
  version line.
- r28.4 (self-check miss): did not fire. S1a/S1b/S1c/S1d all PASS.
- r28.5 (quote failure): did not fire. Every V-B governing display
  was byte-present in its named extract.
- r28.6 (extract-fidelity question): did not fire. No check surfaced
  a suspected defect in a graded extract.
- r28.7 (verdict undecidable): did not fire. The S6 rule applied
  mechanically to a V-NEG verdict; no column missing, no
  normalization mixed, no class ambiguous.
- r28.8 (close-gate failure): did not fire. All close gates green,
  including re-run stability and the ledger append-only check.
- r28.9 (scope pressure): did not fire. No step required web access,
  a PDF open, a Lean edit, an edit to an anchored file, or an eighth
  HASHES.txt line.
- r28.10 (sequence collision): did not fire. The last annotation
  before this session was ANN-20260731-87; this session's entry is
  ANN-<date>-88, the next sequence number.

---

## 9. Follow-up candidates (observations only, no items)

- The direction-asymmetry table of `pintz10-source-defects.md`
  Section 5 (1004.1084v1's two-sided-vs-lower-bound-only theorems
  against Lemma 2's unmarked general-r moment) is now landed and on
  the item-0029/item-0030 desks via this landing, per the workpaper's
  own Section 5 routing note.
- C5e's absent h-averaged Pi_2 treatment (and the joint average of
  Pi_1^r Pi_2^r it would require) is the same rescuable-but-uncarried
  shape as the pintz-constants F2 finding; a future item could attempt
  it, but it is new proof work outside this item's rule-15 grain.
- A9's IMPRECISE reading of the `[Pin]` dependency in
  `pintz10-singser.md` (Section 8 item 2 of the landed workpaper) is
  recorded here as sustained on a second, independent read; no
  further action taken.

---

## 10. Budget reconciliation

| task | estimate (Section 9 of the dispatch) | actual |
| --- | --- | --- |
| Task A | one careful extract-reading pass over two extracts | one full read of both extracts plus the workpaper; 10 V-A rows adjudicated; one script re-run |
| Task B | 250-350 script lines, sieve ranges <= k^3 <= 11146, one p<=2e6 pass | `class_restricted_sheet_28.py` is within the estimated line-count band; sieve ranges matched exactly (k^3 up to 11146 at 1e1000; one p<2e6 pass for Kowalski, shared with the C3 sieve cross-check) |
| Task C | one workpaper | this report |
| Task D | mechanical | HASHES.txt (7 lines), ANN-<date>-88, HANDOVER.md (3 bounded deltas), roadmap done-move -- all mechanical, one apply |
| network / PDF / Lean | none, none, none | none, none, none (all verification ran against the graded extracts, rule 26(4); no PDF was opened) |

No budget overrun.

---

END OF ITEM-0028 FINAL REPORT
