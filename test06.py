import unittest

from parameterized import parameterized

import day06 as day

test_data = """
"""


class AoCTest(unittest.TestCase):

    @parameterized.expand([
        ["mjqjpqmgbljsphdztnvjfqwrcgsmlb", 7],
        ["bvwbjplbgvbhsrlpgdmjqwftvncz", 5],
        ["nppdvjthqldpwncqszvftbrmjlhg", 6],
        ["nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg", 10],
        ["zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw", 11],
    ])
    def test_part1(self, data, expected):
        result = day.part1(data)
        self.assertEqual(expected, result)

    @parameterized.expand([
        ["mjqjpqmgbljsphdztnvjfqwrcgsmlb", 19],
        ["bvwbjplbgvbhsrlpgdmjqwftvncz", 23],
        ["nppdvjthqldpwncqszvftbrmjlhg", 23],
        ["nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg", 29],
        ["zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw", 26],
    ])
    def test_part2(self, data, expected):
        result = day.part2(data)
        self.assertEqual(expected, result)


if __name__ == '__main__':
    unittest.main()
