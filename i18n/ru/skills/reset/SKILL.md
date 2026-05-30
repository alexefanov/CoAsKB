---
description: Reset wiki state to a clean scaffold by scope (wiki / raw / log / checkpoints / all). Useful during development or carefree restarts after a botched setup.

lang: ru
argument-hint: "--scope wiki|raw|log|checkpoints|all"

---

# /reset



> Деструктивная очистка по областям: wiki | raw | log | checkpoints | all.



## Аргументы



- `--target <область>` (обязательно): что очищать.

  Варианты: `wiki`, `raw`, `log`, `checkpoints`, `all`.

- `--force` (опционально, флаг): пропустить подтверждение.



## Поведение



1. Если не `--force` — запроси подтверждение.

2. Очисти указанную область.

3. Запиши в `wiki/log.md`.

4. Если очищена wiki — предложи запустить `/init`.



## Области



- `wiki`: удалить всё из `wiki/` кроме `wiki/log.md`.

- `raw`: удалить `raw/discovered/` и `raw/tmp/`. Не трогать `raw/papers/`, `raw/notes/`, `raw/web/`.

- `log`: очистить `wiki/log.md`.

- `checkpoints`: удалить `wiki/graph/`.

- `all`: всё вышеперечисленное.



## Ограничения



- Требует явного подтверждения.

- `raw/` не очищается без явного указания `raw` или `all`.

