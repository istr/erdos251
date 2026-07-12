# Payload 1b (contamination class C) -- briefed stage, revision 2 (post-1a)

## Rules
- Web access per run config; if unavailable, label literature-based claims
  UNVERIFIED unless proved inline. Never invent citations.
- Distinguish clearly: proved / sketch / heuristic. Mark every use of the
  briefing facts (primorial, parity, countermodel, empirics) explicitly.

## Task
Erdős Problem #251. Let p_n denote the n-th prime (p_1 = 2). Target: rigorous
progress on the irrationality of S = sum_{n>=1} p_n / 2^n.

PRIMARY OBJECTIVE (revised after stage 1a): a complete, precise proof of

    HL_quant  ==>  fork-merge hypothesis (FM)  ==>  S is irrational,

where HL_quant is a quantified Hardy-Littlewood-type package you state
exactly (expected shape: prime tuples/patterns in windows of k <= C loglog x
gaps, shifts <= (log x)^3, with polylogarithmic error savings; name the
uniformity range and every place it is spent), and (FM) is stated below.
Structure the proof for Lean 4 along the named skeleton at the end.
SECONDARY: the same for the v2-block or word-power route. TERTIARY: entropy
(statistical control of the binary expansion) or a base-2 uniformization of
a ScPu11-style elimination engine. Deliver the primary completely before
polishing anything else.

Lean target (0-indexed Nat.nth; the Lean sum equals 2S):

    theorem erdos_251 : Irrational (tsum fun n : Nat => (Nat.nth Nat.Prime n : Real) / 2 ^ n)

## Frozen prior analysis (identical to blind stage)

Notation: gaps g_n = p_{n+1} - p_n.

1. Identities (elementary, verified numerically to 1e-147):
   - sum_{n>=1} g_n / 2^n = S - 2.
   - Tail u_n = sum_{k>=1} p_{n+k}/2^k satisfies u_{n+1} = 2 u_n - p_{n+1}.
   - delta_n := u_n - p_{n+1} = sum_{j>=1} g_{n+j}/2^j, the geometric weighted
     average of future gaps; delta_n >= 2; delta_n ~ log n on average;
     delta_{n+1} = 2 delta_n - g_{n+1}.
   - If S = a/(2^s b), b odd, then b delta_n is integral for all n >= s;
     conversely a single such n makes S rational.
2. Calibration: sum n/2^n = 2 kills growth/monotonicity/average arguments;
   sum 2^{-p_n} is trivially irrational; the difficulty is the carries.
3. Vacuity warning: d_{n+1} = 2 d_n - b g_{n+1} propagates integrality
   forward; no congruence pattern on gaps follows from rationality. Only size
   arguments carry.

## Briefing part I: thread and literature (2026-07-11 dissection)

1. T. Tao (problem thread, 2025-10-07, paraphrase): partial summation reduces
   the problem to irrationality of sum g_n/2^n; a sufficiently quantitative
   and uniform prime tuples conjecture, giving statistical control over
   windows of about log log n consecutive gaps (each typically of size about
   log n), could rule out periodicity of the binary expansion; Shannon
   entropy suggested as a tool. Nobody has executed this.
2. [ScPu11] = J.-C. Schlage-Puchta, Acta Arith. 126 (2007) 295-303,
   arXiv:1105.1451: factorial-world engine. Rationality forces
   near-integrality of leading tail terms; recursive cross-elimination over
   consecutive n leaves polynomials in the gaps; Selberg-sieve upper bounds
   show no nonzero gap-polynomial vanishes on a positive proportion of n
   (bounded windows); van der Corput discrepancy closes. In base 2 the same
   scheme needs uniformity in window size k ~ log log n, and lower-bound
   (existence) input which Selberg upper bounds do not give.
3. The g_1...g_n generalization on the problem page was resolved NEGATIVELY
   (2026-04-15) by adversarial telescoping (choose c_{n+1} = c_n g_n - p_n).
   This exploits adaptive denominators and says NOTHING about base 2. Do not
   spend budget there.

## Briefing part II: stage-1a route landscape (all implications PROVED)

Five mechanisms, all on the same loglog window budget. b = odd denominator
part; parity fact below sharpens A, C, E, G thresholds by a factor 2.

A. Equal-run squeeze (P)/(L*): run g_{n+1}=...=g_{n+J}=c gives
   delta_n - c = 2^{-J}(delta_{n+J} - c). Needs existence PLUS strict
   anti-concentration 0 < |delta_{n+J} - c| < 2^{J+1}/b.
C. H-sep: a repeated length-J gap pattern at n, m forces
   b(delta_{n+J} - delta_{m+J}) in 2^{J+1} Z; needs a pair with
   0 < |difference| < 2^{J+1}/b.
E. v2-blocks: with backward code C_{n,J} = sum_{i=1..J} 2^{J-i} g_{n+i},
   rationality forces b*delta_{n+J} >= 2^{min(J, v2(C_{n,J}))}. Hypothesis:
   blocks with min(J, v2(C)) - log2 delta_{n+J} -> infinity. Existence-only.
F. Word-powers: word w = (c_1..c_r), B_w = sum 2^{r-i} c_i,
   alpha_w = B_w/(2^r - 1) = m_w/q_w reduced. K adjacent repeats give
   delta_n - alpha_w = 2^{-Kr}(delta_{n+Kr} - alpha_w); if q_w does not
   divide b then |delta_{n+Kr} - alpha_w| >= 2^{Kr}/(b q_w). Hypothesis:
   words with q_k -> infinity and q_k |delta_end - alpha_k| / 2^{K_k r_k}
   -> 0. Existence-only; constant words have q_w = 1 (degenerate case A).
G. FORK-MERGE (primary): two sites n < m with common gap prefix W (|W| = J),
   differing next gaps a != a', common suffix V (|V| = K). Rationality plus
   |delta_{n+J} - delta_{m+J}| < 2^J/b forces exact equality at the fork;
   the fork then gives tail difference a' - a != 0; the suffix doubles it to
   2^K |a - a'| >= 2^{K+1}; contradiction with the four tails' bound
   H < 2^K. Sufficient: configurations with min(n_r, m_r) -> infinity and
   H_r/2^{J_r} -> 0, H_r/2^{K_r} -> 0. Existence-only; immune to exact
   locking; b enters only the prefix condition.

## Briefing part III: hard structural facts (respect these)

1. PRIMORIAL OBSTRUCTION (proved): a J-run of gap c with p_{n+1} > J+1
   forces q | c for every prime q <= J+1, hence c >= (J+1)#. Exactly
   x# <= 2^x for x in {2,3,4,5,6,8,9,10,12,15,16,28}; x# > 2^x for all
   x >= 29. Consequence: any hypothesis demanding long equal-gap runs of a
   FIXED value, or locking thresholds 2^J >= b*c at large J, is FALSE.
   Two independent stage-1a attempts died on this. Long runs of a fixed
   WORD die the same way through the word sum; small repeat counts K of
   growing words evade it.
2. PARITY (proved): b delta_n is an EVEN integer for all n >= s+1 (gaps are
   even from index 2, b odd). All thresholds above double.
3. EXACT-LOCKING COUNTERMODEL (proved): there is a rational series with
   positive even unbounded gaps of size Theta(log n), arbitrarily long
   equal-gap runs whose difference is divisible by lcm(1..J+1), and
   delta = c exactly at every interior run end -- the squeeze never fires.
   Any equal-run hypothesis must therefore include strict positivity;
   fork-merge needs no such clause.
4. STATISTICS NO-GO (proved twice, independently): sequences matching
   parity, monotonicity, growth profile, and PNT-grade counting can have
   rational sums. Only prime-specific arithmetic structure can win.

## Briefing part IV: empirics (primes below 3e7, rigorous where stated)

- Unique J = 4 run: c = 30 = 5# (primorial fingerprint), at p = 9,843,019;
  aftermath |delta_{n+4} - 30| = 4.6934 (exact enclosure).
- 262,687 repeating J = 6 gap patterns; minimal nonzero aftermath
  difference 1.7e-6 (float-grade): fork-merge-type configurations are
  birthday-abundant in data.
- min delta_n = 2.7943 (exact); 1907 sites with delta_n < 4 below 3e7.
- Finite exclusions already on record: any rational S has denominator
  > 10^298; S != a/(2^s b) for all s <= 1,857,459 and odd b <= 99,999.

## Output contract
1. CLAIMS ledger: id, exact statement, status {proved, sketch, heuristic,
   false-start}, dependencies, confidence in [0,1].
2. HL_quant stated in full, prose plus Lean-ready form; every use marked.
3. Main writeup referencing claim ids; every use of briefing facts marked.
4. Lean-ready statements for the whole chain; suggested skeleton names:
   delta_block, rational_delta_eventually_lattice,
   repeated_block_quantization, fork_merge_contradiction,
   erdos_251_of_small_tail_fork_merge.
5. "Where I am stuck": the exact missing ingredient, if any.
