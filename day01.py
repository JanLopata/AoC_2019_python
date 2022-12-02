import os

from aoc_tools import get_data


def part1(data: str):
    return max(count_calories(data))


def count_calories(data):
    elfs = data.split("\n\n")
    # sum calories for every elf
    calories = []
    for elf in elfs:
        cal = 0
        for line in elf.split("\n"):
            if line == "":
                continue
            cal += int(line)
        calories.append(cal)
    return calories


def part2(data: str):
    calories = count_calories(data)
    return sum(sorted(calories)[-3:])


if __name__ == "__main__":
    data = get_data(os.path.basename(__file__))

    print(part1(data))
    print(part2(data))
