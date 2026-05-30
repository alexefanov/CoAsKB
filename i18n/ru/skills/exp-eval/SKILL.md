---
description: "Experiment verdict gate — Review LLM independently judges results → 4 verdict paths → auto-update the linked idea's status / failure_reason and graph edges"
lang: ru
argument-hint: "<experiment-slug> [--auto]"
---
# /exp-eval

> Оценить результаты эксперимента, вынести вердикт и обновить связанные страницы.

## Аргументы

- `--from <slug-эксперимента>` (обязательно): страница эксперимента
- `--result <файл>` (опц.): путь к файлу с результатами (если не указан — прочитать с диска)

## Поведение

1. Прочитай страницу эксперимента (гипотеза, метод, метрики, бейзлайн).
2. Загрузи результаты (из файла или из описания).
3. Сравни с метриками и бейзлайном.
4. Вынеси вердикт:
   - **Успех**: гипотеза подтверждена, метрики превзошли бейзлайн
   - **Неудача**: гипотеза не подтверждена
   - **Неопределённо**: данные неполны или неоднозначны
5. Обнови страницу эксперимента: status, outcome, key_result, date_completed.
6. Обнови связанную идею: status (validated/failed), date_resolved.
7. Добавь рёбра:
   ```bash
   python3 tools/research_wiki.py add-edge wiki/ --from experiments/<slug> --to ideas/<slug> --type supports --evidence "<вердикт>"
   ```

## Выходы
- Обновлённая страница эксперимента
- Обновлённая страница идеи
- Новые рёбра графа
- Запись в log.md

## Зависимости
### Инструменты
- `python3 tools/research_wiki.py set-meta <path> <field> <value>`
- `python3 tools/research_wiki.py add-edge wiki/ --from X --to Y --type Z`

