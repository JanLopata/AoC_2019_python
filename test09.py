import unittest

from day09 import Line, part1, part2

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
        self.assertEqual(50, part1(test_data))

    def test_part2(self):
        self.assertEqual(24, part2(test_data))

    def test_intersection(self):
        self.assertTrue(Line((2, 1), (11, 1)).intersects(Line((7, 3), (7, 1))))
        self.assertTrue(Line((2, 5), (2, 1)).intersects(Line((2, 3), (7, 3))))




if __name__ == '__main__':
    unittest.main()