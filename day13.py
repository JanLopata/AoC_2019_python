import os

from aoc_tools import get_data

debug_part1 = True
debug_part2 = False


def check_symmetry(data, start):
    idx = 0
    first = start - idx - 1
    second = start + idx
    while second < len(data) and first >= 0:
        if data[first] != data[second]:
            return False
        idx += 1
        first = start - idx - 1
        second = start + idx

    return True


def find_symmetry(data):
    prev = -1
    for i in range(len(data)):
        if data[i] == prev:
            if check_symmetry(data, i):
                return i
        prev = data[i]
    return 0


def read_to_numbers(data):
    rows = []
    cols = None
    for line in data.splitlines():
        new_row = 0
        if cols is None:
            cols = [0 for _ in range(len(line))]
        for col in range(len(line)):

            val = 0
            if line[col] == '#':
                val = 1
            new_row = new_row * 2 + val
            cols[col] = cols[col] * 2 + val
        rows.append(new_row)
    return cols, rows


def part1(data):
    result = 0
    for subdata in data.split("\n\n"):
        cols, rows = read_to_numbers(subdata)

        sym_col = find_symmetry(cols)
        sym_row = find_symmetry(rows)

        incr = sym_row * 100 + sym_col
        result += incr

    return result


def part2(data):
    pass


def do_tests():
    testdata1 = """#.##..##.
..#.##.#.
##......#
##......#
..#.##.#.
..##..##.
#.#.##.#.

#...##..#
#....#..#
..##..###
#####.##.
#####.##.
..##..###
#....#..#
"""
    print(part1(testdata1))
    print(part2(testdata1))


if __name__ == "__main__":
    input_data = get_data(os.path.basename(__file__))

    do_tests()

    print(part1(input_data))
    # print(part2(input_data))
