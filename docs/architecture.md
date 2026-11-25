# UI library architecture

## Responsibility
Reusable, presentational Angular components for Pulse and future apps (status badge, uptime chart, pipeline timeline, CVE card, layout shell). Published as `@marcelstypa/pulse-ui` (ADR 0004).

## Rules
- No HTTP calls, no auth, no tenant data: inputs in, events out
- Theming through CSS variables (design tokens) so tenants can be re-branded
- Public API only through `public-api.ts`; internals are not exported
- Semantic versioning through conventional commits and `release-please`
