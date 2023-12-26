import math
import os
import queue

from aoc_tools import get_data

debug_part1 = False
debug_part2 = False

DIRS = [(0, 1), (1, 0), (-1, 0), (0, -1)]


def read_grid(data):
    grid = []
    start = -1, -1
    first_row = []
    grid.append(first_row)
    i = 0
    for line in data.splitlines():
        i += 1
        row = ['#']
        for j in range(len(line)):
            ch = line[j]
            if ch == 'S':
                start = i, j + 1
            row.append(ch)
        row.append('#')

        grid.append(row)

    grid.append(first_row)
    for i in range(len(grid[1]) + 2):
        first_row.append('#')

    return grid, start


def init_distance_grid(grid, start):
    distance_grid = []
    for row in grid:
        d_row = []
        distance_grid.append(d_row)
        for _ in row:
            d_row.append(math.inf)

    distance_grid[start[0]][start[1]] = 0
    return distance_grid


def init_checker_counter_grid(grid):
    result = []
    for row in grid:
        d_row = []
        result.append(d_row)
        for _ in row:
            d_row.append(0)
    return result


def count_reachable(max_steps, distance_grid):
    reachable = 0
    for row in distance_grid:
        for value in row:
            if value == max_steps or (value < max_steps and value % 2 == 0):
                reachable += 1
    return reachable


def part1(data):
    grid, start = read_grid(data)
    distance_grid = init_distance_grid(grid, start)
    target = 6 if len(grid) < 20 else 64

    go_queue = queue.Queue()
    go_queue.put(start)

    distance_max = 0

    while not go_queue.empty():

        position = go_queue.get()
        distance = distance_grid[position[0]][position[1]]
        if distance > distance_max:
            if debug_part1:
                print("Current reached distance: ", distance)
            distance_max = distance
            if distance_max > target + 1:
                break

        for delta in DIRS:

            x = position[0] + delta[0]
            y = position[1] + delta[1]

            if grid[x][y] == '#':
                continue

            if distance + 1 >= distance_grid[x][y]:
                continue

            distance_grid[x][y] = distance + 1
            go_queue.put((x, y))

    return count_reachable(target, distance_grid)


def part2(data):
    pass


def do_tests():
    testdata1 = """...........
.....###.#.
.###.##..#.
..#.#...#..
....#.#....
.##..S####.
.##..#...#.
.......##..
.##.#.####.
.##..##.##.
...........
"""
    print(part1(testdata1))
    print(part2(testdata1))


if __name__ == "__main__":
    input_data = get_data(os.path.basename(__file__))

    do_tests()

    print(part1(input_data))
    # print(part2(input_data))
