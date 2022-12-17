import os

from aoc_tools import get_data

tiles = [
    {(0, 0), (1, 0), (2, 0), (3, 0)},
    {(0, 1), (1, 0), (1, 1), (1, 2), (2, 1)},
    {(0, 0), (1, 0), (2, 0), (2, 1), (2, 2)},
    {(0, 0), (0, 1), (0, 2), (0, 3)},
    {(0, 0), (0, 1), (1, 0), (1, 1)}
]

debug_mode = False


def shifted_tile(tile, shift):
    result = set()
    for x, y in tile:
        result.add((x + shift[0], y + shift[1]))
    return result


def tile_limits(tile):
    min_x = min(x for x, y in tile)
    max_x = max(x for x, y in tile)
    min_y = min(y for x, y in tile)
    max_y = max(y for x, y in tile)
    return min_x, max_x, min_y, max_y


DIRECTION_MAP = {'>': (1, 0), '<': (-1, 0)}


def limits_crossed(tile):
    min_x, max_x, min_y, max_y = tile_limits(tile)
    return min_x <= 0 or max_x > 7 or min_y <= 0


def filled_crossed(shifted, filled):
    return len(filled.intersection(shifted)) > 0


def print_situation(filled, tile, max_height):
    if not debug_mode:
        return

    if tile is None:
        top = max_height
    else:
        top = max(max_height, max(y for x, y in tile))

    for y in range(top + 1, -1, -1):

        for x in range(9):
            char = '.'

            if (x, y) in filled:
                char = '#'
            elif tile is not None and (x, y) in tile:
                char = '@'
            elif y == 0 or x == 0 or x == 8:
                char = '$'
            print(char, end='')
        print()
    print()


def part1(data: str):
    jets = [x for x in data.split("\n") if len(x) > 10][0]

    jets_counter = 0
    tiles_counter = 0

    filled = set()
    max_height = 0
    tile = None

    while tiles_counter < 2023:
        print_situation(filled, tile, max_height)

        if tile is None:
            tile = spawn_tile(tiles_counter, max_height)
            tiles_counter += 1
            continue

        push = DIRECTION_MAP[jets[jets_counter % len(jets)]]
        jets_counter += 1
        shifted = shifted_tile(tile, push)
        if limits_crossed(shifted) or filled_crossed(shifted, filled):
            pass
        else:
            tile = shifted

        shifted = shifted_tile(tile, (0, -1))
        if limits_crossed(shifted) or filled_crossed(shifted, filled):
            # tile stopped
            for x, y in tile:
                filled.add((x, y))
                max_height = max(max_height, y)
            tile = None
        else:
            tile = shifted

    return max_height


def spawn_tile(tiles_counter, max_height):
    tile = tiles[tiles_counter % len(tiles)]
    return shifted_tile(tile, (3, max_height + 4))


def part2(data: str):
    pass


if __name__ == "__main__":
    data = get_data(os.path.basename(__file__))

    print(part1(data))
    print(part2(data))
