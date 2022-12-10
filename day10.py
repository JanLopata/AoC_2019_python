import os

from aoc_tools import get_data


class ClockCpu:
    def __init__(self):
        self.cycle = 1
        self.cycles_memory = {}
        self.value_x = 1
        self.log_frequency = 1
        self.log_start = 1

    def run(self, instruction):
        self.log_cycle()

        if instruction == "noop":
            self.cycle += 1
            self.log_cycle()
            return

        sp = instruction.split(" ")

        self.cycle += 1
        self.log_cycle()
        self.cycle += 1
        self.value_x += int(sp[1])
        self.log_cycle()

    def log_cycle(self):

        if (self.cycle - self.log_start) % self.log_frequency == 0:
            self.cycles_memory[self.cycle] = self.value_x


def draw_image(cycles_memory):
    image = [["." for _ in range(42)] for _ in range(6)]

    for cycle in range(1, 6 * 40 + 1):
        if cycle not in cycles_memory:
            continue
        sprite_main_x = cycles_memory[cycle]
        sprite_pixels = [sprite_main_x + i for i in range(-1, 2)]
        drawn_x = (cycle - 1) % 40
        y = (cycle - 1) // 40
        if drawn_x in sprite_pixels:
            image[y][drawn_x + 1] = "#"

    image_string = "\n"
    for row in image:
        image_string += "".join(row[1:-1]) + "\n"
    return image_string


def part1(data: str):
    cpu = ClockCpu()
    cpu.log_start = 20
    cpu.log_frequency = 40
    for instruction in data.splitlines():
        if instruction == "":
            continue
        cpu.run(instruction)

    return sum([key * value for key, value in cpu.cycles_memory.items()])


def part2(data: str):
    cpu = ClockCpu()
    for instruction in data.splitlines():
        if instruction == "":
            continue
        cpu.run(instruction)

    return draw_image(cpu.cycles_memory)


if __name__ == "__main__":
    data = get_data(os.path.basename(__file__))

    print(part1(data))
    print(part2(data))
