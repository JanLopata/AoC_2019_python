import unittest

import day02

test_data = """
11-22,95-115,998-1012,1188511880-1188511890,222220-222224,
1698522-1698528,446443-446449,38593856-38593862,565653-565659,
824824821-824824827,2121212118-2121212124
"""


class AoCTest(unittest.TestCase):

    def test_part1(self):
        self.assertEqual(1227775554, day02.part1(test_data))

    def test_part2(self):
        self.assertEqual(4174379265, day02.part2(test_data))


if __name__ == '__main__':
    unittest.main()
