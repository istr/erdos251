# Payload R3-FID (contamination class R) -- blind transcription-fidelity review

## Your role
You are a transcription-fidelity referee. Attached separately by the
operator is ONE object with three labeled parts: Part I a prose
mathematical source (sections 1, 2, 4, 5), Part II a Lean 4 statement
file claiming to transcribe prose sections 4-5 as sorried statements,
Part III frozen Lean context (NOT under assessment; it exists so every
Part-II symbol resolves). The claim under review is:

    every statement in Part II faithfully transcribes the prose
    statement it references in Part I.

You are NOT asked whether the prose is true, whether the sorries are
provable, or whether the mathematics is a good idea. You are asked
whether the Lean statements SAY what the prose says. A statement that is
weaker, stronger, or different from its prose source is a finding even
if it is mathematically reasonable. Do NOT assume the transcription is
correct. Do NOT assume it is wrong. You are graded on calibration.

## Rules
- Web access is OFF. Label any check you cannot perform as UNVERIFIED.
- Do not use memory or any material beyond this payload and the attached
  object. No other documents exist for your purposes.
- COMPUTATION IS MANDATORY, not optional. Every finite claim -- the
  concrete construction tables, prime lists, gap words, index arithmetic,
  cardinalities -- must be RE-EXECUTED by you (code if available,
  written-out tables otherwise), never accepted by reading. A claim you
  did not re-execute may be graded at most "plausible", never "correct".
- Judge Part II against Part I only. Pointers to "section 6" or to
  out-of-scope Lean names are opaque; note them, do not speculate.
- Part III is context: read it to resolve symbols (`HLQuantA`,
  `CramerGranville`, `singularSeries`, `modelMass`, `IsAdmissible`,
  `q`, `gap`, `delta`, `SameBlock`). If a Part-II fidelity question
  turns on a Part-III definition (e.g. what `HLQuantA` binds), say so
  explicitly; do not audit Part III beyond that.
- Work in two strictly ordered phases. Complete and WRITE OUT Phase A in
  full before reading the Phase B section below. State explicitly in
  your output that you did so.

## Phase A -- statement-by-statement fidelity ledger (write this first)
For each of the 12 sorried statements and for the definition cluster
(`IsConsecRealization`, `wordPointSet`, `offsetSpan`, `oneExtensions`,
`consCount`, `cK`, `cJ`, `cL`, `cI`, `tailBudget`, `primeIdxAbove`,
`cprime`, `cElem`, `cElem'`, `cword`, `cword'`, `cgamma`), produce:

    name | prose ref | verdict in {faithful, deviation-weaker,
      deviation-stronger, deviation-neutral, unfaithful}
      | one-sentence justification | confidence in [0,1]

Check at minimum: quantifier structure and order (what is existential,
what is universal, what is threaded as a parameter), constant placement,
windows and budgets, inequality directions and strictness, index
conventions (0- vs 1-based; every paper-to-Lean index shift), fork
orientation, cardinality clauses, span shapes, and every hypothesis
present in Lean but absent in prose or vice versa. The Lean docstrings
declare some deviations and omissions; verify each declaration instead
of trusting it, and hunt for undeclared ones. Then give an overall
Phase-A verdict plus confidence.

## Phase B -- targeted probes (open only after Phase A is written)
Answer each probe explicitly, even if redundant with Phase A:

F1. Construction tables: from the LEAN definitions alone (`primeIdxAbove`,
    `cprime`, `cElem`, `cElem'`, `cword`, `cword'`, `cgamma`), compute at
    (J, K) = (3, 4) and (2, 3): the prime list q_0..q_{L+1}, both point
    sets, both full gap words, gamma. Independently compute the same from
    the PROSE construction. Compare entry by entry, including the four
    `example` tables in Part II. Repeat both computations at one fresh
    (J, K) pair of your choice with J, K >= 2.
F2. Deletion encoding: verify that `cElem`/`cElem'` (the `if`
    enumerations) produce exactly A = {q_0,...,q_{L+1}} minus {q_{i_0+1}}
    and A' = ... minus {q_{i_0}}, monotone, and that
    `wordPointSet (cword J K) (cL J K)` equals the 0-based set A - q_0
    elementwise at your tested (J, K) values.
F3. Lemma 4.1 transcription: the two clauses and their shared constant,
    the added `0 < C`, the dropped `x^{1-o(1)}` phrasing, and the
    bookkeeping k = |H| - 1 (so ln(k+2) becomes ln(|H|+1) and the
    exponent's (k+1) becomes |H|): classify each transformation as
    equal, weaker, or stronger, with a one-line proof of the
    classification.
F4. Lemmata 4.2/4.3: the range of t (even, 0 < t < D, not in H,
    insert-admissible) against the prose; both span-hypothesis shapes
    (kappa k ln(k+2) with k = card - 1 versus kappa L ln(L+2)); 4.3's
    conclusion pair (M/4 <= N_cons and 1 <= N_cons) against the prose
    chain N_cons >= (1/4) M >= 1; and the OMISSION of an evenness
    hypothesis in the Lean 4.3 together with its docstring's
    derivability argument -- verify or refute that argument.
F5. Lemma 4.4 index shift: prose delta_nu <= 3 C_g (ln p_nu)^2 for
    nu >= nu_1 versus the Lean `delta (n + 1) <= 3 * Cg * log (q n) ^ 2`:
    check the nu = n + 1 map exactly, and check that the hypothesis `hB`
    is exactly the body of the frozen `CramerGranville`.
F6. Coverage of section 5's quantitative claims: map every prose clause
    of 5(iii), 5(iv) and "Fix x large" to a conjunct of `cspan_le`,
    `cfm2_tendsto` or `cbudget`, and list every prose clause with NO
    Lean counterpart. Judge whether the docstrings' declared
    non-transcriptions are exactly that list.
F7. Hidden-strengthening scan: list every Lean-side hypothesis with no
    prose counterpart (e.g. `0 in H`, evenness of offsets, `1 <= J`,
    `1 <= K`, `1 <= kappa`, `0 < C`) and classify each as prose-implied
    (say where) or a genuine strengthening/weakening of the statement.

## Output contract
1. Phase A fidelity ledger and overall verdict.
2. Phase B answers F1-F7.
3. Final verdict: {FAITHFUL, FAITHFUL with documented deviations (list
   them), UNFAITHFUL (list the failures)} plus overall confidence in
   [0,1].
4. A section "What I could not check" (missing tools, time limits).
5. A section "Computations performed": every re-executed computation
   with its inputs and results (code or written tables).
