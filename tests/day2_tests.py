import unittest
from day2 import run_program


class MyTestCase(unittest.TestCase):

    def test_1(self):
        testlist = [1, 9, 10, 3, 2, 3, 11, 0, 99, 30, 40, 50]
        self.assertEqual(run_program(testlist), [3500, 9, 10, 70, 2, 3, 11, 0, 99, 30, 40, 50])

    def test_2(self):
        testlist = [1,0,0,0,99]
        self.assertEqual(run_program(testlist), [2,0,0,0,99])

    def test_3(self):
        testlist = [2,3,0,3,99]
        self.assertEqual(run_program(testlist), [2,3,0,6,99])

    def test_4(self):
        testlist = [2,4,4,5,99,0]
        self.assertEqual(run_program(testlist), [2,4,4,5,99,9801])

    def test_5(self):
        testlist = [1,1,1,4,99,5,6,0,99]
        self.assertEqual(run_program(testlist), [30,1,1,4,2,5,6,0,99])


if __name__ == '__main__':
    unittest.main()
