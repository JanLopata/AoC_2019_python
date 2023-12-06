import math
import os

from aoc_tools import get_data

debug_part1 = False
debug_part2 = False


def make_figures(r):
    print("Max duration:", r)
    for x in range(r + 1):
        print("{}\t{}".format(x, x * r - x * x))
    print("============")


def part1(data):
    result = 1

    input_rows = data.splitlines()
    durations = [int(x) for x in input_rows[0].split(": ")[1].split()]
    distances = [int(x) for x in input_rows[1].split(": ")[1].split()]

    for i in range(len(durations)):
        distance = distances[i] + 1
        duration = durations[i]

        if debug_part1:
            make_figures(duration)

        ways_to_win = compute_ways_to_win(distance, duration)

        if ways_to_win > 0:
            result *= ways_to_win

    return result


def compute_ways_to_win(distance, duration):
    min_win = (duration - math.sqrt(duration * duration - 4 * distance)) / 2
    max_win = (duration + math.sqrt(duration * duration - 4 * distance)) / 2
    ways_to_win = math.floor(max_win) - math.ceil(min_win) + 1
    return ways_to_win


def part2(data):
    input_rows = data.splitlines()
    duration = int(input_rows[0].replace(" ", "").split(":")[1])
    distance = int(input_rows[1].replace(" ", "").split(":")[1])

    return compute_ways_to_win(distance, duration)


def do_tests():
    testdata1 = """Time:      7  15   30
Distance:  9  40  200
"""
    print(part1(testdata1))
    print(part2(testdata1))


if __name__ == "__main__":
    input_data = get_data(os.path.basename(__file__))

    do_tests()

    print(part1(input_data))
    print(part2(input_data))
