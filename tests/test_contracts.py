from __future__ import annotations

import importlib.util
import json
from pathlib import Path
import runpy
import sys
import tempfile
import unittest


ROOT = Path(__file__).resolve().parents[1]
ISOLATION_PATH = ROOT / "evals" / "context-efficiency" / "isolation.py"
ISOLATION_SPEC = importlib.util.spec_from_file_location("eval_isolation", ISOLATION_PATH)
if ISOLATION_SPEC is None or ISOLATION_SPEC.loader is None:
    raise RuntimeError("Could not load evaluation isolation policy")
ISOLATION = importlib.util.module_from_spec(ISOLATION_SPEC)
ISOLATION_SPEC.loader.exec_module(ISOLATION)
RUNNER_DIR = ROOT / "evals" / "context-efficiency"
sys.path.insert(0, str(RUNNER_DIR))
try:
    CONTRACT_RUNNER = runpy.run_path(str(RUNNER_DIR / "run_contract_suite.py"), run_name="contract_runner")
finally:
    sys.path.remove(str(RUNNER_DIR))


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
                "design-material-flow",
                "design-reference-boundary",
                "github-mcp-scope",
                "context-budget-small-task",
                "unnecessary-delegation",
                "design-system-conflict",
                "marketing-design-routing",
                "design-reference-fallback",
                "visual-verification-integrity",
            }.issubset(self.cases)
        )

    def test_evaluation_contracts_are_platform_neutral(self) -> None:
        for case in self.data["cases"]:
            self.assertFalse(
                any("claude" in key.lower() for key in case),
                f"{case['id']} contains retired platform metadata",
            )

    def test_evaluation_disables_account_integrations_but_keeps_local_plugins(self) -> None:
        self.assertEqual(
            ISOLATION.eval_disabled_feature_args(),
            ["--disable", "apps", "--disable", "remote_plugin"],
        )

    def test_contract_runner_records_supported_reasoning_effort(self) -> None:
        self.assertEqual(
            CONTRACT_RUNNER["reasoning_effort_args"]("low"),
            ["-c", 'model_reasoning_effort="low"'],
        )
        with self.assertRaises(ValueError):
            CONTRACT_RUNNER["reasoning_effort_args"]("unrecognized")

    def test_every_current_contract_has_a_disposable_fixture(self) -> None:
        seed = CONTRACT_RUNNER["seed"]
        for case_id in self.cases:
            with self.subTest(case=case_id):
                self.assertIsInstance(seed(case_id), dict)

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

    def test_explicit_only_cases_invoke_the_named_skill(self) -> None:
        self.assertIn("$senior-engineering:refine", self.cases["refine-without-execute"]["prompt"])
        self.assertIn("$senior-engineering:release", self.cases["release-authorization"]["prompt"])

    def test_runner_marks_fixture_boundary_as_not_part_of_refined_prompt(self) -> None:
        prompt = CONTRACT_RUNNER["task_prompt_for"](
            {"prompt": "Use $senior-engineering:refine. Add search."}
        )
        self.assertIn("not part of the user's request", prompt)
        self.assertIn("not content to copy into a refined prompt", prompt)
        self.assertTrue(prompt.endswith("Use $senior-engineering:refine. Add search."))

    def test_prompt_refinement_cases_cover_requested_inputs_and_boundaries(self) -> None:
        expected_ids = {
            "prompt-refine-vague-feature",
            "prompt-refine-detailed-implementation",
            "prompt-refine-bug-report",
            "prompt-refine-refactor",
            "prompt-refine-ui-restyle",
            "prompt-refine-performance",
            "prompt-refine-security-auth",
            "prompt-refine-failing-tests",
            "prompt-refine-laravel-backend",
            "prompt-refine-frontend",
            "prompt-refine-payment-idempotency",
            "prompt-refine-destructive-migration",
            "prompt-refine-concurrency",
            "prompt-refine-already-good",
        }
        self.assertTrue(expected_ids.issubset(self.cases))
        for case_id in expected_ids:
            with self.subTest(case=case_id):
                case = self.cases[case_id]
                self.assertEqual(case["category"], "prompt-refinement")
                self.assertEqual(case["expected"]["route"], "refine")
                self.assertIn("$senior-engineering:refine", case["prompt"])
                self.assertTrue(case["expected"]["must"])
                self.assertTrue(case["expected"]["must_not"])
        clear_prompt = " ".join(self.cases["prompt-refine-already-good"]["expected"]["must_not"])
        self.assertIn("extra acceptance criteria", clear_prompt)

    def test_design_and_github_cases_cover_the_new_architecture_boundaries(self) -> None:
        design = " ".join(self.cases["design-material-flow"]["expected"]["must"])
        references = " ".join(self.cases["design-reference-boundary"]["expected"]["must_not"])
        github = " ".join(self.cases["github-mcp-scope"]["expected"]["must"])
        context = " ".join(self.cases["context-budget-small-task"]["expected"]["must"])
        design_system = " ".join(self.cases["design-system-conflict"]["expected"]["must"])
        delegation = " ".join(self.cases["unnecessary-delegation"]["expected"]["must"])
        marketing = " ".join(self.cases["marketing-design-routing"]["expected"]["must"])
        fallback = " ".join(self.cases["design-reference-fallback"]["expected"]["must"])
        visual_verification = " ".join(self.cases["visual-verification-integrity"]["expected"]["must"])
        self.assertIn("Design Contract", design)
        self.assertIn("copy", references)
        self.assertIn("read-only", github)
        self.assertIn("focused check", context)
        self.assertIn("authoritative constraints", design_system)
        self.assertIn("not independently separable", delegation)
        self.assertIn("Dribbble", marketing)
        self.assertIn("Pinterest", fallback)
        self.assertIn("unproven", visual_verification)

    def test_evaluation_sandbox_and_environment_are_restricted(self) -> None:
        self.assertEqual(ISOLATION.SANDBOX_MODE, "permission-profile:se-eval-workspace")
        environment = ISOLATION.build_codex_environment(
            {
                "PATH": "C:/Windows/System32",
                "SYSTEMROOT": "C:/Windows",
                "USERPROFILE": "C:/Users/Eval",
                "OPENAI_API_KEY": "must-not-pass",
                "GH_TOKEN": "must-not-pass",
            },
            codex_home=Path("C:/Users/Eval/.codex/se-eval"),
            trace_root=Path("C:/Users/Eval/.codex/se-eval/traces"),
        )
        self.assertNotIn("OPENAI_API_KEY", environment)
        self.assertNotIn("GH_TOKEN", environment)

    def test_permission_profile_denies_codex_home_and_command_network(self) -> None:
        with tempfile.TemporaryDirectory() as temporary_directory:
            user_home = Path(temporary_directory) / "user"
            evaluation_root = Path(temporary_directory) / "local-app-data" / "CodexEval"
            codex_home = evaluation_root / "eval"
            codex_home.mkdir(parents=True)
            protected_home = json.dumps(str(user_home / ".codex").replace("\\", "/"))
            protected_auth = json.dumps(str(codex_home / "auth.json").replace("\\", "/"))
            config = (
                'default_permissions = "se-eval-workspace"\n'
                "\n[windows]\nsandbox = \"elevated\"\n"
                "\n[permissions]\n"
                "\n[permissions.se-eval-workspace]\nextends = \":workspace\"\n"
                "\n[permissions.se-eval-workspace.filesystem]\n"
                "\":root\" = \"read\"\n\":minimal\" = \"read\"\n"
                f"{protected_home} = \"deny\"\n"
                f"{protected_auth} = \"deny\"\n"
                "\n[permissions.se-eval-workspace.filesystem.\":workspace_roots\"]\n"
                "\".\" = \"write\"\n"
                "\n[permissions.se-eval-workspace.network]\nenabled = false\n"
            )
            config_path = codex_home / "config.toml"
            config_path.write_text(config, encoding="utf-8")

            ISOLATION.validate_codex_permissions(codex_home, user_home=user_home)

            config_path.write_text(config.replace('"deny"', '"read"'), encoding="utf-8")
            with self.assertRaises(ValueError):
                ISOLATION.validate_codex_permissions(codex_home, user_home=user_home)

    def test_eval_codex_home_is_separate_from_private_home_and_temp(self) -> None:
        evaluation_root = Path("C:/Users/Eval/AppData/Local/CodexEval")
        with tempfile.TemporaryDirectory() as temporary_directory:
            fixture = Path(temporary_directory) / "fixture"
            valid_home = evaluation_root / "test"
            ISOLATION.validate_codex_home(
                valid_home,
                fixture,
                user_home=Path("C:/Users/Eval"),
                evaluation_root=evaluation_root,
                temp_root=Path("C:/Temp"),
            )
        with self.assertRaises(ValueError):
            ISOLATION.validate_codex_home(
                Path("C:/Temp/eval-home"),
                Path("C:/Temp/fixture"),
                user_home=Path("C:/Users/Eval"),
                evaluation_root=evaluation_root,
                temp_root=Path("C:/Temp"),
            )
        with self.assertRaises(ValueError):
            ISOLATION.validate_codex_home(
                Path("C:/Users/Eval/.codex/eval"),
                Path("C:/Temp/fixture"),
                user_home=Path("C:/Users/Eval"),
                evaluation_root=evaluation_root,
                temp_root=Path("C:/Temp"),
            )

    def test_natural_pr_review_routing_case_exists_without_skill_override(self) -> None:
        case = self.cases["natural-pr-code-review"]
        self.assertNotIn("$senior-engineering:", case["prompt"])
        self.assertIn("local diff", case["prompt"].lower())


if __name__ == "__main__":
    unittest.main()
