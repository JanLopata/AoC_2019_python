import os


def run_program(program: list):
    program = [x for x in program]
    pos = 0
    while program[pos] != 99:

        if program[pos] == 1:
            program[program[pos + 3]] = program[program[pos + 1]] + program[program[pos + 2]]
            pos += 4

        if program[pos] == 2:
            program[program[pos + 3]] = program[program[pos + 1]] * program[program[pos + 2]]
            pos += 4

    return program


def part1():
    program_str = read_file_lines(input_filename)[0]
    program_input = [int(x) for x in program_str.split(",")]
    program_input[1] = 12
    program_input[2] = 2
    print(run_program(program_input)[0])


def part2():
    program_str = read_file_lines(input_filename)[0]
    base_program_input = [int(x) for x in program_str.split(",")]

    for i in range(2000):
        for j in range(2000):
            program = [x for x in base_program_input]
            program[1] = i
            program[2] = j
            try:
                if run_program(program)[0] == 19690720:
                    print(100 * i + j)
                    return
            except IndexError:
                pass


def read_file_lines(filename):
    with open(input_filename) as input_file:
        return [x for x in input_file]


if __name__ == "__main__":
    this_filename = os.path.basename(__file__)
    input_filename = os.path.join("input", this_filename.replace("day", "").replace(".py", ".txt"))
    # print(input_filename)

    part1()
    part2()
