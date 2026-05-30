---
description: "Idea-driven experiment design with iterative ablation — method candidate generation (direct / hybrid / cross-idea combination) → benchmark selection → iterative ablation (non-linear: ablation can trigger method simplification and re-planning) → sensitivity analysis → main experiment → optional generalization → deep analysis of intermediate quantities. Use when designing a full experiment suite for an idea after pilot evaluation."
lang: ru
argument-hint: "<idea-slug>"
---
# /exp-design
> Спроектировать эксперимент из идеи: выбрать метод, метрики, бейзлайн — и записать страницу эксперимента в вики.

## Аргументы
- `--from <slug-идеи>` (обязательно): страница идеи для проверки
- `--method <slug-метода>` (опционально): метод для проверки (если не указан — выбрать лучший из вики)

## Поведение
1. Прочитай страницу идеи (гипотеза, ожидаемый результат, метрики успеха).

2. Выбери метод проверки: синтез из существующих методов в вики или предложи новый.

3. Определи бейзлайн для сравнения.

4. Определи метрики (точность, скорость, стоимость и т.д.).

5. Спроектируй протокол эксперимента: данные, шаги, условия.

6. Создай страницу эксперимента:
   ```bash
   python3 tools/research_wiki.py slug "<название эксперимента>"
   ```

7. Запиши страницу в `wiki/experiments/<slug>.md` с полным frontmatter.

8. Обнови рёбра:
   ```bash
   python3 tools/research_wiki.py add-edge wiki/ --from experiments/<slug> --to ideas/<slug-idea> --type tests_hypothesis
   ```

## Выходы
- Страница эксперимента в wiki/experiments/
- Рёбра графа (linked_idea, evaluates_methods)
- Обновлён index.md и log.md

## Зависимости
### Инструменты
- `python3 tools/research_wiki.py slug "<title>"`
- `python3 tools/research_wiki.py add-edge wiki/ --from X --to Y --type Z`
- `python3 tools/research_wiki.py log wiki/ "<msg>"`
