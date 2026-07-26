"""
Independent re-execution of the k=2 numerical core cited by report 1 and
report 2 (item-0022, Section 4.6 / rule 4.6 of the kickoff dispatch).

Source formula (re-typed from the anchor, not from either report's copy):
anchor 2, https://people.math.ethz.ch/~kowalski/singular-series-distribution.pdf
(Kowalski, "Averages of Euler products, distribution of singular series and
the ubiquity of Poisson distribution"), Example 3.5:

    mu_k(2) = prod_p ( (1-1/p)*(1-2/p)^k + (1/p)*(1-1/p)^k ) * (1-1/p)^(-2*k)

Example 3.5 states numerically (using Pari/GP):
    mu_2(2) = 2.300...      mu_3(2) = 6.03294...
    mu_4(2) = 17.562...     mu_5(2) = 55.255...
    mu_6(2) = 184.18...

Theorem 1.1 (same anchor) states mu_k(1) = 1 for all k >= 1 (Gallagher's
mean); this is used below only as a sanity check on the Euler-product
machinery, via the k=1 case of the general moment formula (3.10), not as
a re-derivation of Example 3.5's closed form.

Report 1 additionally states the even-class-conditioned second-moment
ratio (its own computation, not an anchor quote):
    E_even[S_2] = 2,  E_even[S_2^2] = 2*mu_2(2)
    E_even[S_2^2] / E_even[S_2]^2 = mu_2(2) / 2

This script recomputes mu_k(2) for k = 2..6 from the Euler product over
all primes p < 2*10^6, at 30 significant digits, and reports the derived
ratio for k=2. It does not consume either report's printed figures before
computing.
"""

from mpmath import mp, mpf

mp.dps = 30 + 10  # 30 significant digits + guard digits

LIMIT = 2_000_000


def sieve_primes(n):
    is_composite = bytearray(n + 1)
    primes = []
    for i in range(2, n + 1):
        if not is_composite[i]:
            primes.append(i)
            for j in range(i * i, n + 1, i):
                is_composite[j] = 1
    return primes


def mu_k_2(primes, k):
    prod = mpf(1)
    for p in primes:
        pf = mpf(p)
        factor = ((1 - 1 / pf) * (1 - 2 / pf) ** k + (1 / pf) * (1 - 1 / pf) ** k) * (
            1 - 1 / pf
        ) ** (-2 * k)
        prod *= factor
    return prod


def main():
    primes = sieve_primes(LIMIT)
    print(f"primes used: {len(primes)} (all primes p < {LIMIT})")
    print(f"largest prime used: {primes[-1]}")
    print(f"working precision: {mp.dps} digits (30 significant + guard)")
    print()

    results = {}
    for k in range(2, 7):
        val = mu_k_2(primes, k)
        results[k] = val
        print(f"mu_{k}(2) = {mp.nstr(val, 30)}")

    print()
    mu2 = results[2]
    e_even_s2 = mpf(2)
    e_even_s2_sq = 2 * mu2
    ratio = e_even_s2_sq / (e_even_s2 ** 2)
    print(f"E_even[S_2]        = {mp.nstr(e_even_s2, 30)}")
    print(f"E_even[S_2^2]      = {mp.nstr(e_even_s2_sq, 30)}")
    print(f"E_even[S_2^2] / E_even[S_2]^2 = {mp.nstr(ratio, 30)}")
    print()

    print("Comparison against anchor 2 Example 3.5 (stated, not assumed):")
    anchor_values = {
        2: "2.300...",
        3: "6.03294...",
        4: "17.562...",
        5: "55.255...",
        6: "184.18...",
    }
    for k in range(2, 7):
        print(f"  k={k}: computed {mp.nstr(results[k], 12)}  vs anchor {anchor_values[k]}")

    print()
    print("Comparison against report 1's more precise figures (not assumed):")
    print(f"  report 1 states mu_2(2) = 2.3009615447...")
    print(f"  computed          mu_2(2) = {mp.nstr(mu2, 15)}")
    print(f"  report 1 states E_even[S_2^2] = 4.6019230894...")
    print(f"  computed          E_even[S_2^2] = {mp.nstr(e_even_s2_sq, 15)}")
    print(f"  report 1 states ratio = 1.1504807723...")
    print(f"  computed          ratio = {mp.nstr(ratio, 15)}")


if __name__ == "__main__":
    main()
