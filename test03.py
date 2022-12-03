import unittest

import day03 as day

test_data = """
vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw
"""


class AoCTest(unittest.TestCase):

    def test_part1(self):
        self.assertEqual(157, day.part1(test_data))

    def test_part2(self):
        self.assertEqual(70, day.part2(test_data))


if __name__ == '__main__':
    unittest.main()
