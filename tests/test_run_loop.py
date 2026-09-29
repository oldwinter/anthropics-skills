#!/usr/bin/env python3
"""Data-splitting tests for the description optimization loop."""

from __future__ import annotations

import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILL_ROOT = ROOT / "skills" / "skill-creator"
sys.path.insert(0, str(SKILL_ROOT))

from scripts.run_loop import split_eval_set


class SplitEvalSetTests(unittest.TestCase):
    def test_singleton_classes_remain_in_training_set(self) -> None:
        eval_set = [
            {"query": "positive", "should_trigger": True},
            {"query": "negative", "should_trigger": False},
        ]
        train, test = split_eval_set(eval_set, 0.4)
        self.assertEqual(len(train), 2)
        self.assertEqual(test, [])

    def test_each_class_keeps_a_training_example(self) -> None:
        eval_set = [
            {"query": "positive-1", "should_trigger": True},
            {"query": "positive-2", "should_trigger": True},
            {"query": "negative-1", "should_trigger": False},
            {"query": "negative-2", "should_trigger": False},
        ]
        train, test = split_eval_set(eval_set, 0.4)
        self.assertEqual(len(train), 2)
        self.assertEqual(len(test), 2)
        self.assertEqual({item["should_trigger"] for item in train}, {True, False})

    def test_rejects_out_of_range_holdout(self) -> None:
        for holdout in (-0.1, 0, 1, 1.5):
            with self.subTest(holdout=holdout):
                with self.assertRaises(ValueError):
                    split_eval_set([], holdout)


if __name__ == "__main__":
    unittest.main()
