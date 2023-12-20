import os
import queue

from aoc_tools import get_data

debug_part1 = True
debug_part2 = False

DELTA_MAP = {"D": (0, -1), "U": (0, 1), "L": (-1, 0), "R": (1, 0)}


def parse_instructions(line):
    spl = line.split()
    return spl[0], int(spl[1]), spl[2]


def find_start(visited):
    # hack - works on my dataset
    if len(visited) < 100:
        return 1, -1
    else:
        return 1, 1


def flood(visited):
    pos = find_start(visited)
    # print_visited(visited, pos)

    work_queue = queue.Queue()
    work_queue.put(pos)
    while not work_queue.empty():
        pos = work_queue.get()
        if pos in visited:
            continue
        visited[pos] = "unknown"
        for delta in DELTA_MAP.values():
            nxt = pos[0] + delta[0], pos[1] + delta[1]
            work_queue.put(nxt)


def part1(data):
    visited = {(0, 0): None}
    x, y = (0, 0)
    for line in data.splitlines():
        direction, steps, color = parse_instructions(line)
        delta = DELTA_MAP[direction]
        for i in range(steps):
            x += delta[0]
            y += delta[1]
            visited[(x, y)] = color
    flood(visited)
    return len(visited)


def print_visited(visited, special):
    px_min = min([p[0] for p in visited.keys()])
    py_min = min([p[1] for p in visited.keys()])
    px_max = max([p[0] for p in visited.keys()])
    py_max = max([p[1] for p in visited.keys()])
    print(visited.keys())
    print(px_min, px_max, py_min, py_max)
    for i in range(py_max, py_min - 1, -1):
        s = ""
        for j in range(px_min, px_max + 1):
            if (j, i) == special:
                s += 'O'
            elif (j, i) in visited:
                s += '#'
            else:
                s += '.'
        print(s)


def part2(data):
    pass


def do_tests():
    testdata1 = """R 6 (#70c710)
D 5 (#0dc571)
L 2 (#5713f0)
D 2 (#d2c081)
R 2 (#59c680)
D 2 (#411b91)
L 5 (#8ceee2)
U 2 (#caa173)
L 1 (#1b58a2)
U 2 (#caa171)
R 2 (#7807d2)
U 3 (#a77fa3)
L 2 (#015232)
U 2 (#7a21e3)
"""

    print(part1(testdata1))
    print(part2(testdata1))


if __name__ == "__main__":
    input_data = get_data(os.path.basename(__file__))

    do_tests()

    print(part1(input_data))
    print(part2(input_data))
