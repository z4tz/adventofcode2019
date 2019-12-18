from inputreader import aocinput
from typing import Tuple, List
import re
from math import gcd


class Moon:
    def __init__(self, x: int, y: int, z: int):
        self.position = [int(x), int(y), int(z)]
        self.velocity = [0, 0, 0]
        self.initial_position = self.position.copy()

    def move(self):
        for i in range(3):
            self.position[i] += self.velocity[i]

    def __repr__(self):
        return '(' + ', '.join(str(pos) for pos in self.position) + ')'

    @property
    def total_energy(self):
        return sum((map(abs, self.position))) * sum(map(abs, self.velocity))


def total_energy(data: List[str], steps: int =1000, debug: bool = False) -> Tuple[int, int]:
    moons = [Moon(*re.match('<x=([-\d]*), y=([-\d]*), z=([-\d]*)>', line).groups()) for line in data]
    periodicity = [0, 0, 0]
    i = 0
    energy = 0
    while 0 in periodicity or i < steps:
        step(moons)
        for d in range(3):
            if back_to_start(moons, d) and not periodicity[d]:
                periodicity[d] = i + 1
        if debug:
            print('------', i+1, '----------')
            for moon in moons:
                print(moon.position, moon.velocity, moon.total_energy)
        if i == steps-1:
            energy = sum(moon.total_energy for moon in moons)
        i += 1
    return energy, least_common_multiple(periodicity)


def back_to_start(moons, i):
    for moon in moons:
        if moon.velocity[i] or moon.position[i] != moon.initial_position[i]:
            return False
    return True


def step(moons):
    for i, moon in enumerate(moons[:-1]):
        for other in moons[i + 1:]:
            for d in range(3):
                if moon.position[d] > other.position[d]:
                    moon.velocity[d] -= 1
                    other.velocity[d] += 1
                elif moon.position[d] < other.position[d]:
                    moon.velocity[d] += 1
                    other.velocity[d] -= 1
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
