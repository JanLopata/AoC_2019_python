import os

from aoc_tools import get_data

debug_part1 = False
debug_part2 = False

TARGET_ITERATIONS = 1000000000
# TARGET_ITERATIONS = 15


def roll_up(actors, size):
    min_free = [0 for x in range(size)]
    for i in range(size):
        for j in range(size):
            position = (i, j)
            if position not in actors:
                continue

            actor = actors[position]
            if actor == 'O':
                # shift up to min_free
                actors.pop(position)
                new_pos = (min_free[j], j)
                actors[new_pos] = 'O'
                min_free[j] = new_pos[0] + 1

            if actor == '#':
                min_free[j] = i + 1


def print_situation(actors, size):
    res = ""

    for i in range(size):
        for j in range(size):
            pos = (i, j)
            if pos in actors:
                res += actors[pos]
            else:
                res += '.'
        res += '\n'

    print(res)


def count_north_load(actors, size):
    result = 0
    for i in range(size):
        for j in range(size):
            pos = (i, j)
            if pos in actors and actors[pos] == 'O':
                result += size - i
    return result


def read_actors(data):
    actors = {}
    splitlines = data.splitlines()
    for row_idx in range(len(splitlines)):
        row = splitlines[row_idx]
        for col_idx in range(len(row)):
            char = row[col_idx]
            if char != '.':
                pos = (row_idx, col_idx)
                actors[pos] = char

    assert len(splitlines) == len(splitlines[0])

    return actors, len(splitlines)


def rotate(actors, size):
    temp = {}
    for key in actors:
        temp[key] = actors[key]

    actors.clear()
    for (i, j) in temp:
        actors[(j, size - i - 1)] = temp[(i, j)]


def part1(data):
    actors, size = read_actors(data)
    if debug_part1:
        print_situation(actors, size)

    roll_up(actors, size)
    if debug_part1:
        print_situation(actors, size)

    return count_north_load(actors, size)


def actors_hash(actors):
    return hash(frozenset(actors.items()))


def part2(data):
    actors, size = read_actors(data)

    if debug_part1:
        print_situation(actors, size)

    pattern_hashes = {actors_hash(actors): -1}

    idx = -1
    while True:
        idx += 1
        do_one_cycle(actors, size)
        current_hash = actors_hash(actors)
        print(idx, count_north_load(actors, size))
        if current_hash in pattern_hashes:
            break
        pattern_hashes[current_hash] = idx

    loop_start = pattern_hashes[current_hash]
    loop_length = idx - loop_start
    remaining = (TARGET_ITERATIONS - loop_start - 1) % loop_length

    print("remaining, loop_start, idx, loop_length " + str((remaining, loop_start, idx, loop_length)))
    for i in range(remaining):
        do_one_cycle(actors, size)
        print(i, count_north_load(actors, size))

    if debug_part1:
        print_situation(actors, size)

    return count_north_load(actors, size)


def do_one_cycle(actors, size):
    for i in range(4):
        roll_up(actors, size)
        rotate(actors, size)


def do_tests():
    testdata1 = """O....#....
O.OO#....#
.....##...
OO.#O....O
.O.....O#.
O.#..O.#.#
..O..#O..O
.......O..
#....###..
#OO..#....
"""
    print(part1(testdata1))
    print(part2(testdata1))


if __name__ == "__main__":
    input_data = get_data(os.path.basename(__file__))

    do_tests()

    print(part1(input_data))
    print(part2(input_data))
