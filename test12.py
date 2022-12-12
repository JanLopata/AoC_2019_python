import unittest

import day12 as day

test_data = """
Sabqponm
abcryxxl
accszExk
acctuvwj
abdefghi
"""


class AoCTest(unittest.TestCase):

    def test_part1(self):
        self.assertEqual(31, day.part1(test_data))

    def test_part2(self):
        self.assertEqual(29, day.part2(test_data))


if __name__ == '__main__':
    unittest.main()
