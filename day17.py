import os
import queue

from aoc_tools import get_data

debug_part1 = False
debug_part2 = False

ALL_DIRECTIONS = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def out_of_bounds(grid_size, pos):
    if pos[0] < 0 or pos[0] >= grid_size:
        return True
    if pos[1] < 0 or pos[1] >= grid_size:
        return True


def reached_position_hash(pos, vector, current_straight):
    return hash((pos[0], pos[1], vector[0], vector[1], current_straight))


def find_possible_moves(grid_size, pos, vec, straight, visited_set:set):
    moves = []

    for v in ALL_DIRECTIONS:
        if v[0] == -1 * vec[0] and v[1] == -1 * vec[1]:
            continue
        is_straight = v[0] == vec[0] and v[1] == vec[1]
        if straight >= 3 and is_straight:
            continue

        new_pos = pos[0] + v[0], pos[1] + v[1]
        if new_pos in visited_set:
            continue

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

    if debug_part1:
        for row in grid:
            print(row)

    assert len(grid) == len(grid[0])
    grid_size = len(grid)

    visited_grid = init_visited_grid(grid)
    rewrites_grid = []
    for i in range(grid_size):
        rewrites_grid.append([])
        for j in range(grid_size):
            rewrites_grid[-1].append(0)

    go_queue = queue.Queue()
    element = ((0, 0), (0, 0), 0, 0, set())
    go_queue.put(element)

    while not go_queue.empty():
        element = go_queue.get()
        if debug_part1:
            print("Dequeued:", element[0])
        position = element[0]
        current_price = element[3]
        visited_set = element[4]
        moves = find_possible_moves(grid_size=grid_size, pos=position, vec=element[1], straight=element[2], visited_set=visited_set)
        # if debug_part1:
        #     print(moves)

        for move in moves:
            new_position = move[0]
            vector = move[1]
            current_straight = move[2]
            rph = reached_position_hash(new_position, vector, current_straight)
            visited_here_map = visited_grid[new_position[0]][new_position[1]]
            proposed_price_on_position = current_price + grid[new_position[0]][new_position[1]]
            if rph in visited_here_map:
                already_visited_price = visited_here_map[rph]
                if already_visited_price <= proposed_price_on_position:
                    continue

            visited_here_map[rph] = proposed_price_on_position
            rewrites_grid[new_position[0]][new_position[1]] += 1
            new_visited_set = set(visited_set)
            new_visited_set.add(new_position)
            go_queue.put((new_position, vector, current_straight, proposed_price_on_position, new_visited_set))


    if debug_part1:
        sum_rw = 0
        print("Rewrites: ")
        for rr in rewrites_grid:
            s = ""
            for rc in rr:
                s += str(rc) + "\t"
                sum_rw += rc
            print(s)
        print("Total:", sum_rw)

    if debug_part1:
        for vr in visited_grid:
            s = ""
            for vc in vr:
                minimal = min(vc.values())
                s += str(minimal) + "\t"
            print(s)


    return min(visited_grid[-1][-1].values())


def init_visited_grid(grid):
    visited_grid = []
    for row in grid:
        vr = []
        for col in grid:
            vr.append({})
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

    print(part1(input_data))
    # print(part2(input_data))
