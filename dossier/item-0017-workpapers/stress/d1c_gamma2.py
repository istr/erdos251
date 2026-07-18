# item-0017 D1/D5.c -- the per-position collision constant gamma_2.
# Claim under check (dossier Section 4): the unweighted-capacity floor
# route has threshold A'_crit = 2 sqrt(2)/(e gamma_2) (model gamma_2 =
# 1/2 -> 2.081; route needs A' > 1), and for the primes the heuristic
# asymptote is gamma_2 = E_even[S_2^2]/4 with
#   E_even[S_2^2] = 4 C_2^2 prod_{p>2} (1 + ((p-1)^2/(p-2)^2 - 1)/p).
# This script computes (a) the Euler product, (b) the direct average
# (2/D) sum_{even d <= D} S_2(d)^2 by an spf sieve, (c) the empirical
# per-position collision constant from consecutive prime gaps at x,
# to exhibit the finite-x -> asymptote trend.
import numpy as np, math, sys

def euler_product(P=10**7):
    s = np.ones(P+1, dtype=bool); s[:2] = False
    for i in range(2, int(P**0.5)+1):
        if s[i]: s[i*i::i] = False
    pr = np.nonzero(s)[0][1:]  # odd primes
    a = ((pr-1.0)/(pr-2.0))**2
    return float(np.exp(np.sum(np.log1p((a-1.0)/pr))))

def C2(P=10**7):
    s = np.ones(P+1, dtype=bool); s[:2] = False
    for i in range(2, int(P**0.5)+1):
        if s[i]: s[i*i::i] = False
    pr = np.nonzero(s)[0][1:]
    return float(np.exp(np.sum(np.log1p(-1.0/(pr-1.0)**2))))

def direct_average(D=10**7):
    # S_2(d) for even d via smallest-prime-factor decomposition
    spf = np.zeros(D+1, dtype=np.int32)
    for i in range(2, int(D**0.5)+1):
        if spf[i] == 0:
            spf[i*i::i][spf[i*i::i] == 0] = i
    c2 = C2()
    tot = 0.0; cnt = 0
    for d in range(2, D+1, 2):
        m = d; val = 2*c2
        while m % 2 == 0: m //= 2
        while m > 1:
            p = spf[m] if spf[m] else m
            val *= (p-1.0)/(p-2.0)
            while m % p == 0: m //= p
        tot += val*val; cnt += 1
    return tot/cnt

def empirical_gamma2(LIMIT):
    s = np.ones(LIMIT+1, dtype=bool); s[:2] = False
    for i in range(2, int(LIMIT**0.5)+1):
        if s[i]: s[i*i::i] = False
    p = np.nonzero(s)[0]
    g = np.diff(p)[1:]  # even gaps only (drop g_1 = 1)
    _, cnt = np.unique(g, return_counts=True)
    f = cnt/len(g)
    coll = float(np.sum(f*f))
    return coll*math.log(LIMIT), coll

if __name__ == '__main__':
    c2 = C2(); ep = euler_product()
    E = 4*c2*c2*ep
    print(f"C_2 = {c2:.6f}, Euler product = {ep:.6f}")
    print(f"E_even[S_2^2] = 4 C_2^2 prod = {E:.6f}; heuristic gamma_2 = E/4 = {E/4:.6f}")
    print(f"critical gamma_2 at A'=1: 2 sqrt2/e = {2*math.sqrt(2)/math.e:.6f}")
    print(f"thresholds A'_crit = 2 sqrt2/(e gamma_2): model (gamma_2=1/2) = "
          f"{2*math.sqrt(2)/(math.e*0.5):.6f}; primes (heuristic) = {2*math.sqrt(2)/(math.e*E/4):.6f}")
    Dd = int(float(sys.argv[1])) if len(sys.argv) > 1 else 2*10**6
    da = direct_average(Dd)
    print(f"direct (2/D) sum_(even d<=D) S_2(d)^2 at D={Dd:.0e}: {da:.6f} (vs {E:.6f})")
    for LIM in (2*10**6, 2*10**7):
        gam, coll = empirical_gamma2(LIM)
        print(f"empirical x={LIM:.0e}: per-position collision = {coll:.6f}, gamma_2 = coll*ln x = {gam:.4f}")
