# AGENTS.md

## Execution environment

- The default executor is local in a VS Code IDE extension on Linux.
- The project supports both Anthropic Claude Code and OpenAI Codex plugins.
- Do not delegate repository work or computation to Codex Cloud.
- Number-crunching, Lean builds, and census runs execute on the local workstation.
- Do not assume cloud memory, CPU, storage, or runtime characteristics.

## Steering and execution

- Steering may create only proposed roadmap items.
- Execute only ratified items.
- Operator ratification is mandatory.
- The ratifying commit or merge is the handover from steering to execution.
- Byte-exact execution contracts are ephemeral and pinned to one commit.

## Discovery and planning
- If you want to discover content from files ALWAYS read the full file.
- DO NOT use windowing techniques (sed-windows, head, tail) for discovery.
- You may use windowing techniques for targeted edits only during execution
  and to prepare changes where discovery has exactly located the target.

## Evidence discipline

- Preserve proved, conditional, measured, heuristic, and model-only classifications.
- Never strengthen a mathematical statement during exposition or formatting work.
- Preserve scope qualifiers, constants, quantifier order, and dependency declarations.

## Report generation and MathJax

- Generated Markdown reports must use the repository's MathJax-compatible notation.
- Inline formulas carry a four-character delimiter pair whose halves each
  contain a backtick. An inline example cannot show them without escaping, and
  the escape character is itself a backtick, so the pattern below is the ONLY
  authoritative source for it. Copy it from there; never reconstruct it from a
  prose description, and never wrap it in outer backticks.

  ```
  $`S`$
  ```

  Opener is dollar then backtick; closer is backtick then dollar. Never use bare
  dollar delimiters. Keep display formulas in `$$` blocks.
- Use `\mathrm{...}` instead of `\operatorname{...}`.
- Write absolute values and cardinalities with `\lvert ... \rvert`; never use
  bare pipes, `\#`, or `#` as mathematical cardinality notation.
- Inside `\substack{...}`, separate rows with `\cr`, never a double backslash.
  This restriction is local to `\substack`; retain the double backslash where
  required by environments such as `aligned` or `array`.
- For visible braces, use `\lbrace` and `\rbrace` instead of the escaped
  literal braces.
- For logarithm, use `\log{}` instead of raw `\log`. If you need an index,
  use `\log_n{}` where n is the index.
- `scripts/mathjax_lint.py` enforces the delimiter rule. Run it before handing
  over any generated Markdown; CI runs it on every push.
- Apply these rules to mathematical prose and formulas only. Preserve Markdown
  headings and table delimiters, divisibility notation such as ``\mid``, and
  literal source or code fences unless a task explicitly calls for changing them.

## Repository history

- Treat dossier/, runs/, and payloads/ as historical and evidentiary material.
- Modify those paths only when the execution contract explicitly allows it.

## Roadmap

- For roadmap operations, use the `roadmap-items` skill.
- Do not hand-edit roadmap state when the roadmap tool supports the operation.
