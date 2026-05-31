---
description: "Generate and update visualization artifacts — Obsidian graph config and Canvas knowledge maps. The interactive web graph view lives in the SPA at app/modules/graph.js (served by tools/serve.py)."
lang: ru
argument-hint: "[--obsidian] [--canvas] [--focus <node_id>] [--depth N] [--types <page-type,...>] [--edge-types <edge-type,...>] [--all]"
---
# /visualize
> Сгенерировать или обновить артефакты визуализации графа знаний (веб-интерфейс, Obsidian-конфиг, Canvas).

## Аргументы
- `--type <тип>` (обязательно): тип визуализации. Варианты: graph (веб-граф) | obsidian (конфиг Obsidian) | canvas (Obsidian Canvas)
- `--output <путь>` (опционально): путь для сохранения (по умолчанию outputs/viz/)

## Поведение
### Тип: graph
1. Прочитай `wiki/graph/edges.jsonl`.
2. Сгенерируй HTML-страницу с интерактивным графом (D3.js/vis.js).
3. Узлы = страницы, рёбра = связи, цвета = типы сущностей.

### Тип: obsidian
1. Сгенерируй/обнови `.obsidian/` конфиг для правильного отображения вики-ссылок.

### Тип: canvas
1. Создай Obsidian Canvas (.canvas) с узлами и связями для выбранной темы.

## Выходы
- HTML / Canvas / конфигурационные файлы
- Обновлён index.md

## Зависимости
### Инструменты
- `python3 tools/research_wiki.py neighbors wiki/ <slug> --depth N`
- `python3 tools/research_wiki.py find wiki/ <kind>`
