import os


def part1(data: str):
    direct_orbit_map = parse_direct_orbit_map(data)

    counter = 0
    for start in direct_orbit_map.keys():
        counter += len(get_full_path(start, direct_orbit_map)) - 1
    return counter


def parse_direct_orbit_map(data):
    direct_orbit_map = {}
    for row in data.split("\n"):
        if len(row) == 0:
            continue
        orbit_info = row.split(")")
        direct_orbit_map[orbit_info[1]] = orbit_info[0]
    return direct_orbit_map


def get_full_path(start, direct_orbit_map):
    pointer = start
    path = []
    while pointer in direct_orbit_map:
        path.append(pointer)
        pointer = direct_orbit_map[pointer]

    path.append(pointer)
    return path


def part2(data: str):
    direct_orbit_map = parse_direct_orbit_map(data)

    you_path = get_full_path("YOU", direct_orbit_map)
    san_path = get_full_path("SAN", direct_orbit_map)

    while you_path[-1] == san_path[-1]:
        you_path.pop()
        san_path.pop()

    return len(you_path) + len(san_path) - 2


def read_data():
    with open(input_filename) as input_file:
        return input_file.read()


if __name__ == "__main__":
    this_filename = os.path.basename(__file__)
    input_filename = os.path.join("input", this_filename.replace("day", "").replace(".py", ".txt"))
    data = read_data()

    print(part1(data))
    print(part2(data))
