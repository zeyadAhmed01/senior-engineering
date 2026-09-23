from __future__ import annotations

import json
from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]


class ContractTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.data = json.loads((ROOT / "evals" / "cases.json").read_text(encoding="utf-8"))
        cls.cases = {case["id"]: case for case in cls.data["cases"]}

    def test_pressure_cases_cover_material_failure_modes(self) -> None:
        self.assertTrue(
            {
                "bug-root-cause",
                "ambiguous-destructive-migration",
                "user-hypothesis",
                "production-2fa-bug",
                "small-ui-padding",
                "whatsapp-report-feature",
                "webhook-duplicate-fulfillment",
                "avoid-overengineering",
                "typo-scope-creep",
                "validate-review-finding",
                "github-ship-ambiguity",
                "force-push-main",
                "github-write-boundary",
                "release-authorization",
                "premature-completion-pressure",
                "untrusted-pr-instructions",
            }.issubset(self.cases)
        )

    def test_every_case_has_a_distinct_claude_fixture(self) -> None:
        native_cases = [case["native_claude_case"] for case in self.data["cases"]]
        self.assertEqual(len(native_cases), len(set(native_cases)))
        for native_case in native_cases:
            root = ROOT / "evals" / "claude" / native_case
            self.assertTrue((root / "prompt.md").is_file())
            self.assertTrue((root / "graders" / "criteria.md").is_file())
            self.assertTrue((root / "graders" / "skill-fired.md").is_file())

    def test_every_case_has_positive_and_negative_contracts(self) -> None:
        for case in self.cases.values():
            expected = case["expected"]
            self.assertIn(expected["risk"], {"low", "medium", "high"})
            self.assertGreaterEqual(len(expected["must"]), 2)
            self.assertGreaterEqual(len(expected["must_not"]), 2)

    def test_external_actions_have_negative_guards(self) -> None:
        github = " ".join(self.cases["github-write-boundary"]["expected"]["must_not"])
        release = " ".join(self.cases["release-authorization"]["expected"]["must_not"])
        self.assertIn("comment", github)
        self.assertIn("release", release)


if __name__ == "__main__":
    unittest.main()
