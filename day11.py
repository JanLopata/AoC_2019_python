import os

from aoc_tools import get_data

debug_part1 = True
debug_part2 = False

GALAXY = '#'


def count_manhattan_expanded_distance(x, y, expanded: set, factor=2):
    tmp_factor = factor - 1
    if x > y:
        tmp = x
        x = y
        y = tmp

    expanded_dist = 0
    for i in expanded:
        if x < i < y:
            expanded_dist += tmp_factor

    result = expanded_dist + y - x
    return result


def part1(data):
    grid = []
    for line in data.splitlines():
        row = []
        for ch in line:
            row.append(ch)
        grid.append(row)

    glx = []
    for i in range(len(grid)):
        row = grid[i]
        for j in range(len(row)):
            if grid[i][j] == GALAXY:
                glx.append((i, j))

    colwg = set()
    rowwg = set()
    for i in range(len(grid)):
        row = grid[i]
        has_g = False
        for j in range(len(row)):
            if grid[i][j] == GALAXY:
                has_g = True
                break

        if not has_g:
            rowwg.add(i)

    for j in range(len(grid[0])):
        has_g = False
        for i in range(len(grid)):
            if grid[i][j] == GALAXY:
                has_g = True
                break

        if not has_g:
            colwg.add(j)

    print(rowwg)
    print(colwg)

    result = 0
    for i in range(len(glx)):
        for j in range(len(glx)):

            if i >= j:
                continue

            result += count_manhattan_expanded_distance(glx[i][0], glx[j][0], rowwg)
            result += count_manhattan_expanded_distance(glx[i][1], glx[j][1], colwg)

    # print_grid(grid)
    return result


def part2(data):
    grid = []
    for line in data.splitlines():
        row = []
        for ch in line:
            row.append(ch)
        grid.append(row)

    glx = []
    for i in range(len(grid)):
        row = grid[i]
        for j in range(len(row)):
            if grid[i][j] == GALAXY:
                glx.append((i, j))

    colwg = set()
    rowwg = set()
    for i in range(len(grid)):
        row = grid[i]
        has_g = False
        for j in range(len(row)):
            if grid[i][j] == GALAXY:
                has_g = True
                break

        if not has_g:
            rowwg.add(i)

    for j in range(len(grid[0])):
        has_g = False
        for i in range(len(grid)):
            if grid[i][j] == GALAXY:
                has_g = True
                break

        if not has_g:
            colwg.add(j)

    print(rowwg)
    print(colwg)

    result = 0
    for i in range(len(glx)):
        for j in range(len(glx)):

            if i >= j:
                continue

            result += count_manhattan_expanded_distance(glx[i][0], glx[j][0], rowwg, 1000000)
            result += count_manhattan_expanded_distance(glx[i][1], glx[j][1], colwg, 1000000)

    # print_grid(grid)
    return result

def print_grid(grid):
    for row in grid:
        rowstr = ""
        for x in row:
            rowstr += x

        print(rowstr)


def do_tests():
    testdata1 = """...#......
.......#..
#.........
..........
......#...
.#........
.........#
..........
.......#..
#...#.....
"""

    print(part1(testdata1))
    print(part2(testdata1))


if __name__ == "__main__":
    input_data = get_data(os.path.basename(__file__))

    do_tests()

    print(part1(input_data))
    print(part2(input_data))
