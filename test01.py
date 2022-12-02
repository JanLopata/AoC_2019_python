import unittest

# from nose.tools import assert_equal
from parameterized import parameterized

import day01 as day

test_data = """
1000
2000
3000

4000

5000
6000

7000
8000
9000

10000
"""


class AoCTest(unittest.TestCase):

    def test_part1(self):
        self.assertEqual(24000, day.part1(test_data))

    def test_part2(self):
        self.assertEqual(45000, day.part2(test_data))


if __name__ == '__main__':
    unittest.main()
