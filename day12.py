from inputreader import aocinput
from typing import Tuple, List
import re
import numpy as np
from matplotlib import pyplot as plt


class Moon:
    def __init__(self, x: int, y: int, z: int):
        self._position = np.array([x, y, z], dtype=int)
        self._velocity = np.zeros(3, dtype=int)

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

    # todo: look at periodicity for each of the position directions
    # todo: compare for all planets and get lowest common denominator?


def total_energy(data: List[str], steps: int =2000, debug: bool = False) -> int:
    moons = [Moon(*re.match('<x=([-\d]*), y=([-\d]*), z=([-\d]*)>', line).groups()) for line in data]
    for i in range(steps):
        step(moons)
        if debug:
            print('------', i+1, '----------')
            for moon in moons:
                print(moon.position, moon._velocity, moon.total_energy)
    return sum(moon.total_energy for moon in moons)


def step(moons):
    for i, moon in enumerate(moons[:-1]):
        for other in moons[i + 1:]:
            gravity = np.array([-1 if pos1 > pos2 else 1 if pos1 < pos2 else 0 for pos1, pos2 in zip(moon.position, other.position)])
            moon.gravity(gravity)
            other.gravity(-gravity)  # negative sign flips all values in array
    for moon in moons:
        moon.move()


def main(day):
    data = aocinput(day)
    result = total_energy(data)
    print(result)


if __name__ == '__main__':
    main(12)
