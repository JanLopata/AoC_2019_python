import os

import numpy as np

from aoc_tools import get_data

debug_part1 = True
debug_part2 = False


def part1(data):
    result = 0
    for line in data.splitlines():
        dp = [int(x) for x in line.split()]
        res = []
        a = np.array(dp)
        diff = compute_diff(a)
        res.append(diff[-1])
        while diff.max() > 0 or diff.min() < 0:
            a = diff
            diff = compute_diff(a)
            res.append(diff[-1])

        increment = 0
        for x in res[::-1]:
            increment += x
        increment += dp[-1]

        result += increment

    return result


def compute_diff(a):
    shifted = np.zeros_like(a)
    shifted[1:] = a[:-1]
    diff = a - shifted
    return diff[1:]


def part2(data):
    result = 0
    for line in data.splitlines():
        dp = [int(x) for x in line.split()]
        res = []
        a = np.array(dp)
        diff = compute_diff(a)
        res.append(diff[0])
        while diff.max() > 0 or diff.min() < 0:
            a = diff
            diff = compute_diff(a)
            res.append(diff[0])

        increment = 0
        for x in res[::-1]:
            increment = x - increment

        result += dp[0] - increment

    return result


def do_tests():
    testdata1 = """0 3 6 9 12 15
1 3 6 10 15 21
10 13 16 21 30 45
"""

    print(part1(testdata1))
    print(part2(testdata1))


if __name__ == "__main__":
    input_data = get_data(os.path.basename(__file__))

    do_tests()

    print(part1(input_data))
    print(part2(input_data))
