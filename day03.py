import os

from aoc_tools import get_data


def find_largest_digit(data):
    mx = 0
    arg_max = 0
    for i in range(len(data)):
        if data[i] > mx:
            mx = data[i]
            arg_max = i

    return arg_max, mx


def find_largest_2digit(line: str):
    data = [int(x) for x in line]

    position, first_digit = find_largest_digit(data[:-1])
    position2, second_digit = find_largest_digit(data[position + 1:])

    return first_digit * 10 + second_digit


def find_largest_12digit(line: str):
    data = [int(x) for x in line]

    current_position = 0
    result_stack = []
    for i in range(11, -1, -1):
        if i > 0:
            target = data[current_position:-i]
        else:
            target = data[current_position:]
        position_largest_digit, largest_digit = find_largest_digit(target)
        next_position = current_position + position_largest_digit + 1
        current_position = next_position
        result_stack.append((current_position + position_largest_digit, largest_digit))

    result = 0
    for p, d in result_stack:
        result = 10 * result + d

    return result


def part1(data):
    result = 0
    for line in data.splitlines():
        result += find_largest_2digit(line)

    return result


def part2(data):
    result = 0
    for line in data.splitlines():
        if len(line) < 2:
            continue
        result += find_largest_12digit(line)

    return result


if __name__ == "__main__":
    input_data = get_data(os.path.basename(__file__))

    print(part1(input_data))
    print(part2(input_data))
