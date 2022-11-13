import os

from intcode_computer import IntcodeComputer

debug_mode = False


def interpret_screen(output, screen_map: dict):
    for i in range(int(len(output) / 3)):
        x = output[3 * i]
        y = output[3 * i + 1]
        tile_id = output[3 * i + 2]
        screen_map[(x, y)] = tile_id
        if tile_id == 0:
            screen_map.pop((x, y))

    return screen_map


def print_screen(screen_map: dict):
    if not debug_mode:
        return
    output = ""
    for i in range(24):
        for j in range(50):
            if (j, i) in screen_map:
                output += str(screen_map[(j, i)])
            else:
                output += ' '

        output += '\n'
    score = get_score(screen_map)

    print(output)
    print('Score: {}'.format(score))


def get_score(screen_map):
    return screen_map.get((-1, 0))


def part1(data: str):
    program = [int(x) for x in data.split(",")]
    computer = IntcodeComputer()
    computer.import_program(program)
    screen_map = {}
    computer.compute_while_possible()
    interpret_screen(computer.output, screen_map)
    print_screen(screen_map)
    return count_blocks(screen_map)


def part2(data: str):
    program = [int(x) for x in data.split(",")]
    program[0] = 2
    computer = IntcodeComputer()
    computer.import_program(program)

    return win_game_return_score(computer)


def count_blocks(screen_map):
    return len(find_tile_type(screen_map, 2))


def find_tile_type(screen_map, tile_type):
    return [x for x in screen_map.items() if x[1] == tile_type]


def win_game_return_score(computer):
    computer.compute_while_possible()
    screen_map = {}
    interpret_screen(computer.output, screen_map)
    print_screen(screen_map)
    previous_paddle_x, previous_ball = find_paddle_and_ball(screen_map)
    if debug_mode:
        print("Paddle: {}, ball: {}".format(previous_paddle_x, previous_ball))

    joystick_value = 0

    while count_blocks(screen_map) > 0:
        computer.accept_input([joystick_value])
        computer.reset_output()
        computer.compute_while_possible()
        interpret_screen(computer.output, screen_map)
        print_screen(screen_map)

        # decision
        paddle, ball = find_paddle_and_ball(screen_map)
        if paddle > ball[0]:
            joystick_value = -1
        elif paddle < ball[0]:
            joystick_value = 1

    return get_score(screen_map)


def find_paddle_and_ball(screen_map):
    paddle = max([int(coord[0]) for coord, _ in find_tile_type(screen_map, 3)])
    ball, _ = find_tile_type(screen_map, 4)[0]
    return paddle, ball


def read_data():
    with open(input_filename) as input_file:
        return input_file.read()


if __name__ == "__main__":
    this_filename = os.path.basename(__file__)
    input_filename = os.path.join("input", this_filename.replace("day", "").replace(".py", ".txt"))
    data = read_data()

    print(part1(data))
    print(part2(data))
