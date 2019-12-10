import unittest
from day10 import detector_location


class MyTestCase(unittest.TestCase):
    def test_line_of_sight(self):
        setup = [".#..#",
                 ".....",
                 "#####",
                 "....#",
                 "...##"]

        self.assertEqual(8, detector_location(setup))


if __name__ == '__main__':
    unittest.main()
