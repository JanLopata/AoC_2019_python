import os

from aoc_tools import get_data

INFINITY = 1e20


def parse_row(row: str):
    sp = row.split(",")
    return [int(i) for i in sp]


def compute_distance_square(point_a, point_b):
    dist_square = 0
    for i in range(len(point_a)):
        diff = (point_b[i] - point_a[i])
        dist_square += diff * diff
    return dist_square


def find_shortest_distance(d_matrix):
    minimum = INFINITY
    arg_min = None
    for i in range(len(d_matrix)):
        row = d_matrix[i]
        for j in range(len(row)):
            if i == j:
                continue
            # TODO: optimize
            if row[j] < minimum:
                arg_min = i, j
                minimum = row[j]

    return arg_min[0], arg_min[1], minimum


def add_edge(circuits: dict[int, set[int]], idx1, idx2):
    circ1 = circuits[idx1]
    circ2 = circuits[idx2]

    if circ1 == circ2:
        return

    union = circ1.union(circ2)
    for idx in union:
        circuits[idx] = union


def remove_edge(d_matrix, idx1, idx2):
    d_matrix[idx1][idx2] = INFINITY
    d_matrix[idx2][idx1] = INFINITY


def part1(data: str, iterations):
    rows = data.splitlines()
    points = [parse_row(row) for row in rows]

    d_matrix = []
    for i in range(len(points)):
        matrix_row = []
        for j in range(len(points)):
            distance = compute_distance_square(points[i], points[j])
            matrix_row.append(distance)
        d_matrix.append(matrix_row)

    circuits = dict()
    for i in range(len(points)):
        circuits[i] = set()
        circuits[i].add(i)

    for k in range(iterations):
        idx1, idx2, distance = find_shortest_distance(d_matrix)
        add_edge(circuits, idx1, idx2)
        # debug_circuits(circuits, idx1, idx2, k, d_matrix, points)
        remove_edge(d_matrix, idx1, idx2)

    unique_circuits = get_unique_circuits(circuits)
    unique_circuits_lengths = [len(x) for x in unique_circuits]
    unique_circuits_lengths.sort(reverse=True)
    return unique_circuits_lengths[0] * unique_circuits_lengths[1] * unique_circuits_lengths[2]


def debug_circuits(circuits, idx1, idx2, k, d_matrix, points):
    unique_circuits = get_unique_circuits(circuits)
    print("Step {} - connecting {} -> {}, squared {}, [{} - {}]".format(
        k + 1, idx1, idx2, d_matrix[idx1][idx2], points[idx1], points[idx2]))
    unique_circuit_lengths = [len(x) for x in unique_circuits]
    unique_circuit_lengths.sort(reverse=True)
    print("unique circuit sizes: {}".format(unique_circuit_lengths))
    for c in unique_circuits:
        print(c)

    return unique_circuits


def get_unique_circuits(circuits):
    known_points = set()
    unique_circuits = []
    for circuit in circuits.values():
        if not is_known_set(circuit, known_points):
            unique_circuits.append(circuit)
            for idx in circuit:
                known_points.add(idx)
    return unique_circuits


def is_known_set(circuit: set[int], known_points):
    for idx in circuit:
        if idx in known_points:
            return True
    return False


def part2(data: str):
    pass


if __name__ == "__main__":
    input_data = get_data(os.path.basename(__file__))

    print(part1(input_data, 1000))
    print(part2(input_data))
