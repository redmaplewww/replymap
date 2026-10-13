# FAQ

## 为什么生成的图看起来太空？

检查 Agent 是否保留了证据、决策、结果和限制节点。复杂回答至少应保留 8 个有意义节点，避免泛化标签。

## 为什么中文显示异常？

确保输入和输出都是 UTF-8。命令行可先设置 `$env:PYTHONUTF8='1'`；HTML 或 SVG 渲染时使用系统字体栈并声明 UTF-8。

## 为什么我看到黑白图？

检查渲染结果是否包含 `classDef` 和 `class`。ReplyMap 默认使用语义色；若宿主过滤 Mermaid 样式，请使用支持 Mermaid class 的 Markdown 渲染器。
