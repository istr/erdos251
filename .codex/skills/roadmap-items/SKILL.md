---
name: roadmap-items
description: >-
  Manage the repository's item-based roadmap/backlog. Use this skill for roadmap
  items, arcs, execution order, prioritization, ratification, or landed versus
  open state. The shared workflow is the source of truth; do not hand-edit the
  roadmap when its commands apply.
---

# roadmap-items (Codex adapter)

This is a discovery adapter only. Before acting, read and follow the shared
workflow at `.agents/skills/roadmap-items/SKILL.md` in full. Its script,
references, assets, schema, command semantics, and ratification gate are the
single source of truth.

From the repository root, invoke the shared implementation with:

```
python3 .agents/skills/roadmap-items/scripts/roadmap.py <command> [options]
```
