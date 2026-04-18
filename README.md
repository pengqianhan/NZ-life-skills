<h1 align="center">NZ Life Skills</h1>

![NZ Life Skills](./assets/banner.png)

A bundled onboarding package for Codex and Claude Code, focused on practical New Zealand newcomer workflows and policy-heavy tasks.

Chinese version: [README.zh-CN.md](./README.zh-CN.md)

Docs:

- [Package structure](./docs/package-structure.md)
- [Skills index](./docs/skills-index.md)
- [For agents](./docs/for-agents.md)
- [GitHub Pages entry](./docs/index.md)
- [llms.txt](./llms.txt)

## Agent Readiness

This repository also exposes machine-readable endpoints for agent discovery and ingestion:

- `llms.txt` at repository root: [llms.txt](./llms.txt)
- GitHub Pages discovery files: `robots.txt` and `sitemap.xml`
- package manifests: [docs/bundles.json](./docs/bundles.json) and [docs/skills.json](./docs/skills.json)
- agent skill index: [docs/.well-known/agent-skills/index.json](./docs/.well-known/agent-skills/index.json)

When published via GitHub Pages, these endpoints are available under the site root and `/.well-known/agent-skills/`.

## Package Intent

This repository is best understood as a `New Zealand newcomer onboarding` package, not a flat list of unrelated skills.

It is designed to be:

- easy to ingest as one vertical capability pack
- easy to install into Codex or Claude Code
- easy to maintain with official-source-first references

## Bundle Index

### Arrival Setup

First-week setup tasks for new arrivals.

- `kiwi-access-card`
- `nz-ird-number`
- `nz-bank-account`
- `nz-mobile-connectivity`
- `nz-public-transport`

### Living Basics

Day-to-day setup tasks after arrival.

- `nz-renting-basics`
- `nz-healthcare-access`

### Meta

Support tooling for adoption and distribution.

- `repo-discoverability`

## Repository Layout

```text
skills/
  <skill-name>/
    SKILL.md
    agents/openai.yaml
    references/
scripts/
.claude-plugin/
```

Each skill lives under `skills/` and is maintained once. The repository is intended to be adopted either as one package or as a small number of bundles.

## Skills

| Skill | Description |
|---|---|
| `kiwi-access-card` | Explain Kiwi Access Card eligibility, online versus in-person application, required documents, fees, timelines, and PDF form handling. |
| `nz-ird-number` | Explain IRD number application, tax-setup basics, and first-arrival tax admin questions. |
| `nz-bank-account` | Explain how to open and set up a New Zealand bank account as a newcomer or student. |
| `nz-mobile-connectivity` | Compare SIM, eSIM, prepaid, and mobile setup options for new arrivals. |
| `nz-public-transport` | Explain city-specific public transport setup, cards, apps, and concession questions. |
| `nz-renting-basics` | Explain rental setup, flatting, tenancy basics, and move-in questions for newcomers. |
| `nz-healthcare-access` | Explain how to use GPs, urgent care, pharmacies, and student health services in New Zealand. |
| `repo-discoverability` | Improve a GitHub repository so search engines, GitHub users, and AI agents can discover it more easily. |

For a concise packaging view, see [Package structure](./docs/package-structure.md).

## Install For Codex

### Install one skill

```bash
git clone https://github.com/pengqianhan/NZ-life-skills.git ~/.codex/skill-repos/nz-life-skills
bash ~/.codex/skill-repos/nz-life-skills/scripts/install-codex-skill.sh kiwi-access-card
```

### Install all skills

```bash
git clone https://github.com/pengqianhan/NZ-life-skills.git ~/.codex/skill-repos/nz-life-skills
bash ~/.codex/skill-repos/nz-life-skills/scripts/install-codex-all.sh
```

## Install For Claude Code

### Install as a plugin repository

```bash
git clone https://github.com/pengqianhan/NZ-life-skills.git ~/.claude/plugins/nz-life-skills
```

This repository includes `.claude-plugin/plugin.json`, so Claude Code can treat the repo as a plugin-style skill collection rooted at `./skills`.

### Install one skill into `~/.claude/skills`

```bash
git clone https://github.com/pengqianhan/NZ-life-skills.git ~/.claude/skill-repos/nz-life-skills
bash ~/.claude/skill-repos/nz-life-skills/scripts/install-claude-skill.sh kiwi-access-card
```

### Install all skills into `~/.claude/skills`

```bash
git clone https://github.com/pengqianhan/NZ-life-skills.git ~/.claude/skill-repos/nz-life-skills
bash ~/.claude/skill-repos/nz-life-skills/scripts/install-claude-all.sh
```

## Updating Installed Skills

If you installed from a cloned repo plus install script:

```bash
cd ~/.codex/skill-repos/nz-life-skills
git pull
bash scripts/install-codex-all.sh
```

or for Claude Code:

```bash
cd ~/.claude/skill-repos/nz-life-skills
git pull
bash scripts/install-claude-all.sh
```

If you installed by cloning directly into `~/.claude/plugins/nz-life-skills`, update with:

```bash
cd ~/.claude/plugins/nz-life-skills
git pull
```

## Maintenance Rule For Policy Skills

Some skills in this repository depend on live public policy or application rules. For those skills:

- treat fees, requirements, and process details as unstable
- verify official sources before answering any `current`, `latest`, `today`, or operational question
- update the skill reference files if the official policy has changed

## Official Source Rule

Every skill in this repository must include an explicit official-source basis in its reference files.

- Each skill reference file should contain an `Official Sources` section.
- Prefer government, regulator, transport authority, university, bank, carrier, or provider official websites.
- If the skill is comparative, list the main official providers that should be checked.
- Do not rely on blogs, forums, or social media when an official source exists.
