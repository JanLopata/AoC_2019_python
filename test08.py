import unittest

from parameterized import parameterized

import day08 as day


class AoCTest(unittest.TestCase):

    @parameterized.expand([["123456789012", 1]])
    def test_part1(self, data, expected):
        result = day.part1(data, 3, 2)
        self.assertEqual(expected, result)


if __name__ == '__main__':
    unittest.main()
