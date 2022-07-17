import os


def part1(data: str):
    direct_orbit_map = {}
    for row in data.split("\n"):
        if len(row) == 0:
            continue
        orbit_info = row.split(")")
        direct_orbit_map[orbit_info[1]] = orbit_info[0]

    counter = 0
    for start in direct_orbit_map.keys():
        counter += count_indirect(start, direct_orbit_map)
    return counter

def count_indirect(start, direct_orbit_map):
    pointer = start
    counter = 0
    while pointer in direct_orbit_map:
        counter += 1
        pointer = direct_orbit_map[pointer]

    return counter


def part2(data: str):
    return -1


def read_data():
    with open(input_filename) as input_file:
        return input_file.read()


if __name__ == "__main__":
    this_filename = os.path.basename(__file__)
    input_filename = os.path.join("input", this_filename.replace("day", "").replace(".py", ".txt"))
    data = read_data()
    # print(input_filename)

    print(part1(data))
    print(part2(data))
