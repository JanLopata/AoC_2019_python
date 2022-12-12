import os

from aoc_tools import get_data

DIRS = [(0, 1), (0, -1), (1, 0), (-1, 0)]


def parse_grid(data):
    grid = []
    for line in data.split("\n"):
        if line == "":
            continue
        grid.append([ord(c) - ord('a') for c in line])

    start = (0, 0)
    end = (0, 0)

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == -14:
                start = (i, j)
                grid[i][j] = 0

            if grid[i][j] == -28:
                end = (i, j)
                grid[i][j] = ord('z') - ord('a')

    grid_map = {}
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            grid_map[(i, j)] = grid[i][j]

    return grid_map, start, end


def part1(data: str):
    grid, start, end = parse_grid(data)

    candidates = [(start, 0)]
    visited = {}

    while len(candidates) > 0:

        current, path_length = candidates.pop(0)

        if current in visited:
            continue
        else:
            visited[current] = path_length

        if current == end:
            return path_length

        for direction in DIRS:
            target = (current[0] + direction[0], current[1] + direction[1])
            if target in visited:
                continue
            if target not in grid:
                continue
            elevation_target = grid[(target[0], target[1])]
            elevation_current = grid[(current[0], current[1])]
            if elevation_target > elevation_current + 1:
                continue
            candidates.append((target, path_length + 1))


def part2(data: str):
    grid, start, end = parse_grid(data)

    candidates = [(end, 0)]
    visited = {}

    while len(candidates) > 0:

        current, path_length = candidates.pop(0)

        if current in visited:
            continue
        else:
            visited[current] = path_length

        if grid[current] == 0:
            return path_length

        for direction in DIRS:
            target = (current[0] + direction[0], current[1] + direction[1])
            if target in visited:
                continue
            if target not in grid:
                continue
            elevation_target = grid[(target[0], target[1])]
            elevation_current = grid[(current[0], current[1])]
            if elevation_target + 1 < elevation_current:
                continue
            candidates.append((target, path_length + 1))


if __name__ == "__main__":
    data = get_data(os.path.basename(__file__))

    print(part1(data))
    print(part2(data))
