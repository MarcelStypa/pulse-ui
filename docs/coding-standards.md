# UI library standards

Claude MUST follow these.

- Angular current stable; standalone components, `ChangeDetectionStrategy.OnPush`, signals for state, new control flow syntax
- Typed inputs and outputs (`input()`, `output()`); no `any`
- Selector prefix `pulse-`; one component per folder with `.ts`, `.html`, `.scss`, `.spec.ts`, `.stories.ts`
- Accessibility: semantic HTML, keyboard support, ARIA where needed, WCAG AA contrast
- Styling only with design tokens; no hard-coded colors or spacing
- Charts must have a text alternative or data table
- Breaking API changes are marked in the commit (`!` or `BREAKING CHANGE:`)
