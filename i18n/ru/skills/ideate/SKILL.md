---
description: "Multi-phase research idea generation pipeline: landscape scan → dual-model brainstorm → filter & validation → write to wiki → pilot"
lang: ru
argument-hint: "[research-direction-or-topic] [--max-ideas N] [--skip-validation] [--skip-pilot] [--auto]"
---
# /ideate
> Многофазовый конвейер генерации исследовательских идей: обзор ландшафта → дуальная мозговая атака → фильтрация → запись → пилот.

## Аргументы
- `--topic <тема>` (обязательно): тема для генерации идей
- `--deep` (опц.): глубокий поиск по теме
- `--pilot` (опц.): выполнить пилотное тестирование лучшей идеи

## Поведение
### Фаза 1: Обзор ландшафта
1. Прочитай context_brief.md и open_questions.md.

2. Выполни внешний поиск по теме (Semantic Scholar, arXiv).

3. Сформируй карту ландшафта: ключевые работы, методы, пробелы.

### Фаза 2: Генерация идей
1. Сгенерируй 5-10 идей на основе пробелов.

2. Для каждой: гипотеза, метод проверки, ожидаемый результат.

### Фаза 3: Фильтрация
1. Проверь новизну (поиск в вики + внешний).

2. Оцени по: новизна, реализуемость, влияние.

3. Отранжируй, выбери топ-3.

### Фаза 4: Запись
1. Создай страницу для каждой идеи:
   ```bash
   python3 tools/research_wiki.py slug "<название идеи>"
   ```

2. Запиши в wiki/ideas/<slug>.md.

### Фаза 5: Пилот (если --pilot)
1. Запусти /exp-design для лучшей идеи.

2. Запусти /exp-pilot-run.

3. Запусти /exp-pilot-eval.

## Выходы
- Страницы идей в wiki/ideas/
- Рёбра графа (origin_gaps → concepts/topics)
- Обновлён index.md, log.md

## Зависимости
### Инструменты
- `python3 tools/research_wiki.py slug "<title>"`
- `python3 tools/research_wiki.py add-edge wiki/ --from X --to Y --type Z`

### Скиллы
- /exp-design, /exp-pilot-run, /exp-pilot-eval
