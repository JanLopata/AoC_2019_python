import unittest

import day20 as day

test_data1 = """broadcaster -> a, b, c
%a -> b
%b -> c
%c -> inv
&inv -> a
"""

test_data2 = """broadcaster -> a
%a -> inv, con
&inv -> b
%b -> con
&con -> output
"""


class AoCTest(unittest.TestCase):
    def test_data_1part1(self):
        result = day.part1(test_data1)
        self.assertEqual(32000000, result)

    def test_data_2part1(self):
        result = day.part1(test_data2)
        self.assertEqual(11687500, result)


if __name__ == '__main__':
    unittest.main()
