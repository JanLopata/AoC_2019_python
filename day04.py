import os

from aoc_tools import get_data


def parse_interval(second_half):
    sp = second_half.split("-")
    return int(sp[0]), int(sp[1])


def parse_line(line):
    line_split = line.split(",")
    first_half = line_split[0]
    second_half = line_split[1]

    return parse_interval(first_half), parse_interval(second_half)


def is_inside(d):
    if d[0][1] - d[0][0] > d[1][1] - d[1][0]:
        longer = 0
        shorter = 1
    else:
        longer = 1
        shorter = 0

    if d[longer][0] <= d[shorter][0] and d[longer][1] >= d[shorter][1]:
        return True
    else:
        return False


def some_overlap(d):
    if d[0][0] < d[1][0]:
        first = 0
        second = 1
    else:
        first = 1
        second = 0

    return d[first][1] >= d[second][0]


def part1(data: str):
    lines = data.split("\n")

    parsed = parse_input(lines)
    return len([d for d in parsed if is_inside(d)])


def part2(data: str):
    lines = data.split("\n")

    parsed = parse_input(lines)
    return len([d for d in parsed if some_overlap(d)])


def parse_input(lines):
    parsed = []
    for line in lines:
        if line == "":
            continue

        parsed.append(parse_line(line))
    return parsed


if __name__ == "__main__":
    data = get_data(os.path.basename(__file__))

    print(part1(data))
    print(part2(data))
