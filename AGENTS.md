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

## Evidence discipline

- Preserve proved, conditional, measured, heuristic, and model-only classifications.
- Never strengthen a mathematical statement during exposition or formatting work.
- Preserve scope qualifiers, constants, quantifier order, and dependency declarations.

## Repository history

- Treat dossier/, runs/, and payloads/ as historical and evidentiary material.
- Modify those paths only when the execution contract explicitly allows it.

## Roadmap

- For roadmap operations, use the `roadmap-items` skill.
- Do not hand-edit roadmap state when the roadmap tool supports the operation.
