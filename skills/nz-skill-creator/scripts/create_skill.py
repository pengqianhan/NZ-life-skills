#!/usr/bin/env python3
"""Create a new NZ Life Skills skill and register it in repo manifests."""

from __future__ import annotations

import argparse
import re
import subprocess
from pathlib import Path
from textwrap import dedent


SKILL_CREATOR_ROOT = Path("/Users/pengqianhan/.codex/skills/.system/skill-creator")
INIT_SKILL = SKILL_CREATOR_ROOT / "scripts/init_skill.py"


def parse_bool(value: str) -> bool:
    lowered = value.strip().lower()
    if lowered in {"true", "1", "yes"}:
        return True
    if lowered in {"false", "0", "no"}:
        return False
    raise argparse.ArgumentTypeError(f"Expected true/false, got: {value}")


def run(cmd: list[str], cwd: Path) -> None:
    subprocess.run(cmd, cwd=str(cwd), check=True)


def yaml_quote(value: str) -> str:
    return '"' + value.replace("\\", "\\\\").replace('"', '\\"') + '"'


def write_openai_yaml(
    path: Path, *, display_name: str, short_description: str, default_prompt: str
) -> None:
    content = (
        "interface:\n"
        f"  display_name: {yaml_quote(display_name)}\n"
        f"  short_description: {yaml_quote(short_description)}\n"
        f"  default_prompt: {yaml_quote(default_prompt)}\n"
    )
    path.write_text(content)


def validate_created_skill(skill_dir: Path, expected_name: str) -> None:
    skill_md = skill_dir / "SKILL.md"
    openai_yaml = skill_dir / "agents" / "openai.yaml"
    reference_md = skill_dir / "references" / "current-guidance.md"

    if not skill_md.exists():
        raise SystemExit(f"Missing SKILL.md: {skill_md}")
    if not openai_yaml.exists():
        raise SystemExit(f"Missing agents/openai.yaml: {openai_yaml}")
    if not reference_md.exists():
        raise SystemExit(f"Missing references/current-guidance.md: {reference_md}")

    content = skill_md.read_text()
    match = re.match(r"^---\n(.*?)\n---\n", content, re.DOTALL)
    if not match:
        raise SystemExit("SKILL.md frontmatter is missing or malformed.")
    frontmatter = match.group(1)
    if f"name: {expected_name}" not in frontmatter:
        raise SystemExit("SKILL.md frontmatter name does not match the requested skill name.")
    if "description:" not in frontmatter:
        raise SystemExit("SKILL.md frontmatter is missing description.")


def write_skill_md(
    path: Path,
    *,
    name: str,
    description: str,
    bundle: str,
    geography: str,
    audience: list[str],
    policy_sensitive: bool,
    official_sources_required: bool,
    goal: str,
    scope: list[str],
    preferred_source_order: list[str],
) -> None:
    audience_block = "\n".join(f"    - {item}" for item in audience)
    scope_block = "\n".join(f"- {item}" for item in scope)
    source_block = "\n".join(f"{idx}. {item}" for idx, item in enumerate(preferred_source_order, start=1))
    content = (
        "---\n"
        f"name: {name}\n"
        f"description: {description}\n"
        "metadata:\n"
        "  author: Pengqian Han\n"
        "  package: nz-life-skills\n"
        f"  bundle: {bundle}\n"
        f"  geography: {geography}\n"
        "  audience:\n"
        f"{audience_block}\n"
        f"  policy_sensitive: {str(policy_sensitive).lower()}\n"
        f"  official_sources_required: {str(official_sources_required).lower()}\n"
        "---\n\n"
        f"# {name}\n\n"
        "## Overview\n\n"
        f"{goal}\n\n"
        "## Workflow\n\n"
        "1. Clarify the user's exact question and determine whether they need eligibility, process, comparison, or planning help.\n"
        "2. Read [references/current-guidance.md](references/current-guidance.md).\n"
        "3. Separate stable explanation from any current operational detail.\n"
        "4. If the question is current or policy-sensitive, verify the latest official sources before answering.\n"
        "5. Update the reference file if the official guidance has changed materially.\n\n"
        "## Scope\n\n"
        f"{scope_block}\n\n"
        "## Source Order\n\n"
        f"{source_block}\n\n"
        "## Answering Rules\n\n"
        "- Prefer concise, practical guidance over broad lifestyle commentary.\n"
        "- State scope or eligibility first when relevant.\n"
        "- Call out uncertainty and current-policy boundaries directly.\n"
        "- Use official sources as the authority when live rules may have changed.\n\n"
        "## References\n\n"
        "- Read [references/current-guidance.md](references/current-guidance.md) before answering.\n"
    )
    path.write_text(content)


def write_reference(path: Path, *, title: str, goal: str, preferred_source_order: list[str]) -> None:
    sources = "\n".join(f"- {item}" for item in preferred_source_order)
    content = dedent(
        f"""\
        # {title} Current Guidance

        As of: `TODO`

        {goal}

        Replace this scaffold with a concise baseline summary. For policy-sensitive topics, keep only the durable framing here and verify anything current before answering.

        ## Official Sources

        {sources}

        ## Stable Framing

        - Add the stable baseline explanation here.
        - Keep changing prices, forms, and process details out of the static summary unless they are verified and dated.
        """
    )
    path.write_text(content)


def main() -> None:
    parser = argparse.ArgumentParser(description="Create and register an NZ Life Skills skill.")
    parser.add_argument("--repo-root", required=True)
    parser.add_argument("--name", required=True)
    parser.add_argument("--bundle", required=True)
    parser.add_argument("--bundle-title")
    parser.add_argument("--bundle-title-zh")
    parser.add_argument("--bundle-description")
    parser.add_argument("--bundle-description-zh")
    parser.add_argument("--geography", required=True, choices=["nz", "global", "mixed"])
    parser.add_argument("--audience", action="append", required=True)
    parser.add_argument("--policy-sensitive", type=parse_bool, required=True)
    parser.add_argument("--official-sources-required", type=parse_bool, required=True)
    parser.add_argument("--description", required=True)
    parser.add_argument("--description-zh")
    parser.add_argument("--title-zh")
    parser.add_argument("--goal", required=True)
    parser.add_argument("--scope", action="append", required=True)
    parser.add_argument("--preferred-source", action="append", required=True)
    parser.add_argument("--display-name")
    parser.add_argument("--short-description")
    parser.add_argument("--default-prompt")
    args = parser.parse_args()

    repo_root = Path(args.repo_root).resolve()
    skill_dir = repo_root / "skills" / args.name

    if skill_dir.exists():
        raise SystemExit(f"Skill already exists: {skill_dir}")

    display_name = args.display_name or title_from_slug(args.name)
    short_description = args.short_description or f"Create {args.name} and sync repo manifests"
    default_prompt = args.default_prompt or (
        f"Use ${args.name} to help with this New Zealand life workflow."
    )

    run(
        [
            "python3",
            str(INIT_SKILL),
            args.name,
            "--path",
            str(repo_root / "skills"),
            "--resources",
            "references",
            "--interface",
            f"display_name={display_name}",
            "--interface",
            f"short_description={short_description}",
            "--interface",
            f"default_prompt={default_prompt}",
        ],
        cwd=repo_root,
    )

    write_skill_md(
        skill_dir / "SKILL.md",
        name=args.name,
        description=args.description,
        bundle=args.bundle,
        geography=args.geography,
        audience=args.audience,
        policy_sensitive=args.policy_sensitive,
        official_sources_required=args.official_sources_required,
        goal=args.goal,
        scope=args.scope,
        preferred_source_order=args.preferred_source,
    )
    write_reference(
        skill_dir / "references" / "current-guidance.md",
        title=args.name,
        goal=args.goal,
        preferred_source_order=args.preferred_source,
    )

    write_openai_yaml(
        skill_dir / "agents" / "openai.yaml",
        display_name=display_name,
        short_description=short_description,
        default_prompt=default_prompt,
    )

    register_cmd = [
        "python3",
        str(skill_dir.parent / "nz-skill-creator" / "scripts" / "register_skill.py"),
        "--repo-root",
        str(repo_root),
        "--name",
        args.name,
        "--bundle",
        args.bundle,
        "--geography",
        args.geography,
        "--policy-sensitive",
        str(args.policy_sensitive).lower(),
        "--official-sources-required",
        str(args.official_sources_required).lower(),
        "--description",
        args.description,
        "--description-zh",
        args.description_zh or args.description,
        "--title-zh",
        args.title_zh or args.name,
    ]
    for audience in args.audience:
        register_cmd.extend(["--audience", audience])
    for bundle_arg, value in [
        ("--bundle-title", args.bundle_title),
        ("--bundle-title-zh", args.bundle_title_zh),
        ("--bundle-description", args.bundle_description),
        ("--bundle-description-zh", args.bundle_description_zh),
    ]:
        if value:
            register_cmd.extend([bundle_arg, value])
    run(register_cmd, cwd=repo_root)

    validate_created_skill(skill_dir, args.name)


def title_from_slug(slug: str) -> str:
    return " ".join(part.capitalize() for part in slug.split("-"))


if __name__ == "__main__":
    main()
