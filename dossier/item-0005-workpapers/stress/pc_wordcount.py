import numpy as np, math
# Precision-check: does the number of DISTINCT length-L gap-words realized at
# delta-controlled sites grow like 2^{L^2/2} (product-bound / sqrt(log x) capacity)
# or like (const)^L (typical-gap / log x per loglog x capacity)?
# Also: is the section 3(i) product bound prod 2^{i-1} D the reason, or is the
# realized entropy linear in L (so capacity ~ log x/loglog x is the *typical* rate)?
LIMIT = 100_000_000
sieve = np.ones(LIMIT+1, dtype=bool); sieve[:2] = False
for i in range(2, int(LIMIT**0.5)+1):
    if sieve[i]: sieve[i*i::i] = False
p = np.nonzero(sieve)[0].astype(np.int64)
g = np.diff(p); M = len(g)
delta = np.zeros(M); delta[M-1] = 2.0
for t in range(M-2, -1, -1): delta[t] = 0.5*(g[t] + delta[t+1])
VALID = M-200
gg = g.astype(np.int32)
N = VALID
lnx = math.log(LIMIT)
print(f"x=1e8 pi={len(p)} lnx={lnx:.2f} log2(N)={math.log2(N):.2f}")
print(f"  mean gap={g[:VALID].mean():.2f}  sqrt(2 log2 N)={math.sqrt(2*math.log2(N)):.2f} (worst-case product-bound capacity)")
print(f"  (log x)/(loglog x)={lnx/math.log(lnx):.2f}  (2/log2)*loglog x={(2/math.log(2))*math.log(lnx):.2f}\n")

# Count distinct length-L contiguous gap words over ALL sites (no delta filter)
# and over sites with all-window-gaps <= G (the tight rigorous restriction).
G = 4*lnx  # ~ A log x uniform gap cap
print(f"Distinct length-L words realized (all sites) vs unique-word ceiling; G-cap={G:.0f}")
print(f"{'L':>3} {'#distinct(all)':>15} {'log2':>7} {'bits/pos':>9} {'#sites gaps<=G':>15} {'#distinct(<=G)':>15}")
for L in range(2, 16):
    # all-site distinct words
    words = set()
    step = 1
    for t in range(0, VALID-L, step):
        words.add(gg[t:t+L].tobytes())
    nall = len(words)
    # sites with all window gaps <= G, distinct words among them
    wordsG = set(); nsite=0
    for t in range(0, VALID-L, step):
        w = gg[t:t+L]
        if w.max() <= G:
            nsite += 1; wordsG.add(w.tobytes())
    b = math.log2(nall)
    print(f"{L:>3} {nall:>15} {b:>7.2f} {b/L:>9.3f} {nsite:>15} {len(wordsG):>15}")
