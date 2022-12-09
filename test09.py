import unittest

import day09 as day

test_data = """
R 4
U 4
L 3
D 1
R 4
D 1
L 5
R 2
"""

larger_data = """
R 5
U 8
L 8
D 3
R 17
D 10
L 25
U 20
"""


class AoCTest(unittest.TestCase):

    def test_part1(self):
        self.assertEqual(13, day.part1(test_data))

    def test_part2_1(self):
        self.assertEqual(1, day.part2(test_data))

    def test_part2_2(self):
        self.assertEqual(36, day.part2(larger_data))


if __name__ == '__main__':
    unittest.main()
