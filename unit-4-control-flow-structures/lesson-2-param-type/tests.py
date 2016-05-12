import unittest


class WhatIsThisTestCase(unittest.TestCase):

    def test_what_is_this_integer(self):
        self.assertEqual(what_is_this(10), "This is an Integer.")

    def test_what_is_this_string(self):
        self.assertEqual(what_is_this("Hello"), "This is a String.")

    def test_what_is_this_boolean(self):
        self.assertEqual(what_is_this(True), "This is a Boolean.")

    def test_what_is_this_float(self):
        self.assertEqual(what_is_this(10.92), "This is a Float.")

    def test_what_is_this_float(self):
        self.assertEqual(what_is_this(object()), "I have no idea what this is")
