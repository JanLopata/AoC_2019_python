import os
import queue

from aoc_tools import get_data

debug_part1 = True
debug_part2 = True

d1 = (0, 1)
d2 = (0, -1)
d3 = (-1, 0)
d4 = (1, 0)


def compute_next(pos, delta):
    return pos[0] + delta[0], pos[1] + delta[1]


def process_dash(pos, delta):
    if delta == (1, 0) or delta == (-1, 0):
        res = []
        d1 = (0, -1)
        res.append((compute_next(pos, d1), d1))
        d2 = (0, 1)
        res.append((compute_next(pos, d2), d2))
        return res
    else:
        return continuation(delta, pos)


def process_pipe(pos, delta):
    if delta == (0, 1) or delta == (0, -1):
        res = []
        d1 = (-1, 0)
        res.append((compute_next(pos, d1), d1))
        d2 = (1, 0)
        res.append((compute_next(pos, d2), d2))
        return res
    else:
        return continuation(delta, pos)


def continuation(delta, pos):
    return [(compute_next(pos, delta), delta)]


def process_lr(pos, delta):
    if delta == d1:
        return continuation(d3, pos)
    if delta == d2:
        return continuation(d4, pos)
    if delta == d4:
        return continuation(d2, pos)
    if delta == d3:
        return continuation(d1, pos)


def process_rl(pos, delta):
    if delta == d1:
        return continuation(d4, pos)
    if delta == d2:
        return continuation(d3, pos)
    if delta == d3:
        return continuation(d2, pos)
    if delta == d4:
        return continuation(d1, pos)


def compute_rays(pos, delta, grid, used_elements):
    if pos[0] < 0 or pos[0] >= len(grid):
        return []
    if pos[1] < 0 or pos[1] >= len(grid[0]):
        return []

    element = grid[pos[0]][pos[1]]
    if element == '.':
        return continuation(delta, pos)

    if (pos, delta) in used_elements:
        return []

    used_elements.add((pos, delta))
    if element == '-':
        return process_dash(pos, delta)

    if element == '|':
        return process_pipe(pos, delta)

    if element == '/':
        return process_lr(pos, delta)

    if element == '\\':
        return process_rl(pos, delta)

    return []


def part1(data: str):
    grid = []
    for row in data.splitlines():
        gr = []
        for char in row:
            r = char
            gr.append(r)
        grid.append(gr)

    if debug_part1:
        for row in grid:
            s = "".join(row)
            print(s)

    start = (0, 0)
    delta = (0, 1)

    return process_rays_and_compute_activation(delta, grid, start)


def process_rays_and_compute_activation(delta, grid, start):
    activation = set()
    go_queue = queue.Queue()
    go_queue.put((start, delta))
    used_elements = set()
    while not go_queue.empty():

        pos, delta = go_queue.get()
        activation.add(pos)

        rays = compute_rays(pos, delta, grid, used_elements)

        for ray in rays:
            go_queue.put(ray)
    return compute_activation(activation, grid)


def compute_activation(activation, grid):
    if debug_part1:
        print()
    res = 0
    for i in range(len(grid)):
        s = ""
        for j in range(len(grid[i])):
            if (i, j) in activation:
                s += '#'
                res += 1
            else:
                s += '.'
        if debug_part1:
            print(s)

    return res


def part2(data: str):
    pass


def do_tests():
    testdata1 = """.|...\\....
|.-.\\.....
.....|-...
........|.
..........
.........\\
..../.\\\\..
.-.-/..|..
.|....-|.\\
..//.|....
"""

    print(part1(testdata1))
    print(part2(testdata1))


if __name__ == "__main__":
    input_data = get_data(os.path.basename(__file__))

    do_tests()

    print(part1(input_data))
    # print(part2(input_data))
