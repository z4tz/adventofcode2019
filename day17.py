from inputreader import aocinput
from intcomp import Intcomp
from typing import List


def drawScaffolding(output):
    data = []
    for num in output:
        if num == 10:
            print(''.join(data))
            data.clear()
        else:
            data.append(chr(num))


def findIntersections(data: List[int]):
    comp = Intcomp(data)
    comp.run()
    output = comp.full_output()
    drawScaffolding(output)
    x = 0
    y = 0
    scaffolding = set()
    intersections = set()
    robot = None
    for number in output:
        if number == 35:
            scaffolding.add((x, y))
            if {(x-1, y-1), (x, y-1), (x+1, y-1), (x, y-2)}.issubset(scaffolding):
                intersections.add((x, y-1))
        elif number == 94:
            robot = (x, y)
        if number == 10:
            y += 1
            x = 0
        else:
            x += 1
    print(robot)
    return sum(x * y for x, y in intersections)


def main(day):
    data = aocinput(day)
    data = [int(part) for part in data[0].strip().split(',')]
    result = findIntersections(data)
    print(result)



if __name__ == '__main__':
    main(17)
