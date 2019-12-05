import unittest

from day4 import valid_password, extra_valid_password


class MyTestCase(unittest.TestCase):
    def test_validator(self):
        self.assertEqual(valid_password([1, 1, 1, 1, 1, 1]), True)
        self.assertEqual(valid_password([2, 2, 3, 4, 5, 0]), False)
        self.assertEqual(valid_password([1, 2, 3, 7, 8, 9]), False)

    def test_extra_validator(self):
        self.assertEqual(extra_valid_password([1, 1, 2, 2, 3, 3]), True)
        self.assertEqual(extra_valid_password([1, 2, 3, 4, 4, 4]), False)
        self.assertEqual(extra_valid_password([1, 1, 1, 1, 2, 2]), True)
        self.assertEqual(extra_valid_password([1, 1, 1, 2, 4, 5]), False)
        self.assertEqual(extra_valid_password([1, 1, 1, 1, 2, 3]), False)



if __name__ == '__main__':
    unittest.main()
