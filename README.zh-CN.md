# NZ Life Skills

![NZ Life Skills](./assets/banner.png)

一个同时面向 Codex 和 Claude Code 的新西兰生活技能仓库，重点覆盖国际学生，尤其是中国留学生，在新西兰落地后最常见、最容易卡住的生活问题。

English version: [README.md](./README.md)

## 这个仓库解决什么问题

这个仓库把新西兰生活中的高频问题整理成可安装、可复用的 skills，例如：

- IRD number 申请
- 银行开户
- 手机卡和 eSIM
- 公共交通
- 租房基础
- 医疗资源使用
- Kiwi Access Card

每个 skill 都尽量遵循同一原则：

- 优先使用官方网站作为依据
- 当前政策、费用、流程如果可能变化，先联网核实
- 如果官方规则变化，更新 skill reference

## 支持的 Agents

- Codex
- Claude Code

## 技能列表

| Skill | 说明 |
|---|---|
| `kiwi-access-card` | 解释 Kiwi Access Card 的资格、线上和线下申请、所需材料、费用和表格问题。 |
| `nz-ird-number` | 解释 IRD number 的申请、用途、常见材料和到达新西兰后的税务初始化问题。 |
| `nz-bank-account` | 解释新西兰银行开户、常见材料、地址证明和日常使用设置。 |
| `nz-mobile-connectivity` | 解释 SIM、eSIM、预付费、套餐选择和落地即用的通信方案。 |
| `nz-public-transport` | 解释不同城市的交通卡、官方 app、机场到住处和学生优惠。 |
| `nz-renting-basics` | 解释租房、flatting、bond、入住检查和租房常见文档。 |
| `nz-healthcare-access` | 解释 GP、urgent care、pharmacy、student health 等医疗入口。 |
| `repo-discoverability` | 帮助改造 GitHub 仓库，让搜索引擎、GitHub 用户和 AI agents 更容易发现它。 |

## 安装到 Codex

### 安装单个 skill

```bash
git clone https://github.com/pengqianhan/NZ-life-skills.git ~/.codex/skill-repos/nz-life-skills
bash ~/.codex/skill-repos/nz-life-skills/scripts/install-codex-skill.sh kiwi-access-card
```

### 安装全部 skills

```bash
git clone https://github.com/pengqianhan/NZ-life-skills.git ~/.codex/skill-repos/nz-life-skills
bash ~/.codex/skill-repos/nz-life-skills/scripts/install-codex-all.sh
```

## 安装到 Claude Code

### 作为 plugin-style 仓库使用

```bash
git clone https://github.com/pengqianhan/NZ-life-skills.git ~/.claude/plugins/nz-life-skills
```

### 安装单个 skill 到 `~/.claude/skills`

```bash
git clone https://github.com/pengqianhan/NZ-life-skills.git ~/.claude/skill-repos/nz-life-skills
bash ~/.claude/skill-repos/nz-life-skills/scripts/install-claude-skill.sh kiwi-access-card
```

### 安装全部 skills 到 `~/.claude/skills`

```bash
git clone https://github.com/pengqianhan/NZ-life-skills.git ~/.claude/skill-repos/nz-life-skills
bash ~/.claude/skill-repos/nz-life-skills/scripts/install-claude-all.sh
```

## 适合谁

这个仓库特别适合：

- 刚到新西兰的国际学生
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
