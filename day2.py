from inputreader import aocinput
from typing import List
from intcomp import Intcomp


class IntcompExtract(Intcomp):
    def get_intcode(self, position: int) -> int:
        return self._intcode[position]

    def set_intcode(self, position: int, value: int):
        self._intcode[position] = value


def find_noun_verb(intcode: List[int]) -> int:
    for noun in range(100):
        for verb in range(100):
            comp = IntcompExtract(intcode.copy())
            comp.set_intcode(1, noun)
            comp.set_intcode(2, verb)
            comp.run()
            if comp.get_intcode(0) == 19690720:
                return 100*noun+verb


def main(day):
    data = aocinput(day)
    data = [int(value) for value in data[0].split(',')]
    comp = IntcompExtract(data.copy())
    comp.set_intcode(1, 12)
    comp.set_intcode(2, 2)
    comp.run()
    result = comp.get_intcode(0)
    noun_verb = find_noun_verb(data.copy())
    print(result, noun_verb)


if __name__ == '__main__':
    main(2)
