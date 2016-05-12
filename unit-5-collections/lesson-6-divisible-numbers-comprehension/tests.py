import unittest


class DivisibleNumbersTestCase(unittest.TestCase):
    def test_many_divisible_number(self):
        self.assertEqual(
            divisible_numbers([9, 8, 7, 6, 5, 4, 3, 2, 1], 3), [9, 6, 3])

    def test_empty_list(self):
        self.assertEqual(divisible_numbers([], 2), [])

    def test_no_result(self):
        self.assertEqual(divisible_numbers([2, 4, 8], 5), [])
