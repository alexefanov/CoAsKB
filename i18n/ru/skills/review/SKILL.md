---
description: General-purpose cross-model review — Review LLM independently reviews any research artifact, outputs structured scores, wiki entity mapping, and improvement suggestions
lang: ru
argument-hint: <artifact-path-or-slug> [--difficulty standard|hard|adversarial] [--focus method|evidence|writing|completeness]
---

# /review

> Межмодельная adversarial-рецензия любого исследовательского артефакта.

## Аргументы

- `--from <файл>` (обязательно): артефакт для рецензии (.tex, .md, .pdf)
- `--type <тип>` (опц.): тип рецензии: full (по умолч.) | quick | methodology | writing

## Поведение

1. Прочитай артефакт (статья, план, идея, постер).
2. Выполни анализ по критериям:
   - **Новизна**: насколько работа новая
   - **Корректность**: верны ли утверждения
   - **Полнота**: все ли аспекты покрыты
   - **Ясность**: понятен ли текст
   - **Цитирования**: уместны ли ссылки
3. Если доступен Review LLM (настройка в .env):
   - Передай артефакт на независимую рецензию
   - Сравни результаты
4. Составь сводный отчёт с оценками и рекомендациями.

## Выходы
- Отчёт рецензии с баллами и комментариями
- (Опц.) Сравнение с Review LLM

## Зависимости
### Скиллы
- /edit — для исправления по рецензии
