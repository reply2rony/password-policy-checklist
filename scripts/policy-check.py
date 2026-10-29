#!/usr/bin/env python3
"""Starter learning template: summarise a password-policy checklist CSV.

Reads password-policy-checklist.csv (sample data only) and prints how
many rules are Met, Partial, or Missing. It never reads, stores, or
tests any real password, and it does not change the CSV.
"""

import csv
import sys
from collections import Counter
from pathlib import Path

CSV_PATH = Path(__file__).resolve().parent.parent / "password-policy-checklist.csv"


def main() -> int:
    if not CSV_PATH.exists():
        print(f"Checklist not found: {CSV_PATH}")
        return 1

    rows = list(csv.DictReader(CSV_PATH.open(newline="", encoding="utf-8")))
    counts = Counter(row["sample_policy_status"].strip() for row in rows)
    total = len(rows)
    met = counts.get("Met", 0)

    print(f"Password policy checklist: {total} rules reviewed")
    print(f"  Met:     {met}")
    print(f"  Partial: {counts.get('Partial', 0)}")
    print(f"  Missing: {counts.get('Missing', 0)}")
    if total:
        print(f"  Met rate (sample only): {met * 100 // total}%")
    print()
    print("Rules needing attention (Partial or Missing):")
    attention = [r for r in rows if r["sample_policy_status"].strip() != "Met"]
    if not attention:
        print("  None — every sample rule is marked Met.")
    for row in attention:
        print(f"  - {row['rule']} [{row['sample_policy_status']}] — {row['notes']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
