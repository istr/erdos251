#!/usr/bin/env python3
"""Integrity checks for the split ledger store (item-0032).

The ledger is one small mutable bets file plus one strictly append-only file
per annotation entry.  Three checks, no third-party dependencies:

* ``relocation-check`` re-verifies the item-0032 split: the entry files the
  pinned revision's annotations body names, concatenated in ascending sequence
  order, must reproduce that body byte for byte.  The rev defaults to the
  pre-split pin, so the check does NOT expire at the split commit -- it
  re-proves on every run that no pre-split entry has been edited, deleted or
  renamed since.  Entries added AFTER the pin are outside its scope by
  construction and are ``append-only``'s business; that division is the item's
  own ("it keeps proving that no historical entry has been edited since, which
  is the same invariant the append-only check enforces for everything added
  later").  Same instrument as ``lean/scripts/blocks.py relocation-check``,
  which the item-0016 split owns.

* ``validate`` checks the store's own shape: filename equals the ``id:`` the
  file carries, ids are unique with contiguous sequence numbers 1..N, every
  entry parses to id / refs / date, and every ref resolves.  Ref integrity is
  by namespace: an internal ref (``ANN-``/``BET-``) must name a live id or sit
  on the grandfathered allowlist below; ``ERRATUM-`` is a legal external
  namespace and is not resolved; anything else fails.

* ``append-only`` is the mechanical enforcement for post-split entries: over
  ``<base>..HEAD`` the annotations directory may show additions only.  The
  guarantee is INCREMENTAL -- it composes into a whole-history guarantee only
  under branch protection that forbids force-push to main and preserves linear
  history.  Correct base resolution in CI (pull_request base sha vs push
  before-sha) is the fragile part and lives in the workflow.

Usage (from the repo root or from scripts/):

    python3 scripts/ledger_check.py relocation-check [--rev REV]
    python3 scripts/ledger_check.py validate
    python3 scripts/ledger_check.py append-only --base REV

Exit code 0 = all checks passed.
"""

from __future__ import annotations

import argparse
import difflib
import hashlib
import pathlib
import re
import subprocess
import sys

# The pre-split pin: the last commit at which ledger.yaml still carried the
# annotations body.  Baked as the default so the relocation check is absolute
# rather than incremental (cf. blocks.py PIN).
PIN = "733f989b5487b3ce39a5d53137bd6f3b6aaf4e92"

HERE = pathlib.Path(__file__).resolve().parent
REPO = HERE.parent
STORE = REPO / "ledger"
ANN = STORE / "annotations"
BETS = STORE / "bets.yaml"
OLD_PATH_IN_REV = "ledger.yaml"

INTERNAL = ("ANN-", "BET-")
EXTERNAL_OK = ("ERRATUM-",)

ENTRY_NAME = re.compile(r"^ANN-\d{8}-\d+\.yaml$")
ID_LINE = re.compile(r"^  - id: (ANN-\d{8}-\d+)\s*$", re.M)
REFS_LINE = re.compile(r"^    refs: \[(.*?)\]", re.M | re.S)
DATE_LINE = re.compile(r"^    date: (\S+)\s*$", re.M)
BET_ID_LINE = re.compile(r"^  - id: (BET-\S+)\s*$", re.M)

# Four historical dangling internal refs, all of the shape "correct sequence
# number, wrong date component".  They sit inside byte-frozen entries and
# cannot be edited, so they are grandfathered rather than repaired.  The key is
# the (citing entry, malformed ref) pair only; the intended id is the analysis
# lane's reading and is advisory, so it is a comment and not data.
#
#   ANN-20260717-49 cites ANN-20260711-07  (reads as ANN-20260712-07)
#   ANN-20260717-47 cites ANN-20260716-14  (reads as ANN-20260712-14)
#   ANN-20260717-48 cites ANN-20260716-47  (reads as ANN-20260717-47)
#   ANN-20260726-74 cites ANN-20260717-27  (reads as ANN-20260716-27)
#
# THIS LIST IS NOT A REPAIR CHANNEL.  A new entry is an operator decision, not
# a convenience: a post-split entry that dangles must be fixed before it lands,
# because it is not yet frozen.
MALFORMED_ALLOW = {
    ("ANN-20260717-49", "ANN-20260711-07"),
    ("ANN-20260717-47", "ANN-20260716-14"),
    ("ANN-20260717-48", "ANN-20260716-47"),
    ("ANN-20260726-74", "ANN-20260717-27"),
}


def seq(entry_id: str) -> int:
    return int(entry_id.rsplit("-", 1)[1])


def sha256(text: str) -> str:
    return hashlib.sha256(text.encode()).hexdigest()


def entry_files() -> list[pathlib.Path]:
    """Entry files in ASCENDING SEQUENCE ORDER -- that order IS the order the
    concatenation gate is stated against, and it is not filesystem lexical
    order (mirrors blocks.py using the umbrella's declared import order)."""
    return sorted(ANN.glob("ANN-*.yaml"), key=lambda p: seq(p.stem))


def parse_entry(path: pathlib.Path) -> tuple[str, list[str] | None, str | None]:
    text = path.read_text()
    m_id = ID_LINE.search(text)
    if not m_id:
        sys.exit(f"{path}: no '  - id: ANN-...' line")
    m_refs = REFS_LINE.search(text)
    refs = None
    if m_refs:
        refs = [t.strip() for t in m_refs.group(1).split(",") if t.strip()]
    m_date = DATE_LINE.search(text)
    return m_id.group(1), refs, (m_date.group(1) if m_date else None)


# ------------------------------------------------------------ relocation


def cmd_relocation_check(rev: str) -> int:
    try:
        old = subprocess.run(
            ["git", "show", f"{rev}:{OLD_PATH_IN_REV}"],
            cwd=REPO, capture_output=True, text=True, check=True,
        ).stdout
    except subprocess.CalledProcessError as exc:
        sys.exit(f"cannot read {OLD_PATH_IN_REV} at {rev}: {exc.stderr.strip()}")

    lines = old.splitlines(keepends=True)
    hdr = [i for i, l in enumerate(lines) if l.rstrip("\n") == "annotations:"]
    if len(hdr) != 1:
        sys.exit(f"{rev}: expected exactly one 'annotations:' line, found {len(hdr)}")
    old_body = "".join(lines[hdr[0] + 1:])

    # The entries the PINNED body carries, in the order it carries them. The
    # scope is read off the pin rather than off the directory: entries added
    # after the pin are not part of this gate (append-only owns them), and
    # taking the directory as the scope would make the gate fail on the very
    # first legitimate append -- including this item's own booking entry.
    pinned_ids = ID_LINE.findall(old_body)
    if not pinned_ids:
        sys.exit(f"{rev}: no annotation entries in the body")
    if pinned_ids != sorted(pinned_ids, key=seq):
        sys.exit(f"{rev}: the pinned body is not in ascending sequence order; "
                 "the declared concatenation order does not describe it")

    missing = [i for i in pinned_ids if not (ANN / f"{i}.yaml").exists()]
    if missing:
        print(f"RELOCATION CHECK FAILED -- {len(missing)} pinned entr(ies) have no file "
              f"under {ANN.relative_to(REPO).as_posix()}:")
        print("\n".join("  " + i for i in missing))
        return 1

    new_body = "".join((ANN / f"{i}.yaml").read_text() for i in pinned_ids)
    later = [p.stem for p in entry_files() if p.stem not in set(pinned_ids)]

    print(f"  {len(pinned_ids)} pinned entries, ascending sequence order")
    print(f"  {len(later)} post-pin entr(ies), out of scope here, covered by append-only")
    print(f"  old body @ {rev[:7]}  {len(old_body.splitlines()):5d} lines  sha256 {sha256(old_body)}")
    print(f"  concatenation       {len(new_body.splitlines()):5d} lines  sha256 {sha256(new_body)}")

    if new_body != old_body:
        diff = list(difflib.unified_diff(
            old_body.split("\n"), new_body.split("\n"),
            fromfile=f"ledger.yaml@{rev} (annotations body)", tofile="concatenation",
            lineterm="",
        ))
        print("\nRELOCATION CHECK FAILED -- the store is not a pure relocation:\n")
        print("\n".join(diff[:200]))
        return 1
    print("\nRELOCATION CHECK PASSED -- concatenation is byte-identical to the old body.")
    return 0


# -------------------------------------------------------------- validate


def cmd_validate() -> int:
    ok = True

    stray = sorted(p.name for p in ANN.iterdir()
                   if p.is_file() and not ENTRY_NAME.match(p.name))
    for name in stray:
        print(f"  FAIL stray file under annotations/: {name}")
        ok = False

    files = entry_files()
    if not files:
        sys.exit(f"no entry files under {ANN}")

    ids: list[tuple[str, list[str] | None]] = []
    seen: set[str] = set()
    for path in files:
        entry_id, refs, date = parse_entry(path)
        if path.stem != entry_id:
            print(f"  FAIL filename/id mismatch: {path.name} holds {entry_id}")
            ok = False
        if entry_id in seen:
            print(f"  FAIL duplicate id: {entry_id}")
            ok = False
        if refs is None:
            print(f"  FAIL no refs list: {entry_id}")
            ok = False
        if date is None:
            print(f"  FAIL no date: {entry_id}")
            ok = False
        seen.add(entry_id)
        ids.append((entry_id, refs or []))

    nums = sorted(seq(e) for e, _ in ids)
    if nums != list(range(1, len(nums) + 1)):
        missing = sorted(set(range(1, nums[-1] + 1)) - set(nums))
        print(f"  FAIL sequence numbers not contiguous 1..{len(nums)}; missing {missing}")
        ok = False

    bet_ids = set(BET_ID_LINE.findall(BETS.read_text()))
    if not bet_ids:
        print(f"  FAIL no bet ids parsed from {BETS}")
        ok = False
    live = seen | bet_ids

    grandfathered = 0
    for entry_id, refs in ids:
        for ref in refs:
            if ref.startswith(INTERNAL):
                if ref in live:
                    continue
                if (entry_id, ref) in MALFORMED_ALLOW:
                    grandfathered += 1
                    continue
                print(f"  FAIL dangling internal ref {ref} in {entry_id}")
                ok = False
            elif not ref.startswith(EXTERNAL_OK):
                print(f"  FAIL unknown ref namespace {ref} in {entry_id}")
                ok = False

    print(f"  {len(files)} entries, sequence numbers up to {nums[-1] if nums else 0}, "
          f"{len(bet_ids)} bets")
    print(f"  {grandfathered} grandfathered malformed refs (allowlist size {len(MALFORMED_ALLOW)})")
    print("VALIDATE: " + ("passed." if ok else "FAILURES -- do not repair a frozen entry, report."))
    return 0 if ok else 1


# ----------------------------------------------------------- append-only


def cmd_append_only(base: str) -> int:
    rel = ANN.relative_to(REPO).as_posix()
    try:
        out = subprocess.run(
            ["git", "diff", "--name-status", f"{base}..HEAD", "--", rel],
            cwd=REPO, capture_output=True, text=True, check=True,
        ).stdout
    except subprocess.CalledProcessError as exc:
        sys.exit(f"cannot diff {base}..HEAD: {exc.stderr.strip()}")

    changes = [l for l in out.splitlines() if l.strip()]
    bad = [l for l in changes if l[0] in "MDR"]
    if bad:
        print(f"APPEND-ONLY VIOLATION under {rel} over {base}..HEAD:")
        print("\n".join("  " + l for l in bad))
        print("A landed annotation file is never modified, deleted or renamed;")
        print("an amendment is a successor entry, never an edit.")
        return 1
    print(f"APPEND-ONLY: {len(changes)} change(s) under {rel} over {base}..HEAD, additions only.")
    return 0


def main() -> int:
    ap = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    rc = sub.add_parser("relocation-check",
                        help="concatenation reproduces the pre-split annotations body")
    rc.add_argument("--rev", default=PIN,
                    help=f"git rev holding the pre-split ledger.yaml (default {PIN[:7]})")
    sub.add_parser("validate", help="ids, sequence contiguity, filenames, ref integrity")
    ao = sub.add_parser("append-only", help="annotations/ shows additions only over base..HEAD")
    ao.add_argument("--base", required=True, help="the base rev to compare HEAD against")
    args = ap.parse_args()

    if args.cmd == "relocation-check":
        return cmd_relocation_check(args.rev)
    if args.cmd == "validate":
        return cmd_validate()
    return cmd_append_only(args.base)


if __name__ == "__main__":
    sys.exit(main())
