import os

from intcode_computer import IntcodeComputer

debug_mode = False


def interpret_screen(output):
    screen_map = {}
    for i in range(int(len(output) / 3)):
        x = output[3 * i]
        y = output[3 * i + 1]
        tile_id = output[3 * i + 2]
        screen_map[(x, y)] = tile_id
        if tile_id == 0:
            screen_map.pop((x, y))

    return screen_map


def print_screen(screen_map: dict):
    output = ""
    for i in range(24):
        for j in range(50):
            if (j, i) in screen_map:
                output += str(screen_map[(j, i)])
            else:
                output += ' '

        output += '\n'
    score = screen_map.get((-1, 0))

    print(output)
    print('Score: {}'.format(score))


def part1(data: str):
    program = [int(x) for x in data.split(",")]
    computer = IntcodeComputer()
    computer.import_program(program)
    print(computer.compute_while_possible())

    screen_map = interpret_screen(computer.output)
    print_screen(screen_map)
    return count_blocks(screen_map)


def count_blocks(screen_map):
    return len([x for x in screen_map.items() if x[1] == 2])


def part2(data: str):
    program = [int(x) for x in data.split(",")]
    program[0] = 2
    computer = IntcodeComputer()
    computer.import_program(program)
    pass


def read_data():
    with open(input_filename) as input_file:
        return input_file.read()


if __name__ == "__main__":
    this_filename = os.path.basename(__file__)
    input_filename = os.path.join("input", this_filename.replace("day", "").replace(".py", ".txt"))
    data = read_data()

    print(part1(data))
    print(part2(data))
