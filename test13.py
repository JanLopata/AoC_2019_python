import unittest

from parameterized import parameterized

import day13 as day

test_data = """
[1,1,3,1,1]
[1,1,5,1,1]

[[1],[2,3,4]]
[[1],4]

[9]
[[8,7,6]]

[[4,4],4,4]
[[4,4],4,4,4]

[7,7,7,7]
[7,7,7]

[]
[3]

[[[]]]
[[]]

[1,[2,[3,[4,[5,6,7]]]],8,9]
[1,[2,[3,[4,[5,6,0]]]],8,9]
"""


class AoCTest(unittest.TestCase):

    def test_part1(self):
        self.assertEqual(13, day.part1(test_data))

    # @parameterized.expand([
    #     ["1234", 1],
    # ])
    # def test_parametrized_part1(self, data, expected):
    #     result = day.part1(data)
    #     self.assertEqual(expected, result)

    def test_part2(self):
        self.assertEqual(-1, day.part2(test_data))


if __name__ == '__main__':
    unittest.main()
