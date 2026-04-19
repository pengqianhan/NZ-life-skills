<h1 align="center">NZ Life Skills</h1>

![NZ Life Skills](./assets/banner.png)

A bundled onboarding package for Codex and Claude Code, focused on practical New Zealand pre-departure, arrival, and newcomer workflows with policy-heavy tasks where needed.

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

### Pre-Departure
Pre-departure planning and packing guidance for students heading to New Zealand.

- `prepare-nz-study-departure`

### Arrival Setup
First-week setup tasks for identity, tax, banking, mobile, and public transport.

- `kiwi-access-card`
- `nz-ird-number`
- `nz-bank-account`
- `nz-mobile-connectivity`
- `nz-public-transport`

### Living Basics
Day-to-day setup tasks after arrival, including housing and healthcare.

- `nz-renting-basics`
- `nz-healthcare-access`

### Meta
Repository distribution and discoverability support.

- `repo-discoverability`
- `nz-skill-creator`

### Extended
Travel-planning skills that extend the repository beyond newcomer onboarding.

- `nz-travel-planner`
- `travel-planner`

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
| `prepare-nz-study-departure` | Build and tailor a pre-departure checklist for Chinese students heading to New Zealand, covering documents, payment, phone setup, electronics, adapters, and packing decisions. |
| `kiwi-access-card` | Answer questions about New Zealand Kiwi Access Card eligibility, online versus in-person application, required documents, fees, processing times, and form interpretation. |
| `nz-ird-number` | Explain how to apply for and use a New Zealand IRD number, including eligibility, required identity documents, tax setup, and common first-arrival questions. |
| `nz-bank-account` | Explain how international students and new arrivals can open and use a New Zealand bank account, including common document requirements and setup tasks. |
| `nz-mobile-connectivity` | Explain how new arrivals in New Zealand can choose and activate mobile service, including prepaid versus plan, SIM versus eSIM, and airport setup. |
| `nz-public-transport` | Explain how to start using public transport in New Zealand cities, including transport cards, local transit apps, airport-to-city setup, and concessions. |
| `nz-renting-basics` | Explain the basics of renting in New Zealand for international students, including application documents, bond, tenancy setup, and first-week housing questions. |
| `nz-healthcare-access` | Explain how international students and new arrivals can access healthcare in New Zealand, including GPs, urgent care, pharmacies, and student health services. |
| `repo-discoverability` | Improve the discoverability of a GitHub repository for search engines, GitHub users, and AI agents. |
| `nz-travel-planner` | New Zealand travel planning skill for road trips and multi-day travel, especially in the Auckland Northland and Bay of Islands region. |
| `travel-planner` | Universal travel planning skill for multi-day road trips and city-hopping itineraries anywhere in the world. |
| `nz-skill-creator` | Create or update repository-native skills in NZ Life Skills and keep package docs, manifests, and bundle-level agent indexes in sync. |

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
