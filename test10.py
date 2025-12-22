import unittest

import day10

test_data = """[.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}
[...#.] (0,2,3,4) (2,3) (0,4) (0,1,2) (1,2,3,4) {7,5,12,7,2}
[.###.#] (0,1,2,3,4) (0,3,4) (0,1,2,4,5) (1,2) {10,11,11,5,10,5}
"""


class AoCTest(unittest.TestCase):

    def test_part1(self):
        self.assertEqual(7, day10.part1(test_data))

    def test_part2(self):
        self.assertEqual(0, day10.part2(test_data))


if __name__ == '__main__':
    unittest.main()
