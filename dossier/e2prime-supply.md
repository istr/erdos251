# (E2') supply -- item-0017 working dossier (v0 DRAFT, Session A)

Date: 2026-07-18. Author: steering (Claude Fable 5), item-0017 executed
against kickoff v1 (operator-ratified, ephemeral, never committed).
Pin: 96dc30c, re-pinned to 66adc54 at session A start by operator
ratification after a STOP-AND-REPORT (anchor roadmap/item-0010.md
changed by the append-only M1+M2 landing note, the event anticipated by
the kickoff's faithfulness watch; all other anchors byte-identical; all
14 literature hashes verified, the three formerly unbooked lines now
committed at 7ca2388 verbatim). STATUS: DRAFT under construction;
Section 1 verdict PENDING until D1-D5 close. Mandate
(roadmap/item-0017.md @ 66adc54): produce unconditionally two
tail-typical indices with matched J-prefix and K-suffix windows and a
dominant weighted middle difference ((E2'), dossier/tate-transfer.md
O4) at depths J,K ~ log2 log x -- or prove a precise obstruction
extending the O4 blocker register.

Discipline: B1 obstruction-language from sentence one (located
obstruction, never impossibility; scope qualifiers inline). Checklist
rules i-iv of the triage-1b register. Findings F17.n, UNVERIFIED
register U17.n (Sections 9/8), never emptied silently. Read-only
anchors: dossier/chain-v1.md (Lemmas 2.1-2.5), dossier/tate-transfer.md
(O4, A3), payloads/item-0005-adjudication-v1.md (B1/B2, F1). No edits
under lean/ this window; no edits to chain-v1.md or tate-transfer.md.

## 1. Verdict

PENDING. Gate state (D2 Cramer-model gate): NOT YET RUN -- D1 is
untrusted and unexecuted until D2/M1+M2 are written and checked
(kickoff gate rule), and D5.c (empirical landing of the D1 balance
terms) runs before the D1.a route is trusted.

## 2. D0 -- statement layer

All definitions here are FIXED and used verbatim by every later
section. Paper-side notation follows chain-v1: p_1 = 2 < p_2 = 3 < ...,
g_n = p_{n+1} - p_n, S = sum_{n>=1} p_n 2^{-n},
delta_n = sum_{j>=1} g_{n+j} 2^{-j}, delta_{n+1} = 2 delta_n - g_{n+1}.
Anchors consumed read-only: chain-v1 Lemma 2.1 (convergence;
p_n <= C_0 n ln(n+2), Chebyshev; delta_n >= 2 for n >= 1 --
"two_le_delta"), Lemma 2.2 (block identity), Lemma 2.3 (lattice and
parity), Lemma 2.4 (quantization), Lemma 2.5 (small lattice element is
0). Gaps g_k are even for k >= 2; g_1 = 1.

### 2.1 Site filter, word map, projections

DEFINITION D0.1 (word map). For integers J, K >= 1 and M >= 1, set
L = J + M + K. The (length-L) gap word at index n is
    w(n) = (g_{n+1}, ..., g_{n+L}).
The side projection forgets the M middle entries:
    pi_M(w) = ((w_1,...,w_J), (w_{J+M+1},...,w_{J+M+K}))
            = (prefix_J, suffix_K),
and the middle block is mid(w) = (w_{J+1}, ..., w_{J+M}). The item's
default is M = 1 (the O4 normal-form width); every statement carrying
general M says so explicitly. pi with no subscript means pi_1.

DEFINITION D0.2 (site filter; kickoff-verbatim, selection order
A3(a)/(b): filters FIRST, counting SECOND). For x >= 3 and integer
parameters A >= 1, D >= 3:
    S_x(A, D) = { n >= 1 : p_n <= x,
                  g_{n+i} <= A ln x for 1 <= i <= L,
                  delta_{n+J} <= D,
                  delta_{n+L} <= 2^K }.
(The far-cap index n+L equals the O4 index n+J+K+1 at M = 1; for
general M the far cap sits at n+L with L = J+M+K, the direct (E2')
offset.) For a depth threshold s >= 0 write
S_x^{(s)}(A,D) = S_x(A,D) cap {n : n >= s+1}. Under the standard
parameter choice of P3 below, 2^K >= D, so the far cap is implied by
delta_{n+L} <= D; the filter is stated with 2^K to stay verbatim with
O4's (E4).

The selection ORDER is part of the definition: the filter events are
Chebyshev/Markov-cheap (P3) and are imposed BEFORE any counting or
collision argument runs; no construction is permitted to demand tail
bounds at sites it first constructed by sieving (that order triggers
the Cramer-type requirement, tate-transfer A3(b)).

DEFINITION D0.3 (realized sets and pair counts). For a finite index set
T with word map w and projection pi_M:
    W_L(T) = w(T),   P(T) = pi_M(w(T)),
    N_v(T) = #{ n in T : w(n) = v },
    C_words(T) = sum_v N_v(T)^2
               = #{ (n,n') in T^2 : w(n) = w(n') },
    C_sides(T) = sum_{(a,c)} ( sum_{mid m} N_{(a,m,c)}(T) )^2
               = #{ (n,n') in T^2 : pi_M(w(n)) = pi_M(w(n')) }.
Both counts are over ORDERED pairs and include the diagonal (which
cancels in the difference). Default T = S_x^{(s)}(A,D).

### 2.2 Targets

DEFINITION D0.4 (SUP'_b, (E2')-supply at odd modulus b >= 1;
kickoff-verbatim). SUP'_b: for every s >= 0 there exist x and indices
t, u in S_x^{(s)}(A, D) (parameters per the P3 map Par(b,x)) with
pi_M-matched words, w(t) != w(u) on the middle block, and
    (E2')  | sum_{1<=i<=L} (g_{t+i} - g_{u+i}) 2^{-i} |
           >  2^{-L} | delta_{t+L} - delta_{u+L} |,
with (E5) b(D-2) < 2^{J+1} honored by the parameter choice
J = ceil(log2(b D)), K = ceil(log2 D). SUP'_1 is the b = 1 case
feeding item-0010.

DEFINITION D0.5 (SUP_b^norm, normal form, M = 1). As D0.4 with M = 1
and the (E2') clause replaced by the bare collision clause
w(t) != w(u) (equivalently g_{t+J+1} != g_{u+J+1}). By P2 below,
SUP_b^norm implies the (E2') clause outright on the filtered sites, so
SUP_b^norm => SUP'_b; the converse direction is open (a general-M
supply with vanishing-middle-weight pairs excluded is what SUP'_b
asks; see P2's E-invariant).

THEOREM D0.6 (consumption; EXCH' instantiation, proof re-executed this
session from the read-only anchors). Let b >= 1 odd, and suppose
S = a/(2^s b) with a integer, s >= 1 (WLOG per Lemma 2.3). Let
t, u >= s+1 be indices with (i) pi_M-matched words (prefix J, suffix
K), (ii) delta_{t+J}, delta_{u+J} <= D and delta_{t+L},
delta_{u+L} <= 2^K, (iii) b(D-2) < 2^{J+1}, and (iv) the (E2')
inequality of D0.4. Then contradiction; hence SUP'_b for all odd b
implies S irrational, and SUP'_1 implies S not in Z[1/2].
Proof. Lemma 2.3 puts b delta_n in 2Z for n >= s+1. Lemma 2.4 on the
shared J-prefix puts b(delta_{t+J} - delta_{u+J}) in 2^{J+1} Z. By
(ii) and two_le_delta, |delta_{t+J} - delta_{u+J}| <= D - 2, so by
(iii) the lattice element has absolute value < 2^{J+1}, hence is 0
(Lemma 2.5): delta_{t+J} = delta_{u+J}. Subtracting Lemma 2.2 at t and
u with T = J (prefix sums cancel) gives delta_t - delta_u
= 2^{-J}(delta_{t+J} - delta_{u+J}) = 0. Subtracting Lemma 2.2 at t
and u with T = L now gives
    0 = sum_{1<=i<=L} (g_{t+i} - g_{u+i}) 2^{-i}
        + 2^{-L} (delta_{t+L} - delta_{u+L}),
and (iv) makes the right side nonzero (strict triangle inequality).
Contradiction. For the consequences: given S = a/(2^s b), apply SUP'_b
at threshold s to get such a pair with t, u >= s+1. QED

### 2.3 P1 (pigeonhole form; anti-concentration as a counting identity)

LEMMA P1. Let T be a finite index set, w its word map, pi = pi_M.
(a) C_sides(T) - C_words(T)
    = #{ (n,n') in T^2 : pi(w(n)) = pi(w(n')), w(n) != w(u') } >= 0
    (n' for u'; ordered pairs, diagonal cancels). In particular
    C_sides > C_words iff T carries a pi-collision pair with
    differing middles.
(b) Rigidity iff equality: C_sides(T) = C_words(T) iff on T the word
    is determined by its side pair ("sandwich rigidity" on T).
(c) Cardinality form: |W_L(T)| > |P(T)| implies a pi-collision pair
    with differing middles exists in T.
(d) Cauchy-Schwarz floor: C_sides(T) >= |T|^2 / |P(T)|.
Proof. (a) The pi-matched ordered pairs split into word-equal and
word-different; the first class is counted by C_words since word-equal
implies pi-matched. (b) is (a) with the difference set empty. (c) The
restriction of pi to the realized set W_L(T) is non-injective, so two
realized words share sides; any two preimage sites form the pair.
(d) Cauchy-Schwarz on the fibers of the map n -> pi(w(n)):
sum_P M_P^2 >= (sum_P M_P)^2 / #{realized P} = |T|^2/|P(T)|. QED

Remark P1.R (what P1 does NOT give). P1 converts supply into the
POSITIVITY C_sides - C_words > 0 on the filtered sites; it is exactly
the O4 blocker "pigeonhole variability-blindness" that no cardinality
or first-moment count so far forces this positivity: C_words is not
bounded by anything unconditional at the needed word lengths except
sieve upper bounds carrying the constant that D1 interrogates. P1 is
bookkeeping, not progress; it fixes the battleground.

### 2.4 P2 (weighted-clause bridge)

LEMMA P2. Let J, K, M >= 1, L = J + M + K, and let t, u >= 1 be
indices with pi_M-matched words. Write d_j = g_{t+J+j} - g_{u+J+j}
(1 <= j <= M) for the middle differences and set the weighted middle
invariant
    E(t,u) = sum_{1<=j<=M} d_j 2^{M-j}   (an integer).
Assume the far caps delta_{t+L} <= 2^K and delta_{u+L} <= 2^K. If
E(t,u) != 0, then the (E2') inequality of D0.4 holds at (t,u); in
fact, with two_le_delta,
    | sum_{1<=i<=L} (g_{t+i} - g_{u+i}) 2^{-i} |
        = |E| 2^{-(J+M)} >= 2^{-(J+M)}
    > 2^{-(J+M)} (1 - 2^{1-K})
        >= 2^{-L} |delta_{t+L} - delta_{u+L}|.
If moreover min(t,u) >= 1 so that all middle indices t+J+j, u+J+j are
>= 2, all d_j are even, E is even, and the left side is
>= 2^{1-(J+M)}: the inequality holds with a factor-2 margin.
Proof. The prefix and suffix terms of the weighted sum cancel
(pi-match), leaving sum_j d_j 2^{-(J+j)} = 2^{-(J+M)} E. E is a
nonzero integer, so |E| >= 1. For the right side, two_le_delta and the
far caps give |delta_{t+L} - delta_{u+L}| <= 2^K - 2, and
2^{-L}(2^K - 2) = 2^{-(J+M)}(1 - 2^{1-K}) < 2^{-(J+M)}. Parity: for
index k >= 2, g_k is a difference of odd primes, hence even. QED

COROLLARY P2.1 (M = 1). On far-capped sites, EVERY pi_1-collision with
differing middles satisfies (E2') with a factor-2 margin: at M = 1,
E = d_1 != 0 is the collision clause itself. Hence SUP_b^norm =>
SUP'_b, and the P1 positivity C_sides - C_words > 0 on
S_x^{(s)}(A,D), for a single x per threshold s, already supplies
SUP'_b in its normal form.

REMARK P2.2 (the general-M sufficient condition is E != 0, and it is
strictly needed). For M >= 2 a pi_M-collision can have differing
middles yet E = 0, and then the (E2') left side is exactly 0: the
standard example is middle blocks (2,8) vs (4,4) at M = 2
(d = (-2,+4), E = 2(-2) + 1(+4) = 0). Multi-difference supply
arguments must therefore track the dyadic-weighted invariant E, not
mere tuple distinctness. This is the precise content of the O4 phrase
"sufficiently weighted"; it is recorded once here and consumed by
D1/D4.

REMARK P2.3 (which clauses need which caps). (E2') consumes ONLY the
far caps (and two_le_delta); the near caps delta_{.+J} <= D and the
gate (E5) are consumed by the delta-pin in Theorem D0.6. The site
filter D0.2 carries both so that a collision pair on filtered sites is
a complete EXCH' configuration with no further conditions.

### 2.5 P3 (depth accounting; the exact constants, recorded once)

Standing constants: C_0 is chain-v1 Lemma 2.1's Chebyshev constant
(p_n <= C_0 n ln(n+2) for all n >= 1, C_0 >= 1 absolute). All numbered
constants below are explicit functions of C_0 alone. N := pi(x), so
{n : p_n <= x} = {1, ..., N}, and ln N <= ln p_N = ln x.

LEMMA P3.1 (mean gap window; Markov). For 1 <= i <= L and N >= L+16:
    sum_{n<=N} g_{n+i} <= 2.4 C_0 N ln N,
    #{ n <= N : g_{n+i} > A ln x } <= 2.4 C_0 N / A.
Proof. sum_{n<=N} g_{n+i} = p_{N+i+1} - p_{i+1} <= C_0 (N+L+1)
ln(N+L+3). For N >= max(L+16, 32): N+L+1 <= 2N, and
ln(N+L+3) <= ln(2N) = ln N + ln 2 <= 1.2 ln N since
ln 2 <= 0.2 ln N iff N >= 2^5 = 32. So the sum is
<= 2.4 C_0 N ln N; Markov at threshold A ln x >= A ln N. (The
lemma's N >= L+16 is read with this absolute floor N >= 32
throughout; P3.3's x_1(b) absorbs it.) QED

LEMMA P3.2 (mean tail; Markov). For 0 <= r <= L and N >= L + 16:
    sum_{n<=N} delta_{n+r} <= 13 C_0 N ln N,
hence with D >= 13 C_0 A ln x:
    #{ n <= N : delta_{n+r} > D } <= N / A.
Proof. sum_{n<=N} delta_{n+r} <= sum_{n<=N'} delta_n with
N' = N + L. Writing delta_n = sum_{j>=1} g_{n+j} 2^{-j} and swapping
sums, each g_m (m >= 2) receives weight
c_m = sum_{d=max(1, m-N')}^{m-1} 2^{-d} < min(1, 2^{N'-m+1}).
The m <= N'+1 block contributes < p_{N'+2} <= C_0 (N'+2) ln(N'+4).
The m > N'+1 block contributes < sum_{j>=1} g_{N'+1+j} 2^{-j}
= delta_{N'+1} <= C_0 sum_{j>=1} (N'+j+2) ln(N'+j+4) 2^{-j}
<= C_0 (N'+2) ln(N'+4) sum_{j>=1} (j+1)(1 + ln(j+1)) 2^{-j}
<= 11 C_0 (N'+2) ln(N'+4),
using (N'+j+2) <= (N'+2)(j+1), ln(N'+j+4) <= ln(N'+4)(1 + ln(j+1))
for N' >= 3, and sum_{j>=1} (j+1)^2 2^{-j} = 11 as the majorant.
Total < 12 C_0 (N'+2) ln(N'+4) <= 13 C_0 N ln N for N >= L+16.
Markov at threshold D >= 13 C_0 A ln x >= 13 C_0 A ln N. QED
[Constants deliberately loose; only explicitness is load-bearing.
D5.c measures the true empirical means (~ ln x for both), so every
downstream consumer uses the SYMBOLIC forms with these named
constants, replaceable wholesale.]

LEMMA P3.3 (standard parameter choice Par(b,x) and site abundance).
Let b >= 1 be odd and fixed. Define, for x >= x_1(b):
    A = A(x)   = ceil(32 C_0 log2 ln x),
    D = D(x,A) = ceil(13 C_0 A ln x),
    J = ceil(log2(b D)),  K = ceil(log2 D),  L = J + 1 + K  (M = 1).
Then for x >= x_1(b) (an explicit threshold from the display below):
(i)   (E5) holds with room: b(D-2) < b D <= 2^J <= 2^{J+1}/2.
(ii)  2^K >= D, so the far cap in D0.2 is implied by
      delta_{n+L} <= D.
(iii) A >= 8 C_0 L, hence by P3.1/P3.2 (union over the L gap filters
      and the two delta filters, run at threshold D >= 13 C_0 A ln x):
      |S_x(A,D)| >= N - 2.4 C_0 L N/A - 2 N/A >= N/2,
      and |S_x^{(s)}(A,D)| >= N/2 - s.
(iv)  Depth: L = 2 log2 ln x + 2 log2 log2 ln x + log2 b + O(1),
      with the envelope 2 log2 ln x <= L <= 4 log2 ln x for
      x >= x_1(b). DEVIATION NOTE vs kickoff P3 ("L(b,x) ~
      2 log2 log2 x + O_b(1)"): the second-order term is
      2 log2 log2 ln x, which is unbounded, not O_b(1); the kickoff's
      "~" clause is correct, its "+O_b(1)" is not exact. Cause: the
      per-position gap filter over L positions forces A to grow like
      L (density loss L/A per P3.1), and A feeds back into D, J, K
      through log2 A. Harmless for every consumer in this dossier
      (all use only L = (2+o(1)) log2 ln x and L = o(ln x / lnln x));
      recorded per checklist rule iii instead of silently absorbed.
(v)   Capacity: side entries are even integers in [2, A ln x], so
      |P(S_x(A,D))| <= (A ln x / 2)^{J+K} = x^{o(1)}, and
      |W_L(S_x(A,D))| <= (A ln x / 2)^L = x^{o(1)}. Explicitly,
      (A ln x/2)^{J+K} = exp( (J+K)(lnln x + ln(A/2)) )
      <= exp( 5 (lnln x)^2 ) for x >= x_1(b).
Proof. (i) 2^J >= b D by J's definition. (ii) 2^K >= D by K's.
(iii) L <= log2 b + 2 log2 D + 3 and log2 D <= log2(13 C_0) + log2 A
+ log2 ln x + 1, so L <= 2 log2 ln x + 2 log2 A + log2 b
+ 2 log2(13 C_0) + 5 <= 4 log2 ln x for x >= x_1(b) (absorbing the
b- and C_0-terms and 2 log2 A <= 2 log2(33 C_0 log2 ln x) into
2 log2 ln x of slack); then A = ceil(32 C_0 log2 ln x)
>= 8 C_0 * 4 log2 ln x >= 8 C_0 L, and the union bound is
(2.4 C_0 L + 2) N/A <= (2.4/8 + 2/(8 C_0 L)) N <= N/2. (iv) J and K
are each log2 ln x + log2 log2 ln x + O(1) (+ log2 b for J) by
substituting A into D. (v) Count even values <= A ln x per side
coordinate; (J+K) <= 2 log2 ln x + 2 log2 log2 ln x + O_b(1) and
lnln x + ln(A/2) <= (1 + o(1)) lnln x give the display for x large;
5 is a safe absolute envelope for x >= x_1(b). QED

REMARK P3.4 (thresholds). x_1(b) is effective and monotone in b; no
attempt to optimize it is made anywhere in this item (the mandate is
asymptotic). Every later section states its own x-threshold as
x >= x_i(b) with x_i absorbing x_1.

### 2.6 Faithfulness watch: D0 vs the landed Lean ExchangeSupply1

Executed this session against lean/Erdos251/Exchange.lean @ 66adc54
(read-only). The landed statement layer is:
ExchangeAt n m J K D (clauses 1<=J, 1<=K, (E1) SameBlock n m J, (E2)
gap(n+J) != gap(m+J), (E3) SameBlock (n+J+1) (m+J+1) K, (E4) near caps
delta(.+J) <= D and far caps delta(.+J+1+K) <= 2^K), and
ExchangeSupply1 : forall t, exists n m J K D, t <= n and t <= m and
ExchangeAt n m J K D and (D - 2 < 2^{J+1}). Index conventions: Lean
gap k = paper g_{k+1}, Lean delta k = paper delta_k; the far-cap index
n+J+1+K is the paper n+L. Divergence register (FLAGGED, not absorbed,
in either direction):

FW-1 (substantive, direction: Lean stricter). ExchangeSupply1 demands
the M = 1 normal form (single differing gap); the mandate's general
(E2') clause (any M with E != 0, P2) does NOT literally instantiate
ExchangeAt. Consequence, binding for this item: only SUP_1^norm
(D0.5) feeds the landed Prop verbatim; a general-(E2') supply theorem
would additionally need either a Lean-side generalization of
ExchangeAt (out of scope this window: no lean/ edits) or a
normal-form post-processing step (extract a Hamming-1 pair), which is
NOT automatic. All supply attempts in this item therefore state which
of SUP_1^norm / SUP'_1 they produce.

FW-2 (direction: Lean weaker; no conflict). ExchangeSupply1
quantifies J, K, D existentially per threshold with NO depth scaling;
the mandate fixes J, K ~ log2 log x via Par(b,x). Paper supply at the
mandated depths instantiates the Lean existential a fortiori.

FW-3 (bookkeeping). Lean's threshold semantics (t <= n, m with the
s-uniformization t = s+2 for the b = 1 even lattice,
dyadic_delta_even_lattice) vs the paper's t, u >= s+1 (Lemma 2.3, odd
b): the forall-threshold form absorbs the offset; no divergence in
strength. Paper Theorem D0.6 keeps s+1 (general odd b); the b = 1
consumer needs s+2 -- SUP'_b's "for every s" covers both.

FW-4 (proof-level only). Lean's exchange_contradiction derives
|d| >= 1 from bare distinctness of naturals (no parity); the paper
normal form has |d_1| >= 2 by evenness (P2). No statement divergence;
the paper's factor-2 margin is extra room, not a requirement.

FINDING F17.1 (from FW-1, consequential): the landed consumption
interface is strictly normal-form. Item-0017's supply target set is
therefore ordered: SUP_1^norm (feeds Lean verbatim) > SUP'_1 (paper
EXCH', Theorem D0.6) > SUP'_b all odd b (full irrationality); the
mandate's acceptance clause "feeding EXCH'_b (EXCH'_1 suffices for
item-0010)" is met by any of the three, but only the first closes the
Lean gap without further statement-layer work.

## 3. D2 -- Cramer-model gate (M1 drafted Session A; M2 Session B)

[Draft in Session A; the gate decision is recorded ONLY after M1+M2
are complete and checked (Session B). Model-language discipline: every
statement in this section is about the MODEL; no claim about the
primes is made or implied. Frame citations (heuristic status, per
kickoff): Lau 2604.15042 Section 7 format; Gallagher / Granville-
Lumley 2009.05000 as the heuristic frame; the model definition below
is verbatim GL p. 19 (anchors resolved, U17.4).]

### 3.1 The model

MODEL M (Bernoulli/Cramer). Fix x >= 16 and work on the integer
interval (x/2, x]. Let (X_n)_{n > 2} be independent Bernoulli with
P(X_n = 1) = 1/ln n. Model "primes" are {n : X_n = 1} in increasing
order q_1 < q_2 < ...; model gaps h_i = q_{i+1} - q_i; model tails
delta^M_i = sum_{j>=1} h_{i+j} 2^{-j}; model words, side projections,
site filters S^M_x(A,D), pair counts C^M_sides, C^M_words: verbatim
D0.1-D0.3 read over the model sequence. Parameters: Par(1,x) of P3.3
verbatim (same A, D, J, K, L as the b = 1 primes case). No parity:
model gaps may be odd; the E-invariant of P2 loses its factor-2
margin, nothing else (P2's |E| >= 1 case). [The parity-corrected
model variant is NOT needed for M1/M2; recorded as an M2 sensitivity
check, Session B.]

### 3.2 M1 (statement, drafted; proof skeleton; full check Session B)

CLAIM M1 (model supply, a.s. along dyadic scales). In Model M, with
x_r = 2^r: almost surely, for all large r, the filtered site set
S^M_{x_r}(A,D) contains at least x_r^{1-o(1)} DISJOINT pi_1-matched
pairs with differing middles and, a fortiori (P2 with |E| >= 1),
(E2')-pairs; consequently the model analogue of SUP'_1 holds a.s.
with x^{1-o(1)} qualifying disjoint pairs per dyadic scale, and the
ORDERED-pair count is x_r^{2-o(1)}. [Kickoff's "x^{1-o(1)} qualifying
pairs" is hereby read as the disjoint-pair count; the ordered count
is x^{2-o(1)}. Interpretation fixed here once; not a deviation, a
precision.]

Proof skeleton (quantities to be fully checked in Session B):
(a) Site abundance. E|S^M_x| >= c x/ln x after the filters (the model
    Markov bounds mirror P3.1/P3.2 with means <= 2 ln x on (x/2,x];
    Chernoff concentration for the Bernoulli sums). [Check: model
    tail delta^M has the same 2^{-j}-weighted mean ~ ln x.]
(b) Side-collision probability. For two disjoint model sites, the
    probability that their (J+K) side gaps agree entrywise and stay
    under the cap is ((1+o(1))/(2 ln x))^{J+K} in the capped-geometric
    computation: P(two independent near-Geometric(1/ln x) gaps agree)
    = (1+o(1))/(2 ln x). Hence
    E[C^M_sides - diag] = |S^M|^2 ((1+o(1))/(2 ln x))^{J+K}
    = x^{2-o(1)}   [(2 ln x)^{J+K} = exp((2/ln 2 + o(1))(lnln x)^2)
    = x^{o(1)} at Par(1,x) depths].
(c) Middle anti-concentration. Conditional on a side match, the two
    middles agree with probability (1+o(1))/(2 ln x) = o(1): the
    model's sandwich-rigidity probability per matched-flank pair
    vanishes. E[# pi-matched pairs with differing middles]
    = (1 - O(1/ln x)) E[C^M_sides - diag] = x^{2-o(1)}.
(d) Concentration + Borel-Cantelli. Var of the pair count is
    dominated by overlapping-pair covariances; second-moment/Chebyshev
    at each dyadic scale, then sum over r (Lau Lemma 7.1 pattern:
    Borel-Cantelli in the Bernoulli model). Disjointification: a
    greedy matching in the collision graph keeps >= (pairs)/(2 max
    site degree); degree bounds from the same second-moment tables.
    [The greedy-matching floor and the covariance table are the two
    Session B verification obligations; everything else is standard.]

### 3.3 M2 (balance in the model; Session B)

TO RUN (Session B, before any D1 trust): compute E[C^M_sides],
E[C^M_words] and their concentration at Par(1,x); expected outcome per
kickoff is that the model balance closes with room because the model
per-word constant is 1+o(1); the exact room exponent is TO BE
DERIVED, and any deviation from the kickoff's "(log x)^{2-o(1)}"
expectation is a finding, not an error (the model's own margin
computation supersedes the kickoff's orientation heuristic). D5.c
calibrates both against the primes empirically. GATE RULE (binding):
if M2 does not close, D1 is architecturally dead and is not attempted
unconditionally; the M2 failure mode becomes the obstruction
statement.

## 4. D1 -- the second-moment balance (GATED on D2; not started)

Gate state: BLOCKED until Section 3 completes (kickoff gate order;
also D5.c empirical landing before route trust). Target recorded for
fidelity: prove C_sides - C_words > 0 on S_x^{(s)}(A,D) via
C_sides >= |S|^2/|P| (P1(d), P3.3(v)) against per-word Selberg upper
bounds; ladder D1.a (max-S, self-proved Selberg constant; qualitative
form citable secondhand via Pintz 1305.6289 Lemma 3 ONLY), D1.b
(first-moment averaging via Kuperberg 2210.09775 Thm 1.2, regime gap
vs Thm 1.1 stated explicitly), D1.c (S second moment at growing k;
MoSo 0409258 assessment), D1.d (Merikoski Chen-substitution constant
at the critical spot).

## 5. D3 -- tool cartography (not started; extraction anatomies in
## flight)

## 6. D4 -- blocker hardening at the weighted clause (not started)

## 7. D5 -- certificate layer extension (D5.c STARTED Session A; seed
## scripts exch_scan.py, exch_cert.py, exch_growth.py,
## pc_wordcount2.py at dossier/item-0005-workpapers/stress/)

D5.c script: item-0017-workpapers/stress/balance_stats.py (committed
with this dossier), measuring on S_x(A,D) per D0.2/D0.3: |S_x|,
|W_L|, |P|, C_words, C_sides, the P1 pair count C_sides - C_words,
exchange class counts, singular-series site moments (D1.c), and the
per-word ratio lambda_w = N_w (ln x)^{L+1}/(S(H_w) x) (D1.a), on the
seed grid (J,K,D0) in {(4,5,30),(5,5,34),(6,6,64),(7,7,67),(8,8,67)}
with gap-cap variants A in {none, 8, 4}. Validation at x = 2e6:
exchange-class counts REPRODUCE the committed record (12 at (4,5,30),
2 at (5,5,34); tate-transfer Section 4). First calibration data
(x = 2e6, to be re-measured at 2e7/1e8):
(a) the naive independent-model side-collision rate underestimates
    the empirical off-diagonal C_sides by ~3.4x PER POSITION
    (empirical per-position gap-collision probability ~ 0.116 vs
    model 1/(2 ln x) ~ 0.034): parity (factor ~2) plus
    singular-series clumping. M2's model M must carry this
    correction before its numbers are compared to the primes
    (D5.c's calibration role, kickoff).
(b) singular-series site moments are tame: S2nd/(S1st)^2 in
    [1.32, 1.51] across the grid at 2e6 -- empirical support that
    S-averaging (D1.b/c) is not where the balance dies.
(c) lambda_w means are >> 1 at all reachable x (sub-1-mass corner:
    realized words have N_w >= 1 while HL mass << 1) -- the
    D1.a-relevant regime is not directly observable at x <= 1e8;
    D5.c calibrates SHAPES, not the asymptotic constant.
Container probe (rule 9, once): 96 GB total / ~88 GB free; 1e8 runs
in-core; 1e9 feasible only with a segmented sieve (recorded as D5.a
candidate, decision deferred).

NOTE (seed-script census vs kickoff): the kickoff lists
pc_wordcount.py among the committed seed scripts; the committed tree
at 66adc54 carries only pc_wordcount2.py (plus the three exch_*.py).
git log finds no pc_wordcount.py at any commit. Recorded as U17.5;
if the v1 script is needed it must be reconstructed from
pc_wordcount2.py, not assumed.

## 8. UNVERIFIED register (U17.n; populated as items arise, never
## emptied silently)

U17.1 Secondary-source claims pending primary location: (a) the
      "9 -> 5/4 blocks" reduction attributed to the Pintz
      1510.04577 / Merikoski line; (b) Merikoski syndeticity.
      RESOLVED Session A against the primary texts:
      (a) NOT FOUND as phrased -- the secondary phrase conflates two
      separate printed facts in Pintz 1510.04577: the k = 9 -> k = 5
      reduction is in VALUES beta_i, not blocks ("it is sufficient to
      work with k = 5 values of beta_i in (1.4) instead of k = 9
      values", Section 2 p. 2), and the measure constant improves
      T/8 -> T/4 ((1.5) vs (2.5)/Corollary 2 p. 3), plausibly garbled
      to "5/4"; the proof's actual block count is 4m+1 blocks with
      >= m+1 forced prime-containing ((3.5)-(3.6) p. 4). Anatomy:
      extract/pintz15-quarter.md Section 5.
      (b) VERIFIED VERBATIM -- Merikoski 1811.03008 Corollary 3
      (Section 1 p. 2: "L cap [T, T + C] != emptyset", C absolute
      ineffective) plus the explicit sentence "Corollary 3 can be
      rephrased as saying that the set of limit points L is
      syndetic"; the paper notes it "actually follows already from
      [2, Theorem 1.1]". Anatomy: extract/merikoski18-limitpoints.md
      Section 1-2.
U17.2 Kickoff steering heuristic (D1 display): classical per-word
      bound N_w <= C_sel(L) S(H_w) x/(log x)^{L+1} with
      C_sel(L) ~ 2^L L!, and the reduction of the balance to
      (log x)^2 > C_sel(L) * S-term * (A/2)^{J+K}. UNVERIFIED,
      orientation only; every constant re-derived in D1.a before use.
U17.3 Kuperberg regime claims (Thm 1.1 k = O((log h)^{1-delta});
      Thm 1.2 T_k(h) << h^k (3 log k)^k with no growth condition):
      pending extraction verification against the PDF.
      RESOLVED Session A with a CORRECTION to the kickoff phrasing:
      Thm 1.1 (p. 2, verbatim) is "Fix delta > 1/2, and let h,k in N
      with k = O((log h)^{1-delta}) ... T_k(h) = h^k + O(h^{k-beta})"
      -- the constraint delta > 1/2 is essential (Rankin-trick
      constraint (1-delta)(2+2alpha)+alpha < 1, p. 7), so the
      asymptotic regime is k below (log h)^{1/2}, NOT any
      (log h)^{1-delta}; the kickoff line omitted delta > 1/2.
      T_k(h) is the ORDERED distinct-tuple sum (eq (4), p. 2).
      Thm 1.2's growth-condition-free upper bound stands (exact
      display in extract/kuperberg22-singseries.md; re-verify at
      first D1.b use). CRT-method barrier at larger k stated p. 11
      verbatim. Anatomy: extract/kuperberg22-singseries.md.
U17.4 D2 frame citations (Lau Section 7 format; Gallagher;
      Granville-Lumley model definitions): exact anchors pending the
      Session A extraction anatomies. RESOLVED Session A: the model
      of Section 3.1 is verbatim Granville-Lumley 2009.05000 p. 19
      ("Consider an infinite sequence of independent random variables
      (X_n)_{n>=3} for which Prob(X_n = 1) = 1/log n ...",
      extract/gl20-heuristics.md Section 7, including the flaw
      discussion used for model-language discipline); the Lau
      Section 7 usage-pattern anchor stays tate-transfer.md Section 5
      (item-0005 extraction, unchanged this window).
U17.5 pc_wordcount.py absent from the committed tree (Section 7
      note); kickoff seed-script list is inexact on this point.
U17.6 Model M1 skeleton items (Section 3.2 (d)): covariance table and
      greedy-matching floor; Session B obligations.

## 9. Findings register (F17.n)

F17.1 (Section 2.6): the landed Lean consumption interface
      (ExchangeSupply1) is strictly normal-form (M = 1); the supply
      target set is ordered SUP_1^norm > SUP'_1 > SUP'_b, and only
      the first closes the Lean gap without further statement-layer
      work. [Faithfulness watch executed at 66adc54.]

## 10. Follow-up candidates (described only; never silently executed)

[none yet]

## 11. Review section

[Session D: R1 same-family fresh-role (computation audit) + R2
cross-family (scope audit), blind, anchor-stripped payload via a
committed deterministic strip script; web OFF; reviewer receives
exactly payload + object.]
