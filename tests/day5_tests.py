import unittest
from day5 import TEST


class MyTestCase(unittest.TestCase):
    def test_something(self):
        arr = [1002,4,3,4,33]
        test = TEST(arr)
        test.run()
        self.assertEqual(test.intcode, [1002,4,3,4,99])


if __name__ == '__main__':
    unittest.main()
