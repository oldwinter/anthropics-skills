#!/usr/bin/env python3
"""Security tests for standalone review HTML generation."""

from __future__ import annotations

import json
import re
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
VIEWER_DIR = ROOT / "skills" / "skill-creator" / "eval-viewer"
sys.path.insert(0, str(VIEWER_DIR))

from generate_review import generate_html


class GenerateReviewTests(unittest.TestCase):
    def test_embedded_json_cannot_close_inline_script(self) -> None:
        payload = "</script><script>globalThis.injected=true</script>\u2028\u2029"
        rendered = generate_html([], payload)
        template = (VIEWER_DIR / "viewer.html").read_text(encoding="utf-8")
        self.assertEqual(rendered.count("</script>"), template.count("</script>"))
        self.assertNotIn(payload, rendered)

        match = re.search(r"const EMBEDDED_DATA = (.*);", rendered)
        self.assertIsNotNone(match)
        embedded = json.loads(match.group(1))
        self.assertEqual(embedded["skill_name"], payload)


if __name__ == "__main__":
    unittest.main()
