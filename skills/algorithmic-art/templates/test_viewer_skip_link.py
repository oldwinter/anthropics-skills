#!/usr/bin/env python3
"""Lock the algorithmic-art viewer skip-link contract."""

from __future__ import annotations

import re
import unittest
from pathlib import Path

VIEWER = Path(__file__).with_name("viewer.html")


class ViewerSkipLinkTests(unittest.TestCase):
    def test_skip_link_is_first_focusable_and_keyboard_only(self) -> None:
        html = VIEWER.read_text(encoding="utf-8")
        body = html[html.find("<body>") :]
        first = re.search(r"<(?:a|button|input|select|textarea)\b[^>]*>", body)
        self.assertIsNotNone(first)
        self.assertIn('class="skip-link"', first.group(0))
        self.assertIn('href="#artwork"', first.group(0))
        self.assertIn("Skip to artwork", first.group(0))
        self.assertIn('id="artwork"', html)
        self.assertIn('<main class="canvas-area"', html)
        self.assertIn('tabindex="-1"', html)
        self.assertIn(".skip-link:focus-visible", html)
        self.assertNotRegex(html, r"\.skip-link:focus\s*\{")
        self.assertIn(".seed-input:focus", html)


if __name__ == "__main__":
    unittest.main()
