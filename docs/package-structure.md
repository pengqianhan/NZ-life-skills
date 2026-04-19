# Package Structure

This repository is easier to adopt when treated as a bundled capability pack, not a flat list of unrelated skills.

## Package Positioning

Use this repository as:

- a `New Zealand student and newcomer onboarding` package
- a reusable vertical bundle for `international students` and `new arrivals`
- an agent-friendly source of policy-aware setup workflows

## Recommended Bundle Model

Group the skills into 5 bundles.

### 1. Pre-Departure

Purpose: Pre-departure planning and packing guidance for students heading to New Zealand.

- `prepare-nz-study-departure`

### 2. Arrival Setup

Purpose: First-week setup tasks for identity, tax, banking, mobile, and public transport.

- `kiwi-access-card`
- `nz-ird-number`
- `nz-bank-account`
- `nz-mobile-connectivity`
- `nz-public-transport`

### 3. Living Basics

Purpose: Day-to-day setup tasks after arrival, including housing and healthcare.

- `nz-renting-basics`
- `nz-healthcare-access`

### 4. Meta

Purpose: Repository distribution and discoverability support.

- `repo-discoverability`
- `nz-skill-creator`

### 5. Extended

Purpose: Travel-planning skills that extend the repository beyond newcomer onboarding.

- `nz-travel-planner`
- `travel-planner`

## Recommended Repository Shape

Keep the current file layout for compatibility, but present the repository in this order:

1. package intent
2. bundle index
3. skill index
4. installation paths
5. policy and source rules

## External Packaging Guidance

If another project wants to ingest this repository, the cleanest unit is:

- the whole repository as `NZ newcomer onboarding`
- or the `Arrival Setup` bundle as a standalone package

Avoid presenting one isolated skill as the primary product. The package is more valuable when the skills are treated as a connected workflow.

## What Makes The Package Valuable

- one clear audience
- one geographic scope
- one quality standard
- official-source-first maintenance
- reusable structure across multiple agents

## Near-Term Packaging Priorities

To improve inclusion in larger directories or marketplaces, emphasize:

- bundle names over individual skill names
- newcomer journey coverage over one-off tasks
- stable package docs over long README prose
- clear ingestion points for agents and maintainers
