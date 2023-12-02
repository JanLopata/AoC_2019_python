import os

from aoc_tools import get_data

debug_part1 = True
debug_part2 = False


def part1(data):
    result = 0

    for line in data.splitlines():
        pass
    return result


def part2(data):
    pass



def do_tests():
    testdata1 = """
    """
    testdata2 = """
    """
    print(part1(testdata1))
    print(part2(testdata1))


if __name__ == "__main__":
    input_data = get_data(os.path.basename(__file__))

    do_tests()

    print(part1(input_data))
    print(part2(input_data))
