#!/usr/bin/env python3
"""Create a conservative Mermaid scaffold from headings and list items in a response.

This is intentionally structural. The calling agent should review and enrich it
with semantic relationships before presenting it to a user.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from pathlib import Path


def slug(value: str, fallback: str) -> str:
    words = re.findall(r"[A-Za-z0-9]+", value.lower())
    return "-".join(words[:5]) or fallback


def safe(value: str) -> str:
    value = re.sub(r"\s+", " ", value.strip())
    value = value.replace('"', "'")
    return value[:60]


def build(text: str) -> dict:
    digest = hashlib.sha256(text.encode("utf-8")).hexdigest()[:12]
    lines = text.splitlines()
    items = []
    current_heading = None
    paragraph_index = 0
    for line in lines:
        heading = re.match(r"^\s*(#{1,6})\s+(.+?)\s*$", line)
        ordered = re.match(r"^\s*(\d+)[.)]\s+(.+?)\s*$", line)
        bullet = re.match(r"^\s*[-*+]\s+(.+?)\s*$", line)
        if heading:
            current_heading = heading.group(2)
            paragraph_index += 1
            items.append(("section", current_heading, paragraph_index, current_heading))
        elif ordered:
            paragraph_index += 1
            items.append(("step", ordered.group(2), paragraph_index, current_heading))
        elif bullet and len(items) < 12:
            paragraph_index += 1
            items.append(("detail", bullet.group(1), paragraph_index, current_heading))
    if not items:
        paragraphs = [p.strip().replace("\n", " ") for p in re.split(r"\n\s*\n", text) if p.strip()]
        items = [("section", p, i + 1, None) for i, p in enumerate(paragraphs[:8])]
    items = items[:12]
    nodes = []
    for i, (kind, label, fragment, parent) in enumerate(items, 1):
        node_id = f"a-{slug(label, f'node-{i}')}-{i}"
        node_kind = "step" if kind == "step" else "section" if kind == "section" else "other"
        nodes.append({
            "id": node_id,
            "label": safe(label),
            "kind": node_kind,
            "summary": safe(label),
            "fragment_refs": [f"r-p{fragment}"],
            "confidence": 0.65,
            "provenance": "ai_suggestion",
            "status": "suggested",
        })
    edges = []
    for i in range(1, len(nodes)):
        edges.append({
            "id": f"r-e{i}",
            "from": nodes[i - 1]["id"],
            "to": nodes[i]["id"],
            "relation": "leads_to",
            "label": "leads to",
            "fragment_refs": nodes[i - 1]["fragment_refs"] + nodes[i]["fragment_refs"],
            "confidence": 0.45,
            "provenance": "ai_suggestion",
            "status": "suggested",
        })
    mermaid = ["flowchart TD"]
    for node in nodes:
        label = node["label"].replace("\\", "\\\\").replace('"', "'")
        shape = '(["{}"])' if node["kind"] == "section" else '{{"{}"}}' if node["kind"] == "step" else '["{}"]'
        mermaid.append(f'  {node["id"]}{shape.format(label)}:::{node["kind"]}')
    for edge in edges:
        mermaid.append(f'  {edge["from"]} -->|{edge["label"]}| {edge["to"]}')
    mermaid.extend([
        "",
        "  classDef section fill:#4F46E5,color:#FFFFFF,stroke:#312E81,stroke-width:2px;",
        "  classDef step fill:#FEF3C7,color:#78350F,stroke:#F59E0B,stroke-width:1.5px;",
        "  classDef other fill:#E0F2FE,color:#0C4A6E,stroke:#38BDF8,stroke-width:1.5px;",
    ])
    outline = []
    for i, node in enumerate(nodes):
        prefix = "└─ " if i else ""
        outline.append(f'{prefix}[{node["id"]}] {node["label"]}')
    return {
        "response": {
            "id": "r-response",
            "content_hash": digest,
            "fragments": [{"id": f"r-p{i}", "locator": f"structural item {i}"} for i in range(1, len(items) + 1)],
            "architecture": {
                "nodes": nodes,
                "edges": edges,
                "diagram": {"direction": "TD", "mermaid": "\n".join(mermaid), "fallback_outline": "\n".join(outline)},
            },
        }
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", type=Path, help="UTF-8 text or Markdown file; defaults to stdin")
    parser.add_argument("--format", choices=("json", "markdown"), default="json")
    args = parser.parse_args()
    text = args.input.read_text(encoding="utf-8") if args.input else sys.stdin.read()
    result = build(text)
    if args.format == "json":
        print(json.dumps(result, ensure_ascii=False, indent=2))
    else:
        diagram = result["response"]["architecture"]["diagram"]
        print("> **阅读导航**：以下图示是基于回答标题与步骤生成的结构草图，请以正文为准。\n")
        print("```mermaid")
        print(diagram["mermaid"])
        print("```")
        print("\n**结构草图**\n")
        print("\n".join(f"- {line}" for line in diagram["fallback_outline"].splitlines()))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
