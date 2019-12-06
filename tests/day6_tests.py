import unittest
from day6 import find_orbits


class MyTestCase(unittest.TestCase):
    def test_part1(self):
        testlist = ["COM)B",
                    "B)C",
                    "C)D",
                    "D)E",
                    "E)F",
                    "B)G",
                    "G)H",
                    "D)I",
                    "E)J",
                    "J)K",
                    "K)L"]

        self.assertEqual(find_orbits(testlist)[0], 42)

    def test_part2(self):
        testlist = ["COM)B",
                    "B)C",
                    "C)D",
                    "D)E",
                    "E)F",
                    "B)G",
                    "G)H",
                    "D)I",
                    "E)J",
                    "J)K",
                    "K)L",
                    "K)YOU",
                    "I)SAN"]

        self.assertEqual(find_orbits(testlist)[1], 4)


if __name__ == '__main__':
    unittest.main()
