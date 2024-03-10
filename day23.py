import os
import queue

from aoc_tools import get_data

debug_part1 = False
debug_part2 = False

SLOPE_MAP = {">": (0, 1), "<": (0, -1), "^": (-1, 0), "v": (1, 0)}
DIRS = SLOPE_MAP.values()


def plus_2d(pos, delta):
    return pos[0] + delta[0], pos[1] + delta[1]


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

    max_i = max([x[0] for x in result.keys()])
    max_j = max([x[1] for x in result.keys()])

    return result, (max_i, max_j)


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
        go_queue.put((visited_copy, pos, delta, next_pos))


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


def print_maze(maze_map, maze_dimensions, visited):
    max_i, max_j = (maze_dimensions[0], maze_dimensions[1])
    if not debug_part1:
        return
    for i in range(max_i + 1):
        line = ""
        for j in range(max_j + 1):
            if (i, j) in visited:
                ch = 'O'
                if maze_map[(i, j)] == '#':
                    print("ERROR - unreachable {} visited!".format((i, j)))
                    ch = 'X'
            else:
                ch = maze_map[(i, j)] if (i, j) in maze_map else 'x'
            line += ch
        print(line)


def part1(data):
    maze_map, maze_dimensions = read_maze(data)
    print_maze(maze_map, maze_dimensions, set())

    start_point = (0, 1)
    end_point = (maze_dimensions[0], maze_dimensions[1] - 1)

    go_queue = queue.Queue()
    go_queue.put((set(), start_point, (0, 0), start_point))

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
            fun_here = len(visited)
            fun = max(fun, fun_here)
            if debug_part1:
                print("end reached in {} steps".format(fun_here))
                # print_maze(maze_map, max_i, max_j, visited)

        next_steps = find_next_steps(visited, maze_map, pos_i, pos_j)

        if len(next_steps) == 1:
            add_one_direction(visited, pos, next_steps[0], go_queue)
        else:
            add_various_directions(visited, pos, next_steps, go_queue)

    return fun


def part2(data):
    updated_data = data.replace("^", ".").replace("v", ".").replace("<", ".").replace(">", ".")
    # print(updated_data)

    maze_map, maze_dimensions = read_maze(data)
    start = (0, 1)
    graph = convert_to_graph(maze_map, start)
    print(graph)
    for key in graph:
        maze_map[key] = '*'
    print_maze(maze_map, maze_dimensions, set())


def add_edge(graph, source, target, distance):
    if source not in graph:
        graph[source] = {}

    graph[source][target] = distance


def apply_symmetry(graph):
    edges_to_add = []
    for source in graph:
        edges_map = graph[source]
        for target in edges_map:
            edges_to_add.append((target, source, edges_map[target]))

    for source, target, distance in edges_to_add:
        add_edge(graph, source, target, distance)


def convert_to_graph(maze_map, start_point):
    graph = {start_point: {}}
    visited = set()
    visited.add(start_point)
    go_queue = queue.Queue()
    go_queue.put((start_point, start_point))

    while not go_queue.empty():
        element = go_queue.get()
        start = element[0]
        previous_for_graph = element[1]
        next_position, distance = crawl_to_next(visited, start, maze_map)
        if next_position is not None:
            # maze_map[next_position] = '*'
            add_edge(graph, previous_for_graph, next_position, distance)
            next_starts = find_unvisited_allowed(maze_map, visited, next_position)
            for next_start in next_starts:
                go_queue.put((next_start, next_position))

    apply_symmetry(graph)
    return graph


def find_unvisited_allowed(maze_map, visited, start):
    result = []
    for delta in DIRS:
        target = plus_2d(start, delta)

        if target in visited:
            continue

        if target not in maze_map:
            continue

        if maze_map[target] == '#':
            continue

        result.append(target)
    return result


def crawl_to_next(visited, start, maze_map):
    # should return next interesting point and distance to it
    visited.add(start)

    distance = 0
    next_step = None
    next_steps = find_unvisited_allowed(maze_map, visited, start)
    while len(next_steps) == 1:
        visited.add(start)
        distance += 1
        next_step = next_steps[0]
        visited.add(next_step)
        next_steps = find_unvisited_allowed(maze_map, visited, next_step)

    return next_step, distance


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

    print(part1(input_data))
    print(part2(input_data))
