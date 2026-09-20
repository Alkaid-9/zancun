#!/usr/bin/env python3
"""Text-only Gemini through Claude Code; no global routing/config mutations."""
from __future__ import annotations

import argparse
import hashlib
import json
import os
from pathlib import Path
import re
import signal
import subprocess
import sys
import tempfile

GUARD_DIR = Path(__file__).resolve().parent
REPO = GUARD_DIR.parent.parent
SETTINGS = GUARD_DIR / "settings.json"
CLAUDE = Path("/home/alkaid/miniconda3/envs/solver/bin/claude")
PROVIDER_SETTINGS = Path("/home/alkaid/.claude/settings.json")
MAX_INPUT_BYTES = 65536
MAX_SECONDS = 1200
PROVIDER_KEYS = ("ANTHROPIC_AUTH_TOKEN", "ANTHROPIC_API_KEY", "ANTHROPIC_BASE_URL")


def read_guard() -> tuple[dict, str]:
    settings = json.loads(SETTINGS.read_text(encoding="utf-8"))
    permissions = settings.get("permissions", {})
    if permissions.get("defaultMode") != "dontAsk" or permissions.get("allow") != []:
        raise ValueError("invalid guard permission mode/allow list")
    if permissions.get("disableBypassPermissionsMode") != "disable":
        raise ValueError("bypass mode must be disabled")
    if not set(["Bash", "Read", "Write", "Edit", "Agent", "mcp__*"]).issubset(permissions.get("deny", [])):
        raise ValueError("guard deny list incomplete")
    if settings.get("disableAllHooks") is not True or settings.get("enabledPlugins") != {}:
        raise ValueError("customizations must be disabled")
    policy = (REPO / "GEMINI.md").read_text(encoding="utf-8")
    return settings, policy


def resolve_provider(override: str | None) -> tuple[str, dict[str, str]]:
    data = json.loads(PROVIDER_SETTINGS.read_text(encoding="utf-8"))
    configured = data.get("env", {})
    model = override or configured.get("ANTHROPIC_DEFAULT_HAIKU_MODEL", "")
    # Use the explicit upstream identifier, never fable/opus/sonnet/haiku aliases.
    if not isinstance(model, str) or not re.fullmatch(r"[A-Za-z0-9._/-]*gemini[A-Za-z0-9._/\[\]-]*", model):
        raise ValueError("explicit Gemini model ID required; aliases and non-Gemini models rejected")
    provider = {k: configured[k] for k in PROVIDER_KEYS if isinstance(configured.get(k), str) and configured[k]}
    if not provider.get("ANTHROPIC_BASE_URL") or not (provider.get("ANTHROPIC_AUTH_TOKEN") or provider.get("ANTHROPIC_API_KEY")):
        raise ValueError("configured provider endpoint and credential required")
    return model, provider


def validate_prompt(prompt: str) -> None:
    if not prompt.strip() or len(prompt.encode("utf-8")) > MAX_INPUT_BYTES:
        raise ValueError("task must contain 1..65536 UTF-8 bytes")
    # @file expansion is client-side and can happen without a Read tool call.
    if re.search(r"(?:^|\s)@\S", prompt):
        raise ValueError("@ references/decorators are rejected: paste escaped literal content, not client file references")
    if prompt.lstrip().startswith("/"):
        raise ValueError("slash commands are not task input")


def build_command(model: str, settings: dict, policy: str) -> list[str]:
    return [
        str(CLAUDE), "--print", "--safe-mode", "--tools", "",
        "--strict-mcp-config", "--mcp-config", '{"mcpServers":{}}',
        "--setting-sources", "", "--settings", json.dumps(settings),
        "--disable-slash-commands", "--no-chrome", "--no-session-persistence",
        "--permission-mode", "dontAsk", "--model", model, "--effort", "low",
        "--max-turns", "1", "--output-format", "json", "--system-prompt", policy,
    ]


def child_environment(provider: dict[str, str], config_dir: Path) -> dict[str, str]:
    # Strip inherited model/permission/agent/proxy-client overrides; keep normal OS env.
    env = {k: v for k, v in os.environ.items()
           if not (k.startswith("ANTHROPIC_") or k.startswith("CLAUDE_") or k == "CLAUDECODE")}
    env.update(provider)
    env.update({
        "CLAUDE_CONFIG_DIR": str(config_dir),
        "CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC": "1",
        "DISABLE_AUTOUPDATER": "1",
        "API_TIMEOUT_MS": "60000",
    })
    return env


def execute(prompt: str, model: str, provider: dict[str, str], settings: dict, policy: str,
            timeout: int = MAX_SECONDS) -> dict:
    validate_prompt(prompt)
    with tempfile.TemporaryDirectory(prefix="claude-gemini-worker-") as directory:
        scratch = Path(directory)
        config_dir = scratch / "config"
        config_dir.mkdir(mode=0o700)
        command = build_command(model, settings, policy)
        process = subprocess.Popen(command, cwd=scratch, env=child_environment(provider, config_dir),
                                   stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                                   text=True, start_new_session=True)
        try:
            stdout, stderr = process.communicate(prompt, timeout=timeout)
        except (subprocess.TimeoutExpired, KeyboardInterrupt):
            os.killpg(process.pid, signal.SIGTERM)
            try:
                process.communicate(timeout=5)
            except subprocess.TimeoutExpired:
                os.killpg(process.pid, signal.SIGKILL)
                process.communicate()
            raise ValueError("worker stopped; process group terminated; no retry or session resume") from None
        # Do not echo raw diagnostics: provider errors can contain credentials/URLs.
        if process.returncode:
            raise ValueError(f"Claude Code exited {process.returncode}; no result accepted (diagnostics withheld)")
        try:
            result = json.loads(stdout)
        except json.JSONDecodeError:
            raise ValueError("invalid Claude Code JSON response; no result accepted") from None
        if result.get("is_error") or result.get("subtype") != "success":
            raise ValueError("Claude Code returned an unsuccessful task; no result accepted")
        return {
            "status": "DRAFT", "model_requested": model,
            "task_sha256": hashlib.sha256(prompt.encode()).hexdigest(),
            "tools": [], "mcp_servers": [],
            "session_id": result.get("session_id"),
            "candidate": result.get("result", ""),
            "usage": result.get("usage"),
            "limitations": "Candidate only. Tool-less Claude Code session, not an OS sandbox or factual verification.",
        }


def main() -> int:
    parser = argparse.ArgumentParser(description="Gemini short text task with no Claude Code tools or MCP")
    parser.add_argument("--model", help="Explicit configured Gemini upstream ID, not an alias")
    parser.add_argument("--check", action="store_true", help="Validate local config only; no model request")
    args = parser.parse_args()
    try:
        settings, policy = read_guard()
        model, provider = resolve_provider(args.model)
        if args.check:
            print(json.dumps({"configuration": "VALID", "model_requested": model,
                              "builtin_tools": [], "mcp_servers": [], "hooks": False,
                              "plugins": False, "session_resume": False,
                              "global_settings_modified": False,
                              "note": "Configuration check, not a live model test"}, ensure_ascii=False))
            return 0
        if sys.stdin.isatty():
            raise ValueError("pass the frozen task and source text through stdin; no interactive/resume mode")
        raw = sys.stdin.buffer.read(MAX_INPUT_BYTES + 1)
        prompt = raw.decode("utf-8")
        print(json.dumps(execute(prompt, model, provider, settings, policy), ensure_ascii=False, indent=2))
        return 0
    except (OSError, UnicodeError, ValueError, KeyError) as error:
        print(f"BLOCKED: {error}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
