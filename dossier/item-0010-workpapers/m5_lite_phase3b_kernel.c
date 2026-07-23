/*
 * item-0010 M5-lite Phase 3b residue/rho kernel.
 *
 * This is an implementation of the frozen Python reference object in
 * m5_lite_measure.py.  It changes no mathematical definition.  For one side
 * class and one odd prime p, it forms the two side residue sets once and uses
 *
 *   nu_H(d) = nu_pre + nu_suf - overlap[(d mod p)]
 *
 * for every prospective and realized middle.  All admissibility decisions
 * and CRT profiles are integer-exact.  Rho products are accumulated in
 * long double and accompanied by a conservative enclosure for the exact
 * rational product through Q.
 */

#include <float.h>
#include <math.h>
#include <stdint.h>
#include <stdlib.h>
#include <string.h>

#define M5_MAX_SIDE_POINTS 128
#define M5_MAX_DOMAIN 4096
#define M5_MAX_PRIME 4096
#define M5_PROFILE_COUNT 5
#define M5_BAND_OPERATION_BOUND 200000

static const int m5_profile_primes[M5_PROFILE_COUNT] = {3, 5, 7, 11, 13};

static int
m5_profile_index(int p)
{
    int i;
    for (i = 0; i < M5_PROFILE_COUNT; ++i) {
        if (m5_profile_primes[i] == p) {
            return i;
        }
    }
    return -1;
}

static double
m5_lower(double nominal, long double gamma)
{
    long double value;
    if (nominal == 0.0) {
        return 0.0;
    }
    value = (long double)nominal / (1.0L + gamma);
    return nextafter((double)value, -INFINITY);
}

static double
m5_upper(double nominal, long double gamma)
{
    long double value;
    if (nominal == 0.0) {
        return 0.0;
    }
    value = (long double)nominal / (1.0L - gamma);
    return nextafter((double)value, INFINITY);
}

/*
 * Process a contiguous class shard.
 *
 * sides has shape (nclass, J+K).  cell_offsets has nclass+1 entries and is
 * local to this shard; mids has cell_offsets[nclass] entries.  All output
 * arrays are caller-owned and have the corresponding class/cell lengths.
 *
 * Return values:
 *   0 success
 *   1 unsupported dimensions
 *   2 invalid cell offsets
 *   3 invalid prime list
 *   4 invalid band decimal
 */
int
m5_phase3b_batch(
    const int16_t *sides,
    int64_t nclass,
    int J,
    int K,
    int W_floor,
    const int64_t *cell_offsets,
    const int64_t *mids,
    const int32_t *small_primes,
    int nsmall,
    const char *band_decimal,
    int32_t *A_out,
    int32_t *domain_out,
    double *rho_pros_out,
    double *rho_pros_lower_out,
    double *rho_pros_upper_out,
    int32_t *pros_off_out,
    double *realized_rho_out,
    double *realized_lower_out,
    double *realized_upper_out,
    uint8_t *realized_off_out,
    int16_t *profiles_out)
{
    int64_t cls;
    char *band_end = NULL;
    long double band;
    const int side_width = J + K;
    const int k = J + K + 2;
    const long double unit_roundoff = ldexpl(1.0L, -LDBL_MANT_DIG);

    if (J < 0 || K < 0 || J + 1 > M5_MAX_SIDE_POINTS ||
        K + 1 > M5_MAX_SIDE_POINTS || W_floor >= 2 * M5_MAX_DOMAIN ||
        W_floor >= M5_MAX_PRIME) {
        return 1;
    }
    if (cell_offsets[0] != 0 || cell_offsets[nclass] < 0) {
        return 2;
    }
    if (nsmall <= 0 || small_primes[0] < 3 ||
        small_primes[nsmall - 1] > W_floor) {
        return 3;
    }
    band = strtold(band_decimal, &band_end);
    if (band_end == band_decimal || *band_end != '\0' ||
        !(band > 0.0L) || !isfinite(band)) {
        return 4;
    }

    for (cls = 0; cls < nclass; ++cls) {
        int pre[M5_MAX_SIDE_POINTS];
        int suf[M5_MAX_SIDE_POINTS];
        int pre_res[M5_MAX_SIDE_POINTS];
        int suf_res[M5_MAX_SIDE_POINTS];
        int overlap[M5_MAX_PRIME];
        long double candidate[M5_MAX_DOMAIN];
        uint8_t candidate_alive[M5_MAX_DOMAIN];
        uint8_t candidate_admissible[M5_MAX_DOMAIN];
        uint8_t candidate_off[M5_MAX_DOMAIN];
        long double realized[M5_MAX_DOMAIN];
        uint8_t realized_alive[M5_MAX_DOMAIN];
        uint8_t realized_off[M5_MAX_DOMAIN];
        int dmax;
        int domain;
        int ncells;
        int i;
        int prime_index;
        int A = 0;
        int off_count = 0;
        double rho_sum = 0.0;
        const int64_t cell_lo = cell_offsets[cls];
        const int64_t cell_hi = cell_offsets[cls + 1];

        if (cell_hi < cell_lo || cell_hi - cell_lo > M5_MAX_DOMAIN) {
            return 2;
        }
        ncells = (int)(cell_hi - cell_lo);

        pre[0] = 0;
        for (i = 0; i < J; ++i) {
            pre[i + 1] = pre[i] + (int)sides[cls * side_width + i];
        }
        suf[0] = 0;
        for (i = 0; i < K; ++i) {
            suf[i + 1] =
                suf[i] + (int)sides[cls * side_width + J + i];
        }
        dmax = W_floor - pre[J] - suf[K];
        domain = dmax >= 2 ? dmax / 2 : 0;
        if (domain > M5_MAX_DOMAIN) {
            return 1;
        }
        domain_out[cls] = (int32_t)domain;

        for (i = 0; i < domain; ++i) {
            candidate[i] = 2.0L * band;
            candidate_alive[i] = 1;
            candidate_admissible[i] = 1;
            candidate_off[i] = 0;
        }
        for (i = 0; i < ncells; ++i) {
            realized[i] = 2.0L * band;
            realized_alive[i] = 1;
            realized_off[i] = 0;
        }

        for (prime_index = 0; prime_index < nsmall; ++prime_index) {
            const int p = (int)small_primes[prime_index];
            const int profile_index = m5_profile_index(p);
            int na = 0;
            int nb = 0;
            int a;
            int b;
            int side_bad;

            if (p <= 2 || p >= M5_MAX_PRIME) {
                return 3;
            }
            memset(overlap, 0, (size_t)p * sizeof(overlap[0]));
            for (a = 0; a <= J; ++a) {
                int r = pre[a] % p;
                int found = 0;
                for (b = 0; b < na; ++b) {
                    if (pre_res[b] == r) {
                        found = 1;
                        break;
                    }
                }
                if (!found) {
                    pre_res[na++] = r;
                }
            }
            for (a = 0; a <= K; ++a) {
                int r = suf[a] % p;
                int found = 0;
                for (b = 0; b < nb; ++b) {
                    if (suf_res[b] == r) {
                        found = 1;
                        break;
                    }
                }
                if (!found) {
                    suf_res[nb++] = r;
                }
            }
            for (a = 0; a < na; ++a) {
                for (b = 0; b < nb; ++b) {
                    int shift = pre_res[a] - (pre[J] % p) - suf_res[b];
                    shift %= p;
                    if (shift < 0) {
                        shift += p;
                    }
                    overlap[shift] += 1;
                }
            }
            side_bad = na == p || nb == p;

            for (i = 0; i < domain; ++i) {
                const int d = 2 * (i + 1);
                const int nh = na + nb - overlap[d % p];
                if (p <= k && nh == p) {
                    candidate_admissible[i] = 0;
                }
                if (!candidate_alive[i]) {
                    continue;
                }
                if (side_bad) {
                    candidate[i] = 0.0L;
                    candidate_alive[i] = 0;
                    candidate_off[i] = 1;
                } else if (nh == p) {
                    candidate[i] = 0.0L;
                    candidate_alive[i] = 0;
                } else {
                    const long double numerator =
                        (long double)(p - nh) * (long double)p;
                    const long double denominator =
                        (long double)(p - na) * (long double)(p - nb);
                    candidate[i] *= numerator / denominator;
                }
            }

            for (i = 0; i < ncells; ++i) {
                const int64_t d = mids[cell_lo + i];
                int dmod = (int)(d % p);
                int nh;
                if (!realized_alive[i]) {
                    continue;
                }
                if (dmod < 0) {
                    dmod += p;
                }
                nh = na + nb - overlap[dmod];
                if (profile_index >= 0) {
                    const int64_t base =
                        ((cell_lo + i) * M5_PROFILE_COUNT + profile_index) * 3;
                    profiles_out[base] = (int16_t)nh;
                    profiles_out[base + 1] = (int16_t)na;
                    profiles_out[base + 2] = (int16_t)nb;
                }
                if (side_bad) {
                    realized[i] = 0.0L;
                    realized_alive[i] = 0;
                    realized_off[i] = 1;
                } else if (nh == p) {
                    realized[i] = 0.0L;
                    realized_alive[i] = 0;
                } else {
                    const long double numerator =
                        (long double)(p - nh) * (long double)p;
                    const long double denominator =
                        (long double)(p - na) * (long double)(p - nb);
                    realized[i] *= numerator / denominator;
                }
            }
        }

        for (i = 0; i < domain; ++i) {
            const double value = (double)candidate[i];
            if (candidate_admissible[i]) {
                A += 1;
            }
            if (candidate_off[i]) {
                off_count += 1;
            }
            /*
             * Deliberately sum rounded binary64 candidates in ascending d
             * order, matching the reference Python accumulation order.
             */
            rho_sum += value;
        }
        A_out[cls] = (int32_t)A;
        pros_off_out[cls] = (int32_t)off_count;
        rho_pros_out[cls] = domain ? rho_sum / (double)domain : 0.0;
        {
            const long double operation_count =
                8.0L + (long double)M5_BAND_OPERATION_BOUND
                + 2.0L * (long double)nsmall + (long double)domain;
            const long double raw =
                operation_count * unit_roundoff;
            const long double gamma =
                8.0L * raw / (1.0L - raw);
            rho_pros_lower_out[cls] =
                m5_lower(rho_pros_out[cls], gamma);
            rho_pros_upper_out[cls] =
                m5_upper(rho_pros_out[cls], gamma);
        }

        for (i = 0; i < ncells; ++i) {
            const int64_t out_index = cell_lo + i;
            const double value = (double)realized[i];
            const long double operation_count =
                8.0L + (long double)M5_BAND_OPERATION_BOUND
                + 2.0L * (long double)nsmall;
            const long double raw =
                operation_count * unit_roundoff;
            const long double gamma =
                8.0L * raw / (1.0L - raw);
            realized_rho_out[out_index] = value;
            realized_lower_out[out_index] = m5_lower(value, gamma);
            realized_upper_out[out_index] = m5_upper(value, gamma);
            realized_off_out[out_index] = realized_off[i];
        }
    }
    return 0;
}

int
m5_phase3b_long_double_mantissa_bits(void)
{
    return LDBL_MANT_DIG;
}
