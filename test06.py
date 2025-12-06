import unittest

import day06

test_data = """123 328  51 64 
 45 64  387 23 
  6 98  215 314
*   +   *   +  
"""


class AoCTest(unittest.TestCase):

    def test_part1(self):
        self.assertEqual(4277556, day06.part1(test_data))

    def test_part2(self):
        self.assertEqual(3263827, day06.part2(test_data))


if __name__ == '__main__':
    unittest.main()
