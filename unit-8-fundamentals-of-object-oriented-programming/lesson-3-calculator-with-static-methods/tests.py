import unittest


class CalculatorTestCase(unittest.TestCase):

    def test_add(self):
       self.assertEqual(Calculator.add(5, 2), 7)

    def test_subtract(self):
       self.assertEqual(Calculator.subtract(5, 2), 3)

    def test_multiply(self):
       self.assertEqual(Calculator.multiply(7, 9), 63)

    def test_divide(self):
       self.assertEqual(Calculator.divide(9, 3), 3.0)

    def test_divide_decimal(self):
       self.assertEqual(Calculator.divide(9, 2), 4.5)
