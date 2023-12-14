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


def print_grid(grid):
    for row in grid:
        print("".join(row))


def find_symmetry(data):
    prev = -1
    for i in range(len(data)):
        if data[i] == prev:
            if check_symmetry(data, i):
                return i
        prev = data[i]
    return 0


def find_symmetries(data):
    symmetries_found = []
    prev = -1
    for i in range(len(data)):
        if data[i] == prev:
            if check_symmetry(data, i):
                symmetries_found.append(i)
        prev = data[i]

    return symmetries_found


def read_to_numbers(grid):
    rows = []
    cols = None
    for row in grid:
        new_row = 0
        if cols is None:
            cols = [0 for _ in range(len(row))]
        for col in range(len(row)):

            val = 0
            if row[col] == '#':
                val = 1
            new_row = new_row * 2 + val
            cols[col] = cols[col] * 2 + val
        rows.append(new_row)
    return cols, rows


def convert_to_grid(data):
    rows = []
    for line in data.splitlines():
        new_row = []
        for col in range(len(line)):
            new_row.append(line[col])
        rows.append(new_row)
    return rows


def part1(data):
    result = 0
    for subdata in data.split("\n\n"):
        grid = convert_to_grid(subdata)
        cols, rows = read_to_numbers(grid)

        sym_col = find_symmetry(cols)
        sym_row = find_symmetry(rows)

        incr = sym_row * 100 + sym_col
        result += incr

    return result


def get_smudge(ch):
    if ch == '#':
        return '.'
    else:
        return '#'


def remove_smudge_and_find_symmetry(grid, ignored_sym):

    for i in range(len(grid)):
        for j in range(len(grid[0])):

            orig = grid[i][j]
            smudge = get_smudge(orig)
            grid[i][j] = smudge
            cols, rows = read_to_numbers(grid)

            grid[i][j] = orig

            sym_col = find_symmetries(cols)
            sym_row = find_symmetries(rows)
            if ignored_sym[0] in sym_col:
                sym_col.remove(ignored_sym[0])
            if ignored_sym[1] in sym_row:
                sym_row.remove(ignored_sym[1])

            score = 0
            if len(sym_col) == 1:
                score += sym_col[0]

            if len(sym_row) == 1:
                score += sym_row[0] * 100

            if score > 0:
                return score

    return 0


def remove_smudge_and_find_symmetry_score(grid):
    cols, rows = read_to_numbers(grid)
    sym_col = find_symmetry(cols)
    sym_row = find_symmetry(rows)

    return remove_smudge_and_find_symmetry(grid, (sym_col, sym_row))


def part2(data):
    result = 0
    for subdata in data.split("\n\n"):
        grid = convert_to_grid(subdata)
        result += remove_smudge_and_find_symmetry_score(grid)

    return result


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

    testdata2 = """##....##.#.
##.##.#..#.
..####....#
#######..##
##..#......
...##......
###....##..
..#.#..##..
...#.#....#
..##.......
..##.#.##.#
##...##..##
######.##.#
###...#..#.
...###....#
..##.......
###.##....#"""

    print(part1(testdata1))
    print(part2(testdata1))

    print(part1(testdata2))
    print(part2(testdata2))


if __name__ == "__main__":
    input_data = get_data(os.path.basename(__file__))

    do_tests()

    print(part1(input_data))
    print(part2(input_data))
