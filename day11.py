import os

from aoc_tools import get_data


class Accumulator:

    def __init__(self):
        self.value = 0

    def increment(self):
        self.value += 1


def read_graph(data):
    graph = {}
    for line in data.split("\n"):
        sp = line.split(": ")
        if len(sp) < 2:
            continue
        source = sp[0]
        targets = [x for x in sp[1].split(" ")]
        graph[source] = targets
    return graph


def count_paths(graph, source, target, accumulator:Accumulator):
    if source == target:
        accumulator.increment()

    if source not in graph:
        return 0

    for available_target in graph[source]:
        count_paths(graph, available_target, target, accumulator)


def part1(data: str):
    graph = read_graph(data)
    acc = Accumulator()
    count_paths(graph, "you", "out", acc)
    return acc.value


def part2(data: str):
    pass


if __name__ == "__main__":
    input_data = get_data(os.path.basename(__file__))

    print(part1(input_data))
    print(part2(input_data))
