#!/usr/bin/env python3
"""Enforce the inline-math delimiter rule of AGENTS.md on Markdown files.

The rule: an inline formula opens with dollar-then-backtick and closes with
backtick-then-dollar. The failure this lint exists for is the delimiter
carrying an extra outer backtick on each side, which renders as two inline
code spans containing a dollar sign with unrendered text between them.

That failure has a known cause. AGENTS.md has to display a delimiter that
contains a backtick, and Markdown's only escape for a backtick is a longer
run of backticks. Stripping one backtick per side instead of two yields the
corrupted form, and the corrupted form looks plausible because it is still
symmetric. The lint removes the need to get that right by hand.

Checks, in order:

  E1  corrupted delimiter: backtick-dollar-backtick outside a code block.
  E2  unbalanced delimiters: opener count differs from closer count.
  E3  bare dollar-delimited inline math: dollar, non-space, ..., dollar,
      where neither end is part of a display block or a correct delimiter.

Code spans and fenced code blocks are exempt: they exist to show literal
text, including this very notation.

Exit status 0 if clean, 1 if any file fails.

Usage:
  python3 scripts/mathjax_lint.py              # lint the tracked Markdown tree
  python3 scripts/mathjax_lint.py PATH ...     # lint the given paths
"""

from __future__ import annotations

import os
import re
import sys

SKIP_DIRS = {".git", "node_modules", ".lake", "build"}

# runs/ and payloads/ hold verbatim external model output and issued prompts.
# AGENTS.md classes them as historical and evidentiary: they were never authored
# under this convention and must not be rewritten to satisfy it. They are not
# linted, by design, and that exemption is a rule rather than an oversight.
EXEMPT_PREFIXES = ("runs" + os.sep, "payloads" + os.sep,
                   "." + os.sep + "runs" + os.sep, "." + os.sep + "payloads" + os.sep)

CORRUPTED = re.compile(r"`\$`")
OPENER = re.compile(r"(?<!`)\$`")
CLOSER = re.compile(r"`\$(?!`)")
BARE = re.compile(r"(?<![\$`\\])\$(?![\$`\s])[^\$\n]*[^\$\s\\]\$(?![\$`])")

FENCE = re.compile(r"^\s*(```|~~~)")


def strip_fences(text: str) -> str:
    """Blank fenced blocks and multi-backtick spans, preserving offsets."""
    out = []
    in_fence = False
    for line in text.splitlines(keepends=True):
        if FENCE.match(line):
            in_fence = not in_fence
            out.append(" " * (len(line) - 1) + "\n")
            continue
        if in_fence:
            out.append(" " * (len(line) - 1) + "\n")
            continue
        line = re.sub(r"(`{2,})(.+?)\1", lambda m: " " * len(m.group(0)), line)
        out.append(line)
    return "".join(out)


def strip_code_spans(text: str) -> str:
    """Blank single-backtick code spans that are not inline math.

    In this repository inline math and inline code are the same Markdown
    construct: a single-backtick span. The one distinguishes itself from the
    other by being flanked by a dollar sign on both sides. Anything else is
    code -- a shell variable, a toolchain string, a path -- and a dollar sign
    inside or beside it must not be read as a math delimiter.
    """
    def repl(m):
        i, j = m.start(), m.end()
        before = text[i - 1] if i > 0 else ""
        after = text[j] if j < len(text) else ""
        if before == "$" and after == "$":
            return m.group(0)          # inline math: keep
        return " " * len(m.group(0))   # inline code: blank
    return re.sub(r"`[^`\n]*`", repl, text)


def lint_file(path: str) -> list[str]:
    try:
        raw = open(path, encoding="utf-8").read()
    except (OSError, UnicodeDecodeError) as exc:
        return ["%s: unreadable (%s)" % (path, exc)]

    # E1 is checked before code spans are blanked: the corrupted delimiter is
    # itself a single-backtick span, so blanking first would hide it.
    defenced = strip_fences(raw)
    text = strip_code_spans(defenced)
    problems = []

    for m in CORRUPTED.finditer(defenced):
        line = defenced.count("\n", 0, m.start()) + 1
        problems.append(
            "%s:%d: E1 corrupted inline-math delimiter (extra outer backtick); "
            "see the fenced pattern in AGENTS.md" % (path, line)
        )

    n_open = len(OPENER.findall(text))
    n_close = len(CLOSER.findall(text))
    if n_open != n_close:
        problems.append(
            "%s: E2 unbalanced inline-math delimiters (%d openers, %d closers)"
            % (path, n_open, n_close)
        )

    masked = OPENER.sub("  ", CLOSER.sub("  ", text))
    masked = re.sub(r"\$\$.*?\$\$", lambda m: " " * len(m.group(0)), masked, flags=re.S)
    for m in BARE.finditer(masked):
        line = masked.count("\n", 0, m.start()) + 1
        problems.append(
            "%s:%d: E3 bare dollar-delimited inline math: %s"
            % (path, line, m.group(0)[:40])
        )

    return problems


def collect(paths: list[str]) -> list[str]:
    files = []
    for p in paths:
        if os.path.isfile(p):
            files.append(p)
            continue
        for root, dirs, names in os.walk(p):
            dirs[:] = [d for d in dirs if d not in SKIP_DIRS]
            for n in sorted(names):
                if not n.endswith(".md"):
                    continue
                f = os.path.join(root, n)
                if f.startswith(EXEMPT_PREFIXES):
                    continue
                files.append(f)
    return sorted(set(files))


def main(argv: list[str]) -> int:
    files = collect(argv[1:] or ["."])
    problems = []
    for f in files:
        problems.extend(lint_file(f))
    for p in problems:
        print(p)
    print(
        "MATHJAX LINT: %d file(s) checked, %d problem(s)" % (len(files), len(problems))
    )
    return 1 if problems else 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
