---
name: unslop-ui
description: Audit AI-like UI patterns without breaking design systems.
---

# Unslop UI

Use this skill when a website, app screen, component, prototype, or frontend
implementation feels generic, template-like, over-decorated, or disconnected from
its product. The target is a specific, usable interface—not a style that merely
looks less machine-generated.

The operating loop is **AUDIT -> BOUND -> CHANGE -> VERIFY**. Run the audit before
editing. Preserve the host design system, product behavior, and accessibility.

## When to use

Use it for:

- generated or vibe-coded frontend review;
- visual convergence, generic copy, or repetitive component composition;
- a request to make a UI feel naturally designed while retaining its brand;
- a polished screenshot that may hide missing states or broken interaction.

Keep a normal design-system review when the user has not asked for anti-slop work.
This skill does not determine authorship, hide AI use, invent product content, or
replace documented fonts, colors, tokens, components, routes, or permissions.

## Procedure

### 1. Bind the real surface

Identify the route/component, user task, source files, local instructions, run/build
commands, and supported viewports. Inspect the rendered UI when available. Record
unrelated dirty work before editing.

Inventory the existing contract: fonts and type scale, semantic colors, spacing and
breakpoints, radii/elevation, icon and image rules, components, interaction states,
content terminology, and accessibility behavior.

**Done when:** each proposed change has an observed problem, a source or render
location, and a stated preservation boundary.

### 2. Run the audit gate

Read `references/audit-report-template.md` and produce its `AUDIT GATE` before
suggesting or applying changes. Read `references/anti-slop-checklist.md` for the
numbered catalog.

The gate must contain a status, evidence, applicable checklist IDs, and the smallest
safe action for each area:

1. surface and hierarchy;
2. eyebrows, labels, badges, subtitles, and supporting text;
3. copy and content truth;
4. decoration and visual convergence;
5. typography and design-system drift;
6. states, interaction, responsive behavior, and accessibility.

Use `FLAGGED`, `NOT FLAGGED`, `N/A`, or `BLOCKED`. Evidence can be a selector, exact
text, token, source location, screenshot observation, test result, console result,
or network result. No evidence is `BLOCKED`, never `NOT FLAGGED`.

**Done when:** every applicable checklist ID has an evidence-backed finding. A slop
score or short summary never replaces the gate.

### 3. Perform the auxiliary-text pass

For every heading-bearing section, inspect both source and rendered output. Search
markup, props, CMS fields, and selectors for `label`, `eyebrow`, `kicker`, `overline`,
`badge`, `subtitle`, `subheading`, `description`, `supportingText`, and local names.
Record the exact text, selector/component, heading, following body, visual treatment,
and sibling repetition.

Classify each item:

- **MEANINGFUL:** adds category, date, location, status, mode, scope, workflow
  state, instruction, constraint, or other new information;
- **REDUNDANT:** repeats the heading or body;
- **GENERIC:** makes an unsupported claim such as “Build better” or “Everything you
  need”;
- **DECORATIVE:** fills a template slot or adds visual polish without meaning;
- **UNCLEAR:** cannot be classified from the available evidence.

Flag repeated `eyebrow -> heading -> subtext` scaffolding across unrelated sections,
repeated supporting copy, meaningless badges, tiny or low-contrast labels, and
auxiliary text that fails to wrap or remain accessible on narrow screens. Preserve
meaningful metadata even when its decorative styling changes.

**Done when:** the report contains one row per auxiliary-text instance, or a counted
inventory with exact selectors and text. “There are some eyebrows” is incomplete.

### 4. Identify clusters and product specificity

Use the checklist as a diagnostic catalog, not an automatic rejection list. Look for
clusters such as repeated feature-card grids, centered hero stacks, icon toppers,
uneared gradients/glows/glass, generic claims, identical spacing, decorative motion,
missing states, and mobile/keyboard failures.

Ask what real data, workflow, decision, relationship, or content shape should determine
the composition. A card, gradient, dark theme, serif heading, or rounded button is
not a finding by itself.

**Done when:** each flagged cluster explains what task or product relationship it
obscures and why the evidence is stronger than a style preference.

### 5. Make the smallest bounded change

Prioritize broken tasks, lost data, missing states, accessibility, mobile overflow,
weak hierarchy, generic copy, and only then decorative polish. Use existing tokens
and primitives. Safe local changes include flattening unearned containers, varying
composition according to content, removing ornamental glow, tightening copy, and
rebalancing hierarchy.

Do not add novelty, random asymmetry, fake content, new dependencies, or a second
design system. Do not remove a meaningful eyebrow, status, date, or instruction only
because AI interfaces often overuse the pattern.

**Done when:** every changed line maps to a finding in the audit gate and no preserved
contract was changed without explicit authorization.

### 6. Verify at the real boundary

Run the repository's own lint, type, test, build, and browser checks when available.
Inspect the affected states at wide and narrow viewports, zoom, keyboard focus,
touch, reduced motion, loading, empty, error, permission, and success states.
Check console/network failures, overflow, contrast, accessible names, heading order,
form errors, layout shift, and the relationship between actions and results.

If a check cannot run, report the exact blocker. A screenshot does not prove behavior.

**Done when:** the changed route has passed the relevant checks, the rendered states
were inspected, and every remaining limitation is named.

## Output contract

Use `references/audit-report-template.md` for the final report. It must include:

- route/component and evidence boundary;
- the six-row audit gate;
- the auxiliary-text inventory;
- applicable checklist IDs and exact findings;
- preserved design-system contracts;
- changes and rationale;
- checks actually run and their results;
- `BLOCKED` or `UNCLEAR` items.

Do not report “unslopped,” “humanized,” or “no issues” when an applicable area is
unverified. This is a UI quality procedure, not an authorship detector.

## Supporting files

- `references/audit-report-template.md`: required evidence and final response shape.
- `references/anti-slop-checklist.md`: 100-item diagnostic catalog.
- `references/sources.md`: accessibility, responsive, usability, and design sources.

## Pitfalls

- **Anti-slop slop:** replacing one generic template with another.
- **Screenshot fallacy:** treating visual polish as proof of behavior.
- **Design-system drift:** changing fonts, brand colors, or tokens because they are
  associated with AI aesthetics.
- **Checklist theatre:** listing findings without exact evidence or changing them
  without verification.
- **Content invention:** adding metrics, testimonials, customers, capabilities, or
  explanatory copy not supported by the product.
- **Accessibility regression:** hiding content, removing focus, reducing contrast, or
  relying on hover/animation to explain the interface.
