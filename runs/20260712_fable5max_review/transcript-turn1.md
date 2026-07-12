I've reviewed the full document across all sections, and I noticed that line 235 had a line break issue where a mathematical expression got split awkwardly in the display. Now I'm going through the mathematical argument carefully to verify its correctness.
Looking at the setup, the document defines prime gaps gn=pn+1−png_n = p_{n+1} - p_n
gn​=pn+1​−pn​ and introduces a weighted sum SS
S of primes. There's a notation inconsistency where the variable is defined as unu_n
un​ but then used as νn\nu_n
νn​ throughout section 2 — they should be the same thing. The key definition is νn=∑k≥1pn+k/2k\nu_n = \sum_{k \geq 1} p_{n+k}/2^k
νn​=∑k≥1​pn+k​/2k, and from this δn=νn−pn+1\delta_n = \nu_n - p_{n+1}
δn​=νn​−pn+1​ represents the weighted tail sum of primes after position n+1n+1
n+1. I'm working through the algebra to express δn\delta_n
δn​ in terms of the prime gaps. Now I'm verifying the recursion formula by expanding 2δn2\delta_n
2δn​ and showing it equals gn+1+δn+1g_{n+1} + \delta_{n+1}
gn+1​+δn+1​, which confirms that δn+1=2δn−gn+1\delta_{n+1} = 2\delta_n - g_{n+1}
δn+1​=2δn​−gn+1​. Next I'm moving on to analyze the block code Cn,JC_{n,J}
Cn,J​. The sum telescopes to give Cn,J+1C_{n,J+1}
Cn,J+1​, confirming the recurrence. For absolute convergence, I need pn=O(nlog⁡(n+2))p_n = O(n \log(n+2))
pn​=O(nlog(n+2)), which follows from the Prime Number Theorem or Chebyshev's bounds—either way, the series converges without issue.
Now I'm checking the rationality condition: if S=A/(2sb)S = A/(2^s b)
S=A/(2sb) with AA
A an integer, s≥0s \geq 0
s≥0, and bb
b odd, then for n≥sn \geq s
n≥s I can write 2nS2^n S
2nS as the finite sum of weighted primes plus the tail νn\nu_n
νn​, where the tail captures all terms beyond index nn
n.
For the parity argument when n≥max⁡(s+1,2)n \geq \max(s+1, 2)
n≥max(s+1,2): the term $A2^{n-s}$ is even since n−s≥1n - s \geq 1
n−s≥1. In the sum ∑r=1npr2n−r\sum_{r=1}^n p_r 2^{n-r}
∑r=1n​pr​2n−r, only the r=nr = n
r=n term survives modulo 2, giving pnp_n
pn​, which is odd for n≥2n \geq 2
n≥2 (since pn≥3p_n \geq 3
pn​≥3 for n≥2n \geq 2
n≥2, while p1=2p_1 = 2
p1​=2 is even). Since bb
b is odd, bνnb\nu_n
bνn​ must be even. The statement in the ledger specifies this holds for all sufficiently large nn
n, which is made explicit as n≥max⁡(s+1,2)n \ge \max(s+1,2)
n≥max(s+1,2). Since δn\delta_n
δn​ is always positive, bδnb\delta_n
bδn​ is a positive even integer, so bδn≥2b\delta_n \ge 2
bδn​≥2, giving us δn≥2/b\delta_n \ge 2/b
δn​≥2/b — this bound appears implicitly in Section 11. Now moving to the next property: when consecutive digits match over a window of length JJ
J, the corresponding digit blocks are equal.
From equation (2.2), if the gaps match at positions nn
n and mm
m over JJ
J steps, the difference scales by 2J2^J
2J. Since both bδnb\delta_n
bδn​ and bδmb\delta_m
bδm​ are even integers, their difference lies in 2J+1Z2^{J+1}\mathbb{Z}
2J+1Z. Then in (4.3), if the gap difference falls below the threshold 2J+1/b2^{J+1}/b
2J+1/b, the quantized difference must vanish.
Now I'm setting up the FM hypothesis with sequences of pairs (nr,mr)(n_r, m_r)
(nr​,mr​) where the indices diverge after a common prefix of length JrJ_r
Jr​, then fork at different symbols before eventually merging back together. For large rr
r, both inequalities Hr<2Jr/bH_r < 2^{J_r}/b
Hr​<2Jr​/b and Hr<2KrH_r < 2^{K_r}
Hr​<2Kr​ are satisfied by condition 5, since Hr/2Jr→0H_r/2^{J_r} \to 0
Hr​/2Jr​→0 and Hr/2Kr→0H_r/2^{K_r} \to 0
Hr​/2Kr​→0 as r→∞r \to \infty
r→∞, with bb
b being the fixed odd denominator. From the first two tail bounds, I can establish that ∣δnr+Jr−δmr+Jr∣≤2Hr|\delta_{n_r+J_r} - \delta_{m_r+J_r}| \le 2H_r
∣δnr​+Jr​​−δmr​+Jr​​∣≤2Hr​.
Since both values lie in [0,Hr][0, H_r]
[0,Hr​], their difference is at most HrH_r
Hr​, but the bound of 2Hr<2Jr+1/b2H_r < 2^{J_r+1}/b
2Hr​<2Jr​+1/b is still valid and slightly conservative. Combining bounds (4.2) and (4.3) yields the exact equality δnr+Jr=δmr+Jr\delta_{n_r+J_r} = \delta_{m_r+J_r}
δnr​+Jr​​=δmr​+Jr​​. To apply condition C3, I need to verify that the prefix condition matches the indices: gnr+i=gmr+ig_{n_r+i} = g_{m_r+i}
gnr​+i​=gmr​+i​ for the relevant range.
Now applying C3 with parameters n=nrn=n_r
n=nr​, m=mrm=m_r
m=mr​, J=JrJ=J_r
J=Jr​ gives the divisibility condition b(δnr+Jr−δmr+Jr)∈2Jr+1Zb(\delta_{n_r+J_r}-\delta_{m_r+J_r}) \in 2^{J_r+1}\mathbb{Z}
b(δnr​+Jr​​−δmr​+Jr​​)∈2Jr​+1Z, which holds when bδnr,bδmr∈2Zb\delta_{n_r}, b\delta_{m_r} \in 2\mathbb{Z}
bδnr​​,bδmr​​∈2Z — satisfied for sufficiently large nr,mrn_r, m_r
nr​,mr​. Moving to the fork step, I'm computing the difference D1:=δnr+Jr+1−δmr+Jr+1D_1 := \delta_{n_r+J_r+1} - \delta_{m_r+J_r+1}
D1​:=δnr​+Jr​+1​−δmr​+Jr​+1​ as twice the previous difference minus a correction term.
By equation (2.1) applied at indices nr+Jrn_r+J_r
nr​+Jr​ and mr+Jrm_r+J_r
mr​+Jr​, this simplifies to D1=ar′−arD_1 = a'_r - a_r
D1​=ar′​−ar​. On the common suffix where gnr+Jr+1+i=gmr+Jr+1+ig_{n_r+J_r+1+i} = g_{m_r+J_r+1+i}
gnr​+Jr​+1+i​=gmr​+Jr​+1+i​ for 1≤i≤Kr1 \le i \le K_r
1≤i≤Kr​, the recurrence Di+1=2DiD_{i+1} = 2D_i
Di+1​=2Di​ holds, so after KrK_r
Kr​ steps I get DKr+1=2KrD1D_{K_r+1} = 2^{K_r} D_1
DKr​+1​=2Kr​D1​. So equation (5.2) checks out. Since all prime gaps are even for sufficiently large indices, both ara_r
ar​ and ar′a'_r
ar′​ are even and distinct, meaning ∣ar−ar′∣≥2|a_r - a'_r| \ge 2
∣ar​−ar′​∣≥2, which gives us ∣DKr+1∣≥2Kr+1|D_{K_r+1}| \ge 2^{K_r+1}
∣DKr​+1​∣≥2Kr​+1. Now I need to bound this from the other direction using the maximum gap HrH_r
Hr​.
The difference between the two tail values is at most HrH_r
Hr​, and since Hr<2KrH_r < 2^{K_r}
Hr​<2Kr​, we get ∣DKr+1∣≤Hr<2Kr+1|D_{K_r+1}| \le H_r < 2^{K_r+1}
∣DKr​+1​∣≤Hr​<2Kr​+1. This contradicts the lower bound, confirming C4 is correct. The key insight is that this contradiction relied on the even lattice property from the C3 quantization step. so the parity constraint with ∣a−a′∣≥2|a - a'| \ge 2
∣a−a′∣≥2 actually does give them the tighter lower bound of 2Kr+12^{K_r+1}
2Kr​+1 they need to contradict the upper bound 2Hr<2Kr+12H_r < 2^{K_r+1}
2Hr​<2Kr​+1, making the bookkeeping work out. Now checking condition C4: choosing rr
r large enough so all relevant indices fall in the even lattice is fine since we need n≥max⁡(s+1,2)n \ge \max(s+1,2)
n≥max(s+1,2) and the indices nr,mrn_r, m_r
nr​,mr​ go to infinity anyway.
For C5, every rational decomposes as A/(2sb)A/(2^s b)
A/(2sb) with bb
b odd, and since S>0S > 0
S>0 but C4 excludes it, we get that SS
S must be irrational. The subtle point is that the exact equality δnr+Jr=δmr+Jr\delta_{n_r+J_r} = \delta_{m_r+J_r}
δnr​+Jr​​=δmr​+Jr​​ in C4 relies on equation (4.2), which requires bδnrb\delta_{n_r}
bδnr​​ and bδmrb\delta_{m_r}
bδmr​​ to both land in the even lattice—this forces nr,mr≥max⁡(s+1,2)n_r, m_r \ge \max(s+1,2)
nr​,mr​≥max(s+1,2), and since their minimum tends to infinity, this constraint is satisfied.
Now I'm setting up the quantitative framework with specific constants and defining Q1, which bounds the discrepancy between the actual count Nx(d)N_x(d)
Nx​(d) of gap patterns and the model prediction Mx(d)M_x(d)
Mx​(d) across all short even words with bounded span.
I'm questioning whether non-admissible patterns (those where the pattern set covers all residues modulo some prime qq
q) necessarily have Nx(d)=0N_x(d) = 0
Nx​(d)=0—this is probe P4. The key insight is that if a pattern occurs at a prime pnp_n
pn​ in the range, then all shifted positions pn+hip_n + h_i
pn​+hi​ must also be prime, but if the pattern covers all residues mod qq
q, then one of these shifted positions must be divisible by qq
q, forcing it to equal qq
q itself to remain prime.
Since pn+hi≥xp_n + h_i \geq x
pn​+hi​≥x, we'd need q≥xq \geq x
q≥x, yet the covering property requires q≤∣H∣≪xq \leq |\mathcal{H}| \ll x
q≤∣H∣≪x for large xx
x—a contradiction. So for sufficiently large xx
x, non-admissible patterns indeed have Nx(d)=0N_x(d) = 0
Nx​(d)=0 unconditionally, though I need to be more precise about what non-admissibility means in terms of the covering condition. ionally for large xx
x. So the Mx(d)=0M_x(d)=0
Mx​(d)=0 clause in Q1 is unconditionally satisfied and harmless—it doesn't secretly strengthen the statement—and it's essential for the relative-error form to remain consistent (otherwise we'd have a contradiction when Mx=0M_x=0
Mx​=0 but Nx>0N_x>0
Nx​>0, though that can't happen since Nx=0N_x=0
Nx​=0 unconditionally). The clause also ensures no real mass accumulates on words where the model predicts zero, which is needed to guarantee Tx≥(1−ε)∑MxT_x \ge (1-\varepsilon)\sum M_x
Tx​≥(1−ε)∑Mx​.
Now I'm checking where exactly this constraint becomes necessary. Let me trace through the definitions: TxT_x
Tx​ sums the real counts over words of length LxL_x
Lx​ with bounded span, and DxD_x
Dx​ takes the maximum real count per word pair. From Q1, the termwise bounds Nx≤(1+ε)MxN_x \le (1+\varepsilon)M_x
Nx​≤(1+ε)Mx​ and Nx≥(1−ε)MxN_x \ge (1-\varepsilon)M_x
Nx​≥(1−ε)Mx​ hold everywhere, including when Mx=0M_x=0
Mx​=0. This gives me Dx≤(1+ε)D_x \le (1+\varepsilon)
Dx​≤(1+ε) times the corresponding sum over MxM_x
Mx​.
I'm verifying the chain of inequalities: the first step applies the termwise bound to the maximum, the second invokes Q2 about the sum of maxima, and the third uses the lower bound on TxT_x
Tx​ to relate the sum of MxM_x
Mx​ back to TxT_x
Tx​. For large xx
x with ε=(log⁡x)−10\varepsilon = (\log x)^{-10}
ε=(logx)−10 shrinking to zero, the ratio 1+ε1−ε\frac{1+\varepsilon}{1-\varepsilon}
1−ε1+ε​ approaches 1, so the whole expression should satisfy the desired inequality with the η/2\eta/2
η/2 margin.
Now I'm checking whether the specific choice of η=1/20\eta = 1/20
η=1/20 makes the ratio 1+ε1−ε\frac{1+\varepsilon}{1-\varepsilon}
1−ε1+ε​ small enough compared to 1−η/21−η\frac{1-\eta/2}{1-\eta}
1−η1−η/2​, which works out to roughly 1.0263, and since 1+ε1−ε\frac{1+\varepsilon}{1-\varepsilon}
1−ε1+ε​ is approximately 1+2ε1 + 2\varepsilon
1+2ε for small ε\varepsilon
ε, this constraint is satisfied.
Moving to the next part, I'm analyzing the mean tail behavior by decomposing the sum over IxI_x
Ix​ using a dyadic expansion, where IxI_x
Ix​ contains primes in the range [x,2x)[x, 2x)
[x,2x) with cardinality asymptotic to x/log⁡xx/\log x
x/logx by the prime number theorem.
The inner sum telescopes nicely, collapsing to a difference of prime values at the boundaries. Since n1≍x/log⁡xn_1 \asymp x/\log x
n1​≍x/logx corresponds roughly to π(2x)\pi(2x)
π(2x), I need to bound pn1+r+j+1p_{n_1+r+j+1}
pn1​+r+j+1​ using the standard upper bound on primes, which gives something like x+(r+j)log⁡(x+r+j+2)x + (r+j)\log(x+r+j+2)
x+(r+j)log(x+r+j+2) — though I should double-check the exact form of the prime bound. Now I'm verifying the bound from the document matches my calculation, then working through a geometric summation over jj
j where the xx
x term contributes ≪x\ll x
≪x and the logarithmic term simplifies to ≪log⁡x\ll \log x
≪logx after summing. Taking the average gives ≪log⁡x\ll \log x
≪logx, confirming equation (7.1) holds uniformly for r=O(log⁡log⁡x)r = O(\log\log x)
r=O(loglogx).
The parameter rr
r only appears through pn1+r+j+1p_{n_1+r+j+1}
pn1​+r+j+1​ and gets absorbed into the bound. The claim about uniformity in rr
r is valid—the estimate actually holds uniformly for r≪x/log⁡xr \ll x/\log x
r≪x/logx or larger. I'm also confirming that δn+r\delta_{n+r}
δn+r​ equals the weighted sum ∑j≥1gn+r+j2−j\sum_{j\ge1} g_{n+r+j} 2^{-j}
∑j≥1​gn+r+j​2−j by definition, and swapping the order of summation over the finite nn
n-sum and infinite jj
j-sum is justified since all terms are positive (Tonelli's theorem applies).
Now moving to section C7 to show the four tail-bad sets are negligible, with Hx=(log⁡x)4H_x = (\log x)^4
Hx​=(logx)4.
For each offset r∈{Jx,Jx+Kx+1}r \in \{J_x, J_x+K_x+1\}
r∈{Jx​,Jx​+Kx​+1}, I'm applying Markov's inequality from equation (7.1) to bound the number of indices n∈Ixn \in I_x
n∈Ix​ where δn+r\delta_{n+r}
δn+r​ exceeds HxH_x
Hx​, which gives roughly ∣Ix∣(log⁡x)−3|I_x|(\log x)^{-3}
∣Ix​∣(logx)−3. A start index nn
n is classified as "tail-bad" if either δn+Jx>Hx\delta_{n+J_x} > H_x
δn+Jx​​>Hx​ or δn+Jx+Kx+1>Hx\delta_{n+J_x+K_x+1} > H_x
δn+Jx​+Kx​+1​>Hx​, and the union bound over these two offsets shows the total share of tail-bad indices is O(∣Ix∣(log⁡x)−3)O(|I_x|(\log x)^{-3})
O(∣Ix​∣(logx)−3).
When I find two good start sites nn
n and mm
m, each one independently satisfies both tail bounds for both offsets, so together they provide all four tail bounds required by the FM condition. This confirms that "good site" is defined per-site with respect to both offsets, and two such sites deliver exactly what's needed. For C8, the span of consecutive elements equals the difference of prefix sums, which telescopes nicely. When I sum over all starting positions in IxI_x
Ix​, each inner sum over the indices contributes at most O(x)O(x)
O(x), so the span-bad blocks contribute negligibly overall. log x)^3$ is satisfied, so Q1 applies to each word individually. The Markov bound shows that the proportion of words exceeding the span threshold is o(1)o(1)
o(1), which is what we need. Now I'm verifying that the transition from HL_quant to FM works: the bound Dx≤(1−η/2)TxD_x \le (1-\eta/2)T_x
Dx​≤(1−η/2)Tx​ holds because we're restricting to words with controlled span, and this restriction doesn't affect the asymptotic count since the exceptional words form a negligible fraction. is crucial—C7 and C8 show that bad start indices are a vanishing fraction of ∣Ix∣|I_x|
∣Ix​∣, but to conclude they're o(Tx)o(T_x)
o(Tx​) I need TxT_x
Tx​ to be comparable to ∣Ix∣|I_x|
∣Ix​∣, which is exactly what probe P2 establishes. Since each n∈Ixn \in I_x
n∈Ix​ generates one word of length LxL_x
Lx​, and that word gets counted in TxT_x
Tx​ precisely when its span doesn't exceed (log⁡x)3(\log x)^3
(logx)3, I'm tracking how many starting positions actually contribute to the sum.
By C8, almost all positions in IxI_x
Ix​ yield words with acceptable span, so Tx=(1−o(1))∣Ix∣T_x = (1-o(1))|I_x|
Tx​=(1−o(1))∣Ix​∣. The document mentions in Section 8.2 that tail-bad and span-bad sites are o(Tx)o(T_x)
o(Tx​), but it doesn't explicitly state this relationship between TxT_x
Tx​ and ∣Ix∣|I_x|
∣Ix​∣—it's left implicit, which might be a small gap in the exposition. So TxT_x
Tx​ counts exactly those start indices with span at most (log⁡x)3(\log x)^3
(logx)3, giving (1−O(log⁡log⁡x/(log⁡x)2))∣Ix∣(1-O(\log\log x/(\log x)^2))|I_x|
(1−O(loglogx/(logx)2))∣Ix​∣ indices, which is positive and grows like x/log⁡xx/\log x
x/logx. Within this TxT_x
Tx​ population, the span-bad indices are already filtered out, but I need to bound how many tail-bad ones remain.
The tail-bad count within TxT_x
Tx​ is at most O(Tx(log⁡x)−3)=o(Tx)O(T_x(\log x)^{-3}) = o(T_x)
O(Tx​(logx)−3)=o(Tx​), staying below (η/4)Tx(\eta/4)T_x
(η/4)Tx​ for large xx
x. So the "good" start sites—those with both span and tail conditions satisfied—number at least (1−η/4)Tx(1-\eta/4)T_x
(1−η/4)Tx​.
Now applying pigeonhole: among these good sites, I'm assuming each context pair (W,V)(W,V)
(W,V) has at most one associated fork value aa
a. So I've reached a contradiction: the number of good sites must be both at most DxD_x
Dx​ and strictly greater than DxD_x
Dx​ for large xx
x. This means my assumption was wrong—there can't be at most one fork value per context among good sites. Therefore, some context (W,V)(W,V)
(W,V) must have at least two good sites with different fork values, giving me the two sites nxn_x
nx​ and mxm_x
mx​ I need: same prefix word WW
W, same suffix word VV
V, but different fork gaps.
Now I'm checking the constraints: both sites have all four tails bounded by HxH_x
Hx​, they're distinct sites with nx<mxn_x < m_x
nx​<mx​, and the fork matching condition is satisfied. Then I'm computing the size relations—with Jx=Kx=⌈8log⁡log⁡x⌉J_x = K_x = \lceil 8\log\log x\rceil
Jx​=Kx​=⌈8loglogx⌉, I get 2Jx2^{J_x}
2Jx​ growing like (log⁡x)8log⁡2≈(log⁡x)5.545(\log x)^{8\log 2} \approx (\log x)^{5.545}
(logx)8log2≈(logx)5.545, which dominates Hx=(log⁡x)4H_x = (\log x)^4
Hx​=(logx)4, so their ratio vanishes as x→∞x \to \infty
x→∞.
For the Folkman-Maillet construction, I need sequences indexed by rr
r where min⁡(nx,mx)→∞\min(n_x, m_x) \to \infty
min(nx​,mx​)→∞ as x→∞x \to \infty
x→∞ (guaranteed since pnx≥xp_{n_x} \ge x
pnx​​≥x), and the fork gap condition requires that the symbols at position Jr+1J_r + 1
Jr​+1 differ between the two sites: gnr+Jr+1≠gmr+Jr+1g_{n_r+J_r+1} \ne g_{m_r+J_r+1}
gnr​+Jr​+1​=gmr​+Jr​+1​, with the word structure being (W,a,V)(W, a, V)
(W,a,V) where ∣W∣=Jx|W| = J_x
∣W∣=Jx​.
The gap positions align perfectly with the FM conditions: prefix gaps cover positions 11
1 through JxJ_x
Jx​, the fork gap is at position Jx+1J_x+1
Jx​+1, and suffix gaps span positions Jx+2J_x+2
Jx​+2 through LxL_x
Lx​. Condition 3 requires the suffix gaps to match between the two occurrences at offsets Jr+1+iJ_r+1+i
Jr​+1+i for i=1i = 1
i=1 to KrK_r
Kr​, which corresponds to word positions Jx+2J_x+2
Jx​+2 through LxL_x
Lx​, and this all checks out.
For condition 5, the exponential decay conditions Hx/2Jx→0H_x/2^{J_x} \to 0
Hx​/2Jx​→0 and Hx/2Kx→0H_x/2^{K_x} \to 0
Hx​/2Kx​→0 both hold as required. The HL_quant to FM implication is sound—the key step that Tx=(1−o(1))∣Ix∣T_x = (1-o(1))|I_x|
Tx​=(1−o(1))∣Ix​∣ is straightforward, and the bad count bound of ≪Tx(log⁡x)−3\ll T_x (\log x)^{-3}
≪Tx​(logx)−3 ensures it stays below the (η/4)Tx(\eta/4)T_x
(η/4)Tx​ threshold needed for the removal step.
For the good sites count in section 8.3, I'm verifying that the bound of at least (1−η/4)Tx(1-\eta/4)T_x
(1−η/4)Tx​ holds: starting with TxT_x
Tx​ and subtracting the tail-bad sites of size O(∣Ix∣(log⁡x)−3)O(|I_x|(\log x)^{-3})
O(∣Ix​∣(logx)−3), combined with Tx=(1−o(1))∣Ix∣T_x = (1-o(1))|I_x|
Tx​=(1−o(1))∣Ix​∣, this gives the required lower bound eventually. That checks out.
Now I need to examine whether HL_quant itself is reasonable and avoids circularity—specifically whether any clause implicitly assumes the irrationality conclusion or something equivalent, and how the probe questions and Phase A's hypothesis design fit into this.
Looking at the three questions: Q1 is a strong quantitative equidistribution statement about primes themselves; Q2 concerns only the model MxM_x
Mx​—the singular series and explicit formula (6.1)—not primes directly; Q3 is just arithmetic of constants. So the irrationality conclusion isn't directly baked in. The key question is whether Q2, being "about the model only," is actually checkable and provable unconditionally. Q2 is a concrete, unconditional statement about singular series sums—if it's true, it's a theorem waiting for proof; if false, HL_quant becomes vacuous and the conditional is trivially satisfied but useless. The document honestly notes in Section 14 that proving Q2 remains open.
Now I'm wondering whether Q1's relative-error form with exponent Aerr=10A_{err}=10
Aerr​=10, uniform over words up to length 20log⁡log⁡x20\log\log x
20loglogx with span up to (log⁡x)3(\log x)^3
(logx)3, is genuinely Hardy–Littlewood-type or actually much stronger. The standard HL conjecture for fixed admissible H\mathcal{H}
H gives an asymptotic with the singular series and logarithmic integral, but uniform quantitative versions with power-saving errors are substantially stronger, and the consecutive version with the Poisson exponential factor pushes even further.
The real concern is whether model (6.1) can even conjecturally achieve relative error (log⁡x)−10(\log x)^{-10}
(logx)−10. The exponential factor exp⁡(−span/log⁡t)\exp(-\mathrm{span}/\log t)
exp(−span/logt) is just a heuristic Poisson approximation for excluding primes in the gaps between prescribed primes, but the true consecutive count should come from inclusion–exclusion over HL for all supersets, which is a more intricate alternating sum.
When evaluated via Gallagher-type singular series, this only gives Poisson behavior in the limit and on average. The actual probability that no prime falls in the gaps isn't exactly exp⁡(−span/log⁡t)\exp(-\mathrm{span}/\log t)
exp(−span/logt) — there are lower-order corrections of relative size O(span/(log⁡t)2⋅log⁡(…))O(\mathrm{span}/(\log t)^2 \cdot \log(\ldots))
O(span/(logt)2⋅log(…)) and singular-series fluctuations around O(1/log⁡t)O(1/\log t)
O(1/logt). Montgomery–Soundararajan's work on moments of primes in short intervals confirms these corrections to Poisson are significant, with variance showing corrections involving logarithmic factors.
For intervals of length hh
h, the variance goes as hlog⁡(x/h)h\log(x/h)
hlog(x/h) rather than hlog⁡xh\log x
hlogx — meaning relative corrections of order log⁡h/log⁡x∼log⁡log⁡x/log⁡x\log h/\log x \sim \log\log x/\log x
logh/logx∼loglogx/logx for h≈poly-log⁡h \approx \mathrm{poly}\text{-}\log
h≈poly-log, which is vastly larger than (log⁡x)−10(\log x)^{-10}
(logx)−10.
But here's the issue: the span can reach (log⁡x)3(\log x)^3
(logx)3, so λ=span/log⁡t\lambda = \mathrm{span}/\log t
λ=span/logt can be as large as (log⁡x)2(\log x)^2
(logx)2. The exponential factor e−λe^{-\lambda}
e−λ with λ≈(log⁡x)2\lambda \approx (\log x)^2
λ≈(logx)2 becomes astronomically small — essentially x−log⁡xx^{-\log x}
x−logx — and a relative error of (log⁡x)−10(\log x)^{-10}
(logx)−10 on such a tiny quantity becomes absurdly large.
Looking at the numbers: there are roughly x/log⁡xx/\log x
x/logx available start sites, and the model count for a single word of span ≈(log⁡x)3\approx (\log x)^3
≈(logx)3 is super-polynomially small, far less than 1. This means Q1 with relative error forces Nx(d)=0N_x(d) = 0
Nx​(d)=0 whenever the model mass falls below a threshold, effectively forbidding any occurrence of words whose expected count is negligible. 1}$ with L≈16log⁡log⁡xL \approx 16\log\log x
L≈16loglogx, which gives e16(log⁡log⁡x)2e^{16(\log\log x)^2}
e16(loglogx)2 — sub-polynomial in xx
x. The total count of words with bounded span grows like exp⁡(O((log⁡log⁡x)2))\exp(O((\log\log x)^2))
exp(O((loglogx)2)), matching what Section 9 predicts, and spreading x/log⁡xx/\log x
x/logx sites across this many words means a typical word still captures a huge number of sites even after accounting for the exponential decay.
But the equidistribution requirement is much stricter when applied to atypical words — those with span near (log⁡x)3(\log x)^3
(logx)3 where the model mass drops to e−(log⁡x)2xe^{-(\log x)^2}x
e−(logx)2x, essentially zero. For these, the quantitative hypothesis forces no gap words to appear at all.
Now I'm wondering whether such extreme words actually occur in practice. A word spanning (log⁡x)3(\log x)^3
(logx)3 within a window of size ≈16log⁡log⁡x\approx 16\log\log x
≈16loglogx would require average gaps of (log⁡x)3/log⁡log⁡x(\log x)^3/\log\log x
(logx)3/loglogx — that's a massive prime gap, far larger than what Cramér's conjecture allows. The conjecture predicts max gaps of O((log⁡x)2)O((\log x)^2)
O((logx)2), which would rule out such words entirely. But unconditionally, we only know gaps are ≪x0.525\ll x^{0.525}
≪x0.525, so gaps of size (log⁡x)2(\log x)^2
(logx)2 remain unresolved.
The known lower bounds from Ford–Green–Konyagin–Maynard–Tao show gaps of size ≫log⁡xlog⁡log⁡xlog⁡log⁡log⁡log⁡xlog⁡log⁡log⁡x\gg \log x \frac{\log\log x \log\log\log\log x}{\log\log\log x}
≫logxlogloglogxloglogxloglogloglogx​ definitely exist — slightly above log⁡x\log x
logx but nowhere near (log⁡x)2(\log x)^2
(logx)2. So Q1's requirement that Nx(d)=0N_x(d) = 0
Nx​(d)=0 for these huge-span words is really a Cramér-type statement in disguise, implying no prime gaps of size ≥(log⁡x)3−O(stuff)\ge (\log x)^3 - O(\text{stuff})
≥(logx)3−O(stuff) can exist. But I need to be more careful about whether Q1 is actually constraining individual gaps or something else.
For a single gap d1≤(log⁡x)3d_1 \le (\log x)^3
d1​≤(logx)3, the heuristic model predicts Mx((d1))≈xe−(log⁡x)2(…)⋘1M_x((d_1)) \approx x e^{-(\log x)^2}(\ldots) \lll 1
Mx​((d1​))≈xe−(logx)2(…)⋘1, which is tiny. So Q1 forces Nx((d1))=0N_x((d_1)) = 0
Nx​((d1​))=0 — meaning no gap of exactly that size appears in [x,2x)[x,2x)
[x,2x). This holds uniformly across all d1d_1
d1​ where the model predicts fewer than half an occurrence. So Q1 actually encodes something much stronger than Hardy–Littlewood: it's essentially giving us Cramér's conjecture with a constant around 1, which means bounding prime gaps by roughly (log⁡x)2(\log x)^2
(logx)2 across the entire range [x,2x)[x, 2x)
[x,2x). Let me verify this threshold calculation though—the model mass Mx(d1)M_x(d_1)
Mx​(d1​) scales as S⋅x(log⁡x)−2e−d1/log⁡x\mathfrak{S} \cdot x(\log x)^{-2}e^{-d_1/\log x}
S⋅x(logx)−2e−d1​/logx, and I need to check where the singular series S({0,d1})\mathfrak{S}(\{0, d_1\})
S({0,d1​}) factors in for divisors of d1d_1
d1​. with gaps larger than (log⁡x)3(\log x)^3
(logx)3 since the span filter cuts off at that threshold, so Q1 only constrains gaps in the range [(1+ϵ′)(log⁡x)2,(log⁡x)3][(1+\epsilon')(\log x)^2, (\log x)^3]
[(1+ϵ′)(logx)2,(logx)3] where the model predicts less than half the mass. So Q1 is really saying "HL-Poisson with relative error (log⁡x)−10(\log x)^{-10}
(logx)−10 up to span (log⁡x)3(\log x)^3
(logx)3", which forbids gaps in the range [C(log⁡x)2,(log⁡x)3][C(\log x)^2, (\log x)^3]
[C(logx)2,(logx)3] but permits arbitrarily large gaps beyond that threshold. It's a quirk of the hypothesis, but it's what we're working with. The key insight is that Q1 is substantially stronger than standard Hardy–Littlewood asymptotics: it pins down consecutive/Poisson structure, enforces Cramér-like bounds on gaps up to (log⁡x)3(\log x)^3
(logx)3, and delivers remarkably tight relative error even for rare patterns with model mass e−(log⁡x)2e^{-(\log x)^2}
e−(logx)2—essentially sharp zero-one laws in the tail.
Now, is this a gap in the document itself? The paper does acknowledge in section 6.2 that the model is a hypothesis, not a theorem, and sections 1 and 14 identify the missing piece as deriving Q2 and consecutive-uniformity from more standard uniform HL. But the document's framing—especially the title "Das exakt verwendete Paket HL_quant" and the language about "quantitative HL"—suggests it's positioning Q1 as a quantitative Hardy–Littlewood result, not just a conjecture floating in isolation.
The referee's point cuts deeper: Q1 is already materially stronger than uniform HL in several respects—the consecutive-with-Poisson-factor model, relative error behavior in sparse regimes, Cramér-like consequences. The document partially owns this ("Der Exponentialfaktor modelliert... Dies ist eine Hypothesenformulierung"), citing Gallagher and Kuperberg on the fixed-dimension versus log log x window problem. Section 14 then identifies what's actually missing: the transition from uniform counts of non-necessarily-consecutive prime k-tuples to consecutive ones.
So the framing is honest that Q1 exceeds standard HL, but I should flag that "HL_quant" is a misleading label—the hypothesis package is materially stronger than any standard uniform HL, and the relative-error form across all words (including deep-tail spans) smuggles in Cramér-strength gap bounds. That's not fatal since the document claims a conditional proof, and a conditional proof from a strong hypothesis remains valid, but the framing question in the payload needs scrutiny.
The hypothesis is materially stronger than Hardy-Littlewood-type, not equivalent. Now I'm checking for circularity: does Q1+Q2 covertly assume irrationality or something equivalent? The conclusion via fork-merge needs small-tail configurations, Q2 is model-only, Q1 transfers. The real question is whether Q2 could be false for the model, making the implication vacuous. I need to probe whether the model-entropy clause about averaged fork anti-concentration is a statement about the explicit local model only and whether it's plausibly provable for the standard singular-series model.
Q2 is purely about the explicit model—singular series, logarithmic bounds, exponential factors—and is unconditional in principle, provable or disprovable through singular series analysis. For the model, conditioned on the word pair, the fork gap has a conditional distribution proportional to the singular series times an exponential decay factor.
In a Poisson-like regime, the conditional distribution of the scaled gap would be roughly exponential, so any single even value carries mass around 2/log⁡t2/\log t
2/logt, which vanishes as tt
t grows. This means Q2 with η=1/20\eta = 1/20
η=1/20 should hold with vast room to spare—the maximum should be O(1/log⁡x)O(1/\log x)
O(1/logx) rather than 1−η1-\eta
1−η. However, the singular series is highly irregular: it varies sharply with the residue structure of the configuration. or covers all residues mod small primes, which would eliminate most fork values aa
a. The key insight is that while certain contexts could theoretically force non-admissibility for many choices of aa
a, the actual constraints from avoiding full residue coverage mod small primes leave enough room that most aa
a remain viable in practice. the model's structure suggests the fork gap follows roughly an exponential distribution scaled by log⁡t\log t
logt with bounded singular-series corrections, so no single residue class can concentrate most of the mass even accounting for small prime boosts. The averaged nature of Q2 means pathological contexts with negligible total mass can't skew the overall picture, which supports plausibility, though there are counterarguments to weigh. The singular series bounds for kk
k-tuples grow exponentially with kk
k, potentially reaching ecklog⁡log⁡ke^{ck\log\log k}
eckloglogk in the densest cases, though the exact growth isn't critical here. The key takeaway is that Q2 remains genuinely open even in the simplified model, as the document acknowledges in Section 14, and the choice of η=1/20\eta = 1/20
η=1/20 is deliberately conservative since heuristics suggest the true deterministic mass fraction should vanish.
Regarding circularity: Q1 and Q2 together establish FM through the conditional argument, which is the whole point—but there's no hidden circularity because Q2 concerns the mass distribution across fork values in the model, while the tail behavior (δ\delta
δ's) is handled separately and unconditionally through the structural conditions, so no clause smuggles in FM itself.
The fork existence emerges from combining counting arguments with pigeonhole reasoning. Though I should note Q1 has a subtle consequence: whenever Mx(d)<1M_x(d) < 1
Mx​(d)<1, it forces Nx(d)=0N_x(d) = 0
Nx​(d)=0, which means for words where Mx(d)≥2M_x(d) \geq 2
Mx​(d)≥2, Q1 actually guarantees Nx(d)≥1N_x(d) \geq 1
Nx​(d)≥1—enforcing uniform existence of every typical word, an extraordinarily strong constraint.
This uniform existence of all typical words nearly delivers FM on its own without needing Q2. If I pick any context with two distinct fork values both having decent model mass, Q1 immediately gives me occurrences at both, creating a fork-merge pair. But the catch is I also need those four tails to be small at those specific occurrences, and tail control only works on averages, not pointwise.
So the specific occurrences Q1 produces might all be tail-bad. That's precisely why Q2 is essential—it uses entropy and counting to eliminate an exceptional set that's o(1)o(1)
o(1) per word but not summable overall. The document's Section 9 explains this correctly in German: uniform existence of each word doesn't guarantee that the tail-good occurrences collapse to exactly one fork value in every context.
Now I'm wondering whether Q2 is actually necessary given Q1, or if I could instead apply Q1 to longer words to control the tails directly, since those tail terms depend on all subsequent gaps but are dominated by the first log⁡2H\log_2 H
log2​H or so gaps. The bound on small tails follows from the span of the next few gaps plus an exponentially decaying remainder. But really, the question isn't about optimizing—it's whether their proof holds up, and it does, assuming that implicit P2 step is valid.
Actually, wait—I'm spotting a potential real gap in Section 8.3 with the "gute Startstellen" pigeonhole argument. They claim existence of two good starting positions with the same (W,V)(W,V)
(W,V) but different aa
a, but the pigeonhole principle requires...
The count of good sites with a given context (W,V)(W,V)
(W,V) is bounded by Nx(W,a∗,V)N_x(W, a^*, V)
Nx​(W,a∗,V) where a∗a^*
a∗ is the unique fork value, and those good sites form a subset of all sites with the full word (W,a∗,V)(W,a^*,V)
(W,a∗,V). That checks out. The contexts themselves range over span-bounded full words (W,a,V)(W,a,V)
(W,a,V), and any good site has a full word within the span bound since it belongs to the TxT_x
Tx​ population. So that's solid too.
Now I'm verifying the conditions for M with the specific parameters Jx,Kx,HxJ_x, K_x, H_x
Jx​,Kx​,Hx​ as x→∞x \to \infty
x→∞. The FM requirement that min⁡(nr,mr)→∞\min(n_r, m_r) \to \infty
min(nr​,mr​)→∞ holds, and both Jr,Kr≥1J_r, K_r \ge 1
Jr​,Kr​≥1 are satisfied. For the Q3 arithmetic check, I'm confirming that with Jx=Kx=⌈8log⁡log⁡x⌉J_x = K_x = \lceil 8\log\log x \rceil
Jx​=Kx​=⌈8loglogx⌉ and Lx=Jx+Kx+1L_x = J_x + K_x + 1
Lx​=Jx​+Kx​+1, the bound Lx≤20log⁡log⁡xL_x \le 20\log\log x
Lx​≤20loglogx is satisfied for sufficiently large xx
x — specifically when x≥ee0.75x \ge e^{e^{0.75}}
x≥ee0.75, which is roughly 8.3.
For the "Blockkonstante 8" condition, I'm verifying that 2Jx2^{J_x}
2Jx​ and 2Kx2^{K_x}
2Kx​ exceed (log⁡x)4(\log x)^4
(logx)4 by computing 28ln⁡ln⁡x=(ln⁡x)8ln⁡2≈(log⁡x)5.5452^{8\ln\ln x} = (\ln x)^{8\ln 2} \approx (\log x)^{5.545}
28lnlnx=(lnx)8ln2≈(logx)5.545, which indeed dominates the required power.
Now I'm checking the epsilon bookkeeping: the bound N≤(1+ε)MN \le (1+\varepsilon)M
N≤(1+ε)M follows from the error condition with εx=(log⁡x)−10\varepsilon_x = (\log x)^{-10}
εx​=(logx)−10, and I'm verifying that Tx≥(1−ε)∑MT_x \ge (1-\varepsilon)\sum M
Tx​≥(1−ε)∑M holds termwise, with DxD_x
Dx​ bounded above by... Now I'm solving for the constraint on ε\varepsilon
ε by setting up the inequality and working through the algebra to find that ε≤0.01298\varepsilon \le 0.01298
ε≤0.01298. With the specific choice of ε=(log⁡x)−10\varepsilon = (\log x)^{-10}
ε=(logx)−10, this translates to a requirement on xx
x that's easily satisfied for large values. The bad share bound in section 8.2 comes from a decay rate of O((log⁡x)−3)O((\log x)^{-3})
O((logx)−3).
For the good sites versus DxD_x
Dx​ comparison, I'm checking that the lower bound on good sites exceeds the upper bound on DxD_x
Dx​, which requires (1−η/4)>(1−η/2)(1-\eta/4) > (1-\eta/2)
(1−η/4)>(1−η/2)—this holds strictly since η>0\eta > 0
η>0. There's also a technical detail to verify: the good sites must actually lie within IxI_x
Ix​, and the FM configuration requires two distinct site indices nxn_x
nx​ and mxm_x
mx​ rather than the same index repeated.
Now I'm examining whether the two window occurrences in the FM configuration can overlap or even coincide. The contradiction argument in C4 only depends on the stated gap equalities and lattice membership conditions, not on whether the indices are distinct or the windows overlap—so the algebra works regardless. The strict ordering nr<mrn_r < m_r
nr​<mr​ comes from the fact that the sites themselves are different (since a≠a′a \ne a'
a=a′), and we just order them accordingly.
I'm also double-checking the four tails condition in FM: the tail bounds like δnr+Jr\delta_{n_r+J_r}
δnr​+Jr​​ are automatically positive, and they're bounded by Hr=(log⁡x)4H_r = (\log x)^4
Hr​=(logx)4 from the good-site definition, which feeds into condition C7.
For FM's condition 5 on convergence along the sequence rr
r: here the sequence is indexed by x→∞x \to \infty
x→∞, and since we produce a configuration for all sufficiently large xx
x, we have infinitely many configurations available. I can formally index the rr
r-th configuration at xr=rx_r = r
xr​=r to make this precise.
Now I need to carefully verify C6's telescoping bound, which is where the real analytic work happens—specifically the sum ∑n∈Ixgn+r+j\sum_{n \in I_x} g_{n+r+j}
∑n∈Ix​​gn+r+j​ over consecutive values of nn
n from n0n_0
n0​ to n1n_1
n1​.
The telescoping sum collapses to pn1+r+j+1−pn0+r+jp_{n_1+r+j+1} - p_{n_0+r+j}
pn1​+r+j+1​−pn0​+r+j​, which is at most pn1+r+j+1p_{n_1+r+j+1}
pn1​+r+j+1​. With n1≈π(2x)−1≪x/log⁡xn_1 \approx \pi(2x) - 1 \ll x/\log x
n1​≈π(2x)−1≪x/logx, I can bound the prime using pm≪mlog⁡mp_m \ll m \log m
pm​≪mlogm where m=n1+r+j+1m = n_1 + r + j + 1
m=n1​+r+j+1. If j≤xj \le x
j≤x, then m≪x/log⁡x+xm \ll x/\log x + x
m≪x/logx+x, but I need to be more careful about how these terms combine.
Let me refine this by bounding pm≪(x/log⁡x+j)log⁡(x+j)p_m \ll (x/\log x + j) \log(x+j)
pm​≪(x/logx+j)log(x+j), which gives ≪xlog⁡(x+j)log⁡x+jlog⁡(x+j)\ll x\frac{\log(x+j)}{\log x} + j\log(x+j)
≪xlogxlog(x+j)​+jlog(x+j). For j≤xj \le x
j≤x, the logarithm ratio is at most log⁡(2x)/log⁡x≪1\log(2x)/\log x \ll 1
log(2x)/logx≪1, so this becomes ≪x+jlog⁡x\ll x + j\log x
≪x+jlogx. For j>xj > x
j>x, the term x/log⁡xx/\log x
x/logx is dominated by jj
j, so pm≪jlog⁡jp_m \ll j\log j
pm​≪jlogj. Either way, the bound ≪x+jlog⁡(x+j+2)\ll x + j\log(x+j+2)
≪x+jlog(x+j+2) holds, and now I need to sum this weighted by 2−j2^{-j}
2−j over all j≥1j \ge 1
j≥1.
The first part sums to ≪x\ll x
≪x. For the second part, I'll use the fact that log⁡(x+j+2)≤log⁡x+log⁡(j+3)\log(x+j+2) \le \log x + \log(j+3)
log(x+j+2)≤logx+log(j+3) when x≥1x \ge 1
x≥1, which lets me split the sum into two pieces: one weighted by log⁡x\log x
logx and one by log⁡(j+3)\log(j+3)
log(j+3). The weighted sum of j⋅2−jj \cdot 2^{-j}
j⋅2−j equals 2, so the total contribution is ≪log⁡x\ll \log x
≪logx, which is absorbed into the xx
x bound. Everything checks out to ≪x\ll x
≪x.
Now for C8, I'm bounding the span sum over IxI_x
Ix​ by splitting it into contributions from each position ii
i up to LL
L. Using the prime bound pn1+i+1≪xp_{n_1+i+1} \ll x
pn1​+i+1​≪x (which holds since n1+i+1≪x/log⁡xn_1 + i + 1 \ll x/\log x
n1​+i+1≪x/logx), the sum is ≪L⋅x\ll L \cdot x
≪L⋅x. Applying Markov's inequality with threshold (log⁡x)3(\log x)^3
(logx)3 gives a count of O(Lx)/(log⁡x)3O(Lx)/(\log x)^3
O(Lx)/(logx)3, and after dividing by ∣Ix∣|I_x|
∣Ix​∣, this becomes O(Llog⁡x/(log⁡x)3)O(L\log x/(\log x)^3)
O(Llogx/(logx)3) per element.
The ledger C7 confirms that each of the two offset tails contributes O((log⁡x)−3)O((\log x)^{-3})
O((logx)−3) to the share, which checks out. There's a minor notational quirk in the ledger—it mentions "one of four needed tails" when really there are two tails per site and four total across both sites—but the counting argument per index is sound.
For the FM statement, I need to verify the four small tails: the maximum is bounded by HrH_r
Hr​, with tails appearing at the four positions nr+Jrn_r+J_r
nr​+Jr​, mr+Jrm_r+J_r
mr​+Jr​, nr+Jr+Kr+1n_r+J_r+K_r+1
nr​+Jr​+Kr​+1, and mr+Jr+Kr+1m_r+J_r+K_r+1
mr​+Jr​+Kr​+1. Checking against C4... Now I'm verifying that the fork-merge argument avoids needing an explicit "tail differs from an integer" clause, unlike approaches like equal-run squeeze that require ruling out exact locking scenarios. The key is that this construction doesn't rely on δ\delta
δ being trapped near a rational value, so the immunity to that countermodel is built into the proof structure itself. proof actually permits exact equality at the merge point — that's the branch it follows. The key immunity comes from the fork condition a≠a′a \ne a'
a=a′, which is structural rather than a Diophantine assumption, and the FM conditions don't require any non-integer clauses. Now I'm checking the math in Section 11 for the alternative route, starting with how bδn+Jb\delta_{n+J}
bδn+J​ relates to powers of 2. So δ>0\delta > 0
δ>0 always as a positive integer, and the 2-adic valuation of the difference is at least min⁡(J+1,v2(C))\min(J+1, v_2(C))
min(J+1,v2​(C)), which they conservatively state as min⁡(J,v2(C))\min(J, v_2(C))
min(J,v2​(C)). This means bδn+Jb\delta_{n+J}
bδn+J​ is bounded below by 2min⁡{J,v2(Cn,J)}2^{\min\{J, v_2(C_{n,J})\}}
2min{J,v2​(Cn,J​)}. If along the sequence this exponent grows much faster than log⁡2δn+J\log_2\delta_{n+J}
log2​δn+J​, then bb
b would have to grow without bound, contradicting that bb
b is fixed.
The V2 route checks out as a conditional statement, and the ledger confirms it's proved. Now moving into Section 12 on word powers: I'm defining a word ww
w as a sequence of digits, computing its binary weight BwB_w
Bw​ and the reduced fraction αw=mw/qw\alpha_w = m_w/q_w
αw​=mw​/qw​. The claim is about periodic gap patterns where a word repeats KK
K times starting at position nn
n.
When gaps follow this periodic pattern, an affine iteration relation holds: the deviation from the fixed point αw\alpha_w
αw​ gets scaled by 2−Kr2^{-Kr}
2−Kr after KrKr
Kr steps. Verifying this: one period of the word gives δn+r=2rδn−Bw\delta_{n+r} = 2^r\delta_n - B_w
δn+r​=2rδn​−Bw​, and the fixed point satisfies α=Bw/(2r−1)\alpha = B_w/(2^r-1)
α=Bw​/(2r−1), which checks out. Iterating KK
K times compounds this scaling...
Now I'm working through the rationality constraint: if bδnb\delta_n
bδn​ lies in the integer lattice and qw∤bq_w \nmid b
qw​∤b, then δn\delta_n
δn​ can't get closer to αw\alpha_w
αw​ than 1/(bqw)1/(bq_w)
1/(bqw​). The key is that the difference δn−αw\delta_n - \alpha_w
δn​−αw​ becomes a fraction with integer numerator and denominator bqwbq_w
bqw​, so any nonzero gap has a minimum size.
From the scaling relation, this distance gets amplified by 2Kr2^{Kr}
2Kr at the next step, giving ∣δn+Kr−αw∣≥2Kr/(bqw)|\delta_{n+Kr}-\alpha_w| \ge 2^{Kr}/(bq_w)
∣δn+Kr​−αw​∣≥2Kr/(bqw​). The irrationality argument then follows: if we have a sequence of word powers where the denominators grow unbounded and the scaled error shrinks toward zero, the inequality forces a contradiction—the error can't simultaneously stay bounded below by 1/b1/b
1/b and approach zero. The ledger confirms WP as a valid implication. Now I'm looking at FS1's claim in Section 9 about whether a pointwise HL asymptotic alone, without summable family-uniformity or fork anti-concentration, can rule out fork behavior.
The argument hinges on two points: errors can't be summed across exponentially many words, and uniform existence doesn't control what happens on the tail-good subset. It's presented as a logical limitation with high confidence, but the reasoning is more of a heuristic counting argument than a formal countermodel—there's no rigorous independence proof constructed. I should probably treat this as plausible reasoning that shows the given proof route needs more structure, rather than a definitive impossibility result.
Now I'm working through the combinatorial count: with word length around log⁡log⁡x\log\log x
loglogx and span bounded by (log⁡x)3(\log x)^3
(logx)3, the number of words with typical span is roughly (Llog⁡x/2L)\binom{L\log x/2}{L}
(LLlogx/2​), which evaluates to approximately eΘ((log⁡log⁡x)2)e^{\Theta((\log\log x)^2)}
eΘ((loglogx)2), matching what the document claims.
For Section 10, I'm noting that the cited reference has an inconsistency — the paper is attributed to Acta Arithmetica 126 (2007) but the arXiv ID 1105.1451 is from May 2011, which would be a later posting. I can't verify the exact details without access, though I recall Schlage-Puchta has work on irrationality of number-theoretic series in that journal.
The comparison claim about the Selberg sieve method not yielding what's needed here is plausible given the context, but I can't verify it externally. I'm also wondering whether the irrationality of ∑pn/2n\sum p_n/2^n
∑pn​/2n might already follow from known results — I believe this is actually still open, though Erdős did prove results about ∑1/2pn\sum 1/2^{p_n}
∑1/2pn​. Gallagher's 1976 paper on prime distribution in short intervals is a real citation from what I recall, though I can't verify it without checking — same caveat applies to Kuperberg's arXiv work on singular series sums. Now I'm checking the Lean code snippets for correctness, particularly the indexing: the prime function uses 0-indexing where P(0) = 2, and the gap function subtracts consecutive primes.
I'm verifying how the delta function translates between the 1-indexed mathematical notation and the 0-indexed Lean implementation — the sum of weighted gaps needs to match across both formulations.
Now I'm checking the Erdős sum definition, confirming it equals twice the original sum S, and noting that the irrationality of one directly implies the irrationality of the other.
I'm also working through the block code formula, which sums weighted values of G over a range of indices up to J. Verifying the mathematical consistency between the Lean definitions and the formulas—checking that the delta step and delta block definitions align with the expected recurrence relations, though I need to be careful about natural number subtraction in Lean. Now checking the SamePrefix case: the equation b(δn+J−δm+J)=2J+1zb(\delta_{n+J}-\delta_{m+J}) = 2^{J+1}z
b(δn+J​−δm+J​)=2J+1z from math (4.2) holds because blockCode n J = blockCode m J follows from the prefix condition, and then the delta difference telescopes to 2J+1(zn−zm)2^{J+1}(z_n-z_m)
2J+1(zn​−zm​), which Lean confirms as ⟨zn - zm, _⟩. Moving into fork_merge_contradiction where the signature requires G(n+J) ≠. J)): needed for $|a-a'|\ge2$ ✓ (in the final theorem they discharge it via eventually_even_prime_gaps ...— a placeholder; fine as blueprint). hsmallJ:H < 2^J / b; hsmallK: H < 2^K` ✓ matches (5.1). Conclusion False ✓.
Now checking the fork_merge_contradiction setup — the hlattice constraint is positioned at n and m, which is necessary for the quantization step. I'm also verifying the positivity of delta: the upper bound argument relies on ∣δ(n+J)−δ(m+J)∣≤2H|δ(n+J)-δ(m+J)| \le 2H
∣δ(n+J)−δ(m+J)∣≤2H, which requires δ≥0\delta \ge 0
δ≥0, though actually ∣A−B∣≤A+B≤2H|A-B|\le A + B \le 2H
∣A−B∣≤A+B≤2H might be the tighter constraint needed.
Since delta is a sum of nonnegative terms, the positivity holds — in Lean this would need a dedicated positivity lemma but it's sound as a blueprint. FourTailBound similarly lacks an explicit 0≤H0 \le H
0≤H constraint, though delta ≥ 0 is provable. The ForkMergeHyp statement now captures the denominator-free form: for any B and N with B > 0, there exist n, m, J, K, H satisfying the prefix/fork/suffix conditions along with the four-tail bound and the two size constraints on H. This should be sufficient for the main theorem.
When instantiating this in the proof, they extract the configuration from ForkMergeHyp and pass N := s, but they need both n ≥ s and m ≥ s for the lattice instantiation — they handle this by using the lattice hypothesis on n with the proof that s ≤ n, and on m with a transitivity argument showing m > n ≥ s. However, there's a gap: the existential form of ForkMergeHyp allows J and K to be 0, which would make the SamePrefix condition vacuous and the quantization at J = 0 yield b(δn−δm)∈2Zb(\delta_n - \delta_m) \in 2\mathbb{Z}
b(δn​−δm​)∈2Z, but then the fork condition at G(n) creates issues for the contradiction argument.
When J = 0, the equality δn=δm\delta_n = \delta_m
δn​=δm​ requires 2H<20+1/b2H < 2^{0+1}/b
2H<20+1/b, which follows from hsmallJ giving H<1/bH < 1/b
H<1/b, so that works. When K = 0, the SameSuffix condition is vacuous, D_1 = a' - a has |D_1| ≥ 2, and FourTailBound bounds the deltas at n+J+1 and m+J+1 by H, but then |D_1| ≤ 2H < 2 contradicts |D_1| ≥ 2 when H < 1 from hsmallK. So dropping the J,K ≥ 1 constraints is harmless. I also notice that ForkMergeHyp doesn't include an even-gap clause or any largeness condition for the even case, unlike what appears elsewhere.
Now I'm checking the even-gaps requirement more carefully. The final proof invokes eventually_even_prime_gaps, which needs the index to be sufficiently large, but the normalization from rational_delta_eventually_even_lattice only guarantees n ≥ s, where s comes from rationality normalization and isn't necessarily large enough. The even-gap property holds for k ≥ 1 (since G(0) = 1 is odd but G(k) is even for k ≥ 1), so if the Lean proof sets N := s and s = 0 with n = 0 and J = 0, then G(n+J) = G(0) = 1, which is odd and violates the requirement.
The fix is straightforward: take N := max(s, 1) instead, ensuring n+J ≥ 1 and m+J ≥ 1 hold. This is a minor blueprint-level issue that's easily repairable, and since the Lean sketch is explicitly non-compiled with sorries and an ellipsis at that exact spot, I'll note it as cosmetic.
Now I'm looking at the HLQuant structure and how uniform_count uses a negative power of the logarithm. The entropy bound for the model fork checks out with J and K set to ⌈8 log log x⌉, matching the required inequality. The final theorem statement for the irrationality of the Erdős sum is correctly formulated. The hash claim for the briefing file can't be verified since the file wasn't provided, and there's a mismatch between the claimed hash and the actual review payload hash.
Now I'm looking for potential gaps to flag as a critical reviewer. The P2 issue in section 8.2 involves an implicit step where the o(Tx)o(T_x)
o(Tx​) claim needs additional justification about how TxT_x
Tx​ is defined. The word entries must all be positive and even-gapped for indices in IxI_x
Ix​ when x≥3x \geq 3
x≥3, which checks out since all subsequent gaps after pn≥xp_n \geq x
pn​≥x are even. The sequence length LxL_x
Lx​ is available for all these indices, so that constraint is satisfied. Q1's design with uniform relative error down to tiny model masses actually forces exact zero counts and guarantees existence when mass is large enough—this makes HLquantHL_{quant}
HLquant​ materially stronger than standard uniform HL, though not a logical gap in the conditional itself. The naming might need clarification for whether we're claiming HL-type results or something genuinely stronger.
There's also the question of whether HLquantHL_{quant}
HLquant​ could be vacuous if Q1 itself is false. The Cramér model predicts max gaps around (log⁡x)2(\log x)^2
(logx)2, but Granville's refinement suggests the model underestimates and max gaps might exceed this by a constant factor—possibly reaching between (log⁡x)2(\log x)^2
(logx)2 and (log⁡x)3(\log x)^3
(logx)3 for infinitely many xx
x, which would contradict Q1's premise. So the singular series correction in the model does account for divisibility structure, but Granville's insight about primorial-rich intervals suggests the actual boost to extreme-gap probabilities goes beyond what the pointwise singular series alone predicts—the Cramér–Granville model captures this by recognizing that certain interval types systematically favor larger gaps in ways the basic Poisson framework misses. So Maier's phenomenon applies to specific short intervals, not to averages across starting points in [x,2x][x,2x]
[x,2x] — those are different statistics. But Maier-type irregularities do reveal that naive uniform error bounds with power-of-log precision fail in certain regimes, which constrains what equidistribution results can actually hold for primes in arithmetic progressions.
Montgomery–Soundararajan's 2004 work on primes in short intervals is particularly relevant here: they computed moments under a strong uniform Hypothesis L with error O(x1/2+ϵ)O(x^{1/2+\epsilon})
O(x1/2+ϵ) and found that the distribution of primes in intervals of length hh
h is approximately normal with variance roughly hlog⁡(x/h)h\log(x/h)
hlog(x/h). This means the Poisson approximation — which would give variance equal to the mean — has corrections that are lower order in 1/log⁡x1/\log x
1/logx, though not as small as powers of log⁡x\log x
logx might naively suggest. For gap statistics at span ∼λlog⁡x\sim \lambda\log x
∼λlogx with fixed λ\lambda
λ, Poisson is believed accurate to leading order, but the corrections are more substantial than one might hope.
The secondary terms in kk
k-point correlations, computed via Gallagher's method, involve summing the singular series S(H)\mathfrak{S}(\mathcal{H})
S(H) over kk
k-element subsets of [0,h][0,h]
[0,h], which yields (hk)(1+Ok((log⁡h)/h))\binom{h}{k}(1 + O_k((\log h)/h))
(kh​)(1+Ok​((logh)/h)) — the relative error per term is of order (log⁡h)/h(\log h)/h
(logh)/h. The key question is pinning down the exact form of the exponential decay factor e−span/log⁡te^{-\text{span}/\log t}
e−span/logt and how the polynomial prefactor behaves.
The heuristic model with (log⁡t)−(ℓ+1)(\log t)^{-(\ell+1)}
(logt)−(ℓ+1) and relative error O((log⁡t)−10)O((\log t)^{-10})
O((logt)−10) is almost certainly too optimistic; even under GRH and the Hardy–Littlewood conjecture with square-root error bounds, the true consecutive-gap distribution is expected to match this model only to relative accuracy like O(span/(log⁡t)2)O(\text{span}/(\log t)^2)
O(span/(logt)2) or O(ℓ2/log⁡t)O(\ell^2/\log t)
O(ℓ2/logt) — polynomially small in 1/log⁡t1/\log t
1/logt, but with exponent 1 rather than 10, and with secondary corrections that remain conjectural. So the specific claim in Q1 with (log⁡x)−10(\log x)^{-10}
(logx)−10 error is almost certainly false unless the model is refined to include secondary terms from the kk
k-tuple integral.
The inclusion–exclusion formula for consecutive primes within a span involves summing over all subsets of gaps, where each term is weighted by the Hardy–Littlewood singular series and integral; the Poisson approximation for "no primes in the complement of H\mathcal{H}
H within the span" introduces an exponential factor exp⁡(−span/log⁡t)\exp(-\text{span}/\log t)
exp(−span/logt) whose corrections are of relative order ∼1/log⁡t\sim 1/\log t
∼1/logt-ish, and these corrections might be absorbed into the model, but achieving the demanded (log⁡x)−10(\log x)^{-10}
(logx)−10 relative error seems to require much finer control than the standard heuristics provide. The Montgomery–Soundararajan result gives the secondary term in the singular series average, showing corrections scale like k2log⁡h/hk^2\log h/h
k2logh/h. With h≍ℓlog⁡xh \asymp \ell\log x
h≍ℓlogx and kk
k up to ℓ\ell
ℓ, these corrections become roughly ℓlog⁡log⁡x/log⁡x\ell\log\log x/\log x
ℓloglogx/logx, which dominates the error term.
Comparing this to (log⁡x)−10(\log x)^{-10}
(logx)−10: the correction is vastly larger—it's actually (log⁡x)−1+o(1)(\log x)^{-1+o(1)}
(logx)−1+o(1). This means the true consecutive prime count should differ from the model by relative errors around 1/log⁡x1/\log x
1/logx (modulo loglog factors), which would make the exponent-10 claim false under standard conjectures. But I need to be careful about where exactly these averaged singular series corrections apply.
The "no prime in between" probability comes out to e−h/log⁡t(1+O(corrections))e^{-h/\log t}(1 + O(\text{corrections}))
e−h/logt(1+O(corrections)), where the corrections involve secondary singular series terms scaled by h/(log⁡t)2h/(\log t)^2
h/(logt)2 and depend on the specific configuration. This is deeply heuristic. The real issue is that Q1 demands relative accuracy of (log⁡x)−10(\log x)^{-10}
(logx)−10 uniformly across all deep-tail words in the closed-form model, which goes far beyond what any standard conjecture supports and is likely false because the model ignores known secondary corrections of order roughly 1/log⁡x1/\log x
1/logx.
The conditional theorem still holds—an implication from false premises is still valid—but the hypothesis itself is problematic: HL_quant isn't a Hardy–Littlewood-type statement but something much stronger and probably false. What matters is that the proof only needs error o(1)o(1)
o(1) relative or even just η/100\eta/100
η/100 relative, so the Aerr=10A_{err}=10
Aerr​=10 bound is massive overkill; the argument uses the inequality 1+ε1−ε(1−η)≤1−η/2\frac{1+\varepsilon}{1-\varepsilon}(1-\eta)\le 1-\eta/2
1−ε1+ε​(1−η)≤1−η/2.
I can repair this by weakening Q1 to allow relative error ≤ε0\le \varepsilon_0
≤ε0​ for some small constant (or o(1)o(1)
o(1)), which makes the hypothesis far more plausible and the proof goes through unchanged. The model itself could be generalized—the derivation only uses Q1-transfer and Q2 for the same model, never the specific form analytically, so the exponential factor and singular series don't actually enter the argument. This suggests the whole framework could be abstracted as a general package depending only on Q1, Q2, Q3 as black-box properties of MxM_x
Mx​.
Checking sections 8.1–8.4 confirms the explicit model form is never used analytically—only Q1, Q2, Q3 appear alongside the unconditional conditions C6–C8. So tying the hypothesis to the explicit form (6.1) makes it unnecessarily strong and possibly false; this is a repairable design issue, not a fatal gap.
Now looking at the Mx(d)=0M_x(d) = 0
Mx​(d)=0 clause... epsilon)M_x$ even when Mx=0M_x = 0
Mx​=0, which is where the clause actually matters — if a non-admissible word somehow had Nx>0N_x > 0
Nx​>0, the bound would fail, but since NxN_x
Nx​ is unconditionally zero there, the clause is automatically satisfied. So the clause adds no real strength but is needed for the termwise upper bound and for properly accounting TxT_x
Tx​. Now checking the four-tails bookkeeping from P3...
The good site controls both offsets JxJ_x
Jx​ and Jx+Kx+1=LxJ_x + K_x + 1 = L_x
Jx​+Kx​+1=Lx​, giving us the four tails we need. The Markov inequality from C7 is applied at both r=Jxr = J_x
r=Jx​ and r=Jx+Kx+1r = J_x + K_x + 1
r=Jx​+Kx​+1, each O(log⁡log⁡x)O(\log\log x)
O(loglogx), which stays within C6's uniformity bounds. For the constants table in P5, the window size Cwin=20C_{win} = 20
Cwin​=20 is sufficient since Lx≤16log⁡log⁡x+3≤20log⁡log⁡xL_x \le 16\log\log x + 3 \le 20\log\log x
Lx​≤16loglogx+3≤20loglogx for log⁡log⁡x≥3/4\log\log x \ge 3/4
loglogx≥3/4. With Hx=(log⁡x)4H_x = (\log x)^4
Hx​=(logx)4, the removal exponent comes from the tail-bad share being (log⁡x)−3(\log x)^{-3}
(logx)−3 relative to the mean.
The span-bad share is log⁡log⁡x/(log⁡x)2\log\log x/(\log x)^2
loglogx/(logx)2, and the relative error of (log⁡x)−10(\log x)^{-10}
(logx)−10 is actually overkill for what's needed. The ratio Hx/2Jx=(log⁡x)−1.545...H_x/2^{J_x} = (\log x)^{-1.545...}
Hx​/2Jx​=(logx)−1.545... decays to zero since 8ln⁡2≈5.545>48\ln 2 \approx 5.545 > 4
8ln2≈5.545>4. With η=1/20\eta = 1/20
η=1/20, the removal budget of η/4=1/80\eta/4 = 1/80
η/4=1/80 needs to cover the bad share of O((log⁡x)−3)O((\log x)^{-3})
O((logx)−3) plus the span contribution.
The inequality (1+ε)(1−η)/(1−ε)≤1−η/2(1+\varepsilon)(1-\eta)/(1-\varepsilon) \le 1-\eta/2
(1+ε)(1−η)/(1−ε)≤1−η/2 holds for ε≲0.0129\varepsilon \lesssim 0.0129
ε≲0.0129, which is satisfied once log⁡x≥1.55\log x \ge 1.55
logx≥1.55. All the numeric checks pass, and the table claim that the block constant 8 makes 2J,2K2^J, 2^K
2J,2K larger than (log⁡x)4(\log x)^4
(logx)4 checks out since (log⁡x)5.545>(log⁡x)4(\log x)^{5.545} > (\log x)^4
(logx)5.545>(logx)4 for log⁡x>1\log x > 1
logx>1. Now I'm comparing C4's requirement against the FM condition to verify they're compatible. Checking that δn\delta_n
δn​ is well-defined and positive from the convergence argument and the fact that gaps between consecutive integers are at least 1. Then reconsidering the pigeonhole principle: if each context (W,V) had at most one fork value among the good starting positions, the total count would be bounded by DxD_x
Dx​, but this needs careful verification of which fork value actually occurs for each context. When the set of admissible contexts is empty, the maximum convention gives zero, which keeps both sides consistent—a measure-zero edge case that doesn't affect the argument. Now checking the structural claims: IxI_x
Ix​ is indeed a set of consecutive prime indices, its cardinality follows from the prime number theorem or Chebyshev bounds unconditionally, and Bertrand's postulate ensures it's nonempty. Moving to section 8.3 and 8.4, where the tail bound is claimed to be at most (log⁡x)4(\log x)^4
(logx)4 and the ratio is being verified.
The FM condition requires checking the ratio along the constructed sequence, which holds since pnx≥x→∞p_{n_x} \geq x \to \infty
pnx​​≥x→∞. The parameters Jx,Kx=⌈8log⁡log⁡x⌉J_x, K_x = \lceil 8\log\log x \rceil
Jx​,Kx​=⌈8loglogx⌉ are constructed to be at least 1, satisfying what FM needs. There's no overlap constraint between the prefix, fork, and suffix windows across the two occurrences—that's already accounted for.
For the bound on δ\delta
δ differences: both values lie in (0,Hr](0, H_r]
(0,Hr​], so their difference is at most HrH_r
Hr​, though the authors use the weaker bound of 2Hr2H_r
2Hr​, which is also valid. This then requires 2Hr<2Jr+1/b2H_r < 2^{J_r+1}/b
2Hr​<2Jr​+1/b, which simplifies to Hr<2Jr/bH_r < 2^{J_r}/b
Hr​<2Jr​/b, and that checks out. The claims in Section 1 about the two arrows being elementary and fully proven from the stated package appear accurate based on this analysis.
Now I'm verifying the ledger entries: HLQ does imply the fork anti-concentration result for prime gap words as stated in (8.1), and that's conditionally proved. The EMP/HASH components are externally unverifiable, though the ledger honestly marks EMP as a 0.50 heuristic. For the TxT_x
Tx​ pattern count claim, I need to confirm that both sides of the sum are constrained identically—the statement specifies all sums run over positive even words with total span at most (log⁡x)3(\log x)^3
(logx)3, so that's consistent. In Q1, the words range over even positive integers, and I should verify the exact constraints match across both questions.
Checking the window sizes: Q1 allows ℓ≤20log⁡log⁡x\ell \le 20\log\log x
ℓ≤20loglogx, but the argument only uses ℓ=Lx\ell = L_x
ℓ=Lx​, which is fine. For the fork gap definition, FM item 2 defines it as gnr+Jr+1g_{n_r+J_r+1}
gnr​+Jr​+1​—the (J+1)-th gap after n—and in section 8.3, when a word (W,a,V)(W,a,V)
(W,a,V) occurs at position n, the fork gap dJ+1=a=gn+Jx+1d_{J+1} = a = g_{n+J_x+1}
dJ+1​=a=gn+Jx​+1​ matches this definition correctly. Now I'm checking the C4 step regarding the next different gap.
The difference formula D1=δn+J+1−δm+J+1D_1 = δ_{n+J+1}−δ_{m+J+1}
D1​=δn+J+1​−δm+J+1​ applies the recurrence relation at position n+J to get δn+J+1=2δn+J−gn+J+1δ_{n+J+1} = 2δ_{n+J} − g_{n+J+1}
δn+J+1​=2δn+J​−gn+J+1​, which checks out. The even-gap step requires indices nr+Jr+1≥2n_r+J_r+1 ≥ 2
nr​+Jr​+1≥2 to ensure we're looking at gaps between odd primes, which holds for large r. I should also verify whether the document claims unconditional progress anywhere in sections 1, 13, or 14.
The paper is appropriately honest about the unconditional nature of the problem. There's a potential concern with Q2 possibly being false for the explicit model due to span truncation at extreme lengths, though boundary contexts carry negligible mass and heuristically Q2 should hold by a large margin—but since it's a hypothesis, it doesn't create a gap. Another subtlety: the maximum value in DxD_x
Dx​ versus the pigeonhole principle's constraint that there's at most one fork value among good sites—the good-site fork value a* might not be the argmax of Nx(W,⋅,V)N_x(W,\cdot,V)
Nx​(W,⋅,V), but the bound uses the maximum anyway, so it's still valid. I'm also checking whether the derivation Tx≥(1−ε)∑MT_x \ge (1-\varepsilon)\sum M
Tx​≥(1−ε)∑M has any issues.
Now I'm verifying the algebraic chain: from Tx≥(1−ε)ΣMT_x \ge (1-\varepsilon)\Sigma M
Tx​≥(1−ε)ΣM, I can rearrange to get ΣM≤Tx/(1−ε)\Sigma M \le T_x/(1-\varepsilon)
ΣM≤Tx​/(1−ε), then substitute into the bound on DxD_x
Dx​ to confirm that Dx≤(1+ε)(1−η)1−εTxD_x \le \frac{(1+\varepsilon)(1-\eta)}{1-\varepsilon}T_x
Dx​≤1−ε(1+ε)(1−η)​Tx​ holds as written. For the constant in equation (8.1) to satisfy the required inequality at large x, I need to check when 1+ε1−ε(1−η)≤1−η/2\frac{1+\varepsilon}{1-\varepsilon}(1-\eta) \le 1-\eta/2
1−ε1+ε​(1−η)≤1−η/2, which constrains ε\varepsilon
ε in terms of η\eta
η.
With η=1/20\eta = 1/20
η=1/20, this gives ε≤0.012987\varepsilon \le 0.012987
ε≤0.012987, matching my earlier calculation. Moving to Section 11, I'm verifying that bδn+Jb\delta_{n+J}
bδn+J​ is indeed a positive integer (since δ>0\delta > 0
δ>0 and n+J≥sn+J \ge s
n+J≥s), and then establishing a lower bound on its 2-adic valuation in terms of JJ
J and the valuation of Cn,JC_{n,J}
Cn,J​.
Now I'm working through the ultrametric property: since bδn+J=2Jbδn−bCn,Jb\delta_{n+J} = 2^J b\delta_n - bC_{n,J}
bδn+J​=2Jbδn​−bCn,J​, the 2-adic valuation of the first term is at least J+1J+1
J+1 (because bδnb\delta_n
bδn​ is even and positive), while the valuation of bCn,JbC_{n,J}
bCn,J​ equals the valuation of Cn,JC_{n,J}
Cn,J​ itself. This means the minimum of these two valuations gives me the bound I need.
From the hypothesis that min⁡{J,v2(Cn,J)}−log⁡2δn+J→+∞\min\{J, v_2(C_{n,J})\} - \log_2 \delta_{n+J} \to +\infty
min{J,v2​(Cn,J​)}−log2​δn+J​→+∞, I can derive that b≥2min⁡/δn+Jb \ge 2^{\min}/\delta_{n+J}
b≥2min/δn+J​ grows without bound, which contradicts the assumption that bb
b is fixed—so the hypothesis must hold.
I'm now checking the internal coherence of Section 12, which involves examining how sequences of word powers with qw→∞q_w \to \infty
qw​→∞ behave under the stated hypothesis. So the lower bound ≥1/b\ge 1/b
≥1/b directly contradicts the hypothesis that this expression goes to zero, which confirms the argument. The derivation hinges on δn≠αw\delta_n \neq \alpha_w
δn​=αw​, which follows from qw∤bq_w \nmid b
qw​∤b, so everything checks out consistently.
I'm also noticing a notation inconsistency: Section 2 introduces unu_n
un​ but the rest of the document uses νn\nu_n
νn​ instead, which looks like a typo. And the definition δn:=νn−pn+1\delta_n := \nu_n - p_{n+1}
δn​:=νn​−pn+1​ references νn\nu_n
νn​ without properly establishing it first.
Verifying the C2 claim about n≥sn \geq s
n≥s: the identity 2nS=∑r=1npr2n−r+νn2^nS = \sum_{r=1}^n p_r 2^{n-r} + \nu_n
2nS=∑r=1n​pr​2n−r+νn​ actually holds for all nn
n, but the integrality condition on bνnb\nu_n
bνn​ requires 2n−sA∈Z2^{n-s}A \in \mathbb{Z}
2n−sA∈Z, which is why we need n≥sn \geq s
n≥s. The FM condition 4 constraints and C4 requirements check out as well. The "Where I am stuck" section is honest and aligns with everything else, and the confidence levels in the ledger look solid across the board.
Now I'm moving to compile the Phase A ledger with the required fields: id, location, verdict (correct/gap/repairable/fatal/cosmetic), one-sentence justification, and confidence. I'll work through the items starting with the notation identities and the early claims. Noting some remaining issues like notation inconsistencies and overconfident confidence scores, plus identifying one repairable gap where the implicit step in section 8.2 needs explicit bridging, and a hypothesis-design finding showing the quantified version is materially stronger than the type-level formulation—though this doesn't break the conditional logic. The core argument still holds despite these gaps.
The logical chain checks out: the FM⇒irrational step is sound, and the HL_quant⇒FM direction works modulo an easy lemma, so the overall structure is valid with fixable issues. There's no circularity in the hypothesis design since no clause quantifies over tails or assumes fork-merge existence; the model-only treatment of Q2 and unconditional handling of tails avoid that trap. But the naming is misleading—this is substantially stronger than Hardy–Littlewood-type results, combining consecutive-Poisson structure with extreme uniformity constraints that force 0/1 laws in the deep tail, leading to Cramér-like gap bounds that are likely false under Granville-type heuristics.
The core issue is whether the fixed error exponent of 10 is too rigid. If true asymptotics have secondary corrections of relative order ~1/log x compared to the model M_x, then |N−M| would be much larger than (log x)^{-10}M, making Q1 false—though this is conjectural based on Montgomery–Soundararajan-type secondary terms I can't verify without access. The safe repair is to weaken A_err to a small constant ε₀ or an o(1) term, which costs nothing since the argument only needs something small anyway. I should flag this as plausibly false as stated but easily repairable, and mark the Montgomery–Soundararajan and Granville support as unverified from memory.
There's also the deep-tail problem: Q1 for words with M_x < 1/2 forces N_x = 0, which is quasi-Cramér-like; under Granville's conjecture about maximal gaps being ≳ 1.12(log x)², even the ℓ=1 case would fail infinitely often (again, memory-based and unverified). On the flip side, for words with M_x just above 1, Q1 becomes overly restrictive.
But here's the sharper issue: when M_x = 2.4, the constraint |N − M| ≤ εM forces N into [2.4(1−ε), 2.4(1+ε)], which contains no integer for sufficiently small ε, making Q1 vacuously false at such words unless they don't exist at all. This reveals an internal tension in Q1 itself. — so the window is roughly [3.0, 4.0], which contains the integer 4. But if M_x(d) lands at, say, 3.7, the window [3.65, 3.75] contains no integer at all. So Q1 fails outright for such words, not because of prime behavior but because the integrality constraint is arithmetically impossible — the model value simply doesn't land close enough to any integer for the bound to hold. For the integral defining M_x, as d increases by 2, the value decreases by a factor around e^{-2/log x}, which is roughly 1 − 2/log x. This means consecutive d values are densely spaced on a logarithmic scale. In the range where M falls between 1/2 and 2, there are about 0.7 log x different d values, and each would need M to land within roughly (log x)^{-10} of an integer—an astronomically tight constraint that's essentially impossible to satisfy across the board. M becomes large enough (above (log x)^{11}), there's room for integers in the approximation window, but the real trouble emerges in the mesoscopic regime where M_x(d) stays between a constant and (log x)^{10} — here the window shrinks to size less than 1, so Q1 fails to find integer solutions for words where M drifts sufficiently far from integers. This mesoscopic band spans roughly (log x)² values, so such problematic words definitely exist within the family. For M in (0,1), the rounding error to N=0 is M itself, which can't satisfy M ≤ εM, so that's impossible. But rounding to N=1 works only when M ≥ 1−ε, meaning roughly M ∈ [1−O(ε), 1). This means any word where M_x(d) falls outside these narrow bands around integers—essentially M not within relative-ε of an integer and M ≲ (log x)^{10}—gets ruled out. So the constraint N ∈ [M(1−ε), M(1+ε)] means for tiny M like 10^{-100}, there's no integer in that interval at all—zero doesn't qualify since M(1−ε) > 0. This means Q1 is mathematically unsatisfiable for every admissible word with sufficiently small M, and such words definitely exist (deep-tail admissible words with specific gap structures). So the quantitative Hilbert-Langlands statement as written is vacuously true for all large x because the hypothesis can never be satisfied.
Wait, let me double-check the exact statement of Q1 from the document to make sure I'm reading this correctly.
Yes, Q1 requires a relative error bound for every word in the family, including those with arbitrarily small positive model mass. Since Nx(d)N_x(d)
Nx​(d) must be a non-negative integer and the interval [M(1−ε),M(1+ε)][M(1-\varepsilon), M(1+\varepsilon)]
[M(1−ε),M(1+ε)] contains no integers when 0<M<11+ε0 < M < \frac{1}{1+\varepsilon}
0<M<1+ε1​, Q1 actually fails for any admissible word with model mass in that range. So the question becomes whether such words actually appear in the constrained family for sufficiently large xx
x. Let me check the simplest case: taking ℓ=1\ell=1
ℓ=1 with a single even digit d1d_1
d1​ where 2≤d1≤(log⁡x)32\le d_1\le(\log x)^3
2≤d1​≤(logx)3.
The set H={0,d1}\mathcal{H} = \{0, d_1\}
H={0,d1​} is admissible for every even d1d_1
d1​ because two points can't cover all residues modulo any prime q≥2q\ge 2
q≥2. Modulo 2, both 0 and d1d_1
d1​ are even, so we only hit residue 0, giving ν2=1<2\nu_2=1<2
ν2​=1<2. Modulo any prime q≥3q\ge 3
q≥3, we hit at most 2 residues, which is less than qq
q. This means S>0\mathfrak{S} > 0
S>0, so Mx>0M_x > 0
Mx​>0. Now if I choose d1=2⌈(log⁡x)3/2⌉−2≤(log⁡x)3d_1 = 2\lceil (\log x)^3/2\rceil - 2 \le (\log x)^3
d1​=2⌈(logx)3/2⌉−2≤(logx)3, the model mass behaves like Mx≈S⋅x(log⁡x)−2e−(log⁡x)2(1+o(1))M_x \approx \mathfrak{S}\cdot x(\log x)^{-2}e^{-(\log x)^2(1+o(1))}
Mx​≈S⋅x(logx)−2e−(logx)2(1+o(1)), which decays super-polynomially.
Comparing the exponential decay e−(log⁡x)2e^{-(\log x)^2}
e−(logx)2 against the polynomial growth x=elog⁡xx = e^{\log x}
x=elogx, I get Mx=elog⁡x−(log⁡x)2(1+o(1))→0M_x = e^{\log x - (\log x)^2(1+o(1))} \to 0
Mx​=elogx−(logx)2(1+o(1))→0 extremely fast—definitely less than 1/(1+ε)1/(1+\varepsilon)
1/(1+ε) for large xx
x. The integral bound also checks out: ∫x2x(log⁡t)−2e−d1/log⁡tdt\int_x^{2x}(\log t)^{-2}e^{-d_1/\log t}dt
∫x2x​(logt)−2e−d1​/logtdt is dominated by the right endpoint, giving roughly x⋅e−d1/log⁡2x(log⁡x)−2x\cdot e^{-d_1/\log 2x}(\log x)^{-2}
x⋅e−d1​/log2x(logx)−2, and with d1≈(log⁡x)3d_1 \approx (\log x)^3
d1​≈(logx)3, the exponent becomes −(log⁡x)2(1+o(1))-(\log x)^2(1+o(1))
−(logx)2(1+o(1)), which matches. Finally, the singular series S({0,d1})\mathfrak{S}(\{0,d_1\})
S({0,d1​}) is bounded by a product over primes dividing d1d_1
d1​.
So the conclusion is solid: for all sufficiently large xx
x, the family admits admissible words with 0<Mx<10 < M_x < 1
0<Mx​<1, which makes the quantitative Hardy-Littlewood conjecture as stated provably false unconditionally—no dependence on unproven prime-theoretic assumptions. The "conditional theorem" becomes vacuous. But wait, let me verify this is truly airtight by checking whether any integer can actually fall in the interval [M(1−ε),M(1+ε)][M(1-\varepsilon), M(1+\varepsilon)]
[M(1−ε),M(1+ε)] when 0<M<1/(1+⋯ )0 < M < 1/(1+\cdots)
0<M<1/(1+⋯). So the real problem is that HL_quant is actually false—it's inconsistent with the integrality constraints in the small-mass regime—which makes the implication vacuously true but completely useless as a theorem. The deeper question becomes whether the hypothesis itself smuggles in assumptions equivalent to the conclusion, or if it's just materially too strong; the document hints that the relative form's power to sum over arbitrary word families is essential, suggesting the hypothesis design has a fundamental flaw beyond mere circularity.
There are straightforward fixes: add an additive error floor to the mixed bound, impose a mass threshold like M_x(d) ≥ (log x)^B to exclude low-mass words, or apply relative error only after aggregating sub-families. But each repair cascades through the proof of 8.1—the transfer argument requires termwise upper bounds N ≤ (1+ε)M across the entire word family, so introducing a mass threshold means low-mass words still feed into T_x/D_x and the whole argument needs restructuring. The total additive error across all words stays manageable since there are only polynomially many words, so I can reformulate the bound as |N−M| ≤ εM + x^{2/3}, which has the right shape for GRH-type estimates. This lets me bound D_x by summing over all word and variable pairs, where each term contributes at most (1+ε)M plus a context-dependent error, keeping the overall bound below (1+ε)(1−η). So I need to verify that the bound holds by relating ΣM to T_x through the inequality T_x ≥ (1−ε)ΣM − x^{2/3}, which gives me ΣM ≤ (T_x + x^{2/3})/(1−ε), and then checking that the final bound D ≤ (1−η/2)T_x is achievable for large x.
Now I'm evaluating whether the proof structure is sound: the implication chain checks out, but the hypothesis itself turns out to be provably false, making the conditional technically vacuous even though the reasoning is valid. The core issue is that the hypothesis needs an additive error floor added to it without disrupting the overall proof architecture. The core issue is that the hypothesis HL_quant is demonstrably false (probability near zero), which undermines the entire proof chain's significance—the logical steps themselves are valid, but they're built on a refuted premise. The document presents HL_quant with a confidence rating of 0.55 as plausible, yet this contradicts the mathematical reality that it's provably false, making the fatal flaw one of hypothesis design rather than deductive reasoning. The deep-tail words with d₁ near (log x)³ exist for all large x and always satisfy M ∈ (0,1), so M_x(d) stays definitively less than 1 for those cases. Rereading equation (6.1), the integral involves the Siegel-Walfisz constant divided by (log t)^{ℓ+1} with an exponential decay term where the exponent is span/(log t) with span = (log x)³·(1−o(1)), and for ℓ=1 this makes the integrand decay like (log x)^{-2} times an exponentially small factor.
The integral over [x, 2x] is bounded by x times that exponentially small term, which goes to zero, confirming M_x(d) ∈ (0, e^{−(1/2)(\log x)^2}) for large x. With ε_x = (log x)^{-10} < 1, the interval [M(1−ε), M(1+ε)] stays strictly in (0,1) and contains no integers—the argument is airtight and elementary. Now checking admissibility of the pair {0, d₁} where d₁ is even and ≥ 2: modulo 2 both elements are 0, giving just one residue class, which satisfies the requirement of fewer than 2 classes since ν₂ = 1 < 2. For odd primes p I need to verify the residue classes.
The singular series for {0, d₁} evaluates to 2C₂ times a product over odd primes dividing d₁, each factor (p−1)/(p−2) positive, giving a positive constant of the twin-prime type. The standard convergence argument confirms this: each factor in the product representation is positive since ν_q ≤ 2 < q for q ≥ 3, and for q = 2 the factor equals 2, which is also positive. So Phase A has successfully identified gaps.
The main issue is Q1 as stated is unsatisfiable—this undermines the hypothesis's non-vacuity, though the logical implication itself remains sound. There's also an implicit assumption that T_x ≈ |I_x| which is fixable and straightforward. A few minor presentation issues round out the list.
Now looking at P1's question about whether the singular-series model plausibly proves something: Q2 (restricted to the model) appears plausibly true with room to spare—heuristically the maximum conditional mass on a is O(1/log x)—but a rigorous proof remains open. This is a well-posed unconditional problem about singular series behavior. The model-only framing is sound. Both directions have arguments: the Poisson-like conditional distribution of a and Gallagher-type bounds on singular-series weights suggest it could work, though boundary and degenerate cases need care.
Against it: the max-inside-sum interaction is delicate, correlations of the singular series across different a and contexts near k ≍ log log x lack proven uniformity, span truncation couples contexts in ways that complicate analysis, and there's no literature covering windows that grow with x. So it's plausibly provable but genuinely open.
For P5 I've recomputed the constants and they all check out. The error tolerance A_err=10 is actually 100 times larger than needed—only ε ≤ ~0.013 is required—and given the fatal finding about Q1, it's actively harmful in the small-mass regime. The window size of 20 versus 16+3 works, and 8ln2 ≈ 5.545 exceeds the threshold of 4. The removal exponents of 3 for the tail and 2 for the span are appropriate.
P6 confirms the epsilon bookkeeping throughout. P7 verifies that the proof derives and uses exact equality with no "not an integer" clause anywhere, so immunity holds. The caveat is that it requires a_r ≠ a'_r and even gaps, which are structural properties supplied by pigeonhole and large indices.
For P2, the step is both necessary—P8.2 depends on it—and true, though the document leaves it implicit. The statement that every start index carries some word and only the span filter removes indices is correct, and for x > 2 the word is automatically even and positive, with non-admissible words contributing zero.
Now I'm clarifying that T_x sums N over all even positive words with span at most the bound, so every start index with acceptable span contributes to exactly one word's count, and that word is guaranteed to be even and positive. Non-admissible words simply have N = 0, which is consistent. This gives T_x as the count of indices in I_x with span at most (log x)³, which equals (1 − O(loglog x/(log x)²))|I_x|.
P3 checks out with two offsets per site, both sites good yielding four bounds, and C7 covering exactly the offsets {J_x, J_x + K_x + 1}.
P4 is verified...
For non-admissible d, the condition N_x(d) = 0 holds unconditionally for large x since any covered prime q ≤ ℓ + 1 < x would have to divide a prime ≥ x, which is impossible. The clause is needed for the termwise upper bound in section 8.1 to prevent a hypothetical N > 0 at M = 0 from breaking the D_x transfer, or equivalently one restricts sums to admissible words and applies the same unconditional fact. Either way adds no conjectural strength. There's a subtle interplay here with the fatal finding: the boundary case "M = 0 ⟹ N = 0" is exactly where Q1 becomes unsatisfiable for M > 0, and the document caught the M = 0 edge but missed the 0 < M < 1 edge—worth making explicit.
The flaw is essentially one epsilon away from something they already considered. For Phase A, I'm very confident in the unsatisfiability argument since it's elementary. Let me do a quick numerical sanity check on the integral bound with a concrete large x value to be extra sure. Taking x = e^100 (so log x = 100), I can estimate d₁ ≈ 10^6 and the span/log t ratio falls in a range around 10^4, giving an exponentially small bound that confirms the asymptotic behavior.
For the threshold where M ≈ 1, I can calculate that d₁ ≈ (log x)² − 2 log x log log x, which for x = e^100 gives roughly d₁ ≈ 9079. This means across all even d₁ values in the range of thousands, M stays strictly between 0 and 1, providing thousands of counterexample words that satisfy the constraints.
I'm also checking whether the document might have intended Q1 only for words with sufficient mass or whether the span bound implicitly excludes tiny-mass words, but the universal phrasing and explicit discussion of M=0 cases make clear they meant the reading to apply broadly. Even allowing ℓ=1, I can construct in-family counterexamples, so there's no escape clause there either.
So the fatal finding holds. C10's proof itself is internally valid—it correctly derives FM from HLQ using Q1 termwise without division by zero—but the antecedent HLQ is provably false, making the implication vacuously true. C11 has the same structure. The real problem is the ledger's entry rating HLQ as "0.55 als plausible Hypothese" when the correct value is approximately 0, which is a provably false claim and represents the core defect against the document's own stated conclusions.
Now I'm reconsidering whether this counts as "unsound" under the review taxonomy. The conditional chain is complete and mathematically correct, but the document simultaneously claims—across multiple sections—that HL_quant is an open, unresolved hypothesis whose proof would complete the program. That's the fatal contradiction: HL_quant isn't open; it's refuted. A reader following the document's stated mathematical program would be attempting to prove a false statement, so the program as specified is broken, though it could be salvaged with the additive-floor correction. The logic holds up: N_x is definitely an integer as a count, M_x(d) stays strictly positive for admissible words, and the interval can't contain zero unless M itself is zero—so the refutability argument is solid at 0.97 confidence. Let me verify the remaining details: the even positive integers constraint checks out, the (1−o(1)) claim follows from the logarithmic bounds, and I need to confirm how the tail-bad start sites factor into the span-ok population. Now checking whether the hypothesis contains any hidden circularity—the clauses about tails, irrationality, and fork existence don't directly assume the conclusion, though the integrality observation does create an equivalence between Q1's relative form at sub-unit masses and strong existence/non-existence statements about the count N relative to the mass M. Most values of M below (log x)^{10}/2 fall outside these thin bands around integers, making the condition generically unsatisfiable. The cleanest counterexample is M < 1/(1+ε), where the window contains no integers at all—no way around it. I'll use this as the main theorem-grade counterexample and explain the banding structure as the broader structural issue.
Now I need to address whether Q1 is materially stronger than classical HL even after the additive-floor repair, particularly around the consecutive-integer constraint. Checking references and Mathlib module paths — some citations are unverified or possibly mislabeled, and I'm uncertain about the exact location of certain Lean library modules like the irrationality definitions, which might be scattered across different namespaces than initially recalled. The SHA claim about the third file can't be verified here, but I can compute checksums for the two files we have. For Section 6.2's singular series formula, the definition looks standard—the product over primes with the convergence argument checks out since for large q the factor behaves like 1 + O(|H|²/q²), which converges properly.
I'm also verifying that the non-admissible case (setting the singular series to zero) is consistent with the Euler product having a zero factor when ν_q = q, and the exponent (log t)^{ℓ+1} matches the constraint structure from ℓ+1 primes. The bound in (Q2) with η=1/20 giving a "deterministic mass ≤ 95%" interpretation checks out, and the relative error claim in 6.4's table aligns with the usage in 8.1. The window constraint ℓ ≤ 20 log log x for complete words also matches Q3.
Now I'm clarifying that the statement about the explicit local model is textual—it refers specifically to the model's sums M_x—but since the constants are pinned down (η=1/20, J=K=⌈8 log log x⌉, span cutoff), Q2 becomes a fully concrete open problem in analytic number theory.
I'm examining whether this is plausibly provable for the standard singular-series model from both angles: the heuristic argument suggests the conditional law of (W,V) under M scales with the singular series and an exponential decay term, and for the pure Poisson case where the singular series is constant across a, the maximum mass concentrates around 2/log t, which vanishes much faster than 1−η.