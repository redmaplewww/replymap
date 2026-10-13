<div align="center">

  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="docs/images/logo-dark.svg">
    <img src="docs/images/logo.svg" width="176" alt="ReplyMap logo">
  </picture>

  # ReplyMap

  **Turn long AI replies into a colorful, faithful reading map.**

  [简体中文](README.md) | **English**

  [![License](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
  [![CI](https://img.shields.io/github/actions/workflow/status/redmaplewww/replymap/ci.yml?branch=main&label=CI)](https://github.com/redmaplewww/replymap/actions/workflows/ci.yml)
  [![GitHub stars](https://img.shields.io/github/stars/redmaplewww/replymap?style=social)](https://github.com/redmaplewww/replymap/stargazers)

  [🚀 Quick Start](#-quick-start) · [📖 Documentation](docs/) · [🎨 Colorful Graphs](#-colorful-graphs) · [🤝 Contributing](#-contributing)

</div>

## ✨ Features

- **Response-level architecture maps**: expose goals, evidence, operations, decisions, results, and limits.
- **Information-density guardrails**: complex replies retain 8–12 meaningful nodes instead of a generic five-step pipeline.
- **Semantic colors**: goals, processes, evidence, decisions, results, and risks use explainable colors with text and shape support.
- **Graceful output**: prefer Mermaid and fall back to an ID-preserving outline when Mermaid is unavailable.
- **Agent-ready packaging**: `agents/openai.yaml` declares the Codex skill display name and prompt.

## 📦 Requirements

- Python 3.10+
- Mermaid support from the host Agent or Markdown client (optional)

## 🔧 Installation

~~~powershell
git clone https://github.com/redmaplewww/replymap.git $HOME/.codex/skills/reply-architecture
~~~

## 🚀 Quick Start

~~~powershell
python scripts/measure_response.py --input response.md --json
python scripts/render_response_graph.py --input response.md --format markdown
~~~

The renderer is a structured starting point. Review nodes, edges, evidence, and caveats against the response.

## 🧭 Agent behavior

Activate for long or structurally dense replies with multiple stages, decisions, dependencies, or architectures. Place the map after the opening orientation, never as a replacement for the response. Inferred relationships use dashed edges and are explained in the legend.

## 🎨 Colorful graphs

| Role | Color family | Purpose |
| --- | --- | --- |
| Goal / root | Indigo | Find what the reply is solving |
| Process / evidence | Blue, violet, teal | See actions and supporting material |
| Decision / branch | Amber | Find places that require judgment |
| Result / output | Green, cyan | Find concrete conclusions |
| Risk / limit | Coral, red | Find claims that need checking |

Color never replaces labels, shapes, or a legend.

## 📚 Documentation

| Document | Contents |
| --- | --- |
| [Getting started](docs/getting-started.md) | Install the skill and generate a first map |
| [Usage guide](docs/usage.md) | Activation, extraction, color, and fallback rules |
| [FAQ](docs/faq.md) | Common questions and troubleshooting |
| [Response contract](references/response-contract.md) | Stable IDs and evidence mapping |

## 🤝 Contributing

Read [CONTRIBUTING.md](CONTRIBUTING.md) and run `python -m compileall scripts` before submitting.

## 📄 License

[MIT](LICENSE) © 2026 redmaplewww
