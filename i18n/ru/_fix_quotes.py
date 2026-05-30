"""Mass-fix all ru SKILL.md frontmatter: wrap description/argument-hint in quotes.
Also remove blank lines inside frontmatter.
"""
from pathlib import Path
import re

RU = Path(r"C:\CoAsKB\i18n\ru\skills")
fixed = 0

for f in sorted(RU.rglob("SKILL.md")):
    text = f.read_text(encoding="utf-8")
    
    # Split by --- (max 2 splits)
    parts = text.split("---", 2)
    if len(parts) < 3:
        continue
    
    raw_fm = parts[1]
    body = parts[2]
    
    # Ensure each YAML field value is properly quoted
    lines = raw_fm.split("\n")
    new_lines = []
    
    for line in lines:
        # Skip empty lines
        if not line.strip():
            continue
        # Quote description and argument-hint values if not already quoted
        stripped = line.strip()
        if stripped.startswith("description:"):
            val = stripped[len("description:"):].strip()
            if not (val.startswith('"') and val.endswith('"')):
                # Escape any double quotes inside
                val_escaped = val.replace('"', '\\"')
                line = f"description: \"{val_escaped}\""
        elif stripped.startswith("argument-hint:"):
            val = stripped[len("argument-hint:"):].strip()
            if not (val.startswith('"') and val.endswith('"')):
                val_escaped = val.replace('"', '\\"')
                line = f"argument-hint: \"{val_escaped}\""
        new_lines.append(line)
    
    new_fm = "\n".join(new_lines)
    
    # Reconstruct
    result = f"---\n{new_fm}\n---\n{body}"
    f.write_text(result, encoding="utf-8")
    fixed += 1

print(f"Fixed {fixed} files")
