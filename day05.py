import math
import os

from aoc_tools import get_data

debug_part1 = False
debug_part2 = False


class AlmanachMapper:

    def __init__(self):
        self.range_breaks = [-1]
        self.range_shifts = [0]

    def __str__(self):
        return "Breaks: " + str(self.range_breaks) + ", shifts: " + str(self.range_shifts)

    def add_range(self, line):
        split = [int(x.strip()) for x in line.split(" ")]
        dest_start = split[0]
        source_start = split[1]
        length = split[2]
        source_end = source_start + length
        shift_diff = dest_start - source_start

        if debug_part1:
            print("To {} will add range {} to {}".format(self, source_start, source_end))

        self.add_start(source_start, shift_diff)
        self.add_end(source_end)

    def add_start(self, source_start, shift_diff):
        position_to_insert = 0

        for i in range(len(self.range_breaks)):
            if self.range_breaks[i] <= source_start:
                position_to_insert = i

        if self.range_breaks[position_to_insert] == source_start:
            # only update
            self.range_shifts[position_to_insert] = shift_diff
            return

        self.range_breaks.insert(position_to_insert + 1, source_start)
        self.range_shifts.insert(position_to_insert + 1, shift_diff)
        self.check_validity()

    def add_end(self, source_end):

        position_to_insert = len(self.range_breaks) - 1
        for i in range(len(self.range_breaks) - 1, 0, -1):
            if self.range_breaks[i] <= source_end:
                position_to_insert = i
                break

        if self.range_breaks[position_to_insert] == source_end:
            pass
        else:
            self.range_breaks.insert(position_to_insert + 1, source_end)
            self.range_shifts.insert(position_to_insert + 1, 0)
        self.check_validity()

    def map_number_with_debug(self, x):
        result = self.map_number(x)
        if debug_part1:
            print("Mapping {} to {} using {}".format(x, result, self))
        return result

    def map_number(self, x):
        if x < self.range_breaks[0]:
            return x

        for i in range(len(self.range_breaks) - 1):
            if self.range_breaks[i] <= x < self.range_breaks[i + 1]:
                return x + self.range_shifts[i]

        return x

    def check_validity(self):
        prev = -math.inf
        for x in self.range_breaks:
            assert prev < x, "Not ascending" + self
            prev = x


def remap(x, almanach):
    current = x
    for mapper in almanach:
        current = mapper.map_number_with_debug(current)

    return current


def part1(data):
    first = True
    seeds_to_plant = []
    almanach = []
    for section in data.split("\n\n"):

        if first:
            seeds_to_plant = [int(x.strip()) for x in section.split(": ")[1].split(" ")]
            if debug_part1:
                print(seeds_to_plant)
            first = False
            continue

        mapper = AlmanachMapper()
        first_row = True
        for line in section.splitlines():
            if first_row:
                first_row = False
                continue

            mapper.add_range(line)

        almanach.append(mapper)

    return min([remap(x, almanach) for x in seeds_to_plant])


def part2(data):
    pass


def do_tests():
    testdata1 = """seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4"""
    print(part1(testdata1))
    print(part2(testdata1))


if __name__ == "__main__":
    input_data = get_data(os.path.basename(__file__))

    do_tests()

    print(part1(input_data))
    print(part2(input_data))
