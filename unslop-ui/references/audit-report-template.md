# Unslop UI audit report

Use this template before editing and again for the final handoff. Replace every
placeholder. Do not omit a row; use `N/A` or `BLOCKED` with evidence.

## Evidence boundary

- Route/component:
- Source files inspected:
- Rendered states/viewports inspected:
- Checks available but not run:

## AUDIT GATE

| Area | Status | Exact evidence | Checklist IDs | Smallest safe action |
| --- | --- | --- | --- | --- |
| Surface and hierarchy | FLAGGED / NOT FLAGGED / N/A / BLOCKED |  |  |  |
| Eyebrows, labels, badges, subtitles, supporting text | FLAGGED / NOT FLAGGED / N/A / BLOCKED |  |  |  |
| Copy and content truth | FLAGGED / NOT FLAGGED / N/A / BLOCKED |  |  |  |
| Decoration and visual convergence | FLAGGED / NOT FLAGGED / N/A / BLOCKED |  |  |  |
| Typography and design-system drift | FLAGGED / NOT FLAGGED / N/A / BLOCKED |  |  |  |
| States, interaction, responsive behavior, accessibility | FLAGGED / NOT FLAGGED / N/A / BLOCKED |  |  |  |

`NOT FLAGGED` requires evidence. `BLOCKED` is the correct status when source,
rendered behavior, or a required check was unavailable.

## Auxiliary-text inventory

| Selector/component | Exact auxiliary text | Heading/body | Classification | Checklist ID | Decision |
| --- | --- | --- | --- | --- | --- |
|  |  |  | MEANINGFUL / REDUNDANT / GENERIC / DECORATIVE / UNCLEAR |  |  |

Inventory every eyebrow, kicker, overline, section label, badge, subtitle,
description, and supporting-text instance. A counted inventory may group identical
siblings only when it gives the count, selector pattern, and exact text.

## Findings

For each applicable checklist ID:

- **ID and pattern:**
- **Evidence:**
- **Why it harms this task/product:**
- **Preserved contract:**
- **Smallest change:**
- **Verification:**

## Handoff

- Preserved design-system contracts:
- Changes made:
- Checks actually run and results:
- Remaining BLOCKED or UNCLEAR items:
- Scope deliberately not changed:
