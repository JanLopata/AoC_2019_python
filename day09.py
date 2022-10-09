import os


def run_program(input_program: list, x_inputs, x_outputs, stop_on_output=False, pos=0):
    program = {}
    for i in range(len(input_program)):
        program[i] = input_program[i]
    input_idx = 0
    relative_base = 0

    while program[pos] != 99:

        operation = program[pos] % 100

        if operation == 1:
            a = interpret_nth_param(program, pos, 1, relative_base)
            b = interpret_nth_param(program, pos, 2, relative_base)
            program[program.get(pos + 3)] = a + b
            pos += 4

        if operation == 2:
            a = interpret_nth_param(program, pos, 1, relative_base)
            b = interpret_nth_param(program, pos, 2, relative_base)
            program[program.get(pos + 3)] = a * b
            pos += 4

        if operation == 3:
            program[program.get(pos + 1)] = x_inputs[input_idx]
            input_idx += 1
            pos += 2

        if operation == 4:
            a = interpret_nth_param(program, pos, 1, relative_base)
            x_outputs.append(a)
            pos += 2
            if stop_on_output:
                return program, pos

        if operation == 5:
            a = interpret_nth_param(program, pos, 1, relative_base)
            if a != 0:
                pos = interpret_nth_param(program, pos, 2, relative_base)
            else:
                pos += 3

        if operation == 6:
            a = interpret_nth_param(program, pos, 1, relative_base)
            if a == 0:
                pos = interpret_nth_param(program, pos, 2, relative_base)
            else:
                pos += 3

        if operation == 7:
            a = interpret_nth_param(program, pos, 1, relative_base)
            b = interpret_nth_param(program, pos, 2, relative_base)
            program[program.get(pos + 3)] = int(a < b)
            pos += 4

        if operation == 8:
            a = interpret_nth_param(program, pos, 1, relative_base)
            b = interpret_nth_param(program, pos, 2, relative_base)
            program[program.get(pos + 3)] = int(a == b)
            pos += 4

        if operation == 9:
            a = interpret_nth_param(program, pos, 1, relative_base)
            relative_base += a
            pos += 2

        if operation > 9:
            raise ValueError

    return program, pos


def interpret_nth_param(program: dict, position: int, param_number: int, relative_base):
    mode = mode_for_nth_parameter(program.get(position, 0), param_number)

    if mode == 0:
        return program.get(program.get(position + param_number, 0), 0)

    if mode == 1:
        return program.get(position + param_number, 0)

    if mode == 2:
        return program.get(relative_base + program.get(position + param_number, 0), 0)

    raise ValueError


def mode_for_nth_parameter(code, n):
    code = code // 100
    divisor = 1
    for i in range(n - 1):
        divisor *= 10
    return code // divisor % 10


def part1(data: str):
    program = [int(x) for x in data.split(",")]
    outputs = []
    program_memory, halting_position = run_program(program, [1], outputs)
    print(program_memory, halting_position)
    return outputs


def part2(data: str):
    program = [int(x) for x in data.split(",")]


def read_data():
    with open(input_filename) as input_file:
        return input_file.read()


if __name__ == "__main__":
    this_filename = os.path.basename(__file__)
    input_filename = os.path.join("input", this_filename.replace("day", "").replace(".py", ".txt"))
    data = read_data()

    print(part1(data))
    print(part2(data))
