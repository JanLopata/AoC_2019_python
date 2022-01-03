import os
from functools import reduce


def part1(data: str):
    lines = data.split("\n")
    first_wire_dict = get_wire_path_dict(lines[0])
    second_wire_dict = get_wire_path_dict(lines[1])
    return reduce(lambda x, y: min(x, y),
                  map(lambda pos: abs(pos[0]) + abs(pos[1]),
                      set(first_wire_dict.keys()).intersection(set(second_wire_dict.keys()))
                      ))


def part2(data: str):
    lines = data.split("\n")
    first_wire_dict = get_wire_path_dict(lines[0])
    second_wire_dict = get_wire_path_dict(lines[1])
    return reduce(lambda x, y: min(x, y),
                  map(lambda pos: first_wire_dict[pos] + second_wire_dict[pos],
                      set(first_wire_dict.keys()).intersection(set(second_wire_dict.keys()))
                      ))


def get_wire_path_dict(csv):
    x = 0
    y = 0
    res = {}
    step = 0

    for instruction in csv.split(","):
        direction = instruction[0]
        value = int(instruction[1:])
        xdiff = 0
        ydiff = 0
        if direction == 'R':
            xdiff = 1
        if direction == 'L':
            xdiff = -1
        if direction == 'D':
            ydiff = 1
        if direction == 'U':
            ydiff = -1

        for i in range(value):
            x += xdiff
            y += ydiff
            step += 1
            res[(x, y)] = step

    return res


def read_data():
    with open(input_filename) as input_file:
        return input_file.read()


if __name__ == "__main__":
    this_filename = os.path.basename(__file__)
    input_filename = os.path.join("input", this_filename.replace("day", "").replace(".py", ".txt"))
    # print(input_filename)

    print(part1(read_data()))
    print(part2(read_data()))
