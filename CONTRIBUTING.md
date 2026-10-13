# 贡献指南

欢迎为 ReplyMap 提交 Issue 和 PR。

~~~powershell
git clone https://github.com/redmaplewww/replymap.git
cd replymap
$env:PYTHONUTF8='1'
python -m compileall scripts
python scripts/measure_response.py --input README.md --json
~~~

请在提交中说明触发场景、图的结构变化、颜色语义和验证方式。涉及渲染时，附一段输入与预期 Mermaid 输出。
