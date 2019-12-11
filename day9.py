from inputreader import aocinput
from typing import List
from intcomp import Intcomp


def find_keycode(intcode: List[int])->int:
    intcomp = Intcomp(intcode, [1])
    intcomp.run()
    return intcomp.next_output()


def get_coordinates(intcode: List[int])->int:
    intcomp = Intcomp(intcode, [2])
    intcomp.run()
    return intcomp.next_output()


def main(day):
    data = aocinput(day)
    data = [int(i) for i in data[0].split(',')]
    result = find_keycode(data.copy())
    result2 = get_coordinates(data.copy())
    print(result, result2)


if __name__ == '__main__':
    main(9)
