import os
import re

import numpy as np

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
    pattern = re.compile("<.*=([-\d]*),.*=([-\d]*),.*=([-\d]*)>")

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


def part2(input_program: str):
    lines = data.split("\n")
    return


def read_data():
    with open(input_filename) as input_file:
        return input_file.read()


if __name__ == "__main__":
    this_filename = os.path.basename(__file__)
    input_filename = os.path.join("input", this_filename.replace("day", "").replace(".py", ".txt"))
    data = read_data()

    print(part1(data))
    print(part2(data))
