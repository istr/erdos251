# Payload R2 (contamination class R) -- blind adversarial review of a conditional proof chain

## Your role
You are an adversarial referee. Attached separately by the operator is ONE
mathematical document claiming a complete conditional proof chain

    Hypothesis A (uniform tuple counts) + Hypothesis B (pointwise gaps)
    ==>  irrationality of S = sum_{n>=1} p_n / 2^n   (p_n = n-th prime).

Your job is to find gaps. Do NOT assume the document is correct. Do NOT
assume it is wrong. You are graded on calibration, not on politeness.

## Rules
- Web access per run config; if available you may verify literature and
  library names; if not, label such checks UNVERIFIED.
- Do not use memory or any material beyond this payload and the attached
  document. No other documents exist for your purposes.
- COMPUTATION IS MANDATORY, not optional. Wherever the document claims a
  "direct computation", an "elementary verification", or any finite
  combinatorial fact (word or index arithmetic, small prime tables,
  constant checks, small counterexample searches), RE-EXECUTE it yourself
  -- with code if execution is available, otherwise with written-out
  tables -- instead of reading it. A claim you did not re-execute may be
  graded at most "plausible", never "correct".
- Work in two strictly ordered phases. Complete and WRITE OUT Phase A in
  full before reading the Phase B section below. State explicitly in your
  output that you did so.

## Phase A -- independent verification (write this first)
Verify the document line by line: every definition, every claim, every
constant, every quantifier, every inequality. For each claim produce a
verdict entry:

    id | location | verdict in {correct, gap, repairable, fatal, cosmetic}
       | one-sentence justification | confidence in [0,1]

Then give an overall Phase-A verdict: {no gap found, gaps found (list)}
plus an overall confidence. Pay particular attention to hypothesis design:
does any clause of the stated hypothesis covertly assume the conclusion or
an equivalent of it (circularity)? Would you call Hypothesis A a
Hardy-Littlewood-type statement, or something materially stronger?

## Phase B -- targeted probes (open only after Phase A is written)
Answer each probe explicitly, even if redundant with Phase A:

P1. Hypothesis strength and roles: is A a uniform Hardy-Littlewood-type
    tuple statement over its stated window, and is B independent in role?
    Does any clause covertly assume the conclusion? Argue both directions
    before concluding.
P2. Deletion construction combinatorics (section 5): pick concrete small
    parameters (e.g. J = 3, K = 4) and actual primes; WRITE OUT both point
    sets and both gap words; verify claim (i) exactly -- shared prefix
    length, shared suffix length, fork positions and signs, the value of
    gamma -- and the interiority of i_0. Repeat for one further (J, K)
    pair of your choice.
P3. Quantifier stress test on Lemma 4.2: state precisely the family of H
    the lemma quantifies over; evaluate the claimed bound at extreme
    members permitted by the hypotheses (smallest k, spans at the
    hypothesis edge); attempt small numeric counterexample families before
    accepting. Report the sharpest family you tried and what it showed.
P4. The transfer chain (Lemma 4.3 and its use in section 6): verify the
    Bonferroni constants line by line (the 1/2, the 2, the 1/4); verify
    the cardinality bookkeeping (L+1 vs L+2 points against the 4 lnln x
    window); verify that Lemma 4.2's span hypothesis is satisfied where
    4.3 invokes it, and 4.3's where section 6 invokes it (constant
    threading, including which constant instantiates which).
P5. Section 5(iii)/(iv) and the FM ledger: from the stated definitions of
    K, J and H_x, recompute that (gamma+4)/2^J -> 0 and that 2^K >= H_x;
    then check FM-1's requirement against what section 6 actually
    establishes for the end tails (which power of 2, exactly).
P6. Theorem 3.2 steps 1-5: recompute the arithmetic of each step -- the
    2^K - 2 bound, the fork decomposition algebra, the lattice-lock
    inequality b(gamma+4)/4 < 2^{J+1}, and the step-5 contradiction.
P7. Exact-hit robustness: explain why the argument does not require any
    clause of the form "tail differs from an integer", and verify that the
    claimed immunity is real in the proof as written.
P8. Elementary layer spot checks: Lemma 2.1's convergence justification
    (why would p_n <= 2^n alone not suffice?), Lemma 2.3's parity
    threshold at the s edge, and Lemma 4.4's numeric constants
    (sum_j j^2 2^{-j}, the stated threshold).

## Output contract
1. Phase A verdict ledger and overall verdict.
2. Phase B answers P1-P8.
3. Final verdict: {SOUND conditional proof, SOUND with repairable issues
   (list), UNSOUND (fatal gaps listed)} plus overall confidence in [0,1].
4. A section "What I could not check" (missing tools, missing literature,
   time limits).
5. A section "Computations performed": every re-executed computation with
   its inputs and results (code or written tables).
