import unittest

from parameterized import parameterized

import day05
import day05 as day


class AoCTest(unittest.TestCase):

    @parameterized.expand([[[10, 20], [10, 20]], [[40, 70], [40, 50, 70]], [[10, 100], [10, 50, 98, 100]],
                           [[70, 105], [70, 98, 100, 105]]])
    def test_int_computer(self, data, expected):
        almanach_input = """50 98 2
52 50 48"""

        mapper = day05.AlmanachMapper()
        for line in almanach_input.splitlines():
            mapper.add_range(line)

        result = mapper.cut_interval(data[0], data[1])

        self.assertEqual(expected, result)

    @parameterized.expand([[[81, 95], [81, 95]]])
    def test_alm2(self, data, expected):

        almanach_input = """0 15 37
37 52 2
39 0 15"""

        mapper = day05.AlmanachMapper()
        for line in almanach_input.splitlines():
            mapper.add_range(line)

        result = mapper.cut_interval(data[0], data[1])

        self.assertEqual(expected, result)


if __name__ == '__main__':
    unittest.main()
