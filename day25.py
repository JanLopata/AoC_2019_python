import os
import queue

from aoc_tools import get_data

debug_part1 = True
debug_part2 = False


def upsert(source, target, graph):
    if source not in graph:
        graph[source] = set()

    graph[source].add(target)


def remove(source, target, graph):
    if source in graph:
        graph[source].remove(target)
    if target in graph:
        graph[target].remove(source)


def parse_line(graph, line):
    sp1 = line.split(": ")
    source = sp1[0]
    targets = sp1[1].split()
    for target in targets:
        upsert(source, target, graph)
        upsert(target, source, graph)


def walk_graph(graph, start):
    go_queue = queue.Queue()
    go_queue.put(start)
    visited = set()

    while not go_queue.empty():

        current = go_queue.get()
        visited.add(current)

        for next_node in graph[current]:
            if next_node not in visited:
                go_queue.put(next_node)

    return visited


def part1(data):
    graph = {}
    for line in data.splitlines():
        parse_line(graph, line)

    if len(graph) < 20:
        to_remove = [("hfx", "pzl"), ("bvb", "cmg"), ("nvd", "jqt")]
    else:
        to_remove = [("rmt", "nqh"), ("psj", "fdb"), ("ltn", "trh")]

    for a, b in to_remove:
        remove(a, b, graph)

    visited = walk_graph(graph, to_remove[0][0])
    print(len(graph) - len(visited), len(visited))

    return (len(graph) - len(visited)) * len(visited)


def print_graph_for_dot(graph):
    for source in graph:
        for target in graph[source]:
            print("\t{} -- {}".format(source, target))


def part2(data):
    pass


def do_tests():
    testdata1 = """jqt: rhn xhk nvd
rsh: frs pzl lsr
xhk: hfx
cmg: qnr nvd lhk bvb
rhn: xhk bvb hfx
bvb: xhk hfx
pzl: lsr hfx nvd
qnr: nvd
ntq: jqt hfx bvb xhk
nvd: lhk
lsr: lhk
rzs: qnr cmg lsr rsh
frs: qnr lhk lsr
"""

    print(part1(testdata1))
    print(part2(testdata1))


if __name__ == "__main__":
    input_data = get_data(os.path.basename(__file__))

    do_tests()

    print(part1(input_data))
    # print(part2(input_data))
