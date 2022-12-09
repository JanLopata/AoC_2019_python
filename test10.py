import unittest

from parameterized import parameterized

import day10 as day

test_data = """

"""


class AoCTest(unittest.TestCase):

    def test_part1(self):
        self.assertEqual(-1, day.part1(test_data))

    @parameterized.expand([
        ["1234", 1],
    ])
    def test_parametrized_part1(self, data, expected):
        result = day.part1(data)
        self.assertEqual(expected, result)

    def test_part2(self):
        self.assertEqual(-1, day.part2(test_data))


if __name__ == '__main__':
    unittest.main()
