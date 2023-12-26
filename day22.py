import os
import queue

from aoc_tools import get_data

debug_part1 = False
debug_part2 = True


def add_to_playground(brick, playground):
    for vector in brick.all_blocks():
        playground[vector] = brick.idx


def remove_from_supports(idx, supports):
    # can be optimized, the supports should be represented with two dicts
    to_remove = []
    for supported in supports:
        if idx in supports[supported]:
            supps = supports[supported]
            supps.remove(idx)
            if len(supps) == 0:
                to_remove.append(supported)

    for i in to_remove:
        supports.pop(i)

    return to_remove


def remove_from_playground(brick, playground):
    for vector in brick.all_blocks():
        playground.pop(vector)


def fall_brick_down(brick, playground, supports):
    remove_from_supports(brick.idx, supports)
    remove_from_playground(brick, playground)
    brick.move_down()
    add_to_playground(brick, playground)
    for element in brick.all_blocks():
        add_support_if_any(brick.idx, element, playground, supports)


def fall_down(bricks, playground, supports):
    falls = 0
    for brick in bricks:
        if brick.idx in supports:
            # is supported
            continue
        if brick.start[2] <= 1 or brick.end[2] <= 1:
            continue

        fall_brick_down(brick, playground, supports)
        falls += 1

    return falls > 0


def upsert_support(supported_idx, supporting_idx, supports):
    if supported_idx not in supports:
        supports[supported_idx] = set()

    supports[supported_idx].add(supporting_idx)


def add_support_if_any(idx, element, playground, supports):
    under = (element[0], element[1], element[2] - 1)
    if under in playground and playground[under] != idx:
        upsert_support(idx, playground[under], supports)


def find_supports(playground):
    supports = {}
    checked_indices = set()

    for element in playground:

        idx = playground[element]
        if idx in checked_indices:
            continue

        add_support_if_any(idx, element, playground, supports)

    return supports


def part1(data):
    bricks = []
    idx = 0
    for line in data.splitlines():
        idx += 1
        brick = Bricke(idx, line)
        bricks.append(brick)
        if debug_part1:
            print(brick, brick.all_blocks())

    playground = {}
    for brick in bricks:
        add_to_playground(brick, playground)

    supports = find_supports(playground)
    while True:
        if not fall_down(bricks, playground, supports):
            break

    if debug_part1:
        print(supports)

    cannot = set()
    for k in supports:
        if len(supports[k]) == 1:
            only_support = [x for x in supports[k]][0]
            cannot.add(only_support)
            # print("{} cannot be ddd".format(only_support))

    return len(bricks) - len(cannot)


def copy_supports(supports):
    supports_copy = {}
    for key in supports:
        supports_copy[key] = set()
        for element in supports[key]:
            supports_copy[key].add(element)

    return supports_copy


def part2(data):
    bricks = []
    idx = 0
    for line in data.splitlines():
        idx += 1
        brick = Bricke(idx, line)
        bricks.append(brick)
        if debug_part1:
            print(brick, brick.all_blocks())

    playground = {}
    for brick in bricks:
        add_to_playground(brick, playground)

    supports = find_supports(playground)
    while True:
        if not fall_down(bricks, playground, supports):
            break

    if debug_part2:
        print(supports)

    unsafe = set()
    for k in supports:
        if len(supports[k]) == 1:
            only_support = [x for x in supports[k]][0]
            unsafe.add(only_support)
            # print("{} cannot be ddd".format(only_support))

    moved_sum = 0
    for unsafe_block_idx in unsafe:
        supports_copy = copy_supports(supports)

        work_queue = queue.Queue()
        work_queue.put(unsafe_block_idx)

        moved = 0
        while not work_queue.empty():
            current_idx = work_queue.get()
            removed = remove_from_supports(current_idx, supports_copy)
            moved += len(removed)
            for rem in removed:
                work_queue.put(rem)
        moved_sum += moved

    return moved_sum


class Bricke:

    def __init__(self, idx, line):
        spl = line.split("~")
        # self.idx = chr(ord('A') - 1 + idx)
        self.idx = idx
        self.start = [int(x) for x in spl[0].split(",")]
        self.end = [int(x) for x in spl[1].split(",")]

    def all_blocks(self):
        result = []
        for x in range(self.start[0], self.end[0] + 1):
            for y in range(self.start[1], self.end[1] + 1):
                for z in range(self.start[2], self.end[2] + 1):
                    result.append((x, y, z))
        return result

    def move_down(self):
        self.start[2] += -1
        self.end[2] += -1

    def __repr__(self):
        return str((self.idx, self.start, self.end))


def do_tests():
    testdata1 = """1,0,1~1,2,1
0,0,2~2,0,2
0,2,3~2,2,3
0,0,4~0,2,4
2,0,5~2,2,5
0,1,6~2,1,6
1,1,8~1,1,9
"""

    print(part1(testdata1))
    print(part2(testdata1))


if __name__ == "__main__":
    input_data = get_data(os.path.basename(__file__))

    do_tests()

    print(part1(input_data))
    print(part2(input_data))
