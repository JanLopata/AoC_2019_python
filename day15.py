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



def part2(data):
    pass


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
