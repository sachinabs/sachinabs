#!/usr/bin/env python3

from datetime import date
from pathlib import Path
import re

# Experience started in February 2022
START_YEAR = 2022
START_MONTH = 2

# Find repository root:
# scripts/update_experience.py -> scripts -> repository root
SCRIPT_DIR = Path(__file__).resolve().parent
REPO_ROOT = SCRIPT_DIR.parent

README_PATH = REPO_ROOT / "README.md"

today = date.today()

# Calculate completed months
months = (
    (today.year - START_YEAR) * 12
    + (today.month - START_MONTH)
)

experience = months / 12
experience_text = f"{experience:.1f}"

print(f"Repository root: {REPO_ROOT}")
print(f"README path: {README_PATH}")
print(f"Experience start: {START_YEAR}-{START_MONTH:02d}")
print(f"Current date: {today}")
print(f"Calculated experience: {experience_text} years")

if not README_PATH.exists():
    raise SystemExit(
        f"README.md not found at: {README_PATH}"
    )

content = README_PATH.read_text(encoding="utf-8")

# Matches:
# I'm a Software Engineer with **4+ years of industry experience
# I'm a Software Engineer with **4.7 years of industry experience
pattern = (
    r"(I'm a Software Engineer with )"
    r"\*\*[0-9]+(?:\.[0-9]+)?\+?"
    r"( years of industry experience)"
)

updated, count = re.subn(
    pattern,
    rf"\g<1>**{experience_text}\g<2>",
    content,
    count=1,
)

if count == 0:
    raise SystemExit(
        "Could not find the experience sentence in README.md.\n"
        "Expected something like:\n"
        "I'm a Software Engineer with **4+ years of industry experience"
    )

README_PATH.write_text(updated, encoding="utf-8")

print("✅ README.md experience updated successfully")