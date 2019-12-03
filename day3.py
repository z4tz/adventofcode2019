from inputreader import aocinput
from typing import List, Tuple, Dict


direction = {'R': 1,
             'L': -1,
             'U': 1j,
             'D': -1j}


def get_wirecoords(wirepath: str) -> Dict[complex, int]:
    """
    Returns dict with each coordinate of the wire as a key paired with the length of wire from start to that coord.
    Complex numbers are used as coordinates with x-axis for real and y-axis for imaginary part
    Does not include starting coordinate
    """
    distances = dict()
    current_coord = 0j
    distance = 0
    for path in wirepath.split(','):  # path example: U32 | U direction, 32 number of steps
        d = direction[path[0]]
        for steps in range(int(path[1:])):
            current_coord += d
            distance += 1
            distances[current_coord] = distance
    return distances


def closest_intersection(wirepaths: List[str]) -> Tuple[int, int]:
    distances1 = get_wirecoords(wirepaths[0])
    distances2 = get_wirecoords(wirepaths[1])
    intersections = set(distances1.keys()).intersection(set(distances2.keys()))  # all coords where wires intersect
    closest = int(min(abs(intersection.real) + abs(intersection.imag) for intersection in intersections))
    shortest = min(distances1[intersection] + distances2[intersection] for intersection in intersections)
    return closest, shortest


def main(day):
    data = aocinput(day)
    result = closest_intersection(data)
    print(result)


if __name__ == '__main__':
    main(3)
