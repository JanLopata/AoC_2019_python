import os

from aoc_tools import get_data

debug_part1 = False
debug_part2 = False


def map_card_to_number(card_char):
    if card_char.isnumeric():
        return int(card_char)

    if card_char == "T":
        return 10
    if card_char == "J":
        return 11
    if card_char == "Q":
        return 12
    if card_char == "K":
        return 13
    if card_char == "A":
        return 14


def compute_strength(card_numbers: list):
    d = {}
    for c in card_numbers:
        if c in d:
            d[c] += 1
        else:
            d[c] = 1

    v = d.values()
    if max(v) == 5:
        return 7

    if max(v) == 4:
        return 6

    if max(v) == 3:
        if len(v) == 2:
            return 5  # full-house
        else:
            return 4

    if max(v) == 2:
        if len(v) == 3:
            return 3  # two-pair
        else:
            return 2

    return 1


class HandOfCards:

    def __init__(self, line: str):
        line_split = line.split()
        self.cards_str = line_split[0]
        self.cards = [map_card_to_number(x) for x in line_split[0]]
        self.bet = int(line_split[1])
        self.strength = compute_strength(self.cards)
        self.comparison_key = self.compute_comparison_key()
        self.rank = None

    def __str__(self):
        return "{} bet {} strength {} cards_n {} compkey {}".format(self.cards_str, self.bet, self.strength, self.cards,
                                                                    self.comparison_key)

    def compute_comparison_key(self):
        k = self.strength
        for c in self.cards:
            k *= 100
            k += c
        return k

    def set_rank(self, val):
        self.rank = val


def part1(data):
    result = 0

    hands = []
    for line in data.splitlines():
        hand = HandOfCards(line)
        hands.append(hand)
        # print(hand)

    hands.sort(key=lambda h: h.comparison_key)

    for i in range(len(hands)):
        hand = hands[i]
        hand.set_rank(i + 1)
        # print(i, hand)
        result += hand.rank * hand.bet

    return result


def part2(data):
    pass


def do_tests():
    testdata1 = """32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483"""
    print(part1(testdata1))
    print(part2(testdata1))


if __name__ == "__main__":
    input_data = get_data(os.path.basename(__file__))

    do_tests()

    print(part1(input_data))
    print(part2(input_data))
