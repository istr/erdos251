# item-0019 m5 -- small-span thinning calibration (kickoff 3(f)).
#
# ENTIRELY in the N^o world of RS.4 (consCount semantics): anchor
# prime in (sqrt x, x], NO caps, NO S'_x mixing.  ANCHOR FIREWALL
# (item-0018 report F3): consCount's anchor is q n = p[n] in the
# 0-indexed array -- one off from anchorPrime n = p[n-1] used by
# m1-m4.  m5 tables are NEVER joined with m1-m4 tables on a site
# index.  The anchor clause sqrt x < p is evaluated as the exact
# integer comparison p*p > x (equivalent to Real.sqrt x < p for
# integer p >= 0).
#
# Word set (deterministic, printed): for k in {4, 5, 6, 8}, the
# lexicographically first 3 admissible all-even gap words (k-1 gaps,
# each >= 2) with span <= kappa (k-1) ln(k+1), kappa in {1, 2}.
# Admissibility: H = prefix sums (k points, 0 in H) misses a residue
# class mod every prime p <= k (p > k is automatic, |H| = k < p).
# An empty set at some (k, kappa) is printed as EMPTY -- itself a
# datum (budget below the minimal admissible even span).
#
# N^o_consec: consecutive realizations (IsConsecRealization; the L =
# k-1 gaps after the anchor spell the word), anchor in (sqrt x, x].
# N^o_tuple: tupleCount semantics (all k points prime), same anchor
# range; bitset shift-and.  The sieve extends to x + 64 (> max span)
# so realizations whose non-anchor points exceed x are counted, as in
# the Lean defs.
#
# HEURISTIC/U18.1 reference line: exp(-span/ln x) (Cramer thinning);
# no asymptotic exponent is fitted.

import numpy as np, math, os, sys, json
import common as C

KS = [4, 5, 6, 8]
KAPPAS = [1, 2]
XS = [100_000_000, 1_000_000_000]
PAD = 64


def admissible(H, k):
    for p in range(2, k + 1):
        if p == 2 or all(p % q for q in range(2, p)):
            if len(set(h % p for h in H)) == p:
                return False
    return True


def first_words(k, kappa, want=3):
    B = kappa * (k - 1) * math.log(k + 1)
    L = k - 1
    out = []

    def rec(prefix, s):
        if len(out) >= want:
            return
        if len(prefix) == L:
            H = [0]
            for w in prefix:
                H.append(H[-1] + w)
            if admissible(H, k):
                out.append(list(prefix))
            return
        rem = L - len(prefix) - 1
        w = 2
        while s + w + 2 * rem <= B:
            rec(prefix + [w], s + w)
            if len(out) >= want:
                return
            w += 2
    rec([], 0)
    return out, B


def build_m5(x):
    fpr = os.path.join(C.CACHE, f"m5pr_{x}.npy")
    fp5 = os.path.join(C.CACHE, f"m5p_{x}.npy")
    if os.path.exists(fpr):
        return np.load(fpr), np.load(fp5)
    pr = C.sieve_primes(x + PAD)
    p5 = np.nonzero(pr)[0].astype(np.int64)
    np.save(fpr, pr); np.save(fp5, p5)
    return pr, p5


def main():
    results = []
    for x in XS:
        pr, p5 = build_m5(x)
        g5 = np.diff(p5).astype(np.int64)
        lnx = math.log(x)
        a0 = math.isqrt(x) + 1  # smallest integer with a^2 > x ...
        # exact anchor clause: a in (sqrt x, x] <=> a >= a0' where
        # a0' = isqrt(x)+1 (a > sqrt x <=> a^2 > x <=> a > isqrt(x))
        n_lo = int(np.searchsorted(p5, a0))
        n_hi = int(np.searchsorted(p5, x, side='right'))  # p <= x
        for k in KS:
            L = k - 1
            for kappa in KAPPAS:
                words, B = first_words(k, kappa)
                if not words:
                    results.append(dict(x=x, k=k, kappa=kappa,
                                        budget=B, word=None))
                    continue
                for w in words:
                    H = [0]
                    for wi in w:
                        H.append(H[-1] + wi)
                    span = H[-1]
                    # consecutive realizations, anchor p5[n]
                    m = len(g5) - L + 1
                    mask = np.ones(m, dtype=bool)
                    for i, wi in enumerate(w):
                        mask &= g5[i:m + i] == wi
                    idx = np.nonzero(mask)[0]
                    idx = idx[(idx >= n_lo) & (idx < n_hi)]
                    ncons = len(idx)
                    # tuple count, same anchor range, bitset shift-and
                    acc = pr[a0:x + 1].copy()
                    for h in H[1:]:
                        acc &= pr[a0 + h:x + 1 + h]
                    ntup = int(np.count_nonzero(acc))
                    results.append(dict(
                        x=x, k=k, kappa=kappa, budget=B,
                        word=w, span=span, ncons=ncons, ntup=ntup,
                        ratio=(ncons / ntup if ntup else float('nan')),
                        cramer=math.exp(-span / lnx)))
                    print(f"x={x:.0e} k={k} kappa={kappa} w={w} "
                          f"span={span} cons={ncons} tup={ntup} "
                          f"ratio={ncons / ntup if ntup else 0:.4f} "
                          f"exp(-span/lnx)={math.exp(-span / lnx):.4f}",
                          flush=True)
        del pr, p5, g5
    with open(os.path.join(C.CACHE, "m5.json"), "w") as f:
        json.dump(results, f, indent=1)


if __name__ == '__main__':
    main()
