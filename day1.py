from inputreader import aocinput
from math import floor
from typing import List


def fuel_required(mass: int) -> int:
    return floor(mass/3) - 2


def fuel_req_recursive(mass: int) -> int:
    fuel = fuel_required(mass)
    if fuel <= 0:
        return 0
    return fuel + fuel_req_recursive(fuel)


def sum_fuel(modulemasses: List[int]):
    fuel = sum(fuel_required(int(mass)) for mass in modulemasses)
    totalFuel = sum(fuel_req_recursive(int(mass)) for mass in modulemasses)
    return [fuel, totalFuel]


def main(day: int):
    data = aocinput(day)
    print(sum_fuel(data))


if __name__ == '__main__':
    main(0)
