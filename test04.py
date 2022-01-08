import unittest

from parameterized import parameterized

import day04 as day


class AoCTest(unittest.TestCase):

    @parameterized.expand([
        ["111111", True],
        ["223450", False],
        ["123789", False]])
    def test_part1(self, n, expected):
        self.assertEqual(expected, day.check_criterias(int(n)))

    @parameterized.expand([
        ["111111", False],
        ["112233", True],
        ["111122", True],
        ["123444", False]])
    def test_part2(self, n, expected):
        self.assertEqual(expected, day.additional_crit(int(n)))


if __name__ == '__main__':
    unittest.main()
