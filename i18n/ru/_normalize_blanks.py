"""Normalize blank lines in ru SKILL.md bodies:
- Collapse 2+ consecutive blank lines → 1 blank line
- Remove blank lines at very start of body (after ---)
- Keep single blank lines between sections (standard markdown)
"""
from pathlib import Path
import re

RU = Path(r"C:\CoAsKB\i18n\ru\skills")

for f in sorted(RU.rglob("SKILL.md")):
    text = f.read_text(encoding="utf-8")
    parts = text.split("---", 2)
    if len(parts) < 3:
        continue
    
    fm = parts[1]
    body = parts[2]
    
    # Collapse 2+ blank lines → 1 blank line
    body = re.sub(r"\n{3,}", "\n\n", body)
    
    # Remove blank lines at start of body (after the ---\n)
    body = body.lstrip("\n")
    
    # Ensure exactly one newline before first heading
    if not body.startswith("#"):
        body = "\n" + body
    
    result = f"---{fm}---\n{body}\n"
    f.write_text(result, encoding="utf-8")
    print(f"  OK  {f.parent.name}")

print("\nDone.")
