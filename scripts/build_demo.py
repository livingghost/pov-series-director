#!/usr/bin/env python3
"""Assemble the long worked example from canonical current-procedure artifacts."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "examples/demo-episode.md"

MARKDOWN_SOURCES = [
    "examples/storm-watch/README.md",
    "examples/storm-watch/source-brief.md",
    "examples/storm-watch/phase-a-plan.md",
    "examples/storm-watch/media-briefs/character-reference-brief.md",
    "examples/storm-watch/media-briefs/clip1-start-frame-brief.md",
    "examples/storm-watch/media-briefs/clip1-end-frame-brief.md",
    "examples/storm-watch/media-briefs/clip2-end-frame-brief.md",
    "examples/storm-watch/planning-diagrams/README.md",
    "examples/storm-watch/media/media-log.md",
    "examples/storm-watch/frame-inspection.md",
    "examples/storm-watch/target-contrast.md",
    "examples/storm-watch/runway-gen45-i2v/director-package.md",
    "examples/storm-watch/runway-gen45-i2v/submission-sheet.md",
    "examples/storm-watch/runway-gen45-i2v/post-production.md",
    "examples/storm-watch/runway-gen45-i2v/result-log.md",
    "examples/storm-watch/veo31-first-last/director-package.md",
    "examples/storm-watch/veo31-first-last/submission-sheet.md",
    "examples/storm-watch/veo31-first-last/post-production.md",
    "examples/storm-watch/veo31-first-last/result-log.md",
    "examples/storm-watch/seedance20-first-last/director-package.md",
    "examples/storm-watch/seedance20-first-last/submission-sheet.md",
    "examples/storm-watch/seedance20-first-last/post-production.md",
    "examples/storm-watch/seedance20-first-last/result-log.md",
]

LITERAL_SOURCES = [
    ("examples/storm-watch/runway-gen45-i2v/submitted-text.txt", "text"),
    ("examples/storm-watch/veo31-first-last/submitted-text.txt", "text"),
    ("examples/storm-watch/veo31-first-last/negative-prompt.txt", "text"),
    ("examples/storm-watch/veo31-first-last/request-body.template.json", "json"),
    ("examples/storm-watch/seedance20-first-last/submitted-text.txt", "text"),
    ("examples/storm-watch/seedance20-first-last/clip2-submitted-text.txt", "text"),
    ("examples/storm-watch/seedance20-first-last/request-body.template.json", "json"),
    ("examples/storm-watch/seedance20-first-last/subtitles-en.srt", "text"),
]


def read(rel: str) -> str:
    path = ROOT / rel
    if not path.is_file():
        raise FileNotFoundError(path)
    return path.read_text(encoding="utf-8").rstrip()


def render() -> str:
    chunks = [
        "# Storm Watch: Generated Canonical Worked Example\n",
        "This file is assembled from the canonical artifacts under `examples/storm-watch/` by "
        "`scripts/build_demo.py`. It demonstrates the artifact set the current natural-language "
        "procedure is expected to produce; it is not a deterministic language-model transcript and "
        "it does not claim a video-generation run.\n",
        "The approved production media live under `examples/storm-watch/media/` with lineage in "
        "its media log; the planning diagrams are kept separate and are never submitted.\n",
    ]

    for rel in MARKDOWN_SOURCES:
        chunks.append(f"\n---\n\n<!-- Canonical artifact: {rel} -->\n\n{read(rel)}\n")

    for rel, language in LITERAL_SOURCES:
        chunks.append(
            f"\n---\n\n## Literal field file: `{rel}`\n\n"
            f"```{language}\n{read(rel)}\n```\n"
        )

    return "".join(chunks).rstrip() + "\n"


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true", help="fail when examples/demo-episode.md is stale")
    args = parser.parse_args(argv)

    content = render()
    if args.check:
        if not OUTPUT.is_file() or OUTPUT.read_text(encoding="utf-8") != content:
            print("stale generated example: examples/demo-episode.md", file=sys.stderr)
            return 1
        print(f"worked example is current: examples/demo-episode.md ({len(content.encode('utf-8')):,} bytes)")
        return 0

    OUTPUT.write_text(content, encoding="utf-8")
    print(f"wrote examples/demo-episode.md ({len(content.encode('utf-8')):,} bytes)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
