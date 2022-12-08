import os

from aoc_tools import get_data

directions = [
    (1, 0),
    (0, 1),
    (-1, 0),
    (0, -1)]


def read_grid(data):
    lines = data.split("\n")
    grid = []
    for line in lines:
        if line == "":
            continue
        grid.append([int(x) for x in line])
    return grid


def print_grid(grid):
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            print(grid[y][x], end="")
        print()


def extract_line(grid, x, y, delta_x, delta_y):
    line = []

    while 0 <= x < len(grid[0]) and 0 <= y < len(grid):
        line.append(grid[y][x])
        x += delta_x
        y += delta_y
    return line


def line_has_first_max(line):
    for i in range(1, len(line)):
        if line[0] <= line[i]:
            return False
    return True


def compute_score(line):
    for i in range(1, len(line)):
        if line[0] <= line[i]:
            return i
    return len(line) - 1


def part1(data: str):
    grid = read_grid(data)

    visible_count = 0
    for y in range(1, len(grid) - 1):
        for x in range(1, len(grid[y]) - 1):
            for delta_x, delta_y in directions:
                line = extract_line(grid, x, y, delta_x, delta_y)
                if line_has_first_max(line):
                    visible_count += 1
                    break

    return visible_count + 2 * len(grid) + 2 * len(grid[0]) - 4


def part2(data: str):
    grid = read_grid(data)
    scores = []
    for y in range(1, len(grid) - 1):
        for x in range(1, len(grid[y]) - 1):
            score = 1
            for delta_x, delta_y in directions:
                line = extract_line(grid, x, y, delta_x, delta_y)
                score *= compute_score(line)
            scores.append(score)

    return max(scores)


if __name__ == "__main__":
    data = get_data(os.path.basename(__file__))

    print(part1(data))
    print(part2(data))
