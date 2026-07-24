# Status of Erdős Problem 251

## 1. The problem and how we study it

Let $`p_n`$ denote the $`n`$-th prime. Erdős Problem 251 asks whether

$$
S=\sum_{n\ge 1}\frac{p_n}{2^n}
$$

is irrational. The series converges absolutely, but that elementary fact does not decide its arithmetic nature. The original problem remains open.

**Nothing in this project is an unconditional proof of the irrationality of** $`S`$.

The project studies the problem through consecutive prime gaps. Write $`g_n=p_{n+1}-p_n`$ and introduce weighted tails of the gap sequence. If $`S`$ were rational, those tails would eventually satisfy strong binary lattice constraints. The basic strategy is therefore to find two long prime-gap configurations that agree on long flanks but differ locally in the middle. If the corresponding tails are small enough, the local difference is incompatible with the lattice forced by rationality.

This point of view separates the problem into two parts: a deterministic arithmetic contradiction, which can be checked once the right gap configuration exists, and an analytic supply problem, which asks whether the primes actually produce enough such configurations.

## 2. What we have achieved so far

The current unconditional program has isolated a one-gap exchange configuration as a sufficient local witness. Its supply has been decomposed into three statements:

$$
\begin{aligned}
&\text{MatchedFlankLower}
+\text{TailIntersection}
+\text{RelExtensionUpper}\\
&\hspace{4em}\Longrightarrow
\text{ExchangeSupply1}
\Longrightarrow
S\notin\mathbb Z[1/2].
\end{aligned}
$$

At the pinned parameter map, `MatchedFlankLower` and `TailIntersection` are proved. The implication from the three suppliers to `ExchangeSupply1` is machine-checked, as is the final deterministic implication

$$
\text{ExchangeSupply1}
\Longrightarrow
S\notin\mathbb Z[1/2].
$$

Thus only `RelExtensionUpper` remains open in this chain.

That remaining supplier has itself been reduced to one explicit class-normalized pair estimate:

$$
\boxed{
\text{B2.pairs}
\Longrightarrow
\text{RelExtensionUpper}
\Longrightarrow
\text{ExchangeSupply1}
\Longrightarrow
S\notin\mathbb Z[1/2]
}
$$

For a class $`P`$ of filtered sites with the same left and right gap flanks, let $`N_P`$ be the class size and let $`N_{P,d}`$ count members whose middle gap equals $`d`$. Define

$$
Q(x,s)=
\sum_{P}
\frac{1}{N_P}
\sum_{\substack{d\ge2 \cr 2\mid d}}
N_{P,d}\bigl(N_{P,d}-1\bigr).
$$

`B2.pairs` asks for

$$
Q(x,s)
\le
\varepsilon_{\mathrm{pair}}
\lvert S_x^{\prime(s)}\rvert
$$

for every fixed $`\varepsilon_{\mathrm{pair}}>0`$, eventually in $`x`$, with one threshold that works uniformly in $`s`$. The proved reduction loses only a square root:

$$
\varepsilon_{\mathrm{REU}} = \sqrt{\varepsilon_{\mathrm{pair}}}.
$$

The present exchange argument needs $`\varepsilon_{\mathrm{REU}}=1/8`$, so

$$
\varepsilon_{\mathrm{pair}}=\frac1{64}
$$

is sufficient. The reduction and this constant are proved; `B2.pairs` itself remains open.

Two later audits have relativized this picture. The value $`1/64`$ is convenient slack from the current generic interface, not the logical threshold of the dyadic target: the exchange argument needs only $`\varepsilon_{\mathrm{REU}}<\delta/2`$, hence a pair coefficient below $`(\delta/2)^2`$, which at $`\delta=1/2`$ is $`1/16`$.

More importantly, a strictly weaker endpoint is already sufficient. Write $`N=\lvert S_x^{\prime(s)}\rvert`$ for the filtered site count and let $`F`$ be the number of realized flank classes. The exact finite criterion for producing one exchange witness is $`Q<N-F`$, and $`F/N\to0`$ for each fixed $`s`$ is already proved. It is therefore enough that

$$
\liminf_{x\to\infty}\frac{Q(x,s)}{N(x,s)}<1
\qquad\text{for each fixed }s.
$$

This consumes no threshold uniform in $`s`$, no statement valid at all large $`x`$, and neither `MatchedFlankLower` nor `RelExtensionUpper` at integration time. It is the weakest clean, non-tautological analytic campaign target currently known. It is not the logically weakest sufficient endpoint: the exact criterion $`Q<N-F`$ itself is strictly weaker, and is the right minimal core, but it so nearly restates the desired combinatorial conclusion that it is not a useful analytic target. Whether the collision gap is easier to prove than `B2.pairs` is open: the barrier described in Section 5 applies to both.

## 3. Why proving `B2.pairs` would already be useful

A proof of `B2.pairs` would not yet solve Erdős Problem 251. It would, however, close the first fully unconditional version of the exchange mechanism and prove

$$
S\notin\mathbb Z[1/2],
$$

that is,

$$
S\ne\frac{a}{2^s}
\qquad
\text{for all }a\in\mathbb Z,\ s\ge0.
$$

This is a natural first denominator class because the series itself is built from the binary weights $`2^{-n}`$. For a hypothetical dyadic value, repeated shifting eventually removes the denominator completely and places the weighted tails on the cleanest possible binary lattice. The present exchange theorem is designed exactly for that case.

More importantly, this step separates two difficulties that are currently entangled in the full irrationality problem. The first is the **prime-distribution problem**: do the actual primes supply matching long flanks with enough variation in the middle while satisfying the required tail filters? The second is the **denominator-uniformity problem**: can the quantitative lattice gate be made strong enough to absorb an arbitrary fixed odd denominator part?

A proof of `B2.pairs` would settle the first question for the current exchange architecture at the dyadic level. The remaining obstacle to full irrationality would then be much more sharply identified: strengthen the quantitative exchange supply so that the argument works not only for denominator $`2^s`$, but for

$$
2^s b
$$

with arbitrary fixed odd $`b`$.

So the value of `B2.pairs` is not that dyadic rationals are somehow “almost all” rationals; they are not. Its value is structural: it would show that the new unconditional mechanism genuinely works for the primes and would isolate the next missing quantitative step.

## 4. How this relates to the conditional irrationality route

The project also contains a different proof route that reaches the stronger conclusion

$$
S\notin\mathbb Q,
$$

but only from two strong open inputs: a uniform Hardy-Littlewood-type prime-tuple estimate and a Cramér-Granville pointwise prime-gap bound.

These two routes are **not consecutive stages of one implication**. The strong conditional inputs are not used to prove `B2.pairs`, `RelExtensionUpper`, or `ExchangeSupply1`, and the exchange route does not assume them.

They are nevertheless closely related because they share the same arithmetic core.

In both routes, a hypothetical rational value of $`S`$ forces a binary lattice structure on weighted prime-gap tails. A long common prefix of two gap configurations then quantizes the difference of the corresponding tails. A controlled local difference in the middle, together with matching behavior afterward and sufficiently small end tails, forces a contradiction with that lattice.

What differs is the local configuration and the way it is supplied.

The conditional route uses a **two-gap fork-merge**:

$$
\text{strong tuple input}
+
\text{strong gap bound}
\Longrightarrow
\text{two-slot fork-merge supply}
\Longrightarrow
S\notin\mathbb Q.
$$

The current exchange route seeks a simpler **one-gap exchange**:

$$
\text{B2.pairs}
\Longrightarrow
\text{one-slot exchange supply}
\Longrightarrow
S\notin\mathbb Z[1/2].
$$

The two deterministic contradictions are therefore siblings, not instances of one another. They use the same binary quantization mechanism, block identities, and small-tail principle, but the conditional route constructs a compensated two-gap change, whereas the exchange route needs only one differing middle gap between matching flanks.

This explains the role of the conditional theorem. It validates the underlying fork/lattice mechanism and proves that sufficiently rich prime-distribution input can force full irrationality. The exchange program asks a different and more targeted question: can the same arithmetic mechanism be activated by a simpler local configuration whose supply may be provable without assuming those two large open conjectural packages?

## 5. Why `B2.pairs` is difficult

The main difficulty is that matching long flanks strongly conditions the middle gap. One cannot simply treat the middle as an independent random prime gap.

An earlier target used an unnormalized count of repeated full words. That condition is actually false in the relevant asymptotic regime: the number of possible words grows only like $`x^{o(1)}`$, while the retained site population is $`x^{1-o(1)}`$. Large classes are therefore unavoidable, and raw ordered-pair counts grow quadratically with class size.

`B2.pairs` removes exactly this distortion by dividing the within-class pair count by $`N_P`$:

$$
\frac{1}{N_P}
\sum_d N_{P,d}(N_{P,d}-1).
$$

Singleton middle cells contribute nothing, and very large flank classes are put back on the correct linear scale. This normalization is essential, not cosmetic.

There is also a proved scoped barrier. The identities, capacity bounds, retention estimates, Chebyshev/PNT information, and current parameter arithmetic are compatible with an explicit smooth-gap model in which matching flanks make the middle gap almost rigid. In that model, both `B2.pairs` and `RelExtensionUpper` fail.

Therefore the existing identity-and-capacity layer alone cannot prove the target. Any successful proof must use additional information about the primes that fails in the smooth model. The most visible missing input is genuine distributional control of the middle gap after conditioning on long left and right flanks, at a word rank of order $`\log{}\log{} x`$.

That is a delicate regime. Pointwise equidistribution statements are generally too strong when individual classes are small, while ordinary per-word sieve estimates can lose constants that grow too quickly with the rank. The required statement must instead be averaged, class-normalized, uniform in the filter parameter, and strong enough to reach the explicit $`1/64`$ consumption point.

## 6. What we plan to do next

The recommended analytic campaign target is the collision gap of Section 2, which bypasses `RelExtensionUpper` entirely. Proving `B2.pairs`, or a different statement implying `RelExtensionUpper` with the required constant, remains a sufficient alternative but is no longer the primary route. The two most concrete directions are unchanged by that reordering: class-level distributional control of the middle gap after conditioning on matching flanks, or a word-grain mean-value or dispersion estimate that controls the normalized ordered-pair statistic directly without paying a prohibitive rank-dependent constant.

Computationally, that measurement has since been carried out. A frozen campaign over seven scales through $`x=10^9`$, at five values of the filter parameter, resolved the statistic by class size, middle multiplicity, and arithmetic alignment. Every realized flank class turned out to be a singleton: $`N=F`$ and $`Q=0`$ on every row. The statistic therefore vanishes identically over the entire measured range and supplies no evidence for or against the asymptotic statement. Calibrated finite models place the first flank collision many orders of magnitude beyond any reachable census, so computing this statistic further is not the bottleneck. The bottleneck is the missing prime-distribution input described in Section 5.

In parallel, the denominator-uniformity problem should be kept explicit. Once a dyadic exchange supply is available, the natural strengthening is to gain enough quantitative slack in the lattice gate to absorb every fixed odd denominator part $`b`$. A condition of the schematic form

$$
\frac{D}{2^J}\longrightarrow0
$$

would be the kind of strengthening that could eventually make the exchange contradiction work for arbitrary rational denominators.

Finally, the conditional full-irrationality route remains useful as a second research guide, but the right target there is not to attack the full Hardy-Littlewood and Cramér-Granville conjectures as black boxes. The proof uses much less: localized existence of two specially constructed gap words and sufficiently small word-conditioned end tails. Isolating and weakening those exact local requirements is a parallel route toward full irrationality.

The current research frontier is therefore deliberately split:

$$
\boxed{\text{prove the collision gap to close the next unconditional theorem}}
$$

and, in parallel,

$$
\boxed{\text{strengthen the exchange gate or localize the full-irrationality inputs}}
$$

with the long-term goal of passing from

$$
S\notin\mathbb Z[1/2]
$$

to

$$
S\notin\mathbb Q.
$$
