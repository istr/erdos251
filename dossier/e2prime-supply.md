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

PENDING. Gate state (D2 Cramer-model gate, Session B): M1 + M2
COMPLETE (Sections 3.2-3.3); GATE: PASS WITH AMENDMENTS (Section
3.4) -- the model balance closes (a.s. positivity along dyadic
scales, x^{2-o(1)} ordered / x^{1-o(1)} disjoint model pairs), so D1
is not architecturally dead and D1.a-d are unblocked, BINDINGLY
amended by F17.2 (room budget is (2 ln x)^M per middle position, not
(log x)^2) and F17.3 (D1 runs on the aggregate filter D0.2',
A' in (1, 4 sqrt(2)/e); the pinned per-position filter's floor route
is dead in the model by capacity slack alone). D5.c's empirical
landing ran first (Section 7), per the kickoff's order.

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

### 2.7 ADDENDUM (Session B, carried by finding F17.3): aggregate
### filter D0.2' and parameter map Par'(b,x)

D0.2 stays pinned and unchanged; the following VARIANT is added
because the M2 route audit (Section 3.3) shows the per-position
filter's capacity accounting kills the D1 floor route even in the
model, while the aggregate variant below repairs it.

DEFINITION D0.2' (aggregate site filter). For fixed A' > 1, fixed
A'' >= 1, and D = D''(x) := ceil(13 C_0 A'' ln x):
    S'_x(A', A'', D) = { n >= 1 : p_n <= x,
                         sum_{1<=i<=L} g_{n+i} <= A' L ln x,
                         delta_{n+J} <= D,  delta_{n+L} <= 2^K }.
Selection order unchanged (filters first, counting second).

LEMMA P3.1' (window-sum Markov at the PNT-sharp mean). By the prime
number theorem (classical, unconditional), sum_{n<=N} g_{n+i} =
p_{N+i+1} - p_{i+1} = (1+o(1)) N ln N, hence
    sum_{n<=N} sum_{1<=i<=L} g_{n+i} = (1+o(1)) L N ln N
and Markov at threshold A' L ln x (>= A' L ln N) removes density at
most (1+o(1))/A'. [PNT enters ONLY here and only to make fixed
A' < 4 sqrt(2)/e usable; with Chebyshev's C_0 the same lemma holds
with A' rescaled by C_0-dependent constants, which would break the
Section 3.3 threshold -- recorded, not absorbed. Classical citation
duty: PNT, Hadamard / de la Vallee Poussin 1896; no effective form
needed.]

LEMMA P3.3' (parameter map Par'(b,x) and properties). Fix
A' in (1, 4 sqrt(2)/e), A'' = 16. For x >= x_1'(b), with
D = ceil(13 C_0 A'' ln x), J = ceil(log2(b D)), K = ceil(log2 D),
L = J + 1 + K (M = 1):
(i)   (E5) with room, and 2^K >= D (far cap implied), as in P3.3.
(ii)  Site abundance: |S'_x| >= N (1 - (1+o(1))/A' - 2/A'') - o(N),
      a positive proportion of pi(x) for A' > 1 strict (P3.1' +
      P3.2 twice).
(iii) Depth: L = 2 log2 ln x + log2 b + 2 log2(13 C_0 A'') + O(1)
      = 2 log2 ln x + O_b(1): the kickoff's O_b(1) form HOLDS on
      this variant (the P3.3(iv) deviation was per-position-filter
      specific).
(iv)  Capacity (simplex count): side tuples are even positive
      integers with sum <= A' L ln x, so
      |P(S'_x)| <= C(floor(A' L ln x / 2), J+K)
                <= ((e A'/2)(L/(J+K)) ln x)^{J+K}
                 = ((e A'/2 + o(1)) ln x)^{J+K} = x^{o(1)}.
Proofs: (i) as P3.3; (ii) union of the three Markov filters;
(iii) direct substitution (A', A'' no longer feed J, K through a
growing A); (iv) stars-and-bars with even parts, C(m, r) <=
(e m/r)^r, and L/(J+K) = 1 + o(1). QED

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

### 3.2 M1 (model supply; COMPLETE, Session B)

Notation for this section: p := 1/ln x; over anchors in (x/2, x] the
per-integer hit probability is p(1+O(1/ln x)) and every per-position
collision constant below carries a factor (1+O(1/ln x)) whose
(J+K)-fold product is 1+o(1); these factors are written once here and
suppressed. Windows may extend beyond x; the process is defined on
(x/2, 2x] and site anchors are restricted to model primes in
(x/2, 3x/4], so all window positions stay in the p = (1+o(1))/ln x
range. N_S := |S^M_x| after the filters.

THEOREM M1 (model supply, a.s. along dyadic scales). In Model M with
Par(1,x) and x_r = 2^r: almost surely, for all large r, the filtered
site set S^M_{x_r}(A,D) contains
(i)  at least x_r^{2-o(1)} ordered pi_1-matched pairs with differing
     middles -- all of them (E2')-pairs by P2 (|E| >= 1; no parity in
     the model), and
(ii) a DISJOINT family of at least x_r^{1-o(1)} such pairs; the
     explicit disjoint floor is N_S/(8 (2-p)^{J+K})
     = N_S (ln x_r)^{-2+o(1)}.
Consequently the model analogue of SUP'_1 holds a.s. with x^{1-o(1)}
qualifying disjoint pairs per dyadic scale. [Kickoff's "x^{1-o(1)}
qualifying pairs" is the disjoint-pair count; the ordered count is
x^{2-o(1)}. Interpretation fixed once; a precision, not a deviation.]

Proof.
(a) Site abundance. #model primes in (x/2, 3x/4] concentrates at
    mu := sum_{x/2 < n <= 3x/4} 1/ln n = (1+o(1)) x/(4 ln x)
    (Chernoff for independent Bernoulli sums: deviation
    P(|S - mu| > mu/2) <= 2 exp(-mu/10)). Filters: a model gap
    exceeds A ln x with probability <= (1-p)^{A ln x} <= e^{-A} =
    (ln x)^{-32 C_0/ln 2} (union over L positions: o(1) density);
    the model tails delta^M have mean E[delta^M] = E[h](1+o(1)) =
    (1+o(1)) ln x (the 2^{-j}-weights sum to 1), so Markov at
    D = ceil(13 C_0 A ln x) and at 2^K >= D removes density o(1).
    Hence a.s. eventually N_S >= x/(8 ln x) =: N_1 at every dyadic
    scale (Chernoff + Borel-Cantelli; filter events are functions of
    disjoint gap blocks, so the filtered count is a Lipschitz
    function of independent blocks and McDiarmid applies; crude
    bounds suffice at the stated density).
(b) Per-position collision. Two gaps at disjoint sites are
    independent near-Geometric(p): q_2 := P(h = h') =
    sum_t (p(1-p)^{t-1})^2 = p/(2-p) = (1+o(1))/(2 ln x). Similarly
    q_3 := P(h = h' = h'') = p^2/(3 - 3p + p^2) = (1+o(1)) p^2/3,
    and max_t P(h = t) = p.
(c) Ordered pair count. For disjoint sites (index distance > L+2),
    side-match probability is q_2^{J+K}; conditional on the side
    match, the two middles differ with probability 1 - q_2 =
    1 - O(1/ln x); the four cap events change all displayed
    probabilities by 1+o(1) factors (their failure probabilities are
    o(1) even conditionally on any window values under the cap, since
    tails are dominated by the geometric mass beyond the window).
    With T := #ordered disjoint qualifying pairs:
    E[T] = (1+o(1)) N_S^2 q_2^{J+K}, and
    (2 ln x)^{J+K} = exp((2/ln 2 + o(1)) (lnln x)^2) = x^{o(1)}
    at Par(1,x) depths, so E[T] = x^{2-o(1)}.
(d) Concentration. Var(T) decomposes over pairs of ordered pairs by
    window overlap: (identical or swapped) <= 2 E[T]; (one shared
    site) <= 4 N_S^3 q_3^{J+K} with
    q_3^{J+K}/q_2^{2(J+K)} = ((p^2/3)/(p^2/(2-p)^2))^{J+K}
    = (1+o(1)) (4/3)^{J+K} = (ln x)^{0.831+o(1)},
    so this block / E[T]^2 <= 4 (4/3)^{J+K}/N_S = x^{-1+o(1)};
    (overlapping windows, no shared site) <= 4 N_S^3 (L+2) q_2^{J+K}
    crudely (bound one pair's indicator by its side-match, the
    other's by 1... sharpened: bound E[YY'] <= q_2^{J+K} and count
    <= 4 N_S^2 (L+2) N_S pairs), giving / E[T]^2 <=
    4(L+2)/(N_S q_2^{J+K}) = x^{-1+o(1)}. Total Var(T)/E[T]^2 =
    x^{-1+o(1)}; Chebyshev gives P(T < E[T]/2) = x^{-1+o(1)}, and
    sum over dyadic x_r converges: Borel-Cantelli yields (i).
(e) Disjointification. deg(i) := #{j in S^M : side(j) = side(i)}.
    Conditional on side(i) = v, deg(i) is a sum of side-match
    indicators with q_v <= (max_t P(h=t))^{J+K} = p^{J+K} =: q_max,
    and N_S q_max = x^{1-o(1)}. The indicators over j are not
    mutually independent (adjacent sites share gaps): split the
    sites into L+3 residue classes mod L+3 -- within a class the
    windows are disjoint, hence independent -- apply Chernoff per
    class and union over classes and sites (dilution step; absorbed
    from the Section 3.5 check). A.s. eventually max_i deg(i) <=
    2 N_S q_max. Greedy matching: each
    selected pair invalidates <= 2 max_deg incident pairs, so the
    matching size is >= T/(4 max_deg) >=
    (N_S^2 q_2^{J+K}/2)/(8 N_S p^{J+K}) = (N_S/16)(2-p)^{-(J+K)}
    = N_S (ln x)^{-2+o(1)} = x^{1-o(1)}   [2^{J+K} =
    (ln x)^{2+o(1)}], giving (ii). QED
    [U17.6 discharged: the covariance table is (d), the matching
    floor is (e).]

### 3.3 M2 (balance in the model; COMPLETE, Session B) + GATE

All statements remain about Model M; primes-side conclusions are
drawn ONLY as architecture decisions (gate rule), not as theorems.

M2.1 (expectation balance). On S^M_x at Par(1,x), splitting both pair
counts into diagonal (= N_S each, cancels), overlapping (|i-j| <=
L+2: o(main) by the (d)-type bounds), and disjoint parts:
    E[C^M_sides - C^M_words]
      = (1+o(1)) N_S^2 q_2^{J+K} (1 - q_2)
      = (1+o(1)) E[C^M_sides,off],
i.e. the model balance CLOSES, with x^{2-o(1)} margin in absolute
terms. The RELATIVE room is
    E[C^M_sides,off]/E[C^M_words,off] = q_2^{-M} = (2 ln x)^{M}
per middle position; at the normal form M = 1 this is
(2 ln x)^{1} = (log x)^{1+o(1)}.
FINDING F17.2 (kickoff orientation corrected): the kickoff's M2
expectation "closes with (log x)^{2-o(1)} room" is NOT reproduced;
the model room at M = 1 is (2 ln x)^{1+o(1)}. The architecture
consequence is unchanged (the balance closes), but every D1 budget
downstream must be set against ONE power of log x per middle
position, not two. General M: room (2 ln x)^M, at linear cost in
depth (L = J + M + K); no fixed M recovers a super-polylog budget.

M2.2 (concentration). Var(C^M_sides,off) / E[...]^2 = x^{-1+o(1)}
(same table as M1(d) with the middle clause dropped); likewise for
C^M_words,off, whose overlapping block is again o(main) [runs of
equal gaps: an adjacent pair i, i+1 with word(i) = word(i+1) needs
h_{i+1} = h_{i+2} = ... : probability q_2^{L} per adjacent pair].
Hence a.s. along dyadic scales C^M_sides - C^M_words > 0 eventually:
the model analogue of the P1 positivity holds a.s.

M2.3 (route audit: the Cauchy-Schwarz floor as D1.a would run it).
D1.a's unconditional skeleton is floor := |S|^2/|P| vs C_words with
the worst-case capacity |P| <= cap. Audited IN THE MODEL, where the
per-word constant is perfect (1+o(1)):
(i) Under the PINNED per-position filter (D0.2, all L gaps <=
    A ln x): unconditional Markov forces A >= 8 C_0 L (P3.3), so
    cap = (A ln x/2)^{J+K} and
      floor / E[C^M_words,off]
        = (2/(A ln x))^{J+K} (2 ln x)^{L} = (2 ln x)(4/A)^{J+K},
    and (A/4)^{J+K} = exp((J+K) ln(A/4)) is superpolylog for any
    A -> infinity (a fortiori for A asymp L): the floor route FAILS
    IN THE MODEL, killed by CAPACITY SLACK alone, before any sieve
    constant enters. In the model the per-position filter could be
    run at A ~ ln(2L) (exponential gap tails), but then the slack
    (A/4)^{J+K} is still superpolylog; for the primes, Markov-only
    tails force A asymp L outright. The per-position formulation is
    dead on this route in either world.
(ii) AGGREGATE-FILTER FIX (definition D0.2', Section 2.7): replace
    the per-position caps by the single window-sum cap
        sum_{1<=i<=L} g_{n+i} <= A' L ln x,   A' > 1 fixed.
    One Markov application loses site density <= (1+o(1))/A'
    [primes: P3.1' with the PNT-sharp mean; model: E[h] =
    (1+o(1)) ln x]; capacity becomes the simplex count
        |P| <= #{even (J+K)-tuples, sum <= A' L ln x}
             <= C(floor(A' L ln x/2), J+K)
             <= ((e A'/2) (L/(J+K)) ln x)^{J+K}
             = ((e A'/2 + o(1)) ln x)^{J+K},
    and the floor audit becomes
        floor / E[C^M_words,off] = (2 ln x) (4/(e A'))^{J+K}
        = (2 ln x)^{1 - (2/ln 2) ln(e A'/4) + o(1)}.
    THRESHOLD: the route survives iff
        (2/ln 2) ln(e A'/4) < 1  iff  A' < 4 sqrt(2)/e = 2.08104...,
    with room exponent theta(A') = 1 - (2/ln 2) ln(e A'/4):
    theta(2) = 0.1146, theta(1.9) = 0.2628, theta(1.5) = 0.9447,
    theta(4/e = 1.4715...) = 1 exactly. [Decimals corrected per the
    Section 3.5 check.] Site-density cost 1/A' (need A' > 1;
    the window sum concentrates at (1+o(1)) L ln x in the model by
    CLT, and for the primes Markov at fixed A' > 1 suffices).
    In the model, with A' in (1, 2.081) the floor route CLOSES with
    room (ln x)^{theta(A')}.
FINDING F17.3 (constructive, model-derived; binds D1): the
kickoff's D1 balance display carries the per-position capacity
(A log x/2)^{J+K} with A forced asymp L; that route is dead
independently of the sieve constant (capacity slack (A/4)^{J+K}).
The aggregate window-sum filter D0.2' at fixed A' in (1, 4 sqrt(2)/e)
is the repair; it also restores the kickoff's L = 2 log2 log x +
O_b(1) depth form (the P3.3(iv) deviation was an artifact of the
per-position filter). D1.a MUST run on D0.2'.

M2.4 (what remains for D1 after the fix; pre-shape of D1.a). With
D0.2' at fixed A', room (ln x)^{theta(A')} = exp(theta lnln x) =
2^{(theta/2)(1+o(1)) L} [lnln x = (ln 2/2) L (1+o(1))]. The
unconditional per-word Selberg constant to beat is C_sel(L) ~ 2^L L!
(U17.2, to be re-derived in D1.a): even its 2^L factor alone
exceeds the room 2^{theta L/2} (theta < 1), before L!. EXPECTED
D1.a outcome, now precisely budgeted: deficit factor
~ 2^{L(1 - theta/2)} L! at the critical spot; the kickoff's
"fails by a factor traceable to 2^L L!" is confirmed as the
post-fix residual -- the capacity slack (i) would otherwise mask it.

M2.5 (calibration discipline). D5.c (Section 7) measures the primes'
per-position collision rate at ~3.4x the naive model value at
x = 2e6 (parity ~2x + singular-series clumping ~1.7x): model-M
numbers are compared to primes data ONLY through those measured
correction factors; no primes-side conclusion is drawn from raw
model constants. [Asymptotically the parity factor is the model's
missing evenness; the clumping factor is the Hardy-Littlewood
pair-correlation mass, both irrelevant to the (2 ln x)^M ROOM
structure, which is scale-free.]

### 3.4 GATE DECISION (recorded Session B)

M1 + M2 are written and checked (independent re-derivation pass:
Section 3.5). The D2 gate rule evaluates as follows:
- M2 CLOSES in the model (M2.1/M2.2): the (E2')-supply architecture
  is model-consistent. D1 is NOT architecturally dead.
- GATE: PASS, with two binding amendments carried by findings:
  (a) F17.2 -- all D1 budgets are set against room (2 ln x)^M per
      middle position (M = 1 default), not (log x)^2;
  (b) F17.3 -- D1.a runs on the aggregate filter D0.2' with fixed
      A' in (1, 4 sqrt(2)/e), NOT on the pinned per-position filter.
- D1.a-d are hereby UNBLOCKED (gate order honored: this section
  precedes any D1 execution; D5.c's empirical landing (Section 7)
  ran before D1-route trust per the kickoff rule).

### 3.5 Independent re-derivation (review pass, Session B; EXECUTED)

Two independent checker agents re-derived the section's
computations from the setup + claimed answers only (derivations
withheld). Results:
- M1 checker: CONFIRMED on all constants (q_2 = p/(2-p), q_3 =
  p^2/(3-3p+p^2), q_3/q_2^2 -> 4/3 with O(p^2) correction,
  (2/ln 2) ln(4/3) = 2 log2(4/3) = 0.83007..., matching floor at
  the /16 level, 2^{J+K} = (ln x)^{2+o(1)} with constant exactly 2,
  dyadic Borel-Cantelli summability). Two absorbed refinements:
  (i) the degree-concentration Chernoff needs the residue-class
  dilution step (adjacent sites share gaps) -- absorbed into
  M1(e); (ii) within the x^{o(1)} slack the overlapping-window
  variance block dominates the shared-one-site block -- noted, both
  x^{-1+o(1)}, conclusion unchanged.
- M2 checker: PARTIAL solely on decimal places, all formulas
  confirmed (per-position and aggregate capacity forms, the
  floor/C_words displays with and without the evenness convention,
  threshold A' < 4 sqrt(2)/e, theta(A') form, theta(4/e) = 1
  exact). Corrections absorbed into M2.3: 4 sqrt(2)/e =
  2.08104... (not 2.0811), theta(2) = 0.1146, theta(1.5) = 0.9447.
  Parity-sensitivity answer: WITHOUT the evenness convention the
  threshold is 2 sqrt(2)/e = 1.04052 -- consistent with the
  general form A'_crit = 2 sqrt(2)/(e gamma_2) of Section 4.0
  (model no-parity capacity doubles, collision constant
  unchanged).
No discrepancy affects any conclusion of Sections 3.3-3.4; the
gate decision stands as recorded.

## 4. D1 -- the second-moment balance (UNBLOCKED Session B by the
## Section 3.4 gate; a/b this session, c/d Session C)

### 4.0 Route bookkeeping after the gate

Binding amendments carried in: F17.2 (room budget (2 ln x)^M per
middle position), F17.3 (execution on the aggregate filter D0.2',
A' in (1, 4 sqrt(2)/e) fixed). Balance target restated: on
S'_x(A', A'', D) with Par'(1,x), prove
    C_sides - C_words > 0 with pairs beyond every threshold s,
via floor := |S'_x|^2/|P| (P1(d)) with |P| <= ((e A'/2 + o(1))
ln x)^{J+K} (P3.3'(iv)), against unconditional upper bounds on
C_words. The general threshold calculus, proved by the M2.3
computation and reused throughout this section: writing the
per-position gap-collision rate at filtered sites as gamma_2/ln x
(gamma_2 a constant; MODEL: gamma_2 = 1/2), the floor route closes
iff
    (2/ln 2) ln(e A' gamma_2 / sqrt(2) / ... ) -- canonical form:
    floor / C_words,off = (ln x / gamma_2) (2/(e A' gamma_2))^{J+K}
    -> infinity  iff  A' < A'_crit := 2 sqrt(2) / (e gamma_2),
with room exponent theta = 1 - (2/ln 2) ln(e A' gamma_2 / 2) when
positive. Model instance: gamma_2 = 1/2, A'_crit = 4 sqrt(2)/e =
2.081 (Section 3.3). Equivalently: at the minimal admissible
A' -> 1+, the route is open iff gamma_2 < gamma_2^crit :=
2 sqrt(2)/e = 1.0405...

### 4.1 D1.a -- max-S version with the self-proved Selberg constant

[IN EXECUTION: inline lemma D1-L (k-uniform Selberg upper bound with
explicit constant, no Halberstam-Richert citation for the constant;
qualitative shape citable secondhand as Pintz 1305.6289 Lemma 3, eq.
(3.12), including its "H << log N" span note, asserted there and
therefore NOT relied on here) is being derived as a max-effort
workpaper (item-0017-workpapers/d1a-selberg.md) with independent
verification; the balance run against C_sel(L) lands here when it
completes. Expected per F17.4: deficit 2^{L(1-theta/2)} L!.]

### 4.2 D1.b -- first-moment averaging (COMPLETE)

The C_words side factorizes through site sums of singular series:
with any per-word upper bound N_w <= C_per(L) S(H_w) x/(ln x)^{L+1},
    C_words = sum_w N_w^2 <= C_per(L) x (ln x)^{-(L+1)}
              * sum_{n in S'_x} S(H_{w(n)}),
so D1.b needs upper control of the SITE-sum of S -- a first moment
over sites, i.e. (in the HL calculus) a SECOND moment over the word
box, since sites realize w at rate proportional to S(H_w).
Available tools, with their exact regimes (anchors re-verified this
session, extraction files cited):
(i) Kuperberg 2210.09775 Thm 1.1: T_k(h) = h^k + O(h^{k-beta})
    REQUIRES delta > 1/2 in k = O((log h)^{1-delta}) (U17.3
    correction), i.e. k below (log h)^{1/2}. Our regime: span
    budget h = A' L ln x gives log h = (1+o(1)) lnln x, and
    k = L+1 = (2/ln 2 + o(1)) lnln x = (2/ln 2 + o(1)) log h:
    k is LINEAR in log h -- the regime gap to Thm 1.1 is a full
    square, not a refinement. REGIME GAP STATED.
(ii) Kuperberg Thm 1.2 (growth-condition-free): T_k(h) <<
    h^k (3 log k)^k-type box bounds (exact display in
    extract/kuperberg22-singseries.md; re-verified at use). This
    gives box-average of S <= (3 log k)^k = exp(k ln(3 log k)):
    at k = (2/ln 2) lnln x this is
    (ln x)^{(2/ln 2) ln(3 ln k)} -- superpolylog (the exponent
    grows like 2.885 ln ln ln ... x), vs polylog room: even the
    box-average bound exceeds ANY (ln x)^theta budget.
(iii) Pintz 1004.1084 Thm 1/1' (via 1305.6289 Lemma 4): one-point
    extension averages (1/H) sum_h S(H u h)/S(H) = 1 + O(eta)
    require H >= exp(k^{1/eta}); meaningful accuracy (eta < 1)
    needs log H >= k^{1/eta} > k, while our log H = (1+o(1)) lnln x
    = (ln 2/2 + o(1)) k: FAILS for every eta <= 1. The
    LOWER-bound direction (Thm 1', regime H >= exp((1/eps) k/log k))
    eventually holds at our depths -- but C_words needs the UPPER
    direction. Direction split recorded.
CONCLUSION D1.b: first-moment averaging replaces max_w S by a box
average, and the best growth-free box average available
((3 log k)^k, Kuperberg Thm 1.2) still exceeds every polylog room
budget; the asymptotic-average tools (Kuperberg Thm 1.1, Pintz
Lemma 4 upper direction) sit a full square outside the regime. The
precise missing estimate is registered for D1.c: upper bounds of
S-moments at k ~ (2/ln 2) lnln x with span ~ ln x.

### 4.3 FINDING F17.5 -- the collision-constant closure of the
### unweighted floor route (new; model-invisible)

The threshold calculus of 4.0 depends only on gamma_2. For the
primes (measurements: balance_stats.py, d1c_gamma2.py; committed):
- Marginal (single-position) collision constant: empirical
  gamma_2 = (sum over even d of P-hat(g = d)^2) ln x = 1.2005 at
  x = 2e6, 1.1808 at 2e7, declining toward the HL/Gallagher-frame
  heuristic asymptote
      gamma_2 = E_even[S_2^2]/4,
      E_even[S_2^2] = 4 C_2^2 prod_{p>2} (1 + ((p-1)^2/(p-2)^2
                      - 1)/p) = 4.601923...,
  i.e. gamma_2 -> 1.150481...; the Euler product is CONFIRMED by
  direct summation (2/D) sum_{even d <= D} S_2(d)^2 = 4.601842 at
  D = 2e6 (d1c_gamma2.py).
- Vector-level (consecutive-window) rates from the D5.c pair
  counts: per-position geometric means 1.68 (x = 2e6) and 1.58
  (2e7) -- ABOVE the marginal product, i.e. consecutive-gap
  correlations add clumping beyond independent marginals (U17.8).
- Critical value: gamma_2^crit = 2 sqrt(2)/e = 1.040520...
CONSEQUENCE: gamma_2 > gamma_2^crit in every measurement and in the
heuristic asymptote (margin ratio 1.106 at the asymptote -- a
remarkably thin, but strict, closure). Hence A'_crit < 1 for the
primes: NO admissible aggregate cap A' > 1 opens the unweighted
floor route. Obstruction statement (B1 discipline, scope exact):
(a) PROVABILITY face: the floor's capacity term is the max-entropy
    simplex count; tightening it to the primes' true side-support
    requires exactly a two-point HL-type input (the collision
    constant), unavailable unconditionally -- the route cannot be
    completed by counting alone.
(b) TRUTH face (heuristic + empirical, model-language discipline):
    the target inequality floor > C_words is FALSE for the primes
    at every A' > 1 if gamma_2 > 1.0405, as all measurements and
    the HL asymptote indicate; the deficit factor is
    (e A' gamma_2/2)^{J+K}/(ln x/gamma_2)
    = (ln x)^{(2/ln 2) ln(e A' gamma_2/2) - 1 + o(1)}, e.g.
    (ln x)^{0.35+o(1)} at A' -> 1+, gamma_2 = 1.1505.
This closure is INDEPENDENT of the sieve constant (it binds even at
C_per = 1) and is invisible in Model M (gamma_2 = 1/2 <
gamma_2^crit): it is a genuinely primes-side obstruction, created
by Hardy-Littlewood clumping -- the same mass that makes exchange
configurations ABUNDANT (D5's superlinear class growth) makes the
unweighted capacity floor too weak to certify them. The three
surviving routes, each meeting a named blocker, are pre-shaped for
Session C: (1) S-weighted floors -- need HL LOWER bounds at matched
sides (parity-blocked prescription, O4 blocker 2) plus S-second
moments at growing k (D1.c register target); (2) typical-set
capacity restriction -- needs upper-sieve control of rare side
words at entropy precision (D1.a constant territory, F17.4);
(3) middle-width amplification (M > 1) -- room (2 ln x)^M grows
only linearly in the exponent while the closure deficit is
per-position multiplicative: no fixed M escapes.

### 4.4 D1.c / D1.d -- Session C (pre-shaped)

D1.c: name and assess "S second moment at growing k": needed form
    sum over (J+K)-tuples in the aggregate simplex of S(H_side)^2
    at k ~ (2/ln 2) lnln x, span ~ ln x; MoSo 0409258 proves
    R_k(h)/V_k asymptotics at FIXED k only (its sole uniformity
    remark defers to Granville-Soundararajan restrictions);
    Kuperberg stops at k << (log h)^{1/2}. Candidate register
    entry confirmed as a genuine gap in the tool base.
D1.d: Merikoski Chen substitution LOCATED (1811.03008 eq. (1.6)
    p. 6, A = 4 -> 3.99, Prop 12): a pairwise (k = 2-level)
    upper-sieve constant improvement of 0.25%; the D1 critical
    constant is per-word at k ~ lnln x with deficit
    exp(Theta(L log L)) -- map and exact reach statement Session C.

## 5. D3 -- tool cartography (the parity gray zone, mapped; drafted
## Session B from the 14 anatomies, to be finalized Session C)

Column legend per mechanism: which of (E1)/(E3) exact flank match,
(E2)/(E2') middle variability, (E4) tail caps at the produced sites,
(E5)-compatible depth (J,K ~ log2 log x), TT = tail-typicality
(positive-density sites so Markov selection applies), and the EXACT
missing ingredient. Standing structural fact used repeatedly: on a
site set of relative density rho, unconditional Markov tail
selection costs the factor 1/rho in the tail budget D, which feeds
J >= log2(bD): sparse-site constructions self-defeat once
log2(1/rho) exceeds the depth budget O(log2 log x) ("sparse-site
Markov cost"; the A3(b) order-of-quantifiers artifact made
quantitative).

T1 Pintz Thm 5 pattern (1305.6289 Sec 6; anatomy
pintz13-polignac.md). Supplies: two-site NEXT-GAP variability at a
constructed core -- if all sites of the constructed
consecutive-pair event continued with the same next gap, summed
Selberg bounds ((6.9)-(6.11)) contradict the Maynard-type lower
bound (6.6): the ONLY corpus mechanism that certifies
anti-rigidity of a continuation. Reach: variability is at the
EVENT class (tuple positions + almost-primality), not at matched
realized gap words; sites are sieve-weighted (density
S(H) N/log^k N: log-power sparse), k fixed (>= 3.5e6). Missing
EXACTLY: (a) class-count LOWER bounds for word-level flank classes
(replacing (6.6)) -- a prescribed-tuple lower bound at k ~ L, the
parity-blocked class; (b) (E4) at log-power-sparse sites: Markov
cost log^k x inflates D by log^k x, hence J by ~ k log2 log x --
self-defeat by factor k. TRANSPLANT SHAPE (recorded as the sharpest
positive lead of the corpus): T1's exclusion argument applied to a
flank class would derive (E2)-supply from HL-type lower bounds for
ONE matched-flank family -- the wall is exactly the lower bound,
nothing else in the pattern breaks.

T2 BFM bins + uniform Maynard-Tao (1404.5094; anatomy
bfm14-limitpoints.md). Supplies: chains of consecutive normalized
gaps at prescribed reals up to o(1), k = 8m^2+8m (verified
verbatim), along scale subsequences. NOTE (kickoff wording
corrected): the uniform engine's modulus is W = prod_{p <= w} p
with w = eps log N, i.e. W is a small POWER of N, not "W up to
eps log N". Missing EXACTLY: exact integer gap values ((E1)/(E3)
need entrywise equality; limit-point approximation has o(1)-
normalized slack ~ o(log x) absolute -- infinitely too coarse);
depth (chains of length ~ loglog x need k ~ (loglog x)^2 with
value prescription -- outside every uniform range in the corpus);
TT fails (Maynard-Tao-weighted sites, log-power sparse).

T3 BFTB composite-forcing trap (1311.7003; anatomy
bftb14-consecutive.md). Supplies: EXACT consecutive realization of
admissible tuples (dedicated prime q_t kills each non-tuple offset
along one AP mod Q = prod q_t) -- realizing two tuples H, H' with
equal flank point-sets and different middles would give exact
(E1)+(E2)+(E3) pairs: the only corpus mechanism reaching exact
matched flanks. Missing EXACTLY: (E4)/TT. The trap modulus is
exponential in the tuple span; for span s the AP density is
e^{-(1+o(1)) s}-level, so the sparse-site Markov cost inflates D by
e^{s}, J by ~ s -- and (E1)/(E3) at depth J,K need s >= 2(J+K):
J >= s >= 2J, quantitative self-defeat (the Shiu-circularity
blocker in trap form). Conditional note (scope-qualified): under a
Cramer-Granville pointwise bound (Hypothesis-B shape) the (E4)
caps hold pointwise with D ~ log^2 x, K ~ 2 log2 log x, and the
trap route CLOSES -- consistent with EXCH' being strictly weaker
than the chain's A+B package (tate-transfer O4); the entire
unconditional content is the sparse-site tail clause.

T4 Pintz DHL*(k,2) almost-prime consecutivization (1305.6289
Sec 3; anatomy pintz13-polignac.md). Supplies: consecutive prime
PAIRS inside tuples at the cheapest density in the corpus
(c_2(k) S(H) N/log^k N; the P^- clause certifies compositeness
between hits with no trap modulus). Missing EXACTLY: word-level
flanks (other tuple components are almost-primes, their positions
free); sparse-site Markov cost log^k x -> J inflated by
~ k log2 log x (k >= 3.5e6 fixed): self-defeat by factor k, milder
in form than T3 but same shape. Cheapest consecutivization,
still flankless.

T5 scale flexibility (Pintz 1407.2213 normalizer class; BF15
1510.08054 R-scale chains + window confinement; anatomies
pintz14-gapdist.md, bf15-erdosrankin.md). The class-F cap is
exactly the Erdos-Rankin scale g(x) log x (verified); BF15's
Corollary 4.2/(6.8) confinement P cap (n+x, n+y] = P cap (n+H)
holds for EVERY n == b (W) -- exact upper-set control of a whole
window, the strongest prescription device in the corpus. FINDING
F17.6 (kickoff expectation corrected): the transport does NOT die
at (E5)'s b-D coupling -- at R-scale sites the caps take D ~ R(x),
J, K ~ log2 R(x) = (1+o(1)) log2 log x, which is (E5)-compatible.
It dies at: (a) exactness (normalized prescription has o(f(x))
slack; (E1)/(E3) need exact integers) -- except via the BF15
confinement, which controls the prime SET only from above, so
which skeleton points are prime varies and matched-flank
variability again needs an anti-concentration input (pigeonhole-
blind otherwise); and (b) TT: W = e^{(1+o(1)) C x}, sites
astronomically sparse, Markov cost e^{Cx} -- the worst in the
corpus. Verified and recorded in place of the expected b-D
failure.

T6 Merikoski refinements (1811.03008; anatomy
merikoski18-limitpoints.md). Syndeticity of the limit-point set:
verified verbatim (Cor 3 + rephrasing sentence; the paper notes it
follows already from BFM). Chen substitution at the pairwise
upper-sieve constant (A = 4 -> 3.99, eq (1.6), Prop 12): feeds
D1.d. Reach class: T2 (normalized/limit-point level); adds no new
(E)-clause reach; its constant datum is the corpus's only
improvement lever at an upper-sieve spot.

Maier matrix (fourth tool type, from D4; Maier 1985 +
Hildebrand-Maier 1988; anatomies maier85-matrix.md,
hm88-chains.md). Supplies: COUNT oscillations in translated
intervals (both selection steps verbatim averaging pigeonholes);
prescribes only the average gap ratio (HM88), never values --
pigeonhole-blind for (E2'); columns are APs mod P(z) with
P(z) = x^{1/D}: polynomially sparse, Markov cost x^{1/D} -> J ~
(log x)/D >> L: self-defeat. Both D4 reduction options of the
kickoff hold simultaneously: prescription-free (parity-safe but
variability-blind) AND sparse-sited.

TABLE SUMMARY (unconditional reach): exact flanks -- only T3, at
self-defeating trap sparsity; middle variability certificate --
only T1, at event (not word) level, blocked by the class lower
bound; tail typicality -- only unfiltered positive-density site
sets (this dossier's D0.2/D0.2' selection layer); depth
(E5)-compatibility -- generic (even R-scale transports pass, F17.6).
No mechanism or composition in the corpus supplies all clauses
simultaneously; each composition meets at least one of: class
lower bounds (parity-blocked), sparse-site Markov cost
(Shiu-circularity shape), pigeonhole variability-blindness. The
three O4 blockers are confirmed EXHAUSTIVE for this corpus, with
the sparse-site Markov cost now quantified as the uniform
mechanism behind every TT failure.

## 6. D4 -- blocker hardening at the weighted clause (drafted
## Session B; each O4 blocker gets a WEIGHTED-CLAUSE addendum)

### 6.1 Blocker 3 addendum: Shiu circularity vs many-small-
### difference configurations

The kickoff asks for the exact inequality deciding whether spread
differences (M >= 2, small d_j, E != 0) evade the string-density
penalty. They do not; the exact accounting:
(a) Depth floor is M-invariant. (E4) tail caps at tail-typical
    sites need D >= typical delta ~ ln x, and 2^K >= D; (E5) needs
    J >= log2(b D). Hence J, K >= (1+o(1)) log2 ln x REGARDLESS of
    the middle width M or the difference pattern: the weighted
    clause cannot shrink the flank depth below the (E4)/(E5) floor
    J + K >= (2+o(1)) log2 ln x.
(b) The penalty is flank-driven. A Shiu-string prescription of a
    matched-flank configuration needs string length m >= J + K + M
    >= (2+o(1)) log2 ln x; Maynard 1405.2593 Thm 3.3's site density
    >> pi(x)/(2q)^{exp(Cm)} then costs, by the sparse-site Markov
    mechanism (F17.8), a tail-budget inflation
    D -> (2q)^{exp(Cm)} D, i.e.
        J >= log2(b D) + exp(C m) log2(2q)
          >= exp((2C + o(1)) log2 ln x) = (ln x)^{(2C/ln 2)(1+o(1))},
    against available J = (1+o(1)) log2 ln x: failure by an
    exponential level, for EVERY M >= 1 and every distribution of
    the middle differences. The 2^{-i} decay of the weighted sum is
    irrelevant: by P2 the clause only needs the integer invariant
    E != 0, and the supply cost sits entirely in the flanks.
EXACT KILLING INEQUALITY (recorded): the route requires
    (ln x)^{(2C/ln 2)(1+o(1))} <= (1+o(1)) log2 ln x,
false for all large x; equality of scales would need the Thm 3.3
penalty exponent exp(Cm) to be replaced by O(log m) -- a
doubly-exponential improvement of the string technology.

### 6.2 Blocker 1 addendum: pigeonhole variability-blindness at
### M >= 2 (a strictly finer blindness)

At M = 1 the P1 positivity C_sides - C_words > 0 certifies an
(E2')-pair outright (P2.1). At M >= 2 it does NOT: a differing-
middle collision may have E = 0 (P2.2's example (2,8) vs (4,4)),
and counting cannot separate E = 0 from E != 0 pairs -- the
pigeonhole target would have to be the E-graded count
C_sides - C_words - #(E = 0 collisions), whose upper control is
again a two-point correlation input. Model-side number (discipline:
model only): conditional on a side match with differing middles,
P(E = 0) is a single lattice condition on the middle-difference
vector, of probability O(1/ln x) at M = 2 -- so the degeneracy is
measure-thin in the model, but certifying THAT for the primes is
once more HL-type information. Net: the general (E2') clause makes
pigeonhole-blindness strictly worse, never better; the normal form
M = 1 is the pigeonhole-optimal instance (one more reason the
supply order of F17.1 puts SUP_1^norm first).

### 6.3 Blocker 2 addendum: parity-blocked prescription at the
### weighted clause

The prescription length cannot drop below the (E4)/(E5) depth
floor (6.1(a)): any prescriptive route must pin >= J + K =
(2+o(1)) log2 ln x consecutive gap values (or their point-set
equivalent), i.e. a prescribed-tuple event of k ~ L points with
consecutiveness -- Maynard 1405.2593's own limitation remark
(read per the adjudication as a statement about the unconditional
tool class) applies at every M. The weighted clause relocates
NOTHING of the prescription burden into the middle: F17.7's
transplant lead shows the burden can be shifted to a class-count
LOWER bound for one matched-flank family, which is the same
blocked class in counting form. Maier-matrix as a fourth tool
type: mapped in the D3 table -- both selection steps are averaging
pigeonholes (variability-blind) and its columns are x^{1/D}-sparse
(F17.8 cost); it joins, not escapes, the register.

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
in-core; 1e9 feasible in-core (~6 GB peak) -- D5.b deep scan
launched at 1e9 (d5b_deep.py; deeper firsts (7,7)/(8,8), b in {3,5}
certificates honoring (E5), (6,6) continuity row).

### 7.1 D5.c grid (balance_stats.py; A = None | 8 | 4 gap caps give
### near-identical counts at these x -- caps far above actual gaps;
### table reports A = None)

x = 2e6 (pi = 148933, ln x = 14.51):
  (J,K,D0)   sites     |W_L|     |P|      C_w-diag C_s-diag P1pairs cls
  (4,5,30)   143787    143761    143749   52       76       24      12
  (5,5,34)   145248    145241    145239   14       18       4       2
  (6,6,64)   148703    148702    148702   2        2        0       0
  (7,7,67)+  148711    saturated (all words distinct)       0       0
x = 2e7 (pi = 1270607, ln x = 16.81):
  (4,5,30)   1162405   1162194   1162016  422      778      356     178
  (5,5,34)   1190922   1190889   1190868  66       108      42      21
  (6,6,64)   1269901   1269900   1269900  2        2        0       0
x = 1e8 (pi = 5761455, ln x = 18.42):
  (4,5,30)   4978302   4976976   4975689  2654     5232     2578    1287
  (5,5,34)   5161256   5161080   5160937  352      638      286     143
  (6,6,64)   5754075   5754073   5754072  4        6        2       1
  (7,7,67)+  5758932   saturated                            0       0
(C_w-diag / C_s-diag = off-diagonal word / side collision counts;
P1pairs = C_sides - C_words; cls = exchange classes. Class counts
REPRODUCE the committed record 12/178/1287, 2/21/143, first
(6,6,64) at 1e8.)

Vector-level collision constants (per-position geometric means of
actual/naive-model off-diagonal side-collision ratios):
  x = 2e6: (4,5): (76/1.418e-3)^{1/9}/2 -> gamma_2^vec = 1.68
  x = 2e7: (4,5): (778/2.461e-2)^{1/9}/2 -> 1.58 ; (5,5): 1.64
  x = 1e8: (4,5): (5232/1.982e-1)^{1/9}/2 -> 1.55 ; (5,5): 1.60
declining toward, and consistently above, the marginal asymptote
1.1505 and the critical 1.0405 (F17.5; marginal empirical values
1.2005/1.1808 at 2e6/2e7 from d1c_gamma2.py).

S-site sample moments (A = None rows): S2nd/S1st^2 stable in
[1.32, 1.51] across the grid and across x -- the S-site
distribution is low-variance at these depths (D1.b/c context);
lambda_w means (sub-1-mass corner) decline with x as expected
(e.g. (4,5): 105 -> 47 -> 24).

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
      greedy-matching floor; Session B obligations. DISCHARGED
      Session B: Theorem M1 proof steps (d)/(e); independent
      re-derivation pass Section 3.5.
U17.7 PNT-sharp window-sum mean (P3.1'): the o(1) rate in
      p_N = (1+o(1)) N ln N is used qualitatively only (fixed A'
      strictly inside the threshold absorbs it for x large); no
      effective PNT form is invoked. Flagged because chain-v1's
      elementary layer deliberately used only Chebyshev; this
      dossier's D0.2' layer is the first project use of PNT.
U17.8 Vector-level collision constant: the D5.c pair counts imply
      per-position rates (1.68/1.58) ABOVE the marginal product
      (1.20/1.18) -- consecutive-gap correlations add clumping. No
      derivation of the asymptotic vector constant is attempted;
      the F17.5 closure already binds at the (smaller) marginal
      asymptote, so the vector excess only widens the margin.
U17.9 The gamma_2 asymptote uses the Gallagher-frame gap law
      P(g = d) ~ S_2(d) e^{-d/ln x}/ln x (heuristic; frame anchors
      in extract/gl20-heuristics.md). The F17.5 TRUTH face is
      explicitly heuristic+empirical; the PROVABILITY face does not
      use it.

## 9. Findings register (F17.n)

F17.1 (Section 2.6): the landed Lean consumption interface
      (ExchangeSupply1) is strictly normal-form (M = 1); the supply
      target set is ordered SUP_1^norm > SUP'_1 > SUP'_b, and only
      the first closes the Lean gap without further statement-layer
      work. [Faithfulness watch executed at 66adc54.]
F17.2 (Section 3.3, M2.1): model-balance room is (2 ln x)^M per
      middle position ((log x)^{1+o(1)} at the normal form M = 1);
      the kickoff's "(log x)^{2-o(1)}" orientation is not
      reproduced. All D1 budgets recalibrated accordingly.
F17.3 (Section 3.3, M2.3): capacity-slack obstruction and repair.
      The pinned per-position gap filter forces A asymp L
      (Markov-only tails), and the D1 Cauchy-Schwarz floor route
      then fails EVEN IN THE MODEL by the capacity slack
      (A/4)^{J+K}, independently of any sieve constant. Repair:
      aggregate window-sum filter D0.2' at fixed A'; the floor
      route survives in the model iff A' < 4 sqrt(2)/e = 2.081...,
      with room exponent theta(A') = 1 - (2/ln 2) ln(e A'/4). Also
      restores L = 2 log2 log x + O_b(1). D1 execution bound to
      D0.2'.
F17.4 (Section 3.3, M2.4): post-fix D1.a budget: room 2^{theta L/2}
      vs unconditional per-word constant C_sel(L) ~ 2^L L! (U17.2)
      -- expected deficit 2^{L(1-theta/2)} L!, the kickoff's "2^L L!
      failure" confirmed as the post-fix residual (it would
      otherwise be masked by the capacity slack).
F17.5 (Section 4.3): collision-constant closure of the unweighted
      floor route. Threshold calculus: route open iff
      gamma_2 < 2 sqrt(2)/e = 1.0405 (at A' -> 1+); the primes'
      gamma_2 exceeds it in every measurement (1.20/1.18 marginal
      at 2e6/2e7; 1.68/1.58 vector-level) and at the heuristic
      asymptote E_even[S_2^2]/4 = 1.1505 (Euler product =
      4.601923/4, confirmed by direct summation). The route is
      closed for the primes at every admissible A' > 1,
      independently of the sieve constant, and invisibly to Model
      M (gamma_2 = 1/2). HL clumping both supplies the exchange
      configurations and defeats the max-entropy capacity floor.
F17.6 (Section 5, T5): the cross-normalization transport does NOT
      fail at (E5)'s b-D coupling (the kickoff's expected outcome):
      R-scale caps give J,K ~ (1+o(1)) log2 log x, (E5)-compatible.
      It fails at exactness (o(f) normalized slack vs exact integer
      flank equality) and at tail typicality (W = e^{(1+o(1))Cx}
      site sparsity). Corrected expectation recorded.
F17.7 (Section 5, T1): transplant shape -- Pintz's Thm 5 exclusion
      argument, applied to a matched-flank word class, derives
      (E2)-supply from ONE missing input: an HL-type lower bound
      for the class count of a single matched-flank family
      (prescribed-tuple lower bound at k ~ L, the parity-blocked
      class). Every other step of the pattern (summed Selberg
      exclusion of the rigid middle) survives at our depths. The
      sharpest positive lead in the corpus.
F17.8 (Section 5, standing fact + T3): the sparse-site Markov cost
      -- unconditional tail selection on a density-rho site set
      inflates the tail budget D by 1/rho, hence J by log2(1/rho);
      every TT failure in the corpus is this mechanism (T1/T4:
      log-power rho, self-defeat by factor k; T3: e^{-span},
      J >= span >= 2J self-defeat; T5: e^{-Cx}; Maier matrix:
      x^{1/D}-sparse columns). Under a Hypothesis-B-shaped
      pointwise bound the T3 trap route CLOSES (scope-qualified,
      consistent with EXCH' < A+B) -- the entire unconditional
      content of (E2')-supply-by-construction is the sparse-site
      tail clause.

## 10. Follow-up candidates (described only; never silently executed)

[none yet]

## 11. Review section

[Session D: R1 same-family fresh-role (computation audit) + R2
cross-family (scope audit), blind, anchor-stripped payload via a
committed deterministic strip script; web OFF; reviewer receives
exactly payload + object.]
