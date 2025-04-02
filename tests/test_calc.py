import math
import unittest
from math import inf

from parameterized import parameterized

from app.main import Calculator


class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()

    @parameterized.expand([
        ("integers", 2, 3, 6),
        ("floats", 2.5, 3.1, 5.6),
        ("negative", -2.5, 3.0, 0.5)
    ])
    def test_sum(self, name, a, b, expected_result):
        self.assertEqual(self.calc.sum(a, b), expected_result)

    @parameterized.expand([
        ("strings", 'aaa', 'bbb', TypeError),
        ("int_None", 1, None, TypeError),
        ("None_float", None, 1.1, TypeError),
        ("None_None", None, None, TypeError)
    ])
    def test_sum_invalid_values(self, name, a, b, expected_result):
        with self.assertRaises(expected_result):
            self.calc.sum(a, b)

    @parameterized.expand([
        ("list_integers", [1, 2, 3, 4], 10),
        ("list_empty", [], 0),
        ("list_single", [1], 1)
    ])
    def test_sum_list(self, name, a, expected_result):
        self.assertEqual(self.calc.sum(*a), expected_result)

    @parameterized.expand([
        ("tuple_integers", (1, 2, 3, 4), 10),
        ("tuple_empty", (), 0),
        ("tuple_single", (1,), 1),
        ("set_integers", {1, 2, 3, 4}, 10),
        ("set_empty", set(), 0),
        ("set_single", {1}, 1),
    ])
    def test_sum_tuple(self, name, a, expected_result):
        self.assertEqual(self.calc.sum(*a), expected_result)

    def test_multiply(self):
        a = 5
        b = 0.000000005
        self.assertAlmostEqual(self.calc.multiply(a, b), 1)

    def test_divide(self):
        with self.assertRaises(ZeroDivisionError):
            self.calc.divide(5, 0)

    def test_divide_inf(self):
        result = self.calc.divide(inf, inf)
        self.assertNotEqual(result, None)
        self.assertIsInstance(result, float)
        self.assertTrue(math.isinf(result) or not math.isnan(result))

if __name__ == "__main__":
    unittest.main()
