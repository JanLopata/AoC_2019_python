import unittest

import day04 as day

test_data = """
2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8
"""


class AoCTest(unittest.TestCase):

    def test_part1(self):
        self.assertEqual(2, day.part1(test_data))

    def test_part2(self):
        self.assertEqual(4, day.part2(test_data))


if __name__ == '__main__':
    unittest.main()
