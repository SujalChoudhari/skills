# AI-looking UI diagnostic checklist

Use this as a diagnostic catalog, not a score that determines authorship. A
single item may be intentional. The strongest signal is a cluster of generic
patterns that is unrelated to the product's content, task, or design system.

## AI-signature patterns

1. Purple-to-blue gradients used across the whole identity.
2. Glass panels, neon borders, and glowing orbs used without a layering need.
3. Buttons bouncing, icons wiggling, and badges floating at the same time.
4. A colored stripe placed on every rounded card.
5. Multiple nested cards around the same content.
6. The same hero, metrics, feature grid, and CTA structure repeated across pages.
7. Inter used everywhere without a product-specific typographic reason.
8. Oversized icon tiles dominating the content they introduce.
9. Poor contrast hidden beneath a polished visual treatment.
10. Several lines of copy explaining the same field, feature, or action.
11. Large settings forms squeezed into scrolling modals instead of a page.

## Design-system drift

12. A font appears outside the documented type system.
13. One-off colors appear outside the documented palette.
14. Random corner radii appear outside the documented scale.
15. Font sizes are chosen ad hoc rather than from a deliberate type scale.

## Decorative visual details

16. Decorative grid lines used without a canvas or measurement task.
17. A thick border accent added to an already rounded element.
18. Glassmorphism applied to nearly every surface.
19. A colored side-tab border used without alert or status meaning.
20. A thin border and a large soft shadow defining the same card.
21. Repeating gradient stripes filling otherwise empty space.
22. Extremely large border radii on ordinary cards.
23. Rough, hastily drawn SVG mascots used as personality substitutes.

## Typography

24. A tiny label placed above every heading.
25. Interface text made too small to scan comfortably.
26. Headings and body copy have almost the same visual weight.
27. A rounded icon tile is stacked above every heading.
28. An italic serif display headline used as a generic premium signal.
29. A badge is placed above the main headline without meaningful status.
30. The hero headline is so large it becomes the main visual object.
31. Letter spacing is compressed until text is cramped.
32. One fashionable font is overused for every purpose.
33. A single font is used for headings, labels, data, and navigation without rationale.
34. Body text is written in all caps.

## Color and contrast

35. A radial-gradient halo is behind every important section.
36. A soft spotlight sits behind content without improving focus or grouping.
37. Purple, electric blue, cyan, and dark navy are used by default as an AI palette.
38. Dark mode relies on glowing accents rather than clear semantic states.
39. Gradient text is used for headings that do not need emphasis.
40. Gray text is placed on a colored background with inadequate contrast.
41. A cream or beige editorial palette is applied without a content or brand reason.

## Layout and spacing

42. Tiny numbered section labels are added to ordinary marketing sections.
43. Cards touch a horizontal scroller edge without an intentional affordance.
44. Text is covered by another element or decorative layer.
45. Opening columns are visually unbalanced without a reason.
46. A heading sits too close to the previous section.
47. A giant metric is presented as the hero without supporting a decision.
48. Every section is an identical three- or four-column card grid.
49. The same spacing gap is used regardless of hierarchy.
50. Cards are nested inside cards inside panels.
51. Paragraphs use excessively long line lengths.
52. Content overflows its container at common viewport sizes.
53. Menus and popovers are clipped by their containers.

## Motion

54. Status indicators pulse even when nothing is changing.
55. A blinking cursor is used decoratively rather than as an input affordance.
56. A marquee auto-scrolls content users need to read.
57. Buttons and cards use bounce or elastic easing without functional meaning.
58. Animations change layout and push surrounding content around.
59. Images move on hover even when movement communicates nothing.

## Copy and language

60. The same sentence is repeated inside one component.
61. Em dashes are overused as a rhythm substitute.
62. Generic claims such as “unlock your potential” appear without evidence.
63. Copy repeatedly manufactures forced contrast: “not just X, but Y.”
64. Ordinary features are called “magic,” “intelligence,” or “the future” without mechanism.

## Imagery

65. Placeholder-style illustrations remain in the finished design.
66. Jagged or awkward image masks create artificial uniqueness.
67. Images are hidden under excessive overlays, gradients, or glass effects.
68. Broken, missing, or obviously placeholder images reach the final page.

## General quality

69. JavaScript errors occur during page load.
70. Content stays hidden if an entrance animation or reveal script fails.
71. Padding is cramped despite large decorative surfaces elsewhere.
72. Body text touches the page edge on small screens.
73. Paragraphs are fully justified without a strong editorial reason.
74. Low-contrast text is used for secondary content.
75. Heading structure skips directly to `h3` without an `h2`.
76. Heading levels are skipped purely for visual sizing.
77. Line height is too tight for comfortable reading.
78. Body text is too small.
79. Wide letter spacing is applied to normal body text.

## Interaction and implementation

80. A `div` or `span` is used as a button instead of semantic controls.
81. Icon-only controls have no accessible name or visible explanation.
82. Keyboard focus is removed or invisible.
83. Status is communicated through color alone.
84. Mobile layout requires two-dimensional scrolling for ordinary content.
85. Touch targets are tiny or too close together.
86. Form errors say only “Something went wrong.”
87. Errors identify neither the affected field nor how to fix it.
88. A failed form submission clears entered data.
89. Loading, empty, error, success, and permission states are missing.
90. Essential content is hidden until JavaScript succeeds.
91. Sticky headers or overlays cover the focused element.
92. The page shifts when fonts, images, or components load.
93. Effects consume main-thread time without improving the task.
94. The DOM is excessively large because every visual wrapper became a component.
95. Navigation changes position or naming between pages.
96. Destructive actions have no confirmation, undo, or recovery path.
97. Hover is required to discover important information on touch devices.
98. Form fields rely on placeholder text instead of persistent labels.
99. The interface has no visible relationship between an action and its result.
100. The page looks polished in a default screenshot but fails keyboard, zoom,
    mobile, or reduced-motion use.

## Review rule

Do not reject a UI because it uses cards, gradients, dark mode, a sans-serif
font, or a centered hero. For each finding, record:

- what the user is trying to do;
- what the current pattern makes harder;
- which existing token or component contract must remain unchanged;
- the smallest change that fixes the problem;
- how the fix will be verified at the real interaction boundary.
