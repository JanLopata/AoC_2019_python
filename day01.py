import os

from aoc_tools import get_data


def compute_fuel_req(mass: int):
    return int(mass / 3) - 2


def compute_combined_fuel_req(mass):
    result = 0
    increment = compute_fuel_req(mass)
    while increment > 0:
        result += increment
        increment = compute_fuel_req(increment)
    return result


def part1(data: str):
    result = 0
    for line in data.splitlines():
        result += compute_fuel_req(int(line))

    return result


def part2(data: str):
    result = 0
    for line in data.splitlines():
        result += compute_combined_fuel_req(int(line))

    return result


if __name__ == "__main__":
    input_data = get_data(os.path.basename(__file__))

    print(part1(input_data))
    print(part2(input_data))
