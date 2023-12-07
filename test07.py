import unittest

from parameterized import parameterized

import day07 as day


class AoCTest(unittest.TestCase):
    @parameterized.expand([
        ["32T3K 0", 2],
        ["T55J5 0", 4],
        ["KK677 0", 3],
        ["KTJJT 0", 3],
        ["QQQJA 0", 4],
    ])
    def test_hand_strength(self, inp, expected):
        hand = day.HandOfCards(inp)
        self.assertEqual(expected, hand.strength)


if __name__ == '__main__':
    unittest.main()
