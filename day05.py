import os

from aoc_tools import get_data


def parse_range(line: str):
    rs = line.split("-")
    return int(rs[0]), int(rs[1])


def parse_input(data):
    ranges_processed = False
    ranges = []
    ids = []
    for line in data.splitlines():
        if line == "":
            ranges_processed = True
            continue

        if ranges_processed:
            ids.append(int(line))
        else:
            ranges.append(parse_range(line))

    return ranges, ids


def part1(data: str):
    ranges, ids = parse_input(data)

    result = 0
    for num in ids:
        if is_number_in_any_range(num, ranges):
            result += 1
    return result


def is_number_in_any_range(num, ranges):
    for r in ranges:
        if is_number_in_range(num, r):
            return True
    return False


def is_number_in_range(num, r: tuple[int, int]):
    return r[0] <= num <= r[1]


def compute_range_overlaps(ranges):

    pointers = []
    for r in ranges:
        pointers.append((r[0], r[1], "S"))
        pointers.append((r[1], r[0], "E"))

    pointers.sort(key=lambda pointer: pointer[1], reverse=True) # it is important to have the longer intervals first
    pointers.sort(key=lambda pointer: pointer[0])

    depth = 0
    start = 0
    end = 0
    overlap_ranges = []
    for p in pointers:
        if p[2] == "S":
            if depth == 0:
                start = p[0]
            depth += 1
        else:
            depth -= 1
            if depth == 0:
                end = p[0]
                overlap_ranges.append((start, end))

    return overlap_ranges




def part2(data: str):
    ranges = []
    for line in data.splitlines():
        if line == "":
            break
        ranges.append(parse_range(line))

    overlaps = compute_range_overlaps(ranges)
    result = 0
    for r in overlaps:
        result += r[1] - r[0] + 1

    return result


if __name__ == "__main__":
    input_data = get_data(os.path.basename(__file__))

    print(part1(input_data))
    print(part2(input_data))
