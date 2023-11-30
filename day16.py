import math
import os

from aoc_tools import get_data

debug_part1 = True
debug_part2 = True

pattern = [0, 1, 0, -1]

steps_needed = 100


def prepare_pattern(n, length):
    result = []

    idx = -1

    for counter in range(length + 1):
        if counter % n == 0:
            idx += 1
            idx %= len(pattern)
        result.append(pattern[idx])

    result.pop(0)
    return result


def prepare_patterns(n: int):
    result = []
    for i in range(n):
        result.append(prepare_pattern(i + 1, n))

    return result


def compute_value(my_input, sub_pattern):
    val = 0
    for i in range(len(my_input)):
        val += my_input[i] * sub_pattern[i]

    val = abs(val)
    val %= 10

    return val


def do_step(my_input, patterns):
    result = []
    for sub_pattern in patterns:
        sub = compute_value(my_input, sub_pattern)
        result.append(sub)

    return result


def part1(data: str):
    patterns = prepare_patterns(len(data))

    my_input = [int(x) for x in data.replace("\n", "")]
    for step in range(steps_needed):
        output = do_step(my_input, patterns)
        my_input = output

    result = ""
    for x in my_input[0:8]:
        result += str(x)
    return int(result)


def part2(data: str):
    pass


if __name__ == "__main__":
    input_data = get_data(os.path.basename(__file__))

    print(part1(input_data))
    print(part2(input_data))
