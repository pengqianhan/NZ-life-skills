# Contributing

Thanks for contributing to `NZ-life-skills`.

## What To Contribute

Useful contributions include:

- new skills for common New Zealand newcomer tasks
- better official-source coverage
- updates when policies or application flows change
- README and documentation improvements
- installation improvements for Codex or Claude Code

## Contribution Rules

### 1. Prefer official sources

If a skill covers policy, onboarding, or operations, include official sources in the reference files.

Examples:

- government sites
- university sites
- official transport authorities
- bank sites
- telecom provider sites
- healthcare provider or public-health sites

### 2. Treat policy as unstable

Do not hard-code current fees, eligibility, or document requirements without verification.

If you update a policy-sensitive skill:

- verify the current official source
- update the skill reference file
- keep the `As of:` date current

### 3. Keep skills reusable

Each skill should be useful across repeated tasks, not just a one-off answer.

Good skill structure usually includes:

- clear frontmatter
- clear triggering description
- workflow guidance
- references with official sources

### 4. Keep the repo bilingual where it helps

English is the default for broad discoverability.
Chinese content is welcome when it improves usefulness for the target audience.

## Adding A New Skill

If you are adding a new skill, start from the template in [docs/add-skill-template.md](./docs/add-skill-template.md).

Use that template to keep the new skill aligned with the repository's package structure, bundle model, and machine-readable manifests.

Typical steps are:

1. Create a new folder under `skills/`.
2. Add `SKILL.md` with the current frontmatter schema.
3. Add `agents/openai.yaml`.
4. Add `references/` with at least one reference file.
5. Include an `Official Sources` section in the reference file when relevant.
6. Update [docs/skills-index.md](./docs/skills-index.md).
7. Update [docs/skills.json](./docs/skills.json).
8. Update [docs/bundles.json](./docs/bundles.json) if bundle membership changes.
9. Update `docs/.well-known/agent-skills/` if a bundle-level endpoint is affected.
10. Update `README.md` and `README.zh-CN.md` only if the package story materially changes.

## Validating A Skill

Use the validator from the local skill-creator tooling:

```bash
python3 ~/.codex/skills/.system/skill-creator/scripts/quick_validate.py skills/<skill-name>
```

If the skill is policy-sensitive, also manually verify that the listed official links still reflect the current workflow.

## Pull Requests

When opening a PR, describe:

- what changed
- why it changed
- which official sources you used
- whether the change affects a current policy-sensitive workflow
