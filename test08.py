import unittest

from parameterized import parameterized

import day08 as day

test_data = """
30373
25512
65332
33549
35390
"""


class AoCTest(unittest.TestCase):

    def test_part1(self):
        self.assertEqual(21, day.part1(test_data))

    def test_part2(self):
        self.assertEqual(8, day.part2(test_data))


if __name__ == '__main__':
    unittest.main()
