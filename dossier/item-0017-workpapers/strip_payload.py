# item-0017 D6 -- deterministic anchor-strip for blind review payloads.
# Reads dossier/e2prime-supply.md, emits an anchor-stripped review object:
# fixed substitution TABLE (no first-seen state), applied longest-first,
# then line-level drops for the identity preamble. Deterministic by
# construction: same input bytes -> same output bytes.
# Usage: python3 strip_payload.py <in.md> <out.md>
import sys, re

TABLE = [
    # most-specific first (applied sequentially; earlier entries must not
    # be substrings of later needs)
    ("Sessions A-B", "[PHASES-1-2]"), ("Sessions B-C", "[PHASES-2-3]"),
    ("Session A", "[PHASE-1]"), ("Session B", "[PHASE-2]"),
    ("Session C", "[PHASE-3]"), ("Session D", "[PHASE-4]"),
    ("kickoff", "[MANDATE-DOC]"), ("chain-v1", "[CHAIN-DOC-ID]"),
    ("lean/", "[PROOF-TREE]/"), ("Lean", "[PROOF-ASSISTANT]"),
    ("steering", "[STEERING-ROLE]"),
    ("Erdos251", "[PROJECT-NS]"), ("erdos251", "[PROJECT]"),
    ("96dc30c", "[PIN-1]"), ("f812fdc", "[PIN-1A]"),
    ("7ca2388", "[PIN-1B]"), ("66adc54", "[PIN-2]"),
    ("dcc3f63", "[PIN-3]"), ("a7b9f19", "[PIN-4]"),
    ("fb80f44", "[PIN-5]"), ("ANN-50", "[LEDGER-2]"),
    # arXiv ids / papers -> neutral tokens (longest first)
    ("S0002-9939-1988-0958032-5", "[TEXT-J]"),
    ("Maier-Primes-in-short-intervals", "[TEXT-K]"),
    ("1305.6289", "[TEXT-A]"), ("1404.5094", "[TEXT-B]"),
    ("1311.7003", "[TEXT-C]"), ("2210.09775", "[TEXT-D]"),
    ("0409258", "[TEXT-E]"), ("1511.04468", "[TEXT-F]"),
    ("1407.2213", "[TEXT-G]"), ("2009.05000", "[TEXT-H]"),
    ("1004.1084", "[TEXT-I]"), ("1811.03008", "[TEXT-L]"),
    ("1510.08054", "[TEXT-M]"), ("1510.04577", "[TEXT-N]"),
    ("1405.2593", "[TEXT-O]"), ("2512.01739", "[TEXT-P]"),
    # author/name tokens
    ("Banks-Freiberg-Turnage-Butterbaugh", "[AUTH-C]"),
    ("Banks-Freiberg-Maynard", "[AUTH-B]"),
    ("Hildebrand-Maier", "[AUTH-J]"),
    ("Granville-Lumley", "[AUTH-H]"),
    ("Granville-Soundararajan", "[AUTH-Q]"),
    ("Montgomery-Soundararajan", "[AUTH-E]"),
    ("Baker-Freiberg", "[AUTH-M]"),
    ("Ford-Maynard-Tao", "[AUTH-F]"),
    ("Tao-Teravainen", "[AUTH-P]"),
    ("Kuperberg", "[AUTH-D]"), ("Merikoski", "[AUTH-L]"),
    ("Gallagher", "[AUTH-G1]"), ("Maynard-Tao", "[AUTH-MT]"),
    ("Maynard", "[AUTH-O]"), ("Pintz", "[AUTH-A]"),
    ("Maier", "[AUTH-K]"), ("MoSo", "[AUTH-E]"),
    ("Erdos-Rankin", "[SCALE-ER]"), ("Shiu", "[AUTH-S]"),
    ("Selberg", "[SIEVE-1]"), ("Chen", "[SIEVE-2]"),
    ("Cramer-Granville", "[MODEL-CG]"), ("Cramer", "[MODEL-C]"),
    ("Hardy-Littlewood", "[HL]"), ("Chebyshev", "[CLASSIC-1]"),
    ("Mertens", "[CLASSIC-2]"), ("Borel-Cantelli", "[PROB-1]"),
    ("Chernoff", "[PROB-2]"), ("McDiarmid", "[PROB-3]"),
    ("Bernoulli", "[PROB-4]"), ("Markov", "[PROB-5]"),
    ("Cauchy-Schwarz", "[INEQ-1]"),
    ("Hadamard / de la Vallee Poussin 1896", "[CLASSIC-3]"),
    ("Rosser-Schoenfeld", "[CLASSIC-4]"),
    ("Halberstam-Richert", "[BOOK-1]"), ("Greaves", "[BOOK-2]"),
    # project structure
    ("dossier/item-0017-workpapers/extract/", "[EXTRACT]/"),
    ("dossier/item-0017-workpapers/stress/", "[STRESS]/"),
    ("dossier/item-0017-workpapers/", "[WORKPAPERS]/"),
    ("payloads/item-0005-adjudication-v1.md", "[ADJUDICATION]"),
    ("lean/Erdos251/Exchange.lean", "[LEAN-MODULE]"),
    ("dossier/tate-transfer.md", "[VERDICT-DOC]"),
    ("dossier/chain-v1.md", "[CHAIN-DOC]"),
    ("roadmap/item-0017.md", "[ITEM-SELF]"),
    ("roadmap/item-0010.md", "[ITEM-CONSUMER]"),
    ("item-0017", "[ITEM-SELF-ID]"), ("item-0010", "[ITEM-CONSUMER-ID]"),
    ("item-0005", "[ITEM-PRIOR-ID]"),
    ("Erdos #251", "[PROBLEM]"), ("Erdos", "[NAMESAKE]"),
    ("Claude Fable 5", "[EXECUTOR-MODEL]"), ("Fable", "[MODEL-FAM-1]"),
    ("ChatGPT", "[MODEL-FAM-2]"),
    ("tate-transfer", "[VERDICT-DOC-ID]"), ("TaTe", "[AUTH-P]"),
    ("ANN-49", "[LEDGER-1]"), ("ANN-50", "[LEDGER-2]"),
]

DROP_LINE_PATTERNS = [
    re.compile(r"^Date: "), re.compile(r"^Pin: "),
    re.compile(r"(?i)ratif"), re.compile(r"@ [0-9a-f]{7}"),
    re.compile(r"\b[0-9a-f]{7,40}\b.*commit|commit.*\b[0-9a-f]{7,40}\b"),
]

def strip(text):
    out_lines = []
    for ln in text.splitlines():
        if any(p.search(ln) for p in DROP_LINE_PATTERNS):
            out_lines.append("[IDENTITY LINE STRIPPED]")
            continue
        out_lines.append(ln)
    text = "\n".join(out_lines) + "\n"
    for a, b in TABLE:
        text = text.replace(a, b)
    return text

if __name__ == "__main__":
    src, dst = sys.argv[1], sys.argv[2]
    with open(src) as f: t = f.read()
    with open(dst, "w") as f: f.write(strip(t))
    print(f"stripped {src} -> {dst} ({len(t)} -> {len(strip(t))} bytes)")
