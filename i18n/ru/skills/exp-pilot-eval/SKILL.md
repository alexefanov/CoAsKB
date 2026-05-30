---
description: Pilot result evaluation — read pilot results, apply success criteria, update idea page (pilot_result, failure_reason if failed), generate PILOT_VERDICT_REPORT. Called by /ideate Phase 5 after /exp-pilot-run.
argument-hint: <idea-slug> [--auto]

lang: ru---
# /exp-pilot-eval

> Оценить результаты пилотного эксперимента с лояльной логикой вердикта.

## Аргументы

- `--from <slug-пилота>` (обязательно): страница пилотного эксперимента

## Поведение

1. Прочитай страницу пилота.
2. Загрузи результаты.
3. Примени лояльную логику: пилот считается успешным, если:
   - Основная функциональность работает (допускаются незначительные баги)
   - Метрики хотя бы не хуже бейзлайна в пределах погрешности
   - Нет фатальных ошибок
4. Вынеси вердикт (успех/доработка/провал).
5. Обнови страницу пилота.
6. Если успех — рекомендую полный эксперимент (/exp-run).

## Зависимости
### Инструменты
- `python3 tools/research_wiki.py set-meta <path> <field> <value>`
