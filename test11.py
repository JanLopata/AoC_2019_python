import unittest

import day11

test_data = """aaa: you hhh
you: bbb ccc
bbb: ddd eee
ccc: ddd eee fff
ddd: ggg
eee: out
fff: out
ggg: out
hhh: ccc fff iii
iii: out
"""


class AoCTest(unittest.TestCase):

    def test_part1(self):
        self.assertEqual(5, day11.part1(test_data))

    def test_part2(self):
        self.assertEqual(33, day11.part2(test_data))


if __name__ == '__main__':
    unittest.main()
