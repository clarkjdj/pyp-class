import string
import random


class SimplePasswordGenerator(object):

    def __init__(self, available_chars=None, length=8):
        if not available_chars:
            available_chars = list(
                string.ascii_lowercase + string.digits + string.punctuation)

        self.available_chars = available_chars
        self.length = length

    def __iter__(self):
        return self

    def next(self):  # use __next__ in Python 3.x
        return ''.join([random.choice(self.available_chars) for _ in range(self.length)])

    __next__ = next
