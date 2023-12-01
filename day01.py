import os

from aoc_tools import get_data

debug_part1 = False
debug_part2 = False


def find_first_number(line, reverse, use_spelling):
    if reverse:
        line = line[::-1]

    buffer = ""
    for ch in line:
        buffer += ch
        if reverse and use_spelling:
            possibly_reversed_buffer = buffer[::-1]
        else:
            possibly_reversed_buffer = buffer

        if use_spelling:
            spelled = buffer_contains_number(possibly_reversed_buffer)
            if spelled is not None:
                ch = number_spelling[spelled]
        if ch.isdigit():
            return int(ch)


def part1(data):
    result = 0

    for line in data.splitlines():
        lower = find_first_number(line, False, False)
        upper = find_first_number(line, True, False)

        if debug_part1:
            print(lower, " ", upper)

        val = lower * 10 + upper
        result += val

    return result


def part2(data):
    result = 0

    for line in data.splitlines():
        lower = find_first_number(line, False, True)
        upper = find_first_number(line, True, True)

        if debug_part2:
            print(lower, " ", upper)

        val = lower * 10 + upper
        result += val

    return result


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


def buffer_contains_number(buffer):
    for key in number_spelling.keys():
        if key in buffer:
            return key
    return None


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

    # do_tests()

    print(part1(input_data))
    print(part2(input_data))

