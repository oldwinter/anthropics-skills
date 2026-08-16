# Anthropic Agent Skills 中文化档案

同步上游后先读本档案，再处理新增或变更内容。

## 项目定位

- 上游项目：`anthropics/skills`
- 中文 fork：`oldwinter/anthropics-skills`
- 当前同步上游 commit：`f6656c1256d5f8a70d9c10df7198a6b79939b18c`
- 主要安装面：Claude Code plugin marketplace
- 目标用户：使用 Claude Code 和 Claude Agent Skills 的中文开发者
- 中文 runtime 入口：11 个 Apache-2.0 示例 skill 的 `skills/*/SKILL.md`，以及 `skills/claude-api/SKILL.md`
- 不应宣传为中文版安装的入口：`document-skills`、`doc-coauthoring`、`template`

## 中文化目标

本 fork 提供可直接执行的中文触发说明和中文运行导读，同时保留上游英文技术正文作为精确契约。翻译帮助中文用户选择流程、理解边界并找到正确参考文件，不改写命令、代码、协议和 API 事实。

## 许可边界

- `docx`、`pdf`、`pptx`、`xlsx` 的 `LICENSE.txt` 明确禁止创建衍生作品和再分发，不修改其内容，也不宣传为中文版。
- `doc-coauthoring` 与 `template` 没有明确的衍生翻译许可，保持上游原文。
- 仅修改带 Apache-2.0 许可的 skill 入口；保留每个 `LICENSE.txt` 和 `THIRD_PARTY_NOTICES.md` 原文。

## 翻译策略

- `name`、skill slug、plugin 名、命令、参数、环境变量、URL、路径、model ID、beta header、YAML/JSON key 保持原样。
- Frontmatter `description` 中文化并保留英文关键词，使中文请求能够触发相同能力。
- 短流程提供完整中文执行导读；长篇 API、schema、eval 和语言实现文档保留英文，由中文导读导航。
- 中文导读与英文正文冲突时，以同一文件的英文权威契约和官方实时文档为准。
- 上游同步时先比较入口文件；更新中文导读涉及的事实、路径或行为，避免无关重写造成长期冲突。

## 安装与交付

注册 marketplace：

```text
/plugin marketplace add oldwinter/anthropics-skills
```

安装中文示例 skill 集合：

```text
/plugin install example-skills-zh@anthropic-agent-skills
```

安装 Claude API 中文导航 skill：

```text
/plugin install claude-api@anthropic-agent-skills
```

## 同步后检查

- `git diff --check`
- `rg -n '^(<<<<<<<|=======|>>>>>>>)$' .`
- `.claude-plugin/marketplace.json` 是有效 JSON，且 `example-skills-zh` 只包含获准中文化的入口。
- 所有修改的 `SKILL.md` frontmatter 可由 `skills/skill-creator/scripts/quick_validate.py` 解析。
- 与上游比较时，受限制或未明确授权的六个入口以及全部 `LICENSE.txt`、`THIRD_PARTY_NOTICES.md` 必须保持不变。
- README 安装命令指向中文 fork，plugin 安装后实际加载带中文导读的 `SKILL.md`。
