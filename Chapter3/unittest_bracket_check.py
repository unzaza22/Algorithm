import unittest
from bracket_check import bracket_check


class MyTestCase(unittest.TestCase):
    def test_no_error(self):
        test_string = '[{(Hello)}]'
        isError, location = bracket_check(test_string)
        self.assertEqual(isError, False)  # add assertion here
        self.assertEqual(location, [])  # add assertion here

    def test_error_1(self):
        test_string = '[{(Hello})]'
        isError, location = bracket_check(test_string)
        self.assertEqual(isError, True)  # add assertion here
        self.assertEqual(location, [8,9])  # add assertion here

    def test_error_2(self):
        test_string = '[{(Hello'
        isError, location = bracket_check(test_string)
        self.assertEqual(isError, True)  # add assertion here
        self.assertEqual(location, [0,1,2])  # add assertion here

    def test_error_3(self):
        test_string = 'Hello)('
        isError, location = bracket_check(test_string)
        self.assertEqual(isError, True)  # add assertion here
        self.assertEqual(location, [5,6])  # add assertion here

    def test_error_4(self):
        test_string = '{}{'
        isError, location = bracket_check(test_string)
        self.assertEqual(isError, True)  # add assertion here
        self.assertEqual(location, [2])  # add assertion here


    def test_error_5(self):
        test_string = 'H))('
        isError, location = bracket_check(test_string)
        self.assertEqual(isError, True)  # add assertion here
        self.assertEqual(location, [1,2,3])  # add assertion here


if __name__ == '__main__':
    unittest.main()
