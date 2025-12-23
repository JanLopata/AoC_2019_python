import os

from aoc_tools import get_data


def indicators_to_number(indicators_str: str):
    result = 0
    target = 0
    revers = indicators_str[::-1]
    for c in revers:
        result *= 2
        target *= 2
        target += 1
        if c == "#":
            result += 1
    return result, target


def mask_indices_to_number(mask_indices: list[str]):
    result = 0
    for str_idx in mask_indices:
        idx = int(str_idx)
        result += 2 ** idx
    return result


def parse_line(line):
    sp = line.split()
    indicators, target_indicators = indicators_to_number(sp[0][1:-1])
    buttons = []
    for button_source in sp[1:-1]:
        mask_indices = button_source[1:-1].split(",")
        mask = mask_indices_to_number(mask_indices)
        buttons.append(mask)

    return indicators, target_indicators, buttons, None


def toggle_by_mask(indicators, all_bits_on, mask):
    to_be_toggled = indicators & mask
    without_masked = indicators - to_be_toggled
    toggled = (to_be_toggled ^ all_bits_on) & mask
    return without_masked + toggled


def find_target_by_applying_masks(indicators, target, masks):
    work_queue = []
    for mask in masks:
        switch_result = toggle_by_mask(indicators, target, mask)
        work_queue.append(([indicators, switch_result], mask))
        print(work_queue[-1])

    # while len(work_queue) > 0:





def part1(data: str):
    for line in data.splitlines():
        indicators, target, wiring, _ = parse_line(line)
        print(indicators, target, wiring)
        find_target_by_applying_masks(indicators, target, wiring)

    return 0


def part2(data: str):
    pass


if __name__ == "__main__":
    input_data = get_data(os.path.basename(__file__))

    print(part1(input_data))
    print(part2(input_data))
