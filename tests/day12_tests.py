import unittest
from day12 import total_energy, least_common_multiple


class MyTestCase(unittest.TestCase):
    def test_movement(self):
        data = ["<x=-1, y=0, z=2>",
                "<x=2, y=-10, z=-7>",
                "<x=4, y=-8, z=8>",
                "<x=3, y=5, z=-1>"]

        self.assertEqual(179, total_energy(data, 10, debug=True))

    def test_energy(self):
        data = ["<x=-8, y=-10, z=0>",
                "<x=5, y=5, z=10>",
                "<x=2, y=-7, z=3>",
                "<x=9, y=-8, z=-3>"]

        self.assertEqual(1940, total_energy(data, 100, debug=True))

    def test_lcm(self):
        self.assertEqual(30, least_common_multiple([5, 10, 15]))
        self.assertEqual(30, least_common_multiple([15, 10, 5]))
        self.assertEqual(10, least_common_multiple([10, 10, 1]))


if __name__ == '__main__':
    unittest.main()
