# Status of Erdős Problem 251

## The problem

<!-- sources: chain-main, literature-problem -->

Let $`p_n`$ denote the $`n`$-th prime. Erdős Problem 251 asks whether

$$
S=\sum_{n\ge 1}\frac{p_n}{2^n}
$$

is irrational. The series converges absolutely, but that elementary fact does not decide its arithmetic nature. The original problem remains open.

**Nothing in this project is an unconditional proof of the irrationality of $`S`$.**

The project studies the problem through consecutive prime gaps. Write $`g_n=p_{n+1}-p_n`$. Summation and tail identities turn a hypothetical rational representation of $`S`$ into strong lattice restrictions on weighted tails of the gap sequence. The main strategy is then to find two long prime-gap words with matching flanks but different middle behavior. Such a configuration conflicts with those lattice restrictions once its end tails are sufficiently small.

## The conditional result

<!-- sources: chain-main -->

There is a reviewed conditional theorem. It assumes two open analytic hypotheses.

Hypothesis A is a uniform two-sided prime-tuple estimate. In the exact form used here, it applies simultaneously to every admissible even-offset set whose cardinality is at most $`4\log{}\log{} x`$ and whose span is at most $`(\log{} x)^3`$. Its predicted Hardy–Littlewood mass is bounded above and below by fixed factors. This is a conjectural uniform statement, not a proved theorem.

Hypothesis B is the pointwise Cramér–Granville prime-gap bound: for some fixed $`C_g`$, all sufficiently late gaps satisfy $`g_n\le C_g(\log{} p_n)^2`$. This hypothesis is also open.

Assuming both hypotheses, the repository proves that $`S`$ is irrational. The conclusion is therefore proved modulo the two explicitly named assumptions. It would be incorrect either to call the assumptions established or to describe the original problem as solved. The result is also purely asymptotic; no effective threshold is claimed.

## What is machine-checked

<!-- sources: chain-mechanism, lean-layout -->

The deterministic implication layer has been checked in Lean. This includes the convergence and tail identities, the eventual lattice and parity consequences of rationality, the quantization step for repeated prefixes, the fork–merge contradiction, the conditional counting construction, and the final composition from Hypotheses A and B to irrationality. The checked theorem depends on the named hypotheses and ordinary classical axioms, not on an unconditional proof of those hypotheses.

The formal development therefore verifies the logic of the implication and much of the combinatorial supply machinery. It does not formalize a solution of the original problem. The unconditional target remains intentionally open in the formal source tree. A separate checked integrator shows how three supply propositions—`MatchedFlankLower`, `RelExtensionUpper`, and `TailIntersection`—would produce the exchange configuration needed by a related deterministic argument. That integrator likewise does not prove its analytic suppliers.

## Unconditional progress

<!-- sources: item0020-verdict, claim-c1, relext-props -->

The current unconditional progress concerns filtered prime sites. Fix a scale $`x`$ and a threshold $`s`$. A filtered site belongs to $`S_x^{\prime(s)}`$ when its index is beyond $`s`$, its gap window of length $`L`$ obeys the pinned aggregate cap, and two weighted gap tails obey the pinned near and far caps. The word is split into a prefix of length $`J`$, one middle gap, and a suffix of length $`K`$. A side pair $`P=(a,c)`$ records the prefix and suffix. Its class size $`N_P`$ is the number of filtered sites with those same flanks. The family $`\mathrm{Fam}_2(S_x^{\prime(s)})`$ consists of side-pair classes with at least two members.

At the pinned parameter map, the following statement is proved asymptotically:

$$
\sum_{P\in\mathrm{Fam}_2(S_x^{\prime(s)})}N_P
\ge \frac12\lvert S_x^{\prime(s)}\rvert.
$$

The quantifiers matter. One may fix $`\delta=1/2`$; then for every $`s`$ there is a threshold depending on $`s`$, and the inequality holds for all sufficiently large $`x`$. In fact every fixed $`\delta<1`$ eventually works. This is `MatchedFlankLower` at the pinned map.

The proof is a capacity argument. The number of possible realized side pairs is only $`x^{o(1)}`$, while the retained filtered-site mass is $`x^{1-o(1)}`$. Singleton side-pair classes therefore carry a negligible fraction of the site mass. This argument is unconditional at the dossier level, but it begins to have content only at enormous asymptotic scales. It makes no finite-scale claim.

`TailIntersection`, the positive-density lower bound for the filtered set, was already proved. Consequently the three-part supply chain now lacks only `RelExtensionUpper`.

## The remaining estimate

<!-- sources: frontier-verdict, claim-c3, relext-definitions -->

For a realized side-pair class $P$, let $`N_{P,d}`$ be the number of its members whose middle gap equals the even integer $`d\ge2`$. Define

$$
Q(x,s)=
\sum_{P\in\mathrm{Fam}(S_x^{\prime(s)})}
\frac{1}{N_P}
\sum_{\substack{d\ge2 \cr 2\mid d}}
N_{P,d}\bigl(N_{P,d}-1\bigr).
$$

The explicit surviving sufficient target, called `B2.pairs`, asks that for every $`\varepsilon_{\mathrm{pair}}>0`$, uniformly in $`s`$ once $`x`$ is sufficiently large,

$$
Q(x,s)\le
\varepsilon_{\mathrm{pair}}\lvert S_x^{\prime(s)}\rvert.
$$

`B2.pairs` remains open. It is a class-normalized ordered-pair estimate: singleton classes contribute nothing, and division by $`N_P`$ prevents very large classes from distorting the scale. The repository proves that `B2.pairs` at $`\varepsilon_{\mathrm{pair}}`$ implies `RelExtensionUpper` at

$$
\varepsilon_{\mathrm{REU}}=\sqrt{\varepsilon_{\mathrm{pair}}}.
$$

The current pigeonhole argument consumes $`\varepsilon_{\mathrm{REU}}=1/8`$, so the corresponding pair target is $`\varepsilon_{\mathrm{pair}}=1/64`$. The implication and these constants are proved; the pair estimate itself is not.

## Why the remaining step is difficult

<!-- sources: claim-c4, frontier-verdict -->

Several tempting counting routes lose too much. In particular, the older sufficient condition $`W2=o(\lvert S'\rvert)`$, based on an unnormalized full-word pair count, is false at the pinned depths. The failure is structural: asymptotically large word classes create quadratically many ordered pairs compared with linearly many sites. The factor $`1/N_P`$ in `B2.pairs` is therefore essential rather than cosmetic.

There is also a precise but scoped barrier. An explicit deterministic smooth-gap system satisfies the identity, capacity, retention, Chebyshev, and prime-number-theorem layer used by the present program, yet it is almost entirely middle-rigid and violates both `B2.pairs` and `RelExtensionUpper`. Thus those named inputs alone cannot imply the target. A successful argument must use some fact about the primes that fails in this smooth model. Distributional control of the middle slot, at the growing word rank relevant here, is the most visible candidate family.

This is not a general impossibility theorem. It neither says that `B2.pairs` is unprovable nor rules out methods using additional prime-number input.

## What is not claimed

<!-- sources: chain-main, final-observations, frontier-verdict -->

The original irrationality problem is not solved. Hypotheses A and B are not proved. The machine-checked result is a conditional implication, not a formalization of an unconditional solution. `RelExtensionUpper` is open, and `B2.pairs` is open.

Finite computations have measured class multiplicities, repeated-middle shares, and local quotient behavior at accessible scales. Those observations are useful for choosing plausible statements and rejecting poor normalizations. They are measured, direction-only evidence. The finite-scale evidence is not an asymptotic proof; indeed the proved capacity argument operates in a regime far beyond the measured range. Heuristic middle laws and singular-series interpretations are motivation only and carry no proved conclusion.

Finally, the smooth-gap construction locates the limit of a named tool layer. It must not be promoted to the claim that no unconditional proof exists or that every possible non-distributional idea fails.

## Current next steps

<!-- sources: frontier-verdict, final-observations -->

The central mathematical task is to prove `B2.pairs`, or to prove a different statement strong enough to yield `RelExtensionUpper` with the required constant. The most concrete routes are class-level equidistribution for the middle gap and word-grain upper mean-value estimates at rank comparable with $`\log{}\log{} x`$. Either route must retain the filters-first quantifiers and handle the mass of arithmetically aligned classes rather than assuming it is typical.

On the computational side, the full class-normalized statistic $`Q(x,s)`$, separated by class-size and alignment strata, can refine calibration of the distance to $`1/64`$. Such measurements can guide a proof target but cannot establish its asymptotic form. On the formal side, the proved cardinality argument for `MatchedFlankLower` could eventually be connected to the existing checked supply integrator; that would remove one stated supplier without changing the open analytic core.
