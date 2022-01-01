import os


def compute_fuel_req(mass: int):
    return int(mass / 3) - 2


def compute_combined_fuel_req(mass):
    result = 0
    increment = compute_fuel_req(mass)
    while increment > 0:
        result += increment
        increment = compute_fuel_req(increment)
    return result


def part1():
    with open(input_filename) as input_file:
        result = 0
        for line in input_file:
            result += compute_fuel_req(int(line))

        print(result)


def part2():
    with open(input_filename) as input_file:
        result = 0
        for line in input_file:
            result += compute_combined_fuel_req(int(line))

        print(result)


if __name__ == "__main__":
    this_filename = os.path.basename(__file__)
    input_filename = os.path.join("input", this_filename.replace("day", "").replace(".py", ".txt"))
    # print(input_filename)

    part1()
    part2()
