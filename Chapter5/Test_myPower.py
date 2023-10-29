import unittest
import myPower

class MyTestCase(unittest.TestCase):
    def test_something(self):
        x = myPower.myPowerRec(8, 2)
        expected = 64
        self.assertEqual(expected, x)  # add assertion here

    def test_something1(self):
        x = myPower.myPowerRec(10, 5)
        expected = 100000
        self.assertEqual(expected, x)  # add assertion here

    def test_something1(self):
        x = myPower.myPowerRec(10, 0)
        expected = 1
        self.assertEqual(expected, x)  # add assertion here

    def test_something1(self):
        x = myPower.myPowerRec(2, 8)
        expected = 256
        self.assertEqual(expected, x)  # add assertion here

    def test_something1(self):
        x = myPower.myPowerRec(10, 1)
        expected = 10
        self.assertEqual(expected, x)  # add assertion here

if __name__ == '__main__':
    unittest.main()
