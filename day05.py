import os

from aoc_tools import get_data


def read_instructions(param):
    result = []
    lines = param.split("\n")
    for line in lines:
        if line == "":
            continue

        sp = line.split(" ")

        result.append((int(sp[1]), int(sp[3]), int(sp[5])))

    return result


def read_start(param):
    lines = param.split("\n")
    maxlen = max(len(x) for x in lines)
    start = {}
    for i in range(int(maxlen / 4 + 2)):
        start[i] = []

    for line in lines:
        for i, ch in enumerate(line):
            if ch.isalpha():
                start[int(i / 4) + 1].append(ch)

        if line == "":
            continue

    return start


def process(situation, instructions):
    for instruction in instructions:

        for i in range(instruction[0]):
            crate = situation[instruction[1]].pop(0)
            where = instruction[2]
            situation[where].insert(0, crate)


def process2(situation, instructions):
    for instruction in instructions:

        stack = []
        where = instruction[2]
        for i in range(instruction[0]):
            crate = situation[instruction[1]].pop(0)
            stack.append(crate)

        stack.reverse()
        for crate in stack:
            situation[where].insert(0, crate)


def collect_result(situation):
    result = ""
    for key in situation:
        row = situation[key]
        if len(row) > 0:
            result += row[0]
    return result


def part1(data: str):
    data_parts = data.split("\n\n")
    start = read_start(data_parts[0])
    instructions = read_instructions(data_parts[1])
    process(start, instructions)

    return collect_result(start)


def part2(data: str):
    data_parts = data.split("\n\n")
    start = read_start(data_parts[0])
    instructions = read_instructions(data_parts[1])
    process2(start, instructions)
    return collect_result(start)


if __name__ == "__main__":
    data = get_data(os.path.basename(__file__))

    print(part1(data))
    print(part2(data))
