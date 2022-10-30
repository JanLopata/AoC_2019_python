import os
import re
from copy import deepcopy

import numpy as np
from numpy import lcm

debug_mode = False


class HeavenBody:

    def __init__(self, coords: list):
        self.position = np.array(coords)
        self.velocity = np.array([0, 0, 0])
        self.acceleration = np.array([0, 0, 0])

    def __str__(self):
        return "pos=<x={},y={},z={}>, vel=<x={},y={},z={}>".format(
            self.position[0], self.position[1], self.position[2],
            self.velocity[0], self.velocity[1], self.velocity[2],
        )

    def apply_acceleration(self):
        self.velocity += self.acceleration
        self.acceleration = np.array([0, 0, 0])

    def add_gravitation_acceleration(self, second):
        acceleration = - np.sign(self.position - second.position)
        self.acceleration += acceleration

    def apply_velocity(self):
        self.position += self.velocity

    def compute_energy(self):
        energy = sum(abs(self.position))
        energy *= sum(abs(self.velocity))
        return energy


def print_situation(step: int, bodies: list):
    if not debug_mode:
        return
    print("step: {}".format(step))
    for body in bodies:
        print(str(body))


def parse_body(line):
    pattern = re.compile("<.*=([-\\d]*),.*=([-\\d]*),.*=([-\\d]*)>")

    match = pattern.match(line)
    return HeavenBody([int(x) for x in match.groups()])


def part1(data: str):
    return compute_energy_after_n_steps(data, 1000)


def compute_energy_after_n_steps(data, n: int):
    bodies = parse_bodies(data)
    print_situation(0, bodies)
    for i in range(n):
        simulate_one_step(bodies)
        print_situation(i + 1, bodies)
    energy = sum([body.compute_energy() for body in bodies])
    return energy


def simulate_one_step(bodies):
    for i in range(len(bodies)):
        for j in range(len(bodies)):
            if i == j:
                continue
            bodies[i].add_gravitation_acceleration(bodies[j])
    for body in bodies:
        body.apply_acceleration()
        body.apply_velocity()


def parse_bodies(data):
    lines = data.split("\n")
    bodies = []
    for line in lines:
        if line == "":
            continue
        vector = parse_body(line)
        bodies.append(vector)

    return bodies


def find_full_cycle(bodies):
    dimensions_to_check = [x for x in range(3)]

    cycles_found = []
    target = [deepcopy(body) for body in bodies]

    step = 0
    while len(dimensions_to_check) > 0:

        simulate_one_step(bodies)
        step += 1
        if debug_mode and step % 1000 == 0:
            print("Step {}".format(step))
        to_remove = []
        for dim in dimensions_to_check:

            if all_bodies_match_in_given_dimension(bodies, dim, target):
                # cycle found
                print("found cycle for dim {} in {} steps".format(dim, step))
                to_remove.append(dim)

        for r in to_remove:
            dimensions_to_check.remove(r)
            cycles_found.append(step)

    return lcm_on_array(cycles_found)


def lcm_on_array(values: np.array):
    lcm_work = 1
    for steps in values:
        lcm_work = lcm(steps, lcm_work)
    return lcm_work


def position_match(body1, body2, dimension):
    return body1.position[dimension] == body2.position[dimension]


def velocity_match(body1, body2, dimension):
    return body1.velocity[dimension] == body2.velocity[dimension]


def is_match(body1, body2, dimension):
    return position_match(body1, body2, dimension) and velocity_match(body1, body2, dimension)


def all_bodies_match_in_given_dimension(bodies, dimension, target):
    return all(is_match(bodies[i], target[i], dimension) for i in range(len(bodies)))


def part2(data: str):
    bodies = parse_bodies(data)
    return find_full_cycle(bodies)


def read_data():
    with open(input_filename) as input_file:
        return input_file.read()


if __name__ == "__main__":
    this_filename = os.path.basename(__file__)
    input_filename = os.path.join("input", this_filename.replace("day", "").replace(".py", ".txt"))
    data = read_data()

    print(part1(data))
    print(part2(data))
