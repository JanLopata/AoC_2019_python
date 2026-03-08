import unittest

from parameterized import parameterized

from day12 import part1, part2, Piece, PreparedPiece

test_data = """
0:
###
##.
##.

1:
###
##.
.##

2:
.##
###
##.

3:
##.
###
##.

4:
###
#..
###

5:
###
.#.
###

4x4: 0 0 0 0 2 0
12x5: 1 0 1 0 2 2
12x5: 1 0 1 0 3 2
"""


class AoCTest(unittest.TestCase):

    def test_part1(self):
        self.assertEqual(2, part1(test_data))

    def test_part2(self):
        self.assertEqual(0, part2(test_data))

    @parameterized.expand([
        ({(0, 0), (2, 1), (3, 2)}, {(0, 3), (1, 1), (2, 0)}),
        ({(0, 1), (1, 0), (2, 0), (2, 2), (3, 1)}, {(0, 1), (0, 2), (1, 0), (1, 3), (2, 1)})
    ])
    def test_right_rotation(self, original, expected):
        self.assertEqual(expected, Piece(original).rotate_right().get_indices())

    @parameterized.expand([
        ({(0, 0), (2, 1), (3, 2)}, {(3, 0), (1, 1), (0, 2)}),
        ({(0, 1), (1, 0), (2, 0), (2, 2), (3, 1)}, {(0, 1), (1, 0), (2, 0), (1, 2), (3, 1)})
    ])
    def test_top_down_flip(self, original, expected):
        self.assertEqual(expected, Piece(original).flip_top_down().get_indices())

    def test_variants(self):
        prepared_piece = PreparedPiece(Piece({(0, 0), (2, 1), (3, 2)}))




if __name__ == '__main__':
    unittest.main()
