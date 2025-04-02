import math

import pytest
from parameterized import parameterized

from app.error import InvalidInputException
from app.main import log


@pytest.fixture
def default_base():
    return 10

@parameterized.expand([
    (100, 10, 2),
    (8, 2, 3),
    (1, 10, 0),
])
def test_log_valid_cases(x, base, expected):
    assert math.isclose(log(x, base), expected, rel_tol=1e-9)

@parameterized.expand([
    ("abc", 10),
    (100, "xyz"),
    (None, 2),
])
def test_log_invalid_type(x, base):
    with pytest.raises(TypeError):
        log(x, base)

@parameterized.expand([
    (-1, 10),
    (0, 10),
    (100, -2),
    (100, 1),
])
def test_log_invalid_input_exception(x, base):
    with pytest.raises(InvalidInputException):
        log(x, base)
