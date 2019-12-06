from inputreader import aocinput
from typing import List


class TEST:
    def __init__(self, intcode: List[int]):
        self.intcode = intcode
        self.position = 0
        self.running = False
        self.input = None
        self.log = []
        self.modes = [0, 0, 0]
        self.opcodes = {1: [self.addition, 3],  # opcode for each method and how many parameters it takes
                        2: [self.multiplication, 3],
                        3: [self.insert, 1],
                        4: [self.output, 1],
                        5: [self.jump_if_true, 2],
                        6: [self.jump_if_false, 2],
                        7: [self.less_than, 3],
                        8: [self.equals, 3],
                        99: [self.stop, 0]}

    def getValue(self, parameter):
        return self.intcode[self.position + parameter] if self.modes[parameter-1] else self.intcode[self.intcode[self.position + parameter]]

    def addition(self):
        self.intcode[self.intcode[self.position + 3]] = self.getValue(1) + self.getValue(2)

    def multiplication(self):
        self.intcode[self.intcode[self.position + 3]] = self.getValue(1) * self.getValue(2)

    def get_input_value(self):
        if self.input is not None:
            return self.input
        else:
            return int(input('Input value to the TEST: '))

    def insert(self):
        self.intcode[self.intcode[self.position + 1]] = self.get_input_value()

    def output(self):
        self.log.append(self.getValue(1))

    def jump_if_true(self):
        if self.getValue(1):
            self.position = self.getValue(2)
            self.position -= 3  # correct for moving forward if jumping

    def jump_if_false(self):
        if not self.getValue(1):
            self.position = self.getValue(2)
            self.position -= 3  # correct for moving forward if jumping

    def less_than(self):
        self.intcode[self.intcode[self.position + 3]] = int(self.getValue(1) < self.getValue(2))

    def equals(self):
        self.intcode[self.intcode[self.position + 3]] = int(self.getValue(1) == self.getValue(2))

    def stop(self):
        self.running = False

    def run(self):
        self.running = True
        while self.running:
            opcode = f"{self.intcode[self.position]:05d}"  # get leading zeros visible
            try:
                instruction = self.opcodes[int(opcode[-2:])][0]
                self.modes = [int(i) for i in reversed(opcode[:3])]
                instruction()
                self.position += self.opcodes[int(opcode[-2:])][1] + 1
            except KeyError:
                print('Error, invalid opcode: ', opcode)
                exit()


def main(day):
    data = aocinput(day)
    data = [int(value) for value in data[0].split(',')]

    test = TEST(data.copy())
    test.input = 1
    test.run()
    print(test.log[-1])

    # part 2
    test = TEST(data.copy())
    test.input = 5
    test.run()
    print(test.log[-1])


if __name__ == '__main__':
    main(5)
