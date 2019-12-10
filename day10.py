from __future__ import annotations
from inputreader import aocinput
from typing import List, Tuple, Dict
from fractions import Fraction
from math import gcd


class Asteroid:
    def __init__(self, coodinates: complex):
        self.coordinates = coodinates
        self.in_los = set()

    @property
    def x(self):
        return int(self.coordinates.real)

    @property
    def y(self):
        return int(self.coordinates.imag)

    def add_detectable(self, asteroid: Asteroid)->None:
        self.in_los.add(asteroid)

    def __repr__(self):
        return f"({self.x}, {self.y})"


def get_coordinates(data: List[str])-> List[complex]:
    return [complex(x,y) for y, line in enumerate(data) for x, char in enumerate(line) if char == '#']


def detector_location(data: List[str])->int:
    asteroids: Dict[complex, Asteroid] = {coord: Asteroid(coord) for coord in get_coordinates(data)}

    def in_los(a1: Asteroid, a2: Asteroid)->bool:
        if a1 is a2:
            return False
        if a2.y-a1.y == 0:
            xcoords = range(a1.x + 1, a2.x, 1)
            ycoords = [a1.y] * len(xcoords)  # same length list for zip
        elif a2.x - a1.x == 0:
            ycoords = range(a1.y + 1, a2.y, 1)
            xcoords = [a1.x] * len(ycoords)  # same length list for zip
        else:
            print('case 3', a1, a2)
            frac = Fraction(a2.x-a1.x, a2.y - a1.y)
            dx = frac.numerator
            dy = frac.denominator
            print(dx, dy)
            xcoords = range(a1.x + dx, a2.x, dx)
            ycoords = range(a1.y + dy, a2.y, dy)

        for x, y in zip(xcoords, ycoords):
            if complex(x, y) in asteroids:
                return False
        return True

    #for a1 in asteroids.values():
    a1 = asteroids[3+4j]
    for a2 in asteroids.values():
        if in_los(a1, a2):
            a1.add_detectable(a2)
            a2.add_detectable(a1)
    #for a in asteroids.values():
    #    print(a)
    return len(max(asteroids.values(), key=lambda x: len(x.in_los)).in_los)


def main(day):
    data = aocinput(day)
    result = detector_location(data)
    print(result)


if __name__ == '__main__':
    main(10)
