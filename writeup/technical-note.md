# Technical note on the current reduction

## Notation and filtered sites

<!-- sources: relext-definitions, relext-props -->

Let $`p_1=2<p_2=3<\cdots`$ be the primes and set

$$
g_n=p_{n+1}-p_n.
$$

$$
S=\sum_{n\ge1}\frac{p_n}{2^n}.
$$

The relative-extension framework fixes a scale $`x`$ and a depth threshold $`s`$. At the pinned parameter map, the gap window has the form

$$
\begin{aligned}
&(a_1,\ldots,a_J,d,c_1,\ldots,c_K),\\
&L=J+1+K.
\end{aligned}
$$

where $`J=K=\lceil\log_2{} D\rceil`$, $`D`$ is a fixed constant multiple of $`\log{} x`$, and the middle width is one. The set $`S_x^{\prime(s)}`$ contains the prime sites beyond $`s`$ that satisfy an aggregate window bound of length $`L`$ and both the near and far weighted-tail caps. These filters are part of the set definition; they are not imposed after counting.

A side pair is $`P=(a,c)`$, consisting of the prefix and suffix gap words. For a finite filtered set, define

$$
N_P=\lvert \lbrace n\in S_x^{\prime(s)}:n\text{ has side pair }P\rbrace \rvert
$$

and, for an even middle gap $`d\ge2`$,

$$
N_{P,d}=\lvert \lbrace n\in S_x^{\prime(s)}:n\text{ has side pair }P\text{ and middle }d\rbrace \rvert.
$$ 

The realized family $`\mathrm{Fam}(S_x^{\prime(s)})`$ consists of the classes with $`N_P\ge1`$; its subfamily $`\mathrm{Fam}_2(S_x^{\prime(s)})`$ consists of those with $`N_P\ge2`$. Exact partition identities give $`\sum_dN_{P,d}=N_P`$ and $`\sum_PN_P=\lvert S_x^{\prime(s)}\rvert`$.

## The conditional irrationality theorem

<!-- sources: chain-main -->

The reviewed theorem assumes two analytic inputs. Hypothesis A is a uniform two-sided Hardy–Littlewood-type estimate for all admissible even-offset sets in a growing but explicit cardinality and span budget. Hypothesis B is a pointwise Cramér–Granville bound $`g_n\le C_g(\log{} p_n)^2`$ for all sufficiently large $`n`$. Both hypotheses remain open.

Under A and B, $`S`$ is irrational. Hypothesis A supplies consecutive realizations of carefully designed gap words: it first counts the associated prime tuples, then uses a one-point-extension estimate to remove tuples with an intervening prime. Hypothesis B bounds the final weighted tails of those realizations. The construction produces the fork–merge configurations needed by the deterministic contradiction.

The theorem is conditional and asymptotic. Its proof does not establish either analytic hypothesis, and it does not solve the original problem unconditionally.

## The deterministic contradiction mechanism

<!-- sources: chain-mechanism, lean-layout -->

Define the shifted weighted tail

$$
\delta_n=\sum_{j\ge1}g_{n+j}2^{-j}.
$$

Absolute convergence licenses the block identity

$$
\delta_n=\sum_{i=1}^{T}g_{n+i}2^{-i}+2^{-T}\delta_{n+T}.
$$

If $`S`$ were rational, write its denominator as a power of two times an odd integer $`b`$. Past a fixed index, $`b\delta_n`$ lies on an even integer lattice. Hence two sites with an identical prefix of length $`J`$ have a tail difference at the end of that prefix lying in $`2^{J+1}\mathbb Z/b`$.

The fork–merge configuration uses two gap words with a common prefix of length $`J`$, two middle gaps differing by $`(+\gamma,-\gamma)`$, and a common suffix of length $`K`$. Small end tails make the difference after the prefix strictly smaller than one nonzero lattice step. Quantization therefore forces equality of those prefix-end tails. But the explicit two-slot fork and common suffix then force an end-tail difference of magnitude at least $`2^{K+1}`$, contradicting the strict bound below $`2^K`$. This deterministic layer, including its composition with the named analytic assumptions, is machine-checked.

## Matched-flank classes

<!-- sources: relext-definitions, relext-props -->

The unconditional supply program seeks a simpler Hamming-one exchange: two filtered sites in the same side-pair class but with different middle gaps. If every realized class were middle-rigid, one could choose its common middle $`d_P`$, obtaining $`N_{P,d_P}=N_P`$. Multi-member mass would then force a large repeated-middle contribution. An upper bound on every such adversarial selection would contradict rigidity.

This is separated into three propositions. `MatchedFlankLower` supplies enough mass in classes with $`N_P\ge2`$. `RelExtensionUpper` limits the repeated-middle mass for arbitrary selections of $`d_P`$. `TailIntersection` ensures that the filtered population is nontrivial and remains a positive fraction of the underlying sites. The checked integrator proves that these three statements yield the required exchange supply. At the pinned map, the first and third statements are proved at dossier level; the second is open.

## The proved matched-flank lower bound

<!-- sources: claim-c1, item0020-verdict -->

At the pinned parameter map, for one fixed $`\delta=1/2`$, every $`s`$ has a threshold $`x_2(s)`$ such that for all $`x\ge x_2(s)`$,

$$
\begin{aligned}
\sum_{P\in\mathrm{Fam}_2(S_x^{\prime(s)})}N_P
&\ge
\frac12\lvert S_x^{\prime(s)}\rvert.
\end{aligned}
$$

Indeed, every fixed $`\delta<1`$ eventually works. The order of quantifiers is essential: $`\delta`$ is fixed first, $`s`$ is arbitrary, and the threshold for sufficiently large $`x`$ may depend on $`s`$.

The proof is purely a cardinality comparison. Every realized side pair is a $`(J+K)`$-tuple of positive even gaps whose total size is bounded by the window cap. Stars and bars gives a side-pair capacity of $`x^{o(1)}`$. On the other hand, `TailIntersection`, a Chebyshev inversion, and the prime number theorem give retained site mass $`\lvert S_x^{\prime(s)}\rvert=x^{1-o(1)}`$ for fixed $`s`$. Since

$$
\begin{aligned}
\sum_{P\in\mathrm{Fam}_2}N_P
&=\lvert S_x^{\prime(s)}\rvert
-\lvert \lbrace P:N_P=1\rbrace \rvert.
\end{aligned}
$$

and the singleton count is at most the total side-pair capacity, singleton-class mass is negligible. This preserves the actual proof logic: realized side-pair capacity is $`x^{o(1)}`$, retained site mass is $`x^{1-o(1)}`$, and therefore singleton mass is negligible.

The statement is asymptotic only. At measured scales the capacity bound is vacuous and singleton classes dominate, so the theorem carries no finite-scale conclusion.

## The class-normalized pair estimate

<!-- sources: frontier-verdict, claim-c3 -->

Define the ordered within-middle pair statistic

$$
\begin{aligned}
Q(x,s)
&=
\sum_{P\in\mathrm{Fam}(S_x^{\prime(s)})}
\frac{1}{N_P}
\sum_{\substack{d\ge2 \cr 2\mid d}}
N_{P,d}\bigl(N_{P,d}-1\bigr)\\
&\le
\varepsilon_{\mathrm{pair}}
\lvert S_x^{\prime(s)}\rvert.
\end{aligned}
$$

The surviving target `B2.pairs` states that for every $`\varepsilon_{\mathrm{pair}}>0`$, there is an $`s`$-independent threshold such that this inequality holds for all later $`x`$ and all $`s`$.

The factor $`1/N_P`$ is load-bearing. An older unnormalized word-pair condition, $`W2=o(\lvert S_x^{\prime(s)}\rvert)`$, is false at the pinned depths because the number of realized full words is only $`x^{o(1)}`$ while the site mass is $`x^{1-o(1)}`$. Cauchy–Schwarz then forces enormous ordered-pair counts. A separate exact class-size configuration shows that an unnormalized relative pair comparison also does not imply `RelExtensionUpper`. Class normalization removes precisely this size skew, while the factor $`N_{P,d}(N_{P,d}-1)`$ makes singleton middle cells inert.

`B2.pairs` remains open. Finite measurements point in a favorable direction for some strata, but they remain well above the required constant and do not establish the asymptotic statement.

## Reduction to `RelExtensionUpper`

<!-- sources: claim-c3, relext-props -->

The square-root reduction is elementary and proved. In a fixed class $`P`$, choose a largest middle cell and write

$$
M_P=\max_d N_{P,d}.
$$

For any adversarial selection $`d_P`$,

$$
\begin{aligned}
(N_{P,d_P}-1)_+
&\le (M_P-1)_+\\
&\le \sqrt{M_P(M_P-1)}\\
&\le \sqrt{\sum_dN_{P,d}(N_{P,d}-1)}.
\end{aligned}
$$

Now apply weighted Cauchy–Schwarz with weights $`N_P`$:

$$
\begin{aligned}
\sum_P\sqrt{\sum_dN_{P,d}(N_{P,d}-1)}
&\le
\sqrt{\left(\sum_PN_P\right)
\left(\sum_P\frac{1}{N_P}\sum_dN_{P,d}(N_{P,d}-1)\right)}.
\end{aligned}
$$

Using $`\sum_PN_P=\lvert S_x^{\prime(s)}\rvert`$ yields

$$
\begin{aligned}
&\text{`B2.pairs' at }\varepsilon_{\mathrm{pair}}
\quad\Longrightarrow\quad
\text{`RelExtensionUpper' at }\\
&\hspace{8em}\varepsilon_{\mathrm{REU}}
=\sqrt{\varepsilon_{\mathrm{pair}}}.
\end{aligned}
$$

Thus the current pigeonhole consumption point

$$
\varepsilon_{\mathrm{REU}}=\frac18
$$

is supplied by

$$
\varepsilon_{\mathrm{pair}}=\frac1{64}.
$$

The logic is exactly: choose the largest middle cell, dominate its excess by the square root of the ordered within-class pair count, apply weighted Cauchy–Schwarz, and accept the square-root loss. The reduction works for unrestricted selections, hence also for any restricted selection form used by the checked consumer.

## The identity-layer barrier

<!-- sources: claim-c4, frontier-verdict -->

The proved barrier is relative to a named tool layer: exact partition identities, side and word capacity bounds, Chebyshev and prime-number-theorem aggregates, Markov-style retention, gap parity, and the pinned parameter arithmetic. There is an explicit deterministic even-gap sequence with prime-like counting growth and smooth gaps of size $`\log{} q_n+O(1)`$ that satisfies these facts.

Its gaps are long monotone step runs. Away from the small set of sites whose windows cross a step boundary, matching prefix and suffix runs squeeze the middle to the same gap value. The non-rigid transitional site mass is only $`O(L\log{} x)=o(\lvert S'_x\rvert)`$. Consequently an argmax middle selection has repeated-middle excess $`(1-o(1))\lvert S'_x\rvert`$, and the normalized statistic $`Q(x,0)`$ has the same maximal order. Both `RelExtensionUpper` and `B2.pairs` fail in this system.

Therefore the named identity-and-capacity layer does not logically imply either target. Any successful proof must add a prime-number input that fails in the smooth system. Middle-slot equidistribution and word-grain mean-value estimates are salient possibilities. The scope is crucial: this is not a theorem that `B2.pairs` is unprovable, not a claim about every conceivable elementary input, and not a general obstruction to an unconditional solution.

## Open analytic routes

<!-- sources: frontier-verdict, final-observations -->

The most direct open route is class-level control of the middle gap at the growing rank $`J+K\asymp\log{}\log{} x`$, uniform enough over realized and arithmetically aligned side pairs to imply `B2.pairs`. Pointwise laws are too strong at small multiplicity because integer granularity dominates, so the natural target is averaged and singleton-inert.

A second route is a word-grain upper mean-value theorem strong enough to control the dispersion or ordered-pair sum without inserting a separate upper-bound sieve constant for every word. Existing per-word and pair-sieve routes in the recorded regime pay super-polylogarithmic rank constants, while the available relative room is only one power of $`\log{} x`$.

A conditional fallback would separate a small exceptional family of strongly aligned classes and prove the middle law on the complement. Such a route owes both a quantitative bound on the aligned mass and a cap-blind definition of the exceptional family. Measurements can test these decompositions and calibrate $`Q(x,s)`$, but an asymptotic proof needs new uniform prime input.

Any proposed estimate must also preserve the uniformity order. The pair target chooses $`\varepsilon_{\mathrm{pair}}`$ first, then one threshold in $`x`$ that works for every $`s`$. A statement proved only for each fixed $`s`$ with an $`s`$-dependent threshold would not match `B2.pairs` as currently consumed. Likewise, replacing $`\mathrm{Fam}`$ by $`\mathrm{Fam}_2`$ inside $`Q`$ would be harmless only after an explicit singleton argument; it should not be done silently even though singleton contributions vanish in the displayed numerator.

The alignment issue is quantitative rather than terminological. Singular-series heuristics predict roughly one inverse power of $`\log{} x`$ of relative room for the middle slot in bulk classes. For residue-aligned classes, the local quotient can grow nearly like a full power of $`\log{} x`$, erasing most of that margin. A proof must therefore average this inflation, show that the aligned mass is sufficiently small, or exploit cancellation unavailable to the present positive counting arguments. Merely bounding the largest local quotient cannot reach the target.

## Verification and limitations

<!-- sources: lean-layout, final-observations, frontier-verdict -->

The conditional implication and deterministic supply integration are machine-checked modulo their named propositions. The matched-flank lower bound, the failure of the old unnormalized condition, the square-root reduction, and the scoped smooth-model barrier are proved at dossier level. `TailIntersection` is proved at that layer. `RelExtensionUpper` and `B2.pairs` remain open.

The finite census is measured evidence only. It records a regime in which singleton mass is still dominant, unlike the far-asymptotic regime of the capacity proof. Heuristic singular-series and middle-law calculations motivate candidate statements but are not used as premises of the proved claims above. No finite computation closes the $`1/64`$ target, and no finite-scale trend is promoted to an asymptotic result.

There are two distinct verification boundaries. The first is logical: checked code establishes implications from named propositions but cannot upgrade an open proposition to a theorem. The second is analytic: the dossier proofs of the cardinality result and barrier use classical asymptotic inputs and explicit model comparisons that have not all been transferred into Lean. Calling the deterministic implication machine-checked is therefore accurate; calling every unconditional analytic statement machine-checked would not be.

Finally, the original problem remains open. The formal theorem is conditional, the unconditional partial result concerns one supplier at a pinned parameter map, and the barrier is confined to its named input layer. These qualifications are part of the mathematical content, not presentational caveats.
