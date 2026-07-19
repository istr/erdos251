# item-0020 W3 -- proof investment (referee grain; AUDIT-REPAIRED
# copy -- every sustained finding of the in-run adversarial pass is
# folded in at the marked [audit repair] sites; full disposition in
# audit-record.md)
# Claims C1-C4 on the W2 priority order; every constant that appears
# went through budget_sheet_20 (evaluator-first inner loop).  Support
# class of every claim below: PROVED modulo the NAMED consumed
# inputs, each cited with its provenance and its own grade.

Standing frame: D0 pin of dossier/relext-statements.md (A' = 1.5,
A'' = 48, D = ceil(13 C_0 A'' ln x), J = ceil(log2 D) = K, L =
J+1+K, M = 1); counts RS.1 on T = S'^{(s)}_x; C_0 = chain-v1 Lemma
2.1's Chebyshev constant (p_n <= C_0 n ln(n+2) for all n >= 1,
C_0 >= 1 absolute; e2prime-supply P3 standing constants). W2, V2,
cap_r per the W0 dictionary.

CONSUMED INPUTS (named once; provenance grade per item
[audit repair: I3/I4 provenance labels made exact; I5 corrected]):
  (I1) RS.1 partition identities: sum_d N_{P,d} = N_P and
       sum_P N_P(T) = |T| exactly (relext-statements RS.1; PROVED
       -- definitional).
  (I2) TailIntersection at the pin: forall s exists x_7(s) forall
       x >= x_7: |S'^{(s)}_x| >= N/4 (relext-statements 7.1; C2
       base form = P3.3'(ii) repaired, PROVED unconditional at
       dossier level, pin provenance note carried).
  (I3) Capacity pattern: the count of r-tuples of positive even
       integers with sum <= B is <= C(floor(B/2), r)
       <= (e floor(B/2) / r)^r (stars and bars with a slack
       variable; C(M,r) <= (eM/r)^r). The r = J+K instance is
       P3.3'(iv) verbatim (e2prime-supply, PROVED); the general-r
       form consumed at r = L is a THIS-RUN extension by the
       identical proof (declared in the W0 dictionary), not a
       displayed corpus lemma.
  (I4) Chebyshev inversion: N = pi(x) >= x/(2 C_0 ln x) for all
       x >= x_0(C_0). Derived HERE, one line, from the anchored
       Chebyshev bound p_n <= C_0 n ln(n+2), n >= 1 (chain-v1
       Lemma 2.1 via e2prime P3 standing constants): with
       n = ceil(x/(2 C_0 ln x)), C_0 n ln(n+2) <= x for x large,
       so p_n <= x, i.e. pi(x) >= n. The inversion display is
       this run's; the consumed corpus fact is the Chebyshev
       bound alone.
  (I5) Gap parity under the RS.1/T6 indexing: gaps g_m are even
       for GAP index m >= 2 (difference of odd primes; g_1 = 1 is
       the only odd gap -- e2prime P2 parity clause and D0). The
       word of site n has entries g_{n+i}, i >= 1, so every entry
       of every site word (n >= 1) has gap index >= 2 and is
       even: NO site word carries an odd entry, and the RS.1
       partition over even side pairs is exact with no
       exceptional class.

----------------------------------------------------------------
## Claim C1 (A3.card): MatchedFlankLower holds at the D0 pin,
## delta = 1/2, s-uniformly, asymptotically

STATEMENT. For every s >= 0 there is x_2(s) such that for all
x >= x_2(s):

    sum over P in Fam_2(S'^{(s)}_x) of N_P  >=  (1/2) |S'^{(s)}_x|.

More precisely: for every constant delta < 1 the same holds with
delta in place of 1/2 (threshold depending on delta); the s-uniform
quantifier order of the 7.1 Prop (exists delta forall s exists
x_2(s)) is delivered at delta = 1/2.

PROOF. Fix s and x. Write S' = S'^{(s)}_x, F = Fam(S'), F_2 =
Fam_2(S').
(1) By (I1), sum_{P in F} N_P = |S'|, and since Fam_2 collects
    exactly the classes with N_P >= 2,
        sum_{P in F_2} N_P = |S'| - #{P in F : N_P = 1}
                          >= |S'| - |F|.
(2) Capacity: every P = (a, c) in F is realized by some n in S'.
    The L window gaps of n sum to at most A' L ln x (the D0.2'
    window cap, definitional in S'), the middle gap is >= 2, and
    ALL side entries are even positive integers (I5: every site
    word is all-even under the RS.1/T6 indexing) [audit repair:
    the draft's n = 1 exception and its +1 were vacuous and are
    deleted]. Hence (a, c) is a (J+K)-tuple of positive even
    integers with sum <= A' L ln x - 2, and by (I3) with
    r = J+K, B = A' L ln x:
        |F| <= C(floor(A' L ln x / 2), J+K)
            <= ((e A'/2)(L/(J+K)) ln x)^{J+K} =: cap.
    Since L/(J+K) = 1 + o(1) and J+K = (2/ln 2) lnln x + O(1) at
    the pin (P3.3'(iii) ADDITIVE depth form) [audit repair:
    additive, not coefficient-O(1)], ln cap = (2/ln 2)(lnln x)^2
    (1 + o(1)): cap = x^{o(1)}.
(3) Population: by (I2), |S'| >= N/4 for x >= x_7(s), and by (I4)
    N >= x/(2 C_0 ln x): so |S'| >= x^{1-o(1)}.
(4) Let x_cap be s-free with 8 cap <= x/(2 C_0 ln x) for all
    x >= x_cap (exists since cap = x^{o(1)}; budget_sheet_20 T2
    prints both conventions: scale marker x ~ 1e25, and the
    PROOF-condition crossings at the ceil-honest D0 depths
    x ~ 1e100-1e107 for C_0 in {1,2} [audit repair: exact
    condition and ceil depths]). For
    x >= x_2(s) := max(x_7(s), x_cap, x_0(C_0)) [audit repair:
    the I4 threshold folded in]:
        |F| <= cap <= N/8 <= |S'|/2,
    hence by (1): sum_{F_2} N_P >= |S'| - |S'|/2 = (1/2)|S'|.  QED

REMARKS. (a) The same argument with 8 replaced by 4/(1-delta)
gives every delta < 1: the asymptotic Fam_2 mass fraction is
1 - o(1). (b) Nothing here concerns middles, HL inputs, or class
laws: the statement-layer status of A3 ("OPEN for the primes",
relext-statements 4.A) is superseded for the D0-pinned parameter
map by this cardinality argument; the route-hardness remarks there
concerned class-law routes and remain true of those routes. (c)
Finite scales: at x <= 1e10, cap exceeds N by many orders (T2;
measured: 99.75%+ singleton mass, m1) -- the bound is empty there;
no finite-scale claim is made (D3(vi) row printed in T2). (d) The
7.4 ledger consequence: the slack item (s1) delta/2 is now a
PROVED 1/4 (delta = 1/2), s-uniform, at asymptotic scales.

----------------------------------------------------------------
## Claim C2 (M1.a falsity): the kickoff's M1 sufficient condition
## fails at the D0 depths

STATEMENT. For every fixed s: W2(x;s)/|S'^{(s)}_x| -> infinity as
x -> infinity (along the D0 parameter map; W2 is counted on
S'^{(s)}_x, so it carries the s-argument -- notation made explicit
per audit). In particular "W2 = o(|S'^{(s)}_x|) uniformly in s" is
false.

PROOF. Fix s, take x >= x_7(s). The full words w(n) = (a, d, c) of
sites n in S' are L-tuples of positive even integers (I5: every
site word is all-even) with window sum <= A' L ln x, so as in
C1(2), with r = L:
    R := #realized full words <= ((e A'/2) ln x)^L =: cap_L
       = x^{o(1)}.
The full-word classes are the cells (P, d), N_w = N_{P,d}, and
sum_w N_w = |S'| (I1). By Cauchy-Schwarz on the word fibers,
    sum_w N_w^2 >= (sum_w N_w)^2 / R >= |S'|^2/cap_L,
so
    W2 = sum_w N_w(N_w - 1) = sum_w N_w^2 - |S'|
       >= |S'| ( |S'|/cap_L - 1 ).
By (I2) + (I4), |S'|/cap_L >= x^{1-o(1)} -> infinity.  QED

REMARKS. (a) This refutes the SUFFICIENT CONDITION displayed in
the kickoff's M1 lane, not the lane's relative hope; the
refinement is executed non-silently (mechanism-inventory M1;
F20.1). (b) The failure mechanism is pair-vs-site mass mismatch
at astronomical class multiplicities (average full-word class
size |S'|/R >= x^{1-o(1)}), not any sieve constant: the trap the
kickoff pre-registered (rank-2k constant) is a SECOND, independent
obstruction on upper-bound routes (T1 trap row). (c) Same chain on
side fibers gives the unconditional side-collision abundance
    V2 >= |S'| ( |S'|/cap_{J+K} - 1 ),  V2/|S'| -> infinity
(M3.2; the P1(d) Cauchy-Schwarz floor of e2prime read as a lower
bound with the P3.3'(iv) capacity in the denominator). (d) Both
(a)-type and (c)-type conclusions are asymptotic; the W2
finite-scale vacuity rows are printed in T3, and the V2-floor's
vacuity scales are T2's A3.card side-cap crossover rows [audit
repair: citation corrected from T3].

----------------------------------------------------------------
## Claim C3 (the reduction): B2.pairs implies RelExtensionUpper,
## unrestricted selections, with eps_REU = sqrt(eps_pair)

STATEMENT. Suppose B2.pairs (mechanism-inventory M1.c): for every
eps > 0 there is x_8(eps) with, for all x >= x_8 and all s >= 0,

    Q(x,s) := sum over P in Fam(S'^{(s)}_x) of
              (1/N_P) sum over even d >= 2 of N_{P,d}(N_{P,d}-1)
           <= eps |S'^{(s)}_x|.

(The d-range matches the anchored M1.c display verbatim [audit
repair]; by (I5) every realized middle is an even gap >= 2 and
N_{P,d} = 0 elsewhere, which is also exactly what step (2) below
needs: the maximizing cell lies inside the hypothesis's d-range.)

Then RelExtensionUpper (7.1 text) holds with x_4(eps) := x_8(eps^2),
for ALL total selections d : SidePair -> N (a fortiori for the
FL-1-restricted selections Supply.lean consumes).

PROOF. Fix x >= x_8(eps^2), s, and any selection (d_P). Work over
P in Fam = Fam(S'^{(s)}_x); write M_P := max over d of N_{P,d}
(the max over realized middles; N_{P,d} = 0 off them).
(1) Per class, (N_{P,d_P} - 1)_+ <= (M_P - 1)_+.
(2) Per class, (M_P - 1)_+ <= sqrt(M_P (M_P - 1))  [squares:
    (M-1)^2 <= M(M-1) iff M >= 1; both sides 0 at M in {0,1}],
    and M_P(M_P - 1) is one summand of pairs_P :=
    sum_d N_{P,d}(N_{P,d}-1), so (M_P - 1)_+ <= sqrt(pairs_P).
(3) Cauchy-Schwarz with weights N_P (N_P >= 1 on Fam):
      sum_P sqrt(pairs_P)
        = sum_P sqrt(N_P) sqrt(pairs_P/N_P)
        <= sqrt( sum_P N_P ) sqrt( sum_P pairs_P/N_P )
        =  sqrt( |S'| * Q(x,s) )        [by (I1)]
        <= sqrt( |S'| * eps^2 |S'| ) = eps |S'|.
(4) Chain (1)-(3): sum_P (N_{P,d_P} - 1)_+ <= eps |S'|
    = eps sum_P N_P (I1).  QED

REMARKS. (a) No per-word sieve constant, no rho, no class law, no
k-dependent factor appears: the consumption is sheet-empty (T5
row (a): NONE). (b) The reduction proves the UNRESTRICTED form;
per FL-1 this is declared: if B2.pairs is ever proved, the
one-line Supply.lean statement change (delete hrestr) becomes
available as a follow-up. (c) Sharpness of the sqrt [audit
repair: exact arithmetic; this is its OWN configuration, not a
C(t) modification]: take t homogeneous classes of size m, each
with one middle of multiplicity r (2 <= r <= m) and the rest
distinct. Then |S'| = tm, LHS = t(r-1), Q = t r(r-1)/m, and
    (LHS/|S'|) / sqrt(Q/|S'|) = sqrt(1 - 1/r) -> 1,
i.e. the chain is tight to within sqrt(1-1/r) for EVERY
2 <= r <= m: the eps -> sqrt(eps) loss is inherent to this
consumption, not slack to recover. (d) Gate arithmetic at the
ledger values (T5) [audit repair: one eps_C convention]: eps_C
enters 7.4(s2) only when a proof detours through window-only
counts; the C1/C3 chains never do, so eps_C is absent from this
run's chain. With delta = 1/2 (C1), the 7.2 pigeonhole coupling
(eps = delta/4 = 1/8) closes from B2.pairs at pair-eps =
(delta/4)^2 = 1/64; the gate SENTENCE display at the
conservative consumption eps_C < 1/2 lands in the same class
((1-eps)^2/64). The m4 measured eps_C ~ 0 is cited as direction
only and enters no constant (D3(vi)).

----------------------------------------------------------------
## Claim C4 (the barrier): the unconditional identity layer cannot
## prove RelExtensionUpper or B2.pairs

TOOL LIST T (named; exactly the unconditional facts consumed
anywhere in this run's chains and in the anchored counting layer's
unconditional shelf):
  (T-a) the RS.1/D0.3 definitional identities (I1) and all
        cardinality bookkeeping (P1(a)-(d) of e2prime);
  (T-b) the capacity bounds (I3)/(P3.3'(iv) pattern);
  (T-c) the aggregate Markov/Chebyshev facts: P3.1' (window sums,
        PNT-sharp mean), P3.2 (tail sums), Chebyshev
        p_n <= C_0 n ln(n+2) and its inversion (I4), PNT
        pi(x) = (1+o(1)) x/ln x;
  (T-d) the retention conclusions P3.3'(ii)/(iii) and
        TailIntersection at the pin (I2);
  (T-e) two_le_delta, gap parity (I5), the (E5)/parameter-map
        arithmetic (P3.3'(i)), and the seed recurrence defining
        delta.

STATEMENT [audit repair, 3x-convergent MAJOR: the draft's "every
realized class of size >= 2 is middle-rigid" is FALSE in the model
-- each gap-step boundary realizes one size-2 class with distinct
middles (~ln x/2 such classes at scale x, verified computationally
by the audit at 1e6/5e6/1e8); the clause is weakened to what the
verification proves, and the conclusions are unchanged]. There is
a deterministic sequence (a "gap system") which satisfies every
fact in T -- verbatim, with the same constants -- and in which, at
s = 0 and every large x at the D0 parameters, every realized class
OUTSIDE a transitional subfamily of total site mass
O(L ln x) = o(|S'_x|) is middle-rigid, so that, at the selection
d_P = argmax_d N_{P,d} (majority middle),
    sum_P (N_{P,d_P} - 1)_+ >= (1 - o(1)) |S'_x|
and Q(x,0) >= (1 - o(1)) |S'_x|. (s = 0 suffices: both targets
carry forall-s inside forall-x, so failure at s = 0 for one fixed
eps refutes them.) Consequently RelExtensionUpper and B2.pairs are
not logical consequences of T: any proof of either must consume at
least one input OUTSIDE T -- precisely, an input that FAILS in
this model. The salient family of such inputs is the middle-slot
distributional statements (NI-M2/NI-M4 shapes); the
characterization is failure-in-model, not middle-slot-ness [audit
repair: the SCOPE's own Maynard example is a non-middle-slot
input that also fails in the model].

CONSTRUCTION AND VERIFICATION. Define q_1 = 2, q_2 = 3, q_3 = 5,
q_4 = 7, and for n >= 4:
    q_{n+1} = q_n + 2 ceil( ln(q_n) / 2 ).
(An even-gap Cramer-smooth recursion.) Facts checked:
  (1) Growth: g_n := q_{n+1} - q_n = ln q_n + O(1), so q_n =
      (1 + o(1)) n ln n (standard comparison with the ODE
      y' = ln y; U20.5 write-out grade), hence the counting
      function pi_q(x) = (1 + o(1)) x/ln x: (T-c) PNT holds.
      Chebyshev: sup_n q_n/(n ln(n+2)) = q_1/ln 3 = 2/ln 3 =
      1.8205..., attained at the SHARED datum q_1 = p_1 = 2 --
      exactly the primes' own n = 1 requirement -- and
      q_n/(n ln(n+2)) -> 1 [audit repair: the draft's "C_0 >= 2"
      numeral replaced by the exact value]: the bound
      q_n <= C_0 n ln(n+2) holds for every n with any C_0
      admissible for the primes, so (I4) holds with the same
      constant.
  (2) Tails: delta_n = sum_j g_{n+j} 2^{-j} = g_n + O(1) =
      ln q_n + O(1): P3.2's conclusion sum_{n<=N} delta_{n+r}
      <= 13 C_0 N ln N holds with vast room; two_le_delta holds
      for ALL n >= 1 by the one-line argument: every gap at gap
      index >= 2 is >= 2 (even positive), and delta_n consumes
      only gap indices >= n+1 >= 2, so delta_n >= sum_j 2*2^{-j}
      = 2 [audit repair: the draft's "glued initial values"
      appeal replaced]; (T-e) holds.
  (3) Filters at the D0 pin: window sums = L(ln q_n + O(1)) <=
      A' L ln x for all q-sites with q_{n+L} <= x (A' = 1.5 > 1);
      delta caps hold with room (D ~ 624 C_0 ln x >> ln x);
      hence S' loses only the threshold/edge sites: retention
      (T-d) holds, |S'^{(s)}| = N - s - O(L) >= N/4.
  (4) Words and rigidity: g_n = 2 ceil(ln q_n / 2) is a step
      function of n, constant on runs where ceil(ln q_n/2) is
      constant; the number of distinct gap values up to x is
      <= ln x / 2 + O(1). Within a constant run, every site's
      word is the constant word (g, ..., g): these classes are
      middle-rigid by construction. Sites whose window straddles
      a step boundary number <= (ln x/2 + O(1)) L =: the
      TRANSITIONAL subfamily. SEPARATION (the load-bearing
      confinement, one line [post-repair audit addition]): g_n is
      nondecreasing in n, so a site whose side pair is
      (g^J, g^K) has its middle squeezed between g and g to
      exactly g -- every class containing a run-interior member
      is therefore rigid, and every NON-rigid class consists of
      straddling sites only, with total site mass bounded by the
      transitional count O(L ln x). Transitional classes indeed
      need not be rigid: each boundary g -> g+2 whose adjacent
      runs exceed the depths realizes the side pair
      (g^J, (g+2)^K) at exactly two consecutive sites with
      middles g and g+2, a non-rigid size-2 class (~ln x/2 such
      classes at scale x; audit-verified computationally at
      1e6/5e6/1e8, e.g. 7 of them at 1e8 at the pin depths --
      the earliest short runs realize none) [audit repair: the
      draft's universal rigidity clause is false; this is the
      exact non-rigid population]. With #classes <=
      (ln x/2 + O(1))(L + 1) = O(L ln x), at the argmax
      selection,
      sum_P (N_{P,d_P}-1)_+ >= |S'| - #classes - O(L ln x)
        = (1 - o(1)) |S'|,
      and likewise Q(x,0) >= (1-o(1))|S'|: both targets FALSE.
      (Audit note: an alternative construction -- insert a
      single-site run of the intermediate gap value at each
      boundary -- makes every size->=2 class literally rigid at
      the price of re-checking (T-c); recorded as an option, not
      executed: the hedged statement above is what the barrier
      needs.)
  (5) Finite-scale extension: replacing the recursion's start by
      the actual primes up to any fixed x_0 chosen ABOVE every
      measured window datum (e.g. x_0 = 2e10, clear of the 1e10
      stretch certificates' window tails [post-repair audit
      precision]) and running the recursion beyond changes
      nothing above: every FINITE-SCALE corpus fact (the m1-m5
      tables, the continuity records, the stretch certificates)
      also holds in the glued system, so adjoining any finite
      set of measured facts to T does not restore derivability.

SCOPE (B1 discipline; located obstruction, no impossibility). The
barrier is relative to the NAMED list T. It does NOT say
RelExtensionUpper is unprovable; it says every proof must consume
an input about the primes that FAILS for the smooth model -- e.g.
any middle-slot equidistribution/upper-uniformity statement (the
NI-M2/NI-M4 shapes), a second-moment gap statistic (present in
the anchored literature shelf only as the Montgomery-
Soundararajan record, dossier/literature.md; not an unconditional
corpus TOOL at word grain, and itself Cramer-model-defying in its
own abstract [audit repair: corpus-status wording]), or a
bounded/small-gap input (Maynard-class 1311.4600, in the anchored
corpus; it FAILS in the model -- all model gaps -> infinity --
but its quantitative cost at growing rank is superpolylog: priced
in sheet row T6 M3(c) [audit repair: the row now exists], so it
does not by itself extend T's reach at exchange depth). The
barrier also explains E1 structurally: T cannot see CRT alignment
either; any route through T alone was bound to be
alignment-blind, confirming that the aligned population is a
feature the eventual proof input must carry.

----------------------------------------------------------------
## What was attempted and where each attempt stands (route log,
## rule-16(a) support classes attached)

  A3.card (C1)                      PROVED (asymptotic; consumed
                                    inputs I1-I5, dossier grade)
  M1.a falsity (C2)                 PROVED (same grade)
  V2 floor (C2 remark (c))          PROVED (same grade)
  B2.pairs => REU (C3)              PROVED (elementary; no consumed
                                    analytic input beyond I1)
  Barrier (C4)                      PROVED (elementary model
                                    construction + fact checks)
  B2.pairs itself                   OPEN (U20.1); supported by m2/m3
                                    direction (measured, direction
                                    only) and the F17.2 room
                                    (heuristic); obstructed routes:
                                    union sieve (T1 trap row,
                                    superpolylog), identity layer
                                    (C4), Selberg/dispersion lanes
                                    (NI-M2/NI-M4, named)
  RelExtensionUpper itself          OPEN (the run's target; (S-)
                                    verdict with the above as the
                                    partial-progress record)
