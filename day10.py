import os

from aoc_tools import get_data


def indicators_to_number(indicators_str: str):
    result = 0
    revers = indicators_str[::-1]
    for c in revers:
        result *= 2
        if c == "#":
            result += 1
    return result


def mask_indices_to_number(mask_indices: list[str]):
    result = 0
    for str_idx in mask_indices:
        idx = int(str_idx)
        result += 2 ** idx
    return result


def parse_line(line):
    sp = line.split()
    indicators = indicators_to_number(sp[0][1:-1])
    buttons = []
    for button_source in sp[1:-1]:
        mask_indices = button_source[1:-1].split(",")
        mask = mask_indices_to_number(mask_indices)
        buttons.append(mask)

    return indicators, buttons, None


def part1(data: str):
    for line in data.splitlines():
        indicators, wiring, _ = parse_line(line)
        print(indicators, wiring)

    return 0


def part2(data: str):
    pass


if __name__ == "__main__":
    input_data = get_data(os.path.basename(__file__))

    print(part1(input_data))
    print(part2(input_data))
