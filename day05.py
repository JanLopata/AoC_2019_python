import os


def run_program(program: list, x_input, x_outputs):
    program = [x for x in program]
    pos = 0

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
            program[program[pos + 1]] = x_input
            pos += 2

        if operation == 4:
            a = interpret_nth_param(program, pos, 1)
            x_outputs.append(a)
            pos += 2

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

    return program


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
    outputs = []
    run_program(program, 1, outputs)
    return outputs[-1]


def part2(data: str):
    program = [int(x) for x in data.split(",")]
    outputs = []
    run_program(program, 5, outputs)
    return outputs[-1]


def read_data():
    with open(input_filename) as input_file:
        return input_file.read()


if __name__ == "__main__":
    this_filename = os.path.basename(__file__)
    input_filename = os.path.join("input", this_filename.replace("day", "").replace(".py", ".txt"))
    data = read_data()
    # print(input_filename)

    print(part1(data))
    print(part2(data))
