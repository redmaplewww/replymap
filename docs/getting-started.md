# 入门指南

## 安装

~~~powershell
git clone https://github.com/redmaplewww/replymap.git $HOME/.codex/skills/reply-architecture
~~~

刷新 Agent 后，使用 `$reply-architecture` 触发。

## 生成第一张图

准备 UTF-8 的 `response.md`：

~~~powershell
python scripts/measure_response.py --input response.md --json
python scripts/render_response_graph.py --input response.md --format markdown
~~~

输出中的 Mermaid 代码包含 `classDef` 和 `class`，支持 Mermaid 的宿主会显示彩色节点。

## 复核

自动草图必须由 Agent 复核：节点能否回指正文，关系是否被正文支持，重要结果与限制是否保留，颜色是否有足够对比度。
