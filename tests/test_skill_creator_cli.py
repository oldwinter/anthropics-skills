#!/usr/bin/env python3
"""Regression tests for direct and package skill-creator imports."""

from __future__ import annotations

import subprocess
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILL_ROOT = ROOT / "skills" / "skill-creator"
SCRIPT_CASES = (
    ("improve_description.py", ("--help",), 0, "usage:"),
    ("package_skill.py", (), 1, "Usage:"),
    ("run_eval.py", ("--help",), 0, "usage:"),
    ("run_loop.py", ("--help",), 0, "usage:"),
)


class SkillCreatorCliTests(unittest.TestCase):
    def assert_cli_contract(
        self,
        command: list[str],
        cwd: Path,
        expected_returncode: int,
        expected_output: str,
    ) -> None:
        result = subprocess.run(
            command,
            cwd=cwd,
            capture_output=True,
            text=True,
            check=False,
        )
        self.assertEqual(
            result.returncode,
            expected_returncode,
            f"command failed: {' '.join(command)}\n{result.stderr}",
        )
        self.assertIn(expected_output, result.stdout)
        self.assertNotIn("Traceback", result.stderr)

    def test_direct_scripts_honor_cli_contract_from_repository_root(self) -> None:
        for script_name, args, returncode, output in SCRIPT_CASES:
            with self.subTest(script=script_name):
                script = SKILL_ROOT / "scripts" / script_name
                self.assert_cli_contract(
                    [sys.executable, str(script), *args],
                    ROOT,
                    returncode,
                    output,
                )

    def test_direct_scripts_honor_cli_contract_from_skill_root(self) -> None:
        for script_name, args, returncode, output in SCRIPT_CASES:
            with self.subTest(script=script_name):
                self.assert_cli_contract(
                    [sys.executable, f"scripts/{script_name}", *args],
                    SKILL_ROOT,
                    returncode,
                    output,
                )

    def test_modules_import_as_package(self) -> None:
        for script_name, _, _, _ in SCRIPT_CASES:
            module_name = Path(script_name).stem
            with self.subTest(module=module_name):
                result = subprocess.run(
                    [sys.executable, "-c", f"import scripts.{module_name}"],
                    cwd=SKILL_ROOT,
                    capture_output=True,
                    text=True,
                    check=False,
                )
                self.assertEqual(result.returncode, 0, result.stderr)


if __name__ == "__main__":
    unittest.main()
