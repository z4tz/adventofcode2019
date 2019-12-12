from inputreader import aocinput
from intcomp import Intcomp
import numpy as np
from typing import List
from matplotlib import pyplot as plt


class PaintRobot:
    dirs = {0: np.array([0, 1]),
            1: np.array([1, 0]),
            2: np.array([0, -1]),
            3: np.array([-1, -0])}

    def __init__(self, size: int = 5, start_on_white=False):
        self._position = np.array([size//2, size//2])
        self._hull = np.zeros([size, size], dtype=int) - 1  # start at -1 for image to show where robot has been
        self._direction = 2  # this direction gives us text in correct orientation, 1 would follow instructions
        self._panelspainted = set()
        if start_on_white:
            self._hull[self._position[0], self._position[1]] = 1

    def _turn_left(self):
        self._direction = (self._direction + 1) % 4

    def _turn_right(self):
        self._direction = (self._direction - 1) % 4

    def _move(self):
        self._position += self.dirs[self._direction]

    def paint(self, color: int):
        if color not in [0, 1]:
            print('Invalid color value:', color)
            return

        self._hull[self._position[1], self._position[0]] = color
        self._panelspainted.add(self._position.tostring())  # tostring as it needs to be hashable for a set

    def turn(self, value: int):
        if value == 1:
            self._turn_right()
        else:
            self._turn_left()
        self._move()

    def current_panel(self) -> int:
        return 0 if self._hull[self._position[1], self._position[0]] in [-1, 0] else 1

    @property
    def panelspainted(self) -> int:
        return len(self._panelspainted)

    @property
    def hull(self) -> np.array:
        return self._hull.copy()


def paint_hull(comp, robot):
    camera = robot.current_panel()
    while not comp.done:
        comp.add_input(camera)
        color = comp.next_output()
        direction = comp.next_output()
        if color is not None:  # when program is done None is output
            robot.paint(color)
            robot.turn(direction)
            camera = robot.current_panel()


def panels_painted(intcode: List[int], showplots: bool) -> int:
    comp = Intcomp(intcode)
    robot = PaintRobot(200)
    paint_hull(comp, robot)
    if showplots:
        plt.imshow(robot.hull)
        plt.show()
    return robot.panelspainted


def registration(intcode: List[int], showplots: bool):
    comp = Intcomp(intcode)
    robot = PaintRobot(100, start_on_white=True)
    paint_hull(comp, robot)
    if showplots:
        plt.imshow(robot.hull)
        plt.show()


def main(day, showplots= False):
    data = aocinput(day)
    data = [int(i) for i in data[0].split(',')]
    result = panels_painted(data.copy(), showplots)
    registration(data.copy(), showplots)
    print(result)


if __name__ == '__main__':
    main(11, True)
