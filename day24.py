import os

import numpy.linalg
import scipy

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


def compute_derivative(current_guess, balls):
    derivative = numpy.zeros(shape=6 + len(balls))
    derivative[0:3] = [derivative_by_constant_part(current_guess, balls, j) for j in range(3)]
    derivative[3:6] = [derivative_by_linear_part(current_guess, balls, j) for j in range(3)]
    derivative[6:] = [derivative_by_time_part(current_guess, balls, i) for i in range(len(balls))]

    return derivative


def minimize_error(balls):
    problem_size = 6 + len(balls)

    current_guess = numpy.zeros(problem_size)
    error = error_function(current_guess, balls)
    derivative = compute_derivative(current_guess, balls)
    step = 0.001
    counter = 0
    result = scipy.optimize.minimize(fun=lambda x: error_function(x, balls), x0=numpy.zeros(problem_size), jac=lambda x: compute_derivative(x, balls))

    print(result)
    return result.get('x')


def part2(data):
    balls = []
    for line in data.splitlines():
        balls.append(parse_snowball(line))

    minimum = minimize_error(balls)
    rounded_guess = [round(x) for x in minimum]
    print(rounded_guess)
    print(error_function(rounded_guess, balls))
    return rounded_guess[0] + rounded_guess[1] + rounded_guess[2]


def error_function(current_guess, balls):
    t_values = current_guess[6:]
    error_value = 0
    for i in range(len(balls)):
        for j in range(3):
            ball = balls[i]
            bt = ball[0][j] + ball[1][j] * t_values[i]
            gt = current_guess[j] + current_guess[j + 3] * t_values[i]
            err = bt - gt
            error_value += err * err

    return error_value


def derivative_by_constant_part(current_guess, balls, j):
    t_values = current_guess[6:]
    derivative = 0
    for i in range(len(balls)):
        ball = balls[i]
        diff = -2 * (ball[0][j] - current_guess[j] + t_values[i] * (ball[1][j] - current_guess[j + 3]))
        derivative += diff

    return derivative


def derivative_by_linear_part(current_guess, balls, j):
    t_values = current_guess[6:]
    derivative = 0
    for i in range(len(balls)):
        ball = balls[i]
        diff = -2 * t_values[i] * (ball[0][j] - current_guess[j] + t_values[i] * (ball[1][j] - current_guess[j + 3]))
        derivative += diff

    return derivative


def derivative_by_time_part(current_guess, balls, i):
    t_values = current_guess[6:]
    derivative = 0
    ball = balls[i]
    for j in range(3):
        diff = 2 * (ball[1][j] - current_guess[j + 3]) * \
               (ball[0][j] - current_guess[j] + t_values[i] * (ball[1][j] - current_guess[j + 3]))
        derivative += diff

    return derivative


def do_tests():
    testdata1 = """19, 13, 30 @ -2,  1, -2
18, 19, 22 @ -1, -1, -2
20, 25, 34 @ -2, -2, -4
12, 31, 28 @ -1, -2, -1
20, 19, 15 @  1, -5, -3
"""

    # print(part1(testdata1))
    print(part2(testdata1))


if __name__ == "__main__":
    input_data = get_data(os.path.basename(__file__))

    do_tests()

    # print(part1(input_data))
    print(part2(input_data))
