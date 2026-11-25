# Git and commits

> Canonical source: `pulse/docs/git-and-commits.md`. Copies in other repos must stay identical.

Claude MUST follow this when proposing or creating commits.

## Commit messages
- Format: `type(scope): subject` ([Conventional Commits](https://www.conventionalcommits.org/))
- Types: `feat`, `fix`, `docs`, `refactor`, `test`, `build`, `ci`, `chore`, `perf`
- Subject: imperative, lower-case, max 72 chars, no trailing period
- Body explains why, not what. Breaking changes use `!` or a `BREAKING CHANGE:` footer
- AI-assisted commits end with the `Co-Authored-By` trailer for the assistant (see `ai-workflow.md`)

## Commit hygiene
- One logical change per commit; code, tests and docs for that change travel together
- No "wip", "fix stuff", "update" commits on `main`; squash or rewrite them on the branch first
- Never commit: `.env*`, `*.tfvars`, `*.tfstate`, keys, tokens, generated build output
- Never force-push `main`; never skip hooks (`--no-verify`) to get past a failing check

## Branches and PRs
- `main` is protected: PR only, required checks green, squash merge
- Branch names: `feat/…`, `fix/…`, `docs/…`, `chore/…`
- PR description: what changed, why, how it was verified, and an AI-assistance note if relevant

## Claude behaviour
- Create commits or push only when the user explicitly asks
- Show the proposed message and staged file list before committing
- If a check fails, report the real output; do not hide or "fix" a failure by weakening the check
