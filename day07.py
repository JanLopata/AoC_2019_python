import os

from aoc_tools import get_data


def split_beam(i, beams: set[int], split_counter: list[int]):
    beams.remove(i)
    split_counter.append(i)
    beams.add(i - 1)
    beams.add(i + 1)


def part1(data: str):
    active_beams = set()
    removed_beams = []
    for line in data.splitlines():

        for i in range(len(line)):
            ch = line[i]
            if ch == "S":
                active_beams.add(i)

            if ch == "^" and i in active_beams:
                split_beam(i, active_beams, removed_beams)

    return len(removed_beams)


def part2(data: str):
    pass


if __name__ == "__main__":
    input_data = get_data(os.path.basename(__file__))

    print(part1(input_data))
    print(part2(input_data))
