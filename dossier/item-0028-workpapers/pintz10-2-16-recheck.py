#!/usr/bin/env python3
"""Local per-prime average in (2.16) of arXiv:1004.1072v1 (Pintz, "Patterns of
primes"), evaluated as a formal series in 1/p.

Object.  Display (2.16) of the source states the average of Pi_1(h)^r over a
full period modulo P as a product over p | P of the per-prime factor

      { (nu_p/p) (1 - nu_p/p)^r + (1 - nu_p/p) (1 - (nu_p+1)/p)^r }
      -------------------------------------------------------------
                  (1 - nu_p/p)^r  (1 - 1/p)^r

and asserts that this factor equals 1 + O(1/p^2).  This script reproduces the
expansion and finds that the quadratic terms cancel as well, so the factor is

      1 + r * nu_p * (r - 1) / 2 * p^{-3} + O(p^{-4}),

whose coefficient vanishes identically at r = 1.  The r = 1 collapse is checked
separately as an exact identity, and it reproduces (2.7) of arXiv:1004.1084v1,
where the same average is stated to be exactly 1.

Support class of the output: MEASURED.  This is a series identity verified
symbolically to the printed order plus numerical spot checks.  It is not a
proof: no remainder is controlled uniformly in p, nu_p and r here.

Reproducibility hazard, recorded because it cost a wrong intermediate result:
calling sympy.simplify() on the quotient N/D with a symbolic exponent r
returns the literal 1, which is false.  Expand numerator and denominator
separately and divide the truncated series; do not simplify the quotient.

Anchors (read-only, not opened by this script):
  arXiv:1004.1072v1  sha256 74824028eb50c322f43da700fcb31fe10ce91272fe8e73695e9a4f82df22053b
  arXiv:1004.1084v1  sha256 f730b045f1163bd539120e3e47237e92720e222d4663db1f86931d620739e5e5

Run:  python3 pintz10-2-16-recheck.py
Deterministic; no network, no randomness, no input files.
"""

import mpmath as mp
import sympy as sp

ORDER = 5  # expand to x^4 inclusive, so the x^3 coefficient is trustworthy

x, v, r = sp.symbols("x v r")  # x = 1/p, v = nu_p, r = moment order

# The per-prime factor exactly as printed in (2.16).
NUM = (v * x) * (1 - v * x) ** r + (1 - v * x) * (1 - (v + 1) * x) ** r
DEN = (1 - v * x) ** r * (1 - x) ** r


def banner(text):
    print()
    print(text)
    print("-" * len(text))


def main():
    print("pintz10-2-16-recheck.py")
    print("sympy %s, mpmath %s" % (sp.__version__, mp.__version__))

    banner("1. Numerator and denominator, expanded separately in x = 1/p")
    sN = sp.expand(sp.series(NUM, x, 0, ORDER).removeO())
    sD = sp.expand(sp.series(DEN, x, 0, ORDER).removeO())
    for name, s in (("N", sN), ("D", sD)):
        for k in range(4):
            print("  %s  coeff x^%d: %s" % (name, k, sp.factor(sp.simplify(s.coeff(x, k)))))

    banner("2. Quotient N/D as a series (no simplify on the quotient)")
    q = sp.series(sN / sD, x, 0, ORDER).removeO()
    q = sp.expand(q)
    coeffs = []
    for k in range(4):
        c = sp.factor(sp.simplify(sp.expand(q.coeff(x, k))))
        coeffs.append(c)
        print("  coeff x^%d: %s" % (k, c))

    assert coeffs[0] == 1, "constant term is not 1"
    assert coeffs[1] == 0, "linear term does not cancel"
    assert coeffs[2] == 0, "quadratic term does not cancel"
    print()
    print("  linear term cancels identically     : yes")
    print("  quadratic term cancels identically  : yes")
    print("  first surviving term                : %s * x^3" % coeffs[3])
    print("  vanishes identically at r = 1       : %s"
          % ("yes" if sp.simplify(coeffs[3].subs(r, 1)) == 0 else "no"))

    banner("3. The r = 1 case is an exact identity, not an expansion")
    diff = sp.simplify(sp.expand(NUM.subs(r, 1) - DEN.subs(r, 1)))
    print("  N - D at r = 1: %s" % diff)
    print("  so the local average is exactly 1 at r = 1: %s"
          % ("yes" if diff == 0 else "no"))
    print("  this reproduces (2.7) of arXiv:1004.1084v1, stated there as = 1")

    banner("4. Numerical spot checks of the printed factor")
    mp.mp.dps = 40
    print("  %-6s %-6s %-8s %-24s %-24s" % ("nu_p", "r", "p", "factor - 1", "predicted c3 / p^3"))
    c3 = coeffs[3]
    for vv, rr in ((1, 1), (1, 2), (2, 3), (3, sp.Rational(5, 2)), (4, 7)):
        f = sp.lambdify(x, NUM.subs({v: vv, r: rr}) / DEN.subs({v: vv, r: rr}), "mpmath")
        pred = sp.lambdify(x, c3.subs({v: vv, r: rr}) * x ** 3, "mpmath")
        for p in (101, 10007):
            got = f(mp.mpf(1) / p) - 1
            print("  %-6s %-6s %-8d %-24s %-24s"
                  % (vv, rr, p, mp.nstr(got, 10), mp.nstr(pred(mp.mpf(1) / p), 10)))

    banner("5. Summary")
    print("  printed in (2.16) of 1004.1072v1 : 1 + O(1/p^2)")
    print("  reproduced here                  : 1 + %s / p^3 + O(1/p^4)" % c3)
    print("  support class                    : MEASURED")


if __name__ == "__main__":
    main()
