# Agent Skills

Small, portable skills for coding and writing agents. Each skill lives in its own
folder and starts with a lowercase `skill.md` entrypoint.

## Included

- [`storyscope`](./storyscope/skill.md): Shape prose structure and reader trust
  without inventing experience or forcing a human-writing template.
- [`unslop-ui`](./unslop-ui/skill.md): Audit generic AI-like UI patterns while
  preserving the host design system, product intent, and interaction contracts.

## Layout

```text
skills/
├── README.md
├── LICENSE
├── storyscope/
│   ├── skill.md
│   └── references/
│       └── editorial-checklist.md
└── unslop-ui/
    ├── skill.md
    └── references/
        ├── anti-slop-checklist.md
        ├── audit-report-template.md
        └── sources.md
```

The entrypoints stay focused on triggers, procedure, boundaries, and verification.
Long checklists and report shapes live beside the skill and are read only when the
relevant branch needs them.

These are quality procedures, not authorship detectors or detector-evasion
promises. They do not authorize invented facts, fabricated anecdotes, broken
accessibility, or arbitrary replacement of an existing product's system.

## Format references

- [Anthropic Agent Skills](https://github.com/anthropics/skills)
- [Agent Skills specification](https://agentskills.io/specification)
- [Matt Pocock's skills](https://github.com/mattpocock/skills)
- [Writing documents for agents](https://github.com/mattpocock/skills/blob/main/skills/productivity/writing-for-agents/SKILL.md)
