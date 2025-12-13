import os

from aoc_tools import get_data


def read_points(data):
    result = []
    for row in data.splitlines():
        values = [int(x) for x in row.split(",")]
        result.append((values[0], values[1]))

    return result


def part1(data: str):
    points = read_points(data)

    max_product = 0
    arg_max = None
    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            diff0 = abs(points[i][0] - points[j][0])
            diff1 = abs(points[i][1] - points[j][1])
            product = (diff0 + 1) * (diff1 + 1)
            if product > max_product:
                # print("{}, {} -> {}".format(points[i], points[j], product))
                max_product = product
                arg_max = (i, j)

    return max_product


def part2(data: str):
    pass


if __name__ == "__main__":
    input_data = get_data(os.path.basename(__file__))

    print(part1(input_data))
    print(part2(input_data))
