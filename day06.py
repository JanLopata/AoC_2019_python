import os

from aoc_tools import get_data


def parse_numbers(line: str, numbers: list[list[int]] | None):
    row_numbers = [int(x) for x in line.split()]
    for i in range(len(row_numbers)):
        numbers[i].append(row_numbers[i])

    return numbers


def initialize_numbers(data):
    first_line = data.splitlines()[0]
    numbers = []
    for _ in first_line.split():
        numbers.append([])
    return numbers


def parse_data(data):
    numbers = initialize_numbers(data)
    operators = []

    for line in data.splitlines():
        if "+" in line or "*" in line:
            parse_operators(line, operators)
        else:
            numbers = parse_numbers(line, numbers)

    return numbers, operators


def parse_operators(line, operations):
    for op in line.split():
        operations.append(op)


def part1(data: str):
    result = 0
    numbers, operators = parse_data(data)
    for col_i in range(len(numbers)):
        neutral, operation = get_operation(operators[col_i])

        col_result = neutral
        for num in numbers[col_i]:
            col_result = operation(col_result, num)
        result += col_result

    return result


def get_operation(symbol):
    if symbol == "+":
        operation = lambda x, y: x + y
        neutral = 0
    else:
        operation = lambda x, y: x * y
        neutral = 1
    return neutral, operation


def parse_data_backwards(data):
    backwards = []
    for line in data.splitlines():
        backwards.append(line[::-1])

    cols = len(backwards[0])
    rows = len(backwards)

    current_numbers = []
    skip = False
    for col in range(cols):
        if skip:
            skip = False
            continue

        current_number = 0
        for row in range(rows - 1):
            symbol = backwards[row][col]
            if symbol != " ":
                digit = int(symbol)
                current_number = current_number * 10 + digit

        current_numbers.append(current_number)

        operator_symbol = backwards[-1][col]
        if operator_symbol in ["+", "*"]:
            yield current_numbers, operator_symbol
            current_numbers = []
            skip = True


def part2(data: str):
    result = 0
    for numbers, operator in parse_data_backwards(data):
        neutral, operation = get_operation(operator)
        tmp = neutral
        for num in numbers:
            tmp = operation(tmp, num)
        result += tmp
    return result


if __name__ == "__main__":
    input_data = get_data(os.path.basename(__file__))

    print(part1(input_data))
    print(part2(input_data))
