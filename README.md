<div align="center">

  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="docs/images/logo-dark.svg">
    <img src="docs/images/logo.svg" width="176" alt="ReplyMap logo">
  </picture>

  # ReplyMap

  **把长篇 AI 回复变成有颜色、忠实于原文的阅读地图。**

  **简体中文** | [English](README.en.md)

  [![License](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
  [![CI](https://img.shields.io/github/actions/workflow/status/redmaplewww/replymap/ci.yml?branch=main&label=CI)](https://github.com/redmaplewww/replymap/actions/workflows/ci.yml)
  [![GitHub stars](https://img.shields.io/github/stars/redmaplewww/replymap?style=social)](https://github.com/redmaplewww/replymap/stargazers)

  [🚀 快速开始](#-快速开始) · [📖 文档](docs/) · [🎨 彩色图形](#-彩色图形) · [🤝 贡献](#-贡献)

</div>

## ✨ 特性

- **回答级架构图**：把目标、证据、操作、决策、结果和限制组织成可扫描的阅读骨架。
- **信息密度保护**：复杂回答默认保留 8–12 个有实际含义的节点，避免退化成空泛的五步流程。
- **语义化配色**：根目标、处理过程、证据、决策、结果和风险使用可解释的颜色，并保留文字与形状辅助。
- **多种输出**：优先生成 Mermaid；不支持 Mermaid 时提供保持相同 ID 的缩进式阅读地图。
- **Agent 友好**：通过 `agents/openai.yaml` 声明展示名和默认调用提示，可直接作为 Codex skill 安装。

## 📦 环境要求

- Python 3.10+
- Mermaid 渲染能力（由宿主 Agent 或 Markdown 客户端提供，可选）

## 🔧 安装

~~~powershell
git clone https://github.com/redmaplewww/replymap.git $HOME/.codex/skills/reply-architecture
~~~

## 🚀 快速开始

~~~powershell
python scripts/measure_response.py --input response.md --json
python scripts/render_response_graph.py --input response.md --format markdown
~~~

渲染器是结构化起点，Agent 仍应根据回答复核节点、边、证据映射和风险表达。

## 🧭 Agent 使用原则

长回答或包含多阶段推理、决策树、系统架构时启用。图应紧跟在回答开头的执行摘要之后，不替代正文。每个节点必须能回指到回答中的可见内容；推断关系使用虚线并在图中说明。

## 🎨 彩色图形

| 角色 | 颜色倾向 | 作用 |
| --- | --- | --- |
| 目标 / 根节点 | 靛蓝 | 定位回答要解决什么 |
| 过程 / 证据 | 蓝、紫、青绿 | 识别行动和依据 |
| 决策 / 分支 | 琥珀 | 标出需要判断的地方 |
| 结果 / 输出 | 绿色、青色 | 定位可执行结论 |
| 风险 / 限制 | 珊瑚、红色 | 提醒需要核对的内容 |

颜色不会替代文字、形状或图例，因此在不同主题和色觉条件下仍可阅读。

## 📚 文档

| 文档 | 内容 |
| --- | --- |
| [入门指南](docs/getting-started.md) | 安装 skill 并生成第一张图 |
| [使用手册](docs/usage.md) | 激活、抽取、配色和降级规则 |
| [FAQ](docs/faq.md) | 常见问题和排查方式 |
| [响应契约](references/response-contract.md) | 稳定 ID 和证据映射 |

## 🤝 贡献

请先阅读 [贡献指南](CONTRIBUTING.md)，提交前运行 `python -m compileall scripts`。

## 📄 License

[MIT](LICENSE) © 2026 redmaplewww
