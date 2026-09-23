from __future__ import annotations

import json
from pathlib import Path
import subprocess
import sys
import tempfile
import tomllib
import unittest

from scripts.generate_adapters import expected_files, find_orphans


ROOT = Path(__file__).resolve().parents[1]


class AdapterTests(unittest.TestCase):
    def test_generated_adapters_are_current(self) -> None:
        result = subprocess.run(
            [sys.executable, str(ROOT / "scripts" / "generate_adapters.py"), "--check"],
            cwd=ROOT,
            capture_output=True,
            text=True,
            check=False,
        )
        self.assertEqual(result.returncode, 0, result.stderr)

    def test_runtime_manifests_match_canonical_identity(self) -> None:
        canonical = json.loads((ROOT / "plugin.json").read_text(encoding="utf-8"))
        for path in (ROOT / ".codex-plugin" / "plugin.json",):
            adapter = json.loads(path.read_text(encoding="utf-8"))
            for field in ("name", "version", "description", "author", "license"):
                self.assertEqual(adapter[field], canonical[field], f"{path}: {field}")

    def test_portable_manifest_uses_openai_extension(self) -> None:
        manifest = json.loads((ROOT / "plugin.json").read_text(encoding="utf-8"))
        self.assertEqual(manifest["version"], "1.0.0")
        self.assertEqual(
            manifest["$schema"],
            "https://agent-plugins.org/schemas/1.0.0/plugin.schema.json",
        )
        self.assertNotIn("skills", manifest)
        self.assertNotIn("interface", manifest)
        self.assertIn("interface", manifest["extensions"]["com.openai"])

    def test_codex_agent_adapters_are_read_only(self) -> None:
        paths = sorted((ROOT / ".codex" / "agents").glob("*.toml"))
        self.assertEqual(len(paths), 4)
        for path in paths:
            data = tomllib.loads(path.read_text(encoding="utf-8"))
            self.assertEqual(data["name"], path.stem)
            self.assertEqual(data["sandbox_mode"], "read-only")
            self.assertTrue(data["description"])
            self.assertTrue(data["developer_instructions"])

    def test_release_contains_only_codex_adapter_surfaces(self) -> None:
        unsupported_surfaces = (
            ROOT / ".claude-plugin",
            ROOT / "CLAUDE.md",
            ROOT / "dist" / "claude",
            ROOT / "evals" / "claude",
        )
        self.assertEqual([path for path in unsupported_surfaces if path.exists()], [])
        generated = expected_files()
        self.assertTrue(generated)
        self.assertTrue(all("claude" not in path.as_posix().lower() for path in generated))

    def test_orphan_detection_catches_stale_generated_files(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            expected = root / ".codex" / "agents" / "expected.toml"
            orphans = [
                root / ".codex" / "agents" / "old-name.toml",
                root / ".codex-plugin" / "unexpected.json",
            ]
            expected.parent.mkdir(parents=True)
            expected.write_text("expected", encoding="utf-8")
            for orphan in orphans:
                orphan.parent.mkdir(parents=True, exist_ok=True)
                orphan.write_text("orphan", encoding="utf-8")
            self.assertEqual(find_orphans({expected}, root), sorted(orphans))


if __name__ == "__main__":
    unittest.main()
