"""Local tests use the actual Claude Code binary and a loopback fake provider.

The fake model deliberately emits unauthorized tool_use requests; it is not
evidence about Gemini model quality and makes no paid provider requests.
"""
from __future__ import annotations

from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
import importlib.util
import json
from pathlib import Path
import tempfile
import threading
import unittest
from urllib.parse import urlsplit

SPEC = importlib.util.spec_from_file_location("guard_worker", Path(__file__).with_name("worker.py"))
worker = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(worker)


class Endpoint:
    def __init__(self, tool: str | None = None, args: dict | None = None):
        self.requests = []
        outer = self

        class Handler(BaseHTTPRequestHandler):
            def log_message(self, *args):
                pass

            def do_POST(self):
                body = json.loads(self.rfile.read(int(self.headers.get("Content-Length", "0"))))
                outer.requests.append((self.path, body))
                if "count_tokens" in self.path:
                    payload = {"input_tokens": 32}
                elif tool:
                    payload = {"id": "msg_guard", "type": "message", "role": "assistant",
                               "model": "gemini-test", "content": [{"type": "tool_use", "id": "tool_guard",
                               "name": tool, "input": args or {}}], "stop_reason": "tool_use",
                               "stop_sequence": None, "usage": {"input_tokens": 32, "output_tokens": 8}}
                else:
                    payload = {"id": "msg_guard", "type": "message", "role": "assistant",
                               "model": "gemini-test", "content": [{"type": "text", "text": "DRAFT: fixture only"}],
                               "stop_reason": "end_turn", "stop_sequence": None,
                               "usage": {"input_tokens": 32, "output_tokens": 8}}
                if body.get("stream") and "count_tokens" not in self.path:
                    self.send_response(200)
                    self.send_header("Content-Type", "text/event-stream")
                    self.end_headers()
                    content = payload["content"][0]
                    start = dict(payload, content=[])
                    start["stop_reason"] = None
                    events = [("message_start", {"type": "message_start", "message": start})]
                    if content["type"] == "text":
                        events += [("content_block_start", {"type": "content_block_start", "index": 0,
                                   "content_block": {"type": "text", "text": ""}}),
                                   ("content_block_delta", {"type": "content_block_delta", "index": 0,
                                   "delta": {"type": "text_delta", "text": content["text"]}})]
                    else:
                        events += [("content_block_start", {"type": "content_block_start", "index": 0,
                                   "content_block": dict(content, input={})}),
                                   ("content_block_delta", {"type": "content_block_delta", "index": 0,
                                   "delta": {"type": "input_json_delta", "partial_json": json.dumps(content["input"])}})]
                    events += [("content_block_stop", {"type": "content_block_stop", "index": 0}),
                               ("message_delta", {"type": "message_delta", "delta": {
                                   "stop_reason": payload["stop_reason"], "stop_sequence": None},
                                   "usage": {"output_tokens": 8}}),
                               ("message_stop", {"type": "message_stop"})]
                    for name, event in events:
                        self.wfile.write(f"event: {name}\ndata: {json.dumps(event)}\n\n".encode())
                    self.wfile.flush()
                else:
                    data = json.dumps(payload).encode()
                    self.send_response(200)
                    self.send_header("Content-Type", "application/json")
                    self.send_header("Content-Length", str(len(data)))
                    self.end_headers()
                    self.wfile.write(data)

        self.server = ThreadingHTTPServer(("127.0.0.1", 0), Handler)
        self.thread = threading.Thread(target=self.server.serve_forever, daemon=True)

    def __enter__(self):
        self.thread.start()
        return self

    def __exit__(self, *args):
        self.server.shutdown()
        self.server.server_close()
        self.thread.join()

    @property
    def provider(self):
        return {"ANTHROPIC_BASE_URL": f"http://127.0.0.1:{self.server.server_port}",
                "ANTHROPIC_AUTH_TOKEN": "local-fixture-not-a-real-credential"}


class GuardTests(unittest.TestCase):
    def setUp(self):
        self.settings, self.policy = worker.read_guard()

    def test_config_and_command(self):
        command = worker.build_command("gemini-test", self.settings, self.policy)
        for option, value in [("--tools", ""), ("--setting-sources", ""),
                              ("--permission-mode", "dontAsk"), ("--max-turns", "1")]:
            self.assertEqual(command[command.index(option) + 1], value)
        for option in ["--strict-mcp-config", "--safe-mode", "--no-session-persistence", "--no-chrome"]:
            self.assertIn(option, command)
        self.assertNotIn("--dangerously-skip-permissions", command)

    def test_input_rejection(self):
        for prompt in ["", "x" * 65537, "@/etc/passwd", "read @secret", "/resume"]:
            with self.subTest(prompt=prompt[:30]), self.assertRaises(ValueError):
                worker.validate_prompt(prompt)
        worker.validate_prompt("Task G01: extract ONLY the supplied text: Alpha 2026")

    def test_real_cli_text_no_tools(self):
        with Endpoint() as endpoint:
            result = worker.execute("Task G01: return the literal DRAFT fixture.", "gemini-test",
                                    endpoint.provider, self.settings, self.policy, timeout=45)
            self.assertEqual(result["status"], "DRAFT")
            self.assertIn("fixture", result["candidate"])
            requests = [body for path, body in endpoint.requests if urlsplit(path).path.endswith('/messages')]
            self.assertTrue(requests)
            for body in requests:
                self.assertEqual(body.get("tools", []), [])
                self.assertEqual(body["model"], "gemini-test")
                self.assertNotIn("ANTHROPIC_AUTH_TOKEN", json.dumps(body))

    def test_real_cli_rejects_injected_tools(self):
        with tempfile.TemporaryDirectory(prefix="gemini-guard-probe-") as directory:
            sentinel = Path(directory) / "sentinel.txt"
            original = b"unchanged-test-only\n"
            sentinel.write_bytes(original)
            probes = [
                ("Write", {"file_path": str(sentinel), "content": "OVERWRITE"}),
                ("Bash", {"command": f"echo OVERWRITE > {sentinel}"}),
                ("Read", {"file_path": str(sentinel)}),
                ("Agent", {"description": "escape", "prompt": "write files", "subagent_type": "general-purpose"}),
                ("mcp__fake__write", {"path": str(sentinel), "content": "OVERWRITE"}),
            ]
            for tool, args in probes:
                with self.subTest(tool=tool), Endpoint(tool, args) as endpoint:
                    with self.assertRaises(ValueError):
                        worker.execute("Task G02: return a candidate only.", "gemini-test",
                                       endpoint.provider, self.settings, self.policy, timeout=45)
                    requests = [body for path, body in endpoint.requests if urlsplit(path).path.endswith('/messages')]
                    self.assertTrue(requests, "must actually reach the local provider")
                    self.assertTrue(all(not body.get("tools") for body in requests))
                    self.assertEqual(sentinel.read_bytes(), original)


if __name__ == "__main__":
    unittest.main(verbosity=2)
