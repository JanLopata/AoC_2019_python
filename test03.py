import unittest

import day03

test_data = """
987654321111111
811111111111119
234234234234278
818181911112111
"""

class AoCTest(unittest.TestCase):

    def test_part1(self):
        self.assertEqual(357, day03.part1(test_data))

    def test_part2(self):
        self.assertEqual(3121910778619, day03.part2(test_data))


if __name__ == '__main__':
    unittest.main()
