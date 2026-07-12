# Payload R1 (contamination class R) -- blind cross-review of a conditional proof

## Your role
You are an adversarial referee. Attached separately by the operator is ONE
mathematical document claiming a complete conditional proof chain

    HL_quant  ==>  fork-merge hypothesis (FM)  ==>  irrationality of
    S = sum_{n>=1} p_n / 2^n   (p_n = n-th prime).

Your job is to find gaps. Do NOT assume the document is correct. Do NOT
assume it is wrong. You are graded on calibration, not on politeness.

## Rules
- Web access per run config; if available you may verify literature and
  Lean/Mathlib names; if not, label such checks UNVERIFIED.
- Do not use memory or any material beyond this payload and the attached
  document. No other documents exist for your purposes.
- Work in two strictly ordered phases. Complete and WRITE OUT Phase A in
  full before reading the Phase B section below. State explicitly in your
  output that you did so.

## Phase A -- independent verification (write this first)
Verify the document line by line: every definition, every claim, every
constant, every quantifier, every inequality. For each claim produce a
verdict entry:

    id | location | verdict in {correct, gap, repairable, fatal, cosmetic}
       | one-sentence justification | confidence in [0,1]

Then give an overall Phase-A verdict: {no gap found, gaps found (list)} plus
an overall confidence. Pay particular attention to hypothesis design: does
any clause of the stated hypothesis covertly assume the conclusion or an
equivalent of it (circularity)? Would you call the hypothesis a
Hardy-Littlewood-type statement, or something materially stronger?

## Phase B -- targeted probes (open only after Phase A is written)
Answer each probe explicitly, even if redundant with Phase A:

P1. The model-entropy clause (averaged fork anti-concentration with a fixed
    constant): is it a statement about the explicit local model only, and is
    it plausibly provable for the standard singular-series model? Argue both
    directions before concluding.
P2. Verify that the total pattern count T_x equals (1 - o(1)) |I_x| (every
    start index carries some word; only the span filter removes indices).
    If the document does not need this step, say why.
P3. Verify the four-tails bookkeeping: does "good site" control BOTH needed
    tail offsets per site, so that two good sites yield all four bounds?
P4. Verify the M_x(d) = 0 clause of the counting axiom: is N_x(d) = 0 for
    non-admissible words actually unconditional, and is the clause needed?
P5. Recompute the constants table: window length vs block length, the
    relative-error exponent vs the removal exponents, and the inequality
    that makes H / 2^J tend to 0. State each numeric check.
P6. The epsilon bookkeeping (1 + eps)/(1 - eps) style steps: verify each.
P7. Exact-hit robustness: explain why the argument does not require any
    clause of the form "tail differs from an integer", and verify that the
    claimed immunity is real in the proof as written.

## Output contract
1. Phase A verdict ledger and overall verdict.
2. Phase B answers P1-P7.
3. Final verdict: {SOUND conditional proof, SOUND with repairable issues
   (list), UNSOUND (fatal gaps listed)} plus overall confidence in [0,1].
4. A section "What I could not check" (missing tools, missing literature,
   time limits).
