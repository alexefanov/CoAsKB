---
description: "Compile a paper outline from the idea graph — evidence map → narrative structure → section plan + figure plan + citation plan, Review LLM review mandatory"
lang: ru
argument-hint: "<idea-slugs...> --venue <ICLR|NeurIPS|ICML|ACL|CVPR|IEEE> [--title <working-title>]"
---
# /paper-plan


> Составить план статьи из валидированных идей + матрицы свидетельств.


## Аргументы


- `--from <slug1,slug2,...>` (обязательно): страницы идей, лежащих в основе статьи

- `--venue <название>` (опц.): целевой журнал/конференция для форматирования


## Поведение


1. Прочитай указанные страницы идей.

2. Построй матрицу свидетельств: какая идея какими экспериментами подтверждена.

3. Собери релевантные методы и понятия из вики.

4. Составь структуру статьи:

   - Title, Abstract

   - Introduction: проблема, пробел, вклад

   - Related Work: группировка по темам

   - Method: архитектура, ключевые решения

   - Experiments: настройки, результаты, анализ

   - Discussion: ограничения, выводы

5. Для каждого раздела укажи:

   - Какие идеи/методы/понятия цитировать

   - Какие фигуры/таблицы включить

6. Запиши страницу плана:

   ```yaml

   ---

   title: ""

   slug: ""

   venue: ""

   sections: [...]

   ---

   ```

7. Проверь BibTeX для всех запланированных цитат.


## Выходы

- Страница плана в wiki/outputs/

- Список BibTeX для цитирований

- Обновлён index.md


## Зависимости

### Инструменты

- `python3 tools/research_wiki.py slug "<title>"`

- `python3 tools/research_wiki.py find wiki/ experiments --field linked_idea <slug>`


### Скиллы

- /paper-draft — для написания разделов
