import unittest
from CSVReader.CSVReader import CSVReader, ClassFactory
from pprint import pprint

class MyTestCase(unittest.TestCase):

        def setUp(self) -> None:
            self.csv_reader = CSVReader('addition.txt')

        def test_return_data_as_objects(self):
            people - self.csv_reader.return_data_as_objects('person')
            self.asserIsInstance(people, list)
            test_class = ClassFactory('person', self.csv_reader.data[0])
            for person in people:
                self.asserEqual(person.__name__, test_class.__name__)


if __name__ == '__main__':
    unittest.main()
