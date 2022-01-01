import unittest

# from nose.tools import assert_equal
from parameterized import parameterized

import day01


class AoCTest(unittest.TestCase):

    @parameterized.expand([[12, 2], [14, 2], [1969, 654], [100756, 33583]])
    def test_fuel_req(self, mass, expected):
        self.assertEqual(expected, day01.compute_fuel_req(mass))

    @parameterized.expand([[14, 2], [1969, 966], [100756, 50346]])
    def test_combined_fuel_req(self, mass, expected):
        self.assertEqual(expected, day01.compute_combined_fuel_req(mass))


if __name__ == '__main__':
    unittest.main()
