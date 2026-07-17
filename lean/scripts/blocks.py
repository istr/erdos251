#!/usr/bin/env python3
"""Block-level integrity checks for the erdos251 Lean tree (item-0016).

Two jobs, both path-independent by design:

* ``relocation-check`` re-verifies the item-0016 split: the bodies of the
  ``Erdos251/Counting/*.lean`` modules, concatenated in the umbrella's
  import order, must reproduce the body of ``Erdos251/Counting.lean`` as it
  stood at a given git rev, byte for byte.  A module "body" is everything
  between the uniform wrapper (``namespace Erdos251`` / ``noncomputable
  section`` ... ``end`` / ``end Erdos251``); the wrapper and the module
  header are the only text the split is allowed to add.

* ``extract`` / ``check-frozen`` address a frozen block by DECLARATION NAME
  rather than by file path and line number, so that a relocation cannot
  silently invalidate the check (the failure mode item-0016 exists to
  remove).  A block is the doc comment plus the declaration; ``open ... in``
  and ``set_option ... in`` lines are NOT part of it (ANN-26 convention:
  they precede the docstring, so the frozen block stays untouched).

Usage (from the repo root or from lean/):

    python3 lean/scripts/blocks.py relocation-check [--rev REV]
    python3 lean/scripts/blocks.py extract DECL_NAME
    python3 lean/scripts/blocks.py check-frozen

Exit code 0 = all checks passed.  No third-party dependencies.
"""

from __future__ import annotations

import argparse
import hashlib
import pathlib
import re
import subprocess
import sys

PIN = "6683ee0f009baeb5dd6e759f265544e7f91af23d"

HERE = pathlib.Path(__file__).resolve().parent
LEAN = HERE.parent
REPO = LEAN.parent
UMBRELLA = LEAN / "Erdos251" / "Counting.lean"
FROZEN_MANIFEST = LEAN / "frozen-blocks.yaml"

# The ONE prose exception the operator ratified alongside the item-0016
# split (ANN-46 residual: q_eq_of_count's docstring was already stale in its
# "only", and the split breaks its "below" as well).  It is applied to the
# pre-split body BEFORE the comparison, so the relocation gate stays exact
# rather than approximate: everything not listed here must match byte for
# byte.  This list is not a repair channel -- a new entry is an operator
# decision, not a convenience.
DECLARED_AMENDMENTS = [
    (
        "/-- Bridge from `Nat.count` (computable) to `Nat.nth` (not), used only by\n"
        "the smoke tests below. Flagged as glue in the traceability table. -/",
        "/-- Bridge from `Nat.count` (computable) to `Nat.nth` (not), used by\n"
        "`consCount_bonferroni` and by the section-5 smoke tests in\n"
        "`Counting/Construction.lean`. Flagged as glue in the traceability table. -/",
    ),
]

TOP_LEVEL = re.compile(
    r"^(/--|/-!|@\[|private\s|def\s|theorem\s|lemma\s|abbrev\s|example\s"
    r"|instance\s|structure\s|inductive\s|open\s|set_option\s|section\s"
    r"|namespace\s|end\b)"
)


def sha256(text: str) -> str:
    return hashlib.sha256(text.encode()).hexdigest()


# ---------------------------------------------------------------- wrappers


def strip_wrapper(text: str, where: str) -> str:
    """Return the body of a module, i.e. everything strictly inside the
    uniform ``namespace Erdos251`` / ``noncomputable section`` wrapper.

    The rule is positional and deterministic: the body starts two lines
    after the sole ``noncomputable section`` line (skipping one blank) and
    ends one line before the trailing ``end`` that precedes the final
    ``end Erdos251`` (again skipping one blank).  Any deviation from the
    wrapper shape is an error, not a guess.
    """
    lines = text.split("\n")
    opens = [i for i, l in enumerate(lines) if l == "noncomputable section"]
    if len(opens) != 1:
        sys.exit(f"{where}: expected exactly one 'noncomputable section' line, found {len(opens)}")
    start = opens[0] + 1
    if lines[start] != "":
        sys.exit(f"{where}: expected a blank line after 'noncomputable section'")
    start += 1

    closes = [i for i, l in enumerate(lines) if l == "end Erdos251"]
    if not closes:
        sys.exit(f"{where}: no 'end Erdos251' line")
    j = closes[-1] - 1
    if lines[j] != "":
        sys.exit(f"{where}: expected a blank line before 'end Erdos251'")
    j -= 1
    if lines[j] != "end":
        sys.exit(f"{where}: expected 'end' (closing the noncomputable section) before 'end Erdos251'")
    return "\n".join(lines[start:j]) + "\n"


def umbrella_modules() -> list[str]:
    """The Counting submodules, in the umbrella's import order -- that order
    IS the declared order the concatenation gate is stated against."""
    mods = []
    for line in UMBRELLA.read_text().split("\n"):
        m = re.match(r"^import Erdos251\.Counting\.([A-Za-z0-9_.]+)$", line)
        if m:
            mods.append(m.group(1))
    if not mods:
        sys.exit("umbrella imports no Erdos251.Counting.* modules")
    return mods


def cmd_relocation_check(rev: str) -> int:
    try:
        old = subprocess.run(
            ["git", "show", f"{rev}:lean/Erdos251/Counting.lean"],
            cwd=REPO, capture_output=True, text=True, check=True,
        ).stdout
    except subprocess.CalledProcessError as exc:
        sys.exit(f"cannot read Counting.lean at {rev}: {exc.stderr.strip()}")

    old_body = strip_wrapper(old, f"Counting.lean@{rev}")
    for i, (before, after) in enumerate(DECLARED_AMENDMENTS, start=1):
        if old_body.count(before) != 1:
            sys.exit(f"declared amendment {i} does not match the body at {rev} exactly once")
        old_body = old_body.replace(before, after)
    if DECLARED_AMENDMENTS:
        print(f"  ({len(DECLARED_AMENDMENTS)} declared amendment(s) applied to the old body)\n")

    parts, ok = [], True
    for mod in umbrella_modules():
        path = LEAN / "Erdos251" / "Counting" / (mod.replace(".", "/") + ".lean")
        if not path.exists():
            sys.exit(f"missing module file: {path}")
        body = strip_wrapper(path.read_text(), str(path))
        parts.append(body)
        print(f"  {mod:16s} {len(body.splitlines()):5d} lines  sha256 {sha256(body)}")

    new_body = "".join(parts)
    print(f"\n  old body @ {rev[:7]}   {len(old_body.splitlines()):5d} lines  sha256 {sha256(old_body)}")
    print(f"  concatenation       {len(new_body.splitlines()):5d} lines  sha256 {sha256(new_body)}")

    if new_body != old_body:
        ok = False
        import difflib
        diff = list(difflib.unified_diff(
            old_body.split("\n"), new_body.split("\n"),
            fromfile=f"Counting.lean@{rev} (body)", tofile="concatenation", lineterm="",
        ))
        print("\nRELOCATION CHECK FAILED -- the split is not pure:\n")
        print("\n".join(diff[:200]))
    else:
        print("\nRELOCATION CHECK PASSED -- concatenation is byte-identical to the old body.")
    return 0 if ok else 1


# ------------------------------------------------------------------ blocks


def lean_files() -> list[pathlib.Path]:
    return sorted(p for p in (LEAN / "Erdos251").rglob("*.lean"))


def extract_block(name: str) -> tuple[pathlib.Path, int, str]:
    """Find the unique declaration ``name`` in the tree and return its block:
    the doc comment (if any) plus the declaration, addressed by ANCHOR."""
    decl = re.compile(rf"^(?:private\s+)?(?:def|theorem|lemma|abbrev)\s+{re.escape(name)}\b")
    hits = []
    for path in lean_files():
        lines = path.read_text().split("\n")
        for i, line in enumerate(lines):
            if decl.match(line):
                hits.append((path, i, lines))
    if not hits:
        sys.exit(f"declaration not found: {name}")
    if len(hits) > 1:
        sys.exit(f"declaration not unique: {name} in {[str(h[0]) for h in hits]}")

    path, i, lines = hits[0]

    # walk back over the doc comment only (NOT over 'open ... in' /
    # 'set_option ... in', which sit outside the frozen block by ANN-26)
    start = i
    if start > 0 and lines[start - 1].rstrip().endswith("-/"):
        j = start - 1
        while j >= 0 and not lines[j].lstrip().startswith("/--"):
            j -= 1
        if j >= 0:
            start = j

    # walk forward to the next top-level item
    end = i + 1
    while end < len(lines):
        if TOP_LEVEL.match(lines[end]):
            break
        end += 1
    while end > i and lines[end - 1].strip() == "":
        end -= 1

    return path, start + 1, "\n".join(lines[start:end]) + "\n"


def read_manifest() -> list[tuple[str, str]]:
    """Deliberately trivial 'name: sha256' reader -- no yaml dependency."""
    out = []
    for raw in FROZEN_MANIFEST.read_text().split("\n"):
        line = raw.split("#", 1)[0].strip()
        if not line:
            continue
        m = re.match(r"^([A-Za-z0-9_'.]+)\s*:\s*([0-9a-f]{64})$", line)
        if not m:
            sys.exit(f"malformed manifest line: {raw!r}")
        out.append((m.group(1), m.group(2)))
    return out


def cmd_extract(name: str) -> int:
    path, line, block = extract_block(name)
    print(f"-- {path.relative_to(REPO)}:{line}  sha256 {sha256(block)}\n")
    print(block, end="")
    return 0


def cmd_check_frozen() -> int:
    ok = True
    for name, want in read_manifest():
        path, line, block = extract_block(name)
        got = sha256(block)
        status = "OK  " if got == want else "DRIFT"
        if got != want:
            ok = False
        print(f"  {status} {name:34s} {path.relative_to(REPO)}:{line}")
        if got != want:
            print(f"        expected {want}\n        found    {got}")
    print("\nFROZEN BLOCKS: " + ("all byte-identical." if ok else "DRIFT DETECTED -- do not repair silently, report."))
    return 0 if ok else 1


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    rc = sub.add_parser("relocation-check", help="item-0016: concatenation reproduces the old body")
    rc.add_argument("--rev", default=PIN, help=f"git rev holding the pre-split Counting.lean (default {PIN[:7]})")
    ex = sub.add_parser("extract", help="print a block addressed by declaration name, with its sha256")
    ex.add_argument("name")
    sub.add_parser("check-frozen", help="check every block in lean/frozen-blocks.yaml")
    args = ap.parse_args()

    if args.cmd == "relocation-check":
        return cmd_relocation_check(args.rev)
    if args.cmd == "extract":
        return cmd_extract(args.name)
    return cmd_check_frozen()


if __name__ == "__main__":
    sys.exit(main())
