import os

from aoc_tools import get_data

debug_part1 = False
debug_part2 = False


def part1(data):
    result = 0
    for line in data.splitlines():
        card_number, matches = parse_card(line)
        if matches > 0:
            result += 2 ** (matches - 1)

        # print(line, " have matches: ", matches)

    return result


def parse_card(line):
    card_number, tips = line.split(": ")
    card_number = int(card_number.split(" ")[-1])
    winning, have = tips.split(" | ")
    winning = set([int(x) for x in winning.split(" ") if len(x) > 0])
    have = set([int(x) for x in have.split(" ") if len(x) > 0])
    matches = len([1 for x in have if x in winning])
    return card_number, matches


def part2(data):
    result = 0

    card_counts = {}
    highest = 0

    for line in data.splitlines():
        card_number, matches = parse_card(line)
        highest = card_number
        add_cart_to_cart_counts(card_counts, card_number)

        multiplier = card_counts[card_number]
        for i in range(matches):
            add_cart_to_cart_counts(card_counts, card_number + i + 1, multiplier)

    for card in card_counts:
        if card <= highest:
            result += card_counts[card]

    return result


def add_cart_to_cart_counts(card_counts, card_number, added_amount=1):
    if card_number in card_counts:
        card_counts[card_number] = card_counts[card_number] + added_amount
    else:
        card_counts[card_number] = added_amount


def do_tests():
    testdata1 = """Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11"""
    print(part1(testdata1))
    print(part2(testdata1))


if __name__ == "__main__":
    input_data = get_data(os.path.basename(__file__))

    do_tests()

    print(part1(input_data))
    print(part2(input_data))
