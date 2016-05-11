import unittest


class String2NumberTestCase(unittest.TestCase):
    def test_cast_string_into_integer(self):
        self.assertEqual(string2number('2'), 2)

    def test_cast_string_into_float(self):
        self.assertEqual(string2number('2.8'), 2.8)

    def test_cast_invalid_string_value(self):
        with self.assertRaises(ValueError):
            string2number('invalid-value')

    def test_cast_invalid_data_type(self):
        with self.assertRaises(ValueError):
            string2number(True)
