from inputreader import aocinput
from typing import Tuple, List, Dict, Set
import math
from collections import deque, defaultdict


class Reaction:
    def __init__(self, text: str):
        req, out = text.split('=>')
        ammount, chem = out.strip().split(' ')
        self.output = [int(ammount), chem]
        self.requires = []
        self.depth = None  # how many reaction steps the output chemical requires to become ore
        for part in req.split(','):
            ammount, chem = part.strip().split(' ')
            self.requires.append([int(ammount), chem])

    @property
    def chemical(self):
        return self.output[1]


reactions: Dict[str, Reaction] = {}


def add_reactions(data: List[str]):
    for line in data:
        reaction = Reaction(line)
        reactions[reaction.chemical] = reaction


def expand(chemical: Tuple[int, str]) -> Tuple[List[Tuple[int, str]], Tuple[int, str]]:
    needed = []

    reaction = reactions[chemical[1]]
    to_produce = math.ceil(chemical[0] / reaction.output[0])
    rests = (to_produce * reaction.output[0] - chemical[0], chemical[1])
    for reactant in reaction.requires:
        needed.append((reactant[0] * to_produce, reactant[1]))
    return needed, rests


def find_depths():
    for reaction in reactions.values():
        depth = 1
        ingredients: Set[str] = {ingredient[1] for ingredient in reaction.requires}
        while ingredients != {'ORE'}:
            nextIngredients = set()
            for ingredient in ingredients:
                if ingredient != 'ORE':
                    nextIngredients.update([nextIngredient[1] for nextIngredient in reactions[ingredient].requires])
            ingredients = nextIngredients
            depth += 1
        reaction.depth = depth


def fuel_cost(fuel_amt=1) -> int:
    ore = 0
    needed = defaultdict(int)
    needed['FUEL'] = fuel_amt
    rests = defaultdict(int)
    queue = list(needed.keys())
    steps = 0
    while queue:
        queue.sort(key=lambda x: reactions[x].depth)
        chemName = queue.pop()
        if chemName in needed:
            toProduce = (needed.pop(chemName), chemName)
            if toProduce[1] in rests:  # try to use rests
                if rests[toProduce[1]] > toProduce[0]:  # if more or exact rests as needed
                    rests[toProduce[1]] -= toProduce[0]

                else:  # reduce how much needs to be produced, remove from rests
                    toProduce = (toProduce[0] - rests.pop(toProduce[1]), toProduce[1])  # a new tuple is needed

            if toProduce[0]:  # if not enough could be found in rests
                inp, rest = expand(toProduce)
                for chemical in inp:
                    if chemical[1] == 'ORE':
                        ore += chemical[0]
                    else:
                        needed[chemical[1]] += chemical[0]
                        queue.append(chemical[1])
                if rest[0]:
                    rests[rest[1]] += rest[0]
            steps += 1
    return ore


def fuel_ammount(data: List[str]) -> Tuple[int, int]:
    single_cost = fuel_cost(1)
    guess = math.ceil(10**12/single_cost)
    while True:
        cost = fuel_cost(guess)
        if cost > 10**12:
            return single_cost, guess - 1
        else:
            guess = math.floor(guess * (2 - cost / 10**12)) + 1


def main(day):
    data = aocinput(day)

    # setup
    add_reactions(data)
    find_depths()

    result = fuel_ammount(data)
    print(result)


if __name__ == '__main__':
    main(14)
