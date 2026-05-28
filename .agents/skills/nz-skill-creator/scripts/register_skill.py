#!/usr/bin/env python3
"""Register or update a skill in the NZ Life Skills repository.

This repo-specific helper updates the machine-readable manifests and re-renders
the repository-level docs that are derived from them.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from textwrap import dedent


PACKAGE_SLUG = "nz-life-skills"
PACKAGE_TITLE = "New Zealand newcomer onboarding"
PACKAGE_TITLE_ZH = "新西兰新来者与留学生 onboarding"
PACKAGE_DESCRIPTION = (
    "Agent-friendly onboarding package for international students and newcomers in New Zealand."
)
PACKAGE_DESCRIPTION_ZH = (
    "一个面向国际学生与新来者的、适合 agents 接入的新西兰生活 onboarding 技能包。"
)
REPO_URL = "https://github.com/pengqianhan/NZ-life-skills"
SITE_URL = "https://pengqianhan.github.io/NZ-life-skills"
DEFAULT_BUNDLE_ZH = {
    "nz-pre-departure": ("出发前准备", "覆盖赴新西兰前的准备和行李规划问题。"),
    "nz-arrival-setup": ("落地办理", "覆盖新到新西兰后第一周最关键的身份、办理和落地事项。"),
    "nz-living-basics": ("日常生活", "覆盖落地后日常生活的基础问题。"),
    "meta": ("仓库维护", "覆盖这个 package 的分发和可发现性支持。"),
    "extended": ("扩展能力", "覆盖超出 newcomer 主线但仍有复用价值的延伸技能。"),
}
DEFAULT_SKILL_ZH = {
    "prepare-nz-study-departure": (
        "留学出发前 checklist",
        "为赴新西兰的中国留学生整理出发前清单，覆盖证件、支付、电子设备、插头和打包取舍。",
    ),
    "kiwi-access-card": (
        "Kiwi Access Card",
        "解释 Kiwi Access Card 的资格、线上和线下申请、所需材料、费用和表格问题。",
    ),
    "nz-ird-number": (
        "IRD number 申请",
        "解释 IRD number 的申请、用途、常见材料和到达新西兰后的税务初始化问题。",
    ),
    "nz-bank-account": (
        "银行开户",
        "解释新西兰银行开户、常见材料、地址证明和日常使用设置。",
    ),
    "nz-mobile-connectivity": (
        "手机卡和 eSIM",
        "解释 SIM、eSIM、预付费、套餐选择和落地即用的通信方案。",
    ),
    "nz-public-transport": (
        "公共交通",
        "解释不同城市的交通卡、官方 app、机场到住处和学生优惠。",
    ),
    "nz-renting-basics": (
        "租房基础",
        "解释租房、flatting、bond、入住检查和租房常见文档。",
    ),
    "nz-healthcare-access": (
        "医疗资源使用",
        "解释 GP、urgent care、pharmacy、student health 等医疗入口。",
    ),
    "repo-discoverability": (
        "repo discoverability",
        "帮助改造 GitHub 仓库，让搜索引擎、GitHub 用户和 AI agents 更容易发现它。",
    ),
    "nz-skill-creator": (
        "nz-skill-creator",
        "在这个仓库里创建或更新 skill，并同步维护 docs、manifests 和 bundle 级 agent 索引。",
    ),
    "nz-travel-planner": (
        "新西兰旅行规划",
        "为新西兰多日行程与自驾路线提供旅行规划能力。",
    ),
    "travel-planner": (
        "通用旅行规划",
        "为不同国家和地区的多日旅行路线提供通用规划能力。",
    ),
}


def parse_bool(value: str) -> bool:
    lowered = value.strip().lower()
    if lowered in {"true", "1", "yes"}:
        return True
    if lowered in {"false", "0", "no"}:
        return False
    raise argparse.ArgumentTypeError(f"Expected true/false, got: {value}")


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


def title_from_slug(slug: str) -> str:
    return " ".join(part.capitalize() for part in slug.split("-"))


def chinese_title_from_slug(slug: str) -> str:
    return DEFAULT_BUNDLE_ZH.get(slug, (slug, ""))[0]


def audience_for_agent(audience: list[str]) -> list[str]:
    return [item.replace("-", " ") for item in audience]


def local_path_from_github_url(url: str | None) -> str | None:
    if not url:
        return None
    marker = "/blob/main/"
    if marker not in url:
        return None
    return url.split(marker, 1)[1]


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


def skill_title_zh(skill: dict) -> str:
    return skill.get("title_zh") or skill["name"]


def skill_description_zh(skill: dict) -> str:
    return skill.get("description_zh") or skill["description"]


def bundle_name_zh(bundle: dict) -> str:
    return bundle.get("name_zh") or bundle["name"]


def bundle_description_zh(bundle: dict) -> str:
    return bundle.get("description_zh") or bundle["description"]


def package_title(package: dict) -> str:
    return package.get("title", PACKAGE_TITLE)


def package_title_zh(package: dict) -> str:
    return package.get("title_zh", PACKAGE_TITLE_ZH)


def package_description(package: dict) -> str:
    return package.get("description", PACKAGE_DESCRIPTION)


def package_description_zh(package: dict) -> str:
    return package.get("description_zh", PACKAGE_DESCRIPTION_ZH)


def render_readme_en(skills: list[dict], bundles: list[dict], package: dict) -> str:
    bundle_lines = []
    for bundle in bundles:
        bundle_lines.append(f"### {bundle['name']}\n")
        bundle_lines.append(f"{bundle['description']}\n\n")
        for skill_name in bundle["skills"]:
            bundle_lines.append(f"- `{skill_name}`\n")
        bundle_lines.append("\n")

    table_lines = ["| Skill | Description |", "|---|---|"]
    for skill in skills:
        table_lines.append(f"| `{skill['name']}` | {skill['description']} |")
    bundle_block = "".join(bundle_lines).rstrip()
    table_block = "\n".join(table_lines)

    return normalize_markdown(
        f"""
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

        This repository is best understood as a `{package_title(package)}` package, not a flat list of unrelated skills.

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
        git clone {REPO_URL}.git ~/.codex/skill-repos/nz-life-skills
        bash ~/.codex/skill-repos/nz-life-skills/scripts/install-codex-skill.sh kiwi-access-card
        ```

        ### Install all skills

        ```bash
        git clone {REPO_URL}.git ~/.codex/skill-repos/nz-life-skills
        bash ~/.codex/skill-repos/nz-life-skills/scripts/install-codex-all.sh
        ```

        ## Install For Claude Code

        ### Install as a plugin repository

        ```bash
        git clone {REPO_URL}.git ~/.claude/plugins/nz-life-skills
        ```

        This repository includes `.claude-plugin/plugin.json`, so Claude Code can treat the repo as a plugin-style skill collection rooted at `./skills`.

        ### Install one skill into `~/.claude/skills`

        ```bash
        git clone {REPO_URL}.git ~/.claude/skill-repos/nz-life-skills
        bash ~/.claude/skill-repos/nz-life-skills/scripts/install-claude-skill.sh kiwi-access-card
        ```

        ### Install all skills into `~/.claude/skills`

        ```bash
        git clone {REPO_URL}.git ~/.claude/skill-repos/nz-life-skills
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


def render_readme_zh(skills: list[dict], bundles: list[dict], package: dict) -> str:
    bundle_lines = []
    skill_map = {skill["name"]: skill for skill in skills}
    for bundle in bundles:
        bundle_lines.append(f"### {bundle_name_zh(bundle)}\n\n")
        bundle_lines.append(f"{bundle_description_zh(bundle)}\n\n")
        for skill_name in bundle["skills"]:
            bundle_lines.append(f"- {skill_title_zh(skill_map[skill_name])}\n")
        bundle_lines.append("\n")

    table_lines = ["| Skill | 说明 |", "|---|---|"]
    for skill in skills:
        table_lines.append(f"| `{skill['name']}` | {skill_description_zh(skill)} |")
    bundle_block = "".join(bundle_lines).rstrip()
    table_block = "\n".join(table_lines)

    return normalize_markdown(
        f"""
        # NZ Life Skills

        ![NZ Life Skills](./assets/banner.png)

        一个同时面向 Codex 和 Claude Code 的新西兰生活 onboarding package，重点覆盖国际学生，尤其是中国留学生，在赴新前准备、落地和安顿阶段最常见、最容易卡住的生活问题。

        English version: [README.md](./README.md)

        文档入口：

        - [Package structure](./docs/package-structure.md)
        - [Skills index](./docs/skills-index.md)
        - [For agents](./docs/for-agents.md)
        - [GitHub Pages entry](./docs/index.md)
        - [llms.txt](./llms.txt)

        ## Agent Readiness

        这个仓库也暴露了一组可供 agents 发现和接入的机器可读入口：

        - 仓库根目录的 [llms.txt](./llms.txt)
        - GitHub Pages 站点下的 `robots.txt` 和 `sitemap.xml`
        - package manifests: [docs/bundles.json](./docs/bundles.json) 和 [docs/skills.json](./docs/skills.json)
        - agent skill index: [docs/.well-known/agent-skills/index.json](./docs/.well-known/agent-skills/index.json)

        如果启用了 GitHub Pages，这些入口会出现在站点根目录和 `/.well-known/agent-skills/` 下。

        ## Package 定位

        这个仓库更适合被理解为一个 `{package_title(package)}` 能力包，而不是一组彼此无关的零散 skills。

        它的目标是：

        - 方便外部项目按一个垂直 package 收录
        - 方便安装到 Codex 或 Claude Code
        - 方便围绕官方来源持续维护

        ## Bundle 结构

        {bundle_block}

        ## 这个仓库解决什么问题

        这个仓库把新西兰生活中的关键 onboarding 问题整理成可安装、可复用的 skills，并尽量遵循同一原则：

        - 优先使用官方网站作为依据
        - 当前政策、费用、流程如果可能变化，先联网核实
        - 如果官方规则变化，更新 skill reference

        ## 支持的 Agents

        - Codex
        - Claude Code

        ## 仓库结构

        ```text
        skills/
          <skill-name>/
            SKILL.md
            agents/openai.yaml
            references/
        scripts/
        .claude-plugin/
        ```

        每个 skill 只在 `skills/` 下维护一次。这个仓库可以被当作一个完整 package 使用，也可以按 bundle 方式接入。

        ## 技能列表

        {table_block}

        如果只想先看 package 视角，可直接阅读：[docs/package-structure.md](./docs/package-structure.md)

        ## 安装到 Codex

        ### 安装单个 skill

        ```bash
        git clone {REPO_URL}.git ~/.codex/skill-repos/nz-life-skills
        bash ~/.codex/skill-repos/nz-life-skills/scripts/install-codex-skill.sh kiwi-access-card
        ```

        ### 安装全部 skills

        ```bash
        git clone {REPO_URL}.git ~/.codex/skill-repos/nz-life-skills
        bash ~/.codex/skill-repos/nz-life-skills/scripts/install-codex-all.sh
        ```

        ## 安装到 Claude Code

        ### 作为 plugin-style 仓库使用

        ```bash
        git clone {REPO_URL}.git ~/.claude/plugins/nz-life-skills
        ```

        这个仓库包含 `.claude-plugin/plugin.json`，Claude Code 可以把它当作一个以 `./skills` 为根目录的 plugin-style skill collection 使用。

        ### 安装单个 skill 到 `~/.claude/skills`

        ```bash
        git clone {REPO_URL}.git ~/.claude/skill-repos/nz-life-skills
        bash ~/.claude/skill-repos/nz-life-skills/scripts/install-claude-skill.sh kiwi-access-card
        ```

        ### 安装全部 skills 到 `~/.claude/skills`

        ```bash
        git clone {REPO_URL}.git ~/.claude/skill-repos/nz-life-skills
        bash ~/.claude/skill-repos/nz-life-skills/scripts/install-claude-all.sh
        ```

        ## 适合谁

        这个仓库特别适合：

        - 刚到新西兰的国际学生
        - 需要一个新西兰 newcomer onboarding bundle 的项目方
        - 想给留学生做 AI 助手的人
        - 想把本地生活信息结构化成 skills 的维护者
        - 需要同时兼容 Codex 和 Claude Code 的使用者

        ## 官方依据规则

        这个仓库中的每个 skill 都应该尽量带有明确的 `Official Sources`：

        - 优先使用政府、大学、银行、运营商、交通机构、医疗机构等官方网站
        - 不依赖博客、论坛或社交媒体作为主要依据
        - 涉及 `current`、`latest`、`today`、价格、资格、流程时，先联网核实再回答

        ## 贡献方式

        欢迎提交：

        - 新的 NZ life skills
        - 官方来源补充
        - README 改进
        - 安装脚本优化
        - 针对国际学生的新场景补充

        贡献说明见：[CONTRIBUTING.md](./CONTRIBUTING.md)
        """
    )


def render_docs_index(bundles: list[dict]) -> str:
    bundle_lines = []
    for bundle in bundles:
        bundle_lines.append(f"### {bundle['name']}\n\n")
        for skill_name in bundle["skills"]:
            bundle_lines.append(f"- {skill_name}\n")
        bundle_lines.append("\n")
    bundle_block = "".join(bundle_lines).rstrip()

    return normalize_markdown(
        f"""
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
        sections.append(f"### {idx}. {bundle['name']}\n\n")
        sections.append(f"Purpose: {bundle['description']}\n\n")
        for skill_name in bundle["skills"]:
            sections.append(f"- `{skill_name}`\n")
        sections.append("\n")
    sections_block = "".join(sections).rstrip()

    return normalize_markdown(
        f"""
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
    bundle_lines = "\n".join(f"- `{bundle['name']}`" for bundle in bundles)
    return normalize_markdown(
        f"""
        # For Agents

        This repository is a bundled New Zealand newcomer onboarding package for Codex and Claude Code.

        ## Repository Intent

        Use this repository when the user needs help with real-life New Zealand setup tasks, especially for international students and newcomers.

        Treat the repository as one vertical package with small internal bundles, not as unrelated one-off skills.

        Typical bundles include:

        {bundle_lines}

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
        sections.append(f"### {bundle['name']}\n\n")
        sections.append(f"Purpose: {bundle['description']}\n\n")
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
        f"""
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


def update_bundle_index(repo_root: Path, package: dict, bundles: list[dict]) -> None:
    index_path = repo_root / "docs/.well-known/agent-skills/index.json"
    index_data = {
        "version": "1.0",
        "name": "NZ Life Skills",
        "title": package_title(package),
        "description": package_description(package),
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


def render_repo_docs(repo_root: Path, skills: list[dict], bundles: list[dict], package: dict) -> None:
    (repo_root / "README.md").write_text(render_readme_en(skills, bundles, package))
    (repo_root / "README.zh-CN.md").write_text(render_readme_zh(skills, bundles, package))
    (repo_root / "docs/index.md").write_text(render_docs_index(bundles))
    (repo_root / "docs/package-structure.md").write_text(render_package_structure(bundles))
    (repo_root / "docs/for-agents.md").write_text(render_for_agents(bundles))
    (repo_root / "docs/skills-index.md").write_text(render_skills_index(skills, bundles))


def ensure_manifest_defaults(skills_data: dict, bundles_data: dict) -> None:
    package = bundles_data.setdefault("package", {})
    package.setdefault("slug", PACKAGE_SLUG)
    package.setdefault("title", PACKAGE_TITLE)
    package.setdefault("title_zh", PACKAGE_TITLE_ZH)
    package.setdefault("description", PACKAGE_DESCRIPTION)
    package.setdefault("description_zh", PACKAGE_DESCRIPTION_ZH)
    package.setdefault("repository_url", REPO_URL)
    package.setdefault("site_url", SITE_URL)

    for bundle in bundles_data["bundles"]:
        default_name_zh, default_desc_zh = DEFAULT_BUNDLE_ZH.get(
            bundle["slug"], (chinese_title_from_slug(bundle["slug"]), bundle["description"])
        )
        if "name_zh" not in bundle or bundle["name_zh"] == bundle["name"]:
            bundle["name_zh"] = default_name_zh
        if "description_zh" not in bundle or bundle["description_zh"] == bundle["description"]:
            bundle["description_zh"] = default_desc_zh

    for skill in skills_data["skills"]:
        default_title_zh, default_desc_zh = DEFAULT_SKILL_ZH.get(
            skill["name"], (skill["name"], skill["description"])
        )
        if "title_zh" not in skill or skill["title_zh"] == skill["name"]:
            skill["title_zh"] = default_title_zh
        if "description_zh" not in skill or skill["description_zh"] == skill["description"]:
            skill["description_zh"] = default_desc_zh


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
    parser.add_argument("--description-zh", default=None)
    parser.add_argument("--title-zh", default=None)
    parser.add_argument("--reference-path", default=None)
    parser.add_argument("--bundle-title", default=None)
    parser.add_argument("--bundle-title-zh", default=None)
    parser.add_argument("--bundle-description", default=None)
    parser.add_argument("--bundle-description-zh", default=None)
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
    ensure_manifest_defaults(skills_data, bundles_data)

    skills = skills_data["skills"]
    bundles = bundles_data["bundles"]
    package = bundles_data["package"]

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
        "description_zh": args.description_zh or args.description,
        "title_zh": args.title_zh or args.name,
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
            "name_zh": args.bundle_title_zh or args.bundle_title,
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
            "description_zh": args.bundle_description_zh or args.bundle_description,
            "doc_url": f"{SITE_URL}/skills-index.html#{args.bundle}",
            "agent_skill_url": f"{SITE_URL}/.well-known/agent-skills/{args.bundle}.json",
            "skills": [args.name],
        }
        bundles.append(bundle_entry)
    else:
        bundle_entry.setdefault("name_zh", args.bundle_title_zh or bundle_entry["name"])
        bundle_entry.setdefault(
            "description_zh", args.bundle_description_zh or bundle_entry["description"]
        )
        if args.bundle_title:
            bundle_entry["name"] = args.bundle_title
        if args.bundle_title_zh:
            bundle_entry["name_zh"] = args.bundle_title_zh
        if args.bundle_description:
            bundle_entry["description"] = args.bundle_description
        if args.bundle_description_zh:
            bundle_entry["description_zh"] = args.bundle_description_zh
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
        write_json(agent_dir / f"{bundle['slug']}.json", build_bundle_manifest(bundle, skills))

    update_bundle_index(repo_root, package, bundles)
    render_repo_docs(repo_root, skills, bundles, package)


if __name__ == "__main__":
    main()
