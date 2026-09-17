# Unslop UI adversarial fixture

Use this fixture to test whether an agent actually performs the mandatory audit gate
instead of returning a generic design summary. It is intentionally small and
contains both bad and meaningful auxiliary text.

```html
<section class="feature-section">
  <p class="eyebrow">Build better</p>
  <h2>Automate your work</h2>
  <p class="subtext">Everything you need to move faster and achieve more.</p>
</section>
<section class="feature-section">
  <p class="eyebrow">Powerful tools</p>
  <h2>Organize your work</h2>
  <p class="subtext">Everything you need to move faster and achieve more.</p>
</section>
<section class="feature-section">
  <p class="eyebrow">Designed for you</p>
  <h2>Understand your work</h2>
  <p class="subtext">Everything you need to move faster and achieve more.</p>
</section>
<section class="status-section">
  <p class="eyebrow">Updated 17 September 2026</p>
  <h2>Release notes</h2>
  <p class="subtext">Changes since the previous release.</p>
</section>
```

## Required findings

A compliant audit must identify at least:

- **24:** the eyebrow/overline pattern is repeated above every heading, and the
  first three labels are generic rather than contextual;
- **29:** the first three labels are decorative/context-free, not meaningful status
  or orientation;
- **60:** the same supporting subtext is repeated across the first three sections;
- **62:** “Build better,” “Powerful tools,” “Designed for you,” and “Everything you
  need…” are unsupported generic claims;
- **recomposition finding:** the same `eyebrow → heading → subtext` scaffold is
  applied to unrelated feature sections;
- **preservation finding:** “Updated 17 September 2026” is meaningful metadata and
  must not be removed merely because it is an eyebrow;
- **verification finding:** the agent must state whether the source and rendered
  narrow/mobile behavior were actually checked.

The agent must quote or reference the exact text and selector/component for each
finding. “The page has some repetitive labels” is insufficient evidence.

## Expected classification table

| Text | Selector | Classification | Expected treatment |
| --- | --- | --- | --- |
| `Build better` | `.feature-section:nth-of-type(1) .eyebrow` | `GENERIC` | rewrite/remove |
| `Powerful tools` | `.feature-section:nth-of-type(2) .eyebrow` | `GENERIC` | rewrite/remove |
| `Designed for you` | `.feature-section:nth-of-type(3) .eyebrow` | `GENERIC` | rewrite/remove |
| `Everything you need…` | first three `.subtext` nodes | `REDUNDANT` / `GENERIC` | consolidate/rewrite |
| `Updated 17 September 2026` | `.status-section .eyebrow` | `MEANINGFUL` | preserve |
| `Changes since the previous release.` | `.status-section .subtext` | `MEANINGFUL` | preserve |

A test passes only when the required findings are explicit and the meaningful status
metadata is preserved. A pass based only on detecting gradients, cards, or fonts
fails this fixture.
