class Calculator(object):
    def __init__(self):
        pass

    @staticmethod
    def add(num1, num2):
        return num1 + num2

    @classmethod
    def subtract(cls, num1, num2):
        return cls.add(num1, num2 * -1)

    @staticmethod
    def multiply(num1, num2):
        return num1 * num2

    @staticmethod
    def divide(num1, num2):
        return float(num1) / num2
