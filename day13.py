import os

from aoc_tools import get_data


def read_bracket_or_number(text, idx, depth):
    if text[idx] == "[":
        return "[", depth + 1, idx + 1
    elif text[idx] == "]":
        return "]", depth - 1, idx + 1
    elif text[idx] == ",":
        return ",", depth, idx + 1
    elif text[idx:] == "":
        return "", depth, idx + 1
    else:
        sp = text[idx:].split(",")
        number_str = sp[0]
        number_str = number_str.replace("]", "")
        if not number_str.isnumeric():
            print("ERROR", number_str)
        return int(number_str), depth, idx + len(number_str) + int(len(sp) > 1)


def in_right_order(left, right):
    print(left, right)

    if type(left) == int and type(right) == int:
        if left == right:
            return 0
        return -1 if left < right else 1

    if type(left) == int:
        return in_right_order([left], right)

    if type(right) == int:
        return in_right_order(left, [right])

    for i in range(len(left)):
        if len(right) <= i:
            return 1
        comparison = in_right_order(left[i], right[i])
        if comparison != 0:
            return comparison

    if len(right) < len(left):
        return -1

    return 0


def parse_line(line):
    idx = 0
    depth = 0
    stack = [[]]
    node = []

    while idx < len(line):
        reading, depth, idx = read_bracket_or_number(line, idx, depth)
        if reading == "[":
            new_node = []
            node.append(new_node)
            node = new_node
            stack.append(node)
        elif reading == "]":
            # stack[-2].append(node)
            node = stack.pop()
        elif reading == ",":
            pass
        else:
            node.append(reading)

    return stack[0]


def parse_recursively(line, node):
    depth = 0
    reading, depth, idx = read_bracket_or_number(line, 0, depth)


def parse_eval(line):
    chars = set([x for x in line])
    chars.add("[")
    chars.add("]")
    chars.add(",")
    for i in range(10):
        chars.add(str(i))

    if len(chars) > 13:
        print("ERROR", chars)
        raise Exception("ERROR")

    return eval(line)


def parse_block(block):
    lines = block.split("\n")
    if lines[0] == "":
        lines = lines[1:]

    left = parse_eval(lines[0])
    right = parse_eval(lines[1])
    return left, right


def part1(data: str):
    blocks = data.split("\n\n")
    counter = 0
    result = 0
    for block in blocks:
        counter += 1
        left, right = parse_block(block)
        right_order = in_right_order(left, right)
        print("{} result is {}".format((left, right), right_order))
        print()
        if right_order < 0:
            result += counter

    return result


def part2(data: str):
    pass


if __name__ == "__main__":
    data = get_data(os.path.basename(__file__))

    print(part1(data))
    print(part2(data))
