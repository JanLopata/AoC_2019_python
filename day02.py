import os

from aoc_tools import get_data

debug_part1 = False
debug_part2 = False


def bag_check(draw_record):
    for rec in draw_record:
        color = rec[0]
        count = rec[1]

        if color == "red":
            if count > 12:
                return False
        if color == "green" and count > 13:
            return False

        if color == "blue" and count > 14:
            return False

    return True


def part1(data):
    result = 0

    for line in data.splitlines():
        split1 = line.split(": ")
        game_id = int(split1[0].split()[1])
        split2 = split1[1].split("; ")
        dicts = []
        draw_record = []
        for draw in split2:
            draw_dict = {}
            for cubes in draw.split(", "):
                cubesplit = cubes.split(" ")
                color = cubesplit[1]

                count = int(cubesplit[0])
                draw_record.append([color, count])

            # dicts.append({game_id, draw_record})
        if bag_check(draw_record):
            result += game_id

    return result


def part2(data):
    pass


def do_tests():
    testdata1 = """Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"""
    testdata2 = """
    """
    print(part1(testdata1))
    print(part2(testdata2))


if __name__ == "__main__":
    input_data = get_data(os.path.basename(__file__))

    do_tests()

    print(part1(input_data))
    print(part2(input_data))
