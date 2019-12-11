import unittest
from day10 import best_location, get_distance, get_angle, Asteroid


class MyTestCase(unittest.TestCase):
    def test_line_of_sight(self):
        setup = [".#..#",
                 ".....",
                 "#####",
                 "....#",
                 "...##"]

        self.assertEqual(8, detector_location(setup))

    def test_line_of_sight_2(self):
        setup = ["......#.#.",
                 "#..#.#....",
                 "..#######.",
                 ".#.#.###..",
                 ".#..#.....",
                 "..#....#.#",
                 "#..#....#.",
                 ".##.#..###",
                 "##...#..#.",
                 ".#....####"]
        self.assertEqual(33, best_location(setup))

    def test_distance(self):
        a1 = Asteroid(0 + 0j)
        a2 = Asteroid(1 + 0j)
        a3 = Asteroid(-3 - 4j)
        self.assertEqual(1, get_distance(a1, a2))
        self.assertEqual(5, get_distance(a1, a3))

    def test_angle(self):
        a1 = Asteroid(0 + 0j)
        a2 = Asteroid(1 + 0j)
        a3 = Asteroid(1 + 1j)
        a4 = Asteroid(-1 + 1j)
        a5 = Asteroid(-1 - 1j)
        a6 = Asteroid(0 + 1j)
        self.assertEqual(0, get_angle(a1, a2))
        self.assertAlmostEqual(45, get_angle(a1, a3))
        self.assertAlmostEqual(45, get_angle(a1, a4))
        self.assertAlmostEqual(-45, get_angle(a1, a5))
        self.assertAlmostEqual(90, get_angle(a1, a6))

    def test_part2(self):
        setup = [".#..##.###...#######",
                 "##.############..##.",
                 ".#.######.########.#",
                 ".###.#######.####.#.",
                 "#####.##.#.##.###.##",
                 "..#####..#.#########",
                 "####################",
                 "#.####....###.#.#.##",
                 "##.#################",
                 "#####.##.###..####..",
                 "..######..##.#######",
                 "####.##.####...##..#",
                 ".#####..#.######.###",
                 "##...#.##########...",
                 "#.##########.#######",
                 ".####.#.###.###.#.##",
                 "....##.##.###..#####",
                 ".#.#.###########.###",
                 "#.#.#.#####.####.###",
                 "###.##.####.##.#..##"]

        self.assertEqual(802 ,best_location(setup)[1])


if __name__ == '__main__':
    unittest.main()
