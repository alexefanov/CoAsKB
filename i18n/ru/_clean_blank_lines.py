"""Clean up extra blank lines in ru SKILL.md files.
- Frontmatter: no blank lines between fields, no trailing blank before ---
- Body: no runs of >2 consecutive blank lines
- No blank line after opening --- or before closing ---
"""
from pathlib import Path
import re

RU = Path(r"C:\CoAsKB\i18n\ru\skills")

for f in sorted(RU.rglob("SKILL.md")):
    text = f.read_text(encoding="utf-8")
    parts = text.split("---", 2)
    if len(parts) < 3:
        continue
    
    raw_fm = parts[1]
    body = parts[2]
    
    # Clean frontmatter: remove blank lines, strip each line
    fm_lines = [l.strip() for l in raw_fm.split("\n") if l.strip()]
    new_fm = "\n".join(fm_lines)
    
    # Clean body: collapse runs of 3+ blank lines to 2
    body = re.sub(r"\n{4,}", "\n\n\n", body)
    # Also trim leading/trailing whitespace
    body = body.strip()
    
    result = f"---\n{new_fm}\n---\n{body}\n"
    f.write_text(result, encoding="utf-8")
    print(f"  OK  {f.parent.name}")

print("\nDone.")
