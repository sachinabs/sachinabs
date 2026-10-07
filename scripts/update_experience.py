#!/usr/bin/env python3

from datetime import date
from pathlib import Path
import re

# Your experience started in February 2022
START_YEAR = 2022
START_MONTH = 2

today = date.today()

months = (today.year - START_YEAR) * 12 + (today.month - START_MONTH)

experience = months / 12
experience_text = f"{experience:.1f}"

readme = Path("README.md")
content = readme.read_text(encoding="utf-8")

pattern = r"(I'm a Software Engineer with )\*\*[0-9]+(?:\.[0-9]+)?\+? years( of industry experience)"

updated, count = re.subn(
    pattern,
    rf"\g<1>**{experience_text} years\2",
    content,
    count=1,
)

if count == 0:
    raise SystemExit(
        "Could not find experience text in README.md"
    )

readme.write_text(updated, encoding="utf-8")

print(f"Experience start: {START_YEAR}-{START_MONTH:02d}")
print(f"Current date: {today}")
print(f"Calculated experience: {experience_text} years")