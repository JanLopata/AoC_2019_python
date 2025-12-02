import os

from aoc_tools import get_data


def part1(data: str):
    dial = 50
    zeros = 0
    for line in data.splitlines():
        if len(line) == 0:
            continue
        num = int(line[1:])
        if line.startswith("L"):
            diff = - num
        else:
            diff = num

        dial += diff
        dial %= 100
        if dial == 0:
            zeros += 1

    return zeros


def part2(data: str):
    dial = 50
    zeros = 0
    for line in data.splitlines():
        if len(line) == 0:
            continue

        num = int(line[1:])
        if line.startswith("L"):
            diff = - num
        else:
            diff = num

        previous = dial
        dial += diff
        clicks = abs(dial) // 100
        if previous * dial < 0 or dial == 0:
            clicks += 1
        dial %= 100


        zeros += clicks

        print(line, dial, clicks)

    return zeros


if __name__ == "__main__":
    input_data = get_data(os.path.basename(__file__))

    print(part1(input_data))
    print(part2(input_data))
