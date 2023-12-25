import os

import numpy.linalg

from aoc_tools import get_data

debug_part1 = False
debug_part2 = False

TEST_RANGE = [7, 27]
PROD_RANGE = [200000000000000, 400000000000000]


def parse_snowball(line):
    sp = line.split(" @ ")
    sp1 = [int(x) for x in sp[0].split(", ")]
    sp2 = [int(x) for x in sp[1].split(", ")]
    return sp1, sp2


def find_intersection_2d(i, j, ball1, ball2):
    p1 = ball1[0]
    p2 = ball2[0]
    d1 = ball1[1]
    d2 = ball2[1]
    dx1 = d1[0]
    dy1 = d1[1]
    dx2 = d2[0]
    dy2 = d2[1]
    px1 = p1[0]
    py1 = p1[1]
    px2 = p2[0]
    py2 = p2[1]

    matrix = numpy.array([[dx1, -dx2], [dy1, -dy2]])
    b = numpy.array(([px2 - px1, py2 - py1]))

    if numpy.linalg.det(matrix) == 0:
        return None, None, None, None

    solution = numpy.linalg.solve(matrix, b)
    t1 = solution[0]

    return px1 + dx1 * t1, py1 + dy1 * t1, t1, solution[1]
    # return x_int, y_int, tx1_int, ty_int


def part1(data):
    balls = []
    for line in data.splitlines():
        balls.append(parse_snowball(line))

    check_area_range = PROD_RANGE if len(balls) > 5 else TEST_RANGE

    collisions = []
    for i in range(len(balls)):
        for j in range(len(balls)):
            if i >= j:
                continue

            ball1 = balls[i]
            ball2 = balls[j]

            if debug_part1:
                print(i, j, ball1, ball2, find_intersection_2d(i, j, ball1, ball2))
            x, y, t1, t2 = find_intersection_2d(i, j, ball1, ball2)
            if x is None:
                continue
            if t1 < 0 or t2 < 0:
                continue

            if check_area_range[0] <= x <= check_area_range[1] and check_area_range[0] <= y <= check_area_range[1]:
                print(i, j, "collided")
                collisions.append((i, j))

    print(collisions)
    return len(collisions)


def part2(data):
    pass


def do_tests():
    testdata1 = """19, 13, 30 @ -2,  1, -2
18, 19, 22 @ -1, -1, -2
20, 25, 34 @ -2, -2, -4
12, 31, 28 @ -1, -2, -1
20, 19, 15 @  1, -5, -3
"""

    print(part1(testdata1))
    print(part2(testdata1))


if __name__ == "__main__":
    input_data = get_data(os.path.basename(__file__))

    do_tests()

    print(part1(input_data))
    # print(part2(input_data))
