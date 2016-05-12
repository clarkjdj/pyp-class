import unittest
from datetime import date


class CountDaysTestCase(unittest.TestCase):

    def test_count_days_year(self):
        days = count_days(date(2015, 1, 1),
                          date(2016, 1, 1))
        self.assertEqual(days, 365)

    def test_count_days_month(self):
        days = count_days(date(2016, 1, 1),
                          date(2016, 2, 1))
        self.assertEqual(days, 31)

    def test_count_days_one_day(self):
        days = count_days(date(2016, 2, 1),
                          date(2016, 2, 2))
        self.assertEqual(days, 1)

    def test_count_days_no_difference(self):
        days = count_days(date(2016, 1, 1),
                          date(2016, 1, 1))
        self.assertEqual(days, 0)

    def test_count_days_invalid_order(self):
        with self.assertRaises(ValueError):
            days = count_days(date(2016, 1, 1),
                              date(2015, 1, 1))
