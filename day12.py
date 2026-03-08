import os

from aoc_tools import get_data

debug_mode = False


def parse_piece(part: str) -> tuple[int, set]:
    line_idx = -1
    num = None
    result_set = set()
    for line in part.splitlines():
        if len(line) == 0:
            continue
        if ":" in line:
            num = int(line[:-1])
        else:
            for i in range(len(line)):
                if line[i] == "#":
                    result_set.add((line_idx, i))
        line_idx += 1

    return num, result_set


def parse_requirements(part: str):
    requirements = []
    for line in part.splitlines():
        sp = line.split(": ")
        dimensions = parse_dimensions(sp[0])
        parts = parse_parts(sp[1])
        requirements.append((dimensions, parts))
    return requirements


def parse_dimensions(line: str):
    sp = line.split("x")
    return int(sp[0]), int(sp[1])


def parse_parts(line: str):
    sp = line.split()
    result = []
    for idx in range(len(sp)):
        count = int(sp[idx])
        if count > 0:
            result.append((idx, count))
    return result


def parse_data(data):
    pieces = []
    for part in data.split("\n\n"):
        if "x" in part:
            requirements = parse_requirements(part)
        else:
            n, p_set = parse_piece(part)
            pieces.append((n, p_set))

    print(pieces)
    print(requirements)


def part1(data: str):
    parse_data(data)
    pass


def part2(data: str):
    pass


if __name__ == "__main__":
    input_data = get_data(os.path.basename(__file__))

    print(part1(input_data))
    print(part2(input_data))
