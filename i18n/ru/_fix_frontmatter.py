"""Fix broken frontmatter in all ru SKILL.md files.
Issue: 'lang: ru---' (closing --- glued to last YAML line).
Fix: ensure --- is on its own line after lang: ru.
"""
from pathlib import Path

RU = Path(r"C:\CoAsKB\i18n\ru\skills")
fixed = 0

for f in sorted(RU.rglob("SKILL.md")):
    text = f.read_bytes()
    
    # Find first ---
    first = text.find(b"---")
    if first < 0:
        continue
    
    # Find second ---  
    second = text.find(b"---", first + 3)
    if second < 0:
        continue
    
    # Extract frontmatter and body
    fm_raw = text[first + 3 : second].decode("utf-8").strip()  # content between --- and ---
    body = text[second + 3 :].decode("utf-8").lstrip("\n\r")
    
    # Parse YAML lines, ensure lang: ru exists and --- is on its own line
    lines = fm_raw.split("\n")
    
    # Remove any existing lang: ru (including broken ones)
    cleaned = [l for l in lines if not l.strip().startswith("lang: ru")]
    
    # Add proper lang: ru
    # Insert after the description line, or at the beginning
    desc_idx = None
    for i, l in enumerate(cleaned):
        if l.strip().startswith("description:"):
            desc_idx = i
            break
    
    if desc_idx is not None:
        cleaned.insert(desc_idx + 1, "lang: ru")
    else:
        cleaned.append("lang: ru")
    
    # Remove trailing empty lines from cleaned
    while cleaned and cleaned[-1].strip() == "":
        cleaned.pop()
    
    # Rebuild with proper formatting
    new_fm = "\n".join(cleaned)
    new_text = f"---\n{new_fm}\n---\n\n{body}"
    
    f.write_text(new_text, encoding="utf-8")
    fixed += 1
    print(f"  OK  {f.parent.name}")

print(f"\nFixed {fixed} files")
