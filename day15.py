from inputreader import aocinput
from typing import List
import numpy as np
from intcomp import Intcomp
from matplotlib import pyplot as plt


class Robot:
    def __init__(self, position: complex):
        self.position = position

    @property
    def x(self):
        return int(self.position.real)

    @property
    def y(self):
        return int(self.position.imag)


def neighbors(pos: complex) -> List[complex]:
    return [pos + 1, pos - 1, pos + 1j, pos - 1j]


def distance(pos1: complex, pos2: complex) -> int:
    return int(abs(pos1.real - pos2.real) + abs(pos1.imag - pos2.imag))


def direction(current, other):
    diff = current - other
    if diff == 1j:
        return 1
    if diff == -1j:
        return 2
    if diff == 1:
        return 3
    if diff == -1:
        return 4
    print('invalid direction', current, other)


def find_path(position: complex, goal: complex, grid: np.ndarray) ->List[complex]:
    visited = set()
    visited.add(position)
    path = []

    def step(pos):
        visited.add(pos)
        if distance(pos, goal) == 1:
            path.append(pos)
            return True

        for neighbor in neighbors(pos):
            if neighbor not in visited and grid[int(neighbor.imag), int(neighbor.real)] == 1:
                if step(neighbor):  # step returns true if goal is found further up
                    path.append(pos)
                    return True

        return False  # if no further path can be explored

    step(position)
    path.pop()  # remove current position as it gets added in current implementation
    return path


def find_oxygen(data: List[int]):

    def move_robot(goal):
        if distance(robot.position, attempt) > 1:
            path = find_path(robot.position, goal, grid)
            for pos in reversed(path):
                comp.add_input(direction(robot.position, pos))
                out = comp.next_output()
                if out != 1:
                    print('invalid path?')
                    exit()
                robot.position = pos

        # final step
        comp.add_input(direction(robot.position, goal))

    comp = Intcomp(data)
    grid = np.zeros([50, 50])  # 0 unknown, 1 traversable, 2 walls, 3 oxygen
    start = 25 + 25j
    robot = Robot(start)
    grid[robot.y, robot.x] = 1  # start position is traversable
    to_visit = neighbors(robot.position)
    len_to_oxygen = 0

    to_oxygenate = []  # for part 2

    while to_visit:
        attempt = to_visit.pop()  # get latest coord added (to minimize travel distance?)

        move_robot(attempt)

        output = comp.next_output()
        if output == 2:  # oxygen found
            robot.position = attempt
            grid[robot.y, robot.x] = 3
            len_to_oxygen = len(find_path(start, robot.position, grid)) + 1
            to_oxygenate.append(robot.position)

        elif output == 1:
            robot.position = attempt
            grid[robot.y, robot.x] = 1
            for neighbor in neighbors(robot.position):

                if not grid[int(neighbor.imag), int(neighbor.real)]:  # if unknown
                    to_visit.append(neighbor)
        elif output == 0:
            grid[int(attempt.imag), int(attempt.real)] = 2
        else:
            print('unknown output from intcomputer:', output)
            exit()

    minutes = -1  # -1 as the first minute is for the spread in location of oxygen system
    while to_oxygenate:
        spread = []
        for pos in to_oxygenate:
            grid[int(pos.imag), int(pos.real)] = 3
            for neighbor in neighbors(pos):
                if grid[int(neighbor.imag), int(neighbor.real)] == 1:
                    spread.append(neighbor)
        minutes += 1
        to_oxygenate = spread

    #plt.imshow(grid)
    #plt.show()

    return len_to_oxygen, minutes


def main(day):
    data = aocinput(day)
    data = [int(part) for part in data[0].strip().split(',')]
    result = find_oxygen(data)
    print(result)


if __name__ == '__main__':
    main(15)
