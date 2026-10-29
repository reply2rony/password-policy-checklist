# Password Policy Checklist

A simple starter template for reviewing a small-office password
policy: one checklist row per rule, a sample policy to practise
against, and a small starter script that scores the sample against
the checklist.

## What it is
- `password-policy-checklist.csv` — one row per password rule
  (what the rule is, the recommended setting, and whether the
  sample policy meets it). Sample data only; replace it with your
  own organisation's rules.
- `docs/policy-guide.md` — how to read each checklist item, why it
  matters, and a short quarterly review routine.
- `scripts/policy-check.py` — reads the checklist CSV and prints a
  summary: how many rules are met, which ones are missing, and which
  rows need attention. It checks the checklist file only; it does
  not read, store, or test any real password.
- `docs/diagram.png` — a generated Sample / Demo diagram of the
  policy-review flow. It is an illustration, not a screenshot of a
  real system, and it does not show any real company system or data.

## How to use it (no code)
1. Copy `password-policy-checklist.csv` and delete the sample rows.
2. Add one row per rule in your own policy, following
   `docs/policy-guide.md`.
3. Once a quarter, work through the review routine in the guide and
   update any row whose setting has changed.

## How to use it (with Python)
1. Install Python 3 — no extra packages needed.
2. In a terminal, go to this folder and run:
   `python scripts/policy-check.py`
3. Read the summary it prints. It does not change your CSV and it
   never handles a real password.

## Sample data note
All rules, settings, and example values in the sample file are
illustrative only. Never put real employee data, real system names,
real policies from a real employer, or real credentials in a public
repository.

## Note on skills
Python is labelled "Learning" in the author's profile. This script is
an intentionally short, commented starter learning template for IT
support work, and the CSV and guide versions work without it. No CCTV
content is used as experience here, and no performance numbers are
claimed.
