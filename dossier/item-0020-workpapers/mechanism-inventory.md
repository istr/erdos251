# item-0020 W1 -- mechanism inventory at statement grain
# (M1-M7; one page per mechanism; written BEFORE any proof step,
# per kickoff Section 3 W1; F18.3 binds: every B-input here is
# singleton-inert or states its reduction to the reduced form)

Vocabulary: RS.1-RS.4 of dossier/relext-statements.md at the D0 pin
(A' = 1.5, A'' = 48, D = ceil(13 C_0 A'' ln x), J = ceil(log2 D) =
K, L = J+1+K, k = L+1). W2, V2, cap_r per the W0 dictionary
(working-notes.md Section 5): W2 = C_words,off, V2 = C_sides,off.
TARGET consumed by every page: RelExtensionUpper (7.1 text, W0
Section 1), restricted-selection primary (FL-1). The FIXED-DELTA
gate (W0 Section 2) is the quantitative reading.

----------------------------------------------------------------
## M1 -- global pair counting (the designated lane; 7.5)

ANCHORED STATEMENT (kickoff Section 3 M1, consumed verbatim, then
refined NON-silently below): for nonnegative integers
(N-1)_+ <= N(N-1); summing over P at any selection,

    sum_P (N_{P,d_P} - 1)_+  <=  W2(x),

selection-free; since sum_P N_P = |S'^{(s)}_x| exactly (RS.1),
RelExtensionUpper follows from

    (M1.a)   W2(x) = o(|S'^{(s)}_x|)   uniformly in s.

What is bounded: the reduced selection sum, by the ordered
full-word-coincidence pair count. Quantifiers: forall s, one x_4 per
eps; selection eliminated by the sum-over-d majorant. Where o(ln x)
would come from: W2 carrying less than site mass. Singleton-inert:
YES ((N-1)_+ form; W2 vanishes on singleton cells).

STATEMENT-GRAIN AUDIT OF (M1.a) (recorded here, settled in W2/W3):
(M1.a) compares a PAIR count against a SITE count. The realized
full-word space has capacity |W_L| <= cap_L = ((eA'/2 + o(1)) ln x)^L
= x^{o(1)} (P3.3'(iv) pattern at r = L), while |S'^{(s)}_x| >= N/4
(TailIntersection at the pin). Cauchy-Schwarz on word fibers then
FORCES W2 >= |S'|^2/cap_L - |S'|, whose ratio to |S'| tends to
infinity. (M1.a) is therefore expected FALSE at the D0 depths -- not
by the sieve-constant trap but by pair-vs-site mass mismatch at
astronomical class multiplicities. W3 claim C2 proves this; F20
registration accompanies it. The lane does NOT die: the kickoff's
own relative hope ("full-word pairs against SIDE-collision pairs")
is the repair, in two steps:

    (M1.b) relative pair form: W2(x) <= eps V2(x) + eps |S'|.
    STATEMENT DEFECT (found at statement grain, before proof): (M1.b)
    does NOT imply RelExtensionUpper. Adversarial configuration:
    rigid mass hidden in N_P = 2 classes (where full-word pairs =
    side pairs per class, blind to eps) while V2 is inflated by one
    large non-rigid class. Quantified in sheet table T4 [audit
    repair: reference]; registered F20.2. Repair: normalize per
    class.

    (M1.c) = CANDIDATE B2.pairs (this run's refined lane statement;
    NEW, stated in the relext-statements.md candidate pattern):
    for every eps > 0 there is x_8(eps) such that for all
    x >= x_8, all s >= 0:

        sum over P in Fam(S'^{(s)}_x) of
          (1/N_P) * sum over even d >= 2 of N_{P,d}(N_{P,d} - 1)
        <=  eps * |S'^{(s)}_x|.

    (Division safe: N_P >= 1 on Fam. Selection-free; singleton-inert:
    the inner sum vanishes on N_P = 1. Constant dependence: none
    beyond the D0 pins. Normalization: counting ratio; no rho
    reference in the statement.) CONSUMPTION CLAIM (W3 claim C3):
    B2.pairs implies RelExtensionUpper -- unrestricted selections --
    with eps_REU = sqrt(eps), by the per-class inequality
    (max_d N_{P,d} - 1)_+ <= sqrt(N_{P,d}(N_{P,d}-1) summed over d)
    and one Cauchy-Schwarz with weights N_P. No per-word sieve
    constant, no rho, no class law is instantiated anywhere in the
    reduction: the F17.9-evading shape is preserved.

MANDATORY SHEET LINE (the known trap, carried): any upper bound on
W2 (or on B2.pairs' numerator) that sieves the UNION of the two
translated point sets pays a sieve constant at rank up to 2k:
exp((1+o(1)) 2k ln 2k), superpolylog -- the F17.9 wall one floor up.
Tabulated in budget_sheet_20 T1 [audit repair: was misdirected to
T2]. The heuristic room of the relative
step is ONE power of ln x (F17.2: (2 ln x)^M at M = 1); the trap
constant exceeds it superpolylogarithmically.

Where the o(ln x) comes from in the refined lane: the middle-slot
conditional collision rate ~ gamma-type/ln x among side-colliding
pairs (F17.2 room). What remains open: any unconditional upper
control of that conditional rate (see M7 for why its dimension is 1
and M2/M4 for why the available devices do not reach it).

----------------------------------------------------------------
## M2 -- relative Selberg weights for the extension/base ratio

TARGET INEQUALITY (statement grain): for P in Fam(S'^{(s)}_x) and
even d, bound the extension count relative to the base,

    N_{P,d}(x) <= (C_rel(x)/ln x) N_P(x) + 1,   C_rel = o(ln x),

per class or summed with mass weights (the +1 keeps it
singleton-inert; equivalently state on (N_{P,d}-1)_+). What is
bounded: the one-position extension count. By what: a Selberg
quadratic form either (route i) over the full word at rank k, or
(route ii) over the extension position only, relative to the class.

WALL w1 DISCHARGE (mandatory at statement grain, kickoff W1): the
span hypothesis of oneExtension_sum_le (span <= kappa (k-1) ln(k+1))
is NECESSARY (its docstring exhibits the unrestricted form as false:
ratio sum growing like the span). The D0 window budget is A' L ln x,
larger by the factor ~ ln x/ln k (this run's sheet rows T6 M2(a),
5.9 -> 541 across the grid [audit repair: the draft cited the
item-0018 T5(b) reserve-ratio rows 101 -> 268, a different
quantity]). ESCAPE INVENTORY, stated before proof:
  (e1) restrict to small-span classes: covers a vanishing share of
       the realized family (realized spans concentrate at
       Theta(L ln x); m3 span data + P3.1' mean); the uncovered mass
       is 1 - o(1): not a route to the full statement, at most a
       subfamily contribution priced by the B3 ledger.
  (e2) route (i) at full rank k: per-word constant class
       exp((1+o(1)) k ln k) (T1 rows; D1.a documented outcome):
       F17.9 DOA -- D3(i) fails on the route.
  (e3) route (ii), Selberg relative to the base F_P: the quadratic
       form's main term requires the distribution of F_P in residue
       classes to level ~ the d-range -- a class-level
       equidistribution input (Bombieri-Vinogradov shape AT THE
       CLASS, growing rank). NAMED MISSING INPUT NI-M2: no such
       statement exists in the corpus (checked against the Section 2
       anchor list and the frozen HLQuantA text: HLQuantA is a
       lower-bound card, no upper/equidistribution content).
No fourth escape is claimed. Where o(ln x) would come from: the
dimension-1 local densities of the single extension point (correct
size ~ rho/ln x) -- the shape is right; the unconditional carrier is
absent. Selection handling: pointwise-in-d, so the adversarial
quantifier is free once the per-class bound holds on the capped
domain -- but the capped domain re-imports B1's (b1-rho)/floor
apparatus (F18.5, corrected T4) and m1 DROPPED B1's floor at
reachable x. Expected verdict: NO-GO(w1 + NI-M2), gaps quantified in
sheet rows M2(a)-(c).

----------------------------------------------------------------
## M3 -- averaging over side classes (order-of-summation devices on
## the exact identities of RS.1)

TARGET STATEMENTS (statement grain; this mechanism is the run's
unconditional engine -- it proves ABOUT the neighborhood of the
target, not the target):

  (M3.1) = CANDIDATE A3.card (asymptotic cardinality form of
  MatchedFlankLower; NEW): for every s >= 0 and x >= x_2(s):
      sum over P in Fam_2(S'^{(s)}_x) of N_P
        >= |S'^{(s)}_x| - cap_{J+K}
        >= (1/2) |S'^{(s)}_x|,
  with cap_{J+K} = ((eA'/2 + o(1)) ln x)^{J+K} = x^{o(1)} the
  P3.3'(iv) side capacity and the last step from TailIntersection at
  the pin (|S'| >= N/4). Quantifiers: delta = 1/2 s-UNIFORM; x_2(s)
  = max(x_7(s), x_cap) with x_cap s-free. Inputs consumed: RS.1
  partition identity; #singleton classes <= |Fam| <= cap_{J+K};
  P3.3'(ii)/(iv) [both PROVED at dossier level]. W3 claim C1.

  (M3.2) unconditional V2 floor (side-collision abundance):
      V2(x) >= |S'|^2/cap_{J+K} - |S'|,
  the P1(d) Cauchy-Schwarz floor read as a LOWER bound with the
  capacity in the denominator; V2/|S'| -> infinity. (Same device as
  the (M1.a) refutation, run on sides instead of words.)

  (M3.3) BARRIER (statement-grain; the mechanism's reach limit,
  proved as W3 claim C4): the identity layer -- RS.1 partition
  identities, the capacity bounds, the P3-family aggregate
  (Chebyshev/PNT/Markov) facts, and the C2 retention -- is invariant
  under per-class relabeling of middle values; a configuration
  that is middle-rigid outside a transitional subfamily of site
  mass O(L ln x) = o(|S'|) (an even Cramer-smooth gap model; see
  the W3 correction note below and the S1 audit repair in
  proofs.md C4) satisfies every fact in that list while violating
  RelExtensionUpper at the maximal order (LHS >= (1-o(1))|S'| at
  the argmax selection) [audit repair: the draft's universal
  rigidity and exact LHS = |S'| - |Fam| were false in the executed
  model]. Hence NO combination of tools from that named list
  alone proves RelExtensionUpper or B2.pairs; every route must
  consume at least one input that FAILS in that model -- the
  salient family being middle-slot distributional inputs [audit
  repair: failure-in-model characterization]. (B1 discipline:
  located obstruction against a NAMED
  tool inventory, no impossibility claim; in-corpus literature
  anchors (Maynard-type clustering) are priced separately in sheet
  row T6 M3(c) -- their k-uniformity cost is superpolylog at
  growing rank, so they do not extend the list's reach at the D0
  depths.)
  W3 CORRECTION NOTE (non-silent mutation, recorded): this page's
  original barrier sketch proposed a CONSTANT-gap model; that
  sketch violates the PNT/window-mean rows of the very list T it
  must satisfy (constant gap ~ ln x breaks Chebyshev at small n
  and PNT at all n). The executed model is the even Cramer-smooth
  recursion of proofs.md C4; the deviation is recorded here per
  the kickoff's non-silent-mutation rule.

Selection handling: none needed (all selection-free). Singleton-
inert: (M3.1) is an A-side statement (not a B-input); (M3.2)/(M3.3)
are pair/meta statements. Where o(ln x) comes from: nowhere -- this
mechanism cannot see the middle slot (that is the content of M3.3);
its role is the A-side constant delta = 1/2 for the 7.4 ledger and
the falsity/floor results that reshape the M1 lane.

----------------------------------------------------------------
## M4 -- bilinear / dispersion use of shared flank structure

TARGET INEQUALITY (statement grain; quantified [audit repair]):
for SOME explicit reference profile mu_P (a middle law) with
max_d mu_P(d) = o(1) uniformly over Fam: for every eps > 0 there
is x_9(eps) such that for all x >= x_9 and all s >= 0,

    Disp(x,s) := sum_P sum_d ( N_{P,d} - mu_P(d) N_P )^2
              <= eps^2 * |S'^{(s)}_x|,

whence
max_d N_{P,d} <= mu-max N_P + sqrt(per-class dispersion) and the
reduced sum is bounded by Cauchy-Schwarz (same consumption pattern
as M1.c). Selection handling: eliminated by the max/dispersion
majorant. Singleton-inert after the -1 bookkeeping (state on
(N-1)_+; dispersion of a singleton cell is <= 1 and must be absorbed
by the additive slack -- noted, the F18.5 lesson).

STATEMENT-GRAIN AUDIT: expanding Disp needs (a) the cross term
sum_P sum_d mu_P(d) N_{P,d} N_P -- a first moment against the
profile, and (b) the square term W2-type pair counts. Controlling
(a) at the main-term level is EXACTLY a mean value theorem for the
word-level counts (a tuple-level Bombieri-Vinogradov / dispersion
input at rank k ~ (2/ln 2) lnln x). Inventory against the corpus:
the arithmetic large sieve and BV apply to residue classes /
Dirichlet characters, not to word classes (no group structure on
side pairs); the S-moment tools anchored in D1.b (Kuperberg Thm
1.1/1.2, Pintz Lemma 4) are a full regime square away or
superpolylog (D1.b's documented conclusion, consumed verbatim).
NAMED MISSING INPUT NI-M4: an upper mean-value theorem for
N_{P,d}-masses at rank ~ k, span ~ A'L ln x, of strength
sum_P sum_d |N_{P,d} - model| <= |S'|/(ln x)^{1+eps'} -- nothing of
this shape exists unconditionally at growing rank (D3(ii): compare
frozen HLQuantA BY TEXT -- HLQuantA has no upper content; a
dispersion input at this rank is strictly beyond it). Where the
o(ln x) would come from [audit repair: mandated line was absent]:
the mu-profile's middle-law rate ~ rho-average/ln x -- the same
(2 ln x)^1 room as M1/M7; the room is fine, the CARRIER is what
is missing. Expected verdict: NO-GO(NI-M4); gap = the full
absence of an unconditional word-grain mean value theorem,
quantified against the (2 ln x)^1 room in sheet row M4(a).

----------------------------------------------------------------
## M5 -- local quotient control on a large favorable subfamily

TARGET (statement grain; B3 fallback shape, D5-ratified): one fixed
C_q with C_q(x)/ln x -> 0, an exceptional sub-family E of eps-mass,
and outside E the per-class bound

    N_{P,d} <= (C_q(x)/ln x) N_P + 1    (all even d <= A' L ln x).

Consumption price: 7.4(s3), eps_B3 <= delta/4 -- with (M3.1) landing
delta = 1/2, the price is eps_B3 <= 1/8, s-uniform.

DESIGN CONSTRAINTS (binding, from the kickoff Section 4): E1 -- the
realized population IS CRT-alignment-selected (rho medians ~10.5 vs
reference 2; full two-block alignment at p = 3, 5 in every top-10
profile; level grows with row depth); "favorable" may NOT be defined
as "typical rho". The C1 repair (MAJOR-4) binds by analogy: the
family rule must be EX ANTE and cap-blind -- a rho-threshold rule
F_fav(R) = {P : sup over in-window even d of rho(P,d) <= R(x)} is
admissible (word-data-only, outcome-blind); an "all middles
distinct" rule (the r2 diagnostic theta = 0 family) is NOT (it
conditions on the outcome the statement bounds).

STATEMENT-GRAIN AUDIT: two named inputs are consumed by any closure:
  NI-M5a (alignment-mass bound): sum over P outside F_fav(R) of N_P
      <= (1/8) sum_P N_P for some admissible R = o(ln x). Status:
      OPEN; empirical direction only (m3: top-decile rho classes
      carry ~10% of Fam_2 mass; but alignment level GROWS with
      depth, E1 -- the direction at coupled depth is unmeasured).
  NI-M5b (capped-domain middle law): the per-class bound above on
      F_fav(R) -- this is B1' on the (b1-rho)-capped domain, named
      open input OI-B1 (relext-statements 4.B), with the m1-measured
      caveat that B1-type truth windows are multiplicity-gated and
      empty at reachable x.
Where o(ln x) comes from: R(x) = o(ln x) via the cap. Singleton-
inert: the +1. Selection handling: pointwise in d, so adversarial
selections are covered on F_fav; E pays the ledger. Expected
verdict: CONDITIONAL(NI-M5a AND NI-M5b) -- a statement-shaping lane,
not a proof lane, in this corpus. Empirical note (E2, both-readings
duty): no exceptional sub-family exists on the measured range; the
fallback is asymptotically legitimate but not empirically motivated.

----------------------------------------------------------------
## M6 -- signed exclusion weights with positive final count

TARGET (statement grain): weights lambda(n) (signed, e.g.
Selberg-type squared out of a signed system, or Bonferroni/
inclusion-exclusion truncations) with

    sum_P (N^lambda_{P,d_P} - 1)_+ <= eps sum_P N^lambda_P    and
    N^lambda comparable to N on the needed family,

i.e. the exclusion runs against a weighted count whose final
positivity is part of the claim. SINGLETON-INERTNESS (F18.3
discharge [audit repair: the mandated statement was absent]): the
weighted (N^lambda - 1)_+ form is NOT automatically singleton-
inert (a singleton with lambda(n) > 1 contributes lambda(n) - 1 >
0); any executed M6 statement must either normalize lambda <= 1
sitewise or state its reduction to the unweighted reduced form
explicitly (e.g. via (N^lambda_{P,d_P} - max_n lambda(n))_+
bookkeeping) BEFORE proof. Where the o(ln x) would come from: the
dimension-1 signed system at the extension position (inheriting
M2 route (ii)'s answer -- and its missing carrier NI-M2).
STATEMENT-GRAIN AUDIT: the weight
system must (a) carry content outside the M3.3 tool list T --
middle-slot-sensitive weights being the salient case (else the
barrier applies
verbatim to the weighted identities), and (b) keep positivity after
truncation. Any lambda supported on word-level divisibility data
re-imports the rank-k (or rank-2k, pair level) truncation constants:
the Bonferroni/Selberg positivity price at rank r is the T1 constant
class exp((1+o(1)) r ln r) (D3(i) FAIL on the route, F17.9 verbatim
-- this is the wall's original home). Any lambda supported on
class-level data only is middle-blind and lands in M3 (merged there;
recorded, not silent). NAMED alternative: a signed system at the
SINGLE extension position (dimension 1, constants O(1)) -- this is
exactly M2 route (ii) and inherits NI-M2. Expected verdict:
NO-GO(F17.9 verbatim at word rank; else merges into M2/M3). No
mechanism-specific open input to name beyond NI-M2.

----------------------------------------------------------------
## M7 -- explicit one-extension specificity

TARGET (statement grain): exploit that exactly ONE position is free
relative to the base: the extension event {middle = d} given
membership in F_P is a ONE-point condition, local densities
nu-insert/p per RS.3's insert algebra, aggregate size rho(P,d)/ln x.
Candidate statement (the honest form of "specificity"):

    sum over P of N_P * ( share of F_P at its modal middle )
      <= eps sum_P N_P,

which IS RelExtensionUpper restated -- the mechanism contributes no
independent statement; it contributes the DIMENSION COUNT: the
relative step is dimension 1, so its correct constant class is O(1)
local factors (rho algebra, machine-checked per-insert:
nuMod_insert, log_singularFactor_insert_sub_le), NOT k-uniform
constants. What is missing is the CARRIER: to convert the
dimension-1 local densities into an upper COUNT bound relative to
F_P requires the base to be sieve-regular (equidistributed in the
relevant residue classes) -- the same NI-M2 input; without it the
specificity is a heuristic (U18.2's middle law: the mean-2 d-mean,
measurement target only, never load-bearing). CONTRIBUTION CONSUMED
BY THE RUN: M7 justifies the (2 ln x)^1 room row (F17.2) that makes
the M1.c/B2.pairs shape plausible with a full ln x margin on typical
mass, and E1/T4 bound its aligned-mass erosion ((ln x)^{-o(1)}
margin on aligned classes: sup rho = (ln x)^{1-o(1)}, RS.3). No
separate verdict: subsumed -- NO-GO as a standalone proof mechanism
(NI-M2 carrier absent), consumed as the room calculus of the M1
lane. Singleton-inert: inherited from the forms it feeds.

----------------------------------------------------------------
## Inventory summary (feeds W2)

  lane   statement                        expected verdict class
  -----  -------------------------------  -----------------------
  M1.a   W2 = o(|S'|)                     NO-GO (FALSE; W3-C2)
  M1.b   W2 <= eps V2                     NO-GO as consumer
                                          (insufficient; F20.2)
  M1.c   B2.pairs (normalized relative    REDUCED-target: GO for
         pair statement, NEW)             reduction proof (W3-C3);
                                          OPEN as a statement
  M2     relative Selberg                 NO-GO(w1 + NI-M2)
  M3     cardinality/averaging engine     GO (proves A3.card,
                                          floors, barrier; cannot
                                          reach the target: M3.3)
  M4     dispersion                       NO-GO(NI-M4)
  M5     B3 on rho-capped family          CONDITIONAL(NI-M5a,b);
                                          DEFERRED (no in-corpus
                                          proof surface)
  M6     signed weights                   NO-GO(F17.9)/merged
  M7     one-extension specificity        subsumed into M1 room
                                          calculus; NO-GO alone

Mechanism additions/merges are recorded here (M6 -> M2/M3 partial
merge; M7 -> M1 room calculus), per the kickoff's non-silent-mutation
rule; every NO-GO above becomes a REGISTERED F20.n only after its
sheet row (W2) and, where applicable, its W3 proof.
