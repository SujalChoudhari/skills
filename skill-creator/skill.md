---
name: skill-creator
description: Create, revise, evaluate, and package Agent Skills. Use when designing a new skill, improving an existing skill, reviewing a skill that is ignored or inconsistent, writing SKILL.md or skill.md instructions, tuning activation descriptions, or testing a skill against realistic and adversarial prompts.
---

# Skill Creator

Turn a repeatable capability into a small, predictable Agent Skill. Optimize for a
reliable process, not identical prose or a large instruction dump.

Operating loop: **INTENT -> SHAPE -> DRAFT -> PROBE -> REVISE -> PACKAGE**.
Choose the smallest loop that answers the user's request. Do not force a full
benchmark on a one-off subjective writing task; do not call a skill finished when
its behavior has never been probed.

## 1. Choose the work mode

Classify the request before editing:

- **CREATE:** no usable skill exists.
- **REVISE:** an existing skill has a known failure, drift, or trigger problem.
- **EVALUATE:** test behavior without changing the skill yet.
- **PACKAGE:** validate links, metadata, portability, and distribution layout.

Read repository instructions and inspect the target directory first. Preserve its
entrypoint convention (`SKILL.md`, `skill.md`, or another explicitly documented
path); do not create duplicate aliases merely to satisfy a preference from another
runtime.

**Done when:** the mode, target path, runtime/discovery convention, and user-visible
outcome are known.

## 2. Capture intent

Extract answers from the conversation before asking questions. Ask only for gaps
that change the design:

1. What repeatable capability should the skill provide?
2. Which user phrases, artifacts, or contexts should activate it?
3. When should it stay out of the way?
4. What inputs may it read or change?
5. What output or side effect counts as success?
6. Which dependencies, tools, runtimes, or permissions are real requirements?
7. Is evaluation expected, and can success be checked objectively?

Write a short **skill brief** before the draft:

```text
Capability: one sentence
Triggers: concrete phrases and contexts
Non-triggers: nearby requests that should not activate it
Inputs: files, arguments, state, permissions
Output: artifact, report, or verified side effect
Boundaries: what remains owner-controlled or unsupported
Success: observable completion evidence
```

Avoid turning a preference into a skill. A skill earns its maintenance cost when it
captures a recurring workflow, judgment pattern, domain procedure, or tool sequence
that benefits from consistent execution.

**Done when:** the brief distinguishes capability, trigger, boundary, and evidence.

## 3. Shape the information hierarchy

Put material at the lowest useful load:

1. **Frontmatter:** name and activation description only.
2. **Entrypoint body:** the procedure, branch decisions, boundaries, and completion
   criteria needed on every activation.
3. **References:** detailed rules, schemas, examples, source notes, or branch-only
   guidance, linked with a condition for reading them.
4. **Scripts/assets:** deterministic helpers or files used in the produced artifact.

Use progressive disclosure by branch: inline what every run needs; disclose what only
one branch needs. Co-locate a concept's definition, rules, and caveats. Keep one
source of truth. Do not duplicate the same rule in the body, README, and reference
just to make it feel important.

A pointer must say both **what the file contains** and **when to read it**. A weak
pointer creates variance: the needed material exists but the agent never reaches it.
A reference with no branch-specific reason to exist is probably sediment.

**Done when:** every supporting file has a named consumer and a trigger condition;
every body section earns its always-loaded cost.

## 4. Write the entrypoint

Use minimal valid frontmatter for the target runtime. At minimum, provide:

```yaml
---
name: lowercase-kebab-name
description: What the skill does and the concrete situations that should trigger it.
---
```

Make the description a strong context pointer. Put activation conditions in it,
not only in the body. Include distinct branches, not a thesaurus of one trigger.
Keep it specific enough to avoid both under-triggering and unrelated activation.

Write the body as an ordered procedure. Prefer imperative actions and explain why a
non-obvious step matters. Give each phase a completion criterion that distinguishes
done from not-done and demands the evidence needed to continue.

Include only the sections the skill needs:

- when to use and when not to use;
- invocation/argument dispatch when flags or modes exist;
- ordered workflow and branch points;
- safety, ownership, and failure boundaries;
- output contract;
- verification and known limitations;
- pointers to branch-specific resources.

Use a compact leading word for a repeated concept when it genuinely improves recall
(`AUDIT`, `BOUND`, `VERIFY`, or a domain term). Define it once. Do not coin jargon
just to make a short skill look like a framework.

**Done when:** a new agent can follow the body without guessing the order, branch,
artifact, or evidence required.

## 5. Probe behavior before polishing

Create a small evaluation set appropriate to the skill:

- 2-3 realistic positive prompts;
- at least 1 nearby negative prompt that should not activate it;
- 1 adversarial or edge prompt targeting its likely failure mode;
- input fixtures only when the skill actually consumes files or data.

For objective tasks, define assertions before judging outputs. For subjective tasks,
define a human review rubric instead of fake precision. Compare a new skill with a
baseline: no skill for a new capability, or the previous version for a revision.
Hold out at least one prompt when the evaluation is large enough to overfit.

Check the process, not only the final answer:

- Did the skill activate when it should and stay quiet when it should not?
- Did it follow the ordered phases?
- Did it produce the required artifact or report?
- Did it preserve exact technical content and user constraints?
- Did it stop at owner-controlled or unsafe boundaries?
- Did it verify the real output boundary?

Record failures with the prompt, observed behavior, expected behavior, and the
smallest generalized change that should prevent recurrence. Do not patch around one
fixture with a growing list of brittle prohibitions.

**Done when:** each known failure mode has either passing evidence or an explicit
`BLOCKED`/`UNCLEAR` result.

## 6. Revise with deletion pressure

Improve the rule that explains the failure, not merely the example that exposed it.
Prefer this order:

1. sharpen a weak trigger or completion criterion;
2. remove a no-op or stale restatement;
3. move branch-only material behind a precise pointer;
4. add one general rule or reusable script when repeated work proves it is needed;
5. add a narrow guardrail only when a positive instruction cannot express the safety
   boundary.

Read the execution trace when available. If the skill makes agents waste time,
repeat context, or inspect irrelevant files, remove or relocate the instruction that
caused the detour. Shorter is not automatically better; every deletion must retain
capability, safety, and evidence.

Re-run the original prompts and at least one unseen prompt after a meaningful change.
A skill is improved only when the failure is reduced without creating a new boundary
failure.

**Done when:** the revised skill passes the original regression set and does not
merely memorize its wording.

## 7. Package and verify

Before calling the skill complete, inspect the final package:

- entrypoint exists at the repository's documented path;
- frontmatter parses and the name matches the directory;
- name is lowercase kebab case and description is concrete;
- every relative pointer resolves to a real file;
- no reference points to a local home path, private vault, credential, token, or
  machine-specific service unless the skill explicitly declares that dependency;
- scripts are deterministic, executable, and safe to run—or are omitted;
- examples and fixtures do not contain secrets or invented claims presented as facts;
- instructions do not rely on one vendor when portability is promised;
- no duplicate rule has drifted across body, references, and README;
- the documented verification actually ran.

If the target runtime has a validator, use it. Otherwise perform a structural check
and a behavioral smoke test. Report unavailable checks as unavailable; never turn a
syntax pass into proof that the workflow works.

## Output contract

Return a concise closeout containing:

```text
Skill: <name and path>
Mode: CREATE | REVISE | EVALUATE | PACKAGE
Brief: <capability and trigger boundary>
Files: <created, changed, removed>
Evaluation: <prompts, baseline, result, or why qualitative review was used>
Verification: <checks actually run>
Limitations: <BLOCKED, UNCLEAR, dependency, or owner-controlled items>
```

Do not claim a skill is portable, published, triggered reliably, or behaviorally
verified without the corresponding evidence.

## Failure patterns to catch

- **Prompt dump:** long advice with no order, branch, artifact, or done signal.
- **Weak pointer:** the skill exists but its description does not name the situations
  that need it.
- **Reference hiding:** a required rule is externalized without a precise read
  condition.
- **Checklist theatre:** many checks are listed but no evidence is produced.
- **Overfit patch:** a special case fixes one eval while making the skill brittle.
- **No-op sediment:** prose restates defaults, config, or nearby documentation.
- **Compression harm:** terseness changes code, exact errors, numbers, safety warnings,
  or meaning. Preserve technical substance; shorten ceremony only.
- **Generic output:** the workflow ignores the actual project or input and produces a
  reusable-looking template instead of a specific result.
- **Premature completion:** a phase says “reviewed” or “understood” without an
  observable bound.

## Further reading

Read `references/inspiration.md` when reviewing the design rationale or comparing
patterns from public skills. It records principles, not copied source.
