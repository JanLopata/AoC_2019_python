import os

import numpy as np

from aoc_tools import get_data

debug_part1 = True
debug_part2 = False

directions_map = {8: "LEFT", 4: "UP", 2: "RIGHT", 1: "DOWN"}
char_map = {'|': 5, '-': 10, 'L': 6, 'J': 12, '7': 9, 'F': 3, 'S': 15}
direction_masks = {(-1, 0): (4, 1),
                   (1, 0): (1, 4),
                   (0, -1): (8, 2),
                   (0, 1): (2, 8)
                   }


def remap_char(x):
    if x in char_map:
        return char_map[x]
    else:
        return 0


def is_adjacent_connected(origin, delta, grid):
    x = grid[origin[0]][origin[1]]
    y = grid[origin[0] + delta[0]][origin[1] + delta[1]]
    masks = direction_masks[delta]
    one_way = x & masks[0] > 0
    second_way = y & masks[1] > 0
    return one_way and second_way


def print_grid(grid):
    for row in grid:
        rowstr = ""
        for x in row:
            if x == 0:
                x = "."
            rowstr += str(x).rjust(3, ' ')

        print(rowstr)


def do_breath_first(queue, visited, grid):
    current = queue.pop(0)
    for delta in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        if is_adjacent_connected(current, delta, grid):
            new_coords = (current[0] + delta[0], current[1] + delta[1])
            if new_coords not in visited:
                queue.append(new_coords)
                visited[new_coords] = visited[current] + 1


def part1(data):

    grid = []
    for line in data.splitlines():
        grid_line = [remap_char(x) for x in line]
        grid_line.insert(0, 0)
        grid_line.append(0)
        grid.append(grid_line)

    grid.insert(0, len(grid[0]) * [0])
    grid.append(len(grid[0]) * [0])

    print_grid(grid)

    start_coords = None
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            if grid[row][col] == 15:
                start_coords = (row, col)
                break
    queue = [start_coords]
    visited = {start_coords: 0}

    while len(queue) > 0:
        do_breath_first(queue, visited, grid)

    return max(visited.values())



def compute_diff(a):
    shifted = np.zeros_like(a)
    shifted[1:] = a[:-1]
    diff = a - shifted
    return diff[1:]


def part2(data):
    pass


def do_tests():
    testdata1 = """-L|F7
7S-7|
L|7||
-L-J|
L|-JF
"""
    testdata2 = """7-F7-
.FJ|7
SJLL7
|F--J
LJ.LJ
"""
    testdata3 = """...........
.S-------7.
.|F-----7|.
.||.....||.
.||.....||.
.|L-7.F-J|.
.|..|.|..|.
.L--J.L--J.
..........."""
    testdata4 = """..........
.S------7.
.|F----7|.
.||....||.
.||....||.
.|L-7F-J|.
.|..||..|.
.L--JL--J.
..........
"""

    print(part1(testdata1))
    print(part1(testdata2))
    print(part2(testdata1))


if __name__ == "__main__":
    input_data = get_data(os.path.basename(__file__))

    do_tests()

    print(part1(input_data))
    print(part2(input_data))
