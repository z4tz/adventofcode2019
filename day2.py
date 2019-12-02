from inputreader import aocinput
from typing import List


def run_program(intcode: List[int], noun=12, verb=2) -> int:
    position = 0
    intcode[1] = noun
    intcode[2] = verb

    while intcode[position] != 99:
        if intcode[position] == 1:
            intcode[intcode[position+3]] = intcode[intcode[position+1]] + intcode[intcode[position+2]]
        elif intcode[position] == 2:
            intcode[intcode[position+3]] = intcode[intcode[position+1]] * intcode[intcode[position+2]]
        else:
            print('Opcode not identified', intcode[position])
            exit(99)
        position += 4
    return intcode[0]


def find_noun_verb(intcode: List[int]) -> int:
    for noun in range(100):
        for verb in range(100):
            if run_program(intcode.copy(), noun, verb) == 19690720:
                return 100*noun+verb


def main(day):
    data = aocinput(day)
    data = [int(value) for value in data[0].split(',')]
    result = run_program(data.copy())
    noun_verb = find_noun_verb(data.copy())
    print(result, noun_verb)


if __name__ == '__main__':
    main(2)
