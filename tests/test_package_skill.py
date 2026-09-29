#!/usr/bin/env python3
"""Packaging boundary tests for skill archives."""

from __future__ import annotations

import contextlib
import io
import os
import sys
import tempfile
import unittest
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPT_DIR = ROOT / "skills" / "skill-creator" / "scripts"
sys.path.insert(0, str(SCRIPT_DIR))

from package_skill import package_skill


class PackageSkillTests(unittest.TestCase):
    def test_external_symlink_is_not_packaged(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            skill = root / "demo"
            skill.mkdir()
            (skill / "SKILL.md").write_text(
                "---\nname: demo\ndescription: Use for tests.\n---\n",
                encoding="utf-8",
            )
            (skill / "normal.txt").write_text("normal", encoding="utf-8")
            secret = root / "outside-secret.txt"
            secret.write_text("outside-secret", encoding="utf-8")
            os.symlink(secret, skill / "linked-secret.txt")

            with contextlib.redirect_stdout(io.StringIO()):
                archive = package_skill(skill, root / "out")

            self.assertIsNotNone(archive)
            with zipfile.ZipFile(archive) as zipf:
                names = set(zipf.namelist())
                self.assertIn("demo/normal.txt", names)
                self.assertNotIn("demo/linked-secret.txt", names)


if __name__ == "__main__":
    unittest.main()
