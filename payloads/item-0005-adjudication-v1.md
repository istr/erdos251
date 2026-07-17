# item-0005 adjudication v1 -- two adversarial reviews vs. verdict

Date: 2026-07-17. Author: steering (analytics side), against
dossier/tate-transfer.md @ e16306f (branch tate-transfer-verdict).
Inputs: review R1 (Fable, fresh instance, falsification attempt no. 7,
payload = verdict + TaTe only) and review R2 (ChatGPT, cross-family,
same payload). Steering's own independent checks this session: Lean
structural correspondence (fork_merge_contradiction, ForkMerge.lean:50,
clause-by-clause match to EXCH); depth-supply reconstruction
(Chebyshev/Markov/pigeonhole at J ~ log x/loglog x); by-product
identity sum_{m>=1} 2^{-pi(2m)} = S/2 - 3/4 re-derived; TaTe anchors
(5.1)-(5.8), Lemma 5.2 via [53,(11.7)], Thm 3.1 consumption at
(5.42)-(5.45), Remarks 4.2 third bullet -- three-way convergent
(dossier, R1, steering first read); Maynard 1405.2593 anchors verified
first-hand this session (Thm 3.3 incl. diameter clause and
(2q)^{-exp(Cm)} density; Section 3 limitation remark + footnote 1).

## 1. Headline adjudication

The two reviews do not contradict each other; they answer different
questions. R1 answers "is the mathematics right?" -- YES, and it
supplies sharpenings. R2 answers "does the mathematics cover the
verdict as worded?" -- NO: the covered claim is strictly narrower than
the announced one. Both are correct. The mathematical core now has
three independent confirmations (executor proofs; R1 re-derivations
incl. the delicate 2^{J+1} divisibility; steering's Lean/manual
checks). R2 challenges no core computation; it challenges scope
wording, and four of its five hits are sustained as WORDING defects
with the intended (narrower) claim already present in the text.

## 2. Point-by-point

P1. Verdict header "THE METHOD DOES NOT EXTEND" and O2 header "why no
    repair exists". R2 SUSTAINED. Covered by the evidence: "no
    verbatim transfer is exhibited; the linear formal layer is fully
    classified (rigidity); every examined nonlinear architecture
    funnels into EXCH-type requirements; no unconditional transfer
    plan exists in the eight texts". Not covered: a no-go over all
    possible reductions. NOTE (process): the kickoff explicitly
    deferred the obstruction-not-impossibility language discipline to
    the write-up stage ("not here"); the review caught exactly the
    deferred discipline. Steering kickoff defect; see Section 5.

P2. O3 "an exact count<->value bridge is impossible outright".
    R2 SUSTAINED as worded -- the dossier's own C1 by-products
    (S = sum_m 2^{-pi(m)}; sum_m pi(m)2^{-m} = 2T) are exact bridges
    as identities, and steering re-derived a third
    (sum 2^{-pi(2m)} = S/2 - 3/4). The intended and correct claim
    stands one clause later in the same paragraph: any
    RATIONALITY-TRANSFERRING bridge in the product-formula class
    would already prove #251 (T is trivially irrational). Substance
    unharmed -- R2 itself concedes the identities are "possibly not
    analytically strong enough", and neither reviewer found a
    transfer path around the unbounded kernel 2^{m-pi(m)}. Fix:
    delete the absolute sentence; define the bridge class formally
    (the transfer-lemma object), keep the closure statement.

P3. O3 interface sentence "Every series the engine can digest has
    numerator covariant under argument division by primes".
    R2 SUSTAINED. Theorem 3.1 classifies no numerators; TaTe feed it
    only auxiliary completely multiplicative sieve indicators at
    (5.43)-(5.45) -- a fact the dossier itself states one sentence
    earlier, and which R1 verified. The sentence describes the KNOWN
    reduction architecture, not the interface. Fix: reword as "every
    known reduction reaching the engine does so through
    additivity-type covariance; the interface itself excludes
    nothing; no alternative reduction of S terminating in admissible
    auxiliary correlations is exhibited, and the examined ones funnel
    into (E2)". Same fix for the "(loglog x)-point control" clause:
    claim it for the examined reductions only (R2's cube-order
    observation -- formal term count is not correlation order -- is
    correct and consistent with TaTe's own architecture).

P4. O4 "THE WALL IS CLAUSE (E2) ALONE" / summary "residual gap is
    exactly (E2)". R2 SUSTAINED as a necessity claim: EXCH is proved
    sufficient; necessity is not proved and must not be asserted.
    CONSTRUCTIVE GAIN adopted from R2: the weighted generalization --
    after a prefix argument forces delta_t = delta_u, ANY
    configuration with |sum_{i<=L} (g_{t+i}-g_{u+i}) 2^{-i}| >
    2^{-L} |delta_{t+L} - delta_{u+L}| contradicts; Hamming-distance-1
    is the normal form, not the definition. Steering verified this
    against chain-v1 Lemma 2.2. v2 shall state EXCH' with (E2')
    (dominant weighted word difference at matched context) and note
    that R1's contraposition gives the correct framing: WITHIN the
    lattice layer, rationality forces sandwich rigidity at typical
    matched-flank pairs, so a tail-dominant word difference at
    matched context is the only contradiction lever available there
    -- exactness holds relative to the lattice layer, not globally.
    The three supply blockers (pigeonhole variability-blindness;
    parity block on prescribed patterns -- Maynard Section 3 remark
    verified, to be cited as a statement about the unconditional TOOL
    CLASS, not about the primes, per R2's caveat; Shiu circularity)
    apply verbatim to (E2'); v2 shall say so explicitly.

P5. EXCH computation detail. R2's |d_1| <= 1 observation: SUSTAINED
    against the dossier's proof PROSE (which asserts < 1 without
    stating the lower tail bound); the sharp form is R1's and the
    Lean kernel's: delta >= 2 unconditionally, hence
    |Delta_end| <= 2^K - 2 < 2^K. R2's parity patch (|d_1| >= 2) is
    also valid. One-line fix; no mathematical damage.

P6. O2 closure scope. R2's polynomial-consequence dilemma: SUSTAINED
    as a scope restriction -- the rigidity classifies the LINEAR
    formal layer; products of lattice constraints are integer but are
    not linear gap functionals and are not classified. v2 shall carry
    the explicit scope sentence and shall NOT claim a nonlinear
    no-go; the nonlinear evidence remains the funnel finding (every
    examined nonlinear architecture, incl. translation cubes = K-fold
    difference operators with digit coefficient identically 1 (R1
    angle 1, matching O2's own rank-1 observation), lands in
    EXCH-type requirements). R2's formal complaint about "closed
    Z-span" without topology: fix by stating the space (coefficientwise
    limits of finite integer combinations, the sense actually used).

P7. R1 sharpenings ADOPTED for v2 (all steering-verified): the
    one-generator observation (b delta_s in Z forward-generates the
    whole family; rationality supplies exactly one lattice bit, all
    else is translation); tail periodicity b delta_n == 2^{n-s}
    b delta_s (mod b); the [2, 2^K] end-tail bound; the
    contraposition framing of (E2).

P8. Anchor register. All dossier anchors challenged by neither
    review; steering verified first-hand: TaTe (5.1)-(5.3), (5.7)
    (h-k) structure, Lemma 5.2 [53,(11.7)], Thm 3.1 usage
    (5.42)-(5.45), Remarks 4.2 third bullet; Maynard Thm 3.3
    (diameter clause, (2q)^{-exp(Cm)}), Section 3 limitation +
    footnote 1. R1's four "unverifiable" residuals are closed by
    steering's text access; the only one requiring action is the
    bridge-lemma formalization (P2).

## 3. Required revisions for tate-transfer.md v2 (complete list)

1. Verdict header -> "NO UNCONDITIONAL TRANSFER EXISTS IN THE
   EVIDENCE BASE, AND THE FAILURE IS STRUCTURAL" + one-sentence scope
   statement (verbatim-transfer refuted; linear layer classified;
   examined architectures funnel into (E2'); no all-reductions no-go
   claimed).
2. O2 header "why no repair exists" -> "why the formal linear layer
   admits no second family"; add the scope sentence of P6; specify
   the closure topology.
3. O3: delete "impossible outright"; insert formal bridge-class
   definition; keep and foreground the would-prove-#251 closure.
4. O3: reword the interface sentence and the (loglog x)-point clause
   per P3.
5. O4: state EXCH' with (E2'); demote (E2) to normal form; replace
   "ALONE"/"exactly" by lattice-layer-relative exactness via the
   contraposition; extend the three blockers to (E2') explicitly;
   recast the Maynard citation as a tool-class statement.
6. EXCH proof prose: insert delta >= 2 and |Delta_end| <= 2^K - 2.
7. Add R1's one-generator sharpening and tail periodicity to O2;
   credit both reviews in a review-response section; register the
   two reviews as payloads with sha256 in payloads/HASHES.txt.
8. Summary sentence: rewrite to the covered claim; BET-07 paragraph
   unchanged (evidence AGAINST unconditional progress -- both
   reviews concur; R2's "understanding progress" framing matches).

## 4. Recommended verdict wording (v2)

"No unconditional transfer of the TaTe method to S exists in the
eight-text evidence base, and the failure is structural: the
(5.1)-layer transfers verbatim, the (5.2)-derivation has no
p_n-analogue (no exact non-translational self-map of the prime-count
index), the linear formal layer of rationality consequences is fully
classified and dilation-free, and every examined repair architecture
-- seven adversarial angles across three independent parties --
terminates in the exchange-supply requirement (E2'), a two-site
word-correlation lower bound outside every unconditional technique in
the evidence base. Sufficiency of (E2') is proved (EXCH'); necessity
is claimed only relative to the lattice layer. This documents a
located obstruction, not an impossibility theorem."

## 5. Process findings (steering blind-spot register)

B1. Kickoff v1 deferred the obstruction-language discipline out of
    the verdict stage ("not here") although the verdict section was
    the review payload; the cross-family review then hit precisely
    the deferred discipline. Correct rule: the language discipline
    binds any section that leaves the session.
B2. Review-architecture finding worth codifying: same-family
    fresh-role review audited the computations constructively
    (re-derivations, a sharpening, a strict-inequality catch);
    cross-family review audited logical scope and found the
    overclaims. Complementary, not redundant; keep both roles.

## 6. Follow-up item candidates (described, NOT created)

F1. (E2')-supply as a research item: unconditional production of a
    tail-typical matched-flank pair with dominant weighted middle
    difference; owns the three blockers as its obstacle register;
    reference consumer item-0010 via EXCH'_1.
F2. EXCH'/EXCH Lean formalization as a FINDING-layer module (no
    chain-v1 change): the finite kernel exists sorry-free
    (fork_merge_contradiction); the delta from it to EXCH' is small.
F3. Write-up positioning note: HLQuantA vs Pratt Conjecture 1.2
    incomparability (recorded earlier this session) + the
    #69-vs-#251 value/count dichotomy as the public framing.

## 7. Merge gate recommendation

Revise to v2 on the branch per Section 3; steering re-checks the
diff; then merge. The two review files enter payloads/ (hashed);
workpapers disposition per operator F5 decision.
