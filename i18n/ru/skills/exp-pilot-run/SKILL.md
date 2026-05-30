---
description: Pilot experiment execution — read Pilot Spec YAML, write pilot code, run experiment(Confirm with the user before operation and require the applicant to conduct manual inspection), return results. Called by /ideate Phase 5. Does NOT modify wiki pages or judge pass/fail.
argument-hint: <idea-slug> [--env local|remote]

lang: ru---
# /exp-pilot-run

> Запустить пилотный эксперимент: написать код, развернуть, отследить, собрать результаты.

## Аргументы

- `--from <slug-дизайна>` (обязательно): страница дизайна эксперимента
- `--local` (опц.): запустить локально (по умолч.)
- `--remote` (опц.): запустить на удалённом сервере

## Поведение

1. Прочитай страницу дизайна эксперимента.
2. Подготовь окружение: зависимости, данные.
3. Напиши минимальный код пилота (упрощённая версия полного эксперимента).
4. Запусти пилот:
   ```bash
   python3 tools/run_experiment.py --config <slug> --mode pilot
   ```
5. Отслеживай выполнение.
6. Собери сырые результаты.
7. Обнови страницу пилота: status=running → completed, добавь run_log.
8. Передай результаты в /exp-pilot-eval.

## Выходы
- Код пилота
- Сырые результаты
- Обновлённая страница эксперимента

## Зависимости
### Инструменты
- `python3 tools/run_experiment.py --config <slug> --mode pilot`
