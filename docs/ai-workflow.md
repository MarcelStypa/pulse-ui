# AI-assisted development

> Canonical source: `pulse/docs/ai-workflow.md`. Copies in other repos must stay identical.

This project is built with an AI coding assistant (Claude Code). That is deliberate
and disclosed. AI makes the work faster; it does not replace engineering judgment,
review or accountability. The rules below apply to humans and to the assistant.

## Principles
1. **Human owns decisions.** Architecture and trade-offs are decided by the maintainer and recorded as ADRs. The assistant proposes options with a recommendation; it does not silently decide.
2. **Review everything.** No AI-generated change is merged unless the maintainer has read it and can explain it.
3. **Verification over trust.** Tests, linters, scanners and the Sonar quality gate decide whether work is done, not the assistant's claim. Failures are reported honestly with the real output.
4. **Small, reviewable changes.** One logical change at a time, with tests and docs in the same commit.
5. **Docs are the contract.** The assistant reads `CLAUDE.md` and `docs/` before working and follows them. If a request conflicts with a doc, it stops and says so; the doc is changed first (ADR), then the code.
6. **No invention.** Library versions, config keys and APIs are verified against official documentation or the code, not guessed. Unknowns are stated as unknowns.
7. **Approval for risky actions.** `terraform apply`, pushing, deleting, force operations, creating cloud resources or anything outward-facing needs explicit approval for that action.
8. **Privacy.** No secrets or personal data in prompts, files or commits.
9. **Attribution.** AI-assisted commits carry a `Co-Authored-By` trailer. The README of each repo states that AI assistance is used.
10. **Keep context current.** When behaviour or conventions change, update `CLAUDE.md` and `docs/` in the same commit.

## Division of work
| Maintainer | Assistant |
|---|---|
| Goals, scope, architecture decisions | Options, trade-offs, a recommendation |
| Review and approval of every change | Drafts code, tests, docs, scripts |
| Final say on merge, deploy and cost | Runs checks and reports results truthfully |

## Definition of done for an AI-assisted change
- [ ] Builds, tests and lint pass locally (real output seen)
- [ ] New behaviour has tests; bug fixes have a regression test
- [ ] Security rules respected (`security.md`), no secrets
- [ ] Docs and ADRs updated where behaviour or decisions changed
- [ ] Diff reviewed by the maintainer
- [ ] Conventional commit message with attribution trailer

## Enforcement
Rules that matter are enforced by automation, not only by documentation:
- Claude Code hooks in `.claude/hooks/` block non-conventional commits, `--no-verify`, force-push and writes to secret-like files
- `.claude/settings.json` denies reading secret files and asks before `terraform apply`, `git push` and `az`
- CI (reusable workflows in `pulse-workflows`) runs tests, the Sonar quality gate, dependency and image scans and gitleaks
- The pull request template carries the AI-assistance and new-dependency checklist
- Hook scripts are shared files: canonical copy in `pulse/.claude/hooks/`, keep copies identical
