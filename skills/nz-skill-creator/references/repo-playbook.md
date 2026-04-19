# NZ Skill Creator Playbook

This repository uses a two-layer model when adding skills:

1. Create or update the skill itself.
2. Register the skill across the package so humans and agents see a consistent structure.

## Required Inputs

Mirror the fields in [../../docs/add-skill-template.md](../../docs/add-skill-template.md):

- `name`
- `bundle`
- `geography`
- `audience`
- `policy_sensitive`
- `official_sources_required`
- `goal`
- `scope`
- `preferred source order`

## Repository Conventions

- Put every skill under `skills/<name>/`.
- Prefer `references/current-guidance.md` unless another filename is clearly better.
- Keep `SKILL.md` concise; move detailed repository or policy material into `references/`.
- Include `metadata` in the skill frontmatter because this repository uses it for package registration.

## Existing Bundles

- `nz-pre-departure`
- `nz-arrival-setup`
- `nz-living-basics`
- `meta`
- `extended`

## Source Of Truth

- `docs/skills.json`: skill registry
- `docs/bundles.json`: bundle registry

The repository-level English docs are rendered from these manifests by `scripts/register_skill.py`.

## Manual Follow-Up

After running the registration script, review:

- `README.zh-CN.md`
- any custom bundle phrasing if a new bundle changes package positioning
- any skill-specific examples or references that should be richer than the default scaffold
