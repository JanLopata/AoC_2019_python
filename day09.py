import math
import os

from aoc_tools import get_data

directions = {
    'U': (0, -1),
    'D': (0, 1),
    'L': (-1, 0),
    'R': (1, 0),
}

PRINT_SIZE = 14
debug_print = False


def simulate(head, tail, delta_x, delta_y):
    head = (head[0] + int(delta_x), head[1] + int(delta_y))

    # distance between head and tail
    dist_x = head[0] - tail[0]
    dist_y = head[1] - tail[1]
    dist2 = dist_x ** 2 + dist_y ** 2
    if dist2 >= 4:
        # move tail
        if dist_x * dist_y == 0:
            # head is on the same line as tail
            if dist_x == 0:
                # head is on the same vertical line as tail
                tail = (tail[0], tail[1] + int(math.copysign(1, dist_y)))
            else:
                # head is on the same horizontal line as tail
                tail = (tail[0] + int(math.copysign(1, dist_x)), tail[1])

        else:
            # head is on the diagonal line
            tail = (tail[0] + math.copysign(1, dist_x), tail[1] + math.copysign(1, dist_y))

    return head, tail


def compute_delta(point1, point2):
    return int(point1[0] - point2[0]), int(point1[1] - point2[1])


def part1(data: str):
    lines = data.split("\n")

    head = (0, 0)
    tail = (0, 0)
    visits = set()
    visits.add(tail)

    for line in lines:
        if line == "":
            continue
        sp = line.split(" ")
        direction = sp[0]
        count = int(sp[1])

        for _ in range(count):
            delta = directions[direction]
            head, tail = simulate(head, tail, delta[0], delta[1])
            visits.add(tail)

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

    knots = [(0, 0)] * 10
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
                head, tail = simulate(head, tail, delta[0], delta[1])
                delta = compute_delta(tail, knots[i + 1])
                knots[i] = head
                # do not move the tail, it will be moved by the next call of simulate
                if delta == (0, 0):
                    break

            # move the tail last time
            knots[-1] = (knots[-1][0] + delta[0], knots[-1][1] + delta[1])
            visits.add(knots[-1])

        if debug_print:
            print_situation(knots, PRINT_SIZE)

    return len(visits)


if __name__ == "__main__":
    data = get_data(os.path.basename(__file__))

    print(part1(data))
    print(part2(data))
