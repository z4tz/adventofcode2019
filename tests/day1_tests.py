import unittest

from day1 import fuel_required, fuel_req_recursive


class MyTestCase(unittest.TestCase):
    def test_mass_12(self):
        self.assertEqual(fuel_required(12), 2)

    def test_mass_14(self):
        self.assertEqual(fuel_required(14), 2)

    def test_mass_1969(self):
        self.assertEqual(fuel_required(1969), 654)

    def test_mass_100756(self):
        self.assertEqual(fuel_required(100756), 33583)

    def test_recursive_mass_14(self):
        self.assertEqual(fuel_req_recursive(14), 2)

    def test_recursive_mass_1969(self):
        self.assertEqual(fuel_req_recursive(1969), 966)

    def test_recursive_mass_100756(self):
        self.assertEqual(fuel_req_recursive(100756), 50346)


if __name__ == '__main__':
    unittest.main()
