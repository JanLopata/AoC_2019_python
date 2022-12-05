import unittest

import day05 as day

test_data = """
    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2
"""


class AoCTest(unittest.TestCase):

    def test_part1(self):
        self.assertEqual("CMZ", day.part1(test_data))

    def test_part2(self):
        self.assertEqual("MCD", day.part2(test_data))


if __name__ == '__main__':
    unittest.main()
