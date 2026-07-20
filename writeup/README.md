# Curated writeup

The `writeup/` directory is a curated, human-readable account of the mathematical state of the project. The working language is English.

Canonical historical, audit, computation, and provenance material remains in `dossier/`, `runs/`, `payloads/`, `ledger.yaml`, and `lean/`. The files here are expository derivatives, not replacements for those sources. Substantive sections map back to source packets through `sources.yml`.

Generated proposals under `_draft/` are never canonical. Manual review is mandatory before any draft material moves into a canonical writeup file, and the source comments must remain in place until that review is complete.

## File map

- `status.md` gives the concise mathematical status.
- `technical-note.md` develops the notation, reductions, and current barrier.
- `notation.md` is a compact symbol guide.
- `references.md` separates external literature, internal sources, and verification sources.
- `sources.yml` records section-level provenance for the conservative mapper.
- `_draft/` is the disposable destination for generated proposals.

## Manifest grammar

The mapper accepts a deliberately restricted YAML subset. Indentation uses spaces only. Top-level scalar keys have the form `key: value`; `symbols` is a two-space-indented scalar map; `entries` is a list whose `- id` line is indented two spaces and whose remaining scalar fields are indented four spaces. Blank lines and full-line comments are allowed. Flow collections, anchors, aliases, multiline scalars, tags, implicit booleans, and arbitrary nesting are not allowed.
