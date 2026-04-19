# For Agents

This repository is a bundled New Zealand newcomer onboarding package for Codex and Claude Code.

## Repository Intent

Use this repository when the user needs help with real-life New Zealand setup tasks, especially for international students and newcomers.

Treat the repository as one vertical package with small internal bundles, not as unrelated one-off skills.

Typical bundles include:

- `Pre-Departure`
- `Arrival Setup`
- `Living Basics`
- `Meta`
- `Extended`

## Repository Layout

```text
skills/
  <skill-name>/
    SKILL.md
    agents/openai.yaml
    references/
assets/
scripts/
```

## Discovery Endpoints

If this repository is published via GitHub Pages, agents should also check:

- `robots.txt`
- `sitemap.xml`
- `bundles.json`
- `skills.json`
- `.well-known/agent-skills/index.json`

## How To Read This Repo

1. Start with [README.md](../README.md) or [README.zh-CN.md](../README.zh-CN.md) for project-level context.
2. Read [package-structure.md](./package-structure.md) for bundle-level intent.
3. Go to `skills/<skill-name>/SKILL.md` for the skill workflow.
4. Read the skill's `references/` files before answering policy-sensitive questions.
5. Treat any operational detail as potentially time-sensitive unless the skill clearly marks it as stable.

## Official Source Rule

Every skill in this repository should be grounded in official sources.

- Look for an `Official Sources` section in the skill's reference files.
- Prefer government, university, bank, carrier, transport authority, or provider sites.
- Do not rely on blogs, forums, or community posts when an official source exists.

## Policy Freshness Rule

Many skills in this repository are policy-sensitive.

If the user asks about:

- current rules
- latest fees
- eligibility
- document requirements
- official application steps

then verify the current official sources on the web before answering.

If the official rules differ from the stored reference, update the skill reference before finishing the task.

## Expected Answer Style

- State eligibility or scope first.
- Separate stable explanation from current operational detail.
- Call out uncertainty directly when the general rule and the current portal flow do not match.
- Use the official source as the authority, not repository memory.

## Installation Pointers

Codex users generally install from:

- `~/.codex/skills`

Claude Code users generally install from:

- `~/.claude/skills`
- or clone the repo as a plugin-style collection

Helper scripts live in `scripts/`.
