import unittest
import csv
from Calculator import Calculator

test_data_file_object = None


def load_test_data_into_list(test_data_file_path):
    global test_data_file_object
    my_list = list()
    test_data_file_object = open(test_data_file_path, 'r')
    csv_reader = csv.reader(test_data_file_object, delimiter=',')
    for row in csv_reader:
        my_list.append(row)
    test_data_file_object.close()
    test_data_file_object = None
    return my_list


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.calculator = Calculator()

    def tearDown(self) -> None:
        it self.calculator is not None:
            self.calculator = None

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.calculator, Calculator)

    def test_add_method_calculator(self):
        test_data = load_test_data_into_list('../src/addition.csv').data
        for row in test_data:
            result = float(row['Result'])
            self.assertEqual(self.calculator.add(row['Value 1'], row['Value 2']), int(row['Result']))
            self.assertEqual(self.calculator.result, int(row['Result']))

    def test_subtraction(self):
        test_data = load_test_data_into_list('../src/Subtraction.csv").data
        for row in test_data:
            result = float(row['Result'])
            self.assertEqual(self.calculator.subtract(row['Value 1'], row['Value 2']), int(row['Result']))
            self.assertEqual(self.calculator.result, int(row['Result']))

    def test_multiplication(self):
        test_data = load_test_data_into_list('../src/Multiplication.csv').data
        for row in test_data:
            result = float(row['Result'])
            self.assertEqual(self.calculator.multiply(row['Value 1'], row['Value 2']), int(row['Result']))
            self.assertEqual(self.calculator.result, int(row['Result']))

    def test_division(self):
        test_data = load_test_data_into_list('../src/Division.csv').data
        for row in test_data:
            result = float(row['Result'])
            self.assertEqual(self.calculator.divide(row['Value 1'], row['Value 2']), int(row['Result']))
            self.assertEqual(self.calculator.result, int(row['Result']))

    def test_Square(self):
        test_data = load_test_data_into_list('../src/Square.csv').data
        for row in test_data:
            result = float(row['Result'])
            self.assertEqual(self.calculator.square(row['Value 1'], int(row['Result']))
            self.assertEqual(self.calculator.result, int(row['Result']))

    def test_SquareRoot(self):
        test_data = load_test_data_into_list('../src/Squareroot.csv').data
        for row in test_data:
            result = float(row['Result'])
            self.assertEqual(self.calculator.square(row['Value 1'], int(row['Result']))
            self.assertEqual(self.calculator.result, int(row['Result']))


if __name__ == '__main__':
    unittest.main()
