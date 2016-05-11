import unittest


class TruncateCharsTestCase(unittest.TestCase):

    def setUp(self):
        self.s = "This is a wonderful world!"

    def test_truncatechars(self):
        self.assertEqual(truncatechars(self.s, 4), "This...")

    def test_truncatechars_no_chars(self):
        self.assertEqual(truncatechars(self.s, 0), "...")

    def test_truncatechars_limit_exceeded(self):
        self.assertEqual(truncatechars(self.s, 100), self.s)

    def test_truncatechars_invalid_value(self):
        with self.assertRaises(ValueError):
            truncatechars(False, 100)
