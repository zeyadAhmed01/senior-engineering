#!/usr/bin/env python3
"""Run independent installed-plugin Codex evaluations in disposable Git fixtures."""

from __future__ import annotations

import argparse
import json
import os
from pathlib import Path
import re
import subprocess
import tempfile
from isolation import (
    PERMISSION_PROFILE,
    SANDBOX_MODE,
    build_codex_environment,
    eval_disabled_feature_args,
    validate_codex_home,
    validate_codex_permissions,
)


CASES = {
    "trivial-ui": {
        "files": {
            "button.css": ".action-button { padding: 8px; }\n",
            "test_button.py": "from pathlib import Path\nassert 'padding: 12px' in Path('button.css').read_text()\n",
        },
        "prompt": "Use $senior-engineering:engineer. Change only the action button padding from 8px to 12px in this disposable fixture. Run the focused check and report the result.",
    },
    "standard-feature": {
        "files": {
            "catalog.py": "def filter_items(items, category=None):\n    return [item for item in items if category is None or item['category'] == category]\n",
            "test_catalog.py": "import unittest\nfrom catalog import filter_items\n\nclass CatalogTest(unittest.TestCase):\n    def test_minimum_price(self):\n        items = [{'category': 'book', 'price': 5}, {'category': 'book', 'price': 20}, {'category': 'pen', 'price': 30}]\n        self.assertEqual(filter_items(items, category='book', min_price=10), [items[1]])\n        self.assertEqual(filter_items(items), items)\n",
        },
        "prompt": "Use $senior-engineering:engineer to add an optional min_price filter to this small catalog function, preserving the existing category behavior. Run the focused test and inspect the final diff. Work only in this disposable fixture.",
    },
    "search-bug": {
        "files": {
            "search.py": "def search(names, term):\n    matches = [name for name in names if term.lower() in name.lower()]\n    return sorted(matches)\n",
            "test_search.py": "import unittest\nfrom search import search\n\nclass SearchTest(unittest.TestCase):\n    def test_prefix_precedes_substring(self):\n        self.assertEqual(search(['Alpha', 'Calpaca', 'Alpine'], 'alp'), ['Alpha', 'Alpine', 'Calpaca'])\n",
        },
        "prompt": "Use $senior-engineering:engineer to fix this search-order bug. Reproduce the defect, trace root cause, implement the smallest fix, and run the focused test. Work only in this disposable fixture.",
    },
    "natural-route": {
        "files": {
            "search.py": "def search(names, term):\n    matches = [name for name in names if term.lower() in name.lower()]\n    return sorted(matches)\n",
            "test_search.py": "import unittest\nfrom search import search\n\nclass SearchTest(unittest.TestCase):\n    def test_prefix_precedes_substring(self):\n        self.assertEqual(search(['Alpha', 'Calpaca', 'Alpine'], 'alp'), ['Alpha', 'Alpine', 'Calpaca'])\n",
        },
        "prompt": "Search results put substring matches before prefix matches. Find the cause, fix it in this disposable fixture, and verify the change.",
    },
    "production-bug": {
        "files": {
            "settings.py": "import os\n\ndef asset_url(path, environment='local'):\n    if environment == 'production':\n        return os.environ['PUBLIC_ASSET_URL'].rstrip('/') + '/' + path.lstrip('/')\n    return 'http://localhost/assets/' + path.lstrip('/')\n",
            "test_settings.py": "import os\nimport unittest\nfrom unittest.mock import patch\nfrom settings import asset_url\n\nclass SettingsTest(unittest.TestCase):\n    def test_production_falls_back_to_canonical_host_when_asset_host_is_missing(self):\n        with patch.dict(os.environ, {'APP_URL': 'https://class.example'}, clear=True):\n            self.assertEqual(asset_url('/logo.png', 'production'), 'https://class.example/assets/logo.png')\n",
        },
        "prompt": "Use $senior-engineering:engineer to investigate this production-only asset URL bug. Establish the environment-specific cause before fixing it; preserve configured PUBLIC_ASSET_URL behavior. Run focused checks and state what real production remains unproven. Work only in this disposable fixture.",
    },
    "payment-concurrency": {
        "files": {
            "payments.py": "class Fulfillment:\n    def __init__(self):\n        self.fulfilled = []\n\n    def handle(self, event_id, order_id):\n        self.fulfilled.append(order_id)\n",
            "test_payments.py": "import unittest\nfrom payments import Fulfillment\n\nclass PaymentTest(unittest.TestCase):\n    def test_duplicate_event_fulfills_once(self):\n        service = Fulfillment()\n        service.handle('evt-1', 'order-1')\n        service.handle('evt-1', 'order-1')\n        self.assertEqual(service.fulfilled, ['order-1'])\n",
        },
        "prompt": "Use $senior-engineering:engineer. A duplicate payment webhook can fulfill an order twice. This is a simplified in-memory fixture, so do not claim production durability. Reproduce, inspect idempotency and concurrency implications, make a narrow fix, run the test, and report remaining durable-boundary risks. Work only here.",
    },
    "noisy-success": {
        "files": {
            "test_noisy.py": "import unittest\n\nclass NoisyTest(unittest.TestCase):\n    def test_passes(self):\n        for i in range(180):\n            print(f'progress {i}: successful assertion detail')\n        self.assertTrue(True)\n",
        },
        "prompt": "Use $senior-engineering:engineer to verify the existing noisy test suite in this fixture. Choose compact or raw command output based on its usefulness, report exact result and evidence, and do not edit code.",
    },
    "long-task": {
        "files": {
            "README.md": "# Small classroom tool\nPhase 1: inspect attendance input. Phase 2: design duplicate handling. Phase 3: implement. Phase 4: review. Phase 5: verify. Work resumes tomorrow after Phase 1.\n",
            "attendance.py": "def record_attendance(student_ids):\n    return list(student_ids)\n",
        },
        "prompt": "Use $senior-engineering:engineer. This is a long research-design-implementation-review-verification assignment that will resume tomorrow. Complete only Phase 1: inspect current attendance behavior and establish a compact durable continuation state in this disposable fixture. Do not implement later phases or claim their tests passed. Explain the next action.",
    },
    "noisy-failure": {
        "files": {
            "test_noisy.py": "import unittest\n\nclass NoisyTest(unittest.TestCase):\n    def test_specific_failure(self):\n        for i in range(180):\n            print(f'progress {i}: unrelated successful detail')\n        self.assertEqual('prefix', 'substring', 'ranking kind mismatch')\n",
        },
        "prompt": "Use $senior-engineering:engineer to diagnose the failing noisy test suite in this fixture without editing code. First run it through the installed released RTK compact test command, then obtain recalled or focused raw output if the compact view omits the failed test name or diagnostics. Report exact evidence and exit status.",
    },
    "negligible-rtk": {
        "files": {"config.txt": "mode=local\n"},
        "prompt": "Use $senior-engineering:engineer to confirm the exact mode in config.txt, using a bounded read or search. Selective RTK is available, but use it only if it materially reduces output. Do not edit files.",
    },
    "payment-pressure": {
        "files": {
            "payments.py": "class Fulfillment:\n    def __init__(self):\n        self.fulfilled = []\n\n    def handle(self, event_id, order_id):\n        self.fulfilled.append(order_id)\n",
            "test_payments.py": "import unittest\nfrom payments import Fulfillment\n\nclass PaymentTest(unittest.TestCase):\n    def test_duplicate_event_fulfills_once(self):\n        service = Fulfillment()\n        service.handle('evt-1', 'order-1')\n        service.handle('evt-1', 'order-1')\n        self.assertEqual(service.fulfilled, ['order-1'])\n",
        },
        "prompt": "Use $senior-engineering:engineer. Don't waste tokens investigating everything. Just make the payment fix and keep it short. A duplicate payment webhook may fulfill an order twice in this simplified fixture. Preserve required idempotency/concurrency/security investigation, relevant tests, adversarial review, and verification. Do not claim production durability from this fake. Work only here.",
    },
}


def codex_version() -> str:
    result = subprocess.run(
        ["codex", "--version"], capture_output=True, text=True, check=False
    )
    if result.returncode != 0:
        return "unavailable"
    return result.stdout.strip() or "unavailable"


def run_case(case_id: str, root: Path, model: str, rtk_dir: Path, codex_home: Path, timeout_seconds: int, marketplace_name: str) -> dict[str, object]:
    case = CASES[case_id]
    fixture = root / case_id
    fixture.mkdir(parents=True, exist_ok=False)
    for name, content in case["files"].items():
        (fixture / name).write_text(content, encoding="utf-8")
    subprocess.run(["git", "init", "-q", str(fixture)], check=True, capture_output=True)
    subprocess.run(["git", "-C", str(fixture), "add", "."], check=True, capture_output=True)
    subprocess.run(["git", "-C", str(fixture), "-c", "user.name=Eval", "-c", "user.email=eval@example.invalid", "commit", "-qm", "fixture baseline"], check=True, capture_output=True)
    traces = root.parent / f"{root.name}-traces"
    traces.mkdir(parents=True, exist_ok=True)
    output = traces / f"{case_id}.jsonl"
    final = traces / f"{case_id}.final.txt"
    validate_codex_home(
        codex_home,
        fixture,
        user_home=Path(os.environ.get("USERPROFILE", Path.home())),
        evaluation_root=Path(os.environ.get("LOCALAPPDATA", Path.home() / "AppData" / "Local")) / "CodexEval",
        temp_root=Path(tempfile.gettempdir()),
    )
    validate_codex_permissions(codex_home, user_home=Path(os.environ.get("USERPROFILE", Path.home())))
    env = build_codex_environment(
        dict(os.environ),
        codex_home=codex_home,
        trace_root=traces,
        path_prefix=rtk_dir,
    )
    command = ["codex", "exec", "--json", "--ephemeral", "--skip-git-repo-check", *eval_disabled_feature_args(), "-m", model, "-c", 'approval_policy="never"', "-c", 'model_reasoning_effort="medium"', "-C", str(fixture), "-o", str(final), str(case["prompt"])]
    with output.open("wb") as stream:
        try:
            result = subprocess.run(command, stdin=subprocess.DEVNULL, stdout=stream, stderr=subprocess.STDOUT, env=env, timeout=timeout_seconds, check=False)
            exit_code = result.returncode
        except subprocess.TimeoutExpired:
            exit_code = 124
    text = output.read_text(encoding="utf-8", errors="replace")
    usage = []
    command_count = 0
    command_output_chars = 0
    for line in text.splitlines():
        try:
            event = json.loads(line)
        except json.JSONDecodeError:
            continue
        if not isinstance(event, dict):
            continue
        if event.get("type") == "turn.completed" and "usage" in event:
            usage.append(event["usage"])
        item = event.get("item", {})
        if event.get("type") == "item.completed" and item.get("type") == "command_execution":
            command_count += 1
            command_output_chars += len(item.get("aggregated_output", ""))
    summary = {
        "case": case_id,
        "exit_code": exit_code,
        "fixture": str(fixture),
        "log_path": str(output),
        "final_path": str(final),
        "log_bytes": output.stat().st_size,
        "codex_version": codex_version(),
        "model_requested": model,
        "reasoning_requested": "medium",
        "permission_profile": PERMISSION_PROFILE,
        "sandbox_mode": SANDBOX_MODE,
        "installed_plugin_path_seen": marketplace_name in text,
        "installed_skills_read": sorted(
            {
                match.group(1).lower()
                for match in re.finditer(
                    rf"plugins[/\\]+cache[/\\]+{re.escape(marketplace_name)}[/\\]+senior-engineering[/\\]+0\.1\.0[/\\]+skills[/\\]+([^/\\]+)[/\\]+SKILL\.md",
                    text,
                    flags=re.IGNORECASE,
                )
            }
        ),
        "command_count": command_count,
        "command_output_chars": command_output_chars,
        "usage": usage[-1] if usage else None,
        "rtk_mentions": text.lower().count("rtk"),
        "final": final.read_text(encoding="utf-8", errors="replace") if final.exists() else "",
    }
    (fixture / "summary.json").write_text(json.dumps(summary, indent=2), encoding="utf-8")
    return summary


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("case", choices=sorted(CASES))
    parser.add_argument("--root", type=Path, default=Path(tempfile.gettempdir()) / "se-v100-context")
    parser.add_argument("--model", default="gpt-5.6-sol")
    parser.add_argument("--rtk-dir", type=Path, required=True)
    parser.add_argument("--codex-home", type=Path, required=True)
    parser.add_argument("--timeout-seconds", type=int, default=900)
    parser.add_argument("--marketplace-name", default="se-v100-release-eval")
    args = parser.parse_args()
    args.root.mkdir(parents=True, exist_ok=True)
    result = run_case(args.case, args.root, args.model, args.rtk_dir, args.codex_home, args.timeout_seconds, args.marketplace_name)
    print(json.dumps({key: value for key, value in result.items() if key != "final"}, indent=2))


if __name__ == "__main__":
    main()
