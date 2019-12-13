from inputreader import aocinput
from typing import Tuple, List
import re
import numpy as np
from matplotlib import pyplot as plt
from math import gcd


class Moon:
    def __init__(self, x: int, y: int, z: int):
        self._position = np.array([x, y, z], dtype=int)
        self._velocity = np.zeros(3, dtype=int)
        self._initial_position = self._position.copy()
        self._periodicity = [0, 0, 0]

    def move(self):
        self._position += self._velocity

    def gravity(self, gravity):
        self._velocity += gravity

    def __repr__(self):
        return '(' + ', '.join(self.position) + ')'

    @property
    def position(self) -> np.array:
        return self._position

    @property
    def total_energy(self):
        return abs(self._position).sum() * abs(self._velocity).sum()

    def check_periodicity(self, steps: int):
        for i in range(3):
            if not self._periodicity[i] and self._position[i] == self._initial_position[i] and self._velocity[i] == 0:
                self._periodicity[i] = steps

    def periods_found(self):
        return self._periodicity.count(0) == 0


def total_energy(data: List[str], steps: int =7000, debug: bool = False) -> Tuple[int, int]:
    moons = [Moon(*re.match('<x=([-\d]*), y=([-\d]*), z=([-\d]*)>', line).groups()) for line in data]
    print(moons[1]._position)
    for i in range(steps):
        step(moons)
        for moon in moons:
            if not moon.periods_found():
                moon.check_periodicity(i+1)
        for d in range(3):
            if back_to_start(moons, d):
                print(i, 'hello')
        if debug:
            print('------', i+1, '----------')
            for moon in moons:
                print(moon.position, moon._velocity, moon.total_energy)
    periods = []
    for i in range(3):
        periods.append(least_common_multiple([moon._periodicity[i] for moon in moons]))
    print(least_common_multiple(periods))

    return sum(moon.total_energy for moon in moons)


def back_to_start(moons, i):
    return sum([moon._position[i] == moon._initial_position[i] and moon._velocity == 0 for moon in moons]) == 4



def step(moons):
    for i, moon in enumerate(moons[:-1]):
        for other in moons[i + 1:]:
            gravity = np.array([-1 if pos1 > pos2 else 1 if pos1 < pos2 else 0 for pos1, pos2 in zip(moon.position, other.position)])
            moon.gravity(gravity)
            other.gravity(-gravity)  # negative sign flips all values in array
    for moon in moons:
        moon.move()


def least_common_multiple(numbers: List[int]):
    """
    Finds the least common multiple for all numbers in list
    """
    lcm = numbers[0]
    for number in numbers:
        lcm = lcm*number // gcd(lcm, number)
    return lcm


def main(day):
    data = aocinput(day)
    result = total_energy(data, debug=False)
    print(result)


if __name__ == '__main__':
    main(12)
