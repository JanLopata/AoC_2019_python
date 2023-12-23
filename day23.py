import os
import queue

from aoc_tools import get_data

debug_part1 = True
debug_part2 = False

SLOPE_MAP = {">": (0, 1), "<": (0, -1), "^": (-1, 0), "v": (1, 0)}


def read_grid(data):
    result = []
    for line in data.splitlines():
        result.append([x for x in line])

    return result


def read_maze(data):
    result = {}
    i = 0
    for line in data.splitlines():
        for j in range(len(line)):
            result[(i, j)] = line[j]
        i += 1

    return result


def add_one_direction(visited: set, pos, delta, go_queue: queue):
    next_pos = (pos[0] + delta[0], pos[1] + delta[1])
    visited.add(next_pos)
    go_queue.put((visited, pos, delta, next_pos))


def add_various_directions(visited: set, pos, next_steps, go_queue):
    for delta in next_steps:
        visited_copy = set()
        visited_copy.update(visited)
        next_pos = (pos[0] + delta[0], pos[1] + delta[1])
        visited_copy.add(next_pos)
        go_queue.put((visited, pos, delta, next_pos))


def find_next_steps(visited: set, maze_map: dict, pos_i, pos_j):
    slopes = []
    general = []
    for delta in SLOPE_MAP.values():

        next_pos_i = pos_i + delta[0]
        next_pos_j = pos_j + delta[1]

        next_pos = (next_pos_i, next_pos_j)

        if next_pos not in maze_map:
            continue

        if next_pos in visited:
            continue

        ch = maze_map[next_pos]
        if ch == '#':
            continue

        if ch in SLOPE_MAP and SLOPE_MAP[ch] == delta:
            slopes.append(delta)

        general.append(delta)

    if len(slopes) == 0:
        return general
    else:
        return slopes


def print_maze(maze_map, max_i, max_j, visited):
    for i in range(max_i + 1):
        line = ""
        for j in range(max_j + 1):
            if (i, j) in visited:
                ch = 'O'
                if maze_map[(i, j)] != '.':
                    print("ERROR - unreachable {} visited!".format((i, j)))
                    ch = 'X'
            else:
                ch = maze_map[(i, j)] if (i, j) in maze_map else 'x'
            line += ch
        print(line)


def part1(data):
    maze_map = read_maze(data)

    max_i = max([x[0] for x in maze_map.keys()])
    max_j = max([x[1] for x in maze_map.keys()])

    print_maze(maze_map, max_i, max_j, set())

    start_point = (0, 1)
    end_point = (max_i, max_j - 1)

    go_queue = queue.Queue()
    go_queue.put((set(start_point), start_point, (1, 0), (1, 1)))

    fun = 0
    while not go_queue.empty():
        element = go_queue.get()
        visited = element[0]
        pos = element[3]
        pos_i = pos[0]
        pos_j = pos[1]
        if pos not in maze_map:
            continue

        if pos == end_point:
            if debug_part1:
                fun_here = len(visited)
                print("end reached in {} steps".format(fun_here))
                fun = max(fun, fun_here)
                print_maze(maze_map, max_i, max_j, visited)

        next_steps = find_next_steps(visited, maze_map, pos_i, pos_j)

        if len(next_steps) == 1:
            add_one_direction(visited, pos, next_steps[0], go_queue)
        else:
            add_various_directions(visited, pos, next_steps, go_queue)

    return fun


def part2(data):
    pass


def do_tests():
    testdata1 = """#.#####################
#.......#########...###
#######.#########.#.###
###.....#.>.>.###.#.###
###v#####.#v#.###.#.###
###.>...#.#.#.....#...#
###v###.#.#.#########.#
###...#.#.#.......#...#
#####.#.#.#######.#.###
#.....#.#.#.......#...#
#.#####.#.#.#########v#
#.#...#...#...###...>.#
#.#.#v#######v###.###v#
#...#.>.#...>.>.#.###.#
#####v#.#.###v#.#.###.#
#.....#...#...#.#.#...#
#.#########.###.#.#.###
#...###...#...#...#.###
###.###.#.###v#####v###
#...#...#.#.>.>.#.>.###
#.###.###.#.###.#.#v###
#.....###...###...#...#
#####################.#
"""

    print(part1(testdata1))
    print(part2(testdata1))


if __name__ == "__main__":
    input_data = get_data(os.path.basename(__file__))

    do_tests()

    # print(part1(input_data))
    print(part2(input_data))
