---
name: repo-discoverability
description: Improve the discoverability of a GitHub repository for search engines, GitHub users, and AI agents by auditing repository metadata, README structure, docs pages, GitHub Pages setup, community health files, and agent-friendly index files such as llms.txt. Use when Codex needs to help a user promote a repository, make it easier to discover on the web, improve GitHub Pages visibility, or make a skills or docs repository easier for agents to parse and reuse.
---

# Repo Discoverability

## Overview

Use this skill to turn a repository into a clearer public entry point for humans and agents. Focus on making the repo easier to find, easier to understand quickly, and easier to cite from stable pages.

## Workflow

1. Identify the repository's audience:
   - human readers
   - GitHub search users
   - search engines
   - AI agents
2. Read [references/discoverability-checklist.md](references/discoverability-checklist.md).
3. Audit the repository for:
   - GitHub About completeness
   - README quality
   - bilingual or audience-specific docs
   - skills or docs index pages
   - community health files
   - GitHub Pages status
   - agent-facing entry points
4. Apply the highest-leverage fixes first:
   - repository metadata
   - landing-page README
   - stable docs pages
   - structured agent files
5. If GitHub Pages is involved, separate:
   - content changes inside the repo
   - manual GitHub settings steps the user must do in the UI
6. Verify final links and static asset paths before finishing.

## What To Improve

Prioritize these surfaces:

1. GitHub repository `About`
2. README landing page
3. localized README when the audience is multilingual
4. docs index pages
5. GitHub Pages entry page
6. community health files:
   - LICENSE
   - CONTRIBUTING
   - CODE_OF_CONDUCT
   - issue templates
   - PR template
7. agent-facing files:
   - `docs/for-agents.md`
   - `llms.txt`
   - repository-wide index pages

## GitHub Pages Rule

When using GitHub Pages:

- Distinguish user-project pages from repository project pages.
- For project pages, static asset paths often need the repository prefix.
- If Pages deploys from `/docs`, assets referenced by the page must be reachable from the deployed site, not only from the repository root.
- Explain any required manual Settings changes explicitly because Codex cannot assume it can change GitHub UI settings.

## Answering Rules

- State whether the problem is:
  - discoverability
  - documentation quality
  - GitHub configuration
  - Pages deployment
  - agent parsing
- Prefer durable improvements over one-off promotion tips.
- If the user wants promotion, recommend both:
  - on-repo improvements
  - off-repo distribution steps
- If the user wants search and agent discovery, ensure the repository has stable crawlable documents instead of relying only on a long README.

## Manual UI Boundaries

When the next step must be done in GitHub web settings, say so directly and provide the exact click path. Examples include:

- setting repository description, website, and topics
- uploading a social preview
- enabling GitHub Pages
- choosing the Pages source branch and folder

## References

- Read [references/discoverability-checklist.md](references/discoverability-checklist.md) before applying changes.
- Use that checklist to decide what to add, what to update, and what the user still needs to do manually.
