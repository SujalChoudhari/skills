# Agent Skills

Portable, composable skills for coding and writing agents. Each skill has one
canonical `SKILL.md` entrypoint following the Agent Skills convention. The
lowercase `skill.md` path is retained as a compatibility symlink for the original
repository layout, so the content has one source of truth.

## Included skills

- [`storyscope`](./storyscope/SKILL.md): Shape prose structure and reader trust
  without inventing experience or forcing a human-writing template.
- [`unslop-ui`](./unslop-ui/SKILL.md): Audit generic AI-like UI patterns while
  preserving the host design system, product intent, and interaction contracts.

## Layout

```text
skills/
├── README.md
├── LICENSE
├── storyscope/
│   ├── SKILL.md
│   ├── skill.md -> SKILL.md
│   └── references/
│       ├── editorial-checklist.md
│       └── research-boundary.md
└── unslop-ui/
    ├── SKILL.md
    ├── skill.md -> SKILL.md
    ├── references/
    │   ├── adversarial-fixture.md
    │   ├── anti-slop-checklist.md
    │   ├── audit-report-template.md
    │   └── sources.md
    └── scripts/
        └── validate_skill.py
```

## Design principles

These skills follow two public patterns:

1. **Progressive disclosure:** keep the entrypoint focused on triggers, procedure,
   completion criteria, and verification; move long references and templates behind
   explicit pointers.
2. **Small composable procedures:** use named phases, one source of truth, exact
   completion criteria, and representative fixtures instead of a giant prompt dump.

The skills are quality procedures, not authorship detectors or detector-evasion
guarantees. They do not authorize invented facts, fabricated anecdotes, broken
accessibility, or arbitrary replacement of an existing product's system.

## Sources for the format

- [Anthropic Agent Skills repository](https://github.com/anthropics/skills)
- [Agent Skills specification](https://agentskills.io/specification)
- [Matt Pocock's skills](https://github.com/mattpocock/skills)
- [Matt Pocock's writing-for-agents skill](https://github.com/mattpocock/skills/blob/main/skills/productivity/writing-for-agents/SKILL.md)
