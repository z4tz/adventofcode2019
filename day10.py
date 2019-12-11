from __future__ import annotations
from inputreader import aocinput
from typing import List, Tuple, Dict
from math import gcd, sin, pi, asin


class Asteroid:
    def __init__(self, coodinates: complex):
        self.coordinates = coodinates
        self.in_los = set()

    @property
    def x(self) -> int:
        return int(self.coordinates.real)

    @property
    def y(self) -> int:
        return int(self.coordinates.imag)

    def add_detectable(self, asteroid: Asteroid) -> None:
        self.in_los.add(asteroid)

    def clear_detected(self):
        self.in_los.clear()

    def __repr__(self):
        return f"({self.x}, {self.y})"


def get_coordinates(data: List[str]) -> List[complex]:
    return [complex(x, y) for y, line in enumerate(data) for x, char in enumerate(line) if char == '#']


def get_distance(a1: Asteroid, a2: Asteroid) -> float:
    return ((a1.x-a2.x)**2 + (a1.y-a2.y)**2)**0.5


def get_angle(a1: Asteroid, a2: Asteroid) -> float:
    dy = a1.y - a2.y
    distance = get_distance(a1, a2)
    return asin(dy/distance) / pi * 180


def best_location(data: List[str]) -> Tuple[int, int]:
    asteroids = {coord: Asteroid(coord) for coord in get_coordinates(data)}

    def in_los(a1: Asteroid, a2: Asteroid) -> bool:
        if a1 is a2:
            return False
        if a2.y - a1.y == 0:
            xcoords = range(a1.x + 1, a2.x, -int((a1.x-a2.x)/abs(a1.x-a2.x)))
            ycoords = [a1.y] * len(xcoords)  # same length list for zip
        elif a2.x - a1.x == 0:
            ycoords = range(a1.y + 1, a2.y, -int((a1.y-a2.y)/abs(a1.y-a2.y)))
            xcoords = [a1.x] * len(ycoords)  # same length list for zip
        else:

            dx = a2.x - a1.x
            dy = a2.y - a1.y
            g = gcd(dx, dy)
            dx //= g
            dy //= g

            xcoords = range(a1.x + dx, a2.x, dx)
            ycoords = range(a1.y + dy, a2.y, dy)
        for x, y in zip(xcoords, ycoords):
            if complex(x, y) in asteroids:
                return False
        return True

    for a1 in asteroids.values():
        for a2 in asteroids.values():
            if in_los(a1, a2):
                a1.add_detectable(a2)
                a2.add_detectable(a1)
    best = max(asteroids.values(), key=lambda x: len(x.in_los))
    result1 = len(best.in_los)

    # part 2
    asteroids = list(asteroids.values())
    removed = []
    while len(removed) < 200:

        firstHalf = []
        secondHalf = []

        for a in best.in_los:
            if a.x >= best.x:
                firstHalf.append((a, get_angle(best, a)))
            else:
                secondHalf.append((a, get_angle(best, a)))
        firstHalf.sort(key=lambda x: x[1], reverse=True)
        secondHalf.sort(key=lambda x: x[1])
        removed.extend(item[0] for item in firstHalf)
        removed.extend(item[0] for item in secondHalf)
        for a1 in firstHalf + secondHalf:
            asteroids.remove(a1[0])
        best.clear_detected()
        for a2 in asteroids:
            if in_los(best, a2):
                best.add_detectable(a2)

    return result1, removed[199].x*100 + removed[199].y


def main(day):
    data = aocinput(day)
    result = best_location(data)
    print(result)


if __name__ == '__main__':
    main(10)
