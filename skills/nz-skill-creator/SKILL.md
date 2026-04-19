---
name: nz-skill-creator
description: Create or update skills inside the NZ Life Skills repository while keeping package docs, manifests, and bundle-level agent indexes in sync. Use when Codex needs to add a new repository skill, update an existing skill's package metadata, register a skill in docs/skills.json and docs/bundles.json, refresh docs/.well-known/agent-skills/*, or keep README and docs pages aligned with the repository's bundle structure. Triggers include requests like "add a new skill to this repo", "update all affected indexes and manifests", "register this skill in NZ-life-skills", or "use the add-skill-template workflow".
metadata:
  author: Pengqian Han
  package: nz-life-skills
  bundle: meta
  geography: nz
  audience:
    - maintainers
    - agent-integrators
  policy_sensitive: false
  official_sources_required: false
---

# NZ Skill Creator

## Overview

Use this skill to create repo-native skills for `NZ-life-skills` without leaving package docs or manifests stale. It combines the generic `$skill-creator` workflow with this repository's template, bundle model, and registration scripts.

## Workflow

1. Read [../../docs/add-skill-template.md](../../docs/add-skill-template.md).
2. Read [references/repo-playbook.md](references/repo-playbook.md).
3. If the active environment exposes `$skill-creator`, follow it for scaffolding and validation. Otherwise, mirror its workflow directly.
4. Create or update the skill folder under `skills/<name>/`.
5. Ensure the skill includes:
   - `SKILL.md`
   - `agents/openai.yaml`
   - `references/current-guidance.md` unless a better reference filename is justified
6. Register the skill in repository manifests with:
   - `scripts/register_skill.py`
7. Run:
   - `python3 scripts/register_skill.py ...`
   - the `quick_validate.py` validator from the active `$skill-creator` installation, if available
8. Review the rendered docs and only make manual follow-up edits when localization or package positioning needs extra nuance.

## What This Skill Automates

Use the bundled script to upsert and sync:

- `docs/skills.json`
- `docs/bundles.json`
- `docs/.well-known/agent-skills/index.json`
- `docs/.well-known/agent-skills/<bundle>.json`
- `README.md`
- `docs/index.md`
- `docs/package-structure.md`
- `docs/skills-index.md`
- `docs/for-agents.md`

Treat `README.zh-CN.md` as a manual follow-up unless the requested change is trivial enough to patch safely in the same run.

## Command Pattern

Run the registration step from the repository root:

```bash
python3 skills/nz-skill-creator/scripts/register_skill.py \
  --repo-root . \
  --name <skill-name> \
  --bundle <bundle-slug> \
  --geography <nz|global|mixed> \
  --audience <audience> \
  --policy-sensitive <true|false> \
  --official-sources-required <true|false> \
  --description "<one-sentence skill description>"
```

If the bundle is new, also pass:

```bash
  --bundle-title "<human title>" \
  --bundle-description "<bundle description>"
```

## Answering Rules

- Prefer existing bundles unless the new skill clearly sits outside the current package model.
- Keep the new skill's frontmatter and `docs/skills.json` aligned.
- Treat `docs/skills.json` and `docs/bundles.json` as the machine-readable source used to render package docs.
- If a reference filename differs from `current-guidance.md`, pass it explicitly to the script and verify that the local path and GitHub URL both match.
- When the change affects package positioning, update `README.zh-CN.md` manually after the script run.

## References

- Repository template: [../../docs/add-skill-template.md](../../docs/add-skill-template.md)
- Repo playbook: [references/repo-playbook.md](references/repo-playbook.md)
- Registration script: [scripts/register_skill.py](scripts/register_skill.py)
