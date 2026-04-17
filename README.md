<h1 align="center">NZ Life Skills</h1>

![NZ Life Skills](./assets/banner.png)

A shared skill collection for Codex and Claude Code, focused on practical New Zealand workflows and policy-heavy tasks.

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

Each skill lives under `skills/` and is maintained once. This repository exposes the same skill content to both Codex and Claude Code users.

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
