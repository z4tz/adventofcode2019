import unittest
from day3 import get_wirecoords, closest_intersection


class MyTestCase(unittest.TestCase):
    def test_distances(self):
        self.assertEqual(get_wirecoords('R2,U1,L3,D2'),
                         {1+0j: 1, 2+0j: 2, 2+1j: 3, 1+1j: 4, 0+1j: 5, -1+1j: 6, -1+0j: 7, -1-1j: 8})

    def test_intersection_1(self):
        wire1 = 'R8,U5,L5,D3'
        wire2 = 'U7,R6,D4,L4'
        self.assertEqual(closest_intersection([wire1, wire2])[0], 6)

    def test_intersection_2(self):
        wire1 = 'R75,D30,R83,U83,L12,D49,R71,U7,L72'
        wire2 = 'U62,R66,U55,R34,D71,R55,D58,R83'
        self.assertEqual(closest_intersection([wire1, wire2])[0], 159)

    def test_intersection_3(self):
        wire1 = 'R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51'
        wire2 = 'U98,R91,D20,R16,D67,R40,U7,R15,U6,R7'
        self.assertEqual(closest_intersection([wire1, wire2])[0], 135)


if __name__ == '__main__':
    unittest.main()
