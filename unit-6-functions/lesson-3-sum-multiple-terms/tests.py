import unittest


class MultipleSumTestCase(unittest.TestCase):

    def test_sum_multiple_terms(self):
        self.assertEqual(sum_multiple(2, 3), 5)
        self.assertEqual(sum_multiple(2, 3, 5, 7), 17)

    def test_sum_with_no_elements_raises_error(self):
        with self.assertRaises(AttributeError):
            sum_multiple()
