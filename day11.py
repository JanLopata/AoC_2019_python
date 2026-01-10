import os

from aoc_tools import get_data


class Accumulator:

    def __init__(self):
        self.value = 0
        self.filtered_value = 0
        self.dac = 0
        self.fft = 0

    def increment(self):
        self.value += 1
        if self.dac > 0 and self.fft > 0:
            self.filtered_value += 1

    def mark_visit(self, node):
        if node == "dac":
            self.dac += 1
        if node == "fft":
            self.fft += 1

    def mark_un_visit(self, node):
        if node == "dac":
            self.dac -= 1
        if node == "fft":
            self.fft -= 1

    def __str__(self):
        return "v: {} fv: {} dac: {} fft: {}".format(self.value, self.filtered_value, self.dac, self.fft)


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


def count_paths(graph, source, target, accumulator: Accumulator):
    if source == target:
        accumulator.increment()

    if source not in graph:
        return 0

    for available_target in graph[source]:
        accumulator.mark_visit(available_target)
        count_paths(graph, available_target, target, accumulator)
        accumulator.mark_un_visit(available_target)


def part1(data: str):
    graph = read_graph(data)
    acc = Accumulator()
    count_paths(graph, "you", "out", acc)
    return acc.value


def part2(data: str):
    graph = read_graph(data)
    acc = Accumulator()
    count_paths(graph, "svr", "out", acc)
    return acc.filtered_value


if __name__ == "__main__":
    input_data = get_data(os.path.basename(__file__))

    print(part1(input_data))
    print(part2(input_data))
