import unittest

import day04

test_data = """..@@.@@@@.
@@@.@.@.@@
@@@@@.@.@@
@.@@@@..@.
@@.@@@@.@@
.@@@@@@@.@
.@.@.@.@@@
@.@@@.@@@@
.@@@@@@@@.
@.@.@@@.@.
"""


class AoCTest(unittest.TestCase):

    def test_part1(self):
        self.assertEqual(13, day04.part1(test_data))

    def test_part2(self):
        self.assertEqual(43, day04.part2(test_data))


if __name__ == '__main__':
    unittest.main()