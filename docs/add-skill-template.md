# Add Skill Template

Use this template when asking Codex to add a new skill to this repository.

The goal is to avoid creating an isolated `SKILL.md` without updating the package structure, docs indexes, and machine-readable manifests.

## Recommended Prompt

Copy, fill in, and send this to Codex:

```text
Help me add a new skill to this repository and keep it consistent with the current package structure.

Create or update everything needed, including:
- skills/<name>/SKILL.md
- skills/<name>/references/current-guidance.md (or a better-named reference file if needed)
- docs/skills-index.md
- docs/skills.json
- docs/bundles.json if needed
- docs/.well-known/agent-skills/* if needed
- README.md / README.zh-CN.md if the new skill changes package positioning

New skill details:

name: <skill-name>
bundle: <nz-arrival-setup | nz-living-basics | meta | extended | new-bundle-name>
geography: <nz | global | mixed>
audience:
- <audience-1>
- <audience-2>
policy_sensitive: <true | false>
official_sources_required: <true | false>

Goal:
<one short paragraph explaining what problem this skill solves and for whom>

Scope:
- <what it should cover>
- <what it should cover>
- <what it should not overclaim or do>

Preferred source order:
- <official source type or specific source>
- <official source type or specific source>

If this should become part of a new bundle, update the package docs and agent manifests accordingly.
```

## Minimal Version

If you want a shorter prompt, use this:

```text
Add a new skill to this repo and update all affected indexes and manifests.

name:
bundle:
geography:
audience:
policy_sensitive:
official_sources_required:
goal:
scope:
preferred source order:
```

## Field Guidance

Use these fields consistently:

- `name`: kebab-case skill id, for example `nz-job-search-basics`
- `bundle`: one of the current bundles, unless you intentionally want to create a new one
- `geography`:
  - `nz` for New Zealand-specific skills
  - `global` for reusable skills not tied to New Zealand
  - `mixed` for bundles or skills that span both
- `audience`: use stable machine-readable values when possible, for example:
  - `international-students`
  - `newcomers`
  - `new-migrants`
  - `visitors`
  - `maintainers`
  - `agent-integrators`
  - `travelers`
  - `trip-planners`
- `policy_sensitive`: `true` when rules, pricing, eligibility, or official process details may change
- `official_sources_required`: `true` when the skill should rely on government, provider, university, bank, regulator, or other official sources

## Bundle Guidance

Use the current bundle model unless there is a strong reason to introduce a new one:

- `nz-arrival-setup`: first-week setup tasks
- `nz-living-basics`: day-to-day setup after arrival
- `meta`: package distribution and discoverability support
- `extended`: adjacent skills that extend beyond the core newcomer package

## What Codex Should Usually Update

When adding a new skill, Codex should usually update:

1. the new skill folder under `skills/`
2. the skill frontmatter schema in `SKILL.md`
3. the skill reference file under `references/`
4. [skills-index.md](./skills-index.md)
5. [skills.json](./skills.json)
6. [bundles.json](./bundles.json) if bundle membership changes
7. `.well-known/agent-skills/` if a bundle-level endpoint is affected
8. README files only if the package story materially changes

## Example

```text
Help me add a new skill to this repository and keep it consistent with the current package structure.

Create or update everything needed, including:
- skills/<name>/SKILL.md
- skills/<name>/references/current-guidance.md
- docs/skills-index.md
- docs/skills.json
- docs/bundles.json if needed
- docs/.well-known/agent-skills/* if needed

New skill details:

name: nz-job-search-basics
bundle: nz-living-basics
geography: nz
audience:
- international-students
- newcomers
policy_sensitive: true
official_sources_required: true

Goal:
Explain the basics of finding part-time work, internships, and early-career opportunities in New Zealand for international students and new arrivals.

Scope:
- local job platforms and search paths
- CV and application expectations
- work-rights and policy-sensitive boundaries

Preferred source order:
- official university career pages
- official New Zealand government employment guidance
- official employer or platform help pages
```
