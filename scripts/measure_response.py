#!/usr/bin/env python3
"""Estimate whether an AI response is structurally large enough for a diagram."""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path


def measure(text: str) -> dict:
    clean = re.sub(r"```.*?```", "", text, flags=re.S)
    non_ws = len(re.sub(r"\s", "", clean))
    words = len(re.findall(r"\b[\w'-]+\b", clean, flags=re.UNICODE))
    headings = len(re.findall(r"(?m)^\s{0,3}#{1,6}\s+\S+", clean))
    ordered = len(re.findall(r"(?m)^\s*(?:\d+[.)]|[一二三四五六七八九十]+[、.])\s+\S+", clean))
    bullets = len(re.findall(r"(?m)^\s*[-*+]\s+\S+", clean))
    paragraph_count = len([p for p in re.split(r"\n\s*\n", clean.strip()) if p.strip()])
    reasons = []
    if non_ws >= 900:
        reasons.append("length")
    if words >= 700:
        reasons.append("length")
    if headings >= 5 or ordered >= 4:
        reasons.append("section_density")
    if (headings >= 3 and paragraph_count >= 6) or ordered >= 4:
        reasons.append("multi_stage")
    reasons = list(dict.fromkeys(reasons))
    return {
        "triggered": bool(reasons),
        "reasons": reasons,
        "metrics": {
            "non_whitespace_chars": non_ws,
            "words": words,
            "headings": headings,
            "ordered_items": ordered,
            "bullet_items": bullets,
            "paragraphs": paragraph_count,
        },
        "thresholds": {
            "non_whitespace_chars": 900,
            "words": 700,
            "headings": 5,
            "ordered_items": 4,
        },
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", type=Path, help="UTF-8 text or Markdown file; defaults to stdin")
    parser.add_argument("--json", action="store_true", help="emit JSON instead of a human-readable result")
    args = parser.parse_args()
    text = args.input.read_text(encoding="utf-8") if args.input else sys.stdin.read()
    result = measure(text)
    if args.json:
        print(json.dumps(result, ensure_ascii=False, indent=2))
    else:
        state = "ACTIVATE" if result["triggered"] else "SKIP"
        print(f"{state}: reasons={','.join(result['reasons']) or 'none'}")
        print(json.dumps(result["metrics"], ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
