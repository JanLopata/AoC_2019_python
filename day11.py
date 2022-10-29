import os

from IntcodeComputer import IntcodeComputer, StoppingCondition


class PaintingRobot:

    def __init__(self):
        self.debug_mode = False
        self.direction_idx = 0
        self.directions = [(0, -1), (-1, 0), (0, 1), (1, 0)]
        self.position = (0, 0)
        self.environment = set()
        self.painted = set()

    def move(self):
        direction = self.get_direction()
        new_position = (self.position[0] + direction[0], self.position[1] + direction[1])
        if self.debug_mode:
            print("Moving {} -> {} by {}, dir. {}".format(self.position, new_position, direction, self.direction_idx))
        self.position = new_position

    def get_direction(self):
        return self.directions[self.direction_idx]

    def turn(self, turn_number):
        increment = -1 if turn_number == 1 else 1
        new_direction = (self.direction_idx + increment) % len(self.directions)
        if self.debug_mode:
            print("Turning to {} by {}".format(new_direction, turn_number))
        self.direction_idx = new_direction

    def paint(self, color_number):
        if self.debug_mode:
            print("Painting on {} to {}".format(self.position, color_number))
        if color_number == 1:
            self.environment.add(self.position)

        if color_number == 0 and self.position in self.environment:
            self.environment.remove(self.position)

        self.painted.add(self.position)

    def get_color_number(self):
        return 1 if self.position in self.environment else 0


def part1(data: str):
    program = [int(x) for x in data.split(",")]
    computer = IntcodeComputer()
    computer.import_program(program)
    computer.set_stop_on_output(True)
    # this encapsulation is bad
    # - the intcode computer should be inside of robot
    # - the environment should be outside of robot
    robot = PaintingRobot()
    partial_output = []

    stopping_condition = None
    while stopping_condition != StoppingCondition.END_OF_PROGRAM:

        stopping_condition = computer.compute_while_possible()
        if stopping_condition == StoppingCondition.EXPECTING_INPUT:
            # read color
            computer.accept_input([robot.get_color_number()])

        if stopping_condition == StoppingCondition.STOP_ON_OUTPUT:
            partial_output.append(computer.output[-1])
            if len(partial_output) == 1:
                robot.paint(partial_output[0])
            if len(partial_output) >= 2:
                robot.turn(partial_output[1])
                robot.move()
                partial_output.clear()

    return len(robot.painted)


def part2(data: str):
    program = [int(x) for x in data.split(",")]
    computer = IntcodeComputer()
    computer.import_program(program)


def read_data():
    with open(input_filename) as input_file:
        return input_file.read()


if __name__ == "__main__":
    this_filename = os.path.basename(__file__)
    input_filename = os.path.join("input", this_filename.replace("day", "").replace(".py", ".txt"))
    data = read_data()

    print(part1(data))
    print(part2(data))
