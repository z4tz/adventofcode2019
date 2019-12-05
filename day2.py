from inputreader import aocinput
from typing import List


class IntcodeComputer:
    def __init__(self, intcode: List[int], noun=12, verb=2):
        self.position = 0
        self.intcode = intcode
        self.intcode[1] = noun
        self.intcode[2] = verb
        self.position = 0
        self.opcodes = {1: self.addition,
                        2: self.multiplication,
                        99: self.end}
        self.running = False

    def addition(self):
        icode = self.intcode
        icode[icode[self.position + 3]] = icode[icode[self.position + 1]] + icode[icode[self.position + 2]]
        self.position += 4

    def multiplication(self):
        icode = self.intcode
        icode[icode[self.position + 3]] = icode[icode[self.position + 1]] * icode[icode[self.position + 2]]
        self.position += 4

    def end(self):
        self.running = False

    def get_result(self):
        self.running = True
        while self.running:
            self.opcodes[self.intcode[self.position]]()
        return self.intcode[0]


def find_noun_verb(intcode: List[int]) -> int:
    for noun in range(100):
        for verb in range(100):
            comp = IntcodeComputer(intcode.copy(), noun, verb)
            if comp.get_result() == 19690720:
                return 100*noun+verb


def main(day):
    data = aocinput(day)
    data = [int(value) for value in data[0].split(',')]
    comp = IntcodeComputer(data.copy())
    result = comp.get_result()
    noun_verb = find_noun_verb(data.copy())
    print(result, noun_verb)


if __name__ == '__main__':
    main(2)
