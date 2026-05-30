---
description: "General-purpose multi-round iterative improvement — repeatedly calls /review on any research artifact, parses feedback, applies fixes, updates wiki, until the target score is reached"
lang: ru
argument-hint: "<artifact-slug-or-path> [--max-rounds N] [--target-score N] [--difficulty standard|hard|adversarial] [--focus method|evidence|writing|completeness]"
---
# /refine
> Многораундовое улучшение: создать → рецензировать → исправить → перерецензировать.

## Аргументы
- `--from <файл>` (обязательно): исходный артефакт (.tex/.md)
- `--skill <скилл>` (обязательно): какой скилл использовать для создания (paper-draft, poster, survey)
- `--rounds <N>` (опционально. число раундов (по умолч. 3)
- `--quality <порог>` (опционально): порог качества для остановки (high/medium, по умолч. high)

## Поведение
1. **Раунд 1**: Создай артефакт через указанный скилл.
2. **Рецензия**: Передай артефакт в /review.
3. **Исправление**: Внеси исправления по замечаниям (через /edit).
4. **Перерецензия**: Снова передай в /review.
5. Повторяй шаги 3-4, пока:
   - Не достигнут порог качества, ИЛИ
   - Не превышено макс. число раундов
6. Запиши историю улучшений.

## Выходы
- Улучшенный артефакт
- История раундов (оценки, изменения)

## Зависимости
### Скиллы
- /review — рецензия
- /edit — исправление
