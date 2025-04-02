# Educational Project: Calculator with Unit Tests

## Project Description

This project includes a Python-based educational calculator and a suite of unit tests covering various functions of the calculator, specifically focusing on the `log()` function.

---

## Project Structure

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

## Completed Tasks (Homework)

### Task 1: Unit tests for the `log()` function

A new test class has been created to cover the `log()` function.

#### Tested Scenarios:

- ✅ Regular correct usage of the `log()` function.
- ✅ Testing function with incorrect data types (e.g., passing a string instead of a number).
- ✅ Verifying that the function correctly raises `InvalidInputException` when inputs are outside the domain of definition.

#### Tools used:
- `pytest`
- `pytest fixtures`
- Test parametrization using the `parameterized` module

#### Additional test cases:
- Added additional test cases for boundary values and extreme conditions.

---

### Task 2: Workshop Source Code

The workshop source code is available [here](https://drive.google.com/file/d/1bvzukw691GB7KIHzh9hVocIvsssqpUSn/view?usp=drive_link). This homework assignment continues the workshop project.

---

### Task 3: Test Structure

- Tests are created in a separate module located in the `tests` directory.
- The `parameterized` library is used for test parametrization.

---

## Dependency Installation

Install all dependencies using the following command:

```bash
pip install -r requirements.txt
```

---

## Running Tests

Run tests using the following command:

```bash
pytest --cov=app --cov-report=term --cov-report=html
```

---

## Linting (Ruff)

Check and automatically fix stylistic code errors:

```bash
ruff check .
ruff check --fix .
```
