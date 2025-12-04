import os

from aoc_tools import get_data


def count_neighbourhood(coords, item_set):
    neighbours = 0
    x, y = coords
    for i in range(x - 1, x + 2):
        for j in range(y - 1, y + 2):
            if x == i and y == j:
                continue
            if (i, j) in item_set:
                neighbours += 1

    return neighbours


def part1(data: str):
    item_set = load_items(data)

    result = len(get_accessible(item_set))

    return result


def get_accessible(item_set):
    result = []
    for coords in item_set:
        neighbours = count_neighbourhood(coords, item_set)
        if neighbours < 4:
            result.append(coords)
    return result


def load_items(data):
    item_set = set()
    line_num = 0
    for line in data.splitlines():
        line_num += 1
        col_num = 0
        for char in line:
            col_num += 1
            if char == '@':
                item_set.add((line_num, col_num))
    return item_set


def part2(data: str):
    result = 0
    item_set = load_items(data)

    while True:
        accessible = get_accessible(item_set)
        result += len(accessible)
        if len(accessible) == 0:
            break
        for a in accessible:
            item_set.remove(a)

    return result


if __name__ == "__main__":
    input_data = get_data(os.path.basename(__file__))

    print(part1(input_data))
    print(part2(input_data))
