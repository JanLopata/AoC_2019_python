import os

from aoc_tools import get_data


def interpret_indicator(x):
    if x == "#":
        return 1
    else:
        return 0


def parse_line(line):

    sp = line.split()
    indicators = [interpret_indicator(x) for x in sp[0][1:-1]]
    buttons = []
    for button_source in sp[1:-1]:
        wiring = [int(x) for x in button_source[1:-1].split(",")]
        buttons.append(wiring)

    return indicators, buttons, None


def part1(data: str):
    for line in data.splitlines():
        indicators, wiring, _ = parse_line(line)



    return 0


def part2(data: str):
    pass


if __name__ == "__main__":
    input_data = get_data(os.path.basename(__file__))

    print(part1(input_data))
    print(part2(input_data))
