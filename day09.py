import os

from aoc_tools import get_data


def compute_span(point_a, point_b, dim_idx):
    return min(point_a[dim_idx], point_b[dim_idx]), max(point_a[dim_idx], point_b[dim_idx])


class Line:

    def __init__(self, point_a: tuple[int, int], point_b: tuple[int, int]):

        self.point_a = point_a
        self.point_b = point_b
        self.horizontal = point_a[1] == point_b[1]
        self.horizontal_span = compute_span(point_a, point_b, 0)
        self.vertical_span = compute_span(point_a, point_b, 1)

    def intersects(self, other):
        if self.horizontal == other.horizontal:
            return False

        if not self.horizontal:
            return other.intersects(self)

        return self.horizontal_span[0] <= other.horizontal_span[0] <= self.horizontal_span[1] \
            and other.vertical_span[0] <= self.vertical_span[0] <= other.vertical_span[1]

    def is_inside_of_rectangle(self, point_a: tuple[int, int], point_b=tuple[int, int]):
        x_span = compute_span(point_a, point_b, 0)
        y_span = compute_span(point_a, point_b, 1)
        return (x_span[0] < self.point_a[0] < x_span[1] and
                y_span[0] < self.point_a[1] < x_span[1]) \
            or \
            (x_span[0] < self.point_b[0] < x_span[1] and
             y_span[0] < self.point_b[1] < x_span[1])

    def __str__(self):
        return "Line ({}): {} -> {}".format("H" if self.horizontal else "V", self.point_a, self.point_b)


def read_points(data):
    result = []
    for row in data.splitlines():
        values = [int(x) for x in row.split(",")]
        result.append((values[0], values[1]))

    return result


def part1(data: str):
    points = read_points(data)

    max_product = 0
    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            diff0 = abs(points[i][0] - points[j][0])
            diff1 = abs(points[i][1] - points[j][1])
            product = (diff0 + 1) * (diff1 + 1)
            if product > max_product:
                max_product = product

    return max_product


def get_rectangle_lines(point_a: tuple[int, int], point_b: tuple[int, int]) -> list[Line]:
    result = []
    points = [point_a, (point_a[0], point_b[1]), point_b, (point_b[0], point_a[1]), point_a]
    for i in range(4):
        result.append(Line(points[i], points[i + 1]))

    return result


def has_illegal_crossing(point_a, point_b, green_lines):
    rectangle_lines = get_rectangle_lines(point_a, point_b)
    for line in rectangle_lines:
        for green_line in green_lines:
            if line.intersects(green_line):
                if green_line.is_inside_of_rectangle(point_a, point_b):
                    return True

    return False


def get_middle_point(point_a, point_b):

    x = (point_a[0] + point_b[0]) // 2
    y = (point_a[1] + point_b[1]) // 2
    result = (x, y)
    if point_a == result or point_b == result:
        raise "Invalid middle point"

    return result


def part2(data: str):
    points = read_points(data)
    previous_point = points[-1]
    green_lines = []
    for i in range(len(points)):
        current_point = points[i]
        middle_point = get_middle_point(current_point, previous_point)
        green_lines.append(Line(previous_point, middle_point))
        green_lines.append(Line(middle_point, current_point))
        previous_point = current_point

    max_product = 0
    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            point_a, point_b = points[i], points[j]
            diff0 = abs(point_a[0] - point_b[0])
            diff1 = abs(point_a[1] - point_b[1])
            product = (diff0 + 1) * (diff1 + 1)
            if product <= max_product:
                continue

            if has_illegal_crossing(point_a, point_b, green_lines):
                continue

            max_product = product
            print(max_product, point_a, point_b)

    return max_product


if __name__ == "__main__":
    input_data = get_data(os.path.basename(__file__))

    print(part1(input_data))
    print(part2(input_data))
