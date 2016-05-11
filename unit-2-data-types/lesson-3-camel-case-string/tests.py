import unittest


class CamelCaseTestCase(unittest.TestCase):
    def test_word_with_spaces(self):
        self.assertEqual(camel_case("testing 123 hello"), 'Testing 123 Hello')

    def test_single_word(self):
        self.assertEqual(camel_case("testing"), 'Testing')

    def test_empty_string(self):
        self.assertEqual(camel_case(""), '')
