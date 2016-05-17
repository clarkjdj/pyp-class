import unittest


class CalculatorTestCase(unittest.TestCase):
    def test_calculator_with_one_operation(self):
        calc = Calculator(
            operations={
                'add': AddOperation
            }
        )
        res = calc.calculate(1, 5, 13, 2, 'add')
        self.assertEqual(res, 21)

    def test_calculator_with_multiple_operations(self):
        calc = Calculator(
            operations={
                'add': AddOperation,
                'subtract': SubtractOperation
            }
        )
        res = calc.calculate(1, 5, 13, 2, 'add')
        self.assertEqual(res, 21)
        res = calc.calculate(13, 3, 7, 'subtract')
        self.assertEqual(res, 3)

    def test_calculator_invoked_with_an_invalid_operation(self):
        calc = Calculator(
            operations={
                'add': AddOperation
            }
        )
        with self.assertRaises(OperationInvalidException):
            res = calc.calculate(1, 5, 13, 2, 'INVALID')


class AddOperationTestCase(unittest.TestCase):
    def test_add_operation_with_multiple_arguments(self):
        op = AddOperation(5, 1, 8, 3, 2)
        self.assertEqual(op.operate(), 19)

    def test_add_operation_with_1_arguments(self):
        op = AddOperation(5)
        self.assertEqual(op.operate(), 5)

    def test_add_operation_with_no_arguments(self):
        op = AddOperation()
        self.assertEqual(op.operate(), 0)


class SubtractOperationTestCase(unittest.TestCase):
    def test_subtract_operation_with_multiple_arguments(self):
        op = SubtractOperation(10, 1, 3, 2, 1)
        self.assertEqual(op.operate(), 3)

    def test_subtract_operation_with_1_arguments(self):
        op = SubtractOperation(5)
        self.assertEqual(op.operate(), 5)

    def test_subtract_operation_negative_result(self):
        op = SubtractOperation(5, 3, 3)
        self.assertEqual(op.operate(), -1)

    def test_subtract_operation_with_no_arguments(self):
        op = SubtractOperation()
        self.assertEqual(op.operate(), 0)
