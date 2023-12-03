import os

from aoc_tools import get_data

debug_part1 = False
debug_part2 = False


def find_parts(schematic, searched_char=None):
    parts = {}
    for i in range(len(schematic)):
        row = schematic[i]
        for j in range(len(row)):
            ch = row[j]
            if ch.isdigit():
                continue
            if ch == ".":
                continue

            if searched_char is None or ch == searched_char:
                parts[(i, j)] = ch
    return parts


def coord_adjacent_part(dn, parts):
    j1 = dn[2] - 1
    j2 = dn[2] + 1 + dn[3]

    rn = dn[1]
    for i in [rn - 1, rn, rn + 1]:
        for j in range(j1, j2):
            if (i, j) in parts:
                return i, j

    return None


def detect_numbers(schematic):
    numbers_detected = []
    buffer = ""
    for i in range(len(schematic)):
        row = schematic[i]
        for j in range(len(row)):
            char = row[j]
            if char.isdigit():
                buffer += char
                continue
            if len(buffer) > 0:
                detected_number = (int(buffer), i, j - len(buffer), len(buffer))
                numbers_detected.append(detected_number)
                buffer = ""
    return numbers_detected


def get_schematic(data):
    # add dot to every line so the buffer is cleaned up automatically
    schematic = [x + "." for x in data.splitlines()]
    return schematic


def part1(data):

    schematic = get_schematic(data)
    if debug_part1:
        for line in schematic:
            print(line)
        print()

    parts = find_parts(schematic)

    numbers_detected = detect_numbers(schematic)

    if debug_part1:
        print(numbers_detected)
        print(parts)

    result = 0
    for dn in numbers_detected:
        if coord_adjacent_part(dn, parts) is not None:
            if debug_part1:
                print(dn, "is part number")
            result += int(dn[0])
        else:
            if debug_part1:
                print(dn, "is not part number")
    return result


def part2(data):
    result = 0

    schematic = get_schematic(data)
    parts = find_parts(schematic, '*')

    numbers_detected = detect_numbers(schematic)

    possible_gears = {}
    for num in numbers_detected:
        possible_gear = coord_adjacent_part(num, parts)
        if possible_gear is not None:
            if possible_gear in possible_gears:
                possible_gears[possible_gear].append(num)
            else:
                possible_gears[possible_gear] = [num]

    if debug_part2:
        for g in possible_gears:
            print(possible_gears[g])
    for g in possible_gears:
        pg = possible_gears[g]
        if len(pg) != 2:
            continue

        result += pg[0][0] * pg[1][0]

    return result


def do_tests():
    testdata1 = """467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598.."""
    print(part1(testdata1))
    print(part2(testdata1))


if __name__ == "__main__":
    input_data = get_data(os.path.basename(__file__))

    do_tests()

    print(part1(input_data))
    print(part2(input_data))
