from inputreader import aocinput
from day5 import TEST
from typing import List
from collections import defaultdict


class BOOST(TEST):
    def __init__(self, intcode: List[int],  input_values: List[int] or int = None):
        super().__init__(intcode, input_values)
        self.intcode = defaultdict(int)
        self.intcode.update(zip(range(len(intcode)), intcode))
        self.base = 0
        self.opcodes[9] = [self.adjust_base, 1]

    def adjust_base(self):
        self.base += self.getValue(1)

    def get_position(self, parameter):
        mode = self.modes[parameter-1]
        if mode == 2:
            return self.base + self.intcode[self.position + parameter]
        elif mode == 1:
            return self.position + parameter
        elif mode == 0:
            return self.intcode[self.position + parameter]
        else:
            raise ValueError('Mode out of range, must be 0,1 or 2')

    def getValue(self, parameter, output=False):
        return self.intcode[self.get_position(parameter)]

    def insert(self):
        value = self.get_input_value()
        self.intcode[self.get_position(1)] = value

    def output(self):
        self.log.append(self.getValue(1))

    def addition(self):
        self.intcode[self.get_position(3)] = self.getValue(1) + self.getValue(2)

    def multiplication(self):
        self.intcode[self.get_position(3)] = self.getValue(1) * self.getValue(2)

    def less_than(self):
        self.intcode[self.get_position(3)] = int(self.getValue(1) < self.getValue(2))

    def equals(self):
        self.intcode[self.get_position(3)] = int(self.getValue(1) == self.getValue(2))


def find_keycode(intcode: List[int])->int:
    boost = BOOST(intcode, [1])
    boost.run()

    return boost.log[-1]


def get_coordinates(intcode: List[int])->int:
    boost = BOOST(intcode, [2])
    boost.run()

    return boost.log[-1]


def main(day):
    data = aocinput(day)
    data = [int(i) for i in data[0].split(',')]
    result = find_keycode(data.copy())
    result2 = get_coordinates(data.copy())
    print(result, result2)


if __name__ == '__main__':
    main(9)
