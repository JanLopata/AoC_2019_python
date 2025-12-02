import unittest

import day01

# from nose.tools import assert_equal

test_data = """
L68
L30
R48
L5
R60
L55
L1
L99
R14
L82
"""

mini_example = "R1000"


class AoCTest(unittest.TestCase):

    def test_part1(self):
        self.assertEqual(3, day01.part1(test_data))

    def test_part2(self):
        self.assertEqual(6, day01.part2(test_data))

    def test_part2_mini(self):
        self.assertEqual(10, day01.part2(mini_example))

if __name__ == '__main__':
    unittest.main()
