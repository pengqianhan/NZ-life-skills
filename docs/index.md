# NZ Life Skills

![NZ Life Skills](/NZ-life-skills/assets/banner.png)

New Zealand newcomer onboarding package for Codex and Claude Code, with official-source-backed guidance for international students and new arrivals.

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

### Arrival Setup

- Kiwi Access Card
- IRD number
- bank account setup
- mobile setup
- public transport

### Living Basics

- renting basics
- healthcare access

### Meta

- repository discoverability support

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
- or the `Arrival Setup` bundle as the smallest strong package

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
