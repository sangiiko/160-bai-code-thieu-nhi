#!/usr/bin/env python3
"""Inspect 160-bai-code-thieu-nhi/problems and summarize readiness for Polygon."""

import json
import os
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DEFAULT_REPO = ROOT / "problems"


def main() -> int:
    repo_dir = Path(os.environ.get("REPO_DIR", DEFAULT_REPO))
    if not repo_dir.is_dir():
        print(f"Problems directory not found: {repo_dir}")
        return 1

    manifest_path = repo_dir / "CHECKER_MANIFEST.json"
    if manifest_path.is_file():
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
        summary = manifest.get("_summary", {})
        if summary:
            print("Checker Manifest Summary:", json.dumps(summary))
            print()

    categories = sorted(
        p for p in repo_dir.iterdir()
        if p.is_dir() and not p.name.startswith(".")
    )

    total_problems = 0
    total_with_stmt = 0
    total_with_tests = 0
    total_with_solution = 0
    total_with_checker = 0

    print(f"{'Category':<32} {'Problems':>8} {'Stmt':>6} {'Tests':>7} {'Sol':>7} {'Checker':>8}")
    print("-" * 73)

    for cat in categories:
        probs = sorted(p for p in cat.iterdir() if p.is_dir() and "_" in p.name)
        if not probs:
            continue
        n_probs = len(probs)
        n_stmt = sum(1 for p in probs if (p / "statement_vi.md").is_file())
        n_tests = sum(1 for p in probs if list(p.glob("tests_*.zip")) or (p / "tests").is_dir())
        n_sol = sum(1 for p in probs if (p / "solution.cpp").is_file())
        n_chk = sum(1 for p in probs if (p / "checker.cpp").is_file())

        total_problems += n_probs
        total_with_stmt += n_stmt
        total_with_tests += n_tests
        total_with_solution += n_sol
        total_with_checker += n_chk

        print(
            f"{cat.name:<32} {n_probs:>8} {n_stmt:>6} {n_tests:>7} "
            f"{n_sol:>7} {n_chk:>8}"
        )

    print("-" * 73)
    print(
        f"{'TOTAL':<32} {total_problems:>8} {total_with_stmt:>6} "
        f"{total_with_tests:>7} {total_with_solution:>7} {total_with_checker:>8}"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
