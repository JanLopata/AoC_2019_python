import os

from aoc_tools import get_data


def check_range(r: str):
    sp = r.split("-")
    first = int(sp[0])
    last = int(sp[1])
    result = []

    # naive
    for i in range(first, last + 1):
        s = str(i)
        if len(s) % 2 == 1:
            continue

        half = len(s) // 2
        if s[:half] == s[-half:]:
            result.append(s)
    return result


def has_pattern(s, pattern_length):
    if len(s) % pattern_length > 0:
        return False

    substring = s[:pattern_length]
    repeats = len(s) // pattern_length
    for i in range(1, repeats):
        if s[i * pattern_length:(i + 1) * pattern_length] != substring:
            return False

    return True


def check_range_2(r: str):
    sp = r.split("-")
    first = int(sp[0])
    last = int(sp[1])
    result = []

    # naive
    for i in range(first, last + 1):
        s = str(i)

        half = len(s) // 2
        for pattern_length in range(1, half + 1):
            if has_pattern(s, pattern_length):
                result.append(s)
                break

    return result


def part1(data):
    ranges = [x for x in data.split(",")]

    invalids = []
    for r in ranges:
        current_invalids = check_range(r)
        invalids.extend(current_invalids)

    result = 0
    for inv in invalids:
        result += int(inv)

    return result


def part2(data):
    ranges = [x for x in data.split(",")]

    invalids = []
    for r in ranges:
        current_invalids = check_range_2(r)
        invalids.extend(current_invalids)

    result = 0
    for inv in invalids:
        result += int(inv)

    return result


if __name__ == "__main__":
    input_data = get_data(os.path.basename(__file__))

    print(part1(input_data))
    print(part2(input_data))
