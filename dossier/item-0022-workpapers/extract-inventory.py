#!/usr/bin/env python3
"""item-0022 extract inventory -- mechanical count of report-indexed structure.

Lane B of the item-0033 Phase 2a apply. Deterministic, dependency-free
(standard library only), and reproducible: running this script twice over an
unchanged extract set produces a byte-identical output file.

WHAT THIS IS. A count, per extract, along five axes, of the ways the extract's
selection and section structure are indexed to the three reports that were
dropped as objects on 2026-07-27, or sourced to the ephemeral item-0022 kickoff
dispatch. It exists to size the Phase 2b grading pass.

WHAT THIS IS NOT. It opens no PDF. It asserts no fidelity, issues no verdict on
any extract or claim row, recommends no disposition, and books no hash. Those
require the primary sources and belong to Phase 2b.

DISCIPLINE. Naming a report-indexed heading is naming a defect, not restating a
claim. Heading matches are quoted whole because the heading text IS the finding;
every other match quotes only the matched phrase, never the sentence around it,
so that no content of a dropped report enters this artifact. Emitted text is
ASCII-folded (non-ASCII characters are rendered as <U+XXXX>) because every file
this apply writes is ASCII-only.

Usage:
  python3 dossier/item-0022-workpapers/extract-inventory.py
"""

from __future__ import annotations

import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
EXTRACT_DIR = os.path.join(HERE, "extract")
OUT_PATH = os.path.join(HERE, "extract-inventory-r1.md")

MAX_QUOTE = 200

# ---------------------------------------------------------------------------
# Axis patterns. Disclosed here and reprinted in the output, so the counts are
# auditable without reading this file.
# ---------------------------------------------------------------------------

RE_HEADING = re.compile(r"^#{1,6}\s")
RE_REPORT_N = re.compile(r"report\s+[123]\b", re.IGNORECASE)
RE_REPORT_SET = re.compile(r"cited by item-0022's reports", re.IGNORECASE)

# I1, class A: in-body annotations that frame extracted content as a dropped
# report's claim. Narrow and explicit by design; a wider net would sweep in bare
# mentions, which are axis I3.
I1_ANNOTATION = [
    r"confirms? report\s+[123]",
    r"matches report\s+[123]",
    r"matching report\s+[123]",
    r"report\s+[123]'s claim",
    r"report\s+[123]'s own characterization",
    r"report\s+[123]'s characterization",
]

# I2: assertions sourced to the item-0022 kickoff dispatch, which no longer
# exists in any form, or to another object outside the tree. Longest match at a
# given position wins, so the specific pattern beats the generic one.
I2_PATTERNS = [
    (r"item-0022 kickoff dispatch", "item-0022 kickoff dispatch"),
    (r"item-0022-kickoff-v1\.md", "item-0022 kickoff dispatch"),
    (r"kickoff dispatch", "kickoff dispatch"),
    (r"against the dispatch", "the dispatch (kickoff)"),
    (r"Pintz_Lemma2_Image_Analysis_Report\.pdf", "operator-held PDF"),
    (r"Pintz_Lemmas_1_and_2_Report\.pdf", "operator-held PDF"),
    (r"operator supplied two documents", "operator-held material"),
    (r"operator[- ]supplied", "operator-held material"),
    (r"operator[- ]commissioned", "operator-held material"),
]

# I4: in-tree cross-references. These survive the drop and are not defects.
I4_PATTERNS = [
    (r"/home/istr/pro/erdos251/dossier/[A-Za-z0-9._/-]+", "anchor-source-path"),
    (r"(?:dossier|roadmap|payloads|lean|runs|writeup|scripts)/[A-Za-z0-9._/-]+",
     "tree-path"),
    (r"\b(?:AGENTS|HANDOVER)\.md\b", "named-artifact"),
    (r"\bledger\.yaml\b", "named-artifact"),
    (r"\bitem-0022\.md\b", "named-artifact"),
    (r"\bkowalski-mu-recheck\.(?:py|txt)\b", "named-artifact"),
    (r"\b(?:R1|R2)-\d{3}\b", "checklist-row"),
    (r"\bC3-\d{3}\b", "checklist-row"),
]

AXIS_DOC = [
    ("I1", "headings or annotations framing content as a dropped report's claim"),
    ("I2", "assertions sourced to the item-0022 kickoff dispatch or another "
           "ephemeral object"),
    ("I3", "occurrences of report 1 / report 2 / report 3 outside I1 and I2"),
    ("I4", "in-tree cross-references, which survive and are not defects"),
    ("I5", "total lines, and lines inside display or code fences"),
]

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------


def ascii_fold(s: str) -> str:
    """Render a source fragment as ASCII-only, printable, single-line text."""
    out = []
    for ch in s:
        if ch == "\t":
            out.append(" ")
        elif ch in ("\n", "\r"):
            out.append(" ")
        elif " " <= ch <= "~":
            out.append(ch)
        else:
            out.append("<U+%04X>" % ord(ch))
    folded = "".join(out)
    folded = folded.replace("```", "'''")      # never break an output fence
    if len(folded) > MAX_QUOTE:
        folded = folded[:MAX_QUOTE] + " [...]"
    return folded.rstrip()


def keep_disjoint(spans):
    """Greedy longest-first, left-to-right selection of non-overlapping spans.

    spans: list of (start, end, kind, text). Deterministic: ties break on the
    order the pattern list declares, which is captured in the sort key.
    """
    ordered = sorted(spans, key=lambda s: (s[0], -(s[1] - s[0]), s[4]))
    chosen = []
    last_end = -1
    for start, end, kind, text, _rank in ordered:
        if start < last_end:
            continue
        chosen.append((start, end, kind, text))
        last_end = end
    return chosen


def find_all(line, patterns, ignore_case=True):
    """All (start, end, kind, text, rank) matches of a (regex, kind) list.

    I4 runs case-sensitively: in-tree paths and artifact names are case-exact,
    and case-folding them matches prose such as a Lean/informal contrast inside
    a verbatim quotation from an anchored paper, which is not a tree path.
    """
    flags = re.IGNORECASE if ignore_case else 0
    hits = []
    for rank, (pat, kind) in enumerate(patterns):
        for m in re.finditer(pat, line, flags):
            hits.append((m.start(), m.end(), kind, m.group(0), rank))
    return hits


def fence_map(lines):
    """Per-line flag: is the line inside a display or code fence?

    Code fences are ``` or ~~~ delimited, inclusive of the fence lines. Display
    blocks are $$-delimited; a line is a display line if a display block is open
    when the line starts, or if the line contains a $$ token at all (which
    covers the single-line display case).
    """
    flags = []
    in_code = False
    in_display = False
    for line in lines:
        stripped = line.lstrip()
        if stripped.startswith("```") or stripped.startswith("~~~"):
            in_code = not in_code
            flags.append(True)
            continue
        if in_code:
            flags.append(True)
            continue
        n = line.count("$$")
        flags.append(in_display or n > 0)
        if n % 2 == 1:
            in_display = not in_display
    return flags


# ---------------------------------------------------------------------------
# Per-extract scan
# ---------------------------------------------------------------------------


def scan(path):
    name = os.path.basename(path)
    text = open(path, encoding="utf-8").read()
    lines = text.split("\n")
    if lines and lines[-1] == "":
        lines = lines[:-1]

    rows = {"I1": [], "I2": [], "I3": [], "I4": []}
    blocked = {}          # line index -> list of (start, end) claimed by I1/I2

    for i, line in enumerate(lines, start=1):
        claimed = []

        # --- I1 -------------------------------------------------------------
        if RE_HEADING.match(line):
            if RE_REPORT_N.search(line):
                rows["I1"].append((i, "report-named-heading", ascii_fold(line)))
                claimed.append((0, len(line)))
            elif RE_REPORT_SET.search(line):
                rows["I1"].append((i, "report-set-heading", ascii_fold(line)))
                claimed.append((0, len(line)))
        else:
            ann = keep_disjoint(find_all(
                line, [(p, "framing-annotation") for p in I1_ANNOTATION]))
            for start, end, kind, txt in ann:
                rows["I1"].append((i, kind, ascii_fold(txt)))
                claimed.append((start, end))

        # --- I2 -------------------------------------------------------------
        for start, end, kind, txt in keep_disjoint(find_all(line, I2_PATTERNS)):
            if any(start < ce and cs < end for cs, ce in claimed):
                continue
            rows["I2"].append((i, kind, ascii_fold(txt)))
            claimed.append((start, end))

        blocked[i] = claimed

        # --- I3 -------------------------------------------------------------
        for m in RE_REPORT_N.finditer(line):
            if any(m.start() < ce and cs < m.end() for cs, ce in claimed):
                continue
            rows["I3"].append((i, "bare-mention", ascii_fold(m.group(0))))

        # --- I4 -------------------------------------------------------------
        for start, end, kind, txt in keep_disjoint(
                find_all(line, I4_PATTERNS, ignore_case=False)):
            rows["I4"].append((i, kind, ascii_fold(txt)))

    flags = fence_map(lines)
    total_lines = len(lines)
    fenced_lines = sum(1 for f in flags if f)

    # Header facts, read from the extract only. No PDF is opened.
    m_pages = re.search(r"\b(\d+)\s+pages\.", text)
    pages = int(m_pages.group(1)) if m_pages else 0
    m_src = re.search(r"^Source \(only evidence base\):\s*(\S+)", text, re.M)
    source = m_src.group(1) if m_src else "(not declared)"
    has_sha = bool(re.search(r"^sha256 [0-9a-f]{64}$", text, re.M))
    m_bound = re.search(r"read to PDF page (\d+) of (\d+)", text)
    bounded = (int(m_bound.group(1)), int(m_bound.group(2))) if m_bound else None

    return {
        "name": name,
        "source": source,
        "has_sha": has_sha,
        "pages": pages,
        "bounded": bounded,
        "rows": rows,
        "total_lines": total_lines,
        "fenced_lines": fenced_lines,
    }


# ---------------------------------------------------------------------------
# Report
# ---------------------------------------------------------------------------


def render(results):
    o = []
    w = o.append

    w("# item-0022 extract inventory r1 -- mechanical, no fidelity claim")
    w("")
    w("Generated by `dossier/item-0022-workpapers/extract-inventory.py` "
      "(Lane B of the")
    w("item-0033 Phase 2a apply). Deterministic and dependency-free; two runs "
      "over an")
    w("unchanged extract set produce a byte-identical file.")
    w("")
    w("**This is an inventory. It carries no verdict, no fidelity claim and no")
    w("disposition recommendation.** No PDF was opened. No hash is booked. No "
      "extract")
    w("is edited. Grading the extracts against their primary sources is Phase "
      "2b, and")
    w("the counts below exist to say how large that pass is.")
    w("")
    w("**Why the extracts need a grade at all.** Their content is transcribed "
      "from")
    w("anchored primary sources, but their selection and section structure are")
    w("indexed to three reports that were dropped as objects on 2026-07-27, and "
      "some")
    w("assertions are sourced to the item-0022 kickoff dispatch, an ephemeral "
      "object")
    w("that no longer exists in any form. Neither clean nor worthless; "
      "ungraded.")
    w("")
    w("**Quotation discipline.** Naming a report-indexed heading names a "
      "defect; it")
    w("does not restate a claim. Heading matches are quoted whole, because the")
    w("heading text is itself the finding. Every other match quotes the matched")
    w("phrase only, never the sentence around it. No content of any dropped "
      "report")
    w("appears here. Quoted text is ASCII-folded; a non-ASCII character is "
      "rendered")
    w("as its code point.")
    w("")
    w("---")
    w("")
    w("## Axes")
    w("")
    w("| axis | what is counted |")
    w("| --- | --- |")
    for axis, doc in AXIS_DOC:
        w("| %s | %s |" % (axis, doc))
    w("")
    w("Axis membership is disjoint by construction: a span claimed by I1 or I2 "
      "is")
    w("excluded from I3. I4 is counted independently of the other three, since "
      "an")
    w("in-tree path may legitimately appear inside a report-indexed heading.")
    w("")
    w("**What I2 mechanically counts, stated precisely.** Every reference to an")
    w("ephemeral object, in either direction. Most are an assertion resting on "
      "the")
    w("kickoff dispatch. Some are the opposite -- a disclaimer that an "
      "operator-held")
    w("document was NOT used as evidence. Both are counted, and neither is "
      "graded")
    w("here: a disclaimer is still a place where the extract's provenance chain")
    w("passes through an object no session can open, which is what Phase 2b has "
      "to")
    w("decide about. The per-extract listings below show which kind each match "
      "is.")
    w("")
    w("Patterns, verbatim, so the counts can be audited without reading the "
      "script:")
    w("")
    w("```")
    w("I1  heading   ^#{1,6}\\s  AND  (report\\s+[123]\\b  OR")
    w("                              cited by item-0022's reports)")
    w("I1  annotation (non-heading lines, case-insensitive):")
    for p in I1_ANNOTATION:
        w("      %s" % p)
    w("I2  (case-insensitive, longest match at a position wins):")
    for p, kind in I2_PATTERNS:
        w("      %-44s -> %s" % (p, kind))
    w("I3  report\\s+[123]\\b   outside every I1 and I2 span")
    w("I4  (CASE-SENSITIVE, longest match at a position wins):")
    for p, kind in I4_PATTERNS:
        w("      %-44s -> %s" % (p, kind))
    w("I5  total lines; a line is fenced if it sits in a ``` / ~~~ block or in")
    w("      a $$-delimited display, inclusive of the delimiter lines")
    w("```")
    w("")
    w("---")
    w("")
    w("## Per-extract inventory")
    w("")

    for r in results:
        w("### %s" % r["name"])
        w("")
        w("| field | value |")
        w("| --- | --- |")
        w("| source, as declared in the extract header | `%s` |" % r["source"])
        w("| header declares a sha256 for that source | %s |"
          % ("yes" if r["has_sha"] else "NO"))
        w("| PDF pages, as declared in the extract header | %d |" % r["pages"])
        if r["bounded"]:
            w("| extract declares a bounded read | pages 1-%d of %d |"
              % (r["bounded"][0], r["bounded"][1]))
        else:
            w("| extract declares a bounded read | no |")
        w("")
        w("| axis | count |")
        w("| --- | --- |")
        for axis in ("I1", "I2", "I3", "I4"):
            w("| %s | %d |" % (axis, len(r["rows"][axis])))
        w("| I5 total lines | %d |" % r["total_lines"])
        w("| I5 fenced or display lines | %d |" % r["fenced_lines"])
        w("")
        any_rows = any(r["rows"][a] for a in ("I1", "I2", "I3", "I4"))
        if not any_rows:
            w("No I1, I2, I3 or I4 match.")
            w("")
            continue
        w("```")
        for axis in ("I1", "I2", "I3", "I4"):
            for lineno, kind, txt in r["rows"][axis]:
                w("%-3s %-22s L%-5d %s" % (axis, kind, lineno, txt))
        w("```")
        w("")

    # --- totals -----------------------------------------------------------
    w("---")
    w("")
    w("## Totals")
    w("")
    w("| extract | I1 | I2 | I3 | I4 | lines | fenced |")
    w("| --- | --- | --- | --- | --- | --- | --- |")
    tot = {"I1": 0, "I2": 0, "I3": 0, "I4": 0, "lines": 0, "fenced": 0,
           "pages": 0}
    for r in results:
        w("| %s | %d | %d | %d | %d | %d | %d |"
          % (r["name"], len(r["rows"]["I1"]), len(r["rows"]["I2"]),
             len(r["rows"]["I3"]), len(r["rows"]["I4"]),
             r["total_lines"], r["fenced_lines"]))
        for a in ("I1", "I2", "I3", "I4"):
            tot[a] += len(r["rows"][a])
        tot["lines"] += r["total_lines"]
        tot["fenced"] += r["fenced_lines"]
        tot["pages"] += r["pages"]
    w("| **total** | **%d** | **%d** | **%d** | **%d** | **%d** | **%d** |"
      % (tot["I1"], tot["I2"], tot["I3"], tot["I4"], tot["lines"],
         tot["fenced"]))
    w("")

    n_i1 = sum(1 for r in results if r["rows"]["I1"])
    n_i2 = sum(1 for r in results if r["rows"]["I2"])
    n_i3 = sum(1 for r in results if r["rows"]["I3"])
    n_clean = sum(1 for r in results
                  if not r["rows"]["I1"] and not r["rows"]["I2"]
                  and not r["rows"]["I3"])
    w("Extracts carrying at least one I1 match: %d of %d." % (n_i1, len(results)))
    w("Extracts carrying at least one I2 match: %d of %d." % (n_i2, len(results)))
    w("Extracts carrying at least one I3 match: %d of %d." % (n_i3, len(results)))
    w("Extracts carrying none of I1, I2, I3: %d of %d." % (n_clean, len(results)))
    w("")

    # --- what 2b has to read ---------------------------------------------
    w("---")
    w("")
    w("## What Phase 2b will have to read")
    w("")
    w("Plain counts, no recommendation.")
    w("")
    w("| line | count |")
    w("| --- | --- |")
    w("| extracts to grade | %d |" % len(results))
    w("| extract lines to read | %d |" % tot["lines"])
    w("| of those, lines inside a display or code fence | %d |" % tot["fenced"])
    w("| distinct primary PDFs to open | %d |" % len(results))
    w("| PDF pages, summed as declared in the extract headers | %d |"
      % tot["pages"])
    w("| report-indexed headings and annotations to re-decide (I1) | %d |"
      % tot["I1"])
    w("| references to an ephemeral object to re-decide (I2) | %d |"
      % tot["I2"])
    w("| further report mentions to re-read in context (I3) | %d |" % tot["I3"])
    w("| in-tree cross-references that need no work (I4) | %d |" % tot["I4"])
    w("")
    bounded = [r for r in results if r["bounded"]]
    if bounded:
        w("Two page counts are upper bounds on what 2b must open, not lower "
          "ones:")
        w("the following extracts declare a bounded read of their own source, "
          "so a")
        w("grading pass that only re-checks what was transcribed reads fewer "
          "pages.")
        w("")
        w("| extract | declared read | source pages |")
        w("| --- | --- | --- |")
        for r in bounded:
            w("| %s | pages 1-%d | %d |"
              % (r["name"], r["bounded"][0], r["bounded"][1]))
        w("")
        covered = sum(r["bounded"][0] for r in bounded)
        unbounded = sum(r["pages"] for r in results if not r["bounded"])
        w("Summed that way the floor is %d pages (%d declared-read pages plus "
          "%d"
          % (covered + unbounded, covered, unbounded))
        w("pages across the %d extracts that declare no bound) against a "
          "ceiling of %d."
          % (len(results) - len(bounded), tot["pages"]))
        w("")
    w("The two precedent extracts are listed here on the same footing as the")
    w("other five. Whether they stay in the corpus at all is an open question")
    w("recorded in HANDOVER.md and routed to item-0033; this inventory does not")
    w("answer it.")
    return "\n".join(o) + "\n"


def main(argv):
    if not os.path.isdir(EXTRACT_DIR):
        sys.stderr.write("no extract directory at %s\n" % EXTRACT_DIR)
        return 1
    names = sorted(n for n in os.listdir(EXTRACT_DIR) if n.endswith(".md"))
    if not names:
        sys.stderr.write("no extracts found in %s\n" % EXTRACT_DIR)
        return 1
    results = [scan(os.path.join(EXTRACT_DIR, n)) for n in names]
    out = render(results)
    with open(OUT_PATH, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(out)
    sys.stdout.write("wrote %s (%d extracts, %d lines)\n"
                     % (os.path.relpath(OUT_PATH, os.getcwd()), len(results),
                        len(out.split("\n")) - 1))
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
