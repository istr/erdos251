# C1 stress-test: duality / role reversal attack on CLAIM-A1

Status: attack executed and CLOSED. Verdict: CLAIM-A1 NOT falsified from
this angle; angle C1 is moreover provably sealed for the entire class of
bridges the assignment names ("exact mod-1 bridges with controlled error
terms that stay in the lattice"). Author: C1 subagent, 2026-07-17.
Numerics: c1_numerics.py (same directory); all exact identity checks pass
in exact rational arithmetic; PSLQ exclusions at ~4200-bit precision.

Notation as in chain-v1.md: p_n = n-th prime, g_n = p_{n+1} - p_n,
S = sum_{n>=1} p_n 2^{-n}, delta_n = sum_{j>=1} g_{n+j} 2^{-j},
delta_{n+1} = 2 delta_n - g_{n+1}; if S = a/(2^s b), b odd, then
b delta_n in Z for n >= s (chain-v1 Lemma 2.3). pi(m) = #{p <= m}.
Role-reversed constants: T := sum_p 2^{-p} = sum_m 1_P(m) 2^{-m}
(binary digits of T are literally the prime indicator), and
U := sum_{m>=1} pi(m) 2^{-m}.

--------------------------------------------------------------------
## 1. Exact duality identities (all PROVED, all machine-verified)

(I1) TRANSPOSE FORM OF S:
        S = sum_{m>=0} 2^{-pi(m)}.
     Proof: Fubini on S = sum_n 2^{-n} #{m : 1 <= m <= p_n}
     = sum_{m>=1} sum_{n > pi(m-1)} 2^{-n} = sum_{m>=1} 2^{-pi(m-1)}.
     Finite exact form verified (c1_numerics.py, I1):
        sum_{m=0}^{p_{N+1}-1} 2^{-pi(m)} = S_N + p_{N+1} 2^{-N},
     S_N the N-th partial sum of S. So S IS an integer-indexed series --
     but the integer index m enters only through pi(m) in the EXPONENT.

(I2) ABEL PAIR FOR U (the assignment's identity, verified exactly):
        sum_{m=1}^{M} pi(m) 2^{-m} = 2 sum_{p <= M} 2^{-p} - pi(M) 2^{-M},
     hence U = 2T in the limit. pi as digit VALUE pairs with T, never
     with S.

(I3) LARGEST-PRIME-BELOW SERIES (p_{pi(m)} = largest prime <= m):
        sum_{m=2}^{M} p_{pi(m)} 2^{-m} + p_{pi(M)} 2^{-M}
        = 2 sum_{n <= pi(M)} (p_n - p_{n-1}) 2^{-p_n}   (p_0 := 0).
     Verified exactly. Everything lands at value-scale positions p_n;
     S never appears.

(I4) TAIL OF THE TRANSPOSE FORM: for p_n <= M < p_{n+1} (n = pi(M)):
        sum_{m > M} 2^{-pi(m)} = 2^{-n} ( (p_{n+1} - 1 - M) + delta_n ).
     Verified exactly at truncated level.

(I5) COMPOSITION COLLAPSE: sum_n pi(p_n) 2^{-n} = sum_n n 2^{-n} = 2,
     rational independently of all prime data -- the composed identity
     pi(p_n) = n carries no information into the lattice.

--------------------------------------------------------------------
## 2. Attempt A: congruence family of the transpose form (I1)

Rationality q S in Z (q = 2^s b) applied to (I1) gives, for every M, the
tail congruence q sum_{m>M} 2^{-pi(m)} == -q head_M (mod 1). By (I4),

    q * tail_M = 2^{s-n} [ b (p_{n+1} - 1 - M) + b delta_n ].

The new integer parameter M (position INSIDE the run of constant pi)
contributes b(p_{n+1}-1-M), an integer -- lattice-trivial. What remains
is b delta_n in Z: THE SAME translated family, reparametrized.

PRECISE FAILURE SENTENCE (Attempt A): the duality S = sum_m 2^{-pi(m)}
is a change of summation variable, not of arithmetic content; its
induced congruence family is identical to {b delta_n in Z}, the intra-run
offset entering mod 1 only as the integer b(p_{n+1}-1-M). No second
family arises.

--------------------------------------------------------------------
## 3. Attempt B: Abel/partial-summation bridges S <-> T, U

Identities (I2), (I3) are exact and PURELY on the value-scale side: every
term has weight 2^{-m} or 2^{-p_n}. Identity (I1) is exact and purely on
the index-scale side (weights 2^{-n}, exponents pi(m)). This is forced:

WEIGHT-PRESERVATION FACT. Abel summation and Fubini interchange over the
incidence sets {(n,m) : m <= p_n} or {(n,m) : p_n <= m} preserve the
weight attached to each variable. To obtain S as a marginal one must
take c_{n,m} = 2^{-n} 1_{m <= p_n}, whose other marginal is (I1); to
obtain T or U one must take c_{n,m} = 2^{-m}-weighted kernels, whose
other marginal is (I2)/(I3). The unique kernel converting index-scale
weight into value-scale weight is the diagonal ratio 2^{n - p_n}, with
2-adic valuation n - p_n -> -infinity.

Concretely, the boundary term of every partial summation between the two
sides is pi(M) 2^{-M} (or p_N 2^{-N}): a quantity whose archimedean size
is the TARGET's digit scale but whose q-multiple has 2-adic denominator
2^{M-s}, exponentially finer than the resolution 2^{-n} (n = pi(M)) at
which rationality of S quantizes anything.

PRECISE FAILURE SENTENCE (Attempt B): every Abel/Fubini bridge between
q S and an integer-indexed prime series has boundary term pi(M) 2^{-M}
(equivalently kernel 2^{n-p_n}), which is not lattice-quantized: the
S-lattice has resolution 1/(b 2^n) while the term lives at scale
2^{-p_n}, and mod-1 information does not survive division by
2^{p_n - n} (x in (1/q)Z does not imply x/2 in (1/q)Z).

--------------------------------------------------------------------
## 4. Attempt C: Mobius/Lambert bridge (multiplicative structure on
## positions of the integer-indexed side)

TaTe's series has the Lambert form sum_n omega(n) z^n =
sum_p z^p/(1-z^p): the coefficient omega = 1 * 1_P (Dirichlet
convolution of the constant 1 with a BOUNDED, PRIME-SUPPORTED function),
which is precisely why omega(pn) = omega(n) + 1 - 1_{p|n} is exact and
the digit value is additive under argument dilation. Try the same for S:
define f := mu * p, so p_n = sum_{d|n} f(d) (verified: check for
n <= 39) and formally S = sum_d f(d) 2^{-d}/(1-2^{-d}).
Computed values (c1_numerics.py): f(1..24) = 2, 1, 3, 4, 9, 7, 15, 12,
18, 17, 29, 20, 39, 25, 33, 34, 57, 30, 65, 38, 53, 47, 81, 40, with
f(d)/p_d in [0.44, 0.98] for 18 <= d <= 24: f is UNBOUNDED and has FULL
support, not prime support. The dilation correction for the coefficient
function is c(pn) - c(n) = p_{pn} - p_n ~ (p-1) n ln n: unbounded, and
possessing no exact closed form (p_{2n} ~ 2 p_n is asymptotic only).

PRECISE FAILURE SENTENCE (Attempt C): the Lambert/Mobius rewriting
exists formally but its kernel f = mu * p is unbounded with full
support, so the digit value p_n is NOT additive-with-bounded-correction
under any argument dilation; the TaTe absorption step (5.2) has no
counterpart because p_{pn} - p_n is unbounded and admits no exact
identity.

--------------------------------------------------------------------
## 5. Attempt D: Legendre/Meissel dilation identities for pi

pi DOES satisfy exact dilation-type identities: Legendre's
pi(x) = pi(sqrt x) - 1 + sum_{d | P(sqrt x)} mu(d) floor(x/d), which
expresses pi at an argument via floors of DIVIDED arguments -- formally
the right shape for a (5.2)-analogue. But:
 - In the series where pi appears LINEARLY as digit value (U = 2T), the
   TaTe machinery has a potential target -- and nothing to prove: U = 2T
   is UNCONDITIONALLY irrational (Section 6, Lemma 1), and rationality
   of S supplies no congruence family for U (Attempt B).
 - In the series tied to S (transpose form (I1)), pi sits in the
   EXPONENT: Legendre's additive decomposition of pi(m) acts
   MULTIPLICATIVELY on the term 2^{-pi(m)} =
   prod_d 2^{-mu(d) floor(m/d)}, and the rationality lattice (1/q)Z is
   an additive group not closed under such factorizations; membership
   q sum_m 2^{-pi(m)} in Z does not decompose over the sieve terms.

PRECISE FAILURE SENTENCE (Attempt D): the only exact dilation identities
available on the C1 side (Legendre/Meissel) act additively on pi, hence
linearly only in the series U = 2T whose rationality is not supplied
(and is in fact false); in S itself pi is in the exponent, where those
identities act multiplicatively and the additive lattice (1/q)Z gives
them no purchase.

--------------------------------------------------------------------
## 6. Closure of the angle: two lemmas

LEMMA 1 (the target side is explicit and cannot receive constraints).
(a) T is irrational, elementarily: its binary digit string is 1_P; if
1_P were eventually periodic with period P beyond M, any residue class
c (mod P) containing one prime > M would consist entirely of primes
beyond M; but a(1+P) == a (mod P) and (1+P)^2 == 1 (mod P) provide
arbitrarily large composites in every class. Aperiodicity => T
irrational. (Same for U = 2T and the (I3) constant.)
(b) Any SINGLE exact lattice constraint on T is already full
rationality: if q' sum_{h>=1} 1_P(m+h) 2^{-h} in Z for even one pair
(q', m), then 2^m q' T in Z, i.e. T rational -- false by (a).
Consequently a transferred congruence family on the integer-indexed side
cannot be nontrivial-but-true: ANY true exact bridge from "S rational"
to a T-side lattice statement refutes the hypothesis outright, i.e. IS a
complete irrationality proof of S. Angle C1's success condition is not
"feed TaTe's engine" but "prove Erdos 251 in one line"; correspondingly
no elementary mechanism can supply it (Lemma 2).

LEMMA 2 (product-formula annihilation of lattice-controlled bridges).
Let z in Z[1/2], z != 0. Then |z|_R * |z|_2 >= 1 (write z = a/2^k with a
odd: |z|_2 = 2^k, |z|_R >= |a|/2^k >= 2^{-k}). Now suppose a bridge
identity presents a T-side tail as (S-side lattice element) + E where
the error E is REQUIRED (as in the assignment: "controlled error terms
that stay in the lattice") to lie in the S-lattice (1/(b 2^k))Z at some
resolution k, while doing its job archimedeanly, |E| < 2^{-p_n}, at a
target position p_n with p_n > k + log2 b. Then bE in Z[1/2] and
|bE|_R * |bE|_2 < b 2^{-p_n} * 2^k < 1, forcing E = 0; and E = 0
reduces the bridge to an exact T-side lattice statement, false by
Lemma 1(b). Since Abel summation, Fubini, telescoping, and Mobius
inversion produce UNCONDITIONAL identities (true independently of the
rationality of S), any exact bridge they produced would be an
unconditional proof that T is rational. Hence: no unconditional
rearrangement identity can transport the S-lattice to the
integer-indexed side; in every true identity the connecting term either
exits the lattice (Attempts A-D name it each time: the intra-run
integer, the boundary term pi(M) 2^{-M}, the kernel 2^{n-p_n}, the
unbounded correction p_{pn} - p_n, the multiplicative sieve
factorization) or exceeds the lattice spacing and carries no mod-1
content.

Numerical support (not needed for the lemmas, flagged as numerics): a
hidden exact linear or bilinear relation between the two sides would
also constitute a bridge; PSLQ at ~4200-bit precision excludes integer
relations c_0 + c_1 S + c_2 T = 0 with |c_i| <= 10^50 and
relations over {1, S, T, ST, S^2, T^2} with coefficients <= 10^25
(c1_numerics.py). [Numerical exclusion, not proof.]

--------------------------------------------------------------------
## 7. Secondary obstruction (sparsity), for completeness

Even if the family {b delta_n in Z} were transported verbatim through
the position map n -> p_n onto the target expansion, the constraints
would land on the density-zero position set {p_n} (density ~ 1/log m).
TaTe's amplification consumes the translated family at EVERY offset n
and the dilated family at every (n, p | n) with an algebraically free
second parameter; a density-zero, configuration-tied family cannot feed
the Hilbert-cube alternating sum (this mirrors the gating obstruction
already on record for chain-v1 Lemma 2.4, steering notes section 6).

Reverse direction (transport T's KNOWN irrationality back to S): the
only unconditional content of T's aperiodicity is that the gap sequence
(g_n) is not eventually periodic. Rationality of S does not assert
periodicity of (g_n) -- only of the carry-convolved digit stream of S,
and the unbounded carries (g_n ~ ln n > 1 eventually forces perpetual
carrying) decouple digit periodicity of S from periodicity of gaps. The
delta lattice is exactly the surviving invariant; nothing new comes
back.

--------------------------------------------------------------------
## 8. Verdict

CLAIM-A1 SURVIVES angle C1, strengthened: within the assignment's own
class of mechanisms (exact mod-1 bridges with lattice-controlled
errors), a bridge PROVABLY does not exist unless it is itself a
complete irrationality proof, and no unconditional rearrangement
identity (Abel, Fubini, telescoping, Mobius/Lambert, Legendre sieve)
can be one.

THE PRECISE FAILURE SENTENCE (deliverable): every C1 bridge between
q S = q sum_{m>=0} 2^{-pi(m)} and the integer-indexed prime series
(T = sum_m 1_P(m) 2^{-m}, U = sum_m pi(m) 2^{-m} = 2T,
sum_m p_{pi(m)} 2^{-m}) loses exactness at the boundary term joining
index-scale to value-scale weights -- pi(M) 2^{-M}, equivalently the
conversion kernel 2^{n - p_n} -- a term that would have to lie in the
S-rationality lattice (1/(b 2^n))Z while having archimedean size below
the target digit scale 2^{-p_n}; by the product formula on Z[1/2]
(|z|_R |z|_2 >= 1 for z != 0) the only such element is 0, and E = 0
would make the bridge assert rationality of T, which is unconditionally
false (aperiodicity of the prime indicator); hence the translated
family {b delta_n in Z} remains the ONLY exact congruence family
reachable through the C1 dualities, exactly as CLAIM-A1 asserts.

Positive spin-offs for the project ledger:
 1. New exact identity S = sum_{m>=0} 2^{-pi(m)} (finite form
    sum_{m=0}^{p_{N+1}-1} 2^{-pi(m)} = S_N + p_{N+1} 2^{-N}), with tail
    formula (I4); harmless here but possibly useful to other angles.
 2. Sharpened win condition: ANY exact S->integer-indexed transfer, if
    one is ever proved by non-elementary means, immediately proves
    Erdos 251 via the elementary irrationality of T -- no TaTe
    machinery needed. The target side is explicit; the entire
    difficulty is the bridge, and elementary bridges are dead by
    Lemma 2.
 3. PSLQ exclusion of low-height linear/bilinear relations between S
    and T (heights 10^50 / 10^25 at 4200 bits).
