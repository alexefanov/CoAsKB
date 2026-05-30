---
description: "End-to-end research orchestrator — idea discovery → experiment design → execution → verdict → paper writing, with human gates and session-resumable state"
lang: ru
argument-hint: "<research-direction-or-brief> [--auto] [--start-from stage1|stage2|stage3|stage3-collect|stage3-check|stage4|stage5] [--skip-paper] [--venue ICLR|NeurIPS|ICML|ACL|CVPR]"
---
# /research


> Сквозной оркестратор исследования с человеческими шлюзами.

> Проводит полный цикл: идеация → эксперименты → статья.


## Аргументы


- `--topic <тема>` (обязательно): тема исследования

- `--deep` (опц.): глубокий режим (больше идей, экспериментов)

- `--quick` (опц.): быстрый режим (минимум итераций)


## Поведение


### Фаза 1: Идеация

1. Запусти /ideate для генерации идей по теме.

2. Покажи идеи пользователю. Жди утверждения.


### Фаза 2: Эксперименты

Для каждой утверждённой идеи:

1. Запусти /exp-design.

2. Запусти /exp-pilot-run.

3. Запусти /exp-pilot-eval.

4. Если пилот успешен — запусти /exp-run → /exp-eval.

5. Покажи результаты пользователю. Жди решения.


### Фаза 3: Статья

1. Запусти /paper-plan (из валидированных идей).

2. Запусти /paper-draft для каждого раздела.

3. Запусти /paper-compile.

4. Запусти /refine (до порога качества).

5. Покажи финальный результат.


## Человеческие шлюзы

После каждой фазы — покажи результат и жди подтверждения:

- Фаза 1: «Выберите идеи для проверки»

- Фаза 2: «Утвердите результаты экспериментов»

- Фаза 3: «Утвердите финальную статью»


## Выходы

- Страницы идей, экспериментов, плана, черновиков

- PDF статьи

- Записи в log.md


## Зависимости

### Скиллы

- /ideate, /exp-design, /exp-pilot-run, /exp-pilot-eval, /exp-run, /exp-eval

- /paper-plan, /paper-draft, /paper-compile, /refine
