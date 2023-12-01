import os

from aoc_tools import get_data

debug_part2 = True

def part1(data):
    result = 0
    for line in data.splitlines():
        lower = -1
        upper = -1
        for ch in line:
            if ch.isdigit() and lower == -1:
                lower = int(ch)
            if ch.isdigit():
                upper = int(ch)

        result += lower * 10 + upper

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

def despell_numbers(line):
    for key in number_spelling.keys():
        line = line.replace(key, number_spelling[key])
    return line


def buffer_contains_number(buffer):
    for key in number_spelling.keys():
        if key in buffer:
            return key
    return None


def part2(data):
    result = 0
    for line in data.splitlines():

        lower = -1
        buffer = ""
        for ch in line:
            buffer += ch
            contained_number = buffer_contains_number(buffer)
            if contained_number is not None:
                ch = number_spelling[contained_number]
                buffer = ""
            if ch.isdigit():
                lower = int(ch)
                break

        upper = -1
        buffer = ""
        for ch in line[::-1]:
            buffer += ch
            contained_number = buffer_contains_number(buffer[::-1])
            if contained_number is not None:
                ch = number_spelling[contained_number]
                buffer = ""
            if ch.isdigit():
                upper = int(ch)
                break

        increment = lower * 10 + upper
        if debug_part2:
            print(line)
            print(increment)
        result += increment

    return result


if __name__ == "__main__":
    input_data = get_data(os.path.basename(__file__))

    testdata = """two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen"""

    print(part1(input_data))
    print(part2(input_data))
    # print(part2(testdata))
