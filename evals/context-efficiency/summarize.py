#!/usr/bin/env python3
"""Summarize observable metrics from isolated Codex JSONL evaluations."""

from __future__ import annotations

import argparse
import json
from pathlib import Path


def summarize(fixture: Path) -> dict[str, object]:
    summary_file = fixture / "summary.json"
    run = json.loads(summary_file.read_text(encoding="utf-8")) if summary_file.exists() else {}
    log = Path(run.get("log_path", fixture / "codex.jsonl"))
    events = []
    for line in log.read_text(encoding="utf-8", errors="replace").splitlines():
        try:
            event = json.loads(line)
            if isinstance(event, dict):
                events.append(event)
        except json.JSONDecodeError:
            continue

    commands = [
        event["item"]
        for event in events
        if event.get("type") == "item.completed"
        and event.get("item", {}).get("type") == "command_execution"
    ]
    usage = [event["usage"] for event in events if event.get("type") == "turn.completed" and "usage" in event]
    final = Path(run.get("final_path", fixture / "final.txt"))
    return {
        "case": fixture.name,
        "log_bytes": log.stat().st_size,
        "command_count": len(commands),
        "command_output_chars": sum(len(item.get("aggregated_output", "")) for item in commands),
        "final_chars": len(final.read_text(encoding="utf-8")) if final.exists() else None,
        "usage": usage[-1] if usage else None,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("fixtures", nargs="+", type=Path)
    args = parser.parse_args()
    print(json.dumps([summarize(fixture) for fixture in args.fixtures], indent=2))


if __name__ == "__main__":
    main()
