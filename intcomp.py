from typing import List, Callable
from collections import defaultdict


class Intcomp:
    def __init__(self, intcode: List[int], input_values: List[int] or int = None):
        self._intcode = defaultdict(int)  # default dict to facilitate expanding memory, todo: block negative memory?
        self._intcode.update(zip(range(len(intcode)), intcode))
        self._position = 0
        self._input = []
        if type(input_values) is int:
            self._input.append(input_values)
        elif type(input_values) is list:
            self._input.extend(input_values)
        self._log = []
        self._full_log = []
        self._modes = [0, 0, 0]
        self._base = 0
        self._previous_instruction = None
        self._opcodes = {1: [self._addition, 3],  # opcode for each method and how many parameters it takes
                         2: [self._multiplication, 3],
                         3: [self._insert, 1],
                         4: [self._output, 1],
                         5: [self._jump_if_true, 2],
                         6: [self._jump_if_false, 2],
                         7: [self._less_than, 3],
                         8: [self._equals, 3],
                         9: [self._adjust_base, 1],
                         99: [self._stop, 0]}
        self.running = False

    # helper functions

    def _get_position(self, parameter) -> int:
        """
        Returns the resulting position for the given parameter, adjusted for parameter mode
        """
        mode = self._modes[parameter - 1]
        if mode == 2:
            return self._base + self._intcode[self._position + parameter]
        elif mode == 1:
            return self._position + parameter
        elif mode == 0:
            return self._intcode[self._position + parameter]
        else:
            raise ValueError(f'Mode out of range, must be 0,1 or 2. Current modes:{self._modes}')

    def _get_value(self, parameter: int) -> int:
        """
        Returns stored value at position that the given parameter points to
        """
        return self._intcode[self._get_position(parameter)]

    # instruction functions

    def _addition(self):
        """
        Add param 1 and 2 and store to param 3 position
        """
        self._intcode[self._get_position(3)] = self._get_value(1) + self._get_value(2)

    def _multiplication(self):
        """
        Multiply param 1 and 2 and store to param 3 position
        """
        self._intcode[self._get_position(3)] = self._get_value(1) * self._get_value(2)

    def _insert(self):
        """
        Insert value next in line at param 1 position
        """
        if self._input:
            value = self._input.pop(0)
        else:
            value = int(input('Input value to the TEST: '))
        self._intcode[self._get_position(1)] = value

    def _output(self):
        """
        Log value at param 1 position
        """
        value = self._get_value(1)
        self._full_log.append(value)
        self._log.append(value)

    def _jump_if_true(self):
        if self._get_value(1):
            self._position = self._get_value(2)
            self._position -= 3  # correct for moving forward if jumping

    def _jump_if_false(self):
        if not self._get_value(1):
            self._position = self._get_value(2)
            self._position -= 3  # correct for moving forward if jumping

    def _less_than(self):
        self._intcode[self._get_position(3)] = int(self._get_value(1) < self._get_value(2))

    def _equals(self):
        self._intcode[self._get_position(3)] = int(self._get_value(1) == self._get_value(2))

    def _adjust_base(self):
        self._base += self._get_value(1)

    def _stop(self):
        self.running = False

    # public functions, interaction with Intcomp from outside

    def add_input(self, value: int):
        self._input.append(value)

    def step(self):
        """
        Step one instruction at a time
        """
        opstring = f"{self._intcode[self._position]:05d}"  # get leading zeros visible
        try:
            opcode = self._opcodes[int(opstring[-2:])]
            instruction = opcode[0]
            self._modes = [int(i) for i in reversed(opstring[:3])]
            instruction()
            self._position += opcode[1] + 1
            self._previous_instruction = instruction
        except KeyError:
            print('Error, invalid opcode: ', opstring)
            exit()

    def run(self):
        """
        Run continuous until stop instruction is reached
        """
        self.running = True
        while self.running:
            self.step()

    def run_until(self, instruction: Callable):
        """
        Run until a specific instruction is reached, or program ends
        """
        self.running = True
        while self.running and self._previous_instruction != instruction:
            self.step()
        self.running = False

    def next_output(self) -> int or None:
        """
        Gets the next output integer from the intcomp, returns None if program ends
        """
        if self._log:
            return self._log.pop(0)
        else:
            self.run_until(self._output)
            if self._log:  # check for log, if stop instruction reached no more input to be had
                return self._log.pop(0)
            else:
                return None

    def full_output(self) -> List[int]:
        """
        returns the full log for the program
        """
        return self._full_log
