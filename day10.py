import math
import os

debug = 0


def create_spiral(origin, grid_size):
    result = []
    # origin omitted
    for diameter in range(1, grid_size + 1):

        for i in range(-diameter, diameter):
            result.append((origin[0] - diameter, origin[1] + i))

        for i in range(-diameter, diameter):
            result.append((origin[0] + i, origin[1] + diameter))

        for i in range(diameter, -diameter, -1):
            result.append((origin[0] + diameter, origin[1] + i))

        for i in range(diameter, -diameter, -1):
            result.append((origin[0] + i, origin[1] - diameter))

    return result


def compute_visible_points(origin, grid, grid_size):
    found_points = []
    spiral = create_spiral(origin, grid_size)

    for point in spiral:
        if point in grid:
            found_points.append(point)
            remove_invisible(grid, grid_size, origin, point)

    if debug:
        print(origin, len(grid), len(found_points))
    return len(found_points)


def gcd(a, b):
    sign_a = -1 if a < 0 else 1
    sign_b = -1 if b < 0 else 1
    a = a * sign_a
    b = b * sign_b
    while b != 0:
        (a, b) = (b, a % b)
    return a


def remove_invisible(grid: set, grid_size, origin, point):
    delta = (point[0] - origin[0], point[1] - origin[1])
    divider = gcd(delta[0], delta[1])
    if divider > 1:
        delta = (int(delta[0] / divider), int(delta[1] / divider))

    inc = 0
    while True:
        inc += 1
        x = point[0] + inc * delta[0]
        if abs(x) > grid_size:
            break
        y = point[1] + inc * delta[1]
        if abs(y) > grid_size:
            break

        if (x, y) in grid:
            if debug:
                print("removing ", (x, y))
            grid.remove((x, y))


def part1(data: str):
    grid_data, grid_size = read_grid_to_set(data)

    visibility_data = {}
    for origin in grid_data:
        visible_count = compute_visible_points(origin, set(grid_data), grid_size)
        visibility_data[origin] = visible_count

    max_origin = None
    max_val = 0
    for origin in visibility_data:
        if visibility_data[origin] > max_val:
            max_origin = origin
            max_val = visibility_data[origin]

    return max_val, max_origin


def read_grid_to_set(data):
    rows = data.split("\n")
    grid_data = set()
    row_counter = 0
    for row in rows:
        if row == "":
            continue

        for i in range(len(row)):
            if row[i] == "#":
                grid_data.add((row_counter, i))

        row_counter += 1
    return grid_data, row_counter


def part2(data):
    _, origin = part1(data)
    grid_data, grid_size = read_grid_to_set(data)
    grid_data.remove(origin)

    destroyed = []
    sorted_points = sort_points_for_laser(grid_data, origin)
    while True:

        skip_angle = -4
        if len(destroyed) >= 200:
            break

        i = 0
        while i < len(sorted_points):

            point_wa = sorted_points[i]
            i += 1
            if point_wa[1] <= skip_angle:
                continue

            destroyed.append(point_wa[0])
            skip_angle = point_wa[1]
            if len(destroyed) >= 200:
                break

    last = destroyed[-1]
    return last[1] * 100 + last[0]


def sort_points_for_laser(grid_data, origin):
    sorted_points = []
    for point in grid_data:
        delta = (point[0] - origin[0], point[1] - origin[1])
        # clock-wise
        theta = - math.atan2(delta[1], delta[0])
        sorted_points.append((point, theta, delta[0] ** 2 + delta[1] ** 2))
    return sorted(sorted_points, key=lambda x: (x[1], x[2]))


def read_data():
    with open(input_filename) as input_file:
        return input_file.read()


if __name__ == "__main__":
    this_filename = os.path.basename(__file__)
    input_filename = os.path.join("input", this_filename.replace("day", "").replace(".py", ".txt"))
    data = read_data()

    print(part1(data))
    print(part2(data))
