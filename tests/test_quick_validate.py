#!/usr/bin/env python3
"""Agent Skills specification checks for quick_validate."""

from __future__ import annotations

import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPT_DIR = ROOT / "skills" / "skill-creator" / "scripts"
sys.path.insert(0, str(SCRIPT_DIR))

from quick_validate import validate_skill


class QuickValidateTests(unittest.TestCase):
    def validate_frontmatter(self, directory: str, frontmatter: str) -> tuple[bool, str]:
        with tempfile.TemporaryDirectory() as tmp:
            skill = Path(tmp) / directory
            skill.mkdir()
            (skill / "SKILL.md").write_text(
                f"---\n{frontmatter}\n---\n\n# Test\n",
                encoding="utf-8",
            )
            return validate_skill(skill)

    def assert_invalid(self, directory: str, frontmatter: str) -> None:
        valid, message = self.validate_frontmatter(directory, frontmatter)
        self.assertFalse(valid, message)

    def test_rejects_empty_required_fields(self) -> None:
        self.assert_invalid("empty-name", "name: ''\ndescription: valid")
        self.assert_invalid("empty-description", "name: empty-description\ndescription: ''")

    def test_rejects_name_that_differs_from_parent_directory(self) -> None:
        self.assert_invalid("directory-name", "name: another-name\ndescription: valid")

    def test_rejects_empty_compatibility_when_field_is_present(self) -> None:
        self.assert_invalid(
            "empty-compatibility",
            "name: empty-compatibility\ndescription: valid\ncompatibility: ''",
        )

    def test_rejects_metadata_that_is_not_string_mapping(self) -> None:
        self.assert_invalid("metadata-list", "name: metadata-list\ndescription: valid\nmetadata: []")
        self.assert_invalid(
            "metadata-value",
            "name: metadata-value\ndescription: valid\nmetadata:\n  version: 1",
        )

    def test_repository_skills_remain_valid(self) -> None:
        for skill_file in sorted((ROOT / "skills").glob("*/SKILL.md")):
            with self.subTest(skill=skill_file.parent.name):
                valid, message = validate_skill(skill_file.parent)
                self.assertTrue(valid, message)


if __name__ == "__main__":
    unittest.main()
