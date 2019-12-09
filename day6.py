from __future__ import annotations
from inputreader import aocinput
from typing import List, Tuple


class Planet:
    def __init__(self, name: str):
        self.name = name
        self.children = set()
        self.parent = None

    def add_child(self, child: Planet):
        self.children.add(child)

    def set_parent(self, parent: Planet):
        self.parent = parent

    def __repr__(self) -> str:
        return f"{self.name} - {len(self.children)} children"


def find_orbits(data: List[str]) -> Tuple[int, int]:
    planets = {}

    def getplanet(name: str) -> Planet:
        if name in planets:
            return planets[name]
        else:
            planets[name] = Planet(name)
            return planets[name]

    for line in data:
        parent, child = line.strip().split(')')
        parentPlanet = getplanet(parent)
        childPlanet = getplanet(child)
        parentPlanet.add_child(childPlanet)
        childPlanet.set_parent(parentPlanet)

    # Part 1
    current = [getplanet('COM')]
    orbits = 0
    step = 1
    while current:
        nextcurrent = []
        for planet in current:
            nextcurrent.extend(planet.children)
        orbits += len(nextcurrent) * step
        step += 1
        current = nextcurrent

    # Part 2
    transfers = 0
    current = [getplanet('YOU')]
    visited = set()
    while current:
        nextcurrent = []
        for planet in current:
            visited.add(planet)
            # gather all non visited neighbors
            nextcurrent.extend(child for child in planet.children if child not in visited)
            if planet.parent and planet.parent not in visited:
                nextcurrent.append(planet.parent)
        if getplanet('SAN') in nextcurrent:
            current = []
        else:
            current = nextcurrent
        transfers += 1

    return orbits, transfers - 2  # -2 to not count transfer from YOU and to  SAN


def main(day):
    data = aocinput(day)
    result = find_orbits(data)
    print(result)


if __name__ == '__main__':
    main(6)
