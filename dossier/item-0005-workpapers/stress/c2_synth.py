#!/usr/bin/env python3
# C2 numerics 1: verify the run-divisibility identity on a SYNTHETIC rational
# series. Gap sequence: arbitrary even prefix, then periodic word repeated
# forever. Then every tail delta_n is rational with denominator dividing
# 2^j (2^P - 1); the odd part b of the global denominator makes b delta_n
# integral for n >= s.
#
# CLAIM to verify (algebra of the C2 run-divisibility family):
#   if g_{n+1}, ..., g_{n+r} are all == 0 (mod 2^t) with r <= t and
#   b delta_n in Z, then 2^r | b delta_{n+r}.
# (In the real problem the gap congruence comes from a run of r+1 consecutive
# primes all == a (mod 2^t); here we plant the congruence directly.)

from fractions import Fraction

def delta_from_gaps(gaps_prefix, period, n):
    """delta_n = sum_{j>=1} g_{n+j} 2^{-j}; gaps indexed from 1:
    g_i = gaps_prefix[i-1] for i <= len(prefix), then periodic."""
    L = len(gaps_prefix)
    P = len(period)
    def g(i):
        if i <= L:
            return gaps_prefix[i-1]
        return period[(i - L - 1) % P]
    # delta_n = sum_{j=1}^{J0} g(n+j) 2^{-j} + 2^{-J0} * delta_{n+J0}
    # choose J0 so that n+J0 lands exactly at end of prefix + multiple of P
    # then the remaining tail is the pure periodic tail starting at phase 0:
    # T = sum_{j=1}^{P} period[j-1] 2^{-j} * (1 + 2^{-P} + ...) =
    #     (sum period[j-1] 2^{P-j}) / (2^P - 1)
    A = sum(period[j] * 2**(P - 1 - j) for j in range(P))
    Tper = Fraction(A, 2**P - 1)  # periodic tail at phase 0
    if n >= L:
        # phase within period: g(n+1) = period[(n-L) % P]
        ph = (n - L) % P
        # delta_n = sum_{j=1}^{P-ph} period[ph+j-1] 2^{-j} + 2^{-(P-ph)} Tper
        s = Fraction(0)
        for j in range(1, P - ph + 1):
            s += Fraction(period[ph + j - 1], 2**j)
        return s + Fraction(1, 2**(P - ph)) * Tper
    else:
        s = Fraction(0)
        J0 = L - n
        for j in range(1, J0 + 1):
            s += Fraction(g(n + j), 2**j)
        return s + Fraction(1, 2**J0) * delta_from_gaps(gaps_prefix, period, L)

# --- synthetic example ---------------------------------------------------
# prefix: some even gaps; period contains a planted run of gaps divisible by
# 2^t = 16 (t = 4), run length r = 3 <= t.
prefix = [2, 4, 2, 6]
period = [16, 32, 48, 2, 4, 6, 10, 2]   # first three gaps: == 0 mod 16
t = 4
run_start_gap_index = len(prefix) + 1    # g_5 = 16 (first gap of run)
r = 3

# global odd denominator b: lcm of denominators' odd parts
from math import lcm
dens = set()
for n in range(0, len(prefix) + 3 * len(period)):
    d = delta_from_gaps(prefix, period, n)
    dens.add(d.denominator)
# odd part of lcm
D = lcm(*dens)
b = D
while b % 2 == 0:
    b //= 2
s_pow = 0
DD = D
while DD % 2 == 0:
    DD //= 2
    s_pow += 1
print("denominator lcm D =", D, " odd part b =", b, " 2-power s =", s_pow)

# check b delta_n integral for n >= s_pow, even for n >= s_pow+1
ok_int = all((b * delta_from_gaps(prefix, period, n)).denominator == 1
             for n in range(s_pow, s_pow + 40))
ok_even = all((b * delta_from_gaps(prefix, period, n)) % 2 == 0
              for n in range(s_pow + 1, s_pow + 40))
print("b delta_n integral (n >= s):", ok_int, "   even (n >= s+1):", ok_even)

# run-divisibility check: run of r gaps == 0 mod 2^t starts at gap index
# run gaps are g_{n+1}..g_{n+r} with n = run_start_gap_index - 1
n0 = run_start_gap_index - 1
val = b * delta_from_gaps(prefix, period, n0 + r)
print("planted run: gaps", [16, 32, 48], "== 0 mod 2^%d, r = %d, n0 = %d" % (t, r, n0))
print("b delta_{n0+r} =", val, " divisible by 2^r = %d :" % 2**r,
      val % 2**r == 0)

# also check every periodic recurrence of the run
for rep in range(1, 4):
    n1 = n0 + rep * len(period)
    v = b * delta_from_gaps(prefix, period, n1)  # n1 = end of run at rep
    v = b * delta_from_gaps(prefix, period, n1 + 0)
    vv = b * delta_from_gaps(prefix, period, (n0 + rep * len(period)) + r)
    print("recurrence rep %d: b delta_{n+r} = %s, div by %d: %s"
          % (rep, vv, 2**r, vv % 2**r == 0))

# negative control: a run of gaps NOT all divisible by 2^t should generally
# fail the 2^r divisibility at depth r=3
n_ctl = n0 + 3  # gaps 2,4,6 -- divisible by 2 only
vc = b * delta_from_gaps(prefix, period, n_ctl + 3)
print("control (gaps 2,4,6): b delta =", vc, " div by 8:", vc % 8 == 0,
      " div by 2:", vc % 2 == 0)
