#!/usr/bin/env python3
"""Report instruction bytes and exact repeated paragraphs without loading source text."""

from __future__ import annotations

import argparse
from collections import defaultdict
from pathlib import Path
import re


ROOT = Path(__file__).resolve().parents[1]


def instruction_files(global_agents: Path | None) -> list[Path]:
    files = [ROOT / "AGENTS.md"]
    if global_agents is not None and global_agents.is_file():
        files.append(global_agents)
    files.extend(sorted((ROOT / "skills").glob("*/SKILL.md")))
    files.extend(sorted((ROOT / "skills").glob("*/references/*.md")))
    return files


def repeated_paragraphs(files: list[Path]) -> list[tuple[int, str, list[str]]]:
    owners: dict[str, set[str]] = defaultdict(set)
    for path in files:
        text = path.read_text(encoding="utf-8")
        for paragraph in re.split(r"\n\s*\n", text):
            normalized = " ".join(paragraph.split())
            if len(normalized) >= 100:
                owners[normalized].add(str(path.relative_to(ROOT)) if path.is_relative_to(ROOT) else str(path))
    return sorted(
        ((len(places), paragraph[:100], sorted(places)) for paragraph, places in owners.items() if len(places) > 1),
        reverse=True,
    )


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--global-agents", type=Path, help="Optional global AGENTS.md path")
    args = parser.parse_args()
    files = instruction_files(args.global_agents)
    for path in files:
        label = str(path.relative_to(ROOT)) if path.is_relative_to(ROOT) else str(path)
        text = path.read_text(encoding="utf-8")
        metadata = ""
        if path.name == "SKILL.md":
            match = re.match(r"\A---\n(.*?)\n---", text, re.DOTALL)
            if match:
                metadata = f" metadata_bytes={len(match.group(1).encode('utf-8'))}"
        print(f"{label}\tbytes={path.stat().st_size}{metadata}")
    print(f"TOTAL\tbytes={sum(path.stat().st_size for path in files)}")
    duplicates = repeated_paragraphs(files)
    print(f"EXACT_DUPLICATE_PARAGRAPHS\tcount={len(duplicates)}")
    for count, excerpt, places in duplicates:
        print(f"{count} files: {', '.join(places)}: {excerpt}")


if __name__ == "__main__":
    main()
