#!/usr/bin/env python3
"""Register or update a skill in the NZ Life Skills repository.

This is a repo-specific helper that upserts machine-readable manifests and
re-renders the English package docs that are derived from them.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from textwrap import dedent


PACKAGE_SLUG = "nz-life-skills"
PACKAGE_TITLE = "New Zealand newcomer onboarding"
REPO_URL = "https://github.com/pengqianhan/NZ-life-skills"
SITE_URL = "https://pengqianhan.github.io/NZ-life-skills"
PACKAGE_DESCRIPTION = (
    "Agent-friendly onboarding package for international students and newcomers in New Zealand."
)


def parse_bool(value: str) -> bool:
    lowered = value.strip().lower()
    if lowered in {"true", "1", "yes"}:
        return True
    if lowered in {"false", "0", "no"}:
        return False
    raise argparse.ArgumentTypeError(f"Expected true/false, got: {value}")


def title_from_slug(slug: str) -> str:
    return " ".join(part.capitalize() for part in slug.split("-"))


def audience_for_agent(audience: list[str]) -> list[str]:
    return [item.replace("-", " ") for item in audience]


def github_blob(path: str) -> str:
    return f"{REPO_URL}/blob/main/{path}"


def load_json(path: Path) -> dict:
    return json.loads(path.read_text())


def write_json(path: Path, data: dict) -> None:
    path.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")


def normalize_markdown(text: str) -> str:
    lines = []
    for line in dedent(text).splitlines():
        if line.startswith("        "):
            line = line[8:]
        lines.append(line.rstrip())
    return "\n".join(lines).strip() + "\n"


def find_skill(skills: list[dict], name: str) -> dict | None:
    for item in skills:
        if item["name"] == name:
            return item
    return None


def find_bundle(bundles: list[dict], slug: str) -> dict | None:
    for item in bundles:
        if item["slug"] == slug:
            return item
    return None


def local_path_from_github_url(url: str | None) -> str | None:
    if not url:
        return None
    marker = "/blob/main/"
    if marker not in url:
        return None
    return url.split(marker, 1)[1]


def render_readme(skills: list[dict], bundles: list[dict]) -> str:
    bundle_lines = []
    for bundle in bundles:
        bundle_lines.append(f"### {bundle['name']}\n")
        bundle_lines.append(f"{bundle['description']}\n")
        for skill_name in bundle["skills"]:
            bundle_lines.append(f"- `{skill_name}`\n")
        bundle_lines.append("\n")

    table_lines = ["| Skill | Description |", "|---|---|"]
    for skill in skills:
        table_lines.append(f"| `{skill['name']}` | {skill['description']} |")
    bundle_block = "".join(bundle_lines).rstrip()
    table_block = "\n".join(table_lines)

    return normalize_markdown(
        f"""\
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

        {bundle_block}

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

        {table_block}

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
        """
    )


def render_docs_index(bundles: list[dict]) -> str:
    bundle_lines = []
    for bundle in bundles:
        bundle_lines.append(f"### {bundle['name']}\n")
        for skill_name in bundle["skills"]:
            bundle_lines.append(f"- {skill_name}\n")
        bundle_lines.append("\n")
    bundle_block = "".join(bundle_lines).rstrip()

    return normalize_markdown(
        f"""\
        # NZ Life Skills

        ![NZ Life Skills](/NZ-life-skills/assets/banner.png)

        New Zealand pre-departure and newcomer onboarding package for Codex and Claude Code, with official-source-backed guidance for international students and new arrivals.

        ## Start Here

        - [Repository on GitHub]({REPO_URL})
        - [English README](../README.md)
        - [中文 README](../README.zh-CN.md)
        - [Package structure](./package-structure.md)
        - [For agents](./for-agents.md)
        - [Skills index](./skills-index.md)
        - [Bundles manifest](./bundles.json)
        - [Skills manifest](./skills.json)

        ## Package View

        {bundle_block}

        ## Why This Exists

        Newcomers often need help with everyday setup tasks, but the correct answer depends on current official rules. This repository packages those tasks as one reusable vertical bundle with explicit official-source grounding and a policy-freshness rule.

        It is designed to be:

        - easy to ingest as one newcomer package
        - easy to install into Codex or Claude Code
        - easy to maintain as policies change

        ## Installation

        ### Codex

        ```bash
        git clone {REPO_URL}.git ~/.codex/skill-repos/nz-life-skills
        bash ~/.codex/skill-repos/nz-life-skills/scripts/install-codex-all.sh
        ```

        ### Claude Code

        ```bash
        git clone {REPO_URL}.git ~/.claude/skill-repos/nz-life-skills
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
        """
    )


def render_package_structure(bundles: list[dict]) -> str:
    sections = []
    for idx, bundle in enumerate(bundles, start=1):
        sections.append(f"### {idx}. {bundle['name']}\n")
        sections.append(f"Purpose: {bundle['description']}\n")
        sections.append("\n")
        for skill_name in bundle["skills"]:
            sections.append(f"- `{skill_name}`\n")
        sections.append("\n")
    sections_block = "".join(sections).rstrip()

    return normalize_markdown(
        f"""\
        # Package Structure

        This repository is easier to adopt when treated as a bundled capability pack, not a flat list of unrelated skills.

        ## Package Positioning

        Use this repository as:

        - a `New Zealand student and newcomer onboarding` package
        - a reusable vertical bundle for `international students` and `new arrivals`
        - an agent-friendly source of policy-aware setup workflows

        ## Recommended Bundle Model

        Group the skills into {len(bundles)} bundles.

        {sections_block}

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
        """
    )


def render_for_agents(bundles: list[dict]) -> str:
    bundle_lines = [f"- `{bundle['name']}`" for bundle in bundles]
    bundle_block = "\n".join(bundle_lines)
    return normalize_markdown(
        f"""\
        # For Agents

        This repository is a bundled New Zealand newcomer onboarding package for Codex and Claude Code.

        ## Repository Intent

        Use this repository when the user needs help with real-life New Zealand setup tasks, especially for international students and newcomers.

        Treat the repository as one vertical package with small internal bundles, not as unrelated one-off skills.

        Typical bundles include:

        {bundle_block}

        ## Repository Layout

        ```text
        skills/
          <skill-name>/
            SKILL.md
            agents/openai.yaml
            references/
        assets/
        scripts/
        ```

        ## Discovery Endpoints

        If this repository is published via GitHub Pages, agents should also check:

        - `robots.txt`
        - `sitemap.xml`
        - `bundles.json`
        - `skills.json`
        - `.well-known/agent-skills/index.json`

        ## How To Read This Repo

        1. Start with [README.md](../README.md) or [README.zh-CN.md](../README.zh-CN.md) for project-level context.
        2. Read [package-structure.md](./package-structure.md) for bundle-level intent.
        3. Go to `skills/<skill-name>/SKILL.md` for the skill workflow.
        4. Read the skill's `references/` files before answering policy-sensitive questions.
        5. Treat any operational detail as potentially time-sensitive unless the skill clearly marks it as stable.

        ## Official Source Rule

        Every skill in this repository should be grounded in official sources.

        - Look for an `Official Sources` section in the skill's reference files.
        - Prefer government, university, bank, carrier, transport authority, or provider sites.
        - Do not rely on blogs, forums, or community posts when an official source exists.

        ## Policy Freshness Rule

        Many skills in this repository are policy-sensitive.

        If the user asks about:

        - current rules
        - latest fees
        - eligibility
        - document requirements
        - official application steps

        then verify the current official sources on the web before answering.

        If the official rules differ from the stored reference, update the skill reference before finishing the task.

        ## Expected Answer Style

        - State eligibility or scope first.
        - Separate stable explanation from current operational detail.
        - Call out uncertainty directly when the general rule and the current portal flow do not match.
        - Use the official source as the authority, not repository memory.

        ## Installation Pointers

        Codex users generally install from:

        - `~/.codex/skills`

        Claude Code users generally install from:

        - `~/.claude/skills`
        - or clone the repo as a plugin-style collection

        Helper scripts live in `scripts/`.
        """
    )


def render_skills_index(skills: list[dict], bundles: list[dict]) -> str:
    skill_map = {skill["name"]: skill for skill in skills}
    sections = []
    for bundle in bundles:
        sections.append(f"### {bundle['name']}\n")
        sections.append(f"\nPurpose: {bundle['description']}\n\n")
        for skill_name in bundle["skills"]:
            skill = skill_map[skill_name]
            sections.append(f"#### `{skill_name}`\n\n")
            sections.append(f"- Purpose: {skill['description']}\n")
            sections.append("- Files:\n")
            skill_doc_local = local_path_from_github_url(skill.get("skill_doc_url"))
            if skill_doc_local:
                sections.append(f"  - [SKILL.md](../{skill_doc_local})\n")
            reference_local = local_path_from_github_url(skill.get("reference_url"))
            if reference_local:
                sections.append(f"  - [Current guidance](../{reference_local})\n")
            sections.append("\n")
    sections_block = "".join(sections).rstrip()

    return normalize_markdown(
        f"""\
        # Skills Index

        This page indexes the repository as a bundled `New Zealand newcomer onboarding` package.

        ## Audience

        This package is designed for:

        - international students arriving in New Zealand
        - Chinese newcomers who want bilingual guidance
        - Codex users
        - Claude Code users
        - maintainers who want a reusable newcomer bundle

        ## Bundle View

        {sections_block}

        ## Package Rules

        - Prefer official sources.
        - Treat policy-sensitive details as unstable.
        - Verify current rules before answering operational questions.
        - Update the relevant reference file if official guidance changes.
        """
    )


def build_bundle_manifest(bundle: dict, skills: list[dict]) -> dict:
    skill_lookup = {skill["name"]: skill for skill in skills}
    return {
        "version": "1.0",
        "slug": bundle["slug"],
        "title": bundle["name"],
        "description": bundle["description"],
        "audience": audience_for_agent(bundle["audience"]),
        "package": f"{SITE_URL}/",
        "skills_index_url": f"{SITE_URL}/skills-index.html#{bundle['slug']}",
        "skills": [
            {
                "name": skill_name,
                "url": skill_lookup[skill_name]["skill_doc_url"],
            }
            for skill_name in bundle["skills"]
        ],
    }


def update_bundle_index(repo_root: Path, bundles: list[dict]) -> None:
    index_path = repo_root / "docs/.well-known/agent-skills/index.json"
    index_data = {
        "version": "1.0",
        "name": "NZ Life Skills",
        "title": PACKAGE_TITLE,
        "description": PACKAGE_DESCRIPTION,
        "homepage": f"{SITE_URL}/",
        "repository": REPO_URL,
        "documents": {
            "package": f"{SITE_URL}/package-structure.html",
            "skills_index": f"{SITE_URL}/skills-index.html",
            "for_agents": f"{SITE_URL}/for-agents.html",
            "llms_txt": github_blob("llms.txt"),
        },
        "bundles": [
            {
                "slug": bundle["slug"],
                "title": bundle["name"],
                "url": f"{SITE_URL}/.well-known/agent-skills/{bundle['slug']}.json",
            }
            for bundle in bundles
        ],
        "manifests": {
            "bundles": f"{SITE_URL}/bundles.json",
            "skills": f"{SITE_URL}/skills.json",
        },
    }
    write_json(index_path, index_data)


def render_english_docs(repo_root: Path, skills: list[dict], bundles: list[dict]) -> None:
    (repo_root / "README.md").write_text(render_readme(skills, bundles))
    (repo_root / "docs/index.md").write_text(render_docs_index(bundles))
    (repo_root / "docs/package-structure.md").write_text(render_package_structure(bundles))
    (repo_root / "docs/for-agents.md").write_text(render_for_agents(bundles))
    (repo_root / "docs/skills-index.md").write_text(render_skills_index(skills, bundles))


def main() -> None:
    parser = argparse.ArgumentParser(description="Register a skill in NZ Life Skills.")
    parser.add_argument("--repo-root", required=True)
    parser.add_argument("--name", required=True)
    parser.add_argument("--bundle", required=True)
    parser.add_argument("--geography", required=True, choices=["nz", "global", "mixed"])
    parser.add_argument("--audience", action="append", required=True)
    parser.add_argument("--policy-sensitive", type=parse_bool, required=True)
    parser.add_argument("--official-sources-required", type=parse_bool, required=True)
    parser.add_argument("--description", required=True)
    parser.add_argument("--reference-path", default=None)
    parser.add_argument("--bundle-title", default=None)
    parser.add_argument("--bundle-description", default=None)
    parser.add_argument("--bundle-geography", default=None, choices=["nz", "global", "mixed"])
    parser.add_argument("--bundle-audience", action="append", default=None)
    parser.add_argument("--bundle-policy-sensitive", type=parse_bool, default=None)
    parser.add_argument("--bundle-official-sources-required", type=parse_bool, default=None)
    args = parser.parse_args()

    repo_root = Path(args.repo_root).resolve()
    skills_path = repo_root / "docs/skills.json"
    bundles_path = repo_root / "docs/bundles.json"

    skills_data = load_json(skills_path)
    bundles_data = load_json(bundles_path)
    skills = skills_data["skills"]
    bundles = bundles_data["bundles"]

    skill_doc_rel = f"skills/{args.name}/SKILL.md"
    reference_rel = args.reference_path or f"skills/{args.name}/references/current-guidance.md"
    reference_abs = repo_root / reference_rel

    skill_entry = {
        "name": args.name,
        "package": PACKAGE_SLUG,
        "bundle": args.bundle,
        "geography": args.geography,
        "audience": args.audience,
        "policy_sensitive": args.policy_sensitive,
        "official_sources_required": args.official_sources_required,
        "description": args.description,
        "skill_doc_url": github_blob(skill_doc_rel),
    }
    if reference_abs.exists():
        skill_entry["reference_url"] = github_blob(reference_rel)

    existing_skill = find_skill(skills, args.name)
    if existing_skill:
        existing_skill.update(skill_entry)
    else:
        skills.append(skill_entry)

    bundle_entry = find_bundle(bundles, args.bundle)
    if bundle_entry is None:
        if not args.bundle_title or not args.bundle_description:
            raise SystemExit("New bundles require --bundle-title and --bundle-description")
        bundle_entry = {
            "name": args.bundle_title,
            "slug": args.bundle,
            "package": PACKAGE_SLUG,
            "geography": args.bundle_geography or args.geography,
            "audience": args.bundle_audience or args.audience,
            "policy_sensitive": (
                args.bundle_policy_sensitive
                if args.bundle_policy_sensitive is not None
                else args.policy_sensitive
            ),
            "official_sources_required": (
                args.bundle_official_sources_required
                if args.bundle_official_sources_required is not None
                else args.official_sources_required
            ),
            "description": args.bundle_description,
            "doc_url": f"{SITE_URL}/skills-index.html#{args.bundle}",
            "agent_skill_url": f"{SITE_URL}/.well-known/agent-skills/{args.bundle}.json",
            "skills": [args.name],
        }
        bundles.append(bundle_entry)
    else:
        if args.name not in bundle_entry["skills"]:
            bundle_entry["skills"].append(args.name)

    skill_order = {skill["name"]: idx for idx, skill in enumerate(skills)}
    for bundle in bundles:
        bundle["skills"] = sorted(bundle["skills"], key=lambda item: skill_order[item])

    write_json(skills_path, skills_data)
    write_json(bundles_path, bundles_data)

    agent_dir = repo_root / "docs/.well-known/agent-skills"
    agent_dir.mkdir(parents=True, exist_ok=True)
    for bundle in bundles:
        bundle_manifest = build_bundle_manifest(bundle, skills)
        write_json(agent_dir / f"{bundle['slug']}.json", bundle_manifest)

    update_bundle_index(repo_root, bundles)
    render_english_docs(repo_root, skills, bundles)


if __name__ == "__main__":
    main()
