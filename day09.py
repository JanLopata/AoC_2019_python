import os

from intcode_computer import IntcodeComputer


def part1(data: str):
    program = [int(x) for x in data.split(",")]
    computer = IntcodeComputer()
    computer.import_program(program)
    computer.accept_input([1])
    print(computer.compute_while_possible())
    print(computer.program, computer.position)
    return computer.output


def part2(data: str):
    program = [int(x) for x in data.split(",")]
    computer = IntcodeComputer()
    computer.import_program(program)
    computer.accept_input([2])
    print(computer.compute_while_possible())
    print(computer.program, computer.position)
    return computer.output


def read_data():
    with open(input_filename) as input_file:
        return input_file.read()


if __name__ == "__main__":
    this_filename = os.path.basename(__file__)
    input_filename = os.path.join("input", this_filename.replace("day", "").replace(".py", ".txt"))
    data = read_data()

    print(part1(data))
    print(part2(data))
