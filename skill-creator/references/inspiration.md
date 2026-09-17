# Inspiration notes

This reference records portable design lessons from public skills and their
published documentation. It is a synthesis, not a copy of their source files.

## Anthropic `skill-creator`

- Start from user intent and the current stage: create, evaluate, or improve.
- Treat the description as the primary activation mechanism.
- Use progressive disclosure: metadata, entrypoint, then branch-specific resources.
- Create realistic test prompts and compare with a baseline when the output can be
  judged.
- Iterate from user feedback and observed transcripts, not only aggregate scores.

Source: <https://github.com/anthropics/skills/tree/main/skills/skill-creator>

## Matt Pocock's `writing-for-agents`

- A pointer must name its target and the branches that should reach it.
- Completion criteria should make done observable and sufficiently demanding.
- Use leading words to compress repeated concepts without inventing needless jargon.
- Prune no-ops, stale sediment, duplicated rules, and environment facts that the
  agent can look up directly.
- Choose model invocation only when autonomous discovery is worth its always-loaded
  description; otherwise keep the skill user-invoked where the runtime supports it.

Sources:
- <https://github.com/mattpocock/skills/blob/main/skills/productivity/writing-for-agents/SKILL.md>
- <https://github.com/mattpocock/skills/blob/main/skills/productivity/writing-for-agents/SKILL-MECHANICS.md>

## Julius Brussee's `caveman`

- Reduce ceremony, not substance.
- Keep code, commands, exact errors, numbers, and safety warnings intact.
- Treat compression as a measured behavior with clarity fallbacks, not as a license
  for vague fragments or mangled technical language.

Source: <https://github.com/JuliusBrussee/caveman/blob/main/skills/caveman/SKILL.md>

## Latent Spaces' `brag`

- Parse invocation flags and mode before starting the main workflow.
- Make the skill narrow, opinionated, and specific to the current project.
- Define output directories, intermediate artifacts, and gates explicitly.
- Keep optional behavior opt-in rather than silently changing the default path.
- Treat a rendered or produced artifact as incomplete until its real delivery checks
  pass.

Source: <https://github.com/latent-spaces/brag/blob/main/skills/brag/SKILL.md>

## Synthesis

The useful common pattern is not a voice or a checklist. It is controlled variance:
clear activation, a short ordered process, branch-local detail, explicit boundaries,
and evidence that the process reached its intended boundary. Borrow mechanics; do
not copy personalities, claims, assets, or vendor-specific commands.
