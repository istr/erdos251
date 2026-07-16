#!/usr/bin/env python3
"""Derive the blind-review object from dossier/chain-v1.md (v1.1).

Deterministic, assertion-enforced anchor stripping (ANN-21). Removed:
prior-review verdicts and per-claim review tags (anchor-propagation risk,
Q5 record), v1.1 amendment brackets and version markers (they localize the
former defects), repair/item/process vocabulary, and the provenance
section 9. All mathematical content is preserved byte-for-byte outside the
listed transformations. Re-run at the pinned commit to reproduce the
object; sha256 must match HASHES (operator hash canonical).

Usage: python3 strip_review_copy.py <chain-v1.md> <output.md>
"""
import re
import sys

NEW_HEADER = """# Conditional irrationality of S = sum p_n/2^n

STATUS: conditional theorem. Hypotheses A and B below are open, standard-
shaped conjectures; everything else is claimed proved here or cited as
classical. Erdos problem #251.
"""

LITERALS = [
    # (exact old, new, expected count)
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
    ('"tail differs from an integer" clause -- confirmed by both reviews, P7).',
     '"tail differs from an integer" clause).', 1),
    ("Proof sketch (review-1 A36-A40):", "Proof sketch:", 1),
    ("Mertens' theorems (classical: Mertens 1874; Rosser-Schoenfeld 1962) --\nrepair R3: these are now CITED, not asserted bare; exact-constant\nverification tracked in item-0004. QED-sketch",
     "Mertens' theorems (classical: Mertens 1874; Rosser-Schoenfeld 1962);\nexact-constant verification pending. QED-sketch", 1),
    ("LEMMA 4.2 (one-point extension sum; v1.1).",
     "LEMMA 4.2 (one-point extension sum).", 1),
    ("Proof sketch (review-1 A41-A43):", "Proof sketch:", 1),
    ("LEMMA 4.3 (consecutive lower bound; the transfer; v1.1).",
     "LEMMA 4.3 (consecutive lower bound; the transfer).", 1),
    ("composite for p > x^{1/2} -- review-1 A44).",
     "composite for p > x^{1/2}).", 1),
    ("(L+2 points, +1 -- repair R5: the cardinalities",
     "(L+2 points, +1 -- the cardinalities", 1),
    ("[EXPLICIT one-line lemma per review-2 P2, stated here",
     "[EXPLICIT one-line lemma, stated here", 1),
    ("i_0 = J + 1 (v1.1; interior with slack:",
     "i_0 = J + 1 (interior with slack:", 1),
    ("computation (review-1 A53).", "computation.", 1),
    ("there are only L+1 < p points (review-1 A54).",
     "there are only L+1 < p points.", 1),
    ("## 7. What is NOT claimed (repairs R4, R7)",
     "## 7. What is NOT claimed", 1),
    ("(exponent bookkeeping; review-1 A65).", "(exponent bookkeeping).", 1),
    ("Section 8.2 is an interface sketch; the real\n  formalization is item-0002.",
     "Section 8.2 is an interface sketch; the real\n  formalization is separate work.", 1),
    ("8.1 Kernel ordering (round-1 synthesis). The residual statistical content\nof ALL round-1 architectures is one kernel in ordered formulations:",
     "8.1 Kernel ordering. The residual statistical content\nof the surveyed architectures is one kernel in ordered formulations:", 1),
    ("the model-side entropy clause (Q2 of the gpt-web arm) is orthogonal and\nplausibly provable, but this consolidation does not need it.",
     "a model-side entropy clause (considered elsewhere) is orthogonal and\nplausibly provable, but this document does not need it.", 1),
    ("8.2 Lean interface (repair R6).", "8.2 Lean interface.", 1),
]

BANNED = ["v1.1", "v1.0", "review", "Review", "repair", "Repair",
          "item-00", "ANN-", "steering", "fable", "gpt", "Claude",
          "consolidat", "e5f818", "0.94", "round-1", "round 1"]

REQUIRED = ["i_0 = J + 1", "kappa k ln(k+2)", "kappa L ln(L+2)",
            "kappa = C_1", "There exists x_A", "sequences n_r, m_r",
            "HYPOTHESIS A", "HYPOTHESIS B", "## 8. Remarks",
            "the span hypothesis", "N_cons(w; x) >= (1/4)"]


def main(src_path: str, out_path: str) -> None:
    text = open(src_path, encoding="ascii").read()

    # 1. Header/STATUS block wholesale (title through 'Erdos problem #251.').
    m = re.match(r"\A#[^\n]*\n\nSTATUS:.*?Erdos problem #251\.\n",
                 text, re.DOTALL)
    assert m, "header/STATUS block not found"
    text = NEW_HEADER + text[m.end():]

    # 2. Remove the v1.1 amendment bracket blocks (multiline, non-nested).
    blocks = re.findall(r"\n?\[v1\.1.*?\]\n", text, re.DOTALL)
    assert len(blocks) == 4, f"expected 4 v1.1 blocks, found {len(blocks)}"
    text = re.sub(r"\n?\[v1\.1.*?\]\n", "\n", text, flags=re.DOTALL)

    # 3. Literal table.
    for old, new, count in LITERALS:
        found = text.count(old)
        assert found == count, f"literal x{found} (want {count}): {old[:50]!r}"
        text = text.replace(old, new)

    # 4. Truncate the provenance section.
    idx = text.find("## 9. Provenance")
    assert idx > 0, "section 9 heading not found"
    text = text[:idx].rstrip() + "\n"

    # 5. Whitespace hygiene.
    text = re.sub(r"\n{3,}", "\n\n", text)

    # 6. Assertions.
    for token in BANNED:
        assert token not in text, f"banned token survived: {token!r}"
    for token in REQUIRED:
        assert token in text, f"required content missing: {token!r}"
    text.encode("ascii")  # ASCII-clean or die

    open(out_path, "w", encoding="ascii").write(text)
    print(f"wrote {out_path}: {len(text)} bytes, "
          f"{text.count(chr(10))} lines, assertions passed")


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
