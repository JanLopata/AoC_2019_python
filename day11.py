import os

from aoc_tools import get_data


class PathCounter:
    def __init__(self):
        self.memory = {}

    def memoize(self, source, path_count):
        self.memory[source] = path_count

    def is_memoized(self, source):
        return source in self.memory.keys()

    def get_path_count(self, source):
        if self.is_memoized(source):
            return self.memory[source]
        else:
            return 0


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


def count_paths(graph, source, target, path_counter: PathCounter):
    if path_counter.is_memoized(source):
        return path_counter.get_path_count(source)

    if source == target:
        path_counter.memoize(source, 1)
        return 1

    if source not in graph:
        return 0

    for available_target in graph[source]:
        count_paths(graph, available_target, target, path_counter)

    path_count = sum([path_counter.get_path_count(target) for target in graph[source]])
    path_counter.memoize(source, path_count)

    return path_count


def part1(data: str):
    graph = read_graph(data)
    path_counter = PathCounter()
    count_paths(graph, "you", "out", path_counter)
    return path_counter.get_path_count("you")


def part2(data: str):
    graph = read_graph(data)

    c1 = PathCounter()
    count_paths(graph, "svr", "fft", c1)

    c2 = PathCounter()
    count_paths(graph, "fft", "dac", c2)

    c3 = PathCounter()
    count_paths(graph, "dac", "out", c3)

    return c1.get_path_count("svr") * c2.get_path_count("fft") * c3.get_path_count("dac")


if __name__ == "__main__":
    input_data = get_data(os.path.basename(__file__))

    print(part1(input_data))
    print(part2(input_data))
