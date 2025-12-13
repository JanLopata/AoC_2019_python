import unittest

import day08

test_data = """162,817,812
57,618,57
906,360,560
592,479,940
352,342,300
466,668,158
542,29,236
431,825,988
739,650,466
52,470,668
216,146,977
819,987,18
117,168,530
805,96,715
346,949,466
970,615,88
941,993,340
862,61,35
984,92,344
425,690,689
"""


class AoCTest(unittest.TestCase):

    def test_part1(self):
        self.assertEqual(40, day08.part1(test_data, 10))

    def test_part2(self):
        self.assertEqual(25272, day08.part2(test_data))


if __name__ == '__main__':
    unittest.main()