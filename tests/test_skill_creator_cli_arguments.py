#!/usr/bin/env python3
"""Input-boundary tests for skill-creator command arguments."""

from __future__ import annotations

import subprocess
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPT_DIR = ROOT / "skills" / "skill-creator" / "scripts"


class SkillCreatorArgumentTests(unittest.TestCase):
    def assert_argument_rejected(self, script: str, option: str, value: str) -> None:
        command = [
            sys.executable,
            str(SCRIPT_DIR / script),
            "--eval-set",
            "missing.json",
            "--skill-path",
            "missing-skill",
        ]
        if script == "run_loop.py":
            command.extend(["--model", "test-model"])
        command.extend([option, value])
        result = subprocess.run(
            command,
            cwd=ROOT,
            capture_output=True,
            text=True,
            check=False,
        )
        self.assertEqual(result.returncode, 2, result.stderr)
        self.assertIn("invalid", result.stderr.lower())

    def test_run_eval_rejects_invalid_numeric_arguments(self) -> None:
        cases = (
            ("--num-workers", "0"),
            ("--timeout", "0"),
            ("--runs-per-query", "0"),
            ("--trigger-threshold", "-0.1"),
            ("--trigger-threshold", "1.1"),
        )
        for option, value in cases:
            with self.subTest(option=option, value=value):
                self.assert_argument_rejected("run_eval.py", option, value)

    def test_run_loop_rejects_invalid_numeric_arguments(self) -> None:
        cases = (
            ("--num-workers", "0"),
            ("--timeout", "0"),
            ("--max-iterations", "0"),
            ("--runs-per-query", "0"),
            ("--trigger-threshold", "-0.1"),
            ("--trigger-threshold", "1.1"),
            ("--holdout", "-0.1"),
            ("--holdout", "1"),
        )
        for option, value in cases:
            with self.subTest(option=option, value=value):
                self.assert_argument_rejected("run_loop.py", option, value)


if __name__ == "__main__":
    unittest.main()
