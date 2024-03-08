import math
import os

from aoc_tools import get_data

debug_part1 = False
debug_part2 = False


def parse_instructions(line):
    result = []
    for x in line:
        if x == 'R':
            result.append(1)
        else:
            result.append(0)
    return result


def parse_dm(data):
    result = {}
    for line in data.splitlines():
        line = line.replace("=", ",")
        line = line.replace("(", "")
        line = line.replace(")", "")
        line = line.replace(" ", "")
        split3 = line.split(",")
        result[split3[0]] = [split3[1], split3[2]]
    return result


def part1(data):
    split1 = data.split("\n\n")
    instructions = parse_instructions(split1[0])
    direction_map = parse_dm(split1[1])
    if debug_part1:
        print(instructions)
        print(direction_map)

    current = "AAA"
    target = "ZZZ"

    result = count_steps_to_destination(current, target, direction_map, instructions)

    return result


def count_steps_to_destination(current, target, direction_map, instructions):
    idx = 0
    result = 0
    while current != target:
        instr = instructions[idx]
        # do step
        current = direction_map[current][instr]
        #
        idx = (idx + 1) % len(instructions)
        result += 1
    return result


def count_steps_to_some_end(current, direction_map, instructions):
    idx = 0
    result = 0
    while current[2] != 'Z':
        instr = instructions[idx]
        # do step
        current = direction_map[current][instr]
        #
        idx = (idx + 1) % len(instructions)
        result += 1
    return result


def find_all_start_end(direction_map):
    all_starts = [x for x in direction_map.keys() if x.endswith("A")]
    all_ends = [x for x in direction_map.keys() if x.endswith("Z")]

    result = []
    for start in all_starts:
        end = start[0:2] + "Z"
        if end in all_ends:
            result.append((start, end))
    return result


def part2(data):
    split1 = data.split("\n\n")
    instructions = parse_instructions(split1[0])
    direction_map = parse_dm(split1[1])
    if debug_part2:
        print(instructions)
        print(direction_map)

    all_starts = [x for x in direction_map.keys() if x.endswith("A")]

    steps_per_start = []
    for start in all_starts:
        steps_per_start.append(count_steps_to_some_end(start, direction_map, instructions))

    result = steps_per_start[0]
    for x in steps_per_start:
        result = math.lcm(result, x)

    return result


def do_tests():
    testdata1 = """RL

AAA = (BBB, CCC)
BBB = (DDD, EEE)
CCC = (ZZZ, GGG)
DDD = (DDD, DDD)
EEE = (EEE, EEE)
GGG = (GGG, GGG)
ZZZ = (ZZZ, ZZZ)"""
    testdata2 = """LLR

AAA = (BBB, BBB)
BBB = (AAA, ZZZ)
ZZZ = (ZZZ, ZZZ)
"""
    testdata3 = """LR

11A = (11B, XXX)
11B = (XXX, 11Z)
11Z = (11B, XXX)
22A = (22B, XXX)
22B = (22C, 22C)
22C = (22Z, 22Z)
22Z = (22B, 22B)
XXX = (XXX, XXX)"""

    print(part1(testdata1))
    print(part1(testdata2))
    print(part2(testdata3))


if __name__ == "__main__":
    input_data = get_data(os.path.basename(__file__))

    do_tests()

    print(part1(input_data))
    print(part2(input_data))
