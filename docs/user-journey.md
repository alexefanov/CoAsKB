# Путь пользователя: от инициализации до первой статьи

## Этап 0: Настройка среды

```bash
/setup
```
Настройка API-ключей (Semantic Scholar, OpenReview, ArXiv, Email). Интерактивно.

---

## Этап 1: Инициализация wiki

```bash
/init "Обследование бетонных конструкций"
```
- Создаёт структуру wiki (papers/, concepts/, methods/, topics/, ideas/, experiments/)
- Заполняет фоновые знания (foundations/)
- Создаёт index.md
- Автоматически находит и загружает ключевые документы

**Результат:** пустая, но структурированная база знаний по теме.

---

## Этап 2: Загрузка документов

```bash
/ingest raw/papers/gost-31937-2024.pdf
/ingest raw/papers/sp-13-102-2003.pdf
/ingest https://arxiv.org/abs/2401.12345
```
- Извлекает текст, метаданные, цитаты
- Создаёт страницы papers/ с frontmatter
- Создаёт графовые рёбра: `cites`, `introduces_concept`, `uses_concept`, `builds_on`
- Обновляет index.md, biblio.md, terms.md

**Результат:** документы в wiki с семантическими связями.

---

## Этап 3: Поиск и расширение

```bash
/discover --topic "трансферное обучение в строительстве" --limit 20
/discover --from-wiki
```
- Ищет похожие статьи через Semantic Scholar
- Рекомендует кандидатов для загрузки
- Оценивает релевантность

**Результат:** список кандидатов для进一步 загрузки.

---

## Этап 4: Генерация идей

```bash
/ideate "Методы контроля трещин в бетоне"
```
- Анализирует текущее состояние wiki
- Ищет пробелы в знаниях
- Генерирует research-идеи с гипотезами
- Создаёт страницы ideas/
- Создаёт рёбра `addresses_gap`, `inspired_by`

**Результат:** список идей с приоритетами и гипотезами.

---

## Этап 5: Проектирование экспериментов

```bash
/exp-design idea-crack-detection
```
- Читает идею и связанные документы
- Проектирует эксперимент (метод, данные, метрики)
- Создаёт страницу experiments/
- Создаёт ребро `tested_by`

**Результат:** план эксперимента с методологией.

---

## Этап 6: Пилотный запуск

```bash
/exp-pilot-run idea-crack-detection
/exp-pilot-eval idea-crack-detection
```
- Запускает уменьшенную версию эксперимента
- Оценивает работоспособность подхода
- Корректирует план при необходимости

**Результат:** подтверждение/корректировка плана.

---

## Этап 7: Полный эксперимент

```bash
/exp-run exp-crack-detection-001 --full
/exp-eval exp-crack-detection-001
```
- Запускает полный цикл эксперимента
- Собирает результаты
- Оценивает: supported / partially_supported / not_supported
- Создаёт рёбра `supports` / `invalidates`
- Обновляет статус идеи

**Результат:** данные с вердиктом по гипотезе.

---

## Этап 8: Написание статьи

```bash
/survey "Контроль трещин в бетоне" --format latex --max-papers 30
/paper-plan idea-crack-detection --venue NeurIPS
/paper-draft papers/crack-detection/plan.md
```
- Генерирует Related Work (с цитатами)
- Составляет план статьи
- Пишет черновик по разделам

**Результат:** черновик статьи в LaTeX.

---

## Этап 9: Улучшение и проверка

```bash
/review papers/crack-detection --difficulty hard --focus method
/refine papers/crack-detection --max-rounds 3 --focus writing
/paper-compile papers/crack-detection --fix
```
- Экспертная проверка (методология, текст, полнота)
- Итеративное улучшение
- Компиляция LaTeX с исправлением ошибок

**Результат:** готовая статья к отправке.

---

## Этап 10: Отправка и рецензии

```bash
/share
```
- Отправка в конференцию
- Ожидание рецензий

---

## Этап 11: Ответ рецензентам

```bash
/rebuttal reviews/neurips-2024/review1.md --paper-slug crack-detection --venue NeurIPS
```
- Анализ замечаний
- Формирование ответа с дополнительными экспериментами
- При необходимости: доработка статьи

**Результат:** ответ на рецензии + доработанная статья.

---

## Дополнительные команды на любом этапе

| Команда | Когда |
|---------|-------|
| `/ask "Что такое модуль упругого отроска?"` | Вопрос к базе знаний |
| `/check --fix` | Проверка целостности wiki |
| `/visualize --obsidian` | Обновление графа связей |
| `/exp-status` | Мониторинг экспериментов |
| `/novelty "Новый метод сегментации"` | Проверка новизны |
| `/survey "Тема" --format markdown` | Обзор литературы |

---

## Типичная последовательность (сжато)

```
1. /setup
2. /init "Тема"
3. /ingest (повторять для каждого документа)
4. /discover --from-wiki (расширение)
5. /ideate "Направление"
6. /exp-design idea-xxx
7. /exp-pilot-run idea-xxx → /exp-pilot-eval idea-xxx
8. /exp-run exp-xxx --full → /exp-eval exp-xxx
9. /survey → /paper-plan → /paper-draft
10. /review → /refine → /paper-compile
11. /share
12. /rebuttal (после рецензий)
```

**Среднее время:** 1–2 недели от инициализации до отправки статьи.
