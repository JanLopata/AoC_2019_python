import os

from aoc_tools import get_data

debug_part1 = True
debug_part2 = False


def parse_instructions(line):
    sp = line.split(" ")
    springs = sp[0]
    blocks = [int(x) for x in sp[1].split(",")]
    return springs, blocks


def combine(cur_blk, rem_blk, rem_data, stack, acc):
    # print(stack, "\t", cur_blk, rem_blk, rem_data)
    if len(rem_data) == 0:
        if cur_blk <= 0 and len(rem_blk) == 0:
            acc.append(stack)
        return

    if cur_blk > 0:
        if rem_data[0] == '.':
            return
        combine(cur_blk - 1, rem_blk, rem_data[1:], stack + '#', acc)
        return

    ch = rem_data[0]
    if (ch == '?' or ch == '#') and len(rem_blk) > 0 and cur_blk != 0:
        combine(rem_blk[0] - 1, rem_blk[1:], rem_data[1:], stack + '#', acc)

    if ch == '?' or ch == '.':
        combine(cur_blk - 1, rem_blk, rem_data[1:], stack + '.', acc)

    return


def part1(data):
    result = 0
    for line in data.splitlines():
        springs, blocks = parse_instructions(line)
        # print(springs, blocks)
        acc = []
        combine(-1, blocks, springs, "", acc)
        result += len(acc)

    return result


def part2(data):
    result = 0
    for line in data.splitlines():
        springs, blocks = parse_instructions(line)
        springs = 4 * (springs + "?") + springs
        blocks = 5 * blocks
        # print(springs, blocks)
        acc = []
        combine(-1, blocks, springs, "", acc)
        result += len(acc)

    return result


def do_tests():
    testdata1 = """???.### 1,1,3
.??..??...?##. 1,1,3
?#?#?#?#?#?#?#? 1,3,1,6
????.#...#... 4,1,1
????.######..#####. 1,6,5
?###???????? 3,2,1
"""
    print(part1(testdata1))
    print(part2(testdata1))


if __name__ == "__main__":
    input_data = get_data(os.path.basename(__file__))

    do_tests()

    print(part1(input_data))
    # print(part2(input_data))
