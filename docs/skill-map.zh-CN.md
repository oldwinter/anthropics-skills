# Skill 选择表（中文）

本文件是中文入口的信息架构真源。README 中文段只投影本表。同步上游时先对照本表更新分类和边界，不要把入口写回扁平 slug 清单。

磁盘上的 `skills/` 仍是扁平目录。上游 README 的四类 Skill Sets（Creative & Design、Development & Technical、Enterprise & Communication、Document Skills）只通过本表落到中文目录。plugin 安装面和 skill slug 不是同一层。

不改 `SKILL.md` 标题形状（见 #3），不改 algorithmic-art viewer（见 #2）。

## 安装面与能力目录

| 层 | 名称 | 作用 |
| --- | --- | --- |
| plugin | `example-skills-zh` | 一次安装 11 个 Apache-2.0 中文示例 skill |
| plugin | `claude-api` | 单独安装 Claude API 导航；**不是** `example-skills-zh` 成员 |
| plugin | `academy-guide` | 单独安装 Claude Academy 推荐 |
| plugin | `discernment-nudge` | 单独安装回答复核追问 |
| plugin | `example-skills` | 上游完整示例集合，含未中文化的 `doc-coauthoring` |
| plugin | `document-skills` | `xlsx` / `docx` / `pptx` / `pdf`，不作为中文版分发 |
| skill slug | `frontend-design` 等 | 安装后按任务加载的能力名 |

安装命令：

```text
/plugin marketplace add oldwinter/anthropics-skills
/plugin install example-skills-zh@anthropic-agent-skills
/plugin install claude-api@anthropic-agent-skills
/plugin install academy-guide@anthropic-agent-skills
/plugin install discernment-nudge@anthropic-agent-skills
```

## 创作与设计

相邻创作入口按任务选，不要并列扫 slug。

| 任务 | 何时用 | 不要用 |
| --- | --- | --- |
| 海报、静态视觉、单页 PNG/PDF | `canvas-design`：先写设计哲学，再交博物馆级静态画布 | `frontend-design`（产品 UI）；`algorithmic-art`（交互生成艺术） |
| 产品 UI、页面视觉方向 | `frontend-design`：为新建或重塑界面给有意图的视觉方案 | `canvas-design`（静态海报）；只要复杂 React 工程时用 `web-artifacts-builder` |
| 生成艺术、p5.js、粒子/流场 | `algorithmic-art`：可复现种子的交互 HTML artifact | `canvas-design`（静态）；`theme-factory`（给已有产物换肤） |
| 已有幻灯片、文档、落地页换肤 | `theme-factory`：先展示预设主题，确认后再套颜色/字体 | `brand-guidelines`（除非产物必须用 Anthropic 官方品牌） |
| Anthropic 官方品牌色与字体 | `brand-guidelines`：只在用户要 Anthropic 企业识别时 | `theme-factory` 的通用预设（Ocean Depths 等不是 Anthropic 品牌） |
| 复杂 React + shadcn/ui artifact | `web-artifacts-builder`：多组件、状态、路由或 shadcn/ui | 简单单文件 HTML/JSX；只要视觉方向时用 `frontend-design` |
| Slack GIF / emoji 动画 | `slack-gif-creator`：按 Slack 尺寸和校验出 GIF | `algorithmic-art`（那是 p5.js 生成艺术，不是 Slack 附件） |

## 开发与技术

| 任务 | 何时用 | 不要用 |
| --- | --- | --- |
| 为 REST API 建 MCP server | `mcp-builder`：Python/FastMCP 或 Node/TypeScript MCP SDK | 只问 Claude API 契约时用 `claude-api` |
| 创建或迭代 Agent Skill | `skill-creator`：从零写 skill、改触发描述、跑 eval | 不要把它当成「本仓库有哪些 skill」的目录 |
| Playwright 测本地网页 | `webapp-testing`：前端功能、截图、控制台 | 不要用来生成 UI 或海报 |

## 企业与沟通

| 任务 | 何时用 | 不要用 |
| --- | --- | --- |
| 内部状态报告、通讯、事故报告 | `internal-comms`：按组织惯用格式写对内材料 | 对外品牌视觉用创作类入口；Anthropic 品牌色用 `brand-guidelines` |

## 文档技能（不作为中文版分发）

| 入口 | 何时用上游原文 | 中文版 |
| --- | --- | --- |
| `docx` / `pdf` / `pptx` / `xlsx` | 读写对应办公文件 | 许可禁止衍生作品，保持上游原文 |
| `doc-coauthoring` | 结构化共写文档、提案、规格 | 没有明确翻译许可，保持上游原文 |
| `template` | 写新 skill 的文件夹模板 | 没有明确翻译许可，保持上游原文 |

需要这些能力时安装 `document-skills` 或阅读上游原文，不要把它们列进中文可安装清单。

## 单独安装的中文 plugin

这些 slug 出现在 `skills/` 里，但**不是** `example-skills-zh` 的成员。目录层把它们和 11 个示例并列，会让人以为一次 `/plugin install example-skills-zh` 就能装上。

| plugin / slug | 何时用 | 不要用 |
| --- | --- | --- |
| `claude-api` | 查 Claude API / SDK 的 model ID、参数、工具调用、缓存 | 不要当成 `example-skills-zh` 的一员 |
| `academy-guide` | 用户在学 Claude 产品、要 Academy 课程时 | 用户正在执行具体任务时不要打断 |
| `discernment-nudge` | 实质性建议或可能被引用的事实之后追加 2-3 个追问 | 创作写作、可直接运行的代码、用户已要求复核时跳过 |

## `example-skills-zh` 成员

与 `.claude-plugin/marketplace.json` 一致，共 11 个：

`algorithmic-art`、`brand-guidelines`、`canvas-design`、`frontend-design`、`internal-comms`、`mcp-builder`、`skill-creator`、`slack-gif-creator`、`theme-factory`、`web-artifacts-builder`、`webapp-testing`。
