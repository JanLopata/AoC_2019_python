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

    joltage_source = sp[-1][1:-1]
    joltage_target = [int(x) for x in joltage_source.split(",")]

    return indicators, target_indicators, buttons, joltage_target


def toggle_by_mask(indicators, all_bits_on, mask):
    to_be_toggled = indicators & mask
    without_masked = indicators - to_be_toggled
    toggled = (to_be_toggled ^ all_bits_on) & mask
    return without_masked + toggled


def increment_by_mask(indicators: list[int], mask):
    result = indicators[::]
    for i in range(len(indicators)):
        if mask & 2 ** i > 0:
            result[i] += 1
    return result


def find_target_by_applying_masks(starting_position, all_ons, masks):
    known_values = set()
    work_queue = [(starting_position, [])]

    while len(work_queue) > 0:
        head = work_queue.pop(0)
        indicators = head[0]
        if indicators == 0:
            print(head)
            return len(head[1])

        for mask in masks:
            toggle_result = toggle_by_mask(indicators, all_ons, mask)
            if toggle_result in known_values:
                continue
            else:
                known_values.add(toggle_result)

            progress = head[1][::]
            progress.append(mask)

            work_queue.append((toggle_result, progress))


def compare_joltage(indicators, joltage_target):
    equality = False
    for i in range(len(indicators)):
        if indicators[i] > joltage_target[i]:
            return 1
        if indicators[i] < joltage_target[i]:
            equality = False

    return 0 if equality else -1


def find_joltage_target(masks, joltage_target):
    starting_indicators = [0 for x in joltage_target]
    # known_values = set()
    work_queue = [(starting_indicators, [])]

    while len(work_queue) > 0:
        head = work_queue.pop(0)
        indicators = head[0]
        comparison = compare_joltage(indicators, joltage_target)
        if comparison == 0:
            print(head)
            return len(head[1])
        if comparison > 0:
            continue

        for mask in masks:
            increased_indicators = increment_by_mask(indicators, mask)
            progress = head[1][::]
            progress.append(mask)

            work_queue.append((increased_indicators, progress))


def part1(data: str):
    result = 0
    for line in data.splitlines():
        indicators, target, wiring, _ = parse_line(line)
        result += find_target_by_applying_masks(indicators, target, wiring)

    return result


def part2(data: str):
    result = 0
    for line in data.splitlines():
        indicators, _, wiring, joltage_target = parse_line(line)
        print(indicators, wiring, joltage_target)
        result += find_joltage_target(wiring, joltage_target)

    return result


if __name__ == "__main__":
    input_data = get_data(os.path.basename(__file__))

    print(part1(input_data))
    print(part2(input_data))
