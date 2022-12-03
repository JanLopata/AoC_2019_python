import os

from aoc_tools import get_data


def part1(data: str):
    lines = data.split("\n")

    value_sum = 0

    for line in lines:
        if line == "":
            continue

        # half of the line
        half = len(line) // 2
        first_half = line[:half]
        second_half = line[half:]
        first_set = set([x for x in first_half])
        second_set = set([x for x in second_half])

        intsec = first_set.intersection(second_set)
        ch = intsec.pop()
        value_sum += get_character_value(ch)

    return value_sum


def part2(data: str):
    lines = data.split("\n")
    found = set()

    value_sum = 0
    counter = 0

    for line in lines:

        if line == "":
            continue

        counter += 1

        if counter == 1:
            found = set([x for x in line])
        else:
            found = found.intersection(set([x for x in line]))

        if counter == 3:
            counter = 0
            ch = found.pop()
            value = get_character_value(ch)

            value_sum += value

    return value_sum


def get_character_value(ch):
    if ch.isupper():
        value = ord(ch) - ord('A') + 1 + 26
    else:
        value = ord(ch) - ord('a') + 1
    return value


if __name__ == "__main__":
    data = get_data(os.path.basename(__file__))

    print(part1(data))
    print(part2(data))
