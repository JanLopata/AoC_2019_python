import math
import os

import numpy as np

from aoc_tools import get_data

debug_part1 = False
debug_part2 = True

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


def do_breath_first_on_pipes(queue, visited, grid):
    current = queue.pop(0)
    for delta in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        if is_adjacent_connected(current, delta, grid):
            new_coords = (current[0] + delta[0], current[1] + delta[1])
            if new_coords not in visited:
                queue.append(new_coords)
                visited[new_coords] = visited[current] + 1


def find_loop(data: str):
    grid = []
    for line in data.splitlines():
        grid_line = [remap_char(x) for x in line]
        grid_line.insert(0, 0)
        grid_line.append(0)
        grid.append(grid_line)

    grid.insert(0, len(grid[0]) * [0])
    grid.append(len(grid[0]) * [0])

    if debug_part1:
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
        do_breath_first_on_pipes(queue, visited, grid)

    return visited, grid


def compute_diff(a):
    shifted = np.zeros_like(a)
    shifted[1:] = a[:-1]
    diff = a - shifted
    return diff[1:]


def part1(data):
    visited, _ = find_loop(data)
    return max(visited.values())


def join_areas(areas, row, col):
    current = len(areas) - 1

    for delta in [(1, 0), (-1, 0), (0, 1), (0, -1)]:

        target = row + delta[0], col + delta[1]
        for i in range(len(areas) - 1):
            if i == current:
                continue
            area_set = areas[i]
            if target in area_set:
                # must merge the areas
                merged_with = areas.pop(current)
                area_set.update(merged_with)
                current = i
                break


def find_areas(grid, grid_size):
    areas = []
    idx = 0

    for row in range(grid_size):
        for col in range(grid_size):

            if grid[row][col] > 0:
                continue
            coords = (row, col)
            new_set = set()
            new_set.add(coords)
            areas.append(new_set)
            join_areas(areas, row, col)

    for i in range(len(areas)):

        for coords in areas[i]:
            grid[coords[0]][coords[1]] = i + 11

    return areas


def compute_depth(area, grid, zero_idx):
    depth = math.inf
    for delta in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        for coords in area:
            d = 0
            i = coords[0] + delta[0]
            j = coords[1] + delta[1]
            while grid[i][j] != zero_idx:
                d += 1
                i += delta[0]
                j += delta[1]
            if d < depth:
                depth = d

    return depth


def part2(data):
    visited, origi_grid = find_loop(data)

    grid_size = max(len(origi_grid), len(origi_grid[0]))
    grid = []
    for i in range(grid_size):
        grid.append(grid_size * [0])

    for coord in visited:
        grid[coord[0]][coord[1]] = 9

    print()
    print_grid(grid)

    current_color = 0
    for row in range(grid_size):

        change_on_line = set()
        for col in range(1, grid_size - 1):
            curr = grid[row][col]
            nxt = grid[row][col + 1]
            prev = grid[row][col -1]
            if curr == 9 and (curr != nxt or curr != prev):
                change_on_line.add(col)

        for c in change_on_line:
            grid[row][c] = 'C'

        print(row, change_on_line)

        for col in range(grid_size - 1):
            curr = grid[row][col]
            if col in change_on_line:
                current_color = 1 - current_color
            if curr == 0:
                grid[row][col] = current_color

    print_grid(grid)
    result = 0
    for row in grid:
        for c in row:
            if c == 1:
                result += 1

    return result


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
    testdata5 = """.F----7F7F7F7F-7....
.|F--7||||||||FJ....
.||.FJ||||||||L7....
FJL7L7LJLJ||LJ.L-7..
L--J.L7...LJS7F-7L7.
....F-J..F7FJ|L7L7L7
....L7.F7||L7|.L7L7|
.....|FJLJ|FJ|F7|.LJ
....FJL-7.||.||||...
....L---J.LJ.LJLJ...
"""

    # print(part1(testdata1))
    # print(part1(testdata2))
    print(part2(testdata1))
    print(part2(testdata4))
    print(part2(testdata5))


if __name__ == "__main__":
    input_data = get_data(os.path.basename(__file__))

    do_tests()

    # print(part1(input_data))
    # print(part2(input_data))
