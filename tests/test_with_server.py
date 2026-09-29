#!/usr/bin/env python3
"""Lifecycle tests for the webapp-testing server wrapper."""

from __future__ import annotations

import shlex
import socket
import subprocess
import sys
import time
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
WITH_SERVER = ROOT / "skills" / "webapp-testing" / "scripts" / "with_server.py"


def free_port() -> int:
    with socket.socket() as sock:
        sock.bind(("127.0.0.1", 0))
        return sock.getsockname()[1]


class WithServerTests(unittest.TestCase):
    def test_large_server_output_does_not_block_readiness(self) -> None:
        port = free_port()
        server_code = (
            "import socket,sys,time;"
            "sys.stdout.write('x'*200000);sys.stdout.flush();"
            f"s=socket.socket();s.bind(('127.0.0.1',{port}));s.listen();time.sleep(10)"
        )
        server_command = f"exec {shlex.quote(sys.executable)} -c {shlex.quote(server_code)}"
        result = subprocess.run(
            [
                sys.executable,
                str(WITH_SERVER),
                "--server",
                server_command,
                "--port",
                str(port),
                "--timeout",
                "2",
                "--",
                sys.executable,
                "-c",
                "print('PAYLOAD_RAN')",
            ],
            capture_output=True,
            text=True,
            timeout=8,
            check=False,
        )
        self.assertEqual(result.returncode, 0, result.stderr[-500:])
        self.assertIn("PAYLOAD_RAN", result.stdout)

    def test_occupied_port_does_not_count_as_new_server_readiness(self) -> None:
        listener = socket.socket()
        listener.bind(("127.0.0.1", 0))
        listener.listen()
        port = listener.getsockname()[1]
        try:
            result = self.run_wrapper("exit 23", port)
        finally:
            listener.close()
        self.assertNotEqual(result.returncode, 0)
        self.assertNotIn("PAYLOAD_RAN", result.stdout)
        self.assertIn("already in use", result.stderr)

    def test_server_exit_is_reported_before_timeout(self) -> None:
        port = free_port()
        start = time.monotonic()
        result = self.run_wrapper("exit 23", port, timeout=5)
        elapsed = time.monotonic() - start
        self.assertNotEqual(result.returncode, 0)
        self.assertNotIn("PAYLOAD_RAN", result.stdout)
        self.assertIn("exited with status 23", result.stderr)
        self.assertLess(elapsed, 2)

    def run_wrapper(self, server_command: str, port: int, timeout: int = 2) -> subprocess.CompletedProcess[str]:
        return subprocess.run(
            [
                sys.executable,
                str(WITH_SERVER),
                "--server",
                server_command,
                "--port",
                str(port),
                "--timeout",
                str(timeout),
                "--",
                sys.executable,
                "-c",
                "print('PAYLOAD_RAN')",
            ],
            capture_output=True,
            text=True,
            timeout=timeout + 5,
            check=False,
        )


if __name__ == "__main__":
    unittest.main()
