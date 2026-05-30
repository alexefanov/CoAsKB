"""Add Russian bilingual comments alongside English ones in YAML/Python files.
Keeps original English, adds Russian after each comment line."""
import re
from pathlib import Path

ROOT = Path(r"C:\CoAsKB")

# Mapping of translator comments to add after English comments
RUSSIAN_COMMENTS = {
    # entities.yaml comments
    "Node contract for the wiki entity types.": "Контракт узлов для типов сущностей вики.",
    "Field attributes:": "Атрибуты полей:",
    "nested schema for object": "вложенная схема для объекта",
    "per-element schema for list_object": "поэлементная схема для list_object",
    "terminal: true means the entity writes no outward links (xref reverse-rule exempt).": 
        "terminal: true означает, что сущность не пишет внешних ссылок (исключение из правил обратных ссылок xref).",
    
    # edges.yaml comments
    "Relation contract for graph edges (incl. citations).":
        "Контракт отношений для рёбер графа (включая цитирования).",
    "Each edge type declares:": "Каждый тип ребра объявляет:",
    "'*' means any kind": "'*' означает любой тип",
    "directed | symmetric": "направленное | симметричное",
    "symmetric edges are stored once with sorted endpoints":
        "симметричные рёбра хранятся один раз с отсортированными концами",
    "which subsystem owns this edge type":
        "какая подсистема владеет этим типом ребра",
    "schema for edge-record fields beyond from/to/type":
        "схема полей записи ребра помимо from/to/type",
    "Paper ↔ Paper semantic edges  (written by /ingest)":
        "Семантические рёбра Статья ↔ Статья (создаются /ingest)",
    "Paper → Concept semantic edges  (written by /ingest)":
        "Семантические рёбра Статья → Концепт (создаются /ingest)",
    "Workflow edges (evidence / experiments / ideas / provenance)":
        "Рабочие рёбра (свидетельства / эксперименты / идеи / происхождение)",
    "Endpoints stay broad because these span multiple entity kinds.":
        "Концы остаются широкими, так как охватывают несколько видов сущностей.",
    "Bibliographic citation": "Библиографическое цитирование",
}

def add_russian_comment(line, next_line=None):
    """If line is a comment, check if we should add Russian after it."""
    stripped = line.strip()
    if not stripped.startswith("#"):
        return None
    
    # Skip lines that are just separators or already have Russian
    if stripped in ("#", "# ---", "# =") or "—" in stripped or "Русский" in stripped:
        return None
    
    # Skip lines that contain only structure markers
    if re.match(r'^#\s*\{\s*$', stripped) or re.match(r'^#\s*\}\s*$', stripped):
        return None
    
    # Extract the comment text (after # and optional space)
    text = re.sub(r'^#+\s*', '', stripped).strip()
    if not text or len(text) < 3:
        return None
    
    # Check if we already added Russian
    if next_line and next_line.strip().startswith("#") and "—" in next_line:
        return None  # Russian already exists
    
    # Find translation
    ru = RUSSIAN_COMMENTS.get(text)
    if not ru:
        # Try partial match
        for en, ru_text in RUSSIAN_COMMENTS.items():
            if en in text or text in en:
                ru = ru_text
                break
    
    if ru:
        indent = line[:len(line) - len(line.lstrip())]
        return f"{indent}# {text} / {ru}\n"
    return None

def process_file(path):
    if not path.exists():
        return
    text = path.read_text(encoding="utf-8")
    lines = text.split("\n")
    new_lines = []
    changes = 0
    
    for i, line in enumerate(lines):
        new_lines.append(line)
        ru_line = add_russian_comment(line, lines[i+1] if i+1 < len(lines) else None)
        if ru_line:
            new_lines.append(ru_line.rstrip("\n"))
            changes += 1
    
    if changes > 0:
        path.write_text("\n".join(new_lines), encoding="utf-8")
        print(f"  {path.name}: {changes} comments")
    else:
        print(f"  {path.name}: no changes")

# Process YAML files
print("=== Processing YAML files ===")
process_file(ROOT / "runtime" / "schema" / "entities.yaml")
process_file(ROOT / "runtime" / "schema" / "edges.yaml")
process_file(ROOT / "runtime" / "schema" / "conventions.yaml")
process_file(ROOT / "runtime" / "schema" / "xref.yaml")
process_file(ROOT / "runtime" / "policy" / "writers.yaml")

print("\nDone!")
