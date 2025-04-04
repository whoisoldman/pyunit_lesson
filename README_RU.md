# Учебный проект: Калькулятор с Unit-тестами

## Описание проекта

Проект содержит учебный калькулятор, реализованный на Python, и набор unit-тестов, покрывающих различные функции калькулятора, в частности функцию `log()`.

---

## Структура проекта

```
PYUNIT_LESSON/
├─ .github/
│  └─ workflows/
│     ├─ ruff-lint.yml
│     └─ tests.yml
├─ app/
│  ├─ __init__.py
│  ├─ error.py
│  └─ main.py
├─ tests/
│  ├─ __init__.py
│  ├─ test_calc.py
│  └─ test_log.py
├─ .coveragerc
├─ .gitignore
├─ .gitattributes
├─ LICENSE
├─ README.md
├─ requirements-dev.in
├─ requirements-dev.txt
├─ requirements.in
├─ requirements.txt
└─ ruff.toml
```

---

## Выполненные задачи (Домашнее задание)

### Задание 1: Unit-тесты для функции log()

Создан новый тест-класс для покрытия функции `log()`.

#### Протестированы сценарии:

- ✅ Обычное корректное использование функции `log()`.
- ✅ Тестирование функции на неправильные типы входных данных (например, передача строки вместо числа).
- ✅ Проверка, что функция корректно бросает ошибку `InvalidInputException` при выходе входных данных за область допустимых значений (ОДЗ).

#### Использованные инструменты:
- `pytest`
- `pytest fixtures`
- Параметризация тестов с помощью модуля `parameterized`

#### Дополнительные тест-кейсы:
- Добавлены дополнительные кейсы на граничные значения и экстремальные случаи.

---

### Задание 2: Исходный код воркшопа

Исходный код для воркшопа доступен [по ссылке](https://drive.google.com/file/d/1bvzukw691GB7KIHzh9hVocIvsssqpUSn/view?usp=drive_link). Текущее домашнее задание является продолжением воркшопа.

---

### Задание 3: Структура тестов

- Тесты созданы в отдельном модуле в директории `tests`.
- Использована библиотека `parameterized` для параметризации тестов.

---

## Установка зависимостей

Установить все зависимости можно командой:

```bash
pip install -r requirements.txt
```

---

## Запуск тестов

Для запуска тестов используйте команду:

```bash
pytest --cov=app --cov-report=term --cov-report=html
```

---

## Линтинг (Ruff)

Проверка кода на стилистические ошибки и автоматическое исправление:

```bash
ruff check .
ruff check --fix .
```

---
