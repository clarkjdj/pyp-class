import unittest


class LengthTestCase(unittest.TestCase):
    def test_length_multiple_words(self):
        self.assertEqual(length('hello world'), 11)

    def test_length_single_word(self):
        self.assertEqual(length('hello'), 5)

    def test_length_empty_string(self):
        self.assertEqual(length(''), 0)
