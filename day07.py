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
        return 7  # five of kind

    if max(v) == 4:
        return 6  # four of kind

    if max(v) == 3:
        if len(v) == 2:
            return 5  # full-house
        else:
            return 4  # tree of kind

    if max(v) == 2:
        if len(v) == 3:
            return 3  # two-pair
        else:
            return 2  # one pair

    return 1  # highest card


def remap_joker(x, target):
    if x == 1:
        return target
    return x


class HandOfCards:

    def __init__(self, cards: str, bet: int):
        self.cards_str = cards
        self.cards = [map_card_to_number(x) for x in cards]
        self.bet = bet
        self.rank = None
        best_strength, best_joker = self.compute_strength()
        self.best_joker = best_joker
        self.strength = best_strength
        self.comparison_key = self.compute_comparison_key()

    def __str__(self):
        return "{} bet {} joker {} strength {} cards_n {} compkey {}".format(self.cards_str, self.bet, self.best_joker,
                                                                             self.strength, self.cards,
                                                                             self.comparison_key)

    def compute_strength(self):
        jokers = 0
        if 1 in self.cards:
            max_strength = 0
            best_joker = None
            # joker present - test every possibility
            for joker_value in range(2, 15):
                tmp = [remap_joker(x, joker_value) for x in self.cards]
                strength = compute_strength(tmp)
                if strength > max_strength:
                    max_strength = strength
                    best_joker = joker_value

            return max_strength, best_joker
        else:
            return compute_strength(self.cards), None

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
        split = line.split()
        hand = HandOfCards(split[0], int(split[1]))
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
    hands = []
    for line in data.splitlines():
        split = line.split()
        cards = split[0]
        # introduce joker
        cards = cards.replace("J", "1")
        hand = HandOfCards(cards, int(split[1]))
        hands.append(hand)
        # print(hand)

    hands.sort(key=lambda h: h.comparison_key)

    result = 0
    for i in range(len(hands)):
        hand = hands[i]
        hand.set_rank(i + 1)
        # print(i + 1, hand)
        result += hand.rank * hand.bet

    return result


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
