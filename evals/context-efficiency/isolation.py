"""Build a minimal environment for sandboxed installed-plugin evaluations."""

from __future__ import annotations

import os
import tomllib
from pathlib import Path


PERMISSION_PROFILE = "se-eval-workspace"
SANDBOX_MODE = f"permission-profile:{PERMISSION_PROFILE}"
EVAL_DISABLED_FEATURES = ("apps", "remote_plugin")
ALLOWED_ENVIRONMENT_KEYS = frozenset(
    {
        "APPDATA",
        "COMSPEC",
        "HOMEDRIVE",
        "HOMEPATH",
        "LOCALAPPDATA",
        "PATH",
        "PATHEXT",
        "SYSTEMROOT",
        "TEMP",
        "TMP",
        "USERPROFILE",
        "WINDIR",
    }
)


def eval_disabled_feature_args() -> list[str]:
    """Disable account integrations while keeping the local test plugin active."""
    return [argument for feature in EVAL_DISABLED_FEATURES for argument in ("--disable", feature)]


def validate_codex_home(
    codex_home: Path,
    fixture: Path,
    *,
    user_home: Path,
    evaluation_root: Path,
    temp_root: Path,
) -> None:
    """Require a dedicated CODEX_HOME outside private data, fixtures, and temp."""
    home = codex_home.resolve()
    fixture_root = fixture.resolve()
    private_codex_root = (user_home / ".codex").resolve()
    private_evaluation_root = evaluation_root.resolve()
    temporary_root = temp_root.resolve()

    if home == private_codex_root or home.is_relative_to(private_codex_root):
        raise ValueError("CODEX_HOME must be separate from the user's private .codex directory")
    if home == private_evaluation_root or not home.is_relative_to(private_evaluation_root):
        raise ValueError("CODEX_HOME must be a dedicated subdirectory of the evaluation-only root")
    if home.is_relative_to(temporary_root):
        raise ValueError("CODEX_HOME must not be stored under a sandbox-writable temporary directory")
    if home == fixture_root or home.is_relative_to(fixture_root) or fixture_root.is_relative_to(home):
        raise ValueError("CODEX_HOME and the disposable fixture must be separate trees")


def validate_codex_permissions(codex_home: Path, *, user_home: Path) -> None:
    """Require fixture writes, no command network, and blocked credential stores."""
    config_path = codex_home / "config.toml"
    if not config_path.is_file():
        raise ValueError("The isolated CODEX_HOME must define its sandbox permission profile")

    configuration = tomllib.loads(config_path.read_text(encoding="utf-8-sig"))
    if configuration.get("default_permissions") != PERMISSION_PROFILE:
        raise ValueError("The isolated Codex home must select the evaluation permission profile")
    if configuration.get("windows", {}).get("sandbox") != "elevated":
        raise ValueError("Native Windows behavioral evaluations require the elevated sandbox backend")

    profile = configuration.get("permissions", {}).get(PERMISSION_PROFILE, {})
    filesystem = profile.get("filesystem", {})
    workspace_roots = filesystem.get(":workspace_roots", {})
    network = profile.get("network", {})
    protected_codex_home = str((user_home / ".codex").resolve()).replace("\\", "/").casefold()
    protected_eval_auth = str((codex_home / "auth.json").resolve()).replace("\\", "/").casefold()
    denied_paths = {
        str(path).replace("\\", "/").casefold(): access
        for path, access in filesystem.items()
        if not str(path).startswith(":")
    }

    if profile.get("extends") != ":workspace":
        raise ValueError("The evaluation permission profile must extend Codex's workspace profile")
    if filesystem.get(":root") != "read" or filesystem.get(":minimal") != "read":
        raise ValueError("The native Windows permission profile must retain required root and toolchain reads")
    if denied_paths.get(protected_codex_home) != "deny":
        raise ValueError("The evaluation permission profile must deny reads from the user's .codex directory")
    if denied_paths.get(protected_eval_auth) != "deny":
        raise ValueError("The evaluation permission profile must deny reads from its authentication file")
    if workspace_roots.get(".") != "write":
        raise ValueError("The evaluation permission profile must allow writes through the active workspace root")
    if network.get("enabled") is not False:
        raise ValueError("Command networking must be disabled during behavioral evaluations")


def build_codex_environment(
    source_environment: dict[str, str],
    *,
    codex_home: Path,
    trace_root: Path,
    path_prefix: Path | None = None,
) -> dict[str, str]:
    """Return a Windows process environment that omits inherited credentials."""
    environment = {
        key: source_environment[key]
        for key in ALLOWED_ENVIRONMENT_KEYS
        if key in source_environment
    }
    if not environment.get("PATH"):
        raise ValueError("PATH is required to start Codex and fixture tools")

    if path_prefix is not None:
        environment["PATH"] = str(path_prefix) + os.pathsep + environment["PATH"]

    environment.update(
        {
            "CODEX_HOME": str(codex_home),
            "GH_CONFIG_DIR": str(trace_root / "empty-gh-config"),
            "GIT_CONFIG_GLOBAL": str(trace_root / "empty-gitconfig"),
            "GIT_CONFIG_NOSYSTEM": "1",
            "PYTHONDONTWRITEBYTECODE": "1",
            "PYTHONPYCACHEPREFIX": str(trace_root / "python-cache"),
        }
    )
    return environment
