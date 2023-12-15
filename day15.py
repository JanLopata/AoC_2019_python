import os

from aoc_tools import get_data

debug_part1 = True
debug_part2 = False


def compute_hash(data):
    result = 0
    for ch in data:
        result += ord(ch)
        result *= 17
        result %= 256
    return result


def part1(data):
    result = 0
    for inp in data.strip().split(","):
        result += compute_hash(inp)

    return result


def add_to_box(list_to_add, label, power):
    found_same = False
    for i in range(len(list_to_add)):
        current_lens = list_to_add[i]
        if current_lens.label == label:
            found_same = True
            list_to_add[i] = Lens(label, power)

    if not found_same:
        list_to_add.append(Lens(label, power))


def remove_from_box(list_to_remove_from, label):
    remaining = []
    for i in range(len(list_to_remove_from)):

        current_lens = list_to_remove_from[i]
        if current_lens.label != label:
            remaining.append(current_lens)

    list_to_remove_from.clear()
    for x in remaining:
        list_to_remove_from.append(x)

    pass


def compute_box_holding_factor(box):
    if len(box) == 0:
        return 0

    result = 0
    for i in range(len(box)):
        lens = box[i]
        result += (i + 1) * lens.power

    return result


def compute_score(boxes):
    sum = 0
    for i in range(len(boxes)):
        box_n = i + 1
        factor = compute_box_holding_factor(boxes[i])
        sum += box_n * factor

    return sum


def part2(data):
    boxes = [[] for _ in range(256)]

    for inp in data.strip().split(","):
        hsh = compute_hash(inp)

        if '=' in inp:
            split = inp.split("=")
            label = split[0]
            label_hsh = compute_hash(label)
            add_to_box(list_to_add=boxes[label_hsh], label=label, power=split[1])

        if inp.endswith("-"):
            label = inp[:-1]
            label_hsh = compute_hash(label)
            remove_from_box(list_to_remove_from=boxes[label_hsh], label=label)

    return compute_score(boxes)


class Lens:

    def __init__(self, label, power):
        self.label = label
        self.power = int(power)

    def __repr__(self):
        return "{} {}x".format(self.label, self.power)


def do_tests():
    testdata1 = """rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7
"""

    print(part1(testdata1))
    print(part2(testdata1))


if __name__ == "__main__":
    input_data = get_data(os.path.basename(__file__))

    do_tests()

    print(part1(input_data))
    print(part2(input_data))
