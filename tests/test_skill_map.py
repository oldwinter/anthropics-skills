#!/usr/bin/env python3
"""Assert Chinese skill catalog is a grouped selection table, not a flat slug list."""

from __future__ import annotations

import json
import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
README = (ROOT / "README.md").read_text(encoding="utf-8")
SKILL_MAP = (ROOT / "docs" / "skill-map.zh-CN.md").read_text(encoding="utf-8")
PROFILE = (ROOT / "docs" / "translation-profile.zh-CN.md").read_text(encoding="utf-8")
MARKETPLACE = json.loads((ROOT / ".claude-plugin" / "marketplace.json").read_text(encoding="utf-8"))

CHINESE_README = README.split("\n---\n", 1)[0]

CREATIVE_TASKS = (
    ("海报", "canvas-design"),
    ("产品 UI", "frontend-design"),
    ("生成艺术", "algorithmic-art"),
    ("换肤", "theme-factory"),
    ("Anthropic", "brand-guidelines"),
)

RESTRICTED = ("docx", "pdf", "pptx", "xlsx", "doc-coauthoring", "template")
SOLO_PLUGINS = ("claude-api", "academy-guide", "discernment-nudge")


def plugin_slugs(name: str) -> list[str]:
    for plugin in MARKETPLACE["plugins"]:
        if plugin["name"] == name:
            return [Path(path).name for path in plugin["skills"]]
    raise AssertionError(f"missing plugin {name}")


def same_line(text: str, left: str, right: str) -> bool:
    return any(left in line and right in line for line in text.splitlines())


class SkillMapTests(unittest.TestCase):
    def test_readme_is_grouped_not_flat_slug_list(self) -> None:
        self.assertNotIn("可直接安装的中文入口包括", CHINESE_README)
        self.assertIn("docs/skill-map.zh-CN.md", CHINESE_README)
        for heading in ("创作与设计", "开发与技术", "企业与沟通", "文档技能"):
            self.assertIn(heading, CHINESE_README)
            self.assertIn(heading, SKILL_MAP)

    def test_creative_tasks_map_to_adjacent_skills(self) -> None:
        for task, slug in CREATIVE_TASKS:
            self.assertTrue(
                same_line(CHINESE_README, task, slug),
                f"README missing {task} → {slug} on one row",
            )
            self.assertTrue(
                same_line(SKILL_MAP, task, slug),
                f"skill-map missing {task} → {slug} on one row",
            )
            self.assertIn("不要用", CHINESE_README)
            self.assertIn("不要用", SKILL_MAP)

    def test_example_skills_zh_members_are_not_mixed_with_solo_plugins(self) -> None:
        zh_slugs = plugin_slugs("example-skills-zh")
        self.assertEqual(len(zh_slugs), 11)
        self.assertNotIn("claude-api", zh_slugs)
        for slug in zh_slugs:
            self.assertIn(f"`{slug}`", CHINESE_README)
            self.assertIn(f"`{slug}`", SKILL_MAP)
            self.assertTrue((ROOT / "skills" / slug / "SKILL.md").is_file())
        self.assertIn("不是 `example-skills-zh` 的成员", CHINESE_README)
        self.assertIn("不是** `example-skills-zh` 的成员", SKILL_MAP)
        for slug in SOLO_PLUGINS:
            self.assertIn(f"`{slug}`", CHINESE_README)
            self.assertIn(f"`{slug}`", SKILL_MAP)
            self.assertTrue((ROOT / "skills" / slug / "SKILL.md").is_file())

    def test_restricted_entries_are_not_chinese_distribution(self) -> None:
        self.assertIn("不作为中文版分发", CHINESE_README)
        for slug in RESTRICTED:
            self.assertTrue(
                same_line(SKILL_MAP, f"`{slug}`", "上游原文")
                or slug in re.findall(r"`([^`]+)`", SKILL_MAP),
                f"skill-map missing restricted entry {slug}",
            )
            if slug != "template":
                self.assertTrue((ROOT / "skills" / slug / "SKILL.md").is_file())
            else:
                self.assertTrue((ROOT / "template" / "SKILL.md").is_file())

    def test_translation_profile_points_at_skill_map(self) -> None:
        self.assertIn("skill-map.zh-CN.md", PROFILE)
        self.assertIn("不要把 README 写回扁平 slug 清单", PROFILE)
        self.assertIn("python3 tests/test_skill_map.py", PROFILE)


if __name__ == "__main__":
    unittest.main()
