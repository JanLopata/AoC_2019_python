import unittest

import day05

test_data = """3-5
10-14
16-20
12-18

1
5
8
11
17
32
"""

test_data_2 = """3-5
10-14
16-20
17-17
12-18
8-8
"""

test_data_3 = """3-5
10-10
10-14
16-20
16-16
12-18
"""


class AoCTest(unittest.TestCase):

    def test_part1(self):
        self.assertEqual(3, day05.part1(test_data))

    def test_part2(self):
        self.assertEqual(14, day05.part2(test_data))

    def test_part2_special(self):
        self.assertEqual(15, day05.part2(test_data_2))

    def test_part2_special_alt(self):
        self.assertEqual(14, day05.part2(test_data_3))


if __name__ == '__main__':
    unittest.main()