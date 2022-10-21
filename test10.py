import unittest

from parameterized import parameterized

import day10 as day

mini_data = """
#.........
...#......
...#..#...
.####....#
..#.#.#...
.....#....
..###.#.##
.......#..
....#...#.
...#..#..#
"""

test_data = [
    (8, """
.#..#
.....
#####
....#
...##
"""),
    (33, """
......#.#.
#..#.#....
..#######.
.#.#.###..
.#..#.....
..#....#.#
#..#....#.
.##.#..###
##...#..#.
.#....####
"""),
]

gcd_data = [(4, 6, 2), (1, 8, 1), (4, 16, 4), (-4, 2, 2), (4, -2, 2), (-4, -2, 2)]


class AoCTest(unittest.TestCase):
    def test_part1(self):
        for example in test_data:
            expected = example[0]
            input_data = example[1]
            result = day.part1(input_data)
            self.assertEqual(expected, result)

    def test_mini(self):
        grid_data, grid_size = day.read_grid_to_set(mini_data)
        visible_points = day.compute_visible_points((0, 0), set(grid_data), grid_size)
        self.assertEqual(7, visible_points)

    @parameterized.expand([
        [4, 6, 2],
        [1, 8, 1],
        [4, 16, 4],
        [-4, 2, 2],
        [4, -2, 2],
        [-4, -2, 2]])
    def test_gcd(self, a, b, expected):
        self.assertEqual(expected, day.gcd(a, b))


if __name__ == '__main__':
    unittest.main()
