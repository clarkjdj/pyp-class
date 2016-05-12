import unittest
from datetime import datetime


class FormatDatetimeTestCase(unittest.TestCase):

    def test_format_datetime(self):
        dt = datetime(2016, 1, 5, 13, 30)
        self.assertEqual(format_datetime(dt),
                         "Tuesday January 05th, 2016 at 13:30 hs")

    def test_format_datetime_1st(self):
        dt = datetime(2016, 1, 1, 13, 30)
        self.assertEqual(format_datetime(dt),
                         "Friday January 01st, 2016 at 13:30 hs")

    def test_format_datetime_2nd(self):
        dt = datetime(2016, 1, 2, 13, 30)
        self.assertEqual(format_datetime(dt),
                         "Saturday January 02nd, 2016 at 13:30 hs")

    def test_format_datetime_3rd(self):
        dt = datetime(2016, 1, 3, 13, 30)
        self.assertEqual(format_datetime(dt),
                         "Sunday January 03rd, 2016 at 13:30 hs")
