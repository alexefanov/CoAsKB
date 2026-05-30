"""Smart blank-line normalizer for ru SKILL.md bodies.
- Remove ALL blank lines, then re-add only where structurally needed.
- Rules: 1 blank line before ## headings, before ``` code blocks, before > blockquotes.
- No blank lines between list items, or between heading and its first line.
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
    
    # Split into lines, strip all blank lines
    lines = body.split("\n")
    non_blank = [i for i, l in enumerate(lines) if l.strip()]
    
    if not non_blank:
        continue
    
    # Rebuild with minimal blank lines
    result_lines = []
    in_code_block = False
    prev_was_blank = False
    prev_type = ""  # "heading", "list", "code", "text", "blockquote"
    
    for i, line in enumerate(lines):
        stripped = line.strip()
        
        # Track code blocks
        if stripped.startswith("```"):
            in_code_block = not in_code_block
            result_lines.append(line)
            prev_type = "code_marker"
            prev_was_blank = False
            continue
        
        if in_code_block:
            result_lines.append(line)
            prev_was_blank = False
            continue
        
        # Empty line - skip unless structurally needed
        if not stripped:
            prev_was_blank = True
            continue
        
        current_type = "text"
        if stripped.startswith("#"):
            current_type = "heading"
        elif stripped.startswith("- ") or stripped.startswith("* ") or stripped.startswith("1."):
            current_type = "list"
        elif stripped.startswith(">"):
            current_type = "blockquote"
        elif stripped == "---":
            current_type = "hr"
        
        # Decide whether to add blank line before this line
        need_blank = False
        
        if not result_lines:
            # First line - no blank
            need_blank = False
        elif current_type == "heading":
            # Always blank before heading (unless start of body)
            need_blank = True
        elif current_type == "blockquote" and prev_type != "blockquote":
            need_blank = True
        elif current_type == "list" and prev_type == "heading":
            # List right after heading - no blank
            need_blank = False
        elif current_type == "list" and prev_type == "list":
            # Consecutive list items - no blank
            need_blank = False
        elif current_type == "code":
            need_blank = True
        elif prev_type == "code_marker":
            need_blank = True
        else:
            # Between paragraphs of text
            if prev_was_blank:
                need_blank = False  # already had blank
            elif prev_type == "list" and current_type == "text":
                need_blank = True
            elif prev_type == "text" and current_type == "list":
                need_blank = True
            elif prev_type == "text" and current_type == "text":
                need_blank = True
        
        if need_blank and prev_type != "heading":
            # Ensure we have exactly one blank line
            if result_lines and result_lines[-1].strip() != "":
                result_lines.append("")
        
        result_lines.append(line)
        prev_type = current_type
        prev_was_blank = False
    
    # Clean trailing blank lines
    while result_lines and result_lines[-1].strip() == "":
        result_lines.pop()
    
    new_body = "\n".join(result_lines)
    
    result = f"---{fm}---\n{new_body}\n"
    f.write_text(result, encoding="utf-8")
    print(f"  OK  {f.parent.name}")

print("\nDone.")
