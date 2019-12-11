from inputreader import aocinput
from typing import List, Tuple
from itertools import permutations
from day5 import TEST


class AMPTEST(TEST):
    def __init__(self, intcode: List[int],  input_values: List[int] or int = None):
        super().__init__(intcode, input_values)
        self.done = False

    def output(self):  # pauses the program on _output
        super().output()
        self.running = False

    def stop(self):
        self.done = True
        super(AMPTEST, self).stop()


def maximize_thrusters(data: List[int]) -> Tuple[int, int]:
    thrustersignals = []
    perms = permutations([0, 1, 2, 3, 4])  # all permutations of the settings
    for settings in perms:
        output = run_TESTs(data, settings)
        thrustersignals.append(output)
    amped_thrustersignals = []
    perms_amp = permutations([5, 6, 7, 8, 9])
    for setting in perms_amp:
        output = run_amplified_TESTs(data, setting)
        amped_thrustersignals.append(output)
    return max(thrustersignals), max(amped_thrustersignals)


def run_TESTs(data: List[int], settings) -> int:
    tests = [TEST(data.copy(), setting) for setting in settings]
    output = 0  # _input signal for first TEST
    for test in tests:
        test.input.append(output)
        test.run()
        output = test.log[-1]
    return output


def run_amplified_TESTs(data: List[int], settings) -> int:
    tests = [AMPTEST(data.copy(), setting) for setting in settings]
    output = 0  # _input signal for first TEST
    while True:
        for i, test in enumerate(tests):
            # each TEST is run until an _output, that _output is appended on the next and then run until _output...
            test.input.append(output)
            test.run()
            if test.done:
                return output
            else:
                output = test.log[-1]


def main(day):
    data = aocinput(day)
    result = maximize_thrusters([int(i) for i in data[0].split(',')])
    print(result)


if __name__ == '__main__':
    main(7)
