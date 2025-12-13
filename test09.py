import unittest

import day09

test_data = """7,1
11,1
11,7
9,7
9,5
2,5
2,3
7,3
"""


class AoCTest(unittest.TestCase):

    def test_part1(self):
        self.assertEqual(50, day09.part1(test_data))

    def test_part2(self):
        self.assertEqual(0, day09.part2(test_data))


if __name__ == '__main__':
    unittest.main()