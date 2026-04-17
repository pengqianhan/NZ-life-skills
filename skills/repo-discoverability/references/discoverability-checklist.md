# Repository Discoverability Checklist

Use this file to improve how a repository is discovered by GitHub users, search engines, and AI agents.

## Core Surfaces

### 1. GitHub About

- Add a clear one-line description.
- Add a website URL if a Pages site or homepage exists.
- Add relevant topics.
- Upload a social preview image.

### 2. README Landing Page

- Explain what the repository is in the first paragraph.
- Make the target audience explicit.
- List what problems the repository solves.
- Link to deeper docs instead of hiding everything in one file.
- Add bilingual docs if the audience is multilingual.

### 3. Structured Docs

- Add a skill index or content index.
- Add a page specifically for agents if the repo is agent-oriented.
- Add stable pages that can be cited directly.

### 4. GitHub Pages

- Publish a clean landing page from `docs/` or another stable source.
- Verify that image and asset paths work in the deployed site, not only in local Markdown preview.
- For project pages, remember that paths may need the repository prefix.

### 5. Community Health

- LICENSE
- CONTRIBUTING.md
- CODE_OF_CONDUCT.md
- issue templates
- PR template

### 6. Agent-Facing Files

- `docs/for-agents.md`
- `llms.txt`
- concise repository index pages

## High-Leverage Sequence

Apply improvements in this order:

1. About metadata
2. README landing page
3. docs index
4. community files
5. GitHub Pages
6. agent-facing files
7. off-repo promotion

## Off-Repo Promotion

Once the repository itself is ready:

- share it where the target audience already gathers
- write a short post about the real problem it solves
- get backlinks from relevant organizations, communities, or blogs
- point people to a stable landing page, not only a raw repository tree

## Common Failure Modes

- missing repository description or topics
- README that does not say who the repo is for
- no stable docs index
- Pages enabled but asset paths broken
- no bilingual docs for a multilingual audience
- no official-source rule for policy-sensitive content
- no agent-facing summary page
