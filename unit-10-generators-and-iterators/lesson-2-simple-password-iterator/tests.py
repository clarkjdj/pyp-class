import unittest


class SimplePasswordGeneratorTestCase(unittest.TestCase):

    def test_password_generator_characters(self):
        it = SimplePasswordGenerator(available_chars=['a', 'b'], length=2)
        password = next(it)
        self.assertTrue(
            set(password) == set(['a', 'b']) or
            set(password) == set(['a']) or
            set(password) == set(['b']))

    def test_password_generator_length(self):
        self.assertEqual(len(next(SimplePasswordGenerator(length=2))), 2)
        self.assertEqual(len(next(SimplePasswordGenerator(length=4))), 4)
        self.assertEqual(len(next(SimplePasswordGenerator(length=16))), 16)

    def test_password_largest_length_than_available_chars(self):
        it = SimplePasswordGenerator(available_chars=['a', 'b'], length=8)
        password = next(it)
        self.assertTrue(
            set(password) == set(['a', 'b']) or
            set(password) == set(['a']) or
            set(password) == set(['b']))
        self.assertEqual(len(password), 8)
