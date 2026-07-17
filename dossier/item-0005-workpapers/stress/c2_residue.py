#!/usr/bin/env python3
# C2 numerics 3: verify RESIDUE-PINNING on a synthetic rational series:
#   if b delta_n is an EVEN integer (n >= s+1) and w = (g_{n+1},...,g_{n+J}),
#   A_w = sum_i w_i 2^{J-i}, then   b delta_{n+J} == -b A_w  (mod 2^{J+1}).
# (Rearranged Lemma 2.2 + Lemma 2.3 parity; this is the master family.
#  Slices: w == 0 mod 2^t runs -> divisibility; two sites same word ->
#  chain-v1 Lemma 2.4.)
# Also verify the PAIR-TRAP arithmetic on explicit numbers.

from fractions import Fraction
from math import lcm

prefix = [2, 4, 2, 6]
period = [16, 32, 48, 2, 4, 6, 10, 2]

def delta(n):
    L, P = len(prefix), len(period)
    def g(i):
        return prefix[i-1] if i <= L else period[(i - L - 1) % P]
    A = sum(period[j] * 2**(P - 1 - j) for j in range(P))
    Tper = Fraction(A, 2**P - 1)
    if n >= L:
        ph = (n - L) % P
        s = sum(Fraction(period[ph + j - 1], 2**j) for j in range(1, P - ph + 1))
        return s + Fraction(1, 2**(P - ph)) * Tper
    s = sum(Fraction(g(n + j), 2**j) for j in range(1, L - n + 1))
    return s + Fraction(1, 2**(L - n)) * delta(L)

def g_seq(i):
    L, P = len(prefix), len(period)
    return prefix[i-1] if i <= L else period[(i - L - 1) % P]

dens = {delta(n).denominator for n in range(0, 30)}
D = lcm(*dens); b = D
while b % 2 == 0: b //= 2
s_pow = (D // b).bit_length() - 1
print("b =", b, " s =", s_pow)

bad = 0
for n in range(s_pow + 1, s_pow + 20):
    for J in range(1, 12):
        w = [g_seq(n + i) for i in range(1, J + 1)]
        A_w = sum(w[i] * 2**(J - 1 - i) for i in range(J))
        lhs = (b * delta(n + J)) % 2**(J + 1)
        rhs = (-b * A_w) % 2**(J + 1)
        if lhs != rhs:
            bad += 1
print("residue-pinning checked over n in [s+1, s+19], J in [1,11]:",
      "ALL PASS" if bad == 0 else "%d FAILURES" % bad)

# pair-trap arithmetic on explicit numbers (pure arithmetic, no primes):
# b odd, H tail bound, choose J with 2^J > b*H; words w, w' identical except
# first gap +2  =>  A_w' = A_w + 2^J.  If both realized with end tails
# delta, delta' in (0, H], then b*delta == -b A_w and b*delta' == -b A_w - 2^J
# (mod 2^{J+1});  r in (0,bH] and r+2^J in (0,bH] mod 2^{J+1} are
# incompatible when bH < 2^J.  Exhaustive check for small parameters:
def pair_trap_incompatible(bb, H, J):
    M = 2**(J + 1)
    for r in range(0, M, 2):           # b*delta even
        if 0 < r <= bb * H and 0 < (r + 2**J) % M <= bb * H:
            return False, r
    return True, None

for bb in [1, 3, 5, 85]:
    for H in [2, 3, 5, 10]:
        J = (bb * H).bit_length()      # smallest J with 2^J > bb*H
        ok, r = pair_trap_incompatible(bb, H, J)
        print("b=%3d H=%2d J=%2d 2^J=%5d > bH=%4d : pair-trap forced"
              " contradiction = %s" % (bb, H, J, 2**J, bb * H, ok))
