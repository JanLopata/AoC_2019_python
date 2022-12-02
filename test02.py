import unittest

from parameterized import parameterized

import day02 as day


test_data = """
A Y
B X
C Z
"""
class AoCTest(unittest.TestCase):

    def test_fuel_req(self):
        self.assertEqual(15, day.part1(test_data))

    def test_fuel_req2(self):
        self.assertEqual(12, day.part2(test_data))


if __name__ == '__main__':
    unittest.main()
