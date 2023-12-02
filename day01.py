import os

from aoc_tools import get_data

debug_part1 = False
debug_part2 = False

number_spelling = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9"
}


def generate_search_map(spelling=False, reverse=False):
    result = {}
    for spelled in number_spelling:
        number = int(number_spelling[spelled])
        result[str(number)] = number
        if spelling:
            if reverse:
                result[spelled[::-1]] = number
            else:
                result[spelled] = number
    return result


def find_first_hit(line, search_map):
    buffer = ""
    for ch in line:
        buffer += ch
        for key in search_map:
            if buffer.endswith(key):
                return search_map[key]


def part1(data):
    search_map1 = generate_search_map(False, False)
    search_map2 = generate_search_map(False, True)

    result = 0

    for line in data.splitlines():
        lower = find_first_hit(line, search_map1)
        upper = find_first_hit(line[::-1], search_map2)

        if debug_part1:
            print(lower, " ", upper)

        val = lower * 10 + upper
        result += val

    return result


def part2(data):
    search_map1 = generate_search_map(True, False)
    search_map2 = generate_search_map(True, True)

    result = 0

    for line in data.splitlines():
        lower = find_first_hit(line, search_map1)
        upper = find_first_hit(line[::-1], search_map2)

        if debug_part2:
            print(lower, " ", upper)

        val = lower * 10 + upper
        result += val

    return result


def do_tests():
    testdata1 = """1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet"""
    testdata2 = """two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen"""
    print(part1(testdata1))
    print(part2(testdata2))


if __name__ == "__main__":
    input_data = get_data(os.path.basename(__file__))

    do_tests()

    print(part1(input_data))
    print(part2(input_data))
