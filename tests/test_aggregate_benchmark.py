#!/usr/bin/env python3
"""Benchmark metadata tests for observed run counts."""

from __future__ import annotations

import json
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPT_DIR = ROOT / "skills" / "skill-creator" / "scripts"
sys.path.insert(0, str(SCRIPT_DIR))

from aggregate_benchmark import generate_benchmark, generate_markdown


def write_grading(path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        json.dumps({"summary": {"pass_rate": 1.0, "passed": 1, "failed": 0, "total": 1}}),
        encoding="utf-8",
    )


class AggregateBenchmarkTests(unittest.TestCase):
    def test_reports_observed_uniform_run_count(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            write_grading(root / "eval-0" / "with_skill" / "run-1" / "grading.json")
            write_grading(root / "eval-0" / "without_skill" / "run-1" / "grading.json")
            benchmark = generate_benchmark(root)
            self.assertEqual(benchmark["metadata"]["runs_per_configuration"], 1)

    def test_marks_uneven_run_counts_without_claiming_uniform_sample(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            write_grading(root / "eval-0" / "with_skill" / "run-1" / "grading.json")
            write_grading(root / "eval-0" / "with_skill" / "run-2" / "grading.json")
            write_grading(root / "eval-0" / "without_skill" / "run-1" / "grading.json")
            benchmark = generate_benchmark(root)
            metadata = benchmark["metadata"]
            self.assertIsNone(metadata["runs_per_configuration"])
            self.assertEqual(
                metadata["run_counts_by_configuration"],
                {"with_skill": [2], "without_skill": [1]},
            )
            self.assertIn("varying runs per configuration", generate_markdown(benchmark))


if __name__ == "__main__":
    unittest.main()
