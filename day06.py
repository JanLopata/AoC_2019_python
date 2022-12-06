import os

from aoc_tools import get_data


def find_marker(data, window_size):
    for i in range(len(data) - window_size):

        specs = set(data[i:i + window_size])
        if len(specs) == window_size:
            return i + window_size

    return len(data)


def part1(data: str):
    return find_marker(data, 4)


def part2(data: str):
    return find_marker(data, 14)


if __name__ == "__main__":
    data = get_data(os.path.basename(__file__))

    print(part1(data))
    print(part2(data))
