import os

from aoc_tools import get_data

debug_part1 = True
debug_part2 = False


def roll_up(actors, row_max, col_max):
    min_free = [0 for x in range(col_max)]
    for i in range(row_max):
        for j in range(col_max):
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


def print_situation(actors, row_max, col_max):
    res = ""

    for i in range(row_max):
        for j in range(col_max):
            pos = (i, j)
            if pos in actors:
                res += actors[pos]
            else:
                res += '.'
        res += '\n'

    print(res)


def count_north_load(actors, row_max, col_max):
    result = 0
    for i in range(row_max):
        for j in range(col_max):
            pos = (i, j)
            if pos in actors and actors[pos] == 'O':
                result += row_max - i
    return result


def part1(data):
    actors, row_max, col_max = read_actors(data)
    if debug_part1:
        print_situation(actors, row_max, col_max)

    roll_up(actors, row_max, col_max)
    if debug_part1:
        print_situation(actors, row_max, col_max)

    return count_north_load(actors, row_max, col_max)


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

    return actors, len(splitlines), len(splitlines[0])


def part2(data):
    pass


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
