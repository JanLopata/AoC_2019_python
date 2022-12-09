import os

import numpy as np
import numpy.linalg.linalg

from aoc_tools import get_data

directions = {
    'U': np.array([0, -1]),
    'D': np.array([0, 1]),
    'L': np.array([-1, 0]),
    'R': np.array([1, 0]),
}

PRINT_SIZE = 15
debug_print = False


def simulate(head, tail, delta):
    head = head + delta

    # distance between head and tail
    diff = tail - head
    if np.linalg.norm(diff) >= 2:
        # move tail towards head
        tail = tail - np.sign(diff)

    return head, tail


def part1(data: str):
    lines = data.split("\n")

    head = np.array([0, 0])
    tail = np.array([0, 0])
    visits = set()

    for line in lines:
        if line == "":
            continue
        sp = line.split(" ")
        direction = sp[0]
        count = int(sp[1])

        for _ in range(count):
            delta = directions[direction]
            head, tail = simulate(head, tail, delta)
            visits.add(tuple(tail))

    return len(visits)


def print_situation(knots, size):
    grid = [["."] * (2 * size + 1) for _ in range(-size, size + 1)]
    grid[size][size] = "s"
    for i in range(len(knots) - 1, -1, -1):
        x = knots[i][0] + size
        y = knots[i][1] + size
        char = str(i)
        if i == 0:
            char = "H"
        grid[y][x] = char

    # print grid
    for row in grid:
        print("".join(row))

    print()


def part2(data: str):
    lines = data.split("\n")

    knots = [np.array([0, 0])] * 10
    visits = set()
    if debug_print:
        print_situation(knots, PRINT_SIZE)

    for line in lines:
        if line == "":
            continue
        sp = line.split(" ")
        direction = sp[0]
        count = int(sp[1])

        for _ in range(count):

            delta = directions[direction]
            for i in range(len(knots) - 1):
                head = knots[i]
                tail = knots[i + 1]
                head, tail = simulate(head, tail, delta)
                delta = tail - knots[i + 1]
                knots[i] = head
                # do not move the tail, it will be moved by the next call of simulate
                if np.linalg.norm(delta) == 0:
                    break

            # move the tail last time
            knots[-1] = knots[-1] + delta
            visits.add(tuple(knots[-1]))

        if debug_print:
            print_situation(knots, PRINT_SIZE)

    return len(visits)


if __name__ == "__main__":
    data = get_data(os.path.basename(__file__))

    print(part1(data))
    print(part2(data))
