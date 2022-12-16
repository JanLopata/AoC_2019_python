import os
import re
from itertools import permutations

from aoc_tools import get_data

regex = re.compile(r"Valve ([A-Z][A-Z]) has flow rate=(\d+); tunnels? leads? to valves? (.*)")


def compute_distances_bfs(graph_map, source):
    distances = {}
    queue = [(source, 0)]
    while queue:
        current, distance = queue.pop(0)
        if current in distances:
            continue
        distances[current] = distance
        for neighbor in graph_map[current]:
            queue.append((neighbor, distance + 1))
    return distances


def compute_distances(graph_map):
    distance_map = {}
    for source in graph_map:
        distances = compute_distances_bfs(graph_map, source)
        for destination in distances:
            distance_map[(source, destination)] = distances[destination]
            distance_map[(destination, source)] = distances[destination]

    return distance_map


def check_global_max(global_max, pressure, visited):
    if pressure > global_max[0]:
        print(pressure, visited)
        global_max[0] = pressure
        global_max[1] = visited


def visit_and_open(start_time, source, destination, distance_map, flow_map, destinations, visited,
                   stack, pressure, opened_pressure, global_max):
    t = start_time
    travel_time = distance_map[source, destination]
    effective_time = min(travel_time, 30 - t)
    pressure += effective_time * opened_pressure
    t += effective_time

    if t >= 30:
        check_global_max(global_max, pressure, stack)
        return

    # open valve
    visited.add(destination)
    pressure += opened_pressure
    opened_pressure += flow_map[destination]
    t += 1

    if t >= 30:
        check_global_max(global_max, pressure, stack)
        visited.remove(destination)
        return

    find_max_cumulative_pressure(t, destination, distance_map, flow_map, destinations, visited,
                                 stack + [destination], pressure, opened_pressure, global_max)
    visited.remove(destination)


def find_max_cumulative_pressure(start_time, source, distance_map, flow_map, viable_destinations, visited, stack,
                                 pressure,
                                 opened_pressure, global_max):
    for destination in viable_destinations:
        if destination in visited:
            continue
        visit_and_open(start_time, source, destination, distance_map, flow_map, viable_destinations, visited, stack,
                       pressure, opened_pressure, global_max)

    effective_time = 30 - start_time
    pressure += effective_time * opened_pressure
    check_global_max(global_max, pressure, stack)


def part1(data: str):
    flow_map, graph_map = parse_input_to_maps(data)

    distance_map = compute_distances(graph_map)
    global_max = [0, []]

    viable_destinations = [(destination, flow_map[destination]) for destination in flow_map if
                           flow_map[destination] > 0]
    viable_destinations.sort(key=lambda x: x[1], reverse=True)
    viable_destinations = [x[0] for x in viable_destinations]

    print(distance_map)
    print(viable_destinations)

    find_max_cumulative_pressure(0, "AA", distance_map, flow_map, viable_destinations, set(), [], 0, 0, global_max)

    return global_max[0]


def parse_input_to_maps(data):
    graph_map = {}
    flow_map = {}
    for line in data.split("\n"):
        if line == "":
            continue
        m = regex.match(line)
        source = m.groups()[0]
        flow = int(m.groups()[1])
        destinations = m.groups()[2].split(", ")
        graph_map[source] = destinations
        flow_map[source] = flow
    return flow_map, graph_map


def part2(data: str):
    pass


if __name__ == "__main__":
    data = get_data(os.path.basename(__file__))

    print(part1(data))
    print(part2(data))
