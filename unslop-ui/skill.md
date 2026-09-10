---
name: unslop-ui
description: Humanize UI without breaking its design system.
version: 0.1.0
author: Sujal Choudhari, Hermes Agent
license: MIT
platforms: [linux, macos, windows]
metadata:
  tags: [ui, ux, frontend, design-systems, accessibility, anti-slop]
  references:
    - references/anti-slop-checklist.md
    - references/sources.md
---

# Unslop UI

Use this skill when an agent must review or improve a website, app screen,
component, prototype, or frontend implementation that feels generic, overly
polished, template-like, or AI-generated.

The goal is not to make a UI look eccentric. The goal is to make it feel
specific, intentional, usable, and naturally made by people who understand the
product. Preserve the host project's existing design system and product
identity. You may change gradients, shadows, borders, decorative composition,
copy structure, spacing relationships, motion, and layout when the evidence says
those changes improve the interface.

This is not a detector-evasion guarantee. It does not authorize hiding AI use,
copying another product, inventing product content, removing required
accessibility, or replacing a design system because a different style is more
fashionable.

## When to use

Load this skill when asked to:

- remove AI-generated or “AI slop” patterns from a UI;
- make a generated or vibe-coded frontend look naturally designed;
- review a landing page, dashboard, settings screen, portal, or component for
  generic visual convergence;
- preserve an existing design system while improving composition and product
  specificity;
- turn a polished screenshot or prototype into a reliable working interface.

Do not use this skill to:

- replace a repository's documented fonts, color tokens, spacing scale, icon set,
  component primitives, or brand rules without explicit approval;
- make arbitrary visual changes without inspecting the product, content, and
  existing implementation;
- sacrifice keyboard access, contrast, reduced-motion support, responsive
  behavior, or semantic HTML for visual novelty;
- manufacture testimonials, metrics, illustrations, product capabilities, or
  user stories;
- claim that a page was or was not made by AI based only on visual appearance.

## Preservation contract

Before changing anything, establish the host UI's design-system contract.
Preserve, unless the user explicitly authorizes a change:

- font families, font loading, type tokens, and type scale;
- brand colors, semantic color roles, and theme variables;
- spacing units, breakpoints, grid conventions, and density choices;
- border-radius tokens, elevation conventions, and component primitives;
- icon library, icon stroke/fill rules, and image treatment;
- content hierarchy, product terminology, routes, data contracts, and permissions;
- interaction behavior, keyboard operation, reduced-motion behavior, and focus;
- existing visual language across sibling screens.

A gradient is not a design system. A glow can be removed or rewritten when it is
ornamental, but a semantic color token must not be replaced merely because it is
associated with AI aesthetics.

## Inputs and evidence

Inspect the real artifact before editing. Use the repository's local instructions
and the actual rendered UI when available.

Collect:

1. **Product intent:** primary user, task, action, content model, and important
   states.
2. **Design-system evidence:** theme files, tokens, global CSS, component
   library, typography setup, asset rules, and sibling screens.
3. **Implementation evidence:** routes, component boundaries, data loading,
   error handling, loading states, semantic elements, and tests.
4. **Visual evidence:** desktop, narrow mobile, keyboard focus, empty, loading,
   error, permission, and success states.
5. **Risk evidence:** contrast, overflow, layout shift, clipped menus, broken
   image states, console errors, and animation behavior.

If a screenshot conflicts with source code, treat source code and live behavior as
stronger evidence for implementation claims. A screenshot can reveal a visual
problem but cannot prove that an interaction works.

## Procedure

### 1. Establish the baseline

Read the local instructions first. Identify the canonical app, route, entry point,
and how it is run. Record the working-tree state before editing and preserve
unrelated dirty work.

Build a short baseline table:

| Area | Existing contract | Observed problem | Evidence | Safe change |
| --- | --- | --- | --- | --- |
| Typography | Existing font/token | e.g. weak hierarchy | source + render | size/weight/measure only |
| Color | Existing semantic roles | e.g. decorative glow | source + render | background/effect only |
| Layout | Existing breakpoints | e.g. repeated grids | render | composition, not tokens |
| Components | Existing primitives | e.g. nested cards | source + render | flatten composition |
| Interaction | Existing behavior | e.g. unclear result | live behavior | state/feedback |

Completion check: every proposed visual change maps to an observed problem and
has an explicit preservation boundary.

### 2. Audit for convergence, not individual style choices

Review the page against `references/anti-slop-checklist.md`. Look for clusters:

- centered hero + oversized headline + two pill CTAs;
- Inter or another default sans-serif everywhere without product rationale;
- purple/blue gradient, glow, glass panel, neon accent, and dark background as
  the entire identity;
- identical three-card or four-card grids repeated for unrelated content;
- icon tile above every heading;
- generic claims, fake metrics, vague testimonials, or repeated copy;
- tiny labels, low-contrast supporting text, excessive rounded containers, and
  monotonous spacing;
- decorative motion, pulsing dots, blinking cursors, marquee text, or layout
  animation without task value;
- polished default state with missing loading, empty, error, permission, or
  success states;
- behavior that fails on mobile, keyboard, zoom, reduced motion, or touch.

Do not “fix” a pattern merely because it appears on the list. Ask whether it is
specific to the product, improves a user task, and is consistent with the local
design system.

Completion check: the audit names the smallest set of high-confidence problems,
not a list of every possible preference disagreement.

### 3. Recover product-specific hierarchy

Replace generic composition with information architecture derived from the real
content and user task:

- make the primary task visually and semantically obvious;
- promote real product evidence instead of invented marketing claims;
- give each section one job;
- use a card only when the content needs grouping, comparison, scanning, or an
  independent action;
- flatten nested cards when borders and shadows obscure the hierarchy;
- vary section composition when content relationships differ;
- keep one strong focal point instead of several competing effects;
- use whitespace to establish grouping, not to create empty “premium” theatre;
- let real data determine whether the layout is a list, table, timeline, form,
  comparison, or detail view.

A design can remain minimal, dark, branded, and highly polished. “Human” means
that the visual choices follow the product rather than a generic prompt.

Completion check: a reviewer can explain the hierarchy without mentioning the
implementation framework or visual trend.

### 4. Improve visual craft inside the existing system

Use the host tokens and primitives. Safe changes commonly include:

- remove or localize unearned gradients, halos, glass, glow, and shadow stacks;
- replace decorative effects with real grouping, contrast, or content emphasis;
- correct spacing relationships while staying on the existing scale;
- create more deliberate asymmetry from real content rather than random offsets;
- vary card composition without introducing new component primitives;
- improve text measure, hierarchy, and wrapping without changing the font family;
- replace placeholder-style imagery with existing approved assets or a deliberate
  empty state;
- make borders, radii, and elevation carry semantic meaning rather than appear on
  every surface;
- use motion only for feedback, continuity, status, or orientation;
- respect `prefers-reduced-motion` and avoid motion that changes layout.

Do not add visual noise to prove that a human worked on the page. Restraint is a
valid design decision.

Completion check: every changed token or style declaration is either already
part of the system or is a local composition rule justified in the review.

### 5. Repair copy and content without inventing facts

Use real product language. Remove:

- vague “unlock,” “empower,” “transform,” and “seamless” claims;
- repeated descriptions of the same action;
- fake metrics, testimonials, logos, customer names, or implied endorsements;
- headings that merely restate the paragraph below;
- decorative labels that do not help navigation or comprehension.

Keep useful specificity: real dates, counts, locations, permissions, status,
limitations, sources, and next actions. If content is unavailable, use a clearly
labelled empty or placeholder state rather than fabricating it.

Completion check: every changed sentence is supported by existing content or is
explicitly presented as UI guidance rather than product fact.

### 6. Repair states and interactions

A real interface needs more than its screenshot state. Check and implement, when
relevant:

- loading and skeleton behavior that does not shift the page unexpectedly;
- empty state with a useful next action;
- recoverable error state with a specific explanation;
- permission or authentication state;
- success and completion feedback;
- disabled, pending, selected, expanded, focused, and pressed states;
- destructive-action confirmation, undo, or recovery;
- keyboard traversal and visible focus;
- semantic buttons, links, labels, headings, landmarks, and form associations;
- touch targets and spacing that work on small screens;
- menus, popovers, dialogs, and tooltips that are not clipped or hover-only.

Use the host project's existing interaction patterns before creating a new one.

Completion check: important actions have a visible result and all meaningful
states are reachable without relying on hover or animation.

### 7. Verify responsive and accessibility behavior

Test at the project's supported breakpoints plus a narrow mobile viewport and
browser zoom. Check:

- no horizontal overflow for ordinary content;
- readable text at 200% zoom where applicable;
- no two-dimensional reading scroll for ordinary pages;
- visible focus that is not hidden by sticky UI;
- adequate text and non-text contrast;
- target size and separation for touch controls;
- keyboard-only operation;
- reduced-motion behavior;
- meaningful heading order and accessible names;
- form errors identified in text and associated with the field;
- semantic HTML that survives assistive-technology interpretation.

Use the standards and source ledger in `references/sources.md` as the verification
basis. Do not turn a visual preference into a false accessibility requirement,
and do not treat a passing automated audit as proof of good UX.

Completion check: the UI works at the real interaction boundary, not only in a
static desktop screenshot.

### 8. Run the repository's real checks

Use the project's own commands. Typical checks may include:

- targeted lint and type checks;
- unit and component tests;
- production build;
- browser or end-to-end checks when the repository provides them;
- console-error and network-failure inspection;
- visual comparison at the required viewports.

Do not install a new framework or replace the project's tooling for this pass.
Do not claim success from a screenshot when the build or tests fail. If a check
cannot run, report the exact blocker.

Completion check: the diff is clean, targeted checks pass, and the rendered UI
has been inspected in the states affected by the change.

## Change-priority order

When many problems exist, work in this order:

1. broken task, missing state, or incorrect content;
2. accessibility and keyboard/touch failures;
3. mobile overflow and responsive hierarchy;
4. weak information hierarchy and excessive containers;
5. generic copy and unsupported claims;
6. unearned gradients, glows, glass, shadows, and decorative motion;
7. fine spacing, alignment, and polish.

Do not spend the first pass on gradients while a form loses user input or a
primary action is inaccessible.

## Pitfalls

- **Design-system replacement:** changing fonts or brand colors because they are
  associated with AI is out of scope.
- **Anti-slop slop:** replacing one template with a different “human” template.
- **Novelty theatre:** adding asymmetry, noise, hand-drawn graphics, or random
  imperfection without product meaning.
- **Screenshot fallacy:** treating a static screenshot as proof of behavior.
- **Content invention:** adding believable but unverified customers, numbers,
  testimonials, or anecdotes.
- **Accessibility regression:** removing focus rings, reducing contrast, or
  hiding content to make the screenshot cleaner.
- **Token drift:** adding one-off values when an existing token already serves
  the need.
- **Motion compensation:** using animation to hide missing hierarchy or feedback.
- **Framework drift:** adding dependencies or rewriting architecture for a visual
  review.
- **Scope drift:** redesigning sibling routes that were not part of the request.

## Verification report

Return a concise report with:

- route/component reviewed;
- high-confidence problems found;
- design-system elements preserved;
- changes made and why;
- states and viewports tested;
- commands run and their actual results;
- remaining limitations or blocked checks.

A successful pass makes the UI more specific and usable while leaving the
project's visual identity recognizable. It does not claim that the result is
“human-made” or undetectable.
