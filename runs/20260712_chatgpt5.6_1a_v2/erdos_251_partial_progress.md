# Erdős Problem #251 — rigorous partial progress

## Input integrity

- Input file: `1a_blind.md`
- SHA-256:

```text
482f56ab95bbd912a68b3ade54d4de87cffb721ffda5f6016efdf18023a78fce
```

No web search or external literature was used. The historical attribution and the claims about the present state of the literature in the input are **UNVERIFIED** here and are not used in any proof.

## Result in one paragraph

I do not resolve the irrationality of

\[
S=\sum_{n\ge 1}\frac{p_n}{2^n}.
\]

I prove a new deterministic obstruction to rationality. Under rationality, two occurrences of the same length-\(J\) prime-gap word force their terminal weighted tails either to be identical or to differ by at least \(2^J/b\), where \(b\) is the odd part of the denominator of \(S\). This gives a **fork–merge obstruction**: two gap strings of the form \(W\,a\,V\) and \(W\,b\,V\), with \(a\ne b\), cannot occur with both common contexts sufficiently long relative to the four relevant tail sizes. From this I derive an exact conditional irrationality theorem and a purely gap-theoretic corollary under a stated polylogarithmic gap bound. I also construct a rational countermodel with positive even unbounded gaps, weighted tails of order \(\log n\), and arbitrarily long equal-gap runs. Thus qualitative gap irregularity and long arithmetic-progression runs alone cannot prove the conjecture; a non-degeneracy or incompatible-context ingredient is essential.

---

# 1. CLAIMS ledger

All indices in the main writeup are one-based for primes, with
\(g_n=p_{n+1}-p_n\). The weighted future-gap tail is

\[
\delta_n:=\sum_{j\ge1}\frac{g_{n+j}}{2^j}.
\]

The convergence of the displayed prime series is taken as part of the problem's setup. Every rearrangement below is either a finite telescoping identity or a split/reindexing of a convergent nonnegative series.

| ID | Exact statement | Status | Dependencies | Confidence |
|---|---|---|---|---:|
| **C1** | For every \(n\ge0\) and \(J\ge0\), \(\delta_n=\sum_{r=1}^{J}g_{n+r}/2^r+2^{-J}\delta_{n+J}\). In particular, \(\delta_{n+1}=2\delta_n-g_{n+1}\). | proved | definitions | 1.00 |
| **C2** | \(S\in\mathbb Q\) iff one, equivalently every, \(\delta_n\in\mathbb Q\). More precisely, if \(S=a/(2^s b)\) with \(b\) odd, then \(b\delta_n\in\mathbb Z\) for every \(n\ge s\). | proved | C1 | 1.00 |
| **C3** | If \(S=a/(2^s b)\), \(n,m\ge s\), and \(g_{n+r}=g_{m+r}\) for \(1\le r\le J\), then \(b(\delta_{n+J}-\delta_{m+J})\in 2^J\mathbb Z\). Hence either the terminal tails are equal or \(|\delta_{n+J}-\delta_{m+J}|\ge2^J/b\). | proved | C1, C2 | 1.00 |
| **C4** | **Fork–merge obstruction.** Suppose two gap strings have a common prefix of length \(J\), distinct next gaps, and a common suffix of length \(K\). Under the lattice conclusion of C2, if the two tails after the prefix differ by less than \(2^J/b\), while the two tails after the suffix differ by less than \(2^K\), then a contradiction follows. | proved | C1–C3 | 1.00 |
| **C5** | If there are fork–merge configurations arbitrarily far out for which the maximum of the four relevant tails is \(o(2^J)\) and \(o(2^K)\), then \(S\) is irrational. | proved | C4 | 1.00 |
| **C6** | Assume \(g_t\le C(\log(t+2))^A\) eventually. If fork–merge configurations occur at terminal height \(M_r\) with both \(J_r-A\log_2\log(M_r+2)\to+\infty\) and \(K_r-A\log_2\log(M_r+2)\to+\infty\), then \(S\) is irrational. | proved | C5 and the inline tail estimate in §6 | 0.99 |
| **C7** | For an equal-gap run \(g_{n+1}=\cdots=g_{n+J}=c\), rationality forces exact locking \(\delta_n=\delta_{n+J}=c\) whenever \(|\delta_{n+J}-c|<2^J/b\). | proved | C1, C2 | 1.00 |
| **C8** | There exists a strictly increasing odd integer sequence \((a_n)\) whose gaps are positive, even, unbounded and \(\Theta(\log n)\), whose gap sequence contains arbitrarily long constant runs at differences divisible by every prescribed finite set of moduli, but for which \(\sum a_n/2^n=7\). | proved | explicit construction in §7 | 1.00 |
| **C9** | A strategy using only positivity/evenness, unboundedness, logarithmic tail scale, and arbitrarily long equal-gap runs is insufficient; it must use a genuinely prime-specific incompatibility or a nonzero-tail condition. | false-start | C8 | 1.00 |
| **C10** | A random-symbolic heuristic suggests that fork–merge contexts should be more plentiful than very long constant-gap runs, but no statement of this kind for the actual prime gaps is proved here. | heuristic | none | 0.35 |

---

# 2. Elementary identities and the rationality lattice

Let

\[
u_n:=\sum_{k\ge1}\frac{p_{n+k}}{2^k},
\qquad
\delta_n:=u_n-p_{n+1}.
\]

Since

\[
p_{n+k}=p_{n+1}+\sum_{r=1}^{k-1}g_{n+r},
\]

nonnegative-series rearrangement gives

\[
\delta_n
 =\sum_{k\ge1}\frac{p_{n+k}-p_{n+1}}{2^k}
 =\sum_{r\ge1}g_{n+r}\sum_{k\ge r+1}2^{-k}
 =\sum_{r\ge1}\frac{g_{n+r}}{2^r}.
\]

Splitting this series after \(J\) terms proves **C1**:

\[
\boxed{
\delta_n=
\sum_{r=1}^{J}\frac{g_{n+r}}{2^r}
+\frac{\delta_{n+J}}{2^J}.}
\tag{2.1}
\]

For \(J=1\),

\[
\boxed{\delta_{n+1}=2\delta_n-g_{n+1}.}
\tag{2.2}
\]

Also,

\[
u_n
=2^n\left(S-\sum_{j=1}^{n}\frac{p_j}{2^j}\right).
\tag{2.3}
\]

If \(S=a/(2^s b)\) with \(a\in\mathbb Z\), \(s\ge0\), and odd \(b\ge1\), then for every \(n\ge s\), equation (2.3) gives \(bu_n\in\mathbb Z\). Since \(p_{n+1}\in\mathbb Z\),

\[
\boxed{b\delta_n\in\mathbb Z\qquad(n\ge s).}
\tag{2.4}
\]

Conversely, if one \(\delta_n\) is rational, then \(u_n=p_{n+1}+\delta_n\) is rational, and (2.3) solves for \(S\) as a rational number. This proves **C2**.

The key point is that (2.4) is a lattice condition on the tail state, not a congruence restriction on an individual gap. The recurrence (2.2) propagates the lattice automatically.

---

# 3. Repeated-block quantization

Assume \(S=a/(2^s b)\), with \(b\) odd, and let \(n,m\ge s\). Suppose the next \(J\) gaps agree:

\[
g_{n+r}=g_{m+r}\qquad(1\le r\le J).
\tag{3.1}
\]

Subtracting the two instances of (2.1), the finite blocks cancel:

\[
\delta_n-\delta_m
=2^{-J}(\delta_{n+J}-\delta_{m+J}).
\]

Thus

\[
b(\delta_{n+J}-\delta_{m+J})
=2^J b(\delta_n-\delta_m).
\]

By (2.4), the right-hand side lies in \(2^J\mathbb Z\). Therefore

\[
\boxed{
b(\delta_{n+J}-\delta_{m+J})\in2^J\mathbb Z.}
\tag{3.2}
\]

This proves **C3**, including the separation alternative

\[
\boxed{
\delta_{n+J}=\delta_{m+J}
\quad\text{or}\quad
|\delta_{n+J}-\delta_{m+J}|\ge\frac{2^J}{b}.}
\tag{3.3}
\]

## Interpretation

Under rationality, a repeated gap word of length \(J\) acts as a high-resolution decoder of the terminal tail state. If both possible terminal tails lie in an interval shorter than \(2^J/b\), then they must be exactly equal. This applies to arbitrary repeated gap words, not only to constant-gap runs.

An equivalent residue formulation follows by multiplying (2.1) by \(b2^J\):

\[
b\delta_{n+J}
\equiv
-b\sum_{r=1}^{J}2^{J-r}g_{n+r}
\pmod{2^J}.
\tag{3.4}
\]

Thus, once the terminal integer \(b\delta_{n+J}\) is known to lie in a range of length below \(2^J\), the preceding length-\(J\) gap block determines it uniquely.

---

# 4. Exact locking for a constant-gap run

Suppose

\[
g_{n+1}=g_{n+2}=\cdots=g_{n+J}=c.
\tag{4.1}
\]

Equation (2.1) becomes

\[
\delta_n-c=2^{-J}(\delta_{n+J}-c).
\tag{4.2}
\]

Under rationality and \(n\ge s\), \(b(\delta_n-c)\in\mathbb Z\). Therefore, if

\[
|\delta_{n+J}-c|<\frac{2^J}{b},
\tag{4.3}
\]

then (4.2) gives \(|b(\delta_n-c)|<1\), so this integer is zero. Hence

\[
\boxed{\delta_n=c\quad\text{and}\quad\delta_{n+J}=c.}
\tag{4.4}
\]

This is **C7**. It sharpens the usual squeeze argument: a sufficiently long equal-gap run does not merely threaten rationality; under rationality it must be perfectly balanced by the entire infinite future tail. The countermodel in §7 shows that this exact-equality escape is real and cannot be discarded.

---

# 5. The fork–merge obstruction

The following configuration uses arbitrary words and removes the exact-equality escape.

Take two starting indices \(n<m\). Assume:

1. **Common prefix** of length \(J\):
   \[
   g_{n+r}=g_{m+r}\qquad(1\le r\le J).
   \tag{5.1}
   \]
2. **Fork** at the next gap:
   \[
   a:=g_{n+J+1}\ne g_{m+J+1}=:a'.
   \tag{5.2}
   \]
3. **Common suffix** of length \(K\):
   \[
   g_{n+J+1+r}=g_{m+J+1+r}
   \qquad(1\le r\le K).
   \tag{5.3}
   \]

Symbolically the two gap words are

\[
W\,a\,V
\qquad\text{and}\qquad
W\,a'\,V,
\]

with \(|W|=J\), \(|V|=K\), and \(a\ne a'\).

Assume for contradiction that \(S=a_0/(2^s b)\), with \(b\) odd, and that \(n,m\ge s\). Put

\[
D_0:=\delta_{n+J}-\delta_{m+J}.
\]

By **C3**, either \(D_0=0\) or \(|D_0|\ge2^J/b\). Therefore the smallness condition

\[
|D_0|<\frac{2^J}{b}
\tag{5.4}
\]

forces \(D_0=0\).

Apply the recurrence (2.2) across the fork:

\[
\begin{aligned}
D_1
&:=\delta_{n+J+1}-\delta_{m+J+1}\\
&=2D_0-(a-a')\\
&=-(a-a').
\end{aligned}
\tag{5.5}
\]

Since \(a,a'\) are distinct integers,

\[
|D_1|=|a-a'|\ge1.
\tag{5.6}
\]

Across each gap in the common suffix, the gap terms cancel in the difference recurrence, so the difference doubles. After \(K\) common suffix gaps,

\[
\delta_{n+J+K+1}-\delta_{m+J+K+1}=2^K D_1.
\tag{5.7}
\]

Consequently,

\[
\left|\delta_{n+J+K+1}-\delta_{m+J+K+1}\right|
=2^K|a-a'|
\ge2^K.
\tag{5.8}
\]

This contradicts the second smallness condition

\[
\left|\delta_{n+J+K+1}-\delta_{m+J+K+1}\right|<2^K.
\tag{5.9}
\]

We have proved **C4**:

> **Fork–merge theorem.** Under the rationality lattice, a common length-\(J\) prefix, one differing integer gap, and a common length-\(K\) suffix are incompatible with (5.4) and (5.9).

A convenient sufficient bound is obtained by defining

\[
H:=\max\{\delta_{n+J},\delta_{m+J},
\delta_{n+J+K+1},\delta_{m+J+K+1}\}.
\tag{5.10}
\]

All four tails are nonnegative, so each of the two absolute differences in (5.4) and (5.9) is at most \(H\). Hence rationality is impossible whenever

\[
\boxed{bH<2^J\quad\text{and}\quad H<2^K.}
\tag{5.11}
\]

The first common context defeats the unknown odd denominator. The second common context amplifies the single differing gap until it exceeds the available tail range.

---

# 6. Conditional irrationality theorems

## 6.1 Direct small-tail fork–merge criterion

For each \(r\), suppose there are integers

\[
n_r<m_r,\qquad J_r,K_r\ge1,
\]

satisfying the fork–merge equalities (5.1)–(5.3). Let

\[
H_r:=\max\{\delta_{n_r+J_r},\delta_{m_r+J_r},
\delta_{n_r+J_r+K_r+1},
\delta_{m_r+J_r+K_r+1}\}.
\]

Assume

\[
\min(n_r,m_r)\longrightarrow\infty,
\tag{6.1}
\]

and

\[
\frac{H_r}{2^{J_r}}\longrightarrow0,
\qquad
\frac{H_r}{2^{K_r}}\longrightarrow0.
\tag{6.2}
\]

Then \(S\) is irrational.

### Proof

If \(S=a_0/(2^s b)\), choose \(r\) large enough that \(n_r,m_r\ge s\), \(bH_r<2^{J_r}\), and \(H_r<2^{K_r}\). Equation (5.11) gives a contradiction. This proves **C5**. \(\square\)

This hypothesis is exact: it says precisely where the unknown denominator is spent and exactly how much tail control is required.

## 6.2 A purely gap-theoretic corollary

The direct theorem still mentions \(\delta\). The next lemma converts a stated pointwise gap bound into a tail bound.

### Tail estimate

Assume that for some integer \(A\ge1\), constant \(C>0\), and index \(N_0\),

\[
g_t\le C(\log(t+2))^A\qquad(t\ge N_0).
\tag{6.3}
\]

Then there is a constant \(C_A'>0\), depending only on \(A,C,N_0\), such that

\[
\boxed{\delta_t\le C_A'(\log(t+2))^A\qquad(t\ge N_0).}
\tag{6.4}
\]

Indeed,

\[
\delta_t
\le C\sum_{r\ge1}\frac{(\log(t+r+2))^A}{2^r}.
\]

Since

\[
t+r+2\le(t+2)(r+1),
\]

we have

\[
\log(t+r+2)\le\log(t+2)+\log(r+1).
\]

For \(A\ge1\),

\[
(x+y)^A\le2^{A-1}(x^A+y^A).
\]

Therefore

\[
\delta_t
\le C2^{A-1}\left(
(\log(t+2))^A\sum_{r\ge1}2^{-r}
+
\sum_{r\ge1}\frac{(\log(r+1))^A}{2^r}
\right).
\]

The second series converges because \((\log(r+1))^A\le(r+1)^A\) and every polynomial times \(2^{-r}\) is summable. This proves (6.4) inline.

Now let fork–merge configurations be indexed by \(r\), and define their terminal height by

\[
M_r:=m_r+J_r+K_r+1.
\]

Assume (6.1), (6.3), and

\[
J_r-A\log_2\log(M_r+2)\longrightarrow+\infty,
\tag{6.5}
\]

\[
K_r-A\log_2\log(M_r+2)\longrightarrow+\infty.
\tag{6.6}
\]

By (6.4),

\[
H_r\le C_A'(\log(M_r+2))^A.
\]

Furthermore,

\[
\frac{2^{J_r}}{(\log(M_r+2))^A}
=2^{J_r-A\log_2\log(M_r+2)}\longrightarrow\infty,
\]

and similarly for \(K_r\). Thus (6.2) holds, and **C5** proves irrationality. This proves **C6**.

### Exact use of the assumptions

- The eventual bound (6.3) is used only to derive (6.4).
- Condition (6.5) pays for the unknown odd denominator \(b\) through the repeated prefix.
- Condition (6.6) ensures that the one-gap fork, amplified through the repeated suffix, cannot fit inside the terminal tail range.
- No distribution theorem for primes, no prime-tuple conjecture, and no literature result is invoked.

Whether the actual prime gaps satisfy either (6.3) or the required fork–merge recurrence is **UNVERIFIED** here.

---

# 7. A rational countermodel with prime-like coarse features

This construction proves **C8** and rigorously identifies a false start.

## 7.1 State sequence

For \(k\ge0\), set

\[
c_k:=2k+4,
\qquad
L_k:=2^{c_k},
\qquad
N_0:=0,
\qquad
N_{k+1}:=N_k+L_k.
\]

Define a positive even integer state sequence \((x_n)_{n\ge0}\) by

\[
x_n:=c_k\qquad\text{when }N_k\le n<N_{k+1}.
\tag{7.1}
\]

Define gaps

\[
g_{n+1}:=2x_n-x_{n+1}\qquad(n\ge0).
\tag{7.2}
\]

Inside the \(k\)-th state block, \(x_{n+1}=x_n=c_k\), so

\[
g_{n+1}=c_k.
\tag{7.3}
\]

At the transition to the next state block,

\[
g_{n+1}=2c_k-c_{k+1}=c_k-2\ge2.
\tag{7.4}
\]

Thus every gap is a positive even integer. The gaps are unbounded because \(c_k\to\infty\).

Now set

\[
a_1:=3,
\qquad
a_{n+1}:=a_n+g_n.
\tag{7.5}
\]

Then \((a_n)\) is strictly increasing and every \(a_n\) is odd.

## 7.2 The weighted sum is rational

For every \(N\ge1\), (7.2) telescopes:

\[
\begin{aligned}
\sum_{j=1}^{N}\frac{g_j}{2^j}
&=\sum_{j=1}^{N}\frac{2x_{j-1}-x_j}{2^j}\\
&=\sum_{j=1}^{N}\frac{x_{j-1}}{2^{j-1}}
 -\sum_{j=1}^{N}\frac{x_j}{2^j}\\
&=x_0-\frac{x_N}{2^N}.
\end{aligned}
\tag{7.6}
\]

Here \(x_N=O(\log N)\), so \(x_N/2^N\to0\). Since \(x_0=c_0=4\),

\[
\sum_{j\ge1}\frac{g_j}{2^j}=4.
\tag{7.7}
\]

For any increasing sequence with gaps \(g_j=a_{j+1}-a_j\), nonnegative-series rearrangement gives

\[
\sum_{n\ge1}\frac{a_n}{2^n}
=a_1+\sum_{j\ge1}\frac{g_j}{2^j}.
\tag{7.8}
\]

Therefore

\[
\boxed{\sum_{n\ge1}\frac{a_n}{2^n}=3+4=7.}
\tag{7.9}
\]

## 7.3 Its weighted tails have logarithmic size

Define

\[
\Delta_n:=\sum_{j\ge1}\frac{g_{n+j}}{2^j}.
\]

The shifted version of (7.6) gives

\[
\boxed{\Delta_n=x_n.}
\tag{7.10}
\]

Moreover,

\[
N_k=\sum_{i=0}^{k-1}2^{2i+4}
=\frac{16(4^k-1)}{3}.
\tag{7.11}
\]

For \(N_k\le n<N_{k+1}\), equations (7.1) and (7.11) imply

\[
x_n=2k+4=\log_2(n+2)+O(1).
\tag{7.12}
\]

Hence both the state tails and the gap sizes are \(\Theta(\log n)\), apart from an immaterial bounded initial segment.

## 7.4 Arbitrarily long locally compatible equal-gap runs

The \(k\)-th state block contains \(L_k-1=2^{c_k}-1\) consecutive gaps equal to \(c_k\). Thus equal-gap runs have unbounded length.

More strongly, fix any \(J\). Choose an even integer \(c\ge4\) divisible by

\[
\operatorname{lcm}(1,2,\ldots,J+1).
\]

Since \(c_k\) runs through every even integer at least \(4\), some \(c_k=c\). The corresponding constant-gap run has length \(2^c-1>J\), and its difference is divisible by every modulus up to \(J+1\). This mimics the elementary divisibility compatibility required of a long prime arithmetic progression, though the terms \(a_n\) are not claimed to be prime.

## 7.5 Why the squeeze does not fire

On an interior constant state block, \(\Delta_n=c_k\) at both ends of every equal-gap subrun. Thus the factor

\[
\Delta_{n+J}-c_k
\]

is exactly zero. The run can be extraordinarily long and occur at low height, yet the rational sequence survives through the exact-locking escape identified in **C7**.

Therefore **C9** is rigorous: positivity, parity, unbounded gaps, logarithmic tail scale, and arbitrarily long equal-gap runs do not suffice by themselves. Any successful proof must exclude exact tail locking or produce incompatible repeated contexts such as the fork–merge pattern.

---

# 8. Lean-ready lemma statements

The code below is a Lean-oriented specification, not compile-tested code. It uses a zero-indexed increasing sequence \(q\), matching `Nat.nth Nat.Prime`; thus `q 0 = 2`. Cast and library names may require routine adaptation.

```lean
noncomputable section
open scoped BigOperators Topology

/-- Real-valued gap of a zero-indexed natural sequence. -/
def gap (q : Nat → Nat) (n : Nat) : Real :=
  (q (n + 1) : Real) - (q n : Real)

/-- Weighted future-gap tail. This is the zero-indexed version of δ_n. -/
def Delta (q : Nat → Nat) (n : Nat) : Real :=
  ∑' r : Nat, gap q (n + r) / ((2 : Real) ^ (r + 1))
```

## 8.1 Block decomposition

```lean
lemma delta_block
    (q : Nat → Nat)
    (hsumm : ∀ n, Summable (fun r : Nat =>
      gap q (n + r) / ((2 : Real) ^ (r + 1))))
    (n J : Nat) :
    Delta q n =
      (∑ r in Finset.range J,
        gap q (n + r) / ((2 : Real) ^ (r + 1)))
      + Delta q (n + J) / ((2 : Real) ^ J) := by
  -- split the tsum at J and reindex the tail
  sorry
```

A recurrence corollary is:

```lean
lemma delta_succ
    (q : Nat → Nat)
    (hsumm : ∀ n, Summable (fun r : Nat =>
      gap q (n + r) / ((2 : Real) ^ (r + 1))))
    (n : Nat) :
    Delta q (n + 1) = 2 * Delta q n - gap q n := by
  sorry
```

## 8.2 Eventual denominator lattice

One robust way to avoid low-level rational normal-form details is to state the conclusion existentially:

```lean
lemma rational_delta_eventually_lattice
    (q : Nat → Nat)
    (hrec : ∀ n, Delta q (n + 1) = 2 * Delta q n - gap q n)
    (hgap_int : ∀ n, ∃ z : Int, gap q n = (z : Real))
    (hrat : ¬ Irrational (Delta q 0)) :
    ∃ (b N : Nat), 0 < b ∧ Odd b ∧
      ∀ n ≥ N, ∃ z : Int, (b : Real) * Delta q n = (z : Real) := by
  sorry
```

For the prime target, rationality of the original `tsum` is equivalent to rationality of `Delta q 0`, because

\[
\sum_{n\ge0}\frac{q_n}{2^n}=2(q_0+\Delta_0).
\]

## 8.3 Repeated-block quantization

```lean
lemma repeated_block_quantization
    (q : Nat → Nat) (b N n m J : Nat)
    (hbpos : 0 < b)
    (hlattice : ∀ t ≥ N, ∃ z : Int,
      (b : Real) * Delta q t = (z : Real))
    (hn : N ≤ n) (hm : N ≤ m)
    (hblock : ∀ r < J, gap q (n + r) = gap q (m + r)) :
    ∃ z : Int,
      (b : Real) * (Delta q (n + J) - Delta q (m + J))
        = ((2 : Real) ^ J) * (z : Real) := by
  sorry
```

A separation corollary can be stated as:

```lean
lemma repeated_block_eq_or_separated
    ... :
    Delta q (n + J) = Delta q (m + J) ∨
      ((2 : Real) ^ J) / b ≤
        |Delta q (n + J) - Delta q (m + J)| := by
  sorry
```

## 8.4 Fork–merge contradiction

```lean
lemma fork_merge_contradiction
    (q : Nat → Nat) (b N n m J K : Nat)
    (hbpos : 0 < b)
    (hlattice : ∀ t ≥ N, ∃ z : Int,
      (b : Real) * Delta q t = (z : Real))
    (hn : N ≤ n) (hm : N ≤ m)
    (hprefix : ∀ r < J, gap q (n + r) = gap q (m + r))
    (hfork : gap q (n + J) ≠ gap q (m + J))
    (hgap_int : ∀ t, ∃ z : Int, gap q t = (z : Real))
    (hsuffix : ∀ r < K,
      gap q (n + J + 1 + r) = gap q (m + J + 1 + r))
    (hsmall_prefix :
      |Delta q (n + J) - Delta q (m + J)|
        < ((2 : Real) ^ J) / b)
    (hsmall_suffix :
      |Delta q (n + J + K + 1) - Delta q (m + J + K + 1)|
        < (2 : Real) ^ K) :
    False := by
  sorry
```

The intended final reduction has the form:

```lean
theorem erdos_251_of_small_tail_fork_merge
    (hFM : SmallTailForkMerge (fun n => Nat.nth Nat.Prime n)) :
    Irrational
      (∑' n : Nat,
        (Nat.nth Nat.Prime n : Real) / ((2 : Real) ^ n)) := by
  -- assume rationality, obtain the eventual odd-denominator lattice,
  -- choose a sufficiently far fork–merge configuration, and apply
  -- `fork_merge_contradiction`.
  sorry
```

Here `SmallTailForkMerge` should encode exactly conditions (5.1)–(5.3), (6.1), and (6.2).

---

# 9. Where I am stuck

The exact missing ingredient is a theorem about the **actual prime-gap word** that violates the rationality-induced quantization in **C3**.

The cleanest sufficient target produced here is one of the following:

1. **Direct target:** prove infinitely many fork–merge configurations
   \(W_r a_r V_r\) and \(W_r a_r' V_r\), with \(a_r\ne a_r'\), for which the four terminal weighted tails satisfy
   \[
   H_r=o(2^{|W_r|})
   \quad\text{and}\quad
   H_r=o(2^{|V_r|}).
   \]

2. **Gap-only target:** prove an eventual bound
   \(g_t\le C(\log(t+2))^A\) together with fork–merge occurrences at height \(M_r\) satisfying
   \[
   |W_r|-A\log_2\log M_r\to\infty,
   \qquad
   |V_r|-A\log_2\log M_r\to\infty.
   \]

3. **Alternative target:** find any other prime-specific mechanism forcing two equal length-\(J\) gap blocks to have distinct terminal tails lying closer than \(2^J/b\) for every fixed odd \(b\).

I do not prove any of these prime-specific recurrence or tail-control statements. Their current literature status is **UNVERIFIED** here. The countermodel in §7 shows why a theorem asserting only long equal-gap runs, even with logarithmic tail scale and favorable placement, is still insufficient: exact tail locking can make every squeeze identity vanish.

---

# 10. Final assessment

The irrationality question remains open in this writeup. The rigorous progress is the repeated-block quantization theorem **C3**, the fork–merge obstruction **C4**, the exact conditional irrationality criteria **C5–C6**, and the countermodel **C8** showing that the non-degeneracy issue is mathematically essential rather than a technical nuisance.
