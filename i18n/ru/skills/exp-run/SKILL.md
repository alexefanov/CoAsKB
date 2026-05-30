---
description: "Full experiment execution pipeline — prepare code → deploy(Confirm with the user before operation and ask the applicant to conduct manual inspection) → monitor → collect results, supporting three run modes"
lang: ru
argument-hint: "<experiment-slug> [--review] [--collect] [--full] [--env local|remote]"
---
# /exp-run


> Реализовать, развернуть и отследить полный эксперимент (локально или на удалённом GPU).


## Аргументы


- `--from <slug-дизайна>` (обязательно): страница дизайна эксперимента

- `--local` (опц.): запустить локально

- `--remote` (опц.): запустить на удалённом GPU

- `--watch` (опц.): отслеживать выполнение в реальном времени


## Поведение


1. Прочитай дизайн эксперимента (метод, данные, метрики, бейзлайн).

2. Настрой окружение:

   ```bash

   python3 -m venv .venv

   .venv/bin/pip install -r requirements.txt

   ```

3. Реализуй код эксперимента (модель, датасет, метрики).

4. Разверни и запусти:

   ```bash

   python3 tools/run_experiment.py --config <slug> --mode full

   ```

5. Отслеживай прогресс, логируй метрики.

6. При завершении — собери результаты.

7. Обнови страницу эксперимента: status=completed, outcome, key_result.

8. Передай результаты в /exp-eval.


## Выходы

- Код эксперимента

- Результаты (метрики, графики)

- Обновлённая страница эксперимента

- Запись в log.md


## Зависимости

### Инструменты

- `python3 tools/run_experiment.py --config <slug> --mode full`

- `python3 tools/research_wiki.py set-meta <path> <field> <value>`


### Скиллы

- /exp-eval — для оценки результатов
