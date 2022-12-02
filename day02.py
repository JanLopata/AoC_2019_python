import os

from aoc_tools import get_data

values_dict = {"X": 1, "Y": 2, "Z": 3}
results_dict = {('A', 'X'): 3, ('B', 'Y'): 3, ('C', 'Z'): 3,
                ('A', 'Y'): 6, ('A', 'Z'): 0,
                ('B', 'X'): 0, ('B', 'Z'): 6,
                ('C', 'X'): 6, ('C', 'Y'): 0}

to_choose = {'X': 0, 'Y': 3, 'Z': 6}


def part1(data: str):
    score = 0
    for line in data.split("\n"):
        if line == "":
            continue

        pair = line.split(" ")
        score += results_dict[(pair[0], pair[1])] + values_dict[pair[1]]

    return score


def part2(data: str):
    score = 0
    for line in data.split("\n"):
        if line == "":
            continue

        pair = line.split(" ")

        choose_value = to_choose[pair[1]]

        for key in results_dict:
            if key[0] == pair[0] and results_dict[key] == choose_value:
                score += results_dict[key] + values_dict[key[1]]
                break

    return score


if __name__ == "__main__":
    data = get_data(os.path.basename(__file__))

    print(part1(data))
    print(part2(data))
