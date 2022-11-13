from enum import Enum


def mode_for_nth_parameter(code, n):
    code = code // 100
    divisor = 1
    for i in range(n - 1):
        divisor *= 10
    return code // divisor % 10


class IntcodeComputer:

    def __init__(self):
        self.stop_on_output = False
        self.debug_mode = False
        self.relative_base = 0
        self.position = 0
        self.input_idx = 0
        self.input = []
        self.output = []
        self.program = {}

    def import_program(self, input_program: list):
        for i in range(len(input_program)):
            self.program[i] = input_program[i]

    def set_stop_on_output(self, value: bool):
        self.stop_on_output = value

    def accept_input(self, added_input: list):
        for val in added_input:
            self.input.append(val)

    def reset_output(self):
        self.output = []

    def interpret_nth_param(self, param_number: int):
        mode = mode_for_nth_parameter(self.program.get(self.position, 0), param_number)

        if mode == 0:
            return self.program.get(self.program.get(self.position + param_number, 0), 0)

        if mode == 1:
            return self.program.get(self.position + param_number, 0)

        if mode == 2:
            return self.program.get(self.relative_base + self.program.get(self.position + param_number, 0), 0)

        raise ValueError

    def interpret_write_address(self, param_number: int):
        mode = mode_for_nth_parameter(self.program.get(self.position, 0), param_number)

        if mode == 0:
            return self.program.get(self.position + param_number, 0)

        if mode == 1:
            return self.position + param_number

        if mode == 2:
            return self.relative_base + self.program.get(self.position + param_number, 0)

        raise ValueError

    def compute_while_possible(self):

        while self.program[self.position] != 99:

            operation = self.program[self.position] % 100

            self.print_debug()

            if operation == 1:
                a = self.interpret_nth_param(1)
                b = self.interpret_nth_param(2)
                self.program[self.interpret_write_address(3)] = a + b
                self.position += 4

            if operation == 2:
                a = self.interpret_nth_param(1)
                b = self.interpret_nth_param(2)
                self.program[self.interpret_write_address(3)] = a * b
                self.position += 4

            if operation == 3:
                if len(self.input) <= self.input_idx:
                    return StoppingCondition.EXPECTING_INPUT
                self.program[self.interpret_write_address(1)] = self.input[self.input_idx]
                self.input_idx += 1
                self.position += 2

            if operation == 4:
                a = self.interpret_nth_param(1)
                self.output.append(a)
                self.position += 2
                if self.stop_on_output:
                    return StoppingCondition.STOP_ON_OUTPUT

            if operation == 5:
                a = self.interpret_nth_param(1)
                if a != 0:
                    self.position = self.interpret_nth_param(2)
                else:
                    self.position += 3

            if operation == 6:
                a = self.interpret_nth_param(1)
                if a == 0:
                    self.position = self.interpret_nth_param(2)
                else:
                    self.position += 3

            if operation == 7:
                a = self.interpret_nth_param(1)
                b = self.interpret_nth_param(2)
                self.program[self.interpret_write_address(3)] = int(a < b)
                self.position += 4

            if operation == 8:
                a = self.interpret_nth_param(1)
                b = self.interpret_nth_param(2)
                self.program[self.interpret_write_address(3)] = int(a == b)
                self.position += 4

            if operation == 9:
                a = self.interpret_nth_param(1)
                self.relative_base += a
                self.position += 2

            if operation > 9:
                raise ValueError

        return StoppingCondition.END_OF_PROGRAM

    def print_debug(self):

        if not self.debug_mode:
            return

        max_idx = max(self.program.keys())
        non_zero = {}
        for i in range(max_idx + 1):
            val = self.program.get(i)
            if val is not None and val != 0:
                non_zero[i] = val

        print("DEBUG:", self.position, non_zero)


class StoppingCondition(Enum):
    END_OF_PROGRAM = 0,
    EXPECTING_INPUT = 1,
    STOP_ON_OUTPUT = 2
