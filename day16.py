import itertools
import os
import re
from copy import deepcopy

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


def check_global_max(global_max, valves):
    if valves.accumulated_pressure > global_max[0]:
        print(valves.accumulated_pressure, valves.visited_in_order)
        global_max[0] = valves.accumulated_pressure
        global_max[1] = valves.visited_in_order


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


def recursively_find_max_pressure(vulcano, workers, valves, global_max):
    for worker in workers:
        worker.steps_left -= 1

    if valves.time_left <= 0:
        # print("Check: ", valves.accumulated_pressure, valves.visited_in_order)
        check_global_max(global_max, valves)
        return

    indices_of_workers_to_choose_target = [i for i, worker in enumerate(workers) if worker.current_target is None]
    if len(indices_of_workers_to_choose_target) > len(valves.remaining):
        indices_of_workers_to_choose_target = indices_of_workers_to_choose_target[:len(valves.remaining)]

    if len(valves.visited_in_order) < 3:
        print(valves.visited_in_order)

    next_step = valves.after_time_step()
    for i, worker in enumerate(workers):
        if worker.is_target_reached():
            # print("Worker {} reached target {}".format(i, worker.current_target))
            next_step.open(worker.current_target, vulcano)
            worker.reset()

    if len(indices_of_workers_to_choose_target) > 0:
        for targets in itertools.permutations(valves.remaining, len(indices_of_workers_to_choose_target)):
            recursive_workers = deepcopy(workers)
            recursive_step = deepcopy(next_step)
            # print("setting targets: {} to workers {}".format(targets, [recursive_workers[i] for i in
            #                                                            indices_of_workers_to_choose_target]))
            for i, new_target in zip(indices_of_workers_to_choose_target, targets):
                worker = recursive_workers[i]
                recursive_step.target(new_target)
                worker.set_target(new_target, vulcano.distance_map[(worker.current_position, new_target)])

            recursively_find_max_pressure(vulcano, recursive_workers, recursive_step, global_max)

    if len(indices_of_workers_to_choose_target) == 0 or len(valves.remaining) == 0:
        recursively_find_max_pressure(vulcano, workers, next_step, global_max)


def part1(data: str):
    flow_map, graph_map = parse_input_to_maps(data)

    distance_map = compute_distances(graph_map)
    global_max = [0, []]

    viable_destinations = [(destination, flow_map[destination]) for destination in flow_map if
                           flow_map[destination] > 0]
    viable_destinations = [x[0] for x in viable_destinations]
    vulcano = Vulcano(distance_map, flow_map)
    workers = [Worker("AA")]

    recursively_find_max_pressure(vulcano, workers, Valves(0, 0, 0, 30, viable_destinations, None), global_max)
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
    flow_map, graph_map = parse_input_to_maps(data)

    distance_map = compute_distances(graph_map)
    global_max = [0, []]

    viable_destinations = [(destination, flow_map[destination]) for destination in flow_map if
                           flow_map[destination] > 0]
    viable_destinations = [x[0] for x in viable_destinations]
    viable_destinations.sort(key=lambda x: flow_map[x], reverse=True)
    vulcano = Vulcano(distance_map, flow_map)
    workers = [Worker("AA"), Worker("AA")]

    recursively_find_max_pressure(vulcano, workers, Valves(0, 0, 0, 26, viable_destinations, None), global_max)
    return global_max[0]


class Vulcano:
    def __init__(self, distance_map, flow_map):
        self.pressures_map = flow_map
        self.distance_map = distance_map


class Valves:
    def __init__(self, pressure, opened_pressure, time_stamp, time_left, remaining, handled_in_order=None):
        if handled_in_order is None:
            handled_in_order = []
        self.accumulated_pressure = pressure
        self.opened_pressure = opened_pressure
        self.remaining = remaining
        self.visited_in_order = handled_in_order
        self.time_stamp = time_stamp
        self.time_left = time_left

    def after_time_step(self):
        pressure = self.accumulated_pressure + self.opened_pressure
        time_stamp = self.time_stamp + 1
        # print("time {}, opened_pressure {}, accumulated {}, valves: {}".format(
        #     time_stamp, self.opened_pressure, pressure, self.visited_in_order))
        return Valves(pressure,
                      self.opened_pressure,
                      self.time_stamp + 1,
                      self.time_left - 1, deepcopy(self.remaining), deepcopy(self.visited_in_order))

    def open(self, valve, vulcano):
        if valve in self.remaining:
            self.remaining.remove(valve)
        self.opened_pressure += vulcano.pressures_map[valve]
        self.visited_in_order.append(valve)

    def target(self, valve):
        if valve in self.remaining:
            self.remaining.remove(valve)
            return True
        else:
            return False


class Worker:
    def __init__(self, position):
        self.current_target = None
        self.current_position = position
        self.steps_left = 0

    def is_target_reached(self):
        return self.current_target is not None and self.steps_left <= 0

    def reset(self):
        self.current_position = self.current_target
        self.current_target = None

    def set_target(self, target, distance):
        self.current_position = self.current_target
        self.current_target = target
        self.steps_left = distance

    def __repr__(self):
        return "Worker({}, {}, {})".format(self.current_position, self.current_target, self.steps_left)


if __name__ == "__main__":
    data = get_data(os.path.basename(__file__))

    # print(part1(data))
    print(part2(data))
