# Errata log (append-only)

Policy: `dossier/runde0.md` stays byte-frozen as the class-B pre-dissection
state. Corrections are recorded HERE, never by editing frozen files.

## ERRATUM-1 (2026-07-12) -- runde0.md section 4, Cramer headroom claim

Wrong claim (runde0): "in the Cramér random model the first length-J run
appears at log N(J) ~ J log J, doubly exponentially below the o(2^J) budget;
L is heuristically overwhelmingly true."

Correction: a run of J equal consecutive prime gaps c with p_{n+1} > J+1
forces q | c for every prime q <= J+1 (if q does not divide c, the J+1
AP-terms p_{n+1} + jc cover all residues mod q, so one is a proper multiple
of q). Hence c >= (J+1)# = e^{(1+o(1))J} -- the divisibility-blind i.i.d.
toy model misses exactly this. Under Cramer-with-congruences maximal gaps
(log p)^2, usable runs force log N(J) = e^{(1/2+o(1))J}: doubly exponential.
Lemma L's demand log N(J) = o(2^J) SURVIVES, with exponent margin
ln 2 - 1/2 = 0.19, but typicality never suffices: the run-squeeze route is
intrinsically an anti-concentration event. Honest conditional forms are
Hypothesis (P) and H-sep (run report sections 6-7; items item-0007..0010).

Source: run 20260712_fable5_1a_item0001, report C13-C15 and section 7.
Independently re-derived and verified by steering (C13 proof reproduced;
C14 spot-checked at x = 23, 28, 29). The primorial fingerprint was visible
in runde0's own numerics: the unique J = 4 run has c = 30 = 5#.

## ERRATUM-2 (2026-07-12) -- runde0.md section 6, threshold phrasing

Ambiguity: "the available run sits exactly AT the b=1 threshold" referred to
the run LENGTH (J = 4 vs log2 log p = 4.01), not to the aftermath being near
2^J. The run's trace read it as aftermath ~ 15.6 and propagated that
unverified figure across turns; the exact computation gives
|delta_{n+4} - 30| = 4.693390861..., fully consistent with runde0's own
datum 0.293 = 4.693/16. No numerical error in runde0; phrasing sharpened.
Fidelity lesson recorded under experiment question Q5.

## ERRATUM-3 (2026-07-12) -- runde0.md section 4, Lemma L insufficient as stated

Lemma L demanded runs with aftermath control |delta_{n+J} - c| <= C log p_n
without strict positivity, and runde0 dismissed the exact-hit case
delta_{n+J} = c as a "technical branch (maximal runs / first deviating
gap)". Both points fail: run 20260712_gpt56sol_1a_ab2 constructs a rational
countermodel (report C8, section 7) with positive even unbounded gaps of
size Theta(log n), arbitrarily long equal-gap runs whose common difference
is divisible by lcm(1..J+1), and EXACT tail locking delta = c at every
interior run end -- the squeeze never fires, and those runs are maximal,
refuting the sketched fix as well. Corrected sufficient forms: (L*)/(P)
with strict positivity 0 < |delta_{n+J} - c| (run fable5, Theorems A/B), or
fork-merge (run ab2, C5/C6), which needs no positivity clause because the
differing fork gap supplies the nonzero difference combinatorially.
Status of runde0's Lemma L: RETRACTED as stated; superseded.

## ERRATUM-4 (2026-07-17) -- literature.md item (b), TaTe method attribution

Wrong claim (literature.md, the item-0004 report): the TaTe irrationality
proof uses the probabilistic method plus a high-dimensional Maynard-type
sieve, with the Pilatte-based correlation machinery carrying the other
results; and the limitation quote "unlikely ... at our current level of
understanding of analytic number theory" attributed to the paper.

Correction: the attribution is swapped -- the irrationality strand
(Theorem 1.3, Section 5) is SIEVE-FREE (additivity dilation (5.2),
Hilbert cube via Gowers monotonicity, Erdos-Kac variance layer,
Pilatte-method correlations consumed only at (5.42)-(5.45)); the
Maynard-type sieve carries only the Erdos-Straus part (Theorem 1.1,
Section 2). The limitation quote is not present in v2 (25 Apr 2026);
v2 states, in the Erdos-Straus context for small k, "of comparable
difficulty to the prime tuples conjecture". literature.md stays frozen
as the item-0004 artifact; the binding record is
dossier/tate-transfer.md, Method corrections block.

Source: item-0005 first-hand full-text read of 2512.01739v2, confirmed
three ways (executor extraction agents, review R1, steering anchor
verification); see ANN-49.
