import unittest

from day12 import part1, part2

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


if __name__ == '__main__':
    unittest.main()
