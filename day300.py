import os

from aoc_tools import get_data



def part2(data: str):

    lines = data.split("\n")
    for i in range(len(lines)//2):
        exp = lines[i*2]
        act = lines[i*2+1]
        print("| sed 's|{}|{}|'".format(exp, act))
    pass


if __name__ == "__main__":
    data = get_data(os.path.basename(__file__))

    print(part2(data))
