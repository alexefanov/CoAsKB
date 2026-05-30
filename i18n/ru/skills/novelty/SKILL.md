---
description: "Multi-source novelty verification — WebSearch + Semantic Scholar + wiki + Review LLM cross-verify — outputs novelty score and recommendations. Optionally writes the score back to an idea page with --write."
lang: ru
argument-hint: "<idea-description-or-slug> [--quick] [--verbose] [--write]"
---
# /novelty
> Многоисточниковая проверка новизны: веб + Semantic Scholar + вики + Review LLM.

## Аргументы
- `--from <slug>` (обязательно): страница идеи или черновика для проверки
- `--deep` (опционально): глубокий поиск

## Поведение
1. **Поиск по вики**: найди похожие страницы через `python3 tools/research_wiki.py find`.

2. **Поиск по Semantic Scholar**: выполни поиск по ключевым словам идеи.

3. **Поиск по вебу**: выполни поиск через WebFetch.

4. **Review LLM** (если доступен): передай идею на независимую рецензию.

5. Составь сводный отчёт:

   - Уже есть в вики: ...
   - Похожие работы: ...
   - Оценка новизны: высокая/средняя/низкая
   - Рекомендация: ...

## Выход
Отчёт о новизне с оценкой и рекомендациями.

## Зависимости
### Инструменты
- `python3 tools/research_wiki.py find wiki/ <kind> --field <field> <value>`

### Скиллы
- /review — для кросс-модельной рецензии
