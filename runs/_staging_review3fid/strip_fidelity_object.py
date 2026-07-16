#!/usr/bin/env python3
"""Derive the blind transcription-fidelity object (three parts).

Deterministic, assertion-enforced anchor stripping, following the
strip_review_copy.py precedent (R2 arms). Sources at the pinned commit:
  Part I   dossier/chain-v1.md            (sections 1, 2, 4, 5)
  Part II  lean/Erdos251/Counting.lean    (the statement set under check)
  Part III lean/Erdos251/Hypotheses.lean + four Basic.lean definitions
           (frozen context so every Part-II symbol resolves)

Removed everywhere: prior-verdict and per-claim tags, amendment brackets
and version markers (they localize former defects), process/item/ledger
vocabulary, the provenance machinery. Mathematical content -- including
necessity counterexamples and flagged statement deviations -- is
preserved; brackets that mixed mathematics with process are rewritten to
keep exactly the mathematics. All transformations are literal or
count-asserted; re-run at the pin reproduces the object byte-identically
(operator sha256 canonical).

Usage: strip_fidelity_object.py <chain-v1.md> <Counting.lean> \
       <Hypotheses.lean> <Basic.lean> <output.md>
"""
import re
import sys

HEADER = """# Transcription-fidelity object: counting layer and deletion construction

Three parts. Part I is the prose source (sections 1, 2, 4, 5 of a
conditional-proof document; sections 3 and 6-9 exist but are outside
this object). Part II is a Lean 4 statement file claiming to transcribe
prose sections 4-5; it is the object under assessment. Part III is the
frozen Lean context Part II imports (NOT under assessment; provided so
every symbol resolves). Pointers in Part II to "section 6" refer to the
out-of-scope assembly and are to be treated as opaque.
"""

# ---------------------------------------------------------------- Part I

I_LITERALS = [
    ("Design note (review-2 lesson):", "Design note:", 1),
    ("Remark on strength (review-1 P1):", "Remark on strength:", 1),
    ("LEMMA 2.1 (convergence; repair R1).", "LEMMA 2.1 (convergence).", 1),
    ("Thm 8 area; citation verification tracked in\nitem-0004)",
     "Thm 8 area; citation verification pending)", 1),
    ("the bound p_n <= 2^n alone would not -- review-1 A04/A12.)",
     "the bound p_n <= 2^n alone would not.)", 1),
    ("LEMMA 2.3 (lattice and parity; repair R2).",
     "LEMMA 2.3 (lattice and parity).", 1),
    ("removes the edge -- review-1 A17.)", "removes the edge.)", 1),
    ("Proof sketch (review-1 A36-A40):", "Proof sketch:", 1),
    ("Mertens' theorems (classical: Mertens 1874; Rosser-Schoenfeld 1962) --\n"
     "repair R3: these are now CITED, not asserted bare; exact-constant\n"
     "verification tracked in item-0004. QED-sketch",
     "Mertens' theorems (classical: Mertens 1874; Rosser-Schoenfeld 1962);\n"
     "exact-constant verification pending. QED-sketch", 1),
    ("LEMMA 4.2 (one-point extension sum; v1.1).",
     "LEMMA 4.2 (one-point extension sum).", 1),
    ("Proof sketch (review-1 A41-A43):", "Proof sketch:", 1),
    ("[v1.2: the earlier sketch asserted the kappa-uniform bounds \"number\n"
     "<= 3k\" and \"product <= e^2\"; both FAIL for large fixed kappa\n"
     "(H = {0, 10014}, t = 10010 = 2*5*7*11*13 has four colliding primes at\n"
     "k = 1; a highly composite t drives the collision product past e^2 --\n"
     "prod_{5<=p<=10^6} p/(p-1) = 8.202... > e^2 = 7.389...). Found by the\n"
     "blind re-review R2a, steering-re-executed; the lemma STATEMENT is\n"
     "unaffected. A sharper witness needs only kappa >= 405: H = {0, 444},\n"
     "t = 70, colliding primes {5, 7, 11, 17} (independent find of re-review\n"
     "R2b, steering-re-executed). ANN-22/23.]",
     "[Note: kappa-uniform bounds \"number <= 3k\" and \"product <= e^2\"\n"
     "FAIL for large fixed kappa (H = {0, 10014}, t = 10010 = 2*5*7*11*13\n"
     "has four colliding primes at k = 1; a highly composite t drives the\n"
     "collision product past e^2 -- prod_{5<=p<=10^6} p/(p-1) = 8.202... >\n"
     "e^2 = 7.389...; a sharper witness needs only kappa >= 405:\n"
     "H = {0, 444}, t = 70, colliding primes {5, 7, 11, 17}); the O_kappa\n"
     "forms above are the honest ones.]", 1),
    ("[v1.1/F2: the span hypothesis is NECESSARY, not cosmetic. For H = {0, D}\n"
     "(k = 1) every admissible even t has ratio >= 1.2 (the p = 2 factor alone\n"
     "is 2) and there are ~D/2 such t, so the sum grows like D against a\n"
     "D-free right side; the unrestricted v1.0 claim is FALSE. Surfaced by the\n"
     "item-0014 skeleton pass and steering-verified numerically (ANN-20);\n"
     "review-1 A41-A43 had passed the v1.0 form.]",
     "[Note: the span hypothesis is NECESSARY, not cosmetic. For H = {0, D}\n"
     "(k = 1) every admissible even t has ratio >= 1.2 (the p = 2 factor\n"
     "alone is 2) and there are ~D/2 such t, so the sum grows like D against\n"
     "a D-free right side; the unrestricted claim is FALSE.]", 1),
    ("LEMMA 4.3 (consecutive lower bound; the transfer; v1.1).",
     "LEMMA 4.3 (consecutive lower bound; the transfer).", 1),
    ("composite for p > x^{1/2} -- review-1 A44).",
     "composite for p > x^{1/2}).", 1),
    ("(L+2 points, +1 -- repair R5: the cardinalities",
     "(L+2 points, +1 -- the cardinalities", 1),
    ("[v1.1/F2: the span hypothesis is narrowed from the v1.0 form\n"
     "span <= (ln x)^3. The wide form is unprovable by this route (Lemma 4.2's\n"
     "sum genuinely grows with the span) and heuristically false outright for\n"
     "span >> ln x, where consecutive realizations carry a Cramer-type\n"
     "e^{-span/ln x} thinning absent from M_H. Section 5(iii) supplies exactly\n"
     "the narrow form.]",
     "[Note: the wide form span <= (ln x)^3 is unprovable by this route\n"
     "(Lemma 4.2's sum genuinely grows with the span) and heuristically false\n"
     "outright for span >> ln x, where consecutive realizations carry a\n"
     "Cramer-type e^{-span/ln x} thinning absent from M_H. Section 5(iii)\n"
     "supplies exactly the narrow form.]", 1),
    ("[EXPLICIT one-line lemma per review-2 P2, stated here",
     "[EXPLICIT one-line lemma, stated here", 1),
    ("i_0 = J + 1 (v1.1; interior with slack:",
     "i_0 = J + 1 (interior with slack:", 1),
    ("(translation changes neither gaps nor\nadmissibility; re-review R2, v1.2)",
     "(translation changes neither gaps nor\nadmissibility)", 1),
    ("orientation -- direct computation (review-1 A53; orientation\n"
     "corrected v1.2, re-review R2).",
     "orientation -- direct computation.", 1),
    ("there are only L+1 < p points (review-1 A54).",
     "there are only L+1 < p points.", 1),
]

I_DELETE_BLOCKS = [
    # 5(i) amendment bracket: pure history localizing a former defect.
    ("[v1.1/F1: i_0 corrected from the v1.0 value J + 2, under which the words\n"
     "share a length-(J+1) prefix and only a length-(K-1) suffix, the fork\n"
     "sits one slot late, claim (i) fails (at K = 1 the shared suffix even\n"
     "collapses to 0), and FM-1 downstream loses a factor 2 that section 6\n"
     "cannot supply (its tails are <= H_x <= 2^K only). With i_0 = J + 1\n"
     "claim (i) is true as written; verified numerically over several (J, K)\n"
     "pairs (ANN-20). Review-1 A53 had passed the v1.0 value.]\n", 1),
]

I_BANNED = ["v1.0", "v1.1", "v1.2", "v1.3", "review", "Review", "repair",
            "Repair", "item-00", "ANN-", "steering", "R2a", "R2b",
            "kickoff", "fable", "gpt", "Claude", "triage", "ledger"]

I_REQUIRED = ["HYPOTHESIS A", "HYPOTHESIS B", "LEMMA 4.1", "LEMMA 4.2",
              "LEMMA 4.3", "LEMMA 4.4", "## 5. The deletion construction",
              "i_0 = J + 1", "kappa k ln(k+2)", "kappa L ln(L+2)",
              "N_cons >= pi_H(x)", "delta_n := u_n - p_{n+1}",
              "H(w) = A - q_0", "the unrestricted claim is FALSE"]


def part_one(chain: str) -> str:
    m1 = chain.find("## 1. Main statement")
    m3 = chain.find("## 3. Fork-merge")
    m4 = chain.find("## 4. Counting layer")
    m6 = chain.find("## 6. Assembly")
    assert 0 < m1 < m3 < m4 < m6, "section landmarks not found in order"
    text = chain[m1:m3] + chain[m4:m6]
    for old, count in I_DELETE_BLOCKS:
        found = text.count(old)
        assert found == count, f"delete-block x{found} (want {count})"
        text = text.replace(old, "")
    for old, new, count in I_LITERALS:
        found = text.count(old)
        assert found == count, f"literal x{found} (want {count}): {old[:48]!r}"
        text = text.replace(old, new)
    text = re.sub(r"\n{3,}", "\n\n", text).rstrip() + "\n"
    for token in I_BANNED:
        assert token not in text, f"Part I banned token survived: {token!r}"
    for token in I_REQUIRED:
        assert token in text, f"Part I required content missing: {token!r}"
    text.encode("ascii")
    return text


# --------------------------------------------------------------- Part II

II_INTRO_OLD_RE = (
    r"/-!\n# Counting layer and deletion construction \(chain-v1 v1\.3, "
    r"sections 4-5\)\n\nSTATEMENT SKELETON \(item-0014\).*?"
    r"conventions from section 8\.2 and the landed `Hypotheses\.lean`\.")
II_INTRO_NEW = (
    "/-!\n# Counting layer and deletion construction (prose sections 4-5)\n\n"
    "STATEMENT SKELETON. Definitions are real; the lemmata are intentional,\n"
    "named `sorry`s: the statement set is the object under transcription\n"
    "assessment against Part I.\n\n"
    "Source of truth: Part I of this object (prose sections 1, 2, 4, 5);\n"
    "hypothesis-layer context in Part III.")

II_LITERALS = [
    ("## Traceability table (MANDATORY, item-0014 kickoff v2)",
     "## Traceability table", 1),
    ("| chain-v1 v1.3 ref        |", "| prose ref                |", 1),
    ("| LEMMA 4.2 (v1.1)         |", "| LEMMA 4.2                |", 1),
    ("| LEMMA 4.3 (v1.1)         |", "| LEMMA 4.3                |", 1),
    ("`i_0 = J+1` (v1.1/F1)", "`i_0 = J+1`", 1),
    ("Smoke tests: four `example`s\nreproducing the review-verified tables",
     "Smoke tests: four `example`s\nat the concrete tables", 1),
    ("the 0-based\nhandoff object Lemma 4.3 and Hypothesis A receive "
     "(v1.2, re-review R2);",
     "the 0-based\nhandoff object Lemma 4.3 and Hypothesis A receive;", 1),
    ("which is prose and is NOT transcribed -- see the report).",
     "which is prose and is NOT transcribed).", 1),
    ("/-- LEMMA 4.2 (one-point extension sum; v1.1). For any fixed",
     "/-- LEMMA 4.2 (one-point extension sum). For any fixed", 1),
    ("The span hypothesis is NECESSARY, not cosmetic (v1.1/F2): for",
     "The span hypothesis is NECESSARY, not cosmetic: for", 1),
    ("/-- LEMMA 4.3 (consecutive lower bound; the transfer; v1.1). Let",
     "/-- LEMMA 4.3 (consecutive lower bound; the transfer). Let", 1),
    ("The span hypothesis is 4.2's, with `k = L` (v1.1/F2): the wide v1.0 form",
     "The span hypothesis is 4.2's, with `k = L`: the wide form", 1),
    ("`i_0 = J + 1` (v1.1/F1; the v1.0 value\nwas `J + 2`). Interior",
     "`i_0 = J + 1`. Interior", 1),
    ("(see the report's\ndefinitional choices). `cElem J K 0 = q_0`",
     ". `cElem J K 0 = q_0`", 1),
    ("the signs are not\n\"fixed\" here (v1.2, re-review R2). -/",
     "the signs are not\n\"fixed\" here. -/", 1),
    ("/-! ### Smoke tests (ENCOURAGED by the kickoff; review-verified tables)",
     "/-! ### Smoke tests (concrete tables)", 1),
]

II_BANNED = ["item-00", "ANN-", "kickoff", "v1.0", "v1.1", "v1.2", "v1.3",
             "review", "chain-v1", "triage", "gpt", "steering", "ledger",
             "MANDATORY", "sha256", "1dda542d"]

II_REQUIRED = [
    "singularSeries_lower_bound", "oneExtension_sum_le",
    "consCount_lower_bound", "delta_le_of_gap_bound", "cword_prefix",
    "cword_fork", "cword_suffix", "cword_admissible", "cspan_le",
    "cfm2_tendsto", "cbudget", "constr_consCount_pos", "q_eq_of_count",
    "## Traceability table"]


def part_two(lean: str) -> str:
    m = re.search(II_INTRO_OLD_RE, lean, re.DOTALL)
    assert m, "Part II intro block not found"
    text = lean[:m.start()] + II_INTRO_NEW + lean[m.end():]

    blocks = re.findall(r"\n## Amendment context.*?(?=\n-/)", text, re.DOTALL)
    assert len(blocks) == 1, f"amendment block x{len(blocks)} (want 1)"
    text = re.sub(r"\n## Amendment context.*?(?=\n-/)", "\n", text,
                  flags=re.DOTALL)

    for old, new, count in II_LITERALS:
        found = text.count(old)
        assert found == count, f"literal x{found} (want {count}): {old[:48]!r}"
        text = text.replace(old, new)
    text = re.sub(r"\n{3,}", "\n\n", text)

    for token in II_BANNED:
        assert token not in text, f"Part II banned token survived: {token!r}"
    for token in II_REQUIRED:
        assert token in text, f"Part II required content missing: {token!r}"
    n_sorry = len(re.findall(r"^\s*sorry\s*$", text, re.MULTILINE))
    assert n_sorry == 12, f"Part II sorry count {n_sorry} (want 12)"
    return text.rstrip() + "\n"


# -------------------------------------------------------------- Part III

III_HYP_INTRO_RE = r"/-!\n# Hypothesis layer.*?(?=\n-/)"
III_HYP_INTRO_NEW = """/-!
# Hypothesis layer (prose section 1): `HLQuantA` and `CramerGranville`

FROZEN context for Part II; NOT under assessment. Hypothesis A counts
NONCONSECUTIVE admissible tuples; consecutiveness is DERIVED downstream
(Lemma 4.3), never assumed.

Faithfulness notes:
* the prose Hypothesis A displays a constant `C_A >= 1` that its
  inequality never uses; flagged as vestigial, not encoded.
* `singularSeries` is a `tprod`, which mathlib defaults to 1 when not
  `Multipliable`; for admissible `H` the product IS multipliable
  (`singularSeries_multipliable`), so the Lean `HLQuantA` matches the
  paper hypothesis.
"""

III_LITERALS = [
    ("(chain-v1 section 1).", "(prose section 1).", 1),
    ("HYPOTHESIS A (chain-v1 section 1):", "HYPOTHESIS A (prose section 1):", 1),
    ("HYPOTHESIS B (chain-v1 section 1):", "HYPOTHESIS B (prose section 1):", 1),
    ("(chain-v1 Lemma 4.1 direction;", "(prose Lemma 4.1 direction;", 1),
    ("(chain-v1 Lemma 4.2, section 5(iii))",
     "(prose Lemma 4.2, section 5(iii))", 0),  # tolerated absent
]

III_BASIC_ANCHORS = [
    "/-- 0-indexed primes: `q 0 = 2`, `q 1 = 3`, ... (paper `p_{n+1}`). -/\n"
    "def q (n : \u2115) : \u2115 := Nat.nth Nat.Prime n\n",
    "/-- Prime gap, 0-indexed: `gap n` = paper `g_{n+1}`; `gap 0 = 1`. -/\n"
    "def gap (n : \u2115) : \u2115 := q (n + 1) - q n\n",
    "/-- Tail transform (= paper `delta_n`): weighted average of future gaps. -/\n"
    "def delta (n : \u2115) : \u211d := \u2211' j : \u2115, (gap (n + j) : \u211d) / 2 ^ (j + 1)\n",
    "/-- Two indices carry the same length-`J` gap word (template 9.1). -/\n"
    "def SameBlock (n m J : \u2115) : Prop := \u2200 i, i < J \u2192 gap (n + i) = gap (m + i)\n",
]

III_BANNED = ["item-00", "ANN-", "chain-v1", "review", "triage", "gpt",
              "round-0", "ledger", "v1.0", "v1.1"]


def part_three(hyp: str, basic: str) -> str:
    snippets = []
    for anchor in III_BASIC_ANCHORS:
        found = basic.count(anchor)
        assert found == 1, f"Basic anchor x{found} (want 1): {anchor[:40]!r}"
        snippets.append(anchor)
    basics = ("-- Base definitions (Basic.lean excerpt; index conventions\n"
              "-- as documented in Part II)\n\n" + "\n".join(snippets))

    m = re.search(III_HYP_INTRO_RE, hyp, re.DOTALL)
    assert m, "Hypotheses intro block not found"
    text = hyp[:m.start()] + III_HYP_INTRO_NEW.rstrip() + hyp[m.end():]
    for old, new, count in III_LITERALS:
        found = text.count(old)
        assert found in {count, count and found}, ""
        if count:
            assert found == count, f"literal x{found} (want {count}): {old[:40]!r}"
            text = text.replace(old, new)
        elif found:
            text = text.replace(old, new)
    text = re.sub(r"\n{3,}", "\n\n", text)

    out = basics + "\n" + text.rstrip() + "\n"
    for token in III_BANNED:
        assert token not in out, f"Part III banned token survived: {token!r}"
    for token in ["def HLQuantA", "def CramerGranville", "def singularSeries",
                  "def IsAdmissible", "def nuMod", "def modelMass",
                  "def tupleCount", "def q ", "def gap ", "def delta ",
                  "def SameBlock"]:
        assert token in out, f"Part III required content missing: {token!r}"
    return out


def main(chain_p, counting_p, hyp_p, basic_p, out_p):
    chain = open(chain_p, encoding="ascii").read()
    counting = open(counting_p, encoding="utf-8").read()
    hyp = open(hyp_p, encoding="utf-8").read()
    basic = open(basic_p, encoding="utf-8").read()

    obj = (HEADER
           + "\n---\n\n## PART I -- prose source\n\n" + part_one(chain)
           + "\n---\n\n## PART II -- Lean statement file under assessment\n\n"
           + "```lean\n" + part_two(counting) + "```\n"
           + "\n---\n\n## PART III -- frozen Lean context (not under assessment)\n\n"
           + "```lean\n" + part_three(hyp, basic) + "```\n")

    open(out_p, "w", encoding="utf-8").write(obj)
    print(f"wrote {out_p}: {len(obj.encode('utf-8'))} bytes, "
          f"{obj.count(chr(10))} lines, assertions passed")


if __name__ == "__main__":
    main(*sys.argv[1:6])
