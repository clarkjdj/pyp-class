import unittest


class ConvertTemperatureTestCase(unittest.TestCase):
    def test_fahrenheit_to_celsius(self):
        self.assertEqual(convert_temperature(32, to='celsius'), 0)

    def test_celsius_to_fahrenheit(self):
        self.assertEqual(convert_temperature(40, to='fahrenheit'), 104)

    def test_default_parameter_is_celsius(self):
        self.assertEqual(convert_temperature(32), 0)
