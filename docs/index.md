# NZ Life Skills

![NZ Life Skills](/NZ-life-skills/assets/banner.png)

New Zealand pre-departure and newcomer onboarding package for Codex and Claude Code, with official-source-backed guidance for international students and new arrivals.

## Start Here

- [Repository on GitHub](https://github.com/pengqianhan/NZ-life-skills)
- [English README](../README.md)
- [中文 README](../README.zh-CN.md)
- [Package structure](./package-structure.md)
- [For agents](./for-agents.md)
- [Skills index](./skills-index.md)
- [Bundles manifest](./bundles.json)
- [Skills manifest](./skills.json)

## Package View

### Pre-Departure
- prepare-nz-study-departure

### Arrival Setup
- kiwi-access-card
- nz-ird-number
- nz-bank-account
- nz-mobile-connectivity
- nz-public-transport

### Living Basics
- nz-renting-basics
- nz-healthcare-access

### Meta
- repo-discoverability
- nz-skill-creator

### Extended
- nz-travel-planner
- travel-planner

## Why This Exists

Newcomers often need help with everyday setup tasks, but the correct answer depends on current official rules. This repository packages those tasks as one reusable vertical bundle with explicit official-source grounding and a policy-freshness rule.

It is designed to be:

- easy to ingest as one newcomer package
- easy to install into Codex or Claude Code
- easy to maintain as policies change

## Installation

### Codex

```bash
git clone https://github.com/pengqianhan/NZ-life-skills.git ~/.codex/skill-repos/nz-life-skills
bash ~/.codex/skill-repos/nz-life-skills/scripts/install-codex-all.sh
```

### Claude Code

```bash
git clone https://github.com/pengqianhan/NZ-life-skills.git ~/.claude/skill-repos/nz-life-skills
bash ~/.claude/skill-repos/nz-life-skills/scripts/install-claude-all.sh
```

## Packaging Guidance

The recommended adoption unit is:

- the full repository as `New Zealand newcomer onboarding`
- or a focused bundle such as `nz-arrival-setup`

Machine-readable discovery files are available at:

- `robots.txt`
- `sitemap.xml`
- `bundles.json`
- `skills.json`
- `.well-known/agent-skills/index.json`

## Official Source Rule

- Prefer government, university, bank, carrier, transport authority, or provider websites.
- Do not rely on blogs or forum posts when an official source exists.
- Verify live operational details before answering current-policy questions.
