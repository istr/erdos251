import hashlib
import importlib.util
import tempfile
import unittest
from pathlib import Path


SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "writeup_mapper.py"
SPEC = importlib.util.spec_from_file_location("writeup_mapper", SCRIPT)
mapper = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(mapper)


class MapperFixture(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.root = Path(self.temporary.name)
        (self.root / "writeup").mkdir()
        self.source = self.root / "source.md"
        self.source.write_bytes(b"# Source\r\n\r\nbody\r\n")
        self.target = self.root / "writeup" / "target.md"
        self.target.write_text(
            "# Target\n\n<!-- sources: source-main -->\nText.\n",
            encoding="utf-8",
        )
        self.manifest = self.root / "writeup" / "sources.yml"
        self.write_manifest()

    def tearDown(self):
        self.temporary.cleanup()

    def manifest_text(self, **changes):
        values = {
            "id": "source-main",
            "source_path": "source.md",
            "source_blob": mapper.git_blob_sha(self.source.read_bytes()),
            "source_heading": "# Source",
            "target_path": "writeup/target.md",
            "target_heading": "# Target",
            "transfer": "verbatim",
            "formula_policy": "none",
        }
        values.update(changes)
        return (
            "# restricted mapper manifest\n"
            "version: 1\n"
            f"source_commit: {'1' * 40}\n"
            "symbols:\n"
            "  eps: \\varepsilon\n"
            "entries:\n"
            f"  - id: {values['id']}\n"
            f"    source_path: {values['source_path']}\n"
            f"    source_blob: {values['source_blob']}\n"
            f"    source_heading: {values['source_heading']}\n"
            f"    target_path: {values['target_path']}\n"
            f"    target_heading: {values['target_heading']}\n"
            f"    transfer: {values['transfer']}\n"
            f"    formula_policy: {values['formula_policy']}\n"
        )

    def write_manifest(self, **changes):
        self.manifest.write_text(self.manifest_text(**changes), encoding="utf-8")

    def validated(self):
        parsed = mapper.load_manifest(self.manifest)
        return mapper.validate_manifest(parsed, self.manifest)


class ManifestTests(MapperFixture):
    def test_01_valid_manifest_parses(self):
        parsed = mapper.load_manifest(self.manifest)
        self.assertEqual(parsed["version"], 1)
        self.assertEqual(parsed["entries"][0]["id"], "source-main")

    def test_02_malformed_indentation_is_rejected(self):
        text = self.manifest_text().replace("    source_path", "   source_path")
        with self.assertRaises(mapper.MapperError):
            mapper.parse_manifest_text(text)

    def test_03_duplicate_source_ids_are_rejected(self):
        text = self.manifest_text()
        duplicate = text[text.index("  - id:") :]
        self.manifest.write_text(text + duplicate, encoding="utf-8")
        with self.assertRaisesRegex(mapper.MapperError, "duplicate source id"):
            self.validated()

    def test_04_unknown_enum_values_are_rejected(self):
        self.write_manifest(transfer="creative")
        with self.assertRaisesRegex(mapper.MapperError, "unknown transfer"):
            self.validated()

    def test_05_path_traversal_is_rejected(self):
        self.write_manifest(source_path="../source.md")
        with self.assertRaisesRegex(mapper.MapperError, "confined relative path"):
            self.validated()

    def test_06_correct_git_blob_sha_passes(self):
        entries, warnings = self.validated()
        self.assertEqual(entries[0]["source_blob"], mapper.git_blob_sha(self.source.read_bytes()))
        self.assertEqual(warnings, [])

    def test_07_source_drift_fails(self):
        self.source.write_text("# Source\nchanged\n", encoding="utf-8")
        with self.assertRaisesRegex(mapper.MapperError, "source drift"):
            self.validated()


class ExtractionTests(unittest.TestCase):
    def test_08_unique_heading_extraction_succeeds(self):
        data = b"# A\r\nalpha\r\n## B\r\nbeta\r\n"
        self.assertEqual(mapper.extract_section(data, "## B"), b"## B\r\nbeta\r\n")

    def test_09_missing_heading_fails(self):
        with self.assertRaisesRegex(mapper.MapperError, "missing"):
            mapper.extract_section(b"# A\n", "## B")

    def test_10_duplicate_heading_fails(self):
        with self.assertRaisesRegex(mapper.MapperError, "not unique"):
            mapper.extract_section(b"# A\n# A\n", "# A")

    def test_11_extraction_stops_at_equal_or_higher_heading(self):
        data = b"# A\n## B\ntext\n### C\nmore\n## D\nstop\n"
        self.assertEqual(
            mapper.extract_section(data, "## B"), b"## B\ntext\n### C\nmore\n"
        )


class FormulaTests(unittest.TestCase):
    def normalize(self, text, symbols=None):
        return mapper.normalize_formulas(
            text, symbols or dict(mapper.DEFAULT_SYMBOLS), "green-only"
        )

    def test_12_fenced_code_is_protected(self):
        text = "```\n    eps <= delta\n```\n"
        output, classes, conversions = self.normalize(text)
        self.assertEqual(output, text)
        self.assertEqual(classes, [])
        self.assertEqual(conversions, [])

    def test_13_tables_are_protected(self):
        text = "| eps <= delta | $rho$ |\n| --- | --- |\n"
        output, classes, conversions = self.normalize(text)
        self.assertEqual(output, "| eps <= delta | $`rho`$ |\n| --- | --- |\n")
        self.assertEqual(classes, [])
        self.assertEqual(len(conversions), 1)

    def test_14_inline_code_is_protected(self):
        text = "Use `eps <= delta` here.\n"
        output, classes, conversions = self.normalize(text)
        self.assertEqual(output, text)
        self.assertEqual(classes, [])
        self.assertEqual(conversions, [])
        mixed = "Math $eps <= delta$ and code `$rho$`.\n"
        mixed_output, mixed_classes, mixed_conversions = self.normalize(mixed)
        self.assertEqual(
            mixed_output,
            "Math $`eps <= delta`$ and code `$rho$`.\n",
        )
        self.assertEqual(mixed_classes, [])
        self.assertEqual(len(mixed_conversions), 1)

    def test_15_inline_math_uses_github_wrapper(self):
        text = "Plain $eps <= delta$; wrapped $`rho`$; display $$x = y$$.\n"
        output, classes, conversions = self.normalize(text)
        self.assertEqual(
            output,
            "Plain $`eps <= delta`$; wrapped $`rho`$; display $$x = y$$.\n",
        )
        self.assertEqual(classes, [])
        self.assertEqual(len(conversions), 1)

    def test_16_substack_row_breaks_use_cr(self):
        text = "$$\n\\sum_{\\substack{d\\ge2\\\\2\\mid d}}\n$$\n"
        output, classes, conversions = self.normalize(text)
        self.assertEqual(
            output,
            "$$\n\\sum_{\\substack{d\\ge2 \\cr 2\\mid d}}\n$$\n",
        )
        self.assertEqual(classes, [])
        self.assertEqual(len(conversions), 1)

    def test_17_green_formula_is_converted(self):
        output, classes, conversions = self.normalize("    eps <= delta -> infinity\n")
        self.assertEqual(output, "$$\n\\varepsilon \\le \\delta \\to \\infty\n$$\n")
        self.assertEqual(classes[0]["classification"], "green")
        self.assertEqual(len(conversions), 1)

    def test_18_log_symbol_uses_empty_group(self):
        output, classes, conversions = self.normalize("    log <= delta\n")
        self.assertEqual(output, "$$\n\\log{} \\le \\delta\n$$\n")
        self.assertEqual(classes[0]["classification"], "green")
        self.assertEqual(len(conversions), 1)

    def test_19_inverse_token_mismatch_blocks_conversion(self):
        symbols = {"foo": r"\delta", "delta": r"\delta"}
        output, classes, conversions = self.normalize("    foo = delta\n", symbols)
        self.assertIn("mapper-review: yellow", output)
        self.assertEqual(classes[0]["classification"], "yellow")
        self.assertEqual(conversions, [])

    def test_20_yellow_input_is_unchanged_and_marked(self):
        text = "    value = max(a, b)\n"
        output, classes, conversions = self.normalize(text)
        self.assertTrue(output.endswith(text))
        self.assertIn("mapper-review: yellow", output)
        self.assertEqual(classes[0]["classification"], "yellow")
        self.assertEqual(conversions, [])
        legacy = r"Legacy \(eps <= delta\)." + "\n"
        legacy_output, legacy_classes, legacy_conversions = self.normalize(legacy)
        self.assertTrue(legacy_output.endswith(legacy))
        self.assertIn("mapper-review: yellow", legacy_output)
        self.assertEqual(legacy_classes[0]["classification"], "yellow")
        self.assertEqual(legacy_conversions, [])

    def test_21_red_pseudomathematics_is_unchanged_and_marked(self):
        text = "    sum over even d >= 2\n"
        output, classes, conversions = self.normalize(text)
        self.assertTrue(output.endswith(text))
        self.assertIn("mapper-review: red", output)
        self.assertEqual(classes[0]["classification"], "red")
        self.assertEqual(conversions, [])


class RenderTests(MapperFixture):
    def _snapshot(self, directory):
        return {
            path.relative_to(directory): path.read_bytes()
            for path in sorted(directory.rglob("*"))
            if path.is_file()
        }

    def test_19_render_refuses_an_output_outside_requested_directory(self):
        output = self.root / "rendered"
        output.mkdir()
        with self.assertRaisesRegex(mapper.MapperError, "escapes"):
            mapper._safe_output(output, "../escape.md")

    def test_20_two_render_runs_are_byte_identical(self):
        first = self.root / "first"
        second = self.root / "second"
        mapper.render(self.manifest, first)
        mapper.render(self.manifest, second)
        self.assertEqual(self._snapshot(first), self._snapshot(second))

    def test_21_canonical_files_remain_byte_identical(self):
        before = hashlib.sha256(self.target.read_bytes()).digest()
        mapper.render(self.manifest, self.root / "rendered")
        after = hashlib.sha256(self.target.read_bytes()).digest()
        self.assertEqual(before, after)

    def test_22_source_comment_ids_are_validated(self):
        self.target.write_text(
            "# Target\n<!-- sources: unknown-id -->\n", encoding="utf-8"
        )
        with self.assertRaisesRegex(mapper.MapperError, "unknown source-comment id"):
            self.validated()


if __name__ == "__main__":
    unittest.main()
