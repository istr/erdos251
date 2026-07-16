# Payload R3-FID — Blind Transcription-Fidelity Review

**Object:** `object_fidelity_counting.md` (Part I prose sections 1,2,4,5; Part II Lean 4
statement file, sections 4–5; Part III frozen Lean context).
**Reviewer constraints:** web access OFF; local code execution ON and used throughout;
memory/outside material excluded; Part III read only to resolve symbols, not audited.

## Phase-ordering compliance statement

Phase B's seven probes (F1–F7) were present in the payload text from the start, so I
cannot claim not to have *seen* them before writing Phase A — the payload was delivered
as one document. What I can and do attest to: the Phase A ledger below was produced by
my own independent, statement-by-statement reading of Part II against Part I (with
computation run per row where a finite claim was involved), completed and written out
in full — including the two substantive findings later restated as F4(c) and F5 — before
I drafted a single word of the Phase B answers. I did not use the F1–F7 prompts as a
checklist to reverse-engineer Phase A entries; the ledger's "deviation" rows were found
during the ledger pass itself, and F1–F7 below cite back to that ledger rather than the
reverse. Phase B was opened, in the sense of being *composed*, only after Phase A was
complete.

---

# PHASE A — Statement-by-statement fidelity ledger

Scope check (mechanical, via `grep`): Part II contains exactly 12 `sorry`-terminated
declarations under assessment (`singularSeries_lower_bound`, `oneExtension_sum_le`,
`consCount_lower_bound`, `delta_le_of_gap_bound`, `cword_prefix`, `cword_fork`,
`cword_suffix`, `cword_admissible`, `cspan_le`, `cfm2_tendsto`, `cbudget`,
`constr_consCount_pos`) plus 2 further `sorry`s in Part III (`singularSeries_multipliable`,
`singularSeries_pos`) that are explicitly out of scope (frozen context). The glue lemma
`q_eq_of_count` is PROVED (not `sorry`), carries prose ref "--" in Part II's own
traceability table, and is not one of the 12; I treat it as context, not a ledger row.
The definition cluster named by the payload has exactly 17 members. 12 + 17 = 29 rows
below.

Legend: **F**=faithful, **D-w**=deviation-weaker, **D-s**=deviation-stronger,
**D-n**=deviation-neutral, **U**=unfaithful.

## A.1 — Definitions cluster (17 rows)

| # | name | prose ref | verdict | justification | conf. |
|---|------|-----------|---------|----------------|-------|
| 1 | `IsConsecRealization` | sec.4 preamble, "consecutive realization of a gap word w...at n" | F | `∀i<L, gap(n+i)=w i` reproduces `g_{n+i}=w_i` exactly under the declared 0-index shift (`w i`=paper `w_{i+1}`, `gap m`=paper `g_{m+1}`); prose's "equivalently, L+1 primes occupy the point set with none between" is a restated corollary, not independent content, correctly left untranscribed. | 0.93 |
| 2 | `wordPointSet` | sec.4 preamble / sec.5 ("H(w)=A−q_0") | F | Prefix-sums-of-`w` construction telescopes to `{cElem(j)−cElem(0)}`, i.e. exactly `A−q_0`; verified by direct computation at 3 (J,K) pairs (§Computations). No explicit prose formula exists to compare against — this is the necessary formalization of an implicit prose notion, and it is the right one. | 0.9 |
| 3 | `offsetSpan` | Lemma 4.2 "`D=h_k`", sec.5(iii) "span" | F | `Finset.sup id`, total with `⊥=0` on `∅`. Docstring says "for the H of interest `0∈H`, so this is the paper's max" — technically `sup=max` on *any* nonempty Finset, not only those containing 0; `0∈H` is really what guarantees nonemptiness rather than being independently necessary for sup=max. Harmless imprecision in the comment, not in the definition; no fidelity impact. | 0.85 |
| 4 | `oneExtensions` | Lemma 4.2, range of `t` | F | `{t ∈ range(D) : Even t ∧ 0<t ∧ t∉H ∧ IsAdmissible(insert t H)}` = `{t : even t∈(0,D), t∉H, H∪{t} adm.}`, exact match to prose's range description, `insert t H = H∪{t}`. | 0.95 |
| 5 | `consCount` | Lemma 4.3, `N_cons(w;x)` | F | Filter condition `√x < q n ∧ q n ≤ x` matches prose's half-open `(√x,x]` exactly (open lower, closed upper) under `p_{n+1}=q n`. Outer domain `range(x+1)`: docstring claims "`n<q n≤x` forces `n<x+1`"; verified this requires `q n ≥ n+2` (true: `q` strictly increasing from `q 0=2`), so the search domain is complete, not merely convenient. | 0.92 |
| 6 | `cK` | sec.5, "`K=ceil(log2(4Cg)+2log2 ln x)`" | F | Direct match, `Real.logb 2` = `log2`. | 0.95 |
| 7 | `cJ` | sec.5, "`J=ceil(4 log2(K+20))`" | F | Direct match, uses the just-defined `cK`. | 0.95 |
| 8 | `cL` | sec.5, "`L=J+2+K`" | F | Direct match. | 0.97 |
| 9 | `cI` | sec.5, "`i_0=J+1`" | F | Direct match. | 0.97 |
| 10 | `tailBudget` | sec.5, "`H_x=4Cg(ln x)^2`" | F | Direct match. | 0.97 |
| 11 | `primeIdxAbove` | sec.5, starting index of "first `L+2` primes exceeding `L+3`" | F | `Nat.count Nat.Prime (L+4)` = #{primes < L+4} = #{primes ≤ L+3}; verified numerically for 7 values of `L` against an independent `sympy.primepi` computation — exact match every time. | 0.95 |
| 12 | `cprime` | sec.5, "`q_0<...<q_{L+1}`" | F | `q(primeIdxAbove L + j)`; verified this reproduces the prose's own "first `L+2` primes exceeding `L+3`" list at (J,K)=(3,4),(2,3),(4,6) via a fully independent from-scratch primality scan (not reusing the Lean-mirroring code path). | 0.95 |
| 13 | `cElem` | sec.5, `A={q_0,...,q_{L+1}}\{q_{i_0+1}}` | F | The `if t≤i_0 then q_t else q_{t+1}` monotone skip-enumeration was verified to reproduce `A` exactly, and to be strictly monotone increasing, at all 3 tested (J,K) pairs. | 0.93 |
| 14 | `cElem'` | sec.5, `A'={q_0,...,q_{L+1}}\{q_{i_0}}` | F | Same as above with the boundary at `t<i_0`; verified identically. | 0.93 |
| 15 | `cword` | sec.5, gap word `w` of `A` | F | Consecutive differences of `cElem`; verified against an independently-coded "prose" construction (sorted-set differences of `A`) — exact entrywise match at all 3 pairs. | 0.93 |
| 16 | `cword'` | sec.5, gap word `w'` of `A'` | F | Same, for `A'`; exact match. | 0.93 |
| 17 | `cgamma` | sec.5, `gamma=q_{i_0+1}-q_{i_0}` | F | Direct match; reproduces both Part II's own proved `example`s (`cgamma 3 4 = 2`, `cgamma 2 3 = 4`) exactly. | 0.96 |


## A.2 — The 12 sorried statements

| # | name | prose ref | verdict | justification | conf. |
|---|------|-----------|---------|----------------|-------|
| 1 | `singularSeries_lower_bound` | LEMMA 4.1, both clauses | D-s (self-declared, verified harmless) | Bookkeeping `k=\|H\|-1` correctly threaded into both clauses (`k+2=\|H\|+1` in the log terms, `k+1=\|H\|` in clause 2's `lnln x` term); single shared `C` for both clauses as in prose. `0<C` is added to the outer `∃C`; proved by hand (and spot-checked numerically) that `exp(-Ck ln(k+2))` is strictly decreasing in `C` for `k>0`, so any witness `C₀` can be replaced by `max(C₀,1)>0` without breaking either clause — the addition is provably inert, exactly as the docstring claims ("equivalent: the bound is monotone in `C`"). Dropped `x^{1-o(1)}` gloss is prose commentary restating clause 2, correctly omitted. | 0.88 |
| 2 | `oneExtension_sum_le` | LEMMA 4.2 | F | Quantifier order `∀κ(1≤κ) → ∃C₂(κ), ∀H(...)` matches prose's "for any fixed kappa≥1 there is `C_2=C_2(kappa)`" exactly (κ chosen before C₂). Hypothesis set (`0∈H`, even offsets, admissible, span≤κk ln(k+2) with `k=\|H\|-1`) matches "`H` as above" (i.e. 4.1's category) plus 4.2's own span clause. Neither prose nor Lean sign-constrains `C₂` — consistent, not a gap. The two prose asides ("kappa-uniform bounds FAIL for large kappa"; "span hypothesis is NECESSARY") are proof-technique/motivation commentary, not separate claims, correctly not transcribed. | 0.9 |
| 3 | `consCount_lower_bound` | LEMMA 4.3 | **D-w (undeclared — found in this review, not flagged in the Lean docstring)** | See F4(c) for the full derivation. In short: prose's conclusion is the two-link chain `N_cons ≥ (1/4)M_H(x) ≥ 1`, which asserts (i) `N_cons≥M_H/4` **and** (ii) `M_H(x)≥4` as two separate facts. Lean's conclusion is `M_H/4 ≤ N_cons ∧ 1 ≤ N_cons`. First conjuncts are identical. Second conjuncts are not: prose's `M_H≥4` implies Lean's `N_cons≥1` (via the shared first clause), but Lean's `N_cons≥1` does *not* imply `M_H≥4` — `N_cons≥1` carries no information about the size of `M_H` beyond what the first conjunct already gives. So the Lean pair is strictly implied by, but does not imply, the prose pair: a genuine, provable weakening of the exported conclusion. It is very likely harmless for downstream use (the traceability table itself records `constr_consCount_pos` as needing only "the chain down to `N_cons≥1`"), but "harmless" is not "faithful," per the payload's own instruction. Span-hypothesis shape (`κL ln(L+2)`) matches 4.2's shape under `k=L` (verified: `\|H(w)\|=L+1 ⟹ k=\|H(w)\|-1=L`, so 4.3's shape is 4.2's shape specialized, exactly as prose's own proof says: "using Lemma 4.2 (k=L; the span hypothesis here is exactly 4.2's)"). Evenness of offsets, absent as a hypothesis, is *correctly* absent: proved by hand that `IsAdmissible H ∧ 0∈H ⟹ ∀h∈H, Even h` (admissibility at `p=2` forbids both residues being occupied, and `0∈H` occupies residue 0), matching the docstring's own derivability claim, which I verified rather than trusted; also spot-checked computationally that all three tested constructed point sets are in fact all-even and admissible. Quantifier order `∃x₀,∀x≥x₀,∀w L[hyps(x)]→...`: prose's phrasing ("Let w be... [x-dependent card. bound]... for all large x...") is ambiguous on the page about whether `x₀` may depend on `w`, but the *cardinality hypothesis itself references `x`* (`\|H(w)\|≤4lnln x-1`), so a `w`-first reading isn't even well-formed without first fixing `x`; moreover the uniform reading is the only one compatible with `constr_consCount_pos`, where `w` is itself defined as a function of `x`. Uniform `∃x₀∀x∀w` is correct. | 0.82 |
| 4 | `delta_le_of_gap_bound` | LEMMA 4.4 | **D-s (partially self-declared)** | Index map verified exactly: `nu=n+1` gives `delta_nu = delta(n+1)` (delta has "no shift" per the index-convention note) and `p_nu = q(nu-1) = q(n)`, matching Lean's `delta (n+1) ≤ 3*Cg*log(q n)^2` term-for-term. `hB` is verified byte-for-byte identical to the body of frozen `CramerGranville` (`∀n,n0≤n→gap n≤C*log(q n)^2`, α-renamed). But: prose's Lemma 4.4 is invoked "Under Hypothesis B," and Hypothesis B's own statement is "`∃ C_g≥1` and `nu_B` such that...” — i.e. `C_g≥1` is part of what "Under Hypothesis B" supplies. Neither the frozen `CramerGranville` nor `delta_le_of_gap_bound`'s signature carries any `1≤Cg` (or even `0≤Cg`) constraint; `Cg` ranges over all of `ℝ`. I checked whether this is actually vacuous by another route: `gap n` is a cast natural, hence `≥1` always for every `n` (all 500 gaps computed, minimum was 1); for `Cg<0`, `Cg*log(q n)^2<0` since `log(q n)>0` for all `n` (as `q n≥2`), so `hB` would require `gap n≤(negative)` for all large `n`, impossible — `hB` is *unsatisfiable* for `Cg<0`, so no false theorem results from the missing constraint, but the *literal statement* is still broader than what "Under Hypothesis B" licenses. This is the one instance in the object where the docstring's disclosure ("binds `∃C:ℝ` with no sign or size constraint; the frozen definition is not touched") only names *that* the gap exists, not that it is inert — the inertness is a separate fact I had to prove myself. Root cause is Part III's `CramerGranville`, per the payload's rule I flag this and do not audit Part III further; the Part-II-level fact remains that `delta_le_of_gap_bound`'s own signature (unlike its siblings `oneExtension_sum_le`, `cbudget`, `constr_consCount_pos`, which all carry an explicit `1≤κ`/`1≤Cg`) does not restore the constraint locally. | 0.85 |
| 5 | `cword_prefix` | sec.5(i), prefix | F | `∀j<J, cword j = cword' j`; verified entrywise at (3,4) [(4,2,4)=(4,2,4)], (2,3) [(2,4)=(2,4)], (4,6) [(2,4,6,2)=(2,4,6,2)]. `1≤J,1≤K` hypotheses are prose-implied (see F7) and generalize prose's fixed construction to arbitrary `J,K≥1`, of which the section-5 `cJ(Cg,x),cK(Cg,x)` are one instance recovered later via `cbudget`; this abstraction is content-preserving. | 0.92 |
| 6 | `cword_fork` | sec.5(i), fork, `(-gamma,+gamma)` | F | `cword J + gamma = cword' J` and `cword(J+1) = cword'(J+1)+gamma`; this is exactly "`w`'s first middle entry is `word'`'s minus gamma" and "`w`'s second middle entry is `word'`'s plus gamma," i.e. `(-gamma,+gamma)` in the `(w,w')` order. Verified numerically at all 3 pairs (e.g. (3,4): `6+2=8`✓, `8=6+2`✓). Section-6 sign-swap note is an opaque forward pointer per the rules, not evaluated. | 0.93 |
| 7 | `cword_suffix` | sec.5(i), suffix | F | `∀i<K, cword(J+2+i)=cword'(J+2+i)`; verified entrywise at all 3 pairs. | 0.93 |
| 8 | `cword_admissible` | sec.5(ii) + 5(iv) cardinality | F | Bundles admissibility of both point sets with `card=L+1` for both — a reorganization across prose's (ii)/(iv) boundary, not a content change (traceability table itself documents the merge). Admissibility verified *directly* (not just via the `p≤L+2`/`p>L+2` pigeonhole argument, but by literal residue computation mod every prime `<L+10`) for all 3 pairs; the "`p>L+2` automatic" half of prose's argument checked arithmetically (`p>L+2 ⟹ p≥L+3>L+1=` #points, so pigeonhole applies without further casework). | 0.9 |
| 9 | `cspan_le` | sec.5(iii) | D-w (minor, disclosed) | Conjunct 1 (`q_{L+1}-q_0 ≤ C₁ L ln L`) and conjunct 2 (`gamma ≤ C₁ L ln L`) match prose's chain literally. Conjuncts 3–4 bound `offsetSpan` by `C₁ L ln(L+2)` — a strictly *looser* bound than the `ln L` form, chosen (per the docstring) to match what `consCount_lower_bound` consumes. I verified by direct computation that `offsetSpan(H(w)) = q_{L+1}-q_0` **exactly** (not merely `≤`) at 6 tested (J,K) pairs including the boundary cases (1,1),(1,5),(5,1) — so the tighter `ln L` bound on `offsetSpan` is also true and provable from conjunct 1, but is never stated; only the `ln(L+2)` form is exported. Harmless (`ln L≤ln(L+2)` trivially, verified) and explicitly disclosed ("legitimate since `ln L ≤ ln(L+2)`"), but is a real instance of a tighter available prose-adjacent bound being replaced by a looser stated one. `1≤C₁` matches prose's "`C_1≥1` fixed" verbatim (not even an addition). | 0.83 |
| 10 | `cfm2_tendsto` | sec.5(iii), the limit | F | `Filter.Tendsto (fun x => (cgamma+4)/2^cJ) atTop (nhds 0)` matches prose's "`(gamma+4)/2^J → 0`" (the headline conclusion). The intermediate quantitative rate "`≤ 3C_1/(K+20)^2`" is proof machinery for the limit, not separately exported — reasonable, since nothing else in the object consumes a rate bound (checked: no reference to a `(K+20)^-2`-shaped quantity anywhere else in Part II). | 0.87 |
| 11 | `cbudget` | sec.5 "Fix x large" + 5(iv) | F | All 6 listed conjuncts checked one-to-one against prose text (see F6 for the full map); the one declared non-transcription (asymptotic formula `L+1=(2/ln2)lnln x+O(lnlnln x)`) was verified absent from the statement and its "operative content," the `<3lnln x` clause, verified present. `1≤cJ∧1≤cK` traced to prose's "since J,K≥1" aside (not literally under "(iv)" but present in section 5's text). Computationally explored: `1≤cJ` turns out to hold *unconditionally* for every `(Cg,x)` tested (`cJ≥18` always, since `cK+20≥20` regardless of `cK`), while `1≤cK` is the genuinely `x`-dependent part; both are true, prose's "since J,K≥1" doesn't distinguish which is doing the work, but that's a prose economy, not a Lean deviation. | 0.87 |
| 12 | `constr_consCount_pos` | 4.3∘5, sec.6 entry point | F | Correctly composes `consCount_lower_bound` with the section-5 construction's guarantees. Notably takes `hA:HLQuantA` and `1≤Cg` but **no** `CramerGranville`/Hypothesis-B hypothesis — checked whether this is a coverage gap and concluded it is not: tracing the dependency graph, `consCount_lower_bound`'s hypotheses (admissibility, cardinality, span) and `cbudget`/`cspan_le`'s guarantees never invoke `CramerGranville`; `Cg` is used only as a *numeric parameter* feeding `cK`'s formula, not as a certificate that a gap bound holds. This matches Part I's actual structure: Lemma 4.3 and section 5(i)–(iv) as excerpted only ever invoke Hypothesis A; Hypothesis B surfaces solely in Lemma 4.4, a logically separate fact. So the omission is correct, not a gap. Pointers to "section 6," `FM-F`, the anchors `n_x,m_x` are opaque out-of-scope references per the rules and are not evaluated further. | 0.85 |


## A.3 — Overall Phase-A verdict

**FAITHFUL, with a small number of documented deviations**, all weakenings or harmless
strengthenings, none reversing an inequality direction, none mismatching a quantifier in
a way that changes truth conditions, none miscomputing an index shift. Two deviations
are substantive enough to carry into Phase B in full: the dropped `M_H(x)≥4` half of
Lemma 4.3's conclusion pair (row A.2.3, undeclared) and the dropped `C_g≥1` (really
`≥0`) constraint feeding Lemma 4.4 (row A.2.4, partially declared). One further
deviation (row A.2.9, `cspan_le`'s `ln(L+2)` vs. the provable tighter `ln L`) is minor
and fully disclosed. The self-declared deviation in row A.2.1 (`0<C` addition) was
independently verified to be logically inert via a monotonicity argument, not merely
asserted. Every declared omission I could locate was checked against the actual
statement text rather than taken on the docstring's word, per the payload's instruction;
I found no case where a declared omission was itself misdescribed.

**Overall Phase-A confidence: 0.85** (weighted toward the two substantive rows, which
rest on careful but ultimately human-judgment-inflected readings of where an informal
inequality chain's "real" content ends — I consider both well-argued but not
beyond-reasonable-doubt certain).

---

# PHASE B — Targeted probes

*(Opened only now, after Phase A above was completed in full — see the compliance
statement at the top.)*

## F1 — Construction tables

Computed independently by two separate code paths (one mirroring the Lean definitions
literally, one mirroring the prose sentence "let `q_0<...<q_{L+1}` be the first `L+2`
primes exceeding `L+3`" via a from-scratch primality scan with no shared code below the
sieve), at the two mandated pairs plus one fresh pair `(J,K)=(4,6)` with `J,K≥2`. All
entries agreed exactly; asserts in the script would have raised on any mismatch, none
did.

**(J,K) = (3,4)**: L=9, i₀=4

| | values |
|---|---|
| `q_0..q_10` | 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53 |
| `A` (skip `q_5`=31) | 13,17,19,23,29,37,41,43,47,53 |
| `A'` (skip `q_4`=29) | 13,17,19,23,31,37,41,43,47,53 |
| `w` | 4,2,4,6,8,4,2,4,6 |
| `w'` | 4,2,4,8,6,4,2,4,6 |
| `gamma` | 2 |

This matches Part II's own smoke-test comment exactly ("`q_0..q_{L+1}=13,17,19,23,29,31,
37,41,43,47,53`; `gamma=2`, prefix `(4,2,4)`, suffix `(4,2,4,6)`") and both proved
`example`s (`cgamma 3 4 = 2`; prefix/suffix examples), reproduced independently above.

**(J,K) = (2,3)**: L=7, i₀=3

| | values |
|---|---|
| `q_0..q_8` | 11, 13, 17, 19, 23, 29, 31, 37, 41 |
| `A` (skip `q_{i0+1}=q_4`=23) | 11,13,17,19,29,31,37,41 |
| `A'` (skip `q_{i0}=q_3`=19) | 11,13,17,23,29,31,37,41 |
| `w` | 2,4,2,10,2,6,4 |
| `w'` | 2,4,6,6,2,6,4 |
| `gamma` | 4 |

Matches Part II's smoke-test comment ("`gamma=4`") and the proved `example cgamma 2 3 = 4`.

**(J,K) = (4,6), fresh pair, both ≥2**: L=12, i₀=5

| | values |
|---|---|
| `q_0..q_13` | 17,19,23,29,31,37,41,43,47,53,59,61,67,71 |
| `A` (skip `q_6`=41) | 17,19,23,29,31,37,43,47,53,59,61,67,71 |
| `A'` (skip `q_5`=37) | 17,19,23,29,31,41,43,47,53,59,61,67,71 |
| `w` | 2,4,6,2,6,6,4,6,6,2,6,4 |
| `w'` | 2,4,6,2,10,2,4,6,6,2,6,4 |
| `gamma` | 4 |

Prefix (len 4) `(2,4,6,2)` shared; suffix (len 6) `(6,6,2,6,4)`... (positions 6..11)
shared; fork at positions 4,5: `w`=(6,6), `w'`=(10,2), and `6+4=10`, `6=2+4` — both
fork identities hold. Prose-construction and Lean-construction code paths agreed on
every one of these entries.

## F2 — Deletion encoding

Verified computationally for all three (J,K) pairs above:
- `cElem`/`cElem'`'s `if`-enumerations reproduce `A = {q_0,...,q_{L+1}}\{q_{i_0+1}}` and
  `A' = {q_0,...,q_{L+1}}\{q_{i_0}}` exactly as sets (checked via Python `set` equality
  against the independently-scanned prose prime list).
- Both enumerations are strictly monotone increasing in `t` (checked directly: every
  consecutive pair satisfies `<`).
- `wordPointSet(cword J K)(cL J K)` equals `A − q_0` elementwise at all three pairs, e.g.
  at (3,4): `wordPointSet(w) = {0,4,6,10,16,24,28,30,34,40}` and `A−q_0 =
  {0,4,6,10,16,24,28,30,34,40}` — identical (this also indirectly re-verifies the
  telescoping argument in ledger row A.1.2). Same check for `w'`/`A'` passed at all
  three pairs.

## F3 — Lemma 4.1 transcription

| transformation | classification | one-line proof |
|---|---|---|
| bookkeeping `k=\|H\|-1` (so `ln(k+2)→ln(\|H\|+1)`, exponent's `(k+1)→\|H\|`) | equal | pure substitution: `k=\|H\|-1 ⟹ k+2=\|H\|+1` and `k+1=\|H\|`, both arithmetic identities, verified by direct symbol substitution into both clauses (§Phase A row A.2.1). |
| shared constant `C` across both clauses | equal | syntactically one `∃C` scopes both conjuncts in the Lean source; not two same-named-but-different constants. |
| added `0<C` | stronger-as-written, equal-in-content | `∃C,0<C∧P(C)` strictly implies `∃C,P(C)` in general, so syntactically stronger; but computed `exp(-Ck ln(k+2))` for `k=5`, `C∈{-2,...,10}` and confirmed strict monotone decrease in `C`, which proves any witness `C₀` (any sign) can be upgraded to `max(C₀,1)>0` without breaking either clause — so the *provable content* (the `∃`-statement's truth value) is unchanged; only the syntactic form is stronger. |
| dropped `x^{1-o(1)}` phrasing | equal (correctly omitted) | this is prose's own informal restatement of the immediately preceding exact formula ("`=x^{1-o(1)}`"), not independent content; nothing is lost by omitting a gloss of a formula that is itself transcribed in full. |

## F4 — Lemmata 4.2/4.3

**Range of `t`.** `oneExtensions H = {t∈range(offsetSpan H) : Even t∧0<t∧t∉H∧
IsAdmissible(insert t H)}` = `{t : 0<t<D, even, t∉H, H∪{t} admissible}`, an exact match
to prose's "even `t` in `(0,D)`, `t` not in `H`, `H∪{t}` admissible" (`insert t H =
H∪{t}`). **Faithful.**

**Span-hypothesis shapes.** 4.2 uses `κk ln(k+2)` with `k=|H|-1`; 4.3 uses
`κL ln(L+2)`. These are the *same shape*: since `consCount_lower_bound` requires
`|H(w)|=L+1`, plugging into 4.2's convention gives `k=|H(w)|-1=L`, so `κL ln(L+2)` is
literally `κk ln(k+2)` at `k=L`. This matches prose's own proof of 4.3, which says
outright "using Lemma 4.2 (`k=L`; the span hypothesis here is exactly 4.2's)." Verified
by symbolic substitution, no numeric computation needed beyond confirming the arithmetic
identity `k=L`. **Faithful.**

**4.3's conclusion pair vs. the prose chain.** This is the review's most substantive
finding; full derivation (already given in ledger row A.2.3, repeated here in the form
F4 asks for): let P = prose's `(N≥M/4) ∧ (M/4≥1)`, L = Lean's `(N≥M/4) ∧ (1≤N)`, writing
`M=M_{H(w)}(x)`, `N=consCount`. `P⟹L`: first conjuncts identical; second, `M/4≥1` plus
`N≥M/4` gives `N≥1` by transitivity. `L⟹̸P`: `N≥1` says nothing about `M`'s size; `M`
could in principle be far below `4` while `N≥1` still holds (nothing in the Lean pair
constrains `M` from above, so there is no way to recover `M≥4` from it). Hence `P` is
strictly stronger than `L`; Lean's stated conclusion is a genuine, provable weakening of
prose's stated conclusion. This is **not** flagged in `consCount_lower_bound`'s
docstring (contrast with rows A.2.1 and A.2.4, where the corresponding gaps *are*
flagged) — an undeclared deviation, found by working the logic rather than by pattern-
matching against a stated caveat. I judge it very likely harmless for the object's own
downstream use (`constr_consCount_pos` only ever needs `1≤consCount`), but per the
payload's explicit instruction this counts as a finding regardless of mathematical
reasonableness. **Deviation-weaker, confidence 0.82** (the residual uncertainty is about
how strictly to read an informal "`A≥B≥C`" chain as asserting `B` as independent
content, versus reading it as proof narration whose only "real" claim is the endpoint
comparison `A≥C` — I lean toward the former because the prose displays it as the
lemma's boxed conclusion line, not inside the proof, but a different reasonable referee
could disagree).

**Evenness omission in Lean 4.3, docstring's derivability argument.** Docstring claims:
"[evenness] follows from admissibility, since `0∈H(w)` and an odd offset would occupy
both classes mod 2." Verified by hand: `IsAdmissible H` at `p=2` gives `nuMod H 2 < 2`,
i.e. `H`'s image in `ZMod 2` has at most 1 element; `0∈H` puts residue `0` in that image;
if any `h∈H` were odd, residue `1` would also be in the image, giving 2 elements,
contradiction — so all `h∈H` are even. This is a complete, correct proof, not just a
plausible-sounding claim. Cross-checked computationally: every constructed point set at
all three tested (J,K) pairs is both admissible (verified by literal residue
enumeration mod every prime `<L+10`, not just the `p≤L+2`/`p>L+2` pigeonhole argument)
and entirely even. **Verified correct; the omission is faithful, not a gap** — including
or excluding a hypothesis that is strictly implied by the other stated hypotheses
produces logically equivalent theorems. Note also that prose's own Lemma 4.3 statement
never says "even offsets" either (unlike 4.1/4.2, which explicitly do) — so Lean isn't
even dropping something prose asserts; it matches prose's silence on the point, and
separately proves the silence was safe.

## F5 — Lemma 4.4 index shift

**The `nu = n+1` map, checked exactly.** Index conventions: `delta n` = paper `delta_n`
("no shift," per Part II's own convention note) and `q n` = paper `p_{n+1}`, i.e.
paper `p_ν = q(ν-1)`. Setting `ν=n+1`: `delta_ν = delta(n+1)` directly (no shift needed
on the delta side), and `p_ν = p_{n+1} = q((n+1)-1) = q(n)`. So prose's
`delta_ν ≤ 3C_g(ln p_ν)^2` becomes, under `ν=n+1`, exactly `delta(n+1) ≤ 3Cg·log(q n)^2`
— which is Lean's conclusion verbatim. **Exact, verified.**

**`hB` exactly the body of frozen `CramerGranville`?** `hB : ∀n,n₀≤n→gap n≤Cg·log(q n)^2`.
`CramerGranville := ∃C,∃n0,∀n,n0≤n→gap n≤C·log(q n)^2`; its body (after existentially
eliminating `C,n0`) is `∀n,n0≤n→gap n≤C·log(q n)^2`. Under the renaming `C↔Cg`,
`n0↔n₀`, these are syntactically identical. **Confirmed exactly as claimed.**

**But** (this is where ledger row A.2.4's finding sits): "Under Hypothesis B" in prose
supplies not just the gap-bound body but also "`C_g≥1`" — Hypothesis B's own text is
"There exist `C_g≥1` and `nu_B` such that...". Since `CramerGranville` (frozen, Part III)
does not carry `1≤C` in its own `∃`, and `delta_le_of_gap_bound` does not add it back
locally (contrast: `oneExtension_sum_le`, `cbudget`, and `constr_consCount_pos` all
carry an explicit `1≤κ`/`1≤Cg` hypothesis where their prose sources call for it — this
one does not), the Lean theorem is universally quantified over a strictly larger set of
`Cg` values than "Under Hypothesis B" licenses. I checked whether this is *actually*
exploitable (i.e. whether the broadened theorem could be used to prove something false)
and found it cannot: `gap n` is a natural number cast to `ℝ`, hence `≥0`, and in fact
`≥1` always (every one of 500 computed gaps was `≥1`, consistent with `q` strictly
increasing from `q 0=2`); for `Cg<0`, `log(q n)>0` (since `q n≥2>1` for all `n`), so
`Cg·log(q n)^2<0`, and `hB` would assert `gap n ≤ (a negative number)` for all large `n` —
impossible given `gap n≥1`. So `hB` is unsatisfiable for `Cg<0`: nobody can actually
invoke `delta_le_of_gap_bound` with a negative `Cg`, because no proof of `hB` exists
for one. The missing constraint is therefore inert in the same *sense* as row A.2.1's
`0<C` addition to Lemma 4.1 — but note the direction is opposite (here a hypothesis is
*missing* relative to what "Under Hypothesis B" supplies, not *added* beyond what
prose's inequality needs), and unlike row A.2.1, I did not find this inertness argument
written anywhere in the object's own docstrings; only the *existence* of the gap
("no sign or size constraint") is flagged, not its harmlessness. Since `CramerGranville`
itself is Part III and out of primary scope, per the payload's rule I flag this as
**turning on a Part-III definition** rather than treating it as a pure Part-II
authoring error — but the absence of a local `1≤Cg` (or `0≤Cg`) hypothesis on
`delta_le_of_gap_bound` specifically is a Part-II-level fact I can and do assess:
**deviation-stronger relative to the literal text of "Under Hypothesis B," verified
harmless in effect, partially but not fully self-disclosed.**

## F6 — Coverage of section 5's quantitative claims

Mapping every prose clause of "Fix x large," 5(iii), 5(iv) to `cspan_le` /
`cfm2_tendsto` / `cbudget` conjuncts (● = present, ○ = absent-and-declared,
† = absent-and-covered-by-a-different-theorem):

| prose clause | Lean location | status |
|---|---|---|
| "Fix x large" (governs the whole section) | outer `∃x₀,∀x≥x₀` of `cbudget`; also the `atTop` filter of `cfm2_tendsto`; also `constr_consCount_pos`'s own `∃x₀` | ● |
| "since `J,K≥1`" | `cbudget` conjuncts 1–2 (`1≤cJ∧1≤cK`) | ● |
| "`2^K≥H_x`" (parenthetical right after defining `H_x`) | `cbudget` conjunct 3 (`tailBudget≤2^cK`) | ● |
| "span `≤q_{L+1}-q_0≤C_1Lln L`" | `cspan_le` conjunct 1 (the `q_{L+1}-q_0≤C_1LlnL` half only) | ● (partial — see A.2.9: the *offsetSpan* itself is bounded by the looser `ln(L+2)` form in conjuncts 3–4, not this tighter one, even though I verified `offsetSpan=q_{L+1}-q_0` exactly, so the tight form *would* transfer) |
| "hence `gamma≤C_1Lln L`" | `cspan_le` conjunct 2 | ● |
| "`(gamma+4)/2^J≤3C_1/(K+20)^2`" (explicit rate) | *no direct counterpart* | † — absorbed into `cfm2_tendsto`'s limit conclusion; the rate itself is not separately exported anywhere in Part II (checked: no other conjunct or theorem references a `(K+20)`-shaped quantity) |
| "`...→0`" | `cfm2_tendsto` | ● |
| "the words have `L+1` points" | *not in these three theorems* | † — covered by `cword_admissible`'s `.card=cL+1` conjuncts instead |
| "`L+1=(2/ln2)lnln x+O(lnlnln x)`" | *absent, and the docstring says so* | ○ — verified absent from `cbudget`'s statement; declared omission confirmed accurate |
| "`<3lnln x` eventually" | `cbudget` conjunct 4 | ● |
| "meeting 4.3's `L+1≤4lnln x-1`" | `cbudget` conjunct 5 | ● |
| "one-point extensions `L+2≤4lnln x`" | `cbudget` conjunct 6 | ● |
| "`span≤(ln x)^3`... (operative bound is (iii))" | `cbudget` conjuncts 7–8, for both `w,w'` | ● |

**Judging the docstrings' declared non-transcriptions against this list:** the only
clause the object's own docstrings claim is *not* transcribed is the `L+1=(2/ln2)lnln x
+O(lnlnln x)` asymptotic formula, and I confirmed that claim is accurate (it is indeed
absent, and its "operative content" the `<3lnln x` bound is indeed present). The
declared list is therefore *exactly* that one clause — no more, no less — but it is not
*complete* relative to what I actually found absent: the explicit rate bound
`(gamma+4)/2^J≤3C_1/(K+20)^2` and the tightest form of the `offsetSpan≤...ln L` bound
are also not directly stated (both for defensible reasons given above, and both already
recorded in Phase A), yet neither is separately flagged in a docstring the way the
asymptotic-formula omission is. I judge these as legitimate, low-severity gaps in the
docstrings' own self-reporting rather than in the transcription itself.

## F7 — Hidden-strengthening scan

Every Lean-side hypothesis across the 12 statements with no *literal, word-for-word*
prose counterpart, classified:

| hypothesis | where | classification |
|---|---|---|
| `0∈H` | 4.1 (×2 clauses), 4.2 | prose-implied: `H={0=h_0<h_1<...}` bakes "0 is the minimum element" into prose's own notation for `H` throughout sec. 4; not an extra restriction. |
| `∀h∈H,Even h` | 4.1 (×2), 4.2 | prose-implied: 4.1 says "admissible `H` of even offsets" explicitly; 4.2 says "`H` as above," referencing 4.1's category. |
| `IsAdmissible H` / `IsAdmissible(wordPointSet w L)` | 4.1,4.2,4.3 | prose-implied directly ("admissible `H`"/"`H(w)` is admissible"). |
| `1≤κ` | 4.2, 4.3 | prose-implied, both say "for a fixed kappa≥1" verbatim. |
| `0<C` | 4.1 | genuine syntactic strengthening, proved harmless (row A.2.1, F3) — the one case I could fully close the loop on with an explicit proof of equivalence. |
| `1≤C₁` | `cspan_le` | not an addition — prose's own text says "`C_1≥1` fixed." |
| *(no)* `1≤Cg`/`0≤Cg` | `delta_le_of_gap_bound` | inverse case — a prose-side constraint (`C_g≥1` from "Under Hyp. B") **missing** on the Lean side; proved harmless-in-effect via the unsatisfiability argument (F5) but not a "hidden strengthening," a hidden *generalization*; still flagged as the F5 finding. |
| `1≤J,1≤K` | `cword_prefix/fork/suffix/admissible`, `cspan_le` | prose-implied ("interior with slack:...since `J,K≥1`"); note (verified computationally) these two specific interiority facts (`1≤i_0`, `i_0+1≤L`) actually already hold for any `J,K≥0`, so prose's stated justification is not the *tightest* possible one — a prose-side looseness, not a Lean-side one, and irrelevant to fidelity since Lean matches what prose states, not what prose could have stated. |
| `1≤Cg` | `cfm2_tendsto`, `cbudget`, `constr_consCount_pos` | prose-implied: `Cg` throughout sec. 5 is understood to be the `C_g` supplied by Hypothesis B, which is `≥1` by that hypothesis's own text; standing assumption, not restated at every mention in prose either. |
| `hA:HLQuantA` | `consCount_lower_bound`, `constr_consCount_pos` | prose-implied directly ("Under Hypothesis A"). |
| `(H.card:ℝ)≤4loglogx`, `∀h∈H,h≤logx^3` (4.1 clause 2) | 4.1 | prose-implied: this is "in the budget of Hypothesis A" spelled out; verified this does *not* additionally smuggle in `hA:HLQuantA` itself — clause 2 is a standalone fact about `modelMass` and correctly does not assume Hypothesis A is true, only that `(H,x)` sit in its window (checked: `modelMass` doesn't mention `tupleCount` at all, so nothing here depends on whether the two are actually close). |

No hypothesis was found that lacks *any* prose grounding and also changes provability in
a consequential direction (the closest candidate, `0<C`, was shown inert). The
interesting asymmetry this scan surfaces is the C_g-sign question, which is really a
*missing* restriction rather than an *added* one, and which F5 covers in full.

---

# Final verdict

**FAITHFUL, with documented deviations.**

1. **`consCount_lower_bound` (Lemma 4.3)** — conclusion pair `M/4≤N ∧ 1≤N` is strictly
   weaker than prose's chain `N≥M/4≥1`, which also asserts `M≥4` independently.
   Deviation-weaker. *Undeclared* in the object's own docstring. (Ledger A.2.3, F4.)
2. **`delta_le_of_gap_bound` (Lemma 4.4)** — no `1≤Cg` (or even `0≤Cg`) constraint,
   where prose's "Under Hypothesis B" supplies `C_g≥1`. Proved harmless-in-effect
   (hypothesis is unsatisfiable for `Cg<0`) but broader-as-written. Root cause traces to
   Part III's `CramerGranville`, flagged per the payload's rule rather than audited
   further; the local absence on the Part-II theorem itself is still a Part-II-level
   fact. Deviation-stronger, *partially* declared (existence of the gap is noted in the
   docstring; its harmlessness is not). (Ledger A.2.4, F5.)
3. **`cspan_le`** — `offsetSpan` is bounded by `C_1 L ln(L+2)`, a looser form than the
   `C_1 L ln L` bound the same theorem proves for `q_{L+1}-q_0` (and which I verified
   equals `offsetSpan` exactly, not just bounds it). Minor, fully declared and
   deliberate. (Ledger A.2.9, F6.)
4. **`singularSeries_lower_bound` (Lemma 4.1)** — `0<C` added to the existential;
   proved logically inert via monotonicity. Minor, fully declared. (Ledger A.2.1, F3.)

No row was found unfaithful in the sense of asserting something prose does not (wrong
inequality direction, wrong quantifier scope, wrong index, mismatched constant role).
Every index-convention shift I traced (0- vs 1-based primes, `gap`/`delta`'s "no-shift"
vs `p`'s "-1 shift," the `ν=n+1` substitution in 4.4) checked out exactly. All four
proved `example` smoke tests and the full prime/point-set/gap-word tables at three
`(J,K)` pairs were independently reproduced by code with no discrepancy.

**Overall confidence: 0.85.**

---

# What I could not check

- **Lean/Mathlib compilation or elaboration.** No Lean toolchain was invoked; this
  review reads the displayed Lean text mathematically (what would this Prop mean if
  elaborated as written) rather than mechanically (does it actually parse and
  typecheck against the real `Mathlib`/`Nat.nth`/`Finset.sup`/`Nat.count`/`ZMod`
  APIs). I have no live Mathlib source in this sandbox and did not attempt to fetch and
  build one (a full Mathlib build is a multi-hour undertaking disproportionate to a
  fidelity review, and is explicitly outside what's asked — the payload asks about
  transcription fidelity, not provability or well-formedness). Wherever a *finite*
  numeric consequence of an API's stated meaning was checkable, I re-derived it in
  Python from first principles and cross-checked it 2–3 independent ways (see below);
  that is the strongest substitute available here for compilation, but it is not the
  same thing. **UNVERIFIED: compiles / elaborates as written.**
- **Citations in Part I's proof sketches**: "Hardy-Wright, *An Introduction to the
  Theory of Numbers*, Thm 8 area; citation verification pending" (Lemma 2.1, itself out
  of Part II's transcription scope), "Mertens 1874; Rosser-Schoenfeld 1962" (Lemma
  4.1's proof sketch), "Chebyshev upper bound on `p_{2L+4}`; classical" (5(iii)'s `C_1`
  existence). Web access is off; these are proof-internal classical references, not
  part of the *statements* under fidelity assessment, but I flag them as unverified
  rather than silently passing over them. **UNVERIFIED.**
- **Part III's own correctness beyond symbol resolution** — e.g. whether `singularSeries`
  (a `tprod`) truly computes the standard Hardy–Littlewood singular series, or whether
  `singularSeries_multipliable`/`singularSeries_pos` (Part III's own two `sorry`s) are
  provable — explicitly out of scope per the rules ("NOT under assessment... do not
  audit Part III beyond" resolving what a Part-II question turns on). Where a
  Part-II fidelity question *did* turn on a Part-III definition (`HLQuantA`,
  `CramerGranville`), I said so explicitly (F5; also the `HLQuantA` clause-2 analysis
  in F7's last row) without auditing further.
- **Section 3 and sections 6–9** do not exist in this object; every pointer to
  "section 6," `FM-1`, `FM-2`, `FM-F`, the fork-merge anchors `n_x, m_x` was treated as
  opaque per the rules and not speculated about.
- **Mathematical truth of Hypotheses A/B, or provability of any of the 12 `sorry`s** —
  out of scope by the payload's explicit instruction; not assessed.

---

# Computations performed

All in Python 3 (`sympy` for two independent primality/prime-counting routines,
`bisect` for a `Nat.count`-mirroring binary search, a hand-rolled trial-division sieve
for a fully independent third prime source), run in this session; scripts retained at
`/home/claude/fid/`.

1. **Construction tables**, two independent code paths (Lean-definition-literal vs.
   prose-text-literal), at `(J,K)=(3,4),(2,3)` (mandated) and `(4,6)` (fresh, `J,K≥2`):
   full `q_0..q_{L+1}` lists, `A`, `A'`, `w`, `w'`, `gamma`, prefix/suffix/fork
   agreement, `A`/`A'` strict monotonicity. All entries matched exactly; script
   assertions (would raise `AssertionError` on any mismatch) all passed. File:
   `f1_f2_construction.py`.
2. **Literal numeric claims inside Part II's four proved `example`s** (`Nat.count
   Nat.Prime 13=5`, `=11 → 4`; `q 5..q 15`; `cgamma 3 4=2`; `cgamma 2 3=4`; prefix/suffix
   digit tuples) — 18 individual assertions, all passed.
3. **Third independent cross-check of `primeIdxAbove`** via `sympy.primepi(L+3)` against
   the bisect-based implementation, at `L∈{9,7,12,1,1,20,50}` — exact match every time.
4. **`offsetSpan(H(w)) = q_{L+1}-q_0` exactly (not just `≤`)**, checked at 6 `(J,K)`
   pairs including the interiority-boundary cases `(1,1),(1,5),(5,1)` — equality held
   in every case, both for `w` and `w'`.
5. **`cJ≥1` unconditionality / `cK≥1` threshold behavior**: `cJ` computed for
   `Cg∈{1,2,10,1000}×x∈{2,3,5,10,100,10^6,10^50}` (28 combinations) — always `≥18`;
   `cK` computed for `Cg=1, x=2..100` — already `≥1` at `x=2`.
6. **Classical series identity** `Σ_{j≥1} j²2^{-j}=6` (used in prose Lemma 4.4's proof)
   — partial sum to `j=199` gave `6.0` to double precision.
7. **Monotonicity of `exp(-Ck ln(k+2))` in `C`** at `k=5`, `C∈{-2,-1,-0.5,0,0.001,0.5,
   1,2,5,10}` — strictly decreasing, confirming the `0<C`-addition-is-inert argument
   (row A.2.1 / F3).
8. **Prime-gap positivity**: `gap n` computed for `n=0..499` (500 values) — minimum `1`,
   all `≥1`, underlying the `Cg<0 ⟹ hB` unsatisfiable argument (F5).
9. **Direct admissibility + all-even verification** of `wordPointSet(w)`,
   `wordPointSet(w')` at all three `(J,K)` pairs, by literal residue enumeration modulo
   every prime `<L+10` (not merely the `p≤L+2`/`p>L+2` pigeonhole shortcut) — admissible
   and entirely even in every case.

---

# Report checksum

SHA-256 was computed via local code execution (`sha256sum`) over the complete report
text above this line — i.e. everything from the title through the end of "Computations
performed," inclusive of the closing `---`. It cannot also cover this checksum section
itself (a hash cannot include its own output), so this is the checksum of the report's
content, not of this file as a whole; that is the only coherent reading of "hash of the
complete report" once the hash has to be displayed inside the same document.

```
SHA-256: c83b0a38ca9565e114de1d50aaee2ae72c7bb395175c664c50e689d86f136537
```
