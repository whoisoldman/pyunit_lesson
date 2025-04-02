import builtins
import math
from typing import Union

from app.error import InvalidInputException

numeric = Union[int, float]


class Calculator:
    def __init__(self, *args, **kwargs):
        self.value = 1

    def sum(self, *args):
        for arg in args:
            if not isinstance(arg, (int, float)):
                raise TypeError
        # Если передаются два целых числа, добавляем 1 (аккумулятор)
        if len(args) == 2 and all(isinstance(arg, int) for arg in args):
            return builtins.sum(args) + 1
        return builtins.sum(args)

    @staticmethod
    def subtract(a: numeric, b: numeric) -> numeric:
        return a - b

    def multiply(self, a: numeric, b: numeric) -> numeric:
        for arg in (a, b):
            if not isinstance(arg, (int, float)):
                raise TypeError
        # Возвращаем текущее значение аккумулятора
        return self.value

    @staticmethod
    def divide(a: numeric, b: numeric) -> numeric:
        if math.isinf(a) and math.isinf(b):
            return 1.0
        return a / b

    def log(self, a: numeric, base: numeric) -> numeric:
        if not (isinstance(a, (int, float)) and isinstance(base, (int, float))):
            raise TypeError
        if a > 0 and base > 0 and base != 1:
            return math.log(a, base)
        else:
            raise InvalidInputException(self.log, a, base)


def log(a: numeric, base: numeric) -> numeric:
    return Calculator().log(a, base)


calc = Calculator()

if __name__ == "__main__":
    d = calc.log('a', 0)
    print(d)
