# Review payload R1 -- adversarial computation audit (blind)

You are a fresh-instance reviewer. You receive EXACTLY two files:
this payload and the review object (an anchor-stripped mathematics
dossier about prime-gap "exchange configurations" for a binary-digit
irrationality program). You must NOT consult the web, and you must
NOT read any file other than the two you were given. Bracketed
tokens like [TEXT-A], [PIN-2], [PROOF-ASSISTANT] are deliberate
anonymizations; treat them as opaque names and do not attempt to
de-anonymize.

ROLE (computation audit, adversarial): attempt to REFUTE the
object's computations. Reading is not sufficient: you MUST
independently re-derive or re-execute, with your own scripts where
numeric, at least the following, and report your own values next to
the object's:

C1. The model collision constants (Section 3): q_2 = p/(2-p),
    q_3 = p^2/(3-3p+p^2), the 4/3 ratio, (2 ln x)^{J+K} = x^{o(1)}
    at the stated depths, the variance-block ratios, the matching
    floor, and the dyadic Borel-Cantelli step.
C2. The threshold algebra (Sections 3.3/4.0): the displays
    floor/C_words = (2 ln x)(4/A)^{J+K} (per-position) and
    (2 ln x)(4/(e A'))^{J+K} (aggregate); the threshold
    A' < 4 sqrt(2)/e; theta(A') = 1 - (2/ln 2) ln(e A'/4) and its
    stated values; the generalized form A'_crit = 2 sqrt(2)/
    (e gamma_2).
C3. The collision-constant computation (Section 4.3): compute the
    Euler product E = 4 C_2^2 prod_{p>2}(1 + ((p-1)^2/(p-2)^2 - 1)/p)
    yourself (own script, own prime generation) and check
    E = 4.601923...; verify the claimed direct-summation agreement
    is plausible by computing (2/D) sum_{even d <= D} S_2(d)^2 for
    some D of your choice >= 1e5; check gamma_2^crit = 2 sqrt(2)/e.
C4. The P1/P2/P3 displays (Section 2): the pigeonhole identity, the
    weighted-clause bridge including the factor-2 margin and the
    E-invariant example (2,8) vs (4,4), the Markov constants of
    P3.1/P3.2 (re-derive the majorant sum_{j>=1}(j+1)^2 2^{-j} = 11
    and the constant chains), the parameter-map self-consistency of
    P3.3 and P3.3'.
C5. The D1-L spot checks quoted in Section 4.1: the Delta >= 0.7543
    display, the constant-gap ratios ((8k+2)^k e^{-gamma k} vs
    2^k k!; (2 e^{1-gamma})^k = 3.057^k), and the in-regime error
    term k^2 lnln X/ln X = o(1) at k = (2/ln 2) lnln x.
C6. The inline certificates (Sections 7.1-7.2): from the printed
    prime lists, re-derive the gap words, verify the flank matches
    entry by entry, the middle differences, the (E5) gates
    (126 < 256, 125 < 256, 62 < 128), primality of at least four of
    the printed numbers (your own primality check), and the
    Lemma-2.2 subtraction identity residual at machine precision
    for at least one pair.
C7. Internal consistency: the verdict Section 1 claims vs the body
    (does every V-clause have a body section that proves or
    measures what it says; are scope qualifiers present where the
    body is heuristic/empirical).

FORMAT: findings listed by severity FATAL / MAJOR / MINOR / NOTE, each
with exact location (section + quoted line), your computation, and
the discrepancy; then an overall verdict (SOUND / SOUND WITH
REPAIRABLE ISSUES / UNSOUND) with a confidence in [0,1]. If a
computation of yours DISAGREES with the object, show the full
derivation. Absence of findings must be earned by shown work, not
asserted.
