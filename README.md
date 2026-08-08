> **中文 fork 提示：** 本仓库是 [`anthropics/skills`](https://github.com/anthropics/skills) 的非官方中文 fork，当前同步上游 commit 为 `f17010c9bb483898c1d9c9f42dde2b3a98889434`。Agent Skills 标准见 [agentskills.io](http://agentskills.io)。

# Anthropic Agent Skills 中文版

Skills 是由指令、脚本和资源组成的目录，Claude 会按任务动态加载它们，以可重复的方式完成专业工作。本 fork 在不改变命令、代码、schema 和运行时契约的前提下，为许可允许修改的 skill 增加中文触发说明和中文执行导读。

## 中文化范围

可直接安装的中文入口包括：

- `algorithmic-art`
- `brand-guidelines`
- `canvas-design`
- `frontend-design`
- `internal-comms`
- `mcp-builder`
- `skill-creator`
- `slack-gif-creator`
- `theme-factory`
- `web-artifacts-builder`
- `webapp-testing`
- `claude-api`

长篇 API、协议、schema、代码示例和评测参考保留上游英文，中文执行导读负责导航到正确权威文件。

以下入口不作为中文版分发：

- `docx`、`pdf`、`pptx`、`xlsx` 的许可明确禁止创建衍生作品，因此保持上游原文。
- `doc-coauthoring` 与 `template` 没有明确授予衍生翻译许可，因此保持上游原文。

## 在 Claude Code 中安装中文版

先注册中文 fork 的 marketplace：

```text
/plugin marketplace add oldwinter/anthropics-skills
```

安装 11 个中文示例 skill：

```text
/plugin install example-skills-zh@anthropic-agent-skills
```

单独安装 Claude API 中文导航 skill：

```text
/plugin install claude-api@anthropic-agent-skills
```

安装后直接用自然语言描述任务即可，例如：“使用 MCP Builder skill 为这个 REST API 创建一个 MCP server。”

## 使用边界

- 本 fork 不是 Anthropic 官方发行，更新和中文化由 fork 维护者负责。
- 代码标识符、命令、URL、文件路径、frontmatter 字段、model ID、beta header 和精确 API schema 不翻译。
- 中文执行导读与英文技术正文冲突时，以同一文件中的上游英文契约和官方实时文档为准。
- 这些 skills 主要用于演示和教育；关键工作流应在自己的环境中充分测试。

## 上游资料

- [什么是 Skills？](https://support.claude.com/en/articles/12512176-what-are-skills)
- [在 Claude 中使用 Skills](https://support.claude.com/en/articles/12512180-using-skills-in-claude)
- [创建自定义 Skills](https://support.claude.com/en/articles/12512198-creating-custom-skills)
- [让 Agent Skills 面向真实世界工作](https://anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills)

---

下面保留上游 README，方便核对原始安装方式、免责声明和项目说明。

> **Note:** This repository contains Anthropic's implementation of skills for Claude. For information about the Agent Skills standard, see [agentskills.io](http://agentskills.io).

[![skills.sh](https://skills.sh/b/anthropics/skills)](https://skills.sh/anthropics/skills)

# Skills
Skills are folders of instructions, scripts, and resources that Claude loads dynamically to improve performance on specialized tasks. Skills teach Claude how to complete specific tasks in a repeatable way, whether that's creating documents with your company's brand guidelines, analyzing data using your organization's specific workflows, or automating personal tasks.

For more information, check out:
- [What are skills?](https://support.claude.com/en/articles/12512176-what-are-skills)
- [Using skills in Claude](https://support.claude.com/en/articles/12512180-using-skills-in-claude)
- [How to create custom skills](https://support.claude.com/en/articles/12512198-creating-custom-skills)
- [Equipping agents for the real world with Agent Skills](https://anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills)

# About This Repository

This repository contains skills that demonstrate what's possible with Claude's skills system. These skills range from creative applications (art, music, design) to technical tasks (testing web apps, MCP server generation) to enterprise workflows (communications, branding, etc.).

Each skill is self-contained in its own folder with a `SKILL.md` file containing the instructions and metadata that Claude uses. Browse through these skills to get inspiration for your own skills or to understand different patterns and approaches.

Many skills in this repo are open source (Apache 2.0). We've also included the document creation & editing skills that power [Claude's document capabilities](https://www.anthropic.com/news/create-files) under the hood in the [`skills/docx`](./skills/docx), [`skills/pdf`](./skills/pdf), [`skills/pptx`](./skills/pptx), and [`skills/xlsx`](./skills/xlsx) subfolders. These are source-available, not open source, but we wanted to share these with developers as a reference for more complex skills that are actively used in a production AI application.

## Disclaimer

**These skills are provided for demonstration and educational purposes only.** While some of these capabilities may be available in Claude, the implementations and behaviors you receive from Claude may differ from what is shown in these skills. These skills are meant to illustrate patterns and possibilities. Always test skills thoroughly in your own environment before relying on them for critical tasks.

# Skill Sets
- [./skills](./skills): Skill examples for Creative & Design, Development & Technical, Enterprise & Communication, and Document Skills
- [./spec](./spec): The Agent Skills specification
- [./template](./template): Skill template

# Try in Claude Code, Claude.ai, and the API

## Claude Code
You can register this repository as a Claude Code Plugin marketplace by running the following command in Claude Code:
```
/plugin marketplace add anthropics/skills
```

Then, to install a specific set of skills:
1. Select `Browse and install plugins`
2. Select `anthropic-agent-skills`
3. Select `document-skills` or `example-skills`
4. Select `Install now`

Alternatively, directly install either Plugin via:
```
/plugin install document-skills@anthropic-agent-skills
/plugin install example-skills@anthropic-agent-skills
```

After installing the plugin, you can use the skill by just mentioning it. For instance, if you install the `document-skills` plugin from the marketplace, you can ask Claude Code to do something like: "Use the PDF skill to extract the form fields from `path/to/some-file.pdf`"

## Claude.ai

These example skills are all already available to paid plans in Claude.ai. 

To use any skill from this repository or upload custom skills, follow the instructions in [Using skills in Claude](https://support.claude.com/en/articles/12512180-using-skills-in-claude#h_a4222fa77b).

## Claude API

You can use Anthropic's pre-built skills, and upload custom skills, via the Claude API. See the [Skills API Quickstart](https://docs.claude.com/en/api/skills-guide#creating-a-skill) for more.

# Creating a Basic Skill

Skills are simple to create - just a folder with a `SKILL.md` file containing YAML frontmatter and instructions. You can use the **template-skill** in this repository as a starting point:

```markdown
---
name: my-skill-name
description: A clear description of what this skill does and when to use it
---

# My Skill Name

[Add your instructions here that Claude will follow when this skill is active]

## Examples
- Example usage 1
- Example usage 2

## Guidelines
- Guideline 1
- Guideline 2
```

The frontmatter requires only two fields:
- `name` - A unique identifier for your skill (lowercase, hyphens for spaces)
- `description` - A complete description of what the skill does and when to use it

The markdown content below contains the instructions, examples, and guidelines that Claude will follow. For more details, see [How to create custom skills](https://support.claude.com/en/articles/12512198-creating-custom-skills).

# Partner Skills

Skills are a great way to teach Claude how to get better at using specific pieces of software. As we see awesome example skills from partners, we may highlight some of them here:

- **Notion** - [Notion Skills for Claude](https://www.notion.so/notiondevs/Notion-Skills-for-Claude-28da4445d27180c7af1df7d8615723d0)
