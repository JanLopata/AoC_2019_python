import unittest

import day03 as day

test_data = """
"""


class AoCTest(unittest.TestCase):

    def test_part1(self):
        self.assertEqual(1, day.part1(test_data))

    def test_part2(self):
        self.assertEqual(2, day.part2(test_data))


if __name__ == '__main__':
    unittest.main()
