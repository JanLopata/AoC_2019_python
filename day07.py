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


def find_divider_under(top: tuple[int, int], dividers: dict):
    i, depth = top
    if i in dividers:
        for d in dividers[i]:
            if d > depth:
                return i, d
    return None


def part2(data: str):
    start, dividers = parse_dividers(data)

    stack = [find_divider_under((start, 0), dividers)]
    memory = dict()

    while len(stack) > 0:
        top = stack[-1]
        if top in memory:
            stack.pop()
            continue

        known = []
        for delta in [-1, 1]:
            k = (top[0] + delta, top[1])
            divider_under = find_divider_under(k, dividers)

            if divider_under is None:
                known.append(1)
                memory[k] = 1
            else:
                if divider_under in memory:
                    known.append(memory[divider_under])
                else:
                    stack.append(divider_under)

        if len(known) == 2:
            memory[top] = sum(known)

    return memory[find_divider_under((start, 0), dividers)]


def parse_dividers(data):
    start = -1
    line_number = 0
    dividers = dict()
    for line in data.splitlines():

        for i in range(len(line)):
            ch = line[i]
            if ch == "S":
                start = i
            if ch != '^':
                continue

            if i in dividers:
                dividers[i].append(line_number)
            else:
                dividers[i] = [line_number]
        line_number += 1
    return start, dividers


if __name__ == "__main__":
    input_data = get_data(os.path.basename(__file__))

    print(part1(input_data))
    print(part2(input_data))
