#!/usr/bin/env python3
"""Conservative, deterministic source-to-writeup proposal mapper."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from pathlib import Path


GENERATOR_VERSION = "0.1"
INLINE_MATH_OPEN = "$`"
INLINE_MATH_CLOSE = "`$"
TRANSFERS = {"verbatim", "normalized", "synthesized"}
FORMULA_POLICIES = {"none", "classify-only", "green-only"}
ENTRY_FIELDS = {
    "id",
    "source_path",
    "source_blob",
    "source_heading",
    "target_path",
    "target_heading",
    "transfer",
    "formula_policy",
}
DEFAULT_SYMBOLS = {
    "eps": r"\varepsilon",
    "delta": r"\delta",
    "rho": r"\rho",
    "gamma": r"\gamma",
    "pi": r"\pi",
    "ln": r"\ln",
    "log": r"\log{}",
    "exp": r"\exp",
    "infinity": r"\infty",
}
RED_PHRASES = (
    "sum over",
    "product over",
    "for every",
    "for all",
    "exists",
    "such that",
    "in fam",
    "even d",
    "choose",
    "let",
    "where",
)
YELLOW_WORDS = ("min", "max", "floor", "ceil")
SOURCE_COMMENT_RE = re.compile(r"<!--\s*sources:\s*([^>]+?)\s*-->")
HEADING_RE = re.compile(rb"^(#{1,6})[ \t]+")
ID_RE = re.compile(r"^[A-Za-z0-9][A-Za-z0-9._-]*$")
TOKEN_RE = re.compile(
    r"<=|>=|!=|->|[=+*/^(),\[\]{}<>-]|"
    r"[A-Za-z_][A-Za-z0-9_]*|\d+(?:\.\d+)?|\s+"
)


class MapperError(ValueError):
    """A deterministic validation or rendering failure."""


def _scalar(value: str, line_number: int) -> object:
    value = value.strip()
    if not value:
        raise MapperError(f"line {line_number}: empty scalar")
    if value.startswith('"'):
        try:
            parsed = json.loads(value)
        except json.JSONDecodeError as exc:
            raise MapperError(f"line {line_number}: invalid quoted scalar") from exc
        if not isinstance(parsed, str):
            raise MapperError(f"line {line_number}: scalar must be a string")
        return parsed
    if value.startswith("'"):
        if len(value) < 2 or not value.endswith("'"):
            raise MapperError(f"line {line_number}: invalid quoted scalar")
        return value[1:-1].replace("''", "'")
    if value == "1":
        return 1
    return value


def parse_manifest_text(text: str) -> dict[str, object]:
    """Parse the documented indentation-only YAML subset."""
    if "\t" in text:
        raise MapperError("tabs are not allowed")
    result: dict[str, object] = {"symbols": {}, "entries": []}
    section: str | None = None
    current: dict[str, object] | None = None
    seen_top: set[str] = set()

    for number, raw in enumerate(text.splitlines(), 1):
        if not raw.strip() or raw.lstrip().startswith("#"):
            continue
        indent = len(raw) - len(raw.lstrip(" "))
        stripped = raw[indent:]

        if indent == 0:
            current = None
            if ":" not in stripped:
                raise MapperError(f"line {number}: expected top-level key")
            key, value = stripped.split(":", 1)
            if key in seen_top:
                raise MapperError(f"line {number}: duplicate top-level key {key}")
            seen_top.add(key)
            if key in {"symbols", "entries"}:
                if value.strip():
                    raise MapperError(f"line {number}: {key} must be a block")
                section = key
                continue
            if key not in {"version", "source_commit"}:
                raise MapperError(f"line {number}: unknown top-level key {key}")
            result[key] = _scalar(value, number)
            section = None
            continue

        if section == "symbols":
            if indent != 2 or stripped.startswith("-") or ":" not in stripped:
                raise MapperError(f"line {number}: malformed symbols indentation")
            key, value = stripped.split(":", 1)
            symbols = result["symbols"]
            assert isinstance(symbols, dict)
            if not ID_RE.fullmatch(key):
                raise MapperError(f"line {number}: invalid symbol token {key}")
            if key in symbols:
                raise MapperError(f"line {number}: duplicate symbol token {key}")
            symbols[key] = str(_scalar(value, number))
            continue

        if section == "entries":
            entries = result["entries"]
            assert isinstance(entries, list)
            if indent == 2 and stripped.startswith("- "):
                rest = stripped[2:]
                if ":" not in rest:
                    raise MapperError(f"line {number}: malformed list item")
                key, value = rest.split(":", 1)
                if key != "id":
                    raise MapperError(f"line {number}: entry must begin with id")
                current = {key: _scalar(value, number)}
                entries.append(current)
                continue
            if indent == 4 and current is not None and ":" in stripped:
                key, value = stripped.split(":", 1)
                if key in current:
                    raise MapperError(f"line {number}: duplicate entry field {key}")
                current[key] = _scalar(value, number)
                continue
            raise MapperError(f"line {number}: malformed entries indentation")

        raise MapperError(f"line {number}: unexpected indentation")

    if result.get("version") != 1:
        raise MapperError("version must be 1")
    commit = result.get("source_commit")
    if not isinstance(commit, str) or not re.fullmatch(r"[0-9a-f]{40}", commit):
        raise MapperError("source_commit must be a lowercase 40-hex Git id")
    entries = result["entries"]
    assert isinstance(entries, list)
    if not entries:
        raise MapperError("entries must not be empty")
    return result


def load_manifest(path: Path) -> dict[str, object]:
    try:
        return parse_manifest_text(path.read_text(encoding="utf-8"))
    except (OSError, UnicodeError) as exc:
        raise MapperError(f"cannot read manifest: {exc}") from exc


def git_blob_sha(data: bytes) -> str:
    header = b"blob " + str(len(data)).encode("ascii") + b"\0"
    return hashlib.sha1(header + data).hexdigest()


def _relative_path(value: object, label: str) -> Path:
    if not isinstance(value, str) or not value:
        raise MapperError(f"{label} must be a nonempty string")
    path = Path(value)
    if path.is_absolute() or ".." in path.parts:
        raise MapperError(f"{label} must be a confined relative path: {value}")
    return path


def _heading_matches(data: bytes, heading: str) -> list[int]:
    wanted = heading.encode("utf-8")
    return [
        index
        for index, line in enumerate(data.splitlines(keepends=True))
        if line.rstrip(b"\r\n") == wanted
    ]


def extract_section(data: bytes, heading: str) -> bytes:
    """Extract one exact Markdown section while retaining source bytes."""
    lines = data.splitlines(keepends=True)
    matches = _heading_matches(data, heading)
    if not matches:
        raise MapperError(f"source heading is missing: {heading}")
    if len(matches) != 1:
        raise MapperError(f"source heading is not unique: {heading}")
    start = matches[0]
    match = HEADING_RE.match(lines[start])
    if not match:
        raise MapperError(f"source heading is not Markdown: {heading}")
    level = len(match.group(1))
    end = len(lines)
    for index in range(start + 1, len(lines)):
        next_match = HEADING_RE.match(lines[index])
        if next_match and len(next_match.group(1)) <= level:
            end = index
            break
    return b"".join(lines[start:end])


def _target_has_heading(data: bytes, heading: str) -> bool:
    return bool(_heading_matches(data, heading))


def _canonical_markdown(root: Path) -> list[Path]:
    writeup = root / "writeup"
    if not writeup.is_dir():
        return []
    return sorted(
        path
        for path in writeup.glob("*.md")
        if path.is_file()
    )


def validate_manifest(
    manifest: dict[str, object], manifest_path: Path
) -> tuple[list[dict[str, object]], list[str]]:
    root = manifest_path.resolve().parent.parent
    raw_entries = manifest["entries"]
    assert isinstance(raw_entries, list)
    ids: set[str] = set()
    verified: list[dict[str, object]] = []

    for number, raw_entry in enumerate(raw_entries, 1):
        assert isinstance(raw_entry, dict)
        missing = ENTRY_FIELDS - raw_entry.keys()
        extra = raw_entry.keys() - ENTRY_FIELDS
        if missing:
            raise MapperError(f"entry {number}: missing fields {sorted(missing)}")
        if extra:
            raise MapperError(f"entry {number}: unknown fields {sorted(extra)}")
        entry = {key: str(value) for key, value in raw_entry.items()}
        entry_id = entry["id"]
        if not ID_RE.fullmatch(entry_id):
            raise MapperError(f"entry {number}: invalid id {entry_id}")
        if entry_id in ids:
            raise MapperError(f"duplicate source id: {entry_id}")
        ids.add(entry_id)
        if entry["transfer"] not in TRANSFERS:
            raise MapperError(f"entry {entry_id}: unknown transfer {entry['transfer']}")
        if entry["formula_policy"] not in FORMULA_POLICIES:
            raise MapperError(
                f"entry {entry_id}: unknown formula policy {entry['formula_policy']}"
            )
        source_rel = _relative_path(entry["source_path"], "source_path")
        target_rel = _relative_path(entry["target_path"], "target_path")
        source = root / source_rel
        target = root / target_rel
        if not source.is_file():
            raise MapperError(f"entry {entry_id}: source file does not exist")
        source_data = source.read_bytes()
        actual = git_blob_sha(source_data)
        if actual != entry["source_blob"]:
            raise MapperError(
                f"entry {entry_id}: source drift: expected {entry['source_blob']}, got {actual}"
            )
        extract_section(source_data, entry["source_heading"])
        if not target.is_file():
            raise MapperError(f"entry {entry_id}: target file does not exist")
        if not _target_has_heading(target.read_bytes(), entry["target_heading"]):
            raise MapperError(f"entry {entry_id}: target heading is missing")
        verified.append(entry)

    used: set[str] = set()
    for path in _canonical_markdown(root):
        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeError as exc:
            raise MapperError(f"canonical file is not UTF-8: {path}") from exc
        for match in SOURCE_COMMENT_RE.finditer(text):
            for source_id in (part.strip() for part in match.group(1).split(",")):
                if not source_id:
                    raise MapperError(f"empty source-comment id in {path}")
                if source_id not in ids:
                    raise MapperError(
                        f"unknown source-comment id {source_id} in {path.relative_to(root)}"
                    )
                used.add(source_id)
    warnings = [f"unused manifest ID: {entry_id}" for entry_id in sorted(ids - used)]
    return verified, warnings


def _protected_line(line: str, in_fence: bool, in_comment: bool) -> bool:
    stripped = line.lstrip()
    if in_fence or in_comment:
        return True
    if stripped.startswith(">") or stripped.startswith("|"):
        return True
    if stripped.startswith("---"):
        return True
    if "`" in line or "<!--" in line or re.search(r"\[[^]]+\]\([^)]*\)", line):
        return True
    if re.search(r"(?:^|\s)(?:[A-Za-z0-9_.-]+/)+[A-Za-z0-9_.-]+", line):
        return True
    if re.search(r"\b[A-Za-z0-9_.-]+\.(?:md|py|ya?ml|lean|json)\b", line):
        return True
    if re.search(r"\b[0-9a-f]{40,64}\b", line):
        return True
    if stripped.startswith(('"', "'")):
        return True
    if "|" in line:
        return True
    return False


def _normalize_inline_dollar_spans(line: str) -> tuple[str, bool]:
    """Wrap plain inline dollar math with GitHub's inner backticks."""
    output: list[str] = []
    index = 0
    changed = False
    while index < len(line):
        if line.startswith(INLINE_MATH_OPEN, index):
            end = line.find(INLINE_MATH_CLOSE, index + len(INLINE_MATH_OPEN))
            if end < 0:
                output.append(line[index:])
                break
            end += len(INLINE_MATH_CLOSE)
            output.append(line[index:end])
            index = end
            continue
        if line.startswith("$$", index):
            output.append("$$")
            index += 2
            continue
        if line[index] == "`":
            run = 1
            while index + run < len(line) and line[index + run] == "`":
                run += 1
            marker = "`" * run
            end = line.find(marker, index + run)
            if end < 0:
                output.append(line[index:])
                break
            end += run
            output.append(line[index:end])
            index = end
            continue
        if line[index] == "$":
            end = index + 1
            while end < len(line):
                if line[end] == "`":
                    end = -1
                    break
                if (
                    line[end] == "$"
                    and (end + 1 == len(line) or line[end + 1] != "$")
                ):
                    break
                end += 1
            if end >= 0 and end < len(line) and line[end] == "$":
                content = line[index + 1 : end]
                output.extend((INLINE_MATH_OPEN, content, INLINE_MATH_CLOSE))
                index = end + 1
                changed = True
                continue
        output.append(line[index])
        index += 1
    return "".join(output), changed


def _normalize_substack_row_breaks(line: str) -> tuple[str, bool]:
    """Use KaTeX-compatible ``\\cr`` separators inside ``\\substack``."""
    output: list[str] = []
    position = 0
    changed = False
    opener = r"\substack{"
    while True:
        start = line.find(opener, position)
        if start < 0:
            output.append(line[position:])
            break
        output.append(line[position : start + len(opener)])
        position = start + len(opener)
        depth = 1
        while position < len(line) and depth:
            if line.startswith(r"\\", position):
                output.append(r" \cr ")
                position += 2
                changed = True
                continue
            char = line[position]
            output.append(char)
            if char == "{":
                depth += 1
            elif char == "}":
                depth -= 1
            position += 1
        if depth:
            output.append(line[position:])
            break
    return "".join(output), changed


def _candidate_kind(line: str) -> str | None:
    stripped = line.strip()
    if not stripped or not re.search(r"<=|>=|!=|(?<![-])=(?!=)|->", stripped):
        return None
    if line.startswith("    ") or line.startswith("\t"):
        return "indented"
    if re.fullmatch(r"[A-Za-z0-9_.,+*/^()\[\]{}<>=!~| \t-]+", stripped):
        return "standalone"
    return None


def _balanced(text: str) -> bool:
    pairs = {')': '(', ']': '[', '}': '{'}
    stack: list[str] = []
    for char in text:
        if char in "([{":
            stack.append(char)
        elif char in pairs:
            if not stack or stack.pop() != pairs[char]:
                return False
    return not stack


def _tokenize(text: str) -> list[str] | None:
    tokens: list[str] = []
    position = 0
    while position < len(text):
        match = TOKEN_RE.match(text, position)
        if not match:
            return None
        token = match.group(0)
        if not token.isspace():
            tokens.append(token)
        position = match.end()
    return tokens


def _formula_class(text: str, kind: str) -> str:
    lower = text.lower()
    if any(phrase in lower for phrase in RED_PHRASES):
        return "red"
    if re.match(r"(?:[-*+]|\d+[.)])\s", text):
        return "yellow"
    if re.search(
        r"\b(?:OPEN|PROVED|CONDITIONAL|MEASURED|HEURISTIC|UNVERIFIED|CLOSED)\b",
        text,
    ):
        return "yellow"
    if any(re.search(rf"\b{word}\b", lower) for word in YELLOW_WORDS):
        return "yellow"
    if "~" in text or "|" in text or "{" in text or "}" in text:
        return "yellow"
    if kind != "indented" and re.search(r"[A-Za-z]{3,}\s+[A-Za-z]{3,}", text):
        return "yellow"
    if not _balanced(text) or _tokenize(text) is None:
        return "yellow"
    return "green"


def _normalize_green(text: str, symbols: dict[str, str]) -> str | None:
    original = _tokenize(text)
    if original is None:
        return None
    converted: list[str] = []
    replacements = {"<=": r"\le", ">=": r"\ge", "!=": r"\ne", "->": r"\to"}
    for token in original:
        converted.append(replacements.get(token, symbols.get(token, token)))

    reverse: dict[str, str] = {value: key for key, value in replacements.items()}
    ambiguous: set[str] = set()
    for key, value in symbols.items():
        if value in reverse and reverse[value] != key:
            ambiguous.add(value)
        reverse[value] = key
    if any(token in ambiguous for token in converted):
        return None
    inverse = [reverse.get(token, token) for token in converted]
    if inverse != original:
        return None
    return " ".join(converted)


def normalize_formulas(
    text: str, symbols: dict[str, str], policy: str = "green-only"
) -> tuple[str, list[dict[str, object]], list[dict[str, object]]]:
    lines = text.splitlines(keepends=True)
    raw_candidates = [_candidate_kind(line) is not None for line in lines]
    multiline_chain_lines: set[int] = set()
    for index in range(len(lines) - 1):
        if raw_candidates[index] and raw_candidates[index + 1]:
            multiline_chain_lines.update({index, index + 1})
    output: list[str] = []
    classifications: list[dict[str, object]] = []
    conversions: list[dict[str, object]] = []
    in_fence = False
    in_comment = False
    frontmatter = bool(lines and lines[0].rstrip("\r\n") == "---")

    for number, line in enumerate(lines, 1):
        stripped = line.strip()
        if stripped.startswith("```") or stripped.startswith("~~~"):
            in_fence = not in_fence
            output.append(line)
            continue
        inline_protected = in_comment or frontmatter or "<!--" in line
        if not inline_protected:
            original_line = line
            line, substack_changed = _normalize_substack_row_breaks(line)
            line, inline_changed = _normalize_inline_dollar_spans(line)
            if substack_changed or inline_changed:
                conversions.append(
                    {
                        "line": number,
                        "from": original_line.rstrip("\r\n"),
                        "to": line.rstrip("\r\n"),
                    }
                )
            stripped = line.strip()
        protected = _protected_line(line, in_fence, in_comment) or frontmatter
        if "<!--" in line and "-->" not in line:
            in_comment = True
        if in_comment and "-->" in line:
            protected = True
            in_comment = False
        if frontmatter and number > 1 and stripped == "---":
            output.append(line)
            frontmatter = False
            continue
        if not protected and re.search(r"\\[()\[\]]", line):
            newline = (
                "\r\n"
                if line.endswith("\r\n")
                else "\n"
                if line.endswith("\n")
                else ""
            )
            classifications.append(
                {
                    "line": number,
                    "classification": "yellow",
                    "text": line.strip(),
                }
            )
            output.append(
                "<!-- mapper-review: yellow; no automatic conversion -->" + newline
            )
            output.append(line)
            continue
        kind = None if protected else _candidate_kind(line)
        if kind is None:
            output.append(line)
            continue
        formula = line.strip()
        classification = _formula_class(formula, kind)
        if number - 1 in multiline_chain_lines and classification != "red":
            classification = "yellow"
        record = {"line": number, "classification": classification, "text": formula}
        classifications.append(record)
        newline = "\r\n" if line.endswith("\r\n") else "\n" if line.endswith("\n") else ""
        if classification == "green" and policy == "green-only":
            converted = _normalize_green(formula, symbols)
            if converted is not None:
                output.append(f"$$\n{converted}\n$${newline}")
                conversions.append({"line": number, "from": formula, "to": converted})
                continue
            classification = "yellow"
            record["classification"] = "yellow"
        if classification == "yellow":
            output.append("<!-- mapper-review: yellow; no automatic conversion -->" + newline)
        elif classification == "red":
            output.append(
                "<!-- mapper-review: red; mathematical interpretation required -->" + newline
            )
        output.append(line)
    return "".join(output), classifications, conversions


def _safe_output(output_dir: Path, filename: str) -> Path:
    base = output_dir.resolve()
    candidate = (base / filename).resolve()
    if candidate.parent != base:
        raise MapperError(f"render output escapes requested directory: {filename}")
    return candidate


def _provenance(entry: dict[str, object], commit: str) -> bytes:
    fields = [
        ("source_commit", commit),
        ("source_blob", entry["source_blob"]),
        ("source_path", entry["source_path"]),
        ("source_heading", entry["source_heading"]),
        ("target_path", entry["target_path"]),
        ("target_heading", entry["target_heading"]),
        ("transfer", entry["transfer"]),
        ("formula_policy", entry["formula_policy"]),
        ("generator_version", GENERATOR_VERSION),
    ]
    body = "<!-- writeup-mapper\n" + "".join(f"{key}: {value}\n" for key, value in fields) + "-->\n"
    return body.encode("utf-8")


def render(manifest_path: Path, output_dir: Path) -> tuple[list[str], list[str]]:
    manifest = load_manifest(manifest_path)
    entries, warnings = validate_manifest(manifest, manifest_path)
    root = manifest_path.resolve().parent.parent
    output_dir.mkdir(parents=True, exist_ok=True)
    symbols = dict(DEFAULT_SYMBOLS)
    custom_symbols = manifest["symbols"]
    assert isinstance(custom_symbols, dict)
    symbols.update({str(key): str(value) for key, value in custom_symbols.items()})
    report_entries: list[dict[str, object]] = []

    for entry in entries:
        source_data = (root / str(entry["source_path"])).read_bytes()
        packet = extract_section(source_data, str(entry["source_heading"]))
        classifications: list[dict[str, object]] = []
        conversions: list[dict[str, object]] = []
        transfer = str(entry["transfer"])
        policy = str(entry["formula_policy"])
        if transfer == "normalized":
            normalized, classifications, conversions = normalize_formulas(
                packet.decode("utf-8"), symbols, policy
            )
            packet = normalized.encode("utf-8")
        prefix = _provenance(entry, str(manifest["source_commit"]))
        if transfer == "synthesized":
            prefix += b"<!-- human-synthesis-required: source packet only -->\n"
        destination = _safe_output(output_dir, f"{entry['id']}.candidate.md")
        destination.write_bytes(prefix + packet)
        report_entries.append(
            {
                "conversions_performed": conversions,
                "formula_classifications": classifications,
                "id": entry["id"],
                "source_verification": "verified",
            }
        )

    report = {
        "conversions_performed": sum(
            (item["conversions_performed"] for item in report_entries), []
        ),
        "formula_classifications": sum(
            (item["formula_classifications"] for item in report_entries), []
        ),
        "processed_entries": report_entries,
        "source_verification_status": "verified",
        "warnings": warnings,
    }
    report_path = _safe_output(output_dir, "report.json")
    report_path.write_text(
        json.dumps(report, indent=2, sort_keys=True, ensure_ascii=False) + "\n",
        encoding="utf-8",
        newline="\n",
    )
    return [str(entry["id"]) for entry in entries], warnings


def command_check(manifest_path: Path) -> int:
    try:
        manifest = load_manifest(manifest_path)
        _, warnings = validate_manifest(manifest, manifest_path)
    except MapperError as exc:
        print(f"FAIL: {exc}", file=sys.stderr)
        return 1
    for warning in warnings:
        print(f"WARNING: {warning}")
    print("PASS")
    return 0


def command_render(manifest_path: Path, output_dir: Path) -> int:
    try:
        processed, warnings = render(manifest_path, output_dir)
    except MapperError as exc:
        print(f"FAIL: {exc}", file=sys.stderr)
        return 1
    for warning in warnings:
        print(f"WARNING: {warning}")
    print(f"PASS: rendered {len(processed)} entries")
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    subparsers = parser.add_subparsers(dest="command", required=True)
    check = subparsers.add_parser("check")
    check.add_argument("--manifest", type=Path, required=True)
    render_parser = subparsers.add_parser("render")
    render_parser.add_argument("--manifest", type=Path, required=True)
    render_parser.add_argument("--output-dir", type=Path, required=True)
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    if args.command == "check":
        return command_check(args.manifest)
    return command_render(args.manifest, args.output_dir)


if __name__ == "__main__":
    raise SystemExit(main())
