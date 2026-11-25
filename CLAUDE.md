# CLAUDE.md: pulse-ui

Shared Angular component library with Storybook.
Architecture and decisions: the `pulse` overview repo (README, docs/adr).

## Stack
- Angular library (ng-packagr), Storybook
- Published as @marcelstypa/pulse-ui to GitHub Packages
- Design tokens as CSS variables

## Commands
- `npm test`, `npm run lint`, `npm run build`, `npm run storybook`

## Rules
- Public repo: never write secrets, tokens or real credentials; only `*.example` files
- Conventional Commits (`type(scope): subject`), one logical change per commit, never force-push `main`
- Tests and lint must pass before a commit is proposed
- Every API, DB or auth decision that deviates from an ADR needs a new ADR in `pulse/docs/adr`
- No API calls or tenant data in this library; components are presentational
- Every component has a Storybook story and a test
- Breaking changes need a conventional commit with `!` or BREAKING CHANGE footer

## Required reading (before any change)
Read these first; they are normative. On conflict with a request: stop and ask.
- `docs/README.md` (index)
- `docs/architecture.md`
- `docs/coding-standards.md`
- `docs/testing.md`
- `docs/git-and-commits.md`, `docs/security.md`, `docs/ai-workflow.md`
- ADRs: `pulse/docs/adr/`

## Non-negotiables
- Create commits or push only when the user asks; end AI-assisted commits with the Co-Authored-By trailer
- Report real command output; never claim tests pass without running them
- Do not guess versions, config keys or APIs; verify or say unknown
- Update docs in the same change when behaviour or conventions change
