import math
import os
import queue

from aoc_tools import get_data

debug_part1 = True
debug_part2 = False

ALL_DIRECTIONS = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def out_of_bounds(grid_size, pos):
    if pos[0] < 0 or pos[0] >= grid_size:
        return True
    if pos[1] < 0 or pos[1] >= grid_size:
        return True


def find_possible_moves(grid_size, pos, vec, straight):
    moves = []

    for v in ALL_DIRECTIONS:
        if v[0] == -1 * vec[0] and v[1] == -1 * vec[1]:
            continue
        is_straight = v[0] == vec[0] and v[1] == vec[1]
        if straight >= 3 and is_straight:
            continue

        new_pos = pos[0] + v[0], pos[1] + v[1]

        if out_of_bounds(grid_size, new_pos):
            continue

        new_straight = straight + 1 if is_straight else 1
        moves.append((new_pos, v, new_straight))

    return moves


def part1(data):
    result = 0
    grid = []
    for line in data.splitlines():
        grid.append([int(x) for x in line])

    for row in grid:
        print(row)

    assert len(grid) == len(grid[0])
    grid_size = len(grid)

    visited_grid = init_visited_grid(grid)
    visited_grid[0][0] = (0, (0, 0), 0)

    go_queue = queue.Queue()
    element = ((0, 0), (0, 0), 0)
    go_queue.put(element)

    while not go_queue.empty():
        element = go_queue.get()
        print("Dequeued:", element)
        position = element[0]
        moves = find_possible_moves(grid_size=grid_size, pos=position, vec=element[1], straight=element[2])
        print(moves)

        for move in moves:
            new_position = move[0]
            current_price_on_position = visited_grid[new_position[0]][new_position[1]][0]
            proposed_price_on_position = visited_grid[position[0]][position[1]][0] + grid[new_position[0]][new_position[1]]

            if proposed_price_on_position < current_price_on_position:
                visited_grid[new_position[0]][new_position[1]] = (proposed_price_on_position, move[1], move[2])
                go_queue.put((new_position, move[1], move[2]))


    result = visited_grid[-1][-1][0]

    for vr in visited_grid:
        s = ""
        for vc in vr:
            s += str(vc[0]) + "\t"
        print(s)

    return result


def init_visited_grid(grid):
    visited_grid = []
    for row in grid:
        vr = []
        for col in grid:
            vr.append((math.inf, (0, 0), 0))
        visited_grid.append(vr)
    return visited_grid


def part2(data):
    result = 0
    return result


def do_tests():
    testdata1 = """2413432311323
3215453535623
3255245654254
3446585845452
4546657867536
1438598798454
4457876987766
3637877979653
4654967986887
4564679986453
1224686865563
2546548887735
4322674655533
"""

    print(part1(testdata1))
    print(part2(testdata1))


if __name__ == "__main__":
    input_data = get_data(os.path.basename(__file__))

    do_tests()

    # print(part1(input_data))
    # print(part2(input_data))