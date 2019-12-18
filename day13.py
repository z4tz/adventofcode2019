from inputreader import aocinput
from intcomp import Intcomp
from typing import List, Tuple, Dict
from collections import Counter, defaultdict
from matplotlib import pyplot as plt
from matplotlib.animation import ArtistAnimation
import numpy as np


class Arcade(Intcomp):
    def __init__(self, intcode: List[int]):
        intcode[0] = 2  # freeplay
        super().__init__(intcode)

    def _insert(self):
        if self._input:
            value = self._input.pop(0)
            self._intcode[self._get_position(1)] = value
        else:
            self._position -= 2  # adjust for not getting an input value.

    def board_update(self):
        """
        Run until next input is required, return all output that was generated before input was required
        """
        self.run_until(self._insert)
        output = self._log.copy()
        self._log.clear()
        return output


class Ball:
    def __init__(self, board):
        self.board = board
        self.x = 0
        self.y = 0
        self.prev_x = 0
        self.prev_y = 0

    @property
    def height(self):
        return 23 - self.y

    def move(self, x, y):
        self.prev_x = self.x
        self.prev_y = self.y
        self.x = x
        self.y = y

    def will_turn(self):
        x = self.x + 1 if self.x > self.prev_x else self.x - 1
        y = self.y + 1 if self.y > self.prev_y else self.y - 1

        #if x < 1 or x > 35:  # wall bounce
        #    return True

        if self.board[complex(x, self.y)]:  # side bounce
            if self.board[complex(self.prev_x, self.y)] or (self.board[complex(self.prev_x, y)] and not self.board[complex(self.x, y)]):  # double bounce
                return False
            return True

        if self.board[complex(x, y)] and not self.board[complex(self.x, y)]:  #corner bounce
            return True
        return False


def draw_screen(tiles: Dict[complex, int]):
    xmax = int(max(coord.real for coord in tiles.keys()))
    ymax = int(max(coord.imag for coord in tiles.keys()))

    board = np.zeros([ymax+1, xmax+1])
    for tile in tiles:
        board[int(tile.imag), int(tile.real)] = tiles[tile]

    return plt.imshow(board, animated=True)


def get_tiles(data: List[int]) -> Dict[complex, int]:
    comp = Intcomp(data)
    comp.run()
    log = comp.full_output()
    tiles = {}
    for i in range(len(log)//3):
        tiles[complex(log[i*3], log[i*3+1])] = log[i*3+2]
    return tiles


def predict_ball(ball: Ball) -> int:
    if ball.x and ball.prev_x:
        turnright = ball.x > ball.prev_x
        if ball.will_turn():
            turnright = not turnright
        if turnright:
            prediction = ball.x + (23 - ball.y) + (ball.y == 23)
            if prediction > 34:
                prediction = 68 - prediction
            return prediction
        else:
            prediction = ball.x - (23 - ball.y) - (ball.y == 23)
            if prediction < 1:
                prediction = 2 - prediction
            return prediction


def play(data: List[int]):
    images = []
    fig = plt.figure()
    comp = Arcade(data)
    tiles = defaultdict(int)
    ball = Ball(tiles)
    paddle_x = 18
    expected_paddle = 18
    log = []
    score = 0
    prediction = None
    while not comp.done:
        log = comp.board_update()
        for i in range(len(log) // 3):
            if log[i * 3 + 2] == 4:
                ball.move(log[i * 3], log[i * 3 + 1])

            if log[i * 3 + 2] == 3:
                paddle_x = log[i * 3]
            if log[i * 3] == -1 and log[i * 3 + 1] == 0:
                score = log[i * 3 + 2]
            else:
                tiles[complex(log[i * 3], log[i * 3 + 1])] = log[i * 3 + 2]
        prediction = predict_ball(ball)
        remaining = Counter(tiles.values())[2]
        #if remaining < 80:
        images.append([draw_screen(tiles)])

        if not prediction:
            prediction = paddle_x

        if prediction > ball.x:
            prediction = ball.x + 1
        if prediction < ball.x:
            prediction = ball.x - 1

        if prediction > expected_paddle:
            comp.add_input(1)
            expected_paddle += 1
        elif prediction < expected_paddle:
            comp.add_input(-1)
            expected_paddle -= 1
        else:
            comp.add_input(0)
    print(remaining)
    ani = ArtistAnimation(fig, images, interval=100)
    plt.show()
    return score


def care_package(data: List[int]) -> Tuple[int, int]:
    tiles = get_tiles(data.copy())
    score = play(data.copy())
    return Counter(tiles.values())[2], score


def main(day):
    data = aocinput(day)
    data = [int(part) for part in data[0].strip().split(',')]
    result = care_package(data)
    print(result)


if __name__ == '__main__':
    main(13)
