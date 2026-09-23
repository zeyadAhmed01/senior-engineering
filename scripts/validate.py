#!/usr/bin/env python3
"""Validate Senior Engineering structure, links, manifests, and eval contracts."""

from __future__ import annotations

import json
from pathlib import Path
import re
import subprocess
import sys


ROOT = Path(__file__).resolve().parents[1]
EXPECTED_SKILLS = {"engineer", "refine", "review", "verify", "github", "release"}
EXPECTED_AGENTS = {"investigator", "reviewer", "security-reviewer", "verifier"}
PORTABLE_SCHEMA = "https://agent-plugins.org/schemas/1.0.0/plugin.schema.json"


def frontmatter(path: Path) -> dict[str, str]:
    text = path.read_text(encoding="utf-8")
    match = re.match(r"\A---\n(?P<body>.*?)\n---(?:\n|\Z)", text, re.DOTALL)
    if match is None:
        raise ValueError("missing frontmatter at first line")

    result: dict[str, str] = {}
    for line in match.group("body").splitlines():
        if line.startswith((" ", "-")):
            continue
        key, separator, value = line.partition(":")
        if separator:
            result[key.strip()] = value.strip()
    return result


def markdown_links(path: Path) -> list[Path]:
    text = path.read_text(encoding="utf-8")
    targets: list[Path] = []
    for target in re.findall(r"\[[^\]]+\]\(([^)]+)\)", text):
        if target.startswith(("http://", "https://", "#")):
            continue
        clean = target.split("#", 1)[0]
        if clean:
            targets.append((path.parent / clean).resolve())
    return targets


def validate() -> list[str]:
    errors: list[str] = []

    try:
        manifest = json.loads((ROOT / "plugin.json").read_text(encoding="utf-8"))
        for key in ("$schema", "name", "version", "description", "author", "license", "extensions"):
            if not manifest.get(key):
                errors.append(f"plugin.json: missing {key}")
        if manifest.get("$schema") != PORTABLE_SCHEMA:
            errors.append("plugin.json: unexpected portable schema")
        if "skills" in manifest or "interface" in manifest:
            errors.append("plugin.json: runtime-specific skills/interface fields must not be at root")
        openai = manifest.get("extensions", {}).get("com.openai", {})
        if not openai.get("interface"):
            errors.append("plugin.json: missing extensions.com.openai.interface")
        if manifest.get("name") != "senior-engineering":
            errors.append("plugin.json: unexpected plugin name")
        if not re.fullmatch(r"\d+\.\d+\.\d+", str(manifest.get("version", ""))):
            errors.append("plugin.json: version must be strict semver")
    except (OSError, json.JSONDecodeError) as error:
        errors.append(f"plugin.json: {error}")

    skill_dirs = {path.name for path in (ROOT / "skills").iterdir() if path.is_dir()}
    if skill_dirs != EXPECTED_SKILLS:
        errors.append(f"skills: expected {sorted(EXPECTED_SKILLS)}, got {sorted(skill_dirs)}")
    if len(skill_dirs) > 8:
        errors.append("skills: public catalog exceeds the eight-skill ceiling")

    descriptions: dict[str, str] = {}
    for skill in sorted(skill_dirs):
        path = ROOT / "skills" / skill / "SKILL.md"
        if not path.exists():
            errors.append(f"{skill}: missing SKILL.md")
            continue
        try:
            fields = frontmatter(path)
        except ValueError as error:
            errors.append(f"{path.relative_to(ROOT)}: {error}")
            continue
        if fields.get("name") != skill:
            errors.append(f"{path.relative_to(ROOT)}: name must match directory")
        description = fields.get("description", "")
        if not description:
            errors.append(f"{path.relative_to(ROOT)}: description is required")
        elif len(description) > 500:
            errors.append(f"{path.relative_to(ROOT)}: description exceeds 500 characters")
        elif description in descriptions:
            errors.append(f"{path.relative_to(ROOT)}: duplicate description with {descriptions[description]}")
        descriptions[description] = skill
        if fields.get("license") != "MIT":
            errors.append(f"{path.relative_to(ROOT)}: license must be MIT")
        if not (path.parent / "agents" / "openai.yaml").exists():
            errors.append(f"{skill}: missing agents/openai.yaml")

    agent_files = {path.stem for path in (ROOT / "agents").glob("*.md")}
    if agent_files != EXPECTED_AGENTS:
        errors.append(f"agents: expected {sorted(EXPECTED_AGENTS)}, got {sorted(agent_files)}")
    for agent in sorted(agent_files):
        path = ROOT / "agents" / f"{agent}.md"
        try:
            fields = frontmatter(path)
        except ValueError as error:
            errors.append(f"{path.relative_to(ROOT)}: {error}")
            continue
        if fields.get("name") != agent or not fields.get("description"):
            errors.append(f"{path.relative_to(ROOT)}: valid name and description required")

    for path in ROOT.rglob("*.md"):
        for target in markdown_links(path):
            if not target.exists():
                errors.append(f"{path.relative_to(ROOT)}: broken local link to {target}")

    try:
        evals = json.loads((ROOT / "evals" / "cases.json").read_text(encoding="utf-8"))
        cases = evals.get("cases", [])
        ids = [case.get("id") for case in cases]
        if len(cases) < 8:
            errors.append("evals/cases.json: expected at least eight behavioral cases")
        if len(ids) != len(set(ids)):
            errors.append("evals/cases.json: case IDs must be unique")
        for case in cases:
            expected = case.get("expected", {})
            if not case.get("prompt") or not expected.get("route") or not expected.get("risk"):
                errors.append(f"eval {case.get('id')}: prompt, route, and risk are required")
            if not expected.get("must") or not expected.get("must_not"):
                errors.append(f"eval {case.get('id')}: must and must_not are required")
            native_case = case.get("native_claude_case")
            native_root = ROOT / "evals" / "claude" / str(native_case)
            for relative in ("prompt.md", "graders/criteria.md", "graders/skill-fired.md"):
                if not native_case or not (native_root / relative).exists():
                    errors.append(f"eval {case.get('id')}: missing Claude fixture {relative}")
    except (OSError, json.JSONDecodeError) as error:
        errors.append(f"evals/cases.json: {error}")

    prohibited = re.compile(r"\[(?:TODO|PLACEHOLDER):", re.IGNORECASE)
    for path in ROOT.rglob("*"):
        if not path.is_file() or ".git" in path.parts:
            continue
        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        if prohibited.search(text):
            errors.append(f"{path.relative_to(ROOT)}: unresolved placeholder")

    adapter_check = subprocess.run(
        [sys.executable, str(ROOT / "scripts" / "generate_adapters.py"), "--check"],
        cwd=ROOT,
        capture_output=True,
        text=True,
        check=False,
    )
    if adapter_check.returncode != 0:
        errors.append(adapter_check.stderr.strip() or adapter_check.stdout.strip())

    return errors


def main() -> int:
    errors = validate()
    if errors:
        print("validation failed:", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1
    print("validation passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
