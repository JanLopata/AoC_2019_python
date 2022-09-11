import os
from itertools import permutations


def run_program(program: list, x_inputs, x_outputs, stop_on_output=False, pos=0):
    program = [x for x in program]
    input_idx = 0

    while program[pos] != 99:

        operation = program[pos] % 100

        if operation == 1:
            a = interpret_nth_param(program, pos, 1)
            b = interpret_nth_param(program, pos, 2)
            program[program[pos + 3]] = a + b
            pos += 4

        if operation == 2:
            a = interpret_nth_param(program, pos, 1)
            b = interpret_nth_param(program, pos, 2)
            program[program[pos + 3]] = a * b
            pos += 4

        if operation == 3:
            program[program[pos + 1]] = x_inputs[input_idx]
            input_idx += 1
            pos += 2

        if operation == 4:
            a = interpret_nth_param(program, pos, 1)
            x_outputs.append(a)
            pos += 2
            if stop_on_output:
                return program, pos

        if operation == 5:
            a = interpret_nth_param(program, pos, 1)
            if a != 0:
                pos = interpret_nth_param(program, pos, 2)
            else:
                pos += 3

        if operation == 6:
            a = interpret_nth_param(program, pos, 1)
            if a == 0:
                pos = interpret_nth_param(program, pos, 2)
            else:
                pos += 3

        if operation == 7:
            a = interpret_nth_param(program, pos, 1)
            b = interpret_nth_param(program, pos, 2)
            program[program[pos + 3]] = int(a < b)
            pos += 4

        if operation == 8:
            a = interpret_nth_param(program, pos, 1)
            b = interpret_nth_param(program, pos, 2)
            program[program[pos + 3]] = int(a == b)
            pos += 4

        if operation > 9:
            raise ValueError

    return program, pos


def interpret_nth_param(program: list, position: int, param_number: int):
    mode = mode_for_nth_parameter(program[position], param_number)

    if mode == 0:
        return program[program[position + param_number]]

    if mode == 1:
        return program[position + param_number]

    raise ValueError


def mode_for_nth_parameter(code, n):
    code = code // 100
    divisor = 1
    for i in range(n - 1):
        divisor *= 10
    return code // divisor % 10


def part1(data: str):
    program = [int(x) for x in data.split(",")]
    max = -1

    perms = permutations([0, 1, 2, 3, 4])

    for perm in perms:
        input = 0
        for i in range(5):
            outputs = []
            run_program(program, (perm[i], input), outputs)
            input = outputs[-1]

        if input > max:
            max = input
    return max


def part2(data: str):
    program = [int(x) for x in data.split(",")]
    max = -1

    perms = permutations([5, 6, 7, 8, 9])
    for perm in perms:

        input_val = 0
        program_and_position_list = [(program, 0) for _ in range(5)]
        phase_needed = [True for _ in range(5)]

        stop_flag = False
        while not stop_flag:
            for i in range(5):
                outputs = []
                given_input = (perm[i], input_val) if phase_needed[i] else (input_val,)
                program_and_position_list[i] = run_program(program_and_position_list[i][0], given_input, outputs, True,
                                                           program_and_position_list[i][1])
                phase_needed[i] = False
                if len(outputs) > 0:
                    input_val = outputs[-1]
                else:
                    stop_flag = True
                    break

        if input_val > max:
            max = input_val

    return max


def read_data():
    with open(input_filename) as input_file:
        return input_file.read()


if __name__ == "__main__":
    this_filename = os.path.basename(__file__)
    input_filename = os.path.join("input", this_filename.replace("day", "").replace(".py", ".txt"))
    data = read_data()

    print(part1(data))
    print(part2(data))
