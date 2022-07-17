import unittest

from parameterized import parameterized

import day06 as day

small_test_data = """
COM)B
B)C
C)D
D)E
E)F
B)G
G)H
D)I
E)J
J)K
K)L
"""

class AoCTest(unittest.TestCase):
    def test_part1(self):
        result = day.part1(small_test_data)
        self.assertEqual(42, result)

if __name__ == '__main__':
    unittest.main()
