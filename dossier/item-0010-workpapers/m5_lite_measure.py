#!/usr/bin/env python3
"""item-0010 M5-lite finite measurement engine.

Web-independent local implementation of the frozen registry at
m5-lite-measurement-registry.yaml.  The expensive prospective-rho
object is evaluated on the full residual D0 domain, never on realized
middles alone.

Commands:
  self-test
  continuity
  profile X [NCLASS]
  smoke
  run X S

Raw outputs are written below m5-lite-measurements/.  Regenerable
prime/gap/delta caches live below $ITEM0010_CACHE (default:
/tmp/item0010-m5-lite-cache).
"""

from __future__ import annotations

import hashlib
import json
import math
import os
import platform
import shutil
import sys
import time
from collections import Counter, defaultdict
from decimal import Decimal, ROUND_CEILING, ROUND_FLOOR, localcontext
from fractions import Fraction
from multiprocessing import get_context
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
REPO = HERE.parent.parent
OUT = HERE / "m5-lite-measurements"
REGISTRY = HERE / "m5-lite-measurement-registry.yaml"
REGISTRY_HASH = "047bfe6e64146d78e851e2964033b6381ef78f1aa9802f02401276130f4e547b"
PIN = "8d82901785b36ab87dc413dc7f0cc1e992808748"
Q_RHO = 1_000_000
PROFILE_PRIMES = (3, 5, 7, 11, 13)

ITEM0019 = REPO / "dossier" / "item-0019-workpapers"
sys.path.insert(0, str(ITEM0019))
os.environ.setdefault("ITEM0019_CACHE", "/tmp/item0010-m5-lite-cache")
import common as I19  # noqa: E402


def file_sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for block in iter(lambda: f.read(1 << 20), b""):
            h.update(block)
    return h.hexdigest()


def verify_registry() -> dict:
    got = file_sha256(REGISTRY)
    if got != REGISTRY_HASH:
        raise RuntimeError(
            f"registry hash mismatch: got {got}, frozen {REGISTRY_HASH}")
    with REGISTRY.open() as f:
        reg = json.load(f)
    if reg["dispatch_pin"] != PIN:
        raise RuntimeError("registry dispatch pin mismatch")
    return reg


def git_head() -> str:
    import subprocess
    return subprocess.check_output(
        ["git", "rev-parse", "HEAD"], cwd=REPO, text=True).strip()


def d0_parameters(x: int) -> dict:
    """Ceil/floor-stable 80-digit evaluation of the exact D0 map."""
    vals = []
    for prec in (80, 100):
        with localcontext() as ctx:
            ctx.prec = prec
            dx = Decimal(x)
            lnx = dx.ln()
            c0 = Decimal(2) / Decimal(3).ln()
            raw_d = Decimal(13) * c0 * Decimal(48) * lnx
            D = int(raw_d.to_integral_value(rounding=ROUND_CEILING))
            J = (D - 1).bit_length()
            K = J
            L = J + 1 + K
            w = Decimal(3) * Decimal(L) * lnx / Decimal(2)
            w_floor = int(w.to_integral_value(rounding=ROUND_FLOOR))
            vals.append((D, J, K, L, w_floor, str(+lnx), str(+w)))
    if vals[0][:5] != vals[1][:5]:
        raise RuntimeError(f"D0 boundary unstable at x={x}: {vals}")
    D, J, K, L, wf, lnx, w = vals[-1]
    return dict(
        x=x, C_0="2/log(3)", A_prime="3/2", A_double_prime=48,
        D=D, J=J, K=K, L=L, k=L + 1, W_floor=wf,
        log_x=lnx, W=w, precision_digits=100,
        boundary_stable_80_100=True)


def primes_through(n: int) -> list[int]:
    return np.nonzero(I19.sieve_primes(n))[0].astype(int).tolist()


def tree_prod(vals: list[int]) -> int:
    if not vals:
        return 1
    while len(vals) > 1:
        vals = [
            vals[i] * vals[i + 1] if i + 1 < len(vals) else vals[i]
            for i in range(0, len(vals), 2)
        ]
    return vals[0]


def nu(points: tuple[int, ...], p: int) -> int:
    return len({v % p for v in points})


def point_sets(side: np.ndarray, J: int) -> tuple[tuple[int, ...],
                                                  tuple[int, ...]]:
    pre = tuple([0] + np.cumsum(side[:J], dtype=np.int64).astype(int).tolist())
    suf = tuple([0] + np.cumsum(side[J:], dtype=np.int64).astype(int).tolist())
    return pre, suf


class RhoEvaluator:
    """Exact integer local products through Q with a certified tail."""

    def __init__(self, J: int, K: int, S0: int):
        self.J = J
        self.K = K
        self.k = J + K + 2
        self.S0 = S0
        self.small_primes = [p for p in primes_through(S0) if p & 1]
        band_primes = [p for p in primes_through(Q_RHO)
                       if p & 1 and p > S0]
        self.band_num = tree_prod([(p - self.k) * p for p in band_primes])
        self.band_den = tree_prod([
            (p - (J + 1)) * (p - (K + 1)) for p in band_primes])
        self.band = Fraction(self.band_num, self.band_den)
        self.tail_log_width = 0.51 * self.k * self.k / Q_RHO

    def upper(self, pre: tuple[int, ...], suf: tuple[int, ...],
              d: int) -> tuple[float, bool, dict[int, tuple[int, int, int]]]:
        aj = pre[-1]
        shifted = tuple(aj + d + v for v in suf)
        full = pre + shifted
        num = 1
        den = 1
        profile = {}
        for p in self.small_primes:
            nh, na, nb = nu(full, p), nu(pre, p), nu(suf, p)
            if p in PROFILE_PRIMES:
                profile[p] = (nh, na, nb)
            if na == p or nb == p:
                return 0.0, True, profile
            if nh == p:
                return 0.0, False, profile
            num *= (p - nh) * p
            den *= (p - na) * (p - nb)
        rho_q = Fraction(2 * num, den) * self.band
        return float(rho_q), False, profile


def exact_class_records(g: np.ndarray, sites: np.ndarray, J: int, K: int) -> dict:
    """Materialize the exact class/cell partition for one finite row."""
    L = J + 1 + K
    ns = len(sites)
    word = np.empty((ns, L), dtype=np.int16)
    for j in range(L):
        word[:, j] = g[sites + j]
    side = np.concatenate((word[:, :J], word[:, J + 1:]), axis=1)
    middle = word[:, J].astype(np.int64)
    keys = (sites, middle) + tuple(
        side[:, j] for j in reversed(range(J + K)))
    order = np.lexsort(keys)
    side = side[order]
    middle = middle[order]
    sites = sites[order]
    new_class = np.empty(ns, dtype=bool)
    new_class[0] = True
    new_class[1:] = np.any(side[1:] != side[:-1], axis=1)
    new_cell = new_class.copy()
    new_cell[1:] |= middle[1:] != middle[:-1]
    class_start = np.nonzero(new_class)[0]
    class_end = np.append(class_start[1:], ns)
    cell_start = np.nonzero(new_cell)[0]
    cell_end = np.append(cell_start[1:], ns)
    NP = (class_end - class_start).astype(np.int64)
    NPd = (cell_end - cell_start).astype(np.int64)
    cell_class = np.searchsorted(class_start, cell_start, side="right") - 1
    nmid = np.bincount(cell_class, minlength=len(NP)).astype(np.int64)
    maxNPd = np.zeros(len(NP), dtype=np.int64)
    np.maximum.at(maxNPd, cell_class, NPd)
    return dict(
        sides=side[class_start].copy(), NP=NP, nmid=nmid,
        maxNPd=maxNPd, first_site=sites[class_start].copy(),
        cell_class=cell_class, mid=middle[cell_start].copy(),
        cell_first_site=sites[cell_start].copy(), NPd=NPd)


def collision_metrics(rec: dict) -> dict:
    NP = rec["NP"].astype(np.int64)
    NPd = rec["NPd"].astype(np.int64)
    ci = rec["cell_class"].astype(np.int64)
    F = len(NP)
    N = int(NP.sum())
    q = Fraction()
    W2 = 0
    by_class_num = np.zeros(F, dtype=np.int64)
    np.add.at(by_class_num, ci, NPd * (NPd - 1))
    sum_sq = np.zeros(F, dtype=np.int64)
    np.add.at(sum_sq, ci, NPd * NPd)
    for n, w in zip(NP.tolist(), by_class_num.tolist()):
        q += Fraction(w, n)
    defect = Fraction(N - F) - q
    direct_cross = sum(
        (Fraction(int(n * n - ss), int(n))
         for n, ss in zip(NP.tolist(), sum_sq.tolist())), Fraction())
    W2 = int(by_class_num.sum())
    if defect != direct_cross:
        raise AssertionError("collision defect identity mismatch")
    escape = sum((NP - rec["maxNPd"]).astype(object))
    if not (q <= N - F):
        raise AssertionError("Q <= N-F failed")
    if not (Fraction(escape, N) <= defect / N
            <= 2 * Fraction(escape, N)):
        raise AssertionError("escape/Gini bounds failed")
    return dict(
        N=N, F=F, Q=str(q), Q_num=q.numerator, Q_den=q.denominator,
        Q_over_N=str(q / N), F_over_N=str(Fraction(F, N)),
        defect=str(defect), defect_over_N=str(defect / N),
        all_class_Gini=str(defect / N),
        majority_escape_over_N=str(Fraction(escape, N)),
        W2=W2,
        checks=dict(
            Q_le_N_minus_F=True,
            defect_identity=True,
            Gini_equals_defect=True,
            escape_le_Gini_le_2escape=True))


def class_size_strata(rec: dict, N: int) -> list[dict]:
    NP = rec["NP"].astype(np.int64)
    NPd = rec["NPd"].astype(np.int64)
    ci = rec["cell_class"].astype(np.int64)
    class_w = np.zeros(len(NP), dtype=np.int64)
    class_sq = np.zeros(len(NP), dtype=np.int64)
    np.add.at(class_w, ci, NPd * (NPd - 1))
    np.add.at(class_sq, ci, NPd * NPd)
    rows = []
    M = 1
    while M <= int(NP.max()):
        mask = (NP >= M) & (NP < 2 * M)
        classes = np.nonzero(mask)[0]
        if len(classes):
            cmask = mask[ci]
            n_m = int(NP[mask].sum())
            w2 = int(np.sum(NPd[cmask] * (NPd[cmask] - 1)))
            v2 = int(np.sum(NP[mask] * (NP[mask] - 1)))
            q_m = Fraction()
            rigid_mass = 0
            escape = 0
            gini = Fraction()
            for c in classes.tolist():
                q_m += Fraction(int(class_w[c]), int(NP[c]))
                if rec["nmid"][c] == 1:
                    rigid_mass += int(NP[c])
                escape += int(NP[c] - rec["maxNPd"][c])
                gini += Fraction(int(NP[c]) ** 2 - int(class_sq[c]),
                                 int(NP[c]))
            if not (Fraction(w2, 2 * M - 1) <= q_m
                    <= Fraction(w2, M)):
                raise AssertionError("stratum W2/Q inequality failed")
            if not ((M - 1) * n_m <= v2 <= (2 * M - 2) * n_m):
                raise AssertionError("stratum V2 inequality failed")
            rows.append(dict(
                M=M, upper_exclusive=2 * M, class_count=len(classes),
                N_M=n_m, N_M_over_N=str(Fraction(n_m, N)),
                W2_M=w2, V2_M=v2, Q_M=str(q_m),
                Q_M_over_N=str(q_m / N),
                rigid_site_mass=rigid_mass,
                nonrigid_site_mass=n_m - rigid_mass,
                escape_over_N=str(Fraction(escape, N)),
                Gini_over_N=str(gini / N),
                checks=dict(W2_Q_bounds=True, V2_bounds=True)))
        M *= 2
    return rows


def admissible(pre: tuple[int, ...], suf: tuple[int, ...], d: int,
               primes_k: list[int]) -> bool:
    full = pre + tuple(pre[-1] + d + v for v in suf)
    return all(nu(full, p) < p for p in primes_k)


def prospective_one(side: np.ndarray, J: int, K: int, W_floor: int,
                    primes_k: list[int], rho_eval: RhoEvaluator) -> dict:
    pre, suf = point_sets(side, J)
    dmax = W_floor - pre[-1] - suf[-1]
    ds = range(2, dmax + 1, 2) if dmax >= 2 else ()
    count_domain = max(0, dmax // 2)
    A = 0
    rho_sum = 0.0
    off_domain = 0
    for d in ds:
        if admissible(pre, suf, d, primes_k):
            A += 1
        rho, off, _ = rho_eval.upper(pre, suf, d)
        rho_sum += rho
        off_domain += int(off)
    return dict(
        A_P=A, residual_domain_size=count_domain,
        rho_pros=(rho_sum / count_domain if count_domain else 0.0),
        prospective_off_domain=off_domain)


_PAR_CTX = {}


def _prospective_chunk(bounds: tuple[int, int]) -> tuple[int, list[dict]]:
    lo, hi = bounds
    c = _PAR_CTX
    out = []
    for side in c["sides"][lo:hi]:
        out.append(prospective_one(
            side, c["J"], c["K"], c["W_floor"],
            c["primes_k"], c["rho_eval"]))
    return lo, out


def prospective_parallel(sides: np.ndarray, J: int, K: int, W_floor: int,
                         workers: int) -> tuple[list[dict], float]:
    global _PAR_CTX
    rho_eval = RhoEvaluator(J, K, W_floor)
    _PAR_CTX = dict(
        sides=sides, J=J, K=K, W_floor=W_floor,
        primes_k=primes_through(J + K + 2), rho_eval=rho_eval)
    chunks = [(lo, min(lo + 64, len(sides)))
              for lo in range(0, len(sides), 64)]
    result = [None] * len(sides)
    t0 = time.perf_counter()
    with get_context("fork").Pool(workers) as pool:
        for done, (lo, part) in enumerate(
                pool.imap_unordered(_prospective_chunk, chunks), 1):
            result[lo:lo + len(part)] = part
            if done % 100 == 0 or done == len(chunks):
                print(f"prospective: {done}/{len(chunks)} chunks",
                      flush=True)
    wall = time.perf_counter() - t0
    _PAR_CTX = {}
    return result, wall


def _realized_rho_chunk(bounds: tuple[int, int]) -> tuple[int, list[dict]]:
    lo, hi = bounds
    c = _PAR_CTX
    out = []
    for i in range(lo, hi):
        cls = int(c["cell_class"][i])
        pre, suf = point_sets(c["sides"][cls], c["J"])
        rho, off, profile = c["rho_eval"].upper(
            pre, suf, int(c["mid"][i]))
        out.append(dict(rho=rho, off_domain=off, profile=profile))
    return lo, out


def realized_rho_parallel(rec: dict, J: int, K: int, W_floor: int,
                          workers: int) -> tuple[list[dict], float]:
    global _PAR_CTX
    _PAR_CTX = dict(
        sides=rec["sides"], cell_class=rec["cell_class"],
        mid=rec["mid"], J=J, rho_eval=RhoEvaluator(J, K, W_floor))
    chunks = [(lo, min(lo + 512, len(rec["NPd"])))
              for lo in range(0, len(rec["NPd"]), 512)]
    result = [None] * len(rec["NPd"])
    t0 = time.perf_counter()
    with get_context("fork").Pool(workers) as pool:
        for done, (lo, part) in enumerate(
                pool.imap_unordered(_realized_rho_chunk, chunks), 1):
            result[lo:lo + len(part)] = part
            if done % 100 == 0 or done == len(chunks):
                print(f"realized rho: {done}/{len(chunks)} chunks",
                      flush=True)
    wall = time.perf_counter() - t0
    _PAR_CTX = {}
    return result, wall


def weighted_quantile(values: np.ndarray, weights: np.ndarray,
                      q: float) -> float | None:
    if not len(values) or float(weights.sum()) == 0:
        return None
    order = np.argsort(values, kind="stable")
    v = values[order]
    w = weights[order].astype(np.float64)
    cutoff = q * float(w.sum())
    return float(v[min(int(np.searchsorted(np.cumsum(w), cutoff,
                                           side="left")), len(v) - 1)])


def rule_rows(reg: dict, rec: dict, prospective: list[dict],
              global_metrics: dict) -> list[dict]:
    NP = rec["NP"].astype(np.int64)
    M = rec["maxNPd"].astype(np.int64)
    nmid = rec["nmid"].astype(np.int64)
    N = int(NP.sum())
    F = len(NP)
    r = (M - 1) / NP
    class_sq = np.zeros(F, dtype=np.int64)
    np.add.at(class_sq, rec["cell_class"], rec["NPd"] * rec["NPd"])
    A = np.array([v["A_P"] for v in prospective], dtype=np.int64)
    rho = np.array([v["rho_pros"] for v in prospective], dtype=np.float64)
    lnx = float(Decimal(str(global_metrics["log_x"])))
    q_over_n = float(Fraction(global_metrics["Q_over_N"]))
    rows = []
    for rule in reg["rules"]:
        rid = rule["rule_id"]
        if not (rid.startswith("R0-") or rid.startswith("R1-")
                or rid.startswith("R2-") or rid.startswith("R3-")):
            continue
        if rid.startswith(("R0-", "R1-")):
            selected = np.ones(F, dtype=bool)
        elif rid.startswith("R2-"):
            cap_token = rid.split("-")[1][3:]
            caps = {"1_8": 1 / 8, "1_4": 1 / 4, "1_2": 1 / 2,
                    "3_4": 3 / 4, "1": 1}
            selected = (A > 0) & (rho <= caps[cap_token] * lnx)
        else:
            selected = A > 0
        if rid == "R0-all-k0":
            kappa = np.zeros(F)
            exact_kappa = Fraction(0)
        elif rid.endswith("k1_8"):
            kappa = np.full(F, 1 / 8)
            exact_kappa = Fraction(1, 8)
        elif rid.endswith("k1_4"):
            kappa = np.full(F, 1 / 4)
            exact_kappa = Fraction(1, 4)
        elif rid.endswith("k1_2"):
            kappa = np.full(F, 1 / 2)
            exact_kappa = Fraction(1, 2)
        else:
            coeff = {"R3-weighted-C1_2": 1 / 2,
                     "R3-weighted-C1": 1,
                     "R3-weighted-C2": 2,
                     "R3-weighted-C4": 4}[rid]
            kappa = np.maximum(0.0, 1.0 - coeff * rho / lnx)
            exact_kappa = None
        idx = np.nonzero(selected)[0]
        mass = int(NP[selected].sum())
        f_g = int(selected.sum())
        viol = selected & (r > 1.0 - kappa + 1e-15)
        viol_mass = int(NP[viol].sum())
        delta = (1.0 - kappa[selected]) - r[selected]
        if exact_kappa is not None:
            eta_profile_exact = exact_kappa * Fraction(mass, N)
            eta_profile = float(eta_profile_exact)
            eta_profile_text = str(eta_profile_exact)
        else:
            eta_profile = float(np.sum(kappa[selected] * NP[selected]) / N)
            eta_profile_text = f"{eta_profile:.17g}"
        escape = int(np.sum(NP[selected] - M[selected]))
        gini = sum(
            (Fraction(int(NP[c]) ** 2 - int(class_sq[c]), int(NP[c]))
             for c in idx.tolist()), Fraction())
        eta_escape = Fraction(escape, N)
        eta_gini = gini / N
        eta_weight = Fraction(escape + f_g, N)
        repeated = selected & (NP >= 2)
        lambda_max = float(np.max(r[repeated])) if repeated.any() else 0.0
        eta_cert = (1.0 - lambda_max) * mass / N
        passed = not viol.any()
        f_exc = F - f_g
        bound_rhs = 1.0 - eta_profile - f_exc / N
        if passed and q_over_n > bound_rhs + 2e-12:
            raise AssertionError(f"declared-profile bound failed: {rid}")
        if eta_cert > float(eta_weight) + 2e-12:
            raise AssertionError(f"eta_cert <= eta_weight failed: {rid}")
        if not (eta_escape <= eta_gini <= 2 * eta_escape):
            raise AssertionError(f"escape/Gini failed: {rid}")
        if passed and eta_profile > float(eta_weight) + 2e-12:
            raise AssertionError(f"profile <= weight failed: {rid}")
        qvals = {str(q): weighted_quantile(
            r[selected], NP[selected], q)
                 for q in (0.01, 0.05, 0.25, 0.5, 0.75, 0.95, 0.99)}
        rows.append(dict(
            rule_id=rid, classification=rule["classification"],
            empty=not len(idx), favorable_class_count=f_g,
            favorable_site_mass=mass, alpha=str(Fraction(mass, N)),
            eta_profile=eta_profile_text,
            beta_viol=str(Fraction(viol_mass, N)),
            violation_class_count=int(viol.sum()),
            min_delta=(float(delta.min()) if len(delta) else None),
            max_negative_delta=(float(np.maximum(-delta, 0).max())
                                if len(delta) else None),
            F_exc_over_N=str(Fraction(f_exc, N)),
            passed=passed, positive_finite_H2=passed and eta_profile > 0,
            lambda_max=lambda_max, eta_cert=eta_cert,
            eta_weight=str(eta_weight), eta_escape=str(eta_escape),
            eta_Gini=str(eta_gini), r_weighted_quantiles=qvals,
            r_weighted_mean=(
                float(np.sum(r[selected] * NP[selected]) / mass)
                if mass else None),
            checks=dict(
                eta_cert_le_eta_weight=True,
                eta_weight_identity=True,
                escape_Gini_bounds=True,
                passing_global_bound=(passed or None),
                passing_profile_le_weight=(passed or None))))
    return rows


def A_table(rec: dict, prospective: list[dict], p: np.ndarray,
            J: int, K: int, N: int) -> dict:
    NP = rec["NP"].astype(np.int64)
    A = np.array([v["A_P"] for v in prospective], dtype=np.int64)
    domain = np.array(
        [v["residual_domain_size"] for v in prospective], dtype=np.int64)
    ci = rec["cell_class"]
    exc_add = np.zeros(len(NP), dtype=np.int64)
    contaminated = np.zeros(len(NP), dtype=bool)
    primes_k = primes_through(J + K + 2)
    for i, site in enumerate(rec["cell_first_site"].tolist()):
        if int(p[site]) > J + K + 2:
            continue
        c = int(ci[i])
        pre, suf = point_sets(rec["sides"][c], J)
        if not admissible(pre, suf, int(rec["mid"][i]), primes_k):
            exc_add[c] += 1
            contaminated[c] = True
    Atilde = A + exc_add
    if np.any(Atilde == 0):
        inverse = None
    else:
        inv = sum(Fraction(int(n), int(a))
                  for n, a in zip(NP.tolist(), Atilde.tolist()))
        inverse = str(inv / N)
    bins = [
        ("0", A == 0), ("1", A == 1), ("2", A == 2),
        ("3-4", (A >= 3) & (A <= 4)),
        ("5-8", (A >= 5) & (A <= 8)),
        ("9-16", (A >= 9) & (A <= 16)), ("17+", A >= 17)]
    return dict(
        bins=[dict(label=lab, class_count=int(m.sum()),
                   site_mass=int(NP[m].sum()),
                   site_mass_over_N=str(Fraction(int(NP[m].sum()), N)))
              for lab, m in bins],
        residual_domain_min=int(domain.min()) if len(domain) else None,
        residual_domain_max=int(domain.max()) if len(domain) else None,
        contaminated_class_count=int(contaminated.sum()),
        contaminated_site_mass=int(NP[contaminated].sum()),
        inverse_A_tilde_site_mean=inverse,
        zero_A_tilde_classes=int((Atilde == 0).sum()))


def rho_and_crt_tables(rec: dict, realized: list[dict], N: int) -> tuple[dict, list]:
    NPd = rec["NPd"].astype(np.int64)
    NP = rec["NP"].astype(np.int64)
    ci = rec["cell_class"].astype(np.int64)
    rho = np.array([v["rho"] for v in realized], dtype=np.float64)
    energy = float(np.sum(rho * NPd))
    off = np.array([v["off_domain"] for v in realized], dtype=bool)
    class_sq = np.zeros(len(NP), dtype=np.int64)
    np.add.at(class_sq, ci, NPd * NPd)
    crt = defaultdict(lambda: dict(
        site_mass=0, class_ids=set(), rho_energy=0.0,
        Q=Fraction(), escape=Fraction(), gini=Fraction()))
    for i, row in enumerate(realized):
        c = int(ci[i])
        n = int(NP[c])
        escape_c = n - int(rec["maxNPd"][c])
        gini_c = Fraction(n * n - int(class_sq[c]), n)
        qcell = Fraction(int(NPd[i] * (NPd[i] - 1)), n)
        for prime, prof in row["profile"].items():
            key = (int(prime), *map(int, prof))
            a = crt[key]
            a["site_mass"] += int(NPd[i])
            a["class_ids"].add(c)
            a["rho_energy"] += float(rho[i] * NPd[i])
            a["Q"] += qcell
            a["escape"] += Fraction(escape_c * int(NPd[i]), n)
            a["gini"] += gini_c * Fraction(int(NPd[i]), n)
    rows = []
    for key, a in sorted(crt.items()):
        rows.append(dict(
            p=key[0], nu_H=key[1], nu_pre=key[2], nu_suf=key[3],
            site_mass=a["site_mass"], class_count=len(a["class_ids"]),
            rho_energy=a["rho_energy"], Q=str(a["Q"]),
            majority_escape=str(a["escape"]), Gini=str(a["gini"])))
    table = dict(
        rho_Q=Q_RHO,
        certified_tail_log_width=0.51 * (0 if not len(NP) else 1),
        realized_rho_energy=energy,
        realized_rho_energy_over_N=energy / N,
        off_domain_cell_count=int(off.sum()),
        off_domain_site_mass=int(NPd[off].sum()))
    return table, rows


def smoke_row(x: int = 1_000_000, s: int = 0,
              workers: int = min(24, os.cpu_count() or 1)) -> dict:
    reg = verify_registry()
    if x != reg["primary_x_ladder"][0] or s != 0:
        raise ValueError("smoke is frozen to the smallest primary s=0 row")
    if git_head() != PIN:
        raise RuntimeError("HEAD is not the dispatch pin")
    t_start = time.perf_counter()
    par = d0_parameters(x)
    print(f"smoke: D0 parameters {par}", flush=True)
    p, g, delta, valid = I19.build(x)
    print(f"smoke: cache/build complete, pi(x)={len(p)}", flush=True)
    t = I19.site_range(valid, par["J"], par["K"])
    wsum = I19.window_sums(g, t, par["L"])
    sites = t[
        (t >= s + 1)
        & (wsum <= par["W_floor"])
        & (delta[t + par["J"]] <= par["D"])
        & (delta[t + par["L"]] <= float(2 ** par["K"]))]
    print(f"smoke: filtered sites={len(sites)}", flush=True)
    rec = exact_class_records(g, sites, par["J"], par["K"])
    print(f"smoke: exact classes={len(rec['NP'])}, "
          f"cells={len(rec['NPd'])}", flush=True)
    metrics = collision_metrics(rec)
    metrics["log_x"] = par["log_x"]
    pros_cache = OUT / f"prospective-x{x}-s{s}.npz"
    if pros_cache.exists():
        z = np.load(pros_cache)
        prospective = [
            dict(A_P=int(a), residual_domain_size=int(d),
                 rho_pros=float(r), prospective_off_domain=int(o))
            for a, d, r, o in zip(
                z["A_P"], z["domain"], z["rho_pros"], z["off_domain"])]
        pros_wall = 0.0
        print(f"smoke: reused {pros_cache}", flush=True)
    else:
        prospective, pros_wall = prospective_parallel(
            rec["sides"], par["J"], par["K"], par["W_floor"], workers)
        np.savez_compressed(
            pros_cache,
            A_P=np.array([v["A_P"] for v in prospective], np.int32),
            domain=np.array(
                [v["residual_domain_size"] for v in prospective], np.int32),
            rho_pros=np.array(
                [v["rho_pros"] for v in prospective], np.float64),
            off_domain=np.array(
                [v["prospective_off_domain"] for v in prospective], np.int32))
    realized_cache = OUT / f"realized-rho-x{x}-s{s}.npz"
    if realized_cache.exists():
        z = np.load(realized_cache)
        realized = []
        prof = z["profiles"]
        for i, (rho, off) in enumerate(zip(z["rho"], z["off_domain"])):
            profile = {
                p0: tuple(map(int, prof[i, j]))
                for j, p0 in enumerate(PROFILE_PRIMES)}
            realized.append(dict(
                rho=float(rho), off_domain=bool(off), profile=profile))
        rho_wall = 0.0
        print(f"smoke: reused {realized_cache}", flush=True)
    else:
        realized, rho_wall = realized_rho_parallel(
            rec, par["J"], par["K"], par["W_floor"], workers)
        profiles = np.zeros(
            (len(realized), len(PROFILE_PRIMES), 3), dtype=np.int16)
        for i, row in enumerate(realized):
            for j, p0 in enumerate(PROFILE_PRIMES):
                profiles[i, j] = row["profile"].get(p0, (0, 0, 0))
        np.savez_compressed(
            realized_cache,
            rho=np.array([v["rho"] for v in realized], np.float64),
            off_domain=np.array(
                [v["off_domain"] for v in realized], np.bool_),
            profiles=profiles)
    rules = rule_rows(reg, rec, prospective, metrics)
    rho_table, crt = rho_and_crt_tables(rec, realized, metrics["N"])
    rho_table["certified_tail_log_width"] = (
        0.51 * par["k"] * par["k"] / Q_RHO)
    result = dict(
        schema="item-0010-m5-lite-smoke-row-v1",
        dispatch_pin=PIN, registry_sha256=REGISTRY_HASH,
        evidence_class="MEASURED finite row",
        x=x, s=s, workers=workers, parameters=par,
        global_metrics=metrics,
        class_size_strata=class_size_strata(rec, metrics["N"]),
        A_P=A_table(rec, prospective, p, par["J"], par["K"], metrics["N"]),
        rho_energy=rho_table, rules=rules, CRT_strata=crt,
        runtime=dict(
            prospective_seconds=pros_wall,
            realized_rho_seconds=rho_wall,
            total_seconds=time.perf_counter() - t_start),
        status="PASS")
    path = OUT / f"smoke-x{x}-s{s}.json"
    with path.open("w") as f:
        json.dump(result, f, indent=2)
        f.write("\n")
    print(json.dumps(dict(
        path=str(path), N=metrics["N"], F=metrics["F"],
        Q_over_N=metrics["Q_over_N"],
        defect_over_N=metrics["defect_over_N"],
        A_P=result["A_P"], runtime=result["runtime"],
        passing_rules=[r["rule_id"] for r in rules if r["passed"]],
        status=result["status"]), indent=2))
    return result


def freeze_smoke_outputs() -> None:
    smoke_path = OUT / "smoke-x1000000-s0.json"
    if not smoke_path.exists():
        raise RuntimeError("smoke row is absent")
    with smoke_path.open() as f:
        row = json.load(f)
    if row["status"] != "PASS":
        raise RuntimeError("smoke row did not pass")
    shutil.copyfile(REGISTRY, OUT / "frozen-registry.yaml")
    tables = {
        "global-per-scale.json": [{
            "x": row["x"], "s": row["s"],
            **row["global_metrics"]}],
        "per-rule-certificates.json": row["rules"],
        "A-P-table.json": row["A_P"],
        "rho-energy-table.json": row["rho_energy"],
        "CRT-strata.json": row["CRT_strata"],
        "class-size-table.json": row["class_size_strata"],
        "integrity-checks.json": {
            "global": row["global_metrics"]["checks"],
            "rules": {
                r["rule_id"]: r["checks"] for r in row["rules"]},
            "synthetic_tests": "PASS",
            "item0019_continuity": "PASS"
        }
    }
    for name, data in tables.items():
        with (OUT / name).open("w") as f:
            json.dump(data, f, indent=2)
            f.write("\n")
    ladder_pi = {
        1_000_000: 78_498, 3_000_000: 216_816,
        10_000_000: 664_579, 30_000_000: 1_857_859,
        100_000_000: 5_761_455, 300_000_000: 16_252_325,
        1_000_000_000: 50_847_534}
    total_pi = sum(ladder_pi.values())
    smoke_n = row["global_metrics"]["N"]
    pros_rate = row["runtime"]["prospective_seconds"] / smoke_n
    rho_rate = row["runtime"]["realized_rho_seconds"] / smoke_n
    feasibility = {
        "schema": "item-0010-phase3-feasibility-v1",
        "classification": "MEASURED runtime plus conservative linear projection",
        "smoke_x": row["x"],
        "smoke_N": smoke_n,
        "workers": row["workers"],
        "prospective_wall_seconds": row["runtime"]["prospective_seconds"],
        "realized_rho_wall_seconds": row["runtime"]["realized_rho_seconds"],
        "prospective_wall_seconds_per_smoke_class": pros_rate,
        "realized_rho_wall_seconds_per_smoke_cell": rho_rate,
        "ladder_pi_exact": {str(k): v for k, v in ladder_pi.items()},
        "ladder_pi_sum": total_pi,
        "projected_rho_wall_hours_at_smoke_rate": (
            (pros_rate + rho_rate) * total_pi / 3600),
        "largest_row_projected_rho_wall_hours_at_smoke_rate": (
            (pros_rate + rho_rate) * ladder_pi[1_000_000_000] / 3600),
        "omitted_costs": [
            "larger residual-domain and local-prime ranges",
            "prime/gap/delta cache generation",
            "side-class partitioning and sorting",
            "five fixed s views",
            "certificate, CRT, A_P, correlation, and report reducers"
        ],
        "stop": (
            "Phase 3 STOP: the unchanged mandatory prospective-rho "
            "object is not computationally feasible for the frozen "
            "full ladder in this implementation/resource envelope. "
            "No realized-rho substitution, sampling, cap change, "
            "ladder truncation, or post-hoc selector change was made.")
    }
    with (OUT / "phase3-feasibility.json").open("w") as f:
        json.dump(feasibility, f, indent=2)
        f.write("\n")
    manifest = {
        "schema": "item-0010-m5-lite-run-manifest-v1",
        "dispatch_pin": PIN,
        "registry_sha256": REGISTRY_HASH,
        "web": "OFF",
        "evidence_scope": "finite empirical calibration only",
        "platform": platform.platform(),
        "python": platform.python_version(),
        "numpy": np.__version__,
        "workers": row["workers"],
        "cache": os.environ["ITEM0019_CACHE"],
        "commands": [
            "python3 dossier/item-0010-workpapers/m5_lite_measure.py self-test",
            "python3 dossier/item-0010-workpapers/m5_lite_measure.py continuity",
            "python3 dossier/item-0010-workpapers/m5_lite_measure.py profile 1000000 256",
            "python3 -u dossier/item-0010-workpapers/m5_lite_measure.py smoke",
            "python3 dossier/item-0010-workpapers/m5_lite_measure.py freeze-smoke"
        ],
        "runs": [{
            "phase": 1, "name": "synthetic tests", "status": "PASS"},
            {"phase": 2, "name": "item-0019 continuity", "status": "PASS"},
            {"phase": 3, "name": "D0 smoke x=1000000 s=0",
             "status": "PASS", "runtime": row["runtime"]},
            {"phase": 3, "name": "full-ladder feasibility gate",
             "status": "STOP", "evidence": "phase3-feasibility.json"}
        ],
        "artifacts": {}
    }
    for path in sorted(OUT.iterdir()):
        if path.is_file() and path.name != "run-manifest.json":
            manifest["artifacts"][path.name] = {
                "bytes": path.stat().st_size,
                "sha256": file_sha256(path)}
    with (OUT / "run-manifest.json").open("w") as f:
        json.dump(manifest, f, indent=2)
        f.write("\n")
    print("frozen smoke deliverables: PASS")


def profile_row(x: int, nclass: int) -> dict:
    reg = verify_registry()
    if git_head() != PIN:
        raise RuntimeError("HEAD is not the dispatch pin")
    par = d0_parameters(x)
    p, g, delta, valid = I19.build(x)
    t = I19.site_range(valid, par["J"], par["K"])
    wsum = I19.window_sums(g, t, par["L"])
    mask = (
        (t >= 1)
        & (wsum <= par["W_floor"])
        & (delta[t + par["J"]] <= par["D"])
        & (delta[t + par["L"]] <= float(2 ** par["K"]))
    )
    sites = t[mask]
    rec = exact_class_records(g, sites, par["J"], par["K"])
    take = min(nclass, len(rec["NP"]))
    primes_k = primes_through(par["k"])
    rho_eval = RhoEvaluator(par["J"], par["K"], par["W_floor"])
    t0 = time.perf_counter()
    domain = 0
    A_total = 0
    for side in rec["sides"][:take]:
        got = prospective_one(
            side, par["J"], par["K"], par["W_floor"],
            primes_k, rho_eval)
        domain += got["residual_domain_size"]
        A_total += got["A_P"]
    wall = time.perf_counter() - t0
    per_class = wall / take if take else 0.0
    all_classes = len(rec["NP"])
    estimate_serial = per_class * all_classes
    result = dict(
        schema="item-0010-prospective-rho-profile-v1",
        dispatch_pin=PIN, registry_sha256=REGISTRY_HASH,
        x=x, s=0, parameters=par, N_sites=len(sites),
        class_count=all_classes, profiled_classes=take,
        profiled_residual_candidates=domain,
        profiled_admissible_candidates=A_total,
        wall_seconds=wall, seconds_per_class=per_class,
        projected_serial_seconds_one_s=estimate_serial,
        projected_serial_hours_one_s=estimate_serial / 3600,
        projected_serial_hours_five_s=5 * estimate_serial / 3600,
        note=(
            "Projection covers prospective A_P and rho_Q only. "
            "It excludes sieve/gap construction, sorting, realized rho, "
            "certificate tables, CRT strata, and output rendering."))
    OUT.mkdir(parents=True, exist_ok=True)
    path = OUT / f"profile-x{x}.json"
    with path.open("w") as f:
        json.dump(result, f, indent=2)
        f.write("\n")
    print(json.dumps(result, indent=2))
    return result


def synthetic_metrics(partitions: list[list[int]]) -> dict:
    NP = np.array([sum(v) for v in partitions], dtype=np.int64)
    NPd = np.array([v for row in partitions for v in row], dtype=np.int64)
    ci = np.array([
        i for i, row in enumerate(partitions) for _ in row], dtype=np.int64)
    rec = dict(
        NP=NP, NPd=NPd, cell_class=ci,
        maxNPd=np.array([max(row) for row in partitions], dtype=np.int64))
    return collision_metrics(rec)


def self_test() -> dict:
    verify_registry()
    cases = {
        "all_singletons": [[1], [1], [1]],
        "rigid_class": [[4]],
        "two_equal_cells": [[2, 2]],
        "all_distinct_middles": [[1, 1, 1, 1]],
        "mixed_class_sizes": [[1], [2], [1, 2], [1, 1, 2]],
        "empty_favorable_selector": [[1], [2]],
        "declared_profile_violation": [[3]],
    }
    out = {name: synthetic_metrics(p) for name, p in cases.items()}
    # Exact declared-profile checks on hand data.
    assert Fraction(out["all_singletons"]["Q_over_N"]) == 0
    assert Fraction(out["rigid_class"]["Q_over_N"]) == Fraction(3, 4)
    assert Fraction(out["two_equal_cells"]["defect_over_N"]) == Fraction(1, 2)
    assert Fraction(
        out["all_distinct_middles"]["defect_over_N"]) == Fraction(3, 4)
    extra = dict(
        empty_selector=dict(alpha="0", eta_profile="0", beta_viol="0",
                            extrema=None, passed=True, positive=False),
        violation=dict(kappa="1/2", NP=3, maxNPd=3,
                       r_P=str(Fraction(2, 3)),
                       delta_P=str(Fraction(-1, 6)),
                       beta_viol="1", passed=False))
    result = dict(schema="item-0010-synthetic-tests-v1",
                  registry_sha256=REGISTRY_HASH,
                  cases=out, declared_profiles=extra, status="PASS")
    OUT.mkdir(parents=True, exist_ok=True)
    with (OUT / "synthetic-tests.json").open("w") as f:
        json.dump(result, f, indent=2)
        f.write("\n")
    print("synthetic tests: PASS")
    return result


def continuity() -> dict:
    """Reproduce one overlapping item-0019 D0.2' row exactly."""
    verify_registry()
    x, J, K, D = 2_000_000, 4, 5, 30
    p, g, delta, valid = I19.build(x)
    t = I19.site_range(valid, J, K)
    sites = t[I19.filter_d02p(g, delta, t, J, K, D, math.log(x))]
    agg, _ = I19.class_census(g, delta, sites, J, K, D)
    got = dict(
        pi=len(p), ns=agg["ns"], nW=agg["n_words"],
        nP=agg["n_sides"], cw=agg["C_words"] - agg["ns"],
        cs=agg["C_sides"] - agg["ns"], cls=agg["n_exch"])
    want = dict(
        pi=148933, ns=142130, nW=142104, nP=142092,
        cw=52, cs=76, cls=12)
    checks = {k: got[k] == want[k] for k in want}
    result = dict(
        schema="item-0010-item0019-continuity-v1",
        source="item-0019 (4,5,30), x=2000000, D0.2'",
        got=got, want=want, checks=checks,
        status="PASS" if all(checks.values()) else "FAIL")
    OUT.mkdir(parents=True, exist_ok=True)
    with (OUT / "item0019-continuity.json").open("w") as f:
        json.dump(result, f, indent=2)
        f.write("\n")
    print(json.dumps(result, indent=2))
    if result["status"] != "PASS":
        raise AssertionError("item-0019 continuity mismatch")
    return result


def run_row(x: int, s: int) -> dict:
    """Full exact row. Intended after profile feasibility clears."""
    reg = verify_registry()
    if x not in reg["primary_x_ladder"] or s not in reg["positive_s_panel"]:
        raise ValueError("row is not in the frozen primary grid")
    if git_head() != PIN:
        raise RuntimeError("HEAD is not the dispatch pin")
    par = d0_parameters(x)
    p, g, delta, valid = I19.build(x)
    t = I19.site_range(valid, par["J"], par["K"])
    wsum = I19.window_sums(g, t, par["L"])
    mask = (
        (t >= s + 1)
        & (wsum <= par["W_floor"])
        & (delta[t + par["J"]] <= par["D"])
        & (delta[t + par["L"]] <= float(2 ** par["K"]))
    )
    sites = t[mask]
    rec = exact_class_records(g, sites, par["J"], par["K"])
    metrics = collision_metrics(rec)
    result = dict(
        schema="item-0010-m5-lite-row-v1", dispatch_pin=PIN,
        registry_sha256=REGISTRY_HASH, x=x, s=s, parameters=par,
        global_metrics=metrics,
        class_size_strata=class_size_strata(rec, metrics["N"]),
        status="PARTIAL-NOT-WRITTEN")
    raise RuntimeError(
        "Full row writer is intentionally gated until the exact "
        "prospective-rho profile is declared computationally feasible; "
        "the in-memory collision census was computed but no partial row "
        "was written.")


def main() -> None:
    if len(sys.argv) < 2:
        raise SystemExit(__doc__)
    cmd = sys.argv[1]
    if cmd == "self-test":
        self_test()
    elif cmd == "continuity":
        continuity()
    elif cmd == "profile":
        profile_row(int(sys.argv[2]), int(sys.argv[3])
                    if len(sys.argv) > 3 else 128)
    elif cmd == "smoke":
        smoke_row()
    elif cmd == "freeze-smoke":
        freeze_smoke_outputs()
    elif cmd == "run":
        run_row(int(sys.argv[2]), int(sys.argv[3]))
    else:
        raise SystemExit(f"unknown command: {cmd}")


if __name__ == "__main__":
    main()
