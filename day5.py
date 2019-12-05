from inputreader import aocinput
from day2 import IntcodeComputer
from typing import List
from inspect import signature


class TEST:
    def __init__(self, intcode: List[int]):
        self.intcode = intcode
        self.position = 0
        self.running = False
        self.log = []
        self.opcodes = {1: self.addition,
                        2: self.multiplication,
                        3: self.insert,
                        4: self.output,
                        5: self.jumpIfTrue,
                        6: self.jumpIfFalse,
                        7: self.lessThan,
                        8: self.equals,
                        99: self.stop}

    def addition(self, modes):
        value1 = self.intcode[self.position + 1] if modes[2] else self.intcode[self.intcode[self.position + 1]]
        value2 = self.intcode[self.position + 2] if modes[1] else self.intcode[self.intcode[self.position + 2]]
        value3 = self.intcode[self.position + 3]
        self.intcode[value3] = value1 + value2
        self.position += 4

    def multiplication(self, modes):
        value1 = self.intcode[self.position + 1] if modes[2] else self.intcode[self.intcode[self.position + 1]]
        value2 = self.intcode[self.position + 2] if modes[1] else self.intcode[self.intcode[self.position + 2]]
        value3 = self.intcode[self.position + 3]
        self.intcode[value3] = value1 * value2
        self.position += 4

    def get_input_value(self):
        return int(input('Input value to the TEST: '))

    def insert(self, modes):
        value1 = self.intcode[self.position + 1]
        self.intcode[value1] = self.get_input_value()
        self.position += 2

    def output(self, modes):
        value1 = self.intcode[self.position + 1]
        self.log.append(value1)
        self.position += 2

    def jumpIfTrue(self, modes):
        value1 = self.intcode[self.position + 1] if modes[2] else self.intcode[self.intcode[self.position + 1]]

        if self.intcode[value1]:
            self.position = self.intcode[self.position + 2]

    def jumpIfFalse(self, modes):
        if not self.intcode[self.position + 1]:
            self.position = self.intcode[self.position + 2]

    def lessThan(self, modes):
        pass

    def equals(self, modes):
        pass

    def stop(self, modes):
        self.running = False
        self.position += 1

    def run(self):
        self.running = True
        while self.running:
            opcode = f"{self.intcode[self.position]:05d}"  # get leading zeros visible
            try:
                instruction = self.opcodes[int(opcode[-2:])]
            except KeyError:
                print('Error, invalid opcode: ', opcode)
                exit()
            instruction([int(i) for i in opcode[:3]])


def main(day):
    data = aocinput(day)
    data = [int(value) for value in data[0].split(',')]
    test = TEST(data)
    test.run()


if __name__ == '__main__':
    main(5)
