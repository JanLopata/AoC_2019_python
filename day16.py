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


def simulate(permutation, distance_map, flow_map):
    open_pressure = 0
    cumulative_pressure = 0
    t = 0
    max_time = 30
    position = "AA"
    for valve in permutation:
        travel_time = distance_map[position, valve]
        effective_time = min(travel_time, max_time - t)

        cumulative_pressure += effective_time * open_pressure
        t += effective_time
        # print(t, open_pressure, cumulative_pressure)

        if t >= max_time:
            break
        # open valve
        cumulative_pressure += open_pressure
        open_pressure += flow_map[valve]
        t += 1
        # print(t, open_pressure, cumulative_pressure)
        position = valve

    if t < max_time:
        effective_time = max_time - t
        cumulative_pressure += effective_time * open_pressure

    # print(permutation, cumulative_pressure)
    return cumulative_pressure


def part1(data: str):
    flow_map, graph_map = parse_input_to_maps(data)

    distance_map = compute_distances(graph_map)

    viable_destinations = [(destination, flow_map[destination]) for destination in flow_map if
                           flow_map[destination] > 0]
    viable_destinations.sort(key=lambda x: x[1], reverse=True)

    print(distance_map)
    print(viable_destinations)

    max_pressure = 0
    # get all permutations of viable destinations
    for permutation in permutations([x[0] for x in viable_destinations]):

        pressure = simulate(permutation, distance_map, flow_map)
        if pressure > max_pressure:
            max_pressure = pressure
            print(permutation, pressure)

     # simulate(["DD", "BB", "JJ", "HH", "EE", "CC"], distance_map, flow_map)
    # return simulate([x[0] for x in viable_destinations], distance_map, flow_map)
    return max_pressure


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
